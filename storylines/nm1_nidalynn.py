"""NM1 (2026-10-01): Nidalynn's courtship on her own step, inside the 2/0/1 allocation.

Coordinator ruling (PP10 COX residual): her visits move onto her in-person presence (the widow on the jeweller's steps,
then her chosen form on the same step) and the excess remote deliveries are retired. What stays at a rest: the device
event (`eggs.vault` or `eggs.straw`) and the grey stone in the hearth in Chapter 3 (2), the kiln letter in Chapter 4
(13 §4 supersedes the R2-5 whitelist), and her welcome home from the Abyss in Chapter 5 (1).

Each moved visit keeps its id, nodes and choices. It stops being a remote delivery and becomes an entry on her hub
(E12c): the Commander's line on the step arranges the visit, and a short line of hers, prefixed to the opening, carries
the scene to where it happens (the kiln, the wall, the Commander's rooms). A visit that can fall on either side of her
reveal keeps the widow's step and gets a twin on her chosen form's step (`<id>.chosen`); each forbids the other.
"""
import copy

P = "nidalynn.trickster."
WIDOW_HUB, CHOSEN_HUB = "nidalynn.presence", "nidalynn.presence.chosen"
WIDOW, CHOSEN = "e24a8cb4f83960748b5bead99d58a36e", "3191b154bbed71b4595a5154ad067e90"
FORM = P + "form_chosen"
DREZEN = "2570015799edf594daf2f076f2f975d8"
KEPT_REMOTE = ("eggs.vault", "eggs.straw", "hearth.grey_stone", "letter.from_the_kiln", "door.home_from_the_dark")

# id -> (hub: "widow" | "chosen" | "either", entry, prefix to the opening or None, [(old, new)] edits of the opening)
MOVES = {
    "hearth.listening": ("widow", '"Come up and see it."', None, []),
    "kiln.fire": ("widow", '"When do we take it down?"',
                  '''{n}"When the kiln is white," she says. "I'll be at it from noon. Bring it down after dark, inside your coat, and don't drop it on the tanners' stair."{/n}''', []),
    "kiln.hatching": ("widow", '"Send for me the moment it starts."', None, []),
    "kiln.truth_owed": ("widow", '"About what I told them at the kiln..."',
                        '''{n}"Not on the step," she says, and goes back to her mending, and does not look up again.{/n}''', []),
    "kiln.whose": ("widow", '"How big is she now?"',
                   '''{n}"Come and look," she says, "and bring an apron." She takes you down to the kiln.{/n}''', []),
    "kiln.claim_again": ("widow", '"The quartermaster has sent me another bill."', None, []),
    "kiln.feeding": ("either", '"Is she eating?"', None,
                     [("Nidalynn tells you this at the door", "Nidalynn tells you this on the step")]),
    "kiln.the_spear": ("widow", '"Has anyone come asking about her?"',
                       '''{n}"Not yet," she says. "They will." She draws the needle through her mending and looks up the tanners' stair, and does not say anything else.{/n}''',
                       [("The sergeant with the squint wakes you himself", "A few nights later the sergeant with the squint wakes you himself")]),
    "kiln.the_druids": ("either", '"You look as if you\'ve had a letter."',
                        '''{n}"Not here," she says, and takes you down to the kiln.{/n}''',
                        [("since before you came down the stair", "all the way down the tanners' stair")]),
    "kiln.ulbrig": ("widow", '"Ulbrig wants to meet you."',
                    '''{n}"Does he." Her needle stops, then goes on. "Then bring him to the kiln tomorrow, and I'll be mending."{/n}''', []),
    "kiln.the_goat": ("either", '"Where is the young one?"',
                      '''{n}She does not answer. She gets up, and you follow her down to the kiln.{/n}''', []),
    "steps.the_wake": ("chosen", '"Who is being buried this week?"', None, []),
    "kiln.the_chaplain": ("widow", '"Someone is waiting for me at the kiln?"',
                          '''{n}"Go on down," she says. "I'll come the short way, with barley."{/n}''',
                          [("Nidalynn, in the doorway, has given him", "Nidalynn, who came the short way, is in the doorway; she has given him")]),
    "kiln.in_charge": ("either", '"If you need a day, I can mind her."',
                       '''{n}"Can you," she says. It is not a question. The next morning she takes you at your word.{/n}''', []),
    "door.own_form": ("widow", '[Sit down beside her.]',
                      '''{n}She does not let you sit. "Not here," she says. "Tonight. Your door."{/n}''', []),
    "wall.wings": ("chosen", '"Where is she?"',
                   '''{n}"Learning," she says. "Come and watch at dusk. The east wall, above the kiln."{/n}''', []),
    "ridge.first_flight": ("chosen", '"Is she ready to fly?"',
                           '''{n}"Any day," she says. "Not today." She sends you home. Three days pass.{/n}''', []),
    "kiln.the_heel": ("chosen", '"The loaf is still on the shelf."',
                      '''{n}She gets up without a word and goes down to the kiln, and you follow her.{/n}''',
                      [("She knows you have come in.", "She knows you have followed her in.")]),
    "ridge.snowfield": ("chosen", '"Tonight?"',
                        '''{n}"After moonset," she says. "The lane below the kiln. Come alone, and dress warm."{/n}''', []),
    "after.first_demon": ("chosen", '"I heard the sentries shouting in the night."',
                          '''{n}"Go and look," she says. "She's waiting for you, not for me."{/n}''', []),
    "ridge.claimed_flight": ("widow", '"Is she flying yet?"',
                             '''{n}"Tomorrow," she says, "if the wind holds. Tell your garrison to look up."{/n}''', []),
    "kiln.long_night": ("chosen", '"Is the kiln banked tonight?"',
                        '''{n}"Low," she says. "Come down after the bell."{/n}''', []),
}


# Polish r2 (audit BEL): node text that only the chosen-form twin changes, (node, old, new); the widow keeps the original.
CHOSEN_EDITS = {
    "kiln.the_goat": [("after_wolves", "I wear a belly and a shawl, and nobody pays for it but me. That's a costume.",
                       "I wore a belly and a shawl all winter, and nobody paid for it but me. That was a costume.")],
}


def _chosen_edits(twin, key):
    for node_id, old, new in CHOSEN_EDITS.get(key, ()):
        node = next(n for n in twin["Nodes"] if n["Id"] == node_id)
        if node["Text"].count(old) != 1:
            raise ValueError("nm1_nidalynn: %s/%s changed (%s)" % (twin["Id"], node_id, old))
        node["Text"] = node["Text"].replace(old, new)


def _place(scene, hub, unit, entry, prefix, edits):
    scene["Remote"] = False
    scene.pop("Kind", None)
    scene.pop("Sender", None)
    scene.pop("Parcel", None)
    scene["InteractionHub"] = hub
    scene["ContactUnit"] = unit
    scene["Areas"] = [DREZEN]
    scene["Entry"] = entry
    start = scene["Nodes"][0]
    for old, new in edits:
        if start["Text"].count(old) != 1:
            raise ValueError("nm1_nidalynn: %s opening changed (%s)" % (scene["Id"], old))
        start["Text"] = start["Text"].replace(old, new)
    if prefix:
        start["Text"] = prefix + "\n" + start["Text"]


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    own = [s for s in payload["Scenes"] if s.get("Relationship") == "nidalynn" and s.get("Remote")]
    unplanned = sorted(s["Id"] for s in own if s["Id"][len(P):] not in MOVES and s["Id"][len(P):] not in KEPT_REMOTE)
    if unplanned:
        raise ValueError("nm1_nidalynn: a remote visit has no place: " + ", ".join(unplanned))
    for key, (where, entry, prefix, edits) in MOVES.items():
        scene = scenes[P + key]
        if where == "chosen":
            if FORM not in scene["Requires"] and P + "kissed" not in scene["Requires"] and P + "bread_kept" not in scene["Requires"] \
                    and "nidalynn.committed" not in scene["Requires"] and P + "snowfield" not in scene["Requires"]:
                raise ValueError("nm1_nidalynn: %s is not past her reveal" % scene["Id"])
            _place(scene, CHOSEN_HUB, CHOSEN, entry, prefix, edits)
            continue
        if where == "either":
            twin = copy.deepcopy(scene)
            twin["Id"] = scene["Id"] + ".chosen"
            _chosen_edits(twin, key)
            twin["Requires"] = list(scene["Requires"]) + [FORM]
            twin["Forbids"] = list(scene["Forbids"]) + [scene["Id"], twin["Id"]]
            scene["Forbids"] = list(scene["Forbids"]) + [FORM, twin["Id"]]
            _place(twin, CHOSEN_HUB, CHOSEN, entry, prefix, edits)
            payload["Scenes"].append(twin)
        elif FORM in scene["Requires"]:
            raise ValueError("nm1_nidalynn: %s needs her chosen form" % scene["Id"])
        _place(scene, WIDOW_HUB, WIDOW, entry, prefix, edits)
