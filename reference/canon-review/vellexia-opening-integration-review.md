# Vellexia opening integration review

Independent technical review completed 2026-09-26.
Accepted for the bounded initial manor interlude; this is not full-route or live-game approval.

## Reviewed revision

Source `storylines/vellexia_opening.py` SHA256 `A48E7BC9EF3DA412D88EE2FCD6C1E408E8C7CC82E96DD340C8F38A91D3E62F2D`.
Focused tests SHA256 `AF3016B82044EAAB5F5F023B3AF5D6E0F81FF273BE049C91A440D7EC28669E74`.
Stage `development/vellexia-opening-review.json` SHA256 `F3143FA07DCAF7FDFFD85EC8CAE0FB7CBF21CDE71DD363D28B3C21D04FE2FFA4`.
I independently compared all six staged Vellexia scene objects with the imported source and found exact equality.
I reran the isolated C# harness against this staged file and reproduced 176,097 passing assertions.
The final source includes the author's two painting-orientation prose repairs.

## Native entry and answer ordering

I read the installed `blueprints.zip` records for the Default unit, main greeting, answer list, invitation and departure rather than treating the author's evidence document as the native source.
The initial actor is BlueprintUnit `a32a07903e428d34cb0e98a804d40569`, not the later ThirdDate identity.
All six scenes require that exact contact, Chapter 4, Upper City area `8217b05e37078414981d994151f0ffb1`, witnessed greeting and their earned predecessor.
The manor AreaPart is not substituted for the area.

One precision correction to the handoff's timing explanation matters: greeting `3850d7abe56fba24fb5acb4b8e0767a6` has a Continue sequence, `0209dca037b369941914fcb6b8dfe2ad`.
It therefore need not expose its answer list immediately on the greeting text itself.
The sequence exit `1f31c1bf677e3e848b8731658f1fc9c9` exposes the same main list `7f394dd6cd32c44408a59bd08eb1512a` with no further Continue.
The actual controller records the greeting in Player.Dialog.ShownCues before PlayBasicCue and its later AddAnswers/CanShow processing.
The expansion gate is consequently satisfied by the time the first native main-answer menu appears after that sequence.
This is a source-level timing verification, not a Unity click test.
The native list has seven answers; the shared injector inserts expansion entries before the last answer and preserves the relative order of all native answers.

Invitation cue `746af280c4d1daa47afbb44c7f8b2eea` grants objective `3e9d164134447ee46a3b96d0c93a9905` and starts etude `3349a1115da1cdd4bae62a5ddd085574` on stop.
The witnessed invitation itself blocks new interlude entry, without depending on those later actions or a disappearance inference.
Native Cue_0022 conditionally teleports Default spawner `3bd514d2-3028-4e73-905f-050dde81e5ea` when that objective is started.
Thus the opening cannot claim continuing early access merely because the unit has not yet teleported.

## Physical presence and persistence

The source does not spawn, restore, teleport or adopt a Vellexia actor.
NativeContact observes exact blueprint equality, rejects duplicates, requires the loaded scene and area entity membership, and excludes disposed, suppressed, dead, unconscious or hostile actors.
Historical greeting, completed quest and a ThirdDate PretendUnit identity therefore do not manufacture current Default contact.
Later native departures documented in the route evidence remain real limitations, not solved continuations.

Every authored Set effect is on a terminal choice with no Next, Check or Abort.
Only authored Vellexia outcome flags are written; full commitment and native intimacy history are not granted.
The actual Rules/Program.Walk suite traverses every page through earned predecessor histories, both advice histories and ordinary/Trickster states.
It checks mutually exclusive outcomes, deferral, untouched native/other-romance flags and identical intermediate flags/timestamps.
Abandoning a page does not persist the abandoned outcome, and restarting uses the original earned input.
Contact loss is tested on every partial page; shared continuation conditions and actions recheck physical contact before progressing or committing.

The narrower shared ContactAvailable continuation predicate does not reapply every scene Forbids flag.
Consequently invitation and completed-quest tests certify prevention of new entry, not immediate cancellation if an external tool changes those flags while a custom book is already open and keeps the actor available.
Normal native invitation interaction cannot run inside that custom book; external mid-book state mutation remains outside this reviewed normal-flow claim.
Dead or fighting states are independently unavailable relationship flags and do stop continuation.

## Skill check and choices

The portrait examination builds a real visible BlueprintCheck: Commander-only SkillKnowledgeArcana, DC28, no experience reward.
The shared constructor supplies PlayerCharacter as the unit evaluator and distinct success/failure cue references.
Success, failure and the non-roll demonstration all have reachable successors and distinct panel histories.
Failure does not end the opening or demand a reload.
The keep/return purchase outcome, private/candid conversation and courting/slow/company intentions persist separately.
Chosen intimate contact requires courtship; the other intentions do not inherit a kiss.
The narrated fee does not alter inventory or native economy state.
The tests model both roll results; this review does not claim an observed native die roll in Unity.

## Acceptance boundary and required follow-up

Technical integration score for this bounded source revision: 93/100.
No blocking graph, terminal-effect, initial-contact or native-answer attachment defect was found within that scope.
This score is a reviewer judgment supported by the checks above, not a full-route quality score or a guarantee for other reviewers.
The root reports combined stage `070879FB0FF8AF03FAA0E1A9525FDD88AEC61E89912C853877782BAABA952230` passed 13,013,025 rules assertions, 506 bindings, 93 native targets, 17 parent checks, 34,689 managed assertions and 10,290 constructed blueprints across nine native answer lists.
Those combined results are attributed to the root; the 176,097 focused rerun above was performed independently here.

These are six parts of one extended initial visit with zero required delays.
The author's measured 3,651-3,838 selected words are an opening contribution, not six independent return encounters or satisfaction of the 21,000-word route planning floor.
Players who accepted the invitation or reached later departures still need real later-contact continuation, preserved-history joins and the bespoke attainable Trickster recovery/access route.
A real save must verify the living manor actor, first menu injection after the native sequence, native die behavior, interruption/save-load behavior and transition through the invitation.
Art, final selected-route volume, endings and actual ToyBox coexistence remain separate requirements.
