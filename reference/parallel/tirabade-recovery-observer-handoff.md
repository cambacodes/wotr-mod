# Tirabade saved-actor observer handoff

This change observes five exact native spawners without creating, loading, reviving, moving or unhiding an actor.
It is an implementation prerequisite awaiting independent review, not an implemented recovery route.
Only the assigned source, managed test and this handoff were changed.

## Files and contract

- `src/TirabadeRecoveryObserver.cs`: `5D2A772B15E2B98FDF89828A647CAB77360F64634A95600EF49F4BB4CB75872D`.
- `managed-tests/TirabadeRecoveryObservationTests.cs`: `5A4DDFC80D8187015B5F0D78279DFF63C41E6939367863DBCF00CC8B7530B7F6`.
- `src/JerribethRecovery.cs`: `310311521AAF3028B861752B3231CFE65A1D61F71C88952596C4F55CEEB967A3`.

`TirabadeRecoveryObserver.Observe()` returns one `JerribethRecovery.Observation` for each audited source.
The observer directly reuses `JerribethRecovery.Source`, `Evidence`, `Observation` and `Inspect`.
It does not duplicate native storage, spawner or life-state inspection logic.
The existing Jerribeth source was read but not edited.

The five results retain both capital representations and all three Iz alternatives.
Wrong or unloaded areas remain NotLoaded, and missing saved references remain Unresolved or RecordedDeadMissingActor as appropriate.
Every result keeps its source and saved actor ID.
Two source spawners claiming the same actor ID are marked Conflict on both results.
Distinct living and dead Iz representations remain separate observations; callers must reconcile them before considering any operation.
There is deliberately no aggregate Alive, Recovered, Available or Eligible result for either woman.

A living capital actor therefore proves only that representation's retained life state.
It cannot prove that the actor killed at Iz survived, that another scene is empty, or that the woman has agreed to return.
A view is not required for retained-life observation and no result grants physical contact.
The existing NativeContact checks remain necessary for any later conversation.

## Verified native source table

| Source | Area | Scene name | Spawner | Blueprint |
| --- | --- | --- | --- | --- |
| Anevia capital | `2570015799edf594daf2f076f2f975d8` | `DrezenCapital_Default_Mechanics` | `86b332a9-5910-4d46-9951-8e06f7dcf0cf` | `b5e867e13503c6f41bb1316705efb4a2` |
| Irabeth capital | `2570015799edf594daf2f076f2f975d8` | `DrezenCapital_Default_Mechanics` | `3dc302d8-58ce-44f3-9766-2a437a080108` | `280d4712dceb37f4a88e98f1f4c6e64f` |
| Irabeth monster lair | `2ccc6731787b6ec41ab5adc13f1b9ce9` | `Iz_Default_Mechanics` | `8b5b891b-a569-42c0-a7dd-7177760fa64a` | `9adfeebc39054544fa0f924022e43c1c` |
| Irabeth manuscripts alternative | `2ccc6731787b6ec41ab5adc13f1b9ce9` | `Iz_Default_Mechanics` | `bf142b5f-85f6-439e-9e23-f23646e22401` | `9adfeebc39054544fa0f924022e43c1c` |
| Irabeth manuscripts | `2ccc6731787b6ec41ab5adc13f1b9ce9` | `Iz_Default_Mechanics` | `d16d93ee-d53c-43da-9d0a-ff27eea9d15e` | `9adfeebc39054544fa0f924022e43c1c` |

The capital sources are documented in `reference/canon-review/tirabade-capital-contact-records.json`.
The three Iz sources were extracted from the actual Unity bundle and documented in `reference/canon-review/tirabade-trickster-recovery-design.md`.

The exact Iz scene name was independently resolved again for this implementation from the installed archive, not inferred from the lowercase bundle filename.
`World/Areas/Act_5_HeraldOfTheIvoryLabyrinth/Iz/Addons/Iz_Default.jbp`, asset `7bc4a3c8f40f036458c0fd0364426379`, sets `Scene.m_SceneName` to `Iz_Default_Mechanics`.
Its scene asset is `7dda2cdd7612d8f4ea4996822783c02d`, and its Area is the Iz area above.
The source-byte SHA-256 is `A5C484D6C0A2DAC3122C97B7A25F2E420EC291863BDDF7B55E812E2E750BB51C`.
`World/Etudes/Common/WrathOfTheRighteous/Chapter05_Extra/Chapter05_AreasDefault/Iz_Default.jbp`, asset `d44c5bb992ad6d74aa5efeabbca3444d`, includes this mechanics asset in `m_AddedAreaMechanics`.
Its source SHA-256 is `F6CB869FE3D7106C84F239D71FE26E43D715035E048D104C497EC20507FCA96B`.

## Verification performed

An isolated all-source net48 project compiled against the installed managed assemblies with zero warnings and zero errors.
The project is `C:/Users/Z/AppData/Local/Temp/tirabade-observer-mvuso3bn/Observer.csproj`.
An isolated managed runner passed 154 assertions using the final owned test source.
The runner is `C:/Users/Z/AppData/Local/Temp/tirabade-observer-mvuso3bn/Runner.csproj`.
No shared output directory was built or overwritten.

The fixture uses actual native SceneEntitiesState, UnitSpawnerBase.MyData, UnitReference, UnitEntityData, UnitDescriptor, UnitState and BlueprintUnit objects.
It bypasses constructors and seeds saved private fields because normal entity creation requires Unity.
Only the loaded-state and registry-lookup boundaries are supplied as delegates to the observer's internal Inspect method.
The native life-state getters run in these tests.

For all five sources the tests cover missing spawner, unloaded source, wrong area, unspawned data, contradictory death without a spawn, missing actor ID, unresolved saved actor, recorded death with absent actor, wrong registry type, living/unconscious/dead/finally-dead states, destruction, wrong blueprint, duplicate actor and spawner storage, stale HoldingState, registry disagreement and duplicate scene states.
Cross-source checks exercise two spawners referencing one actor and require conflict on both claimants.
Separate Iz actor IDs with one living and one dead body remain individually reported, preserving all five result entries.
A retained living fixture has no usable Unity view, and all sources in the other area remain NotLoaded.
This establishes that retained life is not being substituted for cross-area evidence or physical contact.
Final assertions verify saved spawn/death/reference/storage data was not changed by observation.

## Deliberate limits and next integration

The top-level Game singleton loading guard is compiled and inspected, but is not exercised by a real running scene in the fixture.
No actual saved-game deserialization, Unity hide/show operation, actor view, navigation, transfer or resurrection is certified.
The no-view fixture is not a claim that a real hidden capital actor was loaded in this test.
Native death, departure, Queen, quest, morale, relationship and refusal histories are neither read as a substitute for actor evidence nor modified.
A future caller must combine the observations with those histories and an earned voluntary agreement.

The observer's internal Inspect method is a testable loaded-area boundary, not an API for manually loading missing native scenes.
Do not construct missing scene states to force a result.
Do not discard NotLoaded observations when deciding whether another representation may survive.

Root can register `TirabadeRecoveryObservationTests.Run(Check)` after independent review.
The production project already includes the new source through its normal source glob.
No caller, test registration, new blueprint, story binding, native-flag override or recovery operation was added here.
