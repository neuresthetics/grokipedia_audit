#!/usr/bin/env python3
"""Model labeling of every prose sentence (13,199), resumable. Progress lives in ../labels/model_labels.csv;
re-running picks up where the last session stopped. Instructions for the labeling model: ../LABEL_PROMPT.md.

    python3 label_queue.py status                    # progress per article
    python3 label_queue.py next [N] [--slug S]       # print the next batch (default 80 unlabeled sentences of
                                                     #   one article, with 2 context sentences on each side);
                                                     #   --slug restricts it to one article
    python3 label_queue.py record <slug> --by <who> < answers.txt

The printout shows only the article title, its group and the sentences (citation markers removed for
reading). It never shows the rule label or any reviewer flag.

Answer format for `record` (whitespace separated, later tokens override earlier ones):
    s0001-s0080:N   every sentence in the range is not_argument
    s0012:P         s0012 is pro      (P pro, A anti, N not_argument)
Only sentence ids of that article are accepted. Each record call stamps a batch number.
"""
import csv, re, sys, pathlib, datetime
HERE = pathlib.Path(__file__).resolve().parent
SURV = HERE.parent
STAGE1 = SURV / "work" / "sentences_stage1.csv"
OUT = SURV / "labels" / "model_labels.csv"
FIELDS = ["slug", "sentence_id", "model_side", "batch", "labeled_by", "labeled_at"]
SIDE = {"P": "pro", "A": "anti", "N": "not_argument"}
TOPIC = SURV.parents[2]


def sentences():
    rows = list(csv.DictReader(open(STAGE1, encoding="utf-8")))
    by = {}
    for r in rows:
        by.setdefault(r["slug"], []).append(r)
    return by


def titles():
    t = (TOPIC / "ARTICLE_LIST.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*\[snapshot\]\(articles/([^/]+)/", t, re.M):
        out[m.group(2)] = m.group(1)
    return out


def order():
    t = (TOPIC / "ARTICLE_LIST.md").read_text(encoding="utf-8")
    return re.findall(r"\]\(articles/([^/]+)/snapshots/", t)


def load():
    if not OUT.exists():
        return {}
    return {(r["slug"], r["sentence_id"]): r for r in csv.DictReader(open(OUT, encoding="utf-8"))}


def save(lab):
    OUT.parent.mkdir(exist_ok=True)
    rows = sorted(lab.values(), key=lambda r: (r["slug"], r["sentence_id"]))
    tmp = OUT.with_suffix(".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    tmp.replace(OUT)


def clean(s):
    return re.sub(r"\s*\[\d+\]", "", s)


def main():
    by, lab = sentences(), load()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        tot = done = 0
        for s in order():
            n = len(by[s]); d = sum((s, r["sentence_id"]) in lab for r in by[s])
            tot += n; done += d
            if 0 < d < n or len(sys.argv) > 2:
                print(f"  {s}: {d}/{n}")
        arts = sum(all((s, r["sentence_id"]) in lab for r in by[s]) for s in order())
        print(f"labeled {done}/{tot} sentences; {arts}/{len(order())} articles complete")
    elif cmd == "next":
        n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 80
        only = sys.argv[sys.argv.index("--slug") + 1] if "--slug" in sys.argv else None
        tt = titles()
        for s in ([only] if only else order()):
            todo = [i for i, r in enumerate(by[s]) if (s, r["sentence_id"]) not in lab]
            if not todo:
                continue
            a, rows = todo[0], by[s]
            b = min(a + n, len(rows))
            print(f"# ARTICLE: {tt.get(s, s)}  (slug {s}, group {rows[0]['group']}, sentences {len(rows)})")
            print(f"# label {rows[a]['sentence_id']}-{rows[b - 1]['sentence_id']}; lines marked ctx are context only")
            for i in range(max(0, a - 2), min(len(rows), b + 2)):
                tag = rows[i]["sentence_id"] if a <= i < b else "ctx  "
                print(f"{tag}| {clean(rows[i]['text'])}")
            return
        print("all sentences labeled")
    elif cmd == "record":
        import fcntl
        lock = open(OUT.parent / ".lock", "w"); fcntl.flock(lock, fcntl.LOCK_EX)  # safe with parallel labelers
        lab = load()
        slug = sys.argv[2]
        who = sys.argv[sys.argv.index("--by") + 1] if "--by" in sys.argv else "model"
        ids = [r["sentence_id"] for r in by[slug]]
        pos = {x: i for i, x in enumerate(ids)}
        ans = {}
        for tok in sys.stdin.read().split():
            m = re.fullmatch(r"(s\d{4})(?:-(s\d{4}))?:([PAN])", tok)
            if not m or m.group(1) not in pos or (m.group(2) and m.group(2) not in pos):
                sys.exit(f"bad token {tok!r}")
            lo, hi = pos[m.group(1)], pos[m.group(2) or m.group(1)]
            for i in range(lo, hi + 1):
                ans[ids[i]] = SIDE[m.group(3)]
        batch = 1 + max([int(r["batch"]) for r in lab.values()] or [0])
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        for sid, side in ans.items():
            lab[(slug, sid)] = dict(slug=slug, sentence_id=sid, model_side=side, batch=batch, labeled_by=who,
                                    labeled_at=now)
        save(lab)
        c = {v: sum(1 for x in ans.values() if x == v) for v in SIDE.values()}
        print(f"batch {batch}: recorded {len(ans)} labels for {slug} {c}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
