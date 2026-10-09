import sys
slug=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 0
t=open(f'/workspace/gta_repo/topics/circumcision/articles/{slug}/snapshots/2026-10-01.txt').read()
t=t.split('='*78,1)[1]
paras=[p for p in t.split('\n') if p.strip()]
chunks=[];cur=''
for p in paras:
    if len(cur)+len(p)>18500 and cur: chunks.append(cur);cur=''
    cur+=p+'\n'
chunks.append(cur)
print(f'[{slug} chunk {n+1}/{len(chunks)}]');print(chunks[n])
