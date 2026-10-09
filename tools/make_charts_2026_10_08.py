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

Chart 5 (what survived) also reads runs/2026-10-08_fallacy_catalog/survival/survival_scores.csv: one row per
argument sentence (pro or anti), with points_left = 3 minus the number of reviewers whose flag overlaps it
(built by survival/scripts/build_survival.py; method in survival/METHOD.md).

Chart 6 (flagged pro types) reads runs/2026-10-08_fallacy_catalog/flagged_pro/flagged_pro.csv: one row per pro
argument sentence in the male circumcision articles (FGM articles are not part of step 6) with fewer than 3 points
left, with its primary fallacy family (the catalog's own category;
built by flagged_pro/scripts/build_flagged_pro.py; method in flagged_pro/METHOD.md).

Writes PNGs to docs/img/circumcision/2026-10-08/ and prints every number it draws.
Every flag is an AI reader's judgment: a lead to check, not a verdict.
"""
import csv
import json
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

# ============================================================= 5. what survived
print("\n[5] What survived: argument sentences by points left (3 = no reviewer flagged it)")
surv = read("survival/survival_scores.csv")
LOST = {2: "#8C959F", 1: "#57606A", 0: "#1F2328"}
SG = [("Male circumcision articles", "male"), ("FGM articles", "FGM")]
sv = {}
for title, g in SG:
    for side in ("pro", "anti"):
        rows = [r for r in surv if r["topic_group"] == g and r["side"] == side]
        c = Counter(int(r["points_left"]) for r in rows)
        sv[g, side] = dict(n=len(rows), pts={k: c.get(k, 0) for k in (3, 2, 1, 0)})
        d = sv[g, side]
        print(f"  {title} {side}: {d['n']} arguments; points left 3/2/1/0 = "
              + "/".join(str(d["pts"][k]) for k in (3, 2, 1, 0)) + f"; untouched {100 * d['pts'][3] / d['n']:.1f}%")


def lost_pct(g, side):
    d = sv[g, side]
    return 100 * (d["n"] - d["pts"][3]) / d["n"]


fig, axes = plt.subplots(1, 2, figsize=(W_IN, 8.8))
for ax, (title, g) in zip(axes, SG):
    for i, side in enumerate(("pro", "anti")):
        d = sv[g, side]
        left = 0
        for k in (3, 2, 1, 0):
            w = 100 * d["pts"][k] / d["n"]
            if w:
                ax.barh(i, w, left=left, height=0.5, color=COLOR[side] if k == 3 else LOST[k], zorder=2)
            left += w
        ax.text(2, i, f"{100 * d['pts'][3] / d['n']:.1f}% kept all 3 points", va="center", ha="left",
                fontsize=14, fontweight="bold", color="white", zorder=3)
        ax.text(101.5, i, f"{lost_pct(g, side):.1f}%\nflagged", va="center", ha="left", fontsize=13,
                fontweight="bold", color=INK, linespacing=1.1)
        ax.text(0, i + 0.42, f"{d['n']:,} {side} arguments:  {d['pts'][3]:,} kept 3  ·  {d['pts'][2]} kept 2  ·  "
                f"{d['pts'][1]} kept 1  ·  {d['pts'][0]} kept 0", va="center", ha="left", fontsize=12, color=MUTED)
    ax.set_yticks([0, 1], ["Pro", "Anti"], fontsize=15)
    for t, side in zip(ax.get_yticklabels(), ("pro", "anti")):
        t.set_color(COLOR[side]); t.set_fontweight("bold")
    ax.set_ylim(1.75, -0.55)
    ax.set_xlim(0, 115)
    ax.set_xticks(range(0, 101, 25), [f"{v}%" for v in range(0, 101, 25)])
    ax.set_title(f"{title}\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
    ax.text(0, 1.0, f"{sum(sv[g, s]['n'] for s in ('pro', 'anti')):,} argument sentences",
            transform=ax.transAxes, va="bottom", fontsize=13, color=MUTED)
    ax.set_xlabel("share of that side's argument sentences", fontsize=13)
    ax.spines["bottom"].set_color(SOFT)
fig.subplots_adjust(left=0.08, right=0.97, top=0.68, bottom=0.24, wspace=0.18)
fig.legend(handles=[Patch(color=COLOR["pro"], label="3 points left (pro)"),
                    Patch(color=COLOR["anti"], label="3 points left (anti)"),
                    Patch(color=LOST[2], label="2 left"), Patch(color=LOST[1], label="1 left"),
                    Patch(color=LOST[0], label="0 left")],
           loc="upper left", bbox_to_anchor=(0.075, 0.835), ncol=5, frameon=False, fontsize=13.5,
           handlelength=1.4, columnspacing=2.0)
fig.text(0.735, 0.81, "−1 point per reader flag:", ha="right", va="center", fontsize=12.5, color=MUTED)
for k, name in enumerate(REV):
    fig_robot(fig, 0.742 + k * 0.032, 0.79, 0.042, BOTS[name])
lm, la = lost_pct("male", "pro"), lost_pct("male", "anti")
fm, fa = lost_pct("FGM", "pro"), lost_pct("FGM", "anti")
head(fig, "How much of each side's argument survived the fallacy check?",
     f"Male circumcision articles: {lm:.1f}% of pro arguments were flagged vs {la:.1f}% of anti. "
     f"FGM articles: close, {fm:.1f}% pro vs {fa:.1f}% anti.")
foot(fig, ["Each argument sentence starts with 3 points and loses 1 for each of three AI readers that flagged it. "
           "Kept 3 = not flagged, not proven true.",
           "Sides labeled by an AI model (9 separate sessions, split by article), not a person. "
           "Method and limits: topics/circumcision/runs/2026-10-08_fallacy_catalog/survival/METHOD.md"],
     "05_what_survived.png")


# ============================================================= 6. flagged pro arguments by type
print("\n[6] Flagged pro arguments by fallacy family (male circumcision articles only; primary family)")
fp = read("flagged_pro/flagged_pro.csv")
assert {r["topic_group"] for r in fp} == {"male"}, "step 6 covers male circumcision articles only"
FAMS = [("relevance", "Off-point reasons", "relevance"),
        ("presumption", "Unearned or clashing premises", "presumption"),
        ("weak_induction", "Thin or ill-fitting evidence", "weak induction"),
        ("statistics", "Stretched numbers", "statistical and probabilistic"),
        ("causal", "Shaky cause and effect", "causal")]
fcnt = Counter(r["primary_family"] for r in fp)
nfp = len(fp)
assert sum(fcnt.values()) == nfp
print(f"  {nfp} flagged pro sentences; " + ", ".join(f"{k} {fcnt.get(k, 0)}" for k, _, _ in FAMS))

fig, ax = plt.subplots(figsize=(W_IN, 8.4))
for i, (k, label, cat) in enumerate(FAMS):
    v = 100 * fcnt.get(k, 0) / nfp
    ax.barh(i, v, height=0.6, color=COLOR["pro"], zorder=2)
    ax.text(v + 0.8, i, f"{fcnt.get(k, 0)}  ({v:.0f}%)", va="center", ha="left", fontsize=15,
            fontweight="bold", color=INK)
ax.set_yticks(range(len(FAMS)), [f"{lab}\n" for _, lab, _ in FAMS], fontsize=15)
for i, (_, _, cat) in enumerate(FAMS):
    ax.text(-0.012, i + 0.2, f"catalog: {cat}", transform=ax.get_yaxis_transform(), ha="right", va="center",
            fontsize=11.5, color=MUTED)
ax.set_ylim(len(FAMS) - 0.4, -0.6)
ax.set_xlim(0, 60)
ax.set_xticks(range(0, 51, 10), [f"{v}%" for v in range(0, 51, 10)])
ax.set_title("Male circumcision articles\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
ax.text(0, 1.0, f"{nfp} flagged pro argument sentences, one family each", transform=ax.transAxes,
        va="bottom", fontsize=13, color=MUTED)
ax.set_xlabel("share of flagged pro arguments", fontsize=13)
ax.spines["bottom"].set_color(SOFT)
fig.subplots_adjust(left=0.25, right=0.95, top=0.70, bottom=0.23)
fig.text(0.04, 0.815, "Pro argument sentences flagged by at least one of three AI readers, sorted by the kind of "
         "flaw named.", ha="left", va="center", fontsize=12.5, color=MUTED)
for k, name in enumerate(REV):
    fig_robot(fig, 0.86 + k * 0.032, 0.795, 0.042, BOTS[name])
mr = 100 * fcnt["relevance"] / nfp
mp = 100 * fcnt["presumption"] / nfp
head(fig, "What kinds of flawed reasoning did the flagged pro arguments use?",
     f"Most often a reason that doesn't bear on the point ({mr:.0f}%), then unearned or clashing premises "
     f"({mp:.0f}%). Male circumcision articles only.")
foot(fig, ["Families are fallacy_catalog's own categories. Where reviewers named different families, the one named by "
           "the most reviewers counts. FGM articles are not part of this step.",
           "Sides labeled by an AI model, not a person. Method and limits: "
           "topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/METHOD.md"],
     "06_flagged_pro_types.png")


# ============================================================= 7. pro points left after the prior check
print("\n[7] Male pro points left before vs after the dependence-on-flagged-priors check (step 6, second layer)")
dep = json.load(open(RUN / "flagged_pro/dependency/summary.json"))
pb = {int(k): v for k, v in dep["male_pro_points_left_before"].items()}
pa = {int(k): v for k, v in dep["male_pro_points_left_after"].items()}
assert pb == sv["male", "pro"]["pts"], "before must match step 5"
assert sum(pa.values()) == sum(pb.values())
an = sv["male", "anti"]["pts"]
BARS = [("Pro, step 5", pb, "pro"), ("Pro, after prior check", pa, "pro"), ("Anti, not rechecked", an, "anti")]
rc_path = RUN / "flagged_pro/recheck/summary.json"
rc = json.load(open(rc_path)) if rc_path.exists() else None
if rc and rc["complete"]:  # pass 3: fresh recheck of the remaining pro arguments
    p3 = {int(k): v for k, v in rc["male_pro_points_left_after_pass3"].items()}
    assert {int(k): v for k, v in rc["male_pro_points_left_after_pass2"].items()} == pa
    BARS = [("Pro, step 5", pb, "pro"), ("Pro, after pass 2", pa, "pro"), ("Pro, after pass 3", p3, "pro"),
            ("Anti, not rechecked", an, "anti")]
for lab, d, _ in BARS:
    print(f"  {lab}: 3/2/1/0 = " + "/".join(str(d[k]) for k in (3, 2, 1, 0)))

fig, ax = plt.subplots(figsize=(W_IN, 8.4 if len(BARS) == 3 else 9.6))
for i, (lab, d, side) in enumerate(BARS):
    n = sum(d.values()); left = 0
    for k in (3, 2, 1, 0):
        w = 100 * d[k] / n
        if w:
            ax.barh(i, w, left=left, height=0.5, color=COLOR[side] if k == 3 else LOST[k], zorder=2)
        left += w
    ax.text(2, i, f"{100 * d[3] / n:.1f}% kept all 3 points", va="center", ha="left",
            fontsize=14, fontweight="bold", color="white", zorder=3)
    ax.text(101.5, i, f"{100 * (n - d[3]) / n:.1f}%\nbelow 3", va="center", ha="left", fontsize=13,
            fontweight="bold", color=INK, linespacing=1.1)
    ax.text(0, i + 0.42, f"{n:,} arguments:  {d[3]:,} kept 3  ·  {d[2]} kept 2  ·  {d[1]} kept 1  ·  {d[0]} kept 0",
            va="center", ha="left", fontsize=12, color=MUTED)
ax.set_yticks(range(len(BARS)), [b[0].replace(", ", ",\n") for b in BARS], fontsize=14)
for t, b in zip(ax.get_yticklabels(), BARS):
    t.set_color(COLOR[b[2]]); t.set_fontweight("bold")
ax.set_ylim(len(BARS) - 0.25, -0.55)
ax.set_xlim(0, 115)
ax.set_xticks(range(0, 101, 25), [f"{v}%" for v in range(0, 101, 25)])
ax.set_title("Male circumcision articles\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
sub7 = (f"{dep['survivors_dinged']} of {dep['survivors']} surviving pro arguments lost 1 point; none lost more"
        if len(BARS) == 3 else
        f"Pass 2: {dep['survivors_dinged']} lost a point for depending on a flagged argument. "
        f"Pass 3: {rc['sentences_dinged']} lost points in a fresh recheck of {rc['items']}")
ax.text(0, 1.0, sub7, transform=ax.transAxes, va="bottom", fontsize=13, color=MUTED)
ax.set_xlabel("share of that side's argument sentences", fontsize=13)
ax.spines["bottom"].set_color(SOFT)
fig.subplots_adjust(left=0.20, right=0.97, top=0.68, bottom=0.23)
fig.legend(handles=[Patch(color=COLOR["pro"], label="3 points left (pro)"),
                    Patch(color=COLOR["anti"], label="3 points left (anti)"),
                    Patch(color=LOST[2], label="2 left"), Patch(color=LOST[1], label="1 left"),
                    Patch(color=LOST[0], label="0 left")],
           loc="upper left", bbox_to_anchor=(0.075, 0.835), ncol=5, frameon=False, fontsize=13.5,
           handlelength=1.4, columnspacing=2.0)
if len(BARS) == 3:
    head(fig, "Did surviving pro arguments lean on the flagged ones?",
         f"A few did: {dep['survivors_dinged']} of {dep['survivors']} lost a point for building on a flagged "
         f"pro argument. Male circumcision articles only.")
    l1 = ("−1 point for each distinct flagged pro argument a survivor was judged to depend on (floor 0). "
          "Dependence judged by an AI model, not a person; flags are leads, not verdicts.")
else:
    s3 = 100 * p3[3] / sum(p3.values())
    head(fig, "Do the surviving pro arguments hold up?",
         f"After a dependence check (pass 2) and a fresh fallacy recheck (pass 3), {s3:.1f}% of pro arguments "
         f"keep all 3 points. Male circumcision articles only.")
    l1 = ("Pass 2: −1 per flagged pro argument a survivor depends on. Pass 3: −1 per catalog fallacy flagged in a "
          "fresh recheck (floor 0). AI model judgments, not a person's.")
foot(fig, [l1,
           ("Anti arguments were not rechecked (only 4 were flagged). " if len(BARS) == 3 else
            "Anti arguments were not rechecked (pro only, by design). ") + "Method and limits: "
           "topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/METHOD.md"],
     "07_pro_after_priors.png")


# ============================================================= 8. what the surviving pro arguments rely on
tt_path = RUN / "flagged_pro/topic_tags/summary.json"
if not tt_path.exists():
    print("\n[8] skipped: flagged_pro/topic_tags/summary.json not built yet (tags not all in)")
else:
    print("\n[8] What the surviving pro arguments rely on (male circumcision articles, all 3 points after pass 3)")
    tt = json.load(open(tt_path))
    TT_ROWS = [("M", "Medical or\nscientific data"), ("E", "Ethics, rights\nor law"),
               ("R", "Religion, culture\nor tradition"), ("O", "Other, mixed\nor framing")]
    ntt = tt["sentences"]
    for k, _ in TT_ROWS:
        d = tt["by_type"][k]
        print(f"  {k} {d['name']}: {d['count']} ({100 * d['share']:.1f}%)")

    def icon(fig, kind, x, y, h, color):
        """Small vector icon in figure coordinates, (x, y) lower left, h = height as a fraction of figure height."""
        W, H = fig.get_size_inches()
        a = fig.add_axes([x, y, h * H / W, h]); a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
        if kind == "M":    # medical cross
            a.add_patch(Rectangle((0.36, 0.08), 0.28, 0.84, color=color))
            a.add_patch(Rectangle((0.08, 0.36), 0.84, 0.28, color=color))
        elif kind == "E":  # scales
            lw = 3
            a.add_line(Line2D([0.5, 0.5], [0.1, 0.88], color=color, linewidth=lw))
            a.add_line(Line2D([0.12, 0.88], [0.78, 0.78], color=color, linewidth=lw))
            a.add_line(Line2D([0.3, 0.7], [0.08, 0.08], color=color, linewidth=lw))
            for cx in (0.18, 0.82):
                a.add_line(Line2D([cx, cx - 0.13], [0.78, 0.42], color=color, linewidth=1.5))
                a.add_line(Line2D([cx, cx + 0.13], [0.78, 0.42], color=color, linewidth=1.5))
                a.add_patch(FancyBboxPatch((cx - 0.16, 0.34), 0.32, 0.08, boxstyle="round,pad=0,rounding_size=0.04",
                                           color=color))
        elif kind == "R":  # open book
            a.add_patch(FancyBboxPatch((0.04, 0.18), 0.43, 0.62, boxstyle="round,pad=0,rounding_size=0.05", color=color))
            a.add_patch(FancyBboxPatch((0.53, 0.18), 0.43, 0.62, boxstyle="round,pad=0,rounding_size=0.05", color=color))
            for yy in (0.36, 0.5, 0.64):
                a.add_line(Line2D([0.12, 0.4], [yy, yy], color="white", linewidth=1.5))
                a.add_line(Line2D([0.6, 0.88], [yy, yy], color="white", linewidth=1.5))
        else:              # three dots
            for cx in (0.18, 0.5, 0.82):
                a.add_patch(Circle((cx, 0.5), 0.12, color=color))

    fig, ax = plt.subplots(figsize=(W_IN, 8.8))
    for i, (k, lab) in enumerate(TT_ROWS):
        d = tt["by_type"][k]
        v = 100 * d["share"]
        ax.barh(i, v, height=0.6, color=COLOR["pro"], zorder=2)
        ax.text(v + 0.8, i, f"{d['count']}  ({v:.0f}%)", va="center", ha="left", fontsize=15,
                fontweight="bold", color=INK)
    ax.set_yticks(range(len(TT_ROWS)), [lab for _, lab in TT_ROWS], fontsize=15)
    ax.set_ylim(len(TT_ROWS) - 0.4, -0.6)
    top = max(100 * tt["by_type"][k]["share"] for k, _ in TT_ROWS)
    xmax = min(100, 10 * (int(top // 10) + 2))
    ax.set_xlim(0, xmax)
    ax.set_xticks(range(0, xmax + 1, 10 if xmax <= 60 else 20), [f"{v}%" for v in range(0, xmax + 1, 10 if xmax <= 60 else 20)])
    ax.set_title("Male circumcision articles\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
    ax.text(0, 1.0, f"{ntt} pro argument sentences that kept all 3 points, one type each", transform=ax.transAxes,
            va="bottom", fontsize=13, color=MUTED)
    ax.set_xlabel("share of surviving pro arguments", fontsize=13)
    ax.spines["bottom"].set_color(SOFT)
    fig.subplots_adjust(left=0.25, right=0.95, top=0.71, bottom=0.26)
    pos = ax.get_position()
    ylo, yhi = ax.get_ylim()
    for i, (k, _) in enumerate(TT_ROWS):
        yc = pos.y0 + pos.height * (ylo - i) / (ylo - yhi)
        icon(fig, k, 0.085, yc - 0.03, 0.06, MUTED)
    m = tt["by_type"]["M"]
    rest = max(("E", "R", "O"), key=lambda k: tt["by_type"][k]["count"])
    head(fig, "What do the surviving pro arguments rely on?",
         f"Mostly medical data: {m['count']} of {ntt} ({100 * m['share']:.0f}%) rest on trial results, rates, risks or "
         f"mechanisms. Next: {tt['by_type'][rest]['name'].lower()} ({100 * tt['by_type'][rest]['share']:.0f}%)."
         if m["count"] == max(tt["by_type"][k]["count"] for k, _ in TT_ROWS) else
         f"Medical data: {m['count']} of {ntt} ({100 * m['share']:.0f}%). Male circumcision articles only.")
    foot(fig, ["Male circumcision pro arguments with all 3 points after pass 3 only. One type per sentence, so mixed "
               "sentences are forced into one type. A tag is not a judgment of truth.",
               f"Tagged by an AI model in {len(tt['by_tagger'])} separate sessions, not a person. Not blind: run from a "
               "conversation that already knew the earlier results.",
               f"Keyword ballpark (regex, no model) matched the model's tag for {100 * tt['keyword_same_as_model']:.0f}% "
               "of sentences. Method: topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/topic_tags/TAGS.md"],
         "08_what_survivors_rely_on.png")


# ============================================================= 9. HIV/STI dependence of the medical survivors (what-if)
sd_path = RUN / "flagged_pro/sti_dependence/summary.json"
if not sd_path.exists():
    print("\n[9] skipped: flagged_pro/sti_dependence/summary.json not built yet (tags not all in)")
else:
    print("\n[9] Medical surviving pro arguments: rest on the HIV/STI claim? (what-if count)")
    sd = json.load(open(sd_path))
    SD_ROWS = [("H", "Rests on the\nHIV/STI claim"), ("X", "Rests on another\nmedical claim"),
               ("N", "No benefit\nclaim relied on")]
    nsd = sd["sentences"]
    for k, _ in SD_ROWS:
        d = sd["by_type"][k]
        print(f"  {k}: {d['count']} ({100 * d['share']:.1f}%)")

    def icon9(fig, kind, x, y, h, color):
        W, H = fig.get_size_inches()
        a = fig.add_axes([x, y, h * H / W, h]); a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
        if kind == "H":    # virus: circle with spikes
            import math
            for j in range(8):
                ang = j * math.pi / 4
                a.add_line(Line2D([0.5 + 0.28 * math.cos(ang), 0.5 + 0.44 * math.cos(ang)],
                                  [0.5 + 0.28 * math.sin(ang), 0.5 + 0.44 * math.sin(ang)], color=color, linewidth=2.2))
                a.add_patch(Circle((0.5 + 0.46 * math.cos(ang), 0.5 + 0.46 * math.sin(ang)), 0.05, color=color))
            a.add_patch(Circle((0.5, 0.5), 0.29, color=color))
        elif kind == "X":  # medical cross
            a.add_patch(Rectangle((0.36, 0.08), 0.28, 0.84, color=color))
            a.add_patch(Rectangle((0.08, 0.36), 0.84, 0.28, color=color))
        else:              # page with lines
            a.add_patch(FancyBboxPatch((0.18, 0.06), 0.64, 0.88, boxstyle="round,pad=0,rounding_size=0.06", color=color))
            for yy in (0.28, 0.44, 0.6, 0.76):
                a.add_line(Line2D([0.3, 0.7], [yy, yy], color="white", linewidth=1.8))

    fig, ax = plt.subplots(figsize=(W_IN, 9.2))
    for i, (k, lab) in enumerate(SD_ROWS):
        d = sd["by_type"][k]
        v = 100 * d["share"]
        ax.barh(i, v, height=0.6, color=COLOR["pro"], zorder=2)
        ax.text(v + 0.8, i, f"{d['count']}  ({v:.0f}%)", va="center", ha="left", fontsize=15,
                fontweight="bold", color=INK)
    ax.set_yticks(range(len(SD_ROWS)), [lab for _, lab in SD_ROWS], fontsize=15)
    ax.set_ylim(len(SD_ROWS) - 0.4, -0.6)
    top9 = max(100 * sd["by_type"][k]["share"] for k, _ in SD_ROWS)
    xmax9 = min(100, 10 * (int(top9 // 10) + 2))
    st9 = 10 if xmax9 <= 60 else 20
    ax.set_xlim(0, xmax9)
    ax.set_xticks(range(0, xmax9 + 1, st9), [f"{v}%" for v in range(0, xmax9 + 1, st9)])
    ax.set_title("Male circumcision articles\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
    ax.text(0, 1.0, f"{nsd} medical pro arguments that kept all 3 points, one tag each", transform=ax.transAxes,
            va="bottom", fontsize=13, color=MUTED)
    ax.set_xlabel("share of medical surviving pro arguments", fontsize=13)
    ax.spines["bottom"].set_color(SOFT)
    fig.subplots_adjust(left=0.25, right=0.95, top=0.72, bottom=0.29)
    pos = ax.get_position()
    ylo, yhi = ax.get_ylim()
    for i, (k, _) in enumerate(SD_ROWS):
        yc = pos.y0 + pos.height * (ylo - i) / (ylo - yhi)
        icon9(fig, k, 0.085, yc - 0.03, 0.06, MUTED)
    hd = sd["by_type"]["H"]
    head(fig, "How many of the medical arguments rest on the HIV/STI claim?",
         f"What-if count: {hd['count']} of {nsd} ({100 * hd['share']:.0f}%) would lose their medical point if the "
         "HIV/STI claim were set aside. A tag is not a finding that the claim is true or false.")
    nses = len(sd["by_tagger"])
    foot(fig, [f"AI-tagged by {nses} session{'s' if nses != 1 else ''}, not a person. Not blind: run from a conversation "
               "that already knew the earlier results. What-if count, not a finding; this audit did not check the HIV/STI claim.",
               f"Keyword check (names HIV or an STI, regex, no model) matched the H tag for "
               f"{100 * sd['keyword_matched_model']:.0f}% of sentences.",
               "Method: topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/sti_dependence/STI_DEPENDENCE.md"],
         "09_sti_dependence.png")


# ============================================================= 10. what-if: medical arguments resting on HIV/STI or cancer
cd_path = RUN / "flagged_pro/cancer_dependence/summary.json"
if not cd_path.exists():
    print("\n[10] skipped: flagged_pro/cancer_dependence/summary.json not built yet (tags not all in)")
else:
    print("\n[10] What-if: medical surviving pro arguments resting on the HIV/STI or cancer claims")
    cdj = json.load(open(cd_path))
    nm = cdj["medical_sentences"]
    SEG = [("Rests on the HIV/STI claim", cdj["H"], COLOR["pro"]),
           ("Rests on the cancer claim only", cdj["C_not_H"], "#A86F00"),
           ("Remaining medical arguments", cdj["remaining_medical"], "#F5D9A0")]
    assert sum(v for _, v, _ in SEG) == nm
    for lab, v, _ in SEG:
        print(f"  {lab}: {v} ({100 * v / nm:.1f}%)")
    fig, ax = plt.subplots(figsize=(W_IN, 8.4))
    left = 0
    for i, (lab, v, col) in enumerate(SEG):
        w = 100 * v / nm
        ax.barh(0, w, left=left, height=0.5, color=col, zorder=2, edgecolor="white", linewidth=2)
        # label above (odd) or below (even) the bar, at the segment's middle, so narrow segments still read
        y = -0.42 if i != 1 else 0.42
        ax.text(left + w / 2, y, f"{lab}\n{v}  ({w:.0f}%)", ha="center", va="bottom" if i != 1 else "top",
                fontsize=14, fontweight="bold", color=INK, linespacing=1.3)
        left += w
    ax.set_yticks([])
    ax.set_ylim(1.0, -1.0)
    ax.set_xlim(0, 100)
    ax.set_xticks(range(0, 101, 25), [f"{v}%" for v in range(0, 101, 25)])
    ax.set_title("Male circumcision articles\n", loc="left", fontsize=17, fontweight="bold", color=INK, pad=4)
    ax.text(0, 1.0, f"{nm} medical pro arguments that kept all 3 points", transform=ax.transAxes, va="bottom",
            fontsize=13, color=MUTED)
    ax.set_xlabel("share of medical surviving pro arguments", fontsize=13)
    ax.spines["bottom"].set_color(SOFT)
    fig.subplots_adjust(left=0.06, right=0.95, top=0.70, bottom=0.27)
    comb = cdj["hiv_sti_or_cancer"]
    head(fig, "How many medical arguments rest on the HIV/STI or cancer claims?",
         f"What-if count: {comb} of {nm} ({100 * comb / nm:.0f}%) would lose their point if both claims were set aside. "
         "A tag is not a finding that a claim is wrong.")
    nses10 = len(set(json.load(open(RUN / "flagged_pro/sti_dependence/summary.json"))["by_tagger"])) + len(cdj["by_tagger"])
    foot(fig, [f"AI-tagged by {nses10} sessions in two passes (HIV/STI, then cancer), not a person. Not blind: run from a "
               "conversation that already knew the earlier results. What-if count, not a finding.",
               f"Cancer pass covers only the {cdj['prefiltered']} sentences with a cancer, HPV or cervical keyword within "
               "two sentences, so it may miss some. Cancer only = tagged cancer and not HIV/STI.",
               "Method: topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md"],
         "10_what_if_removed.png")


# ============================================================= 11. total what-if: how much of the pro side is left
wt_path = RUN / "flagged_pro/whatif_total/summary.json"
if not wt_path.exists():
    print("\n[11] skipped: flagged_pro/whatif_total/summary.json not built yet")
else:
    import math
    print("\n[11] Total what-if: if the three premises are true, how much of the male pro side is invalidated?")
    wt = json.load(open(wt_path))
    N11 = wt["pro_total"]
    g = {k: v["count"] for k, v in wt["groups"].items()}
    flagged, inval, left_n = g["already_flagged"], wt["invalidated_under_what_if"], wt["not_invalidated"]
    gone = flagged + inval
    assert gone + left_n == N11
    pg, pl = round(100 * gone / N11), round(100 * left_n / N11)
    print(f"  already flagged {flagged}, invalidated {inval}, together {gone} ({100 * gone / N11:.1f}%), "
          f"left {left_n} ({100 * left_n / N11:.1f}%)")
    LEFTC = "#C9DCEB"

    fig = plt.figure(figsize=(W_IN, 10.0))
    FW, FH = fig.get_size_inches()

    def icon11(kind, x, y, h, color):
        a = fig.add_axes([x, y, h * FH / FW, h]); a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
        if kind == "virus":
            for j in range(8):
                ang = j * math.pi / 4
                a.add_line(Line2D([0.5 + 0.28 * math.cos(ang), 0.5 + 0.44 * math.cos(ang)],
                                  [0.5 + 0.28 * math.sin(ang), 0.5 + 0.44 * math.sin(ang)], color=color, linewidth=2.2))
                a.add_patch(Circle((0.5 + 0.46 * math.cos(ang), 0.5 + 0.46 * math.sin(ang)), 0.05, color=color))
            a.add_patch(Circle((0.5, 0.5), 0.29, color=color))
        elif kind == "globe":
            a.add_patch(Circle((0.5, 0.5), 0.44, fill=False, ec=color, lw=2.4))
            a.add_line(Line2D([0.06, 0.94], [0.5, 0.5], color=color, lw=1.8))
            a.add_patch(matplotlib.patches.Ellipse((0.5, 0.5), 0.42, 0.88, fill=False, ec=color, lw=1.8))
        else:  # ribbon-free 'no' sign over a cross: cancer prevention not counted as a reason
            a.add_patch(Rectangle((0.38, 0.14), 0.24, 0.72, color=color))
            a.add_patch(Rectangle((0.14, 0.38), 0.72, 0.24, color=color))
            a.add_patch(Circle((0.5, 0.5), 0.46, fill=False, ec=COLOR["anti"], lw=2.6))
            a.add_line(Line2D([0.18, 0.82], [0.82, 0.18], color=COLOR["anti"], lw=2.6))

    head(fig, f"If these three things are true, {pg}% of the pro side is invalidated",
         f"All {N11} pro arguments in the Grokipedia male circumcision articles. Premises are assumed, not tested here.")

    # premises box
    bx, by, bw, bh = 0.04, 0.585, 0.92, 0.245
    fig.patches.append(FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0,rounding_size=0.012",
                                      transform=fig.transFigure, fc="#F6F8FA", ec=SOFT, lw=1.2, zorder=-5))
    fig.text(bx + 0.015, by + bh - 0.022, "IF THESE ARE TRUE", ha="left",
             va="top", fontsize=13, fontweight="bold", color=MUTED)
    PREM = [("virus", "1.  Circumcision does not protect against HIV or other STIs", ""),
            ("globe", "2.  STI rates are highest in circumcising countries",
             "adds no separate count beyond premise 1"),
            ("nocross", "3.  Cancer prevention is not a valid reason",
             "penile cancer is rare, and prevention-by-removal proves too much")]
    for k, (ic, txt, note) in enumerate(PREM):
        yy = by + bh - 0.085 - k * 0.062
        icon11(ic, bx + 0.02, yy - 0.022, 0.045, MUTED)
        fig.text(bx + 0.06, yy, txt, ha="left", va="center", fontsize=16, fontweight="bold", color=INK)
        if note:
            t = fig.text(bx + 0.06, yy, txt, ha="left", va="center", fontsize=16, fontweight="bold", alpha=0)
            ext = t.get_window_extent(renderer=fig.canvas.get_renderer())
            fig.text(fig.transFigure.inverted().transform((ext.x1, 0))[0] + 0.01, yy, f"({note})", ha="left",
                     va="center", fontsize=13.5, color=MUTED)

    # big numbers
    fig.text(0.04, 0.505, f"{pg}%", ha="left", va="top", fontsize=54, fontweight="bold", color=COLOR["pro"])
    fig.text(0.155, 0.478, f"invalidated or already flagged\n{gone} of {N11} pro arguments", ha="left",
             va="center", fontsize=15, color=INK, linespacing=1.35)
    fig.text(0.96, 0.505, f"{pl}%", ha="right", va="top", fontsize=54, fontweight="bold", color="#5B8DB8")
    fig.text(0.845, 0.478, f"left standing\n{left_n} of {N11}", ha="right", va="center", fontsize=15,
             color=INK, linespacing=1.35)

    # bar
    ax = fig.add_axes([0.04, 0.24, 0.92, 0.15])
    SEG = [(f"Already flagged\nby this audit", flagged, "#8A8A8A"),
           (f"Invalidated by the premises\n(rest on HIV/STI or cancer)", inval, COLOR["pro"]),
           ("Left standing\n(other medical, religion, ethics, other)", left_n, LEFTC)]
    x0 = 0
    for lab, v, col in SEG:
        w = 100 * v / N11
        ax.barh(0, w, left=x0, height=0.62, color=col, edgecolor="white", linewidth=2)
        ax.text(x0 + w / 2, 0, f"{v}", ha="center", va="center", fontsize=17, fontweight="bold",
                color="white" if col != LEFTC else INK)
        ax.text(x0 + w / 2, -0.45, f"{lab}  ·  {w:.0f}%", ha="center", va="top", fontsize=12.5, color=INK,
                linespacing=1.25)
        x0 += w
    ax.set_xlim(0, 100); ax.set_ylim(-1.35, 0.4); ax.axis("off")
    ax.plot([0.3, 0.3, 100 * gone / N11 - 0.3, 100 * gone / N11 - 0.3], [0.36, 0.42, 0.42, 0.36], color=COLOR["pro"],
            lw=2, clip_on=False)

    foot(fig, ["What-if layered on the audit: earlier results unchanged; each argument counted once (already flagged "
               "first, then HIV/STI, then cancer). AI-tagged, not a person. Not blind.",
               "Not a finding that the premises are true: premise 1 contradicts the trials the articles cite. "
               f"Non-medical arguments were not tagged for HIV/STI or cancer ({wt['non_medical_model_check']['Y']} of "
               f"{wt['non_medical_keyword_hits']} keyword hits rest on HIV; not added).",
               "Method: topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/whatif_total/TOTAL_WHATIF.md"],
         "11_pro_side_invalidated.png")
