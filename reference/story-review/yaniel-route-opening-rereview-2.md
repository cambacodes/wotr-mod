# Yaniel opening: independent integration and narrative rereview

Source: `storylines/yaniel_route_opening.py`.
Pinned source SHA-256: `F36998B5F9A5F165881DFB29A158179EDFFFF40FB9495D66E1D33A65D7154F9D`.

Development report: `reference/story-review/yaniel-route-opening-development.md`.
Pinned report SHA-256: `3B24E5C7F6CD39C169DF9A67560ED7DE7692400780ABA58A6FB6F2428F13C404`.

This is a fresh review of the exact hashes above, limited to the one-scene opening prototype.
It does not approve a full romance route or runtime integration.

## Review result

The revision materially improves the previous draft's actual scene chronology and adult chemistry.
The letter now describes Yaniel recognizing and taking Radiance before returning it to the Commander, and it separates rescue gratitude from romantic access.
Her willingness to flirt is hers, specific, and conditional; she can still decline touch or leave.
However, the identity and chronology deductions are not fully closed as integration gates: the source's rescue, Radiance, survival, actor, area, and contact conditions remain authored metadata without verified producers.
Accordingly this opening is **not approved for integration or in-game testing**.

## Independent scores

- Genuine Yaniel identity and exclusion of the impostor: **89/100 - revision gate**.
The prose is unambiguously addressed to the woman rescued in the Midnight Fane, and the source names the genuine cue and distinguishes the earlier fake.
But `genuine_midnight_fane_rescue_witness` is only a contract string; nothing in this prototype binds it to the cue or proves the impostor cannot satisfy it.
The prior 88-point concern about an unenforced identity condition therefore remains, though the narrative itself is clearer.
- Rescue and Radiance chronology: **90/100 - revision gate**.
The factual sequence is corrected: Yaniel recognizes and takes Radiance, then returns it to the Commander.
The post-rescue letter and her choice to leave are framed as authored continuation rather than native events.
The contact producer, survival/unbound witness, meeting area, and chapter timing still have no verified live binding, so the prior chronology deduction is narrowed but not resolved for integration.
- Adult chemistry and character-specific friction: **93/100 - pass for this opening**.
The revision adds Yaniel's own frank desire, dry challenge, attraction to an uncontrolled answer, and a live disagreement about duty and control.
Her flirtation is not gratitude payment, and the Commander cannot convert curiosity into permission.
Some boundary language is more explicit and contemporary than the surrounding game's usual indirectness, but it no longer reads as only a consent tutorial.
- Older-woman portrayal and attractive framing: **97/100 - pass for this criterion**.
Silver hair, fine lines, practiced movement, and age are preserved as signs of an adult veteran rather than defects to erase.
The prose makes her desirable without pretending she is young or treating age as a joke.
- Character fidelity and paladin identity: **92/100 - pass for this bounded scene**.
Her resistance to being made a symbol, her insistence on choosing her own enemies, and her disciplined independence suit the rescued paladin presented by the cited cues.
The opening would be stronger with more of her religious or martial vocabulary, but it does not require her to abandon duty or forgive her captors to make the attraction possible.
- Consent, boundaries, and nonromantic agency: **98/100 - pass for this criterion**.
Yaniel authors the invitation and topic boundaries, asks before touch, accepts refusal and uncertainty, and leaves without a pursuit flag.
Apology and repair do not grant romance, and the friendship/decline endings remain real outcomes.
- Prose craft and pacing: **91/100 - pass at threshold**.
The opening has clear emotional turns and several memorable lines, particularly the distinction between legend and life.
The repeated explanatory boundary statements occasionally make the conversation sound designed to teach the player a rule, rather than spoken spontaneously by Yaniel; trim only where repetition dilutes her voice.
- Graph, counts, and source hygiene: **100/100 - pass for the reported checks**.
I verified one scene, 17 unique nodes, 33 choices, no dangling targets, and all nodes reachable from the entry.
Python bytecode compilation passes.
The report's node-text counts reproduce: 1,958 whitespace-delimited words and 1,960 Unicode-tokenized prose words.
No em dash occurs in the pinned source or report.
- Evidence labeling and scope honesty: **96/100 - pass for this criterion**.
The report plainly distinguishes extracted native dialogue evidence from unimplemented custom contracts and does not claim full-route or in-game readiness.
The measurements establish opening size and topology only, not route depth, unique playthrough volume, or quality beyond this review.

Scores are separate gates, not an average.
The two remaining sub-91 scores mean the prior review's identity and chronology findings are not fully fixed for integration.

## Required before reopening these gates

Bind the genuine rescue identity to a verified native producer and demonstrate that the impostor branch cannot set it.
Bind Radiance recognition, alive/unbound presence, Yaniel's voluntary contact, actor, chapter window, and meeting location to source-backed producers or keep the result explicitly prototype-only.
Then review the new exact source hash independently after those changes.

No mythic path is implemented or proven attainable, including Trickster's missed-opportunity recovery.
The prototype remains outside the exported Story content and has no complete route, path-specific progression, intimacy arc, outcomes, epilogue, art, save/load proof, ToyBox compatibility evidence, or live game test.
It is far below the 21,000 meaningful-word planning floor for a full character route.
