#!/usr/bin/env python3
"""Offset probe on fetched source text. For each inline marker n in a cited sentence, compute the share
of the sentence's content words (4+ letters, not stopwords) found in the fetched text of list entry n+k,
for k in K. A marker 'wins' at k when that share is strictly highest among K. Writes per-marker rows.
Usage: offset_fulltext.py claims.csv CACHE_DIR n_sources out.csv"""
import csv, re, sys, glob, os
claims, cache, nsrc, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
K = [0, -1, -10]
STOP = set("that this with from were which their there have been they into also than such these those other only more most about after before while where when what whose under over between within without against through among upon would could should being".split())
def toks(s): return {w for w in re.findall(r"[a-z]{4,}", s.lower()) if w not in STOP}
src = {}
for f in glob.glob(os.path.join(cache, "ref*.txt")):
    n = int(re.search(r"ref(\d+)", f).group(1)); body = open(f, encoding="utf-8", errors="replace").read()
    if len(body) > 1500: src[n] = toks(body)  # skip stubs / error pages
w = csv.writer(open(out, "w", newline="", encoding="utf-8"))
w.writerow(["claim_id", "inline", "block"] + [f"share_k{k}" for k in K] + ["winner"])
for r in csv.DictReader(open(claims, encoding="utf-8")):
    ct = toks(r["text"])
    if len(ct) < 4: continue
    for n in [int(x) for x in r["cites"].split(";") if x.strip().isdigit()]:
        sh = {k: (len(ct & src[n + k]) / len(ct) if (n + k) in src else None) for k in K}
        if all(v is None for v in sh.values()): continue
        vals = {k: v for k, v in sh.items() if v is not None}
        top = max(vals.values()); win = [k for k, v in vals.items() if v == top]
        w.writerow([r["claim_id"], n, (n - 1) // 10 * 10 + 1] + ["" if sh[k] is None else f"{sh[k]:.3f}" for k in K] + [win[0] if len(win) == 1 else "tie"])
