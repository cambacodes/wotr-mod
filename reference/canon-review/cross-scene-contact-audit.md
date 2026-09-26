# Cross-scene contact audit

Reviewed 2026-09-26 against the installed `Assembly-CSharp.dll`, SHA256 `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
This is independent native-code research for the shared contact guard.
It does not approve a live Unity interaction or any complete character route.

## Finding

The previous guard has two independent false negatives for legitimate cross-scene actors.
`AreaPersistentState.AllEntityData` enumerates the main area state and its additional scene states, excluding `Player.CrossSceneState`.
`SceneEntitiesState.IsSceneLoaded` queries `SceneManager.GetSceneByName(SceneName).isLoaded`, whereas the player's cross-scene container is named `<cross-scene>`.
That storage name is not the Unity scene containing the actor's actual view.
Adding cross-scene membership while retaining the unconditional holding-scene check would leave the second rejection intact.

The installed native code positively supports a separate current-player cross-scene storage branch with common attached, active, loaded-view checks.
Requiring party membership would introduce another false negative for companions or pets deliberately placed by capital spawners.

## Native evidence

| Native location | Observed behavior | Implication |
| --- | --- | --- |
| `Player.CrossSceneState`, `AllCrossSceneUnits` | Creates `new SceneEntitiesState("<cross-scene>")`; enumerates units from that container. | Cross-scene storage is a distinct native container. |
| `Game.AddUnitToPersistentState` | Creates the unit and adds it to `State.PlayerState.CrossSceneState`. | Real persistent actors enter this container directly. |
| `SceneEntitiesState.AddEntityData` | Adds the object, assigns `data.HoldingState = this`, and invokes `OnAdded`. | Check exact current container identity and actual membership together. |
| `AddPet.TryUpdatePet` and its spawn call | Spawns into `base.Owner.HoldingState`, sets the owner as master, then sets pet `IsInGame = base.Owner.IsInGame`. | A persistent Commander's pet inherits cross-scene storage. |
| `CompanionSpawner.GetMyCompanion` | Finds the owner in `Player.AllCharacters`; with `m_UsePet`, selects the owner's pet matching `m_PetType`. | The Aivu spawner reuses the real pet. |
| `CompanionSpawner.PlaceCompanion` | Sets position, orientation and view transform, then sets `IsInGame = true` when `ShouldShowUnit` succeeds. | Physical capital placement does not migrate the pet into area storage. |
| `CompanionSpawner.ShouldShowUnit` | Supports remote, capital and ex-companion states according to spawner settings; checks companion/pet hidden flags and the authored show condition. | A capital actor can be present without being an active party member. |
| `Player.UpdateCharacterLists`, `AddCharacterToLists` | Reads cross-scene entities separately; capital mode changes party classification and accounts for pets controlled by spawners. | Party/remote lists are not reliable substitutes for physical contact. |
| `EntityPool<T>.HandleAdded` | Subscribes to additions from scene states and collects matching entities. | `State.Units` is not restricted to current area storage. |
| `EntityPoolEnumerator<T>.MoveNext` | Tests `ShouldBeEnumeratedByEntityPoolEnumerator`. | The enumerator supplies only its documented entity-state filter. |
| `EntityDataBase.ShouldBeEnumeratedByEntityPoolEnumerator` | Returns `m_IsInGame && !m_Suppressed`. | Enumeration does not establish an attached, loaded view. |
| `EntityDataBase.AttachView`, `DetachView` | Establishes reciprocal view attachment; normal detachment clears `View`. | A non-null attached view is a separate necessary condition. |
| `EntityViewBase.AttachToData`, `DetachFromData` | Sets or clears view `Data`. | Checking `view.Data == actor` also rejects one-sided detach states. |
| `EntityViewBase.UpdateViewActive` | Uses `Data.IsViewActive` to set the GameObject's active state. | `activeInHierarchy` checks actual active placement, including inactive ancestors. |
| `SceneLoader.LoadSceneEntities` | Attaches cross-scene data views and adds newly created ones to `CrossSceneRoot`. | The cross-scene container has real views under a scene root. |
| `SceneLoader.LoadAreaCoroutine` | Loads cross-scene views when the root is empty, otherwise repairs missing views. | Storage lifetime and view lifetime are separate. |
| `SceneLoader.UnloadAreaCoroutine` | Sets each cross-scene unit's `IsInGame` from `Player.Party.Contains(unit.Master ?? unit)`. | Absent remote actors are disabled during native area transitions. |
| `SceneLoader.UnloadEntitiesCoroutine` | Clears `CrossSceneRoot` when `unloadCrossScene` is true. | Unloaded cross-scene storage alone does not imply an available actor. |

The exact Aivu throne-room asset, owner lookup, pet type, show condition and dialog interaction were independently extracted in [the capital contact audit](aivu-capital-contact-audit.md).
The native spawner uses the existing Azata havoc dragon and does not create a duplicate proxy pet.
Its actual actor blueprint remains `32a037e97c3d5c54b85da8f639616c57`.

## Smallest supported guard

Keep the existing loaded-area, Commander, combat, actor uniqueness, destroyed/disposed, consciousness, living, nonhostile, `IsInGame` and suppression checks.
Require a real view with reciprocal `view.Data == actor` attachment, an active GameObject hierarchy, and a loaded actual Unity scene.
Unity object comparison must respect destroyed-object semantics.
Accept storage through either of these branches:

1. The actor's holding state is the current player's exact `CrossSceneState`, and that container actually contains the actor.
2. The holding state is a loaded real scene and the current `LoadedAreaState.AllEntityData` contains the actor.

The cross-scene branch must bypass `HoldingState.IsSceneLoaded` because that property interprets a storage label as a Unity scene name.
It must not bypass the common actual-view scene check.
Do not broaden acceptance to any historical cross-scene container, any saved actor sharing a blueprint, or any member of `Player.AllCharacters` without the view and state checks.
Do not require `CompanionState.InParty` or reject `Remote` categorically.
The native capital placement logic deliberately allows visible actors under those conditions.

This establishes physical availability in the loaded game context, not conversation distance or the correct room by itself.
Existing scene/contact and route-specific area/quest conditions still determine where an authored encounter is valid.
The Aivu throne-room condition comes from the extracted native spawner and must remain distinct from a claim that every outdoor location has the same interaction.

## Verification and limits

The owned read-only probe [probe-cross-scene-contact.py](../../tools/probe-cross-scene-contact.py) successfully decompiled all nine requested types and printed the relevant evidence from the installed assembly.
It uses the existing ILSpy installation and writes no game assets or source files.
Run from the project root with the existing Python interpreter.
The `Player` and `Game` findings were checked against the existing `reference/game-Player.cs` and `reference/game-Game.cs` decompilations.
Full `UnitEntityData` C# decompilation was unnecessary and had previously failed inside ILSpy; no conclusion here depends on that failed output.

A managed test should reproduce the old necessary-condition failure by placing the same native entity in area storage, migrating it into the actual cross-scene container, and checking the two distinct memberships.
The corrected helper should accept exact current cross-scene storage, reject stale containers and missing membership, and retain area-actor behavior.
That test proves storage semantics without pretending to execute Unity scene and GameObject APIs.
The loaded-view, inactive hierarchy, detached view and live dialog behavior still require either an appropriate Unity runtime test or direct in-game verification.
The proposed fix has enough native evidence to implement and test now; those remaining runtime checks are not a reason to retain the demonstrated false rejection.

No shared source, authored routes or game state was changed for this audit.
