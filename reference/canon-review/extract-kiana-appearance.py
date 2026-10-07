import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');loc=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];out=[]
for p in z.namelist():
 if not p.endswith('.jbp') or not (p.startswith('Units/') or p.startswith('Portraits/') or ('Seelah' in p and '/Dialogs/' in p)):continue
 raw=z.read(p)
 if p.startswith('Units/') or p.startswith('Portraits/'):
  if not any(s in raw for s in [b'180b0eaa5dce387458d2ebf0ee943985',b'cc92e7a3b8944f7da3bcceec9f7ce0ec',b'd0532fe50faad104daa3d975fa70edc7']) and not re.search('Kyana|Kiana',p,re.I):continue
  v=json.loads(raw); out.append({'path':p,**v})
 else:
  v=json.loads(raw);d=v['Data'];t=d.get('Text',{});s=loc.get(t.get('m_Key',''),'') or loc.get((t.get('Shared') or {}).get('stringkey',''),'')
  if s and (re.search('Kyana|Kiana',p,re.I) or re.search(r'crystal|skin|hair|blue|bride|statue|petrif|appearance',s,re.I)):
   row={'path':p,'guid':v['AssetId'],'text':s};out.append(row)
pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/kiana-appearance-sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
