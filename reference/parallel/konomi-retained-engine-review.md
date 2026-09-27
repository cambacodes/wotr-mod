# Konomi retained recovery engine integration review

Reviewed 2026-09-26 by `/root/minagho_chivarro_editorial_audit`.
I did not author these engine changes or the focused test file.
I applied the ponytail and unslop skills.

## Verdict and frozen scope

Pass for the reviewed engine integration after the defects below were corrected.
This is not approval of the recovery manuscript, full Konomi route, actual native resurrection, or game release.
The service remains limited to the exact retained native body in its loaded capital source.

| File | SHA256 |
| --- | --- |
| `src/Main.cs` | `ECFF46A9D3514BC2E07E6FF1522C5498D9FC867E349B3F43A39717A50BC7CE9E` |
| `src/Story.cs` | `208FCCEA83F2A8CF4F192023512DC4DC3A0159C6AAFFD51AB38F263944EC9DA3` |
| `src/KonomiRecovery.cs` | `5D03FC5270B69B8CEACA3A9C55702060106CD1AF1FB8C3CECAC9774A647901BD` |
| `tests/RetainedRecoveryRulesTests.cs` | `A5F6EE5ECC458B554F0DB88550CC0985224A63886D784D4971F63E3B22BAD405` |
| `tests/Program.cs` | `34D9C879AB046D696EF3A9EC715F1049BDB855A1545541C2A159490A905B2E8E` |

I independently verified these hashes after root reported the engine frozen.
I read the current diffs, full recovery service, contact observer, reused source-provenance inspector, physical-contact helper and earlier independent service/observer reports.
I also inspected the Main action, reconciliation, state publication and journal-entry paths.

## Defects found and corrected during review

The first draft reused `konomi.returned` for verified resurrection.
The actual existing 533-scene story already sets that flag during ordinary `konomi.return`.
I reproduced a validation failure against the existing export in an isolated .NET 8 project; root's full checks independently caught the same collision.
The frozen version uses `konomi.retained_return_confirmed` and leaves the old ordinary flag intact.

The first draft published `konomi.retained_dead` only when `CanRequest()` was true.
That omitted death after an already confirmed return, because repeated resurrection is deliberately disallowed.
The frozen version publishes observed retained death through a separate `RetainedDead()` call, while `CanRequest()` still controls eligibility for the one return.
The semantic separation is visible in source; a later death must not become an absence of death merely because another return is forbidden.

The first draft rejected manufactured proof in choice effects but allowed reserved proof names as scene IDs.
I reproduced three accepted ordinary terminal scenes with IDs matching the new confirmed-return, physical-contact and retained-death flags.
Main records a completed scene's ID, so this bypassed the choice-effect restriction.
The frozen validator also reserves these names against scene IDs, relationship state aliases and all native binding dictionaries.

I identified that two identical terminal revival choices in different nodes would serialize to the same saved request identity and make reconciliation's `SingleOrDefault` ambiguous.
The frozen validator permits at most one Konomi revival terminal per recovery scene.
Unique scene IDs then disambiguate requests across scenes.
The author can converge narrative branches onto that one terminal rather than duplicating it.

The first physical-return wrapper combined verified source identity with a second lookup by blueprint.
I reported the missing explicit equality as a defensive proof gap, not a demonstrated live-game substitution.
The frozen wrapper now requires the unique native unit-pool candidate to be the exact verified actor object before using the existing physical-contact checks.

## Independent execution

My isolated project is `C:/Users/Z/AppData/Local/Temp/konomi-engine-audit-41575ee4/Check.csproj`.
It compiles the reviewed production `Story.cs` and focused test source into its own output directory.
After the final hash check, it independently passed all 38 focused assertions.
I also ran 21 private adversarial probes: three reserved evidence names used as scene IDs and as aliases in each of the six native binding dictionaries.
All 21 now reject.
Those private probes are additional observations, not part of the 38-assertion count.

```powershell
& C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project C:/Users/Z/AppData/Local/Temp/konomi-engine-audit-41575ee4/Check.csproj
```

Root reported the full existing 533-scene rules run passing 24,303,393 assertions and the source build passing without warnings.
I did not independently rerun that full suite.
Root subsequently reported the shared 533-scene managed run passing 66,293 assertions, with DLL SHA256 `3A2C280601E80742B128F8B7CDF077B5B54757B337ECA3D642056883CC67F333`.
Those broader results are root's execution evidence, not independent executions by this reviewer.
No shared source, generated export, installed mod, save or shared build output was changed by me.

## Contract assessment

The explicit RouteAction checks current scene availability, continuation contact and choice requirements before calling `Request`.
Validation requires the current Trickster flag and current retained-death evidence for a Konomi recovery scene.
The production service records the exact serialized scene/choice request and actor ID before native dispatch.
A changed or missing request cannot silently adopt a pending checkpoint.
Changing authored choice text or structure therefore invalidates that exact pending match; any future migration needs an explicit policy rather than guessing.

Only a current Confirmed result records the terminal recovery effects.
The only permitted explicit effect is `konomi.retained_return_confirmed`; Main also records the completed scene ID through its ordinary progress mechanism.
Restoration does not set commitment, affection, office history, dismissal history or access to the missed-contact route.
The recovery service does not clear native death history or manufacture a replacement actor.

Reconciliation matches the saved exact authored request and calls `Poll(true)`.
Here `true` recognizes the earlier explicitly authorized action; it is not a new spell authorization.
Poll cannot call resurrection and grants no success merely because a checkpoint exists.
It requires a current observation of the same actor alive and conscious and a successfully persisted confirmation.
An already recorded scene is skipped, and retained proof is not cleared through the generic Fate path.

The closure exception is scoped to Konomi recovery and validated Konomi aftermath scenes.
Ordinary romance remains closed after refusal.
Aftermath requires both saved confirmed-return history and current original-actor physical-contact evidence, with the exact Konomi ContactUnit.
The contact guards are applied during the conversation as well as at initial availability.
The focused tests cover loss of current evidence, hidden contact, area mismatch, unrelated unavailability, missing Trickster authority, preserved closure and a later retained death.

`ReturnContactAvailable()` validates loaded source provenance, confirmed actor identity, exact native unit-pool identity and existing physical availability.
That physical helper requires the current view to belong to the actor, a loaded active scene, current native storage, consciousness, life, no suppression and no hostility.
Saved confirmation alone cannot substitute for those checks.
These runtime checks were inspected, not executed in a live Unity lifecycle during this review.

Starting a recovery book also uses the existing journal-entry code, which sets `konomi.started` and may give the relationship objective.
Therefore the terminal proof effect is not a claim that the book has no other entry effects.
I checked the existing Konomi ending requirements and found none that grants romance from `konomi.started` alone.
Root has separately agreed to make the journal description neutral about whether earlier correspondence exists before integrating the manuscript.

## Remaining work

The new four-scene manuscript and its joins require their own literary and earned-history review.
The final integrated export must preserve the old ordinary `konomi.returned` meaning, use the new proof flag consistently and include the revised journal copy.
The retained return's native operation still has the documented standalone ECall boundary; no successful Unity resurrection is established by these rules checks.
Real later-frame state, view restoration, save/load, event delivery and ToyBox execution remain required verification.
Missing, destroyed, never-spawned, hostile, displaced and other unsupported histories remain unfinished parts of the broader Trickster objective.
