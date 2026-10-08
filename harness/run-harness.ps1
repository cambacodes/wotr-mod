<#
.SYNOPSIS
  Installs RRT + the RRTTestHarness mod, runs Wrath unattended, collects rrt-harness-report.json,
  restores the Mods folder, and prints a pass/fail summary.

.EXAMPLE
  ./harness/run-harness.ps1 -DryRun -Saves 'Manual_12_Drezen'
  ./harness/run-harness.ps1 -Saves 'Manual_12_Drezen','D:\saves\ch3.zks'
  ./harness/run-harness.ps1 -Saves 'Manual_12_Drezen' -Force -Mode dfs
  ./harness/run-harness.ps1 -Saves 'Manual_12_Drezen' -Force -Screenshots -ScreenshotsPerScene 4 -SceneFilter @('seelah.letter')
  ./harness/run-harness.ps1 -Saves 'D:\saves\ch3.zks' -Force -Inline -Screenshots -SceneFilter @('household.')

  -Inline drives each scene that has a native entry list (Rules.EntryTargets) through its host native dialog, as the player
  reaches it: it starts the host (harness/inline-hosts.json, from harness/resolve-inline-hosts.py), clicks toward the list,
  selects the RRT entry, then walks the scene. A host or list the run cannot reach is reported as skipped-inline, not failed.

  -Screenshots captures a PNG of each shown cue (after the dialog UI has bound it), up to -ScreenshotsPerScene per walk,
  into harness/.runs/<stamp>/shots/<scene-id>__<step>.png; the report lists them per run. A minimized Unity window can
  render black, so -Screenshots launches Wrath in a normal (not minimized) 1280x720 window, as -Windowed does.

  -Spike Residence runs the P2 harem-residence feasibility spike (Writer/handoffs/10b-RESIDENCE-SPIKE.md) instead of
  driving scenes: after each save loads it enters the Council Chamber (area 28a49e11) through Game.LoadArea at
  TricksterCouncil_Enter, records load time, loaded mechanics and native entry actions, spawns one presence copy at a seat
  with RRT's GuestPresence, checks view, rendering (with -Screenshots), a walk and a dialog, then removes it. Nothing is saved.
  ./harness/run-harness.ps1 -Saves 'D:\saves\ch6.zks' -Spike Residence -Screenshots -NoRoundTrip

  -Spike Presence runs the E12d quiet-copy check instead of driving scenes: after each save loads it enters Drezen (unless
  the save is already there), spawns spawn-copy presences of companion and story units (Camelia_Companion,
  EvilArueshalae_Companion, Seelah, Targona) next to the Commander with RRT's GuestPresence, forces their bark triggers
  (Aggro, Pain, LowHealth, Selected, Discovery, CheckFail), watches them for 20 s, and fails on any audible bark, dialog
  start, combat, Player faction, party group or missing Passive flag. It then removes them. Nothing is saved.
  ./harness/run-harness.ps1 -Build -Saves '<copy of a Ch3 Drezen save>' -Spike Presence -NoRoundTrip -TimeoutMinutes 15
  With -PresenceUnits and -PresenceLocator the spike copies those units onto a native locator instead (as an E12b At.Locator
  presence) and also checks the spot: walkable mesh, drift, room for the body; -Screenshots frames each copy. Devarra's Huge
  dragon (engine queue 9d):
  ./harness/run-harness.ps1 -Build -Saves '<copy of a Ch5 Drezen save>' -Spike Presence -PresenceUnits c4b5746d3d2511441ba18a894cecb328 -PresenceLocator d7aa4429-41bd-4d58-bb17-074863d847f7 -Screenshots -NoRoundTrip -TimeoutMinutes 15

  -PresenceProbe "x,y,z" -ProbeRadius N searches the saved area's walkable mesh instead of spawning copies.
  It prints the twenty nearest distinct points within N metres (default 10), also stored in PresenceSpike.Probe.
  Probe mode stays in the saved area and cannot be combined with -PresenceUnits or -PresenceLocator.

  -Probes installs the harness-only probe story (tools/build-harness-probes.py: development/Story.json plus
  storylines/harness_probes.py, e.g. the E-new 0 Prologue probe pacing.e0.probe) and its inline hosts in place of the shipped
  ones. Probes never ship. ./harness/run-harness.ps1 -Saves '<copy of a Prologue save>' -Probes -Inline -SceneFilter @('pacing.e0.')

.NOTES
  Exit codes: 0 all checks passed, 1 tests failed, 2 harness/infrastructure failure (no report, timeout, crash),
  3 bad arguments or failed preflight.
  After a hard kill of this script, restore with:  ./harness/run-harness.ps1 -RestoreFrom harness/.runs/<stamp>
#>
[CmdletBinding()]
param(
    [string]$GameDir = 'C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure',
    [string[]]$Saves = @(),
    [string]$SystemCases,
    [string]$EvidenceRequirements,
    [switch]$Force,
    [switch]$DryRun,
    [ValidateSet('random', 'dfs')][string]$Mode = 'random',
    [int]$Seed = 20,
    [int]$WalksPerScene = 1,
    [int]$MaxPathsPerScene = 8,
    [int]$MaxScenesPerSave = 0,
    [string[]]$SceneFilter = @(),
    [string[]]$SetFlags = @(),
    [string[]]$StartEtudes = @(),
    [string[]]$SetPresenceFailures = @(),
    [string[]]$HoldEtudes = @(),
    [string[]]$SeenCues = @(),
    [string[]]$RemoveCompanions = @(),
    [switch]$NoRoundTrip,
    [switch]$Headless,
    [switch]$Windowed,
    [switch]$FullRes,
    [switch]$BatchMode,
    [switch]$Screenshots,
    [int]$ScreenshotsPerScene = 3,
    [switch]$Inline,
    [int]$MaxInlineNavSteps = 40,
    # BEGIN eng7-f5
    [ValidateSet('Residence', 'Presence', 'NativeEpilogue')][string]$Spike,
    [string]$NativeEpilogueCases,
    # END eng7-f5
    [string[]]$PresenceUnits = @(),
    [string]$PresenceLocator,
    [string]$PresenceKey,
    [string]$PresenceEnterPoint,
    [string]$PresenceProbe,
    [switch]$ProbeEnter,
    [string]$PresenceNearUnit,
    [string]$PresenceSide = 'left',
    [float]$PresenceAnchorDistance = 2.5,
    [float]$ProbeRadius = 10,
    [switch]$Probes,
    [switch]$Build,
    [int]$TimeoutMinutes = 45,
    [string]$UserData = (Join-Path $env:USERPROFILE 'AppData\LocalLow\Owlcat Games\Pathfinder Wrath Of The Righteous'),
    [string]$RestoreFrom
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2

$HarnessDir = $PSScriptRoot
$Repo = Split-Path -Parent $HarnessDir
$ModsDir = Join-Path $GameDir 'Mods'
$UmmParams = Join-Path $GameDir 'Wrath_Data\Managed\UnityModManager\Params.xml'
$SavedGames = Join-Path $UserData 'Saved Games'
$RrtModDir = Join-Path $ModsDir 'RanRomanceTirabade'
$HarnessModDir = Join-Path $ModsDir 'RRTTestHarness'
$PortraitModDir = Join-Path $ModsDir 'CustomNpcPortraits'
$ReportName = 'rrt-harness-report.json'

function Say([string]$Text, [string]$Color = 'Gray') { Write-Host $Text -ForegroundColor $Color }

# ---------------------------------------------------------------------------------------------
# Restore: whole directories (RRT and harness mod folders) and individual files (portraits, UMM Params.xml).
# The manifest is written before anything is touched, so a restore works after any crash.
# ---------------------------------------------------------------------------------------------
function Restore-Run([string]$RunDir) {
    $manifestPath = Join-Path $RunDir 'manifest.json'
    if (!(Test-Path -LiteralPath $manifestPath)) { Say "No manifest in $RunDir; nothing to restore." Yellow; return }
    $m = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    $problems = 0
    foreach ($d in @($m.Dirs)) {
        try {
            if (Test-Path -LiteralPath $d.Target) { Remove-Item -LiteralPath $d.Target -Recurse -Force }
            if ($d.Existed) { Copy-Item -LiteralPath $d.Backup -Destination $d.Target -Recurse -Force }
        } catch { $problems++; Say "  restore failed for $($d.Target): $_" Red }
    }
    foreach ($f in @($m.Files)) {
        try {
            if ($f.Existed) { Copy-Item -LiteralPath $f.Backup -Destination $f.Target -Force }
            elseif (Test-Path -LiteralPath $f.Target) { Remove-Item -LiteralPath $f.Target -Force }
        } catch { $problems++; Say "  restore failed for $($f.Target): $_" Red }
    }
    # Remove directories this run created (deepest first) if they are empty again.
    foreach ($dir in @($m.CreatedDirs | Sort-Object { $_.Length } -Descending)) {
        if ((Test-Path -LiteralPath $dir) -and -not (Get-ChildItem -LiteralPath $dir -Force | Select-Object -First 1)) {
            Remove-Item -LiteralPath $dir -Force
        }
    }
    if ($problems -eq 0) {
        Set-Content -LiteralPath (Join-Path $RunDir 'restored.txt') -Value (Get-Date -Format o) -Encoding utf8
        Say "Mods folder restored from $RunDir" Green
    } else { Say "Restore finished with $problems problem(s); backups remain in $RunDir" Red }
}

if ($RestoreFrom) {
    if (Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue) { Say 'Wrath is running; close it before restoring.' Red; exit 3 }
    Restore-Run (Resolve-Path -LiteralPath $RestoreFrom).Path
    exit 0
}

# ---------------------------------------------------------------------------------------------
# Plan the copy
# ---------------------------------------------------------------------------------------------
$rrtDll = Join-Path $Repo 'src\bin\Release\net48\RanRomance.Tirabade.dll'
$harnessDll = Join-Path $HarnessDir 'bin\Release\net48\RRT.TestHarness.dll'
$dotnet = Join-Path $env:LOCALAPPDATA 'RanRomanceTools\dotnet\dotnet.exe'

if ($Build -or (!(Test-Path -LiteralPath $harnessDll))) {
    if ($DryRun) { Say "[dry-run] would build: $dotnet build $HarnessDir\RRT.TestHarness.csproj -c Release" Cyan }
    else {
        & $dotnet build (Join-Path $HarnessDir 'RRT.TestHarness.csproj') -c Release --nologo -v quiet "-p:GameDir=$GameDir/"
        if ($LASTEXITCODE) { Say 'Harness build failed.' Red; exit 3 }
    }
}

# -Probes (E-new 0): install the harness-only probe story (development/Story.json + storylines/harness_probes.py) and its
# inline hosts instead of the shipped ones, for this run only. Both are built into harness/probes/ (gitignored); the
# shipped story never contains a probe, and the Mods folder is restored after the run as usual.
$storySource = Join-Path $Repo 'development\Story.json'
$inlineHosts = Join-Path $HarnessDir 'inline-hosts.json'
if ($Probes) {
    $probeDir = Join-Path $HarnessDir 'probes'
    Say 'Building the harness-only probe story (harness/probes/, never shipped)...' Cyan
    & (Get-Command python -ErrorAction Stop).Source (Join-Path $Repo 'tools/build-harness-probes.py') --hosts --game $GameDir
    if ($LASTEXITCODE) { Say 'Probe story build failed.' Red; exit 3 }
    $storySource = Join-Path $probeDir 'Story.json'
    $inlineHosts = Join-Path $probeDir 'inline-hosts.json'
}

$copies = [Collections.Generic.List[object]]::new()
function Add-Copy([string]$Source, [string]$Target, [bool]$Optional = $false) {
    $copies.Add([PSCustomObject]@{ Source = $Source; Target = $Target; Optional = $Optional })
}
Add-Copy (Join-Path $Repo 'package\Info.json') (Join-Path $RrtModDir 'Info.json')
Add-Copy $rrtDll (Join-Path $RrtModDir 'RanRomance.Tirabade.dll')
Add-Copy $storySource (Join-Path $RrtModDir 'Story.json')
foreach ($name in @('Tirabade.Narrator.exe', 'Tirabade.Narrator.exe.config')) {
    Add-Copy (Join-Path $Repo "package\$name") (Join-Path $RrtModDir $name) $true
}
$pkgPortraits = Join-Path $Repo 'package\Portraits'
if (Test-Path -LiteralPath $pkgPortraits) {
    foreach ($f in Get-ChildItem -LiteralPath $pkgPortraits -File -Recurse) {
        Add-Copy $f.FullName (Join-Path (Join-Path $RrtModDir 'Portraits') $f.FullName.Substring($pkgPortraits.Length + 1))
    }
}
$artPortraits = Join-Path $Repo 'art\CustomNpcPortraits'
$portraitFiles = @()
if (Test-Path -LiteralPath $artPortraits) {
    foreach ($f in Get-ChildItem -LiteralPath $artPortraits -File -Recurse) {
        $t = Join-Path $PortraitModDir $f.FullName.Substring($artPortraits.Length + 1)
        Add-Copy $f.FullName $t
        $portraitFiles += $t
    }
}
Add-Copy $harnessDll (Join-Path $HarnessModDir 'RRT.TestHarness.dll')
Add-Copy (Join-Path $HarnessDir 'Info.json') (Join-Path $HarnessModDir 'Info.json')
Add-Copy $inlineHosts (Join-Path $HarnessModDir 'inline-hosts.json') (-not $Inline)

# ---------------------------------------------------------------------------------------------
# Saves and plan
# ---------------------------------------------------------------------------------------------
$resolvedSaves = @()
foreach ($s in $Saves) {
    if ([IO.Path]::IsPathRooted($s)) { $p = $s } else {
        $n = $s; if ($n -notlike '*.zks') { $n = "$n.zks" }
        $p = Join-Path $SavedGames $n
    }
    $resolvedSaves += [IO.Path]::GetFullPath($p)
}
if ($resolvedSaves.Count -eq 0 -and (Test-Path -LiteralPath $SavedGames)) {
    $newest = Get-ChildItem -LiteralPath $SavedGames -Filter '*.zks' -File |
        Where-Object { $_.Name -notlike '*RRTHarness*' } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($newest) { $resolvedSaves = @($newest.FullName); Say "No -Saves given; using the newest save: $($newest.Name)" Yellow }
}

$plan = [ordered]@{
    saves             = @($resolvedSaves)
    force             = [bool]$Force
    mode              = $Mode
    seed              = $Seed
    walksPerScene     = $WalksPerScene
    maxPathsPerScene  = $MaxPathsPerScene
    maxScenesPerSave  = $MaxScenesPerSave
    sceneFilter       = @($SceneFilter)
    roundTrip         = -not $NoRoundTrip
    headless          = [bool]$Headless
    screenshots       = [bool]$Screenshots
    screenshotsPerScene = $ScreenshotsPerScene
    inline            = [bool]$Inline
    maxInlineNavSteps = $MaxInlineNavSteps
    quitWhenDone      = $true
    timeouts          = [ordered]@{ globalSeconds = [Math]::Max(60, $TimeoutMinutes * 60 - 60) }
}
# BEGIN eng7-f5: JSON is embedded, so no extra mod-folder installation or shared runtime hook is needed.
if ($SystemCases) {
    if (!$NoRoundTrip -or $Inline -or $Spike -or $SceneFilter.Count -gt 0 -or $SetFlags.Count -gt 0 -or $StartEtudes.Count -gt 0 -or $SetPresenceFailures.Count -gt 0 -or $HoldEtudes.Count -gt 0 -or $SeenCues.Count -gt 0 -or $RemoveCompanions.Count -gt 0) {
        throw '-SystemCases requires -NoRoundTrip and no Inline, Spike, SceneFilter or global fixture setup.'
    }
    $plan.systemCasesJson = Get-Content -LiteralPath $SystemCases -Raw
}
if ($Spike -eq 'NativeEpilogue') {
    if (!$NoRoundTrip -or $Inline -or $Headless) { throw '-Spike NativeEpilogue requires -NoRoundTrip, visible dialogs and no -Inline.' }
    if ($resolvedSaves.Count -eq 0) { throw '-Spike NativeEpilogue requires a loadable free-roam save.' }
    if (!$NativeEpilogueCases) { $NativeEpilogueCases = Join-Path $Repo 'tests/native-cue-policy-fixtures/states.json' }
    $plan.nativeEpilogueCasesJson = Get-Content -LiteralPath $NativeEpilogueCases -Raw
    $plan.maxStepsPerWalk = 1000
} elseif ($NativeEpilogueCases) { throw '-NativeEpilogueCases requires -Spike NativeEpilogue.' }
# END eng7-f5
# Opt-in only: without -Spike the plan (and so the run) is exactly as before.
if ($Spike) { $plan.spike = $Spike.ToLowerInvariant() }
if (($PresenceUnits.Count -gt 0 -or $PresenceLocator -or $PSBoundParameters.ContainsKey('PresenceProbe') -or $PSBoundParameters.ContainsKey('ProbeRadius')) -and $Spike -ne 'Presence') {
    throw '-PresenceUnits, -PresenceLocator, -PresenceProbe and -ProbeRadius need -Spike Presence.'
}
if ($PSBoundParameters.ContainsKey('ProbeRadius') -and !$PSBoundParameters.ContainsKey('PresenceProbe')) { throw '-ProbeRadius needs -PresenceProbe.' }
if ($PSBoundParameters.ContainsKey('PresenceProbe')) {
    if ($PresenceLocator -or $PresenceUnits.Count -gt 0) { throw '-PresenceProbe cannot be combined with -PresenceLocator or -PresenceUnits.' }
    $coordinates = @($PresenceProbe.Split(','))
    if ($coordinates.Count -ne 3) { throw '-PresenceProbe needs three finite coordinates: x,y,z.' }
    foreach ($coordinate in $coordinates) {
        $value = [float]0
        if (![float]::TryParse($coordinate, [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::InvariantCulture, [ref]$value) -or [float]::IsNaN($value) -or [float]::IsInfinity($value)) {
            throw '-PresenceProbe needs three finite coordinates: x,y,z.'
        }
    }
    if ($ProbeRadius -le 0 -or [float]::IsNaN($ProbeRadius) -or [float]::IsInfinity($ProbeRadius)) { throw '-ProbeRadius must be finite and greater than zero.' }
}
if ($PresenceKey -and $Spike -ne 'Presence') { throw '-PresenceKey needs -Spike Presence.' }
if ($PresenceKey -and ($PresenceUnits.Count -gt 0 -or $PresenceLocator -or $PresenceNearUnit -or $PresenceProbe)) { throw '-PresenceKey tests the production placement; copy/probe overrides cannot be combined with it.' }
if ($PSBoundParameters.ContainsKey('PresenceEnterPoint') -and $Spike -ne 'Presence') { throw '-PresenceEnterPoint needs -Spike Presence.' }
if ($Spike -eq 'Presence' -and ($PSBoundParameters.ContainsKey('PresenceEnterPoint') -or $PresenceKey -or $PresenceUnits.Count -gt 0 -or $PresenceLocator -or $PresenceNearUnit -or $PSBoundParameters.ContainsKey('PresenceProbe'))) {
    $presence = [ordered]@{}
    if ($PresenceKey) { $presence.key = $PresenceKey }
    if ($PSBoundParameters.ContainsKey('PresenceEnterPoint')) { $presence.enterPoint = $PresenceEnterPoint }
    if ($PresenceUnits.Count -gt 0) { $presence.units = @($PresenceUnits) }
    if ($PresenceLocator) { $presence.locator = $PresenceLocator }
    if ($PresenceNearUnit) { $presence.nearUnit = $PresenceNearUnit; $presence.side = $PresenceSide; $presence.anchorDistance = $PresenceAnchorDistance }
    if ($PSBoundParameters.ContainsKey('PresenceProbe')) { $presence.probe = $PresenceProbe; $presence.probeRadius = $ProbeRadius; if ($ProbeEnter) { $presence.probeEnter = $true } }
    $plan.presence = $presence
}
# Fixture setup is harness-only, applied after each source-save load.
$plan.setFlags = @($SetFlags | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$plan.setPresenceFailures = @($SetPresenceFailures | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$plan.holdEtudes = @($HoldEtudes | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$plan.seenCues = @($SeenCues | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$plan.removeCompanions = @($RemoveCompanions | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$plan.startEtudes = @($StartEtudes | ForEach-Object { $_.Split(',') } | ForEach-Object { $_.Trim() } | Where-Object { $_ } | Select-Object -Unique)
$planJson = $plan | ConvertTo-Json -Depth 5

$launchArgs = @()
if ($Windowed -or $Screenshots) { $launchArgs = @('-screen-fullscreen', '0', '-screen-width', '1280', '-screen-height', '720') }
# Lean by default: without screenshots nothing needs a real frame, so a small windowed game saves GPU/RAM.
elseif (-not $FullRes) { $launchArgs = @('-screen-fullscreen', '0', '-screen-width', '800', '-screen-height', '600') }
# Experimental: Unity batch mode without a graphics device. WotR's dialog UI and save loading may not survive it.
if ($BatchMode) {
    if ($Screenshots) { throw '-BatchMode cannot take screenshots (no graphics device).' }
    $launchArgs = @('-batchmode', '-nographics')
}
# Screenshots need a rendered (not minimized) window.
$windowStyle = if ($Screenshots) { 'Normal' } else { 'Minimized' }
$exe = Join-Path $GameDir 'Wrath.exe'

# ---------------------------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------------------------
$pre = @()
if (!(Test-Path -LiteralPath $exe)) { $pre += "Wrath.exe not found in $GameDir" }
if (!(Test-Path -LiteralPath (Join-Path $GameDir 'Wrath_Data\Managed\UnityModManager\UnityModManager.dll'))) { $pre += 'UnityModManager is not installed into the game.' }
if (!(Test-Path -LiteralPath (Join-Path $ModsDir 'RanRomance\RanRomance.dll'))) { $pre += 'Parent mod RanRomance is not installed (RRT requires it).' }
if (!(Test-Path -LiteralPath (Join-Path $PortraitModDir 'Info.json'))) { $pre += 'CustomNpcPortraits is not installed (RRT requires it).' }
foreach ($c in $copies) { if (!$c.Optional -and !(Test-Path -LiteralPath $c.Source)) { $pre += "Missing source: $($c.Source)" } }
foreach ($s in $resolvedSaves) { if (!(Test-Path -LiteralPath $s)) { $pre += "Save not found: $s" } }
if ($resolvedSaves.Count -eq 0) { $pre += 'No saves: pass -Saves <name or path>.' }
if (Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue) { $pre += 'Wrath is already running; close it first.' }
if ($Inline -and !(Test-Path -LiteralPath $inlineHosts)) { $pre += 'No harness/inline-hosts.json: run  python harness/resolve-inline-hosts.py' }
if ($EvidenceRequirements -and !(Test-Path -LiteralPath $EvidenceRequirements)) { $pre += 'Evidence requirements file is missing.' }

if ($DryRun) {
    Say '=== RRT harness dry run: nothing is copied, launched or modified ===' Cyan
    Say "Game:        $GameDir"
    Say "Saved games: $SavedGames"
    Say ''
    Say 'Would back up (whole folder, restored afterwards):' Cyan
    foreach ($d in @($RrtModDir, $HarnessModDir)) {
        if (Test-Path -LiteralPath $d) { $state = 'exists, backed up' } else { $state = 'absent, removed afterwards' }
        Say "  $d  [$state]"
    }
    if (Test-Path -LiteralPath $UmmParams) { $state = 'exists, backed up' } else { $state = 'absent' }
    Say "  $UmmParams  [$state]"
    Say ''
    Say 'Would copy:' Cyan
    foreach ($c in $copies) {
        $src = 'ok'
        if (!(Test-Path -LiteralPath $c.Source)) { if ($c.Optional) { $src = 'MISSING, optional, skipped' } else { $src = 'MISSING' } }
        if (Test-Path -LiteralPath $c.Target) { $tgt = 'overwrite' } else { $tgt = 'new' }
        Say ("  {0}`n     -> {1}  [{2}; source {3}]" -f $c.Source, $c.Target, $tgt, $src)
    }
    Say ''
    Say "Would write plan: $(Join-Path $HarnessModDir 'rrt-harness-plan.json')" Cyan
    Say $planJson
    Say ''
    if ($Inline -and (Test-Path -LiteralPath $inlineHosts)) {
        # The offline resolution each matching scene would be driven through (the run re-checks the live entry lists).
        $h = Get-Content -LiteralPath $inlineHosts -Raw | ConvertFrom-Json
        $ids = @($h.scenes.PSObject.Properties | Where-Object {
            $id = $_.Name; ($SceneFilter.Count -eq 0) -or @($SceneFilter | Where-Object { $id -eq $_ -or $id.StartsWith($_) }).Count -gt 0 })
        $ok = @($ids | Where-Object { $_.Value.resolved }).Count
        Say ''
        Say ("Inline hosts ({0}): {1}/{2} matching scenes resolve to a host dialog" -f (Split-Path -Leaf $inlineHosts), $ok, $ids.Count) Cyan
        foreach ($p in $ids | Select-Object -First 40) {
            $s = $p.Value
            if ($s.resolved) { Say ("  {0} [{1}] -> {2} / {3} ({4} click(s)); entry {5}" -f $p.Name, $s.kind, $s.host.dialogName, $s.host.cue, $s.host.clicks, $s.entry.($s.host.list)) }
            else { Say ("  {0} [{1}] unresolved: {2}" -f $p.Name, $s.kind, $s.reason) Yellow }
        }
        if ($ids.Count -gt 40) { Say "  ... $($ids.Count - 40) more" }
        Say ''
    }
    Say ("Would launch: `"{0}`" {1}  (window style {3}; timeout {2} min)" -f $exe, ($launchArgs -join ' '), $TimeoutMinutes, $windowStyle) Cyan
    Say "Would wait for: $(Join-Path $HarnessModDir $ReportName)"
    Say "Would archive report and logs under: $(Join-Path $HarnessDir '.runs\<stamp>')"
    if ($pre.Count) { Say ''; Say 'Preflight problems (a live run would stop here):' Yellow; $pre | ForEach-Object { Say "  - $_" Yellow } }
    else { Say ''; Say 'Preflight: OK' Green }
    exit 0
}

if ($pre.Count) { Say 'Preflight failed:' Red; $pre | ForEach-Object { Say "  - $_" Red }; exit 3 }

# ---------------------------------------------------------------------------------------------
# Install (with manifest), run, restore
# ---------------------------------------------------------------------------------------------
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$RunDir = Join-Path $HarnessDir ".runs\$stamp"
if ($EvidenceRequirements) {
    Push-Location $Repo
    try {
        $evidenceSourceHash = & (Get-Command python -ErrorAction Stop).Source -c 'from pathlib import Path; from tools.gate_receipts import source_hash; print(source_hash(Path.cwd()))'
        if ($LASTEXITCODE) { throw 'Evidence source hashing failed' }
        $evidenceExportHash = (Get-FileHash -LiteralPath $storySource -Algorithm SHA256).Hash.ToLowerInvariant()
    } finally { Pop-Location }
}
New-Item -ItemType Directory -Force -Path (Join-Path $RunDir 'backup') | Out-Null
if ($Screenshots) {
    $plan.screenshotDir = Join-Path $RunDir 'shots'
    New-Item -ItemType Directory -Force -Path $plan.screenshotDir | Out-Null
    $planJson = $plan | ConvertTo-Json -Depth 5
}
$manifest = [ordered]@{ GameDir = $GameDir; Dirs = @(); Files = @(); CreatedDirs = @() }
function Save-Manifest { $manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $RunDir 'manifest.json') -Encoding utf8 }

$exitCode = 2
$startTime = Get-Date
try {
    # 1. Record and back up everything before the first write.
    $i = 0
    foreach ($d in @($RrtModDir, $HarnessModDir)) {
        $b = Join-Path $RunDir ("backup\dir{0}-{1}" -f $i, (Split-Path -Leaf $d)); $i++
        $existed = Test-Path -LiteralPath $d
        if ($existed) { Copy-Item -LiteralPath $d -Destination $b -Recurse -Force }
        $manifest.Dirs += [ordered]@{ Target = $d; Backup = $b; Existed = $existed }
    }
    foreach ($t in @($portraitFiles) + @($UmmParams)) {
        $b = Join-Path $RunDir ("backup\file{0}-{1}" -f $i, (Split-Path -Leaf $t)); $i++
        $existed = Test-Path -LiteralPath $t
        if ($existed) { Copy-Item -LiteralPath $t -Destination $b -Force }
        $manifest.Files += [ordered]@{ Target = $t; Backup = $b; Existed = $existed }
    }
    Save-Manifest

    # 2. Copy.
    foreach ($c in $copies) {
        if (!(Test-Path -LiteralPath $c.Source)) { continue }
        $dir = Split-Path -Parent $c.Target
        $missing = @(); $probe = $dir
        while ($probe -and !(Test-Path -LiteralPath $probe)) { $missing += $probe; $probe = Split-Path -Parent $probe }
        if ($missing.Count) { $manifest.CreatedDirs += $missing; Save-Manifest; New-Item -ItemType Directory -Force -Path $dir | Out-Null }
        Copy-Item -LiteralPath $c.Source -Destination $c.Target -Force
    }
    $reportPath = Join-Path $HarnessModDir $ReportName
    if (Test-Path -LiteralPath $reportPath) { Remove-Item -LiteralPath $reportPath -Force }
    [IO.File]::WriteAllText((Join-Path $HarnessModDir 'rrt-harness-plan.json'), $planJson, [Text.UTF8Encoding]::new($false))
    Say "Installed $($copies.Count) files; backup and manifest in $RunDir" Green

    # 3. Launch and wait.
    Say "Launching Wrath ($($windowStyle.ToLower())). Timeout: $TimeoutMinutes min." Cyan
    if ($launchArgs.Count) { Start-Process -FilePath $exe -ArgumentList $launchArgs -WorkingDirectory $GameDir -WindowStyle $windowStyle | Out-Null }
    else { Start-Process -FilePath $exe -WorkingDirectory $GameDir -WindowStyle $windowStyle | Out-Null }
    $deadline = $startTime.AddMinutes($TimeoutMinutes)
    $status = $null; $sawGame = $false; $lastNote = ''
    while ((Get-Date) -lt $deadline) {
        Start-Sleep -Seconds 5
        $running = @(Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue).Count -gt 0
        if ($running) { $sawGame = $true }
        if (Test-Path -LiteralPath $reportPath) {
            $r = $null
            try { $r = Get-Content -LiteralPath $reportPath -Raw | ConvertFrom-Json; $status = $r.Status } catch { $status = $null }
            if ($r) {
                $note = "harness: $status, saves $(@($r.Saves).Count)/$($resolvedSaves.Count), elapsed $($r.ElapsedSeconds)s"
                if ($note -ne $lastNote) { Say "  $note"; $lastNote = $note }
            }
            if ($status -eq 'complete' -or $status -eq 'aborted') { break }
        }
        if ($sawGame -and !$running) { Say '  Wrath exited before the harness finished.' Red; break }
        if (!$sawGame -and ((Get-Date) - $startTime).TotalMinutes -gt 3) { Say '  Wrath never started (Steam launch failure?).' Red; break }
    }
    # 4. Let Application.Quit finish, then make sure the game is gone before restoring files.
    $quitBy = (Get-Date).AddSeconds(90)
    while ((Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue) -and (Get-Date) -lt $quitBy) { Start-Sleep -Seconds 2 }
    if (Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue) {
        Say '  Wrath still running; stopping it.' Yellow
        Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue | Stop-Process -Force
        Start-Sleep -Seconds 3
    }

    # 5. Archive report and logs.
    if (Test-Path -LiteralPath $reportPath) { Copy-Item -LiteralPath $reportPath -Destination (Join-Path $RunDir $ReportName) -Force }
    foreach ($log in @((Join-Path $UserData 'Player.log'), (Join-Path $UserData 'GameLogFull.txt'), (Join-Path $GameDir 'Wrath_Data\Managed\UnityModManager\Log.txt'))) {
        if (Test-Path -LiteralPath $log) { Copy-Item -LiteralPath $log -Destination $RunDir -Force -ErrorAction SilentlyContinue }
    }
    # Round-trip saves are deleted by the harness; remove any leftovers from this run only.
    if (Test-Path -LiteralPath $SavedGames) {
        Get-ChildItem -LiteralPath $SavedGames -Filter '*RRTHarness_roundtrip*.zks' -File |
            Where-Object { $_.LastWriteTime -ge $startTime } | ForEach-Object { Say "  removing leftover round-trip save $($_.Name)" Yellow; Remove-Item -LiteralPath $_.FullName -Force }
    }

    # 6. Summary.
    $archived = Join-Path $RunDir $ReportName
    if (!(Test-Path -LiteralPath $archived)) {
        Say 'FAIL (infrastructure): no report was produced. Check UMM Log.txt / Player.log in the run folder.' Red
        $exitCode = 2
    } else {
        $r = Get-Content -LiteralPath $archived -Raw | ConvertFrom-Json
        $s = $r.Summary
        Say ''
        Say '=== RRT harness summary ===' Cyan
        Say ("Status: {0}{1}   elapsed {2}s" -f $r.Status, $(if ($r.AbortReason) { " ($($r.AbortReason))" } else { '' }), $r.ElapsedSeconds)
        Say ("RRT init: initialized={0} error={1} degraded=[{2}] warnings={3}" -f $r.Init.Initialized, $r.Init.Error, (@($r.Init.Degraded) -join ', '), @($r.Init.Warnings).Count)
        foreach ($sv in @($r.Saves)) {
            Say ("  {0}: load={1} ({2:N0} ms) available={3} driven={4} choices={5} roundtrip={6}" -f (Split-Path -Leaf $sv.Save), $sv.LoadOk, $sv.LoadMs,
                @($sv.AvailableScenes).Count, $sv.ScenesDriven, $sv.ChoicesTaken, $(if ($sv.RoundTrip.Attempted) { $sv.RoundTrip.Passed } else { "skipped: $($sv.RoundTrip.SkipReason)" }))
            # BEGIN eng7-f5
            if ($sv.PSObject.Properties['NativeSlides'] -and @($sv.NativeSlides).Count) {
                $slides = @($sv.NativeSlides)
                $passedSlides = @($slides | Where-Object { $_.Passed }).Count
                $forcedSlides = @($slides | Where-Object { $_.Forced }).Count
                Say ("    native slides: {0}/{1} passed; synthetic={2}; details in Saves[*].NativeSlides" -f $passedSlides, $slides.Count, $forcedSlides) Cyan
            }
            # END eng7-f5
            if ($sv.PSObject.Properties['Residence'] -and $sv.Residence) {
                $rs = $sv.Residence; $pr = $rs.Presence
                Say ("    residence spike: (a) entry={0} ({1:N0} ms from {2}; closet live={3}) (b) preset={4} ok={5} (c) presence ok={6} -> passed={7}" -f `
                    $rs.EntryOk, $rs.LoadMs, $rs.FromArea, $rs.ClosetLive, $rs.Preset, $rs.PresetOk, $rs.PresenceOk, $rs.Passed) Cyan
                Say ("      mechanics: {0}" -f (@($rs.ActiveMechanics) -join '; '))
                if (@($rs.NativeActions).Count) { Say ("      native actions: {0}" -f (@($rs.NativeActions) -join '; ')) Yellow }
                Say ("      copy {0}: spawned={1} view={2} rendered={3} walked={4} m dialog={5} removed={6}" -f $pr.UnitName, $pr.Spawned, $pr.ViewActive, $pr.Rendered, $pr.PathMovedMetres, $pr.DialogStarted, $pr.Removed)
                foreach ($f in @($rs.Findings)) { Say "      - $f" Yellow }
            }
            if ($sv.PSObject.Properties['PresenceSpike'] -and $sv.PresenceSpike -and $sv.PresenceSpike.PSObject.Properties['Probe'] -and $sv.PresenceSpike.Probe) {
                $probe = $sv.PresenceSpike.Probe
                Say ("    walkable probe: {0}, radius {1} m, area {2}" -f ($probe.Position -join ','), $probe.Radius, $sv.PresenceSpike.Area) Cyan
                foreach ($point in @($probe.Points)) {
                    Say ("      {0} ({1:N3} m)" -f (($point.Position | ForEach-Object { ([double]$_).ToString('R', [Globalization.CultureInfo]::InvariantCulture) }) -join ','), $point.Distance)
                }
            }
        }
        Say ("Runs {0}/{1} passed, choices {2}, relevant exceptions {3}, oracle failures {4}" -f $s.RunsPassed, $s.Runs, $s.Choices, $s.RelevantExceptions, $s.OracleFailures)
        if ($s.PSObject.Properties['SkippedInline'] -and $s.SkippedInline) { Say ("Skipped inline (host or list not reachable): {0}" -f $s.SkippedInline) Yellow }
        foreach ($f in @($s.Failures) | Select-Object -First 25) { Say "  - $f" Red }
        if ($s.PSObject.Properties['Skipped']) { foreach ($k in @($s.Skipped)) { Say "  (skipped) $k" Yellow } }
        if ($s.Passed -and $s.PSObject.Properties['AcceptanceComplete'] -and !$s.AcceptanceComplete) {
            Say 'INCOMPLETE coverage (execution checks passed)' Yellow; $exitCode = 2
        }
        elseif ($s.Passed) { Say 'PASS execution checks; campaign earning requires separate evidence' Green; $exitCode = 0 }
        elseif ($r.Status -ne 'complete') { Say 'FAIL (harness did not complete)' Red; $exitCode = 2 }
        else { Say 'FAIL' Red; $exitCode = 1 }
        if (!$s.PSObject.Properties['AcceptanceComplete']) { Say 'Legacy report: acceptance coverage is unavailable; rebuild the harness for H09 metadata.' Yellow }
        if ($EvidenceRequirements) {
            & (Get-Command python -ErrorAction Stop).Source (Join-Path $Repo 'tools/harness_evidence.py') $archived --requirements $EvidenceRequirements --source-hash $evidenceSourceHash --export-hash $evidenceExportHash --out (Join-Path $RunDir 'evidence-receipt.json')
            if ($LASTEXITCODE) { $exitCode = 2; Say 'INCOMPLETE acceptance: see evidence-receipt.json' Yellow }
        }
        Say "Report: $archived"
    }
}
catch {
    Say "Harness runner error: $_" Red
    $exitCode = 2
}
finally {
    if (Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue) {
        Get-Process -Name 'Wrath' -ErrorAction SilentlyContinue | Stop-Process -Force
        Start-Sleep -Seconds 3
    }
    Restore-Run $RunDir
}
exit $exitCode
