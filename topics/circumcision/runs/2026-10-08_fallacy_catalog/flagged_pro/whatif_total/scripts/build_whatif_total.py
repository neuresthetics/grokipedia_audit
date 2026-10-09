#!/usr/bin/env python3
"""Total what-if: how much of the male pro side is left if Jason's premises are taken as true.

Layers the earlier results; it does not change them. Every male pro argument (971) goes into exactly one
group, in this order, so nothing is counted twice:
  1. already flagged: lost >= 1 point at step 5, pass 2 or pass 3 (recheck/points_by_pass.csv);
  2. what-if: kept 3 points, tagged M, and tagged H (HIV/STI) or C-not-H (cancer only);
  3. not invalidated: the rest, split into medical-other (M, not H or C) and E / R / O.
Also runs a keyword check on the E/R/O group and reads the model check of its keyword hits.
Writes summary.json and TOTAL_WHATIF.md next to this folder.
"""
import csv, json, re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
FP = HERE.parent
pb = list(csv.DictReader(open(FP / "recheck/points_by_pass.csv")))
topic = {(r["article"], r["sentence_id"]): r for r in csv.DictReader(open(FP / "topic_tags/tags.csv"))}
sti = {(r["article"], r["sentence_id"]): r["tag"] for r in csv.DictReader(open(FP / "sti_dependence/tags.csv"))}
can = {(r["article"], r["sentence_id"]): r["tag"] for r in csv.DictReader(open(FP / "cancer_dependence/tags.csv"))}

# word-bounded so 'stigma', 'stipulated' and 'aids hygiene' don't match
HV = re.compile(r"\b(?:HIV|AIDS|STIs?|STDs?|HPV|HSV|VMMCs?)\b|(?i:\b(?:herpes|syphilis|gonorrh\w*|chlamydia\w*|"
                r"trichomon\w*|chancroid|sexually transmitted|papillomavirus|genital ulcers?|seroconver\w*|antiretroviral\w*)\b)")
CA = re.compile(r"(?i:cancer|carcinom|malignan|tumou?r|neoplas)")

groups, when = Counter(), Counter()
for r in pb:
    k = (r["article"], r["sentence_id"])
    if r["points_after_pass3"] != "3":
        groups["already_flagged"] += 1
        when["step5" if r["points_step5"] != "3" else "pass2" if r["points_after_pass2"] != "3" else "pass3"] += 1
        continue
    t = topic[k]["tag"]
    if t == "M":
        if sti[k] == "H":
            groups["whatif_hiv_sti"] += 1
        elif can.get(k) == "C":
            groups["whatif_cancer_only"] += 1
        else:
            groups["medical_other"] += 1
    else:
        groups[{"E": "ethics_law", "R": "religion_culture", "O": "other"}[t]] += 1

N = len(pb)
order = ["already_flagged", "whatif_hiv_sti", "whatif_cancer_only", "medical_other", "ethics_law", "religion_culture", "other"]
assert sum(groups.values()) == N and set(groups) <= set(order)
inval_whatif = groups["whatif_hiv_sti"] + groups["whatif_cancer_only"]
not_inval = N - groups["already_flagged"] - inval_whatif

# keyword check on the non-medical survivors
ero = [r for r in topic.values() if r["tag"] != "M"]
hits = [r for r in ero if HV.search(r["text"]) or CA.search(r["text"])]
hit_keys = {(r["article"], r["sentence_id"]) for r in hits}
jud = list(csv.DictReader(open(HERE / "keyword_check/judgments.csv")))
assert {(j["article"], j["sentence_id"]) for j in jud} == hit_keys, "judgments must cover exactly the keyword hits"
ys = [j for j in jud if j["answer"] == "Y"]

S = {
    "scope": "male circumcision pro arguments (step 5 survival scoring), 971",
    "what_if": "Premises taken as true for this count only: (1) no protection against HIV or other STDs; "
               "(2) STD rates are higher in circumcising countries; (3) cancer prevention is not a valid reason. "
               "Not a finding that the premises are true.",
    "pro_total": N,
    "groups": {g: {"count": groups[g], "share_of_pro": round(groups[g] / N, 6)} for g in order},
    "already_flagged_first_lost_at": dict(when),
    "invalidated_under_what_if": inval_whatif,
    "already_flagged_or_what_if": groups["already_flagged"] + inval_whatif,
    "not_invalidated": not_inval,
    "non_medical_survivors": len(ero),
    "non_medical_keyword_hits": len(hits),
    "non_medical_keyword_hits_by_tag": dict(Counter(r["tag"] for r in hits)),
    "non_medical_model_check": {"checked": len(jud), "Y": len(ys), "N": len(jud) - len(ys),
                                "Y_items": [f"{j['article']} {j['sentence_id']}" for j in ys], "by": sorted({j["by"] for j in jud})},
}
json.dump(S, open(HERE / "summary.json", "w"), indent=2)

pct = lambda n: f"{100 * n / N:.1f}%"
LAB = {"already_flagged": "Already flagged by the audit (lost 1+ point at step 5, pass 2 or pass 3)",
       "whatif_hiv_sti": "What-if: rests on the HIV/STI claim",
       "whatif_cancer_only": "What-if: rests on the cancer claim only",
       "medical_other": "Not invalidated: other medical claims",
       "ethics_law": "Not invalidated: ethics, rights or law",
       "religion_culture": "Not invalidated: religion, culture or tradition",
       "other": "Not invalidated: other, mixed or framing"}
rows = "\n".join(f"| {LAB[g]} | {groups[g]} | {pct(groups[g])} |" for g in order)
yl = "\n".join(f"- `{j['article']}` `{j['sentence_id']}`: {j['reason']}" for j in ys)
md = f"""# Total what-if: how much of the pro side is left under Jason's premises?

**What-if, not a finding.** This page takes three premises as true for the sake of the count:

1. circumcision gives no protection against HIV or other STDs;
2. STD rates are higher in circumcising countries;
3. cancer prevention is not a valid reason (penile cancer is rare, and prevention by removal is not valid).

This audit did not check any of the three. Premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias. Premise 2 is a country-level comparison; this count does not use it separately, because arguments that rest on HIV/STI protection are already set aside under premise 1. So the result holds only if the premises hold.

Scope: the {N} male circumcision pro arguments from step 5. Earlier results are not changed; this page only adds them up.

## Result

| Group | Arguments | Share of {N} |
|---|---:|---:|
{rows}
| **Total** | **{N}** | **100%** |

- Already flagged by the audit: **{groups['already_flagged']}** ({pct(groups['already_flagged'])}). They first lost a point at step 5 ({when['step5']}), pass 2 ({when['pass2']}) or pass 3 ({when['pass3']}).
- Set aside under the what-if: **{inval_whatif}** ({pct(inval_whatif)}), from the HIV/STI pass ({groups['whatif_hiv_sti']}) and the cancer pass ({groups['whatif_cancer_only']} cancer only).
- Flagged or set aside: **{groups['already_flagged'] + inval_whatif}** ({pct(groups['already_flagged'] + inval_whatif)}).
- Not invalidated: **{not_inval}** ({pct(not_inval)}): {groups['medical_other']} medical arguments on other claims (UTIs, phimosis, hygiene, safety, sexual function and so on), plus {len(ero)} ethics, law, religion, culture or other arguments.

Chart: [11_pro_side_invalidated.png](../../../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

![What-if: how much of the pro side is left?](../../../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

## Counting rules (no double counting)

Each argument goes into one group only, in this order:

1. If it lost 1 or more points at step 5, pass 2 or pass 3, it is **already flagged**, whatever its topic.
2. Otherwise, if it was tagged medical (M) and HIV/STI (H), it is **what-if: HIV/STI** ([STI_DEPENDENCE.md](../sti_dependence/STI_DEPENDENCE.md)).
3. Otherwise, if it was tagged medical and cancer (C), it is **what-if: cancer only** ([CANCER_DEPENDENCE.md](../cancer_dependence/CANCER_DEPENDENCE.md)).
4. Otherwise it is **not invalidated**, split by its topic tag ([TAGS.md](../topic_tags/TAGS.md)).

## Not checked: non-medical arguments that lean on HIV/STI or cancer

The {len(ero)} arguments tagged ethics/law, religion/culture or other were not put through the HIV/STI or cancer passes, so the what-if does not touch them. Some may still lean on those claims, which is a recall limit.

- **Keyword check (rough upper bound, no model):** {len(hits)} of {len(ero)} ({100 * len(hits) / len(ero):.1f}%) name HIV, an STI or cancer ({', '.join(f"{v} {k}" for k, v in sorted(S['non_medical_keyword_hits_by_tag'].items()))}). Naming a term is not the same as resting on it.
- **Model check of those {len(jud)}** ([CHECK_PROMPT.md](keyword_check/CHECK_PROMPT.md), [judgments.csv](keyword_check/judgments.csv)): **{len(ys)}** rest on the HIV/STI claim; the other {len(jud) - len(ys)} keep another point (consent, culture, another medical benefit) or only report a view or event.
{yl}

These {len(ys)} are reported separately and are **not** added to the table. Adding them would make the what-if group {inval_whatif + len(ys)} ({pct(inval_whatif + len(ys))}). A non-medical sentence that leans on these claims without naming them would not be found.

## Caveats

- **What-if, not a finding.** A tag means "depends on the claim", not that the claim is wrong.
- **AI-tagged, not blind.** The topic, HIV/STI and cancer tags and the model check above were made by AI model sessions, not a person. All ran from a conversation that already knew the earlier results, so they are not blind. The model check of the {len(jud)} keyword hits was one session.
- **Pro only.** Anti arguments were checked only at step 5 and are not part of this count.
- **Recall limits.** The cancer pass covers only medical sentences with a cancer, HPV or cervical keyword within two sentences. See the non-medical check above too.
- **One topic per sentence.** Mixed sentences were forced into one type at the topic-tagging step.

Built by `scripts/build_whatif_total.py` from `../recheck/points_by_pass.csv`, `../topic_tags/tags.csv`, `../sti_dependence/tags.csv` and `../cancer_dependence/tags.csv`.
"""
pg = round(100 * (groups["already_flagged"] + inval_whatif) / N)
md += f"""
## The premises, in plain words

If these three things are true, {pg}% of the pro side is invalidated ({groups['already_flagged'] + inval_whatif} of {N}: {groups['already_flagged']} already flagged by this audit plus {inval_whatif} that rest on the HIV/STI or cancer claim). The other {not_inval} ({100 - pg}%) are left standing. Premises are assumed, not tested here.

1. **Circumcision does not protect against HIV or other STIs.**
2. **STI rates are highest in circumcising countries.** This adds no separate count beyond premise 1.
3. **Cancer prevention is not a valid reason** (penile cancer is rare, and prevention-by-removal proves too much).

Note on the chart: chart 11 was redrawn so it states this at a glance. Its title is now "If these three things are true, {pg}% of the pro side is invalidated", and the premises are shown in a box on the chart. Alt text above that reads "What-if: how much of the pro side is left?" refers to the same chart.
"""
open(HERE / "TOTAL_WHATIF.md", "w").write(md)
print(json.dumps(S, indent=2))

# appended 2026-10-08: keep the "Limits: a narrow selection" section at the end of TOTAL_WHATIF.md on rebuild
LIMITS = """
## Limits: a narrow selection

The percentage comes from a narrow selection of arguments: the claims in two X posts, plus one point about cancer, applied to the pro arguments in 39 male circumcision Grokipedia articles. It is a what-if count. Applying more premises or arguments would change the numbers, in either direction. Nothing here has been tested beyond that selection.
"""
with open(HERE / "TOTAL_WHATIF.md", "a") as fh:
    fh.write(LIMITS)
