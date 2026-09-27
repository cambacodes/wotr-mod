# Independent rereview: Devarra Trickster opening

Review date: 2026-09-27.

Reviewer voice: skeptical canon, script, and player-agency auditor.

This review applies only to the exact source and development-record hashes below.

Source: `storylines/devarra_trickster_opening.py`.

Source SHA-256: `A6F503B04A674D2F7A1DE4C932A398EB1D7A79166BFD54FE3B6D81C0B514A82A`.

Development record: `reference/story-review/devarra-trickster-opening-development.md`.

Development-record SHA-256: `F6E0AD32795DEB1917D493794DA8C89825E983DA10F0D5A1A28C6C2542079B80`.

## What changed and what the native anchor proves

This revision has materially improved the earlier opening.

The authored scene is now explicitly scoped as a proposed continuation inside the native DLC1 Storyteller Tower encounter after one of Devarra's two inspected native cues.

That is a credible location and encounter anchor: the saved-brood cue (`8c53478782244b90a37f727f7b814318`) directly has Devarra say that the Commander killed her in their last meeting, that demons forced her to fight, and that the Commander spared her brood.

The lost-clutch cue (`d368680393304b5ba324dd5a517140ed`) directly has her accuse the Commander of the pillaged clutch and deaths before birth.

These cues establish Devarra's presence in that DLC scene and offer dialogue that can coherently be followed by an authored exchange there.

They do not establish a main-campaign resurrection mechanism, her availability outside that encounter, a time or place for an additional private meeting, or the mod's ability to insert a cue.

The revised development record now states these boundaries directly.

Accordingly, the native Tower anchor resolves the invented-room and immediate encounter chronology problem at the design level, but the cue hook and scene timing remain unimplemented, and the larger route still lacks a campaign-chronology contract.

The native state distinctions remain accurate against `reference/canon-review/female-dragon-roster.md` and its cited extracts.

The main-campaign `RedDragonDead` and `RedDragonKilledInIvorySanctum` etudes are distinct from DLC `Devarra_dead`.

The saved cue is conditioned on the brood rescue marker playing or the egg kingdom project being complete.

The lost-clutch cue has no cue-local condition, so the report is right that its text cannot be generalized without accounting for the actual cue path and positive history evidence.

The prototype appropriately discloses its need for a source-bound reader, a cue hook, and an actor check.

Those are design intentions, not implemented availability gates.

One logic gap remains in the scene's `RequiresAnyGroups`.

The first group requires either `saved_verified` or `lost_verified`, and the second independently requires either native cue-seen flag.

As written, these groups permit a mismatched pair such as saved-history verified plus the lost-clutch cue seen.

Because the branch-specific choices test only the custom saved/lost flag, the aggregate entry requirements do not prove that the native cue and verified history agree.

The contract's “exactly one” statement is not enforced by this source.

Use correlated alternatives (saved verified AND saved cue seen, OR lost verified AND lost cue seen), with a source-backed exclusivity producer, before treating the history gate as complete.

## Character, Trickster setup, and agency

The author addressed the earlier evidence-loop and markup issues and added more dragon-specific resistance and a clearer hint of attraction.

The Perception check now has distinct success and failure prose, neither grants affection, and failure leaves uncertainty rather than forcing the Commander to invent a fact.

The false report is a useful player-facing investigative beat, though the “dates” discrepancy and the claim about when the courier moved the eggs need a precise authored evidence model before becoming a real quest check.

The added line about an invitation not making a dragon her keeper's pet better fits an ancient, proud, physically formidable speaker.

Her dry amusement, impatient correction of “enemy,” irritation at manipulative flattery, and explicit refusal to reward power all support the intended voice.

The Commander's respect for refusal remains unusually explicit and preserves player and character agency.

The Trickster idea is still mostly a promised opportunity rather than a dramatized Trickster solution.

The contract says Trickster supplies the bespoke invitation, but neither the source nor report explains why this particular Trickster can add a conversation to a native DLC exchange, what they do to arrange it, what it costs, or what game quest pays off the egg evidence.

The refusal to use Trickster power to make Devarra answer favorably is an important boundary, but it does not itself demonstrate the clever, fate-bending route the project requires.

The revised romance spark is stronger: Devarra's mouth-focused appraisal and “I have not decided whether I want it silent” line add adult antagonistic flirtation while retaining threat and uncertainty.

It is still a brief opening signal rather than developed mutual chemistry or the mature relationship dynamic required of a full route.

The author correctly avoids treating it as courtship or consent.

## Verification

`python -m py_compile storylines/devarra_trickster_opening.py` passes.

With the repository root on `PYTHONPATH`, the source graph check passes.

Independent traversal through ordinary choice targets and each skill-check `Success` and `Failure` target found 23 nodes, 58 choices, all 23 nodes reachable, and no unresolved targets.

All node text has balanced `{n}` and `{/n}` tags.

The revised count is 1,031 prose words plus 522 choice words, for 1,553 total segment words.

The development record contains a stale sentence saying the check reaches “all 20 nodes”; the later sentence correctly says 23.

Remove that contradiction when next editing the report.

The graph and markup checks do not validate Unity rendering, cue insertion, flag production, actor delivery, or any live-game behavior.

## Separate scores

Each score is an independent gate.

Any dimension below 91 fails the project threshold.

| Dimension | Score | Assessment |
|---|---:|---|
| Native Tower anchor and local cue chronology | 93 | The native cues establish Devarra's presence and the two histories at this DLC encounter; this is a coherent proposed continuation point. |
| Broader campaign chronology and actor availability | 84 | The scene is not hooked, no post-encounter availability is implemented, and the main-campaign death/restoration cases remain unresolved. |
| Egg-history predicate integrity | 82 | The intent is transparent, but independent any-of groups permit a mismatched custom-history/native-cue pair and the exclusive producer is absent. |
| Devarra characterization | 90 | The dragon-specific pride and danger improved; several Commander lines retain the prior therapy-like framing, and the revised flirt needs later development. |
| Trickster-specific craft and credible access | 82 | The special invitation is asserted but no in-world Trickster scheme, cost, quest hook, or producer is specified. |
| Consent and character agency | 96 | Refusal, departure, and scrutiny remain meaningful; eggs, survival, gratitude, and Trickster power do not buy affection. |
| Opening chemistry and adult tone | 86 | Attraction has a sharper, more characterful hint, but mutual heat and relationship development remain slight at this opening stage. |
| Prose and scene craft | 89 | The investigation improves interactivity; prose is readable, though some contemporary abstractions and the evidence chronology need refinement. |
| Graph and localization markup | 96 | Expanded traversal covers check success/failure; all nodes are reachable and narration tags balance. |
| Integration and runtime readiness | 25 | Source remains unregistered with no cue hook, producers, actor delivery, integrated test, art, or game validation. |

This revision fixes the prior self-loop and unbalanced narration tags and improves the proposed encounter chronology.

It still fails the >=91 all-dimensions gate.

## Readiness boundary

This is a 1,553-word, unregistered opening, not a full romance route.

It does not implement any of the nine non-Trickster paths, a complete Trickster recovery route, the cue hook or outcome producers, art, ToyBox compatibility, save/load behavior, integrated headless verification, or live-game testing.

It is not approved for integration or in-game testing.
