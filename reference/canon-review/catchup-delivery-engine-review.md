# Catch-up delivery engine independent review

Decision: the inspected engine changes support the intended narrow migration mechanism, with no remaining blocking source-level defect identified after the GUI label correction.
This accepts the shared mechanism, not the unintegrated Seelah/Kiana migration content or a real-game save upgrade.
Only this report was written.
No tests were rerun by this reviewer and no source was changed.

| File | Final inspected SHA256 |
| --- | --- |
| `src/Story.cs` | `E83221EC7D0D6AD23F9073482B08A340D3DBEA4E8137300510415D985E322026` |
| `src/Main.cs` | `3CA9FFA76608B3C344F5C068FBFBE22D9D94B4CBEFDAE4DD24539FA496A6E10B` |
| `tests/ForbidOverrideTests.cs` | `B3666D3638A47EF07ABC7E5D143D87C7EDB3E54447FD613C6653EBE8D33F9D53` |

## Availability and negative guards

`ForbidOverrides` changes the treatment of an individually named scene-level forbidden flag only when its explicitly mapped override flag is present.
An old farewell remains in the snapshot and save; it is not cleared, rewritten or mistaken for an unplayed ending.
Other forbidden flags still reject the scene independently.
Earned prerequisites, alternative prerequisites, chapter, area, completed-scene exclusion, contact checks and delay checks remain in place.
An override cannot replay an already completed scene because `state.Has(scene.Id)` is checked first.

Relationship closure and native unavailability are checked separately after the scene-level flag test.
The new dictionary does not override either of those checks.
The existing narrow recovery exception remains tied to the specific recovery binding and available revival state; a farewell override does not create recovery availability.
The existing epilogue-specific behavior is unchanged and should not be treated as a new general migration path.

Validation requires an overridden key to be in that scene's Forbids and in the authored flag set.
It rejects self-overrides, unknown granting flags, relationship closure keys, native etude/quest/history keys and derived-state keys.
Thus a data author cannot simply mark a native death or mythic alias as an overrideable farewell through this field and pass validation.
Validation is run on the deserialized story before normal initialization.

The dictionary is a trusted authoring facility, not a complete proof of player opt-in.
It allows any existing authored flag as the granting value and does not prove that the value is written only by the intended manual consent choice.
For the concrete migrations, review every writer of `catchup_requested`, ensure no automatic completion grants it, and map only the intended farewell exclusions.
There is no need to expand this small mechanism into a generic policy engine to establish those concrete facts.

## Manual delivery and GUI correction

`NextRemote` selects the first available remote scene while excluding `ManualOnly` scenes.
It continues searching after an excluded scene, so a manual breakup or catch-up offer does not occupy the first position and starve ordinary rest content.
`Main.Update` now calls this helper for the actual rest queue.
This is a production-path change, not merely a helper exercised by tests.

Manual-only scenes remain available to `Rules.Available` and therefore appear in the relationship GUI.
The existing Read button calls `Queue`, whose queued scene is checked again with a fresh snapshot before opening.
An opt-in Read action can consequently launch a manual scene while the rest scheduler cannot choose it.
Validation rejects ManualOnly on non-remote scenes, which keeps the current delivery meaning unambiguous.
The existing Memory-owner shorthand still counts as remote.

I found one presentation defect in the initial Main revision: all remote scenes were labeled "available at your next rest", including scenes deliberately removed from that queue.
The parent changed ManualOnly labels to "choose Read below".
I inspected that correction in the final Main hash above.
The label now directs the player to the actual supported action.
When the game is not idle, the existing conditional button remains hidden; actual busy-state presentation should be included in the eventual GUI check.

## Save and backward compatibility

The new bool defaults to false and the new dictionary defaults to empty.
Existing story payloads that omit the fields therefore retain their previous ordinary remote delivery and forbidden-flag behavior when read by the new engine.
The changes do not rename existing scene IDs, choice indices or saved flags.
`RecordProgress` remains additive and records a timestamp only when a flag is first acquired.
A new catch-up choice can persist an explicit opt-in without resetting the historical farewell timestamp or commitment.

The override flag is not automatically included in the scene delay calculation, which still uses the existing Requires timestamps.
That is appropriate for selectively reopening an old exclusion, but an author who wants a fresh wait after the request must require the request flag or encode another deliberate timing prerequisite.
Do not assume the override dictionary itself starts a new timer.

Deploy the new story metadata and matching engine together.
An older engine does not implement ManualOnly exclusion and cannot be credited with preserving the new delivery contract merely because unknown JSON fields deserialize harmlessly.
Real save/load, queued-dialogue cancellation and native availability changes still need focused in-game verification on an old save.
This source review cannot establish those Unity lifecycle outcomes.

## Test assessment and remaining integration checks

`ForbidOverrideTests.Run` is registered in `tests/Program.cs`.
Its focused fixture verifies denial without the request, availability after opt-in while preserving farewell, normal remote scheduling, manual exclusion, continued manual availability and selection of a later ordinary scene.
It separately verifies another scene objection, relationship closure, native unavailability and a missing prerequisite.
Invalid metadata cases cover an unlisted forbidden key, an unwritten granting flag, self-override, closure and a native etude collision.
These are useful direct assertions about the new behavior.

The fixture deliberately uses a compact synthetic authored flag universe.
It does not prove an attainable opt-in writer, actual Seelah/Kiana predecessor history or proper native contact in the exported campaigns.
The parent reports 8,094,366 rule assertions and 22,154 managed assertions covering 6,741 blueprints before the wording-only GUI correction.
Those are parent-reported checks, not independent execution by this reviewer, and did not yet integrate the staged catch-up scenes.

Concrete integration should verify the following cases without resetting state:

- An old farewell save cannot access the newly reopened optional scenes before explicit opt-in.
- Reading and declining or deferring the manual offer grants no migration flag.
- Accepting it grants only the intended opt-in and preserves farewell, commitment and other-romance state.
- Completed new scenes stay completed; closure, native death/departure, contact, area and chapter restrictions still prevent entry.
- Rest skips the manual breakup and migration offers but continues delivering eligible ordinary content.
- GUI Read opens the intended offer, including after save/load, with accurate wording and real native contact behavior.

There is no source-level reason to withhold the narrow engine mechanism after the label repair.
Keep the complete migration acceptance dependent on those concrete authored histories and runtime checks.
