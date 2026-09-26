# Terendelev persistent materialization API

The installed engine supports spawning a unit with a supplied stable identity and saving it in an explicit scene state.
The return from `SpawnUnit` is not evidence that the actor has reached that state.
Use one Terendelev-specific pending delivery, then confirm the same object in the entity registry and persistent state after the engine's creation tick.
This research does not implement or certify a restored actor.

## Evidence inspected

On 2026-09-26 I decompiled the installed `Wrath_Data/Managed/Assembly-CSharp.dll` with the project's ilspycmd.
Its SHA256 is `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
I inspected `Kingmaker.Controllers.EntityCreationController`, `Kingmaker.EntitySystem.EntityService`, `EntityDataBase`, `AreaPersistentState`, `SceneEntitiesState`, and `Kingmaker.EntitySystem.Persistence.AreaDataStash`.
I also resolved the installed archive's actual Drezen area and outdoor part and read `terendelev-recovery-evidence.md` and its extracted records.
Existing source extracts in `reference/art-review/EntityCreationController.cs` and `SceneEntitiesState.cs` match the API discussed here.

## Creation and confirmation

The relevant overload is `EntityCreationController.SpawnUnit(BlueprintUnit unit, Vector3 position, Quaternion rotation, SceneEntitiesState state, string uniqueId = null)`.
It resolves the blueprint prefab and delegates to the overload accepting `UnitEntityView`.
That overload assigns `unitEntityView.UniqueId = uniqueId ?? Game.Instance.Player.GetNewUniqueId()` and `unitEntityView.Blueprint = unit` before creating entity data.
It catches failures and can return null.
The blueprint overload also returns null for null blueprint, ignored spawners or null holding state.

`SpawnEntityWithView` creates and attaches the view and calls `AddEntity`.
`AddEntity` puts a `CreateEntry` containing the entity and target state into `m_ToCreate`; it does not immediately set `HoldingState`.
`CreationQueue` exposes these entries read-only as an enumerable.
`EntityCreationController.Tick` later calls `createEntry.State.AddEntityData(entity)` and sends spawned-unit events.
Do not invoke the controller's tick manually from a dialogue action.
Wait for its ordinary game update and inspect the result.

The `EntityDataBase` constructor registers the object with `EntityService` before that queued insertion.
Consequently `EntityService.Instance.GetEntity(id)` can find an actor that is not yet durably held by a scene.
`SceneEntitiesState.AddEntityData` logs and returns when its list already contains the same ID.
It only sets `HoldingState` after adding the object.
`EntityService.Register` likewise logs an existing-ID collision without replacing the registered object.
Neither collision can safely be treated as an exception-driven rollback.

A successful delivery must require all of the following together:

- The persisted intended ID resolves to exactly the intended object, with the intended blueprint.
- That object occurs exactly once in the destination's `AllEntityData` and its `HoldingState` is that destination object.
- It is no longer awaiting insertion in `CreationQueue`.
- It has a live usable view, is alive, conscious, not destroyed or disposed, and is nonhostile to the Commander.
- The destination is actually loaded and turned on, the Commander is in the expected outdoor area part, and normal physical-contact conditions pass.

Only then may a route acknowledge physical arrival.
A story flag alone must never satisfy subsequent physical contact.

## Destination and save/load

Drezen area `2570015799edf594daf2f076f2f975d8` uses `DrezenCapital_ThroneRoom_Mechanics` as `DynamicScene`.
Its scene GUID is `6ce2c3528312c234ea1fa410d5e19c00`.
`AreaPersistentState.MainState` is constructed with the area's `DynamicScene.SceneName`, so defaulting to MainState would associate an outdoor arrival with the throne room.

The actual outdoor part is `8a076e720870a44438d13b9b939933fd`.
Its dynamic scene is `DrezenCapital_Outdoor_Mechanics`, GUID `a807c65ecf46d5a4bbbcfa2b45b3f79a`.
The native undead Terendelev spawners instead belong to the additional `DrezenCapital_Default_Mechanics` scene, GUID `3e2b5ea054cd5b2479e7f13134363ef4`.
Do not conflate these three scenes.
For a new outdoor delivery, resolve the outdoor dynamic scene through the loaded area's `GetStateForScene` only after confirming that real scene is loaded.
That method creates a state for an arbitrary name when no match exists, so its successful return does not prove scene presence.
Do not manufacture a new scene state with a guessed name.

The exact final standing coordinate remains unverified.
Use an inspected outdoor anchor and verify ground placement, navigation clearance and camera framing in the real scene before approving delivery.
The native undead spawner coordinates are evidence of those actors' placement, not automatic permission to occupy their spot with a second person.

`SceneEntitiesState` serializes its scene name and entity-data list through JsonProperty.
`EntityDataBase.UniqueId` is also serialized.
`AreaPersistentState` serializes MainState directly.
Its additional states are saved separately by `AreaDataStash.StashAreaState` when `IsSceneLoadedThreadSafe` is true.
States marked `SkipSerialize` can be discarded during disposal.
Require a real loaded destination with `SkipSerialize` false; do not override native persistence settings to force delivery.

`AreaDataStash` restores additional scene files and installs them through `SetDeserializedSceneState`.
`SceneEntitiesState.PostLoad` restores holding-state references and calls entity `PrePostLoad`, which registers the saved identity again.
Duplicate registrations on load can cause a LoadGameException.
The normal serializer and loader should own this process; do not retain an old object reference across saves or area changes.

## Minimal transaction recommendation

Persist only the requested branch/provenance, one assigned entity ID, and whether arrival was confirmed, in the existing per-save mod state.
Use explicit internal states equivalent to not requested, pending, and confirmed; an unavailable scene is pending, not failed resurrection.
Assign and save the ID before spawning so interrupted retries use the same identity.
Before every attempt, search the loaded destination state, registry and creation queue for that exact ID.
Adopt an existing matching saved entity rather than spawn another.
If it is still queued, wait.
If the ID belongs to a different blueprint, conflicting object or destroyed actor, stop delivery and preserve the evidence for diagnosis.
Do not respawn a killed confirmed actor automatically.

After loading a save, wait for the destination scene and normal post-load processing before interpreting a missing registry entry as absence.
An actor in an unloaded scene may exist only in the game's saved scene data.
When the proper scene is restored, adopt by the persisted exact ID and recheck contact.
Do not substitute blueprint-wide matching or move an arbitrary native actor to satisfy the route.

No broad resurrection framework is needed for this first route.
A narrow Terendelev request and pending-delivery checker can implement these operations using the existing update and save hooks.
The implementation must expose pending or unavailable outcomes to the dialogue instead of advancing to a successful return speech immediately after the request.

## Identity conflicts and limits

Living human blueprint `9e8401e7703907e4d94189d5992dd13e` has prefab asset `ec900f647b97f4643a9181bf609d3a89` in the inspected record.
This establishes a candidate visual body, not approval of its original prologue dialog, factions, scripts or combat behavior for an adult continuation.
Audit those blueprint components before reusing it or making a narrowly scoped runtime clone.
The silent-caster human blueprint and living dragon blueprint also do not automatically represent the player's current Terendelev history.

The recovery report identifies native Aeon survival, the Iz Ravener, aware-undead and Lich histories separately.
The known capital undead entity IDs are `9f16b2f6-1ea8-4fa0-b527-ecf4193c71d9` and `3029760c-a252-4c8d-a5e8-60feb18a002c`.
Do not delete all entities sharing their blueprints or mark their native etudes completed as a cleanup shortcut.
An exact conflict policy and any replacement of an existing body remain route-specific implementation work.
An already returned RanRomance finale needs delivery of the established person, not a second narrated resurrection.

Headless tests should cover queued creation, null spawn, registration without state insertion, duplicate-ID rejection, wrong-blueprint adoption, retry before and after confirmation, save-state recovery and missing destination.
Real saved-game verification must cover save/reload before and after the creation tick, moving between throne room and outdoors, leaving and revisiting Drezen, and the relevant native Terendelev bodies elsewhere.
This report establishes the transaction API and persistence mechanism but does not certify those runtime outcomes.
