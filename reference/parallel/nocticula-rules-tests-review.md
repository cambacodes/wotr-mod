# Nocticula Rules test independent review

Date: 2026-09-26.
Initial verdict: strengthen the test before shared registration.
The current manuscript is not the source of either regression demonstrated below.
The gaps are in the new test's ability to detect those regressions if introduced later.

## Scope and independence

I reviewed root-authored tests/NocticulaContinuationTests.cs, SHA256 `913C905D6B5135349238083920353404FA52A41A31E8A98BC2CFE913985F6B6B`.
I also read the Rules implementation, Program.Copy, Program.Walk, and reference/parallel/nocticula-rules-integration-handoff.md.
The tested candidate is `C:/Users/Z/AppData/Local/Temp/nocticula-rules-root-tnbje6oj/Revised.json`, SHA256 `57CF856A23048192AAD5A8E970BAB42EA729C6FBE9828DF10BADD23E7DCB20FC`.
It contains the revised manuscript pinned at `9CDD2490621BCE273D3E36E7977208EAFBE41173E0D80ED0BCA8A42EF89E6E74`.
I authored that manuscript; this report independently reviews another author's test code and cannot independently approve my prose or plot.
The different literary reviewer retains that responsibility.

I built an isolated copy of the root test entry point and project at `C:/Users/Z/AppData/Local/Temp/nocticula-tests-audit-v4khtbqw/`.
No production source, shared tests, shared export, or installed assets were edited.
The baseline candidate independently passed 569,185 focused assertions.
These execute the actual C# Rules implementation, not Unity or the native game condition engine.

## Confirmed missing assertions

### Postponement can silently unlock the campaign

The suite walks the postponed invitation but discards outcomes without the current scene marker after checking native-history preservation and physical-contact absence.
It does not assert the authored progress flags or subsequent eligibility of that aborted outcome.

In isolated `Abort-mutant.json`, I changed only noct.unlit_quay/later's terminal Abort choice to set noct.invitation_accepted and noct.started.
The unchanged test and Rules.Validate still passed 569,185 assertions.
That mutant would unlock noct.sixth_passenger because it requires invitation_accepted, even though the player explicitly postponed the undertaking.
The real candidate has an empty Set on this choice and is correct.

Before registration, assert that postponement preserves the pre-entry flags and times, keeps the first invitation available, and leaves the second visit unavailable.
This should use the actually walked aborted outcome.

### Selected ending pages are never executed

The outcome-mask loop checks ending availability and precedence but does not walk the selected page.
The native effect-write restriction also applies only to visits.

In isolated `Ending-mutant.json`, I changed only noct.ending_company's Continue choice to set noct.dead.
The unchanged test and Rules.Validate still passed 569,185 assertions.
The real ending has no such effect.

Before registration, apply effect isolation to all twenty-four scenes and walk each selected ending from an earned witness.
Verify that completing a recollection adds only its own completion marker and timestamp, preserves the existing snapshot, and prevents that page from repeating.
Do not assume a later generic walker will provide this coverage if integration may mark route scenes as already covered.

Both mutation fixtures and the isolated executable are retained beside this review's temporary project.
Root received the findings while this review was in progress.

## Pruning assessment

For this exact frozen campaign, merging by later-read flags is sound.
The future set retains later scene and choice requirements and prohibitions, final decision flags, every bound native flag, and all initial flags.
An actually played snapshot is retained rather than constructing a synthetic combination.
All continuing histories reach each visit in the same order with the same fixed interval.
No effect flag is written by more than one scene, so equal retained flags do not conceal different acquisition times in this candidate.
Chapter, area, and physical-contact sets are constant across this traversal.

The helper is not a general proof for arbitrary future scene schemas.
Reads omits ForbidOverrides values and relationship-level policy flags, and the merge key omits times, chapter, area, and contacts.
The current source has no override gates, no time-changing choices, no actor effects, and no variable-chapter branches; its relevant relationship exclusions are also explicit scene prohibitions or held initial flags.
If those assumptions change, the merge key or an explicit invariant check must change with them.

## What the suite establishes

Program.Walk explores every currently selectable choice and both skill-check targets without choosing an artificial best outcome.
The suite reaches every living node across its thirty-two seeded histories and preserves an earned witness for each of the three final choices.
It checks delay expiry, completed-visit nonrepetition, missing required evidence, all current explicit blockers, area restriction, and loss of essential parent evidence during a dream.
It also checks that no physical contact or resurrection is manufactured.

The ending selectors are correctly tested for death before changed Commander, changed Commander before ascension, and ascension before sacrifice across all sixteen outcome masks.
The ordinary final decisions are mutually exclusive in these witnesses.
The Aeon recollection is evaluated as a separate owner group; its simultaneous availability in this data probe does not mean both native ending sequences execute in one playthrough.
Removing complete blocks all eight supplemental recollections.

## Remaining coverage limits

The suite records node coverage, not an explicit inventory of reached choice edges.
A newly unreachable choice leading to an already reached node could escape that coverage assertion.
It checks the wrong area but does not explicitly test adjacent chapters or a mid-conversation area change.
Those are useful focused additions if this becomes the dedicated replacement for generic scene checks.

Parent acceptance and the five optional history bits are seeded fixtures.
Some combinations are deliberately broader than demonstrated native histories, such as the Socothbenoth disclosure bit without Trickster.
This tests predicate behavior; it does not prove those combinations can be acquired together in the game.
The extra committed relationship markers test their preservation, not a complete concurrent campaign or installed ToyBox configuration.
Skill checks follow both results but do not execute dice, character statistics, or the native skill-check UI.

The handoff I read still pins the intermediate manuscript in its main probe section.
Root separately supplied the revised candidate hash and rerun result, which I independently reproduced above.
Update the checkpoint to distinguish those runs before presenting it as a final integration record.

This report does not approve dialogue quality, native ending insertion/order, parent show-once actions, actual rest-event delivery, art, save migration, or route release.

## Independent verification of root's corrections

Revised test SHA256: `8FA723844A0A9186506070A7F6FD42E714B6EF5E32B063D2802D92022FDE658B`.
Verdict for this revision: the two demonstrated gaps are corrected, and the focused suite is suitable for registration within the limitations above.
This supersedes the initial test-registration objection, not the separate manuscript review.

I rebuilt the isolated project against the revised test and reran the same unchanged fixtures.

| Input | Independent result |
| --- | --- |
| Frozen Revised.json candidate | Exit 0; 569,585 focused assertions passed. |
| Abort-mutant.json | Exit 1 at `Postponing Nocticula changes acceptance or history.` |
| Ending-mutant.json | Exit 1 at `Nocticula ending changes history beyond its own completion marker.` |

The new postponement branch compares exact flags and times with the actual entry snapshot, verifies retry eligibility, advances the prospective next scene's delay, and verifies that scene remains blocked.
The ending loop now walks both the selected ordinary page and the separately selected Aeon page, allowing only their own completion marker and timestamp before checking nonrepetition.
All eight ending IDs are selected under the existing final witnesses and outcome masks.
The exact snapshot comparison detects additional authored flags and timestamps as well as native state changes.
Program.Walk treats setting an already-present flag as a no-op, so that comparison is an outcome-state guarantee rather than a prohibition on every redundant Set declaration.

The added eligible-choice index inventory addresses the prior gap where an unreachable choice could share a destination with another reachable choice.
Because Program.Walk enumerates every eligible choice and both check targets, recording eligibility during its callback is evidence of traversal under this implementation.
It does not claim an actual dice roll or native UI interaction.

The static no-Revive assertion remains visit-scoped.
Program.Walk itself does not execute Revive, but Rules.Validate already rejects a lone ending Revive unless the scene declares matching recovery metadata and a matching relationship revival registration.
There is no Nocticula revival registration in the current candidate.
An all-scenes no-Revive assertion would be a useful cheap invariant if that scope later expands; this is not a third demonstrated passing regression or a blocker for the reviewed candidate.

The current hard requirement against merely narrated promised gameplay remains a separate content-and-implementation question.
These tests establish actual authored flag gates, delays, choices, and ending selection.
They do not transform narration about agents, money, injuries, or research into native quest effects or a playable physical encounter.
Whether a promised consequence needs additional implementation must be judged against the actual scene and user-facing claim, not inferred from this assertion count.

## Final test scope pin

Final reviewed test SHA256: `71A6C253CC2C16FEA7CD58B4FAD53E0510FB1D0048EFF2E2A7F6D511CC013677`.
I inspected the final incremental changes after the independently executed revision above.
The single no-revival and no-native-effect invariant now covers all twenty-four scenes, including endings.
Each living scene also rejects contact after leaving its area and rejects both entry and continuing contact in chapters 4 and 6.
The assertions use separate copied snapshots and leave the valid chapter-5 witness intact.
These additions address the remaining cheap scope invariants identified in this review without changing the traversal or pruning algorithm.

Root reports that this final test revision passes 569,618 focused assertions on the same frozen candidate.
I did not repeat the baseline or mutation executions for this small final change; the independent execution evidence above remains explicitly pinned to the preceding test revision.
The widened invariant may reject the native-effect mutant earlier with a different message, which is acceptable.
Final bounded verdict: suitable for registration as the dedicated Nocticula authored Rules suite.
No literary approval, native acquisition proof, gameplay-delivery approval, or release approval is implied.
