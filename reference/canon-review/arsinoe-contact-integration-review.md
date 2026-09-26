# Arsinoe staged contact integration review

No source-level blocker was found in the bounded capital contact and temporary ceremony suppression integration.
This verdict covers the five staged opening scenes and the existing engine paths they use.
It does not approve the full route, actual Unity behavior, artwork, or save/ToyBox compatibility.
I did not author these scenes and changed only this review.
The parent owns production tests and integration.

## Exact reviewed revisions

| File | SHA256 |
| --- | --- |
| `storylines/arsinoe_opening.py` | `996CE4772C1A9A74663C40E77139D5B7F950F82705902BD55535471248A2071B` |
| `development/arsinoe-integration-review.json` | `0DD8BDE840E1E128B7EAD5F92C70CFDFAC91C77AE46FC693D0C704BAD8318C13` |
| `reference/canon-review/arsinoe-contact-native-records.json` | `2CC80B5409A950654BF0B514F6BFA77E2CC68B487E6573942DA6EAB7D4EFF8A6` |
| `src/Story.cs` | `FDC3D586E51A99B501B47562500D82E597A6C6624CD26077E3D3BCBAE6058B19` |
| `src/NativeContact.cs` | `27E573ECFB994609730B265646EA7B6D4AFFC47B394A50B6D6BB2287D0FA957D` |
| `src/Main.cs` | `8DECA7B215868CAA7BA48B8665885F9B3F8D82B178D3CD10B132E202F0EF1819` |

Read-only Python imports used `-B`.
I compared the staged Arsinoe scenes, relationship and ETUDES with the actual author module and found exact equality.
I also compared all three native records' Data objects against the installed game's `blueprints.zip`; all matched.
I did not run the production suites; the parent's subsequent results are recorded separately below.

## Native predicates

`Arsinoe_Capital`, GUID `3f3fbb973a4ffee47956b4c7714c939a`, is a native BlueprintEtude linked to Drezen with area parts included.
Its play trigger unhides the named Arsinoe spawner and translocates it to ArsinoePosition.
Requiring that etude to be Playing provides a native capital-role condition rather than inferring availability from chapter alone.
This does not itself prove a usable live actor, so the separate ContactUnit check remains necessary.

`Arsinoe_Dialogue_Conditions`, GUID `c4fa13c72fc350d4bae7431242eb095a`, is a ConditionsHolder with one AND condition.
That condition is EtudeStatus for `VictimsRevived`, GUID `6d3fb96f9b60c0449a01add4be5c4a49`, with Playing=true and Not=true.
NotStarted, Started, CompletionInProgress and Completed are false.
The staged integration therefore matches the condition with temporary suppression while that etude is Playing.
It does not interpret the etude's name as proof that Arsinoe herself died or was resurrected.

Both aliases are ordinary ETUDES entries, absent from PermanentEtudes.
Neither name matches the engine's automatic permanent-state suffixes or special cases.
`Main.State` adds them only when GetFact(...).IsPlaying is true.
Completion does not make either alias persist in the snapshot.
This preserves the native distinction between currently active ceremony state and historical completion.

The installed archive also confirms the requested contact GUID `a609ed9b2205d034bb3bb04d2a255681` is Arsinoe's BlueprintUnit.
The attachment GUID `ecaf5cfe8087a4f45a2269974f4885c9` is `NPC_Common/VendorArsinoe/AnswersList_0004`, a BlueprintAnswersList.
The documented vendor dialogue `d5adc0bbbad5f054098b527cf9cc64f1` is a BlueprintDialog.
These are existing vendor assets, not a claimed new companion dialogue or a resurrection scene.

## Temporary unavailability and entry

UnavailableFlags contains `arsinoe.victims_revived`, `swarm` and `true_lich`.
FailureFlags is explicitly empty.
`Main.Update` fails started objectives only for FailureFlags, so the ceremony flag cannot permanently fail the relationship objective through that path.
UnavailableFlags restrict contact without setting ClosedFlag or deleting authored progress.
When the native ceremony condition ends, later entry can resume if capital, actor and other scene requirements are satisfied.

Every scene requires `arsinoe.capital`, permits only chapters 3 and 5, restricts area to Drezen, and has the correct ContactUnit.
All use the existing vendor answer list and forbid `arsinoe.closed`.
The initial scene has zero delay; later scenes add the appropriate authored prerequisite and a 24/48/72-hour delay.
The integration uses existing schema fields and ordinary etude bindings; it does not require a ConditionsHolder evaluator or another schema extension.

`Rules.Available` checks the scene's chapter, area, completion state, required/forbidden flags, live contact and relationship unavailability before permitting entry.
The injected answer checks this both in ShowConditions and SelectConditions.
Its Start action checks again before Queue.
The queued start waits for no active or scheduled dialogue, no combat, and Default game mode, then rechecks Rules.Available with a fresh State before opening the book.
A pending scene is also canceled when its Player instance changes.
This is stronger than relying on the native vendor option having been visible at the time of the initial click.

## Live actor and continuation

NativeContact requires a loaded area, Player, conscious Commander and no player combat.
It finds the exact blueprint in Game.State.Units and refuses an absent or ambiguous match.
The selected actor must not be destroyed, marked for destruction or disposed.
It must belong to a loaded holding scene and the current LoadedAreaState.AllEntityData collection.
It must be in game, unsuppressed, conscious, neither dead nor finally dead, and not hostile to the Commander.
It does not invoke DialogSpeaker.GetEntity, spawn an actor, revive a unit, change faction or advance a native quest.
The blueprint-level identity is deliberately conservative: two active matching actors block contact rather than choosing one arbitrarily.

Because ContactUnit is non-null, each book choice receives Continuation context.
ContactAvailable rechecks the live actor, chapter, area, all scene Requires and the relationship's UnavailableFlags.
Consequently loss of capital Playing or onset of VictimsRevived Playing suppresses continuation as well as initial entry.
Choice visibility, selection and action each use the continuation predicate.
The Knowledge World check cue also receives the predicate, preventing a stale answer from selecting an otherwise unguarded roll cue.

Each page receives a stable named contact_lost exit when contact becomes unavailable.
That exit has no authored effect or scene-completion action, so interruption does not mark the unfinished scene completed.
The exit's selection remains unrestricted after it has been shown, which allows it to close safely even if contact returns before the click.
ContactAvailable intentionally does not reapply completed-scene, closure or delay conditions mid-conversation, allowing an authored closing answer and its goodbye to finish.
No temporary ceremony state is treated as an authored breakup.

## Remaining bounded verification

The parent should exercise absent/present capital, VictimsRevived Playing versus completed/dormant, each physical contact refusal, queued suppression, both check outcomes and contact_lost exit construction in the production suites.
The empty FailureFlags behavior should be asserted separately from ordinary unavailable entry.
The already completed read-only comparisons establish staging consistency and native record fidelity, not the execution of those C# paths.

Native cue selection and later cue execution still have a scheduling interval.
The existing guard does not prove that a cue already scheduled before contact loss will never display its prose or execute a roll.
Actual interruption during ceremony ownership, chapter/area changes and save/load remains an in-game verification requirement.
Previously recorded choice effects survive an interrupted scene; the flag-free exit does not promise transactional rollback.
Same-save branch replay and native outcome history should therefore be checked in the existing save suite and game.

The predicate does not evaluate arbitrary cutscene ownership, distance to Arsinoe, every possible ceremony, or an exact spawner identity.
The verified native ConditionsHolder supplies only the VictimsRevived condition discussed above.
The present Idle gate and native actor restrictions support the bounded vendor integration, but should not be advertised as proof that every Lann, Seelah or other quest interaction has been exhaustively covered.
The staged module still accurately leaves live interaction verification and optional quest-history bindings pending.

The opening's character-specific mythic policy and attainable Trickster access remain separate route work.
Their incompleteness is not a blocker to reviewing this narrowly scoped capital/ceremony contact change.
No full-route, literary, art, ToyBox or runtime approval is inferred from this technical verdict.

## Parent verification supplied after source review

The parent reports that the exact staged hash `0DD8BDE840E1E128B7EAD5F92C70CFDFAC91C77AE46FC693D0C704BAD8318C13` passed 3,232,840 production-rules assertions.
The reported coverage includes the actual five-scene Arsinoe paths, temporary restriction and restoration of availability, both roll outcomes, and friendship/slow paths without a kiss.
The parent also reports 311 native binding uses against 66 typed targets and 22,367 managed construction assertions over 6,785 blueprints.
These are parent-executed results, not independently rerun measurements by this reviewer.
They supplement the static review without proving native dice execution, Unity contact/interruption behavior, save round trips, ToyBox or artwork.
The staged payload had not been promoted when these results were supplied.
