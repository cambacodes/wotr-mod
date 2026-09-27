# Native ending history correction: independent review

Reviewed on 2026-09-26.
Verdict: pass for the native per-page once-only correction and its managed verification.
The actual old failure reproduces, the corrected generated pages respect global native history, and generated save identities remain unchanged.
This does not approve optional RanRomInt attachment, a real save round trip, Unity rendering, or a whole native ending campaign.

## Reviewed pins

| Input | SHA256 |
| --- | --- |
| Old `src/Main.cs` snapshot | `1A09266238C0ED3914202F8DCFE3B89CB490A5DF50B6D4051EA2FF9053C03B4D` |
| Corrected `src/Main.cs` | `36371B8438C792DFF6D0502B508474737F5E0BAE51FCAC21BA3F8E439A5911E6` |
| `managed-tests/EndingDeliveryTests.cs` | `A8502875B713F6B7CFA84A1C881CBA96A4B5B45FCB84D3936192A07F84517947` |
| `managed-tests/Program.cs` | `63A49ABB2674C0258DC66BC32968D40AEB54A8B9728F236E567B4782291D65EF` |
| Input story | `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC` |

I inspected the exact production diff.
It adds only `page.ShowOnce = scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal)` in BuildScene.
It does not add a saved addon flag, change blueprint IDs, alter route predicates, reorder pages, or change ending answer actions.
The ordinary and Aeon owner names both satisfy that explicit suffix test.
Non-ending pages retain their previous false ShowOnce setting.

## Independent reproduction and correction checks

I made two isolated source snapshots under `C:/Users/Z/AppData/Local/Temp/ending-history-independent/`, substituting the retained old Main into the old copy and using the corrected Main in the new copy.
Both compile against the installed actual game assemblies with zero warnings and errors.
The harness invokes real Main.BuildScene for the 195 ending scenes in the pinned export, producing 248 actual BlueprintBookPage objects.
It does not substitute hand-written page construction for the changed production method.
It is a focused BuildScene reproduction, not a claim to have rerun the entire Main.Build fixture independently.

Using the submitted EndingDeliveryTests, the old source fails exactly at `ending_together`: `A played ending can repeat through another sequence`.
Native DialogController.PlayCue has already recorded the page in Player.Dialog.ShownCues and LocalShownCues at that point.
Clearing only local history and using a second native CueSequence still permits the old page to show again.
The plain ending's empty Continue action does not establish a saved addon completion flag.
This reproduces the real policy mismatch found in the prior integration review.

The new build passes all 1,170 submitted native-history assertions across the 195 ending entry pages.
An unseen eligible page is selected by the first native CueSequence.PollNextCue.
Actual PlayCue writes both histories.
After local history is cleared, global history still suppresses CanShow and the second sequence's poll.
A fresh Player.Dialog history makes the same blueprint eligible again, excluding process-global leakage between player histories.

I extended only the temporary test copy to check every remaining node in the multi-node endings while retaining that scene's global history.
All 53 subsequent or alternative pages remained eligible before their own first display and became ineligible after their own native PlayCue.
The expanded independent run passes 1,276 assertions over all 248 ending pages.
This establishes that displaying an entry page does not prematurely consume its remaining branches or following pages.
It does not execute every branch's route conditions or choice effects; those conditions are deliberately removed only during the isolated native history probe and then restored.

I also compared the complete generated name/GUID lists between old and new source runs.
All 972 generated ending blueprint identities match exactly, including pages, cues, answers, dialogs, and any generated checks.
The old and new page identity lists are byte-identical.
No save identity migration is introduced by this correction.

## Test design and runner adoption

The test replaces the Game singleton with a temporary native Player and DialogState fixture.
It temporarily intercepts PlayBookPage before Unity rendering, runs the page's existing OnShow actions, and suppresses only the debug logger needed by this headless path.
It leaves PlayCue's native history mutation and BlueprintCueBase.CanShow/CueSequence.PollNextCue behavior in place.
Conditions are restored in a per-page finally block, and the outer finally removes only this harness's Harmony patches and restores the prior Game singleton.
The fixture player and its histories are discarded rather than changing an existing player's progress.

The generated addon pages currently have empty OnShow actions.
Calling them in the renderer interception is consistent with the tested pages but is not a broad approval of replacing arbitrary native PlayBookPage behavior.
The fixture makes no claim about rendering, input, animation, native etude evaluation, or a real save-load cycle.

Program registers this test after Main.Build initialization and the existing parent-ending integration checks.
Its ordinary generated-blueprint loop also asserts ShowOnce equals ending ownership and ShowOnceCurrentDialog remains false for every page.
That catches accidental application of the global history rule to ordinary conversation pages and an accidental change to dialog-local history only.
The existing stable-ID, answer-count, direct continuation, skill-check target, and action checks remain in place.

For a branched ending, ShowOnce applies to each page independently, matching native page history rather than fabricating completion of the entire authored scene.
Unused branches are not globally marked seen when an entry page displays.
The correction intentionally leaves addon scene completion flags untouched, so the pure Rules synthetic-completion tests must retain their explicit qualification.

## Remaining work

The default native seen-state replay defect is resolved by the reviewed correction.
Native serialization is still a separate boundary: this review uses actual Player.Dialog history but does not save and reload a game.
In-progress ending restoration and rendered multi-page continuation should be included in the eventual live verification.

No additional sequence is attached by this patch.
The absent RanEpilogue plugin's conditional RanRomInt graph, its caller/version provenance, and the choice of where to attach addon endings remain open requirements from the prior integration review.
The two temporary sequences prove that the same corrected page will not display twice against the same global history.
They do not prove that the installed game's conditional graph reaches either sequence at the intended moment or preserves every parent side effect.
The source correction can be committed independently of that unfinished delivery work.
