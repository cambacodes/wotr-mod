import zipfile,json,pathlib,re
b=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference');o=b/'canon-review';z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');paths=json.loads((b/'expansion/etudes.json').read_text()); names=['Seelah_AfterQ2','WeddingEndingBad','WeddingEndingGood','SeelahQ2','SeelahQ3','VictimsRevived','HideoutCleared','HedeoutCleared','FinalResolve','ElanDesperate','Elan_Dead','JannaInPrison','JannaInPrison_Drezen','JannaDead_SeelahKnows','JannaDead_SeelahDoesntKnow','JannaInCondemned','JannaFree','Seelah_BestEnding','Seelah_LawfulEnding','Seelah_ModerateEnding','Seelah_BadEnding']; selected={p:g for p,g in paths.items() if p.split('/')[-1][:-4] in names}; reg=re.compile(b'|'.join(g.encode() for g in selected.values()));out={}
for p in z.namelist():
 if p.endswith('.jbp') and p.startswith(('World/Dialogs/','World/Etudes/','World/Encounters/','World/Quests/')):
  raw=z.read(p)
  if reg.search(raw) or ('World/Quests/' in p and 'Seelah' in p):out[p]=json.loads(raw)
(o/'seelah-later-sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(len(out),'sources')
for p,obj in out.items():
 if 'BlueprintQuest' in obj['Data'].get('$type',''):print(p,obj['AssetId'])
