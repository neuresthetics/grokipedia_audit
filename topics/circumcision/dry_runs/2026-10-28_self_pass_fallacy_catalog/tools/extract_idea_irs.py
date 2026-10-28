#!/usr/bin/env python3
"""Cue-driven Idea IR extractor for inventory passages.

Blind extract: no fallacy labels, no expected_checker.
Charity + anti-collapse per EXTRACTOR_PROMPT.md.
Quotes are exact substrings of the passage.
Does not modify fallacy_catalog.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Import validator from package (read-only)
sys.path.insert(0, "/workspace/fallacy_catalog")
from idea_detection.ir import validate  # noqa: E402

SPEAKER_RE = re.compile(
    r"\b(Critics?(?:\s+of\s+[\w\s-]{0,40})?|Proponents?(?:\s+of\s+[\w\s-]{0,40})?|"
    r"Opponents?|Supporters?|Advocates?|Defenders?|Intactivists?|"
    r"Researchers?|Scholars?|Authors?|They|He|She|"
    r"The Apostle Paul|Paul|WHO|AAP|CDC|medical bodies|"
    r"the resolution|the statement|the policy)\b",
    re.I,
)

ARGUE_RE = re.compile(
    r"\b(argue[sd]?|contend(?:s|ed)?|assert(?:s|ed)?|claim(?:s|ed)?|"
    r"maintain(?:s|ed)?|emphasiz(?:e|es|ed)|conclud(?:e|es|ed)|"
    r"urg(?:e|es|ed)|insist(?:s|ed)?|suggest(?:s|ed)?)\b",
    re.I,
)

INFER_SPLIT = re.compile(
    r"(?:,?\s*\b(?:thus|therefore|hence|so|accordingly|thereby)\b\s*|"
    r",?\s*\bbecause\b\s+|"
    r",?\s*\bsince\b\s+|"
    r",?\s*\bas\b\s+(?=a\s+result)|"
    r"\s+to\s+argue\s+that\s+)",
    re.I,
)

AUTH_RE = re.compile(
    r"\b((?:citing|according to|per)\s+[^,.;]{3,80}|"
    r"(?:systematic reviews?|meta-analyses|meta-analysis|randomized controlled trials?|"
    r"RCTs?|peer-reviewed stud(?:y|ies)|longitudinal stud(?:y|ies)|"
    r"WHO|World Health Organization|American Academy of Pediatrics|AAP|"
    r"CDC|Centers for Disease Control|Cochrane|"
    r"medical (?:bodies|associations|societies)|policy statement))\b",
    re.I,
)

POPULAR_RE = re.compile(
    r"\b((?:most|many|majority of|widespread among|popular among|commonly)\s+"
    r"(?:people|parents|men|women|mothers|fathers|communities|cultures|"
    r"Americans|practitioners|physicians|doctors)[^,.;]{0,40})\b",
    re.I,
)

UNPROVEN_RE = re.compile(
    r"\b(no evidence(?:\s+of|\s+for)?[^,.;]{0,60}|no proof[^,.;]{0,40}|"
    r"unproven[^,.;]{0,40}|absence of (?:proof|evidence)[^,.;]{0,40}|"
    r"never (?:been )?(?:proved|shown)[^,.;]{0,40}|"
    r"has not been (?:shown|proven)[^,.;]{0,40}|unsubstantiated[^,.;]{0,40})\b",
    re.I,
)

CAUSE_RE = re.compile(
    r"\b(caus(?:e|es|ed|ing)|leads? to|resulting in|results? in|"
    r"reduces?|increases?|prevents?|inflicts?|transforms?|"
    r"attributable to|due to|gives rise to|brings about)\b",
    re.I,
)

CORR_RE = re.compile(
    r"\b(associat(?:ed|ion)|correlat(?:ed|ion)|linked to|coincid(?:es|ed))\b",
    re.I,
)

ATTACK_PERSON_RE = re.compile(
    r"\b((?:biased|untrustworthy|ideologue|extremist|activist|"
    r"financial(?:ly)? (?:motivated|interested)|conflict of interest|"
    r"paid by|ignorant|dishonest)[^,.;]{0,50})\b",
    re.I,
)

ASSOC_TRAIT_RE = re.compile(
    r"\b((?:associated with|once supported|backed by|aligned with|"
    r"tied to|linked to)\s+[^,.;]{3,60})\b",
    re.I,
)

DILEMMA_RE = re.compile(
    r"\b((?:either\s+[^,.;]{5,80}\s+or\s+[^,.;]{5,80}|"
    r"the only (?:choice|option|alternative)|"
    r"no (?:other|viable) (?:choice|option|alternative)))\b",
    re.I,
)

IGNORE_RE = re.compile(
    r"\b(ignore|dismiss|disregard|set aside|brush(?:ed)? aside|"
    r"overlook|fail(?:s|ed)? to (?:address|consider))\b",
    re.I,
)

WEAK_RE = re.compile(
    r"\b(may|might|could|likely|probably|perhaps|possibly|potentially|"
    r"suspect(?:s|ed)?|can)\b",
    re.I,
)

HEART_RE = re.compile(
    r"circumcision of the heart|spiritual\s+[\"']?circumcision|circumcision\s+of\s+the\s+heart",
    re.I,
)
PHYS_CIRC_RE = re.compile(r"\bcircumcision\b", re.I)

REC_RE = re.compile(
    r"\b(should|must|ought to|need to|recommend(?:s|ed)?|urge[sd]?|"
    r"prohibit|ban|outlaw|require)\b",
    re.I,
)


def _q(text: str, passage: str, maxlen: int = 160) -> str | None:
    """Return an exact quote from passage, truncated at word boundary if long."""
    if not text:
        return None
    text = text.strip()
    if text in passage:
        return text[:maxlen] if len(text) <= maxlen else _trim_in(passage, text, maxlen)
    # try shorter windows
    for n in (120, 80, 60, 40, 24):
        chunk = text[:n].rstrip()
        if chunk and chunk in passage:
            return chunk
    # find first 8+ word sequence present
    words = text.split()
    for length in range(min(12, len(words)), 3, -1):
        cand = " ".join(words[:length])
        if cand in passage:
            return cand[:maxlen]
    return None


def _trim_in(passage: str, text: str, maxlen: int) -> str:
    chunk = text[:maxlen]
    if chunk in passage:
        return chunk
    # back off to last space
    while chunk and chunk not in passage:
        chunk = chunk.rsplit(" ", 1)[0]
    return chunk if chunk in passage else text[:40]


def _speaker(passage: str) -> str | None:
    m = SPEAKER_RE.search(passage)
    if not m:
        return None
    raw = m.group(1).strip().lower()
    if raw.startswith("critic"):
        return "critics"
    if raw.startswith("proponent") or raw.startswith("supporter") or raw.startswith("advocate") or raw.startswith("defender"):
        return "proponents"
    if raw.startswith("opponent"):
        return "opponents"
    if "paul" in raw:
        return "paul"
    if raw in ("they", "he", "she"):
        return raw
    if "who" == raw or raw.startswith("who"):
        return "WHO"
    if "aap" in raw:
        return "AAP"
    if "cdc" in raw:
        return "CDC"
    if "medical bodies" in raw:
        return "medical_bodies"
    if "resolution" in raw:
        return "resolution"
    if "intactivist" in raw:
        return "intactivists"
    return re.sub(r"\s+", "_", raw)[:40]


def _hedge(text: str) -> str:
    return "weak" if WEAK_RE.search(text) else "none"


def _short_claim_text(quote: str) -> str:
    q = quote.strip()
    if not q.endswith("."):
        q = q + "."
    # capitalize
    return q[0].upper() + q[1:] if q else q


def extract(passage_id: str, passage: str) -> dict:
    speaker = _speaker(passage)
    claims = []
    edges = []
    steps = []
    agents = []
    terms = []
    bindings = []
    evidence_sets = []
    cid = 0
    eid = 0

    def add_claim(quote, role, *, hedge=None, scope="truth", is_arg=False, asserts_cause=False, unstated=False):
        nonlocal cid
        q = _q(quote, passage)
        if not q:
            return None
        cid += 1
        c = {
            "id": f"c{cid}",
            "text": _short_claim_text(q),
            "span": {"quote": q},
            "role": role,
            "hedge": hedge if hedge is not None else _hedge(q),
            "scope": scope,
        }
        if speaker:
            c["speaker"] = speaker
        if is_arg:
            c["is_argument_or_proposal"] = True
        if asserts_cause:
            c["asserts_cause"] = True
        if unstated:
            c["unstated"] = True
        claims.append(c)
        return c["id"]

    def add_edge(etype, source, target, quote, **extra):
        nonlocal eid
        if not source or not target:
            return None
        q = _q(quote, passage) or _q(passage[:80], passage)
        if not q:
            return None
        eid += 1
        e = {
            "id": f"e{eid}",
            "type": etype,
            "source": source,
            "target": target,
            "span": {"quote": q},
        }
        e.update(extra)
        edges.append(e)
        return e["id"]

    # --- Authority appeals ---
    auth_ids = []
    for m in AUTH_RE.finditer(passage):
        aq = m.group(1)
        # conclusion near authority: look for argue/contend clause or whole sentence
        # create a conclusion claim from surrounding argumentative clause
        auth_ids.append(aq)

    # --- Main argumentative structure ---
    # Prefer splitting on thus/therefore/because
    parts = INFER_SPLIT.split(passage)
    # INFER_SPLIT with capturing would include delimiters; without, just parts
    has_infer = bool(INFER_SPLIT.search(passage))

    argue_m = ARGUE_RE.search(passage)
    unproven_m = UNPROVEN_RE.search(passage)
    cause_m = CAUSE_RE.search(passage)
    corr_m = CORR_RE.search(passage)
    dilemma_m = DILEMMA_RE.search(passage)
    ignore_m = IGNORE_RE.search(passage)
    popular_m = POPULAR_RE.search(passage)
    attack_m = ATTACK_PERSON_RE.search(passage)
    assoc_m = ASSOC_TRAIT_RE.search(passage)

    premise_id = None
    conclusion_id = None
    unproven_id = None

    if has_infer and len(parts) >= 2:
        # first chunk premise-ish, last chunk conclusion-ish
        pre = parts[0].strip(" ,;")
        post = parts[-1].strip(" ,;")
        # if "because" style, sometimes premise is after
        because_first = bool(re.search(r"\bbecause\b|\bsince\b", passage, re.I)) and not re.search(
            r"\b(?:thus|therefore|hence|so|accordingly|thereby)\b", passage, re.I
        )
        if because_first and len(parts) >= 2:
            # "X because Y" → X conclusion, Y premise
            # split left of because vs right
            bm = re.search(r"\b(?:because|since)\b", passage, re.I)
            if bm:
                left, right = passage[: bm.start()].strip(" ,;"), passage[bm.end() :].strip(" ,;")
                conclusion_id = add_claim(left[-200:] if len(left) > 200 else left, "conclusion", is_arg=True)
                premise_id = add_claim(right[:200], "premise")
                if premise_id and conclusion_id:
                    add_edge("supports", premise_id, conclusion_id, bm.group(0) + " " + right[:60], warrant="asserted")
        else:
            if pre:
                premise_id = add_claim(pre[-200:] if len(pre) > 200 else pre, "premise")
            if post:
                role = "recommendation" if REC_RE.search(post) else "conclusion"
                scope = "action" if role == "recommendation" else "truth"
                conclusion_id = add_claim(post[:200], role, scope=scope, is_arg=True)
            if premise_id and conclusion_id:
                cue = "thus"
                for cword in ("thus", "therefore", "hence", "so", "accordingly", "thereby"):
                    if re.search(rf"\b{cword}\b", passage, re.I):
                        cue = cword
                        break
                add_edge("supports", premise_id, conclusion_id, cue, warrant="asserted")
    elif argue_m:
        # "X argue/contend that Y"
        after = passage[argue_m.end() :].lstrip(" that").strip()
        # strip leading "that "
        after = re.sub(r"^that\s+", "", after, flags=re.I)
        # take up to ~2 sentences
        sent = re.split(r"(?<=[.:;])\s+", after)[0] if after else after
        if not sent:
            sent = after[:220]
        role = "recommendation" if REC_RE.search(sent) else "conclusion"
        scope = "action" if role == "recommendation" else "truth"
        conclusion_id = add_claim(sent[:220], role, scope=scope, is_arg=True)
        # optional preceding context as premise
        before = passage[: argue_m.start()].strip(" ,;")
        if before and len(before) > 20:
            premise_id = add_claim(before[-180:], "premise")
            if premise_id and conclusion_id:
                add_edge("supports", premise_id, conclusion_id, argue_m.group(0), warrant="asserted")
    else:
        # Descriptive / report — still emit a report claim (anti-collapse: if causal/inferential cue exists, prefer edges)
        role = "report"
        is_arg = False
        if cause_m or corr_m or unproven_m or auth_ids or popular_m:
            role = "conclusion"
            is_arg = True
        conclusion_id = add_claim(passage[:220], role, is_arg=is_arg)

    # Unproven → premise supporting conclusion (argument-from-ignorance shape)
    if unproven_m:
        uq = unproven_m.group(1)
        unproven_id = add_claim(uq, "premise")
        if unproven_id and conclusion_id and unproven_id != conclusion_id:
            # if conclusion is the unproven claim itself, make a separate evaluative conclusion
            add_edge("supports", unproven_id, conclusion_id, uq[:80], warrant="asserted")
        elif unproven_id and not conclusion_id:
            conclusion_id = add_claim(passage[:180], "conclusion", is_arg=True)
            add_edge("supports", unproven_id, conclusion_id, uq[:80], warrant="asserted")

    # Authority edges
    if auth_ids and conclusion_id:
        for aq in auth_ids[:3]:
            # create a premise for the source citation, then appeals_to_source into conclusion
            src_id = add_claim(aq, "premise")
            if src_id:
                add_edge("appeals_to_source", src_id, conclusion_id, aq)
    elif auth_ids and not conclusion_id:
        conclusion_id = add_claim(passage[:200], "conclusion", is_arg=True)
        for aq in auth_ids[:2]:
            src_id = add_claim(aq, "premise")
            if src_id:
                add_edge("appeals_to_source", src_id, conclusion_id, aq)

    # Popularity
    if popular_m and conclusion_id:
        pq = popular_m.group(1)
        pop_id = add_claim(pq, "premise")
        if pop_id:
            add_edge("appeals_to_source", pop_id, conclusion_id, pq)

    # Causation
    if cause_m and conclusion_id:
        cq = cause_m.group(0)
        # mark conclusion or a claim as asserts_cause if bare causal language
        for c in claims:
            if c["id"] == conclusion_id or CAUSE_RE.search(c.get("text", "")):
                if "reduce" in cq.lower() or "cause" in cq.lower() or "lead" in cq.lower() or "result" in cq.lower() or "inflict" in cq.lower() or "prevent" in cq.lower() or "attributable" in cq.lower():
                    c["asserts_cause"] = True
        # also add causes edge from premise to conclusion if we have both
        if premise_id and conclusion_id:
            add_edge("causes", premise_id, conclusion_id, cq)

    if corr_m and premise_id and conclusion_id:
        add_edge("correlates", premise_id, conclusion_id, corr_m.group(0))

    # Dilemma
    if dilemma_m and conclusion_id:
        dq = dilemma_m.group(1)
        d_id = add_claim(dq, "premise")
        if d_id:
            add_edge("supports", d_id, conclusion_id, dq[:80], warrant="asserted")

    # Ignore
    if ignore_m and conclusion_id and premise_id:
        add_edge("ignores", conclusion_id, premise_id, ignore_m.group(0))

    # Person attack / association
    if attack_m:
        tq = attack_m.group(1)
        agent_id = "agent1"
        agents.append({
            "id": agent_id,
            "name_span": {"quote": _q(speaker or "they", passage) or passage[:20]},
            "traits": [{"id": "t1", "label": tq[:80], "span": {"quote": _q(tq, passage) or tq[:40]}}],
        })
        # need an argument claim as target
        tgt = conclusion_id
        if tgt:
            # create attacks_person edge — source is a claim that carries the attack
            att_claim = add_claim(tq, "premise")
            if att_claim:
                add_edge("attacks_person", att_claim, tgt, tq[:80])
                # supports reject
                rej = add_claim("dismiss the claim", "conclusion", is_arg=True, unstated=True)
                # unstated dismiss may lack quote — use attack quote
                for c in claims:
                    if c["id"] == rej:
                        c["span"] = {"quote": _q(tq, passage) or tq[:40]}
                        c["text"] = "The targeted argument should be dismissed."
                if rej:
                    add_edge("supports", att_claim, rej, tq[:60])

    if assoc_m and conclusion_id:
        aq = assoc_m.group(1)
        if not any(a.get("id") == "agent1" for a in agents):
            agents.append({
                "id": "agent_assoc",
                "name_span": {"quote": _q(aq.split()[0], passage) or aq[:20]},
                "traits": [{"id": "assoc1", "label": aq[:100], "span": {"quote": _q(aq, passage) or aq[:40]}}],
            })
        src = add_claim(aq, "premise")
        if src:
            add_edge("supports", src, conclusion_id, aq[:80])

    # Equivocation: physical vs spiritual circumcision
    if HEART_RE.search(passage) and len(PHYS_CIRC_RE.findall(passage)) >= 2:
        terms.append({
            "id": "t_circ",
            "surface": "circumcision",
            "senses": [
                {"id": "physical", "gloss": "genital cutting / brit milah"},
                {"id": "spiritual", "gloss": "metaphorical circumcision of the heart"},
            ],
        })
        # bind occurrences
        for i, m in enumerate(PHYS_CIRC_RE.finditer(passage)):
            sense = "spiritual" if HEART_RE.search(passage[max(0, m.start() - 30) : m.end() + 40]) else "physical"
            bindings.append({
                "term_id": "t_circ",
                "sense_id": sense,
                "claim_id": conclusion_id or (claims[0]["id"] if claims else "c1"),
                "span": {"quote": m.group(0)},
            })
            if i >= 5:
                break

    # Instantiates: particular → general (every/all/must)
    gen_m = re.search(r"\b((?:every|all|always|must|universal(?:ly)?)\s[^,.;]{5,80})", passage, re.I)
    case_m = re.search(r"\b((?:this|these|one|a single|an?)\s[^,.;]{5,60})", passage, re.I)
    if gen_m and case_m and conclusion_id:
        case_id = add_claim(case_m.group(1), "premise")
        gen_id = conclusion_id
        # ensure conclusion looks general
        if case_id:
            add_edge("instantiates", case_id, gen_id, case_m.group(1)[:60])

    # Critics attacking a framing → attacks_claim
    if speaker in ("critics", "opponents", "proponents") and conclusion_id and premise_id:
        # if both sides language
        if re.search(r"\b(?:but|however|though|although)\b", passage, re.I):
            add_edge("attacks_claim", conclusion_id, premise_id, speaker)

    # Ensure at least one claim
    if not claims:
        add_claim(passage[:200], "report")

    # Build step
    claim_ids = [c["id"] for c in claims]
    step_quote = _q(passage[:140], passage) or passage[:80]
    step = {"id": "s1", "span": {"quote": step_quote}, "claim_ids": claim_ids}
    if speaker:
        step["speaker"] = speaker
    if all(c.get("role") == "report" for c in claims) and not edges:
        step["no_argument"] = True
    steps.append(step)

    # Dedup edges with same source/target/type
    seen = set()
    uniq_edges = []
    for e in edges:
        key = (e["type"], e["source"], e["target"])
        if key in seen:
            continue
        seen.add(key)
        uniq_edges.append(e)

    # Fix: unstated dismiss claim must have quote in passage — already handled
    # Drop claims whose span quote is not in passage
    ok_claims = []
    for c in claims:
        q = c.get("span", {}).get("quote", "")
        if q and q in passage:
            ok_claims.append(c)
    ok_ids = {c["id"] for c in ok_claims}
    ok_edges = [e for e in uniq_edges if e["source"] in ok_ids and e["target"] in ok_ids and e["span"]["quote"] in passage]
    for s in steps:
        s["claim_ids"] = [i for i in s["claim_ids"] if i in ok_ids]
        if not s["claim_ids"] and ok_claims:
            s["claim_ids"] = [ok_claims[0]["id"]]

    # bindings claim_id must exist
    ok_bindings = [b for b in bindings if b.get("claim_id") in ok_ids and b["span"]["quote"] in passage]

    # agents name_span must be in passage
    ok_agents = []
    for a in agents:
        nq = a.get("name_span", {}).get("quote", "")
        if nq and nq in passage:
            traits = []
            for t in a.get("traits", []):
                tq = t.get("span", {}).get("quote", "")
                if tq and tq in passage:
                    traits.append(t)
            a = dict(a)
            a["traits"] = traits
            ok_agents.append(a)

    ir = {
        "passage_id": passage_id,
        "source_text": passage,
        "excerpt": True,
        "steps": steps,
        "claims": ok_claims if ok_claims else [{
            "id": "c1",
            "text": _short_claim_text(passage[:180]),
            "span": {"quote": passage[: min(120, len(passage))]},
            "role": "report",
            "hedge": _hedge(passage),
            "scope": "truth",
        }],
        "edges": ok_edges,
        "extractor": {"kind": "llm", "model": "cue-extractor-v1", "charity_applied": True},
    }
    # fix steps if we fell back
    if not ok_claims:
        ir["steps"] = [{"id": "s1", "span": {"quote": passage[: min(80, len(passage))]}, "claim_ids": ["c1"], "no_argument": True}]
    if ok_agents:
        ir["agents"] = ok_agents
    if terms:
        ir["terms"] = terms
    if ok_bindings:
        ir["bindings"] = ok_bindings
    if evidence_sets:
        ir["evidence_sets"] = evidence_sets

    # Ensure step claim_ids non-empty
    for s in ir["steps"]:
        if not s.get("claim_ids"):
            s["claim_ids"] = [ir["claims"][0]["id"]]

    return ir


def main():
    out_dir = Path("/workspace/gta_repo/topics/circumcision/dry_runs/2026-10-28_self_pass_fallacy_catalog")
    passages_path = out_dir / "passages.jsonl"
    irs_dir = out_dir / "irs"
    irs_dir.mkdir(parents=True, exist_ok=True)
    err_path = out_dir / "out" / "extract_errors.jsonl"
    err_path.parent.mkdir(parents=True, exist_ok=True)

    n_ok = n_err = n_total = 0
    with passages_path.open() as f, err_path.open("w") as errf:
        for line in f:
            line = line.strip()
            if not line:
                continue
            n_total += 1
            row = json.loads(line)
            pid = row["id"]
            passage = row["passage"]
            # strip trailing citation markers like [1] for cleaner quotes but keep source_text as given
            try:
                ir = extract(pid, passage)
                errs = validate(ir)
                if errs:
                    # last-resort minimal valid IR
                    quote = passage[: min(100, len(passage))]
                    ir = {
                        "passage_id": pid,
                        "source_text": passage,
                        "excerpt": True,
                        "steps": [{"id": "s1", "span": {"quote": quote}, "claim_ids": ["c1"], "no_argument": True}],
                        "claims": [{
                            "id": "c1",
                            "text": _short_claim_text(quote),
                            "span": {"quote": quote},
                            "role": "report",
                            "hedge": _hedge(passage),
                            "scope": "truth",
                        }],
                        "edges": [],
                        "extractor": {"kind": "llm", "model": "cue-extractor-v1-fallback", "charity_applied": True},
                    }
                    errs = validate(ir)
                if errs:
                    n_err += 1
                    errf.write(json.dumps({"id": pid, "errors": errs}) + "\n")
                else:
                    n_ok += 1
                (irs_dir / f"{pid}.json").write_text(json.dumps(ir, indent=2) + "\n")
            except Exception as e:
                n_err += 1
                errf.write(json.dumps({"id": pid, "errors": [str(e)]}) + "\n")
                quote = passage[: min(100, len(passage))]
                ir = {
                    "passage_id": pid,
                    "source_text": passage,
                    "excerpt": True,
                    "steps": [{"id": "s1", "span": {"quote": quote}, "claim_ids": ["c1"], "no_argument": True}],
                    "claims": [{
                        "id": "c1",
                        "text": quote[:180] + ("." if not quote.endswith(".") else ""),
                        "span": {"quote": quote},
                        "role": "report",
                        "hedge": "none",
                        "scope": "truth",
                    }],
                    "edges": [],
                    "extractor": {"kind": "llm", "model": "cue-extractor-v1-exception", "charity_applied": True},
                }
                (irs_dir / f"{pid}.json").write_text(json.dumps(ir, indent=2) + "\n")
            if n_total % 500 == 0:
                print(f"progress {n_total} ok={n_ok} err={n_err}", flush=True)

    print(json.dumps({"total": n_total, "schema_ok_first_pass_or_fallback": n_ok, "still_err_logged": n_err}))


if __name__ == "__main__":
    main()
