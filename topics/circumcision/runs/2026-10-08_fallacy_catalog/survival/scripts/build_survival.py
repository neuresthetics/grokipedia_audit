#!/usr/bin/env python3
"""Rebuild the 'what survived' scores from committed files. Run from anywhere:

    python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/survival/scripts/build_survival.py

Inputs (all committed):
  ../work/sentences_stage1.csv   stage 1: every prose sentence, its span, rule side, flag overlap, queue reason
                                 (rebuilt by stage1_candidates.py; deterministic)
  ../labels/model_labels.csv     the model's label for every sentence (scripts/label_queue.py, LABEL_PROMPT.md)
  ../../flags.csv, ../../reviewer2_flags.csv, ../../reviewer3_flags.csv   the three reviewers' flags
  ../../../../articles/<slug>/snapshots/2026-10-01.txt                    the snapshots

Writes (in survival/):
  argument_inventory.csv   one row per argument sentence (side pro or anti)
  survival_scores.csv      inventory + r1/r2/r3 hit, points_left, entry ids
  flag_sentence_map.csv    one row per (flag, sentence it overlaps), with conflict type
  conflicts.csv            the subset of flag_sentence_map where the flag's side differs from the inventory side
  sentence_labels.csv      all 13,199 sentences: model label and rule label (rule label for comparison only)
  summary.json             every number used in SURVIVORS.md, METHOD.md and the chart
  SURVIVORS.md             summary and the lists of flagged arguments (2, 1, 0 points left)
  SURVIVORS_3_points_<side>_<group>.md   the untouched arguments (3 points left), one file per side and group
"""
import csv, json, re, sys, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
SURV = HERE.parent
RUN = SURV.parent
sys.path.insert(0, str(HERE))
from sentences import text  # noqa: E402
from stage1_candidates import flag_spans  # noqa: E402

# a --partial build (labeling not finished) writes to work/preview/ so committed outputs are never overwritten
OUTD = SURV / "work" / "preview" if "--partial" in sys.argv else SURV
OUTD.mkdir(parents=True, exist_ok=True)
GROUPS = (("male", "Male circumcision articles"), ("FGM", "FGM articles"))
SIDE = {"P": "pro", "A": "anti", "N": "none"}


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def main():
    st = rd(SURV / "work" / "sentences_stage1.csv")
    ml = {(r["slug"], r["sentence_id"]): r["model_side"] for r in rd(SURV / "labels" / "model_labels.csv")}
    missing = [k for k in ((r["slug"], r["sentence_id"]) for r in st) if k not in ml]
    if missing and "--partial" not in sys.argv:
        sys.exit(f"{len(missing)} sentences have no model label yet (run scripts/label_queue.py, or pass --partial)")
    if missing:
        st = [r for r in st if (r["slug"], r["sentence_id"]) in ml]
        print(f"PARTIAL BUILD: {len(missing)} sentences unlabeled and skipped; output in work/preview/", file=sys.stderr)

    # ---- verbatim check: every sentence must be the exact snapshot text at its span
    bad = 0
    for r in st:
        snap = text(r["slug"])
        exact = snap[int(r["start"]):int(r["end"])]
        if exact.split() != r["text"].split() or snap.find(exact) < 0:
            bad += 1
        r["verbatim"] = exact
    assert bad == 0, f"{bad} sentences not verbatim"

    # ---- side: the model label for every sentence; the rule label is kept for comparison only
    for r in st:
        m = ml[(r["slug"], r["sentence_id"])]
        r["side"] = "none" if m == "not_argument" else m
        r["label_method"] = "model"
    inv = [r for r in st if r["side"] in ("pro", "anti")]

    # ---- flags -> sentences
    flags = flag_spans()
    by_slug = collections.defaultdict(list)
    for r in st:
        by_slug[r["slug"]].append(r)
    fmap = []
    for f in flags:
        a, b = f["span"]
        for r in by_slug[f["slug"]]:
            if min(int(r["end"]), b) - max(int(r["start"]), a) > 0:
                if r["side"] == "none":
                    c = ("" if f["favors"] == "neutral" else
                         f"flag says {f['favors']}, inventory says not an argument (not scored)")
                elif f["favors"] == r["side"]:
                    c = ""
                elif f["favors"] == "neutral":
                    c = "neutral flag on " + ("an anti" if r["side"] == "anti" else "a pro") + " sentence"
                else:
                    c = f"flag says {f['favors']}, inventory says {r['side']}"
                fmap.append(dict(reviewer=f["rev"], flag_row=f["row"], slug=f["slug"], entry_id=f["entry_id"],
                                 favors=f["favors"], sentence_id=r["sentence_id"], inventory_side=r["side"],
                                 conflict=c, quote=f["quote"]))
    hits = collections.defaultdict(lambda: collections.defaultdict(set))
    for m in fmap:
        if m["inventory_side"] != "none":
            hits[(m["slug"], m["sentence_id"])][m["reviewer"]].add(m["entry_id"])
    for r in inv:
        h = hits[(r["slug"], r["sentence_id"])]
        for k in ("r1", "r2", "r3"):
            r[f"{k}_hit"] = int(bool(h.get(k)))
            r[f"{k}_entry_ids"] = "|".join(sorted(h.get(k, ())))
        r["points_left"] = 3 - r["r1_hit"] - r["r2_hit"] - r["r3_hit"]
        r["entry_ids"] = "|".join(sorted(set().union(*h.values()))) if h else ""

    # ---- outputs
    inv_rows = [dict(r, article=r["slug"], text=r["verbatim"], topic_group=r["group"]) for r in inv]
    wr(OUTD / "argument_inventory.csv", inv_rows,
       ["article", "sentence_id", "text", "side", "topic_group", "label_method", "rule_side"])
    wr(OUTD / "survival_scores.csv", inv_rows,
       ["article", "sentence_id", "text", "side", "topic_group", "label_method", "rule_side", "r1_hit", "r2_hit", "r3_hit",
        "points_left", "r1_entry_ids", "r2_entry_ids", "r3_entry_ids", "entry_ids"])
    mf = ["reviewer", "flag_row", "slug", "entry_id", "favors", "sentence_id", "inventory_side", "conflict", "quote"]
    wr(OUTD / "flag_sentence_map.csv", fmap, mf)
    conf = [m for m in fmap if m["conflict"]]
    wr(OUTD / "conflicts.csv", conf, mf)
    wr(OUTD / "sentence_labels.csv", [dict(r, article=r["slug"], topic_group=r["group"],
                                           model_side=r["side"] if r["side"] != "none" else "not_argument") for r in st],
       ["article", "sentence_id", "topic_group", "model_side", "rule_side", "label_method"])

    # ---- numbers
    S = dict(sentences=len(st), by_group={})
    for g, _ in GROUPS:
        gs = [r for r in st if r["group"] == g]
        d = dict(sentences=len(gs), articles=len({r["slug"] for r in gs}))
        for side in ("pro", "anti"):
            rows = [r for r in inv if r["group"] == g and r["side"] == side]
            pts = collections.Counter(r["points_left"] for r in rows)
            d[side] = dict(n=len(rows), points={str(p): pts.get(p, 0) for p in (3, 2, 1, 0)},
                           untouched_share=(pts.get(3, 0) / len(rows)) if rows else None,
                           by_method=dict(collections.Counter(r["label_method"] for r in rows)))
        S["by_group"][g] = d
    S["inventory"] = len(inv)
    S["label_method"] = dict(collections.Counter(r["label_method"] for r in inv))
    S["rule_side_counts"] = {f"{g}/{s}": n for (g, s), n in collections.Counter((r["group"], r["rule_side"]) for r in st).items()}
    S["model_side_counts"] = dict(collections.Counter(ml.values()))
    S["flags"] = dict(total=len(flags), by_reviewer=dict(collections.Counter(f["rev"] for f in flags)))
    S["flag_sentence_pairs"] = len(fmap)
    fl = collections.defaultdict(list)
    for m in fmap:
        fl[(m["reviewer"], m["flag_row"])].append(m)
    S["flags_on_argument"] = sum(any(m["inventory_side"] != "none" for m in v) for v in fl.values())
    S["flags_only_on_non_argument"] = sum(all(m["inventory_side"] == "none" for m in v) for v in fl.values())
    S["flags_spanning_2plus_sentences"] = sum(len(v) > 1 for v in fl.values())
    S["conflicts"] = dict(total=len(conf), by_type=dict(collections.Counter(m["conflict"] for m in conf)),
                          on_scored_sentences=sum(m["inventory_side"] != "none" for m in conf),
                          flags_involved=len({(m["reviewer"], m["flag_row"]) for m in conf}))
    S["non_argument_flags_by_favors"] = dict(collections.Counter(
        v[0]["favors"] for v in fl.values() if all(m["inventory_side"] == "none" for m in v)))
    S["flagged_sentences_dropped_as_non_argument"] = len({(m["slug"], m["sentence_id"]) for m in fmap if m["inventory_side"] == "none"})
    # rules vs model, every sentence (rule "none" = not_argument; rule "mixed" never matches)
    S["rules_vs_model"] = dict(n=len(st), same_label=sum(r["rule_side"] == r["side"] for r in st),
                               table={f"rule {a} / model {b}": n for (a, b), n in sorted(collections.Counter(
                                   (r["rule_side"], r["side"]) for r in st).items())})
    v1p = SURV / "work" / "v1_model_labels_sentence_only.csv"
    if v1p.exists():
        v1 = {(r["slug"], r["sentence_id"]): r["model_side"] for r in rd(v1p)}
        both = [(v1[k], r["side"]) for r in st if (k := (r["slug"], r["sentence_id"])) in v1]
        S["v1_vs_model"] = dict(n=len(both), same_label=sum(a == b for a, b in both))
    # consistency check by labeler (labels came from separate model sessions, split by article)
    lb = {(r["slug"], r["sentence_id"]): r["labeled_by"] for r in rd(SURV / "labels" / "model_labels.csv")}
    S["by_labeler"] = {}
    for k in sorted(set(lb.values())):
        rows = [r for r in st if lb[(r["slug"], r["sentence_id"])] == k]
        fl_ = [r for r in rows if r["flagged_by"]]
        S["by_labeler"][k] = dict(
            articles=len({r["slug"] for r in rows}), sentences=len(rows),
            pro=round(sum(r["side"] == "pro" for r in rows) / len(rows), 4),
            anti=round(sum(r["side"] == "anti" for r in rows) / len(rows), 4),
            not_argument=round(sum(r["side"] == "none" for r in rows) / len(rows), 4),
            rule_cue_share=round(sum(r["rule_side"] != "none" for r in rows) / len(rows), 4),
            same_as_rules=round(sum(r["rule_side"] == r["side"] for r in rows) / len(rows), 4),
            flagged_sentences=len(fl_), flagged_labeled_argument=sum(r["side"] != "none" for r in fl_))
    # sensitivity 2: what if the flagged sentences the inventory calls "not an argument" were counted, on the
    # side most of their non-neutral flags give (ties and neutral-only: left out)
    extra = collections.defaultdict(lambda: collections.defaultdict(set))
    fav = collections.defaultdict(collections.Counter)
    grp = {(r["slug"], r["sentence_id"]): r["group"] for r in st}
    for m in fmap:
        if m["inventory_side"] == "none":
            k = (m["slug"], m["sentence_id"])
            extra[k][m["reviewer"]].add(m["entry_id"])
            if m["favors"] != "neutral":
                fav[k][m["favors"]] += 1
    S["if_dropped_flagged_sentences_counted"] = {}
    for g, _ in GROUPS:
        S["if_dropped_flagged_sentences_counted"][g] = {}
        for side in ("pro", "anti"):
            add_k = [k for k in extra if grp[k] == g and fav[k] and fav[k].most_common(1)[0][0] == side
                     and len(set(fav[k].values())) == len(fav[k])]
            pts = collections.Counter(r["points_left"] for r in inv if r["group"] == g and r["side"] == side)
            for k in add_k:
                pts[3 - len(extra[k])] += 1
            n = sum(pts.values())
            S["if_dropped_flagged_sentences_counted"][g][side] = dict(
                added=len(add_k), n=n, points={str(p): pts.get(p, 0) for p in (3, 2, 1, 0)},
                untouched_share=round(pts.get(3, 0) / n, 4) if n else None)
    (OUTD / "summary.json").write_text(json.dumps(S, indent=2) + "\n", encoding="utf-8")
    write_md(S, inv)
    print(json.dumps(S, indent=2))


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "n/a"


def write_md(S, inv):
    L = ["# What survived the fallacy check (circumcision run, 2026-10-08)", "",
         "Each argument sentence starts with **3 points** and loses **1 point for each AI reviewer** (Reviewer 1, 2, 3) "
         "whose flag quote overlaps it. **Survival means \"not flagged\", not \"true\".** "
         "Flags are leads, not verdicts, and the reviewers were not blind (see the run README).", "",
         "**Who labeled the sides:** an AI model, not a person, labeled every prose sentence (pro, anti or not an "
         "argument), seeing only the article title and the sentences, never the reviewer flags. Instructions: "
         "[LABEL_PROMPT.md](LABEL_PROMPT.md). The labels came from 9 separate model sessions split by article, "
         "with no cross-checking between them, so borderline lines may differ from article to article. "
         "How it was done, and the limits: [METHOD.md](METHOD.md). Every statement below is copied from the snapshot "
         "by character position and checked by script.", "",
         "Pro = for the practice or playing down its harm. Anti = against it. In FGM articles, pro = defending FGM or "
         "playing down its harm.", "", "## Summary", "",
         "| Group | Side | Argument sentences | 3 points (untouched) | 2 | 1 | 0 | Share untouched |",
         "|---|---|---|---|---|---|---|---|"]
    for g, title in GROUPS:
        for side in ("pro", "anti"):
            d = S["by_group"][g][side]; p = d["points"]
            L.append(f"| {title} | {side} | {d['n']:,} | {p['3']:,} | {p['2']} | {p['1']} | {p['0']} | "
                     f"{pct(p['3'], d['n'])} |")
    for side in ("pro", "anti"):
        n = sum(S["by_group"][g][side]["n"] for g, _ in GROUPS)
        p = {k: sum(S["by_group"][g][side]["points"][k] for g, _ in GROUPS) for k in "3210"}
        L.append(f"| All 58 articles | {side} | {n:,} | {p['3']:,} | {p['2']} | {p['1']} | {p['0']} | {pct(p['3'], n)} |")
    L += ["", f"- Prose sentences read: {S['sentences']:,}. Argument sentences (pro or anti): {S['inventory']:,}. "
          "All other sentences were treated as descriptive or neutral and are not scored.",
          f"- Flags: {S['flags']['total']} rows from three reviewers (R1 {S['flags']['by_reviewer']['r1']}, "
          f"R2 {S['flags']['by_reviewer']['r2']}, R3 {S['flags']['by_reviewer']['r3']}). "
          f"{S['flags_on_argument']} touch at least one argument sentence; {S['flags_only_on_non_argument']} touch only "
          "sentences the inventory calls descriptive (logged, not scored).",
          f"- Side conflicts (the flag's side differs from the inventory label; the inventory label is kept): "
          f"{S['conflicts']['total']} flag-sentence pairs from {S['conflicts']['flags_involved']} flags, "
          f"{S['conflicts']['on_scored_sentences']} of them on scored sentences. By type: " + "; ".join(f"{k}: {v}" for k, v in S['conflicts']['by_type'].items()) + ". "
          "Listed in `conflicts.csv`.",
          f"- Rules vs model: the old rule script gave the same label as the model on "
          f"{S['rules_vs_model']['same_label']:,} of {S['rules_vs_model']['n']:,} sentences "
          f"({pct(S['rules_vs_model']['same_label'], S['rules_vs_model']['n'])}). The rule label is kept in "
          "`sentence_labels.csv` for comparison only.", ""]
    ent = lambda r: "; ".join(f"R{k[1]}: {r[k + '_entry_ids']}" for k in ("r1", "r2", "r3") if r[k + "_entry_ids"])  # noqa: E731
    for side in ("pro", "anti"):
        L += [f"## {side.capitalize()} arguments", ""]
        for g, title in GROUPS:
            rows = [r for r in inv if r["group"] == g and r["side"] == side]
            L += [f"### {title}: {side} ({len(rows):,} sentences)", ""]
            for pts in (2, 1, 0):
                sel = sorted((r for r in rows if r["points_left"] == pts), key=lambda r: (r["slug"], r["sentence_id"]))
                lab = {2: "2 points left (flagged by one reviewer)", 1: "1 point left (flagged by two reviewers)",
                       0: "0 points left (flagged by all three reviewers)"}[pts]
                L += [f"#### {lab}: {len(sel)}", ""]
                for r in sel:
                    L.append(f"- **{r['slug']}** `{r['sentence_id']}` ({ent(r)}): {r['verbatim']}")
                L.append("")
            n3 = sum(r["points_left"] == 3 for r in rows)
            fn = f"SURVIVORS_3_points_{side}_{g}.md"
            L += [f"#### 3 points left (no reviewer flagged it): {n3:,}", "",
                  f"Listed in full in [{fn}]({fn}) (a separate file, so each file stays small enough to display "
                  "on GitHub).", ""]
    (OUTD / "SURVIVORS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for side in ("pro", "anti"):
        for g, title in GROUPS:
            sel = sorted((r for r in inv if r["group"] == g and r["side"] == side and r["points_left"] == 3),
                         key=lambda r: (r["slug"], r["sentence_id"]))
            M = [f"# {title}: {side} arguments with all 3 points left ({len(sel):,})", "",
                 "Part of [SURVIVORS.md](SURVIVORS.md). Kept 3 points = no AI reviewer flagged the sentence; it does "
                 "not mean the sentence is true or well argued. Each statement is copied from the 2026-10-01 snapshot "
                 "by character position and checked by script. Sides were labeled by an AI model, not a person.", ""]
            for r in sel:
                M.append(f"- **{r['slug']}** `{r['sentence_id']}`: {r['verbatim']}")
            (OUTD / f"SURVIVORS_3_points_{side}_{g}.md").write_text("\n".join(M) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
