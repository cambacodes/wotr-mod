# Tirabade progression handoff

This work gates the developed final watch and endings on actual shared-campaign completion while preserving a deliberate shorter course and an opt-in continuation for old saves.
The parent owns assembly, `expansion.py`, `tests/Program.cs`, production exports, engine code and installation.
No child agents were spawned and no installed files were changed.
The standalone `story.py` remains unchanged and still returns its original 34 scenes.

## Reproduction

The first `TirabadeProgressionTests.Run` played the existing `future` conversation using `Program.Walk`, selected commitment, advanced time and asked `Rules.Available` whether `last_watch` could bypass the developed chain.
The parent ran the test against the unchanged 213-scene after-roads stage and reported the expected failure: `Original future and elapsed time bypass the entire developed Tirabade campaign.`
This reproduced the player's ability to select the final-watch conversation and thereby forbid later optional scenes.
The Tirabade dates are physical dialogue entries, so this is not the remote automatic-rest queue defect found in Kiana.
The revised tests check actual `Rules.NextRemote` separately.
An additional focused probe reproduced `Tirabade continuation bypasses loss: three_locks` against staged SHA256 `589BD36FD24383ED2A83387AC484BEBA31136665F473AFC9789682F25D6C8B02` before its fix.
The first two optional scenes now explicitly forbid loss, inhuman states and either wife's absence, as well as closure and the completed final watch.
This matches the remaining shared chain and covers derived loss from sacrifice as well as the relationship's native death/gone restrictions.

## Assembly contract

Append `tirabade_progression.SCENES` after the existing Tirabade modules, including `tirabade_after_roads.SCENES`.
Then call `tirabade_progression.integrate(payload)` on the expansion payload.
The overlay verifies that its required scenes exist before changing the exact original IDs it owns.
It adds `RequiresAny` to `last_watch`, requiring either `three_progression.developed` or `three_progression.short_chosen`.
It adds `three_progression.developed` to the existing `ending_together` and `ending_ascend` requirements.
It also excludes derived `ascended` from `ending_together`, making its normal-versus-ascended distinction agree with the fallback pair.
It does not alter any original page, choice index, completion ID, commitment flag, or native reference.
Keeping this overlay expansion-only prevents the standalone 34-scene package from referencing undeclared expansion flags.

## Played decisions and old saves

`three_choose_days` becomes available in chapter 5 after `future`, `committed` and `kept_terms`, with a 24-hour delay and Drezen location restriction.
It offers continued shared days, deferral, or a confirmed shorter course.
Continued days and deferral both leave the scene replayable without writing history; it is a physical dialogue choice and does not enter the rest queue.
The shorter course states that the remaining shared Drezen conversations will be unfinished when the player completes the final watch.
Only confirming that explanation writes `three_progression.short_chosen` and completes the decision.
It does not claim developed-route credit or reset any earlier choice.

`three_more_days` is a physical opt-in after an already completed `last_watch` and the earlier mutual commitment.
Deferral changes nothing; acceptance writes only the new catch-up choice and scene completion.
The original goodbye, timestamp, promise and relationship history remain intact.
It applies to old installed 34-scene saves, partially played expansion saves, and a shorter-course player who later chooses to use remaining time in Drezen.

All 20 optional shared scenes have `ForbidOverrides` mapping only `last_watch` to `three_progression.catchup_requested`.
The first two previously lacked a final-watch restriction; they now require the same explicit catch-up rather than silently reopening only the beginning of a blocked chain.
No completed scene is reset or replayed.
The actual prerequisite chain determines the next unplayed conversation, including both independent-wife orders.
The override never removes native unavailability, closure, chapter, area or delay requirements.

`three_kept_days` requires actual `three_rooms_unlocked.kept`, the earlier future conversation and commitment, then waits 24 hours.
Old final-watch saves require the same explicit catch-up to access this capstone even if they already completed the optional chain.
The wives discuss their own wishes, acknowledge that the theft was not wholly solved, and confirm the existing promise through the days actually played.
Completion writes `three_progression.developed`.
No particular intimacy, evidence result, refund, coat preference, disclosure or wife order is required.
The original `parting` conversation remains available under its existing rules; the capstone does not remove that choice.

## Ending history

The original developed normal and ascension endings require the played capstone.
New `ending_promised` and `ending_ascend_promised` cover committed histories without it, including an old installed save which declines catch-up.
They describe an earlier promise and an unfinished shared future, without inventing the expanded household development.
The fallback and developed pairs are mutually exclusive by the developed flag.
The original loss, separation, unfinished-affair, monster and Aeon histories are preserved.
The wives remain married throughout the continuing histories.
No choice changes another romance, imposes exclusivity, edits ToyBox settings or fabricates a native restoration.

## Verification scope

The focused test plays the original pre-watch route from a chapter-5 start rather than granting all new prerequisites.
It exercises both individual-wife orders, both earlier theft histories, all three evidence methods/outcomes and the new continuation's walk, rest and intimacy endings.
Old-save checkpoints cover no optional expansion progress, completion of the first campaign extension, and completion of all 20 optional scenes before the new capstone existed.
The test checks native and authored blockers, missing predecessors, chapter, area, delay, history preservation, optional deferrals, shorter-course warnings, catch-up, final-watch replay prevention, and unique normal/ascended/Aeon endings.
The parent registers and runs the focused test through `--tirabade-progression` before broad route suites.
The parent reports that the corrected 218-scene stage, SHA256 `18DD1403CE589B67A35416322E0E9FC95E25140A059A9FE4AB1AFA473EDDA0A9`, passed 8,209,712 rules assertions, including the focused progression tests.
The same stage passed 339 bindings across 62 typed targets and 25,063 managed assertions over 7,587 constructed blueprints.
These are parent-executed results, not an additional execution by the author.
The parent's original-only campaign simulation now explicitly chooses the shorter course and expects provisional endings; it does not manufacture a developed-history flag.
Independent technical review remains pending at this handoff freeze.

The work does not implement a live contact predicate for the existing Tirabade scenes, physical map NPCs, currency, inventory, skill-roll scheduling changes, resurrection, or new mythic rescue routes.
Headless rules and managed construction cannot establish actual Unity dialogue delivery, old save persistence, UI, artwork or ToyBox behavior.
The earlier after-roads contribution passed a bounded independent 92 writing / 92 canon review.
The new progression source `B024938B` received a separate bounded independent 91 writing / 92 canon review in `reference/story-review/tirabade-progression-review.md`.
That review corrected the ascended fallback opening so that a player who completed the shared campaign but has not played the new capstone does not lose credit for days actually lived.
Neither review approves the assembled full route, artwork, runtime delivery or all release requirements.
The new five-scene module contains 1,252 raw and 1,251 exact-normalized distinct words, including both fallback endings.

## Frozen files

| File | SHA256 |
| --- | --- |
| `story.py`, unchanged | `5E8B5914C6CD47841C4CD4D899D90BBF06C14A948702E8BDBC46BE7EF91788F1` |
| `storylines/tirabade_later.py` | `3384D72ADFD38C47EA3055888CF4737C4385D1442B3AC7FF07AD1DF609A30F7D` |
| `storylines/tirabade_campaign.py` | `C4E46EF1FEDF08BD32C7994ED10E36100227EB8B1D941B8B9F7EAEABD3266A8E` |
| `storylines/tirabade_reckoning.py` | `6F2C0C2F0846684145860D317FDBD2EA0CEB683E94706AD42884954CE02D58EB` |
| `storylines/tirabade_after_roads.py` | `0BED9353DAAA9E79BA4DFB063979ECC03D41C4808200BCC29B366A7901A14FD3` |
| `storylines/tirabade_progression.py` | `B024938B7DE09ED29D0B05B39A3B3A8F334BA9DADAFF3444B1A5C318A92B50D3` |
| `tests/TirabadeProgressionTests.cs` | `1B13E61C6796F041022C9F6B118A5C1AA2183D7115D2EBB0D797AE33A8153558` |

Ownership of these files and this handoff is released to the parent.
No further author edits are planned unless a reviewer identifies a concrete correction.
