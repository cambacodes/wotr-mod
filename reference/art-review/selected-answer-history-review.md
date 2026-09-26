# Selected-answer history: native semantics and integration review

Reading `player.Dialog.SelectedAnswers.Contains(nativeAnswer)` matches the installed game's own global answer-history condition.
It is appropriate for identifying that the player selected Konomi's rank-six dismissal answer, separately from her present availability.
It does not prove that the answer's subsequent effects or dialogue finish actions completed.

## Independently verified native condition

I directly decompiled `Kingmaker.Designers.EventConditionActionSystem.Conditions.AnswerSelected` from the installed `Wrath_Data/Managed/Assembly-CSharp.dll` with the local ILSpy tool.
Its `Answer` property resolves the private `BlueprintAnswerReference m_Answer` through `m_Answer?.Get()`.
Its condition is exactly:

```csharp
if (!CurrentDialog)
    return Game.Instance.Player.Dialog.SelectedAnswers.Contains(Answer);
return Game.Instance.DialogController.LocalSelectedAnswers.Contains(Answer);
```

The native tooltip likewise says the default checks whole-game history while `CurrentDialog` limits the check to the current dialog instance.
The existing extracted `reference/game-BlueprintAnswer.cs` also uses the global set when deciding whether that answer was previously selected.
This supports typed resolution to the actual cached native `BlueprintAnswer` and the same `Contains` operation, without creating replacement answer objects or copying native selection actions.

`reference/canon-review/konomi-availability-review.md` identifies the rank-six dismissal answer as `73c5728c4c6658344bedcc1b666e598c`.
The native dialogue's finish condition and save upgrader both use that selected-answer history to complete the ordinary officer presence etude.
This is a specific decision marker and is more precise than treating every absent officer as dismissed.

## Persistence and read hazards

`reference/art-review/DialogState.cs` declares `[JsonObject] DialogState` with `[JsonProperty] public readonly HashSet<BlueprintAnswer> SelectedAnswers` initialized to an empty set.
`reference/game-Player.cs` declares `[JsonProperty] private readonly DialogState m_Dialog = new DialogState()` and exposes it through `public DialogState Dialog => m_Dialog`.
Those attributes establish structural participation in the native player save model.
They are not an independently performed live save/load round trip.

`reference/game-DialogController.cs`, `SelectAnswer`, validates the answer and then adds it to the global history before calling `answer.OnSelect.Run()`.
It also records local history, then applies subsequent answer effects and advances or stops the dialogue.
Therefore an interrupted or failed effect can leave a selected marker without completed political changes or the final presence-etude completion.
History should be named and interpreted as a selected decision, not a transaction-completion receipt.
Current presence, actor availability and any future restoration eligibility need their own checks.
The history set records whether selection occurred, not how many times it occurred or when.
It should not create a new relationship delay timestamp.

The read should use the current `Game.Instance.Player.Dialog` each snapshot.
Caching blueprint references is consistent with native condition resolution; caching the selection result across player loads is not.
An empty or missing marker means the current history does not record that selection, not proof of an opposite decision or proof that the officer is available.
The native game also has an import path that can replace SelectedAnswers from another player state, as shown in `reference/game-Game.cs`.
Modified or imported history can therefore diverge from current actor state even without a defect in the addon reader.

Aliases should be resolved as `BlueprintAnswer`, not `BlueprintAnswerBase`, during integration preflight so a wrong-type GUID fails clearly.
The story field should default to an empty dictionary so older story files without the field remain readable.
Read-only native history aliases must not overlap addon scene or choice-effect flag names, because the shared snapshot flag namespace otherwise admits a second source for the same condition.
No native answer should be marked selected, replayed, or removed by this feature.

## Implementation review status

The parent's proposed `Story.SelectedAnswers` alias-to-GUID reader is consistent with these native semantics.
Production changes were not present at the initial review point; the subsequent review below covers the now-implemented reader and invitation.
No game state was changed, and no restoration or full-route approval is claimed.

## Implemented reader and invitation review

No blocking correctness defect was found for the current Konomi bindings and the bounded invitation scene.
`Story.SelectedAnswers` and `Story.CompletedEtudes` default to empty dictionaries, preserving omission compatibility for older stories.
Build resolves the selected-answer values through `Get<BlueprintAnswer>` and completed-etude values through `Get<BlueprintEtude>` before constructing new graph objects.
Only typed blueprint references are retained in these dictionaries.
`Main.State()` reads the current player's completed etudes separately with `EtudeIsCompleted`, then passes the current player's `DialogState` into `ReadDialogHistory`.
That helper uses native `SelectedAnswers.Contains` and adds the alias to the newly created snapshot without writing the native history collection.
No completion timestamp is invented for either native fact.

The mappings are the exact dismissal answer `73c5728c4c6658344bedcc1b666e598c` and completed officer etude `b5f301fbc4c44535a6309d610d5bd28a`.
The separate aliases are `konomi.dismissed` and `konomi.office_completed`.
Requiring both avoids using the early selection marker alone as evidence that the officer state completed.
It still does not certify every unrelated native political side effect or present actor existence, and the implementation does not claim either.

The optional remote `konomi.fate_post` scene requires Trickster, the selected dismissal and completed officer state.
It forbids current ordinary presence, an inhuman Commander and the existing farewell, while normal relationship closure still blocks through the shared availability predicate.
It is limited to Drezen in chapters 3 or 5 and does not depend on the hidden actor's native answer list.
Its choice branches distinguish an established lover from a first personal invitation.
The final send sets `konomi.post_sent`, and branch decisions also set `konomi.post_argument` or `konomi.post_slot`.
Normal scene completion additionally records the completion ID, timestamps and ordinary relationship journal/start progress.
Therefore the exact implementation should not be described as writing literally only one flag.
None of these effects changes native selection history, completes or restarts a native etude, restores Konomi's actor, grants presence, or grants commitment.
Ordinary meetings remain blocked after the invitation is sent.

Validation rejects malformed GUIDs, collisions with other configured native sources, addon scene IDs, authored choice effects, relationship state flags and the `hour.` namespace for the two new binding types.
This prevents the current aliases from being forged through authored choice writes.
The initial review found that synthetic `State()` names were not reserved; the final source now fixes that gap in both new binding validators.
A shared `derivedFlags` set contains `loss`, `ascended`, `inhuman`, `chapter_one`, `chapter_later` and each configured `revive.<id>.available` name.
Both validators reject these names alongside the previously rejected collisions.
I inspected the final source and the focused test that attempts an `inhuman` selected-answer alias and requires the appropriate validation error.
The reported gap is resolved for the current derived-state vocabulary.
Future additions to that vocabulary should maintain this reservation set.

The managed test invokes the actual production `ReadDialogHistory` with a real installed `DialogState`, verifies absent and unrelated answers do not satisfy a binding, adds the matching typed answer and observes the alias, then removes it and checks a fresh snapshot.
It also checks that reading preserves the history collection and unrelated choice.
These are meaningful tests of the extracted reader with actual game types; they do not perform a native player save/load or run the full `Main.State()` etude evaluation.
Pure rules tests cover missing prerequisite facts, each blocker, lover/first-invitation selection, postponement versus sending, preservation of another relationship, one-time completion and continued ordinary-meeting suppression.
Alias-validation tests exercise authored-effect forgery, cross-source collisions, timestamp aliases and malformed GUIDs.
The owner reports 60,675 passing rule assertions; this audit inspected the code and tests without independently rerunning that suite.
The bounded reader and invitation are coherent under the stated conditions, with actual delivery, acceptance and restoration still pending separate implementation and evidence.
