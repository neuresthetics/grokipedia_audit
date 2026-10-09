#!/usr/bin/env python3
"""Assemble FULL_RECORD.md by copying existing text verbatim, in step order.

Every block is cut programmatically from a named source file and section, then checked to appear verbatim
in that source. The only added text is headings and source labels. For blocks from files in other folders,
relative link targets inside (...) are re-based so they resolve from this file; the visible text is unchanged,
and the script checks that the block with its original targets is in the source.
Images appear once each: the walkthrough's chart images. Image lines in ANALYSIS.md and TOTAL_WHATIF.md
sections are left out (each left-out block is an image line only).

Run from anywhere:  python3 topics/circumcision/runs/2026-10-08_fallacy_catalog/scripts/build_full_record.py
"""
import os, re
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
ROOT = RUN.parents[3]
OUT = RUN / "FULL_RECORD.md"


def read(rel):
    return (ROOT / rel).read_text()


def section(rel, heading, level=2):
    """Text of a section from its heading line up to the next heading of the same or higher level."""
    s = read(rel)
    lines = s.split("\n")
    i = next(k for k, l in enumerate(lines) if l == heading)
    j = i + 1
    while j < len(lines) and not re.match(r"#{1,%d} " % level, lines[j]):
        j += 1
    return "\n".join(lines[i:j]).strip("\n")


def lines_between(rel, start, stop=None):
    lines = read(rel).split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith(start))
    j = len(lines) if stop is None else next(k for k, l in enumerate(lines) if k > i and l.startswith(stop))
    return "\n".join(lines[i:j]).strip("\n")


def readme_step(n):
    return next(l for l in read("README.md").split("\n") if l.startswith(f"{n}. **"))


def rebase(block, src_rel):
    src_dir = (ROOT / src_rel).parent

    def fix(m):
        t = m.group(2)
        if re.match(r"[a-z]+:|#", t):
            return m.group(0)
        path, _, frag = t.partition("#")
        new = os.path.relpath(os.path.normpath(src_dir / path), RUN).replace(os.sep, "/")
        return f"{m.group(1)}({new}{'#' + frag if frag else ''})"
    return re.sub(r"(\])\(([^)\s]+)\)", fix, block)


def text_only(block):
    """Drop image-only paragraphs; keep every other paragraph as is."""
    paras = block.split("\n\n")
    return [p for p in paras if not p.strip().startswith("![")]


parts, used = [], []


def add(src_rel, label, block):
    assert block in read(src_rel), f"not verbatim: {label}"
    parts.append(f"*Source: {label}*\n\n" + (rebase(block, src_rel) if (ROOT / src_rel).parent != RUN else block))
    used.append(label)


def add_paras(src_rel, label, block):
    for p in text_only(block):
        assert p in read(src_rel), f"not verbatim: {label}"
    add_joined = "\n\n".join(text_only(block))
    for p in text_only(block):
        assert p in read(src_rel)
    parts.append(f"*Source: {label} (text only: image lines left out; each chart is shown once, in the walkthrough block)*\n\n" +
                 (rebase(add_joined, src_rel) if (ROOT / src_rel).parent != RUN else add_joined))
    used.append(label + " (text only)")


W = "topics/circumcision/runs/2026-10-08_fallacy_catalog/WALKTHROUGH.md"
A = "topics/circumcision/runs/2026-10-08_fallacy_catalog/ANALYSIS.md"
T = "topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/whatif_total/TOTAL_WHATIF.md"
P = "topics/circumcision/background/authors_position.md"

parts.append("# Full record: circumcision articles, fallacy_catalog run (2026-10-08)")
parts.append("## Part 1. The author's position")
add(P, "background/authors_position.md (whole file)", read(P).strip("\n"))

parts.append("## Part 2. The steps, in order, with their charts")
add(W, "WALKTHROUGH.md, introduction and caveats", lines_between(W, "# Walkthrough", "## 1. "))

STEPS = [
    ("## 1. Snapshots", [1], []),
    ("## 2. Claim and source check (citation markers only, so far)", [2, 3], ["## Citation hygiene"]),
    ("## 3. Three reviewers' fallacy flags", [4], ["## What was done"]),
    ("## 4. Comparison and charts 01–04", [], ["## Headline: which side's case relies more on flawed reasoning?",
                                               "## Which articles have the most flawed reasoning per sentence?",
                                               "## Male circumcision vs FGM articles, all sides",
                                               "## How much the reviewers' flags overlap"]),
    ("## 5. Survival scoring and chart 05", [5], ["## What survived: how much of each side's argument was never flagged?"]),
    ("## 6. Flagged pro arguments by type and chart 06", [6], ["## Flagged pro arguments: what kinds of flawed reasoning?"]),
    ("## 7. Dependency pass (pass 2), pass-3 recheck and chart 07", [],
     ["## Flagged pro arguments: did the survivors lean on them, and do they hold up?"]),
    ("## 8. Topic tagging and chart 08", [7], ["## What do the surviving pro arguments rely on?"]),
    ("## 9. What-if checks: HIV/STI and cancer, charts 09 and 10", [8],
     ["## What-if: how many medical arguments rest on the HIV/STI or cancer claims?"]),
    ("## 10. Total what-if: how much of the pro side is left, chart 11", [],
     ["## What-if: how much of the pro side is left under Jason's premises?"]),
]
for wh, rsteps, asecs in STEPS:
    n = wh.split(".")[0][3:]
    add(W, f"WALKTHROUGH.md, section '{wh[3:]}'", section(W, wh))
    for k in rsteps:
        add("README.md", f"README.md, 'How it works' step {k}", readme_step(k))
    for a in asecs:
        add_paras(A, f"ANALYSIS.md, section '{a[3:]}'", section(A, a))
    if n == "10":
        add(W, "WALKTHROUGH.md, appended 'Note on chart 11' and step 10 line", section(W, "## Note on chart 11 (appended)"))
        for t in ["## Result", "## Counting rules (no double counting)",
                  "## Not checked: non-medical arguments that lean on HIV/STI or cancer", "## Caveats",
                  "## The premises, in plain words", "## Limits: a narrow selection"]:
            add_paras(T, f"flagged_pro/whatif_total/TOTAL_WHATIF.md, section '{t[3:]}'", section(T, t))


OUT.write_text("\n\n".join(parts) + "\n")

# check: every local link and image in the output resolves
bad = []
for m in re.finditer(r"\]\(([^)\s]+)\)", OUT.read_text()):
    t = m.group(1).partition("#")[0]
    if t and not re.match(r"[a-z]+:", t) and not (RUN / t).exists():
        bad.append(t)
imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", OUT.read_text())
print(f"wrote {OUT.relative_to(ROOT)}: {len(used)} blocks, {len(imgs)} images, broken links: {bad or 'none'}")
for u in used:
    print("  -", u)
for i in imgs:
    print("  img", i.rsplit("/", 1)[-1])
assert not bad
