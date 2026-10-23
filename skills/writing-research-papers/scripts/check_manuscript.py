#!/usr/bin/env python3
"""投稿前稿件自检脚本（writing-research-papers skill）

对英文/中英混排的论文稿件（.md / .txt / .tex 纯文本）做确定性机械检查，
输出 Markdown 报告。检查项提炼自 brittman(200+ 中国学生论文常见习惯)、
Ten Simple Rules、图灵学术「投稿零容错」清单、Silvia 文风原则。

用法:
    python3 check_manuscript.py manuscript.md
    python3 check_manuscript.py manuscript.docx.txt --max-abstract-words 250 --out report.md
    python3 check_manuscript.py paper.tex --json

注意: 本脚本只做机械可判定项，语义问题（论证、逻辑、创新性）需人工或
按 SKILL.md 的 references 逐项判断。
"""

import argparse
import json
import re
import sys
from collections import Counter

SECTION_PATTERNS = [
    ("Abstract", r"^\s*(?:\d+[\.\s]*)?(abstract|摘要)\b"),
    ("Introduction", r"^\s*(?:\d+[\.\s]*)?(introduction|引言|绪论)\b"),
    ("Related Work", r"^\s*(?:\d+[\.\s]*)?(related work|literature review|background|相关工作|文献综述|研究背景)\b"),
    ("Method", r"^\s*(?:\d+[\.\s]*)?(methods?|methodology|materials and methods|approach|方法|研究方法)\b"),
    ("Results", r"^\s*(?:\d+[\.\s]*)?(results?|experiments?|结果|实验结果)\b"),
    ("Discussion", r"^\s*(?:\d+[\.\s]*)?(discussion|讨论)\b"),
    ("Conclusion", r"^\s*(?:\d+[\.\s]*)?(conclusions?|结论)\b"),
    ("References", r"^\s*(?:\d+[\.\s]*)?(references|bibliography|参考文献)\b"),
]

FILLER_WORDS = [
    "very", "basically", "really", "quite", "extremely", "obviously",
    "clearly", "a lot of", "lots of", "kind of", "sort of", "actually",
]

WORDY_PHRASES = {
    "in order to": "to",
    "due to the fact that": "because",
    "it should be noted that": "(delete or state directly)",
    "it is worth mentioning that": "(delete)",
    "as we all know": "(delete — unsupported claim)",
    "with the rapid development of": "(delete cliché — state the specific change)",
    "plays an important role in": "(be specific about the role)",
    "and so on": "(be exhaustive or say 'etc.' only in informal text)",
    "in a word": "(delete)",
    "for the purpose of": "to / for",
    "in the case of": "for / with",
    "at the present time": "now",
    "a large number of": "many",
    "in spite of the fact that": "although",
}

HEDGES = ["may", "might", "could", "suggest", "suggests", "indicate", "indicates",
          "appear", "appears", "likely", "possibly", "seem", "seems", "tend", "tends",
          "approximately", "relatively", "arguably", "presumably"]

BE_VERBS = ["is", "are", "was", "were", "be", "been", "being", "am"]

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
ACRONYM_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,5})\b")
# 括号内需含小写字母才算"给出全称"，避免把裸缩写 "(DRL)" 误判为已定义
DEFINE_RE = re.compile(r"\((?=[^)]*[a-z])([A-Z][A-Za-z0-9/ ,\-]{2,60})\)")

COMMON_ACRONYM_STOP = {
    "I", "A", "OK", "AI", "US", "UK", "EU", "CA", "SI", "PDF", "DOI", "URL", "HTML",
    "HTTP", "FIG", "TABLE", "EQ", "PHD", "MBA", "CEO", "ID", "TV", "GPS", "CPU", "GPU",
    "RAM", "API", "JSON", "XML", "SQL", "CSV", "CD", "PM", "AM", "II", "III", "IV", "VI",
}


def normalize_heading(line):
    """Strip markdown markers / numbering so section patterns can match."""
    s = line.strip()
    s = re.sub(r"^[#>*\s]+", "", s)
    s = re.sub(r"^\d+(\.\d+)*[\.\s]+", "", s)
    s = re.sub(r"[*_:\s]+$", "", s)
    return s


def split_sections(text):
    """Split text into (section_name, body) pairs by heading lines."""
    sections, current, buf = [], "Preamble", []
    for raw in text.splitlines():
        norm = normalize_heading(raw)
        matched = None
        if norm and len(norm) < 40 and (raw.lstrip().startswith("#") or len(norm) < 30):
            for name, pat in SECTION_PATTERNS:
                if re.match(pat, norm, re.IGNORECASE):
                    matched = name
                    break
        if matched:
            sections.append((current, "\n".join(buf)))
            current, buf = matched, []
        else:
            buf.append(raw)
    sections.append((current, "\n".join(buf)))
    return [(n, b) for n, b in sections if b.strip()]


def words(text):
    return WORD_RE.findall(text)


def sentences(text):
    """Rough sentence splitter tolerant of abbreviations and citations."""
    protected = re.sub(r"\b(e\.g|i\.e|et al|Fig|Eq|Ref|No|vs|cf|approx)\.", r"\1<DOT>", text)
    parts = SENT_SPLIT.split(protected)
    return [p.replace("<DOT>", ".").strip() for p in parts if len(WORD_RE.findall(p)) > 2]


def check(text, args):
    report = {"summary": {}, "issues": []}
    secs = split_sections(text)
    body = text
    all_words = words(body)
    n_words = len(all_words)
    report["summary"]["word_count_en"] = n_words
    report["summary"]["char_count_cjk"] = len(CJK_RE.findall(body))
    report["summary"]["section_word_counts"] = {n: len(words(b)) for n, b in secs}

    def add(level, category, message, evidence=None):
        report["issues"].append(
            {"level": level, "category": category, "message": message, "evidence": evidence or []}
        )

    # --- 1. Abstract length ---
    for name, b in secs:
        if name == "Abstract" and "摘要" not in b:
            wc = len(words(b))
            if wc > args.max_abstract_words:
                add("P1", "结构", f"摘要 {wc} 词，超过 {args.max_abstract_words} 词上限（Ten Simple Rules: ≤250 词且自足）")
            elif wc < 80:
                add("P1", "结构", f"摘要仅 {wc} 词，可能缺少五要素（动机-问题-方法-结果-结论）之一")

    # --- 2. Section presence ---
    present = {n for n, _ in secs}
    for required in ["Abstract", "Introduction", "Method", "Results", "Conclusion"]:
        if required not in present and args.strict_imrad:
            add("P1", "结构", f"未检测到 {required} 章节（IMRaD 完整性检查）")

    # --- 3. Sentence length ---
    long_s, critical_s = [], []
    for s in sentences(text):
        w = len(words(s))
        if w >= 60:
            critical_s.append(f"({w} 词) {s[:140]}...")
        elif w >= 40:
            long_s.append(f"({w} 词) {s[:140]}...")
    if critical_s:
        add("P0", "句子", f"{len(critical_s)} 句超过 60 词（brittman: 中国学生第一顽疾，拆句）", critical_s[:5])
    if long_s:
        add("P1", "句子", f"{len(long_s)} 句在 40–59 词之间，建议拆分", long_s[:5])

    # --- 4. Filler words ---
    low = text.lower()
    filler_hits = [(w, low.count(" " + w + " ")) for w in FILLER_WORDS]
    filler_hits = [(w, c) for w, c in filler_hits if c > 0]
    if filler_hits:
        add("P1", "文风", "寄生强化词（删掉不损失信息）",
            [f"{w}: {c} 次" for w, c in sorted(filler_hits, key=lambda x: -x[1])])

    # --- 5. Wordy phrases ---
    wordy_hits = [(p, len(re.findall(re.escape(p), low))) for p in WORDY_PHRASES]
    wordy_hits = [(p, c) for p, c in wordy_hits if c > 0]
    if wordy_hits:
        add("P1", "文风", "冗长短语，可替换",
            [f"'{p}' ({c} 次) → {WORDY_PHRASES[p]}" for p, c in wordy_hits])

    # --- 6. be-verb density ---
    be_count = sum(low.count(" " + v + " ") for v in BE_VERBS)
    ratio = round(be_count / max(n_words, 1) * 100, 1)
    report["summary"]["be_verb_per_100w"] = ratio
    if ratio > 7:
        add("P1", "文风", f"be 动词密度 {ratio}/100 词偏高；Silvia 建议圈出所有 be 动词并把 1/3 换成实义动词")

    # --- 7. Hedging density ---
    hedge_count = sum(low.count(" " + h + " ") for h in HEDGES)
    hedge_ratio = round(hedge_count / max(n_words, 1) * 100, 2)
    report["summary"]["hedge_per_100w"] = hedge_ratio
    disc = " ".join(b for n, b in secs if n in ("Discussion", "Conclusion")).lower()
    disc_hedge = sum(disc.count(" " + h + " ") for h in HEDGES)
    if disc and len(words(disc)) > 150 and disc_hedge < 3:
        add("P1", "讨论", "讨论/结论部分 hedge 词极少（<3），推论可能过于绝对（may/might/suggest/indicate）")

    # --- 8. respectively / this paper vs this study ---
    resp = len(re.findall(r"\brespectively\b", low))
    if resp:
        bad = [s[:120] for s in sentences(text) if "respectively" in s.lower()
               and not re.search(r"respectively[,\s]*\.?\s*$", s.strip().lower())]
        if bad:
            add("P1", "用词", "'respectively' 未放在句末（brittman：应在句末且仅当顺序有意义时使用）",
                [b + "..." for b in bad[:3]])
    n_paper = len(re.findall(r"in this paper", low))
    n_study = len(re.findall(r"in this study", low))
    if n_paper and n_study:
        add("P2", "用词", f"'in this paper'({n_paper}) 与 'in this study'({n_study}) 混用；study=研究工作, paper=文章本身，全篇统一")

    # --- 9. Full-width / half-width, spacing, quotes ---
    cjk_punct = re.findall(r"[，。；：（）、“”]", text)
    if cjk_punct and n_words > 100:
        add("P1", "格式", f"英文稿中出现 {len(cjk_punct)} 个全角标点（投稿零容错：全半角统一）",
            [f"示例: {p}" for p in Counter(cjk_punct).most_common(5)])
    dbl_space = len(re.findall(r"[A-Za-z]  +[A-Za-z]", text))
    if dbl_space:
        add("P2", "格式", f"发现 {dbl_space} 处英文词语间多余空格")
    if re.search(r"\b\w+'\w+", text) and re.search(r"[\u2018\u2019]", text):
        add("P2", "格式", "直引号与弯引号混用，全稿统一")

    # --- 10. Acronym first-use ---
    defined = set()
    for m in DEFINE_RE.finditer(text):
        for a in ACRONYM_RE.findall(m.group(1)):
            defined.add(a)
    acr = [a for a in ACRONYM_RE.findall(text) if a not in COMMON_ACRONYM_STOP]
    counts = Counter(acr)
    undef = sorted([a for a, c in counts.items() if c >= 1 and a not in defined])
    if undef:
        add("P1", "格式", "缩写首次出现未给全称或未定义（投稿零容错）", undef[:12])

    # --- 11. Figure/table reference consistency ---
    style_flags = []
    if re.search(r"\bFig\.", text) and re.search(r"\bFigure\s+\d", text):
        style_flags.append("'Fig.' 与 'Figure' 混用")
    if re.search(r"\bTab\.", text) and re.search(r"\bTable\s+\d", text):
        style_flags.append("'Tab.' 与 'Table' 混用")
    if style_flags:
        add("P1", "格式", "图表引用形式不统一", style_flags)

    # --- 12. Nominalization density ---
    nom = len(re.findall(r"\b\w+(?:tion|ment|ance|ence|ency|ity|ness)\b", low))
    nom_ratio = round(nom / max(n_words, 1) * 100, 1)
    report["summary"]["nominalization_per_100w"] = nom_ratio
    if nom_ratio > 12:
        add("P2", "文风", f"名词化密度 {nom_ratio}/100 词偏高，部分可改回动词（'perform an analysis of' → 'analyze'）")

    # --- 13. Citation style mixing ---
    has_numeric = bool(re.search(r"\[\d+([,\-–]\s*\d+)*\]", text))
    has_author_date = bool(re.search(r"\([A-Z][A-Za-z\-]+(?:\s+et al\.?)?,?\s+(19|20)\d{2}", text))
    if has_numeric and has_author_date:
        add("P0", "引用", "同时出现数字引用与作者-年份引用，一篇论文只能用一种体例（Turabian）")

    # --- 14. Tense heuristics per section ---
    tense_notes = []
    for name, b in secs:
        bl = b.lower()
        past = len(re.findall(r"\b\w+ed\b", bl))
        pres = len(re.findall(r"\b(is|are|has|have|shows|show|suggest|suggests)\b", bl))
        if name == "Method" and past < pres:
            tense_notes.append("Methods 章过去时偏少（常规用过去时描述已完成的操作）")
        if name == "Results" and past < pres * 0.6:
            tense_notes.append("Results 章过去时偏少（报告已得结果用过去时）")
    if tense_notes:
        add("P2", "时态", "时态启发式提示（需人工确认）", tense_notes)

    return report


def render_markdown(report, path):
    s = report["summary"]
    lines = [f"# 稿件自检报告：{path}", ""]
    lines.append("## 概览")
    lines.append("")
    lines.append(f"- 英文词数：{s.get('word_count_en', 0)}")
    lines.append(f"- 中文字符数：{s.get('char_count_cjk', 0)}")
    lines.append(f"- be 动词密度：{s.get('be_verb_per_100w', 0)} / 100 词（建议 < 7）")
    lines.append(f"- hedge 词密度：{s.get('hedge_per_100w', 0)} / 100 词")
    lines.append(f"- 名词化密度：{s.get('nominalization_per_100w', 0)} / 100 词（建议 < 12）")
    lines.append("")
    swc = s.get("section_word_counts", {})
    if swc:
        lines.append("## 各章节词数")
        lines.append("")
        lines.append("| 章节 | 词数 |")
        lines.append("|------|------|")
        for k, v in swc.items():
            lines.append(f"| {k} | {v} |")
        lines.append("")
    issues = report["issues"]
    p0 = [i for i in issues if i["level"] == "P0"]
    p1 = [i for i in issues if i["level"] == "P1"]
    p2 = [i for i in issues if i["level"] == "P2"]
    lines.append(f"## 问题清单（P0 {len(p0)} · P1 {len(p1)} · P2 {len(p2)}）")
    lines.append("")
    if not issues:
        lines.append("机械检查未发现问题。仍需按 revision-checklist.md 做人工语义检查。")
    for level, items in (("P0 必改", p0), ("P1 建议改", p1), ("P2 提示", p2)):
        if not items:
            continue
        lines.append(f"### {level}")
        for it in items:
            lines.append(f"- **[{it['category']}]** {it['message']}")
            for ev in it["evidence"]:
                lines.append(f"  - {ev}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("机械检查不覆盖：论证是否成立、创新点是否清晰、图表是否服务贡献、")
    lines.append("文献是否读到原文。以上请按 SKILL.md 的 references 人工逐项核对。")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="投稿前稿件自检（机械可判定项）")
    ap.add_argument("manuscript", help="稿件路径（.md/.txt/.tex 等纯文本）")
    ap.add_argument("--out", help="报告输出路径（默认同目录 <name>.check.md）")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而非 Markdown")
    ap.add_argument("--max-abstract-words", type=int, default=250)
    ap.add_argument("--no-strict-imrad", dest="strict_imrad", action="store_false",
                    help="跳过 IMRaD 章节完整性检查（学位论文等适用）")
    args = ap.parse_args()

    try:
        with open(args.manuscript, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"无法读取稿件：{exc}", file=sys.stderr)
        return 2

    if len(WORD_RE.findall(text)) < 30 and len(CJK_RE.findall(text)) < 60:
        print("警告：文本过短，检查结果参考价值有限", file=sys.stderr)

    report = check(text, args)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    md = render_markdown(report, args.manuscript)
    out = args.out or re.sub(r"\.[^.]+$", "", args.manuscript) + ".check.md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(md)
    print(f"\n报告已保存：{out}")
    return 1 if any(i["level"] == "P0" for i in report["issues"]) else 0


if __name__ == "__main__":
    sys.exit(main())
