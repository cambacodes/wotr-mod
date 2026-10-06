# Kiana polish round 2

Uncommitted implementation. No independent 91+ score is claimed. This report
supersedes the copied plans' planning-only status for the implemented portions.
All situations below are authored additions; native fact checks used
`/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`.

## CHANGES

| File | What changed; finding/plan |
|---|---|
| `storylines/kiana_round2.py` | SP1: ceremony-specific court recalls for all three roles; recovered guests answer their own names and Arsinoe interrupts flirting with ward work. F1 6–8,17. Existing captive/ordinary-patient variants remain distinct. |
| Same | SP2: Elan's actual reply stops her borrowed-room rehearsal. Honest waiting reads his independent terms and her answer before another invitation; deferred desire admits the unanswered account. Separation now shows continued love and her reason for ending the marriage. Betrothal's misleading coexistence answer is retired only on current Trickster, with an accurately worded append-only breakup answer. F1 10–12; KIA-02/03; fixed registry device. |
| Same | SP3/H2–H3: invitation, repeated-visit promise, reciprocal kiss, purposeful undressing, fillable first-night cut and dawn. Unsettled living/dead accounts have different aftermaths; reading/distance retain nonsexual exits. The morning conversation no longer claims sex from `lovers`. |
| Same | SP4 partial: preserve the native public reunion and existing discovered letter, admissions, Elan's private demand and permanent affair closure. Physical stairs/bed interruption is withheld for the placement reason below. Both discovery hosts retain their effects. |
| Same | SP5: all four commitment-host copies keep her continued love in the optional breakup, her choice, his separate reply, and share/exclusive/secret/refusal outcomes. Existing share terms and partner-state paragraphs remain. F1 11–16. |
| Same | SP6: apology payment now includes the newly recovered cooper's objection and Kiana crossing out his name. All copied payoff paragraphs carry this real receipt, and annual enforcement distinguishes a living/dead Sunhammer. His demand remains cruel. Her reaction travels in the existing pre-march Last Call letter. Kept-chair ending and Last Call show an actual bodily return only in appropriate surviving mortal histories. F1 21–25; SP6. |
| Same | Native recovery prose identifies the guests as sleepers; neither Elan nor the conscious bride is described as discharged from a coma. F1 9,50; additional spouse-freedom sibling checked. Native override eligibility stays current-Trickster-only. |
| Same | H5–H7: fastening/close contact before the real supper, ink-stained returning desire, hungry parting with a next visit, private desire after the yard quarrel. Existing quiet/walk alternatives and continuation gates remain. No additional encounter, cost, attraction or commitment requirement. |
| `storylines/kiana_partner.py` | Invoke the route-only appender after the existing partner and late-acceptance appenders. No shared source file edited. |
| `tests/test_kiana_round2.py` | History tests: three costume roles with/without a ceremony/recovery, honest waiting, first-night slot/default/legacy exits, nonsexual alternatives, public discovery closure, native sleeper facts. |
| `tests/KianaTricksterTests.cs` | F1 58–59: build the departed-Seelah rescue from its own snapshot and assert actual temple availability for dead-Seelah dog/paid histories before walking. Original CRLF preserved. |
| `tools/route_packs/plans/kiana-{setpieces,tp}.md` | Copy the binding source sheets byte-exact from their specified refs. |
| `tools/route_packs/turning_points.json` | Copy only Kiana's exact atlas reservation: `another_character_intervenes`; Drezen borrowed vampire-court room, Elan's reply interrupting rehearsal; honest guest's exit with husband's state carried. |
| `tools/route_packs/explicit_slots/kiana/*.json` | Copy all four prescribed briefs byte-exact. Add functioning nodes `kiana.date.explicit.1`, `kiana.ink_after.explicit.1`, `kiana.unborrowed_evening.explicit.1`, each with a heated default and exact brief last line. Retain discovery brief pending placement. No explicit prose generated. |

## CLASS SWEEP

- F1 1–5,18–20,26,28–29,37,55–57: preserve already-merged awake/widow letter, neutral timing, postal placement fallback, recovery report, final-answer and printed-question repairs; do not rebuild their mechanics.
- F1 6–9,17,50: sweep three cast roles, ceremony played/skipped, recovered/captive/ordinary ward, conscious/soul-lost bride and unaffected Elan. Casting never proves a ceremony, rounds never prove rescue or affection.
- F1 10–16: live-marriage, postponed betrothal, widow, deferred/honest-wait/separated histories; four stance hosts; physical and Seelah correspondence discovery; partner paragraphs in endings/Last Call. No friendship or arrival inferred from correspondence.
- F1 21–25: paying scene and every copied committed/margin/stage apology paragraph; creditor alive/dead. Unpaid stones remain unpaid; a pardon call alone does not free them.
- H2–H8: first night once, returns rather than repeated first nights, nonsexual reading/quiet/walk alternatives, supper contact, ink and yard continuations, bodily coda versus ascension/sacrifice. Existing art traits are not promoted to native anatomy in briefs.
- Preserve all existing scene/node orders, answer indices and legacy `Next`/`Set` mechanics. Changes append nodes/answers/paragraphs or retire incoming answers by gating. Preserve deliberate refusals and the Trickster continuation budget. No foresight or echo added.

## GATE

Exports, .NET intermediate
and binary outputs, and checker reports use a system-temp directory and are
deleted before delivery. The final user instruction takes precedence over the
earlier writing-phase ban on full tests; no commit is made.

`STORY` denotes the final freshly generated export in system temp. Commands use
`PYTHONHASHSEED=0` unless explicitly noted. No development export is edited.

| Command/check | Result |
|---|---|
| `RRT_STORY_OUTPUT=$STORY python expansion.py` | PASS, 3,755 scenes. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io -q` | PASS, 12 tests. |
| Kiana partner/round-2 Python modules plus two native archive/policy methods | PASS, 15 tests; final partner/round-2 rerun after heat revisions: 13 tests. |
| `python tools/payoff_lint.py --strict --story $STORY` | PASS, 42 routes, 0 hard failures; Kiana has no receipt residual. |
| `python tools/departure_lint.py --strict --story $STORY` | PASS, 43 women, 0 hard failures. |
| `python tools/rrt_verify.py --strict --story $STORY --game /wrath/` | PASS, single final invocation, 0 hard failures; 0 shipped structural errors; intimacy/memory/transaction contracts 0 hard. Runtime 559 seconds; 5,355 player-text reviews remain advisory. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE: both attempts ended with exit 143 and no test summary. First attempt omitted the hash-seed environment; second used it. Neither is counted as passing. |
| `dotnet run --project tests/RulesTests.csproj -c Release -p:BaseIntermediateOutputPath=$TMP/rules-obj/ -p:OutputPath=$TMP/rules-bin/ -- $STORY` | Compilation succeeded in temp; `dotnet run` looked for its executable at the default path and could not launch it. The built DLL was run directly against the final export afterward. |
| `dotnet $TMP/rules-bin/RulesTests.dll $STORY` | INCOMPLETE, exit 143 after initial shared-engine PASS messages; no full-rule summary. |
| Same DLL, `--suites=KianaTricksterTests` | FAIL after 780 assertions: `Trk_Kiana_NoQ3: the pivot ignores its day.` The repaired snapshot retains `seelah_gone` and exposes the scene-wide shared Seelah veto; see ESCALATE. |
| Integration-export-relative Kiana scene/node order and legacy choice `Next`/`Set` comparison | PASS, 0 issues. |
| `git -c core.whitespace=cr-at-eol diff --check`; original LF/CRLF check | PASS; edited existing files preserve their original newline convention. |

## ESCALATE

- SP4 bedroom interruption and `kiana.partner_discovery.explicit.1`: the native `ElandKianaAftermath/Cue_0001` (`81109ea8fb20dbc478cf67116740f4a1`, enGB `b261aab4-14ff-41e7-bd72-21aeeab7df44`) explicitly stages a public reunion. Its attached answer list supplies no private arrival. The sheet itself marks host placement as a coordinator dependency. Implementing stairs/sex there would contradict the native situation; a new arrival/timer/trigger would exceed authorized mechanics. No invented arrival or successful escape added.
- F1 27,32–36,38–54: shared cross-route presence generation still adds a scene-wide Seelah veto to the temple pivot, and treats Arsinoe's romance closure/`VictimsRevived` as loss of professional presence, including historical references. Final export inspection confirms these guards. This needs shared `crossroute_presence`/presence-policy work; no bypass predicate or new gate added. The repaired C# histories now expose it.
- F1 30–31: `src/NativeQ3Recovery.cs` still preserves the whole native recovery on partial rescue. Individually recovered Kiana/dog need independently reviewed sleeping-spawn/awakening exclusions, retaining every other guest and quest completion. Shared native adapter work is outside this scope.
- Required `/work/Writer/judging/codex/kianap1.json` is absent. The available audit union is F1 plus the plans' cited findings; there is no engine-round-3 Kiana receipt residual (0 payoff/departure hard, None in its residual table). Supply P1 before certifying the complete audit union.
- Full Python/default C# milestone gates ended with exit 143 without completion summaries. The focused repaired Kiana C# test has a concrete shared-policy failure as recorded above. The coordinator must complete those gates after fixing the shared delivery guards; the strict verifier's zero hard failures do not replace them.

## PROPOSE

None. The remaining placement/presence/native adapter work above is required
integration work, not an implemented redesign.

## RISKS

- SP4's planned private encounter remains incomplete; its JSON brief is not a
  reachable slot. The other two continuation slots retain their existing gates
  and remain blocked on the current Trickster continuation budget.
- Mechanical gates do not certify independent writing scores. No game, harness,
  packaging build or live-save round trip was run.
- Shared availability and partial native recovery defects remain as listed;
  route-local prose does not repair their runtime delivery.
