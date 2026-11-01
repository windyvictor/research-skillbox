#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""卡片机械自检（单卡；中英文）。

把永久笔记写作标准中可机械判定的部分写成阈值：指示代词与上下文指代、
来源依赖、模糊评价、摘抄嫌疑、多想法嫌疑、标题是否陈述主张、
是否有连接与关系标注、篇幅是否越界，以及 YAML 头（status/author/sources）。

用法：
    python3 check_card.py <卡片.md> [<卡片2.md> ...] [选项]

选项：
    --lang zh|en|auto   规则语言（默认 auto：按正文中文字符占比自动判断）
    --json              输出 JSON（多文件时为数组），便于程序处理
    --strict            WARN 也视为不通过（退出码 1）
    --demo              用内置中英文样例自检本脚本
    -h, --help          显示本说明

退出码：
    0  没有 ERROR（--strict 时：也没有 WARN）
    1  至少一张卡有 ERROR（--strict 时：有 ERROR 或 WARN）
    2  参数错误或文件无法读取

输出只报线索（行号 + 命中项 + 原文片段），不做终判；
术语与冗词的区分、语气是否恰当、"三年后测试"须人工确认。
"""

import argparse
import json
import re
import sys

STATUSES = {"draft", "reviewed", "evergreen", "superseded"}
AUTHORS = {"human", "ai", "mixed", "external"}

# 每条规则：(级别, 名称, 正则, 提示, 正则标志)
RULES = {
    "zh": [
        ("ERROR", "指示代词（依赖上下文）",
         r"这个观点|这个方法|这个理论|这个结论|这种做法|这种情况",
         "把指代对象写进卡片本身，让三年后的自己不翻别的卡也读得懂", 0),
        ("ERROR", "来源依赖（以他人之口代替陈述）",
         r"作者认为|作者说|书中说|文章中提到|某某认为|正如上文|如前所述|上面提到",
         "直接陈述主张，来源移到卡片末尾", 0),
        ("WARN", "模糊评价（缺论证）",
         r"很重要|非常关键|很有意思|有启发|值得注意|意义重大|至关重要",
         "补上机制或例子：它为什么重要、通过什么起作用", 0),
        ("WARN", "摘抄嫌疑（长段引文）",
         r"[\"“”「][^\"“”「」]{30,}[\"“”」]",
         "超过 30 字的连续引文多为摘抄；改成自己的话重述，原文留作来源", 0),
        ("WARN", "可能含多个想法",
         r"另外|此外|还有一点|另一方面|再比如",
         "一卡一想法；第二个想法应另起一张卡并连接过来", 0),
    ],
    "en": [
        ("ERROR", "Demonstrative / context reference",
         r"\b(this (idea|point|method|theory|conclusion|approach)|as (mentioned|stated|noted|discussed) (above|earlier|before)|the above)\b",
         "Name the thing itself so the card reads on its own years later", re.I),
        ("ERROR", "Source dependence",
         r"\b(the author (argues|says|claims|thinks|believes|states)|according to the (author|book|article|paper)|the (book|article|paper) (says|argues|claims))\b",
         "State the claim directly; move the source to the end of the card", re.I),
        ("WARN", "Vague evaluation",
         r"\b((very|really|extremely) (important|interesting|useful)|insightful|worth noting|fascinating)\b",
         "Add the mechanism or an example: why it matters and how it works", re.I),
        ("WARN", "Possible verbatim quote",
         r"[\"“][^\"“”]{120,}[\"”]",
         "Long quotes are usually copying; restate in your own words, keep the quote as source", 0),
        ("WARN", "May contain more than one idea",
         r"\b(additionally|in addition|another point|on the other hand|furthermore|moreover)\b",
         "One idea per card; split the second idea into its own card and link it", re.I),
    ],
}

TITLE_BAD = {
    "zh": re.compile(r"^#+\s*(关于.*的笔记|.*读书笔记|.*感想|笔记：.*|.*摘录|.*摘抄|读书笔记.*|.*总结)\s*$"),
    "en": re.compile(r"^#+\s*(notes? on .*|.*\bnotes|.*\bsummary|summary of .*|thoughts on .*|reading notes.*|highlights.*)\s*$", re.I),
}
TITLE_ADVICE = {
    "zh": "标题应直接写主张，如「反馈的频率比反馈的质量更重要」",
    "en": "Make the title a claim, e.g. 'Feedback frequency matters more than feedback quality'",
}

# 连接：[[双链]]、指向 .md 的相对链接、卢曼式编号（数字/数字+字母，如 21/3d5a；
# 纯数字的 2024/12、3/4 不算，以免把日期、分数误当连接）、带 § 前缀的编号、参见/see also
LINK_RE = re.compile(
    r"\[\[[^\]]+\]\]"
    r"|\]\([^)\s]+\.md\)"
    r"|(?<![\w/])\d{1,4}/\d+[a-z][0-9a-z]*(?![\w/])"
    r"|§\s?\d{1,4}(?:/[0-9a-z]+)+"
    r"|参见\s*\S+"
    r"|\bsee also\b\s*\S+", re.I)
RELATION_RE = {
    "zh": re.compile(r"支持|反驳|补充|延伸|矛盾|修正"),
    "en": re.compile(r"\b(supports?|contradicts?|refutes?|extends?|complements?|qualifies|revises?|supersedes?)\b", re.I),
}
RELATION_ANY = re.compile(RELATION_RE["zh"].pattern + "|" + RELATION_RE["en"].pattern, re.I)

LIMITS = {"zh": (40, 500, "字"), "en": (15, 250, "words")}


def parse_frontmatter(lines):
    """返回 (字段 dict 或 None, 正文起始行下标)。只做简单 key: value 解析，不依赖 PyYAML。"""
    if not lines or lines[0].strip() != "---":
        return None, 0
    fm = {}
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return fm, i + 1
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if m:
            val = re.sub(r"\s+#.*$", "", m.group(2)).strip()
            fm[m.group(1)] = val
        elif line.startswith((" ", "\t", "-")) and fm:
            last = list(fm)[-1]
            fm[last] = (fm[last] + " " + line.strip()).strip()
    return None, 0  # 没有闭合的 ---，当作普通正文


def empty_value(v):
    return v is None or v.strip() in ("", "[]", "''", '""', "~", "null")


def detect_lang(text):
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    if cjk == 0 and latin == 0:
        return "zh"
    # 一个汉字约等于一个英文单词的信息量，英文字母按 5 个折算 1 个词
    return "zh" if cjk >= latin / 5 else "en"


def check_text(text, name="<stdin>", lang="auto"):
    lines = text.split("\n")
    fm, start = parse_frontmatter(lines)
    body_lines = lines[start:]
    body_text = "\n".join(l for l in body_lines if not l.lstrip().startswith("#"))
    if lang == "auto":
        lang = detect_lang(body_text)
    issues = []

    def add(line_no, level, label, frag, advice):
        issues.append({"line": line_no, "level": level, "rule": label,
                       "fragment": frag, "advice": advice})

    # YAML 头
    if fm is None:
        add(0, "INFO", "无 YAML 头", "",
            "数字卡片建议加 status/author/sources（纸笔或无元数据的库可忽略）")
    else:
        status = fm.get("status", "").strip().lower()
        author = fm.get("author", "").strip().lower()
        if not status:
            add(1, "WARN", "缺少 status", "", "填 draft / reviewed / evergreen / superseded")
        elif status not in STATUSES:
            add(1, "WARN", "status 取值不规范", status, "只用 draft / reviewed / evergreen / superseded")
        if author and author not in AUTHORS:
            add(1, "WARN", "author 取值不规范", author, "只用 human / ai / mixed / external")
        if not author:
            add(1, "WARN", "缺少 author", "", "填 human / ai / mixed / external，区分谁写的")
        if empty_value(fm.get("sources")):
            add(1, "WARN", "缺少 sources", "", "写明来源（文献卡、原件路径或 URL；原创写「原创 YYYY-MM-DD」）")
        if author in ("ai", "external") and status and status != "draft":
            add(1, "ERROR", "AI/外部卡未经人审就升级", f"author: {author}, status: {status}",
                "AI 或外部导入的卡只能是 draft；人改写确认后改 author: mixed 再升级")
        if status == "superseded" and empty_value(fm.get("superseded_by")):
            add(1, "WARN", "被更替却未指向新卡", "", "填 superseded_by：指向推翻它的修正卡")

    # 标题
    title_found = False
    for i, line in enumerate(body_lines[:3], start + 1):
        if line.startswith("#"):
            title_found = True
            if TITLE_BAD[lang].search(line):
                add(i, "WARN", "标题未陈述主张", line.lstrip("#").strip(), TITLE_ADVICE[lang])
            break
    if not title_found:
        add(start + 1, "WARN", "缺少标题", "", "卡片应有标题，且标题直接陈述主张")

    # 逐行规则
    for i, line in enumerate(body_lines, start + 1):
        if line.lstrip().startswith("#"):
            continue
        for level, label, pattern, advice, flags in RULES[lang]:
            m = re.search(pattern, line, flags)
            if m:
                frag = line[max(0, m.start() - 12):m.end() + 12].strip()
                add(i, level, label, frag, advice)

    # 篇幅与连接
    if lang == "zh":
        n_len = len(re.sub(r"\s", "", body_text))
    else:
        n_len = len(re.findall(r"[A-Za-z0-9\u4e00-\u9fff][\w'’-]*", body_text))
    lo, hi, unit = LIMITS[lang]
    n_links = len(LINK_RE.findall("\n".join(body_lines)))
    if n_len < lo:
        add(0, "ERROR", "内容过短", f"{n_len} {unit}", f"不足 {lo} {unit}：只有关键词或一句评价，等于没写")
    elif n_len > hi:
        add(0, "WARN", "篇幅过长", f"{n_len} {unit}", f"超过 {hi} {unit}：多半塞进了第二个想法，应拆卡互联")
    if n_links == 0:
        add(0, "ERROR", "无连接", "0", "每张卡至少 1 条连接（[[双链]]／编号如 21/3a／参见）"
            if lang == "zh" else "Every card needs at least one link ([[wikilink]], ID like 21/3a, or 'see also')")
    elif not RELATION_ANY.search(body_text):
        add(0, "INFO", "关系未标注", f"{n_links} 条连接", "连接应注明关系（支持/反驳/补充/延伸/修正）"
            if lang == "zh" else "Label each link: supports / contradicts / extends / qualifies / revises")

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    issues.sort(key=lambda x: (order[x["level"]], x["line"]))
    return {
        "file": name, "lang": lang, "length": n_len, "length_unit": unit,
        "links": n_links, "frontmatter": fm,
        "errors": sum(1 for x in issues if x["level"] == "ERROR"),
        "warnings": sum(1 for x in issues if x["level"] == "WARN"),
        "issues": issues,
    }


def report(res):
    print(f"\n=== {res['file']} ===")
    print(f"语言 {res['lang']}｜正文 {res['length']} {res['length_unit']}｜连接 {res['links']} 条")
    if not res["errors"] and not res["warnings"]:
        for x in res["issues"]:
            print(f"[INFO] {x['rule']} → {x['advice']}")
        print("✅ 未发现机械问题。仍须人工做「三年后测试」：遮住来源重读，看是否读得懂。")
        return
    for x in res["issues"]:
        loc = f"L{x['line']}" if x["line"] else "全文"
        print(f"[{x['level']}] {loc} {x['rule']}" + (f"｜{x['fragment']}" if x["fragment"] else "")
              + f"\n        → {x['advice']}")
    print(f"\n合计 {len(res['issues'])} 条线索（ERROR {res['errors']}，WARN {res['warnings']}）")


DEMOS = [
    ("坏例（中文，应报多条 ERROR/WARN）", """# 关于反馈的笔记

这个观点很有意思。作者认为反馈很重要，但我觉得不止是反馈本身，反馈的频率也很关键。就像上文说的，如果反馈太慢，调整就来不及了。
"""),
    ("好例（中文，应干净；2024/12 不算连接）", """---
status: reviewed
author: human
sources: [[刻意练习-第78页]]
updated: 2026-11-01
---
# 反馈的频率比反馈的质量更重要

很多人讨论反馈时，关注的是反馈是否准确、是否有建设性。但在技能习得中，更关键的因素是反馈的频率。如果反馈太慢——比如 2024/12 交的作业一个月后才收到批改——你在等待期间会反复重复错误的动作，错误会固化成习惯。即时反馈让「尝试—调整」的循环周期尽可能短，让错误在成为习惯之前就被纠正。

支持：[[即时反馈缩短纠错周期]]；反驳：[[过度反馈抑制自主探索]]
"""),
    ("坏例（英文，应报 ERROR/WARN）", """# Notes on feedback

This idea is very important. The author argues that feedback matters, and as mentioned above, slow feedback is bad. Moreover, frequency matters too.
"""),
    ("好例（英文，应干净）", """---
status: reviewed
author: human
sources: ["Ericsson 2016, p.78"]
---
# Feedback frequency matters more than feedback quality in skill acquisition

When feedback arrives weeks after an attempt, the learner keeps repeating the faulty movement in the meantime, and the error hardens into habit. Fast feedback shortens the try-adjust loop so mistakes are corrected before they become automatic, which is why frequent rough feedback often beats rare polished feedback.

Supports: [[Immediate feedback shortens error correction]]; contradicts: [[Too much feedback suppresses exploration]]
"""),
    ("AI 草稿却标 reviewed（应报 ERROR）", """---
status: reviewed
author: ai
sources: []
---
# 间隔重复利用遗忘曲线安排复习时机

在即将遗忘之前复习，提取难度适中，记忆巩固效果最好；间隔随每次成功提取而拉长，因此同样的复习次数能覆盖更长的保持期。

延伸：[[提取练习强化记忆]]
"""),
]


def main(argv=None):
    ap = argparse.ArgumentParser(add_help=False, description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lang", choices=["zh", "en", "auto"], default="auto")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("-h", "--help", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    if a.help:
        print(__doc__)
        return 0
    if a.demo:
        results = [check_text(t, n, a.lang) for n, t in DEMOS]
    elif not a.files:
        print(__doc__)
        return 2
    else:
        results = []
        for path in a.files:
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except (OSError, UnicodeDecodeError) as e:
                print(f"无法读取 {path}: {e}", file=sys.stderr)
                return 2
            results.append(check_text(text, path, a.lang))
    if a.json:
        print(json.dumps(results if len(results) != 1 else results[0], ensure_ascii=False, indent=2))
    else:
        for r in results:
            report(r)
    if a.demo:
        return 0
    failed = any(r["errors"] or (a.strict and r["warnings"]) for r in results)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
