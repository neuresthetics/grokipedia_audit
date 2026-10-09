#!/usr/bin/env python3
"""Stage 1 (script only). Writes ../work/sentences_stage1.csv: every prose sentence of the 58
snapshots (the run's own split, 13,199 sentences), its character span in the snapshot, its
rule-based side (rules.py) and which reviewers' flag quotes overlap it.

The rule side is kept for comparison only; the side used for scoring is the model label
(labels/model_labels.csv, written with label_queue.py following LABEL_PROMPT.md). The labeling model
must not open this file, because it shows the rule side and the flags.
"""
import csv, random, sys, pathlib
sys.dont_write_bytecode = True
from sentences import slugs, sentence_rows, group, RUN, text  # noqa: E402
from rules import script_side  # noqa: E402

sys.path.insert(0, str(RUN / "scripts"))
OUT = pathlib.Path(__file__).resolve().parents[1] / "work"
OUT.mkdir(exist_ok=True)


def read(name):
    with open(RUN / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def flag_spans():
    """Quote spans per reviewer, found exactly as scripts/compare_reviewers.py does."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("cmp", RUN / "scripts" / "compare_reviewers.py")
    cmp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cmp)
    out = []
    for tag, fn in (("r1", "flags.csv"), ("r2", "reviewer2_flags.csv"), ("r3", "reviewer3_flags.csv")):
        for i, r in enumerate(read(fn), 1):  # i = data row number in that csv (1 = first row under the header)
            out.append(dict(r, rev=tag, row=i, span=cmp.span(r["slug"], r["quote"])))
    return out


def main():
    flags = flag_spans()
    rows = []
    for s in slugs():
        g = group(s)
        for sid, t, a, b in sentence_rows(s):
            side, pc, ac, neg = script_side(t, g)
            hit = sorted({f["rev"] for f in flags if f["slug"] == s and f["span"]
                          and min(b, f["span"][1]) - max(a, f["span"][0]) > 0})
            rows.append(dict(slug=s, sentence_id=sid, group=g, start=a, end=b, rule_side=side,
                             pro_cues="|".join(pc), anti_cues="|".join(ac), negated=neg,
                             flagged_by="|".join(hit), text=t))
    with open(OUT / "sentences_stage1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    unm = [f for f in flags if not f["span"]]
    nos = [f for f in flags if f["span"] and not any(r["slug"] == f["slug"] and min(r["end"], f["span"][1]) -
                                                     max(r["start"], f["span"][0]) > 0 for r in rows)]
    import collections
    print("sentences", len(rows), collections.Counter((r["group"], r["rule_side"]) for r in rows))
    print("flags", len(flags), "unlocatable", len(unm), "not on any prose sentence", len(nos))
    for f in nos: print("  ", f["rev"], f["slug"], f["quote"][:80])


if __name__ == "__main__":
    main()
