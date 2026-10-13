# research-copilot

> **严谨科研协作总入口** —— 数学证明、理论推导、论文写作与修改、论文审阅、文献调研、
> 创新性分析、科研选题、算法与数值实验；另附语言层的机械质量底线（受控语言科研适配版），
> 可用脚本检查句长、被动、名词化、术语一致性与 AI 套话。

## 解决什么问题

把「看起来像学术」和「真正对科研有帮助」区分开。核心目标：

- 事实有依据，不虚构论文、DOI、定理、数据；
- 数学推导可检查，不跳过决定性步骤；
- 假设清楚可见，不确定性不被流畅语言掩盖；
- 写作按真实论证过程组织，语言强度匹配证据强度；
- 创新性分析逐组件检查机制，而不是只看关键词组合。

## 何时触发

数学、优化、机器学习及相关方向的科研任务：证明与推导、学术写作与修改、审阅与错误检查、
文献调研与创新性分析、选题与方法设计、算法代码与数值实验、LaTeX。
**不触发**：简单翻译、单词解释、日常软件操作、闲聊等不需要科研推理的任务。

技能内部将任务分 8 类并路由到对应 reference；其中第 8 类（语言质量检查）是交付前的
机械清污，不属于科研推理本身。

## 内容结构

```text
research-copilot/
├── SKILL.md                                   # 触发条件、通用科研工作流、证据层级、禁止事项、自检清单
├── README.md
├── references/
│   ├── academic-writing.md                    # 科学内容与论证：语言强度匹配证据强度
│   ├── controlled-scientific-writing.md       # 语言层机械底线：四档阈值、学术豁免清单、中文受控写法（v2 新增）
│   ├── mathematical-proof.md
│   ├── paper-review.md
│   ├── novelty-analysis.md
│   ├── research-design.md
│   └── algorithm-experiment.md
├── scripts/
│   ├── check_controlled_writing.py            # 统一入口（推荐）：按行判语言 → 分发引擎 → 应用学术豁免
│   ├── check_ste_compliance.py                # 英文引擎（ASD-STE100 Issue 9 可机械判定子集）
│   └── check_plain_language.py                # 中文引擎（中文受控写法 + 通用可读性）
└── assets/
    ├── ste-unapproved-words.tsv               # 科研定制版受控词表（243 条，剔除数学/ML 误报词）
    └── academic-domain-terms.txt              # 领域术语豁免表（138 条，逐条注明豁免理由）
```

依赖 Python 3 标准库，无第三方包。

## 语言体检（v2）

```bash
python3 scripts/check_controlled_writing.py 稿件.md              # 学术档，默认
python3 scripts/check_controlled_writing.py 稿件.md --mode ste   # 严格档，用于对照
python3 scripts/check_controlled_writing.py 中文稿.md --lang zh
python3 scripts/check_controlled_writing.py 稿件.md --no-dictionary  # 只查结构类
python3 scripts/check_controlled_writing.py 稿件.md --json --strict  # hard 级问题时退出码 1
```

两处易错点：

1. **不要用严格 STE 档审理论文**——那会把必需的 hedging（`may`、`should`）和数学术语
   （`assume`、`denote`、`bounds`）判成违规。默认 academic 档已经处理好这些。
2. `--mode ste` 的用途是写**操作规程、实验安全须知、数据采集 SOP**，或用于对照查看
   那些被学术豁免屏蔽掉的条目。

脚本只报线索，不做终判：术语与冗词的区分、hedging 是否恰当，机器判不了，必须人工确认。

## 参考资料 / 灵感来源

> 本节逐条列明参考来源、作者与借鉴内容，供追溯与致谢。
> 本技能为下列材料的**功能性提炼、改写与再组织**，相关权利归原作者与权利方所有；
> 如有疏漏或异议，欢迎提 Issue，我们会立即调整或删除。

| 来源 | 作者 / 出处 | 借鉴内容 |
|---|---|---|
| *ASD-STE100 Simplified Technical English*, Issue 9（2025-01-15） | ASD（欧洲航空航天与防务工业协会），© ASD 2025；官方免费下载：<https://www.asd-ste100.org> | **语言层机械底线的受控语言底座**（v2）：53 条规则的可机械判定子集、未核准词机制；已做**科研适配**——新增学术规则豁免层 + 138 条领域术语表，避免把 hedging 与数学用语误判为违规 |
| [explain-clearly](../explain-clearly/README.md)（本仓库自研技能） | 本仓库作者 | v2 并入其 R1「受控文字」的阈值体系与检查脚本，并向科研场景适配（统一入口脚本、中英自动分派、去 AI 味套话计数） |
| 数学证明规范、审阅清单、创新性分析框架、选题方法等科研工作流 | **原创** | 7 类科研任务的完整工作流、证据层级、禁止事项与自检清单 |

> 如后续引入外部方法论，请在本表增补署名。

## 典型用法

> 「帮我检查这个证明的每一步，找出隐含假设。」
> 「这段引言审稿人说太像 AI 写的，改掉。」（先跑 `academic-writing` 的论证规则，再跑语言体检）
> 「这两个工作是不是重复的？逐组件分析创新性。」
> 「投出前把全文过一遍语言体检。」（`check_controlled_writing.py` 两遍：academic 档 + ste 档对照）

## 版本

- v1（2026-09-22 前）：初版。数学模型/优化方向的科研协作 Skill，7 类任务 + 6 份 references。
- **v2（2026-10-03）**：并入 explain-clearly（原 output-escalation）技能的 R1「受控文字」部分，并做科研适配。
  - 新增 `references/controlled-scientific-writing.md`：把原本定性的写作建议换成可判定的阈值
    （句长 35 词 / 40 字、段落 8 句、名词串 3 词）与可执行的检查。
  - 受控语言源码：ASD-STE100 Issue 9（2025-01-15），全部词条回原书逐条核对页码。
  - **关键设计**：发现完整 STE 与学术写作存在方向性冲突（`may`/`should` 未核准会删掉
    本技能自己要求的 hedging；`assume→THINK`、`bounds→LIMIT` 会破坏数学表达），
    因此新增两个豁免层——academic 模式的规则豁免表 + 138 条领域术语表。
  - 新增统一入口脚本（中英自动分派、学术豁免后处理、去 AI 味套话计数），
    并修正上游脚本的一处漏报 bug 与屈折缺失。
  - 任务分类新增第 8 类；内部检查清单新增第 11 项。详见 `SKILL.md` 第 12 节。
