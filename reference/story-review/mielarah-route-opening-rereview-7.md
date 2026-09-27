# Mielarah Route Opening Independent Rereview 7

This rereview checked `storylines/mielarah_route_opening.py` at SHA256 `4592275CF55B760814A21F19B0629620445B637A45B08FE67BA9D8CE9067F689` and `reference/story-review/mielarah-route-opening-development.md` at SHA256 `66D46F23D6BF508E2307DA6CC74889A2AC891658932815B3AA2E433B2DDB32E3` before review.

Both requested hashes matched before review and were rechecked after this report was written.

## Findings

The local module check passes and reports thirteen unregistered scenes and 134 nodes with topology and cross-scene state contracts valid (source lines 1001-1038).

The authoring model checks chapter, delay, `Requires`, and `Forbids` together, then explores cross-scene states through the ordinary and Trickster openings, crew arc, voyage, and endings (source lines 844-998).

This is a meaningful improvement in branch and state coverage, but it tests authored Python contracts and not a registered story export, game scheduler, save, or runtime flag producer.

The prior hand-contact ambiguity is resolved: Mielarah offers her knuckles, and the Commander kisses the back of her hand, matching the specific question and consent (source lines 263-278).

The new later arc now has clear scene links from a completed watch to the crew departure notice and then, if accepted, to the outer shoals (source lines 793-833, 983-993).

The short voyage carries real consequences: crew can leave with wages paid through departure, the crew receives Mielarah's actual terms, her case key is given to a crew member for inspection, and the crew independently refuses coercive magic during a later storm (source lines 797-824).

The outer-shoals choices establish informed refusal, a longer course, extra time at sea, and a lost contract that Mielarah signs for herself; the sailor who refuses the spell is not blamed (source lines 818-824).

The shared-future, deferred, and separation outcomes each have their own reachable flag and consequence, and the local checks confirm all three states (source lines 824-833, 990-993).

One material crew-scene continuity gap remains: `captain_choice` can enter `rule_debate`, then `rule_debate` can proceed directly to `carry_answer` without reaching `crew_voice` or setting `mielarah.opening.jori_answered` (source lines 799, 802-803).

The `carry_answer` node and its subsequent `crew_meeting` text then frame the transition as though Jori's answer has been brought to Mielarah, including her reference to what Jori told her, despite that branch never showing the Commander speaking with him (source lines 801, 804).

Route the branch through Jori's conversation or provide a distinct version of the meeting setup that does not imply the missing exchange, and add a cross-scene/node assertion for the intended history.

The source count is 13,761 raw words including prose and choices, but the report estimates only about 8,158 ordinary and 7,835 Trickster modeled words through the newly extended chain (development report, “Focused checks and measured scope”).

The route remains below the hard 21,000 meaningful-word complete-route floor; these are modeled source sums, not confirmed selected in-game paths.

The manuscript now progresses past initial attraction with the crew's departure decision, wage release, a risky voyage, and three ending outcomes, but it remains an opening contribution rather than a complete route or long-term relationship arc.

Mielarah's voice continues to be blunt, proud, witty, and fallible, with desire emerging alongside resistance to being judged or treated as a prize (source lines 737-743, 797-824).

The continuation does more to dramatize prior themes through money, crew agency, and a lost contract instead of only repeating explanations about consent and rank, though some boundary reminders continue to recur and should remain tied to new decisions and consequences.

Her adult, sensual romance stays consensual and graphic and explicit, with explicit invitations, refusals, room for a player to defer or leave, and her actions controlling physical contact (source lines 769-787, 824-827).

The native dialogue basis remains distinguished from authored expansion: the Tumberd cues evidence her service offer and her own portrayal, while the storm crash and Vazglar death are native outcomes; the intervention, survival, later passage, and new romance scenes remain authored alternates (source lines 12-21, 90-126; development report “Chronology and native evidence”).

The ordinary opening still requires an unimplemented producer for a living, present Mielarah and an exact parent-dialogue hook; the Trickster answer interception and cue suppression remain proposals rather than implemented recovery (source lines 12-21, 90-95, 141-158).

All ten mythic path entries remain explicitly unimplemented; the authored route does not yet provide attainable path-specific contact or all-path recovery for missed, dead, expelled, or otherwise unavailable histories (source lines 26-97; development report “Remaining work”).

## Delivery, art, and readiness

All thirteen scenes use `ManualOnly=True` and `Remote=True`, and the source checks that this combination satisfies the validator's ManualOnly/remote rule (source lines 160-167, 288-296, 998).

That proves the source-level validation condition only; manual remote delivery is not verified physical presence, an available native contact, or a playable campaign schedule.

No finished art or independent art review is present; the supplied native description identifies Mielarah as a middle-aged sorceress with short dark hair, prominent cheekbones, dark circles, and a worn appearance (reference/canon-review/candidate-extra-mentions.json lines 1598-1601).

No registered export, dialogue binding resolution, live runtime contact, save/load test, ToyBox Free Love or No Jealousy compatibility test, or chronological in-game playthrough is proven (development report “Remote delivery and validator,” “Focused checks and measured scope,” and “Remaining work”).

The previous report's historical scores are not scores for this exact revision; this rereview assigns no score and does not certify the project's strict above-90 requirement in every applicable dimension.

The changed hand touch, later scene links, crew decisions, voyage consequences, and three ending branches are present and locally validated, but a branch continuity gap remains, selected-path depth is below the minimum, and the all-path, art, export, runtime, save, and ToyBox gates remain unmet.

Route and game readiness are therefore withheld.
