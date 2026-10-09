#!/usr/bin/env python3
"""Step 6, pass 3: resumable queue for the fresh recheck of the remaining male pro arguments.
Instructions for the checker: ../RECHECK_PROMPT.md.

  python3 recheck_queue.py init                         write ../work/queue.csv (deterministic; run once)
  python3 recheck_queue.py status                       progress overall and per tier
  python3 recheck_queue.py batches K                    split what is left into K id ranges for parallel checkers
  python3 recheck_queue.py next N [--range r0001-r0300] print the next N unchecked items (in the range)
  python3 recheck_queue.py record --by NAME < answers.txt
        answers: "r0001 no_issue" | "r0002 flag <entry-id> | <quote> | <reason>"
                 | "r0003 possible_issue <entry-id> | <quote> | <reason>"
        Recording an item replaces any earlier answer for that item. File lock, so parallel checkers are safe.

Queue order: tier A first (pro sentences still at 3 points after pass 2), then tier B (2 or 1 points). The
queue and `next` show no points, flags or pass-2 results; the tier is only in the item id range.
"""
import csv, datetime, fcntl, json, pathlib, re, sys, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
RC = HERE.parent
FP = RC.parent
RUN = FP.parent
SNAP = RUN.parent.parent / "articles"
WK = RC / "work"
Q, F = WK / "queue.csv", WK / "findings.csv"
CAT_EXTRACT = RC / "catalog_ids_v0.6.1.json"
FIELDS = ["item", "verdict", "entry_id", "quote", "reason", "checked_by", "checked_at"]


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


def ids():
    return json.load(open(CAT_EXTRACT, encoding="utf-8"))["text_detectable_ids"]


def init():
    assert not Q.exists(), "queue already exists; delete it on purpose to rebuild"
    sc = rd(RUN / "survival" / "survival_scores.csv")
    after2 = {(r["article"], r["sentence_id"]): int(r["points_after"])
              for r in rd(FP / "dependency" / "survivors_after_priors.csv")}
    pro = [r for r in sc if r["side"] == "pro" and r["topic_group"] == "male"]
    keyf = lambda r: (r["article"], num(r["sentence_id"]))
    a = sorted([r for r in pro if after2.get((r["article"], r["sentence_id"]), 0) == 3], key=keyf)
    b = sorted([r for r in pro if 1 <= after2.get((r["article"], r["sentence_id"]), 0) <= 2], key=keyf)
    rows = [dict(item=f"r{i:04d}", tier="A" if i <= len(a) else "B", article=r["article"], sentence_id=r["sentence_id"])
            for i, r in enumerate(a + b, 1)]
    WK.mkdir(exist_ok=True)
    wr(Q, rows, list(rows[0]))
    print(f"queue: {len(a)} tier A (r0001-r{len(a):04d}), {len(b)} tier B (r{len(a)+1:04d}-r{len(rows):04d})")


def done():
    d = collections.defaultdict(list)
    if F.exists():
        for r in rd(F):
            d[r["item"]].append(r)
    return d


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "init":
        return init()
    if cmd == "refresh-catalog":
        full = json.load(open(sys.argv[2], encoding="utf-8"))
        assert full["version"] in ("0.6.1", "v0.6.1")
        keep = sorted(e["id"] for e in full["entries"] if str(e.get("text_detectable")).lower() != "no")
        json.dump({"source": "neuresthetics/fallacy_catalog fallacies.json at commit "
                   "2a56493a3931018e9143bc7235f152f5cc5b459e (v0.6.1)",
                   "note": "ids of all entries whose text_detectable is not 'no'; used to validate answers",
                   "text_detectable_ids": keep}, open(CAT_EXTRACT, "w"), indent=1)
        return print(f"{len(keep)} ids")
    Qr = rd(Q)
    D = done()
    if cmd == "status":
        c = collections.Counter((q["tier"], q["item"] in D) for q in Qr)
        fl = collections.Counter(r["verdict"] for v in D.values() for r in v)
        print(f"checked {len(D)}/{len(Qr)}; tier A {c['A', True]}/{c['A', True] + c['A', False]}, "
              f"tier B {c['B', True]}/{c['B', True] + c['B', False]}; lines {dict(fl)}; "
              f"by {dict(collections.Counter(v[0]['checked_by'] for v in D.values()))}")
        return
    if cmd == "batches":
        k = int(sys.argv[2]); left = [q["item"] for q in Qr if q["item"] not in D]
        n = -(-len(left) // k)
        for i in range(0, len(left), n):
            part = left[i:i + n]
            print(f"--range {part[0]}-{part[-1]}   ({len(part)} unchecked)")
        return
    if cmd == "next":
        n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 20
        lo, hi = "r0000", "r9999"
        if "--range" in sys.argv:
            lo, hi = sys.argv[sys.argv.index("--range") + 1].split("-")
        sent = collections.defaultdict(dict)
        for r in rd(RUN / "survival" / "work" / "sentences_stage1.csv"):
            sent[r["slug"]][r["sentence_id"]] = r
        heads = {}
        todo = [q for q in Qr if lo <= q["item"] <= hi and q["item"] not in D][:n]
        for q in todo:
            a, s = q["article"], q["sentence_id"]
            if a not in heads:
                txt = (SNAP / a / "snapshots" / "2026-10-01.txt").read_text(encoding="utf-8")
                heads[a] = [(m.start(), m.group(1), m.group(2).strip()) for m in re.finditer(r"^(#+)\s+(.*)$", txt, re.M)]
            S = sent[a]; order = sorted(S, key=num); i = order.index(s)
            start = int(S[s]["start"])
            path = {}
            for pos, lvl, h in heads[a]:
                if pos < start:
                    path = {k: v for k, v in path.items() if k < len(lvl)}; path[len(lvl)] = h
            print(f"=== {q['item']}  [{a} {s}]  section: {' > '.join(path[k] for k in sorted(path))}")
            ctx = [j for j in order[max(0, i - 6):i] if clean(S[j]["text"])][-3:]
            for j in ctx:
                print(f"      {j}: {clean(S[j]['text'])}")
            print(f"  >>  {s}: {S[s]['text']}")
            nxt = [j for j in order[i + 1:i + 4] if clean(S[j]["text"])][:1]
            for j in nxt:
                print(f"      {j}: {clean(S[j]['text'])}")
        print(f"\n({len(todo)} shown; {sum(q['item'] not in D for q in Qr) - len(todo)} unchecked after these overall)")
        return
    if cmd == "record":
        who = sys.argv[sys.argv.index("--by") + 1]
        ok = set(ids())
        qby = {q["item"]: q for q in Qr}
        text = {(r["article"], r["sentence_id"]): r["text"] for r in rd(RUN / "survival" / "survival_scores.csv")}
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        new = collections.defaultdict(list)
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"(r\d{4})\s+(no_issue|flag|possible_issue)\b\s*(.*)$", line)
            assert m, f"bad line: {line}"
            it, v, rest = m.groups()
            assert it in qby, it
            if v == "no_issue":
                assert not rest, f"no_issue takes nothing after it: {line}"
                new[it].append(dict(item=it, verdict=v, entry_id="", quote="", reason="", checked_by=who, checked_at=now))
                continue
            parts = [p.strip() for p in rest.split("|")]
            assert len(parts) == 3 and all(parts), f"need '<entry-id> | <quote> | <reason>': {line}"
            e, quote, why = parts
            assert e in ok, f"{it}: unknown or not text-detectable entry id {e!r}"
            t = text[(qby[it]["article"], qby[it]["sentence_id"])]
            assert quote in t, f"{it}: quote is not an exact substring of the sentence"
            new[it].append(dict(item=it, verdict=v, entry_id=e, quote=quote, reason=why, checked_by=who, checked_at=now))
        for it, rows in new.items():
            vs = {r["verdict"] for r in rows}
            assert not ("no_issue" in vs and len(rows) > 1), f"{it}: no_issue mixed with other lines"
            es = [r["entry_id"] for r in rows if r["entry_id"]]
            assert len(es) == len(set(es)), f"{it}: same entry twice"
        with open(WK / ".lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            cur = done()
            cur.update(new)
            rows = [r for k in sorted(cur) for r in cur[k]]
            wr(F, rows, FIELDS)
        print(f"recorded {len(new)} items; total {len(cur)}/{len(Qr)}")


if __name__ == "__main__":
    main()
