#!/usr/bin/env python3
"""Build the topic tags of the surviving male pro arguments (work/tags.csv from tag_queue.py).

    python3 .../flagged_pro/topic_tags/scripts/build_topic_tags.py            needs every item tagged
    python3 .../flagged_pro/topic_tags/scripts/build_topic_tags.py --partial  progress only, writes nothing

Writes topic_tags/tags.csv, topic_tags/summary.json, topic_tags/TAGS.md. Example quotes are picked by a fixed
rule (per type: sentences of 120-260 characters, two different articles, earliest in article order) and
checked verbatim against the 2026-10-01 snapshots. Also runs a keyword ballpark (regex, no model) as a
cross-check of the model tags. Deterministic.
"""
import collections, csv, json, pathlib, re, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
TT = HERE.parent
FP = TT.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
TYPES = [("M", "Medical or scientific data"), ("E", "Ethics, rights or law"),
         ("R", "Religion, culture or tradition"), ("O", "Other, mixed or framing")]

# Keyword ballpark: count pattern hits per type; the most hits wins; no hits or a tie -> O.
KW = {
    "M": r"\b(HIV|STI|UTI|infection|trial|RCT|randomi[sz]ed|meta-analys|systematic review|risk|rate|incidence|"
         r"prevalence|complication|cancer|HPV|herpes|syphilis|mechanism|cells?|mucosa|keratin|sensitiv|"
         r"clinical|medical|health|efficacy|cost-effective|odds ratio|hazard|percent|%|WHO|CDC|AAP|anesthe|"
         r"analges|pain|hygiene|phimosis|balanitis|epidemiolog)",
    "E": r"\b(consent|autonom|rights?|ethic|law|legal|court|statut|ban|prohibit|parental|parents|best interests?|"
         r"bodily integrity|convention|UNCRC|policy|regulat|criminal|liberty|freedom|proxy|state intervention|"
         r"deontolog|utilitarian|moral)",
    "R": r"\b(relig|Jewish|Judaism|Muslim|Islam|covenant|brit|milah|mohel|khitan|sunnah|ritual|rite|tradition|"
         r"cultur|custom|ceremon|initiation|ulwaluko|Xhosa|ancestr|histor|ancient|identity|community|communal|"
         r"stigma|norm|heritage|sacred|God|Torah|Quran|hadith)",
}


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)


def num(s):
    return int(s[1:])


def kw_tag(text):
    hits = {t: len(re.findall(p, text, re.I)) for t, p in KW.items()}
    best = max(hits.values())
    top = [t for t, n in hits.items() if n == best]
    return "O" if best == 0 or len(top) > 1 else top[0]


def main():
    partial = "--partial" in sys.argv
    Q = rd(TT / "work" / "queue.csv")
    T = {r["item"]: r for r in rd(TT / "work" / "tags.csv")} if (TT / "work" / "tags.csv").exists() else {}
    left = [q["item"] for q in Q if q["item"] not in T]
    if left and not partial:
        sys.exit(f"{len(left)} of {len(Q)} items not tagged yet (first {left[:3]}); use --partial for progress")
    if partial:
        print(f"tagged {len(T)}/{len(Q)}; {dict(collections.Counter(r['tag'] for r in T.values()))}"); return
    p3 = {(r["article"], r["sentence_id"]): r["points_after_pass3"] for r in rd(FP / "recheck" / "points_by_pass.csv")}
    S = {(r["article"], r["sentence_id"]): r for r in rd(RUN / "survival" / "survival_scores.csv")}
    snaps, titles = {}, {}
    rows = []
    for q in Q:
        k = (q["article"], q["sentence_id"])
        assert p3[k] == "3" and S[k]["side"] == "pro" and S[k]["topic_group"] == "male", k
        if k[0] not in snaps:
            snaps[k[0]] = (SNAP / k[0] / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
            titles[k[0]] = re.search(r"^Title:\s*(.*)$", snaps[k[0]], re.M).group(1).strip()
        t = T[q["item"]]
        rows.append(dict(item=q["item"], article=k[0], sentence_id=k[1], tag=t["tag"], keyword_tag=kw_tag(S[k]["text"]),
                         note=t["note"], tagged_by=t["tagged_by"], text=S[k]["text"]))
    wr(TT / "tags.csv", rows, list(rows[0]))
    n = len(rows)
    c = collections.Counter(r["tag"] for r in rows)
    kc = collections.Counter(r["keyword_tag"] for r in rows)
    match = sum(r["tag"] == r["keyword_tag"] for r in rows)
    Sm = dict(scope="male circumcision pro argument sentences with all 3 points after pass 3", sentences=n,
              by_type={t: dict(name=nm, count=c[t], share=round(c[t] / n, 4)) for t, nm in TYPES},
              keyword_ballpark={t: kc[t] for t, _ in TYPES},
              keyword_same_as_model=round(match / n, 6), keyword_same_as_model_count=match,
              tagged_by=dict(collections.Counter(r["tagged_by"] for r in rows)), types={}, examples={},
              by_tagger={})
    for who in sorted({r["tagged_by"] for r in rows}):
        its = [r["item"] for r in rows if r["tagged_by"] == who]
        cc = collections.Counter(r["tag"] for r in rows if r["tagged_by"] == who)
        Sm["by_tagger"][who] = dict(range=f"{min(its)}-{max(its)}", sentences=len(its),
                                    counts={t: cc[t] for t, _ in TYPES})
    for t, _ in TYPES:
        art = collections.Counter(r["article"] for r in rows if r["tag"] == t)
        Sm["types"][t] = [dict(article=a, title=titles[a], count=m) for a, m in
                          sorted(art.items(), key=lambda x: (-x[1], x[0]))[:5]]
        ex, used = [], set()
        for r in sorted([r for r in rows if r["tag"] == t], key=lambda r: (r["article"], num(r["sentence_id"]))):
            if 120 <= len(r["text"]) <= 260 and r["article"] not in used:
                assert r["text"] in snaps[r["article"]], f"not verbatim: {r['article']} {r['sentence_id']}"
                ex.append(dict(article=r["article"], sentence_id=r["sentence_id"], text=r["text"]))
                used.add(r["article"])
            if len(ex) == 2:
                break
        Sm["examples"][t] = ex
    json.dump(Sm, open(TT / "summary.json", "w"), indent=1, ensure_ascii=False)
    write_md(Sm)
    print(json.dumps({t: (c[t], f"{100 * c[t] / n:.1f}%") for t, _ in TYPES}), "keyword", dict(kc),
          f"same as model {100 * match / n:.1f}%")


def write_md(Sm):
    n = Sm["sentences"]
    L = ["# What do the surviving pro arguments rely on?", "",
         f"Male circumcision articles only. The {n} pro argument sentences that kept all 3 points after step 6 pass 3 "
         "were each tagged with the one kind of support they rely on to make their point "
         "([TAG_PROMPT.md](TAG_PROMPT.md)). A tag says what an argument rests on, not whether it is right. Keeping "
         "3 points means no reviewer flagged it, not that it is proven true.", "",
         "Read this with the limits in mind:", "",
         f"- **Model-tagged, not by a person**: {len(Sm['by_tagger'])} separate AI model sessions, one per range of "
         "the queue.",
         "- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.",
         "- **One type per sentence**, so sentences that mix two kinds of support are forced into one type.",
         "- **Scope**: male circumcision pro arguments with all 3 points after pass 3 only. Anti arguments and pro "
         "arguments that lost points are not tagged.", "",
         "## Counts", "", "| Type | Sentences | Share |", "|---|---|---|"]
    for t, d in Sm["by_type"].items():
        L.append(f"| **{t}**: {d['name']} | {d['count']} | {100 * d['share']:.1f}% |")
    L += ["", f"**Keyword ballpark** (a regex count, no model; see the script): " +
          ", ".join(f"{t} {v}" for t, v in Sm["keyword_ballpark"].items()) +
          f". The keyword tag matched the model's tag for {100 * Sm['keyword_same_as_model']:.1f}% of sentences. "
          "It is a rough cross-check only.", "",
          "## By tagger", "", "| Tagger | Range | Sentences | M | E | R | O |", "|---|---|---|---|---|---|---|"]
    for who, d in Sm["by_tagger"].items():
        c = d["counts"]
        L.append(f"| {who} | {d['range']} | {d['sentences']} | " + " | ".join(
            f"{c[t]} ({100 * c[t] / d['sentences']:.0f}%)" for t in "MERO") + " |")
    L += ["", "Ranges follow article order, so they cover different articles; differences between taggers mix "
          "article content with tagger habits.", ""]
    for t, d in Sm["by_type"].items():
        L += [f"## {t}: {d['name']}", "", "Articles with the most sentences of this type:", ""]
        for a in Sm["types"][t]:
            L.append(f"- {a['title']} (`{a['article']}`): {a['count']}")
        L += ["", "Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: "
              "120-260 characters, two different articles, earliest in article order):", ""]
        for e in Sm["examples"][t]:
            L += [f"> {e['text']}", ">", f"> `{e['article']}` {e['sentence_id']}", ""]
    L += ["## Files", "",
          "- [tags.csv](tags.csv): every sentence with its tag, the keyword tag, the tagger's note and the text.",
          "- [summary.json](summary.json), [TAG_PROMPT.md](TAG_PROMPT.md), [work/queue.csv](work/queue.csv), "
          "[work/tags.csv](work/tags.csv).",
          "- Scripts: [tag_queue.py](scripts/tag_queue.py), [build_topic_tags.py](scripts/build_topic_tags.py).",
          "- Chart: `docs/img/circumcision/2026-10-08/08_what_survivors_rely_on.png`.", ""]
    (TT / "TAGS.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
