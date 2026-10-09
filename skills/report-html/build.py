#!/usr/bin/env python3
"""研报 Markdown → 单文件 HTML。纯标准库，零依赖，输出自包含（离线可看）。

用法:
    python3 build.py 报告.md [-o 报告.html] [--title 标题] [--strict]

退出码: 0 通过 / 1 自检不合格（不写文件） / 2 用法错误
主题: 改同目录的 theme.css（顶部变量区），本脚本只负责内联它。
"""
import argparse
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(HERE, "theme.css")

# 引用 ID 形如 [N3] [U13] [D1]（本 skill 与 industry-research 的国别前缀约定）
CITE_ID = r"[A-Za-z]\d{1,2}"
CITE_RE = re.compile(r"\[(" + CITE_ID + r")\]")
# 裸 URL：前面是引号/等号/斜杠/尖括号的一律不碰（那些是已生成属性里的 URL）
AUTOLINK_RE = re.compile(r'(?<!["\'=/>])(https?://[^\s]+?)(?=[\s，。；：）)】,;]|$)')
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")
# 来源条目行（"- N1 / 标题 / 发布方 / ..."）→ 打上 id="src-N1"，供正文引用跳转
SRC_LI_RE = re.compile(r"^(" + CITE_ID + r")\s*/")
TOC_LEVELS = (2, 3)  # 目录收录的标题层级


# ---------------------------------------------------------------- 行内
def inline(s, stash):
    s = re.sub(r"<br\s*/?>", "\x03", s, flags=re.I)          # 允许表格里写 <br>
    s = re.sub(r"`([^`]+)`", lambda m: _keep(m.group(1), stash), s)
    s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!~>|])", lambda m: _hold(m.group(1), stash), s)
    # 链接必须在 html.escape **之前**抠出来，否则三个 bug 一起发作：
    #   ① & 先变成 &amp;，而自动链接的终止符集合含 ";"，于是在第一个 "&amp;" 处截断
    #      → 所有带查询参数的 URL 都变成坏链（实测 8/13）
    #   ② URL 里的 * 先被强调解析吃掉 → 公众号 signature 参数自带 *，把 URL 切成 <em>
    #   ③ 代码块内容（_keep）会被二次转义成 &amp;amp;
    s = re.sub(r"!?\[([^\]]*)\]\(([^)\s]+)\)",
               lambda m: _link(m.group(2), m.group(1), stash), s)
    s = AUTOLINK_RE.sub(lambda m: _link(m.group(1), "", stash), s)
    s = html.escape(s, quote=False)
    s = s.replace("\x03", "<br>")
    s = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = CITE_RE.sub(lambda m: '<a class="cite" href="#src-%s">%s</a>' % (m.group(1), m.group(1)), s)
    return s


def _link(url, text, stash):
    """生成链接并暂存 —— 在此处自行转义，之后不再参与强调/链接解析。"""
    stash.append('<a class="u" href="%s">%s</a>'
                 % (html.escape(url, quote=True), html.escape(text or url, quote=False)))
    return "\x00%d\x00" % (len(stash) - 1)


def _keep(code, stash):
    stash.append("<code>%s</code>" % html.escape(code, quote=False))
    return "\x00%d\x00" % (len(stash) - 1)


def _hold(literal, stash):
    """反斜杠转义：原样输出该字符，不让它参与后续标记匹配。"""
    stash.append(literal)
    return "\x00%d\x00" % (len(stash) - 1)


def restore(s, stash):
    # 索引从大到小还原：高索引内容里可能嵌着低索引占位符
    for i in range(len(stash) - 1, -1, -1):
        s = s.replace("\x00%d\x00" % i, stash[i])
    return s


# ---------------------------------------------------------------- 表格
def _cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def _aligns(sep):
    out = []
    for c in sep.strip("|").split("|"):
        c = c.strip()
        out.append(' style="text-align:center"' if c.startswith(":") and c.endswith(":")
                   else ' style="text-align:right"' if c.endswith(":") else "")
    return out


# ---------------------------------------------------------------- 列表（支持嵌套）
def _build_tree(items):
    """items: [(indent, ordered, content)] → 嵌套树"""
    def rec(i, indent):
        nodes = []
        while i < len(items):
            ind, ordered, content = items[i]
            if ind < indent:
                break
            if ind > indent:          # 缩进跳级：归到上一项的子树里
                break
            node = {"ordered": ordered, "content": content, "children": []}
            i += 1
            if i < len(items) and items[i][0] > indent:
                node["children"], i = rec(i, items[i][0])
            nodes.append(node)
        return nodes, i
    tree, _ = rec(0, items[0][0])
    return tree


def _render_tree(nodes, stash):
    out, cur = [], None
    for n in nodes:
        tag = "ol" if n["ordered"] else "ul"
        if cur != tag:
            if cur:
                out.append("</%s>" % cur)
            out.append("<%s>" % tag)
            cur = tag
        inner = inline(n["content"], stash)
        if n["children"]:
            inner += _render_tree(n["children"], stash)
        sm = SRC_LI_RE.match(n["content"])
        attr = ' id="src-%s"' % sm.group(1) if (sm and not n["children"]) else ""
        out.append("<li%s>%s</li>" % (attr, inner))
    if cur:
        out.append("</%s>" % cur)
    return "".join(out)


# ---------------------------------------------------------------- 主转换
def convert(md, toc_levels=TOC_LEVELS):
    lines = md.split("\n")
    out, toc, stash = [], [], []
    i, n, hid = 0, len(lines), 0
    list_open = None

    while i < n:
        line = lines[i]

        if line.startswith("```"):                                  # 围栏代码块
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i], quote=False))
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % "\n".join(buf))
            continue

        if re.match(r"^ {0,3}(-{3,}|\*{3,}|_{3,})\s*$", line):       # 水平线
            out.append("<hr>")
            i += 1
            continue

        if line.startswith("|") and i + 1 < n and SEP_RE.match(lines[i + 1]):   # 表格
            align = _aligns(lines[i + 1])
            head = _cells(line)
            i += 2
            body = []
            while i < n and lines[i].startswith("|"):
                body.append(_cells(lines[i]))
                i += 1

            def row(cs, tag):
                tds = []
                for k, c in enumerate(cs):
                    a = align[k] if k < len(align) else ""
                    tds.append("<%s%s>%s</%s>" % (tag, a, restore(inline(c, stash), stash), tag))
                return "<tr>%s</tr>" % "".join(tds)

            # tw = 横向滚动容器；fade = 右缘渐隐提示；scrollhint = 文字提示（仅在实际溢出时由 JS 显示）
            out.append('<div class="twrap"><div class="tw"><table><thead>'
                       + row(head, "th") + "</thead><tbody>")
            out += [row(b, "td") for b in body]
            out.append('</tbody></table></div><span class="fade" aria-hidden="true"></span>'
                       '<div class="scrollhint">← 左右滑动查看 →</div></div>')
            continue

        m = HEAD_RE.match(line)
        if m:                                                        # 标题
            lvl, text = len(m.group(1)), m.group(2)
            hid += 1
            out.append('<h%d id="h%d">%s</h%d>' % (lvl, hid, restore(inline(text, stash), stash), lvl))
            if lvl in toc_levels:
                toc.append((lvl, "h%d" % hid, text))
            i += 1
            continue

        if line.startswith(">"):                                     # 引用块（可嵌套）
            buf = []
            while i < n and lines[i].startswith(">"):
                s = lines[i]
                buf.append(s[1:].lstrip(" ") if s.startswith("> ") else s[1:])
                i += 1
            inner, _ = convert("\n".join(buf), toc_levels)
            out.append("<blockquote>%s</blockquote>" % inner)
            continue

        m = LIST_RE.match(line)
        if m:                                                        # 列表（含嵌套 / 续行）
            items = []
            while i < n:
                mm = LIST_RE.match(lines[i])
                if mm:
                    items.append((len(mm.group(1)),
                                  bool(re.match(r"\d", mm.group(2))),
                                  mm.group(3)))
                    i += 1
                elif not lines[i].strip():
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    nm = LIST_RE.match(lines[j]) if j < n else None
                    if nm and len(nm.group(1)) >= items[-1][0]:
                        i = j
                    else:
                        break
                elif lines[i].startswith(("  ", "\t")) and items:
                    items[-1] = (items[-1][0], items[-1][1],
                                 items[-1][2] + " " + lines[i].strip())
                    i += 1
                else:
                    break
            if list_open:
                list_open = None
            out.append(_render_tree(_build_tree(items), stash))
            continue

        if not line.strip():                                         # 空行
            i += 1
            continue

        out.append("<p>%s</p>" % restore(inline(line, stash), stash))  # 段落
        i += 1

    # 出口统一还原 —— 列表（_render_tree）内部从不调 restore，源码行/列表里的
    # URL 和行内代码会以 \x00N\x00 占位符形态漏进输出（表现为「链接凭空消失」）。
    # 在这里兜底，比在每个分支各还原一次可靠：append 进 out 的内容一律已还原。
    return restore("\n".join(out), stash), toc


# ---------------------------------------------------------------- 自检
def selfcheck(md, out_html):
    errors, warns = [], []
    cited = set(CITE_RE.findall(md))
    listed = set(re.findall(r'<li id="src-(' + CITE_ID + r')">', out_html))

    dangling = cited - listed
    if dangling:
        errors.append("悬空引用：正文引用了但来源锚点不存在 → %s" % sorted(dangling))
    uncited = listed - cited
    if uncited:
        warns.append("来源已列出但正文未引用（%d 条）→ %s" % (len(uncited), sorted(uncited)))

    # 内部占位符泄漏（回归护栏）：
    #   \x00N\x00 是 inline()/stash 的暂存占位符，正常应全部还原成 HTML。
    #   漏一个就说明某条渲染分支忘了调 restore() —— 表现是「链接/代码凭空消失」，
    #   而 href 计数看起来还很正常，极难靠肉眼发现。这条就是为此设的。
    leaked = re.findall(r"\x00\d+\x00", out_html)
    if leaked:
        errors.append("内部占位符泄漏 %d 处（有分支没调 restore）→ %s"
                      % (len(leaked), sorted(set(leaked))[:3]))

    # 链接完整性（回归护栏）：
    #   href 里混入 < > = URL 被强调/链接解析吃掉；以 & 或 &amp 结尾 = 在 & 处被截断
    hrefs = re.findall(r'href="([^"]*)"', out_html)
    broken = [h for h in hrefs if "<" in h or ">" in h]
    if broken:
        errors.append("链接被破坏：href 里混入了 HTML 标记 → %s" % broken[:3])
    trunc = [h for h in hrefs if h.endswith("&amp") or h.endswith("&")]
    if trunc:
        errors.append("链接疑似被截断（以 & 结尾）→ %s" % trunc[:3])

    # 残留 markdown（只在「会被渲染的文本」里查）
    # 剔除顺序有讲究，四类都不是可见正文，误报全出在这里：
    #   style/script —— CSS 注释里写个强调符号就会被当成残留（踩过）
    #   pre>code、code —— 代码块/行内代码本就该原样保留
    #   ="..." 属性值 —— URL 里带 * 或 # 是正常的
    stripped = re.sub(r"<style\b.*?</style>", "", out_html, flags=re.S | re.I)
    stripped = re.sub(r"<script\b.*?</script>", "", stripped, flags=re.S | re.I)
    stripped = re.sub(r"<pre><code>.*?</code></pre>", "", stripped, flags=re.S)
    stripped = re.sub(r"<code>.*?</code>", "", stripped, flags=re.S)
    stripped = re.sub(r'="[^"]*"', '=""', stripped)
    for pat, name in [(r"\*\*", "**"), (r"(?m)^#{1,6}\s", "#"), (r"\]\(", "](md链接"),
                      (r"(?m)^\|", "表格竖线"), (r"`", "反引号")]:
        if re.search(pat, stripped):
            errors.append("残留未转换的 Markdown：%s" % name)

    # 外部依赖（输出必须自包含）
    for pat, name in [(r"<link\b", "<link>"), (r"<script[^>]+src=", "<script src>"),
                      (r"@import", "@import"), (r'<img[^>]+src="https?://', "远程图片")]:
        if re.search(pat, out_html):
            errors.append("输出不自包含：发现 %s" % name)

    return errors, warns


def check_toc(toc, out_html):
    bad = [aid for _, aid, _ in toc if ('id="%s"' % aid) not in out_html]
    return ["目录锚点缺失：%s" % bad] if bad else []


# ---------------------------------------------------------------- 组装
def build_toc(toc):
    items = []
    for lvl, aid, text in toc:
        plain = re.sub(r"\*\*|`", "", text)
        plain = CITE_RE.sub("", plain).strip()
        items.append('<a class="lv%d" href="#%s">%s</a>' % (lvl, aid, html.escape(plain)))
    return "\n".join(items)


TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div class="layout">
<nav class="toc"><div class="ttl">目录</div>
{toc}
</nav>
<main>
{body}
</main>
</div>
<script>
(function(){{
  var links=[].slice.call(document.querySelectorAll('nav.toc a'));
  var targets=links.map(function(a){{return document.querySelector(a.getAttribute('href'))}});
  function onScroll(){{
    var y=window.scrollY+90,best=-1;
    targets.forEach(function(t,i){{if(t&&t.offsetTop<=y)best=i;}});
    links.forEach(function(a,i){{
      a.style.background = i===best ? 'var(--thead)' : '';
      a.style.borderLeftColor = i===best ? 'var(--accent)' : 'transparent';
    }});
  }}
  window.addEventListener('scroll',onScroll,{{passive:true}});onScroll();
  var nav=document.querySelector('nav.toc'),m=window.matchMedia('(max-width:900px)');
  function sync(){{nav.classList.toggle('collapsed',m.matches);m.matches?nav.setAttribute('data-collapsible',''):nav.removeAttribute('data-collapsible');}}
  m.addEventListener('change',sync);sync();
  var b=document.createElement('button');
  b.textContent='目录';b.className='tocbtn';
  b.onclick=function(){{nav.classList.toggle('open');}};
  nav.insertBefore(b,nav.firstChild);
  // 表格横向溢出检测：只在真的能横滑时才显示提示，塞得下就一动不动
  [].forEach.call(document.querySelectorAll('.twrap'),function(w){{
    var tw=w.querySelector('.tw');
    function upd(){{
      var over=tw.scrollWidth>tw.clientWidth+2;
      w.classList.toggle('scrollable',over);
      w.classList.toggle('at-end',tw.scrollLeft+tw.clientWidth>=tw.scrollWidth-2);
    }}
    tw.addEventListener('scroll',upd,{{passive:true}});
    window.addEventListener('resize',upd);
    window.addEventListener('load',upd);
    upd();
  }});
}})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="研报 Markdown → 单文件 HTML")
    ap.add_argument("md")
    ap.add_argument("-o", "--out")
    ap.add_argument("--title")
    ap.add_argument("--strict", action="store_true", help="把警告也视为错误")
    a = ap.parse_args()

    if not os.path.isfile(a.md):
        print("找不到输入文件: %s" % a.md, file=sys.stderr)
        return 2
    md = open(a.md, encoding="utf-8").read()
    out_path = a.out or os.path.splitext(a.md)[0] + ".html"

    title = a.title
    if not title:
        m = HEAD_RE.match(md.split("\n", 1)[0])
        title = re.sub(r"\*\*|`", "", m.group(2)) if m else "研报"

    css = open(THEME, encoding="utf-8").read() if os.path.isfile(THEME) else ""
    if not css:
        print("警告: 未找到 theme.css，将输出无样式页面", file=sys.stderr)

    body, toc = convert(md)
    out_html = TEMPLATE.format(title=html.escape(title), css=css,
                               toc=build_toc(toc), body=body)

    errors, warns = selfcheck(md, out_html)
    errors += check_toc(toc, out_html)

    for w in warns:
        print("警告: %s" % w, file=sys.stderr)
    if errors or (a.strict and warns):
        print("\n自检未通过，未写出文件：", file=sys.stderr)
        for e in errors:
            print("  ✗ %s" % e, file=sys.stderr)
        for w in (warns if a.strict else []):
            print("  ✗ (--strict) %s" % w, file=sys.stderr)
        return 1

    open(out_path, "w", encoding="utf-8").write(out_html)
    print("✓ %s  →  %s" % (a.md, out_path))
    print("  标题 %d 个（目录 %d 条）· 引用 %d 处 · 来源 %d 条 · 表格 %d 张 · %.1f KB"
          % (len(re.findall(r"<h[1-6] ", out_html)), len(toc),
             len(re.findall('class="cite"', out_html)),
             len(re.findall(r'<li id="src-', out_html)),
             len(re.findall(r"<table>", out_html)),
             len(out_html.encode()) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
