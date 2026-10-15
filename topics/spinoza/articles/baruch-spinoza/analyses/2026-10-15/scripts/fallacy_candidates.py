#!/usr/bin/env python3
"""Read 2 candidate screen: list sentences containing an inference or evaluation marker.
Usage: fallacy_candidates.py claims.csv out.csv"""
import csv, re, sys
MARK = r"\b(thus|therefore|hence|so that|underscor\w*|indicat\w*|suggest\w*|reflect\w*|render\w*|leading to|led to|because|since|due to|stemm\w*|caus\w*|contribut\w*|fuel\w*|demonstrat\w*|proves?|ensur\w*|prevent\w*|precludes?|entails?|implies|implying|akin to|compare\w*|parallel\w*|aligns?|aligning|influenc\w*|inspir\w*|scholars?|critics|recent|despite|rather than|essential|only)\b"
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
w = csv.writer(open(sys.argv[2], "w", newline="", encoding="utf-8"))
w.writerow(["claim_id", "section", "markers", "text"]); n = 0
for r in rows:
    m = sorted(set(x.lower() for x in re.findall(MARK, r["text"], re.I)))
    if m: w.writerow([r["claim_id"], r["section"], ";".join(m), r["text"]]); n += 1
print(n, "candidate sentences of", len(rows))
