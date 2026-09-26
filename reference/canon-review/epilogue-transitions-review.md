# Epilogue transitions independent review

The corrected builder preserves authored ending branches instead of replacing every ending page with an unconditional exit.
The final inspected source is suitable for bounded development integration.
No remaining source-level blocker was identified for the current ending graphs.
Actual native sequence execution and saves taken inside an older epilogue remain separate verification cases.

## Reproduction and reviewed revisions

The parent reproduced the defect through actual managed blueprint construction before changing the source.
The failure was `Wrong choice count: seelah.ending_together.history`.
That is evidence of missing generated answers, not merely a literary concern about how the authored graph should read.
The previous epilogue special case supplied one Continue answer regardless of the node's conditional choices and Next destinations.
Consequently a valid source graph could pass rules traversal while its built ending skipped the intended history distinction.

| File | Final inspected SHA256 |
| --- | --- |
| `src/Main.cs` | `F1AE3AECD57BAD6DADF2E25F11D18D3756802E9D3733E74A06F72A10E2F0DFEA` |
| `managed-tests/Program.cs` | `34178AAD7502FFBF4FDA6DC17FD5AAE027AA3651C8B4CB881C7B6BDF37BEA4FD` |

I read BuildScene, epilogue sequence attachment, RouteCondition, RouteAction and RecordProgress, along with the expanded managed checks.
I also inspected the saved native DialogController decompilation for answer selection and cue-sequence continuation.
Only this report was written.

## Builder behavior

A page with one plain terminal Continue still receives the existing `answer.<scene>.<node>.continue` identity.
The special case requires no Next, check, conditions, effects, abort or revival.
It keeps an empty OnSelect action list and empty NextCue list.
This preserves the simple ending behavior and identifiers where the page truly has no authored transition.

Every other ending page uses the ordinary answer builder.
Answers retain their source indices, text, Requires and Forbids.
Both visibility and selection use the actual Choice condition, and the action checks the choice again before applying effects.
Next points to the authored local page rather than an unconditional terminal exit.
This directly repairs the missing Seelah history choices and analogous Jerribeth ending branches.

The action's Complete reference is null for all ending choices, including terminal authored answers.
The builder therefore does not mark an ending scene completed or add its scene-completion timestamp when advancing through it.
An explicitly authored Set effect would still run through RecordProgress.
The inspected 225-scene main payload contains 46 ending scenes and no ending Set effects or skill checks, so the current ending transitions do not change relationship flags.
RecordProgress can still perform its existing journal synchronization; this fix does not invent a separate epilogue journal policy.

During review I identified that the first version of the plain-ending discriminator omitted `Check == null`.
The parent added that condition to both builder and test.
Rules.Validate already rejects epilogue skill checks, so this was a defensive exactness correction rather than another reachable defect in valid current content.

## Native sequence and condition behavior

Only each ending's first authored page is appended to the appropriate native or parent-mod sequence.
The internal pages are reached through the answers' NextCue references.
They are not separately appended as unconditional sequence entries.
Native sequence entries and their reference objects remain in their original order before the appended content.

The inspected native answer-selection code first asks `answer.NextCue.Select()` for the next cue.
When it returns null and a cue sequence is active, the controller polls the next sequence cue, or the sequence exit after exhaustion.
Thus an authored internal Next stays within the ending, while its terminal answer resumes the surrounding sequence.
An empty NextCue on the retained legacy terminal answer is consistent with that mechanism.

Every generated epilogue page retains the scene-level availability condition.
Choice conditions then select the appropriate internal branch.
Current ending choices do not mutate their own scene eligibility, so that repeated page condition does not invalidate the intended current paths.
Future authored ending effects that change a required or forbidden scene flag would need special review: the subsequent page could fail scene availability and cause native selection to advance the outer sequence instead.
That is a concrete consequence of the existing page gating, not a reason to remove eligibility checks now.

The actual native game may also supply its own epilogue context and timing.
Inspecting the selection code and generated references does not establish that every sequence transition renders correctly in Unity or that every conditional branch has a valid native endgame snapshot.

## Tests and save compatibility

The expanded managed test inspects every nontrivial ending answer instead of skipping all epilogues.
It verifies answer count, visibility and selection guards, action references and owners, effect linkage, NextCue GUIDs and the absence of scene completion.
Plain terminal endings have explicit checks for their stable `.continue` GUID, lack of effects and empty NextCue.
Existing checks preserve native sequence references and confirm a second Build does not duplicate entries.

The parent reports 26,239 managed assertions over 7,870 generated blueprints for the 225-scene payload before the defensive discriminator addition.
Those results are parent-executed evidence, not a suite I reran.
The final rebuild and tests remain the parent's verification responsibility.

Page and cue identities continue to derive from the same scene and node IDs.
Plain terminal answer IDs remain stable.
However, a page that formerly received an incorrect `.continue` answer now receives authored indexed answers such as `.0` and `.1`.
That is an intentional replacement of broken generated behavior; it is not proof that a save already inside the old page or storing that old answer reference can resume unchanged.
A release claiming compatibility with such saves must test them or explicitly preserve obsolete registered references as needed.
The present review does not require unneeded migration machinery for a development-only graph, but it does not label every historical save safe.

The fix does not replay endings already passed, synthesize missing relationship history or validate the prose of every route.
The StartedDialogs adapter and its start-versus-completion semantics are separate from this repair.
This verdict covers the corrected construction and inspected current graphs, with full runtime and save claims reserved for their own checks.

## Final parent verification

The parent reports that the final defensive version passed managed construction on the 227-scene Konomi stage with 26,703 assertions and 7,981 generated blueprints.
The stage SHA256 is `B8E0788E85EB1A016C4455B1AA10465449D0FD4A5BB83AE3F618C6E9D5F71514`.
The tested DLL SHA256 is `F81C0C7BD279C832F73B01CD5F5E44B6C37570F675B8873540C7C7D2B30188F4`.
The parent verified that all 225 main scene objects were unchanged within that stage.
These are final parent-executed managed results, including the exact plain-terminal discriminator, rather than an independent rerun by this reviewer.
They close the pending managed-build checkpoint in this report without extending the verdict to Unity sequence playback or historical in-progress saves.
