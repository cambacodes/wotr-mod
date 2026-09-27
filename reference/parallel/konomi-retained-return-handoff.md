# Konomi retained-return author handoff

Four new scenes are ready for independent literary and integration review.
They add 3,093 distinct words to the existing Konomi campaign.
They are an expansion of that campaign, not a separate full-length route, and I do not approve my own writing.

## Owned files

| File | SHA256 |
| --- | --- |
| storylines/konomi_retained_return.py | 2AE88A9B5158745ECE9EBF55C8781843C9C6F5A61EC9F25F8C4051B8ADE1C4F9 |
| tests/KonomiRetainedReturnTests.cs | 06570E35034749530788A054F40FB8166A7842F974F146DC05E1CE3B374CED27 |

All three assigned paths were absent before this task.
I created only the assigned source, focused tests and this handoff in the repository.
I did not edit the shared exporter, production engine, existing route, art or installed package.
The source exports `SCENES` and `REVIVALS` for root-owned integration.

## Authored sequence

| Scene | Function |
| --- | --- |
| konomi.retained_inquiry | Current Trickster examines a fate-map's false inference that death excludes every later event. A Knowledge World check at DC 22 finds the distinction quickly; failure or deliberate patient reading also earns the prepared path. |
| konomi.retained_attempt | The prepared path leads to one explicit native recovery choice. Its only effect is `konomi.retained_return_confirmed`, which the host may award only after current verified success. |
| konomi.return_first_words | The restored woman asks what actually happened and begins dealing with an ordinary hour again. Personal history determines the answer, including a separate closed-relationship response. |
| konomi.return_second_visit | After her invitation and a 48-hour interval, Konomi examines the map, chooses modest plans and distinguishes her unchanged office history from the return. Existing relationships resume their own conversations; a new invitation still has to earn its answer. |

The fate-map, its annotations, the recovery opportunity and all subsequent dialogue are authored alternate developments.
They are not canonical evidence that Konomi dies in a particular quest, that a divine court uses this paperwork, or that her native office changes.
The investigation identifies the exact retained body without inventing a cause of death.
It never replaces her with a copy or claims the death did not occur.

The memory branches distinguish an existing lover, the missed-contact private address, the older dismissal-path private meeting, ordinary authored acquaintance and absence of authored personal history.
Absence of the addon acquaintance flags does not establish that the Commander has never met her through native diplomacy dialogue.
The neutral branch therefore begins a personal conversation without claiming a first native encounter.

Her existing political judgments remain intact.
Active-office, dismissed and unappointed histories have separate follow-up pages.
The authoring never awards or clears office, dismissal, lover, commitment, private-access, native meeting or closure flags.
The existing ordinary `konomi.returned` flag is preserved and is unrelated to the new proof marker.

Closed, farewell and private-parted histories receive nonromantic aftercare.
They cannot select the lover hand kiss, renewed invitation or resumption endings.
Both visits use explicit `AfterRecovery='konomi'` so root's narrow aftercare exception can leave the relationship closed.
Other women's commitment flags are preserved throughout.

## Engine contracts

Preparation and attempt both use `Recovery='konomi'`, current `trickster`, and read-only derived `konomi.retained_dead`.
The existing recovery availability gate must additionally supply `revive.konomi.available` from the reviewed native service.
A retained body that is missing, destroyed, ambiguous or not currently eligible cannot enter merely because a story flag says someone died.
The source creates no fabricated native etude binding for retained death.

`REVIVALS['konomi']` specifies relationship `konomi`, unit `ca2d58c5c65723945857e04fb85d30ce`, and death flag `konomi.retained_dead`.
Add the death flag to the relationship's unavailable flags and use root's explicit derived-revival validation exception.
Do not run the generic companion Fate revival path for this choice.
Use the reviewed `KonomiRecovery.Request/Poll` service and exact authorized-choice checkpoint contract.
Pending, failed or unverifiable native attempts award neither scene completion nor the success effect.

Both aftermath scenes require `konomi.retained_return_confirmed` and derived `konomi.return_contact_available`.
They also set `ContactUnit` to the exact native Konomi blueprint and forbid current retained death.
The derived contact flag must combine exact current verified retained-actor provenance with usable native physical contact.
A historical confirmed checkpoint alone is insufficient.
Office hiding or unavailable actor views must keep the physical scenes closed.
The engine's contact interruption path must reevaluate these requirements during conversation.

New fate action requires current Trickster power.
Already verified aftercare can proceed after a later Legend transition, without attempting another resurrection.
A new death remains blocked by the old confirmed request and needs a separately authored future episode.
Missing, destroyed and cross-area cases remain unfinished work rather than removed requirements.

For integration, give the four new scenes priority before ordinary Konomi remote scenes when their own gates pass.
Otherwise the first post-recovery automatic offer may be an unrelated old conversation before her initial aftercare.
Their native gates already prevent them from interfering before the relevant recovery history.
After their completion, existing office and private campaign conditions determine the next available content.
No copied acquisition route or automatic relationship-access shortcut is added.

## Focused verification

The isolated directory is `C:/Users/Z/AppData/Local/Temp/konomi-retained-story-cpjljh39`.
It contains `candidate.json`, `Check.csproj` and a small runner.
The candidate starts with `expansion.make_expansion()`, appends these scenes, registers this revival and adds the derived death flag to Konomi's unavailable flags.
It does not alter the shared development export.

Run the local dotnet executable with `run --project C:/Users/Z/AppData/Local/Temp/konomi-retained-story-cpjljh39/Check.csproj -- C:/Users/Z/AppData/Local/Temp/konomi-retained-story-cpjljh39/candidate.json`.
The runner validates the candidate with current production Rules and invokes `KonomiRetainedReturnTests`.
The final run passed 52,778 explicit focused assertions.
The project also compiles the existing Program walker, whose own traversal checks are additional to that reported counter.

The tests cover chapters 3 and 5, five personal-history inputs, four open or ended relationship states, and three native-office states.
They play preparation through predecessors, exercise both check outcomes, reach the explicit attempt and every authored page, and verify the 48-hour delay.
They test missing Trickster/death/source evidence, pending versus verified aftercare, lost native contact, new death, Legend continuation, relationship closure and preservation of other romances and native office flags.
Existing personal and political histories are declared input fixtures, not claims that this test replayed every original acquisition route.

The pure story walker does not execute resurrection.
Positive aftermath states are explicit service-result fixtures.
The test discards the walker's simulated attempt outcomes and supplies verified native-result evidence separately.
These checks do not establish actual resurrection, placement, Unity save/load, native body persistence or ToyBox runtime behavior.

The word inventory contains 2,578 prose words and 515 choice words, with no exactly repeated text segments inside this contribution.
It is not a guaranteed playthrough length or evidence that every word meets the literary standard.
Independent reviewers still need to judge characterization, emotional pacing, the fate intervention, restraint after death and the joins into the existing campaign.
No new art was generated or assigned; aftermath pages use the existing general Konomi portrait key.

Root pre-review caught engine terminology in the player-facing fate text and a signed-sheet ownership error.
The revised text uses concrete map and bodily imagery, shortens repeated explanations of the mechanical limits, and keeps the signed sheet with the Commander in the closed-history ending.
