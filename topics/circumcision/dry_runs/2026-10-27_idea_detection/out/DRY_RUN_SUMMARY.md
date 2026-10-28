# Dry-run summary — idea_detection METHOD records

**Date:** 2026-10-27 (America/Los_Angeles)  
**Tip commit:** `bfcbc8b` (`fallacy_catalog` main; PR #7 squash-merged)  
**Passages:** `topics/circumcision/dry_runs/2026-10-27_idea_detection/passages.jsonl` (17 lines)  
**Package:** not modified (read-only check + render)

## Pilot coverage caveat

Only entries with patterns in `idea_detection/pilot_ir_patterns.json` can fire (13 pilots today: ad-hominem, appeal-to-authority, equivocation, false-cause, begging-the-question, cherry-picking, straw-man, argument-from-ignorance, hasty-generalization, slippery-slope, false-dilemma, appeal-to-the-people, guilt-by-association). Most catalog entries cannot flag yet. A `no_issue` row means “this pilot pattern did not match,” not “the passage is fallacy-free.”

Every METHOD-shaped record below is an **assist / lead-to-check**, not a hand METHOD verdict. Spans cannot support every catalog condition; outside-text gaps and excerpt boundaries cap matches at `possible_issue`.

## Counts

| Metric | N |
| --- | ---: |
| Passages | 17 |
| Idea IR files written / schema-ok | 17 / 17 |
| Extract / load errors | 0 |
| Checker report ok | 17 |
| Atom rows: `flag` | 0 |
| Atom rows: `possible_issue` | 3 |
| Atom rows: `no_issue` | 218 |
| Passages with any flag | 0 |
| Passages with any possible_issue | 3 |
| Passages with only no_issue (pilots) | 14 |

## Possible issues (leads to check)

| Passage id | Entry | Why capped / note |
| --- | --- | --- |
| `circ-circumcision-controversies-01` | appeal-to-authority | Outside-text gap: whether experts disagree / source trust / misquote; AAP + systematic reviews cited |
| `circ-religion-and-circumcision-01` | equivocation | Sense split on “circumcision” (physical vs heart) in IR terms/bindings; excerpt boundary → possible_issue. Lead only — theological contrast may be intentional, not a fallacy |
| `circ-views-on-circumcision-01` | argument-from-ignorance | “no evidence of … harm” → absence-as-proof pattern; excerpt boundary → possible_issue |

No `flag` rows.

## Outputs

- IRs: `irs/{id}.json` (17 files)
- Checker dump: `out/check_reports.json`
- METHOD markdown: `out/method_records.md`
- METHOD JSONL (flag + possible_issue only): `out/method_records.jsonl` (3 rows)
- This summary: `out/DRY_RUN_SUMMARY.md`

## Extraction notes

- Blind extract per `EXTRACTOR_PROMPT.md` (no `expected_checker`, no fallacy names in IR).
- All passages marked `excerpt: true` (article snapshots).
- Charity: hedges kept weak where the text says may/potentially; attributed speakers kept; anti-collapse edges used where premise→conclusion cues appear.
- Religion passage: term senses for physical vs spiritual “circumcision” recorded so the checker could see a sense shift; that is graph fidelity, not a verdict.

## Next

Hand METHOD review on the three possible_issue leads if worth it; otherwise treat as pilot smoke for the record renderer. Broader catalog coverage needs more `ir_pattern` pilots.
