# 科研与学术 Skills 合集

**中文 | [English](./README.md)**

> 一套围绕「科研全流程 + 学术职业发展 + 通用思维」构建的 AI Agent Skills（技能包）。
> 覆盖 **读文献 → 想问题 → 做研究 → 写论文 → 报项目 → 建知识库** 的完整闭环，
> 并附带公文职场写作与通识思维工具箱。

本仓库共收录 **12 个 Skill**，以中文为主，遵循通用的 `SKILL.md + references/` 目录规范，
理论上可用于任何支持该规范的 Agent 平台（WorkBuddy / Claude Code / Codex 等）。

技能之外，[`prompt-library/`](./prompt-library/README.md) 另存一套论文提示词
（40 套全流程方案 + 30 条英文写作高级指令），覆盖选题到投稿的全流程，原文保留、供直接
复制粘贴使用。该目录不含 `SKILL.md`，随仓库分发但**不注册为技能**。

根目录另有一份 `SKILL.md`，它是**合集总控（router）**：本身不含写作规则，只负责按任务把
Agent 路由到 `skills/` 下对应的子技能。因此本仓库既可整包使用，也可只取其中单个技能。

---

## 目录

- [这些 Skill 是什么](#这些-skill-是什么)
- [Skill 总览](#skill-总览)
- [按使用场景选 Skill](#按使用场景选-skill)
- [快速开始](#快速开始)
- [仓库结构](#仓库结构)
- [组合用法示例](#组合用法示例)
- [来源与版权声明](#来源与版权声明)
- [License](#license)

---

## 这些 Skill 是什么

一个 Skill 本质上是**一段写给 AI 的、可复用的专业工作流**：它由一份 `SKILL.md`
（说明「什么时候触发、按什么流程做」）和若干 `references/`（存放细分的知识、模板、清单）
组成。当你在对话中提出相关需求时，Agent 会自动加载对应 Skill 并按既定方法执行，
从而把「靠临场发挥」变成「按专家流程走」。

本仓库的 Skill 有三个共同特点：

1. **有出处、可追溯**：多数学科知识提炼自经典著作、权威指南或公开论文，而非凭空生成。
2. **可执行、非泛谈**：给的是判断标准、检查清单、写作公式、提示词模板，而不是空泛建议。
3. **边界清晰**：明确写出「什么时候用」「什么时候不用」，避免过度触发和误用。

---

## Skill 总览

### A. 科研写作与成果产出

| Skill | 一句话定位 | 核心内容 |
|---|---|---|
| [research-paper-writing](./skills/research-paper-writing/README.md) | 论文写作与文献综述**全流程**主力技能 | 检索筛选 → 批判精读 → 综述撰写 → 选题 Idea → 逐节写作（引言/摘要/方法/实验/相关工作/结论）→ 投稿自审 → 答辩，附真实范例库与稿件自检脚本 |
| [academic-deai-writing](./skills/academic-deai-writing/README.md) | 去除论文与申报书的 **AI 味 / AIGC 痕迹** | 根因诊断、通用改写、套话清理、篇幅重分配，以及 Introduction/Results/Discussion/创新点分章节专项处理与英文改写 |
| [grant-proposal-ai](./skills/grant-proposal-ai/README.md) | **课题 / 基金申报书**写作指南 | 申报书各部分（立项依据、研究内容、技术路线、创新点、可行性、预算）写作要领 + 40 个结构化提示词模板 |
| [ai-research-methodology](./skills/ai-research-methodology/README.md) | 用 AI 做科研的 **方法论与工具选型** | 文献检索、选题趋势、数据处理、实验设计与创新点挖掘、统计建模、图表生成、投稿返修；分理工科 / 文科两套黄金提示词 |

### B. 文献阅读与知识管理

| Skill | 一句话定位 | 核心内容 |
|---|---|---|
| [critical-paper-reading](./skills/critical-paper-reading/README.md) | **批判性精读**单篇 / 多篇论文 | Keshav 三遍法 + 结构化要素提取 + 批判性思维引擎（质疑清单、论证评估、研究空白识别），输出结构化阅读报告 |
| [socratic-reading](./skills/socratic-reading/README.md) | 用**苏格拉底提问法**读一本书 | 艾德勒四层次阅读（基础/检视/分析/主题）+ 四个基本问题追问链 + 选书与速读产出法 |
| [zettelkasten-notes](./skills/zettelkasten-notes/README.md) | **卡片盒笔记法**（Zettelkasten） | 闪念 → 文献 → 永久笔记 + 连接 + 索引 + 回顾，解决「记了很多笔记却写不出东西」 |

### C. 科研协作与生涯发展

| Skill | 一句话定位 | 核心内容 |
|---|---|---|
| [research-copilot](./skills/research-copilot/README.md) | 严谨**科研协作**总入口 | 数学证明与理论推导、论文写作与审阅、文献调研、创新性分析、选题与方法设计、算法与数值实验、LaTeX；v2 新增受控语言层（ASD-STE100 科研适配版 + 中英稿件检查脚本） |
| [graduate-research-career](./skills/graduate-research-career/README.md) | **硕博生涯与学术职业**指导 | 提炼自 20 部科研指南：入学适应、选题、读文献、科研习惯、写作发表、导师关系、学术诚信、职业选择，附 6 份可填模板 |

### D. 职场写作与通用思维

| Skill | 一句话定位 | 核心内容 |
|---|---|---|
| [ai-gongwen-writing](./skills/ai-gongwen-writing/README.md) | **公文与职场写作**技能库 | 20+ 公文文种（通知/通报/会议纪要/请示/总结/调研报告/领导讲话…）与职场文体（周报/复盘/申请/公开发言/年终总结），各含写作公式 + 分步提示词 + 成稿自检 |
| [modern-thinking-toolkit](./skills/modern-thinking-toolkit/README.md) | **现代思维工具箱**（约 320 个模型） | 决策算法、博弈论、概率与贝叶斯、批判性思维、系统思维、角色思维、认知成长等，自动选 1 主 + ≤3 辅工具输出结论、机制、权衡与行动 |
| [explain-clearly](./skills/explain-clearly/README.md) | **讲清楚 / 帮我看懂**——先诊断读者卡在哪里，再选最省力气的介质 | 五级阶梯（受控文字 → 图表 → 交互网页 → 讲解视频 → 可丢弃小工具）+ 升维/降级判据；理解诊断层（保住事实、证据边界与来源，如实区分"已完成/未验证"）；内置 ASD-STE100 受控英语 Issue 9 完整实现（53 条规则 + 受控词典 + 检查脚本） |

---

## 按使用场景选 Skill

| 我想…… | 用哪个 |
|---|---|
| 写一篇论文 / 学位论文，或某个章节卡住了 | `research-paper-writing` |
| 写文献综述、开题报告的综述部分 | `research-paper-writing` |
| 一口气读懂一批论文、做文献矩阵 | `critical-paper-reading` + `research-paper-writing` |
| 审稿人说我写得太像 AI、AIGC 率过高 | `academic-deai-writing` |
| 想直接抄一套好用的论文提示词 | [`prompt-library/`](./prompt-library/README.md)（非技能，属参考资料） |
| 要写基金 / 课题申报书 | `grant-proposal-ai` |
| 想知道怎么用 AI 提升科研效率（工具、流程） | `ai-research-methodology` |
| 想把读过的书变成能写作的素材 | `socratic-reading` → `zettelkasten-notes` |
| 数学证明、推导、创新点分析、算法实验 | `research-copilot` |
| 研究生阶段迷茫：选题、导师关系、要不要读博 | `graduate-research-career` |
| 写通知、总结、会议纪要、述职报告 | `ai-gongwen-writing` |
| 自己看懂一份材料，或把复杂的东西讲给别人：画图、做交互网页、做讲解视频 | `explain-clearly` |
| 写操作手册 / SOP / 安全规程，或检查稿件语言质量 | `explain-clearly`（受控语言）+ `research-copilot`（语言体检脚本） |
| 做复杂决策、分析一个乱局、找思维模型 | `modern-thinking-toolkit` |

---

## 快速开始

每个 Skill 都是自包含的独立目录，直接复制即可使用。

**方式一：整包安装（一次装齐 12 个技能）**

```bash
git clone https://github.com/<你的用户名>/<仓库名>.git
cp -r <仓库名> ~/.workbuddy/skills/research-skillbox
```

根目录的 `SKILL.md` 是合集总控，`skills/` 下是 12 个子技能。平台先加载总控，再下探 `skills/`
子目录，把 12 个子技能一并注册。

**方式二：单技能安装（全局，所有项目可用）**

```bash
git clone https://github.com/<你的用户名>/<仓库名>.git

# 把需要的 skill 目录复制到用户级 skills 目录
cp -r <仓库名>/skills/research-paper-writing ~/.workbuddy/skills/
cp -r <仓库名>/skills/critical-paper-reading  ~/.workbuddy/skills/
# ……按需复制
```

**方式三：项目级安装（只在本项目生效，便于团队共享）**

```bash
mkdir -p <你的项目>/.workbuddy/skills
cp -r <仓库名>/skills/research-paper-writing <你的项目>/.workbuddy/skills/
```

安装后重启 Agent 或重新载入技能，即可在对话中自动触发，或显式点名调用
（如「用 research-paper-writing 帮我写文献综述」）。

> 目录规范：`SKILL.md` 为入口，`references/` 为知识分片，`assets/` 为模板，`scripts/` 为脚本。
> **整包安装时，子技能统一放在 `skills/` 子目录**：多数平台在目录含 `SKILL.md` 时只下探
> `skills/`，不会扫描同级其他目录，放在这一层才能被子技能被自动注册。
> 如果你的平台要求特定的 frontmatter 字段，可按平台文档补充，正文无需改动。

---

## 仓库结构

```text
.
├── SKILL.md                      # 合集总控（router）：按任务路由到 skills/ 下的子技能
├── README.md                     # 英文版（默认，GitHub 首页渲染）
├── README.cn.md                  # 中文版（本文件）
├── LICENSE                       # MIT 许可证
├── prompt-library/               # 非技能（无 SKILL.md），随仓库分发的参考资料
│   ├── README.md                 #   索引、来源声明与使用原则
│   └── *.md                      #   40 套提示词方案 + 30 条英文写作指令（原文）
└── skills/                       # 以下每个目录 = 一个独立 Skill
    ├── research-paper-writing/
    │   ├── SKILL.md              #   技能入口：触发条件 + 工作流
    │   ├── README.md             #   技能详情页
    │   ├── references/           #   知识分片（分章节指南、清单、范例）
    │   └── scripts/              #   可执行脚本（如稿件自检）
    ├── academic-deai-writing/
    ├── grant-proposal-ai/
    ├── ai-research-methodology/
    ├── critical-paper-reading/
    ├── socratic-reading/
    ├── zettelkasten-notes/
    ├── research-copilot/
    ├── graduate-research-career/
    ├── ai-gongwen-writing/
    ├── modern-thinking-toolkit/
    └── explain-clearly/
```

---

## 组合用法示例

单独用已经能打，串起来威力更大。几个典型链路：

- **从一堆文献到一篇综述**
  `critical-paper-reading`（逐篇精读、产出要素与质疑）
  → `zettelkasten-notes`（沉淀为文献卡片、建立连接）
  → `research-paper-writing`（组织综述结构、撰写与自审）

- **从想法到基金申报书**
  `research-copilot`（论证科学问题与方法可行性）
  → `grant-proposal-ai`（按申报书结构写作、套用提示词）
  → `academic-deai-writing`（去掉套话与 AI 痕迹）

- **读完一本书到能写文章**
  `socratic-reading`（四层次阅读、四个基本问题）
  → `zettelkasten-notes`（永久笔记）
  → `research-paper-writing` / `ai-gongwen-writing`（成文输出）

---

## 来源与版权声明

本仓库部分 Skill 的方法论与素材**提炼自公开出版的著作、课程、白皮书或公开讲稿**
（例如论文写作指南、文献综述方法论、思维模型类课程、公文写作手册等），
由作者进行**结构化整理、改写与再组织**，用于个人学习与研究效率提升。

### 内容分三类，请分别对待

| 类型 | 说明 | 举例 |
|---|---|---|
| **① 提炼改写**（主体） | 方法要点的重新表述与结构重组，非原文照搬 | 各 Skill 的流程、规则、checklist；`explain-clearly` / `research-copilot` 对 ASD-STE100 受控语言的功能性提炼 |
| **② 原文引用**（均已标注来源） | 为保留原味或功能而保留的原句、提示词模板、句式库 | `modern-thinking-toolkit` 的「金句（第 N 讲）」、`prompt-library/` 的提示词原文集、`research-paper-writing` 的学术句式 |
| **③ 已知受版权约束的第三方素材** | 来源方明确限制再分发的素材，仓库已作显著提示 | `research-paper-writing` 引用的 *Academic Phrasebank*（曼彻斯特大学，仅授权个人使用、禁止电子再分发） |

### 引用规范

- **凡直接引用原文之处，均加引号并注明出处**（讲次、书章、作者或来源文件）。
- **能用自己的话表达的，一律自行撰写**——原文引用只保留在「原味不可替代」或「功能性必需」（如可直接复制的提示词）之处。
- **每个 Skill 目录下的 `README.md` 均设有「参考资料 / 灵感来源」清单**，逐条列明来源、作者、出处与借鉴内容，供追溯与致谢。
- 版权受限的第三方素材，已在对应文件中显著标注**使用与分发限制**。

### 权利主张与联系

- 本仓库的 MIT 许可证**仅覆盖作者本人贡献**，**不改变**任何第三方素材的权利归属。
- 若您是某份原始材料的权利人，认为本仓库中的整理内容侵犯了您的权益，
  请通过 Issue 联系，我们会**立即删除或调整相应内容**。

> 建议使用方在引用这些 Skill 产出论文 / 申请书时，遵守所在机构的学术诚信规范，
> AI 产出必须经人工核验，本仓库不承担由此产生的学术责任。

---

## License

本仓库整体采用 **MIT License** —— 详见 [LICENSE](./LICENSE)。
您可以自由使用、复制、修改、合并、发布、分发、再许可和销售本仓库内容，
只需保留版权声明与许可声明。

**重要说明**：MIT 许可证覆盖的是**作者本人的贡献**（代码、文档与方法论组织）。
它**不授予**任何第三方原始素材的权利 —— 部分 Skill 提炼自公开出版物，
相关权利仍归各自权利人所有。详见上方「来源与版权声明」。

> 最终以仓库根目录的 `LICENSE` 文件为准。

---

## 贡献

欢迎 Issue 与 PR：补充新 Skill、修正知识错误、改进工作流、完善来源标注。

提 PR 时请保持每个 Skill 目录自包含，并在 README 中说明触发场景与来源。
