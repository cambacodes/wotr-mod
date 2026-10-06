# Kaylessa — round 2 implementation report

Changes are uncommitted. Only Kaylessa source, her tests and route-pack files were edited. All exports, compiler outputs and gate reports were directed to the system temporary directory. No harness, game or build-expansion.ps1 was run. The final user instructions control the conflicting earlier commit and gate instructions.

## CHANGES

Finding numbers refer to the `defects` arrays in kaylessap1.json and kaylessaf1.json.

| File | Change and finding coverage |
| --- | --- |
| `storylines/kaylessa_trickster.py` | Dead access: Shyka answers a sending at the Commander's camp; the existing 200-Favors debit represents messengers and diplomatic contacts used to carry the offer. The sender is Shyka. Both payment roads promise twelve hours; the presence uses the existing timestamp facility to enforce that boundary. P1.11–13; F1.2–5,10–11. |
| Same | Living access: both hunters arrange a moonless meeting when preparations are ready. The warning remembers only an actual meeting unless the Commander actually warned her. P1.2; F1.12–13. |
| Same | Turning point: the cell encounter distinguishes the patrol's accusation from her identification of Tessariel, recalling how names and witnesses misled the Wasps. She stops the report and names the lamp-holder herself. Key/doorway/release outcomes, failed persuasion, beast consequences and both dagger acceptances retain their effects. Proposal recalls settled rules rather than unplayed acquiescence. KAY-01/02; P1.8. |
| Same | Late pursuit: she steps out from behind a shutter, reaches and kisses on her own initiative; no assumptions about the Commander's eyesight. Confessions describe the already-paid terms without inventing failed bargaining. P1.14; F1.5–8 class sweep. |
| Same | Endings: exposure defeats blanket clean-swap secrecy; letter, public scout and market witness histories differ. Courier remembrance receives acknowledgement. Late intimacy distinguishes first night from return, reserves a slot, keeps actual dagger custody, and retains the curse and her returns from hunting. P1.9; F1.22,25–31. The already-correct lamp, kissed-ally and price variants were retained. |
| Same | Companion reactions require available Woljif, avoid instant friendship and identify the actual ride. Anevia's ravine report is event-relative. F1.1,16; heat/voice sheet. |
| `storylines/kaylessa_wasps.py` | Native automatic objective completion has its own durable etude reader and appended truthful answer. Existing sale and unresolved answers retain indices. The native-history integration still supplies sent/resolved readers; no shared file was changed. P1.1; F1.19 history sweep. |
| Same | She asks about the destroyed pages and learns their fate from the Commander; withholding has a separate reaction. Giving her the retained message actually removes that item through the existing removal facility and route integration whitelist; keeping it preserves inventory. P1.4–5; F1.19. |
| Same | Tomb stages the custodian's loan and return; the bow is one surviving pre-curse possession. Current gate-watch discussion has an Anevia-absence branch; Woljif's goat scene requires recruitment/current availability. P1.3,6; F1.1,21,24. |
| Same | Courier remembrance distinguishes unsent account from a follow-up. The original remembrance producer remains on its original choice index. Anemora's spoken revelation and death can both be reported. Dispatch predicts receipt rather than same-night arrival and describes diplomatic losses as risks while preserving the 100-Favors debit. F1.22–23,29,32; P1.9. |
| `storylines/kaylessa_clearing.py` | Clearing night appends `explicit.1` after the existing `cut`; original night producer is intact. Morning opens at a current Drezen contact and explicitly recalls the actual morning, preserving all curse/custody and linger/ride branches. Secrecy is no longer asserted after exposure. P1.10; F1.18; set pieces 4–5. |
| Same | At the roof alarm she owns using the Commander's name before the promised postwar conversation. Back under the awning she chooses how her own name is used; public exposure has a spoken consequence without another trust gate. Rule-four callback requires the actual agreement; ordinary response stays available. KAY-03; P1.7; F1.20. |
| Same | Border reply pays courier remembrance and removes the unearned spring date. Hunter entry names letter/scout/market/fumbled-ravine evidence separately; its request no longer recalls a ravine loss of control on clean histories. Existing captive outcomes remain intact. F1.22,29–31,33. |
| `tests/test_kaylessa_round2.py` | Ten regression tests cover arrival boundaries/missing timestamps, automatic closure versus sale, actual item removal, three rule histories, combined Anemora facts, exposure sources, custody, delayed morning, available witnesses, slots and complete ending variants. |
| `tests/KaylessaTricksterTests.cs` | Morning-witness fixture now recruits Woljif for the positive and checks never-recruited/plot-absent negatives. F1.1. |
| `tools/route_packs/explicit_slots/kaylessa/*.json` | Copied the two supplied briefs unchanged. Clearing node and late epilogue paragraph have heated-cut defaults; no explicit prose was generated. |
| `tools/route_packs/plans/kaylessa-{setpieces,tp}.md` | Copied supplied plans for review. The set-piece sheet and atlas supersede the TP sheet's old proposed class. |
| `tools/route_packs/turning_points.json` | Registered only Kaylessa's supplied atlas entry: `canon_lowest_point`; reserved awning/death-site setting; custody → reclaimed death-site → morning danger payoff. No duplicate class + setting in the supplied atlas. |

Six situations are carried through: hands without a spell; priced return/prepared living cover and watch; prisoner accusation and dagger proposal; chosen death-site night; curse/custody/exposure aftermath; late invitation and living continuations. Kaylessa has no established canon partner: no invented partner or stance subsystem was added. Early entry and already-strong courtship remain intact.

Authored additions are the existing tailor/ravine courtship, Tessariel and courier history, correspondence and the camp sending; these are additions, not claims of native quests or biographies. Native identification, refusal of spells, Wasps manipulation, failed dagger, Avennara and automatic letter resolution were checked against `/wrath/blueprints.zip` and English localization. There is no new foresight/echo allocation and no page-derived affection.

## CLASS SWEEP

- Checked all four Kaylessa source modules, all original scene/node ordering and choice effects, and five legacy epilogue exits. A comparison with HEAD confirmed original effects and epilogue Next/Abort mechanics; all three edited source modules retain CRLF.
- Swept ordinary/raised/sending prices, truthful/unconfessed/confessed histories, sent/concealed/automatic/unresolved letters, retained/given/destroyed pages, both dagger custodians, stalled/living/fed curse, clean/fumbled/exposed cover, named/anonymous exposure, companion presence and early/late intimacy.
- Preserved base fixes for F1.6–9,14–15,17,25–28. Removed sibling stock head/rarity deflections and youth comparisons where named in the heat/sameness review.
- No extra fee, virtue test, attraction score, commitment prerequisite, forced reconciliation, cure or partner exclusion was introduced.

## GATE

Generation and Python test commands use PYTHONHASHSEED=0; the export is `/tmp/rrt-kaylessa-r2-gates/Story.json` rather than modifying the forbidden development file. Parent binding environment uses the four manifests selected by build-expansion.ps1. Reports and managed outputs also go to `/tmp`.

| Command/check | Result |
| --- | --- |
| `PYTHONHASHSEED=0 RRT_STORY_OUTPUT=<tmp>/Story.json python expansion.py` | PASS; final export contains 3,755 scenes. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io -q` | PASS; 12 tests. UTF-8 check separately passed again on final source. |
| `python -m unittest tests.test_kaylessa_round2 -q` | PASS; 10 tests on the final export. |
| `python tools/payoff_lint.py --strict --story <tmp>/Story.json` | PASS; 42 routes, 0 hard failures. Kaylessa's inherited L remains REVIEW. |
| `python tools/departure_lint.py --strict --story <tmp>/Story.json` | PASS; 43 women, 0 hard failures. |
| Original-source identity/effect comparison and `git -c core.whitespace=cr-at-eol diff --check` | PASS; original scene/node ordering, original answer effects, all five ending exits and CRLF preserved. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE; both attempts ended with signal 15 / exit 143 and no test summary. No pass inferred. |
| `python tools/rrt_verify.py --strict --story <tmp>/Story.json --game /wrath --json <tmp>/verify.json --text <tmp>/verify.txt` | PASS; invoked once, exit 0, **HARD FAILURES: 0**. Runtime 563.6 seconds; 0 shipped structural errors and 0 draft contract diagnostics. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- <tmp>/Story.json` | INCOMPLETE. Early external-output variants compiled but CLI launch incorrectly used the default path. Retried with the supported `RRT_TEST_BUILD_ROOT=<tmp>/rules-build`; execution ended 143 without a verdict. |
| Execute the temporary compiled RulesTests assembly, full / `--routes kaylessa` / `--suites KaylessaTricksterTests` | INCOMPLETE; execution ended 143 without final verdicts. Route-catalog run emitted `PASS: E-Q7-12 kaylessa:002/paid return` before termination, with no reported failure; this is not a suite pass. |

## ESCALATE

- P1.15/F1.34: the shared finale must collect the already-paid Shyka branch and provide/register `kaylessa.lastcall.page`, with living-cover, ally, absent, closed and unreturned-sacrifice variants. `lastcall.py`, `lastcall_partners.py`, `lastcall_ledger.py` and shared finale integration are outside this task's permitted ownership. The interim note was not relabelled as a settled debt or charged again.
- Supplied set-piece sheet's native dependency review: coordinator must audit deliberate early executions/user closures and narrowly gated native death/memorial/slide consumers under the earned Trickster rewrite. No broad suppression or new access gate was invented here.
- Full Python/managed gates need a completed run on coordinator infrastructure. Repeated termination without a summary leaves broad progression/selectable-answer validation uncertified; no shared test or engine change was attempted to hide it.

## PROPOSE

Engine-round-3 residual L remains a review: late readiness derives from the existing specification gates; there is no separately stored prewar yes. A separate acceptance producer would change the existing commitment contract. It was not added or made mandatory. Coordinator should decide that separately from this prose/receipt pass.

## RISKS

- No independent score or claim that every rubric dimension reaches 91 is made. Shared finale debt is still uncollected.
- Explicit slots are reserved defaults. User/coordinator filling must preserve perspective, first-night/return history, custody and the uncured danger.
- The supplied atlas has no duplicate Kaylessa class + setting; complete pending-route integration still belongs to the coordinator.
- Full-suite verdicts must be read from the completed commands; termination without a summary is not a pass.
- The final isolated Kaylessa managed-suite attempt also ended 143 without a summary, after the verifier had completed. No managed route pass is claimed.

Temporary exports, reports, patch scripts and compiler outputs were removed before handoff. The detailed gate outcomes above are the retained record; no audit/build artifacts were left under the repository.
