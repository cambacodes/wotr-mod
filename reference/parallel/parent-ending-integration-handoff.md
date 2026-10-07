# Parent ending integration handoff

Status: implementation frozen for independent review, not approved by its author.
No installed files or shared story export were changed.
The existing Konomi production wiring is preserved; Main has four added lines for preparation and attachment.

## Frozen files

| File | SHA256 |
| --- | --- |
| src/ParentEndingIntegration.cs | `EF0E00941C620819166C4D791F00986F2EA7A3A71907440D63F26A2015D733F4` |
| src/Main.cs | `CFF27E813B126B874B1C257224187849D3BFEBB9CEF73D5F971E0224312B2EBA` |
| managed-tests/ParentEndingIntegrationTests.cs | `FD7EA52F11EB4792D29A57E63CCA816555DC098E6DA1444587601DE64060486E` |

The isolated candidate has 585 scenes and SHA256 `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A`.
The final isolated production DLL has SHA256 `88E31533B476ED38C17219D1130196E0D03155DA6538BE7918A4D8B181CC954B`.
The installed parent DLL used for evidence has SHA256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
The installed Assembly-CSharp.dll has SHA256 `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.

## Runtime contract

Prepare verifies the reviewed target GUIDs, original localization keys, exact page membership, timeline, history flags and empty per-cue action/answer/continuation/component graphs before registering variants.
The eight parent pages belong to RanRomAdd `ed4baeaf69394754902344f0598d7e5a`.
The repeatable native pair page `5c95d8e3fa4f3b44896914987cb04b0b` belongs separately to native Special sequence `f8d7f50e3bb88c143834d234c0b24474`.
None may occur in the supplied Aeon sequence.
Cue evidence is pinned to the audited 70 ordinary parent cues plus the native pair cue.

Seventeen private variants are registered before Main's generic owner and OnEnable pass.
They contain empty native behavior until that pass finishes.
Attach then preserves original checker objects, native behavior references, history policies, cue ordering and original localization objects while adding the reviewed alternate families and suppression guards.
It checks all original targets again before mutating them and restores original conditions, cue reference lists and element counts if attachment throws.
Bare registered variant identities and private localization entries can remain after failure, but are not inserted into native pages.
No native flags, seen history or original page actions are run during registration.
The original page OnShow actions remain untouched, including the parent's marking of all eight page GUIDs as seen.

The hook installer validates the actual native PlayBookPage IL and requires exactly one page.OnShow followed by ActionList.Run.
Refresh is injected immediately after that call returns, with original branch labels left on their original target instructions.
Unexpected exception-block boundaries or ambiguous hook shapes reject installation.
CanShowAnyCue takes a preview snapshot, while PlayBookPage takes its snapshot after page actions.
Same-page nested previews reuse the active snapshot.
Postfix and finalizer invalidate their owning scope, and finalizers preserve the original exception.
A null or failed snapshot remains null for the entire batch, including page suppression checks.
The helper never evaluates an approximate native selector; ParentEndingAlternate retains the original checker.

Current loss applicability is delegated to the reviewed typed Story policy, including current native loss evidence, ordinary owner scope, and a currently available or already seen replacement scene.
Cue-only edits and survivor precedence therefore use the same policy as pure Rules tests.
No Commander-only sacrifice is treated here as a woman's death.

If Harmony reports active patches owned by `RanEpilogue`, observation preserves all original parent endings and records an unsupported-topology diagnostic.
EpSetup's optional RanRomInt sequence shares the parent pages, while delivery of addon loss replacements on that sequence has not been verified.
This is an explicit compatibility limitation, not a claim that alternate delivery works.
Existing addon scene registration behavior is unchanged.

## Verification

Both isolated projects build with zero warnings and errors.
The final runner exits zero with 71,672 assertions across the existing managed suite and the new integration checks.
It invokes real Main.Build against the 585-scene candidate and registers 20,701 generated blueprints.
The new checks verify original nested condition owners and checker identities, localization object preservation, 17 variants, original action references, original cue order, idempotence, and actual Harmony registration on native page methods.
Adversarial checks reject changed text keys, missing native Special membership, ordinary pages in Aeon, unexpected per-cue actions and mutations between Prepare and Attach.
They reject missing or duplicate native IL boundaries and preserve existing branch targets.
Production hooks are also applied to a small managed playback fixture which runs an actual native ActionList and then observes selection.
That fixture verifies refresh after actions, stable nested previews, cleanup after success and exception, observation failure fallback, null batch stability and optional RanEpilogue fallback.

The parent condition trees are reconstructed from the extracted source expressions using actual native condition classes and exact GUID references.
The installed merged BlueprintCore builders could not execute under standalone CLR because they access private game fields directly and raise FieldAccessException.
The fixture therefore does not claim execution of parent initialization or its builder methods.
The generated fixture keeps the extracted expressions and nested AND/OR structure visible in SourceConditionFixtures.cs.
It assigns owners before integration and verifies those owners remain unchanged.
The parent MarkCuesSeen graph is reconstructed as an actual native action object and preserved by identity; the controlled timing check uses its own explicit action.

Populated native CanShow, actual DialogController.PlayBookPage, Unity UI rendering, save/load, ToyBox and a live epilogue are not executed by these checks.
Native history and condition evaluation still require an in-game verification pass.
The hook timing fixture proves managed callback placement and lifecycle rather than an end-to-end Unity playthrough.
Runtime preflight checks reject unexpected per-cue actions because generic GUID aliases cannot promise correct self-seen behavior.
External mods adding downstream conditions about an original cue's exact seen GUID remain outside the reviewed source contract.
No broad compatibility or route-completion approval is claimed.

## Reproduction

The isolated workspace is `C:/Users/Z/AppData/Local/Temp/parent-ending-integration-ab9ed0b7`.
It contains Observer.csproj, Runner.csproj, Program.cs, Bootstrap.cs, SourceConditionFixtures.cs, candidate.json and the final run-out.txt/run-error.txt.
Observer compiles the current production source; Runner includes the focused tests and calls fixture preparation before Main.Build.
The temporary runner uses `RRT_PARENT_BINDINGS=C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/expansion-parent-bindings.json` for source-proven parent GUID fixtures.

```powershell
Set-Location 'C:/Users/Z/AppData/Local/Temp/parent-ending-integration-ab9ed0b7'
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' build Observer.csproj -c Release --nologo -v quiet
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' build Runner.csproj -c Release --nologo -v quiet
$env:RRT_PARENT_BINDINGS = 'C:/Users/Z/Documents/Projects/RanRomanceTirabade/reference/canon-review/expansion-parent-bindings.json'
& './bin/Release/net48/Runner.exe' 'D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure' './candidate.json'
```

Evidence is under `C:/Users/Z/AppData/Local/Temp/minachiv-ending-review-d9010692`, especially verified-contract.json, native-paired.json, Slide0001.cs through Slide0008.cs, SlideAeon.cs and MinaEpil.cs.
The exact native Special sequence membership was read from blueprints.zip at World/Dialogs/Epilogues/CueSequence_Special.jbp.
EpSetup's ordinary and conditional sequence construction is also available in reference/EpSetup.cs.
The shared managed test Program has not been edited; its adoption of these source fixtures is a root-owned follow-up after review.
