# Native skill-check integration review

Independent technical review on 2026-09-25 of the new check schema, authoring helper, native construction and test coverage.
This report does not review the author's Seelah prose or approve actual Unity dice rolls.

| Reviewed artifact | SHA256 |
| --- | --- |
| src/Story.cs | `3A9072596CCF3919D1665469F5D7F7BBEE59978D832BBB0DB923318CEC41E3FE` |
| src/Main.cs | `7647E81A3783563D42D1B78AB3217A46805B753F1F374473B2AF433AB51F61ED` |
| story_format.py | `E0C76B1174EB89B91C1696B55CC6BC4398E731129E130A6267AD3A5060F87BC2` |
| tests/SkillCheckTests.cs | `BFC3807E02528204E52FC351DCC704EF6EF1E97A4BF935F541EB1BD7AB8F4B67` |
| tests/Program.cs | `1393F15DEDCD4B99275628D90EB2134E81A91470F8CF7222ED3F22E2F95047C2` |
| managed-tests/Program.cs | `DFC583F13FA3139725B052C0194F5FA757DCD187FFB286B8B0C21AF0AC893CB3` |
| managed-tests/write-check-fixture.py | `0DEC68FC01E11124C830AB14CB053F2A8A7EA654F9D9BEA0939C7BE050DFA98B` |
| development/native-check-fixture.json | `81D1C22868F169B9FD5C15C205226016218BE0D2176BA38867B3B45A5406B985` |
| Built addon DLL | `033D97FA8ABCF9D2F0C069905878F06D88937FF967F7E8C679D926B53CDE798F` |

## Required corrections

### A stale selected check can still roll after contact loss

The selected answer's RouteAction correctly refuses authored progression after contact loss.
However, its BlueprintCheck has unconditional Conditions.
The installed DialogController.SelectAnswer does not re-run CanSelect immediately before invoking OnSelect.
It invokes OnSelect, then independently selects and schedules the answer's NextCue.
Returning early from RouteAction therefore does not cancel the following native roll.
An answer displayed while contact was valid can be clicked after contact becomes invalid, causing a roll and result prose even though the addon action refused its effects.
Result-page choices retain their contact guards, so this defect does not itself bypass the final authored progression check.
It does violate the expected rule that a lost physical contact cannot continue a contact-dependent challenge.

Guard the native check cue's eligibility with current contact continuation conditions, independently of the original choice's attempt flags.
Do not blindly reuse the original choice's Forbids after OnSelect, since an intentional attempt marker can legitimately change that condition before the check.
Verify the actual SelectNextCue behavior when no eligible check remains, including a clean exit rather than an empty stuck page.

### Checks on epilogue choices are silently ignored

Rules.Validate accepts a well-formed Check on a choice inside an Epilogue or AeonEpilogue scene.
BuildScene's epilogue branch instead creates its fixed Continue answer and skips all authored choices, including checks.
The schema therefore accepts a construct that native construction silently drops.
Reject checks on epilogue owners unless a deliberate epilogue mechanic is implemented.
The existing malformed-check tests do not cover this unsupported combination.

## Correct native UI behavior

Do not populate ShowCheck for these visible outcome checks.
The installed BlueprintAnswer.SkillChecksDC getter enumerates answer.NextCue.Cues and discovers each non-hidden BlueprintCheck directly.
It derives the stat, effective DC and roller from that native check.
The installed DialogAnswerView exposes its answer's SkillChecksDC for the normal UI.
Thus a visible BlueprintCheck placed directly in NextCue supplies native check metadata without a separate ShowCheck.

ShowCheck is a different mechanic.
BlueprintAnswer.HasShowCheck tests whether ShowCheck.Type is not Unknown.
CanShow then performs a party check, records that result in DialogState.AnswerChecks and hides the answer on failure.
Adding a ShowCheck would introduce a separate visibility roll, not annotate the existing success/failure check.
Keep the empty ShowCheck created by InitializeAnswer.
No FakeChecks should be fabricated for an actual native roll.
Actual font, tooltip, DC display and actor highlighting remain UI verification tasks.

## Actor selection and outcome handling

The native BlueprintCheck API matches construction in Main.cs: Type, DC, Hidden, BanPartyCheckInCamp, Experience, m_Success, m_Fail and m_UnitEvaluator.
CommanderOnly creates the installed PlayerCharacter evaluator and sets its Owner to the check.
It also sets BanPartyCheckInCamp to true.
The installed PlayCheck passes the evaluator's actor into RuleStatCheck and disables camp party substitution through that flag.

For CommanderOnly false, the evaluator remains null and CharacterSelection's default Clear policy returns null.
DialogController.SelectAnswer updates ActingUnit from that selection before playing the check.
The subsequent PlayCheck therefore uses RulePartyStatCheck, with the native capital-party behavior determined by the dialogue's selection policy.
This is native party selection, not an authored guarantee that only the Commander rolls.
The installed CharacterSelection and PlayCheck were decompiled as small native types/methods during this review.
Uninitialized managed fixture objects do not prove actual stat selection in a loaded party.

Both success and failure reference generated BlueprintBookPage objects.
Installed PlayCheck chooses one outcome and passes it to PlayCue, which supports book pages.
NoExperience avoids awarding repeatable courtship check experience.
Hidden false allows failures as well as successes into native skill-check history.
The supplied native romance examples confirm use of visible BlueprintCheck objects with different native skills and failure targets; they do not establish balancing for these new routes.

Premature scene completion is prevented in construction by requiring both choice.Next and choice.Check to be null before assigning RouteAction.Complete.
The attempted answer can still set declared attempt flags before rolling, which is intentional schema behavior.
Authors must put success-only and failure-only effects on their respective outcome paths, not on the attempted choice's shared Set array.
Ordinary completion occurs on a later terminal outcome choice.

## Validation and save identity

The allowed skills use the installed StatType names, including CheckDiplomacy, CheckBluff and CheckIntimidate rather than generic SkillPersuasion.
Native BlueprintCheck validation itself discourages SkillPersuasion for these dialogue checks.
The schema rejects nonpositive DCs, unknown skills, missing or identical outcome nodes, and combining a check with Next, Abort or Revive.
Rules.NextNodes supplies both outcome edges to reachability and the test walker.
Existing graph reachability validation does not itself reject cycles; the traversal tests remain necessary to catch authored cyclic paths.

Existing answer IDs still derive from scene ID, node ID and original choice index.
Each new native check adds a separate stable check ID using those same inputs.
No checks are injected before existing indexed answers.
Changing an already released choice's type, position or meaning still needs save compatibility review; stable hashing alone does not make semantic changes safe.
This fixture proves construction of new objects, not a saved active-check round trip.

## Evidence limits

SkillCheckTests walks both abstract outcomes and checks unrelated romance preservation, exclusive result flags and malformed specifications.
The managed fixture contains 26 checks: 13 skills under both actor policies.
The managed source asserts native check type/DC, outcome page GUIDs, actor evaluator policy, visibility, no XP and delayed scene completion.
Root reports 18,029 passing managed assertions for that fixture.
This reviewer inspected the fixture and assertions rather than rerunning an unchanged parent-owned build.

Those checks do not execute RuleStatCheck, RulePartyStatCheck, Unity book transitions, a real character's modifiers, native dice, critical outcomes, displayed DC calculations, a game save reload or ToyBox behavior.
The fixture's check scene also has no ContactUnit, so it does not demonstrate the stale-contact case identified above.
After corrections, add focused source/managed coverage for check-cue contact gating and invalid epilogue checks, then retain the real runtime checks as outstanding.
No complete gameplay, route-quality or runtime approval is awarded here.

## Correction rereview

Root corrected both source findings and the revised implementation was independently read.
The initial findings above identify the earlier version; they are not outstanding in the version below.

| Corrected artifact | SHA256 |
| --- | --- |
| src/Story.cs | `FDC3D586E51A99B501B47562500D82E597A6C6624CD26077E3D3BCBAE6058B19` |
| src/Main.cs | `8DECA7B215868CAA7BA48B8665885F9B3F8D82B178D3CD10B132E202F0EF1819` |
| tests/SkillCheckTests.cs | `5257FC8CB4AC70833C28DA287949BE29EFFEB3DBA0F0A1826D4A63BBD23B589F` |
| managed-tests/Program.cs | `AA9E5E4429F0D2B6C7FE2C3C5F2EDFB89BD7CCB281A0C60C85743EF971E61C2D` |
| managed-tests/write-check-fixture.py | `54CBF4C164C53E7FC6EFA88BE59198F40EAD55E99906BE78269D9090245D01D3` |
| development/native-check-fixture.json | `A3B81E3D912A17F6C48268F08BF29711833A8FD89356CB24CB07B2D70624FC7E` |
| Built addon DLL | `44AC3111E4D5625C472773665477C69E701B78BC23CC90E249F73FCD25915461` |

Contact-gated BlueprintCheck objects now carry a Continuation-only RouteCondition.
The condition evaluates ContactAvailable without reapplying attempt-choice flags.
This prevents a stale displayed check from being selected into the next cue after contact loss.
Installed CueSelection.Select calls each cue's CanShow, and BlueprintCueBase.CanShow calls Conditions.Check.
With no eligible cue in this direct book flow, SelectAnswer and ScheduleCue stop the dialog instead of starting the check.
The managed fixture now supplies a ContactUnit and asserts that each check has the expected scene guard, no Choice context and no ContactLost inversion.

Validation now rejects check choices in owners ending with Epilogue.
SkillCheckTests adds rejection cases for both Epilogue and AeonEpilogue.
The original premature-completion and UI conclusions remain unchanged.

One native timing boundary remains explicit.
After selection, ScheduleCue stores m_CueToPlay; a later tick calls PlayCue without repeating CanShow.
The guard therefore establishes current eligibility at cue selection, not immunity to an external state change between scheduling and execution.
Result-page progression still rechecks contact through the existing answer/action guards.
A real contact-removal/save-resume test is needed to characterize that runtime boundary.

No further source blocker was found in this rereview.
Root had started the revised test runs when this report was finalized; this review does not substitute an assumed passing result for their output.
The earlier 18,029-assertion figure belongs to the earlier fixture and must not be presented as the result for the revised hashes.
All Unity, actual stat-roll, UI, save and ToyBox limitations remain outstanding.
