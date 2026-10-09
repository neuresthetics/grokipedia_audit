#!/usr/bin/env python3
"""Stage 1 of the argument inventory: a fixed, written rule set (no model).

For each prose sentence (citation markers like [12] removed first) the script looks for
side cues: regular expressions for a claim that helps the case FOR the practice (pro:
a benefit, harmlessness, playing down harm, a rights/freedom claim for doing it, or
dismissing its critics) or AGAINST it (anti: a harm, a rights/ethics objection, a call to
end it, or an explicit critic's stance). The lists differ a little between the male
circumcision group and the FGM group, because the same words mean different things there
(e.g. "mutilation" is part of the name "female genital mutilation" and is not a cue in FGM
articles; names of laws and organisations are removed before matching).

Outcome per sentence (script_side):
  pro    only pro cues hit
  anti   only anti cues hit
  mixed  both sides hit, or a cue sits right after a negation word (so the direction
         may be flipped). Rule labels are kept for comparison only; scoring uses the model labels.
  none   no cue: treated as descriptive / neutral, not an argument sentence

The cue lists were written before any labeling and were not tuned to the flags.
"""
import re

MARK = re.compile(r"\s*\[\d+\]")
NEG = re.compile(r"\b(?:no|not|without|lack(?:s|ed|ing)?|little|neither|nor|never|unproven|questionable|"
                 r"insufficient|absence|unclear|disputed?|contested|minimal|negligible|rarely|rare|low|limited|"
                 r"overstat\w*|exaggerat\w*|deny|denies|denied|challeng\w*|refut\w*|dismiss\w*)\b(?:\W+\w+){0,3}\W+$",
                 re.I)

# Phrases removed before matching (names, not stances).
NAMES = re.compile(r"female genital mutilation(?:/cutting)?|genital mutilation|\bFGM(?:/C)?\b|female genital cutting|"
                   r"female circumcision|prohibition of female circumcision act|"
                   r"international day of zero tolerance|zero tolerance for|act \d{4}|\bact\b", re.I)

PRACTICE = r"(?:circumcis\w*|cutting|cut|procedure\w*|operation\w*|fgm|infibulat\w*|clitoridectom\w*|excision\w*|milah|khitan|foreskin\w*|prepuce|surgery|surgeries|ritual\w*|practice\w*)"
COMMON_PRO = [
    r"\bbenefi(?:t|ts|cial)\b", r"\bprotective\b", r"\bprotect(?:s|ed|ion)? against\b", r"\boutweigh\w*",
    r"\breduc\w* (?:the )?(?:\w+ ){0,2}(?:risk|incidence|rates?|transmission|acquisition|likelihood)\b",
    r"\b(?:lower|reduced|decreased) (?:\w+ ){0,2}(?:risk|rates?|incidence|prevalence|transmission)\b",
    r"\bprevent(?:s|ed|ing|ion|ive)? (?:of )?(?:\w+ ){0,3}(?:hiv|infections?|transmission|cancer|diseases?|utis?|stis?|phimosis|balanitis)\b",
    r"\bhygien\w*", r"\bcleanl\w*", r"\bcost[- ]effective\w*",
    r"\beffective(?:ness)? (?:\w+ ){0,3}(?:against|in prevent\w*|in reduc\w*|for prevent\w*|hiv)\b",
    r"\befficacy (?:\w+ ){0,3}(?:against|in prevent\w*|in reduc\w*|of (?:male )?circumcision)\b",
    r"\b(?:is|are|was|remains|considered|proven|deemed|relatively|generally) safe\b", r"\bsafe and effective\b",
    r"\bsafety profile\b", r"\b(?:religious|parental) (?:freedom|liberty|rights?)\b", r"\bfreedom of religion\b",
    r"\b(?:recommend\w*|endors\w*) (?:\w+ ){0,4}" + PRACTICE, r"\bexaggerat\w*", r"\boverstat\w*",
    r"\bsensationali\w*", r"\b(?:ethnocentr|imperialis|colonialis|relativis)\w*",
]
COMMON_ANTI = [
    r"\bharm(?:s|ed|ful|fully)?\b", r"\bcomplications?\b", r"\badverse (?:event|effect|outcome)s?\b",
    r"\binjur(?:y|ies|ed|ious)\b", r"\bbotched\b", r"\bfatal\w*", r"\bha?emorrhag\w*",
    r"\b(?:deaths?|died) (?:\w+ ){0,8}" + PRACTICE, PRACTICE + r" (?:\w+ ){0,8}(?:deaths?|died)\b",
    r"\btraumati[cz]\w*", r"\bpsychological (?:trauma|harm|distress|damage)\b", r"\bpainful\b", r"\bsuffer\w*",
    r"\b(?:sexual|erectile) dysfunction\w*", r"\birreversib\w*", r"\bviolat\w* (?:\w+ ){0,3}(?:rights?|integrity|autonomy)\b",
    r"\bbodily integrity\b", r"\b(?:without|cannot|unable to|lack of|absence of|incapable of) (?:\w+ ){0,3}consent\w*",
    r"\bautonomy\b", r"\bhuman rights?\b", r"\b(?:child(?:'s|ren's)?|girls'?|women's) rights?\b", r"\babuse\b",
    r"\btortur\w*", r"\bcruel\w*", r"\bbarbar\w*", r"\b(?:medically )?unnecessar\w*", r"\bnon-?therapeutic\b",
    r"\bunjustif\w*", r"\bcritic(?:s|ism|isms|ise|ize|ized|ised)?\b", r"\bopponents?\b", r"\bintactiv\w*",
    r"\bcondemn\w*", r"\bdenounc\w*", r"\bunethical\b", r"\bethical (?:concern|objection|issue|problem|question)s?\b",
    r"\bmorally (?:wrong|problematic|impermissible|unacceptable)\b",
]
MALE_PRO = [r"\b(?:no|not) (?:\w+ ){0,2}(?:affect|impair|diminish|reduce)\w* (?:\w+ ){0,2}(?:sexual|sensitiv|pleasure|satisfaction)"]
MALE_ANTI = [r"\bmutilat\w*", r"\b(?:loss|reduc\w*|decreas\w*|diminish\w*) (?:of |in )?(?:\w+ )?sensitiv\w*",
             r"\bsensitiv\w* (?:\w+ )?(?:loss|reduc\w*|decreas\w*)"]
FGM_PRO = [r"\bpurity\b", r"\bchastity\b", r"\bmodesty\b", r"\bmarriageab\w*", r"\bmarital eligibility\b",
           r"\bbeaut\w*", r"\baesthetic\w*", r"\bsymbolic\b", r"\bmild(?:er)?\b", r"\bless (?:severe|invasive|harmful)\b",
           r"\bdouble standard\b", r"\bcomparable to male circumcision\b", r"\bsunn?a\b", r"\bmakrumah?\b",
           r"\bobligatory\b", r"\bmedicali[sz]\w*", r"\bharm reduction\b", r"\bwestern (?:bias|feminis\w*|critics?)\b",
           r"\bwithout (?:\w+ ){0,2}(?:detriment|harm|adverse)\w*", r"\bpredominant narratives?\b"]
FGM_ANTI = [r"\bfistula\w*", r"\binfections?\b", r"\bdiscriminat\w*", r"\bpatriarch\w*", r"\boppress\w*",
            r"\bcoerc\w*", r"\bcontrol (?:of |over )?(?:women|girls|female)\w*", r"\beradicat\w*",
            r"\babandon\w*", r"\bend (?:the practice|fgm|it)\b", r"\bptsd\b", r"\bdepression\b", r"\banxiety\b"]

def _c(lst):
    return [re.compile(p, re.I) for p in lst]

RULES = {
    "male": (_c(COMMON_PRO + MALE_PRO), _c(COMMON_ANTI + MALE_ANTI)),
    "FGM": (_c(COMMON_PRO + FGM_PRO), _c(COMMON_ANTI + FGM_ANTI)),
}


def clean(s):
    return MARK.sub("", s)


def script_side(sentence, grp):
    """Return (side, pro_cues, anti_cues, negated)."""
    s = NAMES.sub(" ", clean(sentence))
    pro_re, anti_re = RULES[grp]
    hits = {"pro": [], "anti": []}
    neg = False
    for side, rs in (("pro", pro_re), ("anti", anti_re)):
        for r in rs:
            for m in r.finditer(s):
                hits[side].append(m.group(0).lower())
                if NEG.search(s[:m.start()]):
                    neg = True
    p, a = bool(hits["pro"]), bool(hits["anti"])
    if not p and not a:
        side = "none"
    elif neg or (p and a):
        side = "mixed"
    else:
        side = "pro" if p else "anti"
    return side, hits["pro"], hits["anti"], neg
