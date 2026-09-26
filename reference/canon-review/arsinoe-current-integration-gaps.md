# Arsinoe current integration gaps

The existing capital, ceremony and live-contact integration is sufficient for a bounded development-stage opening, subject to current production verification.
The incomplete full romance is not itself a reason to withhold the five opening scenes from an explicitly incomplete development export.
One concrete opening-level issue needs repair before promotion: interruption and replay can accumulate mutually exclusive relationship choices and expose romance after a later friendship selection.
No new blanket mythic exclusion is justified by the inspected evidence beyond the existing Swarm and true-Lich restrictions.

## Current evidence

Reviewed source `storylines/arsinoe_opening.py` SHA256: `996CE4772C1A9A74663C40E77139D5B7F950F82705902BD55535471248A2071B`.
It is the same source accepted in the earlier bounded contact review.
I independently compared all five imported scene objects, the relationship and both etude bindings with `development/arsinoe-integration-review.json`; they are equal.
I also compared the three native records in `reference/canon-review/arsinoe-contact-native-records.json` with their exact paths in the installed `blueprints.zip`; every Data object matches.
At inspection, the current main development export has 225 scenes and no Arsinoe scenes.
`expansion.py` does not yet register her relationship, aliases or scene module.

Current engine hashes inspected:

| File | SHA256 |
| --- | --- |
| `src/NativeContact.cs` | `27E573ECFB994609730B265646EA7B6D4AFFC47B394A50B6D6BB2287D0FA957D` |
| `src/Story.cs` | `E83221EC7D0D6AD23F9073482B08A340D3DBEA4E8137300510415D985E322026` |
| `src/Main.cs` | `3CA9FFA76608B3C344F5C068FBFBE22D9D94B4CBEFDAE4DD24539FA496A6E10B` |

The earlier contact review reported 3,232,840 production-rules assertions, 311 binding uses against 66 typed targets and 22,367 managed construction assertions over 6,785 blueprints.
Those are historical parent-run results for the older stage, not a current combined-export run or a Unity certification.
The earlier writing review also remains bounded to this opening's corrected prose.
I did not assign a new literary score here.

## Required native guards already present

| Concern | Exact current implementation | Integration requirement |
| --- | --- | --- |
| Capital role | Require Playing `arsinoe.capital`, etude `3f3fbb973a4ffee47956b4c7714c939a`. | Register the alias and retain the requirement on every scene. Do not substitute chapter or historical etude completion. |
| Ceremony suppression | Relationship unavailable while `arsinoe.victims_revived`, etude `6d3fb96f9b60c0449a01add4be5c4a49`, is Playing. | Keep it temporary and out of PermanentEtudes and FailureFlags. |
| Physical actor | ContactUnit `a609ed9b2205d034bb3bb04d2a255681`. | Preserve exact live-actor checks at entry and continuation. Do not use the unused or DLC replacement unit. |
| Native entry | Answer list `ecaf5cfe8087a4f45a2269974f4885c9` in vendor dialogue `d5adc0bbbad5f054098b527cf9cc64f1`. | Register the existing attachment without replacing native vendor or quest answers. |
| Location and chapter | Drezen `2570015799edf594daf2f076f2f975d8`, Chapters 3 and 5. | Retain these restrictions; the scenes do not establish Threshold, Nexus or DLC contact. |
| Swarm | Existing `swarm` alias `439e63fed37f52048887d98f99255e40` in UnavailableFlags. | Preserve the block for the warm personal opening. Continued native vendor service is not romantic consent. |
| True Lich | Existing `true_lich` alias `b6b0399039dbdbf43bf8946f7e686469` in UnavailableFlags. | Preserve the authored opening restriction; do not equate every earlier Lich choice with this completed transformation. |
| Authored closure | `arsinoe.closed` plus the relationship ClosedFlag. | Preserve closure; native ceremony completion must not clear or create it. |

The verified native ConditionsHolder `c4fa13c72fc350d4bae7431242eb095a` contains the single NOT Playing VictimsRevived condition.
The current aliases implement that condition without requiring a new arbitrary-ConditionsHolder evaluator.
The native capital etude controls the same spawner hidden by the default-actor etude and depends on the native noncombat role.
The live check independently rejects player combat and a missing or unusable actor.

`NativeContact.IsAvailable` requires a loaded area, a conscious Commander and exactly one matching loaded actor.
It rejects destroyed, disposing, suppressed, out-of-game, unconscious, dead, finally dead and hostile actors.
It does not call a speaker accessor that may spawn or restore someone.
`Rules.ContactAvailable` checks the live contact, chapter, area, required native role and relationship unavailability again during the book.
The injected answer and queued start also recheck current availability.
The flag-free contact-lost exit closes an interrupted scene without completing it.

These checks do not evaluate every arbitrary cutscene, a minimum physical distance or an exact spawner-instance identity.
The previous review already records the scheduling interval between a guarded cue's selection and its execution.
Those are remaining runtime verification limits, not evidence that the current opening needs a new resurrection system or universal quest-condition interpreter before a development-stage integration.

## Concrete interruption and replay blocker

`Main.RecordProgress` persists selected choice flags before the scene is complete.
The contact-lost exit intentionally does not roll those flags back.
An incomplete scene can then be opened again from its beginning after contact returns.

I reproduced the following with the actual source scene dictionaries and choice conditions, using the engine's persistent-effect semantics:

1. Complete the first two opening scenes through their actual choices.
2. In `arsinoe_roofs`, visit `start`, `roof`, `view`, `leaving`, `tell`, then `interest`.
3. Choose the personal-interest answer, which sets `arsinoe.courting` and goes to `touch`.
4. Lose contact before selecting `touch`'s terminal answer. The contact-lost exit leaves `arsinoe.courting` set, while `arsinoe.roof_shared` and scene completion remain unset.
5. Restore valid contact and replay the unfinished roof scene, choosing friendship and completing it.
6. Continue the following scene and reach `arsinoe_hours_of_her_own/evening`.

The state now contains both `arsinoe.courting` and `arsinoe.friendship`.
The final node exposes both `romance` and `friend_end` because each tests only its own required flag.
The romance branch then exposes the kiss choice despite the later explicit friendship selection.
This is an authored-graph reproduction, not a claim to have induced the interruption in Unity.
The root received the exact path for a focused production-rules test.

The current `ArsinoeOpeningTests` exhausts complete fresh walks and asserts exactly one pace flag at their ends.
It does not exercise partial choice effects, contact loss and a different choice on replay.
The same persistence pattern can accumulate other mutually exclusive opening outcomes, such as fantasy versus street-print choices, so the repair should inspect those branch commits as well.

The necessary behavioral contract is simple: replay must not create incompatible histories, and a completed friendship path must not inherit romantic access from an interrupted earlier attempt.
A repair may commit mutually exclusive decisions only when their branch successfully finishes, or deliberately preserve a recorded decision on resumed play with clear appropriate text.
The parent owns the implementation choice and shared engine policy.
Merely adding a friendship forbid to the final kiss does not repair contradictory earlier commercial and relationship histories.
No additional native GUID or mythic exclusion solves this problem.

## What does not block an opening-only development export

The full route still needs later campaign development, sustained personal conflict, endings, the required per-character depth and a complete art set.
Those should remain labeled incomplete instead of being treated as reasons that no playable opening may enter the development build.
This contribution does not award full commitment.

Lann's wedding, Seelah's stolen souls and Arueshalae's dream question have actual quest contexts.
The opening neither claims those quests complete nor awards their outcomes.
Optional contextual responses should use verified history when authored; they do not justify inventing blanket unavailability throughout every related quest.
The native VictimsRevived suppression is a specific contact condition and already has the necessary guard.

Lawful-neutral alignment and Abadar worship alone do not supply an exact native Demon, Devil, Aeon, Angel or Trickster romance predicate.
Do not treat the conditional native approval cue as unconditional approval of those paths, but do not invent a native prohibition from alignment either.
For this scoped opening, retain the evidenced contact restrictions and the explicit Swarm/true-Lich policy.
Character-specific refusals, later moral consequences and the user's attainable Trickster restoration remain required full-route work.
Ordinary healthy contact on Trickster is distinct from restoring an absent, dead or hostile Arsinoe.
The current module implements the former only when the usual predicates hold and does not implement the latter.

Other romances and ToyBox settings are not changed by the opening.
That source fact does not certify runtime coexistence.
The printer, roof and reading outings remain narrated settings rather than newly placed world actors.

## Concrete promotion sequence

Fix and verify the interrupted replay case before promotion.
Then add the module's relationship, both ordinary etude aliases and five scene objects to the current expansion assembly.
Keep the existing contact predicates and typed vendor answer-list binding intact.
Run the focused opening paths and contact predicates against that combined payload, including the new interrupted histories, and run the corresponding typed-binding and managed-construction checks.
Retain the stage's honest incomplete-route label and update the stale unexported/integration metadata to describe what was actually checked.
Keep Unity interruption, save round trips, native dice execution, dialogue presentation, finished art and ToyBox verification explicitly separate.

After the concrete replay defect is fixed and the current stage passes its applicable checks, no additional source-level native guard identified in this audit prevents adding the opening to the incomplete development export.

## Relationship-pace correction inspected

The root reproduced the pace failure with actual `Program.Walk` partial snapshots, contact loss and restoration, then replay.
The failing assertion was `Interrupted Arsinoe roof replay accumulates conflicting relationship choices.`
That production-rules reproduction supplements my read-only graph trace; it is not a Unity session.

I inspected corrected source SHA256 `9027418BE7B925108D00FFDE54D0BC72AD650680C34CD3EDD8C690487B8613D0`.
All three pace flags moved from the `interest` choices to the corresponding `touch`, `slow` or `friend` terminal choice, alongside `roof_shared`.
An interrupted branch no longer commits a pace before the completion action, and a completed scene cannot ordinarily restart.
The prose, node IDs and choice indices are preserved.
This corrects the reported friendship-versus-courtship defect for the never-promoted opening; no installed pre-fix save migration is needed for this source change.

The commercial instance still needs the same attention at this revision.
`arsinoe_printers_view` sets `print_fantasy` or `print_street` before the later completion answer.
Interrupting and replaying the other decision can therefore leave both flags.
`arsinoe_first_impression/start` then offers two identical look-at-print answers leading to incompatible results: one says the street has not yet been cut, while the other displays the printed street.
This is an actual callback contradiction, not merely unused extra flags.
The root received the exact nodes for a focused reproduction and repair before promotion.

## Commercial replay correction inspected

The root reproduced the second defect with the actual rules test and the failing assertion `Interrupted printer replay records contradictory commissions.`
I inspected the repair in source SHA256 `29967C5466D0DE8D4E3CF059F3D0C5B4706029A71D245F82E42038275CF449C7`.
Relative to the preceding pace repair, the two original commercial choices gain opposing flag forbids.
The fantasy choice is unavailable once `print_street` exists, and the street choice is unavailable once `print_fantasy` exists.
The originally issued commission therefore remains the selectable decision on replay.
No existing node, choice index, prose or outcome is removed.

This differs appropriately from the pace repair: the commercial order is retained once issued, while the personal pace commits with successful completion of its branch.
For a valid newly played history, interruption can no longer create both commission flags or expose contradictory print callbacks.
The never-promoted opening does not require migration for installed pre-fix dual-commission saves.
The added focused test captures partial snapshots at both commission branches, removes and restores contact, and checks every replayed completion for exactly one commission result.

Both concrete source-level integration findings in this report are now resolved.
Promotion remains conditional on the parent's current combined-stage checks and honest incomplete-route status, rather than on completion of the entire Arsinoe campaign.
