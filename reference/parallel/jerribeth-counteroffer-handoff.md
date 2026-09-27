# Jerribeth counteroffer contribution

Delivered six optional scenes in `storylines/jerribeth_counteroffer.py`.
The contribution is unexported and awaits independent literary, canon and technical review.
I changed only that new module and this handoff.
No installed files, shared exporter, engine or permanent tests were changed.

## Revisions read and delivered

| File | SHA256 |
| --- | --- |
| Delivered `storylines/jerribeth_counteroffer.py` | `0C9FCE9B9521EAFF98006D7DB9E7A98AB3E6ACAC94C4A87806B8B3600433E3CD` |
| Existing `storylines/jerribeth.py` | `F607D73B030A2640A809081E53022938E62FF3FEBA4C66001BC485AC41FDD03B` |
| Existing `storylines/jerribeth_consequences.py` | `F91B1B0CA826F19B6A0077CBF069DABF6B6D40F98CBAACB08146FF91EBB3DB71` |
| Native text `reference/canon-review/jerribeth.txt` | `B36211563435BF63F3B72CFA57BD67927270F5EC75313A3E78C809184B8155F8` |
| Native mechanical examples `reference/canon-review/native-romance-check-examples.json` | `0B66843385534A9B5F7BDB88D078131FE917306FD939DACEF36C123E81CCEB95` |

The independent consequences writing review and canon rereview were read alongside both existing story modules, correspondence predicates, native skill-check authoring handoff, and EXPANSION gameplay requirements.
This arc addresses their requests for an active adversary, dangerous invention, played consequences, less repeated negotiation about intimacy, and a later use for the optional exposed-illusion study.
No earlier review score is transferred to these new scenes.

## Canon and authored additions

Jerribeth is an oolioddroo, not a glabrezu.
The installed `World/Dialogs/c3/IvorySanctum/JerribethGreetings/Cue_0045.jbp`, GUID `93dfa9597191a6848b925d964d309fe4`, explicitly names her species.
The assignment's glabrezu wording was corrected with the parent before authoring.
Greetings/Cue_0001, GUID `8a632a5249b3c2541a1381111cae9e37`, supports the narrow silhouette, antennae, linked hands and high mental voice.
Greetings/Cue_0017, GUID `3fc161cba43a0ec49b2a86e4d8cfa259`, supports her self-interested allegiance and refusal to treat demonic loyalty as a virtue.
Greetings/Cue_0019, GUID `e47232b2878eff849ac002d2f323cbad`, supports her interest in preserving an enemy as a possession rather than merely defeating him.
These are characterization references, not predicates proving that every Commander heard those particular explanations.
The new common dialogue does not assert knowledge of native Xanthir, Marhevok, Wintersun victims or Vellexia outcomes.

Vardess is an authored adult cambion patron who purchases other artists' work and tries to exhibit an obedient counterfeit Commander and Jerribeth.
Serit is an authored adult tiefling scenery maker who helped build the concealed recorder willingly and now wants payment and release from an unfavorable agreement.
Neither is a native NPC, companion, restored victim, or newly discovered relative.
The theater, recorder, employment agreement, catalogue, patron correspondence and their consequences are authored fiction.
They do not create inventory items, a native debt system, a spawned area encounter, living puppets, soul capture or mind control.
The device retains stage movements and substitutes miniature figures, not private thoughts or genuine consent.

Jerribeth enjoys humiliation, considers retaining financial leverage over Serit, and still wants useful names and profitable work.
The Commander can object, value the less obedient artisan, or enjoy the hostile performance while insisting that the actual bargain be honored.
The public-account outcome costs invitations and subjects her own work to inspection.
The private-catalogue outcome provides contacts while explicitly leaving Vardess able to finish the concealed recording room.
Neither outcome forgives native victims, redeems her general conduct, or reverses an existing native quest result.

## Integration and progression

The parent can import `jerribeth_counteroffer` and append its `SCENES` after `jerribeth_consequences.SCENES` in the development export.
Existing scene IDs and choice indices were not edited.
All six scenes require `jerribeth.consequences_kept`, `jerribeth.terms` and `jerribeth.lovers`.
All are Remote, Optional, chapter 3/4/5, and restricted to the same Drezen and Nexus area GUIDs as the existing correspondence route.
All explicitly forbid `jerribeth.closed`, `jerribeth.unavailable` and `jerribeth.farewell`.
The relationship definition separately retains the native unavailability guard.
No new relationship definition or native alias is needed.

| Scene suffix | Additional prerequisite | Completion effect | Delay |
| --- | --- | --- | --- |
| counterfeit_guest | None | counter_invited | 24 hours |
| counterfeit_hinge | counter_invited | counter_mechanism_known | 24 hours |
| counterfeit_clerk | counter_mechanism_known | counter_clerk_dealt | 24 hours |
| counterfeit_audience | counter_clerk_dealt | counter_audience_done | 48 hours |
| counterfeit_spoil | counter_audience_done | counter_spoils_settled | 24 hours |
| counterfeit_after | counter_spoils_settled | counteroffer_kept | 24 hours |

All suffixes in this table belong to the `jerribeth.` namespace.
The engine also records completed scene IDs.
Choice effects use only newly introduced `jerribeth.counter*` flags.
The module never writes commitment, closed state, another romance, a native quest or a recovery flag.
The existing future, ordinary and farewell sequence can still bypass this contribution.
Do not claim that its completion is already enforced by the campaign or reflected in existing ending variants.

Earlier corrected-sale and withdrawn-sale histories have distinct optional questions about the previous purchaser.
The answer refuses to invent evidence connecting her to Vardess.
The `judges_actions` stance has a specific entry exchange.
The actual `sun_exposed` study opens an earned non-roll investigation method.
Committed history has a reaffirmation without overwriting its flag.
Uncommitted history can request another evening without silently committing.
`fate_terms` permits a callback that explicitly leaves physical access unresolved.
No exclusivity checks, jealousy penalties, other-lover removals or ToyBox setting changes were introduced.

## Played mechanics and consequences

`counterfeit_hinge/start` offers a native `SkillPerception`, DC 25, CommanderOnly check.
It reads visible seams through the charm and instructs Jerribeth where to open the miniature.
It is not a remote touch, spell cast through the frame, check to read her thoughts, or affection test.
The native comparison is Camellia/GiveMeAnIdea/Check_0002, GUID `19972884601e0284b992233e41d778a8`, whose installed data has visible SkillPerception DC 25.
DC 25 is an authored difficulty for a deliberately disguised miniature catch in a route accessible from chapter 3, not an automatic chapter-scaled DC or a copied success probability.
This check is intended to remain easier for a well-developed later Commander.

Success reaches `found`, preserving the strip and setting `counter_cache_intact` only on that outcome's continuing answer.
Failure reaches `missed`, tears the strip and sets `counter_cache_broken` only on its continuing answer.
The check answer has no attempt effects and does not complete the scene.
Intact evidence enables testimony about the mechanism.
Damaged evidence instead requires Serit's retained rehearsal if the player wants him present at the confrontation.
That branch has a distinct replay with Vardess caught in his own rehearsal.
Either history can instead take the final drawings and keep Serit out of the confrontation.
The actual downstream pages and flags differ; failure does not close romance or remove the later quiet/intimate choices.

The patient non-roll method removes the stage underside destructively while preserving the strip.
It sets `counter_stage_cut`, with its immediate cost described on that page.
That flag currently has no additional later penalty; do not credit one.
The `sun_exposed` method reverses the audience's viewing angle, preserves the strip without that destruction, and records `counter_study_used`.
The prior optional study thereby changes an available investigation approach instead of merely receiving a compliment.

The clerk can witness the evidence, bring the rehearsal after failure, or deliver drawings and leave before Vardess arrives.
His agreement can be returned immediately when the exchange is settled or held until the listed adjustments are demonstrated, then destroyed.
The follow-up shows the corresponding return or burning scene.
The final confrontation trades either for a signed account of the concealed recorder or for the catalogue and private silence.
The next scene reports distinct invitation losses/inspection or commercial access/continued danger.
Both settlements return the working adjustments, so neither is described as physically destroying Vardess's future room.

The last scene offers own-form or knowingly invented adult guise, desired graphic and explicit imagining or quiet company, and voluntary continuation.
The closer branch explicitly concerns an arrival imagined together, not a physical visit.
No intimate choice depends on passing the roll or choosing a particular settlement.

## Contact and delivery limits

The existing invited charm continues to transmit chosen images and spoken thoughts between Jerribeth and the Commander.
Vardess and Serit remain physically on Jerribeth's side.
She explicitly repeats their words through the charm and repeats the Commander's selected answers aloud to them.
The text grants neither guest direct access to the Commander's mind and creates no new multiparty channel.
The scene at her table is authored book staging, not a live spawned guest or a new native dialog attachment.
The Commander can be in Drezen or the Nexus without teleporting to that table.

These scenes contain a native check schema and consequential narrative choices but remain rest-delivered remote books.
They do not satisfy the requirement for complete original-style acquisition gameplay on their own.
The existing met-cue/charm invitation still supplies discovery; there is no new map object, courier unit, inspection interaction, inventory reward or native quest event in this contribution.
A later integration could make finding the construction sheet and confronting the patron physical opportunities, but would first need verified contact predicates, locations, props, actor survival, interruption handling and compatible save state.
No such physical feature is claimed here.

The current `Rules.Available` handles chapter, area, prerequisite delays, closure and native unavailability on entry.
`Rules.ContactAvailable` returns true when ContactUnit is null, as it is for these remote scenes.
Consequently this authoring does not establish continuous native-death or hostility rechecking inside an already-open remote book.
The parent's native contact interruption work must not be credited to this scene type without a separate engine review.
Live interruptions, queued rest events and same-save construction indices still need production and game verification.

Art can use the existing Jerribeth portrait and Jerribeth-Guise key where explicitly selected.
The guise page chooses an invented adult elf and preserves the visible shimmer.
Potential scene art is the disassembled miniature and two separate sides of the charm, or the impossible city behind Jerribeth's own form.
Do not depict a physical Commander/Jerribeth embrace or invent a glabrezu body.
Vardess and Serit have written adult descriptions but no generated portraits, guest assets, crops or art approval.

## Checks performed

Read-only imports used Python with `-B`.
The project inventory function reports 6 scenes, 60 nodes, 8,134 raw words, 7,118 prose words, 1,016 choice words, and 8,127 distinct-segment words.
Exact whole-segment repetition accounts for 7 words.
This is a volume measurement, not a semantic originality or literary score.

A read-only graph walk covered 48 seed histories: corrected/withdrawn sale, judges_actions absent/present, sun_exposed absent/present, and uncommitted/committed/committed with prior fate_terms.
It reached all 60 nodes, both native-check destinations, 181,416 traversed eligible transitions and 16,128 distinct terminal flag states.
The walk merged equivalent final flag states while retaining minimum and maximum selected-path word counts, avoiding repeated narration-only branches in later stages.
A completed selected path contains 4,985 to 5,546 words using the project's tokenizer and counting the actually selected answer at each page.
Aborts were excluded from completed-path totals.
The first uncached exploratory walk was interrupted for inefficiency; the reported results are from the completed cached walk, which ran in about 1.5 seconds.

Assertions checked target existence, every page's reachability, an eligible continuation on each visited page, exact skill/DC/actor policy, absent pre-roll effects, mutually exclusive intact/broken evidence, exactly one clerk arrangement, exactly one settlement and exactly one agreement disposition.
They also checked preservation of an unrelated romance sentinel and the final counteroffer_kept effect.
A separate static check traced prerequisites to actual existing scene/choice flags, verified chapter/area/remote/optional declarations and explicit closure/unavailability/farewell guards, and confirmed no Revive action.
The graph simulation does not exercise native probability, Unity rolls, RuleStatCheck, shown-DC UI, managed blueprint construction, real saves, ToyBox or portraits.
The parent should add focused production-rule tests and run the existing export, native binding and managed construction checks after independent review.

## Remaining full-route work

The three Jerribeth modules together now measure 29 scenes, 18,080 raw words and 18,038 distinct-segment words.
They remain at least 2,962 distinct-segment words below the current 21,000-word planning floor, before semantic duplication and campaign-depth review.
That subtraction is not a prescription to add filler.
The route needs consequential full-campaign continuation and ending reactivity to the actual chosen settlement, with enough played development to justify its relationship outcomes.
The present optional chain can be bypassed by the older abbreviated future and farewell sequence.
An attained Trickster recovery/contact route, appropriate other-path access rules, native survival and hostility coverage, physical meetings if pursued, and broader acquisition gameplay remain unfinished.
The final fate callback states an intention and an unresolved cost, not implemented restoration or an attainable new door.
Art, independent scores above 90 in every required discipline, production integration, real game/save testing and ToyBox verification remain outstanding.
This contribution has no author-assigned review score or full-route readiness approval.
