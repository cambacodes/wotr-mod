import json,zipfile,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');reg=re.compile(b'54be53f0b35bf3c4592a97ae335fe765|894a7ba9ecb24f2aad9eefe09a6220d3|c33407f132b192643a438bd33797efa1|1d30b49f8756c2b40bb8271e856675c5');out={}
for p in z.namelist():
 if p.endswith('.jbp') and p.startswith(('World/Etudes/','World/Dialogs/','World/Encounters/','World/Quests/','Units/')):
  raw=z.read(p)
  if reg.search(raw):out[p]=json.loads(raw)
pathlib.Path('reference/canon-review/seelah-recruit-consumers.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for p,v in out.items():
 if any(s in json.dumps(v) for s in ['Unrecruit','RemoveCompanion','FailAll','Lich','Swarm']):print(p,v['AssetId'])
print('objects',len(out))
