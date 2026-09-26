# Soana later access and recovery audit

## Result and scope

The smallest supported next step is a living Chapter 5 reunion at Soana's original Wintersun outdoor contact.
Installed scene and blueprint data show no Chapter 3-only restriction on that actor, its postquest conversation, or the default mechanics that own it.
This is strong static support for a return, not a completed Chapter 5 save replay.
The current authored route's `Chapters=[3]` restriction is a mod restriction; it should not be described as proof that native Soana disappears after Chapter 3.

Dead Soana requires a separate restoration implementation.
Camellia's scripted killing and ordinary combat death produce different physical states, and neither changing a route flag nor loading Wintersun again restores her.
Released Orso is also distinct from a combat-dead bear, a hidden bear after the confrontation, and the cinematic bear spawned after Soana's death.

This audit reads the installed `blueprints.zip`, three Unity scene bundles and `Assembly-CSharp.dll` without writing to the game.
The reproducible probe is [probe-soana-late-access.py](../../tools/probe-soana-late-access.py); extracted records and decompiled types are in [soana-late-access-records.json](soana-late-access-records.json).
Earlier dialogue and localized character evidence remains in [soana-route-evidence.md](soana-route-evidence.md).
No story, art, relationship rules or native saves were changed for this audit.

## Exact location and chapter lifetime

| Object | Native identifier | Observed behavior |
| --- | --- | --- |
| WintersunOutdoor area | `0a5654e7dc18f074d9356009d55eb51b` | Owns the outdoor encounter and lists the separate ForestCave area part. |
| Default mechanics addon | `198b62fe2afa9da4cb314f1b4376b0b9` | Loads scene `5f4ad31583f5c284ab3889c7c5d9cd26`, which contains Soana. |
| Wintersun_Default etude | `87839550c801db944b102f61084fd245` | Adds those mechanics; linked to Wintersun including its parts; empty activation/completion conditions. |
| Chapter03_AreasDefault | `19c0886c9e105ea4a832eec08321ac0f` | Parent of Wintersun_Default; empty activation/completion conditions. |
| Chapter03_Extra | `2d9c51e422e743947bfa0281d0a2db51` | Parent of AreasDefault, itself parented to campaign root `f0e6f6b732c40284ab3c103cad2455cc`, not the Chapter03 etude. |
| Chapter03 | `15e0048c7daf0ac4999c2313b58df0e3` | Starts Chapter03_Extra through `m_StartsWith`; this does not make it the latter's parent. |
| Global map location | `ef2c34c4a052e294cbdb289be35017bb` | Not hidden, not closed on start, initially unrevealed; reveal condition tests Chapter03_Extra Playing. |
| Outdoor entrance | `01398d25f68112646bd9d01179209182` | Entrance referenced by that location. |

Paths are under `World/Areas/Act_3_DemonsHerecy/WintersunOutdoor/`, `World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/`, and `GlobalMaps/WorldWoundGM/Points/Location_WintersunOutdoor.jbp`.
Folder names and `PS4ChunkId=Chapter3` are not runtime chapter predicates.
The point has no alternate location variants or on-enter actions in the inspected record.
Its three adjacent edges have empty `LockCondition.Conditions`: `0b46fa4b18c84524d89609aa930a342a`, `ce87e20ce019830499eeeb681b2cc75f`, and `a6b3a914cc4189f4ba4ad12c4c0a2315`.

The probe scans all installed `.jbp` records for typed objects directly referencing the six recorded access/lifetime targets.
It finds the native `UnlockLocation` in `World/Dialogs/c3/Drezen_C3/Irabeth_C3_Intro/Cue_0079.jbp` and no direct completion/closure action targeting those etudes or the location.
This bounded scan cannot exclude every indirect evaluator or a corrupted/custom save.
Decompiled `SwitchChapter.RunAction` calls `Player.SetChapter` and resets trader limits; the inspected `EtudesSystem` does not implement the chapter-change handler.
No automatic expiry based on an etude's folder name was found.

The ForestCave entrance is a different object from Soana's contact.
`Exit_to_ForestCave`, entity `766f0a0e-867e-40c5-a241-d6b3c3f374bc` in main scene `9a45a0ce7012543499039089e16f6f86`, starts with `m_IsInGame=0` and targets enter point `afb1fed1de261fd478e482bfc6a6c795`.
A repeatable play trigger in Wintersun_Default unhides it if SoanaForest quest `831a725b62c18a443a1d00e4266323a2` is Started, Completed or Failed.
Its interaction has no visibility flag or visibility etude of its own.
Thus a completed/failed quest is not evidence of a permanently sealed cave.
Actual entrance state still needs observation on the save used for acceptance.

A Chapter 4 remote conversation, Abyss relocation, capital actor or universal later-act guest is not supplied by these records.
The proposed next release should explicitly support Chapter 5 at Wintersun, with ordinary world-map access, rather than treating a chapter flag as a teleport.

## Actor and reusable conversation

`Spawner [Soana_Wintersun]` is GameObject path ID 128 in `wintersunoutdoor_mechanics_default.scenes`.
Its exact scene entity is `8f576b8a-4c79-4f42-a575-d0b27b0f5bb1`, using BlueprintUnit `64805abb52739e44280a758f850b300c`.
The spawner and its ForestQuest/Spawners parents are active; `m_IsInGame=1`, `m_SpawnOnSceneInit=1`, `m_RespawnIfDead=0`, and the spawn condition reference is empty.
Its spawn action holder `c6738bf1a8f74dc8b0a1762a721e1eb6` adds native buffs/Aeon handling, not a Chapter 5 deletion.
No second Soana actor was found in the inspected ForestCave or main mechanics selections.

The original actor has three click-dialog interactions:

| Stage | Condition holder | Dialog |
| --- | --- | --- |
| BeforeBear | `e933bd0d9a7abb44dab81e26d7f7ebda` | `856b97bf54e34384796883fa777e583c` |
| AfterBear | `e0fb56ddcc051f44eab3b23196c0ae0c` | `8d3b74ead4775034db1bc842d0db5df6` |
| AfterQuest | `45899992167597b49bb016b2d9ac4e4d` | `1a2202cb676601344942aed3edab7498` |

The postquest holder tests only Playing on SoanaAfterQuest `fccdd316924af204da00c99f01c0e222`.
It does not establish physical life or nonhostility.
The dialog has empty conditions/finish actions and reusable answers list `2b1776f3e398685479ff6b16290b4cc2` with ShowOnce false.
This supports a new later-act option on the existing contact after checking actual speaker identity, life, presence, hostility and earned route history.
It does not justify completing missing native stages to manufacture the contact.

Native postquest answer `41427b1b6e18d2b46a8710deb79d4266` can still start combat with this actor and add the clay medallion to her inventory.
A living hostile actor must remain unavailable to ordinary romance entry.
Restoration must not repeat that action, grant another medallion or silently erase hostile history.

## Outcome distinctions that recovery must preserve

| Native history/state | Physical or narrative meaning | Consequence for a new route |
| --- | --- | --- |
| Spared, OldDefender `c97882cbc65c4c546aed1810627a5b81` | Existing guardian arrangement continues. | Living return can discuss the coercive binding; it is not proof of mercy or a healthy free Orso. |
| Left to seek replacement, NewDefender `bc435ec57d3151c489d760ecfd4c3289` | Soana says she will seek another defender. | No new guardian actor is spawned by this etude; do not claim a successful replacement. |
| BearDead `995f0ac2951bbb041b062806c163fbf1` | Started by the native fight bear's death trigger. | Distinct from merely finishing the bear dialog or hiding the actor. |
| Medallion release cue `945035f8ed0d1474abcb700b985bc5a3` | Native narration describes destruction of the medallion and Orso withering to pelt and bones. | Track release history separately; do not reclassify it as an alive rescue. |
| SoanaDead `d4b624463e52e21438da6f4870320fee` from combat | ForestQuest death trigger also starts ForestDead. | Inspect the saved actor's dead/finally-dead state; normal scene loading will not respawn her. |
| SoanaKilledByCamellia `f102a4d0677148f4cab007f901a5ed3c` | Starts SoanaDead; cutscene hides the actor and displays a separate corpse. | May leave a mechanically alive but hidden unit; do not blindly use a dead-unit operation. |
| ForestDead `ff0d7227c56b2b0488b006893b96040e` | Completes both defender etudes; used by later native outcome material. | Preserve as history until a separately implemented forest recovery reconciles downstream consequences. |

OldDefender can also follow approving suffering, so it must not serve as a benevolence flag.
OldDefender and NewDefender are parented to WintersunStory `86dbec7294a940c468d295b4e0ba97c9`, itself under AreasDefault; their disk folder is not their actual parent relationship.
AfterBear finish actions hide fight-bear spawner `0b9f79f0-01b9-4855-b43e-41e69b26061d` and complete objective `dd1b3a09ebc3f7d40adf973fec9917ce`.
Therefore a hidden bear after a peaceful confrontation does not establish death.

The Camellia cutscene is `875a2bfc47ea6b444be86ddf2624c5d9` under `World/Cutscenes/WintersunOutdoor/CutsceneCamellia_killSoana/`.
Command action `49a65ec06d9109d4599ff957f09fffd1` unhides corpse entity `966bb0bc-4937-4e6a-b1af-314fa0a4e468`, hides the original Soana unit and starts ForestDead.
No KillUnit action was found in the inspected complete cutscene command set.
The corpse is an initially hidden map object, not a second dialog-capable Soana actor.
Native narrative death remains true even if the original hidden unit is mechanically alive.

Orso's release cutscene `afd7f4cc58b08ea4a9ce7d971df4000b` attaches NPC_Untargetable buff `d616ce293b89af14e839c846554b2ccb`, plays effects and hides the fight-bear unit.
Its inspected commands contain no KillUnit or direct BearDead start.
The earlier cue removes medallion item `4d78ec5dd1d1d5d41b9f2d8f2c8b5d53`.
The separate after-Soana-death cutscene `d859223e3fc689d4bb5c1a83c0a961c9` spawns cinematic bear entity `7fb0924c-4917-437d-9f4a-bcb2b5ae64e2`, changes its faction, plays effects and hides it.
Both bear actors use unit blueprint `cca3387e88317974da2c37693cd7591a`; matching the blueprint alone cannot establish which saved bear was restored.

## Attainable investigation and authored Trickster intervention

Native Soana dialog supplies concrete material: the shared life binding, the clay knot and matching bear brand, her fear of losing the forest, and the old letter from Roan.
The inspected main Soana dialog does not itself offer a Trickster resurrection answer.
A new fate intervention is authored alternate development and must be presented as such in planning and review.
Existing Perception DC 25 check `637a490ae7017dc4699ef297c042f2ee` and LoreNature DC 27 check `5334e0782bedf3948a8bdfa698d5efa9` support inspection as an established encounter activity; they do not grant resurrection powers.

The letter has a verified physical producer.
`MessageRoana` is entity `8f22cf08-36af-4dbc-a2c1-28b7983a6091` in the outdoor main scene.
Taking specific item `1873d2826ecbc2c4b8dc488c9c22d4b3` fires action holder `54b2da306959efd4683087d9841d21fa`, starts LetterFromRoan `9987d3c8b2c0969438c17ec84bc781f4`, gives objective `ca5963a3530980345a55809997313544`, and changes the original Soana actor's displayed name.
The flag proves this take trigger ran, not that a new relative has been found alive.
The DLC4 SoanaDaughter blueprint exists, but its guest availability and quest lifecycle are outside this audit; it must not be a required unverified messenger.

The proposed Trickster route can challenge the binding's assertion that one life must secure the forest, using the actual place, known participants and the contradictory survival/death histories as its subject.
For a living Soana, negotiate with her at her native contact before any change to the guardian arrangement.
For dead Soana, introduce a new investigation interaction at the verified death location, then an authored restoration encounter before opening romance contact.
For released Orso, use the recorded release and remains described in the native scene; requiring the intact medallion would make that branch impossible.
A present medallion can be an alternative investigative aid, not the sole universal key.
A failed investigative check should cost information, time or a negotiated favor and leave a non-roll continuation; it should not permanently exclude a Trickster from an otherwise required route.
Recovery must not force affection or erase Soana's response to the Commander or Camellia having killed her.

These are implementable route designs grounded in inspected hooks, not claims that the current build delivers fate changes.
Other mythics retain their own eligibility restrictions; no generic all-mythic resurrection is proposed here.

## Smallest implementation sequence

1. Add a bounded Chapter 5 reunion at the existing postquest contact for living, present, nonhostile Soana with earned predecessor history.
   Keep the existing Chapter 3 scenes and IDs intact, and give missed earlier content an explicitly designed catch-up policy rather than moving every scene to Chapter 5.
   Validate the actual Chapter 5 save's area, default etude, speaker and native dialog before calling this playable.
2. Add Trickster investigation at that living contact, plus a separate death-location entry for the killed branches.
   Store branch history for combat death, Camellia's killing, Orso release, BearDead and the native quest stage without overwriting those native outcomes.
   Author the recovery-specific dialog independently of the ordinary relationship's hard unavailable flags.
3. Implement physical restoration only after observing each saved-state class.
   Resolve the exact original spawner's saved UnitReference, distinguish hidden/alive from dead/finally-dead and missing, reconcile corpse visibility, and provide the correct recovery dialog without completing unrelated native stages.
   Use a new verified restoration state to permit recovered contact while preserving historical death flags and downstream forest consequences.
   A missing original actor needs a separately reviewed reconstruction strategy; it is not handled by setting that state.
4. Develop the restored relationship and forest/Orso consequences as later campaign content, with explicit authored alternatives where native outcomes change.
   The earlier aggregate word floor does not establish multi-act delivery or RanRomance parity.

Current relationship `UnavailableFlags` include `soana.dead`, `soana.killed_by_camellia`, and `soana.forest_dead`.
Consequently an ordinary scene-level exception alone cannot deliver recovery.
The later implementation needs an explicit restored-contact rule and recovery entry outside that blanket block, rather than deleting native history.

## Physical implementation cautions from the installed assembly

`UnitFromSpawner` returns the saved spawner UnitReference; it does not spawn a unit.
`HideUnit` changes `IsInGame`; it does not kill, heal or resurrect.
`UnitSpawnerBase.HandleAreaSpawnerInit` respawns a previously spawned dead unit only when `m_RespawnIfDead` allows it, which Soana's spawner does not.
`TrySpawnOrRespawn` and `ForceReSpawn` can mark the previous noncompanion for destruction and replace saved spawner data, so they are not safe substitutes for preserving an existing actor's identity.
`CommandReviveUnit` explicitly excludes `IsFinallyDead` and handles unconscious/dead units through return-to-consciousness logic; its name is not evidence of a complete resurrection solution.
The actual finally-dead restoration API and its inventory/faction/serialization behavior remain to be validated before implementation.

## Required acceptance evidence

Static extraction can verify scene ownership, GUIDs, predicates, action order and code behavior; the supplied probe does so without opening game windows.
It cannot establish a particular save's living actor, corpse visibility, native cutscene completion or successful re-entry after an actual chapter transition.

| Acceptance case | Required observation |
| --- | --- |
| Living OldDefender and living BearDead/seek-replacement histories | Real Chapter 3 to Chapter 5 return, original unit identity retained, postquest native dialog opens, correct new branch appears. |
| ForestCave after started/completed/failed quest | Entrance visible and traversable under its native trigger; no assumption that Soana herself is inside that separate scene. |
| Hostility after postquest attack answer | Romance unavailable during hostility; no faction reset as a side effect of inspecting eligibility. |
| Combat-dead Soana | Original unit and spawner death state recorded; no restoration or duplicate actor on area reload alone. |
| Camellia-killed Soana | Hidden original unit and corpse state recorded independently of narrative death flags. |
| Released Orso and cinematic bear | Release history preserved, destroyed medallion not required, correct saved actor distinguished from cinematic copy. |
| Interrupted restoration and save/reload | Either no physical changes or one coherent completed restoration; no duplicate units/items, early romance unlock or contradictory corpse. |
| Repeated/reloaded new contact | No repeated recovery reward, quest completion, native flag clearing or auto-commitment. |
| Trickster eligibility | Actual path predicate and earned investigation used; other mythics do not acquire the same access accidentally. |

No runtime restoration, Chapter 5 reunion, recovered forest or comparative full-route approval is claimed by this research release.
