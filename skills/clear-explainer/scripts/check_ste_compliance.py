#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_ste_compliance.py — ASD-STE100 机械自检（英文，严格档）

把 ASD-STE100 Issue 9 的 53 条规则里**可以机械判定**的部分做成检查器。
它只报线索，不做终判：STE 有大量判断依赖"这个词在这个位置是不是技术名词"，
机器判不了。把报告当"该看哪几行"的清单用。

用法
    python3 check_ste_compliance.py draft.md
    python3 check_ste_compliance.py draft.md --mode procedural      # 强制按程序性写作判定
    python3 check_ste_compliance.py draft.md --mode descriptive     # 强制按描述性写作判定
    cat draft.md | python3 check_ste_compliance.py -
    python3 check_ste_compliance.py draft.md --json
    python3 check_ste_compliance.py draft.md --strict               # 有 hard 级问题则退出码 1
    python3 check_ste_compliance.py draft.md --no-dictionary        # 跳过未核准词检查

检查项（括号内为 ASD-STE100 规则号）
    hard  分号 (8.1) · 缩略式 (4.2) · 句长超限 (5.1/6.3/5.5) · 段落超 6 句 (6.6)
          完成时 (3.2) · 进行时 (3.2) · 助动词被动构造 (3.4) · 未核准词 (1.1/1.2/1.3)
          竖排列表项用逗号/分号收尾 (4.3) · 竖排列表缺冒号 (4.3)
    warn  被动语态 (3.6) · -ing 非白名单 (3.5) · 短语动词 (9.3) · 拉丁缩写 (GR-6)
          英式拼写 (1.14) · 列表项首字母未大写 (4.3) · 条件放到句尾 (5.4)
          祈使式前加 must (5.3) · NOTE 里出现祈使式或限值 (5.5)
          WARNING/CAUTION 缺风险解释 (7.3)
    info  疑似 multi-word noun 超过 3 词 (2.1) · 疑似沿用省略冠词的写法 (4.2/4.5)

计词规则（Rule 8.4–8.7，本脚本按保守方式实现）
    括号内整段文本在宿主句中算 1 词（括号内文本另行单独检查）
    引号内文本算 1 词 · 数字算 1 词 · 数字+计量单位算 1 词 · 带句点的缩写算 1 词
    连字符词算 1 词 · 字母数字标识（36L7、No. 1）算 1 词
    ⚠️ 未实现：标题/标语/专有名词整块算 1 词。本脚本不折叠它们，因此词数偏保守
       （宁可报超限，不放过）。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- 常量

HARD_LIMIT_PROCEDURAL = 20      # Rule 5.1
HARD_LIMIT_DESCRIPTIVE = 25     # Rule 6.3
MAX_PARAGRAPH_SENTENCES = 6     # Rule 6.6

# Rule 3.5：词典中带 -ing 的核准词（数量极少，原文逐项列出）+ 常见技术名词修饰语
ING_WHITELIST = {
    # Rule 3.5 原书列出的"已是核准词"的 -ing 词
    "lighting", "opening", "routing", "servicing",        # nouns
    "mating", "missing", "remaining",                      # adjectives
    "something", "during",                                 # pronoun / preposition
    # 原书点名的技术名词（程序标题类）
    "cleaning", "testing", "handling", "packaging", "shipping", "troubleshooting",
    # 常见"功能修饰语 + 名词"型技术名词与工艺名词（Rule 3.5 放行的第二格）
    "engineering", "bearing", "housing", "wiring", "coating", "sealing", "fastening",
    "fitting", "mounting", "coupling", "tubing", "cabling", "packing", "casing",
    "lining", "sleeving", "piping", "plumbing", "marking", "warning", "heading",
    "landing", "sanding", "grinding", "polishing", "welding", "switching",
    # 普通英语高频词，避免噪音
    "thing", "things", "nothing", "anything", "everything", "string", "ring",
    "king", "bring", "spring", "ceiling", "morning", "evening", "meeting",
    "building", "working", "running", "using", "making", "going", "coming",
}

# Rule 9.3 短语动词。前两个是原书点名的禁止项，其余为常见补充（标注 [补充]）
PHRASAL_VERBS_BOOK = {
    "put out": "EXTINGUISH (v)",
    "give off": "RELEASE (v)",
}
PHRASAL_VERBS_EXTRA = {
    "carry out": "DO (v) / DO THE ... ",
    "set up": "INSTALL (v) / ADJUST (v)",
    "turn on": "SET ... TO ON",
    "turn off": "SET ... TO OFF",
    "find out": "MAKE SURE (v) / EXAMINE (v)",
    "look at": "EXAMINE (v) / LOOK (v)",
    "go on": "CONTINUE (v)",
    "keep on": "CONTINUE (v)",
    "take off": "REMOVE (v)",
    "put in": "INSTALL (v)",
    "check out": "EXAMINE (v)",
}

# GR-6 拉丁缩写
LATIN_ABBREV = {
    "e.g.": "for example",
    "i.e.": "that is",
    "etc.": "（列举完即可，删掉）",
    "vs.": "compared with",
    "et al.": "and other persons",
    "cf.": "refer to",
    "viz.": "that is",
    "ibid.": "（不要用）",
}

# Rule 1.14 常见英式拼写 → 美式
BRITISH_SPELLING = {
    "colour": "color", "colours": "colors", "coloured": "colored",
    "fibre": "fiber", "fibres": "fibers",
    "centre": "center", "centres": "centers", "centred": "centered",
    "metre": "meter", "metres": "meters", "litre": "liter", "litres": "liters",
    "aluminium": "aluminum",
    "catalogue": "catalog", "catalogues": "catalogs",
    "analyse": "analyze", "analysed": "analyzed", "analysing": "analyzing",
    "organisation": "organization", "organise": "organize", "organised": "organized",
    "recognise": "recognize", "recognised": "recognized",
    "authorise": "authorize", "authorised": "authorized",
    "utilise": "utilize（且 utilize 本身也不核准，用 USE）",
    "labour": "labor", "behaviour": "behavior", "favour": "favor",
    "humour": "humor", "vapour": "vapor",
    "grey": "gray", "modelling": "modeling", "modelled": "modeled",
    "travelled": "traveled", "cancelled": "canceled", "fuelled": "fueled",
    "programme": "program", "dialogue": "dialog",
    "defence": "defense", "offence": "offense", "licence": "license",
    "practise": "practice", "storey": "story", "tyre": "tire",
    "aeroplane": "airplane", "ageing": "aging", "judgement": "judgment",
    "acknowledgement": "acknowledgment", "enquiry": "inquiry",
}

# 缩略式（Rule 4.2 禁）
CONTRACTION_RE = re.compile(
    r"\b\w+['\u2019](?:t|re|ve|ll|d|m|s)\b", re.I)

# 过去分词：规则动词 -ed，不规则动词用显式清单（**不用**笼统的 -en 后缀，
# 否则 open / often / when 这类普通词会被误判为被动或完成时）
IRREGULAR_PARTICIPLES = (
    "made|done|given|taken|seen|shown|found|held|kept|left|put|set|written|built|"
    "sent|read|chosen|known|begun|broken|brought|bought|got|gotten|become|come|"
    "run|frozen|worn|torn|drawn|grown|blown|thrown|flown|driven|hidden|bitten|"
    "beaten|forgotten|spoken|stolen|woken|risen|fallen|shaken|eaten|forbidden|"
    "laid|paid|sold|told|cut|hit|let|cost|arises|rises"
)
PARTICIPLE = rf"(?:\w{{3,}}ed|{IRREGULAR_PARTICIPLES})"

# 完成时（Rule 3.2 禁）
PERFECT_RE = re.compile(rf"\b(?:have|has|had)\s+(?:been\s+)?{PARTICIPLE}\b", re.I)

# 进行时（Rule 3.2 禁）
PROGRESSIVE_RE = re.compile(r"\b(?:is|are|was|were|be|been)\s+(?:\w+ing)\b", re.I)

# 助动词被动构造（Rule 3.4 禁）
AUX_PASSIVE_RE = re.compile(
    rf"\b(?:can|could|must|will|would|shall|should|may|might)\s+be\s+{PARTICIPLE}\b"
    rf"|\b(?:is|are|was|were)\s+to\s+be\s+{PARTICIPLE}\b", re.I)

# 被动语态（Rule 3.6，需人工确认 agent 是否未知）
PASSIVE_RE = re.compile(
    rf"\b(?:is|are|was|were|be|been|being)\s+{PARTICIPLE}\b", re.I)

# 数字 + 计量单位（Rule 8.6 第 2 类）
UNIT = (r"(?:°C|°F|kg|mg|g|km|cm|mm|µm|nm|m|psi|bar|kPa|MPa|Pa|Nm|N|kV|V|mA|A|"
        r"mW|kW|W|GHz|MHz|kHz|Hz|ml|cc|L|l|ms|s|min|h|rpm|dB|%|"
        r"hours?|minutes?|seconds?|days?|weeks?|months?|years?|"
        r"inches|inch|feet|foot|ft|yards?|miles?|pounds?|lbs?|lb|oz|"
        r"ohms?|knots?|degrees?)")
NUMBER_UNIT_RE = re.compile(rf"\b\d+(?:[.,]\d+)?\s*{UNIT}\b", re.I)

# 带句点的缩写（Rule 8.6 第 3 类）：a.m. / No. / Fig.
DOTTED_ABBREV_RE = re.compile(r"\b(?:[A-Za-z]\.){2,}|\bNo\.\s*\d+", re.I)

QUOTED_RE = re.compile(r"\"[^\"]*\"|\u201c[^\u201d]*\u201d")
PAREN_RE = re.compile(r"\([^()]*\)")

# 祈使式常见动词（用于判定"程序性句子"）
IMPERATIVE_VERBS = {
    "add", "adjust", "apply", "assemble", "attach", "become", "bleed", "bond",
    "break", "calibrate", "care", "change", "check", "clean", "clear", "close",
    "comprise", "connect", "contain", "continue", "control", "cut", "decrease",
    "disconnect", "discard", "do", "drain", "dry", "energize", "engage", "examine",
    "extend", "fill", "find", "flush", "form", "get", "give", "go", "hold",
    "identify", "include", "increase", "inflate", "install", "isolate", "keep",
    "lift", "listen", "load", "locate", "lock", "look", "loosen", "lower",
    "lubricate", "make", "measure", "mix", "monitor", "move", "obey", "open",
    "operate", "point", "position", "pour", "prepare", "press", "prevent",
    "provide", "push", "put", "read", "refer", "release", "reload", "remove",
    "replace", "retract", "rotate", "run", "seal", "set", "slow", "speak",
    "start", "stop", "supply", "tag", "test", "tighten", "touch", "turn", "use",
    "wait", "wind", "write", "zero",
}


def _verb_forms() -> set:
    forms = set()
    for v in IMPERATIVE_VERBS:
        forms |= {v, v + "s", v + "es", v + "ed", v + "ing"}
        if v.endswith("e"):
            forms |= {v[:-1] + "ing", v + "d"}
    return forms


# 疑似 multi-word noun（Rule 2.1 的启发式）：4 个以上连续的非动词、非虚词实词
NOUN_STOPWORDS = _verb_forms() | {
    "the", "a", "an", "this", "these", "those", "that", "of", "to", "in", "on", "for",
    "at", "by", "with", "from", "into", "onto", "and", "or", "but", "then", "thus",
    "when", "while", "if", "unless", "until", "before", "after", "because", "as",
    "is", "are", "was", "were", "be", "been", "being", "can", "must", "will", "do",
    "does", "did", "have", "has", "had", "you", "we", "they", "it", "its", "not",
    "no", "more", "less", "than", "all", "each", "other", "some", "any", "there",
    "here", "also", "again", "both", "many", "much", "most", "one", "two", "three",
    "four", "five", "six", "seven", "eight", "nine", "ten", "twenty", "thirty",
    "first", "second", "third", "fourth", "fifth", "sixth", "last", "next",
}

LIST_ITEM_RE = re.compile(r"^\s*(?:[-*\u2022\u2013]|\(?\d+[.)]|\(?[a-z][.)]|\(?[A-Z][.)])\s+")
VERTICAL_LIST_MARKER_RE = re.compile(r"^\s*(?:[-*\u2022\u2013]|\(?\d+[.)]|\([a-zA-Z]\))\s+")


# ---------------------------------------------------------------- 数据结构

@dataclass
class Finding:
    line: int
    rule: str
    kind: str
    detail: str
    text: str = ""
    severity: str = "warn"      # hard | warn | info


@dataclass
class Stats:
    sentences: int = 0
    procedural: int = 0
    descriptive: int = 0
    paragraphs: int = 0
    words: int = 0
    by_kind: dict = field(default_factory=dict)
    findings: list = field(default_factory=list)

    def add(self, f: Finding) -> None:
        self.findings.append(f)
        self.by_kind[f.kind] = self.by_kind.get(f.kind, 0) + 1


# ---------------------------------------------------------------- 预处理

def strip_noise(text: str) -> str:
    """去掉代码块，避免把代码当正文检查。"""
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " CODE ", text)
    return text


def count_words(sentence: str) -> int:
    """按 Rule 8.4–8.7 计算词数（保守实现，见文件头说明）。"""
    s = sentence
    s = PAREN_RE.sub(" PARENCONTENT ", s)          # 8.5：括号内整段 = 1 词
    s = QUOTED_RE.sub(" QUOTEDTEXT ", s)           # 8.6-5：引用文本 = 1 词
    s = DOTTED_ABBREV_RE.sub(" ABBR ", s)          # 8.6-3 / 8.6-4
    s = NUMBER_UNIT_RE.sub(" NUMUNIT ", s)         # 8.6-2
    s = re.sub(r"\b\d+(?:[.,]\d+)?\b", " NUM ", s)  # 8.6-1
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/_]*", s)
    return len(tokens)


def split_sentences(text: str) -> list[str]:
    """分句：句末标点 + 换行。保护常见缩写里的点。"""
    protected = text
    for ab in ("No.", "Fig.", "Ref.", "Sec.", "Para.", "approx.", "max.", "min.",
               "e.g.", "i.e.", "etc.", "vs.", "a.m.", "p.m.", "Dr.", "Mr."):
        protected = protected.replace(ab, ab.replace(".", "\u2024"))
    parts = re.split(r"(?<=[.!?\u2024])[\s]+|\n+", protected)
    out = []
    for p in parts:
        p = p.strip().replace("\u2024", ".")
        if p:
            out.append(p)
    return out


def iter_paragraphs(text: str):
    """按空行切段，返回 (起始行号, 段落文本)。"""
    lines = text.splitlines()
    buf, start = [], 0
    for i, raw in enumerate(lines, 1):
        if raw.strip():
            if not buf:
                start = i
            buf.append(raw)
        else:
            if buf:
                yield start, "\n".join(buf)
                buf = []
    if buf:
        yield start, "\n".join(buf)


def first_word(sentence: str) -> str:
    s = LIST_ITEM_RE.sub("", sentence.strip())
    s = re.sub(r"^(?:NOTE|WARNING|CAUTION)\s*:\s*", "", s, flags=re.I)
    m = re.match(r"[A-Za-z']+", s)
    return m.group(0).lower() if m else ""


def is_procedural(sentence: str) -> bool:
    return first_word(sentence) in IMPERATIVE_VERBS


# ---------------------------------------------------------------- 词表

def load_unapproved(path: Path) -> dict:
    d = {}
    if not path.exists():
        return d
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        cells = line.split("\t")
        if len(cells) >= 3 and cells[0].strip():
            d[cells[0].strip().lower()] = cells[2].strip()
    return d


# ---------------------------------------------------------------- 检查

def check_sentence(line_no: int, sent: str, st: Stats, mode: str,
                   unapproved: dict, is_note: bool, is_safety: bool) -> None:
    st.sentences += 1
    wor = count_words(sent)
    st.words += wor

    procedural = (mode == "procedural") or (mode == "auto" and is_procedural(sent))
    if is_safety:
        # Rule 5.1：WARNING/CAUTION 与其他安全指令同样受 20 词上限约束
        limit = HARD_LIMIT_PROCEDURAL
        st.procedural += 1
    elif is_note:
        limit = HARD_LIMIT_DESCRIPTIVE          # 5.5
    elif procedural:
        limit = HARD_LIMIT_PROCEDURAL
        st.procedural += 1
    else:
        limit = HARD_LIMIT_DESCRIPTIVE
        st.descriptive += 1

    snip = sent if len(sent) <= 70 else sent[:70] + "…"

    # --- 句长
    if wor > limit:
        st.add(Finding(line_no, "5.1" if procedural else "6.3", "句长超限",
                       f"{wor} 词 > {limit} 词", snip, "hard"))

    # --- 8.1 分号
    if ";" in sent:
        st.add(Finding(line_no, "8.1", "分号", "STE 禁用分号，拆成两个句子", snip, "hard"))

    # --- 4.2 缩略式
    for m in CONTRACTION_RE.finditer(sent):
        st.add(Finding(line_no, "4.2", "缩略式", f"{m.group(0)} → 写全", snip, "hard"))

    # --- 3.2 完成时 / 进行时
    for m in PERFECT_RE.finditer(sent):
        st.add(Finding(line_no, "3.2", "完成时", f"{m.group(0)} → 用一般过去时或现在时", snip, "hard"))
    for m in PROGRESSIVE_RE.finditer(sent):
        st.add(Finding(line_no, "3.2", "进行时", f"{m.group(0)} → 用一般时态", snip, "hard"))

    # --- 3.4 助动词被动构造
    for m in AUX_PASSIVE_RE.finditer(sent):
        st.add(Finding(line_no, "3.4", "助动词被动构造",
                       f"{m.group(0)} → 程序句改祈使式 / 描述句改主动", snip, "hard"))

    # --- 3.6 被动语态
    for m in PASSIVE_RE.finditer(sent):
        if AUX_PASSIVE_RE.search(m.group(0)):
            continue
        st.add(Finding(line_no, "3.6", "被动语态",
                       f"{m.group(0)} → 确认 agent 是否未知；只有描述性写作且 agent 未知才可保留", snip))

    # --- 3.5 -ing 非白名单
    for m in re.finditer(r"\b(\w{4,}ing)\b", sent, re.I):
        w = m.group(1).lower()
        if w in ING_WHITELIST:
            continue
        st.add(Finding(line_no, "3.5", "-ing 用法",
                       f"{m.group(1)} → 只准作技术名词或技术名词中的修饰语", snip, "info"))

    # --- 9.3 短语动词
    low = sent.lower()
    for pv, fix in PHRASAL_VERBS_BOOK.items():
        if re.search(rf"\b{re.escape(pv)}\b", low):
            st.add(Finding(line_no, "9.3", "短语动词（原书点名）",
                           f"{pv} → {fix}", snip))
    for pv, fix in PHRASAL_VERBS_EXTRA.items():
        if re.search(rf"\b{re.escape(pv)}\b", low):
            st.add(Finding(line_no, "9.3", "短语动词 [补充]",
                           f"{pv} → {fix}", snip, "info"))

    # --- GR-6 拉丁缩写
    for ab, fix in LATIN_ABBREV.items():
        if re.search(rf"(?<![\w]){re.escape(ab)}", sent, re.I):
            st.add(Finding(line_no, "GR-6", "拉丁缩写", f"{ab} → {fix}", snip))

    # --- 1.14 英式拼写
    for m in re.finditer(r"\b[A-Za-z]+\b", sent):
        w = m.group(0).lower()
        if w in BRITISH_SPELLING:
            st.add(Finding(line_no, "1.14", "英式拼写", f"{m.group(0)} → {BRITISH_SPELLING[w]}", snip))

    # --- 1.1/1.2/1.3 未核准词
    if unapproved:
        for m in re.finditer(r"\b[A-Za-z][A-Za-z'\- ]{1,20}\b", sent):
            w = m.group(0).strip().lower()
            if w in unapproved:
                st.add(Finding(line_no, "1.1", "未核准词",
                               f"{m.group(0)} → {unapproved[w] or '（词典未给替代词）'}", snip, "hard"))

    # --- 5.4 条件放句尾
    if procedural and re.search(r",\s*(?:when|if)\b", sent, re.I):
        st.add(Finding(line_no, "5.4", "条件位置",
                       "条件从句要放在命令之前（条件 + 逗号 + 命令）", snip))
    if procedural and re.search(r"\b(?:when|if)\b[^,]{0,40}\.$", sent, re.I) and "," in sent:
        st.add(Finding(line_no, "5.4", "条件位置",
                       "疑似把条件写在命令之后，改为条件前置", snip))

    # --- 5.3 祈使式前加 must
    if procedural and re.search(r"\byou\s+must\b", sent, re.I):
        st.add(Finding(line_no, "5.3", "must 误用",
                       "祈使式前不加 must（除非安全指令或重要条件）", snip))

    # --- 5.5 NOTE 里的祈使式与限值
    if is_note:
        if is_procedural(sent):
            st.add(Finding(line_no, "5.5", "NOTE 含祈使式",
                           "NOTE 只给信息、不给指令；祈使式应写成工作步骤", snip))
        if re.search(r"\b(?:must|shall)\b.{0,30}\b(?:not\s+)?(?:more|less|greater|smaller)\b|"
                     r"\bmaximum\b|\bminimum\b|\btolerance\b", sent, re.I):
            st.add(Finding(line_no, "5.5", "NOTE 含限值",
                           "限值/公差必须写在相关工作步骤里，不能藏在 NOTE 中", snip))

    # --- 2.1 疑似 multi-word noun 超 3 词
    toks = re.findall(r"'?[A-Za-z][A-Za-z\-]*", sent)
    run: list[str] = []
    for t in toks:
        if t.lower() not in NOUN_STOPWORDS and len(t) > 2:
            run.append(t)
        else:
            if len(run) >= 4:
                st.add(Finding(line_no, "2.1", "疑似 multi-word noun 超 3 词",
                               " ".join(run), snip, "info"))
            run = []
    if len(run) >= 4:
        st.add(Finding(line_no, "2.1", "疑似 multi-word noun 超 3 词", " ".join(run), snip, "info"))


def check_safety(line_no: int, para: str, st: Stats) -> None:
    """Rule 7.1–7.3：级别词 / 命令或条件起句 / 风险解释。"""
    sents = split_sentences(para)
    if len(sents) < 2:
        st.add(Finding(line_no, "7.3", "安全指令缺解释",
                       "WARNING/CAUTION 必须给出解释，说明风险或可能后果",
                       para[:70], "warn"))
        return
    head = re.sub(r"^(?:WARNING|CAUTION)\s*:\s*", "", sents[0], flags=re.I)
    if not (is_procedural(head) or re.match(r"^(?:when|while|before|if|after)\b", head, re.I)
            or re.match(r"^do not\b", head, re.I)):
        st.add(Finding(line_no, "7.2", "安全指令起句",
                       "必须以清晰的命令或条件起句，不能以说明/背景起句",
                       sents[0][:70], "warn"))
    if not re.search(r"\b(?:injur|death|poison|explos|corros|damage|burn|electric|"
                     r"fire|toxic|permanent|risk|danger|harm)\w*\b",
                     " ".join(sents[1:]), re.I):
        st.add(Finding(line_no, "7.3", "安全指令缺具体危害",
                       "解释里要具名具体危害（injury/death/explosion/corrosion/damage…）",
                       " ".join(sents[1:])[:70], "warn"))


def check_lists(text: str, st: Stats) -> None:
    """Rule 4.3：竖排列表结构。"""
    lines = text.splitlines()
    for i, raw in enumerate(lines, 1):
        m = VERTICAL_LIST_MARKER_RE.match(raw)
        if not m:
            continue
        item = raw[m.end():].rstrip()
        nxt = lines[i].strip() if i < len(lines) else ""
        is_last = not VERTICAL_LIST_MARKER_RE.match(nxt)

        if item.endswith(",") or item.endswith(";"):
            st.add(Finding(i, "4.3", "列表项标点",
                           "列表项末尾不得加逗号或分号", item[:70], "hard"))
        # 首字母大写（允许全大写与数字开头）
        if item and item[0].islower():
            st.add(Finding(i, "4.3", "列表项首字母",
                           "每项以大写字母开头", item[:70]))
        # 最后一项应有句点（仅当整段都是列表时提示）
        if is_last and item and not item.endswith("."):
            st.add(Finding(i, "4.3", "列表末项",
                           "最后一项末尾加句点", item[:70], "info"))
        # 该项之前的引言行应以冒号收尾
        j = i - 2
        while j >= 0 and VERTICAL_LIST_MARKER_RE.match(lines[j]):
            j -= 1
        if j >= 0 and lines[j].strip() and not lines[j].rstrip().endswith(":"):
            st.add(Finding(j + 1, "4.3", "列表缺冒号",
                           "竖排列表第一项之前，引言句末尾要加冒号",
                           lines[j].strip()[:70], "hard"))


def check_document(text: str, st: Stats, mode: str, unapproved: dict) -> None:
    for line_no, para in iter_paragraphs(text):
        st.paragraphs += 1
        head = para.strip()
        is_note = bool(re.match(r"^NOTE\s*:", head, re.I))
        is_safety = bool(re.match(r"^(?:WARNING|CAUTION)\s*:", head, re.I))

        sents = split_sentences(para)
        for s in sents:
            check_sentence(line_no, s, st, mode, unapproved, is_note, is_safety)
        if len(sents) > MAX_PARAGRAPH_SENTENCES:
            st.add(Finding(line_no, "6.6", "段落超长",
                           f"{len(sents)} 句 > {MAX_PARAGRAPH_SENTENCES} 句，拆成两段",
                           head[:70], "hard"))
        if is_safety:
            check_safety(line_no, para, st)

    check_lists(text, st)


# ---------------------------------------------------------------- 报告

def score(st: Stats) -> int:
    if not st.sentences:
        return 100
    hard = sum(1 for f in st.findings if f.severity == "hard")
    warn = sum(1 for f in st.findings if f.severity == "warn")
    info = sum(1 for f in st.findings if f.severity == "info")
    s = 100 - 100 * hard / st.sentences - 40 * warn / st.sentences - 12 * info / st.sentences
    return max(0, min(100, round(s)))


def render(path: str, st: Stats, max_items: int = 60) -> str:
    out = [f"== ASD-STE100 合规体检 · {path} ==", ""]
    if not st.findings:
        out.append("  未发现可机械判定的违规。")
    else:
        order = {"hard": 0, "warn": 1, "info": 2}
        items = sorted(st.findings, key=lambda f: (order[f.severity], f.line))
        counts = {k: sum(1 for f in items if f.severity == k) for k in order}
        out.append(f"  命中 {len(items)} 条（hard {counts['hard']} / warn {counts['warn']} / info {counts['info']}）：")
        for f in items[:max_items]:
            out.append(f"  [{f.severity:<4}] Rule {f.rule:<5} L{f.line:<5} {f.kind}：{f.detail}")
            if f.text:
                out.append(f"  {'':<36}↳ {f.text}")
        if len(items) > max_items:
            out.append(f"  … 还有 {len(items) - max_items} 条，用 --json 取全量")
    out.append("")
    out.append("  统计：")
    out.append(f"    句 {st.sentences}（程序 {st.procedural} / 描述 {st.descriptive}）· 段 {st.paragraphs} · 约 {st.words} 词")
    if st.by_kind:
        top = sorted(st.by_kind.items(), key=lambda kv: -kv[1])[:8]
        out.append("    高频问题：" + " · ".join(f"{k} {v}" for k, v in top))
    sc = score(st)
    grade = "优" if sc >= 85 else ("良" if sc >= 70 else ("及格" if sc >= 55 else "需重写"))
    out.append("")
    out.append(f"  评分 {sc}/100（{grade}）")
    out.append("")
    out.append("  说明：只报线索，不做终判。STE 里大量判断依赖「这个词在此处是不是技术名词」，")
    out.append("        机器判不了；未核准词表是 244 条节选，未报不等于没问题。")
    return "\n".join(out)


def render_json(path: str, st: Stats) -> str:
    return json.dumps({
        "file": path, "score": score(st),
        "stats": {"sentences": st.sentences, "procedural": st.procedural,
                  "descriptive": st.descriptive, "paragraphs": st.paragraphs,
                  "words": st.words, "by_kind": st.by_kind},
        "findings": [{"line": f.line, "rule": f.rule, "kind": f.kind,
                      "severity": f.severity, "detail": f.detail, "text": f.text}
                     for f in st.findings],
    }, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------- 入口

def main() -> int:
    ap = argparse.ArgumentParser(description="ASD-STE100 机械自检（英文）",
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="待检查的文件，或 - 表示读 stdin")
    ap.add_argument("--mode", default="auto",
                    choices=["auto", "procedural", "descriptive"],
                    help="写作类型（默认 auto：按首词是否为祈使式自动判定）")
    ap.add_argument("--dict", dest="dict_path", default="",
                    help="未核准词表 TSV 路径（默认用技能内置的 244 条节选）")
    ap.add_argument("--no-dictionary", action="store_true", help="跳过未核准词检查")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="只输出评分")
    ap.add_argument("--strict", action="store_true", help="有 hard 级问题则退出码 1")
    args = ap.parse_args()

    if args.no_dictionary:
        unapproved = {}
    else:
        p = Path(args.dict_path) if args.dict_path else \
            Path(__file__).resolve().parent.parent / "assets" / "ste-unapproved-words.tsv"
        unapproved = load_unapproved(p)
        if not unapproved and not args.quiet and not args.json:
            print(f"[warn] 未找到未核准词表：{p}（未核准词检查已跳过）", file=sys.stderr)

    hard_total = 0
    for target in args.files:
        try:
            raw = sys.stdin.read() if target == "-" else Path(target).read_text(
                encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"无法读取 {target}: {e}", file=sys.stderr)
            continue
        text = strip_noise(raw)
        st = Stats()
        check_document(text, st, args.mode, unapproved)
        hard_total += sum(1 for f in st.findings if f.severity == "hard")

        if args.json:
            print(render_json(target, st))
        elif args.quiet:
            print(f"{target}: {score(st)}/100")
        else:
            print(render(target, st))
            print()

    if args.strict and hard_total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
