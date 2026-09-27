# Nocticula withdrawal phase rereview

The completed-work wording and interface scope are repaired.
The revised response fits `noct.second_door`, but its reuse at `noct.what_she_keeps` introduces an erased-wall continuity error.
The scoped repair therefore still falls below the strict above-90 gate in one dimension.

## Evidence

- Story source SHA-256: `95853FE74419EF06912B9F1236F702E0231862398F51A3C7F0147BCBB3B5CF0E`.
- `src/Main.cs` SHA-256: `6313F97C7856932AB9055E773065FA5926E27DBEB7A6EA05CDE5E170E46245E4`.
- Export SHA-256: `1FA0ABE9C739ACBBD6B2EA7F38E236E46F4C3B30344AE24A061DCB92FBDB98CB`.

I read the repair report, both exact opening pages, their withdrawal choices and replies, the shared authoring helper, closure effects, and the interface condition.
All three hashes match the assigned revision.

## Corrected behavior

The late choice explicitly declines continued private meetings after the harbor business is settled.
Nocticula acknowledges that the work stands and refuses further invitations without pretending that the Commander owes unfinished labor.
Her pointed insistence that she understands the difference, and her displeasure at hearing the answer, preserve her pride.
The earlier bargain remains under its existing terms.
The response promises neither successful native romance outcomes nor altered parent scenes.

At `noct.second_door/start -> withdraw_undertaking`, the completed room, retained stone and existing exit suit this departure.
Her refusal to erase what she has made is a convincing reaction to rejection.
It remains distinct from accepting the final evening while choosing `limited` later in that scene.
Withdrawal closes the addon before its final completion credit, while preserving earlier authored history.

`src/Main.cs:840` now displays "The harbor undertaking has ended." for the Nocticula entry.
That describes the flag's scope accurately and no longer claims the parent relationship has ended.
The other relationship entries retain their previous label.
This is a source-level UI finding, not an observation of the rendered game.

## Remaining failure

At `noct.what_she_keeps/start`, the newly attempted wall and its badly placed doorway are erased explicitly before the player receives the withdrawal choice.
The response then places her hand against "the new stone" without recreating it.
Its opening reference to the room she has been making and its final claim that the way out is already there also assume more established construction than this opening supplies.
The missing wall is the definite contradiction; the exit wording compounds the uncertainty.
Being inside a dream does not supply an omitted action when the scene has just described that action's opposite.

Use the still-present bollard for her gesture at `what_she_keeps`, or explicitly restore the wall before she touches it.
Give that unfinished quay scene a departure that does not rely on the erased doorway.
The completed-room staging can stay at `second_door`.
The new refusal dialogue itself can remain shared.

## Scores and checks

| Scoped dimension | Score | Result |
|---|---:|---|
| Late refusal voice and non-agreeability | 94 | Pass |
| Completed-work and parent-bargain semantics | 95 | Pass |
| Final-scene staging | 94 | Pass |
| Cross-scene physical continuity | 84 | Fail |
| Undertaking-only UI wording | 96 | Source pass |
| Addon closure effects and predicates | 96 | Static pass |

I independently compared all twenty-four Nocticula source scenes to the current export.
I checked all sixteen refusal or withdrawal terminals, their exact addon-only effects, visit closure blockers, and ending completion prerequisites in Python.
Those checks passed.
Flags still take effect on the sole terminal confirmation after the response, not on the first selection entering it.

The root reports a clean assembly build and 28,662,926 passing rules assertions for this export.
I did not repeat that full run for this prose-and-label change; the previous scoped review independently ran it for the preceding export.
The source checks above are the new independent execution evidence.
No Unity execution, rendered UI inspection, real save persistence or ToyBox verification occurred here.
The broader route's length, acquisition, recovery and art-assignment gaps remain open.
