# Circumcision scan runs

Each folder is one sophistry-scan run over the circumcision articles, named `YYYY-MM-DD_runN_<scope>`. How the three runs fit together and what the comparison does and doesn't show: [METHOD_THREE_PHASE_TEST.md](../../../docs/METHOD_THREE_PHASE_TEST.md).

| Run | Folder | Articles | What was read | Flags (pro / anti / neutral) | Main files |
|---|---|---|---|---|---|
| 1 | [2026-10-01_run1_partial](2026-10-01_run1_partial/README.md) | 58 | About 30% of sentences (triage) | 239 (126 / 56 / 57) | Summary table; per-article flags in `articles/<slug>/analyses/2026-10-01/sophistry_scan_run1_partial.md` |
| 2 | [2026-10-01_run2_full](2026-10-01_run2_full/README.md) | 58 | All 10,258 units | 225 (154 / 49 / 22) | `flags.csv`, `coverage.tsv`, comparison with run 1; per-article flags in `articles/<slug>/analyses/2026-10-01/sophistry_scan.md` |
| 3 | [2026-10-02_run3_title24](2026-10-02_run3_title24/README.md) | 24 (title matches) | All units, blind to runs 1 and 2 | 111 (86 / 18 / 7) | `flags.csv`, `coverage.tsv`, comparison with run 2, scripts |

Run 1 read only part of each article, so its totals are not comparable with the full reads.

Added 2026-10-15 (plain method, not substance_lens):

| Run | Folder | Articles | What was read | Main files |
|---|---|---|---|---|
| fallacy_catalog benchmark | [2026-10-08_fallacy_catalog](2026-10-08_fallacy_catalog/README.md) | 58 (2026-10-01 snapshots) | All 13,199 sentences labeled; three AI reviewers flagged against fallacy_catalog v0.6.1 | [WALKTHROUGH.md](2026-10-08_fallacy_catalog/WALKTHROUGH.md), `flags.csv`, [FULL_RECORD.md](2026-10-08_fallacy_catalog/FULL_RECORD.md) |
