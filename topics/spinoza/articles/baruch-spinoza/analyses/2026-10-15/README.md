# Baruch Spinoza: audit run 2026-10-15

![Headline chart: same 401 sentences, citations as linked vs with the footnote shift undone](../../../../../../docs/img/spinoza/2026-10-15/headline_content_vs_citations.png)

*Headline chart.* Two bars for the same 401 sentences. Top: each sentence judged against the source its footnote actually links. Bottom: the same check with the footnote shift undone (each cite read as the source it seems meant to point to). The words "Mostly accurate content" in the chart title are the assistant's reading of the bottom bar, not a measured label.

This run checks the Grokipedia article against a fresh snapshot (2026-10-15). Each of the 401 sentences gets one row, with its sources fetched and Ethics claims checked against a pinned Elwes text. Flags here are leads for a human to check, not final verdicts. How it was done: [METHOD.md](METHOD.md).

## Summary

| Verdict | as linked | vs. intended source |
|---|---:|---:|
| supported | 30 | 135 |
| partly supported | 81 | 127 |
| unsupported | 73 | 37 |
| miscited | 94 | — |
| unverifiable | 47 | 26 |
| uncited | 76 | 76 |

- "Vs. intended" reads each cite with the numbering drift corrected ([OFFSET.md](OFFSET.md)).
- "As linked" judges each sentence only against the source its marker actually links. These counts were corrected after a second check ([RECHECK.md](RECHECK.md)) and again after a third check ([RECHECK3.md](RECHECK3.md)); every changed row is listed in [CORRECTIONS.md](CORRECTIONS.md).
- Ethics claims against the pinned Elwes text: 82 match in content, 8 do not match, and 47 concern other works with no primary text on hand.
- **Offset:** the [90]+ shift found on 2026-10-01 is still there, now −10 for inline [91]+. The new inline [5] was added to the list as #153, so inline [6]–[90] now read as n−1. Inline [154]–[162] (9 markers) point past the end of the 153-entry list.
- **Diff:** 400 of 401 sentences are unchanged. C003 adds "known as Spinozism (also Spinozaism)" with the new cite. See [DIFF.md](DIFF.md).
- **Fallacy pass:** 9 passages; both reads flagged the same passage in 8 of them. The two reads were by the same checker, so they are not independent. See [FALLACY.md](FALLACY.md).

## Files

| Path | What |
|---|---|
| `data/claim_log.csv` | per-sentence log (main output) |
| `data/verdicts.psv` | hand-written verdicts and reasons (input to the log) |
| `data/claims.csv`, `sources.csv`, `structure.json` | parse of the snapshot |
| `data/evidence.jsonl` | retrieved source windows (aid only) |
| `data/fetch_log.csv`, `linkcheck.csv`, `source_cache_manifest.csv` | fetch record and hashes of cached texts |
| `data/ethics_index.csv` | Elwes Ethics locator → line index |
| `data/offset_fulltext.csv`, `offset_probe.csv` | offset probes |
| `data/fallacy_flags_R1.csv`, `_R2.csv`, `fallacy_compare.csv`, `fallacy_candidates_R2.csv` | fallacy pass |
| `data/spinoza_refs.csv` | `grokaudit refs` output |
| `scripts/` | everything used to build the above |
| `RECHECK.md`, `recheck_log.csv` | second-session recheck |
| `RECHECK3.md`, `recheck3_log.csv` | third-session recheck |
| `CORRECTIONS.md` | every change made after the second and third checks |
| `../../snapshots/2026-10-15.{html,md}` | the snapshot |
| `docs/img/spinoza/2026-10-15/` (repo root) | charts |

## Pinned inputs

- Snapshot html sha256 `2dd665ddb6dfb9314b7c0243d46203a65e9e1e290df2bd882db1eb9dadbe9220`; md sha256 `f73caa1d9bad28e5216c6abb9ef4193a245803d0b92e20e140969aeba3c04bb2`.
- grokAlign `90340d11aa6669b2467e219fda4fff01d9c8a1ce`: `The Ethic.txt` sha256 `43845011…68621`; `cleaned_The Ethic.txt` sha256 `52e36c09…4c079c` (full hashes in METHOD.md).
- fallacy_catalog v0.6.1 `2a56493a3931018e9143bc7235f152f5cc5b459e`.

## Charts

- `docs/img/spinoza/2026-10-15/verdicts_linked_vs_intended.png`: verdict counts per sentence, as linked vs. with the numbering corrected.
- `docs/img/spinoza/2026-10-15/offset_probe_by_block.png`: for each block of 10 inline numbers, the average share of the sentence's words found in list entry n, n−1 and n−10.
- `docs/img/spinoza/2026-10-15/primary_text_check.png`: how many sentences match, do not match, or have no primary text on hand.

## Limits

One Grok Bot session made every judgment. A second, separate Grok Bot session rechecked an 84-row stratified sample (55% same verdict); it did not see the original verdicts while judging but had seen the summary, so the recheck was not blind and was not an independent person ([RECHECK.md](RECHECK.md)). A third Grok Bot session rechecked 196 rows, also not blind ([RECHECK3.md](RECHECK3.md)); see Repeat rates. Third-party source texts are not committed; only their hashes are. The Elwes translation differs from the Curley wording the article mostly quotes. Details are in METHOD.md.

## Repeat rates

- The verdicts were checked three times by Grok Bot sessions of the same model kind. These were not independent people, and the checks were not blind.
- Second check: an 84-row stratified sample; 55% of rows gave the same verdict.
- Third check: 196 rows; 58% gave the same verdict as linked (about 68% when unsupported and miscited are merged), and 68% gave the same verdict with citations corrected.
- The footnote offset, the named errors and the 8 Ethics mismatches were confirmed in every check.
- The fine-grained verdict counts above should be read as approximate.
