# Konomi native availability review

DiplomacyOfficer_InDrezen Playing is a justified positive gate for ordinary Drezen meetings.
Its inspected actions actually unhide and position Konomi's officer actor.
It is not a universal alive predicate, and its temporary inactivity must not close the romance.
Apply it to the ordinary contact scenes, not the Abyss letter or epilogues.
No recovery or new contact was implemented by this audit.

## Positive officer state

World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/DiplomacyOfficer_InDrezen.jbp is BlueprintEtude b5f301fbc4c44535a6309d610d5bd28a.
Its repeating EtudePlayTrigger executes HideUnit with Unhide true and then TranslocateUnit with copied rotation.
Both actions target RankUpOfficer_Diplomacy spawner c658c4cf-116e-4b61-9ff9-8905bcf4fd6b in scene 3e2b5ea054cd5b2479e7f13134363ef4.
The destination is DiplomacyOfficer_Position locator e6a7de2a-ce6f-4413-b24d-06daf1990e4c in the same scene.
This is direct evidence of ordinary contact positioning, not an inference from the etude's name.

The etude links to Drezen area 2570015799edf594daf2f076f2f975d8 and requires NotInCombat e0d8b253efedb70488badaaa3d47632c Playing.
NotInCombat contains an EtudePeacefulZone component and participates in native encounter conflict groups.
DiplomacyOfficer_InDrezen permits action starts, has no explicit completion condition, and has no UnitIsDead condition.
Its parent is RankUpOfficers e423e4d675b64f2bb974cb453aaed4fd.
That parent has no additional activation conditions in its own blueprint and in turn belongs to parent 1a2fbd3143c42c542a15be2ff1a2c33d.
The filename's Chapter03 directory does not itself impose a maximum chapter.

DiplomacyRankUp2 e513ab6862e999644acde5a994911f5a starts DiplomacyOfficer_InDrezen during its play trigger, after launching the rank-up cutscene.
Source path: World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/RankUps/DiplomacyRankUp2.jbp.
An ordinary-contact requirement should therefore use Playing, not merely Started or not Completed.
A not-Completed check would also admit a never-introduced officer.

## Hidden fallback and temporary displacement

World/Etudes/Common/WrathOfTheRighteous/Chapter03/CapitalMechanic/DrezenCapital_DefaultMechanic/Capital_NPC_DefaultActors/RankUpOfficer_Diplomacy_DefaultActor.jbp is BlueprintEtude 0b828275326053d4cb989baddb20bce7.
Its repeating EtudePlayTrigger hides the same officer spawner with Unhide false.
Its priority is -100 in conflicting group Capital_NPC_RankUpOfficer_Diplomacy, 12b19db05c70a2a4fa3210293d35bfd0.
The positive officer state has priority -20 in that same group.
DiplomacyRankUp2 through DiplomacyRankUp8 each also belong to that group with priority 0.

Consequently, native conflict arbitration can suspend the ordinary officer state while a rank-up owns the actor, then restore ordinary positioning afterward.
When the positive state has been completed and no higher-priority encounter owns the actor, the hidden fallback can take over under its active parent.
The completing action does not itself issue HideUnit, so the fallback is an important part of the dismissal mechanism.
This is a structural reading of the native blueprints; no fresh game load was performed in this review.
It supports deferring ordinary romance entries during temporary displacement rather than interpreting every false presence check as death or breakup.

## Rank-six dismissal

World/Crusade/RankUps/Diplomacy/Diplomacy_6/Answer_0070.jbp is BlueprintAnswer 73c5728c4c6658344bedcc1b666e598c.
Its localized text dismisses Lady Konomi along with the Royal Council.
This is an explicit selected-answer history marker, not a dialogue-name guess.
The answer's own OnSelect actions change diplomacy progression and unlock flag 60fb03a2922141338d6f73e8875a7806 with value 1.
Those progression actions must not be replayed by a future personal invitation.

Diplomacy_6_Dialogue.jbp, BlueprintDialog 30333438aac8d3647bef882fa87e978e, has a FinishActions Conditional checking that answer with CurrentDialog false.
Its true branch executes CompleteEtude on b5f301fbc4c44535a6309d610d5bd28a.
Root/Upgraders/Player/PF-360384.jbp, BlueprintPlayerUpgrader fbda3f5666a44d92af69e12338629a16, checks the same selected answer and completes the same etude as a save repair.
This independent updater corroborates that the selected answer is intended to remove ordinary officer access.
Completing the presence state is not a native death action.
A later personal approach can therefore be written as contact after dismissal without pretending that she died or that her official appointment was restored.

## Swarm removal

World/Etudes/Common/WrathOfTheRighteous/MythicLocust/Drezen_SecondState_Locust.jbp is BlueprintEtude 3b2a1572df0d448fb262b4115a1fad95.
Its crusade-advisor removal play trigger completes the positive officer etude and then executes DestroyUnit on the same RankUpOfficer_Diplomacy spawner.
This differs materially from rank-six dismissal, which only completes the ordinary presence state.
DestroyUnit is actor removal, not proof by itself of a narrated murder or recoverable corpse.
A restoration implementation must inspect actor existence and scene handling rather than simply clear a dialogue flag.
No ordinary meeting should claim restored Swarm contact from this audit.

## Rank-eight council conclusion

World/Crusade/RankUps/Diplomacy/Diplomacy_8/Cue_0081.jbp, 7f64a30ceb4bfb046990bccbded7ac75, says the Diplomatic Council has served its purpose.
Its own conditions, OnShow, and OnStop are empty.
Diplomacy_8_Dialogue.jbp, 6178470b05c75484085753b821a6a614, finishes by incrementing progression flags and conditionally completing a crusade objective.
It does not complete DiplomacyOfficer_InDrezen or destroy the officer actor in its inspected finish actions.
The full reference scan for b5f301fbc4c44535a6309d610d5bd28a found rank-six dismissal, its updater, rank-two introduction, and Swarm removal, but no direct rank-eight removal consumer.
Therefore normal council completion must not be equated with Konomi's dismissal or physical disappearance.
The private route may still need institution-aware wording after the council concludes, but that is separate from whether she remains available to talk.

## Repeatable dialogue root

World/Crusade/RankUps/Diplomacy/Diplomacy_Officer/Diplomacy_Officer_dialogue.jbp is BlueprintDialog a81655ed97277974e947c1aaf9e33525.
It has no dialog-level conditions, no start actions, and no finish actions.
Its FirstCue sequence tries Cue_0001 3269417315940ed4daf2a345b5812c4f, which is ShowOnce, followed by Cue_0002 bd0fd5f2a10163941a4e01ada9edc850, which is not ShowOnce.
Both cues use AnswersList_0003, BlueprintAnswersList 0dc8b8604bb33c846a63f3eb62443674.
The answer list has no conditions and is not ShowOnce.
The root is consequently reusable when the actor can be contacted.
This does not make the actor available when the native presence mechanism has hidden or removed her.

## Implementation boundary and future invitation

The proposed konomi.present alias should map exactly to b5f301fbc4c44535a6309d610d5bd28a and require its Playing state on ordinary scenes alongside the existing Drezen area restriction.
Do not add it as a relationship-wide failure or closure condition.
Do not require it for a letter written alone in the Abyss, historical journal entries, or an ending.
Do not silently restart the completed officer etude as the way to make a private invitation accessible.
That would undo an official dismissal and re-enter native actor management without an authored reconciliation.

A future Trickster invitation can distinguish never-established official contact, personal contact after dismissal, and actual actor destruction.
After dismissal, the story should acknowledge the Commander's prior decision and allow Konomi to accept or refuse personal contact without restoring her commission.
A new encounter should preserve the selected rank-six answer and its political effects.
Where the actor was destroyed, restoration needs a separately verified implementation and an accurate explanation of what returned.
Current evidence does not establish a universal contact bypass for crusade automation, unfinished introduction, arbitrary mod changes, or every transformed campaign.

Supporting raw records are konomi-availability-consumers.json, konomi-availability-context.json, and konomi-availability-dialogue.json.
This report assigns no writing score and makes no full-route readiness claim.
