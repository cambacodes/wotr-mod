"""eng7-f6d: authored corrections after Terendelev's paid Trickster restitution.

The funeral cue has no progression actions and is hidden. The scale inquiry
keeps its native Conditional/GiveObjective and continuation into her corruption
story. The obsolete future question is hidden and an answer is appended to its
existing list. No correction grants the old trapped-voice evidence or a return.
Source: blueprints.zip, StoryTeller_MainDialogue/Cue_0765, Cue_0777,
Cue_0785, Answer_0784 and AnswersList_0783; enGB.json.
"""
from copy import deepcopy
from story_format import c, n, scene
from storylines.native_overrides import declare

RETURNED = "terendelev.trickster.returned"
WHEN = [["trickster.ever", RETURNED]]
FUTURE_LIST = "33501a1edc26b2c4285096b9214c5414"
FUTURE_CUE = "ca71b79bc9a45b741bcc6599ef017fe7"
TEXT = ('{n}The Storyteller listens, his head bowed.{/n} "No voice cries out from the darkness now. '
        'Terendelev has returned. What she does with that life is hers to decide. '
        'I would rather hear her tell it than search for it in a scale."')

SCENES = [
    scene("terendelev.native.scale_inquiry", "", "TerendelevEpilogue", 5, "", [
        n("line", "Narrator", '{n}The Storyteller puts his hand to his forehead.{/n} '
          '"Terendelev lives again, but her return has not told us how her struggle began. '
          'If you find something else that belonged to her, perhaps we can learn what happened '
          'before she became the protector of Kenabres."')],
        requires=("trickster.ever", RETURNED), forbids=("sacrifice",),
        ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=99, Relationship="terendelev"),
    scene("terendelev.native.future_returned", "", "TerendelevEpilogue", 5, "", [
        n("line", "Narrator", TEXT)], requires=("trickster.ever", RETURNED),
        forbids=("sacrifice",), ForbidOverrides={"sacrifice": "trickster.commander_back"},
        last=99, Relationship="terendelev"),
    scene("terendelev.native.future_question", "Terendelev's return", "Storyteller", 5,
        '"Can you still hear Terendelev through the scale?"', [
            n("answer", "conversant", TEXT, c('"Then I will ask her."'))],
        requires=("trickster.ever", RETURNED), last=5, delay=0, optional=True,
        Relationship="terendelev", AnswerLists=[FUTURE_LIST],
        ReturnToList=True, ReturnText="{n}The Storyteller nods.{/n}"),
]


def integrate(payload):
    payload["Scenes"].extend(deepcopy(SCENES))
    for target, gate, kind in (
        ("21b10801b6c2b194d92506a137ef1307", "terendelev.scale_funeral", "cue"),
        ("fd39fd84212de2047b6b887c9a9cf28e", "terendelev.trapped_future", "answer"),
    ):
        declare(payload, source=__name__, target=target, target_type=kind, action="HIDE", key=gate,
                spec=dict(Target=target, Relationship="terendelev", When=WHEN))
    for target, parent, key, replacement in (
        ("c68d9b3a2b887f645ac539f996a63a92", "31665b38d6922ef4ab4cb83afa8245fe",
         "222096f4-434d-4e8c-99c5-67c070fb21c8", SCENES[0]["Id"]),
        (FUTURE_CUE, "fd39fd84212de2047b6b887c9a9cf28e",
         "da750b86-b8b0-4a2f-a6d4-fea3512327b0", SCENES[1]["Id"]),
    ):
        declare(payload, source=__name__, target=target, target_type="cue", action="REPLACE",
                spec=dict(Parent=parent, Dialog="bf328bcec67a5014f9a56ee6220f3bcc", Key=key,
                          Replacement=replacement, When=WHEN))
