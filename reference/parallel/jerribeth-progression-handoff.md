# Jerribeth progression and settlement handoff

Source released for independent review and a private test stage on 2026-09-25.
No main export, engine, expansion assembly, Program registration, installation, or art was changed by this author.
The new scenes are authored alternate development through the existing correspondence charm.
They do not establish new native encounters or rewrite the game's quest outcomes.

## Frozen files

| File | SHA256 |
| --- | --- |
| `storylines/jerribeth.py` | `FCD94F9865DE3F0E984633E1AB7DC91F59B8BC8D207F7CFEDC43BCEC2722A086` |
| `storylines/jerribeth_consequences.py` | `640EAAFE48F34AB928ED4F3C6676F31CE482F7103A283AC23ECB1581646BD300` |
| `storylines/jerribeth_counteroffer.py` | `B1FCCD1478DC7551DDBF12934E4EDD9B72B06EF6CFE5211DD72B5B4D09802630` |
| `storylines/jerribeth_progression.py` | `5153BEDCF663FD78FF298DE203ED762B87B9BE34D4EE03D04F01D4734B436D80` |
| `tests/JerribethProgressionTests.cs` | `F9568BD451A6B31D8EFC834772DE3923223CE0BA4237CA5F23E5947323F53A75` |

## Reproduced behavior and progression repair

Before editing, a read-only walkthrough entered the actual original future with commission, terms and lovers.
It selected future indices `0,0,0`, ordinary `0,0,2,0`, and farewell `0,0`.
It obtained committed, chosen_future, ordinary, at_ease, farewell and farewell_kept without any purchaser or counteroffer event.
Both expansion modules then forbade further entry because farewell was completed.
This was a reproduction in the authored graph, not a Unity session or a claim of real game execution.

Future now requires commission and either settlement_kept or an explicitly requested short future.
The developed entry requires settlement_kept and reaches the original conversation.
The short entry acknowledges the missing longer visits and grants a modest continuing promise.
Existing scene IDs and the indices of existing choices are preserved.
New first pages change entry routing; no existing scene is deleted.

The original future/end choice now enters future_conclusion.
Only its settlement_kept answer grants developed_future.
Its other answer preserves an earlier promise as short history, including a saved dialogue that resumes at the old end node.
The original positive epilogue/start similarly retains a terminal fallback when resumed without developed_future.
Actual saved Unity dialogue migration still requires testing.

Farewell requires ordinary, future_settled, and either developed_future or short_farewell_requested.
The new manual farewell_review makes a shorter courtship's early farewell explicit.
Declining that review does not change flags, and the automatic rest queue remains free to deliver unfinished visits.
Fresh developed histories can receive farewell automatically.

Old future/ordinary saves keep their flags and timestamps.
They can play the campaign and then promise_revisited, or explicitly retain their smaller promise through manual old_promise and authorize an early farewell.
Reaffirmation can enlarge the promise, keep it modest, end the relationship, or defer without recording a decision.
Keeping it modest completes that decision; it is not a repeatable persuasion prompt.

Old completed farewells stay completed.
Manual another_evening sets catchup_requested only when accepted.
The existing ForbidOverrides mechanism waives only the authored farewell prohibition on missed visits.
It does not waive chapter, area, delay, native unavailability, authored closure, or completed-scene checks.
Commitment, native history and other romances are never cleared.

## Played consequences

Settlement_visit follows counteroffer_kept after 48 hours in Act 5.
Its starting choices read the actual public-account/private-catalogue result.

The public branch brings an adult inspector, Hessa, to Jerribeth's side of the charm.
The paid examination finds an image held briefly to conceal a moving scenery join.
Jerribeth must expose the basin in the design, remove it from the paid work, or withdraw the commission while allowing the report.
The player can be named only as a remote witness, or remain unnamed.
The Commander never certifies unseen construction.

The private branch brings the adult client Cevra, whose desired staircase grows into a request for involuntary guest caricatures and retained likenesses.
The player can propose a disclosed participatory game, fixed fictional comedy, or refusal of the commission.
Accepted alternatives are actually demonstrated and bargained over while she is present.
Refusal loses the advance; it does not make the catalogue useless or promise that no later offer will be considered.
Vardess still possesses the returned working adjustments.
His invitation is evidence of an announced room, not proof that the room is complete or destroyed.

Room_measure follows settlement_visited after 48 hours.
Its six outcome-specific passages show the next negotiation or lost fee and the work Jerribeth can afford.
Serit's first paid section stands in the image; another section requires another payment.
The Commander chooses between a returning street and an inviting terrace, sees the corresponding illusion played, and can share imagined desire or quiet company.
Neither choice creates a physical passage through the charm.
Its terminal settlement_kept is earned by playing this scene, not supplied by a elapsed-time alias.

The public/private costs are recalled by the developed ordinary and ascended endings.
Earlier promises retain a positive but explicitly unfinished history instead of silently inheriting developed text.
The existing separate closed, unfinished and Aeon epilogues remain otherwise unchanged.

## Integration hooks

Append `jerribeth_progression.SCENES` after the existing counteroffer module.
Replace the three existing Jerribeth modules' scene dictionaries with these reviewed revisions when building the private stage.
Register `JerribethProgressionTests.Run(story, Check)` only in a stage containing the new scenes.
Existing whole-campaign selection should use production Rules.NextRemote or exclude ManualOnly entries.
Manual parting remains ManualOnly and keeps its relationship-preserving abort.

| New ID suffix | Entry requirements beyond commission, terms, lovers | Delivery |
| --- | --- | --- |
| settlement_visit | counteroffer_kept; Act 5; 48-hour delay | Automatic |
| room_measure | settlement_visited; Act 5; 48-hour delay | Automatic |
| short_invitation | Before future and settlement_kept; Act 5 | Manual |
| promise_revisited | future, committed, settlement_kept; no developed_future; Act 5; 24-hour delay | Automatic |
| old_promise | future, committed; no future_settled or settlement_kept; Act 5 | Manual |
| farewell_review | ordinary, committed, future_settled; no developed_future, short_farewell_requested or catchup_requested; Act 5 | Manual |
| another_evening | farewell, committed; no catchup_requested; Act 5 | Manual |

Another_evening uses its own direct scene definition and does not require the three shared prerequisites in the table heading.
The other six definitions forbid farewell and narrowly override it with catchup_requested.
All five consequences scenes and all six counteroffer scenes gain the same override.
No engine modification is required.
The future scene's 24-hour delay still dates from commission because the readiness alternatives are RequiresAny, which does not supply a delay timestamp.
The two new substantial scenes have actual positive predecessor requirements and therefore enforce their specified delays.

No new rolls were invented.
The existing real Perception DC 25 check, its failure and non-roll alternative remain in counterfeit_hinge.
The new inspection and commission decisions depend on the visible work and what the player is willing to sell or forgo; a skill roll does not purchase affection or substitute for those decisions.
No physical actor, inventory, currency or placed-event integration is claimed for this book-delivered authored material.

## Verification and limits

All four source modules import under Python with bytecode disabled.
Node IDs and direct targets were checked for uniqueness and existence.
A source walkthrough exercised 24 representative full authored chains across six settlement outcomes and fresh, old committed, old farewell, and explicit short histories.
It reached every node in both substantial new scenes and retained unrelated romance history.
Later farewell and saved-node guards were checked by four additional coherent fresh chains through the final farewell.
These walkthroughs do not replace the actual Rules tests.

The focused C# file covers real Rules.Available and Rules.NextRemote, actual core and campaign choices, failed/successful/non-roll counteroffer evidence, both Serit agreement dispositions, all six settlement outcomes, delays, chapter and area gates, catch-up acceptance/refusal, legacy promises, closure, native unavailability, ending exclusivity and unrelated romances.
It was delivered for parent registration and execution; no C# pass is claimed in this handoff.
A temporary coverage assertion attached to only four shortest/longer sample paths did not cover all six narrative outcomes, as expected from that restricted sample.
The separate 24-chain walkthrough did cover all new narrative nodes.

Four independently reported joins were corrected before this freeze.
The shared private-cost reply no longer answers only the accepted-commission remark, the cleared-table callback uses climbers present in both histories, quiet intimacy introduces its own lamp, and the public ending does not invent a creative payoff after refusing the commission.
These corrections changed prose only, with source imports and targets rechecked afterward.

The project inventory function reports 24,796 raw words, 24,385 distinct-segment words, 21,172 prose words and 3,624 choice words across 36 entries.
The new module accounts for 5,740 distinct-segment words, of which 5,042 are prose and 698 are choices.
The seven entries include migration and manual decision scenes, not seven sequential romance meetings.
Four representative 21-meeting fresh schedules select 11,285 to 13,037 words, excluding epilogues and unused answers.
The two new substantial scenes account for 1,898 to 2,128 selected words in those schedules.
These are local shorter/longer samples, not exhaustive global bounds.

The volume floor is crossed arithmetically.
Meaningful length, assembled fidelity, literary quality, gameplay enjoyment, art, ToyBox coexistence in the actual game and saved-game behavior remain separate requirements.
No score or full-route approval is assigned by the author.
The separate `reference/story-review/jerribeth-progression-review.md` records the independent review of these final hashes, with bounded writing and character assessments of 92 each.
That contribution review is not a new assembled full-route approval.
An attainable native Trickster fate intervention is still not implemented by the original fate_terms dialogue.
The correspondence remains remote; the shared engine's null ContactUnit continuation limitation is unchanged.
Aeon ending availability is unchanged and should remain part of native-history review.

## Sources and factual boundary

The principal defect and scope source is `reference/story-review/jerribeth-assembled-readiness-20260925.md`.
Character, charm, negotiation and settlement continuity were checked against the actual three authored Jerribeth modules, including counterfeit_audience, counterfeit_spoil and counterfeit_after.
Hessa, Cevra, the inspection, commissions, scenery and private future are new authored events.
Jerribeth's insectile form, antennae, delicate hands and high mental voice follow the established characterization evidence summarized by the assembled audit and used by the existing route.
The adult elven disguise is not recast as her native species.
The core refuge sentence explicitly stating Vellexia's death was removed during this revision as a conservative wording change.
Later direct native research corrected the original rationale: patron_lost actually binds VellexiaKilled and does establish Vellexia's death, while the resulting Jerribeth departure does not establish Jerribeth's death.
The exact native record and departure actions are documented in `reference/canon-review/jerribeth-fate-native-evidence.md`.
No native resurrection, redeemed allegiance, universal mind-reading, restored contact, or consent from an absent third party is inferred.
