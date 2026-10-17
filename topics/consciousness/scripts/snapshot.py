#!/usr/bin/env python3
"""Fetch Grokipedia pages and write articles/<slug>/snapshots/<date>.html (as fetched) and .md.
Parsing reuses tools/grokaudit/grokaudit.py parse_page (div.article-body span[data-tts-block];
sources li#ref-N a.ref-link), same as the Spinoza make_md.py. The .md keeps every sentence with an id
(**C0001**) and its inline [n] markers, then the numbered source list.
Writes snapshot_log.json. Usage: python3 scripts/snapshot.py 2026-10-17"""
import sys, json, hashlib, datetime, re, urllib.request, pathlib
from zoneinfo import ZoneInfo
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / "tools" / "grokaudit"))
from grokaudit import parse_page
PAGES = ["Integrated_information_theory","Giulio_Tononi","Christof_Koch","The_Feeling_of_Life_Itself",
 "Global_workspace_theory","Stanislas_Dehaene","Higher-order_theories_of_consciousness","Attention_schema_theory",
 "Predictive_coding","Orchestrated_objective_reduction","Neural_correlates_of_consciousness","Models_of_consciousness",
 "the_science_of_consciousness","Consciousness","Hard_problem_of_consciousness","Panpsychism",
 "Artificial_consciousness","Anil_Seth"]
date = sys.argv[1]
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
log = []
for t in PAGES:
    url = f"https://grokipedia.com/page/{t}"
    rec = {"title": t, "slug": slug(t), "url": url}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (grokipedia_audit snapshot)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read(); rec["status"] = r.status
    except Exception as e:
        rec["status"] = getattr(e, "code", None); rec["error"] = repr(e); log.append(rec); print(t, e); continue
    rec["fetched_pt"] = datetime.datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d %H:%M:%S %Z")
    d = ROOT / "articles" / rec["slug"] / "snapshots"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{date}.html").write_bytes(raw)
    claims, sources = parse_page(raw.decode("utf-8", "replace"))
    for i, c in enumerate(claims, 1): c["claim_id"] = f"C{i:04d}"
    L = [f"# {t.replace('_', ' ')} (Grokipedia)", "", f"Source: [{url}]({url}), pulled {date} ({rec['fetched_pt']}).",
         "Sentence ids in bold; inline [n] markers kept as on the page.", ""]
    sec = None; para = None; buf = []
    def flush():
        if buf: L.extend([" ".join(buf), ""]); buf.clear()
    for c in claims:
        if c["section"] != sec:
            flush(); sec = c["section"]
            if sec:
                parts = sec.split(" > "); L += [("#" * (len(parts) + 1)) + " " + parts[-1], ""]
        if c["para"] != para: flush(); para = c["para"]
        cites = " ".join(f"[{n}]" for n in c["cites"])
        buf.append(f"**{c['claim_id']}** {c['text']}" + (" " + cites if cites else ""))
    flush()
    L += ["## References", ""]
    for s in sources: L += [f"{s['n']}. [{s.get('title','')}]({s.get('url','')})", ""]
    md = "\n".join(L); (d / f"{date}.md").write_text(md, encoding="utf-8")
    markers = [n for c in claims for n in c["cites"]]
    nmax = max([int(s["n"]) for s in sources], default=0)
    beyond = sorted({n for n in markers if int(n) > nmax}, key=int)
    rec.update(sha256_html=hashlib.sha256(raw).hexdigest(), sha256_md=hashlib.sha256(md.encode()).hexdigest(),
               sentences=len(claims), sources=len(sources), markers=len(markers), distinct_markers=len(set(markers)),
               max_marker=max(map(int, markers), default=0), beyond=len(beyond), beyond_list=beyond)
    log.append(rec); print(t, rec["status"], len(claims), len(sources), len(markers), len(beyond))
json.dump(log, open(ROOT / "snapshot_log.json", "w"), indent=1)
