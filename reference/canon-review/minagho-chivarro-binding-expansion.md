# Minagho and Chivarro binding expansion

The expanded manifest is frozen for independent review.
It supplies source evidence for the continuation and its ending metadata; it does not establish initialized parent blueprints or live epilogue behavior.
Only expansion-parent-bindings.json, this report, and isolated extraction artifacts were changed.
No exporter, Main, Story, shared tests, shared reports, generated story, or installed files were edited.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Expanded `expansion-parent-bindings.json`, including topology and core page bindings | `F48810316BB59449D9C430048F324BDF432E45BEB45082E3E7D615C38CFABC92` |
| Initial core-evidence freeze before topology context | `B20B8FB4E90F556B84CF2A2618AF2EED2C1511E55974F7DAF845FB0946FAA12D` |
| Original 29-entry manifest | `834A19DD9EF61156A1104D176548BDDC09C7BC0540B8DFE27899C4D7CD14514A` |
| Installed `RanRomance.dll` | `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68` |
| Installed parent `LocalizedStrings.json` | `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F` |
| Installed `blueprints.zip` | `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5` |
| Installed native `enGB.json` | `3289C3EBAB206BA6312D4C2D512C0B5623E52D7E2B86596074B81D355725AA75` |
| Reviewed continuation contract source | `BD12627BB8F5BA80DAB93746388BC714E34B058AF76D2F65D6D64CFCC6EAF7FF` |
| Current continuation source after portrait assignment | `171AF8D4950B6C97596C0D9636FCA6982AAB2D176DD653022B0DBFBA27C19665` |
| Isolated 585-scene candidate | `C693521614A03C5DD1B75C79C1773183D8A6EE694212963D6F21A916BBC8D85D` |
| Extraction/check script | `DACE1F23252A019FEC8764C0FD8A0AFE58172C5D2B2FE425AFFFF99096F0324D` |
| Supplemental topology/check script | `13C2209BD53CD56971FE384D03059B4B503859A4AD343BD39F6B959CB17A1D71` |
| Core page promotion/check script | `7E3DF2AD9A0DED348D84B377284B783425A560315A680AEDC6B1F9C05316238A` |

The installed hashes were read again during this task.
The DLL and parent localization still match the earlier canon audits.
The native archive and localization pins are included in the supplemental evidence.
The original contract source and current source are pinned separately.
Commit a682631 adds the reviewed ChivarroWarm portrait assignment to `minachiv.the_entrance_she_wants/warm`.
Comparing the current imported scenes with the frozen candidate found exactly one node difference: Portrait changes from an empty string to ChivarroWarm.
All other scene fields, binding maps, ordinary ending edits, and loss rules compared equal.
The earlier candidate/verifier evidence remains tied to its recorded hash; it is not presented as a run against a newer art candidate.

## Coverage and origin

All original 29 manifest entries are preserved in their original order with every field unchanged.
The core Bindings array now has 106 entries: the existing 29 plus 77 new parent-owned targets.
The additions comprise ten etudes, one quest, 58 cues, and eight ending pages.
Twenty additions are the continuation's direct progress witnesses: ten etudes, the completed quest, and nine distinct seen cues.
Another 49 are parent-owned cues targeted by the ordinary ending edits or loss suppression rules, and eight are their directly requested parent ending pages.
Overlapping ordinary and loss targets are recorded once.

The direct continuation and ending metadata together request 83 distinct targets.
Those consist of 77 parent bindings and six native targets.
The supplemental page evidence additionally includes the three parent book pages containing the continuation's nine witnessed cues, for eleven parent pages in total.
All eleven page witnesses remain in MinaghoChivarroEvidence.ParentBookPages with their ordered membership evidence.
Root extended the generic loader to accept BlueprintBookPage and the C# binding enumerator to request ending metadata, so the eight directly requested ending pages are also core bindings.
The three witness-only book pages remain supplemental.

Each new parent binding contains its exact configurator creation excerpt and declaring Configure method.
Local variable declarations are included where a GUID is passed through a variable.
Cue entries also carry the original text key, resolved English-text hash, localization origin, containing page GUID, and zero-based cue index.
The quest's title and description keys were resolved against the installed parent localization.
Page entries contain their creation excerpt and ordered cue references.
These associations were derived from actual New, SetText, and AddToCues calls, not inferred from similar names.

The six native targets were read directly from the installed archive:

| GUID | Native type | Purpose |
| --- | --- | --- |
| `3b8c0801d5e9a694b848ee13564d2ad7` | BlueprintEtude | Minagho death observation |
| `fd2ab9b67ce3e284184b1894c82c6c5d` | BlueprintEtude | Chivarro death observation |
| `71f85264d9064074f9cf74999ecbffa9` | BlueprintEtude | Chivarro searching history |
| `2570015799edf594daf2f076f2f975d8` | BlueprintArea | Drezen scene area |
| `5c95d8e3fa4f3b44896914987cb04b0b` | BlueprintBookPage | Native paired ending |
| `5787f92575364c1459df8f075676c2db` | BlueprintCue | Native paired reunion text |

NativeTargets records their archive paths and actual data separately from parent creation evidence.
No native target was inserted into the parent Bindings array.
The extraction rejects an unresolved target, wrong requested type, or ambiguous native/parent origin.

## Ending details

All 35 ordinary edit ParentKey values match the actual cue source or native record.
Every parent cue targeted by ordinary edits or any of the three loss rules occurs in the recorded parent page's AddToCues list.
The native paired page contains its actual paired cue.
The eight ordinary parent pages are separately identified through their BookPageConfigurator.New calls.
The fresh MinaEpil source records the later shared OnShow assignment that marks competing parent pages seen, as well as the native paired-page condition replacement.
A page's constructor alone is therefore not a complete account of its final parent-initialized behavior.

Parent fallback cue `c47829fba057400c8e0279990be3d25e` and native cue `5787f92575364c1459df8f075676c2db` share original key `056942f6-32d0-4480-8ff7-29356b43db19`.
That key resolves from native localization, and both memberships were checked separately.
The addon metadata supplies separate private alternate keys; this manifest does not replace the shared original entry.
OriginalTextSha256 hashes the resolved original English text as UTF-8, preserving the actual text rather than the authored alternate.

The eight parent ending page constructors use ShowOnce, and the native paired page/cue records have ShowOnce false.
The fresh source includes SlideAeon as separate evidence; it is not included in the ordinary suppression scope.
Native conditions, action ownership, page arbitration, and ShowOnce semantics still have to be preserved by the runtime integration.

## Containing sequence context

The native paired page is a member of native sequence `f8d7f50e3bb88c143834d234c0b24474`, at zero-based Cues index 5.
The current archive record is `World/Dialogs/Epilogues/CueSequence_Special.jbp` and has type BlueprintCueSequence.
The actual Cues list contains `!bp_5c95d8e3fa4f3b44896914987cb04b0b`.
Its full record is stored under SequenceTopology.NativePairedSequence, separate from the original six direct native targets.
This sequence is additional context and does not change the denominator of 83 direct continuation/ending targets.

Freshly decompiled `Epilogue.Setup.EpSetup.Configure` creates parent sequence RanRomAdd at `ed4baeaf69394754902344f0598d7e5a` and adds the eight RanRomMinaSlide0001 through RanRomMinaSlide0008 pages to it.
SequenceTopology.ParentSequence records that creation chain and resolves each named parent page to its separately verified GUID and source-list position.
The native paired page does not belong to that creation chain.
The native sequence's Cues list does not contain the eight parent page GUIDs.
Runtime preflight must validate these different containers instead of assuming that all nine pages are members of RanRomAdd.

The same source also creates RanRomInt at `2b9424b1b93e4d0896b0958db79d2339` inside `Harmony.HasAnyPatches("RanEpilogue")` and adds the same eight parent page objects.
SequenceTopology.ConditionalParentSequence records that conditional declaration without claiming it is active in the current runtime.
These two parent sequence declarations are contextual evidence, not additional core Bindings entries.
Hooks attached to the parent page objects also affect them when reached through this conditional sequence.
The integration author reports addon ending delivery currently appended only to RanRomAdd, so replacement delivery through the conditional RanEpilogue path remains a separate integration question.
This report does not approve that path.

topology.py independently reads the native sequence, checks memberships against fresh EpSetup source, and compares current manuscript data with the earlier candidate.
The script passed all these checks.
The topology addition leaves the eleven parent page witnesses, six direct native records, and 83-target scope unchanged.
The subsequent promotion of eight existing page witnesses into the core array increases that array from 98 to 106 without introducing a new direct target.

## Extraction and checks

The isolated directory is `C:/Users/Z/AppData/Local/Temp/minachiv-binding-expansion-e4c287`.
Its source folder contains fresh selective decompiles from the installed DLL using repository tools/ilspycmd.exe with DOTNET_ROOT set to the existing local runtime.
The manifest records each extracted file's hash.
Main, MinaQuest, the required book/witness classes, MinaEpil, the eight ordinary slides, and SlideAeon were inspected.
Additional adjacent book classes were extracted during witness lookup but add no unrequested core bindings.
The existing 73-cue ending audit was used for orientation; the new manifest is built from the fresh source and current archive rather than copied from that map.

extract.py imports the actual continuation maps/scenes and ordinary/loss metadata.
It parses explicit creation and membership expressions, resolves original localization, reads native records, checks requested types and all ordinary ParentKeys, and asserts exact preservation of the first 29 entries.
original-manifest.json preserves the pre-expansion manifest for comparison.
all-creations.json records the extracted source map for independent inspection.
Rerunning extract.py writes the owned manifest, so an independent reviewer can instead inspect its assertions or redirect that final output when comparing a frozen file.
The final manifest is reconstructed by running extract.py, then topology.py, then promote-pages.py.
The last script copies exactly the eight directly requested parent ending page witnesses into core Bindings, retains all supplemental evidence, and explicitly excludes the native paired page.

The actual C# binding enumerator was compiled in isolated Bindings.csproj with zero warnings/errors.
A temporary copy of verify-game-bindings.py changes only its runner path and report destination.
Its parent_bindings.py is an unchanged copy of the updated repository loader.
The verifier ran against the isolated 585-scene candidate and expanded manifest:

```text
PASS: 1105 binding uses; 139 archive targets and 106 reviewed parent-source targets.
```

The temporary game-bindings-report.json has no failures.
This final run covers the direct continuation and ordinary/loss ending GUID/type requests through the actual updated C# enumerator.
The earlier run reported 1,012 uses, 137 archive targets, and 49 parent-source targets before root added ending metadata enumeration.
The final result closes that earlier coverage gap.
It still does not prove localization keys, page membership, or sequence topology; those have the separate source/archive checks above.

## Tooling limits and next review

The current parent loader checks the installed assembly pin and core binding identity/type/evidence syntax.
It does not consume the supplemental page/native evidence, source hashes, text keys, text hashes, or localization/archive pins.
It now accepts BlueprintBookPage through root's generic loader change.
The current verifier hardcodes the shared rules-runner and report locations; this task redirected them only in its temporary copy.
This agent changed no shared tooling; root owns the loader and C# enumerator changes used by the final run.

Root should independently compare the additions and supplemental evidence before committing the manifest.
Runtime integration must still resolve the actual initialized parent objects, check original localization keys and page membership, retain the original selectors/actions and ownership, and test load/save and playback.
This source-evidence expansion does not substitute for those checks.
