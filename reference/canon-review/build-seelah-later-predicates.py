import json,pathlib,zipfile
b=pathlib.Path('reference'); o=b/'canon-review'; d=json.loads((o/'seelah-later-sources.json').read_text(encoding='utf-8')); x=json.loads((b/'expansion/blueprints.json').read_text(encoding='utf-8')); pool={v['AssetId']:(p,v['Data']) for p,v in d.items()};pool.update({v['guid']:(p,v['data']) for p,v in x.items()})
rows=[
('wedding_disaster_known','6ba1c92c73ec4cc48acaf26473564492','QuestObjective state Started OR Completed','Granted by wedding aftermath; does not assert Kiana lost her soul.'),
('wedding_investigation_concluded','a1024628f074e4d4f9d2b15956975459','Quest state Completed','Final Drezen report concluded; completion of final objective finishes quest.'),
('sunhammer_death_witnessed','beef9b7110dfebc429bf7109cd3be849','CueSeen','Literal death occurs here; postbattle collection is later.'),
('soul_gems_recovered','83527eddea019674cb123a6a52bdf169','QuestObjective state Completed','Cue0051 completes this when Seelah takes jewelry; victims are not yet restored.'),
('souls_returned','5a5a533c9ce630a48b877f9a194840cb','Quest state Completed','Completed, not merely finished or failed; final Curl dialogue completes ReturnSouls.'),
('return_souls_objective','5b1e04caadc42114281d29db76c19c4f','QuestObjective state Completed','FinishParent true; equivalent successful native quest terminal.'),
('kiana_soulless_history','8a2da1bae7d69b84b999155ac0481223','UnlockableFlag unlocked','DisasterNewsDrezen Cue0020 sets this; historical marker does not prove still soulless after rescue.'),
('wedding_bad','d983621f7b887b043acb0c43186bf824','Etude Playing','FinalResolve uses this to spawn Kiana victim; good wedding spawns another victim.'),
('wedding_good','be924a4c2bfff36459cebb87b84b8fb5','Etude Playing','Do not narrate Kiana soul loss in this branch.'),
('revival_aftermath','6d3fb96f9b60c0449a01add4be5c4a49','Etude Playing','Area-linked temporary staging; not persistent restoration predicate.'),
('kiana_married_conversation_done','97b3254015284346ba32f1749cfae0b0','UnlockableFlag unlocked','Native one-shot aftermath happened; does not prove current physical actor presence.'),
('kiana_widow_conversation_done','b5dff99d2f8140e8bf23fb30048db101','UnlockableFlag unlocked','Native widow aftermath happened; does not prove current physical actor presence.'),
('elan_desperate','ded376ed8b73c3e42b0de967fb1d10a9','Etude Playing','Starts before death; aftermath uses this to choose widow branch. Do not label him dead early.'),
('elan_dead','148423f1d35917946a5ebeeb4f19246c','Etude Playing','ImportantNPCs fate; FinalResolve starts it if ElanDesperate plays. Absence alone does not prove alive in arbitrary modified saves.'),
('final_resolve','2b4a5c01a192d1f4aa8c9d32aa149727','Etude Playing','Area-linked stage, starts native Elan death fate and selects Kiana victim by wedding outcome.'),
('jannah_prison','59632e1775b2f7240af0f6d0db28e35b','Etude Playing','Completed by Seelah_BeforeQ3 during transfer to Condemned; Completed does not mean currently imprisoned.'),
('jannah_condemned','46f4524cec981c544964229e3e08c847','Etude Playing','Starts upon transfer from prison in Seelah_BeforeQ3.'),
('jannah_dead_unknown_to_seelah','f8129442feebb7c49b209c83b8ee6267','Etude Playing','Character knowledge differs from player knowledge; Seelah main Cue0105 completes this and starts knows flag.'),
('jannah_dead_known_to_seelah','699b1ad898227c943b2ee9e0cfd355aa','Etude Playing','Use OR with unknown-death for physical death; use only this for Seelah informed dialogue.'),
('jannah_free','d99770b13ebc47447881d33763209b03','Etude Playing','Release does not establish recruitment or attendance.'),
('seelah_lawful_ending','c702a52487248224796ba18d7c6336ae','Etude Playing','Native epilogue establishes knightly order; romance must preserve her career choice.'),
('seelah_best_ending','c959cc3ef25ce834090ba65cd0169588','Etude Playing','Native joyful wandering knight outcome; activation excludes lawful.'),
('seelah_moderate_ending','2bb1f6f30ca9bb1408f720d6f10c5c05','Etude Playing','Native solitary self-doubt, not joyful wanderer; activation excludes lawful.'),
('seelah_bad_ending','e438007efc4f1474eb447031d4b5a60e','Etude Playing','Native sorrowful departure also applies if Q3 not completed; activation excludes lawful.')]
missing={r[1] for r in rows}-pool.keys(); z=zipfile.ZipFile('D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip')
for p in z.namelist():
 if not missing:break
 if p.endswith('.jbp') and ('UnlockableFlags' in p or '/Seelah' in p):
  v=json.loads(z.read(p));g=v['AssetId']
  if g in missing:pool[g]=(p,v['Data']);missing.remove(g)
assert not missing,missing
result={'scope':'Authoritative offline predicates for Seelah later scenes; no runtime or complete route approval.','semantics':'Etude Playing does not include Completed; negated Playing includes never started and completed states. Quest and objective Completed must not include Failed.','predicates':[{'key':k,'guid':g,'type':pool[g][1]['$type'].split(', ')[-1],'source_path':pool[g][0],'predicate':q,'gotcha':n} for k,g,q,n in rows],'kiana_contact':'For normal completed Q3 saves, native married versus widow selection is NOT ElanDesperate Playing versus ElanDesperate Playing. Both dialogue holders also require their respective aftermath flag locked. Neither is a reusable root. For authored recurring contact, require successful Q3 rescue or explicit separate restoration and stage an actual actor/invitation. No global Kiana-alive predicate established.','evidence_file':'seelah-later-sources.json'}
(o/'seelah-later-predicates.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print('Saved',len(rows),'verified predicates')
