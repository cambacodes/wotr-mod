# Devarra main-campaign delivery audit

All DLC installed is the user's intended baseline, and the user explicitly authorizes DLC dialogue dependencies and flexible handling of actual completed history.
The DLC encounter is a valid route entry when the active or explicitly imported history establishes that it occurred.
The manuscript has enough selected content, but that valid DLC entry cannot simply be registered as a chapter-five main-campaign route without a transfer and actor-delivery contract.
It requires two facts which the addon does not produce: a living confirmed Devarra and a witnessed DLC1 brood conversation.
The main-campaign route needs a proven transfer from an encountered DLC state or its own restoration or living-contact introduction when that encounter has not occurred.
Do not manufacture DLC cue history to satisfy the existing guards.

## Inspected evidence

Inspected frozen opening `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455` and progression `D859C177BD433FD5192A068EB4383BD7E0B9F3FB404382EF9F0D49B5DAB337AE`.
I read `reference/canon-review/female-dragon-roster.md` and the retained Devarra native-art provenance.
I then inspected the actual installed `blueprints.zip`, including egg outcomes, projects, main death markers, DLC speaker cues and unit identities.
Project meanings were checked against installed `Wrath_Data/StreamingAssets/Localization/enGB.json`, not inferred from internal filenames alone.
No source, native flag, blueprint or image was changed.

## DLC availability, active campaign and actual import

The latest user clarification makes DLC content an authorized dependency, not a reason to reject this route.
Missing encounter history still needs different treatment from missing installed content.
I freshly decompiled the installed availability conditions, reward classes, `DlcSaveImporter` and relevant `SaveImportSettings` methods, and inspected both native campaign import definitions.

| Native DLC object | Exact ID |
| --- | --- |
| DLC/DLC1/Dlc1 | `8576a633c8fe4ce78530b55c1f0d14e5` |
| DLC1 campaign reward | `313fb87e4c0143bd84b3fc997c3c2266` |
| DLC1 campaign | `d79943b9b59b446ea5bfc14fa4005b26` |
| Main campaign | `fd2e11ebb8a14d6599450fc27f03486a` |
| Main-campaign DLC1_SaveImport etude | `31417683088d40b8beb3691c393fb3d3` |

`Kingmaker.Designers.EventConditionActionSystem.Conditions.IsDLCEnabled.CheckCondition` returns the selected `BlueprintDlcReward.IsAvailable`.
`BlueprintDlcReward.GetIsAvailable` checks whether any containing `BlueprintDlc.IsAvailable` is true.
The DLC1 reward references its campaign and marks itself required in saves when used.
Use that native availability API rather than merely finding a blueprint in the archive.

`IsDlcActive.CheckCondition` instead checks membership in `Game.Instance.Player.UsedDlcRewards` or `ClaimedDlcRewards`.
That establishes playthrough reward usage, not a visited tower, finished DLC or witnessed Devarra line.
Check `Game.Instance.Player.Campaign` against the DLC1 campaign for active DLC context, and inspect actual cue/etude history for the encounter.
Neither availability nor active-reward membership can stand in for those facts.

`DLC/DLC1/Dlc1Campaign.jbp` is explicitly `IsMainGameContent=false`.
Its main-to-DLC import is NewGameOnly and imports the main character, companions, inventory, gold, date, quests and all etudes.
This gives a concrete reason that the DLC Devarra branch can react to the imported main campaign's eggs.
It does not describe the reverse transfer of a restored dragon into Drezen.

The reverse settings are in `DLC/MainGame/MainCampaign.jbp`.
Its DLC1 import is allowed after new game but sets `m_MainCharacter`, `m_Companions`, `m_CustomCompanions`, `m_Pets`, `m_Inventory`, `m_Gold`, `m_Date`, `m_Quests`, `m_ShownCues` and `m_SelectedAnswers` all false.
It sets `AllEtudes=false`, imports no flags and has no OnImport actions.
Only five named etudes are imported: `7d585a189a8549b99516064e502297f5`, `b9bbbbc2a0a44d9686eb7d45061698cf`, `b8482466105d40ccba48e1f19de02f18`, `0c418cb0cb014e37a4722b40d40bd659` and `91a7fa8a80fa44adbaab98d8b466bd86`.
None of these is the inspected brood-state, main death or DLC Devarra-death identifier.
Their individual reward meanings were not needed to establish this limited import boundary and are not inferred here.

The decompiled `SaveImportSettings.DoImport` copies shown cues only when `ShownCues` is true and selected answers only when `SelectedAnswers` is true.
It records the imported campaign and used DLC reward separately.
Thus native DLC reward import is not a return of Devarra's dialogue history or physical actor to the main save.
This is an inspected implementation fact, not an assumption that the game has no DLC import mechanism.

The DLC1_SaveImport etude invokes native `ImportSave` for the DLC1 campaign, allowing player choice and automatic selection when only one save qualifies, with deferred import.
`DlcSaveImporter.GetSavesForImport` accepts saves of the specified campaign whose type is `SaveInfo.SaveType.ForImport`, and returns no candidates when the campaign reward is unavailable.
`OfferToImportSaves` also checks the current campaign's import settings and whether that campaign was already imported.
Do not treat an arbitrary latest DLC save or the mere existence of a ForImport file as proof of the matching Commander's completed Devarra interaction.

The flexible contract should distinguish these cases.

| Actual state | Valid route handling |
| --- | --- |
| All DLC available; active DLC1 save; matching brood cue actually seen; living Devarra actor confirmed | Preserve and use the native DLC conversation as the opening's legitimate prior event |
| Active DLC1 save before Devarra's encounter | Offer the route after the real encounter, without pre-setting its history |
| Main save with ordinary DLC1 reward import | Treat imported rewards as rewards; do not infer imported Devarra cue history or a restored actor |
| Main save with an explicitly verified matching completed DLC encounter imported by a future addon bridge | Permit a provenance-recorded DLC-aware introduction, after authored chronology and main actor delivery are established |
| Main save without that encounter | Use the separately authored main-campaign discovery/restoration introduction and fresh history acknowledgment |
| Contradictory brood outcomes or unrelated DLC completion save | Do not silently merge histories; retain the current save's facts and expose the conflict for resolution |

A future addon bridge may legitimately read the selected matching DLC completion and record its own narrow provenance marker.
That marker must state what was verified instead of forging native ShownCues in a save which never received them.
The bridge needs an explicit account of how this Commander gains that knowledge and how Devarra gains a usable body or presence in this campaign.
No such bridge or return lifecycle was executed in this audit.
The user's DLC authorization permits building it; it does not mean the native limited reward importer already implements it.

## Verified history bindings

| Native fact | Exact ID | Evidence and limitation |
| --- | --- | --- |
| Main lair dragon death, RedDragonDead | `581521b398fb9dd4eb52bbfffb3b5c43` | Etude under Chapter03_Extra/WormWoundLair; starting it also marks a global-map location explored |
| Ivory Sanctum death, RedDragonKilledInIvorySanctum | `056ba61e04cca104a9c95ac2d4658c67` | Separate Greybor DragonHunt_Q1 state |
| Eggs released | `4ba6fd446353825459f469fe5973fd87` | Native DLC gratitude tests this etude Playing |
| Eggs destroyed | `b0c1344ae8267c94998ca27ad4288c01` | Positive main-campaign loss marker with actual dialogue action producers |
| Egg projects acquired | `02ea801d75381dd48ae15c6c93c5f1dc` | Starts both offered projects, not proof that either has resolved |
| Dragons in Care project | `4aa538f07bd542f7a013b90464577d67` | Native DLC gratitude also accepts KingdomProjectIsDone for this project |
| DragonsInEducationFinished | `e4374a1783c74f68ae46bb5db22e0c58` | Started by the inspected project's successful resolution branch |
| Omelet Innovation project | `88f12bba35004a648023938699769380` | Localized resolution says the woundwyrm eggs fed Drezen |
| UnprecedentedOmeletFinished | `a9a453f695924f99b4326f60b7c3753e` | Started by the inspected omelet project's successful resolution branch |
| DLC battle death, Devarra_dead | `d713e8b772484376a7da810c37ab7922` | Distinct DLC state, not the main hunt's death marker |

The newly located DragonEggsDestroyed marker fills a concrete evidence gap in the opening's current `NATIVE` dictionary.
Its producers include `World/Dialogs/c3/IvorySanctum/DragonEggs/Cue_0006.jbp`, GUID `757a3b2e19b4f8f4d8d438ba15db1d76`, whose OnShow starts it after playing the native cutscene.
`Golems_DragonEggs/Cue_0018.jbp`, `2a5f2604a0ae15841a13a76e6200d030`, and `Cue_0026.jbp`, `e6cbfe0a914eb094d8c42760a17f1fef`, start it in OnStop.
These are positive recorded destructive outcomes, unlike the mere absence of a saved marker.

The two project success branches remove the alternative project, but the project-acquisition etude starts both offers.
Pending projects therefore cannot classify brood survival.
The inspected project data also contains another resolution branch which starts `515c8ad2278f40ba98634b8a40e8936c` for either project.
I did not establish that branch's meaning as a saved/lost result and do not recommend treating it as either without further inspection.
Mirror the DLC's exact released-etude or completed-care-project predicate for saved status, and test the positive destroyed/finished-omelet paths for lost status.
If imported or edited saves report contradictory outcomes, stop classification and report the inconsistency rather than silently select one history.
Unresolved eggs should remain unresolved until a genuine native or separately authored outcome exists.

## DLC evidence is not a main-campaign actor

The native DLC cues are under `World/Dialogs/DLC1_Megaepic/StorytellersTower/Chaleb/`.
`Cue_27`, `8c53478782244b90a37f727f7b814318`, uses an Or condition between eggs released Playing and completed care project.
`Cue_0006`, `d368680393304b5ba324dd5a517140ed`, has no conditions and supplies the alternative accusation.
Both address the same native answer list `29806be2fb3641f48f18b8c7b56a45e3` and name DLC speaker unit `1b7f42d9cfbd424fb31a8186520c29d0`.
The fallback cue by itself is not a positive proof that every main-campaign player destroyed the eggs.

| Actor or location | Exact ID | Verified role |
| --- | --- | --- |
| WoundWormsLair_BlackDragon | `c540d81c08822c14da75761493427e4c` | Main lair unit identity and prototype for related variants |
| RedDragon_Sanctum | `b01da68dab56e004f952d7ad0e83cc46` | Main Ivory Sanctum unit, female and Huge in inspected data |
| DLC1_WoundWormsLair_BlackDragon | `1b7f42d9cfbd424fb31a8186520c29d0` | Separate DLC actor used by the tower dialogue |
| QA unused RedDragon_Sanctum 1 | `c4b5746d3d2511441ba18a894cecb328` | Explicit QA/Unused path, not a released friendly-contact solution |
| WoundWormsLair area | `362dacd5490050b45aa6828c65a7d4c4` | Main campaign area candidate for a return expedition |
| WoundWormsLair_Enter | `5b7505de49cc1aa499731ef0c7e5d574` | Native entry-point identity, not verified chapter-five safe travel |

The misleading BlackDragon filenames do not turn the red Devarra depiction into an identified black-dragon romance candidate.
Unit prototype links and the actual named speaker chain matter more than a filename.
The Sanctum unit's inspected portrait is `271d1a7d87784d37ae42961732ec3cc3` and its prefab reference is `5fba5621d6504284396ec039875dc148`.
Those identify art/model resources; they do not make a dead unit alive or a hostile encounter peacefully reusable.

No inspected native action transfers the DLC unit into the chapter-five main campaign.
The DLC's living conversation supplies characterization and history evidence, not a verified main-campaign resurrection.
Do not spawn its battle actor in Drezen and declare the missing identity and chronology settled.
Do not clear either main death etude, which would alter hunt history and possibly re-enable native attack consumers.

## Why the current manuscript blocks delivery

The opening explicitly proposes continuing the DLC public exchange, describes the Storyteller's tower and says the Commander remembers the mercy Devarra named there.
Its two variants require both verified brood status and the matching `devarra.native_*_cue_seen` flag.
The concluding narration says the native story brought both characters to that Tower.
These are actual story assumptions, not interchangeable technical labels.

The progression then requires chapter-five physical meetings, `devarra.actor_confirmed`, `devarra.history_read` and the same paired history.
Its delivered contact is the placeholder `ContactUnit="Devarra"`, not a registered unit GUID.
Its PhysicalPresenceRequired field is descriptive authoring data, not proof that the engine enforces scene geometry.
There is no implemented main-campaign acquisition, native actor confirmation producer or travel delivery for the tower, vault, warehouse, bridge and ridge.
The main route cannot honestly retain a required DLC witnessed conversation and claim availability to every eligible Trickster save.

## Concrete integration plan

1. Add read-only native history bindings for both main death states and positive egg outcomes.
   Use the exact verified IDs above and distinguish project offered, in progress and completed.
   Implement or reuse a tested project-completion reader before relying on the care-project alternative.
   Do not represent project completion as ordinary SeenCue or assume acquiring its etude completed it.

2. Author a main-campaign acquisition quest connected to the completed Greybor hunt and the Ivory Sanctum eggs.
   The Storyteller is a credible narrative intermediary for interpreting a recovered trace, but no inspected native Devarra relic or restoration spell has yet been verified.
   A newly collected remnant, recovery site, cost and soul-contact mechanism must be presented as authored content and actually produced by the quest.
   The two death locations require appropriate acquisition evidence rather than assuming every corpse lies in the lair.
   A living but unmet dragon needs a separate negotiated contact branch, not a death-state inference from missing flags.

3. Make the Trickster intervention concrete before opening romance.
   For example, a prepared trace and witnessed history could support an authored restoration bargain in which the Commander exploits a specific contradiction while Devarra chooses whether to return.
   This is a proposed alternate development, not a verified native Trickster ability.
   The saved history may affect her willingness to hear the bargain; the lost history must preserve anger and the dead clutch.
   Neither eggs nor resurrection automatically produces attraction or obedience.
   Failed preparation should have a bounded recovery path if the project promises eventual Trickster access, with permanent refusal and consent policy addressed explicitly in the authored route.

4. Establish a verified main-campaign actor and persist its identity before setting actor_confirmed.
   Root should choose between recovery of the actual saved entity and a deliberately authored persistent NPC representation after inspecting current unit lifecycle support.
   Require observation of the expected living, non-hostile actor in the intended area; a successful spawn request alone is insufficient.
   Prevent duplicate actors across reloads, interrupted restoration and area re-entry.
   Keep the historical native death markers intact.
   Do not copy the combat brain, hostile faction or DLC battle triggers without an explicit safe configuration audit.

5. Revise the acquisition handoff and opening's DLC-specific memories for the main-campaign route.
   Introduce a new authored witnessed-history flag after Devarra actually acknowledges the verified brood outcome in that new meeting.
   Never set `devarra.native_saved_brood_cue_seen` or its lost counterpart when those DLC cues have not played.
   Preserve the authorized DLC entry as a supported first-class variant wherever its real encounter history is established.
   Use the alternate introduction only where that event has not occurred or cannot be associated with the current save.
   A DLC-aware main-save variant still needs the explicit knowledge and actor bridge described above.
   Rewrite the Tower arrival and native-story assertion to the chosen actual location and meeting producer.

6. Give follow-ups a physical contact hub with an explicit trip to each represented location.
   A persistent negotiated rendezvous near Drezen can initiate book-event excursions, provided the prose and flags establish travel rather than pretending the dragon and every location occupy the capital.
   The existing main lair area and entry point are candidates for a first return expedition only after chapter-five accessibility, battle cleanup and navigation are tested.
   Do not teleport into that area merely because its GUID is known.
   Reuse existing bounded meeting/contact infrastructure where it fits; a new general travel framework is not required to prove one safe route.

7. Preserve the selected progression and coda guards while adapting the entry producers.
   The main chain's twenty-one visits and minimum waits need a real chapter-five completion test.
   Codas require the actual last invitation, not only a courtship flag or restored actor.
   Existing relationship flags for other women must remain independent under ToyBox free-love settings, while Devarra's authored objections and demands continue to matter.

## Transformation and portrait continuity

The frozen source remains physically draconic throughout: claws hold mechanisms, wings shelter meetings and her size keeps her outside buildings.
The attractive humanoid Devarra-v1 candidate therefore cannot serve as a literal portrait of her current body in those scenes.
It is an authored design candidate, not a native human likeness or evidence that transformation has occurred.

A later transformation requires a narrated cause, her decision, a persistent form state and a model/portrait handoff consistent with the engine representation.
Do not globally replace dragon body choreography with a human portrait while retaining impossible reach and wing actions.
Keep dragon-form illustrations on dragon-form pages and review a separate humanoid scene after that form is actually established.
The current crop-only native art evidence does not certify a native humanoid bust, costume or full-body shape.

## Exact outstanding evidence and verification

The missing native evidence is a peaceful chapter-five Devarra actor producer, a verified recoverable Devarra remnant, a tested safe return location for both death branches, and an observed main-campaign history acknowledgment replacing the DLC prerequisite.
No exact native binding for those missing events is supplied because none was established in this audit.
The general Storyteller dialogue hook and its chapter-five availability must be inspected before inserting the proposed acquisition.
The located chapter-three return KTC answer lists are not claimed as a reusable chapter-five hub.

Build fixtures for released eggs, completed care, directly destroyed eggs, completed omelet, unresolved projects and contradictory imported flags.
Test each against lair death, Sanctum death, living/unconfirmed and DLC-only states.
No unresolved or contradictory fixture may silently gain a matching brood acknowledgment or confirmed actor.
Then test restoration interruption, save/reload, area changes, duplicate prevention, hostile actor exclusion and the full physical-contact chain.

Finally execute both brood histories in a genuine main-campaign save, with other romances active, and verify the acquisition, each location transition, the latest meeting waits and one compatible ending.
This audit provides exact history bindings and a concrete authored-delivery plan.
It does not certify a currently playable main-campaign Devarra route.
