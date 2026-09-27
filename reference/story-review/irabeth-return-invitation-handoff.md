# Irabeth living-departure invitation

Status: independently approved introductory manuscript; runtime integration remains under review.
The three scenes are a 1,736 distinct-word addition to the existing Irabeth campaign, not a replacement for its per-character length requirement.
The source has 20 nodes, 1,740 raw prose-and-choice words, and four exact repeated words removed by the existing inventory tool.
No native romance, office, morale, departure or death state is written.

## Authored premise and scope

A questionable requisition bearing Irabeth's name gives the Commander a concrete reason to seek her judgment after a living political departure.
The account and supplier are authored developments, not a recovered native quest.
The Commander can emphasize protecting her name or setting a trap for the supplier, and openly acknowledge wanting a personal conversation.
The Knowledge World check distinguishes a precise discrepancy from an uncertain case; the failure branch remains honest about missing evidence and receives a different reply.
Irabeth recognizes the tactic and improves the investigation rather than becoming an audience for the Commander's cleverness.
She accepts one conversation without agreeing to return to duty or resume a romance.
The investigation is not resolved in these introductory scenes and needs a later payoff before the departure continuation is called complete.

The native basis for the living departure and exact retained actor is documented in the capital contact, meeting-position, etude-lifecycle and meeting-selector audits.
This candidate does not restore a dead Irabeth or summon an arbitrary replacement actor.
It does not resolve Anevia's absence or assume her attendance.
The hypothetical remark about what Anevia would say is deliberately not a statement that she is presently alive or available.

## Runtime contract

All three scenes require current Trickster, Chapter 5, Drezen and Irabeth's living departure.
Their new typed AfterDeparture metadata must pass the separately reviewed narrow Rules policy before integration.
The two remote scenes additionally require positive read-only correspondence evidence.
The physical scene requires the exact Irabeth contact, an accepted invitation and verified meeting arrival.
Native unavailability remains in force for ordinary romance scenes outside this bounded visit.

| Scene | Earned prerequisite and result |
| --- | --- |
| irabeth.return_request | Read-only correspondence evidence; terminal choice records return_request_sent and the chosen investigative approach. |
| irabeth.return_reply | Completed request and request_sent timestamp at least 48 hours old; records accepted or declined, or allows postponement. |
| irabeth.return_first_words | Completed reply, accepted timestamp at least 12 hours old, actual arrived evidence and native contact; records the kept private hour and completes the one-visit scene. |

All flags in the table use the irabeth prefix.
Acceptance is consent to meet, not evidence of physical arrival.
Completion of the physical scene tells the runtime to release its temporary meeting claim.
The declined and closed states remain respected.
The standard departure rules, runtime helper and their independent review are separate work items.

## Verification still required

Import and inventory succeeded without generating the shared export.
The independent manuscript review passed the scoped character, writing, continuity, mature interest and choice criteria at 92 or 93.
See irabeth-return-invitation-independent-review.md for its evidence and limits.
Both check outcomes and the request, reply and first-visit branches now pass actual Rules traversal in an isolated 588-scene candidate.
The complete Rules run passed 25,962,607 assertions; independent review of the new campaign test remains pending.
The typed policy passed independent review and 181 focused assertions, including malformed metadata and unavailable states.
Current manuscript SHA256 is 0375A0365E6D182D0F234D71E69D8C30610C9EF9EF8E1213669C6140E6056801.
The registered helper needs native construction, claim arbitration, timing, withdrawal and retry review.
Actual arrival, dialogue, save/load and ToyBox behavior still need in-game verification.
Subsequent correspondence, the supplier outcome and continuing romance access remain necessary before this can be described as a complete recovery route.
