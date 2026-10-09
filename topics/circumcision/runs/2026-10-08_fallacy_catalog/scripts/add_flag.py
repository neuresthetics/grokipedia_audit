#!/usr/bin/env python3
"""Record flags as the reviewer goes. Reads a JSON list on stdin:
  [{"slug", "quote", "id", "reason", "favors", "conf", "verdict"}]
favors: pro | anti | neutral (which side of the topic the faulty reasoning helps)
conf: high | medium | low;  verdict: flag | possible issue (default flag)
A row is accepted only if the quote is an exact substring of the snapshot and
the id exists in the catalog; rejected rows go to failed_first_try.jsonl.
Accepted rows are appended to flags_raw.jsonl (next to this script)."""
import sys, json, os, pathlib
from split_units import snapshot_paths
HERE = pathlib.Path(__file__).resolve().parent
CAT = os.environ.get("FALLACY_CATALOG", "/workspace/fallacy_catalog")
cat = {e["id"]: e for e in json.load(open(f"{CAT}/fallacies.json"))["entries"]}
ok = open(HERE / "flags_raw.jsonl", "a"); bad = open(HERE / "failed_first_try.jsonl", "a")
for r in json.load(sys.stdin):
    t = snapshot_paths(r["slug"])[0].read_text(encoding="utf-8")
    err = []
    if r["quote"] not in t: err.append("QUOTE NOT FOUND")
    if r["id"] not in cat: err.append("BAD ID")
    if r["favors"] not in ("pro", "anti", "neutral"): err.append("BAD FAVORS")
    if r["conf"] not in ("high", "medium", "low"): err.append("BAD CONF")
    r.setdefault("verdict", "flag")
    if err:
        print("FAIL", err, r["slug"], r["quote"][:80]); bad.write(json.dumps({**r, "err": err}) + "\n")
    else:
        r["name"] = cat[r["id"]]["name"]; ok.write(json.dumps(r) + "\n"); print("ok", r["slug"], r["id"])
