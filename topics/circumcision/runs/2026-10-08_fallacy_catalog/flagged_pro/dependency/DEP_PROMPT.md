# Dependency judging instructions (step 6, second layer)

You are judging whether a **survivor** depends on a **prior**. This is one step of a public audit of Grokipedia articles on male circumcision. Your judgment is recorded as a model's judgment, not a person's.

- **Survivor:** a pro argument sentence that kept at least 1 point after the fallacy check.
- **Prior:** one of the 61 pro argument sentences that at least one AI reviewer flagged against fallacy_catalog v0.6.1. You are shown the prior's text and the flagged step, in the reviewer's words.

## The question

Does the survivor **use the prior's claim or conclusion as a premise**? Answer Y (depends) or N (does not depend).

Answer **Y** only if at least one of these holds:

1. **Builds on it.** The survivor draws a further conclusion from the prior's claim ("therefore", "thus", "this means", "so", "accordingly"), or its argument would lose its support if the prior's claim were removed.
2. **Refers back to it.** The survivor points to the prior with words like "this", "these benefits", "such data", "as noted", "this evidence", and that referent is the prior's claim, not some other sentence.
3. **Relies on the same claim.** The survivor restates the specific claim the flag is about and leans on it. Example: adult HIV trial results applied to infants. Elsewhere in the same article or in another article, it rests on that same specific claim, not just the same topic or the same general conclusion.

Answer **N** if:

- They are only on the same topic (both about HIV, both about pain, both pro).
- The survivor reaches a similar conclusion by its own, different reasoning or evidence.
- The survivor only **reports** a position ("The AAP concluded that…", "Proponents argue…") without the article adopting it as a premise.
- The survivor is a premise *for* the prior rather than built on it, unless it also restates the flagged claim (rule 3).
- The survivor shares the prior's general conclusion (for example "benefits outweigh risks") but not the specific step the flag is about.
- You are unsure. Uncertain means N.
- The survivor is itself a flagged sentence and the link is only that it makes the same flagged claim (rule 3). Its own flag already cost it a point for that claim. A flagged survivor can still depend on a different prior by rule 1 or 2.

## What you see

Each candidate shows:
- the survivor, with the sentence before it (the full article is in the snapshot if more context is needed);
- the prior, with its article, the flagged step and the reviewer's reason;
- why the pair was pre-selected: W means nearby in the same article; K means a shared keyword for a claim.

The pre-selection is only a cheap filter. Most candidates should be N.

## How to answer

One line per candidate:

```
c0001 N
c0002 Y the survivor says "these benefits justify…", where "these benefits" are the prior's adult HIV trial figures
```

For Y, give a one-line reason naming the link. Keep it about the reasoning, and do not add facts. The link type, same-article or same-claim, is set by the script: it is same-article when both sentences are in one article, otherwise same-claim.

Do not open the flag files, the scores or other judges' answers. Judge only from what is shown.
