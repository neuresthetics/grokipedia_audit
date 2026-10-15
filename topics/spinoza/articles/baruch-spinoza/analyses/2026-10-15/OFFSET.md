# OFFSET: citation numbers vs the source list (snapshot 2026-10-15)

The 2026-10-01 audit found that from inline [90] onward the citation numbers looked shifted by nine places. This run checks that again on the new snapshot.

## What changed since 2026-10-01

- C003 gained a new inline cite [5] (Merriam-Webster, "Spinozism"). In the source list, though, that entry was added at the end as #153, not at position 5.
- So every older inline number from [5] up went up by one (314 unchanged sentences were renumbered by +1, see DIFF.md). The list entries did not move.

## Result

| Inline numbers | Read as list entry | Why |
|---|---|---|
| [1]–[4] | n | unchanged |
| [5] | #153 | the new Merriam-Webster entry, added at the end of the list |
| [6]–[90] | n − 1 | the +1 renumbering of inline cites only |
| [91]–[162] | n − 10 | the old −9 shift plus the new −1 |
| [154]–[162] | (dangle) | 9 markers whose number is higher than the list's 153 entries (in C393, C395–C397, C399–C401) |

As linked, nearly every inline marker from [6] up points to the wrong list entry. Under these rules, [154]–[162] map to list #144–#152.

## Evidence

`scripts/offset_fulltext.py` → `data/offset_fulltext.csv`. For each inline marker, it measures the share of the sentence's content words (4+ letters, minus a short stopword list) that appear in the fetched text of list entry n, n−1 and n−10. A marker "wins" for the k with the strictly highest share. Only sources with more than 1,500 bytes of fetched text are used (128 of 153).

| Inline range | Markers scored | won by n | won by n−1 | won by n−10 | tie |
|---|---:|---:|---:|---:|---:|
| 6–90 | 184 | 37 | 91 | 30 | 26 |
| 91–162 | 71 | 8 | 13 | 47 | 3 |

The clearest blocks are 41–50 (n−1 wins 26 of 31) and 91–100 (n−10 wins 27 of 30; mean share 0.15 at n, 0.73 at n−10). In other blocks the signal is weaker, because many sources are broad surveys that share general vocabulary. Treat this probe as coarse. The per-sentence checks in `data/claim_log.csv` (column `intended_sources`) used the mapping above and read the passages by hand.

Chart: `docs/img/spinoza/2026-10-15/offset_probe_by_block.png`. It plots the mean share per block of 10 inline numbers for n, n−1 and n−10.

`data/offset_probe.csv` is the older title-based probe from `grokaudit.py parse`. It compares sentence words with source titles only, so its signal is weaker. It is kept for continuity.
