# Devarra branch repair and lime-kiln development

The starting progression snapshot was `241A2A819F65FE35B24766FC6E72478280FA640F392A154CE0577B779F8F8FE1`.
The revised progression source SHA-256 is `48A46A34AF6532BD4163B89D38FA52FCC08218E04134C57F1ED824D80F3E9AC4`.
The unchanged opening source SHA-256 is `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
This is an author handoff following the independent continuation review, not a new approval.
The author of this revision previously reviewed the old snapshot and cannot independently approve this revision.

## Repaired defects

The ordinary-time bridge path no longer narrates a repeated minute fading.
The final planning answer refers to the chosen arrangement rather than asserting that the Commander altered time.
A common preparation passage creates the flawed false folio before every plan, including the public plan.
Successful planning records `false_folio_ready`, and bridge delivery requires it.

The cistern's shared return no longer claims that the wheel turned against Vey after the physical shard-breaking outcome.
Separate `return_kept` and `return_paid` pages respond to the preserved shard and the injured hand respectively.
Their choices require exactly the matching anchor outcome and forbid the opposite one.
The paid outcome receives a short injury-and-banter scene; the kept outcome discusses the inert shard and the successful counting trick.

All seven progression scene templates now produce exact saved-brood and lost-clutch variants.
Each delivery variant requires its matching verified-history and native-cue pair and forbids both opposite history flags.
The variants also forbid the opening's closed-relationship state.
This rejects absent, mismatched and contradictory history states before scene delivery.
The shared template definitions are authoring material, not additional delivery entries.
`SCENES` contains only the fourteen guarded variants with unique suffixed IDs.
The original completion and handoff flags remain unchanged, so later scenes follow the same authored events regardless of the delivery ID suffix.

There are seven unique progression narrative scenes and 163 unique progression nodes.
The fourteen delivery variants duplicate text for safe gating and do not represent fourteen separately authored scenes or twice the word count.
Together with the unchanged opening, the selected story has eight narrative scenes.

## New continuation

The lime-kiln scene follows the cistern's appointment with Serevin.
Vey's fate changes the approach.
If spared, he returns voluntarily with a warning and leaves before the confrontation.
If coerced into service, he brings Serevin's receipt and negotiates either a share with release or continued compulsory work.
If dead, Serevin becomes suspicious when he misses the appointment, and the Commander must retrieve the public receipt during her patrol.
These are distinct pages rather than an outcome-neutral recap.

An intact Tower shard permits an Arcana approach to the lamps' mechanism.
The broken-shard history instead uses the Commander's residual scar and physical wear on a latch, with a Perception check.
Both checks are one-shot, and failure keeps the confrontation available while withholding the prepared receipt trap.

The prepared Trickster option makes Serevin's acknowledgement identify her as both the recipient and the delivery.
It requires a prior successful investigation and has its own one-shot World check.
Success frees the prisoners, captures Serevin and preserves her ledger.
Failure requires an immediate rescue and lets Serevin escape with the ledger.
An ordinary good option chooses the prisoners over pursuit.
An ordinary ruthless option captures Serevin and obtains the ledger while the prisoners suffer additional injury before release.
The choices record whether Serevin is held or escaped, whether the ledger was obtained, and whether the workers were hurt for it.

Captured Serevin supplies a lower-vault destination under a ruined watchtower.
If she escapes, a rescued worker supplies the destination but the next location is warned in advance.
The lower-vault encounter itself is not written yet.

Vey's coerced-service bargain also receives a local settlement.
Promising his book back results in its return and `vey_released`.
Keeping his debt in force results in `vey_obligation_continues` and a warning from Devarra about the betrayal that coercion invites.
No money is recovered from this encounter, so the promised percentage generates no invented cash reward.
Inventory, custody, injury and payment descriptions remain manuscript actions and custom flags rather than implemented game API effects.

The ending offers private closeness or a quiet meal followed by separate rooms.
Devarra stays physically in dragon form throughout, matching the wing, talon and muzzle actions in the existing scenes.
No humanoid portrait, transformation or assigned art is implied.
The romance remains graphic and explicit and voluntary.
Her possessiveness, contempt, appetite for revenge and tactical interest remain visible; successful rescue does not make her a moral admirer of every Commander choice.

## Native and authored material

The saved and lost clutch histories are unchanged from the inspected native evidence.
Vey, Serevin, the collectors' devices, the lime kilns, the prisoners, the receipt trap and the ruined watchtower are authored alternate developments.
The contract now names these additions explicitly.
Neither the shard nor the lamp mechanism proves an existing canon restoration power.
Initial acquisition, main-campaign restoration and durable actor presence remain missing.
The new quest protects Devarra's continued presence after access already assumed by the earlier scenes.

## Verification

`py -m storylines.devarra_trickster_progression` passes.
`py -m py_compile storylines/devarra_trickster_progression.py` passes.
`git diff --check -- storylines/devarra_trickster_progression.py` passes.

The graph check covers all seven unique narrative templates for duplicate IDs, edge targets, reachability, cycles, balanced narration tags and one-shot checks.
The delivery check tests all sixteen combinations of saved, lost and native-cue flags for every scene and requires exactly one variant only for a matching pair.
It also verifies that template IDs do not occur in the delivery collection.
The staging check follows the actual ordinary public-plan path into the bridge, checks its prepared folio and absence of time-intervention flags, and checks the mutually exclusive arrival and shard-aftermath pages.

The four-scene carried-state traversal covers the envelope, bridge, cistern and kiln with both valid histories.
It rejects reachable dead ends, enforces delivery predicates, explores each skill outcome and checks exactly one collector fate, one shard fate and one Serevin fate on completed paths.
The ledger exists exactly on captured-Serevin outcomes.
All three Vey fates and both shard states can reach either kiln outcome.
A Vey-service path ends with exactly one of release or continued obligation, while other Vey histories get neither.

## Fresh selected-path count

A separate full-route solver traversed the matching opening followed by all seven guarded progression variants.
It carries real choice flags across scenes, applies requirements and forbids, checks requirement groups, rejects abort and closed/refused results, and explores both skill outcomes.
After each scene, it discards only flags that cannot influence any remaining predicate or the required final completion state.
The tokenizer and normalization are taken from `tools/measure-story-content.py`.
Titles, unused answers, duplicated history variants and external native/RanRomance words are not counted.
The entry fixture assumes current Trickster, an available actor and verified native history, exactly as required by the opening.

| Narrative scene | Saved brood | Lost clutch |
| --- | ---: | ---: |
| Opening | 650 | 610 |
| Evidence and terms | 2,311 | 2,311 |
| Echoing slate | 1,236 | 1,236 |
| Meal | 1,537 | 1,537 |
| Second envelope | 1,384 | 1,394 |
| Bridge | 1,318 | 1,318 |
| Cistern | 1,558 | 1,573 |
| Lime kilns | 2,005 | 2,005 |
| Compatible selected maximum | 11,999 | 11,984 |

The four-scene continuation maxima are 6,265 and 6,290, matching the source self-check.
The full current routes are still 9,001 and 9,016 words below the 21,000-word floor.
The count is a modeled maximum, not a guaranteed minimum for every player selection or a judgment of semantic value.
A different reviewer must assess this source's voice, meaningfulness, canon handling and branch integrity.

## Outstanding requirements

The lower-vault plot and its warned/unwarned consequences remain unwritten.
The older evidence and meal scenes still need the voice review already requested.
A complete mature relationship and its endings are not present.
The initial attainable Trickster acquisition is unresolved.
Registration, actor delivery, native condition producers, persistent runtime effects, art assignment, ToyBox verification, save/load checks and in-game tests remain absent.
No route-ready claim or review score is granted.
