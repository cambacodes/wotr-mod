# Targona — round 2 implementation

Uncommitted implementation of the supplied set-piece and turning-point plans.
The atlas reservation overrides the older TP sheet's proposed uniqueness tuple:
`isolation_via_canon_events`, Drezen's pikeman/stove/shared dawn vigil,
healer chooses desire during the watch and returns to her patients.
The copied planning sheets describe their original planning-only pass; this
document records the subsequent implementation.

## CHANGES

| File / finding | Implemented result and reason |
| --- | --- |
| `storylines/targona_trickster.py`; P1 1–7, F1 1–6 | Ordinary wands are activated by the qualified infirmary chaplain. Commander buys supplies, changes dressings and watches patients. Both report destinations credit those separate hands; every arrival explanation accommodates either existing wand history. Exhausted wands crumble; both dawn choices gather splinters, and Ember plus all three keepsake-ending readers describe linen bundles beside the receipted bill. Existing UMD2 split, −300 Favors, −500 Finances and effects survive. |
| Same file; S2, TAR-01/02 | Each truth/lie/her-answer deathbed branch includes the veteran refusing a prayer, her stopping to hear his requested message, and an impatient officer whom she makes wait. The existing ward report carrier takes knife/message and brings back receipt of delivery. No new courier price or romance condition. At the stove her grip or anger continues to distinguish attraction from approval. |
| Same file; S3/S4, TAR-03, registered turn | The dawn watch needs two caregivers. Repeated interruptions delay what she wants to say. Her affirmative answer owns wanting the Commander beside her after the patients are gone. Shared-watch tenderness and the alternative brother-oath's fierce relief have separate first-night approaches and waking affection. Patients react to the morning, she puts them to work, Wilcer opens stores, and Seelah ribs the Commander while helping the ward. Neither rescue nor a slot creates commitment. |
| Same file; S5 | Targona checks coverage herself and tells the chaplain about the inspection lie before leaving. He reacts and keeps the existing volunteers at the cots through the second bell. Existing paid coverage also visibly receives her inspection. She initiates the wall/guardroom interval, returns at the second bell and resumes a dressing. No deferred confession debt, new payment, gate, scene or promised extra coverage. |
| `storylines/targona_opening.py`; P1 23–24, F1 16–19 | Common first-letter passage establishes complaint space for every reply. Targona sends the requested copies and keeps the original; ward correspondence reflects scarce shared time, rather than impossible lack of awake contact. Successful folds are stated once. All found/failed/cut and public/private branches survive. |
| Same file; S5 heat/voice sweep | Wing contact produces a flinch and her own redirected hand before renewed kissing. Desire is not penance. The copied key is disclosed to the porter, who reacts; no new key mechanic. Existing road/postern inspection, failures, pauses and walk/talk/kiss choices remain. The existing account/public/private pages already contain her concrete rejection of Areelu's justification (TAR-04 ADAPT); no new present-day Areelu encounter or jealousy is invented. |
| `storylines/targona_trickster.py`; P1 17–22, F1 20–21; S6 | All open ward-ending siblings read the existing route-open predicate. Closed refused-promise farewell keeps its identity and reads only actual losses with the established laboratory-return override. Late invitation receives the Commander's answering hand before she leads upstairs. Living ending shows an actual return and her kiss; broken-oath paragraph carries the existing year of distance. Sacrifice opens with the tied dressing and dropped scissors, never a living reunion. |
| `tests/test_targona_round2.py`; P1 28, F1 22 | Generated-output regressions cover seven unavailable states across eight endings, the closed farewell, unchanged prices and acceptance receipts, alternative first nights, effect-free slot continuations, legacy exits and five production anchors. An expected-failure regression explicitly inventories the eight out-of-scope historical/prayer guards. |
| `tools/route_packs/plans/targona-{setpieces,tp}.md` | Copied the required sheets from their respective remote branches, without merging branch code. |
| `tools/route_packs/turning_points.json` | Registers only Targona's authoritative atlas entry, including verified native references. No other route entry is added or edited. |
| `tools/route_packs/explicit_slots/targona/*.json`, `plans/targona-slot-addresses.json` | Copies all five supplied briefs and records exact production addresses. Three slots are appended effect-free nodes. L4/L5 are named unconditional paragraphs interpolated within the old node's Text: the source mapping gives each its full production ID without inventing a runtime Paragraph field, changing existing paragraph indices, or adding conditional prose to ordinary dialogue. Defaults are heated cuts; no explicit prose was written. |

Debts collected: paid ward work receives correctly credited reports/remnants;
the veteran's message receives delivery acknowledgment; the first asking's
shared vigil reaches dawn; only the alternative promise earns `light_sealed`;
covered cots permit the chosen hour and second-bell return; requested copies,
honest failed work and her public/private answer remain in the correspondence;
living affection has a shown homecoming. Lariel never answers a miracle.

No canon partner is established for Targona. Partner discovery/stance scenes
are inapplicable; the morning's public discovery involves ward patients and
Wilcer, not an invented spouse. No Targona echo is allocated. Shyka's page
supplies neither affection nor service, and no new foresight gate is added.

## CLASS SWEEP

- Both ordinary report destinations, five arrival recollections, both dawn answers,
  all Ember wand siblings and every `WARD_PARAGRAPHS` consumer.
- All three pikeman answers; attraction/colleague exits; early/dawn refusal,
  first commitment, alternative promise/refusal and every first-night continuation.
- Friend/lover × ward/wayhouse correspondence; all fold/publication outcomes;
  guarded-postern/public-road/failure and all visit/key off-ramps.
- All eight ward epilogues, living/sacrificed/returned Commander distinction,
  oath-kept/broken paragraphs and actual Seelah/Ember availability.
- Retained retired death-return/washing nodes and unregistered acquisition draft
  inspected; no return producer or draft registration was activated.
- Integration-relative inventory reports no scene/node/choice identity loss or
  reorder. Three existing Continue targets route through their new cut nodes;
  every existing other choice field is unchanged. Legacy ending and wayhouse
  exits remain inert. Both edited source files retain CRLF with zero bare LF.

## GATE

All commands used `PYTHONHASHSEED=0`. `STORY` denotes the fresh system-temp
export; generator parent-binding paths match `build-expansion.ps1`. Tests using
the export received `RRT_TEST_STORY=STORY`.

| Command / check | Result |
| --- | --- |
| `RRT_STORY_OUTPUT=STORY python expansion.py` | PASS on the final source, exit 0; 3,755 scenes. Generator labels its output INCOMPLETE DEVELOPMENT EXPORT, as in this authoring environment. No generated development file edited. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_targona_round2 -q` | PASS, 19 tests; one expected failure documents the shared classifier residual. The original 12-test save/UTF-8 gate also passed separately. |
| `python tools/payoff_lint.py --strict --story STORY` | PASS; 42 routes, zero hard failures. Inherited Targona late-readiness REVIEW retained. |
| `python tools/departure_lint.py --strict --story STORY` | PASS; 43 women, zero hard failures. |
| `python tools/rrt_verify.py --strict --story STORY --game /wrath` | Initial complete run caught two instances of one ambiguous brother-oath pronoun, classified as Commander gender. Fixed by naming Lariel directly; no structural/save failure. Necessary post-fix strict recheck with `--gate-only` PASSED, exit 0, zero hard failures. That flag retains every strict check and omits report-only analyses. JSON/text reports directed to system temp. |
| `python -m unittest tests.test_targona_round2 -q` on final export | PASS; seven tests, one expected failure for the eight shared-classifier surfaces. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE; initial and retry processes exited 143 without a unittest result or failure diagnostic. Not claimed as a pass. |
| `dotnet run --project tests/RulesTests.csproj -c Release … -- STORY` | Build passed with obj/bin redirected to system temp; CLI launcher then sought the default repo executable and failed. Launched the built DLL directly from temp as the equivalent execution fallback. Full execution exited 143 after initial engine suites passed, without a failing-page diagnostic or final result. |
| `dotnet TEMP/RulesTests.dll --suites TargonaTricksterTests,TargonaOpeningTests STORY` | INCOMPLETE; exited 143 without a final result. |
| Integration-relative save inventory / choice-field comparison | PASS; zero lost/reordered identities; only three planned effect-free Continue reroutes. All legacy ending exits retain original mechanics. |
| `git -c core.whitespace=cr-at-eol diff --check`; source byte scan | PASS; zero whitespace defects, zero bare LF in the two existing CRLF route files. |

No failure diagnostics accompanied the exit-143 processes; their cause is not
inferred. No broad suite is represented as passing. All temporary exports,
logs, reports, .NET outputs and task scripts are removed before handoff. No
commit, packaging script, harness or game execution.

## ESCALATE

- Shared historical/religious classifier: P1 8–15 / F1 7–14 remain eight
  erroneous generated surfaces: `unasked_question/start[0]` (Areelu closure),
  `the_folded_room/study[0]` (Irabeth absence), both scene guards on
  `an_unpromised_future`, `spent_light/start[1]`, `after.ward/dawn[1]`, and
  `the_names/start[1:3]` (Iomedae closure). These are past references/prayers,
  not live participants. Shared code/lints were not edited or bypassed.
  P1 16 / F1 15 no longer reproduces on Seelah's required rewritten reaction;
  Seelah's own presence/return guards remain.
- Shared `lastcall` files: P1 25–27 require neutral `targona.lastcall.call`
  entry, with actual Lariel pleas confined to its existing call/breach choices.
  The coda also needs a shown living return while preserving its year of
  distance after breach. These files are expressly prohibited by this task.
  Route-local oath prose cannot repair a plea already voiced at shared entry.
- Any native recap, household or external owning-spec update belongs to its
  coordinator. Authored additions and native evidence are recorded in the
  copied set-piece sheet; no off-path native event was altered here.

## PROPOSE

None. No extra mechanics, prices, attraction thresholds, partner rules,
resurrections, reconciliation conditions or romantic gates were implemented.

## RISKS

- The outstanding shared guards and Last Call entry prevent claiming all audit
  findings resolved or every rubric dimension ≥91. No independent score exists
  for this implementation.
- Eng3's inherited late-readiness REVIEW remains: its legacy effect-free ending
  stores no separate prewar yes. The authorized plan requires an on-page mutual
  answer while retaining that exit and eligibility; no new receipt or condition
  was invented.
- L4/L5 are production-addressed text paragraphs, not serialized Paragraph IDs.
  The coordinator must replace their source mapping values using the address
  manifest, preserving surrounding staging/aftermath.
- Unregistered acquisition-template and dormant historical prose remain dormant;
  their future authorized sweep is not an excuse to add a second acquisition.
