# Tagging instructions: which medical arguments rest on the HIV/STI claim?

You are tagging pro argument sentences from Grokipedia articles on male circumcision. Each sentence favours the practice, was not marked down in this audit's earlier checks, and was tagged earlier as relying on medical or scientific data. Your tags are recorded as a model's judgment, not a person's.

## What this count is, and what it is not

Some critics say circumcision gives no protection against HIV or other sexually transmitted infections. This job counts **how many of these medical arguments would lose their point if that HIV/STI protection claim were set aside**. It is a **what-if count**. A tag of H says only that the argument depends on the HIV/STI claim. It is **not** a finding that the claim is true or false; this audit has not checked it. Do not judge whether any claim is correct.

## The question

**Does this sentence's medical point rest on protection against HIV or another sexually transmitted infection?** Give exactly one tag.

| Tag | Use it when… |
|---|---|
| **H** | The point rests on protection against HIV, STIs/STDs, HPV, herpes (HSV-2), syphilis or another sexually transmitted infection, including claims about partners or community transmission, and programmes justified by HIV prevention. |
| **X** | The point rests on a non-STI medical claim: urinary tract infections, phimosis or paraphimosis, balanitis, penile cancer, hygiene, procedure safety, pain and anaesthesia, complication rates, sexual function or sensitivity data, healing, cost, or clinical guidance not about STIs. |
| **N** | Medical in form but does not depend on a benefit claim: a description of anatomy or technique, a reported view without the article relying on it, a historical claim (when trials ran, when a policy was issued), or a statement of a limitation. Explain briefly in the note. |

## Tie-break rules

1. **Mixed benefits.** If the sentence combines HIV/STI protection with another medical benefit (for example "reduces HIV and UTIs"), imagine the HIV/STI part removed. Tag **H** only if no medical point is left; otherwise tag **X**.
2. **"Benefits outweigh risks" with no benefit named.** Look at the two sentences before it. If they show the benefits meant are HIV/STI only, tag H; if they include any non-STI benefit, tag X; if you cannot tell, tag X and say so in the note.
3. **Penile cancer and cervical cancer.** Penile cancer is X. Cervical cancer in partners via HPV is H (it is a sexually transmitted infection claim).
4. **Mechanisms.** A mechanism offered for HIV/STI protection (target cells, keratinisation against viral entry) is H. A mechanism for hygiene or UTIs is X.
5. **Safety and complications** (low complication rates, anaesthesia, healing) are X even when the article mentions HIV programmes, unless the sentence's point is that the programme prevents infection.
6. **Reported views.** If the article only reports someone's view ("The WHO recommends…") and uses it as its own support, tag by the benefit the view rests on. If it is a bare report or history with no support role, tag N.
7. Do not judge whether the claim is true. Only what the point rests on.

## Examples

All examples below are **invented, generic sentences written for this prompt**. They are not from the articles.

- *(invented)* "Trials found the procedure lowered HIV acquisition in men by about half." → **H**
- *(invented)* "Lower infection rates among men also reduce transmission to their female partners." → **H**
- *(invented)* "The procedure reduces the risk of HIV and of urinary tract infections in infancy." → **X** (rule 1: the UTI point remains)
- *(invented)* "Circumcised men have fewer cases of penile cancer." → **X**
- *(invented)* "Complications are rare when trained staff use sterile instruments." → **X** (rule 5)
- *(invented)* "The cells of the inner foreskin are thought to be an entry point for the virus." → **H** (rule 4)
- *(invented)* "The first of the three trials began in 2002." → **N** | historical claim
- *(invented)* "The procedure removes the foreskin, which covers the glans." → **N** | anatomy description

## What you see

Each item shows the article title, its section, two sentences before and two after, and the sentence to tag (marked `>>`). You may open the article snapshot (`topics/circumcision/articles/<slug>/snapshots/2026-10-01.txt`) for more context.

Do not open anything else in this run: no flag files, score files, earlier passes or tags, other taggers' answers (`work/tags.csv`), the run README, ANALYSIS.md, WALKTHROUGH.md or charts. Do not search the web. Judge only from the sentence and its article.

## How to answer

One line per item: the tag letter, and a short note after a `|` (a note is required for N, optional otherwise):

```
h0001 H
h0002 X | UTI point remains without the HIV part
h0003 N | history of the trials, no benefit relied on
```

Tags must be one of H, X, N. Recording an item again replaces the earlier answer.
