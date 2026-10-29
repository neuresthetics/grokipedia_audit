# Circumcision passages — idea_detection full (2026-10-28)

**Published:** 2026-10-28 on grokipedia_audit `main` in commits [`368a337`](https://github.com/neuresthetics/grokipedia_audit/commit/368a337) and [`1ade5c1`](https://github.com/neuresthetics/grokipedia_audit/commit/1ade5c1). Artifact text below is the run record as produced; leads are assists, not hand verdicts.

Source: Oct 8 survival `argument_inventory.csv` (pro/anti labeled sentences),
emitted as `passages_from_inventory.jsonl` (symlinked as `passages.jsonl`).
Not a raw article carve. ~~Local only; not pushed.~~ (superseded: published, see note above)

- **Passages:** 2616
- **Articles represented:** 54 / 58
- **Sides:** pro=1272, anti=1344
- **Fields:** `id`, `passage`, `article`, `side`, `topic_group`, `source`

## Counts by article

| Article | N |
| --- | ---: |
| `circumcision` | 172 |
| `ethics-of-circumcision` | 160 |
| `circumcision-and-hiv` | 136 |
| `forced-circumcision` | 111 |
| `ashley-montagu-resolution` | 107 |
| `female-genital-mutilation` | 106 |
| `circumcision-controversies` | 95 |
| `women-unaffected-by-female-genital-cutting` | 93 |
| `brit-milah` | 78 |
| `circumcision-in-africa` | 77 |
| `views-on-circumcision` | 77 |
| `gishiri-cutting` | 75 |
| `female-genital-mutilation-in-india` | 73 |
| `infibulation` | 65 |
| `circumcision-and-law` | 63 |
| `foreskin` | 58 |
| `religious-views-on-female-genital-mutilation` | 58 |
| `female-genital-mutilation-in-sudan` | 54 |
| `international-day-of-zero-tolerance-for-female-genital-mutilation` | 53 |
| `clitoridectomy` | 52 |
| `female-genital-mutilation-in-nigeria` | 50 |
| `female-genital-mutilation-in-the-united-states` | 49 |
| `cultural-views-on-circumcision-aesthetics` | 47 |
| `mohel` | 47 |
| `circumcision-surgical-procedure` | 46 |
| `ulwaluko` | 45 |
| `khitan-circumcision` | 44 |
| `female-genital-mutilation-laws-by-country` | 43 |
| `circumcision-controversy-in-early-christianity` | 42 |
| `phimosis` | 41 |
| `penile-subincision` | 38 |
| `religion-and-circumcision` | 36 |
| `female-genital-mutilation-in-the-gambia` | 32 |
| `brit-shalom-naming-ceremony` | 31 |
| `foreskin-man` | 31 |
| `female-genital-mutilation-act-2003` | 30 |
| `prohibition-of-female-circumcision-act-1985` | 30 |
| `foreskin-restoration` | 24 |
| `history-of-circumcision` | 20 |
| `female-genital-mutilation-in-new-zealand` | 18 |
| `prevalence-of-circumcision` | 18 |
| `female-genital-mutilation-in-the-united-kingdom` | 15 |
| `children-act-1989-amendment-female-genital-mutilation-act-2019` | 13 |
| `meatal-stenosis` | 10 |
| `circumcision-in-the-bible` | 8 |
| `prevalence-of-female-genital-mutilation` | 8 |
| `paraphimosis` | 7 |
| `stapler-circumcision` | 7 |
| `restoration-device` | 6 |
| `circumcision-in-brunei` | 5 |
| `forced-circumcision-of-minors-in-south-korea` | 4 |
| `redundant-prepuce` | 4 |
| `circumcision-in-china` | 3 |
| `cost-of-circumcision-surgery-in-chaozhou` | 1 |

## Sample passages (first 5)

### circ-ashley-montagu-resolution-s0001

Article: `ashley-montagu-resolution` · side: `anti`

> The Ashley Montagu Resolution is a 1996 declaration adopted by acclamation at the Fourth International Symposium on Sexual Mutilations, held at the University of Lausanne in Switzerland, petitioning the International Court of Justice to rule that non-therapeutic genital cutting of children—encompassing both female genital mutilation and male circumcision—violates core provisions of the United Nations Universal Declaration of Human Rights and the Convention on the Rights of the Child, including bans on torture, cruel treatment, and harmful traditional practices. [1]

### circ-ashley-montagu-resolution-s0003

Article: `ashley-montagu-resolution` · side: `anti`

> Drafted by developmental neuropsychologist James W. Prescott and named in honor of British-American anthropologist Montague Francis Ashley Montagu (1905–1999), the resolution pays tribute to Montagu's lifelong advocacy for child well-being, the primacy of affectionate touch in neurodevelopment, and opposition to dehumanizing customs, framing genital cutting as antithetical to these principles. [1]

### circ-ashley-montagu-resolution-s0005

Article: `ashley-montagu-resolution` · side: `anti`

> Its preamble invokes prior anti-mutilation statements from symposia, humanist groups, and World Health Organization resolutions targeting harmful traditions, asserting that all forms of child genital modification inflict irreversible physical and psychological harm without consent or medical necessity, thereby breaching children's rights to bodily integrity, health, and protection from abuse.

### circ-ashley-montagu-resolution-s0007

Article: `ashley-montagu-resolution` · side: `anti`

> The resolution demands that governments legislate outright bans, petition the ICJ for an advisory opinion, and launch public education campaigns to counter cultural myths and highlight documented risks such as infection, sexual dysfunction, and trauma, while endorsing broader UN treaty enforcement. [2]

### circ-ashley-montagu-resolution-s0009

Article: `ashley-montagu-resolution` · side: `pro`

> Though it secured endorsements from figures like Francis Crick and Jonas Salk and aimed to mobilize heads of state and organizations like Amnesty International, the petition yielded no formal ICJ ruling, and its undifferentiated condemnation of male neonatal circumcision as mutilation has drawn criticism for overlooking empirical evidence of benefits, including a 50–60% reduction in heterosexual HIV acquisition and lower urinary tract infection rates, as affirmed by health authorities in high-prevalence contexts. [2] [3]

