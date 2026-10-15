#!/usr/bin/env python3
"""Check every double-quoted string (6+ chars) in the verdict reasons against the source it is attributed to.
Normalisation: collapse whitespace, straighten quotes/dashes, drop soft hyphens, lower-case.
Attribution of a quote, in order:
  1. a "[n]" or "([n])" within 25 characters after the closing quote;
  2. otherwise the nearest preceding source token in the same reason: "[n]" (list source n, cached as refNNN.txt),
     "Elwes" or an Ethics locator such as E2P17 (the pinned Elwes text), or "article"/"Article" (the article);
  3. if the reason names no source at all, the Elwes text.
A quote passes if it occurs in the attributed source, or in the row's own article sentence (quoting the article).
Usage: check_quotes.py verdicts.psv CACHE ETHIC_TXT claims.csv"""
import sys, re, csv, os
verd, cache, ethic, claims = sys.argv[1:5]
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\u2013", "-").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).lower()
_c = {}
def src(key):
    if key not in _c:
        if key == "ELWES": p = ethic
        else: p = os.path.join(cache, f"ref{int(key):03d}.txt")
        _c[key] = norm(open(p, encoding="utf-8", errors="replace").read()) if os.path.exists(p) else ""
    return _c[key]
ART = {r["claim_id"]: norm(r["text"]) for r in csv.DictReader(open(claims, encoding="utf-8"))}
TOK = re.compile(r"\[(\d+)\]|\b(Elwes)\b|\b(E\d(?:P|D|A|App|Pref|DefAff)\w*)|\b([Aa]rticle)\b")
def tokkey(m):
    if m.group(1): return m.group(1)
    if m.group(2) or m.group(3): return "ELWES"
    return "ARTICLE"
bad = n = 0
for i, l in enumerate(open(verd, encoding="utf-8")):
    if i == 0 or not l.strip(): continue
    cid, reason = l.split("|")[0], l.rstrip("\n").split("|", 5)[5]
    for m in re.finditer(r'"([^"]{6,})"', reason):
        n += 1; q = m.group(1); qn = norm(q).strip(" .,")
        after = re.match(r"\s*\(?\[(\d+)\]", reason[m.end():m.end() + 25])
        if after: key = after.group(1)
        else:
            prev = [t for t in TOK.finditer(reason[:m.start()])]
            key = tokkey(prev[-1]) if prev else ("ELWES" if not TOK.search(reason) else tokkey(TOK.search(reason)))
        hay = ART[cid] if key == "ARTICLE" else src(key)
        if qn in hay or qn in ART[cid]: continue
        bad += 1; print(f"{cid} NOT IN {key if key in ('ELWES','ARTICLE') else '['+key+']'}: {q}")
print(f"{n} quotes checked, {bad} not found in the attributed source")
