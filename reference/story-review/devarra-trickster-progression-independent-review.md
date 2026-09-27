# Independent review: Devarra Trickster progression prototype

Review date: 2026-09-27.

This review covers only the exact source and development-record hashes below.

It is an independent assessment of an unregistered progression prototype, not approval of a complete romance route or in-game test build.

Source: `storylines/devarra_trickster_progression.py`.

Source SHA-256: `8253C8A0CF6FBAE83777770159C37E756470DD499975E3CF9D91ABA01539ABFF`.

Development record: `reference/story-review/devarra-trickster-progression-development.md`.

Development-record SHA-256: `F1FD2D1E017D19D2AC6D3CABE6C1B1230D5A0D3CF8E0887F45130BBBD0D81D9F`.

I verified both hashes before and after this review.

## Findings

The prototype handles Devarra's two brood histories with care in its prose.

It does not invent an egg recipient, claim that the rescued eggs were returned to her, or make romance payment for loss, mercy, or investigation success.

Those are strong boundaries, consistent with the local dragon roster audit and with the prior review of `devarra_trickster_opening.py`.

The native references in the development record agree with that audit: Tower Cue_27 is the saved-brood account with its native egg-release or project conditions, Cue_0006 is the fallback lost-clutch account, and the two main-game death markers are distinct from the DLC `Devarra_dead` etude.

I also verified the opening's current hash and rereview 4, which rejects its broader chronology, voice, Trickster mechanism, chemistry, and runtime readiness.

This progression consequently has no accepted opening, native state producer, registered entry, verified post-cue actor, or continuity outside the proposed Tower encounter.

The prototype's evidence task, contract, inventory, witnesses, tests, archive, and magical trace are openly labeled as new authorship.

That candor is good, but there is no native quest or script evidence connecting those invented objects to the campaign.

The Trickster role remains mostly a label and a temptation to alter a record or an answer.

The draft does not yet show the Commander preparing a credible intervention, using a real quest connection, paying a fate-related cost, or making a hard-won opportunity possible after a canonical death.

The dialogue gives Devarra pride, vengeance, suspicion of flattery, and sharp corrections.

Several passages instead explain her boundaries in contemporary therapeutic language through the narrator or Commander.

Examples include describing an invitation as something that must not become a debt, repeatedly spelling out that uncertainty must not be taken, and framing the archive in procedural consent terms.

The themes are appropriate, but the repetition makes some of the scene sound like a modern ethics exercise rather than Devarra's dangerous, imperious encounter with a resourceful Trickster.

The adult chemistry is tentative and mutual in principle, and the scene properly allows refusal.

In practice, the romantic section has one explicit attraction exchange and one brief, nonsexual touch.

It ends at an invitation that Devarra may make later, before a second meeting, sustained desire, adult intimacy, or a route-level relationship has been written.

This is a restrained opening beat, not the mature, spicy romance content the project requires.

### State and check defects

The top-level history requirements do not actually bind each egg state to its matching native cue.

`RequiresAnyGroups` asks for either saved or lost history in one group and either saved or lost cue in another group.

As confirmed in `src/Story.cs`, every group needs one present flag, but the engine does not pair the choices across groups.

Therefore saved-history plus lost-cue and lost-history plus saved-cue states both pass the scene gate.

The existing opening does author exact paired variants, but this progression does not require those matched pairs and has no producer enforcing them.

The local `validate()` assertion compares the group tuple shape only; it does not exercise the four combinations or reject the two crossed states.

Three skill checks can be retried through dialogue cycles, so their stated failure consequences are not durable.

The Perception path loops from `teach_method` through `pride_test` back to `teach_method`, allowing another roll on the same marks.

The Diplomacy path loops from `read_statement` through `witness_terms`, `witness_presence`, `witness_detail`, and `witness_boundary` back to `read_statement`.

That can repeat the check after a failed interview, despite the text saying the witness will not speak again that day.

The Arcana path loops from `vengeance_terms` through `trace_failure` and `record_choice` back through `vengeance_question` to `vengeance_terms`.

The source has no check-attempt or outcome flags guarding those nodes, and its local graph validation checks reachability and target existence only.

The World check does not appear in a retry cycle in this graph, but the prototype has no executable integration test of check outcomes or their persistence.

The `TRUST`, `PRIDE`, and `MISTRUST` flags are set by choices but are not read by any later requirement or branch in this source.

They therefore record labels without changing what scene or relationship state becomes available.

## Verification performed

The exact source's local command reports 47 nodes, 47 reachable nodes, 123 choices, five skill-check choices, and 4,812 words when choice labels are included.

Its reported 3,565 words of scene prose are still far below the project floor of 21,000 meaningful words for an individual route.

Choice labels do not count as route prose, and the duplicated entry histories or repeated play through cycles cannot increase the meaningful content count.

The module's local graph/content assertions pass, `python -m py_compile` passes, and `git diff --check` passes for this source.

I independently traversed its edge listing and confirmed all 47 nodes are reachable.

Those checks do not catch the mismatched history/cue combinations or the repeatable check loops described above.

The source is not registered in `expansion.py` or the export, and it has no cue or flag producers, continuation actor, art, ToyBox test, save/load test, all-path access logic, or integration/runtime check.

No Unity or live-game behavior was established.

## Independent rubric

Every applicable project dimension must score above 90 to pass.

| Dimension | Score | Assessment |
|---|---:|---|
| Canon boundary and source attribution | 94 | The record separates native egg/death facts from invented evidence and does not assign the rescued clutch to an unsupported recipient. |
| History-state integrity | 58 | The two any-of groups accept crossed saved/lost combinations, and the local assertion does not detect them. |
| Devarra characterization | 86 | Pride and vengeance land well, but repeated contemporary procedural language dilutes her native danger and authority. |
| Trickster specificity and fate intervention | 65 | Trickster is invoked as leverage or temptation; no earned, quest-connected fate intervention is dramatized. |
| Character agency and consent | 94 | Refusal is explicit, and evidence, rescue, and attraction are not treated as consent. |
| Adult chemistry and mature tone | 61 | Mutual attraction is a brief spark with one light touch; there is no sustained adult heat or intimate progression. |
| Choice consequences and check integrity | 54 | Three checks can be farmed through graph cycles, and trust/pride/mistrust flags do not affect later branches. |
| Dialogue craft | 84 | The prose is clear and sometimes sharp, but narration repeats the same procedural boundary lesson and the witness task is invented scaffolding. |
| Graph and local structural verification | 88 | All nodes are reachable and targets resolve, but validation misses mismatched state pairs and retry cycles. |
| Route scope and content floor | 17 | This is a 4,812-word progression scene, not a complete route, and it falls short of the 21,000-word minimum. |
| Integration, art, path access, and runtime readiness | 12 | It is unregistered and lacks producers, full route access, ToyBox evidence, art, integration checks, and game verification. |

## Decision

This prototype is useful as an authored evidence-and-terms scene, but it fails the project's independent review gate.

Do not integrate it or call Devarra ready for manual in-game testing.

Before another review, bind the saved and lost histories to their matching native cue witnesses and test all four state combinations.

Break the retry cycles or persist attempt outcomes so each check failure changes what the player can do.

Give the Trickster a specific, costly, campaign-connected way to earn continued contact that preserves Devarra's power to refuse.

Revise the voice and romantic section, then continue the route through its major relationship stages until the full meaningful-content floor, other required path handling, art, ToyBox behavior, integration checks, and headless verification can be reviewed.

Passing the source-local checks does not establish any of those remaining requirements.
