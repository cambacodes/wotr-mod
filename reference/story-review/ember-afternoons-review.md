# Ember afternoon contribution review

Reviewed source: `storylines/ember_afternoons.py`.
SHA256: `3271D913B8767C6C9F089AE1C671088EC1E744D42ED7C71D005B423946EA7D1E`.
Reviewer stance: continuity-focused character editor, assessing another author's work.
The review covers these five scenes and their relationship to the three existing `ember.py` opening scenes.
It does not approve Ember's complete route, artwork, runtime delivery or release.

Bounded writing score: **87/100**.
Bounded characterization and canon compatibility score: **91/100**.
Decision: corrections and rereview required before this contribution receives writing acceptance.
The characterization score cannot override the continuity findings or any missing full-route gate.

## What works

The play is a sustained activity with making, rehearsal, performance, criticism and actual revision.
It gives Ember something to want besides helping someone in distress.
She wants an audience, dislikes a criticism and initially mistakes disagreement for misunderstanding.
Those reactions keep her from becoming a source of effortless moral answers.
The bird's stuck beak, the fox's indistinguishable voice and the dispute over a laundry button are concrete and often funny.

The final alternatives actually perform different endings.
The bird can return for a shared song or enter the fox's gate after time apart.
Ember chooses what she wants to preserve rather than letting the Commander settle the story with a maxim.
Ilva can enjoy the work and still dispute its ending, which is stronger than having every listener converted by Ember's kindness.

The continuation correctly recalls General Manyboots or the Rain Inspector from the opening.
The earlier Commander intervention or restraint is not explicitly recited, but the new performance consistently leaves Ember to answer for herself.
It therefore preserves the lesson of that encounter without falsely claiming a particular earlier response.
It does not invent what the Commander drew during the shared-place or shared-fear branch.

The source remains entirely friendship content.
No adult romance, age-up, sexual framing, miracle, restored fingers or native quest resolution is added.
Chapter 3 restriction avoids applying these confident creative scenes unchanged to her later devastated outcome.
Presence, death, departure and absence restrictions use existing project predicates; this review has not independently certified their runtime implementation.

## Required corrections

### 1. The claimed attendance consequence does not occur

`courtyard_play.start` introduces both Ilva and Nessa unconditionally.
Nessa speaks or applauds later on both `stage_road` and `stage_waited` histories.
The road branch explicitly retains the originally chosen afternoon.
The sea branch says Nessa could not attend that original afternoon, and the handoff describes her attendance as a benefit of waiting.

This is a consequence mismatch across the alternatives, rather than a contradiction spoken within the road path itself.
Waiting does not actually enable an attendee the other choice lacks.
Make the attendance and subsequent speaker references reflect the chosen scheduling history, or replace the claimed attendance benefit with a different concrete consequence that the player really sees.
If Nessa is absent on the original afternoon, check every later reference to her, including applause, the defense of the fox and the request for another performance.
Changing only the introductory paragraph will not fix the whole sequence.

### 2. Waiting briefly assigns both puppets to Ember regardless of the player's role

In `missing_cloth.wait`, the rehearsal describes Ember beginning the sneeze without dropping either figure.
That node is available after the Commander selected `ember.player_fox`.
The next role branch immediately has the Commander operating the fox again.
No rehearsal handover explains the change.

Preserve the selected operator in this paragraph, or explicitly describe a brief handover and return.
The narrator role can retain Ember handling both figures.
This is a small but visible failure to honor an earlier choice in a contribution built around collaboration.

### 3. The fox acquires adequately provided feet on an ending that never supplies boots

`second_ending.fox` says the fox examines its feet and announces that they are remarkably well provided for.
This node depends on the player's performer role, not the earlier ending.
The explanation ending makes new boots for the fox, but the restitution ending supplies breakfast after carrying luggage and does not repair or replace its footwear.
The rehearsal explicitly establishes that the fox still wanted something to keep its feet warm.

Use a callback appropriate to each ending, or a shared declaration about leaving the bird's boots alone that does not imply an unplayed material outcome.
There is no need to invent another gift merely to preserve this sentence.

## Editorial improvements for the revision

Several Commander replies explain the emotional lesson more directly than the surrounding puppet activity needs.
Examples are `missing_cloth.disappointed`, `after_applause.company` and the final response after the gate performance.
One such line can suit a patient friend; repeated across the sequence, they make the Commander sound like an instructor delivering conclusions.
Keep more of the meaning in what the characters actually do, and let at least one reply be an ordinary practical suggestion or a joke.
This is a voice and pacing concern, not a request to remove the underlying distinction between kindness and obligation.

The final quiet-afternoon hook is good because it lets the player ask for a different kind of company without rejecting Ember.
The next contribution should honor that hook with a different activity rather than another five scenes about revising this same play.
Full-character depth will require other settings, reciprocal attention and native event connections.
Extending this one metaphor until it fills the word floor would weaken it.

## Canon basis and limits

Read sources were the frozen contribution, `storylines/ember.py`, `reference/parallel/ember-afternoons-handoff.md`, `reference/canon-review/ember-opening-native.json` and `reference/story-review/ember-aivu-full-companion-arcs.md`.
The native extract contains her initial refusal to have the frightened crusaders harmed, including `MeetEmber/Cue_0032`, GUID `a69e66dcfe68c72439e81567fe07b8ba`.
That supplies a concrete basis for her desire that the fox can do something better after wrongdoing.
It does not establish this play or its civilian audience as canon.
The design brief's cited native playfulness, refusal to be made a commander and ability to express personal wishes support this kind of friendship material.
Pella, Ilva, Nessa, the borrowed courtyard and the story remain explicitly authored inventions.

I found no new claim about Soot's private speech, Ember's powers, a healed disability or a completed redemption of a native character.
The performer distinction needs the continuity repair above, but manipulating imperfect puppets does not itself assert that her missing fingers have been restored.

## Verification and acceptance limits

The source hash was checked directly and matched the handoff.
The import succeeds with bytecode writing disabled.
A direct check found balanced narration markers in every node.
An earlier preliminary message questioned the first narration span; that was a reading error, and the concern is withdrawn.

The author's graph-walk counts are recorded in the handoff but are not represented here as independently rerun engine tests.
The review findings come from following the actual branch requirements and text joins.
No source, export, shared test, installed addon or artwork was changed by this reviewer.

The contribution's roughly 5,300 aggregate words remain a fraction of the 21,000-word character planning floor.
Its distinct branches do not prove complete-route attainable depth or parity with RanRomance.
Full-route writing and canon review, art review, Trickster access, later chapter progression, appropriate headless integration checks and game/save verification all remain outstanding.
Rereview must inspect the corrected source and its new hash; these scores do not automatically transfer to a later revision.
