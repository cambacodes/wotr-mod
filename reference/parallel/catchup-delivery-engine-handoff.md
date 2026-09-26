# Catch-up and manual delivery engine checkpoint

Kiana and Seelah need explicit old-save catch-up without deleting historical farewell flags.
Scene.ForbidOverrides maps an authored forbidden flag to an authored permission flag.
Only that individual scene prohibition is waived when its mapped flag is present.
Completed scenes remain completed; prerequisite, chapter, area, delay, relationship closure and native unavailability checks remain in force.
Validation rejects missing prohibitions, unknown authored flags, self-overrides, relationship-closure overrides and native or derived prohibition aliases.
The default empty mapping preserves existing payload behavior.

Kiana's existing breakup scene revealed a separate queue problem: a manually useful repeatable conversation can starve the automatically delivered continuation.
Scene.ManualOnly preserves GUI Read availability but excludes the scene from automatic rest selection.
Rules.NextRemote is now the actual queue selector called by Main.Update, so focused tests can exercise that same selection rather than reproduce its implementation.
Non-remote ManualOnly metadata is rejected.
The GUI labels these offers as choose Read below rather than promising delivery at the next rest.

The current 198-scene export is unchanged at `D042C85C5F5AE98C1BF591BC3380B335203F5601DEE074C6842E2CB5E390F595`.
The new default-compatible engine passed 8,094,366 rules assertions, including targeted override and queue cases.
Managed construction passed 22,154 assertions over 6,741 blueprints before the subsequent GUI-label-only correction.
The production project builds without warnings or errors.
Independent source review is recorded separately in `reference/canon-review/catchup-delivery-engine-review.md` when released.

Kiana's actual automatic farewell failure was reproduced by `--kiana-progression` against this unchanged export.
That deliberately failing test is separate from baseline checks until the corrected route is staged.
The author is implementing scene-level progression and old-save choices; Seelah has a separate author and exclusive files.
The parent has added farewell override metadata to Seelah's four aftermath scenes, six late-campaign scenes and the return bridge.
Those source changes are pending stage integration and must not be represented as already present in the main export.
Actual game interruption, the UI, save round trips and ToyBox execution remain unverified.
