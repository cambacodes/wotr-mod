# Targona ten-path acquisition development

This report records an unregistered manuscript in `storylines/targona_trickster_acquisition.py`.

The new scenes extend the existing RanRomance Targona route for players whose parent history ended without a romance, including declined or missed courtship.

They do not overwrite the old answer or duplicate the parent romance scenes.

The current module has 64 authored scenes and 557 nodes.

The authored path set is Trickster, Angel, Azata, Aeon, Demon, Lich, Devil, Legend, and Gold Dragon.

Swarm remains unavailable because the reviewed native material does not establish that Targona survives there with her identity, freedom, and ability to answer as herself.

The module explicitly blocks the `swarm` state and contains no Swarm scene.

## New path-specific follow-through

Each authored path now has a distinct later relationship event after its future-planning scene.

The Trickster scene asks whether the Commander can leave a remembered refusal intact when another possible fate would have made the outcome easier.

The Angel scene returns to a wounded scout and gives Targona the words, without making her injury a lesson about virtue.

The Azata scene makes a harmless celebration create a real wayfinding mistake, so joy and responsibility both remain in the answer.

The Aeon scene preserves Targona's and Anograt's separate accounts rather than turning them into one convenient verdict.

The Demon scene tests whether the Commander can protect a patrol without using fear to make a dissenter obedient.

The Lich scene rejects using a dead guide as a tool and accepts a slower living investigation.

The Devil scene replaces an absolute patrol guarantee with terms that can be reviewed and withdrawn.

The Legend scene lets a working crew make the repair without treating the Commander's reputation as evidence.

The Gold Dragon scene makes the Commander fit into the repair crew's physical space and follow Targona's instructions.

Each follow-through has branches for working alongside Targona, supporting her decision without taking it over, overreaching, repairing an overreach, and ending the relationship.

The new continuation requires its path-specific `future_continuing` flag, which only the accepted shared-plan or open-plan options set.

The follow-through does not set the courtship flag unless its own continuation choice is accepted.

## Actor and contact contract

I removed the literal `ContactUnit="Targona"` from the public meeting and spar scenes.

The string was not a native actor GUID, so retaining it would make the manuscript claim an invalid actor binding.

The reviewed local evidence identifies the captive actor at `Units/NPC/Unique/Act_3_DemonsHerecy/AreeluLab/AngelTargona.jbp` as `81297c673b63b60448ef88a10db6bc78`.

That Act 3 captive unit is not evidence of a post-finale actor at the authored wayhouse.

The known Drezen spawner `2a27abe5-0d42-4a94-b564-7a406f406d44` belongs to `TargonaInDrezenNearFane`, `4c6d98e2205a9614d9b2d4b4c20ff445`, whose activation is Angel-gated.

I did not bind either GUID to these cross-path scenes.

The existing `targona.path_meeting_actor_verified` requirement remains an explicitly unproduced integration contract on physical scenes.

The local validator confirms that this flag has no choice producer in the manuscript.

The letters and remote follow-through also do not prove an in-game courier, actor, contact schedule, or correspondence producer.

## Cross-scene state simulation

The source validator simulates author-controlled choice flags across the authored route, rather than merely checking that flag strings appear somewhere.

For each authored path it walks the invitation into the public meeting, the accepted date into the spar, the spar into intimacy, the intimate scene into either separation or continuing relationship, and the together ending into future planning.

It also walks the declined-meeting friendship, the meeting that stays friendly, the romance decline, post-intimacy separation, the accepted together ending, the continuing follow-through, and the breakup outcome.

The Trickster simulation first walks the marker investigation and confirms that its bounded intervention flag precedes its invitation and meeting-pending flag.

The simulation never seeds native freedom, treatment, parent-ending, survival, mythic-path, correspondence, or actor flags.

Those remain external entry contracts whose real producers have not been implemented or tested.

The validator confirms the physical-scene actor requirement has no source-side producer and that no scene contains a `ContactUnit` field.

## Native evidence and authored additions

The native RanRomance treatment quest is `6ec03ce2f763460c8ac89f4c2064c5ad`.

The native nonromantic parent ending cues are `ad655c40be31401386b85287483b3841` and `cfc5f3cb2cf94672a96cab742e62225d`.

The reviewed parent-binding inventory contains the 12 tracked RanRomance histories, the completed treatment quest, and both nonromantic end cues.

The parent route's freedom, death, condemned, mythic-history, and ending markers are documented in `reference/canon-review/targona-parent-bindings.json` and `reference/canon-review/targona-route-evidence.md`.

The authored courier report, warning marker errand, runner, public wayhouse, actor verification flag, and all post-finale letters are new story material.

No reviewed native source establishes that these authored events or contact producers exist in the game.

The Trickster marker paradox is exclusive to Trickster.

The other eight paths use their own path-framed concerns and do not inherit the Trickster fate intervention.

The manuscript continues to distinguish the Commander helping Targona from Targona choosing desire, intimacy, or a relationship.

The Lich material keeps her alive and refuses to substitute an undead copy or memory for her consent.

The Aeon route treats Anograt as a separate voice and does not assume that she joins Targona's relationship.

## Selected-chain counts and remaining length

Counts below include each displayed node's text and the labels of choices on one longest reachable chain through the relevant authored scenes.

They do not count source code, hidden alternatives, parent-route text, or runtime dialogue that has not been integrated.

The Trickster chain is 4,175 selected words, comprising 3,743 node-text words and 432 selected-choice-label words.

The Angel chain is 3,076 selected words, comprising 2,712 node-text words and 364 selected-choice-label words.

The Azata chain is 3,047 selected words, comprising 2,683 node-text words and 364 selected-choice-label words.

The Aeon chain is 3,033 selected words, comprising 2,669 node-text words and 364 selected-choice-label words.

The Demon chain is 3,045 selected words, comprising 2,681 node-text words and 364 selected-choice-label words.

The Lich chain is 3,048 selected words, comprising 2,684 node-text words and 364 selected-choice-label words.

The Devil chain is 3,047 selected words, comprising 2,683 node-text words and 364 selected-choice-label words.

The Legend chain is 3,047 selected words, comprising 2,683 node-text words and 364 selected-choice-label words.

The Gold Dragon chain is 3,055 selected words, comprising 2,691 node-text words and 364 selected-choice-label words.

Each chain remains far below the 21,000 meaningful selected-playthrough word floor.

The additional path events improve differentiation and continuity, but they do not make any path complete or ready.

The current source revision has not received an independent review.

## Verification

`$env:PYTHONPATH='.'; python storylines/targona_trickster_acquisition.py` passed its graph and cross-scene authored-state assertions.

`python -m py_compile storylines/targona_trickster_acquisition.py` passed.

`git diff --check -- storylines/targona_trickster_acquisition.py reference/story-review/targona-ten-path-development.md` passed.

These checks do not validate native GUID resolution, state producers, scene registration, actor placement, path availability, ToyBox behavior, save/load, rendering, or Unity gameplay.

The module remains unregistered in `expansion.py` and absent from the exported `development/Story.json`.

The ten-path story access matrix remains incomplete because Swarm is deliberately unresolved.

The three-dimensional correspondence art, integration, runtime checks, and independent review also remain open.

## SHA256

Source SHA256: `FEB583B3D91C8266DBDF22E73E758CBD7DAA94847CCB72F85E8723646C749873`.

This report is a development record, not an approval, readiness claim, or promise of review scores.
