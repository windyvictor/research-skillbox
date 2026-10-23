---
name: ai-research-methodology
description: AI 辅助科研方法论、工具选型与提示词工程实战指南。当用户询问如何用 AI/ChatGPT/大模型/DeepSeek 辅助科研工作（文献检索与精读、选题与热点趋势、数据预处理与特征工程、实验设计与创新点挖掘、实证分析与统计建模、质性编码、文献计量与 PRISMA 系统综述、AI Code 构建与改进 Baseline、消融实验自动化、论文图表生成、投稿与返修回复）、如何选择科研 AI 工具、或需要制定 AI 辅助科研工作流与学术诚信规范时使用。本技能应在涉及"AI + 科研/学术研究"的方法论、提示词工程、工具推荐、流程设计类问题时触发，并按学科（理工科/文科）与环节提供黄金提示词模板。
agent_created: true
---

# AI 辅助科研方法论与提示词工程（AI Research Methodology & Prompt Engineering）

## 概述

本技能整合四份权威方法论指南（《AI for Research 工具选型指南》《AI 时代科研方法论白皮书》《ChatGPT in Scientific Research and Writing 入门指南》《Three Ways ChatGPT Helps Me in My Academic Writing》）与两份学科实战手册（理工科版、文科版《提示词工程实战手册》），提炼为可执行的 AI 辅助科研工作流与"拿来就能用"的黄金提示词模板。

核心理念：**AI 是方法与加速器，专业判断（专业 X）是主体**；所有 AI 产出必须经研究者核验，警惕 AI 幻觉与引用造假。

## 使用方式（按需求路由）

| 用户需求 | 加载文件 |
|---|---|
| 工具选型（"哪个 AI 适合做文献综述/统计分析/写作？"） | `references/methodology-guides.md` 第 1 章（按文献、假设、统计、写作四环节选工具） |
| 科研全流程设计（"帮我设计 AI 辅助科研工作流"） | `references/methodology-guides.md` 第 2 章（七步工作流 + 五项原则） |
| 具体环节怎么用 ChatGPT（初稿、润色、审稿反驳、实验核查） | `references/methodology-guides.md` 第 3、4 章（含英文 prompt 原文） |
| **理工科**：文献检索、数据预处理与特征工程、实验设计、创新建模、AI Code 构建/改进 Baseline、消融实验、论文图表 | `references/prompt-engineering-stem.md`（8 环节 + 7 个代码提示词，模板原文） |
| **文科**：文献检索、量表检验与 CMB、因果识别（DID/IV/RDD/PSM）、中介调节、质性编码、文献计量（CiteSpace/VOSviewer）、PRISMA 系统综述、稳健性检验 | `references/prompt-engineering-humanities.md`（8 环节 + 7 个实战模板，模板原文） |
| 论文写作层的方法论与去 AI 味（润色、降 AIGC、查重、可读性自测） | 转入配套技能 `academic-deai-writing`（去 AI 味）与 `writing-research-papers`（可读性自测、修改 Checklist） |
| 需要可直接复制粘贴的网络流传提示词原文（40 套方案 + 30 条英文指令） | 仓库 `prompt-library/`（资料，非技能） |
| 课题申报书写作 | 转入配套技能 `grant-proposal-ai` |

**执行要点**：模板中的 `[ ]` / `【 】` 占位符必须替换为用户的具体研究对象、数据集、指标后再发送；占位符信息不足时先向用户询问，不要替用户虚构研究内容或实验数据。

## 核心工作流（速查）

1. **文献环节**：AI 用于检索线索、翻译、提炼四要素卡片（贡献/方法/结果/局限）；引用必须逐条回溯源文献核实，AI 常编造文献。
2. **选题与假设**：让 AI 生成多角度研究问题清单 → 研究者筛选 → 再让 AI 找漏洞（自我评审）；文科选题须落到 Research Gap。
3. **数据与实验**：AI 生成可复现代码（固定随机种子、无数据泄露）；实验结果必须真实跑出，**严禁让 AI"生成"数值**。
4. **建模与创新**：以"1–2 个基线 + 1 个创新方向"为提问结构，配套消融实验与可解释性分析（SHAP/LIME）。
5. **写作与投稿**：AI 承担结构化、润色、语言打磨；学术观点与论证由作者主导。投稿信/返修回复须逐条致谢并说明修改位置。
6. **合规底线**：遵守期刊/资助机构的 AI 使用披露要求；不将未发表数据、敏感信息输入公开模型；不将 AI 列为作者；对 AI 幻觉零容忍。

## 详细资料（references/）

- `methodology-guides.md` — 四份方法论指南的完整提炼：工具清单、七步科研工作流、全阶段 prompt 模板、学术诚信注意事项。
- `prompt-engineering-stem.md` — 理工科手册提炼：8 环节黄金提示词（写作与润色类转配套技能）+ AI Code 构建 Baseline（3 场景）+ 改进 Baseline（4 策略：结构改进/训练策略/可视化/消融自动化）+ 全流程检查清单。
- `prompt-engineering-humanities.md` — 文科手册提炼：8 环节黄金提示词（写作与润色类转配套技能）+ 实证分析（问卷量表/因果推断/质性编码）+ 文献计量与 PRISMA 系统综述（4 策略）+ 稳健性检验清单。
