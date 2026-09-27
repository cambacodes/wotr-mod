# Headless verification record

Date: 2026-09-27.

This record pins the current development export and the bounded checks run against it.
It is technical integration evidence, not route approval or proof of an attainable full campaign.

## Export and build

`development/Story.json` contains 631 scenes across 18 relationship keys.
Its SHA-256 is `866B7C66C2027AFEE471FD4C497F57CD173E2AE789814FB268FC5DA49A9249C2`.
The regenerated `development/content-volume-inventory.json` records the same export hash.
The managed build used `src/bin/Release/net48/RanRomance.Tirabade.dll` with SHA-256 `288F8B156DAFB04A029F6A380FD95DE38E2FA9ADB7DBE148DFB06CC1F619ED25`.

## Checks run

The successful root run used the bundled SDK at `$env:LOCALAPPDATA/RanRomanceTools/dotnet/dotnet.exe`.
It set `RRT_PYTHON` to `C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64/python.exe` and set `RRT_PARENT_BINDINGS` to `reference/canon-review/expansion-parent-bindings.json;reference/canon-review/nurah-parent-bindings.json;reference/canon-review/nurah-parent-runtime-cue-bindings.json`.
It built `src/Tirabade.csproj`, `managed-tests/ManagedBuildTests.csproj`, and `tests/RulesTests.csproj` in Release configuration.
`managed-tests/bin/Release/net48/ManagedBuildTests.exe 'D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure' development/Story.json` constructed the current 631-scene graph against the installed game assemblies and passed 84,259 assertions.
That run created 22,850 generated blueprints and preserved 14 native answer lists, the native Aeon sequence, and a parent-mod sentinel sequence across an idempotent second build.
The test explicitly reports that it does not initialize RanRomance, execute Unity, run a real campaign, render portraits, execute ToyBox, or round-trip a game save.

`& "$env:LOCALAPPDATA/RanRomanceTools/dotnet/dotnet.exe" ./tests/bin/Release/net8.0/RulesTests.dll development/Story.json` passed 28,550,910 assertions, covering the original campaign, independent-relationship rules, authored expansion scenarios, and 563 draft expansion scenes.
The Targona sequential test covers both Trickster page-history setups, ordinary correspondence, each of the four prior visit outcomes, and their corresponding follow-up branch.
The Aranka sequential test covers each of the three preceding story-history branches and both concrete-plan and deferred outcomes.
These branches use explicitly seeded snapshot flags and contact fixtures, so they validate authored graph and rule wiring rather than campaign acquisition or a played save.

`python -m unittest tests.test_parent_bindings -v` passed its focused parent-evidence pin test.
`python tools/measure-story-content.py --self-test` passed formatting, deduplication, route-separation, and unsupported-credit checks.
`git diff --check` passed for the current worktree at the time of this record.

These results record the successful root-run environment and are distinct from a later independent reproduction attempted in an environment without the bundled .NET SDK and without the configured parent-binding fixtures.
In that separate environment, the RulesTests apphost could not start because .NET 8 was unavailable, and the managed runner stopped during archive extraction after reporting 68 missing blueprint IDs.
Those local reproduction failures do not overwrite the successful root-run results, but they show that the run depends on its recorded SDK, Python executable, parent-binding fixtures and matching game archive.
Neither run executes Unity, starts a real campaign, verifies live actor placement, renders art, or exercises ToyBox settings or a saved game.

## Unregistered route-draft checks

The following source-only checks were run after the 631-scene export test, against files that are not registered in that export.
`python -m py_compile` passed for `storylines/aranka_path_acquisition.py`, `storylines/targona_trickster_acquisition.py`, and `storylines/terendelev_continuation.py`.
`python storylines/aranka_path_acquisition.py` passed its explicitly synthetic predicate-contract check; the test supplies path and contact flags and proves no producer or actual access.
A focused source invariant check passed for Targona's failed-Perception recovery through route tracing to the bounded intervention.
The same check confirmed ten Terendelev remote scenes have no ContactUnit and seven physical scenes require `returned_actor_confirmed`.
The reviewed source hashes are Aranka `7F7CA38A934ED03AE75651F8688C2C2184A799D6A0C927EE4FEB36D94B6DE3C1`, Targona `9F8C743270CF6F4AD1FBCEF9206AC1B0E83BDF73AE08F282B574BBF6B25C9C06`, and Terendelev `D1744F54076BE63536232ED45D040D266CAB74DE1425B138A0EA93E14C1A30CD`.
Independent reviews confirm the scoped source corrections but explicitly withhold full-route or live-access approval.

## Remaining verification

The managed runner's native resurrection fixture logs a caught `SecurityException` because the engine's native resurrection call cannot execute outside its system module.
The contact fixture also records the known area-state boundary for an actor outside the persistent area's entity list.
These are labeled fixtures and do not prove a live resurrection or actor placement.

No check here proves the complete route for any character, attainable and tested access on all ten mythic paths, concurrent Trickster acquisition and recovery, content read on a substantial single playthrough, reviewer scores for a whole assembled route, art quality or mapping, or compatibility in an actual save.
The Targona acquisition prototype, Aranka all-path access design, and Terendelev continuation are not registered in this 631-scene export and were not exercised by these test results.
Manual Unity verification still needs to cover dialogue display, skill checks, actor interaction, persistence, Love Is Free and Jealousy Begone, scene transitions, and at least one chronological Trickster campaign.
The 631-scene development export is not a packaged release and is not ready for the requested whole-roster playtest.
