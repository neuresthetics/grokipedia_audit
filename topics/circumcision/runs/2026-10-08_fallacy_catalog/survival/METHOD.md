# What survived: method (reduction and mapping)

This file explains how `survival_scores.csv` and `SURVIVORS.md` were built, so another AI or a person can redo and check it. It covers the 58 circumcision article snapshots dated 2026-10-01 and the three reviewers' fallacy flags from the 2026-10-08 fallacy_catalog run. Built on 2026-10-08. Every sentence's side was labeled by an AI model, not a person, and nothing here has been checked by a person yet.

**In one line:** every prose sentence that argues for or against the practice starts with 3 points and loses 1 point for each reviewer whose flag quote overlaps it. Survival means "not flagged", not "true".

## 1. Inputs

| Input | What it is |
|---|---|
| `../../../ARTICLE_LIST.md`, `../../../articles/<slug>/snapshots/2026-10-01.txt` | The 58 articles and their saved text |
| `../scripts/split_units.py` | The run's own sentence split (the same one behind `citation_stats.csv`): 13,199 prose sentences, 8,778 in the 39 male circumcision articles and 4,421 in the 19 FGM articles. Headings and table rows are not sentences. |
| `../flags.csv`, `../reviewer2_flags.csv`, `../reviewer3_flags.csv` | Reviewer 1 (87 rows), Reviewer 2 (64), Reviewer 3 (121) |
| `../scripts/compare_reviewers.py` | Its `span()` function finds each flag quote's character span in the snapshot. It is reused here unchanged. |

**Groups:** an article is in the FGM group if its slug contains `female`, or if it is `clitoridectomy`, `gishiri-cutting` or `infibulation`. All other articles are in the male circumcision group. This is the same rule the run and the charts use.

## 2. What counts as an argument

An argument sentence is one whose claim, as written, supports a side about the practice:

- **Pro:** for the practice or playing down its harm. That includes claimed benefits, safety, low complication rates, no effect on sexual function, a right to do it (parental or religious freedom), and dismissing its critics. In FGM articles, pro means defending FGM or playing down its harm, including reported rationales such as hygiene or chastity that are put forward as reasons for it.
- **Anti:** against the practice. That includes harms, complications, deaths, rights, consent or ethics objections, critics' stated arguments, and calls to end it.
- **Left out (not_argument):** sentences that are descriptive or neutral. That covers procedure steps, history, prevalence figures, statutes and court rulings stated as facts, sentences balanced with no net direction, and claims about something else. "Something else" includes whether a law or campaign worked, race science in the Montagu article, and treating phimosis with steroids. **These sentences are not scored at all.** "Uncertain" also counts as not an argument.
- **Reported arguments count.** "Critics argue X" is an anti argument sentence even though the article only reports it. That differs from the flagging rules, where reported arguments are not flagged. As a result, many sentences in the inventory could never have been flagged (see Limits).
- **Rule R5 (which practice):** the side is judged for the practice of the article's group. In a male circumcision article, a sentence that sets male circumcision apart from FGM as less harmful is pro, and a sentence only about FGM that does nothing for the male circumcision case is not an argument. In an FGM article, a sentence about male circumcision's benefits that is used to show FGM is worse is anti. In articles about a related practice (subincision, traditional initiation, infibulation), the practice is the one the article is about.
- **Mixed sentences** ("X, though Y") are labeled by the side the sentence ends up favoring. If the sentence is truly balanced, it is not an argument.
- The full instructions given to the labeling model are in [LABEL_PROMPT.md](LABEL_PROMPT.md).

## 3. Building the inventory (model labels for every sentence)

**Every one of the 13,199 prose sentences was labeled by an AI model, not a person.** Each got pro, anti or not_argument (`labels/model_labels.csv`, `label_method = model`). The labeling worked like this:

- **Tool:** `scripts/label_queue.py` serves one article at a time in batches of up to 80 sentences. Each batch shows the article title, its group and the sentences, plus two context sentences on each side. Citation markers are removed for reading. The tool never shows the rule labels or any reviewer flag, and the labelers were told not to open the files that contain them. Answers are saved after every batch, so the job could stop and resume.
- **Instructions:** [LABEL_PROMPT.md](LABEL_PROMPT.md), the same definitions and rules as section 2.
- **Who:** 9 separate model sessions (`labeled_by` = labeler-1 to labeler-9), split by article. Each session labeled whole articles, apart from `redundant-prepuce`, which labeler-3 and labeler-9 split, 80 and 87 sentences. Judgment was made batch by batch, and **no labeler cross-checked another's work**. Different labelers may therefore draw borderline lines differently. See the consistency check below.

**Inventory: 2,616 argument sentences** (19.8% of all sentences):

| Group | Sentences | Pro | Anti | Not an argument |
|---|---|---|---|---|
| Male circumcision (39 articles) | 8,778 | 971 | 728 | 7,079 |
| FGM (19 articles) | 4,421 | 301 | 616 | 3,504 |

**Rule labels, for comparison only.** The rule script from the first version (`scripts/rules.py`, `scripts/stage1_candidates.py`) is kept and its label is stored in the `rule_side` column of `sentence_labels.csv`, `argument_inventory.csv` and `survival_scores.csv`. It plays no part in scoring.
- The rules gave the same label as the model on **9,787 of 13,199 sentences (74.1%)**. A rule "mixed" never counts as a match.
- Where they differ, the rules mostly called a sentence an argument when the model did not: 957 rule-anti and 555 rule-pro sentences are not arguments to the model. The rules also missed 930 sentences the model calls arguments: 538 pro and 392 anti.
- The full cross-table is in `summary.json` (`rules_vs_model`).
- The 957 sentences labeled by a model in the first version, which saw each sentence without context, got the same label again in 834 cases (87.1%).

**Consistency check by labeler** (from `summary.json`, `by_labeler`):

| Labeler | Articles | Sentences | Pro | Anti | Not an argument | Rule cue share | Same as rules | Flagged sentences called arguments |
|---|---|---|---|---|---|---|---|---|
| labeler-1 | 8 | 1,687 | 9.7% | 9.4% | 81.0% | 24.1% | 75.8% | 10 of 17 |
| labeler-2 | 5 | 1,352 | 11.9% | 8.5% | 79.6% | 34.8% | 68.0% | 14 of 23 |
| labeler-3 | 6 | 1,400 | 17.3% | 10.7% | 72.0% | 26.4% | 70.6% | 9 of 14 |
| labeler-4 | 5 | 1,326 | 8.7% | 15.4% | 75.9% | 24.9% | 72.5% | 12 of 22 |
| labeler-5 | 8 | 1,688 | 5.4% | 11.5% | 83.1% | 27.7% | 75.9% | 4 of 12 |
| labeler-6 | 7 | 1,645 | 5.2% | 6.2% | 88.6% | 22.6% | 78.1% | 3 of 14 |
| labeler-7 | 6 | 1,488 | 15.3% | 10.0% | 74.7% | 29.7% | 70.2% | 28 of 38 |
| labeler-8 | 7 | 1,630 | 7.6% | 10.7% | 81.7% | 25.3% | 76.4% | 7 of 13 |
| labeler-9 | 7 | 983 | 6.3% | 10.0% | 83.7% | 20.0% | 79.3% | 2 of 10 |

"Rule cue share" is the share of that labeler's sentences in which the rule script found any cue. It is a rough guide to how argumentative the articles were. Articles differ a lot, so the rates are not directly comparable. Two labelers stand apart even after allowing for that:
- **labeler-6 looks strictest.** It called 11.4% of sentences arguments against a 22.6% cue share (ratio 0.51), and only 3 of its 14 flagged sentences arguments. Its articles are mostly descriptive (holy-prepuce, phimosis, paraphimosis, mohel, prevalence of FGM, FGM in Sudan, foreskin-man), which explains part of this.
- **labeler-3 looks most inclusive.** It called 28.0% of sentences arguments against a 26.4% cue share (ratio 1.06). Across all labelers the ratio is 0.75.
- labeler-5 (ratio 0.61) and labeler-9 (2 of 10 flagged sentences called arguments) also lean strict.

None of this was corrected. A second model or a person relabeling the articles of labeler-6 and labeler-3 would be the first check to run.

**Verbatim check:** `build_survival.py` takes each statement straight from the snapshot by its character span. It then checks that the slice matches the split sentence word for word and can be found in the snapshot. All 13,199 pass. Citation markers like `[4]` are part of the verbatim text.

## 4. Mapping flags to sentences (matching rule)

This uses the same rule as `compare_reviewers.py`: same article, and the character spans overlap. Each flag quote is located with `compare_reviewers.span()`, and all 272 are located. A flag is mapped to **every** sentence its span overlaps, so a quote that runs over two sentences hits both; 2 flags do. That gives 274 flag-sentence pairs, all listed in `flag_sentence_map.csv`. Of the 272 flags, 160 touch at least one argument sentence. The other 112 touch only sentences the model calls not an argument (44 neutral, 50 anti, 18 pro). They are logged and not scored. Of the 163 sentences that any flag touches, the model called 89 arguments.

## 5. Scoring

For each argument sentence, `rK_hit = 1` if Reviewer K has at least one flag mapped to it. Several flags from the same reviewer on one sentence still cost only 1 point. Then `points_left = 3 − r1_hit − r2_hit − r3_hit`. A flag costs a point whatever side it gives (pro, anti or neutral) and whether its verdict is "flag" or "possible issue". The catalog entries that hit each sentence are in `r1_entry_ids`, `r2_entry_ids`, `r3_entry_ids` and `entry_ids`.

## 6. Conflicts

A conflict is a flag-sentence pair where the flag's `favors` differs from the model's label. **The model's label is always kept**, and every conflict is logged in `conflicts.csv`. There are 77 pairs from 77 flags:

| Type | Pairs | Scored? |
|---|---|---|
| Flag says anti, model says not an argument | 51 | no |
| Flag says pro, model says not an argument | 18 | no |
| Flag says pro, model says anti | 4 | yes, as anti |
| Neutral flag on an anti sentence | 2 | yes |
| Neutral flag on a pro sentence | 2 | yes |

Neutral flags on not-argument sentences are not conflicts.
- **The 51 anti flags left out:** most are in FGM law, prevalence and policy articles (FGM Act 2003: 8; FGM in New Zealand, FGM in the United States, prevalence of FGM, the 1985 Act and FGM laws by country: 4 each) or in restoration-device (5). Most are inconsistency, false cause or cum hoc flags on claims that a law or campaign worked. Under section 2 those are policy-effect claims, not arguments about the practice.
- **The 4 pro-vs-anti pairs (3 sentences):** all are in FGM articles, on sentences that contrast FGM with male circumcision to show FGM is worse. The reviewers read them as pro (for male circumcision); rule R5 reads them as anti (against FGM).

## 7. Results

| Group | Side | Arguments | 3 left | 2 | 1 | 0 | Untouched |
|---|---|---|---|---|---|---|---|
| Male circumcision | pro | 971 | 910 | 26 | 15 | 20 | 93.7% |
| Male circumcision | anti | 728 | 724 | 2 | 2 | 0 | 99.5% |
| FGM | pro | 301 | 291 | 5 | 1 | 4 | 96.7% |
| FGM | anti | 616 | 602 | 9 | 4 | 1 | 97.7% |

**Compared with the first version** (rule labels for most sentences):
- The inventory shrank from 3,282 to 2,616 sentences: male pro 878 to 971, male anti 1,144 to 728, FGM pro 375 to 301, FGM anti 885 to 616.
- The shares untouched barely moved: male pro 92.7% to 93.7%, male anti 99.5% to 99.5%, FGM pro 96.5% to 96.7%, FGM anti 97.6% to 97.7%.

**Robustness check: left-out flags.** Suppose the flagged sentences the model calls not an argument were counted on the side most of their non-neutral flags give (ties and neutral-only flags left out). That adds 8 male pro, 7 male anti, 5 FGM pro and 30 FGM anti sentences:

| Group | Pro untouched | Anti untouched |
|---|---|---|
| Male circumcision | 92.9% | 98.5% |
| FGM | 95.1% | 93.2% |

**The FGM order still flips**, so the FGM anti side becomes the more flagged one. The male circumcision result does not change direction. The numbers are in `summary.json` (`if_dropped_flagged_sentences_counted`).

**Reading:**
- In the male circumcision articles, pro arguments are flagged far more often than anti ones: 6.3% vs 0.5%. That holds under every check.
- In the FGM articles the two sides are close (3.3% pro vs 2.3% anti flagged). Which side comes out ahead depends on whether claims about laws and campaigns count as arguments. Do not read a winner into the FGM result.

## 8. Known limits

- **Labels come from an AI model, not a person, in 9 separate sessions.** Each session labeled its own articles batch by batch, and no session checked another's. Borderline sentences may be called differently in different articles. The consistency check in section 3 shows labeler-6 leaning strict and labeler-3 leaning inclusive. To redo the labels, give `LABEL_PROMPT.md` and `scripts/label_queue.py` to a different model or a person, then compare their labels with `labels/model_labels.csv`.
- **The policy-claim exclusion matters for FGM.** Leaving out claims about whether laws or campaigns worked removes many anti-favoring flags. That choice is what decides the FGM order (section 7).
- **The reviewers were not blind.** The instructions for Reviewers 2 and 3 mentioned earlier results (see the run README). Overlap between them may be inflated, and that affects the 1- and 0-point counts.
- **Flags are leads, not verdicts.** A lost point means an AI reviewer flagged the reasoning, not that the claim is false. Kept 3 points means not flagged, not true and not well argued. It can also mean the sentence only reports someone else's argument, which the reviewers were told not to flag.
- **Sentence split is rule-based** (abbreviations and citation markers can split or join sentences wrongly), as in `citation_stats.csv`. A few "sentences" are only a citation marker; they read as empty and are labeled not an argument.
- **The unit is the sentence.** A long sentence counts the same as a short one, and an argument spread over three sentences counts three times.

## 9. File lineage and how to rebuild

```
snapshots + ARTICLE_LIST.md ──► ../scripts/split_units.py ──► scripts/sentences.py (sentence spans)
flags.csv, reviewer2_flags.csv, reviewer3_flags.csv ──► ../scripts/compare_reviewers.py span()
        └──► scripts/stage1_candidates.py (+ scripts/rules.py) ──► work/sentences_stage1.csv
             (spans, rule label for comparison, flag overlap; never shown to the labelers)
LABEL_PROMPT.md ──► scripts/label_queue.py (next / record) ──► [9 AI model sessions] ──► labels/model_labels.csv
work/sentences_stage1.csv + labels/model_labels.csv + flags ──► scripts/build_survival.py ──►
        sentence_labels.csv, argument_inventory.csv, survival_scores.csv, flag_sentence_map.csv,
        conflicts.csv, summary.json, SURVIVORS.md, SURVIVORS_3_points_<side>_<group>.md
survival_scores.csv ──► tools/make_charts_2026_10_08.py ──► docs/img/circumcision/2026-10-08/05_what_survived.png
work/v1_model_labels_sentence_only.csv: the first version's 957 model labels (no context), kept only for the comparison in section 3
```

To rebuild from the repo root (needs Python 3; the chart also needs matplotlib):

```
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/survival/scripts/stage1_candidates.py
python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/survival/scripts/build_survival.py
python3 tools/make_charts_2026_10_08.py
```

Every step except the labeling is deterministic. The labels are fixed in `labels/model_labels.csv`. `build_survival.py` refuses to run until every sentence has a label; `--partial` writes a preview to `work/preview/` instead.

## Columns

- `sentence_labels.csv`: all 13,199 sentences: `article`, `sentence_id`, `topic_group`, `model_side` (pro/anti/not_argument), `rule_side` (comparison only), `label_method`.
- `labels/model_labels.csv`: `slug`, `sentence_id`, `model_side`, `batch`, `labeled_by`, `labeled_at`.
- `argument_inventory.csv`: `article`, `sentence_id` (s0001… in reading order, prose sentences only), `text` (verbatim), `side` (pro/anti), `topic_group` (male/FGM), `label_method` (model), `rule_side` (comparison only).
- `survival_scores.csv`: the same columns, plus `r1_hit`, `r2_hit`, `r3_hit` (0/1), `points_left` (0–3), `r1_entry_ids`, `r2_entry_ids`, `r3_entry_ids` and `entry_ids` (catalog entry ids, separated by `|`).
- `flag_sentence_map.csv` and `conflicts.csv`: `reviewer`, `flag_row` (data row number in that reviewer's CSV, 1 = first row under the header), `slug`, `entry_id`, `favors`, `sentence_id`, `inventory_side`, `conflict`, `quote`.
