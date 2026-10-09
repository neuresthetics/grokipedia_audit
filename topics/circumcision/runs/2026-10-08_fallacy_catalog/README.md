# Circumcision articles: fallacy_catalog run (2026-10-08)

**Plain-language analysis and charts:** [ANALYSIS.md](ANALYSIS.md).

## What was done

- **Input:** the 58 article snapshots already saved in this repo (`articles/<slug>/snapshots/2026-10-01.txt`). Nothing was fetched again.
- **Checklist:** [neuresthetics/fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1, commit `2a56493a3931018e9143bc7235f152f5cc5b459e`, used with its METHOD.md.
- **Model judging:** Three separate AI agents each read all 58 articles and wrote their own flags. Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, and each reports it did not, but their instructions came from a conversation that had already discussed earlier results (Reviewer 2: Reviewer 1's totals, top articles and fallacy types; Reviewer 3: counts and example quotes from Reviewers 1 and 2), so they were not blind. Reviewer 1 is the only fully uninfluenced read. (See "Second reviewer and overlap" and "Third reviewer and three-way overlap".)
- **Survival scoring (step 5 of this benchmark):** after the reasoning check, every sentence was labeled pro, anti or not an argument by an AI model, and each argument was scored 3 points minus 1 for each reviewer that flagged it. See "What survived" below and [survival/METHOD.md](survival/METHOD.md).
- **Flagged pro arguments (step 6 of this benchmark, male circumcision articles only):** the 61 pro arguments in the male circumcision articles that lost at least one point are sorted by fallacy family, the catalog's own categories, with mechanics, verbatim quotes and counters. A second layer takes 1 point from each surviving pro argument for each flagged one it depends on, and a third pass rechecks the remaining pro arguments against the catalog. FGM articles are not part of this step. See "Flagged pro arguments" below and [flagged_pro/METHOD.md](flagged_pro/METHOD.md).
- **Date:** 2026-10-08.

Every article was read in full, in 174 chunks. For a passage to be flagged, it had to be the article's own reasoning, read in its strongest form. It also had to meet every required condition of the most specific catalog entry, and the reviewer ruled out that entry's look-alikes. Arguments the article only reports are not flagged.

Reviewer 1's read used no earlier run's flags and no "substance lens" (now retired) as input. The comparison with earlier runs at the bottom was made after the read was finished.

Every quote in `flags.csv` was checked by script against the snapshot text. All 87 match exactly, and none had to be dropped.

A separate script counted citations per article. It uses only the saved snapshot and its sources list.

## Files

| File | What it is |
|---|---|
| `ANALYSIS.md` | Plain-language analysis of the three reviews, with charts (drawn by `tools/make_charts_2026_10_08.py`) |
| `flagged_pro/` | Step 6: the flagged pro arguments in the male circumcision articles by type, with mechanics, quotes and counters; `dependency/` holds the second layer, survivors that depend on them; `recheck/` holds pass 3, a fresh recheck of the remaining pro arguments; `topic_tags/` tags what the surviving pro arguments rely on (see "Flagged pro arguments" below) |
| `survival/` | What survived: argument sentences scored 3 minus the number of reviewers that flagged them (see "What survived" below) |
| `flags.csv` | One row per flag. Columns: `slug`, `quote` (exact text), `entry_id`, `entry_name`, `reason`, `favors` (pro / anti / neutral), `confidence`, `verdict` |
| `citation_stats.csv` | Citation counts per article (column meanings in `scripts/citation_stats.py`) |
| `scripts/split_units.py` | Splits a snapshot into headings, paragraphs, table rows and sentences |
| `scripts/citation_stats.py` | Writes `citation_stats.csv` |
| `scripts/make_chunks.py`, `scripts/next_chunk.sh` | Cut the articles into the 174 reading chunks and serve them in order |
| `scripts/entry.py` | Prints a catalog entry's conditions and look-alikes |
| `scripts/add_flag.py` | Records a flag. Rejects quotes that are not exact substrings, and unknown entry ids |
| `scripts/verify_quotes.py` | Re-checks every quote and drops any that fail. Result: 87 checked, 0 failed |
| `scripts/build_flags.py` | Builds `flags.csv` from the verified rows and prints the counts below |
| `scripts/flags_raw.jsonl`, `scripts/flags_verified.jsonl` | The reviewer's recorded rows, before and after the check |
| `scripts/reading_notes.md` | The working rules applied on top of METHOD.md |

To rebuild, run `python3 scripts/verify_quotes.py && python3 scripts/build_flags.py`.

## Results

**87 rows: 86 flags and 1 possible issue.**

- **By side:** 53 pro (61%), 23 anti (26%), 11 neutral (13%).
- **By confidence:** 1 high, 55 medium, 31 low.
- **Articles with at least one row:** 37 of 58.

What "side" means depends on the article group:

| Group | Articles flagged | Rows | Pro | Anti | Neutral |
|---|---|---|---|---|---|
| Male circumcision (pro = favours the practice) | 21 | 53 | 42 | 7 | 4 |
| FGM (anti = against the practice; pro = defends it or plays down harm) | 16 | 34 | 11 | 16 | 7 |

### By fallacy

| Entry | Rows |
|---|---|
| inconsistency | 14 |
| non-sequitur | 11 |
| bulverism | 9 |
| false-cause | 9 |
| secundum-quid | 8 |
| straw-man | 6 |
| false-analogy | 4 |
| irrelevant-conclusion | 4 |
| cherry-picking | 3 |
| double-standard | 2 |
| hasty-generalization | 2 |
| unrepresentative-sample | 2 |

Thirteen other entries were used once each: observational-interpretation, appeal-to-authority, appeal-to-the-people, post-hoc, mcnamara-fallacy, nut-picking, circumstantial-ad-hominem, relative-risk-framing, argument-from-silence, begging-the-question, base-rate-fallacy, persuasive-definition and appeal-to-tradition.

### By article (articles with at least one row)

| Article | Rows | Pro | Anti | Neutral |
|---|---|---|---|---|
| circumcision-controversies | 7 | 7 | 0 | 0 |
| women-unaffected-by-female-genital-cutting | 7 | 7 | 0 | 0 |
| ethics-of-circumcision | 6 | 6 | 0 | 0 |
| ulwaluko | 5 | 5 | 0 | 0 |
| ashley-montagu-resolution | 4 | 1 | 1 | 2 |
| circumcision | 4 | 4 | 0 | 0 |
| prohibition-of-female-circumcision-act-1985 | 4 | 1 | 3 | 0 |
| views-on-circumcision | 4 | 4 | 0 | 0 |
| brit-milah | 3 | 3 | 0 | 0 |
| circumcision-in-africa | 3 | 3 | 0 | 0 |
| female-genital-mutilation | 3 | 2 | 0 | 1 |
| forced-circumcision | 3 | 0 | 3 | 0 |
| prevalence-of-female-genital-mutilation | 3 | 0 | 2 | 1 |
| female-genital-mutilation-act-2003 | 2 | 0 | 2 | 0 |
| female-genital-mutilation-in-new-zealand | 2 | 0 | 1 | 1 |
| female-genital-mutilation-in-nigeria | 2 | 0 | 0 | 2 |
| female-genital-mutilation-in-the-united-states | 2 | 0 | 1 | 1 |
| mohel | 2 | 2 | 0 | 0 |
| religious-views-on-female-genital-mutilation | 2 | 0 | 1 | 1 |
| restoration-device | 2 | 0 | 2 | 0 |
| circumcision-and-hiv | 1 | 1 | 0 | 0 |
| circumcision-and-law | 1 | 1 | 0 | 0 |
| clitoridectomy | 1 | 0 | 1 | 0 |
| cultural-views-on-circumcision-aesthetics | 1 | 0 | 0 | 1 |
| female-genital-mutilation-in-india | 1 | 1 | 0 | 0 |
| female-genital-mutilation-in-the-gambia | 1 | 0 | 1 | 0 |
| female-genital-mutilation-laws-by-country | 1 | 0 | 1 | 0 |
| forced-circumcision-of-minors-in-south-korea | 1 | 0 | 0 | 1 |
| foreskin | 1 | 1 | 0 | 0 |
| gishiri-cutting | 1 | 0 | 1 | 0 |
| infibulation | 1 | 0 | 1 | 0 |
| international-day-of-zero-tolerance-for-female-genital-mutilation | 1 | 0 | 1 | 0 |
| khitan-circumcision | 1 | 1 | 0 | 0 |
| meatal-stenosis | 1 | 0 | 1 | 0 |
| phimosis | 1 | 1 | 0 | 0 |
| prevalence-of-circumcision | 1 | 1 | 0 | 0 |
| religion-and-circumcision | 1 | 1 | 0 | 0 |

These 21 articles had no rows: brit-shalom-naming-ceremony, children-act-1989-amendment-female-genital-mutilation-act-2019, circumcision-controversy-in-early-christianity, circumcision-in-brunei, circumcision-in-china, circumcision-in-the-bible, circumcision-of-jesus, circumcision-surgical-procedure, cost-of-circumcision-surgery-in-chaozhou, feast-of-the-circumcision-of-christ, female-genital-mutilation-in-sudan, female-genital-mutilation-in-the-united-kingdom, foreskin-man, foreskin-restoration, history-of-circumcision, holy-prepuce, lipodermos, paraphimosis, penile-subincision, redundant-prepuce and stapler-circumcision.

### Citation counts

Across the 58 articles there are 13,199 prose sentences. Of these, 4,658 (35.3%) carry no `[n]` marker. The median article is at 35.1%, and most articles fall between about 24% and 40%.

- **Most uncited sentences:**
  - circumcision-in-brunei 54.4%
  - stapler-circumcision 52.4%
  - female-genital-mutilation 51.9%
  - cost-of-circumcision-surgery-in-chaozhou 50.6%
  - feast-of-the-circumcision-of-christ 48.4%
- **Broken source lists:**
  - female-genital-mutilation lists 3 sources but uses markers up to [76]. 153 markers point past the list.
  - views-on-circumcision lists 2 sources but uses markers up to [114]. 139 markers point past the list.
  - For these two articles, the saved sources list does not match the text.
- **Bracketed years read as citations:** a few markers past the list are years in brackets (such as [2019]) that the site turns into reference links:
  - circumcision-surgical-procedure 8
  - holy-prepuce 2
  - 1 each in children-act-2019, circumcision, circumcision-and-law and female-genital-mutilation-in-india
- **Listed sources never cited in the text:**
  - stapler-circumcision 6
  - feast-of-the-circumcision-of-christ 5
  - circumcision-in-china 4
  - paraphimosis 4
  - redundant-prepuce 4
  - circumcision-in-brunei 3
  - 13 articles have at least one such source.

## Caveats

- **Three AI reviewers, not humans.** A second and a third reviewer were added (see below). The 74 passages flagged for the same side by at least two reviewers, and the 25 flagged for the same side by all three, are the strongest leads. The three runs share the same catalog and method, so their mistakes may be shared; overlap shows consistency, not that a flag is correct. Treat each row as a lead to check, not a verdict.
- **Not blind.** Three separate AI agents each read all 58 articles and wrote their own flags. Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, and each reports it did not, but their instructions came from a conversation that had already discussed earlier results (Reviewer 2: Reviewer 1's totals, top articles and fallacy types; Reviewer 3: counts and example quotes from Reviewers 1 and 2), so they were not blind. Reviewer 1 is the only fully uninfluenced read. Overlap between readers may be partly inflated by that, so the "flagged by at least two" and "flagged by all three" rows are best read as consistency of separate reads, not as confirmation from uninfluenced readers.
- **Fewer flaws is not being right.** A side with fewer flags is argued more cleanly in these articles. That says nothing about whether its conclusion is correct.
- **Conservative by design.** Reported arguments, sections titled as one side's case, and loaded wording were not flagged (see `scripts/reading_notes.md`). An article can read as one-sided and still have few or no rows.
- **Side is a judgement call.** It records which side the faulty step helps. It does not record what the article as a whole argues.
- **Not counted:** factual slips (wrong figures, dates and the like) are not fallacies, so they are not in `flags.csv`.
- **Citation counts are approximate:**
  - Sentence splitting is rule-based.
  - Bracketed years inflate the "beyond the list" counts slightly.
  - The two broken source lists make those articles' citation counts unreliable.
- **Snapshot date.** All text is from the 2026-10-01 snapshots. The live pages may have changed since.

## Compared with the retired run 2 (done after the read)

Run 2 used the retired substance lens and found 225 flags (154 pro, 49 anti, 22 neutral; 68% pro) across 47 articles. This run found 87 rows (61% pro) across 37 articles. The new method is much stricter, but the lean is in the same direction.

36 articles were flagged in both runs. Nine of run 2's ten most-flagged articles are also among this run's most flagged (3 or more rows):
- ethics-of-circumcision
- circumcision-controversies
- circumcision
- women-unaffected-by-female-genital-cutting
- circumcision-in-africa
- views-on-circumcision
- forced-circumcision
- prohibition-of-female-circumcision-act-1985
- ulwaluko

The tenth, circumcision-and-law, had 8 flags in run 2 and 1 here. Flags were not matched one by one, because the two runs use different labels.

## Second reviewer and overlap

After the first read, a second reviewer read all 58 snapshots again. It used the same catalog commit and METHOD.md. It was told not to open `flags.csv`, this README or any earlier run until its own file was saved, and it reports that it did not. It was not blind: its instructions were written in a conversation that had already seen Reviewer 1's totals, top articles and fallacy types. Both reviewers were general-purpose AI agents in separate runs. Neither was a human.

- **Files:**
  - `reviewer2_flags.csv`: the second reviewer's rows. The columns match `flags.csv`, and every quote was checked by script against the snapshot.
  - `scripts/compare_reviewers.py`: the comparison script. It writes `agreement.csv` (despite the file name, it simply lists the passages flagged by both reviewers: matched pairs with each reviewer's entry and side), `per_article_counts.csv` and `agreement_summary.md` (a summary of the overlap).
- **How flags were matched:** two rows match when they are on the same article and their quotes overlap in the snapshot. Each row is matched to at most one other row.
- **Totals:**
  - Reviewer 1: 87 rows (53 pro, 23 anti, 11 neutral).
  - Reviewer 2: 64 rows (42 pro, 8 anti, 14 neutral) across 28 articles. Reviewer 2 marked 52 of its rows "possible issue" and 12 "flag".
- **Overlap:** 41 matched pairs, 46 rows found only by reviewer 1 and 23 found only by reviewer 2. That is about half of reviewer 1's rows and about two thirds of reviewer 2's.
- **Within the matched pairs:**
  - Same side: 36 of 41.
  - Same catalog entry: 20 of 41.
  - Another 10 pairs used closely related entries: bulverism / appeal to motive, false cause / cum hoc, secundum quid / over-extrapolation, and argument from silence / argument from ignorance. METHOD.md counts all of these as "label disputed".
- **Flagged by both, same side:** 36 passages were flagged by both reviewers with the same side: 27 pro, 6 neutral and 3 anti. With the third reviewer added, the passages flagged for the same side by at least two of the three reviewers are now the strongest leads (see the next section). They are listed in `agreement.csv`, where `same_side` is True.
- **Per-article counts:** Spearman correlation across the 58 articles is 0.77. The articles ethics-of-circumcision, circumcision-controversies and women-unaffected-by-female-genital-cutting are the three most-flagged articles for both reviewers.
- **Lean:** 26 articles were flagged by both reviewers. On 20 of them, both reviewers gave the same lean (more pro rows, more anti rows, or even).
- **What this shows:** in separate runs, where the two reviewers flagged the same passage they mostly gave it the same side. They chose the same catalog entry much less often, and each one found rows the other missed. Reviewer 2 found fewer anti-side rows (8 against 23), and that accounts for most of the gap in side split. The overall lean is pro in both.
- **Limits:**
  - The two runs share the same catalog and method, and Reviewer 2's instructions mentioned Reviewer 1's results, so overlap may be partly inflated.
  - Reviewer 2 read text with citation markers removed, and quotes were mapped back to the snapshot afterwards.
  - Overlap here measures consistency between the reviewers. It does not show that a flag is correct.

## Third reviewer and three-way overlap

A third reviewer then read all 58 snapshots. It used the same catalog commit and METHOD.md. It was told not to open `flags.csv`, `reviewer2_flags.csv`, the comparison files, ANALYSIS.md, the charts or any earlier run until its own file was saved, and it reports that it did not. It was not blind: its instructions came from a conversation that had already discussed counts and example quotes from Reviewers 1 and 2. It was also a general-purpose AI agent, not a human. Unlike Reviewer 2, it read the snapshot text with citation markers left in, so its quotes needed no mapping.

- **Files:**
  - `reviewer3_flags.csv`: the third reviewer's rows, same columns as `flags.csv`. Every quote was checked by script against the snapshot: 121 checked, 0 failed, none dropped.
  - `scripts/reviewer3/`: its working files (`flags.jsonl`, `done.txt`, the helper scripts, `build_reviewer3.py` to re-check quotes and rebuild the CSV, and `NOTES.md`).
  - `scripts/compare_reviewers.py` now compares all three. It still writes `agreement.csv` (Reviewers 1 and 2, unchanged), and adds `overlap_r1_r3.csv`, `overlap_r2_r3.csv`, `overlap_pairwise.csv` (one summary row per pair) and `overlap_3way.csv` (one row per passage). `per_article_counts.csv` and `agreement_summary.md` now cover three reviewers.
- **Totals:**
  - Reviewer 3: 121 rows (59 pro, 39 anti, 23 neutral) across 45 articles. It marked 79 rows "flag" and 42 "possible issue"; confidence was medium for 82, low for 37 and high for 2.
  - Most used entries: inconsistency 30, non-sequitur 20, bulverism 11, cum hoc 10, false cause 9.
  - Most flagged articles: ethics-of-circumcision 10, circumcision-controversies 7, female-genital-mutilation 7, women-unaffected-by-female-genital-cutting 6.
- **Pairwise overlap** (same method as above: same article, overlapping quotes, each row matched at most once):

| Pair | Matched | Only first / only second | Same side | Same catalog entry | Near-twin entry |
|---|---|---|---|---|---|
| 1 and 2 | 41 | 46 / 23 | 36 of 41 | 20 of 41 | 10 |
| 1 and 3 | 57 | 30 / 64 | 53 of 57 | 39 of 57 | 7 |
| 2 and 3 | 43 | 21 / 78 | 35 of 43 | 28 of 43 | 6 |

- **Three-way passages:** overlapping quotes from any of the three reviewers in the same article are joined into one passage. In this run no passage holds more than one row per reviewer, and in every passage flagged by all three, all three quotes overlap each other directly.
  - 164 passages in all: 22 flagged only by Reviewer 1, 13 only by Reviewer 2, 54 only by Reviewer 3, 8 by Reviewers 1 and 2 only, 24 by 1 and 3 only, 10 by 2 and 3 only, and 33 by all three.
  - **Flagged by at least two, same side:** 74 passages (45 pro, 18 anti, 11 neutral). At least two of the reviewers gave the same catalog entry in 54 of them.
  - **Flagged by all three, same side:** 25 passages (22 pro, 1 anti, 2 neutral).
  - By group: male circumcision 38 pro, 5 anti, 3 neutral flagged by at least two (18 pro flagged by all three); FGM 7 pro, 13 anti, 8 neutral flagged by at least two (4 pro, 1 anti, 2 neutral by all three).
- **Per-article counts:** Spearman correlation across the 58 articles is 0.77 for Reviewers 1 and 3 and 0.72 for Reviewers 2 and 3 (0.77 for 1 and 2).
- **Lean:** 36 articles were flagged by both Reviewers 1 and 3, and 31 of them got the same lean from both; 28 were flagged by both Reviewers 2 and 3, 20 with the same lean. 26 articles were flagged by all three, 18 with the same lean from all three.
- **What this adds:** Reviewer 3's flags overlap most with Reviewer 1's (two thirds of Reviewer 1's flags were also flagged by Reviewer 3, 93% of those with the same side). In male circumcision articles Reviewer 3 shows the same strong pro lean as the others. In FGM articles it found many more anti-side flags (31) than Reviewer 1 (16) or Reviewer 2 (7); only 12 of those 31 were also flagged for the anti side by another reviewer. Reviewer 3 also flagged 54 passages no one else did.
- **Limits:**
  - The three runs share the same catalog and method, and Reviewers 2 and 3 were started with instructions that mentioned earlier results, so overlap may be partly inflated. Reviewer 1 is the only fully uninfluenced read.
  - Overlap measures consistency between the reviewers. It does not show that a flag is correct. Flags are leads.
  - Fewer flaws on one side means that side is argued more cleanly in these articles, not that its conclusion is right.
  - The third reviewer's task description came from a conversation that had already discussed the earlier results (some counts and example quotes). It was told to disregard them and reports that it did not open any of the earlier files, but it was not blind. Identical quotes are common because reviewers tend to quote the same clause: 44 of Reviewer 3's 57 matches with Reviewer 1 use word-for-word the same quote (77%), close to the 32 of 41 (78%) between Reviewers 1 and 2 (Reviewers 2 and 3: 26 of 43, 60%). Reviewer 2's instructions also mentioned earlier results, so this comparison cannot show whether that influence raised the overlap.

## What survived (argument survival scoring)

Folder: [`survival/`](survival/). Every prose sentence that argues for or against the practice starts with 3 points and loses 1 point for each reviewer whose flag quote overlaps it. The overlap test is the same one `scripts/compare_reviewers.py` uses: same article, overlapping character span.

All 13,199 sentences were labeled pro, anti or not an argument by an AI model, not a person. The labeling ran in 9 separate model sessions split by article, following [`survival/LABEL_PROMPT.md`](survival/LABEL_PROMPT.md). The labelers never saw the reviewer flags. Survival means "not flagged", not "true".

- [`survival/SURVIVORS.md`](survival/SURVIVORS.md): summary counts, plus the arguments left with 2, 1 or 0 points, verbatim, with their article and the catalog entries that hit them. The untouched (3-point) arguments are in `survival/SURVIVORS_3_points_<side>_<group>.md`.
- [`survival/METHOD.md`](survival/METHOD.md): labeling, matching, scoring, conflict handling, a consistency check by labeler, limits and how to rebuild.
- Data: `survival/labels/model_labels.csv`, `survival/sentence_labels.csv`, `survival/argument_inventory.csv`, `survival/survival_scores.csv`, `survival/flag_sentence_map.csv`, `survival/conflicts.csv`, `survival/summary.json`. Scripts are in `survival/scripts/`.
- Chart: `docs/img/circumcision/2026-10-08/05_what_survived.png`.

Headline, share of argument sentences no reviewer flagged:

| Articles | Pro | Anti |
|---|---|---|
| Male circumcision | 93.7% of 971 | 99.5% of 728 |
| FGM | 96.7% of 301 | 97.7% of 616 |

In the FGM articles, the order of the two sides flips when flagged claims about laws and campaigns are counted as arguments. See METHOD.md, section 7.

## Flagged pro arguments (step 6, male circumcision articles only)

Folder: [`flagged_pro/`](flagged_pro/). This step covers the male circumcision articles only; FGM articles are not part of it. It takes the 61 pro argument sentences there with fewer than 3 points left in step 5. It sorts them by the fallacy_catalog v0.6.1 entries the reviewers cited, rolled up to the catalog's own categories. Each sentence gets one primary family (the one the most reviewers named), so the shares add to 100%.

| Family (catalog category) | Flagged pro sentences |
|---|---|
| Off-point reasons (relevance) | 28 (46%) |
| Unearned or clashing premises (presumption) | 20 (33%) |
| Thin or ill-fitting evidence (weak induction) | 9 (15%) |
| Stretched numbers (statistical and probabilistic) | 2 (3%) |
| Shaky cause and effect (causal) | 2 (3%) |

- [`flagged_pro/FLAGGED_PRO.md`](flagged_pro/FLAGGED_PRO.md): for each family, how the move works (with the catalog's definitions and links), verbatim quotes, and the counter. Counters quote the catalog's required conditions and legitimate look-alikes; any added reply is marked as this audit's wording.
- [`flagged_pro/METHOD.md`](flagged_pro/METHOD.md): scope, rollup and primary-family rules, quote checks, how the counters were sourced, limits and how to rebuild.
- Data: `flagged_pro/flagged_pro.csv`, `flagged_pro/summary.json`, `flagged_pro/catalog_entries_v0.6.1.json`. Script: `flagged_pro/scripts/build_flagged_pro.py`.
- Chart: `docs/img/circumcision/2026-10-08/06_flagged_pro_types.png`.

**Second layer: survivors that depend on a flagged pro argument.** Each of the 951 male pro argument sentences that kept at least 1 point was checked for whether its reasoning uses one of the 61 flagged ones as a premise (builds on it, refers back to it, or relies on the same flagged claim). Each distinct flagged argument it depends on costs it 1 point, down to 0. A cheap pre-filter picked 490 pairs (nearby in the same article, or sharing a claim keyword); an AI model judged each one, so this is a model's judgment and a lower bound.

| Male pro points left | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Step 5 | 910 | 26 | 15 | 20 |
| After this check | 888 | 47 | 14 | 22 |

- 25 of 951 survivors lost 1 point; none lost more. They lean on 19 of the 61 flagged arguments, all in the same article.
- Anti arguments were not rechecked: only 4 anti sentences in the male circumcision articles were flagged.
- [`flagged_pro/dependency/DEPENDENCIES.md`](flagged_pro/dependency/DEPENDENCIES.md): the most relied-on flagged arguments and every chain, with verbatim quotes. Method, pre-filter, recall limit and judgment calls: [flagged_pro/METHOD.md](flagged_pro/METHOD.md#second-layer-dependence-on-flagged-priors).
- Data: `flagged_pro/dependency/dependencies.csv`, `flagged_pro/dependency/survivors_after_priors.csv`, `flagged_pro/dependency/summary.json`. Chart: `docs/img/circumcision/2026-10-08/07_pro_after_priors.png`.

**Pass 3: do the remaining pro arguments hold up?** All 949 male pro argument sentences with at least 1 point after the second layer were checked again, fresh, against fallacy_catalog v0.6.1, the same way the reviewers flagged. Each distinct entry flagged costs 1 point; a possible issue costs nothing. Five AI model sessions did the checking. Each was told not to open the earlier flags or scores, but they ran from a conversation that knew earlier results, so this is not blind.

| Male pro points left | 3 | 2 | 1 | 0 | All 3 points |
|---|---|---|---|---|---|
| Step 5 | 910 | 26 | 15 | 20 | 93.7% |
| After pass 2 (second layer) | 888 | 47 | 14 | 22 | 91.5% |
| After pass 3 | 883 | 50 | 15 | 23 | 90.9% |
| Anti, step 5 (not rechecked) | 724 | 2 | 2 | 0 | 99.5% |

**Pro only.** Anti arguments were checked only in step 5. They were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro.

- 8 sentences lost 1 point (5 of the 888 still at 3 points): false analogy 3, red herring 3, secundum quid 2. 39 possible issues were recorded.
- 3 of the 8 had already lost a point for what reads as the same flaw under another name or through pass 2; the rule does not merge them (see METHOD.md).
- [`flagged_pro/recheck/RECHECK.md`](flagged_pro/recheck/RECHECK.md): every counted flag with its verbatim quote and reason. Prompt: [`flagged_pro/recheck/RECHECK_PROMPT.md`](flagged_pro/recheck/RECHECK_PROMPT.md). Method and limits: [flagged_pro/METHOD.md](flagged_pro/METHOD.md#pass-3-fresh-recheck-of-the-remaining-pro-arguments).
- Data: `flagged_pro/recheck/findings.csv`, `flagged_pro/recheck/points_by_pass.csv`, `flagged_pro/recheck/summary.json`.

**What the surviving pro arguments rely on.** The 883 pro arguments with all 3 points after pass 3 were each tagged with one type: medical or scientific data 667 (75.5%), religion, culture or tradition 105 (11.9%), ethics, rights or law 72 (8.2%), other or mixed 39 (4.4%). Tagged by an AI model in 4 separate sessions, not a person; not blind (run from a conversation that already knew the earlier results); one type per sentence, so mixed sentences are forced into one type. A keyword ballpark matched the model's tag for 82.4% of sentences. See [`flagged_pro/topic_tags/TAGS.md`](flagged_pro/topic_tags/TAGS.md) and [flagged_pro/METHOD.md](flagged_pro/METHOD.md#what-the-surviving-pro-arguments-rely-on-topic-tags). Chart: `docs/img/circumcision/2026-10-08/08_what_survivors_rely_on.png`.

**What-if checks: HIV/STI and cancer.** Two more tagging passes asked how many of the 667 medical surviving pro arguments would lose their point if a claim were set aside. A tag means "depends on the claim", not that the claim is wrong; this audit did not check either claim.

- **HIV/STI** (all 667, no keyword prefilter): 254 (38.1%) rest on protection against HIV or other STIs, 399 (59.8%) on another medical claim, 14 (2.1%) on no benefit claim. Three AI model sessions.
- **Cancer** (prefiltered to the 210 with a cancer, HPV or cervical keyword within two sentences; a sentence relying on cancer only through "these benefits" outside that window is missed): 35 rest on cancer prevention, 8 of them also on HIV/STI. Two AI model sessions.
- **Combined:** 281 of 667 medical arguments (42.1%), or 31.8% of all 883 surviving pro arguments, rest on the HIV/STI or cancer claims.
- AI-tagged by sessions that already knew the earlier results, so not blind. See [`flagged_pro/sti_dependence/STI_DEPENDENCE.md`](flagged_pro/sti_dependence/STI_DEPENDENCE.md), [`flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md`](flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md) and [flagged_pro/METHOD.md](flagged_pro/METHOD.md#what-if-checks-do-the-medical-arguments-rest-on-the-hivsti-or-cancer-claims). Charts: `docs/img/circumcision/2026-10-08/09_sti_dependence.png`, `10_what_if_removed.png`.

**Total what-if: how much of the pro side is left.** Taking Jason's three premises as true (no HIV or STD protection; higher STD rates in circumcising countries; cancer prevention not a valid reason), the 971 male pro arguments split, each counted once, into: already flagged by the audit 88 (9.1%); set aside under the what-if 281 (28.9%: HIV/STI 254, cancer only 27); not invalidated 602 (62.0%: other medical 386, religion or culture 105, ethics or law 72, other 39). The non-medical arguments were not tagged for HIV/STI or cancer; 14 name such a term, and one AI model check found 2 that rest on the HIV claim (reported, not added). What-if, not a finding: premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias; this audit did not check either side, so the result holds only if the premises hold. See [`flagged_pro/whatif_total/TOTAL_WHATIF.md`](flagged_pro/whatif_total/TOTAL_WHATIF.md). Chart: `docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png`.

## Walkthrough and new files (appended)

**Every step in order, with its chart:** [WALKTHROUGH.md](WALKTHROUGH.md).

Files added since the Files table above:

| File | What it is |
|---|---|
| `WALKTHROUGH.md` | Every step of the run in order, with who did it, the key number, the chart and links to each method |
| `flagged_pro/sti_dependence/` | What-if check: medical survivors that rest on the HIV/STI claim |
| `flagged_pro/cancer_dependence/` | What-if check: medical survivors that rest on the cancer claim |
| `flagged_pro/whatif_total/` | Total what-if: the whole male pro side, already flagged, invalidated under the premises, or left |
