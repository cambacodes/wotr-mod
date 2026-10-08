import json,zipfile,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');o=pathlib.Path('reference/canon-review');reg=re.compile(b'cd8666952065ce74d94d960a23482133|cc5e8c94d484b9c48ad32afd6d5c90ef');out={}
for p in z.namelist():
 if not p.endswith('.jbp'):continue
 if not (p.startswith(('World/','Units/'))):continue
 raw=z.read(p)
 if reg.search(raw) or '/JerribetnFinal/' in p or ('Jerribeth' in p and ('Conditions' in p or 'Actions' in p)):
  out[p]=json.loads(raw)
(o/'jerribeth-contact-sources.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(len(out));print('\n'.join(out))
