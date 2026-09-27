# Nocticula withdrawal independent review

Verdict: the closure implementation passes the inspected static checks, but the repair does not pass the strict above-90 gate in every applicable dimension.
The shared withdrawal wording fails at the final celebration, and the addon interface describes undertaking closure as the end of the relationship.
This is a scoped review, not approval of the full route.

## Reviewed evidence

- `storylines/nocticula_continuation.py`, SHA-256 `99AF5CE02EFC0D7A8A196331190076DD1F173A5FA5D279D8028609809D85C128`.
- `tests/NocticulaContinuationTests.cs`, SHA-256 `A37D28E3FF5CEC5C797AEC8870169AB8265AD06A47279B937E84CC7A0F3D2C30`.
- `development/Story.json`, SHA-256 `E2C233C8429E956F56AA602EFF1C706EE1FB4B3B78CC1AD25C8DC21D39068C60`.
- `nocticula-withdrawal-development.md`, the prior independent route review, and current `src/Story.cs` and `src/Main.cs` closure and answer handling.

I inspected the new initial refusal, the shared response injected into all fifteen subsequent visits, its entry choices, the surrounding early and late plot phases, and all ending prerequisites.
The source and export contained the same twenty-four Nocticula scene objects.

## What passes

`noct.unlit_quay/offer -> decline_undertaking` now gives a genuine permanent refusal without accepting the undertaking or choosing the intimate postponement.
Nocticula's disappointment remains sharp and personal.
Her complaint that the Commander can ration curiosity suits an interested manipulator whose invitation has failed, while her refusal to renegotiate the Worldwound preserves her larger priorities.
She is neither delighted by rejection nor suddenly punitive merely to prove that she is dangerous.

The early shared withdrawal reply also works well.
The interruption, sharpened gaze, complaint about arranging the evening, and abrupt termination of the dream let her dislike the answer without removing the player's choice.
She controls the dream's ending and does not reward withdrawal with affection.
The promise concerns future harbor invitations and the unchanged terms of the earlier bargain, not guaranteed future parent-romance scenes or a successful native ending.

Every closure terminal sets only `noct.closed` and exactly one addon reason flag.
No native or parent binding is written, no revival runs, and no `noct.complete` credit is awarded.
All sixteen visit definitions forbid `noct.closed`.
All eight supplementary endings require `noct.complete`, which these paths cannot earn.
Existing completed scene history and unrelated relationship flags survive.

Closure occurs when the player confirms the sole terminal choice after reading Nocticula's response.
The first refusal or withdrawal selection enters that response without setting the flags yet.
There is no continuation branch from the response back into the undertaking.
This is a two-step authored exit, not closure on the first click.

## Changes required

### The final withdrawal misstates the completed work

The helper `s()` at source lines 38-50 injects the same choice and response into every later scene.
At `noct.second_door/start`, the Commander can say, "Find someone else to finish it."
By this point the passenger crossing, hearing, last buyer and subsequent accounting have already occurred.
The opening is a celebration in the finished room, and its later `future` node asks whether they want further private company.
Nocticula's stock response about selecting her next adviser treats this final invitation as an abandoned unfinished assignment.
The text does not identify any remaining task for that replacement adviser.

Use a late-phase departure choice and reply that acknowledge the completed harbor work while refusing further addon meetings.
The existing `limited` branch remains a separate valid answer: it completes this final evening and declines a larger promise.
If an immediate departure intentionally withholds the final recollection flag, describe that as leaving before their final conversation, not undoing earlier work.

`noct.what_she_keeps/start` also needs late-phase wording.
Ossin has already withdrawn his offer there, and the scene turns toward the results of the investigation and their ambitions.
An unfinished-operation complaint is weaker than an explicit refusal to remain involved in whatever follows.

At `noct.her_own_face/start`, withdrawing from the harbor while she explicitly offers an evening without accounts is abrupt but possible.
It is not a factual contradiction: the Commander can introduce that subject.
A brief acknowledgment that the Commander has chosen to discuss work during a private invitation would make her reaction less interchangeable.

### The interface overstates what has ended

`src/Main.cs:840` displays "This relationship has ended." whenever the relationship's `ClosedFlag` is set.
The Nocticula relationship maps that field to `noct.closed`.
After this undertaking-only withdrawal, that label conflicts with both the dialogue and the preserved parent state.
The heading "The uncounted shore" gives context, but does not make the categorical relationship claim accurate.

Provide Nocticula closure text that says the harbor undertaking has ended and leaves the earlier bargain under its existing terms.
No new parent breakup or reconciliation behavior is needed to repair this wording.
This finding comes from the rendering source; I did not inspect the label in a running game.

## Scoped scores

| Dimension | Score | Result |
|---|---:|---|
| Initial refusal voice and agency | 95 | Pass |
| Early withdrawal voice and non-agreeability | 93 | Pass |
| Consistency of reused response across plot phases | 79 | Fail |
| Native and parent state preservation | 96 | Static pass |
| Blocking subsequent addon visits and recollections | 96 | Static pass |
| Accuracy of player-facing closure scope | 84 | Fail |

These scores apply only to this repair and the inspected evidence.
The previous full-route length and acquisition failures remain unresolved and were not rescored.

## Verification and limits

I reran the existing Release rules executable with the bundled .NET SDK against the pinned development export using `dotnet run --no-build --project tests/RulesTests.csproj -c Release -- development/Story.json`.
It passed 28,662,926 assertions.
I did not rebuild that executable in this review.
I separately compared all twenty-four imported source scene objects against the export and checked all sixteen closure terminal effects and all ending completion requirements in Python.

The C# traversal checks all thirty-two optional-history fixtures, refusal and withdrawal outcomes, parent-state preservation, future visit blocking, and absence of completed recollections.
It does not judge whether an adviser still has work to finish at the final celebration or whether the interface describes the result accurately.
Unity execution, save persistence, native parent behavior after withdrawal, rendered UI and ToyBox compatibility remain untested here.
