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

# eng7-f6d begin: no new actor or jealousy history is granted by this adapter.
HUB = "wenduag.vellexia_network.presence"
PRESENCES = {HUB: dict(Unit=WENDUAG_UNIT, Area=VELLEXIA_MANOR, Mode="reuse-native",
    Requires=[RECEPTION_HISTORY], Forbids=list(RELATIONSHIP["UnavailableFlags"]),
    MinChapter=4, MaxChapter=4, AnswerLists=[], Dialog="hub")}
# eng7-f6d end
SCENES = [scene(
    "wenduag.vellexia_network.reception",
    "A useful sort of jealousy",
    "Wenduag",
    4,
    "[Recall Wenduag's jealousy at Vellexia's reception]",
    [
        n("start", "Narrator", '''{n}The reception is thinning. Wenduag watches Vellexia dismiss a guest with a touch to his cheek. He tries to kiss her hand; she pulls it away without looking at him.{/n} "Look at him. Still wagging his tail." {n}Wenduag bares her teeth.{/n} "I watched you like that once. Tonight I\'m watching her. I want to see what she does when someone bites back."''',
          c('"You want to fight her?"', "terms"),
          c('"Leave it, Wenduag."', "close")),
        n("terms", "Wenduag", '''"I could walk over and show her my teeth. Half this room would come to watch." {n}She turns her cup between her fingers.{/n} "I\'d rather catch her without the audience. She can tell me to piss off. Then I\'ll know she hasn\'t got anything better to offer."''',
          c('"What do you want from her?"', "her_terms"),
          c('"Then keep away from her tonight."', "close")),
        n("her_terms", "Wenduag", '''"I want to know whether she\'s quick when nobody\'s applauding." {n}Wenduag\'s gaze follows Vellexia\'s hands.{/n} "And I want her looking at me when she answers. You\'re not the only thing in this room worth wanting."''',
          c('[Approach Vellexia.] "A word away from the music, Vellexia."', "invite", flags=("wenduag.vellexia_network.started",)),
          c('"Get her attention yourself."', "wenduag_leads"),
          c('"Leave her out of it."', "close")),
        n("wenduag_leads", "Wenduag", '''{n}Wenduag laughs into her cup.{/n} "Fine. I\'ll get her attention myself." {n}She watches a fresh crowd close around Vellexia.{/n} "Not while those little dogs are yapping. I\'ve had enough of waiting for scraps."''',
          c('[Leave her watching the reception.]', flags=("wenduag.vellexia_network.started",)),
          c('"Enough of this."', "close")),
        n("invite", "Narrator", '''{n}Vellexia sees Wenduag at your shoulder. Her gaze travels slowly over the hunter\'s hands.{/n} "You brought teeth to my reception. Are they for display?" {n}Wenduag sets down her cup.{/n} "Come out of the crowd and find out."''',
          c('"And what do you say, Vellexia?"', "vellexia_answer"),
          c('"Another time."', "close")),
        n("vellexia_answer", "Vellexia", '''"The alcove, perhaps. I can hear the musicians from there, but not my guests." {n}Vellexia touches the stem of her glass without lifting it.{/n} "Tell me, little huntress: do you always need an audience to make a kill?"''',
          c('"Come with us."', "vellexia_accepts"),
          c('[Wait for her answer.]', "vellexia_declines", flags=("wenduag.vellexia_network.closed",)),
          c('[Leave them to answer each other.]', "privacy")),
        n("vellexia_accepts", "Vellexia", '''"Yes, come. Both of you. I have heard quite enough about the crusade\'s supply carts." {n}Vellexia hooks a finger through Wenduag\'s empty cup and carries it into the alcove.{/n} "You may have this back when you tell me something worth drinking to."''',
          c('[Follow her into the alcove.]', "conversation", flags=("wenduag.vellexia_network.conversation_accepted",)),
          c('[Leave the two women together.]', "privacy")),
        n("conversation", "Narrator", '''{n}Vellexia asks how Wenduag would make hungry hunters eat from a stranger\'s hand. Wenduag\'s smile thins.{/n} "A knife behind them. Meat in front." {n}Vellexia laughs.{/n} "And here you are, watching my hands. How attentive." {n}Wenduag leans nearer.{/n} "I\'m watching where you hide the knife."''',
          c('[Return to the reception.]')),
        n("privacy", "Narrator", '''{n}Behind you, Vellexia\'s laugh rises over the music. Wenduag answers too softly to hear. When she rejoins you, she has her cup back and a fresh scratch across one knuckle.{/n} "She wanted to know why I carry a knife at a reception. I asked why she didn\'t need one." {n}Her grin shows all her teeth.{/n} "Go on. Guess which answer she liked."''',
          c('"Keep your secrets, then."')),
        n("vellexia_declines", "Vellexia", '''"No. I\'ve already been menaced by three pretty creatures tonight. One had better claws." {n}Vellexia turns her back on Wenduag and beckons another guest.{/n} "Your huntress may wait outside. I have better company."''',
          c('[Leave her to the next guest.]', flags=("wenduag.vellexia_network.closed",))),
        n("close", "Wenduag", '''{n}Wenduag sets her cup down hard enough to crack its stem.{/n} "Enough, then." {n}She watches Vellexia greet someone else, then turns toward the door.{/n} "Come on. Something outside this house must still have a throat worth cutting."''',
          c('[Leave the reception.]', flags=("wenduag.vellexia_network.closed",))),
    ],
    requires=(RECEPTION_HISTORY,),
    forbids=("wenduag.vellexia_network.closed", "wenduag.dead", "vellexia.dead", "vellexia.early_fight", "vellexia.final_fight"),
    delay=0,
    last=4,
    optional=True,
    Relationship="wenduag.vellexia_network",
    ContactUnit=WENDUAG_UNIT, InteractionHub=HUB,  # eng7-f6d
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


# eng7-f6d: only the dormant contact contract; no production registration.
def integrate(payload):
    from copy import deepcopy
    payload.setdefault("Presences", {}).update(deepcopy(PRESENCES))
