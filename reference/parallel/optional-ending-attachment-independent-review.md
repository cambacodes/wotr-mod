# Optional ending attachment independent review

Reviewed 2026-09-27.
Verdict: pass for the source attachment, managed construction, failure preflight, and build-script changes reviewed here.
No blocking defect remains in this scope.
The absent external plugin's initialized caller graph, gameplay timing, and save round trip remain unverified.

## Frozen inputs

| Input | SHA256 |
| --- | --- |
| `src/Main.cs` | `132A8C0F3B287C48F1A15AC6D9D733D0C9F443C25E7427C3D957CE4B98B0BF1B` |
| `managed-tests/Program.cs` | `7E542197F2B491C6DDFCD4A1B6F4635BB611BA8CB8808BD738E687F8BC11826F` |
| `build-expansion.ps1` | `F9F439E58B74C4912B56407D328660101F783A8908BAA09F114D5B864F6246C3` |
| Root tested DLL | `329E1A49C3AD47114DC46DDFDFF58C2CA46EE86D9EEE0030BBC9BEE649CAF162` |
| Development story | `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC` |

This review changes no production files, generated outputs, installed files, or package.
The independent probe compiled a frozen source copy before subsequent Nurah movement work.
That later work is outside this verdict.

## Parent contract and initialization

The installed Relations and Romances version is 0.1.11, with Harmony owner `RanRomance`.
Its DLL SHA256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Reviewed parent evidence includes `C:/Users/Z/AppData/Local/Temp/nocticula-audit-8d261252/RootMain.cs` and the fresh `C:/Users/Z/AppData/Local/Temp/nocticula-final-independent/EpSetup-fresh.cs`.

Parent `EpSetup.Configure` creates the ordinary `RanRomAdd` sequence, GUID `ed4baeaf69394754902344f0598d7e5a`.
When `Harmony.HasAnyPatches("RanEpilogue")` is true, the parent also creates `RanRomInt`, a `BlueprintCueSequence` with GUID `2b9424b1b93e4d0896b0958db79d2339`.
The two sequences contain the same parent page assets, including the four ordinary Nocticula pages.
They have separate exits and caller wiring.
The optional sequence is parent-created conditional integration, rather than a native archive sequence or an addon-owned replacement.

Parent initialization calls `EpSetup.Configure` from its blueprint-cache postfix.
The addon postfix retains `HarmonyAfter("RanRomance")` and `Priority.Last`, so its lookup follows that pinned parent initialization.
This supports the presence check used here.
It does not establish attachment to a blueprint created later by an unrelated initializer.

The parent patches native `SequenceExit0306`, GUID `d649f17a42a8e0c418bb336ced272934`, to offer its default sequence.
Its conditional branch instead patches exit `607351955e174bd8b3d61ba9a4df9b6c` to offer `RanRomInt`.
The latter exit is absent from the inspected native archive, and no installed mod manifest identifies `RanEpilogue`.
An applicable external plugin version and its complete caller graph therefore cannot be named or certified from this installation.
The unchanged native Aeon sequence is `ced82f299d246f448b48afa0b630dd70`.

## Implementation findings

Main resolves the optional identifier before parent-ending preparation, addon registration, or dialogue mutation.
An absent blueprint leaves default construction intact.
A present blueprint of another type throws the specific preflight error before mutation.
The ordinary ending loop appends one reference object to both sequences, resolving to the same generated `BlueprintBookPage` instance.
It does not clone pages, change their GUIDs, duplicate page actions, or replace the existing sequence lists.
Aeon endings only enter the Aeon sequence.

Existing sequence prefixes remain in their own order.
The change assigns neither sequence conditions nor exit references.
The existing initialization/error guard prevents a second Build from appending duplicates and prevents repeated mutation after a failed preflight.
It intentionally does not retry an initialization failure within the same process.

The earlier independently reviewed global `ShowOnce` correction remains present on generated ending pages.
Because both sequences resolve the same page, native player history applies to both entries.
The earlier actual `DialogController.PlayCue` and `CueSequence.PollNextCue` tests cover global seen-state for all first pages and the independent follow-up covers all 53 later pages.
See `reference/parallel/ending-native-history-independent-review.md` for the exact rendering bypass and history limitations.
This attachment introduces no new history writes or completion flags.

## Independent checks and root suite

The original managed reproduction failed with `Optional epilogue omits or reorders addon endings` before the production correction.
Its retained log is `C:/Users/Z/AppData/Local/Temp/optional-ending-repro.err`.
This reproduces missing sequence attachment as closely as the available installation allows, without pretending to execute an absent plugin.

My independent fixture is retained at `C:/Users/Z/AppData/Local/Temp/optional-ending-independent/`.
It calls actual Main.Build against native game types with two ordinary endings and one Aeon ending from the pinned story.
The default sequence begins with reference A, while the optional sequence begins with the deliberately different prefix B, A.
This avoids relying on the shared runner's identical-prefix fixture.

| Independent mode | Result |
| --- | --- |
| Optional absent | 5 checks passed |
| Optional present with different prefix | 10 checks passed |
| Optional wrong type | 3 checks passed |

The presence probe checks exact prefix reference identity, unchanged Conditions object identity, exact appended reference and page identity across both ordinary sequences, exclusion of the Aeon page, and second-Build idempotence.
The wrong-type probe checks failure, zero generated registrations, and unchanged ordinary/Aeon references.
Temporary fixture compilation completed with zero warnings and errors.
An initial fixture assembly-resolution failure was corrected in its bootstrap before these executions; it did not require a production change.

The submitted runner also checks preservation of native answer references after preflight failure and the full exported ordinary-ending order.
I inspected the final root logs and their DLL/story pins.

| Root full managed mode | Result |
| --- | --- |
| Absent | 79,952 assertions passed |
| Present | 79,955 assertions passed |
| Wrong type | 774 assertions passed with the expected preflight rejection |

Logs are `C:/Users/Z/AppData/Local/Temp/optional-ending-0-fixed.out`, `optional-ending-1-fixed.out`, and `optional-ending-wrong-type-fixed.out`, with adjacent error streams.
The present fixture models the parent's reuse of page assets, not the external plugin's complete initialized graph.

## Packaging script review

The script now invokes the managed runner in three separate processes using modes `0`, `1`, and `wrong-type`.
Separate processes prevent the static Build guard and blueprint cache from leaking between modes.
A nonzero exit throws before package staging.
The previous `RRT_TEST_EXPANDED_EPILOGUE` value is captured and restored in `finally`, including the previously absent case.
Existing Python/binding environment restoration and the story-hash check remain intact.
This script change passes static review.
The complete packaging command has not been rerun at this checkpoint, so this report does not certify a fresh package.

## Remaining integration boundary

When the external plugin is available, record its exact version and inspect the final initialized caller graph and both exits before claiming compatibility.
Verify actual route eligibility, timing, page presentation, and persisted seen-state in a game save.
The current fixtures bypass full campaign eligibility and Unity rendering; they establish attachment and native history behavior under their stated inputs.
They do not establish that either external caller is reached in a real campaign, whether both are reached, or that a save round trip has occurred.
Those open checks do not invalidate the corrected same-page attachment, but they prevent a full external-plugin or release approval.
