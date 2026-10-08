"""Herrax: cloud voice-owner pass (villain-route-herrax, design-first).

Applied last in expansion._make_expansion, after every route, harem row, Last Call
partner and engine appender, so the paragraphs it appends never shift an index
another pass registers. Text and flag-gated paragraphs only: no scene, node or
choice id, choice position, Next, Set, gate, check, cost or GuidFor changes.
Review and truth table: tools/route_packs/redesign/herrax/cloud-review.md,
truth-table.json.

Structure fixed here (read-only consumers of flags the route already sets):
  * costs and promises with no reader: the crusade's 500 paid to Rokhorn on the
    Drezen doorstep (late.paid_his_price), Rokhorn's renewed offer left open
    ("Let me think about it", letters.offer.strung_along), the Commander's three
    letter replies (letters.reply.*), the "forty-one" appraisal, the eye asked a
    third time, the dead man's ring refused;
  * the late road's answer about Chivarro (trickster.contract.kept_out /
    stood_by_her, given at the Ch5 doorstep) was read only by the Ch4 ending;
    the late ending now reads it;
  * the household pair outcomes Herrax is party to (household.pair.herrax_chivarro.*,
    household.pair.herrax_minagho.*) were read by no Herrax ending;
  * branch-false text: the coin "never left her bodice" on the branch where the
    Commander lost it before the night; "He had paid on account" on the branch
    where the Commander paid Rokhorn; Rokhorn "for the first time speaks" after
    he has already spoken three times in the same packet;
  * one debt paid twice the same way: the Battlebliss thousand and the Chivarro
    favour ("When I call, you won't ask what") were both a night behind her bar;
    the favour is now collected as what she said it was;
  * Last Call's truce line was a withdrawal of "inducements", contradicting the
    merged pair scene, where she cancels her hired knives by killing them.

Prose that failed CHARACTER-TRUTH 2/12 (menace by report) is rewritten: the late
return's "she had described the cutting in her letter" / "reported it in her
letter" lines are staged in the hall at the Commander's return; the late ending
no longer sends the Commander back to a finished crusade.

Canon used (writer knowledge/characters/herrax/native-lines.json and the
Herraxa_dialogue cues quoted in voice.md): 360e6e7f (the haggle, "insolent
bitch"), a776e081 (the curse), Cue_0052 (rings cut off with the fingers),
Cue_0097 (beyond anyone's reach), Cue_0064 (scars as a reminder for others).
Authored, no canon claim: as in herrax_trickster / herrax_house.
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

# (scene, node, paragraph index or None for node text, substring the reviewed text contains, new text)
RETEXT = [
    # The coin: true on every branch, including the con blown with the coin already gone.
    (T + "epilogue.reachable", "page", 6, "The golden coin never left her bodice.",
     '''{n}She never gave out another golden coin. The arches of Alushinyrra never carried the Commander to the Delights again, and the Commander always came anyway, up the stairs, like everyone else, and without paying, like no one else.{/n}'''),
    # The Chivarro favour, collected as she priced it, not as a second bar shift.
    (T + "epilogue.reachable", "page", 16, "She announced the repayment of her favour",
     '''{n}Herrax called in her favour from the matter of Chivarro's body the first spring after the war. A guest from the Upper City had tried to leave without paying. She had the Commander pin the guest's wrist flat on the bar while she took two of the guest's fingers for the tray, and explained the price to neither of them. "When I call, you won't ask what," she had said. The Commander didn't. She told the whole bar the favour was paid, and wiped the knife on the guest's sleeve.{/n}'''),
    (T + "epilogue.after_hours", "page", 1, "for the favour owed over Chivarro's body",
     '''{n}On another night she called in her favour from the matter of Chivarro's body: a guest who had tried to leave without paying, pinned to her bar by the wrist under the Commander's hand, and two fingers off that hand for her tray. The Commander did not ask what the price was for. That was the price.{/n}'''),
    # The late ending: a postwar page, not a report of the invitation.
    (T + "epilogue.after_hours", "page", None, "Herrax's returning guest stayed at closing",
     '''{n}Herrax kept her rooms in the Ten Thousand Delights long after the war, and kept herself beyond anyone's reach, as she always had, with one exception, who came back up her stairs a season late and stayed for closing. By noon the whole house knew who had slept in her bed without paying; she made sure it did.{/n}
{n}After that the Commander came back to the Isles whenever the world allowed, up the stairs like everyone else, and without paying, like no one else. The rest of her house still charged by the night, and she still took her share.{/n}'''),
    # The late return: the seller's bargain, true on both doorstep branches.
    (T + "epilogue.after_hours.invitation", "arrival", 0, "He had paid on account on a Drezen doorstep",
     '''{n}Rokhorn had been waiting all winter for the seller he had bargained with on a Drezen doorstep, and he had never once looked closely at what he had bought. Herrax named the night, and the Commander delivered it to Rokhorn over a cup of the incubus's wine, with a gold coin she had pressed into the Commander's palm for the purpose; every word of it was true except who would be waiting. After midnight the girl who kept the arch took Rokhorn up the back stair carrying the coin. Her people filled the room. Herrax cut Rokhorn from lip to cheekbone; the Commander stood at the front and watched.{/n}'''),
    # The late return: punishments already done are staged in the hall, not reported by letter.
    (T + "epilogue.after_hours.invitation", "arrival", 6, "Herrax had described the cutting in her letter.",
     '''{n}Rokhorn brought the wine with his scar on show, the one she had given him up her back stair the night after the Commander left the Isles. She made him hold the tray while she looked her returning guest over, and then made him tell the Commander how it had gone, every word, while the girls on the couches listened. "You missed my performance, lover," she said when he had finished. "Stay for closing this time."{/n}'''),
    (T + "epilogue.after_hours.invitation", "arrival", 7, "as her letter promised to remind the absent seller",
     '''{n}Rokhorn had shouted the Commander's lie off every couch in the Delights before the Commander left the Isles, and Herrax had cut him anyway, under the lamps, with the seller nowhere in the hall. Now he brought the wine and stood where the whole house could compare his scar with the claw mark on the Commander's cheek. Herrax caught her guest by the chin and inspected the mark. "He was here for his lesson. You ran off to your war. Tonight you stay."{/n}'''),
    (T + "epilogue.after_hours.invitation", "arrival", 8, "reported it in her letter",
     '''{n}The Commander had given her knife back before the Sinners and left the Isles before she used it. She had performed her delayed punishment the next night, with the hall full and the back of it empty. Now she tapped the bone sheath as her guest came up the stairs, and had Rokhorn turn his face to the lamp so the Commander could see what had been missed. "You gave it back. I used it. This time, lover, you will be here when I decide what I want."{/n}'''),
    # Last Call: the truce as the merged pair scene stages it.
    (H + "lastcall.page", "page", 5, "Herrax withdrew every inducement she controlled",
     '''{n}The knives Herrax had hired for Chivarro were long cancelled, a ring, a bootlace and a tooth at a time, and she hired no new ones while she waited for the news. She kept the Delights' chair and lost only the pleasure of promising Chivarro's head.{/n}'''),
    # The packet: Rokhorn has already spoken at the court answers; this is the first time he speaks to the Commander.
    (L + "the_courier", "reply", None, "and for the first time speaks.",
     '''{n}Rokhorn takes your answers between two claws and tucks them away without looking at them. At the door he stops, and turns his ruined face toward you, and speaks to you instead of about the letters.{/n}
"Hello, hot stuff." {n}The raw scar pulls. He does not smile.{/n} "Every word of it was true, you know. That's what I can't stop thinking about."'''),
]

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
    for sid, nid, index, old, new in RETEXT:
        node = _node(scenes, sid, nid)
        target = node if index is None else node.get("Paragraphs", [])[index]
        if old not in target["Text"]:
            raise ValueError("herrax cloud: %s/%s#%s no longer reads %r" % (sid, nid, index, old))
        target["Text"] = new.strip()
    for sid, nid, paras in APPEND:
        node = _node(scenes, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [copy.deepcopy(x) for x in paras]
    for sid in {row[0] for row in RETEXT} | {row[0] for row in APPEND}:
        for node in scenes[sid]["Nodes"]:
            texts = [node["Text"]] + [a["Text"] for a in node["Choices"]] + [
                para["Text"] for para in node.get("Paragraphs", [])]
            if any(PENDING in t for t in texts):
                raise ValueError("herrax cloud: prose still pending at %s/%s" % (sid, node["Id"]))
            if any("Morevet" in para["Text"] and MOREVET_DEAD not in para.get("Forbids", [])
                   for para in node.get("Paragraphs", [])):
                raise ValueError("herrax cloud: unguarded Morevet paragraph at %s/%s" % (sid, node["Id"]))
