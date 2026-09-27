# Konomi retained-return placement audit

Resurrection alone does not make every retained Konomi available for the current aftercare scenes.
A dismissed or not-yet-appointed actor is normally hidden by a separate native placement etude, and her scene spawner also starts hidden.
A personal meeting can temporarily displace that exact hidden fallback without restarting her office or clearing dismissal.
The native selector probe supports a candidate priority of -90 for that meeting, below every audited office/rank-up claim and above only the known hidden fallback.
This is a proposed implementation contract, not an implemented meeting or successful Unity revival.

## Current reachability

The inspected `src/KonomiRecovery.cs` SHA256 is `5D03FC5270B69B8CEACA3A9C55702060106CD1AF1FB8C3CECAC9774A647901BD`.
The inspected `src/NativeContact.cs` SHA256 is `018BE371E40D1950564D6C74D1EB79CD195E781DCF2C28FA0A8CC826D10170B3`.
The inspected four-scene `storylines/konomi_retained_return.py` SHA256 is `B0514BA7BE3BA5115899BB9B4E533EAEDFAE359A599B3670924DD1B2B566E227`.
ReturnContactAvailable requires the exact restored actor among loaded units and all NativeContact checks, including an active loaded view, IsInGame, consciousness, current storage and no hostility or suppression.
The two aftercare visits require that positive contact flag.
The first aftercare scene already speaks to her physically, and its later invitation cannot unlock itself for an actor still hidden before that first scene.
The preceding resurrection attempt contains no authored personal meeting invitation or reply.
A remote, nonphysical invitation/reply between verified life and the first physical aftercare scene is therefore needed for hidden histories.
The existing invitation for the second visit can authorize its later meeting window after the first scene becomes attainable.

## Exact native identities and actions

| Purpose | Identity |
| --- | --- |
| Capital area | `2570015799edf594daf2f076f2f975d8` |
| Saved scene name | `DrezenCapital_Default_Mechanics` |
| Scene asset | `3e2b5ea054cd5b2479e7f13134363ef4` |
| Original Konomi unit blueprint | `ca2d58c5c65723945857e04fb85d30ce` |
| Original RankUpOfficer_Diplomacy spawner | `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b` |
| Native DiplomacyOfficer_Position locator | `e6a7de2a-ce6f-4413-b24d-06daf1990e4c` |
| Actor conflict group | `12b19db05c70a2a4fa3210293d35bfd0` |
| Hidden default etude | `0b828275326053d4cb989baddb20bce7`, priority -100 |
| Ordinary office etude | `b5f301fbc4c44535a6309d610d5bd28a`, priority -20 |
| Selected rank-six dismissal answer | `73c5728c4c6658344bedcc1b666e598c` |

The hidden default's archive path is `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/Capital_NPC_DefaultActors/RankUpOfficer_Diplomacy_DefaultActor.jbp`.
It has one EtudePlayTrigger, m_Once false, with one HideUnit action targeting the exact spawner and Unhide false.
There are no quest, dialogue, rank or death actions in that trigger.
Its activation checker is empty, its parent is `ce5f755519ff2c945ab4eacd67d3f8e3`, and that parent's StartsWith includes the hidden default.
The parent in turn belongs to `30862a76dd4a11049be42d3de26159fb`.
Do not force any of these parents into a playing state to create a meeting window.

The office archive path is `World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/DiplomacyOfficer_InDrezen.jbp`.
Its repeating trigger first calls HideUnit with Unhide true and then TranslocateUnit to the native locator, copying orientation from that locator.
It requires NotInCombat `e0d8b253efedb70488badaaa3d47632c` Playing and is linked to the capital area.
Its parent chain includes RankUpOfficers `e423e4d675b64f2bb974cb453aaed4fd`, RankUps `1a2fbd3143c42c542a15be2ff1a2c33d` and `0264cfa0da54fbd4e897fcd193d82bf3`.
Those immediate parent activation checkers are empty, but live parent/campaign/area eligibility still needs the native fact state.

The rank-two trigger starts the office etude after launching the rank-up cutscene.
The rank-six dialogue finish and player upgrader complete that office etude when the dismissal answer was selected.
Neither should be replayed, erased or reversed for a personal meeting.
Rank-eight council conclusion is not itself office dismissal.
Swarm etude `3b2a1572df0d448fb262b4115a1fad95` completes office access and calls DestroyUnit on the exact spawner.
A destroyed or absent actor is not a retained corpse that this placement proposal can resurrect or move.

## Every audited competing claim

A fresh byte-content scan of every jbp in installed blueprints.zip found the following etudes explicitly sharing the actor group.
The scan also retained all spawner and office-reference consumers, including the Swarm destroy action and dismissal repair.

| Etude | GUID | Priority |
| --- | --- | --- |
| Hidden default | `0b828275326053d4cb989baddb20bce7` | -100 |
| Office | `b5f301fbc4c44535a6309d610d5bd28a` | -20 |
| DiplomacyRankUp2 | `e513ab6862e999644acde5a994911f5a` | 0 |
| DiplomacyRankUp3 | `71df1c68c12597643958448bfe97b5b5` | 0 |
| DiplomacyRankUp4 | `94dd874651f8e7840988a71c508ce235` | 0 |
| DiplomacyRankUp5 | `1d8fe7ff1dc86394d8abdc578c9fb4eb` | 0 |
| DiplomacyRankUp6 | `ca689964117a4a52924362442702ee8e` | 0 |
| DiplomacyRankUp7 | `b972856b6dd54910a93ffde0b84fa05c` | 0 |
| DiplomacyRankUp8 | `cbbf833050aa4ad99550559bfc4427a6` | 0 |
| ExampleMilitaryRankUp | `5e9ac74d787de04428043a2cdeb2579f` | 0 |

The example-named etude still contains a real actor claim and cutscene action in the archive.
Do not assume its name makes it safe to interrupt if it is actually started and eligible.
Rank-up activation requires no other member of group `10d01be767521a340978c8e57ab536b6` Playing.
The diplomacy events also claim `829ef51ab732b0e4f934859c5a307870`; the example claims `3e74f31d7165bbe4594856814cee1090`.
They are actual events, not background actor placement.
The personal meeting should claim only Konomi's actor group and refuse every unreviewed holder, including future mod-added lower-priority holders.

## View and resurrection behavior

The existing scene extraction `konomi-contact-records.json` matches installed `drezencapital_default_mechanics.scenes` SHA256 `D451FEF29C6B22F5D13E8BACEA70BA063175DDEE8B3F43F48D6CAE7F22B4A9E3`.
It shows SpawnOnSceneInit true, RespawnIfDead false, SpawnHidden true, SimplifyWhenHidden true, SleepWhenFarAway true and ForceOptimizeInSaves true on Konomi's spawner/components.
The locator and spawner local transforms differ substantially.
Use the real locator evaluator to obtain world placement, not the stored local coordinates as guessed world coordinates.

The installed assembly remains SHA256 `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
Native ResurrectAndFullRestore clears death-specific state and IsHiddenBecauseDead, handles an existing view where present, and raises resurrection events.
Its body does not set IsInGame true or run the office placement trigger.
Therefore an actor hidden by the fallback remains a separate placement problem after verified resurrection.
If the original office actor was already visible and retained its ordinary placement, successful resurrection may be sufficient for contact, but only the current NativeContact observation proves that result.
An officer etude merely marked Playing is insufficient, since its placement trigger may have run before the death.

Fresh native HideUnit decompilation confirms Unhide sets the retained unit's IsInGame true, without spawning a new unit.
EntityDataBase.IsInGame updates an existing view, raises an in-game change event and calls OnIsInGameChanged.
Targeted UnitEntityData decompilation shows that override calls UpdateHasDummyView.
That method can replace a hidden optimization dummy view using AttachToViewOnLoad on the same actor and destroy the old view GameObject.
Actor identity must remain unchanged, but the View reference need not remain unchanged across unhiding.
Re-read and validate the current View after the native action.
Sleeping or absent-view cases do not guarantee immediate materialization.

Native TranslocateUnit calls Unit.GetValue, MarkNoExtra, View.StopMoving and Commands.InterruptMove, then assigns the evaluated position and orientation.
It requires a usable view; successful life proof alone is insufficient.
UnitFromSpawner resolves the saved spawner's existing SpawnedUnit reference and does not create an actor.
Do not use Spawn, ForceReSpawn or TrySpawnOrRespawn to repair a missing view or hidden original actor.
Those operations can replace the actor and violate the retained-identity contract.
A genuinely absent view needs a separately reviewed same-entity view restoration or normal reload path; UpdateHasDummyView returns without creating one when its current view is absent.
This remains required follow-up, not a declaration that such histories are impossible.

## Proposed attainable personal-meeting contract

1. After currently verified recovery, deliver a remote request for a short visit that does not require physical contact.
Konomi's reply must explicitly choose whether to meet and supply an authored meeting request flag.
A refusal or delay does not undo her resurrection or her native political history.
The existing next-visit invitation can authorize the second meeting window.

2. Require the exact original living conscious actor, source scene/storage/registry agreement, confirmed return identity, peaceful loaded capital and a conscious non-hostile Commander.
Require the native hidden fallback as the only allowed displaced holder, with its actual parent and scene eligibility intact.
If office placement already supplies actual contact, use that contact without starting or restarting the office.
If a rank-up, cutscene, unknown claim, conflicting representation, load transition or unresolved view owns the situation, wait.

3. Start a genuine addon meeting etude with proposed priority -90 and only the exact Konomi actor conflict group.
The native selector must acquire its actual held claim before any move or unhide.
Check eligible pending native events as well as held claims, using their real parent, campaign, area and activation conditions.
A priority rule alone is not permission to take an unknown lower-priority event.
Do not directly write the native held-claim dictionary in production.

4. Preflight the exact actor and the real position/orientation locators before mutation.
Use the native unhide path under the held meeting claim, then re-resolve the same actor's current view before native translocation.
This follows the office's unhide-before-move order and accommodates dummy-to-real view replacement.
Recheck identity and claim between operations and verify position, loaded active view and NativeContact after placement.
If either action fails or the claim changes, report no arrival and yield through the genuine lifecycle; do not start the physical aftercare dialogue on an attempt alone.
A short visit at the existing locator changes actor placement, not office appointment; authored wording should identify it as her chosen personal visit.

5. Keep the temporary request separate from proof of arrival and from romance state.
On ending, interruption, combat, area departure or native event eligibility, withdraw the addon claim through its normal lifecycle.
Allow the native fallback to resume and hide its actor, or let the native office/rank-up become the new owner.
Never restore an old position or hide the actor after a different native holder has taken control.
No native completion, dismissal, rank-up or selected-answer state is rewritten.
Save/load must revalidate the actual held claim and same actor, rather than trusting a saved Placed bit.

## Actual native selector witness

The isolated `Probe.csproj` uses installed EtudesSystem, EtudesTree, Etude and BlueprintEtude classes with the exact native actor group and audited priorities.
It calls actual FilterOnActors, RemoveFromPlaying and AddToPlaying methods on detached native fixtures.
It passes 14 assertions with zero build warnings and errors.

The probe proves meeting -90 schedules hidden -100 to stop, but scheduling alone does not transfer the held claim.
Office -20 and rank-up 0 block it and can preempt it later.
An eligible pending rank-up wins independent of insertion order.
An unknown holder at -95 would be stolen by raw priority, demonstrating why the allowlist is required.
After actual release the original hidden fallback can hold the group again without being completed, and a stale meeting release does not remove a later office holder.
These checks establish native arbitration behavior, not actor visibility or successful placement.

The optional full selector observation retained the higher-priority office fixture and did not activate the meeting.
Direct OnActivate then reached a missing GameHistoryLog dependency in the standalone process.
No full activation, actor unhide, movement, dummy-view restoration, Unity scene visibility or game save/load success is claimed.

## Evidence and remaining checks

All temporary extraction and probe files are in `C:/Users/Z/AppData/Local/Temp/konomi-return-placement-l8f6kpb7`.

| Evidence | SHA256 |
| --- | --- |
| Fresh native consumers.json | `35A6FC24B22A2F05E909A0334D456F8843B053D472C3002C9DC89F4E6242C6AA` |
| Native parents.json | `A131B9199CA389C627768794D997122391A430D3C45D66E05F184A46BE9F9004` |
| Native selector Program.cs | `D1F8E5FC0B2FD0695E125D6788EA4415A7AB24451736086301CC2B5B3D33F2BC` |
| probe-output.txt | `B5BBEA4432244EC3EFDC3485D913081FFF8C95FCC3AABC4664CBAA435565DAAE` |
| Targeted UnitEntityData-methods.txt | `B43852A61A7EC4D8A0E0511AFB12F688CA629974792585BB5CDC783A6C13A757` |

The temporary DecompileMethods project extracts individual native methods to avoid a full-type ILSpy stack overflow.
That failure did not affect the successful HideUnit, TranslocateUnit, UnitFromSpawner, EntityDataBase or targeted UnitEntityData evidence.

Implementation must still prove the remote reply is reachable for dismissed and preappointment saves, then prove their original actor becomes visible under the temporary claim, aftercare starts only after actual arrival, and office/history remains unchanged.
Test a native rank-up beginning during the visit, a new native appointment, refusal, partial placement failure, sleeping/dummy views, area changes and save/reload.
Missing/destroyed bodies, missing views, hostile histories and cross-area travel remain separate required recovery work.
Only this report and temporary probes were written; no production helper was added before contract review.
