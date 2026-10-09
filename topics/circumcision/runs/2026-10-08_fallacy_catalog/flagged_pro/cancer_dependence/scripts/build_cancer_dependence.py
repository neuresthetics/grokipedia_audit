#!/usr/bin/env python3
"""Build the cancer dependence tags (work/tags.csv from cancer_queue.py) and the combined what-if count.

    python3 .../flagged_pro/cancer_dependence/scripts/build_cancer_dependence.py            needs every item tagged
    python3 .../flagged_pro/cancer_dependence/scripts/build_cancer_dependence.py --partial  progress only

What-if count: C = the point rests on a cancer-prevention claim. A tag means "depends on the claim", not a finding
that the claim is wrong. Combined with the HIV/STI tags (../sti_dependence/tags.csv): medical arguments resting on
HIV/STI or cancer = H + (C and not H). Writes cancer_dependence/tags.csv, summary.json, CANCER_DEPENDENCE.md.
Example quotes: fixed rule (per type: 120-260 characters, three different articles, earliest in article order),
checked verbatim against the 2026-10-01 snapshots. Keyword cross-check: does the sentence itself name cancer?
Deterministic.
"""
import collections, csv, json, pathlib, re, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
CD = HERE.parent
FP = CD.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
TYPES = [("C", "Rests on the cancer-prevention claim"), ("K", "Rests on a non-cancer claim"),
         ("N", "Mentions cancer, not relied on as a benefit")]
KW = re.compile(r"cancer|carcinom|malignan|tumou?r|neoplas", re.I)


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)


def num(s):
    return int(s[1:])


def main():
    partial = "--partial" in sys.argv
    Q = rd(CD / "work" / "queue.csv")
    T = {r["item"]: r for r in rd(CD / "work" / "tags.csv")} if (CD / "work" / "tags.csv").exists() else {}
    left = [q["item"] for q in Q if q["item"] not in T]
    if left and not partial:
        sys.exit(f"{len(left)} of {len(Q)} items not tagged yet (first {left[:3]}); use --partial for progress")
    if partial:
        print(f"tagged {len(T)}/{len(Q)}"); return
    H = {(r["article"], r["sentence_id"]): r["tag"] for r in rd(FP / "sti_dependence" / "tags.csv")}
    n_med = len(H)
    n_surv = sum(1 for r in rd(FP / "topic_tags" / "tags.csv"))
    S = {(r["article"], r["sentence_id"]): r for r in rd(RUN / "survival" / "survival_scores.csv")}
    snaps, titles, rows = {}, {}, []
    for q in Q:
        k = (q["article"], q["sentence_id"])
        assert k in H, k
        if k[0] not in snaps:
            snaps[k[0]] = (SNAP / k[0] / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
            titles[k[0]] = re.search(r"^Title:\s*(.*)$", snaps[k[0]], re.M).group(1).strip()
        t = T[q["item"]]
        rows.append(dict(item=q["item"], article=k[0], sentence_id=k[1], tag=t["tag"], sti_tag=H[k],
                         keyword_names_cancer="yes" if KW.search(S[k]["text"]) else "no", note=t["note"],
                         tagged_by=t["tagged_by"], text=S[k]["text"]))
    wr(CD / "tags.csv", rows, list(rows[0]))
    n = len(rows)
    c = collections.Counter(r["tag"] for r in rows)
    c_and_h = sum(r["tag"] == "C" and r["sti_tag"] == "H" for r in rows)
    c_not_h = c["C"] - c_and_h
    h = sum(v == "H" for v in H.values())
    comb = h + c_not_h
    kw_yes = sum(r["keyword_names_cancer"] == "yes" for r in rows)
    match = sum((r["keyword_names_cancer"] == "yes") == (r["tag"] == "C") for r in rows)
    Sm = dict(scope="medical (M) surviving male pro arguments, prefiltered to a cancer/HPV/cervical keyword in the "
                    "sentence or the two sentences on either side", what_if=True,
              medical_sentences=n_med, surviving_pro_sentences=n_surv, prefiltered=n,
              prefiltered_self_keyword=kw_yes,
              by_type={t: dict(name=nm, count=c[t], share_of_prefiltered=round(c[t] / n, 6)) for t, nm in TYPES},
              C_and_H=c_and_h, C_not_H=c_not_h, H=h,
              hiv_sti_or_cancer=comb, hiv_sti_or_cancer_share_of_medical=round(comb / n_med, 6),
              hiv_sti_or_cancer_share_of_surviving_pro=round(comb / n_surv, 6),
              remaining_medical=n_med - comb,
              keyword_matched_model=round(match / n, 6), keyword_matched_count=match,
              tagged_by=dict(collections.Counter(r["tagged_by"] for r in rows)), by_tagger={}, top_articles=[],
              examples={})
    for who in sorted({r["tagged_by"] for r in rows}):
        its = [r["item"] for r in rows if r["tagged_by"] == who]
        cc = collections.Counter(r["tag"] for r in rows if r["tagged_by"] == who)
        Sm["by_tagger"][who] = dict(range=f"{min(its)}-{max(its)}", sentences=len(its), counts={t: cc[t] for t, _ in TYPES})
    art = collections.defaultdict(collections.Counter)
    for r in rows:
        art[r["article"]][r["tag"]] += 1
    for a, cc in sorted(art.items(), key=lambda x: (-x[1]["C"], -sum(x[1].values()), x[0]))[:8]:
        Sm["top_articles"].append(dict(article=a, title=titles[a], prefiltered=sum(cc.values()),
                                       counts={t: cc[t] for t, _ in TYPES}))
    for t, _ in TYPES:
        ex, used = [], set()
        for r in sorted([r for r in rows if r["tag"] == t], key=lambda r: (r["article"], num(r["sentence_id"]))):
            if 120 <= len(r["text"]) <= 260 and r["article"] not in used:
                assert r["text"] in snaps[r["article"]], f"not verbatim: {r['article']} {r['sentence_id']}"
                ex.append(dict(article=r["article"], sentence_id=r["sentence_id"], text=r["text"], note=r["note"]))
                used.add(r["article"])
            if len(ex) == 3:
                break
        Sm["examples"][t] = ex
    json.dump(Sm, open(CD / "summary.json", "w"), indent=1, ensure_ascii=False)
    write_md(Sm)
    print(json.dumps({t: c[t] for t, _ in TYPES}), f"C and H {c_and_h}; C not H {c_not_h}; H {h}; combined {comb} "
          f"= {100 * comb / n_med:.1f}% of {n_med} medical, {100 * comb / n_surv:.1f}% of {n_surv} surviving pro; "
          f"keyword matched {100 * match / n:.1f}%")


def write_md(Sm):
    n = Sm["prefiltered"]
    pc = lambda a, b: f"{100 * a / b:.1f}%"
    L = ["# Which medical arguments rest on the cancer-prevention claim? (what-if count)", "",
         "Male circumcision articles only. This is the second what-if pass on the medical surviving pro arguments, "
         "after the HIV/STI pass ([../sti_dependence/STI_DEPENDENCE.md](../sti_dependence/STI_DEPENDENCE.md)). "
         "Instructions: [CANCER_PROMPT.md](CANCER_PROMPT.md).", "",
         "**This is a what-if count, not a finding.** Some critics say cancer prevention is not a valid reason for "
         "circumcision. A tag of C means only that an argument depends on the cancer-prevention claim, not that the "
         "claim is wrong. Penile cancer is rare in absolute terms, but how much a rare benefit should weigh is a "
         "question this audit does not settle.", "",
         "Read this with the limits in mind:", "",
         f"- **AI-tagged, not by a person**: {len(Sm['by_tagger'])} separate AI model sessions, one per range of the queue.",
         "- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.",
         "- **One tag per sentence.** A sentence that names cancer and another benefit is tagged C only if no point is "
         "left without the cancer part.",
         f"- **Prefilter.** Only the {n} of {Sm['medical_sentences']} medical sentences whose own text or the two prose "
         "sentences on either side name cancer, carcinoma, malignancy, tumour, neoplasia, HPV, papillomavirus or "
         "cervical were tagged. Recall limit: a sentence that relies on cancer through \"these benefits\" is caught "
         "only if a keyword sits inside that window; the rest of the medical sentences count as not resting on cancer.", "",
         "## Counts", "", "| Tag | Meaning | Sentences | Share of the prefiltered |", "|---|---|---|---|"]
    for t, d in Sm["by_type"].items():
        L.append(f"| **{t}** | {d['name']} | {d['count']} | {pc(d['count'], n)} |")
    m, s = Sm["medical_sentences"], Sm["surviving_pro_sentences"]
    L += ["", "## Combined with the HIV/STI pass", "",
          f"- C sentences also tagged H (HIV/STI): **{Sm['C_and_H']}**. C but not H: **{Sm['C_not_H']}**.",
          f"- Medical arguments resting on the HIV/STI claim or the cancer claim: H {Sm['H']} + cancer only "
          f"{Sm['C_not_H']} = **{Sm['hiv_sti_or_cancer']}**, which is {pc(Sm['hiv_sti_or_cancer'], m)} of the {m} "
          f"medical arguments and {pc(Sm['hiv_sti_or_cancer'], s)} of all {s} surviving pro arguments.",
          f"- Remaining medical arguments: {Sm['remaining_medical']} ({pc(Sm['remaining_medical'], m)} of {m}).", "",
          "Again: these counts say which arguments depend on those claims, not that the claims are wrong.", "",
          f"**Keyword cross-check** (a regex, no model): {Sm['prefiltered_self_keyword']} of the {n} prefiltered "
          "sentences name cancer themselves. Whether a sentence names cancer matched whether the model tagged it C "
          f"for {100 * Sm['keyword_matched_model']:.1f}% of them. It is a rough cross-check only.", "",
          "## Top articles (by C)", "", "| Article | Prefiltered | C | K | N |", "|---|---|---|---|---|"]
    for a in Sm["top_articles"]:
        cc = a["counts"]
        L.append(f"| {a['title']} (`{a['article']}`) | {a['prefiltered']} | {cc['C']} | {cc['K']} | {cc['N']} |")
    L += ["", "## By tagger", "", "| Tagger | Range | Sentences | C | K | N |", "|---|---|---|---|---|---|"]
    for who, d in Sm["by_tagger"].items():
        cc = d["counts"]
        L.append(f"| {who} | {d['range']} | {d['sentences']} | " +
                 " | ".join(f"{cc[t]} ({100 * cc[t] / d['sentences']:.0f}%)" for t in "CKN") + " |")
    L += [""]
    for t, d in Sm["by_type"].items():
        L += [f"## {t}: {d['name']}", "", "Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked "
              "by a fixed rule: 120-260 characters, three different articles, earliest in article order):", ""]
        for e in Sm["examples"][t]:
            L += [f"> {e['text']}", ">", f"> `{e['article']}` {e['sentence_id']}" +
                  (f" · tagger's note: {e['note']}" if e["note"] else ""), ""]
    L += ["## Files", "",
          "- [tags.csv](tags.csv): every prefiltered sentence with its tag, its HIV/STI tag, the keyword check, the "
          "tagger's note and the text.",
          "- [summary.json](summary.json), [CANCER_PROMPT.md](CANCER_PROMPT.md), [work/queue.csv](work/queue.csv), "
          "[work/tags.csv](work/tags.csv).",
          "- Scripts: [cancer_queue.py](scripts/cancer_queue.py), [build_cancer_dependence.py](scripts/build_cancer_dependence.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/10_what_if_removed.png`.", ""]
    (CD / "CANCER_DEPENDENCE.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
