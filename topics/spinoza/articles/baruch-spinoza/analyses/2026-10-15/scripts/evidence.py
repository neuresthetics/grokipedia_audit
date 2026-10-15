#!/usr/bin/env python3
"""Retrieval aid for the claim check (not a verdict). For every sentence and every citation
marker n, pull the best-matching 50-word window from (a) the source as linked (list entry n)
and (b) the source it was most likely meant to cite under the observed numbering drift
(n=5 -> 153; 6..90 -> n-1; >=91 -> n-10; see OFFSET.md). Score = share of the sentence's
content words (5+ letters) found in the window. Also reports the best of k in {0,-1,-9,-10}.
Usage: evidence.py data/claims.csv data/sources.csv CACHE data/evidence.jsonl"""
import csv, json, sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../../../../../tools/grokaudit"))
from grokaudit import best_passages, _ftoks
claims, sources, cache, out = sys.argv[1:5]
S = {int(r["n"]): r for r in csv.DictReader(open(sources, encoding="utf-8"))}
TXT = {}
def text(n):
    if n not in TXT:
        p = os.path.join(cache, f"ref{n:03d}.txt")
        t = open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""
        TXT[n] = t if len(t) > 1500 else ""
    return TXT[n]
def intended(n):
    return 153 if n == 5 else n if n < 5 else n - 1 if n <= 90 else n - 10
def ev(claim, n):
    if n not in S: return {"n": n, "listed": False}
    t = text(n); bp = best_passages(claim, t, win=50) if t else []
    return {"n": n, "listed": True, "title": S[n]["title"], "url": S[n]["url"], "fetched": bool(t),
            "score": round(bp[0][0], 2) if bp else None, "passage": bp[0][1] if bp else ""}
with open(out, "w", encoding="utf-8") as f:
    for c in csv.DictReader(open(claims, encoding="utf-8")):
        rec = {"claim_id": c["claim_id"], "section": c["section"], "text": c["text"], "cites": []}
        for n in map(int, c["cites"].split()):
            ks = {}
            for k in (0, -1, -9, -10):
                m = n + k
                if m in S and text(m): ks[k] = round(best_passages(c["text"], text(m), win=50)[0][0], 2) if _ftoks(c["text"]) else 0
            rec["cites"].append({"marker": n, "linked": ev(c["text"], n), "intended": ev(c["text"], intended(n)),
                                 "k_scores": ks})
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
