# Jerribeth native recovery observer handoff

Implemented 2026-09-26 for independent review.
This is a read-only prerequisite, not a recovery route or a successful actor return.
Owned files are `src/JerribethRecovery.cs`, `managed-tests/JerribethRecoveryObservationTests.cs` and this handoff only.
No shared registration, builder, story JSON, installed mod or native saved state was changed.

## Release identities

| File | SHA256 |
| --- | --- |
| `src/JerribethRecovery.cs` | `310311521AAF3028B861752B3231CFE65A1D61F71C88952596C4F55CEEB967A3` |
| `managed-tests/JerribethRecoveryObservationTests.cs` | `A76244119139D38C1F9921F95D3EB7CA2ED30C2F446B874376FB9002B221723B` |

The shared reviewed DLL remains `4C3B0CEE5BB412833058A9801C72549790FEA9BEAED7F198A698B0BA2779F286` and does not include this addition.
All compilation used a separate temporary project and output tree.
Root was notified before that full-source isolated compile.

## Implemented contract

`JerribethRecovery.Observe()` returns an observation for each of the four audited native spawners.
It does not select one actor to restore.
The source entries retain exact area GUID, scene name, spawner ID and expected unit blueprint.
An observation contains that immutable source, Evidence, saved ActorId when available and a diagnostic Detail string.
Detail is technical diagnostic text, not player-facing prose.

The evidence values are NotLoaded, Unresolved, NotSpawned, RetainedAlive, RetainedDead, RecordedDeadMissingActor and Conflict.
The observer requires a completed normal load, the current loaded source area, its actual matching scene state and a loaded/postloaded scene.
It reads the native `UnitSpawnerBase.MyData` object from saved storage and checks that the registry resolves the same object.
It then reads `SpawnedUnit.UniqueId` directly, without resolving a UnitReference proxy or invoking a spawner operation.
For a retained actor it requires matching registry object, exact expected blueprint and unique membership in the original source state.
An actor being destroyed or disposed remains unresolved.
The actual native dead/finally-dead properties classify retained life state.

HasSpawned false with a saved death or actor identity is inconsistent and returns Conflict.
HasSpawned true without an actor ID remains Unresolved even when HasDied is true.
HasDied with an identified but unresolved actor returns RecordedDeadMissingActor only when no contradictory storage entry exists.
That state never supplies a replacement actor.
A retained living actor takes precedence over historical HasDied, matching the native distinction between current life and a previous recorded death.
RetainedAlive includes unconscious, hidden or hostile actors and is deliberately not a usable-contact or consent result.

Duplicate source states, duplicate source IDs, inconsistent registry/storage, wrong actor type or blueprint and stale HoldingState are conflicts.
The top-level result also marks an actor ID attributed to multiple audited spawners as conflicting provenance.
Different retained native representations remain separate observations rather than being silently ranked or deleted.
The caller must resolve that history before authorizing any future operation.

Unloaded sources remain NotLoaded.
The code never calls GetStateForArea, GetStateForScene, Unstash, a game deserializer, Spawn, Resurrect, HideUnit, faction mutation or any native history setter.
It reads no unavailable etude and therefore cannot mistake the attack-before-death marker for physical death.
The future coordinator must combine native narrative history with these physical observations without rewriting either.

## Additional exact scene-name verification

The names used in the source were resolved directly from installed `blueprints.zip` before implementation.
`World/Areas/Act_3_DemonsHerecy/IvorySanctum/IvorySanctum.jbp` has AssetId `982abcee3e7b25f459bef22ea22b3ab5` and dynamic scene `IvorySanctumMainPart_Mechanics`, asset GUID `1b3609da30e000d4da2f192527f56b0d`.
`AlushinyrraHigherCityVellexiaPlace_MechaicsBlueprint.jbp` declares `AlushinyrraHigherCityVellexiaPlace_DefaultEtude_Mechanics`, scene GUID `48a42fff8aa13dc46b09c4d230f9aac2`, area `8217b05e37078414981d994151f0ffb1`.
`AlushinyrraHigherCity_VellexiaThirdDate_MechaicsBlueprint.jbp` declares `AlushinyrraHigherCity_VellexiaThirdDate_Mechanics`, scene GUID `d6384baf058b5fc48aff9054c08745e7`, in the same area.
The latter two paths are under `World/Areas/Act_4_MidnightIsles/AlushinyrraHigherCity/Addons/`.
These are actual scene names, not guesses derived from lowercased bundle filenames.

## Validation performed

An isolated project linking all current `src/*.cs` compiled against the installed game assemblies with zero warnings and zero errors.
Its path is `C:/Users/Z/AppData/Local/Temp/jerribeth-observer-n74s45ji/Observer.csproj`.
An isolated net48 runner referencing that DLL and the owned managed test file passed 93 assertions.
Its project is `C:/Users/Z/AppData/Local/Temp/jerribeth-observer-n74s45ji/Runner.csproj`.
The final observer source was recompiled and the 93 assertions rerun after adding the disposed-spawner guard.

Tests inspect actual game SceneEntitiesState, UnitSpawnerBase.MyData, UnitReference, UnitEntityData, UnitDescriptor, UnitState and BlueprintUnit types.
The fixture bypasses constructors and seeds private saved fields by reflection because ordinary actor construction requires Unity.
It does not replace native classes with fake Unity types.
Loaded-scene and registry delegates provide the test boundary for the internal Inspect method.
Actual native UnitState getters distinguish Conscious, Unconscious, Dead and IsFinallyDead states in the tests.

For every audited source, checks cover missing/unloaded/wrong-area source, not-spawned data, contradictory death history, missing saved identity, unresolved reference, recorded death, preservation of the saved actor ID, wrong registry type, retained life/death/final death, unconscious life, destruction pending, wrong character blueprint, duplicate actor and spawner storage, stale HoldingState, absent spawner registration and duplicate scene states.
A final assertion checks that observation preserved the native saved spawn/death/reference/storage fields.
The test does not claim actual Unity loading, native spawner initialization, an authentic serialized save round-trip or real view availability.
The top-level loading guard and cross-spawner reconciliation were inspected but are not exercised through a running Game singleton by this fixture.

Root can register `JerribethRecoveryObservationTests.Run(Check)` in the shared managed runner after independent review.
The new source file is already included by the project's ordinary `src/*.cs` compilation.
No test registration or shared build was performed here.

## Next operation boundary

No Request or Poll method is implemented in this change.
The reviewed plan still requires a saved, fully played agreement, exact current mythic/quest gates, an operation-specific identity and post-operation contact confirmation.
A retained actor would first require a separately reviewed in-place restoration/disposition operation.
Cross-area transfer, missing-body reconstruction and a privately delivered returning representation remain different operations.
None may treat RetainedAlive, RecordedDeadMissingActor or an observation exception as successful recovery.
The observer does not establish absence in other unloaded scenes, and callers must not discard those NotLoaded observations when deciding whether a new body is safe.
An explicit authored romantic refusal must remain effective through every future branch.
