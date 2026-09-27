# Independent rereview 4: Devarra Trickster opening

Review date: 2026-09-27.

Reviewer voice: skeptical source, state-integrity, and character auditor.

This review applies only to the exact source and development-record hashes below.

Source: `storylines/devarra_trickster_opening.py`.

Source SHA-256: `374815D14C6676150DF54ABE867F109E3D8DC4CF89D7C818EE8DEA51899C2D1E`.

Development record: `reference/story-review/devarra-trickster-opening-development.md`.

Development-record SHA-256: `5299128579E9852CE690392501DAC50D24AF3DAE0F0EFA0AE522316E10A3996A`.

## Exact state-gate verification

The exported `SCENES` collection contains only the two outcome-specific scene variants.

The saved-brood scene requires both `devarra.brood.saved_verified` and `devarra.native_saved_brood_cue_seen`.

It forbids both `devarra.brood.lost_verified` and `devarra.native_lost_clutch_cue_seen`.

The lost-clutch scene requires both `devarra.brood.lost_verified` and `devarra.native_lost_clutch_cue_seen`.

It forbids both `devarra.brood.saved_verified` and `devarra.native_saved_brood_cue_seen`.

Neither exported scene has `RequiresAnyGroups`.

I confirmed the runtime predicate semantics in `src/Story.cs`: all required flags must be present, and any forbidden flag blocks the scene or choice.

I then asserted the valid saved state opens only the saved scene, the valid lost state opens only the lost scene, and missing, partial, or contradictory pairs open neither.

The `own_history` saved choice now requires the saved egg flag plus saved cue witness, and forbids both lost flags.

The lost choice symmetrically requires the lost egg flag plus lost cue witness, and forbids both saved flags.

The same valid, missing, partial, and contradictory state cases were tested at both choices, and each branch passed the expected truth table.

This closes the static cross-branch defect found in rereview 3.

The source still does not register producers for any of the custom egg or cue-witness flags.

Therefore, this proves the intended gate logic in the authored scene data, not that a real campaign can set the right state or reach either scene.

The internal `SCENE` template still contains its former any-of groups as construction input, but `outcome_scene` removes them from both exported scene variants.

This is not an active shortcut in `SCENES`.

## Structural checks

`python -m py_compile storylines/devarra_trickster_opening.py` passes.

The module's local graph checks pass for both variants.

Independent traversal followed each ordinary choice and every skill-check success and failure target.

Each variant has 23 nodes and 58 choices, all 23 nodes are reachable, and no target is unresolved.

All node narration has balanced `{n}` and `{/n}` tags.

The shared single-playthrough content count is 1,031 prose words plus 522 choice words, totaling 1,553 words.

The duplicated graph does not double the authored word count or route depth.

The development report retains a stale sentence saying that the local check reaches “all 20 nodes,” then gives the correct count of 23 nodes later.

That sentence should be corrected for accurate provenance.

These local checks do not validate native cue insertion, flag producers, in-game availability, rendering, save/load, or live-game behavior.

## Canon, chronology, and story quality

The native Tower cue anchor remains coherent for a proposed immediate continuation inside the DLC encounter.

The saved-brood cue directly acknowledges that the Commander killed Devarra and then speaks with her in the Tower.

The lost-clutch cue speaks her accusation there.

The prototype and its report appropriately avoid claiming that these DLC lines implement a main-campaign resurrection or an actor that persists outside that scene.

The mod still has no cue hook or second-conversation producer, so the encounter chronology is a design premise rather than an executable connection.

The custom egg-history and cue-witness checks likewise have no source-bound producers yet.

The dialogue's strongest character work remains Devarra's pride, capacity for a dry correction, wariness of flattery, explicit menace, and refusal to treat rescue or access as debt.

The tentative mouth-focused flirt is more charged than a generic compliment and does not convert interest into consent.

However, this is still a short opening with one suggestive line, not an adult romance with demonstrated mutual chemistry or sustained mature heat.

The calm therapeutic framing sometimes sounds more like the author's contemporary vocabulary than Devarra's native vengeful, imperious voice.

The Trickster idea is still not dramatized beyond offering this authored second conversation and rejecting the use of power to force an answer.

No quest chain, clever fate intervention, cost, preparation, roll sequence, or player-visible contact mechanism is implemented to make the opportunity feel earned.

The perception check gives useful success and failure branches, but its disputed report, dates, courier evidence, and witness follow-up remain authored placeholders without a native quest or producer.

## Separate scores

Each score is an independent review gate, not an average.

Any score below 91 fails the project threshold.

| Dimension | Score | Assessment |
|---|---:|---|
| Native Tower anchor and local encounter chronology | 93 | The native cues place Devarra in the Tower and support this proposed immediate continuation. |
| Scene-level egg and cue pairing | 97 | The two exported scenes require their exact matching positive flags and forbid both opposite-history flags, with no any-of group. |
| Choice-level saved/lost isolation | 96 | Both `own_history` branches now require their matching egg and cue pair and forbid the other pair; missing and contradictory-state cases fail. |
| Broader campaign chronology and live availability | 84 | The scene is not hooked, cue witnesses are not produced, and availability beyond the native DLC exchange is undefined. |
| Devarra characterization | 90 | Pride, danger, and resistance are present, but the reflective register remains uneven and needs further native-voice scrutiny. |
| Trickster-specific craft and access | 82 | The costly, credible Trickster method and quest-connected contact producer remain absent. |
| Consent and character agency | 96 | Refusal and departure remain meaningful, and no history or power grants intimacy. |
| Opening chemistry and mature tone | 86 | The flirt is improved but still only a brief spark, with little mutual adult heat developed. |
| Prose and authored evidence craft | 89 | The scene reads clearly, but the evidence chronology remains placeholder logic and some emotional framing is too contemporary. |
| Graph and markup structure | 96 | Both variants pass full local traversal, and all narration tags balance. |
| Integration and runtime readiness | 25 | Source remains unregistered and lacks cue/state producers, integration testing, actor delivery, art, and live-game verification. |

The exact scene and choice history-pair gates now pass static review.

The full review still fails the >=91-per-dimension threshold because chronology outside the cue, character voice, Trickster design, chemistry, prose, and runtime readiness remain below the bar.

## Readiness boundary

This is 1,553 words of shared opening dialogue rendered in two mutually exclusive, unregistered scene variants, not a complete route.

It does not implement the Trickster fate intervention, the other nine mythic paths, any cue or history producer, art, ToyBox compatibility, save/load behavior, integrated headless verification, or live-game testing.

It is not approved for integration or in-game testing.
