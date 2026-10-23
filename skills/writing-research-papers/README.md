# writing-research-papers

> 科研论文写作与文献综述**全流程**技能 —— 从检索一批文献，到投出最终稿。

## 一句话定位

把「写论文」这件模糊的大事，拆成**有指南、有句式、有范例、有检查清单**的可执行步骤，
覆盖从文献检索到投稿返修的每一个环节。

## 解决什么问题

- 文献太多，不知道从哪里读起、怎么组织成综述
- 论文写不出来，每一节（引言/摘要/方法/实验/相关工作/结论）都缺招式
- 段落读起来「不顺」，逻辑断层，说不清为什么值得做
- 主张（claim）与证据（evidence）对不上，被审稿人抓
- 投稿前不知道该自查什么，答辩前一片茫然

## 何时触发

写文献综述 / 综述章节 / 开题报告综述 / 研究背景梳理；检索与精读文献；整理文献矩阵；
确定研究方向或 idea；设计顶会顶刊实验；撰写或润色论文；逐节重写 Introduction /
Abstract / Method / Experiments / Related Work / Conclusion；检查段落衔接与逻辑流畅度；
可读性自测；claim-evidence 对齐检查；投稿前对抗式自审；回应审稿人；准备答辩。

## 内容结构

```text
writing-research-papers/
├── SKILL.md                          # 总工作流与路由
├── references/
│   ├── literature-review-workflow.md # 文献综述六步法工作流
│   ├── machi-six-steps.md            # Machi & McEvoy 六步法
│   ├── methodology-models.md         # 各家综述方法论对比
│   ├── literature-reading-and-synthesis.md
│   ├── critical-reading-writing.md   # 批判性阅读与写作
│   ├── source-selection.md / source-types-and-citation.md
│   ├── structure-and-argument.md     # 结构与论证
│   ├── introduction.md / method.md / abstract.md
│   ├── experiments.md / related-work.md / conclusion.md
│   ├── revision-checklist.md         # 修改检查清单
│   ├── citation-and-integrity.md     # 引用与学术诚信
│   ├── academic-english-phrases.md / phrasebank-extended.md
│   ├── chicago-editing-style.md      # 芝加哥格式规范
│   ├── turabian-argument-craft.md / turing-academic-insights.md
│   ├── chinese-guides-insights.md    # 中文写作指南精要
│   ├── thesis-and-defense.md         # 学位论文与答辩
│   ├── paper-review.md / habits-and-pitfalls.md
│   ├── does-my-writing-flow-source.md
│   ├── readability-self-test.md      # 可读性自测（读者视角）
│   └── examples/                     # 真实范例库（引言 13 版 / 方法 / 摘要 3 版）
├── assets/
│   └── synthesis-matrix-template.md  # 文献综合矩阵模板
└── scripts/
    └── check_manuscript.py           # 稿件格式自检脚本
```

## 参考资料 / 灵感来源

> 本节逐条列明参考来源、作者与借鉴内容，供追溯与致谢。
> 本技能为下列材料的**结构化整理、改写与再组织**；少量功能性文本（学术句式、可读性自测提示词）
> 为**原文引用并已标注来源**，见下表。
> 相关权利归原作者与出版方所有；如有疏漏或异议，欢迎提 Issue 指出，我们会立即调整或删除。

### A. 论文结构与论证

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *A Manual for Writers of Research Papers, Theses, and Dissertations* (9th ed.) | Kate L. Turabian | 论文结构、引用体例、论证技艺 |
| 《芝加哥大学论文写作指南》（杜拉宾第 8 版中译本） | 凯特·杜拉宾 著，雷蕾 译，新华出版社 2015 | 编辑体例（拼写/标点/数字/缩写/图表）、论证框架 |
| *Ten Simple Rules for Structuring Papers* (2017) | Brett Mensh & Konrad Kording | 论文结构规则、C-C-C 与沙漏模型 |
| *How to Write a Research Paper*、*Handbook for Writing Research Paper* | — | 结构补充 |

### B. 写作习惯与常见错误

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *How to Write a Lot* (2019, 2e) | Paul J. Silvia | 写作习惯养成、每日可判定目标 |
| *The Most Common Habits from 200+ English Papers by Graduate Chinese Engineering Students* | Felicia Brittman | 中国学生英语论文常见错误 |
| *The Facts On File Guide to Good Writing* | Martin H. Manser | 写作规范 |
| *Academic Writing: A Handbook for International Students* | Stephen Bailey | 学术写作单元训练 |

### C. 学术英语句式与语体

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *Academic Phrasebank* (2023) | John Morley，曼彻斯特大学 | 按交际功能（move）组织的句式骨架——本技能句式库的核心资源 |
| *PhraseBook for Writing Papers and Research in English* | Stephen Howe & Kristina Henriksson | 定义、数据呈现、比较对照、衔接等句式 |
| *Academic Writing* | Jeffrey R. Wilson，哈佛大学 | 学术写作方法 |
| *English for Academic Purposes: An Advanced Resource Book* | Ken Hyland & Liz Hamp-Lyons | genre analysis 理论、hedges/boosters 语料库研究 |
| *CARS 模型* | John M. Swales | 引言三语步（建立领域→指出缺口→占据缺口） |

> ⚠️ **版权提示（Phrasebank 类素材）**：*Academic Phrasebank* 为**曼彻斯特大学的知识产权**
> （Copyright © 2023 The University of Manchester），官方授权为**下载者个人学习使用**，
> 并明确声明**禁止以电子方式（邮件、网络下载等）再分发**。
> - **短语本身**属 content-neutral 的通用学术表达，作为写作素材使用**不构成抄袭**；
> - 但**该书的编排汇编受版权保护**，本仓库保留的仅为**部分代表性句式**，完整资源请访问官方免费站点
>   <https://www.phrasebank.manchester.ac.uk/>。
> - 本仓库的 MIT 许可**不覆盖**此类第三方素材。

### D. 文献综述方法论

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *The Literature Review: Six Steps to Success*（中译本《怎样做文献综述——六步走向成功》，上海教育出版社 2011） | Lawrence A. Machi & Brenda T. McEvoy | 六步法主流程 |
| 五步结构 | John W. Creswell | 综述结构 |
| 六步法 | Sonja K. Foss & William Waters | 综述流程 |
| *Ten Simple Rules for Writing a Literature Review* | Marco Pautasso | 十条规则 |
| *The Literature Review: A Step-by-Step Guide for Students* (2012) | Diana Ridley | 批判性阅读、综合矩阵 |
| *Writing a Critical Review of Literature* (2018) | Shah & Ahmed | 批判性综述 |
| *Doing a Literature Review* (1998) | Chris Hart | 引用策略 |
| *Doing a Literature Review in Health and Social Care* (2014) | Helen Aveyard | 阅读清单 |
| SQ3R 阅读法 | Francis P. Robinson | 分层精读 |

### E. 中文写作指南

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| 《学术论文阅读与写作》 | 文再文，北京大学 BICMR | 分维度质疑、读写方法 |
| 《硕博论文写作与研究方法全攻略 3.0》 | — | gap 识别、常见质量缺陷 |
| 《论文成长笔记（2025 最新版）》 | — | 检索技巧、阅读深度分级 |
| 《论文白皮书》 | 小木虫 | 检索五法 |
| 【图灵学术】系列四册：《如何确定自己的 idea》《顶会顶刊的实验思路是如何炼成的》《高水平写作思路与方法》《写作常见问题与误区》 | 图灵学术 | 选题、实验思路、写作方法与常见误区 |

### F. 顶会分节写作与范例库

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| 公开学习笔记 | 彭思达（北京大学），github.com/pengsida/learning_research | 引言/摘要/方法/实验/相关工作/结论的分节实战指南与真实范例（含 13 版引言范例） |
| Research-Paper-Writing-Skills | Master-cai（MIT License） | 上述笔记的结构化整理，2026-09-26 并入本技能 |

### G. 可读性自测（原文引用的提示词）

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| 《40 套 AI 提示词》方案 38 | **原始作者与出版信息未标注**（网络流传资料） | 用"不熟悉领域的读者 / 评审专家"视角自测可读性的 4 条提示词（**原文引用**），见 `references/readability-self-test.md` |

> ⚠️ 该来源为未标注作者的网络流传资料，版权状态不明。提示词为功能性文本，按原文引用并标注来源，
> 本仓库不主张任何权利；如您是原始作者并希望署名或移除，请通过 Issue 联系，我们将立即处理。

### H. 本项目自研部分

| 内容 | 作者 | 说明 |
|---|---|---|
| `scripts/check_manuscript.py` 稿件自检脚本 | 本项目作者 | 投稿前格式与规范自检 |
| 全流程工作流设计、文件组织与路由逻辑 | 本项目作者 | 将上述材料组织为可执行的 Skill 结构 |
| `readability-self-test.md` 的流程编排与使用边界 | 本项目作者 | 将方案 38 的提示词组织为可执行的自测流程 |

## 典型用法

> 「帮我写一篇关于多视图聚类的文献综述，我手上有这 30 篇论文。」
> 「我这篇论文的 Introduction 被审稿人说『问题不清、动机不足』，帮我重写。」
> 「投稿前帮我做一遍对抗式自审，重点查 claim-evidence 对齐。」
