# ASD-STE100 受控词典（Part 2 · Issue 9）

**来源**：ASD-STE100 *Simplified Technical English*, Issue 9, 2025-01-15, General introduction (pp.35–42) +
Part 2 – Dictionary (pp.131–434)。© ASD, 2025。官方免费下载：<https://www.asd-ste100.org>。
本文件是字典**机制的功能性提炼 + 高频映射的事实性摘录**；完整词条（例句、help、完整替代词）以官方文档为准。

**规模**：**875 个核准词（approved）** + **1274 个未核准词（not approved）**。核准词是技术写作中最常用的词。

---

## 1. 字典是干什么的

写作规则（Part 1）管**语法和风格**；受控词典（Part 2）管**你能用哪些词、以及这些词的哪个含义能用**。
两者缺一不可：规则说"只能一句一事"，字典说"这件事只能用哪个词说"。

**为什么需要它**：技术文档的读者往往不是英语母语者。英语一词多义、同义词过多、句式复杂都会造成误解；
在航空等领域，误读维修文档直接关系安全。受控词典把"同义词爆炸"压成"一个意思一个词"。

## 2. 条目的解剖结构

字典是一张长表格，每页 4 列：

| 列 | 表头 | 内容 |
|---|---|---|
| 1 | `Word (part of speech)` | 词 + 词性缩写；动词后另列允许的词形 |
| 2 | `Approved meaning / ALTERNATIVES` | 核准词的**核准含义**（定义）；或未核准词的**核准替代词** |
| 3 | `STE EXAMPLE` | 用核准词写出的正确例句 |
| 4 | `Non-STE example` | 用未核准词写的错误例句 |

**读法**：行内横向读（词 → 词性 → 含义/替代词 → 正误对照）；行间纵向读（按字母序）。
列 2 用 `1.` `2.` 编号时，说明该词有多个核准含义，列 3 会有同样数量的例句与之对应。
核准词的列 4 一般是空的。列 2 左侧的**灯泡符号**表示"此处有额外说明（help）"。

### 大小写就是判据（最实用的读法）

- **全大写 = 核准词，可以用**。`AID (n)`、`ABOUT (prep)`、`REMOVE (v)`
- **小写 = 未核准词，不能用**。`main (adj)`、`build (v)`、`ensure (v)`
- 列 2 里的替代词同样全大写；替代词后的 `(TN)` / `(TV)` = 技术名词 / 技术动词。

## 3. 词性限制（最容易踩的坑）

**一个核准词只能按它被标注的词性使用**（Rule 1.2）。同一个拼写的词若被核准为多种词性，会**各占一条**：

- `CHECK (n)` 核准，`check (v)` **不**核准
- `DAMAGE (n)` 核准，`damage (v)` **不**核准
- `BACK (adv)` 核准，`back (adj)` / `back (n)` **不**核准

所以"这个词能不能用"取决于**你要用的是哪个词性**。

## 4. 一个字出现多次，不算冲突

字典里 2198 条条目对应 1993 个不重复词头；192 个词头有多条条目（如 `OFF`/`ON`/`UP`/`DOWN` 各有
`(adj)` `(adv)` `(prep)` 三条）。这是设计使然：一个词头 → 多条条目，每条一个词性、一个含义。
用法上只需说清"我引用的是哪一条"。

## 5. 未核准词的 4 条出路

对照字典的选词流程图，未核准词只有 4 个终点：

| 类别 | 条件 | 做法 | 例 |
|---|---|---|---|
| **A. 逐词替换** | 替代词与原词**词性相同** | 直接换词 | `ensure (v) → MAKE SURE (v)`；`utilize (v) → USE (v)` |
| **B. 换句式** | 替代词词性不同，或只给了短语/结构 | 换一种句子构造（Rule 9.1） | `attempt (n) → TRY (v)`；`ability (n) → CAN (v)`；`simultaneously (adv) → AT THE SAME TIME` |
| **C. 当 TN/TV 用** | 该词属本公司/行业/学科的 TN 或 TV | **先登记进项目术语表**（带上类别），再用 | `abnormality (n) → DEFECT (TN)`；`land (v) → LANDING (TN)` |
| **D. 不能用** | 既不在字典里，又不是 TN/TV；或把核准词用在了错误的含义上 | 换词或换结构 | 字典列 2 只有 help、没有大写替代词的 13 条：`act (v)` `any (adj)` `except (prep)` `exception (n)` `facility (n)` `have to (v)` `opportunity (n)` `product (n)` `re- (prefix)` `rework (v)` `serve (v)` `volatile (adj)` `whose (pron)` |

### help 的 4 个类别

1. **怎么正确使用**这个核准词（如 `PUSH (v)` 要配方向介词/副词）。
2. **该词含义受限**，其他含义请用别的核准词（如 `ABOUT (prep)` 只表"关于"，表"大约"要用 `APPROXIMATELY (adv)`）。
3. **该词只核准用于某一语境**（如 `SWALLOW (v)` 只用于安全说明）。
4. 其他重要提示（含未核准词）。

## 6. technical noun / technical verb 与字典的关系

- 字典**从不收录** TN / TV。字典只给"核准通用词"这一核心词汇。
- **谁定义**：公司、行业或学科领域（Rules 1.5 / 1.8 / 1.12）。要求短、易懂（1.9），不用方言俚语行话（1.10），同一物件不换词（1.11）。
- **怎么登记**：写进项目术语表（project glossary / company glossary / terminology database），登记时必须带上它属于哪个 TN / TV 类别。
- **接口**：TN / TV 可以出现在字典第 2 列作为未核准词的核准替代词，须用 `(TN)` / `(TV)` 标注。

## 7. 词性缩写与符号

| 缩写 | 全称 | 中文 |
|---|---|---|
| `n` | noun | 名词 |
| `v` | verb | 动词 |
| `adj` | adjective | 形容词（有比较级/最高级） |
| `adv` | adverb | 副词 |
| `pron` | pronoun | 代词 |
| `art` | article | 冠词（a, an, the） |
| `prep` | preposition | 介词 |
| `conj` | conjunction | 连词 |

其他写法：`(TN)` 技术名词 · `(TV)` 技术动词 · `1.` `2.` 多个核准含义 · `…` 可插入内容的结构（如 `DO (v) … AGAIN`）
· `No other verb forms.` 声明无其他词形 · 灯泡符号 = help · `For other meanings, use:` = 其他含义改用下列核准词。

## 8. STE 不管什么（明确划出去的）

- **缩写**：各行业/公司/项目不同，STE 不给规则。
- **文本格式**：字体、编号、字母标注由适用的技术出版物规范/风格指南规定。
- **计量单位**：表示法由项目/公司自己决定。
- **口语**：STE 只为技术文档开发（规则对会议演讲有帮助，可用可不用）。
- **不能单独用**：STE 必须与适用的技术出版物规范、风格指南、官方指令**一起**用。
- **不是英语课**：要用对 STE，必须先有相当高的英语水平。
- **标点通则**：STE 只禁分号（Rule 8.1），其余通则查 The Chicago Manual of Style 等参考书。
- **拼写与含义依据**：美式英语，参考 Merriam-Webster's Collegiate Dictionary。

---

## 9. 高频「未核准词 → 核准替代词」对照表（244 条）

**用途**：写作/改写时最快的查表入口；也是 `scripts/check_ste_compliance.py` 的内置词表。

**读表约定**：左列括号内是未核准词的词性；右列是字典给的核准替代词（按字典顺序），第一个通常与左列词性
相同（可逐词替换），其余往往需要改句式。

**⚠️ 三处与直觉相反，已核实**：
- `APPROXIMATELY (adv)` 与 `SUFFICIENT (adj)` 在 Issue 9 里**是核准词**，别当未核准词处理。
- `in order to`、`numerous`、`utilise`、`obtainable` 在字典里**没有条目**——它们不在"未核准词"名单上，
  但按 Rule 1.1 也不能用（既非核准词又非 TN/TV）。
- 短语动词（`put out` / `give off` 等）通常**不会**标成 not approved，查表查不到，见 Rule 9.3。

| 未核准词 | 词性 | 核准替代词 |
|---|---|---|
| `ability` | n | CAN |
| `acceptable` | adj | PERMITTED / SATISFACTORY / SERVICEABLE |
| `accomplish` | v | DO / COMPLETE |
| `accuracy` | n | PRECISION |
| `achieve` | v | GET |
| `addition` | n | ADD |
| `additional` | adj | MORE |
| `adequate` | adj | SUFFICIENT |
| `adverse` | adj | BAD |
| `advise` | v | TELL / RECOMMEND |
| `allocate` | v | GIVE |
| `allow` | v | LET |
| `already` | adv | IN PROGRESS / NO OTHER |
| `alter` | v | CHANGE |
| `alteration` | n | CHANGE |
| `alternately` | adv | IN ONE / AND THEN THE OTHER |
| `alternatively` | adv | ALTERNATIVE |
| `amount` | n | QUANTITY |
| `analyze` | v | ANALYSIS |
| `application` | n | APPLY |
| `appropriate` | adj | APPLICABLE |
| `approve` | v | APPROVAL |
| `arrange` | v | PUT |
| `arrangement` | n | CONFIGURATION / PREPARE |
| `assessment` | n | ESTIMATE / CALCULATE |
| `assistance` | n | AID / HELP |
| `assume` | v | THINK |
| `assure` | v | MAKE SURE |
| `attempt` | n | TRY / TRY |
| `attention` | n | AID / CAREFUL / MONITOR |
| `avoid` | v | PREVENT / DO NOT |
| `by means of` | prep | WITH |
| `capable` | adj | APPROVED / CAN |
| `cease` | v | STOP |
| `certain` | adj | SURE / SOME / SPECIFIED |
| `characteristic` | n | PROPERTY / QUALITY |
| `check` | v | MAKE SURE / MEASURE / EXAMINE / CHECK |
| `choose` | v | SELECT / ALTERNATIVE |
| `classification` | n | CLASS / CATEGORY |
| `combine` | v | MIX / PUT TOGETHER |
| `comparison` | n | COMPARE |
| `complete` | adj | FULL / ALL / COMPLETED |
| `completely` | adv | FULLY |
| `completion` | n | END / COMPLETE |
| `complicated` | adj | NOT EASY |
| `comply` | v | OBEY |
| `conduct` | v | DO |
| `confirm` | v | MAKE SURE |
| `consecutive` | adj | ONE / AFTER THE OTHER |
| `consequence` | n | BECAUSE OF |
| `consider` | v | THINK |
| `considerable` | adj | LARGE / IMPORTANT / DANGEROUS |
| `construct` | v | ASSEMBLE |
| `convert` | v | CHANGE |
| `correspond` | v | AGREE / SAME / DIFFERENT |
| `create` | v | MAKE / CAUSE |
| `critical` | adj | VERY IMPORTANT CAREFUL |
| `damage` | v | DAMAGE |
| `danger` | n | RISK / DANGEROUS |
| `define` | v | CALCULATE / GIVE / SPECIFIED |
| `delay` | n | INTERVAL / IMMEDIATELY / AFTER |
| `delete` | v | ERASE / REMOVE |
| `deliver` | v | SUPPLY |
| `delivery` | n | SUPPLY |
| `demand` | v | NECESSARY |
| `depend` | v | IF |
| `describe` | v | GIVE |
| `design` | v | HAVE |
| `destroy` | v | BREAK |
| `detail` | n | INSTRUCTION / GIVE / REFER / SPECIFIED |
| `determine` | v | FIND / GIVE / SELECT / CALCULATE |
| `develop` | v | START / CAUSE |
| `difficult` | adj | NOT EASY NOT EASILY |
| `difficulty` | n | NOT EASY NOT EASILY |
| `discontinue` | v | STOP |
| `discrepancy` | n | DIFFERENCE |
| `distribution` | n | SUPPLY |
| `due to` | prep | BECAUSE OF / BECAUSE |
| `duration` | n | DURING |
| `effect` | v | DO |
| `effective` | adj | GOOD |
| `efficient` | adj | SATISFACTORY |
| `efficiently` | adv | SATISFACTORILY |
| `effort` | n | FORCE / TRY |
| `employ` | v | USE / HAVE |
| `enable` | v | LET |
| `end` | v | STOP / COMPLETE |
| `ensure` | v | MAKE SURE |
| `entire` | adj | FULL / ALL |
| `establish` | v | MAKE SURE |
| `estimate` | v | ESTIMATE |
| `evaluate` | v | EXAMINE / ANALYSIS |
| `evaluation` | n | EXAMINE / ANALYSIS |
| `eventually` | adv | SOME TIME |
| `evidence` | n | INDICATION / SIGN / SHOW / SHOW / FIND |
| `exactly` | adv | ACCURATELY / FULLY / CORRECT |
| `examination` | n | EXAMINE / FIND |
| `exceed` | v | MORE THAN |
| `excess` | adj | TOO MUCH MORE THAN UNWANTED / TOO MUCH MORE THAN |
| `excessive` | adj | TOO MUCH MORE THAN |
| `excessively` | adv | TOO MUCH MORE THAN |
| `exclude` | v | NOT INCLUDE NOT USE |
| `exist` | v | BE |
| `expect` | v | POSSIBLE |
| `explain` | v | TELL |
| `facilitate` | v | HELP / EASIER |
| `fail` | v | NOT FAILURE / UNSATISFACTORY |
| `failure` | n | NOT |
| `feasible` | adj | POSSIBLE / CAN |
| `feature` | v | HAVE |
| `final` | adj | LAST |
| `finding` | n | RESULT |
| `finish` | v | COMPLETE |
| `following` | adj | THESE / FOLLOW |
| `forecast` | v | POSSIBLE |
| `function` | v | OPERATE / MOVE |
| `fundamental` | adj | IMPORTANT |
| `further` | adj | MORE / MORE |
| `generally` | adv | USUALLY |
| `generate` | v | BE / GIVE / SUPPLY |
| `great` | adj | LARGE / MORE THAN VERY |
| `greatly` | adv | VERY MUCH |
| `handle` | v | MOVE / TOUCH / USE / CAREFUL |
| `immediate` | adj | IMMEDIATELY |
| `impact` | n | HIT / HIT / EFFECT |
| `implement` | v | DO |
| `improve` | v | BETTER |
| `indicate` | v | SHOW / IDENTIFY / SPECIFIED |
| `inform` | v | TELL |
| `investigate` | v | INVESTIGATION |
| `lack` | n | NOT SUFFICIENT |
| `last` | v | CONTINUE |
| `later` | adj | SUBSEQUENT / THEN / SUBSEQUENTLY / WHEN / AFTER |
| `level` | v | LEVEL |
| `limitation` | n | LIMIT |
| `locate` | v | FIND / ENGAGE / PUT |
| `main` | adj | PRIMARY |
| `maintain` | v | KEEP / HOLD / MAINTENANCE |
| `major` | adj | PRIMARY |
| `manufacture` | v | MAKE |
| `mention` | v | GIVE |
| `minor` | adj | SMALL |
| `modify` | v | CHANGE / MODIFICATION |
| `normal` | adj | USUAL / CORRECT |
| `normally` | adv | USUALLY / CORRECTLY |
| `notify` | v | TELL / CONTACT / WRITE |
| `observe` | v | MONITOR / SEE / OBEY |
| `obtain` | v | GET |
| `often` | adv | FREQUENTLY |
| `order` | n | SEQUENCE / TELL / ORDER |
| `origin` | n | SOURCE |
| `original` | adj | INITIAL |
| `overlap` | v | OVERLAP |
| `part` | v | DISCONNECT |
| `particular` | adj | ONLY APPLICABLE VERY |
| `particularly` | adv | VERY |
| `permit` | v | LET |
| `position` | v | PUT / SET |
| `precede` | v | BEFORE |
| `precise` | adj | ACCURATE |
| `precisely` | adv | ACCURATELY |
| `preparation` | n | PREPARE |
| `presence` | n | BE |
| `present` | adj | BE / GIVE / SHOW |
| `prior to` | prep | BEFORE |
| `probable` | adj | VERY POSSIBLE RISK |
| `proceed` | v | CONTINUE |
| `process` | n | PROCEDURE / DO / PROCEDURE |
| `produce` | v | CAUSE / GIVE / MAKE / SUPPLY |
| `progress` | n | CONTINUE / CONTINUE |
| `prohibit` | v | PREVENT / TELL |
| `proper` | adj | CORRECT |
| `properly` | adv | CORRECTLY |
| `provide` | v | GIVE / SUPPLY |
| `quick` | adj | QUICKLY |
| `rapid` | adj | FAST |
| `rapidly` | adv | QUICKLY |
| `ready` | adj | PREPARE / PREPARE |
| `reason` | n | CAUSE / BECAUSE OF |
| `recover` | v | COLLECT |
| `reduce` | v | DECREASE |
| `reference` | n | REFER |
| `register` | v | SHOW |
| `relevant` | adj | RELATED / THEIR / ITS |
| `remain` | v | STAY |
| `render` | v | MAKE |
| `repeat` | v | AGAIN |
| `require` | v | NECESSARY |
| `respective` | adj | RELATED / CORRECT |
| `respectively` | adv | RELATED |
| `respond` | v | RESULT |
| `restrict` | v | DECREASE / PREVENT / ONLY / LIMIT |
| `result` | v | CAUSE / RESULT |
| `return` | n | GO / GO |
| `reverse` | adj | OPPOSITE / OPPOSITE |
| `rotate` | v | TURN |
| `save` | v | KEEP |
| `secure` | adj | TIGHT / SAFE / CORRECTLY / ATTACH / SAFETY |
| `seek` | v | GET |
| `separate` | adj | ISOLATED / DIFFERENT / DISCONNECT / DIVIDE |
| `serious` | adj | IMPORTANT / DANGEROUS |
| `settle` | v | COLLECT / STABLE |
| `several` | adj | SOME |
| `shorten` | v | DECREASE |
| `similar` | adj | EQUIVALENT / ALMOST THE SAME |
| `simultaneous` | adj | AT THE SAME TIME |
| `simultaneously` | adv | AT THE SAME TIME |
| `slight` | adj | SMALL / LIGHT |
| `slightly` | adv | SMALL |
| `smooth` | v | SMOOTH |
| `solve` | v | SOLUTION |
| `specific` | adj | APPROVED / SPECIFIED |
| `specifically` | adv | SPECIALLY |
| `stability` | n | STABLE |
| `state` | n | CONDITION / TELL |
| `store` | v | KEEP / CONTAIN / STORAGE |
| `stress` | v | FORCE |
| `submit` | v | SEND |
| `subsequent to` | prep | AFTER |
| `substitute` | adj | EQUIVALENT / ALTERNATIVE / ALTERNATIVE / REPLACE |
| `suitable` | adj | APPLICABLE / CORRECT |
| `support` | n | SUPPORT / HOLD / HOLD / SUPPORT |
| `suspend` | v | HANG / STOP |
| `switch` | v | SET |
| `terminate` | v | STOP |
| `test` | v | TEST |
| `therefore` | adv | THUS / AS A RESULT |
| `transfer` | n | MOVEMENT / SUPPLY / MOVE / INSTALL |
| `transport` | v | SEND |
| `treat` | v | APPLY / TOUCH |
| `unnecessary` | adj | NOT NECESSARY |
| `utilization` | n | USE |
| `utilize` | v | USE |
| `valid` | adj | CORRECT / APPLICABLE |
| `various` | adj | DIFFERENT |
| `verify` | v | MAKE SURE |
| `view` | v | SEE / LOOK |
| `visible` | adj | SEE / VIEW |
| `warn` | v | TELL / WARNING |
| `watch` | v | MONITOR / LOOK |
| `well` | adv | CORRECTLY / GOOD / FULLY |
| `withdraw` | v | REMOVE |
| `work` | v | WORK |
| `wrong` | adj | INCORRECT |

---

## 10. 覆盖度说明（诚实交代）

- 本表是**筛选过的 244 条**，不是全部 1274 个未核准词。筛选口径：字典自带的 "List of recurring errors"
  （书里认定的最高频错误）＋ 面向通用技术写作最常被顺手用错的一批动词/名词/形容词/副词/介词短语。
- 因此 `check_ste_compliance.py` 对未核准词的检出是**有漏的**：它报出来的基本可以确定有问题，
  但它没报不等于没问题。要 100% 覆盖须查官方文档的完整词表。
- 替代词映射全部取自字典列 2，未经臆造；有多个替代词时按字典顺序排列。
