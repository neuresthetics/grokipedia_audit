# Recheck instructions (step 6, pass 3: do the remaining pro arguments hold up?)

You are checking pro argument sentences from Grokipedia articles on male circumcision against the fallacy catalog. This is one pass of a public audit. Your answers are recorded as a model's judgment, not a person's.

## What you check

Each item is one sentence that an earlier step labeled a **pro** argument (it favours the practice). You see the sentence, the section it sits in, the three sentences before it and the one after it. You may open the article snapshot for more context: `topics/circumcision/articles/<slug>/snapshots/2026-10-01.txt`.

The question: **does this sentence's own reasoning hold up, or does it commit a fallacy from the catalog?**

## The catalog and the method

- Catalog: [neuresthetics/fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1, commit `2a56493a3931018e9143bc7235f152f5cc5b459e`. Entries: `FALLACIES.md` (or `fallacies.json`) at that commit. Use entry ids exactly as in the catalog.
- Method: the catalog's `METHOD.md` at that commit, steps (a) to (g). In short: restate the step in its strongest reasonable form; pick the most specific entry (fallbacks such as non sequitur and false cause only when nothing more specific fits); check **every** required condition against the words on the page; rule out each legitimate look-alike; then give a verdict.
- **flag**: every condition is met from the text (or common knowledge) and no look-alike applies.
- **possible_issue**: a condition depends on facts not in the text, or a look-alike might apply. Only a flag costs a point; possible issues are recorded but not counted.
- **no_issue**: no condition-complete fallacy. Most sentences should be no_issue.

## Working rules (the same ones the three reviewers used)

- Judge only reasoning in the **article's own voice**. A sentence that reports, quotes or attributes a view ("The AAP concluded…", "Proponents argue…", "Critics contend…") is no_issue, even if the reported view is weak.
- Sections titled as one side's case count as reported material; flag there only where the article clearly argues in its own voice.
- A plain factual statement with no inference is no_issue. Wrong figures, dates and other factual slips are not fallacies.
- Loaded or charged wording that no inference rests on is not a flag.
- An observational-to-causal health claim is not flagged when the mechanism is well known (for example UTI or penile cancer and the foreskin).
- Using adult African HIV trial results as if they settle infant circumcision or low-prevalence settings is secundum quid (`secundum-quid`).
- Where the article contradicts itself and the contradiction carries an argument, use `inconsistency`, and quote or cite the other passage in the reason. A plain number or date mismatch is a factual slip, not a flag.
- Never use entries whose `text_detectable` is "no".
- Two entries on one sentence only if there are two separate errors, each meeting its own conditions. Do not stack labels from the same family.

## What you must not open

Do not open the earlier reviewers' flag files (`flags.csv`, `reviewer2_flags.csv`, `reviewer3_flags.csv`, overlap or agreement files), anything under `survival/`, anything under `flagged_pro/` other than this prompt and the queue output, the run README, ANALYSIS.md, or the charts. Do not look at other checkers' answers in `work/findings.csv`. Judge only from the sentence, its article and the catalog.

## How to answer

One or more lines per item, then the next item:

```
r0001 no_issue
r0002 flag secundum-quid | <exact words from the sentence> | <one line: the step, the conditions met, the look-alike ruled out>
r0003 possible_issue appeal-to-authority | <exact words> | <one line, and what fact would settle it>
```

- The quote must be an exact substring of the item's sentence (citation markers may be left out at the ends). The script rejects anything else.
- The entry id must exist in the catalog at that commit and be text-detectable.
- One line per distinct fallacy. An item with any flag or possible_issue line needs no no_issue line.
- Keep reasons about the reasoning. Do not add facts that are not in the article or common knowledge.
