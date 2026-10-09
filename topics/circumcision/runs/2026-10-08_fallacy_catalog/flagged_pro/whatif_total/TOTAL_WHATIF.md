# Total what-if: how much of the pro side is left under Jason's premises?

**What-if, not a finding.** This page takes three premises as true for the sake of the count:

1. circumcision gives no protection against HIV or other STDs;
2. STD rates are higher in circumcising countries;
3. cancer prevention is not a valid reason (penile cancer is rare, and prevention by removal is not valid).

This audit did not check any of the three. Premise 1 contradicts the three randomized trials the articles cite (Auvert 2005, Bailey 2007, Gray 2007), which the `circumcision-and-hiv` article says later Cochrane reviews rated at low risk of bias. Premise 2 is a country-level comparison; this count does not use it separately, because arguments that rest on HIV/STI protection are already set aside under premise 1. So the result holds only if the premises hold.

Scope: the 971 male circumcision pro arguments from step 5. Earlier results are not changed; this page only adds them up.

## Result

| Group | Arguments | Share of 971 |
|---|---:|---:|
| Already flagged by the audit (lost 1+ point at step 5, pass 2 or pass 3) | 88 | 9.1% |
| What-if: rests on the HIV/STI claim | 254 | 26.2% |
| What-if: rests on the cancer claim only | 27 | 2.8% |
| Not invalidated: other medical claims | 386 | 39.8% |
| Not invalidated: ethics, rights or law | 72 | 7.4% |
| Not invalidated: religion, culture or tradition | 105 | 10.8% |
| Not invalidated: other, mixed or framing | 39 | 4.0% |
| **Total** | **971** | **100%** |

- Already flagged by the audit: **88** (9.1%). They first lost a point at step 5 (61), pass 2 (22) or pass 3 (5).
- Set aside under the what-if: **281** (28.9%), from the HIV/STI pass (254) and the cancer pass (27 cancer only).
- Flagged or set aside: **369** (38.0%).
- Not invalidated: **602** (62.0%): 386 medical arguments on other claims (UTIs, phimosis, hygiene, safety, sexual function and so on), plus 216 ethics, law, religion, culture or other arguments.

Chart: [11_pro_side_invalidated.png](../../../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

![What-if: how much of the pro side is left?](../../../../../../docs/img/circumcision/2026-10-08/11_pro_side_invalidated.png)

## Counting rules (no double counting)

Each argument goes into one group only, in this order:

1. If it lost 1 or more points at step 5, pass 2 or pass 3, it is **already flagged**, whatever its topic.
2. Otherwise, if it was tagged medical (M) and HIV/STI (H), it is **what-if: HIV/STI** ([STI_DEPENDENCE.md](../sti_dependence/STI_DEPENDENCE.md)).
3. Otherwise, if it was tagged medical and cancer (C), it is **what-if: cancer only** ([CANCER_DEPENDENCE.md](../cancer_dependence/CANCER_DEPENDENCE.md)).
4. Otherwise it is **not invalidated**, split by its topic tag ([TAGS.md](../topic_tags/TAGS.md)).

## Not checked: non-medical arguments that lean on HIV/STI or cancer

The 216 arguments tagged ethics/law, religion/culture or other were not put through the HIV/STI or cancer passes, so the what-if does not touch them. Some may still lean on those claims, which is a recall limit.

- **Keyword check (rough upper bound, no model):** 14 of 216 (6.5%) name HIV, an STI or cancer (7 E, 7 O). Naming a term is not the same as resting on it.
- **Model check of those 14** ([CHECK_PROMPT.md](keyword_check/CHECK_PROMPT.md), [judgments.csv](keyword_check/judgments.csv)): **2** rest on the HIV/STI claim; the other 12 keep another point (consent, culture, another medical benefit) or only report a view or event.
- `circumcision-in-africa` `s0279`: Argues Western norms do not fit Africa because HIV epidemiology differs; no point left without the HIV benefit
- `circumcision-in-africa` `s0287`: Point is that autonomy claims should not outrank verifiable HIV transmission reductions; rests on the HIV claim

These 2 are reported separately and are **not** added to the table. Adding them would make the what-if group 283 (29.1%). A non-medical sentence that leans on these claims without naming them would not be found.

## Caveats

- **What-if, not a finding.** A tag means "depends on the claim", not that the claim is wrong.
- **AI-tagged, not blind.** The topic, HIV/STI and cancer tags and the model check above were made by AI model sessions, not a person. All ran from a conversation that already knew the earlier results, so they are not blind. The model check of the 14 keyword hits was one session.
- **Pro only.** Anti arguments were checked only at step 5 and are not part of this count.
- **Recall limits.** The cancer pass covers only medical sentences with a cancer, HPV or cervical keyword within two sentences. See the non-medical check above too.
- **One topic per sentence.** Mixed sentences were forced into one type at the topic-tagging step.

Built by `scripts/build_whatif_total.py` from `../recheck/points_by_pass.csv`, `../topic_tags/tags.csv`, `../sti_dependence/tags.csv` and `../cancer_dependence/tags.csv`.

## The premises, in plain words

If these three things are true, 38% of the pro side is invalidated (369 of 971: 88 already flagged by this audit plus 281 that rest on the HIV/STI or cancer claim). The other 602 (62%) are left standing. Premises are assumed, not tested here.

1. **Circumcision does not protect against HIV or other STIs.**
2. **STI rates are highest in circumcising countries.** This adds no separate count beyond premise 1.
3. **Cancer prevention is not a valid reason** (penile cancer is rare, and prevention-by-removal proves too much).

Note on the chart: chart 11 was redrawn so it states this at a glance. Its title is now "If these three things are true, 38% of the pro side is invalidated", and the premises are shown in a box on the chart. Alt text above that reads "What-if: how much of the pro side is left?" refers to the same chart.

## Limits: a narrow selection

The percentage comes from a narrow selection of arguments: the claims in two X posts, plus one point about cancer, applied to the pro arguments in 39 male circumcision Grokipedia articles. It is a what-if count. Applying more premises or arguments would change the numbers, in either direction. Nothing here has been tested beyond that selection.
