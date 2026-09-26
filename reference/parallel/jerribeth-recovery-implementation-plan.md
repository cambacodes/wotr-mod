# Jerribeth recovery implementation contract

Prepared 2026-09-26 from the installed game and the existing delivery service.
This plan specifies the smallest safe next implementation and names the branches it cannot yet complete.
It does not approve a returned actor, universal Trickster access or a live save.
Only the assigned Jerribeth evidence and planning files were changed.

## Concrete next change

Implement a Jerribeth-specific evidence reader and a request/poll coordinator before adding successful-return dialogue.
Use the existing mod conversation action for the first verified meeting.
Do not add a general revival framework or copy Terendelev's complete service under a new name.
The immediate supported operation is recovery of an exact retained actor in its own loaded source scene after an authored voluntary agreement.
Capital delivery is a separate operation for a reviewed returning representation, not a fallback when retained-actor lookup fails.

The original native unavailable marker stays intact in all branches.
The source identity, observed history and selected authored bargain belong in a saved request.
Neither a saved request nor a spawn return may grant the relationship's recovery-success condition.
An explicit romantic refusal remains final regardless of recovery eligibility.

## Newly resolved facts

`Game.State` is `Kingmaker.EntitySystem.PersistentState`.
Its public `SavedAreaStates` list can be searched without constructing a new area state.
`GetStateForArea` creates a new state when absent, so it is unsuitable as proof that a native encounter was visited or retained.
Likewise, finding no actor in `Game.State.Units` proves nothing about an unloaded saved scene.

`UnitSpawnerBase.MyData.SpawnedUnit.UniqueId` exposes the saved actor ID without requiring the actor to resolve.
`UnitReference.Value` consults the entity proxy; it does not load the absent scene.
Use the exact saved spawner identity from the audit, then this saved actor reference, then validate the actor's expected blueprint and storage.
Do not substitute a spawner GUID for an actor GUID.
Do not collapse an unresolved reference into an alive or dead answer.

`AreaDataStash.GetJsonStreamForArea(area, state)` reads the corresponding stash file and returns null when absent or unreadable.
If an unloaded-state inspection is needed, consume that stream into inert JSON tokens only.
Do not call the game's entity serializer or `UnstashAreaState` to conduct an observation.
The latter performs real state restoration and can dispose an existing area proxy; `UnstashAreaSubState` installs scene state and calls PostLoad.
Those are engine operations, not harmless JSON readers.
A missing file remains Unknown, especially before normal save/load completion.
The exact serialized spawner/UnitReference token shape still needs a captured real save before a raw-token adapter can be accepted.
The initial implementation can return SourceNotLoaded rather than invent a raw schema.

`SceneEntitiesState.RemoveEntityData` sets HoldingState null and calls Dispose before removing the actor from its collection.
It is not a transfer method.
`AddEntityData` adds storage and sets HoldingState but does not remove old storage.
A naive remove/add transfer destroys the actor, while an add-only transfer risks duplicate persistence.
No identity-preserving cross-area native NPC transfer is certified by this research.
Retained actor recovery must therefore stay in its original loaded source storage in the first implementation.
Cross-area relocation requires a separately verified native transfer path and save/load tests.

These methods and the fresh UnitReference decompile are retained in `reference/canon-review/jerribeth-recovery-managed-records.json`.
An attempted full UnitEntityData C# decompile hit an ILSpy stack overflow; no transfer claim is derived from that failed extraction.

## Exact actor observation result

Return one immutable observation with an evidence kind, source scene, source spawner, referenced actor ID, expected blueprint, native history snapshot and any conflict reason.
The minimal evidence kinds are Unknown, RetainedAlive, RetainedDead, RecordedDeadMissingActor and Conflict.
Keep observed hostility and visibility as separate fields because neither changes identity or proves death.
Departure cue/cutscene history is additional provenance, not an alternative mechanical life-state test.

Read only after the game's loading/unloading process finishes.
For a loaded source, require the spawner's actual saved data and a unique matching actor reference.
For an unloaded source, return Unknown unless the saved record was inspected without instantiating game entities.
RetainedDead requires the referenced actor's actual dead state.
RecordedDeadMissingActor requires HasSpawned, saved HasDied and an unresolved saved actor reference; it is not permission to create a fake corpse.
JerribethDead alone never produces either death result.
Conflicting live representations or a reference to the wrong blueprint produce Conflict, not a preference for whichever actor is convenient.
Hidden entrance/final representations must be identified by their individual source histories rather than treated as automatic duplicates to delete.

## Request and polling contract

Suggested narrow signatures are `Observe()`, `Request(observation, agreement, currentEligibility)` and `Poll(currentEligibility)`.
The agreement identifies the fully played authored bargain; it must not be a caller-supplied arbitrary string used as proof of consent.
The coordinator validates it against actual saved story milestones and the observation.
CurrentEligibility includes the applicable mythic gate, campaign stage and absence of a closed relationship.
After an intervention was legitimately earned, any permitted later mythic continuation must be an explicit rule, not a fresh acquisition shortcut.

The per-save request stores version, operation, source scene/spawner, source actor ID if known, source blueprint, evidence kind, agreement milestone, assigned delivery ID if applicable, dispatched status and confirmed status.
Use a single operation enum with RestoreRetained and DeliverReturningRepresentation initially.
Do not expose discarded-body reconstruction as an implemented operation until its authored identity process and materialization policy are reviewed.

The result set should distinguish NotRequested, Pending, Blocked and Confirmed.
Pending covers an unloaded destination or queued engine creation.
Blocked covers conflicting identity, revoked agreement, wrong mythic access, closed relationship, a killed confirmed actor, or a dispatched request whose entity cannot be recovered safely.
Return narrative-safe status to the player and retain exact technical diagnostics separately.

For RestoreRetained, persist the exact source actor ID before invoking resurrection.
Require that source area and scene are actually loaded, that its saved actor is the same registry object, and that it is still dead.
Call the verified descriptor resurrection API on that actor only.
On a subsequent poll, confirm the same actor is living, conscious, not suppressed, visible and nonhostile in its original saved storage.
The call itself must not set success.
Resurrection does not resolve hostility, hidden state or quest consequences automatically.
If negotiated disposition/visibility handling has not been independently implemented and reviewed, return Blocked with the living actor preserved rather than pretending that contact is available.
Resurrection raises global events, so a failure after that mutation must be recorded as dispatched and reconciled from the actual actor on retry.
Never call resurrection twice simply because the final story flag was not written.

For DeliverReturningRepresentation, first prove that the supported departed history and authored return agreement apply and that no conflicting retained living representation requires reconciliation.
Register one separately reviewed private blueprint before load.
Persist the stable delivery ID before SpawnUnit.
Then follow the reviewed queue, registry, state-membership and load-adoption pattern described below.
This operation represents a new scene body for a voluntarily returning person; it does not claim to preserve an old Unity entity or prove resurrection.
It cannot be silently substituted for RestoreRetained or RecordedDeadMissingActor.

## Capital arrival vicinity and actual dimensions

The extended probe's `--delivery` mode rereads the installed Jerribeth prefab and capital locator with UnityPy.
Records are appended under `delivery` in `jerribeth-recovery-records.json`.
It also checks that the current navigation bundle hash matches the previously parsed navigation evidence before retaining that evidence with explicit provenance.
This is a new asset/transform inspection plus a hash check of prior parsed navigation, not a fresh live pathfinding run.

The proposed public arrival vicinity is the existing outdoor StorytellerPosition locator, not the Storyteller actor's occupied point.
GameObject468, transform1207, locator component2718 in `drezencapital_default_mechanics.scenes` identify it as `236d0480-c95c-431d-87d3-8e966fc9ffbd`.
Its position is approximately `(7.49, 62, -28.07)` and its rotation approximately `(0, -0.08658724, 0, 0.99624425)`.
The newly extracted parent transform chain confirms the world transform used in the prior audit.
This vicinity is a proposal for the agreed capital meeting, not a canonical Jerribeth location.
It is shared space and must not displace the Storyteller, Terendelev or any other actor.

The actual destination storage is the loaded outdoor dynamic scene `DrezenCapital_Outdoor_Mechanics`, in area `2570015799edf594daf2f076f2f975d8`, outdoor part `8a076e720870a44438d13b9b939933fd`.
Do not save the delivery into the default mechanics merely because that bundle contains the locator.
Do not use the area's MainState, which represents the throne room in this setup.
Require an existing loaded, serializable scene state and the actual current outdoor part.

Native prefab `f8acb79bcccd0fb4a93db8e50a0d7c82.unit` has root UnitEntityView component `-2623573646244160563` on GameObject `-1999383574769128734`.
Its soft collider height is about 2.4, radius 1.0 and corpulence 0.9.
Terendelev's code uses a height suited to her 1.8m human prefab and therefore cannot be copied unchanged.
Use Jerribeth's inspected collider dimensions for placement, with a conservative margin, and retain a live check of the instantiated view.
The baked triangle under StorytellerPosition is walkable at approximately62.0054; it does not establish enough unobstructed volume for this larger actor or her rendered wings.

Select a live free position near the anchor using the existing FreePlaceSelector approach, then verify the center and full footprint remain on the same walkable navigation region.
Check standing volume at Jerribeth's full height against static colliders and dynamic actors.
Reject positions beyond the agreed bounded vicinity or on a different floor.
If Storyteller, Terendelev or another NPC occupies all acceptable space, remain Pending.
Do not move that occupant, reduce the tested footprint or choose an arbitrary position elsewhere.
Camera framing and wing clipping still require an actual scene inspection.

## Terendelev reuse boundaries

Reuse the pattern of stable checkpoint-before-dispatch, exact registry lookup, queued-entity detection, exact HoldingState membership and post-load adoption.
Reuse the principle that Submitted without an identifiable actor blocks automatic redispatch.
Reuse registration-before-deserialization for any private delivery blueprint.
Reuse narrative-safe status plus LastError-style diagnostic separation.
These can remain local code until an actual duplicate implementation justifies a small shared helper.

Do not reuse the human blueprint allowlist, native identity conflicts, 1.8m collider assumptions or arrival-success conditions without Jerribeth's own validation.
Her ten combat components, class progression, added facts and native spellcasting require a separate private-blueprint review.
Her true form must retain its native body and animation setup.
Neutral faction and passive brain belong only to an explicitly negotiated social representation, never a mutation of the cached native blueprint or a rewrite of her moral alignment.
Removing Experience prevents importing an encounter reward, but by itself does not make an NPC safe or stop inherited behavior.
Do not strip every class component merely to obtain a passive prop with invalid health.

Terendelev's conflict scan only covers the loaded destination's actors.
That is insufficient to prove that no native Jerribeth survives in another saved scene.
Jerribeth needs the source observation before authorizing delivery.
Terendelev's clone construction fixtures also do not prove a live Unity deep copy or rendered body.
Keep actual clone registration and actor materialization verification separate from those fixtures.

## Required acceptance tests

Start with the closest executable end-user sequence: earn the authored agreement through Rules, call the adapter, poll, then attempt the arrival conversation.
The conversation must remain unavailable until the adapter confirms contact.
Fixture-only adapter tests supplement this sequence; they must not replace it with a boolean marked successful.

| Test group | Required cases and evidence |
| --- | --- |
| Native observation | Attack marker before death remains alive/hostile; actual retained corpse; HasDied with unresolved reference; unloaded scene; missing stash; hidden survivor; destroyed departed representation; conflicting live copy; wrong blueprint under the saved ID. |
| Retained operation | Persist failure before dispatch performs no resurrection; resurrection event runs once; retry adopts the same living actor; hostile, hidden, unconscious or missing-view actor does not confirm; original HoldingState and actor ID remain unchanged. |
| Delivery | Save stable ID before creation; null spawn; registry-before-state insertion; queued actor; duplicate ID; wrong blueprint; another private actor; wrong scene; rejected volume; loading transition; save/load before and after commit; confirmed actor killed later does not respawn. |
| Narrative access | Native unavailable marker survives; verified recovery permits only the intended exception; relationship refusal and all unrelated blockers remain; failed checks keep an attainable alternate investigation; missed-contact prose invents no shared native memory. |
| Consequences | Native quest states, selected answers, seen cues and other romances compare unchanged; actual resurrection-event differences are documented; no repeated native XP, medallion, servant or patron changes. |
| Placement | Existing Storyteller/Terendelev blocks occupied space; Jerribeth's 2.4m body fits; same-floor navigation and footprint pass; indoor/other-part requests remain pending; view and camera have no obvious clipping. |

Use actual managed APIs for clone construction and fixture compilation, with isolated build outputs.
Use real saves for persistent actor identity, spawner history, resurrection events, scene unloading and reload.
At least one save must represent attack-marker-with-survival, one a retained death, and one Vellexia departure; none may be manufactured by clearing native history to fit the test.
Include ToyBox free-love/no-jealousy enabled and existing other romance history in the final runtime pass.

## Remaining bounded prerequisites

The observation/coordinator contract and capital placement checks are ready to implement within the limits above.
The discarded-dead or unknown-identity case still needs an authored, reviewed reconstitution process before any new living body can represent recovery.
A safe identity-preserving cross-area transfer remains unverified and is deliberately excluded from the first retained-actor operation.
The native Jerribeth added-fact and class behavior allowlist remains a prerequisite to registering a private social body.
These are concrete next tasks, not reasons to claim the existing romance already supports every Trickster history.
