import json,pathlib,zipfile
base=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference'); z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip'); rows=json.loads((base/'expansion/blueprints.json').read_text(encoding='utf-8')); byid={r['guid']:(p,r) for p,r in rows.items()}
want=['Diplomacy_Officer_dialogue','JerribethGreetings_ISanctum_dialog','Jerribeth_Velexia_dialogue','Velexia_MainDialogue','VendorArsinoe_dialogue','BlindCarver_Wintersun_dialog','PeacefulWoodCarver_Wintersun_dialog','Chivarro_dialogue.jbp','KyanaWelcome_SeelahQ2_dialog','ElanKianaAftermath_SeelahQ3_diaog','KianaAloneAftermath_SeelahQ3_dialog']
result={}
for path,r in rows.items():
 if r['type']!='BlueprintDialog' or not any(w in path for w in want):continue
 todo=list(r['data']['FirstCue']['Cues']); seen=set(); cues=[]; lists=[]
 while todo:
  guid=todo.pop(0).replace('!bp_','')
  if guid in seen or guid not in byid:continue
  seen.add(guid); p,x=byid[guid];d=x['data'];cues.append(dict(path=p,guid=guid,type=x['type'],data=d,text=x['text']))
  for a in d.get('Answers',[]):
   ag=a.replace('!bp_','')
   if ag in byid:
    ap,ar=byid[ag]; lists.append(dict(path=ap,guid=ag,data=ar['data'],incoming=p))
  cont=d.get('Continue',{}); todo+=cont.get('Cues',[]) if isinstance(cont,dict) else []
  cs=d.get('Cues',[]);todo+=cs if isinstance(cs,list) else []
 result[path]=dict(guid=r['guid'],data=r['data'],initial_cues=cues,initial_answer_lists=lists)
 print(path.split('/')[-1],r['guid']);print(' root lists:',[(l['path'].split('/')[-1],l['guid']) for l in lists]);print(' starts:',[(c['path'].split('/')[-1],c['text'][:80]) for c in cues])
(base/'canon-review/dialogue-entry-map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
