#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""卡片库只读体检（库级 lint）。只读不写：不修改、不移动、不删除任何文件。

检查项：
    orphans            孤岛卡：既无出链也无入链
    broken_links       断链：[[目标]] 找不到对应卡片（按文件名、标题、id 匹配）
    near_duplicates    近似重名：标题规范化后相同或高度相似
    stale_drafts       超期草稿：status: draft 且超过 --stale-days 天未更新
    missing_sources    有 YAML 头但 sources 为空
    unreviewed_ai      author 为 ai/external 却不是 draft（未经人审就升级）
    superseded_issues  status: superseded 但缺 superseded_by，或指向不存在的卡
另给出指标：卡片总数、各 status 数量、平均每卡连接数、孤岛比例、无 YAML 头卡数。

用法：
    python3 lint_vault.py <卡片目录> [选项]

选项：
    --json              输出 JSON
    --stale-days N      草稿超期天数（默认 30）
    --exclude GLOB      排除匹配的相对路径，可重复（如 --exclude 'raw/*' --exclude 'templates/*'）
    --similarity R      近似重名阈值 0–1（默认 0.9；卡片数 >3000 时只做精确规范化比对）
    --fail-on-issues    发现任何问题时退出码为 1（默认总是 0，体检只出报告）
    -h, --help          显示本说明

退出码：
    0  体检完成（未加 --fail-on-issues 时，无论是否有问题）
    1  加了 --fail-on-issues 且发现问题
    2  参数错误或目录不存在
"""

import argparse
import datetime as dt
import difflib
import fnmatch
import json
import os
import re
import sys

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"\]\(([^)\s]+\.md)\)")
PREFIX = re.compile(r"^(文献|闪念|结构|索引|项目|概念卡|观点卡|方法卡|行动卡|案例卡|金句卡)\s*[｜|:：]\s*")


def parse_frontmatter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    fm = {}
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return fm, "\n".join(lines[i + 1:])
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if m:
            fm[m.group(1)] = re.sub(r"\s+#.*$", "", m.group(2)).strip()
        elif line.startswith((" ", "\t", "-")) and fm:
            last = list(fm)[-1]
            fm[last] = (fm[last] + " " + line.strip()).strip()
    return None, text


def empty(v):
    return v is None or v.strip() in ("", "[]", "''", '""', "~", "null")


def norm(s):
    s = PREFIX.sub("", s.strip())
    s = s.lower()
    return re.sub(r"[\s\W_]+", "", s)


def parse_date(s):
    if not s:
        return None
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def load(root, excludes):
    cards = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".md") or fn.startswith("._") or fn.startswith("."):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            if any(fnmatch.fnmatch(rel, g) for g in excludes):
                continue
            try:
                with open(full, encoding="utf-8") as f:
                    text = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            fm, body = parse_frontmatter(text)
            title = None
            for line in body.split("\n"):
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            stem = os.path.splitext(fn)[0]
            links = [m.strip() for m in WIKILINK.findall(text)]
            links += [os.path.splitext(os.path.basename(m))[0] for m in MDLINK.findall(text)]
            cards.append({
                "path": rel, "stem": stem, "title": title or stem, "fm": fm,
                "links": links, "mtime": dt.date.fromtimestamp(os.path.getmtime(full)),
            })
    return cards


def lint(root, stale_days=30, excludes=(), similarity=0.9, today=None):
    today = today or dt.date.today()
    cards = load(root, excludes)
    index = {}
    for i, c in enumerate(cards):
        keys = {norm(c["stem"]), norm(c["title"])}
        if c["fm"] and c["fm"].get("id"):
            keys.add(norm(c["fm"]["id"]))
        for k in keys:
            if k:
                index.setdefault(k, set()).add(i)

    def resolve(target):
        return index.get(norm(target), set())

    inbound = [set() for _ in cards]
    outbound = [set() for _ in cards]
    broken = []
    for i, c in enumerate(cards):
        for t in c["links"]:
            hits = resolve(t) - {i}
            if not resolve(t):
                broken.append({"card": c["path"], "target": t})
            for j in hits:
                outbound[i].add(j)
                inbound[j].add(i)

    orphans = [c["path"] for i, c in enumerate(cards) if not inbound[i] and not outbound[i]]

    dups = []
    groups = {}
    for c in cards:
        groups.setdefault(norm(c["title"]), []).append(c["path"])
    for k, paths in groups.items():
        if k and len(paths) > 1:
            dups.append({"titles": [next(x["title"] for x in cards if x["path"] == p) for p in paths],
                         "cards": paths, "similarity": 1.0})
    if len(cards) <= 3000:
        normed = [(norm(c["title"]), c) for c in cards]
        for a in range(len(normed)):
            for b in range(a + 1, len(normed)):
                na, ca = normed[a]
                nb, cb = normed[b]
                if not na or not nb or na == nb:
                    continue
                r = difflib.SequenceMatcher(None, na, nb).ratio()
                if r >= similarity:
                    dups.append({"titles": [ca["title"], cb["title"]],
                                 "cards": [ca["path"], cb["path"]], "similarity": round(r, 2)})

    stale, missing_src, unreviewed_ai, superseded = [], [], [], []
    status_count = {}
    no_fm = 0
    for c in cards:
        fm = c["fm"]
        if fm is None:
            no_fm += 1
            status_count["(无 YAML 头)"] = status_count.get("(无 YAML 头)", 0) + 1
            continue
        st = fm.get("status", "").lower() or "(缺 status)"
        status_count[st] = status_count.get(st, 0) + 1
        author = fm.get("author", "").lower()
        if empty(fm.get("sources")):
            missing_src.append(c["path"])
        if author in ("ai", "external") and st != "draft":
            unreviewed_ai.append({"card": c["path"], "author": author, "status": st})
        if st == "draft":
            d = parse_date(fm.get("updated")) or parse_date(fm.get("imported")) or parse_date(fm.get("created")) or c["mtime"]
            age = (today - d).days
            if age > stale_days:
                stale.append({"card": c["path"], "days": age})
        if st == "superseded":
            sb = fm.get("superseded_by")
            if empty(sb):
                superseded.append({"card": c["path"], "problem": "缺 superseded_by"})
            else:
                targets = WIKILINK.findall(sb) or [sb.strip("[]\"' ")]
                if not any(resolve(t) for t in targets):
                    superseded.append({"card": c["path"], "problem": f"superseded_by 指向不存在的卡：{sb}"})

    n = len(cards)
    edges = sum(len(o) for o in outbound)
    metrics = {
        "cards": n,
        "status": status_count,
        "no_frontmatter": no_fm,
        "avg_links_per_card": round(2 * edges / n, 2) if n else 0,
        "orphan_ratio": round(len(orphans) / n, 3) if n else 0,
    }
    findings = {
        "orphans": orphans, "broken_links": broken, "near_duplicates": dups,
        "stale_drafts": stale, "missing_sources": missing_src,
        "unreviewed_ai": unreviewed_ai, "superseded_issues": superseded,
    }
    return {"root": os.path.abspath(root), "date": today.isoformat(),
            "metrics": metrics, "findings": findings,
            "issue_count": sum(len(v) for v in findings.values()),
            "note": "只读体检：本脚本不修改任何文件；处理方式由人决定"}


LABELS = {
    "orphans": "孤岛卡（无入链也无出链）",
    "broken_links": "断链",
    "near_duplicates": "近似重名",
    "stale_drafts": "超期草稿",
    "missing_sources": "缺 sources",
    "unreviewed_ai": "AI/外部卡未经人审就升级",
    "superseded_issues": "更替缺指向",
}


def fmt(item):
    if isinstance(item, str):
        return item
    if "target" in item:
        return f"{item['card']} → [[{item['target']}]]"
    if "titles" in item:
        return " ≈ ".join(item["titles"]) + f"（{item['similarity']}）：" + "，".join(item["cards"])
    if "days" in item:
        return f"{item['card']}（{item['days']} 天）"
    if "author" in item:
        return f"{item['card']}（author: {item['author']}, status: {item['status']}）"
    return f"{item['card']}：{item['problem']}"


def report(res):
    m = res["metrics"]
    print(f"卡片库体检 {res['date']}｜{res['root']}")
    print(f"卡片 {m['cards']}｜平均每卡连接 {m['avg_links_per_card']}｜孤岛比例 {m['orphan_ratio']:.1%}｜无 YAML 头 {m['no_frontmatter']}")
    print("状态分布：" + "，".join(f"{k} {v}" for k, v in sorted(m["status"].items())))
    for key, label in LABELS.items():
        items = res["findings"][key]
        print(f"\n[{label}] {len(items)}")
        for it in items[:50]:
            print("  - " + fmt(it))
        if len(items) > 50:
            print(f"  …另有 {len(items) - 50} 条（用 --json 查看全部）")
    print(f"\n合计 {res['issue_count']} 条线索。{res['note']}。")


def main(argv=None):
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("root", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--stale-days", type=int, default=30)
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--similarity", type=float, default=0.9)
    ap.add_argument("--fail-on-issues", action="store_true")
    ap.add_argument("--today", help=argparse.SUPPRESS)
    ap.add_argument("-h", "--help", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    if a.help:
        print(__doc__)
        return 0
    if not a.root or not os.path.isdir(a.root):
        print(__doc__ if not a.root else f"目录不存在：{a.root}", file=sys.stderr)
        return 2
    today = dt.date.fromisoformat(a.today) if a.today else None
    res = lint(a.root, a.stale_days, a.exclude, a.similarity, today)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        report(res)
    return 1 if (a.fail_on_issues and res["issue_count"]) else 0


if __name__ == "__main__":
    sys.exit(main())
