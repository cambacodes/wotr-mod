# Nocticula continuation author handoff

Status: revised complete manuscript candidate for a second independent review, not approved or exported.
Date: 2026-09-26.
Owned source: `storylines/nocticula_continuation.py`.
Frozen SHA256: `9CDD2490621BCE273D3E36E7977208EAFBE41173E0D80ED0BCA8A42EF89E6E74`.
The author supplies no editorial score and cannot independently approve this work.

## Delivered scope

The uncounted shore is a sixteen-visit living continuation of the existing RanRomance Chapter 5 dream relationship.
It contains 117 visit nodes and eight supplementary ending nodes, for 125 nodes total.
All intimate participants are adults; new intimacy is non-graphic.
No portrait has been assigned and no art is claimed complete.

Nocticula asks the Commander to investigate a private passage operating under a stolen remnant of her protection.
The investigation concerns missing passengers, sale of unfinished arrivals, an instrument whose limits must be learned, and a magician who would like to exchange culpability for useful employment.
Choices determine investigative method, protection for a witness, the demand made at a demonstration, who carries the return tokens, how the crossing is reinforced, the price of the rescue, the magician's disposition, and the answer to the remaining buyers.
The personal relationship develops through private company, conflict over ambition, and a final invitation which can be accepted or limited without overwriting the original bargain.

The campaign preserves Nocticula's appetite for power and her willingness to threaten, confine, exploit a rival's weakness, or employ a dangerous person.
It does not make redemption mandatory or claim that a successful rescue establishes a good alignment.
The Commander may act from rescue, ambition, or curiosity, and the final scene recalls the selected motive.
Trickster options use competing buyers, a question exposing an unguaranteed berth, a counted limitation on new research, and an exact auction that turns a threat back on its financier.
These are authored strategic interventions, not claims that a native mythic ability automatically changes history or compels desire.

## Entry and integration contract

Every living visit requires all of these read-only witnesses:

- `noct.parent_active`, parent `RanRomNoctActive`, `18affced672d4c56a52bf6ffc00601b9`.
- `noct.parent_agreement_seen`, at least one accepted Book 2 terminal cue: `631bf0ede36742559cee476f34dcb5de`, `cb13766be07b448f8cacb477be32e13c`, or `5388a7d7a1da48deb333d34abab1a6d0`.
- `noct.gift`, native `ProfaneGift`, `0c1695f4a362f0243a4afcfd1957eb0d`.

Every living visit forbids NocticulaDead, the parent's Reject state, this extension's closed state, `inhuman`, `legend`, and `dragon`.
The first visit has zero delay; subsequent visits require the prior authored outcome and twelve hours.
Visits are optional `Memory` scenes, `Remote=True`, restricted to Chapter 5 and Drezen.
They narrate sleep and dream meetings; they do not spawn Nocticula, transport the Commander's physical actor, or make her a party companion.

The module's `integrate(payload)` registers its verified Etudes, SeenCues, and Relationship metadata only.
It checks existing bindings for conflicts.
It does not append scenes, change any parent blueprint, or edit a shared exporter.
Root owns copying SCENES into an isolated candidate and registering integration at the appropriate stage.
No exporter, manifest, shared Story.json, tests, art, or installed mod was changed by this author task.

The module contains 83 authored effect flags, all in the `noct.` namespace and none colliding with its native or parent binding keys.
It never writes ProfaneGift, Active, Reject, Laulieh states, RanRomCount, ShamiraKilled, native quest state, gold, inventory, or physical actor state.
Money, payments, travel, and injuries within the new affair are narrated consequences involving authored participants.
They are not claims that crusade resources or the Commander's inventory were changed.

## Canon and parent evidence

The evidence base is `reference/canon-review/nocticula-parent-extension-audit.md` and the installed parent/native material it pins.
The author of this manuscript also wrote that prior audit, so a different reviewer is required for the new implementation and characterization.
The audit itself is not approval of this manuscript.

The installed parent DLL hash remains `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Its localized strings hash remains `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
Fresh decompilation evidence is in `C:/Users/Z/AppData/Local/Temp/nocticula-audit-8d261252/`.

The accepted terminal cue bindings resolve to Book02Page002 Cue0020, Cue0021, and Cue0022 respectively.
`noct.parent_ambition_heard` resolves to Book03Page003 Cue0002, `b3a4ce99bc30440fa9ebcbfce2776176`.
The optional Socothbenoth callback requires native c5 Trickster Nocticula Cue0016, `bb552fe4e21cb874fa3c98c2cc328186`.
Thus the Commander cannot claim that disclosure merely from being a Trickster.
Laulieh callbacks require the actual parent LaulRom or LaulRom2 state.
The latter recalls the promise to give her a chance to leave without guaranteeing the departure or the acceptance of another realm.

The parent already explicitly accepts other lovers.
The new campaign makes no blanket exclusivity demand, does not clear any other romance, and does not grant permission on another partner's behalf.
No new played triad is authored here.
Existing parent Laulieh intimacy and the narrowly gated ascended Arueshalae/Nocticula/Commander ending remain parent content, with no new word credit claimed for either.
The chapter 4 fling and the parent's later uncertainty about feelings are registered as verified history keys but are not required entry conditions.

The harbor, its rules, Orren, Dessa, Meret, Ilvara, Vessa, Tomar, Halren, Ren, Sere, Teren, Rhez, Senet, and Ossin are authored additions.
Dream reconstructions use recorded replies and reports; they do not claim live remote observation or knowledge of questions never asked.
The story distinguishes a flame marking an unfinished arrival from a soul and does not assert that Nocticula can create, replace, or resurrect arbitrary souls through this method.
The limited Trickster reinforcement is prepared by Nocticula's agents as new work within the invented incident.
Its success is a fact of this alternate story, not a documented base-game power.

## New content ledger

The inventory counts only node Text and choice Text.
It strips brace and angle-bracket markup, collapses whitespace, deduplicates exact normalized segments, and counts Unicode alphanumeric words with internal apostrophes.
Metadata, titles, comments, IDs, journal guidance, and parent text receive no credit.
The total is branch-inclusive manuscript content, not words read in one playthrough.
Independent reviewers must still decide whether it is meaningful content rather than treating the numerical floor as literary approval.

- Raw text/choice words: 25,411.
- Distinct normalized text/choice words: 25,323.
- Distinct visit words alone: 24,192.
- Distinct supplementary ending words: 1,131.
- Segments: 302 total, 287 distinct.
- Parent-credit contribution: zero.

| Visit | New distinct words |
| --- | ---: |
| unlit_quay | 881 |
| sixth_passenger | 1,148 |
| lamp_measure | 1,117 |
| captains_reply | 1,458 |
| her_own_face | 1,320 |
| white_shoes | 1,431 |
| demonstration | 1,621 |
| voices_in_glass | 1,313 |
| cost_of_return | 1,507 |
| return_count | 1,563 |
| after_the_lamps | 1,375 |
| another_place | 1,431 |
| hearing | 1,837 |
| last_buyer | 1,681 |
| what_she_keeps | 2,569 |
| second_door | 1,940 |

## Revision after the first independent review

The independent first report remains revision-required evidence for source `853B655BBC4E7137A5E089388265A622D261623CA03321880DAB9EF75352ED47`.
It is not superseded by an author's assertion that the corrections are sufficient.
A second independent full read must judge this revised candidate.

The seventh berth is now shown in Dessa's final copy in the common white_shoes/meeting node before every applicable choice.
The common cost_of_return opening introduces Teren as a pilot consulted about return precautions, without claiming he volunteered on the Ilvara-carrier branch.
The hearing/business response now concerns the proposal just made rather than recalling the exclusive contradictory-buyers method.
The private night introduces the book's flood and poisoner anecdote itself rather than importing the queen and drainage story from the unselected conversation.

The her_own_face common opening explicitly acknowledges the continuing gift and its coercive potential.
Nocticula chooses to ask for an answer in this meeting; neither the scene nor its effects removes her existing power.
The demonstration's anger, the threat against Dessa's employer, and several aftermath responses now show specific appetites and conduct instead of relying on a narrator's statement that she remains dangerous.
Private final company and alliance scenes contain actual exchanges and physical intimacy within the non-graphic limit, replacing assurances about what the encounter should mean.
A sustained narration pass removed author-facing moral and ending guarantees across the investigation, aftermath, final invitation, and all eight recollections.
This is an editorial revision submitted for judgment, not proof that the character voice now passes.

The commissioned Ilvara outcome now leads to one of four new report nodes under the exact earlier hearing-method flag.
`fee_admission` recalls the successful check through a disputed maintenance charge and the useful written admission.
`extra_observer` recalls the failed check through a second paid observer and two delayed proposals while the unexplained danger is examined.
`return_condition` recalls the direct question by rejecting a paid-clerk substitute and requiring actual return appointments.
`new_price` recalls the Trickster business question through limited installments rather than paying for promised future power.
These are narrated consequences, not crusade-money deductions, GameTime increments, or claims that a native blueprint has changed.
Confinement and exile do not employ Ilvara and therefore do not acquire the conditional employment cost promised on the failed-check branch.
The existing scene gates, native bindings, private effect vocabulary, and ending selectors are unchanged.

Author probe ledger: `C:/Users/Z/AppData/Local/Temp/nocticula-revision-author-probe.json`.
Root reported 569,185 actual focused Rules assertions on an intermediate revision, not on this final frozen hash.
The author does not transfer that result to the final candidate; root will rerun its owned tests after freeze.

## Author verification performed

Python import with `-B` passed without writing bytecode.
Local structural checks found unique node IDs, valid direct and skill-check targets, and no native-bound effect writes.
All six observed cue GUIDs were resolved against the decompiled parent classes or the verified native Trickster witness.
A wording scan found no em dashes and removed two accidental out-of-world descriptions before freeze.
A continuity scan also corrected an unconditional claim that the Commander had selected the curiosity motive.

A custom author data traversal supplied 32 combinations of Trickster, LaulRom, LaulRom2, parent ambition disclosure, and Socothbenoth disclosure history.
It explored direct choices and both skill-check results, retained only flags read by future nodes when merging states, and rejected any reachable node without a valid choice.
The revised source traversal reached all 117 visit nodes and 172 distinct choice/check outcomes over 108,976 evaluated transitions.
The three completed ordinary outcome histories each selected exactly one of the company, alliance, or limit recollections.
A final wording correction changed an unconditional chart reference to a report; it changed neither the traversed structure nor the word count.

This is an author structural probe, not an independent review and not execution of the C# Rules engine.
No Unity dialog, native condition evaluation, real sleeping transition, ToyBox setting, actor lifecycle, portrait crop, or saved-game migration was executed for this new module.
The eight endings require separate full selector coverage under actual Rules and native ending order.

## Endings and remaining project scope

The ending pages are supplementary recollections of the completed undertaking.
Three distinguish its final personal answer; five cover Nocticula's death, sacrifice, ascension, changed Commander, and Aeon history.
They deliberately do not replace or promise the outcome of Nocticula's older Worldwound bargain.
They do not claim permanent romance after a native or parent rejection.
No parent ending suppression or replacement contract is supplied.
Root must review their delivery against actual native and RanRomance endings, including Expanded Epilogue if supported, before registering them.
Interrupted campaigns retain the parent's own outcomes; this candidate does not add an unfinished-campaign epilogue.

The following remain unimplemented and must not be reported as fulfilled by this living continuation:

- A bespoke Trickster acquisition route for missing or rejected parent relationships.
- A Nocticula death recovery mechanism with soul/body evidence and original actor provenance.
- Re-entry after losing ProfaneGift or a separately earned replacement contact method.
- An alternate Trickster quest resolution preserving living Shamira while satisfying the actual essence and Council requirements.
- A new played Nocticula/Arueshalae or Nocticula/Laulieh triad campaign with independently earned mutual chemistry.
- Native export, binding validation, actual Rules tests, managed blueprint checks, and live play verification.
- Art generation, independent art review, and any portrait assignment.
- Installed ToyBox Love Is Free and Jealousy Begone coexistence tests.

The source is ready for the different reviewer's full read and targeted criticism.
It is not ready to be called approved, integrated, playable, or complete across every planned mythic and recovery history.
