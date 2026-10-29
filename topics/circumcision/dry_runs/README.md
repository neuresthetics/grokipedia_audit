# Circumcision: idea_detection dry runs (2026-10-27 to 2026-10-28)

**Status:** dry runs of the [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) `idea_detection` checker on the circumcision argument inventory. Every output is an *assist lead* (a lead to check), not a hand verdict.

**Terms.** `flag`: a pilot pattern matched and every condition it tests was met in the text. `possible_issue`: a pattern matched but at least one condition depends on facts outside the excerpt (for example, whether a cited body is expert or trustworthy). `no_issue`: no pilot pattern matched; this does not mean the passage is free of fallacies. *Nested peel*: re-checks each lead with wider context (article snapshot window, cite text); a lead *survives* if every peel closes with no issue, *breaks* otherwise, either as `flagged` (a hard flag closed) or `open` (still unresolved).

## Runs

| Run | Input | Result | Summary |
|---|---|---|---|
| Pilot, 2026-10-27 | small set of verbatim snapshot excerpts | renderer test only | [README](2026-10-27_idea_detection/README.md) |
| Flat, 2026-10-28 (fallacy_catalog `bfcbc8b`) | 2,616 passages from the 2026-10-08 pro/anti argument inventory | 0 `flag`; 452 `possible_issue` on 450 passages (appeal-to-authority 426, argument-from-ignorance 18, false-cause 6, begging-the-question 2) | [RUN_SUMMARY](2026-10-28_idea_detection_full/out/RUN_SUMMARY.md) |
| Nested, 2026-10-28 (fallacy_catalog `f304b80`) | the 450 lead passages + [`contexts.jsonl`](2026-10-28_idea_detection_full/CONTEXT_MAP_README.md) (450/450 covered) | survives 1; breaks 449 (flagged 25, open 424); max depth 3 | [RUN_SUMMARY](2026-10-28_idea_detection_full/nested_out/RUN_SUMMARY.md) |
| Self-pass, 2026-10-28 (`bfcbc8b`) | 98 passages from fallacy_catalog's own method docs | 0 `flag`; 4 `possible_issue` | [README](2026-10-28_self_pass_fallacy_catalog/README.md) |

## Reading the numbers

- Most of the 424 open breaks are citation-expertise gaps: the passage names a source, and the context map does not carry facts about that source's expertise or agreement with other experts. They are a queue for bibliography review, not 424 established fallacies.
- The 25 flagged breaks are the suggested first queue for human review. By theme: HIV/VMMC efficacy and "no evidence of risk compensation" wording (argument-from-ignorance); FGM law and harm claims ("no evidence of benefit"); historical medical claims moving from association to cause (false-cause); and culture/rights pages.
- The single survivor (`circ-forced-circumcision-s0041`) closed softly through a cite peel; it is not a cleared passage.

## Limitations

- Only 13 pilot patterns exist, so most catalog entries cannot fire.
- Input is the 2026-10-08 sentence inventory, not a fresh carve of the snapshots.
- Cite expansion is missing for 16 passage ids (see nested RUN_SUMMARY).
- All labels come from AI tooling; none is a human expert ruling.
