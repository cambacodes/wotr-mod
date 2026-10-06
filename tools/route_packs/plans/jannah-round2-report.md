# Jannah — polish round 2 implementation

Uncommitted, as requested. All runtime additions below are authored Trickster continuations, not recovered native romance. Native references were checked directly in `/wrath/blueprints.zip` and `enGB.json`: Deserter/Cue_0002, 0015, 0018; ElanDying/Cue_0003; SeelahInDoubt/Cue_0005; HideoutIntro/Cue_0023. The atlas reservation remains `canon_lowest_point`, Ch5 Drezen gaol → garrison muster chalk circle, public desertion account → separately chosen desire → crossed blades/night/gossip. No partner, foresight or echo was invented.

## CHANGES

| File | Finding / set piece | Change and reason |
|---|---|---|
| `storylines/jannah_trickster.py` | SP1 | Retained the existing early laugh/bout invitation and the missed promise; no retroactive bout or affection receipt. |
| Same | SP2; f1:07; JAN-01/04 | Unmet escape now has nights of preparation, a worked fastening, a bone sliver, a torn hand and hiding. She retracts her polished account herself. The existing ford explicitly lets wounded soldiers cross behind her file; she chooses her return. |
| Same | SP2/4; JAN-01–03 | Blood-and-tale names the Commander's limited witness role. A recruit repeats an inflated account in the muster; she corrects it before fighting. Shared-camp and visitors' answers attest only what the Commander actually knows. No forged proof or new contest. |
| Both route files | SP3; p1:28–35; f1:02,08–12,16–22 | Retired introductory blade/measure staging after the challenge/commit/night, preserving all old targets. Removed premature wall recall and fixed chronology. Optional ride, return lesson, frightened conversation and tavern song now start at her cell; the ride has an accepted departure. Ordinary Mivon correspondence waits 720 hours. Her frightened refusal remains nonsexual. |
| `storylines/jannah_trickster.py` | SP4; p1:23–26; f1:05 | Confession no longer grants commitment. It leads to the applicable sincere salute, public correction promise or enacted private yield, then her spoken yes and the terminal acceptance. Both her-first exits record the actual blood result. Public promise has its own receipt; private yield never spends public Favors or grants public yield. Leaving still closes. |
| `storylines/jannah_circle.py` | SP4; f1:06 | An earned returned Seelah confronts the witnessed cage killing. Jannah owns walking past her. The narrow reckoning precedes ordinary courtship in that history; no new forgiveness payment or return device. Shared memory/presence suppression still needs coordinator repair. |
| Both route files | SP5; HEAT inventory | Kept the first-night descent and appended `jannah.trickster.circle_night.explicit.1`; the later voluntary return appends `jannah.circle.eyes_open.explicit.1`. Defaults are heated cuts, not explicit prose. Replaced coy "allowed" kissing and wound-pressure staging. Morning retains desire, drill, gossip and recurring fear; Q3 friendship has her own telling. |
| Both route files | SP6; p1:01–06; f1:01 | Elan dies of the trap, never a stolen soul. Full paid rescue variants name empty settings/revenge and Commander/Arsinoe attribution, including joined letters. Curl's recovery selects paid flags before native recovery; his subsequent whereabouts remain unknown. Single Kiana rescue does not free Curl. |
| `storylines/jannah_trickster.py` | SP6; p1:26,36; f1:03,04,13,14; eng3 late residual | Public correction reads its promise receipt. Thrown bout remains void; maintained lie stays in her cell. Rejection is short and wounded. Late readiness excludes unpaid false blood, unresolved refusals and the narrow unreckoned cage history; she voices desire separately from the deferred bout. Unpaid false blood uses the existing service/refusal ending with an appended conditional paragraph. The existing Seelah cell hook now branches between game and wagon histories. Legacy ending Continue identities and mechanics remain intact. |
| `tests/JannahTricksterTests.cs` | p1:37–38; f1:25–26 | Uses `Program.WalkVia` to prove actual node/index traversal. Replaced 160-hour exploration jumps with scene due times; updated repair delay and assertions for terminal acceptance. |
| `tests/test_jannah_round2.py` | p1:23–26,37–38; f1:04–05,08–12,18–26 | Seven selected-path regressions: actual challenge → each combined held-lie refusal → repair/yes, refusal after confession, truth-gated late readiness, paid rescue precedence, phase/delivery guards, actual-producer 132/168-hour routes and one-time slot placement. |
| `tools/route_packs/plans/jannah-setpieces.md`, `jannah-tp.md` | Required plans | Copied the binding sheets without merging other branch code. They describe planning history; this report records implemented versus escalated work. |
| `tools/route_packs/explicit_slots/jannah/*.json` | Required slots | Copied both briefs, preserving voice traits, factual limits, anatomy variants and exact final lines. No filler generated. |
| `tools/route_packs/turning_points.json` | Uniqueness | Registered only Jannah's fixed atlas entry; no other route entries changed. No global sameness-lint pass claimed. |

## CLASS SWEEP

- Audited the full repair union, all four old opening answers, their preserved targets, first-blood results, commitment/night/morning/ending consumers and public versus private yield receipts.
- Checked both Elan histories, both door histories, joined letters, both Curl question paths, full/native/single recovery attribution and optional aftermath.
- Checked blade/measure/notch ordering; pre-wall wording; Houndheart/ Kenabres duration siblings; correspondence and recruit-song timing; optional physical invitations.
- Read historical versus participating Seelah/Kiana/Irabeth references in stories, Houndheart, mourning, Kenabres, ride, Curl, door, one-question, paper and the dormant board. Protected shared injection remains escalated below.
- Kept dead-cage primers retired, every original authored node in order, all old choice positions and legacy ending exits. Both route files and the C# test retain CRLF byte style. `git -c core.whitespace=cr-at-eol diff --check` passes.

## GATE

Export, reports and .NET obj/bin use a disposable system-temporary directory, never `development/` or `tests/`. Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`; Python fixtures read the temporary export through `RRT_TEST_STORY`.

- `python expansion.py` with `RRT_STORY_OUTPUT=<temporary>/Story.json`: PASS, 3,755 scenes. No generated development file edited.
- `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_jannah_round2`: PASS, 19 tests on the corrected final source/export; 144.531 seconds. The seven Jannah selected-path tests also pass independently and use Kiana's actual single-rescue receipts.
- `python tools/payoff_lint.py --strict --story <temporary>/Story.json`: PASS, 42 routes, zero hard failures. Shared REVIEW entries remain.
- `python tools/departure_lint.py --strict --story <temporary>/Story.json`: PASS, 43 women, zero hard failures. Two initially unregistered additions were folded into existing scenes, then export and both lints were rerun.
- `python -m unittest discover -s tests -p "test_*.py" -q`: attempted twice; both processes ended with signal 143 before a unittest summary. A terminal retry ended with code 1 and no diagnostic output. **Not a pass.**
- `dotnet run --project tests/RulesTests.csproj -c Release ... -- <temporary>/Story.json`: compilation succeeded outside the repo, but the CLI launcher looked in the default repo output directory. The equivalent temporary `RulesTests.dll` was executed directly; full runs ended with signal 143 after initial PASS lines. **Not a completed rules gate.**
- `dotnet build tests/RulesTests.csproj -c Release` with temporary `BaseIntermediateOutputPath`, `MSBuildProjectExtensionsPath`, `BaseOutputPath`: PASS, zero errors, eight inherited warnings. A focused `--suites=JannahTricksterTests` run identified the newly expanded actual Seelah hub as incorrectly included in the Jannah-only solitude assertion; that assertion was corrected without weakening live-actor gates. Its subsequent run also ended with signal 143. No `Page has no selectable answers` diagnostic was reported in these runs.
- `python tools/rrt_verify.py --strict --gate-only --game /wrath --story <temporary>/Story.json`: PASS, **zero hard failures**, 177.9 seconds; zero validation, save-compatibility, structural or player-text hard errors. `--gate-only` runs every strict check and skips report-only analyses. The initial default-path attempt could not find the Windows archive. The subsequent full report found two local failures (quoted escape-letter self-correction misattribution and a singleton eligibility group); both were fixed, export regenerated, and strict/payoff/departure/19-test gates rerun. No shared lint or baseline was changed to obtain the pass.

## ESCALATE

- **p1:07–22 and dormant board sibling:** `storylines/crossroute_presence.py` and `tools/crossroute_checks/*` still inject current-presence restrictions into history and mourning, including Kiana romance closure blocking Jannah's mandatory memory. They also suppress the returned-cage dialogue's containing scene. Those protected shared files were not edited; route-local prose cannot reliably repair their classification.
- **Eng3 late residual:** shared `engine_eng3_ab.py` / payoff registry and household/Last Call consumers still treat the existing late predicate as readiness rather than a separately observed yes. The route-local truth/refusal/reckoning guard survives their integration, and the existing late page voices her choice, but this is not a new stored acceptance. Do not certify automatic prewar household admission as fixed.
- **SP6 shared coda:** Jannah Last Call living/returned/dead continuation is in protected shared `lastcall*.py`; its requested ordinary-company rewrite was not made. No unreturned Commander was added to route-local living scenes.
- Updating the external character handoff/spec's implementation notes needs coordinator scope. This authorized report labels additions instead.
- The incomplete full Python/C# runs need a conclusive coordinator gate. Signal termination was observed; no specific external cause was established.

## PROPOSE

None beyond completing the named shared residuals. No additional attraction, commitment, reconciliation, fee, partner stance, magical device or echo was implemented.

## RISKS

- The shared memory blockers prevent claiming the all-history feasibility or the >=91 audit bar. No independent quality score is claimed.
- Old saves that already received the former incomplete combined-repair commitment do not contain a distinct historical salute receipt; the current graph fixes actual new traversals without fabricating prior acts.
- Explicit slots contain defaults only; coordinator/user filler still needs continuity review. The global uniqueness registry must be compared by the coordinator.
- Full-suite gate completion must be assessed from the final results below, not from compilation or early PASS lines.
