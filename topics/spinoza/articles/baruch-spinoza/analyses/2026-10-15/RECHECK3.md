# RECHECK3: third recheck of the 2026-10-15 Spinoza audit (local, not pushed)

## Scope
Seed 20261015. 196 unique rows: 68 rows changed in CORRECTIONS.md, 72 mixed linked/unlinked rows, a stratified random sample of 60 other rows (S3 P3 U12 M27 X15; U/M rows were checked for the reverse error), and 40 rows for the corrected-column check. Per-row results are in recheck3_log.csv.

## How independent or blind this check was
This check was **not fully blind or independent**:
- It was run by the same kind of model that ran the earlier checks.
- Before judging, I had already seen the parent conversation's summaries, the counts in CORRECTIONS.md, the first 8 rows of its table (C020–C068), and its "Not changed" notes.
- The verdict columns were hidden while I judged. Inputs were built only from claims.csv, the source list and the cache.
- I saved my verdicts before comparing (sha256 330b9828…87cd1, frozen 11:40 PT).
- I judged from keyword-window excerpts plus targeted greps, not a full reading of every source.
- After freezing, I corrected the wording of 9 evidence quotes so they are verbatim. The verdicts did not change.

## Same-verdict rates
| Category | As linked, exact | As linked, U and M merged | Corrected, exact |
|---|---|---|---|
| Corrections (68) | 37/68 (54%) | 51/68 (75%) | 45/68 (66%) |
| Mixed (72) | 42/72 (58%) | 42/72 (58%) | 48/72 (67%) |
| Random sample (60) | 35/60 (58%) | 41/60 (68%) | 42/60 (70%) |
| Corrected-column sample (40) | 20/40 (50%) | 27/40 (68%) | 26/40 (65%) |
| All rows (196) | 114/196 | | 133/196 |

Most common disagreements:
- As linked: P→U 13, S→P 13, U→M 11, U→P 11, M→U 9, P→S 9, M→X 9, X→U 4.
- Corrected: S→P 30, P→S 12, P→U 10, U→P 5.

Many of these are judgment calls on the S/P and U/M borderlines. I recommend changing only the rows below.

## Recommendations
- **C087** (high): recommended linked P, intended S. intended X->S: [41] and [42] are cached with content (1,086 and 1,320 bytes, hashes match the manifest); fetch_log marked them 'bot wall' only because the pages are short. [41]: 'Between early September 1669 and early February 1671, Spinoza rehoused from Voorburg to The Hague, where he rented rooms at the Stille Veerkade (now no. 32)'. As linked P stays (early 1671 only in [41]).
- **C085** (high): recommended linked U, intended X. as linked X->U: [41] is cached and readable (see C087); it is about the Stille Veerkade lodgings, not the TTP thesis.
- **C118** (high): recommended linked U, intended P. as linked P->U: the as-linked reason quotes Monoskop, which is [17]; the sentence links [9] and [18]. [9] has no 1677 death (0 hits for 1677/Schuller).
- **C192** (high): recommended linked M, intended S. as linked P->M: the only linked source is [78] SEP psychology; the reason leans on [77] Gutenberg Ethics, which is the n-1 source. Intended P->S: [77] has E2P16-17 text.
- **C200** (high): recommended linked M, intended S. as linked P->M: linked [78] only; reason leans on E2P18 / [77]. Intended P->S: [77] 'PROP. XVIII. If the human body has once been affected by two or more bodies at the same time'.
- **C121** (high): recommended linked U, intended P. as linked P->U: the reason's support is the Elwes text, not linked [60]; [60] uses 'conceived through itself' only of extension. Ethics check (match) is unaffected.
- **C299** (high): recommended linked U, intended U. as linked and intended P->U: the reason's ban evidence comes from [94], which this sentence does not cite; [106] and [96] have no bans or Leibniz.
- **C062** (medium): recommended linked U, intended X. intended U->X: the reason uses [24], which is not cited here; intended [32] is a paywall page, so the intended source could not be read.
- **C021** (medium): recommended linked U, intended S. as linked P->U: [12] SEP says only 'Amsterdam's Portuguese-Jewish community'; no Marrano/converso text (0 hits). The sentence's point is Marrano descent.
- **C178** (medium): recommended linked U, intended U. P->U both: reason is only '[72]/[73] general'; neither says intuition is the mind's highest freedom or that no method is given.
- **C329** (medium): recommended linked U, intended U. P->U both: reason is only '[50] ... and [49] EMLO general'; no passage on a guarded style.
- **C298** (medium): recommended linked U, intended P. as linked P->U: [60] SEP physical theory is about inertia and conatus of bodies; reason is only '[60]/[59] general'.
- **C166** (medium): recommended linked U, intended P. as linked P->U: reason is '[73]/[72] general'; linked [73] is about the geometric method in general.
- **C340** (medium): recommended linked U, intended P. as linked P->U: linked [112] is a JSTOR challenge page and [113] is a PSR paper; the theistic reading is in [103] (n-10).
- **C353** (medium): recommended linked U, intended P. as linked P->U: the Oldenburg passage the reason cites is in [111] (n-10), not linked [121] (Diderot).
- **C096** (medium): recommended linked P, intended P. reverse error, as linked U->P: linked [46]: 'supporting himself by grinding lenses for microscopes and telescopes' supports the first clause.
- **C296** (medium): recommended linked P, intended P. reverse error, as linked U->P: linked [60] quotes the Part IV preface: 'we conceive that his power of acting ... is increased or diminished'.
- **C301** (medium): recommended linked P, intended P. reverse error, as linked U->P: linked [46]: 'All of his work, including the “Ethics,” was left in manuscript form for his friends to print after his death'.
- **C268** (low): recommended linked P, intended P. reverse error, as linked U->P: linked [46]: 'more likely than monarchy or aristocracy to preserve libertas philosophandi'.
- **C302** (low): recommended linked P, intended P. reverse error, as linked U->P: linked [46] describes the TTP's freedom defence; the TP side is not in [46].
- **C050** (note): recommended linked P, intended U. verdicts can stay; the reason says IEP 'mentions Collegiant/Mennonite friends' but [11] has 0 hits for Collegiant/Mennonite/Quaker; it says 'so-called ‘free-thinking’ Protestants – dissenters from the dominant Calvinism'. Reason text should be fixed.

## Impact on the headline counts
- High-confidence changes only:
  - As linked: S 30, P 88→82, U 67→72, M 92→94, X 48→47, N 76.
  - Intended: S 132→135, P 132→129, U 35, X 26, N 76.
- High- and medium-confidence changes: as linked is about S 30, P 81, U 73, M 94, X 47.

## Script reruns
- check_quotes.py: 234 quotes checked, 0 not found.
- consistency.py: 0 S/P rows flagged.
- charts.py, regenerated in /tmp: all 3 PNGs are byte-identical to docs/img/spinoza/2026-10-15.
- The counts in verdicts.psv match the README table:
  - As linked: S30 P88 U67 M92 X48 N76.
  - Intended: S132 P132 U35 X26 N76.
  - Ethics: 82 match, 8 mismatch, 47 with no primary text.
- The cache matches all 135 manifest hashes. Elwes sha256 was verified at grokAlign 90340d11.

## All disagreements
Columns: original verdict (linked/intended), my verdict (linked/corrected), recommendation, and my evidence.

| claim | orig L/I | mine L/C | recommendation | my evidence |
|---|---|---|---|---|
| C005 | X/X | U/X | keep original | linked [7] (Curley, biblical scholarship) has no bans/atheism passage; corrected [6] Wiley not cached |
| C006 | P/X | P/P | keep original | [8] JE: "The insistence of Spinoza upon the love of God as the highest quality of human reason"; Enlightenment/biblical-scholarship influence and "remain debated" not stated; [4] thin page |
| C012 | M/P | U/P | keep original | linked [10] abstract has no Hannah/Porto; corrected [9]: "Hannah Deborah Senior, recent immigrants to the Netherlands from Portugal" (Porto and Amsterdam birth not in it) |
| C013 | U/P | M/P | keep original | linked [10]/[11] windows lack "Portuguese Nation"/trade; corrected [9]: "Michael's business was importing dried fruit and nuts, mainly from Spanish and Portuguese colonies" |
| C021 | P/S | U/S | medium: U/S | linked [12] SEP has no Marrano/converso passage (grep: 0 hits); corrected [11] IEP: "son of Marrano parents. They had immigrated to Amsterdam from Portugal in order to escape the Inquisition" |
| C028 | U/P | P/P | keep original | [12] SEP: "one of the star pupils in the congregation's Talmud Torah school"; shaping of worldview and free-thinking contrast is interpretation; [11] IEP has "so-called 'free-thinking' Protestants" |
| C033 | P/P | P/S | keep original | [16] mentions denial of immortality (of da Costa); corrected [15]: "Spinoza was treating God as material, a personal afterlife as mythical, and the Jewish Law false" |
| C036 | U/U | P/P | keep original | [2] Kasher: "some of the ideas that caused the rift between him and the ma'amad and hakhamim might have been inspired by Descartes"; "substance-monist worldview" at that date not stated |
| C040 | P/P | S/S | keep original | [2] Kasher: "Lucas cites the same views of Spinoza against the truth of the Torah and the immortality of the soul" |
| C041 | X/U | X/X | keep original | linked [20] Oxford not cached; [21] Hicks has no da Costa/1640; corrected [19],[20] same gap |
| C043 | U/U | P/P | keep original | [3] NEH: "in 1656, he went to the Dutch authorities to have himself declared an orphan so as to be relieved of the debts he inherited"; claim says it was to "claim his share", which the source does not say |
| C050 | P/P | U/U | note: P/U | linked [11] IEP has no Mennonite/Collegiant merchant support (grep 0 hits for Mennonite/Collegiant); corrected [10] is a Cambridge abstract page |
| C051 | S/S | P/X | keep original | [24]: "Jarig Jelles, Pieter Balling, and Simon Joosten de Vries ... formed the core of his earliest circle"; death dates not stated. Corrected [23] not cached |
| C052 | S/S | P/P | keep original | [26]: "Het licht op den kandelaar ... Balling was the first to pub- lish some of Spinoza's ideas"; "inward spiritual experience" not stated; corrected [25]: "identified as a Spinozist tract" |
| C057 | P/P | P/S | keep original | [12] SEP: "on July 27, 1656, Spinoza was issued the harshest writ of herem"; lens grinding absent from [12] (0 hits). Corrected [11]: "it was most likely at this time that he took up lens grinding as an occupation" |
| C058 | S/S | P/S | keep original | [29] Boscacci: "lenses of glass ... in telescopes, microscopes and handheld magnifiers"; [30] not cached; corrected [28]: "known for making not just lenses, but also telescopes and microscopes" |
| C059 | U/S | M/S | keep original | linked [29] does not describe precision/patience/isolation; corrected [28]: "a quiet, intense, and solitary occupation, demanding discipline and patience" |
| C062 | U/U | U/X | medium: U/X | linked [33]: "supported himself through Peter Serrarius"; no de Vries annuity (0 hits for Vries); corrected [32] paywall page |
| C065 | M/X | U/X | keep original | linked [35] Spinoza Web Rijnsburg page has no glass dust/respiratory text (0 hits); corrected [34] WSJ not cached |
| C080 | P/P | S/P | keep original | [13]: "a room where Spinoza set up his lense-grinding equipment, where in addition to lenses he also made telescopes and microscopes"; [13] names "Henry Oldenburg"; Boyle not shown in [13]. Corrected [12] SEP has no lens text |
| C085 | X/X | U/X | high: U/X | linked [41] (Stille Veerkade page) is about lodgings, not the TTP thesis; corrected [40] not cached |
| C087 | P/X | P/S | high: P/S | [42]: "Spinoza relocated to The Hague, presumably sometime after 5 September 1669. Initially, he lodged at the Stille Veerkade ... (nos 72–74"; "until early 1671" only in [41]: "Between early September 1669 and early February 1671" |
| C090 | S/P | P/P | keep original | [46]: "Ministers in several cities immediately forbade booksellers to carry the 'Tractatus,' and, in 1674, it was officially banned in the Netherlands"; "democratic freedoms enhance ... sovereignty" not shown |
| C092 | P/S | P/P | keep original | [46]: democracy "of all forms of government the most natural, and the most consonant with individual liberty" (quoted from TTP, not TP); dates 1675-76 not in [46]; [45]: "Tractatus Politicus [Hereafter: TP] was composed in the aftermath of, and perhaps prompted in part by, the events of 1672" |
| C095 | U/S | M/P | keep original | linked [49] EMLO has no Utrecht episode; corrected [48]: "In 1673 Spinoza was invited to Utrecht to meet Louis II, prince de Condé ... returned to The Hague with presents"; "rebuffed" not stated |
| C096 | U/P | P/P | medium: P/P | [46]: "supporting himself by grinding lenses for microscopes and telescopes"; passions/institutions point is in [45]: "institutional structures and procedures channel the natural passions of men towards the common good" |
| C099 | S/S | P/P | keep original | [50] letters cover philosophy, theology and science; clarifying the Short Treatise not shown; [49] EMLO names the Short Treatise |
| C108 | M/U | M/P | keep original | linked [54] is Boxel's ghost letter; corrected [53]: "Spinoza declines further correspondence with Blyenbergh ... (Voorburg, 3rd June, 1665.)" (June, not March; reason given is not "scriptural literalism") |
| C111 | U/S | U/P | keep original | linked [55] index and [51] Letter 15 have no superstition critique; corrected [54] Boxel asks "your opinion about apparitions and ghosts" |
| C113 | P/P | P/U | keep original | [56]: "before venturing to publish his own views on philosophy and religion, which were sure to arouse the hostility o f the Calvinist clergy"; corrected [55] is an index page |
| C114 | U/P | P/P | keep original | [12] SEP: "When Spinoza died in 1677, in The Hague"; May 1670 and lens-grinding not in [12]; corrected [11]: "Spinoza's last move, in 1670, was to The Hague" |
| C115 | S/S | P/S | keep original | [13]: "the Tractatus Politicus, written in 1676–1677"; posthumous publication not in that passage; corrected [12]: "still at work on his Political Treatise; this was soon published by his friends" |
| C117 | P/S | P/P | keep original | [58]: "a lung ailment, exacerbated or even caused by years of inhaling glass dust"; phthisis and 1676 decline not in [58]; [57] calls glass dust "oft repeated, unsupported" |
| C118 | P/P | U/P | high: U/P | linked [9] has no 1677 death (0 hits) and [18] is the herem record; corrected [17]: "In February of 1677, Spinoza dies, probably of a pulmonary disease, in the presence of his friend Meyer" (Meyer, not Schuller) |
| C119 | P/S | P/P | keep original | [12] SEP: "this was soon published by his friends along with his other unpublished writings"; "without a will" and Meyer not in [12]; corrected [11]: "He left no will, but the manuscripts of his unpublished works ... were found in in his desk" |
| C120 | M/U | M/P | keep original | linked [50] (EMT correspondence) has no burial; corrected [49] EMLO: "buried on 25 February in a rented vault in the Nieuwe Kerk, The Hague, close to the grave of Johan de Witt" (contradicts "near the tomb of Grotius") |
| C121 | P/P | U/U | high: U/P | linked [60] SEP physical theory uses "conceived through itself" only of extension, does not give E1D3; corrected [59] same. Content matches Elwes E1D3 ("By substance, I mean that which is in itself, and is conceived through itself") |
| C123 | P/S | P/P | keep original | [60]: "it cannot be divided into multiple substances"; corrected [59]: "it is impossible for two different substances to both have the same attribute"; article's "would limit each other" and "Definition 6: substance" not in sources (D6 defines God) |
| C131 | P/S | S/S | keep original | [61]: "there is nothing separate from God but all things in existence are components of the singular infinite substance"; [60]: "Finite things are but modifications of that substance" |
| C133 | P/P | P/S | keep original | [13]: "Everything happens in Nature with a deterministic necessity"; the quoted Appendix words are not in [13]; corrected [12]: "Nature has no end set before it … All things proceed by a certain eternal necessity of nature"; "There are no 'final causes'" |
| C134 | P/P | P/S | keep original | [60] gives the Ip14/Ip16 overview, no geometry analogy; corrected [59]: "the universe simply follows from God's essence in just the way that the properties of a triangle follow from the essence of the triangle" |
| C143 | P/P | S/P | keep original | [63]: "infinite many things follow from the eternal ... necessity of God's nature in infinitely many modes (see ... Ip16)" (two-column PDF text interleaved) |
| C145 | U/S | M/P | keep original | linked [64] is a Cambridge chapter preview; corrected [63]: "We know only that motion is an immediate ... infinite of extension" |
| C161 | P/S | P/P | keep original | [71] (Elwes Ethics 2) on adequate and inadequate ideas following "by the same necessity"; corrected [70]: "The mind ... thinks nothing but its body's affections" |
| C163 | S/S | P/S | keep original | [72]: first kind "through the senses in a way which is mutilated, confused, and without order for the intellect"; corrected [71]: "(2.) From symbols ... I shall call both these ways of regarding things knowledge of the first kind, opinion, or imagination" |
| C166 | P/P | U/P | medium: U/P | linked [73] (IEP Geometrical Method) is about the method generally; corrected [72]: first kind "mutilated, confused, and without order for the intellect"; "useful for survival and communication" not in either |
| C171 | S/S | P/P | keep original | [72]: reason refers to the ability to "perceive many things and form universal notions…from the fact that we have common notions and adequate ideas"; "principle of contradiction" and "innate capacity" not in source |
| C174 | U/S | M/S | keep original | linked [73] silent; corrected [72]: "reason cannot grasp the essences of singular things, while intuition can" |
| C176 | P/P | S/P | keep original | [70]: "Blessedness consists in loving God with the love whereby he loves himself (VP36) ... With the third kind of knowledge, knowledge is solely sub specie aeternitatis"; [69]: "accomplished 'in one glance'" |
| C178 | P/P | U/U | medium: U/U | neither [73] nor [72] says intuition is "the mind's highest freedom" or that no method is given |
| C180 | M/S | P/S | keep original | [75]: "Both works derive propositions from definitions and axioms"; corrected [74]: "A3: From a given determinate cause the effect follows neces- sarily" |
| C189 | U/S | M/S | keep original | linked [77] is the Ethics text (modes follow from necessity) but says nothing about the method mirroring it; corrected [76]: "the deductive structure of the Ethics mirrors the causal necessity by which all of nature follows from God" |
| C192 | P/P | M/S | high: M/S | linked [78] SEP psychology has no imagination-genesis passage; corrected [77] Elwes: "the modifications of the human body, of which the ideas represent external bodies as present to us, we will call the images of things" |
| C193 | U/S | M/S | keep original | linked [78] does not quote IIp17; corrected [77] Elwes: "PROP. XVII. If the human body is affected in a manner which involves the nature of any external body, the human mind will regard the said external body as actually existing" |
| C195 | U/S | M/S | keep original | linked [78] silent on IIp25; corrected [77]: "PROP. XXV. The idea of each modification of the human body does not involve an adequate knowledge of the external body" |
| C198 | U/S | M/S | keep original | linked [78] silent on IIp41; corrected [77]: "this kind of knowledge is the only source of falsity (II. xxxv.)" |
| C200 | P/P | U/S | high: M/S | linked [78] silent on IIp18; corrected [77]: "PROP. XVIII. If the human body has once been affected by two or more bodies at the same time, when the mind afterwards imagines any of them, it will straightway" [remember the others] |
| C204 | S/P | P/P | keep original | [79]: "'In nature there is nothing contingent, but all things have been determined from the necessity of the divine nature'"; "finite modes express God's infinite power finitely" not stated as such |
| C205 | S/P | P/P | keep original | [79]: "the striving to persevere in being and consequently to increase the power of acting"; corrected [78] quotes IIIp9 |
| C206 | P/S | S/S | keep original | [79]: "When the conatus is conceived as related to both mind and body, Spinoza calls it appetite, and when humans are conscious of their appetite, he calls it desire (IIIP9S)"; [78]: "desire can be defined as appetite together with consciousness of the appetite" |
| C208 | P/P | S/S | keep original | [79]: things "that increase their power of acting and thinking (IIIP12), causing joy, while ... decrease ... causing sadness"; [78]: "joy is an increase in that power ... sadness is a decrease" |
| C215 | P/P | P/U | keep original | [83]: "man through his body and through his mind strives to persevere in his being and his mind is conscious of this striving"; corrected [82] (review of Kisner) not on desire |
| C221 | M/P | U/P | keep original | linked [89] (EMT TTP) and [90] (TTP ch. 14) are not about the affects; corrected [88]: "When we form 'adequate ideas' about reality, we become less passive and more active" |
| C225 | U/S | U/P | keep original | linked [92] IEP political philosophy is about regimes; corrected [82]: "autonomy -- which consists in forming adequate ideas" |
| C230 | M/S | U/P | keep original | linked [96] JSTOR Daily is biographical; corrected [86]: beatitude is "that satisfaction of mind that stems from the intuitive knowledge of God" |
| C232 | P/P | U/P | keep original | linked [71] (Ethics 2 P32-40) has no eternity-of-mind passage; corrected [70]: "our mind knows itself and the body under a species of eternity" (VP30); "persist immortally" overstated |
| C236 | M/S | X/S | keep original | linked [99] Cambridge Lexicon page has no entry text (access page); corrected [89] TTP: "the prophet’s own certainty was only moral certainty" (two-column PDF text) |
| C244 | M/S | X/S | keep original | linked [99] access page only; corrected [89] TTP ch. 7: "history’ analogy is always dominant" (two-column PDF text; the phrase is split by the other column) |
| C248 | M/S | X/P | keep original | linked [99] access page only; corrected [89] TTP: "So faith in historical narratives is far from being" (two-column PDF text) |
| C249 | M/P | X/P | keep original | linked [99] access page only; corrected [89] TTP ch. 20 on freedom and "the peace and piety of the State" |
| C255 | P/S | P/P | keep original | [13]: "Spinoza refers to Deus sive Natura (God, or Nature)"; "The intellectual love of God, which arises from intuitive knowledge"; the contrast with theology is not stated there |
| C259 | M/P | U/P | keep original | linked [101] is a Hackett catalog page for the PCP; corrected [91] TTP 16: "all men ... are equally bound by the Divine command to love their neighbour as themselves" |
| C268 | U/P | P/P | low: P/P | [46]: "more likely than monarchy or aristocracy to preserve libertas philosophandi"; equality of the natural state not stated |
| C270 | U/P | M/P | keep original | linked [46] has no institutional-design passage; corrected [45]: "the more unchecked a monarch is, the worse off everyone is, including the monarch (TP 6.8)" |
| C271 | P/S | P/P | keep original | [46]: the TTP "declared the best policy in religious matters to be 'allowing every man to think what he likes, and say what he thinks.'"; "rare and a private virtue" not stated |
| C272 | U/S | P/P | keep original | [46]: "to bring men as far as possible under the control of reason, so that they may live in peace and harmony"; councils/checks are in [45], not [46] |
| C276 | M/P | X/S | keep original | linked [99] access page only; corrected [89] TTP preface: "of opinion and worship is not harmful to the piety and peace" (two-column PDF text, interleaved) (the article's quoted wording is not in [89]) |
| C279 | M/S | X/P | keep original | linked [99] access page only; corrected [89] TTP has the chapter on whether "Are miracles events that conflict with the order of" (two-column PDF text) |
| C282 | M/P | X/P | keep original | linked [99] access page only; corrected [89] TTP 20 on freedom "provided he ... doesn't think it entitles him to launch a new law" |
| C293 | S/S | P/P | keep original | [60]: "characterized by infinite attributes ... Finite things are but modifications of that substance"; "humans perceive only thought and extension" not shown |
| C294 | S/S | P/P | keep original | [71] (Ethics 2 P38-40) on adequate ideas and kinds of knowledge; "the mind is the idea of the body" not in this excerpt |
| C296 | U/S | P/P | medium: P/P | [60] quotes the Part IV preface: "his power of acting ... is increased or diminished"; [59] lists "Of Human Bondage, or the Power of the Affects" |
| C298 | P/P | U/P | medium: U/P | linked [60] SEP physical theory is about inertia and conatus of bodies; corrected [59]: "no free will ... everything that happens could not have happened differently" |
| C299 | P/P | U/U | high: U/U | linked [106] New Humanist (Nadler) argues Spinoza is an atheist; no bans/Leibniz; corrected [96] JSTOR Daily same gap |
| C301 | U/S | P/P | medium: P/P | [46]: "All of his work, including the 'Ethics,' was left in manuscript form for his friends to print after his death. He died ... in 1677"; TP dates not given |
| C302 | U/S | P/P | low: P/P | [46] on the TTP's freedom defence; corrected [45]: TTP goals "to defend the freedom to philosophize (Epistle 30)" |
| C303 | U/P | U/U | keep original | [46] and [102] do not discuss the TP's audience or method; corrected [45] window is bibliography |
| C305 | U/S | M/S | keep original | linked [46]/[102] silent on natural right; corrected [92]: "their rights are only limited by their ability" |
| C309 | M/P | M/S | keep original | linked [46] silent on monarchy; corrected [45]: "One of the central constitutional checks is that the King be responsive to a large" [council] |
| C316 | M/S | X/P | keep original | linked [107] not cached, [108] (free-will paper) does not list the early works; corrected [97] Hackett TOC lists "Treatise on the Emendation of the Intellect Short Treatise ... Principles of Cartesian Philosophy and Metaphysical Thoughts" (no dates) |
| C319 | M/S | M/P | keep original | linked [109]/[110] are on conatus and freedom; corrected [100] is the TIE text itself ("If there yet remains some sceptic, who doubts of our primary truth") |
| C322 | M/S | U/X | keep original | linked [108] free-will paper silent on the Short Treatise; corrected [98] Cambridge Lexicon access page |
| C329 | P/P | U/U | medium: U/U | [50] letters do not characterize a guarded style; [49] EMLO metadata page silent |
| C335 | P/P | M/P | keep original | linked [113] (Leibniz/PSR paper) does not frame a pantheism-vs-atheism debate; corrected [103] "Spinoza's Model of God: Pantheism or Panentheism?" |
| C339 | M/S | M/P | keep original | linked [115] (Lamy refutation) silent; corrected [105]: "Friedrich Heinrich Jacobi ... proclaimed explicitly that Spinozism equals fatalism and atheism"; Lessing and Goethe not shown |
| C340 | P/P | U/P | medium: U/P | linked [112] JSTOR challenge page, [113] PSR paper silent; corrected [103] argues a panentheistic "theistic (and ethical) system" |
| C342 | X/X | U/X | keep original | linked [117] 3:16 interview not on divine personality; corrected [107] not cached |
| C348 | M/S | U/P | keep original | linked [118] Stack Exchange page silent; corrected [108]: "men are conscious of their appetite and ignorant of the causes by which they are determined" (from E1 Appendix, not IIp48-49) |
| C352 | U/S | U/P | keep original | linked [120] IAS article silent on virtue/good; corrected [110] on conatus, virtue, power |
| C353 | P/P | U/P | medium: U/P | linked [121] (Diderot paper) not on responsibility as heuristic; corrected [111]: Oldenburg's worry that necessity renders "[moral] rewards and punishments . . . ineffectual" |
| C354 | P/P | S/S | keep original | [13]: "The intellectual love of God, which arises from intuitive knowledge, is eternal"; blessedness "describes as union with, or love for, God" |
| C356 | M/P | U/P | keep original | linked [123] (reading list) silent; corrected [113] on Leibniz, Spinoza and the PSR; "moral necessity" not shown |
| C358 | U/P | U/U | keep original | neither [125] nor corrected [115] (Lamy) mentions Gerdil |
| C360 | X/P | X/U | keep original | linked [127] not cached; corrected [117] interview is on Hume's own theory of causation, not a critique of Spinoza |
| C370 | P/S | S/S | keep original | [3] NEH: "It was the harshest writ of herem ... ever pronounced upon a member of the Portuguese-Jewish community in Amsterdam"; date 1656 in [3]; [136] says "at the age of 24"; corrected [126]: "July 27, 1656, when the Talmud Torah congregation of Amsterdam issued a writ of cherem" |
| C371 | S/S | P/P | keep original | [3] gives the writ: "the abominable heresies which he practiced and taught and about his monstrous deeds"; [19] on Torah authorship; the "likely encompassing" list is inference; corrected [18]: "or within four ells of him" |
| C379 | M/S | U/P | keep original | linked [141] (envy paper) silent; corrected [131]: "Christian Spinozists would have to see Christ as a Socrates like figure rather than divine" |
| C384 | U/U | U/P | keep original | linked [146] political-theory paper has no Einstein; corrected [136]: Einstein "was influenced by and agreed with many of Spinoza's ideas"; conatus/quantum claims not shown |
| C389 | U/P | P/P | keep original | [46]: "Democratic ideas that were punishable by imprisonment in the sixteen-sixties became the watchwords of the American and French Revolutions"; corrected [45]: "institutional structures and procedures channel the natural passions" |
| C391 | M/P | X/P | keep original | linked [152] Project Syndicate login wall; corrected [142]: "Spinoza's naturalism and determinism mak[e]..." (review of a democratic-theory reading) |
| C394 | P/P | P/S | keep original | [13]: "Clearly this is far from the personal creator outside and apart from his creation"; corrected [12]: "it is a mistake to call him a pantheist in so far as pantheism is still a kind of religious theism" |
| C399 | X/P | U/P | keep original | linked markers [158] and [159] point past the end of the 153-item list (dangling); corrected [148]: "On February 21, 2027, Jews around the world will observe ... the 350th yahrzeit"; the trustees "commissioned four leading scholars" |
