#!/usr/bin/env python3
"""Compare two fallacy-flag files. Checks every passage is a verbatim substring of the article
sentence and every entry_id exists in the catalog; writes a per-passage comparison and prints counts.
Usage: fallacy_compare.py claims.csv fallacies.json R1.csv R2.csv out.csv"""
import csv, json, sys
claims = {r["claim_id"]: r["text"] for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"))}
ids = {e["id"] for e in json.load(open(sys.argv[2]))["entries"]}
def load(p):
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    for r in rows:
        assert r["passage"] in claims[r["claim_id"]], ("passage not verbatim", r["claim_id"])
        assert r["entry_id"] in ids, ("unknown entry", r["entry_id"])
    return {r["claim_id"]: r for r in rows}
a, b = load(sys.argv[3]), load(sys.argv[4])
w = csv.writer(open(sys.argv[5], "w", newline="", encoding="utf-8"))
w.writerow(["claim_id", "R1_entry", "R1_verdict", "R2_entry", "R2_verdict", "status"])
c = {}
for k in sorted(set(a) | set(b)):
    x, y = a.get(k), b.get(k)
    if x and y:
        st = "flagged the same passage, same entry" if x["entry_id"] == y["entry_id"] else "flagged the same passage, label disputed"
        if x["verdict"] == y["verdict"] == "flag" and x["entry_id"] == y["entry_id"]: st += ", both flag"
    else: st = "R1 only" if x else "R2 only"
    c[st] = c.get(st, 0) + 1
    w.writerow([k, x and x["entry_id"], x and x["verdict"], y and y["entry_id"], y and y["verdict"], st])
print(f"R1 rows {len(a)}, R2 rows {len(b)}")
for k, v in sorted(c.items()): print(f"{v:3d}  {k}")
