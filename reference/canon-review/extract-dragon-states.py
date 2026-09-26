import zipfile,json,pathlib
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');out={}
for p in z.namelist():
 if p.endswith('.jbp') and ((any(s in p for s in ['Terendelev','Devarra','Melazmera','Nidalynn','Tyvanadis']) and p.startswith(('World/Etudes/','World/Quests/','Items/','Units/NPC/','Units/Monsters/'))) or p.endswith('/Chaleb/Cue_0006.jbp') or p.endswith('/Chaleb/Cue_27.jbp')):
  v=json.loads(z.read(p));out[p]=v
  if p.startswith(('Units/NPC/','Units/Monsters/')) and 'Brain' not in p and 'Prebuff' not in p:print(p,v['AssetId'],[(k,a) for k,a in v['Data'].items() if any(s in k.lower() for s in ['gender','size','name','race'])])
  elif p.startswith(('World/Etudes/','Items/')):print(p,v['AssetId'])
pathlib.Path('reference/canon-review/dragon-state-sources.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
