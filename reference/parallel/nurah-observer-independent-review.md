# Nurah observer independent review

Reviewed on 2026-09-26.
Verdict: revision required for the prison-completion adapter.
The retained-actor checks passed the focused probes, but the observer can consider imprisonment released before its active native fact has finished.
No production helper, tests, registration, or shared build outputs were changed by this review.

## Frozen inputs

- `src/NurahMeeting.cs`: SHA256 `95B06A61D46158DB64E5BB7E1596CEC04832C196B3921F1CDFA8D55005F4B639`.
- `managed-tests/NurahMeetingTests.cs`: SHA256 `EA0CECDD781E2B28232D19AE29B0B0CB0170CA6D5CD555674DA62780FBBA8EB3`.
- Author scope and source evidence: `reference/parallel/nurah-meeting-handoff.md` and the independently reviewed Nurah binding audit.
- Independent harness and native decompiles: `C:/Users/Z/AppData/Local/Temp/nurah-observer-independent/`.

The isolated harness compiles a copied source snapshot against the installed actual game assemblies.
Its production and test builds completed with zero warnings and errors.
The original 30 assertions and fourteen additional provenance/history assertions passed.
Three further assertions reproduced the defect below, giving 47 assertions in the final reproduction run.
Those three assert the observed faulty state rather than implying that it is acceptable behavior.

## Required correction: completed history is not finished imprisonment

`CorrespondenceAvailable` currently supplies the imprisonment argument as `system.EtudeIsStarted(prison) && !system.EtudeIsCompleted(prison)`.
The fact's current Playing and CompletionInProgress states are not consulted.

Fresh selective decompilation of the installed `Kingmaker.AreaLogic.Etudes.EtudesSystem` establishes the native ordering.
`MarkEtudeCompleted` first writes Completed to its saved state dictionary when a fact exists, then calls `fact.MarkCompleted`.
The latter sets CompletionInProgress and propagates completion to children.
It does not immediately deactivate the fact.
`Etude.FinishCompletion` itself rejects a fact that is still Playing.
Meanwhile, `EtudeIsCompleted` already returns true from the dictionary, and `EtudeIsStarted` returns false because it delegates to the completed query.

The independent reproduction uses actual native EtudesSystem and Etude objects.
It sets the saved prison dictionary entry to Completed and constructs a prison fact that is Playing and CompletionInProgress but not IsCompleted, matching the ordering above.
The exact current adapter expression produces `imprisoned=false`.
With the other positive history prerequisites, the frozen `HistoryPermits` then returns true.
The console records: `REPRODUCED: actual native dictionary Completed + prison fact Playing/CompletionInProgress produces jailed=false and HistoryPermits=true.`

This proves a concrete history-adapter false positive in the native completion interval.
It does not claim a whole Unity visit was spawned or that the full CorrespondenceAvailable entry point was executed headlessly.
The current module is observer-only, so there is no movement side effect to report.
Nevertheless it fails its stated requirement to exclude current imprisonment and should be corrected before its result authorizes an invitation or later movement.

Keep the historical release allowance, but also reject a still-playing or completing prison fact regardless of the already-published completed history.
Test the adapter using the actual native dictionary/fact combination rather than passing a precomputed boolean to HistoryPermits.
The regression should reject pending completion, allow a truly finished release, and continue rejecting started or pending imprisonment.
Romance and personality already inspect fact-level completion; that distinction should also be respected for imprisonment.

## Retained actor and other history checks

The observer resolves exact typed parent/native GUIDs and rejects resolver aliases.
The source-specific inspection delegates to JerribethRecovery's saved provenance checks, then rejects historical spawner death, multiple spawners naming the same actor, and multiple capital-blueprint actors.
The existing suite checks absent actors, never-spawned sources, loaded area, dead/finally dead state, destruction, duplicate scenes and actors, registry replacement, wrong representation, and recovery to the valid witness after rejected observations.

My additional probes reject an actor or spawner whose HoldingState differs, a missing registry entry for either, a retained actor ID without HasSpawned, HasSpawned without an actor ID, a registry-only actor absent from saved storage, and the same actor stored in two scene states.
They verify that rejected observations leave the positive retained witness usable.
Additional history probes reject a completed personality, missing romance, and malformed personality-array length.
No evidence of actor creation, spawner replacement, native history writes, or foreign romance mutation was found in this observer.

The exact saved actor is valid identity evidence even without a Unity view.
That must remain distinct from visible presence, navigable placement, contact, or consent.
The native SceneEntitiesState type records SceneName rather than the scene asset GUID; the observer's current name plus exact source spawner, holding-state, actor identity, and registry agreement is the inspected provenance chain.
The separate SceneAsset constant is supporting source evidence, not an extra runtime GUID check.

Fresh native EtudesSystem inspection also confirms that EtudeIsCompleted includes PreCompleted and that EtudeIsStarted means recorded and not completed, not necessarily currently Playing.
For death histories, the observer's started-or-completed union conservatively excludes recorded death even when the fact is dormant or its parent is not yet active.
For the current romance and exactly one personality, fact-level IsPlaying plus explicit completion exclusions is the relevant narrower requirement.
The actual accepted Book 5 finale is read from shown-cue history rather than inferred from quest completion or a completed romance etude.

## Boundaries retained after correction

The positive full CorrespondenceAvailable path was not run against a real Game singleton, loaded scene, player, EtudesTree, and dialog history.
Its loading/unloading, duplicate saved-area, Commander consciousness/combat, Nurah consciousness/suppression/hostility, and registry APIs were inspected but not collectively exercised as a live entry point.
There is no callback, consent episode, timer, claim arbitration, placement, retry persistence, arrival observation, or Main registration in this stage.
Chapter, mythic path, closure, acceptance, refusal, and delay requirements remain the future caller's responsibility as the handoff states.
The Yaker location investigation is not approval of an empty or available meeting point.
After correcting and independently rechecking the prison transition, this can be approved only as a retained-living-actor observer foundation.
It cannot establish an attainable complete Nurah route, resurrection, physical visit, or manual-play readiness.


## Targeted correction re-review

The original defect and reproduction above remain the verdict for source 95B06.
This section reviews corrected source `723223CE6F6AD0DBF7B19B02DEFC23757FF49314DBF28A9B54050436DDE38DBD` and tests `A69C732F7637B0BB38500B96960FF9C831388C3F617E7CEE2CFDE0B9F55202D8`.

Verdict: pass as an observer-only foundation after the prison adapter correction.
No movement, invitation, arrival, Main integration, or route readiness approval is added by this verdict.

CorrespondenceAvailable now obtains imprisonment through PrisonBlocks using both the actual EtudesTree fact and saved native history.
A retained fact blocks while unfinished, Playing, or CompletionInProgress, regardless of the saved dictionary having already published Completed.
Started or pending recorded imprisonment also blocks when no live fact is available.
Completed history without a retained prison fact and never-imprisoned history remain eligible for the other independent prerequisites.
The actor, romance, personality, finale, and death checks are otherwise unchanged.

The corrected tests build actual EntityFactsManager and EtudesTree objects, insert the prison fact into native fact storage, and verify that GetFact resolves that exact object.
They reproduce the dictionary Completed plus Playing/CompletionInProgress interval through the new adapter instead of substituting a boolean result.
The transition now blocks as required.
They additionally cover deactivated but completing, unfinished dormant, completed but still-playing, started history, missing live fact, fully completed history, and no imprisonment.

I copied the corrected production source and submitted tests into a separate isolated harness at `C:/Users/Z/AppData/Local/Temp/nurah-observer-independent-fixed/`.
I retained the fourteen independent provenance/history checks from the first review alongside the eleven new submitted adapter assertions.
Both production and runner builds complete with zero warnings and errors.
The combined run passes all 55 assertions.
No shared assembly or test output was overwritten.

A further native lifecycle check matters when interpreting the test fixtures.
Freshly decompiled Etude.FinishCompletion sets IsCompleted but does not clear CompletionInProgress.
EtudesTree.MaybeDeactivateCompletedEtudes subsequently removes completed facts and preserves completed history through InternalMarkCompleted.
The representative ordinary released state is therefore the tested completed-history/no-retained-fact case.
The test's retained completed/non-completing fact is an additional permissive consistency case, not a claim that native FinishCompletion creates that exact combination.
Conservatively blocking the still-retained completing fact until cleanup avoids the original early release without permanently blocking the normal cleaned-up state.

The earlier full Game/Unity entry-point, consent, native-claim, placement, and live contact limits remain unchanged.
The corrected observer and its focused tests can proceed to shared managed-runner adoption; later movement work needs its own independent review.
