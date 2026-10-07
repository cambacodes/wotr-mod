# S39 — Galfrey / Nocticula carried undertaking

Authored RRT addition, implementing HAREM-SHEETS-36-41 row 39 and the binding
contract in origin/claude/harem-plan:tools/route_packs/harem/WAVE-PLAN.md.
The berth, orderly, mortal factor, pilot, scout captain, survey and political
undertaking are authored. No native passengers, deaths, quest rewards, portal,
body, item blueprint or native event are changed. No echo or explicit slot is
allocated: the sheet authorizes political respect only.

## Assembly and save layout

`story.py` registers the row at the existing household assembly seam through
`household_pair_galfrey_nocticula.register()`. Shared source files are untouched.
The wrapper invokes the existing integrator first, then appends only S39 data.
Registration is idempotent; each export constructs fresh scenes and readers.

The reserved `open`, `undertaking`, `last_litter` scene IDs and `start`, `sent`,
`kept`, `mistranslated`, `interpreted`, `home` nodes are preserved. Start answer
indices match the sheet. Refusals lead to single-Continue terminals so the actual
response precedes the receipt. All completion flags and expenses are terminal
answer effects; Abort is available only before a deed.

Each scene has a mutually exclusive `.kitrane` presentation wrapper, using the
same witnesses, start choice indices, expenses, clock and allowance. The base
forbids `galfrey.trickster.returned`; the wrapper requires it. This avoids
conditional paragraphs in ordinary dialogue while showing Kitrane withdrawing
her own sponsorship before the Green Crows, never issuing royal orders.
Completion of either presentation suppresses both through the same `.seen`.
No prior IDs, answers or source line endings were changed.

## Witnesses, costs and policy boundary

Preparation pays 200 Finances (50 survey, 150 two courier fares), establishes
the useful survey and mustered sortie, and receives both separate promises.
Settlement shows the factor's marked renewed demand beside Nocticula's earlier
instruction. Diplomacy DC 24 or the 300-Finances interpreter exposes its scope.
Nocticula personally countermanding the levy and removing its collector,
Galfrey/Kitrane publicly withdrawing sponsorship, burning the only survey,
recalling the mustered sortie and answering the factor's accusation all precede
the held receipt. No transportation or reception earns that receipt.

Failed handling leaves the levy, survey and sortie intact and records the
Commander's omitted clause. The one 400-Finances retry carries the complete
demand separately and performs the same concessions. Title insult, exposed
scout and final refusal permanently end this docket, never either romance.
The exact terminal lists are checked in the row test.

`POLICY` exposes the sheet's two respect candidate witness groups, Galfrey's
failure toward Nocticula and that edge's one reconciliation candidate. It does
not produce attitudes, strain, tolerated stance, enmity or reconciliation. The
current shared household still reserves those hooks without producers. The
coordinator must consume these inputs through its first-wins policy; no new
policy or reconciliation conditions were implemented here.

## Attendance, clocks and readers

Every scene uses current Trickster, the paid public page, kept Table, both
current eligible routes, copied ClosedFlag/UnavailableFlags/overrides and
epoch absence guards, Ch5 only, Drezen, manual remote visit and protected
allowance. Galfrey's deliberate kill remains non-overridable. The owner's
Council-fight silence additionally blocks Nocticula until her earned return.
There is no Ch6 fallback, rest letter, optional arc or new cap.

Settlement and recovery wait 48 hours on their actual prerequisite deed
witnesses. No stage supplies a clock. Separately carried exchanges remain
possible with an existing enmity; there is no conversation between the women.
Own-house stance never blocks them.

Historical Ledger and Seating Notes entries retain all outcomes and each cost,
including expense and failure records after repair. Existing Last Call pages
receive only epilogue paragraphs recalling the deed, guarded by the currently
open claimant and her channel. Each has exclusive living/earned-Commander-return
variants. No absent respondent receives fresh speech. The row's Nocticula
reader uses the existing Council and return keys, without a new death binding.

## Canon verification

Reopened in `/wrath/blueprints.zip`, resolving keys against
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

| Native anchor | Asset GUID | Localization key |
|---|---|---|
| Galfrey_Incognito/Cue_0010 | 85cfdab678616fd4f9666352f75a45cf | 13e07068-5a48-4cb6-903a-d6b75c94ffdf |
| Galfrey_Incognito/Cue_0017 | 876d21647a935ba4fab1249ce7fa6fbc | f70f9108-4165-42c9-a515-55ec43c5bd60 |
| c4/Nocticula_main/Cue_0523 | b84ef61b070e9cb4e84f142dc8c04cdb | 049612f7-955f-4727-a3ff-e39dfa29f754 |
| c5/Drezen_Under_Siedge/Goddesses_Summit/Cue_0045 | 909f6c75bd0169047806f1493f971e8a | e040a4de-fe20-4b27-a284-8977a913290f |

These establish duty, independent paladin action, Nocticula's rank and political
deception, not an existing treaty or desire between the women. Nocticula's
slavery and coercive patronage remain; Galfrey condemns them even when she
acknowledges this narrow countermand.

## Acceptance

The row test checks exact writes, expenses, DC, frozen answer positions,
pre-deed Abort, policy isolation, identity exclusivity, paid-page/live-path
gates, both closures, deliberate kill despite return, epoch absence, Council
silence/earned return, own-house, separate enmity recovery, deed clocks,
single completion, Ch6 exclusion, every historical cost and Last Call survival
variants. Household engine tests cover the shared saved allowance semantics.
No native attachment is added; available manual visits are the fallback.

## Implementation gate results

2026-10-07; PYTHONHASHSEED=0. Exports and all build/report artifacts were kept
outside the repository and removed after verification.

- `python expansion.py`, with RRT_STORY_OUTPUT pointing at the temporary export
  and the four available build-expansion parent-binding files: success,
  3836 scenes.
- Combined `test_household*.py`, `test_harem*.py`, savecompat baseline and UTF-8:
  108 tests passed. After the final two political wording substitutions, the
  row/UTF-8 subset passed another six tests and the final export's frozen
  save-reference check returned zero failures.
- `payoff_lint.py --strict` and `departure_lint.py --strict`: zero hard failures.
- `rrt_verify.py --strict --gate-only`: zero hard failures on the final export.
  The default run was stopped during report-only whole-game analyses; gate-only
  retains every strict check. Its initial therapy-budget failure was fixed by
  class across both identity presentations: political "permission" became
  "offer"/"leave", preserving the bargain and all state.
- Compiled C# S39, HouseholdTests, HouseholdEngineTests and
  HouseholdTransactionTests: 573 assertions passed, including the production
  branch walker's selectable-answer checks. The historical S39 Seating Notes
  entry is excluded from the existing five-seeded-frictions assertion; those
  original eligibility tests remain unchanged.
- The requested unfiltered Python/C# invocations ended with signal 143 without
  diagnostics. The dotnet run launcher also lacked its expected apphost; the
  completed Release DLL was invoked directly for the passing selected suites.
  No full-suite pass is claimed. No game, harness or build-expansion script ran.

## Coordinator integration still required

Consume POLICY through the shared first-wins enmity, capped respect and one-edge
reconciliation producers. They remain reserved hooks on this base; the pair
module deliberately supplies only the sheet's exact deed/cost witnesses.

Update tools/harem-schedule.json, outside this job's edit scope: S39 is still a
reserved one-primary/one-retry row with empty reads. Charge the additional
preparation and use the emitted witnesses in the combined actual schedule.
The three mutually exclusive presentation pairs are two actual ideal visits or
three with recovery, never six completions and never rest-delivered letters.

Independent prose scores and whole-roster schedule certification are pending
the coordinator/auditor. No additional design is proposed. No commit was made,
following the task's final instruction.

Wave 1 integration: the entry point is `storylines/harem_rows/s39.py`
(`register(payload, scenes, refs)`), discovered through the single story hook.
Row checks are in `tests/test_harem_row_s39.py`; shared C# registries are
unchanged. Scene, answer, deed and cost contracts are retained.
