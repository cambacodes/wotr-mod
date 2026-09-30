"""Yaniel's authored final Drezen meeting before joining Targona's Abyss journey."""

from story_format import c, n, scene
from storylines.yaniel_route_opening import SCENES as OPENING_SCENES


REQUIRES = (
    "yaniel.genuine_midnight_fane_rescue_witness",
    "yaniel.radiance_recognition_witnessed",
    "yaniel.confirmed_alive_and_unbound_at_contact",
    "yaniel.contact_invitation_authored_by_yaniel",
    "yaniel.opening.complete",
    "yaniel.opening.future_invitation_possible",
)
FORBIDS = (
    "yaniel.fake_yaniel_branch_without_genuine_rescue_witness",
    "yaniel.dead",
    "yaniel.contact_refused",
    "yaniel.identity_or_agency_lost",
    "yaniel.opening.friendship",
    "yaniel.opening.closed_friendly",
    "yaniel.opening.closed_hostile",
)

FOLLOWUP = scene(
    "yaniel.departure.before_abyss",
    "Before the road into the Abyss",
    "Yaniel",
    3,
    "Meet Yaniel before she leaves with Targona",
    [
        n("opening", "Narrator", '''{n}The next note arrives the morning after your first meeting. Yaniel says she has asked Targona to take her into the Abyss. She will leave Drezen today. Before the road opens, she wants one more conversation. This short pre-departure window follows her native account of spending a day in Drezen before choosing to go with Targona; the note, timing and meeting remain authored additions.{/n}
"Yesterday I thought I might stay. I was wrong. There is work below that I cannot leave to others. If you still want to know me, meet me by the east gate before we depart. I promise no more than the time it takes to speak plainly."''',
            c("Meet her, and let her decide what this parting means.", "table", flags=("yaniel.departure.attended",)),
            c("Decline kindly and let her take the road she chose.", "decline", flags=("yaniel.departure.declined",))),
        n("decline", "Yaniel", '''"Thank you for telling me plainly." Her reply is warm, though the ink is spare. "I will not ask why. If I want to invite you again, I will. If you change your mind, the same courtesy applies." No follow-up is scheduled for either of you.''',
            c("Keep the relationship at the distance she offered.", flags=("yaniel.departure.closed",), abort=True)),
        n("table", "Narrator", '''{n}At the east gate, Yaniel checks the fastening on her travel cloak. Her hair is tied back for the road. Silver threads it; fine lines crease her smile; her attentive face gives nothing away for free. Radiance rests within reach, not in her hand. Targona waits beside a pack mule, giving the two of you space while she checks the straps.{/n}
Yaniel hands you a piece of dark bread wrapped in cloth. "I was told there would be a proper meal before we left. The crusade has mistaken a crust for one." Her mouth quirks. "It is still better than an empty stomach. I hoped you would come. Do not make me explain why before breakfast."''',
            c("Ask what she does when no one asks her to represent the past.", "ordinary_life"),
            c("Tell her about a choice you regret, without asking to be absolved.", "honesty"),
            c("Ask whether she has regretted sending the invitation.", "invitation"),
            c("Praise the legendary woman the stories describe.", "legend")),
        n("legend", "Yaniel", '''Her hand stills on the pack strap. "The legends are useful when a commander needs people to stand in a line. They are less useful across a table." She is not angry, but she watches whether you defend the compliment.
"If you want to flatter me, tell me what you noticed today. If you want to know me, ask something whose answer might surprise you." She tightens the pack strap and waits. The road is still hers to take or delay.''',
            c("Apologize, then ask what she wants from the years she has now.", "ordinary_life", flags=("yaniel.departure.corrected_course",)),
            c("Say you meant the compliment and keep praising the legend.", "end_early", flags=("yaniel.departure.missed_her",))),
        n("end_early", "Narrator", '''{n}Yaniel goes quiet. "You are speaking to the woman standing here, not the statue other people made of her." She lets the silence stand, then turns toward Targona. There is no punishment or dramatic accusation. She simply does not offer another private meeting.{/n}''',
            c("Accept her decision and leave without following.", flags=("yaniel.departure.ended",), abort=True)),
        n("ordinary_life", "Yaniel", '''She tells you she has started with small choices: what to eat, how long to sleep, whether to practice with Radiance or leave it in its stand. She walks the rebuilt walls at dawn, not to inspect them, but because the city sounds different before the soldiers wake. Some days she reads dispatches. Some days she puts them aside and lets another person answer.
"I still want to be useful. I do not want usefulness to be the price of keeping my place in the world." She asks whether you understand the difference. "You need not agree. I would rather hear your thought than a polished answer designed to keep me at this table."''',
            c("Use Knowledge (World) to ask about one remembered name without treating memory as proof. DC 24.", check=dict(Skill="SkillKnowledgeWorld", DC=24, Success="name_success", Failure="name_failure", CommanderOnly=True)),
            c("Ask what kind of quiet she enjoys now.", "quiet"),
            c("Offer her a campaign role before asking whether she wants one.", "unasked_role")),
        n("name_success", "Yaniel", '''You name a person from an old dispatch and ask whether the detail is hers to share. Yaniel corrects one date, then laughs when you catch why the record was wrong: the clerk copied an order after the patrol changed its route. She tells you about the woman who carried the message, including a joke that never made it into the official account.
"That is what I miss. Not being young. Being in the middle of something that had not yet been reduced to a report." She is pleased that you noticed the error without claiming to solve her memory for her.''',
            c("Ask what you could do together that has no strategic purpose.", "shared_evening", flags=("yaniel.departure.listened_well",))),
        n("name_failure", "Yaniel", '''You reach for the date and get it wrong. Yaniel catches the error at once. "That dispatch was copied after the order changed." She gives you the correction without ridicule.
"It is all right to miss a detail. What matters is whether you keep listening when I correct you." She does not reward the check with confidence. She does leave room for an honest conversation.''',
            c("Thank her and ask what you could do together without a campaign purpose.", "shared_evening", flags=("yaniel.departure.accepted_correction",)),
            c("Defend your guess as close enough.", "defensive", flags=("yaniel.departure.defended_guess",))),
        n("defensive", "Yaniel", '''"A wrong answer is not a crime. Protecting it from correction is a choice." She is not cruel, but her interest cools. You can apologize and continue the walk, or part here.''',
            c("Apologize without asking her to reassure you.", "shared_evening", flags=("yaniel.departure.repaired",)),
            c("Part here without demanding another chance.", "end_early", flags=("yaniel.departure.ended",))),
        n("honesty", "Yaniel", '''You tell her what you regret and name the harm plainly. You do not ask whether that makes you a good person. She asks what you would do differently if the same choice appeared tomorrow, then challenges the part of your answer that sounds convenient.
"I hear you. But remorse cannot command what I feel next." Her expression softens after the hard edge has done its work.''',
            c("Ask what she herself regrets, and accept if she declines to answer.", "regret"),
            c("Thank her for the question and return to easier talk.", "quiet")),
        n("regret", "Yaniel", '''She talks about a patrol she once led too far from support. She names the companions who made the decision with her, the order she misunderstood, and the people who paid for the delay. Her regret has lasted. It has not made her incapable of choosing another risk.
"I can remember failure without making it the only true thing about me." She watches for pity. When it does not arrive, she nods once. The silence feels earned, not empty.''',
            c("Admire how she owns the choice without surrendering her life to it.", "shared_evening", flags=("yaniel.departure.shared_regret",)),
            c("Promise that you will make sure she never has to lead again.", "unasked_role")),
        n("unasked_role", "Yaniel", '''"You have mistaken concern for authority. I have not asked to be put on the shelf, restored to command, or handed a cause. You can offer work when I ask what is available. My risks remain mine to choose."
She asks whether you can sit with the correction without making her manage your embarrassment.''',
            c("Accept the correction and ask what she wants without proposing an answer.", "quiet", flags=("yaniel.departure.heard_correction",)),
            c("Say she should be grateful someone is protecting her.", "end_early", flags=("yaniel.departure.protection_overstep",))),
        n("invitation", "Yaniel", '''"I did, briefly. Then I remembered curiosity is not a vow. I am allowed to change my mind. So are you." She leans back, looking at you without the armor of a paladin's inspection.
"I was curious whether you could speak with me without asking what my survival means. So far, you have managed often enough." Her mouth turns toward a smile. "That is praise. Do not make me repeat it."''',
            c("Ask whether she wants to continue seeing you, while making refusal easy.", "desire"),
            c("Say you are content to let the conversation stand on its own.", "quiet")),
        n("quiet", "Yaniel", '''The talk turns to weather, old songs, and the absurdity of soldiers trying to march in rhythm. You disagree over a tune. Neither of you pretends to yield. Targona finishes the last strap and waits by the gate.
Yaniel says, "I would like to know you better. That does not yet tell either of us what we are. I want to find out without an audience, a prophecy, or the thought that my survival has decided it for me."''',
            c("Tell her you would like that too, and ask before offering your hand.", "hand", flags=("yaniel.departure.third_meeting_possible",)),
            c("Say you prefer friendship and do not soften the answer.", "friendship", flags=("yaniel.departure.friendship",)),
            c("Thank her and leave the next choice with her.", "friendship", flags=("yaniel.departure.deferred",))),
        n("shared_evening", "Yaniel", '''The conversation turns to what she wants now. She likes that you listen and still disagree. Her gaze lingers on your hands, then returns to your face, as if testing whether you can meet desire without turning it into a claim.
"I have spent a long time learning what I can bear. I would like to remember what I enjoy. That may include you. It does not give you leave to guess the next step." She asks for another evening, with no promise that courtship will become a relationship.''',
            c("Accept, and ask if she would like to hold your hand before you part.", "hand", flags=("yaniel.departure.third_meeting_possible",)),
            c("Tell her you want her, but accept that tonight ends here.", "desire", flags=("yaniel.departure.desire_stated",)),
            c("Say the desire is not mutual and end courtship kindly.", "friendship", flags=("yaniel.departure.friendship",))),
        n("desire", "Yaniel", '''Yaniel studies your face as if weighing a difficult order. "I am not afraid of desire. I am careful of being made into an answer." She rests one hand on the gatepost. "I want to see what this is. I do not know what I will want after that." Her choice to continue is not a claim on either of you.''',
            c("Say that is enough for this morning, and ask whether a hand would be welcome.", "hand", flags=("yaniel.departure.third_meeting_possible",)),
            c("Thank her and leave without asking for touch.", "friendship", flags=("yaniel.departure.deferred",))),
        n("hand", "Yaniel", '''She answers by offering her hand. The contact is warm, direct, and brief. Her thumb passes over your knuckles, carrying more heat than the formal greeting in the Fane ever could.
"I have missed touching someone because I wanted to, not because the moment required a gesture." She lets go first. "That was mine to choose. I am glad you asked." Neither of you mistakes the touch for permission to take more.''',
            c("Ask whether you may kiss her, then wait for her answer.", "kiss_question", flags=("yaniel.departure.hand_consented",)),
            c("Leave the hand as the only touch before the journey.", "ending", flags=("yaniel.departure.hand_consented",)),
            c("Say you would rather not touch after all.", "ending", flags=("yaniel.departure.touch_declined",))),
        n("kiss_question", "Yaniel", '''"Yes, if you still want to." She says it plainly, without turning permission into a performance. When you meet her, she kisses you with a controlled patience that warms as she decides to stay. Her hand settles at your collar, not pulling you closer until you answer with your own movement. The kiss is adult, unhurried, and chosen by both of you.
After a moment she breaks it herself. Her breath catches; she smiles at the evidence. "I remember more than I thought." She straightens your collar with two fingers. "That is enough for this morning. If we continue, let us ask before we guess. That much courtesy is owed between us."''',
            c("Agree and leave together at an ordinary pace.", "ending", flags=("yaniel.departure.kiss_consented",)),
            c("Ask to travel with her, then accept her answer without argument.", "travel_invitation", flags=("yaniel.departure.kiss_consented",))),
        n("travel_invitation", "Yaniel", '''"I would like you beside us, if you can bear the road and the work waiting below. I do not ask you to command me there." Desire warms the invitation; it does not turn it into an order.
Targona waits without interrupting. Yaniel has already chosen her road. You are being asked whether you will share it, not whether you will permit her to go.''',
            c("Ask whether she wants you as companion and accept her answer.", "road_choice", flags=("yaniel.departure.travel_question_asked",))),
        n("friendship", "Yaniel", '''"Thank you for saying so directly. I would rather have a clear friendship than courtship performed out of pity or obligation." She turns toward Targona, and you part without a kiss or a promise that one will follow.''',
            c("End as friends, if she still wants the friendship.", flags=("yaniel.departure.friendship",), abort=True)),
        n("ending", "Narrator", '''{n}Targona calls that the road is ready. Yaniel takes Radiance from where she set it and turns to you. She will go into the Abyss, whether or not you come. What remains undecided is whether the two of you will see one another again.{/n}''',
            c("Ask to accompany Yaniel and Targona as a companion, not her commander.", "road_choice", flags=("yaniel.departure.travel_question_asked",)),
            c("Wish her a safe road and remain in Drezen.", "parting", flags=("yaniel.departure.parting_chosen",))),
        n("road_choice", "Yaniel", '''Yaniel considers the request, then looks to Targona. The angel does not answer for her. "You may come, if you understand that I am choosing my road. I will not be ordered back, and I will not be made into a prize for following me." She holds your gaze. The risk and the work are real; an invitation is not a promise that the Abyss will welcome you.''',
            c("Accept her terms and join their journey.", "travel_together", flags=("yaniel.departure.travelling_together",)),
            c("Decide the road is not yours and stay in Drezen.", "parting", flags=("yaniel.departure.parting_chosen",))),
        n("travel_together", "Narrator", '''{n}You fall into step beside Yaniel and Targona. The journey is hers to undertake, not a campaign you have been asked to command. At the threshold, Yaniel offers you her hand. "Come, then. We have miles before any of us needs to decide what to call this."{/n}
This authored departure gives the relationship a continuing situation; it does not prove how the Abyss journey works on every mythic path or that the required actors can be scheduled there.''',
            c("Take her hand and go with them.", flags=("yaniel.departure.travel_started", "yaniel.departure.complete"))),
        n("parting", "Narrator", '''{n}Yaniel gives you a small, private smile before she turns toward Targona. She does not ask you to follow or promise that a letter will arrive. The gate opens, and she leaves Drezen because she chose to go.{/n}
The courtship may continue only if a later, authored contact is produced. This is an ending to the Drezen opening, not a resolution of their relationship.''',
            c("Let her go, with no pursuit assumed.", flags=("yaniel.departure.complete",))),
    ],
    requires=REQUIRES,
    forbids=FORBIDS,
    delay=12,
    optional=True,
    PhysicalPresenceRequired=True,
    ActorContract="yaniel.genuine_surviving_unbound_actor_unverified",
    AreaContract="yaniel.drezen_departure_gate_unverified",
    Relationship="yaniel.opening",
    ContactContract="yaniel.invitation_from_yaniel_unverified",
)

SCENES = [FOLLOWUP]


def _validate_scene():
    nodes = {node["Id"]: node for node in FOLLOWUP["Nodes"]}
    assert len(nodes) == len(FOLLOWUP["Nodes"]), "duplicate Yaniel departure node"
    assert FOLLOWUP["Entry"] == "Meet Yaniel before she leaves with Targona"
    assert OPENING_SCENES[0]["DelayHours"] == 4
    assert FOLLOWUP["DelayHours"] == 12
    assert OPENING_SCENES[0]["DelayHours"] + FOLLOWUP["DelayHours"] < 24
    assert "opening" in nodes
    reachable = set()
    pending = ["opening"]
    while pending:
        node_id = pending.pop()
        if node_id in reachable:
            continue
        reachable.add(node_id)
        for choice in nodes[node_id]["Choices"]:
            check = choice.get("Check") or {}
            for target in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                if target:
                    assert target in nodes, f"dangling target {target} from {node_id}"
                    pending.append(target)
    assert reachable == set(nodes), f"unreachable Yaniel nodes: {set(nodes) - reachable}"
    assert "yaniel.opening.future_invitation_possible" in FOLLOWUP["Requires"]
    assert "yaniel.opening.friendship" in FOLLOWUP["Forbids"]
    assert sum(bool(choice.get("Check")) for node in nodes.values() for choice in node["Choices"]) == 1
    assert any("yaniel.departure.kiss_consented" in choice["Set"] for node in nodes.values() for choice in node["Choices"])


_validate_scene()


if __name__ == "__main__":
    print(f"1 unregistered scene; {len(FOLLOWUP['Nodes'])} nodes; unique targets and authored route gates valid")
