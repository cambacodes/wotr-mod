# Nocticula audience lifecycle probe

Inspected 2026-09-27.
The existing queued-book insertion cannot return the player to the original audience by the current graph.
I recommend a narrow opt-in inline native-cue branch, with terminal answers returning to the existing audience cue.
This avoids ending and restarting the native dialog, replaying its startup or copying its reward and teleport actions.
The recommendation is supported by native blueprint and freshly decompiled controller behavior, not an executed Unity session.

## Reproduction and evidence

I read the installed `blueprints.zip` and freshly decompiled `Kingmaker.Controllers.Dialog.DialogController` and `Kingmaker.DialogSystem.DialogSpeaker` from the installed game assembly.
The repository `tools/ilspycmd.exe` initially failed because its runtime was not on the environment path.
Setting `DOTNET_ROOT=C:/Users/Z/AppData/Local/RanRomanceTools/dotnet` allowed both selective decompilations to complete.
No runtime was installed and no production file changed.

| Evidence | SHA256 |
| --- | --- |
| Installed Wrath_Data/Managed/Assembly-CSharp.dll | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |
| .codex/tmp/nocticula-dialogcontroller.cs | `53C6614BD865E5E559017F36BA24B9CE1923A28BF669EBA0F8ED1A88F4736F52` |
| src/Main.cs | `6313F97C7856932AB9055E773065FA5926E27DBEB7A6EA05CDE5E170E46245E4` |

Standalone probe `.codex/tmp/nocticula-audience-probe.py` passed against the actual native JSON and fresh decompilation.
It verifies the return cue's empty actions and repeatability, disclosure/reward/departure edges, native action identities, and selection-before-stop ordering.
Its printed old/new traces are a graph replay, not invocation of `DialogController`.
This distinction matters: the probe does not prove that a player can click through a new implementation in the game.

## Actual failure ordering

`Main.InitializeAnswer` initializes an empty `NextCue`.
The inserted entry answer sets `OnSelect` to `RouteAction { Start = scene }` but does not replace that empty continuation.
`RouteAction.RunAction` checks availability and calls `Queue`, recording an in-memory pending scene, player reference and frame delay.

Native `DialogController.SelectAnswer(BlueprintAnswer, UnitEntityData)` records the selected answer, selects the acting unit, runs `answer.OnSelect.Run()`, applies alignment/experience, then calls `SelectNextCue(answer)`.
An empty selection calls `StopDialog()` before the eventual scheduled cue processing.
`StopDialog` schedules UI disposal, clears the current dialog and invokes its `FinishActions`.
`Clear` sets `Dialog=null`, `CurrentCue=null`, clears answers, continuation cue, sequences and local histories.
Setting `CurrentCue` away from an existing cue runs that cue's `OnStop`.

`Main` later waits for idle/loading conditions and the frame delay, clears pending state, rechecks availability and starts the addon with `StartDialogWithoutTarget`.
Nothing captures or restores the previous native cue or answer list.
The addon terminal answer then ends its own book dialog.
Its prose about returning to the audience cannot rebuild the original answers.
The native audience's finish action also stops its custom music at the premature exit.

## Verified native continuation

| Native object | GUID | Relevant behavior |
| --- | --- | --- |
| Nocticula_TricksterC5_Dialogue | `2c57f65d4b98d764d98794ae8ef9ffdd` | Common dialog; starts custom music, stops it in FinishActions |
| Cue_0006 | `20451daada07f744b9d7f3e14a37a864` | Repeatable, empty conditions, empty OnShow and OnStop |
| AnswersList_0007 | `2729c49e2bf20c64caa4f54b352e03f6` | Referenced by Cue_0006; contains native disclosure answer |
| Answer_0011 | `fd4f6c1d6397fa94db7aaf08de7dfeca` | OnSelect starts etude `8ee3df5466722b94091a3b867b33063a`; NextCue is Cue_0016 |
| Cue_0016 | `bb552fe4e21cb874fa3c98c2cc328186` | OnShow plays native cutscene; Continue is Cue_0019 |
| Cue_0019 | `19a0d2e4bae6246469852a4abf7705e6` | OnShow plays native cutscene; OnStop teleports party then hides portal |

Both cue OnShow actions name cutscene `f7b26e31f26841f3b43c052eb1d0c6b8` with native `CheckExistence=true`.
Do not collapse them into one addon action or infer that they execute identically without the cutscene controller.
The departure teleport targets `0341ea0cc1a719849b927a6a10a4d163`, with `AutoSaveMode=None`.
Its next action hides portal entity `236a7b03-a709-4f89-a2eb-e642531de492`.

Returning to Cue_0006 replays its spoken line and rebuilds the audience answers, but repeats no cue action, reward or teleport.
`PlayBasicCue` assigns `CurrentCue`, resolves `Continue`, then calls `AddAnswers` when outside a book page.
`AddAnswers` expands the selectable `BlueprintAnswersList`, then includes answers whose `CanShow()` passes.
Leave the existing native answer conditions and choices unchanged.
The player must actually select Answer_0011 and see Cue_0016 for the acquisition's genuine disclosure/reward evidence to become true.

## Minimal implementation recommendation

An opt-in `Scene.NativeReturnCue` can distinguish this physical audience insert from normal queued books.
For those scenes only, build ordinary `BlueprintCue` nodes and link the inserted entry answer directly to `scene.Nodes[0]` through `BlueprintAnswer.NextCue`.
Do not attach `RouteAction.Start`, call `Queue`, start another dialog or invoke `StopDialog` for this branch.
Keep the original Common dialog, actor context, history and FinishActions alive throughout.

The actual fields are `BlueprintCue.Answers`, a `List<BlueprintAnswerBaseReference>`, and `BlueprintCue.Continue`, a `CueSelection`.
Initialize `Conditions`, `OnShow` and `OnStop` explicitly with existing helpers.
Set `ShowOnce=false` and keep `Continue` empty for authored nodes with explicit choices.
Nonempty Continue takes precedence over ordinary choices through `AddAnswers`, so do not put the return cue there while expecting terminal choices to appear.
Use each `BlueprintAnswer.NextCue` for local transitions, and point every terminal answer to `Get<BlueprintCue>(NativeReturnCue)`.
That includes a terminal refusal and any future abort/postponement.
An empty terminal NextCue would recreate the original defect.

Reuse `InitializeAnswer`, `RouteCondition` for both ShowConditions and SelectConditions, and `RouteAction { Choice = choice, Complete = terminal && !choice.Abort ? scene : null }` for the existing authored flag writes and scene completion.
Internal checks can retain the existing `BlueprintCheck` implementation and references, though these three audience variants currently have none.
Do not gate all internal nodes on scene availability after the terminal choice has just set a flag that closes its entry.
Do not gate the native return cue on addon availability at all.
That return must remain reachable after acceptance or refusal.

Existing `RecordProgress` writes choice flags and the completed scene ID idempotently, then updates relevant objectives.
It does not create the objective at entry.
Decide objective initiation explicitly without blindly copying the queued start behavior.
The acquisition relationship's `StartedFlag` is `noct.acq.requested`, while its manuscript deliberately writes requested and seal_received only at acceptance.
The ordinary queued path writes StartedFlag before showing the first node, which would prematurely assert requested for this opening.
Inline entry should preserve the manuscript distinction rather than mark acceptance before the player makes it.
An objective can be granted at the accepted terminal or use a separate genuinely-started flag if product behavior needs an earlier journal entry.

Use stable IDs derived from scene and node IDs through the existing `New`/`GuidFor` machinery.
Give inline cues their own namespace, such as `nativecue.<scene>.<node>`, if book cue objects might otherwise coexist.
Keep answer IDs stable where there is no collision, and preserve the project's element Owner/name registration and `OnEnable` handling.
Validate that NativeReturnCue resolves before publishing the injected answer.
If the expected audience layout is absent, fail this insertion closed rather than attach an empty continuation.

`BlueprintCue.Speaker` has type `DialogSpeaker`.
Its public fields include `NoSpeaker`, `MoveCamera`, `NotRevealInFoW` and `SwitchDual`.
Its blueprint and portrait references are private serialized `m_Blueprint` and `m_SpeakerPortrait`, with read-only `Blueprint` and `SpeakerPortrait` properties.
Use the existing native Cue_0006 speaker configuration for Nocticula, without mutating that shared instance.
`new DialogSpeaker { NoSpeaker=true, MoveCamera=false }` remains suitable for neutral narration; `TurnSpeaker=false` prevents an unnecessary turn.
Do not label a Commander monologue as spoken by Nocticula merely to reuse her speaker.
If an exact player speaker is needed, use a verified native player-speaker configuration rather than guessing a writable `Blueprint` property.
Inline common-dialog presentation will not automatically use the BookEventVM per-page portrait patch, so do not claim the existing scene-art behavior carries over unchanged.

## Cancellation, saves and remaining proof

The recommended bridge removes the volatile pending scene and two-frame disposal gap from this acquisition entry.
It also avoids restarting the native dialog's FirstCue and StartActions.
Normal acceptance or refusal stays within the same native dialog until the player actually follows a native exit.
The addon must not execute native disclosure actions on the player's behalf or return directly to the reward cue.

An explicit authored cancel answer should return to Cue_0006 without writing completion or acceptance.
A real engine stop, loading another save or forced area transition is different and must not trigger an automatic replay of the native audience.
Do not persist a guessed suspended dialog and resurrect it later merely because a request flag exists.
Native save availability and restoration of the current dialog were not executed in this probe.
Stable blueprint IDs and idempotent writes are necessary but insufficient to certify save/reload behavior.

The controller exposes `DialogController(bool headlessMode)` and `SetHeadlessMode(bool)`.
Headless mode skips some UI scheduling and animation, but `CurrentCue` still unconditionally accesses `Game.Instance.UI.GetCameraRig()`, and startup accesses Player, mode state, projectiles and other live services.
Therefore constructing a headless controller outside Unity does not create a faithful standalone gameplay test.
I did not fake those services and call that an end-to-end result.

After implementation, run an actual managed schema/graph fixture for all three history variants and all terminal edges, then an in-game test from the real audience.
That test must show the addon, return to the genuine native answer list, select actual disclosure, observe the reward cue, and confirm one normal native departure with its portal handling.
Also test refusal, interruption before acceptance, loading a pre-audience save, and persistence after completed acceptance.
Check native FinishActions occur only at the true dialog exit, not at addon entry or return.
Until those checks run, the direct bridge is a concrete supported implementation proposal, not a certified lifecycle fix.
