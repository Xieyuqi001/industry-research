#!/usr/bin/env bash
# 把本仓库的两个 skill 安装到 Claude Code 的 skills 目录。
#
#   ./install.sh
#
# 目标目录默认 ~/.claude/skills，可用环境变量覆盖：
#   CLAUDE_SKILLS_DIR=/path/to/skills ./install.sh
#
# 已存在同名 skill 时会先备份（加时间戳后缀），不会静默覆盖。

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

if [ ! -d "$SRC" ]; then
  echo "找不到 skills/ 目录：$SRC" >&2
  exit 1
fi

mkdir -p "$DEST"

for name in industry-research report-html; do
  target="$DEST/$name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    backup="$target.bak-$(date +%Y%m%d-%H%M%S)"
    echo "已存在 $target → 备份到 $backup"
    mv "$target" "$backup"
  fi
  cp -R "$SRC/$name" "$target"
  echo "✓ $name → $target"
done

echo
echo "装好了。在 Claude Code 里说「帮我看看光伏行业」即可触发 industry-research。"
echo "skills 目录：$DEST"
