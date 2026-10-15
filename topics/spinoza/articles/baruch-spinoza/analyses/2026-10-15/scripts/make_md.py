#!/usr/bin/env python3
"""Build snapshots/<date>.md from grokaudit parse output (claims.csv, sources.csv).
Text is copied verbatim from claims.csv; citation markers re-added as ' [n]'.
Usage: python3 make_md.py data/claims.csv data/sources.csv OUT.md "Oct 15, 2026" """
import csv, sys
claims, sources, out, date = sys.argv[1:5]
rows = list(csv.DictReader(open(claims, encoding="utf-8")))
L = ["# Baruch Spinoza (Grokipedia)", "",
     f"Source: [grokipedia.com/page/Baruch_Spinoza](https://grokipedia.com/page/Baruch_Spinoza), pulled {date}.", ""]
sec_h2 = sec_h3 = None; para = None; buf = []
def flush():
    if buf: L.append(" ".join(buf)); L.append(""); buf.clear()
for r in rows:
    parts = r["section"].split(" > ") if r["section"] else []
    h2 = parts[0] if parts else None; h3 = parts[1] if len(parts) > 1 else None
    if h2 != sec_h2:
        flush(); sec_h2 = h2; sec_h3 = None
        if h2: L += [f"## {h2}", ""]
    if h3 != sec_h3:
        flush(); sec_h3 = h3
        if h3: L += [f"### {h3}", ""]
    if r["para"] != para: flush(); para = r["para"]
    cites = " ".join(f"[{c}]" for c in r["cites"].split())
    buf.append(r["text"] + (" " + cites if cites else ""))
flush()
L += ["## References", ""]
for s in csv.DictReader(open(sources, encoding="utf-8")):
    L.append(f"{s['n']}. [{s['title']}]({s['url']})"); L.append("")
open(out, "w", encoding="utf-8").write("\n".join(L))
