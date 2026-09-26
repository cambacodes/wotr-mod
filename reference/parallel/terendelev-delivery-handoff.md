# Terendelev persistent delivery handoff

Released for independent review on 2026-09-26.
Only the four assigned source/test files and this handoff were written.
Shared Main, Story, registrations and installed files were not changed.
The service compiles against the actual installed game assemblies; it has not spawned an actor in Unity and is not author-approved for production.

## Exact release

| File | SHA256 |
| --- | --- |
| `src/TerendelevDelivery.cs` | `E13C14EB47C9EFEB7D05C9656A9E3E34F4CEDC750B70975CE4331658B77588C2` |
| `src/TerendelevDeliveryAttempt.cs` | `54A9262C731061B4624C82C42A942FF9C71A1232DA8A42F7D716FCC2E11D8A74` |
| `tests/TerendelevDeliveryTests.cs` | `6043B398DA3D0916CC06C5D287431558C1B082C8B7E63EB5397EAF221B09F73B` |
| `managed-tests/TerendelevDeliveryBlueprintTests.cs` | `31A8EF220B55024C79DCEF40E7CBBC50863232285327F110549ECBFD1884E9F1` |

## Small integration contract

`TerendelevDelivery.CreateBlueprint(nativeHuman)` creates the private human unit blueprint with deterministic GUID `93578a5a84c7ec724d14de6d5aba6692`.
The caller must register it once through the existing blueprint-cache build lifecycle before saved entities deserialize.
Do not reconstruct or replace that cached object on every poll.
The source is native human `9e8401e7703907e4d94189d5992dd13e`.
The clone uses the inspected native Become method, verifies copied body/faction data, requires an independent visual object and component objects, strips typed Experience, retains exactly one AddClassLevels, substitutes the verified passive brain and neutral faction, and clears bandit barks.
Unexpected component types or alternative brains fail closed instead of silently importing newly patched behaviors.
Native class setup, appearance, equipment and facts otherwise remain intact.

Call `Request(provenance, authorized, blueprint, out actor, out message)` only after the route's actual chosen restoration action is authorized.
Provenance is a stable branch/choice identifier retained across saves; requesting a different provenance never replaces the checkpoint.
The boolean must represent current caller-verified mythic, native and parent-mod history, including Aeon survival, Ravener/remains, conscious-undead, Lich bondage and parent finale conflicts.
This small delivery service does not reinterpret those story branches itself.
It additionally refuses a loaded living native human, silent-caster human, dragon, aware-undead or Lich identity rather than displacing it.
No native actor is deleted, teleported, resurrected or adopted.

Call `Poll(currentAuthorization, cachedBlueprint, out actor, out message)` on an ordinary game update or an explicit status action to finish pending delivery.
Neither request nor poll invokes EntityCreationController.Tick.
Only result Confirmed supplies the exact usable actor for an arrival dialogue.
NotRequested, Pending and Blocked must not advance the story into a successful return speech.
Messages are concise player-facing status text.
Exceptions are retained in the internal LastError property for caller logging/debugging and are not appended to player messages.
LastError is cleared at the beginning of each request or poll.
Later scenes must still use physical-contact checks against the private blueprint; the historical Confirmed checkpoint alone is insufficient.
A spawned actor does not automatically acquire world-click dialogue, so the first integration uses the explicit mod conversation action with the returned actor.

## Transaction and save behavior

The existing per-save Player.SettingsList stores JSON under `RanRomance.Tirabade.TerendelevDelivery`.
The checkpoint records version, generated stable GUID, provenance, Submitted and Confirmed.
The generated ID and Submitted state are saved before entering SpawnUnit.
If persistence throws, Submit has already changed its local in-memory object to Submitted, but it does not dispatch SpawnUnit.
The next service call reads a fresh object from SettingsList; when the write failed before replacing the saved value, that is the prior unsubmitted checkpoint and the same ID can safely retry.
If an unusual persistence failure occurred after storing Submitted, the conservative submitted checkpoint instead blocks replay.
The focused test explicitly exercises failure-before-write, the local submitted state and successful retry after re-reading the prior serialized pending checkpoint.
A successful SpawnUnit return is not credited as arrival.
A later poll requires the exact saved ID and private blueprint in the entity registry, exactly one matching area entity, exact outdoor HoldingState, exactly one matching destination list entry, no pending creation entry, and a living conscious nonsuppressed nonhostile unit with a view.
Wrong-ID private actors, registry/list disagreement and queued identity/state conflicts block delivery without removing anything.
After save/load the same checkpoint adopts only that exact saved identity after normal load processing completes.
Already confirmed contact is revalidated, but its unchanged checkpoint is not rewritten every tick.
A subsequently dead or absent confirmed actor is never recreated automatically.

An unavailable destination before submission can be retried normally.
A submitted creation that throws or disappears without a provably usable actor retains its checkpoint and blocks another spawn.
This deliberately also treats a null native SpawnUnit return as ambiguous, because the native method catches failures after partial creation.
There is no automatic checkpoint reset or administrative repair command in this service.
A rare failed submission with no surviving actor therefore needs a separately reviewed repair decision, rather than an automatic duplicate-risk retry.
The player-facing message reports the unconfirmed result instead of silently awarding success.

## Destination and clearance

Delivery requires Drezen area `2570015799edf594daf2f076f2f975d8`, outdoor part `8a076e720870a44438d13b9b939933fd` and the actually loaded existing `DrezenCapital_Outdoor_Mechanics` state.
The service does not call GetStateForScene with an arbitrary name or default to throne-room MainState.
It waits through loading/unloading/save-load and rejects a state marked SkipSerialize or not loaded for saving.
It uses the audited StorytellerPosition world anchor `(7.49, 62, -28.07)` as a nearby reference, without moving the Storyteller.
The active nearest anchor node must be walkable and close to its verified floor.
Native FreePlaceSelector generates a candidate using 0.5 corpulence.
The candidate must stay within four metres, lie on the same connected walkable area, match navmesh height, pass eight one-metre footprint samples, and clear current units using the larger inspected view footprint.
A standing-volume Physics.CheckBox then rejects collider obstruction while leaving five centimetres above the ground surface.
These are conservative live checks, not a claim that a particular save supplies a vacant position.
Crowding or a changed navmesh leaves arrival pending.

## Verification performed

Temporary actual-assembly build and runner: `C:/Users/Z/AppData/Local/Temp/terendelev-delivery-check-jral48_w/Check.csproj`.
It compiled with zero warnings and zero errors, then passed 10 managed blueprint-configuration assertions.
Those assertions use real installed BlueprintUnit, Experience, AddClassLevels and blueprint-reference classes, verify copied XP/bark/brain/faction changes and unchanged native data, and reject native/shared visual/shared component/missing-class inputs.
The fixture tests ConfigureBlueprint on independently constructed managed objects; it does not pretend to have deserialized the full native prefab.
An additional real CreateBlueprint invocation reached native Become and failed at UnityEngine.JsonUtility.ToJson with `SecurityException: ECall methods must be packaged into a system module` outside Unity.
That concrete native-host limitation means full clone serialization must still be verified inside the game.
It was not replaced with a fake successful clone.

Temporary pure coordinator runner: `C:/Users/Z/AppData/Local/Temp/terendelev-delivery-state-check/Check.csproj`.
It passed 23 focused transaction assertions.
These execute the actual production Submit/TryConfirm methods through unauthorized/occupied/unloaded rejection, checkpoint-before-spawn ordering, a thrown native-call substitute after registration, JSON save/load, no duplicate retry, registry-only rejection, wrong identity, unusable actor, changed authorization, successful adoption, later loss of contact, delayed pre-submission retry and checkpoint-write failure.
The test substitute does not create a Unity entity.
Root shared rule integration needs a Compile link to `src/TerendelevDeliveryAttempt.cs` and `TerendelevDeliveryTests.Run(check)`.
Managed registration needs `TerendelevDeliveryBlueprintTests.Run(check)` after the production assembly includes this service.

## Remaining review and runtime checks

Independent review is required for the exact source and contract above.
Root-owned route gating, cache registration, update polling, pending UI and arrival dialogue integration remain separate work.
A real Unity save must verify Become copying, retained class initialization and appearance, neutral behavior, the active outdoor navigation/physics checks, ordinary creation-tick insertion and explicit conversation startup.
Save/reload must verify adoption with the same ID, no duplicate after loading, area departure/return, a killed delivered actor, obstructed anchor and a native identity conflict.
The conservative physics footprint may reject crowded or sloped positions; it must be checked in the real scene before claiming delivery is attainable in that save.
No full resurrection route, courtship length, ToyBox runtime compatibility or ready-character status is certified by this implementation.
