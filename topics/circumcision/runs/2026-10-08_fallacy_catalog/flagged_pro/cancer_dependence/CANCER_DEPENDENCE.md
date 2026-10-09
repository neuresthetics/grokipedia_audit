# Which medical arguments rest on the cancer-prevention claim? (what-if count)

Male circumcision articles only. This is the second what-if pass on the medical surviving pro arguments, after the HIV/STI pass ([../sti_dependence/STI_DEPENDENCE.md](../sti_dependence/STI_DEPENDENCE.md)). Instructions: [CANCER_PROMPT.md](CANCER_PROMPT.md).

**This is a what-if count, not a finding.** Some critics say cancer prevention is not a valid reason for circumcision. A tag of C means only that an argument depends on the cancer-prevention claim, not that the claim is wrong. Penile cancer is rare in absolute terms, but how much a rare benefit should weigh is a question this audit does not settle.

Read this with the limits in mind:

- **AI-tagged, not by a person**: 2 separate AI model sessions, one per range of the queue.
- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.
- **One tag per sentence.** A sentence that names cancer and another benefit is tagged C only if no point is left without the cancer part.
- **Prefilter.** Only the 210 of 667 medical sentences whose own text or the two prose sentences on either side name cancer, carcinoma, malignancy, tumour, neoplasia, HPV, papillomavirus or cervical were tagged. Recall limit: a sentence that relies on cancer through "these benefits" is caught only if a keyword sits inside that window; the rest of the medical sentences count as not resting on cancer.

## Counts

| Tag | Meaning | Sentences | Share of the prefiltered |
|---|---|---|---|
| **C** | Rests on the cancer-prevention claim | 35 | 16.7% |
| **K** | Rests on a non-cancer claim | 174 | 82.9% |
| **N** | Mentions cancer, not relied on as a benefit | 1 | 0.5% |

## Combined with the HIV/STI pass

- C sentences also tagged H (HIV/STI): **8**. C but not H: **27**.
- Medical arguments resting on the HIV/STI claim or the cancer claim: H 254 + cancer only 27 = **281**, which is 42.1% of the 667 medical arguments and 31.8% of all 883 surviving pro arguments.
- Remaining medical arguments: 386 (57.9% of 667).

Again: these counts say which arguments depend on those claims, not that the claims are wrong.

**Keyword cross-check** (a regex, no model): 60 of the 210 prefiltered sentences name cancer themselves. Whether a sentence names cancer matched whether the model tagged it C for 80.5% of them. It is a rough cross-check only.

## Top articles (by C)

| Article | Prefiltered | C | K | N |
|---|---|---|---|---|
| Ethics of circumcision (`ethics-of-circumcision`) | 38 | 8 | 30 | 0 |
| Foreskin (`foreskin`) | 20 | 5 | 15 | 0 |
| Circumcision controversies (`circumcision-controversies`) | 16 | 3 | 12 | 1 |
| Circumcision in Africa (`circumcision-in-africa`) | 10 | 3 | 7 | 0 |
| Views on circumcision (`views-on-circumcision`) | 10 | 3 | 7 | 0 |
| Circumcision (`circumcision`) | 26 | 2 | 24 | 0 |
| Circumcision surgical procedure (`circumcision-surgical-procedure`) | 17 | 2 | 15 | 0 |
| _Khitan_ (circumcision) (`khitan-circumcision`) | 12 | 2 | 10 | 0 |

## By tagger

| Tagger | Range | Sentences | C | K | N |
|---|---|---|---|---|---|
| cancer-tagger-1 | p0001-p0105 | 105 | 15 (14%) | 89 (85%) | 1 (1%) |
| cancer-tagger-2 | p0106-p0210 | 105 | 20 (19%) | 85 (81%) | 0 (0%) |

## C: Rests on the cancer-prevention claim

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> Circumcision performed in childhood or adolescence substantially lowers the incidence of invasive penile cancer, a rare malignancy linked primarily to chronic inflammation and HPV persistence under the foreskin.
>
> `brit-milah` s0215

> Penile cancer is rare (about 1 in 100,000 in developed countries) and mostly affects uncircumcised males, with near-zero rates in populations with universal neonatal circumcision, such as Israel (0.1–0.3 per 100,000). [108]
>
> `circumcision` s0183

> Penile cancer, though rare (incidence ~1 in 100,000 in developed countries), shows substantially lower rates in circumcised populations, particularly when performed in childhood or adolescence.
>
> `circumcision-controversies` s0040

## K: Rests on a non-cancer claim

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> Scientific studies have identified several health benefits associated with male circumcision, particularly in reducing the risk of certain infections.
>
> `ashley-montagu-resolution` s0196 · tagger's note: general infection-benefit intro; infections point stands without cancer

> Randomized controlled trials (RCTs) in sub-Saharan Africa have demonstrated that male circumcision reduces the risk of heterosexual HIV acquisition by 50-60% in men.
>
> `brit-milah` s0211 · tagger's note: HIV

> The World Health Organization and Centers for Disease Control and Prevention recommend it as an additional strategy in high-prevalence areas, with over 27 million procedures since 2007. [2] [91]
>
> `circumcision` s0162 · tagger's note: HIV recommendation

## N: Mentions cancer, not relied on as a benefit

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, three different articles, earliest in article order):

> These films, released in the late 2000s and 2010s, contributed to broader media discussions on consent and harm, though empirical support for long-term claims often relies on anecdotal evidence rather than large-scale controlled studies.
>
> `circumcision-controversies` s0209 · tagger's note: about evidence quality of anti documentaries, not a cancer-prevention point

## Files

- [tags.csv](tags.csv): every prefiltered sentence with its tag, its HIV/STI tag, the keyword check, the tagger's note and the text.
- [summary.json](summary.json), [CANCER_PROMPT.md](CANCER_PROMPT.md), [work/queue.csv](work/queue.csv), [work/tags.csv](work/tags.csv).
- Scripts: [cancer_queue.py](scripts/cancer_queue.py), [build_cancer_dependence.py](scripts/build_cancer_dependence.py).
- Chart: `docs/img/circumcision/2026-10-08/10_what_if_removed.png`.
