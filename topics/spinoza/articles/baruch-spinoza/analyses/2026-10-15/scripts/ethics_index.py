#!/usr/bin/env python3
"""Index Elwes's Ethics (Gutenberg #3800 text as stored in neuresthetics/grokAlign
junkDrawer/Ethics/'The Ethic.txt') by locator, E1P15 style, with line numbers.
Locators: E{part}D{n} definition, E{part}A{n} axiom, E{part}P{n} proposition,
E{part}P{n}C{k} corollary, E{part}P{n}S{k} note/scholium ('Note' in Elwes),
E{part}P{n}Dem proof, E{part}Pref preface, E{part}App appendix, E3DefAff{n} definitions of the emotions.
Heuristic line scan; an entry's span runs to the line before the next entry.
Usage: ethics_index.py "The Ethic.txt" out.csv"""
import re, sys, csv
R = {"I":1,"V":5,"X":10,"L":50,"C":100}
def rom(s):
    t=0
    for i,c in enumerate(s):
        v=R[c]; t+= -v if i+1<len(s) and R[s[i+1]]>v else v
    return t
lines = open(sys.argv[1], encoding="utf-8", errors="replace").read().split("\n")
part=0; mode=None; prop=None; ent=[]; nc=ns=0
def add(loc, i): ent.append([loc, i+1])
for i,l in enumerate(lines):
    s=l.strip()
    m=re.match(r"^PART (I|II|III|IV|V)\b[.:]", s)
    if m and i>20: part=rom(m.group(1)); mode=None; prop=None; add(f"E{part}", i); continue
    if i==18: part=1; add("E1", i); continue
    if part==0: continue
    if re.match(r"^\*\*\* ?END", s): break
    if re.match(r"^PREFACE", s): add(f"E{part}Pref", i); mode="pref"; continue
    if re.match(r"^APPENDIX", s): add(f"E{part}App", i); mode="app"; continue
    if re.match(r"^DEFINITIONS? OF THE EMOTIONS", s): mode="defaff"; continue
    m=re.match(r"^(DEFINITIONS?|AXIOMS?|POSTULATES?)\.?\s*(?=[IVX]+\.|$)", s)
    if m:
        mode={"D":"def","A":"ax","P":"post"}[m.group(1)[0]]
        s=s[m.end():].strip()
        if not s: continue
    s=re.sub(r"^DEFINITION (?=[IVX]+\.)", "", s)
    m=re.search(r"PROP\. ([IVXLC]+)\.", s)
    if m:
        prop=rom(m.group(1)); mode="prop"; nc=ns=0; add(f"E{part}P{prop}", i); continue
    m=re.match(r"^([IVXLC]+)\. (?=[A-Z\"\u201c])", s)
    if m and mode in ("def","ax","post","defaff"):
        tag={"def":"D","ax":"A","post":"Post","defaff":"DefAff"}[mode]
        add(f"E{part}{tag}{rom(m.group(1))}", i)
        for mm in re.finditer(r"\.([IVXL]+)\. [A-Z]", s):  # run-together items on one line
            add(f"E{part}{tag}{rom(mm.group(1))}", i)
        continue
    if prop and mode=="prop":
        if re.match(r"^Proof\.?", s): add(f"E{part}P{prop}Dem", i); continue
        m=re.match(r"^Coroll(?:ary|\.)\s*([IV]+)?\.?", s)
        if m: nc+=1; add(f"E{part}P{prop}C{rom(m.group(1)) if m.group(1) else nc}", i); continue
        m=re.match(r"^Note\s*([IV]+)?\.?", s)
        if m: ns+=1; add(f"E{part}P{prop}S{rom(m.group(1)) if m.group(1) else ns}", i); continue
w=csv.writer(open(sys.argv[2],"w",newline="",encoding="utf-8")); w.writerow(["locator","line_start","line_end","first_line"])
for k,(loc,ln) in enumerate(ent):
    end = ent[k+1][1]-1 if k+1<len(ent) else len(lines)
    w.writerow([loc, ln, end, lines[ln-1].strip()[:160]])
print(len(ent), "entries")
