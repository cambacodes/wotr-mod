# S16 implementation — Galfrey / Konomi

Authored RRT addition, hs-C fields 1–11: the public dispatch correction, its
courier, text, replies, and deed/cost witnesses are new situations. They do not
alter a native order, imply a played council rank-up, or rewrite any native
death, slide or history. There is no echo and no intimate slot (respect ceiling).

## CHANGES

- `storylines/harem_rows/s16.py`: one protected Ch5 errand and its 48-hour retry,
  with mutually exclusive queen/Kitrane × office/post wrappers. All wrappers
  share the sheet's completion witnesses and fixed choice indices. Implements
  the DC22 handling check, labour alternative, pending failure, final failure,
  refusal and effect-free Later answer, with exhaustive terminal receipts.
- The same module applies the shared lore corrections at both entry points:
  current page/Trickster/Table, relationship eligibility, closure, live Galfrey,
  named loss/epoch gates and actual physical contact. Konomi's established post
  channel requires its address/letter terms and supplies no bodily contact.
  `ContactUnit`/`AdditionalContactUnits` check the visited actors without adding a native
  answer-list injection or turning a messenger into Galfrey. Separate replies
  are carried by the Commander, so no prohibited direct exchange is staged.
- `storylines/harem_rows/__init__.py`: exact coordinator-supplied discovery
  module. `story.py`: only the explicitly authorized discovery hook and a local
  payload scene-list copy, preventing repeated builds from appending row scenes
  to the base list. Existing scenes/nodes/answers are unchanged; CRLF preserved.
- `tests/test_harem_row_s16.py`: branch walks, exact receipts, shared clocks,
  channel distinctions, earned-page history, later-loss veto, post conflict,
  and repeatable isolated registration. No C# registration or shared test edit.

## CANON / CLASS SWEEP

Reopened `/wrath/blueprints.zip`:
`World/Crusade/RankUps/Diplomacy/Diplomacy_6/Cue_0084.jbp`, asset
`54c35c2fd573e18438883d534b2bd961`, localization key
`26711ae7-5701-460e-aa88-70cd74517eff`. Its enGB text shows Galfrey's silent
anger at Konomi. This is a voice/conflict anchor, not a trigger or proof of the
authored dispatch. The Queen audience asset `AnswersList_0002.jbp` at
`World/Dialogs/c5/DrezenMain_C5/Galfrey/` also resolves. Existing
`galfrey_kitrane.py` and exported presence definitions distinguish living Queen,
returned Kitrane and the Crows' sergeant; only the two women's actual actor IDs
  are accepted. Konomi's native office and returned presence use the existing
`konomi_contact.py` unit; post requirements follow `konomi.capital_letter` and
the current `konomi.reachable_by_letter` adapter.

Swept all eight wrappers and every result sibling for current presence,
authority, postal-versus-bodily staging, chapter bounds, shared witnesses,
non-timestamped delay inputs, outcome-before-deed writes, accidental intimacy,
conditional paragraphs, unallocated echoes and local stance writes. No new
mechanics, costs, attraction gates or reconciliation conditions were added.

## GATE

All commands used `PYTHONHASHSEED=0`. `S` below denotes the final export produced
by `RRT_STORY_OUTPUT=<system-temp>/Story.json python expansion.py`; it contains
3,838 scenes. No generated `development` or `package` file was edited.

| Command/check | Result |
|---|---|
| `python expansion.py` (temporary output) | PASS |
| `python tools/rrt_verify.py --strict --story S` | First full run identified four invalid row-level overrides of a derived predicate. Fixed the entire class by using the existing `present_now` adapter for bodily visits. |
| `python tools/rrt_verify.py --strict --gate-only --quiet --story S` | PASS, 0 hard failures after that fix; all strict checks enabled, report-only analyses omitted on the rerun. |
| `python tools/payoff_lint.py --strict --story S` | PASS, 42 routes, 0 hard failures |
| `python tools/departure_lint.py --strict --story S` | PASS, 43 women, 0 hard failures |
| Row Python discovery | PASS, 5 tests |
| Household Python discovery | PASS, 24 tests |
| Individual harem engine / schedule / smoothing / rest-simulation modules | PASS, 6 / 16 / 23 / 6 tests |
| Savecompat check of final `S`; nine savecompat tests without generator rebuilds | PASS, 0 failures; 9 tests |
| UTF-8 tests | PASS, 1 test |
| `dotnet run --project tests/RulesTests.csproj -c Release -- S --suites=HouseholdTests,HouseholdEngineTests,HouseholdTransactionTests` (retry using compiled build) | PASS, 480 assertions in 3 suites |
| Required unfiltered `dotnet run --project tests/RulesTests.csproj -c Release -- S` | Incomplete: SIGTERM / exit 143. Final attempt passed the coarse payoff, departure/reload epoch, E-Q8-01 and Q8-05 checks before termination; no selectable-answer diagnostic. |
| Required `python -m unittest discover -s tests -p "test_*.py" -q` | Incomplete: exit 143, no failure diagnostics. |
| Aggregate harem discovery; inventory/transaction modules; full savecompat module | Incomplete runs, including exit 143 without failure diagnostics. No passing full-suite claim. |

The first rules validation also identified missing primary contact units; fixed
all eight wrappers using the existing primary/additional contact fields. The
coordinator discovery module is byte-identical to the supplied content, the
existing `story.py` CRLF bytes are preserved, and diff whitespace checks pass
with `core.whitespace=cr-at-eol`. Temporary exports/reports and .NET obj/bin are
deleted after recording these results.

## ESCALATE

Runtime correction to the old B envelope: that sheet prohibited `ContactUnit`,
but Rules.Validate rejects additional actor checks without a primary contact.
The row uses Galfrey as primary and Konomi (office only) as additional contact;
this enforces the later binding attendance rule through existing engine fields.

1. The sheet explicitly permits a departed, living Konomi's existing post.
   `konomi.reachable_by_letter` permits that history, but
   `konomi.harem.eligible` has `DerivedOpenRoutes=[konomi]`; RouteOpen vetoes
   `konomi.epoch_unavailable`, including the private departure. Participants
   repeat that veto. The post wrappers therefore remain unavailable in that
   history. The row does **not** weaken or override those shared guards. Shared
   engine/eligibility ownership must reconcile correspondence attendance before
   enabling that part of S16. Tests reproduce the exact conflict.
2. No assembled general attitude/first-wins F controller is present at this
   base. Per sheet ownership, this row writes witnesses only. Integration must
   consume `retry.failed` (not pending `settle.failed`) with Galfrey as claimant
   toward Konomi, preserving one target and one reconciliation. No local stance,
   enmity, tolerated, closure or reconciliation producer was invented.
3. Integration-owned stage registration: rival inputs are `[[P+ready]]` in each
   direction. Respect inputs are the single AND group
   `[P+correction.delivered, P+galfrey.name_withheld, P+konomi.office_named,
   P+cost.galfrey.endorsement_withheld, P+cost.konomi.joint_cover_lost]`.
   No friend/lover stage. `P=household.pair.galfrey_konomi.`
4. W5 must attach the sheet's historical Ledger/Seating Notes and gated living
   Last Call readers in their shared hosts. These hosts are outside row scope;
   no monkey-patch, extra completion scene or conditional dialogue paragraph
   was introduced. The schedule remains coordinator-owned reserved metadata.
5. The coordinator must complete the broad Python, inventory/transaction,
   generator-dependent savecompat and unfiltered C# gates. Repeated processes
   ended with SIGTERM/143 without actionable assertion diagnostics. Their
   passing subsets and the strict verifier do not certify the unfinished runs.

## PROPOSE

None. The escalations above implement existing approved contracts, not a new
design proposal.

## RISKS

This is source implementation for coordinator integration, not shipped/runtime
certification or an independent rubric score. The post conflict and missing
shared state/readers prevent claiming complete household progression. No live
game, installation, harness or full expansion build was run. No commit made.
