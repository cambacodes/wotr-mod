# Jerribeth recovery and physical contact audit

Examined installed blueprints and managed code on 2026-09-26.
This is a bounded implementation proposal, not approval of a working recovery route.
I previously reviewed the assembled Jerribeth writing and did not author those story modules.
No story, engine, native blueprint, installed mod or saved game was changed for this audit.

## Decision

The native game supplies usable identity and death evidence, but no discovered Jerribeth restoration quest or confirmed Act 5 placement.
A bespoke Trickster intervention must therefore be authored and implemented.
It cannot consist of clearing `jerribeth.unavailable`, replaying her native spawner, or pretending that a missing actor was successfully resurrected.
The smallest credible design separates retained dead actors, living hostile actors, departed actors and unknown histories before offering a negotiated return.
The existing correspondence route can continue after that return without resetting its relationship history.

## Reproducible evidence

The extraction script is [jerribeth-recovery-probe.py](jerribeth-recovery-probe.py).
It examines all 236,661 `.jbp` records and retains 309 relevant definitions or references in [jerribeth-recovery-records.json](jerribeth-recovery-records.json).
The record file contains exact blueprint paths, GUIDs, per-record SHA256, parsed fields and directly resolved installed English localization.
Faction and brain targets retain their definitions only, avoiding thousands of irrelevant combat-unit references.
The search found 17 references to the native unavailable marker, eight to the base unit, one to the Sanctum unit, 21 to VellexiaKilled and eight to the Sanctum map location.
[jerribeth-recovery-managed-records.json](jerribeth-recovery-managed-records.json) preserves fresh ILSpy output for UnitSpawnerBase, UnitSpawner, UnitDescriptor, ContextActionResurrect and UnitFromSpawnerIsDead, with the installed assembly hash.

Actual native bundle spawners and hashes were already extracted in [jerribeth-fate-native-evidence.md](jerribeth-fate-native-evidence.md).
This audit reread that evidence and independently checked the associated blueprint actions.
It does not claim a fresh exhaustive scan of every Unity scene bundle.

## Native identities and dispositions

| Role | Blueprint or saved spawner identity | Evidence |
| --- | --- | --- |
| Base Jerribeth, reused in Act 4 | `417ce3dcf3a9707488f2b9b2a790814b` | `Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Jerribeth.jbp` |
| Sanctum form | `bb9fe2c12d6941a43bfd5d5090ac97b9` | `Units/NPC/Unique/Act_3_DemonsHerecy/IvorySanctum/Jerribeth_Sanctum.jbp` |
| Wintersun variant | `fc8d7d07d716bee4499c9d17f6c43196` | `Units/NPC/Unique/Act_3_DemonsHerecy/Wintersun/Jerribeth_Wintersun.jbp` |
| Sanctum entrance | `9fa07641-a8db-4f01-b43e-28658574e4ce` | Scene `1b3609da30e000d4da2f192527f56b0d`, Sanctum blueprint |
| Sanctum final room | `b9c46ad9-ea18-462b-bfef-140a1060348c` | Same scene and blueprint |
| Default Vellexia manor | `5f976e09-1f17-4f78-907c-fb133d947090` | Scene `48a42fff8aa13dc46b09c4d230f9aac2`, base blueprint |
| Vellexia third date | `da348c4f-6c2a-452c-9c20-0d65fdba7168` | Scene `d6384baf058b5fc48aff9054c08745e7`, base blueprint |

These spawner IDs are not automatically the spawned actors' UniqueIds.
Resolve the saved spawner's UnitReference and validate the resulting actor rather than constructing an actor ID from a spawner ID.
Multiple native representations are expected across scenes, so choosing the first unit with a matching blueprint is unsafe.

The native forms are ChaoticEvil and use portrait `6f8d1a597cc64337a2fbb83b0d986768` and prefab `f8acb79bcccd0fb4a93db8e50a0d7c82`.
The base blueprint inherits the oolioddroo parent `7e22e32226ef6cf469bf00a047a96c80`.
A humanized portrait does not make the native actor human or justify replacing her demon abilities and motives in the story.
The base and Wintersun variants use `Factions/Mobs.jbp`, `0f539babafb47fe4586b719d02aff7c4`, whose attack list includes player-facing factions.
The Sanctum variant uses `Factions/CutsceneNeutrals.jbp`, `d64258e86eeb1d8479f35a9b16f6590a`, with an empty attack list but Peaceful, Neutral and NeverJoinCombat all false.
Neither configuration establishes a safe permanent capital guest.
Her brain `f8ff8935f7859494fb18e056657d30ff` contains 14 combat action references.

Both inspected base and Sanctum definitions have ten components, including two MobCaster components, two AddClassLevels components, Experience, ApplyClassProgression, three AddFacts components and ChangeImpatience.
The class entries grant 14 levels of `92ab5f2fe00631b44810deffcc1a97fd` and four of `2a624b417a801be49b8b97b6355e2f4c`.
Terendelev's human clone allowlist cannot be reused for this creature.
A future delivery blueprint needs a separate review of the referenced facts, class grants, visual barks, weapons and combat brain before its allowlist is accepted.

## The unavailable marker is not a death certificate

`JerribethDead`, `cd8666952065ce74d94d960a23482133`, has no restoration components.
Its parent `ImportantNPCs_fate/Jerribeth`, `cc5e8c94d484b9c48ad32afd6d5c90ef`, likewise supplies no restoration mechanism.

| Native producer | When the marker starts |
| --- | --- |
| JerribethGreetings/Cue_0029, `a59dfd2fd29eeb54dbcf891c71d7b6ea` | OnStop, before running cutscene `e92347099ddedf9409fb314aa23965ec` |
| JerribetnFinal/Answer_0017, `e3158fbb613ebec4bade9b91b9c31aed` | On selecting the attack answer, before StartCombat |
| JerribetnFinal/Cue_0012, `09280d586e0118b4882abcdb5a4787c6` | Before Glabrezu spawning and StartCombat |
| JerribetnFinal/Cue_0029, `8ccd036dc7f03704590ac5787c3997d2` | Before Glabrezu spawning and StartCombat |
| IvorySanctum_MainEtude, EvaluatedUnitDeathTrigger named `$EvaluatedUnitDeathTrigger$ead58c78-e194-414e-ba73-b42d5366ec14` | Actual entrance-spawner death |

The attack answer's alignment description calls the act a killing even though its effects start combat.
That description is not independent evidence that the combat ended in death.
No distinct final-room actual-death etude was established in this scan.

The marker also changes native Demon quest handling.
`03_SanctumBosses`, `d44f91b07f9914349aa0b6c082d98c25`, checks Started and conditionally starts a timer, completes another etude and grants quest experience.
`04_ReportToJerri`, `56dbf60a49b985d449187c410a060d7c`, checks NotStarted for its timer and experience branch.
Preserve these records and the marker even after an authored return.
Do not replay native objective completion or grant its experience again.

## Saved actor evidence and real resurrection API

`UnitSpawnerBase.MyData` serializes `m_SpawnedUnit`, `HasSpawned` and `HasDied`.
`SpawnedUnitHasDied` returns false unless HasSpawned is true.
When a spawned actor resolves, it reads that actor's `State.IsDead`; otherwise it falls back to saved `Data.HasDied`.
`UnitFromSpawnerIsDead` uses that property, but requires an actual spawner view and returns false when the view cannot be found.
Consequently, calling the condition in Drezen cannot prove that an unloaded Sanctum actor survived.
A saved-state reader must preserve Unknown as distinct from Alive.

`UnitDescriptor.ResurrectAndFullRestore(initiator)` operates on an existing actor.
It clears death state, restores damage and attributes, handles negative levels, updates a present view and raises `IUnitResurrectedHandler.HandleUnitResurrected`.
It does not create a missing actor, clear a native etude, change faction, restore a destroyed scene object, or guarantee a navigable destination.
NPC relocation also cannot be inferred from the player-faction-specific position correction in that method.
The context action adds a resurrection buff after invoking the descriptor API, so the descriptor call alone is not a reproduction of the entire spell action.

`TrySpawnOrRespawn` and `ForceReSpawn` clear or replace the old spawner reference and can destroy the existing actor.
They are inappropriate shortcuts for a history-preserving recovery route.
Restoring a retained actor can change what native death conditions observe and raises global events even without resetting etudes.
That requires explicit native quest/event regression checks; it is not a side-effect-free operation.

## Departure, patron and Act 5 limits

The final Sanctum departure hides Jerribeth, the Marhevok pot and servants.
Reversing that cutscene would affect more than one NPC and must not be used as a romance delivery action.
Both Sanctum spawners have RespawnIfDead false.

VellexiaKilled is `72e423c719ed9d44fa432a6b9629babd`.
The installed departure bark says Jerribeth needs a new patron and must leave because the place is no longer safe.
The departure cutscene first plays a teleport-style effect and then destroys the third-date actor.
This supports a living departure, not an inferred Jerribeth death or a known new residence.
Do not turn Vellexia's death into proof that she released employees, debts or other dependents.
Her refuge explanation establishes patronage and companionship; it does not establish a sexual relationship with Vellexia.

The named and direct Jerribeth-reference scan did not establish an Act 5 actor placement.
It is not an exhaustive proof that every bundle lacks one.
The Ivory Sanctum map point `669220945fa20fa4a9317dea3618a19c` is not closed on start and has no location variations, but its reveal condition is False and a native quest addendum explicitly unlocks it.
These fields do not prove access on every Act 5 save.
Do not make a mandatory recovery route depend solely on revisiting that area until actual campaign access is verified.
The previously transcribed tablet text naming Jerribeth and Xanthir was not found by its localization key in this blueprint scan.
It remains useful narrative context, but is not yet a verified new interaction hook or collectible item.

## Concrete authored route proposal

Use an Act 5 Trickster investigation available from the commander's existing remote interface, without requiring the missed manor encounter.
Gate it on the current appropriate Trickster access and forbid `jerribeth.closed` throughout.
Retained history after a later mythic conversion needs an explicit separate continuation rule; it must not silently grant fresh Trickster acquisition to another path.
The premise is an attempted correction to the Sanctum's succession and Jerribeth's interrupted dealings, grounded in her actual role and the commander's campaign knowledge.
The impossible reply and any identity reconstruction are authored Trickster developments, not recovered native content or ordinary resurrection lore.

1. An investigation scene establishes which history can actually be observed.
   Known killing, attack without verified death, missed contact and loss of Vellexia each get different wording.
   Unknown evidence receives no invented corpse, witnessed death, friendship or remembered invitation.
2. A bounded challenge exposes an imitation that can repeat public facts but cannot answer a chosen consequence from the commander's recorded history.
   Use verified native cue/answer evidence where present and a fresh contest where no personal meeting occurred.
   Check failure should cost a lead or require a different played approach; it must not fabricate the right identity or permanently exclude an otherwise eligible Trickster.
3. Jerribeth bargains over her own return or relocation.
   She wants independent access to clients and protection from being treated as another patron's property.
   She can resent a killing and demand compensation without becoming repentant or automatically attracted.
   Existing endangered employees and retained native patron history constrain the bargain rather than becoming free rewards.
4. Only a completed voluntary agreement authorizes the actor operation.
   The player can abandon the intervention, negotiate, or leave the relationship closed.
   Recovery success grants access to an invitation or resumes earned correspondence; it does not grant lovers, commitment, met-native-cue history, mythic rank or native quest completion.
5. A separate arrival conversation proves physical contact and addresses the specific cost of the bargain.
   Her true form remains recognizable; a chosen guise is her presentation, not an explanation that she has become human.

The first implementation should expose a narrow request/poll operation and typed evidence result rather than build a general NPC resurrection framework.

| Evidence | Proposed actor operation | Non-negotiable limit |
| --- | --- | --- |
| Exact retained dead native actor | After the authored agreement, restore that actor through verified descriptor API and a separately tested placement transaction | Preserve actor identity and native flags; verify resurrection events and hostility before completion |
| Exact retained living actor, hostile or hidden | Negotiate first, then relocate only that identified actor with deliberately scoped disposition handling | Never unhide a whole cutscene group or reset global faction relations |
| Explicit departed native copy destroyed, no surviving conflicting representation | Authored voluntary arrival through a reviewed private delivery actor, with source-history provenance stored | Call this a new representation of a returning NPC, not resurrection of the destroyed Unity object |
| Saved spawner proves death but actor was discarded | Separate authored reconstitution branch and explicit materialization contract | Do not instantiate a fake dead actor just to call Resurrect and report success |
| Missing or contradictory actor/spawner evidence | Investigation remains unresolved until the authored identity process establishes a supported result | No marker-based guess, arbitrary actor deletion or success flag |

The last two rows are still implementation prerequisites, not completed universal access.
A living blueprint alone is insufficient proof that the person and her history have been restored.
The proposal must preserve that distinction in both narrative and engine results.

## Integration and verification requirements

The current relationship has `UnavailableFlags=["jerribeth.unavailable"]`, and individual scenes also forbid that flag.
Current ContactAvailable independently enforces relationship unavailability for physical scenes.
An authored recovery scene or a scene ForbidOverrides entry alone cannot make the whole route work while the native marker stays set.
Integration needs one narrow, consistently applied authored recovery condition for this native unavailable flag, at both entry and continuation, while preserving every closed/refusal flag and other native restriction.
That condition must require verified delivery or negotiated living contact, not the request to attempt it.
Do not remap the original native alias to hide its true state.

NativeContact currently verifies a unique loaded unit for the configured blueprint, current saved storage, live active view, consciousness and nonhostility.
A private delivery actor requires an explicit supported identity/contact binding; the old Act 4 blueprint alone will not recognize it.
For correspondence after recovery, distinguish actual ongoing remote consent from physical presence requirements.
Do not claim the 38 existing scenes are physical meetings merely because an arrival actor exists.

Before implementation, choose and verify a destination anchor in the intended loaded area part.
No new coordinate is certified by this audit.
Terendelev's outdoor anchor and clone allowlist are not transferable evidence for Jerribeth.
For new materialization, persist a stable actor ID before dispatch, reject collisions, and confirm exact registry object, HoldingState, saved state membership and alive nonhostile view after the engine commits the queued entity.
On save/load, adopt only the proven actor belonging to the saved attempt.
A return from SpawnUnit is not completion.

Focused checks must cover attack-before-death, retained corpse, discarded corpse with saved death, hidden survivor, destroyed departed representation, duplicate representations, missed native dialog and unsupported map access.
Also cover request persistence failure, queued spawn across save/load, identity collision, actor death or disappearance during conversation, and withdrawal before commitment.
All native quest/etude/cue/answer history must compare unchanged across the intervention except engine-observed consequences explicitly documented for real resurrection.
The native death-trigger and resurrection-event cases require live game verification in addition to managed fixtures.
An accepted branch must leave old earned correspondence, old endings, other romances and ToyBox free-love/no-jealousy behavior intact.

This research makes the next implementation concrete, but does not certify full Trickster recovery or runtime actor delivery.

## Targeted implementation follow-up

The subsequent [implementation contract](../parallel/jerribeth-recovery-implementation-plan.md) resolves the loaded saved-spawner lookup and proposes a specifically inspected capital arrival vicinity.
The extended probe's `--delivery` mode now records Jerribeth's true-form prefab collider and the actual StorytellerPosition locator with its parent transforms.
The current navigation bundle hash matches the earlier parsed triangle evidence, retained with that provenance rather than described as a new live navmesh test.
This updates the earlier lack of a proposed coordinate: the anchor is verified, while the final free standing position and camera clearance remain runtime checks.

Jerribeth's collider is approximately2.4m high with radius1.0 and corpulence0.9.
The existing Terendelev placement volume cannot be reused unchanged.
The capital vicinity is shared with native actors and may already be occupied; delivery must wait when no validated free position exists.

Fresh decompilation establishes that `PersistentState.SavedAreaStates` can be inspected without creating a state and that `UnitReference.UniqueId` preserves the actor reference even when Value cannot resolve.
It also establishes that `SceneEntitiesState.RemoveEntityData` disposes the entity.
A remove/add transfer is therefore unsafe.
The earlier proposal for retained actor relocation is narrowed to in-place restoration in the actor's own loaded source state until a real cross-area transfer path is separately verified.
Missing or unreadable unloaded-state evidence remains Unknown and never authorizes a duplicate body.
