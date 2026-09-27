"""An unregistered authored interlude connecting Wenduag and Vellexia.

The native Vellexia reception and Wenduag's jealousy are continuity anchors.
This draft adds an invitation to explore, not a claim that either woman already
desires the other or has agreed to a triad.
"""
from story_format import c, n, scene


PATH_ACCESS = {
    "angel": "Unresolved: no source-backed cross-path contact producer audited.",
    "aeon": "Unresolved: no source-backed cross-path contact producer audited.",
    "azata": "Unresolved: no proof that the reception contact is available on this path.",
    "demon": "Unresolved: no source-backed cross-path contact producer audited.",
    "devil": "Unresolved: no source-backed cross-path contact producer audited.",
    "gold_dragon": "Unresolved: no source-backed cross-path contact producer audited.",
    "legend": "Unresolved: no source-backed cross-path contact producer audited.",
    "lich": "Unresolved: no source-backed cross-path contact producer audited.",
    "swarm": "Unresolved: survival, identity, and contact are not established.",
    "trickster": "Authored proposal only: the reception is a plausible shared contact, but the Trickster route adapter and all-state reachability are not implemented.",
}

RELATIONSHIP = dict(
    Title="A useful sort of jealousy",
    Description="Wenduag proposes a careful introduction to Vellexia; each woman decides for herself whether to continue.",
    Objective="Hear Wenduag's proposal and decide whether to invite Vellexia into the conversation",
    Guidance="Draft interlude following Wenduag's documented jealousy at Vellexia's reception. A producer must verify native history and both current actors before delivery. No path is registered by this file.",
    StartedFlag="wenduag.vellexia_network.started",
    ClosedFlag="wenduag.vellexia_network.closed",
    CommittedFlag="wenduag.vellexia_network.relationship_chosen",
    UnavailableFlags=["wenduag.dead", "vellexia.dead"],
    FailureFlags=[],
)

WENDUAG_UNIT = "ae766624c03058440a036de90a7f2009"
VELLEXIA_UNIT = "a32a07903e428d34cb0e98a804d40569"
VELLEXIA_MANOR = "8217b05e37078414981d994151f0ffb1"
RECEPTION_HISTORY = "wenduag.vellexia_network.reception_history_verified"

# The authored contact requires a producer which does not yet exist. It must
# observe the native unlockable flag and confirm both original units can be
# contacted in the manor before it exposes this scene.
PRODUCER_CONTRACT = {
    RECEPTION_HISTORY: {
        "native_unlockable_flag": "23cacf7a07480da459b3a59d0fd6da82",
        "native_flag_name": "WenduagRomance_VelexiaConflict_flag",
        "required_current_contacts": (WENDUAG_UNIT, VELLEXIA_UNIT),
        "required_area": VELLEXIA_MANOR,
        "implemented": False,
    },
}

SCENES = [scene(
    "wenduag.vellexia_network.reception",
    "A useful sort of jealousy",
    "Wenduag",
    4,
    "[Recall Wenduag's jealousy at Vellexia's reception]",
    [
        n("start", "Narrator", '''{n}The reception has thinned enough that the music no longer hides every conversation. Wenduag watches Vellexia across the room, her spider legs held close and still. She notices you noticing.{/n}
"You remember that night," she says. "I was jealous. I told myself it was because she could take your attention away from me. That was true. It was not the whole truth."
Her mouth tilts, amused at her own admission rather than softened by it.
"She knew exactly how much the room was watching her, and she never once asked it to approve. I wanted to know whether that was courage, vanity, or simply another kind of weapon."''',
          c('Ask whether she wants to meet Vellexia as a rival or as a possible equal.', "terms"),
          c('Tell Wenduag you are not interested in turning jealousy into a contest.', "close")),
        n("terms", "Wenduag", '''"A rival is useful. An equal is dangerous. A lover might be either, if she chose it." Wenduag studies your face, waiting to see if you will mistake the answer for a promise.
"I am not asking you to arrange her for me. I am asking whether you want me to make an introduction. I can speak to her about the reception, the paintings, or the fact that she can unsettle a room without raising her voice. Then I can leave the two of you to decide whether there is anything worth continuing."
She taps one claw lightly against her cup.
"If she says no, I will not ask twice. If I decide I dislike the answer, that will be my problem to own."''',
          c('Ask Wenduag what she wants from the introduction before you answer.', "her_terms"),
          c('Decline. You will not make Vellexia part of a test.', "close")),
        n("her_terms", "Wenduag", '''"A look at how she thinks when no audience is rewarding her. A chance to see whether her composure survives a question she did not choose." Her eyes narrow with frank appetite for the contest, but she does not dress it up as tenderness.
"And perhaps the pleasure of discovering that she can surprise me. That is all I know. I will not pretend attraction because you might enjoy the arrangement."
There is no softness in the admission, but there is care in its precision: Wenduag is giving you her actual motive before you involve anyone else.
"You can still say no. I will be disappointed, not obediently grateful."''',
          c('Agree to ask Vellexia whether she wants a private conversation with both of you.', "invite", flags=("wenduag.vellexia_network.started",)),
          c('Tell Wenduag to approach Vellexia herself, without using you as a prize.', "wenduag_leads"),
          c('Decline and leave Vellexia out of it.', "close")),
        n("wenduag_leads", "Wenduag", '''Wenduag's laugh is low and pleased. "Better. If I want her attention, I should be able to earn it without hiding behind yours."
She considers the room, then shakes her head. "Not tonight. The reception is still a stage, and I have no wish to confuse an audience's interest with hers. I will speak to her another time if there is a real reason. You have not promised me anything, and I will not claim that you did."''',
          c('Leave the possibility open without making a promise.', flags=("wenduag.vellexia_network.started",)),
          c('Close the subject.', "close")),
        n("invite", "Narrator", '''{n}You approach Vellexia with Wenduag beside you, but stop before speaking for either of them.{/n}
"Wenduag would like to ask you a question about the way you held the room tonight," you say. "I would like to join the conversation if you want that. This is an invitation, not a request for a favor, and you can refuse without explanation."
Vellexia's gaze moves from you to Wenduag. "An unusually careful opening. Did you write it together?"
"No," Wenduag says. "I chose to come. The Commander chose to ask. You choose what happens next."''',
          c('Let Vellexia answer without filling the silence.', "vellexia_answer"),
          c('Withdraw the invitation and leave her evening undisturbed.', "close")),
        n("vellexia_answer", "Vellexia", '''"You asked me directly, which I appreciate," Vellexia says. "I have not agreed to anything beyond hearing the invitation."
Wenduag's smile shows one sharp edge. "I would be disappointed if you made it easy."
"Then let me make my own answer." Vellexia studies both of you, and the room stays quiet long enough for her to choose without being hurried.
No one has agreed to romance, touch, or a shared arrangement. The question is only whether she wants one conversation.''',
          c('Ask if Vellexia wants one conversation, with no expectation beyond that.', "vellexia_accepts"),
          c('Give Vellexia space to decline the conversation.', "vellexia_declines", flags=("wenduag.vellexia_network.closed",)),
          c('Leave the invitation unanswered and give them privacy.', "privacy")),
        n("vellexia_accepts", "Vellexia", '''Vellexia gives a small, deliberate nod. "Yes. I will stay for one conversation. I am curious, and that is my reason. It is not a promise of another meeting, much less anything physical."
Wenduag's expression sharpens with interest, but she does not move until Vellexia turns toward the alcove.
"Then let us begin with the question I actually wanted to ask," Wenduag says. "How do you make a room full of people think you owe them nothing?"
Vellexia's smile is slight. "Practice. And the occasional reminder that attention is not ownership."''',
          c('Thank her and join the brief conversation.', "conversation", flags=("wenduag.vellexia_network.conversation_accepted",)),
          c('Thank her and let the evening end here.', "privacy")),
        n("conversation", "Narrator", '''{n}Vellexia asks Wenduag whether she believes every display of power is meant to command an audience. Wenduag answers that a display is useful only if someone changes their behavior after seeing it.{/n}
"And what behavior did mine change?" Vellexia asks.
"I watched you more carefully," Wenduag replies. "I have not decided what that means."
Vellexia's amusement deepens, though her answer stays measured. "That is a better beginning than certainty. I may be willing to speak again, provided neither of you arrives believing the next conversation is owed."
Wenduag accepts the condition without surrendering her pride. "Then let the next one be earned."''',
          c('End the evening here without asking either woman for a next step.')),
        n("privacy", "Narrator", '''{n}You leave them with the alcove and the right to end the conversation. When you see Wenduag again, she does not report Vellexia's private answer. She says only that she will decide whether to ask for another conversation, and Vellexia will decide whether to accept.{/n}
"No secret agreement, then?" you ask.
"No agreement you are entitled to hear," Wenduag replies. "If there is another step, the three of us can name it together. If there is not, you will not turn one polite conversation into a story about us."''',
          c('Respect their privacy and leave the invitation unanswered.')),
        n("vellexia_declines", "Vellexia", '''"No," Vellexia says, without making the word cruel. "I will not turn this evening into an experiment in whether you can make me curious. I accept the invitation as a compliment, and decline the conversation."
Wenduag's expression tightens for a breath, then settles. "Understood."
"Thank you for asking me directly," Vellexia adds. "Please do not ask again unless I bring it up myself."
You leave her to the reception. Wenduag does not seek another answer from her tonight, and neither of you recasts this refusal as a challenge to overcome.''',
          c("Respect Vellexia's refusal and leave the subject closed.", flags=("wenduag.vellexia_network.closed",))),
        n("close", "Wenduag", '''Wenduag studies you for a moment, then inclines her head. "Good. I wanted an answer, not permission to ignore one."
She returns her attention to the room. Her jealousy has been acknowledged, but it has not been converted into entitlement, and Vellexia has not been made responsible for soothing it.
"Come," she says. "There are better uses for a night than arranging people like trophies."''',
          c('Leave the subject closed.', flags=("wenduag.vellexia_network.closed",))),
    ],
    requires=(RECEPTION_HISTORY,),
    forbids=("wenduag.vellexia_network.closed", "wenduag.dead", "vellexia.dead", "vellexia.early_fight", "vellexia.final_fight"),
    delay=0,
    last=4,
    optional=True,
    Relationship="wenduag.vellexia_network",
    ContactUnit=WENDUAG_UNIT,
    AdditionalContactUnits=[VELLEXIA_UNIT],
    Chapters=[4],
    Areas=[VELLEXIA_MANOR],
    ManualOnly=True,
)]


if __name__ == "__main__":
    assert len(PATH_ACCESS) == 10
    assert {"angel", "aeon", "azata", "demon", "devil", "gold_dragon", "legend", "lich", "swarm", "trickster"} == set(PATH_ACCESS)
    assert len(SCENES) == 1 and len(SCENES[0]["Nodes"]) == 11
    assert SCENES[0]["ContactUnit"] == WENDUAG_UNIT and len(WENDUAG_UNIT) == 32
    assert SCENES[0]["AdditionalContactUnits"] == [VELLEXIA_UNIT]
    assert not PRODUCER_CONTRACT[RECEPTION_HISTORY]["implemented"]
    ids = {node["Id"] for node in SCENES[0]["Nodes"]}
    targets = [choice["Next"] for node in SCENES[0]["Nodes"] for choice in node["Choices"] if choice.get("Next")]
    flags = {flag for node in SCENES[0]["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
    assert all(target in ids for target in targets)
    assert SCENES[0]["Nodes"][6]["Id"] == "vellexia_accepts"
    assert "wenduag.vellexia_network.conversation_accepted" in flags
    assert RELATIONSHIP["CommittedFlag"] not in flags
    assert "wenduag.vellexia_network.followup_possible" not in flags
