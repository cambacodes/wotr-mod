# Milestone system coverage

These are authored test scenarios, not additions to the campaign. Run them only after the
coordinator integrates the matching export and builds RRT. Do not use fixture results as evidence
that a campaign paid a bargain, returned a woman, or earned a commitment.

`harness/system-scenarios.json` is the reviewable inventory. Regenerate it after integration:

```powershell
python tools/harness_system_cases.py --story development/Story.json
```

The manifest selects Ch3 scenarios for a Ch3 source save and later scenarios for a Ch6 source save.
`Chapter` is the scene's test chapter; `SaveChapter` is the source-save chapter. In `-Force` mode,
the probe supplies synthetic prerequisite flags and that test chapter. Area, contact units,
native actors, money, items and checks remain those of the loaded save. A missing contact or wrong
area fails the scenario. Every scenario reloads the original save; save writes are blocked and
the source is loaded again at the end. In fixture mode the disposable world's RRT unlockable
values are synchronized to the fixture, so a previously recorded effect cannot mask the script's
new write. Degradation flags remain real. Fixtures do not change native etudes or bypass checkers.

Without `-Force`, every step uses real saved history, including the real chapter. Ch5 scenes
therefore need a genuine Ch5 save: copy the corresponding cases into a temporary JSON outside
the repository and change their `SaveChapter` to 5. Do not change their prerequisite flags to
make a natural-history test pass. Unavailable required steps fail and remain acceptance debt.

## Save preflight

The local Writer memory names `RRT_*` saves in the game's Saved Games directory. Those saves and
that memory are not mounted in this checkout; no exact filename is invented here. Inspect copies
locally using the Writer probe, then select a Ch3 Drezen free-roam save and a Ch6 free-roam save:

```powershell
$saves = Join-Path $env:USERPROFILE 'AppData\LocalLow\Owlcat Games\Pathfinder Wrath Of The Righteous\Saved Games'
$preflight = Join-Path $env:TEMP 'rrt-save-coverage.json'
python tools/harness_save_coverage.py $saves --probe 'C:\Users\Z\Documents\Projects\Writer\tools\rrt_save_probe.py' --out $preflight
```

Preflight evaluates only initial availability under both contact assumptions. It lists blockers,
not scenes touched. The Writer prototype does not mirror every new runtime predicate, especially
rest allowance and departure epochs; production rules and the live observations are authoritative.
The wrapper copies saves into system temp and removes them when it finishes.

## Scripted milestone runs (coordinator, local PC only)

Use absolute paths to copies selected from preflight. Ch6 household/stance fixtures require
Drezen and the corresponding real contacts; a Threshold save can exercise Last Call directly,
but cannot supply actors in Drezen. Split the cases into temporary manifests by system/venue
when the source saves differ. A completed campaign is unnecessary for synthetic snapshots.

For the two Drezen milestone sources, this selects the actual local names from preflight and
copies them outside the repository. If either source is absent, create that free-roam test save
locally before running the full manifest:

```powershell
$inventory = Get-Content -LiteralPath $preflight -Raw | ConvertFrom-Json
$drezen = '2570015799edf594daf2f076f2f975d8'
$ch3 = $inventory | Where-Object { $_.Chapter -eq 3 -and $_.Area -eq $drezen } | Select-Object -First 1
$ch6 = $inventory | Where-Object { $_.Chapter -eq 6 -and $_.Area -eq $drezen } | Select-Object -First 1
if (!$ch3 -or !$ch6) { throw 'Need RRT_* free-roam saves in Drezen for both Ch3 and Ch6; inspect the preflight inventory.' }
$inputs = Join-Path $env:TEMP ('rrt-milestone-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $inputs | Out-Null
$ch3Copy = Join-Path $inputs $ch3.Save
$ch6Copy = Join-Path $inputs $ch6.Save
Copy-Item -LiteralPath (Join-Path $saves $ch3.Save) -Destination $ch3Copy
Copy-Item -LiteralPath (Join-Path $saves $ch6.Save) -Destination $ch6Copy
```

```powershell
$cases = 'harness/system-scenarios.json'
# Preflight script: no install or launch.
.\harness\run-harness.ps1 -DryRun -SystemCases $cases -Saves $ch3Copy,$ch6Copy -Force -NoRoundTrip
# Explicitly authorized milestone execution, after integration/build and save selection.
.\harness\run-harness.ps1 -Build -SystemCases $cases -Saves $ch3Copy,$ch6Copy -Force -NoRoundTrip -TimeoutMinutes 180
# Repeat with appropriate earned-history saves and a venue/chapter-scoped temporary manifest.
.\harness\run-harness.ps1 -SystemCases $earnedCases -Saves $earnedSaveCopy -NoRoundTrip -TimeoutMinutes 90
# Once all runs have finished/restored and reports have been reviewed:
Remove-Item -LiteralPath $inputs -Recurse -Force
```

Allow approximately 60–150 minutes for the integrated inventory, dominated by save reloads;
budget 180 minutes initially. A small venue/system subset usually takes 5–20 minutes.
These are planning estimates, not measured live timings. Natural campaign preparation is extra.
The harness never silently truncates the script, substitutes the first visible answer, or turns
a missing integration contract into a passing skip.

## Expected inventory

| System | Scripted scope | Evidence |
|---|---|---|
| Table / pair allowance | Seelah–Nenio question selected through the real paged Table | Exact choice identities, completion, spent allowance; exhausted, failed-rest and successful-rest controls call production rules on copies |
| Household pairs | Seelah–Wenduag spar; Delamere–Hepzamirah opening | Separate scripted Table entries and outcomes; no inferred reconciliation |
| W4 | Ch3 supper with Seelah/Nenio/Wenduag; Nenio's knowledge visit | Actual Table slot selection and scene completion |
| W5 | S10 Seelah/Nenio; S20 Jannah's account; S21 Seelah/Yaniel; S29 Seelah/Kiana; S30 Eliandra/Targona | Scripted deed then production Ledger visibility; historical deed supplies no current body |
| Partner stance | Share, exclusive and secret for Anevia, Irabeth, Jerribeth, Kiana, Soana, Minagho/Chivarro, Nocticula, Shamira and Wenduag | 27 distinct effect scripts; refusal/closure remains a valid authored exclusive outcome |
| Last Call | Anevia call-in; final last joke | Unpaid, closed and off-Trickster call-in controls; unresolved debt blocks the last joke; successful effects checked |
| ix-a | Targona/Yaniel, Iomedae/Galfrey, Iomedae/Targona, Iomedae/Yaniel, Yaniel/Galfrey | Nine explicit variants, including queen/crown/Kitrane siblings |
| ix-b | Gesmerha/Soana, Aranka/Arueshalae, Nenio/fallen Arueshalae | Fourteen variants covering clan/bear history, dreamer/fallen, yard and scholar/replacement |

The pair scenario also checks unpaid Shyka page, off-Trickster and closed/dead Seelah; its W5
current Ledger reader checks unreturned Commander sacrifice. Snapshot controls check production availability without executing their
mutations in the live world. Rest controls do not claim a real camp/rest UI was executed.
W5 checks Ledger entry eligibility; rendered Ledger lines, Last Call paragraphs and residence
placement remain live acceptance work. These are covered by the existing book, native epilogue
and presence modes, not certified by a visibility check.

In this base checkout ix-a/ix-b are absent. Their 23 cases intentionally have no fixture contract
and fail until integration and regeneration. The existing source test runs every integrated
script against production `Rules`, including derived-state recomputation between choices.

## Coverage report

Read `Saves[*].Systems` in `rrt-harness-report.json`. Each row records scenario, system, evidence,
result, `AvailabilityChecked`, `ScenesTouched`, `ChoicesTouched`, `LedgerTouched` and findings.
`ScenesTouched` is populated only after the target's real cue appears; checked availability and
Ledger eligibility are separate observations. Failures contribute to the ordinary summary and
exit code 1. An empty applicable inventory, failed reload, missing scene, hidden scripted answer,
early dialog end or unused answer script cannot pass.

Still needed locally: copies of the actual `RRT_*` saves, matching built RRT DLL/export,
integrated ix-a/ix-b, earned Ch5 household/stance history, correct contact venues, successful
real rest/reset, and native finale host/entitlement evidence. Direct Last Call dialogs validate
their runtime conditions/effects; they do not establish that the native finale answer list is
reachable from an arbitrary free-roam save.
