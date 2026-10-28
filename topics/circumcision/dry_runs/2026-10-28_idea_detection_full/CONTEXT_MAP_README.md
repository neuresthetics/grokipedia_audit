# Context map — circ idea_detection nested (2026-10-28)

Built for the 452 `possible_issue` rows in `out/leads.json` (**450 unique** `passage_id`s; 2 duplicate lead ids collapsed: `['circ-circumcision-and-hiv-s0170', 'circ-circumcision-in-africa-s0005']`).

Use with fallacy_catalog nested CLI (tip **f304b80**):

```bash
cd /workspace/fallacy_catalog
python3 -m idea_detection.nested --context-map \
  /workspace/gta_repo/topics/circumcision/dry_runs/2026-10-28_idea_detection_full/contexts.jsonl \
  --method-record \
  /workspace/gta_repo/topics/circumcision/dry_runs/2026-10-28_idea_detection_full/irs/
```

(Optionally filter `irs/` to the 450 lead ids first.)

## How built

1. Parse each lead `id` → article slug + sentence id (`circ-{slug}-sNNNN`).
2. Load passage text from `passages.jsonl`.
3. Load `articles/{slug}/snapshots/2026-10-01.txt`; locate the passage (exact match for all in this build); take a ±3-sentence window clamped to ~800–1500 chars, snapped to sentence/paragraph boundaries.
4. Emit `kind=snapshot_window` with `"full": true` when surrounding article text was found (lifts excerpt cap on the peel).
5. Extract `[n]` markers; look up `ref_number` in `2026-10-01_sources.csv` (`title` / `url` / `raw_text`).
6. Emit `kind=cite` records: if the IR has `appeals_to_source` edges, set `target_id` to the edge id (`e1`, …); otherwise `target_id=ref-{n}`. Missing CSV refs still get a cite record noting `MISSING`.

No invented expert/trust facts — expand text is snapshot body and CSV fields only. Local only; not committed.

## Counts

| Metric | Value |
|---|---|
| Lead rows in `possible_issues` | 452 |
| Unique passage_ids | 450 |
| Passage_ids with ≥1 context record | 450 |
| Uncovered | 0 |
| Total context records | 1032 |
| `snapshot_window` | 450 |
| `cite` | 582 |
| Records with `full: true` | 450 |
| Exact snapshot matches | 450 |
| Fuzzy snapshot matches | 0 |
| Passage not found in snapshot | 0 |
| Missing snapshot files | 0 |
| Cite refs found in CSV | 391 |
| Cite refs missing from CSV | 20 |
| Cite with IR edge, no `[n]` marker | 176 |
| Cite without IR edge (`ref-N` target) | 13 |
| Window length min / median / max | 972 / 1500 / 1500 |
| Windows starting mid-word | 0 |

## Notes

- All 47 lead articles had both `2026-10-01.txt` and `2026-10-01_sources.csv`.
- Uncovered ids: (none).
- Sample missing cite refs (up to 12): `[('circ-female-genital-mutilation-s0145', '23'), ('circ-female-genital-mutilation-s0196', '35'), ('circ-female-genital-mutilation-s0221', '44'), ('circ-female-genital-mutilation-s0323', '35'), ('circ-views-on-circumcision-s0003', '3'), ('circ-views-on-circumcision-s0003', '4'), ('circ-views-on-circumcision-s0069', '49'), ('circ-views-on-circumcision-s0070', '50'), ('circ-views-on-circumcision-s0074', '51'), ('circ-views-on-circumcision-s0078', '52'), ('circ-views-on-circumcision-s0083', '53'), ('circ-views-on-circumcision-s0090', '56')]`.
- Duplicate lead ids (same passage, possibly different `entry`): `['circ-circumcision-and-hiv-s0170', 'circ-circumcision-in-africa-s0005']` — one context set each.
