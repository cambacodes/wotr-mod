# Mielarah route opening rereview 5

Review target: `storylines/mielarah_route_opening.py`.

Requested source SHA-256: `B2206C1C13A6DA7248ECCB9F6E00B3A40C4BD6AB27691A20281054D1F38BE6EA`.

Author report: `reference/story-review/mielarah-route-opening-development.md`.

Requested report SHA-256: `87D7F6C0E5616AF3E37C5B4182D2B8336D230F4CFE8ECD2B52C3469B4C64F26C`.

I verified both hashes before review and again after review; both still match.

## Verdict

This revision fixes the previous deterministic scene-validator defect by setting both `ManualOnly=True` and `Remote=True` on all eight scenes.

It adds a separate authored three-day repair and arrival passage between the Trickster hard landing and the living-contact flag.

Those are meaningful source-level improvements, and the local topology and state-contract assertions pass.

The contribution remains unregistered, and its prerequisite Trickster interception is still an invented flag with no runtime producer.

The regular route also lacks a verified native contact producer and later physical scene attachment.

The arrival, survival, repaired ship, and Colyphyr healer sequence are expressly counterfactual rather than native outcomes.

The contribution has no art and no complete relationship route.

Its entire eight-scene inventory is under half the project's 21,000-word single-character floor, even before distinguishing exclusive branches from reachable playthrough text.

It fails the project acceptance gate and is not ready for integration or in-game testing.

## Independent scores

Each applicable criterion is an independent gate and must strictly exceed 90.

These scores assess the exact requested source snapshot, not a planned future implementation.

- Canon and alternate-history framing: 94/100.
The source consistently distinguishes native branch evidence from authored survival and repair events, and it does not claim those inventions are canon.

- Chronology and native binding: 56/100.
The cited crash cue is conditional on selected `Answer_0351` and the active `CaptainMielara` etude, but the proposed pre-cue interception string has no verified selected-answer binding or producer.
The author acknowledges that neither cue suppression nor continued campaign progression is implemented.
The ordinary Colyphyr invitation likewise lacks its parent-choice chain, persistent flag, later actor location, and a tested extension point.

- Character fidelity: 88/100.
Mielarah retains command, pride, self-justification, anger, attraction, and the capacity to repeat a coercive act.
Her willingness to articulate every ethical caveat and romantic boundary at length makes the dialogue more self-explanatory and consistent than the game's sharper, more uneven characterization.

- Writing and scene craft: 86/100.
The chart, amulet case, captain's evening, crew meeting, and quay walk give the opening a coherent motif and escalating structure.
The dialogue repeatedly explains that attraction is not forgiveness, access is not consent, and command remains hers, sometimes restating a point already made in the preceding scene.
That repetition makes the prose feel like a careful design brief in places rather than a fully natural game expansion.

- Dramatic chemistry and romance: 84/100.
The mutual attraction grows through disagreement and a shared practical task, and the sensual beats remain specific to Mielarah's captaincy and guardedness.
The relationship is still an opening, with kissing and a tentative invitation rather than a developed adult romance or sustained intimate arc.

- Consent and agency: 96/100.
The player can leave or decline, Mielarah sets limits and pace, and the authored Trickster intervention cannot use rescue as payment for attraction.
The romance choices are not presented as a cure for her curse or an absolution for coercive magic.

- Trickster concept and authored choices: 92/100.
The proposal gives the Commander Arcana DC 26 and Perception DC 24 checks, a bounded wind deception, failure branches, and an explicit Mielarah veto while keeping her at the helm.
This score covers the authored design only; the prerequisite hook is not mechanically produced, so it does not mean Trickster access works in game.

- Trickster availability and mechanics: 18/100.
No runtime binding intercepts `Answer_0351`, suppresses `Cue_0426`, persists the survival outcome, or verifies that the campaign continues after the altered crash.
The authored checks are not registered game checks until the scenes and external producer exist in the mod.

- Source-model state design: 87/100.
The module's focused assertions pass for representative refusal, timing, arrival, contradictory-state, and cross-scene cases.
Those checks exercise the Python contract model, not the game scheduler, flag persistence, or actual native state.
The opening's ordinary native contact path remains unproduced, and the external Trickster hook is a placeholder.

- Route scope and selected-path length: 24/100.
I independently applied `tools/measure-story-content.py`'s tokenizer to the eight unregistered scenes and measured 9,438 raw and 9,438 distinct normalized-segment words.
That is the aggregate across all authored prose and choices, so no individual selected path can reach the 21,000-word floor.
The author reports 5,137 words for the modeled ordinary continuation and 4,814 for the modeled Trickster continuation; those modeled paths remain far short of the floor.
There is no complete romance route or all-path implementation.

- Art and visual fidelity: 0/100.
No Mielarah artwork is included for comparison with her in-game model or the requested character redesign.

- Registration and runtime readiness: 12/100.
The previous `ManualOnly` validation failure is fixed in this source: `src/Story.cs` requires manual-only scenes to be remote, and all eight scenes now satisfy that predicate.
`Rules.NextRemote` deliberately skips manual-only scenes, while `src/Main.cs` offers remote scenes through a manual `Read` button.
Because these scenes have no native contact unit or verified area restriction, this delivery can display narrated quay or ship scenes away from those locations.
The module is absent from `development/Story.json` and `expansion.py`, and neither its state producers nor save/load behavior have been integrated or tested.

Only the canon/alternate-history framing, consent, and authored Trickster concept score above 90.

The contribution does not pass the independent review gates.

## Evidence checked

- Source and development-report SHA-256 values were recomputed before and after review and match the requested hashes.
- `py -3.12 -m py_compile storylines/mielarah_route_opening.py` passes.
- `py -3.12 -m storylines.mielarah_route_opening` passes and reports eight unregistered scenes, 77 nodes, valid local topology and cross-scene state assertions, and no courtship commit.
- The independent content inventory reports 9,438 raw words, 7,533 prose words, 1,905 choice words, and 9,438 distinct normalized-segment words.
- `src/Story.cs` defines remote status from `Remote` or the `Memory` owner, excludes manual-only scenes from automatic `NextRemote` delivery, and rejects manual-only scenes that are not remote.
- `src/Main.cs` labels manual-only scenes as requiring the `Read` button and provides that button for remote scenes.
- Searches of `development/Story.json` and `expansion.py` found no Mielarah scene registration or runtime producer.
- The author's development record accurately labels all-path producers, physical integration, native Trickster interception, campaign continuation, art, full-route expansion, and game-level testing as incomplete.

## Required work before another review

- Bind the ordinary post-Colyphyr contact to the exact native parent-choice and survival state, then prove actor availability at the authored scene or revise the scene to a credible remote exchange.
- Implement and test the pre-crash Trickster answer interception, cue suppression, campaign progression, survival persistence, ship repair, and three-day arrival across save and load.
- Ensure the Trickster entry is available through an attainable, source-bound condition and preserves the native crash outcome on failure, refusal, or boundary violation.
- Provide attainable, character-appropriate route entries for all ten mythic paths, including the dead, expelled, and unavailable histories.
- Expand each intended playable route to at least 21,000 meaningful reachable words and independently measure selected paths.
- Continue the adult romance beyond this opening with consequential intimate development while preserving Mielarah's agency, conflict, and moral complexity.
- Create and independently review art against the in-game model and requested redesign requirements.
- Register only after native contact, scene delivery, flags, and progression are implemented and reviewed, then run the integrated headless verification before manual in-game testing.
