#!/usr/bin/env python3
"""Draw the three run charts (light style). Usage: charts.py DATA_DIR OUT_DIR"""
import csv, sys, os, collections, statistics as st
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
data, out = sys.argv[1:3]; os.makedirs(out, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white"})
log = list(csv.DictReader(open(os.path.join(data, "claim_log.csv"), encoding="utf-8")))
order = ["supported", "partly supported", "unsupported", "miscited", "unverifiable", "uncited"]
def short(v): return v.split(" (")[0]
a = collections.Counter(short(r["verdict"]) for r in log); b = collections.Counter(short(r["verdict_vs_intended"]) for r in log)
fig, ax = plt.subplots(figsize=(8, 4)); x = range(len(order)); wd = 0.38
ax.bar([i - wd/2 for i in x], [a[o] for o in order], wd, label="as linked", color="#9bb7d4")
ax.bar([i + wd/2 for i in x], [b[o] for o in order], wd, label="vs. intended source (drift corrected)", color="#e0b27a")
for i, o in enumerate(order):
    ax.text(i - wd/2, a[o] + 2, a[o], ha="center", fontsize=8); ax.text(i + wd/2, b[o] + 2, b[o], ha="center", fontsize=8)
ax.set_xticks(list(x)); ax.set_xticklabels(order); ax.set_ylabel("sentences (of 401)")
ax.set_title("Spinoza article, 2026-10-15: verdict per sentence"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(os.path.join(out, "verdicts_linked_vs_intended.png"), dpi=130); plt.close(fig)
rows = list(csv.DictReader(open(os.path.join(data, "offset_fulltext.csv"), encoding="utf-8")))
B = collections.defaultdict(list)
for r in rows: B[int(r["block"])].append(r)
blocks = sorted(B); fig, ax = plt.subplots(figsize=(8, 4))
for k, c in (("0", "#9bb7d4"), ("-1", "#7fb77e"), ("-10", "#e0b27a")):
    ys = [st.mean([float(r[f"share_k{k}"]) for r in B[bk] if r[f"share_k{k}"]] or [float("nan")]) for bk in blocks]
    ax.plot(blocks, ys, marker="o", color=c, label=f"list entry n{'' if k == '0' else k}" + (" (as linked)" if k == "0" else ""))
ax.axvline(85.5, color="#bbbbbb", ls="--", lw=1); ax.text(87, 0.05, "inline 91+", fontsize=8, color="#777777")
ax.set_xticks(blocks); ax.set_xticklabels([f"{bk}-{bk+9}" for bk in blocks], rotation=45, fontsize=8)
ax.set_ylabel("mean share of sentence words\nfound in fetched source"); ax.set_xlabel("inline citation number (blocks of 10)")
ax.set_title("Which list entry best matches each inline cite"); ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(out, "offset_probe_by_block.png"), dpi=130); plt.close(fig)
c = collections.Counter(r["primary_text_check"] or "not an Ethics claim" for r in log)
labs = ["primary-text-match", "primary-text-mismatch", "no primary text on hand"]
fig, ax = plt.subplots(figsize=(7.5, 3.2)); ax.barh(labs[::-1], [c[l] for l in labs[::-1]], color="#9bb7d4")
for i, l in enumerate(labs[::-1]): ax.text(c[l] + 1, i, c[l], va="center", fontsize=8)
ax.set_xlabel("sentences"); ax.set_xlim(0, max(c[l] for l in labs) * 1.15); ax.set_title("Claims checked against the pinned Elwes Ethics text", loc="left")
fig.tight_layout(); fig.savefig(os.path.join(out, "primary_text_check.png"), dpi=130); plt.close(fig)
print("ok", dict(c))
