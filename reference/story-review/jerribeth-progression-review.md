# Jerribeth progression independent review

The new settlement visits and explicit progression choices address the earlier automatic-farewell bypass and give the public and private bargains lasting consequences.
This review covers the seven new scenes and changed progression, refuge and ending text.
It does not renew full literary approval of the older counteroffer module or approve the complete route.
The corrected released revision receives bounded acceptance below.

## Scope and compatibility inspection

I read `jerribeth_progression.py`, the changed `jerribeth.py`, the continuation metadata in `jerribeth_consequences.py` and `jerribeth_counteroffer.py`, and the relevant predecessor bargain outcomes.
I compared the current imported scene objects with the 207-scene `development/Story.json` baseline using a read-only Python script.
All 29 existing Jerribeth scene IDs and every existing node ID remain present.
The revised route contains seven additional scene IDs.
No existing choice index disappears.

The only changed existing choice objects found in that comparison were `jerribeth.future/end/0` and the first `start` choice in each of `ending_together` and `ending_ascended`.
The former keeps its text and original chosen-future flag while joining the new conclusion.
The two ending choices retain index zero while adding the developed-history condition and continuation; an appended fallback permits old saved node positions to finish.
New entry nodes distinguish the intended fresh and legacy histories.
This source comparison does not prove that Unity reloads every partially played old book correctly.

## Prose findings sent for correction

| Location | Selectable history | Required repair |
| --- | --- | --- |
| `settlement_visit/private_cost` | `decline -> private_cost` | The opening answers the cure-clients remark found only on the other incoming branch. Use a self-contained opening. |
| `settlement_visit/after` | Private client routes, particularly `player` and `decline` | The shared conversation recalls a figure stuck beneath an arch, which those demonstrations never showed. Refer to common material or supply branch-specific callbacks. |
| `room_measure/quiet` | `terrace -> private -> quiet` | The shared quiet scene places the figure at a window and discusses its lamp, details introduced only by `loop`. Establish a fresh image or use common staging. |
| Developed ending `account` | `inspection_refused -> public_refused` | The shared ending credits the inspector's question with producing an idea worth keeping despite this path rejecting the commission without that discovery. Gate the creative payoff or use a common consequence. |

These findings concern recalled history, not the viability of the new plot.
They can be corrected without new mechanics or reordered choices.

## Public and private consequences

The public account leads to scrutiny of Jerribeth's own work rather than a cost-free victory over Vardess.
Hessa examines the actual supports and identifies a briefly held image that Jerribeth used to hide a scenery change.
The distinction from a concealed archive remains explicit.
The Commander can suggest displaying the mechanism, removing it from the commission or refusing the commission and accepting the report.
The later visit preserves the consequences: a revised paid design, a smaller fee and smaller possible section, or no second advance.

The private archive path retains the uncomfortable result of returning what Vardess needs to finish his room.
His invitation is evidence of his claim, not proof that the concealed recorder has been completed or stopped.
Cevra wants the same advantage from Jerribeth at a lower price.
Her demands turn the purchased client list into an actual problem instead of a decorative reward.
The alternatives produce a voluntary performance, a fixed comedy about invented rivals, or a refused fee and continued search for another client.
Later dialogue remembers the chosen design and Cevra's attempts to improve her own advantage.

These are authored patrons, payments and construction, not changes to native factions, currency or quests.
The Commander's advice does not transfer funds or issue a native commission.
The inspection permits either acknowledging attendance through the charm or leaving the Commander's name out.
Neither choice pretends remote observation can certify the whole construction.

The new consequences are sustained through `room_measure` and the developed ending.
The smaller payment and refused payment remain frustrations even after the intimate conversation goes well.
The source does not reward romance by making the lost fee disappear.

## Voice, intimacy and agency

Jerribeth remains competitive, possessive of her work and irritated by other people's prices.
She enjoys refusing Cevra's presumptions and threatens no sudden general reform.
Her refusal to falsify Hessa's findings follows an inspection she offered and the demands of this particular relationship; it is not presented as proof that her native cruelty has been absolved.
Her resentful response to losing a fee gives the more considerate choices a cost.

The strongest personal development is her shifting desire for the room.
She initially wants to choose whom to exclude, then realizes she keeps extending the imagined streets because she wants this particular person to ask what lies beyond them.
That is a more specific romantic change than another promise to respect consent in the abstract.
The finished physical section also gives the imaginary ambition a material limit.
Serit still expects payment for the next section, and she has not bought a whole room simply by imagining it.

The remote intimate option is adult and graphic and explicit.
Both sets of hands remain on their respective sides, and the shared experience consists of spoken description and voluntary response.
The alternative remains close company with the image open.
No kiss, physical visit, transported object, mind-reading power or new portal is smuggled through the charm.
Third-party dialogue is relayed by Jerribeth, consistent with the earlier chosen-image connection.

Much of the commercial dialogue turns on artistic irritation and pointed qualifications.
That suits this character, although repeated versions of being inconvenient, disliking a question and wanting payment occasionally make several exchanges sound alike.
The varied demonstrations and the refusal costs give these scenes enough action to avoid becoming another abstract terms discussion.

## Earned, shorter and legacy progression

Fresh `future` availability now requires either completed `settlement_kept` or an explicit `short_future_requested` choice.
The developed route therefore plays both the earlier bargains and their new consequences before receiving the developed promise.
The shorter route promises further courtship without claiming the longer evenings have happened.
The ordinary core scene remains available afterward.

`farewell` requires settled future terms plus either the developed future or an explicit shorter-farewell request.
A player who made the shorter promise must actively elect the early farewell through the manual review.
This removes the old automatic cutoff while keeping a usable shorter campaign path.
Manual deferrals set no catch-up request and cannot occupy the automatic rest queue.

For old saves with an existing promise, `old_promise` accepts the earlier promise as real and lets the player choose the shorter farewell without pretending the missing work is complete.
An existing promise followed by the completed new visits can instead reach `promise_revisited`, which offers renewal, keeping the original promise or closure.
Keeping the original promise deliberately retains the modest ending classification even if more content was played.
The phrase about not promising more tonight leaves room for an imagined later conversation, but this scene itself is a one-time choice and should not be described in UI as a repeatable commitment upgrade.

For an old completed farewell, `another_evening` is a manual opt-in.
Its accepted answer sets `catchup_requested`; its declined answer aborts without resetting history.
The three continuation helpers override only the authored farewell prohibition when that request exists.
They preserve the farewell completion rather than deleting it.
The existing relationship closure and unavailability checks still apply through `Rules.Available`.
No restoration or native-contact exception is added here.

The developed endings require the actual developed-future flag and recall the appropriate public account or private catalogue.
The provisional ending acknowledges the real promise while leaving much of the relationship's future undiscovered.
The ascended ending uses the same history distinction instead of awarding the complete settlement memories automatically.
Breaking up remains a voluntary separate result.

## Native facts and remaining boundaries

The changed refuge language concerns losing Vellexia's protection and leaving the manor.
It does not assert that Vellexia died merely because the patron-loss condition was observed.
The existing knowledge and patron-loss requirements remain on that scene.
This is the appropriate narrow textual correction; it does not independently verify all native conditions that set those flags.

Jerribeth's native allegiances, victims and species remain separate from her chosen private relationship.
The new material makes no claim to cure Wintersun, reverse Xanthir's history or end Vardess's authored enterprise.
The existing Trickster invitation to find a loophole remains dialogue, not an implemented recovery route.
This contribution does not prove contact after hostility or death, suitable boundaries for every mythic path, or post-final-battle delivery.

The new scenes specify Chapter 5 and the established Drezen/Nexus area identifiers.
Those metadata values do not prove both areas are ordinarily reachable at that chapter.
Actual route acquisition and contact availability require the separate native audit.
Other romances and ToyBox preferences receive no new exclusion or mutation here.
Runtime coexistence still needs testing.

The existing manual breakup exclusion from the rest queue remains intact.
The present source inspection supports the new progression conditions but is not a fresh production scheduler, managed-blueprint or Unity test run.
Author word inventories and aggregate floors are separate from this literary assessment.
No source-art or runtime-crop approval is included.

## Corrected released revision and bounded verdict

The new structure addresses specific assembled-route problems with played consequences and explicit choices rather than word-count padding.
I read the author handoff and reread all four corrected passages against the released files.

| File | Reviewed SHA256 |
| --- | --- |
| `storylines/jerribeth.py` | `FCD94F9865DE3F0E984633E1AB7DC91F59B8BC8D207F7CFEDC43BCEC2722A086` |
| `storylines/jerribeth_consequences.py` | `640EAAFE48F34AB928ED4F3C6676F31CE482F7103A283AC23ECB1581646BD300` |
| `storylines/jerribeth_counteroffer.py` | `B1FCCD1478DC7551DDBF12934E4EDD9B72B06EF6CFE5211DD72B5B4D09802630` |
| `storylines/jerribeth_progression.py` | `5153BEDCF663FD78FF298DE203ED762B87B9BE34D4EE03D04F01D4734B436D80` |

The private-cost opening now concerns putting the room aside for the evening and fits both incoming replies.
The shared closing asks about the little climbers rather than recalling the public-only trapped figure.
The quiet scene adds its own lamp beside the arch, so it no longer inherits the loop branch's window.
The public ending recalls Hessa's report and Jerribeth's irritation without claiming that refusal produced an unplayed artistic breakthrough.
All four findings are resolved.

Bounded writing score: 92/100.
The new demonstrations give the commercial choices visible action, preserve the costs afterward and make the private desire specific to this relationship.
Repeated patterns of artistic irritation and the brief procedural character of the migration scenes keep this below a higher assessment.

Bounded canon and character score: 92/100.
The new behavior remains plausibly self-interested, the charm's physical limits stay explicit, and the endings distinguish played consequences from modest or legacy promises.
The score concerns these revisions and their joins, not full approval of older prose or every native branch.

No remaining material contribution-level prose or continuity blocker was identified in this review.
Production progression checks, native contact and mythic restrictions, complete-route depth, art and runtime verification remain separate requirements.
