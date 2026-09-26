# Tirabade retained-actor meeting contract

This is a proposed implementation contract, not an implemented return or a live-game approval.
Root inspected the installed `Assembly-CSharp.dll` with ILSpy for `EtudesSystem`, `EtudesTree`, `Etude` and `EtudePlayTrigger`.
The input native actor records are preserved in `tirabade-positioning-native.json`.

## What the native lifecycle establishes

`EtudesTree.SelectPlayingEtudes` gathers eligible starting facts, filters conflicting actors, stops interrupted facts and then activates selected facts.
`FilterOnActors` orders starting actor claims by descending priority.
`CheckBlockConflicts` rejects a candidate when a conflicting holder has at least its priority.
Equal priority therefore does not provide a reliable takeover mechanism.
`BreakConflictingEtude` schedules the former holder to stop rather than completing its history.

`Etude.OnDeactivate` removes its conflict-group claims and marks conditions dirty.
It does not mark the etude completed.
An eligible stopped fact can be selected again later.
`EtudePlayTrigger.OnActivate` resets `AlreadyProcessedActivation`.
`MaybeTrigger` can then run its actions again when `m_Once` is false and the trigger conditions pass.
Consequently, returning control to a native placement can rerun more than its positioning actions.

`EtudesSystem` serializes its etude-state dictionary but does not mark the held-conflict-group dictionary for serialization.
`FixupActorChanges` reconciles claims from playing facts after load and can schedule conflicting facts to stop.
An authored saved claim is therefore insufficient proof that an actor is currently available after load.

## Concrete hazards in the installed records

Anevia's departure hide etude `6125c10886d6465091f4e092618ca55a` has priority 99 and two repeatable play triggers.
The second tests whether objective `1a32315f0f94f6a4588c2705f9782fee` is Started.
If true, it fails `6b9242706b8c43d49003813b869f023e` with `StartObjectiveIfNone` enabled and then fails the tested objective.
The independent audit identifies these as Arueshalae's `WhatYouDreamOf/ArueQ3_HiddenFail` and `Obj_01_TalkAnevia`.
The hidden failure objective finishes its parent quest, so the possible consequence extends to an existing companion's quest.
Reactivation could therefore change quest state if that condition becomes true between the original activation and the meeting's release.
Do not change `m_Once`, complete the native etude or suppress its quest actions to conceal this consequence.
The independent lifecycle review must determine a bounded safe invitation window before this claim can be interrupted.

Irabeth's ordinary departure hide `99a03d4f02004b76a5e97c85ba0ec37e` has priority 99 and only the inspected hide action.
Her separate queen-expedition placement `260454e5186fbd34694a0393097f77b5` has priority 400.
The expedition is an actual location commitment and must not be classified as an ordinary political departure.

Priority alone cannot classify background placement.
The archive contains ordinary throne-room placements at -50 and hidden defaults at -100, but also actual Camellia and Wenduag events at -10 and Sosiel events at zero.
A rule allowing every nonpositive-priority holder would steal those events' actors.

## First implementation target

Implement an accepted, temporary meeting with a retained living Irabeth in the loaded capital state after a verified political departure.
Use the existing exact-identity observer to reject death history, the queen expedition, ambiguous Iz representations, missing saved ownership and unavailable views.
This target is one delivered recovery case; Anevia, retained death, reconstitution and cross-area travel remain required subsequent work.
The invitation remains remote and attainable without the absent actor, with her answer earned through the authored request.
It grants neither a lover flag nor a physical-arrival flag.

The meeting owns only Irabeth's conflict group while its accepted request is active and its exact actor is available in that state.
An initial priority of 100 is only a candidate for managed and live tests against the verified ordinary hide at 99.
It is not approved merely because the arithmetic works.
It must yield explicitly to every eligible non-background native event, including events below 100.
The queen-expedition claim is never background.

Background recognition must use reviewed blueprint identities, not priority ranges or name substrings.
For Irabeth the inspected candidates are default hidden `dedf24e8a06c48f449b85044879d3d62`, throne-room `48967c3ec4330294ab1f5d24d9b45052`, and the specific ordinary departure hide above.
Their parent and action context still governs whether each is safe to interrupt.
Unknown conflict holders or unresolved references defer the meeting.
No native parent, completion or started state is changed to manufacture an eligible window.

Before taking the claim, inspect started facts sharing that exact group and their current area, campaign, parent and activation eligibility.
Do not inspect only the current winner: a lower-priority pending native event can otherwise remain suppressed by the meeting.
Reevaluate on native etude updates and when requests, area or actor evidence change.
The implementation must avoid recursively updating the etude system from its own condition evaluation.

## Arrival and release

Use native same-state positioning for the retained actor only after the meeting wins its claim.
Do not add the object to a second scene state's list or adopt a different capital representation of someone dead at Iz.
Confirm the actor after the update by exact saved identity, registry membership, holding state, usable view, consciousness, nonhostility and actual meeting ownership.
Only then can a physical scene open.
Check both women independently before any shared scene; Irabeth's accepted return does not imply Anevia's presence or agreement.

When native activity preempts the meeting, invalidate physical availability immediately and allow the existing flag-free conversation interruption exit.
Preserve the request as pending only if the actor is still the same willing living participant.
A death or new departure does not trigger automatic respawn or renewed consent.
At release, stop the authored placement and let native selection restore its own placement; do not restore an old position over a newer event.
After save/load, discard cached arrival certainty and reobserve ownership and actor state before displaying physical choices.

## Evidence still required

The native source establishes selection and replay mechanics, not a successful end-user return.
Before approval, exercise the real native selector with ordinary hide, equal-priority events, lower-priority pending events and the expedition claim.
Exercise claim loss and reacquisition using the same retained actor, then verify actual positioning and save/load in Unity.
The Anevia trigger needs its separate replay witness and quest-history decision.
No production positioning code, custom placement blueprint or invitation is registered by this document.
