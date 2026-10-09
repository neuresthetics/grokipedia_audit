# Tagging instructions: which medical arguments rest on the cancer-prevention claim?

You are tagging pro argument sentences from Grokipedia articles on male circumcision. Each sentence favours the practice, was not marked down in this audit's earlier checks, was tagged earlier as relying on medical or scientific data, and mentions cancer (or HPV or cervical) in itself or in the two sentences on either side. Your tags are recorded as a model's judgment, not a person's.

## What this count is, and what it is not

Some critics say cancer prevention is not a valid reason for circumcision: penile cancer is rare, and preventing cancer by removing tissue proves too much. This job counts **how many of these medical arguments would lose their point if the cancer-prevention claim were set aside**. It is a **what-if count**. A tag of C means only "depends on the cancer claim". It is **not** a finding that the claim is wrong. Penile cancer is rare in absolute terms, but how much a rare benefit should weigh is a question this audit does not settle. Do not judge whether any claim is correct or how much it should count.

## The question

**Does this sentence's point rest on a cancer-prevention claim?** Give exactly one tag.

| Tag | Use it when… |
|---|---|
| **C** | The point rests on preventing cancer: penile cancer, or cervical cancer in female partners via HPV, or another cancer named as a benefit of circumcision. |
| **K** | The point rests on a non-cancer claim (HIV or other infections, UTIs, phimosis, hygiene, safety, complications, sexual function, guidance), even if cancer is mentioned nearby. |
| **N** | The sentence mentions cancer but does not rely on cancer prevention as a benefit: history, a bare reported view, a description, a critic's rebuttal, or a statement of a limitation. Explain briefly in the note. |

## Tie-break rules

1. **Mixed benefits.** If the sentence combines cancer prevention with another benefit (for example "reduces UTIs and penile cancer"), imagine the cancer part removed. Tag **C** only if no point is left; otherwise tag **K**.
2. **HPV.** HPV protection offered as a way to prevent cervical or penile cancer is C. HPV infection named only as a sexually transmitted infection, with no cancer point, is K.
3. **"These benefits" with no benefit named.** Look at the two sentences before it. If the benefits meant are cancer only, tag C; if they include any non-cancer benefit, tag K; if you cannot tell, tag K and say so in the note.
4. **Mechanisms.** A mechanism offered for cancer prevention (smegma, chronic inflammation, phimosis leading to cancer) is C when the sentence's point is the cancer outcome. Phimosis as a problem in itself is K.
5. **Reported views.** If the article only reports a view and uses it as its own support, tag by the benefit the view rests on. A bare report or history with no support role is N.
6. Do not judge whether the claim is true or how much it should weigh. Only what the point rests on.

## Examples

All examples below are **invented, generic sentences written for this prompt**. They are not from the articles.

- *(invented)* "Penile cancer occurs almost only in men who were not circumcised." → **C**
- *(invented)* "Lower HPV rates in circumcised men reduce cervical cancer risk in their partners." → **C** (rule 2)
- *(invented)* "The procedure lowers the risk of urinary tract infections and penile cancer." → **K** (rule 1: the UTI point remains)
- *(invented)* "Circumcised men had lower rates of HPV infection in the trials." → **K** (rule 2: infection, no cancer point)
- *(invented)* "Early studies in the 1930s linked the foreskin to cancer." → **N** | history
- *(invented)* "Critics note that penile cancer is very rare in developed countries." → **N** | critic's point, not relied on as a benefit

## What you see

Each item shows the article title, its section, two sentences before and two after, and the sentence to tag (marked `>>`). You may open the article snapshot (`topics/circumcision/articles/<slug>/snapshots/2026-10-01.txt`) for more context.

Do not open anything else in this run: no flag files, scores, earlier passes or tags (including `../sti_dependence/` and `../topic_tags/`), other taggers' answers (`work/tags.csv`), the run README, ANALYSIS.md, WALKTHROUGH.md or charts. Do not search the web. Judge only from the sentence and its article.

## How to answer

One line per item: the tag letter, and a short note after a `|` (required for N, optional otherwise):

```
p0001 C
p0002 K | UTI point remains without the cancer part
p0003 N | history of the claim, not relied on
```

Tags must be one of C, K, N. Recording an item again replaces the earlier answer.
