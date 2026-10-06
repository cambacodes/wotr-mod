# MERGE ENGINE ROUND 3 — resolve-eng3

## CHANGES

Uncommitted, scoped three-way integration of `origin/claude/eng3-ab` (`8a75adee`) into integration HEAD `219bcbeb`, using merge base `a68bb988`. The final instruction prohibiting a commit takes precedence. No merge commit or ancestor metadata was written; the coordinator can review the working diff before completing the merge.

| Finding | Files | Resolution |
|---|---|---|
| Preserve integrated route content and eng3 runtime | `src/Story.cs`, `src/Main.cs`, `expansion.py`, new `storylines/engine_eng3_ab.py` | Keep persisted departure epochs, repeated observations, current presence and earned payoff gates; apply the mechanical pass after all integration appenders. All route source modules remain byte-exact to HEAD. |
| Post-base payoff coverage | `tools/payoff_contracts.json`, `tools/payoff_lint.py` | Increase scene/answer surfaces from 297 to 824: 100 Anevia clones, 426 Wenduag clones, and split Arsinoe's mixed late coda into two accepted-answer surfaces. Add four absence/history pages, 90 paragraph contracts, 187 guard sets covering 3,573 existing stance paragraphs, and 265 exact integrated commitment-producer inventories. Acceptance, share/exclusive/secret, refusal and exposure receipts remain the authored ones. |
| Post-base departure coverage | `tools/departure_contracts.json`, `tools/departure_epochs.py`, engine integration | Increase current-availability surfaces from 3,134 to 3,960 and absence/history variants from 419 to 425. Classify the new correspondence, stance clones, endings and living paragraphs separately from mourning/refusal text. Preserve existing return mechanisms and prices. |
| Mixed accepted/refused histories | Payoff contracts, engine integration, contract tests | Gate Arsinoe's two accepted answers rather than the entire late page, preserving the declined business-memory answer. Preserve Terendelev's earned friendship mourning arm through a derived alias over existing returned/declined receipts. Neither change creates a new acceptance condition. |
| Strict verifier on dense integrated dependency graphs | `tools/presence_dependency_lint.py`, `tests/test_presence_dependency_lint.py` | Solve forced observations and independent producers with monotonic work queues, memoize loss contexts, and traverse shared dependencies once. Treat answers producing the same return receipt in the same scene as alternatives; every mandatory composite receipt and common physical staging still needs an independent bootstrap. Mutation checks retain circular-contact rejection. |
| Stale pre-stance own-life index | `tools/own_life_contracts.json` | Remove the obsolete rewire targeting paragraph 0 of the Chivarro epilogue: integration replaced that paragraph with mourning. The live Minagho paragraph remains covered by the existing paragraph-2 life contract and the new current-presence gate. |
| Editorial inventory behind integration | `tools/player_text_baseline.json` | Register the eight already-integrated Minagho therapy-term occurrences. Integration and the merged export contain exactly the same eight occurrences; no prose changes or new text allowance beyond that count. Editorial reviews remain visible. |
| Tests must model completed engine state | Incoming `tests/*.cs`, selected Python tests, managed tests, native-cue fixtures | Retain incoming primitive-observation/earned-history fixture repairs, integration's prose-independent assertions and legacy-exit checks. Rebuild synthetic snapshots from persistent flags, complete current readers, and regenerate policy cases against the final export and `/wrath/blueprints.zip`. |
| Save baseline invocation and stale new-answer assertion | `tests/test_savecompat_baseline.py` | Use the package-qualified fixture import. Match integration commit `219bcbeb`'s new Soana stance acceptance IDs; retain all old abort/continue identities and effect checks. The frozen save baseline is unchanged. |
| Safe writing-phase export | `expansion.py` | Add optional `RRT_STORY_OUTPUT`; its default is unchanged. This allows the prescribed generator command to write to system temp without editing forbidden `development/Story.json`. Explicit UTF-8 contract reads pass the I/O gate. |

Incoming shared checker adaptations remain in `tools/crossroute_checks/{common,mention_context,other_woman}.py`, `tools/{hub_attachment_lint,native_contradictions,own_life_lint,return_provenance_lint,timeline_contract_lint,rrt_verify}.py` and `tools/delivery_inventory2_contracts.json`. They read the new availability aliases while preserving integration's checks. `story.py` already contains the incoming-compatible hooks and required no edit.

### Conflicts and resolutions

All eleven merge-tree conflicts were resolved:

| File | Both intents retained |
|---|---|
| `managed-tests/NativeEpilogueEditManagedTests.cs` | Integration's native archive union and legacy-exit coverage; eng3's earned Anevia receipts and completed state. |
| `tests/ArsinoeTricksterTests.cs` | Structured surface identities; primitive Last Call receipts/current readers. |
| `tests/ElyankaTricksterTests.cs` | Paragraph/count assertions; left-free negative history. |
| `tests/GesmerhaTricksterTests.cs` | Prose-independent surface assertions; primitive Last Call observations. |
| `tests/MinaghoChivarroContinuationTests.cs` | Cooled/refused ending branches; completed current availability. |
| `tests/NidalynnTricksterTests.cs` | Structured rendering/count checks; earned fixture context. |
| `tests/Program.cs` | Integration's selective suite runner and existing guards; eng3's epoch copying, event observation and payoff/departure suite registration. |
| `tests/SoanaLateCampaignTests.cs` | Existing non-Trickster exclusive-refusal/closed-route negatives; current reader completion. Existing mixed line endings retained. |
| `tests/TirabadeChronologyTests.cs` | Structured ending assertions; current availability. |
| `tests/native-cue-policy-fixtures/states.json` | Integration's appended stance-agency cases and IDs; final engine gates. Regenerated from final content. |
| `tests/test_engine_f6c.py` | Integration's retired wife-state negatives; eng3's earned payoff/presence assertions. |

### Added departure inventory

| Woman | Current surfaces added | Absence/history variants added |
|---|---:|---:|
| kiana | 1 | 0 |
| soana | 7 | 0 |
| arsinoe | 0 | 1 |
| anevia | 200 | 0 |
| irabeth | 164 | 1 |
| nocticula | 1 | 0 |
| nenio | 9 | 0 |
| terendelev | 5 | 0 |
| galfrey | 7 | 0 |
| horzalah | 1 | 2 |
| wenduag | 429 | 0 |
| minagho | 1 | 1 |
| chivarro | 1 | 1 |

## CLASS SWEEP

- Compared every assembled scene, node, choice and paragraph against integration HEAD: identical text/order across 3,755 scenes, 21,610 nodes, 34,422 choices and 8,525 paragraphs. Frozen-baseline and integration-relative identity checks report zero losses/reorders.
- Inventoried every payoff ending/Last Call sibling, post-base Anevia/Wenduag stance clone, and stance/partner paragraph. Checked ordinary/late alternatives without replacing existing route negatives.
- Swept the mixed refusal, friendship mourning, deferred acceptance and absent-partner pages; preserved their historical paragraphs while gating their living actors.
- Checked every departure consumer target, including correspondence, books, households, native variants and individual paired seats. Native selectors and replacement pages read the same final gates.
- Exercised mutation negatives for deleted stance acceptance/history guards, lost producer effects, unclassified stance surfaces, mixed late payoff alternatives, repeated departure/reload and circular return dependencies.
- Preserved CRLF files and protected storyline modules. No full Python suite, full RulesTests, packaging script, harness or game was run, following the task-specific milestone restriction.

### Lint residuals per route

`P/D` is the hard-failure count from payoff/departure strict checks. `L` is the inherited late-readiness review: existing specification gates provide readiness, but no separately stored prewar yes exists. These remain REVIEW, not invented acceptance mechanics. Paired rows aggregate their individual departure seats. Friendship rows have departure coverage only.

| Route | P/D hard | Inherited REVIEW residual |
|---|---|---|
| anevia | 0/0 | None |
| aranka | 0/0 | L; native parent-cue suppression lacks verified bindings. |
| areelu | 0/0 | L |
| arsinoe | 0/0 | None |
| arueshalae | 0/0 | L |
| camellia | 0/0 | L; old coffin saves without death witnesses fail closed. |
| chadali | 0/0 | Missing separate late yes, repayment and Last Call deed receipts. |
| delamere | 0/0 | L |
| devarra | 0/0 | L |
| dorgelinda | 0/0 | L |
| eliandra | 0/0 | L |
| elyanka | 0/0 | Shipped producer-derived intent needs specification confirmation. |
| eritrice | 0/0 | Missing separate late acceptance receipt. |
| galfrey | 0/0 | Uncharged payment recaps and plans credited as executed deeds. |
| gesmerha | 0/0 | L |
| hepzamirah | 0/0 | L |
| herrax | 0/0 | None |
| horzalah | 0/0 | L |
| iomedae | 0/0 | None |
| irabeth | 0/0 | L |
| jannah | 0/0 | L |
| jerribeth | 0/0 | L |
| kaylessa | 0/0 | L |
| kiana | 0/0 | None |
| konomi | 0/0 | None |
| melazmera | 0/0 | None |
| mielarah | 0/0 | Opaque expelled loss lacks a reader/producer binding. |
| minagho_chivarro | 0/0 | No engine residual; eight inherited editorial therapy-term reviews remain visible. |
| nenio | 0/0 | L |
| nidalynn | 0/0 | None |
| nocticula | 0/0 | None |
| nurah | 0/0 | None |
| seelah | 0/0 | Settlement/repayment histories lack distinct receipts and variants. |
| shamira | 0/0 | Proposed-only late branch remains retired; no acceptance invented. |
| soana | 0/0 | L |
| targona | 0/0 | L |
| terendelev | 0/0 | None |
| tirabade | 0/0 | None |
| vellexia | 0/0 | L |
| wenduag | 0/0 | None |
| yaniel | 0/0 | Threshold/Fane recap lacks corresponding observed-deed receipts. |
| nocticula.acquisition | 0/0 | None |
| aivu (friendship) | —/0 | None in departure contracts. |
| ember (friendship) | —/0 | None in departure contracts. |

## GATE

All authoring commands used `PYTHONHASHSEED=0`. The export and every build/report artifact were directed to system temp. `STORY` below denotes that freshly generated export. `--gate-only` runs every strict verifier check and omits report-only analyses under the writing-phase policy.

| Command/check | Result |
|---|---|
| `RRT_STORY_OUTPUT=$STORY python expansion.py` | PASS — 3,755 scenes. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io` | PASS — 12 tests. |
| `python tools/payoff_lint.py --strict --story $STORY` | PASS — 42 contracts, 0 hard failures. |
| `python tools/departure_lint.py --strict --story $STORY` | PASS — 43 women, 0 hard failures. |
| `python tools/rrt_verify.py --strict --gate-only --story $STORY --game /wrath/` | PASS — 0 hard failures. |
| `tools/managed_tests_linux.sh /wrath/ $STORY` | PASS — all six construction/load/degradation fixtures, including managed legacy exits. |
| Selected payoff/engine Python tests | PASS — 24 tests; native-policy checks included below. |
| Presence dependency, player-text baseline and native-policy tests | PASS — 23 tests, including dense cycles, composite receipts, optional return alternatives and the eight-to-nine phrase budget mutation. |
| Selected `PayoffDepartureRulesTests` | PASS — 40,204 assertions. |
| Seven conflict-affected C# suites | PASS — 1,841,626 assertions in four suites and 69,497,043 in three suites. |
| Galfrey/Nenio earned controls and Irabeth/pair stance/native controls | PASS — 12,509 and 1,754 assertions in selected suites. |
| Prose/order, frozen and integration-relative save identity, allowed scope, CRLF, whitespace | PASS — no prose/order changes or save identity failures. |

The full-suite boilerplate was not followed because this task expressly limits verification to milestone gates. Source-only C# builds used temporary `BaseIntermediateOutputPath`/`OutputPath`; selected suites ran through the built DLL, avoiding repository `bin`/`obj` output.

## ESCALATE

- `build-expansion.ps1` is outside the allowed edit scope. Incoming eng3 adds `payoff_lint.py --strict` and `departure_lint.py --strict` to its packaging gate; the coordinator must apply that change. The script was not edited or run.
- Completing ancestry/committing the reviewed integration is left to the coordinator under the final no-commit instruction.
- Inherited Aranka bindings, Mielarah loss evidence and old-save death witnesses need verified native/shared-code evidence. Remaining receipt/prose reviews above need separately authorized route work.

## PROPOSE

Resolve the inherited review table in subsequent route polish: confirm late intent, add only specifically authorized acceptance/deed/payment receipts, and verify native migration/bindings. No additional mechanic, attraction/commitment threshold, price or reconciliation requirement was implemented in this merge.

## RISKS

- Untimed legacy saves cannot establish every historical departure/return ordering; the incoming engine's fail-closed behavior is retained.
- Managed fixtures report expected Unity/Mono internal-call and unavailable achievement-counter warnings. They pass construction checks; actual Unity execution and real-save round trips were not tested.
- Passing mechanical gates is not an independent 91+ rubric score. The inherited route reviews and 5,357 player-text review diagnostics remain visible; no DLC-tier prose rewrite was attempted in this engine-only scope.
- The editorial baseline now records eight unchanged integrated phrases. Further additions still fail the strict occurrence budget; editorial quality remains a human review item.
