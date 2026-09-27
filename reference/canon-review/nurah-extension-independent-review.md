# Nurah extension evidence: independent review

Reviewed on 2026-09-26.
Verdict: pass for the researched binding and native-state evidence described below.
This is not approval of a new manuscript, romance acquisition route, resurrection, actor placement, or release.
No production source, binding manifest, or shared export was changed for this review.

## Frozen inputs and independent checks

- Audit: `nurah-extension-audit.md`, SHA256 `566F98A42EF56CD6F13F317B5366D27C7932F4D565FA78057B922B157AF88051`.
- Research manifest: `nurah-parent-bindings.json`, SHA256 `D4E4BA4752C850745D629EED6960CB0C8B3529360C476DD953948DBF2F39E1DC`.
- Installed parent DLL: `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
- Installed localization: `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
- Installed readme: `8CB10A67132130C179359BC2941E91EA058FFA47F1D394180F0D00AC373581CD`.
- Retained IL: `074AC42A4125B96715B96BEF6EE3F64A77894B9422D0E4FC29A5BD237B74683B`.

All three installed pins and all 42 retained source-file hashes match.
For each of the 36 distinct creation records, I independently resolved the two `Configurator.New` arguments, including declared constants and local variables, and checked the claimed name, GUID, creator type, exact source excerpt, optional GUID declaration, and source-file hash.
Each GUID also appears in the named `Configure` method in the retained IL.
This verifies the actual creation evidence rather than merely finding a GUID somewhere in the assembly.

I independently extracted all 18 native records from the installed blueprint archive.
Their raw hashes, asset identifiers, and native types match; embedded `Data` objects match the actual archive records where the manifest supplies them.
Probe results and extracted records are retained under `C:/Users/Z/AppData/Local/Temp/nurah-independent-review/`.
The manifest remains a research artifact, not an assertion that all future runtime references have already been registered through the production binding loader.

## Romance and completion distinctions

The audit correctly distinguishes the currently playing romance etude `9f655e252d334f04884f10188b0d8928` from its completion.
Its play action increments the parent romance count by one; completion decrements it by one.
Several non-romantic or hostile transitions complete it, so completion cannot be reused as a positive romance witness.

Book 4 acceptance answer `968b8f00f553498c8a2ba53c992e20cb` starts the romance.
The corresponding accepted terminal cue is `17e224c5f33141f59456f3e4effdcf8e`, conditioned on that answer having been selected.
Its enclosing acquisition conditions must remain intact: the Evil/Gold Dragon combination, the compound Lich/quest condition, Devil class, and the dialog's flirt and Swarm conditions are not interchangeable generic alignment checks.

Book 5 romantic answer `319cc9e35abd471384c9c4698f9d22e1` excludes the Lich arrangement and leads to the page containing terminal cue `f8a7511233524742bc42b25190609f4c`.
The terminal cue checks that answer selection.
For precision, the containing page also requires either answer `bd78354881d149889fbb0343d0ea89cd` together with Chaos playing, or cue `bb174b47251d4b67af8f4e85115970a1` having been seen.
Observing the actual terminal avoids treating a synthetic selected-answer flag as proof that the player traversed all enclosing conditions.

Book 5 cue `ea8bc70ed743483eb29e6af6c4960766` starts the Lich arrangement and completes the romance.
The Chaos ending cue `b7c37130c10d491abbef16dfa1dfe813` can also complete the romance.
The external Anevia chapter-five Devil reaction fails Nurah's quest and completes both the romance and Lich etudes.
Book 5's unconditional quest-objective completion is consequently not a romantic success witness either.
The audit's proposed combination of current romance, an observed romantic terminal, living state, and actual availability is supported by these sources.
It is still a design requirement, not an implemented continuation gate.

## Actor absence is a real delivery constraint

The capital default placement etude `245524f91e743b64eaa16445c3ea8e73` hides the retained capital Nurah spawner even in a living baseline.
The prison placement `21a061de3610732438072d2b975b6f43` has distinct chapter, killed, and ran-off conditions and only unhides/translocates that actor in its qualifying chapter-three branch.
Neither a living blueprint nor a remembered romance proves that an accessible chapter-five Nurah actor exists.

The capital death mechanism `20927a9471c00814b808fd69e88879c7` is parented to the killed etude and can kill the exact capital spawner when its play action runs.
Any future resurrection proposal must account for that mechanism instead of merely clearing an addon death flag.
This source observation does not assert that the action is currently running in every save.
Running away completes the prison etude; it does not itself establish alliance, romance, or a safe return placement.

Pulura uses a different spawner in a different scene.
Its mechanics exclude the documented killed/prison/death-mechanism histories before spawning Nurah, and its battle affiliation separately depends on alliance or redemption.
Treating this as the same retained capital entity would be incorrect.
The audit preserves that distinction and does not claim a companion recruitment or physical meeting implementation.

## Pulura action-list defect

The reported defect is reproducible in the installed sources.
Native etude `75a4fb7cf239bb14f8d7bfd29073ffaf` has a Mutasafen death trigger whose original action list contains two different actions.
Action zero unlocks flag `04841f0b76b25d84c9ee6536bd8ecd27`.
Action one checks whether captives-dead etude `e02683b27fe26ce4bb6ac6f6f9e038bf` is playing, then completes objective `0a4665a793bd31541a9676f3ae9a07e2` or gives objective `cf7a0cc593eedd442aa7d2125b23b161`.

The installed parent replacement appends original action zero twice, then starts its dialog.
It does not append original action one.
I freshly decompiled the relevant Book 4 builder from the installed DLL, independently of the retained source, and obtained the same duplicate-index expression.
The native JSON confirms that index one is meaningful quest progression, not a duplicate or empty action.

This supports a concrete static defect report: the replacement drops the original conditional objective action.
It does not establish the final quest state in a running save, because other actions, later patches, and load order can affect that state.
A fix should first reproduce both captive-state paths against the final initialized action list, preserve each original action once, and separately check dialog timing and repeated execution.
No fix or native action mutation was performed in this review.

## Limits and next gates

No blocking evidence discrepancy was found within the assigned 36 parent records and 18 native records.
I did not independently approve the audit's entire literary interpretation or re-read every parent localization entry as a manuscript review.
The counts and source checks cannot approve adult characterization, art, new mutual attraction, or a minimum-length extension that has not yet been written.
Future runtime tests must still distinguish current romance from stale terminal history, conversion, death, prison, ran-off history, foreign actors sharing the blueprint, and current native claims.
ToyBox concurrency, actual Unity placement, and save/load behavior remain unverified by this read-only evidence review.
