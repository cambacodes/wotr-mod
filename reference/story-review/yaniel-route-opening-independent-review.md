# Yaniel opening: independent character and consent review

Source: `storylines/yaniel_route_opening.py`.
Pinned source SHA-256: `B9C31383EE3AA3AA4317AC617F778EF3FE2ACB34AB5488E4E769918412958931`.

Development record: `reference/story-review/yaniel-route-opening-development.md`.
Pinned report SHA-256: `85B3A0667DE55B13E4C9DE403AFCE805A4BFFE429F9EC1391316AB176664BC1B`.

This review applies only to this 17-node opening prototype.
It does not approve a complete romance, any mythic route, art, registration, or runtime behavior.
Scores are independent gates, not an average.
Any score below 91 requires revision before this bounded opening can pass review.

## Native evidence checked

The local extracted dialogue inventory identifies `World/Dialogs/c3/MidnightFane/TrueYaniel/Cue_0001.jbp`, GUID `cedf416f4d873d0468b01270c7b8eb9e`, as the blue-eyed old woman who identifies herself as Yaniel and an unlucky paladin after the Fane rescue.
`World/Dialogs/c3/MidnightFane/TrueYaniel/Cue_0008.jbp`, GUID `cbf1a11c8d3ce814595149a211502ad1`, has Yaniel recognize Radiance and take the sword.
The surrounding genuine-Yaniel cues include Seelah's intervention against killing her, the Hand of the Inheritor recognition, and Yaniel's account of captivity and resistance.
The local inventory separately places the impersonator in `World/Dialogs/c2_vs/DrezenSiege/FakeYaniel_First/`.
The native evidence supports the prototype's distinction between rescued Yaniel and the earlier fake, its explicit old-woman portrayal, and the rescue/recognition prerequisites.
It does not provide a native romance, post-rescue contact channel, survival flag, public-garden scene, or proof that the Commander can meet her in the prototype's chapter window.

## Scores

- Genuine Yaniel portrayal versus the impersonator: **88/100 - revision gate**.
The scene writes the genuine rescued Yaniel consistently, and the development record correctly distinguishes the false Yaniel.
However, `yaniel.false_impersonation_only` is an authored placeholder, not a verified native state check, so the source does not yet enforce that the impersonator cannot satisfy the entry condition.
- Rescue and Radiance continuity: **86/100 - revision gate**.
The letter credits the Commander with returning Radiance to Yaniel, which is compatible with the recognition interaction, and it does not treat that contact as consent.
The source's rescue, Radiance-recognition, alive/free, and voluntary-contact requirements are placeholders; the public garden and chapter 4-5 availability have no verified producers or location evidence.
The record is candid about this gap, but the opening itself is not yet tied to a playable post-rescue chronology.
- Explicit old-woman status and age portrayal: **96/100 - pass for this criterion**.
The prototype retains silver hair, fine lines, measured movement, and her own statements about age without making age an insult or treating her as a younger version of herself.
The portrayal remains dignified and attractive in framing, though it does not yet give the player much specific visual or sensual detail.
- Trauma is not used as romantic access: **98/100 - pass for this criterion**.
Her captivity and trauma explain boundaries and anger, not attraction or obligation.
The Commander cannot demand disclosure, and rescue gratitude is explicitly separated from access to her time or affection.
- Paladin agency and character integrity: **93/100 - pass for this criterion**.
Yaniel chooses the meeting, topics, sword's role, touch, pace, and departure.
She rejects vengeance spoken in her name and retains faith, duty, and independent judgment.
The authorial dialogue is unusually explicit about boundaries, but her agency remains legible and consequential.
- Mature adult chemistry without excessive agreeableness: **87/100 - revision gate**.
The desire disclosure and requested hand touch establish an adult possibility with room for refusal.
The exchange is still mostly a consent-and-boundary demonstration, with limited attraction, wit, friction, or distinctly Yaniel-specific flirtation.
The many polished affirmations and acceptance lines risk making her too accommodating to the Commander's repair attempts.
Strengthen chemistry through her own desire and sharper individual voice while preserving these boundaries.
- Nonromantic, refusal, and withdrawal choices: **98/100 - pass for this criterion**.
The graph gives direct decline, friendship, touch refusal, uncertainty, hostile closure, repair without romantic reward, and independent departure.
Refusal does not secretly unlock pursuit, and touch withdrawal is respected.
- Source/report counts and topology: **98/100 - pass for this criterion**.
Independent checks found one scene, 17 unique nodes, 33 choices, and all 17 nodes reachable from `opening`.
The development record's stated 1,757 whitespace-delimited prose words matches a fresh `split()` count of 1,757.
The repository's Unicode-aware content tokenizer counts 1,758 prose words, which is a different counting method and not a contradiction.
The source and report hashes above match the requested pins.
- Gate and presence metadata honesty: **95/100 - pass for this criterion**.
The source comments state that the custom contract names are authored names rather than native etudes or verified flags.
The report explicitly says `Requires`, `Forbids`, `ActorContract`, `AreaContract`, `ContactContract`, and presence fields are descriptive metadata not enforced by the current runtime.
This is an honest disclosure, not proof those gates work.
- Style and graph hygiene: **100/100 - pass for this criterion**.
No U+2014 em dash occurs in the scene text or choices.
All choice targets resolve, all nodes are reachable, and terminal choices are visibly unlinked rather than accidental dangling targets.

## Required revisions and scope still open

The first two criteria and the chemistry criterion are below the required 91 threshold.
Before this opening can pass, bind identity, rescue, Radiance recognition, survival, contact, actor, and location requirements to verified native producers, and establish an actually reachable chronology for the cited garden meeting.
The custom metadata should remain labeled as design-only until those bindings exist.
Add a little more of Yaniel's self-directed attraction and particular voice without converting survival, trauma, or the Commander's good deeds into romantic credit.

No one of the ten mythic-path entries is implemented; every entry in `CONTRACT["path_access"]` is explicitly unresolved.
The prototype does not provide a complete route or meet the 21,000 meaningful-word planning floor.
It has no route progression, mature intimacy arc, outcomes, epilogue, integrated portrait or scene art, native flag/actor producer, save/load proof, ToyBox compatibility check, or game-runtime test.
The module remains excluded from the exported Story content according to its development record.

Review result: **not approved for integration or in-game testing**.
This result applies only to the pinned bounded opening and does not judge the character concept as infeasible.
