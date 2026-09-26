# Managed construction tests

This net48 executable invokes the development DLL's actual private `Main.Build` using the installed game assemblies.
Build the production project first so `src/bin/Release/net48/RanRomance.Tirabade.dll` contains the code under review.
The executable always loads that DLL, rather than a copied test version.
It reads the supplied story and does not assume a fixed scene count.

Run from the repository root in PowerShell:

```powershell
$env:RRT_PYTHON = "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe"
$env:RRT_PARENT_BINDINGS = (Resolve-Path reference/canon-review/expansion-parent-bindings.json).Path
& "$env:LOCALAPPDATA/RanRomanceTools/dotnet/dotnet.exe" build src/Tirabade.csproj -c Release --nologo -v quiet
& "$env:LOCALAPPDATA/RanRomanceTools/dotnet/dotnet.exe" build managed-tests/ManagedBuildTests.csproj -c Release --nologo -v quiet
& ./managed-tests/bin/Release/net48/ManagedBuildTests.exe 'D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure' development/Story.json
```

For another installation, pass `-p:GameDir=<game directory>/` to the build and the same game directory to the executable.
The .NET Framework 4.8 runtime and Python must be available.
Set `RRT_PYTHON` to the actual interpreter executable on another machine.
Without that override the runner uses `python` from the process search path; this machine's PyManager launcher has intermittently delivered empty redirected input, so the checked command selects the interpreter directly.
The combined parent manifest supplies explicitly tagged source fixtures for the Targona and Aranka extensions, not parent-mod initialization.
The tiny Python helper reads the installed `blueprints.zip` because .NET Framework's ZIP reader rejects this installation's archive headers.
It extracts only requested native records and writes no files.

The assertions cover:

- Successful actual blueprint construction, without a stored initialization error.
- GUID/type existence of native entry targets and etudes in the installed blueprint export.
- GUID/type existence of completed-quest bindings and their registration before construction.
- GUID/type existence of native cue-history bindings and their registration before construction.
- Preservation of native answer reference objects in their original order, with addon entries inserted before the final original answer.
- Preservation of native Aeon epilogue reference objects and order, followed by the expected addon pages.
- Preservation of two representative existing references in the parent mod's epilogue sequence.
- Unique generated blueprint IDs, correct scene first pages, resolvable page cues and choices, terminal choices and next-page links.
- Entry and choice visibility/selection guards retain the authored scene or choice and the correct owning blueprint.
- Choice actions retain authored effects and complete scenes only on non-aborted terminal choices.
- Persistent timestamp blueprints exist for all authored choice effects.
- A second `Build` call preserves the same registered objects, answer lists and epilogue lists without duplicates.

The normal epilogue sequence `ed4baeaf69394754902344f0598d7e5a` is created by RanRomance rather than supplied by the base game.
The fixture places two sentinel references in that sequence to test preservation.
It does not claim to reconstruct the parent's real slide list.
The parent also adds slides to the native Aeon sequence; this test's initial Aeon references come from the base-game archive.

The fixture seeds real game blueprint instances with actual native reference lists, but does not load the entire native graph or execute the parent mod.
Native etudes have validated IDs and types, but their state machines are not evaluated.
Game assemblies, localization, cache, blueprint classes, `OnEnable`, UMM entry and logger are real implementations.
No fake Unity types are used.
No game process, player, save, renderer or ToyBox instance is started.
Logging stays in the test process's console and manager buffers because the manager's watcher and file writer are never called.

The report includes hashes of the development DLL and story so the evidence can be tied to a specific build.
This is a construction and preservation test, not an in-game playthrough or save compatibility test.
