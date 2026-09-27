# Parent ending alternate helper: frozen implementation for independent review

Status: implemented and tested in an isolated harness; independent review and production integration remain required.
This handoff does not approve the helper, manuscript, parent ending contract, or playable route.
Only `src/ParentEndingAlternate.cs`, `managed-tests/ParentEndingAlternateTests.cs`, and this handoff belong to this engineering change.
No Main, exporter, story registration, generated output, or manuscript changes were made for this task.

## Frozen files

| File | SHA-256 |
| --- | --- |
| `src/ParentEndingAlternate.cs` | `E96D53EB9B772F1D8C5A0EC54D4B8C8D08A6BEBE74B6B86F3C9013C394F9F347` |
| `managed-tests/ParentEndingAlternateTests.cs` | `ECC55259BFF60CFCF7A11307D8EF9E21991C7B116E3B1BDE8FDC634523BC82E4` |
| Inspected game `Assembly-CSharp.dll` | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |

## Caller contract

`Attach(page, original, ordinaryReference, survivorReference, select, wasShown)` returns a binding with `Refresh()`, `Invalidate()`, and `LastObservationError`.
The optional survivor reference may be null.
The caller registers actual native cue identities, supplies distinct private localized text keys, and copies the original cue's behavior references before attachment.
The helper does not register blueprints, clone action graphs, generate localization, or change any original text/key.
The original and variants must have distinct nonempty GUIDs and distinct element-registration lists.
Each declared BlueprintCue behavior field other than Text must match the original, including exact ActionList, continuation, speaker, and answer references.
ShowOnce and ShowOnceCurrentDialog must also match.

The selector returns the original cue, ordinary alternate, survivor alternate, or null to intentionally suppress the entire family.
The caller owns earned-state, arrival, death precedence, and consequence decisions.
Unknown selections and selector/history observation exceptions select the original and retain an error for diagnostics.
Failures of the original native condition checker are not converted into invented eligibility.
Do not separately attach ParentEndingGuard to the same original cue; unrelated suppression targets may use that helper.

The original ConditionsChecker is retained by reference inside a new outer AND guard.
Nested OR, negation, native element owners, and the original checker are not flattened or rewritten.
The family occupies the original logical page position as ordinary, optional survivor, then original.
Keeping the original last allows a late history-observation failure on an alternate to fall through to the original.
Unrelated page entries retain their order.
Repeated attachment to the same unchanged family reuses the binding and guards; changed family/order is rejected.

`wasShown(cue, localScope)` must read the actual cue history without changing it.
The boolean selects current-dialog versus global history using the original ShowOnceCurrentDialog policy.
If any member of a ShowOnce family has been consumed, every member is suppressed.
The history is checked both at Refresh and when a selected member is evaluated, covering consumption by an earlier page cue.
Repeatable cues do not acquire an invented ShowOnce rule.
No code artificially marks the original cue seen.
If the history observer itself fails, original fallback cannot establish unknown sibling history; native original CanShow still enforces its own history.

## Required integration timing

Main.Build currently reassigns owners of public ConditionsChecker and ActionList elements before OnEnable.
Running that pass after an alternate shares original ActionList objects would reparent native actions.
Register alternate identities and their private text before save deserialization, keep them bare through that generic initialization pass, then populate shared behavior references and attach this helper afterward.
Do not run the generic owner-reassignment pass over those shared objects again.
Attach adds only its own per-cue guards to the respective element lists.
Original action and condition elements retain their original owners.

Native `private void DialogController.PlayBookPage(BlueprintBookPage page)` runs `page.OnShow.Run()` before iterating all page cues and invoking CanShow and PlayCue on each eligible cue.
PlayCue records the selected cue identity in dialog/global history, and CurrentCue changes run cue OnStop/OnShow actions.
Live selection predicates on successive family members could therefore display two alternatives if the first member's OnShow changes eligibility.
Refresh freezes selection once per native evaluation batch; selected cue actions do not switch to another sibling during that pass.
History checks remain live to prevent replay.

Production integration needs these concrete hook points:

1. Refresh page bindings before standalone `private bool DialogController.CanShowAnyCue(BlueprintBookPage page)` evaluation and invalidate afterward in a postfix/finalizer.
2. In PlayBookPage, inject Refresh after the exact `BlueprintBookPage.OnShow` field read followed by `ActionList.Run`, before the cue loop.
3. Invalidate the active PlayBookPage batch in a postfix/finalizer, including exceptional exits.
4. Track active page scopes so nested preview calls cannot refresh or invalidate a page already being played.

A PlayBookPage prefix alone is too early because page actions can change earned state.
Do not refresh each frame or leave a selection cached indefinitely.
The inspected native IL has exactly one matching OnShow.Run sequence: the OnShow field read starts at IL_0035, and the call completes at IL_003F.
The page field is read through a compiler-generated closure, so matching must not require ldarg.1 immediately before the OnShow field read.
Injected ldarg.1 can still pass the method's page argument to the refresh callback.
CanShowAnyCue has no such page action sequence.
The root's eventual transpiler must preserve labels and exception blocks and reject an unexpected match count.
No hook implementation or production registration is included in this helper.

## Action and identity limits

The chosen alternate executes the exact shared original OnShow and OnStop ActionLists, with original action owners.
Page actions are neither copied nor executed by attachment or condition evaluation.
However, native dialog history records the chosen alternate GUID, not the original GUID.
An action or external condition explicitly querying the original cue's seen identity can consequently observe a different result.
The audited current parent constructors contain no per-cue actions, but integration must inspect actual runtime action graphs and reject or separately adapt any dependency on the original cue's seen identity.
Shared object identity alone does not prove semantic equivalence for arbitrary future actions.
The helper deliberately does not rewrite those action references or fabricate original history.

## Focused verification

The isolated harness is `C:/Users/Z/AppData/Local/Temp/parent-ending-alternate-8fa82025`.
Observer.csproj compiles the owned helper against the installed native assemblies, with a temporary Main marker only for assembly discovery.
Runner.csproj compiles the owned tests and loads the installed game assemblies.
No shared build outputs are used.

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe build C:/Users/Z/AppData/Local/Temp/parent-ending-alternate-8fa82025/Observer.csproj -c Release --nologo
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/parent-ending-alternate-8fa82025/Runner.csproj -c Release --no-launch-profile
```

Result: build passed with zero warnings/errors; 187 native observation assertions passed.
Coverage includes family exclusivity, optional survivors, suppression, initial and late observation failures, global/current-dialog history, consumed original and sibling identities, repeatable cues, idempotency, rejected malformed variants, preserved condition trees/owners, and selection stability while actual native ActionList.Run changes the desired selection.
Fixture actions execute once through shared ordinary OnShow/OnStop lists; page actions remain untouched.
The tests use actual BlueprintCue, BlueprintBookPage, ConditionsChecker, ActionList, LocalizedString, and native reference types.
Test references populate their native cached-reference field directly; they do not prove global registration.

Guard assertions invoke the attached native Condition directly.
Populated native ConditionsChecker.Check reaches Unity logging initialization and fails outside Unity with `System.Security.SecurityException: ECall methods must be packaged into a system module`.
No Unity methods were replaced to hide that boundary.
The original nested checker identity and structure are verified, but full populated parent truth tables, native CanShow, PlayBookPage execution, Harmony hook behavior, global blueprint registration, save/load, and manual game presentation remain unverified here.
Actual native ActionList.Run with the fixture actions did execute successfully.

Independent review should examine the helper and tests at the frozen hashes, then review production wiring separately once the root provides it.
