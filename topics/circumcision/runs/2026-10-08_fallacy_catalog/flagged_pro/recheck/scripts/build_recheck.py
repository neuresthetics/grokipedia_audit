#!/usr/bin/env python3
"""Step 6, pass 3: build the results of the fresh recheck (work/findings.csv, from recheck_queue.py).

    python3 .../flagged_pro/recheck/scripts/build_recheck.py            needs every queue item checked
    python3 .../flagged_pro/recheck/scripts/build_recheck.py --partial  progress only, prints counts, writes nothing

Scoring: each sentence loses 1 point per distinct catalog entry with verdict "flag" (possible_issue costs
nothing), starting from its points after pass 2, floor 0. Tier B sentences (already below 3 points) are not
dinged again for an entry that a step-5 reviewer already flagged on that sentence.
Writes recheck/findings.csv, recheck/points_by_pass.csv, recheck/summary.json, recheck/RECHECK.md.
Every quote is checked as an exact substring of the sentence and of the 2026-10-01 snapshot. Deterministic.
"""
import collections, csv, json, pathlib, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
RC = HERE.parent
FP = RC.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
REV = {"r1": "flags.csv", "r2": "reviewer2_flags.csv", "r3": "reviewer3_flags.csv"}


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)


def num(s):
    return int(s[1:])


def main():
    partial = "--partial" in sys.argv
    Q = rd(RC / "work" / "queue.csv")
    qby = {q["item"]: q for q in Q}
    F = collections.defaultdict(list)
    for r in rd(RC / "work" / "findings.csv") if (RC / "work" / "findings.csv").exists() else []:
        F[r["item"]].append(r)
    left = [q["item"] for q in Q if q["item"] not in F]
    if left and not partial:
        sys.exit(f"{len(left)} of {len(Q)} items not checked yet (first {left[:3]}); use --partial for progress")
    ok = set(json.load(open(RC / "catalog_ids_v0.6.1.json"))["text_detectable_ids"])
    sc = rd(RUN / "survival" / "survival_scores.csv")
    S = {(r["article"], r["sentence_id"]): r for r in sc}
    after2 = {(r["article"], r["sentence_id"]): int(r["points_after"])
              for r in rd(FP / "dependency" / "survivors_after_priors.csv")}
    prev = collections.defaultdict(set)  # entries already flagged by a step-5 reviewer on the sentence
    flags = {k: rd(RUN / fn) for k, fn in REV.items()}
    for m in rd(RUN / "survival" / "flag_sentence_map.csv"):
        prev[(m["slug"], m["sentence_id"])].add(flags[m["reviewer"]][int(m["flag_row"]) - 1]["entry_id"])
    p2 = collections.defaultdict(list)  # pass-2 links (survivor -> flagged sentence it depends on)
    for d in rd(FP / "dependency" / "dependencies.csv"):
        p2[(d["survivor_article"], d["survivor_id"])].append(f"{d['prior_article']} {d['prior_id']}")
    snaps = {}
    rows, pts3, dings = [], {}, {}
    for it in sorted(F):
        q = qby[it]; k = (q["article"], q["sentence_id"])
        if q["article"] not in snaps:
            snaps[q["article"]] = (SNAP / q["article"] / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
        counted = set()
        for r in F[it]:
            if r["verdict"] != "no_issue":
                assert r["entry_id"] in ok, (it, r["entry_id"])
                assert r["quote"] in S[k]["text"] and r["quote"] in snaps[q["article"]], f"{it}: quote not verbatim"
            c = r["verdict"] == "flag" and r["entry_id"] not in prev[k] if q["tier"] == "B" else r["verdict"] == "flag"
            if c:
                counted.add(r["entry_id"])
            earlier = "; ".join([f"step 5: {e}" for e in sorted(prev[k])] + [f"pass 2: depends on {x}" for x in p2[k]])
            rows.append(dict(item=it, tier=q["tier"], article=k[0], sentence_id=k[1], verdict=r["verdict"],
                             entry_id=r["entry_id"], quote=r["quote"], reason=r["reason"],
                             counted="yes" if c else "no", earlier_dings=earlier, checked_by=r["checked_by"]))
        dings[k] = len(counted)
        pts3[k] = max(0, after2[k] - len(counted))
    pro = sorted([r for r in sc if r["side"] == "pro" and r["topic_group"] == "male"],
                 key=lambda r: (r["article"], num(r["sentence_id"])))
    dist = lambda d: {str(p): sum(v == p for v in d) for p in (3, 2, 1, 0)}
    a2 = [after2.get((r["article"], r["sentence_id"]), 0) for r in pro]
    a3 = [pts3.get((r["article"], r["sentence_id"]), a2[i]) for i, r in enumerate(pro)]
    overlap = sorted({(r["article"], r["sentence_id"]) for r in rows if r["counted"] == "yes" and r["earlier_dings"]})
    a3_alt = [a2[i] if (r["article"], r["sentence_id"]) in overlap else a3[i] for i, r in enumerate(pro)]
    vc = collections.Counter(r["verdict"] for r in rows)
    ent = collections.Counter(r["entry_id"] for r in rows if r["counted"] == "yes")
    tierA = [q["item"] for q in Q if q["tier"] == "A"]
    Sm = dict(complete=not left, items=len(Q), checked=len(F), unchecked=len(left),
              tier_A_checked=sum(i in F for i in tierA), tier_A=len(tierA),
              lines=dict(vc), flags_counted=sum(ent.values()),
              sentences_dinged=sum(v > 0 for v in dings.values()),
              tier_A_dinged=sum(dings[(qby[i]["article"], qby[i]["sentence_id"])] > 0 for i in tierA if i in F),
              points_lost={str(n): sum(v == n for v in dings.values()) for n in (0, 1, 2, 3)},
              male_pro_points_left_step5=dist([int(r["points_left"]) for r in pro]),
              male_pro_points_left_after_pass2=dist(a2), male_pro_points_left_after_pass3=dist(a3),
              dinged_with_earlier_ding=[f"{a} {b}" for a, b in overlap],
              male_pro_points_left_after_pass3_without_those=dist(a3_alt),
              flags_not_counted_same_entry_as_step5=sum(r["verdict"] == "flag" and r["counted"] == "no" for r in rows),
              entries_counted=dict(sorted(ent.items(), key=lambda t: (-t[1], t[0]))),
              checked_by=dict(collections.Counter(v[0]["checked_by"] for v in F.values())))
    if partial:
        print(json.dumps(Sm, indent=1)); return
    wr(RC / "findings.csv", rows, list(rows[0]))
    out = [dict(article=r["article"], sentence_id=r["sentence_id"], points_step5=int(r["points_left"]),
                points_after_pass2=a2[i], points_after_pass3=a3[i],
                pass3_flags=dings.get((r["article"], r["sentence_id"]), 0)) for i, r in enumerate(pro)]
    wr(RC / "points_by_pass.csv", out, list(out[0]))
    json.dump(Sm, open(RC / "summary.json", "w"), indent=1)
    write_md(Sm, rows, S)
    print(json.dumps({k: Sm[k] for k in ("checked", "lines", "sentences_dinged", "male_pro_points_left_after_pass3")}))


def write_md(Sm, rows, S):
    s5, s2, s3 = (Sm[k] for k in ("male_pro_points_left_step5", "male_pro_points_left_after_pass2",
                                  "male_pro_points_left_after_pass3"))
    L = ["# Step 6, pass 3: do the remaining pro arguments hold up?", "",
         "Male circumcision articles only. Every pro argument sentence that still had at least 1 point after pass 2 "
         f"({Sm['items']} sentences) was checked again, fresh, against fallacy_catalog v0.6.1, the same way the "
         "three reviewers flagged. Each distinct catalog entry with verdict **flag** costs 1 point, down to 0. "
         "\"Possible issue\" is recorded but costs nothing.", "",
         "Read this with the limits in mind. The checks are a **model's judgment, not a person's**, by "
         f"{len(Sm['checked_by'])} checker sessions. Each was told not to open the earlier flags, scores or pass-2 "
         "results, but they ran from a conversation that already knew earlier results, so this is **not blind**. "
         "Flags are leads, not verdicts. Anti arguments were not rechecked. Instructions: [RECHECK_PROMPT.md](RECHECK_PROMPT.md). Method and limits: "
         "[../METHOD.md](../METHOD.md#pass-3-fresh-recheck-of-the-remaining-pro-arguments).", "",
         "## Result", "",
         f"- Sentences checked: **{Sm['checked']}**. Lines recorded: " +
         ", ".join(f"{v} {Sm['lines'].get(v, 0)}" for v in ("flag", "possible_issue", "no_issue")) + ".",
         f"- Sentences that lost points: **{Sm['sentences_dinged']}** "
         f"({Sm['tier_A_dinged']} of the {Sm['tier_A']} that still had all 3 points), 1 point each.",
         f"- {Sm['flags_not_counted_same_entry_as_step5']} more flags were not counted: they named the same entry a "
         "step-5 reviewer had already flagged on that sentence.",
         f"- {len(Sm['dinged_with_earlier_ding'])} of the dinged sentences had already lost a point for what reads as "
         "the same flaw under another name (step 5 irrelevant conclusion, now red herring) or through pass 2. "
         "The rule does not merge these. Without them, pass 3 would end at "
         + "/".join(str(Sm['male_pro_points_left_after_pass3_without_those'][k]) for k in "3210")
         + " (3/2/1/0); the count at full points is the same.", "",
         "| Male pro points left | 3 | 2 | 1 | 0 |", "|---|---|---|---|---|"]
    for lab, d in (("Step 5", s5), ("After pass 2", s2), ("After pass 3", s3)):
        L.append(f"| {lab} | " + " | ".join(str(d[k]) for k in "3210") + " |")
    L += ["", "## Entries flagged", "", "| Entry | Sentences |", "|---|---|"]
    for e, n in Sm["entries_counted"].items():
        L.append(f"| [{e}](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#{e}) | {n} |")
    L += ["", "## Flags", "",
          "Each flagged sentence, verbatim from the 2026-10-01 snapshot (checked by script), with the quoted words "
          "and the checker's one-line reason.", ""]
    for r in [r for r in rows if r["counted"] == "yes"]:
        k = (r["article"], r["sentence_id"])
        L += [f"> {S[k]['text']}", ">", f"> `{k[0]}` {k[1]} · **{r['entry_id']}** on \"{r['quote']}\"", "",
              f"Checker's reason: {r['reason']}", ""]
        if r["earlier_dings"]:
            L += [f"Earlier points lost on this sentence: {r['earlier_dings']}.", ""]
    L += ["## Files", "",
          "- [findings.csv](findings.csv): every line recorded (flag, possible issue, no issue), with quote, entry, "
          "reason, whether it counted, and the checker.",
          "- [points_by_pass.csv](points_by_pass.csv): all male pro argument sentences, points at step 5, after pass 2 "
          "and after pass 3.",
          "- [summary.json](summary.json), [RECHECK_PROMPT.md](RECHECK_PROMPT.md), "
          "[work/queue.csv](work/queue.csv), [work/findings.csv](work/findings.csv).",
          "- Scripts: [recheck_queue.py](scripts/recheck_queue.py), [build_recheck.py](scripts/build_recheck.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/07_pro_after_priors.png`.", ""]
    (RC / "RECHECK.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
