# What do the surviving pro arguments rely on?

Male circumcision articles only. The 883 pro argument sentences that kept all 3 points after step 6 pass 3 were each tagged with the one kind of support they rely on to make their point ([TAG_PROMPT.md](TAG_PROMPT.md)). A tag says what an argument rests on, not whether it is right. Keeping 3 points means no reviewer flagged it, not that it is proven true.

Read this with the limits in mind:

- **Model-tagged, not by a person**: 4 separate AI model sessions, one per range of the queue.
- **Not blind**: the tagging ran from a conversation that already knew the earlier results of this audit.
- **One type per sentence**, so sentences that mix two kinds of support are forced into one type.
- **Scope**: male circumcision pro arguments with all 3 points after pass 3 only. Anti arguments and pro arguments that lost points are not tagged.

## Counts

| Type | Sentences | Share |
|---|---|---|
| **M**: Medical or scientific data | 667 | 75.5% |
| **E**: Ethics, rights or law | 72 | 8.2% |
| **R**: Religion, culture or tradition | 105 | 11.9% |
| **O**: Other, mixed or framing | 39 | 4.4% |

**Keyword ballpark** (a regex count, no model; see the script): M 628, E 49, R 112, O 94. The keyword tag matched the model's tag for 82.4% of sentences. It is a rough cross-check only.

## By tagger

| Tagger | Range | Sentences | M | E | R | O |
|---|---|---|---|---|---|---|
| tagger-1 | t0001-t0221 | 221 | 167 (76%) | 12 (5%) | 31 (14%) | 11 (5%) |
| tagger-2 | t0222-t0442 | 221 | 181 (82%) | 17 (8%) | 19 (9%) | 4 (2%) |
| tagger-3 | t0443-t0663 | 221 | 171 (77%) | 16 (7%) | 22 (10%) | 12 (5%) |
| tagger-4 | t0664-t0883 | 220 | 148 (67%) | 27 (12%) | 33 (15%) | 12 (5%) |

Ranges follow article order, so they cover different articles; differences between taggers mix article content with tagger habits.

## M: Medical or scientific data

Articles with the most sentences of this type:

- Circumcision (`circumcision`): 99
- Circumcision and HIV (`circumcision-and-hiv`): 99
- Ethics of circumcision (`ethics-of-circumcision`): 87
- Circumcision controversies (`circumcision-controversies`): 49
- Circumcision in Africa (`circumcision-in-africa`): 40

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, two different articles, earliest in article order):

> The symposia positioned genital cutting as a form of bodily violation akin to mutilation, drawing parallels between male and female practices despite differing prevalence and severity in empirical data on outcomes like infection rates or sexual function.
>
> `ashley-montagu-resolution` s0042

> This approach avoids potential complications from anesthetics, such as delayed healing or allergic reactions in neonates.
>
> `brit-milah` s0130

## E: Ethics, rights or law

Articles with the most sentences of this type:

- Circumcision and law (`circumcision-and-law`): 12
- Views on circumcision (`views-on-circumcision`): 10
- Ethics of circumcision (`ethics-of-circumcision`): 8
- Forced circumcision (`forced-circumcision`): 7
- Religion and circumcision (`religion-and-circumcision`): 7

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, two different articles, earliest in article order):

> Amnesty International, while active on female genital mutilation since the 1990s, has not equated it with male circumcision in policy statements, highlighting divergent institutional priorities despite the resolution's broader scope.
>
> `ashley-montagu-resolution` s0147

> Proponents argue that parental proxy consent is sufficient, allowing decisions in the child's best interest based on cultural, religious, or preventive health grounds until maturity.
>
> `circumcision` s0413

## R: Religion, culture or tradition

Articles with the most sentences of this type:

- Ulwaluko (`ulwaluko`): 18
- Brit shalom (naming ceremony) (`brit-shalom-naming-ceremony`): 14
- Brit milah (`brit-milah`): 12
- Circumcision controversy in early Christianity (`circumcision-controversy-in-early-christianity`): 10
- Cultural views on circumcision aesthetics (`cultural-views-on-circumcision-aesthetics`): 10

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, two different articles, earliest in article order):

> Critics of the Ashley Montagu Resolution contend that equating male circumcision with female genital mutilation overlooks entrenched cultural practices where male circumcision functions as a non-harmful rite of passage promoting social cohesion and identity.
>
> `ashley-montagu-resolution` s0211

> Maimonides (Guide for the Perplexed 3:49) gives two reasons: primarily, circumcision moderates excessive lust without harming procreative function, directing sexuality toward holiness (marriage, continuity).
>
> `brit-milah` s0091

## O: Other, mixed or framing

Articles with the most sentences of this type:

- Cultural views on circumcision aesthetics (`cultural-views-on-circumcision-aesthetics`): 10
- Mohel (`mohel`): 6
- Ashley Montagu Resolution (`ashley-montagu-resolution`): 5
- Circumcision (`circumcision`): 4
- Circumcision in Africa (`circumcision-in-africa`): 3

Examples (verbatim from the 2026-10-01 snapshots, checked by script; picked by a fixed rule: 120-260 characters, two different articles, earliest in article order):

> The resolution's policy influence was constrained by its origins in niche symposia and reliance on ethical rather than empirical consensus, with critics noting insufficient engagement from sovereign states practicing ritual circumcision. [35]
>
> `ashley-montagu-resolution` s0166

> Proponents argue this ritual instills communal identity and ethical formation from birth, with parental authority extending to irreversible acts that secure the child's religious inheritance, akin to other parental decisions in child-rearing.
>
> `brit-milah` s0256

## Files

- [tags.csv](tags.csv): every sentence with its tag, the keyword tag, the tagger's note and the text.
- [summary.json](summary.json), [TAG_PROMPT.md](TAG_PROMPT.md), [work/queue.csv](work/queue.csv), [work/tags.csv](work/tags.csv).
- Scripts: [tag_queue.py](scripts/tag_queue.py), [build_topic_tags.py](scripts/build_topic_tags.py).
- Chart: `docs/img/circumcision/2026-10-08/08_what_survivors_rely_on.png`.
