import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');o=pathlib.Path('reference/canon-review');l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];reg=re.compile(r'\b(Mielarah|Eliandra|Jannah|Areelu)\b');out=[]
for p in z.namelist():
 if not p.startswith('World/Dialogs/') or not p.endswith('.jbp'):continue
 v=json.loads(z.read(p));t=v['Data'].get('Text',{});s=l.get(t.get('m_Key',''),'')
 if not s and t.get('Shared'):s=l.get(t['Shared'].get('stringkey',''),'')
 if s and reg.search(s):out.append({'path':p,'guid':v['AssetId'],'text':s})
(o/'candidate-extra-mentions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(len(out))
for r in out:
 if 'Mielarah' in r['text']: print(r)
