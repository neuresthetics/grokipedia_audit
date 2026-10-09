# Labeling instructions (model labeling of all 13,199 sentences)

These are the exact instructions the labeling model followed. To redo the labels, give these instructions to a different model or a person and run the same tool. Labels are written by an AI model, not a person.

## Tool

From `survival/scripts/`:

```
python3 label_queue.py status              # progress
python3 label_queue.py next 80             # next batch: up to 80 sentences of one article
python3 label_queue.py record <slug> --by <labeler-name> <<'EOF2'
s0001-s0080:N s0004:P s0012:A
EOF2
```

`next` shows only the article title, its group (male or FGM) and the sentences. Two sentences before and two after are marked `ctx`; they are context only and are not labeled in this batch. Citation markers are removed for reading. The tool never shows rule labels or reviewer flags, and the labeler must not open `work/sentences_stage1.csv`, `rules.py`, the flags CSVs or any results file while labeling.

Answers: give a range as `not_argument` first (`sFIRST-sLAST:N`), then list each pro (`:P`) or anti (`:A`) sentence. Every sentence in the batch must be covered. Progress is saved after every `record` call in `labels/model_labels.csv`, so the job can stop and resume at any batch.

## The question for each sentence

Does this sentence, as written, make an argument for or against the practice?

- **P (pro):** for the practice or playing down its harm. That includes claimed benefits, safety, low complication rates, no effect on sexual function, a right to do it (parental or religious freedom), and dismissing its critics. In FGM articles, pro means defending FGM or playing down its harm, including rationales such as hygiene, chastity or marriageability that are put forward as reasons for it.
- **A (anti):** against the practice. That includes harms, complications, deaths, rights, consent or ethics objections, critics' stated arguments, and calls to end it.
- **N (not_argument):** everything else. That covers descriptive or neutral sentences: definitions, procedure steps, history, prevalence figures, and statutes or court rulings stated as facts. It also covers sentences balanced with no net direction, and claims about something else. "Something else" includes whether a law, campaign or programme worked or was enforced (policy-effect claims), race science, treatments for unrelated conditions, the restoration device as a product, and comic-book plots.

## Rules

1. **Reported arguments count.** "Critics argue X" is labeled by X's side, even though the article only reports it.
2. **R5, which practice:** judge the side for the practice of the article's group. In a male circumcision article, a sentence that sets male circumcision apart from FGM as less harmful is P, and a sentence only about FGM that does nothing for the male circumcision case is N. In an FGM article, a sentence about male circumcision's benefits that is used to show FGM is worse is A. In articles about related practices (subincision, traditional initiation, infibulation), the practice is the one the article is about.
3. **Mixed sentences** ("X, though Y") are labeled by the side the sentence ends up favoring. If the sentence is truly balanced, it is N.
4. **Context sentences** may be read to understand a sentence (for example, what "this" refers to), but each sentence is labeled on its own claim.
5. **Uncertain means N.** If a sentence is not clearly an argument, label it N. Do not label by topic alone: a sentence that mentions complications in a neutral, descriptive way is N.
