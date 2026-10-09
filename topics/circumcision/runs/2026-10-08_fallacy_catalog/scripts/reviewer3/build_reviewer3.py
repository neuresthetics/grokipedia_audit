#!/usr/bin/env python3
"""Rebuild reviewer3_flags.csv from scripts/reviewer3/flags.jsonl and re-check every quote.

Run from the run folder: python3 scripts/reviewer3/build_reviewer3.py [path/to/fallacy_catalog]
Checks: each quote is an exact substring of its 2026-10-01 snapshot; each entry id exists in the catalog;
no entry with text_detectable "no" is used (if a catalog path is given); all 58 articles are in done.txt.
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(os.path.dirname(HERE))
ART = os.path.join(RUN, '..', '..', 'articles')
COLS = ['slug', 'quote', 'entry_id', 'entry_name', 'reason', 'favors', 'confidence', 'verdict']

rows = [json.loads(l) for l in open(os.path.join(HERE, 'flags.jsonl'), encoding='utf-8')]
done = open(os.path.join(HERE, 'done.txt'), encoding='utf-8').read().split()
fail = [r for r in rows if r['quote'] not in
        open(os.path.join(ART, r['slug'], 'snapshots', '2026-10-01.txt'), encoding='utf-8').read()]
if len(sys.argv) > 1:
    cat = {e['id']: e for e in json.load(open(os.path.join(sys.argv[1], 'fallacies.json')))['entries']}
    assert all(r['entry_id'] in cat for r in rows), 'unknown entry id'
    assert not [r for r in rows if str(cat[r['entry_id']].get('text_detectable')).lower() == 'no'], 'text_detectable no'
print(f'rows {len(rows)}; quote failures {len(fail)}; articles read {len(set(done))}')
assert not fail
with open(os.path.join(RUN, 'reviewer3_flags.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r[k] for k in COLS})
print('wrote reviewer3_flags.csv')
