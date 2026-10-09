#!/usr/bin/env python3
"""Step 6b, stage 1: cheap pre-filter of (survivor, prior) pairs for the model to judge.

Survivor = a pro argument sentence in a male circumcision article with points_left >= 1 (step 5).
Prior    = one of the 61 flagged pro sentences in flagged_pro.csv (step 6).
A pair becomes a candidate if either:
  W  (window)      same article, and the survivor sits from 2 sentences before to 8 sentences after the prior
                   (sentence ids are in reading order, prose sentences only);
  K  (claim key)   the survivor matches the keyword pattern of a claim key that a prior carries
                   (prior_claims.csv, assigned by a model from the flag reasons). It is paired with the
                   nearest earlier prior carrying that key in the same article if there is one, else the
                   nearest later one in the same article, else the key's single representative prior
                   (fewest points left, then article and sentence order).
Writes ../work/candidates.csv. Deterministic.
"""
import csv, re, pathlib, collections, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
DEP = HERE.parent
FP = DEP.parent
RUN = FP.parent
W_BEFORE, W_AFTER = 2, 8

KEYS = {  # key: (pattern A, pattern B or None); both must match (case-insensitive)
    "hiv_trial_carryover": (r"\bHIV\b", r"neonat|infan|newborn|lifelong|childhood|low[- ]prevalence|Europe|United States|U\.S\.|developed|ritual|traditional"),
    "net_benefit_settled": (r"benefits? (clearly |far |substantially )?outweigh|net (health |public health )?benefit", None),
    "pain_minimal": (r"\bpain", r"near-painless|minimal|transient|brief|rapid|heal|no lasting|long-term"),
    "critics_dismissed": (r"critic|activist|advoca|intactiv|opponent|NGO|anti-circumcision",
                          r"bias|ideolog|anecdot|low-quality|selective|exaggerat|amplif|emotional|misinform|unsubstantiated|conflict"),
    "observational_double_standard": (r"observational|self-report|recall|correlat", r"RCT|randomi|bias|causal"),
    "no_risk_compensation": (r"compensat|disinhibit", None),
    "outcomes_answer_consent": (r"consent|autonom|bodily integrity|deontolog", r"satisf|regret|complication|harm|benefit|outcome"),
    "vmmc_decline_causal": (r"incidence|declin|averted", r"VMMC|scale-up|program|rollout"),
    "sensation_unaffected": (r"glans|sensitiv|sensation|nerve|pleasure|Meissner|sexual function|satisfaction",
                             r"unaffected|preserved|no (significant |measurable |consistent )?(difference|effect|loss|reduction|impact|deficit)|comparable|not (reduce|impair|affect)|without (harm|adverse|loss|impair)"),
    "preventive_medicine_analogy": (r"vaccin|heel|immuni[sz]|herd|orthodont|screening", None),
    "deferral_incoherent": (r"defer|adult(hood)? (choice|decision)|uptake|wait(ing)? until", None),
    "restoration_means_acceptance": (r"restor|revers", None),
    "tradition_proves_fit": (r"continuity|persist|generations|centuries|millennia|enduring|long-?standing",
                             r"safe|adaptive|fit\b|valid|efficac|benefit|wisdom"),
}


def rd(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(sid):
    return int(sid[1:])


def main():
    sc = rd(RUN / "survival" / "survival_scores.csv")
    surv = [r for r in sc if r["topic_group"] == "male" and r["side"] == "pro" and int(r["points_left"]) >= 1]
    pri = {(r["article"], r["sentence_id"]): r for r in rd(FP / "flagged_pro.csv")}
    keys = {(r["article"], r["sentence_id"]): [k for k in r["claim_key"].split("|") if k]
            for r in rd(DEP / "prior_claims.csv")}
    assert set(keys) == set(pri), "prior_claims.csv must list exactly the 61 flagged pro sentences"
    for ks in keys.values():
        for k in ks:
            assert k in KEYS, k
    bykey = collections.defaultdict(list)
    for p, ks in keys.items():
        for k in ks:
            bykey[k].append(p)
    rep = {k: sorted(ps, key=lambda p: (int(pri[p]["points_left"]), p[0], num(p[1])))[0] for k, ps in bykey.items()}
    cand = {}
    for s in surv:
        sk = (s["article"], s["sentence_id"])
        for p in pri:
            if p[0] == sk[0] and p != sk and -W_BEFORE <= num(sk[1]) - num(p[1]) <= W_AFTER:
                cand.setdefault((sk, p), set()).add("W")
        for k, (a, b) in KEYS.items():
            if k not in bykey or not re.search(a, s["text"], re.I) or (b and not re.search(b, s["text"], re.I)):
                continue
            same = [p for p in bykey[k] if p[0] == sk[0] and p != sk]
            if same:
                before = [p for p in same if num(p[1]) < num(sk[1])]
                p = max(before, key=lambda p: num(p[1])) if before else min(same, key=lambda p: num(p[1]))
            else:
                p = rep[k]
                if p == sk:
                    continue
            cand.setdefault((sk, p), set()).add("K:" + k)
    rows = []
    for (sk, p), why in sorted(cand.items(), key=lambda t: (t[0][0][0], num(t[0][0][1]), t[0][1][0], num(t[0][1][1]))):
        rows.append(dict(survivor_article=sk[0], survivor_id=sk[1], prior_article=p[0], prior_id=p[1],
                         same_article="yes" if sk[0] == p[0] else "no", prefilter="|".join(sorted(why))))
    out = DEP / "work" / "candidates.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"survivors {len(surv)}; candidate pairs {len(rows)}; survivors with a candidate "
          f"{len({(r['survivor_article'], r['survivor_id']) for r in rows})}; "
          f"by source {collections.Counter('W' if 'W' in r['prefilter'] else 'K only' for r in rows)}; "
          f"cross-article {sum(r['same_article'] == 'no' for r in rows)}")


if __name__ == "__main__":
    main()
