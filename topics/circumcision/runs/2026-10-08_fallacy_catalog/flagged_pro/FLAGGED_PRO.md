# Step 6: the flagged pro arguments in the male circumcision articles (2026-10-08)

This is the last step of the benchmark. It covers the **male circumcision articles only**: 39 of the 58 articles. FGM articles are not part of this step. It takes every **pro** argument sentence there that lost at least one point in step 5 ([`../survival/`](../survival/)), meaning at least one of the three AI reviewers flagged it. Then it asks what kinds of flawed reasoning those flags name, how each kind works, and what reply exposes it.

Read this with the limits in mind. **Flags are leads, not verdicts**: each one is an AI reviewer's judgment against [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog) v0.6.1. The three reviewers were **not blind** (later reviewers' instructions mentioned earlier results). The pro/anti labels came from an **AI model, not a person**. A flagged sentence may still have a true conclusion; the flag is about the step from reason to conclusion. How this was built: [METHOD.md](METHOD.md). Full table: [flagged_pro.csv](flagged_pro.csv).

## Scope

- **61** flagged pro argument sentences in the male circumcision articles: 26 with 2 points left, 15 with 1 and 20 with 0 (flagged by all three reviewers).
- Out of scope: FGM articles, and anti arguments (only 4 anti sentences in the male circumcision articles lost a point).

## Types: shares by family

Each catalog entry belongs to one of the catalog's own categories, used here as the families. **Primary family** gives each sentence one family (the one the most reviewers named; see METHOD.md), so the shares add to 100%. **Any hit** counts a sentence once for every family any reviewer named, so those shares can add to more than 100%.

| Family (catalog category) | What it means | Primary | Any hit |
|---|---|---|---|
| **Off-point reasons** (`informal: relevance`) | the reason given does not bear on the point at issue | 28 (46%) | 28 (46%) |
| **Unearned or clashing premises** (`informal: presumption`) | the step rests on a premise that is assumed, dropped a qualification, or clashes with the article itself | 20 (33%) | 22 (36%) |
| **Thin or ill-fitting evidence** (`informal: weak induction`) | the evidence is real but too thin, too selective or too unlike the case to carry the conclusion | 9 (15%) | 9 (15%) |
| **Stretched numbers** (`informal: statistical and probabilistic`) | a figure is carried beyond the data it came from, or only what is measurable is allowed to count | 2 (3%) | 7 (11%) |
| **Shaky cause and effect** (`informal: causal`) | a trend or a correlation is read as proof of cause while a rival cause is left open | 2 (3%) | 3 (5%) |

7 sentences were hit by more than one family; 5 needed the tie-break to pick a primary family.

Family lines are soft. The same move, carrying HIV trial results from adult men to infant circumcision in general, was named secundum quid (presumption) by one reviewer and over-extrapolation (stretched numbers) by another. That is why stretched numbers is named on more sentences than it is primary for.

## Off-point reasons (`informal: relevance`)

Primary family for 28 of 61 flagged pro sentences (46%); named at all on 28.

### Mechanics

In short, the reason given does not bear on the point at issue. The entries the reviewers used in this family, with the catalog's own definition (sentences hit in brackets):

- [Non sequitur](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#non-sequitur) (10): A conclusion that doesn't follow from the reasons given, because they are irrelevant to it or far too weak.
- [Straw man](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#straw-man) (6): Misrepresenting someone's position as a weaker or more extreme version and then attacking that version instead of what they actually hold.
- [Irrelevant conclusion](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#irrelevant-conclusion) (5): Offering an argument that may be fine in itself but supports a different conclusion from the one at issue.
- [Appeal to tradition](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#appeal-to-tradition) (3): Arguing that a practice or belief is right because it has long been held or done.
- [Genetic fallacy](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#genetic-fallacy) (2): Judging a claim or practice good or bad by where it came from rather than by its present merits.
- [Appeal to authority (illegitimate)](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#appeal-to-authority) (1): Accepting a claim because someone said it when that person is not a genuine expert on the question, the experts disagree, or the authority is being treated as settling the matter regardless of the evidence.
- [Appeal to motive](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#appeal-to-motive) (1): Dismissing an argument by questioning why its proponent is making it.
- [Appeal to the people](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#appeal-to-the-people) (1): Arguing that a claim is true, or a practice right, simply because many or most people believe or do it.
- [Bulverism](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#bulverism) (1): Assuming a view is wrong and then explaining why the other person holds it (their bias, psychology or upbringing) instead of showing that it is wrong.
- [Circumstantial ad hominem](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#circumstantial-ad-hominem) (1): Arguing that a claim is false, or a proposal should be rejected, because of the arguer's circumstances, such as what they stand to gain, rather than on the merits.
- [Guilt by association](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#guilt-by-association) (1): Judging a claim or person by the company they keep or the groups they're linked to, rather than on the merits.
- [Poisoning the well](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#poisoning-the-well) (1): Discrediting a person in advance, before they speak, so that anything they say will be dismissed.
- [Red herring](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#red-herring) (1): Bringing in an irrelevant topic to divert attention from the issue under discussion.
- [Relative privation](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#relative-privation) (1): Dismissing a problem or complaint because worse problems exist elsewhere.

### Quotes

Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.

> While some evidence suggests unmitigated neonatal pain may heighten responses to later vaccinations, the procedure's brevity and rapid healing—typically within one week—limit long-term sequelae in healthy infants. [65] [66]
>
> `brit-milah` s0138 · **0 of 3 points left** · flagged by R1: Non sequitur; R2: Non sequitur; R3: Non sequitur

> However, these initiatives have faced setbacks due to insufficient evidence of harm in population-level data, with surveys indicating that adult circumcised men report satisfaction rates comparable to uncircumcised peers, suggesting that consent-based objections may not align with observed outcomes.
>
> `views-on-circumcision` s0125 · **0 of 3 points left** · flagged by R1: Irrelevant conclusion; R2: Irrelevant conclusion; R3: Irrelevant conclusion

> Mainstream portrayals tend to prioritize autonomy arguments against non-consensual procedures, reflecting institutional biases toward secular norms, while underrepresenting the ritual's centrality to Jewish continuity amid declining circumcision rates among non-religious U.S. Jews (from 90% in the 1970s to about 70% by 2020).
>
> `mohel` s0231 · **0 of 3 points left** · flagged by R1: Bulverism; R2: Appeal to motive; R3: Bulverism

> While these values sustain cultural continuity—practiced by over 80% of Xhosa males as of recent surveys—they have drawn critique for entrenching hierarchical gender expectations, such as male primacy in provision, potentially at odds with egalitarian modern ideals, yet empirical persistence underscores their adaptive fit within enduring Xhosa social fabrics. [7]
>
> `ulwaluko` s0097 · **0 of 3 points left** · flagged by R1: Appeal to tradition; R2: Appeal to tradition; R3: Appeal to tradition

### Effective counter

**From the catalog.** The catalog has no separate "counter" field. An entry applies only when all its required conditions hold, so the reply is to test the condition the flag rests on, and its legitimate look-alikes say what a sound version of the step would look like. Catalog wording:

- [Non sequitur](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#non-sequitur). Required: "The reasons are irrelevant to it or extremely weak (state the missing link)." Legitimate look-alike (what would answer the flag): "An enthymeme whose unstated premise is obvious and acceptable."
- [Irrelevant conclusion](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#irrelevant-conclusion). Required: "The argument supports a different conclusion." Legitimate look-alike (what would answer the flag): "Evidence relevant to a related question (such as leniency rather than guilt), offered for that question."
- [Straw man](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#straw-man). Required: "The restatement differs materially from what they said or meant (show the original wording or a reliable summary of it; without it, at most possible issue)." Legitimate look-alike (what would answer the flag): "Restating a view in words its holder would accept."
- [Bulverism](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#bulverism). Required: "The explanation is offered in place of showing that the view is wrong." Legitimate look-alike (what would answer the flag): "Explaining why someone holds a view after the view has been shown to be wrong on independent grounds."
- [Appeal to tradition](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#appeal-to-tradition). Required: "Its age is treated as sufficient reason, with no account of why it works or is right." Legitimate look-alike (what would answer the flag): "A long record can be some evidence that a practice works; the error is treating age as enough."

**This audit's wording** (not from the catalog): Name the question actually at issue, then ask what links the reason to it. Low complication rates answer "is it safe?", not "who should decide?". If an opponent's view is restated, set their own words (usually given elsewhere in the same article) beside the restatement. If a view is explained by its holders' motives, source or long history, ask for the error in the view itself.

## Unearned or clashing premises (`informal: presumption`)

Primary family for 20 of 61 flagged pro sentences (33%); named at all on 22.

### Mechanics

In short, the step rests on a premise that is assumed, dropped a qualification, or clashes with the article itself. The entries the reviewers used in this family, with the catalog's own definition (sentences hit in brackets):

- [Inconsistency](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#inconsistency) (9): Relying on two or more claims that cannot all be true, as if all of them supported the conclusion, without noticing the conflict.
- [Secundum quid](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#secundum-quid) (7): Aristotle's fallacy of treating something true only in a certain respect, or with a qualification, as if it were true without qualification.
- [Double standard](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#double-standard) (5): Judging two relevantly similar people or cases by different standards.
- [Begging the question](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#begging-the-question) (1): Supporting a conclusion with a premise that is only acceptable to someone who already accepts the conclusion, so the argument gives no independent reason. Includes arguing in a circle, where the conclusion reappears, openly or reworded, among the premises.
- [Far-fetched hypothesis](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#far-fetched-hypothesis) (1): Offering a bizarre explanation as the correct one without first ruling out simpler, more likely explanations.
- [No true Scotsman](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#no-true-scotsman) (1): Protecting a generalization from a counterexample by redefining the group so that the counterexample doesn't count.

### Quotes

Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.

> Neonatal circumcision in the first week enables near-painless outcomes under optimal blocks, given lower pre-phimosis sensitivity. [39]
>
> `circumcision` s0060 · **0 of 3 points left** · flagged by R1: Inconsistency; R2: Inconsistency; R3: Inconsistency

> Anti-circumcision claims often use observational data, contrasting RCT strength and highlighting the value of causal over correlative evidence. [251] [245]
>
> `circumcision` s0459 · **0 of 3 points left** · flagged by R1: Double standard; R2: Double standard; R3: Double standard

> Empirical audits reveal that core ritual elements under qualified custodians exhibit fewer failures, with escalated risks tracing primarily to modern encroachments such as fee-based, unregulated schools rather than inherent procedural flaws.
>
> `ulwaluko` s0147 · **0 of 3 points left** · flagged by R1: Inconsistency; R2: No true Scotsman; R3: Inconsistency

### Effective counter

**From the catalog.** The catalog has no separate "counter" field. An entry applies only when all its required conditions hold, so the reply is to test the condition the flag rests on, and its legitimate look-alikes say what a sound version of the step would look like. Catalog wording:

- [Inconsistency](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#inconsistency). Required: "They cannot all be true together (show the clash)." Legitimate look-alike (what would answer the flag): "Apparent conflicts that disappear on a fair reading (different times, respects or senses)."
- [Double standard](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#double-standard). Required: "The same standard should apply because they are alike in the relevant respects." Legitimate look-alike (what would answer the flag): "The cases differ in a relevant way, so different standards are justified."
- [Secundum quid](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#secundum-quid). Required: "The conclusion relies on dropping the qualification." Legitimate look-alike (what would answer the flag): "The qualification does not affect the conclusion."

**This audit's wording** (not from the catalog): Put the two clashing claims side by side, often from the same article, and ask which one holds. Apply the stated test, for example "observational data are weak", to both sides' evidence. Restore the dropped qualification (which ages, which setting, which procedure) and check whether the conclusion still follows.

## Thin or ill-fitting evidence (`informal: weak induction`)

Primary family for 9 of 61 flagged pro sentences (15%); named at all on 9.

### Mechanics

In short, the evidence is real but too thin, too selective or too unlike the case to carry the conclusion. The entries the reviewers used in this family, with the catalog's own definition (sentences hit in brackets):

- [False analogy](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#false-analogy) (5): Arguing that because two things are alike in some ways they are alike in another way, when the similarities are not relevant to that point or the differences matter more.
- [Argument from ignorance](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#argument-from-ignorance) (1): Treating a lack of disproof as proof, or a lack of proof as disproof.
- [Argument from silence](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#argument-from-silence) (1): Drawing a conclusion from the absence of a statement or record, when that absence has other likely explanations.
- [Cherry-picking](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#cherry-picking) (1): Drawing a conclusion from a selected part of the evidence while the rest of it, which is stated or plainly known, points the other way or weakens it and goes unanswered. Unlike suppressed evidence, the contrary evidence is in plain view.
- [Nut-picking](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#nut-picking) (1): Finding the most extreme or fringe members of an opposing group and presenting them as typical of the whole group.
- [Suppressed evidence](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#suppressed-evidence) (1): Leaving out evidence that is significant and would weaken the conclusion, when the arguer had it or should have had it, and presenting the case as if it were complete.

### Quotes

Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.

> Critiques framing infant circumcision as inherently non-therapeutic, thus presumptively harmful, falter against precedents in preventive pediatric medicine, where procedures like heel-stick blood sampling for newborn metabolic screening inflict comparable or greater procedural pain yet are standard due to utility in averting conditions like phenylketonuria, which untreated causes intellectual disability in 1:10,000-15,000 births. [67]
>
> `ethics-of-circumcision` s0106 · **0 of 3 points left** · flagged by R1: False analogy; R2: False analogy; R3: False analogy

> This contextual reading prioritizes verifiable health outcomes over absolutist interpretations of bodily integrity, as the UNCRC's silence on condemnation reflects an acknowledgment that proxy parental decisions can align with overall child welfare when risks are minimized through sterile procedures. [176] [177]
>
> `ethics-of-circumcision` s0302 · **0 of 3 points left** · flagged by R1: Argument from silence; R2: Argument from ignorance; R3: Argument from ignorance

> In 2012, intactivists coordinated negative Amazon reviews to demote a book synthesizing evidence for circumcision's role in HIV control, illustrating ideological efforts to suppress data-driven discourse over scientific merit. [132]
>
> `circumcision-in-africa` s0285 · **1 of 3 points left** · flagged by R1: Nut-picking; R2: Nut-picking

### Effective counter

**From the catalog.** The catalog has no separate "counter" field. An entry applies only when all its required conditions hold, so the reply is to test the condition the flag rests on, and its legitimate look-alikes say what a sound version of the step would look like. Catalog wording:

- [False analogy](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#false-analogy). Required: "They differ in a respect relevant to the conclusion (state it)." Legitimate look-alike (what would answer the flag): "An analogy where the shared features are the ones that matter to the conclusion."
- [Argument from ignorance](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#argument-from-ignorance). Required: "It is concluded to be true (or false) on that basis." Legitimate look-alike (what would answer the flag): "A thorough search was done and a proof would have been found if it existed."
- [Argument from silence](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#argument-from-silence). Required: "There is no strong reason to expect the source would have mentioned it." Legitimate look-alike (what would answer the flag): "The source would very likely have mentioned it if it were so."
- [Nut-picking](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#nut-picking). Required: "They are presented as representing the whole group." Legitimate look-alike (what would answer the flag): "Examples that are shown to be typical."

**This audit's wording** (not from the catalog): Name the difference between the two cases that matters to the conclusion. Ask whether the cases shown stand for the whole group they are used to describe. Silence or a missing condemnation is not evidence of approval.

## Stretched numbers (`informal: statistical and probabilistic`)

Primary family for 2 of 61 flagged pro sentences (3%); named at all on 7.

### Mechanics

In short, a figure is carried beyond the data it came from, or only what is measurable is allowed to count. The entries the reviewers used in this family, with the catalog's own definition (sentences hit in brackets):

- [Over-extrapolation](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#over-extrapolation) (5): Extending a trend far beyond the range of data that support it, as if it would continue indefinitely.
- [McNamara fallacy](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#mcnamara-fallacy) (1): Deciding only on what can easily be measured and treating what can't be measured as unimportant or nonexistent.
- [Relative-risk framing (absolute risk left out)](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#relative-risk-framing) (1): Presenting a change in risk only as a relative figure ('halves the risk', '50% more likely') when the absolute change is small, so the effect seems larger or more important than it is.

### Quotes

Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.

> Prioritizing observable utilities over subjective proxies, the procedure's net causal effect favors reduced disease transmission over unsubstantiated pleasure deficits.
>
> `circumcision-controversies` s0128 · **2 of 3 points left** · flagged by R1: McNamara fallacy

> Systematic reviews of these trials and observational data affirm the mechanism involves keratinization of the glans and reduced viral entry sites under the foreskin, conferring lifelong protection when performed neonatally, as evidenced by lower HIV prevalence in circumcised populations. [62]
>
> `mohel` s0122 · **0 of 3 points left** · flagged by R1: Secundum quid; R2: Cum hoc ergo propter hoc; R3: Over-extrapolation

> However, this framing overlooks its preventive classification in contexts analogous to vaccines, where interventions target rare but severe outcomes with net benefits; for instance, systematic reviews affirm circumcision reduces UTI risk by 90% in infancy and heterosexual HIV acquisition by 50-60% based on randomized controlled trials (RCTs) in high-prevalence settings, benefits that scale population-wide despite low baseline risks. [1] [125]
>
> `ethics-of-circumcision` s0198 · **0 of 3 points left** · flagged by R1: Relative-risk framing (absolute risk left out); R2: False analogy; R3: False analogy

### Effective counter

**From the catalog.** The catalog has no separate "counter" field. An entry applies only when all its required conditions hold, so the reply is to test the condition the flag rests on, and its legitimate look-alikes say what a sound version of the step would look like. Catalog wording:

- [Over-extrapolation](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#over-extrapolation). Required: "No reason is given to think the trend continues there." Legitimate look-alike (what would answer the flag): "Short-range forecasts with stated uncertainty, or extrapolation backed by a model of why the trend continues."
- [McNamara fallacy](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#mcnamara-fallacy). Required: "It is ignored or dismissed because it is hard to measure." Legitimate look-alike (what would answer the flag): "The measured thing is the thing that matters."
- [Relative-risk framing (absolute risk left out)](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#relative-risk-framing). Required: "The conclusion relies on the relative figure." Legitimate look-alike (what would answer the flag): "Both the relative and the absolute figures are given and weighed."

**This audit's wording** (not from the catalog): Ask where the figure comes from (ages, setting, procedure, follow-up time) and whether the conclusion stays inside that range. Ask for absolute numbers next to relative ones. Ask what was left out because it is hard to measure.

## Shaky cause and effect (`informal: causal`)

Primary family for 2 of 61 flagged pro sentences (3%); named at all on 3.

### Mechanics

In short, a trend or a correlation is read as proof of cause while a rival cause is left open. The entries the reviewers used in this family, with the catalog's own definition (sentences hit in brackets):

- [Cum hoc ergo propter hoc](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#cum-hoc) (2): Concluding that because two things occur together, one causes the other.
- [False cause](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#false-cause) (1): Concluding that one thing causes another when the only support is that they occur together or in sequence, or when an obvious alternative explanation (a common cause, reversed direction, or chance) has not been ruled out.
- [Post hoc ergo propter hoc](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#post-hoc) (1): Concluding that because B happened after A, A caused B.

### Quotes

Verbatim from the 2026-10-01 snapshots, checked by script. Citation markers are part of the text.

> In high-risk African settings, VMMC interventions have demonstrated epidemiological causality through time-series declines in incidence post-uptake, exceeding expectations from behavioral interventions alone, whereas low-prevalence contexts like Europe show minimal marginal gains due to already subdued transmission dynamics. [56]
>
> `circumcision-controversies` s0073 · **0 of 3 points left** · flagged by R1: Post hoc ergo propter hoc; R2: Post hoc ergo propter hoc; R3: Post hoc ergo propter hoc

> Program evaluations confirm population-level HIV incidence declines correlating with VMMC scale-up, independent of confounding factors like antiretroviral therapy expansion.
>
> `prevalence-of-circumcision` s0058 · **0 of 3 points left** · flagged by R1: False cause; R2: Cum hoc ergo propter hoc; R3: Cum hoc ergo propter hoc

### Effective counter

**From the catalog.** The catalog has no separate "counter" field. An entry applies only when all its required conditions hold, so the reply is to test the condition the flag rests on, and its legitimate look-alikes say what a sound version of the step would look like. Catalog wording:

- [Post hoc ergo propter hoc](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#post-hoc). Required: "The order in time is the main or only evidence offered." Legitimate look-alike (what would answer the flag): "Timing plus a known mechanism or controlled comparison."
- [Cum hoc ergo propter hoc](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#cum-hoc). Required: "At least one plausible alternative (chance, a third factor, the reverse direction) is left open, and the causal claim is stated as established rather than as a hypothesis to test." Legitimate look-alike (what would answer the flag): "A correlation can support a causal conclusion once coincidence, a confounding cause and the reverse direction have been ruled out."
- [False cause](https://github.com/neuresthetics/fallacy_catalog/blob/2a56493a3931018e9143bc7235f152f5cc5b459e/FALLACIES.md#false-cause). Required: "The only support is that the two occur together or in sequence, or an obvious alternative (a common cause, the reverse direction, chance) is left open." Legitimate look-alike (what would answer the flag): "A tentative causal hypothesis offered for testing."

**This audit's wording** (not from the catalog): Name a rival cause running at the same time and ask how it was ruled out. The second quote names one itself (antiretroviral therapy expansion) and states, without showing how, that the decline is independent of it. A trend that moves with a programme is a reason to test for cause, not proof of it.

## Files

- [flagged_pro.csv](flagged_pro.csv): every flagged pro sentence, with group, points left, reviewers, primary family, all families, catalog entries and the verbatim text.
- [summary.json](summary.json): the counts above.
- [catalog_entries_v0.6.1.json](catalog_entries_v0.6.1.json): verbatim catalog fields used for the definitions and counters.
- [METHOD.md](METHOD.md) and [scripts/build_flagged_pro.py](scripts/build_flagged_pro.py).
- Chart: `docs/img/circumcision/2026-10-08/06_flagged_pro_types.png`.
