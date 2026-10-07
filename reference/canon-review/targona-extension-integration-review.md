# Targona extension integration review

The corrected source is accepted at the bounded story, native-binding, and parent-source contract levels.
The author corrected the one concrete presentation defect identified during review.
The corrected portrait stage passed the parent's rerun, and no remaining source-level technical blocker was found.
The final literary text revision has also been inspected and is accepted without a new technical finding.
This acceptance concerns the Targona portion of the combined stage, not an independent review of Kiana content authored by this reviewer.
This is an independent technical review, not a literary score or approval of the complete Targona campaign.

## Reviewed revision

The previously verified portrait stage is `D98EA8E9D15CF663C6B3CE582B0FCAC406FE9F71D721787600202957ED9F62A1`, with 252 scenes.
The reviewer independently verified its hash and exact equality of all six Targona scenes to corrected source `FCEDE76356BEDF31AB0F1AD24E25B1538C5139E258643D27D661643D6C3C36BE`.
The table preserves the initial review inputs used for the full independent rule rerun and native-source analysis.

| Artifact | SHA256 |
| --- | --- |
| `development/targona-extension-review.json`, 252 scenes | `5274FDE367E4E00B425A9DA7ED56F6728F404662A9763FDD0F367606693F136C` |
| `storylines/targona_opening.py` | `E83E9F421E60945C3A2C44A00E3C4A7572C4AB50403A0F5B5F7D0F4B27A6F24F` |
| `tests/TargonaOpeningTests.cs` | `379712006196354DEDBE536A6762D9C2A28CF97AA6892883BDCF3E006FEDA4F3` |
| `reference/canon-review/targona-parent-bindings.json` | `39D1108E85484D188EC002D2AE5D6B66BC85DE4CDBC948C76EB56BF2D3BDCE57` |
| `tools/parent_bindings.py` | `B27E66D5301AEAE4C4E757C51A2C408F219E4BE1BBD29E94CE5BEF4973AF9E9B` |
| Installed `RanRomance.dll` | `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68` |

All six staged Targona scene graphs match the current source exactly.
The module's Etudes, CompletedQuests, and SeenCues mappings match the stage.
The reviewer independently reran the existing compiled RulesTests against this stage and obtained PASS with 11,405,557 assertions.
The output explicitly excludes Unity execution and real save persistence.
The parent-manifest unit tests also passed independently, covering the accepted fixture, changed assembly bytes, wrong type, duplicate record, and mismatched identity.
No shared source, staged JSON, installed file, or test file was edited by this reviewer.

## Corrected finding: incorrect portrait fallback

The initially reviewed revision left all 39 new pages with Portrait empty.
`Main.BookPatch.Postfix` resolves an empty narrator portrait to `Together`, rather than to the scene's owner.
`Portrait("Together")` reads `CustomNpcPortraits/RanRomance-Tirabade/Scenes/Together.png`.
The reviewer confirmed that this file exists in the installed mod tree.
Thus the initially reviewed correspondence could display the Tirabade scene image despite containing neither wife.

Set an explicit outcome-neutral correspondence portrait key on these pages, or otherwise suppress the unrelated fallback through an intentional supported presentation path.
This does not require pretending that new outcome-specific art already exists.
A missing intentional image key safely leaves the underlying book picture unchanged under the current engine, whereas an empty key selects a known unrelated image.
Any later Targona or Anograt image must still respect the actual parent transformation history.
The finding was sent to both root and the source author.
The author corrected all 39 pages to the explicit `TargonaCorrespondence` key and added a focused assertion requiring it.
Corrected source SHA256 is `FCEDE76356BEDF31AB0F1AD24E25B1538C5139E258643D27D661643D6C3C36BE`.
Corrected test SHA256 is `AB65CD02AD2FF1F0B6AEC1982E141082311D35186F603E937728DEF3E7838AD8`.
The reviewer independently compared every scene, page, and choice against the initial stage and confirmed that only Portrait fields changed.
The missing neutral image does not trigger a fallback retry and does not explicitly clear EventPicture; the current engine leaves the underlying book picture untouched.
That prevents the verified explicit Together lookup but is not approval of finished Targona art or proof of the eventual rendered background.
The addon does not set an explicit default image when building these pages, and its postfix does not clear an inherited picture when the requested asset is missing.
What the game's own SetPage leaves in EventPicture, including any visual carryover, must therefore be observed in Unity or addressed by a separately reviewed fallback policy.
The code-side portrait-selection finding is closed, while actual image presentation remains a runtime verification item.

## Parent creation and completion evidence

The reviewer directly decompiled the installed assembly with the existing ilspycmd, reading stdout only.
All 17 manifest creation records were independently matched against the relevant decompiled type.
There are 12 BlueprintEtude creations in `RanRomance.Targ.Main.Configure`, one BlueprintQuest creation in `TargQuest.Configure`, and four BlueprintCue creations in `TargBook04End.Configure`.
The installed assembly hash matches the manifest pin.
The quest and cue excerpts are selected noncontiguous lines, not a claim that the declarations and calls were adjacent in the decompiled method.
Their local variable-to-GUID associations are correct.

`RanRomTargQuest`, GUID `6ec03ce2f763460c8ac89f4c2064c5ad`, contains final objective `227778a66d0f478fbb6e1b7e89758d22` with SetFinishParent.
`TargBook04.Configure` installs a FinishActions call to SetObjectiveStatus on `RanRomTargQuestEntry0003`.
The extension additionally requires a witnessed final cue, so merely opening the parent finale is insufficient.
The parent also has a hidden finishing objective; retaining both the actual quest-completion test and the final-cue witness is therefore useful rather than redundant.

The four accepted final cues are correctly associated with the parent's real ending conditions.
`ad655c40be31401386b85287483b3841` covers nonromantic suitable single-person outcomes, including outcomes the extension separately excludes.
`cfc5f3cb2cf94672a96cab742e62225d` covers nonromantic Aeon/Trickster outcomes with Anograt.
`62c24328ae744ee98fabd219dbe74c92` covers romantic Aeon/Trickster endings.
`ec76729da60441a1b2028f340743c0a8` covers other romantic outcomes, again constrained by the extension's independent history exclusions.
The cue union alone is not treated as proof that every transformation is compatible.

The extension reads active `RanRomTargRomance` rather than creating a substitute romance.
No authored effect starts or completes that etude, increments the parent's romance counter, changes the parent's wedding marker, or alters its epilogues.
The distinction between parent friendship and romance is retained on the actual letter pages.
A warm friendship reply during an existing romance is not interpreted as a breakup.

## Native and mythic predicates

The reviewer verified the four native GUIDs directly in `blueprints.zip` under `ImportantNPCs_fate/Targona/`.
They identify freedom, laboratory death, Mutasafen-lair death, and condemnation etudes of the expected BlueprintEtude type.
No copied or invented archive entry is used for the parent's new assets.

Parent transformation history and current Commander mythic status remain separate inputs.
Anograt appears only for actual parent Aeon or Trickster treatment history.
The optional impossible-paper choice requires the current `trickster` predicate.
A small-power parent result can therefore coexist with a current Trickster without fabricating Anograt.
The ordinary paper continuation remains available on Trickster.

The reviewed bounded support includes parent None, Angel, Azata, Aeon, and Trickster histories.
Current Demon, Lich, Devil, Swarm, Legend, and Dragon predicates and the incompatible parent transformation markers exclude these particular letters.
The parent's late Legend, Dragon, and Devil transitions complete earlier large-power history etudes; the reviewer confirmed those actions in `Targ.Main.Configure`.
The parent also reuses laboratory-death history in a Legend transformation, so this report does not interpret that alias as universal proof of a literal corpse.
The separate transformation restrictions avoid presenting that transformed character as the unchanged angel in this contribution.

These exclusions do not satisfy the roster's eventual all-candidate Trickster recovery requirement or promise every mythic transition.
No new resurrection, body restoration, native freedom, actor spawn, presence in Drezen, inventory letter, or permanent magical paper item is implemented or claimed.

## Delivery, effects, and interruptions

All six scenes are Chapter 5 Drezen correspondence, Remote and ManualOnly, with no ContactUnit or native answer-list attachment.
The existing manual Read interface exposes them when available.
`Rules.NextRemote` skips them, so they cannot take another route's automatic rest slot.
Subsequent scenes require their actual predecessor and 24 hours; the first begins after the genuine parent endpoint without an invented extra delay.
The focused suite rejects missing prerequisites, unsupported history, wrong chapter/area, death/path blockers, and a fake dialogue-start substitute for the ending witness.

Every new effect is attached to a terminal answer.
The focused suite asserts that every intermediate snapshot retains exactly the entry flags.
An interrupted skill-result page therefore does not retain a success or failure marker before the player acknowledges that result and completes the scene.
Reopening and choosing the non-roll door produces one outcome, not contradictory fold markers.
All later callbacks consume the selected publication, construction, fictional ending, and optional Trickster result.
Other romance and parent/native flags remain unchanged.
No new committed state is awarded by the correspondence.

Remote pages use the existing entry-time availability contract.
`ContactAvailable` intentionally returns true when no ContactUnit is configured, so these pages do not continuously recheck native death or mythic transitions while already open.
That limitation is documented in the author's handoff and is not disguised as verified continuous actor gating.
Ordinary chapter or quest progression cannot be assumed to occur concurrently with an open book; state modification through other tools still needs a real-game test and an explicit policy before claiming broader support.

## Manifest and initialization scope

`load_parent_bindings` verifies the pinned assembly bytes and validates identities, supported types, attribution, duplicate records, and creation-excerpt identity/type evidence.
It is not a decompiler or an authenticity proof for arbitrary supplied source text.
Independent comparison to the actual decompiled assembly supplies that missing review step here.

The offline binding verifier uses the manifest only for targets unresolved in the native archive and keeps `reviewed-parent-source` provenance.
The managed reader supplies explicitly marked `ReviewedParentFixture` typed objects only when an explicit manifest is provided and the native archive lacks the requested target.
It invents no parent quest actions or conditions.
Without the explicit manifest those objects remain unresolved.
These fixtures support construction and type checks, not an assertion that the parent initializer was executed.

The installed parent Info.json declares Harmony owner `RanRomance`, and its loader constructs Harmony using that actual ID.
Its BlueprintsCache.Init postfix calls `RanRomance.Targ.Main.Configure`, which creates the referenced records and calls the quest/finale configuration methods.
The addon source currently declares HarmonyAfter("RanRomance") together with its late postfix priority.
That is appropriate source-level ordering evidence.
It does not demonstrate successful parent initialization in Unity, compatibility with a different installed assembly, or the absence of an earlier exception in the parent's initializer.
The addon resolves required assets before creating its own content, so unresolved parent assets are not silently replaced with fake runtime blueprints.

Actual parent initialization, real parent save histories, manual Read UI, native roll presentation, saved-book interruption, correct artwork, and ToyBox combinations remain runtime checks.
For the initial stage, the parent reports 440 binding uses across 78 native and 17 parent-source targets and 31,070 managed assertions across 9,227 blueprints.
These are attributed parent results, not independently rerun managed checks.
For corrected portrait stage `D98EA8E9D15CF663C6B3CE582B0FCAC406FE9F71D721787600202957ED9F62A1`, the parent reports PASS with 11,405,563 rules assertions and 31,070 managed assertions over 9,227 blueprints.
Those rerun results are attributed to the parent.
After that result, a separate literary reviewer requested correction-history and blue-cup prose joins.
The parent applied those changes and the additional prose edits reviewed below.
Earlier counts remain attached to their original hashes; the final combined-stage results are recorded separately.
Earlier parent-fixture checkpoint totals are not substituted for a stage-specific result.

## Final text revision and combined stage

Final Targona source SHA256 is `D1552944742E7D3F4C59F900CDE634C8C43939D1C297CEA301FBF4C95126D369`.
The 252-scene Targona stage is `BB542280EFDCCD51B1044FC92B278E139B424A47A7C38E420EC662A2EE886F84`.
The 256-scene combined stage at `development/kiana-targona-final-review.json` is `D5E26EF079857222B1D306ECDD6E928F3755FCB6DFD829AB9DD03647A9DF9B87`.
The reviewer independently verified all three hashes and exact equality of all six current Targona scenes in both staged files.

The reviewer read the revised pages against the earlier source review and rechecked the complete technical graph.
Scene and node identities, choice order, targets, effects, requirements, exclusions, delay values, manual delivery, parent/native mappings, and the Perception25 contract remain as previously reviewed.
All 39 pages retain the explicit neutral correspondence portrait key.
No new actor, item, romance, parent quest, or native state mutation appears in the revision.

`second_margin/start` now describes Targona reconsidering her correction without claiming that every prior reply asked that question.
`the_unscheduled_door/receiving` now acquires the chipped blue cup before the shared ordinary continuation uses it.
`the_folded_room/cut` now actually trims the narrow strip that the later reply says she retained.
The other edits replace explanatory audit language with performed paper, drawing, or letter actions.
The original and copy remain distinct through the Trickster branch, and the added cup and paper strip remain authored scene props rather than awarded inventory.
These changes introduce no technical regression in the reviewed graph.

For the final combined stage, the parent reports PASS with 11,901,387 rules assertions, 31,632 managed assertions over 9,397 blueprints, and 444 binding uses across 78 native and 17 parent-source targets.
These final combined results are attributed to the parent; the reviewer's independent full rule rerun remains the earlier explicitly identified stage result.
The separate literary reviewer reports writing 91 and canon 93 for exact final Targona source D1552944.
Those are attributed literary assessments, not scores assigned by this technical review.

Bounded Targona integration is accepted for the final stage with no remaining technical blocker found.
The visual carryover, actual parent initialization, saved-game delivery, transformation coverage, and full-route limitations above remain open and are not waived by this acceptance.
