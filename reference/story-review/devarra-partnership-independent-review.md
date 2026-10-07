# Devarra partnership independent review

Reviewed 2026-09-27.
The delayed-return timing repair works at the source level, and the western-house arc adds substantive choices and a partnership conversation.
The revision does not pass all required gates.
A new recollection invents a cup on two valid home histories, prose still contains implementation-facing assurances, and even the longest selected completion remains below 21,000 words.
The route is unregistered and not ready for manual in-game review.

## Independence and frozen evidence

Progression source: `storylines/devarra_trickster_progression.py`, SHA256 `3FB5F4425E94412399F3AA310859EB66B34EF22203F25E4A7766C57429C2F206`.
Opening source: `storylines/devarra_trickster_opening.py`, reported and retained SHA256 `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
The progression hash was rechecked after execution and was unchanged.
I read the actual new scenes, retry construction, ending predicates, `devarra-partnership-development.md` when delivered, and the prior lower-vault independent review.

I previously authored an earlier kiln/branch repair in this file.
I therefore do not independently approve my unchanged earlier prose here.
Fresh literary judgments concern the different author's missed-cart rewrite, five western-house/partnership scenes, two recollections and their joins.
The full selected-length computation is a mechanical measurement, not self-approval of older writing.
Only this report was edited.

## Blocking recollection defect

`recollection_partnership/memory` always recalls the cup the Commander and Devarra discussed afterward.
The actual cup appears only in `what_she_comes_back_for/return_owned`, reached after the fixed home purchase.
The seized-platform and rejected-platform branches instead use `return_claimed` and `return_roaming`.
Neither mentions a cup, and the shared subsequent partnership pages do not introduce one.

I reproduced both witnesses from the emitted saved-history partnership variant with its required state and the appropriate home/map history:

- `return_choice -> return_claimed -> return_power -> return_unarmed -> return_answer -> return_partners -> return_farewell -> return_depart`.
- `return_choice -> return_roaming -> return_power -> return_unarmed -> return_answer -> return_partners -> return_farewell -> return_depart`.

Both write partnership completion and admit the partnership recollection.
Neither displays a cup in any selected node, yet the recollection recalls one.
This is a narrative state leak, not merely an absent prop in an illustration.
Use a genuinely shared remembered detail, or guard separate home-specific recollection text.
Do not fix it by silently granting every branch the fixed-purchase conversation.
The current author test checks ending exclusivity, which passes, but does not catch this false remembered detail.

## Timing repair and delayed rescue

The earlier defect was an approaching cart that remained available after a minimum-only delay, including a week later.
The new return opens after that departure at every eligible time.
`src/Story.cs:223` computes the latest relevant timed prerequisite, and line 225 checks elapsed time against a minimum DelayHours.
There is no maximum window supplied by these source fields.
The new story no longer relies on one.

The retry remains unavailable before its one-hour minimum and remains available at 1, 24 and 168 hours under the matching predicates.
At all those eligible times, its first page states that the cart has already left, Serevin has removed the lamps and departed with her ledger, and the workers must be located at their later place of imprisonment.
The quarry is a stable destination rather than a cart held in place indefinitely by the menu.
Neither the success nor failure of the new Perception check can lead to the old receipt trap or capture page.
Both outcomes set the prisoners free, mark Serevin escaped and leave the lower vault warned.
Neither writes Serevin-held or ledger-taken.
The failure adds the worker's injury and a harder rescue, while the success still acknowledges raw wrists and harm from the lost time.
Abandonment leaves the rescue and later completion unavailable.

The original withdrawal now warns of risking the cart's departure and ends with preparing to follow the workers after it leaves.
This is enough to distinguish retreat from a free repeat of the same encounter, though the first choice would be clearer if it said the opening will be lost, since every supported return now occurs after it.
The one-hour bound is no longer a false opportunity to capture Serevin.

The new five-scene sequence declares delays of 24, 12, 0, 24 and 24 hours.
The storm can follow preparation without another required wait, and the writing adds no precise expiration which those fields pretend to enforce.
These declarations do not prove actual actor timing, weather changes or delayed triggering in Unity.

## Selected-route measurement

I executed a separate carried-state solver using the repository `words()` tokenizer.
It traverses the matching opening and emitted history-specific progression scenes from `Nodes[0]`, honors Requires, Forbids and any requirement groups, accumulates selected effects and explores both check results.
It skips the optional return when the direct kiln outcome already completed that stage.
It excludes closed/refused paths from completed courtship totals and adds exactly one eligible partnership or visits recollection.
Future-equivalent states retain separate minimum and maximum costs before merging.
No saved/lost duplicate, unselected answer, incompatible check outcome or second recollection receives content credit.

| Complete current draft including one recollection | Saved brood | Lost clutch |
| --- | ---: | ---: |
| Minimum allowing delayed quarry rescue | 14,053 | 14,094 |
| Minimum using direct kiln progression | 14,107 | 14,148 |
| Maximum | 19,714 | 19,714 |

These independently reproduce the author's full-route figures.
The minimum remains 6,947 words short of 21,000 and the maximum 1,286 short.
Correcting the false cup recollection will require a recount.
A rounded inventory or two historical variants must not be used to hide the shortfall.

There are fourteen main progression templates, one delayed-return template and two recollection templates.
The two history variants of each produce 34 progression definitions, plus the two separate opening definitions.
Those are delivery counts, not 36 unique scenes of new narrative.

`python -m storylines.devarra_trickster_progression` passed its source validators.
Its printed continuation maximum covers only the internally selected continuation subset, so it is not the full-route minimum/maximum reported above.
My independent full-route pass reached 262 nodes and 523 choices for saved history, and 257 nodes and 509 choices for lost history while exploring refusal answers before excluding their terminated results.
Those figures are reached graph coverage, not unique prose credited to a playthrough.
Both injured and uninjured quarry-rescue outcomes were reproduced, with assertions excluding ledger or Serevin capture in completed retry results.

## Character and choices

The new house is not awarded merely because the Commander requests a romance.
It sits above occupied rooms, a neglected retaining wall and a diverted channel.
Devarra wants a place that can bear her weight and remain hers without making her another person's military asset.
Mareth's insistence that she first consider the people beneath the wall gives her a concrete obstacle she cannot solve by being larger.
The dragon remains proud and dangerous: she approves threatening Talvren, resents lost advantages and may openly seize the platform.
She does not become agreeable simply because the player proposed a home.

The estate dispute gives the Commander several recognizable options.
World-knowledge success defeats a specific written claim, failure leaves public responsibility and survey costs, intimidation obtains payment but produces a truthful coercion complaint, and Trickster prepares a bounded delivery to a named empty yard.
The magic needs the owner's answer, marked stones, an opened outlet and preparation before the roll.
Arcana failure costs time and a tool and forces ordinary labor instead of repeating the successful trick under another name.
The physical alternative remains available even when the magical delivery was prepared.
These are useful source-level distinctions, not merely different tones leading immediately to identical prose.

The settlement preserves lawful purchase, openly disputed seizure and departure as separate home histories.
The final scene reads those histories and the kept/destroyed targeting map.
Her possessiveness survives the map restriction: destroying this weapon does not mean she has become uninterested in power.
The taken-house branch retains an enemy and future complaint instead of quietly converting force into legitimate ownership.
The survey, complaint, weapon leads and future repairs are still promises or unresolved work, not completed native sidequests.

The final invitation adds relationship content beyond another rescue reward.
She wants a return chosen freely, tolerates other lovers without converting them into property, and distinguishes partnership from separate lives with continued affection.
Kiss, quiet company and immediate departure are distinct farewell choices.
The quiet and departure terminals do not pass through the kiss node.
Ending courtship writes refusal without partnership completion and preserves practical consequences.
The two ordinary recollections are predicate-exclusive, subject to the cup defect in the partnership text.

Devarra remains an articulate adult dragon in dragon form throughout this new material.
There is no written transformation which would make the humanoid art candidate accurate for these pages.
The saved/lost variants do not restore a lost clutch or invent another survivor.
The acquisition, resurrection and DLC-to-main-campaign actor questions remain unresolved by these scenes.

## Prose issue requiring revision

The delta repeatedly explains production safeguards in narration after the scene has already shown the relevant behavior.
The clearest example is the quarry passage calling this an established place of imprisonment, not a cart which waits forever for the player to catch it.
That explains the timing repair to a developer rather than describing what the Commander learns at the weighhouse.
Replace it with an observable fact about where the workers are held and how the delivery records identify it.

The pattern recurs in `ledge_challenge`, which announces that no household has joined the crusade, and `ledge_guest`, which explains that walking the inspection has not agreed to cohabitation.
`rain_work` reiterates that no ownership claim has yet become a shared home; `settlement_buy` assures the reader that the choice does not conjure rooms, furniture or treasury.
`return_answer` surveys all three possible home arrangements even after the selected home branch has just been heard.
Individually these statements are understandable, but together they repeatedly sound like safeguards from a review checklist rather than expansion dialogue.
Keep concrete reactions, limits and consequences while removing the repeated author commentary.
The existing goat, wet tool, lodged stone, inconvenient chair and possessive jokes are stronger ways to carry the same distinctions.

## Strict scoped results

| Dimension | Score or result |
| --- | --- |
| New dragon characterization and resistant motives | 93 |
| Western-house causality and antagonist incentives | 93 |
| Commander good/coercive/Trickster agency | 94 |
| New graphic and explicit courtship and local refusal handling | 94 |
| Source-level delayed-return repair | 95 |
| New scene follow-through before recollections | 93 |
| Recollection history fidelity | 88 - fail: unearned cup |
| Prose immersion and restraint | 90 - fail under strictly-above-90 gate |
| Minimum 21,000 selected words | Fail: minimum 14,053 |
| Native state acquisition and runtime integration | Unverified and unregistered |

No average overrides the failures.
Repair the false recollection, remove implementation-facing narration, then continue substantive development toward the selected-path floor.
A different reviewer still needs the assembled prose once that work is complete.
These local tests did not execute native actor delivery, inventory/economy effects, world weather, save persistence, ToyBox behavior, ending integration or in-game portraits.
No image, source, export or shared project report was changed.
