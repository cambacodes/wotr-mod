# Parent ending guard prerequisite

This is an unregistered condition wrapper for a caller-selected existing BlueprintCueBase, including a BlueprintBookPage or an individual BlueprintCue.
All three assigned paths were absent before this task.
The source and focused tests are frozen for independent review.
I authored them and do not claim independent approval.
No Main, story export, parent blueprint registration, saved state, installed mod or shared build output was changed.

| File | SHA256 |
| --- | --- |
| `src/ParentEndingGuard.cs` | `73D006810C90675998979BF9829D3CBD67724D2404E6E7F96E50792D8AD4AE46` |
| `managed-tests/ParentEndingGuardTests.cs` | `504F606E8EA8BB9E2B67BDC41EEAFEA3EFE4BC0D699C11882FA2516FB883F5E6` |

## Parent behavior and integration boundary

I read the ending section of `reference/canon-review/minagho-chivarro-integration.md` and the decompiled `MinaEpil.cs`.
The parent sets each ordinary page's OnShow to mark all eight ordinary pages seen.
It also sets a separate native paired-page condition, while Aeon uses its own sequence.
Those existing actions and conditions must remain intact for untouched parent histories.

Root's later literary review identified that suppressing an entire parent page could discard cult, redemption, dragon and divine consequences alongside the relationship text.
This helper therefore has no hardcoded page list, cue list, timeline mapping or suppression policy.
Native decompilation confirms BlueprintCueBase declares Conditions and both page and cue inherit it.
`Attach(BlueprintCueBase cue, Func<bool> replacementAvailable)` can wrap exactly the relationship cue selected by the later reviewed contract.
It can also wrap a page when a complete and appropriate replacement has actually been established.
Calling it on all parent pages without that contract is not authorized by this prerequisite.

Root must supply a predicate proving an earned applicable replacement is currently available or has already played, with ordinary and rewritten timelines separated.
A merely planned route, generic relationship flag or extension installation is insufficient.
The helper does not establish that proof itself.

## Implementation

Attach stores the original ConditionsChecker object without flattening its AND/OR operation, changing its condition order or altering original element identities, negation, names or owners.
It installs a single outer AND condition owned by the same cue and adds only that new element to the cue's ElementsArray.
The original checker remains the actual evaluator when replacement eligibility is false.
A true replacement predicate short-circuits before any original condition evaluates.
No OnShow, OnStop, text, answer, cue-list or continuation content is changed or invoked.
No parent page is marked seen and no native story flag is forced.

Repeated attachment to the unchanged single-guard checker updates its predicate without adding another wrapper or element.
The helper does not search or rewrite arbitrary structures created afterward by another mod.
If no original checker exists, the wrapper treats the target as unconditioned.

A replacement-observation exception falls back to the original checker and is retained in the guard's LastObservationError property.
A later successful observation clears that diagnostic.
The wrapper does not catch or redefine failures of the original native checker.
Thus an unavailable replacement observation cannot itself remove the parent ending, although the parent's own conditions may still reject it.

## Verification and limits

Isolated projects are `C:/Users/Z/AppData/Local/Temp/parent-ending-guard-347336f9/Observer.csproj` and `Runner.csproj`.
The isolated source and runner builds pass with zero warnings and errors.
The focused runner passes 37 assertions.

The tests construct actual native BlueprintBookPage, BlueprintCue, ConditionsChecker, Condition and ActionList objects.
They verify preservation of the original checker, both operation values, condition identities and negation, owner/elements registration, unchanged parent actions and content lists, duplicate attachment, true-predicate short-circuiting, predicate-failure fallback and diagnostic reset.
They exercise actual native empty-checker semantics and null-entry AND/OR terminal semantics for false and throwing replacement predicates.
They also verify independent cue wrapping and preservation of its OnShow, OnStop and continuation.
The action fixtures are counters, not a claim that actual parent MarkCuesSeen actions have run.

A separate temporary `BoundaryTests.cs` invokes the native populated checker through the wrapper.
It reaches `System.Security.SecurityException: ECall methods must be packaged into a system module` during the native checker failure-reporting path, including Application logging and Game service initialization.
The native source shows nonempty condition evaluation first enters ProfileScope.New, which reads Unity Application.isEditor.
No engine method was patched or replaced to bypass this boundary.
Full populated-condition truth tables, BlueprintCueBase.CanShow, native parent initialization, final cue selection and real OnShow seen arbitration are not proven by this standalone runner.
The preserved checker identity and direct call establish the intended delegation, while final Unity execution remains required.

The exact cue-level replacement contract, available-or-already-played predicates, timeline separation, literary approval and integration tests remain root-owned work.
No route readiness or parent-story parity is claimed from this prerequisite.
