#!/usr/bin/env python3
"""Shared helper: the run's own sentence split (../../scripts/split_units.py), with each
sentence located in the snapshot text so flag quotes can be mapped to sentences by
character span.

sentence_id = s0001, s0002, ... in reading order, counting only units of kind
"sentence" (headings and table rows are not sentences, same as citation_stats.csv).
Spans are found by a forward search that tolerates whitespace differences, because
split_units joins pieces with a single space.
"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parents[1]
sys.path.insert(0, str(RUN / "scripts"))
sys.dont_write_bytecode = True
from split_units import slugs, units, snapshot_paths, body_lines  # noqa: E402

FGM_EXTRA = {"clitoridectomy", "gishiri-cutting", "infibulation"}


def group(slug):
    return "FGM" if ("female" in slug or slug in FGM_EXTRA) else "male"


def text(slug):
    return snapshot_paths(slug)[0].read_text(encoding="utf-8")


def sentence_rows(slug):
    """[(sentence_id, text, start, end)] with start/end char offsets in the full snapshot file."""
    t = text(slug)
    sep = re.search(r"^=+$", t, re.M)
    pos = sep.end()
    out, k = [], 0
    for kind, s in units(slug):
        toks = s.split()
        pat = r"\s+".join(re.escape(x) for x in toks)
        m = re.compile(pat).search(t, pos)
        if m is None:
            raise ValueError(f"cannot locate unit in {slug}: {s[:60]}")
        pos = m.end()
        if kind == "sentence":
            k += 1
            out.append((f"s{k:04d}", s, m.start(), m.end()))
    return out


if __name__ == "__main__":
    tot = 0
    for s in slugs():
        n = len(sentence_rows(s)); tot += n
    print("sentences", tot)
