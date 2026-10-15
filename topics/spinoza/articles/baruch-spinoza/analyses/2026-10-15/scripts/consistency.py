#!/usr/bin/env python3
"""Consistency pass: for every row whose as-linked verdict is S or P, list the [n] numbers named in the
reason and the numbers the sentence actually links. A row is flagged when the reason's as-linked part names
no linked source (so the as-linked verdict may rest on another source). If the reason has an
"As linked:" segment, only that segment is checked. Usage: consistency.py verdicts.psv evidence.jsonl"""
import sys, json, re
verd, evid = sys.argv[1:3]
E = {json.loads(l)["claim_id"]: json.loads(l) for l in open(evid, encoding="utf-8")}
flag = 0
for i, l in enumerate(open(verd, encoding="utf-8")):
    if i == 0: continue
    p = l.rstrip("\n").split("|", 5); cid, v, r = p[0], p[1], p[5]
    if v not in "SP": continue
    linked = {c["linked"]["n"] for c in E[cid]["cites"]}
    seg = r.split("Intended:")[0] if "As linked:" in r else r
    named = {int(x) for x in re.findall(r"\[(\d+)\]", seg)}
    if not (named & linked):
        flag += 1; print(f"{cid}\t{v}\tlinked={sorted(linked)}\tnamed={sorted(named)}\t{r[:160]}")
print(f"{flag} S/P rows whose as-linked reasoning names no linked source")
