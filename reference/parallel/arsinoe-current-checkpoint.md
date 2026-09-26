# Arsinoe current integration checkpoint

The opening was restaged against main 225 and independently reviewed for concrete integration gaps.
The old opening passed complete-path tests but failed the new interruption replay tests.
The first reproduction reported `Interrupted Arsinoe roof replay accumulates conflicting relationship choices`.
The relationship pace flags now commit with the final rooftop answer rather than before the last page.
The second reproduction reported `Interrupted printer replay records contradictory commissions`.
The printer choices now forbid the opposing prior commission, preserving the recorded agreement when an interrupted scene is replayed.
All scene IDs, node IDs, choice indices and prose remain unchanged.
No pre-fix Arsinoe scene was installed or included in the main export.

The corrected 230-scene stage is `development/arsinoe-current-review.json`, SHA256 `1365DAECEC2CC99F283DC8A7F429B2F4EC2768EFBED09246E6F108EF87D31649`.
It passes 9,139,490 rules assertions, including partial-choice contact-loss and replay cases.
All 370 binding uses resolve to 66 typed native targets.
Managed construction passes 27,012 assertions over 8,180 blueprints and six native answer lists.
Production DLL for these checks is `757B8648C23CBD3C9185A148A3806EED8B2FD86D84856DF5A7959F997BD91304`.
The latest independent gap report is `reference/canon-review/arsinoe-current-integration-gaps.md`.
The main export remains 225 until contribution review and integration are completed.

## Shared work in progress

The DLL also includes a new StartedDialogs adapter for Konomi's native political history.
It reads actual DialogState.ShownDialogs and deliberately does not claim dialogue completion.
The isolated adapter stage `development/started-dialog-review.json`, SHA256 `78EC5812437B7B6B39A31B547DBA3A2C1122174576309E5D09207C2E0452127F`, binds the actual rank-eight dialog as a test fixture.
Managed construction and collection-read checks passed 27,018 assertions.
Tests prove an unrelated dialog does not match, a shown dialog matches without cue or answer history, reads preserve collections, and a fresh snapshot does not retain a removed entry.
That stage predates the printer replay fix and is adapter evidence only.
Adapter validation coverage and independent review remain pending.

A separate confirmed engine defect remains in Main.BuildScene: epilogues receive an unconditional Continue instead of their authored node choices.
This can suppress multi-node ending branches despite passing graph walks.
Root must reproduce it against constructed blueprints, fix transition and choice guards, and add managed coverage before treating assembled endings as verified.
Existing assertion totals are not evidence that those authored ending branches run in game.
No installed files changed.
