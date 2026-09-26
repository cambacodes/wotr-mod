import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');names=['Soana','Areelu','Jannah','Janna','Yaniel','Delamere','Elyanka','Herrax','Mielarah','Shamira','Hepzamirah','Iomedae','Eliandra'];out={}
for p in z.namelist():
 if p.endswith('.jbp') and p.startswith('World/Dialogs/') and any(n.lower() in p.lower() for n in names):out[p]=json.loads(z.read(p))
l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];rows=[]
for p,v in out.items():
 t=v['Data'].get('Text',{});s=l.get(t.get('m_Key',''),'')
 if not s and t.get('Shared'):s=l.get(t['Shared'].get('stringkey',''),'')
 if s:rows.append({'path':p,'guid':v['AssetId'],'text':s})
o=pathlib.Path('reference/canon-review');(o/'candidate-inventory-dialogue.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8');print(len(rows));print('\n'.join(sorted(set(r['path'].rsplit('/',1)[0] for r in rows))))
