# Nocticula final integration review

Reviewed independently on 2026-09-26.
Disposition: the final manuscript delta, portrait assignment, exporter registration, and focused Rules coverage pass within their stated scope.
The default installed ending append is source-consistent with preserving the parent pages.
Native ending replay/persistence and the conditional Expanded Epilogue delivery path remain open integration requirements.
This is a development checkpoint, not full runtime or release approval.
Only this report and isolated temporary probes were written by the reviewer.

## Final reviewed inputs

| Input | SHA256 |
| --- | --- |
| `storylines/nocticula_continuation.py` | `81526DA3BCF6CD672E4F956B4F0BA84098C8E9BD787BD9AFBA6193728ED9DE02` |
| Final assembled `development/Story.json` | `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC` |
| `expansion.py` | `48E667227C04AF65690B8C4880EA8485C81FC4B26D13E73BBFEF34A75937FD85` |
| `tests/Program.cs` | `E1BF9CAFF4CD8806D5C8827422AA556B00C01713B5FEE7D1CBC34BAD973AAC70` |
| `tests/NocticulaContinuationTests.cs` | `3308F608E0D3E8D279B12E050A8A32A7100D6AAE5BD3FF5404CBF646A710EAD2` |
| `src/Main.cs` | `1A09266238C0ED3914202F8DCFE3B89CB490A5DF50B6D4051EA2FF9053C03B4D` |
| `src/Story.cs` | `F70AFD9652D2660E7F33AB9A451F501980958616C5351E9BEBEB3103220AC56C` |
| Candidate and staged general portrait | `D82D234E6E60DCAA614A06C320001E0FE22A54330FBA185604AA6DCDEF5BD5C5` |

The installed parent is Relations and Romances 0.1.11, DLL SHA256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Parent evidence includes the previously pinned `nocticula-audit-8d261252` sources and a fresh selective decompile of `Epilogue.Setup.EpSetup` from that installed DLL.
Independent comparison exports, native records, decompile, and the focused harness are retained under `C:/Users/Z/AppData/Local/Temp/nocticula-final-independent/`.

## Manuscript and export delta

I imported the frozen 74E0 source previously read in full and compared its assembled scene objects against B259 and then the final 8152 source.
B259 changed exactly 128 Portrait values and two Text values.
The two text changes remove the optional Orren-description attribution in `lamp_measure/start` and identify the drawer in `another_place/refused_dance`.
The final 8152 change removes one trailing space before a newline in `second_door/rescue`.
It does not change the wording or scene behavior.
No other scene metadata, choice position, condition, flag, target, parent binding, or relationship declaration changed.
The earlier ordinary-manuscript literary verdict therefore applies to this final text with these verified precision edits.

`expansion.py` imports the module once, calls its binding/relationship integration once, and extends Scenes once with a deep copy.
My independent assembly contains 612 distinct scene IDs, exactly 24 of them Nocticula scenes.
Those 24 equal the module's SCENES values.
The assembled scenes, node lists, nodes, observed-cue lists, and relationship record are separate objects from the imported module values.
The independently serialized final assembly matches the shared final export hash above exactly.
This check does not imply that calling the entire expansion builder twice on the same payload is supported or required.

Every Nocticula node now explicitly requests `Portrait="Nocticula"`, including the Narrator and ending nodes.
Main's BookEvent page patch checks this explicit key before the Narrator fallback to Together.
The staged file at `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/Nocticula.png` is byte-identical to the reviewed v3 candidate.
The key matches Main's existing Scenes lookup convention.
This is a general identity portrait, not an illustration of every described outfit, gesture, dream location, or historical moment.
The death and Aeon recollections do not become current living appearances merely because her portrait accompanies them.
No new image generation, crop approval, live texture load, or installation was performed here.

## Dedicated suite and actual focused execution

Program invokes NocticulaContinuationTests before the generic route walker, then adds all 24 Nocticula scene IDs to the covered set.
The dedicated suite explicitly expects sixteen visits and eight endings, so excluding those scenes from the generic synthetic-entry walker does not silently omit the endings.
It plays the visits from 32 declared parent-history fixtures, explores direct and check targets, tracks all visit nodes and available choices, and retains played witnesses for the three final decisions.
It checks required intervals, prerequisite removal, death and path blockers, area/chapter restrictions, contact loss, postponement, and preservation of native and existing relationship flags.
The final ending checks cover all sixteen combinations of death, inhuman, ascended, and sacrifice state for each final decision, plus the separate Aeon owner.

I built an isolated focused harness using the actual current Story.cs, dedicated suite, and the repository's Copy/Walk implementation.
It loads and validates the exact independently assembled final export and runs the dedicated suite.
Result: exit zero, 760,338 assertions.
The total includes the copied Walk helper's own assertions and is not directly comparable to a different launcher that counts only the callback assertions.
An intermediate harness rebuild accidentally included the retained decompile through the SDK's default source glob; an explicit three-file compile list corrected that temporary harness error before the successful final run.
No shared build output was used or overwritten by this run.

These are actual pure Rules checks, not a traversal of the parent's acquisition, real skill-roll RNG, native dialog selection, or Unity save loading.
The optional history fixtures include combinations that establish branch coverage without proving every combination attainable in a native campaign.
Root's separate managed Main.Build results are useful additional evidence but were not executed by this reviewer and do not establish a live ending session.

## Default installed ending coexistence

Main gets parent BlueprintCueSequence `ed4baeaf69394754902344f0598d7e5a`, RanRomAdd, and native BlueprintCueSequence `ced82f299d246f448b48afa0b630dd70`, CueSequence_AeonFinalWorld.
It appends each addon ordinary ending's first page to RanRomAdd and each Aeon ending's first page to the native Aeon sequence.
It does not replace any Nocticula parent page, condition, action, text, or localization key.
The addon parent-ending replacement metadata is for the separately reviewed Minagho/Chivarro work, not Nocticula.

Fresh parent source confirms the existing ordinary Nocticula order in RanRomAdd: Slide0001, Slide0003, Slide0002, Slide0004.
Their page GUIDs are respectively `e242ee7eee34426688c6ae80c64b3bb7`, `4e630f20b32d4c05bc86ca79c8ae7c15`, `bafc1b22afed4f058f3353b0e89dee77`, and `c38e993874914cb4907dcf8c0822cc83`.
NoctEpil assigns each page an OnShow action marking all four parent pages seen.
All four are ShowOnce pages, and their existing native redemption, ascension, mythic, sacrifice, and active-relationship conditions remain untouched.
Those actions do not name the newly generated addon pages.
The addon recollections describe the earlier undertaking rather than guaranteeing a contradictory continuing romance after the parent's final outcome.

The parent Aeon cue `21d688a2c41f448e98a2932cb10c1bbc` is added to native page `8f5dbea30be280a4f8a5c30a96e0ddd6` and requires the active parent relationship.
I independently extracted that page and its actual containing Aeon sequence from the native archive; the page is the third member of the native sequence.
The addon recollection is appended later in that sequence and does not remove the cue.
The installed localization has Nocticula remembering an unnamed person who ruined her plans in the rewritten history.
The addon says the harbor meetings did not occur in the remade world; it does not explicitly erase her memory of the former world.
This reading permits coexistence, but future prose must not turn it into an amnesia claim.
Actual final initialized sequence order and rendered coexistence remain runtime verification boundaries.

## Open conditional Expanded Epilogue delivery

RanRomInt is a parent-created BlueprintCueSequence, GUID `2b9424b1b93e4d0896b0958db79d2339`.
The installed parent creates it only inside `Harmony.HasAnyPatches("RanEpilogue")` in EpSetup.Configure.
It contains the same four existing Nocticula page references in the same order as RanRomAdd.
Its own exit is parent-created RanRomIntExit, `b0665c9fa44f4fe7b30f2b95b0d22b44`.
The parent modifies sequence exit `607351955e174bd8b3d61ba9a4df9b6c` to try RanRomInt first, followed by its existing conditional continuation targets.
The ordinary path independently modifies native SequenceExit_0306, `d649f17a42a8e0c418bb336ced272934`, to try RanRomAdd first.
I extracted the latter exit from the native archive.
The former 607351 target is absent from all installed World/Dialogs archive records; its full creation and caller graph were not available in this installation.

No Mods Info.json in the inspected installed Mods tree identifies RanEpilogue.
There is consequently no installed Expanded Epilogue version or initialized conditional graph to pin or execute in this review.
The parent declares RanEpilogue in LoadAfter, but that declaration is not proof that it is installed or that its Harmony condition is true.
The source proves two potential entry setups, not whether a particular Expanded Epilogue version visits one or both in a final session.

Main does not append the new Nocticula recollections to RanRomInt.
Delivery through that conditional route is therefore an open implementation and verification requirement, separate from the default installed append.
It must not be waived by claiming the ordinary sequence test covers it.
Blindly appending the same addon pages to both sequences is not yet proved safe: the shared parent pages have ShowOnce/seen protections, while the addon pages currently have neither equivalent native ShowOnce configuration nor a real saved completion action.
The next work should first reproduce the two-entry setup and seen-state behavior with actual native types, then prove mutually exclusive delivery or implement an appropriate once-only guard before attaching to both.

## Completion-test claim corrected; native persistence still open

Program.Walk adds the terminal scene ID and completion time when it finishes any non-aborted scene, including these recollections.
Actual Main intentionally creates the plain ending Continue answer with empty OnSelect actions.
The managed blueprint checks explicitly assert that empty action list, and Main does not set the ending page's ShowOnce property.
Therefore the dedicated suite's original assertion wording, "Completed Nocticula recollection repeats", overstated what that probe could establish.
It tested Rules against a synthetic completion marker, not the marker's production creation or native replay behavior.

Root corrected the final suite with an explicit two-line comment and the failure message "Nocticula recollection ignores a simulated completion flag".
I inspected that exact comment/message-only delta and reran the final focused suite.
No production behavior changed.
Reports must describe this as synthetic completion policy, not proof of once-only native display, completion persistence, or save/reload.
The next managed reproduction should call the generated native ending answer and observe real saved flags/seen state before changing production code.
It should also verify parent OnShow effects run once and that sharing a page across conditional sequences cannot replay it or suppress it before its first valid display.

The reviewed changes can be retained as a development checkpoint with these requirements open.
No universal Trickster acquisition, resurrection, Gift replacement, living-Shamira resolution, ToyBox runtime concurrence, or manual-play readiness is granted by this integration review.
