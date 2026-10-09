# 光刻机设备 · 全球行业研究报告

**数据截至 2026-10-09 | 深度：完整深度 | 覆盖：全球主要市场**
**重点国家/地区：荷兰、日本、德国、美国、中国、台湾**

---

## 1. 行业界定

本报告覆盖**半导体光刻（曝光）设备**，即把电路图形转移到晶圆上的专用装备，具体含：

- **整机**：EUV（极紫外，13.5nm）、ArF 浸没式 / ArF 干式、KrF、i-line 光刻机（scanner / stepper）。
- **上游核心零部件与子系统**：光源系统、投影与照明光学系统、双工件台、超高真空系统、激光干涉计量。
- **上游关键材料**：光刻胶、掩模基板（mask blanks）、光掩模、相关电子特气——仅在与光刻机供给能力直接相关的环节涉及。

**不含**：刻蚀、薄膜沉积、量测检测等非光刻工序设备（同属晶圆制造设备 WFE，仅在对照处提及）；不含光刻胶等材料的完整品种谱系；不含面板（FPD）曝光设备的独立分析。

---

## 2. 全球产业链地图

### 2.1 全球总量级锚点

- **全球晶圆制造设备（WFE）销售额 2025 年 1,350.6 亿美元，同比 +15%，创历史新高** [U7][J4][T4]。
- 按 SEMI 区域口径的 2025 年设备支出分布：**中国大陆约 493 亿美元**、**台湾 315.0 亿美元（+90%）**、**韩国约 257 亿美元（+26%）**、**北美 108.9 亿美元（−20%）**、**日本 95.2 亿美元（+22%）**、欧洲 28.6 亿美元 [U7][J4][T4]。
- **光刻机细分市场**：2025 年约 **350 亿美元**，2026 年预计 **392 亿美元** [C2]。⚠️ **该细分市场各机构口径分歧极大**（另有机构给出显著更低的估算），差异源于是否计入先进封装设备与售后服务收入，横向引用时必须注明口径。
- **EUV 装机**：ASML 累计出货 EUV 逾 300 台，**台积电单独占逾 50%（约 157 台）**——此为机构推估，ASML 不按客户披露 [T14]。

### 2.2 国别识别 + 五轴角色标注

| 国家/地区 | 上游资源 | 中游制造 | 下游需求 | 技术研发 | 资本上市地 | 综合角色 |
|---|---|---|---|---|---|---|
| **荷兰** | — | ● **整机垄断** | — | ● **EUV 唯一** | ● ASML | 整机供给 + 管制守门人 |
| **日本** | ● **材料寡头** | ○ 整机第二梯队 | ○ 全球第 5 | ○ ArF 浸没第二家 | ● 多家东证 Prime | 材料霸主 + 整机退守 |
| **德国** | ○ 镜坯等 | ● **核心零部件** | ○ 净进口 | ● **EUV 光学/激光垄断** | ✗ 两家均未上市 | 不可替代的子系统 |
| **美国** | — | ○ 非光刻 WFE | ○ 约占全球 8% | ● **EUV 光源 + 规则制定** | ● 最大资本池 | 技术源头 + 规则制定者 |
| **中国** | ○ 稀土/特气 | ○ 整机追赶 | ● **全球最大采购** | ○ 追赶（90nm 量产） | ● A 股板块 | 最大需求 + 追赶者 |
| **台湾** | — | ○ 光罩盒等配套 | ● **全球第二大** | — | ● 台积电 | 先进制程需求轴 |

**筛选规则说明**：本行业主导轴为**技术/资本型 + 制造型**。按「五轴任一有实质份额即入围」，候选池含荷、日、德、美、中、台、韩七方；韩国（2025 年设备支出 257 亿美元、ASML 收入占比 25.0%）与台湾高度同质（均为先进制程需求轴），取份额更大的台湾入选，韩国在跨国产能分布中体现。制造国（荷/日/中）与需求国（台）均已覆盖。

### 2.3 供应链依赖与卡脖子关系

一台 EUV 光刻机的价值集中在少数**全球唯一节点**上：

```
ASML（荷兰 · 总装集成，唯一 EUV 供应商）
  ├─ 投影/照明光学系统 ← Carl Zeiss SMT（德国）  ← 全球唯一 [D1][D4]
  │     └─ 镜坯玻璃陶瓷 ← Schott Zerodur（德国）
  ├─ 高功率 CO₂ 驱动激光 ← TRUMPF 通快（德国）  ← 独家供应商 [D2][D3]
  ├─ EUV 光源模块 ← Cymer（美国 · ASML 全资子公司） [U8]
  └─ 双工件台 / 真空 / 计量 ← ASML 自研 + 外部（Edwards、VAT、是德科技等）
```

**关键依赖结论**：

1. **德国握有对 ASML 供应链的实质否决权**——即便 ASML 与荷兰政府批准出口，德国可拒发蔡司反射镜或通快激光的许可，从而卡死整机出口 [D6]。这是「荷兰垄断整机」这一表象下更深一层的卡点。
2. **美国以「含美国原产技术」为管辖支点**——EUV 光源来自 Cymer（美国），构成美国对 ASML 对华出口行使管辖权的技术依据 [U8][U6]。
3. **日本卡在材料端**——掩膜基板日系 3 家占 96%、光刻胶日系 5 家占 91–92% [J5]。
4. **中国的敞口在需求端而非供给端**——2025 年进口半导体设备 391.66 亿美元中光刻机占 27%（106.2 亿美元），但本土自给率仅约 2.5% [C3][C2]。

---

## 3. 分国别深潜

### 3.1 荷兰 — 整机垄断者与管制守门人

**角色定位**：技术（EUV 唯一）+ 上游制造（整机总装）+ 资本（ASML 上市地）三重角色叠加。ASML 总部位于 Veldhoven，自述为行业「领先供应商」，在 20-F 中把光刻定义为半导体制造的关键工序 [N3]。

**代表公司**：ASML Holding N.V.（Euronext Amsterdam: **ASML** / NASDAQ: **ASML**），FY2025 员工逾 44,500 FTE [N2][N3]。上游依赖：Carl Zeiss SMT（德，光学**排他性**供应）、Cymer（美，光源，ASML 子公司）、ASML Berlin GmbH [N3]。

**产能 · 市场规模**
- FY2025 总净销售额 **€32,667M（+15.6%）**，其中净系统销售 €24.5bn、服务与现场选项 €8.2bn；毛利率 52.8%；净利润 **€9,609M**；基本 EPS €24.73。（已披露事实）[N1][N3]
- FY2025 出货 **327 台**（2024 年为 418 台），其中**确认收入的 EUV 系统 48 台**（2024 年 44 台）[N3]。
- 2025 年末在手订单 **€38.8bn**；Q4 2025 净订单 €13.2bn（EUV 占 €7.4bn）[N1]。
- Q2 2026：净销售额 €9,326M、毛利率 54.0%、净利润 €2,918M、新增光刻系统 86 台 [N2]。
- 产能指引（**公司 guidance，属预测**）：2026 年 low-NA EUV 约 **65 台**，2027、2028 各再 +30%；浸没式 DUV 2026 约 **130 台** [N2]。
- 市场份额：JPMorgan 口径 2025 年约 **95%**（二手券商口径，非 ASML 披露；20-F 仅称 "leading supplier"）[N11]。

**估值**（NASDAQ 美元口径，TTM，时点 2026-10-09）
- 市值约 **US$722.8bn**；**PE(TTM) 57.8**、forward PE 33.2、**PB 28.2**、PS 17.4、EV/EBITDA 45.2 [N9]。
- 历史分位：GuruFocus 十年 PE(TTM) 区间 **21.95–64.41**、中位数约 **36.4**，当前读数高于中位数约 **44%**，处历史偏高区间 [N10]。
- 口径提示：集团以欧元记账（FY2025 基本 EPS €24.73）[N1]，美股估值已换算为美元，两口径不可直接混用。

**政策 · 监管 · 关税 · 补贴**
- 荷兰国别出口管制 **2023-09-01 生效**；**2024-09-07 扩展至 DUV 浸没式光刻设备**；**2025-01-15 再收紧**，纳入特定量测/检测设备，2025-04-01 生效。属**逐案审批的许可制**（非出口禁令），适用于自荷兰输往 EU 以外目的地 [N5][N6][N3]。
- 欧盟层面：2025 年 11 月将荷兰国家管制并入 **EU Control List**，把 DUV 浸没式等许可要求扩展至全欧盟（对 ASML 无实质变化）[N3]。
- 美国因素：**MATCH Act** 拟通过外交「协调」盟友管制并具**域外效力**，**荷兰政府明确反对其域外性**，警告可能实质削弱包括荷兰企业在内的市场地位 [N7]。

**本土竞争格局**
- 荷兰境内 ASML 为**唯一光刻整机厂商**，无本土第二家 [N11]。
- 护城河 = 唯一 EUV 供应商 + 与蔡司 SMT 的排他光学供应；但该独家关系本身被 20-F 列为**供应链风险** [N3]。
- 收入地理集中（FY2025 分地区净销售额）：**中国 €9,519.7M（29.1%）、台湾 €8,337.9M（25.5%）、韩国 €8,159.6M（25.0%）、美国 €4,089.1M（12.5%）、日本 €1,420.9M** [N3]。较 2024 年中国占比 36.1% 明显回落 [N3]。
  ⚠️ **口径分歧**：荷兰议会答覆称 2025 年中国占 ASML 收入约 **33%**，与 20-F 的 29.1% 不同 [N7]；两者可能分别对应「净系统销售」与「总净销售」，引用须注明口径。

---

### 3.2 日本 — 材料寡头与退守的整机第二梯队

**角色定位**：**上游材料是全球最强、最不可替代的一轴**；中游整机已从霸主退为缝隙角色；本土需求居全球第 5；资本层有多家东证 Prime 上市公司。

**代表公司**：尼康 Nikon（7731）、佳能 Canon（7751）、东京电子 Tokyo Electron（8035）、信越化学（4063）、HOYA（7741）、东京応化（4186）[J1][J2][J9][J10][J11][J12]。

**产能 · 市场规模**
- **上游材料份额（METI 令和 7 年度委托调查，引 2019 年口径）**：**掩膜基板** 日系 3 家合计 **96%**（市场 942 亿日元）；**光刻胶** 日系 5 家合计 **91–92%**（市场 2,015 亿日元）；光掩膜日系 3 家 37%、CMP 浆料日系 5 家 43% [J5]。（属结构性数据，年份较旧）
- **佳能**：2025 年半导体光刻机出货 **234 台**（KrF 46 + i-line 188）、FPD 33 台；2026 年指引半导体 224 台（KrF 71 + i-line 153）[J3]。佳能 2025 年宇都宫新厂使光刻机产能达 2024 年的 **1.5 倍** [J13]。
- **尼康**：FY2026/3 半导体 **22 台新机 + 5 台二手**、FPD 32 台；FY2027/3 指引 23+6 台、FPD 27 台 [J1]。⚠️ 佳能以 i-line/KrF 后道机为主、尼康含 ArF，均价差异大，**台数不可简单横比** [J1][J3]。
- 日本作为设备采购地：2025 年 95.2 亿美元（+22%），约占全球 7%，居全球第 5 [J4]。产能由 TSMC 熊本（JASM）、Rapidus 拉动 [J14]。
- 尼康 **2025 年 9 月关闭运营 58 年的横滨制作所**，光刻业务进一步收缩 [J15]。

**估值**（2026-10-09，Yahoo!ファイナンス 实时；**PER 为「公司预想」口径，非 TTM**）

| 公司 | 代码 | 市值 | PER（公司预想） | PBR（实绩连） | 股息率 |
|---|---|---|---|---|---|
| 尼康 | 7731 | 6,251 亿日元 | 61.73 倍 ⚠️ 因一次性损失失真 | 1.04 倍 | — |
| 佳能 | 7751 | 6.28 万亿日元 | 12.00 倍 | 1.15 倍 | 3.40% |
| 东京电子 | 8035 | 29.12 万亿日元 | 未披露 | 13.36 倍 | — |
| 信越化学 | 4063 | 12.08 万亿日元 | 21.54 倍 | 2.49 倍 | 2.24% |
| 东京応化 | 4186 | 11,929 亿日元 | 26.27 倍 | 4.52 倍 | 0.86% |
| HOYA | 7741 | 8.39 万亿日元 | 未披露 | 8.25 倍 | — |

来源 [J7]–[J12]（尼康的失真说明见 [J1]）。**历史分位未能取得**（该数据源未提供）。PS 未披露故不列。

**政策 · 监管 · 关税 · 补贴**
- **出口管制**：经产省 2023-05-23 公布、**2023-07-23 施行**，将先端半导体制造装置等 **23 个项目**纳入出口管理，分 6 类：清洗 3、成膜 11、热处理 1、**光刻 4**（含 EUV 相关制造装置、涂布显影、掩膜制造设备）、刻蚀 3、检查 1；对华出口由「一般概括许可」降为**逐案申请** [J6]。
- **补贴**：日本半导体战略累计投入约 **5.7 万亿日元**，其中 TSMC 熊本（JASM）约 **1.2 万亿日元**、Rapidus 累计约 **2.3 万亿日元**（目标 2027 年最尖端量产）[J14]。
- **关税**：尼康 FY2026/3 受关税影响营业利润 **−68 亿日元** [J1]。

**本土竞争格局**
- 光刻整机呈**双雄均边缘化、佳能反超尼康**：ASML 占曝光设备金额份额 9 成以上；**佳能按台数约占 3 成**，且在后道先进封装曝光对台积电出货、份额「压倒性」[J13]；台数上佳能半导体机（234 台）约为尼康（22 台）的 10 倍 [J1][J3]。
- 尼康仍是 **ASML 之外唯一的 ArF 浸没式供应商**，但已终止 EUV 商业化开发 [J13][J1]。
- 上游材料寡头格局稳固（见上）；设备端由东京电子在涂布显影（光刻工序核心）领跑 [J9]。

---

### 3.3 德国 — 不可替代的子系统与「隐形否决权」

**角色定位**：**上游核心零部件技术垄断方，而非整机厂**——没有一个德国公司造整台光刻机，但 EUV 最关键的「眼睛」（蔡司反射镜）与「心脏」（通快驱动激光）都产自德国。同时是设备**净进口国**；**资本轴缺位**（两大皇冠资产均未上市）。

**代表公司**
- **Carl Zeiss SMT GmbH**（Oberkochen）：产 EUV/DUV 成像与照明光学系统、光罩方案、过程控制；员工 4,000+。母公司 **Carl Zeiss AG 未上市**（由 Carl-Zeiss-Stiftung 基金会 100% 持有），**ASML 持 SMT 24.9%** [D1][D4]。
- **TRUMPF 通快**（Ditzingen）：EUV 高功率驱动激光**独家供应商**，家族企业、**未上市** [D2][D3]。
- 上市可比标的（法兰克福）：**Aixtron SE（AIXA）**、**Süss MicroTec SE（SMHN）**、**Jenoptik AG（JEN）**[D9][D10][D11]。蔡司系唯一上市实体 Carl Zeiss Meditec（AFX）属医疗，与光刻无关。

**产能 · 市场规模**
- **蔡司 SMT FY2024/25 营收 €5.055bn（+23%）**，为蔡司四大板块中最大、增长最快 [D1]。
- 蔡司集团 FY2024/25 营收 **€11.896bn（+9%）**、EBIT €1.552bn（利润率 13%）、研发占营收 **15%**、员工 46,622 人 [D1]。
- **通快 FY2024/25 营收 €4.3bn（−16%）**、订单 €4.2bn（−7%）、EBIT €59m（利润率 1.4%）；**EUV 板块营收 €724m（−23%）**，主因 ASML 因产能过剩减少采购 [D2]。
- 德国 WFE 市场 2026 年估算 €3.8–4.2bn，贸易逆差 €2.5–3.0bn（估算/预测口径）[D8]。

**估值**
- **蔡司 SMT、通快均未上市 → 无公开市值 / PE / PB / PS，无历史分位。** 德国不存在光刻机纯正标的；唯一锚点是 ASML 2016 年以 €1bn 收购蔡司 SMT 24.9% 的历史交易 [D1]。
- 上市可比公司（2026-10，市值 USD；P/E 为 TTM）：**Aixtron $4.75bn / P/E ≈184**（最低盈利基数导致畸高）、**Süss MicroTec $1.43bn / P/E ≈40.2**、**Jenoptik $2.57bn / P/E ≈29.4** [D9][D10][D11]。
- **结论**：德国环节的利润池不体现在二级市场——真正的行业利润在荷兰上市的 ASML。

**政策 · 监管 · 关税 · 补贴**
- 法律框架：德国《对外经济法 AWG》+《对外经济条例 AWV》、欧盟两用物项条例 (EU) 2021/821、瓦森纳安排；**BAFA 为发证机关**（BMWK 定政策）[D5]。
- **AWV 第 21 次修订**（联邦内阁 2024-07-17 通过）：将「新兴技术」列入国家两用清单，含 Cryo-CMOS、低温冷却系统、特定扫描电镜、**干法刻蚀设备**、低温晶圆检测设备等 [D6]。
- **德国的「隐形否决权」**：即便 ASML 与荷兰政府批准，德国可拒发蔡司反射镜 / 通快激光的出口许可，从而卡死对华 EUV 出口 [D6]。
- 补贴：IPCEI 微电子与通信技术（ME/CT）欧盟核准约 €4.5bn；蔡司 SMT 本身受 IPCEI 资助 [D4]。

**本土竞争格局**
- 光刻环节**不是整机竞争，而是供应商寡头**：蔡司 SMT 在 EUV 光学近乎垄断（尼康/佳能始终未攻克 EUV 光学）；通快是 EUV 驱动激光独家供应 [D1][D2][D3]。
- 结构特征被概括为「**每个零件都是世界冠军，冠军相加不等于一台光刻机**」——ASML 负责整合，德国负责不可替代的关键子系统，这解释了德国在出口管制上对 ASML 供应链的实质杠杆 [D12][D6]。
- 互补性德国供应商：Schott（Zerodur 镜坯）、Jenoptik（光罩/量测）、Süss MicroTec、Aixtron、Siltronic 等隐形冠军 [D13]。

---

### 3.4 美国 — 技术源头、规则制定者与最大资本池

**角色定位**：**本土不生产任何光刻扫描机**（整机由荷兰 ASML、日本尼康/佳能供应），但掌握 EUV 最关键的子系统——**极紫外光源**；同时是**除光刻机之外的全部前道晶圆制造设备**的主力供应国、出口管制的规则制定者、以及全球最大的设备与芯片公司上市地。

**代表公司**
- **Applied Materials（AMAT，NASDAQ）**：产品覆盖沉积、刻蚀、CMP、量测检测、离子注入等 [U1]。
- **KLA Corporation（KLAC，NASDAQ）**：过程控制/量测检测龙头 [U2]。
- **Lam Research（LRCX，NASDAQ）**：刻蚀/沉积 [U3]。
- **Intel（INTC，NASDAQ）**：美国唯一本土先进逻辑制造/代工，采用 EUV [U4]。
- **Micron（MU，NASDAQ）**：1γ DRAM 节点已导入 EUV 量产 [U5]。
- **Cymer / ASML San Diego（非独立上市）**：EUV/DUV 光源研发与制造中心，负责 LPP 光源与液滴发生器 [U8]。
- **美国没有任何在产的光刻扫描机整机厂商。**

**产能 · 市场规模**
- 北美 2025 年设备支出 **108.9 亿美元（−20%）**，约占全球 **8%** [U7]。
- **AMAT FY2025**（截至 2025-10-26）：总营收 **283.68 亿美元（+4%）**；Semiconductor Systems **207.98 亿美元**（按市场拆 foundry/logic 67%、DRAM 26%、flash 7%）[U1]。
- **KLA FY2026**（截至 2026-06-30）：总营收 **135.79 亿美元（+12%）**，Semiconductor Process Control **122.45 亿美元**；国际收入占 87% [U2]。
- **Lam FY2026**（截至 2026-06-28）：总营收 **232.33 亿美元（+26%）**[U3]。
- **Micron FY2026**（截至 2026-09-03）：总营收 **1,331.88 亿美元（+256%）**；1γ（首个导入 EUV 的 DRAM 节点）在 2026 Q4 成为其 DRAM 位产出主体 [U5]。

**估值**（TTM，时点 2026-10-09，stockanalysis.com / S&P Global 数据）

| 公司 | 代码 | 市值 | PE(TTM) | 前瞻 PE | P/S | P/B |
|---|---|---|---|---|---|---|
| Applied Materials | AMAT | 4,066.2 亿美元 | 43.95 | 28.91 | 13.11 | 15.78 |
| KLA | KLAC | 2,595.4 亿美元 | 53.75 | 36.18 | 18.91 | 40.49 |
| Lam Research | LRCX | 4,034.7 亿美元 | 55.66 | 33.84 | 17.27 | 32.17 |
| Micron | MU | 1.17 万亿美元 | 13.94 | 5.88 | 8.78 | 8.46 |
| Intel | INTC | 5,607.6 亿美元 | n/a（净利为负） | 63.42 | 9.84 | 6.17 |

来源 [U9]–[U13]。**历史分位**：KLA 现 PE ~53.75x 显著高于其 5 年 PE 中位数约 **28.7x**（该分位为聚合/搜索摘要，**未核验原文**）[U10]。INTC 因亏损无 TTM PE，只能看前瞻 [U13]。

**政策 · 监管 · 关税 · 补贴**
- **BIS 出口管制**：2024-12-02 生效的规则（Entity List 终规则 89 FR 96830，配合同日中间终规则）**新增管制 24 类半导体制造设备与 3 类软件工具，明确含光刻**；**将 140 个实体列入 Entity List**（另修改 14 个）；新设 **SME FDP 规则**与 **Footnote 5 FDP 规则**扩展域外管辖；合规宽限至 2024-12-31 [U6]。终规则点名 Beijing Guangke Xintu、Dongfang Jingyuan Electron、Oriental Crystal 等实体为「co-developing lithography technology with advanced-node fabrication facilities that produce chips for military end use」[U6]。
- **企业合规风险**：KLA、Lam、Intel、Micron 均在 10-K 中列出 BIS 规则对其中国业务的影响 [U2][U3][U4][U5]；**AMAT 更披露自 2022 年起已收到来自美国司法部、BIS 与 SEC 的多份传票**，涉及其中国客户出货与出口管制合规 [U1]。
- **关税调查**：Micron 披露 2025-04-14 BIS 依《1962 年贸易扩展法》第 232 条对进口半导体、半导体制造设备及衍生产品发起国家安全调查 [U5]。

**本土竞争格局**
- 全球 WFE 第一梯队为 ASML、Applied Materials、Lam、Tokyo Electron、KLA 五家（合计约 70% 份额——**该数值为搜索摘要，未核验原文**）[U1][U2]。
- **光刻整机：美国零份额**，仅提供其中的光源子系统 [U8]。
- 离子注入：AMAT 用「comprehensive portfolio」自述覆盖，第三方口径称其全球份额约 63%（**摘要获取、未核验原文**）[U1]。
- **来自中国的竞争**：AMAT 10-K 明确警示，因地方政府补贴 + 美国出口管制，**中国本土设备厂商竞争加剧**，且出口管制可能使其相对非美系竞争对手处于劣势 [U1]。

---

### 3.5 中国 — 最大需求方与艰难追赶者

**角色定位**：**超级需求方 + 技术追赶者**，前道制造端几乎空白。

**代表公司**
- **上海微电子装备（SMEE）** — **未上市**：国内唯一具备前道光刻机量产能力的企业 [C10][C13]。
- **张江高科（600895.SH）**：通过全资子公司张江浩成持有上海微电子 **10.78%** 股权，是 A 股最核心的 SMEE 概念标的 [C14][C13]。
- **北方华创（002371.SZ）**、**中微公司（688012.SH）**：A 股设备双龙头，但**主战场是刻蚀/薄膜沉积，非光刻机** [C12]。
- 光刻机产业链上市公司：茂莱光学（688502.SH，透镜/棱镜/DUV 光学器件）、苏大维格（300331.SZ，定位光栅尺）、波长光电（301421.SZ，DUV 镜头）、福晶科技（002222.SZ，非线性光学晶体）、炬光科技（688167.SH，激光光源/光束匀化）、富创精密（688409.SH，精密金属结构件，已进 ASML 供应链）、新莱应材（300260.SZ，超高真空）、芯碁微装（688630.SH，直写光刻整机）[C13]。
- **华卓精科** — IPO 在审（科创板）：光刻机双工件台概念商，源自清华 IC 装备团队 [C7]。

**产能 · 市场规模**
- 2025 年中国进口半导体设备 **391.66 亿美元（+3%）**，全球第一；其中**光刻机 106.2 亿美元（约 732–740 亿元），占设备进口额 27%** [C3]。
- 2026Q1 中国内地设备采购约 **98 亿美元（+25%）**，占全球 35%，创历史新高 [C2]。
- **国产化率极低**：约 **2.5%**（2024，SEMI 口径）[C2] 或 **不足 1%**（2025）[C10]——两个口径不一，均指向极低自给。
- 中国光刻机行业市场规模 2025 年 **197.34 亿元（+10.40%）**（该口径疑指本土供给，与进口额不可直接比较）[C10]。
- ⚠️ **口径警告**：海关总署「分步重复光刻机」口径下 2024 年进口 **240 台 / 8.10 亿美元**（中国电子专用设备工业协会）[C11]，与伯恩斯坦「光刻机」106.2 亿美元**差异极大**，源于 HS 分类口径不同，**引用时不可混用**。

**估值**（时点不一，均已标注；PE 为 TTM）

| 公司 | 代码 | 估值指标 | 时点 |
|---|---|---|---|
| 中微公司 | 688012.SH | PE(TTM) 110.50x → 108.76x（近 1 月 −25%） | 2026-05-18 → 2026-08-03 [C4][C5] |
| 北方华创 | 002371.SZ | PE(TTM) 80.56x → 83.46x | 2026-05-18 → 2026-08-03 [C4][C5] |
| 茂莱光学 | 688502.SH | 国金证券预测 2026–2028 营收 10.12/15.11/22.78 亿元、归母净利 0.88/1.37/2.22 亿元，首次覆盖「买入」（**券商预测**） | 2026-06-10 [C8] |
| 张江高科 | 600895.SH | 2025-09-24 收盘 50.78 元、两连板、总市值一度 851 亿元 | 2025-09-24 [C14] |
| 华卓精科 | IPO 在审 | 拟募资 35 亿元；估值由前次 29.4 亿升至 140 亿元；2023–2025 归母净利 −0.73/−0.66/−0.95 亿元 | 2026-08 [C7] |

> 注：C4 来源未披露当日总市值，故上表市值缺失处不补。

**政策 · 监管 · 关税 · 补贴**
- **国内扶持**：大基金三期注册资本 **3,440 亿元**，重点支持光刻机、EDA 等短板；上海、北京目标把光刻机零部件国产化率提升至 **70% 以上** [C2]。
- **外部管制**：荷兰 2023-09 起对先进浸没式 DUV 实施许可、2024-01 起 ASML 预计无法获许可对华出口 NXT:2000i 等机型 [N5]；日本 2023-07 起管制 [J6]。
- **美国 MATCH 法案**（2026-04 众议院外委会通过；**立法在途、尚未生效，属提案而非既成事实**）：拟全面禁止向中国出口浸没式 DUV 光刻设备与低温刻蚀设备；拟将中芯国际、长江存储、长鑫存储、华虹、华为列为「受管制设施」，中微、北方华创、上海微电子、芯源微、华海清科等设备企业亦列入；要求日、荷在 150 天内对齐管制，必要时动用「外国直接产品规则」[C15]。
- ASML 表态：CEO 富凯称进一步收紧管制只会加速中国自研；ASML 销华 DUV 基于 2015 年技术，为「八代之前」；荷兰政府反对 MATCH 法案 [C6]。
- **关税**：本次未检索到光刻机专项关税信息，暂缺。

**本土竞争格局**
- 整机：**上海微电子一家独大**，国内唯一前道光刻机整机厂，现主推 **90nm 成熟制程**（SSX/SSA600 系列），2025 年 SSX600 系列出货量占国内光刻机市场份额超 **80%** [C2][C10]。
- 综合设备：北方华创 + 中微公司合计营收/归母净利约占 2025 年 A 股半导体设备板块的一半（16 家合计营收 920.8 亿元、扣非净利 111.15 亿元）[C12]。
- 零部件生态：光源（福晶科技、炬光科技）、光学（茂莱光学、波长光电）、精密结构件（富创精密、新莱应材）、工件台（华卓精科）、定位光栅（苏大维格）[C13]。⚠️ 该生态多为**概念性梳理**，各公司光刻机收入占比普遍很小（如茂莱光学 2022H1 光刻机营收仅 466 万元）[C8][C13]。
- 华卓精科招股书**大量淡化「光刻机」叙事**（「光刻机」出现次数由上轮 322 次降至 26 次），定位改为「集成电路专用设备及关键部件供应商」，双工件台产业化多年未成规模收入 [C7]。

**⚠️ 关键争议核实：「SSA800 28nm 已批量交付、良率 90%+」= 传闻，已被辟谣**

- **传闻（营销号，未证实）**：公众号「曜哥谈基」（2026-03-10）称 SSA800 系列 28nm 浸没式 DUV 于 2026 年初交付中芯国际上机测试、良率稳定超 90%、国产化率超 85%、2026Q3 完成量产验证；并称 EUV 原型机 Hyperion 1 进入试产。该文另称中芯国际以多重曝光实现 7nm 稳定量产、良率超 80%——**均无权威信源** [C9]。
- **已辟谣（权威媒体独立核实）**：芯智讯指出原消息仅称「据报道」、无权威来源；所称「长三角半导体产业峰会官宣量产」查无此会；SEMICON China 现场上海微电子展台**无该设备**；「光刻机不存在量产良率指标」；据晶圆厂人士，**SSA800 未进入任何商业化晶圆厂**，仍在集成电路研发中心（ICRD）测试验证 [C1]。
- **21 世纪经济报道**（2026-05-19）独立核实：传闻最早于 2026 年 3–4 月由个别博主散布，无可靠信源，关键数据与实际不符；设备仍在调试阶段 [C2]。
- **口径较软的第三方**：智研咨询称「28nm 浸没式 DUV（SSA800 系列）完成多轮工艺验证」，**未称量产或交付** [C10]。
- **结论**：该说法的可核实状态 = **仍在研发中心测试验证/调试，未进入商业化晶圆厂，28nm 国产光刻机尚无量产证据** [C1][C2]。

---

### 3.6 台湾 — 先进制程需求轴与光刻配套

**角色定位**：主导轴为**下游需求**（先进制程晶圆厂的设备采购），并在光刻**配套环节**有全球领先地位；本身不生产光刻机整机，EUV 100% 依赖 ASML。

**代表公司**：台积电 TSMC（TWSE: **2330** / NYSE ADR: **TSM**）、联电 UMC（2303 / NYSE: UMC）、世界先进 VIS（5347）、力积电 PSMC（6770）、**家登精密 Gudeng（3680）**[T3][T8][T11][T13]。

**产能 · 市场规模**
- 台湾 2025 年设备采购 **315 亿美元（+90%）**，创历史新高、增幅居各市场之冠，**居全球第二**（仅次中国大陆），高于韩国 257 亿美元 [T4]。
- **对 ASML 的权重**：FY2025 台湾贡献 **€8,337.9M、占 ASML 总净销售额 25.5%**，与韩国并列第二，仅次于中国（29.1%），远高于美国（12.5%）[N3][T5]。
- 台积电 2025 年营收 **3.809 兆新台币（约 1,220 亿美元）**、税后净利 **1.7178 兆新台币**、**EPS 66.25 元** [T3]。
- 台积电 2025 Q4 营收 **337.3 亿美元**、毛利率 **62.3%**（创高）；2 纳米已于 2025 Q4 在新竹与高雄量产，A16 计划 2026 下半年量产 [T1]。
- 台积电资本支出：2025 年 **409 亿美元**；**2026 年指引 520–560 亿美元（同比 +27%~37%，续创新高）**，其中约 **70–80% 投向先进制程** [T2][T1]。
- **EUV 保有量**：机构统计截至 2025 年底 ASML 全球 EUV 累计出货逾 300 台，**台积电占逾 50%（约 157 台）**——此为**二手机构推估，非 ASML 官方分客户披露** [T14]。
- **家登（3680）**：ASML 认证的**全球唯二 EUV 光罩传送盒供应商**、台湾唯一，且为**全球唯一获 High-NA EUV 光罩盒认证者**；EUV 光罩盒全球市占约 **7 成** [T8]。

**估值**（时点 2026-10-08 收盘；PE 为 TTM）

| 公司 | 代码 | 市值 | PE(TTM) | Forward PE | PB |
|---|---|---|---|---|---|
| 台积电 | 2330 | 约 66.13 兆新台币 | 29.8 倍 | 20.1 倍 | 约 10.3 倍 |
| 联电 | 2303 | 约 1.86 兆新台币 | 22.3 倍 | 23.9 倍 | 4.2 倍 |
| 世界先进 | 5347 | — | 40.4 倍 | — | 5.6 倍 |
| 力积电 | 6770 | — | 24.1 倍 | — | 2.6 倍 |

来源 [T9][T12][T13]。台积电另：EPS(TTM) 85.49 元、现金股利 28 元（殖利率约 1.1%）[T9]。**家登** 2024 年营收 **65.45 亿新台币（+28.91%）**、**EPS 12.32 元**（因来源时点落差大，未采信单一 PE 数字）[T8]。
⚠️ **台湾数据源（FinLab）仅提供当日 PE/PB，未提供 5/10 年历史分位**，故估值模块未输出分位数 [T12]。

**政策 · 监管 · 关税 · 补贴**
- **台美对等关税贸易协议（2026-01-15 签署）**：台湾输美对等关税由 **20% 降至 15%**；半导体及衍生品取得 232 条款「最优待遇」——在美建厂期间可免税进口相当于在建产能 **2.5 倍**的设备与产品、完工后 1.5 倍；台方承诺 **2,500 亿美元企业直接投资 + 2,500 亿美元政府信贷担保（合计 5,000 亿美元）**；美方目标将台湾 **40% 半导体供应链**移至美国 [T6]。该协议重塑台湾「需求」角色的地理分布 [T6]。
- **本地补贴**：产创条例第 10 条之 2（「台版芯片法案」，施行至 2029 年底）给予**研发投入 25%、先进设备支出 5%** 的营所税抵减；门槛为年研发费 ≥60 亿新台币、研发密度 ≥6%、有效税率 15%；2026 年（第 3 年）共 **5 家**业者申请 [T7]。

**本土竞争格局**
- **先进制程呈「单极」**：台积电独占台湾 EUV 采购，是 ASML 最大客户与全球最大 EUV 用户 [T5][T14]。
- **台积电弃用 High-NA EUV**：2026 年北美技术论坛上，副共同营运长张晓强表示**至 2029 年所有规划节点均不采用** ASML 最新 High-NA EUV（单台逾 3.5 亿欧元、约现有 EUV 两倍），A13/A12 等节点续用现有 Low-NA EUV + 多重曝光 [T10]——此结构性决定**压缩 ASML 在台的 High-NA 增量需求**。
- **成熟制程第二梯队**：联电、世界先进、力积电承接台积电 8 吋/6 吋缩产后的需求，三厂**均用 DUV、不采购 EUV** [T11]。
- **配套环节**：家登（3680）为 ASML 认证的全球唯一 High-NA EUV 光罩盒供应商，EUV 光罩盒全球市占约 7 成 [T8]。

---

## 4. 全球竞争格局与估值对标

### 4.1 各环节格局

| 环节 | 格局 | 依据 |
|---|---|---|
| **光刻整机（金额）** | ASML >90%（JPMorgan 口径约 95%） | [N11] |
| **光刻整机（台数）** | 佳能约占 3 成（后道先进封装份额「压倒性」）；尼康剩余 | [J13][J1] |
| **EUV 整机** | ASML 唯一，无第二家 | [N3][D1] |
| **EUV 投影光学** | Carl Zeiss SMT 近乎垄断（尼康/佳能未攻克） | [D1] |
| **EUV 驱动激光** | TRUMPF 独家 | [D2][D3] |
| **EUV 光源** | Cymer（ASML 美国子公司） | [U8] |
| **光刻胶** | 日系 5 家 91–92% | [J5] |
| **掩膜基板** | 日系 3 家 96% | [J5] |
| **涂布显影** | 东京电子领跑 | [J9] |
| **中国整机** | 上海微电子一家独大，主推 90nm，国内份额 >80% | [C2][C10] |

### 4.2 龙头跨国估值对标

⚠️ **跨币种市值不可直接横比**，下表列出原币种数值；**PE 为跨市场可比指标**，但需注意各家口径（荷兰/美国为 TTM；日本为「公司预想」；中国为 TTM 且时点不一；台湾为 TTM）。

| 公司 | 代码 | 上市地 | 市值（原币） | PE | PB | 口径/时点 |
|---|---|---|---|---|---|---|
| **ASML** | ASML | Euronext/NASDAQ | US$722.8bn | **57.8**(TTM) | 28.2 | 2026-10-09 [N9] |
| Applied Materials | AMAT | NASDAQ | US$406.6bn | 43.95(TTM) | 15.78 | 2026-10-09 [U9] |
| Lam Research | LRCX | NASDAQ | US$403.5bn | 55.66(TTM) | 32.17 | 2026-10-09 [U11] |
| KLA | KLAC | NASDAQ | US$259.5bn | 53.75(TTM) | 40.49 | 2026-10-09 [U10] |
| Intel | INTC | NASDAQ | US$560.8bn | n/a | 6.17 | 2026-10-09 [U13] |
| Micron | MU | NASDAQ | US$1.17tn | 13.94(TTM) | 8.46 | 2026-10-09 [U12] |
| **台积电** | 2330 | TWSE | NT$66.13tn | 29.8(TTM) | 约 10.3 | 2026-10-08 [T9][T12] |
| 联电 | 2303 | TWSE | NT$1.86tn | 22.3(TTM) | 4.2 | 2026-10-08 [T13][T12] |
| 东京电子 | 8035 | 东证 Prime | ¥29.12tn | 未披露 | 13.36 | 2026-10-09 [J9] |
| 信越化学 | 4063 | 东证 Prime | ¥12.08tn | 21.54(预想) | 2.49 | 2026-10-09 [J10] |
| HOYA | 7741 | 东证 Prime | ¥8.39tn | 未披露 | 8.25 | 2026-10-09 [J12] |
| 佳能 | 7751 | 东证 Prime | ¥6.28tn | 12.00(预想) | 1.15 | 2026-10-09 [J8] |
| 东京応化 | 4186 | 东证 Prime | ¥1,192.9bn | 26.27(预想) | 4.52 | 2026-10-09 [J11] |
| 尼康 | 7731 | 东证 Prime | ¥625.1bn | 61.73(预想，**失真**) | 1.04 | 2026-10-09 [J7] |
| **中微公司** | 688012.SH | 上交所科创板 | — | **108.76**(TTM) | — | 2026-08-03 [C5] |
| **北方华创** | 002371.SZ | 深交所 | — | **83.46**(TTM) | — | 2026-08-03 [C5] |
| Aixtron | AIXA | 法兰克福 | US$4.75bn | ≈184(TTM) | — | 2026-10 [D9] |
| Süss MicroTec | SMHN | 法兰克福 | US$1.43bn | ≈40.2(TTM) | — | 2026-10 [D10] |
| Jenoptik | JEN | 法兰克福 | US$2.57bn | ≈29.4(TTM) | — | 2026-10 [D11] |

**未上市、无公开估值**：上海微电子（SMEE）[C10]、Carl Zeiss SMT [D1]、TRUMPF [D2]、Cymer [U8]、华卓精科（IPO 在审）[C7]。

### 4.3 估值观察

1. **全球设备链估值普遍处历史高位**：ASML 当前 PE(TTM) 高于其十年中位数约 **44%** [N10]；KLA 现 PE 显著高于其 5 年中位数约 28.7x [U10]。
2. **日本第二梯队严重分化**：佳能 PE(预想) 仅 **12.00**，尼康高达 **61.73**（因 FY2026/3 一次性损失失真 [J1]）——**不可把尼康的 PE 当作行业估值锚**。
3. **中国 A 股设备龙头估值显著高于全球同业**：中微公司 108.76x、北方华创 83.46x [C5]，对比 ASML 57.8x、AMAT 43.95x [N9][U9]。且两者主战场是刻蚀/薄膜**而非光刻** [C12]，高估值含国产替代预期溢价。
4. **德国环节不体现在二级市场**：真正的利润在荷兰上市的 ASML；德国上市可比（Aixtron/Süss/Jenoptik）均非光刻主业的直接受益者 [D9][D10][D11]。

---

## 5. 关键标的（按上市地归类）

| 上市地 | 标的 |
|---|---|
| **荷兰 Euronext + 美国 NASDAQ** | ASML [N9] |
| **美国 NASDAQ** | Applied Materials (AMAT)、Lam Research (LRCX)、KLA (KLAC)、Intel (INTC)、Micron (MU) [U9]–[U13] |
| **日本 东证 Prime** | 尼康 7731、佳能 7751、东京电子 8035、信越化学 4063、HOYA 7741、东京応化 4186 [J7]–[J12] |
| **台湾 TWSE / TPEx** | 台积电 2330（ADR: TSM）、联电 2303、世界先进 5347、力积电 6770、家登精密 3680 [T3][T8][T11][T13] |
| **德国 法兰克福**（非光刻纯标的，可比） | Aixtron AIXA、Süss MicroTec SMHN、Jenoptik JEN [D9][D10][D11]；蔡司 SMT 与通快**未上市** [D1][D2] |
| **中国 A 股** | 张江高科 600895（持股 SMEE 10.78%）、北方华创 002371、中微公司 688012、茂莱光学 688502、波长光电 301421、苏大维格 300331、福晶科技 002222、炬光科技 688167、富创精密 688409、新莱应材 300260、芯碁微装 688630 [C12][C13][C14]；华卓精科（IPO 在审）[C7]；**上海微电子未上市** [C10] |

---

## 6. 风险提示

1. **出口管制持续升级，双向冲击**：美国 BIS 2024-12-02 规则新增管制的 24 类设备**明确含光刻** [U6]；MATCH 法案（**立法在途，尚未生效**）拟禁售浸没式 DUV [C15]；日本 2023-07-23 施行 23 项管制、对华降为逐案申请 [J6]；荷兰 2023-09 起三轮收紧 [N5][N6]。管制既打击设备商中国收入（ASML 中国占比已由 36.1% 降至 29.1% [N3]），又反向加速中国自研 [C6]。
2. **需求高度集中且已现回落**：ASML 出货由 2024 年 418 台降至 2025 年 327 台 [N3]；EUV 需求由台积电、三星、Intel、SK 海力士等少数客户决定 [T14]。
3. **技术路线风险**：**台积电明确至 2029 年不采用 High-NA EUV**（张曉強，2026 北美技术论坛），续用 Low-NA + 多重曝光 [T10]——直接压缩 ASML 在台的 High-NA 增量空间。
4. **供应链单点脆弱**：蔡司 SMT 的 EUV 光学为全球唯一、通快驱动激光为独家 [D1][D2][D3]，任一环节中断将中断全球 EUV 供给。ASML 自身也在 20-F 中把该独家供应关系列为供应链风险 [N3]。
5. **德国握有对 ASML 供应链的实质否决权**：即便荷兰批准，德国可拒发蔡司/通快出口许可 [D6]——管制风险不只在荷兰与美国。
6. **口径风险（引用必读）**：中国光刻机进口额 **106.2 亿美元 vs 8.10 亿美元**（HS 分类不同）[C3][C11]；ASML 中国收入占比 **29.1%（20-F）vs 33%（荷兰议会）**[N3][N7]；中国光刻机国产化率 **2.5%（SEMI/2024）vs 不足 1%（2025）**[C2][C10]；光刻机细分市场规模各机构差异极大 [C2]。**上述均不可混用或取平均。**
7. **信息质量风险**：中国「SSA800 已量产交付、良率 90%+」类说法已被芯智讯与 21 世纪经济报道**证伪**（设备仍在 ICRD 测试验证）[C1][C2]；本次检索到的两篇高时效自媒体文（《中科大副院长说…》《美国又一"隐形设备"垄断 68.3%》）经正文核实后，**账号为个人自媒体、正文与标题不符、数据无法核实，不作事实引用** [U14][U15]。该板块自媒体噪声显著偏高。
8. **估值风险**：全球设备链 PE 普遍处历史高位（ASML 高于十年中位数约 44% [N10]）；中国 A 股设备龙头 PE(TTM) 达 80–110x [C5]；中国光刻机概念股波动剧烈（张江高科两连板创历史新高 [C14]）。
9. **地缘与汇率**：台美对等关税贸易协议重塑台湾需求地理分布，美方目标将台湾 40% 半导体供应链移至美国 [T6]；ASML 以欧元记账、美股估值已换算美元，口径不可混用 [N1][N9]。
10. **下游集中度传导**：台积电 2026 年资本支出指引 520–560 亿美元（+27%~37%）[T2]，是拉动全球光刻需求的核心变量；其单边技术路线或资本开支调整将直接冲击设备链。

---

## 资料来源

> 说明：本附录只列被正文引用的来源，与正文引用 1:1 对应。前缀含义：N=荷兰、J=日本、D=德国、U=美国、C=中国、T=台湾。

**荷兰（N）**

- N1 / ASML reports €32.7 billion total net sales and €9.6 billion net income in 2025 (Q4 & FY2025 results, Form 6-K Exhibit 99.1) / ASML Holding N.V. (via SEC EDGAR) / 公告 / https://www.sec.gov/Archives/edgar/data/937966/000162828026003701/pressreleasefinancialresul.htm / 2026-01-28 / accessed=2026-10-09
- N2 / ASML reports €9.3 billion total net sales and €2.9 billion net income in Q2 2026 (Form 6-K Exhibit 99.1) / ASML Holding N.V. (via SEC EDGAR) / 公告 / https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/pressreleasefinancialresul.htm / 2026-07-15 / accessed=2026-10-09
- N3 / ASML Holding N.V. Annual Report 2025 (Form 20-F) / ASML Holding N.V. (via SEC EDGAR) / 公告 / https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm / 2026-02-25 / accessed=2026-10-09
- N5 / Nederland breidt exportcontrolemaatregel uit voor geavanceerde productieapparatuur halfgeleiders / Rijksoverheid.nl（荷兰政府） / 公告 / https://www.rijksoverheid.nl/actueel/nieuws/2024/09/06/nederland-uitbreiding-exportcontrolemaatregel-geavanceerde-productieapparatuur-halfgeleiders / 2024-09-06 / accessed=2026-10-09
- N6 / Klever: aanscherping exportcontrole op geavanceerde productieapparatuur voor halfgeleiders / Rijksoverheid.nl（荷兰政府） / 公告 / https://www.rijksoverheid.nl/actueel/nieuws/2025/01/15/klever-aanscherping-exportcontrole-op-geavanceerde-productieapparatuur-voor-halfgeleiders / 2025-01-15 / accessed=2026-10-09
- N7 / Antwoord op vragen van het lid Hoogeveen over de Amerikaanse MATCH Act en de gevolgen daarvan voor ASML, nr. 1903 / Tweede Kamer der Staten-Generaal / 公告 / https://zoek.officielebekendmakingen.nl/ah-tk-20252026-1903.html / 2026-05-12 / accessed=2026-10-09
- N9 / ASML Holding (ASML) Statistics & Valuation / StockAnalysis.com（S&P Global 数据） / 媒体 / https://stockanalysis.com/stocks/asml/statistics/ / 2026-10-09 / accessed=2026-10-09
- N10 / ASML Holding NV PE Ratio (TTM) — 10-year range & median / GuruFocus / 媒体 / https://www.gurufocus.com/term/pettm/XTER:ASME / 2026-05-23 / accessed=2026-10-09
- N11 / 摩根大通：2025年ASML在全球光刻机市场份额达95% / 199IT（原作者：快科技，转引 JPMorgan） / 媒体 / http://www.199it.com/archives/1851676.html / 2026-09-14 / accessed=2026-10-09

**日本（J）**

- J1 / 2026年3月期 決算報告（通期実績・2027年3月期見通し） / 株式会社ニコン / 公告 / https://www.jp.nikon.com/content/dam/web-assets/nikoncom/company/local/jp/ja/ir/ir_library/result/pdf/2026/26_all.pdf / 2026-05-08 / accessed=2026-10-09
- J2 / キヤノン(株)(7751) 2025年12月期 決算短信〔米国基準〕(連結) / キヤノン株式会社 / 公告 / https://global.canon/ja/ir/results/2025/rslt2025j.pdf / 2026-01-29 / accessed=2026-10-09
- J3 / 2025年12月期 決算説明会資料（ノート） / キヤノン株式会社 / 公告 / https://global.canon/ja/ir/conference/pdf/conf2025j-note.pdf / 2026-01-29 / accessed=2026-10-09
- J4 / 2025年の世界半導体製造装置販売額は前年比15％増の1,351億ドル（World Wide SEMS Report） / 日本半導体製造装置協会(SEAJ) / 行业协会 / https://www.seaj.or.jp/statistics/37771064915417.pdf / 2026-04-08 / accessed=2026-10-09
- J5 / 令和7年度 集積回路製造用材料の市場規模・日本企業シェア調査（経済産業省委託調査） / 経済産業省(METI) / 官方统计 / https://www.meti.go.jp/meti_lib/report/2025FY/report_202605251153_0.pdf / 2026 / accessed=2026-10-09
- J6 / 外為法改正（2023年7月施行）先端半導体の輸出規制とコンプライアンス管理 / トムソン・ロイター / 媒体 / https://insight.thomsonreuters.co.jp/business/resources/resource/revision-of-foreign-trade-law / 2024-08-27 / accessed=2026-10-09
- J7 / ニコン(7731) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/7731.T / 2026-10-09 / accessed=2026-10-09
- J8 / キヤノン(7751) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/7751.T / 2026-10-09 / accessed=2026-10-09
- J9 / 東京エレクトロン(8035) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/8035.T / 2026-10-09 / accessed=2026-10-09
- J10 / 信越化学工業(4063) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/4063.T / 2026-10-09 / accessed=2026-10-09
- J11 / 東京応化工業(4186) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/4186.T / 2026-10-09 / accessed=2026-10-09
- J12 / HOYA(7741) 株価・株式情報 / Yahoo!ファイナンス / 媒体 / https://finance.yahoo.co.jp/quote/7741.T / 2026-10-09 / accessed=2026-10-09
- J13 / 【インタビュー】キヤノンが"旧型"露光装置の生産能力を1.5倍へ増強、先端パッケージの後工程で圧倒的シェア / 東洋経済オンライン / 媒体 / https://toyokeizai.net/articles/-/930998 / 2026-01-27 / accessed=2026-10-09
- J14 / 日本政府計劃放寬成熟製程半導體的補助門檻（引日經 2026-05-14 報導） / 經貿透視雙周刊（台灣經貿網） / 媒体 / https://www.trademag.org.tw/page/newsid1/?id=7927115&iz=6 / 2026-05-18 / accessed=2026-10-09
- J15 / 公众号：华商韬略 · 日本光刻机巨头，崩了！ / 微信公众号（华商韬略） / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552801&ver=7016&signature=mAOtdznEK1scCwuVoJtCqWI1vxvTp3DX83zw5iDFfiz4u9ZCw4np7ToCuJ902*jVKr65fVUqsVFP1BTzPj3y5*FRWE28MJQ4HFWTdPWf3Itw7sUJJ1vSf1thpSARFrwE&new=1 / 文章发布时间 2026-03-16 / accessed=2026-10-09

**德国（D）**

- D1 / ZEISS Group – Facts & Figures / ZEISS / 官方统计 / https://www.zeiss.com/corporate/en/about-zeiss/present/facts-figures.html / FY2024/25 / accessed=2026-10-09
- D2 / Abkühlung der Weltkonjunktur führt zu rückläufigem Umsatz bei TRUMPF (FY2024/25) / TRUMPF / 公告 / https://www.trumpf.com/de_DE/newsroom/pressemitteilungen-global/pressemitteilung-detailseite-global/release/abkuehlung-der-weltkonjunktur-fuehrt-zu-ruecklaeufigem-umsatz-bei-trumpf-leibinger-kammueller-vorsichtige-anzeichen-der-besserung-9792/ / 2025-10-22 / accessed=2026-10-09
- D3 / ASML ehrt TRUMPF für neuen EUV-Laser / TRUMPF / 公告 / https://www.trumpf.com/de_INT/newsroom/pressemitteilungen-global/pressemitteilung-detailseite-global/release/asml-ehrt-trumpf-fuer-neuen-euv-laser-9837/ / 2025-10-24 / accessed=2026-10-09
- D4 / IPCEI-Projektsteckbrief: CARL ZEISS SMT GMBH（EUV Optiksysteme für Lithographie mit sub-10nm Auflösung） / BMWK（德国联邦经济与气候行动部） / 公告 / https://www.bundeswirtschaftsministerium.de/Redaktion/DE/Downloads/I/Ipcei-Projektsteckbriefe/2020-12-ipcei-projektsteckbrief-zeiss.pdf / 2020-12 / accessed=2026-10-09
- D5 / Export Control（出口管制总览） / BAFA（联邦经济与出口管制局） / 公告 / https://www.bafa.de/EN/Foreign_Trade/Export_Control/export_control_node.html / 2026 / accessed=2026-10-09
- D6 / Emerging technologies become part of the German national export list: An interference with the Single Market?（AWV 第 21 次修订简报） / BLOMSTEIN Rechtsanwälte / 媒体 / https://www.blomstein.com/assets/downloads/240718_briefing_awv-novelle_en.pdf / 2024-07-18 / accessed=2026-10-09
- D8 / Germany Wafer Manufacturing Equipment Market（Analysis, Forecast, Size, Trends） / IndexBox / 券商研报（市场研究估算） / https://www.indexbox.io/store/germany-wafer-manufacturing-equipment-market-analysis-forecast-size-trends-and-insights/ / 2026 / accessed=2026-10-09
- D9 / Aixtron – Market capitalization & P/E ratio / companiesmarketcap.com / 媒体 / https://companiesmarketcap.com/aixtron/marketcap/ / 2026-10 / accessed=2026-10-09
- D10 / SÜSS MicroTec – Market capitalization & P/E ratio / companiesmarketcap.com / 媒体 / https://companiesmarketcap.com/suss-microtec/marketcap/ / 2026-10 / accessed=2026-10-09
- D11 / Jenoptik AG – Market capitalization & P/E ratio / companiesmarketcap.com / 媒体 / https://companiesmarketcap.com/jenoptik/marketcap/ / 2026-10 / accessed=2026-10-09
- D12 / 公众号：看懂AI和科技 · 全球最强的光刻机为何出在荷兰，而不是美国日本德国？芯片界的唯一老大——荷兰ASML / 微信公众号 / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552817&ver=7016&signature=aa4Use8Rsu04GHxNx6qD4kdkDQkGt0W6TedsNdBoR914gRLZ128ZW6paTwWNnDGYmwy*q1C60Cig22XwG7H08qp09DhLd204bLXTS-4mQE2ypEHZ9x2AKUAYraU574hP&new=1 / 文章发布时间 2026-10-04 / accessed=2026-10-09
- D13 / 公众号：展芯科技说 · 不做光刻机的德国公司，凭什么活到今天？6个关键节点看懂它的逆袭 / 微信公众号 / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552817&ver=7016&signature=cUCClQb5NcMfrdle0OhaFNE6KHLgYHCDAvDdKl1EvlFLiuFEQERZhuIWFuKSPTWBEUNEKazlHHgm8mgXi3G8IpmZx0U4Zuu0y8IcQ0*y*4X6GHOsNCUYd3I-7FptrcDk&new=1 / 文章发布时间 2026-03-30 / accessed=2026-10-09

**美国（U）**

- U1 / Applied Materials, Inc. Form 10-K (FY2025) / SEC/EDGAR / 公告 / https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm / 2025-12-12 / accessed=2026-10-09
- U2 / KLA Corporation Form 10-K (FY2026) / SEC/EDGAR / 公告 / https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/klac-20260630.htm / 2026-08-06 / accessed=2026-10-09
- U3 / Lam Research Corporation Form 10-K (FY2026) / SEC/EDGAR / 公告 / https://www.sec.gov/Archives/edgar/data/707549/000070754926000037/lrcx-20260628.htm / 2026-08-07 / accessed=2026-10-09
- U4 / Intel Corporation Form 10-K (FY2025) / SEC/EDGAR / 公告 / https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm / 2026-01-23 / accessed=2026-10-09
- U5 / Micron Technology, Inc. Form 10-K (FY2026) / SEC/EDGAR / 公告 / https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm / 2026-10-09 / accessed=2026-10-09
- U6 / Additions and Modifications to the Entity List; Removals From the VEU Program (BIS Final Rule, 89 FR 96830) / Federal Register (BIS, U.S. Dept. of Commerce) / 官方统计 / https://thefederalregister.org/documents/2024-28267/additions-and-modifications-to-the-entity-list-removals-from-the-validated-end-user-veu-program / 2024-12-05 / accessed=2026-10-09
- U7 / SEMI Reports Global Semiconductor Equipment Billings Reached $135 Billion in 2025（经 Evertiq 转载） / SEMI / 行业协会 / https://evertiq.com/news/2026-04-09-semiconductor-equipment-billings-reached-135b-in-2025 / 2026-04-09 / accessed=2026-10-09
- U8 / Explore ASML San Diego (Cymer / EUV & DUV light source) / ASML / 公告 / https://www.asml.com/en/company/about-asml/locations/san-diego / 2026 / accessed=2026-10-09
- U9 / Applied Materials (AMAT) Statistics & Valuation / StockAnalysis.com / 媒体 / https://stockanalysis.com/stocks/amat/statistics/ / 2026-10-09 / accessed=2026-10-09
- U10 / KLA Corporation (KLAC) Statistics & Valuation / StockAnalysis.com / 媒体 / https://stockanalysis.com/stocks/klac/statistics/ / 2026-10-09 / accessed=2026-10-09
- U11 / Lam Research (LRCX) Statistics & Valuation / StockAnalysis.com / 媒体 / https://stockanalysis.com/stocks/lrcx/statistics/ / 2026-10-09 / accessed=2026-10-09
- U12 / Micron Technology (MU) Statistics & Valuation / StockAnalysis.com / 媒体 / https://stockanalysis.com/stocks/mu/statistics/ / 2026-10-09 / accessed=2026-10-09
- U13 / Intel (INTC) Statistics & Valuation / StockAnalysis.com / 媒体 / https://stockanalysis.com/stocks/intc/statistics/ / 2026-10-09 / accessed=2026-10-09
- U14 / 公众号：W侃科技 · 不止光刻机？美国又一"隐形设备"垄断68.3%，正偷偷拿捏中国芯命脉 / 微信公众号（个人自媒体，**未核验，不作事实引用**） / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552832&ver=7016&signature=5bxWl3O2d3*nczzxIEaTMPAZgrnm61TqVd24QI1aaYa0wTbOH8wBfwsl18*AEUVsDhB4NGsth-rpL8nz9WVOELR80mWHnvhBMEb73CLfvwf2LV5RozTpo4D1xvrimJ5s&new=1 / 文章发布时间 2026-10-06 / accessed=2026-10-09
- U15 / 公众号：糖糖Qg · 中科大副院长说：光刻机美国造不出，中国永远都不可能！ / 微信公众号（个人自媒体，**未核验，不作事实引用**） / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552832&ver=7016&signature=EebnyYllodfKMFrkaVE3aRy14XiXjwrwxGr5t2VrMwH0OwpBZeYzmxQ0pI4-gwrohkyrZPevrEDKWBajGiNgzvqNCJqxKg5mpRVeyKQIdwKTallrM1AjmaOPt*QX7PeW&new=1 / 文章发布时间 2026-10-08 / accessed=2026-10-09

**中国（C）**

- C1 / 国产28nm光刻机SSA800批量交付 良率超90%？媒体辟谣：假消息！ / 快科技（myDrivers） / 媒体 / http://m.mydrivers.com/newsview/1121180.html / 2026-05-10 / accessed=2026-10-09
- C2 / 放下「先进制程」执念，「成熟制程」引领半导体设备逆势狂欢 / 21世纪经济报道 / 媒体 / https://www.21jingji.com/article/20260519/herald/8b430e7d627238215fb039418f39134f.html / 2026-05-19 / accessed=2026-10-09
- C3 / 2025年我国半导体设备进口额391.66亿美元 光刻机占比27% / 快科技（AET电子技术应用转载） / 媒体 / http://www.chinaaet.com/article/3000175961 / 2026-01-28 / accessed=2026-10-09
- C4 / 中芯国际涨超9%，寒武纪、中微公司再创新高，半导体设备龙头估值全景扫描 / 21世纪经济报道（东方财富网转载） / 媒体 / https://finance.eastmoney.com/a/202605203743242779.html / 2026-05-20 / accessed=2026-10-09
- C5 / 多家半导体设备龙头近1月估值回落超20%！8月板块催化节点密集 / 21世纪经济报道 / 媒体 / https://www.21jingji.com/article/20260804/herald/9c8d5faf79576dd1f735f5cee3ace97a.html / 2026-08-04 / accessed=2026-10-09
- C6 / 阿斯麦CEO：美收紧光刻机输华只会令中国自研加速 / 参考消息（云南网转载） / 媒体 / http://news.yunnan.cn/system/2026/05/22/034019376.shtml / 2026-05-22 / accessed=2026-10-09
- C7 / 光刻机概念褪去、三年亏超2.3亿元 华卓精科140亿元估值能否撑起二闯科创板？ / 蓝鲸财经（东方财富网转载） / 媒体 / https://finance.eastmoney.com/a/202608123839439657.html / 2026-08-12 / accessed=2026-10-09
- C8 / 茂莱光学(688502)：深耕精密光学，半导体领域空间广阔（首次覆盖，买入） / 国金证券 / 券商研报 / https://data.eastmoney.com/report/info/AP202606101823417993.html / 2026-06-10 / accessed=2026-10-09
- C9 / 公众号：曜哥谈基 · 中国光刻机：2026 年突破进行时，国产替代加速前行（**营销号，其 SSA800 说法已被证伪**） / 微信公众号 / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552771&ver=7016&signature=u0wxhdCjatr6cA1*gI7-S8zcqgwB-49xzBbtcXaZ7n6zAbV0BUKI91AQw3oa9REMzYH4g8iSbvgcZMwJm8UzniHoVzgjnJbB*65KURSBlGKFsakNoEEqzcL7fjk2eEI0&new=1 / 文章发布时间 2026-03-10 / accessed=2026-10-09
- C10 / 研判2026！中国光刻机行业工作原理、迭代历程、市场规模、进口情况分析 / 智研咨询 / 媒体 / https://www.chyxx.com/industry/1269856.html / 2026-07-01 / accessed=2026-10-09
- C11 / 2024年13类主要半导体设备中国大陆进口金额同比增加8.5% / 中国电子专用设备工业协会（CEPEA） / 行业协会 / https://cepea.com/?list_29/614.html / 2025-01-26 / accessed=2026-10-09
- C12 / 2025年16家中国半导体设备制造企业业绩继续增长 / 中国电子专用设备工业协会（CEPEA） / 行业协会 / https://cepea.com/?list_28/714.html / 2026-04-24 / accessed=2026-10-09
- C13 / 光刻机核心概念股产业链 / 东方财富网·财富号 / 媒体 / https://caifuhao.eastmoney.com/news/20260107173737825818150 / 2026-01-07 / accessed=2026-10-09
- C14 / 两连板张江高科，手握上海微电子超10%股权，还投资了这些企业 / 21世纪经济报道 / 媒体 / https://www.21jingji.com/article/20250924/herald/fea93849e27b92ac8b142847e4fd9143.html / 2025-09-24 / accessed=2026-10-09
- C15 / 美国施压日荷 拟对华禁售两类半导体设备（MATCH 法案） / 芯智讯（AET电子技术应用） / 媒体 / http://m.chinaaet.com/article/3000177096 / 2026-04-07 / accessed=2026-10-09

**台湾（T）**

- T1 / TSMC 4Q25 Quarterly Results（法说会简报） / TSMC Investor Relations / 公告 / https://investor.tsmc.com/english/quarterly-results/2025/q4 / 2026-01-15 / accessed=2026-10-09
- T2 / 台积电：预计今年资本支出将升至520亿美元至560亿美元 / 证券时报 stcn.com / 媒体 / https://stcn.com/article/detail/3595602.html / 2026-01-15 / accessed=2026-10-09
- T3 / 台積電去年Q4營收首破兆元、獲利同登頂！全年EPS 66.25元創新高 / 非凡新聞 / 媒体 / https://news.ustv.com.tw/newsdetail/20260115A001019 / 2026-01-15 / accessed=2026-10-09
- T4 / 半導體設備支出 台灣去年高居全球第二 / 工商時報（转载于工研院 IEK 產業情報網） / 行业协会 / https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=37322b4f2bc44dd38ca9ca066bd821dd / 2026-04-14 / accessed=2026-10-09
- T5 / ASML Holding N.V. FY2025 revenue by country（原档：20-F） / ASML Holding N.V.（经 metricshour 整理） / 公告 / https://metricshour.com/data/geo/asml/fy2025/ / 2026-02-25 / accessed=2026-10-09
- T6 / 美台貿易協議正式拍板！台承諾5,000億美元投資、關稅降至15% / 優分析 UAnalyze / 媒体 / https://uanalyze.com.tw/articles/5511045542 / 2026-01-16 / accessed=2026-10-09
- T7 / 台版晶片法租稅優惠邁入第3年 經部：今年共5家申請 / 中央社（转载于工研院 IEK 產業情報網） / 媒体 / https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=3df683d6496248ff80f7344162803620 / 2026-06-09 / accessed=2026-10-09
- T8 / 曾瀕臨破產，家登如何獲台積電及ASML青睞，成為EUV光罩盒霸主？ / 商業周刊 Smart 自學網 / 媒体 / https://smart.businessweekly.com.tw/Reading/IndepArticle.aspx?id=6021645 / n.d.（内容涵盖至 2025） / accessed=2026-10-09
- T9 / Taiwan Semiconductor Manufacturing (TPE:2330) Stock Price & Overview / StockAnalysis.com / 媒体 / https://stockanalysis.com/quote/tpe/2330/ / 2026-10-08 / accessed=2026-10-09
- T10 / 台積電為何暫不採用 ASML 最新 High-NA？（2026 北美技術論壇） / TechOrange 科技報橘 / 媒体 / https://techorange.com/2026/04/23/tsmc-shows-smaller-faster-chips-without-pricey-new-tool-asml/ / 2026-04-23 / accessed=2026-10-09
- T11 / 台積電逐步縮減8吋產能，聯電、世界先進、力積電成熟製程三雄誰受惠？ / 永豐金證券 豐雲學堂 / 媒体 / https://www.sinotrade.com.tw/richclub/hotstock/696eea2a9ea35c2d3d87fa64 / 2026-04 / accessed=2026-10-09
- T12 / 個股本益比·股價淨值比比較（6770 vs 2330 vs 2303 vs 5347） / FinLab / 媒体 / https://finlab.finance/stocks/compare/6770-vs-2330-vs-2303-vs-5347 / 2026-10-08 / accessed=2026-10-09
- T13 / United Microelectronics (TPE:2303) Stock Price & Overview / StockAnalysis.com / 媒体 / https://stockanalysis.com/quote/tpe/2303/ / 2026-10-08 / accessed=2026-10-09
- T14 / 公众号：无限进步的泡沫板 · EUV 光刻机和台积电//美国对台湾的介入 / 微信公众号 / 媒体 / https://mp.weixin.qq.com/s?src=11&timestamp=1791552848&ver=7016&signature=JloLUvascn6JnH5OtZpL53R7wrsquner3M0At6dLD2Kl9ospGP7wAf1yI2kHZQ5WDJUVbediRn2GoFl2kL*S2gAG9uJlJW6EcEjBCjOE58VU7o9zRoNluA7ogIhtezn8&new=1 / 文章发布时间 2026-03-05 / accessed=2026-10-09

### 公众号通道使用情况（本次运行的透明披露）

本次「完整深度」运行启用了公众号通道，执行结果如下：

- **检索**：主 agent 驱动 Chrome 跑搜狗微信搜索 **1 + 5 = 6 组查询**（中国池用泛查询「光刻机」「光刻机 国产替代」；其余五国用「光刻机 + 国别词」），共获 **约 70 条候选**，**0 条解析失败**。另有 1 组补充查询（「蔡司 光刻机」）连续三次被搜狗软拦（`NO-RESULT`）——**同一时刻对照查询正常，说明是特定查询被拦而非会话限流**，未再重试。
- **国别相关性**：五国池返回的均为「主体该国」的内容，路由有效。
- **时效**：中国池最新一条为 2026-10-08（1 天前）；美国池有 2026-10-08、2026-10-06；德国池有 2026-10-04。**荷兰池全部超过 1 年**（最新 2024-01-26），按用途分级只作背景，未用于支撑「当前进展」。
- **采用情况**：进入正文的公众号来源共 **5 条**（D12、D13、J15、T14、C9），其中 C9 作为**已被证伪的传闻**引用，U14/U15 作为**不可作事实引用的自媒体噪声**引用。其余池内文章均按日期分级处理为背景或弃用。
- **抓取失败（如实报告）**：中国池中最新鲜的 2026-10-08《光刻机国产替代的投资逻辑》**正文抓取失败**（curl 返回 JS 渲染页、静态 HTML 无正文；WebFetch 被微信反爬拦为「环境异常」验证页）；另有 2026-02-20 一篇显示「此内容因违规无法查看」、2024-02-21 一篇显示「已被发布者删除」。三条均未以摘要或推测填充。

---

## 免责声明

本报告基于公开信息整理，仅供研究参考，**不构成任何投资建议**。报告中的市场数据存在来源口径差异（已在正文相应位置标注），估值数据为特定时点快照且各市场口径不完全可比。使用前请以公司公告、监管文件等一手材料自行核实。

数据截至 2026-10-09。
