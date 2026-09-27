# Parent ending alternate independent engineering review

The frozen helper passes this bounded independent engineering review under its documented caller contract.
No blocking defect was reproduced in the helper's family selection, preservation, or failure behavior.
This approval does not cover production hooks, blueprint registration, a specific ending mapping, or playable ending output.
I did not author ParentEndingAlternate.
My earlier authorship of ParentEndingGuard is disclosed and does not supply independent approval for using that other helper.

## Exact inputs and execution

| Input | SHA256 |
| --- | --- |
| `src/ParentEndingAlternate.cs` | `E96D53EB9B772F1D8C5A0EC54D4B8C8D08A6BEBE74B6B86F3C9013C394F9F347` |
| `managed-tests/ParentEndingAlternateTests.cs` | `ECC55259BFF60CFCF7A11307D8EF9E21991C7B116E3B1BDE8FDC634523BC82E4` |
| Installed `Assembly-CSharp.dll` | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |

I read the entire helper, tests, and handoff, the native BlueprintCueBase and BlueprintCue definitions, the current DialogController decompilation, and Main's generic owner-assignment pass.
The independent temporary harness is `C:/Users/Z/AppData/Local/Temp/parent-alternate-review-1afc5da6`.
It builds the frozen helper against installed native assemblies and runs actual native cue, page, action, checker, localized-string, and reference types.
Both isolated projects compiled with zero warnings and zero errors.
The original 187 assertions passed independently.
Twenty added assertions rejected ten malformed attachments and checked that rejection had not mutated the original page, checker, or elements.
Two further assertions decoded actual native IL instruction boundaries and verified the proposed page-hook shapes.
The total is 209 passing assertions, with the populated-checker Unity boundary reported separately rather than counted as success.

## Conditions, precedence, and history

The original complete ConditionsChecker survives by reference in the binding.
Each member receives one outer AND condition that delegates to the original checker only when that member is selected.
Its nested OR/AND structure, negation, and original native element ownership are not flattened or reassigned.
The helper does not transform original condition exceptions into a successful condition.
The standalone tests establish identity and several empty/null-entry native checker cases; populated truth tables remain a Unity limitation described below.

The page order becomes ordinary alternate, optional survivor alternate, then original at the original logical position.
Unrelated entries retain their order.
Exactly one member is selected by a successful Refresh, including when the caller selects the survivor.
Selection does not itself decide which death, timeline, relationship, or consequence applies; the caller must provide that policy.
Null intentionally suppresses all members.
An unknown cue or selector exception restores original selection and records the observation error.
An unrefreshed or invalidated binding also defaults to the original.

The native ShowOnce and ShowOnceCurrentDialog policies are copied and validated.
The supplied history callback receives the exact local/global scope required by the original policy.
For ShowOnce families, consumption of any sibling blocks the entire family, including an original shown before this extension existed.
Repeatable original cues remain repeatable and do not query a fabricated show-once history.
The second live history read in Allows protects against a sibling consumed after Refresh by an earlier page entry.
A failed late history read on an alternate changes selection to the original, which is still later in page order.
If the history source itself fails, the helper cannot prove unknown sibling history; original fallback still relies on native original CanShow to enforce its own history.
That is an explicit failure fallback, not a guarantee against every duplicate after an unavailable history observation.

## Actions, text, and ownership

Variants must have distinct nonempty blueprint identities, separate element lists, distinct private localization keys, and matching ShowOnce policies.
Every declared BlueprintCue behavior field other than Text is checked against the original, including private listener reference and exact shared action, speaker, continuation, answer, and alignment objects.
The original localized text object and key are preserved.
The helper registers only its own Member condition in each member's element list with the correct member owner.
It does not duplicate page OnShow or change page conditions.

The actual native ActionList.Run tests execute the shared original OnShow and OnStop fixture actions once through the selected alternate, without reparenting them.
An action that changes the requested variant cannot switch the selected sibling during the same refreshed batch.
This matters because native PlayBookPage evaluates and plays every eligible page cue in order rather than selecting only one page cue.
Live selector evaluation for each family member could otherwise show two contradictory outcomes.

Shared action identity does not make all action semantics interchangeable.
Native PlayCue records the selected alternate GUID in local and global history before playing that cue.
An action, continuation condition, or external observer that specifically asks whether the original GUID was shown can therefore see a different answer.
Before integration, inspect the actual targeted runtime behavior graphs for original-self-seen dependencies and either reject that mapping or explicitly review its adaptation.
Do not mark the original seen artificially to conceal this difference.
The existing parent constructor audit reports empty per-cue actions; this review does not convert that older evidence into proof about every future patched runtime action graph.

## Initialization and hook requirements

Main's current generic initialization pass assigns each top-level public ConditionsChecker and ActionList element to the registered blueprint and changes its name before calling OnEnable.
If a variant already shares original action lists at that point, the pass would reparent the original actions to the variant.
The documented order is therefore necessary: register bare alternate identities and private text, finish the generic owner pass, then copy native behavior references and attach the family.
Do not run that owner pass over the shared graphs afterward.
The helper's matching checks are not a substitute for observing that initialization order.

The independently decoded installed IL confirms one BlueprintBookPage.OnShow field read followed by ActionList.Run in PlayBookPage.
The field instruction begins at IL_0035 and the following instruction begins at IL_003F.
CanShowAnyCue has zero matching OnShow.Run sequences.
The native source likewise executes page actions before iterating cue CanShow and PlayCue.
A PlayBookPage prefix refresh is therefore too early if page actions affect earned state.

Production wiring still needs a refresh after that exact action call, before the cue loop, and cleanup on every normal or exceptional exit.
Standalone CanShowAnyCue previews need their own refresh and cleanup.
Nested preview calls must not overwrite or invalidate an active playback snapshot for the same page.
The eventual transpiler must preserve labels and exception blocks and reject unexpected match counts.
I verified instruction locations, not a working Harmony patch or its exception/nesting behavior.

## Idempotence and adversarial coverage

Reattaching the same unchanged family reuses its binding and updates its observation callbacks without duplicating guards or page entries.
Changed family size, identity, owning page, guard shape, or relative family order is rejected on that supported repeated-attachment path.
Arbitrary external mutation of alternate behavior after attachment is outside that contract; repeated Attach is not a general repair operation for a corrupted blueprint graph.
Attach should run only during the controlled initialization stage, not as a recurring update.

Independent added fixtures reject changed global and current-dialog show-once policies, duplicate original page occurrences, missing original, an alternate already in the page, altered continuation or speaker, empty alternate identity, shared original text, and changed OnStop.
Each rejection retained the original checker, page count, and original element registration state.
The original suite additionally covers duplicate survivor identity, changed OnShow, colliding text keys and GUIDs, unknown selector results, observer exceptions, late exceptions, global/local consumed siblings, repeatable cues, batch stability, optional survivor absence, and reordered families.

## Runtime limits and verdict

Invoking a populated native ConditionsChecker in this standalone process reproduced `System.Security.SecurityException: ECall methods must be packaged into a system module` through Unity logger initialization.
No replacement Unity methods or synthetic success hook was used.
Full native CanShow, populated original condition truth tables, PlayBookPage presentation, global registration, save/load, and the forthcoming Harmony integration remain unverified here.
Cached reference fixtures prove actual-type behavior, not registration in the game's blueprint cache.

The helper is suitable for the next independently reviewed integration step.
Its scoped pass is conditional on private localization, the after-owner-pass attachment order, batch refresh/cleanup, actual cue-history observers, and target-specific self-seen dependency checks.
It does not authorize blanket suppression of parent epilogue pages or loss of retained cult, redemption, dragon, divine, service, Legend, or couple-history consequences.
