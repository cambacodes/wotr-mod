# Recovery implementation report

Baseline `6b313d36`, worktree `claude/recovery`. Read the binding polish prompt,
writing guide, Trickster rubric, newest Camellia/S04 reports, later route history,
registry rule and voice-lock manifest before recovery. Source remains uncommitted
under the final instruction, **“Do not git commit.”** The Camellia no-fast-forward
merge is resolved and staged, with its merge parents retained for coordinator review.

## CHANGES

### A — Camellia round one, preserving later integration

Recovered `origin/claude/polish-camellia` (`ab94d567`) with a no-fast-forward,
no-commit merge. Kept the later `731231c6` round-two integration and `750a3e49`
Last Call held-flask rule. Generated native fixture changes were discarded;
`InventoryFixtureMutationTests.cs` retains HEAD without a diff.

| File | Finding and resulting change |
|---|---|
| `storylines/camellia_cards.py` | Recover informed Mireya alternatives, branch-specific deck endings and encounter callbacks. |
| `storylines/camellia_days.py` | Recover this-dance morning receipts and branch-specific memories. |
| `storylines/camellia_evenings.py` | Recover distinguishable breakfast recollections and continuity prose. |
| `storylines/camellia_last.py` | Recover personal living-refusal closure without romantic fulfilment. |
| `storylines/camellia_masks.py` | Recover informed spirit dialogue without asserting Mireya exists. |
| `storylines/camellia_native.py` | Recover native-context prose and verified identity exposure. |
| `storylines/camellia_trickster.py` | Recover confirmed-corpse guards, prepared/unprepared fallback distinction, breath-before-return receipts and actual sexton payment. Fix the old gate-red derived death clock using the already integrated `native_death_observed` latch; both 72-hour hosts still require current execution/death evidence. |
| `storylines/camellia_intimate_aftermath.py` | Keep later round-two integration and recovered specific breakfast questions/callback continuation. Existing explicit cut slots remain. |
| `storylines/camellia_round2.py` | Reuse five overlapping informed nodes rather than emitting duplicate IDs; retain round-two saved answer order. Preserve both native disclosure and recovered amulet knowledge arms. Make the two appended oath fallback answers exclusive of the original answers, retaining every index. |
| `storylines/lastcall_partners.py`, Camellia paragraph 3 only | Recover the corked-death wording while retaining the current `lastcall.bottled_held` guard. |
| `tests/CamelliaPolishTests.cs`, `CamelliaTricksterTests.cs`, `PacingPP2Tests.cs`, `test_intimacy_contract_lint.py`, `test_recovery.py` | Restore round-one acceptance, adapt to existing native timestamp and later informed-choice/explicit-cut slots. Test genuine fresh death timing, payments, living refusals, unresolved combat, current bodies and preserved saved targets. |
| `tools/return_provenance_contracts.json`, `payoff_contracts.json`, `departure_contracts.json` | Classify the prepared return producer, coffin acquisition variant and present living-refusal closure; do not treat closure as romance payoff. |

### B — S04 registry recovery

| File | Finding and resulting change |
|---|---|
| `storylines/harem_rows/s04.py` | Recover row from `origin/claude/hi-S04` (`c64100e4`) through the existing auto-discovery registry. Its `register(payload, scenes, refs)` owns only this row; no `story.py`, shared household or registry edit. |
| `tests/test_harem_row_s04.py` | Recover refusal/abort, blockers, current-body and repeat-registration acceptance. |
| `tools/route_packs/harem/s04.md` | Recover the implementation/canon contract and its explicit missing success dependencies. |
| `tools/harem_wave1_contracts.json`, `departure_contracts.json` | Classify the new scene and both physical participants. No postwar, Ledger or Last Call success reader claimed. |

S04 retains the branch's reviewed safe subset: root answers 3/4 are refusal and
effect-free postponement. Religion/confession/Word success remain behind the
branch's unproduced authoring blockers. No DC, confession producer, successful
resolution, retry tool, attraction or reconciliation condition was invented.
Seelah's suspicion never becomes proof of murder; Camellia remains unrepentant.

### C — abandoned patches

The [triage](recovery-triage.md) covers all **16 patches / 250 hunks** with
file-local hunk numbers, patch lines, original headers, decision, commit evidence
and disposition: 160 SUPERSEDED; 90 LOST, including applied/adapted and explicitly
deferred dependencies. These counts describe hunks, not new gameplay features.

| File | Recovered lost finding |
|---|---|
| `storylines/crossroute_presence.py`, `tests/test_crossroute_presence.py` | Append the missing Seelah soul-rescue aftercare ending when Arsinoe is unavailable, preserving original answer slots. Retain the later `eb1667dc` proof/edge traversal. |
| `storylines/minagho_chivarro_continuation.py`, `tests/ParentEndingRulesTests.cs`, `managed-tests/ParentEndingIntegrationTests.cs` | Scope ordinary native replacements and all three loss rules to the live Trickster path. Retain earned invitation/death/payoff rules; test none/failed/dragon/legend/swarm, seen/unseen loss, and current native death evidence. Managed positive fixture now supplies the required path. |
| `storylines/arueshalae_hours.py` | Replace the still-unchanged Abyssal wait-for-sleep quarrel reference with turning one's back. No clinic/doctor framing restored. |
| `storylines/horzalah_guild.py` | Missed-shelves letter names the missed visit rather than assuming the Commander went away without saying goodbye. |
| `storylines/konomi_trickster.py`, named Konomi entry in `lastcall_partners.py`, `tests/test_recovery.py` | Recover envoy exclusion from romantic eligibility/coda while preserving political openness and the paid call. Do not restore obsolete historical departure exclusions. |
| `storylines/herrax_house.py`, `herrax_trickster.py`, `tests/test_recovery.py` | Recover pre/post-palace recollection using native `Nocticula_main/Cue_0022` (`30469883ce1583743a6b4228d24778bc`, enGB `506700c3-85e0-4399-a683-567a795c4c5f`). Keep saved `joke` answer 0/`end`, retire it on the Trickster host, append new continuations/nodes. No native audience is manufactured. |
| `storylines/wenduag_trickster.py` | Recover the field-charm/wound explanation, remove narrated Commander quotation and unsupported elapsed-time claims, retain Savamelekh's actual hall/body context, and correct street burial/watch chronology. Exclude the patch proposed new 50-Finances charm fee/flag; existing checks, outcomes, prices and receipts remain. Sweep the sibling before-noon claim too. Do not revive the later-discarded Kerz transport proposal. |

### Strict gate findings

The first completed full verifier exposed two nested narration tags in the
recovered Camellia Last Call paragraph, a new Wenduag vocabulary-budget hit, and
four unchanged Areelu male-visitor references misclassified as Commander gender.
Removed only the redundant Camellia inner tags (`page_p` supplies narration);
recast Brask wanting permission for a corpse-head display as wanting the head;
added four exact, occurrence-bounded male-NPC explanations in
`tools/player_text_exceptions.json`. Both Areelu passages retain their existing
prose and voice locks. `tests/test_recovery.py` proves the exceptions still reject
a real gendered Commander claim and that Wenduag stays within its existing
vocabulary budget. No therapy budget was increased.

## CLASS SWEEP

- Camellia: all five overlapping informed IDs; native disclosure/amulet versus
  ignorance; three encounter suffixes; all timed coffin hosts; unresolved kill,
  battlefield death, stale death timestamp and present body; prepared/unprepared
  bargain; actual gold payment/refusal; living terms/test versus early closure;
  all Nurah/Soana/Kaylessa oath routing arms; breakfast outcomes and explicit-cut
  continuations. Later round-two prose and saved answer positions remain.
- S04: both directed enmity overrides, both native/returned physical bodies,
  later loss/closure, chapter/path/Table/payment gates, root refusal versus abort,
  repeated registry invocation and each blocked success position.
- Chivarro/Minagho: all ordinary cue edits and all three loss rules; every path
  loss, both seen states, containing-page suppression and survivor precedence.
- Recovered prose: Herrax palace knowledge before/after actual native dismissal;
  Konomi romance versus political paid call; Seelah aftercare with/without
  Arsinoe; Horzalah missed-visit chronology; Wenduag Kenabres, Savamelekh and
  street-device siblings. Rejected old transporter assumptions across branches.
- Reviewed every recovery hunk against later polish/r2/r3 work and voice locks.
  No locked Melazmera/Hepzamirah scene or lock manifest changed. No foresight,
  echo, new happy-path push or new explicit act added. The later DLC cut nodes
  remain; stale tests were adapted to their continuations, not their old prose.
- Existing CRLF/LF conventions are retained. No scene/node/relationship ID was
  deleted or reordered; saved answer targets remain and new choices append.

## GATE

All runtime exports, build products and checker outputs were produced in a
disposable system-temp copy, with `PYTHONHASHSEED=0`; root `development/Story.json`
and generated fixtures were not edited. Task-specific **“No full suites”** was
followed: no unittest discovery and no default full RulesTests run. No game,
build-expansion.ps1 or gameplay harness ran.

| Command/check | Result |
|---|---|
| `PYTHONHASHSEED=0 RRT_GAME_DIR=/wrath RRT_PARENT_BINDINGS=<existing reviewed reference files> RRT_STORY_OUTPUT=$STORY python expansion.py` | PASS, exit 0, 4,054 scenes. Final rebuild timed with Python monotonic/runpy: **118.014 s**. |
| `python -m unittest tests.test_harem_row_s04 tests.test_recovery tests.test_camellia_round2 tests.test_intimacy_contract_lint tests.test_savecompat_baseline tests.test_utf8_io tests.test_crossroute_presence tests.test_horzalah_polish tests.test_konomi_round2 tests.test_konomi_round3 tests.test_wenduag_polish -q` | PASS, 111 tests, 596.937 s. |
| `python -m unittest tests.test_harem_row_s04 tests.test_recovery tests.test_savecompat_baseline tests.test_utf8_io -q` | PASS, 24 tests, 421.696 s after oath/Herrax integration. |
| `python -m unittest tests.test_recovery tests.test_utf8_io -q` | PASS, final 7 tests, 9.042 s, including original Wenduag check/no-new-fee and exact NPC-gender exception regressions. |
| `python tools/savecompat.py --story $STORY` | PASS, 0 hard failures. |
| `python tools/payoff_lint.py --strict --story $STORY` | PASS, 42 routes, 0 hard failures; existing advisory receipt reviews remain. |
| `python tools/departure_lint.py --strict --story $STORY` | PASS, 43 women, 0 hard failures; existing Mielarah advisory remains. |
| `python tools/voice_lock_lint.py --strict --story $STORY` | PASS, 63 locked scenes, 0 changed, 0 missing/ambiguous. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- $STORY --suites=CamelliaTricksterTests,CamelliaNativeSlideTests,PacingPP2Tests,ParentEndingRulesTests,KonomiTricksterTests` | PASS, **6,958 assertions / 5 suites**, final export. CamelliaPolishTests runs inside CamelliaTricksterTests. |
| Optional broader C# selection including `HerraxTricksterTests` | FAIL at the existing scene-level Minagho/Chivarro gating assertion; the recovered palace-knowledge Python regression passes. See ESCALATE. |
| Optional broader C# selection including `WenduagTricksterTests` | FAIL at its allocated-reactor guard assertion; recovered Wenduag prose does not alter reactor entries. See ESCALATE. |
| `bash tools/managed_tests_linux.sh /wrath/` | PASS, exit 0, all six fixture modes: ordinary and expanded construction (713,284 / 713,287 assertions), wrong-type optional owner (2,026), load smoke, missing Irabeth etude (6,131), missing Trickster etude (6,131). Main.Build constructs 4,054 scenes / 201,047 generated blueprints. Unity/Mono boundary diagnostics remain informational. |
| `python tools/rrt_verify.py --strict --gate-only --game /wrath --json $TMP/verify-final.json --text $TMP/verify-final.txt` | PASS, exit 0, **0 hard failures**, 0 shipped structural errors, 0 draft diagnostics; intimacy/memory/transactions 0 hard. Runtime **219.5 s**; 4,763 player-text reviews remain advisory. Full advisory analyses were completed by the earlier 558.8 s invocation; all strict validators were rerun after its seven findings were fixed. |
| `git -c core.whitespace=cr-at-eol diff --check HEAD`; original newline convention and allowed-path checks | PASS; no source build folders, generated fixture diff, forbidden path, unresolved merge marker or newline drift. |

Two pre-final verifier attempts were stopped after source corrections. The one
completed full strict invocation took 558.8 s and reported 7 hard findings
(2 narration nesting, 1 vocabulary budget, 4 male-NPC false positives). After
fixing all seven, the final export receives a strict `--gate-only` recheck, which
runs every strict validator and defers only the full advisory world/budget
analyses already completed. No `--no-zip`, raised budget or validator bypass. Earlier recovered
C# test failures (scope, informed-node slots and older direct cut edges) were
corrected against current source and then passed; unrelated assertions are
reported rather than relaxed.


## ESCALATE

- Camellia Last Call paragraph 1 retains its old corpse-hearing/three-day assumptions, identified in the original polish report. The merge changes only the named paragraph 3 and current held-flask rule; the older paragraph needs shared receipt-specific prose review, not a new delay or return price.
- Kiana LOST native-text adapter/runtime and absent untracked support files,
  partial Kiana/dog Q3 suppression, and native/copy kill observations require
  prohibited `src` work. Existing partial-recovery limitation is also recorded
  by the later Kiana round-two report. No unsupported story fields installed.
- Areelu LOST former-half-demon introduction requires a reviewed native parent
  cue family in shared validation; current fate/Pharasma continuations retained.
- Herrax LOST native ShowOnce response rewrite requires its absent `src`
  implementation. The optional Herrax C# suite also reports pre-existing shared
  scene-level `crossroute.chivarro.unavailable` gates on non-discovery scenes
  (`madam.the_night`, `owed.night`, `house.labyrinth`, etc.). Recovery changes
  only Seelah's named neutral-ending insertion in that shared pass; unrelated
  Herrax gating was not redesigned or its assertions weakened.
- The optional Wenduag C# suite still reports its allocated-reactor guard assertion. The recovered changes do not edit any reactor scene; current shared presence/guard generation needs route-owner review. Targeted Wenduag Python polish tests pass.
- Melazmera surviving Greybor/Hepzamirah availability and hunt/hunger placement
  findings affect Claude voice-locked scenes since `9005695a`; deferred to that
  owner, with every relevant hunk identified in the triage.
- Gesmerha's missing persistent placement-failure proposal depends on the old
  rejected reuse-native body policy. Review it against current spawn-copy and
  departure epochs before authorizing any new persistent mechanism.
- S04 approved numeric Religion DC, confession discovery/item producer,
  settlement authority and retry contract remain missing. Success stays blocked
  as in the recovered branch; no manufactured blessing or absolution.

## PROPOSE

No independent route redesign proposed or implemented. Coordinator may assign
the explicitly deferred shared/voice-owner dependencies in the triage.

## RISKS

- This recovers supported lost work, not a certification that all pre-existing
  route audit findings are resolved or every rubric dimension scores at least 91.
  Deferred shared-code, locked-scene and S04 success work remains visible.
- The staged Camellia merge is intentionally uncommitted; coordinator must
  review both parents and complete it under their own commit authority.
- Headless managed checks report Unity/Mono internal-call boundaries; a passing
  construction fixture does not claim Unity rendering or a game save round trip.
- No generated JSON recovery reports, fixtures, bin/obj or temp folders remain
  in the source repository. System-temp test copy and outputs are deleted before
  handoff; this report records results rather than retaining audit artifacts.
