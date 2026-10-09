#!/usr/bin/env python3
"""Step 6: the flagged pro arguments in the male circumcision articles (types, shares, mechanics, quotes,
counters). FGM articles are out of scope for this step.

Run from the repo root:
    python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/scripts/build_flagged_pro.py

Reads (all committed):
  survival/survival_scores.csv       argument sentences with points_left (step 5)
  survival/flag_sentence_map.csv     which flag (reviewer, flag_row) touches which sentence
  flags.csv, reviewer2_flags.csv, reviewer3_flags.csv
  flagged_pro/catalog_entries_v0.6.1.json   verbatim extract of the fallacy_catalog entries used here,
                                     from fallacies.json at commit 2a56493 (see --refresh-catalog)
  ../../articles/<slug>/snapshots/2026-10-01.txt   for the verbatim check
Writes flagged_pro/flagged_pro.csv, flagged_pro/FLAGGED_PRO.md, flagged_pro/summary.json.

--refresh-catalog PATH  rebuilds the catalog extract from a fallacies.json file (for example a clone of
neuresthetics/fallacy_catalog checked out at 2a56493a3931018e9143bc7235f152f5cc5b459e).
Deterministic: same inputs, same outputs. No model is called.
"""
import collections, csv, json, pathlib, sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
RUN = OUT.parent
SNAP = RUN.parent.parent / "articles"
CAT = OUT / "catalog_entries_v0.6.1.json"
COMMIT = "2a56493a3931018e9143bc7235f152f5cc5b459e"
LINK = f"https://github.com/neuresthetics/fallacy_catalog/blob/{COMMIT}/FALLACIES.md#"
REV = {"r1": ("R1", "flags.csv"), "r2": ("R2", "reviewer2_flags.csv"), "r3": ("R3", "reviewer3_flags.csv")}

# Families = the catalog's own `category` field. Fixed order (used for display and as the last tie-break).
FAMILIES = [
    ("informal: relevance", "relevance", "Off-point reasons",
     "the reason given does not bear on the point at issue"),
    ("informal: presumption", "presumption", "Unearned or clashing premises",
     "the step rests on a premise that is assumed, dropped a qualification, or clashes with the article itself"),
    ("informal: weak induction", "weak_induction", "Thin or ill-fitting evidence",
     "the evidence is real but too thin, too selective or too unlike the case to carry the conclusion"),
    ("informal: statistical and probabilistic", "statistics", "Stretched numbers",
     "a figure is carried beyond the data it came from, or only what is measurable is allowed to count"),
    ("informal: causal", "causal", "Shaky cause and effect",
     "a trend or a correlation is read as proof of cause while a rival cause is left open"),
]
FAM = {c: (k, short, gist) for c, k, short, gist in FAMILIES}
ORDER = [k for _, k, _, _ in FAMILIES]

# Quotes shown per family (article, sentence_id). Chosen by hand from sentences that family hit, preferring
# 0-point sentences. The script checks each pick
# is in scope, is hit by that family, and is verbatim in the snapshot.
PICKS = {
    "relevance": [("brit-milah", "s0138"), ("views-on-circumcision", "s0125"), ("mohel", "s0231"),
                  ("ulwaluko", "s0097")],
    "presumption": [("circumcision", "s0060"), ("circumcision", "s0459"), ("ulwaluko", "s0147")],
    "weak_induction": [("ethics-of-circumcision", "s0106"), ("ethics-of-circumcision", "s0302"),
                       ("circumcision-in-africa", "s0285")],
    "statistics": [("circumcision-controversies", "s0128"), ("mohel", "s0122"),
                   ("ethics-of-circumcision", "s0198")],
    "causal": [("circumcision-controversies", "s0073"), ("prevalence-of-circumcision", "s0058")],
}

# Counters. `entries` lists (catalog entry, index of the required condition quoted, index of the legitimate
# look-alike quoted); the quoted text is pulled verbatim from the extract. `audit` is this audit's wording: a reply about the reasoning move,
# not a new factual claim about circumcision.
COUNTERS = {
    "relevance": dict(entries=[("non-sequitur", 1, 1), ("irrelevant-conclusion", 1, 0), ("straw-man", 1, 0),
                               ("bulverism", 2, 0), ("appeal-to-tradition", 1, 0)],
                      audit="Name the question actually at issue, then ask what links the reason to it. "
                            "Low complication rates answer \"is it safe?\", not \"who should decide?\". If an "
                            "opponent's view is restated, set their own words (usually given elsewhere in the same "
                            "article) beside the restatement. If a view is explained by its holders' motives, "
                            "source or long history, ask for the error in the view itself."),
    "presumption": dict(entries=[("inconsistency", 1, 1), ("double-standard", 1, 0), ("secundum-quid", 2, 0)],
                        audit="Put the two clashing claims side by side, often from the same article, and ask "
                              "which one holds. Apply the stated test, for example \"observational data are weak\", "
                              "to both sides' evidence. Restore the dropped qualification (which ages, which "
                              "setting, which procedure) and check whether the conclusion still follows."),
    "weak_induction": dict(entries=[("false-analogy", 2, 0), ("argument-from-ignorance", 1, 0),
                                    ("argument-from-silence", 2, 0), ("nut-picking", 1, 0)],
                           audit="Name the difference between the two cases that matters to the conclusion. "
                                 "Ask whether the cases shown stand for the whole group they are used to describe. "
                                 "Silence or a missing condemnation is not evidence of approval."),
    "statistics": dict(entries=[("over-extrapolation", 2, 0), ("mcnamara-fallacy", 2, 0), ("relative-risk-framing", 2, 0)],
                       audit="Ask where the figure comes from (ages, setting, procedure, follow-up time) and "
                             "whether the conclusion stays inside that range. Ask for absolute numbers next to "
                             "relative ones. Ask what was left out because it is hard to measure."),
    "causal": dict(entries=[("post-hoc", 2, 1), ("cum-hoc", 2, 1), ("false-cause", 1, 0)],
                   audit="Name a rival cause running at the same time and ask how it was ruled out. The second "
                         "quote names one itself (antiretroviral therapy expansion) and states, without showing "
                         "how, that the decline is independent of it. A trend that moves with a programme is a "
                         "reason to test for cause, not proof of it."),
}


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def refresh(path):
    full = json.load(open(path, encoding="utf-8"))
    assert full.get("version") in ("0.6.1", "v0.6.1"), full.get("version")
    used = set()
    for r in rd(RUN / "flags.csv") + rd(RUN / "reviewer2_flags.csv") + rd(RUN / "reviewer3_flags.csv"):
        used.add(r["entry_id"])
    keep = ["id", "name", "category", "definition", "required_conditions", "legitimate_lookalikes"]
    ents = {e["id"]: {k: e[k] for k in keep} for e in full["entries"] if e["id"] in used}
    json.dump({"source": f"neuresthetics/fallacy_catalog fallacies.json at commit {COMMIT} (v0.6.1)",
               "note": "Verbatim fields of every entry cited in this run's three flag files.",
               "entries": dict(sorted(ents.items()))}, open(CAT, "w", encoding="utf-8"), indent=1,
              ensure_ascii=False)
    print(f"wrote {CAT} ({len(ents)} entries)")


def main():
    if "--refresh-catalog" in sys.argv:
        refresh(sys.argv[sys.argv.index("--refresh-catalog") + 1])
    E = json.load(open(CAT, encoding="utf-8"))["entries"]
    flags = {k: rd(RUN / fn) for k, (_, fn) in REV.items()}
    fmap = collections.defaultdict(list)
    for m in rd(RUN / "survival" / "flag_sentence_map.csv"):
        fmap[(m["slug"], m["sentence_id"])].append(m)
    scope = [r for r in rd(RUN / "survival" / "survival_scores.csv")
             if r["side"] == "pro" and int(r["points_left"]) < 3 and r["topic_group"] == "male"]

    rows, snaps = [], {}
    for r in scope:
        key = (r["article"], r["sentence_id"])
        if r["article"] not in snaps:
            snaps[r["article"]] = (SNAP / r["article"] / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
        assert r["text"] in snaps[r["article"]], f"not verbatim: {key}"
        hits = []
        for m in fmap[key]:
            f = flags[m["reviewer"]][int(m["flag_row"]) - 1]
            assert f["entry_id"] == m["entry_id"] and f["slug"] == r["article"], key
            hits.append(dict(rev=REV[m["reviewer"]][0], entry=f["entry_id"], name=f["entry_name"],
                             fam=FAM[E[f["entry_id"]]["category"]][0], reason=f["reason"]))
        revs = sorted({h["rev"] for h in hits})
        assert len(revs) == 3 - int(r["points_left"]), key
        fr = collections.defaultdict(set); fn = collections.Counter()
        for h in hits:
            fr[h["fam"]].add(h["rev"]); fn[h["fam"]] += 1
        # primary family: most reviewers; then most flags; then the fixed family order
        primary = sorted(fr, key=lambda k: (-len(fr[k]), -fn[k], ORDER.index(k)))[0]
        rows.append(dict(
            article=r["article"], sentence_id=r["sentence_id"], topic_group=r["topic_group"],
            points_left=int(r["points_left"]), reviewers="|".join(revs), primary_family=primary,
            families="|".join(k for k in ORDER if k in fr),
            primary_tie_broken="yes" if sum(len(fr[k]) == len(fr[primary]) for k in fr) > 1 else "no",
            entries="; ".join(f"{h['rev']}: {h['entry']}" for h in sorted(hits, key=lambda h: h["rev"])),
            entry_names="; ".join(f"{h['rev']}: {h['name']}" for h in sorted(hits, key=lambda h: h["rev"])),
            text=r["text"], _hits=hits))

    fields = [k for k in rows[0] if not k.startswith("_")]
    with open(OUT / "flagged_pro.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader()
        for x in rows:
            w.writerow({k: x[k] for k in fields})

    # counts
    n = len(rows)
    S = {"scope": {"group": "male circumcision articles only", "sentences": n,
                   "points_left": {str(k): sum(x["points_left"] == k for x in rows) for k in (2, 1, 0)}},
         "families": {}}
    for k in ORDER:
        p = sum(x["primary_family"] == k for x in rows)
        a = sum(k in x["families"].split("|") for x in rows)
        d = dict(primary=p, primary_share=round(p / n, 4), any=a, any_share=round(a / n, 4))
        ent = collections.Counter()
        for x in rows:
            for e in sorted({h["entry"] for h in x["_hits"] if h["fam"] == k}):
                ent[e] += 1
        d["entries"] = dict(sorted(ent.items(), key=lambda t: (-t[1], t[0])))
        S["families"][k] = d
    S["multi_family_sentences"] = sum(len(x["families"].split("|")) > 1 for x in rows)
    S["primary_ties_broken"] = sum(x["primary_tie_broken"] == "yes" for x in rows)
    json.dump(S, open(OUT / "summary.json", "w"), indent=1)

    # picks: in scope, hit by that family, verbatim
    by = {(x["article"], x["sentence_id"]): x for x in rows}
    for k, ps in PICKS.items():
        assert 2 <= len(ps) <= 4
        for p in ps:
            assert p in by and k in by[p]["families"].split("|"), (k, p)
    write_md(S, rows, by, E)
    print(json.dumps({k: (v["primary"], v["any"]) for k, v in S["families"].items()}))
    print("scope", S["scope"], "multi-family", S["multi_family_sentences"], "ties", S["primary_ties_broken"])


def pc(a, b):
    return f"{100 * a / b:.0f}%" if b else "–"


def link(e, E):
    return f"[{E[e]['name']}]({LINK}{e})"


def write_md(S, rows, by, E):
    sc = S["scope"]
    n = sc["sentences"]
    pts = sc["points_left"]
    L = ["# Step 6: the flagged pro arguments in the male circumcision articles (2026-10-08)", "",
         "This is the last step of the benchmark. It covers the **male circumcision articles only**: 39 of the 58 "
         "articles. FGM articles are not part of this step. It takes every **pro** argument sentence there that "
         "lost at least one point in step 5 ([`../survival/`](../survival/)), meaning at least one of the three AI "
         "reviewers flagged it. Then it asks what kinds of flawed reasoning those flags name, how each kind works, "
         "and what reply exposes it.", "",
         "Read this with the limits in mind. **Flags are leads, not verdicts**: each one is an AI reviewer's "
         "judgment against [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1. The three "
         "reviewers were **not blind** (later reviewers' instructions mentioned earlier results). The pro/anti "
         "labels came from an **AI model, not a person**. A flagged sentence may still have a true conclusion; "
         "the flag is about the step from reason to conclusion. How this was built: [METHOD.md](METHOD.md). "
         "Full table: [flagged_pro.csv](flagged_pro.csv).", "",
         "## Scope", "",
         f"- **{n}** flagged pro argument sentences in the male circumcision articles: {pts['2']} with 2 points "
         f"left, {pts['1']} with 1 and {pts['0']} with 0 (flagged by all three reviewers).",
         "- Out of scope: FGM articles, and anti arguments (only 4 anti sentences in the male circumcision "
         "articles lost a point).", "",
         "## Types: shares by family", "",
         "Each catalog entry belongs to one of the catalog's own categories, used here as the families. "
         "**Primary family** gives each sentence one family (the one the most reviewers named; see METHOD.md), so "
         "the shares add to 100%. **Any hit** counts a sentence once for every family any reviewer named, so "
         "those shares can add to more than 100%.", "",
         "| Family (catalog category) | What it means | Primary | Any hit |", "|---|---|---|---|"]
    for c, k, short, gist in FAMILIES:
        d = S["families"][k]
        L.append(f"| **{short}** (`{c}`) | {gist} | {d['primary']} ({pc(d['primary'], n)}) "
                 f"| {d['any']} ({pc(d['any'], n)}) |")
    L += ["", f"{S['multi_family_sentences']} sentences were hit by more than one family; "
          f"{S['primary_ties_broken']} needed the tie-break to pick a primary family.", "",
          "Family lines are soft. The same move, carrying HIV trial results from adult men to infant circumcision "
          "in general, was named secundum quid (presumption) by one reviewer and over-extrapolation (stretched "
          "numbers) by another. That is why stretched numbers is named on more sentences than it is primary for.", ""]
    for c, k, short, gist in FAMILIES:
        d = S["families"][k]
        L += [f"## {short} (`{c}`)", "",
              f"Primary family for {d['primary']} of {n} flagged pro sentences ({pc(d['primary'], n)}); named at "
              f"all on {d['any']}.", "",
              "### Mechanics", "",
              f"In short, {gist}. The entries the reviewers used in this family, with the catalog's own "
              "definition (sentences hit in brackets):", ""]
        for e, m in d["entries"].items():
            L.append(f"- {link(e, E)} ({m}): {E[e]['definition']}")
        L += ["", "### Quotes", "",
              "Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.", ""]
        for p in PICKS[k]:
            x = by[p]
            L.append(f"> {x['text']}")
            L.append(">")
            L.append(f"> `{x['article']}` {x['sentence_id']} · **{x['points_left']} of 3 points left** · "
                     f"flagged by {x['entry_names']}")
            L.append("")
        L += ["### Effective counter", "",
              "**From the catalog.** The catalog has no separate \"counter\" field. An entry applies only when all "
              "its required conditions hold, so the reply is to test the condition the flag rests on, and its "
              "legitimate look-alikes say what a sound version of the step would look like. Catalog wording:", ""]
        for e, ri, li in COUNTERS[k]["entries"]:
            assert e in d["entries"], (k, e)
            key = E[e]["required_conditions"][ri]
            look = E[e]["legitimate_lookalikes"][li]["text"]
            L.append(f"- {link(e, E)}. Required: \"{key}\" Legitimate look-alike (what would answer the flag): "
                     f"\"{look}\"")
        L += ["", f"**This audit's wording** (not from the catalog): {COUNTERS[k]['audit']}", ""]
    dep = OUT / "dependency" / "summary.json"
    if dep.exists():  # second layer (dependency/scripts/build_dependency.py)
        D = json.load(open(dep))
        b, a = D["male_pro_points_left_before"], D["male_pro_points_left_after"]
        L += ["## Second layer: surviving pro arguments that depend on these", "",
              f"Each of the {D['survivors']} pro argument sentences in the male circumcision articles that kept at least "
              "1 point was checked for whether its reasoning uses one of the flagged sentences above as a premise "
              "(builds on it, refers back to it, or relies on the same flagged claim). Each distinct flagged sentence "
              "it depends on costs it 1 point, down to 0. Dependence was judged by an AI model, not a person, on "
              f"{D['judged']} pairs picked by a cheap pre-filter, so the count is a lower bound.", "",
              f"- **{D['survivors_dinged']} of {D['survivors']}** survivors lost 1 point; none lost more. "
              f"{D['priors_relied_on']} of the 61 flagged sentences were relied on, all within their own article.",
              "- Male pro points left, 3/2/1/0: " + "/".join(str(b[k]) for k in "3210") + " before, "
              + "/".join(str(a[k]) for k in "3210") + " after.",
              "- Anti arguments were not rechecked (only 4 were flagged).", "",
              "Chains with verbatim quotes, files and limits: [dependency/DEPENDENCIES.md](dependency/DEPENDENCIES.md). "
              "Method: [METHOD.md](METHOD.md#second-layer-dependence-on-flagged-priors). "
              "Chart: `docs/img/circumcision/2026-10-08/07_pro_after_priors.png`.", ""]
    rc = OUT / "recheck" / "summary.json"
    if rc.exists():  # pass 3 (recheck/scripts/build_recheck.py)
        X = json.load(open(rc))
        assert X["complete"]
        p3 = X["male_pro_points_left_after_pass3"]
        ents = ", ".join(f"{e} {n}" for e, n in X["entries_counted"].items())
        L += ["## Pass 3: do the remaining pro arguments hold up?", "",
              f"All {X['items']} male pro argument sentences with at least 1 point after the second layer were checked "
              "again, fresh, against the catalog, the same way the reviewers flagged. Each distinct entry flagged costs "
              "1 point. Five AI model sessions did the checking; they were told not to open the earlier flags or "
              "scores but ran from a conversation that knew earlier results, so this is not blind.", "",
              f"- **{X['sentences_dinged']}** sentences lost 1 point ({X['tier_A_dinged']} of the {X['tier_A']} still "
              f"at 3 points). Entries: {ents}. {X['lines'].get('possible_issue', 0)} possible issues were recorded "
              "and cost nothing.",
              "- Male pro points left, 3/2/1/0: " + "/".join(str(p3[k]) for k in "3210") + f" after pass 3 "
              f"({100 * p3['3'] / sum(p3.values()):.1f}% at full points).",
              "- **Pro only.** Anti arguments were checked only in step 5. They were not put through pass 2 or "
              "pass 3, so comparing pro and anti after pass 3 is tilted against pro.", "",
              "Quotes, reasons and limits: [recheck/RECHECK.md](recheck/RECHECK.md). Method: "
              "[METHOD.md](METHOD.md#pass-3-fresh-recheck-of-the-remaining-pro-arguments).", ""]
    L += ["## Files", "",
          "- [flagged_pro.csv](flagged_pro.csv): every flagged pro sentence, with group, points left, reviewers, "
          "primary family, all families, catalog entries and the verbatim text.",
          "- [summary.json](summary.json): the counts above.",
          "- [catalog_entries_v0.6.1.json](catalog_entries_v0.6.1.json): verbatim catalog fields used for the "
          "definitions and counters.",
          "- [METHOD.md](METHOD.md) and [scripts/build_flagged_pro.py](scripts/build_flagged_pro.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/06_flagged_pro_types.png`.", ""]
    (OUT / "FLAGGED_PRO.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
