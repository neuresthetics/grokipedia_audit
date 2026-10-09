#!/usr/bin/env python3
"""Print catalog entries (definition, required conditions, look-alikes) so the
reviewer can check each condition before flagging. Usage: entry.py ID [ID ...]
Catalog location: $FALLACY_CATALOG (default /workspace/fallacy_catalog)."""
import json, os, sys
CAT = os.environ.get("FALLACY_CATALOG", "/workspace/fallacy_catalog")
d = {e["id"]: e for e in json.load(open(f"{CAT}/fallacies.json"))["entries"]}
for i in sys.argv[1:]:
    if i not in d:
        print("no such id:", i, "| close:", [k for k in d if i.split("-")[0] in k]); continue
    e = d[i]
    print("##", i, "|", e["name"], "| outside-text conditions:", e["outside_text_conditions"],
          "| text_detectable:", e["text_detectable"], "| related:", ",".join(e["related"]))
    print(" DEF", e["definition"])
    for k, c in enumerate(e["required_conditions"], 1): print(" ", k, c)
    for l in e["legitimate_lookalikes"]: print("  LOOK-ALIKE", l["text"])
