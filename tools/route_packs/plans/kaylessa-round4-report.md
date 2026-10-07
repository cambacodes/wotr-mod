# R4-kaylessa local residue report

Starting commit: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
No commit requested by the final task instruction; changes remain uncommitted.

## CHANGES

| Finding | Status | File and evidence |
| --- | --- | --- |
| kaylessa:D01 | Done; Claude voice review pending | `storylines/kaylessa_wasps.py`, `watching_hands/camellia_killed` and `promise`: removed her ranking herself below Camellia and endorsing the Commander's keeping her killer. Kaylessa draws a sleeve knife, threatens to pin an attacking hand to the table, and makes the Commander face the resulting blood among the guests. The promise response keeps that weapon and responsibility with her. It does not alter either woman's availability or relationship state. |
| kaylessa:D02 | Done; Claude voice review pending | `storylines/kaylessa_trickster.py`, `alive.warning/swap` plants the thin crystal's vulnerability; `alive.amulet_swap/volley` shows an arrow punching through it before the existing burnout and loss of cover. |
| kaylessa:D03 | Done; Claude voice review pending | The successor's `volley_s` shows the same arrow damage while retaining his separate identity and all original outcome effects. |
| kaylessa:D04 | Done; Claude voice review pending | The shared `fumble` predecessor shows the hunter striking the amulet against his stone and cracking its crystal. Both shield histories now reach `beast` with an already demonstrated cause for its dying glare and burnout. No new charge limit, price, check, or magical fee. |
| kaylessa:K01 | Addressed by D02–D04 | The existing permanent disguise cost follows physical damage on all three outcomes. Crystal construction and failure behavior are explicitly authored details of the already authored glamour device, not claims about a native item. |
| kaylessa:D05 | Done | `storylines/kaylessa_wasps.py` records inclusion in the first letter separately from dispatch of a supplement. `storylines/kaylessa_clearing.py` keeps the original letter's existing thirty-day clock, prevents it acknowledging a later supplement, and appends `kaylessa.clearing.courier_reply` with its own thirty-day dispatch clock. Opening either applicable acknowledgment records the receipt. `storylines/kaylessa_trickster.py` makes the courier epilogue paragraph and its ending copies read that actual acknowledgment. `tools/departure_contracts.json` appends only the new scene to Kaylessa's existing physical-presence surfaces. |
| kaylessa:D06 | Out of scope: S43/J08 | Latest S3 ownership assigns the present-day household insertion to shared `storylines/harem_rows/s43.py` and J08. No shared prose or insertion changed. |
| kaylessa:D07 | Out of scope: S43/J08 | The same shared insertion owns the incorrect exit into recalled actions. No released exit changed here. |
| kaylessa:D08 | Out of scope: S2 | Section 4.3 explicitly assigns the acceptance repair to S2. `tests/test_kaylessa_round3.py` remains unchanged. |
| kaylessa:D09 | Done; Claude voice review pending | `storylines/kaylessa_clearing.py`, `once_when_it_counts`: both existing name answers lead to appended `wall`, then the player covers the wounded or draws the swarm across the crossbowmen. Each action shows Kaylessa shooting and the sergeant reacting before the existing aftermath. The roof response names those witnesses. No new combat system, skill check, resource cost, attraction requirement, or outcome gate. |

`tests/test_kaylessa_round4.py` covers late supplements before and after the first reply, the 719/720-hour boundary, original-letter acknowledgment, unearned epilogue acknowledgment, and both performed defense roads. `tests/test_kaylessa_round2.py` updates only the original-letter receipt history for D05. `tests/KaylessaCourierHistoryTests.cs` plays the actual dispatch answer through the production walker, checks 719/720 hours with the first reply both read and unread, opens the separate reply, and verifies its receipt and non-repeat. `tests/KaylessaTricksterTests.cs` invokes this dedicated history for the new scene instead of asking its four older sampled worlds to supply that dispatch; all original courtship checks remain.

`tools/route_packs/plans/voice-review-pending.json` queues all five scenes whose prose was changed or added. None is voice-locked; no prose-pending lock exception was needed. Existing scene IDs, node IDs, choice positions, relationship IDs, and outcome effects remain; additions append. All edited existing files retain their original line endings, including CRLF in the three story modules.

### Character evidence

Native keys below were read directly through the referenced cue blueprints in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`.

| Re-voiced scene | Her want, action, and cost | Native register anchor |
| --- | --- | --- |
| `kaylessa.wasps.watching_hands` | Wants to survive proximity to the woman who killed her; arms herself and threatens retaliation; risks blood and conflict among the Commander's guests instead of surrendering her standing. The sleeve knife does not change custody of her separately tracked Kyonin dagger. | `Kaylessa_main/Cue_0001`, key `3c1bde69-5c33-4e72-a2da-75139575109a`: malicious stare and “What are you looking at, soldier? Like what you see?” |
| `kaylessa.trickster.alive.warning` | Wants her hunter caught in his own ambush; exposes the amulet's vulnerability and plans the swap; stakes the face she uses to buy bread. | `Kaylessa_Reveal/Cue_0039`, key `ef78bd35-8e19-42c1-8b2f-0143680418e1`: her Calistrian vigilante past and attacks on those the law failed to punish. The device and vulnerability remain authored. |
| `kaylessa.trickster.alive.amulet_swap` | Wants to escape the hunter; performs the agreed attack and cover, or attacks him with her hands on failure; loses the disguise, with the existing wound and exposure consequences on failure. | `Kaylessa_Reveal/Cue_0039`, key `ef78bd35-8e19-42c1-8b2f-0143680418e1`. New wording supplies the cause of the established cost, not redemption or a cure. |
| `kaylessa.clearing.once_when_it_counts` | Wants the city and Commander to survive the swarm; shoots from the roof while watching the wall; spends her quiver and is witnessed defending Drezen. Keeps her soldier's mockery after the danger. | `Kaylessa_main/Cue_0073`, key `507bc918-9fbb-455c-9a54-eb69aac0c81d`: “Everyone's a soldier in a war, generals and privates alike.” |
| `kaylessa.clearing.courier_reply` | Wants the dead courier identified; opens the separate answer and keeps it with her account; acknowledgment follows the exposed-name dispatch and actual delivery wait, rather than intent alone. | `Kaylessa_Reveal/Cue_0028`, key `bc247a5c-d792-439f-b57c-d8fff7909afa`: asks for her account to reach Avennara and survive the Winter Council's suppression. This reply is an authored continuation. |

## CLASS SWEEP

- D01: checked `camellia`, `promise`, and the remaining Hands responses. The non-killer branch retains her butcher comparison and watchfulness; the promise sibling now preserves her defiance. No coexistence gates added.
- D02–D04/K01: checked both warning identity branches, successful Forn/successor volleys, the shared fumble, both shield branches, `beast`, and both aftermaths. Existing burn-out consumers still describe the same lost disguise. No extra foresight or echo introduced.
- D05: checked `name`, `courier_unsent`, `courier_followup`, the first reply, all copied courier-acknowledgment epilogue paragraphs, and the unsent-account ending. The unposted ending still describes carrying her account home, without pretending to have received a reply.
- D09: checked both `name` and `name_fresh`, both tactics, the existing aftermath and roof response. Each road has a performed action and witnesses; original nodes remain in their original positions. The aftermath counts twelve arrow kills across the parapet and roofs, so the new wall shots fit her existing twelve kills and empty quiver.
- D06–D08: inspected the shared current-versus-recalled insertion and the stale assembled-story assertion; left them with their assigned owners.

## GATE

Environment: `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, `RRT_GAME_DIR=/wrath`, and the four `RRT_PARENT_BINDINGS` files listed by `build-expansion.ps1`. Generated exports, verifier reports, Python logs, .NET build outputs, timing files, and native-coverage files use a system temporary directory. `RRT_STORY_OUTPUT`, `RRT_TEST_STORY`, and `RRT_TEST_BUILD_ROOT` keep the checks off prohibited `development/` output and repository build folders; `$STORY` below means that fresh temporary export.

| Command | Result |
| --- | --- |
| `python expansion.py` | Pass: 4,055 scenes. Final export regenerated after the new reply's presence classification was added. |
| `python tools/savecompat.py --story $STORY` | Pass: 0 hard failures. A separate comparison with HEAD also preserved every original scene/node position and original answer count. |
| `python -m unittest tests.test_kaylessa_round2 tests.test_kaylessa_round4 tests.test_utf8_io -q` | Pass: 15 tests against the final export, after the speaker-attribution and arrow-census corrections. |
| `python -m unittest tests.test_kaylessa_round2 tests.test_kaylessa_round3 tests.test_kaylessa_round4 tests.test_utf8_io -q` | 24 tests, one failure: the unchanged D08/S2 assertion expects `['ride', 'longer']` instead of the assembled `['ride', 'longer', 's43_road']`. The other 23 checks pass. |
| `python tools/payoff_lint.py --strict --story $STORY` | Pass: 42 routes, 0 hard failures; existing review notes retained. |
| `python tools/departure_lint.py --strict --story $STORY` | Pass after registering only Kaylessa's new physical reply surface: 43 women, 0 hard failures. |
| `python tools/voice_lock_lint.py --strict --story $STORY` | Pass: 576 locks, 0 changed, 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --known-rebuilds --story $STORY` | Pass: 320 briefs, 0 hard, 315 known rebuild findings, 168 warnings. No explicit slots changed. |
| `python tools/rrt_verify.py --strict --gate-only --story $STORY` | Exit 1: 14 hard findings, comprising 13 diagnostics in locked Jerribeth prose and one newly exposed speaker-attribution diagnostic in Kaylessa's amulet preparation. Fixed the Kaylessa line attribution with explicit handling of the crystal and cord, regenerated, and reran the exact player-text lint/baseline and text-structure checks used by the verifier: 13 current player-text hard diagnostics, all Jerribeth; 0 Kaylessa hard diagnostics; 0 text-structure hard/review diagnostics. All other strict hard buckets were empty. A project-wide zero cannot be supplied within this route's authorized scope. Gate-only retains every strict hard check and defers report-only world/budget analyses. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- --suites=KaylessaTricksterTests,PayoffDepartureRulesTests,ContactDisambiguationTests $STORY` | Initial run reached the courtship inventory, then failed on the new reply because the four old sampled histories did not supply its dispatch. No page-without-answers error. Added the dedicated played-dispatch history described above; did not repeat the lengthy old-history search. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- --suites=KaylessaCourierHistoryTests,ContactDisambiguationTests $STORY` | Pass against the final export: `Rules.Validate` plus 91 assertions in two selected suites. Both new timing roads walk to a selectable acknowledgment; no page-without-answers error. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | Attempted; host test guard terminated it with exit 143. Not a completed gate. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- $STORY` | Attempted; host test guard terminated it with exit 143. Not a completed gate. |
| `git -c core.whitespace=cr-at-eol diff --check` | Pass. CRLF preservation checked in each edited story module. |

The host policy is `/work/testguard.sh`, which classifies full Python discovery and RulesTests without `--suites=` as full suites and kills them in route worktrees. Its log explicitly records both R4-kaylessa commands as `kill(full)`. No guard, allow-list, coordinator worktree, or host configuration was changed to bypass this restriction.

All five standalone lints above were rerun on the final export and retained the stated results. Temporary exports, logs, verifier reports, timing files, build outputs, and Python cache directories were removed before handoff.

## ESCALATE

- D06–D07: S43/J08 must stage `s43_road` under the present awning and give it a present-day exit, with a history where settlement follows the recalled night.
- D08: S2 must repair the acceptance assertion that mistakes the appended `s43_road` choice for a remembered action. The focused Python run reproduces this exact failure.
- The coordinator must run the two broad test commands in an authorized full-gate worktree; the host terminated both route-worktree attempts with exit 143.
- The strict verifier's 13 remaining diagnostics are all on locked Jerribeth scenes, outside the Kaylessa scope. Review belongs to the Claude prose owner/shared lint coordinator; no Jerribeth text or global exception policy was edited. Exact surfaces:

| Locked scene/node | Reported diagnostic |
| --- | --- |
| `jerribeth.farewell/traitor_fed` | commander-gender |
| `jerribeth.farewell/discovery_distant` | speaker-attribution-review |
| `jerribeth.ending_together/catalogue` | commander-gender |
| `jerribeth.ending_ascended/catalogue` | commander-gender |
| `jerribeth.offered_signature/companion_regill` | commander-gender |
| `jerribeth.counterfeit_guest/maker` | commander-gender |
| `jerribeth.counterfeit_guest/square` | commander-gender |
| `jerribeth.counterfeit_guest/scout_known` | embedded-commander-speech |
| `jerribeth.counterfeit_audience/challenge` | commander-gender |
| `jerribeth.counterfeit_audience/leverage.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/departure.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/raid_dismissed` | commander-gender |
| `jerribeth.counterfeit_spoil/object` | commander-gender |

- Shared J01–J10 contract/controller/native-runtime work and Claude rebuilds remain outside this route patch. In particular, no changes to `household.py`, `lastcall*.py`, `trickster_world.py`, `scene_kinds.py`, or the S43 insertion. No native/runtime repair was necessary for the authored amulet damage.
- Kaylessa's pre-existing payoff-contract review note about a separately stored late yes is shared contract/spec work, not a new requirement implemented here.

## PROPOSE

None. No additional mechanics or route redesign proposed or implemented.

## RISKS

- Claude's queued voice pass and the independent coordinator/auditor review are still required; this report does not claim scores of 91 or higher.
- Shared D06–D08 residuals remain on the starting branch until their owners integrate their repairs.
- The broad Python/C# commands remain host-blocked, the revised full Kaylessa sampled-world suite was not repeated, and project-wide strict verification remains blocked by the 13 locked Jerribeth diagnostics. The new dispatch fixture and final route-local gates pass; this is not a blanket full-suite pass.
- The added reply preserves the existing committed, present Kaylessa contact window. No departure correspondence or earned-return bypass is introduced.
- No refused beats. No commit, merge, full mod build, harness, or game run.
