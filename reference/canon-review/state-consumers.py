import json,pathlib,zipfile,re
b=pathlib.Path('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference');z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');es=json.loads((b/'canon-review/relevant-etudes.json').read_text()); wanted=['JerribethDead','JerribethLovesUsVeryMuch','ChivarroHappyEnd','ChivarroKilled','ChivarroRemovedFormPower','MinaghoDead','MinaghoSetFreeInC4','VellexiaKilled','VellexiaPeacefulResolution','KianaIsPosessed','VictimsRevived','Elan_Dead'];ids={e['AssetId']:p for p,e in es.items() if p.split('/')[-1][:-4] in wanted}; reg=re.compile(b'|'.join(g.encode() for g in ids));found={}
for p in z.namelist():
 if not p.endswith('.jbp') or not p.startswith('World/'):continue
 raw=z.read(p)
 if reg.search(raw):found[p]=json.loads(raw)
(b/'canon-review/state-consumers.json').write_text(json.dumps(found,ensure_ascii=False,indent=2),encoding='utf-8');print(len(found),'references')
for g,p in ids.items():
 checks=[]
 def walk(x,fp):
  if isinstance(x,dict):
   if x.get('m_Etude')=='!bp_'+g and 'EtudeStatus' in x.get('$type',''):checks.append((fp,{k:v for k,v in x.items() if k in ['Not','NotStarted','Started','Playing','CompletionInProgress','Completed']}))
   for v in x.values():walk(v,fp)
  elif isinstance(x,list):
   for v in x:walk(v,fp)
 for fp,obj in found.items():walk(obj,fp)
 print(p.split('/')[-1],checks[:3])
