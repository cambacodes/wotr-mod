# Wenduag and Vellexia relationship-network slice

## Status

This is an authored, unregistered Chapter 4 interlude draft, not a route approval or an integrated playable scene.

The draft contains one scene, eleven nodes, and 1,209 whitespace-delimited words of node and choice text.

It does not meet Wenduag's 21,000-word route floor, Vellexia's route floor, or the project's review gates.

The scene establishes only an optional conversation; no mutual attraction, romance, sexual relationship, or triad is established as canon or as a completed authored outcome.

## Source-backed connection

The native Wenduag romance includes a Vellexia reception as a point of jealousy and vulnerability.

Wenduag's later dialogue recalls the look she gave at Vellexia's reception in `World/Dialogs/Companions/CompanionRomances/Wenduag/TooMuchStress/Cue_0078.jbp` and `Cue_0097.jbp`.

The game's ending glossary independently records that the Commander allayed Wenduag's suspicions when she was jealous of the Commander and Vellexia.

The source audit identifies `WenduagRomance_VelexiaConflict_flag`, native `BlueprintUnlockableFlag` GUID `23cacf7a07480da459b3a59d0fd6da82`.

These records establish Wenduag's jealousy and shared history with Vellexia, not mutual attraction between the women.

The authored premise lets Wenduag express curiosity and competitive respect while stating she has not decided what either means.

Wenduag cannot consent for Vellexia or present the Commander as a prize.

Vellexia receives the invitation directly and gives an explicit affirmative answer before the conversation branch, or she can decline explicitly or be given privacy without an answer that night.

Even acceptance authorizes one conversation only; no romance, touch, or shared arrangement follows automatically.

The native jealousy condition remains emotionally meaningful, and a ToyBox setting cannot stand in for consent or mutual interest.

## Canon and authored development

Canon anchors are Wenduag's native jealousy at the Vellexia reception, her later recollection of it, the Commander having a female Wenduag romance option, and Vellexia's native Chapter 4 manor presence.

Authored developments are Wenduag's clarified curiosity about Vellexia, her offer to make an introduction, Vellexia's affirmative choice to have one conversation, and her explicit refusal branch.

The draft does not modify the native Wenduag romance, jealousy event, romance flags, endings, or Vellexia's native dates and route.

The original contact actors, actual reception-history flag state, manor location, and delivery timing must still be verified in blueprint data and a real save.

## Entry and contact contract

The scene requires an addon-owned `wenduag.vellexia_network.reception_history_verified` condition.

Its unimplemented producer contract must observe the native jealousy flag `23cacf7a07480da459b3a59d0fd6da82` and establish the required contact and location state before enabling the scene.

The scene uses the recognized `ContactUnit` field with Wenduag's native unit GUID in 32-character N format and `AdditionalContactUnits` for Vellexia.

It does not rely on the unsupported `PartnerUnit` or `ContactProof` fields.

The previous draft's unbound `wenduag.ran_romance_active` alias and historical `vellexia.greeted` cue requirement were removed.

The native jealousy flag is the source-backed relationship-history predicate; the addon producer and its lifecycle mapping have not been implemented or tested.

No active-romance alias is required, because this slice is an authored relationship-network interlude rather than a declared continuation of Wenduag's native romance.

## Path access map

The requirement is a bespoke attainable route on every mythic path.

This draft does not satisfy that requirement because no all-path event producer, contact contract, or tested actor availability exists.

| Mythic path | Status in this slice |
| --- | --- |
| Angel | Unresolved; no path-specific contact evidence audited. |
| Aeon | Unresolved; no path-specific contact evidence audited. |
| Azata | Unresolved; the shared reception does not prove this authored contact is available. |
| Demon | Unresolved; no path-specific contact evidence audited. |
| Devil | Unresolved; no path-specific contact evidence audited. |
| Gold Dragon | Unresolved; no path-specific contact evidence audited. |
| Legend | Unresolved; no path-specific contact evidence audited. |
| Lich | Unresolved; no path-specific contact evidence audited. |
| Swarm | Unresolved; identity, survival, and consent cannot be assumed. |
| Trickster | Authored proposal only; a Trickster fate intervention and its delivery are not implemented or tested. |

The scene is a continuation hook requiring the source-backed jealousy history, not a missed-romance acquisition route.

It cannot be counted as making either character available across all paths.

## File and checks

Source file: `storylines/wenduag_relationship_network.py`.

The source exposes a ten-entry path map, one scene, eleven nodes, and 1,209 whitespace-delimited words across node and choice text.

Vellexia's affirmative response is a distinct node before the conversation begins, and only this node's explicit continuation choice records `wenduag.vellexia_network.conversation_accepted`.

The accepted conversation and unanswered privacy path do not set the `CommittedFlag`; its reserved `wenduag.vellexia_network.relationship_chosen` state is not set anywhere in this slice.

No later-meeting flag remains, because this file contains no callback scene that could consume one.

The prior exact-source rereview's affirmative-response and committed-state findings have been addressed, and an independent rereview of this revision is still required.

The module imports successfully and its local assertions check the ten path entries, N-format Wenduag identifier, additional Vellexia contact, unimplemented producer status, graph links, explicit acceptance flag, and absence of a false committed relationship state.

Every internal choice target resolves to one of the eleven nodes.

Current source SHA-256: `E91343DDB8F16B61C3750FC7903023D7439F6474CFD2C5B88E39978173991520`.

The authored file is intentionally not registered in `expansion.py` and does not alter `development/Story.json`.

No project-wide headless test, game build, live save test, independent final review, or art review has been completed for this unregistered module.

## Remaining gates

Verify the native jealousy flag, reception event, both original units, exact area, timing, and dialogue conditions against the installed blueprints.

Implement and test the producer contract, including lifecycle-safe mapping of the native flag and both current actors.

Design and implement credible bespoke access on all ten mythic paths, including Trickster intervention with evidence, limits, failure, and voluntary response.

Author the complete Wenduag and Vellexia routes to their individual content floors, with any triad material additional to each woman's route and with direct opt-in from both women.

Register and integrate the scenes only after contact, persistent state, and delivery contracts exist.

Obtain independent canon, characterization, writing, mechanics, and art reviews of the full routes, then revise against each review.

Complete headless campaign and package checks, followed by a real in-game save test of timing, actor presentation, path access, and ToyBox compatibility.
