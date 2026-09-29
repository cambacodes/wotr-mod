param([string]$GameDir = 'C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure')
$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    $dotnetPath = Join-Path $env:LOCALAPPDATA 'RanRomanceTools/dotnet/dotnet.exe'
    if (!(Test-Path -LiteralPath $dotnetPath)) { $dotnetPath = (Get-Command dotnet -ErrorAction Stop).Source }
    python story.py
    if ($LASTEXITCODE) { throw 'Story build failed' }
    & $dotnetPath build src/Tirabade.csproj -c Release --nologo -v quiet "-p:GameDir=$GameDir/"
    if ($LASTEXITCODE) { throw 'Mod build failed' }
    & $dotnetPath build narrator/Narrator.csproj -c Release --nologo -v quiet
    if ($LASTEXITCODE) { throw 'Narrator build failed' }
    & $dotnetPath run --project tests/RulesTests.csproj -c Release -- package/Story.json
    if ($LASTEXITCODE) { throw 'Progression validation failed' }
    Copy-Item -LiteralPath 'src/bin/Release/net48/RanRomance.Tirabade.dll' -Destination 'package/RanRomance.Tirabade.dll'
    Copy-Item -LiteralPath 'narrator/bin/Release/net48/Tirabade.Narrator.exe' -Destination 'package/Tirabade.Narrator.exe'
    Copy-Item -LiteralPath 'narrator/bin/Release/net48/Tirabade.Narrator.exe.config' -Destination 'package/Tirabade.Narrator.exe.config'
} finally { Pop-Location }
