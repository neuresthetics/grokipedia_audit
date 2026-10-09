#!/usr/bin/env python3
"""Split each saved snapshot (.txt) into reading units: headings, paragraphs,
table rows and sentences. Shared by the citation counter and the reader.

Snapshot layout: a header block, a line of '=' characters, then the body.
In the body, lines starting with '#' are headings, lines containing ' | ' are
table rows, and other non-empty lines are paragraphs. [n] is an in-text
citation pointing at source n.
"""
import re, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3] / "articles"
DATE = "2026-10-01"
MARK = re.compile(r"\[(\d+)\]")
# Sentence end: . ! or ? (optionally followed by closing quote/bracket), then any
# citation markers, then whitespace, then something that can start a sentence.
SPLIT = re.compile(r'(?<=[.!?])(["\u201d\u2019)]?(?:\s*\[\d+\])*)\s+(?=[A-Z0-9"\u201c\u2018(\[])')
ABBREV = re.compile(r'(?:\b(?:Dr|Mr|Mrs|Ms|St|Jr|Sr|vs|v|al|cf|e\.g|i\.e|U\.S|U\.K|No|Vol|pp|ca|c|approx|Gen|Rev|Prof|Inc|Ltd|Co|Fig)\.|\b[A-Z]\.)$')

def snapshot_paths(slug):
    d = ROOT / slug / "snapshots"
    return d / f"{DATE}.txt", d / f"{DATE}_sources.csv"

def slugs():
    return sorted(p.name for p in ROOT.iterdir() if (p / "snapshots").is_dir())

def body_lines(txt):
    lines = txt.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("=====") and set(l.strip()) == {"="}:
            return lines[i + 1:]
    raise ValueError("no header separator")

def sentences(par):
    parts, out, buf = SPLIT.split(par), [], ""
    # SPLIT keeps the captured trailing marker group; rejoin pieces
    i = 0
    pieces = []
    while i < len(parts):
        seg = parts[i] + (parts[i + 1] if i + 1 < len(parts) else "")
        pieces.append(seg)
        i += 2
    for seg in pieces:
        buf = (buf + " " + seg) if buf else seg
        if ABBREV.search(MARK.sub("", buf).rstrip()):
            continue  # likely an abbreviation, not a sentence end
        out.append(buf.strip()); buf = ""
    if buf.strip():
        out.append(buf.strip())
    return [s for s in out if s]

def units(slug):
    """Yield (kind, text) for every unit in the article body."""
    txt = snapshot_paths(slug)[0].read_text(encoding="utf-8")
    for l in body_lines(txt):
        s = l.strip()
        if not s:
            continue
        if s.startswith("#"):
            yield "heading", s
        elif " | " in s:
            yield "table_row", s
        else:
            for sent in sentences(s):
                yield "sentence", sent

def n_sources(slug):
    with open(snapshot_paths(slug)[1], newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))

if __name__ == "__main__":
    import sys
    for slug in (sys.argv[1:] or slugs()):
        for kind, t in units(slug):
            print(f"{slug}\t{kind}\t{t}")
