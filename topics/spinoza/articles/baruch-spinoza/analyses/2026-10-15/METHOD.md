# METHOD: how this run was made (2026-10-15)

These are the steps as they were actually done. One Grok Bot session made judgments; a second separate Grok Bot session rechecked an 84-row stratified sample (55% same verdict) without seeing original verdicts but having seen the summary, so not blind and not an independent person. No person checked any row. Scripts are in `scripts/` and use only the Python standard library, except `charts.py`, which uses matplotlib. Paths are relative to this folder unless noted.

## 1. Snapshot
- `curl` of https://grokipedia.com/page/Baruch_Spinoza returned HTTP 200 and 631,317 bytes, saved as `../../snapshots/2026-10-15.html` (sha256 `2dd665ddb6dfb9314b7c0243d46203a65e9e1e290df2bd882db1eb9dadbe9220`).
- `tools/grokaudit/grokaudit.py parse` produced `data/claims.csv`, `data/sources.csv`, `data/structure.json` and `data/offset_probe.csv`. The article splits into 401 sentences (325 cited, 76 uncited), 390 inline markers and 153 list sources.
- `scripts/make_md.py` built `../../snapshots/2026-10-15.md` (sha256 `f73caa1d9bad28e5216c6abb9ef4193a245803d0b92e20e140969aeba3c04bb2`). The text is copied from claims.csv, with the markers re-added.

## 2. Diff
`scripts/diff_snapshots.py` (difflib over the sentence lists) compared this snapshot with 2026-10-01 → `DIFF.md`.

## 3. Primary text (Ethics)
- Both copies come from neuresthetics/grokAlign, commit `90340d11aa6669b2467e219fda4fff01d9c8a1ce`, folder `junkDrawer/Ethics/`:
  - `The Ethic.txt`: Elwes translation, Gutenberg #3800 text. sha256 `43845011b8f98b585e9a7ba74673cec243cb85dedb70f8ca1421e4cc39568621`, 5,996 lines.
  - `cleaned_The Ethic.txt`: sha256 `52e36c09e3fc13ac2805eac9255997e9fd03c510d87ae384ec71e5ec864c079c`, 6,527 lines. It has the same translation, reflowed. All line numbers in this run refer to `The Ethic.txt`.
- `scripts/ethics_index.py` → `data/ethics_index.csv` (828 locators, such as E1P15, E2P40S2 and E3DefAff48, each with start and end lines). Propositions per part: 36/49/59/73/42. Known index faults: E2D7 is missing; the lemma axioms in Part II create a duplicate E2A1/A2; there is one stray "E1A" row; the span of the last entry (E5P42S1) runs into the Gutenberg licence. None of these affect a cited locator.
- Both copies are the Elwes (1883) translation. The article often quotes the Curley translation, so a different wording counts as a match when the content is the same. Exact Elwes wording is noted where it occurs.

## 4. Sources and claim log
- Fetch: `grokaudit.py fetch` first. Sources that failed went to `scripts/refetch.py`, which tries live curl with browser headers, then the Wayback latest capture via `https://web.archive.org/web/2026id_/<url>` (the availability API timed out, so it was not used). `data/fetch_log.csv` has one row per refetch. `data/source_cache_manifest.csv` gives the bytes and sha256 of every cached text. The cache itself (`/workspace/spcache_1015/` on the work box) is not committed, because it holds third-party text.
- Readable text was found for 128 of 153 sources (more than 1,500 bytes). No readable text was found for refs 4, 6, 20, 23, 30, 34, 36, 38, 40, 41, 42, 80, 84, 85, 87, 93, 104, 107, 112, 114, 127, 139, 143 and 147; ref 53 is a soft page. Refs 83 and 95 were flagged by `grokaudit soft404`, but both are full pages: the trigger words occur in the body text.
- `scripts/evidence.py` → `data/evidence.jsonl`. For each sentence and marker, it finds the best 50-word window in the source as linked and in the drift-corrected source (see OFFSET.md). This is a retrieval aid only.
- Verdicts: the checker read each sentence, the retrieved windows and, where needed, the wider source text, then wrote one row per sentence in `data/verdicts.psv`. Columns: id | verdict as linked | verdict vs intended | Ethics locator | primary-text code | reason. Codes: S supported, P partly supported, U unsupported, M miscited (the linked source is about something else; the right source exists elsewhere in the list), X unverifiable (source not reachable or not listed), N uncited.
  - An Ethics locator may carry `@phrase`. The builder then fails unless that exact phrase is in the entry, and shows the lines around it.
  - Findings reused from the 2026-10-01 audit are marked as such in the reason.
- `scripts/check_quotes.py`: every double-quoted string (6+ characters) in a reason must occur verbatim in the source it is attributed to: a `[n]` right after the quote, otherwise the nearest preceding `[n]`, "Elwes"/Ethics locator, or "article" in the same reason. Quoting the row's own article sentence also passes. The first version only checked that a quote existed somewhere in the cache; the recheck found 7 quotes not in the named source, and the stricter version found 2 more. All were fixed (CORRECTIONS.md). The final run: 238 quotes, 0 not found in the attributed source.
- `scripts/consistency.py`: lists every S/P as-linked row whose as-linked reasoning names none of the sources the sentence links. After corrections it reports 0. Re-judged rows carry reasons in the form `As linked: ... // Intended: ...`.
- `scripts/build_claim_log.py` → `data/claim_log.csv`, one row per sentence. Source and Elwes excerpts are copied by the script, not typed.

## 5. Offset
`scripts/offset_fulltext.py` → `data/offset_fulltext.csv` and `OFFSET.md`.

## 6. Fallacy pass
See FALLACY.md. The catalog is fallacy_catalog v0.6.1, commit `2a56493a3931018e9143bc7235f152f5cc5b459e`. There were two reads by the same checker, so they are **not independent**. `scripts/fallacy_candidates.py` and `scripts/fallacy_compare.py` were used.

## 7. Charts
`scripts/charts.py data ../../../../../../docs/img/spinoza/2026-10-15`.

## Limits
- One Grok Bot session made judgments; a second separate Grok Bot session rechecked an 84-row stratified sample (55% same verdict) without seeing original verdicts but having seen the summary, so not blind and not an independent person. A third Grok Bot session rechecked 196 rows (RECHECK3.md); its 20 recommended changes and one reason fix were applied (CORRECTIONS.md, Round 2).
- "As linked" verdicts can credit a wrong-numbered source that happens to cover the same topic. The first pass did this in 37 rows (and the consistency pass found 20 more); those rows were re-judged against the linked source only (CORRECTIONS.md). After that and the third-check changes, 94 rows are M. Rows on the same topic as the wrong-numbered source are U or P rather than M.
- Paywalled sources were judged from abstracts or Wayback captures where that was all that was available. Such rows are mostly P or X.
- Material outside the Ethics (TTP, TP, letters, Short Treatise) was not checked against a primary text (code "no primary text on hand").
- Retrieval scores are word overlap. They point to passages and do not decide verdicts.

## Repeat rates

- The verdicts were checked three times by Grok Bot sessions of the same model kind. These were not independent people, and the checks were not blind.
- Second check: an 84-row stratified sample; 55% of rows gave the same verdict.
- Third check: 196 rows; 58% gave the same verdict as linked (about 68% when unsupported and miscited are merged), and 68% gave the same verdict with citations corrected.
- The footnote offset, the named errors and the 8 Ethics mismatches were confirmed in every check.
- The fine-grained verdict counts in README.md should be read as approximate.
