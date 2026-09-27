# Shared 585-scene verification

The development export now includes the 47-scene Minagho and Chivarro continuation and the scoped SoanaForest and ChivarroWarm portrait assignments.
It contains 585 scenes in 16 route groups representing 16 of the 37 planned characters.
These are integration counts, not completed-route counts.

| Artifact | SHA256 |
| --- | --- |
| development/Story.json | `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A` |
| src/bin/Release/net48/RanRomance.Tirabade.dll | `AEB714C5AF2C88FD156588CC072DFE8A40C60AD2B75B4B43D8A5ACC4E7027176` |
| Installed addon Story.json, unchanged | `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4` |

The shared managed runner conditionally loads the portable parent-ending fixtures when the story contains parent edits or loss rules.
It prepares the reviewed source condition trees before Main.Build, records original sequence references after fixture preparation, checks preflight rejection, and exercises the integration after successful construction.
Stories without the metadata retain the existing setup.
The [independent fixture review](parent-ending-fixture-independent-review.md) checks portability, pinned evidence, native defaults, aliases and source expression agreement.
The generated fixture file was not manually edited.
The separate [runner adoption review](parent-ending-runner-adoption-review.md) passed and independently reran both this 585-scene export and the prior no-metadata 538-scene export against the same DLL.
The latter passed 67,302 assertions, confirming that the added fixture setup is conditional.

The shared managed project built with zero warnings and zero errors.
ManagedBuildTests passed 71,672 assertions against the exact story and DLL above, constructing 20,701 generated blueprints through the real Main.Build.
The full RulesTests command passed 25,958,597 assertions against the same export.
The binding verifier passed 1,105 binding uses against 139 archive targets and 106 reviewed parent-source targets.
The shared game-bindings-report.json now identifies the shared development export rather than a temporary candidate.

Native resurrection reached the documented standalone CLR ECall boundary.
Native meeting Tick requires Unity's LoadingProcess instance, so actual withdrawal scheduling was not executed headlessly.
The source fixtures use actual condition objects but do not initialize the parent mod or evaluate populated native conditions.
Unity presentation, actor arrival, portraits in the game, save/load and ToyBox execution remain unverified.
The optional RanEpilogue topology remains outside supported loss-delivery verification; the integration preserves original parent endings when that patch set is active.

The current [assembled trio review](../story-review/tirabade-assembled-review-20260926-current.md) passes the doubled length floor but requires literary revision.
The review found a reproduced Chapter 1 injury contradiction, similar early motivations, repeated explanations and insufficient native-history responses.
An author is revising the opening and early motivations separately from the reviewer.
Those ongoing source revisions are not included in the frozen export checked here.
No new package was staged and no installed files were changed during this checkpoint.
The previous development package still contains 533 scenes.
No complete character release or roster-wide completion is claimed.
