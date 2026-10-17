# Consciousness

This topic covers how Grokipedia handles consciousness: the main scientific theories, the hard problem, and the people behind them. It has 18 pages and about 4,100 sentences. Integrated information theory (IIT) goes through the same checks as every other page and gets no special treatment.

## Status

- **Snapshots saved 2026-10-17.** Each page is stored as it was fetched (`.html`) and as readable text (`.md`). The text gives every sentence an id and keeps its inline `[n]` footnote markers, followed by the numbered source list. See [ARTICLE_LIST.md](ARTICLE_LIST.md).
- **No checks have been run yet.** Two are planned, and each gets its own separate recheck:
  1. **Source check:** does the source a sentence's footnote links actually say what the sentence says?
  2. **Reasoning check:** reviewers flag passages against `fallacy_catalog`.
- Flags from either check are leads to look into, not verdicts.

## Files

- `articles/<slug>/snapshots/2026-10-17.html` and `.md`: one pair per page
- `snapshot_log.json`: fetch time, HTTP status, sha256 hashes and counts for each page
- `scripts/snapshot.py`: the script that fetched and parsed the pages. It uses the same parser as the Spinoza run (`tools/grokaudit`).
