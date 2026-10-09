# Reviewer 3 working files

Reviewer 3 was a third general-purpose AI agent. It was told not to open `flags.csv`, `reviewer2_flags.csv`, the comparison files, ANALYSIS.md, the charts or any earlier run until `reviewer3_flags.csv` was saved, and it reports that it did not. It was not blind: its instructions came from a conversation that had already discussed counts and example quotes from Reviewers 1 and 2.

- `show.sh <slug>` prints a snapshot without its header; `chunk.py <slug> [n]` prints chunk n (about 18,500 characters, split at paragraph breaks) for longer articles. Citation markers were left in the text.
- `add.py` takes one article's flags as JSON on stdin. It rejects unknown entry ids and any quote that is not an exact substring of the snapshot, appends the rest to `flags.jsonl`, and records the slug in `done.txt`.
- `build_reviewer3.py` re-checks every quote and rebuilds `../../reviewer3_flags.csv` from `flags.jsonl` (byte-identical to the committed file). Given a fallacy_catalog checkout, it also checks that no entry marked `text_detectable: no` was used.
- Result: 121 rows from 58 articles, 0 quote failures, 0 rows dropped.

`show.sh`, `chunk.py` and `add.py` were run from a scratch folder and use absolute `/workspace/...` paths; they are kept as a record, not as portable tools.

Reading rules: METHOD.md at fallacy_catalog commit `2a56493`. Attributed views were not flagged; entries with `text_detectable: no` were not used; factual slips alone were not flagged; an inconsistency was flagged only when the article relies on both sides of it.
