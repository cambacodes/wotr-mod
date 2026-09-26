# Independent Tirabade etude lifecycle review

The native departure etude can replay quest-failure actions when reactivated.
Its second trigger is not once-only, and the affected quest is Arueshalae's third companion quest.
The proposed first retained-living Irabeth case avoids this particular Anevia trigger but still requires real selector, placement and save/load verification.
This review implements no meeting, resurrection, native state change or actor transfer.

## Pinned evidence

- Installed `Assembly-CSharp.dll`: `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
- `tirabade-positioning-native.json`: `A10BD12A4653738112B4888F9D94B972FB606362046A0D40A04078C5DAE32579`.
- Inspected parent `tirabade-meeting-position-contract.md`: `00A8DAE1F210BEF42FD152917FC2A93E2B825B3515B5463B125114A8EFFAC30D`.

I independently decompiled the installed trigger, bracket runtime, selector, etude deactivation, conflict release, objective status action and quest-failure propagation.
I also reread the actual archive members and confirmed parsed equality with the five relevant etudes in the recorded JSON.
No native blueprint identity or priority below is inferred from a filename alone.

## Anevia's concrete quest consequence

`World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/AneviaNotInDrezen.jbp` is `6125c10886d6465091f4e092618ca55a`, priority 99.
Its archive-member SHA-256 is `4D4854CEE56814FCB1CD9E09AA8B600BCD2C3D8405E559D51BE383172365A4B8`.
Both play triggers have `m_Once=false` and `IsActivateOnLoadArea=false`.
The first hides capital spawner `86b332a9-5910-4d46-9951-8e06f7dcf0cf` in scene asset `3e2b5ea054cd5b2479e7f13134363ef4`.

The second trigger, `$EtudePlayTrigger$b691237d-ca53-4e98-aba3-cd9e539f0f86`, tests objective `1a32315f0f94f6a4588c2705f9782fee` for `Started` without negation.
Its ordered actions are:

1. Fail `6b9242706b8c43d49003813b869f023e`, with `StartObjectiveIfNone=true`.
2. Fail `1a32315f0f94f6a4588c2705f9782fee`, with `StartObjectiveIfNone=false`.

The tested objective resolves to `World/Quests/Companions/Arueshalae/Q3_WhatYouDreamOf/Obj_01_TalkAnevia.jbp`.
Its archive hash is `0DB6B9542EC7792F8B4794DD49B6EA124BDAF73CA5B3660F55BD73A8D1A56363`.
The first failure target resolves to sibling `ArueQ3_HiddenFail.jbp`, hash `A8EADBD22323356D9D24634B67291C6864E047211070B53AE598148357F717E0`.
That hidden objective has `m_FinishParent=true`, `IsFakeFail=false` and parent quest `a836a86056d777b418cf421aebbc6030`.

Native `SetObjectiveStatus.RunAction` gives a missing objective when requested, then calls the quest helper's failure operation if its state is not None.
`QuestObjective.Fail` refuses a read-only quest or an already completed/failed quest, otherwise changes the objective state and notifies its quest.
`Quest.OnObjectiveFinished` propagates a failed finish-parent objective to quest failure.
This is therefore a potential failure of another companion's quest, not only a placement-side flag.
The second action is still present in the ordered list, although the first can already have finished the parent quest.
Do not assume both operations independently change state after that parent failure.

## Activation, suspension and replay

`EtudesTree.FilterOnActors` sorts starting actor claims by descending priority.
`CheckBlockConflicts` rejects a candidate when a current or earlier selected conflicting holder has priority greater than or equal to the candidate.
An equal-priority meeting has no guaranteed takeover.
`BreakConflictingEtude` schedules an interrupted fact to stop.
`Stop` recursively stops children and deactivates playing facts; it does not complete them.

`Etude.OnDeactivate` marks conditions dirty and calls `RemoveFromPlaying`.
That method removes the fact's conflict-group holdings through `RemoveConflictingGroupTask`.
The stopped, uncompleted fact can become eligible to activate again.
Completion or unstarting would be different operations and must not be substituted for temporary release.

`EtudePlayTrigger.OnActivate` resets `AlreadyProcessedActivation=false`.
`MaybeTrigger` marks the activation processed before evaluating its conditions and runs its actions if `!m_Once || !AlreadyTriggered` and the conditions pass.
Consequently it does not retry the condition on every ordinary update within the same activation.
A condition that was false at the earlier activation may be checked again after suspension and reactivation.
That distinction is exactly why a newly Started TalkAnevia objective can be endangered by releasing an authored override.
`m_Once=false` means actions can replay on a new activation, not that they run repeatedly on every tick.

The bracket runtime separately handles entry and linked-area availability.
A managed call to the trigger's activation callback does not prove that a complete live etude has won its conflict or entered an available area.
The native held-conflict dictionary is not marked for serialization like the etude-state dictionary, and `FixupActorChanges` reconciles holdings from playing facts after load.
Saved authored request state is therefore not sufficient arrival evidence.

## Bounded native managed witness

The isolated project is `C:/Users/Z/AppData/Local/Temp/etude-replay-_ztftmb6/Probe.csproj`.
It compiles against the actual installed managed assemblies into its own temporary output.
It uses the actual native `EtudePlayTrigger`, its native runtime and event context, an in-memory native etude/blueprint with an empty added-mechanics list, and a counting test action.
Reflection supplies the detached fixture's fact reference; no game actor or native quest is changed.

Four assertions passed:

1. The first activation executes the counting action once.
2. Another update in that same activation does not execute it again.
3. Reactivation executes it again when `m_Once=false`, despite prior `AlreadyTriggered` history.
4. Setting `m_Once=true` in the test fixture prevents another execution after reactivation.

This demonstrates native action replay, not a copied implementation of the branch condition.
The once-only mutation occurs exclusively in the synthetic fixture as a contrasting test, not in installed content.
A nonempty condition fixture could not run normally outside Unity because `ConditionsChecker.Check` invokes `ProfileScope.New`, which accesses `Application.isEditor`.
Its error-reporting path then failed on the detached test element's missing asset identity.
I did not patch those engine methods to manufacture a successful quest test.
The final passing probe uses empty conditions; the objective gate and failure propagation above are verified by native source and archive records, not claimed as executed quest behavior.
No real arbitration, linked-area enter/exit, loaded actor, quest save or save/load round trip was exercised.

## Review of the proposed meeting contract

The stated Irabeth identities and priorities match the actual archive:

| Role | Blueprint | Priority | Inspected play actions |
| --- | --- | ---: | --- |
| Default hidden | `dedf24e8a06c48f449b85044879d3d62` | -100 | Hide |
| Throne-room placement | `48967c3ec4330294ab1f5d24d9b45052` | -50 | Unhide, translocate |
| Ordinary departure | `99a03d4f02004b76a5e97c85ba0ec37e` | 99 | Hide |
| Queen expedition | `260454e5186fbd34694a0393097f77b5` | 400 | Hide |

All four claim Irabeth group `997d865aa6f17cc48b480bd62ba02841`.
The ordinary departure and queen-expedition etudes explicitly link the capital area part `2570015799edf594daf2f076f2f975d8`.
The default and throne-room records rely on their parent context, so their missing direct area field does not authorize arbitrary-area use.
I found no contradiction in the contract's limited retained-living Irabeth target or its exclusion of death, unresolved Iz alternatives and the queen expedition.

Priority 100 is only a candidate above the observed ordinary hide at 99.
Native arbitration will not automatically yield it to a newly eligible lower-priority event.
The contract correctly requires explicit detection of eligible non-background pending claims, not only inspection of the present holder.
That eligibility must use actual parent, activation, area and campaign conditions; a started flag alone is not sufficient.
I have not reproduced a full selector test establishing that the future implementation does this correctly.

The contract should explicitly identify the Arueshalae Q3 failure consequence described above.
Anevia cannot be declared safe merely because TalkAnevia is not Started at invitation time: None can later become Started while the placement is suspended.
A conservative candidate window is after that quest has genuinely reached a native terminal state, with state rechecked at acceptance and release, but this report does not prove all ways external mods might alter those states.
An earlier window needs a specific native quest-history argument and a tested release policy.
Do not block release indefinitely, reset the objective, suppress the trigger or change `m_Once` to hide the problem.

Decision: the contract is a defensible bounded research/implementation proposal with the additional named quest consequence, not approval of an implemented return.
Cross-area retained actors, Anevia access, death recovery, real positioning and Unity save/load remain outstanding.
