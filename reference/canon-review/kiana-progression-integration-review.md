# Kiana progression integration audit

Decision: no blocking defect identified in the inspected progression integration for supported authored histories.
This is a bounded technical acceptance, not full-character or live-game approval.
The reviewer did not author the new progression, queue changes, or tests.
The reviewer previously authored `kiana_followthrough.py`, so this report does not independently score or approve that module's prose.

## Inspected artifact and execution

Stage: `development/kiana-progression-review.json`.
SHA256: `17170B8915EFB569280EB76F7D50BD4656CBE46EE44BBBFE437E82975486DA17`.
The artifact contains 204 scenes, including 33 Kiana scenes.

All four current Kiana modules match their staged scene dictionaries after normal JSON normalization of Python tuples to arrays.
Inspected source hashes are recorded below.

| Module | SHA256 |
|---|---|
| `kiana.py` | `095CC97EB49E55E0E9DC73E2F59C5020C424360533D5A77BF83D4728078C2EF7` |
| `kiana_consequences.py` | `445023B128A4DD6B19C9F3F193E7EFCD8FFD6278AF00979257F43C1B79ACB3FE` |
| `kiana_followthrough.py` | `BDBEF6ABD0B3097DC480B11A05921BAD57E833877E15F54FBE560B647C31BACD` |
| `kiana_progression.py` | `9DA195E83020C5C3D09E86C654EA0BCD076939F7A339033AC92DEE7B356279A5` |

The reviewer independently executed the existing Release rules runner with `--kiana-progression` and this exact staged artifact.
It passed **8,140,239 assertions**.
This rerun includes the registered progression tests and root's updated `CheckKianaCampaign`.
The parent's reported 308 bindings across 62 targets and 22,365 managed assertions covering 6,819 blueprints were not independently rerun for this report.
Those figures must retain their parent-executed attribution.

A read-only comparison with the 198-scene main artifact found no removed existing Kiana node and no changed existing choice array.
The existing answer ordering, effects, and next-node references are preserved.
Changes to existing scenes concern progression requirements, ending applicability, ManualOnly, and farewell overrides.
The new progression scenes and endings have their own IDs.

## Automatic delivery and manual choices

`Rules.NextRemote` selects the first available remote scene that is not ManualOnly.
`Main.Update` uses this method for ordinary rest scheduling and checks actual availability again before starting the queued scene.
The mod's manual Read interface still lists available ManualOnly scenes and allows them to be selected explicitly.
ManualOnly is therefore a scheduling exclusion, not a state that makes the relationship decision unreachable.

The two Kiana ManualOnly scenes are `parting` and `another_page`.
This removes the old breakup/stay conversation from automatic delivery without removing manual breakup access.
It also prevents an old completed farewell from automatically becoming consent to further content.

Farewell requires its original morning milestone and either `future_settled` or the existing `inhuman` fallback.
Moving the scene later in the list alone would not have solved the original defect because a waiting-period gap could still make farewell the first eligible event.
The actual added condition blocks that gap for supported ordinary histories.
Arbitrarily advancing time does not supply the missing developed decision.

The progression suite walks the actual Kiana prerequisites, then invokes production `Rules.NextRemote` against the ordered Kiana scene subset.
The observed sequence is guest_table, market_weather, lenna_door, blue_room, bakery_stairs, last_page, first_readers, ink_after, working_room, kept_evening, and a_place_afterward.
Thus guest_table wins over farewell and the manual parting scene when its actual delay is met.
This proves Kiana-relative delivery, not global fairness among every character's competing rest events.
Other available remote scenes can delay a Kiana event, and this report does not establish a scheduler starvation bound.

## Old farewells and state preservation

Without opt-in, an old farewell continues to block the ten continuation scenes and the new capstone.
`another_page` is available as a manual choice for an eligible old history and does not enter the rest queue.
Its initial deferral preserves the prior flag set.
Completing the reply records `catchup_requested` and the new scene completion, without clearing or retiming the old farewell.

Exactly eleven staged Kiana scenes declare `ForbidOverrides` with the single mapping `kiana.farewell -> kiana.catchup_requested`.
They are the ten consecutive continuation scenes and `a_place_afterward`.
The override affects only that authored forbid.
The code still evaluates required flags, alternative prerequisites, chapter, area, relationship closure, unavailability, and delays.
Completed-scene exclusion runs first, so previously played scenes do not repeat after the opt-in.

Schema validation requires the overridden key to be an existing scene forbid and both names to be authored flags.
It rejects overrides of relationship closure, mapped native predicates, and derived flags.
The actual Kiana metadata uses no other override key.
No reset operation is introduced; progress recording remains additive.

The tested old-save histories preserve farewell flags and the original farewell timestamp, marital history, prior commitment, native predicates, and unrelated relationship sentinels.
Already committed histories remain committed even if the later answer closes the relationship; closure takes precedence in ending selection.
Catch-up does not falsely label an earlier uncommitted history as a broken promise.

## Capstone and endings

`a_place_afterward` requires the completed soul quest, lovers, morning, and actual followthrough completion.
Its 48-hour delay is anchored to the latest timestamp among these required flags, including the newly earned followthrough milestone.
The capstone cannot be reached by letting time pass before the continuation is complete.

The separated and bereaved pages use mutually exclusive supported history conditions and the actual Elan death alias.
Neither grants native death, resurrection, separation, or marital consent.
An existing commitment can be reaffirmed or the relationship ended.
An uncommitted Commander can commit, continue openly without promising a lifetime, or end the relationship.
Only completed answers set `future_settled`; initial deferral leaves the relationship decision unrecorded.
The open answer cannot downgrade an existing commitment because it is unavailable to a committed history.

Normal ending selection is exclusive in the tested separated/widow, wait/affair, committed/uncommitted, old/new farewell combinations.
Developed committed histories select together or bereaved, developed open histories select open, and closure selects apart.
Ascension selects the corresponding committed or open ascended outcome while closure still selects apart.
Continuing open histories have a separate Aeon ending; committed histories retain the existing Aeon outcome.

An earlier commitment lacking `future_settled` receives the provisional promised ending.
An earlier uncommitted history receives unfinished rather than a developed open ending.
The provisional promised ending also remains the deliberate fallback for the abbreviated transformed history.
It does not assert that the unavailable physical continuation was played.

Farewell's old 48-hour delay remains based on morning.
`RequiresAny` is an eligibility condition, not a new timing source, so another rest can deliver farewell immediately after a completed capstone.
This matches the handoff and is not represented as a new 48-hour wait after the decision.
An old completed farewell remains excluded after catch-up, so no second farewell is silently fabricated.

## Coverage limits and remaining work

The new tests cover twelve principal combinations and every capstone node, while existing consequence/follow-through tests cover their internal literary branches.
Root's older campaign test now plays the continuation and capstone before farewell for ordinary histories instead of retaining the old shortcut as its expected behavior.
The test retains the transformed fallback without claiming full transformed-route depth.

The normal tested histories keep native and authored marital predicates consistent.
The capstone history page has no fallback for externally altered inconsistent states such as `kiana.separated` plus a later `seelah.elan_dead` flag, or neither supported marital outcome.
This is not a newly demonstrated native reachable path after the completed soul quest, but supported restoration or arbitrary edited saves must not be advertised as covered.
If such transitions become supported, they need an authored reconciliation branch and a corresponding test rather than silently selecting the wrong spouse history.

Native guards here establish the completed quest and previously seen aftermath conditions, with the existing remote presentation model.
Kiana's relationship still has no live-unit unavailable flags, and these scenes have no ContactUnit.
`ContactAvailable` returns true for that model, so the source does not prove a native actor is currently present or provide a native-contact resume guard inside an already running book.
This limitation predates the progression repair and remains relevant to full-game verification.

The reviewer did not inspect rendered dialogue, native save serialization, actual rest-event timing, artwork, or a running ToyBox configuration.
No source, export, test, or installed file was changed during the review.
The bounded integration is acceptable for staged promotion after the parent's remaining release checks; full-route literary, native availability, mythic, visual, and game-level requirements remain open.
