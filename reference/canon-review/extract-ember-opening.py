import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip'); l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings']; rows=[]; states=[]
for p in z.namelist():
 if not p.endswith('.jbp'):continue
 if '/Etudes/' in p and 'Ember' in p:
  v=json.loads(z.read(p));states.append({'path':p,**v})
 if '/Dialogs/' in p and 'Ember' in p:
  v=json.loads(z.read(p));d=v['Data'];t=d.get('Text',{});s=l.get(t.get('m_Key',''),'') or l.get(t.get('Shared',{}).get('stringkey',''),'')
  if s:rows.append({'path':p,'guid':v['AssetId'],'text':s})
o=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review');(o/'ember-opening-native.json').write_text(json.dumps({'states':states,'dialogue':rows},ensure_ascii=False,indent=2),encoding='utf-8')
for r in states:
 if r['AssetId'] in ['3a708ad53771a2d44ac506361fb7aafc','fcbd1ad00e1c7044b8485d7feda8b9b7','787273d702a87884e9f14cfb7ef91180']:print(json.dumps(r,indent=2))
for r in rows:
 if re.search(r'Soot|pray|gods|shoes|barefoot',r['text'],re.I):print(r['path'],r['guid'],r['text'][:1600])
