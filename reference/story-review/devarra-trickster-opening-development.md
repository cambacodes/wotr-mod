# Devarra Trickster opening: development record

Source: `storylines/devarra_trickster_opening.py`.
Source SHA-256: `374815D14C6676150DF54ABE867F109E3D8DC4CF89D7C818EE8DEA51899C2D1E`.

This is a source-only, unregistered opening experiment for the expanded Devarra route.
It does not establish a romance, implement the proposed Trickster follow-up producer, restore Devarra beyond her native DLC encounter, deliver an actor, or alter a native quest.
It is not ready for integration or in-game testing.

## Native facts used

The local [female dragon audit](../canon-review/female-dragon-roster.md) identifies Devarra as a female red dragon and mother of a clutch, which supports adult portrayal without inventing a numeric age.
The audit records the main-campaign death etudes `RedDragonDead` (`581521b398fb9dd4eb52bbfffb3b5c43`) and `RedDragonKilledInIvorySanctum` (`056ba61e04cca104a9c95ac2d4658c67`).
Those distinct markers must be read directly before any recovery proposal is evaluated.
The DLC etude `Devarra_dead` (`d713e8b772484376a7da810c37ab7922`) is not a substitute for the main-campaign death states.

The native DLC dialogue distinguishes two egg histories.
In `World/Dialogs/DLC1_Megaepic/StorytellersTower/Chaleb/Cue_27.jbp` (`8c53478782244b90a37f727f7b814318`), Devarra says demons forced her to fight and recognizes that the Commander spared her brood.
In `Cue_0006.jbp` (`d368680393304b5ba324dd5a517140ed`), she names the pillaged clutch and her offspring who died before birth.
The latter cue has no local condition, so an absence of the saved-brood marker cannot prove the loss branch.
This prototype therefore expects a future source-bound history reader to record exactly one verified outcome before offering branch-specific dialogue.

The authored opening is now explicitly designed as a continuation inside the Storyteller Tower encounter after one of those exact native Devarra cues.
That DLC text already places Devarra in the scene, including a history where she says the Commander previously killed her.
The mod still needs a cue hook, and this presence is not evidence that a main-campaign body was restored or that Devarra persists beyond the DLC event.

## Authored alternate development

The 23-node scene gives Devarra room to reject, correct, or leave the Commander.
Mercy, survival, a rescued brood, and the Commander's power never award affection.
Her lost clutch remains a loss rather than a wound the romance magically repairs.
The player can ask about the egg report, take a Perception check whose failure only preserves uncertainty, make an intrusive attempt at flattery and repair it, or close the contact.
Devarra's possible interest is deliberately tentative and is not a courtship commit.
This is new dialogue, not recovered game dialogue or evidence of her canonical attraction to the Commander.

The `CONTRACT` ties the intended entry to the existing DLC encounter and describes a separate voluntary invitation as an authored Trickster-specific opportunity.
The cue hook, invitation producer, checked history reader, and actor verification remain unimplemented.
The `CONTRACT` explicitly leaves any fate intervention, body restoration outside the native DLC scene, route access, and all nine non-Trickster paths unimplemented.
No score or review approval is claimed.

## Local verification and remaining work

The source compiles with `python -m py_compile`.
Its local graph check reaches all 23 nodes from `arrival` in each scene variant and confirms all targets resolve.
The source contains two duplicated scene variants, one for each matching egg-outcome and native-cue pair.
Each variant has 23 nodes and 58 choices, with 1,553 words in a single-playthrough copy of the opening: 1,031 prose words and 522 choice words.
The duplicated scene records do not add route depth or count twice toward length.
The local graph check follows ordinary choices and skill-check success/failure targets, reaches all 23 nodes in each scene object, checks exact paired scene and choice requirements plus mutual exclusions, and verifies balanced `{n}` / `{/n}` narration tags.
The prototype remains outside `expansion.py` and the exported `Story.json`.

The first independent review of source SHA256 `4F80F456262E57EDAA9F53D71E8D3575EEDC467E063F19D9735B367AFBBFC4FA` failed chronology, voice, Trickster setup, chemistry, markup, graph, and runtime gates.
Rereview 2 of source SHA256 `A6F503B04A674D2F7A1DE4C932A398EB1D7A79166BFD54FE3B6D81C0B514A82A` confirmed the markup and loop fixes and found that the two independent any-of groups could mismatch an egg outcome and native cue.
Rereview 3 of source SHA256 `B688655EBBC2653302A45EA4176F924BEBA748F225824204B27977E95A56FDDE` confirmed paired scene gates but found that contradictory egg flags could still expose the wrong `own_history` choice.
The current source adds the matching native cue to each choice and forbids the opposite outcome at both scene and choice level.
Rereview 4 of source SHA256 `374815D14C6676150DF54ABE867F109E3D8DC4CF89D7C818EE8DEA51899C2D1E` confirmed the static saved/lost gate truth tables and graph, but retained sub-91 findings for broader chronology, character voice, Trickster setup, chemistry, prose, and runtime readiness.
No cue hook, state producer, complete route, or live behavior was approved.

The current source still needs a credible, tested Trickster contact mechanism, native-bounded egg and death outcome handling, a real solution for living contact after a main-campaign death, all-path access, and full-route content at or above the project floor.
Art, ToyBox compatibility, save/load, concurrent-route, headless integration, and live-game verification remain open.
