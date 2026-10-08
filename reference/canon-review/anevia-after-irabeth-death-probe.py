"""Read installed native records mentioning the capital actor or death/absence states."""
import hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
TARGETS=['86b332a9-5910-4d46-9951-8e06f7dcf0cf','b14e13f9359585e498fcd81ab95d4d7e','6125c10886d6465091f4e092618ca55a','09f46662bcd14a03a0874267e16d6e6f']
archive=Path('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip')
records={}
with zipfile.ZipFile(archive) as z:
 for name in z.namelist():
  if not name.endswith('.jbp'): continue
  raw=z.read(name)
  matches=[t for t in TARGETS if t.encode() in raw]
  if matches or '/DrezenMain_C5/Coronation/' in name or any(i.encode() in raw[:120] for i in ['30862a76dd4a11049be42d3de26159fb','a30fa65c287ebb8418736a544797b7f4','ef35e9838eea48f48b22ae3aef9ca6cd']):
   records[name]={'sha256':hashlib.sha256(raw).hexdigest().upper(),'matches':matches,'record':json.loads(raw)}
locpath=archive.parent/'Wrath_Data/StreamingAssets/Localization/enGB.json'
strings=json.loads(locpath.read_text(encoding='utf-8-sig'))['strings']
for value in records.values():
 field=value['record']['Data'].get('Text',{})
 key=(field.get('Shared') or {}).get('stringkey') or field.get('m_Key')
 if key in strings: value['english']=strings[key]
out={'localization_sha256':hashlib.sha256(locpath.read_bytes()).hexdigest().upper(),'archive':str(archive),'targets':TARGETS,'records':records}
(ROOT/'reference/canon-review/anevia-after-irabeth-death-records.json').write_text(json.dumps(out,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
print('Matched',len(records),'records')
