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
```

From the repo root (Python 3; the chart also needs matplotlib):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/scripts/build_flagged_pro.py
python3 tools/make_charts_2026_10_08.py
```

Deterministic: same inputs, same outputs.

## Columns of flagged_pro.csv

`article`, `sentence_id` (as in step 5), `topic_group` (always male here), `points_left` (0–2), `reviewers` (R1|R2|R3, those that flagged it), `primary_family`, `families` (every family named), `primary_tie_broken` (yes/no), `entries` (reviewer: entry_id, one per mapped flag), `entry_names`, `text` (verbatim sentence).
