# ENGINE F8: integrated ideal-run reachability regression

Base: `claude/eng7-integ`, `3a38c84`. Worktree: `/work/wt/RRT-eng7-f8`.
Date: 2026-10-04. No production engine or story changes were needed.

## Result

Both corrected combined histories reach **45/47 relationships in the original
baseline roster**, including Last Call. The integrated export adds `foresight`,
so its raw total is **46/48**, with only Ember and Aivu excluded. Against that
same original roster, the unchanged kit initially reached **44/47** (raw
45/48): Delamere alone regressed. All other in-scope commits stayed within their
original chapter limits in both profiles.

| Profile | Original kit | Corrected kit | Last Call before -> after | Delamere before -> after |
|---|---|---|---|---|
| Default: Ch3=30, Ch4=12, Ch5=40, Ch6=45 | 44/47 baseline; 45/48 raw | 45/47 baseline; 46/48 raw | day 114 -> **115**, Ch6 | no -> **day 16**, Ch3 |
| `CHDAYS=3:80,5:30`; Ch4=12, Ch6=45 | 44/47 baseline; 45/48 raw | 45/47 baseline; 46/48 raw | day 154 -> **155**, Ch6 | no -> **day 16**, Ch3 |

Last Call plays **all 22 creditor call-ins**, including `delamere.lastcall.call`,
then `trickster.lastcall.last_joke`. The paid Foresight page is taken through
the executed `trickster.foresight.page` choices on day 10; it is not forced by
a native fixture and does not replace any woman's earned device.

### Per-relationship status

Each yes cell gives **sim day / chapter**. 80/30 means Ch3=80 and Ch5=30.
Foresight is the additional integrated relationship.

| Relationship | Original kit, default | Corrected kit, default | Original kit, 80/30 | Corrected kit, 80/30 |
|---|---|---|---|---|
| `tirabade` | yes: 55 / Ch5 | yes: 55 / Ch5 | yes: 105 / Ch5 | yes: 105 / Ch5 |
| `seelah` | yes: 53 / Ch5 | yes: 53 / Ch5 | yes: 103 / Ch5 | yes: 103 / Ch5 |
| `konomi` | yes: 54 / Ch5 | yes: 54 / Ch5 | yes: 104 / Ch5 | yes: 104 / Ch5 |
| `jerribeth` | yes: 52 / Ch5 | yes: 52 / Ch5 | yes: 102 / Ch5 | yes: 102 / Ch5 |
| `kiana` | yes: 66 / Ch5 | yes: 66 / Ch5 | yes: 116 / Ch5 | yes: 116 / Ch5 |
| `ember` | no (excluded) | no (excluded) | no (excluded) | no (excluded) |
| `soana` | yes: 58 / Ch5 | yes: 58 / Ch5 | yes: 108 / Ch5 | yes: 108 / Ch5 |
| `arsinoe` | yes: 25 / Ch3 | yes: 25 / Ch3 | yes: 25 / Ch3 | yes: 25 / Ch3 |
| `targona` | yes: 17 / Ch3 | yes: 17 / Ch3 | yes: 17 / Ch3 | yes: 17 / Ch3 |
| `gesmerha` | yes: 20 / Ch3 | yes: 20 / Ch3 | yes: 20 / Ch3 | yes: 20 / Ch3 |
| `vellexia` | yes: 59 / Ch5 | yes: 59 / Ch5 | yes: 109 / Ch5 | yes: 109 / Ch5 |
| `aivu` | no (excluded) | no (excluded) | no (excluded) | no (excluded) |
| `aranka` | yes: 20 / Ch3 | yes: 20 / Ch3 | yes: 20 / Ch3 | yes: 20 / Ch3 |
| `anevia` | yes: 54 / Ch5 | yes: 54 / Ch5 | yes: 104 / Ch5 | yes: 104 / Ch5 |
| `irabeth` | yes: 56 / Ch5 | yes: 56 / Ch5 | yes: 106 / Ch5 | yes: 106 / Ch5 |
| `minagho_chivarro` | yes: 59 / Ch5 | yes: 59 / Ch5 | yes: 109 / Ch5 | yes: 109 / Ch5 |
| `nocticula` | yes: 94 / Ch6 | yes: 94 / Ch6 | yes: 134 / Ch6 | yes: 134 / Ch6 |
| `nocticula.acquisition` | yes: 54 / Ch5 | yes: 54 / Ch5 | yes: 104 / Ch5 | yes: 104 / Ch5 |
| `nurah` | yes: 17 / Ch3 | yes: 17 / Ch3 | yes: 17 / Ch3 | yes: 17 / Ch3 |
| `dorgelinda` | yes: 54 / Ch5 | yes: 54 / Ch5 | yes: 104 / Ch5 | yes: 104 / Ch5 |
| `hepzamirah` | yes: 59 / Ch5 | yes: 59 / Ch5 | yes: 109 / Ch5 | yes: 109 / Ch5 |
| `camellia` | yes: 55 / Ch5 | yes: 55 / Ch5 | yes: 105 / Ch5 | yes: 105 / Ch5 |
| `eritrice` | yes: 18 / Ch3 | yes: 18 / Ch3 | yes: 18 / Ch3 | yes: 18 / Ch3 |
| `areelu` | yes: 96 / Ch6 | yes: 96 / Ch6 | yes: 136 / Ch6 | yes: 136 / Ch6 |
| `longcon` | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 |
| `chadali` | yes: 26 / Ch3 | yes: 26 / Ch3 | yes: 26 / Ch3 | yes: 26 / Ch3 |
| `arueshalae` | yes: 63 / Ch5 | yes: 63 / Ch5 | yes: 113 / Ch5 | yes: 113 / Ch5 |
| `devarra` | yes: 19 / Ch3 | yes: 19 / Ch3 | yes: 19 / Ch3 | yes: 19 / Ch3 |
| `delamere` | **no** | yes: 16 / Ch3 | **no** | yes: 16 / Ch3 |
| `kaylessa` | yes: 24 / Ch3 | yes: 24 / Ch3 | yes: 24 / Ch3 | yes: 24 / Ch3 |
| `mielarah` | yes: 61 / Ch5 | yes: 61 / Ch5 | yes: 111 / Ch5 | yes: 111 / Ch5 |
| `nidalynn` | yes: 52 / Ch5 | yes: 52 / Ch5 | yes: 102 / Ch5 | yes: 102 / Ch5 |
| `shamira` | yes: 63 / Ch5 | yes: 63 / Ch5 | yes: 113 / Ch5 | yes: 113 / Ch5 |
| `jannah` | yes: 63 / Ch5 | yes: 63 / Ch5 | yes: 113 / Ch5 | yes: 113 / Ch5 |
| `nenio` | yes: 13 / Ch3 | yes: 13 / Ch3 | yes: 13 / Ch3 | yes: 13 / Ch3 |
| `herrax` | yes: 43 / Ch4 | yes: 43 / Ch4 | yes: 93 / Ch4 | yes: 93 / Ch4 |
| `terendelev` | yes: 64 / Ch5 | yes: 64 / Ch5 | yes: 114 / Ch5 | yes: 114 / Ch5 |
| `eliandra` | yes: 71 / Ch5 | yes: 71 / Ch5 | yes: 121 / Ch5 | yes: 121 / Ch5 |
| `galfrey` | yes: 58 / Ch5 | yes: 58 / Ch5 | yes: 108 / Ch5 | yes: 108 / Ch5 |
| `horzalah` | yes: 57 / Ch5 | yes: 57 / Ch5 | yes: 107 / Ch5 | yes: 107 / Ch5 |
| `elyanka` | yes: 63 / Ch5 | yes: 63 / Ch5 | yes: 113 / Ch5 | yes: 113 / Ch5 |
| `melazmera` | yes: 56 / Ch5 | yes: 56 / Ch5 | yes: 106 / Ch5 | yes: 106 / Ch5 |
| `yaniel` | yes: 63 / Ch5 | yes: 63 / Ch5 | yes: 113 / Ch5 | yes: 113 / Ch5 |
| `wenduag` | yes: 54 / Ch5 | yes: 54 / Ch5 | yes: 104 / Ch5 | yes: 104 / Ch5 |
| `iomedae` | yes: 55 / Ch5 | yes: 55 / Ch5 | yes: 105 / Ch5 | yes: 105 / Ch5 |
| `lastcall` | yes: 114 / Ch6 | yes: 115 / Ch6 | yes: 154 / Ch6 | yes: 155 / Ch6 |
| `foresight` | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 |
| `household` | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 | yes: 10 / Ch3 |

### Chapter budget

| Chapter | Default: needed / available rests | Default load | 80/30: needed / available rests | 80/30 load |
|---|---|---|---|---|
| 0 | 0 / 1 | 0.00 | 0 / 1 | 0.00 |
| 1 | 0 / 3 | 0.00 | 0 / 3 | 0.00 |
| 2 | 1 / 9 | 0.11 | 1 / 9 | 0.11 |
| 3 | 15 / 45 | 0.33 | 15 / 120 | 0.12 |
| 4 | 10 / 18 | 0.56 | 10 / 18 | 0.56 |
| 5 | 42 / 60 | 0.70 | 41 / 45 | 0.91 |
| 6 | 2 / 67 | 0.03 | 2 / 67 | 0.03 |

No chapter is over its rest budget. The 80/30 profile's Ch5 commits finish by day
121 (Eliandra), before Ch5 ends at day 132; its Chapter 6 begins on day 132.
Three optional scenes miss their windows in both corrected runs:
`shamira.trickster.mind.council`, `iomedae.trickster.dream.summit`, and
`iomedae.trickster.platform.bare`. None gates a commitment.
The corrected default log contains 1,057 executed scenes.

## CHANGES

### F8-1: Delamere — valid guard; outdated native script (case a)

**Exact blocker:** `delamere.tomb_book_locked`, required by all crypt waking
siblings at `storylines/delamere_trickster.py:449`, `:453`, and `:457`.
The composite is defined at `:125`; its native SelectedAnswers witnesses
are bound at `:147-148`. Mere `tomb_visited` and `kyado.initiated` do not
produce it. No engine predicate was relaxed.

**Spec evidence:** `/work/Writer/handoffs/trickster/delamere.md:298` (polish
r4) explicitly requires the native Book to lock before each living crypt waking:
“every crypt waking ... now requires the native Book locked”. It also says the
Book locks via **Close**, Answer_0060 or Answer_0059, after relic disposition.
This is a legitimate earned gate under Binding context (5), and prevents the
native corpse Book from contradicting the authored living return under the
DLC-tier rewrite rule.

**Canon verification:** inspected `/wrath/blueprints.zip` and
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`, using the actual
`World/Dialogs/c3/TempleOfDelamere/TombOfDelamere_BookEvent/` records:

| Guide action | Native evidence |
|---|---|
| Break the seal | Answer_0023 `a8596bc7d5d4766409809333280b15b1` leads to BookPage_0043 `2ad1cdc92a2fab84aa62782400f8a74d`; Cue_0040 `1c9182d585e1d4d4c85c574695337ccb` shows the body. |
| Leave the relics; close the lid | Answer_0050 `6a5d2bcd0a6d09249bb3e62c2d1556c2` returns to that page; Cue_0054 `15a598eac4625c84190a1574bc50597d` reads that selected answer. No move-to-Drezen answer is taken. |
| Close the Book | Answer_0059 `173de7e4c8e237d409e3e08f1461b6fb` has the localized text “Close.” and is shown after Answer_0050. Its SwitchInteraction disables Sarcophagus `4576ac76-8c7f-4b37-af54-027f6a28fc13`. |
| Native self-lock | Dialog `96993dc62aebc38469f890b857173117` requires NOT(Answer_0060 OR Answer_0059 selected); neither lock is mod-authored. |

**Changed file:** `tools/ideal-run-kit/natives/delamere.txt:5` adds the four
actual native observations from that sequence in Ch3. The existing opening,
remains disposition, live Trickster gate, refusal and costs remain intact.

### F8-2: kit sweep — Dorgelinda's preparation was injected, not executed

The original `w6/dorgelinda.extra.txt` and `w6/combined.extra.txt` both wrote
the authored `dorgelinda.trickster.cost.carts_signed` after countersign, while
the log actually chose `sign/1` (“Hand the pen back”), whose Set is empty.
That is not evidence of an earned preparation even though she committed.

**Spec evidence:** `/work/Writer/handoffs/trickster/dorgelinda-stranglehold.md:79-97`
requires writing the rider at Logistics_4; backing out writes no flag.
Production choices at `storylines/dorgelinda_trickster.py:116-122` show that
the rider's terminal answer produces the cost.

**Changed files:** `tools/ideal-run-kit/natives/dorgelinda.txt:9` steers away
from the back-out choice using the kit's existing `-choice` mechanism. Both
`tools/ideal-run-kit/w6/dorgelinda.extra.txt` and
`tools/ideal-run-kit/w6/combined.extra.txt` remove the injected cost. The
native tribunal observation still follows the countersign scene. Both final
logs now execute `sign/0 -> rider/0`, whose Set earns `carts_signed`.
No route mechanics, costs or requirements were changed.

### F8-3: reproducible kit and regression

- `tools/ideal-run-kit/`: copies all 56 source-kit files. The other 51 files
  are byte-identical. The supplied Windows-only runner could not directly read
  this Linux worktree; the initial runs used a temporary copy with only its
  worktree paths adapted and its HERE pointing at the original Writer kit.
- `tools/ideal-run-kit/final_sim.py:15-20`: resolves this repository from the
  runner path, allowing the versioned kit to run from any working directory.
  At `:64-69`, rejects non-native flags in plain, timed, never, off and
  after-scene scripts, so a scripted cost/return cannot masquerade as earned.
  The existing availability mirror, planner scoring, 80-node depth policy,
  chapter lengths, successful checks and native-list skips are retained.
- `tools/ideal-run-kit/README.md`: reproduction commands and simulation limits.
- `tests/test_ideal_run_regression.py`: both complete combined histories;
  every original in-scope commit before its chapter closes; Last Call days and
  all 22 call-ins; executed Foresight and Dorgelinda choices; all three crypt
  waking siblings with both native locks, missing/unopened lock, closed route,
  off-Trickster and native move-order negatives.
- `tools/ideal-run-regression.md`: this reviewable result and evidence table.

## CLASS SWEEP

- All 48 relationship outcomes compared in both original and corrected runs;
  the original 45 required commits are checked against their guide chapters.
  Delamere was the only new missed commit; none slipped across a chapter limit.
- All three crypt-waking predicates (`crypt.stag`, `crypt.stag_alone`,
  `crypt.stag_late`) checked, including both Book-lock witnesses and the
  distinct Drezen destination guard. Existing managed
  `Trk_Delamere_BookLocked` tests cover the same lock and move-order class.
- Every active native scheduling class checked against Model.native.
  The only authored injection was Dorgelinda's cost, present in both extras.
  The preserved underscore-prefixed alternative histories are not loaded.
- Original kit newline bytes retained, including the source's mixed endings
  in `w6/combined.extra.txt`; unchanged files compared byte-for-byte.
  No scene, node, relationship or choice ID/index was changed.
- Binding contexts (1)-(5) remain enforced by the existing guards. The kit
  earns a native gate; it grants no player-kill reversal or free return,
  changes no off-Trickster canon and adds no echo/prose.

## GATE

All Python commands use `PYTHONHASHSEED=0`; blueprint checks use `RRT_GAME_DIR=/wrath`.
The regeneration also supplies the four parent binding manifests listed in
`build-expansion.ps1` (expansion, Nurah, Nurah runtime cues, and Terendelev).

| Command | Result |
|---|---|
| `PYTHONHASHSEED=0 python expansion.py` | Exit 0; 2,888 scenes generated. |
| `python tools/ideal-run-kit/final_sim.py /tmp/out.json` | Exit 0; 45/47 original roster, 46/48 raw; Last Call day 115. |
| `CHDAYS=3:80,5:30 python tools/ideal-run-kit/final_sim.py /tmp/out.json` | Exit 0; 45/47 original roster, 46/48 raw; Last Call day 155. |
| `python -m unittest discover -s tests -p test_ideal_run_regression.py -q` | Exit 0; 2 tests, including both combined runs and both sides of the crypt gate. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | Exit 0; **352 tests passed**, no skips, with installed blueprint data. The pre-edit run passed 350 tests (5 skipped); the final run includes the two F8 regressions and all native-data cases. |
| `python tools/rrt_verify.py --strict` | Exit 0; **0 hard failures**, including 1,241 native GUID/type checks and 225 inline return-safety checks. Re-run after kit/test edits: 0 hard failures. |
| `python tools/crossroute_lint.py --strict` | Exit 0; **0 new findings** (2,792 existing baseline findings), repeated after edits. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | Fails solely on the expressly allowed base `areelu:008/extraction continuity` scenario; 68 E-Q7-12 scenarios executed, 1 failed. **No Page has no selectable answers failure**. All preceding route/rules checks ran. |
| `git diff --check` | Exit 0. |

The .NET command redirects `BaseOutputPath`, `BaseIntermediateOutputPath` and
`MSBuildProjectExtensionsPath` via environment variables to the system-temp
scratch directory. This keeps obj/bin outside the repository while retaining
the requested standard rules runner. An initial command-line property attempt
built outside the repo but the .NET CLI tried launching the default repo path;
rerunning with environment properties resolved that invocation issue.

## ESCALATE

No F8 engine predicate or shared-code change is needed. The expressly allowed base `areelu:008/extraction continuity` remains for coordinator-owned Areelu work: post-extraction introductions are missing for TE_Final/Cue_3 (`a9510daab8a04163933d9ecaeffac563`), Cue_0017 (`f8d2b851faecddf448fe18db41e17120`), Cue_0020 (`1c8a6796436a7164fa9d63ec79e0395a`), and GrandFinal/Cue_0088_TricksterAree1 (`0fa64f1d24f706d41b09dee83acf621d`). No Areelu/shared entries were edited.

## PROPOSE

None. No new mechanics, gates, costs or route redesigns proposed or implemented.

## RISKS

- This is a rules/scheduling regression, not a live native progression proof.
  The kit assumes the guide's native actions succeed, adequate resources,
  every skill check succeeds, daily physical visits, and the specified inline
  lists are actually opened. No harness, build-expansion.ps1 or game was run.
- Default Ch3=30 is the original simulator stress case. Native Seelah
  progression needs about 75 days; the Ch3=80/Ch5=30 run is the campaign-length
  case. Chapter 6's 45 simulated days serialize pages that the real Threshold
  answer list offers consecutively; they do not require 45 real campaign days.
- The pre-existing Greybor native-script chapter conflict remains harmless:
  Ch2 and Ch3 both request recruitment; the runner takes the earlier Ch2.
- Ember (`ember.present` missing) and Aivu (`azata` missing) are the two
  unchanged, explicitly excluded friendship-route misses. No additional
  relationship is accepted as legitimately unreachable.
- Generated `development/Story.json` was used only for the mandated export
  and checks, then restored to keep all retained edits within the allow list.
  Regenerate before reproducing. All scratch logs, exports and .NET artifacts
  were placed in system temp and removed before handoff; no commit was made.
