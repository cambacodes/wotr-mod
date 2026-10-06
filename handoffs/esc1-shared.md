# SHARED ESCALATIONS round 1

## CHANGES

| Finding | Status | File and result |
| --- | --- | --- |
| Anevia Last Call :160/:161 | Fixed | `storylines/lastcall_partners.py`: the Commander retains the closet; Anevia delivers notes by hand. The remembered-room/once-per-room restriction stays intact. The exposed Iz lie replaces the false silence-at-the-gate recollection. |
| Nidalynn Ledger | Fixed | `storylines/lastcall_partners.py`: bread and salt identify Reudger's personal rite, matching `nidalynn_salt.py`, rather than claiming a Windstep clan custom. |
| Soana Last Call | Fixed | `storylines/lastcall_partners.py`: common opening no longer presumes she went back to an intact Wintersun wood; removed the narrator's characterization aside. Existing return/accounting paragraphs and all conditions remain intact. |
| Arueshalae F6 overrides | Fixed | `storylines/native_facts.py`: removed the stale opening overwrite. Both neutral nodes inherit the corrected route text and remove only the unobserved first-dream recollection. Both histories retain her explicit waking distress and fingers clear of the Commander's skin; neither invents a sergeant victim. IDs, incoming choices and history selectors are unchanged. |
| Yaniel Iz song | Reader already fixed; claims fixed | `storylines/yaniel_trickster.py` and `/work/Writer/handoffs/trickster/yaniel.md`: distinguish Holy Avenger custody from native song observation. Verified Cue_0036 checks +4 Holy Avenger **or** +4 Bane Living, excluding +6 Holy Avenger. `yaniel.radiance_sang` already reads that exact cue. Kept the valid +6 inventory binding and all saved custody flags; no new sword-trade mechanic. |
| Targona E1 | Deferred: needs shared runtime policy | Verified Answer_0120 still reaches the Heaven-location Cue_0126 after earned ward arrival. See ESCALATE for the exact reconciliation. No unsupported override, dormant replacement scene or native answer change was added. |
| Seelah checklist item 12 / R1:013–014 | Fixed | `storylines/lastcall_partners.py`: neutral purse/list account feeds both Book Text and Journal Description, including pending rider returns. `storylines/lastcall.py`: append three mutually exclusive Book acquisition Lines using existing paid/arrest flags. Also corrected common coda/order wording and the every-evening claim, as item 12 requests. OpenWhen, SettledWhen, entitlements, saved line positions and call effects are unchanged. |
| Nocticula spec drift | Fixed | `/work/Writer/handoffs/trickster/nocticula.md`: replaced the obsolete physical visit/conjurer note with the actual correspondence-only coda and labelled the intimate written exchange as authored within the existing seal's limits. |
| Targona voice citation | Fixed | `/work/Writer/handoffs/trickster/targona.md`: DLC1/Iz/Targona/Cue_0003 now cites `149fa68dfe00411eba19dc07138813b4`, verified with its localized compassion line. |
| Herrax E-Q8-05 | Deferred | Engine round 3 owns payoff/eligibility/presence; no changes. |
| Shamira entitlement reader | Deferred | Engine round 3 owns this reader; no changes. |
| Camellia death observation | Deferred | Engine round 3 owns lifecycle observation; no changes. |
| Minagho D2 | Deferred | Engine round 3 owns departure/return/presence; no changes. |

The source list `/work/Writer/drafts/codex-impl/escalations-r1.md` is absent. The explicit task list, current sources, available reviewed plan refs and canon assets were used; no additional finding was inferred. No commit was made, following the final user instruction.

## CLASS SWEEP

- Inspected the affected Anevia closet and exposed-lie coda siblings against their route events; retained the existing wardrobe restriction and consequence selectors.
- Checked Nidalynn's salt dialogue and Ledger consumers: the route explicitly calls it Reudger's way, not the clan's. Shared common data updates both Book and Journal.
- Checked Soana's common opening, conditional return/accounting paragraphs and commentary sibling; no presence/return condition was changed.
- Checked every F6 override for `arueshalae.treatment.nightmare`: opening, observed/neutral dream, observed/neutral price, and the silent dawn branch. Corrected route text survives generation.
- Searched song/+6/ha6 claims across storylines, tools, tests and all Trickster specs. Verified the five existing inventory forms remain factual; +6 is a real item, but absent from the native Iz song checker. The Bane Living form is native song evidence, not a newly implemented custody/trade path.
- Checked Seelah's separate Book and Journal consumers, both return origins, pending dispatch, clean/concealed/arrested/paid acquisition, chapel credit, and coda duty wording. Exactly one acquisition Line appears in each of 16 selector combinations; existing Book Lines precede the appended Lines.
- Checked Targona's Answer_0120, both candidate cues (0125/0126), their native conditions, actions and answer list. Cue_0125 has separate wing-treatment conditions; no blanket suppression is proposed. Checked the cited DLC voice line against the actual blueprint and enGB text.
- Compared Nocticula's spec note with `nm1_nocticula.py` and the current intimate correspondence donor. No route event, channel power or gate was changed.

## GATE

Full gates use `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `RRT_GAME_DIR=/wrath` and the existing parent-binding files listed by `build-expansion.ps1`. Commands run in a disposable system-temp copy of this worktree; generated exports, reports and .NET intermediate/output paths stay outside the actual repository.

| Command/check | Result |
| --- | --- |
| `python expansion.py` | PASS: 2,959 scenes. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | PASS: clean full rerun, 562 tests, exit 0. The initial copy lacked Git context and failed one selector fixture; read-only temporary Git context resolved it without a source change. |
| `python tools/rrt_verify.py --strict` | PASS: exit 0; 0 hard failures, 0 shipped structural errors, 0 draft contract diagnostics. |
| `python tools/crossroute_lint.py --strict` | PASS: exit 0; 0 findings, 0 new findings. |
| `python tools/drezen_placement_lint.py --strict` | PASS: exit 0; 0 hard failures. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | PASS: exit 0; 147,916,107 assertions, 2,889 draft expansion scenes; rules and progression validation completed. |
| Focused rendered-history/canon probe | PASS: both Arueshalae branches; 16 Seelah receipt combinations; independent Book/Journal inspection; exact native Iz cue/items; corrected Targona voice GUID. |
| Regenerated HEAD/export comparison | PASS: all 2,959 scene IDs/order, all node IDs/order, relationship IDs/order, every choice index/destination/condition/check/effect, and all scene metadata unchanged. |
| Diff and newline check | PASS with `git -c core.whitespace=cr-at-eol diff --check`; original CRLF/LF styles preserved. No scene/node/relationship ID or choice index changed. |

No build-expansion script, harness, game or independent prose audit was run. All temporary copies, generated exports, logs, reports, scripts and .NET outputs were removed after verification.

## ESCALATE

**Targona E1 remains unresolved in shipped code.** Cue `afc32621ab47fd64c93e2c04e9ad86a9` is absent from `src/NativeEpilogueEdit.cs`'s reviewed policy. Adding that shared C# policy is outside this task's named content entries. The current registry rejects an unsupported target, so a content-only declaration cannot complete the reconciliation.

Coordinator/runtime owner handoff, verified in `blueprints.zip`:

- Dialog: `World/Dialogs/c3/Drezen_C3/Herald/Herald_Drezen_c3_dialog.jbp`, `5574af05c30b1ca41b3399b316548691`.
- Parent answer: `Answer_0120`, `5f8e1f56812651b4ca100619d4f32a95`. Preserve its index, conditions, history, actions and NextCue order `[22cc6489b63d94943afafbb824f09a7d, afc32621ab47fd64c93e2c04e9ad86a9]`.
- Target: `Cue_0126`, `afc32621ab47fd64c93e2c04e9ad86a9`, localized key `7e81cbb1-6f06-4f31-b5f0-f960513e488a`. No OnShow/OnStop actions, no Continue cues; Answers `[4ec1b902634784c42b2705727c8d91eb]`.
- Use the existing text-only native override contract. Select the authored replacement only for current `trickster.now` plus the existing earned ward-arrival flag `targona.trickster.met`, with the existing route-loss exclusions. Taking the wand night without meeting her must not change the location account. Keep native wording before arrival and on every other mythic path.
- Suggested authored Hand text: `"Targona has returned to Drezen to tend your wounded. She has written to Heaven's healers to tell them where she is. Her corrupted wing still troubles her, but she will not leave those soldiers without help. I pray that she finds healing in this work as well."`
- Label the eventual override as authored in Targona's spec. Check off-Trickster, before-arrival, wand-night-only and earned-arrival histories; preserve native cue history and all answer order. Add no new rescue, cost, affection requirement or arrival producer.

The four engine round 3 items in CHANGES remain deferred to that owner. The missing source list prevents verification of any escalation not explicitly named in the task.

**Worktree registration interruption — resolved externally:** during validation, `/work/repo/.git/worktrees/RRT-esc1-shared` disappeared and ordinary Git commands failed. No repair to real Git metadata was attempted. Validation used a temporary private HEAD/index backed by the existing read-only Git objects, anchored at `db1fd2da210fe5a92c2399f322a4b074d85b7068`. At the final check, registration was available again, ordinary Git commands passed, and HEAD still matched that commit. The temporary Git context was deleted with the other verification files. No coordinator action remains for this interruption.

## PROPOSE

None. No extra mechanics, checks, costs, reconciliation conditions or eligibility changes were implemented.

## RISKS

- Targona E1's native location contradiction remains until the shared runtime-policy owner lands its reconciliation.
- The three spec corrections are external Writer files; they are not included in the repository's Git diff. Their exact paths and changes are recorded above for coordinator review.
- Gates and local canon checks do not establish independent rubric scores. No >=91 quality score, game/harness behavior or live save/runtime compatibility is self-certified.
- The actual worktree's generated `development/Story.json` is untouched by design; reviewers must regenerate from these sources in their integration environment.
