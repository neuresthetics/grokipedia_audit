# Which medical arguments rest on the HIV/STI claim? (what-if count)

Male circumcision articles only. The 667 pro argument sentences that kept all 3 points after pass 3 and were tagged as relying on medical or scientific data were each tagged again: does the medical point rest on protection against HIV or another sexually transmitted infection? ([SIDEIDEA_PROMPT.md](SIDEIDEA_PROMPT.md))

**This is a what-if count, not a finding.** Some critics say circumcision gives no protection against HIV or other STIs. If that claim were set aside, the 254 arguments tagged H would lose their medical point. A tag of H says only that an argument depends on the HIV/STI claim. It is not a finding that the claim is true or false; this audit has not checked it.

Read this with the limits in mind:

- **AI-tagged, not by a person**: 3 separate AI model sessions, one per range of the queue.
- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.
- **One tag per sentence.** A sentence that names HIV and another medical benefit is tagged H only if no medical point is left without the HIV/STI part.
- **Scope**: medical pro arguments with all 3 points after pass 3 only.

## Counts

| Tag | Meaning | Sentences | Share |
|---|---|---|---|
| **H** | Rests on the HIV/STI protection claim | 254 | 38.1% |
| **X** | Rests on a non-STI medical claim | 399 | 59.8% |
| **N** | Medical in form, no benefit claim relied on | 14 | 2.1% |

**Keyword cross-check** (a regex, no model): 287 sentences name HIV or an STI. Whether a sentence names HIV or an STI matched whether the model tagged it H for 81.3% of sentences. 79 name HIV or an STI but were not tagged H, and 46 were tagged H without naming it (the notes in tags.csv give the taggers' reasons where they wrote one). It is a rough cross-check only.

## Top articles

| Article | Medical sentences | H | X | N | H share |
|---|---|---|---|---|---|
| Circumcision (`circumcision`) | 99 | 30 | 64 | 5 | 30% |
| Circumcision and HIV (`circumcision-and-hiv`) | 99 | 95 | 4 | 0 | 96% |
| Ethics of circumcision (`ethics-of-circumcision`) | 87 | 28 | 58 | 1 | 32% |
| Circumcision controversies (`circumcision-controversies`) | 49 | 11 | 38 | 0 | 22% |
| Circumcision in Africa (`circumcision-in-africa`) | 40 | 28 | 12 | 0 | 70% |
| Foreskin (`foreskin`) | 37 | 4 | 33 | 0 | 11% |
| Views on circumcision (`views-on-circumcision`) | 34 | 7 | 27 | 0 | 21% |
| Circumcision surgical procedure (`circumcision-surgical-procedure`) | 28 | 6 | 22 | 0 | 21% |

## By tagger

| Tagger | Range | Sentences | H | X | N |
|---|---|---|---|---|---|
| sti-tagger-1 | h0001-h0223 | 223 | 110 (49%) | 108 (48%) | 5 (2%) |
| sti-tagger-2 | h0224-h0446 | 223 | 87 (39%) | 134 (60%) | 2 (1%) |
| sti-tagger-3 | h0447-h0667 | 221 | 57 (26%) | 157 (71%) | 7 (3%) |

Ranges follow article order, so differences between taggers mix article content with tagger habits.

## H: Rests on the HIV/STI protection claim

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> Randomized controlled trials in Africa demonstrated that voluntary medical male circumcision reduces the risk of heterosexual HIV acquisition in men by approximately 60%. [3]
>
> `ashley-montagu-resolution` s0197

> Randomized controlled trials (RCTs) in sub-Saharan Africa have demonstrated that male circumcision reduces the risk of heterosexual HIV acquisition by 50-60% in men.
>
> `brit-milah` s0211

> Three randomized controlled trials in sub-Saharan Africa (2005–2007) showed voluntary medical male circumcision reduces HIV acquisition risk in heterosexual men by approximately 60%. [87] [88] [89]
>
> `circumcision` s0160

## X: Rests on a non-STI medical claim

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> The symposia positioned genital cutting as a form of bodily violation akin to mutilation, drawing parallels between male and female practices despite differing prevalence and severity in empirical data on outcomes like infection rates or sexual function.
>
> `ashley-montagu-resolution` s0042 · tagger's note: infection rates (not STI-specific) and sexual function data

> This approach avoids potential complications from anesthetics, such as delayed healing or allergic reactions in neonates.
>
> `brit-milah` s0130 · tagger's note: anaesthesia complications

> For older children and adults, local infiltration or DPNB is standard, with sedation or general anesthesia for anxiety or complexity; trained providers keep complications below 1%. [12]
>
> `circumcision` s0059 · tagger's note: anaesthesia/complications

## N: Medical in form, no benefit claim relied on

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> In the United States, orthopedic surgeon Lewis Sayre advanced the practice in the 1870s by associating uncircumcised foreskins with "reflex neurosis"—irritation allegedly causing spinal issues, paralysis, epilepsy, and leg weakness. [152]
>
> `circumcision` s0256 · tagger's note: 1870s history of Sayre's claims

> Khitan, the Islamic practice of male circumcision, surgically excises the foreskin covering the glans penis, preserving the organ's primary erectile and urinary functions while removing a non-vital cutaneous layer. [13]
>
> `khitan-circumcision` s0201 · tagger's note: anatomy/technique description

> The entire operation, leveraging the infant's physiological resilience, typically lasts under one minute from incision to completion, emphasizing the mohel's training in both surgical asepsis and ritual exactitude.
>
> `mohel` s0100 · tagger's note: technique description

## Files

- [tags.csv](tags.csv): every sentence with its tag, the keyword check, the tagger's note and the text.
- [summary.json](summary.json), [SIDEIDEA_PROMPT.md](SIDEIDEA_PROMPT.md), [work/queue.csv](work/queue.csv), [work/tags.csv](work/tags.csv).
- Scripts: [sti_queue.py](scripts/sti_queue.py), [build_sti_dependence.py](scripts/build_sti_dependence.py).
- Chart: `docs/img/circumcision/2026-10-08/09_sti_dependence.png`.
