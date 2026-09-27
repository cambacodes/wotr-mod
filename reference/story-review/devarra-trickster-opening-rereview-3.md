# Independent rereview 3: Devarra Trickster opening

Review date: 2026-09-27.

Reviewer voice: skeptical source and state-integrity auditor.

This review applies only to the exact source and development-record hashes below.

Source: `storylines/devarra_trickster_opening.py`.

Source SHA-256: `B688655EBBC2653302A45EA4176F924BEBA748F225824204B27977E95A56FDDE`.

Development record: `reference/story-review/devarra-trickster-opening-development.md`.

Development-record SHA-256: `93AB119702A8D4AB99969A19B55653BE6871061F63FC316E59603FC083563811`.

## Paired scene gate audit

The source now creates two scene variants from the same dialogue graph.

`devarra.trickster.saved_brood` requires both `devarra.brood.saved_verified` and `devarra.native_saved_brood_cue_seen`.

`devarra.trickster.lost_clutch` requires both `devarra.brood.lost_verified` and `devarra.native_lost_clutch_cue_seen`.

Both retain the Trickster, actor-confirmed, and history-read requirements, and neither retains the old any-of groups.

These exact positive scene requirements pass the requested static assertion.

The revised development record correctly discloses that the matching reader and cue-witness producers are not implemented.

The choice-level branches are still not isolated against inconsistent state.

In both scene variants, the `own_history` node's saved-brood option requires only `devarra.brood.saved_verified`, and its lost-clutch option requires only `devarra.brood.lost_verified`.

Neither choice also requires its matching native cue witness or forbids the opposite verified outcome.

For example, if both egg flags become true while only the saved cue witness is true, the saved scene passes its paired gate, but the lost-clutch option is still selectable there.

The converse can happen in the lost scene.

The source does not implement the history producer that promises exactly one flag, so that promise cannot be used as evidence that these cross-branch states are impossible.

Add matching cue and egg requirements plus an opposite-outcome forbid to each corresponding choice, or provide a separately tested invariant producer and assert that invariant at the choice gate.

The current exact scene pairing is an improvement, but the requested no-crossing property does not yet pass.

## Other verification

`python -m py_compile storylines/devarra_trickster_opening.py` passes.

The module's local graph test passes when run with the repository root on `PYTHONPATH`.

I independently traversed ordinary choice targets and `Check.Success` and `Check.Failure` targets for both scene objects.

Each variant has 23 nodes and 58 choices, all 23 nodes are reachable, and no target is unresolved.

Every node's `{n}` and `{/n}` narration tags balance.

The shared authored content has 1,031 prose words and 522 choice words, for 1,553 words in one playthrough copy.

The two scene variants duplicate the graph and do not double the route's authored depth.

The development record still has a stale sentence saying the graph check reaches “all 20 nodes,” followed by the correct per-variant count of 23.

Remove that contradictory sentence in a future edit.

The checks establish Python compilation and local graph structure only.

They do not prove any native cue hook, story-flag producer, actor delivery, campaign chronology, Unity rendering, save/load, or live-game behavior.

## Reassessment of the remaining review gates

The native Tower anchor remains a coherent design-level continuation point because the inspected native DLC cues themselves present Devarra in that encounter and establish their respective brood histories.

The saved-brood cue explicitly recalls that the Commander killed her, so the local encounter does not require this mod to invent a new resurrection inside that scene.

The anchor does not implement a cue hook or define post-DLC availability, and it does not resolve any proposed main-campaign recovery route outside the DLC encounter.

The dialogue retains Devarra's pride, danger, appetite for candor, capacity for dry amusement, and right to refuse.

The added flirt is more specific and charged than the previous version, while still leaving attraction tentative.

The route remains a single opening with modest chemistry rather than a developed mature romance.

The Trickster-specific intervention remains an assertion in the contract.

The opening does not yet dramatize a concrete Trickster scheme, quest connection, cost, or player-visible process that earns this extra contact while preserving Devarra's ability to reject it.

The evidence check adds useful interactivity, but the unimplemented report, false-date discrepancy, witnesses, and egg-history states need one coherent source-backed quest chain before the check can be treated as a meaningful game mechanic.

The first review's unmatched tags and evidence self-loop are fixed.

## Separate scores

Each dimension is an independent gate, not an average.

Any score below 91 fails the project threshold.

| Dimension | Score | Assessment |
|---|---:|---|
| Native Tower anchor and local scene chronology | 93 | The design now continues from a native encounter that presents Devarra and states the relevant histories. |
| Exact paired scene-entry requirements | 95 | Each cloned scene requires its matching positive outcome flag and native cue witness, with the broad any-of gate removed. |
| Choice-level outcome isolation | 82 | The opposite saved/lost option remains selectable if both outcome flags exist; exclusivity has no source producer yet. |
| Broader campaign chronology and actor availability | 84 | No cue hook or post-DLC availability is implemented, and restoration outside the native encounter remains unresolved. |
| Devarra characterization | 90 | Dragon-specific pride and resistance are improving, but the reflective modern register remains uneven and the romantic voice needs continued work. |
| Trickster-specific craft and access | 82 | No concrete, costly Trickster method, quest connection, or contact producer is authored. |
| Consent and character agency | 96 | Refusal and departure remain real outcomes; attraction, mercy, and power do not compel agreement. |
| Opening chemistry and mature tone | 86 | The new line creates a sharper spark, but this short exchange does not yet establish mutual adult heat. |
| Prose and scene craft | 89 | The investigative branch is functional as a draft, but the evidence facts and contemporary abstractions need refinement. |
| Graph and localization markup | 96 | Both 23-node graphs traverse all ordinary and check branches, and narration tags balance. |
| Integration and runtime readiness | 25 | The scenes remain unregistered and lack producers, cue hooks, actor delivery, integration tests, art, and game verification. |

The exact scene gate passes; the no-crossing branch requirement fails.

The overall revision therefore still fails the >=91 all-dimensions gate.

## Readiness boundary

This is 1,553 words of shared opening dialogue duplicated into two source-only scene variants, not a complete route.

It does not implement Trickster recovery, any of the nine non-Trickster paths, the cue or history producers, art, ToyBox compatibility, save/load behavior, integrated headless verification, or live-game testing.

It is not approved for integration or in-game testing.
