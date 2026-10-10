"""Shamira: cloud voice-owner pass (villain-route-shamira, design-first).

Applied last in shamira_dream.integrate, after shamira_partner and
shamira_round2. Text and flag-gated read-only paragraphs only: no scene, node
or choice id, choice position, Next, Set, gate, check or cost changes. New
paragraphs are appended after the existing ones (payoff_contracts registers
the stance paragraphs by index). Review and machine truth table:
tools/route_packs/redesign/shamira/cloud-review.md and truth-table.json.

Structure fixed here (readers for flags the route already sets):
  * promises with no reader: manifest_shown (the forty-first crate she swore
    to trace), bargain ("find me something worthy, then we will talk about
    behaving"), want.her / want.nothing (what the Commander said she was kept
    for), asked_lady.enjoyed, game_accepted, night_alone.given_back and
    spy.hanged now have later consumers;
  * a stale decoy (a "crystal tally") contradicted the moonshine-recipes
    answer in ch4.read; the first nights in Drezen were staged in a tent;
    the surgeon's inquiry gave the inquisitor's silence to the chaplain;
  * the flat partner-state register on every epilogue page and the identical
    Nocticula-status sentence repeated on every page of the late epilogue
    are re-voiced, same gates and indices; pages where she has no body (or
    no life) get lines that fit what is left of her.

Canon used (enGB): 2c48146b, d409d925, 339f715c, a05b45a9, 8fededb1 (the
court of false justice), 6a624195 (throne and head), 63e099a8, 4ca2466a.
Authored, no canon claim: the Harem's rooms, the crate's fate is withheld.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, record
import copy

from story_format import p

P = "shamira.trickster."
DEAD, HIDING, RETURNED = "noct.dead", "noct.defeated_not_dead", "nocticula.trickster.returned"
STANCE = "shamira.partner_stance."
SHARE, EXCLUSIVE, SECRET = (STANCE + s for s in ("share", "exclusive", "secret"))
EXPOSED = "shamira.partner.secret_exposed"
PAID = "shamira.partner.public_claim"
BROKEN = "shamira.partner.affair_ended"
CHOSEN = "shamira.partner.exclusive_chosen"

# ---------------------------------------------------------------------------
# 1. Text that failed: (scene prefix, old substring, new substring, minimum hits)
# ---------------------------------------------------------------------------
SUBS = [
    # ch4.read: the decoy matches the answer the player chose.
    ("shamira.trickster.ch4.read",
     '''{n}You hold an imagined crystal tally at the front of your thoughts, its numbers neatly arranged: a harmless decoy prepared for her search. Behind it, the private memory stays shut. Her attention catches on the neatness.{/n} "You rehearsed that. How considerate." {n}She tests behind the numbers, then encounters the recipes you piled over the closed thought. Her nails bite into the throne's arm.{/n} "Something worth hiding. Keep it, for now. I shall remember where you put it."''',
     '''{n}You think of moonshine, loudly: barley and mash, how long the wash should stand, which cousin's still blew up and took his eyebrows with it, a song about copper pipes that rhymes "worm" with "squirm". Under all of it, small and folded, you put the one thing you do not want her to have.{/n}
"Oh, you rehearsed this." {n}She sounds delighted. You feel her wade through the recipes the way a woman lifts her skirts through a midden, testing each one for a false bottom, and then you feel her nails find the edge of something under the barley and slide off it, twice. They bite into the throne's arm instead.{/n} "Something worth hiding. Under a still. Keep it, for now. I shall remember where you put it."''', 1),
    # after.visit: voice.md never_wistful names this exact line as the pattern to avoid.
    ("shamira.trickster.after.visit",
     '''"Liar." {n}Fondly, for her.{/n} "You miss being alone in there. I can feel you missing it, some nights; it moves through your dreams like a draught under a door." {n}She takes her finger away.{/n} "I know that draught. I have had it since I fell. I did not think I would ever be the thing that caused it."''',
     '''"Liar." {n}Fondly, for her, which is to say with her teeth showing.{/n} "You miss being alone in there. I can feel you missing it, some nights; it moves through your dreams like a draught under a door." {n}She takes her finger away.{/n} "Miss it, then. Lie awake missing it. I sleep very well on the warm side of a draught."''', 2),
    # The inquiry copy gave the inquisitor's silence to the chaplain, and put Drezen in a tent.
    ("shamira.trickster.mind.barracks_inquiry", "The chaplain wrote nothing down, Commander.", "He didn't write anything down, Commander.", 1),
    ("shamira.trickster.mind.barracks_inquiry", "intercepts you outside the command tent", "catches you on the stair below your quarters", 1),
    # The first nights after the kill are in the Commander's quarters in Drezen
    # (the wardrobe, the north barracks), not a field tent.
    ("shamira.trickster.", "you sit at the camp table, among the maps", "you sit at your table in Drezen, among the maps", 2),
    ("shamira.trickster.", "You sit at the camp table, among the maps", "You sit at your table in Drezen, among the maps", 1),
    ("shamira.trickster.", "Outside, the sentries change.", "Outside, in the yard, the sentries change.", 3),
    ("shamira.trickster.", "Then the air in the tent goes warm and close", "Then the air in the room goes warm and close", 3),
    ("shamira.trickster.", '"A tent. A cot. Maps with wine on them.', '"A cot. A soldier\'s room in somebody else\'s fortress. Maps with wine on them.', 3),
    ("shamira.trickster.", "in a tent that smells of feet.", "in a room that smells of boots.", 3),
    ("shamira.trickster.", "listening to your sentries piss outside this tent.", "listening to your sentries piss against your wall.", 3),
    ("shamira.trickster.", "You lie a long time listening to the camp,", "You lie a long time listening to the citadel,", 3),
    ("shamira.trickster.", "through your eyes, around the tent, with a disgust", "through your eyes, around the room, with a disgust", 3),
    ("shamira.trickster.killed.drowning", "on your knees on the floor of the tent", "on your knees on the floor of your room", 1),
    # The partner pages wrote 'Her lady' mid-sentence.
    ("shamira.trickster.epilogue.", "to bring to Her lady's bed.", "to bring to her lady's bed.", 2),
    # The night given back was flat; the throw of the game was a shrug.
    ("shamira.trickster.harem",
     '''{n}Her mouth parts. She withdraws from your mind and holds out her hand.{/n} "That was deliberate. Come here, then. I have an answer of my own."''',
     '''{n}Her mouth parts. She withdraws from your mind, and the court voice goes out of hers.{/n} "That was deliberate. You lost on purpose, in my house, with your eyes open." {n}She holds out her hand.{/n} "Nobody throws a game to me. They cheat, and then they die. Come here, then. I have an answer of my own, and you will not like all of it."''', 2),
    # epilogue.kept: "the terms the Commander had actually offered" was paperwork.
    ("shamira.trickster.epilogue.kept",
     "{n}Shamira returned for the warmth that sustained her body, under the terms the Commander had actually offered. A place on her dais did not give her another door into their dreams.{/n}",
     "{n}She came into the Commander's sleep every night for the warmth her body ran on, and took what had been offered, to the last coal. A place on her dais did not buy her a second door into the Commander's head. She tried it anyway, now and then, to keep the Commander honest.{/n}", 1),
    ("shamira.trickster.epilogue.invited",
     "{n}Shamira returned to the window after the war. Her wager had never been played; no thought had been offered for her to answer. She left the invitation open. The warmth that kept her flesh alive bought the Commander no welcome on her dais.{/n}",
     "{n}After the war Shamira came to the Commander's window with her game still unplayed. Nobody had ever come to the Harem to play it. She left the invitation where it was, the way a cat leaves a door open on a bird, and took her coal from the Commander's sleep every night. It bought the Commander nothing on her dais. She made sure her court knew it.{/n}", 1),
]

# ---------------------------------------------------------------------------
# 2. Readers for promises the route made and never paid.
#    (scenes, node, paragraph)
# ---------------------------------------------------------------------------
CRATE = p('''"And your paper-eater's crate." {n}She turns the cup a quarter-turn.{/n} "Forty-one sent under my lady's seal, by Hepzamirah's word, and forty arrived. I said I would find out whether the last was stolen, diverted or given. I have." {n}She smiles at something a long way off.{/n} "I am not going to tell you. I am going to wait until Hepzamirah wants something from my lady, and then say one number in the right room, and watch her face."''',
          requires=(P + "manifest_shown",))
WANT_HER = p('''"You told me you kept me because you wanted me." {n}She lets your coat fall open, once, on purpose, and closes it again.{/n} "Look, then. You have paid for that much. The rest you will have to take up with my court."''',
             requires=(P + "want.her",))
WANT_NOTHING = p('''"You kept me for nothing. Like string." {n}She pulls your coat tight across a body that is finally hers.{/n} "String does not usually walk out of wardrobes, Golarian. Remember that, the next time you think of me as something in a drawer."''',
                 requires=(P + "want.nothing",))
BARGAIN = p('''{n}She looks down at the body she is wearing, at the marks the weeds left on its hips.{/n} "You told me to behave, and I told you to find me something worthy of me first. This is an order nobody paid for." {n}She looks back at you.{/n} "So, no. I shall not behave. Consider that the talk."''',
            requires=(P + "bargain",))
ENJOYED = p('''{n}She does not look at you while she pins her hair.{/n} "You enjoyed killing me. I felt it at the end, under your carpets: a bright little thing, like a boy with a stolen pie. I felt it again last night." {n}The pin goes in hard.{/n} "I have had people flayed for less. I find I would rather keep it."''',
            requires=(P + "asked_lady.enjoyed",))
UNANSWERED = p("{n}You never told her you would come. She has decided that silence was an answer, and that it was yes.{/n}",
               forbids=(P + "game_accepted",))
KEPT_EXTRA = (
    p("{n}The Commander once came the length of her Harem to ask her for one night alone, and then gave it back. She told that story at court for years, a different way every time. In every version the Commander begged.{/n}",
      requires=(P + "night_alone.given_back",)),
    p("{n}The captain of the north postern hanged at dawn, as ordered, and the templars bought another captain within the month. Shamira never asked what became of his girl, and neither did the Commander. She called that the beginning of a proper education.{/n}",
      requires=(P + "spy.hanged",)),
)
NEVER_CRATE = p("{n}She did find out what became of the forty-first crate from the paper-eater's tally. Hepzamirah learned that she knew at a feast, from a single number spoken across the table, and did not enjoy the rest of the evening.{/n}",
                requires=(P + "manifest_shown",))

READERS = [
    (("shamira.trickster.after.city", "shamira.trickster.after.city_awning"), "home", [CRATE]),
    (("shamira.trickster.harem", "shamira.trickster.harem_awning"), "start", [UNANSWERED]),
    (("shamira.trickster.harem", "shamira.trickster.harem_awning"), "morning", [ENJOYED]),
    (("shamira.trickster.epilogue.kept",), "page", list(KEPT_EXTRA)),
    (("shamira.trickster.epilogue.never",), "page", [NEVER_CRATE]),
]
# The waking node exists in three copies (mind.dream f_w_understand, mind.fuel
# w_understand, mind.waking understand), before she leaves through the
# wardrobe; it is found by its text so every copy gets the readers.
WAKING_TEXT_START = '"No. You don\'t." {n}She closes her eyes, reading you.{/n}'
WAKING = [WANT_HER, WANT_NOTHING, BARGAIN]

# ---------------------------------------------------------------------------
# 3. Partner-state and Nocticula-status lines: same gates and indices, her
#    register. Keyed by page condition (shamira_partner.partner_paragraphs).
# ---------------------------------------------------------------------------
CONDITION = {
    "shamira.trickster.epilogue.never": "alive",
    "shamira.trickster.epilogue.captive": "mind", "shamira.trickster.epilogue.unhoused": "mind",
    "shamira.trickster.epilogue.cast_out": "gone", "shamira.trickster.epilogue.drowned": "gone",
    "shamira.trickster.epilogue.mourned": "gone",
}
BODY = "Nocticula's palace kept its mistress and its throne, and its mistress went on taking her pleasure in the Harem whenever the islands bored her. Shamira went on lying under her and looking past her shoulder at the chair."
STATUS = {
    "lady": {
        "body": BODY,
        "alive": "Nocticula's palace kept its mistress and its throne. Shamira kept her Harem, her lady's bed and her lady's errands, and counted the years to the chair the way priests count prayers.",
        "mind": "Nocticula's palace kept its mistress, and its mistress did not trouble to wonder where her steward had gone. What remained of the Ardent Dream heard the city's gossip from inside the Commander's skull and could do nothing with it, having no hands.",
        "gone": "Nocticula's palace kept its mistress. The Harem of Ardent Dreams kept its fountains and lost its mistress, and nobody at the palace summoned what was not there to answer.",
    },
    "hiding": {
        "body": "Nocticula's disappearance after her defeat left the throne standing empty, and its owner alive somewhere in the dark; every demon in Alushinyrra could feel it. Shamira walked past the open doors of the palace more often than she would ever admit, and wanted, and waited. An empty chair with a living owner is the oldest trap in the city.",
        "alive": "Nocticula's disappearance after her defeat left the throne standing empty, and its owner alive somewhere in the dark; every demon in Alushinyrra could feel it. Shamira walked past the open doors of the palace more often than she would ever admit, and wanted, and waited. An empty chair with a living owner is the oldest trap in the city.",
        "mind": "Nocticula's disappearance after her defeat left the throne standing empty. Shamira wanted it from behind the Commander's eyes, which is the worst place in the Abyss to want a chair from.",
        "gone": "Nocticula's disappearance after her defeat left the throne standing empty. The Ardent Dream was not there to want it.",
    },
    "dead": {
        "body": "Nocticula's disappearance after she was struck down brought no answer. Shamira said her lady's name once in the empty palace, to hear whether the shadows would say anything back. They did not. She never said it again where anyone could hear.",
        "alive": "Nocticula's disappearance after she was struck down brought no answer. Shamira said her lady's name once in the empty palace, to hear whether the shadows would say anything back. They did not. She never said it again where anyone could hear.",
        "mind": "Nocticula's disappearance after she was struck down brought no answer. Behind the Commander's eyes something listened for an answer for a long time, and then stopped listening, and would not say why.",
        "gone": "Nocticula's disappearance after she was struck down brought no answer, and there was no Shamira left to call after her.",
    },
    "returned": {
        "body": "Nocticula's palace answered through a projection: a voice with no flesh under it. Shamira had flesh, and made sure her lady knew it. Every message she sent the palace was an invitation and a threat in the same hand, and she wrote them naked.",
        "alive": "Nocticula's palace answered through a projection: a voice with no flesh under it. Shamira had flesh, and made sure her lady knew it. Every message she sent the palace was an invitation and a threat in the same hand, and she wrote them naked.",
        "mind": "Nocticula's palace answered through a projection: a voice with no flesh under it. Behind the Commander's eyes, her steward had no flesh either. Two bodiless women wanted each other's places across the whole of the Abyss, and neither could lay a finger on it.",
        "gone": "Nocticula's palace answered through a projection: a voice with no flesh under it. Nobody at the palace asked after the steward. There was nothing left of Shamira to ask after.",
    },
    "returned_after": {
        "body": "Nocticula's palace answered through a projection while the Commander's tricks still had their power, and the voice outlasted them with no flesh under it. Shamira laughed about that in public exactly once, and the courtier who laughed with her did not live out the week.",
        "alive": "Nocticula's palace answered through a projection while the Commander's tricks still had their power, and the voice outlasted them with no flesh under it. Shamira laughed about that in public exactly once, and the courtier who laughed with her did not live out the week.",
        "mind": "Nocticula's palace answered through a projection while the Commander's tricks still had their power, and the voice outlasted them with no flesh under it. Something behind the Commander's eyes laughed about that, once.",
        "gone": "Nocticula's palace answered through a projection while the Commander's tricks still had their power, and the voice outlasted them with no flesh under it. No steward was left to laugh.",
    },
}
STANCE_TEXT = {  # body pages and the Last Call page only; elsewhere these cannot fire or are kept neutral
    "exclusive_refused": "The Commander once told Shamira to put her lady out of her bed. She laughed, kept her lady, and put the Commander out instead. She went on taking the coal that kept her alive from the Commander's sleep, every night, the way a creditor takes interest.",
    "exclusive_chosen": "Shamira put her lady out of her bed for a mortal who had cheated Ramisa out of a body, and told her so to her face. She did not put her ambitions out with her. She fed on the Commander's dreams every night, lay in the Commander's bed when it amused her, and never once promised to leave the throne alone.",
    "share_paid": "Shamira kept two lovers, a queen and a clown, and let Alushinyrra watch her keep them. Whenever the court asked whose city it was she said \"my lady's\" through her teeth, and smiled, and went on wanting the chair. Neither lover was fool enough to think she had stopped.",
    "share_unanswered": "The Commander had agreed to share her with a lady who never answered. Shamira kept the empty half of her bed exactly as it was, and made sure the Commander noticed it every night.",
    "secret": "Shamira and the Commander kept their nights from her lady. Her servants knew; servants always know. Shamira let them live and watched which of them were saving up to sell it, and that was most of the pleasure.",
    "secret_paid": "When the secret came out before her court, the Commander bought her back with a public confession: their bed, and her lady's city, said aloud under her lady's seal. Shamira made the Commander say it again whenever the court needed reminding. She found the servant who had sold them, and had him flayed in the fountain room where the court could hear.",
    "secret_forged": "Somebody forged her lady's hand to expose them, with her lady dead or gone. Shamira had the forger brought to her alive and kept him alive for as long as it took him to say every name he knew. It took most of a season.",
    "broken": "When the secret came out, the Commander would not name it before her court, and Shamira threw the Commander out of her Harem in front of everyone. After that she came into the Commander's sleep only for the coal she was owed, took it without a word, and left the bed cold.",
    "none": {
        "body": "Nothing was ever settled between Shamira and the Commander about her lady, and Shamira preferred it so. Unsettled things can still be taken.",
        "alive": "Shamira had nothing to settle with the Commander about her lady. She had her lady. She wanted her lady's chair. The Commander was a head she had opened once and meant to open again.",
        "mind": "There was nothing to settle about her lady's bed. A voice behind the Commander's eyes makes no arrangements about anyone's bed; it only listens to them.",
        "gone": "Nothing was left to settle. The Ardent Dream had gone down the Abyss's throat with every claim she had ever made.",
    },
}


def _status_kind(para):
    req, forb = set(para.get("Requires", ())), set(para.get("Forbids", ()))
    if not para.get("Text", "").startswith(("{n}Nocticula", "{n}Her lady", "{n}Every word", "{n}The palace", "{n}No word", "{n}Nothing from", "{n}Whatever had", "{n}A shadow")):
        return None
    if RETURNED in req:
        return "returned" if "trickster.now" in req else "returned_after" if "trickster.now" in forb else None
    if HIDING in req and RETURNED in forb:
        return "hiding"
    if DEAD in req and {HIDING, RETURNED} <= forb:
        return "dead"
    if not req and {DEAD, HIDING, RETURNED} <= forb:
        return "lady"
    return None


def _stance_kind(para):
    req, forb = set(para.get("Requires", ())), set(para.get("Forbids", ()))
    sig = (frozenset(req), frozenset(forb))
    table = {
        (frozenset({EXCLUSIVE}), frozenset({CHOSEN})): "exclusive_refused",
        (frozenset({EXCLUSIVE, CHOSEN, "crossroute.nocticula.available"}), frozenset()): "exclusive_chosen",
        (frozenset({SHARE, PAID}), frozenset()): "share_paid",
        (frozenset({SHARE}), frozenset({PAID})): "share_unanswered",
        (frozenset({SECRET}), frozenset({EXPOSED})): "secret",
        (frozenset({SECRET, EXPOSED, PAID}), frozenset({BROKEN})): "secret_paid",
        (frozenset({SECRET, EXPOSED}), frozenset({PAID, BROKEN})): "secret_forged",
        (frozenset({BROKEN}), frozenset()): "broken",
        (frozenset(), frozenset({SHARE, EXCLUSIVE, SECRET})): "none",
    }
    return table.get(sig)


def _revoice_page(node, condition):
    hits = 0
    for para in node.get("Paragraphs", ()):
        kind = _status_kind(para)
        if kind:
            para["Text"] = "{n}" + STATUS[kind][condition] + "{/n}"
            hits += 1
            continue
        kind = _stance_kind(para)
        if kind == "none":
            para["Text"] = "{n}" + STANCE_TEXT["none"][condition] + "{/n}"
            hits += 1
        elif kind and condition == "body":
            para["Text"] = "{n}" + STANCE_TEXT[kind] + "{/n}"
            hits += 1
    return hits


# Late epilogue intermediate pages: one state line per page, rotated so the
# same sentence is not repeated page after page.
ROTATE = {
    "lady": [
        "Nocticula's court sat across the city. Nothing said in this room would stay in it.",
        "Her lady ruled the city beyond these doors, and had ears in most of its rooms.",
        "Nocticula's palace had its mistress on her throne, and Shamira's lover in its bed.",
        "Every word spoken here would reach the palace by morning. Shamira was counting on it.",
    ],
    "hiding": [
        "Her lady's chair stood empty across the city, and its owner was somewhere in the dark, listening.",
        "Nocticula's disappearance had left an empty throne that nobody in Alushinyrra was brave enough to sit in.",
        "The palace doors stood open on an empty throne. Shamira did not look toward them. She did not need to.",
        "Her lady was in hiding, not dead. Shamira did not forget it for one breath.",
    ],
    "dead": [
        "No word from Nocticula's palace since the fall. The silence sat in the Harem like a guest.",
        "Her lady had not answered since she fell. Shamira kept the place, and kept her own counsel about what silence meant.",
        "Nothing from the palace. No pillow, no knife, no word.",
        "Whatever had become of her lady, the shadows were keeping it.",
    ],
    "returned": [
        "Nocticula's palace had answered with a shadow and no flesh. Every cup Shamira lifted was a small cruelty aimed across the city.",
        "Her lady could speak again, through a projection. She could not touch anything. Shamira touched everything.",
        "A shadow could hear a conspiracy as well as flesh. Shamira conspired anyway, in full view.",
        "Her lady was a voice without a body. Shamira wore hers like a taunt.",
    ],
}
ROTATE["returned_after"] = ROTATE["returned"]
LATE_PAGES = ("page", "partner_late_end", "partner_late_no", "partner_late_private")


def _rotate_late(scene):
    count = 0
    turn = 0
    for node in scene["Nodes"][1:]:
        if node["Id"] in LATE_PAGES:
            continue
        touched = False
        for para in node.get("Paragraphs", ()):
            kind = _status_kind(para)
            if kind:
                para["Text"] = "{n}" + ROTATE[kind][turn % 4] + "{/n}"
                touched = True
                count += 1
        turn += touched
    return count


def _retext_partner_lastcall():
    """Last Call builds Shamira's page from lastcall_partners.PARTNERS later in the
    build; the module-global list is edited the same way shamira_partner does."""
    from storylines import lastcall_partners
    part = next(part for part in lastcall_partners.PARTNERS if part["key"] == "shamira")
    hits = _revoice_page({"Paragraphs": part["paragraphs"]}, "body")
    if hits == 0 and not any(STANCE_TEXT["none"]["body"] in para.get("Text", "") for para in part["paragraphs"]):
        record('overlay.text_mismatch', detail="shamira_cloud: Last Call partner paragraphs not found")


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    own = [s for s in payload["Scenes"] if s["Id"].startswith("shamira.")]

    for prefix, old, new, minimum in SUBS:
        with overlay_item():
            hits = 0
            for s in own:
                if not s["Id"].startswith(prefix):
                    continue
                for node in s["Nodes"]:
                    if old in node["Text"]:
                        node["Text"] = node["Text"].replace(old, new)
                        hits += 1
                    for para in node.get("Paragraphs", ()):
                        if old in para.get("Text", ""):
                            para["Text"] = para["Text"].replace(old, new)
                            hits += 1
            if hits < minimum:
                raise OverlayMismatch('overlay.text_mismatch', detail=str(old)[:70])

    for ids, node_id, paras in READERS:
        for sid in ids:
            with overlay_item():
                if sid not in scenes:
                    raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=node_id, detail="shamira_cloud: missing scene " + sid)
                node = next((n for n in scenes[sid]["Nodes"] if n["Id"] == node_id), None)
                if node is None:
                    raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=node_id, detail=f"shamira_cloud: missing node {sid}:{node_id}")
                node.setdefault("Paragraphs", []).extend(copy.deepcopy(list(paras)))

    waking = [n for s in own for n in s["Nodes"] if n["Text"].startswith(WAKING_TEXT_START)]
    if len(waking) != 3:
        record('overlay.text_mismatch', detail=f"shamira_cloud: expected 3 waking nodes, got {len(waking)}")
    for node in waking:
        node.setdefault("Paragraphs", []).extend(copy.deepcopy(WAKING))

    pages = 0
    for sid, s in scenes.items():
        if not sid.startswith(P + "epilogue."):
            continue
        condition = CONDITION.get(sid, "body")
        targets = [s["Nodes"][0]]
        if sid == P + "epilogue.late":
            targets += [n for n in s["Nodes"] if n["Id"] in LATE_PAGES[1:]]
        for node in targets:
            pages += bool(_revoice_page(node, condition))
    if pages < 12:
        record('overlay.text_mismatch', detail=f"shamira_cloud: partner pages re-voiced: {pages}")
    late = scenes.get(P + "epilogue.late")
    if late is None:
        record("overlay.scene_resolution", scene=P + "epilogue.late")
    elif _rotate_late(late) < 60:
        record('overlay.text_mismatch', scene=P + "epilogue.late", detail="shamira_cloud: late status lines not found")
    _retext_partner_lastcall()
