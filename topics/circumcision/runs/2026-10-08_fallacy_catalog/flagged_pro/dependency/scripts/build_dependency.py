#!/usr/bin/env python3
"""Step 6, second layer: ding each surviving male pro argument once for every flagged pro argument
(the 61 priors in flagged_pro.csv) it was judged to depend on. Floor 0.

Run from anywhere:
    python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/dependency/scripts/build_dependency.py

Reads (all committed):
  survival/survival_scores.csv          survivors: side pro, male articles, points_left >= 1 (step 5)
  flagged_pro/flagged_pro.csv           the 61 priors (step 6)
  dependency/work/candidates.csv        pre-filtered pairs (scripts/dep_candidates.py), ids c0001.. by row order
  dependency/work/judgments.csv         model judgments Y/N with a one-line reason (scripts/dep_queue.py)
  ../../articles/<slug>/snapshots/2026-10-01.txt   for the verbatim check of every quote
Writes dependency/dependencies.csv, dependency/survivors_after_priors.csv, dependency/summary.json,
dependency/DEPENDENCIES.md. Deterministic. No model is called here.
"""
import collections, csv, json, pathlib, sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
DEP = HERE.parent
FP = DEP.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)


def sid(s):
    return int(s[1:])


def main():
    scores = rd(RUN / "survival" / "survival_scores.csv")
    surv = {(r["article"], r["sentence_id"]): r for r in scores
            if r["side"] == "pro" and r["topic_group"] == "male" and int(r["points_left"]) >= 1}
    priors = {(r["article"], r["sentence_id"]): r for r in rd(FP / "flagged_pro.csv")}
    assert len(priors) == 61 and all(p["topic_group"] == "male" for p in priors.values())
    cands = rd(DEP / "work" / "candidates.csv")
    for i, c in enumerate(cands, 1):
        c["candidate"] = f"c{i:04d}"
    J = {r["candidate"]: r for r in rd(DEP / "work" / "judgments.csv")}
    missing = [c["candidate"] for c in cands if c["candidate"] not in J]
    assert not missing, f"{len(missing)} candidates not judged yet, first {missing[:5]}"

    snaps = {}
    def verbatim(a, text):
        if a not in snaps:
            snaps[a] = (SNAP / a / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
        assert text in snaps[a], f"not verbatim: {a}"

    deps = []
    for c in cands:
        j = J[c["candidate"]]
        if j["decision"] != "Y":
            continue
        s, p = (c["survivor_article"], c["survivor_id"]), (c["prior_article"], c["prior_id"])
        assert s in surv and p in priors and s != p, c
        assert j["reason"].strip(), c["candidate"]
        deps.append(dict(candidate=c["candidate"], survivor_article=s[0], survivor_id=s[1],
                         prior_article=p[0], prior_id=p[1],
                         link_type="same_article" if s[0] == p[0] else "same_claim",
                         prefilter=c["prefilter"], reason=j["reason"].strip(), judged_by=j["judged_by"]))
    # one ding per distinct prior per survivor
    seen = set()
    for d in deps:
        k = (d["survivor_article"], d["survivor_id"], d["prior_article"], d["prior_id"])
        assert k not in seen, k; seen.add(k)
    deps.sort(key=lambda d: (d["survivor_article"], sid(d["survivor_id"]), d["prior_article"], sid(d["prior_id"])))
    wr(DEP / "dependencies.csv", deps, list(deps[0]))

    by_s = collections.defaultdict(list)
    for d in deps:
        by_s[(d["survivor_article"], d["survivor_id"])].append(f"{d['prior_article']} {d['prior_id']}")
    out = []
    for k in sorted(surv, key=lambda k: (k[0], sid(k[1]))):
        b = int(surv[k]["points_left"]); n = len(by_s[k])
        out.append(dict(article=k[0], sentence_id=k[1], points_before=b, n_priors=n,
                        points_after=max(0, b - n), points_lost=b - max(0, b - n),
                        flagged_itself="yes" if k in priors else "no", priors="; ".join(by_s[k])))
    wr(DEP / "survivors_after_priors.csv", out, list(out[0]))

    # counts
    allpro = [r for r in scores if r["side"] == "pro" and r["topic_group"] == "male"]
    zero = sum(int(r["points_left"]) == 0 for r in allpro)
    before = collections.Counter(int(r["points_left"]) for r in allpro)
    after = collections.Counter({0: zero})
    for o in out:
        after[o["points_after"]] += 1
    anti = collections.Counter(int(r["points_left"]) for r in scores if r["side"] == "anti" and r["topic_group"] == "male")
    pri_n = collections.Counter((d["prior_article"], d["prior_id"]) for d in deps)
    S = dict(
        scope="male circumcision articles, pro argument sentences",
        candidates=len(cands), judged=len(J), judged_yes=len(deps),
        candidates_by_prefilter={k: sum((k in c["prefilter"]) for c in cands) for k in ("W", "K")},
        candidates_window_only=sum(c["prefilter"] == "W" for c in cands),
        candidates_key_only=sum("W" not in c["prefilter"] for c in cands),
        candidates_cross_article=sum(c["same_article"] != "yes" for c in cands),
        yes_by_link_type=dict(collections.Counter(d["link_type"] for d in deps)),
        survivors=len(out), survivors_with_a_candidate=len({(c["survivor_article"], c["survivor_id"]) for c in cands}),
        survivors_dinged=sum(o["n_priors"] > 0 for o in out),
        flagged_survivors_dinged=sum(o["n_priors"] > 0 and o["flagged_itself"] == "yes" for o in out),
        points_lost={str(k): sum(o["points_lost"] == k for o in out) for k in (0, 1, 2, 3)},
        priors_per_survivor={str(k): sum(o["n_priors"] == k for o in out) for k in sorted({o["n_priors"] for o in out})},
        total_points_before=sum(o["points_before"] for o in out), total_points_after=sum(o["points_after"] for o in out),
        male_pro_points_left_before={str(k): before[k] for k in (3, 2, 1, 0)},
        male_pro_points_left_after={str(k): after[k] for k in (3, 2, 1, 0)},
        male_anti_points_left_unchanged={str(k): anti[k] for k in (3, 2, 1, 0)},
        priors_relied_on=len(pri_n),
        top_priors=[dict(article=a, sentence_id=s, dependents=n) for (a, s), n in
                    sorted(pri_n.items(), key=lambda t: (-t[1], t[0][0], sid(t[0][1])))])
    assert sum(after.values()) == sum(before.values()) == len(allpro)
    json.dump(S, open(DEP / "summary.json", "w"), indent=1)

    # chains, verbatim
    text = {(r["article"], r["sentence_id"]): r["text"] for r in scores}
    top = [(t["article"], t["sentence_id"]) for t in S["top_priors"]]
    for p in pri_n:
        verbatim(p[0], text[p])
    for d in deps:
        verbatim(d["survivor_article"], text[(d["survivor_article"], d["survivor_id"])])
    write_md(S, deps, out, priors, text, top)
    print(json.dumps({k: S[k] for k in ("judged_yes", "survivors_dinged", "points_lost", "male_pro_points_left_before",
                                         "male_pro_points_left_after", "priors_relied_on")}))


def write_md(S, deps, out, priors, text, top):
    b, a = S["male_pro_points_left_before"], S["male_pro_points_left_after"]
    pl = S["points_lost"]
    L = ["# Step 6, second layer: surviving pro arguments that depend on a flagged one", "",
         "Male circumcision articles only. Step 5 left 951 pro argument sentences with at least 1 point. "
         "Step 6 listed the 61 pro sentences that at least one AI reviewer flagged. This layer asks, for each of "
         "the 951: **does its reasoning use one of those 61 flagged arguments as a premise?** Each distinct "
         "flagged argument it depends on costs it 1 point, down to 0.", "",
         "Read this with the limits in mind. Each dependency is a **model's judgment, not a person's**. "
         "Flags are leads, not verdicts, so a point lost here means \"rests on a step a reviewer flagged\", "
         "not \"wrong\". The reviewers were **not blind**. Anti arguments were not checked against the flagged "
         "anti arguments (only 4 exist). How this was built: [../METHOD.md](../METHOD.md#second-layer-dependence-on-flagged-priors).", "",
         "## Result", "",
         f"- Pairs judged: **{S['judged']}** (all pairs the pre-filter found). Judged as a dependency: "
         f"**{S['judged_yes']}** ({S['yes_by_link_type'].get('same_article', 0)} in the same article, "
         f"{S['yes_by_link_type'].get('same_claim', 0)} the same claim in another article).",
         f"- Survivors that lost points: **{S['survivors_dinged']} of {S['survivors']}**, "
         f"relying on {S['priors_relied_on']} of the 61 flagged arguments.",
         f"- Points across the 951 survivors: {S['total_points_before']} before, {S['total_points_after']} after.", "",
         "| Points lost | Survivors |", "|---|---|"]
    for k in ("0", "1", "2", "3"):
        L.append(f"| {k} | {pl[k]} |")
    L += ["", "All male pro argument sentences (971), points left:", "",
          "| Points left | Before (step 5) | After this layer |", "|---|---|---|"]
    for k in ("3", "2", "1", "0"):
        L.append(f"| {k} | {b[k]} | {a[k]} |")
    L += ["", "## Most relied-on flagged arguments", "",
          "| Flagged argument | Dependents | Flagged as |", "|---|---|---|"]
    for t in S["top_priors"]:
        p = (t["article"], t["sentence_id"])
        L.append(f"| `{p[0]}` {p[1]} | {t['dependents']} | {priors[p]['entry_names']} |")
    L += ["", "## Chains", "",
          "Each flagged argument, then the survivors judged to depend on it, with the model's one-line reason. "
          "Quotes are verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of "
          "the text. All relied-on flagged arguments are shown, most dependents first.", ""]
    for p in top:
        L += [f"### `{p[0]}` {p[1]}", "",
              f"> {text[p]}", ">", f"> **Flagged** ({priors[p]['points_left']} of 3 points left) as {priors[p]['entry_names']}", ""]
        for d in [d for d in deps if (d["prior_article"], d["prior_id"]) == p]:
            s = (d["survivor_article"], d["survivor_id"])
            o = next(o for o in out if (o["article"], o["sentence_id"]) == s)
            L += [f"Depends on it ({d['link_type'].replace('_', ' ')}): `{s[0]}` {s[1]}, "
                  f"{o['points_before']} → {o['points_after']} points", "",
                  f"> {text[s]}", "", f"Model's reason: {d['reason']}", ""]
    L += ["## Files", "",
          "- [dependencies.csv](dependencies.csv): every judged dependency (survivor, prior, link type, pre-filter, reason, judge).",
          "- [survivors_after_priors.csv](survivors_after_priors.csv): all 951 survivors, points before and after.",
          "- [summary.json](summary.json): the counts above.",
          "- [prior_claims.csv](prior_claims.csv): claim keys used by the pre-filter.",
          "- [DEP_PROMPT.md](DEP_PROMPT.md): the judging instructions.",
          "- [work/candidates.csv](work/candidates.csv) and [work/judgments.csv](work/judgments.csv): every pair "
          "judged, Y or N.",
          "- Scripts: [dep_candidates.py](scripts/dep_candidates.py), [dep_queue.py](scripts/dep_queue.py), "
          "[build_dependency.py](scripts/build_dependency.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/07_pro_after_priors.png`.", ""]
    (DEP / "DEPENDENCIES.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
