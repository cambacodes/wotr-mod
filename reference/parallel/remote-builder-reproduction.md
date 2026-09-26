# Remote continuation builder reproduction

Root extended the managed builder assertions before editing production `Main.cs`.
The expected contract is that physical conversations and non-epilogue remote conversations carry a continuation guard on answer visibility, selection, mutation and native checks, plus an interruption exit.
Epilogues retain their existing terminal handling.

The updated managed test built with zero warnings and errors against the unchanged development DLL `EEBA86B2454713BFFF1DEECE2D7B96040B9ABC59C4251F4139B4B78B117BE428`.
Running actual `Main.Build` on the integrated 459-scene story `20C417875617D4217F73855BCF37121C400C81209A68316FF1F0CC5E969719B0` failed at `Wrong choice count: abyss_letter.start`.
The old builder omitted the interruption exit and passed a null continuation for that remote scene.
The native answer-list and blueprint fixtures are the same managed fixtures used by the regular construction suite.
This reproduces the generated-object defect, not the live Unity interaction.

Root then changed `Main.BuildScene` to select the continuation once per node when the scene has physical contact or is remote, excluding epilogues.
The existing answer, action and check construction uses that selected continuation.
The interruption exit is appended whenever it exists, retaining all original numbered answer identities.
The rules author independently inspected this wiring and found no missing path in the diff.

A separate actual-Rules reproduction by the rules author played all eight local Vellexia predecessors, observed native dismissal, opened the Nexus echo and then introduced the native death state.
Before the rules patch, the opened conversation still passed `ContactAvailable`.
That reproduction and the rules-side patch are recorded separately in `remote-continuation-repair.md` once frozen.
Both the builder wiring and rules change are needed; neither alone fixes the actual constructed conversation.

The source patch and full post-fix builds were still pending joint validation when this record was written.
No live save, installed mod or Unity scene was changed.
