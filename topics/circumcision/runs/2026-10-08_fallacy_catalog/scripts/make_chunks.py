#!/usr/bin/env python3
"""Cut every saved snapshot into reading chunks for the reviewer.

Each chunk is one article's body (header block dropped, blank lines dropped),
at most about 17,500 characters, cut only at line ends. Every chunk starts with
'=== <slug>' so the reviewer always knows which article it is reading.
58 articles -> 174 chunks. Usage: make_chunks.py OUT_DIR
"""
import sys, pathlib
from split_units import ROOT, slugs, snapshot_paths, body_lines

LIMIT = 17500

def chunks():
    out = []
    for slug in slugs():
        lines = [l for l in body_lines(snapshot_paths(slug)[0].read_text(encoding="utf-8")) if l.strip()]
        head, body = f"=== {slug}\n", ""
        for l in lines:
            if body and len(body) + len(l) + 1 > LIMIT:
                out.append(head + body); body = ""
            body += l + "\n"
        if body:
            out.append(head + body)
    return out

if __name__ == "__main__":
    d = pathlib.Path(sys.argv[1]); d.mkdir(parents=True, exist_ok=True)
    c = chunks()
    for i, t in enumerate(c, 1):
        (d / f"{i:03d}.txt").write_text(t, encoding="utf-8")
    print(len(c), "chunks written to", d)
