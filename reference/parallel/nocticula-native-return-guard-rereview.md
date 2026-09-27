# Native return guard delta: independent rereview

The guard changes address the generic safety gaps identified in the preceding engineering review.
I found no regression in the inspected Nocticula return contract or enum comparisons.
This is a source and supplied-test-log review of the guard delta, not execution of the native dialogue lifecycle or approval of authored romance prose.
Only this report was edited.

## Frozen inputs

| File | SHA256 |
| --- | --- |
| `src/Main.cs` | `28F41F461816C721BF14660B4F516C525CE41EED375E7FC1EEE318087B837948` |
| `src/Story.cs` | `0100EF281695F9C0B024B0A2B4BBFF35AB91F96000B8033B6A175278A2D3B0F9` |
| `managed-tests/Program.cs` | `74445AE15D32513D924DC39388EF1B34DA6AB5C71B3569C2F7288ED6F7B00B48` |
| Development DLL reported by positive log | `977068593F40FAB2E6A188522809D1C4BA53DF9E663EF7ACE207FEB06F6E426D` |
| 644-scene living fixture reported by positive log | `15E9CC0392BFD8BFE60EF9EC7BD14B53688CAE8310226CCF5DF2BAEB1836756F` |

I read the changed source and the complete result tails of `C:/Users/Z/.codex/tmp/nocticula-guard-{positive,show-once,list-show-once,experience,alignment,extra-list}.log`.
Those are root-run tests; I did not rerun or rebuild the managed fixture during this delta review.
I independently decompiled the installed game's actual answer-list/base classes and enum definitions to verify the field types and defaults rather than infer them from the passing log.

## Contract now enforced

Schema validation requires exactly one explicit insertion answer list for `NativeReturnCue`.
The earlier rejection of remote/epilogue, contact-unit, hub and revival combinations remains in place.
Build obtains that single list and requires the return cue to reference exactly that one object.
An overlap with one of several insertion targets no longer satisfies the contract.

The preflight rejects cue show-once flags, conditions, OnShow/OnStop actions, Continue, experience and nonzero alignment shift.
It also rejects a show-once answer list, nonempty list conditions, and nondefault mythic/alignment requirements.
These checks still run before creation or attachment of the addon graph.
An invalid return fails initialization rather than publishing an entry that ends or diverts the original audience.

The known native Nocticula cue and list satisfy the stricter contract.
The earlier independent native archive inspection established one matching list, repeatable cue/list behavior, empty conditions/actions/Continue, no experience, zero alignment change and both requirement fields set to `None`.
The strengthened guard does not require changing the original native disclosure, reward or departure edges.

## Actual enums and field loading

Fresh decompilation shows that `BlueprintAnswerBase.MythicRequirement` has type `Kingmaker.DialogSystem.Blueprints.Mythic`.
Its first member is `None`, implicitly zero.
`AlignmentRequirement` has type `Kingmaker.Enums.AlignmentComponent`, whose `None` is explicitly zero.
Therefore `returnList.MythicRequirement != default` and `returnList.AlignmentRequirement != default` correctly reject non-None values for these actual game types.
`DialogExperience.NoExperience` is also zero, while the negative fixture's cast of `1` selects `SmallExperience` rather than another spelling of no experience.

The freshly inspected `BlueprintAnswersList.CanSelect()` checks its ShowOnce history and Conditions.
The mythic/alignment fields are inherited from `BlueprintAnswerBase`; requiring their None values deliberately keeps the new return contract conservative even though this specific list method does not itself read them.
This introduces no restriction on the verified current Nocticula list, which has both None values.

`SeedNativeFields` obtains the real public field and deserializes the archive token into that field's actual type.
Public inherited fields are available through this lookup, so it handles both requirement fields on the answer-list subclass.
It does not silently substitute defaults for missing fields or failed conversion.
The list's ShowOnce, Conditions and requirements, plus the cue's Experience and AlignmentShift, are now copied from actual native JSON.
Existing code copies the other cue fields and resolves reference lists separately.
This avoids whole-blueprint deserialization and its unrelated duplicate serialized-property problem without replacing relevant native state with a blank seed.
The successful positive fixture is evidence that these particular field conversions execute on the installed assembly.

## Negative tests and their limits

The positive log reports **86,652 assertions**, 644 scenes, three inline audience graphs and nine terminal return edges.
Each of the five negative logs reports **943 assertions** and the expected native-return preflight rejection.

- `show-once` sets the native cue's `ShowOnceCurrentDialog`.
- `list-show-once` makes its actual return list nonrepeatable.
- `experience` changes the cue to `SmallExperience`.
- `alignment` sets the cue's alignment-shift value to one.
- `extra-list` duplicates the cue's answer-list reference, making the count two.

The rejection branch checks that initialization stays false, the expected preflight error is recorded, the addon registered-blueprint collection is empty, and the original native answer and sequence reference arrays remain unchanged.
Thus the tests distinguish deliberate early rejection from merely throwing at some later build stage.

The negative cases do not individually exercise nonempty list conditions, non-None mythic/alignment requirements, a single wrong-list reference, or schema rejection of two explicit scene insertion lists.
Those branches are supported by direct source inspection, not falsely reported as covered negative fixtures.
The duplicated-reference test establishes the count guard; it is not a test of selecting between two distinct eligible native lists.
This distinction does not invalidate its purpose, since the new contract forbids either kind of two-list return.

## Scoped verdict

The previously identified return-cue experience/alignment and list eligibility/identity gaps are repaired at schema/preflight level.
The observed tests support preservation of the safe current graph and rejection of representative unsafe inputs before addon mutation.
No additional code defect was demonstrated in this delta.

The preceding report's live journal, camera/dialog execution, interruption, portrait and save/load limits remain unchanged.
These guards prove neither that a player has clicked through the native audience nor that an objective event has been shown and persisted in a real save.
The authored acquisition and concession still require their separate prose, history and route-integration reviews.
