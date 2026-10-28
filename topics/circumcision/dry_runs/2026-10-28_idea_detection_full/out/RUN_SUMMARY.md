# RUN_SUMMARY — idea_detection full circ inventory (2026-10-28)

**Date:** 2026-10-28 (America/Los_Angeles)
**Tip commit:** `bfcbc8b` (`fallacy_catalog` main; PR #7 squash-merged)
**Passages:** `topics/circumcision/dry_runs/2026-10-28_idea_detection_full/passages_from_inventory.jsonl` (2616 lines; symlinked as `passages.jsonl`)
**Source:** Oct 8 survival `argument_inventory.csv` (pro/anti), not a raw snapshot carve
**Package:** not modified (read-only check + render)
**Git:** local only under gta_repo; **not pushed**; tree left untracked/dirty as found

## Pilot coverage caveat

Only entries with patterns in `idea_detection/pilot_ir_patterns.json` can fire (13 pilots today: ad-hominem, appeal-to-authority, equivocation, false-cause, begging-the-question, cherry-picking, straw-man, argument-from-ignorance, hasty-generalization, slippery-slope, false-dilemma, appeal-to-the-people, guilt-by-association). Most catalog entries cannot flag yet. A `no_issue` row means “this pilot pattern did not match,” not “the passage is fallacy-free.”

Every METHOD-shaped record below is an **assist / lead-to-check**, not a hand METHOD verdict. Spans cannot support every catalog condition; outside-text gaps and excerpt boundaries cap matches at `possible_issue`.

## Counts

| Metric | N |
| --- | ---: |
| Passages | 2616 |
| Idea IR files written / schema-ok | 2616 / 2616 |
| Extract / load errors | 0 |
| Checker report ok | 2616 |
| Atom rows: `flag` | 0 |
| Atom rows: `possible_issue` | 452 |
| Atom rows: `no_issue` | 33556 |
| Passages with any flag | 0 |
| Passages with any possible_issue | 450 |
| Passages with only no_issue (pilots) | 2166 |

### possible_issue by entry

| Entry | N |
| --- | ---: |
| `appeal-to-authority` | 426 |
| `argument-from-ignorance` | 18 |
| `false-cause` | 6 |
| `begging-the-question` | 2 |

## Flags

No `flag` rows (excerpt boundary + outside-text caps keep hard flags at zero for this set).

## Possible issues (leads to check)

Full machine list also in `out/leads.json` and `out/method_records.jsonl` (452 rows).

| Passage id | Entry | Why capped / note |
| --- | --- | --- |
| `circ-ashley-montagu-resolution-s0032` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0046` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0053` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-ashley-montagu-resolution-s0130` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0159` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0163` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0176` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ashley-montagu-resolution-s0197` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0199` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0203` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0207` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0216` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ashley-montagu-resolution-s0232` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0204` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0208` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-brit-milah-s0211` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0212` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0213` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0216` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-brit-milah-s0222` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-brit-milah-s0240` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-brit-milah-s0244` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0260` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0275` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-brit-milah-s0289` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0290` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0291` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0292` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0316` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-milah-s0334` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-shalom-naming-ceremony-s0029` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-shalom-naming-ceremony-s0085` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-shalom-naming-ceremony-s0088` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-brit-shalom-naming-ceremony-s0089` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-children-act-1989-amendment-female-genital-mutilation-act-2019-s0076` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-children-act-1989-amendment-female-genital-mutilation-act-2019-s0079` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-children-act-1989-amendment-female-genital-mutilation-act-2019-s0083` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-children-act-1989-amendment-female-genital-mutilation-act-2019-s0141` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0001` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0003` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0020` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-and-hiv-s0026` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0027` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0030` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0035` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0039` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0047` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0048` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0052` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0053` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0056` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0066` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0091` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0095` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0096` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0098` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0103` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0138` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0156` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0164` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-and-hiv-s0167` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0170` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0170` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-and-hiv-s0177` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0178` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-and-hiv-s0183` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0186` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0191` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0195` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0198` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0222` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0224` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0229` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0245` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0247` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-and-hiv-s0249` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-and-hiv-s0251` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0252` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0260` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0269` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0273` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0274` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-hiv-s0278` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0003` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0066` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0117` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0205` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0306` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0327` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0346` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0385` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0395` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-and-law-s0398` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0036` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0037` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0041` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-controversies-s0044` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0046` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0057` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0065` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0086` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0087` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0091` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0093` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0117` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversies-s0125` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-controversies-s0192` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversy-in-early-christianity-s0070` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-controversy-in-early-christianity-s0089` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0005` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0005` | begging-the-question | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-in-africa-s0138` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0151` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0169` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0172` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0183` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0209` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0216` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0217` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0220` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0223` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0225` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0228` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0231` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0240` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-in-africa-s0241` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0275` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-africa-s0284` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-in-brunei-s0049` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0047` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0077` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0081` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0115` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0126` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0142` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0143` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0146` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0151` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0152` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0158` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0160` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0174` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0180` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0183` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0191` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0198` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0199` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0211` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0212` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0220` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0258` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-s0270` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0273` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0275` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0279` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0324` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0329` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0333` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0364` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0367` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0369` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0370` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0388` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0402` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0415` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0419` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0424` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0439` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0441` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0444` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-s0446` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0448` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0452` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-s0459` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0004` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-surgical-procedure-s0034` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0038` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-circumcision-surgical-procedure-s0041` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0042` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0047` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0063` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0314` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0322` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0323` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0325` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0326` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-circumcision-surgical-procedure-s0329` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0333` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-circumcision-surgical-procedure-s0334` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0008` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0046` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0140` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-clitoridectomy-s0147` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0155` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-clitoridectomy-s0158` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0190` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0202` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-clitoridectomy-s0206` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-clitoridectomy-s0207` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-clitoridectomy-s0214` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-clitoridectomy-s0226` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-cost-of-circumcision-surgery-in-chaozhou-s0026` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-cultural-views-on-circumcision-aesthetics-s0034` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-cultural-views-on-circumcision-aesthetics-s0121` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-cultural-views-on-circumcision-aesthetics-s0124` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0049` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0051` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0064` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0067` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0072` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0073` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0075` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0095` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0099` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0103` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0104` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0105` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0110` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0117` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0118` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0120` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0133` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0136` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0144` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0149` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0151` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0152` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0153` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0170` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0178` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0198` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0200` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0210` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0214` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0231` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0237` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0245` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0248` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0254` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-ethics-of-circumcision-s0256` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0267` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0274` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0275` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-ethics-of-circumcision-s0277` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0306` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0318` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ethics-of-circumcision-s0320` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-act-2003-s0058` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-act-2003-s0162` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-act-2003-s0163` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-female-genital-mutilation-act-2003-s0165` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-act-2003-s0170` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-act-2003-s0189` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0025` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0027` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0104` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0114` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0128` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0164` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0207` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0222` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0223` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0242` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-india-s0243` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-new-zealand-s0025` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-in-new-zealand-s0037` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-female-genital-mutilation-in-nigeria-s0102` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-nigeria-s0126` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-in-nigeria-s0193` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0079` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0149` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0156` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0166` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0172` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0259` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-sudan-s0264` | begging-the-question | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-female-genital-mutilation-in-the-gambia-s0021` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-gambia-s0067` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-gambia-s0124` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-gambia-s0131` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-gambia-s0146` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-united-kingdom-s0185` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-united-kingdom-s0192` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-in-the-united-states-s0141` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-united-states-s0155` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-in-the-united-states-s0190` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-united-states-s0192` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-in-the-united-states-s0197` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-laws-by-country-s0021` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0041` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0048` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0064` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0254` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0271` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-laws-by-country-s0280` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0282` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-laws-by-country-s0312` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0040` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0070` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-s0071` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0128` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0145` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0164` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0166` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0196` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0199` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-female-genital-mutilation-s0209` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0221` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-female-genital-mutilation-s0314` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-female-genital-mutilation-s0323` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0009` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-forced-circumcision-s0026` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0041` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether the source can be trusted; whether the source is mi… |
| `circ-forced-circumcision-s0133` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-forced-circumcision-s0173` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-forced-circumcision-s0175` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-forced-circumcision-s0177` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0185` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-forced-circumcision-s0205` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0255` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-forced-circumcision-s0260` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0263` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-forced-circumcision-s0274` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-man-s0079` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-man-s0084` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-restoration-s0269` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-restoration-s0274` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0009` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0080` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0157` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0160` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0164` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0187` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0188` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0189` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0191` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0203` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0273` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0274` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-foreskin-s0278` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-foreskin-s0285` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-gishiri-cutting-s0070` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-gishiri-cutting-s0091` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-gishiri-cutting-s0103` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-gishiri-cutting-s0114` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-gishiri-cutting-s0121` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-gishiri-cutting-s0130` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-gishiri-cutting-s0137` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0179` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0182` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0190` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0195` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0200` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-history-of-circumcision-s0201` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0144` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0149` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0152` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0153` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-infibulation-s0162` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0177` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0178` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-infibulation-s0186` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0240` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-infibulation-s0244` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0007` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0015` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0020` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0129` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0133` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0216` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-international-day-of-zero-tolerance-for-female-genital-mutilation-s0252` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0146` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0147` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0150` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0153` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0156` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0198` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0203` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0205` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0229` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-khitan-circumcision-s0230` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-meatal-stenosis-s0151` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-meatal-stenosis-s0165` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-mohel-s0016` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0121` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0122` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-mohel-s0124` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0136` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0154` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0161` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0162` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0163` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-mohel-s0172` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-mohel-s0229` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-penile-subincision-s0130` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-phimosis-s0281` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-prevalence-of-circumcision-s0053` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prevalence-of-circumcision-s0062` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prevalence-of-circumcision-s0090` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-prohibition-of-female-circumcision-act-1985-s0032` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-prohibition-of-female-circumcision-act-1985-s0037` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prohibition-of-female-circumcision-act-1985-s0048` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prohibition-of-female-circumcision-act-1985-s0128` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prohibition-of-female-circumcision-act-1985-s0138` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prohibition-of-female-circumcision-act-1985-s0139` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-prohibition-of-female-circumcision-act-1985-s0142` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-redundant-prepuce-s0106` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-religion-and-circumcision-s0042` | false-cause | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-religion-and-circumcision-s0214` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-religion-and-circumcision-s0216` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religion-and-circumcision-s0223` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religion-and-circumcision-s0225` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religious-views-on-female-genital-mutilation-s0019` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-religious-views-on-female-genital-mutilation-s0022` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religious-views-on-female-genital-mutilation-s0080` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religious-views-on-female-genital-mutilation-s0124` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-religious-views-on-female-genital-mutilation-s0201` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ulwaluko-s0039` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ulwaluko-s0127` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ulwaluko-s0130` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-ulwaluko-s0149` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0003` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-views-on-circumcision-s0069` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0070` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-views-on-circumcision-s0074` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-views-on-circumcision-s0077` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0078` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0080` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0083` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0086` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-views-on-circumcision-s0087` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0090` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0094` | appeal-to-authority | possible issue; missing fact: whether experts substantially disagree; whether the source can be trusted; whether the source is misquoted |
| `circ-views-on-circumcision-s0104` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0108` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-views-on-circumcision-s0119` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0121` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-views-on-circumcision-s0122` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0129` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-views-on-circumcision-s0188` | argument-from-ignorance | possible issue; excerpt boundary — support may lie outside the passage |
| `circ-views-on-circumcision-s0190` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0001` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0028` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0032` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0082` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0108` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0119` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0128` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0134` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0174` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0181` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |
| `circ-women-unaffected-by-female-genital-cutting-s0186` | appeal-to-authority | possible issue; missing fact: whether the source is an expert on this question; whether experts substantially disagree; whether the source … |

## Outputs

- Passages: `passages_from_inventory.jsonl` / `passages.jsonl` (symlink), `passages.md`
- IRs: `irs/{id}.json` (2616 files)
- Checker dump: `out/check_reports.json`
- METHOD markdown: `out/method_records.md`
- METHOD JSONL (flag + possible_issue only): `out/method_records.jsonl` (452 rows)
- Leads index: `out/leads.json`, `out/counts.json`
- Extractor (local tool, not package): `tools/extract_idea_irs.py`
- This summary: `out/RUN_SUMMARY.md`

## Extraction notes

- Blind cue-driven extract per `EXTRACTOR_PROMPT.md` shape (no `expected_checker`, no fallacy names in IR).
- All passages marked `excerpt: true` (inventory sentences from article context).
- Charity: hedges kept weak where may/can/potentially; attributed speakers kept; anti-collapse edges where premise→conclusion / authority / unproven cues appear.
- Extractor model tag: `cue-extractor-v1` (structural cue graph; not a substitute for hand METHOD).

## Next

Hand METHOD review on high-value possible_issue leads if worth it; broader catalog coverage needs more `ir_pattern` pilots. Holding push until Jason says so.

