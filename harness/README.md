# RRT in-game test harness (GLOBAL-20)

`RRTTestHarness` is a separate UnityModManager mod. It loads real saves in the real game, opens every
RRT scene dialog, picks answers programmatically, and records what breaks. It needs no human input and
no OCR: every observation comes from game objects, RRT internals read by reflection, and log hooks.

```
harness/
  RRT.TestHarness.csproj      UMM mod (net48, game DLLs referenced with Private=false, like src/Tirabade.csproj)
  Info.json                   Id RRTTestHarness, LoadAfter RanRomanceTirabade, EntryMethod RRT.TestHarness.Entry.Load
  src/Entry.cs                activation gate, Harmony hooks, creates the runner object
  src/HarnessRunner.cs        step machine: main menu -> load -> snapshot -> drive scenes -> round-trip -> report -> quit
  src/RrtBridge.cs            reflection into Tirabade.Main / Story / Rules (pure, no Unity)
  src/LogCapture.cs           Unity, Owlcat (PFLog) and UMM log hooks, plus Harmony finalizers
  src/HarnessPlan.cs          plan model and activation rule (pure)
  src/HarnessReport.cs        report model and pass/fail summary (pure)
  src/InlineHosts.cs          -Inline host model and navigation policy (pure)
  SelfTest/                   offline net48 console self-test (no game launch)
  run-harness.ps1             install, run, collect, restore
  resolve-inline-hosts.py     offline resolver: native host dialog, owning cue and click path for every entry list
  inline-hosts.json           its output (commit it after regenerating; SelfTest fails when it is stale)
```

## Quick start

```powershell
# 1. Build (0 errors expected). RRT itself is built by build.ps1 into src/bin/Release/net48.
& "$env:LOCALAPPDATA\RanRomanceTools\dotnet\dotnet.exe" build harness/RRT.TestHarness.csproj -c Release
# 2. Offline self-test: plan parsing, report writing, reflection lookups against the built RRT DLL.
& "$env:LOCALAPPDATA\RanRomanceTools\dotnet\dotnet.exe" build harness/SelfTest/RRT.TestHarness.SelfTest.csproj -c Release
harness/SelfTest/bin/Release/net48/RRT.TestHarness.SelfTest.exe
# 3. See what a live run would touch (it copies and launches nothing):
./harness/run-harness.ps1 -DryRun -Saves 'Manual_1_Neathholm__15_Arodus__VIII__4715__12_30_02'
# 4. Live run (this modifies the game's Mods folder and restores it afterwards):
./harness/run-harness.ps1 -Saves 'Manual_1_Neathholm__15_Arodus__VIII__4715__12_30_02'
```

The `run-harness.ps1` options are:

- `-Saves` takes names in `Saved Games` or absolute `.zks` paths. If you omit it, the script uses the newest save.
- `-Force` drives every scene that has a dialog, not only the available ones.
- `-Mode random|dfs` chooses the answer strategy. Tune it with `-Seed`, `-WalksPerScene`, `-MaxPathsPerScene` and `-MaxScenesPerSave`.
- `-SceneFilter` takes scene ids or prefixes.
- `-NoRoundTrip` skips the save round-trip.
- `-Inline` drives scenes through their host native dialogs instead of opening RRT dialogs directly; `-MaxInlineNavSteps`
  (default 40) bounds the clicks inside the host. See [Inline mode](#inline-mode--inline).
- `-Screenshots` captures each shown scene cue into `harness/.runs/<stamp>/shots` (up to `-ScreenshotsPerScene`, default 3).
  It opens a normal, visible 1280x720 window: warn the user first and do not click in it.
- `-Headless` opens dialogs without the UI.
- Launch size: runs without `-Screenshots`/`-Windowed` start Wrath in a lean 800x600 window (pass `-FullRes` for the default resolution). `-BatchMode` (experimental) launches with `-batchmode -nographics`; it cannot take screenshots.
- `-Windowed` passes the standard Unity `-screen-*` arguments.
- `-TimeoutMinutes` sets the run timeout (default 45).
- `-Spike Residence` runs the P2 residence feasibility spike instead of driving scenes. See [Residence spike](#residence-spike--spike-residence).
- `-Spike Presence` runs the E12d quiet-copy check instead of driving scenes. See [Presence spike](#presence-spike--spike-presence).
- `-Build` rebuilds the harness first.
- `-RestoreFrom harness/.runs/<stamp>` restores the Mods folder after the script itself was killed.

Exit codes: `0` means every check passed. `1` means a test failed. `2` means an infrastructure failure: no report, a timeout, or a crash. `3` means bad arguments or a failed preflight.

## What a run does

1. **Install** (`run-harness.ps1`). Before any file is written, the script:
   - backs up `Mods/RanRomanceTirabade` and `Mods/RRTTestHarness` as whole folders;
   - backs up each `Mods/CustomNpcPortraits` file it will overwrite;
   - backs up UMM `Params.xml`;
   - writes a manifest to `harness/.runs/<stamp>/`.

   It then copies these files:

   | Source | Destination |
   |---|---|
   | `package/Info.json`, `src/bin/Release/net48/RanRomance.Tirabade.dll`, `development/Story.json`, the narrator (if built) and `package/Portraits` | `Mods/RanRomanceTirabade` |
   | `art/CustomNpcPortraits/**` | `Mods/CustomNpcPortraits` |
   | the harness DLL, its `Info.json` and `rrt-harness-plan.json` | `Mods/RRTTestHarness` |

   The script launches `Wrath.exe` minimized and polls for the report. After the run, it archives:
   - the report;
   - `Player.log`, `GameLogFull.txt` and the UMM `Log.txt`.

   It restores everything in a `finally` block, and the restore also runs after a failure or Ctrl+C.
2. **Activation** (`Entry.Load`). The harness does nothing unless `rrt-harness-plan.json` is in its mod folder,
   or `RRT_HARNESS_PLAN` points to a plan file (`RRT_HARNESS_PLAN=1` runs the default init-only plan).
   On start, the plan file is renamed to `*.consumed-<time>`. A forgotten install therefore never takes over a normal session.
   The harness also sets `Application.runInBackground = true`, so a minimized window keeps ticking.
3. **Init check.** The harness waits for the main menu (`Game.Instance.UI.MainMenu != null` and no loading process),
   then for `BlueprintsCache.Init`. RRT builds its blueprints in a postfix on `BlueprintsCache.Init`, and the harness postfix
   is ordered after the RRT Harmony id. It then records:
   - UMM's view of RRT: `FindMod("RanRomanceTirabade")`, `Active` and `ErrorOnLoading`;
   - the private statics of `Tirabade.Main`: `initialized`, `enabled`, `error`, `degraded` and `warnings`;
   - the scene and dialog counts;
   - any reflection mismatch.
4. **Per save.** The harness loads the save and waits until the area is loaded and the game is idle. It then snapshots
   `Tirabade.Main.State()` (internal static), evaluates `Tirabade.Rules.Available(story, scene, state)` for every scene,
   and drives each target scene:
   1. It sets the relationship's started flag (`Main.Set`), exactly as `Main.Update` does before it queues a scene.
      In force mode, it also sets the scene's `Requires` flags.
   2. It calls `DialogController.StartDialogWithoutTarget(dialogs[scene.Id], null)`.
   3. It loops until the dialog closes. Each iteration waits until no cue is scheduled and answers are shown, then picks an index:
      - a seeded random walk (the seed is FNV(scene id) mixed with the plan seed and walk number, so runs are reproducible); or
      - DFS over answer indices, where every branch replays its prefix after a fresh save reload.
   4. It calls `DialogController.SelectAnswer(answer)`.
   5. After each RRT choice, it checks two oracles that mirror `RouteAction.RunAction`'s own guards
      (`Rules.Match`, `ContactAvailable`, no revive):
      - the choice's `Set` flags are present in `State()`;
      - a terminal choice (`Next == null`, no check, not abort, not an epilogue) recorded the scene-completion flag.
   6. Before the next scene, the harness reloads the save by default, so every scene starts from the saved state.
      With `-Force`, it keeps going in the same state instead.
5. **Save round-trip.** After the first scene that completes in a save, the harness:
   1. compares `State()` before and after a save and reload through a temporary manual save,
      created with `CreateNewSave("RRTHarness roundtrip")` and `Game.SaveGame`;
   2. deletes the temporary save afterwards with `SaveManager.DeleteSave`.

   Only persistent RRT unlockable flags (the keys of `Main.flags`) and `hour.*` times count toward pass or fail.
   Derived live flags (contact presence, correspondence availability) are listed in `DerivedChanged` for information only.
   The round-trip is skipped with a reason on ironman saves and wherever `IsSaveAllowed(Manual)` is false.
6. **Report and quit.** The harness writes `rrt-harness-report.json` atomically after init, after every scene and at the end.
   It records:
   - status, timings and init state;
   - per save: load result, load time, not-idle reason, the full `State()` snapshot, available scenes and scenes without a dialog;
   - per run: strategy, answer-index path, choices (answer blueprint name, text, story choice `scene/node/i`),
     result (`completed`, `not-started`, `stuck`, `step-limit`, `path-diverged`, `exception`, `skipped-native`, `skipped-delay`;
     with `-Inline` also `skipped-inline`, `entry-hidden` and `entry-not-started`, plus the `Inline` host record),
     oracle failures, flags added and removed, exceptions with stack traces, and time in ms;
   - the round-trip result and a summary with a failure list.

   The harness then calls `Application.Quit()`. A global timeout aborts the run cleanly and still writes the report.

### Exception capture

Every error is stored with its source, severity, message, stack and context (save, scene or phase). The harness collects errors from these sources:

- **Unity log.** `Application.logMessageReceivedThreaded` entries of type Error, Exception and Assert.
- **Owlcat log (`PFLog`, `LogChannel`, the source of `GameLogFull.txt`).** A sink registered with `Owlcat.Runtime.Core.Logging.Logger.Instance.AddLogger(ILogSink, false)`. It catches `Trying to select invalid dialog answer` and `Could not select any cue in book page`.
- **UMM logger.** Harmony prefixes on `UnityModManager.Logger.Log(string, string)` for `[Error]` and `[Critical]` lines, and on `LogException(string, Exception, string)` for the full exception.
- **Harmony finalizers.** On `DialogController.SelectAnswer`, `DialogController.Tick`, `Tirabade.Main+RouteAction.RunAction` and `Tirabade.Main+RouteCondition.CheckCondition`. They record the exception and rethrow it unchanged, so game behaviour does not change.

An entry is **relevant**, and fails the run, when it:

- comes from a finalizer; or
- mentions Tirabade, `RRT_`, RanRomance, the harness, `DialogController`, `BookEvent`, or the invalid-answer or cue errors.

Other native noise is kept in the report but does not fail the run.

## Verified game API (decompiled with ilspycmd 9.1 into `Writer/tools/scratch/harness-decomp`)

| Purpose | Exact signature (file:line in harness-decomp) |
|---|---|
| Game exists without creating it | `public static bool Game.HasInstance` (Kingmaker.Game.cs:359) |
| Load from main menu | `public void MainMenu.LoadGame(SaveInfo saveInfo)` → `EnterGame(() => Game.Instance.LoadGameFromMainMenu(saveInfo))` (Kingmaker.MainMenu.cs:387; Game.cs:2174) |
| Load in game | `public void Game.LoadGame(SaveInfo saveInfo)` (Game.cs:2143). This is what `CommonUILoadService.Load` calls after its confirmation modal. It returns silently when chargen is open or `!saveInfo.CheckDlcAvailable()`, so the harness checks the DLC first and times out on "load did not start". |
| Main menu present | `public MainMenu UIAccess.MainMenu` (Kingmaker.UI.UIAccess.cs:67), set in `MainMenu.Awake` and cleared in `OnDestroy` |
| Save list refresh | `public void SaveManager.UpdateSaveListIfNeeded(bool force = false)` (SaveManager.cs:309); `SaveManager : IEnumerable<SaveInfo>` |
| Save from path | `[CanBeNull] public SaveInfo SaveManager.LoadZipSave(string file)` (SaveManager.cs:251). It is used only when the file is outside the listed saves. |
| Saves folder | `public string SaveManager.SavePath` (SaveManager.cs:115) |
| New save slot | `public SaveInfo SaveManager.CreateNewSave(string name)` (SaveManager.cs:319). This is the same sequence `SaveLoadVM.ExecuteCreateNewSave` uses. |
| Save | `public void Game.SaveGame(SaveInfo saveInfo, Action callback = null)` (Game.cs:2206). It refuses silently when `!IsSaveAllowed` or ironman (`SettingsRoot.Difficulty.OnlyOneSave`). |
| Save allowed | `public bool SaveManager.IsSaveAllowed(SaveInfo.SaveType saveType)` (SaveManager.cs:730) |
| Save committed | `public bool SaveManager.CommitInProgress` (SaveManager.cs:135); `SaveInfo.IsActuallySaved`, `SaveInfo.FolderName` (SaveInfo.cs:146, :120) |
| Delete temp save | `public void SaveManager.DeleteSave(SaveInfo saveInfo)` (SaveManager.cs:590) |
| DLC check | `public bool SaveInfo.CheckDlcAvailable()` (SaveInfo.cs:232) |
| Loading state | `public bool Game.IsLoadingSave` (Game.cs:409), `public bool Game.IsUnloading` (Game.cs:407), `public static LoadingProcess LoadingProcess.Instance` (LoadingProcess.cs:111), `public bool LoadingProcess.IsLoadingInProcess` (:131), `public bool LoadingProcess.IsLoadingScreenActive` (:143) |
| Idle | `public BlueprintArea Game.CurrentlyLoadedArea` (Game.cs:396); `public GameModeType Game.CurrentMode` (Game.cs:504), compared with `GameModeType.Default` and `GameModeType.GlobalMap` (GameModeType.cs:27, :29); `public bool Game.IsPaused { get; set; }` (Game.cs:436); `Player.IsInCombat`; `Player.Dialog.Scheduled`. These match RRT's own `Main.Idle()`. |
| Start dialog | `public void DialogController.StartDialogWithoutTarget([NotNull] BlueprintDialog dialog, [CanBeNull] LocalizedString speakerName, [CanBeNull] UnitEntityData initiator = null)` (DialogController.cs:330) |
| Dialog state | `public BlueprintDialog DialogController.Dialog` (:84), `public BlueprintCue CurrentCue` (:146), `public IEnumerable<BlueprintAnswer> Answers => m_Answers` (:287), `private bool m_CuePlayScheduled` (:121). The next cue plays on the following `Tick()` (:300). |
| Select answer | `public void DialogController.SelectAnswer(BlueprintAnswer answer, UnitEntityData manualUnitSelection = null)` (:641). It logs "Trying to select invalid dialog answer" when the answer is not in `m_Answers`, and returns when `CurrentCue == null`. |
| Book pages | `PlayBookPage` (:991) plays each page cue as a `BlueprintCue` (sets `CurrentCue`), then `AddAnswers(page.Answers)`. `SelectAnswer` therefore works for RRT book dialogs. |
| Stop / headless | `public void DialogController.StopDialog()` (:603); `public void SetHeadlessMode(bool enabled)` (:315) |
| Answer text | `public string BlueprintAnswer.DisplayText` (BlueprintAnswer.cs:61) |
| Cache hook | `public void BlueprintsCache.Init()` (BlueprintsCache.cs:32) |
| Owlcat log sink | `public void Logger.AddLogger(ILogSink logSink, bool populateWithExistingMessages = true)` (Owlcat.Runtime.Core.Logging.Logger.cs:150); `interface ILogSink { void Log(LogInfo); void Destroy(); }`; `LogInfo.Severity/Message/Callstack/IsException` |
| UMM log hooks | `public static void UnityModManager.Logger.Log(string str, string prefix)` (UMM.Logger.cs:1304); `public static void LogException(string key, Exception e, string prefix)` (:1338). `ModLogger.Error`, `Critical` and `LogException` all route here. |

The members read from RRT by reflection are listed with their expected type shapes in `RrtBridge.Expectations`
(48 entries). `SelfTest` checks all of them against `src/bin/Release/net48/RanRomance.Tirabade.dll`.
`Main.State()` is internal and `Main.Set(string,int)` is private.

### `-batchmode` / `-nographics`: not used

Neither `Assembly-CSharp.dll` nor `Owlcat.Runtime.Core.dll` references `Application.isBatchMode`, so Wrath has no batch-mode path.
Save loading also goes through UI-driven loading screens (`LoadingProcess` and `RootUIContext.CommonVM.ShowLoadingScreen`).
The script therefore launches the normal windowed game minimized. `-Windowed` adds only standard Unity `-screen-*` arguments.

## What it proves

- RRT loads under UMM with the current DLL and `Story.json`, and `Build()` finishes. The report records `initialized`,
  `error`, the `degraded` relationships and the `warnings`, which are the GLOBAL-01 and GLOBAL-02 blocker symptoms.
- Real saves load with RRT installed, and `State()` does not throw on them.
- Availability is computed per save. This is the in-game counterpart of `tools/rrt_save_probe.py`: diff the two to find
  probe divergences, such as `IsPlaying` or contact units.
- Every driven scene opens, every page shows answers, and every selection runs without exceptions. That covers
  RRT's route conditions and actions, `BookPatch` portraits, the dialog controller and the UI book view (non-headless).
  The run also has no invalid-answer or empty-page errors, and it terminates within the step budget.
- The terminal-choice and `Set`-flag bookkeeping (`RecordProgress`) actually lands in the save's unlockable flags.
- RRT flags survive a real save and load cycle.

## What it does not prove

- **Physical entries in native dialogs, by default.** Without `-Inline`, RRT answers injected into owner answer lists are not
  clicked: scenes are opened directly with `StartDialogWithoutTarget`, and inline scenes (`NativeReturnCue`, `ReturnToList`),
  which have no standalone dialog, are only listed under `ScenesWithoutDialog`. `-Inline` covers them; its own limits are
  listed in [Inline mode](#inline-mode--inline).
- **Skill checks.** Checks roll normally. One walk sees one outcome, so both branches are not guaranteed.
  Plan item 3.2(e), forcing `RuleSkillCheck` outcomes, is not implemented.
- **Rest-triggered and remote queues.** `Main.Update` and the `RestController.Stop` patch are not exercised as triggers.
  The harness opens their dialogs directly.
- **Writing quality.** It does not check localized text quality, portraits' visual correctness or narration audio. It does record answer text.
- **Performance.** There is no frame-time assertion.
- **DFS limits.** DFS is bounded by `MaxPathsPerScene` and does no (node, flags) deduplication.
- **Force mode.** Force mode runs scenes out of their gated state. A failure there can be an artefact of the forced state.
- **Relevance heuristic.** "Relevant" error classification is text-based, so an RRT bug that logs a message without any RRT
  or dialog marker may be missed. It is still in the report.
- **Live runs.** No live run has been made yet. The first run should be watched once, because of possible first-launch modals,
  Steam relaunch, and a save that opens into a cutscene (reported as `NotIdle`).

## How Astra uses it in the loop

1. Edit the story or code, then run `build.ps1` (story, mod, `RulesTests`), `managed-tests` and `tools/rrt_verify.py`. These are the fast offline gates.
2. Run `harness/SelfTest` (seconds). It fails immediately if an RRT refactor renamed a field or method the harness reads.
   Update `RrtBridge.Expectations` when that happens.
3. Run `./harness/run-harness.ps1 -Saves <regression corpus>` with one or two saves per chapter or companion fate, the
   same corpus as `rrt_save_probe.py`. Use the exit code as the gate. On failure, read `Summary.Failures` in
   `harness/.runs/<stamp>/rrt-harness-report.json`. Each failing run has the save, scene, strategy, the answer path to
   replay, the exceptions with stacks, and the archived `Player.log` and `GameLogFull.txt`.
4. To reproduce a failure deterministically, rerun with the same `-Seed`, `-SceneFilter <scene id>` and `-Saves <save>`.
   For branch coverage of one scene, use `-Mode dfs -MaxPathsPerScene 32`.
5. Nightly or pre-release, run `-Force` over a late-game save for crash-hunting across all scenes.

## Inline mode (`-Inline`)

`-Inline` reaches each scene the way the player does: through the native dialog that shows the scene's entry answer.
It targets every scene with a native entry list (`Rules.EntryTargets`: explicit `AnswerLists`, or Anevia's and Irabeth's
lists for Tirabade). That covers the inline-only scenes (`NativeReturnCue`, `ReturnToList`), which the default mode cannot
open at all, and the native entries of scenes that also have their own RRT dialog. Remote, epilogue and hub scenes have no
native entry and are not driven in this mode.

**1. Resolve hosts offline.** After a story or game update, regenerate the hosts file and commit it.
SelfTest fails when the file no longer matches the built RRT's `EntryTargets`.

```powershell
python harness/resolve-inline-hosts.py      # about 20 s; reads blueprints.zip and development/Story.json
```

For each entry list, the resolver finds the cues whose `Answers` show it. The list's `ParentAsset` comes first, then any other
cue holding it directly or through a nested list. It walks each cue's `ParentAsset` chain to its `BlueprintDialog`. It then
computes the shortest click path from the dialog's `FirstCue` to an owning cue over this graph:

- cue answers, with lists expanded;
- `Continue` (one click);
- answer `NextCue`;
- check success and fail, and cue-sequence cues and exit (no click).

Conditions are recorded along the path but not evaluated. The resolver writes `harness/inline-hosts.json` with:

- per scene: kind, lists, entry answer name, and the chosen host;
- per list: every host dialog with its owning cues, speaker unit, reachability, path, and the click distance of every
  native answer on the way.

The current file resolves 750 of 751 entry-target scenes: 130 of 131 inline-only scenes, and 369 of the 370 scenes with
explicit `AnswerLists` and no `ContactUnit`. The exception, `areelu.trickster.audience.notes`, uses a list that no dialog cue shows.

**2. Drive at run time** (`HarnessRunner.DriveInline`). For each target:

1. Choose the first live entry list with a reachable host (fewest clicks). None: `skipped-inline` with the resolver's reason.
2. Force as in a normal run: the scene's `Requires`, one flag per unmet `RequiresAnyGroups` group, the started flag.
3. Start the host as the `StartDialog` action does. When the host's speaker unit (first cue, else owning cue) is loaded in the
   area, use `StartDialogWithUnit(dialog, unit, mainCharacter)`. Otherwise use `StartDialogWithoutTarget(dialog, null, mainCharacter)`.
4. Click toward the list, at most `MaxInlineNavSteps` clicks (`InlineHosts.Pick`, covered by SelfTest). At each click, choose:
   - the entry answer, as soon as it is shown;
   - else the shown answer with the fewest clicks left, least used first;
   - else Continue;
   - else the first least-used unconditioned native answer.

   It never picks Exit or another RRT answer. Each click is logged in `Inline.NavPath` beside the offline `ResolvedPath`.
5. Select `RRT_entry.<scene>`, or `RRT_entry.<scene>.<list>` for a return-to-list scene. With `-Screenshots`, the native
   list is captured first, with the entry on it (`<scene>__list.png`).
6. Wait until a cue of the scene (`RRT_cue.<scene>.*`) is current:
   - an inline scene continues inside the host;
   - a scene with its own dialog is queued by `RouteAction` and started by `Main.Update`.

   It then walks the scene like a direct run: random or DFS, the oracles, and screenshots of scene cues.
   The walk completes when the dialog closes, or when a `native_next` or the return cue hands the conversation back to a native cue.

Results that are not failures are `skipped-inline`, with the reason. The cases are:

- no reachable host;
- the host does not start, is stuck, or ends first;
- the click budget runs out, or only Exit is left;
- the list's own answers are hidden;
- a forced run cannot hold the scene's native or derived keys.

`skipped-delay` is not a failure either: a forced run could not satisfy the scene's `DelayHours` (see below).

`skipped-forbidden` is not a failure either: the save itself already held one of the scene's `Forbids` before the run
(`ForbiddenHeld`), so the page is legitimately closed there. The harness never creates that state: `MarkStarted` does not
set a relationship's started flag when the scene forbids it (a pre-start page such as `chadali.trickster.council.orange`).

**Delayed scenes (`DelayHours`).** `Rules.Available` opens a delayed page only when `DelayHours` have passed since the
latest `hour.<key>` time of its held `Requires` (and held `RequiresAnyGroups` members). A forced run sets those flags
"now", and `Main.RecordLatches` stamps a latch such as `trickster.ever` "now" on the first idle tick after loading a save
that predates it, so the page could never open. A forced run therefore backdates those times (`DelayForcing`): each such
key gets `hour.<key>` = the current hour minus `DelayHours` minus a 2-hour margin, and a held latch is persisted so it is
not re-stamped. Game time is not advanced and the mod's delay rule is unchanged. The run records `DelayBackdated`
(`key@hour`). When the delay cannot be met (the save is younger than the delay, or a blocking key has no `hour.*` flag)
the run records `DelayUnmet`, and a page that then stays hidden is `skipped-delay`. This applies to direct and `-Inline` runs.

Failures are:

- `entry-hidden`: the list is shown but the entry is not, although the scene is available, or all of its `Requires` were forced
  (and its delay backdated);
- `entry-not-started`: the entry was selected but no scene cue followed;
- any exception or oracle failure.

**Known limits.**

- Paths are offline lower bounds. A native cue or answer condition, `ShowOnce`, or a skill check can hide the step the
  navigator wants. The navigator then falls back to Continue or unconditioned answers and may run out of clicks.
- One host per scene per run: the first reachable one. Other hosts of the same list are not tried.
- `StartDialogWithoutTarget` skips proximity and speaker presence, so a host is reachable even where its unit is absent.
  A host whose first cue needs a present speaker may still bark only.
- Contact-unit scenes are driven as well, but their entries also need the contact present (`ContactAvailable`). A forced
  run away from the unit usually ends in `skipped-inline`.
- E16 native openers (`RRT_opener.*`, the Table menu) are not clicked. Table scenes open from the menu view, not from a list.
  `household.table.offered` (the offer itself) is an inline scene and is driven.
- `household.any_eligible` and other derived keys cannot be forced from a save.

**Recommended Table run** (the Ch3 Hiriko Trickster save). It opens a visible window, so warn the user first:

```powershell
./harness/run-harness.ps1 -Saves 'C:\Users\Z\AppData\Local\Temp\claude\C--Users-Z-Documents-Projects-Writer\7b33789b-9992-4a4a-baa6-d771af8d5b6a\scratchpad\saves\Manual_313_Hiriko_The_Trickster.zks' -Force -Inline -Screenshots -SceneFilter @('household.')
```

Add `-DryRun` to see each matching scene's host, owning cue and click count without launching anything.

## Presence hooks (E12/E12c)

`RrtBridge.PresenceReport()` returns one line per presence ("key [mode] wanted; status; click-to-talk attached|not attached"). `RrtBridge.PresenceClick(key)` clicks a presence the way the player would and returns true when its RRT hub dialog started; a live run can assert that the presence appeared and that its hub opens.

## Presence spike (`-Spike Presence`)

The live check of E12d (the quiet copy). Spawn-copy presences are instances of native unit blueprints, and some are
companions: `Camelia_Companion` and `EvilArueshalae_Companion` carry the Player faction, a party AI brain and the
companion's voice set. As spawned natively such a copy joins the party's unit group (`<directly-controllable-unit>`),
shares the party inventory, joins the party's fights and barks the companion's lines. `GuestPresence` now switches every
copy to the Neutrals faction and its own group, sets the native silent `PC_None_Barks` as its `OverrideAsks`, and marks it
`Passive` (re-applied every tick, since `Passive` is not saved). It is opt-in: without `-Spike` nothing changes. With it,
after each save loads (`PresenceSpike.cs`, `PresenceSpikeModel.cs`):

1. If the save is not in Drezen (capital) it loads `DrezenCapital_FromThroneRoom` and waits for idle.
2. For each candidate unit with no live unit in the area it builds a spawn-copy `GuestPresence` 3 m from the Commander and
   ticks it, recording the repairs applied at spawn (`Quiet`), the copy's faction, group, `Passive` flag and asks.
3. It forces each copy's Aggro, Pain, LowHealth, Selected, Discovery and CheckFail barks, then watches for `observeSeconds`
   (20), ticking the presences as `Main.TickPresences` does. A Harmony prefix on `UnitAsksComponent.Bark.Play` (patched in
   presence-spike runs only) records every audible bark (voice event or text) a copy plays; dialogs that start and combat
   are recorded too.
4. It removes the copies and checks their records are gone.

The result is `Saves[i].PresenceSpike`: per copy `NativeFaction`, `NativeAsks` (what it had before E12d), `Faction`,
`PlayerFaction`, `PartyGroup`, `Passive`, `Asks`, `AsksSilent`, `InCombat`, `Barks`, `Removed`; `Dialogs`, `Passed` and
`Findings`. A spike that does not pass is a summary failure. Settings are under `presence` in the plan (`enterPoint`, ""
to stay in the loaded area; `units`, `distance`, `observeSeconds`, `entrySeconds`, `settleSeconds`).

```powershell
./harness/run-harness.ps1 -Build -Saves '<copy of a Ch3 Drezen save>' -Spike Presence -NoRoundTrip -TimeoutMinutes 15
```

## Residence spike (`-Spike Residence`)

The P2 spike of `Writer/handoffs/10-HAREM-RESIDENCE.md`; the static findings and the verdict rules are in
`Writer/handoffs/10b-RESIDENCE-SPIKE.md`. It is opt-in: without `-Spike` the plan has no `spike` key, the harness never
reaches `ResidenceSpike.cs`, and the report has no `Residence` keys. With it, each save is loaded and then, instead of
driving scenes (`ResidenceSpike.cs`, `ResidenceSpikeModel.cs`):

1. **(a) Entry.** It records whether the native closet would still teleport (`Obj_6a_KillNocta` / `Obj_6b_KillCouncil`,
   as `ToCouncil_CheckPassedActions` checks) and the Council etude states, then calls `Game.LoadArea(TricksterCouncil_Enter,
   AutoSaveMode.None)`, which is what `TeleportParty` does for another area. It records whether the load started, the load
   time, and every `ShowPartySelection`, `StartCombat`, `PlayCutscene` and `TeleportParty` action that runs meanwhile
   (Harmony prefixes that only record, patched in spike runs only).
2. **(b) Preset.** After up to `SettleSeconds` it records the idle blocker, game mode, combat, the addon mechanics the
   etudes loaded (`EtudesSystem.GetActiveAdditionalMechanics`), the preset they match (`Default` = Council1 + NoCouncil,
   `NoCouncil`, `base` or `other`), the etude states again and every non-party unit in the area. A native dialog still
   open is noted and closed so that (c) is measured on its own.
3. **(c) Presence.** It builds a spawn-copy `GuestPresence` (RRT's own engine, by reflection: `RrtBridge.SpikeExpectations`)
   for the first candidate unit with no live unit in the area, at the seat (default `Locators/CouncilLoc3`, 0/0/3.92,
   facing 180), and ticks it as `Main.TickPresences` does. It checks the copy exists, has an active view, is rendered
   (required only with `-Screenshots`, which gives a rendered window), walks at least 2 m toward `Locators/CouncilLoc2`
   under a `UnitMoveTo`, and that an RRT presence hub dialog starts with it as the target unit. It then ticks the presence
   unwanted and checks that the copy and its `Player.SettingsList` record are gone.
4. With `-Screenshots` it saves `residence__entry.png`, `residence__presence.png` and `residence__dialog.png` in the shots folder.

The result is `Saves[i].Residence` in the report: `EntryOk`, `PresetOk`, `PresenceOk`, `Passed` and `Findings`, which lists
each failed check prefixed with (a), (b) or (c). A spike that does not pass is a summary failure (exit code 1). That is a
feasibility answer, not a harness defect. Nothing is saved, so the area change and the copy are discarded. The settings are
under `residence` in the plan (`enterPoint`, `seat`, `pathTo`, `units`, `entrySeconds`, `settleSeconds`, `pathSeconds`,
`pathMinMetres`); `run-harness.ps1` uses the defaults.

```powershell
./harness/run-harness.ps1 -Build -Saves '<copy of Manual_339_Trickster_Ending_Act_5.zks>' -Spike Residence -Screenshots -NoRoundTrip -TimeoutMinutes 20
```
