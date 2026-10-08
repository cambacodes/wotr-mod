import json,pathlib,zipfile,re
b=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference');z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');e=json.loads((b/'expansion/etudes.json').read_text());d=json.loads((b/'canon-review/relevant-etudes.json').read_text())
for p,g in e.items():
 if p.endswith(('/BlindCarver_Dead.jbp','/ElanDesperate.jbp','/KTC_WintersunHelp_BlindCarver.jbp')):d[p]=json.loads(z.read(p))
(b/'canon-review/relevant-etudes.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
ids=['49839ba15f34bee469c4f093dace0811','8a2da1bae7d69b84b999155ac0481223','ded376ed8b73c3e42b0de967fb1d10a9'];reg=re.compile(b'|'.join(x.encode() for x in ids));out=json.loads((b/'canon-review/state-consumers.json').read_text(encoding='utf-8'))
for p in z.namelist():
 if p.endswith('.jbp') and p.startswith(('World/Dialogs/','World/Etudes/','World/Encounters/')):
  raw=z.read(p)
  if reg.search(raw):out[p]=json.loads(raw)
(b/'canon-review/state-consumers.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print('state consumers',len(out))
for p,obj in out.items():
 if '8a2da1bae7d69b84b999155ac0481223' in json.dumps(obj):print('soulless consumer',p)
