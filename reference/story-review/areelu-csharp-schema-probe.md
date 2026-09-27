# Areelu current C# schema probe

Source SHA-256: `FDA89B9610C6951D0DA975768D4BB64885CA3145D64AEE1F9F99C93FFDE4C70A`.
The source supplies 33 delivered scenes.
This probe used the actual `Rules.Validate` implementation through the existing `RulesTests.dll --bindings` command, not a Python reimplementation.
It does not independently review the whole manuscript or certify a played route.

## Unmodified manuscript result

A temporary JSON fixture contained only the imported scenes and their relationship metadata.
No native bindings, actor evidence or acquisition producers were invented.
Validation failed at `areelu.trickster_opening.the_live_fold` because the physical Areelu scene has no dialogue attachment points.
The manuscript contains thirty physical scenes without explicit attachment lists.
This is a real remaining integration failure, not a passing test.

## Isolated graph and schema result

A separate deep-copied temporary fixture added the clearly synthetic attachment ID `00000000000000000000000000000001` to those thirty scenes.
No manuscript, export or native registry was changed by this fixture.
With that prerequisite isolated, the actual C# validator accepted all scene graphs and check shapes and emitted the fixture's requested attachment list.
That supports the narrow claim that the repaired first-node reachability and choice/check schema are compatible with current validation.
It does not prove a valid native attachment, runtime condition producer, actor availability, chronological delivery, save persistence, ToyBox behavior or story quality.

The temporary fixtures are `C:/Users/Z/.codex/tmp/areelu-schema-fixture.json` and `C:/Users/Z/.codex/tmp/areelu-schema-placeholder-fixture.json`.
Neither belongs in a release or should be registered as game content.
The minimum modeled committed length and campaign timing limitations remain unresolved.
