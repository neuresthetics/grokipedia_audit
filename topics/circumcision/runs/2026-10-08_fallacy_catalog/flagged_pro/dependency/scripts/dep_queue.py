#!/usr/bin/env python3
"""Resumable queue for the dependency judgments (instructions: ../DEP_PROMPT.md).

  python3 dep_queue.py status
  python3 dep_queue.py next [N]                  print the next N unjudged candidates (default 25)
  python3 dep_queue.py record --by NAME < answers.txt
        answers: one line per candidate, "c0001 N" or "c0002 Y one-line reason"
Judgments are appended to ../work/judgments.csv (candidate, decision, reason, judged_by, judged_at).
"""
import csv, fcntl, pathlib, re, sys, datetime, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
DEP = HERE.parent
FP = DEP.parent
RUN = FP.parent
J = DEP / "work" / "judgments.csv"
FIELDS = ["candidate", "decision", "reason", "judged_by", "judged_at"]


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def clean(t):
    return re.sub(r"\s*\[\d+\]", "", t).strip()


def cands():
    rows = rd(DEP / "work" / "candidates.csv")
    for i, r in enumerate(rows, 1):
        r["candidate"] = f"c{i:04d}"
    return rows


def judged():
    return {r["candidate"]: r for r in rd(J)} if J.exists() else {}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    C = cands()
    done = judged()
    if cmd == "status":
        y = sum(r["decision"] == "Y" for r in done.values())
        print(f"judged {len(done)}/{len(C)} candidates; Y {y}; by {dict(collections.Counter(r['judged_by'] for r in done.values()))}")
        return
    if cmd == "next":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 25
        sent = collections.defaultdict(dict)
        for r in rd(RUN / "survival" / "work" / "sentences_stage1.csv"):
            sent[r["slug"]][r["sentence_id"]] = r["text"]
        fp = {(r["article"], r["sentence_id"]): r for r in rd(FP / "flagged_pro.csv")}
        reasons = collections.defaultdict(list)
        F = {"r1": rd(RUN / "flags.csv"), "r2": rd(RUN / "reviewer2_flags.csv"), "r3": rd(RUN / "reviewer3_flags.csv")}
        for m in rd(RUN / "survival" / "flag_sentence_map.csv"):
            f = F[m["reviewer"]][int(m["flag_row"]) - 1]
            reasons[(m["slug"], m["sentence_id"])].append(f"{f['entry_name']}: {f['reason']}")
        todo = [c for c in C if c["candidate"] not in done][:n]
        pri = sorted({(c["prior_article"], c["prior_id"]) for c in todo})
        print("PRIORS in this batch (flagged pro sentences):")
        for p in pri:
            print(f"  [{p[0]} {p[1]}] {clean(fp[p]['text'])}")
            print(f"      flagged step: {reasons[p][0][:260]}")
        print()
        last = None
        for c in todo:
            a, s = c["survivor_article"], c["survivor_id"]
            if (a, s) != last:
                ids = sorted(sent[a], key=lambda x: int(x[1:]))
                i = ids.index(s)
                print(f"--- survivor {a} {s}")
                for j in range(max(0, i - 1), i + 1):
                    t = clean(sent[a][ids[j]])
                    if t:
                        print(("   >> " if j == i else "      ") + f"{ids[j]}: {t}")
                last = (a, s)
            print(f"   {c['candidate']} <- prior [{c['prior_article']} {c['prior_id']}]  ({c['prefilter']})")
        print(f"\n({len(todo)} shown; {len(C) - len(done) - len(todo)} more after these)")
        return
    if cmd == "record":
        who = sys.argv[sys.argv.index("--by") + 1]
        valid = {c["candidate"] for c in C}
        new = []
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"(c\d{4})\s+([YN])\b\s*(.*)$", line)
            assert m, f"bad line: {line}"
            cid, d, why = m.groups()
            assert cid in valid, cid
            assert d == "N" or why, f"Y needs a reason: {line}"
            new.append(dict(candidate=cid, decision=d, reason=why, judged_by=who,
                            judged_at=datetime.datetime.now().astimezone().isoformat(timespec="seconds")))
        J.parent.mkdir(exist_ok=True)
        with open(DEP / "work" / ".lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            cur = judged()
            for r in new:
                cur[r["candidate"]] = r
            with open(J, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, FIELDS); w.writeheader()
                w.writerows(sorted(cur.values(), key=lambda r: r["candidate"]))
        print(f"recorded {len(new)}; total {len(cur)}/{len(C)}")


if __name__ == "__main__":
    main()
