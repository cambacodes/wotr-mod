"""villain-route-elyanka (cloud voice owner, 2026-10-08): Elyanka Camilary's late text-only layer.

Runs after every appender (expansion.make_expansion, last), so paragraph indices registered elsewhere stay put: it only
replaces text in place and appends flag-gated read-only paragraphs after the existing ones. No id, node, choice, Next,
Set, gate, check or cost changes, except one Ledger display line (book lines carry no save identity). Every target must
resolve or the build stops. Review and evidence: tools/route_packs/redesign/elyanka/cloud-review.md.

Native register (writer knowledge/characters/elyanka/voice.md): she cackles, hisses and shrieks (fa330470, f3be11dc),
threatens in ritual terms ("a death even more painful than the one I have already prepared for you", fa330470), and the
Way's teaching is told, never written (Cue_0061 98312252).
"""
from story_format import p

E = "elyanka.trickster."

MISLED = E + "inquiry.misled"
TABLE_LEFT = E + "table.left"
TOLD_HER = E + "tyrant.told_her"
ANATOMY_LEFT = E + "anatomy.left"
WOODS = E + "ustalav.woods"
US_REFUSED = E + "ustalav.refused"
FIT_REFUSED = E + "fitting.refused"
HUNT_HELD = E + "hunt.held"
HUNT_GORED = E + "hunt.gored"


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(payload, sid, nid):
    scene = _scenes(payload).get(sid)
    if scene is None:
        raise KeyError("elyanka_cloud: missing scene " + sid)
    for node in scene["Nodes"]:
        if node["Id"] == nid:
            return node
    raise KeyError("elyanka_cloud: missing node %s/%s" % (sid, nid))


def _swap(payload, sid, nid, old, new):
    node = _node(payload, sid, nid)
    if node["Text"].count(old) != 1:
        raise ValueError("elyanka_cloud: anchor not found once in %s/%s: %r" % (sid, nid, old[:60]))
    node["Text"] = node["Text"].replace(old, new)


def _rewrite(payload, sid, nid, starts, new):
    node = _node(payload, sid, nid)
    if not node["Text"].startswith(starts):
        raise ValueError("elyanka_cloud: unexpected text in %s/%s" % (sid, nid))
    node["Text"] = new.strip()


def _answer(payload, sid, nid, index, old, new):
    choice = _node(payload, sid, nid)["Choices"][index]
    if choice["Text"] != old:
        raise ValueError("elyanka_cloud: unexpected answer %s/%s>%d" % (sid, nid, index))
    choice["Text"] = new


def _paragraphs(payload, scene_ids, table):
    """Replace whole paragraph texts (same gates) wherever they occur in the named scenes; every entry must be used."""
    used = set()
    scenes = _scenes(payload)
    for sid in scene_ids:
        if sid not in scenes:
            raise KeyError("elyanka_cloud: missing scene " + sid)
        for node in scenes[sid]["Nodes"]:
            for para in node.get("Paragraphs") or []:
                if para["Text"] in table:
                    used.add(para["Text"])
                    para["Text"] = table[para["Text"]]
    missing = set(table) - used
    if missing:
        raise ValueError("elyanka_cloud: paragraph text not found: %r" % sorted(missing)[0][:80])


def _append(payload, sid, nid, paragraphs):
    _node(payload, sid, nid).setdefault("Paragraphs", []).extend(paragraphs)


def _ledger_entry(payload, entry_id):
    for entry in payload.get("Books", {}).get("trickster.ledger", {}).get("Entries", []):
        if entry["Id"] == entry_id:
            return entry
    raise KeyError("elyanka_cloud: missing Ledger entry " + entry_id)


# --- S1 / ELY-AUD-01: held for Claude; aftermath alone does not establish an on-screen death -------------------------

KILL2 = '[PROSE PENDING: ELY-AUD-01 show the master being killed on screen; retain Elyanka ownership motive and master.killed outcome.]'
MASTER_KILL = '[PROSE PENDING: ELY-AUD-01 authorized violent counter-move against her order; stage dispatch and the on-screen death without a dialogue-click journey.]'
MASTER_HERS = '[PROSE PENDING: ELY-AUD-01 delegated violent counter-move on screen; retain her agency and the distinct master.hers outcome.]'


# --- V1: the embalmer lie answered in her native register (fa330470: the shriek, the hiss, the prepared death) ---------

LIED2 = '''{n}She waits until the gate has closed behind them. Then she turns on you, and she does not lower her voice; she lets it climb until the horses stamp in the yard.{/n}
"Your *embalmer*!" {n}It comes out of her as a shriek, and then as a hiss.{/n} "I am a matriarch priestess of the Pallid Princess and a noblewoman of the Immortal Principality, and you have made me your servant in front of a clerk!" {n}She steps close enough that her breath is cold on your chin.{/n}
"It worked. I grant you that. A small, cheap, clever lie, and it worked." {n}One cackle, with no pleasure in it at all.{/n} "Tell it again, Commander. Make me anybody's servant once more, in front of anybody, and I promise you a death more painful than the one I have already measured you for. I will take my time over the fitting."'''

# --- S7 / work-queue D08: the driven hart (the old interception moved to the checked answer) -------------------------

KILL_QUICK = '''{n}You go crashing through the brush on his flank, shouting like a beater, and he breaks from you the only way left: across the clearing, straight at her. She does not step aside. She lets him come the last three strides, and the knife goes in under his jaw as he reaches her, and the weight of him nearly takes her off her feet.{/n}
{n}She holds his head against her body while he dies. Then she looks at you, flushed and breathless and scratched to the elbows by the thorns, and laughs out loud.{/n} "Useful after all. You bark very well, for a crusader."'''

# --- S3: the bottled-death and death-notice consequences as scenes, not a property dispute ----------------------------

BOTTLED = {
    # elyanka.trickster.epilogue.claim / .debt (endings1, gates unchanged)
    "{n}The death notice made Elyanka present her bequest. The returned body was living; possession was refused. She kept the claim contested, and watched the corked flask without pretending it erased the death.{/n}":
    "{n}When the death notice came, Elyanka came for the body. It was living, and it refused her. She did not withdraw the claim; she never withdrew anything in her life. After that she watched the corked flask whenever the Commander came to the dead-house, the way a cat watches a stopped hole, and swore she could smell the death through the wax.{/n}",
    "{n}Elyanka examined the stranger behind closed curtains. The flask was empty and the death remained in Pharasma's book. She had demanded her corpse; no corpse had been delivered. She kept the bequest contested and the stranger's name to herself.{/n}":
    "{n}Elyanka went over the stranger behind drawn curtains, by one candle, with her cold fingers: the empty flask, the warm throat, the death still standing in Pharasma's book. She had been promised a corpse and handed a riddle. She kept the claim, and the stranger's name, to herself. A secret was worth more to her than meat she could not yet eat.{/n}",
    # elyanka.lastcall.page (lastcall_partners history paragraphs 4, 6, 9; gates unchanged)
    "{n}The Commander had died at Threshold. Elyanka presented her bequest when the living body returned. She was refused possession: there was no corpse to hand over. She contested it, furious at having a death notice and breathing collateral. The cork did not erase her claim.{/n}":
    "{n}The Commander had died at Threshold, and came back breathing. Elyanka was at the door when the living body was carried in, with the hearse in the street and her six behind her, come to take what had fallen due. There was nothing to take. She laid two cold fingers on the Commander's throat in front of the whole hall, found the pulse, and shrieked at it like a cheated fishwife; then she laughed until she had to sit down. \"Dead, and sweating,\" she said. \"The cork changes nothing. The death is in her book, and the body is still mine when it stops.\"{/n}",
    "{n}The Commander's death notice reached Elyanka. She demanded the body and found the coffin empty. She refused to withdraw the bequest: someone had kept her collateral from her, and she intended to learn who.{/n}":
    "{n}The Commander's death notice reached Elyanka in the dead-house, and she had the hearse at the chapel before the bell stopped. She tore the lid off the coffin with her own hands and found it empty. Nobody in the chapel would say where the body had gone. She named the chaplains to their faces, one by one, and promised each of them that she would learn who had kept her collateral from her, and what they tasted like.{/n}",
    "{n}In private Elyanka inspected the returned body and the empty flask. The death remained in Pharasma's book. \"A death proved, and no corpse delivered,\" she said. She kept her claim contested; she did not report the stranger to Drezen.{/n}":
    "{n}Elyanka had the returned body brought to the dead-house behind drawn curtains and went over it by candlelight, the empty flask on the trestle beside it. The death was in Pharasma's book; the body was warm. \"Proved dead, and still not on my table,\" she said, and laughed until the candle guttered. She told nobody in Drezen who the stranger was. A secret kept was a debt owed her, and she liked those better than meat.{/n}",
}

# Last Call collectors page: her three paragraphs only (gated on elyanka.lastcall.called). The collector is Elyanka, not
# a "he", and the Way keeps nothing "on file".
COLLECTORS = {
    "{n}The Whispering Way demanded the body named in the death notice. Its collector was shown a living Commander and refused possession. He returned to Caliphas with the bequest still disputed.{/n}":
    "{n}The Whispering Way came for the body named in the death notice: Elyanka Camilary, with the hearse and her six. She was shown a living Commander, and put two cold fingers to the throat in front of everyone to be sure of it. She left without her corpse and without giving up one whispered word of the claim.{/n}",
    "{n}The Whispering Way demanded the body named in the death notice. The coffin was empty. Its collector left without the concealed stranger's name, and without withdrawing the bequest.{/n}":
    "{n}The Whispering Way came for the body named in the death notice, and Elyanka Camilary tore open an empty coffin. She left without the concealed stranger's name, and without withdrawing one whispered word of the bequest.{/n}",
    "{n}No death had made the whispered bequest payable. The Way's collector examined the sealed flask and left the living Commander to wait. The bequest remained on file in Caliphas.{/n}":
    "{n}No death had made the whispered bequest payable. Elyanka weighed the sealed flask in her palm, sniffed at the wax, and gave it back to the living Commander to carry. The bequest stayed where the Way keeps such things: unwritten, in the ears of the people who had heard it.{/n}",
}

# --- S4: the inquiry outcomes as what the women did, not as a filing report --------------------------------------------

INQUIRY = {
    "{n}The Commander remembered Seelah hearing the truth about the sixty-one from the mouth that had ordered their removal. The count went to the chaplains; a witness stood at the dead-house door. Elyanka had stayed out of the paladin's road.{/n}":
    "{n}Seelah heard the truth about the sixty-one from the Commander's own mouth, on the chapel steps, and never again asked the Commander to help her find anything. After that a young crusader with a lamp stood at the dead-house door whenever the carts came in. Elyanka stayed out of the paladin's road. She whispered the lamp-bearer's name to her Lady every seventh night instead, as a grace before meat, so that her Lady would know him when he came.{/n}",
    "{n}A resurrection man hanged at the south gate of Drezen for sixty-one bodies he never touched. The Commander remembered Seelah blocking the gallows steps with the carters' testimony, and the watch forcing her down under the Commander's seal. The Commander's order had kept her from stopping the carts, not from recording who sent them. The chaplains received the testimony; a witness stood at the dead-house door.{/n}":
    "{n}A resurrection man hanged at the south gate of Drezen for sixty-one bodies the man had never touched, with a placard on the dead man's chest and the Commander's seal on the sentence. Seelah had stood on the gallows steps with the carters' word in her fist until the watch shoved her down them, and after that she put a crusader with a lamp at the dead-house door and never believed the Commander again. When they cut the hanged man down nobody claimed him but Elyanka. He went south in the hearse, past the lamp, and Seelah watched him go.{/n}",
    "{n}Elyanka told the paladin the truth about the sixty-one herself, in the dead-house yard, without one lie. The Commander remembered Seelah refusing the excuse that the dead could not suffer. She had taken the names and count to the chaplains and put a witness at the dead-house door. Neither culprit had received her forgiveness.{/n}":
    "{n}Elyanka told the paladin the truth about the sixty-one herself, in the dead-house yard, without one lie, and enjoyed every word of it. Seelah did not draw. She would not hear that the dead could not suffer, and she forgave neither of them, and from that day a crusader with a lamp stood at the dead-house door when the carts came in. Elyanka gave him a stool, and wine he never drank, and called him her little mourner.{/n}",
    "{n}Her Lady's table was still laid every seventh night. The witness at the dead-house door counted the guests and took their names to the chaplains. Elyanka made him stand outside while her worshippers ate, and sent the bones out under his lamp. The Commander's protection kept her in Drezen; it did not silence the testimony.{/n}":
    "{n}Her Lady's table was still laid every seventh night, and the paladin's lamp-bearer stood at the dead-house door and counted the masks going in. Elyanka made him stand in the lane while her worshippers ate, and sent the bones out past him on a platter, still warm, so that he could count those too. He carried every name he could get to the chaplains. The Commander's protection kept the table laid; it never kept the lamp from the door.{/n}",
    "{n}The Commander remembered the sixty-one chalk marks on the dead-house floor after the inquiry. Elyanka had swept around them; a witness had stood at the door.{/n}":
    "{n}Seelah's sixty-one chalk crosses stayed on the dead-house floor for as long as Elyanka kept the house. She swept around them, and set her Lady's table over them, and on her Lady's nights she made her guests eat with their boots on the paladin's count.{/n}",
}

# --- S2: promises and grudges set in Chapter 5 that nothing read (append after the existing paragraphs) ----------------

CLAIM_READERS = (
    p('''{n}The Commander had walked out of her Lady's table before the wine, the first night it was laid. Behind their grey half-masks the lower town talked about it for years, as she had promised it would: the Knight Commander who knew where the table was, and would not sit, and would not tell. Thirty people who owed the Commander their necks, and knew it, and hated it every seventh night.{/n}''',
      requires=(TABLE_LEFT,)),
    p('''{n}No knight of Lastwall rode for Gallowspire on the Commander's whisper. She asked about it every spring, over wine, with her hand closed hard on the Commander's, and every spring she watched the Commander's hands instead of the face while the answer came, to see whether it was true.{/n}''',
      requires=(TOLD_HER,)),
    p('''{n}She burned the Deskari cultist alone, the night the Commander would not look inside the corpse, and kept that grudge for years. Whenever the Commander refused her anything afterwards she said, pleasantly, "Burn it, then," and the Commander knew exactly how long she had been thinking about it, and how unkindly.{/n}''',
      requires=(ANATOMY_LEFT,)),
    p('''{n}She never took anyone else to the black circle in the Camilary woods where the priests had made their fire, and the Way never learned that it was there. Only the Commander knew. She said that if it was ever spoken of, in any tongue, she would know whose mouth it had come out of, and the Commander would learn what the Way does with a whisper that has got loose.{/n}''',
      requires=(WOODS,)),
    p('''{n}The Commander never went to Ustalav alive. She reminded the Commander now and then that this was a matter of time, not of choice: the body always goes home with the collector, and this one would go down the Ustalav road under glass, with the curtains drawn, whether it had wanted to see the country or not.{/n}''',
      requires=(US_REFUSED,)),
    p('''{n}The Way's joiners planed the shoulders, as she told them to, and finished the true table in ebony without the Commander ever lying in its practice piece. She said that was what a creditor's patience was for: the dish would fit when it was served, whether or not the guest had tried it.{/n}''',
      requires=(FIT_REFUSED,)),
    p('''{n}The Commander had once held a hart by the antlers in the woods above Drezen while she cut its throat, and she never let anyone forget that the Knight Commander of the Fifth Crusade was, at need, a passable hunting dog. From her it was the highest praise there was.{/n}''',
      requires=(HUNT_HELD,)),
    p('''{n}The hart's tine left a long white seam above the Commander's knee. Elyanka knew it by touch in the dark, and on her Lady's nights she ran her thumbnail down it and called it the only honest mark anyone had ever put on her collateral, and the most wasteful.{/n}''',
      requires=(HUNT_GORED,)),
)

COLLATERAL_SCAR = p('''{n}Her thumb stops on the seam above your knee where the hart's tine went in.{/n} "And this. The stag marked my goods before the Wound could." {n}She presses, hard enough to hurt.{/n} "I ate him, and I have still not forgiven him."''',
                    requires=(HUNT_GORED,))


def integrate(payload):
    # S1: the master's murder, on screen.
    _rewrite(payload, E + "beat.master", "kill2", "{n}Three days later a carriage is found in a ditch", KILL2)
    _rewrite(payload, E + "beat.master", "kill", "{n}She does not smile. She nods once,", MASTER_KILL)
    _rewrite(payload, E + "beat.master", "hers", "{n}She studies you across the trestle,", MASTER_HERS)
    # V1: the embalmer lie.
    _rewrite(payload, E + "beat.writ", "lied2", "{n}She waits until the gate has closed behind them.", LIED2)
    # D08: the hunt. The unchecked "quick" answer now drives the hart; the interception is the checked trailing answer.
    _answer(payload, E + "beat.hunt", "stag", 1, "[Be quick. Get between the stag and the trees.]",
            "[Be quick. Beat the brush on his flank and drive him onto her knife.]")
    _rewrite(payload, E + "beat.hunt", "kill_quick", "{n}He comes out of the dark at a run, a big grey hart, and you are where",
             KILL_QUICK)
    # S7: one speaker, one quotation (two adjacent quotes read as two voices); the paladin fragment.
    _swap(payload, E + "executor.haggle", "sold",
          '"Not a copper, and still you whispered it back." "You are mine when you are dead.',
          '"Not a copper, and still you whispered it back. You are mine when you are dead.')
    _swap(payload, E + "executor.haggle", "bare_sold",
          '"Nothing paid. Nothing due to you." "You are mine when you are dead, Commander.',
          '"Not a copper changes hands. You are mine when you are dead, Commander.')
    _swap(payload, E + "straight.offer", "sold",
          '"Nothing paid. Nothing due to you." "You are mine when you are dead. Do not dawdle."',
          '"Not a copper changes hands, and you are still mine when you are dead. Do not dawdle."')
    _swap(payload, E + "test.the_dead", "carrion", '"Carrion." "You would send my Lady', '"Carrion. You would send my Lady')
    _swap(payload, E + "test.the_dead", "paladin",
          '"the paladin of Iomedae, kneeling to pray for Pharasma\'s dead, row by row, until her knees were grey with lime. She did not see me in the yard.',
          '"Kneeling to pray for Pharasma\'s dead, row by row, until her knees were grey with lime. A paladin of Iomedae. She did not see me in the yard.')
    # S3 / S4: whole-paragraph rewrites, gates unchanged.
    epilogues = [E + "epilogue." + k for k in ("claim", "debt", "lock", "left_free")]
    _paragraphs(payload, epilogues + ["elyanka.lastcall.page"], BOTTLED)
    _paragraphs(payload, epilogues, INQUIRY)
    _paragraphs(payload, ["trickster.lastcall.page.collectors"], COLLECTORS)
    # S2: readers for the Chapter 5 promises (appended; existing indices unchanged).
    _append(payload, E + "epilogue.claim", "page", CLAIM_READERS)
    _append(payload, E + "ch6.collateral", "inspect", (COLLATERAL_SCAR,))
    # S5: after the hanging Seelah holds the carters' word that the carts were Elyanka's ("another woman's crime").
    seelah_line = _ledger_entry(payload, "secret.elyanka_siege_dead")["Lines"][0]
    if seelah_line["Text"] != "{n}Unknown to Seelah.{/n}":
        raise ValueError("elyanka_cloud: unexpected siege-dead Seelah line")
    seelah_line["Forbids"] = list(dict.fromkeys([*seelah_line["Forbids"], MISLED]))
    # S6: her Guest List entry, in her own terms (no harem row produces her stance; household registry: indifferent).
    guest = _ledger_entry(payload, "guest.elyanka")
    if not guest["Text"].endswith("if she wants it.{/n}"):
        raise ValueError("elyanka_cloud: unexpected guest.elyanka text")
    guest["Text"] = guest["Text"][:-len("{/n}")] + (" She keeps her own table, in the dead-house by the south gate, laid "
                                                     "every seventh night, and has never sat at anyone else's.{/n}")
