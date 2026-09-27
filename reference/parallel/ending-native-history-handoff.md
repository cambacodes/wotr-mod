# Native ending history correction

The preceding goal turn integrated and checked Nocticula in commit `6b50336`, so it counts as progress.
Independent final integration review exposed the difference between simulated story completion and native page history.
Root reproduced a native replay gap before changing production code.

## Reproduction

The existing addon DLL `A2920CD3EC1043ADFF018B390851599A0C68064FE4186B92F7ECCDA83CA73BB9` built the actual 612-scene story pages.
The new probe invoked native `DialogController.PlayCue`, which added the generated page to both local and player dialogue history.
The generated plain Continue answer ran its empty native action list.
After clearing local history, the original generated `ending_together` page still returned true from native `CanShow`.
The probe failed with `A played ending can repeat through another sequence: ending_together`.
The reproduction log is `C:/Users/Z/AppData/Local/Temp/ending-native-history-repro.err`.

The probe replaces route conditions with an empty checker to isolate delivery from campaign eligibility, then restores the original checker.
Temporary Harmony hooks bypass Unity page rendering and debug logging.
Native page history writes, `CanShow`, and sequence selection execute from the installed game assembly.
Earlier fixture setup errors involved missing debug-log state and an ambiguous debug method overload; those were corrected before the replay failure reproduced.

## Correction and evidence

`Main.BuildScene` now sets the native global `ShowOnce` policy on ending pages.
Ordinary conversation pages retain their prior policy.
Generated IDs, native parent pages, dialogue flags and Continue actions remain unchanged.
The test uses two native `CueSequence` instances referencing the same generated page, checks first selection, plays it, and checks that the second sequence skips it.
It also verifies that a fresh player's dialogue history allows first display.
Every generated page is checked for the expected global history policy, including later pages of branched endings.
A separate traversal of the exported ending graphs found 195 ending scenes, fifteen with multiple pages, and no cycles requiring a page to be shown again.

The full managed runner passed 79,911 assertions against story `A23F0AE6ABE6FAB6F0C275FBF8E1E8044EBEEA1FD040C12D61C4BD0F7D5829CC`.
Both addon and test builds completed with zero warnings and errors.
The tested addon DLL is `B62BFFD43650B40544F8359914D63C6D79922A020312E14FA87F6DE42804ADDC`.
Its source glob includes the then-current unregistered Nurah observer foundation, which was separately under review and does not run through Main.
The success log is `C:/Users/Z/AppData/Local/Temp/ending-native-history-fixed.out`.
The test runner's final scope sentence was subsequently clarified to distinguish native seen-state evaluation from unexecuted full campaign conditions.

## Remaining gates

The independent review at `reference/parallel/ending-native-history-independent-review.md` grants a scoped pass to the correction and tests.
Its isolated old-code run reproduces the failure; the corrected probe passes 1,276 assertions over all 195 entry pages and 53 later pages.
The reviewer verified all 972 generated ending blueprint names and GUIDs are unchanged.
This does not add the conditional Expanded Epilogue sequence attachment or prove the optional plugin's initialized graph.
It does not exercise a full game save round trip, Unity rendering, or actual parent initialization.
The new test covers repeat delivery of the same page; it does not establish mutual exclusion between different outcome pages if world state changes during the epilogue.
The original parent mechanisms for its own pages remain intact.
No installed mod files or distributable package were changed.
