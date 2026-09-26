exec(open('C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/extract.py',encoding='utf-8').read().split('rows=[]')[0])
keys={k for k,v in loc.items() if isinstance(v,str) and any(t in v.lower() for t in ['konomi','gesmerha'])}
found=[]
for name in z.namelist():
 if not name.startswith('World/Dialogs/') or not name.endswith('.jbp'): continue
 obj=json.loads(z.read(name));d=obj['Data'];key=d.get('Text',{}).get('m_Key')
 if key in keys: found.append({'path':name,'guid':obj['AssetId'],'text':loc[key]})
(out/'extra-mentions.json').write_text(json.dumps(found,ensure_ascii=False,indent=2),encoding='utf-8')
for r in found: print(r['path']+' | '+r['guid']+'\n'+r['text'][:1100])
