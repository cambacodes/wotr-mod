# Started-dialog adapter independent review

The inspected adapter correctly exposes native dialogue-start history as a read-only snapshot predicate.
No source-level blocker was identified for this bounded adapter.
It must not be described as evidence that a dialogue finished, a council decision was made or a quest was completed.
The separate authored-epilogue transition defect is outside this verdict.

## Inspected revisions

| File | SHA256 |
| --- | --- |
| `src/Story.cs` | `DD6B591E40FEDD2EAF6BACD4D58E6B86C7BAD50FD80569EBCEECE872C3467F8D` |
| `src/Main.cs` | `BE848D20D5F6EB7F1D41B5748539C74E7602C8594D8C9C62E6A19C7D98A50DCD` |
| `development/started-dialog-review.json` | `78EC5812437B7B6B39A31B547DBA3A2C1122174576309E5D09207C2E0452127F` |

I read the schema, validation, typed blueprint registration and history reader, plus the corresponding managed fixture and binding-audit registration.
I also inspected the saved current native decompilations of DialogSeen, DialogController and DialogState.
The staged adapter fixture contains 230 scenes and binds `fixture.rank8_started` to dialogue `6178470b05c75484085753b821a6a614`.
Only this report was written for the adapter review.

## Native meaning and implementation

The native `DialogSeen.CheckCondition` tests membership in `Game.Instance.Player.Dialog.ShownDialogs`.
The inspected `DialogController` adds the dialogue immediately after scheduling the opening cue and logging that the dialogue started.
It does not wait for finish actions.
`DialogState` marks the ShownDialogs collection for JSON serialization.
These inspected native references support the adapter's deliberately narrow name and comment.

`Story.StartedDialogs` defaults to an empty dictionary, so older payloads omitting the field retain existing behavior.
Build resolves each mapped GUID as a `BlueprintDialog` before attaching authored content.
It stores blueprint references in the same manner as the existing shown-cue and selected-answer adapters.
The history reader adds an alias to the fresh snapshot only when the current player's native ShownDialogs collection contains that blueprint.

The adapter does not set unlockable flags, add native shown-dialogue entries, start a dialogue, alter a faction, complete an etude or write quest history.
The native player history supplies persistence.
Because State creates a fresh snapshot each time, a binding does not remain true simply because another player or earlier snapshot once contained it.
The new adapter introduces no timestamp from which a dialogue completion time could be inferred.

## Validation and guard integrity

Validation requires a nonblank alias and a 32-digit GUID.
It rejects aliases colliding with etudes, completed quests, shown cues, selected answers, completed etudes, authored scene/effect/relationship flags, derived predicates or the reserved `hour.` prefix.
The checks occur before the new native history is used by authored conditions.
Multiple aliases for a single dialogue are not inherently contradictory; the dictionary already ensures each alias has one binding.

The binding audit classifies these targets as `BlueprintDialog`, and managed construction reads and seeds that native type.
The new field is included in the known-condition inventory used by the production test runner.
A scene can therefore require a declared started-dialog alias without disguising it as a cue or completion etude.

ForbidOverrides validation explicitly rejects overriding a StartedDialogs key.
An authored catch-up request cannot thereby erase the observed native-start predicate or selectively bypass a prohibition keyed to it.
The adapter itself changes no availability or ending-order policy.
Whether a particular scene uses the predicate correctly remains a separate review of that scene's conditions and prose.

## Test evidence and limits

The managed fixture invokes the actual private ReadDialogHistory method with a native DialogState instance.
It checks absent history, an unrelated dialogue, the target dialogue present without any completion cue, preservation of native history collections, and removal of the target before a fresh snapshot.
These are meaningful checks of both the narrow positive case and stale-history behavior.
The test does not use a fabricated completion event to satisfy the started predicate.

I inspected those tests but did not run the suite or independently assign an assertion count.
The parent owns current execution and combined-stage results.
An actual Unity save round trip remains separate from the inspected native serialization declaration and managed object checks.

For Konomi or another authored consumer, require a shown conclusion cue or the appropriate native outcome predicate when remembering the final decision.
Use StartedDialogs only where the native condition or prose truly concerns having begun or seen the dialogue.
An interrupted rank-eight meeting may satisfy native DialogSeen while leaving its concluding speech unseen.
The adapter correctly preserves that distinction; it does not decide the political response precedence for the author.

The root's separately reproduced epilogue transition bypass concerns execution of authored ending choices.
Neither this adapter's acceptance nor the fixture's successful history membership can validate that unrelated transition path.
No full-route, epilogue-runtime or save-compatibility approval is inferred from this bounded source review.
