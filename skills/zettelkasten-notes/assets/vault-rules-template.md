# 卡片库本地规则模板（vault rules template）

> 用途：为一个新的卡片库起草根目录规则文件（可命名为 AGENTS.md / CLAUDE.md / README.md，按所用工具的约定）。
> 本模板不绑定任何路径或学科；尖括号内按自己的库填写，不需要的条目直接删掉。规则文件一旦存在，其约定优先于 zettelkasten-notes 技能的默认值。

```markdown
# 本卡片库规则

## 目录
- 原件：<原件目录>（只读，任何人/AI 不得修改）
- 收件箱：<收件箱目录或标签>（闪念、外部导入、AI 草稿先到这里）
- 卡片：<卡片目录>（文献卡、永久卡、修正卡、结构型笔记、索引）
- 项目：<项目笔记目录>
- 日志：<日志文件>（只追加）

## 字段
- 必填：status（draft | reviewed | evergreen | superseded）、author（human | ai | mixed | external）、sources
- 可选：id、updated、superseded_by、citekey、doi、imported_from

## AI 权限
- 可以：在收件箱新建 draft 卡；提出连接建议；跑体检脚本出报告；在日志末尾追加
- 不可以：改原件；删卡；把卡升为 reviewed/evergreen；批量改名或移动；改本规则文件
- 每次操作后：写一行日志 `## [YYYY-MM-DD] <操作> | <对象> | <结果>`

## 节奏
- 每日：<N> 张卡；收件箱 <N> 天内清空
- 每周：体检 <15> 分钟，只出报告
- 每月：<1> 小时深度体检；系统规则改动按"实验"处理（观察 2–4 周，留或撤）

## 自检
- 每张卡写完跑：`python3 <技能目录>/scripts/check_card.py <卡片> --strict`
- 每周跑：`python3 <技能目录>/scripts/lint_vault.py <卡片目录>`
```
