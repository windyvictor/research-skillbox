# ASD-STE100 写作规则（Issue 9 · Part 1 · 53 条）

**来源**：ASD-STE100 *Simplified Technical English*, Issue 9, 2025-01-15, Part 1 – Writing rules, pp.45–126
（© ASD, 2025，欧盟注册商标 No. 017966390）。官方免费下载：<https://www.asd-ste100.org>。
本文件是**规则的功能性提炼**，用于本技能的写作与自检；规则的完整正文、示例与受控词典以官方文档为准。

**结构**：9 节 53 条 —— §1 Words(14) · §2 Multi-word nouns(2) · §3 Verbs(7) · §4 Sentences(5) ·
§5 Procedural(5) · §6 Descriptive(6) · §7 Safety(3) · §8 Punctuation & word count(7) · §9 Writing practices(4)，
另有 GR-1 ~ GR-8 八条一般性建议。

---

## 0. 先记住这一页

### 0.1 三个合法用词来源（Rule 1.1，全书地基）

1. **Approved words** —— Part 2 受控词典里核准的词（875 个）。**受三重约束**：只能用核准的词性（1.2）、
   只能用核准的含义（1.3）、只能用词典列出的词形（1.4）。
2. **Technical nouns（TN）** —— 词典**不收录**。够格条件：能归入 §1.5 的 22 个类别之一，且指涉某专业领域的
   特定概念。由公司/行业/领域定义（1.8），登记在项目术语表里。
3. **Technical verbs（TV）** —— 词典**不收录**。够格条件：能归入 §1.12 的 4 个类别之一。**优先级低于 approved
   word**：能用 approved 动词写就不要用 TV（1.12 明文）。

**三种非法用法**：TN 当动词（1.7）；TV 当名词（1.13）；既不 approved 又归不进任何类别。

### 0.2 全文最常用的硬阈值

| 项目 | 阈值 | 出处 |
|---|---|---|
| 程序性写作单句词数 | **≤ 20 词**（含 WARNING/CAUTION） | 5.1 |
| 描述性写作单句词数 | **≤ 25 词** | 6.3 |
| NOTE 中单句词数 | **≤ 25 词**（NOTE 不受 20 词约束） | 5.5 |
| 每段句数 | **≤ 6 句** | 6.6 |
| 每段主题数 | **1 个**，主题句放段首 | 6.5 |
| multi-word noun 词数 | **≤ 3 词**；> 3 词先写全再缩短或加连字符 | 2.1 / 2.2 |
| 自选新 TN 词数 | **not more than three words** | 1.9 |
| 连字符词计词 | 整块算 **1 词** | 2.2 / 8.7 |
| 括号内整段文本在宿主句中的计词 | **1 词** | 8.5 |
| 冒号（竖排列表） | 等价于句号，**冒号前后各自受句长限制** | 8.4 |
| 分号 | **禁用** | 8.1 |
| 允许的动词形式/时态 | **6 种**：不定式、祈使式、一般现在、一般过去、一般将来、过去分词（作形容词） | 3.2 |
| 拼写 | **美式英语**（其他官方指令除外） | 1.14 |

### 0.3 程序性 vs 描述性：先分类，再写

| | 程序性（§5） | 描述性（§6） |
|---|---|---|
| 功能 | 给指令，教人完成任务 | 给信息，不给指令 |
| 单句上限 | 20 词 | 25 词 |
| 祈使式 | **必须用**（5.3） | **不允许** |
| 组织 | 工作步骤，用数字/字母标序 | 段落 + 主题句 |
| 安全提示 | 属于程序性一侧，受 20 词约束 | 通常不含，除非引用文本或本身涉险 |

**描述性 = ① 对 item/product/system/component 的描述（功能、制造、工作原理）；② 一般信息文本（报告、手册、论文）；③ 程序里的一个 NOTE。**

**改写的第一个决定是"这句话是程序句还是描述句"**——同一个被动态句子，两条改写路径完全不同（3.6）。

---

## Section 1 – Words（Rule 1.1 ~ 1.14）

### Rule 1.1 Use words that are: Approved in the dictionary / Technical nouns / Technical verbs.
见 0.1。TN/TV 必须"指涉一个特定概念且适用于某个 subject field"（subject field 按 ISO 1087:2019 定义）。

### Rule 1.2 Use approved words from the dictionary only as the specified part of speech.
- 一个词只被核准为它被标注的那个词性。**词性不同 → 另一条词条**。`CHECK (n)` 核准，`check (v)` 不核准。
- 替换时先做**同词性逐词替换**；无同词性替代词则必须**换句子结构**（转 Rule 9.1）。
- 例：`Test the system for leaks.` → `Do the leak test of the system.`（test 只核准为名词）

### Rule 1.3 Use approved words only with their approved meanings.
- 核准含义常比普通英语**窄**。超出即违规，哪怕普通英语里说得通。
- 例：`follow`（核准义＝come after / go after）→ `Follow the safety instructions.` 应改 `Obey the safety instructions.`

### Rule 1.4 Use only the approved forms of verbs and adjectives.
- 动词词条形如 `REMOVE (v) — REMOVES, REMOVED, REMOVED`，即四类槽位；不规则动词另计（`GIVE — GIVES, GAVE, GIVEN`）。
- 形容词形如 `SLOW (adj) (SLOWER, SLOWEST)`；用 more/most 的形容词不再列（more/most 本身是核准词）。

### Rule 1.5 You can use words that you can include in a technical noun category.
- **22 个类别**（只是示例，非完整清单）：
  1. Official parts information
  2. Vehicles or machines, and locations on them
  3. Tools and support equipment, their parts, and locations on them
  4. Materials, consumables, and unwanted material
  5. Facilities, infrastructure, and logistic procedures
  6. Systems, components and circuits, their functions, configurations, and parts
  7. Mathematical, scientific, engineering terms, and formulas
  8. Navigation and geographic terms
  9. Numbers, units of measurement and time (and their symbols)
  10. Quoted text
  11. Professional roles, individuals, groups, organizations, and geopolitical entities
  12. Parts of the body
  13. Common personal effects, food, and beverages
  14. Medical terms
  15. Official documents, parts of documentation, standards, and guidelines
  16. Environmental and operational conditions
  17. Colors
  18. Damage terms
  19. Computer science, information and communication technology
  20. Civil and military operations
  21. Law and regulations
  22. Animals, plants, and other life forms
- **类别 17 Colors 特例**：颜色本是形容词，STE 归为 TN；但颜色的比较级/最高级（blacker、the reddest）**不允许**。

### Rule 1.6 Use a word that is not approved in the dictionary, only when it is a technical noun or part of a technical noun.
- 词典里小写的词（不核准）**只要在句中构成 TN 就可以用**。同一个词在不同语境可归入不同类别。
- 例：`base` 不核准 → `at the base of the unit` 改 `at the bottom of the unit`；但 `base of the triangle` 里 base 是 TN（类别 7），可用。
- **关键例外**：官方固定的 TN 即使是不核准词也**不得替换**（如 `main landing gear` 不能改成 `primary landing gear`）。

### Rule 1.7 Do not use words that are technical nouns as verbs.
- 例：`Oil the steel surfaces.` → `Apply oil to the steel surfaces.`（oil 是 TN 类别 4）
- 一个词可以同时合法地是 TN 和 TV（如 drill、plate），条件是同时满足 1.5 与 1.12。

### Rule 1.8 Use technical nouns that are approved in your company, industry, or subject field.
- 优先级：公司/行业/领域批准词 > 自造词。有官方 TN 就用官方 TN。

### Rule 1.9 When you must select a technical noun, use one which is short and easy to understand.
- 自定名 **不得超过 3 词**。有索引号且图能识别时，只用核心名词；必要时可加 **1–2 个形容词**。

### Rule 1.10 Do not use regional, slang, or jargon words as technical nouns.
- 判据：读者能否**立即明白**。例：`choker`（地域词）→ `cable`；`brick the router`（IT 俚语）→ `set the router to OFF`。

### Rule 1.11 Do not use different technical nouns for the same item.
- 同一物件全文只用一个 TN。例：`servo control unit` / `actuator` / `control unit` 三选一，统一用其中一个。

### Rule 1.12 You can use verbs that you can include in a technical verb category.
- **4 个类别**（示例，非完整清单）：
  1. **Manufacturing processes** — a) Remove material: drill, grind, mill, ream, unsolder；b) Add material: flame, insulate, remetal, retread；c) Attach material: braze, crimp, solder, weld；d) Change mechanical strength/structure/physical properties: anneal, cure, decay, freeze, heat-treat, magnetize, normalize, vaporize；e) Change surface finish: buff, burnish, dress, passivate, plate, polish；f) Change shape: blend, cast, extrude, spin, stamp
  2. **Computer processes and applications** — a) Input/output: click, digitize, enter, press, print, swipe, tap, type；b) UI & application: clear, close, copy, cut, delete, deselect, disable, drag, drag and drop, enable, encrypt, erase, filter, highlight, invalidate, maximize, minimize, navigate, open, paste, save, scroll, sort, store, validate, zoom in, zoom out；c) System operations: abort, boot, communicate, debug, download, format, install, load, manage, process, reboot, update, upgrade, upload
  3. **Instructions and information for applicable subject fields** — a) Engineering/math/science: bisect, compensate for, convert, detect, float, modulate, radiate, transform, sink；b) Medical: disinfect, intubate, operate, prescribe, sanitize, sterilize；c) Civil & military: aim, arm, disable, dry-motor, enable, explode, fire, inhibit, intercept, lase, load, lock on, unlatch, unload, wet-motor, parachute；d) Navigation: approach, descend, deviate, fly, hover, land, maintain, navigate, retrim, take off, trim, respond, taxi；e) Automotive & railway: accelerate, brake, couple, crank, crash, decouple, dispatch, drift, inflate, park, qualify, steer；f) Energy/oil/gas: compress, distill, drill, emit, extract, inject, pump
  4. **Law and regulations** — acknowledge, comply with, communicate, conform to, describe, enforce, explain, meet (a requirement), inform, modify, notify, omit, regulate, sign, supersede, understand, waive
- **优先级硬规则**：能用 approved 动词准确表达的，**不准**改用 TV。必须用 TV 时只能用该语境中**确切**的 TV（`machine` 太泛 → 用 `ream`）。

### Rule 1.13 Do not use technical verbs as nouns.
- 例：`Give the hole 0.20-inch ream.` → `Ream the hole to a 0.20-inch dimension.`
- **允许**：TV 的**过去分词作形容词**（`Lubricate the reamed hole.`）。

### Rule 1.14 Use American English spelling unless other official directives tell you differently.
- 默认美式（以韦氏词典为准）。例外来源：技术出版物规范、风格指南、合同等官方指令。
- **引文里的英式拼写保持原样，不得改写**（见 8.6）。例：`colour` → `color`；`fibre` → `fiber`。

---

## Section 2 – Multi-word nouns（Rule 2.1 ~ 2.2）

### Rule 2.1 Write multi-word nouns of no more than three words.
- multi-word noun = 由名词/形容词组成、在句中充当主语或宾语的词群；**中心词（head noun）通常是最后一个词**。
- **≤ 3 词**。压不下来的用介词（of / on / in / for）拆成多个 ≤3 词的短词群。
- 例：`Runway light connection resistance calibration.`（5 词）→ `Calibration of the resistance of the runway light connection.`

### Rule 2.2 When a technical noun has more than three words, write it in full. Then you can: give a shorter form / use hyphens between words that you use as one unit.
- 超过 3 词的 TN 常是领域固定说法，不能随意拆：**首次写全**，然后二选一：
  - **方法 1（短式/缩写）**：首次全称，其后用较短形式或**批准缩写**。≤3 词的批准 TN **不必**用缩写。
  - **方法 2（连字符）**：把"作为一个单元"的词连起来，**连起来整块算 1 词**。不得用连字符拼出 > 3 词的组合，不得连接不相关的词。
- 批准 TN 自带连字符的**不得改**；≤3 词的批准 TN 也**不必**加连字符（`diaphragm assembly` 不要写成 `diaphragm-assembly`）。

---

## Section 3 – Verbs（Rule 3.1 ~ 3.7）

### Rule 3.1 Use only the verb forms that are given in the dictionary.
- 词典词条里列出的形态即白名单，不得类推。

### Rule 3.2 Use only these verb forms and tenses of verbs:
**允许的 6 项**：
1. The infinitive form（不定式）
2. The imperative form (command form)（祈使式）
3. The simple present tense（一般现在时）
4. The simple past tense（一般过去时）
5. The simple future tense（一般将来时）
6. The past participle form (as an adjective)（过去分词，作形容词）

**被禁**（原文点名 + 兜底）：现在完成时（`have/has adjusted`）、过去完成时（`had adjusted`）、
现在/过去进行时（`is/was adjusting`）、以及 **all other complex verb constructions**。

- 例：`The operator has adjusted the linkage.` → `The operator adjusted the linkage.`

### Rule 3.3 Use the past participle form as an adjective.
- 过去分词表达的是**状态（condition）**，不是被动态。只准出现在两个位置：
  ① **名词之前**（`the disassembled unit`）；② **`to be` / `to become` / `to stay` 的某个形式之后**（`When the unit is fully disassembled, ...`）。
- 词典里存在"来源动词未核准但形容词已核准"的过去分词（如 `permitted`、`damaged`），可用。

### Rule 3.4 Do not use auxiliary verbs to make complex verb constructions.
**被禁的助动词构造**（原文点名）：
1. `have / has / had + 过去分词`（完成时）
2. `is / are to be + 过去分词` → `The seat is to be installed before you install the cushion.`
3. `can be + 过去分词` → `The volume control can be adjusted.`
4. `must be + 过去分词` → `The temperature must be adjusted.`
5. `will be + 过去分词` → `The sleeve will be adjusted by the robot.`
6. 其他 `be + 过去分词（+ by / with）` 的被动实例 → `are used by` / `are given by` / `is held by` / `can be opened with`
7. **兜底**：一切未获批准的复合动词构造。
- 改法：程序句 → 祈使式；描述句 → 主动语态陈述句。
- 例：`The volume control can be adjusted.` → `You can adjust the volume control.` ／ `Adjust the volume control.`

### Rule 3.5 Use the "-ing" form of a verb only as a technical noun or as a modifier in a technical noun.
- `-ing` 只准落在两格：
  - **作为技术名词**：本身是被命名的活动/工序名。例：`Cleaning`、`Testing and Fault Isolation`、`Handling`、`Packaging`、`Shipping`、`Troubleshooting`（程序标题/标题栏）。
  - **作为 TN 中的修饰语**：形容词性修饰，且**与该系统/部件/零件/工具/材料/设备的功能有关**。例：`air-conditioning system`、`degreasing agent`、`grinding wheel`、`polishing disc`、`sanding machine`、`switching relay`、`welding torch`。
- 禁止：作进行时动词、作普通形容词、作动名词短语。
- 例：`An opening door can be dangerous.` → `When a door opens, it can be dangerous.`
- **词典中带 -ing 的核准词极少**：名词 `lighting` / `opening` / `routing` / `servicing`；形容词 `mating` / `missing` / `remaining`；代词 `something`；介词 `during`。

### Rule 3.6 Use the active voice. In descriptive writing, you can use the passive voice only when the agent is unknown.
- **豁免只属描述性写作**，且仅当 agent 未知。判定法：自问 "by whom or by what?"——能回答就是 agent 已知，不可豁免。
- 豁免还有附加条件：改成主动后**技术上必须仍然正确**。`During transmission, the data was corrupted.` 正确；改成 `Transmission corrupted the data.` 反而错（transmission 不是真正原因）。
- **被动改主动四法**：
  1. agent 已给出（通常是 by 的宾语）→ 把它移到句首作主语。
  2. 把不定式动词改成主动动词：`These values are used by the computer to calculate...` → `The computer calculates... from these values.`
  3. 程序性写作 → 改祈使式：`The test can be continued by the operator.` → `Continue the test.`
  4. agent 未给出 → 用 `you`（agent 是读者）或 `we`（agent 是本企业/机构）作主语：`...the valve can be opened with the override handle.` → `...you can open the valve with the override handle.`
- **救急词 `something`**：agent 未知又必须写主动句时，用 `something` 充当 agent（`During transmission, something corrupted the data.`）。

### Rule 3.7 Use an approved verb to describe an action, not a noun or other parts of speech.
- 只要有描述该动作的 approved 动词，就用动词。本条判**清晰度**，不判合法性（书中的反例其实也都在 STE 之内）。
- 例：`The ohmmeter gives an indication of 450 ohms.` → `The ohmmeter shows 450 ohms.`
- 例：`Before the removal of the unit, ...` → `Before you remove the unit, ...`

---

## Section 4 – Sentences（Rule 4.1 ~ 4.5）

本节是**程序性与描述性共用的通则**；句长阈值在 §5 / §6。

### Rule 4.1 Write short and clear sentences.
1. 程序里用祈使式把指令直接给读者。
2. 描述里每句**只有一个主题**，且**不含祈使式**；后续句逐步展开该主题。
3. 超长句拆成编号工作步骤（`1.` + `A./B./C.`）。
4. 两类写作都**不得抽象**。
5. **必须准确**，不给可有多种理解的信息。
6. **给具体数值**：`When the temperature increases, the cure time will decrease.` 之外还应给 `The cure time is 2 hours at a temperature of 20 °C.`
7. **不得回避动作**：`No leaks are permitted.` → `Make sure that there are no leaks.`

### Rule 4.2 Do not omit words or use contractions to make your sentences shorter.
- 不得省略：**名词、动词、主语、冠词**。不得用缩略式（`don't` / `isn't` / `aren't`）。
- 例：`Rotary switch to INPUT.` → `Set the rotary switch to INPUT.`
- 例：`Remove the bolt and stop.` 有歧义（the stop 是零件）→ `Remove the bolt and the stop.`

### Rule 4.3 Use a vertical list for complex text.
**结构规定 8 条**：
1. 列表第一项之前，在**第一句句末加冒号**。
2. 用数字、字母、标点或符号标识每一项（`-`、`•`、`a b c`、`1 2 3`）。
3. 每项**以大写字母开头**。
4. 适用时，在每项作主语的名词前**加冠词**。
5. **完整句**→ 末尾加句点；**不是完整句**→ 不加句点。
6. **不得**在项末加逗号或分号。
7. **最后一项末尾加句点**。
8. 具体用哪种符号，参照适用的技术出版物规范。
- 同一个竖排列表内**不得混用**程序性与描述性（程序项用祈使式，描述项用陈述句）。
- 不得在主列表内嵌子列表；要嵌就用括号并入父项：`- The flange (2) (that includes the two O-rings (6) and the seals (7))`。
- 安全指令要否定就**逐项都写 DO NOT**。

### Rule 4.4 Use connecting words and connecting phrases to connect sentences that contain related topics.
- 原文举例：连接词 `and`、`but`、`then`、`thus`；连接短语 `as a result`、`at the same time`；另可用**指示形容词**（this/these）连接。
- 原文措辞是 "Some of the connecting words that are approved in the dictionary are…"，属**部分列举**。
  **完整清单 = 词典里核准的 17 个连词**：`AFTER, ALTHOUGH, AND, AS ... AS, BECAUSE, BEFORE, BUT, IF, OR, SINCE, THAN, THAT, UNLESS, UNTIL, WHEN, WHERE, WHILE`。
- 程序里可在工作步骤需要解释时使用；安全指令里可用来连接相关句。
- 见 6.2：key words / key phrases 用过就不得改。

### Rule 4.5 When applicable, use an article (the, a, an) or a demonstrative adjective (this, these) before a noun or a multi-word noun.
- 短句：**所有名词前都加**更清楚（`Install the nuts (2) and the bolts (3).`）。
- 长串项目：**只在第一个名词前加**更清楚（`Discard the O-rings (3), gaskets (4), seals (7), and washers (9).`）。加冠词会改变范围：`the new O-rings (15), spacers (14), ...` 表示全是新的；`the new O-rings (15), the spacers (14), ...` 只表示 O-rings 是新的。
- **不得加冠词的场合**：一般性陈述/概念/抽象性质（`Solvents can cause damage to paint.` / `This software increases performance.`）。
- **定冠词特殊禁令**：名词后跟字母数字标识符时（即专有名词），**不得**用 the：`Tag circuit breaker 36L7.`（不是 `Tag the circuit breaker 36L7.`）。

---

## Section 5 – Procedural writing（Rule 5.1 ~ 5.5）

### Rule 5.1 Write short sentences. Use a maximum of 20 words in each sentence.
- 含 **WARNING / CAUTION / 其他安全指令**。NOTE 不在此列（见 5.5，上限 25 词）。
- 超限就拆成两句；但**不得拆成两个独立工作步骤**（见 5.2）。

### Rule 5.2 Write only one instruction in each sentence unless two or more actions occur at the same time.
- 默认 **1 句 = 1 个指令**，用数字或字母显式标序。工作步骤数量不限。
- **例外（两个层次，别混淆）**：
  - 一句里可有多个动作——条件是**同时发生**（`Cut and remove the wire.` / `Remove and discard the seal.`）。不同时则必须拆成 A、B 两个步骤。
  - 一个**工作步骤**里可有多个句子——条件是**动作同时发生**，或**一个动作之后立即出现一个结果**。

### Rule 5.3 Write instructions in the imperative (command) form.
- 以动词原形起句（`Set…` / `Remove…`），主语 you 不出现。
- **`must` 的硬条件**：祈使式前不加 must，除非①该指令对**安全**非常重要，或②你给出的是一个**重要条件**。
  - `Before you remove the clamp, you must disconnect the hose.` → `Before you remove the clamp, disconnect the hose.`
- 禁止：被动式表动作（`are to be removed` / `can be continued`）。

### Rule 5.4 When there is a condition that the reader must know about first, start the instruction with a descriptive statement. Then, divide that descriptive statement from the command with a comma.
- 结构固定为 `条件从句 + 逗号 + 祈使式命令`。条件必须**前置**。
- 例：`Set the switch to NORMAL when the light comes on.` → `When the light comes on, set the switch to NORMAL.`
- 逗号位置**决定语义**：`If the CSD does not operate correctly, disconnect it...`（correctly 修饰 operate）vs `If the CSD does not operate, correctly disconnect it...`（correctly 修饰 disconnect）。按真实语义放置。

### Rule 5.5 Write notes only to give information, not instructions.
- NOTE 属**描述性文本**，遵守 §6；**每句 ≤ 25 词**；可含一句或多句。
- **禁止**：祈使式；指令；要求；**限值/公差/结果**（这些必须紧跟在相关工作步骤之后，写成工作步骤的第二句）。
- 自检法：**不看 NOTE 通读全篇程序，若仍能正确完成，则 NOTE 用得对**。若关键信息在 NOTE 里，就把它移出来写成工作步骤。
- 有伤害风险 → WARNING；有损坏风险 → CAUTION。**绝不能把防伤害/防损坏的信息写成 NOTE**。
- 描述性文本里，只在插图或表格必需时才写 NOTE。

---

## Section 6 – Descriptive writing（Rule 6.1 ~ 6.6）

### Rule 6.1 Give information gradually.
- 每句**只含一个主语/一个信息单元**。一次给太多太快，读者只能重读。
- 手段：一句一信息单元、用短句、**先总述后细节**、长复句拆成多短句（而不是删信息）、切成段落、用 key words 缝合。

### Rule 6.2 Use key words and key phrases to give your text a logical structure.
- **用过即定型**：`make sure that you do not change them in your text`——同一术语必须原样复用，换词会让文本难读。
- 连接词/连接短语清单同 4.4。

### Rule 6.3 Write short sentences. Use a maximum of 25 words in each sentence.
- 描述性比程序性复杂，故放宽到 25 词（含上限）。

### Rule 6.4 Use paragraphs to show related information.
- 每段以**主题句（topic sentence）**开头，说明该段讲什么；后续句只做"解释主题句"或"补充相关信息"。
- 换主题 → 换段落。

### Rule 6.5 Make sure that each paragraph has only one topic.
- 主题句是段落**第一句、也是最重要的一句**，它给新信息，并与已有信息建立逻辑连接——因此主题句通常含 **key word** 和/或 **connecting word / connecting phrase**。
- 自检法：**把各段主题句依次抄下来，应能得到全文的好提纲**。

### Rule 6.6 Make sure that no paragraph has more than six sentences.
- **每段 ≤ 6 句**（含 6）。超过就拆段。竖排列表项不按"句子"另计（由冒号引入）。

---

## Section 7 – Safety instructions（Rule 7.1 ~ 7.3）

### 定义（p.103）
- **WARNING**：`there is a risk of injury or death`（**人身伤害或死亡**）。
- **CAUTION**：`there is a risk of damage to objects`（**物品损坏**）。
- **两种风险同时存在 → 用 WARNING**。
- 用别的词（danger / attention / notice）或图形符号时，内容**仍须守 7.1–7.3**，并参照 ISO 45001:2018、ISO 3864、ANSI Z535。

### 三段式骨架
```
<级别词>： ① 命令或条件（祈使式命令 / when·while·before 条件）
           ② （可选）安全做法
           ③ 解释：说明风险或可能后果
```

### Rule 7.1 Use an applicable word (for example, "warning" or "caution") to identify the level of risk.
- 先做**准确的风险分析**定级 → 人身伤害/死亡用 warning；物品损坏用 caution；两者并存用 warning。
- 禁止用抽象陈述代替具体风险：`CAUTION: EXTREME CLEANLINESS OF OXYGEN TUBES IS IMPERATIVE.` → `WARNING: MAKE SURE THAT THE OXYGEN TUBES ARE FULLY CLEAN. OXYGEN AND GREASE MAKE AN EXPLOSIVE MIXTURE. AN EXPLOSION CAN CAUSE INJURY OR DEATH.`

### Rule 7.2 Start a safety instruction with a clear and accurate command or condition.
- 起始成分二选一：**清晰准确的命令**（`DO NOT SWALLOW THE SOLVENT.`）或**清晰准确的条件**（`WHEN YOU ASSEMBLE THE UNIT, ...`）。
- 读者必须在开始前就知道的条件 → **放最前面**。
- 禁止以解释、背景、抽象说明、名词性陈述起句。

### Rule 7.3 Give an explanation to show the risk or possible result.
- 必须包含解释，并**具名到具体危害**（poisonous / explosion / injury / death / corrosion / permanent damage）。
- 例：`SOLVENTS ARE POISONOUS AND CAN CAUSE INJURY OR DEATH.`

**格式说明**：§7 示例全用大写，但 **STE 不规定格式**；大写用法由适用的技术出版物规范决定。

---

## Section 8 – Punctuation and word count（Rule 8.1 ~ 8.7）

### Rule 8.1 You can use all standard English punctuation marks but not the semicolon (;).
- 禁用分号（理由：会诱导长句，且分号本身难用对）。**唯一替代 = 拆成两个独立句子**（各自计词）。
- 例：`Examine the removed parts; replace the damaged ones.` → `Examine the removed parts for damage.` + `Replace the damaged part(s).`
- STE **不给一般标点规则**，参考 The Chicago Manual of Style / Gregg Reference Manual / GPO Style Manual / Practical English Usage。

### Rule 8.2 Use hyphens (-) to connect words that are directly related.
**必须用连字符的 5 类**：
1. 名词前作形容词、由 ≥2 词组成的术语：`low-altitude flight`、`high-pressure chamber`、`quick-release fastener`、`trial-and-error method`、`air-to-air refueling`、`up-to-date information`、`self-sealing hose`
2. 两词的分数或数词：`forty-seven`、`ninety-ninth`、`three-sixteenths`、`one thirty-second`
3. 「大写字母 + 名词」或「数字 + 名词」表示形状/构型：`L-shaped bracket`、`O-ring`、`U-beam`、`V-band clamp`、`3-prong connector`、`180-grit abrasive cloth`
4. 第一部分是名词（或其他词类）的动词：`die-cast`、`arc-weld`、`stop-drill`、`heat-treat`、`short-circuit`、`cold-roll`、`dry-clean`
5. 前缀末尾是元音、且词根以元音开头：`pre-amplifier`、`de-icing`、`anti-icing`、`pre-engage`
- **不得把连字符当破折号用**（破折号分隔思想/表范围/表停顿，常以「空格 + 连字符 + 空格」出现）。

### Rule 8.3 You can use parentheses:
**7 类允许用途**：① 引用插图或文本；② 放入标识插图/文本中物件的字母或数字；③ 标识程序中的工作步骤；
④ 放入缩写；⑤ 同时给出名词的单数与复数形式；⑥ 解释词或句子的一部分；⑦ 放入一个备选项。
- 例：`Remove the valve (10, Figure 1).` ／ `Increase the pressure slowly (not more than 10 psi each minute).` ／ `Open the left (right) access panel L42 (R42).`

### Rule 8.4 In a vertical list, a colon (:) has the same effect on word count as a period and shows the end of a sentence.
- 冒号**前**不得超过：程序 20 词 / 描述 25 词。
- 冒号**后每一项各自算新句子**，每项上限同样是 20 / 25 词。

### Rule 8.5 When you put text in parentheses, it counts as one word in that sentence.
- 宿主句中括号内整段文本 = **1 词**；但括号内文本**另作独立句子**逐词计数。
- 括号内的标识符、缩写按 8.6 各算 1 词。
- 例：`Make sure that the EMER pushbutton switch is released (the EMER legend is off).` = 宿主句 10 词；括号句 5 词另计。

### Rule 8.6 Count each of these elements as one word:
**7 类**：
1. **Numbers** 数字（`Do steps 13 thru 16 a minimum of three times.` = 10 词）。**注**：标识段落/工作步骤的数字不计入。
2. **Numbers together with units of measurement** 数字 + 计量单位（`10 °C`、`20 kg`、`10 ohms` 各 1 词，拼写单位与符号单位相同）。
3. **Abbreviations** 缩写（含 acronym、initialism；`10 a.m.` 算 1 词）。
4. **Alphanumeric identifiers** 字母数字标识（`No. 1`、`36L7` 各 1 词）。
5. **Quoted text** 引用文本（引号内内容；大写串如 `SHORT-CIRCUIT TEST` 也算；**公式** `C = (A - B) - 0.063 mm` 算 1 词）。
6. **Titles, headings, and text on placards and labels** 标题、标题栏、标牌与标签上的文本（`Structural Repair Manual` 算 1 词）。
7. **Proper nouns of individuals, groups, organizations, and geopolitical entities** 专有名词（`United States of America` 算 1 词）。

### Rule 8.7 Hyphenated words count as one word.
- 例：`soap-and-water solution` 句 = 7 词；`Use the trial-and-error method.` = 4 词；`Cutoff-switch power connection` = 3 词。

---

## Section 9 – Writing practices（Rule 9.1 ~ 9.4）

### Rule 9.1 Use a different sentence construction to write a sentence when a word-for-word replacement is not sufficient.
**逐词替换失败的 4 种情况**（出现即必须换构造）：
1. 用替代词必须改变句子语法结构（词性不同）。
2. 逐词替换产生无意义的结果。
3. 替代词改变了句义。
4. 要替换的词不在词典中。

**换构造的做法**：换用不同的词 → 更换动词形式 → 写新的句子构造 → 拆长句 → 删掉不必要的信息 →
向工程师要更多信息 → 改动后**复检全文**无副作用。

**写作前自问**：`What is the meaning of the word in this context?` / `What is the action that a reader must do?`

- 例：`The oil level on the sight gauge must be visible during the test.` → `During the test, make sure that you can see the oil level on the sight gauge.`
- **易错**：`just` 的替代词 `only` 不得误用为 `immediately`；`clear` 的替代只有动词 `clean`，词义不符时不得硬换。

### Rule 9.2 Use each approved word correctly.
**常见误用三类**：
1. **用了标准英语的引申义而非核准义**：
   - `wear`（核准义＝受摩擦而损坏）→ 表"穿戴"用 `use` / `put on`
   - `goes down`（只指物理运动）→ 表压力用 `decreases`
   - `see`（只指用眼看到）→ 表"弄清"用 `make sure`
   - `turn`（只指绕轴转动）→ 表颜色用 `changes`
   - `above` / `below`（只表物理位置）→ 表限值用 `more than` / `less than`
2. **词性错误**：`work`（只核准为名词）→ `When you do work with...`；`help`（只核准为动词）→ `with the aid of...`；`damage`（只核准为名词）→ `not to cause damage to the sleeve`
3. **一词多词性需按位置判别**：`flush` 既核准为动词（冲洗）又核准为形容词（齐平）。

### Rule 9.3 When you use two words together, do not make phrasal verbs.
- **禁止**短语动词（语义不等于各词核准义之和）。书中点名：
  - 禁止：`put out`（`Put out the cat.` vs `Put out the fire.` 歧义）→ 用 `extinguish`
  - 禁止：`give off`（`give off poisonous fumes`）→ 用 `release`
  - 核准但含义受限：`put on`、`come on`
- **陷阱**：短语动词通常**不会**在词典里标成 not approved，查词典发现不了——必须自己确保新句语法正确、各词保持词典义。

### Rule 9.4 When you select terminology or wording, always use a consistent style.
**三个层次**：
1. **术语一致**：同一物件始终同一名词（不要把 (9) 写成 `main body` / `body` / `body assembly` 三种）。
2. **措辞一致**：同一动作同一语境始终同一措辞（不要 `torque` 与 `torque-tighten` 混用）。
3. **句式一致**：同类工作步骤选定一种句式后反复沿用。

---

## General recommendations（GR-1 ~ GR-8，不是规则，只帮助避免常见错误）

| # | 主题 | 要点 |
|---|---|---|
| GR-1 | 连词 `that` | 在 `make sure`、`show`、`recommend` 等动词后**尽量用 that**，防歧义、利翻译。`Make sure the valve is open.` → `Make sure that the valve is open.` |
| GR-2 | 介词 `with` | 有 3 个核准含义（关联 / 帮助共享 / 手段工具），极易歧义。`Install the panel with the green fasteners` 可有 3 解。写完复读确认无歧义。 |
| GR-3 | 代词 | 代词须在词典中，且**无歧义**才用。可指多个名词时改用所指代的名词。 |
| GR-4 | 代词 `this` | 确保读者知道 `this` 指什么；有歧义就重给语境：`Make sure that the cover is not locked. If the cover is locked, this can cause damage to the probe.` |
| GR-5 | False friends | 形似母语、义不同的词（英语 disposition ≠ 意/西语 disposizione/disposición）。`Obey the dispositions of the manufacturer...` → `...obey the manufacturer's instructions.` |
| GR-6 | 拉丁缩写 | **不用** `e.g.` / `i.e.` / `etc.`，改用英语词：`(e.g., washers, screws, bolts, and nuts)` → `(for example, washers, bolts, and nuts)` |
| GR-7 | 包容性语言 | **必须用性别中性语言**。性别特定代词 `he` / `she` 不允许；`man` / `woman` 除必要语境（如医学文本）外不允许。 |
| GR-8 | 所有格 | 允许但**不确定就别用**（非母语读者不易理解）。`refer to the manufacturer's instructions.` |

---

## 附：可机械化判定的清单（交给 `scripts/check_ste_compliance.py`）

| # | 判据 | 规则 | 可实现性 |
|---|---|---|---|
| 1 | 出现分号 `;` | 8.1 | 字面 |
| 2 | 缩略式 `don't` / `isn't` / `aren't` | 4.2 | 字面 |
| 3 | 句长 > 20 词（程序）/ > 25 词（描述）/ > 25 词（NOTE） | 5.1 / 6.3 / 5.5 | 计词规则见 8.4–8.7 |
| 4 | 段落 > 6 句 | 6.6 | 字面 |
| 5 | 完成时 `have/has/had + 过去分词`；进行时 `is/was + -ing` | 3.2 | 模式 |
| 6 | 助动词被动 `can be / must be / will be / is to be + 过去分词` | 3.4 | 模式 |
| 7 | 被动语态 `be + 过去分词 (+ by)` | 3.6 | 模式（需人工确认 agent 是否未知） |
| 8 | `-ing` 词不在白名单内 | 3.5 | 需白名单 + 人工确认是否为 TN |
| 9 | 短语动词 `put out` / `give off` 等 | 9.3 | 词表 |
| 10 | 未核准词（如 `ensure` / `utilize` / `perform` / `prior to`） | 1.1 / 1.2 / 1.3 | 用 `assets/ste-unapproved-words.tsv` |
| 11 | 拉丁缩写 `e.g.` / `i.e.` / `etc.` | GR-6 | 字面 |
| 12 | 英式拼写 `colour` / `fibre` / `centre` 等 | 1.14 | 词表 |
| 13 | multi-word noun > 3 词 | 2.1 | 启发式（需人工确认） |
| 14 | 竖排列表项以逗号/分号收尾、首字母未大写 | 4.3 | 字面 |
| 15 | 竖排列表前缺冒号 | 4.3 | 字面 |
| 16 | 祈使式前加 `must`（非安全/非重要条件） | 5.3 | 启发式 |
| 17 | 程序性写作里出现 `to be + 过去分词` | 3.6 / 5.3 | 模式 |
| 18 | NOTE 里出现祈使式或限值表述 | 5.5 | 启发式 |
| 19 | WARNING / CAUTION 缺"解释风险"的第二句 | 7.3 | 启发式 |
| 20 | 句中无冠词的名词短语（省略冠词） | 4.2 / 4.5 | 难，交人工 |

脚本只报**线索**（line + 命中项 + 原文片段），不做终判——受控语言里大量判断依赖"这个词在这里是不是 TN"。
