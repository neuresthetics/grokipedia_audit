# Tagging instructions: what does each surviving pro argument rely on?

You are tagging pro argument sentences from Grokipedia articles on male circumcision. Each sentence favours the practice and was not marked down in this audit's earlier checks. Your tags are recorded as a model's judgment, not a person's.

## The question

**What kind of support does this sentence rely on to make its point?** Give exactly one tag.

| Tag | Type | Use it when the sentence's point rests on… |
|---|---|---|
| **M** | Medical or scientific data | trial results, infection or complication rates, risks and benefits, biological mechanisms, clinical guidance from medical bodies, epidemiology, statistics, cost-effectiveness |
| **E** | Ethics, rights or law | consent, autonomy, parental rights, best interests, legal standing, court rulings, human rights instruments, policy or regulatory arguments |
| **R** | Religion, culture or tradition | religious commands, rituals, customs, community identity, social norms, the history or continuity of the practice |
| **O** | Other, mixed or framing | aesthetics or personal preference, framing or summary statements with no clear support, sentences that rely about equally on two types, anything that fits none of the above |

## Tie-break rules

1. **Tag what the point rests on, not the topic.** A sentence about a religious rite that argues it is safe because complication rates are low is **M**. A sentence about HIV programmes that argues they respect consent is **E**.
2. **Conclusion from data.** If a sentence reaches an ethical or policy conclusion and its only stated support is medical data ("benefits outweigh risks, so parents may choose"), tag **M**: the data carry the point. If it weighs data against a rights claim and the rights reasoning carries the conclusion, tag **E**.
3. **Medical bodies.** A position of a medical body (AAP, CDC, WHO) based on evidence is **M**. A legal ruling or a rights convention is **E**, even if it mentions health.
4. **History.** The history or persistence of the practice is **R**. The history of medical research (when trials were run) is **M**.
5. **Social benefit.** Stigma, belonging and peer acceptance are **R** (social norms). Population health effects (herd effects, healthcare burden) are **M**.
6. **Two types equally, or neither clearly:** **O**. Use O sparingly; most sentences lean one way.
7. **Do not judge whether the argument is good or true.** Only what it relies on.

## Examples

All examples below are **invented, generic sentences written for this prompt**. They are not from the articles.

- *(invented)* "Trials found that the procedure lowered infection rates by half over two years." → **M**
- *(invented)* "Because complications occur in fewer than 1 in 200 procedures, the benefits outweigh the risks for newborns." → **M** (rule 2)
- *(invented)* "Parents routinely decide on medical care for infants who cannot consent, so this decision also falls to them." → **E**
- *(invented)* "The court held that a ban would breach the parents' freedom of religion." → **E** (rule 3)
- *(invented)* "For centuries the rite has marked a boy's entry into the community." → **R**
- *(invented)* "In places where most men undergo the procedure, those who do not may face teasing." → **R** (rule 5)
- *(invented)* "The rite is performed by trained practitioners whose complication rates are low." → **M** (rule 1)
- *(invented)* "Many people simply prefer how it looks." → **O**
- *(invented)* "These considerations together explain the practice's continued support." → **O** (framing with no clear support)

## What you see

Each item shows the article title, its section, two sentences before and two after (for context), and the sentence to tag (marked `>>`). You may open the article snapshot (`topics/circumcision/articles/<slug>/snapshots/2026-10-01.txt`) for more context.

Do not open anything else in this run: no flag files, score files, earlier passes, other taggers' answers (`work/tags.csv`), the run README, ANALYSIS.md or charts. Judge only from the sentence and its article.

## How to answer

One line per item, the tag letter, and optionally a short note after a `|`:

```
t0001 M
t0002 E | parental proxy consent carries the point
t0003 O | equal parts ritual and infection data
```

Tags must be one of M, E, R, O. Recording an item again replaces the earlier answer.
