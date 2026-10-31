#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""永久笔记机械自检。

按教程第 23 篇「永久笔记的写作标准」把可机械判定的部分写成硬阈值：
指示代词、来源依赖、上下文指代、模糊评价、摘抄嫌疑、标题是否陈述主张、
是否有连接与关系标注、篇幅是否越界。

用法：
    python3 check_card.py <卡片.md> [<卡片2.md> ...]
    python3 check_card.py 卡片.md --strict      # 有 ERROR 时退出码 1
    python3 check_card.py --demo                # 用内置样例自检本脚本

输出只报线索（行号 + 命中项 + 原文片段），不做终判。
术语与冗词的区分、语气是否恰当，须人工确认。
"""

import re
import sys

# 每条规则：(级别, 名称, 正则, 提示)
RULES = [
    ("ERROR", "指示代词（依赖上下文）",
     r"这个观点|这个方法|这个理论|这个结论|这种做法|这种情况",
     "把指代对象写进卡片本身，让三年后的自己不翻别的卡也读得懂"),
    ("ERROR", "来源依赖（以他人之口代替陈述）",
     r"作者认为|作者说|书中说|文章中提到|某某认为|正如上文|如前所述|上面提到",
     "直接陈述主张，来源移到卡片末尾"),
    ("WARN", "模糊评价（缺论证）",
     r"很重要|非常关键|很有意思|有启发|值得注意|意义重大|至关重要",
     "补上机制或例子：它为什么重要、通过什么起作用"),
    ("WARN", "摘抄嫌疑（长段引文）",
     r"[\"“”][^\"“”]{30,}[\"“”]",
     "超过 30 字的连续引文多为摘抄；改成自己的话重述，原文留作来源"),
    ("WARN", "可能含多个想法",
     r"另外|此外|还有一点|另一方面|再比如",
     "一卡一想法；第二个想法应另起一张卡并连接过来"),
    ("INFO", "关系标注缺失",
     r"^(?!.*(支持|反驳|补充|延伸|矛盾|参见|相关)).*$",
     "连接宜注明关系类型（支持／反驳／补充／延伸）"),
]

# 标题规则：主题标签式标题（不陈述主张）
TITLE_BAD = re.compile(r"^#+\s*(关于.*的笔记|.*读书笔记|.*感想|笔记：|.*摘录|.*摘抄|读书笔记.*|.*总结)$")
# 连接：[[双链]] 或 编号引用
LINK_RE = re.compile(r"\[\[[^\]]+\]\]|[0-9]{1,4}/[0-9a-zA-Z]{1,6}|参见\s*\S+")

MIN_CHARS, MAX_CHARS = 40, 500
A6_MIN, A6_MAX = 100, 200  # 纸卡 A6 容量参照


def check_text(text, name="<stdin>"):
    """返回 (问题列表, 正文字数, 连接数)。"""
    lines = text.split("\n")
    issues = []

    # 标题检查
    for i, line in enumerate(lines[:3], 1):
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            if TITLE_BAD.search(line):
                issues.append((i, "WARN", "标题未陈述主张", title,
                               "标题应直接写主张，如「反馈的频率比反馈的质量更重要」"))
            break
    else:
        issues.append((1, "WARN", "缺少标题", "", "卡片应有标题，且标题直接陈述主张"))

    # 逐行规则
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("#"):
            continue
        for level, label, pattern, advice in RULES:
            if label == "关系标注缺失":
                continue  # 该规则在全文层判定
            for m in re.finditer(pattern, line):
                frag = line[max(0, m.start() - 12):m.end() + 12].strip()
                issues.append((i, level, label, frag, advice))
                break  # 同一行同一规则只报一次

    body = "\n".join(l for l in lines if not l.lstrip().startswith("#"))
    n_chars = len(re.sub(r"\s", "", body))
    n_links = len(LINK_RE.findall(text))

    if n_chars < MIN_CHARS:
        issues.append((0, "ERROR", "内容过短", f"{n_chars} 字",
                       f"不足 {MIN_CHARS} 字：只有关键词或一句评价，等于没写"))
    elif n_chars > MAX_CHARS:
        issues.append((0, "WARN", "篇幅过长", f"{n_chars} 字",
                       f"超过 {MAX_CHARS} 字：多半塞进了第二个想法，应拆卡互联"))

    if n_links == 0:
        issues.append((0, "ERROR", "无连接", "0 条",
                       "每张卡至少 1 条连接（[[双链]]／编号／参见）"))
    elif not re.search(r"支持|反驳|补充|延伸|矛盾", body):
        issues.append((0, "INFO", "关系未标注", f"{n_links} 条连接",
                       "连接应注明关系类型（支持／反驳／补充／延伸）"))

    return issues, n_chars, n_links


def report(issues, n_chars, n_links, name):
    print(f"\n=== {name} ===")
    print(f"正文 {n_chars} 字｜连接 {n_links} 条")
    if not issues:
        print("✅ 未发现机械问题。仍须人工做「三年后测试」：遮住来源重读，看是否读得懂。")
        return 0
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    issues.sort(key=lambda x: (order[x[1]], x[0]))
    n_err = sum(1 for x in issues if x[1] == "ERROR")
    for line_no, level, label, frag, advice in issues:
        loc = f"L{line_no}" if line_no else "全文"
        print(f"[{level}] {loc} {label}"
              + (f"｜{frag}" if frag else "")
              + f"\n        → {advice}")
    print(f"\n合计 {len(issues)} 条线索（ERROR {n_err}）")
    return n_err


DEMO_BAD = """# 关于反馈的笔记

这个观点很有意思。作者认为反馈很重要，但我觉得不止是反馈本身，反馈的频率也很关键。就像上文说的，如果反馈太慢，调整就来不及了。
"""

DEMO_GOOD = """# 反馈的频率比反馈的质量更重要

很多人讨论反馈时，关注的是反馈是否准确、是否有建设性。但在技能习得中，更关键的因素是反馈的频率。如果反馈太慢——比如一个月后才收到老师的批改——你在等待期间会反复重复错误的动作，错误会固化成习惯。等反馈来了，你不仅要学正确的动作，还要先改掉错误的习惯。即时反馈的价值在于：它让「尝试—调整」的循环周期尽可能短，让错误在成为习惯之前就被纠正。

支持：[[即时反馈缩短纠错周期]]；反驳：[[过度反馈抑制自主探索]]
来源：文献笔记《刻意练习》第 78 页
"""


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv

    if "--demo" in sys.argv:
        print("—— 坏例（应报出多条 ERROR/WARN）——")
        report(*check_text(DEMO_BAD), "坏例")
        print("\n—— 好例（应基本干净）——")
        report(*check_text(DEMO_GOOD), "好例")
        return 0

    if not args:
        print(__doc__)
        return 0

    total_err = 0
    for path in args:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        issues, n_chars, n_links = check_text(text, path)
        total_err += report(issues, n_chars, n_links, path)
    if strict and total_err:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
