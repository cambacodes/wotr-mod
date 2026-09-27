# Parent ending integration independent review

Independent review completed on 2026-09-26.
Verdict: pass for the frozen managed integration and the supported ordinary ending topology, within the runtime limits below.
No blocking defect remained in the inspected source or independent probes.
This is not approval of a live epilogue, universal mod compatibility or a full character release.

| Frozen artifact | SHA256 |
| --- | --- |
| `src/ParentEndingIntegration.cs` | EF0E00941C620819166C4D791F00986F2EA7A3A71907440D63F26A2015D733F4 |
| `src/Main.cs` | CFF27E813B126B874B1C257224187849D3BFEBB9CEF73D5F971E0224312B2EBA |
| Author's `managed-tests/ParentEndingIntegrationTests.cs` | FD7EA52F11EB4792D29A57E63CCA816555DC098E6DA1444587601DE64060486E |
| Isolated 585-scene candidate | 780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A |

The independent workspace is `C:/Users/Z/AppData/Local/Temp/parent-ending-independent-4e750d82`.
Both isolated projects compiled with zero warnings and errors.
The unmodified author harness passed 71,672 assertions independently.
The final runner with my additional probes passed 71,772 assertions, exited zero and exercised real `Main.Build` for 585 scenes and 20,701 generated blueprints.
The independent production DLL hash is `EF2ADEC42BDB66C0961D530846D13E47BABEC7B2F6AE8857F5DB5579A2EF1FBE`.
The different isolated build path means that binary hash need not equal the author's binary hash; source hashes above were checked directly.

## Reviewer independence and scope

I did not author `ParentEndingIntegration` or the production wiring in `Main.cs`.
I previously reviewed the guard helper and related native integration evidence.
The earlier helper reviews establish their recorded scope only and do not approve this new integration.
This review owns this report and isolated probes, not production sources or shared build outputs.

The new review covers native topology, preparation and attachment order, page observation scopes, action timing, history selection, failure handling and rollback.
Root is separately checking the cue manifest.
Literary approval, art approval, deployed gameplay and every possible third-party patch combination are outside this engineering report.

## Topology, ownership and preservation

The current source treats native pair page `5c95d8e3fa4f3b44896914987cb04b0b` separately through `CueSequence_Special` `f8d7f50e3bb88c143834d234c0b24474`.
It does not incorrectly require that page to be one of the eight RanRomance additions in the ordinary sequence.
It also checks that targeted pages do not occur in the supplied Aeon sequence.

Main prepares bare variants before registration and attaches the shared original behavior only after the generic element-owner pass.
This order avoids assigning original native condition and action owners to the private variants during that pass.
The existing Konomi initialization remains in Main's build sequence.

The inspected native `DialogController.PlayBookPage` executes `page.OnShow.Run()` before enumerating and playing eligible cues.
`CanShowAnyCue` performs a separate preview without running that page action.
The frozen hook refreshes playback after the action boundary and supplies a separate preview scope.
The runner verifies actual Harmony registration on the native methods and inspects the actual native IL boundary.
It applies the same hooks to a small managed playback fixture to exercise their callback timing and lifecycle.
That fixture is not execution of native `DialogController.PlayBookPage`.

Prepare verifies target identity, localization key, page membership, timeline placement, show-once policy and absence of unreviewed per-cue actions, answers, continuation and components.
It rejects changed evidence before original attachment.
The final attachment rechecks checker identity, element counts, original cue references and text keys after registration.
Seventeen private variants retain original behavior references and original checker objects while receiving their own localization keys and guard elements.
The tests check nested original condition owners, original action identity, original cue-reference order, native history policies and repeated attachment.
The four-line Main change leaves the committed Konomi wiring intact.

These checks are not a claim that arbitrary mutations to original conditions after attachment are detected or repaired.
This attachment is a controlled initialization operation.
The cue manifest and its wider literary consequences remain covered by root's separate contract review.

## Observation, timing and failure cases

Playback observation occurs after the original page action returns and before the original cue loop.
Standalone previews refresh once; same-page nested previews reuse the owning scope's selection.
The final `Evaluating` distinction preserves a null snapshot for the entire batch instead of treating null as permission to observe again.
Null or throwing observation falls back to original cue selection and does not establish loss suppression.
The author's null-batch, observer-failure, nested-preview and post-action timing tests passed independently.

The transpiler requires exactly one recognized action boundary and rejects incompatible exception-block placement.
Existing branch labels remain on their original instructions, so a branch that originally skipped the action does not acquire an unintended refresh.
The hook validation and labeled-instruction fixture passed.
Postfix and finalizer cleanup invalidate the owning snapshot and selection.
The finalizer returns the same supplied exception rather than swallowing it.

`RanEpilogue` is explicitly unsupported for replacement delivery.
If Harmony reports that patch owner, observation returns null and records a diagnostic, preserving original parent endings rather than suppressing them for an unverified replacement sequence.
The fallback test passed.
This is a compatibility limitation, not support for that alternate sequence, and it does not establish that addon scenes are delivered there.

## Additional independent probes

My temporary test copy adds 100 assertions beyond the author's frozen suite.
No production or shared test source was modified.

I reused the preflight fixture's deliberately unregistered variant references to force failure inside Attach after original suppression guards had begun attaching.
The failure restored every captured original checker reference and element count, and every captured page cue-reference sequence.
This tests actual rollback after partial mutation, beyond the author's preflight rejection before mutation.
The unused registered/private objects that the production contract permits after failure remain outside native page selection.

I opened two standalone preview scopes for the same page, changed the observed death flags between them, and ended the inner scope.
The outer selected variant and observation count remained stable.
Ending the outer scope twice cleared the selection and left no scopes behind.

I also made a native ActionList fixture action throw before the injected refresh point.
The first version of this probe expected the action's explicit exception, but native error logging in standalone CLR instead raised NullReferenceException because Unity services were absent.
I did not count that first probe run as passing or alter production behavior to hide the boundary.
The corrected probe checks cleanup for the exception actually escaping native ActionList in this environment.
Observation remained uncalled, selection reset to original and the scope list was empty.
A separate direct finalizer probe confirmed reference identity of an explicitly supplied exception and cleanup of its pending scope.
Those checks passed in the final run.

## Native execution limits

The fixture reconstructs extracted parent expressions using actual native condition classes, nested AND/OR structure, negation and GUID references.
It does not execute the installed merged BlueprintCore builders, whose private-field access fails under standalone CLR.
Checker-object preservation and element ownership are verified; populated native condition truth evaluation is not.
The native MarkCuesSeen action graph is preserved by identity, while timing tests use a controlled action that changes the observed fixture state.
Neither should be described as executing the full parent initialization or a native epilogue.

Live `CanShow`, actual native page playback, game save/load, ToyBox behavior, rendered text and alternate cue history across a real epilogue still need in-game verification.
External mods adding downstream checks for an original cue's exact seen GUID are outside the reviewed contract.
The managed pass establishes a concrete, independently exercised implementation to take into those checks; it does not replace them.
