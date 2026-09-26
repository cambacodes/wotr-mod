# Terendelev living actor and destination audit

A private runtime copy of the native human blueprint can supply the living visual body without importing the prologue scene's spawner identity or actions.
Do not use the unmodified blueprint as a finished social NPC.
It carries a combat brain, boss experience, equipment and bandit voice barks, and spawning it does not create a clickable dialogue interaction.
The inspected Storyteller locator supplies a verified outdoor arrival anchor with baked navigation beneath it, but the exact free standing position must be selected and checked in the running scene.

## Sources and exact records

I inspected the installed blueprint archive, native prefab and capital/prologue scene bundles with UnityPy, and decompiled the installed Assembly-CSharp and AstarPathfindingProject classes.
The companion `terendelev-actor-blueprint-records.json` stores exact relevant blueprint records, Unity object/component records, parent transforms, navigation settings and containing triangles, and bundle SHA256 values.
The Assembly-CSharp SHA256 remains `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` as recorded in the previous API audit.
No installed assets were changed, and no actor was spawned.

## Native human behavior

The blueprint is `Units/NPC/Unique/Act_0_Prologue/Prologue_Kenabres/TerendelevHuman.jbp`, GUID `9e8401e7703907e4d94189d5992dd13e`.
Its PrototypeLink is empty.
The complete component list has exactly two entries, Experience and AddClassLevels.
It has no blueprint dialog component, spawn action, death action or cutscene component in that list.

| Field | Inspected value | Implementation implication |
| --- | --- | --- |
| Gender, size, alignment | Female, Medium, LawfulGood | Preserve for the native human presentation. |
| Prefab | `ec900f647b97f4643a9181bf609d3a89` | Reuse the native visual asset, with a new persistent entity identity. |
| Portrait | `d9d0098309a546c6bd8fe825874e50ae` | Preserve until an approved route portrait is installed. |
| Faction | Neutrals `d8de50cc80eb4dc409a983991e0b77ad` | No configured attack factions; still verify runtime hostility. |
| Brain | Dumb Monster Brain `5abc8884c6f15204c8604cb01a2efbab` | Contains AttackAiAction `866ffa6c34000cd4a86fb1671f86c7d8`; replace on the private copy for a noncombat social actor. |
| Experience | Boss, CR14, modifier1 | Remove from the private copy to avoid importing an encounter reward. |
| Class levels | 15 levels, class `bfa11238e7ae3544bbeb4d0b92e897ec`, Charisma selections and spells | Preserve for now rather than accidentally producing a zero-HP uninitialized actor by stripping all components. |
| Additional facts | Only `c4cbe77f822100f4d85e907fa9a50e9a` | This is LocalMapMarker_VIT with AddLocalMapMarker; no revival or quest effect. |
| Barks | BanditFemale01 `c19c6b9c2772526409b7cdb5f3364efe` | Clear on a separately copied visual-parameters object unless a reviewed Terendelev voice source is supplied. |
| Body | Weapon, shield, armor, belt, head item, ring and two quick-slot consumables | Treat as inherited equipment, not romance rewards; do not permit repeated new-actor farming. |
| Alternative brains, starting inventory, templates | Empty | No extra branch or inventory provider in these fields. |

The silent-caster variant `045e2ea911644fa0abaa2f6c76b83feb` derives from the same human blueprint and changes faction to CutsceneNeutrals, SilentCaster to true, and adds Greater Restoration `fafd77c6bfa85c04ba31fdc1c962c914`.
Do not prefer it merely because it is the prologue's visible conversation body.
The ordinary human is the simpler base for this continuation.

Both inspected Neutrals and CutsceneNeutrals have empty attack-faction lists, but Peaceful, Neutral and NeverJoinCombat are false.
The names are not invulnerability or permanent nonhostility guarantees.
Passive Monster Brain `5718d805516c5ff48bf3e928b6c0e6fd` is a verified existing brain with an empty action list.
It is a concrete replacement for automatic attack behavior without inventing a brain framework.
It does not itself prevent incoming combat or make an otherwise hostile entity eligible for conversation.

## Prefab versus scene scripts

In `ec900f647b97f4643a9181bf609d3a89.unit`, root GameObject `8338277150881718741` is `BCT_TerendelevHuman`.
Its UnitEntityView component is `14282617362353763`.
The root also has movement, particle attachment, highlighting, character rendering and dismemberment components.
It has no root SpawnerInteractionDialog or prologue action component.
The saved view identity `0eee2292-ea74-4f27-a7f1-06a6ed92dd55` is a prefab value, not the identity the new route should retain.
The verified SpawnUnit overload replaces it with the supplied saved ID before creating entity data.

The prefab records corpulence0.5, soft collider radius1.0 and height1.8.
Those are useful actual dimensions for placement validation.
The skeletal/animation children should remain intact.
Do not delete renderer, animation or movement components because their names are unfamiliar.

The original prologue scene has a misleadingly named `TerendelevDragon` GameObject265 whose spawner2734 actually points to the ordinary human blueprint.
Its entity ID is `339e6401-1cd3-4839-b30e-7cdc565119b7`, and SpawnOnSceneInit is false.
The separate `Terendelev` GameObject683 spawner2845 points to the silent-caster human, identity `f8e7ab8f-0bd4-477d-b194-3079ae87c8ef`, with SpawnOnSceneInit true.
Its additional component2846 is a bark interaction.
These scene entities and locators belong to the scripted prologue and must not be adopted as a new restored person's save identity.
Creating the reviewed blueprint at a new ID does not copy those scene objects.
This inspection does not claim that every external native action referring to Terendelev has been rewritten or disabled.

## Concrete clone recipe

Register one new deterministic BlueprintUnit GUID for this route and construct it before saved entities are deserialized, using the project's normal blueprint cache registration.
The actual `SimpleBlueprint.Become(SimpleBlueprint other)` method performs `JsonUtility.FromJsonOverwrite(JsonUtility.ToJson(other), this)`.
It provides an inspected copy mechanism for a newly allocated BlueprintUnit; assign the new AssetGuid and name after copying and before registration.
Do not call Become on the native blueprint or mutate cached native nested objects.
Verify the resulting copy and native source remain independent when editing their component arrays, visual fields, body, faction overrides and references.

On the private copy, remove the Experience component, preserve AddClassLevels, replace the brain reference with the verified passive brain, and clear BanditFemale01 barks on independent visual data.
Preserve the native name, portrait, prefab, adult human presentation, attributes, class setup and VIT marker.
Preserving equipment is the least invasive initial body implementation; any removal of equipment for a noncombat presentation should happen on independently copied Body data and be checked against the baked appearance.
Do not alter native item blueprints or give this equipment to the Commander as part of delivery.
Use the existing stable-entity transaction to prevent repeated creation after death or reload.

The private brain field is `m_Brain`, while the faction has a public BlueprintUnit.Faction setter.
Use the same reviewed field-access approach as other project blueprint construction rather than assuming a nonexistent writable DefaultBrain property.
After spawn, require the expected private blueprint, correct save ID, scene membership, living state and nonhostile contact, as specified in the previous API report.

A spawned unit has no conversation simply because its name is Terendelev.
The inspected `SpawnerInteractionDialog` inherits SpawnerInteraction, which has RequireComponent UnitSpawnerBase and supplies interaction through SpawnerInteractionPart.
Adding that MonoBehaviour directly to the spawned UnitEntityView is not an established clickable-dialogue solution.
For the first delivery service, use the existing mod's explicit conversation action after verifying the physical unit and starting the new dialog with that unit.
Ordinary world-click interaction requires a separately implemented and reload-tested adapter.
Do not present that interaction as complete merely because a portrait or actor exists.

## Verified outdoor anchor and navigation

Use Drezen area `2570015799edf594daf2f076f2f975d8`, actual outdoor part `8a076e720870a44438d13b9b939933fd` and its loaded `DrezenCapital_Outdoor_Mechanics` state.
The area MainState remains the throne-room scene and is unsuitable as an implicit outdoor destination.

The exact candidate anchor is the StorytellerPosition locator in `drezencapital_default_mechanics.scenes`.
GameObject468 has Transform1207 and entity component2718 with ID `236d0480-c95c-431d-87d3-8e966fc9ffbd`.
Its position is `(7.489999771118164, 62.0, -28.06999969482422)`.
Its quaternion is `(0, -0.08658724278211594, 0, 0.9962442517280579)`.
Its Locators parent is identity position, rotation and scale, so these are world coordinates rather than an unverified local offset.
The companion records contain the full fields and parent chain.

This is a reference point near an existing NPC location, not a vacant reserved plot.
Do not spawn on top of the Storyteller or move him aside.
The route can arrange a meeting near him and choose an actually clear adjacent position at runtime.

I decoded the installed `drezencapital.nav` TextAsset6388077926062486588, `DrezenCapital_ThroneRoom_DrezenCapital_Outdoor_GraphCache`.
Its archive identifies RecastGraph and GridGraph with serializer version4.3.10.
Using the actual Astar `NavmeshBase.DeserializeExtraInfo`, `TriangleMeshNode.DeserializeNode` and `GraphNode.DeserializeNode` layouts, I parsed every byte of graph0_extra.binary and tested the anchor in XZ against its triangles.
The anchor lies inside static-walkable tile `(16,10)`, node2, with vertices `(10,62.007,-25)`, `(10,62.011,-28)` and `(6.2,62.004,-29.2)`.
Interpolated ground height at the rounded anchor is62.005412807, only0.005413 above the locator.
The graph was baked for character radius0.5, collider and terrain rasterization, walkable height3 and climb0.5.
This is direct baked navigation evidence at the anchor.

The bundle also contains another TextAsset named `DrezenCapital_Outdoor_GraphCache`, which did not contain a triangle under these world coordinates in this audit.
Therefore validate the active loaded graph rather than selecting a cache solely because its name contains Outdoor.
The actual game's NavMeshManager chooses graphs by current part.
Baked StaticWalkable also differs from runtime Walkable, which checks DynamicBlocked.

For the small service, resolve the actual locator or its verified position only while the correct outdoor part and state are fully loaded.
Require a non-null walkable nearest node from `ObstacleAnalyzer.GetNearestNode(anchor)` with close XZ and height agreement.
Call the inspected `FreePlaceSelector.PlaceSpawnPlaces(1, 0.5f, anchor)`, then `GetRelaxedPosition(0, true)` as a candidate generator.
This method considers nearby living units and projects onto navigation/ground, but its loop stops after30 iterations and has no success result.
It is not sufficient proof of clearance.
Recheck the result's walkable node, compatible connected area, modest distance from the anchor, ground height, current unit clearance and static obstruction before spawning.
Use the actual0.5 corpulence and view collider dimensions rather than an arbitrary tiny radius.
If no clear candidate exists, keep delivery pending and report that the meeting place is unavailable.
Do not teleport the Commander, displace residents or silently choose a different floor.

## Identity conflicts and remaining verification

The native aware-undead capital spawner is GameObject184, entity `9f16b2f6-1ea8-4fa0-b527-ecf4193c71d9`, blueprint `59e7482d41d058a4bace7434c67a08be`.
Its initial position is `(93.24,65.43,6.57)`; that initial point did not lie on the audited outdoor cache and must not be used as a guessed living destination.
The native Lich capital spawner is GameObject210, entity `3029760c-a252-4c8d-a5e8-60feb18a002c`, blueprint `376195cab0179734880947969d2b4e9c`, at `(97.4,62.62,3.7)`.
Its relocation locator `d7aa4429-41bd-4d58-bb17-074863d847f7` is at `(33.58,62.33,-4.31)` and does have baked outdoor navigation beneath it.
These are native identities with their own etudes and dialogue, not reusable free slots.
The prior recovery report's Aeon survival, Ravener death, aware-undead, Lich and parent-mod finale distinctions still govern whether one new living identity is appropriate.

The report supplies a concrete clone and candidate-placement recipe, not an executed runtime clone or obstacle-clearance pass.
Actual actor instantiation, class initialization, equipment appearance, active navigation, dynamic obstacles, social interaction, save/reload and duplicate prevention still require the service's headless construction checks and real Unity verification.
No persistent resurrection or in-game readiness is claimed here.
