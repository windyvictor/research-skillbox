# evals：本技能的触发测试与任务评测

> 何时用：修改 SKILL.md（尤其 description）或规则后，验证"该触发时触发、不该触发时不触发"，以及新版是否比旧版/无技能时做得更好。

- `trigger_queries.json`：20 条查询（13 条应触发、7 条易混淆的不应触发）。每条在新会话跑 3 次，统计触发率。
- `evals.json`：5 个任务及其断言。分别在"有本技能"与"无本技能/旧版本"条件下运行，逐条判定并引用证据。
- `fixtures/vault/`：10 张样例卡（中英文），故意包含：只有日期没有连接的卡（`2024/12` 不应算连接）、AI 草稿、AI 卡未审升级、超期草稿、断链、近似重名、被更替缺指向、坏例卡。

脚本快速回归（期望结果）：

```bash
python3 scripts/check_card.py --demo
python3 scripts/check_card.py evals/fixtures/vault/只有日期没有连接.md      # 期望：ERROR 无连接，退出码 1
python3 scripts/check_card.py evals/fixtures/vault/AI卡被直接升级.md        # 期望：ERROR AI/外部卡未经人审就升级
python3 scripts/check_card.py evals/fixtures/vault/feedback-frequency.md --strict   # 期望：英文好例，退出码 0
python3 scripts/lint_vault.py evals/fixtures/vault --today 2026-11-01      # 期望：7 类问题各至少 1 条，共 8 条
```
