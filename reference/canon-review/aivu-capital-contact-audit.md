# Aivu capital contact audit

The native asset chain supports Aivu's existing-pet conversation in Drezen's throne room.
The requested spawner uses the Commander's actual Azata havoc dragon and attaches the expected native dialogue and answer list.
It is not a second Aivu or an NPC proxy, so this investigation finds no need to replace the opening's ContactUnit or invent a new actor.
This closes the previously missing asset-binding evidence, while a loaded-save UI test remains outstanding.

## Reproduction and sources

Run `reference/asset-extraction-env/Scripts/python.exe tools/probe-aivu-capital-contact.py` from the project root.
The read-only probe extracts the installed Unity scene, relevant blueprint records and decompiled native classes into `aivu-capital-contact-records.json`.
The resulting record contains three relevant scene objects, their components and parent transforms, 36 native blueprint records and seven decompiled classes.
No game asset, native state, source module or shared export was changed.

| Inspected input | SHA256 |
| --- | --- |
| `Bundles/drezencapital_mechanics_mythicazata.scenes` | `BE0DD5C3B341A5F5D0DC636462B9E4C1DB112AE19BCB34B12E9373AAD189324E` |
| `Wrath_Data/Managed/Assembly-CSharp.dll` | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |

The scene mapping is explicit in native `World/Areas/Act_3_DemonsHerecy/DrezenCapital/Addons/DrezenCapital_MythicAzata.jbp`, GUID `69bf5090bc7e2f34f83b73e64972f54b`.
It names `DrezenCapital_Mechanics_MythicAzata`, links scene asset `828e4d2ac7dffa9429c4d6721e7728c2`, and belongs to area `2570015799edf594daf2f076f2f975d8`.
The playing `PlayerIsAzata` etude `d3b47e973d65c6c46af1cce815d1f6ce` lists this mechanics blueprint in `m_AddedAreaMechanics`.
This is an exact mapping, not a bundle chosen merely because its filename contains Drezen.

## Exact throne-room object

GameObject43 is `AzataDragon_ThroneRoom`.
Its three components are Transform160, CompanionSpawner322 and SpawnerInteractionDialog321.
The serialized MonoScript records independently identify the latter two classes and their Assembly-CSharp namespaces.

| Spawner322 field | Value |
| --- | --- |
| UniqueId | `5f0e977b-e342-4a4d-a52c-0beced8ffc87` |
| m_Blueprint | `4391e8b9afbb0cf43aeba700c089f56d` |
| m_UsePet | 1 |
| m_IsPlayerPet | 0 |
| m_PetType | 2 |
| m_SpawnOnSceneInit | 1 |
| m_SpawnWhenInCapital | 1 |
| m_SpawnWhenRemote / m_SpawnWhenEx | 0 / 0 |
| ShowCondition | `a55dfc5df40b491d92a873a6e29f6412` |

The apparent blueprint mismatch is explained by the actual spawner implementation.
`4391e8b9afbb0cf43aeba700c089f56d` is `Units/Pregens/StartGame/StartGame_Player_Unit.jbp`, the owner lookup.
`CompanionSpawner.GetMyCompanion` finds that character using `CheckEqualsWithPrototype`, then, because m_UsePet is true, selects the existing pet whose UnitPartPet.Type matches m_PetType.
The native enum makes value2 `AzataHavocDragon`.
`DragonAzataCompanionFeature`, GUID `cf36f23d60987224696f03be70351928`, supplies the actual unit `32a037e97c3d5c54b85da8f639616c57` with that pet type.
The spawner's SpawnUnit override returns GetMyCompanion and calls BeginControllingCompanion; it does not instantiate the owner blueprint or manufacture another dragon.
The serialized m_IsPlayerPet value does not override that inspected GetMyCompanion logic.

Transform160 places the actor at approximately `(218.617, 79.207, 14.826)`.
Its parent Transform134, GameObject17 `Spawners`, has identity position, rotation and scale.
These are therefore world coordinates in the inspected scene.
They document the native placement, not a proposed new spawn location.

## Dialogue attachment and entry

SpawnerInteractionDialog321 points directly to `de63e66fbc4992e4caf70ed3e9584cbb`, `Dracosha_AzataIsland_dialog`.
Its own Conditions reference is empty and TriggerOnApproach is false.
The Island name in the dialogue asset does not restrict this component to the island; the same native dialogue is explicitly attached here.

The decompiled `UnitSpawnerBase` initializes its IUnitInitializer parts on spawn and view reattachment.
`SpawnerInteractionPart.OnInitialize` adds the interaction wrapper to the actual unit's UnitPartInteractions; OnDispose removes it.
The wrapper uses normal spawner interaction priority and rejects a helpless target.
`SpawnerInteractionDialog.Interact` calls `StartDialogWithUnit(Dialog, target, user)`.
`CompanionSpawner` also reapplies or disposes initializers when its existing companion's placement changes.
This establishes how the scene component becomes an interaction on the reused pet.

The dialogue has twelve random initial cues.
Ten point directly to main answer list `f1a65c6d838f58d49ad4ff40544b895b`.
The two special initial cues use AnswersList0013 and AnswersList0020; their ordinary answers lead through Cue0017/0018 and Cue0023/0024 respectively, all returning to the same main list.
One special greeting has an etude condition and both special greetings are show-once, but the main-list path is not confined to them.
The main list itself has no conditions and is not show-once.
Thus the opening's existing answer-list target is supported through every inspected native initial greeting, rather than requiring a fortunate random greeting.

## Capital versus outdoor placement

ShowCondition `a55dfc5df40b491d92a873a6e29f6412` is an AND of CurrentAreaIs DrezenCapital and UnitIsInAreaPart for the player character against `2570015799edf594daf2f076f2f975d8`.
The latter condition checks the referenced area's MechanicBounds.ContainsXZ against the player's position.
The parent area's own dynamic/static scenes are DrezenCapital_ThroneRoom_Mechanics and DrezenCapital_ThroneRoom_Static.
Its outdoor part is the separate `8a076e720870a44438d13b9b939933fd`, with DrezenCapital_Outdoor scenes.
The show condition therefore describes the throne-room placement, not an unconditional outdoor capital appearance.
The spawner also requires native CapitalPartyMode and an eligible existing pet not hidden by its pet/companion state.
Its control logic respects another current spawner and IgnoresSpawners rather than seizing an actor already controlled elsewhere.

The same bundle contains GameObject39 `AzataDragon_Coronation`, CompanionSpawner317, with SpawnOnSceneInit false and no attached conversation component.
GameObject58 `AzataDragon_OutdoorCoronation` is a LocatorView, not another pet or a free-roaming dialogue proxy.
Native Coronation_Azata can unhide and translocate the throne-room pet to that locator for its own sequence.
That special sequence must not be generalized into permanent outdoor contact.

The opening's Areas value remains appropriate because `Main.State()` records CurrentlyLoadedArea, not the current sub-area part.
Its actual clickable entry is the existing throne-room pet conversation.
The narrated laundry outings can depart from that meeting within the book scene without pretending the mod has placed an outdoor laundry actor.
Player-facing guidance should say to speak with Aivu in the throne room during Chapter3, rather than imply that any outdoor view of Aivu offers this entry.
No new pet, ownership change, forced native etude or proxy ContactUnit is needed.

## Remaining verification

This is positive static evidence for a real Chapter3 Azata route to the native list, conditional on the existing pet and ordinary capital state.
It supersedes the earlier evidence statement that no capital dialogue attachment had been found.
It is not a report of a played save.

The small remaining live check is to enter the throne room with the existing Azata pet, open its native conversation, verify the added answer, finish a visit, reload, and return after its delay.
Check an outdoor/throne-room transition and ensure no duplicate actor or repeated completed book appears.
The current NativeContact guard additionally requires exactly one matching loaded, conscious, living, friendly pet in LoadedAreaState.AllEntityData.
A real save must verify that native pet holding-state membership satisfies that guard during the throne-room interaction; the component binding alone does not prove that collection membership.
Native die execution and rendered dialogue remain separate UI checks.
Nothing in this research supplies a non-Azata or Trickster Aivu, a rescue continuation, artwork or a completed full friendship route.
