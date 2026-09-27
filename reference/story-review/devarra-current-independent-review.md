# Independent current review: Devarra Trickster route draft

## Exact snapshot reviewed

`storylines/devarra_trickster_opening.py` SHA-256: `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.

`storylines/devarra_trickster_progression.py` SHA-256: `379C6599D343C705EEC1EB66A3688500955227DA1875CAFD9A827D6C5EE2A1A5`.

`reference/story-review/devarra-current-development.md` SHA-256: `B9CB41F0F69B58F39385989433036423AEE732101BF5A35C375B42FEB78224A5`.

The opening hash differs from the originally supplied pin, and the corrected development snapshot records the current opening hash above.

I reviewed the exact files shown here, not the mismatched opening snapshot.

## Verdict

**Fail for route readiness and the 21,000-word route floor.**

This is a thoughtful, structurally varied writing prototype with strong consent boundaries and careful handling of Devarra's two egg histories.

It is not a full romance route yet.

The longest compatible saved-brood romance path is 5,724 selected words, and the lost-clutch path is 5,684 selected words.

Both are far below the hard 21,000-word minimum, and the romantic payoff currently reaches only a consensual kiss.

The Trickster access and actor continuity are descriptive proposals, not implemented or demonstrated events.

## Independent route-length calculation

I independently loaded both modules and traversed their choice graphs with each choice's `Requires`, `Forbids`, and `Set` flags applied.

For skill checks, I explored both success and failure edges.

I counted selected node prose and the selected choice labels with the report's word-token convention, excluding `{n}` markup and unselected alternatives.

The longest selected path to the saved-brood invitation is 649 words.

The longest path from that invitation through evidence work to `end_interest` is 2,310 words.

The slate case path to `case_complete` is 1,235 words.

The meal path to `meal_end_romance` is 1,530 words.

Those compatible branches total 5,724 words, which is 15,276 words below the required floor.

For the lost-clutch opening, the longest path to invitation is 609 words.

Its compatible route total is 5,684 words, or 15,316 words below the floor.

These are longest paths; shorter player-selected routes also exist.

The module graph checks pass when run with the repository root on `PYTHONPATH`.

The opening reports two reachable 23-node variants.

The progression reports 48 reachable evidence nodes, 18 slate nodes, and 16 meal nodes.

My graph traversal reproduced all four development-report selected-path numbers for the saved-brood route.

## Canon and authored alternate development

The native evidence correctly supports two distinct histories.

In DLC1 Storyteller Tower Cue 27 (`8c53478782244b90a37f727f7b814318`), Devarra says the Commander killed her, that demons forced her to fight after taking her clutch, and that the Commander showed mercy to her brood, so she does not consider the Commander an enemy.

Cue 0006 (`d368680393304b5ba324dd5a517140ed`) is the alternative account in which her clutch was pillaged and her offspring died before birth, followed by her vengeful hiss.

The authored opening keeps these accounts apart, uses both verified-history and matching-cue gates in its specific variants, and does not treat mercy, rescue, or attraction as interchangeable.

The evidence scene also avoids inventing a recipient for rescued eggs or claiming to know where they went.

The Tower cues are evidence that the DLC encounter presents Devarra there.

They do not prove that a main-campaign Devarra killed by the Commander was bodily restored, persists after the encounter, or has an available actor for later scenes.

The draft explicitly labels restoration, actor continuation, custom condition producers, and cue hooks as unimplemented, which is candid and correct.

Those same omissions prevent this from being a playable route.

The hard Trickster requirement is not met by the present text.

The route is gated to Trickster and rejects using mythic power to override Devarra's choice, which is appropriate for consent.

But the actual plot offers no authored fate intervention that creates the later contact, preserves a main-campaign-dead Devarra, or otherwise makes the impossible possible through Trickster planning.

The proposed bounded restoration exists in metadata only.

The route needs an actual quest-linked sequence with clear prerequisites, cost, consequences, and a source-backed actor or restoration plan, while leaving attraction and consent solely to Devarra.

## Characterization, agency, and romance

The best characterization comes from Devarra's pride, threat, dry corrections, anger, and refusal to let the Commander claim ownership of the rescued brood or her grief.

The romantic arc makes her initiative legible: she decides whether to continue, identifies mutual interest, sets the terms of a meal, and chooses whether to kiss.

Refusals close the route rather than becoming hidden approval, and neither skill checks nor successful investigations can set her attraction by themselves.

That agency is a real strength.

The main weakness is voice and dramatic texture.

Many exchanges repeatedly explain limits, consent, uncertainty, record handling, and the Commander's obligation not to interpret silence.

The themes fit the events, but their repeated procedural wording gives Devarra and the Commander a contemporary counseling register and makes several scenes feel like an ethics exercise.

Devarra remains dangerous and proud in places, yet her distinctive dragon authority and vengeful sharpness are often softened by extended discussion of emotional process.

The Commander is usually careful and accommodating, with too little of the Trickster's wit, misdirection, improvisation, or morally complicated resourcefulness.

This risks the agreeable-Commander problem the project explicitly prohibits.

The opening has a memorable adult flirt line about the Commander's mouth, and the meal culminates in a chosen kiss.

Across the full compatible route, however, the romantic and sensual material is very slight.

There is no sustained desire, escalating adult intimacy, or mature relationship consequence yet.

The route needs significantly more romance, erotic tension, and character-specific heat without making Devarra agreeable or turning her anger into consent.

## Gameplay and branching

The checks mostly serve the scene's actual investigation: reading dates and seals, interviewing a witness, noticing a magical trace, and handling the slate incident.

Success and failure produce different information or trust consequences, and the authoring uses one-shot attempt flags rather than inviting repeated rolls until success.

This gives the draft useful play structure.

The check design does not yet express a bespoke Trickster acquisition method.

Most checks test ordinary skills, and none demonstrates a fate-bending plan with a credible cost and persistent consequence.

The saved and lost openings offer distinct motives, information, and emotional tone, then converge on the same evidence, case, and meal scenes.

The distinction is present and responsibly handled, though the shared continuation has little branch-specific content after the opening.

The graph modules verify unique reachable nodes, balanced narration tags, check targets, and attempt-flag constraints.

The draft is designed as a finite graph, and the measured routes terminate.

This does not prove replay safety in the game because custom flags have no registered producers, scene order has not been exercised, and the scenes are not hooked to native cues.

The local module checks are source-level evidence only.

## Scores

These are independent scores for the pinned writing draft, not readiness scores and not predictions of other reviewers.

| Dimension | Score | Assessment |
| --- | ---: | --- |
| Canon and source alignment | 92 | The native saved and lost histories are distinguished and the draft labels its major additions. Actor continuity and resurrection remain proposals rather than supported current events. |
| Devarra characterization | 82 | Pride, vengeance, menace, and sharp corrections land; the repeated counseling register dilutes her native danger and authority. |
| Commander and Trickster characterization | 71 | The Commander can be thoughtful, but dialogue leans agreeable and procedural. Trickster wit and a concrete fate intervention are missing. |
| Agency, consent, and refusal handling | 96 | Devarra owns the invitations, attraction, pace, and kiss. Refusal has consequences and is not reinterpreted as consent. |
| Meaningful checks and consequences | 86 | Investigation checks are one-shot and affect evidence or trust, but they do not create the bespoke Trickster acquisition or route continuity. |
| Finite graph and replay-safe design | 84 | The source graphs are reachable and finite under local checks. Runtime flag producers, scene ordering, and repeated-play behavior remain unverified. |
| Saved/lost branch quality | 88 | The opening treats both native histories distinctly and the common continuation avoids contradicting either; branch-specific follow-through is limited. |
| Mature romance and character-specific heat | 49 | Flirtation and a freely chosen kiss are present, but the route lacks sustained mature intimacy and the heat requested for a full romance. |
| Compatible path length and completeness | 27 | The longest route is 5,724 words saved and 5,684 lost, far below 21,000, and the relationship is only beginning. |

## Final disposition

Keep this as a promising, unregistered writing prototype, not as a ready route or a route that has passed the project quality gate.

Preserve its history distinctions and strong agency rules while expanding the emotional and sensual arc, making Devarra's voice more dangerous and specific, and writing an actual quest-connected Trickster intervention.

Before readiness review, every compatible route needs at least 21,000 meaningful selected words, source-backed native state and actor handling, registered cue and flag producers, and verified runtime ordering.

The current files do not establish art, ToyBox behavior, in-game compatibility, or a route that is ready for manual play testing.
