# Recheck of the 2026-10-15 run (second checker)

Done 2026-10-15 by a second Grok Bot session that did not make the original judgments. It is the same kind of model as the first checker, so this is a separate pass, not a separate person. Row-level results: `recheck_log.csv`. No existing run file was edited.

What was not blind: I had seen the run's README summary (counts and headline errors) before starting. For the verdict sample (step 3) I wrote my verdicts from article text + cached source text with the original verdict and reason columns hidden, saved them, then compared.

## 1. Snapshot
Re-fetched https://grokipedia.com/page/Baruch_Spinoza (HTTP 200, 631,317 bytes, same size). The sha256 differs from the snapshot, but only the per-request script nonces differ. Re-parsing with `grokaudit.py parse` gives 401 sentences and 153 sources, field-for-field identical to `data/claims.csv` and `data/sources.csv`. Confirmed.

## 2. Offset
- `sources.csv` #153 is merriam-webster.com/dictionary/Spinozism; #5 is the Cambridge TTP book. Inline [5] appears only in C003. Confirmed.
- 390 inline markers; [154]-[162] are 9 markers in C393, C395-C397, C399-C401, past the 153-entry list. Confirmed.
- Seeded sample (seed 20261015) of 32 markers, judged by source title plus word share in the cached text: [6]-[90] 12 markers: 5 clearly fit n-1, 7 ambiguous (neighbouring sources on the same topic), none clearly fit n. [91]-[153] 12 markers: 10 clearly fit n-10, 2 unclear. [154]+ 5 markers: all 5 fit n-10. [3] (3 markers): no shift, as stated. The offset claim holds; the [6]-[90] -1 shift is the weaker-evidenced block because neighbouring sources overlap in topic.

## 3. Verdict sample (seed 1015, 14 per verdict type, 84 rows)
Same verdict as the original: 46 of 84 (55%).

| original verdict | same / 14 |
|---|---:|
| uncited | 14 |
| unverifiable | 9 |
| miscited | 8 |
| unsupported | 7 |
| supported | 4 |
| partly supported | 4 |

Most differences are on the fuzzy lines between miscited/unsupported and supported/partly supported, and many are reasonable either way. Every disagreement, with the original reason, is in `recheck_log.csv` (check = verdict_sample). Errors in my own pass: C030 (I said unsupported; [3] NEH does say the business "was importing dried fruit", so the original partly supported is right).

**Main finding: the "as linked" column partly uses the intended source.** In 37 rows marked supported (6) or partly supported (31) as linked, every [n] in the reason is a source that is not linked from that sentence (it is the n-1 or n-10 source). Examples: C189 linked [77], reason quotes [76]; C288 and C296 linked [60], reason uses [59]; C114 linked [12], reason quotes [11] ("was to The Hague"); C119's "He left no will" is in [11], not linked [12]. List: C027 C035 C054 C083 C092 C114 C123 C126 C127 C131 C132 C143 C174 C176 C181 C185 C189 C193 C195 C198 C205 C208 C255 C267 C268 C270 C272 C288 C296 C301 C303 C305 C307 C322 C356 C379 C389. Some linked sources may also support these sentences, but this was not shown. So the as-linked supported (38) and partly supported (115) counts are likely too high, and miscited (86) likely too low. These rows need re-judging against the linked source before the as-linked numbers are published.

Other point: C020 says the SEP gives the mother's death in 1638; "1638" does not appear in the cached [12] text.

## 4. Headline errors (16)
All 16 confirmed against the cache or the Elwes text:
- C120: ref049 has "close to the grave of Johan de Witt"; no "Grotius".
- C368: no "papal" or "pope" in refs 123-125 or 133-135, except ref124, which mentions the Papal Index in 1738 for a different book. ref049 has "banned by the States of Holland".
- C108: ref053 has "3rd June, 1665".
- C313: ref092 has "TP:XVI:204".
- C383: ref134 has "I believe not in a God who concerns himself with the fate and the doings of mankind, but in Spinoza’s God, who reveals himself in the harmony of all that exists", which was the reply to Rabbi Herbert S. Goldstein. Note: ref136 (not cited by C383) has the article's exact wording ("orderly harmony of what exists ... fates and actions") and calls it a reply to a telegram. The quote is real; "interview" is the error.
- C043: ref003 says he went "to have himself declared an orphan so as to be relieved of the debts he inherited from his father".
- C064: ref033 has "Peter Serrarius, who sponsored him since his expulsion".
- C118: ref017 says "probably of a pulmonary disease, in the presence of his friend Meyer"; "Schuller" does not appear in refs 9, 17 or 18.
- C173 and C177: Elwes line 1747 has "the fourth proportional is six"; no "2 + 2".
- C209: Elwes line 3926 (E4P18 note) has "virtue is nothing else but action in accordance with the laws of one's own nature"; E4P37 (line 4190) is different.
- C123: E1D6 (line 34) defines God, not substance, as absolutely infinite.
- C158: E1D4/D5 (lines 29-31) define attribute and mode; "conceived through itself" is E1P10.
- C199: "about two hundred feet" is at line 1628 (E2P35 note) and line 3695 (E4P1 note), not at E2P17.
- C201: E2P3 (line 991) is "In God there is necessarily the idea...".
- C291: E1P7 (line 93) is "Existence belongs to the nature of substances"; the order-and-connection proposition is E2P7 (line 1045).

## 5. Ethics
grokAlign re-cloned at 90340d11. The sha256 of both files equals METHOD.md (43845011...68621, 52e36c09...4c079c). The 8 mismatches are the 8 above (C123 C158 C173 C177 C199 C201 C209 C291); all are confirmed. Note that 4 of them (C199 C209 C291 C158) are right in content but give the wrong locator; "mismatch" here includes locator errors. 20 sampled matches (seed 2015): 20 hold in content. Minor notes: C139 (E2P1 covers thought only; extension is E2P2), C142 (finite modes are E1P28, not E1P21), C126 (the article's "each of which" vs Elwes "of which each").

## 6. Quotes
`check_quotes.py` re-run: 181 quotes, 0 not found. A stricter check of my own (the quote must be in a source named in the same reason, the Elwes text or the article) leaves 7 loosely attributed quotes: C045, C180, C232, C242, C287, C330 (x2). All exist verbatim somewhere in the cache, but not in the named source. Example: C232 gives "something of it remains which is eternal" as E5P23, but that wording is in refs 11 and 124 (a modern translation), not in Elwes. The script only checks that the text exists anywhere in the corpus, not that it is attributed correctly.

## 7. Charts and counts
The verdict chart (38/115/38/86/48/76 as linked; 133/132/34/0/26/76 intended) and the Ethics chart (82/8/47) equal the claim_log.csv counts. METHOD: 401 sentences = 325 cited + 76 uncited; 390 markers; 9 dangle. All consistent. Cosmetic: the title of primary_text_check.png is clipped ("...Ethics tex").

## 8. Fallacy flags (leads, not verdicts), against v0.6.1 conditions
C261, C342, C381: reasonable flags. C046, C113, C159: reasonable as possible issues (C159 straw-man needs Descartes' own wording). C129: a reasonable lead, but closer to a possible issue than a flag, because it reports a comparison and doesn't argue a claim. C401, C314: weak leads (the value words are mild).

## Overall
The snapshot, offset, headline errors, Ethics mismatches, quote existence and chart arithmetic hold up. The weak point is the as-linked verdict column: 37 supported/partly-supported rows rest on the intended source, not the linked one, and the 84-row sample matched 55%. Treat the as-linked counts as provisional until those 37 rows are re-judged against the linked source.
