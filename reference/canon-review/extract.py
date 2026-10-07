import json,zipfile,pathlib
root=pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure')
out=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review')
z=zipfile.ZipFile(root/'blueprints.zip')
loc=json.loads((root/'Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings']
terms=['konomi','jerribeth','kiana','velexia','vellexia','gesmerha','chivarro','arsinoe','seelah','minagho','wenduag']
rows=[]
for name in z.namelist():
 if not name.startswith('World/Dialogs/') or not name.endswith('.jbp'): continue
 if not any(t in name.lower() for t in terms): continue
 obj=json.loads(z.read(name)); d=obj['Data']; key=d.get('Text',{}).get('m_Key'); text=loc.get(key,'')
 if text: rows.append({'path':name,'guid':obj['AssetId'],'text':text,'speaker':d.get('Speaker'), 'conditions':d.get('Conditions'), 'onstop':d.get('OnStop')})
(out/'dialogues.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for term in terms:
 rs=[r for r in rows if term in r['path'].lower()]
 (out/(term+'.txt')).write_text('\n\n'.join(r['path']+' | '+r['guid']+'\n'+r['text'] for r in rs),encoding='utf-8')
 print(term,len(rs))
(out/'localized-mentions.txt').write_text('\n\n'.join(k+'\n'+v for k,v in loc.items() if isinstance(v,str) and any(t in v.lower() for t in ['kiana','gesmerha','konomi','arsinoe'])),encoding='utf-8')
