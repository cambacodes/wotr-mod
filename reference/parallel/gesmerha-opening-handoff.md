# Gesmerha recovered opening handoff

Recovered the existing six-scene source without rewriting it on 2026-09-26.
Added focused tests and native provenance in the assigned files only.
The main export and shared engine are unchanged by this worker.

Source SHA256: 97C44235E57D6073EAD45831972CD354E272CECDC50BC6B1A4C744CC92B45426
Tests SHA256: F3AD4A78D2EB152B1E4C70D6888B8755E98222D1AD2624F03D62E637017B1091

## Integration

Import storylines.gesmerha_opening.
Append SCENES, add RELATIONSHIP under gesmerha, merge ETUDES and COMPLETED_QUESTS.
Register GesmerhaOpeningTests.Run only when gesmerha.unbought_work is present.
The generic fixture may need to omit scenes after the first because their conditional prose requires earned history, which the focused chain supplies.
Do not invent all mutually exclusive flags to satisfy those pages.
All scene and choice IDs in the recovered source are preserved.

The scene sequence is unbought_work, along_the_grain, whose_mark, the_first_game, the_unclaimed_hour, against_the_current.
The opening starts without delay; each later visit waits 24 hours after its earned prerequisite.
Each outcome flag is written only on the terminal answer after the associated narrative.
The last visit records opening_kept, not a complete romance or commitment.

## Executed local checks

The isolated temporary C# runner compiled the actual src/Story.cs, src/RecoveryAttempt.cs and project test sources in a separate temporary project.
It called GesmerhaOpeningTests.Run against a generated main-plus-Gesmerha candidate and passed 104,743 focused assertions.
The temporary project is C:/Users/Z/AppData/Local/Temp/gesmerha-check-9ime718k/Check.csproj.
The candidate is the adjacent Story.json.
The command was dotnet run --project <temporary project> -c Release -- <temporary Story.json>.
No shared build output was overwritten.

The existing inventory tokenizer measured 6,952 raw words and 6,930 distinct-segment words across six scenes and 47 pages.
An exhaustive successful-completion source walk across ordinary and Trickster, removed and retained illusions, and chief/Marhevok histories found 4,608 paths with 3,856 to 4,150 selected words.
Those lengths include selected answer text, exclude defer branches, and do not count both skill-check outcomes in one playthrough.
They are opening lengths only and fall well below the 21,000-word full-route planning floor.
No RanRomance full-route parity, assembled approval, quality score or in-game readiness is claimed.

## Remaining work

Request independent writing, characterization and integration review of these exact artifacts.
Run the assembled rules, native-binding and managed-build checks before promotion.
Develop the actual full route, later consequences and credible Trickster access/recovery rather than treating the boat trick as that requirement.
Create and review art preserving Gesmerha's blindness and identifying scars under the current art brief.
Verify runtime portraits, native rolls, actual saves and ToyBox coexistence before declaring the character ready.

## Independent review repairs

Repaired three prose continuity findings after independent review.
The first visit no longer claims Gesmerha sees the Commander watching her knife.
The commercial discussion now folds the parchment by aligning its corners, without treating an unseen ink shield as a tactile edge.
The friendship response recalls the shared outer-row defense from the played game instead of inventing a third-piece error.
A structural comparison against the prior generated candidate confirms that only node Text values changed; IDs, node order, choice order, gates and effects are unchanged.
The focused C# suite was rerun on the revised candidate and again passed 104,743 assertions.
Independent rereview remains required; these repairs are not self-approval.
