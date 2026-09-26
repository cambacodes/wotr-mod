# Arsinoe continuation author handoff

## Scope and ownership

This contribution owns only `storylines/arsinoe_continuation.py`, `tests/ArsinoeContinuationTests.cs`, and this handoff.
It adds six scenes after the actual `arsinoe.opening_kept` outcome.
It does not modify the opening, shared engine, native history bindings, exports, installed assets, or other routes.
The parent must append this module's `SCENES` after the opening and register `ArsinoeContinuationTests.Run` in a staged payload before promotion.
No new schema or native history adapter is required.

Source SHA256: `436B93BF01C2CFE82009BAF9BA3E43A9C168A524C10E1218D11094A49BA60D9A`.
Focused test SHA256: `F52BB21FD04183EEBAE96AE8F86C01A13DAAD94F7D85D06E76E8BE04BB2B0216`.

## Played development

| Scene | Development and consequence |
| --- | --- |
| `arsinoe_your_hours` | Pays off her request to learn a Commander's interest through a competitive paper game or an amusingly bad adventure story, with two played variations of each. |
| `arsinoe_borrowed_court` | Arsinoe reciprocates with a traveling board whose instructions are damaged; native Knowledge World success, failure, and a non-roll house-rule approach each produce a different game. |
| `arsinoe_price_of_an_evening` | Her proposed advertised gathering causes disagreement about public access to the Commander, price, loneliness, and the cost of private leisure; the player chooses a public subsidized arrangement or a private invitation. |
| `arsinoe_courtyard_company` | Plays the chosen arrangement and rule history, then the Commander's chosen interest; a courier's working hours require an actual choice between earlier noisy meetings and quieter later ones. |
| `arsinoe_another_hour` | Reports a subsequent trial with specific benefits and exclusions, accounts for the chosen financial arrangement, and lets Arsinoe acknowledge the private company she missed while hosting. |
| `arsinoe_the_unprofitable_hour` | Returns to the personal activity and explores her desire to stay without turning the Commander into her only reason; courting permits an optional kiss or hand-holding, while slow courtship and friendship receive separate complete endings. |

The first scene is available after 24 hours; the courtyard gathering waits 72 hours after its terms are chosen; the other gaps are 48 hours.
Each requires its actual predecessor scene ID, `arsinoe.opening_kept`, and `arsinoe.capital`.
All four exclusive decisions are recorded only on their terminal choices: interest, game rules, payment arrangement, and meeting schedule.
Changing an unacknowledged decision after interrupted reentry therefore cannot retain a conflicting outcome from this contribution.
The native check attempt records no effect, and neither outcome is recorded before its result page is acknowledged.
The optional kiss flag is likewise terminal, after the kiss prose.
No choice writes `arsinoe.committed`, changes the opening's pacing flags, writes native history, or removes another relationship.

## Native evidence and authored additions

The source foundation is `reference/canon-review/arsinoe-route-evidence.md`, checked against `reference/expansion/arsinoe.txt`.
Vendor Cue0003 (`532d08eaffe92064c8461cb819f6b827`) supplies Absalom upbringing, travel, and her preference for useful work where it is needed.
Cue0013 (`7bebb812c92fa5f40a183cb1fa566847`) supplies the earlier Stolen Lands stay and departure after its prosperity.
Cue0015 (`45e474be0d232444bb054c5ac037ebe3`) supplies her account of law, trade, and civilization under Abadar.
Cue0014 (`c29c3b029ace6294988fb5b7883c7c3e`) supplies her practical scroll trade and professional caution.
Cue0016 (`6b8e9376e375de844a43cabd6546ab4f`) supplies aasimar identity and confident awareness of her attractive appearance.
The new wish to keep a personal life in Drezen is an authored development from that traveling history, not a canon statement that she has already settled permanently.
Neral, the courtyard, guests, board, damaged rules, book, notices, accounts, and private room are authored additions.
Neral, the courier, and the other guests are adults and have no romance interactions in this contribution.
The old game describes fictional merchants and tolls; it does not assert a previously unknown Abadaran religious doctrine or a native historical event.
Nothing asserts a completed Seelah or Arueshalae quest, recovered soul, native wedding, Commander spouse, resurrection, or cured Commander wound.
The native dialogue's partner status remains unasserted.

## Contact and delivery

All six scenes retain Drezen area `2570015799edf594daf2f076f2f975d8`, chapters 3 and 5, and live `ContactUnit` `a609ed9b2205d034bb3bb04d2a255681`.
They use the existing vendor answer list `ecaf5cfe8087a4f45a2269974f4885c9` and the opening's registered `arsinoe` relationship.
Native capital etude `3f3fbb973a4ffee47956b4c7714c939a` remains required through `arsinoe.capital`.
The existing relationship's `arsinoe.victims_revived` restriction continues to represent native etude `6d3fb96f9b60c0449a01add4be5c4a49` and the native vendor ConditionsHolder `c4fa13c72fc350d4bae7431242eb095a`.
This is temporary unavailability, with no new failure flag or permanent route closure.
Existing `swarm`, `true_lich`, and `arsinoe.closed` restrictions remain active.
The contribution neither unhides the native actor nor creates a duplicate one.
These optional physical book scenes enter through the live vendor, not an automatic rest scene or remote contact charm.

The courtyard walks and room transition are prose within that book encounter.
There is no placed courtyard map, interactive guest NPC, separate guest model, animated board, inventory booklet, or wallet transaction implemented here.
The small payments and later gatherings are authored narrative consequences, not modifications to game currency or independently simulated events.
Do not market these as completed map exploration or native economic gameplay.
The acquisition hook is the completed opening and the delayed live vendor invitation; stronger native quest-specific discovery and campaign connections remain future work.

## Native roll

`arsinoe_borrowed_court/method` offers Commander-only `SkillKnowledgeWorld`, DC24, with distinct `original` and `uncertain` pages.
The task is specialized reconstruction of a damaged commercial game's terminology, not general intelligence or an affection check.
The DC matches the existing Arsinoe opening's specialized World24 inspection and the local native Sosiel chapter-three card example's World24 scale, recorded in `reference/canon-review/native-romance-check-examples.json`.
It is authored balance, not a claim that Arsinoe has a native DC24 encounter.
Failure leaves the old rule unresolved, lengthens the later game, and reduces the reading time; it does not end the route or withhold intimacy.
The non-roll approach invents openly labeled house rules that guests later improve.
There is no experience reward, coin reward, advantage to courtship pacing, or required successful roll.
The engine must still demonstrate native roll UI, actor selection, actual result routing, and contact-loss timing in Unity before runtime approval.

## Verification and counts

A read-only Python graph traversal imported the actual module and reached all 50 pages across the three pacing histories.
It traversed both check targets, the non-roll alternative, both interests, both financial choices, both schedules, and every terminal path.
It confirmed that every new effect is on a terminal choice and no played branch is stranded.
Exact-segment counting uses the existing `tools/measure-story-content.py` tokenizer through an import, without writing generated inventory files.
The contribution contains 7,668 raw words: 7,069 prose and 599 choice words, with 7,630 exact-distinct words.
An attainable selected traversal of the contribution is 3,624-4,167 words depending on choices and pace, not the aggregate 7,668.
The current opening plus this contribution contains 13,405 raw and 13,305 exact-distinct words across eleven scenes.
This remains below the 21,000-word per-character planning floor before assessing complete-route depth.

The focused C# test plays the existing opening's final scene to obtain `opening_kept`, then all six actual continuation scenes with chapter, delay, and contact rules.
It deduplicates equivalent flag histories between scenes instead of multiplying alternate wording paths.
It checks live contact loss/restoration, temporary ceremony suppression, native capital prerequisites, closure, chapter and area restrictions, both roll outcomes, non-roll replay after interrupted results, pacing, optional intimacy, and untouched native/other romance histories.
It also asserts that no new flags are present on entry to any intermediate page, directly guarding premature outcome persistence.
The parent must restrict the older `ArsinoeOpeningTests` scene selection to its original five opening IDs because that test currently selects every Arsinoe scene without state deduplication.
No C# staged execution, managed blueprint construction, binding verification, or Unity run is claimed by this handoff at initial release.
Independent prose and technical review remain required; no quality score has been assigned by the author.

## Remaining route work

The eleven scenes do not yet form a complete RanRomance-length campaign.
Remaining needs include substantial native quest reactivity where exact history is bound, later campaign separation and return, deeper relationship conflict and resolution, attainable character-specific Trickster intervention, other mythic restrictions, an earned commitment opportunity, and ending variations that preserve played history.
No conventional or ascended ending, breakup scene, resurrection route, companion recruitment, or automatic farewell has been added here.
Friendship and slow courtship must keep comparable future story weight without being forced to choose romantic intimacy.
ToyBox free-love/no-jealousy behavior has been preserved structurally by leaving all other relationships untouched; testing its live interaction with this route remains necessary.
Arsinoe-specific portraits and scene art are still missing.
Suitable future art subjects are the gold-eyed priest handling the green-wrapped brass game, the six-chair courtyard beneath a patched awning, and a quiet two-person room with the opened book and hair clasp.
Those images must preserve her native appearance and distinguish authored guest designs from native companions; none were generated or installed for this handoff.
