# FALLACY pass (snapshot 2026-10-15)

Catalog: neuresthetics/fallacy_catalog, version 0.6.1, commit 2a56493a3931018e9143bc7235f152f5cc5b459e (`fallacies.json`, 221 entries). The procedure follows that repo's METHOD.md: quote the passage, give the strongest reading, pick the most specific entry, check each required condition, rule out look-alikes, then give a verdict (flag / possible issue / no issue).

## Reviewers: not independent

There is no second model or person on the box. Both reads were done by the same checker (Grok Bot) in the same session.
- Read 1 (R1): a straight read of all 401 sentences, in order.
- Read 2 (R2): a screen first. `scripts/fallacy_candidates.py` lists 230 sentences that contain an inference or evaluation word (thus, underscores, indicating, akin to, scholars, ...). Each was then re-checked against the catalog conditions. R2 did not open the R1 file, but R1 was still in the same checker's memory.

So these are two passes by one reader, not two independent reviews. Where both passes flagged the same passage, that shows consistency, not independent confirmation. Flags are leads, not verdicts.

## Counts (`scripts/fallacy_compare.py` → `data/fallacy_compare.csv`)

- R1: 8 passages (4 flag, 4 possible issue). R2: 9 passages (4 flag, 5 possible issue).
- 8 passages were flagged by both reads. In 4 of them both reads gave a full flag with the same entry; in 3 both gave possible issue with the same entry; 1 has the label disputed.
- 1 passage was flagged in R2 only. R1 had no passages of its own.

| Sentence | R1 | R2 | Passage (verbatim) |
|---|---|---|---|
| C129 | proof-surrogate, flag | same | "Scholars compare natura naturans ..." (sentence carries no cite) |
| C261 | cum-hoc, flag | same | "separation correlates with tolerance and intellectual progress" |
| C342 | non-sequitur, flag | same | "causally inert and thus nonexistent in orthodox terms" |
| C381 | non-sequitur, flag | same | "This rejection persisted ... underscoring the causal incompatibility" |
| C046 | false-dilemma, possible | same | "failed, indicating deeply entrenched heterodoxy rather than mere youthful rebellion" |
| C113 | hasty-generalization, possible | same | "Such exchanges underscore Spinoza's reluctance to publish unfinished works" |
| C401 | loaded-language, possible | same | "relevant to contemporary struggles against illiberalism" |
| C159 | loaded-language, possible | straw-man, possible | "Descartes' dualism thus fragments reality into competing finite entities" |
| C314 | — | loaded-language, possible | "rendering the Tractatus Politicus a bold defense of republican principles" |

C342, C381 and C261 are in the article's own voice, not reports of someone else's argument.

## Other notes (not fallacies)

- C330 says Spinoza died "from pulmonary issues caused by lens-grinding dust" as a fact. C065 and C117 hedge the same point ("likely").
- C368: "the 1678 papal condemnation". No source found for it (see claim_log). This is a factual problem, not a reasoning error.
- C182 and C184 say the method "ensure[s] logical progression" and is "preventing gaps". These are unhedged claims of success, though C190 itself reports a charge of circularity.
- Checked and dropped: C130 (the Daoist "akin to" is an illustration, not an argument), C047, C368 as false cause (no causal support is offered at all, so the conditions are not met), and C395 (it has a checkable cite).
