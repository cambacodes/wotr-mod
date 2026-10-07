import zipfile,json,pathlib,re
z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip');ids=['581521b398fb9dd4eb52bbfffb3b5c43','056ba61e04cca104a9c95ac2d4658c67','d713e8b772484376a7da810c37ab7922','fee0f0cf006c96f4f90f895ba8d73d97','4ba6fd446353825459f469fe5973fd87','4aa538f07bd542f7a013b90464577d67','7ef78c8e02070af428efe1dd851ec8a1','6b98ec3e704599149b99fe70b5f793ab'];reg=re.compile(b'|'.join(g.encode() for g in ids));out={}
for p in z.namelist():
 if p.endswith('.jbp') and p.startswith(('World/','Items/')):
  raw=z.read(p)
  if reg.search(raw):out[p]=json.loads(raw)
pathlib.Path('reference/canon-review/dragon-state-consumers.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for p,v in out.items():
 if v['AssetId'] in ids or 'Melazmera' in p or 'Devarra' in p:print(p,v['AssetId'])
