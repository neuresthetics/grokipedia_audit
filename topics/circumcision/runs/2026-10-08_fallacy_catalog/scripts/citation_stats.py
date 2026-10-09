#!/usr/bin/env python3
"""Plain citation-hygiene counts per article, from the saved snapshot only
(no source fetching). Writes ../citation_stats.csv.

Columns:
  sources_listed            rows in <date>_sources.csv
  markers_total             [n] markers in the body
  highest_marker            largest n used
  markers_beyond_list       markers whose n is larger than sources_listed
  distinct_numbers_beyond   distinct such n
  sources_never_cited       listed sources that no marker points to
  sentences / sentences_uncited / pct_sentences_uncited   prose sentences, and those with no [n]
  table_rows / table_rows_uncited
  paragraphs / paragraphs_uncited   prose paragraphs with no [n] anywhere in them
"""
import csv, pathlib
from split_units import slugs, units, n_sources, snapshot_paths, body_lines, MARK

OUT = pathlib.Path(__file__).resolve().parents[1] / "citation_stats.csv"
rows = []
for slug in slugs():
    ns = n_sources(slug)
    body = body_lines(snapshot_paths(slug)[0].read_text(encoding="utf-8"))
    marks = [int(m) for l in body for m in MARK.findall(l)]
    beyond = [m for m in marks if m > ns]
    pars = [l.strip() for l in body if l.strip() and not l.strip().startswith("#") and " | " not in l]
    sents = [t for k, t in units(slug) if k == "sentence"]
    trs = [t for k, t in units(slug) if k == "table_row"]
    su = sum(1 for s in sents if not MARK.search(s))
    rows.append(dict(
        slug=slug, sources_listed=ns, markers_total=len(marks),
        highest_marker=max(marks) if marks else 0,
        markers_beyond_list=len(beyond), distinct_numbers_beyond=len(set(beyond)),
        sources_never_cited=len(set(range(1, ns + 1)) - set(marks)),
        sentences=len(sents), sentences_uncited=su,
        pct_sentences_uncited=round(100 * su / len(sents), 1) if sents else 0,
        table_rows=len(trs), table_rows_uncited=sum(1 for t in trs if not MARK.search(t)),
        paragraphs=len(pars), paragraphs_uncited=sum(1 for p in pars if not MARK.search(p)),
    ))
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(f"wrote {OUT} ({len(rows)} articles)")
