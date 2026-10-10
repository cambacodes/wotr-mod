"""Devarra: cloud voice-owner pass (villain-route-devarra, design-first).

Applied last, at the end of expansion._make_expansion (after her route, Last
Call's pages and account rows, Nidalynn's pages, the S50 pair row and the late
outcome passes that finish epilogue.commit have all written their copies). Text and flag-gated paragraphs only: no scene, node or choice id,
choice position, Next, Set, gate, check, cost or GuidFor changes. Paragraphs are
only appended after existing ones; existing paragraphs are re-voiced in place
with their gates checked. The S50 pair row gets text only (J03: no paragraphs).
Review and truth table: tools/route_packs/redesign/devarra/cloud-review.md.

Structure fixed here (read-only consumers of flags the route already sets):
  * the smallest-egg debt: "I will name it ... at the edge of the world"
    (smallest_egg:want) had no payment; her epilogue said "she had never named
    it" (P31 reads lastcall.called and printed the same words as P32), while
    Nidalynn's pages said she named it at the rift. Now the Last Call is an
    answer, not a negotiation (no paper bill), and she names the price herself
    afterwards on every page that can show it; unanswered, she collects from
    whatever is nearest, as she promised (smallest_egg:wont);
  * the S50 pair: "She named her price" before any naming, "She has claimed a
    debt" for the Commander's own "Then you owe me" (wrong speaker), and "the
    grey one" asking questions in runs where she is dead;
  * marked is set by three different confessions (absent, smashed, ordered);
    two readers assumed the retired moult answer "I watched";
  * promises with no reader: the twelfth-egg lie ("I will add them together"),
    the stolen Queen of Iobaria, "Say no to me again" (vault_refused), "Remember
    that" (looked_away), "I will let you say that once" (tower.warned), "you will
    not like the coin" (debt_claimed), the purchased and the voluntary battle
    (claude-work-queue devarra:D03-D06), the S50 feed in her own epilogue;
  * the late-acceptance epilogue (epilogue.commit) read none of her history;
  * the_cells sent the Commander away before the meal she staged for them;
  * flown-world leftovers of the retired moult: the grey seam and grey scars.

Canon used (enGB): 05070eba, 07ec4e7c, 5ccf6032, ce8e21b7, 3b37a8b4, f6fcc869,
a73cb7ca, ca4b91d7. Authored, no canon claim: the tower, the month, the herald,
the deserter, the burned column, the cavalry horses.
"""
from copy import deepcopy

from story_format import p

PENDING = "[PROSE PENDING:"
D = "devarra.trickster."
T = "devarra.tower."
PAIR = "household.pair.nidalynn_devarra."
BILL = D + "cost.egg_withheld"
CALLED = "devarra.lastcall.called"


def when(requires, body, forbids=(), any_groups=()):
    return p(body, requires=requires, forbids=forbids, any_groups=any_groups)


# ---------------------------------------------------------------------------
# Shared paragraph bodies.
# ---------------------------------------------------------------------------
NAMED = ("{n}The Commander had said her name at the rift, and the debt with it. She named the price herself, on her ridge, "
         "the spring after: not the child, and not the silver who kept her. A month of the Commander's every year, beginning "
         "on the day she chose. The Commander spent it in the tower and nowhere else, ate what she carried up the mountain, "
         "raw, and went down when the month was done and not an hour before. The annual bite was another matter; that was "
         "only the tariff.{/n}")
NAMED_UNBOUND = ("{n}The Commander had said her name at the rift, and the debt with it. She named the price herself, on her "
                 "ridge, the spring after: a month of the Commander's every year, beginning on the day she chose. No bite, no "
                 "bed, no appointment; only the month, spent in her tower eating what she brought up the mountain, and owed "
                 "whether the Commander liked her or not.{/n}")
NAMED_FAR = ("{n}The Commander had said her name at the rift, and the debt with it. She named the price on the ridge the "
             "spring after: a month of the Commander's every year. She flew back from her far hunting grounds once a year "
             "to collect it, kept the Commander in the old tower for the whole of it, and left on the last day without a "
             "word.{/n}")
NEAREST = ("{n}Nobody ever answered her for the smallest egg, so she collected it the way she had said she would: from "
           "whatever of the Commander's was nearest when she came. The first spring it was a horse out of the citadel "
           "stable, eaten in the yard while the grooms watched. The next it was the hound that slept by the Commander's "
           "door. Once it was the groom who held the stable shut against her and did not run. She called every one of "
           "them interest, and the debt no smaller.{/n}")
UNCOLLECTED = ("{n}What she was owed for the smallest egg she never came back to collect, and never released. Every spring "
               "the Commander listened for wings on the roof, and never stopped listening.{/n}")

# ---------------------------------------------------------------------------
# Whole-node text replacements: (scene, node) -> (expected old prefix, new text).
# ---------------------------------------------------------------------------
NODES = {}

NODES[("devarra.lastcall.call", "call")] = ("{n}Devarra's bill names the egg", '''{n}Devarra never wrote anything down in her life. What she is owed for the smallest egg is not in your pack: it is on the north ridge above Drezen, lying with its chin on the sill, counting eleven where she laid twelve. She is not here, and nothing at Threshold will bring her. You can turn north, into the wind off the Wound, and put her name and the debt into it aloud, so that it is said before the end. Or you can let it stand, and let her come and collect it her own way.{/n}''')

NODES[("trickster.lastcall.account.devarra", "call")] = ("{n}The bill for the smallest egg", '''{n}Somewhere north of the rift a woundwyrm is still counting eleven where she laid twelve. You do not say her name. Nothing is promised and nothing is released; whatever she takes for the smallest egg, she will choose it herself, from whatever of yours is nearest when she comes.{/n}''')

NODES[(D + "epilogue.pending", "page")] = ("{n}Devarra kept the north ridge", '''{n}Devarra kept the north ridge and ate whatever Drezen sent up it, carts and carters' oxen alike. The Commander's story was still unfinished, so she asked every carter what had happened next, and ate the oxen of the ones who did not know. When the carts stopped, she hunted the old Wound and came back with demon flesh between her teeth. She never named an appointment. A thing that had not answered her, she said, had not earned one.{/n}''')

NODES[(D + "epilogue.claimed", "page")] = ("{n}The ending sent to Devarra", '''{n}Devarra never gave the conqueror's ending another answer; she had given it one already, with her claw through the parapet. She left the north ridge and hunted far from the crusade's banners. Twice a herald rode out after her with the Commander's colours and a fine speech. The first one's horse came back. The second time nothing did.{/n}''')

NODES[(D + "epilogue.commit", "page_exit")] = ("{n}Her answer stood.", '''{n}The ridge stayed hers, and so did the Commander, one night a year at least. She never let either of them forget it.{/n}''')

NODES[(T + "the_cells", "verdict")] = ('"Not impressive,"', '''"Not impressive," {n}she says at last, gently.{/n} "True, and small, and sad, and not impressive." {n}She looks at you.{/n} "You see, crusader? That is the difference between his god and me. His god promised him something, and took the price, and never came. I told him my price at the start, and now I keep my word."
{n}She does it slowly, so that you can see all of it. She burns him first, with a thin flame from the feet up, the way she bastes a stag, until he is screaming the Locust Lord's name and then nobody's name at all. Then she bites him in half at the waist and eats the top half while the rest is still moving in the chains. One of the guards at the door is sick on the stair. She does not hurry. When she has finished she licks the chains clean.{/n}
"Go down the mountain now. You have seen what you came for."''')

# Substring edits inside an existing node text: (scene, node) -> [(old, new)].
SUBS = {}
SUBS[(D + "after.tithe", "watch")] = [(
    '"She says she is still deciding what you will watch next. She said it twice, so that I would remember the exact words."',
    '"She says you told her to her face how her clutch died, and that she has decided you are going to watch something die for it, when she has chosen what. She said it twice, so that I would remember the exact words."')]
SUBS[(T + "the_clutch", "nest")] = [('"You watched once. Watch again."', '"You told me how mine died. Now you see how theirs do."')]
SUBS[(T + "the_cells", "leave")] = [(
    '"Go. I will tell you whether he impressed me. He will not."',
    '"Go. I will tell you whether he impressed me. He will not."\n{n}You are halfway down the ridge when the screaming starts. It follows you all the way to the north gate; she is a patient cook. When it stops, the quiet is worse.{/n}')]
SUBS[(T + "the_dwarf", "climb")] = [("with the grey seam under her wing", "with the pale seam under her wing")]
SUBS[(T + "the_scar", "start")] = [("A neat grey crescent of punctures", "A neat crescent of punctures")]
for _body in ("widow", "chosen"):
    SUBS[(PAIR + "notice." + _body, "account")] = [('"And what did the grey one ask of you?"',
                                                    '"And her mother? Has she come asking what you owe for this one?"')]
    SUBS[(PAIR + "notice." + _body, "debt")] = [(
        '''"A debt isn't the same as the price of her egg. Don't mix them up when she comes collecting."''',
        '''"You told a woundwyrm she owes you." {n}Nidalynn looks at you as if you had put your hand into the kiln to see whether it was hot.{/n} "Then she'll pay it in something you'd never have asked for. Don't let her pay it in this one."''')]

# Choice text edits: (scene, node, index) -> (old, new).
CHOICES = {
    ("devarra.lastcall.call", "call", 0): ("Continue", '[Turn north] "Devarra. The smallest egg. Name it, and I\'ll pay."'),
    ("devarra.lastcall.call", "call", 1): ("[Leave the demand unanswered. The bill remains outstanding.]",
                                           "[Say nothing. Let her come and collect it her own way.]"),
}
for _body in ("widow", "chosen"):
    CHOICES[(PAIR + "notice." + _body, "account", 0)] = ('"She named her price for the smallest egg."',
                                                         '"She has put a life on my head for it. She hasn\'t said whose."')
    CHOICES[(PAIR + "notice." + _body, "account", 1)] = ('"She has claimed a debt. She has not named the egg\'s price."',
                                                         '"I told her she owes me for her clutch. She said dragons are owed, and that I wouldn\'t like the coin."')
    CHOICES[(PAIR + "notice." + _body, "account", 2)] = ('"She has not named a bill for it."', '"Nobody has come asking."')

# Scene titles / entries: scene -> {field: (old, new)}.
FIELDS = {
    "trickster.lastcall.account.devarra": {"Title": ("The Grey Bill", "The Smallest Egg"),
                                           "Entry": ("[Leave the grey dragon's bill unanswered.]",
                                                     "[Leave the woundwyrm's debt unanswered.]")},
    "devarra.lastcall.page": {"Title": ("The Grey Tariff", "The Woundwyrm's Tariff")},
}

# ---------------------------------------------------------------------------
# Existing paragraphs re-voiced in place: (scene, node, index) -> (gate, old prefix, new).
# The gate is the paragraph's (Requires, Forbids) and must still match.
# ---------------------------------------------------------------------------
REVOICE = {
    (D + "epilogue.woken", "page", 13): (
        ([T + "one_battle_sold", T + "battle_price_accepted"], []), "{n}The generals still had no battle",
        "{n}Devarra never flew the battle the generals had bought. The war, she said, had never once been worth her wings, so "
        "there was no story of every death in it to collect, and she took the difference out of the generals instead, as she "
        "had promised: a horse off the staff picket line every week until the march to Threshold. The general who had thrown "
        "the inkwell climbed the ridge to complain. That one came down without boots, and never climbed again.{/n}"),
    (D + "epilogue.woken", "page", 20): (
        ([BILL, "nidalynn.trickster.hatched"], ["nidalynn.trickster.left_with_it"]), "{n}The silver kept the smallest",
        "{n}The silver kept the smallest of Devarra's clutch by the east wall. When the child could fly she came up the ridge "
        "on her own wings. Devarra counted her, made room on the sill, and taught her to take a goat off the east road in one "
        "stoop while the silver shouted from the wall. The child was hers. What the thief owed for carrying her off was owed "
        "all the same.{/n}"),
    (D + "epilogue.woken", "page", 26): (
        ([BILL], ["nidalynn.trickster.left_with_it", "nidalynn.trickster.hatched"]), "{n}The smallest shell remained",
        "{n}The smallest shell stayed in the silver's keeping by the east wall, and did not hatch while the war lasted. "
        "Devarra flew over it every evening, low enough to set the kiln smoke spinning, and never once landed. What the "
        "thief owed for carrying it off was owed whether it hatched or not.{/n}"),
    (D + "epilogue.woken", "page", 29): (
        ([T + "battle_offered"], [T + "battle_price_accepted"]), "{n}Devarra had offered one battle",
        "{n}Devarra had offered one battle: where she chose, when she chose, unannounced and unthanked. The generals waited "
        "for word and got none. In the last weeks before Threshold the scouts found a demon column on the Wound side of the "
        "supply road burned where it stood, a mile of it, the stones too hot to cross for a day. The dispatch said the cause "
        "was unknown. Nobody thanked her. She was on her ridge, eating, and would have bitten anyone who tried.{/n}"),
    (D + "epilogue.woken", "page", 31): (([BILL, CALLED], []), "{n}She had never named what she would take", NAMED),
    (D + "epilogue.woken", "page", 32): (([BILL], [CALLED]), "{n}She had never named what she would take", NEAREST),
    (D + "epilogue.commit", "late_accepted", 0): (
        (["lastcall.active"], []), "{n}Before the march, Devarra had come for the answer herself.",
        "{n}She had come down to the road outside Drezen for that answer before the march, and blocked the supply carts "
        "until she got it. Threshold changed nothing she had been promised. She said she would have come into the Wound to "
        "collect, if it had.{/n}"),
    ("devarra.lastcall.page", "page", 0): (
        ([CALLED, BILL], []), "{n}The grey dragon still held her bill",
        "{n}The Commander had said her name at the rift, and the debt for the smallest egg with it. That was an answer, not "
        "a payment. She named the price herself afterwards, on her ridge, the way she had said she would: a month of the "
        "Commander's every year. Whether there was a Commander left to pay it was the Commander's problem, not hers.{/n}"),
    ("devarra.lastcall.page", "page", 1): (
        ([D + "cost.bitten"], []), "{n}The tariff was collected every year",
        "{n}The tariff was collected every year on the same night, in a ring of fire, where she chose. By the end the "
        "Commander's forearm was a ladder of pale crescents from wrist to elbow, and she could tell anyone who asked exactly "
        "how many rungs it had.{/n}"),
}

# Nidalynn's pages (she owns the voice; only the claim about Devarra is aligned).
NIDALYNN_SUBS = [
    ("{n}At the rift the grey dragon named her bill for the smallest egg, and it was not the hatchling and not the silver who "
     "raised her. It was a month of the Commander's every year, on her ridge.{/n}",
     "{n}The Commander answered the woundwyrm's bill for the smallest egg at the rift. Whatever she named for it, it would "
     "not be the hatchling, and it would not be the silver who raised her; Nidalynn made very sure of that before the "
     "spring.{/n}", 7),
    ("The grey one had named her bill at Threshold: a month of the Commander's every year. Before the first journey, "
     "Nidalynn heard the account at her own fire.",
     "The Commander had answered the woundwyrm's bill at Threshold, and whatever she named for it, the Commander would "
     "pay it, not the child. Before the first climb, Nidalynn heard the account at her own fire.", 1),
]

# ---------------------------------------------------------------------------
# Appended read-only consumers: (scene, node) -> [paragraph].
# ---------------------------------------------------------------------------
APPEND = {}
APPEND[(D + "epilogue.woken", "page")] = [
    when((BILL, T + "twelfth_lied"),
         "{n}She had added the Commander's lie about the twelfth egg to the debt, as she had promised. Every spring, before "
         "anything else, she made the Commander say how many eggs there had been. The answer was twelve now. She made the "
         "Commander say it twice.{/n}"),
    when((T + "coin_stolen",),
         "{n}The Queen of Iobaria stayed in the Commander's sleeve for the rest of the war. At every appointment Devarra asked "
         "to see her, turned her over with one claw, and gave her back, the way a cat gives back a mouse it has not finished "
         "with.{/n}"),
    when((T + "vault_refused", "eggs.project"),
         "{n}She never got into the Drezen vault. She lay against its outside wall every night of the war instead, close "
         "enough to hear the shells, and when the clutch hatched into the crusade's hands she was at that wall, and nobody on "
         "that stretch of the battlements slept for a week.{/n}",
         forbids=(T + "vault_opened", "eggs.omelet", "eggs.druids", "eggs.destroyed")),
    when((T + "looked_away",),
         "{n}She never took the Commander to the Wound's edge again to watch her work. A thing that looked away once, she "
         "said, did not get shown twice.{/n}"),
    when((PAIR + "resolved", "nidalynn.trickster.hatched", "crossroute.nidalynn.available"),
         "{n}She knew what the silver fed her daughter: goat, cut small, so that the child would not learn the taste of "
         "soldiers. The first spring after the war Devarra left a deserter from the Mendevian line at the kiln door, alive, "
         "with both legs broken, and flew off before the silver could open it. Nidalynn let him crawl away. The next spring "
         "there was another.{/n}",
         forbids=("nidalynn.trickster.left_with_it",)),
]
# epilogue.commit: the late acceptance reads the same history as the ordinary page (copied after the re-voice).
COMMIT_COPIES = (0, 1, 2, 3, 4, 5, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32)
APPEND[(D + "epilogue.pending", "page")] = [when((BILL, CALLED), NAMED_UNBOUND), when((BILL,), NEAREST, forbids=(CALLED,))]
APPEND[(D + "epilogue.hungry", "page")] = [when((BILL, CALLED), NAMED_UNBOUND), when((BILL,), NEAREST, forbids=(CALLED,))]
APPEND[(D + "epilogue.claimed", "page")] = [when((BILL, CALLED), NAMED_FAR), when((BILL,), NEAREST, forbids=(CALLED,))]
APPEND[(D + "epilogue.refused", "page")] = [when((BILL,), UNCOLLECTED)]
# Five tower readers (before_the_end/climb, the_dwarf/protect, the_hoard/{honest,steal,ask}_her) were removed
# 2026-10-08: tower scenes are inline (NativeReturnCue) and cannot carry gated paragraphs. Their text waits in
# claude-work-queue.json (git history of this file) for gated host nodes (structure).



def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    scene = scenes.get(sid)
    if scene is None:
        raise ValueError(f"devarra cloud: missing scene {sid}")
    for node in scene["Nodes"]:
        if node["Id"] == nid:
            return node
    raise ValueError(f"devarra cloud: missing node {sid}:{nid}")


def _gate(paragraph):
    return (sorted(paragraph.get("Requires", [])), sorted(paragraph.get("Forbids", [])))


def _optional(scenes, sid):
    """The S50 rows exist only when the harem rows are registered (test fixtures build without them)."""
    return sid.startswith(PAIR) and sid not in scenes


def apply(payload):
    scenes = _scenes(payload)
    for (sid, nid), (old, new) in NODES.items():
        node = _node(scenes, sid, nid)
        if node["Text"] != new:
            if not node["Text"].startswith(old):
                raise ValueError(f"devarra cloud: {sid}:{nid} text changed upstream")
            node["Text"] = new
    for (sid, nid), pairs in SUBS.items():
        if _optional(scenes, sid):
            continue
        node = _node(scenes, sid, nid)
        for old, new in pairs:
            if new in node["Text"]:
                continue
            if old not in node["Text"]:
                raise ValueError(f"devarra cloud: {sid}:{nid} missing {old[:50]!r}")
            node["Text"] = node["Text"].replace(old, new)
    for (sid, nid, index), (old, new) in CHOICES.items():
        if _optional(scenes, sid):
            continue
        choice = _node(scenes, sid, nid)["Choices"][index]
        if choice["Text"] not in (old, new):
            raise ValueError(f"devarra cloud: {sid}:{nid}>{index} choice text changed upstream")
        choice["Text"] = new
    for sid, fields in FIELDS.items():
        scene = scenes[sid]
        for key, (old, new) in fields.items():
            if scene.get(key) not in (old, new):
                raise ValueError(f"devarra cloud: {sid} {key} changed upstream")
            scene[key] = new
    for (sid, nid, index), ((requires, forbids), old, new) in REVOICE.items():
        paragraph = _node(scenes, sid, nid)["Paragraphs"][index]
        if _gate(paragraph) != (sorted(requires), sorted(forbids)):
            raise ValueError(f"devarra cloud: {sid}:{nid}#{index} gate changed upstream")
        if paragraph["Text"] != new:
            if not paragraph["Text"].startswith(old):
                raise ValueError(f"devarra cloud: {sid}:{nid}#{index} text changed upstream")
            paragraph["Text"] = new
    for old, new, minimum in NIDALYNN_SUBS:
        hits = 0
        for scene in payload["Scenes"]:
            if not scene["Id"].startswith("nidalynn."):
                continue
            for node in scene["Nodes"]:
                for paragraph in node.get("Paragraphs") or []:
                    if old in paragraph["Text"]:
                        paragraph["Text"] = paragraph["Text"].replace(old, new)
                        hits += 1
        if hits < minimum:
            raise ValueError(f"devarra cloud: Nidalynn page claim {old[:40]!r}: {hits} < {minimum}")
    woken = _node(scenes, D + "epilogue.woken", "page")
    commit = _node(scenes, D + "epilogue.commit", "page")
    for (sid, nid), extra in APPEND.items():
        target = _node(scenes, sid, nid).setdefault("Paragraphs", [])
        for paragraph in extra:
            if paragraph not in target:
                target.append(deepcopy(paragraph))
    history = [woken["Paragraphs"][i] for i in COMMIT_COPIES] + APPEND[(D + "epilogue.woken", "page")]
    for paragraph in history:
        if paragraph not in commit["Paragraphs"]:
            commit["Paragraphs"].append(deepcopy(paragraph))
    for scene in payload["Scenes"]:
        if scene["Id"].startswith(("devarra.", PAIR, "trickster.lastcall.account.devarra")):
            for node in scene["Nodes"]:
                texts = [node.get("Text", "")] + [x.get("Text", "") for x in node.get("Paragraphs") or []]
                if ((scene['Id'], node['Id']) not in {
                        (D + 'epilogue.claimed_unjudged', 'page'),
                        (T + 'the_hoard', 'climb_checked'),
                        (T + 'the_hoard', 'climb_noticed')}
                        and any(PENDING in t for t in texts)):
                    raise ValueError(f"devarra cloud: prose pending left in {scene['Id']}:{node['Id']}")


def integrate(payload):
    apply(payload)
    from storylines import devarra_rubric2
    devarra_rubric2.integrate(payload)
    from storylines.devarra_round2 import keeper_history
    scenes = {s['Id']: s for s in payload['Scenes']}
    for suffix in ('epilogue.woken', 'epilogue.commit'):
        sid = D + suffix
        keeper_history(_node(scenes, sid, 'page'), sid)
