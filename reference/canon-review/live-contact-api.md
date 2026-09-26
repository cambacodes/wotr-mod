# Live native NPC contact API

Verified on 2026-09-25 against installed `Wrath_Data/Managed/Assembly-CSharp.dll`.
Assembly SHA256: `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
Investigation used ilspycmd 9.1.0.7988 for small native classes and dnlib metadata/IL for selected UnitEntityData methods.
Whole UnitEntityData decompilation was not attempted.

## Hostility

The installed public signature is `bool Kingmaker.EntitySystem.Entities.UnitEntityData.IsEnemy(UnitEntityData unit)`.
Native `Kingmaker.Designers.EventConditionActionSystem.Conditions.IsEnemy.CheckCondition()` evaluates its two UnitEvaluators and calls `value.IsEnemy(value2)`.
The UnitEntityData method returns false for a null argument, otherwise calls `Group.IsEnemy(unit)`.
Therefore an absent Commander must be rejected explicitly, before negating the hostility result.
`Game.Instance.Player.MainCharacter` is a `UnitReference`; its `Value` supplies the Commander entity.

`Kingmaker.UnitLogic.Groups.UnitGroup` has public overloads `bool IsEnemy(UnitGroup group)` and `bool IsEnemy(UnitEntityData unit)`.
The group overload checks the private directional function in both directions.
One `npc.IsEnemy(commander)` call therefore checks the installed game's symmetric hostility relation; calling the reverse again is unnecessary.
The relation includes group identity, enemy-for-everyone state and attack-faction membership.
Alignment and the character's ordinary blueprint faction are insufficient substitutes.

The Group getter calls `UpdateGroup()`.
That method may initialize and register missing group state, so this native query is not literally free of internal writes.
It does not set romance flags, quests, life state or faction allegiance.
Disposed entities enter a special group-repair branch, so reject `IsDisposed` before this call.

## Loaded state and identity

`Game.State` is a readonly `Kingmaker.EntitySystem.PersistentState` field.
`PersistentState.Units` is a readonly `EntityPool<UnitEntityData>` initialized with a filter rejecting `unit.Blueprint.IsFake`.
EntityPool subscribes to the static `SceneEntitiesState.OnAdded` and `OnRemoved` events.
It is not, by itself, proof that an entity belongs to the loaded area.
Its enumerator checks `ShouldBeEnumeratedByEntityPoolEnumerator`, whose implementation is only `IsInGame && !Suppressed`.
Its `.All` property exposes the underlying list without that enumeration filter.

Verified additional API members:

| Declaring type | Member | Meaning |
| --- | --- | --- |
| PersistentState | `AreaPersistentState LoadedAreaState { get; set; }` | Current loaded area state |
| AreaPersistentState | `IEnumerable<EntityDataBase> AllEntityData` | All records from `GetAllSceneStates().SelectMany(s => s.AllEntityData)` |
| EntityDataBase | `virtual SceneEntitiesState HoldingState { get; set; }` | Owning scene state, possibly null |
| SceneEntitiesState | `bool IsSceneLoaded` | Calls `SceneManager.GetSceneByName(SceneName).isLoaded` |
| SceneEntitiesState | `bool IsSceneLoadedThreadSafe { get; set; }` | Stored flag, not the same live scene query |
| EntityDataBase | `bool IsDisposed { get; private set; }` | Disposal completed |
| EntityDataBase | `bool Destroyed { get; protected set; }` | Destroy completed |
| EntityDataBase | `bool DestroyMark { get; private set; }` | Scheduled destruction |
| EntityDataBase | `EntityViewBase View { get; private set; }` | Attached Unity view, nullable |
| EntityDataBase | `string UniqueId { get; private set; }` | Entity instance identity |
| UnitEntityData | `BlueprintUnit Blueprint` | Returns `Descriptor.Blueprint` |

For a local noncompanion NPC introduction, require membership in the current `LoadedAreaState.AllEntityData`, a non-null HoldingState, and `HoldingState.IsSceneLoaded` in addition to the active/living/conscious/nonhostile checks.
This is an authored conservative contact rule, not a claim that Owlcat's speaker resolver imposes these exact conditions.
Do not generalize loaded-area membership to recruited companions without checking their cross-scene storage behavior.
A loaded scene can still contain an actor behind a closed door or outside the present encounter, so retain authored scene/quest gates and verify the actual interaction in game.
Native `UnitIsInAreaPart.CheckCondition()` checks `AreaPart?.Bounds?.MechanicBounds.ContainsXZ(value.Position) == true`; this tests coordinates, not entity ownership or loaded-state membership.

Use the actual Blueprint or its AssetGuid, not `BlueprintForInspection`, `ReplaceBlueprintForInspection`, portrait identity or display name.
Multiple entities can share a Blueprint.
Count distinct matching entity instances, then reject ambiguity instead of selecting an arbitrary instance.
SceneEntitiesState rejects duplicate UniqueId values within its own list, but that does not prove one instance of a blueprint exists globally.

## Do not use DialogSpeaker.GetEntity as the predicate

Existing `reference/game-DialogSpeaker.cs` documents the installed implementation.
It searches State.Units plus Player.Party and a creation queue, then chooses the nearest matching Blueprint.
It also calls MakeEssentialCharactersConscious and can restore a non-finally-dead or unconscious matching unit through UnitReturnToConsciousController and UnitLifeController.
Calling it to decide whether an invitation should appear could change native life state.
Its creation-queue search also does not establish an already loaded, interactable actor.

## Verification

Compile the production predicate against the installed assemblies to prove member names and signatures.
Exercise rules with no contact, one available contact and another character's contact to prove that scene availability uses the correct transient contact GUID.
Exercise entity filtering with hidden, suppressed, unconscious, dead, finally dead, hostile, disposed, destroy-marked, duplicate, wrong-blueprint and unloaded-area records.
Check that the filtering does not change quest flags, faction assignments, romance commitments or death state.
Loaded-scene querying crosses a Unity boundary; a headless fixture that supplies a boolean only proves the decision logic around that boolean.
It does not prove Unity's scene manager reports the intended current actor.
Avoid claiming a native uninitialized-object fixture proves real group initialization or real scene loading.
An in-game check must cover the actual NPC encounter, loading away and back, saving/loading, native removal/death, and invitation visibility before and after the quest transition.
ToyBox compatibility still requires its own checks; a nonhostile living NPC is not proof of Love Is Free or Jealousy Begone behavior.
