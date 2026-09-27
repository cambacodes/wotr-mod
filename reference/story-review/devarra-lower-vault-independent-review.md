# Devarra lower-vault independent review

The four earlier defects are repaired, and the new vault and rooftop scenes give previous choices substantial consequences.
One new retry-timing failure remains.
The assembled route is also incomplete, below its selected-length floor, and unregistered.
It does not pass every applicable dimension strictly above 90 and is not ready for in-game review.

## Snapshot and scope

- Progression source SHA-256: `1A2C085F77B9297934C1CC26BFAEFE6C63A7985318E2BA42FF4D878DA732392D`.
- Opening source SHA-256: `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
- Read `devarra-lower-vault-development.md`, the preceding branch-repair review, the actual repaired kiln passages, the lower vault, rooftop, retry construction and delivery variants.
- Checked native saved/lost dialogue in `reference/canon-review/dragon-candidate-dialogue.json` and book entry and delay handling in `src/Main.cs` and `src/Story.cs`.

I did not write these Devarra scenes or edit their source during this review.
The fresh literary judgments concern the repaired passages and new delta, not blanket approval of the earlier assembled prose.

## Verified repairs

`kiln_survey` no longer asserts an employment discussion shared by the spared and killed histories.
Only `BUYER_SERVES` enters `kiln_employment`.
The other fates enter the appropriate intact-shard or physical survey directly.
The callback now follows the actual coercive arrangement.

The kiln's delay is 144 hours, matching the six-day appointment.
The earlier 120-hour inconsistency is removed at the source level.

`stone_survey -> kiln_retreat` is an actual selectable withdrawal before the inspection roll.
It sets retreat without setting `KILN_TRIED`.
The original kiln then forbids retreat history, and the return scene supplies a new first page.
Returning permits one inspection, while the alternative deliberately leaves the operation unfinished.
The retry removes the old retreat edge and forbids an already attempted inspection, finished operation, abandoned retry and incompatible intact-shard history.
This repairs the missing menu choice and avoids a repeated-roll loop, subject to the timing failure below.

At `receipt_trap`, Serevin tests her handler ring, states the exemption she believes it provides, and moves under the beam for a tactical reason.
The Commander then exploits her simultaneous identification as owner and delivery.
This is an intelligible authored loophole with a prepared mark, location, acknowledgement and one-shot check.
The ring gives her a credible reason to make the mistake instead of requiring a dangerous antagonist to cooperate merely because the narrator says she should.
It remains authored magic, not a verified native ability.

## Remaining timing failure

`kiln_retreat` says there is an hour at most before the quarry cart permits Serevin to move the prisoners.
`kiln_return` then says it is an hour after withdrawal, the cart is still approaching, and its arrival will empty the meeting place.
However, `KILN_RETRY_SCENE` has `DelayHours=1` and no expiration predicate or late outcome.

The current C# delay rule is a lower bound measured from the latest timed prerequisite.
With the matching history and retreat state, unchanged actor and chapter, and no other blocker, the same scene remains eligible at 1, 24 and 168 elapsed hours.
I reproduced that eligibility from the actual predicates and delay condition.
At zero hours it is unavailable.
At a week it still narrates the same approaching cart and permits the same successful rescue.
This is a manuscript-to-rules inconsistency, not an observation from a live game.

Either enforce the announced window and provide a coherent late-arrival consequence, or revise the fictional opportunity so that a minimum-delay return remains plausible.
Do not retain a firm deadline which the selectable route silently ignores.
The existing abandonment correctly withholds rescue and later continuation, but it does not address choosing the retry after waiting too long.

## New scenes and characterization

The lower vault develops the collectors' mechanism instead of staging another seller asking to own Devarra.
Captured Serevin supplies the entrance sequence and ledger in the earlier custody page; the vault does not invent that testimony afterward.
Escape produces destroyed destinations, an exposed entrance and a more urgent discharge problem.
Vey's spared, bound, released and killed outcomes each produce a different landing passage.
The released account is actually supplied in `vey_paid` before it is remembered in `vault_released`.

Devarra's strongest passages remain proprietary and dangerous.
At `vault_dead`, she acknowledges the investigative cost of killing Vey without apologizing for having wanted him dead.
At `vault_bargain`, she wants the targeting weapon but demands destruction of her own plate and divided control.
Insisting on keeping her plate reaches a real breakup and blocks later courtship through `REFUSED`.
Her interest in the Commander does not make captivity acceptable merely because he proposes it.

The roof retains that disagreement.
Keeping the map produces a specific discussion of extortion versus investigation.
Destroying it produces regret without secretly recreating the discarded targeting information.
The failure exposure produces a watch and an uncertain possible reconnaissance object, not a claim that danger has disappeared.
The prospective home remains an unresolved ownership dispute with different player intentions, rather than a house awarded by selecting a romantic answer.

The new mature courtship is graphic and explicit and character-specific.
`roof_desire` offers a kiss, company without touch and immediate departure.
The latter two terminate without traversing `roof_kiss`.
The earlier quiet exit also avoids that page.
The kiss follows the player's expressed request and her initiative; the successful investigation alone is not its consent flag.
This delta improves the relationship, but a full partnership arc and endings are still missing.

All these passages describe an adult, articulate dragon in dragon form.
They do not establish a humanoid transformation or authorize assigning the humanoid candidate to these scenes.

## Native history and authored continuity

Native Tower cue `8c53478782244b90a37f727f7b814318` distinguishes the spared brood and prior demonic coercion.
Cue `d368680393304b5ba324dd5a517140ed` describes the pillaged clutch and offspring dead before birth.
The new copied nest sketch supplies neither a replacement history nor an invented survivor or egg recipient.
Saved and lost responses differ in motive and grief, while Devarra herself destroys the targeting detail.

The plates, copied departures, reservoir, map bargain and prospective western home are authored developments.
Destroying the new mechanism protects access which this opening has already assumed.
It does not prove main-campaign restoration, transfer out of the DLC encounter or a living actor who can attend later scenes.
Those acquisition and delivery requirements remain unimplemented.

## Independent selected-length measurement

I traversed one matching opening and each exact-history delivery variant from `Nodes[0]`, carrying choice effects and enforcing requirements, forbids and requirement groups.
Both check outcomes were explored.
Refused and closed histories were excluded from completed courtship paths.
The solver retained minimum and maximum prefixes only when equivalent for future predicates.
The repository's normalized Unicode `words()` counter counted visited prose and selected answers.
No parent-mod text, duplicate history variant or repeated full kiln scene was credited.

| Completed path through the rooftop | Saved brood | Lost clutch |
|---|---:|---:|
| Minimum, direct or optional-return search | 9,868 | 9,909 |
| Maximum without retreat | 15,169 | 15,169 |
| Maximum allowing one retreat and return | 15,432 | 15,432 |
| Lower vault on that maximum witness | 1,849 | 1,864 |
| Rooftop on that maximum witness | 1,121 | 1,121 |

These reproduce the development report's maxima and add the missing minima.
The optional return contributes only its selected detour; the unfinished kiln continuation is visited once afterward.
The best path remains 5,568 words below 21,000, and the direct maximum is 5,831 short.
Shorter complete paths are much further below the floor.
These are completions of the current manuscript through the rooftop, not completed romance campaigns with endings.

## Verification and delivery limits

`python -m storylines.devarra_trickster_progression` and compilation both pass.
I independently checked all 160 history combinations across the ten template pairs.
Only an exact saved-plus-saved-cue or lost-plus-lost-cue pair admits a delivery variant.
Missing, mismatched and contradictory histories admit none.

The twenty progression delivery variants represent nine main templates plus one retry template.
The C# source starts at `Nodes[0]`; `Entry` supplies interaction text.
The variants now use readable scene titles and retain the intended first page, including `kiln_return` for the retry.
The unchanged opening and its broader delivery still need integration review when registered.

The module's one-shot attempt and branch tests pass, but passing them does not verify expiry or prose truth.
Inventory, custody, injuries, water contamination, map powers and restoration remain narrated outcomes with addon flags, not implemented game systems.
No new C# export run, Unity session, ToyBox run, save test or art assignment was performed or approved here.

## Scoped scores

| Dimension | Score | Result |
|---|---:|---|
| Native versus authored history in the delta | 95 | Pass |
| Devarra's danger and refusal of ownership | 94 | Pass |
| Commander and prepared Trickster intervention | 93 | Pass |
| Selected branch consequences in vault and roof | 94 | Pass |
| New intimacy and refusal agency | 96 | Pass |
| New adult courtship texture | 92 | Delta pass, not full-route maturity approval |
| Exact-history delivery and one-shot source structure | 94 | Static pass |
| Retreat deadline and delayed-return coherence | 82 | Fail |
| Assembled selected length and route completeness | 63 | Fail |

The repaired and new prose can proceed to further development.
The retry window, substantial missing selected content, partnership ending, attainable acquisition and runtime integration remain open requirements.
