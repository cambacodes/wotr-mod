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
    n("page", "Narrator", "{n}Wenduag refused the offered ascent. She called it another master's bait. Her hunters stayed near Drezen, "
      "and anyone who claimed the Commander had abandoned her was invited to say it within reach of her knife.{/n}",
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
    # eng8-q8b begin: the legacy copy's survival lift shares its existing
    # current-path presence policy. Stored return/payment facts remain intact;
    # this does not alter other women's persistent completed return contracts.
    from pathlib import Path
    import json
    contract = json.loads((Path(__file__).resolve().parents[1] / "tools/left_trickster_consumer_contracts.json").read_text(encoding="utf-8"))
    for group in payload["Derived"].get(contract["return_reader"], []):
        if "trickster.now" not in group:
            group.append("trickster.now")
    # eng8-q8b end
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    register_legacy(payload, __name__, edits=NATIVE_EPILOGUE_EDITS)
    from storylines import wenduag_partner_stance
    wenduag_partner_stance.integrate(payload)


# eng8-q8e begin: authored reconciliations of retained partnership, never redemption.
DEPARTURE = "8f6017d8d3bc5ec46b15773947e80c70"
MOURNING = "86bf0569a9029ae4b8c9d300a41e5739"
GREYBOR = "8593ec10e3c34cdaaa2d2ed45e73e58a"
EMBER = "3d54fe05a0fe44f78ac907c37fe8a460"
NATIVE_BACK = "wenduag.trickster.epilogue.native_commander_back"
PACK = "wenduag.trickster.epilogue.pack"

def _ending(id, text, requires=("trickster.now", "wenduag.committed")):
    return scene(id, "", "WenduagEpilogue", 6, "", [n("page", "Narrator", text, portrait="Wenduag")],
        requires=requires, forbids=FORBIDS + ("wenduag.trickster.echo.abyss.unavailable",), last=99,
        Relationship="wenduag", ForbidOverrides={"sacrifice": "trickster.commander_back"})

SCENES.extend([
    _ending("wenduag.trickster.epilogue.native_pack", '''{n}After the war, Wenduag gathered her own band of hunters in Drezen. She fought where the fighting was worst, took what she wanted, and returned to the Commander with blood on her hands. The citadel was still her den.{/n}'''),
    _ending(NATIVE_BACK, '''{n}Wenduag took the Commander's return with a snarl. She had already sharpened her knives for the next war. Now she had someone worth fighting beside again.{/n}''',
            ("trickster.now", "trickster.commander_back", "wenduag.trickster.native")),
    _ending("wenduag.trickster.epilogue.native_greybor", '''{n}The price on Wenduag's head reached Greybor. Taking it meant hunting her through the Commander's citadel. He declined the contract. The huntress laughed when she heard, and kept sharpening her knives.{/n}'''),
    _ending("wenduag.trickster.epilogue.native_ember", '''{n}Wenduag led her hunters out of Drezen to pillage and burn the orphanage. She turned its inhabitants out onto the street and returned to the citadel with her plunder. She never spoke of the former companion she had found there.{/n}'''),
])
# Native romance keeps its own earned yes; it does not require RRT commitment.
SCENES[-3]["Forbids"].extend(["wenduag.dead_any", "wenduag.kicked_out"])
SCENES[-3]["ForbidOverrides"].update({"wenduag.dead_any": "wenduag.trickster.returned", "wenduag.kicked_out": "wenduag.trickster.returned"})
NATIVE_EPILOGUE_EDITS.update({
    DEPARTURE: dict(Page=PAGE, Sequence=COMPANIONS, Key="8590f7c2-79d5-4179-9c8a-0798f4ef5de9",
        Replacement="wenduag.trickster.epilogue.native_pack", When=[["trickster.now", "wenduag.committed"]], KeepNativeImage=False, Variants=[]),
    MOURNING: dict(Page=PAGE, Sequence=COMPANIONS, Key="0dfe0435-8149-466d-bf0c-88d648651c3a",
        Replacement=NATIVE_BACK, When=[["trickster.now", "trickster.commander_back", "wenduag.trickster.native"]], KeepNativeImage=False, Variants=[]),
    GREYBOR: dict(Parent="62f20840e6aa33844b641c5c8e10f814", Dialog="ae58532cb72b28b4eaaccb82eb78eaea", Key="0f468f97-27b0-492b-9213-7a53171c52af",
        Replacement="wenduag.trickster.epilogue.native_greybor", When=[["trickster.now", "wenduag.committed"]], KeepNativeImage=False,
        Variants=[dict(Replacement="wenduag.trickster.epilogue.native_greybor_back", When=[["trickster.now", "trickster.commander_back", "wenduag.trickster.native"]], KeepNativeImage=False)]),
    EMBER: dict(Parent="47c754ad6f357e64f9d1295065698aae", Dialog="ae58532cb72b28b4eaaccb82eb78eaea", Key="5442dcf4-e1dd-47f5-b41a-c127471418f0",
        Replacement="wenduag.trickster.epilogue.native_ember", When=[["trickster.now", "wenduag.committed"]], KeepNativeImage=False, Variants=[]),
})
_gb_back = copy.deepcopy(SCENES[-2])
_gb_back["Id"] = "wenduag.trickster.epilogue.native_greybor_back"
SCENES.append(_gb_back)
# eng8-q8e end
