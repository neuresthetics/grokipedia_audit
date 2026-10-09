# Analysis: circumcision articles, fallacy_catalog run (2026-10-08)

A short read of what the three reviews found. The full method and file list are in [README.md](README.md). Every number here comes from the committed CSVs in this folder. The charts are drawn by [`tools/make_charts_2026_10_08.py`](../../../../tools/make_charts_2026_10_08.py), which prints each number it plots.

## What was done

- **Articles:** the 58 circumcision-related Grokipedia articles saved on 2026-10-01. Nothing was fetched again.
- **Checklist:** [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1, commit `2a56493`, used with its METHOD.md.
- **Reviewers:** Reviewer 1, 2 and 3. Three separate AI agents each read all 58 articles and wrote their own flags. Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, and each reports it did not, but their instructions came from a conversation that had already discussed earlier results (Reviewer 2: Reviewer 1's totals, top articles and fallacy types; Reviewer 3: counts and example quotes from Reviewers 1 and 2), so they were not blind. Reviewer 1 is the only fully uninfluenced read. Their results are shown side by side, not merged.
- **Flag:** a passage where the article's own reasoning is flawed, matched to a catalog entry. A flag is a lead for a human to check, not a verdict.
- **Passage:** flags from different reviewers count as the same passage when their quotes overlap in the same article (`overlap_3way.csv`).
- **Flagged by at least two / by all three:** that many reviewers, reading separately, flagged the passage and gave it the same side. This is overlap, not proof that the flag is right.
- **Side:** in male circumcision articles, *pro* means the flaw helps the case for the practice and *anti* the case against it. In FGM articles, *anti* means against the practice and *pro* means defending it or playing down harm. *Neutral* helps neither side.
- **Rate:** flags per 100 sentences = 100 × flags ÷ prose sentences. Sentence counts are the `sentences` column of `citation_stats.csv` (prose sentences in each snapshot, rule-based split). The 58 articles have 13,199 sentences: 8,778 in the 39 male circumcision articles and 4,421 in the 19 FGM articles.

## Headline: which side's case relies more on flawed reasoning?

![Which side's case relies more on flawed reasoning: pro vs anti flags per 100 sentences for Reviewers 1, 2 and 3, in male circumcision and FGM articles, with a check on the cleaner-argued side where the rule applies](../../../../docs/img/circumcision/2026-10-08/01_which_side.png)

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

## Which articles have the most flawed reasoning per sentence?

![Top 10 articles by flagged reasoning per 100 sentences, averaged over the three readers and colored by which side the flaws help](../../../../docs/img/circumcision/2026-10-08/02_most_flagged_articles.png)

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

## Male circumcision vs FGM articles, all sides

- **Male circumcision (8,778 sentences):** Reviewer 1 0.60 per 100 sentences (53 flags), Reviewer 2 0.46 (40), Reviewer 3 0.74 (65); flagged by at least two 0.52 (46 passages: 38 pro, 5 anti, 3 neutral); flagged by all three 0.21 (18, all pro).
- **FGM (4,421 sentences):** Reviewer 1 0.77 (34), Reviewer 2 0.54 (24), Reviewer 3 1.27 (56); flagged by at least two 0.63 (28: 7 pro, 13 anti, 8 neutral); flagged by all three 0.16 (7: 4 pro, 1 anti, 2 neutral).
- Reviewer 3 flags the FGM articles at a higher rate than the other two (1.27 per 100 sentences against 0.77 and 0.54), and more than half of its FGM flags are anti (31 of 56).

## How much the reviewers' flags overlap

![How often the readers flagged the same passage: 89 passages by one reader only, 42 by two (41 with the same side), 33 by all three (25 with the same side)](../../../../docs/img/circumcision/2026-10-08/04_reader_overlap.png)

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

## Citation hygiene

![Citation gaps: top 10 articles by share of sentences with no citation marker, with the broken source list on female-genital-mutilation highlighted](../../../../docs/img/circumcision/2026-10-08/03_citation_gaps.png)

- **4,658 of 13,199 prose sentences (35.3%) have no `[n]` citation marker.** The median article is at 35.1%.
- **Highest uncited shares:** circumcision-in-brunei 54.4%, stapler-circumcision 52.4%, female-genital-mutilation 51.9%, cost-of-circumcision-surgery-in-chaozhou 50.6%. **Lowest:** meatal-stenosis 23.8%, foreskin 24.1%.
- **Two broken source lists.** female-genital-mutilation lists 3 sources but uses markers up to [76] (153 markers point past the list). views-on-circumcision lists 2 sources but uses markers up to [114] (139 markers past the list). The saved sources for these two don't match the text, so their citation counts are unreliable.
- Sentence splitting is rule-based, so these shares are approximate.

## What survived: how much of each side's argument was never flagged?

![How much of each side's argument survived the fallacy check: share of pro and anti argument sentences with 3, 2, 1 and 0 points left, in male circumcision and FGM articles](../../../../docs/img/circumcision/2026-10-08/05_what_survived.png)

The headline above counts flaws. This chart asks the reverse question: of the sentences that argue for or against the practice, how many did no reviewer flag? Each argument sentence starts with 3 points and loses 1 point for each reviewer whose flag overlaps it.

- **Male circumcision articles:** 6.3% of pro argument sentences were flagged by at least one reviewer (61 of 971), against 0.5% of anti ones (4 of 728). 20 pro sentences lost all 3 points; no anti sentence did.
- **FGM articles:** the two sides are close: 3.3% of pro (10 of 301) and 2.3% of anti (14 of 616). If flagged claims about whether laws or campaigns worked are counted as arguments, the order flips, so this group has no clear winner.

Survival means "not flagged", not "true". All 13,199 sentences were labeled by an AI model, not a person, in 9 separate sessions split by article, and no session checked another's work. The male circumcision gap holds under every check. The lists, the method, the limits and a consistency check by labeler are in [`survival/`](survival/): [SURVIVORS.md](survival/SURVIVORS.md) and [METHOD.md](survival/METHOD.md).

## Flagged pro arguments: what kinds of flawed reasoning?

![What kinds of flawed reasoning did the flagged pro arguments use: share of flagged pro argument sentences in the male circumcision articles by fallacy family](../../../../docs/img/circumcision/2026-10-08/06_flagged_pro_types.png)

Step 6 covers the male circumcision articles only. It looks at the 61 pro arguments there that lost at least one point and sorts each by the kind of flaw the reviewers named, using fallacy_catalog's own categories.

- **Most common: a reason that doesn't bear on the point** (28, 46%). Examples are answering a consent objection with satisfaction surveys, answering lasting-pain evidence with quick healing, or explaining critics' views by their supposed bias.
- **Next: unearned or clashing premises** (20, 33%). Often the article contradicts itself, for example calling the procedure "near-painless" after saying pain relief falls short. Or it applies a stricter test to the other side's evidence than to its own.
- **Thin or ill-fitting evidence** (9, 15%) is mostly false analogies (5 of 9), such as comparisons with heel-prick blood tests or vaccines.
- Stretched numbers and shaky cause and effect are each primary for 2 sentences.

The quotes, the catalog's definitions and the counter for each family are in [flagged_pro/FLAGGED_PRO.md](flagged_pro/FLAGGED_PRO.md). Flags are leads, not verdicts, and a flagged step can still lead to a true conclusion.

## Flagged pro arguments: did the survivors lean on them, and do they hold up?

![Do the surviving pro arguments hold up: male pro argument sentences by points left at step 5, after the dependence check (pass 2) and after a fresh recheck (pass 3), with anti for reference](../../../../docs/img/circumcision/2026-10-08/07_pro_after_priors.png)

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
