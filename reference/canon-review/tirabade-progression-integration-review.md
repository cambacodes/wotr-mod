# Tirabade progression integration review

Reviewed independently on 2026-09-25.
The reviewer did not author the progression module, its integration overlay, or the focused test.
Only this report was written.

**Bounded verdict: accepted for integration of the reviewed stage.**
No blocking technical defect was found in its supported fresh, shorter-course, or legacy-save histories.
This is not full-route literary approval, proof of live Unity delivery, or a readiness score.

## Inspected snapshot

The reviewed `development/tirabade-progression-review.json` contains 218 scenes and has SHA256 `18DD1403CE589B67A35416322E0E9FC95E25140A059A9FE4AB1AFA473EDDA0A9`.
The baseline main export inspected during this review contained 207 scenes, SHA256 `70D09CC9150AF3141ECC72C8934FA16A56AF69599701A57017B8C9A60F5EED79`.
The stage includes the six after-roads scenes and five progression entries beyond that baseline.

| Source | SHA256 |
| --- | --- |
| `storylines/tirabade_progression.py` | `B024938B7DE09ED29D0B05B39A3B3A8F334BA9DADAFF3444B1A5C318A92B50D3` |
| `storylines/tirabade_later.py` | `3384D72ADFD38C47EA3055888CF4737C4385D1442B3AC7FF07AD1DF609A30F7D` |
| `storylines/tirabade_campaign.py` | `C4E46EF1FEDF08BD32C7994ED10E36100227EB8B1D941B8B9F7EAEABD3266A8E` |
| `storylines/tirabade_reckoning.py` | `6F2C0C2F0846684145860D317FDBD2EA0CEB683E94706AD42884954CE02D58EB` |
| `storylines/tirabade_after_roads.py` | `0BED9353DAAA9E79BA4DFB063979ECC03D41C4808200BCC29B366A7901A14FD3` |
| `tests/TirabadeProgressionTests.cs` | `1B13E61C6796F041022C9F6B118A5C1AA2183D7115D2EBB0D797AE33A8153558` |

A read-only import and JSON-normalized dictionary comparison matched all 25 scenes in those five modules exactly to the stage.
Every original node and choice in the standalone 34-scene story matched the stage unchanged.
The original metadata differences were limited to the last-watch readiness alternatives and the two developed ending gates, including the normal ending's derived-ascended exclusion.
Existing shared-scene node and choice dictionaries also matched the baseline unchanged.

Calling the integration overlay twice produced the same payload as calling it once.
The actual expansion builder copies the standalone payload before integration.
A separate check confirmed that `make_story()` still returned its unchanged 34-scene payload after applying the overlay to a copy.

## Progression and migration

The former shortcut is closed at scene availability.
Completing the original future conversation and advancing time cannot open last_watch without either the new developed flag or an explicit shorter-course choice.
The developed flag comes from the played capstone after three_rooms_unlocked.kept.
The preceding authored requirements lead through the shared campaign; there is no alternative based only on elapsed time or a particular successful skill check.

The shorter-course decision has a separate confirmation page which identifies the unfinished conversations.
Continuing the shared days or postponing that decision aborts without recording completion or granting the short flag.
These are physical dialogue entries, so replayable decisions do not occupy Rules.NextRemote.
This is distinct from the remote queue problem previously found in other routes.

The older final watch remains recorded, including its timestamp.
It does not silently reopen the optional chain.
Acceptance of three_more_days records catchup_requested and its own scene completion; refusal leaves the state unchanged.
All 20 shared scenes waive only last_watch through that flag.
Completed scenes remain unavailable, so the next unplayed prerequisite determines where a legacy save continues.
The capstone itself also requires opt-in after an old final watch, including a save which had completed all 20 shared scenes before this new capstone existed.

The repaired three_locks and three_outing explicitly forbid closed, loss, inhuman, and both away flags as well as last_watch.
Their reviewed stage definitions contain the correction that was absent in the earlier red stage.
The other continuing scenes retain their equivalent guards.
ForbidOverrides does not bypass relationship death, disappearance, swarm, or true-lich unavailability, chapter and location restrictions, required predecessors, or delays.

The capstone reaffirms an existing mutual commitment rather than creating that commitment from a partial affair.
Its requirement does not demand a particular intimate ending, wife order, evidence result, financial result, or disclosure choice.
Deferral gives no developed credit.
The original parting conversation remains available under its existing rules.

## Ending and native-state checks

The ordinary and ascension ending pairs are exclusive on three_progression.developed.
An earlier committed save that declines catch-up receives a promised-history ending, rather than losing its promise or inheriting unplayed household development.
The original loss, separation, unfinished-affair, monster and Aeon entries are not replaced.

In addition to the C# tests, a read-only predicate check exercised 16 combinations across developed and undeveloped commitment.
For each history, ordinary, ascended, dead, gone, sacrifice, swarm, true-lich and closed states selected exactly one ordinary epilogue.
Native outcomes were supplied with their actual derived flags, such as sacrifice with loss and true_lich with inhuman.
Impossible simultaneous mythic endings created by external flag editing were not treated as supported campaign histories.

Etude, completed-etude, quest, selected-answer, seen-cue, relationship and revival dictionaries exactly match the inspected main export.
The new choices add authored progression flags and do not alter native marriage, quest, death, departure, mythic or companion flags.
The focused test preserves the existing affair and mutual-promise flags and unrelated Seelah and Arueshalae commitments.
No exclusivity rule or ToyBox setting is introduced.
This verifies authored state coexistence; it does not establish actual ToyBox behavior in a running game.

## Executed verification

I independently ran the existing compiled test runner against the frozen stage:

```text
RulesTests.dll --tirabade-progression development/tirabade-progression-review.json
PASS: 8,209,712 assertions
```

The focused test runs before the original campaign suite.
It plays the original pre-watch route through actual choices and then exercises 12 continuation histories combining both wife orders, three evidence/outcome profiles, and fresh versus historical final-watch states.
Historical checkpoints cover no expansion progress, the first eight shared scenes, and all 20 shared scenes before the capstone.
It also exercises the separate explicit shorter-course path.
The checkpoint/profile combinations are representative cases, not the full Cartesian product of every earlier narrative choice.
All newly authored progression pages are visited by the focused test.

Availability checks include positive prerequisites, one-at-a-time predecessor removal, delay boundaries, chapter and area restrictions, native and authored blockers, old-watch preservation, deferral behavior, capstone gating and ending exclusivity.
Program's original-only campaign now selects the actual shorter-course answer rather than manufacturing its readiness flag.
The normal campaign expectation changes to the promised ending accordingly.
At the inspected Program revision, the focused test is registered through the explicit command-line option; the parent will register automatic execution for an integrated payload containing the capstone.

The parent separately reported 339 bindings with 62 typed targets and 25,063 managed assertions constructing 7,587 blueprints for this exact stage hash.
Those two results were not rerun by this reviewer and are reported as parent-run evidence.

## Remaining limits

Rules tests exercise snapshots and authored transitions, not loading a historical Unity save into the revised assembly.
They cannot prove current-dialogue save migration, scene presentation, physical NPC availability, portraits, camera behavior, UI quality or real-time skill-roll scheduling.
The unchanged null-ContactUnit continuation behavior remains a shared-engine limitation; the reviewed work does not claim a new live actor predicate.

The catch-up route requires the living, available wives and the existing mutual promise.
It does not resurrect either woman, repair an ended relationship, override an incompatible mythic outcome, or manufacture missing native contact.
Those restrictions are intentional and are not failures of the reviewed migration.

The separate literary review owns its writing and characterization assessments.
This report assigns no score and does not establish the assembled route's 42,000-word quality floor, art readiness, every mythic route, or final release readiness.
Promotion should use these reviewed source hashes and retain the demonstrated focused-test registration.
