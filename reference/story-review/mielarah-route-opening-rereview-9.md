# Mielarah Route Opening Independent Rereview 9

This rereview checked `storylines/mielarah_route_opening.py` at SHA256 `5829B7F37EA8FF3D314B662D2834BA636D70D060BC06C008FAEE576172DD492F` and `reference/story-review/mielarah-route-opening-development.md` at SHA256 `9ECB3AF427BA81DB0F8A4FFC6A3D3EDE0F66F9F4086DBABBC1783927303971AE` before review.

Both requested hashes matched before review and were rechecked after this report was written.

## Findings

The local module check passes and reports fifteen unregistered scenes and 164 nodes with topology and cross-scene state assertions valid (source lines 1070-1107).

The R8 shore-week defect is fixed: leaving at dawn sets `short_visit_complete` and the text says the week continues without the Commander, while the full-week completion flag is set only by the separate stay-through-week node (source lines 851-858).

The source assertion verifies the short visit cannot set `shore_week_complete` or enter the new-sail scene, while a completed week reaches the new-sail scene after its required delay (source lines 1086-1094).

The Jori history split also remains correctly enforced: `carry_answer` and the original `crew_meeting` require the `jori_answered` history, while the unbriefed meeting is a distinct branch that makes no private-answer claim (source lines 797-805, 1064-1070).

The new sail-contract scene gives Mielarah a concrete financial dispute to resolve herself: the order proves duplicate charges, she distinguishes a legitimate repair charge from an unjustified fee, and she rejects the Commander's offer to pay or use rank to decide the bill (source lines 861-878).

The prior shore-week gift/loan exchange remains well characterized: she refuses a gift that could buy access, offers a documented no-interest loan she can refuse, and specifies that the loan buys no cabin key, vote, or future evening (source lines 842-844).

A material branch-state defect remains in the departure scene: the option “Accept as a friend, without romance” sets `mielarah.opening.friendship_only`, but no scene gate or later branch checks that flag (source line 807; the only source occurrence is the flag write).

That friendship-only choice can still enter the outer-shoals scene, the romantic future choice, the shore-week date, and the new-sail partnership progression, which contradicts the player's explicit selection and Mielarah's romantic advances (source lines 815-878).

Either route that choice into a distinct friendship continuation or make all later romance scenes and outcomes respect the friendship-only state.

The source-level chain simulation confirms both ordinary and Trickster routes can reach the new-sail scene, but it does not currently assert the friendship-only exclusion because there is no such exclusion in the source (source lines 1045-1098).

I independently counted node text and selected choice text along the longest valid progression to the new-sail completion using the authored gates and flags: the modeled ordinary chain is 9,882 words, and the modeled Trickster chain is 9,569 words.

These selected-chain counts remain well below the hard 21,000 meaningful-word floor for a complete route, even before removing repeated explanations or discounting any content judged non-substantive.

The development report's separate 9,761 ordinary and 9,438 Trickster figures are upper estimates assembled from local maximum branch sums and are not one measured selected playthrough (development report, “Focused checks and measured scope”).

The new sail scene ends by stating that the route continues beyond this opening; it does not provide a complete long-term romance arc or a full set of relationship outcomes (source lines 874-878).

Mielarah's characterization remains distinct in the new scene: she is proud and self-sufficient, accepts responsibility for trial damage, resists the Commander's rank, and still lets the Commander contribute by reading evidence and respecting her lead (source lines 861-878).

The shore-week and sail scenes broaden the relationship through ordinary finances, an invoice dispute, and the choice to build a partnership; some authority and independence explanations recur, but mostly in response to new decisions rather than as repeated summaries (source lines 840-878).

The adult romance is sensual and consensual, with Mielarah inviting a private evening, initiating contact, setting boundaries, and allowing the player to leave, remain friendly, or defer; neither an earlier rescue nor financial help is treated as sexual consent (source lines 840-853, 874-878).

The native/AU boundary remains appropriately explicit: native dialogue supports her Colyphyr service offer, storm crash, and raid death, while the pre-crash Trickster intervention, alternate survival, later contact, romance, shore-week, and sail-contract scenes are authored additions (source lines 12-21, 90-126; development report, “Chronology and native evidence”).

The ordinary contact hook and parent dialogue chain remain unverified, and the Trickster interception, suppression of the native crash cue, alternate campaign progression, and survival persistence remain unimplemented dependencies (source lines 12-21, 90-95, 141-158).

All ten mythic path descriptions remain unimplemented plans, so neither broad path availability nor recovery for dead, expelled, missed-history, and otherwise unavailable states is demonstrated (source lines 26-97, 1071-1080).

## Delivery and readiness

All fifteen scenes set `ManualOnly=True` and `Remote=True`, and the local source check confirms that pair satisfies the validator's ManualOnly/remote rule (source lines 160-167, 998, 1067).

This source-level check does not prove that the game displays these scenes at the authored times, that Mielarah is physically present, or that the matching native flags can be produced.

The scenes remain unregistered, with no verified dialogue export, native contact binding, actor placement, campaign scheduler, save/load behavior, ToyBox Free Love or No Jealousy run, or live chronological playthrough (development report, “Remote delivery and validator,” “Focused checks and measured scope,” and “Remaining work”).

There is no finished artwork or independent art review for Mielarah's redesign (development report, “Remaining work”).

The previous review scores are historical and do not apply to this exact snapshot; this report assigns no numeric scores and cannot establish the strict above-90 threshold across applicable disciplines.

The shore-week correction, Jori split, financial characterization, and new-sail branching are improvements, but the friendship-only flag is not honored downstream, the selected route remains under half the required word floor, and all-path access, art, export, runtime, save, and ToyBox gates remain unmet.

Route and game readiness are withheld.
