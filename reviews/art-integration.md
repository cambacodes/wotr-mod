# Art and integration audit

Reviewed 2026-09-25 as a demanding visual director and practical QA auditor.
This is an evidence review of the existing addon and expansion requirements.
The expansion has not been produced, so it has no art or technical score yet.
I applied the unslop writing skill and ponytail review skill.
I changed no game files or implementation files.

## Actual visual references

The installed custom portrait root is `C:/Users/Z/AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous/`.
I opened and visually inspected these files through the image viewer:

| Relative file | Observed traits and direction |
| --- | --- |
| `Portraits/CustomNpcPortraits - Seelah/Medium.png` | Black woman with braided hair, substantial steel armor, red cloak, upright bearing and shield behind her shoulder. Keep her face, skin tone and physical presence. A softer private expression can add range without replacing the soldier with an unrelated fashion model. |
| `Portraits - Npc/Jerribeth/Medium.png` | Strongly insectoid demon, green luminous eyes, long tongue, branching horns and translucent wings. Her nonhuman silhouette is the reference's identity. A disguise should be explicitly identified in the story and visually tied to this form. |
| `Portraits - Npc/Minagho/Medium.png` | Eyeless face, swept horns, pale long hair, pointed ears, red dress and elaborate gold jewelry. Restoring ordinary eyes in a romantic portrait would erase the most immediate visual identifier. |
| `Portraits - Npc/Arsinoe/Medium.png` | Long fair hair, luminous golden eyes, gold ceremonial armor and blue forehead jewel. This is an installed custom interpretation, not verified canonical evidence. Avoid copying its glossy metal and facial template to every other woman. |
| `C:/Users/Z/Documents/Projects/RanRomanceTirabade/art/originals/Together.png` | Anevia and Irabeth share a tavern table with touching hands, distinct silhouettes, cloth, armor and an inhabited setting. This is a useful benchmark for graphic and explicit intimacy. The faces stay separate and readable, though the small hand overlap deserves inspection in every final crop. |
| `C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/runtime-screen.png` | Saved screenshot of ordinary Anevia dialogue in the tavern with the custom portrait displayed. It proves that portrait presentation occurred at one point. It does not show the addon book scene, opening answers or a current expanded build. |

Matching named custom NPC directories exist for Arsinoe, Jerribeth and Minagho under the game's `Mods/CustomNpcPortraits/Portraits - Npc/` too.
Seelah uses the companion layout.
No named Konomi, Kiana, Vellexia, Gesmerha or Chivarro directory exists in the inspected user-data NPC portrait directory.
That is an asset gap, not proof that those characters have no canonical visuals.

Canonical blueprint data is available in `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip`.
The scoped index is recorded in `reference/art-review/canonical-blueprint-paths.txt`.
It includes active units, portrait definitions and some unused QA entries, which must not be mistaken for active story content.
I extracted `Seelah_Portrait.jbp` and `MinaghoFemaleDemon_Portrait.jbp` to the same review directory.
Seelah's full-length texture asset is `9aada42fab0f667449832a2236c61b2d`.
Blueprint texture identifiers are pointers, not inspected canonical images.
Canonical raster comparison remains required before signing off on likeness.
Vellexia also has distinct initiative portrait definitions for several date costumes, so a single guessed outfit would miss available reference detail.

## Art rubric

Score each character separately out of 100 after inspecting the full image, medium crop, small crop and story context.
Require at least 91 to satisfy the user's request for above 90 percent.

| Criterion | Points |
| --- | ---: |
| Canonical likeness, species, age presentation, build and signature features | 30 |
| Personality conveyed through expression, posture and clothing | 20 |
| Consistency between approved likeness and every scene variant | 15 |
| Anatomy, hands, props, light and absence of generation artifacts | 15 |
| Crop composition, readable faces and actual runtime presentation | 10 |
| Adult romantic chemistry, distinctive staging and scene accuracy | 10 |

A missing character, missing image, unreadable face, wrong species, lost defining feature, visibly broken anatomy or unclear adult presentation blocks approval regardless of score.
Attractive rendering alone earns no likeness credit.
Distinctive portraits should still look like they belong in the same game.
Group art requires independent identity and readable body language for every participant.

## Integration findings

1. `src/Main.cs` assigns every unrecognized scene owner to Anevia's answer list.
   New owner names alone would silently put Konomi and the others in the wrong conversation.
   Expansion needs explicit validated owner-to-answer-list mappings and a check that every integration GUID resolves to the expected blueprint type.
2. `Rules.Available` blocks all non-epilogue scenes when either Tirabade wife is dead or gone.
   It also blocks swarm and true lich globally, and all non-memory scenes in chapter 4.
   These rules cannot govern independent romances or ordinary Abyss meetings.
   All mythic routes need authored survival and contact behavior rather than an unrelated global veto.
3. The global `closed`, `committed` and journal objective belong to the existing couple.
   Independent routes need independent state so ending one relationship cannot close every other route or finish the wrong journal entry.
4. `BookPatch` defaults unrecognized speakers to the Together portrait.
   Every expansion node needs an explicit valid portrait or a correct speaker mapping.
5. The runtime image loader reads `Mods/CustomNpcPortraits/RanRomance-Tirabade/Scenes/<key>.png`.
   Images in `package/Portraits` are not runtime inputs.
   Missing images currently return null silently, so a successful dialogue registration log does not prove that art exists or displays.
6. `package-release.py` ships top-level package files plus the art tree.
   Both installers explicitly enumerate only Anevia and Irabeth for user-data portrait deployment.
   Expansion art needs a shared manifest or similarly explicit complete deployment list, including Seelah's companion layout.
   Development install also populates companion copies in the mod directory; release install does not make those same copies.
7. `prepare-portraits.ps1` stretches the entire original to the full-length ratio and uses fixed coordinates for the other crops.
   New source aspect ratios can distort faces or bodies.
   Export must preserve aspect ratio and inspect final crops individually.
8. Blueprint IDs derive from `RanRomance.Tirabade.v1/` plus stable names.
   Preserve that namespace and existing scene/node IDs for saved progress.
   Choice blueprint IDs use numeric positions, so reordering choices deserves a mid-dialogue save compatibility check.
9. Build integration modifies answer and epilogue lists as it goes.
   A late failure can leave partially attached content even though initialization reports an error.
   Preflight all external targets, portrait references and data before attaching the expanded content.

## What the current checks prove

I ran the existing compiled RulesTests executable against current `package/Story.json`.
It passed 3,224 assertions.
The test project compiles `Story.cs` and does not compile or execute `Main.cs`.
This meaningfully checks the existing graph, delayed progression, selected starting chapters, selected branch conditions and model ending exclusivity.
Its JSON round trip serializes `Snapshot`, not a Wrath save.
Its mythic loop adds path labels to a pre-completed state and walks one scene.
It does not prove complete campaigns on each path.
Its ToyBox compatibility evidence is the absence of gender, romance-count and jealousy inputs in the model.
It does not load ToyBox or run Harmony interaction checks.
Several assertions intentionally enforce the blockers that the expansion now needs to scope differently.

## Technical rubric

Score only demonstrated behavior and report missing evidence separately.
Require at least 91 out of 100 and no critical defects.

| Criterion | Points |
| --- | ---: |
| Every character attaches to correct live dialogue and resolves game references | 20 |
| All mythic routes, encounter dependencies, availability and endings | 20 |
| Independent progress, abort behavior, repeat prevention and save migration | 20 |
| ToyBox Free Love and Jealousy Begone combinations preserve intended simultaneous relationships | 15 |
| Portrait, package and installer completeness with backup/restore evidence | 15 |
| Build, schema, graph and runtime diagnostics make failures actionable | 10 |

Missing required characters, inaccessible required routes, lost save progress, broken base dialogue, global romance shutdown or missing distributed art block approval.
One character's score cannot compensate for another character's missing route.
Headless tests should cover complete per-character paths, all mythic states, starts after missed encounters, simultaneous commitments, introducer present/absent, deaths, departures and route-specific endings.
Read the installed output for the final run and compare its hashes with the reviewed build and packaged artifact.
Validate every portrait key against a decodable image at the actual runtime path and the zip entry used by release install.
If engine execution is unavailable, say precisely which runtime behaviors remain unverified instead of converting assertion count into confidence percentage.

## Trickster fate-changing branches

The added rescue requirement needs a recorded transition for each candidate's missed, dead, hostile or departed state.
Removing a death flag from the story snapshot does not resurrect or relocate a game unit.
For each rescue, inspect the original unit state, authoritative etudes, quest outcome, area, contact mechanism and resulting romance entry.
An explicitly authored supernatural meeting can use the book interface without claiming that the physical NPC was restored.
If the script claims physical restoration, the engine must actually restore a usable NPC without duplicating her or restarting completed hostile encounters.
Save and reload after the rescue and after the next meeting.
Repeating the rescue must not duplicate units, reset progress or produce contradictory endings.
Other paths still need their advertised availability, with separately authored contact rules where an NPC is absent.

## Efficient engine checks

`SimpleBlueprint` is a managed class, not a Unity ScriptableObject subclass, and `BlueprintsCache.AddCachedBlueprint` is available in the inspected game sources.
That makes a small managed blueprint-construction fixture plausible.
It is not yet a proven standalone engine runner.
`ResourcesLibrary`, localization, blueprint `OnEnable`, `Game.Instance`, etude state and Unity image loading introduce additional dependencies.
Do not spend time writing a fake Unity implementation just to report that the engine was tested.
First use `reference/expansion/blueprints.json` and `etudes.json` to validate target GUIDs and types against the actual exported game data.
Then compile against the installed managed assemblies, test the pure rules, and inspect the generated registration mappings and preserved existing IDs.
A genuine fixture should call production construction code and inspect its attached answer/page references.
It must report native initialization failures openly and must not be described as a real save/load or rendered-image test.

## Seelah v1 source-art review

I directly viewed `art/expansion/originals/Seelah-v1.png` alongside both the canonical backup and the installed enhanced full-length portrait.
The canonical file is `C:/Users/Z/AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous/Portraits/CustomNpcPortraits - Seelah/Backup of Game Default Portraits/Fulllength.png`.
The enhanced file is the `Fulllength.png` in its parent directory.
This updates the earlier canonical-reference gap for Seelah only.

The new image is a close reconstruction of the canonical stance and equipment with a more detailed face and environment.
It keeps her dark skin, braided-back hair, stocky armored silhouette, red cape, circular wooden shield, broad sword, decorated scabbard and visible battle wear.
Her facial treatment sits between the canonical image and the installed enhanced image.
The new jaw and lips are smoother and fuller than the original, but she remains recognizable.
The rendering returns toward the game's painted surfaces and simpler armor decoration compared with the glossy enhanced reference.
That is a sensible compromise for this portrait.

| Observable source-art criterion | Score | Reason |
| --- | ---: | --- |
| Canonical likeness and signature features | 28/30 | Strong agreement in face, hair, build, stance, cloak and equipment. Some facial softening remains. |
| Personality through expression, posture and clothing | 18/20 | Credible experienced paladin with a firm stance and direct expression. It provides little of Seelah's humor, which should appear in private-scene variants rather than being forced into this formal portrait. |
| Anatomy, hands, props, light and artifacts | 14/15 | The two gauntleted hands plausibly wrap the same sword grip; wrists connect to their corresponding forearms and the visible digit plates do not establish an extra-finger defect. The overlap is dense, so preserve this construction during cropping or variant generation. Metal edges, legs and footwear read coherently. |

The observed source-art subtotal is 60/65, approximately 92.3 percent of those three criteria.
This is not a complete 92.3/100 art approval.
Consistency across scene variants, final crops, actual runtime framing and romantic-scene chemistry remain unscored because their evidence is absent.
The portrait is suitable to proceed to crop preparation and a first character-specific scene variant.
I found no source-image defect that warrants regenerating the whole portrait.
Do not count this neutral character portrait as a romantic scene or use it to award the chemistry category.

For the crop review, keep her whole head, braid edge and readable shield silhouette in the medium view.
At small size the eye line and mouth need enough pixels to preserve her expression.
The source is 1024 by 1536, while the game's 692 by 1024 full-length format has a slightly different aspect ratio.
Use aspect-preserving resize with a deliberate crop or padding rather than stretching.
The sword tip extends outside the source frame, as in the canonical composition; that is intentional framing rather than a broken prop.

## Verified restoration APIs and their limits

These findings come from the installed `Assembly-CSharp.dll` and scoped blueprint exports.
Relevant decompilations are saved under `reference/art-review/`.
No API below was invoked against a live player or save.

| Operation | Actual API and findings |
| --- | --- |
| Restore an existing dead unit | `unit.Descriptor.ResurrectAndFullRestore(caster)` is used by `ContextActionResurrect`. The alternative signature is `Resurrect(UnitEntityData, Single, Boolean)`. The game action also gives the standard resurrection buff for one round. Prefer the descriptor operation to toggling a death field. Preconditions and scripted permanent deaths still need runtime validation. |
| Find the original dismissed companion | `UnitPartCompanion.FindCompanion(BlueprintUnit, CompanionState.ExCompanion)` searches `Player.AllCrossSceneUnits`. Also inspect `Player.AllCharacters` and the known entity ID before spawning anything. |
| Restore a dismissed companion to reserve | `RecruitInactive.RunAction()` reuses an existing `ExCompanion`, sets `UnitPartCompanion.SetState(CompanionState.Remote)`, raises party/recruit events and runs its supplied `OnRecruit` actions. Set `AvailableDelay=false` and use an empty action list for the narrow operation. It rejects double recruitment of a companion in another state. It does not resurrect a dead companion. |
| Avoid forced party changes | `Recruit` can invoke party selection and remove companions to satisfy its six-member logic. `Player.AddCompanion` appends a party reference and raises activation events, so it is not an idempotent reserve-roster setter. |
| Reveal an existing hidden unit | The standard `HideUnit` action with `Unhide=true` sets `IsInGame=true`. Its hide path can set `UnitPartCompanion.IsIgnoreFixInGame=true`, while its unhide path does not clear that flag. Inspect and reconcile this saved flag when restoring a deliberately hidden companion. |
| Restore a loaded original NPC spawner | `GameHelper.GetUnitSpawner(EntityReference)` followed by `UnitSpawnerBase.TrySpawnOrRespawn()` is the operation used by `Spawn` with `RespawnIfDead=true`. It needs that spawner's scene loaded. A corpse-respawn does not by itself reconcile hostile AI or quest dialogue. |
| Spawn only when no original entity remains | `Game.Instance.EntityCreator.SpawnUnit(BlueprintUnit, Vector3, Quaternion, SceneEntitiesState, string uniqueId=null)` accepts a stable identity. It loads actual prefabs and requires a non-null holding state. `EntityService.Instance.GetEntity(string)` can find a currently registered identity. Registry absence alone does not establish absence from unloaded saved areas. |
| Change faction | Public installed methods include `UnitEntityData.SwitchFactions(BlueprintFaction, Boolean)` and the descriptor equivalent. Faction switching alone is not proven to remove scripted attack actions or change combat interaction into dialogue. The meaning and appropriate value of the Boolean require implementation inspection before use. |
| Begin direct contact with an actual unit | The existing game dialogue action uses `Game.Instance.DialogController.StartDialogWithUnit(BlueprintDialog, UnitEntityData)`. This bypasses reliance on a recovered unit's original click interaction for that invocation. Persistent click-to-talk behavior requires a correct unit interaction component. |

The narrow restoration sequence is to identify the original entity, restore health if needed, restore an existing companion to reserve where applicable, establish a safe physical location and contact mechanism, and only then record the addon rescue as successful.
Do not mark success when spawning returns null or when the contact target is still unavailable.
Use a stable addon identity only for a documented fallback, and recheck it on repeated rescue and save load.
Do not spawn another original-name NPC merely because her original area is unloaded.

`SceneEntitiesState.RemoveEntityData` calls `Dispose()` on the entity.
Removing from one state and adding to another is therefore not a valid relocation recipe.
Keep an existing unit in its holding state until the game's supported move/attach API is identified.
For first implementation, a rescue invoked while the original area and spawner are loaded is safer than silently moving serialized NPCs across visited areas.
Remote physical contact for an already visited inaccessible area remains an implementation problem, not a verified capability of the current addon.

The extracted Seelah blueprints provide a useful concrete state distinction.
`SeelahNotInParty_Dead` derives its activation from a dead companion condition.
`SeelahInParty` accepts active, detached and remote companions, but rejects dead or ex-companions.
`SeelahNotInParty_KickedOut` activates for ex-companions and has a repeatable play trigger that fails her quests and completes the camp-laughter etude.
Restoring her roster state can resolve the derived presence conditions; it does not undo quests that were already failed.
Do not restart the whole companion parent just to reopen romance contact.

`EtudesSystem.UnstartEtude(BlueprintEtude, bool markPreStarted=false)` recursively unstarts children and changes completed descendants to precompleted states.
It is not a harmless Boolean setter.
Inspected `MinaghoDead` and `ChivarroKilled` are leaf etudes without actions or child-start lists, but every reader of those flags still needs review before clearing them.
A scoped addon restoration fact may preserve historical quest results while overriding the new romance's availability and ending.
That must be reflected honestly in the script, and any contradictory base-game ending requires a targeted correction.
No broad quest reset or autosave belongs in the rescue operation.

## Standalone managed construction probe

The earlier standalone-fixture uncertainty is partly resolved by execution.
I wrote and compiled `reference/art-review/ManagedProbe.cs` using Windows .NET Framework's `csc.exe` and ran it against the installed managed assembly directory.
The output is recorded in `reference/art-review/managed-probe-result.txt`.
The process constructed real `SimpleBlueprint`, `BlueprintAnswer`, `BlueprintAnswersList`, `BlueprintBookPage`, `BlueprintDialog` and `LocalizationPack` instances, called actual `OnEnable`, assigned `LocalizationManager.CurrentPack` and accessed the real `ResourcesLibrary.BlueprintsCache` successfully.
It also reflected the restoration method signatures listed above.
It did not load fake Unity assemblies, launch Wrath or change game state.

This proves a real managed blueprint-construction fixture is viable in this environment.
To run production `Build`, seed its exact external blueprint dependencies into the real cache with their correct GUIDs and types, initialize the real localization pack, supply the story and mod-entry logging fields, and call the actual construction method.
Then inspect the actual attached answer references, book pages and conditions.
External fixtures should be populated from the exported game definitions rather than assumed empty answer lists when preservation is being tested.
Any unavailable native call remains a failure to report, not a reason to substitute dummy engine methods.
Production `Build`, mod-entry logger setup and complete exported dependency hydration have not been executed by this reviewer yet.
Even a passing production-construction fixture will not prove unit resurrection, area loading, Unity image decoding, player etude evaluation or real save deserialization.

## Production Build proof

I extended the same managed probe and successfully invoked the current development assembly's actual private `Tirabade.Main.Build` with `package/Story.json`.
Output is saved in `reference/art-review/managed-build-probe-result.txt`.
The assembly registered 34 scenes, set `initialized=True` and left `error` empty.
The reviewed DLL SHA-256 is `6EFD8EB93D26BD82CBB3BC5202DF08A5975B4B06198E6318B538878DAAC840FA`.
The story SHA-256 is `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4`.
This run exercised the newer scoped engine with the existing 34-scene story.
It does not establish that any unwritten expansion scene works.

The setup uses a real `UnityModManager.ModInfo` with `Id`, `Version` and a nonempty `ManagerVersion`, then the normal `ModEntry(info, path)` constructor.
Setting `ManagerVersion` avoids its fallback read of the global manager configuration.
The constructor creates the real `ModLogger`.
The logger's normal write path uses the console and in-memory buffers.
Its file writer is reached by `Watcher` or `WriteBuffers`, neither of which this process invokes.
No native dependency blocked this run and no logger replacement was needed.

The probe assigns private `entry` and `story` fields, uses the actual JSON deserializer, creates an actual localization pack, and seeds 28 external blueprint instances in the real cache.
It obtains entry-target IDs from the actual `Rules.EntryTargets` implementation and includes the story's etude IDs plus both epilogue sequence IDs.
The external blueprints have the correct runtime types and GUIDs but otherwise minimal contents.
This proves production blueprint construction runs under standalone .NET Framework.
For preservation and integration tests, populate external answers and cues from actual exported game data, then compare before/after object references and count repeated Build calls.
Do not describe this minimal fixture as complete base-game blueprint hydration or live Unity execution.

## Seelah evening v1 source-art review

I viewed `art/expansion/originals/Seelah-evening-v1.png`, the approved `Seelah-v1.png`, and the canonical full-length backup directly.
I also read the recorded generation prompt and the current `EVENING` nodes in `storylines/seelah.py`.
This is a scene illustration review, not a portrait-crop or runtime approval.

The scene reads as the first private supper.
Seelah sits on a coarse blanket beside a wrapped loaf and two visibly flattened pastries, with her cloak and shield nearby.
The food is ordinary and slightly spoiled in presentation, which supports her horse-and-pastries joke.
Her tilted head, direct gaze and small uneven smile convey the warmth that the formal armored portrait lacked.
This feels like a person enjoying the Commander's attention, rather than an interchangeable seduction pose.
She retains the recognizable brow, nose, mouth, closely braided hair, dark complexion and substantial forearms of the approved likeness.
The lamp warms her skin without making her appear to be a different character.

| Observable source-art criterion | Score | Reason |
| --- | ---: | --- |
| Canonical likeness and defining features | 28/30 | Recognizable Seelah with the approved face and sturdy build. The fuller lips and cosmetic finish remain a modest departure from the original game's rougher portrait. |
| Personality conveyed by expression and posture | 19/20 | Warm, amused and attentive. Her expression fits a first invitation to intimacy without making her look helpless or coy. |
| Consistency with the approved source | 13/15 | Hair, face, complexion and red cloak agree. The evening rendering is more photographic and glossy than the armored source, particularly on the face and shirt. |
| Anatomy, hands, clothing, props and light | 14/15 | The visible resting hand has four long fingers and a separate thumb; the hand beneath her chin connects plausibly to her forearm with partly occluded digits. Knees, wrists, boots and crossed-leg arrangement are coherent. No extra limb or fused-hand defect is visible. |
| Romantic chemistry and fit to the actual scene | 9/10 | Blanket, loaf, two flat pastries and conversational gaze closely fit supper. The brown marks on the shirt read partly as stains rather than loose crumbs, slightly weakening the clean-shirt detail. |

The observed source-art subtotal is 83/90, approximately 92.2 percent of scored criteria.
Final crop composition and runtime presentation remain unscored, so this is not a complete 92.2/100 delivery score.
There is no critical source-image defect requiring regeneration.

Use the image for the supper or quiet-conversation beat.
It does not depict the later hand clasp or kiss, and should not be described as illustrating those actions literally.
The neckline is more open than the prompt's phrase "modest neckline" suggests, but the character remains fully clothed in a believable off-duty shirt.
It does not undermine this scene's adult, affectionate tone.
The apparent fabric stains are a minor visual mismatch rather than a story blocker.

Preserve enough of the blanket and pastries in any scene export for the joke to retain its visual context.
A tight face-only crop will work as a speaking portrait but will lose that scene-specific evidence.
Do not award the current source score to such an unreviewed crop automatically.
The new shield emblem and distant camp heraldry are plausible additions but have not been verified against separate canonical equipment references.

## Completed-quest and choice-timestamp audit

This is an intermediate source audit of `Main.cs` and `Story.cs`, not a release score.
I inspected the current completed-quest bindings, registration order, snapshot conversion, choice actions and rule validation.
I also inspected the installed game's decompiled `QuestBook.GetQuestState` implementation and checked the current development story for naming collisions.
I did not rerun unrelated art reviews or claim a live save test.

The completed-quest read is correctly narrow.
`GetQuestState(BlueprintQuest)` returns the quest's actual state or `QuestState.None` if it is absent.
Comparing it with `QuestState.Completed` avoids treating a started or failed quest as completed.
The quest blueprints are resolved before registering generated flags or attaching answers, so a missing quest binding fails before those external list mutations.
Quest aliases are derived when `State()` runs and are not saved as separate addon completion flags.

Registering `hour.<effect>` for every distinct `Choice.Set` effect fixes the runtime omission that made choices unsuitable as delay anchors.
Recording the first activation only prevents later dialogue from continually restarting a courtship delay.
The existing `hour + 1` encoding preserves hour zero, and snapshot decoding subtracts one consistently.
`Rules.Available` uses the latest recorded time among its required flags.
This is coherent for the door scene whose prerequisite is a courtship choice.

The existing blueprint GUID namespace and names are unchanged.
The newly registered timestamp blueprints are additive, so this change does not itself invalidate previous scene or choice references.
There is one migration limit: a save that already contains a choice flag without its timestamp will not acquire that missing timestamp when the same flag is set again.
The first-activation guard examines the flag, not the timestamp.
Such a save can still satisfy a delay immediately if no other timed prerequisite supplies an anchor.
This needs an explicit compatibility decision for previously distributed builds; it is not evidence of save corruption.

The current development story contains one completed-quest alias, `seelah.souls_returned`.
I found no overlap between external aliases and writable effects, scene IDs or relationship-state flags, no authored key beginning with `hour.`, and no effect that is also a scene ID.
These particular collision cases therefore do not block current content.
Runtime `Rules.Validate` does not yet reject all of them, however.
A future effect named like a quest alias could cause the snapshot to satisfy that alias before the real quest completes.
A future authored `hour.*` flag could overwrite or be interpreted as timestamp storage.
The validation currently checks quest alias collisions with etude aliases, but not with those other writable key families.
The headless unknown-condition audit is broader than runtime `Validate`, so it remains part of the required export checks.

Quest aliases have no timestamp of their own.
For example, the delay on `seelah.souls`, whose requirements include `seelah.morning` and `seelah.souls_returned`, counts from the recorded morning scene rather than the instant the native quest completes.
That can be correct for an immediately available post-quest conversation, but it must not be described as a delay after quest completion.

Internal preflight dictionaries can remain partly populated after a missing binding causes Build to fail.
The stored error then prevents another Build attempt in that process.
No newly attached answers have been added at that stage, so a restart after correcting the data is the current recovery path.
The broader previously noted late-construction partial-attachment risk remains separate from these two focused changes.

The parent has now documented the legacy missing-timestamp fallback and the intended post-quest timing semantics in `development/verification.md`.
The aftermath delay deliberately measures time since the prior relationship scene, not time since native quest completion.
That resolves the interpretation question for current content.
The documented 4,818-assertion construction run completed in 8.03 seconds after the native archive reader switched to one AssetId extraction and set lookup per record.
Those updated execution figures are the parent's recorded evidence, not an additional independent execution by this reviewer.
Broader schema collision hardening remains an identified improvement; this audit still makes no release claim.

## Repeatable Jerribeth contact

The installed game stores persistent dialogue history in `Game.Instance.Player.Dialog`.
`ShownDialogs` is a `HashSet<BlueprintDialog>`, `ShownCues` is a `HashSet<BlueprintCueBase>`, and `SelectedAnswers` is a `HashSet<BlueprintAnswer>`.
All three fields have `JsonProperty` annotations in the inspected `DialogState` implementation.
The exact checks used by native conditions are `ShownDialogs.Contains(dialog)` and `ShownCues.Contains(cue)`.
`CueSeen.CurrentDialog=true` instead reads `DialogController.LocalShownCues`, which is unsuitable for persistent first-contact eligibility.

`DialogController` records a shown dialogue after scheduling its first cue.
Therefore a shown dialogue means that the conversation began successfully, not that the Commander completed a bargain or reached its ending.
A route that requires an actual deal should bind a decisive seen cue, selected answer or native outcome etude.
A route that only needs recognition can use the seen-dialogue flag.
These are source-level persistence findings; this review did not serialize a real save.

The scoped export identifies these native Jerribeth dialogues:

| Native encounter | Dialogue GUID |
| --- | --- |
| Ivory Sanctum greeting | `80f8dac1bd80ff846ba839fb14ed83b8` |
| Wintersun revelation | `6825f92d429082944b504c1f78b4e30a` |
| Vellexia encounter | `992c44e6775d87444b562e855fd64af1` |

The narrow engine addition is a typed seen-dialogue or seen-cue binding dictionary resolved during Build preflight, then read into snapshot aliases during `State()`.
Aliases must remain distinct from writable relationship effects.
The headless binding checker should verify the requested native type, and the managed-construction fixture should seed those external types.
No native dialogue conditions or finish actions need alteration.

The existing remote scene path is the safer repeatable channel for correspondence from Drezen or Nexus.
It already supports `Remote`, chapter/area restrictions, rest scheduling, an explicit read action in the mod interface, and `StartDialogWithoutTarget` for the addon book dialogue.
The narrative should describe correspondence, a vision or a separately arranged encounter consistently with that presentation.
It must not claim that a dead or missing NPC was physically restored merely because a remote book page opened.
A prior shown dialogue can establish that Jerribeth knows the Commander, while an outcome flag can distinguish an accepted deal from an interrupted conversation.
This design avoids reopening a canceled native encounter or depending on its exhausted click interaction.

The actual blueprint component for click dialogue is `Kingmaker.UnitLogic.Interaction.DialogOnClick`, not a type named `DialogueInteraction`.
It has a private `m_Dialog` reference, a `NoDialogActions` list and inherited `Conditions` from `UnitInteractionComponent`.
Its interaction calls `DialogController.StartDialogWithUnit(Dialog, target, user)`.
Its availability check checks inherited conditions and whether a first-cue list exists; it does not prove that the selected dialogue's own conditions will pass.
Initialize both action and condition lists if using it.

Simply appending another click component does not guarantee that it will run.
`UnitPartInteractions.SelectClickInteraction` chooses available interactions by priority and lets later interactions win at equal priority.
Blueprint interaction priority is zero, spawner priority is 100, and etude override priority is 200.
In a development build, multiple available interactions at the same priority can produce an error and no chosen interaction.
`UnitPartInteractions.AddInteraction` inserts at the front, so insertion position alone does not solve the equal-priority selection rule.
Existing loaded entities also need their interaction list updated; changing only the blueprint does not establish that their current list changes.
`SetupBlueprintInteractions(unit)` adds all blueprint interactions and is not a safe repeatedly called refresh because it can duplicate them.
The class does offer `RemoveInteraction` and `RemoveInteractions`, which should target only the addon's own interaction if a live rebind is implemented.

A physical click hub therefore needs entity-specific availability, safe add/remove ownership, mutual exclusion with native click actions, and testing against spawner/etude overrides and disabled interactions.
That is more engine work than the existing remote book channel and should not be silently introduced just to make one-shot native dialogue repeatable.
The remote channel plus precise persistent-history bindings is the recommended minimum for the current Jerribeth arc.

## Jerribeth v1 source-art review

I directly viewed `art/expansion/originals/Jerribeth-v1.png` and the installed `Portraits - Npc/Jerribeth/Fulllength.png` under the game's user-data directory.
The installed image is a custom portrait reference.
Neither this comparison nor its score establishes fidelity to an original game raster.
I also read the image prompt, the drafted correspondence scene and the scoped native dialogue describing her insectile appearance and mental voice.

Native cue `3b4288a9837026c419c15a218bd668ec` describes an insectoid face that is difficult to read.
Cues `666c827662e8af14798009a98c5aae52` and `063d159af56b4c54292e6e2eaca8ca08` establish mental communication and buzzing laughter.
The portrait preserves those broad character traits without substituting an ordinary human face with horns.
Telepathy itself is a writing fact, not something a static portrait can prove.

The new image preserves the custom reference's narrow chitinous face, green luminous eyes, swept horns, antennae, wispy hair, long tongue and several translucent wing sections.
Her linked clawed hands fit the correspondence scene's described gesture.
The dark plum gown is an authored wardrobe change that keeps her nonhuman frame readable.
It also provides a useful contrast with Seelah's practical shirt and Konomi's more formal court direction.
The chamber, furnishings and warm wing illumination give the image an established place rather than the custom reference's generic bright meadow.

| Observable source-art criterion | Score | Reason |
| --- | ---: | --- |
| Fidelity to the installed custom identity and script-supported species traits | 29/30 | Major silhouette, facial structures, eyes, tongue and wings are retained. This is explicitly a custom-reference score, not a canonical-raster score. |
| Personality through expression and posture | 18/20 | Stillness and watchful attention suit a calculating telepath. Amusement is subtle rather than a human smile, which agrees with the script's difficult-to-read face. |
| Anatomy, materials and artifacts | 13/15 | Arm connections and the two-hand arrangement are plausible. The overlapping narrow claws are dense and hard to trace individually; there is no definite extra hand or limb, but this is the least clear part of the source. Chitin and wing veins are well separated. |
| Usability for the written correspondence scene | 9/10 | Linked hands, direct attention and a private interior fit the opening contact. A static source cannot illustrate the charm being turned over or her image disappearing. |

The source subtotal is 69/75, or 92 percent of these bounded criteria.
The 30-point identity category is restricted to the installed custom likeness plus the cited written species traits.
Canonical raster fidelity, cross-variant consistency, final crops and runtime appearance remain unapproved.
No guise image exists yet, so there is no evidence for consistency between her forms.

The image is suitable for crop preparation without a full regeneration.
Keep a copy with the horns, antennae and wings intact, since a human-style head crop would discard much of her identity.
The medium crop should prioritize the eyes, ridged face and visible origin of the tongue without letting that single feature dominate the composition.
At small size, verify that glowing eyes remain separated from the dark facial ridges.
Do not automatically approve the linked hands in a later close-up merely because they are acceptable at this full composition size.

The rendering is compatible with the detailed fantasy direction, though the soft background and polished surfaces lean toward rendered illustration rather than the original game's rough brushwork.
The image prompt requested no camera-like background blur; the distant furniture is visibly soft, a minor prompt departure.
The gown and private chamber should remain identified as addon art direction rather than established canonical clothing or location.

## Retained Seelah restoration preconditions

This review supports only an existing retained companion entity.
It does not support creating a replacement when the original cannot be found.
Seelah's companion blueprint is `54be53f0b35bf3c4592a97ae335fe765`.
Find the original in `Player.AllCrossSceneUnits`, cross-check `Player.AllCharacters`, and require exactly one matching retained object.
Capture its `UniqueId`, object identity, original roster state, holding state and party membership before changing anything.
Reject ambiguous duplicates, missing holding state, missing player/initiator, combat, an active or scheduled dialogue, or an unavailable required area before mutation.
The action should also enforce the authored Trickster and rescue-eligibility conditions at execution time.

`UnitPartCompanion.FindCompanion(blueprint, CompanionState.ExCompanion)` can locate the ex-companion in cross-scene state.
Before invoking `RecruitInactive`, also require that the object its own `Player.AllCharacters.FirstOrDefault` search will find is that same ex-companion.
Otherwise its fallback can call `SpawnUnit`, contrary to the retained-entity-only requirement.
Use `AvailableDelay=false` and an empty `OnRecruit` action list.
For an already remote or active retained companion, skip recruitment rather than asking `RecruitInactive` to double-recruit her.
A direct `SetState(Remote)` uses the original entity and invalidates character lists, but does not reproduce the standard recruitment events by itself.

I inspected the installed `UnitDescriptor` IL and saved only that class to `reference/art-review/UnitDescriptor.il`.
`ResurrectAndFullRestore(initiator)` calls the native resurrection implementation with full restoration enabled.
That implementation clears final-death, forced-kill and marked-for-death state, repairs damage and relevant conditions, handles native repositioning and animation, removes resurrection-related buffs as implemented by the game, and raises the resurrection event.
This is materially more complete than assigning a life-state flag.
It also means the action can affect more than hit points and must only be invoked when resurrection is actually required.
An already alive companion must not be repeatedly healed by reopening the rescue dialogue.

The verified faction signature is `SwitchFactions(BlueprintFaction faction, bool resetAttackFactions=false)`.
The Boolean is specifically `resetAttackFactions`.
For a restored ex-companion left hostile, explicitly restoring `BlueprintRoot.Instance.PlayerFaction` with attack-faction reset is available.
Do this only for the resolved retained companion after all preflight checks, not for every unit sharing a display name.
The native party repair code also normalizes the group string to `<directly-controllable-unit>`.

Clear `IsIgnoreFixInGame` if the rescue is reversing the saved hide state that set it.
Simply running `HideUnit` with `Unhide=true` does not clear that flag.
Do not reset arbitrary `ShouldBeHidden`, `IgnoresSpawners` or other countable flags without identifying their owners.
They may represent active story or cutscene restrictions.

## Seelah restoration postconditions

Before recording a rescue as completed, verify that the matching retained object and `UniqueId` are unchanged, that no second Seelah was introduced, and that her actual life state is alive and conscious.
Verify that an original ex-companion is now remote, while a previously active companion has not been silently removed from the party.
Verify player faction, absence of the intended hostile attack-faction relationship, and that the saved hide override no longer defeats the intended placement.
Roster restoration and physical contact should be reported separately if one succeeds before the other.

`FixPartyAfterChange()` does not itself prove remote-companion contact in Drezen.
Its `FixPartyMember` positioning branch explicitly excludes `CompanionState.Remote` and `InPartyDetached`.
The method can correct faction and group while leaving a remote unit absent or at an unsuitable location.
Contact success therefore requires `IsInGame`, a live view, an actual safe loaded-area position and a viable interaction or explicitly started addon dialogue with that unit.
`GetCurrentSpawner()?.ShouldShowUnit(unit)` can explain whether the current companion spawner permits her presence.
If it does not, forcing `IsInGame` once may be undone by subsequent area or etude processing.
Verify presence after the relevant frame/update work before setting the final rescue flag.
Do not remove/add her between scene states because `RemoveEntityData` disposes the entity.

The inspected native etudes are derived from companion state.
`SeelahNotInParty_Dead` accepts the dead state, while `SeelahNotInParty_KickedOut` accepts ex-companion state.
`SeelahInParty` accepts living active, detached and remote states.
Restoring the actual unit and roster can therefore change their activation results without manually clearing a guessed quest flag.
Allow native etude evaluation to run before asserting that the derived gates have changed.
Previously failed companion quests and already completed departure actions remain historical outcomes.
Restoring the companion is not permission to restart her entire quest parent.

These are verified API and source-level preconditions, not evidence that a real restored Seelah has survived a frame, a dialogue, or a save reload.
The initial implementation should leave unsupported missing-entity and unsafe-contact states explicitly unresolved rather than spawning a blind copy or falsely marking full restoration.

## First retained-death implementation review

I reviewed the initial `src/Fate.cs`, its invocation from `Main.RouteAction`, and the `Recovery`/`Revive` schema rules.
This review concerns resurrection of a unique already retained dead companion only.
Dismissal, missing entities, hostile replacements, physical contact and save persistence remain separately pending.
No native resurrection action was executed during this review.

The implementation has several correct boundaries.
It rejects missing or duplicate matching cross-scene entities and accepts only active or remote companion states.
It calls the native descriptor resurrection operation rather than spawning a new unit.
Recovery availability bypasses only the configured death gate while retaining the relationship's other unavailability flags and closure state.
The current Seelah recovery also requires Trickster, the native death alias and the authored Drezen area/chapter constraints.
Execution rechecks full scene availability before calling resurrection.
Schema validation requires revival to be a terminal, non-abort choice belonging to that recovery.
The action records choice effects and scene completion only after `TryRevive` reports success.
The current Seelah relationship has no failure flags, so the generic objective-failure loop does not permanently fail her relationship journal merely because this death occurred.

Concrete gaps within this narrow slice are:

- `FindRetainedCompanion` filters roster state but not actual faction or holding-state validity. Its comment excludes hostile replacements more strongly than the implemented checks do. A retained active/remote entity with a changed faction can still qualify.
- The success predicate checks that the unit is no longer dead and that lookup returns the same object. It does not explicitly verify consciousness, unchanged roster state or unchanged `UniqueId`. The native operation and event subscribers can affect state, so these should be checked before claiming the intended postconditions.
- Native resurrection is not transactional. The inspected implementation clears death state before later positioning, animation and event work. If a later operation throws, the catch returns false even though the unit may already be alive. `CanRevive` then becomes false, leaving the recovery unavailable without its authored success marker. The failure message should disclose partial state rather than imply that nothing changed, and the design needs a bounded reconciliation decision for this case.

Preserving the same entity is strong evidence that the implementation avoids replacing equipment and progression wholesale.
The current success message nevertheless states equipment and progression preservation more categorically than the code verifies.
A message limited to actual life and identity checks would be more precise, or the implementation can record and compare the specific invariants it promises.

The absence of a view is not itself proof that native resurrection will throw.
The inspected descriptor IL branches around view-specific work when no view exists.
That supports the feasibility of restoring a remote retained entity's life state, but still provides no evidence of physical placement or usable contact afterward.

## Save-owned partial-restoration checkpoint

The installed player class already provides `[JsonProperty] public Dictionary<string, object> SettingsList`.
It is part of the player object, not the mod manager's global settings file.
A namespaced entry such as `RanRomance.Tirabade.Revival.seelah` can hold a JSON string containing the original `UniqueId`, original companion state, checkpoint version and phase.
Use a string value rather than a custom CLR checkpoint object so save loading does not require an additional mod-defined serialized type.
Read through `TryGetValue` and validate the string's schema and identifiers before using it.
Never overwrite an unrelated key or silently accept a malformed checkpoint.

There is also a native per-entity alternative.
`unit.Ensure<EntityPartKeyValueStorage>().GetStorage("RanRomance.Tirabade.Revival")` returns `Dictionary<string, string>`.
The built-in `EntityPartKeyValueStorage` declares its nested string dictionaries with `JsonProperty`.
`EntityPartsManager` declares its list of entity parts with `JsonProperty` too.
These sources are saved in `reference/art-review/EntityPartKeyValueStorage.cs` and `EntityPartsManager.cs`.
No custom unit-part subclass is necessary.
`GetStorage` creates a missing bucket, so an availability check should not call it as though it were a completely read-only lookup.

For this recovery, a player-owned string checkpoint is the simpler option because its original unit ID remains discoverable without first guessing which unit owns the record.
Write the pending checkpoint after all preconditions pass and immediately before the native resurrection call.
If the call throws, keep that checkpoint and record the observed partial outcome.
On retry, resolve the recorded original ID and require the same intended companion blueprint, valid holding state and supported original roster state.
Do not select another same-name unit or create a replacement.

The next action depends on actual state.
If the recorded original is still dead and its preconditions remain valid, a retry may invoke resurrection.
If it is already alive, do not invoke resurrection again just to replay missing dialogue effects.
Instead verify the full agreed postconditions and allow the unfinished addon effects to complete only when those postconditions hold.
An alive but unconscious, wrong-faction or otherwise unreconciled original needs a precise partial-state message, not an invented successful recovery.
Keep the checkpoint until authored effects and scene completion are recorded; deleting it before those writes can recreate the lost-progress window.
The checkpoint does not request an autosave and does not substitute for actual save/reload testing.

Exact available identity predicates include `unit.UniqueId`, `unit.IsPlayerFaction`, `unit.HoldingState`, membership by object identity in `Player.AllCrossSceneUnits`, and `unit.Get<UnitPartCompanion>()?.State`.
For this explicitly retained-cross-scene slice, compare `unit.HoldingState` by reference with `Player.CrossSceneState` rather than accepting an arbitrary non-null state.
These checks establish that the recorded object is still the expected retained companion.
They do not establish loaded-area visibility or viable dialogue contact.

The serialization annotations establish native save participation at source level.
This reviewer has not run a real game-save round trip containing either checkpoint option.

## Checkpoint coordinator implementation review

I reviewed `RecoveryAttempt.cs`, the revised `Fate.cs`, `Main.RecordProgress`, `Main.ReconcileRecoveries` and `tests/RecoveryTests.cs`.
The core ordering addresses the earlier partial-resurrection defect.
The player-owned checkpoint is written before the native call, carries the original unit ID and roster plus the scene and exact chosen action, and survives an exception.
The production coordinator calls the resurrection delegate only when its inspected original remains dead.
An already living original must also be conscious, eligible and identical in saved ID and roster before it is credited.
The native adapter's eligibility now requires player faction, cross-scene holding-state identity and a supported retained roster state.

Idle reconciliation resolves the original checkpoint and compares the current choice's serialized contents with those originally authorized.
It does not substitute another recovery effect or resurrect the living unit again.
`RecordProgress` skips already-set flags, so retrying after some effect writes have succeeded preserves those effects and their timestamps.
The checkpoint is cleared only after progress recording returns.
If an objective update or other progress step throws, the checkpoint remains available for another reconciliation attempt.
The inspected native `ActionList.Run` catches and reports individual game-action exceptions, so the normal engine action wrapper does not inherently require crashing the whole dialogue controller on such a failure.
This is code-path evidence, not an executed failure inside Unity.

One concrete visibility gap remains in the reviewed version.
`ReconcileRecoveries` silently continues when a valid checkpoint exists but its unit status is not restored.
That includes a missing original, changed ID or roster, ineligible faction, and an alive but unconscious original.
After loading a save, the user may have neither a pending explanation nor a selectable dead-only recovery scene.
A valid checkpoint that cannot reconcile should produce a bounded explanation of the failed condition rather than disappear from status reporting.
`recoveryMessage` is also static process state and is not reset on player changes in the reviewed code, so an old save's success message can remain visible after loading another save.
The stored checkpoint is correctly player-owned; the displayed status should be tied to that same player context.

Exact serialized choice matching is intentionally conservative.
It includes visible text as well as effects, so even a harmless copy edit can prevent an existing checkpoint from matching after a mod update.
This safely avoids unauthorized changed effects, but requires a documented migration or manual reconciliation path if pending checkpoints are expected to survive story edits.
It should not be reported as unrestricted update compatibility.

The fault tests invoke the actual `RecoveryAttempt.TryApply` coordinator with an injected delegate that changes the model's life state and then throws.
They meaningfully cover no-credit-on-throw, no-repeat-on-living, unconscious-state rejection, identity/roster/eligibility mismatch, retry while still dead and unknown checkpoint versions.
Their JSON round trip uses a detached checkpoint model.
They do not execute the native resurrection method, the `SettingsList` save path, real player-state inspection, or `Main.RecordProgress` failing between individual writes.
The managed test separately checks serialization annotations, which is useful structural evidence but not a real game-save round trip.
These tests support the bounded coordinator claim and leave the live engine/save behavior unverified.

### Recovery status follow-up

The implementation owner reports adding pending reasons for each saved checkpoint, player-scoped message reset/display guards, and aggregation during each idle pass to prevent alternating log spam.
Those changes address the two reporting gaps above; this follow-up records the owner's resolution rather than a new live-game verification.
The owner also added a real-assembly check for native `SettingsList` serialization annotations and a Newtonsoft JSON string-checkpoint round trip.
Neither check establishes native save/load behavior or fault tolerance inside `Main.RecordProgress`.

### Installed RanRomance route content inventory

The largest mapped route initializer is Targona at 19,004 keyed words, or 18,359 words after exact normalized-text deduplication.
This is a reproducible inventory of localization text referenced by configuration code, not a single-playthrough count or a quality score.
The expansion's full per-character benchmark remains provisional until helper conversations are attributed and branch reachability is assessed.

| Route initializer | Localization keys | Keyed words | Exact normalized-text deduplicated words |
| --- | ---: | ---: | ---: |
| Nocticula | 168 | 6,265 | 6,132 |
| Nurah | 357 | 14,715 | 14,101 |
| Targona | 581 | 19,004 | 18,359 |
| Terendelev | 403 | 15,199 | 14,827 |
| Aranka | 440 | 16,556 | 15,758 |
| Minagho | 394 | 16,324 | 15,790 |

The extraction reads the installed `Mods/RanRomance/RanRomance.dll`, `LocalizedStrings.json`, and `readme.txt` under `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure`.
Input SHA-256 hashes are retained in `reference/art-review/ran-route-word-inventory.json`.
`reference/art-review/RouteInventory.cs` extracts actual IL string literals and resolved method operands without running the mod's configuration or mutating game state.
`reference/art-review/ran-route-il.json` records 835 methods and 2,419 localization entries.
`reference/art-review/route-inventory.py` walks each `RanRomance.{Noct,Nura,Targ,Tere,Aran,Mina}.Main.Configure` entrypoint, referenced callbacks, and visited type initializers.
Each counted key in the resulting JSON has its declaring method, method token, IL offset, and word count.
The loader root `RanRomance.Main+BlueprintsCaches_Patch.Init` is separately walked to distinguish configured helpers from other localization.

The exact tokenizer first computes `plain = " ".join(re.sub(r"\{[^}]*\}|<[^>]*>", "", text).split())`, then counts `re.findall(r"\b[^\W_]+(?:['’][^\W_]+)*\b", plain)`.
Brace placeholders and angle-bracket tags contribute no words, Unicode alphanumerics and digits count, underscores do not count, apostrophe contractions remain one word, and hyphens split words.
Exact deduplication compares the resulting normalized text, not semantic similarity.
Titles, journals, narration, and answers are included when their localization keys are referenced by the route initializer.
This raw total must not be described as meaningful dialogue alone.

The six initializer sets share no exact localization keys with one another.
There are 69 additional loader-configured keys containing 1,138 words in shared helper/revision configuration.
These include Anevia and Storyteller conversations that introduce or check on several routes, alongside universal interface text.
Their route-specific branch conditions have not yet been fully mapped, so these words receive no individual character credit in the table.
Even assigning all 1,138 helper words to Targona would produce 20,142 keyed words, which is a conservative bound rather than an actual Targona count.
Another seven localization keys containing 218 words fall outside the loader walk: four unreferenced Terendelev keys and three referenced Aranka epilogue keys whose methods were not reached.
Static nonreachability alone does not establish that reflection or other dynamic entrypoints cannot use them.
Assigning every unallocated localization word to the largest initializer produces a still more conservative envelope of 20,360 words.
A provisional 21,000-word numerical floor covers that source-inventory envelope, but it cannot guarantee equal quality, meaningfulness, route length in play, or the absence of repeated text.
The full localization total of 89,419 words is not a per-character comparison.

Four merged BlueprintCore helper types failed reflection loading because their installed game dependencies expose inaccessible nested types.
The missing types and exact exceptions are retained in the extraction and report.
Gameplay method inventory was compared with the local type listing, and no inspected method operand failed resolution.
This is bounded source evidence; it does not prove exhaustive dynamic call-graph reachability.

The installed architecture already separates six route initializers from shared Anevia/Storyteller contacts and epilogue/revision setup.
That separation supports the expansion's use of reusable construction and contact helpers while keeping character-owned writing and accounting separate.
Reusing engine code should not confer content credit for another character's dialogue or for a generic shared menu.
The next benchmark step is to trace helper answer/cue conditions to each route, separate universal prompts from route-owned prose, then record mutual exclusions and reachable endings.
The exact initializer inventory is complete under the stated static method; a complete route-attributed gameplay benchmark is not yet complete.

Repeat the inventory with `python reference/art-review/route-inventory.py` after refreshing `ran-route-il.json` with the compiled `RouteInventory.exe` against the installed game directory.
The current report records source hashes so an installation change can be detected before comparing counts.

### Kiana-v1 source-art review

I directly viewed `art/expansion/originals/Kiana-v1.png` and the currently referenced native raster `reference/art-review/kiana-native/ad4aac3138a248646a42424c9e3ca79a_BCT_Kyana.png`.
The reviewed source SHA-256 is `7266ED3754CCAA4C21203D46BF9D56BDD590665E09036AEF622681AE1BCA831C`.
I also read the exact adjacent prompt `art/expansion/originals/Kiana-v1.prompt.txt` and the native appearance adjudication `reference/canon-review/kiana-appearance.md`.
The native raster supports an oread with turquoise skin, angular features, green-blue eyes, tall pale crystalline hair and dark rear mineral strands.
The alternative dark-haired raster is not the portrait currently referenced by the inspected unit and was not used as a likeness target.
The dress and theatrical rehearsal setting are authored additions, not verified native costume or scene reconstruction.

| Observable source-art criterion | Score | Finding |
| --- | ---: | --- |
| Native visual likeness | 28/30 | Preserves blue mineral skin, angular cheeks and nose, pale crystalline silhouette, dark rear strands and green-blue eyes; face is softened into an expressive painted interpretation of a very small native raster. |
| Painting and material quality | 18/20 | Strong warm/cool lighting, convincing plum fabric folds and distinct crystal, skin, paper and wood surfaces; dense gold trim and fairly sharp background detail compete slightly with the face. |
| Anatomy and hands | 14/15 | Arms connect coherently through sleeves, table contact is plausible, and the page grip has no demonstrable extra or fused digit; several digits remain occluded, so their complete anatomy cannot be certified. |
| Adult personality and authored scene fit | 14/15 | The direct gaze and restrained asymmetric smile suggest amused, self-possessed interest; papers, moon prop and borrowed-room furniture support rehearsal, though the elaborate gown gives the scene a more formal tone than a casual practice. |
| Composition and crop potential | 8/10 | Face is readable high in the frame and the full figure has a strong silhouette, but the tallest crystal nearly touches the upper edge, failing the prompt's generous hair margin. |
| Observable source total | 82/90 | 91.1% of assessed source criteria; finished crops and runtime presentation are unscored. |

The page-holding hand shows distinct fingers laid across the lower-right face of the sheet, with the opposing grip plausibly hidden behind it.
The resting hand has a visible thumb and overlapping fingers following the tabletop plane; I do not see a concrete extra-finger, detached-wrist or impossible-contact defect at source resolution.
Occlusion and painterly edges prevent a definitive view of every digit, which is a limit of this pose rather than proof of a defect.
The eyes align with the head angle, the mouth reads as a slight knowing smile, and the neck and shoulders join naturally.
The skin's faceted blue treatment and mineral hair preserve the nonhuman identity without introducing human brown hair or flesh-colored skin.
The crystal arrangement reads as growing from the scalp and continuing behind the ears, although its tall frontal silhouette can also suggest a crown at a glance.
That resemblance is already present in the native raster and is not by itself a likeness failure.

The main practical defect is top clearance.
A portrait crop should retain the upper source boundary and prioritize the face; it cannot promise both generous space over the crystal tips and a complete hair silhouette from this source alone.
For a close dialogue crop, deliberate loss of the tallest tips could be acceptable if consistent with the portrait set, but that choice must be judged on the actual crop.
No small or medium crop was supplied for this review, so thumbnail eye readability, edge clipping and final scaling remain unverified.
The source clears 90% on the bounded visual rubric, with no observed critical anatomy defect.
This does not approve the complete character route, finished portrait package, crop set, deployment, or runtime appearance.

### Kiana-v2 framing revision

I directly viewed `art/expansion/originals/Kiana-v2.png` and compared it with the previously viewed v1 and current native oread raster.
The verified source SHA-256 is `2A216F3E8BB2C49651AD95292D1E7552F1A79C2610C635C28D8B024882D182AD`.
The targeted framing issue is resolved: the highest crystal now has a clearly visible band of background above it, approximately seven percent of the image height by visual inspection.
The entire crystalline silhouette fits comfortably within the source rather than nearly touching the top edge.
The wider composition also preserves both hands, the paper and table contact.

Native likeness remains 28/30, painting quality 18/20, anatomy and hands 14/15, and adult personality with authored scene fit 14/15.
Composition and crop potential rises from 8/10 to 9/10, for an observable source total of **83/90, or 92.2%**.
The face is somewhat smaller in the wider frame, so a dialogue portrait should use a deliberate closer crop rather than simply reducing the entire illustration.
That is a framing tradeoff to inspect in the eventual crop, not a new anatomy or likeness defect.

I see no material regression in turquoise mineral skin, angular face, blue-green eyes, pale crystal growth, darker rear strands, or the small knowing smile.
The paper grip retains separate visible fingers and a plausible hidden opposing grip.
The table hand retains believable contact and wrist alignment; occluded fingers remain an observational limit as in v1.
The flowing plum gown, warm room, papers and theatrical moon preserve the authored rehearsal scene.
The background and gold trim remain relatively detailed, which still competes slightly with the face.
No new critical source-art defect is observed.
V2 is the preferable source for subsequent portrait preparation because it fixes the actual top-edge restriction without a demonstrated identity or anatomy regression.
Finished crops, thumbnail readability, deployment and runtime presentation remain unscored; this review does not require their export now or grant release approval.
