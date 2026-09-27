# Devarra partnership repair and eastern continuation

Author development record, not an independent approval.
The route remains below the required 21,000-word minimum on its shortest completed paths.

## Frozen inputs and output

Input review: `reference/story-review/devarra-partnership-independent-review.md`.
Input progression SHA256: `3FB5F4425E94412399F3AA310859EB66B34EF22203F25E4A7766C57429C2F206`.
Revised progression SHA256: `077D96A12BC4E283AD56AFFD25DDC66C5C0B6CB4270852CC5D632D6A5CE20A73`.
Unchanged opening SHA256: `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
Only the assigned progression source and this report were edited.

## Reproduction before repair

The closest available source-level reproduction followed the emitted saved-history scene from its actual `Nodes[0]`, evaluating choice requirements and applying selected choice flags.
With either `home_taken` or `home_declined`, the selected path was `return_choice -> return_claimed|return_roaming -> return_power -> return_unarmed -> return_answer -> return_partners -> return_farewell -> return_depart`.
All selected edges were eligible and the partnership coda became eligible.
Neither selected history contained a cup, but the eligible coda explicitly recalled one.
This reproduced the semantic contradiction without pretending that source traversal was an in-game test.

## Repairs

The coda recalls the shared appointment rather than the cup which exists only on the purchased-house branch.
Both codas now require completion of the new eastern account scene, so the retrospective cannot become eligible before the additional visits occur.
The twelve combinations of two brood histories, three property outcomes and two relationship arrangements each permit exactly one coda.
Removing the final account flag permits neither coda.
Source assertions prohibit the cup reference in each eligible coda.

Replaced the quarry's explanation about a cart waiting for the player with the weighhouse record and the workers' sleeping shed.
Replaced assurances about households joining the crusade, inspections implying cohabitation, automatic shared-home ownership and conjured furniture with concrete requests, preparations and repairs.
Replaced the partnership's survey of all possible house outcomes with observed crows, and replaced retrospective procedural wording about the buyer with the next available address.
The late quarry route still cannot recover Serevin or her ledger and never resets the departed cart opportunity.

## Added selected content

Four new unique visits follow the partnership decision, with 24-hour delays between them.
They use existing `scene`, `page`, `c`, `Requires`, `Forbids`, `Set`, `Check`, `DelayHours` and terminal-choice behavior.
No new engine field or blueprint identifier was introduced.

- **An evening without an alibi:** the promised supper actually happens before the next dispute.
  Devarra's embroidered coast, missing sailor, appetite for cities and inconvenient memories give her something to discuss besides contracts or the Commander.
  Both story choices establish the blue-painted brick used later.
- **The buyer at the western gate:** a merchant has sold false protection connected to the western property dispute.
  Purchased, seized and declined property outcomes produce different explanations for how the claim became believable.
  Keeping the vault map supplies evidence directly; burning it requires the docket and carter, giving the merchant time to warn the store.
  Public exposure and purchasing the surviving claim produce separate later consequences.
- **A door without permission:** an unauthorized delivery frame damages an occupied house.
  The one-shot Arcana 35 turn requires a cleared loading arch and an inspected catch.
  Failure breaks a tooth, causes additional masonry damage and forces supported dismantling without a reroll.
  Ordinary manual dismantling remains available from the start.
  Destroying or dividing the device produces different immediate Devarra responses and persistent outcome flags.
- **The price of an address:** restitution, the mill clerk's actual culpability and either public complaints or the purchased debt are addressed.
  Failed improvisation has a separate repair account and personal exchange.
  Successful or manual dismantling acknowledges the supported lintel and her physical work instead.
  The evening returns to the brick, embroidered ship, distant city and an invitation that still allows ambition and disagreement.

Devarra does not forgive the destruction of a useful object merely because the Commander chooses it.
Lethra does not accept an ambitious dragon's curiosity as justification for damage to her house.
Adrast attempts to substitute damaged flour for restitution.
Talvren's clerk is culpable for circulating an unsigned offer, but the prose does not invent proof that he wrote the extortion demand.
The public path does not automatically recover stolen funds, and the purchased debt does not establish ownership of the receiving agent.
No new physical intimacy is mandatory.

## Reproducible verification

Run `python -m storylines.devarra_trickster_progression` from the repository root.
This passes structure/reachability, cycle, paired-history delivery, prior branch staging, lower-vault/quarry checks, partnership exclusivity and the new eastern consequence checks.
The new `validate_eastern_consequences()` follows actual selected choice states through all three dismantling methods and both device outcomes for each brood history.
It checks mutually exclusive method pages, single-use checks, resulting damage-menu eligibility and exactly one device disposition.
It also checks the twelve coda combinations and both brick producers.

The new `selected_completed_word_bounds()` uses the repository's word-count function.
It starts at `Nodes[0]`, follows eligible choices with their effects, explores success and failure, excludes aborted or refused completions, and projects only flags required by future visits.
It includes the unchanged matching opening, skips the quarry retry only when the kiln already completed, and adds exactly one eligible terminal coda.
It does not add the two brood variants together or count mutually exclusive scenes as simultaneous reading.

| Native history | Minimum selected words | Maximum selected words | Shortfall to minimum |
| --- | ---: | ---: | ---: |
| Saved brood | 18,173 | 24,097 | 2,827 |
| Lost brood | 18,214 | 24,097 | 2,786 |

There are eighteen unique main progression visits, one optional quarry retry and two unique codas.
Those produce forty-two history-guarded delivery definitions, not forty-two different visits.
The printed legacy `continuation_max_words` measures an older subset and must not be used as the full-route metric.
The relevant full-route result is `selected_completed_route_words`.

## Canon and implementation limits

The saved and lost brood histories remain distinct and neither is rewritten by romance or a recollection.
The merchant, householder, cloth, foreign city, warehouse and miniature frame are authored expansion material, not claims about native dialogue or native quests.
The frame extrapolates from the route's already authored vault apparatus, not a newly discovered canon Trickster power.
Nothing here proves Devarra's native restoration or acquisition bindings.
The existing emitted actor-contact and physical-presence assumptions remain integration work; this authoring pass does not implement native spawning or availability.
No installed-game export, engine E2E test, localization validation or in-game timing test was performed within this exclusive source assignment.
Four additional daily visits need chronology review before integration.

## Review requests and remaining work

A different reviewer must judge characterization, prose, romance quality and every applicable rubric on the frozen source.
No score or approval is assigned here.
Review the implied payment enforcement and warehouse geometry particularly closely; they are authored situations which need to remain credible rather than paperwork that magically binds opponents.
The retained apparatus and purchased eastern debt deliberately remain potential future obligations, not falsely completed quests.
The separate-visits and partnership choices share these later meetings; the reviewer should decide whether their practical distinction needs additional later development.
At least 2,827 meaningful selected words remain necessary on the shortest compatible completion, before any independent quality gate can consider the route length complete.
New scenes should develop consequences of the retained/destroyed apparatus, the receiving agent or a distinct shared ambition rather than add inventory recitations or mandatory intimacy.
