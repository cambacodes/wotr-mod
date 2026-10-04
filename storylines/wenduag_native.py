"""Wenduag's native ascension slide for a committed Wenduag (engine queue 7b; Writer/handoffs/trickster/wenduag.md).

Epilogues/BookPage_0349 Cue_0580 (TE with companions seen, and her Q3 not done; RanRomance's AranEpil replaces its second
condition with "etude 6eddba95 not playing", its only change to the cue): "Wenduag refused to ascend with the Commander. She
wished to walk her path alone, for solitude brings strength." Beside a committed Wenduag's pack page that reads as a parting.
The variant keeps her refusal (a Mongrel takes power, she is not handed it) and drops the parting. Read only; warning-only
(a refusal keeps the native slide and degrades nothing); delivered only while its scene is available (E14d delivery: the
pack page's own forbids). Save name: native-edit.4bb3706172f1ed54ca11db96254c4638.
"""
import copy

from storylines.native_overrides import register_legacy

from story_format import n, scene

CUE_0580 = "4bb3706172f1ed54ca11db96254c4638"    # World/Dialogs/Epilogues/Cue_0580
PAGE = "223fd069ee25c784db2df011adbf10f8"        # World/Dialogs/Epilogues/BookPage_0349
COMPANIONS = "fec3b6f28610c8a48a239f148ed3ed60"  # CueSequence_Companions
ASCENT = "wenduag.trickster.epilogue.native_ascent"
FORBIDS = ("wenduag.closed", "sacrifice", "wenduag.q3_killed", "wenduag.q3_sent_away", "wenduag.hello_sent_away", "wenduag.hello_attacked")

SCENES = [scene(ASCENT, "", "WenduagEpilogue", 6, "", [
    n("page", "Narrator", "{n}Wenduag refused to ascend with the Commander. Power that was handed to her was not power she had "
      "taken, and she would not wear it. She walked her path alone, as she said, for solitude brings strength. It was "
      "noticed that the path ran through the Commander's door every night, and that she never once explained this.{/n}",
      portrait="Wenduag")],
    # Engine-q2 (T6a): trickster.now. Her commitment is not provably a Trickster act, so the path is this edit's only
    # Trickster evidence; a run that left the path at a Chapter 4 failure or a Summit conversion keeps the native slide.
    requires=("trickster.now", "wenduag.committed"), forbids=FORBIDS + ("wenduag.trickster.echo.abyss.unavailable",), last=99, Relationship="wenduag",
    ForbidOverrides={"sacrifice": "trickster.commander_back"})]

NATIVE_EPILOGUE_EDITS = {
    CUE_0580: dict(Page=PAGE, Sequence=COMPANIONS, Key="7d53ebcc-5fe2-4066-b52f-eb54fa081512", Replacement=ASCENT,
                   When=[["wenduag.committed", "trickster.now", "!wenduag.closed", "!wenduag.trickster.echo.abyss.unavailable"]], KeepNativeImage=False, Variants=[]),
}


def integrate(payload):
    """Register the scene and the edit (after the Wenduag route)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)
