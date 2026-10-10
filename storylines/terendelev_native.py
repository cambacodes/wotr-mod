"""eng7-f6d: saved scenes retained after consolidation with eng7-f6c.

The active corrections live in engine_f6c. These duplicate deliveries are
retired by chapter gating, retaining every saved scene, node and choice.
The native future question stays available with its corrected reply.
Source: blueprints.zip, StoryTeller_MainDialogue/Cue_0765, Cue_0777,
Cue_0785, Answer_0784 and AnswersList_0783; enGB.json.
"""
from copy import deepcopy
from story_format import c, n, scene

RETURNED = "terendelev.trickster.returned"
WHEN = [["trickster.now", RETURNED]]
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
        requires=("trickster.now", RETURNED), forbids=("sacrifice",),
        ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=99, Relationship="terendelev"),
    scene("terendelev.native.future_returned", "", "TerendelevEpilogue", 5, "", [
        n("line", "Narrator", TEXT)], requires=("trickster.now", RETURNED),
        forbids=("sacrifice",), ForbidOverrides={"sacrifice": "trickster.commander_back"},
        last=99, Relationship="terendelev"),
    scene("terendelev.native.future_question", "Terendelev's return", "Storyteller", 5,
        '"Can you still hear Terendelev through the scale?"', [
            n("answer", "conversant", TEXT, c('"Then I will ask her."'))],
        requires=("trickster.now", RETURNED), last=5, delay=0, optional=True,
        Relationship="terendelev", AnswerLists=[FUTURE_LIST],
        ReturnToList=True, ReturnText="{n}The Storyteller nods.{/n}"),
]


def integrate(payload):
    # eng7-integ3: f6c owns these native corrections. Keep every f6d scene,
    # node and answer for saves, but retire its duplicate deliveries. The
    # original future question remains native and reaches the corrected cue.
    retired = deepcopy(SCENES)
    for page in retired:
        page["Forbids"].append("chapter_later")
    payload["Scenes"].extend(retired)
