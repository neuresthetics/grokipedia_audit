#!/usr/bin/env python3
"""Resumable queue for tagging what each surviving male pro argument relies on (M / E / R / O).
Instructions for the tagger: ../TAG_PROMPT.md.

  python3 tag_queue.py init                          write ../work/queue.csv (deterministic; run once)
  python3 tag_queue.py status                        progress and tag counts so far
  python3 tag_queue.py batches K                     split what is left into K id ranges
  python3 tag_queue.py next N [--range t0001-t0221]  print the next N untagged items (in the range)
  python3 tag_queue.py record --by NAME < answers.txt
        answers: "t0001 M" or "t0002 E | short note"; tags M, E, R, O. Re-recording an item replaces it.
        File lock, so parallel taggers are safe.

Scope: male circumcision pro argument sentences with all 3 points after pass 3
(../../recheck/points_by_pass.csv). The queue and `next` show no points, flags or earlier results.
"""
import collections, csv, datetime, fcntl, pathlib, re, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
TT = HERE.parent
FP = TT.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
WK = TT / "work"
Q, T = WK / "queue.csv", WK / "tags.csv"
TAGS = ("M", "E", "R", "O")
FIELDS = ["item", "tag", "note", "tagged_by", "tagged_at"]


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wr(p, rows, fields):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fields); w.writeheader(); w.writerows(rows)


def num(s):
    return int(s[1:])


def clean(t):
    return re.sub(r"\s*\[\d+\]", "", t).strip()


def init():
    assert not Q.exists(), "queue already exists; delete it on purpose to rebuild"
    rows = [r for r in rd(FP / "recheck" / "points_by_pass.csv") if r["points_after_pass3"] == "3"]
    rows.sort(key=lambda r: (r["article"], num(r["sentence_id"])))
    out = [dict(item=f"t{i:04d}", article=r["article"], sentence_id=r["sentence_id"]) for i, r in enumerate(rows, 1)]
    WK.mkdir(exist_ok=True)
    wr(Q, out, list(out[0]))
    print(f"queue: {len(out)} items (t0001-t{len(out):04d})")


def done():
    return {r["item"]: r for r in rd(T)} if T.exists() else {}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "init":
        return init()
    Qr = rd(Q)
    D = done()
    if cmd == "status":
        print(f"tagged {len(D)}/{len(Qr)}; tags {dict(collections.Counter(r['tag'] for r in D.values()))}; "
              f"by {dict(collections.Counter(r['tagged_by'] for r in D.values()))}")
        return
    if cmd == "batches":
        k = int(sys.argv[2]); left = [q["item"] for q in Qr if q["item"] not in D]
        n = -(-len(left) // k)
        for i in range(0, len(left), n):
            part = left[i:i + n]
            print(f"--range {part[0]}-{part[-1]}   ({len(part)} untagged)")
        return
    if cmd == "next":
        n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 20
        lo, hi = ("t0000", "t9999")
        if "--range" in sys.argv:
            lo, hi = sys.argv[sys.argv.index("--range") + 1].split("-")
        sent = collections.defaultdict(dict)
        for r in rd(RUN / "survival" / "work" / "sentences_stage1.csv"):
            sent[r["slug"]][r["sentence_id"]] = r
        meta = {}
        todo = [q for q in Qr if lo <= q["item"] <= hi and q["item"] not in D][:n]
        for q in todo:
            a, s = q["article"], q["sentence_id"]
            if a not in meta:
                txt = (SNAP / a / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
                title = re.search(r"^Title:\s*(.*)$", txt, re.M).group(1).strip()
                heads = [(m.start(), len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^(#+)\s+(.*)$", txt, re.M)]
                meta[a] = (title, heads)
            title, heads = meta[a]
            S = sent[a]; order = sorted(S, key=num); i = order.index(s)
            path = {}
            for pos, lvl, h in heads:
                if pos < int(S[s]["start"]):
                    path = {k: v for k, v in path.items() if k < lvl}; path[lvl] = h
            print(f"=== {q['item']}  article: {title}  [{a} {s}]")
            print(f"    section: {' > '.join(path[k] for k in sorted(path))}")
            for j in [j for j in order[max(0, i - 6):i] if clean(S[j]["text"])][-2:]:
                print(f"      {clean(S[j]['text'])}")
            print(f"  >>  {S[s]['text']}")
            for j in [j for j in order[i + 1:i + 7] if clean(S[j]["text"])][:2]:
                print(f"      {clean(S[j]['text'])}")
        print(f"\n({len(todo)} shown; {sum(q['item'] not in D for q in Qr) - len(todo)} untagged after these overall)")
        return
    if cmd == "record":
        who = sys.argv[sys.argv.index("--by") + 1]
        valid = {q["item"] for q in Qr}
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        new = {}
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"(t\d{4})\s+([A-Za-z])\s*(?:\|\s*(.*))?$", line)
            assert m, f"bad line: {line}"
            it, tag, note = m.group(1), m.group(2).upper(), (m.group(3) or "").strip()
            assert it in valid, f"unknown item {it}"
            assert tag in TAGS, f"{it}: tag must be one of {TAGS}"
            assert it not in new, f"{it} twice in one batch"
            new[it] = dict(item=it, tag=tag, note=note, tagged_by=who, tagged_at=now)
        with open(WK / ".lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            cur = done(); cur.update(new)
            wr(T, [cur[k] for k in sorted(cur)], FIELDS)
        print(f"recorded {len(new)}; total {len(cur)}/{len(Qr)}")


if __name__ == "__main__":
    main()
