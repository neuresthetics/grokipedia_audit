#!/usr/bin/env python3
"""Second-chance fetch for sources that failed in `grokaudit.py fetch`.
Order: (1) curl with full browser headers; (2) Wayback Machine latest capture
(https://web.archive.org/web/2026id_/<url>, which redirects to the closest capture). Writes refNNN.txt into the cache with a
VIA: line saying which route worked, and appends data/fetch_log.csv.
Usage: refetch.py data/sources.csv CACHE data/fetch_log.csv"""
import csv, sys, subprocess, json, os, tempfile, re, urllib.parse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../../../../../tools/grokaudit"))
from grokaudit import html_to_text
src, cache, logp = sys.argv[1:4]
H = ["-H", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36",
     "-H", "Accept: text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8", "-H", "Accept-Language: en-US,en;q=0.9"]
def curl(url):
    with tempfile.NamedTemporaryFile(delete=False) as tf: p = tf.name
    r = subprocess.run(["curl", "-sL", "--compressed", "--max-time", "40", "-o", p, "-w", "%{http_code}"] + H + [url], capture_output=True, text=True)
    data = open(p, "rb").read(); os.unlink(p); return r.stdout.strip(), data
def to_text(data):
    if data[:4] == b"%PDF":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as tf:
            tf.write(data); tf.flush()
            return subprocess.run(["pdftotext", "-layout", tf.name, "-"], capture_output=True, text=True).stdout
    return html_to_text(data.decode("utf-8", errors="replace"))
BLOCK = re.compile(r"just a moment|enable javascript and cookies|access denied|captcha|are you a robot|cf-chl", re.I)
log = open(logp, "a", newline="", encoding="utf-8"); w = csv.writer(log)
for r in csv.DictReader(open(src, encoding="utf-8")):
    n = int(r["n"]); dest = os.path.join(cache, f"ref{n:03d}.txt")
    if os.path.exists(dest) and os.path.getsize(dest) > 3000: continue
    via, txt, note = None, "", ""
    code, data = curl(r["url"])
    if code == "200" and data:
        t = to_text(data)
        if len(t) > 1500 and not BLOCK.search(t[:3000]): via, txt = "live-curl", t
        else: note = f"live 200 but {len(t)} chars / bot wall"
    else: note = f"live HTTP {code}"
    if not via:
        c3, d3 = curl("https://web.archive.org/web/2026id_/" + r["url"])
        t = to_text(d3) if d3 else ""
        if c3 == "200" and len(t) > 1500 and not BLOCK.search(t[:3000]): via, txt = "wayback (web.archive.org/web/2026id_/<url>, latest capture)", t
        else: note += f"; wayback HTTP {c3}, {len(t)} chars"
    if via:
        open(dest, "w", encoding="utf-8").write(f"URL: {r['url']}\nVIA: {via}\n\n{txt}")
    w.writerow([n, r["url"], via or "not reachable", note]); log.flush(); print(n, via or "FAIL", note)
