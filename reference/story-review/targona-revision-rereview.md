# Targona two-scene revision rereview

This rereview compares the revised `the_open_threshold` and `the_key_remains_hers` scenes with the prior independent review in `reference/story-review/targona-two-scene-independent-review.md`.

The reviewed `storylines/targona_opening.py` SHA256 is `13F96B696B12A159A7AA190350CDFC2955037C46D233D247EE4B28FF077E209D`, verified directly against the current file.

The earlier SHA is no longer current, so only this rereview applies to the revised scene text.

## Prior findings addressed

**Return-risk disclosure:** Targona now explicitly warns that a made passage might fail to return someone, refuses to cross an untested opening, and retains the option to stay at her wayhouse without an apology or relationship penalty.

The successful magical route tests an empty dispatch pouch from both ends before Targona chooses whether to come, gives her the test information and key, and states that the passage returns to the same two places.

The failed Arcana test closes the passage before Targona or the courier approaches it, sends a frank letter about the failure, and has her stay at the wayhouse.

**Correspondence after declining or failure:** declining the visit, rejecting the courier invitation, and failing the route test all lead to correspondence and set `targona.visit_correspondence`.

The next scene has a matching correspondence response, and the text says a declined visit leaves the parent romance unchanged.

**Distinct Trickster setups:** the impossible-paper setup requires both the current Trickster flag and `targona.extra_ending`, while the separate courier-fate setup requires Trickster and `targona.ordinary_ending`.

Each setup is an understandable continuation of its corresponding previous choice, and both offer a credible authored path to an in-person meeting without making Targona's answer compulsory.

**Arcana and fallback semantics:** the Arcana check is clearly a test before anyone is sent through, and its failure safely returns the story to correspondence.

The alternative in the paper-door setup explicitly rejects a made passage and uses the known courier road instead.

**Origin and arrival:** the new wayhouse is named as Targona's current location, and the portal and public-road options both explain how she can reach the Drezen courtyard.

These edits resolve the prior major consent, preparation, and location concerns.

## Remaining findings

**Moderate, lines 333-350:** the `close` response says Targona chooses to end the visit, then says she has a few hours to spare and routes into further shared time before she eventually decides to leave.

The entry choice asks whether she would rather close the passage and take the public road, but the response text instead describes ending the visit, so the action, line, and follow-through do not agree.

Remedy this by deciding whether this node means she closes the passage but stays for the evening, or leaves immediately, and make the following page and choice consistent with that decision.

**Moderate, line 283:** the narrator calls the wayhouse an "authored current location" and explains that it is not a new place in Targona's past.

Those are production notes exposed as player-facing dialogue and break the otherwise immersive correspondence.

Replace the aside with an in-world sentence identifying the wayhouse as her current Celestial Order assignment, or keep continuity caveats in review documentation rather than the scene.

**Continuity question, lines 247-260 and 278-352:** the immediately preceding correspondence gives Anograt a speaking role on the Trickster-parent history branch, but these meeting pages do not establish whether she is nearby, separated, or choosing not to attend.

The parent evidence describes limits on Anograt's separate presence, so the omission is not proof of a canon error, but one brief conditional line would help preserve continuity without making her part of this romantic meeting.

Consider stating only what the route can establish about her current presence and choice, without inventing travel or assuming consent to join the encounter.

## Canon, characterization, and branch check

The new wayhouse is clearly a present-day authored setting and does not revise Targona's canonical captivity or past.

The bounded passage is now prepared by a specific earlier Trickster page choice, while the ordinary-page alternative has its own smaller courier-chain intervention.

Targona keeps her precise voice, dry humor, protective instincts, and right to refuse or leave.

The romance remains an extension of the existing parent romance rather than a replacement or a claim that intimacy cures her trauma.

The new scene entry still requires Targona's freedom, the completed parent finale quest, a recorded parent finale cue, and the existing romance.

The opening choices require mutually exclusive prior page flags for their two Trickster setups, and the four follow-up replies match the `visit_desire`, `visit_tender`, `visit_pause`, and `visit_correspondence` outcomes.

This source review does not prove runtime evaluation of dialogue checks, flags, or scene transitions.

## Gates still outstanding

Resolve the `close` branch contradiction and remove the player-facing production note before treating these pages as final.

Review the assembled route against the required full-length standard using a selected playthrough, then independently review the complete route for canon, characterization, consent, mythic-path history, and branch continuity.

Review final art against Targona's in-game model and installed RanRomance variants.

Verify parent-mod initialization, Unity dialogue and check execution, save/load persistence, ToyBox compatibility, and a complete in-game playthrough.

No score is assigned, and this rereview does not approve the full route or declare it ready for in-game testing.
