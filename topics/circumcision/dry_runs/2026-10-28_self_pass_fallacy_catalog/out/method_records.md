# METHOD records (idea_detection assist / lead-to-check)

## self-IDEA_DETECTION-001

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-002

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-003

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-004

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-005

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-006

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-007

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-008

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-009

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-010

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-011

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-012

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-013

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-IDEA_DETECTION-014

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-001

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-002

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-003

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-004

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-005

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-006

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-007

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Every catalog condition below has a closed in-text span the checker bound. This remains an assist: it does not apply METHOD charity or a second reviewer.

Passage: "**(c) Pick the most specific entry.** Use one label per step. - Check the entry's **Related, use only one per step** list and pick the single entry in that family that fits best. Do not stack labels from the same family. - Entries marked **Fallback** (use_only_if_nothing_more_specific: true), such as non sequitur, false cause and formal fallacy, may be used only when no more specific entry fits. Say which specific entries you considered and why they don't fit. - Some families also give a cross-family tie-break (for example, the selective-evidence family separates suppressed evidence, cherry-picking, Texas sharpshooter, survivorship bias and the lottery fallacy). Follow it. - Two labels in one sentence are allowed only if you can show two separate errors, each meeting its own conditions. Example: 'They've never been proven safe, so they must be what's causing these headaches' contains an argument from ignorance ('never proven safe' treated as showing harm) and a separate causal leap (the headaches blamed on them with no evidence). Both labels may be recorded if each is shown. - **Cross-family ties.** Some ties cross families; follow these rules: - Ambiguity vs accident: if the key term changes sense between the rule and the case, use equivocation; if it keeps the same sense but the rule's rationale doesn't fit the case, use accident. - Causal alternatives: follow the order in the causation family rule (Simpson's paradox when the passage gives a reversing breakdown; then an identifiable common cause, then reverse direction, then cum hoc; observational interpretation when the study design is the problem). - Nature vs tradition: naturalness or 'built for' wording is appeal to nature; age or history alone is appeal to tradition; if both appear in one step, report appeal to nature and note tradition. - Probability: follow the probability family rule (prosecutor's fallacy, base-rate fallacy, confusion of the inverse). - Generalization vs comparison: an exceptional source case (a special population or special circumstances) used to set a rule for ordinary cases or for everyone is converse accident; one case carried over to another comparable case is false analogy. - Experts disagreeing: 'experts disagree, so nothing can be known' is inflation of conflict; a claim that simply ignores well-established findings is disregarding known science. - **Separate steps get separate rows.** A step that builds on an earlier error gets its own row if it commits a separate move of its own. Adjacent sentences are two steps when each meets its own entry. Example: 'It's up to the county to prove the plant is safe. They haven't, so it isn't' contains a burden demand (misplaced burden of proof) and a conclusion from lack of proof (argument from ignorance); record both if each is shown. - **Weak premises without a label.** A second weak link in a chain gets its own row only if it meets an entry's conditions. Otherwise note it as 'weak premise' without a fallacy label. - **Charged wording is not a second error.** Loaded words in the same step as a flagged error are not a second flag unless they carry their own inference. - **Reporting names.** Use the entry's name, not an alias. Where a family rule says to report under a familiar name with a qualifier, do so: a shift of meaning in a syllogism's middle term is reported as 'equivocation (four terms)'."
Strongest reading: P bias and the lottery fallacy). Follow it. - Two labels in one sentence are allowed only if you can show two separate errors, each meeting its own conditions.; No evidence.; Per step.; Per step** list and pick the single entry in that family that fits best.; One label per step. -> : a shift of meaning in a syllogism's middle term is reported as "equivocation (four terms)". (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Argument from ignorance (argument-from-ignorance)   Other entries considered: machine rows only, not a hand family review: appeal-to-authority: no issue; ir_forbid matched: authority_one_piece_among_others; appeal-to-the-people: no issue; ir_forbid matched: popularity_one_piece_among_others
Conditions:
  1. A claim has not been proven false (or true). — met by: "no evidence" (span `exists_claim`)
  2. It is concluded to be true (or false) on that basis. — met by: "no evidence" (span `supports`); "no evidence" (span `absence_of_proof_used_as_proof`)
  3. Nothing in the context shows a thorough search was made where evidence would be expected if the claim were true. — met by: "no evidence" (span `no_thorough_search_shown`)
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: ": a shift of meaning in a syllogism's middle term is reported as 'equivocation (four terms)'."
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - A thorough search was done and a proof would have been found if it existed. — ir_forbid `thorough_search_done` did not match
  - A procedural default or burden rule established independently of this argument (a law, regulation, a null hypothesis or a house rule set beforehand), with the conclusion kept to a decision about what to do rather than asserting that the claim is false. It does not apply if an established standard exists and points the other way. — ir_forbid `procedural_default_action_only` did not match
  - A precautionary decision under uncertainty, stated as a decision, with the costs of being wrong either way weighed. — ir_forbid `precautionary_decision_with_costs_weighed` did not match
Verdict: possible issue (whether the full text supplies the unmet support)
Checker reason: possible issue; excerpt boundary — support may lie outside the passage

## self-METHOD-008

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-009

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-010

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-011

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-012

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Spans cannot support every catalog condition. Do not use this record as a substitute for a hand METHOD review.

Passage: "**(h) Recommended: a second reviewer.** A second reviewer, who has not seen the first reviewer's verdicts, re-checks each flag using steps (a) to (g). Report only the flags both reviewers agree on; list the disagreements separately as possible issues. - If both reviewers flag the same step but with different entries, report the flag, list both names as 'label disputed', and resolve it with the family or cross-family tie-break. If the names are still split, report the more general of the two entries."
Strongest reading: Who. -> **(h) Recommended: a second reviewer.** A second reviewer, who has not seen the first reviewer's verdicts, re-checks each flag using steps (a) to (g). Report on. (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Appeal to authority (illegitimate) (appeal-to-authority)   Other entries considered: not produced; no other pilot row carried a match or a forbid hit
Conditions:
  1. A claim is supported by what some person or body says. — met by: "who" (span `appeals_to_source`)
  2. At least one of: the source is not an expert on this question; experts substantially disagree; the source cannot be trusted to be truthful; or the source is misquoted. — not met from a closed span. Open span `source_not_expert_on_question`: "who" is an outside-text gap, not satisfaction. No quote is treated as meeting this condition. Catalog outside_text_conditions includes this condition.
  3. The authority is treated as settling the matter. — met by: "**(h) Recommended: a second reviewer.** A second reviewer, who has not seen the first reviewer's verdicts, re-checks each flag using steps (a) to (g). Report on" (span `authority_treated_as_settling`)
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: "**(h) Recommended: a second reviewer.** A second reviewer, who has not seen the first reviewer's verdicts, re-checks each flag using steps (a) to (g). Report on"
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - Relying on a genuine expert speaking within their field, where experts broadly agree; most reasoning from authority is of this kind. — ir_forbid `source_expert_in_field+passage_reports_expert_agreement` did not match
  - Citing an authority as one piece of evidence among others. — ir_forbid `authority_one_piece_among_others` did not match
Verdict: possible issue (whether the source is an expert on this question; whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted)
Checker reason: possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted

## self-METHOD-013

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-014

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-015

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-016

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-017

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-018

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-019

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-020

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-021

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-METHOD-022

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Spans cannot support every catalog condition. Do not use this record as a substitute for a hand METHOD review.

Passage: "Look-alikes: relying on genuine experts within their field who broadly agree, which is the case the source says most appeals to authority fall under, applies here."
Strongest reading: Who. -> Look-alikes: relying on genuine experts within their field who broadly agree, which is the case the source says most appeals to authority fall under, applies he. (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Appeal to authority (illegitimate) (appeal-to-authority)   Other entries considered: not produced; no other pilot row carried a match or a forbid hit
Conditions:
  1. A claim is supported by what some person or body says. — met by: "who" (span `appeals_to_source`)
  2. At least one of: the source is not an expert on this question; experts substantially disagree; the source cannot be trusted to be truthful; or the source is misquoted. — not met from a closed span. Open span `source_not_expert_on_question`: "who" is an outside-text gap, not satisfaction. No quote is treated as meeting this condition. Catalog outside_text_conditions includes this condition.
  3. The authority is treated as settling the matter. — met by: "Look-alikes: relying on genuine experts within their field who broadly agree, which is the case the source says most appeals to authority fall under, applies he" (span `authority_treated_as_settling`)
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: "Look-alikes: relying on genuine experts within their field who broadly agree, which is the case the source says most appeals to authority fall under, applies he"
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - Relying on a genuine expert speaking within their field, where experts broadly agree; most reasoning from authority is of this kind. — ir_forbid `source_expert_in_field+passage_reports_expert_agreement` did not match
  - Citing an authority as one piece of evidence among others. — ir_forbid `authority_one_piece_among_others` did not match
Verdict: possible issue (whether the source is an expert on this question; whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted)
Checker reason: possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted

## self-METHOD-023

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-001

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-002

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-003

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-004

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-005

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-006

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-007

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-008

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-009

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-010

idea_detection assist / lead-to-check
Machine output from the deterministic checker joined to fallacies.json. Not a hand METHOD record. Spans cannot support every catalog condition. Do not use this record as a substitute for a hand METHOD review.

Passage: "5. **Association, no person-attack required.** Passage: “This housing plan is associated with a developer who once supported the last failure, so it must be a bad plan.” Emit an agent trait (“associated with” / “once supported”), supports into “must be a bad plan”, and ignores if an object-level reason is brushed aside. attacks_person is optional and not required."
Strongest reading: 5. **Association, no person-attack required.** Passage: “This housing plan is associated with a developer who once supported the last failure.; It must be a bad plan.” Emit an agent trait (“associated with” / “once supported”), supports into “must be a bad plan”, and ignores if an object-level reason is.; Who.; Associated with a developer who once supported the last failure.; This housing plan is associated with a developer who once support. -> (no conclusion claim text) (Idea IR claim texts, not a hand METHOD strongest reading)
Entry: Guilt by association (guilt-by-association)   Other entries considered: machine rows only, not a hand family review: appeal-to-authority: no issue; ir_forbid matched: authority_one_piece_among_others; appeal-to-the-people: no issue; ir_forbid matched: popularity_one_piece_among_others
Conditions:
  1. A person or claim is linked to a group, person or idea that the audience dislikes. — met by: "associated with a developer who once supported the last failure" (span `exists_agent_trait`); "associated with a developer who once supported the last failure" (span `trait_is_association`)
  2. The link is offered as a reason to reject the claim or condemn the person. — met by: "so" (span `supports`); "it must be a bad plan.” Emit an agent trait (“associated with” / “once supported”), supports into “must be a bad plan”, and ignores if an object-level reason is" (span `association_used_as_evaluative_reason`)
  3. No evidence is given that the association bears on the specific claim. — not span-mapped. No pilot span is declared for this catalog condition. No quote is attached.
Spans not assigned to a catalog condition (not used as met-by):
  - closed span `exists_claim`: "it must be a bad plan.” Emit an agent trait (“associated with” / “once supported”), supports into “must be a bad plan”, and ignores if an object-level reason is"
Look-alikes:
  Look-alikes were checked via ir_forbid and none matched.
  - The association is real evidence about the specific claim or about a witness's reliability. — ir_forbid `association_bears_on_the_claim` did not match
  - Showing that someone actually shares the specific commitment being criticised. — ir_forbid `shares_the_criticised_commitment` did not match
  ir_forbid atoms with no catalog look-alike line: `independent_merits_engaged`, `association_mere_disclosure`. They were checked and none matched. They are not a prose rule-out of an unpaired look-alike.
Verdict: possible issue (whether the full text supplies the unmet support)
Checker reason: possible issue; excerpt boundary — support may lie outside the passage

## self-idea_detection-EXTRACTOR_PROMPT-011

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-EXTRACTOR_PROMPT-012

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-001

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-002

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-003

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-004

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-005

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-006

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-007

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-008

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-009

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-010

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-011

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-012

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-013

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-014

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-015

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-016

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-017

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-018

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-019

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-020

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-021

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-022

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-023

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-024

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-025

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-026

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-027

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-028

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-029

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-IDEA_LEVEL_DETECTION-030

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-001

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-002

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-003

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-004

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-005

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-006

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-007

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-008

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-009

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-010

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-011

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-012

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-013

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-014

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-015

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-016

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-017

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-idea_detection-NESTED_LAYERS-018

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.

## self-pilot-pattern_language-note-01

No record. The checker did not emit a flag or possible issue row for this passage. Pattern misses are not rendered.
