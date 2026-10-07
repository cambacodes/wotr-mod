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
There are no friend or lover producers, explicit slots or unreachable intimate
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

The exact auto-discovery initializer is supplied. This checkout has no discovery
caller: `story.make_story()` returns a dict directly and has no `payload` local.
The coordinator must supply its shared registration hook; the row does not edit
the prohibited `story.py` or `expansion.py`. Review validation explicitly attaches
the module to the exported payload in system temp, and does not claim that
unmodified `expansion.py` discovers S49.

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

## Gate record

With `PYTHONHASHSEED=0`, `python -B expansion.py` succeeded with
`RRT_STORY_OUTPUT` pointing to system temp (3,830 baseline scenes). Explicitly
registering S49 on that export produced the 3,833-scene review payload.
`rrt_verify.py --strict --gate-only` passed that corrected payload with zero
hard failures. Save compatibility, payoff and departure checks also returned
zero hard failures. The targeted savecompat/UTF-8/household/harem modules passed
84 tests; a final focused S49 plus UTF-8 run passed eight tests.

The requested unittest discovery was terminated by `/work/testguard.sh`, which
blocks full suites in `RRT-hi-*` worktrees. The C# project compiled with output
and intermediates in system temp; `dotnet run` then looked for its executable
in the default repo output path. Direct execution of the compiled DLL caught
the missing pair hook declarations, which were fixed. The corrected C# run was
terminated by the same workspace guard before it reported a result. Therefore
C# progression/page coverage is pending coordinator validation, not a pass.

All temporary exports, reports and compiled output were deleted. No commit was
made, following the task's final instruction.
