# RUN_SUMMARY — fallacy_catalog doctrine self-pass (flat) 2026-10-28

**Published:** 2026-10-28 on grokipedia_audit `main` in commits [`368a337`](https://github.com/neuresthetics/grokipedia_audit/commit/368a337) and [`1ade5c1`](https://github.com/neuresthetics/grokipedia_audit/commit/1ade5c1). Artifact text below is the run record as produced; leads are assists, not hand verdicts.

**Date:** 2026-10-28 (America/Los_Angeles)
**Tip commit:** `bfcbc8b` (`fallacy_catalog` main; METHOD record renderer from #7)
**Passages:** `topics/circumcision/dry_runs/2026-10-28_self_pass_fallacy_catalog/passages.jsonl` (98 lines)
**Source:** claim-bearing doctrine from METHOD / IDEA_DETECTION / IDEA_LEVEL / NESTED_LAYERS / EXTRACTOR_PROMPT (+ sparse pilot prose)
**Checker:** flat only (`python3 -m idea_detection`); nested NOT used (PR #8 not merged)
**Package:** not modified (read-only extract + check + render)
**Git:** ~~local only under gta_repo; not pushed~~ (superseded: published, see note above)

## Pilot coverage caveat

Only entries with patterns in `idea_detection/pilot_ir_patterns.json` can fire (13 pilots).
A `no_issue` row means “this pilot pattern did not match,” not “the passage is fallacy-free.”
Doctrine text is often definitional / instructional — many genuine no_issue expected.

Every METHOD-shaped record below is an **assist / lead-to-check**, not a hand METHOD verdict.
`substitute_for_hand_method` is always false.

## Counts

| Metric | N |
| --- | ---: |
| Passages | 98 |
| Idea IR files written / schema-ok | 98 / 98 |
| Extract / load errors (still invalid) | 0 |
| Checker report ok | 98 |
| Atom rows: `flag` | 0 |
| Atom rows: `possible_issue` | 4 |
| Atom rows: `no_issue` | 1270 |
| Passages with any flag | 0 |
| Passages with any possible_issue | 4 |
| Passages with only no_issue (pilots) | 94 |

### Extractor model tags

- `cue-extractor-v1`: 98

### possible_issue by entry

| Entry | N |
| --- | ---: |
| `appeal-to-authority` | 2 |
| `argument-from-ignorance` | 1 |
| `guilt-by-association` | 1 |

## Flags

No `flag` rows (0). Excerpt boundary + outside-text caps keep hard flags at zero for this set.

## Possible issues (leads to check)

Full machine list in `out/leads.json` and `out/method_records.jsonl` (4 rows).

| Passage id | Entry | Verdict | Why capped / note |
| --- | --- | --- | --- |
| `self-METHOD-007` | argument-from-ignorance | possible_issue | possible issue; excerpt boundary — support may lie outside the passage |
| `self-METHOD-012` | appeal-to-authority | possible_issue | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the sourc… |
| `self-METHOD-022` | appeal-to-authority | possible_issue | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the sourc… |
| `self-idea_detection-EXTRACTOR_PROMPT-010` | guilt-by-association | possible_issue | possible issue; excerpt boundary — support may lie outside the passage |

## Reading the 4 leads (honest)

These are cue-extractor + pilot-pattern assists on *doctrine describing fallacies*, not adversary prose:

1. `self-METHOD-007` / argument-from-ignorance — METHOD text that *explains* the ignorance+causal example contains the cue phrase “never been proven”; excerpt-boundary `possible_issue`. Lead to check that the extractor did not treat instructional example as a live argument.
2. `self-METHOD-012` / appeal-to-authority — second-reviewer wording tripped a thin `who` authority cue; missing outside-text facts → `possible_issue`. Soft lead.
3. `self-METHOD-022` / appeal-to-authority — look-alike prose about “genuine experts” fired authority pattern with open outside-text condition.
4. `self-idea_detection-EXTRACTOR_PROMPT-010` / guilt-by-association — EXTRACTOR_PROMPT *worked example* of association (“housing plan… developer…”) intentionally contains the pattern; expected self-hit on example prose.

None of these are hand METHOD verdicts that the doctrine itself is fallacious. They are assists that the cue IR + pilot stack can fire on instructional text.

## Artifacts

- IRs: `irs/*.json` (98)
- Checker dump: `out/check_reports.json`
- METHOD markdown: `out/method_records.md`
- METHOD JSONL (flag + possible_issue only): `out/method_records.jsonl` (4 rows)
- Leads index: `out/leads.json`, `out/counts.json`
- Extract errors: `out/extract_errors.jsonl` (empty)
- This summary: `out/RUN_SUMMARY.md`

## Hold

Local-only; do not push. Nested self-pass waits on Jason’s OK to merge PR #8. Package tip left at `bfcbc8b`; fallacy_catalog files not edited.
