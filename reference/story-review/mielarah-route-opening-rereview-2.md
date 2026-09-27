# Independent rereview: Mielarah route opening

Review target: `storylines/mielarah_route_opening.py`.

Target SHA-256: `B60AC9F5E4CA9D106E8F669F6F3517F7C7382839AEE97882B5153B267C0A1FB5`.

Author development report: `reference/story-review/mielarah-route-opening-development.md`.

Development report SHA-256: `3E3549BBE20B01925EB684416C6A635EA8C7D0C1145EC9F1F2623DA952756D5D`.

These hashes were recomputed before review and identify the exact reviewed versions.

## Verdict

This revision makes concrete progress on each of the first review's main story concerns: it anchors the scene to the Colyphyr service exchange, puts a chart-reading interaction between the Commander and captain, gives the attraction a specific stated basis, and separates the fatal native outcomes from proposed interventions.

The scene's strongest quality is that Mielarah keeps command and can reject both the conversation and the Commander, while the confession about coercive magic remains morally unresolved.

The opening still does not earn its attraction strongly enough, and the new chronology remains an unverified integration premise rather than an available native follow-up.

The ten mythic entries remain pitches marked unimplemented, including the Trickster check proposal; none establishes an attainable route.

This is an unregistered, prototype-only opening, not an integrated or game-ready route.

The measured authored volume is 2,273 words, against the 21,000-word planning floor, and says nothing by itself about a full route's reachable playthrough length.

No scored criterion passes the requested 91-point gate, so this revision is not approved for integration or in-game testing.

## Independent scores

Scores judge this opening only, not a projected full route.

Each criterion is a separate gate; no average is used.

Any score below 91 fails.

- Character fidelity: 89/100 - the captaincy, sharp humor, pride, defense of a coercive choice, and refusal of easy absolution are substantially more individual than the first draft; some of the exchange still speaks in polished explanatory formulations, and the source evidence provided here does not establish her conversational cadence beyond the quoted native lines.
- Consent and agency: 96/100 - she sets the initial limits, refusal ends contact, she controls the ship and timing of any next invitation, and the requested hand kiss receives a narrow affirmative answer with an explicit stop condition.
- Native chronology and availability: 87/100 - the Colyphyr cue text and farewell cue support a service offer and living Mielarah at those dialogue moments; they do not establish that the new quay scene can run afterward, that she remains spawned there, or that the proposed authored contact flag can be populated on the correct parent-choice branch.
- Dramatic chemistry: 88/100 - the chart exercise gives them a concrete shared task, and Mielarah names listening and accepting correction as reasons for interest; however, the attraction follows one conversation and a confession of serious coercion, and her desire still reads partly as an authorial declaration instead of a specific playable moment of mutual tension earned over time.
- Mythic-path specificity: 45/100 - the access map is more disciplined and includes conditions, consequences, failure states, and anchors, but these are prose contracts, not implemented branches; the proposed Trickster checks have DCs and failure states but no verified selected-answer bindings, quest-state producer, or runtime test.
- Native-source and implementation evidence: 42/100 - the local candidate extracts corroborate several cue paths, text, and GUIDs, and the local etude catalog maps the cited CaptainMielara etude GUID; the report's specific Answer_0351 selected-answer binding is not present in the reviewed source corpus, and no live actor/contact producer or registered scene exists.
- Mature scene craft: 89/100 - the scene handles desire without turning rescue, gratitude, or absolution into payment, and the hand-kiss branch is sensual but bounded; this remains mostly an accountability conversation with a single brief touch rather than a developed mature romance opening with sustained sensual tension.
- Scope and route completeness: 12/100 - the source is one optional opening scene, far short of the route floor and without full mythic-path routes, art, or integration.

## Checks and source evidence

`python -m py_compile storylines/mielarah_route_opening.py` passes.

With the repository root on `PYTHONPATH`, the source self-check passes and reports one unregistered scene, 16 nodes, valid topology, and no courtship commit awarded.

The source self-check follows ordinary choice links and both check success and failure links; all 16 nodes are reachable from `start`.

An independent count using the repository tokenizer's markup stripping and word rules gives 2,273 raw words: 1,878 prose words and 395 choice words, with 2,273 distinct normalized segment words.

The revised development report's volume figure matches this count, but the file's earlier source-version history should not be confused with the current node count: the current file has 16 nodes, not 14.

No em dash occurs in the source or development report.

The local `candidate-extra-mentions.json` extract confirms the text and GUIDs for `AirAdventures/Cue_0426` (`1b4e78245cb3a244588f9ec0fda54ea8`), `AirAdventures/Cue_0482` (`dbec675b71e9d5f4d96055f4bb31762e`), `TavernBadLuck/Tumberd/Cue_0020` (`424cf61a022d8d34b9131e99bf360ebd`), `Cue_0070` (`e05a1a1f1bc27674fbd569208c28c739`), and farewell `Cue_0040` (`4dcc095f94bcdb945867be5c7f546946`).

That local extract supports treating the crash and raid as distinct fatal events and the service cues as offers made in those dialogue moments; it does not prove the new scene's hook or later actor placement.

The local `expansion/etudes.json` maps `CaptainMielara.jbp` to `8d0fcb697a43a464fa7119e274bf9d7b`, consistent with the report's etude reference.

The report states that native `Answer_0351` GUID `b98a0a14e5741ea4c90ae015154bc861` is selected by the crash cue and describes the helm order, but that answer record is not present in the local candidate extracts I could inspect; this rereview therefore treats that exact binding as author-reported evidence, not independently verified evidence.

The development report also says the installed raw blueprints were opened, but no copied raw blueprint record or reproducible query is included here to let this reviewer independently check all selected-answer and active-etude conditions.

## Remaining gates

- Bind the proposed Colyphyr extension to the verified native parent choice, actor presence, and persistent state in the actual integration.
- Provide reviewable raw blueprint evidence for the crash and raid answer, cue, etude, survival, and death bindings, then implement their state handling.
- Implement and verify attainable access and consequences for all ten mythic paths; in particular, turn the Trickster proposal into a quest-connected pre-crash intervention with tested roll and failure paths, while retaining Mielarah's right to refuse.
- Continue the attraction over time with concrete reciprocal behavior and stronger Mielarah-specific voice, leaving genuine incompatibility and rejection possible.
- Expand to a complete route with at least 21,000 distinct authored words and audit reachable content per playthrough; the current 2,273-word opening does not satisfy that requirement.
- Obtain the separate art, integration, runtime, and independent creative reviews required by the project gates.
- Keep the route unregistered until these gates pass, then run headless checks on the integrated export before requesting in-game testing.
