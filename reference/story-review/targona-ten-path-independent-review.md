# Independent review: Targona ten-path continuation

This review targets source SHA256 `FEB583B3D91C8266DBDF22E73E758CBD7DAA94847CCB72F85E8723646C749873` in `storylines/targona_trickster_acquisition.py` and development report SHA256 `5B8B0D153C4A75D6524666D1968C05AFB8DE78A6F3155F27E10174959F397312` in `reference/story-review/targona-ten-path-development.md`.

The source and development report hashes matched before inspection and were rechecked after review.

I also inspected `storylines/targona_opening.py` at SHA256 `517AAA3B923EC23F2E54ABED31064778A1528CAD1309865297A71C9EA25E8DBD` to understand the existing parent-route boundary.

## Decision

**Fail for route readiness and manual in-game review.**

This is a substantial and carefully structured continuation manuscript, not a complete romance route under the project's requirements.

The report's longest modeled selected chains range from 3,033 to 4,175 words, well below the hard 21,000-word floor per supported path.

The Trickster path is the only one that has a bespoke fate-intervention opening, and it has meaningful skill and choice branches, but the corresponding ordinary-path access material does not establish Trickster access to this character's complete romance alongside all the other routes.

The authored transitions are simulated locally, but the scenes still depend on unproduced native and contact flags, the physical scene actor is not bound, and the source is not registered in the exporter or development story payload.

The source art key has an independently reviewed illustration, but book-size crops and in-game display have not been verified.

## Scores

| Dimension | Score | Assessment |
| --- | ---: | --- |
| Canon distinction and source honesty | 95 | The report separates native treatment, parent endings, and path history from the authored courier, marker, wayhouse, contact, and post-finale events. |
| Targona characterization | 91 | Her practical care, guarded humor, service, altered wing, and insistence on her own choices remain legible across the manuscript. |
| Consent and relationship agency | 96 | Refusals, friendship, pauses, changed boundaries, and separation remain available, and help is not treated as payment for desire. |
| Trickster fate intervention | 92 | The marker contradiction and bounded one-test effect use Trickster's wit and reality-bending while explicitly limiting what the trick can do. |
| Mythic-path differentiation | 88 | Eight path frames and later decisions have distinct thematic situations, but they share much of the same contact and relationship scaffold, and Swarm remains unavailable. |
| Choice and skill-check design | 89 | Perception, Knowledge: World, Diplomacy, Athletics, and planning decisions affect certainty or approach, but several checks can be bypassed and do not consistently change later consequences. |
| Cross-scene state and repeatability | 77 | The local simulator exercises authored flag handoffs, but it does not prove native prerequisites, actor/contact production, or one-shot scheduling in game. |
| Prose and relationship development | 88 | The intimacy is adult, direct, and character-conscious, although repeated consent explanations and parallel path scaffolds sometimes make the writing feel instructional. |
| Selected-playthrough length | 12 | The longest modeled chain is 4,175 words against a 21,000-word minimum, and all other reported paths are shorter. |
| Art asset and visual readiness | 86 | The `TargonaCorrespondence` source illustration passed its scoped art review and is staged, but runtime crops, book sizing, readability, and actual game presentation remain open. |
| Export and integration readiness | 10 | The acquisition module has no match in `expansion.py` or `development/Story.json`, and physical scenes require a contact-verification state with no producer. |
| ToyBox, save, and runtime behavior | 10 | No live game, save/load, or ToyBox Free Love/No Jealousy run is supplied for this manuscript. |

No dimension should be read as an approval score for the complete route.

The project's strict gate is greater than 90 in every applicable dimension, and this snapshot fails multiple hard gates independently of editorial scores.

## What works

The Trickster opening treats the original nonromantic answer as final for its own time and makes the new approach a separate question.

Its Perception success distinguishes the dispatch dates, while failure preserves uncertainty and still allows a cautious investigation or refusal.

The bounded Trickster intervention cannot identify or summon a person, move the marker, or compel Targona to accept an encounter.

Across the nine authored path frames, assistance is kept separate from romance, and the Lich branch avoids using the dead as a substitute for a living person's consent.

The later scenes include public meetings, sparring, intimacy, relationship endings, future choices, and path-specific follow-through, so this revision reaches well beyond the earlier short invitation-only draft.

The staged art is materially more advanced than a placeholder: `reference/art-review/targona-v2-review.md` records an independent review of the exact source illustration, while `art/expansion/scene-art-staging.md` clarifies that the source images are not approved runtime portraits.

## Blocking findings

**The modeled paths are far too short.**

The pinned development report counts the longest Trickster chain at 4,175 selected words and the eight other path chains at 3,033 to 3,076 words.

These are substantial opening arcs but only about one fifth of the required minimum on Trickster and roughly one seventh on the other paths.

The source includes 64 scenes and 557 nodes, but scene and node counts do not replace the meaningful selected-playthrough floor.

**Swarm remains explicitly blocked.**

`BLOCKED` contains `swarm`, the module has no Swarm scene, and the development report appropriately says that native evidence for Targona's identity, freedom, and survival there is absent.

This is an honest limitation, but it means this module does not provide a route for every candidate or path scenario that the project may ultimately require.

**Native prerequisites and the physical contact producer are unresolved.**

The scenes require parent treatment completion, a nonromantic ending cue, survival and freedom flags, path history, and `targona.path_meeting_actor_verified`.

The report says the first parent bindings are evidenced, while the meeting actor flag, wayhouse actor, courier scheduling, and correspondence producers are authored contracts without verified runtime producers.

The physical meeting and spar scenes correctly omit the invalid literal `ContactUnit="Targona"`, but they cannot become reachable physical scenes until a real contact actor and producer are supplied and tested.

**Local graph validation is not integration proof.**

`py -m storylines.targona_trickster_acquisition` passes the module's graph and authored cross-scene simulations, and the source's path walk covers friendship, decline, intimacy, breakup, future, and follow-through outcomes.

Those simulations intentionally do not seed native path, survival, treatment, ending, or actor state, so they prove authored choices can set flags after entry but not that a real save can satisfy entry requirements.

Scene delays do not establish one-shot scheduling or prevent re-entry after their cooldown; the live scheduler and persistence behavior remain untested.

**The module is absent from the checked export.**

A search found no `targona_trickster_acquisition` or `trickster_acq` match in `expansion.py` or `development/Story.json`.

Consequently the manuscript is not present in the checked built story payload and cannot yet be tested by playing it in the game.

**The art is source-reviewed, not runtime-approved.**

The exact Targona v2 source illustration has review scores above 90 for the listed art disciplines, and its hash matches the staged image.

However, the art review explicitly excludes runtime files, dialogue-size crops, small-display legibility, and actual page transitions.

The single correspondence illustration also does not demonstrate scene-specific visual coverage for the full route.

## Checks and limits

`py -m storylines.targona_trickster_acquisition` passed its local graph and authored-state assertions during this review.

Source inspection confirmed that the module has no `ContactUnit` value and that no choice produces `targona.path_meeting_actor_verified`.

Exporter and story-payload search returned no acquisition-module registration.

The source and development report SHA256 values were rechecked after the review and remained `FEB583B3D91C8266DBDF22E73E758CBD7DAA94847CCB72F85E8723646C749873` and `5B8B0D153C4A75D6524666D1968C05AFB8DE78A6F3155F27E10174959F397312` respectively.

This was a source, report, and local-validation review only.

It did not launch the game, render the art, validate installed blueprints, exercise a save, or test ToyBox.

Do not mark the Targona route complete or ready for manual playthrough review on this evidence.
