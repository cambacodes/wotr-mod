# Cross-scene contact fix review

Independent review on 2026-09-26 accepts the bounded storage and physical-presence correction.
No blocking defect was found in the reviewed source.
This verdict does not assert a completed live Aivu throne-room test or route readiness.

## Reviewed snapshot

| File | SHA256 |
| --- | --- |
| `src/NativeContact.cs` | `018BE371E40D1950564D6C74D1EB79CD195E781DCF2C28FA0A8CC826D10170B3` |
| `managed-tests/NativeContactStorageTests.cs` | `008C26954A484E71F3DA4E7610184F47586EFD640DF5349B96DEAA86C7B6565D` |

The review checked both files directly against the native evidence in [cross-scene-contact-audit.md](cross-scene-contact-audit.md).
The installed `AreaPersistentState.GetAllSceneStates` was independently decompiled again to confirm that it enumerates the main state and additional states.
Its `AllEntityData` is exactly the flattening of those containers.

## Source judgment

`HasCurrentStorage` requires the actor's non-null holding state to contain the actor.
It then requires that exact state to be either the current player's cross-scene container or one of the current area's native scene-state containers.
This is stronger than accepting a stale actor entry anywhere in the flattened area list.
A container sharing the `<cross-scene>` name cannot substitute for the current player's actual container.

`IsAvailable` bypasses the holding-state Unity scene lookup only for the exact current cross-scene container.
Area-held actors still require their real holding scene to be loaded.
Both branches require a non-null Unity view, reciprocal `view.Data` identity, a loaded actual view scene and an active GameObject hierarchy.
These checks keep persistent storage from becoming an exception for detached or inactive actors.

The prior exact single-blueprint match remains intact.
Destroyed, destroy-marked, disposed, suppressed, out-of-game, unconscious, dead, finally dead and hostile actors remain unavailable.
The Commander and loaded-area guards remain, with save-loading and unloading rejection added.
No `InParty` requirement was introduced, so native capital placement can expose an actual visible remote companion or pet.
No actor is spawned, woken, revived, teleported or mutated by the guard.

## Test judgment

The fixture uses an actual uninitialized native `UnitEntityData` and native `SceneEntitiesState` containers.
It deliberately seeds `EntityDataBase`'s saved holding-state backing field because the normal unit setter invokes Unity-dependent game state.
Its helper migration manipulates that backing field and the native lists directly.
This is a managed storage test, not native setter execution or a running game simulation.

The first assertions reproduce the old mandatory area-membership rejection while proving that the same unit belongs to current cross-scene storage.
The corrected helper is then exercised for cross-scene acceptance, current area acceptance, another area's rejection, rejection of a stale area-list entry and rejection of an orphaned holding reference.
The production helper is invoked through reflection from the built mod assembly rather than copied into the test.
The shared managed runner invokes this fixture through `NativeContactStorageTests.Run(Check)`.

The test does not call the full `IsAvailable` Unity branch and makes no claim to verify live view loading, GameObject activation, reciprocal attachment or actual dialog presentation.
Those are explicit runtime verification limits.
They do not weaken the demonstrated cause of the storage rejection or justify keeping it.

Root owns the production build and shared managed run, so this reviewer did not run a conflicting duplicate build.
Root reported the successful shared managed run after this source review: 36,214 assertions, 283 scenes, 10,680 blueprints and 10 native answer lists.
The storage fixture passed all seven assertions, including the negative witness for the legacy area-membership condition.
Production and managed builds completed with zero warnings.
The built DLL hash was `CB2FCD2383C770D7046C36581C84E92673E032571E7884B0E376E7615B7EA59C`, with story hash `B25FEBE22935CAB61077AF08EE9452EB530CB116789379BD82AF4977A2BF5426`.
An earlier managed attempt failed because the bare Python launcher received empty standard input.
Root added the optional `RRT_PYTHON` explicit interpreter setting and reran successfully using the installed pythoncore executable.
This execution evidence is attributed to root's run; the reviewer independently inspected the source and fixture but did not duplicate that run.
The view checks remain source-reviewed and were not exercised in Unity by this managed test.
