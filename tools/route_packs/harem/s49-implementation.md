# S49 implementation: Wenduag / Vellexia

Authored addition: the returned Midnight Isles consignment, cult courier and
private Drezen storehouse are new incidents, not recalled native history. The
Table launches and returns the Chapter 5 watch handover; no new map, unit,
army assignment, return device or native-event rewrite is introduced.

## Implemented contract

`storylines/harem_rows/s49.py` exposes `register(payload, scenes, refs)`.
It appends notice, handover and one recovery, using the exact sheet prefix
`household.pair.wenduag_vellexia.`. Root choices retain the sheet order.
Success requires each woman's deed, not the page alone: Wenduag yields her
live quarry; Vellexia gives up torment long enough to keep the handover moving.
The Commander keeps the cargo risk and cold relief watch. Failure loses cargo;
refusal remains retryable once. A second refusal records unresolved friction
without closing or renegotiating either romance or Wenduag's Lann arrangement.

Both existing eligibility/open-route contracts, current departure-epoch
attendance, live Trickster, paid page and Table stance apply on every step.
Wenduag requires companion presence or her existing scoped returned-body
availability. Vellexia additionally requires `in_person` and forbids `visited`
and `kept_as_mirror`: her current physical market presence is withdrawn by
`visited`; an echo shell or an old return receipt is insufficient.
Both directed enmities retain the Table's existing reconciliation overrides.
No scene produces enmity, reconciliation, attraction or new partner terms.

Notice has no delay. Handover ages `notice.accepted` for 48 hours. Recovery
ages either `handover.failed` or `handover.refused` for 48 hours and forbids
settlement and its own completion. Each completion charges one protected
allowance; no optional arc, cap expansion or extra letter is registered.
Perception DC 22 resolves the courier's seal, never affection. The paid
handover costs Materials 150; recovery costs Materials 200. Only the successful
full-debit terminal publishes both deeds and its completion witness.

The stage producers are the sheet's two deed-dependent respect groups.
There are no friend or lover producers, runtime explicit slots or unreachable intimate
stubs. The sheet explicitly authorizes this complete baseline when the optional
ceiling extension is not enabled. Reviewed optional ceiling/ladder metadata and
the full later body-window contract remain integration prerequisites for Nera's
four-step extension; they are not manufactured by this row.

## Canon verification and corrections

Verified directly in `/wrath/blueprints.zip` and the installed `enGB.json`:

| Asset | Meaning used |
| --- | --- |
| `d70c17267a6713d42a71144cc4ea8f2e`, `Velexia_Third_Date/Cue_0139.jbp`, shared key `29ff3b7e-8af7-44ed-acf6-4cb9adb4cb5d` | Wenduag's adversarial combat innuendo; not mutual desire. Existing `wenduag.vellexia_conflict` alone selects recall. |
| `7a54110bd06a25742a0813a405079cec`, `Velexia_Main/Cue_0063.jbp`, key `c262ac56-74f1-4886-828e-a49f077f37f7` | Wenduag addresses Daeran. Never evidence of this pair's romance. |
| `c06e6223610c82c4c8cd43a60f2abc53`, `Velexia_Main/Cue_0013.jbp`, key `5b61c41a-4069-49ec-bf0e-02dc2fe22cca` | Vellexia's boredom and reinvention, not remorse. |
| `8a142cc07fa2d3446a676e54c58f923a`, `Velexia_Third_Date/Cue_0054.jbp`, key `66a0ffbe-87e4-4025-9fcd-f04f0160b54b` | Vellexia orders a killing for entertainment. Her practical concession does not redeem her. |

Additional sheet correction: `82ab52a731c9db24db049bb2cc6f382c`,
`Velexia_Third_Date/Cue_0137.jbp`, is Finnean's cue (blueprint Comment and
speaker), not Vellexia defending her combat prowess. It is not used as her
voice evidence. No duplicate native cue binding is added.

## Integration boundaries

The merged baseline now calls `register_all` from `expansion.py`; S49 is
auto-discovered. No shared registration edit or manual export attachment is
needed in W3-S49.

W3-S49 remains blocked by two independently required contracts:

- `tools/harem-schedule.json`, row `49`, still declares `rom=false` and
  `ceiling=respect/respect`. The sheet's section 7 requires an integrator-owned
  reviewed optional extension before friend/lover producers are enabled.
  The classification lint also still rejects romance eligibility for these
  promoted rows. This job does not change shared classification policy.
- `vellexia.presence` in `storylines/vellexia_trickster.py` requires historical
  `in_person` and forbids `visited`. There is no separately earned, current
  bodily stay covering the required 152 hours from settlement through morning.
  The lore-check's S49 correction explicitly requires such a window at every
  optional continuation. A shell, return history or settlement is insufficient.
  Establishing it would require another route's attendance contract, outside
  this job's permitted entries. No synthetic lease, free arrival or new gate
  is introduced here.

The exact planning brief is retained under
`explicit_slots/blocked/wenduag_vellexia/household.pair.wenduag_vellexia.desire.explicit.1.json`.
It is non-graphic editorial material for two women, Commander absent; it is
not an exported node or an eligible runtime interval. After the shared blockers
are resolved, the row implementation still needs bond, observance, desire and
morning as specified by the sheet, including their full terminal write tables,
48/48/48/8-hour clocks and four charged optional steps. No unreachable desire
stub is shipped. This report does not claim that the optional unit is complete.

Shared Seating Notes and the women's Last Call readers are separate W5 work.
Successful and unresolved friction witnesses use the shared Seating Notes naming
contract, but this checkout has no S49 friction entry in its shared census and
therefore no S49 Seating Notes reader. That missing shared reader is escalated;
it is not claimed as emitted. Row-local respect witnesses are supplied for its
stage readers. No edits to shared household/Last Call hosts are attempted here.

Acceptance: Python row tests exercise current bodies, closure/later loss,
page/live-path withdrawal, both directed enmities/reconciliation, exact clock
boundaries, unknown versus observed history, insufficient funds, atomic payment,
completion replay, Abort, one recovery, append-only registration and isolation
from shared authoring globals. No independent audit score is claimed.

## W3-S49 class sweep and validation

All three emitted steps were checked for current bodies, paid page/live path,
closure and later loss, both enmity edges, actual timestamped predecessors,
refusal and Abort. Both directed stage producers remain respect-only. No new
runtime surface was added: payoff/departure inventories need no new entry.
Native history remains recall only, and no echo or native rewrite is introduced.
Compared the planned recognition/encore/false-name aftermath with S25 and the
women's solo devices; the brief retains the sheet's distinct recognition device.

With PYTHONHASHSEED=0 and bytecode writes disabled:

- expansion.py succeeded: 3,992 scenes, including all three S49 scenes, exported
  via RRT_STORY_OUTPUT to system temp; shared auto-discovery confirmed.
- S49 + UTF-8 unittests passed 11 tests. Direct exported-story savecompat,
  payoff and departure checks each returned zero hard failures. A broader
  savecompat unittest invocation was stopped because it repeatedly regenerates
  the entire export; its direct exported-story check had already passed.
- tools/rrt_verify.py --strict --story <temporary export> --game /wrath
  completed its full pass once: zero hard failures, zero validation errors,
  zero shipped structural errors and zero draft contract diagnostics.
- Requested full unittest discovery was terminated with exit 143 by the
  workspace guard that blocks full suites in RRT-hw worktrees.
- dotnet run compiled with --artifacts-path in system temp, then failed to
  launch from its default tests/bin location. Direct execution of the compiled
  RulesTests.dll was terminated with exit 143 by the same workspace guard.
  Progression and selectable-answer coverage are unverified, not passes.

Temporary exports, verifier reports and C# output were removed from system
temp. Existing LF endings were preserved; the reserved JSON is byte-identical
to the planning source. git diff --check passed. No scene/node/relationship ID,
choice index or runtime text changed.

No independent audit score is claimed. No commit is made, per the task's final
instruction. W3-S49 is incomplete pending the reviewed metadata and real body
window; the baseline is preserved rather than quietly enabling its extension.
