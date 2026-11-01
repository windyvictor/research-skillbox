# CHANGELOG

## 2026-11-02

- 删除 `references/02-growth-logic.md` 中个人绝对路径行（`来源目录：/Volumes/Mac mini/...`）；用户确认直接删除，不改写成通用说明。

## 2.1.0 — 2026-11-01

依据：karpathy/autoresearch、agentskills.io 规范与最佳实践、Karpathy「LLM Wiki」、Matuschak 常青笔记、zettelkasten.de（Sascha Fast）、Bob Doto《A System for Writing》、Maggie Appleton 成长阶段，以及得到大脑与 IMA 中的知识管理笔记。

### 新增
- **AI 协作协议**（P1-1）：SKILL.md 新增「AI 参与时的规则」；新增 `references/10-ai-collaboration.md`（人机分工、草稿门控、来源锚定、非对称核查、日志、维护会话固定预算、反模式）。
- **卡片状态与来源元数据**（P1-2）：`assets/card-templates.md` 新增 §0.5 YAML 头（status / author / sources / updated / superseded_by）；文献卡、永久卡模板加 YAML 头；SKILL.md 判据表加「卡片成熟度」。
- **本地规则优先 + 默认自治边界**（P1-3）：SKILL.md 新增「先读本地规则」；新增 `assets/vault-rules-template.md`（通用规则文件模板，不绑定路径）。
- **矛盾与更替协议**（P2-1）：`references/04-connection-org.md` 末尾新增「当新证据推翻旧卡」；模板新增 §8 修正卡；SKILL.md 路由与判据各加一行。
- **输出回填**（P2-2）：`references/05-writing-pipeline.md` 末尾新增「输出回填」，把结项回填推广到问答、AI 对话与调研；SKILL.md 路由加一行。
- **体检循环**（P2-3）：`references/09-community-practices.md` 的体检清单改为「系统体检循环」（固定预算 + 5 项指标 + 规则改动按实验留/撤 + 古德哈特提醒）；新增 `assets/review-log-template.md`。
- **库级只读体检脚本**（P2-4）：新增 `scripts/lint_vault.py`（孤岛、断链、近似重名、超期草稿、缺来源、AI 卡未审升级、更替缺指向；`--json`、`--stale-days`、`--exclude`、`--fail-on-issues`）。
- **评测**（P2-5）：新增 `evals/`（20 条触发查询、5 个任务评测、10 张样例卡）。
- **外部导入契约**（P3-2）：`references/10-ai-collaboration.md` §4 与模板 §9：外部导入只进收件箱、一律 draft、必须带 sources；文献卡可选 citekey / doi。

### 修改
- **check_card.py**（P1-4）：新增英文规则组与 `--lang zh|en|auto`；卢曼编号识别改为"数字/数字+字母"（如 21/3d5a），`2024/12`、`3/4` 等日期和分数不再误判为连接；支持 `[[双链|别名]]` 与 `.md` 相对链接；新增 YAML 头检查（缺 status/author/sources 报 WARN；author 为 ai/external 但非 draft 报 ERROR；superseded 缺 superseded_by 报 WARN）；新增 `--json`、`-h/--help`；删除未生效的规则。
  - **行为变化**：有 ERROR 时默认退出码为 1（旧版需 `--strict`）；`--strict` 现在表示 WARN 也算不通过；参数错误或文件不可读退出码 2。
  - YAML 头不再被误判为"缺少标题"。
- **SKILL.md**（P1-5、P2-5、P2-6）：
  - frontmatter 合规：`version`、`summary`、`agent_created` 移入 `metadata`；通过 `agentskills validate`。
  - description 改写：覆盖 AI 协助与知识库体检场景，写明"适用于任何学科"与"不用于"边界。
  - 「系统全图（五阶段）」更正为「六阶段」。
  - 立题门槛统一为"≥10–20 张且彼此有论证关系（经验值）"（同步 04 与模板 §5）。
  - 卢曼数据注明口径（58 本为阿伦斯书中数字，其他来源统计不一）；01 引用注意同步。
  - 新增「常见坑（Gotchas）」；References 表改为「何时读」。
- **大型 reference 渐进披露**（P2-6）：02、04、05、06 文件头新增「本文件目录（按需跳读）」与"何时读哪节"。

### 未采纳
- P3-1 可选主动回忆模块：按用户决定暂不实现。

## 2.0.0
- 48 篇教程主轴 + 阿伦斯原著 + 伴生方法 + 社区实践（09）；check_card.py 初版。
