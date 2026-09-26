# Konomi private continuation: bounded integration review

No blocking integration defect was found in the three new scenes.
This review covers authored flag flow, export wiring, availability and offline test coverage only.
It does not approve native actor behavior, art, live presentation or the complete route.

## Reviewed revisions

| File | SHA-256 |
| --- | --- |
| `storylines/konomi_private.py` | `E4A570ED6CB6CD5BF4287D04D49E393945915671341C1D4A720E34D94D127EE4` |
| `expansion.py` | `66F20C6D7923C2D32C7B2EAA56A3643B418FFF2AEBF306E0BAE435DD20883E9C` |
| `tests/Program.cs` | `D94D282CC6A6A3F6949EBBBF8BDCD44A752338B3CA8AD8776C9392A8490ADEEE` |
| `development/Story.json` | `AD74301FF6B9D6B2998DF9D38DA8E1288E30B33AAA18A02CECEB61570E1C581D` |

The exporter imports `konomi_private` and extends the scene list with its `SCENES` once.
The reviewed export contains `konomi.carriers`, `konomi.before_road` and `konomi.private_departure` with the expected requirements and effects.
Production rule code is unchanged within this task.

## Availability and state effects

All three scenes are remote books restricted to Drezen in chapters 3 or 5.
They require the native selected dismissal, completed officer state and authored `konomi.reconnection_open`.
They forbid ordinary capital presence, inhuman state, the ordinary farewell and `konomi.private_departed`.
Normal relationship closure also blocks them through the existing production predicate.
They do not independently require current Trickster status because the earlier reconnection establishes access; this permits continuing that established relationship after a path change such as Legend.
The tests explicitly exercise Legend with prior reconnection facts rather than pretending Legend itself creates the opening.

The sequence requires `konomi.private_meeting` before carriers, `konomi.carriers_inspected` before the evening, and both `konomi.before_road_kept` and `konomi.private_letters` before departure.
Each new scene has a 24-hour delay.
Under existing rules, that delay uses the latest timestamp among its required authored facts; the native history facts do not introduce timestamps.
The real completion/choice timestamp from the preceding scene therefore supplies the wait.
Legacy or externally supplied flags without timestamps retain the existing permissive fallback and are not a newly introduced behavior.

The effects are ordinary addon choices, interests, correspondence preferences, scene completions and timestamps.
The evening can set `konomi.attracted` and `konomi.private_interest` on the new mutual-attraction branch.
It does not manufacture `konomi.lovers` or `konomi.committed`, and an existing commitment survives.
Departure records `konomi.private_departed` and `konomi.private_address`; it does not close the romance.
No effect restores presence, changes native dismissal history, restarts the officer etude, changes trade state, or writes another relationship's flags.
Normal journal/start bookkeeping remains part of completion and is not equivalent to restored appointment or physical contact.

Once departed, all three new local-visit scenes are explicitly unavailable even if their individual completion flags are removed.
Earlier private meeting/reply scenes are suppressed by their normal one-time completion in the valid progression that reaches departure.
The ordinary council route remains unavailable while `konomi.present` is false.
No arrival letter or use of `konomi.private_address` is delivered by these three scenes; the departure is a continuation boundary, not an implemented correspondence campaign.
This is a scope limit, not a blocker for the reviewed departure checkpoint.

## Offline test assessment

`CheckKonomiPrivateContinuation` is called when the departure scene exists.
It walks all branches of each scene for chapters 3 and 5 with new, lover and committed histories.
It checks the correct intimate-history branch, the hand-pace prerequisite for a farewell kiss, unchanged relationship stage, preserved native facts and another commitment, postponement without flag writes, one-time completion and departure suppression.
It also removes each prerequisite individually and checks presence, closure, inhuman state, farewell, departure, chapter-four separation and wrong-area blockers.
These are relevant behavioral assertions rather than simple scene-count checks.

The test checks immediate next-scene unavailability after carriers and the evening, then advances 24 hours and requires the next scene to open.
The final test revision also copies the initial state, records the private meeting at hour 1000 and requires carriers to remain unavailable at hour 1023 and become available at hour 1024.
I inspected this addition, which runs for both chapters and all three histories and closes the previously reported first-link timing gap.
The test does not claim actual postdeparture travel, a native actor leaving the city, or a real save/load transition.
Those are not needed to assess the stated offline flag and book-scene integration.

The owner reports 119,933 passing rule assertions for this final test revision.
This audit inspected source, exported records and tests; it did not independently rerun the suite or treat that count as proof of writing quality.
Managed construction and native binding checks were still pending when this review was assigned, so no result for those checks is asserted here.
