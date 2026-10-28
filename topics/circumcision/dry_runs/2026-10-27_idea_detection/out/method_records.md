# METHOD records (idea_detection assist / lead-to-check)

## circ-ashley-montagu-resolution-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-brit-shalom-naming-ceremony-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-circumcision-and-hiv-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-circumcision-and-law-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-circumcision-controversies-01

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Spans cannot support every catalog condition. Do not use this record as a substitute for a hand METHOD review.

Passage: "Proponents, often citing systematic reviews, argue that neonatal circumcision reduces risks of urinary tract infections, penile cancer, and heterosexual HIV acquisition, with bodies like the American Academy of Pediatrics concluding in 2012 that benefits outweigh risks, though not sufficiently to recommend universal adoption."
Strongest reading: Systematic reviews support risk-reduction claims for neonatal circumcision.; Those benefits are not sufficient to recommend universal adoption. -> Neonatal circumcision reduces risks of UTIs, penile cancer, and heterosexual HIV acquisition.; The AAP concluded in 2012 that benefits outweigh risks. (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Appeal to authority (illegitimate) (appeal-to-authority)   Other entries considered: machine rows only, not a hand family review: appeal-to-the-people: no issue; ir_forbid matched: popularity_not_decisive
Conditions:
  1. A claim is supported by what some person or body says. — met by: "citing systematic reviews" (span `appeals_to_source`)
  2. At least one of: the source is not an expert on this question; experts substantially disagree; the source cannot be trusted to be truthful; or the source is misquoted. — not met from a closed span. Open span `experts_substantially_disagree`: "citing systematic reviews" is an outside-text gap, not satisfaction. No quote is treated as meeting this condition. Catalog outside_text_conditions includes this condition.
  3. The authority is treated as settling the matter. — met by: "neonatal circumcision reduces risks of urinary tract infections, penile cancer, and heterosexual HIV acquisition" (span `authority_treated_as_settling`)
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: "neonatal circumcision reduces risks of urinary tract infections, penile cancer, and heterosexual HIV acquisition"
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - Relying on a genuine expert speaking within their field, where experts broadly agree; most reasoning from authority is of this kind. — ir_forbid `source_expert_in_field+passage_reports_expert_agreement` did not match
  - Citing an authority as one piece of evidence among others. — ir_forbid `authority_one_piece_among_others` did not match
Verdict: possible issue (whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted)
Checker reason: possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted

## circ-circumcision-controversies-02

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-circumcision-controversies-03

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-ethics-of-circumcision-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-ethics-of-circumcision-02

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-female-genital-mutilation-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-forced-circumcision-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-foreskin-man-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-foreskin-restoration-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-religion-and-circumcision-01

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Every catalog condition below has a closed in-text span the checker bound. This remains an assist: it does not apply METHOD charity or a second reviewer.

Passage: "The Apostle Paul argued that reliance on circumcision nullifies the benefits of faith in Christ, emphasizing instead a spiritual 'circumcision of the heart' by the Holy Spirit (Romans 2:25-29; Galatians 5:2-6)."
Strongest reading: What matters is a spiritual circumcision of the heart by the Holy Spirit. -> Reliance on circumcision nullifies the benefits of faith in Christ. (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Equivocation (equivocation)   Other entries considered: not produced; no other pilot row carried a match or a forbid hit
Conditions:
  1. A word or phrase occurs more than once in the argument. — met by: "reliance on circumcision" (span `term_occurs_at_least`)
  2. It has one meaning in one place and a different meaning in another (state both). — met by: "reliance on circumcision" (span `sense_shift`)
  3. The conclusion follows only if the meanings are treated as the same. — met by: "reliance on circumcision" (span `conclusion_requires_sense_identity`)
Look-alikes:
  Declared ir_forbid atoms were checked and none matched. A look-alike with no paired ir_forbid atom was not ruled out.
  - The word keeps one meaning throughout (substitute a definition at each use to check). — ir_forbid `single_sense_throughout` did not match
  - Puns or wordplay not offered as argument. — ir_forbid `wordplay_not_argument` did not match
  - When the shifting word is the middle term of a categorical syllogism, report it as equivocation and add '(four terms)'. — no ir_forbid atom is paired with this look-alike; the checker did not rule it out
  - If the key term keeps the same sense but the rule's rationale doesn't fit the case, use accident. — no ir_forbid atom is paired with this look-alike; the checker did not rule it out
Verdict: possible issue (whether the full text supplies the unmet support)
Checker reason: possible issue; excerpt boundary — support may lie outside the passage

## circ-views-on-circumcision-01

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Every catalog condition below has a closed in-text span the checker bound. This remains an assist: it does not apply METHOD charity or a second reviewer.

Passage: "Critics of these rights-based arguments contend that intactivist rhetoric over-relies on anecdotal reports of psychological trauma and body image dissatisfaction, with empirical data from longitudinal studies showing no evidence of widespread mental health harm attributable to neonatal circumcision."
Strongest reading: Intactivist rhetoric cites anecdotal reports of psychological trauma and body image dissatisfaction.; Longitudinal studies' empirical data show no evidence of widespread mental health harm attributable to neonatal circumcision. -> Intactivist rhetoric over-relies on those anecdotal reports.; There is no widespread mental health harm attributable to neonatal circumcision. (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Argument from ignorance (argument-from-ignorance)   Other entries considered: not produced; no other pilot row carried a match or a forbid hit
Conditions:
  1. A claim has not been proven false (or true). — met by: "empirical data from longitudinal studies showing no evidence of widespread mental health harm attributable to neonatal circumcision" (span `exists_claim`)
  2. It is concluded to be true (or false) on that basis. — met by: "showing no evidence of widespread mental health harm" (span `supports`); "showing no evidence of widespread mental health harm" (span `absence_of_proof_used_as_proof`)
  3. Nothing in the context shows a thorough search was made where evidence would be expected if the claim were true. — met by: "empirical data from longitudinal studies showing no evidence of widespread mental health harm attributable to neonatal circumcision" (span `no_thorough_search_shown`)
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: "no evidence of widespread mental health harm attributable to neonatal circumcision"
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - A thorough search was done and a proof would have been found if it existed. — ir_forbid `thorough_search_done` did not match
  - A procedural default or burden rule established independently of this argument (a law, regulation, a null hypothesis or a house rule set beforehand), with the conclusion kept to a decision about what to do rather than asserting that the claim is false. It does not apply if an established standard exists and points the other way. — ir_forbid `procedural_default_action_only` did not match
  - A precautionary decision under uncertainty, stated as a decision, with the costs of being wrong either way weighed. — ir_forbid `precautionary_decision_with_costs_weighed` did not match
Verdict: possible issue (whether the full text supplies the unmet support)
Checker reason: possible issue; excerpt boundary — support may lie outside the passage

## circ-views-on-circumcision-02

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## circ-women-unaffected-by-female-genital-cutting-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.
