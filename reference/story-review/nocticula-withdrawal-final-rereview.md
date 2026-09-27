# Nocticula withdrawal final scoped rereview

The inspected withdrawal repair passes its scoped review.
The revised staging works at both late scenes, preserves Nocticula's displeasure, and no longer invents a wall after she has erased it.
This does not approve the full route or certify in-game behavior.

## Pinned evidence

- `storylines/nocticula_continuation.py`: `8976F636EBEEFBAE17DB048C8D45EF5864C467E340F12C1D499BD94713535685`.
- `development/Story.json`: `38F3442E5B33C1C6E9DE548E46C77B6C033783FB68E96FA3D0631EA3D0D44255`.
- `src/Main.cs`: `6313F97C7856932AB9055E773065FA5926E27DBEB7A6EA05CDE5E170E46245E4`.

I read both actual `start` nodes, their selected withdrawal answers, the resulting complete response and terminal effects, and the current UI closure label.
The hashes match the assigned revision.

## Findings

At `noct.what_she_keeps/start`, Nocticula erases her attempted wall before discussing Ossin's withdrawn offer.
The revised `withdraw_undertaking` response uses her averted gaze, an uncomfortable silence and an explicit fading of the dream.
None requires the erased wall, a completed room or an existing doorway.
The completed business remains completed, even though the Commander leaves before hearing the remaining report and discussing future ambitions.

At `noct.second_door/start`, the finished room and celebratory drink precede the same refusal.
The response now recognizes that the refusal concerns continued private meetings after the work, rather than an obligation to find a replacement adviser.
Nocticula's loss of her teasing tone, deliberate silence and pointed demand for courtesy suit this rejection.
Her willingness to hear an answer does not become enjoyment of it.
Ending her own dream with two raised fingers preserves her control of the encounter without undoing the player's decision.

The dialogue leaves the earlier bargain under its existing terms.
It does not promise future parent-romance invitations, change native outcomes or imply a parent breakup.
The interface continues to say "The harbor undertaking has ended." for this entry, accurately describing the addon flag.
I checked this wording in source, not in a rendered interface.

The terminal choice still writes only `noct.closed` and `noct.undertaking_withdrawn`.
Initial refusal retains its separate `noct.undertaking_declined` reason.
These flags take effect when the player confirms the sole terminal choice after the response.
No branch returns from that response to continued participation.
All visits forbid closure, and all supplementary endings require the unearned `noct.complete` flag.
Previous work remains in history; leaving before the final conversation does not award that final conversation's completion or recollection.

## Scoped scores

| Dimension | Score | Result |
|---|---:|---|
| Late refusal voice and non-agreeability | 94 | Pass |
| Completed-work and parent-bargain semantics | 95 | Pass |
| Staging continuity across both late scenes | 95 | Pass |
| Undertaking-only UI wording | 96 | Source pass |
| Addon closure effects and predicates | 96 | Static pass |

## Verification limits

I independently compared all twenty-four Nocticula source scenes against the current export.
Python checks passed for all sixteen closure terminals, their exact addon-only effects, all visit closure blockers and all ending completion requirements.
No native or parent binding occurs in a closure effect.

The full rules suite was not rerun for these three prose sentences.
The root reports unchanged graph and effects since the previous 28,662,926-assertion pass, and the checks above confirm the current exported closure structure.
My earlier scoped review independently reproduced that full suite on its then-pinned export.
No Unity execution, real save persistence, ToyBox run or rendered UI inspection is claimed.
The broader selected-route length, acquisition, recovery and art-assignment gaps remain unresolved.
