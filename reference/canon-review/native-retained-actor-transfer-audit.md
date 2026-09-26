# Retained native actor movement audit

Installed-source audit, 2026-09-26.
Both assigned report/probe paths were unused when this task began.
No game save, installed mod, shared engine or character manuscript was changed.
I applied the ponytail and unslop skills to keep the proposed operation small and the findings explicit.

## Decision

`TranslocateUnit.RunAction` is a verified native operation for moving an existing actor within its loaded scene environment.
It does not transfer saved ownership between scenes or areas.
I did not find a supported identity-preserving cross-area transfer operation in the inspected APIs and callers.
This is a bounded negative finding, not proof that no such method exists anywhere in the game.

Proceed first with a living-departure encounter in the actor's own retained capital scene, subject to an explicit solution for native hide/position conflicts.
For an Iz actor, keep any proposed first encounter in its own loaded Iz state until a cross-area storage operation has been separately demonstrated.
Neither recommendation authorizes resurrection or proves that a particular old save retains the required actor.
Do not implement remove-and-add, cross-scene party storage, blueprint replacement, or a clone as a shortcut.

## Installed evidence and reproducibility

The inspected `Wrath_Data/Managed/Assembly-CSharp.dll` SHA256 is `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
I used the project's ILSpy 9.1.0.7988 decompiler and a temporary method-specific `CSharpDecompiler` runner referencing that installed decompiler DLL.
The temporary evidence directory is `C:/Users/Z/AppData/Local/Temp/native-actor-transfer-joh350ek`.
Its `decompile/Decompile.csproj` accepts the game DLL, full type name and method name.
The earlier whole-assembly IL export in that directory was interrupted and must not be represented as an exhaustive call audit.
Reflection searches of declared method names, scene-state parameters and candidate call sites were discovery tools; the conclusions below come from reading the resolved method bodies.

The sibling `native-retained-actor-transfer-probe.py` reproduces the unsafe ownership behavior with installed native `SceneEntitiesState` and `UnitSpawnerBase.MyData` objects in a separate managed process.
It bypasses construction of the spawner-data object because Unity is unavailable, then invokes the actual native `AddEntityData` method twice.
It proves that the same object remains in both source and target lists while `HoldingState` points only to the target.
This deliberately invalid synthetic state demonstrates why the primitive is insufficient.
It is not a live-unit movement, serialization, registry or Unity test.
The initial isolated witness built with zero warnings/errors and passed.

## Actual operations

| Native method | Observed behavior | Consequence |
| --- | --- | --- |
| `SceneEntitiesState.AddEntityData` | Rejects an existing target ID, otherwise appends, assigns `HoldingState`, emits added event. | Does not detach the source list. |
| `SceneEntitiesState.RemoveEntityData` | Clears `HoldingState`, calls `Dispose`, removes and emits removed event. | Cannot be the detach half of a living actor move. |
| `UnitEntityData.set_HoldingState` | Assigns base state and may ensure a personal inventory outside player cross-scene state. | Does not synchronize either entity list. |
| `AreaPersistentState.AddEntityData` | Delegates to `MainState.AddEntityData`. | Adds no transfer semantics and may select the wrong scene. |
| `TranslocateUnit.RunAction` | Marks unit non-extra, stops view motion, interrupts movement commands, assigns position and optionally orientation. | Retains actor identity and ownership; requires an existing view. |
| `UnitEntityData.set_Position` | Stores `m_Position`, wakes the unit and calls `OnPositionChanged`. | Position is unit data, but this setter does not move storage. |
| `EntityDataBase.set_IsInGame` | Updates field, updates view activity when present, emits change event and invokes callback. | Visibility does not resolve etude conflicts or provenance. |
| `HideUnit.RunAction` | Hides with optional fade or unhides subject to pet rules; optional save-hide behavior changes companion handling. | Native history and future hide actions remain. |
| `UnitEntityView.MoveToAppropriateRoot` | Chooses dynamic or cross-scene transform root from `HoldingState`. | View hierarchy alone is not saved ownership. |
| `UnitStateTransfer.RunAction` | Copies selected buffs and proportional HP between source and target actors. | Misleading name; not identity transfer. |
| `EntityCreationController.ChangeUnitBlueprint` | Retires/hides old unit, assigns a new unique ID and creates a new unit from its view. | Replaces identity. |
| `Game.AddUnitToPersistentState` | Creates a new unit, adds it to player cross-scene storage and raises spawn events. | Not a retained actor move. |
| `Player.AddCompanion` | Changes companion/party and mythic progression state. | Inappropriate NPC storage workaround. |

## Scene loading, disposal and save order

`Kingmaker.EntitySystem.Persistence.Scenes.SceneLoader.LoadAreaCoroutine` unstashes area state, runs post-load, matches active dynamic scenes and turns their states on.
It then installs the current navigation mesh and loads or repairs cross-scene views.
It later destroys unattached extra views, turns the area on and processes native spawner activation.
An actor reference obtained before these operations finish is insufficient proof of usable contact.

`SceneLoader.LoadSceneEntities` matches native views by unique ID and attaches retained entity data to compatible views.
Dynamically created views enter the appropriate dynamic or cross-scene root.
Entities that need a view but still have none are removed through `RemoveEntityData`.
An improvised list reassignment can therefore appear to work in memory and lose the actor during a later scene load.

`SceneLoader.UnloadAreaCoroutine` waits for `SaveManager.CommitInProgress` before beginning its unloading work.
For a normal unload it interrupts cross-scene commands, sets cross-scene units in-game according to party membership, and marks hidden units without `UnitPartCompanion` for destruction.
Player cross-scene state is not a general guest-NPC parking area.
The loader turns off the area, calls `PreSave`, and stashes its state with `dispose: true`, unless the area is excluded from saves.
A managed object reference cannot be carried through that disposal and treated as the still-live saved actor on the other side.
Reacquire the saved identity through the observer after each load.

The existing creation queue does not solve transfer.
`EntityCreationController.AddEntity` queues a create entry and `Tick` later adds it to its destination and raises spawn events.
Queue acceptance is not completed ownership, and these spawn semantics do not detach a retained source actor.
The earlier `terendelev-materialization-api.md` correctly requires later registry/state confirmation for a newly created actor; that service is not evidence for moving an existing one.

## Exact Tirabade implications

The five source identities and exact scene names remain those audited in `tirabade-trickster-recovery-design.md` and the independently reviewed `TirabadeRecoveryObserver`.
Capital representations belong to `DrezenCapital_Default_Mechanics` in area `2570015799edf594daf2f076f2f975d8`.
The three alternative retained Iz representations belong to `Iz_Default_Mechanics` in area `2ccc6731787b6ec41ab5adc13f1b9ce9`.
Do not substitute capital `MainState`, whose throne-room ownership differs from the outdoor mechanics state.

Native capital positioning already combines hide/unhide actions with locator-based translocation.
Irabeth's throne-room positioning etude `48967c3ec4330294ab1f5d24d9b45052` uses locator `adee9a01-42a3-4850-b2d1-4a3dfcee9369`.
Anevia's coronation positioning etude `7076d6e6f8e984749829211b04119a80` uses locator `0c6a9c0e-59eb-4aae-84a7-a3ad8ac0e476` and priority 100.
These are native positioning precedents, not approved recovery destinations.

Irabeth's `NotInDrezen` etude `99a03d4f02004b76a5e97c85ba0ec37e` and Anevia's `NotInDrezen` etude `6125c10886d6465091f4e092618ca55a` use priority 99 hide behavior.
Irabeth's queen-associated placement has priority 400.
Merely setting `IsInGame = true` or replaying a low-priority throne-room action does not establish durable control over those states.
The authored invitation needs a narrowly scoped positioning-etude design in the same actual conflicting group, with activation and release reviewed against these native entries.
That conflict-resolution implementation is not supplied or approved here.
Historical death, departure and Commander-killed-wife flags must remain readable and unchanged.
An alive hidden capital representation cannot establish that the Iz woman survived or was resurrected.

## Minimal next implementation contract

For a same-state living invitation, request only after authored agreement, a unique retained living source observation and the exact source scene/area part are loaded.
Reject unresolved, dead, duplicate or conflicting alternatives without changing them.
Resolve a verified native locator or a separately audited meeting anchor within that same source scene.
Use current navigation and occupancy checks before moving; the existing Terendelev free-place and footprint checks provide reusable mechanics, not a validated Tirabade destination.
Apply the scoped native positioning conflict solution, then use the existing unit's movement/position API without replacing its ID or adding/removing state entries.
After native ticks and positioning actions settle, poll the same registry object, source-list membership, `HoldingState`, alive/nonhostile state, active view and reachable destination.
Only then expose contact.
Persist a mod-owned request/meeting record and reobserve on reload; do not persist an object pointer or grant success when the request was merely submitted.
Native contact's historical unavailable gates need a separately reviewed, specific recovery acknowledgement, not a blanket flag override.

Required follow-up tests are a real loaded invitation, a competing native hide/position activation, interruption before confirmation, leaving/reentering the area and save/reload with exactly one saved actor identity.
Verify release returns control to the intended native positioning behavior without clearing historical flags.
For cross-area transport, the missing prerequisite is a demonstrated non-disposing detach plus target adoption with consistent serialization, registry and view lifecycle.
No inspected public operation provided that contract.
Until such an operation is demonstrated, stage contact in the original scene or leave cross-area delivery explicitly unavailable.

## Follow-up: callers that mutate the exposed entity list

The parent correctly identified `AllEntityData`'s mutable list as a second discovery path.
I reran the installed-assembly scan with actual IL instruction boundaries and resolved method tokens, instead of the earlier byte-pattern candidate search.
It examined declared method bodies, including compiler-generated iterator methods, for calls to `get_AllEntityData` and removal/clear methods in the same body.
This search does not prove the absence of mutation through a helper, a previously stored list alias, reflection or another assembly.

One concrete direct-list removal exists in `Player.RemoveEverybody`.
It first calls `RemoveCompanionInternal` for party members, collects all `UnitEntityData` from `CrossSceneState.AllEntityData`, removes those objects directly from that list and updates the character lists.
It does not adopt the actors into an area state, update their `HoldingState`, reconcile target spawners or establish a surviving view in a destination.
It is a bulk party reset precedent, not a complete NPC transfer operation.

I also decompiled `Player.RemoveCompanion`, `RemoveCompanionInternal` and `UnitPartCompanion.SetState`.
They change party membership, companion state, pet state, visibility and associated notifications.
They do not provide source-to-target scene ownership transfer.
The other matched bodies remove party references, clear derived character caches, dispose scene entities, change the saved-area collection or clean up unrelated inventory/import state.
The scene-loader methods were already read in full for the earlier findings.

The additional native precedent therefore confirms that bypassing disposal through direct list removal is possible in special-purpose engine code, but leaves the required complete transfer contract unproved.
Do not promote that partial operation to a production recovery primitive without target adoption, native-spawner behavior, save/reload and view-lifecycle evidence.
