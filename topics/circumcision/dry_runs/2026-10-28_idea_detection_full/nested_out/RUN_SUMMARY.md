# Nested peel run summary — circ leads

**Published:** 2026-10-28 on grokipedia_audit `main` in commits [`368a337`](https://github.com/neuresthetics/grokipedia_audit/commit/368a337) and [`1ade5c1`](https://github.com/neuresthetics/grokipedia_audit/commit/1ade5c1). Artifact text below is the run record as produced; leads are assists, not hand verdicts.

**Package tip:** `f304b80` (`f304b807d945c708be21d0495bc56c4076931dcd`)  
**Dry-run:** `/workspace/gta_repo/topics/circumcision/dry_runs/2026-10-28_idea_detection_full`  
**Output:** `/workspace/gta_repo/topics/circumcision/dry_runs/2026-10-28_idea_detection_full/nested_out`  
~~Local only — not pushed.~~ (superseded: published, see note above)

## Input
- Lead seeds: **450** unique passage_ids from `out/leads.json` (0 flags + 452 possible_issues → 450 unique)
- All 450 IR files present under `irs/`
- Context coverage: **450/450** lead ids in `contexts.jsonl` (1032 lines: 450 snapshot_window `full:true`, 582 cite)
- MISSING cite expands: **24** lines / **16** unique passage_ids (README notes 20 missing ref numbers; some lines bundle multiple refs / targets)

## CLI
```bash
cd /workspace/fallacy_catalog
python3 -m idea_detection.nested \
  --context-map …/contexts.jsonl \
  --method-record --json \
  …/nested_out/lead_irs
```
- `--max-depth` omitted (unlimited; cycle detection still applies)
- Wall clock ~3.1s; single run; no OOM; **0 failures**
- Package source untouched; no git push

## Stress / outcome (seed level)
| | count |
|---|---|
| survives | 1 |
| breaks | 449 |
| breaks → flagged | 25 |
| breaks → open | 424 |

Outcome hist: `{'open': 424, 'flagged': 25, 'survives': 1}`

Doctrine reminder: philosophy survives / sophistry breaks. These are **assist leads**, not hand METHOD verdicts.

## Depth (checked IR nodes via peel.child)
- Max depth reached: **3**
- Mean of per-tree max depth: **1.3111**
- Mean depth all checked nodes: **1.0342**
- Per-tree max-depth hist: `{'1': 329, '2': 102, '3': 19}`
- Trees with checked depth > 0: **450**
- Checked nodes total: 1463
- Peels total: 2672 (with checked child: 1013; empty_expander: 590)
- Peel kind hist: `{'cite': 2039, 'atom': 442, 'premise': 148, 'excerpt': 43}`

## Flags / opens at layers
- Trees with hard `flag` anywhere in the peel: **25**
- Checked-node aggregate hist: `{'possible_issue': 1233, 'flag': 57, 'no_issue': 1}`
- Leaves still carrying `possible_issue`: **458**

## Stop-reason histogram
```
{
  "empty_expander": 818,
  "cycle": 1775,
  "hard_flag": 42,
  "confirmed_no_issue": 1
}
```
- `empty_expander` peels: 590 (trees touched: 220)
- Snapshot windows answer **excerpt** peels only; cite records need matching `target_id` (edge id / ref-N). Atom peels with no atom-kind map entry stop as empty_expander — expected when the map has snapshot+cite only.
- MISSING cite refs still expand (marker text); they do not invent expert/trust facts. Soft gap, not a verdict.

## METHOD records
- Count: **1295** (embedded in `trees.json` → `records`; also `method_records.jsonl`)
- Index: `METHOD_INDEX.md` (full markdown dump skipped as impractical at this size)

## Artifacts
- `trees.json` — full nested JSON (~23963 KB)
- `method_records.jsonl`
- `leads_nested.json` — break seeds with layer_path / entry_hit / peel_stop highlights
- `counts.json`
- `lead_ids.txt` / `lead_ir_paths.txt` / `lead_irs/` (symlinks to `irs/`)

## Example break passage_ids
- `circ-ashley-montagu-resolution-s0053`
- `circ-brit-milah-s0275`
- `circ-children-act-1989-amendment-female-genital-mutilation-act-2019-s0083`
- `circ-ashley-montagu-resolution-s0032`
- `circ-ashley-montagu-resolution-s0046`

## Survives
- `circ-forced-circumcision-s0041`

## Gaps / notes
- No IR or context-map gaps for the 450 seeds.
- 16 passage_ids have ≥1 MISSING-marked cite expand (see `counts.json`).
- Nest stress inherits L0 coverage: most seeds **break/open** because L0 `possible_issue` stays open when cite/atom peels cannot close the missing facts (expert/trust/etc.). Assist only.
