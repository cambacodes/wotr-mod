# Areelu engine and survey-station repair

This author revision follows `areelu-choice-repair-independent-review.md`.
The starting source SHA-256 was `EC26B251855F2CEFBBB6236AC43077E218CEA718632C044CCEA8E5D591F57D3C`.
The revised source SHA-256 is `FDA89B9610C6951D0DA975768D4BB64885CA3145D64AEE1F9F99C93FFDE4C70A`.
The author of this repair cannot independently approve it.

## Choice and state repair

The survey-station kiss now ends with a player decision instead of supplying an overnight encounter.
The player can accept a private evening, keep the kiss as the evening's limit, or leave immediately.
Accepting the private evening leads to another explicit choice between staying until morning and returning to the Commander's own room.
Only choosing to stay schedules the morning followup.
The morning scene has an eight-hour minimum delay, and only its answer records `unmeasured_night_shared`.

The nonsexual handholding path remains an evening conversation followed by departure.
It no longer offers a morning continuation or sets the shared-night flag.
The common doorway conversation works after either an evening departure or a morning departure and no longer asserts daylight on every history.
The earlier private-kiss, no-touch, dinner, breakup, memory and gate-aftermath repairs remain in place.

The final private-letter page now describes an actual bundle of letters and a blank sheet rather than enumerating relationship-state categories.
The paused and closed futures no longer discuss what ?the ending? says or preserves.
These are fixes to the identified production-language passages, not a blanket independent certification of every line's voice.

## Actual starting-node contract

Current `src/Main.cs` opens `scene.Nodes[0]`, while `Entry` supplies the player's entry-answer text.
The manuscript transformation now emits the intended starting node first in every scene.
This puts `returned_entry`, `copy_entry` and `gate_entry` before their active pages so the new relationship guards actually run first under the engine's convention.
The emitted `Entry` field contains the scene's existing human-readable title instead of a node identifier.
The authored input retains its internal starting-node identifier only until the transformation builds the delivery dictionary.

Local traversal of emitted scenes now starts from `Nodes[0]`, including scheduled followups and final-outcome checks.
It does not use the display label as a graph address.
Graph assertions require every node to be reachable from the first stored node, matching the engine's validation rule.

The two skill choices at `record_entry` and `gate_entry_active` no longer contain both `Next` and `Check`.
Their success and failure fields supply the destinations.
The local structural check now rejects that invalid combination, checks positive DC and supported skill identifiers, rejects aborted or revival checks, requires distinct success/failure destinations, and verifies both destinations exist.
It also checks nonempty text and choices, unique nodes, chapter bounds and nonnegative delay fields.
Repeated generated Set flags are deduplicated without changing their meanings.

These are the applicable structural dictionary checks drawn from the current C# source.
They do not constitute a successful full C# package load.
Physical Areelu scenes still lack native attachment points and actor/contact bindings; the route and its condition producers remain unregistered.
The current engine's `EntryTargets` requires such attachment points before those scenes can be delivered.
No missing binding is invented to make validation appear complete.

## Timing repair

`copy_pause` now ends when the Commander leaves.
The three-day notice is a distinct 72-hour followup, with its own document and answer choices.
The first returned-name page now says that letters arrived since the hearing; it no longer claims ten days elapsed inside a sequence whose actual delay is seven days.
The spent-archive residents' next-morning walk is a separate twelve-hour followup.
The survey-station overnight conversation is a separate eight-hour followup after the explicit stay choice.

There are now 33 scene dictionaries and 214 emitted nodes.
That includes branch-specific followups and copied shared exits; it does not mean every playthrough visits 33 scenes.
The longest measured committed path visits 32 scene dictionaries, whose delay fields total 3,236 hours, or 134 days and 20 hours.
It does not visit the pause-notice branch.
The shortest measured committed path visits 19 scenes and has 1,728 hours, or 72 days, in delay fields.

These remain manuscript minimum-delay sums, not observed campaign durations.
Delivery later than eligibility, the timing of required native flags, actor availability, location and the time of day still require actual integration.
In particular, a delayed morning page needs correct delivery staging; its delay field alone does not reserve the Commander in a room or control the game's clock.
The large Chapter 5 calendar budget still needs design review.
The repair does not silently compress it or claim it is campaign-compatible.

## Verification

`py -m storylines.areelu_trickster_rivalry_opening` passes with 33 unintegrated scenes and 214 nodes.
`py -m py_compile storylines/areelu_trickster_rivalry_opening.py` passes.
`git diff --check -- storylines/areelu_trickster_rivalry_opening.py` passes.

New selected-choice assertions establish that the nonsexual path cannot reach the night or morning pages, kiss-only and immediate-departure choices avoid morning, and leaving after the private evening avoids morning as well.
The stay choice does reach the delayed morning, which is the sole producer of the shared-night flag.
The tests explicitly check the three repaired guard nodes are the first stored node of their delivery scene.
The existing final-outcome and earlier refusal/privacy/memory/gate checks still pass under first-node traversal.
No live in-game scene or C# package was executed during this repair.

## Selected minimum and maximum

A fresh local solver used `Nodes[0]` for every emitted scene, carried predicate-relevant flags between scenes, enforced scene and choice requirements and forbids, and explored both check outcomes.
It skipped unavailable branch followups and rejected abort, closed, ended, paused and rivalry-only outcomes.
It retained both minimum and maximum complete prefixes for each equivalent future state.
The final filter required commitment, sealed letters and the ordinary future.
The tokenizer came from `tools/measure-story-content.py`.
Entry labels, titles and unselected alternatives were excluded.

The entry fixture still assumes `entry_ready`, active Trickster, verified cradle-memory record and an available non-declined answer.
Those are missing runtime prerequisites, not an attained game route.

| Completed trajectory | Minimum selected words | Maximum selected words |
| --- | ---: | ---: |
| Any active committed trajectory | 15,231 | 25,650 |
| Private research pact and power-partnership terms | 17,435 | 25,650 |
| Protected memory, private counterledger, ordinary grounding | 16,075 | 23,123 |
| Protected memory, private counterledger, unresolved gate | 15,231 | 23,162 |

The every-route 21,000-word minimum still fails.
The shortest committed trajectory is 5,769 words below the floor.
The longest trajectory's numerical result is not proof that its repeated material earns that length.

Further development must supply distinct relationship and quest events for the shorter paths, including nonphysical courtship and choices to leave an evening early.
It must not make intimacy compulsory, remove refusal options, count alternate branches together, or retain repetitive material solely to protect a number.
That substantive continuation is not claimed as part of this focused repair.
Independent literary and branch review, initial Trickster acquisition, registration, native state readers, actor delivery, art assignments, save/load and ToyBox verification remain outstanding.
The route is not approved or ready for manual play.
