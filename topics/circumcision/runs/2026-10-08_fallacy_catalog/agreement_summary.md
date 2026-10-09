# Reviewer comparison (three separate AI reader runs, not blind)

Wording: "flagged by both / all three / at least two" means that many reviewers, in separate runs, flagged overlapping text in the same article. It is overlap, not proof that a flag is right.

The runs were not blind: Reviewers 2 and 3 were told not to open the other reviewers' files until their own were saved, but their instructions came from a conversation that had already discussed earlier results. Overlap may be partly inflated by that; Reviewer 1 is the only fully uninfluenced read.

- Articles: 58
- R1: 87 flags; by side {'neutral': 11, 'anti': 23, 'pro': 53}; by verdict {'flag': 86, 'possible issue': 1}; articles with a flag 37
- R2: 64 flags; by side {'pro': 42, 'neutral': 14, 'anti': 8}; by verdict {'possible issue': 52, 'flag': 12}; articles with a flag 28
- R3: 121 flags; by side {'neutral': 23, 'pro': 59, 'anti': 39}; by verdict {'flag': 79, 'possible issue': 42}; articles with a flag 45
- Quotes not locatable in snapshot (excluded from matching): 0 []

## Pairwise overlap (one-to-one matching)

| Pair | Flags | Matched | Only first | Only second | Share of first matched | Share of second matched | Same side | Same fallacy name | Near-twin name | Same side: pro / anti / neutral |
|---|---|---|---|---|---|---|---|---|---|---|
| R1-R2 | 87 / 64 | 41 | 46 | 23 | 47.1% | 64.1% | 36/41 (88%) | 20/41 (49%) | 10 | 27 / 3 / 6 |
| R1-R3 | 87 / 121 | 57 | 30 | 64 | 65.5% | 47.1% | 53/57 (93%) | 39/57 (68%) | 7 | 35 / 13 / 5 |
| R2-R3 | 64 / 121 | 43 | 21 | 78 | 67.2% | 35.5% | 35/43 (81%) | 28/43 (65%) | 6 | 27 / 4 / 4 |
- Spearman rho of per-article flag counts, R1 vs R2: 0.765
- Spearman rho of per-article flag counts, R1 vs R3: 0.769
- Spearman rho of per-article flag counts, R2 vs R3: 0.722

## Three-way passages (overlapping spans joined)

- Passages flagged by any reviewer: 164
  - flagged only by reviewer 1: 22
  - flagged only by reviewer 2: 13
  - flagged only by reviewer 3: 54
  - flagged by reviewers 1 and 2 only: 8
  - flagged by reviewers 1 and 3 only: 24
  - flagged by reviewers 2 and 3 only: 10
  - flagged by all three: 33
- Flagged by at least two, any side: 75; flagged by all three, any side: 33
- Flagged by at least two with the same side: 74, by side {'neutral': 11, 'pro': 45, 'anti': 18}
- Flagged by all three with the same side: 25, by side {'pro': 22, 'neutral': 2, 'anti': 1}
- Of the 74 at-least-two same-side passages, at least two reviewers gave the same fallacy name in 54
- Passages where two sides each had at least two reviewers (side tie): 0
- Largest passage: 3 rows; three-reviewer passages where some pair of quotes does not overlap directly (joined through the third): 0
  - Male circumcision: at least two same side {'neutral': 3, 'pro': 38, 'anti': 5}; all three same side {'pro': 18}
  - FGM: at least two same side {'anti': 13, 'neutral': 8, 'pro': 7}; all three same side {'neutral': 2, 'anti': 1, 'pro': 4}

## R3 by entry

- inconsistency: 30
- non-sequitur: 20
- bulverism: 11
- cum-hoc: 10
- false-cause: 9
- post-hoc: 5
- false-analogy: 5
- over-extrapolation: 5
- appeal-to-tradition: 3
- double-standard: 3
- argument-from-ignorance: 2
- hasty-generalization: 2
- cherry-picking: 2
- irrelevant-conclusion: 2
- straw-man: 2
- base-rate-fallacy: 1
- suppressed-evidence: 1
- unrepresentative-sample: 1
- red-herring: 1
- ad-hoc-rescue: 1
- far-fetched-hypothesis: 1
- tu-quoque: 1
- ecological-fallacy: 1
- genetic-fallacy: 1
- circumstantial-ad-hominem: 1

## R3 by article

- ethics-of-circumcision: 10
- circumcision-controversies: 7
- female-genital-mutilation: 7
- women-unaffected-by-female-genital-cutting: 6
- ulwaluko: 5
- female-genital-mutilation-act-2003: 5
- female-genital-mutilation-laws-by-country: 5
- views-on-circumcision: 4
- prevalence-of-female-genital-mutilation: 4
- circumcision: 4
- female-genital-mutilation-in-sudan: 4
- religious-views-on-female-genital-mutilation: 3
- female-genital-mutilation-in-nigeria: 3
- restoration-device: 3
- female-genital-mutilation-in-the-united-states: 3
- circumcision-in-africa: 3
- forced-circumcision: 3
- forced-circumcision-of-minors-in-south-korea: 2
- children-act-1989-amendment-female-genital-mutilation-act-2019: 2
- foreskin-man: 2
- female-genital-mutilation-in-the-gambia: 2
- female-genital-mutilation-in-new-zealand: 2
- gishiri-cutting: 2
- khitan-circumcision: 2
- mohel: 2
- international-day-of-zero-tolerance-for-female-genital-mutilation: 2
- ashley-montagu-resolution: 2
- female-genital-mutilation-in-india: 2
- brit-milah: 2
- circumcision-and-law: 2
- foreskin: 2
- cultural-views-on-circumcision-aesthetics: 1
- redundant-prepuce: 1
- lipodermos: 1
- meatal-stenosis: 1
- penile-subincision: 1
- stapler-circumcision: 1
- prohibition-of-female-circumcision-act-1985: 1
- circumcision-of-jesus: 1
- prevalence-of-circumcision: 1
- religion-and-circumcision: 1
- female-genital-mutilation-in-the-united-kingdom: 1
- infibulation: 1
- clitoridectomy: 1
- circumcision-and-hiv: 1

## Passages flagged by all three with the same side

| article | side | R1 entry | R2 entry | R3 entry |
|---|---|---|---|---|
| brit-milah | pro | non-sequitur | non-sequitur | non-sequitur |
| circumcision | pro | inconsistency | inconsistency | inconsistency |
| circumcision | pro | double-standard | double-standard | double-standard |
| circumcision-and-law | pro | appeal-to-the-people | non-sequitur | non-sequitur |
| circumcision-controversies | pro | post-hoc | post-hoc | post-hoc |
| circumcision-controversies | pro | straw-man | non-sequitur | non-sequitur |
| circumcision-controversies | pro | non-sequitur | non-sequitur | non-sequitur |
| circumcision-controversies | pro | secundum-quid | over-extrapolation | inconsistency |
| circumcision-in-africa | pro | non-sequitur | non-sequitur | non-sequitur |
| ethics-of-circumcision | pro | false-analogy | false-analogy | false-analogy |
| ethics-of-circumcision | pro | argument-from-silence | argument-from-ignorance | argument-from-ignorance |
| female-genital-mutilation | neutral | inconsistency | cum-hoc | cum-hoc |
| female-genital-mutilation-act-2003 | anti | bulverism | appeal-to-motive | bulverism |
| female-genital-mutilation-in-india | pro | straw-man | straw-man | straw-man |
| female-genital-mutilation-in-nigeria | neutral | inconsistency | cum-hoc | cum-hoc |
| foreskin | pro | inconsistency | inconsistency | inconsistency |
| mohel | pro | secundum-quid | cum-hoc | over-extrapolation |
| mohel | pro | bulverism | appeal-to-motive | bulverism |
| prevalence-of-circumcision | pro | false-cause | cum-hoc | cum-hoc |
| ulwaluko | pro | appeal-to-tradition | appeal-to-tradition | appeal-to-tradition |
| ulwaluko | pro | inconsistency | no-true-scotsman | inconsistency |
| views-on-circumcision | pro | irrelevant-conclusion | irrelevant-conclusion | irrelevant-conclusion |
| women-unaffected-by-female-genital-cutting | pro | false-analogy | false-analogy | false-analogy |
| women-unaffected-by-female-genital-cutting | pro | bulverism | appeal-to-motive | bulverism |
| women-unaffected-by-female-genital-cutting | pro | non-sequitur | non-sequitur | non-sequitur |
