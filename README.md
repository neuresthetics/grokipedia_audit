![Grok logo under a magnifying glass](docs/img/header.jpg)

# Grokipedia Audit

This repo checks Grokipedia articles against the sources they cite. Grokipedia is xAI's AI-written encyclopedia. Its articles look well sourced, but an AI writer can attach a citation that doesn't say what the sentence claims, or let the numbering slip so that a footnote points to the wrong source. This repo looks for those problems one claim at a time and keeps the evidence next to every finding, so a reader can check the work without having to trust it.

## How it works

Each audit is done by a general-purpose AI agent that follows plain written instructions, with no custom framework, scoring system or private vocabulary. Each article goes through the same steps:

1. **Snapshot.** Save the article as it appeared on the day of the audit, because Grokipedia pages change.
2. **Claim and source.** For each claim, quote what the article says, then quote what the cited source actually says.
3. **Verdict.** Mark the claim *supported*, *miscited* (the source exists but doesn't say this), *unsupported* (the source contradicts it or gives nothing to check) or *uncited*. The article, the source and the judgment are kept as three separate things.
4. **Reasoning check.** Where an article argues rather than reports, its arguments are checked against [fallacy_catalog](https://github.com/neuresthetics/fallacy_catalog), a plain, sourced list of known logical fallacies. A flag is a lead for a reader to follow up, not a verdict.

Every finding records the date and the model that made the judgment. Nothing is presented as a human expert's ruling, and citations or quotes are never filled in from memory.

## Why it's built this way

An audit only helps if people can check it. Plain steps, quoted sources and standard fallacy names let anyone repeat the check and get the same answer. The goal is to make AI-written reference pages more trustworthy, not to argue for a position on any topic.

## Layout

- `topics/<topic>/` holds one folder per topic, with its own README, article list and an `articles/<article>/` folder for each article's snapshots and analyses.
- `docs/` holds shared notes and images.
- `tools/` holds scripts for pulling articles and summarizing results.

## Older files

Audits made before October 2026 used substance_lens, a custom framework that has since been retired. It has been replaced by the plain approach described above: a general-purpose agent, written steps and a standard fallacy list, so each finding is easier to see and easier to trust. Those older files will be rechecked or removed as each topic is rebuilt, and until then they shouldn't be read as current findings.

## Credits

The Grok logo in the header image is a trademark of xAI, used here only for identification; this repo is not affiliated with xAI. Logo source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Grok-feb-2025-logo.svg).
