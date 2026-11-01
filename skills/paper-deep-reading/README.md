# paper-deep-reading

> **论文深度精读** —— 读得快、读得全、读得狠、讲得透、落得成卡。

## 一句话定位

以**阅读目的**锁定深度，以三遍法控制阅读节奏，以结构化框架与 Claim–Evidence–Warrant 矩阵提取要素，
以批判性思维引擎与可执行检验协议主动质疑每一篇论文，
以 AI 导师式精读协议（学术时空坐标、认知阶梯 L1–L4、讲解载体阶梯、苏格拉底式辩证、证据四级标签、AI 核验协议）
讲透核心文献，并以可选**领域地图**与**卡片盒导出**把阅读沉淀为研究资产，
最终产出**可直接用于综述写作、选题与知识库入库**的结构化阅读报告。

## 何时触发

1. **学术文献输入**：论文链接命中学术平台域名（arXiv、IEEE Xplore、ACL Anthology、
   ACM DL、SpringerLink、ScienceDirect、PubMed、Semantic Scholar、Google Scholar、
   ResearchGate、bioRxiv、medRxiv、SSRN、CNKI、万方、维普、顶会官网、doi.org 等）；
   本地 PDF / Word / Markdown / TeX / ePub 学术文档；粘贴文本含 ≥2 项学术结构标记
   （Abstract / Keywords / Introduction / References / DOI / arXiv ID）。
2. **结构化阅读意图**：速读 / 精读 / 深读 / 批判性阅读；要素提取；多篇对比；
   评估论文质量；找研究空白；领域地图；卡片盒导出；阅读目的（找 idea / 复现基线等）；
   合书复述 / Claim–Evidence 矩阵。

## 内容结构

```text
paper-deep-reading/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── assets/
│   └── interactive-tutorial-prompt.md  # 交互式讲解网页生成提示词模板（含批判嵌入）
└── references/
    ├── critical-checklists.md   # 质疑清单、CEW、检验协议、反模式
    ├── cognitive-ladder.md      # AI 导师式精读协议（时空坐标、认知阶梯、载体、辩证、核验）
    └── report-templates.md      # 结构化阅读报告与卡片盒导出模板
```

## 参考资料 / 灵感来源

> 本节逐条列明参考来源、作者与借鉴内容，供追溯与致谢。
> 本技能为下列材料的**结构化整理、改写与再组织**，不含原书原文的大段复制。
> 相关权利归原作者与出版方所有；如有疏漏或异议，欢迎提 Issue 指出，我们会立即调整或删除。
> **禁止**把未打开全文的来源写成逐步条目（例如 Nature Cornwell 2026 七步）。

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *How to Read a Paper* | S. Keshav（ACM SIGCOMM CCR） | 三遍法；5C；图表与虚拟复现 |
| Rice Cain Project 阅读材料 | Michael Purugganan & Jan Hewitt（Rice University） | 读前/读后提问清单 |
| 逐节猜答案法 | Mihai Pop（University of Maryland） | 主动阅读：先猜作者下一步再验证 |
| 《学术论文阅读与写作》 | 文再文，北京大学 BICMR | 分维度质疑 |
| 《如何高效检索和阅读文献》 | 【图灵学术】 | 10 项挑战清单、笔记五要素、文献树 |
| 《硕博论文写作与研究方法全攻略 3.0》 | — | research gap 识别、8 大质量缺陷 |
| 《论文成长笔记》《论文白皮书》 | — | 9 问清单、三级阅读深度、查缺补漏 |
| 结构化报告模板与导出格式规范 | 本项目作者 | Markdown / Word / PDF 报告模板与排版规范 |
| 文献速读员（Tabbit 妙招 v1.0） | Tabbit 平台 | 速读档双轨要素、取全文路由与降级阶梯、导出排版、GB/T 7714、奥卡姆与第一性原理；其"只客观呈现"立场未采用 |
| 王树义《AI 加持下，啃论文能从「苦差事」变「探险」吗？》 | 公众号「玉树芝兰」，2025-05 | 讲解载体阶梯、交互式教程提示词 |
| 王树义《如何用 AI 帮你把论文读透？》 | 公众号「玉树芝兰」，2025-11 | 学术时空坐标、认知阶梯 L1–L4、苏格拉底辩证、全源可核查引证 |
| PLOS Comp Biol: Ten simple rules for reading a scientific paper | Mirzoyan et al., https://doi.org/10.1371/journal.pcbi.1008032 | 阅读目标先行；文章类型；六问骨架；图表拆解；善意批判；谈出来并接到自己研究 |
| 李沐「如何读论文」及相关笔记 | 公开笔记转写（如 huweim.github.io 等） | 摘要–结论–关键图第一遍；合书能讲清；可跟进的简单有效 |
| 李沐研究价值公式 | 公开博客笔记 | 新意×有效×问题大小（1/10/100）；研究问题 vs 工程问题 |
| Claim–Evidence–Warrant（Toulmin） | 写作教学材料（如 CUNY JJ Honors 介绍页） | 主张–证据–warrant 三元组；缺 warrant 则证据无关 |
| Oxford Bodleian: Evaluating AI-generated references | https://libguides.bodleian.ox.ac.uk/ai-for-literature-searching/evaluating-ai-references | DOI/URL 核验；未查阅不引；对照原文查局限 |
| Faithfulness / 引用支持粒度 | 相关 arXiv 研究（如 2408.12398 脉络） | Full / Partial / No support；Partial 须拆句 |
| ML Reproducibility Checklist v2.0 | Joelle Pineau et al. | 假设、数据、超参、误差、算力、复现命令快检 |
| NeurIPS / ICLR Reviewer Guidelines（近年公开版） | neurips.cc / iclr.cc | 按贡献类型解读；理论假设；use-inspired 基线；清晰可复现 |
| Michael Nielsen《Principles of Effective Research》要点 | Andy Matuschak 笔记等转述 | 新方向深读约 10 篇优先于浅扫数百；跟踪期浅扫+精选深读 |
| Cal Newport：难文预处理 / Closed-Loop Research | calnewport.com | QEC 预处理；Research Bible 与 little bet（读后出口可选） |
| Matt Might: How to peer review | matt.might.net | 边读边记；先优点；gut reaction 防确认偏误 |
| Michael Mitzenmacher: How to read a research paper | 公开 PDF | 批判性与创造性阅读；1–2 句总结 |
| Ahrens / Zettelkasten 概念澄清 | zettelkasten.de | fleeting → literature notes → permanent notes；自己的话与链接 |
| Zotero 批注 → Obsidian 文献笔记实践 | 公开教程（如 professorkenton.com） | 批注结构导入；文献笔记≠永久笔记 |
| Nature Careers: Jacques Cornwell「Seven steps…」(2026) | https://www.nature.com/articles/d41586-026-01209-0 | **策略先行**（全文本轮未核；勿冒充逐步七条） |
| Nature Reviews: How to critically appraise an article | 公开综述 | 设计匹配问题；方法学关键特征；专用清单 |
| 中文笔记归纳（得到大脑 / IMA 等，见迭代建议稿） | 13 问 / PaperForge、12 项 Prompt、一线博士 6 步 SOP、学术创新三层审视、「你真的会读文献么」2A/2B/2C、卡片盒实操、毛政元文献阅读技巧等 | 阅读目的；思路重建；四级标签；检验协议；A/B/C；领域地图；读后六件套；合书复述 |

## 典型用法

> 「这是 5 篇关于深度强化学习码垛的论文，帮我逐篇精读并做对比。」
> 「这篇论文结论看起来很漂亮，帮我找找它没说的研究空白。」
> 「我要开一个新方向，先做领域地图，再标精读候选。」
> 「精读完导出文献卡草稿到我的卡片盒，想法卡先放候选等我批准。」
> 「阅读目的是复现基线，按 L3 做 CEW 矩阵和一周验证计划。」
