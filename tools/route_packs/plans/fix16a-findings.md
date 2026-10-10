# fix16a behavioural findings

Base: `e82aeef30885c04f2c3749b66fca386adf2ea7d7`. Pinned bundle manifest: `9da33481b1b4a0482aaa9cd6b495f6e0c04efeb9a42009bd323f7d114b9ebfd5`.

Inputs were read through manifest bundle_path entries. History was inspected with `git log -p keep/cand-13-final..HEAD -- <affected files>` and older history where that range contained no causal change. Older changes below explain stale assertions; they are not claims of inherited gate failures or passes. No matching baseline receipts were supplied.

| Failure class | Cause and contract evidence | Delivered fix and sibling sweep |
| --- | --- | --- |
| S24/S25/S30/S35/S42 missing foundations | `94162b97` added complete-delivery dependency enforcement; partial row fixtures omit nominated Delamere D05/Gesmerha D09 surfaces. No causal change to the fixture in the requested cand-13 range. Complete assembled source contains both. | Tests build complete dependencies and re-register only the owned row before final controller decorations. S30 exercises register_all discovery/collector restoration with only its own registrar selected. Foundation deletion mutations retain strict full-delivery enforcement. S24/S25/S35/S42 registrar and idempotence siblings checked. |
| Engine Q5 Aranka missing scenes | Same catalog enforcement; its small fixture models Aranka, not the full Arueshalae reaction inventory. | Explicit fixture relationship scope; production/CLI retains full inventory. Missing-delivery and non-live producer mutations checked. |
| Row registry difference | `67ac2432` added reviewed S04 metadata, but expected rows omit S04 and metadata omits reviewed living ending hosts. J03 contracts require Religion/evidence/Word/retry/disclosure structure. | Update registry and S02/S41/S04 host metadata; classify S04 retry. Remove the blanket paragraph assertion invalidated by approved prose decoration. All rows' exact surface classification remains tested. |
| Arsinoe native soul aftercare | `e62d94c4` (fix15) intentionally permits non-romantic physical presence after closure. Fix15 body/correspondence rules distinguish closure from actual absence. | Put Arsinoe in the central living-after-refusal class and update tests. Death/absence remain blockers; closed plus physically present permits aftercare. Anevia/Irabeth class siblings retained. |
| S49 visited history | `e62d94c4` deliberately removes the visited ban, as do S24/S25. Reviewed S49/fix15 plans require a current body, not lack of a historical visit. | Tests allow visited plus current presence and reject history without the current body. S24/S25 visited and S35 released-prison/complete-versus-meeting alternatives checked. |
| Kiana stance/no outcome | `a6350549` fix14-a extends delayed replies to morning; `a1b6fa75` approves prose fills. Reply dispatch now precedes her decision. | Walk each early dispatch/reply/delivery sequence before asserting stance outcomes; assert no premature stance, commitment or separation at dispatch. Company and rehearsal siblings checked. |
| Herrax threshold2 / foreign actor | `6f89a003` heat host sweep changes the reviewed cut's source digest; exact classifier fails closed and skips its structure transformation. Struct3-a cut contract still requires the same presence-safe partition. | Refresh classifier digest only. Keep authored text, answers, IDs and targets intact. Threshold2 and actor-presence partitions checked by struct3-a tests. |
| Areelu departure / earned-presence readers | `3cfccae3` struct3-b creates the postwar report.departed receipt without a P1 reason. It is future history, not a campaign physical departure; the living afterword forbids it. | Add reasoned exemption, keep campaign gone strict, use fresh exports in cached-export tests. Sibling Nidalynn visitor-chaplain departure (`e7ecf8c9`) receives a reason distinguishing the dismissed visitor from Nidalynn. Fresh export additionally exposes T5's rejection of Irabeth native-life-or-earned-return predicates on Anevia surfaces (`36140421`): prove under the actual death that presence implies a serialized relationship/epoch return, which must independently pass the earned-path check. An unpaid-native-branch mutation remains rejected. Gesmerha transient-receipt mutation now targets the named current finale gate instead of an obsolete positional Derived entry. |
| Chivarro brief schema | `dc880635` coordinator installs the canonical single-source brief (`source.node`), replacing source_nodes. | Test accepts the canonical schema and retains compatibility with older multi-node briefs. Installed default brief siblings checked. |
| Arueshalae dream variants | `814c3df2` approved first-dream fill resolves placeholders introduced by `4a3dde45`; placeholder prose is not a behavioural contract. | Assert registered node targets and native-history answer partitions, keeping answer positions/targets. Other callback-history partitions retained. |

## Scope and validation limits

No player-visible text was edited. Source narrative/multiline literal comparison and newline-style comparison against the base passed. IDs and answer targets are unchanged; save ID comparison against the declared base export is additional finding evidence, not a sealed runner receipt.

The full structural validator separately reports six uncovered textless nodes: Eritrice reconciled_debate/exchange; Areelu report.graft/after, crossroads/end, dagger/end, visitors/end; Chadali epilogue.declined/page. Their ownership is the C4 coverage job and the Eritrice, Areelu and Chadali route owners. This lane cannot add prose or guess paragraph guards. Both candidate resolutions (supply the intended paragraph, or repair the intended visibility guard) require their contracts/owners. S35 validation now checks its owned row; the global findings remain escalated.

Out-of-scope overlay drift (C3b), draft-contract C4 tests, and fix16b pinned-text tests were not changed. Proposal: migrate other legacy include_harem=False registrar fixtures to complete dependency fixtures under their owners.

Runner admission owns fresh receipts, staging, commits and pushes. The final response leaves gates empty and reports check results separately. Cancelled and superseded failed diagnostic runs are not gate passes.

## Implementer check evidence (unsealed)

All paths below are disposable system-temp logs, not runner receipts.

| Check | argv / configuration | Exit / result |
| --- | --- | --- |
| Final regeneration | `python expansion.py`, `RRT_STORY_OUTPUT=/tmp/fix16a-final-story.json` | 0; 4095 scenes; `/tmp/fix16a-final-regeneration.log` |
| Changed tests | `python /work/Writer/tools/jobs/changed_tests.py /work/wt/RRT-fix16a e82aeef30885c04f2c3749b66fca386adf2ea7d7` | 0; 207 tests; `/tmp/fix16a-changed-tests-final.log` |
| Supplemental | `python -m unittest tests.test_eng7_l07_contracts.InventoryContracts.test_clean_required_checks tests.test_struct3_a` | 0; 7 tests; `/tmp/fix16a-supplemental.log` |
| Save/encoding | `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io` | 0; 22 tests; `/tmp/fix16a-final-savecompat.log` |
| Payoff | `python tools/payoff_lint.py --story /tmp/fix16a-delivered-story.json` | 0; 42 routes, 0 hard; `/tmp/fix16a-final-payoff.log` |
| Departure | `python tools/departure_lint.py --strict --story /tmp/fix16a-delivered-story.json` | 0; 43 women, 0 hard; `/tmp/fix16a-final-departure.log` |
| Save IDs | Writer id_guard.check API using the declared base committed export and fresh temp export | 0; lost=[], shrunk=[]; required exact runner CLI remains unrun here (exit null) |

The two temp exports are byte-identical: SHA256 `b9cbb4d519bde211b7754fb59592918d1491cbb51797df4109eeeb2afc999af8`. Tests/lints that read a file used the first identical export; fresh_story tests rebuilt current source.

Diagnostic runs before corrections failed (changed_tests exits 1; targeted runs exits 1; one early small run exit 137). Two broad superseded diagnostic sweeps were cancelled with exit 143. None are presented as passes. Exact default-path payoff/departure commands and the exact runner id_guard argv were not executed here (exit null); the wrapper owns their fresh receipts. No inherited gate status is established.
