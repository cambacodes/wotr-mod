# Independent review: Targona revision 2

## Scope and verdict

I independently reviewed `storylines/targona_trickster_acquisition.py` at SHA256 `2C4D4F95A5CFB3C3F03E397ACA4827C35EAAFF30398B8DE3CD09750DF3503EF3` and the associated development report at SHA256 `1603B305D09462D51E630888D41BC15C9DBF2D19B6CD72E845236528017854CA`.

Both requested pins matched before review and were rechecked after writing this report.

This is an independent review of the current snapshot, and the earlier failed review of a 10-scene version is historical evidence only.

The manuscript is substantially more thoughtful than a route sketch, but it is not ready for route or game use because the actual selected paths remain far below the project's 21,000-word complete-route floor, required branches are missing, and the exported physical meeting and sparring scenes use an invalid contact-unit identifier.

The strict project gate is greater than 90 for every applicable criterion, and this snapshot does not pass that gate.

## Criterion scores

| Criterion | Score | Assessment |
|---|---:|---|
| Native binding evidence and canon attribution | 95 | Parent RanRomance bindings and nonromantic end cues are cross-checked, and the new errand is labeled authored alternate material. |
| Characterization | 88 | Targona's caution, service, humor, and boundaries are recognizable, though the repeated scene template and repeated “old answer/new question” framing flatten some path differences. |
| Consent and relationship agency | 95 | The route repeatedly permits refusal, separates aid from affection, gives Targona control over touch and pace, and makes coercive orders end the relationship. |
| Trickster specificity | 93 | The marker contradiction provides a bounded, rule-limited intervention tied to Trickster perception and wit rather than an arbitrary fourth-wall exception. |
| Mythic-path access and state logic | 68 | Nine path branches are authored, Swarm is not, and neither current-path flag production nor cross-scene eligibility has been proven in the game. |
| Consequence and choice design | 89 | Skill checks change certainty, tactical outcome, or planning quality, and ordinary safety choices matter, but the local graphs do not establish that the intended state transitions compose across scenes. |
| Prose and content craft | 87 | The writing is clean and controlled, but repeated explanations and parallel scene scaffolds reduce the sense of nine independently developed routes. |
| Complete-route scope and length | 18 | The longest Trickster chain is about 3,821 words and non-Trickster chains are about 2,684 to 2,721 words, far below 21,000 meaningful words per complete route. |
| Art and visual approval | 0 | The portrait key is a placeholder and there is no completed or reviewed art. |
| Export, integration, runtime, saves, and ToyBox | 12 | The module is unregistered, physical-scene contact IDs fail the native-unit validator, and no in-game, save/load, or ToyBox test exists. |

These are independent review estimates, not automated scores or a prediction of eventual approval.

## What works in the manuscript

The authored alternate is clearly separated from established events: the development report states that the courier-marker errand, runner, safe stop, and meeting are new material, and the story itself calls the errand newly authored rather than a recovered base-game quest (`reference/story-review/targona-ten-path-development.md`, “Evidence and limits”; `storylines/targona_trickster_acquisition.py`, `a_measured_impossibility` opening).

The Trickster intervention has sensible limits: it can test whether the marker is physically touched, cannot identify or draw a person, cannot move the marker or anyone else, and expires after one test (`storylines/targona_trickster_acquisition.py`, `the_second_letter` nodes `careful` and `route`, and `a_measured_impossibility` node `start`).

The relationship does not treat the original no as a hidden yes: Targona says the earlier answer remains valid, chooses whether to reopen contact, and repeatedly states that help does not buy romance (`storylines/targona_trickster_acquisition.py`, `the_second_letter` nodes `start`, `report`, and `decline`; `add_path_frame` node `invite`).

Physical intimacy is optional and explicitly negotiated, including asking before touch, respecting the wing boundary, stopping when asked, and keeping a no-romance friendship route (`storylines/targona_trickster_acquisition.py`, `add_meeting`, `add_spar`, and `add_intimate_invitation`).

The path frames show useful character-sensitive distinctions, including the Angel's faith, the Azata's humor, Aeon's separation of Anograt's voice, Demon's anger, Lich's refusal to treat life as possession, Devil's explicit terms, Legend's mortal future, and Gold Dragon's scale (`storylines/targona_trickster_acquisition.py`, `PATH_FRAMES`, `PATH_MEETING`, and `PATH_FUTURES`).

The authored checks are generally tied to the scene: Perception and Knowledge: World alter certainty, Athletics changes the bout, and Diplomacy tests whether the Commander can make a negotiable future plan (`storylines/targona_trickster_acquisition.py`, `the_second_letter`, `add_path_frame`, `add_spar`, and `add_future`).

## Blocking and material findings

**Invalid native contact IDs block production validation.** Eighteen meeting and spar scenes set `ContactUnit="Targona"` (`storylines/targona_trickster_acquisition.py`, `add_meeting` and `add_spar`, lines 230-250 and 290-297).

`src/Story.cs` requires every non-null `ContactUnit` to parse as a GUID in `N` format and throws `Invalid native contact unit` otherwise (lines 372-375).

The runtime also requires a scene's `ContactUnit` to appear in `Snapshot.AvailableContacts` (`src/Story.cs`, lines 229-237), so replacing the string with a syntactically valid GUID alone will not prove that a Targona actor can be contacted on each path.

**The content is still an opening rather than a complete route.** The development report counts 3,821 words for Trickster and 2,684 to 2,721 for the other authored paths, while acknowledging the hard 21,000-word minimum (`reference/story-review/targona-ten-path-development.md`, “Validation and content size”).

Those counts are consistent with an independent sum of each scene's longest local branch, but they are not proof that every maximum branch is mutually compatible across the full scene sequence.

Even treating those reported totals as generous estimates, every route is short by roughly 17,000 to 18,300 words and lacks enough developed relationship, mythic consequence, conflict, and resolution material to meet the complete-route constraint.

**The authored path graph omits Swarm.** `PATH_FLAGS` and `PATH_ENTRY_PLANS` include Swarm, but `PATH_FRAMES` and the generated meeting, spar, intimacy, ending, and future scenes omit it; the source assertion explicitly expects only eight non-Trickster frames (`storylines/targona_trickster_acquisition.py`, lines 46-60, 169 onward, 360-377).

The development report appropriately leaves Swarm unresolved because survival, identity, freedom, and contact evidence are absent, but this means the requirement for an attainable Trickster route for every romance character is not met for this route and the advertised path coverage is not complete (`reference/story-review/targona-ten-path-development.md`, “Evidence and limits”).

**Scene-local checks do not verify cross-scene eligibility.** `validate_graphs()` proves unique local node IDs, local target validity, local reachability, and acyclicity only (`storylines/targona_trickster_acquisition.py`, lines 377-405).

It does not simulate setting `meeting_pending`, `date_accepted`, `spar_complete`, `committed`, and `ending_together` across the separately scheduled scenes, nor prove the associated `targona.path_meeting_actor_verified` flag is ever produced.

The meeting and spar require that unproduced actor flag, while the development report confirms that no native producer, contact actor, courier stop, or cross-path scheduler has been implemented (`storylines/targona_trickster_acquisition.py`, lines 249, 274, and 296; development report, “Evidence and limits”).

The local graph assertions pass, but this is not evidence that an authored route can be traversed in a game save.

**The module is not registered or exported.** No reference to `targona_trickster_acquisition` or `targona.trickster_acq` is present in `expansion.py` or `development/Story.json`, so the manuscript is not currently available through the built story package.

**The current-path state and eligible history combinations need a real producer audit.** The scene gates require current mythic flags alongside a tracked prior-path history and parent treatment completion, but the development report explicitly notes that the local naming precedent does not prove those flags or combinations resolve in an actual save.

The parent GUID audit is useful evidence for the treatment completion quest and end cues, and I independently confirmed that the four base-game etudes are not RanRomance-owned while the 15 RanRomance-owned references are present in the parent binding inventory.

That binding check does not establish that all eleven history states are reachable, that the correct path flag is preserved after path transitions, or that a new actor contact becomes available on each path.

**Visual, runtime, persistence, and ToyBox readiness remain unverified.** The scenes use `TargonaCorrespondence` as a placeholder portrait, no reviewed art is included, and there are no exporter, runtime, save/load, or ToyBox Free Love and No Jealousy results in this snapshot.

## Checks rerun

`python -m py_compile storylines/targona_trickster_acquisition.py` passed.

`python -m storylines.targona_trickster_acquisition` passed its in-module assertions.

Importing the module constructed 55 scenes and 494 nodes, and enumerated 18 meeting and spar scenes with the invalid literal contact unit.

The native binding comparison matched the audited parent assembly inventory for the RanRomance-owned GUID references but did not prove runtime availability or route registration.

## Required revisions before another readiness review

Replace every literal contact-unit name with a verified native actor GUID, and implement and verify a contact producer that makes the actor available for each supported path and location.

Register the module in the story exporter and validate the resulting package with the production `Story` validator.

Add an explicit cross-scene state simulation or integration test that traverses friendship, decline, meeting, spar, intimacy, committed, unfinished, and future outcomes without fabricating unavailable actor or mythic state.

Resolve whether Swarm is intentionally unavailable or provide a canon-grounded, tested survivor and contact route before claiming all-path availability.

Expand each selectable route to at least the required 21,000 meaningful words along a real compatible selected path, then review the completed path rather than extrapolating from local scene totals.

Complete and review the character art, then test runtime delivery, save/load continuation, and ToyBox Free Love and No Jealousy behavior in a representative live save.

## Final disposition

This snapshot is a promising and unusually careful acquisition manuscript, but it fails the required complete-route scope, path coverage, production validation, integration, art, and live verification gates.

Do not mark the route ready for manual game review or as a complete romance route on the basis of module-local checks.
