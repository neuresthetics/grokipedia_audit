# Full record: circumcision articles, fallacy_catalog run (2026-10-08)

## Part 1. The author's position

*Source: background/authors_position.md (whole file)*

# Author's position (Jason Burns)

Date: 2026-10-08

> **Status: the author's view, not an audit result.** This page records what the repo's author, Jason Burns, thinks, at his request ("you can document what I think."). Nothing on this page was tested by this audit. Quotes in quotation marks are his words; lines marked *paraphrase* are a summary of what he said, not his wording.

## 1. The record should reflect collective reasoned voices

> "Are we not speakers? The record should reflect the voice of collective reason"

*Paraphrase:* people who reason in public are speakers too, and the record should reflect their reasoned voices.

## 2. Good arguments should be considered for the archive

*Paraphrase:* he asked why good arguments are not being considered for the archive. In his view, they should be.

## 3. His hypothesis about X, Grok and Grokipedia

> "You're built into X, KIND OF"

*Paraphrase:* he holds that the pro-side result in this repo came from a narrow selection of arguments, and that if more were applied, it would show that Grok is not built to hear these arguments on X in a way that lets what he calls the collective social digital organism grow. He sees this as the system being unable to feed back honestly into itself.

This is his hypothesis. The audit did not test it. The audit measured only the text of saved Grokipedia articles. It did not measure how Grokipedia selects content, how X posts feed into Grok or Grokipedia, or how Grok is trained.

## 4. His premises in the what-if count

The total what-if count ([TOTAL_WHATIF.md](flagged_pro/whatif_total/TOTAL_WHATIF.md)) took his selected points as premises:

1. circumcision gives no protection against HIV or other STIs;
2. STI rates are highest in circumcising countries;
3. cancer prevention is not a valid reason.

On the third, he said: "we can take cancer prevention off as a valid reason". *Paraphrase:* he compared it with breast cancer and brain cancer, where removing healthy tissue to prevent a cancer would not be accepted as a reason; penile cancer is rare.

The audit has not tested these premises. Premise 1 contradicts the randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007). Under the premises, 281 of the 971 male circumcision pro arguments (29%) rest on the HIV/STI or cancer claims, and 88 (9%) were already flagged by the audit. That is a what-if count, not a finding.

## 5. What this audit can and cannot do

- **It can** publish its checks in this repo, and draft edit submissions for Grokipedia articles (see `../articles/<slug>/edit_submissions/`).
- **It cannot** change Grokipedia. Whether a submission is used is up to Grokipedia.
- **No verified feedback channel.** The AI assistant that ran these checks has no verified channel into Grokipedia's content or Grok's training. It cannot confirm that anything in this repo reaches either. This is a limitation, stated plainly.
- The audit's judgments were made by AI model sessions, not a person, and they are not blind (see the [walkthrough](WALKTHROUGH.md)).

## Part 2. The steps, in order, with their charts

*Source: WALKTHROUGH.md, introduction and caveats*

# Walkthrough: circumcision articles, fallacy_catalog run (2026-10-08)

Every step of this benchmark, in order, with what was done, who or what did it, the key number and the chart. It does not repeat the methods; each step links to its method or detail file. Back to the [run README](README.md). The longer read of the results is [ANALYSIS.md](ANALYSIS.md).

**Read with these caveats.**

- Every judgment below was made by an **AI model, not a person**: the fallacy flags, the pro/anti labels, the dependence check, the recheck, the topic tags, the what-if tags and the step-10 check of non-medical keyword hits. Rule scripts only counted, matched and checked quotes.
- **Not blind.** Reviewers 2 and 3, the pass-3 checkers and all the taggers started from a conversation that already knew earlier results. Reviewer 1 is the only fully uninfluenced read.
- **Flags are leads, not verdicts.** A flag says a step of reasoning fails a catalog entry, not that the conclusion is false. Keeping all points means not flagged, not proven true.
- **Pro only after step 5.** Steps 6 to 10 cover the male circumcision pro arguments only. Anti arguments were checked only in step 5 and were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro.

*Source: WALKTHROUGH.md, section '1. Snapshots'*

## 1. Snapshots

**What:** the 58 circumcision-related Grokipedia articles (39 male circumcision, 19 FGM) were saved as they appeared on 2026-10-01, and nothing was fetched again for this run. **Who:** a plain HTTP fetch (curl) and a text extraction; no model judgment. **Key number:** 58 articles, 13,199 prose sentences (8,778 male circumcision, 4,421 FGM).

Details: [ARTICLE_LIST.md](../../ARTICLE_LIST.md), [SNAPSHOT_INDEX.md](../../SNAPSHOT_INDEX.md).

*Source: README.md, 'How it works' step 1*

1. **Snapshot.** Save the article as it appeared on the day of the audit, because Grokipedia pages change.

*Source: WALKTHROUGH.md, section '2. Claim and source check (citation markers only, so far)'*

## 2. Claim and source check (citation markers only, so far)

**What:** this run counted citation markers against each article's saved source list. It did **not** yet check each claim against what its cited source says; that claim-by-claim check (steps 2 and 3 of the [repo README](../../../../README.md)) is still to be done for this topic. **Who:** a rule script (`scripts/citation_stats.py`). **Key number:** 4,658 of 13,199 sentences (35.3%) carry no citation marker; two articles have broken source lists.

![Citation gaps: top 10 articles by share of sentences with no citation marker](../../../../docs/img/circumcision/2026-10-08/03_citation_gaps.png)

Details: [README.md, "Citation counts"](README.md#citation-counts), [ANALYSIS.md, "Citation hygiene"](ANALYSIS.md#citation-hygiene).

*Source: README.md, 'How it works' step 2*

2. **Claim and source.** For each claim, quote what the article says, then quote what the cited source actually says.

*Source: README.md, 'How it works' step 3*

3. **Verdict.** Mark the claim *supported*, *miscited* (the source exists but doesn't say this), *unsupported* (the source contradicts it or gives nothing to check) or *uncited*. The article, the source and the judgment are kept as three separate things.

*Source: ANALYSIS.md, section 'Citation hygiene' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Citation hygiene

- **4,658 of 13,199 prose sentences (35.3%) have no `[n]` citation marker.** The median article is at 35.1%.
- **Highest uncited shares:** circumcision-in-brunei 54.4%, stapler-circumcision 52.4%, female-genital-mutilation 51.9%, cost-of-circumcision-surgery-in-chaozhou 50.6%. **Lowest:** meatal-stenosis 23.8%, foreskin 24.1%.
- **Two broken source lists.** female-genital-mutilation lists 3 sources but uses markers up to [76] (153 markers point past the list). views-on-circumcision lists 2 sources but uses markers up to [114] (139 markers past the list). The saved sources for these two don't match the text, so their citation counts are unreliable.
- Sentence splitting is rule-based, so these shares are approximate.

*Source: WALKTHROUGH.md, section '3. Three reviewers' fallacy flags'*

## 3. Three reviewers' fallacy flags

**What:** each reviewer read all 58 articles in full and flagged passages where the article's own reasoning meets every condition of a [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1 entry. Every quote was checked by script against the snapshot. **Who:** three separate AI agent sessions (Reviewers 1, 2 and 3). **Key number:** 87 rows from Reviewer 1, 64 from Reviewer 2 and 121 from Reviewer 3.

Details: [README.md, "What was done"](README.md#what-was-done), [scripts/reading_notes.md](scripts/reading_notes.md).

*Source: README.md, 'How it works' step 4*

4. **Reasoning check.** Where an article argues rather than reports, its arguments are checked against [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog), a plain, sourced list of known logical fallacies. A flag is a lead for a reader to follow up, not a verdict.

*Source: ANALYSIS.md, section 'What was done' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What was done

- **Articles:** the 58 circumcision-related Grokipedia articles saved on 2026-10-01. Nothing was fetched again.
- **Checklist:** [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1, commit `2a56493`, used with its METHOD.md.
- **Reviewers:** Reviewer 1, 2 and 3. Three separate AI agents each read all 58 articles and wrote their own flags. Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, and each reports it did not, but their instructions came from a conversation that had already discussed earlier results (Reviewer 2: Reviewer 1's totals, top articles and fallacy types; Reviewer 3: counts and example quotes from Reviewers 1 and 2), so they were not blind. Reviewer 1 is the only fully uninfluenced read. Their results are shown side by side, not merged.
- **Flag:** a passage where the article's own reasoning is flawed, matched to a catalog entry. A flag is a lead for a human to check, not a verdict.
- **Passage:** flags from different reviewers count as the same passage when their quotes overlap in the same article (`overlap_3way.csv`).
- **Flagged by at least two / by all three:** that many reviewers, reading separately, flagged the passage and gave it the same side. This is overlap, not proof that the flag is right.
- **Side:** in male circumcision articles, *pro* means the flaw helps the case for the practice and *anti* the case against it. In FGM articles, *anti* means against the practice and *pro* means defending it or playing down harm. *Neutral* helps neither side.
- **Rate:** flags per 100 sentences = 100 × flags ÷ prose sentences. Sentence counts are the `sentences` column of `citation_stats.csv` (prose sentences in each snapshot, rule-based split). The 58 articles have 13,199 sentences: 8,778 in the 39 male circumcision articles and 4,421 in the 19 FGM articles.

*Source: WALKTHROUGH.md, section '4. Comparison and charts 01–04'*

## 4. Comparison and charts 01–04

**What:** the three sets of flags were compared by side and by article, and matched to each other where their quotes overlap. **Who:** rule scripts (`scripts/compare_reviewers.py`, [`tools/make_charts_2026_10_08.py`](../../../../tools/make_charts_2026_10_08.py)). **Key numbers:** for every flawed argument helping the anti side, the reviewers found 2.3, 5.25 and 1.51 helping the pro side. 33 passages were flagged by all three reviewers (25 for the same side).

![Which side's case relies more on flawed reasoning: pro vs anti flags per 100 sentences, by reviewer](../../../../docs/img/circumcision/2026-10-08/01_which_side.png)

![Top 10 articles by flagged reasoning per 100 sentences](../../../../docs/img/circumcision/2026-10-08/02_most_flagged_articles.png)

![How often the reviewers flagged the same passage](../../../../docs/img/circumcision/2026-10-08/04_reader_overlap.png)

Chart 03 is shown under step 2. Details: [README.md, "Second reviewer and overlap"](README.md#second-reviewer-and-overlap) and ["Third reviewer and three-way overlap"](README.md#third-reviewer-and-three-way-overlap), [ANALYSIS.md](ANALYSIS.md).

*Source: ANALYSIS.md, section 'Headline: which side's case relies more on flawed reasoning?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Headline: which side's case relies more on flawed reasoning?

The chart shows the three readers only; the table below adds passages flagged by at least two and by all three.

This counts flawed reasoning in the articles by which side it helps. Fewer flaws means a side is argued more cleanly in these articles, not that its conclusion is right.

For every 1 flawed argument helping the anti side, across all 58 articles:
- Reviewer 1 found **2.3** helping the pro side.
- Reviewer 2 found **5.25**.
- Reviewer 3 found **1.51**.
- Passages flagged by at least two reviewers show **2.5** (45 pro, 18 anti).
- Passages flagged by all three show 22 pro and 1 anti.

**Rule for marking a side "cleaner-argued":** the other side must have at least 2 times as many flags (the sentence count is shared, so this is also the ratio per 100 sentences) and at least 5 flags. Otherwise there is no check ("no clear difference" in the table). Where the cleaner side has only 1 to 3 flags, the direction is clear but the size of the ratio is fragile (marked "size fragile" in the table).

| Articles | Reader | Pro flags | Anti flags | Pro share | Pro / 100 sentences | Anti / 100 sentences | Pro : anti | Cleaner-argued side |
|---|---|---|---|---|---|---|---|---|
| All 58 | Reviewer 1 | 53 | 23 | 70% | 0.40 | 0.17 | 2.3 : 1 | anti |
| All 58 | Reviewer 2 | 42 | 8 | 84% | 0.32 | 0.06 | 5.25 : 1 | anti |
| All 58 | Reviewer 3 | 59 | 39 | 60% | 0.45 | 0.30 | 1.51 : 1 | no clear difference (under 2 : 1) |
| All 58 | Flagged by at least two | 45 | 18 | 71% | 0.34 | 0.14 | 2.5 : 1 | anti |
| All 58 | Flagged by all three | 22 | 1 | 96% | 0.17 | 0.01 | 22 : 1 | anti (size fragile: 1 anti flag) |
| Male circumcision (39) | Reviewer 1 | 42 | 7 | 86% | 0.48 | 0.08 | 6 : 1 | anti |
| Male circumcision (39) | Reviewer 2 | 35 | 1 | 97% | 0.40 | 0.01 | 35 : 1 | anti (size fragile: 1 anti flag) |
| Male circumcision (39) | Reviewer 3 | 48 | 8 | 86% | 0.55 | 0.09 | 6 : 1 | anti |
| Male circumcision (39) | Flagged by at least two | 38 | 5 | 88% | 0.43 | 0.06 | 7.6 : 1 | anti |
| Male circumcision (39) | Flagged by all three | 18 | 0 | 100% | 0.21 | 0.00 | 18 : 0 | anti (no anti flags at all) |
| FGM (19) | Reviewer 1 | 11 | 16 | 41% | 0.25 | 0.36 | 0.69 : 1 | no clear difference (under 2 : 1) |
| FGM (19) | Reviewer 2 | 7 | 7 | 50% | 0.16 | 0.16 | 1 : 1 | no clear difference (tie) |
| FGM (19) | Reviewer 3 | 11 | 31 | 26% | 0.25 | 0.70 | 0.35 : 1 | **pro** (anti has 2.82x the flags) |
| FGM (19) | Flagged by at least two | 7 | 13 | 35% | 0.16 | 0.29 | 0.54 : 1 | no clear difference (under 2 : 1) |
| FGM (19) | Flagged by all three | 4 | 1 | 80% | 0.09 | 0.02 | 4 : 1 | no clear difference (larger side under 5 flags) |

"Pro share" is pro flags as a share of pro + anti flags. Neutral flags are left out of this table: Reviewer 1 had 11, Reviewer 2 had 14, Reviewer 3 had 23; 11 passages were flagged as neutral by at least two reviewers and 2 by all three.

What this says, plainly:
- **In the male circumcision articles, the pro side's case relies more on flawed reasoning.** All three reviewers, reading separately, found most of the flawed reasoning on the pro side (86%, 97% and 86% of their sided flags), and so do the passages flagged by at least two (38 pro, 5 anti) and by all three (18 pro, 0 anti). The anti side is argued more cleanly there. The 35 : 1 ratio rests on one anti flag and the all-three row on none, so read them as "almost all pro", not as precise numbers.
- **In the FGM articles there is no clear difference across the reviewers.** Reviewer 1 found more anti flags than pro (16 vs 11), Reviewer 2 an even split (7 vs 7), and Reviewer 3 clearly more anti (31 vs 11), which meets the rule for "pro side cleaner-argued" for Reviewer 3 alone. Passages flagged by at least two lean anti (13 vs 7) but fall short of 2 : 1. Only 12 of Reviewer 3's 31 FGM anti flags were also flagged for the anti side by Reviewer 1 or 2, so the FGM anti count is the least settled number in this run.
- **Across all 58 articles,** Reviewers 1 and 2 and the passages flagged by at least two meet the rule (pro has 2.3x to 5.25x the flaws of anti). Reviewer 3 does not (1.51 : 1), because its many FGM anti flags offset its male circumcision pro flags. The all-58 figure mixes two groups that point different ways; the per-group results are the better read.
- **The reviewers differ most on anti flags.** Reviewer 1 flagged 23, Reviewer 2 flagged 8 and Reviewer 3 flagged 39. Pro counts are closer (53, 42, 59).
- **Not a verdict on who is right.** A cleaner-argued side has fewer reasoning flaws in these articles. That says nothing about whether its conclusion is correct.
- **Caveat:** a side's flag count also depends on how much of each side's case the articles present in their own voice. We did not count that. An article that mostly makes one side's argument has more chances to make that side's mistakes.

*Source: ANALYSIS.md, section 'Which articles have the most flawed reasoning per sentence?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Which articles have the most flawed reasoning per sentence?

**Top 10 by the three readers' average rate:** women-unaffected-by-female-genital-cutting 3.17, circumcision-controversies 3.02, ethics-of-circumcision 2.85, ulwaluko 1.88, forced-circumcision-of-minors-in-south-korea 1.61, views-on-circumcision 1.54, prohibition-of-female-circumcision-act-1985 1.26, female-genital-mutilation 1.25, female-genital-mutilation-in-new-zealand 1.24, prevalence-of-female-genital-mutilation 1.17.

Ranked by the average of the three reviewers' rates (flags per 100 sentences of the article). 46 articles have at least one flag from some reviewer; 12 have none. The top three are the same as with two reviewers, and every flag any reviewer made in these three is pro except one neutral flag from Reviewer 2:

| Article | Sentences | Reviewer 1 | Reviewer 2 | Reviewer 3 | Flagged by at least two | Flagged by all three |
|---|---|---|---|---|---|---|
| women-unaffected-by-female-genital-cutting | 189 | 3.70 (7) | 2.65 (5) | 3.17 (6) | 2.12 (4) | 3 |
| circumcision-controversies | 232 | 3.02 (7) | 3.02 (7) | 3.02 (7) | 2.16 (5) | 4 |
| ethics-of-circumcision | 327 | 1.83 (6) | 3.67 (12) | 3.06 (10) | 2.75 (9) | 2 |

Rates per 100 sentences, with flag counts in brackets.

Top 10 for each reader:
- **Reviewer 1:** women-unaffected-by-female-genital-cutting 3.70, circumcision-controversies 3.02, prohibition-of-female-circumcision-act-1985 2.52, ulwaluko 2.17, views-on-circumcision 2.05, ethics-of-circumcision 1.83, ashley-montagu-resolution 1.63, forced-circumcision-of-minors-in-south-korea 1.61 (1 flag in 62 sentences), female-genital-mutilation-in-new-zealand 1.24, prevalence-of-female-genital-mutilation 1.17.
- **Reviewer 2:** ethics-of-circumcision 3.67, circumcision-controversies 3.02, women-unaffected-by-female-genital-cutting 2.65, ulwaluko 1.30, female-genital-mutilation-in-new-zealand 1.24, female-genital-mutilation-in-nigeria 0.96, female-genital-mutilation 0.86, mohel 0.86, ashley-montagu-resolution 0.81, prevalence-of-female-genital-mutilation 0.78.
- **Reviewer 3:** forced-circumcision-of-minors-in-south-korea 3.23 (2 flags in 62 sentences), women-unaffected-by-female-genital-cutting 3.17, ethics-of-circumcision 3.06, circumcision-controversies 3.02, ulwaluko 2.17, views-on-circumcision 2.05, female-genital-mutilation 2.02, female-genital-mutilation-act-2003 1.91, female-genital-mutilation-laws-by-country 1.57, prevalence-of-female-genital-mutilation 1.56.
- **Flagged by at least two:** ethics-of-circumcision 2.75, circumcision-controversies 2.16, women-unaffected-by-female-genital-cutting 2.12, views-on-circumcision 2.05, ulwaluko 1.74, forced-circumcision-of-minors-in-south-korea 1.61, prohibition-of-female-circumcision-act-1985 1.26, female-genital-mutilation-in-new-zealand 1.24, prevalence-of-female-genital-mutilation 1.17, circumcision-in-africa 1.05.

Short articles can rank high from one or two flags. Per-article flag counts line up fairly well between each pair of reviewers (Spearman 0.77 for 1 and 2, 0.77 for 1 and 3, 0.72 for 2 and 3, from `agreement_summary.md`).

*Source: ANALYSIS.md, section 'Male circumcision vs FGM articles, all sides' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Male circumcision vs FGM articles, all sides

- **Male circumcision (8,778 sentences):** Reviewer 1 0.60 per 100 sentences (53 flags), Reviewer 2 0.46 (40), Reviewer 3 0.74 (65); flagged by at least two 0.52 (46 passages: 38 pro, 5 anti, 3 neutral); flagged by all three 0.21 (18, all pro).
- **FGM (4,421 sentences):** Reviewer 1 0.77 (34), Reviewer 2 0.54 (24), Reviewer 3 1.27 (56); flagged by at least two 0.63 (28: 7 pro, 13 anti, 8 neutral); flagged by all three 0.16 (7: 4 pro, 1 anti, 2 neutral).
- Reviewer 3 flags the FGM articles at a higher rate than the other two (1.27 per 100 sentences against 0.77 and 0.54), and more than half of its FGM flags are anti (31 of 56).

*Source: ANALYSIS.md, section 'How much the reviewers' flags overlap' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## How much the reviewers' flags overlap

**Who flagged each passage.** The three reviewers flagged 164 distinct passages between them:

| Flagged by | Passages |
|---|---|
| Reviewer 1 only | 22 |
| Reviewer 2 only | 13 |
| Reviewer 3 only | 54 |
| Reviewers 1 and 2 only | 8 |
| Reviewers 1 and 3 only | 24 |
| Reviewers 2 and 3 only | 10 |
| All three | 33 |

So 75 passages were flagged by at least two reviewers (74 of them with the same side from at least two) and 33 by all three (25 with the same side from all three).

**Each pair of reviewers** (one-to-one matching of overlapping quotes in the same article):

| Pair | Flags | Matched | Share of each reviewer's flags matched | Same side | Same fallacy name | Near-twin name |
|---|---|---|---|---|---|---|
| 1 and 2 | 87 / 64 | 41 | 47% / 64% | 36 of 41 (88%) | 20 of 41 (49%) | 10 |
| 1 and 3 | 87 / 121 | 57 | 66% / 47% | 53 of 57 (93%) | 39 of 57 (68%) | 7 |
| 2 and 3 | 64 / 121 | 43 | 67% / 36% | 35 of 43 (81%) | 28 of 43 (65%) | 6 |

Near-twin names are pairs like bulverism / appeal to motive or false cause / cum hoc. When two reviewers flagged the same passage they usually gave it the same side; they gave the same fallacy name about half to two thirds of the time.

- **Most common fallacy types among the 74 passages flagged by at least two (same side).** At least two reviewers gave the same name in 54: non-sequitur 10, inconsistency 9, bulverism 7, false analogy 5, cum hoc 4, false cause 4, straw man 3. In the other 20 they used different names.

### Representative passages flagged by at least two

Quoted exactly from `overlap_3way.csv` (Reviewer 1's quote). The notes paraphrase the reviewers' reasons.

1. **circumcision, inconsistency (pro), all three.** "Neonatal circumcision in the first week enables near-painless outcomes under optimal blocks, given lower pre-phimosis sensitivity." The same paragraph says pain blocks give reductions that "fall short of elimination".
2. **brit-milah, straw man (pro), Reviewers 1 and 2.** "These positions counter activist claims of net harm by prioritizing randomized and cohort data over anecdotal or ideological critiques" Just above, the article shows critics citing bioethics journals, complication rates and documented herpes cases, which are then recast as anecdotal or ideological.
3. **foreskin, inconsistency (pro), all three.** "forming the primary site for erogenous sensation, which remains unaffected by circumcision" Elsewhere the article says the glans thickens and keratinizes after circumcision.
4. **women-unaffected-by-female-genital-cutting, false analogy (pro), all three.** "Type I (clitoridectomy, affecting ~80% of cases in some regions) involves minimal tissue removal analogous to hoodectomy in cosmetic procedures" The article's own definition of Type I includes removing the clitoral glans.
5. **female-genital-mutilation-act-2003, bulverism / appeal to motive (anti), all three.** "with critics in media and academia—often exhibiting left-leaning biases toward multicultural tolerance—arguing that condemnation risks stigmatizing minority cultures" The critics' concern is put down to their politics instead of being answered.

*Source: WALKTHROUGH.md, section '5. Survival scoring and chart 05'*

## 5. Survival scoring and chart 05

**What:** every sentence was labeled pro, anti or not an argument. Each argument starts with 3 points and loses 1 for each reviewer that flagged it. **Who:** an AI model in 9 separate labeling sessions split by article (the labelers did not see the flags); the scoring is a rule script. **Key number:** in the male circumcision articles, 93.7% of pro arguments (910 of 971) and 99.5% of anti arguments (724 of 728) kept all 3 points. In the FGM articles: 96.7% pro, 97.7% anti.

![How much of each side's argument survived the fallacy check](../../../../docs/img/circumcision/2026-10-08/05_what_survived.png)

Details: [survival/METHOD.md](survival/METHOD.md), [survival/LABEL_PROMPT.md](survival/LABEL_PROMPT.md).

*Source: README.md, 'How it works' step 5*

5. **Survival scoring.** An AI model labels every sentence *pro*, *anti* or *not an argument*. Each argument starts with 3 points and loses 1 for each reviewer that flagged it. The result shows what share of each side's arguments went unflagged; unflagged means not flagged, not proven true. See the circumcision benchmark's [method](survival/METHOD.md).

*Source: ANALYSIS.md, section 'What survived: how much of each side's argument was never flagged?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What survived: how much of each side's argument was never flagged?

The headline above counts flaws. This chart asks the reverse question: of the sentences that argue for or against the practice, how many did no reviewer flag? Each argument sentence starts with 3 points and loses 1 point for each reviewer whose flag overlaps it.

- **Male circumcision articles:** 6.3% of pro argument sentences were flagged by at least one reviewer (61 of 971), against 0.5% of anti ones (4 of 728). 20 pro sentences lost all 3 points; no anti sentence did.
- **FGM articles:** the two sides are close: 3.3% of pro (10 of 301) and 2.3% of anti (14 of 616). If flagged claims about whether laws or campaigns worked are counted as arguments, the order flips, so this group has no clear winner.

Survival means "not flagged", not "true". All 13,199 sentences were labeled by an AI model, not a person, in 9 separate sessions split by article, and no session checked another's work. The male circumcision gap holds under every check. The lists, the method, the limits and a consistency check by labeler are in [`survival/`](survival/): [SURVIVORS.md](survival/SURVIVORS.md) and [METHOD.md](survival/METHOD.md).

*Source: WALKTHROUGH.md, section '6. Flagged pro arguments by type and chart 06'*

## 6. Flagged pro arguments by type and chart 06

**What:** the male circumcision pro arguments that lost at least one point were sorted by the kind of flaw the reviewers named, using the catalog's own categories, with mechanics, verbatim quotes and counters. **Who:** a rule script over the reviewers' flags; no new model judgment. **Key number:** 61 sentences; 28 (46%) are mainly off-point reasons and 20 (33%) unearned or clashing premises.

![What kinds of flawed reasoning did the flagged pro arguments use](../../../../docs/img/circumcision/2026-10-08/06_flagged_pro_types.png)

Details: [flagged_pro/FLAGGED_PRO.md](flagged_pro/FLAGGED_PRO.md), [flagged_pro/METHOD.md](flagged_pro/METHOD.md).

*Source: README.md, 'How it works' step 6*

6. **Flagged pro arguments.** In the male circumcision articles, the pro arguments that lost at least one point are sorted by the kind of flaw the reviewers named, using fallacy_catalog's own categories. Each kind gets its share, how the move works, verbatim quotes, and the reply that exposes it, quoted from the catalog entry where it has one. Then each surviving pro argument loses 1 point for every flagged one it depends on as a premise, and in a third pass the remaining pro arguments are rechecked against the catalog, losing 1 point per fallacy flagged (both judged by AI models). Pro only: anti arguments were checked only in step 5 and were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro. See the circumcision benchmark's [write-up](flagged_pro/FLAGGED_PRO.md).

*Source: ANALYSIS.md, section 'Flagged pro arguments: what kinds of flawed reasoning?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Flagged pro arguments: what kinds of flawed reasoning?

Step 6 covers the male circumcision articles only. It looks at the 61 pro arguments there that lost at least one point and sorts each by the kind of flaw the reviewers named, using fallacy_catalog's own categories.

- **Most common: a reason that doesn't bear on the point** (28, 46%). Examples are answering a consent objection with satisfaction surveys, answering lasting-pain evidence with quick healing, or explaining critics' views by their supposed bias.
- **Next: unearned or clashing premises** (20, 33%). Often the article contradicts itself, for example calling the procedure "near-painless" after saying pain relief falls short. Or it applies a stricter test to the other side's evidence than to its own.
- **Thin or ill-fitting evidence** (9, 15%) is mostly false analogies (5 of 9), such as comparisons with heel-prick blood tests or vaccines.
- Stretched numbers and shaky cause and effect are each primary for 2 sentences.

The quotes, the catalog's definitions and the counter for each family are in [flagged_pro/FLAGGED_PRO.md](flagged_pro/FLAGGED_PRO.md). Flags are leads, not verdicts, and a flagged step can still lead to a true conclusion.

*Source: WALKTHROUGH.md, section '7. Dependency pass (pass 2), pass-3 recheck and chart 07'*

## 7. Dependency pass (pass 2), pass-3 recheck and chart 07

**Pass 2, what:** each surviving pro argument lost 1 point for every flagged pro argument it uses as a premise. A rule pre-filter picked 490 pairs to judge. **Who:** one AI model session. **Key number:** 25 of 951 lost a point; full points went from 910 to 888.

**Pass 3, what:** the 949 pro arguments with at least 1 point left were checked again, fresh, against the catalog, the same way the reviewers flagged. **Who:** five AI model sessions. **Key number:** 8 lost a point; 883 of 971 (90.9%) keep all 3 points.

![Do the surviving pro arguments hold up: points left at step 5, after pass 2 and after pass 3, with anti for reference](../../../../docs/img/circumcision/2026-10-08/07_pro_after_priors.png)

Details: [flagged_pro/dependency/DEPENDENCIES.md](flagged_pro/dependency/DEPENDENCIES.md), [flagged_pro/recheck/RECHECK.md](flagged_pro/recheck/RECHECK.md), [flagged_pro/METHOD.md](flagged_pro/METHOD.md#second-layer-dependence-on-flagged-priors).

*Source: ANALYSIS.md, section 'Flagged pro arguments: did the survivors lean on them, and do they hold up?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Flagged pro arguments: did the survivors lean on them, and do they hold up?

The second layer of step 6 asks whether the pro arguments that survived step 5 used any of the 61 flagged ones as a premise. Each one they depend on costs 1 point.

- **A few did.** 25 of 951 survivors lost 1 point; none depended on more than one flagged argument. Male pro arguments with all 3 points went from 910 to 888.
- **The links were local.** Every dependency judged was within the same article, and 18 of 25 sit within two sentences of the flagged one: "This effect", "These actions", "Similar mechanisms", or a conclusion like "Overall, the absence of verifiable risk compensation…" drawn from a flagged step just before it.
- **Most relied on** (2 dependents each): the no-risk-compensation inference in circumcision-and-hiv, the claim that falling HIV incidence after programmes began shows causation, the heel-prick analogy in ethics-of-circumcision, and three others.
- **Repeated claims in other articles did not add points.** 164 cross-article pairs were judged and none was judged a dependency. Where a claim recurs in another article (for example adult HIV trial results applied to infants), the sentence there was judged to report a position or stand on its own evidence, or it is flagged itself (26 of the 164 pairs) and already lost its point in step 5.

This is a model's judgment on pairs picked by a cheap pre-filter, so it is a lower bound. Anti arguments were not rechecked (only 4 were flagged). Chains with quotes: [flagged_pro/dependency/DEPENDENCIES.md](flagged_pro/dependency/DEPENDENCIES.md).

Pass 3 then checked the 949 remaining pro arguments again, fresh, against the catalog.

- **Most held up.** 8 lost a point: 5 of the 888 still at full points, and 3 that had already lost one. 883 of 971 pro arguments (90.9%) end with all 3 points, against 93.7% after step 5. Anti, which was not rechecked, stood at 99.5% after step 5.
- **The new flags repeat known moves.** Three false analogies (proxy consent compared with vaccination and ear piercing, the "mutilation" label answered with ear piercing, heel lancing), three red herrings (outcome data such as complication rates offered against a consent objection), and two secundum quid (adult African HIV trial results stated for infant decisions).
- 39 possible issues were recorded and cost nothing. 3 of the 8 dings fall on sentences already marked down for what reads as the same flaw under another name; without them the full-points count is unchanged.

**Pro only.** Anti arguments were checked only in step 5. They were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro. These are AI model judgments, five sessions, not blind. Quotes: [flagged_pro/recheck/RECHECK.md](flagged_pro/recheck/RECHECK.md).

*Source: WALKTHROUGH.md, section '8. Topic tagging and chart 08'*

## 8. Topic tagging and chart 08

**What:** each of the 883 pro arguments with all 3 points after pass 3 was tagged with the one kind of support it relies on. One type per sentence, so mixed sentences are forced into one type. **Who:** four separate AI model sessions; a keyword count (rule script) as a cross-check. **Key number:** 667 (75.5%) rest on medical or scientific data. The keyword tag matched the model's tag for 82.4% of sentences.

![What do the surviving pro arguments rely on](../../../../docs/img/circumcision/2026-10-08/08_what_survivors_rely_on.png)

Details: [flagged_pro/topic_tags/TAGS.md](flagged_pro/topic_tags/TAGS.md), [flagged_pro/METHOD.md](flagged_pro/METHOD.md#what-the-surviving-pro-arguments-rely-on-topic-tags).

*Source: README.md, 'How it works' step 7*

7. **Topic tagging.** The male circumcision pro arguments that kept all 3 points after step 6 are each tagged with the one kind of support they rely on: medical or scientific data; ethics, rights or law; religion, culture or tradition; or other. About three in four rest on medical data. The tags are AI-tagged (4 separate model sessions), one type per sentence, so mixed sentences are forced into one type, and not blind. See the circumcision benchmark's [tags](flagged_pro/topic_tags/TAGS.md).

*Source: ANALYSIS.md, section 'What do the surviving pro arguments rely on?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What do the surviving pro arguments rely on?

Ballpark: about three in four. Of the 883 pro arguments that kept all 3 points after pass 3, 667 (75.5%) rest on medical or scientific data: trial results, rates, risks and benefits, mechanisms or clinical guidance. Religion, culture or tradition comes next with 105 (11.9%), then ethics, rights or law with 72 (8.2%) and other or mixed with 39 (4.4%).

A simple keyword count lands in the same range (628 medical) and matched the model's tag for 82.4% of sentences. These are AI model tags from 4 separate sessions, not a person's, and not blind. Each sentence gets one type, so mixed sentences are forced into one. A tag says what an argument rests on, not whether it is right. Details: [flagged_pro/topic_tags/TAGS.md](flagged_pro/topic_tags/TAGS.md).

*Source: WALKTHROUGH.md, section '9. What-if checks: HIV/STI and cancer, charts 09 and 10'*

## 9. What-if checks: HIV/STI and cancer, charts 09 and 10

**Where the idea came from.** The HIV/STI check was prompted by two posts on X. Their text, verbatim (each also attaches an image; the first links a @statsglobe post). Neither cites a study, and this audit takes no position on them:

- [@Joseph4GI, 2026-10-06](https://x.com/joseph4gi/status/2107471990848381126): "Fun fact; STD rates are highest in circumcising countries, including the US."
- [@Intactivisme_Fr, 2026-09-26](https://x.com/intactivisme_fr/status/2103959873621025135): "Circumcision does NOT give you protection against HIV or other STDs. Foreskin is a mucous membrane that actually protects your genitals from getting anything, just like eyelids or nails or the lips."

The cancer check was a second what-if, raised by the repo owner, questioning cancer prevention as a reason.

**What:** two what-if passes over the 667 medical arguments from step 8. A tag means "depends on the claim", not that the claim is wrong; this audit did not check either claim. HIV/STI: all 667 tagged, no keyword prefilter (arguments tagged E, R or O in step 8 were not checked). Cancer: prefiltered to the 210 with a cancer, HPV or cervical keyword within two sentences; one relying on cancer only through "these benefits" outside that window is missed. **Who:** AI model sessions, three for HIV/STI and two for cancer, run from a conversation that already knew the earlier results, so not blind; keyword counts (rule scripts) as cross-checks. **Key numbers:** 254 of 667 (38.1%) rest on the HIV/STI claim; 35 rest on cancer, 8 of them also on HIV/STI; together 281 of 667 (42.1%), or 31.8% of all 883 surviving pro arguments.

![How many of the medical arguments rest on the HIV/STI claim](../../../../docs/img/circumcision/2026-10-08/09_sti_dependence.png)

![How many medical arguments rest on the HIV/STI or cancer claims](../../../../docs/img/circumcision/2026-10-08/10_what_if_removed.png)

Details: [flagged_pro/sti_dependence/STI_DEPENDENCE.md](flagged_pro/sti_dependence/STI_DEPENDENCE.md), [flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md](flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md), [flagged_pro/METHOD.md](flagged_pro/METHOD.md#what-if-checks-do-the-medical-arguments-rest-on-the-hivsti-or-cancer-claims).

*Source: README.md, 'How it works' step 8*

8. **What-if checks.** The medical arguments from step 7 are tagged by whether their point rests on the HIV/STI protection claim, and (for those near a cancer keyword) on the cancer-prevention claim. About two in five rest on one of the two. A tag means "depends on the claim", not that the claim is wrong; the audit does not check either claim. The tags are AI-tagged, one tag per sentence, and not blind. See the circumcision benchmark's [what-if counts](flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md). Added up over all 971 pro arguments, with those premises taken as true, 38% are flagged by the audit or set aside and 62% are left ([total what-if](flagged_pro/whatif_total/TOTAL_WHATIF.md)); this is conditional on the premises, the first of which contradicts the trials the articles cite.

*Source: ANALYSIS.md, section 'What-if: how many medical arguments rest on the HIV/STI or cancer claims?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What-if: how many medical arguments rest on the HIV/STI or cancer claims?

Two what-if passes asked which of the 667 medical arguments would lose their point if a claim were set aside. A tag means "depends on the claim", not that the claim is wrong; this audit did not check either claim.

- **HIV/STI:** 254 of 667 (38.1%) rest on protection against HIV or other sexually transmitted infections. Most of the rest, 399 (59.8%), rest on other medical claims such as UTIs, phimosis, safety or sexual function data.
- **Cancer:** 35 rest on cancer prevention (penile cancer, or cervical cancer via HPV); 8 of these also rest on HIV/STI. Only the 210 sentences with a cancer, HPV or cervical keyword within two sentences were tagged, so this can miss some.
- **Together:** 281 of 667 medical arguments (42.1%), or 31.8% of all 883 surviving pro arguments. The other 386 medical arguments rest on neither claim.

These are AI tags from 5 sessions in two passes, not a person's, and not blind. Penile cancer is rare in absolute terms, but how much that should weigh is not settled here. Details: [STI_DEPENDENCE.md](flagged_pro/sti_dependence/STI_DEPENDENCE.md), [CANCER_DEPENDENCE.md](flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md).

*Source: WALKTHROUGH.md, section '10. Total what-if: how much of the pro side is left, chart 11'*

## 10. Total what-if: how much of the pro side is left, chart 11

**What:** Jason asked how much of the pro side is invalidated if three points are taken as true: (1) circumcision gives no protection against HIV or other STDs; (2) STD rates are higher in circumcising countries; (3) cancer prevention is not a valid reason. This step adds up earlier results for all 971 male pro arguments; it does not change them. Each argument is counted once: already flagged by the audit (lost a point at step 5, pass 2 or pass 3) first, then HIV/STI, then cancer only, then the rest by topic tag. Premise 2 is not counted separately, because it adds nothing to premise 1 here. **Who:** a rule script, using the AI tags from steps 8 and 9; plus one AI model session that checked the 14 non-medical survivors naming HIV, an STI or cancer (not blind). **Key numbers:** already flagged 88 (9.1%); set aside under the what-if 281 (28.9%); together 369 (38.0%). Not invalidated 602 (62.0%): other medical claims 386, religion or culture 105, ethics or law 72, other 39. Of the 14 non-medical keyword hits, 2 rest on the HIV claim; they are reported, not added.

**Key caveat:** this is a what-if, not a finding. Premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias; this audit did not check either side, so the result holds only if the premises hold.

![What-if: how much of the pro side is left](../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

Details: [flagged_pro/whatif_total/TOTAL_WHATIF.md](flagged_pro/whatif_total/TOTAL_WHATIF.md), [flagged_pro/METHOD.md](flagged_pro/METHOD.md#total-what-if-how-much-of-the-pro-side-is-left).

*Source: ANALYSIS.md, section 'What-if: how much of the pro side is left under Jason's premises?' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What-if: how much of the pro side is left under Jason's premises?

Taking three premises as true (no HIV or STD protection; higher STD rates in circumcising countries; cancer prevention not a valid reason), and counting each of the 971 male pro arguments once:

- **Already flagged by the audit:** 88 (9.1%).
- **Set aside under the what-if:** 281 (28.9%): 254 resting on the HIV/STI claim and 27 on the cancer claim only.
- **Not invalidated:** 602 (62.0%): 386 medical arguments resting on other claims (such as UTIs, phimosis, hygiene, safety or sexual function), 105 religion or culture, 72 ethics or law, 39 other.

So about two in five pro arguments are flagged or set aside, and about three in five are left. The ethics, law and religion arguments were not tagged for HIV/STI or cancer. Of them, 14 name HIV, an STI or cancer (a rough upper bound); one AI model check found 2 that rest on the HIV claim, reported but not added.

This is a what-if, not a finding. Premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias; this audit did not check either side, so the result holds only if the premises hold. Details: [TOTAL_WHATIF.md](flagged_pro/whatif_total/TOTAL_WHATIF.md).

*Source: WALKTHROUGH.md, appended 'Note on chart 11' and step 10 line*

## Note on chart 11 (appended)

Chart 11 was redrawn so a reader sees the what-if at a glance. Its title is now "If these three things are true, 38% of the pro side is invalidated", and it lists the three premises in a box: (1) circumcision does not protect against HIV or other STIs; (2) STI rates are highest in circumcising countries (adds no separate count beyond 1); (3) cancer prevention is not a valid reason (penile cancer is rare, and prevention-by-removal proves too much). Premises are assumed, not tested here. Earlier text that calls it "What-if: how much of the pro side is left" refers to the same chart. The numbers are unchanged: 88 already flagged, 281 invalidated under the premises, 602 left.

**Step 10, how to read the 38%:** the headline 38% (369 of 971) includes the 88 arguments the audit had already flagged; the premises alone account for 281 (29%).

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'Result' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Result

| Group | Arguments | Share of 971 |
|---|---:|---:|
| Already flagged by the audit (lost 1+ point at step 5, pass 2 or pass 3) | 88 | 9.1% |
| What-if: rests on the HIV/STI claim | 254 | 26.2% |
| What-if: rests on the cancer claim only | 27 | 2.8% |
| Not invalidated: other medical claims | 386 | 39.8% |
| Not invalidated: ethics, rights or law | 72 | 7.4% |
| Not invalidated: religion, culture or tradition | 105 | 10.8% |
| Not invalidated: other, mixed or framing | 39 | 4.0% |
| **Total** | **971** | **100%** |

- Already flagged by the audit: **88** (9.1%). They first lost a point at step 5 (61), pass 2 (22) or pass 3 (5).
- Set aside under the what-if: **281** (28.9%), from the HIV/STI pass (254) and the cancer pass (27 cancer only).
- Flagged or set aside: **369** (38.0%).
- Not invalidated: **602** (62.0%): 386 medical arguments on other claims (UTIs, phimosis, hygiene, safety, sexual function and so on), plus 216 ethics, law, religion, culture or other arguments.

Chart: [11_pro_side_invalidated.png](../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'Counting rules (no double counting)' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Counting rules (no double counting)

Each argument goes into one group only, in this order:

1. If it lost 1 or more points at step 5, pass 2 or pass 3, it is **already flagged**, whatever its topic.
2. Otherwise, if it was tagged medical (M) and HIV/STI (H), it is **what-if: HIV/STI** ([STI_DEPENDENCE.md](flagged_pro/sti_dependence/STI_DEPENDENCE.md)).
3. Otherwise, if it was tagged medical and cancer (C), it is **what-if: cancer only** ([CANCER_DEPENDENCE.md](flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md)).
4. Otherwise it is **not invalidated**, split by its topic tag ([TAGS.md](flagged_pro/topic_tags/TAGS.md)).

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'Not checked: non-medical arguments that lean on HIV/STI or cancer' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Not checked: non-medical arguments that lean on HIV/STI or cancer

The 216 arguments tagged ethics/law, religion/culture or other were not put through the HIV/STI or cancer passes, so the what-if does not touch them. Some may still lean on those claims, which is a recall limit.

- **Keyword check (rough upper bound, no model):** 14 of 216 (6.5%) name HIV, an STI or cancer (7 E, 7 O). Naming a term is not the same as resting on it.
- **Model check of those 14** ([CHECK_PROMPT.md](flagged_pro/whatif_total/keyword_check/CHECK_PROMPT.md), [judgments.csv](flagged_pro/whatif_total/keyword_check/judgments.csv)): **2** rest on the HIV/STI claim; the other 12 keep another point (consent, culture, another medical benefit) or only report a view or event.
- `circumcision-in-africa` `s0279`: Argues Western norms do not fit Africa because HIV epidemiology differs; no point left without the HIV benefit
- `circumcision-in-africa` `s0287`: Point is that autonomy claims should not outrank verifiable HIV transmission reductions; rests on the HIV claim

These 2 are reported separately and are **not** added to the table. Adding them would make the what-if group 283 (29.1%). A non-medical sentence that leans on these claims without naming them would not be found.

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'Caveats' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Caveats

- **What-if, not a finding.** A tag means "depends on the claim", not that the claim is wrong.
- **AI-tagged, not blind.** The topic, HIV/STI and cancer tags and the model check above were made by AI model sessions, not a person. All ran from a conversation that already knew the earlier results, so they are not blind. The model check of the 14 keyword hits was one session.
- **Pro only.** Anti arguments were checked only at step 5 and are not part of this count.
- **Recall limits.** The cancer pass covers only medical sentences with a cancer, HPV or cervical keyword within two sentences. See the non-medical check above too.
- **One topic per sentence.** Mixed sentences were forced into one type at the topic-tagging step.

Built by `scripts/build_whatif_total.py` from `../recheck/points_by_pass.csv`, `../topic_tags/tags.csv`, `../sti_dependence/tags.csv` and `../cancer_dependence/tags.csv`.

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'The premises, in plain words' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## The premises, in plain words

If these three things are true, 38% of the pro side is invalidated (369 of 971: 88 already flagged by this audit plus 281 that rest on the HIV/STI or cancer claim). The other 602 (62%) are left standing. Premises are assumed, not tested here.

1. **Circumcision does not protect against HIV or other STIs.**
2. **STI rates are highest in circumcising countries.** This adds no separate count beyond premise 1.
3. **Cancer prevention is not a valid reason** (penile cancer is rare, and prevention-by-removal proves too much).

Note on the chart: chart 11 was redrawn so it states this at a glance. Its title is now "If these three things are true, 38% of the pro side is invalidated", and the premises are shown in a box on the chart. Alt text above that reads "What-if: how much of the pro side is left?" refers to the same chart.

*Source: flagged_pro/whatif_total/TOTAL_WHATIF.md, section 'Limits: a narrow selection' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## Limits: a narrow selection

The percentage comes from a narrow selection of arguments: the claims in two X posts, plus one point about cancer, applied to the pro arguments in 39 male circumcision Grokipedia articles. It is a what-if count. Applying more premises or arguments would change the numbers, in either direction. Nothing here has been tested beyond that selection.

## Part 3. What this does and doesn't show

*Source: ANALYSIS.md, section 'What this does and doesn't show' (text only: image lines left out; each chart is shown once, in the walkthrough block)*

## What this does and doesn't show

- **It does not show which side is right.** A cleaner-argued side is not thereby correct. It only looks at how these articles argue: where their own reasoning has gaps, and which side those gaps help. It is not a measure of whether circumcision is good or bad.
- **Pro vs anti depends on what the articles cover.** A side's flag count also depends on how much of each side's case the articles present in their own voice. We did not count that, so the ratio shows where the flawed reasoning sits, not how fairly each side is treated overall.
- **Overlap is consistency, not correctness.** All three reviewers are AI agents using the same catalog and method, so their mistakes may be shared. A passage flagged by two or three of them is a stronger lead. It is not proven.
- **Not blind.** Three separate AI agents each read all 58 articles and wrote their own flags. Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, and each reports it did not, but their instructions came from a conversation that had already discussed earlier results (Reviewer 2: Reviewer 1's totals, top articles and fallacy types; Reviewer 3: counts and example quotes from Reviewers 1 and 2), so they were not blind. Reviewer 1 is the only fully uninfluenced read. Overlap between readers may be partly inflated by that, so the "flagged by at least two" and "flagged by all three" rows are best read as consistency of separate reads, not as confirmation from uninfluenced readers.
- **The reviewers differ in how much they flag.** Reviewer 3 made the most flags (121, against 87 and 64) and 54 of its passages were flagged by no one else. More flags from one reviewer can mean a closer read or a looser one; this run can't tell which.
- **Flags are leads.** Each one points at a passage worth a human check against the article and its sources.
- **Small numbers.** Ratios built on 0 to 3 flags on one side, and rates for short articles, can swing a lot with a single flag.
- **The reading was strict.** Arguments the article only reports, section headings and loaded wording were not flagged. An article can read as one-sided and still have few flags.
- **Side is a judgement call** about which side one faulty step helps. It is not a verdict on the whole article.
- **Snapshot date.** All text is from 2026-10-01. The live pages may have changed.
