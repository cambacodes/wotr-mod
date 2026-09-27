# Wenduag and Vellexia relationship-network independent rereview

Review date: 2026-09-27.

Reviewed source SHA-256: `E91343DDB8F16B61C3750FC7903023D7439F6474CFD2C5B88E39978173991520`.

Reviewed development report SHA-256: `130FD163DBBD325697A20AD80D09825E20B77FBA72EACA652093C6576A19ECD0`.

Prior rereview SHA-256: `A05A403DC7FC8E2DCCBB222B4EB9A223D8DA0F04B435EE2B2AC27108C13397B7`.

I independently checked the exact source and report above, the previous review's consent and state findings, the local Story scene/contact availability rules, and all authored choice targets and flag writes.

I did not edit the source, development report, or generated Story.

Disposition: the prior consent and committed-state findings are resolved in this slice.

This is not approval for integration or full-route readiness.

## Consent and relationship-state findings

**[Fixed] Vellexia gives her affirmative before the conversation proceeds.**

At `vellexia_answer`, Vellexia says she has not agreed beyond hearing the invitation and explicitly says, “let me make my own answer.”

Selecting the affirmative option advances to the separate `vellexia_accepts` node, where Vellexia herself says, “Yes. I will stay for one conversation.”

Only a further player choice advances from that affirmative node to `conversation` and writes `wenduag.vellexia_network.conversation_accepted`.

That flag records the expressly accepted conversation, not attraction, romance, touch, or a triad.

**[Fixed] Refusal and unanswered branches do not accept or commit.**

The explicit refusal branch writes only `wenduag.vellexia_network.closed`.

The privacy branch from `vellexia_answer` advances to `privacy` without writing any flag, and the privacy branch after Vellexia's affirmative also records no continued conversation.

The refusal dialogue asks that she not be asked again unless she raises the subject, and the unanswered branch makes no claim that Vellexia agreed.

**[Fixed] The reserved committed state is not written.**

`RELATIONSHIP.CommittedFlag` is `wenduag.vellexia_network.relationship_chosen`.

No choice in the scene writes that flag.

The authored writes are limited to `started`, `closed`, and the explicitly accepted one-conversation state.

The Story runtime marks a scene complete on exit, which prevents this same completed scene from being offered again; the privacy branch does not need to misuse a relationship or acceptance flag for that purpose.

**[Resolved with clear limits] Jealousy remains history, not proof of attraction.**

The scene requires the addon history alias, whose proposed source is the native Wenduag/Vellexia jealousy flag.

The report correctly limits that canon evidence to Wenduag's jealousy and shared reception history, not mutual attraction between the women.

The prose gives Wenduag curiosity and competitive respect while explicitly saying she will not pretend attraction, and Vellexia's consent remains separate.

Neither the scene nor the report claims an existing romance, mutual desire, sexual relationship, or established triad.

The final privacy line refers to a possible later step only as something the three could name together; it does not say such a step exists or has been accepted.

## Contracts, graph, and remaining limits

The scene's `ContactUnit` is Wenduag's 32-character N-format identifier, and `AdditionalContactUnits` contains Vellexia's N-format identifier.

The runtime checks both identifiers against currently available contacts, in addition to the configured chapter, area, requirements, and forbids.

The report accurately says that this runtime presence check does not implement the missing producer for `reception_history_verified`, prove the native cue's lifecycle in a live save, or establish when both actors are simultaneously present.

The scene is still unregistered and its producer contract is explicitly `implemented: False`.

All eleven authored nodes are reachable by valid internal targets, and the refusal, close, privacy, and accepted-conversation paths have coherent explicit state effects.

The report's word-count and node-count claims match the source at 1,209 whitespace-delimited words across node and choice text, one scene, and eleven nodes.

The source map labels every mythic path unresolved or proposal-only, including Trickster; it does not overstate path access.

The development report also correctly states that the draft is far below either character's route floor and lacks the full routes, path adapters, registered producer, independent full-route reviews, art review, and in-game validation.

## Checks performed

The exact source and development-report hashes matched the requested values before review.

The module's `__main__` assertions passed when run with the `storylines` directory added to Python's import path.

An independent graph/state inspection found eleven nodes, no unresolved targets, no write of the reserved committed flag, and a distinct affirmative node before the conversation node.

The project runtime source confirms that both current-contact identifiers are checked by the scene availability rule.

These are source and local-assertion checks only; they do not validate Unity behavior, native actor availability, campaign timing, mythic-path reachability, ToyBox interaction, art, or save/load behavior.

## Disposition

The specific consent and state defects from the prior rereview are resolved in the reviewed source.

I find no new relationship-state or consent defect in this interlude slice.

Do not count it as a completed romance route or as ready for in-game route testing.

Runtime producer and actor checks, all-path access, complete Wenduag and Vellexia routes, independent full-route quality reviews, art review, integration, and campaign testing remain required.
