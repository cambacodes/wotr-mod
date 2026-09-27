# Parent ending guard independent review

Reviewed 2026-09-26 by `/root/minagho_chivarro_editorial_audit`.
I did not author this helper or its focused tests.
I applied the ponytail and unslop skills.

## Verdict

Pass for the narrowly documented, unregistered helper.
I found no blocking defect in preserving the original checker and story actions while applying the caller's replacement predicate.
This does not approve a suppression mapping, an earned-replacement predicate, a route ending or Unity execution.

| Reviewed file | SHA256 |
| --- | --- |
| `src/ParentEndingGuard.cs` | `73D006810C90675998979BF9829D3CBD67724D2404E6E7F96E50792D8AD4AE46` |
| `managed-tests/ParentEndingGuardTests.cs` | `504F606E8EA8BB9E2B67BDC41EEAFEA3EFE4BC0D699C11882FA2516FB883F5E6` |

I read both complete files, the author handoff, and the decompiled native `ConditionsChecker`, `Condition` and `BlueprintCueBase` sources in `reference/game-*.cs`.
The native sources are important because an empty OR checker returns true, whereas a nonempty OR checker containing only skipped null entries returns false.
The helper retains this distinction by calling the original checker instead of reproducing its logic.

## Independent verification

I rebuilt `C:/Users/Z/AppData/Local/Temp/parent-ending-guard-347336f9/Observer.csproj` in Release configuration.
The build succeeded with zero warnings and errors.
I then ran the isolated `Runner.csproj` in Release configuration and independently observed `PASS 37 native observation assertions`.
These commands used the current reviewed helper and test files, not a shared build directory.

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build C:/Users/Z/AppData/Local/Temp/parent-ending-guard-347336f9/Observer.csproj -c Release --nologo
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/parent-ending-guard-347336f9/Runner.csproj -c Release --no-launch-profile
```

The tests use actual native blueprint, condition and action classes.
They execute the custom guard directly through native `Condition.Check`, not the complete populated outer `ConditionsChecker` or `BlueprintCueBase.CanShow` path.
They demonstrate real empty and null-entry checker results, replacement short-circuiting, observation-error fallback and error reset.
They do not demonstrate populated parent-condition truth tables in Unity.

## Findings

The original `ConditionsChecker` object is retained by reference.
Its AND/OR operation, condition order, condition negation, original owners and element names remain unchanged by attachment.
When the replacement predicate returns false, the original checker remains the evaluator.
When the predicate returns true, the guard returns false without evaluating the original conditions.
That short-circuit is intentional; it does not run original condition diagnostics or update their last-result values for a suppressed ending.

The new outer checker contains a single unnegated guard under AND.
The guard is owned by the target cue and registered once in its `ElementsArray`.
The helper does not replace or execute OnShow, OnStop, continuation, answer collections, cue collections or text.
The original actions and conditions remain registered.
The counter actions in the tests prove non-invocation, not execution of the parent's real MarkCuesSeen bookkeeping.

Repeated installation on the unchanged wrapper reuses the same guard and updates its predicate.
It neither adds another element nor nests another original checker in that case.
This is deliberately not an arbitrary-mod-rewrite reconciliation algorithm.
If another mod changes the condition structure after attachment, the helper does not promise to discover and update every existing guard.
Root should install after parent blueprint configuration and avoid treating repeated installation as repair of an unknown modified tree.

A replacement-observation exception is retained in `LastObservationError`, and evaluation falls back to the original checker.
A later successful observation clears the diagnostic.
The helper does not catch or invent a result for an original-checker failure.
Thus fallback preserves the original conditions' decision rather than forcing a parent ending to appear.
Whether both old and new endings could then appear depends on root's eligibility and delivery contract, which is outside this helper.

An absent original checker is explicitly treated as unconditioned.
That is the helper's documented fallback, not literal preservation of a malformed native cue: native `BlueprintCueBase.CanShow` calls `Conditions.Check(this)` without a null check.
This distinction does not affect properly configured parent cues, but null acceptance should not be reported as a tested native null-checker behavior.

One nonblocking diagnostic difference remains.
The helper calls `Original.Check()` without forwarding the cue debug context.
Native `Condition.Check` uses that context for per-condition dialog debug messages, not for the condition's truth calculation.
Original condition truth and owners are preserved, but the original individual conditions will not contribute those same dialog debug messages through this call.
Preserving detailed dialog diagnostics could use the cue as the original checker's debug context in a later small change, with an appropriate runtime check.

## Remaining boundary

The native populated checker enters Unity profiling and exception-reporting paths.
I read the author's boundary probe and its documented ECall failure, but did not claim to rerun that probe as part of the 37 passing assertions.
No Unity method was patched or substituted in this review.
Final native CanShow behavior, real parent initialization, cue selection, save/load and page OnShow arbitration remain unverified here.

The literary review's requirement remains binding: preserve the parent's appropriate cult, dragon, redemption, service and divine consequences while replacing only relationship claims actually superseded by earned extension events.
This helper's ability to hide a whole page is not approval to discard that page's unrelated outcomes.
Root still needs a reviewed cue/page contract, ordinary versus Aeon separation, available-or-already-played predicates, and old-save coverage before registration.
