#!/usr/bin/env python3
"""Turn flags_verified.jsonl into ../flags.csv and print the counts used in the
README (by verdict, side, confidence, fallacy and article)."""
import json, csv, pathlib, collections
from split_units import slugs
HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in open(HERE / "flags_verified.jsonl")]
rows.sort(key=lambda r: r["slug"])  # stable: keeps reading order inside an article
cols = ["slug", "quote", "entry_id", "entry_name", "reason", "favors", "confidence", "verdict"]
with open(HERE.parent / "flags.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(cols)
    for r in rows:
        w.writerow([r["slug"], r["quote"], r["id"], r["name"], r["reason"], r["favors"], r["conf"], r["verdict"]])
C = collections.Counter
print("total", len(rows))
for k in ("verdict", "favors", "conf", "id"):
    print(k, C(r[k] for r in rows).most_common())
by = C(r["slug"] for r in rows)
print("articles with a row:", len(by), "of", len(slugs()))
for s in slugs():
    sub = [r for r in rows if r["slug"] == s]
    print(f"{s},{len(sub)},{sum(r['favors']=='pro' for r in sub)},{sum(r['favors']=='anti' for r in sub)},{sum(r['favors']=='neutral' for r in sub)}")
