import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];out=[]
for p in z.namelist():
 if p.startswith('World/Dialogs/') and p.endswith('.jbp'):
  v=json.loads(z.read(p));t=v['Data'].get('Text',{});s=l.get(t.get('m_Key',''),'')
  if not s and t.get('Shared'):s=l.get(t['Shared'].get('stringkey',''),'')
  if s and any(k in s.lower() for k in ['clutch','melazmera','devarra','nidalynn']) or p.startswith('World/Dialogs/') and '/DragonHunt/' in p:
   if s:out.append({'path':p,'guid':v['AssetId'],'text':s});print(p,v['AssetId'],s[:1300])
pathlib.Path('reference/canon-review/dragon-family-dialogue.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
