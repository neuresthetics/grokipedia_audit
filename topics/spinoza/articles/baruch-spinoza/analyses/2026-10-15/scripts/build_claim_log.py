#!/usr/bin/env python3
"""Merge parse output, retrieval evidence, the hand-written verdict file and the Ethics index
into the per-sentence claim log (data/claim_log.csv).
Excerpts are copied verbatim (whitespace-collapsed) from fetched source text and from the pinned
Elwes text; nothing in an excerpt column is typed by hand.
Usage: build_claim_log.py data/claims.csv data/evidence.jsonl data/verdicts.psv data/ethics_index.csv ETHIC_TXT data/fetch_log.csv data/linkcheck.csv OUT.csv"""
import csv, json, re, sys
claims, evid, verd, idx, ethic, flog, lchk, out = sys.argv[1:9]
VERD = {"S": "supported", "P": "partly supported", "U": "unsupported", "M": "miscited",
        "X": "unverifiable (source not reachable or not listed)", "N": "uncited"}
EV = {"PM": "primary-text-match", "PX": "primary-text-mismatch", "NP": "no primary text on hand"}
NP = set(("C101 C102 C104 C105 C106 C107 C108 C109 C110 C112 C234 C235 C236 C237 C238 C239 C240 C242 C244 C245 "
          "C246 C247 C248 C250 C251 C252 C276 C279 C282 C283 C305 C309 C310 C311 C312 C313 C316 C317 C318 C319 "
          "C320 C322 C323 C324 C327 C328 C332").split())
V = {}
for i, l in enumerate(open(verd, encoding="utf-8")):
    if i == 0: continue
    p = l.rstrip("\n").split("|", 5); V[p[0]] = p
IDX = {r["locator"]: r for r in csv.DictReader(open(idx, encoding="utf-8"))}
LINES = open(ethic, encoding="utf-8", errors="replace").read().split("\n")
E = {json.loads(l)["claim_id"]: json.loads(l) for l in open(evid, encoding="utf-8")}
via = {int(r["n"]): r["via"] for r in csv.DictReader(open(flog, encoding="utf-8"))}
toks = lambda s: {w for w in re.findall(r"[a-z]{4,}", s.lower())}
def elwes(loc, text):
    loc, _, phrase = loc.partition("@")
    r = IDX[loc]; a, b = int(r["line_start"]), int(r["line_end"])
    ct = toks(text); best = (-1, a)
    if phrase:  # verdict file may name a phrase that must occur verbatim in the entry
        hits = [i for i in range(a, b + 1) if phrase in LINES[i - 1]]
        if not hits: raise SystemExit(f"phrase not found in {loc}: {phrase}")
        best = (99, hits[0])
    for i in (range(a, min(b, a + 400) + 1) if not phrase else []):
        win = " ".join(LINES[i - 1:i + 2]); sc = len(ct & toks(win))
        if sc > best[0]: best = (sc, i)
    i = best[1]
    if i != a:  # always show the entry's first line, then the best-matching lines
        return i, i + 2, LINES[a - 1].strip() + " [...] " + " ".join(x.strip() for x in LINES[i - 1:i + 2])
    return a, min(a + 2, b), " ".join(x.strip() for x in LINES[a - 1:min(a + 2, b)])
def status(c):
    if not c.get("listed"): return "not listed (dangling number)"
    if c["fetched"]: return "fetched (" + via.get(c["n"], "live") .replace(", latest capture", "") + ")"
    return "not reachable / no readable text"
F = ["sentence_id", "section", "article_text", "cite_numbers", "cited_sources", "source_status", "source_excerpt",
     "intended_sources", "intended_excerpt", "ethics_locator", "ethics_elwes_lines", "ethics_elwes_text",
     "verdict", "verdict_vs_intended", "primary_text_check", "reason", "checker", "date"]
w = csv.DictWriter(open(out, "w", newline="", encoding="utf-8"), fieldnames=F); w.writeheader()
for c in csv.DictReader(open(claims, encoding="utf-8")):
    cid = c["claim_id"]; v = V[cid]; e = E[cid]
    L = [x["linked"] for x in e["cites"]]; I = [x["intended"] for x in e["cites"]]
    row = {"sentence_id": cid, "section": c["section"], "article_text": c["text"], "cite_numbers": c["cites"],
           "cited_sources": " ; ".join(f"[{x['n']}] " + (f"{x['title']} <{x['url']}>" if x.get("listed") else "NOT IN SOURCE LIST") for x in L),
           "source_status": " ; ".join(f"[{x['n']}] {status(x)}" for x in L),
           "source_excerpt": " ; ".join(f"[{x['n']}] \"{x['passage'][:320]}\"" for x in L if x.get("listed") and x["fetched"]),
           "intended_sources": " ; ".join(f"[{a['n']}->{b['n']}] {b['title']}" for a, b in zip(L, I) if b.get("listed") and a["n"] != b["n"]),
           "intended_excerpt": " ; ".join(f"[{b['n']}] \"{b['passage'][:320]}\"" for a, b in zip(L, I) if b.get("listed") and b["fetched"] and a["n"] != b["n"]),
           "verdict": VERD[v[1]], "verdict_vs_intended": VERD[v[2]], "reason": v[5],
           "checker": "Grok Bot (model), single reader; retrieval by scripts/evidence.py", "date": "2026-10-15"}
    if v[3]:
        a, b, t = elwes(v[3], c["text"])
        row.update(ethics_locator=v[3].partition("@")[0], ethics_elwes_lines=f"{a}-{b}", ethics_elwes_text=t[:600],
                   primary_text_check=EV[v[4]])
    elif cid in NP:
        row["primary_text_check"] = EV["NP"]
    w.writerow(row)
print("ok")
