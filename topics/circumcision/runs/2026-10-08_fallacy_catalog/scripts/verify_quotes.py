#!/usr/bin/env python3
"""Final check: every quote in flags_raw.jsonl must appear character-for-character
in its article's snapshot. Rows that fail are dropped and listed; passing rows
go to flags_verified.jsonl. Prints the counts."""
import json, pathlib
from split_units import snapshot_paths
HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in open(HERE / "flags_raw.jsonl")]
good, bad = [], []
for r in rows:
    t = snapshot_paths(r["slug"])[0].read_text(encoding="utf-8")
    (good if r["quote"] in t else bad).append(r)
for r in bad: print("DROPPED", r["slug"], "|", r["quote"][:100])
(HERE / "flags_verified.jsonl").write_text("".join(json.dumps(r) + "\n" for r in good))
print(f"checked {len(rows)}, passed {len(good)}, failed {len(bad)}")
