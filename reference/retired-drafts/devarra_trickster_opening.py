"""Unregistered Devarra opening experiment for the Trickster route.

The local DLC script provides a living Devarra encounter after the main-game
dragon hunt, but this file does not implement transfer, resurrection, contact,
or any native state producer. Egg outcomes change her motives, never consent.
"""

from copy import deepcopy

from story_format import c, n, scene


RELATIONSHIP = dict(
    Title="The dragon who remembers",
    Description="Devarra decides whether the Commander deserves another conversation.",
    Objective="Answer Devarra without rewriting her memory or her choice",
    Guidance="Unregistered Trickster opening experiment; actor delivery and chronology are unverified.",
    StartedFlag="devarra.trickster.started",
    ClosedFlag="devarra.trickster.closed",
    CommittedFlag="devarra.trickster.courtship",
    UnavailableFlags=["devarra.trickster.identity_lost", "devarra.trickster.refused"],
    FailureFlags=[],
)

NATIVE = {
    "main_dead": {
        "RedDragonDead": "581521b398fb9dd4eb52bbfffb3b5c43",
        "RedDragonKilledInIvorySanctum": "056ba61e04cca104a9c95ac2d4658c67",
    },
    "brood_saved": "4ba6fd446353825459f469fe5973fd87",
    "kingdom_egg_project": "4aa538f07bd542f7a013b90464577d67",
    "dlc_battle_death": "d713e8b772484376a7da810c37ab7922",
    "saved_brood_dialogue": "8c53478782244b90a37f727f7b814318",
    "destroyed_brood_dialogue": "d368680393304b5ba324dd5a517140ed",
}

CONTRACT = {
    "status": "design only; not registered and none of these custom requirements has a runtime producer",
    "native_entry": {
        "saved_brood": "Continue from DLC1 Storyteller Tower cue 8c53478782244b90a37f727f7b814318, where the native scene presents Devarra and recognizes the spared brood.",
        "lost_clutch": "Continue from DLC1 Storyteller Tower cue d368680393304b5ba324dd5a517140ed, where the native scene presents Devarra and records her accusation.",
        "boundary": "This is a proposed continuation inside that DLC encounter. It does not claim a restored main-campaign body, survival beyond the DLC scene, or an implemented cue hook.",
    },
    "trickster_setup": "This authored follow-up would offer Devarra a separate invitation after her native public exchange. The second-conversation producer is unimplemented; Trickster supplies this bespoke opportunity, never her consent.",
    "eligible_histories": [
        "native Devarra main-campaign death state inspected exactly",
        "actual Ivory Sanctum egg outcome inspected independently",
        "DLC Devarra actor identity and encounter availability verified",
    ],
    "trickster_intervention": (
        "If the main-campaign Devarra was killed, Trickster may propose a costly, "
        "bounded restoration that returns her memory and agency intact. This needs "
        "a living body or explicit resurrection mechanism, her soul's willingness, "
        "and a verified actor producer. A remembered conversation or DLC encounter "
        "alone is not proof of main-campaign resurrection."
    ),
    "consent_rule": "Egg mercy, survival, restoration, and gratitude never set courtship.",
    "history_gate": {
        "devarra.brood.saved_verified": "Set only after a source-bound reader confirms DragonEggsReleased or the completed native egg project.",
        "devarra.brood.lost_verified": "Set only after the native egg outcome is positively confirmed as lost; absence of the saved marker is insufficient.",
        "mutual_exclusion": "The saved and lost scenes each require both their matching positively verified egg outcome and the matching native dialogue cue history; one cannot satisfy the other's entry gate.",
    },
    "egg_outcomes": {
        "saved": "Her own DLC line says the Commander spared her brood and she does not regard the Commander as an enemy; attraction remains unwritten until earned.",
        "destroyed": "Her own DLC line names the pillaged clutch and unborn offspring; this opening allows anger, refusal, and distance without retconning that loss.",
    },
    "path_access": {
        "Trickster": "A bespoke route is proposed here; the fate intervention is unimplemented.",
        "other_nine": "No access or complete route is implemented in this prototype.",
    },
}


def page(id, speaker, text, *choices):
    return n(id, speaker, text, *choices, portrait="Devarra")


SCENE = scene(
    "devarra.trickster.first_answer",
    "The dragon who remembers",
    "Devarra",
    5,
    "arrival",
    [
        page("arrival", "Narrator", '''{n}The Storyteller's tower holds its breath around you. Broken shelves lean over a circular chamber, and a bronze door has been opened just far enough for one huge red claw to rest across the threshold. It could close the gap and crush the latch. Instead, it waits.{/n}

{n}The dragon beyond it is unmistakably Devarra. The old wound beneath her wing has sealed into a dark seam. Her gold eyes travel over your face with the patience of someone choosing where to strike.{/n}

"You came back from the dead once. I have no interest in hearing that you found it charming."''',
            c("Tell her you remember the fight and will not call it a joke.", "own_history"),
            c("Ask whether the Storyteller is forcing her to remain here.", "ask_terms"),
            c("Leave the doorway open and withdraw without demanding an answer.", "leave", flags=("devarra.trickster.closed",))),
        page("own_history", "Commander", '''"I remember the ambush, the fall, and the wound. I also remember what I chose after it. I won't pretend the Trickster made that choice harmless."''',
            c("Acknowledge that her brood's survival purchases no trust.", "saved_brood",
              requires=("devarra.brood.saved_verified", "devarra.native_saved_brood_cue_seen"),
              forbids=("devarra.brood.lost_verified", "devarra.native_lost_clutch_cue_seen")),
            c("Let her name her lost clutch without correcting her.", "lost_brood",
              requires=("devarra.brood.lost_verified", "devarra.native_lost_clutch_cue_seen"),
              forbids=("devarra.brood.saved_verified", "devarra.native_saved_brood_cue_seen")),
            c("Say that she owes you nothing for surviving.", "no_debt")),
        page("ask_terms", "Commander", '''"Are you here because the Storyteller asked you to stand in this room, or because you chose to? I won't make a second conversation out of a command you didn't accept."''',
            c("Wait for her answer without moving closer.", "terms_answer"),
            c("Offer to leave if she would rather not speak.", "leave", flags=("devarra.trickster.closed",))),
        page("terms_answer", "Devarra", '''"He asked. I chose. There is a difference, and if you cannot hear it you will not last long in this room. A dragon can answer an invitation without becoming its keeper's pet."

{n}Her claw shifts against the bronze. The door opens another handspan, then stops.{/n}''',
            c("Accept the distinction and ask what she wants from this meeting.", "question"),
            c("Tell her you have no claim on her time.", "no_debt"),
            c("Leave while the choice is still easy.", "leave", flags=("devarra.trickster.closed",))),
        page("saved_brood", "Commander", '''"I know your brood survived in one history. I remember the mercy you named in the tower. It doesn't mean you have to forgive me, and it doesn't make me entitled to meet you again."''',
            c("Ask what she wants protected now.", "question"),
            c("Offer a practical report about the rescued eggs and accept scrutiny.", "evidence"),
            c("Stop here and let the meeting end on her terms.", "leave", flags=("devarra.trickster.closed",))),
        page("lost_brood", "Commander", '''"I know what you said about the clutch. Your offspring died before they were born. I won't make that sentence smaller to improve my chances with you."''',
            c("Ask whether she wants the truth about what happened recorded in the tower.", "record"),
            c("Say nothing and let her decide whether to continue.", "silence"),
            c("Leave. She owes you no conversation.", "leave", flags=("devarra.trickster.closed",))),
        page("no_debt", "Devarra", '''"Good. Gratitude is a dull chain, and I have worn enough chains for several lifetimes."

{n}Her voice cuts dryly through the chamber. She sounds amused despite herself, then hides the tell in another sharp look.{/n}''',
            c("Ask what she wants you to understand before you speak again.", "question"),
            c("Offer to leave without taking the answer personally.", "leave", flags=("devarra.trickster.closed",))),
        page("question", "Devarra", '''"I want to know whether you can look at a dragon without reducing her to a battlefield, a prize, or a tragedy. You may answer. You may also decide that question is inconvenient."''',
            c("Say that you see an enemy who chose whether to speak again.", "enemy"),
            c("Admit that you don't yet know her beyond the hunt and the tower.", "honesty"),
            c("Call her beautiful and ask whether she will reward your honesty.", "bad_flattery")),
        page("evidence", "Commander", '''"The report says the eggs were moved to safety. I'll show you the seal, the route, and the names of the people who handled them. You can reject the report or inspect it yourself."''',
            c("Compare the seal and dates against the report. Perception DC 26.", flags=("devarra.trickster.opening_perception_attempted",), forbids=("devarra.trickster.opening_perception_attempted",), check=dict(Skill="SkillPerception", DC=26, Success="evidence_verified", Failure="evidence_uncertain", CommanderOnly=True)),
            c("Let Devarra inspect the report and make up her own mind.", "inspect"),
            c("Withhold the report and leave.", "leave", flags=("devarra.trickster.closed",))),
        page("evidence_verified", "Devarra", '''{n}You lay the two pages beside one another. The seal is sound. The dates are not. A courier carried the eggs to safety before the tower's account says the clutch was taken.{/n}

"Someone wanted me to read a lie as though it were mercy. At least you noticed before asking me to be grateful."''',
            c("Give her the papers and let her decide what to do with them.", "inspect"),
            c("Ask who placed the false date, then accept that she may refuse to answer.", "record"),
            c("Claim the discovery means she should trust you.", "hostile", flags=("devarra.trickster.closed",))),
        page("evidence_uncertain", "Devarra", '''{n}The dates blur together. You cannot tell whether the courier arrived before the seizure or after it.{/n}

"Then say you do not know. A clever guess dressed as certainty is still a guess."''',
            c("Admit the record does not answer the question.", "inspect"),
            c("Ask Devarra what evidence she would trust.", "evidence_standard"),
            c("Invent an answer so she will stay.", "hostile", flags=("devarra.trickster.closed",))),
        page("evidence_standard", "Devarra", '''"The names of the hands that carried the eggs. The route they took. A witness whose life was not improved by telling you what you wanted to hear."

{n}Her eye narrows. "You have one chance to bring me that. Do not call it a date."{/n}''',
            c("Agree to look for witnesses without asking for another meeting.", "invitation"),
            c("Decline the errand and leave the conversation here.", "leave", flags=("devarra.trickster.closed",))),
        page("record", "Devarra", '''"The tower is full of people who collect stories and call that the same thing as justice."

{n}She lowers her head until one gold eye is level with yours. The heat against your cheek is not a caress. It is the reminder that she could burn the shelves before you finished a sentence.{/n}

"If you write it down, write the whole thing. The hostage clutch. The bargain. The people who thought eggs were leverage. Do not turn my children into a lesson about your cleverness."''',
            c("Promise an accurate record and name the people responsible where evidence supports it.", "honesty"),
            c("Tell her you will not publish a private grief without her permission.", "silence"),
            c("Argue that a useful story matters more than her preference.", "hostile", flags=("devarra.trickster.closed",))),
        page("silence", "Devarra", '''{n}For a long while, neither of you speaks. Devarra does not mistake your silence for wisdom. You do not mistake her stillness for invitation.{/n}

"That is better than the answer I expected."''',
            c("Ask what she expected.", "honesty"),
            c("Let the quiet be enough for tonight.", "leave", flags=("devarra.trickster.closed",))),
        page("enemy", "Devarra", '''"Then you have learned less than you think. Enemy is a position. It is not a name, and it tells you nothing about what I want now."''',
            c("Accept the correction and ask what she wants now.", "honesty"),
            c("Insist that the hunt settles what you are to each other.", "hostile", flags=("devarra.trickster.closed",))),
        page("honesty", "Devarra", '''"You could have lied more attractively."

{n}The tip of her tail draws a slow line across the dust. Her gaze lingers on your mouth, then returns to your eyes. She does not hide the inspection, and she does not soften it into a promise.{/n}

"I prefer an answer with an edge. We will see whether yours is sharp enough to be useful. You have an irritating mouth, Commander. I have not decided whether I want it silent."''',
            c("Tell her you would like another conversation, if she chooses it.", "invitation"),
            c("Say the look was noticed, but you will not turn it into consent.", "invitation"),
            c("Leave the next step to her.", "leave", flags=("devarra.trickster.closed",))),
        page("inspect", "Devarra", '''{n}She reads the report herself. The dragon's claws press small holes through its corners, but the lines remain legible. When she reaches the names of the druids who carried the eggs, she asks you to repeat each one.{/n}

"If the eggs live, they will owe me nothing either. Do you understand the difference between protecting someone and owning the reason they survived?"''',
            c("Say that protection grants no claim, then ask what she wants done next.", "invitation"),
            c("Admit that you have treated rescue as a debt before.", "honesty"),
            c("Tell her the Commander decides what happens to the eggs.", "hostile", flags=("devarra.trickster.closed",))),
        page("bad_flattery", "Devarra", '''"If you need to be told that a dragon is beautiful, you have not been looking carefully. If you think beauty is a coin you can spend, you have not been listening."

{n}Her nostrils flare. She does not move toward you.{/n}''',
            c("Apologize for trying to turn praise into leverage.", "repair"),
            c("Insist that she misunderstood you.", "hostile", flags=("devarra.trickster.closed",)),
            c("Leave without asking her to reassure you.", "leave", flags=("devarra.trickster.closed",))),
        page("repair", "Devarra", '''"I heard what you meant. The question is whether you can hear what I meant."''',
            c("Agree, without adding an excuse.", "invitation"),
            c("Ask what boundary you should remember.", "silence"),
            c("Tell her she is being unfair.", "hostile", flags=("devarra.trickster.closed",))),
        page("invitation", "Devarra", '''"Perhaps I will speak to you again. That is all I have decided."

{n}Her wing folds across the doorway. It blocks the tower behind her, not the exit behind you.{/n}

"Do not put a romance in my mouth because I let you leave with your head attached. If you return, bring the truth about the eggs, if there is truth to bring. Bring your own answer about the hunt. And leave destiny outside. I like to decide what I want before someone else announces it for me."''',
            c("Accept her terms and leave without asking for a promise.", "end", flags=("devarra.trickster.open",)),
            c("Ask her to choose the next meeting, with no deadline.", "end", flags=("devarra.trickster.open",)),
            c("Try to use Trickster power to make her answer more favorably.", "hostile", flags=("devarra.trickster.closed",))),
        page("hostile", "Devarra", '''{n}The chamber turns white with fire. A wall of harmless ash rises between you and the dragon, marking the distance she has chosen.{/n}

"You were warned. Do not make me repeat myself."''',
            c("Leave and accept that this route is closed.", "end", flags=("devarra.trickster.closed",))),
        page("leave", "Narrator", '''{n}You step away from the bronze door. Devarra does not follow, and the tower does not bend the space to bring you back together.{/n}

{n}Her brood's history remains hers. You came to the Tower because the native story brought you both here; any later private conversation would still require her answer.{/n}''',
            c("End the meeting.", "end")),
        page("end", "Narrator", '''{n}The next move is not written in the dust. You leave the room without taking Devarra's silence, anger, or interest as a promise.{/n}'''),
    ],
    requires=("trickster", "devarra.actor_confirmed", "devarra.history_read"),
    RequiresAnyGroups=[
        ("devarra.brood.saved_verified", "devarra.brood.lost_verified"),
        ("devarra.native_saved_brood_cue_seen", "devarra.native_lost_clutch_cue_seen"),
    ],
    forbids=("devarra.trickster.closed", "devarra.trickster.open"),
    delay=0,
    last=5,
    optional=True,
    Relationship="devarra.trickster",
    ManualOnly=True,
    Remote=False,
    PhysicalPresenceRequired=True,
    ContactUnit="Devarra",
)

def outcome_scene(name, egg_flag, cue_flag, opposite_egg_flag, opposite_cue_flag):
    variant = deepcopy(SCENE)
    variant["Id"] = "devarra.trickster." + name
    variant["Requires"].extend((egg_flag, cue_flag))
    variant.pop("RequiresAnyGroups", None)
    variant["Forbids"].extend((opposite_egg_flag, opposite_cue_flag))
    return variant


SAVED_SCENE = outcome_scene(
    "saved_brood",
    "devarra.brood.saved_verified",
    "devarra.native_saved_brood_cue_seen",
    "devarra.brood.lost_verified",
    "devarra.native_lost_clutch_cue_seen",
)
LOST_SCENE = outcome_scene(
    "lost_clutch",
    "devarra.brood.lost_verified",
    "devarra.native_lost_clutch_cue_seen",
    "devarra.brood.saved_verified",
    "devarra.native_saved_brood_cue_seen",
)
SCENES = [SAVED_SCENE, LOST_SCENE]


if __name__ == "__main__":
    from collections import deque

    for current_scene in SCENES:
        nodes = {node["Id"]: node for node in current_scene["Nodes"]}
        assert len(nodes) == len(current_scene["Nodes"])
        reached = {current_scene["Entry"]}
        queue = deque(reached)
        while queue:
            current = queue.popleft()
            for choice in nodes[current]["Choices"]:
                check = choice.get("Check") or {}
                targets = [choice["Next"], check.get("Success"), check.get("Failure")]
                for target in targets:
                    if target is not None and target not in reached:
                        assert target in nodes, (current, target)
                        reached.add(target)
                        queue.append(target)
        assert len(reached) == len(nodes), sorted(set(nodes) - reached)
        assert all(node["Text"].count("{n}") == node["Text"].count("{/n}") for node in nodes.values())
        print(f"{current_scene['Id']}: {len(nodes)} reachable nodes")
    saved_pair = {"devarra.brood.saved_verified", "devarra.native_saved_brood_cue_seen"}
    lost_pair = {"devarra.brood.lost_verified", "devarra.native_lost_clutch_cue_seen"}
    assert saved_pair.issubset(SAVED_SCENE["Requires"]) and lost_pair.issubset(SAVED_SCENE["Forbids"])
    assert lost_pair.issubset(LOST_SCENE["Requires"]) and saved_pair.issubset(LOST_SCENE["Forbids"])
    assert "RequiresAnyGroups" not in SAVED_SCENE and "RequiresAnyGroups" not in LOST_SCENE
    own_history_choices = [choice for choice in SCENE["Nodes"] if choice["Id"] == "own_history"][0]["Choices"]
    assert saved_pair.issubset(own_history_choices[0]["Requires"]) and lost_pair.issubset(own_history_choices[0]["Forbids"])
    assert lost_pair.issubset(own_history_choices[1]["Requires"]) and saved_pair.issubset(own_history_choices[1]["Forbids"])
