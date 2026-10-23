#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_plain_language.py — R1 受控文字机械自检（中英双语）

用途
    对写好的文字做受控语言（ASD-STE100 风格 / 中文受控写法）的机械体检。
    它只做统计与模式匹配，不做语义判断。输出的是线索，不是判决。

用法
    python3 check_plain_language.py draft.md
    python3 check_plain_language.py *.md --quiet
    cat draft.md | python3 check_plain_language.py -
    python3 check_plain_language.py draft.md --json
    python3 check_plain_language.py draft.md --strict      # 有严重问题则退出码 1

检查项
    长句 / 一句多事（句长超限）
    被动语态（英：be + 过去分词；中：被 / 所 / 由……所）
    名词化（中：进行/加以/予以/作出/实施 + 动词；英：-tion/-ment/-ance/-ity 密度）
    进行时 -ing（英）
    名词簇过长（英：连续名词 ≥ 4 个）
    "的"链过长（中：一句里 的 过多，或连续定语嵌套）
    冗余副词 / 套话（中：实际上、需要注意的是…；英：very、it should be noted…）
    同义漂移（同一概念换词，检查内置的高频同义组）
    段长超限（一段超过 5-6 句）

局限
    不判断是否说清了、不判断技术正确性、不处理代码块（会被跳过）。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- 常量

CN_CHAR = re.compile(r"[\u4e00-\u9fff]")
CJK_PUNCT = "。！？；!?;"

# 句子切分：中文句末标点 / 英文句末标点
SENT_SPLIT = re.compile(r"(?<=[。！？；!?;])|(?<=[.!?])\s+")

# 中文长句阈值
CN_MAX_STATEMENT = 30   # 陈述句字数上限
CN_MAX_STEP = 20        # 步骤句字数上限
CN_MAX_PARAGRAPH_SENT = 5

# 英文长句阈值
EN_MAX_SOFT = 30
EN_MAX_HARD = 25

CN_REDUNDANT = [
    "实际上", "其实", "需要注意的是", "众所周知", "在一定程度上", "总的来说",
    "基本上", "相对来说", "可以说", "毫无疑问", "显而易见", "非常", "极其",
    "十分", "相当", "多多少少", "众所周知的是",
]

EN_REDUNDANT = [
    r"\bvery\b", r"\breally\b", r"\bquite\b", r"\bsomewhat\b", r"\bactually\b",
    r"\bbasically\b", r"\bobviously\b", r"\bclearly\b", r"\bof course\b",
    r"it should be noted", r"it is important to note", r"needless to say",
    r"as we all know", r"in order to",
]

CN_NOMINAL = re.compile(r"(进行|加以|予以|作出|做出|开展|实施|从事)([^\s，。；！？、]{1,4})")
CN_PASSIVE = re.compile(r"被[^\s，。；！？]{1,4}|所[^\s，。；！？]{0,4}|由[^，。；]{1,8}所")

EN_PASSIVE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ed|known|done|made|given|taken|"
    r"seen|shown|found|held|kept|left|put|set|written|built|sent|read|chosen)\b",
    re.I,
)
EN_ING = re.compile(r"\b(\w{4,}ing)\b", re.I)
EN_ING_STOP = {
    "during", "thing", "things", "nothing", "something", "anything", "everything",
    "string", "strings", "ring", "king", "bring", "spring", "ceiling", "engineering",
    "learning", "training", "testing", "modeling", "modelling", "mapping", "embedding",
    "packaging", "sampling", "clustering", "conditioning", "encoding", "decoding",
    "heading", "heading", "setting", "warning", "meaning", "meeting", "opening",
}
EN_NOMINAL = re.compile(r"\b\w{4,}(?:tion|sion|ment|ance|ence|ity|ness)\b", re.I)
EN_WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

# 同义漂移检查：同一组里出现两种以上就提示统一
SYNONYM_GROUPS = [
    ["图片", "图像", "图幅", "图示", "图片"],
    ["算法", "方法", "模型", "方案"],
    ["用户", "客户", "使用者"],
    ["速度", "速率"],
    ["准确率", "精度", "精确度"],
    ["训练", "学习", "拟合"],
    ["问题", "课题", "议题"],
]

STEP_LINE = re.compile(r"^\s*(?:\d+[.、)]|[-*+]\s|\u2022)")


# ---------------------------------------------------------------- 数据结构

@dataclass
class Finding:
    line: int
    kind: str
    detail: str
    text: str = ""
    severity: str = "warn"   # info | warn | hard


@dataclass
class Stats:
    sentences: int = 0
    cn_sentences: int = 0
    total_cn_chars: int = 0
    long_sentences: int = 0
    passive: int = 0
    nominal: int = 0
    ing: int = 0
    de_chain: int = 0
    redundant: int = 0
    noun_cluster: int = 0
    long_paragraphs: int = 0
    words: int = 0
    en_sentences: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def cn_avg_len(self) -> float:
        return self.total_cn_chars / self.cn_sentences if self.cn_sentences else 0.0


# ---------------------------------------------------------------- 预处理

def strip_noise(text: str) -> str:
    """去掉代码块与行内代码，避免误报。"""
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "CODE", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "IMG", text)     # 图片
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)    # 链接保文字
    text = re.sub(r"^\s*\|.*\|\s*$", "", text, flags=re.M)  # 表格行
    return text


def split_sentences(line: str):
    parts = [p.strip() for p in SENT_SPLIT.split(line) if p and p.strip()]
    return parts


def cn_len(s: str) -> int:
    """中文句长：汉字数 + 英文词数。"""
    return len(CN_CHAR.findall(s)) + len(EN_WORD.findall(s))


# ---------------------------------------------------------------- 检查逻辑

def check_line(line_no: int, line: str, st: Stats, *, mode: str) -> None:
    """mode: 'statement' | 'step'"""
    sentences = split_sentences(line)
    if not sentences:
        return

    for sent in sentences:
        has_cn = bool(CN_CHAR.search(sent))
        length = cn_len(sent)

        if has_cn:
            st.sentences += 1
            st.cn_sentences += 1
            st.total_cn_chars += length
            limit = CN_MAX_STEP if mode == "step" else CN_MAX_STATEMENT
            if length > limit:
                st.long_sentences += 1
                st.findings.append(Finding(
                    line_no, "长句", f"{length} 字 > 上限 {limit} 字", sent, "hard"))
            # 的链
            de = sent.count("的")
            if de >= 4:
                st.de_chain += 1
                st.findings.append(Finding(
                    line_no, "的链过长", f"一句出现 {de} 个「的」", sent))
            elif re.search(r"的[^\s，。；、]{0,8}的[^\s，。；、]{0,8}的", sent):
                st.de_chain += 1
                st.findings.append(Finding(
                    line_no, "的链过长", "连续三层定语嵌套", sent))
            # 被动
            for m in CN_PASSIVE.finditer(sent):
                st.passive += 1
                st.findings.append(Finding(line_no, "被动语态", m.group(0), sent))
            # 名词化
            for m in CN_NOMINAL.finditer(sent):
                verb = m.group(2).strip("的了着过时地得个一之其")
                if not verb:
                    continue
                st.nominal += 1
                st.findings.append(Finding(
                    line_no, "名词化", f"{m.group(0)} → 直接用动词「{verb}」", sent))
            # 冗余
            for w in CN_REDUNDANT:
                if w in sent:
                    st.redundant += 1
                    st.findings.append(Finding(line_no, "冗余词", w, sent, "info"))
        else:
            words = EN_WORD.findall(sent)
            if not words:
                continue
            st.sentences += 1
            st.en_sentences += 1
            st.words += len(words)
            if len(words) > EN_MAX_SOFT:
                st.long_sentences += 1
                sev = "hard" if len(words) > EN_MAX_HARD else "warn"
                st.findings.append(Finding(
                    line_no, "long sentence", f"{len(words)} words > {EN_MAX_SOFT}", sent, sev))
            for m in EN_PASSIVE.finditer(sent):
                st.passive += 1
                st.findings.append(Finding(line_no, "passive voice", m.group(0), sent))
            for m in EN_ING.finditer(sent):
                if m.group(1).lower() in EN_ING_STOP:
                    continue
                st.ing += 1
                st.findings.append(Finding(
                    line_no, "-ing form", m.group(1), sent, "info"))
            for m in EN_NOMINAL.finditer(sent):
                st.nominal += 1
                st.findings.append(Finding(
                    line_no, "nominalisation", m.group(0), sent, "info"))
            for pat in EN_REDUNDANT:
                m = re.search(pat, sent, re.I)
                if m:
                    st.redundant += 1
                    st.findings.append(Finding(line_no, "filler", m.group(0), sent, "info"))
            # 名词簇
            for m in re.finditer(r"(?:\b[A-Za-z][\w-]*\b[ \t]+){3,}\b[A-Za-z][\w-]*\b", sent):
                chunk = m.group(0).split()
                if len(chunk) >= 4 and not any(w.lower() in
                        ("the", "a", "an", "of", "to", "in", "on", "for", "and", "or", "is", "are", "was", "were")
                        for w in chunk):
                    st.noun_cluster += 1
                    st.findings.append(Finding(
                        line_no, "noun cluster", " ".join(chunk), sent, "info"))


SENT_END = "。！？；!?;：:"


def iter_blocks(text: str):
    """把软换行的段落合并成逻辑块。返回 [(起始行号, 合并后的文本, 是否步骤块)]。

    markdown 里一段常被硬折行，直接逐行检查会把一句话切碎，导致长句、"的"链等
    统计失真。这里先还原逻辑块，再检查。
    """
    blocks: list[tuple[int, str, bool]] = []
    buf: list[str] = []
    start = 0
    is_step = False

    def flush() -> None:
        nonlocal buf
        if buf:
            blocks.append((start, "".join(buf), is_step))
            buf = []

    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("#") or line.startswith(">"):
            flush()
            continue

        step = bool(STEP_LINE.match(line))
        if not buf:
            start, is_step = i, step
        elif step or is_step:
            # 步骤块一行一步，不合并
            flush()
            start, is_step = i, step

        buf.append(line)
        # 句末标点收尾，或本行是步骤 → 收块
        if line[-1] in SENT_END or step:
            flush()

    flush()
    return blocks


def check_document(text: str, st: Stats) -> None:
    """逐块检查 + 段长检查 + 同义漂移。"""
    for line_no, block, is_step in iter_blocks(text):
        mode = "step" if is_step else "statement"
        check_line(line_no, block, st, mode=mode)
        if not is_step and len(split_sentences(block)) > CN_MAX_PARAGRAPH_SENT:
            st.long_paragraphs += 1
            st.findings.append(Finding(
                line_no, "段过长",
                f"该段 {len(split_sentences(block))} 句 > {CN_MAX_PARAGRAPH_SENT} 句"))

    # 同义漂移
    for group in SYNONYM_GROUPS:
        found = [w for w in dict.fromkeys(group) if w in text]
        if len(found) >= 2:
            st.findings.append(Finding(
                0, "同义漂移", "、".join(found), "同一概念请统一用词"))


# ---------------------------------------------------------------- 报告

def score(st: Stats) -> int:
    if not st.sentences:
        return 100
    s = 100.0
    s -= 60 * (st.long_sentences / st.sentences)
    s -= 45 * (st.passive / st.sentences)
    s -= 30 * (st.nominal / st.sentences)
    s -= 15 * (st.ing / st.sentences)
    s -= 25 * (st.de_chain / st.sentences)
    s -= 20 * (st.redundant / st.sentences)
    s -= 15 * (st.noun_cluster / st.sentences)
    s -= 10 * (st.long_paragraphs)
    return max(0, min(100, round(s)))


def render_report(path: str, st: Stats, max_items: int = 40) -> str:
    out = []
    out.append(f"== R1 受控文字体检 · {path} ==")
    out.append("")
    if not st.findings:
        out.append("  未发现问题。可以交付。")
    else:
        # 按类型聚合，按严重度排序
        order = {"hard": 0, "warn": 1, "info": 2}
        items = sorted(st.findings, key=lambda f: (order[f.severity], f.line))
        out.append(f"  命中 {len(items)} 条：")
        for f in items[:max_items]:
            loc = f"L{f.line}" if f.line else "--"
            out.append(f"  [{f.kind:<14}] {loc:<6} {f.detail}")
            if f.text:
                t = f.text if len(f.text) <= 56 else f.text[:56] + "…"
                out.append(f"  {'':<18}↳ {t}")
        if len(items) > max_items:
            out.append(f"  … 还有 {len(items) - max_items} 条，用 --json 取全量")
    out.append("")
    out.append("  统计：")
    out.append(f"    句数 {st.sentences}（中文 {st.cn_sentences} / 英文 {st.en_sentences}）"
               f" · 中文平均句长 {st.cn_avg_len:.1f} 字")
    out.append(f"    长句 {st.long_sentences} · 被动 {st.passive} · 名词化 {st.nominal}"
               f" · -ing {st.ing} · 的链 {st.de_chain}")
    out.append(f"    冗余词 {st.redundant} · 名词簇 {st.noun_cluster} · 长段 {st.long_paragraphs}")
    out.append("")
    sc = score(st)
    grade = "优" if sc >= 85 else ("良" if sc >= 70 else ("及格" if sc >= 55 else "需重写"))
    out.append(f"  评分 {sc}/100（{grade}）")
    out.append("")
    out.append("  说明：这是机械统计，不判断语义。评分低不代表写得差，")
    out.append("        只代表「读者需要重读」的风险高。")
    return "\n".join(out)


def render_json(path: str, st: Stats) -> str:
    return json.dumps({
        "file": path,
        "score": score(st),
        "stats": {
            "sentences": st.sentences,
            "cn_sentences": st.cn_sentences,
            "en_sentences": st.en_sentences,
            "cn_avg_len": round(st.cn_avg_len, 2),
            "long_sentences": st.long_sentences,
            "passive": st.passive,
            "nominal": st.nominal,
            "ing": st.ing,
            "de_chain": st.de_chain,
            "redundant": st.redundant,
            "noun_cluster": st.noun_cluster,
            "long_paragraphs": st.long_paragraphs,
        },
        "findings": [
            {"line": f.line, "kind": f.kind, "severity": f.severity,
             "detail": f.detail, "text": f.text}
            for f in st.findings
        ],
    }, ensure_ascii=False, indent=2)


def load_text(target: str) -> str:
    if target == "-":
        return sys.stdin.read()
    return Path(target).read_text(encoding="utf-8", errors="replace")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="R1 受控文字机械自检（中英双语）",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="待检查的文件，或 - 表示读 stdin")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--quiet", action="store_true", help="只输出评分")
    ap.add_argument("--strict", action="store_true", help="有 hard 级问题则退出码 1")
    args = ap.parse_args()

    worst = 0
    hard_total = 0
    for target in args.files:
        try:
            text = strip_noise(load_text(target))
        except OSError as e:
            print(f"无法读取 {target}: {e}", file=sys.stderr)
            worst = max(worst, 2)
            continue
        st = Stats()
        check_document(text, st)
        hard_total += sum(1 for f in st.findings if f.severity == "hard")

        if args.json:
            print(render_json(target, st))
        elif args.quiet:
            print(f"{target}: {score(st)}/100")
        else:
            print(render_report(target, st))
            print()

    if args.strict and hard_total:
        return 1
    return worst


if __name__ == "__main__":
    sys.exit(main())
