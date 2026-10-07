import json,pathlib,zipfile
b=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference'); z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip'); roots=json.loads((b/'canon-review/dialogue-entry-map.json').read_text(encoding='utf-8')); ids={r['guid'] for r in roots.values()};matches={}
for p in z.namelist():
 if not p.endswith('.jbp') or not p.startswith(('Units/','World/Etudes/')):continue
 raw=z.read(p)
 if any(g.encode() in raw for g in ids):
  obj=json.loads(raw); matches[p]=obj;print(p,obj['AssetId']);
(b/'canon-review/contact-consumers.json').write_text(json.dumps(matches,indent=2),encoding='utf-8')
