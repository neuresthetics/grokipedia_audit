#!/usr/bin/env python3
"""Charts for the 2026-10-08 circumcision fallacy_catalog run (simple public set).

Run from the repo root (needs matplotlib):
    python3 tools/make_charts_2026_10_08.py

Reads only committed files:
  topics/circumcision/ARTICLE_LIST.md                       the 58 article slugs
  topics/circumcision/runs/2026-10-08_fallacy_catalog/
    flags.csv, reviewer2_flags.csv, reviewer3_flags.csv     Reviewer 1, 2, 3 rows
    overlap_3way.csv                                        passages (overlapping quotes in one article,
                                                            joined across the three reviewers)
    citation_stats.csv                                      per-article counts; `sentences` (prose
                                                            sentences in the 2026-10-01 snapshot) is the
                                                            denominator of every "per 100 sentences" rate

The three reviewers are separate AI reader runs with the same catalog and method. They were not blind:
Reviewers 2 and 3 were started with instructions that mentioned earlier results.

Article groups: FGM if the slug contains "female" or is clitoridectomy, gishiri-cutting or infibulation;
all other articles are in the male circumcision group (matches the run README).

Cleaner-argued rule (headline chart): a side gets a check only if the other side has at least 2x as many
flags (same sentences, so the same ratio per 100 sentences) and at least 5 flags.

Writes PNGs to docs/img/circumcision/2026-10-08/ and prints every number it draws.
Every flag is an AI reader's judgment: a lead to check, not a verdict.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Patch, Rectangle  # noqa: E402

sys.dont_write_bytecode = True
TOPIC = Path("topics/circumcision")
RUN = TOPIC / "runs/2026-10-08_fallacy_catalog"
OUT = Path("docs/img/circumcision/2026-10-08")
if not (RUN / "flags.csv").exists():
    sys.exit("Run this from the repo root: python3 tools/make_charts_2026_10_08.py")
OUT.mkdir(parents=True, exist_ok=True)

SIDES = ("pro", "anti", "neutral")
# Okabe-Ito colorblind-safe palette
COLOR = {"pro": "#E69F00", "anti": "#0072B2", "neutral": "#A6A6A6"}
INK, MUTED, SOFT, GRID = "#1F2328", "#57606A", "#8C959F", "#EAEEF2"
BOTS = {"Reviewer 1": "#24292F", "Reviewer 2": "#6E7781", "Reviewer 3": "#AFB8C1"}
FOOTER = ("Source: neuresthetics/grokipedia_audit · fallacy_catalog v0.6.1 · snapshots 2026-10-01 · "
          "AI reader flags are leads, not verdicts. Not blind.")
CLEAN_NOTE = "Fewer flaws means argued more cleanly here, not that the conclusion is right."
RULE_RATIO, RULE_MIN = 2.0, 5
W_IN, DPI = 16, 100  # 1600 px wide

plt.rcParams.update({
    "font.family": ["Lato", "DejaVu Sans"], "font.size": 14,
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
    "axes.edgecolor": SOFT, "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": INK,
    "axes.grid": True, "axes.grid.axis": "x", "grid.color": GRID, "grid.linewidth": 1.0,
    "axes.axisbelow": True, "xtick.major.size": 0, "ytick.major.size": 0,
})


# ------------------------------------------------------------------ robot icon (vector)
def robot_artists(x, y, s, color, transform=None):
    """Simple robot head in a box of size s at (x, y) (lower left). Needs equal-aspect coordinates."""
    kw = {} if transform is None else {"transform": transform}
    P = lambda u, v: (x + u * s, y + v * s)  # noqa: E731
    arts = [
        Line2D([P(0.5, 0.76)[0], P(0.5, 0.9)[0]], [P(0.5, 0.76)[1], P(0.5, 0.9)[1]], color=color,
               linewidth=max(0.8, s * 0.06), solid_capstyle="round", **kw),
        Circle(P(0.5, 0.93), 0.07 * s, color=color, **kw),
        Rectangle(P(0.02, 0.36), 0.1 * s, 0.2 * s, color=color, **kw),
        Rectangle(P(0.88, 0.36), 0.1 * s, 0.2 * s, color=color, **kw),
        FancyBboxPatch(P(0.12, 0.1), 0.76 * s, 0.66 * s, boxstyle=f"round,pad=0,rounding_size={0.14 * s}",
                       facecolor=color, edgecolor=color, **kw),
        Circle(P(0.35, 0.5), 0.1 * s, color="white", **kw),
        Circle(P(0.65, 0.5), 0.1 * s, color="white", **kw),
        Rectangle(P(0.32, 0.22), 0.36 * s, 0.08 * s, color="white", **kw),
    ]
    return arts


def fig_robot(fig, x, y, h, color):
    """Robot icon in figure coordinates; (x, y) lower left, h = height as a fraction of figure height."""
    W, H = fig.get_size_inches()
    w = h * H / W
    a = fig.add_axes([x, y, w, h])
    a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
    for art in robot_artists(0, 0, 1, color):
        a.add_artist(art)
    return w


def read(name, base=RUN):
    with open(base / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


REV = {"Reviewer 1": read("flags.csv"), "Reviewer 2": read("reviewer2_flags.csv"),
       "Reviewer 3": read("reviewer3_flags.csv")}
p3 = read("overlap_3way.csv")
cites = read("citation_stats.csv")
SENT = {r["slug"]: int(r["sentences"]) for r in cites}
slugs = re.findall(r"\]\(articles/([^/]+)/snapshots/", (TOPIC / "ARTICLE_LIST.md").read_text(encoding="utf-8"))
assert len(slugs) == 58 and set(slugs) == set(SENT), "article list and citation_stats.csv do not match"
FGM_EXTRA = {"clitoridectomy", "gishiri-cutting", "infibulation"}


def group(slug):
    return "FGM" if ("female" in slug or slug in FGM_EXTRA) else "Male circumcision"


def count(rows, side, f=lambda s: True):
    return sum(1 for r in rows if r["favors"] == side and f(r["slug"]))


def rate(n, sentences):
    return 100.0 * n / sentences


def head(fig, title, subtitle):
    H = fig.get_figheight()
    fig.text(0.04, 1 - 0.42 / H, title, ha="left", va="top", fontsize=26, fontweight="bold", color=INK)
    fig.text(0.04, 1 - 1.02 / H, subtitle, ha="left", va="top", fontsize=15.5, color=MUTED)


def foot(fig, lines, name):
    H = fig.get_figheight()
    y = 0.28 / H
    fig.text(0.04, y, FOOTER, ha="left", va="bottom", fontsize=11, color=SOFT)
    for ln in reversed(lines):
        y += 0.3 / H
        fig.text(0.04, y, ln, ha="left", va="bottom", fontsize=12, color=MUTED)
    fig.savefig(OUT / name, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  wrote {OUT / name}")


n_fgm = sum(group(s) == "FGM" for s in slugs)
print(f"Articles: {len(slugs)} ({len(slugs) - n_fgm} male circumcision, {n_fgm} FGM); "
      f"sentences {sum(SENT.values())}")
for name, rows in REV.items():
    print(f"  {name}: {len(rows)} flags, by side {dict(Counter(r['favors'] for r in rows))}")

# ============================================================= 1. headline
print("\n[1] Which side's case relies more on flawed reasoning? (flags per 100 sentences)")
print(f"  Rule: check the cleaner-argued side only if the other side has >= {RULE_RATIO:g}x its flags "
      f"and >= {RULE_MIN} flags.")
GROUPS = [("Male circumcision articles", "Male circumcision"), ("FGM articles", "FGM")]


def cleaner(pro, anti):
    big, small = max(pro, anti), min(pro, anti)
    if pro != anti and big >= RULE_MIN and (small == 0 or big / small >= RULE_RATIO):
        return "anti" if pro > anti else "pro"
    return None


res = {}
for title, g in GROUPS + [("All 58 articles", None)]:
    f = (lambda s, g=g: group(s) == g) if g else (lambda s: True)
    sent = sum(SENT[s] for s in slugs if f(s))
    for name, rows in REV.items():
        pro, anti = count(rows, "pro", f), count(rows, "anti", f)
        c = cleaner(pro, anti)
        res[title, name] = dict(pro=pro, anti=anti, sent=sent, pr=rate(pro, sent), ar=rate(anti, sent), clean=c)
        print(f"  {title} ({sent} sentences) {name}: pro {pro} = {rate(pro, sent):.2f}, anti {anti} = "
              f"{rate(anti, sent):.2f} per 100 sentences; cleaner-argued: {c or 'no clear difference'}")


def takeaway(title):
    cs = [res[title, n]["clean"] for n in REV]
    if all(c == "anti" for c in cs):
        return "all three readers find far more flawed reasoning helping the pro side"
    if all(c == "pro" for c in cs):
        return "all three readers find far more flawed reasoning helping the anti side"
    return "the readers split"


tk = {t: takeaway(t) for t, _ in GROUPS}
print("  takeaway: " + "; ".join(f"{t}: {v}" for t, v in tk.items()))
fig, axes = plt.subplots(1, 2, figsize=(W_IN, 9.2), sharey=True)
xmax = max(max(d["pr"], d["ar"]) for (t, _), d in res.items() if t != "All 58 articles")
bh = 0.32
for ax, (title, g) in zip(axes, GROUPS):
    for i, name in enumerate(REV):
        d = res[title, name]
        for off, side, v, n in ((-bh / 2 - 0.02, "pro", d["pr"], d["pro"]), (bh / 2 + 0.02, "anti", d["ar"], d["anti"])):
            ax.barh(i + off, v, height=bh, color=COLOR[side], zorder=2)
            lab = f"{v:.2f}  ({n})"
            if d["clean"] == side:
                lab += "   ✔ cleaner"
            ax.text(v + xmax * 0.02, i + off, lab, va="center", fontsize=13,
                    color=INK if d["clean"] == side else MUTED,
                    fontweight="bold" if d["clean"] == side else "normal")
    ax.set_xlim(0, xmax * 1.55)
    ax.set_ylim(2.6, -0.6)
    ax.set_title(f"{title}\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
    ax.text(0, 1.0, f"{sum(group(s) == g for s in slugs)} articles, {res[title, 'Reviewer 1']['sent']:,} sentences",
            transform=ax.transAxes, va="bottom", fontsize=13, color=MUTED)
    ax.set_xlabel("flags per 100 sentences", fontsize=13)
    ax.spines["bottom"].set_color(SOFT)
axes[0].set_yticks(range(3), list(REV), fontsize=15)
fig.subplots_adjust(left=0.15, right=0.98, top=0.70, bottom=0.23, wspace=0.12)
for i, name in enumerate(REV):
    yf = axes[0].transData.transform((0, i))[1] / (fig.get_figheight() * DPI)
    fig_robot(fig, 0.022, yf - 0.025, 0.05, BOTS[name])
fig.legend(handles=[Patch(color=COLOR["pro"], label="Pro: the flaw helps the case for the practice"),
                    Patch(color=COLOR["anti"], label="Anti: the flaw helps the case against it")],
           loc="upper left", bbox_to_anchor=(0.15, 0.85), ncol=2, frameon=False, fontsize=13.5,
           handlelength=1.4, columnspacing=2.5)
head(fig, "Which side's case relies more on flawed reasoning?",
     f"Male circumcision articles: {tk['Male circumcision articles']}. FGM articles: {tk['FGM articles']}.")
a = {n: res["All 58 articles", n] for n in REV}
foot(fig, [f"Flags per 100 sentences, pro vs anti, by AI reader (count in brackets). {CLEAN_NOTE}",
           f"✔ cleaner = the other side has at least {RULE_RATIO:g}× as many flags and at least {RULE_MIN}. "
           "All 58 articles, pro vs anti: " + ", ".join(f"R{k + 1} {a[n]['pr']:.2f} vs {a[n]['ar']:.2f}"
                                                         for k, n in enumerate(REV)) + "."],
     "01_which_side.png")

# ============================================================= 2. most-flagged articles
print("\n[2] Most-flagged articles: average of the three readers' flags per 100 sentences (top 10)")
rows2 = []
for s in slugs:
    per = {n: sum(r["slug"] == s for r in rows) for n, rows in REV.items()}
    if not sum(per.values()):
        continue
    side_avg = {sd: sum(count(rows, sd, lambda x, s=s: x == s) for rows in REV.values()) / 3 * 100 / SENT[s]
                for sd in SIDES}
    rows2.append(dict(slug=s, per=per, rt={n: rate(v, SENT[s]) for n, v in per.items()}, side=side_avg,
                      avg=sum(side_avg.values())))
rows2.sort(key=lambda t: (-t["avg"], t["slug"]))
for k, t in enumerate(rows2, 1):
    print(f"  {k:2d}. {t['slug']} ({SENT[t['slug']]} sentences): avg {t['avg']:.2f} = "
          + ", ".join(f"{sd} {t['side'][sd]:.2f}" for sd in SIDES) + "; "
          + ", ".join(f"{n} {t['rt'][n]:.2f} ({t['per'][n]})" for n in REV))
top = rows2[:10]
fig, ax = plt.subplots(figsize=(W_IN, 9.5))
for i, t in enumerate(top):
    left = 0
    for sd in SIDES:
        v = t["side"][sd]
        if v:
            ax.barh(i, v, left=left, height=0.62, color=COLOR[sd], zorder=2)
        left += v
    ax.text(left + 0.05, i, f"{t['avg']:.2f}", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(left + 0.38, i, "R1 {:.1f} · R2 {:.1f} · R3 {:.1f}".format(*(t["rt"][n] for n in REV)),
            va="center", fontsize=12, color=SOFT)
ax.set_yticks(range(len(top)), [t["slug"] + ("  (FGM)" if group(t["slug"]) == "FGM" else "") for t in top],
              fontsize=13.5)
ax.set_ylim(len(top) - 0.4, -0.6)
ax.set_xlim(0, top[0]["avg"] * 1.6)
ax.set_xlabel("flags per 100 sentences (average of the three readers)", fontsize=13)
ax.legend(handles=[Patch(color=COLOR[s], label=s) for s in SIDES], loc="lower right", frameon=False,
          fontsize=13, title="flaw helps", title_fontsize=12, alignment="left")
fig.subplots_adjust(left=0.34, right=0.98, top=0.83, bottom=0.17)
head(fig, "Most-flagged articles",
     f"Top 10 of {len(rows2)} flagged articles by flagged reasoning per 100 sentences, averaged over three AI readers.")
foot(fig, ["Grey text: each reader's own rate. Short articles can rank high from a few flags. " + CLEAN_NOTE],
     "02_most_flagged_articles.png")

# ============================================================= 3. citation gaps
print("\n[3] Citation gaps: share of prose sentences with no [n] marker (top 10) and broken source lists")
cs = sorted(cites, key=lambda r: (-float(r["pct_sentences_uncited"]), r["slug"]))
broken = [r for r in cites if int(r["distinct_numbers_beyond"]) >= 10]
tot_s = sum(int(r["sentences"]) for r in cites)
tot_u = sum(int(r["sentences_uncited"]) for r in cites)
print(f"  all 58: {tot_u}/{tot_s} = {tot_u / tot_s:.1%}")
for r in cs[:10]:
    print(f"  {r['slug']}: {r['pct_sentences_uncited']}% ({r['sentences_uncited']}/{r['sentences']})")
for r in broken:
    print(f"  broken list: {r['slug']} lists {r['sources_listed']} sources, cites up to [{r['highest_marker']}], "
          f"{r['markers_beyond_list']} markers past the list; uncited {r['pct_sentences_uncited']}%")
bset = {r["slug"] for r in broken}
top3 = cs[:10]
fig, ax = plt.subplots(figsize=(W_IN, 9.5))
for i, r in enumerate(top3):
    v = float(r["pct_sentences_uncited"])
    b = r["slug"] in bset
    ax.barh(i, v, height=0.62, color="#CC79A7" if b else "#56B4E9", zorder=2)
    ax.text(v + 0.8, i, f"{v:.1f}%" + ("   source list broken" if b else ""), va="center", fontsize=14,
            fontweight="bold" if b else "normal", color=INK)
avg = tot_u / tot_s * 100
ax.axvline(avg, color=MUTED, linestyle=(0, (4, 3)), linewidth=1.3, zorder=1)
ax.text(avg, -0.75, f"all 58 articles: {avg:.1f}%", ha="center", va="bottom", fontsize=12.5, color=MUTED)
ax.set_yticks(range(len(top3)), [r["slug"] for r in top3], fontsize=13.5)
ax.set_ylim(len(top3) - 0.4, -0.9)
ax.set_xlim(0, 80)
ax.set_xlabel("share of sentences with no citation marker (%)", fontsize=13)
fig.subplots_adjust(left=0.34, right=0.98, top=0.83, bottom=0.19)
head(fig, "Citation gaps",
     "Top 10 articles by share of prose sentences with no [n] citation marker.")
foot(fig, ["Broken source lists (counts unreliable): " + "; ".join(
    f"{r['slug']} lists {r['sources_listed']} sources but cites up to [{r['highest_marker']}]" for r in broken) + ".",
    "Rule-based sentence split, so shares are approximate."],
     "03_citation_gaps.png")

# ============================================================= 4. reader overlap
print("\n[4] Reader overlap: passages by how many readers flagged them")
by_n = Counter(int(p["n_reviewers"]) for p in p3)
same2 = sum(p["at_least_two_same_side"] == "True" for p in p3)
same3 = sum(p["all_three_same_side"] == "True" for p in p3)
two_only = [p for p in p3 if int(p["n_reviewers"]) == 2]
same_two_only = sum(p["at_least_two_same_side"] == "True" for p in two_only)
print(f"  passages {len(p3)}: one reader {by_n[1]}, two {by_n[2]}, three {by_n[3]}")
print(f"  same side: two-reader passages {same_two_only}/{by_n[2]}; all three {same3}/{by_n[3]}; "
      f"at least two same side {same2}")
fig, ax = plt.subplots(figsize=(W_IN, 7))
bars = [("One reader only", by_n[1], None), ("Two readers", by_n[2], same_two_only), ("All three readers", by_n[3], same3)]
for i, (lab, n, same) in enumerate(bars):
    ax.barh(i, n, height=0.6, color="#D0D7DE", zorder=2)
    if same is not None:
        ax.barh(i, same, height=0.6, color="#57606A", zorder=3)
        txt = f"{n}   ({same} gave it the same side)"
    else:
        txt = f"{n}"
    ax.text(n + 1.2, i, txt, va="center", fontsize=14, color=INK)
ax.set_yticks(range(3), [b[0] for b in bars], fontsize=15)
ax.set_ylim(2.5, -0.5)
ax.set_xlim(0, max(by_n.values()) * 1.45)
ax.set_xlabel("flagged passages (overlapping quotes in the same article)", fontsize=13)
ax.legend(handles=[Patch(color="#57606A", label="same side from every reader who flagged it"),
                   Patch(color="#D0D7DE", label="all passages")], loc="lower right", frameon=False, fontsize=13)
fig.subplots_adjust(left=0.2, right=0.98, top=0.78, bottom=0.22)
for k, name in enumerate(REV):
    fig_robot(fig, 0.80 + k * 0.05, 0.885, 0.06, BOTS[name])
    fig.text(0.80 + k * 0.05 + 0.0135, 0.865, f"R{k + 1}", ha="center", va="top", fontsize=11, color=MUTED)
head(fig, "How often the readers flagged the same passage",
     f"{len(p3)} passages flagged by at least one of three AI readers.")
foot(fig, ["Overlap shows consistency of separate reads, not that a flag is right; it may be inflated "
           "because later readers' instructions mentioned earlier results."],
     "04_reader_overlap.png")
