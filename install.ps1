param(
    [string]$GameDir = 'D:\SteamLibrary\steamapps\common\Pathfinder Second Adventure',
    [string]$UserData = (Join-Path $env:USERPROFILE 'AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous')
)
$ErrorActionPreference = 'Stop'
$packageDir = Join-Path $PSScriptRoot 'package'
$portraitDir = Join-Path $PSScriptRoot 'art/CustomNpcPortraits'
$modDir = Join-Path $GameDir 'Mods/RanRomanceTirabade'
$portraitModDir = Join-Path $GameDir 'Mods/CustomNpcPortraits'
if (!(Test-Path -LiteralPath (Join-Path $GameDir 'Mods/RanRomance/RanRomance.dll'))) { throw 'Install Relations and Romances first.' }
if (!(Test-Path -LiteralPath (Join-Path $portraitModDir 'Info.json'))) { throw 'Install CustomNpcPortraits first.' }
foreach ($required in @('Info.json','Story.json','RanRomance.Tirabade.dll','Tirabade.Narrator.exe')) {
    if (!(Test-Path -LiteralPath (Join-Path $packageDir $required))) { throw "Build the package first: missing $required" }
}
$backupDir = Join-Path $PSScriptRoot ('backups/' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
$records = [Collections.Generic.List[object]]::new()
function Install-File([string]$Source, [string]$Target) {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Target) | Out-Null
    if (Test-Path -LiteralPath $Target) {
        if ((Get-FileHash -LiteralPath $Source).Hash -eq (Get-FileHash -LiteralPath $Target).Hash) { return }
        $backup = Join-Path $backupDir ([string]$records.Count + '-' + [IO.Path]::GetFileName($Target))
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        Copy-Item -LiteralPath $Target -Destination $backup
    } else { $backup = $null }
    Copy-Item -LiteralPath $Source -Destination $Target -Force
    $records.Add([PSCustomObject]@{ Target=$Target; Backup=$backup; Hash=(Get-FileHash -LiteralPath $Target).Hash })
}
foreach ($file in Get-ChildItem -LiteralPath $packageDir -File) {
    Install-File $file.FullName (Join-Path $modDir $file.Name)
}
foreach ($file in Get-ChildItem -LiteralPath $portraitDir -File -Recurse) {
    $relative = $file.FullName.Substring($portraitDir.Length + 1)
    Install-File $file.FullName (Join-Path $portraitModDir $relative)
}
foreach ($name in @('Anevia','Irabeth')) {
    foreach ($size in @('Fulllength.png','Medium.png','Small.png')) {
        $source = Join-Path $portraitDir "Portraits - Npc/$name/$size"
        Install-File $source (Join-Path $UserData "Portraits - Npc/$name/$size")
        # Anevia temporarily uses companion presentation in the prologue. Preserve both supported layouts.
        Install-File $source (Join-Path $UserData "Portraits/CustomNpcPortraits - $name/$size")
        Install-File $source (Join-Path $portraitModDir "Portraits/CustomNpcPortraits - $name/$size")
    }
}
New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
$records | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $backupDir 'manifest.json') -Encoding utf8
Write-Output "Installed $($records.Count) files. Backup manifest: $backupDir/manifest.json"
Write-Output 'Restart the game application once, then load an existing save. A new campaign is not required.'
