---
name: writing-research-papers
description: 科研论文写作与文献综述全流程技能（2026-09-24 由 literature-review 技能并入合并，2026-09-26 并入 ML/CV 顶会分节写作指南，2026-09-28 并入杜拉宾 8 版中译本精读）。提炼自 21 本经典论文写作指南（Turabian 9th 英文版 + 芝加哥大学论文写作指南第 8 版中译本全文精读、Ten Simple Rules、How to Write a Lot、Academic Phrasebank、中国学生英语论文常见错误、文再文、图灵学术系列四册等）+ 9 部文献综述方法论著作（Machi & McEvoy 六步法、Creswell 五步、Foss & Walter 六步、Pautasso 十条规则、Ridley 批判性阅读与综合矩阵等）+ 彭思达顶会写作笔记（分节实战指南与真实范例库）+ 1 个稿件自检脚本。覆盖：文献检索与筛选、批判性精读、综述撰写与修改、选题与 Idea、实验设计、逐节写作（引言/摘要/方法/实验/相关工作/结论各有专属指南与句式骨架）、主张-证据对齐、反向提纲与对抗式自审、引用与学术诚信、英语表达、学位论文与答辩、投稿与审稿。当用户请求以下任务时应使用本 skill：写文献综述/综述章节/开题报告综述/研究背景梳理、检索与精读文献、整理文献矩阵、确定研究方向或 idea、设计顶会顶刊实验、撰写或润色科研论文、逐节重写 Introduction/Abstract/Method/Experiments/Related Work/Conclusion、检查段落衔接与逻辑流畅度、claim-evidence 对齐检查、投稿前对抗式自审、写摘要/引言/讨论/结论、检查引用格式与抄袭风险、投稿前稿件自检、准备答辩、克服写作障碍、回应审稿意见。触发词如"写文献综述""综述怎么写""帮我读这批文献""文献太多怎么组织""研究背景怎么写""难题陈述公式""怎么论证这个问题值得做""帮我找 idea""怎么设计实验""帮我写论文""重写 Introduction""摘要再打磨一下""这段读起来顺不顺""可读性自测""检查一下主张有没有证据支撑""数字缩写格式对不对""表格格式规范""投稿前帮我审一遍""润色这段英文""引言怎么写""参考文献格式""回应审稿人""答辩准备"等。
agent_created: true
---

# Research Paper Writing（科研论文写作 · 含文献综述）

## Overview

本 skill 将 21 本论文写作经典书籍（含杜拉宾 8 版中译本全文精读）+ 图灵学术系列讲座 + 9 部文献综述方法论著作的知识提炼为一套可执行系统：**检索阅读 → 综述与立意 → 结构 → 论证 → 语言 → 修改 → 投稿**，并附一个机械自检脚本。核心信条（来自 Ten Simple Rules）：

1. **一稿一主张**：全文只讲一个核心贡献，所有内容为它服务。
2. **C-C-C 贯穿所有尺度**：全文、章节、段落都用"语境（Context）→ 内容（Content）→ 结论（Conclusion）"结构。
3. **时间投向读者最多的地方**：标题、摘要、图表的优先级高于正文。
4. **迭代出好故事**：先写一句一段的提纲，整段重写优于小修小补。
5. **综述是论证不是罗列**：综述要"综"（归类提炼）更要"述"（批判评述），述评 7:3，一切围绕自己的研究问题。
6. **引用可回溯**：每条引文与每处改写都标页码，改写是重构句式而非换词。

## 工作流程（按任务路由）

### 任务 A0：撰写文献综述（完整流程）

1. 先建立四层认知（见 references/literature-review-workflow.md）：综述≠罗列、综述≠背景描述、一切围绕自己的研究问题、综述是"书面论证"；并先分清**基本综述**（课程/硕士）与**高级综述**（博士/独立综述论文）。
2. 按**七阶段**推进：界定主题与范围 → 检索（四组根本问题、五种检索方法、逐步逼近/从细到粗的检索词聚焦、找 seed paper 四法）→ 批判性阅读与笔记（SQ3R、三档阅读、笔记量=成稿 2–3 倍）→ 编码组织（信封法、综合矩阵）→ 构思框架（结构即分类，纵式/横式/纵横结合）→ 撰写（四部分结构、引言六板块、论证自检三问）→ 修改与更新（审核=分析+评价、外部评审）。
3. 组织铁律：**按问题编排，不以作者为线索**；先分析后结论；复原观点背景、提炼所针对的问题、揭示观点间联系。
4. 动笔前对照 references/literature-review-workflow.md 的"常见错误速查"13 项与 references/structure-and-pitfalls.md 的十四项详解自查。
5. 需要完整论证框架（发现式/支持式论证、九类论证模式、谬误清单）查 references/machi-six-steps.md；需要比较四大方法论模型（Machi/Creswell/Foss & Walter/Pautasso）并选型时查 references/methodology-models.md。

### 任务 A：文献检索、精读与编码

1. 检索按**引文追踪法**展开（见 references/literature-reading-and-synthesis.md）：关键词+同义词 → 后向追参考文献、前向用 Cited By → 结果大量重复时才停。
2. 精读用**分层阅读**：核心文献做 200–400 词结构化注释（问题—方法—论点—证据—局限—我将如何用）；批判性问题清单见 references/critical-reading-writing.md。
3. 用**文献矩阵**横向对比多篇文献（列＝作者/目的/方法/样本/关键发现/我的评注），从"空白列"和"冲突列"发现缺口；直接套用 assets/synthesis-matrix-template.md。
4. 选源标准与文献分层见 references/source-selection.md 与 references/source-types-and-citation.md。

### 任务 B：从零撰写论文/章节

1. 先做**立意三问**（见 references/chinese-guides-insights.md）：核心问题是什么？创新属于哪一类（视角/理论/方法/素材）？数据与能力是否可行？
2. 用**难题陈述公式**立起研究合法性（见 references/turabian-argument-craft.md）：我研究 X，因为想弄清 Y，从而帮助读者理解 Z——Z 分概念难题/实践难题两种，引言与开题都靠它论证"这个问题值得做"。
3. 用**引言漏斗四步**搭骨架：领域语境 → However 揭示空白 → So what 意义 → 本文主张+路线图。
4. 按 **IMRaD** 展开正文；写作顺序推荐：方法与结果 → 讨论 → 引言 → 摘要 → 题目。
5. **每写一节，按需加载对应的分节实战指南**（ML/CV 顶会写作经验，含句式骨架与真实范例）：写引言读 `references/introduction.md`（先倒推后顺写、挑战链三版本、方法陈述四版本、"勿写成补丁式"警告）、写摘要读 `references/abstract.md`（三模板：挑战→贡献 / 挑战→洞察→贡献 / 多贡献+优势）、写方法读 `references/method.md`（模块三要素：设计/动机/技术优势，先画 pipeline 图再拆小节）、写实验读 `references/experiments.md`（三大核心问题、消融包、booktabs 表格规范）、写相关工作读 `references/related-work.md`、写结论读 `references/conclusion.md`；每份指南末尾附质量自查清单。
6. 同时对照 references/structure-and-argument.md 与 references/turabian-argument-craft.md 中对应章节（论证五件套详解、承认与回应策略、主张先行 vs 理由先行）。
7. **改写交付格式**（Output Contract）：输出 ① 3–7 条的小节提纲；② 逐段改写并标注段落角色（开场/挑战/方法/优势/证据/局限）；③ 覆盖清晰度、衔接、术语一致性、无支撑主张、缺失证据的自查清单；④ **主张-证据对照表**（`Claim: ... | Evidence: ... | Status: supported/needs evidence`）。

### 任务 C：润色英文段落/全文

1. 先做结构检查（主题句、C-C-C、一句一主题），再做语言检查。
2. **段落流畅度专项检查**（用户问"这段顺不顺/清不清楚"时）：按 references/does-my-writing-flow-source.md 执行——读者视角四问 → **反向提纲**（写出主旨句→各段主题句→各段证据，检查映射关系，映射不上的段落改写或删除）→ 必要时加临时小标题与过渡词定位断点，定稿前删掉。需要外部读者视角时改用 references/readability-self-test.md 的可读性自测（AI 扮演不熟悉该领域的读者，产出问题清单后逐条判断是"缺解释""逻辑断裂"还是模型自身知识不足）。
3. 语言层面重点排查中国学生高频错误：冠词、时态、单复数、respectively、which/that、In this paper/study 混用——逐条对照 references/habits-and-pitfalls.md 的"错误→正确"示例清单。
4. 需要改写句式时，按交际功能从 references/academic-english-phrases.md（基础 8 类）与 references/phrasebank-extended.md（定义/分类/趋势/因果/对比/举例/批判/过渡/图表/摘要/局限）选取匹配句式，投稿信与审稿回复句式也在后者；并遵守时态规则与 hedging 原则。
5. 改写他人观点时：句法+词汇双重重组 + 注明出处，避免 mosaic plagiarism。

### 任务 D：评估/修改已有论文

1. 先跑机械自检：`python3 scripts/check_manuscript.py <稿件路径>`，按报告先清掉 P0，再处理 P1；脚本覆盖不动的语义项再人工查。
2. **快速修订法定结构**（见 references/turabian-argument-craft.md）：只读引言和各章/各节首句，定位全文论证骨架，结构性问题在动句前先动结构。
3. **主张-证据对齐是硬约束**：逐条核对摘要与引言中的每个主张是否被实验证据显式支撑——无证据则补实验、弱化或删除主张（见 references/paper-review.md"Critical Rule"）。
3. **对抗式自审**：以怀疑型审稿人视角按 references/paper-review.md 的五维问题清单（贡献 / 写作清晰度 / 实验强度 / 评估完整性 / 方法设计合理性）逐问作答，每项标 pass / needs revision / needs new experiment，改到无重大拒稿风险为止；常见拒稿信号表也在该文件。
4. 做**反向提纲**检查全文逻辑映射（方法同任务 C 第 2 步）。
5. 按 references/revision-checklist.md 逐项自查（立意→结构→论证→图表→英语→引用→流程→故事线），先修高分值项。
6. **终稿编辑体例专项**（排版/格式级问题）：按 references/chicago-editing-style.md 逐项过——标点与符号、名称术语、数字书写（拼写/数字/科学三路线选定后全程贯彻）、缩写与拉丁缩写、引文改动留痕（省略号/方括号/[sic]/emphasis added，省略不得删去 not/always 等限定语）、表格图版规范（表注四类、小数点对齐）、页码双轨（前置罗马/正文阿拉伯）。
7. 结构性问题的修法是**整段重写**而非小修小补；先重写摘要与引言，再顺流而下。
8. 检查"天真读者"测试：能否一句话复述贡献。

### 任务 E：确定 Idea / 设计实验（科研前期）

1. 选题先走**路线图四步法**（见 references/turing-academic-insights.md）：收集关键文献 → 识别里程碑任务与"原始论文" → 按方法/表征分类 → 找饱和区与空白区，空白即创新点；优先做问题驱动的目标式科研。
2. 实验设计遵循**"以终为始"**：MVP 验证 0→1 可行 → 节点测试给每个里程碑设可验证预期 → 排除法二分定位问题 → 替换法用成熟工具/数据集保准；对所有默认参数做敏感性分析。
3. Idea 打磨与 idea 好坏的判断标准、审稿人期待的实验完整清单，查阅同一文件。

### 任务 F：学位论文与答辩

1. 结构与章节职责、开题报告写法、方法章的可复现性要求，见 references/thesis-and-defense.md。
2. 修改按**四级阶梯**推进：宏观结构 → 段落连贯 → 句子用词 → 一致性校对（Guide to Good Writing 修订法）。
3. 答辩准备：讲稿引言≤3 分钟、结论脱稿、每页幻灯片一个主张；盲审意见区分"建议"与"数据"两类分别处理。

### 任务 G：写作障碍与效率

- 引用 references/habits-and-pitfalls.md 的习惯系统：固定写作时段（每周≥4 小时防御性时段）、每日可判定的具体目标、行为自记录；"写作障碍"的解药就是坐下来写。

### 任务 H：投稿与审稿

- 对照 references/chinese-guides-insights.md：期刊分级与时间规划（提前 6–12 个月）、一稿一投红线、逐条回应审稿意见的格式与策略。
- 投稿信（cover letter）与审稿回复信（response letter）的英文措辞，从 references/phrasebank-extended.md 取用（含同意修改、部分同意并解释、礼貌拒绝三类）。

## References 与脚本（按需加载）

| 文件 | 内容 | 何时读 |
|------|------|--------|
| **分节写作指南（ML/CV 顶会实战，源自彭思达笔记，MIT）** | | |
| `references/introduction.md` | 引言逻辑地图（先倒推后顺写）、开头四版本、技术挑战链三版本、方法陈述四版本+"勿写成补丁式"警告、句式骨架、真实范例索引、质量清单 | 写/改引言 |
| `references/abstract.md` | 摘要三模板（挑战→贡献 / 挑战→洞察→贡献 / 多贡献+优势）、写作前四问、质量清单与范例 | 写/改摘要 |
| `references/method.md` | 模块三要素（设计/动机/技术优势）、先画 pipeline 图再拆小节、Overview 写法、逻辑/段落/句子三层清晰度检查 | 写/改方法章 |
| `references/experiments.md` | 实验三问（强基线/归因消融/泛化边界）、实验规划图、booktabs 表格硬规则与可读性规则、消融包配置、严谨性清单 | 写/改实验章 |
| `references/related-work.md` | 相关工作写作指南 | 写/改相关工作 |
| `references/conclusion.md` | 结论写作指南 | 写/改结论 |
| `references/paper-review.md` | 对抗式自审：主张-证据硬约束、常见拒稿五维信号表、五维终稿自审问题清单、adversarial workflow | 投稿前终审 |
| `references/does-my-writing-flow-source.md` | "写作是否流畅"检查法：读者视角四问、反向提纲、临时小标题法、过渡词分类表 | 段落/章节流畅度检查 |
| `references/readability-self-test.md` | 可读性自测：把"找个人读一遍"变成可执行流程——AI 扮演不熟悉该领域的读者，就研究背景 / 综述 / 结论产出问题清单；含 4 条原文提示词与使用边界 | 自查"读者能不能读懂"时 |
| `references/examples/`（33 个文件） | 真实顶会论文范例库：引言 12 种写法实例、摘要 3 模板实例、方法章模块三要素实例（Instant-NGP/NeuralBody 等），入口 `examples/index.md` | 写对应章节时对照范例 |
| **综述方法（中文方法论体系）** | | |
| `references/literature-review-workflow.md` | 综述七阶段操作主流程 + 核心认知六条 + 常见错误速查 13 项（原 literature-review 技能主文件） | 写任何综述任务的第一站 |
| `references/machi-six-steps.md` | Machi & McEvoy 六步模型全文精读版：论证方案（发现式+支持式）、九类论证模式与推理保障、谬误清单、审核与外部评审细则 | 需要完整论证框架时 |
| `references/methodology-models.md` | 四大模型速览（Machi 六步／Creswell 五步／Foss & Walter 六步／Pautasso 十条）+ 综述类型学 + 模型选用建议 | 选择方法论框架时 |
| `references/critical-reading-writing.md` | SQ3R、批判性七问、Aveyard 评价清单、摘录五类内容、矩阵导写范例、Hart 引用策略、研究者声音技巧 | 阅读与撰写综述时 |
| `references/structure-and-pitfalls.md` | 综述四部分结构、可套用写作模板、GB/T 7714 著录格式、十四类常见错误详解 | 动笔写综述正文前 |
| `references/source-selection.md` | 文献来源分层选择、权威期刊与代表性作者判断、选题类型与文献策略匹配、新旧选题差异 | 确定检索范围与选源标准时 |
| `references/source-types-and-citation.md` | 一次/二次/三次文献分层与使用细则、文献运用三类错误倾向与四个禁忌、直接/间接引用实操 | 判断文献分量、处理中文引用时 |
| `references/literature-reading-and-synthesis.md` | 英文体系：引文追踪法、分层精读与结构化注释、文献矩阵、综述"从罗列到论证"的升级法 | 检索与精读英文文献时 |
| **结构与论证** | | |
| `references/structure-and-argument.md` | 论文结构方法论：C-C-C、引言漏斗、论证五件套（主张-理由-证据-承认-理据）、沙漏结构、图表设计 | 搭结构、写引言/摘要/讨论、设计图表 |
| `references/turabian-argument-craft.md` | 杜拉宾 8 版第一部分精读：题目→问题→难题链、难题陈述公式（X/Y/Z）、warrant 五问法、承认与回应策略、主张先行 vs 理由先行、快速修订法、引言四要素与结论四件事 | 立意论证"问题值得做"、搭论证、修订结构、写引言结论 |
| `references/turing-academic-insights.md` | 图灵学术系列：Idea 路线图四步法、实验"以终为始"（MVP/节点测试/排除法/替换法）、Fact–Logic–Opinion 写作法、结果讨论三层、投稿零容错清单 | 找 idea、设计实验、构建故事线、终稿自查 |
| `references/thesis-and-defense.md` | 学位论文架构与字数分配、开题报告模板、研究方法章写法、修改四级阶梯、答辩准备与盲审应对 | 写学位论文、开题、答辩 |
| **学术英语表达** | | |
| `references/academic-english-phrases.md` | 基础学术英语句库 8 类（背景/空白/目的/方法/结果/讨论/结论/综述引用）+ 时态语态/hedging/paraphrase 规则 | 写或改任何英文段落 |
| `references/phrasebank-extended.md` | 扩展句库 14 类：定义、分类、数量趋势、因果、比较、举例、谨慎与批判、时间表述、过渡衔接、图表描述、摘要、局限性、投稿信、审稿回复 | 需要具体句式、写投稿信与审稿回复 |
| `references/habits-and-pitfalls.md` | 高产写作习惯系统 + 中国学生英语论文高频错误清单（含错误→正确示例对） | 润色英文、克服写作障碍、自我修改 |
| **引用、诚信与编辑体例** | | |
| `references/citation-and-integrity.md` | notes-bibliography vs author-date 两大体例、各类型文献著录模板、直引/改写/概括规则、抄袭类型学与防范、来源评估、文献管理工具 | 处理参考文献、判断抄袭风险、选引用体例 |
| `references/chicago-editing-style.md` | 杜拉宾 8 版第三部分精读：标点符号规范（美式惯例、en/em dash）、名称术语与标题格式、数字书写三路线、缩写与拉丁缩写、引文嵌入铁律与改动留痕（[sic]/方括号/emphasis added）、表格图版规范（表注四类、小数点对齐）、附录学位论文格式（页边距、页码双轨、前置部分顺序） | 终稿排版自查、数字/缩写/表格格式问题、学位论文格式 |
| **语境与流程** | | |
| `references/chinese-guides-insights.md` | 中国语境：选题创新、期刊 vs 学位论文结构、投稿审稿实战 | 选题、学位论文、投稿 |
| `references/revision-checklist.md` | 十板块一页式修改自查清单（综合全部提炼） | 任何修改/评审任务的第一站 |
| `assets/synthesis-matrix-template.md` | 综合矩阵模板（含示例行与学科列调整说明）+ 50 字文献归纳卡模板 | 整理文献时直接复制使用 |
| `scripts/check_manuscript.py` | 投稿前机械自检脚本：章节词数、摘要长度、超长句、寄生词与冗长短语、be 动词/名词化/hedge 密度、respectively 位置、引用体例混用、全半角与空格、缩写未定义、图表引用一致性、时态启发式 | 任何修改/投稿任务的第一步 |

**脚本用法**（纯文本 .md/.txt/.tex，输出 Markdown 报告，P0 存在时退出码为 1）：

```bash
python3 scripts/check_manuscript.py manuscript.md --out report.md
python3 scripts/check_manuscript.py thesis.md --no-strict-imrad   # 学位论文不强制 IMRaD
python3 scripts/check_manuscript.py paper.md --json               # 供程序消费
```

## 使用原则

- **逐节写作/改写**时，第一站加载对应分节指南（introduction/abstract/method/experiments/related-work/conclusion），需要实例时再翻 `references/examples/` 对应子目录；**一次只加载当前要写的那一节**，不要全量加载。
- **主张-证据对齐是硬约束**：摘要与引言的每个主张必须有实验证据支撑，改写交付必须附 Claim-Evidence 对照表。
- **判断"顺不顺"**用反向提纲法（does-my-writing-flow-source.md），不要凭语感。
- **自查"读不读得懂"**用可读性自测（readability-self-test.md）：让 AI 扮演不熟悉该领域的读者，指出术语未解释、逻辑断裂、结论过宽之处。它产出问题清单而非改稿，且不得据此新增原文没有的事实、数据或机制。
- 涉及**写综述/综述章节/开题报告综述**的任务，第一步读 literature-review-workflow.md，按七阶段推进；论证框架查 machi-six-steps.md，模型选型查 methodology-models.md，结构模板与常见错误查 structure-and-pitfalls.md。
- 涉及**文献检索/精读/整理**的任务，查 literature-reading-and-synthesis.md（英文体系）与 critical-reading-writing.md（批判性清单），矩阵直接套用 assets/synthesis-matrix-template.md。
- 涉及**选源与文献分层**的任务，查 source-selection.md 与 source-types-and-citation.md。
- 涉及**找 idea / 定选题 / 设计实验**的任务，必须查阅 turing-academic-insights.md 对应章节。
- 涉及**英文表达**的任务，必须查阅 habits-and-pitfalls.md（查错）与两份句库（选句），不要凭通用语感润色。
- 涉及**结构问题**的任务，必须查阅 structure-and-argument.md 中对应章节。
- 涉及**引用格式/抄袭风险**的任务，英文体系查 citation-and-integrity.md，中文国标查 structure-and-pitfalls.md。
- 涉及**格式/排版/数字/缩写/表格规范**的任务，查 chicago-editing-style.md；引文改动必须留痕，这是学术诚信的机械底线。
- 涉及**论证"问题值得做"/搭建论证**的任务，查 turabian-argument-craft.md（难题陈述公式与 warrant 五问）。
- 涉及**学位论文/开题/答辩**的任务，必须查阅 thesis-and-defense.md。
- 涉及**中国科研语境**（C刊/学位论文/导师协作）的任务，必须查阅 chinese-guides-insights.md。
- 涉及**稿件修改或投稿前检查**的任务，第一步先跑 scripts/check_manuscript.py，再人工补语义项；终审用 paper-review.md 的五维清单做对抗式自审。
- 所有修改任务的收尾动作：用 revision-checklist.md 做完整自查并汇报未通过项；终稿投稿前再过一遍 turing-academic-insights.md 的"投稿零容错"清单。

## 版本说明

- 2026-09-23 v1/v2：由工作区论文写作书籍首创，纳入图灵学术四册。
- 2026-09-24 v3：新增引用与诚信、文献精读、扩展句库、学位论文四份 references 与自检脚本。
- 2026-09-24 v4：**并入原 `literature-review` 技能**（九部综述方法论著作 + 6 份 references + 综合矩阵模板），新增任务路由 A0（综述完整流程）。
- 2026-09-26 v5：**并入 GitHub Master-cai/Research-Paper-Writing-Skills（MIT，源自彭思达老师公开笔记）**：8 份分节写作指南（引言/摘要/方法/实验/相关工作/结论/对抗式自审/流畅度检查）+ 33 个文件的顶会真实范例库；新增反向提纲、主张-证据对照表、对抗式自审工作流与改写交付格式。
- 2026-09-28 v6：**全文 OCR 并精读《芝加哥大学论文写作指南》（杜拉宾第 8 版中译本，508 页扫描版）**：新增 turabian-argument-craft.md（第一部分：难题陈述公式、warrant 五问、承认与回应、快速修订法、引言四要素/结论四件事）与 chicago-editing-style.md（第三部分编辑体例 + 附录：标点/数字/缩写/引文留痕/表格图版/学位论文格式）；任务 B/D 补入对应路由，"引用与诚信"类目扩为"引用、诚信与编辑体例"。
- 2026-10-10 v7：原 `academic-paper-prompts` 技能（40 套提示词方案 + 30 条英文指令）拆解归并——新增 `references/readability-self-test.md`（可读性自测，源自方案 38），原文提示词集移出技能区、改存仓库根 `prompt-library/`（2026-10-10 同日扁平化，原 `prompt-library/paper-writing/`）。
