# Research Skillbox 科研技能导航

**[English](./README.md) | 中文**

> 一套围绕科研全流程、学术职业发展与通用思维构建的 11 个 AI Agent Skills。

它们共同覆盖一条完整的实践链路：**读文献 → 想问题 → 做研究 → 写论文 → 报项目 → 建知识库**。此外还包括研究生涯指导、公文与职场写作、清晰解释和通用思维工具。

每个技能都是写给 AI Agent 的可复用专业工作流，明确规定何时触发、需要什么证据、按什么流程执行，以及怎样判断任务完成。目标是把临场拼提示词，变成可追溯、可执行的方法。

## 状态说明

> [!IMPORTANT]
> 本仓库是**导航页，不是可安装的技能合集**。旧合集文件已从当前分支移除。最新版、安装说明、问题反馈和参与修改，均以下方 11 个独立仓库为准。旧合集仍可从 Git 历史恢复。

原 `research-skillbox` 合集已于 **2026 年 11 月 3 日**拆分为 11 个独立仓库。每个技能现在独立维护版本历史、中英文 README、适用的测试或评测案例，以及安装入口。

原 `ai-research-methodology` 不再作为独立技能维护；其中有效内容已经分别融入论文阅读、论文写作、基金申请、科研协作和科研生涯技能。

## 当前维护的 11 个技能

| 技能 | 用途 |
|---|---|
| [academic-deai-writing](https://github.com/windyvictor/academic-deai-writing) | 在保留事实、限定、引用和作者声音的前提下，修订科研文本并清理模板化表达。 |
| [ai-gongwen-writing](https://github.com/windyvictor/ai-gongwen-writing) | 根据文种、受众和行动目标起草或修改公文与职场材料。 |
| [clear-explainer](https://github.com/windyvictor/clear-explainer) | 诊断理解卡点，用文字、图表、交互网页或视频讲清概念、机制和流程。 |
| [graduate-research-career](https://github.com/windyvictor/graduate-research-career) | 为研究生涯、导师协作、论文发表和学术职业选择提供可执行建议。 |
| [grant-proposal-ai](https://github.com/windyvictor/grant-proposal-ai) | 根据当年项目要求和真实研究基础组织基金申请论证。 |
| [modern-thinking-toolkit](https://github.com/windyvictor/modern-thinking-toolkit) | 为复杂决策、系统、博弈、学习和批判性思考选择少量合适模型。 |
| [paper-deep-reading](https://github.com/windyvictor/paper-deep-reading) | 在明确来源和证据边界的前提下精读、比较和批判评估学术论文。 |
| [research-copilot](https://github.com/windyvictor/research-copilot) | 严谨协作完成证明、研究设计、算法实验、创新性分析和复现核验。 |
| [socratic-reading](https://github.com/windyvictor/socratic-reading) | 用苏格拉底追问与分析阅读法带读书籍和长篇材料。 |
| [writing-research-papers](https://github.com/windyvictor/writing-research-papers) | 根据可回溯证据撰写和修改论文、综述、投稿材料与审稿回复。 |
| [zettelkasten-notes](https://github.com/windyvictor/zettelkasten-notes) | 把阅读与思考沉淀为可复用、可连接并能支持长期写作的卡片。 |

## 按使用场景选择技能

| 我想…… | 从这里开始 |
|---|---|
| 精读论文、核对方法与证据，或比较多篇论文 | [paper-deep-reading](https://github.com/windyvictor/paper-deep-reading) |
| 撰写论文、文献综述、投稿材料或审稿回复 | [writing-research-papers](https://github.com/windyvictor/writing-research-papers) |
| 去掉科研文本的模板化 AI 味，同时保留科学含义 | [academic-deai-writing](https://github.com/windyvictor/academic-deai-writing) |
| 推导证明、分析研究想法、设计算法实验、查新或复现 | [research-copilot](https://github.com/windyvictor/research-copilot) |
| 准备基金或课题申请书 | [grant-proposal-ai](https://github.com/windyvictor/grant-proposal-ai) |
| 把阅读与思考沉淀为长期可用的知识系统 | [zettelkasten-notes](https://github.com/windyvictor/zettelkasten-notes) |
| 用检视阅读、分析阅读或主题阅读读一本书 | [socratic-reading](https://github.com/windyvictor/socratic-reading) |
| 处理研究生涯、导师协作、论文发表或学术职业问题 | [graduate-research-career](https://github.com/windyvictor/graduate-research-career) |
| 把复杂概念、机制或流程讲清楚 | [clear-explainer](https://github.com/windyvictor/clear-explainer) |
| 撰写公文或职场材料 | [ai-gongwen-writing](https://github.com/windyvictor/ai-gongwen-writing) |
| 分析复杂决策、系统、博弈或学习问题 | [modern-thinking-toolkit](https://github.com/windyvictor/modern-thinking-toolkit) |

## 典型组合工作流

- **从一批论文到一篇综述：** `paper-deep-reading` → `zettelkasten-notes` → `writing-research-papers`
- **从研究想法到基金申请：** `research-copilot` → `grant-proposal-ai` → `academic-deai-writing`
- **从读完一本书到形成写作素材：** `socratic-reading` → `zettelkasten-notes` → `writing-research-papers`
- **从技术结果到清晰讲解：** `research-copilot` 或 `paper-deep-reading` → `clear-explainer`

## 应该使用哪个仓库？

- 安装或更新技能：克隆对应的独立仓库。
- 反馈具体问题或提交修改：到对应技能仓库创建 Issue 或 Pull Request。
- 查找全部技能或回看历史：使用本仓库。

```bash
git clone https://github.com/windyvictor/paper-deep-reading.git
```

把 `paper-deep-reading` 换成需要的技能名即可。各仓库 README 中提供具体的安装和使用说明。

感谢访问和 Star。本公开导航页保留整套技能的共同身份与历史，11 个技能则在各自仓库继续更新。

## 许可与历史材料

本仓库历史快照继续适用原有许可证和第三方材料声明。每个独立仓库均包含自己的许可证与来源说明；使用或再分发前，请以对应独立仓库的说明为准。
