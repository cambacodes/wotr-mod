# Parent-mod binding verification

Targona already has a substantial RanRomance route, including an Anograt branch.
The extension must read actual completed quest and witnessed finale history rather than duplicating its first courtship or inferring completion from a started dialogue.
The planned contribution uses existing Etudes, CompletedQuests and SeenCues fields; no production gameplay-state adapter was added.

`tools/parent_bindings.py` loads explicit reviewed creation evidence pinned to the installed parent assembly's SHA256.
It rejects changed assembly bytes, malformed identities, duplicate records, unsupported types and excerpts missing the requested identity or matching creation type.
This is evidence validation, not execution of the parent initializer or automated proof that every decompiled excerpt was interpreted correctly.
The source manifest still requires independent review.

`tools/verify-game-bindings.py` accepts `--parent-bindings` and reports archive targets separately from reviewed parent-source targets.
`managed-tests/read-native.py` accepts an explicit `RRT_PARENT_BINDINGS` path and supplies marked typed fixtures only for otherwise missing parent targets.
It invents no quest actions, native conditions or parent gameplay behavior.
Without an explicit manifest, missing parent assets remain missing.

The Targona manifest contains 17 source records pinned to installed RanRomance.dll SHA256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
The isolated binding fixture is `development/parent-bindings-review.json`, SHA256 `B1C32DDAE28CC42445340E3E06DAC6ADC63DAC1AE4D0311FCBDEB064D880F977`.
It retains main246 and adds synthetic test-only aliases for the 17 records, without adding a Targona route.
Verification passed 430 binding uses across 74 archive targets and 17 parent-source targets.
Managed construction passed 30,457 assertions over 9,043 blueprints, with production DLL `F81C0C7BD279C832F73B01CD5F5E44B6C37570F675B8873540C7C7D2B30188F4`.
The test output identifies each parent fixture and explicitly excludes parent-mod initialization from its scope.
Focused Python checks also passed valid evidence, changed assembly, wrong type, duplicate record and wrong identity cases.

The ordinary main246 archive verification remains unchanged at 413 uses and 74 archive targets with no parent-source fixtures.
No production source, main story or installed file changed during this verifier work.
Actual parent initialization, version compatibility and saved-game histories remain runtime verification requirements.
