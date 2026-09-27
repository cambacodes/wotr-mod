# Mielarah Route Opening Independent Rereview 8

This rereview checked `storylines/mielarah_route_opening.py` at SHA256 `4C4CFCA7799001FED3E8F50E760FDD9313F17854A581BE635E307F456563890F` and `reference/story-review/mielarah-route-opening-development.md` at SHA256 `A02EE9DFDF66E854055B202EBC42FC01A50E4092288D0480272F18F26DD196CD` before review.

Both requested hashes matched before review and were rechecked after this report was written.

## Findings

The module check passes and reports fourteen unregistered scenes and 148 nodes with local topology and cross-scene state checks valid (source lines 1070-1107).

The revised Jori branch resolves the prior history gap: `carry_answer` can only be reached after `crew_voice` sets `jori_answered`, while a rules-only discussion goes to `crew_meeting_unbriefed`, which explicitly says no private answer was carried (source lines 797-805).

The node-history assertions check all modeled visits to both `carry_answer` and `crew_meeting`, and separately verify that the unbriefed path lacks Jori's private-answer flag (source lines 1040-1045).

The shore-week scene requires the outer-shoals completion plus either the open or deferred ending through `RequiresAny`, and its delay is 168 hours (source lines 836-858).

The authored helper tests the 167-hour failure and 168-hour success for both open and deferred histories, and confirms the closed ending cannot reach the shore scene (source lines 1053-1062).

The game source defines and evaluates `RequiresAny` in scene eligibility and validates its contents (src/Story.cs lines 201, 381-382), so the authoring contract uses a supported production field even though this scene remains unregistered.

One internal time-continuity issue remains within the shore-week scene: choosing to leave tomorrow reaches `shore_end`, which describes a week ashore ending and permits `shore_week_complete` to be set despite the Commander departing after one night (source lines 842, 851-852).

Give that branch a separate short-visit completion state or keep the Commander present through the week before using the shared completion marker.

Mielarah's response to the gift offer maintains her independence: she refuses money that could imply a claim, offers a written repayable loan with no interest and no romantic consideration, and permits the Commander to decline it without penalty to the evening (source lines 842-844).

The ordinary and Trickster chain estimates remain approximately 8,934 and 8,611 words respectively, including the new local maxima; both remain far below the hard floor of 21,000 meaningful words for a complete route (development report, “Focused checks and measured scope”).

The 15,050 raw words and 15,020 distinct normalized segment words include mutually exclusive authored text, and the report explicitly does not claim that the maximum local branch sums combine into a single valid playthrough.

The continuation now gives visible relationship consequences through wage release, crew departures, the lost contract, Mielarah's own financial decisions, and her invitation to ordinary companionship; this is useful campaign-scale progression but still only an opening contribution, not a complete romance arc (source lines 797-857).

The writing keeps Mielarah direct, proud, and fallible, with wit and desire alongside clear professional authority; the new discussion of ordinary finances and habits broadens her beyond the recurring ship-command argument (source lines 797-857).

Some boundary statements recur around rank, money, and her refusal of magical control, but most now arise from fresh consequences rather than serving as repeated explanatory speeches.

The shore-week affection and private invitation remain adult and graphic and explicit, with the player able to keep the evening friendly, leave early, accept a loan or refuse one, defer intimacy, or choose a private evening on Mielarah's terms (source lines 840-852).

The intimate scene does not treat acceptance of the loan, financial aid, or prior rescue as consent, and Mielarah retains her right to change her mind (source lines 843-852).

The native/AU distinction remains explicit: the native Tumberd exchange establishes her service offer and her presence then, while the post-crash intervention, survival, repair passage, later contact, relationship, and shore-week scene are authored additions (source lines 12-21, 90-126; development report “Chronology and native evidence”).

The ordinary contact producer and exact parent-dialogue chain remain unimplemented, and the Trickster answer interception, cue suppression, survival persistence, and campaign continuation remain unverified (source lines 12-21, 141-158).

All ten mythic paths remain listed as unimplemented access plans, so this contribution has no implemented all-path acquisition or missed-history recovery (source lines 26-97, 1071-1080).

## Delivery and remaining gates

All fourteen scenes use `ManualOnly=True` and `Remote=True`, and the source verifies this against the validator rule requiring ManualOnly scenes to be remote (source lines 160-167, 998, 1067).

Manual remote availability is not proof of Mielarah's physical presence at the scene, native contact, registered export, or chronological campaign delivery.

There is no finished or independently reviewed art, dialogue export, native binding, runtime contact producer, save/load check, ToyBox Free Love/No Jealousy compatibility test, or live game playthrough (development report, “Remote delivery and validator” and “Remaining work”).

The local tests do not establish whole-route parity, reachable full-length depth, all-path access, or satisfaction of the strict above-90 threshold in every applicable dimension.

This rereview assigns no score and withholds route and game readiness; the Jori history correction and `RequiresAny` shore-week gate are sound at source-model level, but the dawn-departure completion marker remains inconsistent and the full-route, art, integration, runtime, save, and ToyBox gates remain unmet.
