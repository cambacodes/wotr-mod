# Authored epilogue transition repair

The managed builder previously replaced every epilogue node's choices with an unconditional Continue answer.
Story-graph traversal therefore did not establish that those branches existed in the generated game dialogue.
The updated construction test failed against the original builder with `Wrong choice count: seelah.ending_together.history`.
The tested story was main 225, SHA256 `A867F751E353B285EA0C108EE3172C0094696F9A4EBBA2D519460D41F05A2626`.

Main.BuildScene now builds authored epilogue choices with their visibility conditions, selection conditions, effects and next-page references.
Epilogue choices do not mark the whole scene complete, preserving the established non-mutating exit behavior unless an authored choice explicitly carries effects.
Unconditional default terminal Continue answers retain their existing `.continue` identifiers.
All other page IDs and the parent-mod and Aeon sequence insertion logic remain unchanged.
The reviewer requested an explicit null-check for skill checks in the plain-terminal discriminator, which was added even though validation already rejects epilogue skill checks.

The first repaired main225 build passed 26,239 managed assertions over 7,870 blueprints.
After the defensive discriminator addition, the Konomi227 stage passed 26,703 managed assertions over 7,981 blueprints.
That stage contains all unchanged main225 scenes plus the Konomi political contribution, and exercises the same repaired endings.
Final production DLL SHA256 is `F81C0C7BD279C832F73B01CD5F5E44B6C37570F675B8873540C7C7D2B30188F4`.

Managed checks now inspect actual authored ending answer counts, visibility and selection guards, effects, next-page references and stable plain-terminal identities.
These checks also preserve the native answer lists and both epilogue sequence fixtures and verify idempotent construction.
They do not execute the actual Unity cue scheduler, loading a real mid-epilogue save or the parent mod's initialization.
The independent source review is `reference/canon-review/epilogue-transitions-review.md` when released.
No installed assembly or story was changed.
