#!/usr/bin/env python3
"""Build the HIV/STI dependence tags (work/tags.csv from sti_queue.py).

    python3 .../flagged_pro/sti_dependence/scripts/build_sti_dependence.py            needs every item tagged
    python3 .../flagged_pro/sti_dependence/scripts/build_sti_dependence.py --partial  progress only, writes nothing

What-if count: H = the medical point rests on HIV/STI protection. A tag is not a finding that the claim is true.
Writes sti_dependence/tags.csv, summary.json, STI_DEPENDENCE.md. Example quotes are picked by a fixed rule
(per type: 120-260 characters, three different articles, earliest in article order) and checked verbatim against
the 2026-10-01 snapshots. Also runs a keyword cross-check (regex, no model): does the sentence name HIV or an STI?
Deterministic.
"""
import collections, csv, json, pathlib, re, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
SD = HERE.parent
FP = SD.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
TYPES = [("H", "Rests on the HIV/STI protection claim"), ("X", "Rests on a non-STI medical claim"),
         ("N", "Medical in form, no benefit claim relied on")]
KW = re.compile(r"\b(HIV|AIDS|STIs?|STDs?|HPV|herpes|HSV|syphilis|gonorrh|chlamydia|trichomon|chancroid|"
                r"sexually transmitted|papillomavirus|genital ulcer|VMMC|seroconver|antiretroviral)", re.I)


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
    Q = rd(SD / "work" / "queue.csv")
    T = {r["item"]: r for r in rd(SD / "work" / "tags.csv")} if (SD / "work" / "tags.csv").exists() else {}
    left = [q["item"] for q in Q if q["item"] not in T]
    if left and not partial:
        sys.exit(f"{len(left)} of {len(Q)} items not tagged yet (first {left[:3]}); use --partial for progress")
    if partial:
        print(f"tagged {len(T)}/{len(Q)}"); return
    m_tags = {(r["article"], r["sentence_id"]) for r in rd(FP / "topic_tags" / "tags.csv") if r["tag"] == "M"}
    S = {(r["article"], r["sentence_id"]): r for r in rd(RUN / "survival" / "survival_scores.csv")}
    snaps, titles, rows = {}, {}, []
    for q in Q:
        k = (q["article"], q["sentence_id"])
        assert k in m_tags, k
        if k[0] not in snaps:
            snaps[k[0]] = (SNAP / k[0] / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
            titles[k[0]] = re.search(r"^Title:\s*(.*)$", snaps[k[0]], re.M).group(1).strip()
        t = T[q["item"]]
        kw = bool(KW.search(S[k]["text"]))
        rows.append(dict(item=q["item"], article=k[0], sentence_id=k[1], tag=t["tag"],
                         keyword_names_hiv_sti="yes" if kw else "no", note=t["note"], tagged_by=t["tagged_by"],
                         text=S[k]["text"]))
    wr(SD / "tags.csv", rows, list(rows[0]))
    n = len(rows)
    c = collections.Counter(r["tag"] for r in rows)
    kw_yes = sum(r["keyword_names_hiv_sti"] == "yes" for r in rows)
    match = sum((r["keyword_names_hiv_sti"] == "yes") == (r["tag"] == "H") for r in rows)
    Sm = dict(scope="sentences tagged M (medical or scientific data) in topic_tags: male circumcision pro arguments "
                    "with all 3 points after pass 3", sentences=n, what_if=True,
              by_type={t: dict(name=nm, count=c[t], share=round(c[t] / n, 6)) for t, nm in TYPES},
              keyword_names_hiv_sti=kw_yes, keyword_matched_model=round(match / n, 6), keyword_matched_count=match,
              keyword_yes_but_not_H=sum(r["keyword_names_hiv_sti"] == "yes" and r["tag"] != "H" for r in rows),
              keyword_no_but_H=sum(r["keyword_names_hiv_sti"] == "no" and r["tag"] == "H" for r in rows),
              tagged_by=dict(collections.Counter(r["tagged_by"] for r in rows)), by_tagger={}, top_articles=[],
              examples={})
    for who in sorted({r["tagged_by"] for r in rows}):
        its = [r["item"] for r in rows if r["tagged_by"] == who]
        cc = collections.Counter(r["tag"] for r in rows if r["tagged_by"] == who)
        Sm["by_tagger"][who] = dict(range=f"{min(its)}-{max(its)}", sentences=len(its), counts={t: cc[t] for t, _ in TYPES})
    art = collections.defaultdict(collections.Counter)
    for r in rows:
        art[r["article"]][r["tag"]] += 1
    for a, cc in sorted(art.items(), key=lambda x: (-sum(x[1].values()), x[0]))[:8]:
        Sm["top_articles"].append(dict(article=a, title=titles[a], medical=sum(cc.values()),
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
    json.dump(Sm, open(SD / "summary.json", "w"), indent=1, ensure_ascii=False)
    write_md(Sm)
    print(json.dumps({t: (c[t], f"{100 * c[t] / n:.1f}%") for t, _ in TYPES}),
          f"keyword names HIV/STI {kw_yes}; matched model {100 * match / n:.1f}%")


def write_md(Sm):
    n = Sm["sentences"]
    h = Sm["by_type"]["H"]
    L = ["# Which medical arguments rest on the HIV/STI claim? (what-if count)", "",
         f"Male circumcision articles only. The {n} pro argument sentences that kept all 3 points after pass 3 and "
         "were tagged as relying on medical or scientific data were each tagged again: does the medical point rest on "
         "protection against HIV or another sexually transmitted infection? ([SIDEIDEA_PROMPT.md](SIDEIDEA_PROMPT.md))", "",
         "**This is a what-if count, not a finding.** Some critics say circumcision gives no protection against HIV "
         f"or other STIs. If that claim were set aside, the {h['count']} arguments tagged H would lose their medical "
         "point. A tag of H says only that an argument depends on the HIV/STI claim. It is not a finding that the claim "
         "is true or false; this audit has not checked it.", "",
         "Read this with the limits in mind:", "",
         f"- **AI-tagged, not by a person**: {len(Sm['by_tagger'])} separate AI model sessions, one per range of the queue.",
         "- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.",
         "- **One tag per sentence.** A sentence that names HIV and another medical benefit is tagged H only if no "
         "medical point is left without the HIV/STI part.",
         "- **Scope**: medical pro arguments with all 3 points after pass 3 only.", "",
         "## Counts", "", "| Tag | Meaning | Sentences | Share |", "|---|---|---|---|"]
    for t, d in Sm["by_type"].items():
        L.append(f"| **{t}** | {d['name']} | {d['count']} | {100 * d['share']:.1f}% |")
    L += ["", f"**Keyword cross-check** (a regex, no model): {Sm['keyword_names_hiv_sti']} sentences name HIV or an "
          f"STI. Whether a sentence names HIV or an STI matched whether the model tagged it H for "
          f"{100 * Sm['keyword_matched_model']:.1f}% of sentences. {Sm['keyword_yes_but_not_H']} name HIV or an STI "
          f"but were not tagged H, and {Sm['keyword_no_but_H']} were tagged H without naming it (the notes in "
          "tags.csv give the taggers' reasons where they wrote one). It is a rough cross-check only.", "",
          "## Top articles", "", "| Article | Medical sentences | H | X | N | H share |", "|---|---|---|---|---|---|"]
    for a in Sm["top_articles"]:
        cc = a["counts"]
        L.append(f"| {a['title']} (`{a['article']}`) | {a['medical']} | {cc['H']} | {cc['X']} | {cc['N']} | "
                 f"{100 * cc['H'] / a['medical']:.0f}% |")
    L += ["", "## By tagger", "", "| Tagger | Range | Sentences | H | X | N |", "|---|---|---|---|---|---|"]
    for who, d in Sm["by_tagger"].items():
        cc = d["counts"]
        L.append(f"| {who} | {d['range']} | {d['sentences']} | " +
                 " | ".join(f"{cc[t]} ({100 * cc[t] / d['sentences']:.0f}%)" for t in "HXN") + " |")
    L += ["", "Ranges follow article order, so differences between taggers mix article content with tagger habits.", ""]
    for t, d in Sm["by_type"].items():
        L += [f"## {t}: {d['name']}", "", "Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked "
              "by a fixed rule: 120-260 characters, three different articles, earliest in article order):", ""]
        for e in Sm["examples"][t]:
            L += [f"> {e['text']}", ">", f"> `{e['article']}` {e['sentence_id']}" +
                  (f" · tagger's note: {e['note']}" if e["note"] else ""), ""]
    L += ["## Files", "",
          "- [tags.csv](tags.csv): every sentence with its tag, the keyword check, the tagger's note and the text.",
          "- [summary.json](summary.json), [SIDEIDEA_PROMPT.md](SIDEIDEA_PROMPT.md), [work/queue.csv](work/queue.csv), "
          "[work/tags.csv](work/tags.csv).",
          "- Scripts: [sti_queue.py](scripts/sti_queue.py), [build_sti_dependence.py](scripts/build_sti_dependence.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/09_sti_dependence.png`.", ""]
    (SD / "STI_DEPENDENCE.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
