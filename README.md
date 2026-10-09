![Grok logo under a magnifying glass](docs/img/header.jpg)

# Grokipedia Audit

This repo checks Grokipedia articles against the sources they cite. Grokipedia is xAI's AI-written encyclopedia. Its articles look well sourced, but an AI writer can attach a citation that doesn't say what the sentence claims, or let the numbering slip so that a footnote points to the wrong source. This repo looks for those problems one claim at a time and keeps the evidence next to every finding, so a reader can check the work without having to trust it.

## How it works

Each audit is done by a general-purpose AI agent that follows plain written instructions, with no custom framework or private vocabulary. The only score is the simple, documented point count in step 5. Each article goes through the same steps:

1. **Snapshot.** Save the article as it appeared on the day of the audit, because Grokipedia pages change.
2. **Claim and source.** For each claim, quote what the article says, then quote what the cited source actually says.
3. **Verdict.** Mark the claim *supported*, *miscited* (the source exists but doesn't say this), *unsupported* (the source contradicts it or gives nothing to check) or *uncited*. The article, the source and the judgment are kept as three separate things.
4. **Reasoning check.** Where an article argues rather than reports, its arguments are checked against [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog), a plain, sourced list of known logical fallacies. A flag is a lead for a reader to follow up, not a verdict.
5. **Survival scoring.** An AI model labels every sentence *pro*, *anti* or *not an argument*. Each argument starts with 3 points and loses 1 for each reviewer that flagged it. The result shows what share of each side's arguments went unflagged; unflagged means not flagged, not proven true. See the circumcision benchmark's [method](topics/circumcision/runs/2026-10-08_fallacy_catalog/survival/METHOD.md).
6. **Flagged pro arguments.** In the male circumcision articles, the pro arguments that lost at least one point are sorted by the kind of flaw the reviewers named, using fallacy_catalog's own categories. Each kind gets its share, how the move works, verbatim quotes, and the reply that exposes it, quoted from the catalog entry where it has one. Then each surviving pro argument loses 1 point for every flagged one it depends on as a premise, and in a third pass the remaining pro arguments are rechecked against the catalog, losing 1 point per fallacy flagged (both judged by AI models). Pro only: anti arguments were checked only in step 5 and were not put through pass 2 or pass 3, so comparing pro and anti after pass 3 is tilted against pro. See the circumcision benchmark's [write-up](topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/FLAGGED_PRO.md).
7. **Topic tagging.** The male circumcision pro arguments that kept all 3 points after step 6 are each tagged with the one kind of support they rely on: medical or scientific data; ethics, rights or law; religion, culture or tradition; or other. About three in four rest on medical data. The tags are AI-tagged (4 separate model sessions), one type per sentence, so mixed sentences are forced into one type, and not blind. See the circumcision benchmark's [tags](topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/topic_tags/TAGS.md).

Every finding records the date and the model that made the judgment. Nothing is presented as a human expert's ruling, and citations or quotes are never filled in from memory.

## Why it's built this way

An audit only helps if people can check it. Plain steps, quoted sources and standard fallacy names let anyone repeat the check and compare results. The goal is to make AI-written reference pages more trustworthy, not to argue for a position on any topic.

## Layout

- `topics/<topic>/` holds one folder per topic, with its own README, article list and an `articles/<article>/` folder for each article's snapshots and analyses.
- `docs/` holds shared notes and images.
- `tools/` holds scripts for pulling articles and summarizing results.

## Older files

Audits made before October 2026 used substance_lens, a custom framework that has since been retired. It has been replaced by the plain approach described above: a general-purpose agent, written steps and a standard fallacy list, so each finding is easier to see and easier to trust. Those older files will be rechecked or removed as each topic is rebuilt, and until then they shouldn't be read as current findings.

## Credits

The Grok logo in the header image is a trademark of xAI, used here only for identification; this repo is not affiliated with xAI. Logo source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Grok-feb-2025-logo.svg).

## How it works, continued

Steps added after the list above (appended here, since this repo's commits only append to the end of files).

8. **What-if checks.** The medical arguments from step 7 are tagged by whether their point rests on the HIV/STI protection claim, and (for those near a cancer keyword) on the cancer-prevention claim. About two in five rest on one of the two. A tag means "depends on the claim", not that the claim is wrong; the audit does not check either claim. The tags are AI-tagged, one tag per sentence, and not blind. See the circumcision benchmark's [what-if counts](topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/cancer_dependence/CANCER_DEPENDENCE.md). Added up over all 971 pro arguments, with those premises taken as true, 38% are flagged by the audit or set aside and 62% are left ([total what-if](topics/circumcision/runs/2026-10-08_fallacy_catalog/flagged_pro/whatif_total/TOTAL_WHATIF.md)); this is conditional on the premises, the first of which contradicts the trials the articles cite.
