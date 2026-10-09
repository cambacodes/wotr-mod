"""Arueshalae: cloud voice-owner pass (villain-route-arueshalae, design-first; corrupted/fiend branches).

Applied last, at the end of expansion._make_expansion (after every appender, the harem rows and the earlier wave layers),
so appended paragraphs move no index. Text and flag-gated paragraphs only: no scene, node or choice id, choice position,
Next, Set, gate, check, cost or GuidFor changes. Existing text is asserted before it is replaced (including text the arue12
pass in arueshalae_round2 already rewrote). The redeemed register (arue12) is kept; nothing here touches a redeemed scene.
J03 pair rows (household.pair.seelah_arueshalae.fallen.*) get text only, no paragraphs.
Review and truth table: tools/route_packs/redesign/arueshalae/cloud-review.md.

Structure (the scenes themselves are authored in arueshalae_trickster, section 5b):
  * S1 the sergeant: "Not a drop" (house_call:refuse) named a red-bearded sergeant at the back of Fye's; on the road a new
    save can play, only Lann's hearsay and an epilogue line paid it ("told ... as if reporting the weather"). New hub scene
    arueshalae.trickster.fallen.sergeant puts the feed on screen with three answers (steel, complicity, a scroll spent); her
    epilogue now reads which one;
  * S2 the other one: the locked "was she happy?" beat lived only on the retired death-return road; its live twin
    arueshalae.trickster.fallen.the_other_one has its two answers read on her epilogue;
  * S3 the held-out hand: arueshalae.trickster.evil.home_offered (the Trickster's hand at the lair) was set and never read;
    house_call:start now reads it;
  * S4 Seelah's hearing: the fallen pair row staged her fall as a written account crossed out and pinned under a banner
    (paperwork standing in for the scene); it is now said to the scouts' faces in the stable yard.

Canon used (enGB): 2c206218 ("being a strong, healthy demon is pure bliss"), 9f6082a7 ("Come here"), 72dcb220 (pies,
street kittens), 718266a8; hub anchors cited in arueshalae_trickster 5b (Cue_0027 57858226 "Everyone who has tasted my
sweetness said it was worth it"). Authored, no canon claim: the sergeant, his sweetheart, the scouts and the star.
"""
from copy import deepcopy

from story_format import p

PENDING = "[PROSE PENDING:"
P = "arueshalae.trickster."
HUNGRY = P + "cost.sent_away_hungry"
SEELAH = "household.pair.seelah_arueshalae.fallen."

# ---------------------------------------------------------------------------
# Whole-node text replacements: (scene, node) -> (expected old prefix, new text).
# ---------------------------------------------------------------------------
NODES = {}

_HEARD = '''{n}She walks down the line of horses, slowly, and stops at the youngest scout, the one with a little Desnan star still tied to his bridle. She flicks it with one claw.{/n} "I gave that up. The goddess, the prayers, the dreary little promises. I wanted to be hungry again, and now I am." {n}She leans in until he leans back against his horse.{/n} "Ride close to me tomorrow and you'll come home. Come close to me tonight and you won't. That's all you need to know about me, sweet."
{n}The boy cuts the star off his bridle himself. Seelah watches him do it, then turns to Arueshalae.{/n} "I was right to help you try. You chose what to do with it. I won't call you sister."
"Oh, I shall keep calling you sister. That face you make is delicious."
{n}Before nightfall Seelah moves the scouts' tents to the far side of the yard. Arueshalae laughs at that, and leaves them alone. For now.{/n}'''
_REFUSED = '''{n}Seelah turns the scouts' horses round with her own hands.{/n} "Then they don't ride with her. I'll take them up the Wound road myself."
"Do describe me properly on the way. Some of them have such dull imaginations."
{n}Arueshalae bares her teeth at Seelah. The paladin leads the horses out of the yard and does not look back.{/n}'''

NODES[(SEELAH + "settle", "start")] = ("{n}Seelah catches Arueshalae lifting the crusade banner", '''{n}In the stable yard three of Seelah's scouts are saddling for the Wound road. The youngest still has a little Desnan star tied to his bridle, the kind Arueshalae used to bless for anyone who asked. Seelah sees it, and sees Arueshalae watching it, and plants herself between them.{/n}
"They ride with you at dawn, and half of them think they're riding with a servant of Desna. I backed you once. I'm not going to pretend I didn't. So tell them what they're riding with. Your mouth, not mine."
{n}Arueshalae leans back against the stable door and stretches her wings until the horses shy.{/n}
"A succubus. They might even enjoy being disappointed."''')
NODES[(SEELAH + "settle", "heard")] = ('"Mine. I\'m wearing my own colors.', _HEARD)
NODES[(SEELAH + "settle", "misheard")] = ("{n}Seelah takes the account from you", '''{n}Seelah turns on you, not on her.{/n}
"No. Desna's star doesn't make it true. She hasn't offered these boys a damned thing but her teeth."
{n}Arueshalae stretches, grinning at the paladin.{/n}
"But you liked me so much better that way. Leave him his trinket. It'll give him something to hold on to while I eat."
{n}Seelah says nothing more. The star stays on the bridle, and the scouts ride out at dawn believing what they believed.{/n}''')
NODES[(SEELAH + "settle", "refused")] = ("{n}Seelah pulls the stool away from the banner.", _REFUSED)
NODES[(SEELAH + "retry", "start")] = ("{n}Seelah lays the account of the last hearing", '''{n}The boy with the Desnan star on his bridle is back from the Wound road, alive, and saddling again. Arueshalae turns the little star over with one claw while Seelah watches from the stable door.{/n}
"Still hiding behind Desna, sister? Ask me again. I liked the answer."''')
NODES[(SEELAH + "retry", "heard")] = ('"Mine. I\'m wearing my own colors.', _HEARD)
NODES[(SEELAH + "retry", "refused")] = ("{n}Seelah pulls the stool away from the banner.", _REFUSED)

# Choice text edits: (scene, node, index) -> (old, new).
CHOICES = {
    (SEELAH + "settle", "start", 0): ('"Admit what she says here. Nothing she hasn\'t said."', '"Let her tell them herself. Every word."'),
    (SEELAH + "settle", "start", 1): ('"The old Desnan account is enough."', '"Leave the boy his star. It keeps him brave."'),
    (SEELAH + "settle", "start", 2): ('"End the hearing."', '"Nobody tells them anything. Turn the horses out."'),
    (SEELAH + "retry", "start", 0): ('"Let her give her own account."', '"Let her tell them herself."'),
    (SEELAH + "retry", "start", 1): ('"Leave that account unanswered."', '"Nobody tells them anything."'),
}
FIELDS = {
    SEELAH + "settle": {"Title": ("What the witness said", "Whose colors")},
    SEELAH + "retry": {"Title": ("What the witness said", "Whose colors"),
                       "Entry": ("[Seelah and Arueshalae: hear her account again]",
                                 "[Seelah and Arueshalae: the boy with the star]")},
}

# ---------------------------------------------------------------------------
# Existing paragraphs re-voiced in place: (scene, node, index) -> (gate, old prefix, new). Gate = (Requires, Forbids).
# ---------------------------------------------------------------------------
REVOICE = {
    # S1: the report at breakfast becomes the act and its aftermath (true after every answer in fallen.sergeant).
    (P + "epilogue.fallen", "page", 3): (
        ([HUNGRY], []), "{n}A red-bearded sergeant of the third company went to sleep",
        "{n}The red-bearded sergeant of the third company went back to the bench at Fye's again and again, on his own feet, "
        "until one night he went to sleep there and did not wake. She came to the Commander's table the next morning with his "
        "sweetheart's name still in her mouth, and asked {mf|him|her} to pass the bread.{/n}"),
}

# ---------------------------------------------------------------------------
# Appended read-only consumers: (scene, node) -> [paragraph].
# ---------------------------------------------------------------------------
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
    scene = scenes.get(sid)
    if scene is None:
        raise ValueError(f"arueshalae cloud: missing scene {sid}")
    for node in scene["Nodes"]:
        if node["Id"] == nid:
            return node
    raise ValueError(f"arueshalae cloud: missing node {sid}:{nid}")


def _gate(paragraph):
    return (sorted(paragraph.get("Requires", [])), sorted(paragraph.get("Forbids", [])))


def _optional(scenes, sid):
    """The household pair rows exist only when the harem rows are registered (test fixtures build without them)."""
    return sid.startswith("household.pair.") and sid not in scenes


def apply(payload):
    scenes = _scenes(payload)
    for (sid, nid), (old, new) in NODES.items():
        if _optional(scenes, sid):
            continue
        node = _node(scenes, sid, nid)
        if node["Text"] != new:
            if not node["Text"].startswith(old):
                raise ValueError(f"arueshalae cloud: {sid}:{nid} text changed upstream")
            node["Text"] = new
    for (sid, nid, index), (old, new) in CHOICES.items():
        if _optional(scenes, sid):
            continue
        choice = _node(scenes, sid, nid)["Choices"][index]
        if choice["Text"] not in (old, new):
            raise ValueError(f"arueshalae cloud: {sid}:{nid}>{index} choice text changed upstream")
        choice["Text"] = new
    for sid, fields in FIELDS.items():
        if _optional(scenes, sid):
            continue
        for key, (old, new) in fields.items():
            if scenes[sid].get(key) not in (old, new):
                raise ValueError(f"arueshalae cloud: {sid} {key} changed upstream")
            scenes[sid][key] = new
    for (sid, nid, index), ((requires, forbids), old, new) in REVOICE.items():
        paragraph = _node(scenes, sid, nid)["Paragraphs"][index]
        if _gate(paragraph) != (sorted(requires), sorted(forbids)):
            raise ValueError(f"arueshalae cloud: {sid}:{nid}#{index} gate changed upstream")
        if paragraph["Text"] != new:
            if not paragraph["Text"].startswith(old):
                raise ValueError(f"arueshalae cloud: {sid}:{nid}#{index} text changed upstream")
            paragraph["Text"] = new
    for (sid, nid), extra in APPEND.items():
        target = _node(scenes, sid, nid).setdefault("Paragraphs", [])
        for paragraph in extra:
            if paragraph not in target:
                target.append(deepcopy(paragraph))
    for sid in (P + "fallen.sergeant", P + "fallen.the_other_one"):
        if sid not in scenes:
            raise ValueError(f"arueshalae cloud: missing scene {sid}")
    for scene in payload["Scenes"]:
        if scene["Id"].startswith((P + "fallen.", P + "epilogue.fallen", SEELAH)):
            for node in scene["Nodes"]:
                texts = [node.get("Text", "")] + [x.get("Text", "") for x in node.get("Paragraphs") or []]
                if any(PENDING in t for t in texts):
                    raise ValueError(f"arueshalae cloud: prose pending left in {scene['Id']}:{node['Id']}")


def integrate(payload):
    apply(payload)
