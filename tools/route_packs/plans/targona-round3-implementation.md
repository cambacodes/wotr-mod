# Targona round 3

Scope: `targonar2.json`, checked against the merged route and shared endings.
No new costs, attraction requirements, commitment requirements, return devices,
or reconciliation conditions. No shared source edits. No commit, as requested.

## CHANGES / finding disposition

Audit defects are numbered in their JSON order. No audited finding was already
fixed in the current source; generated gate verification is recorded below.

| Finding | Status | Disposition |
| --- | --- | --- |
| CAN cap; 1, repeatable Herald recap | ESCALATED | Cue_0126 remains native; it is absent from the runtime replacement whitelist. Requires a reviewed `src/NativeEpilogueEdit.cs` contract and a route-owned Trickster-only replacement after `free.met`, retaining the injured-wing history and the original before arrival/off Trickster. |
| 2, laboratory drawing | ESCALATED | Generated Areelu availability conditions originate in the shared presence classifier, not the route answer. Historical captivity needs a scoped reference classification. |
| 3, paper-fold check | ESCALATED | Generated Irabeth absence veto originates in the same classifier. Her old report is a recollection. |
| 4, publication / Areelu | ESCALATED | Scene-level veto needs a historical-perpetrator classification in the shared classifier. |
| 5, publication / Irabeth | ESCALATED | Scene-level veto needs a past-report classification there. |
| 6, ordinary wand / Iomedae closure | ESCALATED | A chaplain's work is being classified as the goddess's participation. No authored closure requirement exists to remove. |
| 7, ordinary dawn / Iomedae presence | ESCALATED | A visiting unnamed celestial healer is being classified as Iomedae's participation. Retain the HeraldKilled split when fixing the classifier. |
| 8, dawn refusal / prayer | ESCALATED | Shared classifier treats "Iomedae keep me" as participation. |
| 9, tended refugees / blessing | ESCALATED | Shared classifier treats invocation as participation. |
| 10, unasked refugees / prayer | ESCALATED | Same class, independent answer. |
| 11, normal arrival memory | FIXED | `storylines/targona_trickster.py`: ordinary greeting keeps its identity and receives the charges-spent condition; appended UMD2 greeting recalls personally working the wand. |
| 12, physician arrival memory | FIXED | Same split, retaining recognition of the physician and Heaven departure. |
| 13, correspondence-first arrival memory | FIXED | Same split, retaining the wayhouse address and correspondent recognition. |
| 14, unprepared Lariel oath | FIXED | First vigil prepares her concern before either postponement. Second asking explicitly recalls that concern; original promise/refusal effects remain intact. |
| BEL cap; 15, spoken entry plea | ESCALATED | `storylines/lastcall_partners.py` remains prohibited. Change only Targona's call entry to neutral contemplation; spoken pleas belong exclusively to calling/breaking answers. |
| 16, false oath-kept furlough | ESCALATED | Depends on 15. Existing called/not-called readers are structurally appropriate once the entry is repaired. Do not certify the outcome while its complete spoken history contradicts it. |
| 17, false oath-kept Last Call coda | ESCALATED | Same dependency, separately verify the kept and broken sequences in the shared page. |
| 18, stale C# slot assertion | FIXED | `tests/TargonaTricksterTests.cs`: both first nights require threshold -> effect-free explicit slot -> morning; existing commitment walks and night receipts remain checked. |
| 19, epilogue present tense | FIXED | Past-tense heated cut in `storylines/targona_trickster.py`; existing brief uses `narration: third-past` and matching past-tense anchor/example. |

The new arrival recollections are authored dialogue about the already implemented
paid ward night. They reveal its work, never the concealed unspent charge count.
The Lariel setup is authored characterization of her existing promise, not new lore.
No local `voice_locks.json` exists; the discoverable voice-lock worktree's registry
is empty. No explicit prose was generated; all five existing slot addresses remain.

## CLASS SWEEP

- All five original arrival variants and all their explanations checked. Legacy
  laboratory greetings already recall the shared tending work without claiming
  the ordinary cost; their explanations now fit either night. Three new nodes and
  three appended entry answers cover the affected greetings, preserving old order.
- Both postponements encounter the Lariel setup; both first-night slots retain
  effect-free continuations and the original morning receipt.
- Both oath-kept readers and the shared call entry checked as one situation.
  All three remain escalated rather than hiding the mismatch behind another gate.
- All nine history/prayer surfaces reviewed together; no prose evasions, global
  guard bypasses, or changes to other romances were introduced.
- All five explicit-slot briefs/addresses checked; only the epilogue register
  needed a change. Existing source line-ending styles retained byte-for-byte.

## GATE

`PYTHONHASHSEED=0`; game data `/wrath`; `RRT_PARENT_BINDINGS` contains the same
four existing manifests as `build-expansion.ps1`. `$TMP` below denotes the task's
system temporary directory. Export and reports are never written to development.

- `RRT_STORY_OUTPUT=$TMP/Story.json python expansion.py`: PASS, 3,848 scenes;
  generator labels this an incomplete development export (its existing label).
- `python tools/savecompat.py --story $TMP/Story.json`: PASS, 0 hard failures.
- `python tools/payoff_lint.py --strict --story $TMP/Story.json`: PASS, 42 routes,
  0 hard failures; existing advisory review notes remain.
- `python tools/departure_lint.py --strict --story $TMP/Story.json`: PASS,
  43 women, 0 hard failures; existing advisory review notes remain.
- `RRT_TEST_STORY=$TMP/Story.json python -m unittest
  tests.test_targona_round2 tests.test_targona_round3 tests.test_utf8_io -q`:
  PASS, 11 tests, 1 existing expected failure for the shared history classifier.
- `python -m unittest discover -s tests -p "test_*.py" -q`: BLOCKED, exit 143.
  `/work/testguard.sh` explicitly terminates discovery in `RRT-r3-*` worktrees;
  `/work/testguard.log` records this worktree's killed command. No pass claimed.
- `dotnet build tests/RulesTests.csproj -c Release` with intermediate/project
  extension/output properties pointing to `$TMP`: PASS, 0 errors, 8 existing
  unassigned-field warnings. No repository obj/bin directories were created.
- `dotnet run --project tests/RulesTests.csproj -c Release -- $TMP/Story.json`
  with external paths exported as MSBuild environment properties: BLOCKED,
  exit 143, terminated by the same guard. The first launch attempts used command
  line output properties, but .NET's run phase ignored those and could not find
  its executable; exported properties corrected the path before guard termination.
- `dotnet $TMP/bin/Release/net8.0/RulesTests.dll
  --suites=TargonaOpeningTests,TargonaTricksterTests $TMP/Story.json`: BLOCKED,
  exit 143. The guard matches `RulesTests` even with filtered suite selectors.
- `python tools/rrt_verify.py --strict --story $TMP/Story.json` with explicit
  report paths in `$TMP`: result pending.
- Direct base/current comparison: all scene and old node order preserved;
  all 158 legacy choice targets, effects and costs preserved. Only three existing
  greeting entry conditions gained the already-earned cost discriminator;
  alternate answers and nodes append. CRLF/LF source styles preserved.
- `git -c core.whitespace=cr-at-eol diff --check`: PASS.

Generated story, verifier reports, logs and .NET outputs are deleted after results
are recorded. No full build, game, harness or commit.

## ESCALATE

The CAN and BEL caps remain unresolved for the shared ownership reasons above.
The history/prayer class needs `tools/crossroute_checks/mention_context.py` (or an
equivalent shared scoped-reference contract), outside this task's editable files.
The native cue requires a runtime policy outside this task's editable files.
The promise entry requires the expressly prohibited shared Last Call file.
Full Python discovery and C# execution require coordinator resolution of the
external testguard's writing-job restriction. It was not changed or bypassed.

## PROPOSE

None beyond the exact escalated audit repairs. No design changes implemented.

## RISKS

This round does not claim the >=91 bar: the native recap, unrelated availability
guards and false oath-kept sequences remain blocked by shared ownership. No
independent rescore was run. Gate results below do not certify narrative quality.
