import zipfile,json,pathlib
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');ids={}
for p in z.namelist():
 if p.endswith('.jbp') and any(s in p for s in ['/Melazmera.jbp','/NidalynnDragon.jbp','/Devarra_dead.jbp']):
  v=json.loads(z.read(p));print(p,v['AssetId']);ids[v['AssetId']]=p
l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];out=[]
for p in z.namelist():
 if p.startswith('World/Dialogs/') and p.endswith('.jbp'):
  raw=z.read(p)
  if any(i.encode() in raw for i in ids):
   v=json.loads(raw);d=v['Data'];t=d.get('Text',{});s=l.get(t.get('m_Key',''),'')
   if not s and t.get('Shared'):s=l.get(t['Shared'].get('stringkey',''),'')
   if s:out.append({'path':p,'guid':v['AssetId'],'text':s});print(p,v['AssetId'],s[:1400])
pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/dragon-speaker-dialogue.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
