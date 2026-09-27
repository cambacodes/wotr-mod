# Devarra lower-vault development handoff

This is an author handoff, not independent approval.
The starting progression SHA-256 was `48A46A34AF6532BD4163B89D38FA52FCC08218E04134C57F1ED824D80F3E9AC4`.
The revised progression SHA-256 is `1A2C085F77B9297934C1CC26BFAEFE6C63A7985318E2BA42FF4D878DA732392D`.
The unchanged opening remains `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
Only the assigned progression source and this development record were edited.

## Review repairs

The proprietary-employment callback now occurs only on the compulsory-service history, in `kiln_employment`.
Spared and killed Vey histories proceed directly to the appropriate shard or physical inspection without hearing that claim.
The kiln delivery delay is now 144 hours, matching the six-day appointment.

The physical-inspection menu now offers a real withdrawal before its check.
That choice ends the encounter and sets `kiln_retreat` without spending the inspection attempt.
The original kiln scene forbids the retreat state, so it cannot be selected again as a fresh attempt.
A separate one-hour return scene begins with a new first page and offers either one resumed inspection or abandonment of the unfinished operation.
It forbids an already attempted inspection, a completed kiln, an abandoned retry and the incompatible intact-shard history.
The resumed scene removes the retreat loop and retains the original one-shot check flag.
A player who abandons the return has knowingly left this quest incomplete; the route does not pretend the prisoners were rescued.

Serevin now tests a handler ring before stepping under her lamps.
She believes it exempts the owner from binding and uses the beam to put the lamps between herself and Devarra while keeping the Commander within reach of the latch.
The Trickster exploits the distinction between protected owner and delivered subject, making her occupy both roles.
Her cooperation now follows an apparently verified protection and tactical position instead of the narrator declaring the challenge too small to refuse.
This remains authored magical logic requiring independent credibility review.

## Lower-vault continuation

The ruined watchtower contains the collectors' operating apparatus rather than another collector demanding a sale.
Captured Serevin and her ledger provide the entrance sequence and an unwarned approach.
The earlier custody page now actually supplies that sequence, avoiding an invented later recollection.
Escaped Serevin has visited the site, destroyed destinations and begun emptying the apparatus into the stream.
The nearby settlement creates a concrete cost for lingering over the machinery.

Vey's fate changes the first landing.
A spared Vey's warning supplies partial suspicion.
The still-bound man's account book identifies the omitted safety catches.
The released man's voluntary description supplies the same practical information after his book is returned; that description is now present in the earlier settlement scene.
Killing him leaves the Commander and Devarra to dismantle the counters with less information.
Devarra does not apologize for the killing or deny its investigative cost.

The apparatus stores copies of departures, not captive souls.
Its Tower plate explains the authored collectors' recurring hold on Devarra's continued presence.
An old copied nest sketch produces separate saved-brood and lost-clutch reactions.
It supplies neither an egg recipient nor a survivor contradicting the verified history.
Devarra destroys the targeting detail herself.

The Commander can destroy the targeting apparatus and vent its waste away from the settlement, or attempt a prepared Trickster return through a one-shot Arcana check.
An intact shard and the broken-shard scar provide separate approaches to the connection.
Success stops the apparatus while preserving material for a further choice.
Failure forces emergency venting, destroys the targeting map and exposes the party's location to connected buyers.
The successful player can erase the targeting lines or negotiate shared control of the remaining map.
Devarra requires destruction of her own plate and divided control of the weapon.
Trying to retain her plate against that condition ends the relationship.
The agreeable-companion shortcut is deliberately unavailable.

## Relationship continuation

A separate rooftop scene follows two days later.
It responds to the retained map, destroyed map and exposed departure through different pages.
The retained-map route opens a disagreement over extortion versus investigating captives.
The destroyed-map route lets Devarra regret lost power without secretly reconstructing what she agreed to destroy.
The exposed route posts a watch and treats a possible reconnaissance object as uncertain evidence rather than claiming the threat vanished.

Devarra proposes inspecting a western ruin for a place of her own.
The Commander can approach its ownership through negotiation, force, or visits without planning a shared home.
Those choices establish different intentions for the next quest; they do not claim that the ownership dispute has already been played or resolved.
The scene ends with a chosen kiss, nonphysical company, or immediate departure.
The latter two paths terminate without visiting the kiss page.
She remains in dragon form throughout this manuscript, with no unimplemented humanoid transformation implied.

## Delivery and validation

The source contains nine main progression narrative templates with 200 nodes, plus one retry template containing 17 nodes that reuses the unfinished kiln continuation.
The delivery collection has twenty exact-history variants.
Together with the opening, there are ten main narrative scenes; the optional retreat adds a separate return event rather than a second full kiln story.
History variants and reused retry text receive no aggregate content credit.

The inspected runtime begins a book scene at `Nodes[0]`.
Its `Entry` field is interaction text, not a target node ID.
Every progression delivery variant now uses the scene title as its readable interaction label and retains the intended entry page first in `Nodes`.
The internal templates keep their entry IDs for authoring, while carried-state delivery tests start at the actual first node.
The unchanged opening has not been altered under this task's ownership restriction.

`py -m storylines.devarra_trickster_progression` passes.
`py -m py_compile storylines/devarra_trickster_progression.py` passes.
`git diff --check -- storylines/devarra_trickster_progression.py` passes.

Graph validation covers every delivery template, including retry reachability, cycles, targets, balanced narration and one-shot attempts.
The exact-history test checks every history combination for all ten template pairs.
The carried-state continuation now includes the envelope, bridge, cistern, kiln, optional return, lower vault and rooftop.
It preserves matching outcomes while pruning only flags unused by remaining predicates or final invariants, avoiding an unnecessary combinatorial test cost.
Completed paths require one Vey fate, one shard fate, one Serevin fate, the correct service settlement and exactly one kept/burned targeting-map result.
The specific staging check verifies the six-day wait, fate-specific employment passage, first-node delivery, retreat without spending the roll, one-hour reentry, no repeated attempt, and quiet/departure paths without a kiss.

These are local manuscript checks.
The route is still unregistered and none of its inventory, damage, custody, water contamination, map powers or actor effects has been implemented or tested in the game.

## Fresh compatible selected length

A separate solver traversed the matching opening and every available progression delivery variant from `Nodes[0]`.
It carries actual flags, applies scene and choice requirements and forbids, evaluates requirement groups, explores both check outcomes, and excludes refused or closed results.
It visits the retry only when the original encounter ended in the corresponding retreat.
It counts only selected prose and selected answers with `tools/measure-story-content.py` normalization and Unicode tokenizer.
The seed still assumes current Trickster, an available actor and positively verified native history.

| Measured completed trajectory | Saved brood | Lost clutch |
| --- | ---: | ---: |
| Maximum including the chosen retreat and return | 15,432 | 15,432 |
| Maximum without taking that optional detour | 15,169 | 15,169 |
| Lower-vault scene on the maximum trajectory | 1,849 | 1,864 |
| Rooftop scene on the maximum trajectory | 1,121 | 1,121 |

The full maximum remains 5,568 words below the 21,000-word requirement.
The direct-route maximum remains 5,831 words below it.
These are maxima, not guarantees that every completed route meets a floor, and not independent judgments of meaningfulness.
The optional retreat is not required to inflate route completion credit.
The matching full totals happen to be equal because the differing opening and history passages offset each other on these trajectories.

## Canon and remaining scope

The native saved/lost accounts are unchanged.
The lower-vault apparatus, copied nest measurements, map bargain, watchtower operators and western home proposal are authored alternate developments.
Ending this collector network protects a Devarra whose access has already been assumed by the opening.
It does not establish or implement initial main-campaign resurrection, DLC-to-campaign continuity, or a new canon dragon ability.

The western ledge inspection, its ownership conflict, the retained-map policy and the exposed-buyer threat remain future work.
The relationship still needs a complete partnership arc and endings, plus substantial meaningful selected content beyond the current draft.
Older dialogue still needs its separate characterization and economy pass.
A different reviewer must inspect the new source and all four repairs before approval.
Initial attainable acquisition, runtime registration, native producers, actor delivery, saves, ToyBox behavior, humanized-art staging, headless integration and manual play verification remain outstanding.
