# Vellexia round 3 implementation report

Base: current `r3-vellexia` checkout, including merged shared ending work. No commit, per the final task instruction. No independent score is claimed.

## CHANGES

| Audit cap / defect | Disposition | File and reason |
|---|---|---|
| COX cap: captive mirror performs bodily actions in Last Call | verified-fixed | Current shared `lastcall_partners.py` call uses only her distant voice and laughter. The romance page still forbids `kept_as_mirror`. No shared edit. |
| INT: Storyteller speaks Vellexia's binding explanation | fixed | `storylines/vellexia_trickster.py`: both `reading` nodes explicitly name Vellexia and her verified unit, as `undone` already did. |
| BEL: unexplained footstool, Storyteller unmirror | fixed | Same file: both early crating and late purchase carry a salon footstool with the mirror; porters unload it beside the opened crate before the demonstration. |
| BEL: unexplained footstool, stores unmirror | fixed | Same file: Garms removes that footstool from the delivered crate before the demonstration. |
| BEL: all disclosed lessons converge on furniture magic, Storyteller visit | fixed | Same file: retain the legacy mirror reply; append likeness, prediction, provocation and unfinished-evening replies. The likeness explanation explicitly preserves hands that cannot cast and identifies the charm's catch. |
| BEL: disclosed lesson collapse, quarters visit | fixed | Same shared route-local visit generator applies the identical history partition at both hosts. |
| BEL: withheld secret always means practising furniture magic, Storyteller visit | fixed | Same file: appended replies investigate the charm/painter, wine-factor's information, retaliatory gossip or the abandoned entertainment, respectively. |
| BEL: withheld-secret collapse, quarters visit | fixed | Same shared visit generator; existing onward shell choices and lesson/secret receipts are copied without changes. |
| BEL: painter's sitting accepted before disclosure, Storyteller likeness | fixed | Same file: `spell` ends at the fee, with acceptance and postponement. Only the appended `sitting` node performs the sitting and sets its existing cost before `wake` grants the return. No additional charge or requirement. |
| BEL: automatically accepted sitting, stores likeness | fixed | Same route-local likeness generator applies the explicit bargain to both hosts. |
| BEL: unresolved mirror remembers unplayed threat | fixed | `storylines/vellexia_campaign.py`: base ending recalls only the transformation. `vellexia_trickster.py` appends the remembered threat after every existing mirror paragraph, gated on `cost.watched` or `kept_as_mirror`. |
| COX: Last Call bodily actions for glass | verified-fixed | Current merged shared call is body-neutral; regression asserts this and exclusion from the romance coda. |
| VOI: Last Call says she is never bored | verified-fixed | The merged call instead has her mock dreary instalments and waiting. It contains no defining-appetite reversal. |
| VOI: retired returned-woman greeting | fixed | `storylines/vellexia_campaign.py`: the second Drezen invitation complains that dying crusaders monopolize the Commander's attention. |
| VOI: retired borrowed-cloak staging | fixed | `storylines/vellexia_trickster.py`: she appropriates an officer's mantle, removes the badge and displays the silk lining among soldiers. |

`tests/VellexiaTricksterTests.cs` updates the obsolete automatic-sitting assertion to check both voluntary fee branches and paid returns.

`tests/test_vellexia_round3.py` checks five histories at both visit hosts, given/withheld responses and their existing receipts, both painter hosts and refusal without return, both speaker assignments, both deliveries/unloads, gated mirror memory and the merged mirror-safe Last Call.

The existing epilogue explicit-slot brief now specifies `narration: third-past`. No explicit prose was generated. The existing first-night slot remains intact.

## CLASS SWEEP

Checked both mirror acquisitions, both unmirror hosts, both likeness hosts, both physical visit hosts, the later shell conversation, acquisition-specific ending consequences, mirror ending paragraphs and current Last Call/coda. The later shell conversation repeated the furniture-magic defect; it now has appended history-specific follow-through while preserving both legacy mirror callbacks. Existing ending variants already distinguish mirror, diminished and social secrets; retained them.

Verified native archive/localization: Vellexia unit `a32a07903e428d34cb0e98a804d40569`; native mirror cue `42429350764f92140b293b24039b89ef` contains only her protest before transformation; boredom cues `1447842e408f6624abd1187ee1cf5340` and `c06e6223610c82c4c8cd43a60f2abc53`; furniture-release price `834295fb4d1eade489494f6759972074`. New lesson replies and transport staging are authored continuity for the existing devices, not new native lore. No foresight/echo, partner, return device, attraction gate or reconciliation requirement was added. Existing Trickster restrictions and earned outcomes remain.

## GATE

- `PYTHONHASHSEED=0 python expansion.py` with the build-script parent bindings: PASS, 3,848 scenes.
- `python -m unittest tests.test_vellexia_round3 tests.test_vellexia_round2 -q`: PASS, 16 tests. Repeated the same tests against the final generated export: PASS, 16 tests. The new regression class then adopted the existing isolated `fresh_story` fixture; `RRT_TEST_STORY=development/Story.json python -m unittest tests.test_vellexia_round3 -q`: PASS, 6 tests.
- `python tools/savecompat.py`: PASS, 0 hard failures.
- `python -m unittest tests.test_utf8_io -q`: PASS, 1 test.
- `python tools/payoff_lint.py --strict`: PASS, 42 routes, 0 hard failures; existing REVIEW notes retained.
- `python tools/departure_lint.py --strict`: PASS, 43 women, 0 hard failures; existing Mielarah review retained.
- Full C# `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json`: FAIL on the unrelated Eritrice condition listed below. Executed from a temporary source copy to keep all `obj/bin` outputs outside the repository. Initial attempts encountered the environment guard and .NET's artifacts-path launch mismatch; corrected the execution setup.
- C# `--suites VellexiaTricksterTests,VellexiaCampaignTests,VellexiaOpeningTests`: PASS, 5,327,663 assertions in 3 suites. This also invokes `Rules.Validate` on the full generated story. No selectable-answer failure reported.
- `python tools/rrt_verify.py --strict`: PASS, 0 hard failures; 0 shipped structural errors and 0 draft contract diagnostics (887.5 seconds). Reports directed to system temporary files.
- `python -m unittest discover -s tests -p "test_*.py" -q`: FAIL, 1,125 tests in 6,277.295 seconds; 39 failures, 9 errors, 1 skipped, 1 expected failure. Executed against this checkout from the temporary validation directory with its relative-file and Git context preserved. No Vellexia test failed. Shared/other-route failures are inventoried below; no out-of-scope repairs attempted.

Direct comparison against HEAD already verifies prior route node order and answer identities. Both edited source files retain CRLF with zero bare LF; `git -c core.whitespace=cr-at-eol diff --check` passes.

## ESCALATE

- Full C# gate: `Unknown condition eritrice.council.chadalis_essence in eritrice.council.protection_cancelled` (`Program.cs:864`). Another route owns this condition; no edit attempted. This prevents certifying the unfiltered progression gate, despite the passing Vellexia suites.
- Full Python discovery cannot be certified. Failures include Herrax live-outcome proof; Devarra/Dorgelinda late-readiness assumptions; Eliandra/Galfrey Last Call witnesses; Kiana appended-node expectations; Mielarah location staging; native etude/echo/harem inventory drift; outdated roster/guide counts; Nidalynn wrapping counts; Nocticula/Shamira availability; Arsinoe text-lint inventory; presence-exception mutations; Jerribeth/Soana/Wenduag/Irabeth stance assumptions. Errors include `engine_eng3_ab.py:96` indexing a missing stance paragraph after mutable-generator tests, a Minagho therapy-count lookup, stale combined-run guides, and the environment guard terminating a shared test-selection `dotnet build` with status 143. These need shared engine, inventory, guide or other-route reconciliation, outside this route's named entries.

| Full-suite test module | Failures | Errors |
|---|---:|---:|
| `test_earned_outcomes` | 6 | 0 |
| `test_engine_q7_l12` | 1 | 0 |
| `test_etude_lifecycle` | 1 | 0 |
| `test_foresight_echo` | 1 | 0 |
| `test_harem_inventory_scenarios` | 3 | 0 |
| `test_ideal_run_regression` | 1 | 0 |
| `test_lastcall_history_inventory` | 1 | 0 |
| `test_native_fact_inventory` | 0 | 1 |
| `test_nidalynn_partner_claim` | 1 | 0 |
| `test_nidalynn_round2` | 1 | 0 |
| `test_nocticula_partners` | 1 | 0 |
| `test_player_text_baseline` | 0 | 1 |
| `test_player_text_lint` | 1 | 0 |
| `test_presence_exception_export` | 1 | 0 |
| `test_run_guide_check` | 18 | 5 |
| `test_stance_agency` | 2 | 1 |
| `test_test_selection` | 0 | 1 |

- The existing late-party explicit-slot brief remains blocked on save-safe paragraph insertion. The runtime uses numeric paragraph positions; inserting between its existing threshold and morning would renumber legacy cues. Shared engine support is outside scope. Retained the brief and corrected its narration setting, without inserting or reordering paragraphs.
- The task names `tools/route_packs/voice_locks.json`, but it is absent in this checkout and the checked central/repository locations. No lock entries were available to compare. The coordinator must reconcile any locks omitted from this base.

## PROPOSE

None. No additional mechanics or route redesign implemented.

## RISKS

No game/harness run or independent audit. Static and regression checks do not establish rubric scores or native runtime rendering. Shared Last Call changes were verified in the current code, not rewritten. The late-party explicit insertion remains a documented shared dependency. The generated export was restored byte-for-byte to HEAD after validation. Temporary validation projects, build outputs, scripts and logs were removed. No commit. The full integration gates remain ungreen for the recorded shared/other-route failures.
