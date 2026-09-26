import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];out=[];reg=re.compile(r'Terendelev|Devarra|Melazmera|Halaseliax',re.I)
for p in z.namelist():
 if p.startswith('World/Dialogs/') and p.endswith('.jbp'):
  v=json.loads(z.read(p));d=v['Data'];t=d.get('Text',{});s=l.get(t.get('m_Key',''),'')
  if not s and t.get('Shared'):s=l.get(t['Shared'].get('stringkey',''),'')
  if s and (reg.search(s) or reg.search(p)):out.append({'path':p,'guid':v['AssetId'],'text':s})
o=pathlib.Path('reference/canon-review');(o/'dragon-candidate-dialogue.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(len(out))
for r in out:
 if re.search(r'family|husband|children|daughter|son\b|mother|eggs|mate\b|claw|scale|remains|soul|dead',r['text'],re.I):print(r['path'],r['guid'],r['text'][:1450])
