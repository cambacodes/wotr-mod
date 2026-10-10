"""Arueshalae's appended fallen-route promise readers and presence checks.

Scene text and pair display fields are authored in arueshalae_trickster and
harem_rows/s03b. This pass appends readers without shifting existing indices.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, overlay_node, record
from copy import deepcopy

from story_format import p

PENDING = "[PROSE PENDING:"
P = "arueshalae.trickster."
HUNGRY = P + "cost.sent_away_hungry"
SEELAH = "household.pair.seelah_arueshalae.fallen."

APPEND = {
    (P + "fallen.house_call", "start"): [
        p('''{n}She turns your hand over inside the silk, palm up, the way you held it out to her across the rubble of her lair.{/n} "You walked all the way down there to offer me this, and you're still offering it. Careful, darling. One day I'll take it."''',
          requires=(P + "evil.home_offered",)),
    ],
    (P + "epilogue.fallen", "page"): [
        p('''{n}The Commander had once sat across a tavern bench and watched her eat. She saw to it that it was not the last time: for the rest of the war, whenever she was hungry, she came to fetch {mf|him|her} first, so that someone would be watching.{/n}''',
          requires=(P + "fallen.sergeant_watched",)),
        p('''{n}The Commander had once drawn steel on her over a red beard at the back of Fye's. She never forgot it, and she never held it against the Commander. She held it against the sergeant, and waited until the Commander was three days' march away.{/n}''',
          requires=(P + "fallen.sergeant_stopped",)),
        p('''{n}The Commander had once bought a sergeant back from her for a scroll. It became her favourite game: she would sit down beside some soldier at Fye's and wait to see how long it took the Commander to arrive with the chaplain's ink still wet, and how much {mf|he|she} was prepared to pay this time.{/n}''',
          requires=(P + "fallen.sergeant_bought",)),
        p('''{n}Once, years after the war, she asked the Commander again whether the other one had been happy. Before {mf|he|she} could answer she was out of the window, laughing, and she did not come back for a month.{/n}''',
          requires=(P + "fallen.other_happy",)),
        p('''{n}She never asked about the other one again. Of all the Commander's lies, it was the only one she kept.{/n}''',
          requires=(P + "fallen.other_starving",)),
    ],
}


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    return overlay_node(scenes, sid, nid)


def apply(payload):
    scenes = _scenes(payload)
    for (sid, nid), extra in APPEND.items():
        with overlay_item():
            target = _node(scenes, sid, nid).setdefault("Paragraphs", [])
            for paragraph in extra:
                if paragraph not in target:
                    target.append(deepcopy(paragraph))
    for sid in (P + "fallen.sergeant", P + "fallen.the_other_one"):
        with overlay_item():
            if sid not in scenes:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, detail=f"arueshalae cloud: missing scene {sid}")
    for scene in payload["Scenes"]:
        if scene["Id"].startswith((P + "fallen.", P + "epilogue.fallen", SEELAH)):
            for node in scene["Nodes"]:
                with overlay_item():
                    texts = [node.get("Text", "")] + [x.get("Text", "") for x in node.get("Paragraphs") or []]
                    if any(PENDING in t for t in texts):
                        raise OverlayMismatch('overlay.text_mismatch', scene=scene.get("Id"), node=node.get("Id"), detail=f"arueshalae cloud: prose pending left in {scene['Id']}:{node['Id']}")


def integrate(payload):
    apply(payload)
