import json,sys,os
A='/workspace/gta_repo/topics/circumcision/articles'
cat={e['id']:e['name'] for e in json.load(open('/workspace/fallacy_catalog_r3/fallacies.json'))['entries']}
data=json.load(sys.stdin)
slug=data['slug']; txt=open(f'{A}/{slug}/snapshots/2026-10-01.txt').read()
ok=0
for f in data.get('flags',[]):
    q=f['quote']
    if f['entry_id'] not in cat: print('BAD ID',f['entry_id']); continue
    if q not in txt: print('NO MATCH:',q[:80]); open('failures.jsonl','a').write(json.dumps(dict(slug=slug,**f))+'\n'); continue
    if txt.count(q)>1: print('note: quote occurs',txt.count(q),'times')
    row=dict(slug=slug,quote=q,entry_id=f['entry_id'],entry_name=cat[f['entry_id']],reason=f['reason'],favors=f['favors'],confidence=f['confidence'],verdict=f['verdict'])
    assert row['favors'] in('pro','anti','neutral') and row['confidence'] in('high','medium','low') and row['verdict'] in('flag','possible issue')
    open('flags.jsonl','a').write(json.dumps(row)+'\n'); ok+=1
open('done.txt','a').write(slug+'\n')
print(slug,'saved',ok)
