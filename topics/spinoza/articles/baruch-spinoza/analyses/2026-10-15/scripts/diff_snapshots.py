#!/usr/bin/env python3
"""Sentence-level diff of two grokaudit claims.csv files (+ sources.csv).
Usage: diff_snapshots.py OLD_claims OLD_sources NEW_claims NEW_sources OUT.md"""
import csv, sys, difflib
oc, os_, nc, ns, out = sys.argv[1:6]
ld = lambda p: list(csv.DictReader(open(p, encoding="utf-8")))
O, N = ld(oc), ld(nc); OS, NS = ld(os_), ld(ns)
ot = [r["text"] for r in O]; nt = [r["text"] for r in N]
sm = difflib.SequenceMatcher(None, ot, nt, autojunk=False)
L = ["# DIFF: Baruch Spinoza snapshot 2026-10-01 vs 2026-10-15", "",
     "Made by `scripts/diff_snapshots.py` (Python difflib over sentence lists from `grokaudit.py parse`). Text is verbatim.", ""]
ch = []; same = 0; cite_changes = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        same += i2 - i1
        for a, b in zip(O[i1:i2], N[j1:j2]):
            if a["cites"] != b["cites"]: cite_changes.append((a, b))
    else: ch.append((tag, O[i1:i2], N[j1:j2]))
L += [f"- Sentences: old {len(O)}, new {len(N)}; identical text {same}; changed blocks {len(ch)}.",
      f"- Sources listed: old {len(OS)}, new {len(NS)}.",
      f"- Identical sentences whose citation numbers changed: {len(cite_changes)}.", ""]
# source list diff
ou = [s["url"] for s in OS]; nu = [s["url"] for s in NS]
L += ["## Source list changes", ""]
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ou, nu, autojunk=False).get_opcodes():
    if tag == "equal": continue
    for s in OS[i1:i2]: L.append(f"- removed old #{s['n']}: {s['title']} <{s['url']}>")
    for s in NS[j1:j2]: L.append(f"- added new #{s['n']}: {s['title']} <{s['url']}>")
L += ["", "## Changed sentences", ""]
for tag, a, b in ch:
    L.append(f"### {tag}: old {','.join(r['claim_id'] for r in a) or '-'} -> new {','.join(r['claim_id'] for r in b) or '-'}"); L.append("")
    for r in a: L.append(f"- OLD [{r['cites']}]: {r['text']}")
    for r in b: L.append(f"- NEW [{r['cites']}]: {r['text']}")
    L.append("")
L += ["## Same text, citation numbers changed", ""]
from collections import Counter
deltas = Counter()
for a, b in cite_changes:
    L.append(f"- {a['claim_id']}->{b['claim_id']}: [{a['cites']}] -> [{b['cites']}]")
    try:
        for x, y in zip(a["cites"].split(), b["cites"].split()): deltas[int(y)-int(x)] += 1
    except ValueError: pass
L += ["", f"Per-marker shift counts (new minus old): {dict(deltas)}", ""]
open(out, "w", encoding="utf-8").write("\n".join(L)); print("\n".join(L[:12]))
