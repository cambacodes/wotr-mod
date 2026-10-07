import zipfile,json,pathlib,re
base=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review'); ids=set(re.findall(r'"([a-f0-9]{32})"',''.join(p.read_text(encoding='utf-16') for p in base.glob('aranka-*.cs'))));z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');l=json.loads(pathlib.Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Wrath_Data/StreamingAssets/Localization/enGB.json').read_text(encoding='utf-8-sig'))['strings'];out=[]
for p in z.namelist():
 if not p.endswith('.jbp') or p.startswith('QA/'):continue
 if not ('Aranka' in p or 'Alluring' in p or p.startswith('World/Etudes/') or p.startswith('World/Dialogs/') or p.startswith('Units/')):continue
 v=json.loads(z.read(p));d=v['Data'];t=d.get('Text',{});s=l.get(t.get('m_Key',''),'') or l.get((t.get('Shared') or {}).get('stringkey',''),'')
 if v['AssetId'] in ids or re.search(r'Aranka|Alluring',p,re.I) or ('Aranka' in s and re.search(r'killed|dead|singer|woman|Drezen|Reverie',s,re.I)):
  out.append({'path':p,'text':s,**v})
(base/'aranka-native.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(len(out))
for r in out:
 if '/Etudes/' in r['path'] and re.search('Aranka|Azata|Chapter05',r['path'],re.I):print(r['path'],r['AssetId'],json.dumps(r['Data'].get('ActivationCondition',{})))

