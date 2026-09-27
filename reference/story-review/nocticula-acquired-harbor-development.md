# Nocticula acquired harbor development

Date: 2026-09-27.
Author delivery only; independent review required.

Source: `storylines/nocticula_acquired_harbor.py`.
Frozen SHA256: `4E0F25DC9A97150FE8C16EE8575B0DB55BA63804F2A62CB4F0FEE69F6C5065CD`.
The original donor remains untouched at `11B5B48D10DEDC903FE7FB9A64C3BA265636CED33E96A2508ACED15A5DC2764B`.
The completed bridge read for this work remains `463CC47E4552A611AA5273EE1005AE06626C6B4C0C998797C2288CC71892BBDE`.
Only the new source and this report were written for this assignment.

## Delivered scope

This module adapts the existing twenty-four harbor visits and eight supplementary recollections for the earned Trickster entry.
It deep-copies the original source into distinct stable delivery IDs while preserving the shared quest choices, costs, relationship progress, scene timing and portrait assignments.
It does not register any scenes, change a native binding or alter the original source's saved identifiers.

There are **102 delivery definitions**, representing **24 visits and 8 alternative recollections**.
The count is three provenance families for each of the thirty-two original scenes, plus six additional current-Gift variants for `her_own_face`.
These are alternate deliveries of the same story, not 102 different narrative scenes and not three playthroughs worth of content added to one route.

The source exports `SCENES` and acquired-entry `RELATIONSHIP` metadata for root integration.
It intentionally has no registration helper that could overwrite the existing relationship definition without a root-owned decision.
The original native bindings must remain registered through their existing owners.

## Provenance and physical writing

`new` reads `noct.join.history_new`, `refused` reads `noct.join.history_refused`, and `prior` reads `noct.join.history_prior`.
The latter retains a genuinely accepted earlier bargain even when original patronage is no longer available.
The former two do not invent acceptance of that bargain, palace accommodation or a price already agreed for the Worldwound.
All three depend on the bridge's hosted meeting, whose magic remains an authored extrapolation rather than a native replacement Gift.

The adaptation preserves the original bodily and setting-specific romance: her posture on the bollard, hand contact around the embroidered cloth, the couch and fruit, dance choices, shared warmth, kisses and later private evenings.
It does not turn those encounters into more correspondence or replace her sexual confidence with uniformly reserved behavior.
The new opening callbacks use the sailcloth against a wrist and an exchange of the passenger names to connect the player's earlier priorities to an encounter with her.
They do not award a profit share or rescue a passenger merely for expressing a preference.

This direction follows the character-first and event-based approach described in Owlcat's [How do We Write Romance](https://owlcat.games/news/101).
That article supports using the established character, distinct interactions and player responses to develop intimacy; it does not certify this adaptation's quality or runtime behavior.
Nocticula's danger and appetite remain the point of the attraction, with disagreements the Commander can maintain.
All romantic participants are unrelated adults and the intimacy is graphic and explicit.

The existing optional ambition disclosure still requires the actual native witnessed cue.
The bridge does not grant knowledge of Nocticula's earlier disclosure, her brother's plot or any native ending.
Likewise, the Commander and Nocticula still act through recalled evidence in the harbor dreams, not live surveillance or retroactive commands to past events.

## Exact changes

| Original location | Acquired adaptation |
| --- | --- |
| `unlit_quay/start` | Names the hosted invitation rather than promised accommodation; reads the bridge's passenger/profit preference through distinct selected responses. |
| `unlit_quay/council` | Keeps the genuinely gated Council memory, then still reaches the chosen passenger/profit response. |
| `unlit_quay/offer` | New and refused histories explicitly preserve the absence of an accepted Worldwound bargain; prior history retains the genuine older terms. |
| `unlit_quay/decline_undertaking` | New/refused histories keep personal correspondence after refusing this work, without fabricating an older political agreement. |
| Twenty-three `withdraw_undertaking` nodes | New/refused histories name the letters that remain; prior history retains the older bargain; every existing harbor-closure consequence remains. |
| `counterseal` withdrawal | Corrects the inherited late-exit wording which claimed business was settled while a new creditor claim was being introduced. |
| `her_own_face/start` | Current original Gift, renewed Gift and no Gift receive different danger/context lines; new/refused histories do not acquire an older bargain through intimacy. |
| `second_door/future` | New/refused histories distinguish chosen company and useful work from agreement to the Commander's larger ambitions. |
| `second_door/limited` | New/refused histories explicitly retain letters and decline another private room or wider alliance; records `noct.join.letters_after_harbor`. |
| `second_door/power` | Replaces the apparent repeat of the completed Salven introduction fraud with a different courtier selling the same execution balcony to multiple guests; keeps the intimate scene and callback humor. |
| `ending_alliance` | New/refused histories retain an unanswered larger disagreement rather than inventing an older Worldwound bargain. |
| `ending_limit` | Identifies the personal correspondence actually retained by new/refused entrants. |

The other recollections retain their inherited wording and ending predicates.
Their full history and runtime suitability still requires independent review.
In particular, the native `noct.dead` alias has a previously documented lifecycle limitation: its event can begin before a verified corpse exists.
The inherited death recollection's assertion of death therefore remains a delivery concern, not something this source's static predicate test proves.

## Selection, progress and save contract

Every acquired scene requires bridge readiness, recurring invitation acceptance, demonstrated exit, the bridge's final completion flag and exactly one provenance witness.
Each forbids the other provenance witnesses, so contradictory histories do not silently choose a family.
Ordinary visits also require Trickster and the earned personal agreement; death, Council conflict, acquisition closure, bridge closure and the original unsupported mythic transformations block them.
The acquired family does not clear native rejection or write parent acceptance, Gift, native seen-cue or native completed-etude aliases.

The ID pattern is `original_scene_id.acquired.new`, `.refused` or `.prior`.
Only the face scene adds `.absent`, `.original` or `.renewed`.
The face delivery reads current power state when that visit becomes eligible, not only the Gift state observed during acquisition.
Renewed Gift takes precedence if both power aliases are present; no-Gift delivery requires both absent.
Completion of any face variant writes the original face ID and excludes every sibling, so a later Gift change cannot replay that visit.

Every non-abort terminal choice explicitly writes the original scene ID as well as its existing authored consequences.
Abort retains the original ability to leave the proposal unanswered and does not write that alias.
Every acquired scene forbids its original ID, preventing replay after either an original or acquired delivery has already completed.
Shared original progress flags continue to unlock the next visit.
Withdrawal remains a terminal closure, not a disguised continuation into the next meeting.

Root must apply the approved mutually exclusive export contract: original harbor-family scenes must be withheld when `noct.join.harbor_variant_ready` selects this acquired family.
That exclusion must cover the original recollections too, not just the twenty-four visits.
Without this root-owned step, a gifted entrant with native parent acceptance can meet both families' outer conditions before either version is completed.
The module does not pretend to have solved that duplicate export by modifying the original source behind its owner's back.

Existing completed original IDs and progress flags are preserved.
They can prevent replay and identify the next unfinished visit if a legitimately completed bridge later selects the acquired family.
This is not a claim that arbitrary mid-route migrations or manually seeded bridge flags are safe.
Root should test an actual saved original prefix, a valid acquisition transition and its next unfinished visit before supporting that transition in release.

The new metadata still uses the same `nocticula` relationship flags.
Root should choose history-appropriate or jointly accurate journal wording rather than register both conflicting metadata dictionaries.
The acquired description provided here is specific to this entry; the original accepted-parent guidance remains appropriate to its original family.

## Local execution and selected length

Executed the module's `validate()` on the frozen source.
The final run passed 64 supplied history/Gift/first-question/native-witness fixtures, traversing actual `Nodes[0]`, applicable choices, branch effects and terminal aliases.
It retained minimum and maximum played prefixes when merging states that no later predicate distinguishes.
The repository word tokenizer counted selected prose and selected answers only.
Each completed result includes one compatible ordinary recollection; it does not sum all endings, all branches or any alternate delivery family.

| Acquired provenance | Minimum selected harbor words | Maximum selected harbor words |
| --- | ---: | ---: |
| New personal relationship | 22,020 | 24,428 |
| Earlier parent offer refused | 22,021 | 24,429 |
| Genuine older pact, original patronage lost | 21,985 | 24,392 |
| Across supported fixtures | **21,985** | **24,429** |

These counts exclude the acquisition opening, concession and three-visit bridge entirely.
The harbor alone clears the numeric 21,000 floor by 985 words on the shortest modeled completed selection.
Length is not an approval of meaningfulness, characterization or the inherited prose.
The additional selected writing here corrects history and develops the opening callback; alternate-copy inventory is never credited toward the minimum.

The traversal encountered 248,224 closure paths across its repeated fixture states and verified that closed outcomes cannot continue into later visits.
That figure is a test traversal count, not a count of unique narrative choices or playthroughs.
Checks also reject missing bridge prerequisites, contradictory history witnesses and replay of an already completed original scene ID.
No choice in this module writes the tested native aliases, and no Check-plus-Next choice is introduced.

Separate predicate checks covered 576 recollection combinations across three provenance histories, three chosen ordinary relationship outcomes, sixteen combinations of death/transformation/ascent/sacrifice state and four current-Gift combinations.
The inherited priority remains death, changed Commander, ascent, sacrifice, then the selected ordinary outcome.
Each fixture exposes exactly one ordinary-epilogue definition in its acquired family.
Aeon recollections retain their separate owner and require completed harbor history; they are not counted as another ordinary ending.
These predicates test data selection, not native ending event production or actual epilogue scheduling.

The optional native ambition disclosure and brother-plot witness were tested absent, individually present and together.
Those are explicit read-only test inputs, not evidence that every possible combination is obtainable in a particular Chapter 5 save.
The prior-pact fixture excludes a still-playing original Gift because this acquisition history concerns lost original patronage.
A renewed-Gift fixture tests the text and gate contract without proving the native renewed-Gift producer occurs during this acquisition's Chapter 5 window.

## Remaining work and review boundary

This is ready for an independent source and prose review, not manual-game readiness.
I authored the bridge and this adaptation, so I do not approve their literary or canon quality myself.
The original donor's earlier reviews do not automatically approve these new delivery families.
Every applicable rubric still needs a strictly greater than 90 assessment of the actual integrated variant.

No original acquisition producer, native return lifecycle, C# schema/build fixture, Unity dream delivery, journal transition, save round trip, ToyBox combination or actual ending event was exercised in this author task.
Root owns exports, native registration and those integration checks.
The original nonphysical/private-evening choices remain available, but this is a romance with bodily contact elsewhere, not a claim of an entirely platonic completion.
The player must still be able to use the actual withdrawal presentation after integration; a narrated invitation or sheet is not a working inventory switch.

Current art remains the inherited Nocticula portrait assignment.
No new event image, automatic portrait sequence or clickable selector was added.
The physical scene beats require separate scene-specific illustration review if new pictures are assigned.
