# Arsinoe interruption audit

The corrected five-scene source has no remaining concrete interrupted-reentry blocker identified in this bounded review.
The review found one additional premature event flag, which the parent reproduced and corrected before release of this report.
This is a source and state-transition review, not proof of Unity interruption timing or an installed save round trip.
I edited only this report.

## Inspected revisions

| File | SHA256 |
| --- | --- |
| `storylines/arsinoe_opening.py`, initial audited revision | `29967C5466D0DE8D4E3CF059F3D0C5B4706029A71D245F82E42038275CF449C7` |
| `storylines/arsinoe_opening.py`, accepted correction | `0E9EE2F8ACEB8626850C9D754D84728FF5DB5E760B0EE52D48E4159A6EF4F3BA` |
| `tests/ArsinoeOpeningTests.cs`, corrected focused coverage | `C743A90E93A0D7837D31337606F20BAD366C663D81AF07EFB8A78BF6F76AC112` |
| `src/Main.cs` | `F1AE3AECD57BAD6DADF2E25F11D18D3756802E9D3733E74A06F72A10E2F0DFEA` |
| `src/Story.cs` | `DD6B591E40FEDD2EAF6BACD4D58E6B86C7BAD50FD80569EBCEECE872C3467F8D` |

## Additional finding and correction

In `arsinoe_hours_of_her_own`, the `romance` page's Kiss answer originally wrote `arsinoe.first_kiss` before entering the `kiss` page.
`Main.BuildScene` records answer effects through `RouteAction.OnSelect`, separately from the answer's next cue, while the conversation-completion flag is written only on a terminal answer.
Consequently, the source state after choosing Kiss could contain `first_kiss` while the scene remained incomplete and its payoff had not been acknowledged.

I traced the retained state through an interrupted reentry using `start -> table -> recipe -> evening -> romance -> hand -> parting`.
That hand-only replay completed the scene with `first_kiss` still set and no kiss page visited in the replay.
The current opening has no prose callback conditioned on `first_kiss`, so the demonstrated defect was false recorded intimacy history rather than an already observed downstream dialogue failure.
The report to the parent stated that limit explicitly.

The parent added a focused actual-rules probe and reported the expected red assertion: `Arsinoe kiss recorded before its page is acknowledged.`
The correction removes the effect from the initiating answer and places it on the existing Continue answer after the kiss page.
It changes no scene ID, page ID, choice index or prose.
I inspected the exact revised source and independently replayed the proposed-kiss interruption followed by the hand-only path; `first_kiss` remains absent.
After the kiss page has been acknowledged, the marker may correctly survive a later interruption because that event has actually been played.

## Earlier repairs checked

The printer's two commission choices now forbid each other's recorded commission flag.
An interrupted commission therefore retains the first choice instead of allowing both `print_fantasy` and `print_street`, which would otherwise expose contradictory result pages later.
The existing focused test captures both partial result states, removes and restores contact, and checks that completed replays retain exactly one commission.

The roof's courting, slow and friendship flags now occur on their respective terminal answers, alongside `roof_shared` and scene completion.
They are not recorded while entering `touch`, `slow` or `friend`.
Changing the answer after an interruption before completion therefore does not accumulate multiple relationship modes.
The existing focused test captures all three partial pages and checks exactly one final mode after restored reentry.

The later table-versus-walk invitation also writes its preference on the terminal answer which completes that scene.
The observed route does not expose a normal incomplete-scene replay window after that choice has been committed.
The hours scene's mode and location callbacks therefore have a single applicable prior choice on histories reachable from the corrected source.

## Other inspected flags and scope

`print_source_found` is recorded after the successful observation page and is used as persistent knowledge in the printer conversation.
Keeping previously acknowledged knowledge after a later interruption does not itself invent a new observation; the current callback has one positive and one complementary negative condition.
The other initial approach flags do not select competing printer callbacks.
I did not promote unused preference-marker accumulation into an imagined current dialogue failure.
No additional reachable empty-choice page or contradictory current callback was identified from the remaining opening flags.

The native contact guard and flag-free contact-lost exit remain responsible for stopping continuation while the actor or the capital/event predicates are unavailable.
The review did not change those guards or treat a temporary event as permanent relationship closure.
Existing live actor, native event ownership, skill-roll scheduling, UI, art and save-persistence limitations remain those of the prior contact integration review.

The parent was running the combined Arsinoe/Konomi stage when this report was released.
This report accepts the exact source correction and inspects the focused test without claiming that still-running staged suite as an independent result.
No full-route readiness score or installation approval is assigned.
