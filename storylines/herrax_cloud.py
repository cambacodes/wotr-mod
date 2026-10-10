"""Herrax's appended promise and household outcome readers.

Approved text is authored in herrax_trickster, herrax_house, and S48. Readers
append after existing paragraphs, keeping their registered indices.
"""
import copy

from story_format import p

H = "herrax."
T = H + "trickster."
L = H + "letters."
B = H + "house."
PAIR_C = "household.pair.herrax_chivarro."
PAIR_M = "household.pair.herrax_minagho."
CHIV = "crossroute.chivarro.available"
MINA = "crossroute.minagho.available"
MOREVET_DEAD = "herrax.morevet_dead"
PENDING = "[PROSE PENDING:"

REVIEWED_SCENES = ['herrax.lastcall.page', 'herrax.letters.the_courier', 'herrax.trickster.epilogue.after_hours', 'herrax.trickster.epilogue.after_hours.invitation', 'herrax.trickster.epilogue.reachable']


# The household pair outcomes Herrax is party to, read by both of her living endings.
PAIR_READERS = (
    p('''{n}The terms with Chivarro held, season after season, which surprised both madams. Each sent the other her worst customers, and each called it a gift.{/n}''',
      requires=(PAIR_C + "herrax_turf_terms_kept", CHIV)),
    p('''{n}Chivarro's girls kept walking up the Delights' stairs on their own. Herrax put them in the cheapest rooms under their old names, and charged Chivarro's old regulars double to visit them.{/n}''',
      requires=(PAIR_C + "herrax_term_broken", CHIV)),
    p('''{n}Chivarro never stopped saying the chair was hers. Herrax kept a knife under the cushions that still smelled of her, and told guests it was there for the day Chivarro came to collect.{/n}''',
      requires=(PAIR_C + "chivarro_term_broken", CHIV), forbids=(PAIR_C + "herrax_term_broken",)),
    p('''{n}Nothing was ever agreed between the two madams. Herrax sat in Chivarro's old chair and Chivarro in her new house, and each waited to see which of them had the better knives. Neither found out, and Herrax counted that a win.{/n}''',
      requires=(PAIR_C + "unsettled", CHIV),
      forbids=(PAIR_C + "herrax_term_broken", PAIR_C + "chivarro_term_broken", PAIR_C + "resolved")),
    p('''{n}The knives Herrax had hired for Chivarro never came home. She had cancelled them herself, a ring, a bootlace and a tooth at a time, and she never once complained of the expense where Minagho could hear it.{/n}''',
      requires=(PAIR_M + "settled", MINA)),
    p('''{n}Minagho's hunters and Herrax's boys kept finding each other on the road out of the rift. Herrax replaced every boy she lost and sent Minagho the bill for each one. Minagho sent back the boy's teeth.{/n}''',
      requires=(PAIR_M + "unsettled", MINA), forbids=(PAIR_M + "settled",)),
)

# Ch4-committed ending: unread choices the route set and promised something for.
REACHABLE_READERS = (
    p('''{n}Rokhorn waited a long time for the Commander to finish thinking about his offer. When he finally asked again, on the stair, in front of the whole hall, the Commander laughed in Rokhorn's face, and Herrax had the other side of it opened to match before the laugh was done. Late answers, she told the house, cost double in the Delights.{/n}''',
      requires=(L + "offer.strung_along",)),
    p('''{n}Herrax kept the Commander's filthy letter about the dais. On slow nights she had Rokhorn read it aloud to the hall, slowly and with feeling, while the guests bid for the right to make him start again.{/n}''',
      requires=(L + "reply.crude",)),
    p('''{n}"I miss your stairs," the Commander had written from the war. Herrax had the line cut into the top step of her private stair, and charged the Upper City a silver a head to stand on it.{/n}''',
      requires=(L + "reply.warm",)),
    p('''{n}"The war goes on. So do I." Herrax had it read out at the bar as the cheapest letter ever sent up her stairs, and fined any girl who wrote her own soldier a longer one.{/n}''',
      requires=(L + "reply.cool",)),
    p('''{n}When kings asked the madam's price, Herrax told them forty-one thousand, and never explained the one. The Commander was the only guest who never had to ask.{/n}''',
      requires=(B + "priced.forty_one",)),
    p('''{n}Every year or so she told the Commander a new story about the eye, asked which of them was true, and laughed at every answer the Commander gave.{/n}''',
      requires=(B + "eye.asked",)),
    p('''{n}The ram's-head signet the Commander would not wear went to a guest who was less particular. Herrax made sure the Commander saw it on the guest's hand one spring, and on her tray the next, finger and all.{/n}''',
      requires=(B + "ring.refused",)),
) + PAIR_READERS

# Late-committed ending: the doorstep answer about Chivarro, given on the late road.
AFTER_HOURS_READERS = (
    p('''{n}Rokhorn had carried home the Commander's word that Chivarro would keep out of the Delights. Herrax bit it, as he had said she would, and found it held. Chivarro never set foot on her stairs, and once a year Herrax sent Drezen a bottle of the house's worst wine, without a note.{/n}''',
      requires=(T + "contract.kept_out", CHIV)),
    p('''{n}Rokhorn had carried home the Commander's answer that Chivarro went where she liked. Herrax kept a knife for her after that, the way she kept a room for the Commander: both ready. Neither was used, which she called the Commander's doing and held against the Commander for years.{/n}''',
      requires=(T + "contract.stood_by_her", CHIV)),
) + PAIR_READERS

# The late return: the crusade's 500 paid to Rokhorn on the doorstep.
INVITATION_READERS = (
    p('''{n}Before the cutting, Herrax had Rokhorn's purse emptied on her bar. The crusade's five hundred was still in it. She counted it out in front of him and kept every coin. "Paid on my stairs, kept on my stairs," she told the Commander, and did not offer it back.{/n}''',
      requires=(T + "late.paid_his_price",),
      forbids=(T + "bait_taken", T + "cost.con_blown", T + "lesson_given")),
)

APPEND = [
    (T + "epilogue.reachable", "page", REACHABLE_READERS),
    (T + "epilogue.after_hours", "page", AFTER_HOURS_READERS),
    (T + "epilogue.after_hours.invitation", "arrival", INVITATION_READERS),
]


def _node(scenes, sid, nid):
    scene = scenes.get(sid)
    if scene is None:
        raise KeyError("herrax cloud: missing scene " + sid)
    matches = [n for n in scene["Nodes"] if n["Id"] == nid]
    if len(matches) != 1:
        raise KeyError("herrax cloud: %s/%s matched %d nodes" % (sid, nid, len(matches)))
    return matches[0]


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for sid, nid, paras in APPEND:
        node = _node(scenes, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [copy.deepcopy(x) for x in paras]
    for sid in set(REVIEWED_SCENES) | {row[0] for row in APPEND}:
        for node in scenes[sid]["Nodes"]:
            texts = [node["Text"]] + [a["Text"] for a in node["Choices"]] + [
                para["Text"] for para in node.get("Paragraphs", [])]
            if any(PENDING in t for t in texts):
                raise ValueError("herrax cloud: prose still pending at %s/%s" % (sid, node["Id"]))
            if any("Morevet" in para["Text"] and MOREVET_DEAD not in para.get("Forbids", [])
                   for para in node.get("Paragraphs", [])):
                raise ValueError("herrax cloud: unguarded Morevet paragraph at %s/%s" % (sid, node["Id"]))
