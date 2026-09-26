# Irabeth native meeting-selector witness

The installed native actor-conflict filter can be exercised headlessly, and sixteen arbitration/claim assertions passed.
It confirms that candidate priority 100 can displace the ordinary departure claim at 99, but does not automatically yield to equal or lower-priority native events.
This is a usable prerequisite for implementing the bounded meeting policy, not approval of a delivered meeting or recovered actor.
No production helper, registered placement, native save or installed mod file was changed.

## Reproduction and inputs

Run `reference/canon-review/irabeth-meeting-selector-probe.py` with the project's explicit Python interpreter.
It reads the installed archive, verifies the two native identities/priorities/groups, then creates and builds a fresh isolated .NET Framework 4.8 project against the installed managed assemblies.
The reviewed successful run generated `C:/Users/Z/AppData/Local/Temp/irabeth-meeting-selector-1ky0o6q1`.
The build completed with zero warnings and errors.

Installed `Assembly-CSharp.dll` SHA-256: `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.

| Verified archive record | GUID | Priority | Raw member SHA-256 |
| --- | --- | ---: | --- |
| `ImportantNPCs_fate/IrabethNotInDrezen.jbp` | `99a03d4f02004b76a5e97c85ba0ec37e` | 99 | `D6CED57B8DA0F86F1F404AA655B84EB7D03341508F2DA19762F6BB258E2BA73F` |
| `ImportantNPCs_fate/IrabethNotInDrezenCh5_WithGalfrey.jbp` | `260454e5186fbd34694a0393097f77b5` | 400 | `67F68173DDD5E7650A5C78A76A4829D25682BFF1FFFBF2FC2BD6ED33A33C53F9` |

Both records belong to Irabeth's actual conflicting group `997d865aa6f17cc48b480bd62ba02841`.
Their full archive paths are verified in the probe rather than guessed from display names.

## What the fixture actually executes

The probe calls the installed private `EtudesTree.FilterOnActors` through reflection, including its actual `CheckBlockConflicts` and `BreakConflictingEtude` calls.
It does not copy the sorting or priority algorithm into a test implementation.
It also invokes native `SetConflictingGroupTask`, `GetConflictingGroupTask`, `AddToPlaying` and `RemoveFromPlaying`.
The actual `EntityFactsManager` supplies the facts consumed by the filter's native lookup.

The Game, Player, PersistentState, etude system and fact shells are detached in-memory fixtures.
They supply the narrow native dependencies required by those methods.
Native blueprint-reference objects cache the in-memory group object, preserving the verified GUID without loading a game scene.
The native departure/expedition identities and priorities are represented by minimal synthetic blueprint objects, not a full deserialization or activation of their real HideUnit actions.
The meeting, equal-priority event, lower event and unknown holder use clearly synthetic GUIDs.
No unit, spawner, actor view, quest or invitation is fabricated as present.

An initial attempt reached the native logger's subscription to `UnityEngine.Application.logMessageReceivedThreaded`, which cannot execute in a plain .NET Framework process.
The final fixture supplies an ordinary native Logger instance directly, bypassing only its Unity subscription initialization.
Logging remains enabled; no selector method, Unity internal call or activation method is patched.
This is test scaffolding inside the temporary process, not a proposed production initialization path.

## Observed arbitration

| Fixture state | Native result |
| --- | --- |
| Departure 99 holds group, meeting 100 starts | Meeting remains selected; exact departure fact is scheduled to stop. |
| Native event 100 holds group, meeting 100 starts | Meeting is removed from the starting set; native holder is not stopped. |
| Meeting 100 holds group, native event 100 starts | Native event is blocked; equality does not preempt the meeting. |
| Expedition 400 holds group, meeting 100 starts | Meeting is blocked. |
| Unknown holder -10 holds group, meeting 100 starts | Native arbitration would displace the unknown holder. |
| Meeting 100 holds group, event 0 starts | Event is blocked. |
| Meeting is also added to the stopping set, event 0 starts | Event is still blocked in this filter pass while the held claim remains. |
| Meeting's actual held claim is removed, then event 0 starts | Event becomes selectable. |
| Meeting released, departure 99 and event 0 both start | Native departure wins; releasing the meeting does not suspend native priorities. |
| Event 0 inserted before meeting 100 with no holder | Native filter still chooses meeting 100, confirming priority sorting rather than insertion-order selection. |

The claim lifecycle assertions additionally confirm that native `AddToPlaying` records the exact selected blueprint object.
Calling `RemoveFromPlaying` for an old meeting after a different event has taken ownership preserves that replacement holder.
The exact original departure object can regain the group, and the same meeting object can later be selected and regain it again.
Neither fixture fact is marked completed by these claim operations.
This is identity of etude claims, not preservation or transfer of a saved Irabeth actor.

## Release timing matters

The native filter does not make a scheduled stop equivalent to an already released claim.
`SelectPlayingEtudes` performs its filtering before stopping and activating facts.
The probe's scheduled-stop case therefore supports a pending interval rather than an assumption that a lower-priority replacement is selectable in the same pass.
After actual release, a later selection can admit it.
The future implementation must observe the actual holder after native processing and tolerate a pending handover.
It must not set an arrival flag solely because its request condition became false or a stop was scheduled.

Yielding to a native event means relinquishing the authored claim and allowing native arbitration to run.
It does not mean forcing that event to win over another eligible native claim.
In particular, departure 99 still outranks event 0 if both are eligible after release.
Do not complete, clear or artificially suspend the departure to manufacture a preferred winner.

## Full selector and lifecycle boundary

The probe also calls actual `SelectPlayingEtudes` with an empty synthetic activation predicate, no linked campaign restriction and a registered native facts processor.
The call reached one starting fact, `IsActive=true`, `IsPlaying=true` and the expected held meeting blueprint.
That is not complete activation proof.
The detached fixture does not provide the game's history-log lifecycle infrastructure.
A direct diagnostic invocation of the same native `Etude.OnActivate` exposes `NullReferenceException` in `GameHistoryLog.AddMessage1`.
Native `EntityFact.Activate` catches exceptions from activation callbacks, so merely observing its return or an active flag is not enough to establish that the entire callback completed.

The sixteen passing assertions are specifically arbitration and claim tests, not assertions that the full lifecycle succeeded.
The probe reports the full-selector observation and diagnostic boundary separately.
It does not patch the history logger or create a fake successful actor result to turn that limitation into a pass.

Nonempty native activation predicates also have an existing standalone limitation: `ConditionsChecker.Check` enters `ProfileScope.New`, which accesses Unity's `Application.isEditor`.
That boundary was reproduced in the preceding `tirabade-etude-lifecycle-review.md` investigation.
This probe does not certify evaluation of a custom invitation predicate, actual native parent conditions, area transitions, campaign eligibility or save/load.
The starting/stopping sets in the arbitration cases are controlled fixture inputs representing eligibility already determined elsewhere.
Custom-condition withdrawal is therefore a required policy whose native consequence is demonstrated, not an implemented or tested production condition in this probe.

## Concrete implementation consequences

1. Retain the exact reviewed background allowlist and refuse unknown holders before submitting a meeting claim.
   Native priority arithmetic alone demonstrably steals an unknown lower-priority holder.
2. Inspect eligible pending non-background claims as well as the current holder.
   An already held meeting at 100 blocks both equal and lower-priority events unless the authored meeting withdraws.
3. Express withdrawal through the future meeting's native eligibility/lifecycle rather than editing native historical states or performing manual production claim-table writes.
   The fixture's direct claim calls isolate semantics; they are not a production lifecycle shortcut.
4. Poll actual ownership after native updates and allow a pending release/reselection interval.
   A scheduled stop, an active flag and a saved request are individually insufficient arrival evidence.
5. After any new native winner, preserve it and recheck the exact living saved actor, registry, holding state, view and consent before offering physical dialogue.

Priority 100 remains a reasonable candidate for the narrowly audited ordinary-departure case, with these restrictions.
The full production eligibility condition, completed activation, physical repositioning and save/load still need implementation and independent verification.
This probe does not approve Anevia's dangerous departure-trigger interruption, the queen expedition, an Iz alternative, resurrection or cross-area transfer.
