# Contact continuation review

Independent bounded technical review, 26 September 2026.
Accepted for the current ContactUnit scene set.
I reproduced the Vellexia failure with the new guard removed from a temporary source copy, then independently ran the corrected focused suites.
No product source, shared test or export was edited by this reviewer.

## Exact inspected inputs

| Input | SHA256 |
| --- | --- |
| `src/Story.cs` | `D6AF931FA196A40A16E9D791D711B04AB308DD054AA3AFF5D995A4A7C30C0B48` |
| `tests/ContactContinuationTests.cs` | `4A40405EB4910600D801EDD4F25FFA95B2377087DFEBA5EC0802A233AFD79E0C` |
| `tests/VellexiaOpeningTests.cs` | `A8519E89788D29AD5292AA3FF9BFBE221A04B52022DDD57ACD76430EEF3A1259` |
| Assembled main277 | `070879FB0FF8AF03FAA0E1A9525FDD88AEC61E89912C853877782BAABA952230` |

The independent temporary runner links the actual Story implementation, actual test walker and focused suites.
Its project is `C:/Users/Z/AppData/Local/Temp/contact-review-x86hfwuv/Check.csproj`.
It passed 176,123 focused assertions against main277.
An initial reviewer harness omitted JSON field deserialization and a newly added helper dependency; those harness setup errors were corrected before recording this result.

The negative-control project is `C:/Users/Z/AppData/Local/Temp/contact-before-review-34m1ceqf/Check.csproj`.
It changes only the temporary Story copy by removing the added native-forbid condition.
The actual Vellexia suite then fails with `Vellexia continues after native departure history changes: vellexia.arena_invited`.
This reproduces the rule failure in the real assembled opening scenario, not merely a synthetic flag test.
It is a headless source-level reproduction, not a launched Unity session.

## Behavior and preservation

`ContactAvailable` still immediately permits scenes without ContactUnit, preserving its existing scope.
For scenes with ContactUnit, it now rejects a forbidden flag if the flag belongs to one of the six native binding maps: active etudes, completed etudes, completed quests, seen cues, selected answers or started dialogs.
This makes an externally changed invitation or completed quest invalidate a conversation even while the actor is still physically available.
The same function already checks physical contact, chapter, area, prerequisites, RequiresAny and relationship unavailable flags.

The distinction between native history and authored progress matters.
Authored completion, closing-page flags and cooldown timestamps must not invalidate a goodbye page merely because its own answer recorded progress.
The added condition does not reapply those checks.
The generic focused suite verifies all six binding classes, authored closure/completion/cooldown continuation, and physical contact loss despite that authored continuation.
The real Vellexia suite checks native invitation and quest transition blockers, missing prerequisites, dead/hostile state, wrong area and loss of the original actor, in addition to its complete opening walks.

I inspected the consumers in `src/Main.cs`.
`RouteCondition` uses ContactAvailable for continuing pages, continuing choices and the contact-lost alternative.
`RouteAction` checks it again before applying a continuing choice's effects.
The guard therefore participates in both visibility and the action-side check rather than relying only on the previously displayed answer list.
This inspection does not prove how quickly Unity refreshes an already displayed page or exercise that UI.

The assembled source contains 33 ContactUnit scenes.
I checked them for native ForbidOverrides collisions and found none.
The new native-forbid guard does not honor ForbidOverrides, consistently with `Rules.Validate`, which explicitly rejects override keys in all six native binding maps.
Native-history overrides are not a supported exception to this guard.
I found no blocker for this change.

## Scope of acceptance

The correction closes the reproduced native transition gap for the existing physical-contact model and preserves its authored closing-page behavior.
It does not add ContactUnit to ordinary Konomi, prove physical contact from an office etude, or cancel unitless scenes after external state changes.
It does not unlock Vellexia after the invitation, restore her after death, or provide the missing later route.
Native UI refresh, actual saves and ToyBox manipulation during a live conversation remain runtime verification work.
