# Jerribeth native contact and Trickster opportunity

Researched from the installed game on 2026-09-25.
The proposed letter experiment is authored alternate development, not a discovered native romance or existing Trickster quest.
No source, blueprint, actor, etude or installed game file was modified during extraction.

## Provenance

The blueprint archive is `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip`.
Its SHA256 is `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.
Blueprint JSON was read directly with Python zipfile.
Native scene objects were read with the existing `reference/asset-extraction-env/Scripts/python.exe` and UnityPy, using read_typetree without exporting or changing the bundles.

| Installed bundle | SHA256 |
| --- | --- |
| `Bundles/ivorysanctummainpart_mechanics.scenes` | `74141EBD521A315B30FFC1760F467774F0D3B4E2CF830ECF14B31FF20C95E0C9` |
| `Bundles/alushinyrrahighercityvellexiaplace_defaultetude_mechanics.scenes` | `D9C0DB60F42C6BEFB205F5E8B0A28B9EF6048D9B0A3321F2E22892E3363050A9` |
| `Bundles/alushinyrrahighercity_vellexiathirddate_mechanics.scenes` | `1B159B3E06822B623D257AB001BEFBBA613EC17C8FC761F9885F00B235D4E977` |

## Verified Act 4 entry

The native unit is `Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Jerribeth.jbp`, GUID `417ce3dcf3a9707488f2b9b2a790814b`.
Its folder name alone does not establish placement; the actual Act 4 spawners below establish that this blueprint is reused there.

| Bundle object | Object path ID | Verified fields |
| --- | --- | --- |
| Default-house Jerribeth GameObject | 43 | Name Jerribeth; component 263 is its spawner |
| Default-house spawner | 263 | Unit `417ce3dcf3a9707488f2b9b2a790814b`; UniqueId `5f976e09-1f17-4f78-907c-fb133d947090`; SpawnOnSceneInit false; RespawnIfDead false |
| Default-house dialog component | 262 | Dialog `992c44e6775d87444b562e855fd64af1`; ConditionsHolder `3f75915712ea4810a3d800d92b4b1eb5` |
| Third-date Jerribeth GameObject | 38 | Name JerribethThirdDate; component 271 is its spawner |
| Third-date spawner | 271 | Same unit blueprint; UniqueId `da348c4f-6c2a-452c-9c20-0d65fdba7168`; SpawnOnSceneInit false; RespawnIfDead false |
| Third-date interaction component | 270 | ActionsHolder `9fd25031f3573ef4392fd730803aa6b2` |

The native dialog is `World/Dialogs/c4/RaptureOfRupture/Jerribeth_Velexia/Jerribeth_Velexia_dialogue.jbp`, GUID `992c44e6775d87444b562e855fd64af1`.
It selects the warning cue before the greeting cue, and has empty StartActions, FinishActions and ReplaceActions.
Its answer list is `AnswersList_0003.jbp`, GUID `19786fae9c29f9d439e374bb857c2e84`.
The list is reused after the greeting, warning and ordinary questions.
That makes it an actual native dialog hook, rather than an inferred actor association.

The existing `jerribeth.refuge_known` binding reads native Cue_0011, GUID `edeeb17ba4f3d124890d22bdd2d8901d`.
That cue establishes her friendship with Vellexia and her role as servant and companion under Vellexia's protection.
It does not establish a sexual relationship, permanent safety, or permission to speak for her patron.
The new proposal requires this existing native knowledge rather than inventing it.

The containing area is `World/Areas/Act_4_MidnightIsles/AlushinyrraHigherCity/AlushinyrraHigherCity.jbp`, GUID `8217b05e37078414981d994151f0ffb1`.
Its m_Parts explicitly includes VellexiaPlace, GUID `9846543a8088ace4db0face47a56b205`.
VellexiaPlace is a BlueprintAreaPart, not the BlueprintArea used by Snapshot.Area.
The `180cdb4b48d561f4cb4ef9a066727960` reference seen in the third-date etude's completion condition resolves to AlushinyrraMediumCity.
It must not be copied as this encounter's area simply because it appears in a related etude.

## Native availability is finite

The default dialog condition is an OR of two branches.
One allows a dialog not previously seen.
The other requires the VellexiaThirdDate etude Playing and the warning cue not seen.
The warning is Cue_0002, GUID `a1f97de9145c3574ebd2d7f75c3d39c9`.
The third-date etude is `World/Etudes/Common/WrathOfTheRighteous/Chapter04_Extra/Chapter04_AreasDefault/AlushinyrraHigherCity/VellexiaThirdDate.jbp`, GUID `02ffbe686c198854da2d51e72fccb9ca`.
It spawns the third-date Jerribeth only when her native dead marker is not Playing.

The most direct opportunity is to hear the refuge explanation and select the added answer while that native answer list is open.
The new book scene does not remove the native DialogSeen condition or force that original dialog to reopen later.
The mod's own manual Read path is separately gated by the observed living actor and chapter/location; it is authored access, not proof that the native conversation is repeatable.
The two delivery paths must be distinguished in runtime verification.

The actual native marker `World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/JerribethDead.jbp`, GUID `cd8666952065ce74d94d960a23482133`, is the existing jerribeth.unavailable binding.
Related native scripts can start it when hostility begins, before physical death is observed.
Clearing that marker alone would not establish a living, friendly actor and must not be used as restoration.

The `ImportantNPCs_fate/Jerribeth.jbp` parent, GUID `cc5e8c94d484b9c48ad32afd6d5c90ef`, has no components implementing resurrection or contact.
Its name is not evidence of a usable fate intervention.
JerribethLovesUsVeryMuch, GUID `d4dcc717dd2f550459bb45ccd91ac240`, likewise must not be treated as romance consent.

## Vellexia's death and Jerribeth's departure

The existing jerribeth.patron_lost binding, `72e423c719ed9d44fa432a6b9629babd`, resolves to `World/Etudes/Common/WrathOfTheRighteous/Chapter04/Chapter04_States/Chapter04_States/VellexiaKilled.jbp`.
It is a Vellexia-death state, not a Jerribeth-death state.
This corrects the overly broad shorthand in the earlier progression handoff that treated the binding only as unspecified lost protection or departure.
Removing the literal Vellexia-death sentence from that earlier prose was conservative wording, not proof that the mapping lacked death semantics.

The native cutscene `JerribethLeavingAfterVellexiaKilled`, GUID `35cdf5be10d187e4da757ead0a9aaebe`, includes two important commands.
CommandAction, GUID `789ac87f3601408e87f78796fb5f1a51`, destroys the third-date spawned unit object.
CommandAction1, GUID `64d5e95655b343dc9998d934a3c85d05`, plays a teleport-style effect on that same spawner.
The referenced scene GUID is `d6384baf058b5fc48aff9054c08745e7` and the spawner ID is `da348c4f-6c2a-452c-9c20-0d65fdba7168`.
These commands provide evidence of departure/despawn, not a resurrection target retained like a companion.
The new physical proposal forbids patron_lost and cannot stop this cutscene.
The later letter can acknowledge an earlier voluntary experiment after departure, but does not place Jerribeth back in the manor.

## Why the Sanctum finale was not selected

The installed Ivory Sanctum scene contains two spawners with the same `Jerribeth_Sanctum` unit blueprint, `bb9fe2c12d6941a43bfd5d5090ac97b9`.
Entrance component 10939 uses spawner ID `9fa07641-a8db-4f01-b43e-28658574e4ce` and spawns on scene initialization.
Final-room component 11314 uses spawner ID `b9c46ad9-ea18-462b-bfef-140a1060348c` and does not spawn on initialization.
Both disable respawning after death.
The final-room dialog component 11315 binds the actual finale dialog `2d00a1654b57d8c4a8df5986c9d6f41e`.

The entrance disappearance command uses HideUnit rather than DestroyUnit.
The final departure command `51b68e36a4c52184ca0ce7e7087620d1` also hides the final-room actor, the Marhevok pot and associated servants.
Its native Cue_0020, GUID `94782ddb38fc0e44ab75314458fbf37b`, starts the departure cutscene.
That script must not be rerun or partially reversed merely to make a romance encounter appear.

The current NativeContact implementation counts matching blueprints before filtering out hidden or otherwise unavailable entities.
The verified duplicate-spawner arrangement is therefore a concrete reason to verify actor selection before promising a final-room hook.
It is not proof that both runtime units are always retained simultaneously, but a naked blueprint match is insufficient evidence that only one can exist.
The root was notified of this dependency.
The Act 4 copies also require runtime overlap testing.

## Authored intervention and implementation boundary

The existing Trickster etude binding is `9f486a9c0c9abfc4a952bb22e88a7e96`.
No Trickster answer was found in the inspected native Jerribeth reveal, finale or Vellexia dialog blueprints.
The new paper experiment therefore remains explicitly authored material inspired by her native greeting's interest in fate, her illusion work and her preference for choosing her own arrangements.

The intervention changes the proposed timing/addressing of a voluntarily written letter within book-scene presentation.
It does not change the game's clock, add a physical item, alter a quest, spawn or restore an actor, compel a response through native mechanics, or grant attraction or commitment.
The actual authored consequences are a completed physical proposal and a later separately readable reply, followed by the existing opportunity to accept or reject correspondence.

No shared-engine extension is needed to represent those two scenes with the existing ContactUnit, AnswerLists, chapter/area, delay and narrow ForbidOverrides contracts.
Assembly, native binding checks, managed construction, actual dialog entry, actor uniqueness and saves still require verification before export.
Universal access after death, hostile departure, or a missed Act 4 opportunity remains unimplemented.
A future restoration would need actual entity provenance, native quest reconciliation and a voluntary new encounter; an authored permission flag cannot substitute for them.

This report records native evidence and integration limits, not release approval or a reviewer score.
