param(
    [string]$GameDir = 'C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure',
    [string]$UserData = (Join-Path $env:USERPROFILE 'AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous')
)
$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath (Join-Path $GameDir 'Wrath.exe'))) { throw 'Pass -GameDir with your Wrath installation directory.' }
foreach ($dependency in @('RanRomance','CustomNpcPortraits')) {
    if (!(Test-Path -LiteralPath (Join-Path $GameDir "Mods/$dependency/Info.json"))) { throw "Install $dependency before this extension." }
}
$backupRoot = Join-Path $GameDir ('ThreeAtTheTableBackups/' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
$records = [Collections.Generic.List[object]]::new()
function Copy-BackedUp([string]$Source, [string]$Target) {
    if (Test-Path -LiteralPath $Target) {
        if ((Get-FileHash -LiteralPath $Source).Hash -eq (Get-FileHash -LiteralPath $Target).Hash) { return }
        New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
        $backup = Join-Path $backupRoot ([string]$records.Count + '-' + [IO.Path]::GetFileName($Target))
        Copy-Item -LiteralPath $Target -Destination $backup
    } else { $backup = $null }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Target) | Out-Null
    Copy-Item -LiteralPath $Source -Destination $Target -Force
    $records.Add([PSCustomObject]@{Target=$Target; Backup=$backup})
}
$sourceRoot = Join-Path $PSScriptRoot 'Mods'
foreach ($file in Get-ChildItem -LiteralPath $sourceRoot -File -Recurse) {
    $relative = $file.FullName.Substring($sourceRoot.Length + 1)
    Copy-BackedUp $file.FullName (Join-Path $GameDir "Mods/$relative")
}
foreach ($name in @('Anevia','Irabeth')) {
    foreach ($size in @('Fulllength.png','Medium.png','Small.png')) {
        $source = Join-Path $sourceRoot "CustomNpcPortraits/Portraits - Npc/$name/$size"
        Copy-BackedUp $source (Join-Path $UserData "Portraits - Npc/$name/$size")
        Copy-BackedUp $source (Join-Path $UserData "Portraits/CustomNpcPortraits - $name/$size")
    }
}
if ($records.Count -gt 0) {
    New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
    $records | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $backupRoot 'manifest.json') -Encoding utf8
}
Write-Output 'Installed. Restart Wrath once, then load your existing save and speak to Anevia and Irabeth normally.'
