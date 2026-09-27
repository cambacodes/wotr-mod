# Wenduag continuation audit: independent review

## Verdict and scope

Revision required before this document can serve as the full production plan.
Its central characterization and distinction between native history and authored alternatives are useful.
The twelve printed native identifiers resolve correctly, and the proposed budget adds up.
The missing acquisition contract, unresolved chronology, omitted DLC6 material, and measurement mismatch prevent approval of the plan as complete.
These findings do not establish that the proposed routes are impossible.

Reviewed input: `reference/canon-review/wenduag-continuation-audit.md`, SHA256 `19B4BCE13BD9B11C97222D76ED7508B50B4511348DDE50343A489E4B33E0C3E2`.
Review date: 2026-09-27.
I did not author that report and changed no manuscript, production source, manifest, or exported story.
This is a research/design review, with no numerical literary score for unwritten scenes and no art, runtime, or campaign approval.

I read the complete report, its Wenduag text evidence, relevant project requirements and measurement code, and independently inspected matching records in the installed `blueprints.zip`.
I also inspected native DLC6 Wenduag records and selected localized dialogue, and checked Vellexia's late-date departure records against the existing Vellexia audit.
I did not execute native conditions in Unity or complete a new exhaustive extraction of every Wenduag branch.

## Confirmed evidence

All twelve explicit blueprint GUIDs in the report match the installed archive.
The companion `ae766624c03058440a036de90a7f2009` is a `BlueprintUnit`.
The companion root, Q1 DeadDyra, Q1 Drill, Q2 essential, Q3, Redeemed, romance root, active romance, and FinalRomWithWendu identifiers are `BlueprintEtude` records.
The remaining two are flags, as detailed below.
The unusual hyphenation of the printed unit GUID does not change its normalized value.

The examined export contains no Wenduag relationship or Wenduag-owned continuation scenes.
The report correctly treats the existing romance as native content that cannot be credited toward newly authored volume.

Its account of Wenduag's strength, self-interest, tribe ambitions, danger, and capacity for attachment is supported by the native companion and romance text.
Useful precise anchors in `reference/expansion/wenduag.txt` include:

| Native cue | GUID | Supported point |
| --- | --- | --- |
| Companion Cue_0034 | `ce1991b817c352e4386025702f56fe1d` | Service and mastery can be mutually advantageous. |
| Companion Cue_0049 | `26a1b1af3826a584385d28de115dd6b1` | Being the former chief's daughter does not establish fitness to lead. |
| Companion Cue_0132 | `0267c6f5fd920ac41b57f5dc31a16201` | Her existing Trickster response admires destructive laughter and demonstrated power. |
| Companion Cue_0201 | `0b1ec1e09cf55a84f82c2347e74eb80f` | Her people's survival and future power remain practical concerns. |
| Companion Cue_0223 | `69bfb258f42dda74291052e4d66e17c3` | The Commander's earlier treatment of her can obstruct later sexual access. |
| ThatIsFinal Cue_0039 | `ac019438d0dd8304b953e5f90916ae0e` | Fear of losing the Commander and remembered family loss support genuine attachment. |
| ThatIsFinal Cue_0103 | `3e847706f1f9fe54e86e89298f488c7c` | Love can conflict with her own judgment of her fitness to lead. |

The poison offer and refusal are native, including refusal answer `0e6aa510c309eff498bbf2930de2b036` and the stinger application cue `088bb4898c4aa4245bf2719eae7dbfe8`.
They support divergent continuation material without silently granting communion.
The female Commander claim is supported by romance-specific gender substitutions, including the poison-marriage ending text under localization key `0bcfaf70-95e0-4d08-ac3f-291dc019723a`.
The generic companion address "Mistress" alone would not prove romance eligibility, but the additional romance evidence makes the report's limited dialogue-level conclusion reasonable.

## Corrections to factual or measurement statements

### R1. Separate flags from etudes

`WenduagRomance_LichRomanceEnd_flag` `cd59ed13f1a2c174b8a63afa166ee147` and `WenduagRomance_VelexiaConflict_flag` `23cacf7a07480da459b3a59d0fd6da82` are `BlueprintUnlockableFlag`, not `BlueprintEtude`.
Their paths happen to be under `World/Etudes`.
The body partially acknowledges flags, but the closing instruction to extract "BlueprintEtude records" for Lich closure and Vellexia conflict is inaccurate.
Correct the type inventory and specify flag unlock/value observation separately from etude lifecycle observation.
This is a type correction, not a finding that the GUIDs are fabricated.

The FinalRomWithWendu etude is also not a passive proof that the finale has already happened.
Its activation requires the active romance playing, a companion availability condition, and an unlockable flag condition.
Its components start dialogue, teleport the party, and complete a lock-controller etude.
Its GUID alone cannot serve as a completed-confession predicate or be safely activated to manufacture continuation eligibility.
The report already admits that these actions need further research; retain that limitation prominently in the eventual adapter specification.

### R2. Correct the measurement promise

The fifteen budgets total 27,300 words, exactly 30% above 21,000 and approximately 24.09% above the report's stricter 22,000 target.
There is no arithmetic error in the stated comparison with 21,000.

However, `tools/measure-story-content.py` includes node prose and choice text in `distinct_segment_words`.
It removes exact normalized whole-segment duplicates, not repeated phrases within different passages, semantic paraphrases, or duplicated character credit across routes.
Its own output explicitly excludes claims of originality, reachability, per-character attribution, and quality approval.
The report promises a 22,000-word measure excluding choice labels and repeated phrases while directing the writer to that tool as if it supplied the same measure.
Choose and document a consistent metric, or add a separately reported prose-only/manual attribution calculation.
Do not relabel the existing tool's total as prose-only distinct new words.

The budget also needs a delivery ledger.
Scenes 12 and 13 contribute 3,800 words for unproven recovery routes.
Scenes 8 through 11 contribute 7,350 words for optional multi-woman material.
Removing both categories leaves 16,150 planned words; removing the optional final visit as well leaves 14,450.
This does not prove that each playthrough must contain 21,000 words, since the project counts authored branch volume.
It does show that the current minimum depends on delivering substantial optional or unproven branches.
Only completed, integrated content can satisfy the final total, and the same triad passage cannot be credited in full as independent Wenduag, Vellexia, and Nurah routes.

### R3. Keep ToyBox outside the fiction

Scene 2 explicitly lowers Wenduag's trust if the Commander "invokes ToyBox settings as if they were in-world permission."
That is an inappropriate proposed fictional event and contradicts the report's otherwise sensible separation of configuration from character knowledge.
Replace it with a concrete in-world broken promise or attempted assertion of ownership.
Keep compatibility settings and their tests in implementation documentation.

## Missing research and design decisions

### R4. Add the installed DLC6 romance to the duplication audit

The report's native-content inventory omits an installed Wenduag romance event in A Dance of Masks.
The archive contains `World/Etudes/Common/DLC6_DanceOfMasks/DLC6_WenduagRomanceEvent.jbp`, GUID `04850c8504ac4bac9378aecbb0a65811`, and a Wenduag romance area `31bc528a69344416be7eb39f08dbe3ba`.
Selected native dialogue under `World/Dialogs/DLC6_ADanceOfMasks/TavernFinal/WenduagRomance/` confirms substantial relationship material rather than an unused name alone.
The Labyrith cue `8387f44a42934d1dbfa97525a0f65805` identifies the Shield Maze as the place that formed her; `889fa023831c439bbaa6f1086a697474` introduces a lethal alchemist-fire threat; `76c2f48661244268ac98f74036d6d014` concerns burning her past and what awaits outside it.

These overlap proposed themes of former service, danger, trust, and an ending beyond old wounds.
Read the full event and its entry/completion conditions before claiming the new arc avoids duplicating native development.
Record optional DLC availability and completed-event history separately; archive presence does not establish DLC ownership or event completion in every save.
This is a missing research task, not proof that the proposed scenes necessarily duplicate the DLC.

### R5. Resolve chronology and physical access

The outline places the Chapter 5 poison aftermath in Scene 4 before the Vellexia branch in Scenes 8 and 9.
The native jealousy and date material belong to Chapter 4.
Vellexia's Third_Date cues `58d69774dbe696e46a9232167e8d3479` and `33fbc8d0ca697f044861681fc2cecbf6` both invoke departure cutscene `4328c84d571762247a31bdefe240675e` using her third-date spawner.
There is also a native Vellexia death etude `72e423c719ed9d44fa432a6b9629babd`.
Neither a remembered jealousy flag nor a non-death outcome proves that a living, visible Vellexia can be contacted later.

Choose a Chapter 4 branch placed before the poison aftermath, or research a specific later return/recovery route with its own actor and location proof.
Do not silently treat a chronological list as freely reorderable after writing dependent scenes.
The proposed Nurah branch likewise needs her current invitation and meeting contract, not historical acceptance alone.
The final "after victory" visit requires an explicit supported timing window or a narrative ending presentation; the report supplies no playable postgame delivery proof.

### R6. Specify the attainable Trickster acquisition

Scene 1 requires an already active native romance.
Scene 12 requires prior relationship evidence.
Scene 13 may remain design-only.
Together these do not yet satisfy the requested bespoke attainable Trickster route for a missed or closed romance.
The report acknowledges the need, so this is an unresolved requirement rather than a false implementation claim.

Produce a history matrix covering native active romance, missed opportunity, rejected romance, dismissal, betrayal, and death.
For each proposed supported entry, identify an actual quest connection, current actor/contact route, player discovery or check, cost, failure outcome, and earned invitation.
Native companion cue `fbb8c7b423948ec47ad43f6e3d3dad9a` explicitly addresses an opportunity offered too late and is a useful source to investigate for the missed-romance case.
A chain of unspecified bargains is not yet a fate intervention or a gameplay acquisition route.
Other mythics need a separately verified restriction matrix rather than inheriting every Trickster exception.

### R7. Preserve Wenduag's specific forms of desire and loyalty

The report rightly rejects instant agreeableness and automatic redemption.
It should also avoid replacing her existing chosen service, appetite for domination, and dangerous affection with a universal demand for an equal negotiated arrangement.
Native companion cue `83679020eeb5a2d459da634ca090c3c7` explicitly offers to behave as ordered.
That does not erase her self-interest, but it means subordinate language or a possessive dynamic is not automatically out of character.
Scene 1's rejection of being a collectible can work if grounded in the player's actual treatment and her current history, rather than becoming a mandatory correction of every unequal bond.

Conversely, the native positive ending under localization key `f16f4633-c5b1-4a55-885e-4c8f7074e330` allows gradual softening over years.
Respect that earned development where it applies instead of making every version of Wenduag equally treacherous forever.
The current outline repeatedly returns to terms, ownership, boundaries, and contracts.
Require distinct external problems and embodied encounters so fifteen scenes do not become repeated relationship negotiations.
This is a pacing and characterization risk in a design, not a literary failure measured from a finished manuscript.

### R8. Clarify the optional mutual-women premise

The report correctly labels both pairings as authored alternatives and refuses to equate native jealousy with mutual attraction.
Vellexia's established relevance is evidence for an encounter, not evidence that she is the strongest romantic match.
That preference should remain an authorial hypothesis until actual reciprocal scenes earn it.
Nurah also needs her own desire, refusal, and bargaining position rather than being acquired through Wenduag's influence.

Scene 10 says Nurah challenges "both women" and Scene 11 calls the participants "the three women."
Those lines assume a female Commander.
If these are explicitly female-Commander branches, say so; otherwise write gender-responsive references while keeping both partner slots women.
The report should distinguish Wenduag declining a triad from Wenduag imposing a global exclusivity lock on the Commander's other independent romances.
Emotional jealousy and conflict can remain without defeating the requested no-jealousy compatibility mechanically.

## Evidence pins and limits

Repository evidence SHA256:

| File | SHA256 |
| --- | --- |
| `reference/expansion/blueprints.json` | `79E261E2FBC9F85E7899E5B5DFE67CC3EDB15772F5EE479F46A8D27885B58B39` |
| `reference/expansion/wenduag.txt` | `9484BBF2F922B98CD756D040290ACBB38F5E098C412581673A6903BE62540AD4` |
| `reference/expansion/etudes.json` | `6687429FB6EB4A9B27E1F6AEF4053E33EBF929C80D5AE46F80DA762B500AB5E1` |
| `reference/story-review/Wenduag.txt` | `17635E0C384C4EB13BCC0458BB61C4CF304BB292A0656E600FFC760A7C805393` |
| `reference/canon-review/wenduag.txt` | `8CCEBFDFE2F0343FBA191CDEC27321483E57942D42F38E0B0521AAE9CB5BE568` |
| `development/Story.json` | `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC` |

Selected installed archive entry byte hashes:

| Record | SHA256 |
| --- | --- |
| Wenduag companion unit | `8B292F2670119ABA71A08200080E00066E6929562AD6C09D4C20450D85A4B125` |
| FinalRomWithWendu etude | `BB15D5573FE561E1A26294C5DD926B67CAB02462AA48F281513C993FD0F3BACD` |
| LichRomanceEnd flag | `838B3258C37A70778145184FFB88FED6232A21D581B27BED8546C76E323168FF` |
| VelexiaConflict flag | `90B8BD78A9C473EC45961440A0508C9BEAC632C1716EE5245FC5F0D0A258ED75` |
| DLC6_WenduagRomanceEvent etude | `42254D321E61BD3AF1A802C95C148EE8D109C27151BD0B3292A00C7DBCCCBE93` |
| Vellexia Third_Date Cue_0098 | `404DB88FFD63E966379086B120E4976C308DDA49DA2CD9824C4F8C706C05D696` |

Python probes independently normalized and resolved all twelve printed identifiers in the installed archive, inspected actual record types and selected components, looked up DLC6 cue text in installed `enGB.json`, inspected the export's relationship ownership, and recomputed the budget.
Localization keys cited as ending evidence are text keys, not claimed blueprint GUIDs.
The report's extracted path index is useful for finding records, but a path name cannot establish runtime type, active lifecycle state, action safety, or reachability.
No route approval, successful restoration, working triad, complete mythic compatibility, or live ToyBox behavior follows from these checks.
