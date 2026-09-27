# Scene CG coverage and full manuscript backlog

Date: 2026-09-27.
Status: inventory complete for the present export and exposed source scene objects; actual text assessment is in progress.
The user has authorized a full art production run for all 43 characters, including route-matched intimacy, materially distinct endings and established group milestones.
Writing remains frozen.
This task owns only the coverage ledger; generation, staging and assignment are handled separately.

## Exact coverage boundary

The current development export contains 753 registered scenes and 4,955 nodes.
Reading scene dictionaries from all 84 storyline modules adds 222 draft-only IDs, for 975 IDs and 7,199 primary nodes.
Thirty-seven source/export node variants are retained separately in the JSON ledger because equal IDs do not guarantee identical content.
These counts include alternate histories and epilogues, not 975 distinct dates or 7,199 required images.
Current assessment has actually read 1,997 nodes across all 30 source families, including every node of 292 complete scenes.
The other 5,202 nodes and the 37 source-node variants remain explicitly unassessed.
The exported Minagho/Chivarro continuation now has all 47 scenes and 218 nodes read for CG decisions, including seven exact-text epilogue duplicates.
This does not cover their separate native parent routes or approve existing artwork.

The paired [JSON ledger](scene-cg-coverage.json) stores exact node text hashes, read-page evidence, choice effects and selected state contracts, source paths/hashes, export hash, assigned/effective portrait key, staged file availability and assessment status.
It is an audit artifact, not an export or source manuscript; its read-page evidence must not be edited as a substitute for route sources.
Imports used Python -B and did not run module self-checks or write production files.
Helper-only modules aranka_path_acquisition.py, konomi_contact.py and tirabade_chronology.py expose no standalone scene dictionary; their integration effects are represented by the actual export where present.

## Decision rules

A CG is needed when a specific meaningful action, emotional turn, magical transformation, quest consequence or selected intimacy stage benefits from a distinct image.
A letter does not place its author in the room; memories and proposed journeys do not establish current physical events.
Generic speaker portraits can support dialogue without pretending to depict every object or gesture.
Reuse a setting only while wardrobe, physical form, participant presence and selected branch remain compatible.
Branch copies may share art only after actual text/state comparison; shared titles and word counts are insufficient.
Automatic per-page portrait switching is available; this audit does not request a selector.
Preserve attractive adult racial identity and native revealing design, plus scene-driven clothes, expression/action variety and plausible tailoring/material physics.
Ember and Aivu remain deferred, age-appropriate friendship only.
No universal need for one new image per node or scene is implied.

## Immediate actionable findings from actual text

| Exact page | Required visual decision |
| --- | --- |
| `minachiv.two_answers/start` | Starts with note, then physical windowless room and human-to-lilitu disguise drop. Not letter-only. Later pages show native Minagho alone; Chivarro is not yet there. |
| `noct.unlit_quay/start` | Dream quay has no sea, rain several yards away, black dress and sailcloth. Staged visible-sea harbor/book image is not a literal match. |
| `gesmerha.unbought_work/start` | Unshaped block with two channels. Current finished carved-bird workshop art has wrong prop state. |
| `arsinoe_city_on_paper/start` | She holds a city print by both corners. Ledger-hand shop portrait can be speaker-only, not exact action art. |
| `seelah.boots/start`, `/sock`, `/finish` | Sock starts on sword then may move to bench; later chosen shoulder closeness is separate. Stockinged feet, not combat boots. |
| `soana.threshold/wait` versus `/hold` | Patient gap-opening versus cloth restraint with scrape/blood are different branch outcomes. Do not reuse one rescue image blindly. |
| `vellexia.unfinished_likeness/picture`, `/picture_changed` | Existing pair depicts actual enchanted picture states. Actual speaker returns on `/expectation`; folded-arms state is absent from pair. |
| `areelu.trickster_opening.the_original/entry` | Sending crystal projects her laboratory image. No fixed Commander and no physical shared-room touching. |
| `devarra.trickster.first_answer/arrival` | Huge red dragon claw at bronze threshold. Humanoid concept cannot represent current body. |
| `eliandra.trickster.first_private_audience/invitation` | Native bald identity and text silver-at-temples cue require clarification before art; no automatic hair invention. |
| `aranka.the_wrong_refrain/flight` | Past dream-wing recollection, physically grounded now. Do not generate current real flight. |

## All 43 characters

Shared Tirabade and Minagho/Chivarro counts appear under both participants for coverage, but are not additive route totals.
No exposed local scene means source intake is required; existing native or RanRomance content is not assumed absent.

| Character | Registered / draft IDs touching mapped family | Nodes actually read / primary total | Outstanding coverage |
| --- | --- | --- | --- |
| Anevia | 103 / 0 | 670 / 670 | Exported individual and Tirabade scenes read; actual image review pending |
| Irabeth | 99 / 0 | 704 / 704 | Exported individual and Tirabade scenes read; actual image review pending |
| Seelah | 41 / 0 | 9 / 351 | Full family assessment pending |
| Konomi | 75 / 0 | 644 / 644 | All75 exported scenes read; source variants and image approvals separate |
| Jerribeth | 38 / 0 | 1 / 253 | Full family assessment pending |
| Kiana | 39 / 1 | 1 / 293 | Full family assessment pending |
| Vellexia | 30 / 0 | 164 / 164 | All exported scenes and endings read; actual image review pending |
| Arsinoe | 33 / 0 | 1 / 182 | Full family assessment pending |
| Gesmerha | 38 / 0 | 1 / 165 | Full family assessment pending |
| Minagho | 47 / 0 | 218 / 218 | Exported shared continuation read; native parent route and image approval not covered |
| Chivarro | 47 / 0 | 218 / 218 | Exported shared continuation read; native parent route and image approval not covered |
| Nocticula | 146 / 1 | 2 / 968 | Full family assessment pending |
| Nurah | 13 / 0 | 1 / 147 | Full family assessment pending |
| Targona | 8 / 64 | 2 / 615 | Full family assessment pending |
| Terendelev | 0 / 17 | 1 / 98 | Full family assessment pending |
| Aranka | 10 / 0 | 52 / 93 | First four scenes read; later intimacy and route outcomes pending |
| Arueshalae | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Camellia | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Wenduag | 0 / 1 | 1 / 11 | Full family assessment pending |
| Galfrey | 0 / 8 | 1 / 32 | Full family assessment pending |
| Soana | 35 / 0 | 9 / 236 | Full family assessment pending |
| Areelu | 0 / 33 | 1 / 222 | Full family assessment pending |
| Ember | 36 / 0 | 1 / 181 | Friendship-only, deferred; full scene assessment pending |
| Aivu | 30 / 0 | 1 / 136 | Friendship-only, deferred; full scene assessment pending |
| Jannah Aldori | 0 / 5 | 1 / 63 | Full family assessment pending |
| Yaniel | 0 / 2 | 1 / 41 | Full family assessment pending |
| Delamere | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Elyanka Camilary | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Herrax | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Mielarah | 0 / 16 | 1 / 168 | Full family assessment pending |
| Shamira | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Hepzamirah | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Iomedae | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Eliandra | 0 / 1 | 1 / 35 | Full family assessment pending |
| Devarra | 0 / 73 | 2 / 1003 | Full family assessment pending |
| Melazmera | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Nidalynn | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Nenio | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Eritrice | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Chadali | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Horzalah | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Kaylessa | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |
| Dorgelinda Stranglehold | 0 / 0 | 0 / 0 | No exposed local scene objects found; native/parent manuscript intake pending |

## Assessed page decisions

| Exact scene/node | Decision | Setting and form | Participants and reason |
| --- | --- | --- | --- |
| `a_cup/start` | cg_candidate | headquarters chair and papers; everyday duty clothes, no intimate state | Anevia; Commander offscreen. Moving papers off offered chair beside cold cup gives a distinct welcoming action; generic armed wall portrait is speaker-only. |
| `seelah.boots/start` | cg_needed | bench beside fire; stockinged feet, boots upside down; worn cloth sleeve, no full combat boots | Seelah; Commander offscreen. Playful sock on sword pommel before sock branch moves it; strong off-duty action. |
| `seelah.boots/company` | reuse_scene_or_speaker | bench beside fire; stockinged feet, boots upside down; worn cloth sleeve, no full combat boots | Seelah; Commander offscreen. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `seelah.boots/rest` | reuse_scene_or_speaker | bench beside fire; stockinged feet, boots upside down; worn cloth sleeve, no full combat boots | Seelah; Commander offscreen. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `seelah.boots/sock` | optional_action_variant | bench beside fire; stockinged feet, boots upside down; worn cloth sleeve, no full combat boots | Seelah; Commander offscreen. She laughs and removes sock from pommel to bench; initial sock-on-sword CG cannot persist as exact current illustration afterward. |
| `seelah.boots/meal` | reuse_scene_or_speaker | bench beside fire; Stockinged/off-duty; sock position differs by incoming branch, keep it out of frame. | Seelah; Commander offscreen. Shared bench/food setting; apple and knife state varies, so use restrained shared scene portrait rather than one CG per reply. |
| `seelah.boots/road` | reuse_scene_or_speaker | bench beside fire; Stockinged/off-duty; sock position differs by incoming branch, keep it out of frame. | Seelah; Commander offscreen. Shared bench/food setting; apple and knife state varies, so use restrained shared scene portrait rather than one CG per reply. |
| `seelah.boots/home` | reuse_scene_or_speaker | bench beside fire; Stockinged/off-duty; sock position differs by incoming branch, keep it out of frame. | Seelah; Commander offscreen. Shared bench/food setting; apple and knife state varies, so use restrained shared scene portrait rather than one CG per reply. |
| `seelah.boots/plans` | reuse_scene_or_speaker | bench beside fire; Stockinged/off-duty; sock position differs by incoming branch, keep it out of frame. | Seelah; Commander offscreen. Shared bench/food setting; apple and knife state varies, so use restrained shared scene portrait rather than one CG per reply. |
| `seelah.boots/finish` | cg_candidate | bench beside fire; Stockinged/off-duty; sock position differs by incoming branch, keep it out of frame. | Seelah; Commander offscreen. Deliberate shoulder closeness with room to spare; subtle earned comfort rather than mandatory kiss. |
| `konomi.return_letter/start` | no_new_cg | Commander desk; Konomi absent | Commander hands optional, otherwise objects only. Unfinished invitation letter; no physical visit or gown claim. |
| `jerribeth.invitation/start` | cg_candidate | message desk, lacquered correspondence frame; Jerribeth absent until activated image | Frame and note; no physical Jerribeth. Object-focused charm discovery could introduce remote channel; existing speaker portrait must not imply in-person arrival. |
| `kiana.invitation/start` | no_new_cg | correspondence; Kiana absent | Folded story page. Letter invitation has no present Kiana; reuse object/letter treatment rather than costume CG. |
| `ember.drawing/start` | cg_needed_deferred | sheltered Drezen paving; age-appropriate friendship dress | Ember, Soot, chalk creature. Ground-level drawing/crow composition is specific and affectionate without romance. |
| `soana.threshold/start` | cg_needed | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Knife/cloth and caught basket strap, before rescue choice; current basket/jar seated forest portrait does not depict fox rescue. |
| `soana.threshold/look` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `soana.threshold/wait` | cg_candidate_branch | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Patient gap opening and outward knife cut; fox escapes without rough restraint. Pick preescape moment and do not add cloth over head. |
| `soana.threshold/wait_cost` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Patient branch after fox escaped; severed strap and loss of daylight, no fox still trapped. |
| `soana.threshold/hold` | cg_candidate_branch | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Fast cloth restraint, scraped hand and minor blood on wicker differ materially from patient branch. Do not reuse gentle-uninjured outcome art. |
| `soana.threshold/hold_room` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Fast branch after escape retains scraped hand; padding/reed gathering vary. Current smiling jar portrait not proof of these actions. |
| `soana.threshold/hold_pad` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Fast branch after escape retains scraped hand; padding/reed gathering vary. Current smiling jar portrait not proof of these actions. |
| `soana.threshold/end_wait` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Patient branch after fox escaped; severed strap and loss of daylight, no fox still trapped. |
| `soana.threshold/end_held` | reuse_scene_or_speaker | cave mouth; outdoor working clothing; adult dwarf, no glamour transformation | Soana, trapped ordinary fox; Commander offscreen. Fast branch after escape retains scraped hand; padding/reed gathering vary. Current smiling jar portrait not proof of these actions. |
| `arsinoe_city_on_paper/start` | cg_needed | shop table; clerical civilian robes matching linked identity | Arsinoe; illustrated city print. Both hands hold print by corners; current ledger-hand art has wrong object/action for literal illustration. |
| `targona.unasked_question/start` | no_new_cg | personal correspondence; Targona absent; wing state unseen | Letter and folded laboratory door drawing. Paper-house portrait is not literal current object; use speaker portrait scope or separate drawing closeup. |
| `gesmerha.unbought_work/start` | cg_needed | workbench; civilian craft clothes, blindness retained | Gesmerha, unshaped wooden block, broken-handle cup. Existing carved bird is too finished and wrong object; need hands following shallow channels. |
| `vellexia.unfinished_likeness/start` | reuse_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Head portrait usable as speaker only; full action CG would need bracelet/reversed picture. |
| `vellexia.unfinished_likeness/warning` | reuse_scene_or_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Current explicit Vellexia key is distinct from staged VellexiaManorSpeaker; missing key is an assignment gap, not need for new painting. |
| `vellexia.unfinished_likeness/jerribeth` | reuse_scene_or_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `vellexia.unfinished_likeness/terms` | reuse_scene_or_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `vellexia.unfinished_likeness/picture` | existing_scene_cg | enchanted painting of ordinary room, daylight; painted white dress, sleeve at elbow | painted Vellexia, chipped cup. Existing day painting matches explicitly authored likeness, not real speaker. |
| `vellexia.unfinished_likeness/picture_changed` | existing_scene_cg | same enchanted room, darkened sky; same white dress | painted Vellexia, whole cup. Automatic switch carries actual magical change. |
| `vellexia.unfinished_likeness/expectation` | reuse_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Actual speaker resumes; painting folds arms and then stops imitating, so static changed painting must not be literal page image. |
| `vellexia.unfinished_likeness/wager` | reuse_scene_or_speaker | ornate manor low table; native-inspired actual speaker outfit, not painted white dress | Vellexia, reversed dark frame, bracelet. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `aivu.a_city_with_wings/start` | cg_needed_deferred | Drezen ground; dragon actual size must be checked; friendship only | Aivu, map paper, stones. Claw on toothy building and comic boot-map provide distinct adventure image. |
| `aranka.the_wrong_refrain/start` | cg_needed | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Existing relationship permits corner-mouth greeting kiss; single art should pick greeting OR walking, not invented flight. |
| `aranka.the_wrong_refrain/history` | reuse_scene_or_speaker | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `aranka.the_wrong_refrain/keeper` | reuse_scene_or_speaker | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `aranka.the_wrong_refrain/flight` | reuse_speaker | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Recollection of dream wings while physically grounded; no real wings or current flight CG. |
| `aranka.the_wrong_refrain/traveler` | reuse_scene_or_speaker | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `aranka.the_wrong_refrain/song` | cg_candidate | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Quiet four-line song and grass-stalk knot; mouth/breath/hand action distinct from posed lute portrait. |
| `aranka.the_wrong_refrain/venues` | optional_action_variant | island path then grass; outdoor performer clothes; no current real wings implied | Aranka; customizable Commander offscreen or carefully cropped. Grass ring breaks and she laughs; proposed crowds/venues not yet implemented within this page. |
| `anevia.unborrowed_hour/start` | cg_candidate | table then exit; coat only reached for at end; practical off-duty clothes | Anevia, broken basket handle, string; runner transient. Hands repairing picnic basket; generic wall-lean portrait cannot show the specific action. |
| `irabeth.a_name_on_the_list/start` | cg_candidate | private discussion at page/list; not specified; do not infer armor from generic portrait | Irabeth, recitation sign-up page. Palm uncovers her name and charcoal crown; illustrative performance happens later, not on this page. |
| `minachiv.two_answers/start` | cg_needed | windowless room above shuttered gaming house, dusk; begins blonde human disguise then native lilitu form | Minagho only; Chivarro absent. Actual scene includes physical meeting and dropped disguise after initial note. Two form images or native-form midpage; NOT letter-only classification. |
| `minachiv.two_answers/reply` | reuse_scene_or_speaker | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `minachiv.two_answers/scrolls` | reuse_scene_or_speaker | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `minachiv.two_answers/asking` | reuse_scene_or_speaker | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Same read scene; keep a suitable speaker/setting image unless action or branch notes below require a switch. |
| `minachiv.two_answers/past` | cg_candidate_branch | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Prior relationship only: leans closer but stops and leaves hand distance. No forced kiss or Chivarro already present. |
| `minachiv.two_answers/refusal` | reuse_scene_or_speaker | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Refused-history route keeps meeting nonromantic; do not reuse leaning-close relationship CG. |
| `minachiv.two_answers/agreement` | optional_action_variant | windowless room above shuttered gaming house, dusk; Minagho native lilitu form after disguise dropped; brand status needs native/history evidence | Minagho; Commander offscreen; Chivarro absent. Packet pocketed then brief sleeve touch at door; preserve exact moment and avoid fixed Commander body. |
| `noct.unlit_quay/start` | cg_needed | dream quay without sea; black dress with dry hem; native demon form | Nocticula on bollard then standing; sailcloth. Missing water, remote rain, black flower cloth; staged sea harbor/book/parapet is wrong literal setting. |
| `noct.acq.audience_missed/history` | reuse_native_portrait | native audience context requires preceding cue; native court attire | Nocticula; Commander offscreen. Verbal testing in audience; no earned shared evening. Native portrait sufficient until actual gesture event warrants CG. |
| `nurah.borrowed_name/start` | cg_candidate | delivery/correspondence; Nurah absent | Cheap book, fine wrapper, waiting messenger. Seditious book with duplicate page nine and scored paragraph can support an object insert; no in-person seduction. |
| `areelu.trickster_opening.the_original/entry` | cg_needed | sending-crystal projection from laboratory to desk; adult Areelu native research attire; projection not shared physical room | Areelu projected, shard/table/notes; Commander reflection optional but unfixed. Strong cold intellectual confrontation; exclude fixed Commander face and physical touch. |
| `devarra.trickster.first_answer/arrival` | cg_needed | Storyteller tower bronze doorway; huge red dragon, healed wing seam | Devarra claw across threshold; Commander offscreen. Humanoid candidate cannot replace actual dragon. Confrontation image preserves threatening scale and open retreat. |
| `devarra.trickster.the_second_envelope/second_envelope` | cg_needed | tower east gallery stone table; dragon with claws, no earned humanoid assumption | Devarra, dark-wax envelope. Quest threat between claws; brood history unresolved until selected branch, so no eggs/children in image. |
| `eliandra.trickster.first_private_audience/invitation` | authored_redesign_scope | Pulura temple west arch, evening; no ceremonial veil; source mentions silver at temples | Eliandra, distant Katair/guard optional. Native bald reference differs from silver-temple text. Latest user permits attractive authored hair; record redesign rather than native fact. No prose change or automatic image approval. |
| `galfrey.angel.the_space_between_orders/start` | reuse_speaker | orders desk; duty context, exact attire unspecified | Galfrey, pen and orders. Quiet signing gesture could reuse suitable duty portrait; no need for bespoke CG solely for two lines. |
| `jannah.trickster.the_misdelivered_hour/start` | no_new_cg | letter delivery; Jannah absent | Two sealed envelopes, only personal one opened. No physical restored officer/personal meeting yet; letter treatment sufficient. |
| `mielarah.opening.the_invitation/start` | cg_needed | Colyphyr mooring, Commander remains quay-side; captain outfit must follow native reference intake | Mielarah, brass-edged chart; ship/crew alive. Clear ship-access boundary and sharp invitation; no boarding or curse cure shown before choice. |
| `targona.trickster_acq.the_second_letter/start` | no_new_cg | personal packet; Targona absent | Second letter and copied reply. Signal-marker proposal is written, not current field encounter; no magic fate intervention visual yet. |
| `terendelev.continuation.returned_letter/start` | no_new_cg | unsealed letter delivery; Terendelev absent, restored state not independently proven by portrait | Letter with silver edge. Garden meeting only after acceptance; do not show bodily restoration from correspondence alone. |
| `wenduag.vellexia_network.reception/start` | cg_candidate_draft_only | reception after crowd thins; Wenduag spider limbs close and still; Vellexia actual reception outfit | Wenduag foreground, Vellexia distant. Proposed mutual-interest recognition; not completed triad or earned physical intimacy. Writing freeze preserves draft only. |
| `yaniel.opening.the_letter/opening` | no_new_cg | post-Fane letter; Yaniel absent, recovery not instant youth | Unsealed personal letter. First meeting awaits choice and venue; no automatic healed-body CG. |

## Reviewer proposals, separate from current scenes

| Provenance | Proposed image opportunity |
| --- | --- |
| `Writer/handoffs/gesmerha.md` | Recarve ruined Lady statue; separate from currently read unshaped block. |
| `Writer/handoffs/gesmerha.md GES-06 and soana.md SOA-08` | Conflicting Wintersun visions confrontation, not newly approved triad. |
| `Writer/handoffs/vellexia.md` | Gushing delight beside disturbingly lifelike chair. |
| `Writer/handoffs/trickster/vellexia.md` | Unfinished likeness/Storyteller return concept; not existing changing white painting. |
| `Writer/handoffs/anevia.md, yaniel.md, arsinoe.md` | Character-led romantic physical initiative; exact revised scenes remain proposals under writing freeze. |
| `Writer/handoffs/kiana.md KIA-05/06` | Secret attraction and eventual discovery, branch-specific marriage state. |
| `Writer/handoffs/nocticula.md NOC-05/06 and minagho-chivarro.md MCH-04` | Dangerous appetite and sensual authority; scene must support it, not automatic cruelty. |

These proposals do not establish implemented events or justify altering route prose during the freeze.
Do not convert every reviewer suggestion into romance, resurrection or a new group relationship.

## Complete scene backlog

Every primary scene ID is listed here; all node IDs, text hashes and condition details are in the JSON, with prose evidence for assessed pages only.
The read count is actual text assessment, not inferred from filenames, titles or asset existence.
Registered status means present in the pinned development export, not installed or playable approval.
Draft-only IDs include alternate templates exposed by source modules; they are not all runtime candidates.
For Nocticula history copies, the completion alias and source provenance remain in metadata; do not sum the copies as new art demand.
For Devarra brood histories and Targona mythic variants, compare selected outcome before reusing a shared setting.

| Scene ID | Family | Registration | Read nodes / total | Source |
| --- | --- | --- | --- | --- |
| `a_cup` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `i_watch` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `a_errand` | tirabade | registered | 6 / 6 | `story.py or export integration; exact origin not yet resolved` |
| `i_hands` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `a_roof` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `i_respite` | tirabade | registered | 9 / 9 | `story.py or export integration; exact origin not yet resolved` |
| `a_crossing` | tirabade | registered | 8 / 8 | `story.py or export integration; exact origin not yet resolved` |
| `i_crossing` | tirabade | registered | 9 / 9 | `story.py or export integration; exact origin not yet resolved` |
| `a_morning` | tirabade | registered | 5 / 5 | `story.py or export integration; exact origin not yet resolved` |
| `i_morning` | tirabade | registered | 5 / 5 | `story.py or export integration; exact origin not yet resolved` |
| `reckoning` | tirabade | registered | 8 / 8 | `story.py or export integration; exact origin not yet resolved` |
| `a_truth` | tirabade | registered | 8 / 8 | `story.py or export integration; exact origin not yet resolved` |
| `i_truth` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `table` | tirabade | registered | 12 / 12 | `story.py or export integration; exact origin not yet resolved` |
| `ordinary` | tirabade | registered | 9 / 9 | `story.py or export integration; exact origin not yet resolved` |
| `a_self` | tirabade | registered | 6 / 6 | `story.py or export integration; exact origin not yet resolved` |
| `power` | tirabade | registered | 13 / 13 | `story.py or export integration; exact origin not yet resolved` |
| `future` | tirabade | registered | 14 / 14 | `story.py or export integration; exact origin not yet resolved` |
| `shared_night` | tirabade | registered | 6 / 6 | `story.py or export integration; exact origin not yet resolved` |
| `last_watch` | tirabade | registered | 7 / 7 | `story.py or export integration; exact origin not yet resolved` |
| `ending_together` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_apart` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_unfinished` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_loss` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_ascend` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_monster` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `ending_aeon` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `i_self` | tirabade | registered | 6 / 6 | `story.py or export integration; exact origin not yet resolved` |
| `departure` | tirabade | registered | 4 / 4 | `story.py or export integration; exact origin not yet resolved` |
| `abyss_letter` | tirabade | registered | 4 / 4 | `story.py or export integration; exact origin not yet resolved` |
| `abyss_dream` | tirabade | registered | 2 / 2 | `story.py or export integration; exact origin not yet resolved` |
| `a_waiting` | tirabade | registered | 2 / 2 | `story.py or export integration; exact origin not yet resolved` |
| `return` | tirabade | registered | 14 / 14 | `story.py or export integration; exact origin not yet resolved` |
| `parting` | tirabade | registered | 8 / 8 | `story.py or export integration; exact origin not yet resolved` |
| `seelah.boots` | seelah | registered | 9 / 9 | `storylines/seelah.py` |
| `seelah.wager` | seelah | registered | 0 / 8 | `storylines/seelah.py` |
| `seelah.promise` | seelah | registered | 0 / 8 | `storylines/seelah.py` |
| `seelah.kept` | seelah | registered | 0 / 5 | `storylines/seelah.py` |
| `three_locks` | tirabade | registered | 14 / 14 | `storylines/tirabade_later.py` |
| `three_outing` | tirabade | registered | 16 / 16 | `storylines/tirabade_later.py` |
| `three_yard` | tirabade | registered | 10 / 10 | `storylines/tirabade_campaign.py` |
| `three_match` | tirabade | registered | 11 / 11 | `storylines/tirabade_campaign.py` |
| `three_beth_score` | tirabade | registered | 12 / 12 | `storylines/tirabade_campaign.py` |
| `three_anevia_flour` | tirabade | registered | 17 / 17 | `storylines/tirabade_campaign.py` |
| `three_return_game` | tirabade | registered | 10 / 10 | `storylines/tirabade_campaign.py` |
| `three_small_journeys` | tirabade | registered | 11 / 11 | `storylines/tirabade_campaign.py` |
| `seelah.changed_opening` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.door` | seelah | registered | 0 / 9 | `storylines/seelah_later.py` |
| `seelah.morning` | seelah | registered | 0 / 7 | `storylines/seelah_later.py` |
| `seelah.weight` | seelah | registered | 0 / 6 | `storylines/seelah_later.py` |
| `seelah.watch` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.souls` | seelah | registered | 0 / 9 | `storylines/seelah_later.py` |
| `seelah.road` | seelah | registered | 0 / 36 | `storylines/seelah_later.py` |
| `seelah.ordinary` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.farewell` | seelah | registered | 0 / 11 | `storylines/seelah_later.py` |
| `seelah.parting` | seelah | registered | 0 / 3 | `storylines/seelah_later.py` |
| `seelah.ending_together` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_unsettled` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_grieving` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_unfinished_work` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_changed` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_ascended` | seelah | registered | 0 / 4 | `storylines/seelah_later.py` |
| `seelah.ending_apart` | seelah | registered | 0 / 1 | `storylines/seelah_later.py` |
| `seelah.ending_unfinished` | seelah | registered | 0 / 1 | `storylines/seelah_later.py` |
| `seelah.ending_aeon` | seelah | registered | 0 / 1 | `storylines/seelah_later.py` |
| `seelah.fate_life` | seelah | registered | 0 / 1 | `storylines/seelah_fate.py` |
| `seelah.fate_return` | seelah | registered | 0 / 4 | `storylines/seelah_fate.py` |
| `seelah.letter` | seelah | registered | 0 / 7 | `storylines/seelah_abyss.py` |
| `seelah.letter_after` | seelah | registered | 0 / 8 | `storylines/seelah_abyss.py` |
| `seelah.letter_work` | seelah | registered | 0 / 12 | `storylines/seelah_abyss.py` |
| `seelah.borrowed_saw` | seelah | registered | 0 / 24 | `storylines/seelah_aftermath.py` |
| `seelah.platform_finished` | seelah | registered | 0 / 9 | `storylines/seelah_aftermath.py` |
| `seelah.inheritors_corner` | seelah | registered | 0 / 15 | `storylines/seelah_aftermath.py` |
| `seelah.roof_evening` | seelah | registered | 0 / 14 | `storylines/seelah_aftermath.py` |
| `konomi.return_letter` | konomi | registered | 6 / 6 | `storylines/konomi_return_invitation.py` |
| `konomi.retained_inquiry` | konomi | registered | 10 / 10 | `storylines/konomi_retained_return.py` |
| `konomi.retained_attempt` | konomi | registered | 2 / 2 | `storylines/konomi_retained_return.py` |
| `konomi.return_first_words` | konomi | registered | 11 / 11 | `storylines/konomi_retained_return.py` |
| `konomi.return_second_visit` | konomi | registered | 12 / 12 | `storylines/konomi_retained_return.py` |
| `konomi.margin` | konomi | registered | 7 / 7 | `storylines/konomi.py` |
| `konomi.reception` | konomi | registered | 6 / 6 | `storylines/konomi.py` |
| `konomi.letter` | konomi | registered | 5 / 5 | `storylines/konomi.py` |
| `konomi.evening` | konomi | registered | 11 / 11 | `storylines/konomi.py` |
| `konomi.disagreement` | konomi | registered | 5 / 5 | `storylines/konomi.py` |
| `konomi.leak` | konomi | registered | 6 / 6 | `storylines/konomi.py` |
| `konomi.reckoning` | konomi | registered | 13 / 13 | `storylines/konomi.py` |
| `konomi.unsent` | konomi | registered | 6 / 6 | `storylines/konomi.py` |
| `konomi.return` | konomi | registered | 13 / 13 | `storylines/konomi.py` |
| `konomi.power` | konomi | registered | 7 / 7 | `storylines/konomi.py` |
| `konomi.ordinary` | konomi | registered | 10 / 10 | `storylines/konomi.py` |
| `konomi.farewell` | konomi | registered | 2 / 2 | `storylines/konomi.py` |
| `konomi.parting` | konomi | registered | 3 / 3 | `storylines/konomi.py` |
| `konomi.hearing` | konomi | registered | 13 / 13 | `storylines/konomi.py` |
| `konomi.hearing_after` | konomi | registered | 11 / 11 | `storylines/konomi.py` |
| `konomi.new_letter` | konomi | registered | 21 / 21 | `storylines/konomi.py`, `storylines/konomi_private_hearing.py` |
| `konomi.fate_post` | konomi | registered | 8 / 8 | `storylines/konomi.py` |
| `konomi.fate_reply` | konomi | registered | 6 / 6 | `storylines/konomi.py` |
| `konomi.private_meeting` | konomi | registered | 15 / 15 | `storylines/konomi.py` |
| `konomi.ending_public` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_private` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_changed` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_ascended` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_apart` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_dismissed_apart` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_unfinished` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.ending_aeon` | konomi | registered | 1 / 1 | `storylines/konomi.py` |
| `konomi.private_history` | konomi | registered | 35 / 35 | `storylines/konomi_history.py` |
| `konomi.carriers` | konomi | registered | 10 / 10 | `storylines/konomi_private.py` |
| `konomi.before_road` | konomi | registered | 13 / 13 | `storylines/konomi_private.py` |
| `konomi.private_departure` | konomi | registered | 11 / 11 | `storylines/konomi_private.py` |
| `konomi.capital_letter` | konomi | registered | 9 / 9 | `storylines/konomi_distance.py` |
| `konomi.return_offer` | konomi | registered | 6 / 6 | `storylines/konomi_distance.py` |
| `konomi.private_reunion` | konomi | registered | 41 / 41 | `storylines/konomi_distance.py` |
| `konomi.lease_offer` | konomi | registered | 8 / 8 | `storylines/konomi_future.py` |
| `konomi.chosen_evening` | konomi | registered | 14 / 14 | `storylines/konomi_future.py` |
| `konomi.private_future_choice` | konomi | registered | 5 / 5 | `storylines/konomi_future.py` |
| `konomi.ending_distance` | konomi | registered | 1 / 1 | `storylines/konomi_future.py` |
| `konomi.ending_distance_open` | konomi | registered | 1 / 1 | `storylines/konomi_future.py` |
| `konomi.ending_distance_apart` | konomi | registered | 1 / 1 | `storylines/konomi_future.py` |
| `konomi.ending_distance_changed_open` | konomi | registered | 1 / 1 | `storylines/konomi_future.py` |
| `konomi.ending_distance_ascended_open` | konomi | registered | 1 / 1 | `storylines/konomi_future.py` |
| `konomi.private_hearing` | konomi | registered | 15 / 15 | `storylines/konomi_private_hearing.py` |
| `konomi.private_hearing_after` | konomi | registered | 13 / 13 | `storylines/konomi_private_hearing.py` |
| `konomi.private_new_letter` | konomi | registered | 21 / 21 | `storylines/konomi_private_hearing.py` |
| `jerribeth.invitation` | jerribeth | registered | 1 / 6 | `storylines/jerribeth.py` |
| `jerribeth.question` | jerribeth | registered | 0 / 5 | `storylines/jerribeth.py` |
| `jerribeth.guise` | jerribeth | registered | 0 / 5 | `storylines/jerribeth.py` |
| `jerribeth.price` | jerribeth | registered | 0 / 7 | `storylines/jerribeth.py` |
| `jerribeth.evening` | jerribeth | registered | 0 / 10 | `storylines/jerribeth.py` |
| `jerribeth.commission` | jerribeth | registered | 0 / 4 | `storylines/jerribeth.py` |
| `jerribeth.patron` | jerribeth | registered | 0 / 4 | `storylines/jerribeth.py` |
| `jerribeth.collection` | jerribeth | registered | 0 / 5 | `storylines/jerribeth.py` |
| `jerribeth.refuge` | jerribeth | registered | 0 / 4 | `storylines/jerribeth.py` |
| `jerribeth.future` | jerribeth | registered | 0 / 9 | `storylines/jerribeth.py` |
| `jerribeth.ordinary` | jerribeth | registered | 0 / 7 | `storylines/jerribeth.py` |
| `jerribeth.farewell` | jerribeth | registered | 0 / 3 | `storylines/jerribeth.py` |
| `jerribeth.parting` | jerribeth | registered | 0 / 3 | `storylines/jerribeth.py` |
| `jerribeth.ending_together` | jerribeth | registered | 0 / 7 | `storylines/jerribeth.py` |
| `jerribeth.ending_ascended` | jerribeth | registered | 0 / 7 | `storylines/jerribeth.py` |
| `jerribeth.ending_apart` | jerribeth | registered | 0 / 1 | `storylines/jerribeth.py` |
| `jerribeth.ending_unfinished` | jerribeth | registered | 0 / 1 | `storylines/jerribeth.py` |
| `jerribeth.ending_aeon` | jerribeth | registered | 0 / 1 | `storylines/jerribeth.py` |
| `jerribeth.offered_signature` | jerribeth | registered | 0 / 8 | `storylines/jerribeth_consequences.py` |
| `jerribeth.borrowed_sun` | jerribeth | registered | 0 / 8 | `storylines/jerribeth_consequences.py` |
| `jerribeth.small_print` | jerribeth | registered | 0 / 8 | `storylines/jerribeth_consequences.py` |
| `jerribeth.unsold_evening` | jerribeth | registered | 0 / 11 | `storylines/jerribeth_consequences.py` |
| `jerribeth.purchaser_answer` | jerribeth | registered | 0 / 14 | `storylines/jerribeth_consequences.py` |
| `kiana.invitation` | kiana | registered | 1 / 2 | `storylines/kiana.py` |
| `kiana.rehearsal` | kiana | registered | 0 / 4 | `storylines/kiana.py` |
| `kiana.stagecraft` | kiana | registered | 0 / 9 | `storylines/kiana.py` |
| `kiana.marriage` | kiana | registered | 0 / 5 | `storylines/kiana.py` |
| `kiana.widow` | kiana | registered | 0 / 4 | `storylines/kiana.py` |
| `kiana.answer` | kiana | registered | 0 / 4 | `storylines/kiana.py` |
| `kiana.date` | kiana | registered | 0 / 9 | `storylines/kiana.py` |
| `kiana.morning` | kiana | registered | 0 / 9 | `storylines/kiana.py` |
| `kiana.seelah` | kiana | registered | 0 / 5 | `storylines/kiana.py` |
| `kiana.farewell` | kiana | registered | 0 / 3 | `storylines/kiana.py` |
| `kiana.parting` | kiana | registered | 0 / 3 | `storylines/kiana.py` |
| `kiana.ending_together` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.ending_bereaved` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.ending_ascended` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.ending_apart` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.ending_unfinished` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.ending_aeon` | kiana | registered | 0 / 1 | `storylines/kiana.py` |
| `kiana.guest_table` | kiana | registered | 0 / 11 | `storylines/kiana_consequences.py` |
| `kiana.market_weather` | kiana | registered | 0 / 14 | `storylines/kiana_consequences.py` |
| `kiana.lenna_door` | kiana | registered | 0 / 10 | `storylines/kiana_consequences.py` |
| `kiana.blue_room` | kiana | registered | 0 / 29 | `storylines/kiana_consequences.py` |
| `kiana.bakery_stairs` | kiana | registered | 0 / 13 | `storylines/kiana_followthrough.py` |
| `kiana.last_page` | kiana | registered | 0 / 11 | `storylines/kiana_followthrough.py` |
| `kiana.first_readers` | kiana | registered | 0 / 19 | `storylines/kiana_followthrough.py` |
| `kiana.ink_after` | kiana | registered | 0 / 12 | `storylines/kiana_followthrough.py` |
| `kiana.working_room` | kiana | registered | 0 / 10 | `storylines/kiana_followthrough.py` |
| `kiana.kept_evening` | kiana | registered | 0 / 15 | `storylines/kiana_followthrough.py` |
| `ember.drawing` | ember | registered | 1 / 8 | `storylines/ember.py` |
| `ember.visitor` | ember | registered | 0 / 6 | `storylines/ember.py` |
| `ember.rain` | ember | registered | 0 / 9 | `storylines/ember.py` |
| `ember.paper_bird` | ember | registered | 0 / 9 | `storylines/ember_afternoons.py` |
| `ember.missing_cloth` | ember | registered | 0 / 12 | `storylines/ember_afternoons.py` |
| `ember.courtyard_play` | ember | registered | 0 / 12 | `storylines/ember_afternoons.py` |
| `ember.after_applause` | ember | registered | 0 / 10 | `storylines/ember_afternoons.py` |
| `ember.second_ending` | ember | registered | 0 / 10 | `storylines/ember_afternoons.py` |
| `soana.threshold` | soana | registered | 9 / 9 | `storylines/soana_opening.py` |
| `soana.water_carrier` | soana | registered | 0 / 14 | `storylines/soana_opening.py` |
| `soana.guardian_question` | soana | registered | 0 / 18 | `storylines/soana_opening.py` |
| `seelah.late_course` | seelah | registered | 0 / 8 | `storylines/seelah_late_campaign.py` |
| `seelah.late_lesson` | seelah | registered | 0 / 10 | `storylines/seelah_late_campaign.py` |
| `seelah.late_page` | seelah | registered | 0 / 12 | `storylines/seelah_late_campaign.py` |
| `seelah.late_race` | seelah | registered | 0 / 13 | `storylines/seelah_late_campaign.py` |
| `seelah.late_afterglow` | seelah | registered | 0 / 10 | `storylines/seelah_late_campaign.py` |
| `seelah.late_first_step` | seelah | registered | 0 / 12 | `storylines/seelah_late_campaign.py` |
| `three_stolen_roads` | tirabade | registered | 9 / 9 | `storylines/tirabade_reckoning.py` |
| `three_lantern_debt` | tirabade | registered | 15 / 15 | `storylines/tirabade_reckoning.py` |
| `three_beth_steps` | tirabade | registered | 16 / 16 | `storylines/tirabade_reckoning.py` |
| `three_ista_departure` | tirabade | registered | 8 / 8 | `storylines/tirabade_reckoning.py` |
| `three_lantern_turn` | tirabade | registered | 15 / 15 | `storylines/tirabade_reckoning.py` |
| `three_open_road` | tirabade | registered | 10 / 10 | `storylines/tirabade_reckoning.py` |
| `jerribeth.counterfeit_guest` | jerribeth | registered | 0 / 9 | `storylines/jerribeth_counteroffer.py` |
| `jerribeth.counterfeit_hinge` | jerribeth | registered | 0 / 7 | `storylines/jerribeth_counteroffer.py` |
| `jerribeth.counterfeit_clerk` | jerribeth | registered | 0 / 11 | `storylines/jerribeth_counteroffer.py` |
| `jerribeth.counterfeit_audience` | jerribeth | registered | 0 / 10 | `storylines/jerribeth_counteroffer.py` |
| `jerribeth.counterfeit_spoil` | jerribeth | registered | 0 / 11 | `storylines/jerribeth_counteroffer.py` |
| `jerribeth.counterfeit_after` | jerribeth | registered | 0 / 12 | `storylines/jerribeth_counteroffer.py` |
| `seelah.letter_return` | seelah | registered | 0 / 20 | `storylines/seelah_return.py` |
| `seelah.future_followup` | seelah | registered | 0 / 20 | `storylines/seelah_progression.py` |
| `seelah.farewell_catchup` | seelah | registered | 0 / 2 | `storylines/seelah_progression.py` |
| `kiana.another_page` | kiana | registered | 0 / 2 | `storylines/kiana_progression.py` |
| `kiana.a_place_afterward` | kiana | registered | 0 / 12 | `storylines/kiana_progression.py` |
| `kiana.ending_open` | kiana | registered | 0 / 1 | `storylines/kiana_progression.py` |
| `kiana.ending_open_ascended` | kiana | registered | 0 / 1 | `storylines/kiana_progression.py` |
| `kiana.ending_promised` | kiana | registered | 0 / 1 | `storylines/kiana_progression.py` |
| `kiana.ending_open_aeon` | kiana | registered | 0 / 1 | `storylines/kiana_progression.py` |
| `three_borrowed_names` | tirabade | registered | 8 / 8 | `storylines/tirabade_after_roads.py` |
| `three_back_of_seal` | tirabade | registered | 12 / 12 | `storylines/tirabade_after_roads.py` |
| `three_beth_account` | tirabade | registered | 12 / 12 | `storylines/tirabade_after_roads.py` |
| `three_counterclaim` | tirabade | registered | 17 / 17 | `storylines/tirabade_after_roads.py` |
| `three_unposted_notice` | tirabade | registered | 12 / 12 | `storylines/tirabade_after_roads.py` |
| `three_rooms_unlocked` | tirabade | registered | 16 / 16 | `storylines/tirabade_after_roads.py` |
| `three_choose_days` | tirabade | registered | 3 / 3 | `storylines/tirabade_progression.py` |
| `three_more_days` | tirabade | registered | 2 / 2 | `storylines/tirabade_progression.py` |
| `three_kept_days` | tirabade | registered | 4 / 4 | `storylines/tirabade_progression.py` |
| `ending_promised` | tirabade | registered | 1 / 1 | `storylines/tirabade_progression.py` |
| `ending_ascend_promised` | tirabade | registered | 1 / 1 | `storylines/tirabade_progression.py` |
| `jerribeth.settlement_visit` | jerribeth | registered | 0 / 16 | `storylines/jerribeth_progression.py` |
| `jerribeth.room_measure` | jerribeth | registered | 0 / 16 | `storylines/jerribeth_progression.py` |
| `jerribeth.short_invitation` | jerribeth | registered | 0 / 2 | `storylines/jerribeth_progression.py` |
| `jerribeth.promise_revisited` | jerribeth | registered | 0 / 4 | `storylines/jerribeth_progression.py` |
| `jerribeth.old_promise` | jerribeth | registered | 0 / 2 | `storylines/jerribeth_progression.py` |
| `jerribeth.farewell_review` | jerribeth | registered | 0 / 2 | `storylines/jerribeth_progression.py` |
| `jerribeth.another_evening` | jerribeth | registered | 0 / 1 | `storylines/jerribeth_progression.py` |
| `arsinoe_city_on_paper` | arsinoe | registered | 1 / 9 | `storylines/arsinoe_opening.py` |
| `arsinoe_printers_view` | arsinoe | registered | 0 / 11 | `storylines/arsinoe_opening.py` |
| `arsinoe_roofs` | arsinoe | registered | 0 / 14 | `storylines/arsinoe_opening.py` |
| `arsinoe_first_impression` | arsinoe | registered | 0 / 10 | `storylines/arsinoe_opening.py` |
| `arsinoe_hours_of_her_own` | arsinoe | registered | 0 / 14 | `storylines/arsinoe_opening.py` |
| `konomi.political_account` | konomi | registered | 15 / 15 | `storylines/konomi_political.py` |
| `konomi.private_political_account` | konomi | registered | 18 / 18 | `storylines/konomi_political.py` |
| `jerribeth.fate_envelope` | jerribeth | registered | 0 / 6 | `storylines/jerribeth_fate.py` |
| `jerribeth.fate_letter` | jerribeth | registered | 0 / 6 | `storylines/jerribeth_fate.py` |
| `arsinoe_your_hours` | arsinoe | registered | 0 / 7 | `storylines/arsinoe_continuation.py` |
| `arsinoe_borrowed_court` | arsinoe | registered | 0 / 6 | `storylines/arsinoe_continuation.py` |
| `arsinoe_price_of_an_evening` | arsinoe | registered | 0 / 7 | `storylines/arsinoe_continuation.py` |
| `arsinoe_courtyard_company` | arsinoe | registered | 0 / 12 | `storylines/arsinoe_continuation.py` |
| `arsinoe_another_hour` | arsinoe | registered | 0 / 8 | `storylines/arsinoe_continuation.py` |
| `arsinoe_the_unprofitable_hour` | arsinoe | registered | 0 / 10 | `storylines/arsinoe_continuation.py` |
| `soana.one_account` | soana | registered | 0 / 10 | `storylines/soana_continuation.py` |
| `soana.watch_line` | soana | registered | 0 / 10 | `storylines/soana_continuation.py` |
| `soana.price_of_warning` | soana | registered | 0 / 11 | `storylines/soana_continuation.py` |
| `soana.ordinary_feast` | soana | registered | 0 / 11 | `storylines/soana_continuation.py` |
| `soana.name_between` | soana | registered | 0 / 9 | `storylines/soana_continuation.py` |
| `soana.lower_bend` | soana | registered | 0 / 17 | `storylines/soana_continuation.py` |
| `targona.unasked_question` | targona | registered | 1 / 7 | `storylines/targona_opening.py` |
| `targona.second_margin` | targona | registered | 0 / 5 | `storylines/targona_opening.py` |
| `targona.the_folded_room` | targona | registered | 0 / 5 | `storylines/targona_opening.py` |
| `targona.an_unpromised_future` | targona | registered | 0 / 8 | `storylines/targona_opening.py` |
| `targona.the_unscheduled_door` | targona | registered | 0 / 6 | `storylines/targona_opening.py` |
| `targona.what_she_keeps` | targona | registered | 0 / 8 | `storylines/targona_opening.py` |
| `targona.the_open_threshold` | targona | registered | 0 / 14 | `storylines/targona_opening.py` |
| `targona.the_key_remains_hers` | targona | registered | 0 / 5 | `storylines/targona_opening.py` |
| `kiana.later_incident` | kiana | registered | 0 / 1 | `storylines/kiana_further.py` |
| `kiana.borrowed_name` | kiana | registered | 0 / 9 | `storylines/kiana_further.py` |
| `kiana.yard_evening` | kiana | registered | 0 / 12 | `storylines/kiana_further.py` |
| `kiana.unborrowed_evening` | kiana | registered | 0 / 19 | `storylines/kiana_further.py` |
| `kiana.former_grief` | kiana | registered | 0 / 7 | `storylines/kiana_reconciliation.py` |
| `kiana.uncertain_reports` | kiana | registered | 0 / 8 | `storylines/kiana_reconciliation.py` |
| `gesmerha.unbought_work` | gesmerha | registered | 1 / 8 | `storylines/gesmerha_opening.py` |
| `gesmerha.along_the_grain` | gesmerha | registered | 0 / 7 | `storylines/gesmerha_opening.py` |
| `gesmerha.whose_mark` | gesmerha | registered | 0 / 4 | `storylines/gesmerha_opening.py` |
| `gesmerha.the_first_game` | gesmerha | registered | 0 / 9 | `storylines/gesmerha_opening.py` |
| `gesmerha.the_unclaimed_hour` | gesmerha | registered | 0 / 10 | `storylines/gesmerha_opening.py` |
| `gesmerha.against_the_current` | gesmerha | registered | 0 / 9 | `storylines/gesmerha_opening.py` |
| `vellexia.unfinished_likeness` | vellexia | registered | 8 / 8 | `storylines/vellexia_opening.py` |
| `vellexia.second_painter` | vellexia | registered | 8 / 8 | `storylines/vellexia_opening.py` |
| `vellexia.price_of_novelty` | vellexia | registered | 8 / 8 | `storylines/vellexia_opening.py` |
| `vellexia.two_observers` | vellexia | registered | 7 / 7 | `storylines/vellexia_opening.py` |
| `vellexia.unadvertised_hour` | vellexia | registered | 11 / 11 | `storylines/vellexia_opening.py` |
| `vellexia.a_question_kept` | vellexia | registered | 9 / 9 | `storylines/vellexia_opening.py` |
| `vellexia.the_unused_reply` | vellexia | registered | 7 / 7 | `storylines/vellexia_campaign.py` |
| `vellexia.the_price_of_tomorrow` | vellexia | registered | 11 / 11 | `storylines/vellexia_campaign.py` |
| `vellexia.the_second_invitation` | vellexia | registered | 8 / 8 | `storylines/vellexia_campaign.py` |
| `vellexia.the_claim_before_the_event` | vellexia | registered | 7 / 7 | `storylines/vellexia_campaign.py` |
| `vellexia.the_clerks_own_price` | vellexia | registered | 7 / 7 | `storylines/vellexia_campaign.py` |
| `vellexia.the_wager_with_an_edge` | vellexia | registered | 6 / 6 | `storylines/vellexia_campaign.py` |
| `vellexia.an_hour_that_counts` | vellexia | registered | 13 / 13 | `storylines/vellexia_campaign.py` |
| `vellexia.the_question_after_business` | vellexia | registered | 8 / 8 | `storylines/vellexia_campaign.py` |
| `vellexia.the_voice_after_the_abyss` | vellexia | registered | 13 / 13 | `storylines/vellexia_campaign.py` |
| `vellexia.two_unremarkable_pleasures` | vellexia | registered | 9 / 9 | `storylines/vellexia_campaign.py` |
| `vellexia.the_cover_before_the_battle` | vellexia | registered | 11 / 11 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_lovers` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_friends` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_slow` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_interrupted` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_closed` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_dead` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_mirror` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_coercion` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_hostility` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_changed` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_ascent` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_sacrifice` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `vellexia.ending_aeon` | vellexia | registered | 1 / 1 | `storylines/vellexia_campaign.py` |
| `konomi.another_evening` | konomi | registered | 1 / 1 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.a_useful_supper` | konomi | registered | 4 / 4 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.the_upper_passage` | konomi | registered | 8 / 8 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.two_bad_prices` | konomi | registered | 6 / 6 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.the_trial_day` | konomi | registered | 8 / 8 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.a_name_beside_hers` | konomi | registered | 5 / 5 | `storylines/konomi_ordinary_expansion.py` |
| `konomi.the_evening_she_kept` | konomi | registered | 7 / 7 | `storylines/konomi_ordinary_expansion.py` |
| `aivu.a_city_with_wings` | aivu | registered | 1 / 5 | `storylines/aivu_opening.py` |
| `aivu.the_roof_below` | aivu | registered | 0 / 4 | `storylines/aivu_opening.py` |
| `aivu.a_way_for_feet` | aivu | registered | 0 / 5 | `storylines/aivu_opening.py` |
| `aivu.someone_elses_turn` | aivu | registered | 0 / 13 | `storylines/aivu_opening.py` |
| `aivu.a_garden_that_can_go` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.a_late_garden` | aivu | registered | 0 / 3 | `storylines/aivu_campaign.py` |
| `aivu.the_wheel_with_no_cart` | aivu | registered | 0 / 7 | `storylines/aivu_campaign.py` |
| `aivu.the_garden_procession` | aivu | registered | 0 / 5 | `storylines/aivu_campaign.py` |
| `aivu.the_most_important_tail` | aivu | registered | 0 / 7 | `storylines/aivu_campaign.py` |
| `aivu.a_very_important_guest` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.when_the_drum_does_not_come` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.a_castle_in_a_bad_place` | aivu | registered | 0 / 5 | `storylines/aivu_campaign.py` |
| `aivu.the_watch_she_chooses` | aivu | registered | 0 / 8 | `storylines/aivu_campaign.py` |
| `aivu.a_family_with_too_many_names` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.paint_for_a_weather_day` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.a_small_garden_of_her_own` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.the_people_on_the_map` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.the_turn_the_commander_needs` | aivu | registered | 0 / 8 | `storylines/aivu_campaign.py` |
| `aivu.a_reply_from_the_other_garden` | aivu | registered | 0 / 6 | `storylines/aivu_campaign.py` |
| `aivu.the_next_excellent_thing` | aivu | registered | 0 / 8 | `storylines/aivu_campaign.py` |
| `aivu.ending_garden_friend` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_afternoons_unfinished` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_absence_unresolved` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_power_changed` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_dragon_distance` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_parted` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_swarm_loss` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_sacrifice` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_ascended` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `aivu.ending_rewritten` | aivu | registered | 0 / 1 | `storylines/aivu_campaign.py` |
| `konomi.private_absence` | konomi | registered | 8 / 8 | `storylines/konomi_private_absence.py` |
| `konomi.private_absence_catchup` | konomi | registered | 33 / 33 | `storylines/konomi_private_absence.py` |
| `soana.the_thing_in_the_sack` | soana | registered | 0 / 5 | `storylines/soana_later_progression.py` |
| `soana.the_dry_offering` | soana | registered | 0 / 6 | `storylines/soana_later_progression.py` |
| `soana.the_inherited_debt` | soana | registered | 0 / 6 | `storylines/soana_later_progression.py` |
| `soana.a_voice_in_the_dark` | soana | registered | 0 / 6 | `storylines/soana_later_progression.py` |
| `soana.what_followed_home` | soana | registered | 0 / 9 | `storylines/soana_later_progression.py` |
| `soana.a_promise_still_spoken` | soana | registered | 0 / 7 | `storylines/soana_later_progression.py` |
| `soana.the_unwelcome_path` | soana | registered | 0 / 7 | `storylines/soana_later_progression.py` |
| `soana.after_the_last_visitor` | soana | registered | 0 / 10 | `storylines/soana_later_progression.py` |
| `konomi.private_return_terms` | konomi | registered | 10 / 10 | `storylines/konomi_private_consequence.py` |
| `konomi.private_kept_hours` | konomi | registered | 12 / 12 | `storylines/konomi_private_consequence.py` |
| `konomi.private_last_visit` | konomi | registered | 13 / 13 | `storylines/konomi_private_consequence.py` |
| `konomi.ending_distance_lived` | konomi | registered | 3 / 3 | `storylines/konomi_private_consequence.py` |
| `konomi.ending_distance_open_lived` | konomi | registered | 3 / 3 | `storylines/konomi_private_consequence.py` |
| `konomi.a_turn_for_herself` | konomi | registered | 14 / 14 | `storylines/konomi_early_reciprocity.py` |
| `aranka.the_wrong_refrain` | aranka | registered | 7 / 7 | `storylines/aranka_continuation.py` |
| `aranka.where_the_breath_goes` | aranka | registered | 10 / 10 | `storylines/aranka_continuation.py` |
| `aranka.the_name_missing` | aranka | registered | 6 / 6 | `storylines/aranka_continuation.py` |
| `aranka.an_evening_uncommanded` | aranka | registered | 29 / 29 | `storylines/aranka_continuation.py` |
| `aranka.the_song_afterwards` | aranka | registered | 0 / 8 | `storylines/aranka_continuation.py` |
| `aranka.no_encore_needed` | aranka | registered | 0 / 7 | `storylines/aranka_continuation.py` |
| `aranka.the_story_that_follows` | aranka | registered | 0 / 11 | `storylines/aranka_continuation.py` |
| `aranka.the_next_verse` | aranka | registered | 0 / 10 | `storylines/aranka_continuation.py` |
| `aranka.the_song_and_the_road` | aranka | registered | 0 / 2 | `storylines/aranka_continuation.py` |
| `aranka.the_deferred_answer` | aranka | registered | 0 / 3 | `storylines/aranka_continuation.py` |
| `konomi.the_names_admitted` | konomi | registered | 10 / 10 | `storylines/konomi_political_consequence.py` |
| `konomi.the_answer_on_record` | konomi | registered | 12 / 12 | `storylines/konomi_political_consequence.py` |
| `soana.when_the_road_returns` | soana | registered | 0 / 10 | `storylines/soana_late_campaign.py` |
| `soana.a_track_with_two_ends` | soana | registered | 0 / 7 | `storylines/soana_late_campaign.py` |
| `soana.what_the_hollow_costs` | soana | registered | 0 / 6 | `storylines/soana_late_campaign.py` |
| `soana.where_the_steps_end` | soana | registered | 0 / 8 | `storylines/soana_late_campaign.py` |
| `soana.the_days_she_counted` | soana | registered | 0 / 13 | `storylines/soana_late_campaign.py` |
| `soana.before_the_far_road` | soana | registered | 0 / 9 | `storylines/soana_late_campaign.py` |
| `soana.ending_kept_life` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_chosen_visits` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_familiar_company` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_sacrifice` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_beyond_the_forest` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_unrecognizable_return` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_native_loss` | soana | registered | 0 / 4 | `storylines/soana_late_campaign.py` |
| `soana.ending_aeon` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_unfinished_sacrifice` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_unfinished_ascent` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_unfinished_change` | soana | registered | 0 / 1 | `storylines/soana_late_campaign.py` |
| `soana.ending_unfinished_loss` | soana | registered | 0 / 4 | `storylines/soana_late_campaign.py` |
| `anevia.unborrowed_hour` | anevia | registered | 13 / 13 | `storylines/anevia_independent.py` |
| `anevia.a_question_at_home` | anevia | registered | 12 / 12 | `storylines/anevia_independent.py` |
| `anevia.one_truth` | anevia | registered | 5 / 5 | `storylines/anevia_independent.py` |
| `anevia.beths_question` | anevia | registered | 12 / 12 | `storylines/anevia_independent.py` |
| `anevia.beths_answer` | anevia | registered | 7 / 7 | `storylines/anevia_independent.py` |
| `anevia.her_own_answer` | anevia | registered | 9 / 9 | `storylines/anevia_independent.py` |
| `anevia.a_place_of_our_own` | anevia | registered | 6 / 6 | `storylines/anevia_independent.py` |
| `anevia.an_invitation_afterward` | anevia | registered | 6 / 6 | `storylines/anevia_independent.py` |
| `anevia.borrowed_signature` | anevia | registered | 8 / 8 | `storylines/anevia_independent.py` |
| `anevia.the_paper_seller` | anevia | registered | 9 / 9 | `storylines/anevia_independent.py` |
| `anevia.the_woman_with_the_basket` | anevia | registered | 8 / 8 | `storylines/anevia_independent.py` |
| `anevia.the_counting_room` | anevia | registered | 7 / 7 | `storylines/anevia_independent.py` |
| `anevia.what_the_warning_cost` | anevia | registered | 10 / 10 | `storylines/anevia_independent.py` |
| `anevia.the_evening_without_a_case` | anevia | registered | 11 / 11 | `storylines/anevia_independent.py` |
| `anevia.departure_note` | anevia | registered | 4 / 4 | `storylines/anevia_independent.py` |
| `anevia.the_blank_half` | anevia | registered | 4 / 4 | `storylines/anevia_independent.py` |
| `anevia.the_life_she_lived` | anevia | registered | 8 / 8 | `storylines/anevia_independent.py` |
| `anevia.a_key_that_is_hers` | anevia | registered | 10 / 10 | `storylines/anevia_independent.py` |
| `anevia.the_last_ordinary_thing` | anevia | registered | 4 / 4 | `storylines/anevia_independent.py` |
| `anevia.a_grief_with_a_name` | anevia | registered | 8 / 8 | `storylines/anevia_independent.py` |
| `anevia.ending_kept` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_open` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_unfinished` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_promised` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_parted` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_survivor` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_grief_unanswered` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_wife_absent` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_wife_killed` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_death` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_gone` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_sacrifice` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_changed_power` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_ascended` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `anevia.ending_aeon` | anevia | registered | 1 / 1 | `storylines/anevia_independent.py` |
| `irabeth.a_name_on_the_list` | irabeth | registered | 11 / 11 | `storylines/irabeth_independent.py` |
| `irabeth.the_seized_wagon` | irabeth | registered | 10 / 10 | `storylines/irabeth_independent.py` |
| `irabeth.the_question_outside_duty` | irabeth | registered | 10 / 10 | `storylines/irabeth_independent.py` |
| `irabeth.one_truth_to_tell` | irabeth | registered | 5 / 5 | `storylines/irabeth_independent.py` |
| `irabeth.anevias_answer` | irabeth | registered | 11 / 11 | `storylines/irabeth_independent.py` |
| `irabeth.the_evening_she_chose` | irabeth | registered | 10 / 10 | `storylines/irabeth_independent.py` |
| `irabeth.a_day_of_our_own` | irabeth | registered | 8 / 8 | `storylines/irabeth_independent.py` |
| `irabeth.the_sealed_account` | irabeth | registered | 10 / 10 | `storylines/irabeth_independent.py` |
| `irabeth.ten_minutes_in_a_hall` | irabeth | registered | 11 / 11 | `storylines/irabeth_independent.py` |
| `irabeth.the_cost_afterward` | irabeth | registered | 9 / 9 | `storylines/irabeth_independent.py` |
| `irabeth.without_an_account` | irabeth | registered | 12 / 12 | `storylines/irabeth_independent.py` |
| `irabeth.after_the_shared_answer` | irabeth | registered | 4 / 4 | `storylines/irabeth_independent.py` |
| `irabeth.before_the_unmapped_road` | irabeth | registered | 8 / 8 | `storylines/irabeth_independent.py` |
| `irabeth.an_unposted_line` | irabeth | registered | 4 / 4 | `storylines/irabeth_independent.py` |
| `irabeth.the_person_who_returns` | irabeth | registered | 11 / 11 | `storylines/irabeth_independent.py` |
| `irabeth.when_the_instruction_is_used` | irabeth | registered | 10 / 10 | `storylines/irabeth_independent.py` |
| `irabeth.a_road_she_would_choose` | irabeth | registered | 12 / 12 | `storylines/irabeth_independent.py` |
| `irabeth.the_hour_before_battle` | irabeth | registered | 15 / 15 | `storylines/irabeth_independent.py` |
| `irabeth.ending_lasting` | irabeth | registered | 5 / 5 | `storylines/irabeth_independent.py` |
| `irabeth.ending_open` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_friends` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_unfinished` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_loss` | irabeth | registered | 3 / 3 | `storylines/irabeth_independent.py` |
| `irabeth.ending_changed` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_ascent` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_sacrifice` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.ending_aeon` | irabeth | registered | 1 / 1 | `storylines/irabeth_independent.py` |
| `irabeth.after_the_answer_was_lost` | irabeth | registered | 4 / 4 | `storylines/irabeth_independent.py` |
| `tirabade.negotiated_table` | tirabade | registered | 9 / 9 | `storylines/tirabade_independent_bridge.py` |
| `tirabade.after_local_parting` | tirabade | registered | 6 / 6 | `storylines/tirabade_independent_bridge.py` |
| `tirabade.negotiated_letter` | tirabade | registered | 4 / 4 | `storylines/tirabade_independent_bridge.py` |
| `tirabade.negotiated_ending_together` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `tirabade.negotiated_ending_apart` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `tirabade.negotiated_ending_unfinished` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `tirabade.negotiated_ending_loss` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `tirabade.negotiated_ending_monster` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `tirabade.negotiated_ending_aeon` | tirabade | registered | 1 / 1 | `story.py or export integration; exact origin not yet resolved` |
| `irabeth.return_request` | irabeth | registered | 6 / 6 | `storylines/irabeth_return_invitation.py` |
| `irabeth.return_reply` | irabeth | registered | 6 / 6 | `storylines/irabeth_return_invitation.py` |
| `irabeth.return_first_words` | irabeth | registered | 8 / 8 | `storylines/irabeth_return_invitation.py` |
| `arsinoe_after_rain` | arsinoe | registered | 0 / 8 | `storylines/arsinoe_campaign.py` |
| `arsinoe_two_doors` | arsinoe | registered | 0 / 8 | `storylines/arsinoe_campaign.py` |
| `arsinoe_a_stone_in_hand` | arsinoe | registered | 0 / 7 | `storylines/arsinoe_campaign.py` |
| `arsinoe_the_first_cart` | arsinoe | registered | 0 / 9 | `storylines/arsinoe_campaign.py` |
| `arsinoe_what_she_asks` | arsinoe | registered | 0 / 12 | `storylines/arsinoe_campaign.py` |
| `arsinoe_before_the_road` | arsinoe | registered | 0 / 5 | `storylines/arsinoe_campaign.py` |
| `arsinoe_where_she_stays` | arsinoe | registered | 0 / 6 | `storylines/arsinoe_campaign.py` |
| `arsinoe_the_window_opens` | arsinoe | registered | 0 / 5 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_kept` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_open` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_unfinished` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_promised` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_friend_waiting` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_slow_waiting` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_friend` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_slow` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_parted` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_sacrifice` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_ascended` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_changed` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_swarm` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `arsinoe_ending_aeon` | arsinoe | registered | 0 / 1 | `storylines/arsinoe_campaign.py` |
| `gesmerha.a_story_from_elsewhere` | gesmerha | registered | 0 / 6 | `storylines/gesmerha_campaign.py` |
| `gesmerha.the_unfinished_verse` | gesmerha | registered | 0 / 7 | `storylines/gesmerha_campaign.py` |
| `gesmerha.the_evening_answer` | gesmerha | registered | 0 / 7 | `storylines/gesmerha_campaign.py` |
| `gesmerha.what_she_asks` | gesmerha | registered | 0 / 11 | `storylines/gesmerha_campaign.py` |
| `gesmerha.the_voice_at_court` | gesmerha | registered | 0 / 14 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_living_reunion` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_unmet_again` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_loss` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_changed` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_demon` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_devil` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_ascent` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_sacrifice` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.ending_aeon` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_campaign.py` |
| `gesmerha.the_things_still_here` | gesmerha | registered | 0 / 9 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.the_box_with_two_names` | gesmerha | registered | 0 / 8 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.the_long_way_with_company` | gesmerha | registered | 0 / 8 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.a_lesson_without_her` | gesmerha | registered | 0 / 9 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.the_room_she_chose` | gesmerha | registered | 0 / 8 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.the_work_left_finished` | gesmerha | registered | 0 / 10 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_lovers` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_friends` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_open` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_closed` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_loss` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_changed` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_demon` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_devil` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_ascent` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_sacrifice` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_aeon` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `gesmerha.late_ending_unfinished` | gesmerha | registered | 0 / 1 | `storylines/gesmerha_late_campaign.py` |
| `ember.something_you_cannot_do` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.a_late_afternoon` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.the_empty_basket` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.the_cold_side` | ember | registered | 0 / 8 | `storylines/ember_campaign.py` |
| `ember.the_missing_covering` | ember | registered | 0 / 7 | `storylines/ember_campaign.py` |
| `ember.a_question_at_the_yard` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.what_did_not_mend` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.the_person_in_the_title` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.the_words_people_keep` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.a_letter_with_no_road` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.an_answer_from_elsewhere` | ember | registered | 0 / 8 | `storylines/ember_campaign.py` |
| `ember.where_she_is_needed` | ember | registered | 0 / 6 | `storylines/ember_campaign.py` |
| `ember.the_afternoon_not_promised` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.a_place_to_sit` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.the_small_choice` | ember | registered | 0 / 5 | `storylines/ember_campaign.py` |
| `ember.the_visits_she_can_end` | ember | registered | 0 / 4 | `storylines/ember_campaign.py` |
| `ember.ending_good_friend` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_law_friend` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_friend` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_unfinished` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_care` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_care_unfinished` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_departed` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_absent` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_dead` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_sacrifice` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_ascended` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `ember.ending_aeon` | ember | registered | 0 / 1 | `storylines/ember_campaign.py` |
| `konomi.the_unintroduced_letter` | konomi | registered | 8 / 8 | `storylines/konomi_missed_contact.py` |
| `konomi.the_answer_she_addressed` | konomi | registered | 4 / 4 | `storylines/konomi_missed_contact.py` |
| `konomi.the_courtyard_introduction` | konomi | registered | 9 / 9 | `storylines/konomi_missed_contact.py` |
| `konomi.ending_missed_declined` | konomi | registered | 1 / 1 | `storylines/konomi_missed_contact.py` |
| `konomi.ending_missed_interrupted` | konomi | registered | 8 / 8 | `storylines/konomi_missed_contact.py` |
| `konomi.ending_missed_interrupted_aeon` | konomi | registered | 1 / 1 | `storylines/konomi_missed_contact.py` |
| `minachiv.two_answers` | minagho_chivarro | registered | 7 / 7 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.her_own_arrival` | minagho_chivarro | registered | 6 / 6 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_remaining_customers` | minagho_chivarro | registered | 4 / 4 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_second_address` | minagho_chivarro | registered | 7 / 7 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.a_factor_at_the_table` | minagho_chivarro | registered | 8 / 8 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.what_the_offer_bought` | minagho_chivarro | registered | 8 / 8 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_unhired_evening` | minagho_chivarro | registered | 15 / 15 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_answer_after_business` | minagho_chivarro | registered | 9 / 9 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.minaghos_unfinished_sentence` | minagho_chivarro | registered | 12 / 12 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_performer_and_the_key` | minagho_chivarro | registered | 8 / 8 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_key_in_your_hand` | minagho_chivarro | registered | 10 / 10 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.a_room_she_likes` | minagho_chivarro | registered | 10 / 10 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_price_of_her_name` | minagho_chivarro | registered | 11 / 11 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_paper_she_kept` | minagho_chivarro | registered | 6 / 6 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_man_who_remembers` | minagho_chivarro | registered | 7 / 7 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_first_small_audience` | minagho_chivarro | registered | 8 / 8 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_entrance_she_wants` | minagho_chivarro | registered | 8 / 8 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.who_keeps_the_house` | minagho_chivarro | registered | 6 / 6 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.when_the_door_opens` | minagho_chivarro | registered | 10 / 10 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.after_the_last_lamp` | minagho_chivarro | registered | 9 / 9 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.the_cost_in_daylight` | minagho_chivarro | registered | 9 / 9 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.what_she_will_take` | minagho_chivarro | registered | 9 / 9 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.before_the_last_road` | minagho_chivarro | registered | 7 / 7 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_together` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_two` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_minagho` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_chivarro` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_open` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_friends` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_chivarro_service` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_service` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_both_lost` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_minagho_lost` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_chivarro_lost` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_changed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_ascent` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_sacrifice` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_unfinished_lasting` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_unfinished` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_aeon` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_both_lost_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_minagho_lost_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_chivarro_lost_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_changed_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_ascent_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_sacrifice_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `minachiv.ending_aeon_completed` | minagho_chivarro | registered | 1 / 1 | `storylines/minagho_chivarro_continuation.py` |
| `noct.unlit_quay` | nocticula | registered | 1 / 5 | `storylines/nocticula_continuation.py` |
| `noct.sixth_passenger` | nocticula | registered | 0 / 6 | `storylines/nocticula_continuation.py` |
| `noct.lamp_measure` | nocticula | registered | 0 / 6 | `storylines/nocticula_continuation.py` |
| `noct.captains_reply` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.her_own_face` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.white_shoes` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.demonstration` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.voices_in_glass` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.cost_of_return` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.return_count` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.after_the_lamps` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.another_place` | nocticula | registered | 0 / 11 | `storylines/nocticula_continuation.py` |
| `noct.hearing` | nocticula | registered | 0 / 10 | `storylines/nocticula_continuation.py` |
| `noct.last_buyer` | nocticula | registered | 0 / 9 | `storylines/nocticula_continuation.py` |
| `noct.empty_chair` | nocticula | registered | 0 / 6 | `storylines/nocticula_continuation.py` |
| `noct.mask_and_bell` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.uninvited_guest` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.closed_gallery` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.unborrowed_evening` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.bell_without_master` | nocticula | registered | 0 / 8 | `storylines/nocticula_continuation.py` |
| `noct.counterseal` | nocticula | registered | 0 / 7 | `storylines/nocticula_continuation.py` |
| `noct.no_applause` | nocticula | registered | 0 / 11 | `storylines/nocticula_continuation.py` |
| `noct.what_she_keeps` | nocticula | registered | 0 / 17 | `storylines/nocticula_continuation.py` |
| `noct.second_door` | nocticula | registered | 0 / 10 | `storylines/nocticula_continuation.py` |
| `noct.ending_company` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_alliance` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_limit` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_death` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_sacrifice` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_ascent` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_changed` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.ending_aeon` | nocticula | registered | 0 / 1 | `storylines/nocticula_continuation.py` |
| `noct.unlit_quay.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.unlit_quay.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.unlit_quay.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.sixth_passenger.acquired.new` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.sixth_passenger.acquired.refused` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.sixth_passenger.acquired.prior` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.lamp_measure.acquired.new` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.lamp_measure.acquired.refused` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.lamp_measure.acquired.prior` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.captains_reply.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.captains_reply.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.captains_reply.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.new.absent` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.new.original` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.new.renewed` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.refused.absent` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.refused.original` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.refused.renewed` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.prior.absent` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.prior.original` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.her_own_face.acquired.prior.renewed` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.white_shoes.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.white_shoes.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.white_shoes.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.demonstration.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.demonstration.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.demonstration.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.voices_in_glass.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.voices_in_glass.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.voices_in_glass.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.cost_of_return.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.cost_of_return.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.cost_of_return.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.return_count.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.return_count.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.return_count.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.after_the_lamps.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.after_the_lamps.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.after_the_lamps.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.another_place.acquired.new` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.another_place.acquired.refused` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.another_place.acquired.prior` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.hearing.acquired.new` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.hearing.acquired.refused` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.hearing.acquired.prior` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.last_buyer.acquired.new` | nocticula | registered | 0 / 9 | `storylines/nocticula_acquired_harbor.py` |
| `noct.last_buyer.acquired.refused` | nocticula | registered | 0 / 9 | `storylines/nocticula_acquired_harbor.py` |
| `noct.last_buyer.acquired.prior` | nocticula | registered | 0 / 9 | `storylines/nocticula_acquired_harbor.py` |
| `noct.empty_chair.acquired.new` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.empty_chair.acquired.refused` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.empty_chair.acquired.prior` | nocticula | registered | 0 / 6 | `storylines/nocticula_acquired_harbor.py` |
| `noct.mask_and_bell.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.mask_and_bell.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.mask_and_bell.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.uninvited_guest.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.uninvited_guest.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.uninvited_guest.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.closed_gallery.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.closed_gallery.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.closed_gallery.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.unborrowed_evening.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.unborrowed_evening.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.unborrowed_evening.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.bell_without_master.acquired.new` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.bell_without_master.acquired.refused` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.bell_without_master.acquired.prior` | nocticula | registered | 0 / 8 | `storylines/nocticula_acquired_harbor.py` |
| `noct.counterseal.acquired.new` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.counterseal.acquired.refused` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.counterseal.acquired.prior` | nocticula | registered | 0 / 7 | `storylines/nocticula_acquired_harbor.py` |
| `noct.no_applause.acquired.new` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.no_applause.acquired.refused` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.no_applause.acquired.prior` | nocticula | registered | 0 / 11 | `storylines/nocticula_acquired_harbor.py` |
| `noct.what_she_keeps.acquired.new` | nocticula | registered | 0 / 17 | `storylines/nocticula_acquired_harbor.py` |
| `noct.what_she_keeps.acquired.refused` | nocticula | registered | 0 / 17 | `storylines/nocticula_acquired_harbor.py` |
| `noct.what_she_keeps.acquired.prior` | nocticula | registered | 0 / 17 | `storylines/nocticula_acquired_harbor.py` |
| `noct.second_door.acquired.new` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.second_door.acquired.refused` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.second_door.acquired.prior` | nocticula | registered | 0 / 10 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_company.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_company.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_company.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_alliance.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_alliance.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_alliance.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_limit.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_limit.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_limit.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_death.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_death.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_death.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_sacrifice.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_sacrifice.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_sacrifice.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_ascent.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_ascent.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_ascent.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_changed.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_changed.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_changed.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_aeon.acquired.new` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_aeon.acquired.refused` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.ending_aeon.acquired.prior` | nocticula | registered | 0 / 1 | `storylines/nocticula_acquired_harbor.py` |
| `noct.acq.audience_missed` | nocticula.acquisition | registered | 1 / 6 | `storylines/nocticula_trickster_acquisition.py` |
| `noct.acq.audience_rejected` | nocticula.acquisition | registered | 0 / 6 | `storylines/nocticula_trickster_acquisition.py` |
| `noct.acq.audience_patronage` | nocticula.acquisition | registered | 0 / 6 | `storylines/nocticula_trickster_acquisition.py` |
| `noct.acq.the_missing_line` | nocticula.acquisition | registered | 0 / 5 | `storylines/nocticula_trickster_acquisition.py` |
| `noct.acq.her_hand` | nocticula.acquisition | registered | 0 / 12 | `storylines/nocticula_trickster_acquisition.py` |
| `noct.acq.borrowed_signature` | nocticula.acquisition | registered | 0 / 9 | `storylines/nocticula_trickster_concession.py` |
| `noct.acq.the_paid_address` | nocticula.acquisition | registered | 0 / 8 | `storylines/nocticula_trickster_concession.py` |
| `noct.acq.the_retained_copy` | nocticula.acquisition | registered | 0 / 11 | `storylines/nocticula_trickster_concession.py` |
| `noct.acq.an_answer_of_her_own` | nocticula.acquisition | registered | 0 / 7 | `storylines/nocticula_trickster_concession.py` |
| `noct.join.an_unfinished_map` | nocticula.acquisition | registered | 0 / 13 | `storylines/nocticula_trickster_harbor_join.py` |
| `noct.join.the_room_she_makes` | nocticula.acquisition | registered | 0 / 6 | `storylines/nocticula_trickster_harbor_join.py` |
| `noct.join.a_chosen_shore` | nocticula.acquisition | registered | 0 / 9 | `storylines/nocticula_trickster_harbor_join.py` |
| `nurah.borrowed_name` | nurah | registered | 1 / 6 | `storylines/nurah_continuation.py` |
| `nurah.invitation_reply` | nurah | registered | 0 / 8 | `storylines/nurah_continuation.py` |
| `nurah.the_author_arrives` | nurah | registered | 0 / 8 | `storylines/nurah_continuation.py` |
| `nurah.a_page_with_teeth` | nurah | registered | 0 / 8 | `storylines/nurah_continuation.py` |
| `nurah.the_borrowed_audience` | nurah | registered | 0 / 11 | `storylines/nurah_continuation.py` |
| `nurah.the_editor_opens` | nurah | registered | 0 / 10 | `storylines/nurah_continuation.py` |
| `nurah.the_case_goes_missing` | nurah | registered | 0 / 13 | `storylines/nurah_continuation.py` |
| `nurah.the_letter_she_wrote` | nurah | registered | 0 / 9 | `storylines/nurah_continuation.py` |
| `nurah.the_price_of_a_warning` | nurah | registered | 0 / 9 | `storylines/nurah_continuation.py` |
| `nurah.the_subscribers_evening` | nurah | registered | 0 / 16 | `storylines/nurah_continuation.py` |
| `nurah.the_unpurchased_sentence` | nurah | registered | 0 / 25 | `storylines/nurah_continuation.py` |
| `nurah.the_copies_that_survive` | nurah | registered | 0 / 15 | `storylines/nurah_continuation.py` |
| `nurah.a_margin_for_you` | nurah | registered | 0 / 9 | `storylines/nurah_continuation.py` |
| `areelu.trickster_opening.the_original` | areelu | draft_only | 1 / 7 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_test` | areelu | draft_only | 0 / 9 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_second_problem` | areelu | draft_only | 0 / 7 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu.trickster_opening.the_live_fold` | areelu | draft_only | 0 / 14 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_inventory` | areelu | draft_only | 0 / 6 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_reply` | areelu | draft_only | 0 / 13 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_second_graft` | areelu | draft_only | 0 / 7 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_hour` | areelu | draft_only | 0 / 7 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_hour.followup.private_close` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_open_record` | areelu | draft_only | 0 / 10 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_returned_names` | areelu | draft_only | 0 / 16 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_returned_names.followup.returned_after_walk` | areelu | draft_only | 0 / 4 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_returned_names.followup.returned_future` | areelu | draft_only | 0 / 7 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_returned_names.followup.returned_long_term` | areelu | draft_only | 0 / 2 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy` | areelu | draft_only | 0 / 15 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy.followup.copy_followup` | areelu | draft_only | 0 / 5 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy.followup.copy_revisit` | areelu | draft_only | 0 / 5 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy.followup.copy_second_review` | areelu | draft_only | 0 / 3 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy.followup.copy_long_term` | areelu | draft_only | 0 / 2 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_private_copy.followup.copy_pause_notice` | areelu | draft_only | 0 / 3 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_residual_gate` | areelu | draft_only | 0 / 25 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_residual_gate.followup.gate_result_followup` | areelu | draft_only | 0 / 4 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_residual_gate.followup.gate_reinspection` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_residual_gate.followup.gate_archive_followup` | areelu | draft_only | 0 / 4 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_residual_gate.followup.gate_residents_revisit` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_unmeasured_answer` | areelu | draft_only | 0 / 8 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_unmeasured_answer.followup.unmeasured_morning` | areelu | draft_only | 0 / 2 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after` | areelu | draft_only | 0 / 22 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after.followup.choice_month_later` | areelu | draft_only | 0 / 3 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after.followup.choice_year` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after.followup.choice_shared_future` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after.followup.choice_year_end` | areelu | draft_only | 0 / 6 | `storylines/areelu_trickster_rivalry_opening.py` |
| `areelu_trickster_opening.the_choice_after.followup.choice_ordinary_future` | areelu | draft_only | 0 / 1 | `storylines/areelu_trickster_rivalry_opening.py` |
| `devarra.trickster.first_answer` | devarra.trickster | draft_only | 1 / 23 | `storylines/devarra_trickster_opening.py` |
| `devarra.trickster.saved_brood` | devarra.trickster | draft_only | 0 / 23 | `storylines/devarra_trickster_opening.py` |
| `devarra.trickster.lost_clutch` | devarra.trickster | draft_only | 0 / 23 | `storylines/devarra_trickster_opening.py` |
| `devarra.trickster.evidence_and_terms` | devarra.trickster | draft_only | 0 / 48 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_echoing_slate` | devarra.trickster | draft_only | 0 / 18 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_table_without_witnesses` | devarra.trickster | draft_only | 0 / 16 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_second_envelope` | devarra | draft_only | 1 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_hour_under_the_bridge` | devarra | draft_only | 0 / 17 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_dragon_out_of_place` | devarra | draft_only | 0 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_empty_cage` | devarra.trickster | draft_only | 0 / 24 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_door_that_owed_a_debt` | devarra | draft_only | 0 / 22 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_room_of_her_choosing` | devarra | draft_only | 0 / 13 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_house_above_the_road` | devarra | draft_only | 0 / 5 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_owned_the_rain` | devarra | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_weight_of_the_wall` | devarra | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_roof_is_not_a_rein` | devarra | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.what_she_comes_back_for` | devarra | draft_only | 0 / 15 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.an_evening_without_an_alibi` | devarra | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_buyer_at_the_western_gate` | devarra | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_door_without_permission` | devarra | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_address` | devarra | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_sold_her_shadow` | devarra | draft_only | 0 / 8 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_she_names` | devarra | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_place_above_the_road` | devarra | draft_only | 0 / 11 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_last_kiln_approach` | devarra | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.evidence_and_terms.saved_brood` | devarra.trickster | draft_only | 0 / 48 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.evidence_and_terms.lost_clutch` | devarra.trickster | draft_only | 0 / 48 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_echoing_slate.saved_brood` | devarra.trickster | draft_only | 0 / 18 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_echoing_slate.lost_clutch` | devarra.trickster | draft_only | 0 / 18 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_table_without_witnesses.saved_brood` | devarra.trickster | draft_only | 0 / 16 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_table_without_witnesses.lost_clutch` | devarra.trickster | draft_only | 0 / 16 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_second_envelope.saved_brood` | devarra.trickster | draft_only | 0 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_second_envelope.lost_clutch` | devarra.trickster | draft_only | 0 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_hour_under_the_bridge.saved_brood` | devarra.trickster | draft_only | 0 / 17 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_hour_under_the_bridge.lost_clutch` | devarra.trickster | draft_only | 0 / 17 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_dragon_out_of_place.saved_brood` | devarra.trickster | draft_only | 0 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_dragon_out_of_place.lost_clutch` | devarra.trickster | draft_only | 0 / 21 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_empty_cage.saved_brood` | devarra.trickster | draft_only | 0 / 24 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_empty_cage.lost_clutch` | devarra.trickster | draft_only | 0 / 24 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_last_kiln_approach.saved_brood` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_last_kiln_approach.lost_clutch` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_door_that_owed_a_debt.saved_brood` | devarra.trickster | draft_only | 0 / 22 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_door_that_owed_a_debt.lost_clutch` | devarra.trickster | draft_only | 0 / 22 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_room_of_her_choosing.saved_brood` | devarra.trickster | draft_only | 0 / 13 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_room_of_her_choosing.lost_clutch` | devarra.trickster | draft_only | 0 / 13 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_house_above_the_road.saved_brood` | devarra.trickster | draft_only | 0 / 5 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_house_above_the_road.lost_clutch` | devarra.trickster | draft_only | 0 / 5 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_owned_the_rain.saved_brood` | devarra.trickster | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_owned_the_rain.lost_clutch` | devarra.trickster | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_weight_of_the_wall.saved_brood` | devarra.trickster | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_weight_of_the_wall.lost_clutch` | devarra.trickster | draft_only | 0 / 6 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_roof_is_not_a_rein.saved_brood` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_roof_is_not_a_rein.lost_clutch` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.what_she_comes_back_for.saved_brood` | devarra.trickster | draft_only | 0 / 15 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.what_she_comes_back_for.lost_clutch` | devarra.trickster | draft_only | 0 / 15 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.an_evening_without_an_alibi.saved_brood` | devarra.trickster | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.an_evening_without_an_alibi.lost_clutch` | devarra.trickster | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_buyer_at_the_western_gate.saved_brood` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_buyer_at_the_western_gate.lost_clutch` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_door_without_permission.saved_brood` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_door_without_permission.lost_clutch` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_address.saved_brood` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_of_an_address.lost_clutch` | devarra.trickster | draft_only | 0 / 9 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_sold_her_shadow.saved_brood` | devarra.trickster | draft_only | 0 / 8 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_man_who_sold_her_shadow.lost_clutch` | devarra.trickster | draft_only | 0 / 8 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_she_names.saved_brood` | devarra.trickster | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.the_price_she_names.lost_clutch` | devarra.trickster | draft_only | 0 / 7 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_place_above_the_road.saved_brood` | devarra.trickster | draft_only | 0 / 11 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.a_place_above_the_road.lost_clutch` | devarra.trickster | draft_only | 0 / 11 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.recollection_partnership.saved_brood` | devarra.trickster | draft_only | 0 / 1 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.recollection_partnership.lost_clutch` | devarra.trickster | draft_only | 0 / 1 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.recollection_visits.saved_brood` | devarra.trickster | draft_only | 0 / 1 | `storylines/devarra_trickster_progression.py` |
| `devarra.trickster.recollection_visits.lost_clutch` | devarra.trickster | draft_only | 0 / 1 | `storylines/devarra_trickster_progression.py` |
| `eliandra.trickster.first_private_audience` | eliandra.trickster | draft_only | 1 / 35 | `storylines/eliandra_trickster_opening.py` |
| `galfrey.angel.the_space_between_orders` | galfrey | draft_only | 1 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.azata.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.aeon.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.trickster.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.demon.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.devil.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.dragon.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `galfrey.legend.the_space_between_orders` | galfrey | draft_only | 0 / 4 | `storylines/galfrey_all_path_continuation.py` |
| `jannah.trickster.the_misdelivered_hour` | jannah.trickster | draft_only | 1 / 9 | `storylines/jannah_trickster_opening.py` |
| `jannah.trickster.the_practice_yard` | jannah.trickster | draft_only | 0 / 16 | `storylines/jannah_trickster_opening.py` |
| `jannah.trickster.the_hour_after` | jannah.trickster | draft_only | 0 / 12 | `storylines/jannah_trickster_opening.py` |
| `jannah.trickster.the_line_on_the_order` | jannah.trickster | draft_only | 0 / 10 | `storylines/jannah_trickster_opening.py` |
| `jannah.trickster.the_question_in_the_yard` | jannah.trickster | draft_only | 0 / 16 | `storylines/jannah_trickster_opening.py` |
| `kiana.roof_supper` | kiana | draft_only | 0 / 12 | `storylines/kiana_consequences.py` |
| `mielarah.opening.the_invitation` | mielarah.opening | draft_only | 1 / 16 | `storylines/mielarah_route_opening.py` |
| `mielarah.trickster.ishiar_intervention` | mielarah.opening | draft_only | 0 / 14 | `storylines/mielarah_route_opening.py` |
| `mielarah.trickster.colyphyr_arrival` | mielarah.opening | draft_only | 0 / 5 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.followup_contact` | mielarah.opening | draft_only | 0 / 3 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_case` | mielarah.opening | draft_only | 0 / 11 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_captains_evening` | mielarah.opening | draft_only | 0 / 7 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_crews_answer` | mielarah.opening | draft_only | 0 / 12 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_quay_day` | mielarah.opening | draft_only | 0 / 9 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_repair_ledger` | mielarah.opening | draft_only | 0 / 7 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_sail_trial` | mielarah.opening | draft_only | 0 / 10 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_weather_watch` | mielarah.opening | draft_only | 0 / 16 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_departure_notice` | mielarah.opening | draft_only | 0 / 13 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_outer_shoals` | mielarah.opening | draft_only | 0 / 12 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_outer_shoals_friendship` | mielarah.opening | draft_only | 0 / 4 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_week_on_shore` | mielarah.opening | draft_only | 0 / 14 | `storylines/mielarah_route_opening.py` |
| `mielarah.opening.the_new_sail` | mielarah.opening | draft_only | 0 / 15 | `storylines/mielarah_route_opening.py` |
| `noct.acq.after_the_council` | nocticula.acquisition | draft_only | 0 / 2 | `storylines/nocticula_trickster_acquisition.py` |
| `targona.trickster_acq.the_second_letter` | targona.trickster_acq | draft_only | 1 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.a_measured_impossibility` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_angel` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_azata` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_aeon` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_demon` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_lich` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_devil` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_legend` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.path_golddragon` | targona.trickster_acq | draft_only | 0 / 8 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_trickster` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_trickster` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_trickster` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_trickster` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_trickster` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_trickster` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_angel` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_angel` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_angel` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_angel` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_angel` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_angel` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_azata` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_azata` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_azata` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_azata` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_azata` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_azata` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_aeon` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_aeon` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_aeon` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_aeon` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_aeon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_aeon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_demon` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_demon` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_demon` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_demon` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_demon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_demon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_lich` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_lich` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_lich` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_lich` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_lich` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_lich` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_devil` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_devil` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_devil` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_devil` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_devil` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_devil` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_legend` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_legend` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_legend` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_legend` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_legend` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_legend` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.meeting_golddragon` | targona.trickster_acq | draft_only | 0 / 9 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.spar_golddragon` | targona.trickster_acq | draft_only | 0 / 11 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.intimacy_golddragon` | targona.trickster_acq | draft_only | 0 / 14 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.ending_golddragon` | targona.trickster_acq | draft_only | 0 / 5 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.future_golddragon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `targona.trickster_acq.followup_golddragon` | targona.trickster_acq | draft_only | 0 / 7 | `storylines/targona_trickster_acquisition.py` |
| `terendelev.continuation.returned_letter` | terendelev | draft_only | 1 / 8 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.kenabres_petition` | terendelev | draft_only | 0 / 15 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.private_oath` | terendelev | draft_only | 0 / 5 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.inspection_day` | terendelev | draft_only | 0 / 5 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.windward_evening` | terendelev | draft_only | 0 / 8 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.kenabres_vigil` | terendelev | draft_only | 0 / 5 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.private_aftercare` | terendelev | draft_only | 0 / 5 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.scale_invitation` | terendelev | draft_only | 0 / 10 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.escape_boundary` | terendelev | draft_only | 0 / 6 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_friendship` | terendelev | draft_only | 0 / 4 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_native_lead` | terendelev | draft_only | 0 / 3 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_identity_review` | terendelev | draft_only | 0 / 4 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_other_half_living` | terendelev | draft_only | 0 / 3 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_other_half_dead` | terendelev | draft_only | 0 / 4 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.trickster_new_courtship` | terendelev | draft_only | 0 / 4 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.escape_choice` | terendelev | draft_only | 0 / 4 | `storylines/terendelev_continuation.py` |
| `terendelev.continuation.scale_evening` | terendelev | draft_only | 0 / 5 | `storylines/terendelev_continuation.py` |
| `wenduag.vellexia_network.reception` | wenduag.vellexia_network | draft_only | 1 / 11 | `storylines/wenduag_relationship_network.py` |
| `yaniel.opening.the_letter` | yaniel.opening | draft_only | 1 / 17 | `storylines/yaniel_route_opening.py`, `storylines/yaniel_supper_progression.py` |
| `yaniel.departure.before_abyss` | yaniel.opening | draft_only | 0 / 24 | `storylines/yaniel_supper_progression.py` |

## Next reading batches

1. Finish the remaining physical meeting pages in every family already sampled, especially first arrival versus projection or letter.
2. Read earned private evenings, chosen intimacy and non-intimate alternatives, then conflict/rescue/form changes.
3. Read every remaining node and source variant, deduplicating only proven identical content while preserving distinct incoming history.
4. Review every ending as selected recollection rather than generating unearned future events.
5. Map native/RanRomance routes for characters without local scene objects and add source provenance before calling the 43-character scope exhaustive.

This backlog is deliberately not labeled finished CG assessment.
Only art/scene-cg-coverage.md and art/scene-cg-coverage.json are owned and changed by this task.

## Continued full-scene reading: first Minagho and Chivarro sequence

Adult romance appearances must now target 25-35 and never appear older than 35, while preserving lore age separately.
Attractive humanization and authored hair are permitted design choices, not retroactive native facts or automatic image passes.
Ember and Aivu remain age-appropriate friendship characters.

### minachiv.her_own_arrival

All current exported node text and offered choices read.
Reunion kiss and cup caretaking earn CGs; optional interest branch closeness must not cover company-only outcome.
Setting: Gaming-house room; rain-dark cloak on peg.
Form and wardrobe: Chivarro discards mortal guise after checking room; Minagho native form; no assumed Commander body.

- `start`: Chivarro hand at Minagho neck, mutual laughing reunion kiss; Commander remains offscreen.
- `place`: Minagho turns chipped cup away from Chivarro mouth; intimate care without Commander courtship.
- `interest`: Chosen attraction only: nearer chair, women holding hands, Chivarro free hand near Commander.

### minachiv.the_remaining_customers

All current exported node text and offered choices read.
Reuse established conversation scene; distinct disagreement expression optional, no separate CG for each business reply.
Setting: Gaming-house room, table with letters.
Form and wardrobe: Native forms; indoor clothes not newly specified.

- `stake`: Minagho smile disappears over distance and protection; tension is not resolved automatically.
- `document`: Forwarding impression not decoded yet; do not depict legible solved evidence.

### minachiv.the_second_address

All current exported node text and offered choices read.
Cooperative lamp investigation and selected Trickster paper intervention are distinct earned CG moments.
Setting: Gaming-house room, broad chimney lamp and folding screen.
Form and wardrobe: Native forms; investigative practical posture.

- `start`: Chivarro holds letter beside lamp; Minagho adjusts screen to direct light.
- `read_end`: Successful reading only: Chivarro copies while Commander holds lamp, then touches wrist.
- `blurred`: Failed angle washes out evidence; no readable solved clue.
- `ribbon`: Sealed packet with blue silk; Minagho hand on Chivarro shoulder.
- `trick`: Selected Trickster ability: two pages show wet-looking ink transfer but are dry; no blood effect.

### minachiv.a_factor_at_the_table

All current exported node text and offered choices read.
New factor confrontation merits CG because Minagho form differs from preceding private scene; do not reuse native-form pair.
Setting: Gaming-house room, unblocked second door, table and flat document case.
Form and wardrobe: Minagho explicitly resumes mortal disguise; Chivarro form not newly changed.

- `start`: Mortal Orven opposite Chivarro; disguised Minagho guarding second door; unsigned receipt.
- `ribbon_reply`: Cut blue ribbon half pinned to reply; Chivarro folds retained half into palm.
- `business`: Chivarro strikes out offer and waits; no signed unconditional consent.
- `refuse`: Chivarro tears offer into strips; disappointed ambition, not cheerful surrender.

### minachiv.what_the_offer_bought

All current exported node text and offered choices read.
Branch-specific locations require different CGs; shared start cannot stand for all outcomes.
Setting: Starts gaming house; branch-specific rented meeting room or empty counting room.
Form and wardrobe: Start Minagho travel cloak fastened; do not infer disguise ends after previous factor scene.

- `business`: Chivarro commands two guests attention; Orven unwanted charge; rented private room.
- `business_end`: After guests leave she draws Commander chair close, Minagho brings second cup.
- `bait`: Empty counting room with desk, COLD brazier, three chairs; thin horned agent trapped between two doors, no invented attack.
- `warning`: Torn invitation falls into COLD brazier; women leave shoulders touching.
- `list`: Coded list retained; no burning or slain agent.
- `independent`: Smaller self-funded room, modest steady table, two consenting business guests; not auction of people.
- `independent_end`: Minagho carries two cups, Chivarro laughs unguardedly; cooperative clearing, no automatic kiss.

### minachiv.the_unhired_evening

All current exported node text and offered choices read.
High-priority sequence: mask game, women mutual wrist kiss, selected partner or triad intimacy. Never use kiss CG before selection.
Setting: Private gaming-house room with mask-stone game, cushions, sugared plum.
Form and wardrobe: Indoor native-inspired attire; no automatic undressing; Commander unspecified.

- `start`: Chivarro divides sugared plum, Minagho accepts from fingers then catches hand; game stones on tray.
- `want`: Minagho kisses Chivarro inner wrist; Chivarro holds her chin; established couple intimacy does not imply Commander consent.
- `minagho_kiss`: Only selected Minagho kiss; Chivarro absent for hour; knee bumps table, catches stone. Source continuity query: Chivarro said she was returning tray yet a stone remains. Do not repair prose through image.
- `chivarro_kiss`: Only selected Chivarro kiss; Minagho outside fetching wine until later.
- `together_kiss`: Only selected triad; two women kiss each other and reach back to Commander; Commander identity must remain adaptable.
- `together_close`: Selected no-further-intimacy branch: three seated against cushions, hands loosely held, clothes retained.
- `slow`: Space beside women without pulled embrace; mask game.
- `company`: Women may kiss each other, Commander stays friend; never show Commander kiss.
- `service`: Serious confrontation about coercive service; Chivarro beside Minagho, hands meeting; no seductive compliance.

### minachiv.the_answer_after_business

All current exported node text and offered choices read.
Chivarro independent aftermath may merit one solo CG; branch papers can reuse neutral room while preserving different outcomes.
Setting: Chivarro alone in rented room, stacked letters and EMPTY fireplace.
Form and wardrobe: Chivarro private business clothes; no specific new garment authored.

- `start`: Chivarro throws unwanted fancy advice letter into EMPTY fireplace, not flames.
- `next`: Sivane rehearsal is a proposed letter invitation; performer not physically present.
- `guest`: Chosen company: Chivarro moves chair closer and mimics messenger with amused expression.
- `participant`: She writes and shows offer; autonomous business participation, no forced kiss.


## Continued full-scene reading: rehearsal, independent rooms and reputation

### minachiv.minaghos_unfinished_sentence

All current exported node text and offered choices read.
Quiet solo stair scene is distinct from indoor business, with separately selected hand/kiss.
Setting: Narrow stair outside rented room; rain and broken gutter.
Form and wardrobe: Form not restated; do not invent a new transformation.

- `start`: Chipped cup contains water; seated pause, rain ticking gutter.
- `morning`: Knees drawn nearer to make room; looks at single repaired roof tile, no grand skyline claim.
- `hand`: Selected handholding then asked kiss; no kiss on roof-only branch.
- `roof`: Laughter after passerby carries ladder; Chivarro joins from upper landing only at end.

### minachiv.the_performer_and_the_key

All current exported node text and offered choices read.
New theater establishing CG and Chivarro directing light are valuable; Minagho absent.
Setting: Disused bathhouse, platform across empty shallow basin, gallery, exposed painted-door braces.
Form and wardrobe: Sivane adult succubus in own form, dark traveling coat, folded wings; Chivarro staging clothes unspecified.

- `start`: Chivarro below platform/gallery, Sivane above rail; no functioning bath water.
- `room`: Visible bare reverse and braces of painted door; clear passage after bench moved.
- `delay`: Winter pale mask after silence; not supernatural transformation into actual Winter.
- `comparison`: Sivane mask against hip, pleased despite herself.
- `pleasure`: Chivarro chalk lamp mark, directs offscreen Commander angle.
- `audience`: Chivarro tests welcoming posture at entrance.

### minachiv.the_key_in_your_hand

All current exported node text and offered choices read.
Dress-specific rehearsal CG plus distinct stumble or refusal action; no literal magical portal.
Setting: Same dry bathhouse rehearsal stage, lamp shutters and wooden sound wheel.
Form and wardrobe: Chivarro dark dress with narrow pale stitching at throat; Sivane host cloak or pale Winter mask.

- `start`: Small brass key opens stage painted-door latch; only platform behind.
- `grace`: Mask hanging beyond door while Sivane host remains beside Commander, practical stage illusion.
- `caught`: Commander foot catches cloak, Sivane stops before falling; no injury.
- `caught_end`: Assistant releases altered fastening, cloak falls; Chivarro laughs watching Commander.
- `ask_move`: Host reluctantly gathers cloak; key later returned in refusal.
- `watch`: Chivarro sits down rather than guard door; Sivane effort to remain in character.

### minachiv.a_room_she_likes

All current exported node text and offered choices read.
High-priority distinct private-room sequence; friendship, new date, affectionate pause and later intimacy separated.
Setting: Chivarro private rented room, low couch, one-sound-drawer table, broad window facing blank wall, hanging dark cloth.
Form and wardrobe: Private outfit, outer robe specifically removed only later; native succubus identity; Minagho absent.

- `start`: Chivarro opens door; narrow late light, tea and wrapped ornaments.
- `notice`: Dark and pale pins held against cloth then both put away; no permanent ornament attachment.
- `separate`: Tea overfilled during frustration; do not depict graceful flawless pouring.
- `close`: Selected kiss interrupted by failed cushion; folded blanket remedy.
- `new_interest`: New date chosen, offered hand and careful mutual kiss; no undressing.
- `later`: Only later branch: one lamp lit, other cold, outer robe on unreliable chair; graphic and explicit fade and distinct evening attire.
- `friends`: Dim room before lamp, friendly stories; no Commander kiss.

### minachiv.the_price_of_her_name

All current exported node text and offered choices read.
Human-disguise investigation CG; native lilitu image would contradict stated appearance.
Setting: Outside Chivarro stair then disused storeroom with six listeners, stools and locked document box.
Form and wardrobe: Minagho explicitly blonde Mina mortal disguise, fine gloves with split thumb seam.

- `start`: Gloved Minagho offers handbill whose woodcut crown is deliberately wrong; not true costume reference.
- `reading`: Seated audience, candle, original pages displayed at distance; sealed packet tied faded cord.
- `proof`: Minagho points to true order after public correction; recognition does not imply disguise visibly drops.
- `price`: Coins counted in payment, glove seam still torn afterward.
- `question`: Threat delivered seated; takes packet, no attack or blood.

### minachiv.the_paper_she_kept

All current exported node text and offered choices read.
Needle repair is excellent distinct quiet action; later couple kiss can reuse established identities but not fake removal of disguise.
Setting: Hired room, corrected handbill, copied order, names, torn glove and lamp.
Form and wardrobe: Minagho form not newly stated; wardrobe continuity from preceding Mina scene requires care.

- `start`: Minagho threads needle second attempt, irritation; not poised combat blade.
- `cost`: Bad tight stitch puckers leather then cut and redone; Commander holds lamp offscreen.
- `record`: Copied names and underlined clerk; preserves mistaken memory in margin.
- `door`: Chivarro brings cracked red leather book away from ink; women share amused reading.
- `kept`: Chivarro bends to kiss Minagho; book retained in pocket, last glove stitch holds.

### minachiv.the_man_who_remembers

All current exported node text and offered choices read.
Rehearsal musician CG must be conditional on presence; later no-musician branch must omit him.
Setting: Bathhouse rehearsal, instrument case, platform and lamps.
Form and wardrobe: Rasen tiefling musician has canonically authored grey temples; incidental non-romance age not governed by adult-romance cosmetic cap.

- `start`: Rasen seated, case on knees, does not rise; Chivarro sits opposite.
- `music`: Flat stringed box played with TWO small hammers, not lute or violin; Winter mask and spacing around voices.
- `hire_end`: Chivarro alone beside empty case after performers leave; confession is controlled not cheerful.
- `decline_end`: No musician; assistants lamp shutter and footstep supply sound, Chivarro helps move lamp.

### minachiv.the_first_small_audience

All current exported node text and offered choices read.
Preview and ruthless negotiation merit CG; audience count and optional musician preserved.
Setting: Bathhouse preview, four invited viewers, painted stage door and benches.
Form and wardrobe: Nerath mortal shape; Sivane stage mask then removed with pale fastening in hair; musician state inherited.

- `show`: Guest refuses key, staged Winter keeps house; lamps dark at ending, not actual frozen room.
- `proposal`: Sivane joins without mask; refuses coerced private performance.
- `counter`: Chivarro folds real proposal before buyer sees inflated price; smiling to manipulate, not sincere affection.
- `end`: After public insult Chivarro tears rejected proposal and wedges it under crooked table leg.

### minachiv.the_entrance_she_wants

All current exported node text and offered choices read.
Essential wardrobe selection sequence; final chosen dress is invariant but preview branches visually distinct.
Setting: Chivarro private room, couch, window and hanging cloth changing screen.
Form and wardrobe: Starts plain dressing robe; dark severe dress versus warm loose-sleeved dress; both terminal choices select loose-sleeved performance outfit.

- `start`: Two dresses on couch, Chivarro in plain robe, assessing not posing for combat.
- `dark`: Chosen severe dress, movement exact; do not substitute loose sleeve during trial.
- `warm`: Chosen warm dress, catches trailing cuff before cup; convincing moving fabric physics.
- `promise`: After changing back robe, final choice is warm loose-sleeved dress; help release unused fastening from rough couch seam.
- `ask_later`: Same final warm dress decision, no promise of exact meeting time implied.

### minachiv.who_keeps_the_house

All current exported node text and offered choices read.
Theatrical ending contrast warrants paired prop/action CG if produced; no real mythic Winter being.
Setting: Bathhouse stage and painted door, rehearsal of two endings.
Form and wardrobe: Sivane alternating host and pale Winter mask; Chivarro dress continuity, no new form.

- `versions`: Both alternatives rehearsed: dispossessed host outside door versus hot-water bowl completing invitation.
- `winter`: Winter keeps house; charming host remains outside, no water triumph.
- `host`: Host shakes lifting bowl then plants feet; Winter takes water as imagined victory.
- `winter_end`: Chivarro on platform edge studies dust on shoe, irritation over lost establishment.
- `host_end`: Chivarro on platform edge surveys braces/lamps, pleased and ambitious.


## Continued full-scene reading: finished performance, farewell and all epilogues

### minachiv.when_the_door_opens

All current exported node text and offered choices read.
Production CG: hostess turning dress at entrance, then selected patron removal or stage ending. Audience and ending variants cannot collapse.
Setting: Bathhouse final performance with real audience.
Form and wardrobe: Chivarro warm loose-sleeved dress selected invariantly; Sivane stage costumes; optional musician state.

- `start`: Chivarro turns to show loose sleeve movement; checks braces and chalk lamp mark.
- `private`: Nerath associate informed separately, chooses side-passage bench.
- `open`: Smaller independent audience; elderly incidental guest allowed, no claim real haunted door.
- `patron`: Chivarro removes Nerath quietly through passage; no Commander rescue or violent punishment.
- `heckler`: Sivane offers key to heckler, he refuses laughing; Chivarro remains back.
- `winter`: Host outside door, lamps dark then return with Sivane unmasked beside exposed braces.
- `host`: Hot-water bowl and trembling latch hand; host retains house, not Winter triumph.
- `after`: Final lamp left lit until all collect belongings.

### minachiv.after_the_last_lamp

All current exported node text and offered choices read.
Must use arrival mortal/private outfit followed by native-form rest, never performance dress still worn. Intimacy only after choice.
Setting: Chivarro private room, closed account drawer, blanket bolstering couch, inner room.
Form and wardrobe: Loose-sleeved performance dress already folded on chair at start; current private garment unspecified. Mortal street guise remains until rest, then own face.

- `start`: Tired unarranged expression, partly loose hair; performance dress folded behind, not on body.
- `rest`: Eyes close in mortal guise, disguise released on couch; midpage native-form illustration possible only at latter moment.
- `affection`: Chosen closeness: she moves first, handholding and mutual kiss.
- `night`: Selected overnight only: shoulder turns for silver fastening removal, later pin into bowl before inner room. Prop ambiguity: dress already removed but this pin described as worn under performance lamps; needs brief clarification before exact fastening CG.
- `quiet`: Opposite couch ends, shared silence, no embrace.
- `empty`: Imagined house conversation, not literal relocation or mansion illustration.

### minachiv.the_cost_in_daylight

All current exported node text and offered choices read.
Reuse distinct daytime business environment; partnership negotiation is optional meaningful action, no separate receipt CG required.
Setting: Bathhouse table beside open shutters in daylight.
Form and wardrobe: Business attire not specified anew; do not impose previous night private gown.

- `start`: Account with all performers already paid; daylight exposes less flattering room, not flattering night gala.
- `musician`: Receipt caricature of broken shutter; melody from street does not establish Rasen physically present.
- `quiet`: No hired musician; discussion of absent instrument, not performer in frame.
- `partner`: Sivane arrives with stage sketch; damaged painted door explains repair; agreement signed, rejected draft fire explicitly allowed here.
- `separate`: Two bookings chosen, no ongoing partnership promised.

### minachiv.what_she_will_take

All current exported node text and offered choices read.
Packing is excellent arc payoff CG; lasting kiss/visits/friendship separate, no literal coast or boat.
Setting: Private hired room still rented, packing case and ornament box, hanging cloth removed revealing stain.
Form and wardrobe: Travel preparation, no departure outfit specified; not yet relocated.

- `start`: Case latch tested, room not yet surrendered; revealed wall stain after cloth folded.
- `keep`: Handbill under ornament box causes lid obstruction, moved side pocket.
- `lasting_close`: Selected lasting kiss then blank address sheet beside handbill; lid left open, feet beside case on couch.
- `distance`: Joined hands, address sheet, no obligatory kiss or Commander physique.
- `visits_close`: Coast and little boat described as imagined future, remain on real couch.
- `friends`: Expensive awkward ornament chosen for sale, not romantic surrender.

### minachiv.before_the_last_road

All current exported node text and offered choices read.
Final branch-specific relationship image; shared handholding/triad kiss only together route. Service ending must stay unresolved.
Setting: Chivarro rented room before Commander departure; three cups, sugared fruit, packing.
Form and wardrobe: Hanging cloth remains down after packing; no automatic armor or new attire.

- `start`: Fruit bag brought by Minagho, three cups; women private hand touch before turning to Commander.
- `minagho`: Minagho chosen lasting kiss; Chivarro present smiling, not necessarily triad participant.
- `together`: Earned triad hands and kiss sequence; future better couch only discussed, present old furnishings remain.
- `friendship`: Minagho disappointed but listening; fruit/game future no kiss.
- `open`: Original invitation receives second skull; object keepsake CG can avoid false lifelong commitment.
- `service`: Women touch hands together; no scene declaring Minagho free or receptive to Commander kiss.

### Complete epilogue coverage

All 24 epilogue scene IDs inspected, comprising 17 distinct full texts and seven verified exact-text completed-history duplicates.
State gates remain separately retained for each delivery ID.

- `minachiv.ending_together`: Reuse earned mask-game scene with all three only under shared relationship state; imagined later household not fixed location.
- `minachiv.ending_two`: Use paired invitations or separate relationship moments; do not force a triad kiss.
- `minachiv.ending_minagho`: Reuse earned rain-stair closeness; Chivarro remains lover in her own life, not erased.
- `minachiv.ending_chivarro`: Reuse private post-show room/date; Commander and Minagho friendship only.
- `minachiv.ending_open`: Brass stage key and invitations suitable still life; no permanent home promise.
- `minachiv.ending_friends`: Mask game company with women mutual intimacy only; no Commander romance.
- `minachiv.ending_chivarro_service`: Chivarro correspondence/individual relationship only; no image falsely freeing Minagho.
- `minachiv.ending_service`: Correspondence still life or restrained individual portrait; binding unresolved, no romantic Minagho compliance.
- `minachiv.ending_both_lost`: Old invitation still life; avoid inventing death scene or corpses not narrated.
- `minachiv.ending_minagho_lost`: Chivarro holds packet of letters in grief; no invented death circumstances.
- `minachiv.ending_chivarro_lost`: Minagho studies corrected old invitation; anger/grief, not replacement romance.
- `minachiv.ending_changed`: Old invitation between women, no invented exact Commander transformed body.
- `minachiv.ending_ascent`: Invitation remembrance still life; no unsupported divine form design.
- `minachiv.ending_sacrifice`: Two women remembering note differently; no invented battlefield death illustration.
- `minachiv.ending_unfinished_lasting`: Chivarro seals address with Minagho quietly present; earned lasting commitment preserved.
- `minachiv.ending_unfinished`: Letters still life, no completed finale or shared household.
- `minachiv.ending_aeon`: No erased-scene CG as current memory: omit CG or neutral portraits, no recognition claim.

## Continued full-scene reading: Konomi early courtship and recovery

### konomi.return_letter

All current exported node text and offered choices read.
Object CG optional; do not show Konomi physically present or resurrection accomplished by invitation.
Setting: Commander writing room, map under paperweight.
Form and wardrobe: Konomi absent; only letter and map.

- `request`: Reply folded around original letter with margin mark.
- `accept`: Map tries to unfold, paperweight restored; personal appointment only.
- `good_wishes`: No appointment in reply; preserve non-visit branch.

### konomi.retained_inquiry

All current exported node text and offered choices read.
Distinct fate-investigation object CG; black death stroke remains through attempted future annotation.
Setting: Drezen writing desk, annotated map and lamp.
Form and wardrobe: Konomi dead and absent; no ghost likeness required.

- `start`: Name and dark stroke visible both sides; no resurrection glow on body.
- `read_again`: Magnifying glass and lamp hold map corners as it attempts to fold.
- `known`: Remembered raised eyebrow and empty chair, not present living woman.
- `prepare`: Arrow holds only beneath second name; no erased death fact.

### konomi.retained_attempt

All current exported node text and offered choices read.
Reuse map setup with subtle warm ink intervention; no successful resurrection frame before selected attempt and result.
Setting: Same desk, prepared arrow and clean sheet.
Form and wardrobe: No living Konomi depicted; thought of waking is hypothetical.

- `start`: COPY stamp lifts from sheet turned to ORIGINAL CONTINUES.
- `attempt`: Finger follows arrow, thumb covers annotation; attempt not established success.

### konomi.return_first_words

All current exported node text and offered choices read.
Recovery portrait and cautious hand movement distinct from romance glamour; hand contact only established-love branch.
Setting: Recovery visit, chair with arms and cup within reach.
Form and wardrobe: Recovery-appropriate civilian clothes unspecified; tired adult Konomi, attractive without erasing physical effort.

- `start`: Konomi slowly opens hand, breath between sentences.
- `love`: Reaches but misses Commander hand slightly; assisted connection, no grand embrace.
- `boundary`: Both hands on chair arms, older breakup remains respected.
- `water`: Takes own cup and attends carefully to drinking; wants later visit.

### konomi.return_second_visit

All current exported node text and offered choices read.
Reuse recovery setting with more alert expression; ruler held as hand occupation, no full-body triumphant transformation.
Setting: Recovery conversation beside map, blank paper and ruler.
Form and wardrobe: Civilian recovery outfit, no invented appointment uniform.

- `start`: Measures empty map space twice.
- `laugh`: Brief unprepared laugh, paper folded then reopened.
- `closed`: She puts ruler away and leaves for own planned short walk; no rekindled romance.
- `familiar`: Hand rests beside Commander before withdrawal, no automatic kiss.

### konomi.margin

All current exported node text and offered choices read.
Official desk portrait sufficient; struck-out sentence and written invitation give optional object-focused CG.
Setting: Official desk, corrected report stack and closed door.
Form and wardrobe: Council clothing appropriate here; adult native-recognizable Konomi.

- `start`: Turns paper with heavily crossed-out insult, controlled critical expression.
- `answer`: Writes address and time on blank sheet, not a romantic embrace.
- `official`: Files corrected report and continues professional work.

### konomi.reception

All current exported node text and offered choices read.
High-priority reception-to-covered-walk composition with social dress; no council uniform recolor.
Setting: Crowded reception then covered walk with pillar and open rear door.
Form and wardrobe: Explicitly changed out of council clothing; distinct social outfit required.

- `start`: Nearly untouched glass, claims quiet corner.
- `private`: Leans against pillar looking toward interior lights, social crowd remains through open door.
- `interest`: Open warm smile after attraction chosen; no kiss authored.
- `slow`: Careful expression and uncertain invitation, not overt romantic victory.

### konomi.letter

All current exported node text and offered choices read.
Speaker and letter reuse sufficient; present conversation must not be mistaken for remote correspondence.
Setting: Private conversation at writing case; she is physically present.
Form and wardrobe: Current setting clothes not specified; no obligatory council gear.

- `start`: Finger beside final line of repeatedly opened letter.
- `terms`: Writes one sentence on back; read later when Commander alone.
- `stop`: Folds along old crease and keeps letter, courtship ended.

### konomi.evening

All current exported node text and offered choices read.
Private supper arrival, selected kiss and morning comb are strong differentiated CGs; window state varies by remembered branch.
Setting: Modest private supper room, bare plant pot on windowsill, dish of removed hairpins.
Form and wardrobe: Hair loosened because pins removed; distinct private clothes appropriate, not council equipment.

- `start`: Opens door herself, supper waiting, pins in dish, no official papers.
- `kiss`: Meets kiss before Commander stops, pulls sleeve then keeps hold.
- `stay`: Consensual overnight fade; morning borrows comb and kisses at door, no explicit act illustration.
- `changed`: Unused place setting moved aside for letter; do not impose eating or fixed transformed Commander body.
- `remembered_quiet`: Shutter fastened.
- `remembered_street`: Window opens to street voices.
- `remembered_play`: Taps rhythm at table then deliberately loses beat; dance only proposed afterward.

### konomi.disagreement

All current exported node text and offered choices read.
Reuse serious work portrait; revised crossed-out insult is meaningful action but no new setting needed.
Setting: Official memorandum and settlement petition.
Form and wardrobe: Official attire, no private-date pose.

- `respect`: Reads own opening then crosses it out, recommendation retained.
- `frank`: Pushes petition forward, genuine political disagreement.
- `end`: Papers put away, supper still planned; supplies not secretly reallocated here.

### konomi.leak

All current exported node text and offered choices read.
Distinct privacy-breach expression/prop CG useful; public/discreet/denial breakup kept separate.
Setting: Konomi writing desk, copied intimate letter with outside annotations and seal.
Form and wardrobe: Controlled anger, work clothes.

- `start`: Copied page laid flat, rigid anger rather than flirtation.
- `lie`: Hand rigid beside page, direct refusal.
- `together`: Official reply by door for collection, private page folded separately.
- `end`: Letters tied into bundle, drawer closes; no reconciliation image.

### konomi.reckoning

All current exported node text and offered choices read.
Foot-drawn chair and delighted political deduction offer action variety; kiss only actual selected terminal choice.
Setting: Desk with three letters, petition, receipts, later fourth evidence sheet.
Form and wardrobe: Work attire, absorbed pleased expression then branch-specific hurt.

- `start`: Draws chair closer with foot without graceful performance.
- `discreet`: Fourth sheet reveals differing inspection dates, delighted deduction.
- `repair`: Lets papers go, looks at letter drawer, hurt unresolved.
- `repaired`: Moves chair closer but does not claim apology fully settled trust.
- `close`: Invites closer; choices separately allow kiss or just sitting, so base node CG must not force kiss.

### konomi.unsent

All current exported node text and offered choices read.
Letter still life or Abyss writing detail; all descriptions and Konomi reactions are imagined, no remote meeting.
Setting: Commander in Abyss with fresh sheet, no courier.
Form and wardrobe: Konomi physically absent; no assumed Commander appearance.

- `wonder`: Dark window reflection remembered, crossed-out florid draft; do not show shared sightseeing.
- `fear`: Sheet turned over; vulnerabilities authored in letter, no visible Konomi comforting him.
- `write`: Folded letter kept by Commander; no delivered answer.


## Continued full-scene reading: Konomi return, future and ordinary hours

### konomi.return

All current exported node text and offered choices read.
Lamp-and-glass reconstruction of an Abyss sight is a strong actual shared action, not shared travel.
Setting: Konomi desk and bare pot by window after Abyss return.
Form and wardrobe: Private conversation outfit not specified.

- `wonder_reply`: Empty glass lifted beside lamp casts pale oval on writing case; both adjust tabletop reconstruction.
- `wonder_uneasy`: Glass set down, oval disappears.
- `kindness`: Dinner guests are a recollection only; Konomi currently smooths letter and touches hand.
- `fear_question`: Reaches for pen then leaves it, hand offered beside Commander not forcibly taken.
- `fear_listen`: Tightened expression while waiting; asks lamp moved from Commander eyes.
- `guest_answer`: Laughs at recalled guest, letter finally stored separate from official papers.

### konomi.power

All current exported node text and offered choices read.
Reuse reflective private portrait; no cosmic-control image or imposed Commander form.
Setting: Private discussion with closed writing case and spare seat.
Form and wardrobe: No new costume specified, Commander transformation variable.

- `trickster`: Studies old seal impression; roof repair is a joke/request, not performed fate rewrite.
- `commit`: Relieved laughter while making incomplete plans; no already-built home.
- `part`: Eyes close briefly then respectful separation, no embrace assumed.

### konomi.ordinary

All current exported node text and offered choices read.
New potted plant payoff optional cozy CG; recalled loading trial is not happening in room.
Setting: Private room with plant and papers at opposite ends.
Form and wardrobe: Comfortable visit clothes, not mandatory official uniform.

- `start`: Brings small potted plant and stack, sets far apart.
- `rest`: Settles comfortably, asks lamp moved; no productivity pose.
- `work_morning`: Dirty glove and handcart only remembered; present papers moved away from plant.
- `end`: Papers remain untouched at low lamp.

### konomi.farewell

All current exported node text and offered choices read.
Letter handoff with tender concern useful payoff; no invented departure battlefield or certain survival.
Setting: Personal farewell with unsealed letter.
Form and wardrobe: No new clothing specified.

- `start`: Unsealed letter handed over now, not posthumous delivered note.
- `promise`: Smile fades into serious request to return if possible; waits longer at door.

### konomi.parting

All current exported node text and offered choices read.
No new CG necessary; breakup versus continued scheduling need expression/state-compatible portraits.
Setting: Desk and appointment book.
Form and wardrobe: Existing conversation outfit.

- `end`: Practical returned belongings discussed; no actual packed case authored.
- `stay`: Opens appointment book toward Commander; new time chosen, not breakup.


## Continued full-scene reading: hearing and market, including private-history variants

All six public/private delivery scenes fully assessed.
Shared node texts verified byte-exact before reuse, with separate private and missed-history opening text read.
Borrowed-room starts must not inherit an official office merely because the hearing body is shared.

### konomi.hearing and konomi.private_hearing

Stationer hearing and private courtyard decision merit CG; buyer absent, exactly three women adjudicate, letter masking branch-specific.
Setting: Desk then stationer workroom between two drying racks, courtyard drain.
Form and wardrobe: Public hearing clothes; no combat outfit required.

- `arrival`: Silver-haired registrar and two working copyists at table, empty chair opposite Konomi; incidental older registrar is not romance redesign subject.
- `courtyard`: Konomi pushes spoiled paper from drain with shoe, turns wrapped packet in hands.
- `whole`: Soft-corner wrapper handed to Commander, permission can still change.
- `finding_whole`: Three women read silently; Konomi studies table stain, buyer absent.
- `finding_covered`: Loose slips held by wrapper corners cover BOTH versions, no ink redaction; outside removes slips one by one.

### konomi.hearing_after and konomi.private_hearing_after

Pastry-sharing is distinctive warm aftermath, not forced forgiveness or kiss.
Setting: Konomi room, finding and old wrapped letter on table.
Form and wardrobe: Private supper attire suitable; no fixed court robe.

- `covered`: Rubs ink mark then stops; still disappointed though invites company.
- `trust`: Runner offscreen, finding goes beneath book.
- `evening`: Two unequal apple pastries; Konomi takes larger, mischievous recovering expression.
- `warm`: Breaks off piece onto Commander plate, knee contact under table; next choice may kiss or simply stay, so base illustration no kiss.

### konomi.new_letter and konomi.private_new_letter

High-priority playful ring-throwing sequence plus conditional bell, rooster or ribbon prize; not one universal winning image.
Setting: Letter handoff then afternoon Drezen market ring stall and quieter street.
Form and wardrobe: Civilian outing clothes, active wrist/sleeve fit; no council armor assumption.

- `market`: Plank with THREE wooden pegs; near ribbon, middle brass bell, far garish wooden rooster; older broad-shouldered stallholder incidental.
- `first_throw`: First overshoots, second short, third still in fingers; no rooster victory.
- `advice`: Konomi wins brass bell at middle peg, rings softly beside Commander ear.
- `watch`: Third clips far peg then spins away; frustrated small sound, no prize awarded.
- `ribbon`: Commander wins blue ribbon, Konomi ties it on Commander wrist.
- `frank_reply`: Selected romantic invitation: sleeve-drawn kiss under awning, street passerby.
- `give_rooster`: Rooster gifted to Konomi; grips to keep crest off sleeve.
- `give_ribbon`: Ribbon transferred to Konomi wrist only after chosen gift, imperfect knot left intact.
- `keep_ribbon`: Ribbon remains on Commander wrist; never wear it on Konomi in this branch.


## Continued full-scene reading: impossible post, private departure and distance

### konomi.fate_post

All current exported node text and offered choices read.
Distinct Trickster CG: ruled line from dismissed address grows into door, not restored office or summoned compliant woman.
Setting: Commander desk and wall becoming ink postal door.
Form and wardrobe: Konomi absent; ink-stained gloved clerk hand only.

- `start`: Line runs off page across table and up wall to drawn door and slot.
- `second_slot`: Second PRIVATE LETTERS slot with gloved hand and blank envelope.
- `send`: OFFER added to DELIVERY; ink door folds into receipt, dismissal line remains.

### konomi.fate_reply

All current exported node text and offered choices read.
Letter/ordinary carrier reuse; do not picture Konomi in bath or at her courtyard yet.
Setting: Commander quarters, ordinary carrier and letter.
Form and wardrobe: Konomi absent; mortal carrier not magical clerk.

- `start`: Konomi describes letter under cup in absent scene; current carrier delivers ordinary envelope.
- `accepted`: Corrected directions entrance BESIDE cooper yard, not through it.
- `declined`: Carrier takes refusal, no physical meeting.

### konomi.private_meeting

All current exported node text and offered choices read.
Distinct courtyard introduction and reserved emotional posture; handholding only return history.
Setting: Covered travelers courtyard beside cooper yard, rattling shutter, two chairs.
Form and wardrobe: Independent civilian day clothes, no council office uniform required.

- `start`: Konomi fastening shutter before turning; linen carrier directs visitor.
- `first`: Moves chair to see passage without turning head.
- `interest`: Draws chair slightly closer, no kiss.
- `return`: Hand rests over Commander hand, lingering hurt.
- `arrange`: Opens passage gate herself, hand remains on gate while glad visitor came.

### konomi.carriers

All current exported node text and offered choices read.
Wagon measuring and active negotiation excellent pose variation; no owned third wagon.
Setting: Wagon yard, two wagons, six horses and empty chests.
Form and wardrobe: Practical civilian clothes with sleeves kept from grease; Vanna/Selis incidental middle-aged women not romance cosmetic target.

- `start`: Konomi under RAISED tailboard keeps measuring cord clear of axle grease then steps out.
- `measure`: Vanna and Commander hold cord ends, Konomi records usable space.
- `customers`: Sets cord down, Selis flushes, Vanna anger eases.
- `walk`: Checks sleeve remains grease-free.
- `evening`: Moves cord between hands before sleeve/arm touch at street fork.

### konomi.before_road

All current exported node text and offered choices read.
Existing arrival/seated/near variants support separate moments only after individual and sequence review; kiss needs selected branch, not preselection close portrait.
Setting: Borrowed private room, unfastened case with cloth caught beneath buckle, window ajar, rug and two chairs.
Form and wardrobe: Distinct private gown as authored candidate design; actual prose does not name garment; no automatic battle outfit.

- `start`: Standing door closure; case moved out of seat place, straps loose.
- `departure`: Sits leaving chair nearest case for Commander.
- `company`: Same seated arrangement and visible case, no premature contact.
- `histories`: Window open only a little; sweeping audible below.
- `near`: Closes hand distance and pulls own chair, leg catches rug; downward annoyed laugh before knee contact.
- `kiss`: Selected mutual kiss with hand at back of Commander neck; no assumed race/body.
- `talk`: Can follow either kissed or unkissed route, so no lingering kiss-specific face/action mandatory.
- `finish`: Gets up to trim lamp then returns, case still unfastened; no undressing or overnight claim.

### konomi.private_departure

All current exported node text and offered choices read.
Departure CG with exact carriage placement plus optional farewell kiss; no generic private gown in wagon yard.
Setting: Loaded wagon yard then road departure.
Form and wardrobe: Travel clothes, small shoulder bag; case secured behind driver bench.

- `start`: Two wagons loaded, Selis list and Vanna fastenings, horse stamps, Konomi steps from wheel.
- `kiss`: Bag set down, brief then second kiss; Selis conspicuously studies list.
- `hand`: Both hands around Commander hand, no kiss.
- `leave`: Konomi and Selis first bench, Vanna second wagon; bag between feet, one hand catches bench after rut, other waves.

### konomi.capital_letter

All current exported node text and offered choices read.
Object still life sufficient; if optional capital vignette clearly label correspondence illustration rather than in-person visit.
Setting: Commander quarters receiving and answering Nerosyan letter.
Form and wardrobe: Konomi absent; reported capital life not present physical scene.

- `arrival`: Wall-facing rented room and instrument practice only reported.
- `personal`: Pear eaten while writing alone is reported memory, suitable authored inset only, not shared fruit.
- `answer`: New direct address copied onto ordinary outgoing post.

### konomi.return_offer

All current exported node text and offered choices read.
Reuse letter illustration, optional distinct tune sheet; no arrived Konomi before future reunion.
Setting: Commander reads envelope containing letter and copied tune.
Form and wardrobe: Konomi absent; work and travel proposed only.

- `start`: Copied half-tune with note where player restarts.
- `quiet`: Pear explicitly NOT mailed after carrier explains decay; never depict parcel pear.
- `distraction`: Konomi blocking stairs while reading is reported capital anecdote, not present scene.
- `confirm`: Confirmation posted; journey still pending.


## Continued full-scene reading: private history and reunion

### konomi.private_history

All current exported node text and offered choices read.
No separate CG for 35 history acknowledgments; reuse courtyard with restrained disagreement/relieved invitation variants.
Setting: Covered courtyard, bench, cup over folded petition and narrow writing case.
Form and wardrobe: Civilian meeting attire; histories vary, no restored office assumed.

- `start`: Petition drawn from beneath cup, closed case beside it.
- `public`: Hard expression at lost courier access, not gleeful triumph.
- `discreet`: Brief sharp smile discovering leak channel.
- `apology`: Hands removed from case, stern answer, no automatic forgiveness pose.
- `repaired`: Case moved to other side, space beside her cleared; closeness invited after prior repair.
- `part`: Takes case and stands, waits at passage for Commander exit; no next date.
- `missed_repaired`: Same seating gesture as repaired but no dismissal history; image reuse safe, dialogue histories remain distinct.

### konomi.private_reunion

All current exported node text and offered choices read.
High-priority reunion with parcel, branch-specific meal and earned kiss; merged nodes require setting-neutral crops or state-aware variants.
Setting: Arrival courtyard; chosen walk outdoors or upstairs rented room, then shared meal nodes retain selected setting.
Form and wardrobe: Arrival travel clothes; no wardrobe change stated before meal, no universal private-gown assumption.

- `start`: Standing by travel case with paper parcel, delegation reflex changes to quiet laugh.
- `embrace`: Parcel carefully set on case before chosen embrace.
- `parcel`: Pears bought locally after arriving, not shipped fruit.
- `walk`: Case left in room, Commander carries parcel; wrong-turn locked yard then outdoor seat and paper meal.
- `room`: Commander carries case upstairs, Konomi parcel, bread at little table and interrupted humming.
- `kiss`: Bread set down before cheek touch and kiss; can be outdoor or indoor, cannot hardcode bedroom.
- `content`: Cuts pear and offers first piece, intimate ordinary action without required kiss.
- `absence_page`: Sheet read beside her, no universal table since walk possible.
- `absence_close`: Asks permission to kiss and waits; no kissed expression before selection.
- `absence_kiss`: Selected hand behind neck, mutual kiss then forehead contact; retain inherited indoor/outdoor setting.
- `absence_quiet`: Shoulders touching and listening; no kiss, no room-only backdrop.
- `absence_memory`: Horse and pouch repair remembered, not current departure yard.


## Continued full-scene reading: future choices and Konomi epilogues

### konomi.lease_offer

All current exported node text and offered choices read.
Reuse exterior business portrait, optional hands-behind-back ambition pose; no signing or new mansion already owned.
Setting: Outside leased building, shuttered windows and street corner.
Form and wardrobe: Civilian business outfit, sleeve holding folded offer.

- `start`: Tenant locks door and leaves with agreement; Konomi watches her go.
- `influence`: Hands folded behind back looking upward; open ambition.
- `wait`: Offer tucked away, reduced fee not a cheerful uncomplicated victory.
- `walk`: Stops at corner locating tenant, brushes fingers, supper later only.

### konomi.chosen_evening

All current exported node text and offered choices read.
Distinct relaxed-but-troubled supper and selected intimate standing kiss; breakfast shared across overnight and separately sleeping branches.
Setting: Agreed private supper, later private night OR separate departure then breakfast.
Form and wardrobe: Hair loosened from traveling arrangement, no papers; civilian supper attire.

- `start`: Arrives with loosened hair, drinks before speaking, no papers.
- `close`: After dishes aside draws chair for knee contact and offered hand; no kiss before choice.
- `night`: Selected standing mutual kiss, collar grip, graphic and explicit night fade.
- `quiet`: Head against shoulder, lifts at passage noise then settles; they PART for night and meet breakfast.
- `morning`: Moves bread plate toward Commander; must not imply same-bed wake for quiet branch.
- `friends`: Withdraws hand, looks at empty hands, disappointed not smiling flirtation.

### konomi.private_future_choice

All current exported node text and offered choices read.
Reuse courtyard and departure images with exact commitment/open/parting state; no need image for every future answer.
Setting: Courtyard decision then selected later wagon departure.
Form and wardrobe: Travel preparation civilian clothes, bag strap.

- `commit`: Hand finds Commander hand, pleased commitment.
- `open`: Hand offered despite possible wish for more; not wedding or shared home.
- `kept`: Later yard departure with handhold and bag check, both commitment and open paths.
- `part`: Hand moves to bag strap; goodbye courtyard gate, Commander explicitly ABSENT at departure yard.

### Every current Konomi epilogue read

- `konomi.ending_public`: Reuse letters or independent-work portrait; no surrender of opinions.
- `konomi.ending_private`: Surviving modest potted plant in shared room is optional symbolic CG; privacy remains.
- `konomi.ending_changed`: Neutral correspondence or Konomi portrait; transformed Commander body unspecified.
- `konomi.ending_ascended`: Konomi reads answer alone; no guaranteed humanoid deity appearance.
- `konomi.ending_apart`: Small tied letters among belongings, no current romantic embrace.
- `konomi.ending_dismissed_apart`: Travel correspondence still life; no further meeting or office restoration.
- `konomi.ending_unfinished`: Evening eventually filled, messenger glance; no earned reunion depicted.
- `konomi.ending_aeon`: Margin sentence with inexplicable hesitation, not conscious memory of original romance.
- `konomi.ending_distance`: Reuse earned journey/hand reunion; no single shared house claimed.
- `konomi.ending_distance_open`: Travel invitations with continuing courtship, not commitment tableau.
- `konomi.ending_distance_apart`: Letters finally stored in Nerosyan, no Commander at current business visit.
- `konomi.ending_distance_changed_open`: Unfinished letter put away, visits stopped; no happy transformed couple.
- `konomi.ending_distance_ascended_open`: Letters to unknowable address; no confirmed divine reply or reunion.
- `konomi.ending_distance_lived`: Reuse earned correspondence; exclusive and portfolio career variants retain different outcomes.
- `konomi.ending_distance_open_lived`: Same career variants may reuse art, open relationship not promoted to lifelong promise.
- `konomi.ending_missed_declined`: Crossed-out appointment, independent onward journey, no courtship.
- `konomi.ending_missed_interrupted`: Packet and differently folded pages only; developed/affection/meeting/invitation must not depict unearned history.
- `konomi.ending_missed_interrupted_aeon`: No arrival or current remembered romance; erased impossible delivery has no address.

## Full production instruction and review boundary

Every distinct intimacy, materially different ending and established group milestone needs an explicit illustration or justified reuse decision.
A text assessment is not an image review or approval.
The ledger now stores this review status on every fully assessed scene and node.
Node-specific visual constraints identify the required state if illustrated; they do not mandate a separate image for every response.
Mature intimate imagery remains graphic and explicit.
The established Minagho/Chivarro triad has its own milestone track, separate from their existing couple bond and two independent Commander relationships.
The established Anevia/Irabeth/Commander track remains pending full reading.
Prospective demon groups receive no implemented-relationship credit from solo routes or portraits.

## Continued full-scene reading: political independence and shared working evenings

### konomi.political_account

All current exported node text and offered choices read or exact shared text verified.
No new CG needed beyond serious independent Konomi portrait; political circumstances are reported, not current scenes.
Setting: Private desk, two folded letters and closed writing case.
Form and wardrobe: Work-related private conversation clothing.
Review: candidate comparison and independent image approval pending.

- `foreign`: Foreign garrisons described, not soldiers in room.
- `questions`: Private letters not shown without permission; hand beside Commander.
- `replies`: Chair turned toward Commander after case closes.

### konomi.private_political_account

All current exported node text and offered choices read or exact shared text verified.
Reuse suitable borrowed-room portrait; shared political text verified exact with public version, different role history preserved.
Setting: Borrowed return room, lamp and folded letter.
Form and wardrobe: Civilian clothes; no official role reappointment.
Review: candidate comparison and independent image approval pending.

- `start`: Folded letter set down, evening outside former office.
- `missed_start`: Same setting but no dismissal assertion.
- `concluded`: Letter turned over, no council uniform invented.

### konomi.another_evening

All current exported node text and offered choices read or exact shared text verified.
No new character CG; invitation object reuse.
Setting: Commander reads folded invitation.
Form and wardrobe: Konomi absent.
Review: candidate comparison and independent image approval pending.

- `start`: Merchant supper address, four evenings requested; underlined unpromising dish.

### konomi.a_useful_supper

All current exported node text and offered choices read or exact shared text verified.
Distinct social-business supper ensemble and participant grouping; not private seduction dinner.
Setting: Walk to upstairs merchant supper room above adjoining storage yards.
Form and wardrobe: Konomi good coat and fine gloves, puts one on then second across wrist.
Review: candidate comparison and independent image approval pending.

- `start`: Tugs glove fingers into place, folded sketch of adjoining yards.
- `table`: Varine broad woman tight silver ring, Oselda lean and neat, male Hesset brushed coat, serving woman bowls; no surprise new romance.
- `needs`: Moves dubious covered dish away from Commander plate with dry humor.

### konomi.the_upper_passage

All current exported node text and offered choices read or exact shared text verified.
Noise investigation, laugh at failed test, and branch-specific tenderness earn separate action CGs.
Setting: Upper rented passage above wagon yard then yard/street.
Form and wardrobe: Explicit plain cloak over good coat, impressive gloves.
Review: candidate comparison and independent image approval pending.

- `start`: Four empty barrels and loose pegs; rail transmits sharp sound.
- `miss`: Konomi turns away laughing; Sella appears holding sleeping child, trial stops.
- `slow`: Same child interruption; no further load-carrying trial afterward.
- `hear`: Loose plank jumps against iron bracket, mechanical noise not supernatural effect.
- `early_end`: Selected successful early path: removes splinter with small pin and kisses uninjured palm.
- `late_end`: Late path: arm walk then street-corner kiss, no splinter treatment claim.

### konomi.two_bad_prices

All current exported node text and offered choices read or exact shared text verified.
Reuse ensemble negotiation setting with meaningful quieter under-table contact, not separate CG per cost paragraph.
Setting: Cleared merchant supper table, improved lamp and tenant hours/ruler.
Form and wardrobe: Good coat/social business clothing.
Review: candidate comparison and independent image approval pending.

- `evening`: Foot briefly touches Commander beneath table after selecting her evening trial.
- `morning`: Hand briefly finds Commander beneath table despite rejected preference, no celebratory triumphant pose.

### konomi.the_trial_day

All current exported node text and offered choices read or exact shared text verified.
Distinct actual-work outcome CGs plus selected kiss/rest at closed stall; never merge morning/evening light or dirt history.
Setting: Mutually exclusive evening unloading OR morning waiting yard, then shelter by closed stall.
Form and wardrobe: Practical good coat and gloves; dirty palm only morning cart-moving branch.
Review: candidate comparison and independent image approval pending.

- `evening`: Listen from stair landing, upper passage unavailable; two porters and two casks remain at firm stop time.
- `morning`: Borrowed brazier charcoal, blocking handcart moved with Bel; no magically clear gate.
- `morning_cost`: Dark streak across glove palm intentionally kept.
- `walk`: Shelter from wind by closed stall; she removes one glove before handhold.
- `kiss`: Chosen kiss hand at waist, then other glove removed and folded.
- `rest`: Shoulder resting and hand held, no kiss required.

### konomi.a_name_beside_hers

All current exported node text and offered choices read or exact shared text verified.
Joint-author dispute may reuse supper/work portrait; no romantic triad with Oselda.
Setting: Private table, heavy glass cup and report draft, Oselda visits.
Form and wardrobe: Business conversation attire, no performance costume.
Review: candidate comparison and independent image approval pending.

- `start`: Finishes water before speaking, Oselda enters with differently colored annotations.
- `joint`: Oselda chair closer to correct address, business only; after she leaves Konomi touches Commander sleeve/fingers.
- `circular`: Private offer laid aside with regret, catches Commander hand while inviting later supper.

### konomi.the_evening_she_kept

All current exported node text and offered choices read or exact shared text verified.
Full intimacy sequence decision: supper warmth, kitchen-close anticipation, selected standing kiss and graphic and explicit night aftermath OR coat-on lamplit walk.
Setting: Private supper then inner room night OR cold street walk and doorway farewell.
Form and wardrobe: Coat already over chair indoors; puts it on for air branch; no papers in hands.
Review: candidate comparison and independent image approval pending.

- `start`: Two MATCHING cups, toasted bread/pepper, coat off and shoulders less guarded.
- `supper`: Mushrooms under crisp crust softened by sauce, hand over last slice; she did not cook dish.
- `plans`: Dishes cleared, hand behind neck, brushes lips then waits before final choice.
- `night`: Table edge interrupts kissing, inner-room doorway kiss; lamp remains OUTER table; later relaxed covered graphic and explicit embrace can illustrate chosen overnight.
- `air`: Coat on for cool street, lamplight closeness; goodbye kiss then remains doorway until Commander looks back.


## Continued full-scene reading: absence, earned time, final private farewell and dance

### konomi.private_absence

All current exported node text and choices read or exact donor text verified, including history and career variants.
Pouch/cord/address still life distinct from letter desk; no imagined Konomi waiting as fact.
Setting: Commander in Abyss off-watch, belongings and torn pouch.
Form and wardrobe: Konomi absent, no fixed Commander body.
Review: exact candidate matching and independent approval pending.

- `start`: Catches folded address before ground, crouched only Commander if shown.
- `repair`: Cut weak cord shorter and rethread loops; no magic mend.
- `remember`: Departure horse and sleeve touch are recalled prior scene only.
- `changed_memory`: Explicitly rejects imagining patient woman eternally waiting on road; do not illustrate that trope.

### konomi.private_absence_catchup

All current exported node text and choices read or exact donor text verified, including history and career variants.
Same earned kiss/listening beats can reuse setting-neutral reunion art; no parcel, pears or arrival implied by copied prose.
Setting: Private visit in Drezen, exact venue unspecified.
Form and wardrobe: Visit clothes, no meal props assumed from donor reunion.
Review: exact candidate matching and independent approval pending.

- `start`: Makes room beside her, waits; no specified case/meal.
- `absence_close`: Asks kiss and waits, not kissed already.
- `absence_kiss`: Selected mutual kiss and forehead touch; neutral visit setting.
- `absence_quiet`: Shoulders touching, head tilted listening; no kiss.
- `absence_career_future`: Career outcomes recalled, not happening as simultaneous meetings.

### konomi.private_return_terms

All current exported node text and choices read or exact donor text verified, including history and career variants.
Distinct samples-and-ambition CG plus greeting cheek touch; no furniture seller cosplay.
Setting: Agreed meeting after journey, narrow wooden sample box.
Form and wardrobe: Dust on travel hem, civilian traveling clothes.
Review: exact candidate matching and independent approval pending.

- `start`: Wooden box under arm set down, touches Commander cheek.
- `offer`: Small brass fittings, one leaf-shaped; not jewelry or magical relic.
- `alternative`: Shows plain practical underside of brass leaf to Commander.
- `exclusive`: Terms written and hand caught after lid closed; no actual employer signing yet.
- `portfolio`: Lower fee chosen, larger figure glanced at; hand retained.

### konomi.private_kept_hours

All current exported node text and choices read or exact donor text verified, including history and career variants.
Separate afternoon choices materially change setting and actions; each chosen kiss versus listening needs explicit variant/reuse.
Setting: Lease office then short closed-doorway shelter OR long walk to broken wall/stone seat.
Form and wardrobe: Civilian work/travel clothes, no automatic nightgown.
Review: exact candidate matching and independent approval pending.

- `start`: Applicant exits with traveling cloak; owner absent.
- `work`: Konomi writes, Commander reads book; after hour she marks place with scrap and puts book aside.
- `leave`: Declines extra work, closes sample box for collection then arm offered at street.
- `short_walk`: Shelter of CLOSED doorway, hand at waist, interested look before kiss choice.
- `short_kiss`: Kiss pauses for passerby then resumes; standing doorway, not garden.
- `short_talk`: Hand squeeze at turning, no kiss.
- `long_walk`: Pale unnamed flowers through broken wall, loose stone seat, hand kissed before branch.
- `long_kiss`: Stone shifts midkiss; both settle steadier, later straighten each other collars.
- `long_talk`: Shoulder leaning and thoughtful listening on stone, no mouth kiss.

### konomi.private_last_visit

All current exported node text and choices read or exact donor text verified, including history and career variants.
Final farewell deserves bed-edge closeness then selected overnight or quiet pre-duty parting; different lamp/book states.
Setting: Lived-in rented bedroom, case UNDER bed, book on windowsill, cloth bookmark.
Form and wardrobe: Private civilian outfit; no arrival travel-case pose or undressing before chosen night.
Review: exact candidate matching and independent approval pending.

- `start`: Door closed, rests against it; case no longer by door.
- `business`: Sits bed edge leaving space beside.
- `whole`: Raises Commander hand to cheek, leans in.
- `close`: Holding, thumb touches mouth while waiting for requested kiss; no completed kiss yet.
- `night`: Chosen kiss then lamp OUT, hand held under cover graphic and explicit; morning book stays windowsill and doorway kiss.
- `quiet`: Evening grows dark then she lights lamp before departure; book relocated within bed reach, doorway hug not overnight.

### konomi.a_turn_for_herself

All current exported node text and choices read or exact donor text verified, including history and career variants.
High-priority full-body movement CG and explicit lead/follow/beside states; humanized attractive identity with physical cloth inertia.
Setting: Borrowed reception room cleared for private dance, tables against wall, one shutter.
Form and wardrobe: Skirt with free turn, expensive embroidered sleeve/cuff, soft shoes; outdoor shoes under chair.
Review: exact candidate matching and independent approval pending.

- `start`: Soft brushed shoes in wooden box on desk, invitation not yet dance.
- `room`: Already dancing solo, heel lift and skirt sweep, no supper.
- `follow`: Konomi leads with hand pressure and shoulder orientation.
- `lead`: Commander leads, chair moved together before wider turn.
- `beside`: Parallel dance with generous gap, NO touch required.
- `quiet`: Shutter closed, only thin daylight stripe.
- `pleasure`: Shutter fully open, cuff bright threads lit as wrist turns.
- `play`: Wrong-wall ending, over-shoulder amused glance then exaggerated bow.
- `beauty`: Whole solo figure, bright cuff arcs in light, offered hand stays at distance.
- `finish`: Sits changing shoes, soft pair cooling then boxed; no kiss authored.


## Continued full-scene reading: political result and missed-contact introduction

### konomi.the_names_admitted

All current exported node text and offered choices read.
No new setting CG needed; independent ambition and sharp sponsor smile suitable expression variant, actual people in correspondence absent.
Setting: Private table with two permitted pages, names and folded letter.
Form and wardrobe: Civilian work attire, no new council post implied.
Review: exact candidate matching and independent approval pending.

- `start`: Finger by her name; some others struck out; restricted papers not exposed.
- `recognized`: Writes acceptance plus separate request, no Marenne in room.
- `sponsor`: Sharp pleased smile, sponsorship not counterfeit appointment.

### konomi.the_answer_on_record

All current exported node text and offered choices read.
Result discussion portrait plus explicit selected kiss OR outdoor arm-in-arm walk.
Setting: Desk, two allowed sheets and restricted packet secured in case.
Form and wardrobe: Civilian conversation attire, gloves only fetched for walk.
Review: exact candidate matching and independent approval pending.

- `start`: Moves empty chair closer with foot.
- `role`: Shared pages rewrapped, restricted contents never on Commander side.
- `close`: Draws Commander hand into lap, holds in both hands, no kiss until chosen.
- `kiss`: Meets halfway, hand behind neck; case afterward under desk, not on chair.
- `walk`: Finds gloves INSIDE case, outside each chooses turning; no kiss authored.

### konomi.the_unintroduced_letter

All current exported node text and offered choices read.
Distinct impossible WINDOW IN SHEET, not fate_post full wall door; personal introduction not existing courtship proof.
Setting: Commander desk and sheet with two squabbling bureaucratic sides.
Form and wardrobe: Konomi absent; prudent mortal clerk and magical ink-stained finger.
Review: exact candidate matching and independent approval pending.

- `start`: Annotations on both sides of same sheet.
- `sides`: Rectangular paper window, finger taps notice, mortal clerk offers fresh envelope.
- `send`: Window expands around envelope without folding edges then returns ordinary sheet; no Konomi summoned.

### konomi.the_answer_she_addressed

All current exported node text and offered choices read.
Letter still life or carrier reuse; described envelope-between-carriers moment optional marked memory only.
Setting: Commander receives ordinary carrier letter.
Form and wardrobe: Konomi absent; reported carriers are not physically present.
Review: exact candidate matching and independent approval pending.

- `start`: Delivery recorded in carrier book; wagon partnership recounted in letter.
- `accept`: Ordinary outgoing reply, nothing opens in wall.
- `decline`: Receipt produces no new envelope, invitation ended.

### konomi.the_courtyard_introduction

All current exported node text and offered choices read.
Courtyard introduction can reuse private_meeting setting with DIFFERENT stone-supported chair state and history; no compulsory touch.
Setting: Covered courtyard via passage smelling clean linen, cooper yard next door.
Form and wardrobe: Civilian day clothes, no council gear requirement.
Review: exact candidate matching and independent approval pending.

- `start`: Small stone under second chair leg, chair level, Konomi satisfied.
- `interest`: Konomi moves own chair nearer; stone remains beneath Commander chair.
- `lover`: Chosen existing affection: hand offered then held, no kiss authored.
- `slow`: Leans back looking at wall light, no pulled intimacy.
- `arrange`: Walks to passage, chairs remain; planned wagon work not happening here.


## Completed family reading checkpoint

Konomi: all 75 exported scenes and 644 nodes assessed for visual moments, including exact shared-text reuse and distinct history entries.
Minagho/Chivarro shared continuation: all 47 exported scenes and 218 nodes assessed, including seven exact epilogue text duplicates with separate state gates.
These are manuscript coverage completions, not generated image-set completions or route quality approvals.
Tirabade, Anevia and Irabeth full-family reading is next.
The 37 source/export node variants remain a separate unassessed scope.

## Tirabade early encounters and disclosure

All nodes and choices of these 13 scenes were read, including refusal and disclosure branches.
No image is approved by this text assessment.

### `a_cup`

Optional headquarters tea CG: papers cleared from chair, cold cup, relaxed conversation.
Leg is healed, no perpetual limp.
Bread is only proposed; Irabeth absent.
Flirt and sleeve touch do not earn kiss.

### `i_watch`

Optional report-table CG: repaired gloves, reluctant smile with small tusks, report set aside.
Ear flush and folded hands are restrained attraction; wife anecdote does not put Anevia in room.

### `a_errand`

Distinct burned-bread sharing CG: cloth parcel, dark crust and warm middle, knife, crumb brushed from sleeve.
Previous cup scene has no actual bread.
Recalled marital kiss is not present action.

### `i_hands`

Distinct glove-mending action CG: no gauntlets, healed hand marks retained, threading needle versus repairing sewn-shut thumb, then successful clenched glove and brief forearm touch.
No kiss.

### `a_roof`

Landing above stores, narrow window, stairs and coin trick from worn scarf.
Not an outdoor roof skyline.
Dropped coin and amused distraction merit CG.
Close anticipation remains untouched; honest request steps back to ask wife.

### `i_respite`

Board-game CG with worn grid and button counters.
Irabeth explicitly without sword belt.
Unfinished move and near confession remain without touch; honest request leaves to consult wife.

### `a_crossing`

Separate selected first-kiss CG and optional graphic and explicit night aftermath.
Empty room, papers put away, scarf on chair; latch lowered only for night.
Wife has not agreed.
Stop after kiss is not overnight; honest request and departure get no intimacy image.

### `i_crossing`

Separate selected first-kiss CG: Irabeth bends, hand held and neck touched.
Night variant gloves removed together, lamp out, later seated handhold in darkness.
Gentle branch hand-kiss goodbye is not overnight; refusal and honest request exclude intimate staging.

### `a_morning`

Aftermath CG optional: open headquarters doorway, guarded smile and wrist rubbing.
Tell branch handhold versus both branch hand withdrawn flat on table and bitter laugh need different expressions.
No happy triad.

### `i_morning`

Window-side aftermath CG optional: wedding-ring thumb, drill outside, restraint.
Both branch turns away and asks solitude.
No present kiss; desire discussed does not authorize intimacy image.

### `reckoning`

Priority three-person conflict CG: small table, three chairs, wives face each other and Commander occupies third place.
Irabeth without armor.
Door latch checked.
Wives leave together with distance and no handhold; future possibility is not agreed triad.

### `a_truth`

Solo difficult conversation, untouched cold cup until need branch, no contact at conclusion.
Jealous comparison remains real.
Future three-person possibility must not be painted as completed relationship.
Existing neutral speaker portrait may suffice.

### `i_truth`

Solo steady conversation with fatigue and restrained smile.
End permits offered palm and open handhold; stop fastens glove and leaves distance.
Separate handhold CG optional, no overnight or group assumptions.


## Tirabade agreement, private night and future

All nodes and choices of these seven scenes were read.
Distinct contact states require explicit selection and actual image review.

### `table`

Group milestone: bought loaf and wives holding hands during proposal; accepted room branch earns each woman kissing Commander goodbye in the other presence, no disrobing.
Separate relationships or refusal do not get triad kisses.
Separate_anevia explicitly no farewell kiss; separate_irabeth wife stays after Commander leaves.
Separate_both is two individual relationships, not shared household.

### `ordinary`

Optional group supper action CG: unused setting, bread and note tin.
Practical replaces unreliable note under candle with empty tea tin and lid on.
Angry branch wrist caught while stealing morsel, then morsel given Commander and laughter; anger has not instantly vanished.
Rank_negotiated cup set down hard differs from old secret-affair recollection.
Stop plate pushed away, no cheerful resolution.

### `a_self`

Solo Anevia city-walk CG: joined arms on rough paving, narrow sky between buildings, brief cheek touch only in history branch.
Honey cake and bakery are imagined future, not present props.
End earns doorway kiss after checking obstruction, no secrecy or three-person composition.

### `power`

Reuse conversation scene or speaker portraits for mythic discussion; no new CG per verbal mythic option.
Legend turns warm palm up; dragon squeezes hand, no imposed transformation.
Angel breast symbol and Irabeth green undertone are physical cues.
Knife is expressly metaphorical.
Terms chairs closer versus stop wives shoulder-to-shoulder, no mandatory kiss.

### `future`

Priority shared-life commitment CG: side room with handwritten wishes, not map or requisition.
Yes/yes_negotiated three-person embrace hindered by table, no temple oath or wedding ceremony.
No branch leaves paper and stops hand before contact.
Separate branches exactly reuse table prose with current future-setting state, excluding embrace.

### `shared_night`

Priority earned group intimacy sequence: entry warm room, three cups and plate.
Near wives kiss then invitation hand offered.
Close selected Commander kisses each, Irabeth holds wife, Anevia hand on back then face, lamp turned low.
graphic and explicit fade only.
Quiet chooses cushions and clothed closeness, no sex.
Both reach morning wrist caught and five more minutes, so shared morning must not imply sex or undress.
Familiar recalls selected past nights, not a new dress or map prop tonight.

### `last_watch`

Optional final-watch group farewell CG: seated handhold, fear and brief forehead-to-temple contact, then kisses at end.
Life_broken folded worn-corner travel list shown; other branch discusses list without necessarily holding it.
Scar_unsettled retains anger, no blanket joyful closure.
Queen_letters letters already sent, sleeve crease touched; do not place unsent letters in hand.


## Tirabade travel, separation and distinct endings

Every node and choice in these 12 scenes was read.
These decisions do not treat memories, dreams or wished-for futures as present events.

### `ending_together`

Distinct lasting-household epilogue CG proposed: three permanent chairs, shared meal and successfully baked bread, domestic work set aside.
Old betrayals remain history; preserve private evenings and other attachments.
Review pending; no current image coverage inferred.

### `ending_apart`

Separation ending: wives together without Commander or an empty shared-life place.
Prefer neutral portrait reuse or ordinary quiet married-life composition; no invented reconciliation with Commander.
Review pending.

### `ending_unfinished`

Unsettled ending: no promised triad household, no expectation women wait forever.
Neutral wives portrait reuse or ambiguous separate-life still life, not lasting-household CG.
Review pending.

### `ending_loss`

Loss ending: optional open book and mistakenly set cup still life.
Survivor/death identities unspecified here, so do not invent corpse, death scene or fixed survivor.
Separate review required.

### `ending_ascend`

Ascension ending: table-for-three memory or hope, not proof of corporeal divine visitation, transformed women or ascended joint life.
Reuse an accurately earned table milestone with retrospective framing; new literal reunion CG unsupported.

### `ending_monster`

Relationship lost to Commander transformation.
Neutral distant wives or abandoned-plan still life; no forced affection toward monstrous Commander and no invented species.
Separate ending decision, not happy-image reuse.

### `ending_aeon`

Erased relationship: symbolic empty chair in unreal remembered room optional, explicitly not women remembering Commander or reuniting.
Altered lives unspecified; no mandatory nostalgic expressions.
Separate image review required.

### `i_self`

Priority solo Irabeth reading CG: battered travelers book with loose pages and cloth marker; grand bad verse makes her laugh.
Lake only narrated, not present landscape.
Touch branch hand brought to cheek, eyes closed then kiss; book remains nearby, read branch retrieves it.
No armor mandate or overnight implication.

### `departure`

Group farewell CG with heavy travel pouch: sewing kit, clean cloth, wrapped food and whetstone, no magical charm.
Promise linked hands and embrace; choice-specific farewell kiss possible.
End Anevia straightens Commander collar, retains player-defined appearance; letter private, not public reading.

### `abyss_letter`

Letter still life or neutral Commander framing in Abyss refuge; paper kept folded, never burned or delivered.
Women physically absent; memories may reuse clearly marked earlier CG, not simultaneous reunion.

### `abyss_dream`

Distinct optional dream CG: three-chair impossible room, wrong light and impossible street through window; Anevia inaudible, Irabeth book on knees, empty place across lengthening floor.
Commander never reaches them.
Awake returns to unsent letter, no telepathic conversation.

### `a_waiting`

Anevia alone with Commander while Irabeth absent and safety unresolved.
Tired smile and uneven table tapping; no full reunion image, no assumed death or safe arrival.
Existing sober speaker portrait may suffice.


## Tirabade return and parting

Both complete scenes and their choices were read.

### `return`

Reunion CG must follow actual branch.
Letter reading is shared table with folded worn paper; negotiated_letter puts open page between them.
Future earns sequential welcomed kisses, but scar_quiet and scar_disputed end with wives leaving without reconciliation or kisses.
Disputed collects wife cloak; quiet lamp scraped away from edge, cups left.
Queen has chipped saucer rim turned away, then queen_letters Irabeth writes herself with Commander silently beside, Anevia fetching ink.
Past papers-in-bed anecdote is not present setting.
Separate quiet writing CG recommended; no premature joyous reunion.

### `parting`

Reuse sober table conversation composition with selected expression.
Confirm ends relationship and requests distance, no farewell embrace.
Stay offered hand awaits decision, not mandatory contact.
Separate_* bodies repeat table and future with current side-room context; individual invitations do not become happy triad CG.
No additional intimate image justified.


## Tirabade locks and off-duty outing

Both complete scenes and every choice were read.

### `three_locks`

Distinct courtyard action CG: sheltered corner, small wooden box with three mismatched padlocks, cloth underneath, lantern adjusted by Irabeth and lock tools.
Anevia shoulder contact and finger guidance differ from Irabeth box support.
Opened locks placed on cloth, final sticking lock opened by KEY, not magical skill.
Wives wrist/fingers affection earned, no kiss.
Plans become blank third page and pencil; music/meal are future choices, not simultaneous settings.

### `three_outing`

Priority off-duty date variants.
Irabeth plain shirt and insignia-free coat, Anevia straightens shoulder fold.
Music room crowded, fiddler low platform, drummer, cider kept from elbows.
Wives dance first; selected Irabeth or Anevia dance with Commander versus seated listening require different participants/poses.
Anevia dance ends brief wife kiss, not Commander kiss.
Meal alternative lane window, Irabeth window seat, Anevia door view, Commander third; pie shared and knee contact, no music props.
Long walk linked arm/hand on uneven street versus home door selected kiss OR handhold.
Inside offered hands, no sex or undress implied.


## Tirabade yard, match and private aftermath

All three scenes and their choices were read.

### `three_yard`

Priority casual bowling date CG: nine wooden pins, plank lane with patched board and knot, chalk release line, neighbor fence, different-weight wooden balls, red-cloth pennant initially counter.
Tessa gray braids is incidental adult, not romance redesign.
Straight branch Irabeth leans after ball and Anevia catches back of coat, distinct comic physical action.
Bank has different trajectory.
Date gate wives kiss, Irabeth hand at Anevia waist; Commander not participant in that kiss.
Anevia coat retrieved at exit, not assumed worn during play.

### `three_match`

Same lane reuse with actual match-state variants.
Olva candlemaker and Nessa cook, Perrin gray-bearded cooper; Nessa left-handed slow roll.
Commander scores six; Anevia initial eight disputed at scuffed chalk, no camera claiming foul proven.
Stand wins red pennant, folded into Irabeth coat, subdued disputed victory.
Replay new chalk and clear foot gap gives six, nineteen total, loses pennant; no trophy in losing artwork.
Separate ending expressions required; no cheerful victory applied to both.

### `three_beth_score`

Solo Irabeth bench CG: unfastened practice guards paired, red pressure mark at wrist, twisted lace loosened.
Not armored combat pose.
Hers offered palm; noticed draws Commander hand to knee with ear flush, meaningful attraction.
Pennant is described hanging on chair at home, not held here.
Outcome slides guards UNDERbench; selected kiss stands with hand at back, while walk keeps handhold.
Both retrieve guards at departure.
Kiss and declined-kiss branches need separate assignment.


## Tirabade baking and return match

Both scenes and every choice were read.

### `three_anevia_flour`

Priority baking-action sequence: flour-marked sleeve, stiff dough then wet sticky strand, rear worktable with older Dalia blue apron teaching.
Irabeth absent until share at marital rooms.
Keep dough rise under damp cloth distinct from cleaning cloth dropped in basin; no final loaf before oven.
Same and quick wash fingers before handhold or waist touch.
Shape shares cooled old rolls while loaf rises; baked split seam cooling rack, shoulder contact at open back door.
Leave warm cloth bundle against coat.
Share three plates, wife flour-sleeve held then wives kiss, Commander watching; no fabricated Commander kiss or undress.
Kitchen practice is present, owned future home only imagined.

### `three_return_game`

Bowling-return CG can reuse yard architecture but chalk rule changes: broad marked board rather than thin disputed line, watcher outside lane.
Won history Irabeth returns pennant; lost history Olva returns it.
Line Commander holds straightedge, Irabeth washes chalk, Anevia and Olva mark ends.
Noticed earns Irabeth kissing wife knuckles.
Actual return match LOST in every branch, pennant goes Perrin pocket; Anevia clears remaining two pins only after match.
After cider and bought Dalia rolls, Irabeth brings Anevia hand to cheek.
No winning trophy or claim Anevia baked these rolls.
Invitation map is future prop, not present.


## Tirabade travel planning and stolen road book

Both complete scenes and their choices were read.

### `three_small_journeys`

Priority separate map-planning and earned intimacy CGs.
Cheap traveler map on low table, uneven roads and town pictures, rug, three cups and water jug; garden/boat/market discussed and drawn, not visited.
Near map folded with pencil on SHELF and cups onto table before wives kiss.
Night selected Commander cheek kiss, Anevia linked hand then kiss, Irabeth catches wife wrist and wife returns kiss.
Fire banked and latch checked later; morning blanket over Irabeth ear.
Quiet palms traced with imaginary roads on cushions against couch, Commander leaves same night.
Time adds visible small clock and respects earlier departure.
No night imagery on quiet/time, no spread map during near/night.

### `three_stolen_roads`

Distinct market quest CG: Anevia packet with yellow sash corner remains packed, not worn.
Ista blue travel book red-thread repaired corner, loose garden drawing mill-wheel reverse.
Gresa holds book pending ownership; Ista at wagon mending cover with needle and loosened chest lock.
Secure returns intact book, acknowledgments remain missing.
Watch follows separate stalls and service passage; flight brown-coat seam tears, cart front wheel crushes book, rear wheel stopped before tied papers.
Book broken and mill drawing split only watch branch, no body injury or captured thief invented.
After yellow sash still packet, lantern/music celebration postponed; avoid festive dance image here.


## Tirabade portrait sitting and blue-coat dance practice

Both scenes and every choice were read.

### `three_lantern_debt`

Priority Anevia portrait-sitting action CG: workshop, four paper bird/plover shades, metal lamp cups safely below paper, older Nell paint cuffs and bandaged thumb draws pinned paper.
Anevia turns chair toward door; chin guided for sketch then sideways half-smile captured.
No Irabeth before arrival.
Actual finished sketch side glance and smile, not generic frontal portrait; compare holds sketch beside face then Anevia kisses wife inner wrist.
Private only proposes bedside display, not current bedroom.
Carrying shades in own box with Commander; wives sack ends carry frames/cups separately, drawing rolled canvas inside Irabeth coat.
No lit lantern procession or worn yellow sash yet.

### `three_beth_steps`

Priority distinct blue-coat dance CG and selected solo intimacy variant.
Practice begins coat folded on bench, room cleared and bench moved twice.
Follow hand on Commander shoulder versus lead own count, near collision or boot brush preserve action.
Coat borrowed dark BLUE, plain fastenings, shortened sleeves, purchased only decision not payment here.
Open versus fastened choice affects drape and must persist; no assumption bare torso beneath.
Fastened hem swings around legs and over-shoulder pleased glance into dark window.
Window opens to cool at tessa and closes before ending.
Kiss Irabeth bends then catches warm coat edge while laughing; hold embraces without kiss.
No wife present, no actual fiddler until later event.


## Tirabade consequences and lantern dance

Both complete scenes and all choices were read.

### `three_ista_departure`

Quest consequence CG or reuse wagon-yard speaker view with distinct book state.
Ista and wife Wenna strap folded covers to cart, Commander holds strap only until buckle set.
Receipts branch recovered papers and crushed book blue leather supported between boards, loose stitching, mill halves paper-mended with lost sentence.
Letters branch intact red-stitched blue book but unreplaced acknowledgments delay departure.
Neither is perfect outcome.
Offer new route-copy sheet and steep/easy pencil marks, no actual river excursion.
Ista hands sheet Anevia then Irabeth carries it on return.

### `three_lantern_turn`

Priority established triad dance-event set.
Closed bowling yard, pins STACKED beyond fence and fee board blank, four bird-shade lamps safely mounted.
Anevia yellow sash tied waist; Irabeth bought blue coat, open/turn variants preserve earlier styling.
Gray-haired Veska fiddler and Tessa incidental, not romance subjects.
Coat wives lapel/forehead/corner-mouth then proper kiss.
First wives dance yellow sash against blue coat; Commander watches with cup.
Selected Anevia close versus quick dance, quick sash loose end tucked in BELT after catching.
Irabeth lead/follow dance distinct.
Supper bought Dalia bread, cold meat, pickled roots; wife laugh with mouth full.
Sketch paper compared with living face then ROLLED before kiss.
Quiet group fence closeness differently facing bodies, not implausible identical pose.
Leaving lamps EXTINGUISHED before dismantling, sash folded over arm; returning-home invitation does not itself depict overnight intimacy.


## Tirabade private hearth and false guarantee

Both scenes and all choices were read.
The sash contradiction is recorded for art staging, with no frozen manuscript edit.

### `three_open_road`

Priority earned second private-night sequence.
Irabeth opens door blue coat, warm hearth rug, two maps and walnuts.
After_home versus after_later distinguish prior invitation kept now or later.
Desire sash explicitly across CHAIR, wives kiss as Anevia rises to knees.
Night selected kisses, coat carefully unfastened, later on chair, maps folded, banked fire, shared bed and morning embrace; graphic and explicit depiction only.
Evening selected kisses but Commander own bed, coat stays ON.
Sash continuity HOLD: evening says Anevia loosens sash although desire placed it on chair, with no re-dressing action; avoid literal sash-unfastening CG until source decision.
Company no kisses/sex, shell fished from under rug, shoulder rest and blanket optional.

### `three_borrowed_names`

Investigation table CG optional: loose-button bowl retained, forged guarantee hooked-staff-in-circle merchant wax, wives and Commander plus Ista/Wenna.
Wenna coat initially fastened, unfastens at names.
Recovered has wheel-dirty acknowledgment and DAMAGED book propping papers; missing has INTACT closed book.
No invented official crusade seal.
Private handhold defends relationship without erotic display.
Plan Wenna takes original, Irabeth permitted copy; Anevia fetches coat and briefly kisses wife before leads split.
Evidence exchange not settled account or trial victory.


## Tirabade seal evidence and copyist visit

Both scenes and all choices were read.

### `three_back_of_seal`

Investigation and solo Anevia intimacy CG sequence.
Gresa counter combs/buckles/button jar, scrap examined in slanting awning light, separate clean notes; pencil blunt end NEVER touches fragile scrap.
Successful impression identifies hooked staff broken rim; unreadable admits no name, catalogue full forms from several brokers only.
No universal solved-forgery picture.
After graphite mark behind ear wiped with handkerchief, wagon presses pair to wall and Anevia smooths collar.
Return wife absent, private folded note not read, selected scene ends two kisses and pencil falls from sleeve.
Sleeve storage transition not shown earlier; do not add visible pencil prop to kiss composition without exact moment check.

### `three_beth_account`

Irabeth blue-coat investigation, copyist Ressa broad shoulders silver rings ink fingers, two face-down pages then work record and practice heading.
Record branch cloth-binds unrelated ledger pages; statement branch separate signed sheet dry cover, no stolen whole ledger.
Anevia joins only below stairs then leaves.
Solo handhold beneath projecting roof or quieter passage; future room only described, not visited.
Room branch Commander kisses lowered hand after embarrassed face-covering, not mouth kiss.
Home wife doorway catches OPENblue-coat edge and Irabeth bends into wife kiss, Commander observer.
Later room invitation no automatic overnight assignment.


## Tirabade disputed account and chosen disclosure

Both scenes and every choice were read.

### `three_counterclaim`

Optional evidence-hearing CG at CLOSEDGresa stall, stock moved and Malven square face brushed collar placed to face Ista; not courtroom or arrest.
Recovered original receipts versus replacement confirmations.
Ressa physically present ONLY book branch with protected ledger in lap; signed branch absent.
Linked seal earns fullrefund offer, weak/forms only half; circulate declines immediate coins, no money in Commander hands in any outcome.
No invented proven forger or captured thief.
Leave wives linked hands then Commander as practical solidarity, no victorious kiss demanded.

### `three_unposted_notice`

Domestic consequence visit: Ista undrunk cup, Wenna boot removed with stone through split sole, Anevia leather scrap patch offered.
Refund/half/public retain different money/work consequences; no instant perfect justice.
Saved damaged travel-book gap gets Wenna handwritten new memory; lost intact wrapped book but record missing.
After visitors leave, boot-patch wrapping checked as harmless paper, not discovered proof.
Named chooses future public declaration with handhold; private keeps explanation among lovers, wives fingers/mouth kiss and Commander drawn close.
Arrange wife under-ear kiss and hand kept at waist.
Proposed Tessa narrow bed is not already occupied or selected; invitation does not earn overnight image.


## Tirabade rented room and kept promises

All six scenes and their choices were read.

### `three_rooms_unlocked`

Priority rented-room group sequence.
Tessa upstairs room has wide bed, covered narrow bed, three mismatched chairs, window over emptied yard and leaning washstand; initial lamp on window table.
Told public lovers declaration earns linked hands; untold retains privacy, window opened then wife kiss.
Chosen sash across NARROW BED, wife kisses and blue coat.
Kisses selected each woman with neck/forehead contact, versus hands no Commander kiss.
Sitting low comfortable chair unsuitable for Irabeth, choose other chair; wife knee touch.
Tray branch upstairs hot bowl rescue, Anevia briefly alone or Irabeth landing with Commander.
Meal dishes carried down then lamp low.
Late window CLOSED, sash explicitly RETIED earlier now loosened onto chair, unlike unresolved open_road omission.
Night removes blue coat onto chair, lowers lamp, beneath cover graphic and explicit intimacy; morning wife catches coat sleeve from chair.
Rest no further intimacy, extra blanket from narrow bed, shared sleep with nose beneath wife chin, no stated coat removal.
Walk opencoat, keys returned, optional farewell kisses then Commander own bed.
Shared morning outdoor lane avoids retroactive sex assumption and includes passing-cart separation and repaired hinge.

### `three_choose_days`

Scheduling conversation, optional existing speaker/table reuse.
Short branch explicitly unfinished outings are NOT memories; no CG showing events skipped.
Lamp drawn closer, wives handhold, no new seduction by choosing shortcut.

### `three_more_days`

Resumption conversation can reuse neutral room portrait; Irabeth folds read paper aside, Anevia by chair then arm around waist only yes.
No replay of completed CG claimed as new scene, no new sex or ending.

### `three_kept_days`

Earned ongoing-life milestone CG optional: Irabeth open bluecoat, Anevia collar straightening then handhold; Irabeth playfully straightens Commander collar, wife handkiss, final cheek kiss and planning actual evening.
No resolved thief capture, no forced marriage ceremony or all-party closure.
Reuse suitable affectionate clothed group scene after exact comparison.

### `ending_promised`

Distinct unfinished-promise ending, not settled household.
Reuse actual promise-table image with reflective framing or neutral wives together, no invented home permanently inhabited by three.
Pending separate ending-image review.

### `ending_ascend_promised`

Distinct ascent with unfinished promise: distance and possibility unresolved.
Neutral wives or earlier promise memory, not transformed joint household or worship scene claiming perfect devotion.
Pending separate ending-image review.


## Tirabade negotiated entry and ending variants

All nine scenes and every choice were read.
The complete shared Tirabade family now has 68 scenes assessed; individual Anevia and Irabeth continuations remain separate.
No image approval follows from complete text reading.

### `tirabade.negotiated_table`

Distinct honest-entry supper CG: small HQ side-room table, mismatched cups, covered dish then roasted roots/darkbread/cheese.
Independent relationships already exist; no guilt/deception expressions inherited from original table.
Goodnight wives sleeve-drawn kiss, hand at waist, then each kisses Commander in turn.
Separate/later do not earn group kisses.
Existing table setting can be reused only with food and selected expression/state checked.

### `tirabade.after_local_parting`

Sober side-room conversation after one local refusal, no social props brought.
Separate_* text repeats earlier group table but includes tablecloth not reestablished at this entry; use neutral speaker framing, no invented supper.
No revival of already-refused romance or happy group intimacy image.
Separate_anevia explicitly no farewell kiss.

### `tirabade.negotiated_letter`

Unsent stained paper in Alushinyrra, names cramped beside each other.
Recalled cheese supper not happening now; no physically present wives or delivered letter.
Reuse suitable Abyss letter still life after stain/context review.

### `tirabade.negotiated_ending_together`

Settled three-chair household can share proposed original ending_together domestic composition, but no shame/repaired-betrayal iconography from original history.
Good bread and ordinary shared life; pending image review.

### `tirabade.negotiated_ending_apart`

Marriage persists after shared future ends, no automatic tearful tableau or renewed Commander embrace.
Neutral wives portrait or separate-life composition; distinct from happy household and unfinished hope.

### `tirabade.negotiated_ending_unfinished`

Exact ending_unfinished text reuse; same image constraints.
No settled triad home or waiting obligation.
Candidate compatibility still unreviewed.

### `tirabade.negotiated_ending_loss`

Exact ending_loss text reuse; symbolic open book or set cup, survivor identities unspecified.
No invented death scene.
Candidate compatibility still unreviewed.

### `tirabade.negotiated_ending_monster`

Exact ending_monster text reuse; relationship ended, no forced affection or fixed monstrous form.
Neutral distance/still-life reuse subject to review.

### `tirabade.negotiated_ending_aeon`

Changed-world erasure without affair history: no carried letter or shared invitation occurred.
No remembered Commander love, no literal nostalgia scene.
Neutral altered-life portrait or symbolic absence, pending separate review.


## Anevia independent courtship and spouse conversations

All five complete scenes and their choices were read.

### `anevia.unborrowed_hour`

Priority early solo pear outing CG.
Start repairs wicker basket handle string, foldedcloth and sheathed breadknife, coat fetched.
Market four pears plus fifth split-skin gift, then sunny unremarkable wall no roof or grand skyline.
Damaged pear sliced, juice enlarges cloth stain, relaxed laugh; no Irabeth present.
Watching hands ALMOSTmeet; honest explicitly does NOTtake hand.
No kiss/contact image until later earned.
Wait remaining pear goes wife; friend remaining pear given Commander.
Incidental street children never romance subjects.

### `anevia.a_question_at_home`

Tea conversation can reuse appropriate seated speaker scene.
Two mugs initially too hot then cool, empty teapot refilled together with Commander pot/Anevia mugs.
Useful almost reaches hand then leaves open palm BESIDEmug, no handhold or kiss.
Irabeth only recalled, no happy group composition.
Honest solo courtship possibility is not agreed intimacy.

### `anevia.one_truth`

Affair disclosure scene must remain tense, no flirt image.
Door shut then Anevia moves away without inviting seat.
Account opens window to hear street, coat previously chair retrieved at end.
No touch or resumed secrecy; stop retains hurt/history.
Reuse sober speaker framing rather than unnecessary CG.

### `anevia.beths_question`

Irabeth solo spouse conversation, Anevia explicitly NOTwaitingoutside.
Small room no council table, two chairs window, gloves removed neatly folded, hands knees/lap.
Already_lovers briefly covers Commander hand only established specific history, not generic romance initiation.
Before versus after mood/history differ.
Rank rises retrieves gloves, refused opens door dismisses.
Cardgame recounted, no cards present.
Most branches neutral speaker reuse, no solo-kiss CG.

### `anevia.beths_answer`

Irabeth agreement conversation at end of workday, papers put aside, hand on chairback.
Hurt chair straightening and unresolved anger versus uncertain rueful smile.
No physical romance, no waived past harm, wife absent.
Neutral appropriate portrait reuse pending exact comparison; no new CG required.


## Anevia chosen private invitation

All three complete scenes and their choices were read.

### `anevia.her_own_answer`

Priority independent selected kiss CG: cramped borrowed room oversized table, window not fully close cloth damper, cups/sliced fruit and empty herb box/sandpaper, no plant yet.
Box-work branch sands with cloth catching dust then box on sill; direct start->want skips work so box on table.
Shared kiss crop the box or use actual state variants.
Kiss hand at neck, pleased sound, smiling lips then forehead near and seated knee contact; near deliberate shoulder touch without kiss.
Evening merges kiss/near, hand touch only, no unconditional kiss image.
Stop separate chair and leaves room alone.

### `anevia.a_place_of_our_own`

Established triad solo evening, not courtship reset.
Cramped window room, emptyherb box sill, sandpaper put aside.
Quiet shoulder contact then cheek kiss; ordinary crooked box diagnosed cloth under edge then handhold.
End earned unhurried doorway kiss.
Reuse compatible solo room art after prop/contact review; no wife physically present or erased history.

### `anevia.an_invitation_afterward`

Post-group-change solo invitation in chosen room.
Ended versus declined retain actual histories, no rebuilt triad.
Date box only DESCRIBED and gestured, not necessarily present.
Hand taken then kiss asked with unspecified player answer: avoid unconditional mouth-kiss CG.
Stop folded hands in lap and space.
Seated speaker scene adequate pending review.


## Anevia false inspection and its aftermath

All five scenes and every choice were read.
Ressa the harness repairer is distinct from the shared-route copyist of the same name.

### `anevia.borrowed_signature`

Investigation introduction: Ressa is HARNESS REPAIRER with red wool scarf twice around neck in warm weather, not shared-route copyist Ressa with silver rings.
False inspection paper imitates official mark without being genuine.
Warning discreet folded unsealed versus notice official copied, no witness name published.
Alone recovered reverse impression; kept paper under weight, handhold only outside workroom then later goodbye kiss.
Rescheduled briefkiss at departure and hand released, no false completed date.
Separate incidental identity must not reuse wrong Ressa image.

### `anevia.the_paper_seller`

Paper shop CG optional: Tovra ink-hand, mismatched packets, repaired three-stone rear wall, clear counter and window slantlight.
Cale wet cuffs/blue fingers only witness description, not present.
Perception success reads blue cistern second bell; blurred no reliable address; sorted one-hour stock search yields place not time; uncertain leaves unread.
No universal solved-clue illustration.
Outside short armhold released in narrow passage, no kiss.
Same setting can support multiple evidence states without legible invented text.

### `anevia.the_woman_with_the_basket`

Dema laundry shed leaking roof corner tub, dry baskets, rolled sleeves and blue thumbnail mark.
Help delivers once then returns to work, not confrontation witness.
Blue-covered basket on stool and two occupants known only help report.
Watch outside smoke from sidewindow, no interior view yet.
Approach brief hand squeeze then release; no romantic embrace in operational doorway.
Optional shed action CG or reuse speaker framing.

### `anevia.the_counting_room`

Priority dangerous investigation action CG: unlatched door, desk, blue-cloth basket feet then optional desk, smoldering brazier window, buyer narrow case and side door.
Account basket snatched, cloth comes off and sheets scatter toward heat.
Papers branch Commander saves sheets, Anevia traps Cale hand under rim, single receipt corner scorches and buyer escapes.
Buyer branch Commander blocks exit, Anevia restrains Cale and rescues lists but several receipts burn; Helve identified from case papers.
No gore, weapons invented or demonic conspiracy.
Record opens window after questioning, sealed papers no witness names exposed.
Different consequences require matched action and aftermath props.

### `anevia.what_the_warning_cost`

Consequence-and-romance scene: Ressa letter private names hidden under thumb then put away.
Receipts versus burned retain recovery differences.
Missed selected kiss in wider chair BYWINDOW; trusted chair moved around TABLEcorner, cheek then mouthcorner kiss.
Shared end closerest and planted herb cutting with SOIL and one new leaf, newly acquired since earlier EMPTYbox dates.
Low lamp, pride at leaf, no assumed overnight.
Priority intimate chair image plus growing-herb motif; avoid applying one chair setting to both branches.


## Anevia goat-board evening and departure letter

All three scenes and every choice were read.

### `anevia.the_evening_without_a_case`

Priority solo game and chosen night sequence: six wooden goats, one horn painted wrong side, folded mountain/bridge board with rules on back.
Different from Irabeth grid/button board.
Deciding crooked goat upright beside lamp; seen/different move chair beside Commander, direct desire bypasses these but reaches mutual kiss.
Desire kiss already occurs before night/sleep/leave choice.
Night pieces parcel, crooked goat turned WALL, bed-edge kiss and laughing buckle trouble, wrist caught and knuckles kissed, low lamp and graphic and explicit private night.
Sleep extra blanket, shared bed without further intimacy; leave goodbye kiss and own earlier promise.
Shared morning breakfast bread/cheese/fruit and table handhold works for both night/sleep, no implied nudity.
Game taken away but crooked goat remains lamp.

### `anevia.departure_note`

Priority solo farewell CG optional: small folded page with lower half BLANK, fingers linger, emotion unguarded.
Days cheek touch; end embrace and doorway kiss.
No operational map or charm invented.
Future baking/wife evenings described, not current presence.
Player body not fixed.

### `anevia.the_blank_half`

Letter still life or restrained player framing; Anevia absent, page creases softened, original writing occupies upper part.
Moment/changed fill lower half; memory deliberately NOnew writing.
No sending to Drezen, telepathic reply or actual wife-at-window scene.
Reuse compatible unsent-letter asset only if amount of writing matches selected state.


## Anevia return, lasting key, grief and all endings

All remaining 19 scenes and choices were read.
The independent Anevia family now has all 35 scenes and 176 nodes assessed.
Every ending has an explicit visual decision; none is approved artwork.

### `anevia.the_life_she_lived`

Return/intimate conversation CG: herb has moved to LARGER POT, wooden box now papers/needle case/decorative key opening nothing she owns.
Not future working green-cord key.
Absence handhold, actual written moment/changed page read versus unwritten spoken only; changed fingers kissed.
End mutual kiss and rest while light shifts.
Gardening dirt under nails is recalled, not necessarily on current hands.
No preserved-empty-room assumption.

### `anevia.a_key_that_is_hers`

Priority lasting commitment key CG: working room key GREEN CORD remains hers, yes key table then handhold and kiss.
Key branch copy only promised to be made, no second key handed over.
Invited key beside lamp.
Room cramped hearth, full stone oven only imagined for marital HOME, not built here.
Light clothing-front catch invites closeness; kiss/hold/bread branches distinct, table branch kisses.
End cord catches beneath cup rescued.
Open pockets key before handhold; part keeps key clenched and asks distance.
Prop ambiguity: earlier life scene moves plant larger pot but this entry asks box on sill, do not replace larger plant with old seedling without source decision.

### `anevia.the_last_ordinary_thing`

Final farewell CG with repaired window demonstrated then OPEN.
Crooked goat either given into Commander hand and packed, or remains beside lamp facing board.
Shared future node kisses and cooling tea does not determine goat location.
Expressive near-tears smile permitted, no false heroic grief.
Reuse farewell only with correct selected gift state.

### `anevia.a_grief_with_a_name`

Distinct grief CG: Irabeth deceased, folded personal cloth in hands then lap, cold hearth, fatigue and laugh turning sob at chair memory.
Commander not replacement spouse and no romantic kiss.
Silence handhold only after asking; remain cloth beside chair and later cloak handed at exit.
Part distance, not consolation embrace.
No graphic death depiction or magically healed grief.

### `anevia.ending_kept`

Distinct ending CG decision: Established room and growing seedling/books CG or exact compatible reuse; marriage remains separate living relationship.
No automatic three-person household.
Pending actual image review.

### `anevia.ending_open`

Distinct ending CG decision: Unsettled ongoing visits, game or goat pocket detail suitable; no guaranteed lifetime domestic tableau.
Pending actual image review.

### `anevia.ending_unfinished`

Distinct ending CG decision: Invitation-note composition, not confirmed next visit or settled household.
Pending actual image review.

### `anevia.ending_promised`

Distinct ending CG decision: Green-cord key wound on finger while note composed; lasting promise but lived completion not claimed.
Distinct from fully settled ending.
Pending actual image review.

### `anevia.ending_parted`

Distinct ending CG decision: Sober independent-life portrait or still life; no forced cheerful friendship or lover reunion.
Pending actual image review.

### `anevia.ending_survivor`

Distinct ending CG decision: Irabeth dead, continuing chosen affection with grief.
Cloth remembrance or compassionate quiet company, no wife physically alive or replacing her.
Pending actual image review.

### `anevia.ending_grief_unanswered`

Distinct ending CG decision: Irabeth dead and new visit NOT promised.
Unsent/put-aside message still life, no continued-lover contact presumed.
Pending actual image review.

### `anevia.ending_wife_absent`

Distinct ending CG decision: Irabeth absent, death unestablished.
Neutral uncertainty only, no funeral or grave.
Pending actual image review.

### `anevia.ending_wife_killed`

Distinct ending CG decision: Commander killed Irabeth and romance ends.
No forgiveness or romantic contact; sober Anevia distance, no invented gore.
Pending actual image review.

### `anevia.ending_death`

Distinct ending CG decision: Anevia dead.
Remembered portrait clearly retrospective or ordinary object still life, no new live meeting or invented death scene.
Pending actual image review.

### `anevia.ending_gone`

Distinct ending CG decision: Anevia unavailable, death not established.
Unanswered note or absence composition, no tomb or definite location.
Pending actual image review.

### `anevia.ending_sacrifice`

Distinct ending CG decision: Commander sacrificed, Anevia survives grieving.
Independent grief portrait or empty-place still life, no reunion or grateful saint pose.
Pending actual image review.

### `anevia.ending_changed_power`

Distinct ending CG decision: Ordinary romance ended by transformation.
No possession, forced embrace or invented specific transformed body.
Pending actual image review.

### `anevia.ending_ascended`

Distinct ending CG decision: No automatic divine household or elevated Anevia.
Earlier invitation memory/neutral portrait reuse with explicit uncertainty.
Pending actual image review.

### `anevia.ending_aeon`

Distinct ending CG decision: Private history erased.
No remembered Commander invitation or owed love; neutral changed-life portrait or symbolic unmade invitation.
Pending actual image review.


## Irabeth recitation, seized iron and courtship question

All four scenes and every choice were read.

### `irabeth.a_name_on_the_list`

Priority playful recitation rehearsal CG: six-name list, Irabeth fourth with charcoal crown, no title.
Broad stance, boastful guard versus raised-finger irritated duke, laughing forgotten lines, bow hand over heart.
These are ACTEDroles not real dragon/duke present; no live goat in actual scene.
Later chair creak/scuffed boot, ring glance restrains flirt.
No kiss.
Requisition separate with uneven-wheel wagon sketch introduced only finish.
Distinct expression/body performance over generic soldier portrait.

### `irabeth.the_seized_wagon`

Priority investigation CG at service-yard wagon, straw-packed dark cold-iron bars under cloth.
Brena leather apron, one sleeve rolled and OTHER TIED CLOSED below elbow; preserve actual limb representation, not automatic symmetric hands.
Hadran narrowface officer opposite with order.
Test double stamp versus assay forge, gloves removed only assay.
Success wagon beneath eaves; failed/direct assay spend afternoon, shadowed yard and hinges delayed.
Brena not arrested and no invented corrupt-iron revelation.
Cost sealed intelligence docket only future, no paper already opened.
No intimacy image.

### `irabeth.the_question_outside_duty`

Seated direct attraction, chair moved from desk, ears darken, forearms knees and wedding ring turned.
Wife alive branch WAIT hand settles chair not touching, no kiss.
Bereaved holds ring then widow_yes offered handhold, ring retained.
Gone absence does not prove death or permit romance; no grief-tomb scene.
Refused moves chair back and closes relationship.
Neutral speaker view with mood variants; no unconditional romantic kiss.

### `irabeth.one_truth_to_tell`

Affair confession followup by window, hands sides/frame.
Anevia absent, private future undecided.
Agree relieved/frightened and steps away from door, explicitly NOkiss requested.
Stop standing hurt then window.
Reuse sober speaker portrait; no renewed secret embrace or approved group scene.


## Irabeth spouse answer and practice-room date

Both scenes and all choices were read.

### `irabeth.anevias_answer`

Solo spouse interview with Anevia at drawer/table, drawer key turned then moved, Irabeth explicitly absent.
Asked versus affair and current/past/never lovers histories maintain different expressions, chairs do not become intimate.
Loose cuff thread considered but not pulled.
Yes retrieves drawer key, no lover kiss; refuse stands with scraping chair and opens door.
Neutral speaker reuse suitable subject to actual face/mood review.

### `irabeth.the_evening_she_chose`

Priority independent first date and selected kiss sequence.
Water jug/two cups initial room, then tack-store upper practice room, upright benches wall, window, cushion chair and iron-braced chair.
Key returned downstairs hook after opening, absent upstairs.
Brings participant LIST instead of recital piece; improvised duet laughter then knee near/contact.
Yours asks kiss.
Kiss hand cheek, other hand placed at Commander waist, iron brace CREAK breaks kiss into laughter, then stand at WINDOWSILL to lean and resume kiss/forehead.
Hand branch linked fingers and shoulders seated, no mouth kiss.
End chairs restored, latch checked, brief visible handhold at street.
No generic bedroom or bed introduced; actor roles not actual monster props.


## Irabeth protected evidence, public performance and aftermath

All four scenes and every choice were read.

### `irabeth.a_day_of_our_own`

Existing triad solo-date bridge, not new romance.
Initial book chair moved desk, then storehouse performance space with Dema leaving downstairs.
Guard/duke rehearsal changes posture and voice, no actual beasts.
Desire shoulder and handhold; kiss selected mouth then knuckles interrupt verse, hand branch no mouth kiss.
End outside cheek kiss occurs on both.
Reuse rehearsal art with correct building and empty audience, not actual performance crowd.

### `irabeth.the_sealed_account`

Narrow stores-counting room, open docket with unrelated names COVERED clean sheet, sand from packet, watch purse.
Ordel older beard pale scar cap in hands then table.
Sealed compensation counted with protected evidence, Brena apron keys and purchase extract, no forgiveness implied.
Open relocation occurs FIRST then another day relevant originals read aloud, corrected copy and wagon keys.
Incidental siblings never romantic subjects.
Private doorway sleeve catch released, hand touch, no kiss.
No all-record public disclosure, no Commander coins handout.

### `irabeth.ten_minutes_in_a_hall`

Priority public performance CG: plain DARK SHIRT beneath coat, OPEN throat collar, recital paper LEFT DESK.
Storehouse benches cleared standing space, workclothes audience, soldiers sharing supper and woman mending.
First formal posture then loose shoulders and playful guard/duke acting, awkward delighted bow, no magic dragons or actual duke.
Applause and handhold beneath bench, stay remaining performers.
Outside optional lane walk reflected shop glass versus sheltered doorway conversation; shared kiss_question has different backdrop, use neutral crop or variants.
Kiss selected close hold/cheek-rest, arm alternative flourish and humming only.
Native green face/tusks retained, self-pleased stage expression important.

### `irabeth.the_cost_afterward`

Postcase bench CG optional: two practice swords, split grip separated from sound but worn binding, not combat drawn blades.
Sealed repairs delayed versus open slower investigation and displaced source livelihood.
Own instruction page versus explicit Commander endorsement, no false autograph in unendorsed state.
Direct desire is FUTURE invitation, not present sex.
Gentle offered handhold, end pins separate evening note beside report and leaves swords.
Reuse seated-duty art if exact props matched; no intimate-night image yet.


## Irabeth chosen touch, farewell and present-day return

All five scenes and every choice were read.
The scar branch prohibits face touch and shares later nodes with other histories.

### `irabeth.without_an_account`

Priority solo mature intimacy variants above tack store.
New blanket on WINDOW BENCH, small wrapped loaf, window AJAR, no papers.
Morale expressions differ: broken tired but willing, encouraged fingers kiss, ordinary playful.
Close selected neckhand and other braced bench, open shirt collar CLOTH MOVED from SHOULDER before shoulder kiss, then narrow bench laughter and stand, move AWAY from cool window, hands waist.
Private closes window/latches door, later blanket around shoulders, loose collar and bread heel stolen bite; graphic and explicit private intimacy.
Held closeness then sideways bench beneath blanket and kiss, rest only shoulder embrace with AJARwindow and later lamp for coat, space NOtouch with bread between.
Shared end folding blanket and parting does not establish overnight.
No bed invented.

### `irabeth.after_the_shared_answer`

Separate relationship after triad ends, no reset or covert group restoration.
Bench, wedding ring, palm between then yes familiar handhold and comic recitation.
Stop hands folded, asks departure.
Reuse appropriate sober/pleased speaker portraits; no automatic group kiss or first-date CG.

### `irabeth.before_the_unmapped_road`

Counting-room farewell, hands EMPTY, no provisions or second whetstone actually given.
Handhold and selected embrace+kissing palm versus quiet cheek-close embrace, no overnight.
End comic guard bow then cups gathered; do not confuse with Anevia letter gift or group travel pouch.
Optional solo farewell image with actual empty hands.

### `irabeth.an_unposted_line`

Unsent letter on uneven surface, rank crossed out, no reliable delivery or reply.
Imagined acted answer explicitly memory, not cross-plane communication.
Reuse letter still life with no Irabeth physically present.
Absurd/fear distinct text, same visual setup possible.

### `irabeth.the_person_who_returns`

Window chair reunion with papers aside, distinct older/new/absent/farewell histories.
Returned only selected embrace ORhandhold.
Letter branch worn paper reading then free hand.
Queen guilt remains, no automatic smiling cure.
SCAR specifically forbids FACE TOUCH while moving on; shared ahead/end must not retain hand-on-cheek CG.
Ahead Sella route-maker future invitation, not actual road travel.
End small appointment page with alternatives, no kiss.
Use neutral present-conversation image or matched history variants.


## Irabeth continuation, return correspondence and all endings

All 31 exported Irabeth scenes have now been read, including each selected intimacy and ending branch.
This assesses CG needs, not prose quality, native integration or image acceptance.

### `irabeth.when_the_instruction_is_used`

Workplace portrait reuse is sufficient unless commissioning the secondary review as a quest CG.
Vela has tally, basket and written carrier statement; Pella carries an empty medicine jar.
Three small packets were combined because of wet cloth, with quantity matching, not stolen medicine.
Irabeth stops her raised hand while Vela identifies the missed review time.
Corrected form goes out for copying.
Sealed and open results are reports with different repair and employment costs, not a physical confrontation here.

### `irabeth.a_road_she_would_choose`

Priority playful city walk and selected commitment on arch steps.
Sella works above a provisioner; lake and town drawings are proposed travel, not visited scenery.
Actual practice walk buys TWO onions after a mistaken stair.
Measured route reaches the arch directly; shorter route meets a locked gate and retraces without climbing.
At the steps onions lie between feet and Irabeth leans back on her hands in pale afternoon light.
Lasting branch joins hands and kisses after the response; open holds hands and leans briefly without kiss; friendship folds the map.
Real road copy remains in notebook while exercise is returned.

### `irabeth.the_hour_before_battle`

Priority selected farewell variants at headquarters window, with troublesome chair moved.
Lasting unfolds the road drawing, open folds it between them, friendship puts it away.
Living wife has her own later goodbye; dead wife is remembered through ring and pen story; absent wife is not presumed dead.
Night branch selects kiss, asks for agreement, then latches door and returns for a private hour, followed by clothing straightening.
Hold is an embrace with hand between both of hers; talk remains window conversation.
Do not substitute a bed, wedding or survival guarantee.
Review exact choice gates before assigning an intimacy variant.

### `irabeth.after_the_answer_was_lost`

Quiet grief portrait or explicitly offered hand, not a romantic replacement CG.
Irabeth remains seated with ring on hand at knee and looks toward window before returning to the conversation.
Her wife is dead and absent.
Affair and previously unbegun courtship have distinct histories; an offered hand does not guarantee it is accepted or imply a kiss.
Future recitation and cold iron discussion are not present props.

### `irabeth.return_request`

No character CG required; document still life optional.
Original requisition stays in Drezen and copies are sent only after chosen purpose.
Precise copied correction and uncertain account variants must not both look like proved fraud.
Public request and deliberate investigative trap both admit the personal invitation; put-aside branch sends nothing.
Irabeth is not physically present.

### `irabeth.return_reply`

Letter still life or ordinary portrait UI only, not present speaker illustration.
Reply encloses annotated copy plus second sheet, both signed, second without rank.
Precise and uncertain evidence remain distinct; her corrections include cart number or crossed-out question.
Acceptance arranges one private hour, decline leaves it unarranged.
Neither returns her to duty or establishes romance.

### `irabeth.return_first_words`

Optional restrained reunion table CG, suitable for non-contact branches only.
Irabeth brings copies, no report case, and does not salute.
She lays papers between them and crosses out a line during work; challenge warms her expression without touching.
Company references a forest in a book, not an actual woodland setting.
End she takes her copies and leaves corrected Commander papers behind.
No uniform reinstatement, kiss or revived household is established.

### `irabeth.ending_lasting`

Distinct completed commitment ending CG recommended: an authored journey from Sella drawing now actually taken, with weather and inn disagreements, not a wedding.
Living branch retains marriage to Anevia and permits selected separate or joint visits without declaring a household.
Dead branch keeps grief and notebook without replacing wife; gone branch leaves wife fate uncertain.
Use separate compositions or a neutral Irabeth travel portrait that does not invent spouse presence or absence resolution.
Ring remains part of identity.

### `irabeth.ending_open`

Distinct open relationship ending CG recommended: a temporary visit or road choice without settled household or lifetime exclusivity.
Warmth and postponed invitations are real; marriage loss or absence is unspecified in this node.
Do not add a wedding, fixed shared home or automatic wife cameo.

### `irabeth.ending_friends`

Friendship ending requires non-romantic treatment.
Road drawing may remain as shared history alongside seized wagon and performance memories, but no renewed kiss or promised place on every journey.
A conversational portrait or solitary map decision is suitable; do not reuse lovers embrace.

### `irabeth.ending_unfinished`

No fabricated completed journey or quest achievement.
Optional invitation or restrained portrait with open future, clearly distinct from fulfilled road ending.
Existing chosen affection remains, but an unwalked road cannot be depicted as a shared memory.

### `irabeth.ending_loss`

Separate death and absence decisions required.
Dead branch permits memorial treatment without inventing a death tableau or resurrection; gone branch has no established death, reunion or secret promise.
Empty meeting place or neutral memory portrait can support absence without grave imagery.
No current living embrace for either branch.

### `irabeth.ending_changed`

Distinct separation ending recommended.
Irabeth retains judgment, faith and other loyalties and refuses the transformed Commander.
No submissive demon conversion, compulsory embrace or discarded marriage.
Portrait of firm distance can work without inventing a specific unprovided transformation.

### `irabeth.ending_ascent`

Distinct mortal perspective ending, not a divine couple enthronement.
Irabeth remains faithful to Iomedae and tells an unflattering private story to devotees; no worship of Commander or guaranteed future contact.
Optional amused storyteller portrait with generic listeners, keeping her own life and agency.

### `irabeth.ending_sacrifice`

Distinct bereavement ending: Commander dead, Irabeth alive and continuing her work and choices.
No reunion or foretold sacrifice romance.
A solitary road or private remembrance can depict ongoing life, but props and location beyond manuscript remain authored art interpretation.

### `irabeth.ending_aeon`

Erased-history ending needs symbolic or neutral treatment.
No actual shared memories, reunion or romance owed in rewritten world.
A conventional living-couple ending CG is unsuitable; any visual echo must be explicitly editorial, not an event these characters remember.

## Vellexia picture investigation and chosen first kiss

### `vellexia.second_painter`

Priority magical picture investigation variants, not another generic seated seduction.
Artist waits in entrance hall, frame face down with brass key.
Open back has four catches, silver wire, fingernail-sized pale stone, older shaved panel and paint through crack.
Found branch moves LAST notch to MIDDLE; later painting depicts woman straddling threshold toward almost bare room.
Missed branch white light, Vellexia catches wrist, lift frame upright and older mouth overlaps window, hand overlaps empty chair.
Asked branch no accident, key left in final catch.
Actual Vellexia hair brushes sleeve during examination; no kiss.
Do not reuse previous whole-cup painting as if these new states were identical.

### `vellexia.price_of_novelty`

No additional CG necessary for negotiation if existing actual-speaker portrait fits.
Open frame, thin provenance papers held clear of drink; artist alive in entrance hall.
Earlier damage is repaired in missed variant, doubled mouth gone.
Keep reduces fee, artist leaves, picture stays and she returns with key only.
Return sends wrapped picture and papers away with artist, table then EMPTY.
No torture, transformed artist or retained picture after return.
Future portrait exercise differs by ownership.

### `vellexia.two_observers`

Distinct deep RED fitted dress explicitly specified, opposite chairs and low table clear of drinks and ornaments.
Kept branch painted Vellexia seated alone gains blurred second occupant; real chair moves closer while PAINTED chairs move apart, then frame turned away.
Returned branch NO picture; actual hand pose changes before her chair approaches.
Ordinary moves table aside to clear gap.
Danger offers open palm on her OWN knee, not touched.
No real knife: knife dialogue is metaphor.
Do not render painted blurred Commander as actual participant likeness.

### `vellexia.unadvertised_hour`

Priority character reading/laughter CG in small sitting room, door remains OPEN despite gossip line.
Two cups, book with crowded crossed-out notes and torn paper, she takes chair farthest from door.
Reading uses earnest acted voice then watches over page; alternate leave closes book with marker.
Both bring cup to nearer chair.
Intent knee contact precedes explicit court/slow/company choice.
Court briefly interlaces fingers, no kiss; slow removes knee contact; company draws back.
Costume not restated here, so prior red dress continuity is proposed only, not an independently specified new native costume.

### `vellexia.a_question_kept`

Priority first selected kiss or shoulder companionship CG, not interchangeable.
Book now on SHELF, small bowl of DARK FRUIT replaces it, chairs beside each other.
Answer moves fruit bowl aside.
Kiss_offer hand at Commander collar, waits for approach, deliberate kiss then watchful pause, second kiss and hand opens against theirs; adult mutual moment, no bedroom or undressing.
Close rests shoulder and fingers around wrist without kiss.
Slow offers fruit and retains undecided courtship; company tells past noble story, no physical reenactment.
Painting presence depends on prior keep/return and should not be invented in common framing.

### `vellexia.the_unused_reply`

Priority echo-shell demonstration CG.
Ring tray closes before cabinet visit; moving thread of color belongs to dark ring stone, not every jewel.
Two palm-sized mineral shells with SILVER rims and hinged CLOUDY GLASS covers, not transformed people.
Test places actual Vellexia across room with hand on cabinet while her small face appears in opened shell; closing stops voice and clouds glass.
Both covers must open for conversation.
Accepted shell goes into narrow case with NO ribbon or claiming inscription, her shell stays beside tray.
She removes a pale thread from shoulder, not a kiss or undressing.
Declined/deferred choices do not grant shell ownership.

### `vellexia.the_price_of_tomorrow`

Optional quest table CG with narrow SILK strip bearing written entertainments and two crossed-out entries, not paper scroll.
Retained painting changes from hand suspended over closed book to opening book, then she turns frame away; returned branch empty picture space, never buyback.
Ilveris and Tessar are discussed, absent.
Reply folds silk writing inward, reaches toward case but does NOT touch, offers palm.
Touch joins hands, hand branch explicitly NO kiss; kiss selected touches cheek and kisses, folded silk and CLOSED shell stay table.
Part closes hand and goes to door without contact.
No literal victory, audience performance or prediction demonstration has occurred yet.

### `vellexia.the_second_invitation`

Remote echo-shell CG, not a physically reunited couple.
Initial image accidentally too close shows ONE dark eye, then face as she adjusts distance; folded silk briefly blocks face, then printed questions held near shell.
Former dismissal remains real.
Clerk/copy terms show empty table area before view returns to face, identical terminal text may reuse art.
Refusal stills expression, closes shell and ends correspondence without renewed request.
No kiss, portal or shared room.

### `vellexia.the_claim_before_the_event`

Remote document investigation; three separate sheets shown through shell in turn: dates and sealed packets, predictions, later results.
Tessar initially speaks OUTSIDE glass despite physical presence in Vellexia room; do not show her beside Commander or prematurely inside frame.
Found/missed/ask differ evidence route and extra appointment, not three simultaneous discoveries.
Perfume later addition is proved, Commander prediction is an earlier five-option list, not proved enchanted control.
Method and challenge propose later work; no actual public wager scene yet.

### `vellexia.the_clerks_own_price`

Optional first visible Tessar CG THROUGH shell beside Vellexia table, short dark horns, restrained mouth and leather case beneath hand.
Opens case to annotated sample, most names replaced by marks.
Named closes case after both permissions; limited sets named sample aside to revise, retaining Vellexia perfume permission.
Tessar lowers eyes under threat without removing sample.
No slavery chains or rescue makeover: paid clerk with her own ambitions.
After case clasp and departure, shell brought nearer shows Vellexia alone; duplicate named/limited end may reuse same actual image.

### `vellexia.the_wager_with_an_edge`

Remote proposal with narrow enchanted SILVER circlet beside revised account.
She turns it with ONE finger through it, never wears it on hand.
Publish puts it back inside closed ring tray and cancels demonstration.
Draw/order call Tessar into view for terms; draw lifts circlet toward shell to show joined edges.
No alive jewelry or actual trial performance yet.
A quest prop study is useful; no required fresh CG for every repeated negotiation.

### `vellexia.an_hour_that_counts`

Priority distinct public demonstration, loss and Trickster recollection CGs, all seen REMOTELY.
Published route has NO demonstration: opened purchaser letter, familiar marked play with new crease, amused reading alone.
Wager view has Tessar, THREE witnesses and paid performers; Ilveris ABSENT signed acceptance.
Tiny SILVER mechanical emperor and procession dismantle arch into privy, not real people transformed.
Draw/new choose theater, later emperor becomes door handle; wins retain circlet and refunds, does not buy mechanism.
Quiet chooses unused hour, loses circlet, empty tray compartment then moved away; reaching toward shell stops at distance, no touch.
Fate is voluntary one stored-hour RECOLLECTION within a breath, second light trails first, not world rewind or changed room.
Eyes close, second light goes out, forfeits circlet to Tessar, no cure or second loop.
Preserve these materially different outcomes; no blanket victory CG.

## Vellexia remaining intimacy and distinct endings

All 30 exported scenes and 164 nodes have been read.
The full route does not complete a physical reunion after remote correspondence begins.

### `vellexia.the_question_after_business`

Priority remote lovers declaration, not physical kiss.
She FASTENS earring at start then removes hand from it, leans toward shell and watches directly.
Near adjusts glass distance with mutual laughter; descriptions of kiss remain imagined, NOTHING reaches through.
Desire intimate voice and attentive pauses, gentle rests cheek on own hand listening.
Slow adjusts reflection and discusses earring; company turns head away then back and needs silence.
Do not render proposed kiss, bed or actual arrival as a present event.

### `vellexia.the_voice_after_the_abyss`

Return call separates Commander in Drezen from Vellexia in Abyss.
Lamp glare behind Commander is corrected by turning shell; she turns sharply then composes face.
Lovers raises fingers then lowers them without touching Commander.
Final account in narrow case: published keeps circlet and returns it to case; won explicitly SLIDES circlet onto ONE FINGER here, unlike earlier unworn prop; lost shows empty space and closes case, new design not shown; fate taps CLOSED case and memory is not replayed.
Tessar employment outcomes are narrated, not physically present.
No portal or bodily reunion.

### `vellexia.two_unremarkable_pleasures`

Priority intimate everyday remote CG: Vellexia table crowded with tiny STOPPERED perfume bottles, Commander elsewhere sorting pages.
Inn roof drawing is shown through shell, not shared inn setting.
Keep preserves disliked bottle beside tolerable one; discard removes bottle out of reach.
Chosen UNLABELLED bottle one drop behind ear, sensory descriptions do not transmit scent.
Meeting wish remains unarranged and shell cannot carry bodies; finger to mouth then rests beside shell.
Voice closes chosen bottle and clears others.
Lovers UNFASTENS earring caught in hair, laughs, then imagines future kiss; company has no romantic escalation.
Distinct physical ear/perfume actions can vary pose without undressing or invented kiss.

### `vellexia.the_cover_before_the_battle`

Priority remote farewell variants.
Servant initially removes vase, ordered to discard FLOWERS only, returns EMPTY vase and leaves; she moves vase outside image.
Fingers on silver rim, not cover.
Established lovers/warm and new_lovers describe imagined kisses, not bodily contact.
Quiet rests hand beside shell while Commander separately shows hand on silver, explicitly NO borrowed sensation.
Friends tilts view so EMPTY vase reappears, argumentative laughter.
Slow adjusts lamp reflection; historical balcony/procession not current scene.
Ending withdraws hand then closes cover, no further light; no affectionate farewell image after closure.

### `vellexia.ending_lovers`

Distinct remote lovers ending CG required or explicitly compatible remote reprise.
Continued affectionate calls across separate rooms, earring and singer memories, no body through glass and NO completed physical visit.
Do not manufacture shared bed, domestic household, portal kiss or reformed harmless patron.

### `vellexia.ending_friends`

Friendship ending may reuse engaged remote conversation pose with old play discussion.
No kiss, sensual lover gaze assumed or physical reunion.
Sharp amused disagreement remains, no newly kind patron makeover.

### `vellexia.ending_slow`

Unpromised companionship ending: remote conversation and shared jokes, neither guaranteed eventual romance nor faithful waiting.
Reuse non-contact conversational shell variant if expression fits; no lovers tableau.

### `vellexia.ending_interrupted`

Closed or inactive shell still life, not a fulfilled meeting or proof of death.
Earlier affection remains only as actually selected.
Material wording calls cover silver here, while introduction specifies cloudy glass cover and silver rim; retain established construction and flag wording discrepancy for future review, not source edit.

### `vellexia.ending_closed`

Distinct chosen closure: shell can remain closed while Vellexia privately recalls a play line and laughs.
No renewed incoming signal or reconciliation.
A closed-shell composition differs from active lovers call even if she remembers pleasure.

### `vellexia.ending_dead`

Memorial or silent shell, no responding ghost or woman trapped inside.
Vellexia died; death tableau specifics not supplied.
Keep actual cruel and witty character in optional clearly editorial remembrance, not purified portrait.

### `vellexia.ending_mirror`

Distinct mirror-transformation ending needs review against actual native transformation evidence before literal mirror design.
Shell does NOT restore or contain her; no answering voice, chosen transformation or promise of rescue.
Symbolic silent shell with mirror motif is interpretation, not established exact prop placement.

### `vellexia.ending_coercion`

Coercion ends this freely chosen correspondence.
No willing lovers image or frightened surrender eroticized as continuation.
Closed shell or distant unresponsive portrait fits scope; specific domination tableau is not described and would require separate evidence.

### `vellexia.ending_hostility`

Hostile interruption, not established death or safe unchanged hostess.
No resumed invitation or affectionate call.
Neutral dark shell/ruptured correspondence treatment without invented combat wounds or battle outcome.

### `vellexia.ending_changed`

Altered Commander has no renewed agreement.
Inactive shell or distance motif, not guaranteed acceptance of new form or demon couple.
Exact transformed body unspecified in text.

### `vellexia.ending_ascent`

Distinct unanswered divine-distance ending.
Vellexia dismisses messenger after unanswered question, retains shell without recorded answer from god.
Could depict her skeptical attention and silent shell; no divine embrace, prayer or ascended couple throne.

### `vellexia.ending_sacrifice`

Priority grief CG: Commander dead, Vellexia alone opens long-closed shell, hears ONLY fingernail on rim, then closes before anyone enters.
No spirit image, answering voice or happy reunion.
Visitor dismissed earlier and later recalled is not present in this private moment.
Express resentful grief without removing her vanity and identity.

### `vellexia.ending_aeon`

Erased history: no unchanged shell gift, prediction quest or remembered lover in new world.
Symbolic editorial treatment or no new literal scene CG; never show actual remembered call or owed relationship.

## Aranka rehearsal, disputed song and performance

### `aranka.where_the_breath_goes`

Priority outdoor grass rehearsal and later private singing lesson.
Sella boot keeps time, closes one eye at hard note; bearded Rovan has two smooth percussion sticks and initially other hand folded near chest, not a singer cured by romance.
Heard aligns breath, knee knock; missed strains Sella voice, gives last flask water, shortened rehearsal and she leaves before Rovan talk; separate rebuilds slowly.
Rovan drops stick and returns theatrical crawl; three later Rovan passages identical.
Lesson after others leave puts TWO fingers at Commander side to feel breath, lifts them then later straightens collar; no new kiss on page.
Three lesson variants identical and may reuse.
Distinguish this singer Sella from Irabeth travel adviser without asserting same identity.

### `aranka.the_name_missing`

Serious island grass conversation, Neris grips folded CLOAK with pale knuckles and refolds it.
RED gate and BLUE scarf belong to disputed remembered Deren story, not current costume or physical rescue.
Brother absent with unknown fate, no heroic death tableau.
Neris leaves before Aranka rubs face with both hands and experiments with song endings.
Door ending takes Commander hand between both and kisses fingers; answers leans close then cheek brush.
Song house doorway is lyric, not actual scene backdrop.
Neris does not thank or forgive on command.

### `aranka.an_evening_uncommanded`

Priority performance CG with actual crowd and selected Commander participation, plus opening hand-catch kiss witnessed by Sella and percussion joke.
Grass/wind island, no invented concert hall or raised stage.
Heard has extra comic verse; missed rests voice, shorter upper part/repeat; patient accommodates breath.
Circle draws crowd, rounds begins small groups but recognition interrupts both.
Welcomed seated brief introduction retains audience; ceremony speech loses listeners and drops Sella separate solo, Aranka hands move nervously on SKIRT; step_aside deliberately smaller listening crowd.
Sing has wrist brush and four performers; listen keeps Commander among listeners, do not put them singing onstage.
Door ending unresolved chord then shoulder trail; answers includes mule NAME, not necessarily actual mule, flushed delighted Aranka briefly takes hand.
Neris presence explicitly UNKNOWN, no identifiable grateful cameo.
Repeated part/sing/listen/door/answers text can reuse with crowd/participation gates; not 29 fresh images.
