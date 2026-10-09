#!/usr/bin/env python3
"""Compare the three reviewers (separate AI reader runs, not blind): reviewer 1 (flags.csv), reviewer 2
(reviewer2_flags.csv) and reviewer 3 (reviewer3_flags.csv).

Pairwise: two flags match when they are on the same article and their quotes
overlap in the saved snapshot (character spans intersect). Matching is
one-to-one, greedy by overlap length. Done for each pair (1-2, 1-3, 2-3).

Three-way: every row of every reviewer is a span in its article. Spans that
overlap are joined into one passage (connected groups, so A-B and B-C put
A, B and C in one passage). For each passage we record which reviewers
flagged it and with which side. "Flagged by all three, same side" = all
three reviewers have a row in the passage with the same side. "Flagged by at
least two, same side" = at least two reviewers do.

Writes, next to the CSVs:
  agreement.csv           reviewer 1 vs 2 matched pairs (kept from the
                          two-reviewer run; the name is historical, it just
                          lists overlap)
  overlap_r1_r3.csv, overlap_r2_r3.csv   the other two pairs, same columns
  overlap_pairwise.csv    one row per pair: matched counts, same side, same
                          fallacy name
  overlap_3way.csv        one row per passage flagged by any reviewer
  per_article_counts.csv  per-article counts for all three reviewers
  agreement_summary.md    plain summary of all of the above
"""
import csv, os, re, collections

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = os.path.normpath(os.path.join(RUN, '..', '..', 'articles'))
SNAP = '2026-10-01.txt'

def load(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader(f))

_txt = {}
def text(slug):
    if slug not in _txt:
        with open(os.path.join(ARTICLES, slug, 'snapshots', SNAP), encoding='utf-8') as f:
            _txt[slug] = f.read()
    return _txt[slug]

def span(slug, q):
    t = text(slug)
    i = t.find(q)
    if i >= 0:
        return (i, i + len(q))
    toks = re.findall(r'\w+|[^\w\s]', q)
    pat = r'(?:\s*\[\d+\])*\s*'.join(re.escape(x) for x in toks)
    m = re.search(pat, t)
    return (m.start(), m.end()) if m else None

def ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r

def pearson(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    c = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = sum((x - ma) ** 2 for x in a) ** .5; vb = sum((y - mb) ** 2 for y in b) ** .5
    return c / (va * vb) if va and vb else float('nan')

def lean(rows):
    p = sum(r['favors'] == 'pro' for r in rows); a = sum(r['favors'] == 'anti' for r in rows)
    return 'pro' if p > a else 'anti' if a > p else ('none' if not rows else 'even')

RELATED = {frozenset(p) for p in [('bulverism', 'appeal-to-motive'), ('false-cause', 'cum-hoc'),
                                  ('secundum-quid', 'over-extrapolation'),
                                  ('argument-from-silence', 'argument-from-ignorance')]}
SIDES = ('pro', 'anti', 'neutral')


def overlap(a, b):
    if a['slug'] != b['slug'] or not a['_span'] or not b['_span']:
        return 0
    return min(a['_span'][1], b['_span'][1]) - max(a['_span'][0], b['_span'][0])


def match(ra, rb):
    """One-to-one greedy matching by overlap length. Returns [(i, j, overlap_chars)] sorted by article and position."""
    cands = []
    for i, a in enumerate(ra):
        for j, b in enumerate(rb):
            ov = overlap(a, b)
            if ov > 0:
                cands.append((ov, i, j))
    cands.sort(reverse=True)
    ua, ub, pairs = set(), set(), []
    for ov, i, j in cands:
        if i in ua or j in ub:
            continue
        ua.add(i); ub.add(j); pairs.append((i, j, ov))
    pairs.sort(key=lambda p: (ra[p[0]]['slug'], ra[p[0]]['_span'][0]))
    return pairs


def write_pairs(path, ta, tb, ra, rb, pairs):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['slug', f'{ta}_quote', f'{tb}_quote', f'{ta}_entry_id', f'{tb}_entry_id', 'same_entry',
                    f'{ta}_favors', f'{tb}_favors', 'same_side', f'{ta}_verdict', f'{tb}_verdict', 'overlap_chars'])
        for i, j, ov in pairs:
            a, b = ra[i], rb[j]
            w.writerow([a['slug'], a['quote'], b['quote'], a['entry_id'], b['entry_id'],
                        a['entry_id'] == b['entry_id'], a['favors'], b['favors'],
                        a['favors'] == b['favors'], a['verdict'], b['verdict'], ov])


def passages(revs):
    """Join overlapping spans from all reviewers into passages (connected groups)."""
    nodes = [(k, i) for k, rows in enumerate(revs) for i, r in enumerate(rows) if r['_span']]
    parent = {n: n for n in nodes}

    def find(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n
    for x in range(len(nodes)):
        for y in range(x + 1, len(nodes)):
            a = revs[nodes[x][0]][nodes[x][1]]; b = revs[nodes[y][0]][nodes[y][1]]
            if overlap(a, b) > 0:
                parent[find(nodes[x])] = find(nodes[y])
    groups = collections.defaultdict(list)
    for n in nodes:
        groups[find(n)].append(n)
    out = []
    for g in groups.values():
        rows = [(k, revs[k][i]) for k, i in g]
        slug = rows[0][1]['slug']
        start = min(r['_span'][0] for _, r in rows); end = max(r['_span'][1] for _, r in rows)
        out.append(dict(slug=slug, start=start, end=end, rows=rows))
    out.sort(key=lambda p: (p['slug'], p['start']))
    return out


def main():
    r1 = load(os.path.join(RUN, 'flags.csv'))
    r2 = load(os.path.join(RUN, 'reviewer2_flags.csv'))
    r3 = load(os.path.join(RUN, 'reviewer3_flags.csv'))
    revs = [r1, r2, r3]
    tags = ['r1', 'r2', 'r3']
    slugs = sorted(d for d in os.listdir(ARTICLES) if os.path.isdir(os.path.join(ARTICLES, d)))
    unspanned = []
    for tag, rows in zip(('R1', 'R2', 'R3'), revs):
        for r in rows:
            r['_span'] = span(r['slug'], r['quote'])
            if r['_span'] is None:
                unspanned.append((tag, r['slug'], r['quote'][:60]))

    # ---------------------------------------------------------------- pairwise
    PAIRS = [(0, 1, 'agreement.csv'), (0, 2, 'overlap_r1_r3.csv'), (1, 2, 'overlap_r2_r3.csv')]
    pw = {}
    for a, b, fname in PAIRS:
        pairs = match(revs[a], revs[b])
        write_pairs(os.path.join(RUN, fname), tags[a], tags[b], revs[a], revs[b], pairs)
        ra, rb = revs[a], revs[b]
        n = len(pairs)
        same_s = sum(ra[i]['favors'] == rb[j]['favors'] for i, j, _ in pairs)
        same_e = sum(ra[i]['entry_id'] == rb[j]['entry_id'] for i, j, _ in pairs)
        near = sum(ra[i]['entry_id'] != rb[j]['entry_id'] and
                   frozenset((ra[i]['entry_id'], rb[j]['entry_id'])) in RELATED for i, j, _ in pairs)
        both_side = collections.Counter(ra[i]['favors'] for i, j, _ in pairs if ra[i]['favors'] == rb[j]['favors'])
        pw[a, b] = dict(file=fname, pairs=pairs, n=n, same_s=same_s, same_e=same_e, near=near, both_side=both_side,
                        na=len(ra), nb=len(rb))
    with open(os.path.join(RUN, 'overlap_pairwise.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['pair', 'file', 'flags_a', 'flags_b', 'matched', 'a_only', 'b_only', 'share_of_a_matched',
                    'share_of_b_matched', 'same_side', 'same_side_rate', 'same_entry', 'same_entry_rate',
                    'near_twin_entry', 'same_side_pro', 'same_side_anti', 'same_side_neutral'])
        for (a, b), d in pw.items():
            n = d['n']
            w.writerow([f'{a + 1}-{b + 1}', d['file'], d['na'], d['nb'], n, d['na'] - n, d['nb'] - n,
                        f"{n / d['na']:.3f}", f"{n / d['nb']:.3f}", d['same_s'], f"{d['same_s'] / n:.3f}" if n else '',
                        d['same_e'], f"{d['same_e'] / n:.3f}" if n else '', d['near'],
                        d['both_side']['pro'], d['both_side']['anti'], d['both_side']['neutral']])

    # ---------------------------------------------------------------- three-way passages
    ps = passages(revs)
    with open(os.path.join(RUN, 'overlap_3way.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['passage', 'slug', 'start', 'end', 'reviewers', 'n_reviewers', 'r1_favors', 'r2_favors', 'r3_favors',
                    'r1_entry_ids', 'r2_entry_ids', 'r3_entry_ids', 'side', 'n_reviewers_same_side',
                    'same_side_reviewers', 'all_three_same_side', 'at_least_two_same_side', 'shared_entry_ids',
                    'r1_quote', 'r2_quote', 'r3_quote'])
        for pid, p in enumerate(ps, 1):
            byk = {k: [r for kk, r in p['rows'] if kk == k] for k in range(3)}
            who = [k for k in range(3) if byk[k]]
            sides = {s: [k for k in range(3) if any(r['favors'] == s for r in byk[k])] for s in SIDES}
            # side flagged by the most reviewers; ties broken pro > anti > neutral (none occur in this run)
            best = max(SIDES, key=lambda s: (len(sides[s]), -SIDES.index(s)))
            nbest = len(sides[best])
            ties = [s for s in SIDES if len(sides[s]) == nbest and s != best]
            same_rev = sides[best]
            ents = collections.Counter(e for k in same_rev for e in {r['entry_id'] for r in byk[k] if r['favors'] == best})
            shared = sorted(e for e, c in ents.items() if c >= 2)
            p.update(byk=byk, who=who, side=best, nsame=nbest, same_rev=same_rev, ties=ties, shared=shared)
            w.writerow([pid, p['slug'], p['start'], p['end'], ','.join(str(k + 1) for k in who), len(who),
                        *['|'.join(r['favors'] for r in byk[k]) for k in range(3)],
                        *['|'.join(r['entry_id'] for r in byk[k]) for k in range(3)],
                        best if nbest >= 2 else '', nbest, ','.join(str(k + 1) for k in same_rev) if nbest >= 2 else '',
                        nbest == 3, nbest >= 2, '|'.join(shared),
                        *[(byk[k][0]['quote'] if byk[k] else '') for k in range(3)]])
    multi_side = [p for p in ps if p['nsame'] >= 2 and p['ties']]

    # ---------------------------------------------------------------- per article
    by = [collections.defaultdict(list) for _ in range(3)]
    for k in range(3):
        for r in revs[k]:
            by[k][r['slug']].append(r)
    cnt = [[len(by[k][s]) for s in slugs] for k in range(3)]
    rho = {(a, b): pearson(ranks(cnt[a]), ranks(cnt[b])) for a, b, _ in PAIRS}
    with open(os.path.join(RUN, 'per_article_counts.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['slug', 'r1_flags', 'r2_flags', 'r3_flags', 'r1_lean', 'r2_lean', 'r3_lean'])
        for s in slugs:
            w.writerow([s, len(by[0][s]), len(by[1][s]), len(by[2][s]), lean(by[0][s]), lean(by[1][s]), lean(by[2][s])])

    # ---------------------------------------------------------------- summary
    def ctr(rows, k): return collections.Counter(r[k] for r in rows)
    L = ['# Reviewer comparison (three separate AI reader runs, not blind)\n']
    L.append('Wording: "flagged by both / all three / at least two" means that many reviewers, in separate runs, '
             'flagged overlapping text in the same article. It is overlap, not proof that a flag is right.\n')
    L.append('The runs were not blind: Reviewers 2 and 3 were told not to open the other reviewers\' files until '
             'their own were saved, but their instructions came from a conversation that had already discussed '
             'earlier results. Overlap may be partly inflated by that; Reviewer 1 is the only fully uninfluenced read.\n')
    L.append(f'- Articles: {len(slugs)}')
    for k in range(3):
        rows = revs[k]
        L.append(f'- R{k + 1}: {len(rows)} flags; by side {dict(ctr(rows, "favors"))}; by verdict '
                 f'{dict(ctr(rows, "verdict"))}; articles with a flag {sum(1 for x in cnt[k] if x)}')
    L.append(f'- Quotes not locatable in snapshot (excluded from matching): {len(unspanned)} {unspanned}')
    L.append('\n## Pairwise overlap (one-to-one matching)\n')
    L.append('| Pair | Flags | Matched | Only first | Only second | Share of first matched | Share of second matched '
             '| Same side | Same fallacy name | Near-twin name | Same side: pro / anti / neutral |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for (a, b), d in pw.items():
        n = d['n']
        L.append(f"| R{a + 1}-R{b + 1} | {d['na']} / {d['nb']} | {n} | {d['na'] - n} | {d['nb'] - n} | "
                 f"{n / d['na']:.1%} | {n / d['nb']:.1%} | {d['same_s']}/{n} ({d['same_s'] / n:.0%}) | "
                 f"{d['same_e']}/{n} ({d['same_e'] / n:.0%}) | {d['near']} | "
                 f"{d['both_side']['pro']} / {d['both_side']['anti']} / {d['both_side']['neutral']} |")
    for (a, b), _ in pw.items():
        L.append(f'- Spearman rho of per-article flag counts, R{a + 1} vs R{b + 1}: {rho[a, b]:.3f}')
    L.append('\n## Three-way passages (overlapping spans joined)\n')
    combo = collections.Counter(','.join(str(k + 1) for k in p['who']) for p in ps)
    L.append(f'- Passages flagged by any reviewer: {len(ps)}')
    for c in ('1', '2', '3', '1,2', '1,3', '2,3', '1,2,3'):
        L.append('  - flagged by all three' if c == '1,2,3' else
                 f'  - flagged by reviewers {c.replace(",", " and ")} only' if len(c) > 1 else f'  - flagged only by reviewer {c}')
        L[-1] += f': {combo[c]}'
    two = [p for p in ps if p['nsame'] >= 2]
    three = [p for p in ps if p['nsame'] == 3]
    L.append(f'- Flagged by at least two, any side: {sum(len(p["who"]) >= 2 for p in ps)}; flagged by all three, any side: '
             f'{sum(len(p["who"]) == 3 for p in ps)}')
    L.append(f'- Flagged by at least two with the same side: {len(two)}, by side {dict(collections.Counter(p["side"] for p in two))}')
    L.append(f'- Flagged by all three with the same side: {len(three)}, by side {dict(collections.Counter(p["side"] for p in three))}')
    L.append(f'- Of the {len(two)} at-least-two same-side passages, at least two reviewers gave the same fallacy name in '
             f'{sum(bool(p["shared"]) for p in two)}')
    L.append(f'- Passages where two sides each had at least two reviewers (side tie): {len(multi_side)}')
    L.append(f'- Largest passage: {max(len(p["rows"]) for p in ps)} rows; three-reviewer passages where some pair of '
             f'quotes does not overlap directly (joined through the third): '
             f'{sum(1 for p in ps if len(p["who"]) == 3 and not all(overlap(a, b) > 0 for i, (_, a) in enumerate(p["rows"]) for _, b in p["rows"][i + 1:]))}')
    for g, f_ in (('Male circumcision', lambda s: not ('female' in s or s in ('clitoridectomy', 'gishiri-cutting', 'infibulation'))),
                  ('FGM', lambda s: 'female' in s or s in ('clitoridectomy', 'gishiri-cutting', 'infibulation'))):
        L.append(f'  - {g}: at least two same side {dict(collections.Counter(p["side"] for p in two if f_(p["slug"])))}; '
                 f'all three same side {dict(collections.Counter(p["side"] for p in three if f_(p["slug"])))}')
    L.append('\n## R3 by entry\n')
    for k_, v in ctr(r3, 'entry_id').most_common():
        L.append(f'- {k_}: {v}')
    L.append('\n## R3 by article\n')
    for k_, v in ctr(r3, 'slug').most_common():
        L.append(f'- {k_}: {v}')
    L.append('\n## Passages flagged by all three with the same side\n')
    L.append('| article | side | R1 entry | R2 entry | R3 entry |')
    L.append('|---|---|---|---|---|')
    for p in three:
        L.append(f"| {p['slug']} | {p['side']} | " + ' | '.join(
            '/'.join(r['entry_id'] for r in p['byk'][k] if r['favors'] == p['side']) for k in range(3)) + ' |')
    out = '\n'.join(L) + '\n'
    with open(os.path.join(RUN, 'agreement_summary.md'), 'w', encoding='utf-8') as f:
        f.write(out)
    print(out)


if __name__ == '__main__':
    main()
