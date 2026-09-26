# Aivu friendship opening: native evidence and authored scope

Source: installed `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip`, inspected directly on 2026-09-26.
The full friendship brief is `reference/story-review/ember-aivu-full-companion-arcs.md`; localization excerpts are in `reference/story-review/Aivu-companion-evidence.txt`.
This opening is friendship only and does not change Aivu's age, species, powers, pet ownership, or native quest results.

## Native identity and contact

| Native record | GUID | What inspection establishes |
| --- | --- | --- |
| `Mythic/Azata/AzataDragon/AzataDragonUnit.jbp` | `32a037e97c3d5c54b85da8f639616c57` | Actual female chaotic-good Azata pet, with native portrait and progression facts; distinct from NPC proxies. |
| `Mythic/Azata/AzataDragon/DragonAzataCompanionFeature.jbp` | `cf36f23d60987224696f03be70351928` | `AddPet` owns the above unit with pet type `AzataHavocDragon`. |
| `World/Dialogs/c3/Mythic_Azata/Island/Dracosha/Dracosha_AzataIsland_dialog.jbp` | `de63e66fbc4992e4caf70ed3e9584cbb` | Native Aivu conversation. |
| Same directory, `Cue_0001.jbp` | `12de733844928794080d3b83ca9d8f82` | Speaker is actual pet `32a...`; points to the main answer list. |
| Same directory, `AnswersList_0027.jbp` | `f1a65c6d838f58d49ad4ff40544b895b` | Ten existing answers, no list-level conditions, no show-once gate; opening attaches additional answers without changing existing ones. |
| `.../MythicAzata/PlayerIsAzata.jbp` | `d3b47e973d65c6c46af1cce815d1f6ce` | Native playing Azata etude; existing story alias `azata`. |
| `.../MythicAzata/AzataQuest_C4/NoDragon.jbp` | `39008f5a372a6dc42bddfcf4f334bd95` | Explicit pet detachment and respec suppression during absence. |
| `.../MythicAzata/AzataIsland_DevilDetachDragon.jbp` | `0ece5844b86deb44ea9d54190de1463e` | Explicit detachment and hiding of the Azata pet. |

The native pet blueprint is under `Mythic/`, which root added to native archive reader coverage during this task.
Both `aivu.absent` and `aivu.detached` are ordinary playing-etude aliases, not permanent historical flags.
They are not added to `PermanentEtudes`, do not use `_dead` or `_gone` suffixes, and therefore follow `IsPlaying` in the existing state reader.
Completing the kidnapping absence etude must permit the returned native pet to become available again; merely having been kidnapped does not permanently close this friendship.
The Chapter 3 restriction prevents this opening from treating a later return as a new pre-kidnapping event.
The scene contact is the existing pet GUID; no `AddPet`, resurrection, spawner, or native etude write is authored.
Native NPC proxies small `8d93d4da064846745809748748df069e`, medium `3e56db348cc24838bc78b55a114e552a`, large `a643ed45374b070468138d16815ca2df`, and Threshold `17f662b11ba74d11b189ca165c736513` are not substituted for pet ownership.

## Capital availability is not yet proven

`PetDragonAzata_ThroneRoom` etude `e4a1eb7ccc927bb41afbe8b20f00861f` links Drezen area part `2570015799edf594daf2f076f2f975d8` and prevents direct control of scene spawner `5f0e977b-e342-4a4d-a52c-0beced8ffc87` in scene asset `828e4d2ac7dffa9429c4d6721e7728c2`.
It does not specify that spawner's blueprint or default dialogue in this archive record.
A scan of all non-dialogue `.jbp` records found the main dialogue reference only in `PetDragonAzata_Nexus`, GUID `8ec49bab42a211e4f85f593718ecc536`, which explicitly overrides the actual pet's dialogue and requires Azata playing and NoDragon not playing.
Consequently, valid unit/list GUIDs do not prove this Chapter 3 capital contact is reachable.
The opening's Drezen area, actual pet presence, and native answer-list attachment must be checked in a real Chapter 3 Azata save, including the outside/throne-room scene transition and actual area identity.
If that default contact is a proxy or a different dialogue, root must supply a verified attachment mechanism before calling this opening playable in game.
The authoring and Rules traversal are ready for review; in-game availability remains unverified.

## Native characterization and chronology

Localization `5b841481-fcb0-4c57-a8d1-63109e4b5d58` establishes that Aivu is very young and that her short name reflects that age.
`de4be337-fc44-4212-9192-e40df0ee4ae2` supports her eagerness to help and delight in being an adviser.
`b7d0f242-33e5-4f76-b2a0-b586ee2baa59` supports impulsive help that can have unforeseen consequences.
`8a01a519-d581-488f-9842-b560129e848a` and `74101757-5d5c-40c0-b391-068fc500564e` concern fear after kidnapping and are not treated as Chapter 3 memories.
`4ef5001e-a3f2-4f03-966d-ca228f061f8e` and `9fab2407-9114-4396-bd3e-a8de454e6852` support later opposition to slavery; this opening does not replay or replace those scenes.
`66aed7d1-3b00-4cee-9b09-278f86c0736e` supports native play with Ember, but this opening does not assume Ember's recruitment or availability.

The map, laundry, Nessa, Jori, damaged awning, blocked cart, arrow-stone, and all new dialogue are authored additions.
They are narrative encounters within dialogue, not spawned NPCs, inventory rewards, animated construction, or native map changes.
Aivu's hesitation at a narrow passage is a new, ordinary fear in the present, explicitly independent of later captivity.
She chooses her own project, admits her accident, learns a practical repair, may leave a blocked passage alone, and asks other people for help without making the Commander her sole friend.
Her existing dragon body and native progression remain intact; no art is generated or approved by this contribution.

## Rescue and guest routes reserved for later

`DragonKidnap` etude `11e19248158944d499686309386f65de` sets up kidnapping mechanics and is not sufficient evidence that a rescue happened.
`03_FreeAivu` objective `e72b7fb157d54d24b8fd29f0ce45d2c0` belongs to quest `1ad9b8fa1fe3cb84b932e8a889fc1897`; neither is written or credited here.
`06_AzataC4QuestEnd`, `cd3c2daa826f24f4ebf73da3158d8692`, has `m_FinishParent: true`.
A later rescue-sensitive continuation must bind actual native completion/seen history, rather than infer rescue from having once been Azata.

`AivuWithLegend`, `1ce861b6b2e110048b89d7d19fc52826`, translocates and unhides a native capital NPC spawner under a conflicting group.
This is evidence of a native non-pet appearance for one specific path, not proof that Trickster has the same visit or power bond.
A bespoke Trickster guest meeting still requires researched location/dialogue access and a voluntary story reason for the visit.
No fake Azata flag, duplicate pet, automatic ownership transfer, universal mythic access, or delivered Trickster route is claimed.
