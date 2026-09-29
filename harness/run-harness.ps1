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

.NOTES
  Exit codes: 0 all checks passed, 1 tests failed, 2 harness/infrastructure failure (no report, timeout, crash),
  3 bad arguments or failed preflight.
  After a hard kill of this script, restore with:  ./harness/run-harness.ps1 -RestoreFrom harness/.runs/<stamp>
#>
[CmdletBinding()]
param(
    [string]$GameDir = 'D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure',
    [string[]]$Saves = @(),
    [switch]$Force,
    [switch]$DryRun,
    [ValidateSet('random', 'dfs')][string]$Mode = 'random',
    [int]$Seed = 20,
    [int]$WalksPerScene = 1,
    [int]$MaxPathsPerScene = 8,
    [int]$MaxScenesPerSave = 0,
    [string[]]$SceneFilter = @(),
    [switch]$NoRoundTrip,
    [switch]$Headless,
    [switch]$Windowed,
    [switch]$Screenshots,
    [int]$ScreenshotsPerScene = 3,
    [switch]$Inline,
    [int]$MaxInlineNavSteps = 40,
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

$copies = [Collections.Generic.List[object]]::new()
function Add-Copy([string]$Source, [string]$Target, [bool]$Optional = $false) {
    $copies.Add([PSCustomObject]@{ Source = $Source; Target = $Target; Optional = $Optional })
}
Add-Copy (Join-Path $Repo 'package\Info.json') (Join-Path $RrtModDir 'Info.json')
Add-Copy $rrtDll (Join-Path $RrtModDir 'RanRomance.Tirabade.dll')
Add-Copy (Join-Path $Repo 'development\Story.json') (Join-Path $RrtModDir 'Story.json')
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
$inlineHosts = Join-Path $HarnessDir 'inline-hosts.json'
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
$planJson = $plan | ConvertTo-Json -Depth 5

$launchArgs = @()
if ($Windowed -or $Screenshots) { $launchArgs = @('-screen-fullscreen', '0', '-screen-width', '1280', '-screen-height', '720') }
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
        }
        Say ("Runs {0}/{1} passed, choices {2}, relevant exceptions {3}, oracle failures {4}" -f $s.RunsPassed, $s.Runs, $s.Choices, $s.RelevantExceptions, $s.OracleFailures)
        if ($s.PSObject.Properties['SkippedInline'] -and $s.SkippedInline) { Say ("Skipped inline (host or list not reachable): {0}" -f $s.SkippedInline) Yellow }
        foreach ($f in @($s.Failures) | Select-Object -First 25) { Say "  - $f" Red }
        if ($s.PSObject.Properties['Skipped']) { foreach ($k in @($s.Skipped)) { Say "  (skipped) $k" Yellow } }
        if ($s.Passed) { Say 'PASS' Green; $exitCode = 0 }
        elseif ($r.Status -ne 'complete') { Say 'FAIL (harness did not complete)' Red; $exitCode = 2 }
        else { Say 'FAIL' Red; $exitCode = 1 }
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
