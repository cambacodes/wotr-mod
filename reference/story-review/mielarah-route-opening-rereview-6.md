# Mielarah Route Opening Independent Rereview 6

This rereview checked `storylines/mielarah_route_opening.py` at SHA256 `55806084DB6A36EA1F7ADFF3D22815540465437E3EAA60BCD563277F55311BD1` and `reference/story-review/mielarah-route-opening-development.md` at SHA256 `5EA0E46D9931E2F4D231C3DA46E591F575740591CDFF0E337375EB3C9BE9CE3C` before review.

Both requested hashes matched before review and were rechecked after this report was written.

## Findings

The module's own invocation succeeds and reports eleven unregistered scenes and 110 nodes with topology and cross-scene state checks passing.

The source also evaluates chapter, delay, `Requires`, and `Forbids` together in `authored_scene_eligible`, then simulates delayed ordinary follow-up, Trickster arrival, refusal, consequences, and branches across linked scenes (source lines 802-945).

Those checks establish consistency in the authored model only; they do not establish that a producer writes the contracted flags or the game scheduler delivers the scenes in chronology.

The native references support the report's narrow factual claims: Tumberd `Cue_0020` and `Cue_0070` say Starcatcher and its crew are at the Commander's disposal, `Cue_0040` refers to the curse not claiming the Commander's life, and `Cue_0054` calls Mielarah's coercive magic “disciplinary thought-correction” (reference/canon-review/candidate-extra-mentions.json lines 1603-1620, 1633-1640).

The same extracted reference states that `Cue_0426` depicts the Ishiar crash after the storm answer and that `Cue_0482` depicts the captain's death after the raid (source FATE_AUDIT lines 112-126, corroborated by reference/canon-review/candidate-extra-mentions.json lines 1045-1050).

The module correctly labels the post-crash hard landing, repair passage, and return to Tumberd as authored alternate history, and explicitly states that the native cues do not prove survival or a contact hook (source lines 12-21, 90-95, 112-126).

The first ordinary scene is explicitly contingent on a producer establishing living contact at the same Tumberd conversation; the module says its parent choice chain and extension hook are unverified (source lines 12-21, 181-196, 288-296).

The Trickster acquisition is more specific and mechanically dramatic than a generic fourth-wall bypass: it proposes an Arcana read, a limited visible false wind, Mielarah's informed authorization, a Perception bearing check, and captain-led maneuvering with failed or boundary-breaking outcomes preserving the native crash (source lines 90-95, 314-394).

This is still an unimplemented counterfactual and lacks a verified answer-interception hook, cue suppression, campaign continuation, survival persistence, and native actor/contact availability (source lines 141-158, 300-394).

All ten mythic entries are clearly marked unimplemented plans; most ordinary entries require a verified living Colyphyr arrival, while Aeon expulsion, raid death, and several other unavailable histories remain blocked rather than silently reversed (source lines 26-97, 123-137).

The prose generally keeps Mielarah sharp, pragmatic, proud of her aeronaut identity, and unwilling to surrender captaincy; she corrects the Commander, reacts against being judged or reassured, and treats her use of coercive magic as both effective and harmful (source lines 203-276).

Her attraction arises from specific interactions around risk, command, and respecting limits, while her prior coercive act is not transformed into a romantic debt (source lines 240-279, 459 onward).

Later scenes give her command over crew decisions, make the Commander answer for mistakes, and let her refuse, pause, or end romantic contact (source lines 585-733, 734-793).

There is some repeated boundary language across scenes, especially the recurring reminders not to use rank, ship access, crew risk, or the intervention as leverage; this fits the story's central conflict but should be varied through consequential action so Mielarah does not repeatedly explain the same limit after the player has already respected it.

The intimacy material is adult and sensual but graphic and explicit, with affirmative invitations, player options to decline, touch checks, her direction of contact, and explicit stopping or deferral branches (source lines 263-283, 769-787).

One small wording issue remains at the first touch: the player asks to kiss her hand, but the action specifies the inside of her wrist; make the requested and granted contact match more precisely (source lines 269-276).

The selected-path estimate is the decisive scope blocker: the development report counts 11,933 raw source words, but estimates only about 6,954 ordinary-path words and about 6,631 Trickster-path words through the authored additions, both before integration-generated text (development report, “Focused checks and measured scope”).

Those model totals are below the hard 21,000 meaningful-word floor for a complete route, and no selected in-game playthrough count exists.

The branch progression is consequential at opening scale: accepting the chart leads to a possible later invitation, the Trickster success leads through a repair/arrival bridge, and later branches include crew consultation, sailing risk, refusal, and intimacy choices (source lines 181-793).

It remains an opening rather than a complete romance, and the last authored event is a single watch and possible intimate evening rather than a resolved multi-act relationship, mature long-term conflict, or ending.

## Delivery, art, and remaining gates

All eleven scenes use `ManualOnly=True` with `Remote=True`; the module checks the `Story.cs` validator's rule that ManualOnly scenes must be remote, and notes that manual remote delivery provides a Read button while excluding automatic `NextRemote` delivery (source lines 160-167, 288-296, 851-864).

This addresses that specific source-level validation constraint, but remote reading is not proof that Mielarah's actor is physically present at the quay, ship, or cabin, nor that any of these scenes appears in a real campaign save.

The scenes remain unregistered, have no verified native contact unit or location-specific actor attachment, and do not have a verified extension hook (source lines 12-21, 160-167, development report “Remote delivery and validator”).

No finished art or independent art review is provided; Mielarah's native appearance anchor is a middle-aged sorceress with short dark hair, a skinny face, prominent cheekbones, dark circles, and a worn look (reference/canon-review/candidate-extra-mentions.json lines 1598-1601).

No production dialogue export, native binding resolution, runtime contact producer, answer interception, save/load, ToyBox Free Love/No Jealousy, or live chronological playthrough is verified (development report “Remaining work”).

The report's prior review scores belong to the earlier snapshot and cannot be carried forward; this rereview assigns no score and does not certify the strict above-90 requirement in any dimension.

The exact native citation distinctions, chronology caveats, and unimplemented status are appropriately explicit, and the local scene-link checks pass, but full-route scope, reachable per-playthrough depth, acquisition across histories, finished art, production integration, save behavior, ToyBox compatibility, and runtime delivery remain blocking.
