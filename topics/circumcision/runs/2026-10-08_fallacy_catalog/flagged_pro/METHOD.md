# Step 6 method: the flagged pro arguments (male circumcision articles only)

This file explains how [FLAGGED_PRO.md](FLAGGED_PRO.md), [flagged_pro.csv](flagged_pro.csv), [summary.json](summary.json) and the chart `docs/img/circumcision/2026-10-08/06_flagged_pro_types.png` were built, so another AI or a person can redo and check them. Built on 2026-10-08. No model was called in this step: everything below is done by `scripts/build_flagged_pro.py`, except the quote picks and the counter wording, which were chosen and written by an AI model working on this audit, not by a person.

## 1. Scope

- **In scope:** every row of `../survival/survival_scores.csv` with `side = pro`, `points_left < 3` and `topic_group = male`. That means a pro argument sentence in a male circumcision article that at least one of the three reviewers flagged.
- **Count:** 61 sentences: 26 with 2 points left, 15 with 1 and 20 with 0.
- **Male circumcision articles only.** The FGM articles (slug contains `female`, or `clitoridectomy`, `gishiri-cutting`, `infibulation`) are left out of this step by the owner's choice. Their 10 flagged pro sentences are still listed in `../survival/SURVIVORS.md`.
- **Anti arguments are left out.** Only 4 anti sentences in the male circumcision articles lost a point, too few to break down.
- **Which flags count:** a flag counts for a sentence if `../survival/flag_sentence_map.csv` maps it there. That is the step-5 rule: same article, overlapping character span. Each mapped flag is joined back to its row in `../flags.csv`, `../reviewer2_flags.csv` or `../reviewer3_flags.csv` (`flag_row` is 1-based) to get `entry_id`, `entry_name` and the reviewer's reason. The script checks the number of distinct reviewers equals `3 − points_left` for every sentence.

## 2. Types and the rollup rule

- **Types** are the fallacy_catalog v0.6.1 entries the reviewers cited (`entry_id`, `entry_name`). 32 different entries hit the 61 sentences, too many to chart.
- **Rollup rule:** each entry is rolled up to its own `category` field in the catalog's `fallacies.json` at commit `2a56493a3931018e9143bc7235f152f5cc5b459e`. These are the catalog's own categories; no mapping was made by hand. Five categories occur:

| Family key | Plain name used here | Catalog category |
|---|---|---|
| relevance | Off-point reasons | informal: relevance |
| presumption | Unearned or clashing premises | informal: presumption |
| weak_induction | Thin or ill-fitting evidence | informal: weak induction |
| statistics | Stretched numbers | informal: statistical and probabilistic |
| causal | Shaky cause and effect | informal: causal |

- The plain names are this audit's wording. The catalog also has narrower "use-only-one families" (tie-break groups such as *Generalization* or *Causation*). They are not used for the rollup, because they overlap and do not cover every entry.
- The verbatim catalog fields used (id, name, category, definition, required conditions, legitimate look-alikes) for every entry cited in the run's three flag files are stored in `catalog_entries_v0.6.1.json`. Rebuild that file with `--refresh-catalog <path to fallacies.json at 2a56493>`.

## 3. Counting

- **Any hit:** a sentence counts once for each family any reviewer named on it. Several flags from the same family count once. These shares can add to more than 100%.
- **Primary family:** each sentence gets exactly one family, so shares add to 100%. Rule, in order:
  1. the family named by the most distinct reviewers on that sentence;
  2. if tied, the family with the most flags on that sentence;
  3. if still tied, the first in the fixed order relevance, presumption, weak_induction, statistics, causal (the order of the families' overall size in this scope).
- 7 sentences were hit by more than one family; 5 needed a tie-break (`primary_tie_broken = yes` in the CSV).

## 4. Results

| Family | Primary | Any hit |
|---|---|---|
| Off-point reasons | 28 (46%) | 28 (46%) |
| Unearned or clashing premises | 20 (33%) | 22 (36%) |
| Thin or ill-fitting evidence | 9 (15%) | 9 (15%) |
| Stretched numbers | 2 (3%) | 7 (11%) |
| Shaky cause and effect | 2 (3%) | 3 (5%) |

Entry counts per family are in `summary.json` and in FLAGGED_PRO.md.

## 5. Mechanics, quotes and counters

- **Mechanics.** For each family, FLAGGED_PRO.md lists every entry the reviewers used, with its count, a link to the entry in the catalog at commit 2a56493 (`FALLACIES.md#<entry_id>`) and the catalog's own definition, copied verbatim. The one-line summary of each family is this audit's wording.
- **Quotes.** 2–4 per family, chosen by hand (the `PICKS` list in the script) from sentences that family hit. Picks favor 0-point sentences, meaning all three reviewers flagged them. The script checks each pick is in scope and hit by that family. It also checks that every sentence text in scope, quotes included, appears verbatim in `../../../articles/<slug>/snapshots/2026-10-01.txt`. Citation markers like `[4]` are part of the text.
- **Counters.** The catalog has no separate counter or rebuttal field, so counters come in two labeled parts:
  1. **From the catalog:** for the main entries in each family, one required condition and one legitimate look-alike, quoted verbatim from `catalog_entries_v0.6.1.json`. Which condition and look-alike are quoted is set by index in the script (`COUNTERS`). The logic is the catalog's: an entry applies only if all its required conditions hold, so the reply is to test the condition the flag rests on, and the look-alike says what a sound version of the step would look like.
  2. **This audit's wording:** a short plain reply, labeled as not from the catalog. It is about the reasoning move only. It adds no new factual claim about circumcision. Where it mentions a fact, the fact is in the quoted article sentence itself (antiretroviral therapy expansion, in the causal family).
- No source or citation was added in this step.

## 6. Limits

- **Flags are leads, not verdicts.** Each flag is an AI reviewer's judgment against the catalog. A flagged sentence can still have a true conclusion; the flag is about the step from reason to conclusion.
- **The reviewers were not blind.** Reviewers 2 and 3 started with instructions that mentioned earlier results (see the run README). That can raise the number of sentences flagged by two or three reviewers, and so affect which family wins a tie.
- **Sides were labeled by an AI model, not a person** (step 5: 9 separate model sessions split by article, no cross-checking). A sentence labeled differently would move in or out of this scope.
- **Family lines are soft.** The same move can sit in different categories depending on the entry chosen. Carrying HIV trial results from adult men to infant circumcision in general was named secundum quid (presumption) by Reviewer 1 and over-extrapolation (statistical) by Reviewer 3 on the same sentences. The primary-family rule then picks one. "Any hit" shows how much this matters: stretched numbers is primary for 3 sentences but named on 8.
- **Small numbers.** With 61 sentences, one sentence moves a share by about 1.6 points; the two smallest families have 2 sentences each as primary.
- **What gets flagged depends on the reviewers' rules.** Reported arguments ("critics argue…") were not flagged, so this covers the articles' own reasoning only.

## 7. File lineage and how to rebuild

```
../survival/survival_scores.csv (step 5) ─┐
../survival/flag_sentence_map.csv ────────┤
../flags.csv, ../reviewer2_flags.csv, ../reviewer3_flags.csv ─┤
catalog_entries_v0.6.1.json (from fallacy_catalog fallacies.json @ 2a56493) ─┤
../../../articles/<slug>/snapshots/2026-10-01.txt (verbatim check) ─┘
        └──► scripts/build_flagged_pro.py ──► flagged_pro.csv, summary.json, FLAGGED_PRO.md
flagged_pro.csv ──► tools/make_charts_2026_10_08.py ──► docs/img/circumcision/2026-10-08/06_flagged_pro_types.png
flagged_pro.csv + dependency/ (second layer, below) ──► dependency/scripts/build_dependency.py ──► 07_pro_after_priors.png
```

From the repo root (Python 3; the chart also needs matplotlib):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/scripts/build_flagged_pro.py
python3 tools/make_charts_2026_10_08.py
```

Deterministic: same inputs, same outputs.

## Second layer: dependence on flagged priors

Folder: [`dependency/`](dependency/). Write-up: [dependency/DEPENDENCIES.md](dependency/DEPENDENCIES.md).

**Question.** For each **survivor** (a male pro argument sentence with at least 1 point left in step 5: 951 sentences, 910 with 3 points, 26 with 2, 15 with 1), does its reasoning use one of the 61 flagged pro sentences above (the **priors**) as a premise?

**Rule.** A survivor loses 1 point for each distinct prior it depends on, down to 0. It depends on a prior if it builds on the prior's claim ("therefore", "thus"), refers back to it ("this", "these benefits", "as noted"), or relies on the same specific flagged claim. Topic overlap alone does not count. The full instructions are in [dependency/DEP_PROMPT.md](dependency/DEP_PROMPT.md).

**Pre-filter** (`dependency/scripts/dep_candidates.py`, deterministic, no model). Only pairs it finds are judged. A pair is a candidate if:

- **W (window):** same article, and the survivor sits from 2 sentences before to 8 sentences after the prior.
- **K (claim key):** the survivor matches the keyword patterns of a claim key, and a prior carries that key ([dependency/prior_claims.csv](dependency/prior_claims.csv); 16 keys over 44 priors, assigned by a model from the flag reasons; 17 priors have no key because their claim is specific to one passage). The survivor is paired with the nearest earlier prior with that key in the same article, else the nearest later one there, else the key's one representative prior (fewest points left, then article and sentence order). So a claim repeated across articles costs a survivor at most 1 point for that claim.

Result: 490 pairs (228 W only, 249 K only, 13 both; 164 cross-article), covering 344 of the 951 survivors.

**Recall limit.** The other 607 survivors were not judged against any prior. A survivor is missed if it relies on a flagged claim from outside the window and its wording does not match the keyword patterns, or if the prior it relies on has no claim key and sits outside the window. So the counts here are a lower bound on dependence, not a full count.

**Judging.** One model session ("model-1") judged all 490 pairs from the survivor, the sentence before it, and each prior's text and first flag reason. It did not open the score files. Each answer is Y or N; every Y has a one-line reason. Answers are in `dependency/work/judgments.csv` (resumable through `dependency/scripts/dep_queue.py`, which records answers under a file lock). Link type is set by the script: `same_article` when both sentences are in one article, else `same_claim`.

**Judgment calls** (written into DEP_PROMPT.md):

- A reported position ("The AAP concluded…", "Proponents argue…", "Critics contend…", "have been characterized as…") is N: the article is not adopting it as a premise.
- A survivor that is a premise *for* the prior (it comes before and feeds it) is N, unless it states the flagged claim itself.
- A survivor that is itself flagged is N when the only link is that it makes the same flagged claim: its own flag already cost it a point. It can still depend on a different prior by building on it or referring back to it (3 such cases).
- Sharing a general conclusion ("benefits outweigh risks") is N; only the specific flagged step counts.
- Uncertain is N. For example `c0410` (an article applying the adult trial result to khitan) was first recorded as Y and changed to N on re-reading. The file keeps the final answer only.

**Result.** 25 of the 490 pairs were judged Y, all in the same article as their prior (no cross-article same-claim link was judged Y). 25 survivors lost 1 point each; none depended on more than one prior. 19 of the 61 priors are relied on. Male pro points left, 3/2/1/0: 910/26/15/20 before, 888/47/14/22 after. See [dependency/summary.json](dependency/summary.json).

**Limits.**

- Each dependency is a **model's judgment, not a person's**, by one session with no second judge. Pairs near the line could go either way.
- **Flags are leads, not verdicts.** Losing a point here means the survivor rests on a step a reviewer flagged, not that it is wrong.
- The three reviewers were **not blind** (see above), so the set of priors carries that limit too.
- **Anti arguments were not checked** for dependence on flagged anti arguments: only 4 anti sentences in the male circumcision articles were flagged.
- Recall limit of the pre-filter, as stated above.

**Files.** `dependency/dependencies.csv` (one row per Y: candidate, survivor, prior, link_type, prefilter, reason, judged_by), `dependency/survivors_after_priors.csv` (all 951 survivors: points_before, n_priors, points_after, points_lost, flagged_itself, priors), `dependency/summary.json`, `dependency/DEPENDENCIES.md` (results, most relied-on priors, and every chain with verbatim quotes checked against the snapshots), `dependency/work/candidates.csv`, `dependency/work/judgments.csv`.

Rebuild from the repo root (the judging itself is the model step and is not rerun):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/dependency/scripts/dep_candidates.py
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/dependency/scripts/build_dependency.py
python3 tools/make_charts_2026_10_08.py
```

Chart: `docs/img/circumcision/2026-10-08/07_pro_after_priors.png`.


## Pass 3: fresh recheck of the remaining pro arguments

Folder: [`recheck/`](recheck/). Write-up: [recheck/RECHECK.md](recheck/RECHECK.md).

**Question.** Do the pro arguments that are left hold up? (Pass 1 is step 5's three reviewers; pass 2 is the dependence check above.) Every male pro argument sentence with at least 1 point after pass 2 is checked again, fresh, against fallacy_catalog v0.6.1 (commit `2a56493`), the same way the three reviewers flagged: the catalog's METHOD.md steps (a) to (g) and the reviewers' working rules (own voice only, reported views are no issue, factual slips are not fallacies, text-detectable entries only). Instructions: [recheck/RECHECK_PROMPT.md](recheck/RECHECK_PROMPT.md).

**Scope and order.** 949 sentences (`recheck/work/queue.csv`, deterministic): tier A, r0001–r0888, the 888 still at 3 points after pass 2, checked first; tier B, r0889–r0949, the 61 at 2 or 1 points (47 and 14).

**What the checker sees.** The sentence, its section headings, the three sentences before it and the one after it, and the article snapshot if it wants more. It does not see the earlier flags, the scores or the pass-2 results, and the queue output shows no points. The tier is visible only through the item number.

**Recording.** One line per finding: verdict (`flag`, `possible_issue` or `no_issue`), catalog entry id, the exact quoted words and a one-line reason. `recheck/scripts/recheck_queue.py` rejects quotes that are not an exact substring of the sentence and ids that are not text-detectable catalog entries (`recheck/catalog_ids_v0.6.1.json`). It is resumable, safe for parallel checkers (file lock), and `batches K` splits what is left into id ranges.

**Scoring.** Each distinct entry with verdict `flag` costs 1 point, starting from the points after pass 2, floor 0. `possible_issue` is recorded and costs nothing. In tier B, an entry that a step-5 reviewer already flagged on the same sentence is not counted again.

**Who checked.** Five model sessions (checker-1 to checker-5), 189–190 items each, all 949 items. They ran from a conversation that already knew the earlier results. Each was told not to open the flag files, scores or pass-2 results, but because of where they started, this pass is **not blind**. The checkers shared the box's /tmp folder, and one helper file there was overwritten by another session. Answers were recorded only through `recheck_queue.py`, which validates each line against the queue, the sentence and the catalog, so the overwrite did not affect the recorded answers.

**Result.** Lines recorded: 12 flag, 39 possible issue, 900 no issue. 4 flags were not counted (tier B, same entry a step-5 reviewer had already flagged). 8 sentences lost 1 point each: 5 of the 888 still at 3 points and 3 of the 61 in tier B. Entries counted: false analogy 3, red herring 3, secundum quid 2.

| Male pro points left | 3 | 2 | 1 | 0 | All 3 points |
|---|---|---|---|---|---|
| Step 5 | 910 | 26 | 15 | 20 | 93.7% |
| After pass 2 | 888 | 47 | 14 | 22 | 91.5% |
| After pass 3 | 883 | 50 | 15 | 23 | 90.9% |
| Anti, step 5 (not rechecked) | 724 | 2 | 2 | 0 | 99.5% |

**Pro only.** Anti arguments were checked only in step 5. They were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro.

The 3 tier-B dings all fall on sentences that had already lost a point for what reads as the same flaw: circumcision-and-law s0102 and views-on-circumcision s0098 were flagged as irrelevant conclusion in step 5 and as red herring here, and ethics-of-circumcision s0107 lost a point in pass 2 for depending on the heel-prick analogy and is flagged here as false analogy for the same analogy. The rule as written does not merge these. Without them pass 3 would end at 883/52/14/22, and the count at full points would not change.

**Limits.** Model judgment, not a person's. A fresh check by one model is a different read from the three reviewers', so a new flag can reflect reader variation as much as a missed flaw. Tier B checkers could guess that those sentences lost points before (the item range). Synonym entries (for example secundum quid and over-extrapolation) are not merged when applying the tier-B rule. Flags are leads, not verdicts. Anti arguments are not rechecked.

Rebuild from the repo root (the checking itself is the model step and is not rerun):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/recheck/scripts/build_recheck.py
python3 tools/make_charts_2026_10_08.py
```

Outputs: `recheck/findings.csv` (every line, with quote, entry, reason, whether it counted, earlier points lost, checker), `recheck/points_by_pass.csv` (all 971 male pro sentences: points at step 5, after pass 2, after pass 3), `recheck/summary.json`, `recheck/RECHECK.md`. Chart 07 shows step 5, after pass 2 and after pass 3, with anti for reference.

## What the surviving pro arguments rely on (topic tags)

Folder: [`topic_tags/`](topic_tags/). Write-up: [topic_tags/TAGS.md](topic_tags/TAGS.md). Chart: `docs/img/circumcision/2026-10-08/08_what_survivors_rely_on.png`.

**Question.** Of the pro arguments that kept all 3 points after pass 3, how many rest on medical data? Scope: the 883 male circumcision pro argument sentences with 3 points in `recheck/points_by_pass.csv`.

**Tags.** Each sentence gets exactly one type for what it relies on to make its point: M (medical or scientific data), E (ethics, rights or law), R (religion, culture or tradition) or O (other, mixed or framing). Definitions, tie-break rules and invented examples: [topic_tags/TAG_PROMPT.md](topic_tags/TAG_PROMPT.md). The queue (`topic_tags/work/queue.csv`, `scripts/tag_queue.py`) showed each sentence with its article title, section and two sentences on each side, and no points or flags. Answers were validated and recorded under a file lock.

**Who tagged.** Four separate AI model sessions, one per range: tagger-1 t0001–t0221, tagger-2 t0222–t0442, tagger-3 t0443–t0663, tagger-4 t0664–t0883. They ran from a conversation that already knew the earlier results of this audit, so the tagging is **not blind**. Tagger-4 read `work/tags.csv` (which held the other taggers' answers) after it had finished and recorded its own range, so its own answers were already recorded when it saw the others. This is noted for transparency.

**Result.** M 667 (75.5%), R 105 (11.9%), E 72 (8.2%), O 39 (4.4%).

**Cross-check.** `build_topic_tags.py` also tags every sentence by keyword counts (a regex per type; most hits wins; none or a tie gives O). It is a rough ballpark with no model: M 628, R 112, E 49, O 94. The keyword tag matched the model's tag for 82.4% of sentences.

**Limits.** Model judgment, not a person's, not blind. One type per sentence, so sentences that mix two kinds of support are forced into one type. Ranges follow article order, so differences between taggers mix article content with tagger habits. Scope is male circumcision pro arguments with all 3 points after pass 3 only. A tag says what an argument rests on, not whether it is right.

Rebuild from the repo root (the tagging itself is the model step and is not rerun):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/topic_tags/scripts/build_topic_tags.py
python3 tools/make_charts_2026_10_08.py
```

## Columns of flagged_pro.csv

`article`, `sentence_id` (as in step 5), `topic_group` (always male here), `points_left` (0–2), `reviewers` (R1|R2|R3, those that flagged it), `primary_family`, `families` (every family named), `primary_tie_broken` (yes/no), `entries` (reviewer: entry_id, one per mapped flag), `entry_names`, `text` (verbatim sentence).

## What-if checks: do the medical arguments rest on the HIV/STI or cancer claims?

Folders: [`sti_dependence/`](sti_dependence/) and [`cancer_dependence/`](cancer_dependence/). Write-ups: [sti_dependence/STI_DEPENDENCE.md](sti_dependence/STI_DEPENDENCE.md), [cancer_dependence/CANCER_DEPENDENCE.md](cancer_dependence/CANCER_DEPENDENCE.md). Charts: `docs/img/circumcision/2026-10-08/09_sti_dependence.png`, `10_what_if_removed.png`.

**What-if, not a finding.** Each pass asks how many medical arguments would lose their point if one claim were set aside. A tag means "depends on the claim", not that the claim is wrong. This audit did not check the HIV/STI claim or the cancer claim. Penile cancer is rare in absolute terms, but how much a rare benefit should weigh is a question this audit does not settle.

**HIV/STI pass.** Scope: all 667 sentences tagged M (medical or scientific data) in `topic_tags/`; no keyword prefilter. Tags: H (the point rests on protection against HIV or another sexually transmitted infection, including partner or community transmission), X (rests on a non-STI medical claim), N (medical in form, no benefit relied on; note required). A sentence combining HIV/STI with another benefit is H only if no medical point is left without the HIV/STI part. Instructions: [sti_dependence/SIDEIDEA_PROMPT.md](sti_dependence/SIDEIDEA_PROMPT.md). Recall limit: arguments tagged E, R or O in `topic_tags/` were not checked, even if they mention HIV.

**Cancer pass.** Scope: the same 667, prefiltered to the 210 whose own text or the two prose sentences on either side name cancer, carcinoma, malignancy, tumour, neoplasia, HPV, papillomavirus or cervical (82 name a keyword themselves). Tags: C (rests on a cancer-prevention claim: penile cancer, or cervical cancer in partners via HPV), K (rests on a non-cancer claim), N (mentions cancer, not relied on as a benefit; note required). A sentence combining cancer with another benefit is C only if no point is left without the cancer part. Instructions: [cancer_dependence/CANCER_PROMPT.md](cancer_dependence/CANCER_PROMPT.md). Recall limit: a sentence that relies on cancer through "these benefits" is caught only if a keyword sits inside the window; the other 457 medical sentences count as not resting on cancer.

**Who tagged.** HIV/STI: three AI model sessions (h0001–h0223, h0224–h0446, h0447–h0667). Cancer: two AI model sessions (p0001–p0105, p0106–p0210). All ran from a conversation that already knew the earlier results of this audit, so the tagging is **not blind**. Each was told not to open earlier tags, flags or scores, or to search the web. Answers were recorded through the queue scripts (file lock, validation).

**Results.**

| Pass | Tag | Count | Share |
|---|---|---|---|
| HIV/STI (667) | H | 254 | 38.1% |
| | X | 399 | 59.8% |
| | N | 14 | 2.1% |
| Cancer (210 prefiltered) | C | 35 | 16.7% |
| | K | 174 | 82.9% |
| | N | 1 | 0.5% |

8 of the 35 C sentences are also H. Medical arguments resting on the HIV/STI claim or the cancer claim: 254 + 27 = **281**, 42.1% of the 667 medical arguments and 31.8% of all 883 surviving pro arguments. The other 386 medical arguments rest on neither.

**Cross-checks** (regex, no model). Naming HIV or an STI matched the H tag for 81.3% of the 667. Naming cancer matched the C tag for 80.5% of the 210.

**Limits.** AI-tagged, not by a person, and not blind. One tag per sentence. HIV/STI tagger shares differ a lot (49%, 39% and 26% H), partly because ranges follow article order (circumcision-and-hiv falls in the first range) and partly, perhaps, from tagger habits. The cancer prefilter can miss sentences, as stated above. The idea for these passes came from two posts on X that cite no study (see the walkthrough); this audit takes no position on them.

Rebuild from the repo root (the tagging itself is the model step and is not rerun):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/sti_dependence/scripts/build_sti_dependence.py
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/cancer_dependence/scripts/build_cancer_dependence.py
python3 tools/make_charts_2026_10_08.py
```

## Total what-if: how much of the pro side is left?

Folder: [`whatif_total/`](whatif_total/). Write-up: [whatif_total/TOTAL_WHATIF.md](whatif_total/TOTAL_WHATIF.md). Chart: `docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png`.

**Question.** Jason asked how much of the pro side is invalidated if three premises are taken as true: (1) no protection against HIV or other STDs; (2) STD rates are higher in circumcising countries; (3) cancer prevention is not a valid reason. What-if, not a finding. Premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias; this audit did not check either side, so the result holds only if the premises hold. Premise 2 is not counted separately: any argument resting on HIV/STI protection is already set aside under premise 1.

**Counting.** All 971 male pro arguments from step 5, each in one group only, in this order: already flagged (lost 1+ point at step 5, pass 2 or pass 3, from `recheck/points_by_pass.csv`); tagged M and H (HIV/STI); tagged M and C (cancer only); otherwise not invalidated, split by topic tag. Earlier results are not changed. `scripts/build_whatif_total.py` writes `summary.json` and `TOTAL_WHATIF.md`.

**Result.** Already flagged 88 (9.1%; first lost a point at step 5: 61, pass 2: 22, pass 3: 5). What-if 281 (28.9%; HIV/STI 254, cancer only 27). Not invalidated 602 (62.0%; other medical 386, religion or culture 105, ethics or law 72, other 39).

**Non-medical recall check.** The 216 E, R and O survivors were never put through the HIV/STI or cancer passes. A word-bounded keyword check finds 14 (6.5%) that name HIV, an STI or cancer: a rough upper bound, since naming a term is not resting on it. Because that is under 60, one AI model session checked them with a written prompt ([`whatif_total/keyword_check/CHECK_PROMPT.md`](whatif_total/keyword_check/CHECK_PROMPT.md)); the session ran from a conversation that already knew the earlier results, so it is not blind. It found 2 that rest on the HIV claim (both in `circumcision-in-africa`). They are reported separately, not added; adding them would make the what-if group 283 (29.1%). Non-medical sentences that lean on these claims without naming them are not found.

**Keyword regex note.** The HIV/STI keyword regex used in `sti_dependence/` lacks a closing word boundary, so it also matches words such as "stigma" and "stipulated". This page uses a word-bounded version. Rerun on the 667, the fixed version moves the HIV/STI cross-check from 81.3% to 81.4% matched; the earlier figure is left as committed.

Rebuild from the repo root:

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/whatif_total/scripts/build_whatif_total.py
python3 tools/make_charts_2026_10_08.py
```
