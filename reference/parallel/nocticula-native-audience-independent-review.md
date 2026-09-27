# Nocticula native audience bridge: independent engineering review

The scoped three-variant inline bridge passes managed construction and graph review.
Its nine actual terminal edges return to the genuine native audience cue instead of ending that dialog and queuing a book.
A journal-start omission found during review has been repaired in the final source reviewed below.
Actual journal effects, Unity dialogue execution and save/load behavior remain unverified.
This review does not approve my earlier authored acquisition prose.

## Frozen evidence

| File | SHA256 |
| --- | --- |
| `src/Main.cs` | `3A3F6FD232B41C7AAAD36F9D91C49014038CDD8452CC7D868C66B03F4BDCE559` |
| `src/Story.cs` | `ACC7A93C91A51007F2758B7A5CA730D4CE0E1FF189C3AC7B9D52D33AE28F27C0` |
| `tests/Program.cs` | `DD0FEE343205B67D56A5FBA0B4C2E12266C3E514625DB307DCFF95E26D54F90D` |
| `managed-tests/Program.cs` | `A0CBE647C1B41111DA6A140C6A1CAD46F1FD3258CC1EF29B928AB44B27FFDE31` |
| `managed-tests/NativeAudienceTests.cs` | `E293A6B407FA31EC0B0B611AAB916FF424CFDE7DBB9584505FF837DD57FFB4BB` |
| Final tested development DLL | `455EF27ED41BED110B0C23BCFC08F7D9E8EF328AE0B71E1A1CC8797AD8868168` |
| 645-scene construction fixture | `C1F3819367D77FD042B364734214F130B0C9907DAE4038A95D5A5C56A492828A` |

The fixture is `C:/Users/Z/.codex/tmp/nocticula-native-audience-integration.json`.
I read the lifecycle probe and inspected its fresh decompilation of `DialogController`, particularly `SelectAnswer`, `AddAnswers`, `PlayBasicCue` and cue-change action ordering.
I independently reran the native JSON/decompiled-source probe and separately read the actual cue and answer-list fields from the installed archive.
Only this report was edited.

## Native behavior and implementation

`SelectAnswer` runs the chosen answer's actions before selecting its next cue.
An empty next selection calls `StopDialog`, clearing the native context and eventually running its finish actions.
The former queued-book entry therefore could not preserve the original audience simply by telling the reader to return to it.

For `NativeReturnCue` scenes, the new entry has an empty `OnSelect` and directly selects the first registered ordinary cue.
It does not call `RouteAction.Start`, create a replacement book dialog, or write the relationship's started flag at entry.
Local transitions use actual cue references and the existing choice guards/actions.
Terminal acceptance and refusal select the original `20451daada07f744b9d7f3e14a37a864` cue without making that native cue depend on addon availability.
Consequently a terminal flag that hides the addon entry does not also hide its return destination.

The installed return cue is repeatable both globally and within the current dialog.
It has empty conditions, OnShow, OnStop and Continue, `Experience=NoExperience`, and zero alignment shift.
Its sole answer list is `2729c49e2bf20c64caa4f54b352e03f6`.
That list is itself repeatable, has empty conditions and no mythic or alignment requirement.
This last check matters because `AddAnswers` selects the first eligible nested answer list, rather than treating every referenced list as automatically visible.

The existing disclosure answer, response and departure remain native.
The addon does not select disclosure on the player's behalf, start its Council etude, jump to the reward response, or copy the departure teleport and portal actions.
Returning repeats the audience cue's spoken line; it does not repeat a reward or transport action on the inspected native graph.
No code here restarts the original dialog's FirstCue or StartActions.

The native speaker configuration is reused for Nocticula's lines without modifying it.
Other speakers use neutral narration settings rather than impersonating Nocticula.
Common-dialog cues do not automatically inherit the book-page portrait override, so this implementation does not certify scene-art presentation.

## Schema and preflight

`Rules.Validate` rejects malformed return GUIDs, remote/epilogue scenes, contact-unit and interaction-hub combinations, absent explicit answer lists and revival choices for this delivery mode.
The binding inventory now includes return GUIDs as `BlueprintCue` references.
`Build` resolves the native insertion lists and validates all return cues before creating or attaching authored blueprints.
The guard includes `ShowOnceCurrentDialog` and nonempty Continue as well as ordinary repeatability, conditions and actions.
Its position avoids publishing part of an inline graph before discovering an unsafe return cue.

The new API is broader than the one native target verified here.
The generic guard does not check a return cue's alignment effect or experience, nor the selected answer list's ShowOnce/conditions/mythic/alignment gates.
It also requires only one intersection between the cue's referenced lists and the scene's insertion targets.
A future scene with several targets or a conditionally available list could pass that structural guard without returning to the list from which the player entered.
These are concrete validation limits, not a reproduced failure of the current Nocticula target, whose actual fields are safe as described above.
Before reusing the property elsewhere, constrain it to a separately verified native contract or extend the guard and negative tests for those fields.

## Journal omission found and repaired

The initial inline change bypassed the queued `OnUpdate` path that calls `GiveObjective`.
`RecordProgress` initially completed already-started objectives but never created one.
Thus an accepted request would write its actual flags while leaving the journal absent until some later queued remote scene began.
I reported this to root during review.

The final `RecordProgress` now applies the choice effects, obtains the resulting state, and grants a missing objective when that selected choice actually contains the relationship's StartedFlag and the relationship is neither closed nor committed.
It preserves the existing completion logic afterward.
I inspected the actual three audience variants: only the `bounded` and `leverage` accepted terminals write `noct.acq.requested`; the entry and refusal do not.
This makes the repaired initiation condition match the authored acceptance boundary without pretending that merely opening the request accepted it.
Checking objective state `None` also prevents duplicate grants after a repeated effect.

The managed construction suite does not execute `RecordProgress` against a live Player/QuestBook.
Its setup supplies native blueprint/cache objects, not the running game singleton and complete player services that `State()` and the journal action require.
I did not replace those services with guessed stand-ins and claim an executed quest test.
The final journal change is source-reviewed and included in a passing compiled-construction rerun; its actual GiveObjective event/UI/save effects need runtime verification.

## Tests actually run

I independently invoked `ManagedBuildTests.exe` against the 645-scene fixture using the actual installed game assemblies and the three parent-binding manifests.
The final rerun passed **86,696 assertions**, constructed **23,506 blueprints**, checked **three inline scenes and nine terminal return edges**, and passed the existing second-Build idempotence checks.
The final DLL and fixture hashes are pinned above.
An earlier independent run also passed the preceding DLL `1EB94F65CC897EF09B49CA97A5CEAD32EFDDD61A0DDEB1675A8A2BD159CF9201`; that run alone did not include the final journal fix.

The native audience tests inspect entry and choice guards, direct first-node links, absence of replacement book dialogs/pages, empty cue actions and Continue, owner references, selected choice actions, terminal completion behavior and native returns.
The suite preserves the original native answer reference objects and order while adding entries.
The fixture imports actual archive fields for the native return cue instead of treating a blank invented cue as equivalent evidence.
The actual Nocticula request variants contain no checks or Abort choices.
Therefore the helper's check/abort assertions are not evidence that a synthetic inline check or abort path was exercised in this run.
Negative preflight fixtures for unsafe return cues and answer lists were not run in this review.

The test runner also reported its existing unrelated Unity boundaries, including resurrection and meeting scheduling.
Those messages were not swallowed or interpreted as native gameplay success.
The construction fixture includes the separate unimplemented post-conflict preparation; its construction passing does not establish a producer for that scene's lifecycle prerequisite.
Root's distinct living-only rules fixture is the appropriate input for production-oriented acquisition checks, but I did not independently execute that separate full-rules run here.

## Verdict and remaining verification

The inspected Nocticula bridge has no remaining demonstrated cue-graph blocker after the journal source repair.
The scoped native reference, selected-action and terminal return construction is supported by actual managed objects and the real controller's source semantics.
That does not prove execution of a native audience.

An in-game test still needs to enter each eligible history, accept or refuse, return to the original answers, select actual disclosure, observe its response and leave through the normal native departure.
Confirm that journal initiation follows acceptance and not entry/refusal, and that native finish actions occur only at the true exit.
Also check interruption before acceptance, a pre-audience reload, persistence after acceptance, real text/portrait presentation and ToyBox's unavailable-answer behavior.
Neither the successful graph count nor the repaired journal condition certifies those runtime outcomes.
