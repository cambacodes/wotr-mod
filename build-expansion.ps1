param(
    [string]$GameDir = 'D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure',
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
$previousPython = $env:RRT_PYTHON
$previousBindings = $env:RRT_PARENT_BINDINGS
$previousExpandedEpilogue = $env:RRT_TEST_EXPANDED_EPILOGUE
Push-Location $PSScriptRoot
try {
    $GameDir = (Resolve-Path -LiteralPath $GameDir).Path
    $pythonPath = (Get-Command $Python -ErrorAction Stop).Source
    $dotnetPath = Join-Path $env:LOCALAPPDATA 'RanRomanceTools/dotnet/dotnet.exe'
    if (!(Test-Path -LiteralPath $dotnetPath)) { $dotnetPath = (Get-Command dotnet -ErrorAction Stop).Source }
    $env:RRT_PYTHON = $pythonPath
    $env:RRT_PARENT_BINDINGS = (@(
        'reference/canon-review/expansion-parent-bindings.json'
        'reference/canon-review/nurah-parent-bindings.json'
        'reference/canon-review/nurah-parent-runtime-cue-bindings.json'
    ) | ForEach-Object { Join-Path $PSScriptRoot $_ } | Where-Object { Test-Path -LiteralPath $_ }) -join [IO.Path]::PathSeparator

    & $pythonPath expansion.py
    if ($LASTEXITCODE) { throw 'Expansion generation failed' }
    $validatedStoryHash = (Get-FileHash -LiteralPath 'development/Story.json').Hash
    & $dotnetPath build src/Tirabade.csproj -c Release --nologo -v quiet "-p:GameDir=$GameDir/"
    if ($LASTEXITCODE) { throw 'Expansion assembly build failed' }
    # Static gate (GLOBAL-15): structure, dead gates, TypeIds, native bindings, released-save references.
    & $pythonPath tools/rrt_verify.py --strict --quiet --story development/Story.json --game $GameDir
    if ($LASTEXITCODE) { throw 'Static verification failed (tools/rrt_verify_report.txt)' }
    & $dotnetPath build narrator/Narrator.csproj -c Release --nologo -v quiet
    if ($LASTEXITCODE) { throw 'Narrator build failed' }
    & $dotnetPath run --project tests/RulesTests.csproj -c Release -- development/Story.json
    if ($LASTEXITCODE) { throw 'Expansion progression validation failed' }
    & $pythonPath tools/verify-game-bindings.py development/Story.json --game $GameDir --parent-bindings $env:RRT_PARENT_BINDINGS
    if ($LASTEXITCODE) { throw 'Expansion native binding validation failed' }
    & $dotnetPath build managed-tests/ManagedBuildTests.csproj -c Release --nologo -v quiet "-p:GameDir=$GameDir/"
    if ($LASTEXITCODE) { throw 'Managed verification build failed' }
    foreach ($fixtureMode in @('0', '1', 'wrong-type')) {
        $env:RRT_TEST_EXPANDED_EPILOGUE = $fixtureMode
        & ./managed-tests/bin/Release/net48/ManagedBuildTests.exe $GameDir development/Story.json
        if ($LASTEXITCODE) { throw "Expansion managed construction validation failed: optional epilogue $fixtureMode" }
    }
    # Real UMM entry point: Story.json deserialize + Rules.Validate + Harmony PatchAll per class (GLOBAL-02).
    $env:RRT_TEST_EXPANDED_EPILOGUE = '0'
    $env:RRT_TEST_LOAD = '1'
    & ./managed-tests/bin/Release/net48/ManagedBuildTests.exe $GameDir development/Story.json
    $loadExit = $LASTEXITCODE
    $env:RRT_TEST_LOAD = $null
    if ($loadExit) { throw 'Load smoke test failed: the mod would not load in UnityModManager' }
    # Save-safe degradation (GLOBAL-01): a vanished native binding disables only the relationships that use it.
    foreach ($missing in @('irabeth_dead', 'trickster')) {
        $env:RRT_TEST_MISSING_ETUDE = $missing
        & ./managed-tests/bin/Release/net48/ManagedBuildTests.exe $GameDir development/Story.json
        $missingExit = $LASTEXITCODE
        $env:RRT_TEST_MISSING_ETUDE = $null
        if ($missingExit) { throw "Partial-integration fixture failed: missing $missing" }
    }
    if ((Get-FileHash -LiteralPath 'development/Story.json').Hash -ne $validatedStoryHash) {
        throw 'Expansion story changed during validation; rebuild before packaging'
    }

    # A new directory prevents stale assets from surviving a previous package.
    $output = Join-Path $PSScriptRoot ('dist/expansion-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [guid]::NewGuid().ToString('N').Substring(0, 8))
    $modOutput = Join-Path $output 'Mods/RanRomanceTirabade'
    $artOutput = Join-Path $output 'Mods/CustomNpcPortraits'
    New-Item -ItemType Directory -Path $modOutput, $artOutput -Force | Out-Null
    $inputs = [ordered]@{
        'package/Info.json' = 'Info.json'
        'development/Story.json' = 'Story.json'
        'src/bin/Release/net48/RanRomance.Tirabade.dll' = 'RanRomance.Tirabade.dll'
        'narrator/bin/Release/net48/Tirabade.Narrator.exe' = 'Tirabade.Narrator.exe'
        'narrator/bin/Release/net48/Tirabade.Narrator.exe.config' = 'Tirabade.Narrator.exe.config'
    }
    foreach ($source in $inputs.Keys) {
        $target = Join-Path $modOutput $inputs[$source]
        Copy-Item -LiteralPath $source -Destination $target
        if ((Get-FileHash -LiteralPath $source).Hash -ne (Get-FileHash -LiteralPath $target).Hash) { throw "Package copy mismatch: $source" }
    }
    if ((Get-FileHash -LiteralPath (Join-Path $modOutput 'Story.json')).Hash -ne $validatedStoryHash) {
        throw 'Expansion story changed during staging; package is incomplete'
    }
    $artSource = Join-Path $PSScriptRoot 'art/CustomNpcPortraits'
    foreach ($file in Get-ChildItem -LiteralPath $artSource -File -Recurse) {
        $relative = $file.FullName.Substring($artSource.Length + 1)
        $target = Join-Path $artOutput $relative
        New-Item -ItemType Directory -Path (Split-Path -Parent $target) -Force | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $target
        if ((Get-FileHash -LiteralPath $file.FullName).Hash -ne (Get-FileHash -LiteralPath $target).Hash) { throw "Portrait copy mismatch: $relative" }
    }
    Copy-Item -LiteralPath development/PLAYTEST-PACKAGE.md -Destination (Join-Path $output 'README.md')
    $story = Get-Content -LiteralPath (Join-Path $modOutput 'Story.json') -Raw | ConvertFrom-Json
    $portraitKeys = @($story.Scenes | ForEach-Object { $_.Nodes } | ForEach-Object {
        if ($_.Portrait) { $_.Portrait } elseif ($_.Speaker -eq 'Narrator') { 'Together' } else { $_.Speaker }
    } | Sort-Object -Unique)
    $missingPortraits = @($portraitKeys | Where-Object {
        !(Test-Path -LiteralPath (Join-Path $artOutput ('RanRomance-Tirabade/Scenes/' + $_ + '.png')))
    })
    $files = @(Get-ChildItem -LiteralPath $output -File -Recurse | Sort-Object FullName | ForEach-Object {
        [ordered]@{ Path = $_.FullName.Substring($output.Length + 1); SHA256 = (Get-FileHash -LiteralPath $_.FullName).Hash }
    })
    [ordered]@{
        Status = 'Incomplete development package; not release approval'
        SceneCount = $story.Scenes.Count
        StorySHA256 = (Get-FileHash -LiteralPath (Join-Path $modOutput 'Story.json')).Hash
        MissingPortraitKeys = $missingPortraits
        VerificationScope = 'Rules, native bindings and managed construction; no Unity, save/load or ToyBox execution'
        Files = $files
    } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $output 'manifest.json') -Encoding UTF8
    Write-Output "Development package built: $output"
    Write-Output "Scenes: $($story.Scenes.Count). Missing portrait keys: $($missingPortraits.Count). No installed files changed."
} finally {
    $env:RRT_PYTHON = $previousPython
    $env:RRT_PARENT_BINDINGS = $previousBindings
    $env:RRT_TEST_EXPANDED_EPILOGUE = $previousExpandedEpilogue
    Pop-Location
}
