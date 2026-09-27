# Independent review: Mielarah route opening

Review target: `storylines/mielarah_route_opening.py`.

Target SHA-256: `9780A287686EE9C0DBF74189FCD111937C526ED37CF2C5C97211A2CBF1D4B17B`.

Author development report: `reference/story-review/mielarah-route-opening-development.md`.

Development report SHA-256: `3D922E53A7D05E7F488F4A95316FFD39DBAE52EBA2B6FFBDAC40D9F74C8A2DC2`.

This report reviews that exact source snapshot only.

## Verdict

This is a careful, consent-aware opening draft with a strong central question: what responsibility means when command decisions become other people's danger.

It is not approved for integration or in-game testing.

The largest blockers are unsupported survivor/contact chronology, absent path mechanics, and a romance turn that is too abstract and early to establish Mielarah's mutual desire convincingly.

The opening is not a complete route and cannot meet the route length requirement: it contains 2,477 authored words, against the 21,000-word per-character planning floor.

That floor is an inventory target rather than proof of reachable, distinct playthrough content.

## Independent scores

Scores are separate judgments on this opening, not averages or forecasts for a finished route.

Any score below 91 fails the requested gate.

- Character fidelity: 86/100 - the captaincy, principled self-image, coercive magic, and refusal to accept easy absolution fit the cited material; the polished aphorisms and controlled self-analysis risk giving her the author's modern therapeutic vocabulary instead of a more individually recognizable voice.
- Consent and agency: 96/100 - refusal closes contact, rescue and gratitude are explicitly not romantic currency, uncertain attraction is not treated as assent, and the hand touch follows a specific yes with narrow limits.
- Canon and chronology: 78/100 - the draft knows the fatal Ishiar crash, separate raid death, Aeon expulsion, and curse must be distinguished, but its opening presupposes a living, contactable captain and moored ship without a verified branch-specific chronology or producer.
- Dramatic chemistry: 81/100 - the accountability conversation gives both parties room to disagree, but the attraction is mostly stated in concepts such as compelling, unnerving, and uncertain; the scene does not yet establish a specific shared experience or Mielarah's unmistakable, character-grounded desire.
- Mythic-path specificity: 25/100 - ten concise access pitches exist, but they are explicitly unverified notes rather than attainable routes, conditions, consequences, or implemented Trickster fate intervention.
- Implementation evidence: 20/100 - the file self-checks local topology and contract flags, but is unregistered, has no runtime producer, native GUID binding, actor/survival verification, or game execution evidence.
- Mature writing and scene craft: 89/100 - the coercion confession has moral complexity and the scene avoids making intimacy a reward; however, the opening remains largely a discussion of accountability and the bounded hand touch, with no developed sensual escalation or later relationship material.
- Scope and route completeness: 12/100 - one optional opening scene is only a small start and is far below the route volume floor.

No criterion passes the 91-point gate except consent and agency.

## Evidence and checks

I independently pinned the exact source and development report hashes above before review.

`python -m py_compile storylines/mielarah_route_opening.py` passes.

`PYTHONPATH=. python storylines/mielarah_route_opening.py` passes its local assertion and reports one unregistered scene, 14 nodes, valid topology, and no courtship commit awarded.

An independent traversal from `start` reaches all 14 nodes; there are no unreachable nodes in this scene graph.

Using the repository inventory tokenizer, I measured 2,477 raw words, comprising 2,093 prose words and 384 choice words; exact normalized segment count is also 2,477.

The shared inventory tool expects exported `Story.json`, so it cannot directly accept this Python authoring module; the count was reproduced from its normalization and word-count rules over `SCENES`.

The module header and producer contract correctly label survival, contact, and all path access as unimplemented.

The ten `PATH_ACCESS` strings are design assertions, not source-backed unlock paths.

In particular, the Trickster wind-corridor idea is currently a sentence in an access map, not a stateful quest intervention or proof that a route remains attainable after each native outcome.

The cited native evidence was checked against the repository's curated `additional-candidate-table.md`, `additional-candidate-table.json`, and `candidate-extra-mentions.json` extracts.

Those extracts identify `World/Dialogs/c4/AirAdventures/Cue_0006.jbp` (`8235006c1e10df244a3467c7b3900f2a`) and `Cue_0426.jbp` (`1b4e78245cb3a244588f9ec0fda54ea8`), and preserve the relevant text about her ship, curse, captaincy, and crash.

The same extracted evidence includes the separate raid death at `Cue_0482.jbp`, coercive thought-correction at `Cue_0328.jbp`, and Nocticula's Aeon expulsion at `World/Dialogs/c4/Mythic_Aeon/C4Aeon_Judgement/C4Aeon_Tumberd_Court/Cue_0010.jbp`.

I did not independently open the original native `.jbp` assets in this review, so the extracted catalog is evidence of what the repo records, not a fresh verification against raw game assets.

## Required revisions before another review

Provide a source-backed fate table for every native C4 outcome, including the fatal crash, hostile raid death, successful survival/contact states, and Aeon expulsion; do not route a confirmed death into a living romance without a separately evidenced, authored restoration mechanism.

Replace the placeholder path map with explicit, reviewable conditions and consequences for all ten paths, including a bespoke Trickster intervention whose setup, risk, roll or decision, failure states, and respect for Mielarah's refusal are described.

Strengthen chemistry through a specific reciprocal choice or shared test tied to her captaincy and code, while retaining a credible possibility that she dislikes or rejects the Commander.

Rework portions of the dialogue to distinguish Mielarah's voice from general moral-philosophy prose and verify whether her self-description and terminology match native speech.

Expand this opening into the complete route and demonstrate meaningful distinct content, reachable branches, and a substantial continuation before claiming the route-length target.

Commission character art and review it against the game's model and portrayal; this source snapshot contains no art to assess.

After those changes, obtain a fresh independent review against the exact new source hash.
