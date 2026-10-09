"""Claude voice for the pair rows the Nocticula row owns (villain-route-nocticula).

CLOUD-QUEUE wave 2: Nocticula owns household.pair.arueshalae_nocticula.*,
household.pair.nocticula_shamira.*, household.pair.galfrey_nocticula.* and
household.pair.iomedae_nocticula.*. Text only, after the row builders and the
contract controller (rows load in name order): no node, choice, flag or gate
changes and no paragraphs (J03). Each placeholder is replaced only where its
exact [PROSE PENDING] text stands.

- arueshalae_nocticula: Nocticula's answers through the acquired half-seal
  (claude-work-queue ruling 2: held / failed / retry failed). Arueshalae's
  fallen lines in the .corrupted scenes are the Arueshalae row's proposed text
  (redesign/arueshalae/cloud-review.md 4.1), pasted as written.
- nocticula_shamira.precedence.live: the two letters of ruling 17 (Shamira
  review section 5 proposal, "steward" corrected to her title).
- galfrey_nocticula: two flat Nocticula lines put back in her register.
Native register: afa1bd23 ("Few are courageous enough, or stupid enough"),
d3d9a3e6 ("my collection of torture implements"), 6c27d43e, 70a37858.
"""

A = "household.pair.arueshalae_nocticula."
S = "household.pair.nocticula_shamira.precedence.live"
G = "household.pair.galfrey_nocticula."

HELD = "[PROSE PENDING: nocticula - want rank without conceding the throne / answer through the acquired seal, acknowledge Arueshalae's name / limit this claim, no summons]"
FAILED = "[PROSE PENDING: nocticula - want obedience / return a sealed rejection / ownership claim remains disputed]"
RETRY_FAILED = "[PROSE PENDING: nocticula - want rank acknowledged / reject the repeated renunciation / public claim remains disputed]"
A_START = "[PROSE PENDING: arueshalae - want her own name / publicly dictate renunciation over the crusade map / defy her former mistress]"
A_ANSWER = "[PROSE PENDING: arueshalae - want freedom from ownership / answer the queen in her own name and sign / public defiance]"
A_REFUSED = "[PROSE PENDING: arueshalae - want the crusade or her own appetite / withhold the renunciation / leave the claim disputed]"

NOCT_HELD = '''{n}The half-seal warms through its wrapping before anyone touches it. The answering mark crawls out across the sheet, under Arueshalae's name, in a hand the whole Table can read.{/n} "Arueshalae. So the girl has a name now, and says it to my face in front of soldiers. How brave. How very mortal of her." {n}The mark stops, the way a cat stops with one paw still on the mouse.{/n} "I am the Lady in Shadow, girl, and I do not need you on your knees to remain so. Keep your little life among the crusaders. I shall not summon you, and I shall not send for you. But every succubus in my city will know that you walked out of my service and that I let you, and they will wonder what you paid for it. Let them wonder. It will cost you more than kneeling would have."'''
NOCT_HELD_RETRY = '''{n}This time the half-seal is warm before the sheet is even unfolded, as if it had been waiting. The mark writes under Arueshalae's name without hurrying.{/n} "Again, and louder. Very well, girl: Arueshalae. There, I have said it, in my own hand, where the whole Table can read it." {n}A pause, long enough to be insulting.{/n} "I am the Lady in Shadow, and I do not need you on your knees to remain so. Keep your little life among the crusaders. I shall not summon you, and I shall not send for you. But every succubus in my city will know that you walked out of my service and that I let you, and they will wonder what you paid. Let them wonder. It will cost you more than kneeling would have."'''
NOCT_FAILED = '''{n}The half-seal stays cold for an hour. Then the sheet comes back folded, sealed with her mark pressed so hard the wax has split, and inside, under Arueshalae's renunciation, one stroke through the whole of it.{/n} "Mine. Come home on your knees, girl, or do not come home at all; but do not send me paper telling me what you are."'''
NOCT_RETRY_FAILED = '''{n}The same sheet comes back a second time. The mark has not bothered to strike anything out; it has written underneath, small and amused, where every soldier at the Table can read it.{/n} "Twice. The second time is always less convincing, girl. I am still the Lady in Shadow, you are still mine until I say otherwise, and I have not said it."'''
# Arueshalae row, cloud-review.md 4.1 (fallen register), as proposed.
ARUE_START_SETTLE = '''{n}Arueshalae unrolls the crusade map across the Table with both hands and puts one claw through the black blot that is Alushinyrra.{/n} "Say it for her, darling, out loud, since she has a seal on your table now. 'Arueshalae. Of nobody's house.' Not hers. Not Vellexia's. Not yours, either, before you get ideas." {n}She smiles at the seal as if it could see her, and her wings are pressed flat against her back.{/n} "I bowed to her my whole life, because that is what one does. I worship one god now. She is standing here, and she is hungry, and she does not kneel."'''
ARUE_START_RETRY = '''"Again, darling? You are stubborn." {n}She flattens the map with the heel of her hand, over the old claw-mark.{/n} "Louder, then. 'Arueshalae. Of nobody's house.' Let the seal hear it twice."'''
ARUE_ANSWER = '''"She said my name." {n}She laughs, low and delighted, and does not quite stop her hands from shaking.{/n} "Our Lady in Shadow said my name, and not 'my succubus'. Do you know how few of her creatures have heard that and lived to sulk about it?" {n}She signs under the queen's line with one claw, through the paper and into the wood of the Table.{/n} "Arueshalae. Mine. She can keep the rest of the city. I've had all of it I want."'''
ARUE_REFUSED = '''"Then leave it." {n}She rolls the map up, quick and neat, before anyone can see where her claw went in.{/n} "Let her think she owns me. Let her come and collect, if she likes. I'd rather be hunted by a queen than pardoned by one; at least the hunt is interesting." {n}She drops the map on the Table.{/n} "Now feed me something. Defiance makes me hungry."'''

QUEEN_REPLY = '''{n}The first sheet carries the Lady in Shadow's seal, pressed so deep it has cut the paper.{/n} "My Ardent Dream wishes it known that she sits beside me. How sweet. She sits where I put her, and she will go on sitting there because it amuses me to watch her want the chair next to it. Read her claim aloud at your table if you like, Commander. I shall let it stand. I have always liked a little treason with my wine."'''
SHAMIRA_REPLY = '''{n}The second sheet smells of cinnamon and is sealed with the Ardent Dream's own sign.{/n} "I rule her city. I hear her petitioners, I choose which of them she sees and which go home without a tongue, and I share her bed when she is bored of the islands. Write that I stand beside her, Commander, not behind. She lets it stand? Of course she does. She thinks it costs her nothing. Let her think so a little longer."'''

# (scene, node, placeholder, text)
NODES = [
    (A + "settle.redeemed", "held", HELD, NOCT_HELD),
    (A + "settle.redeemed", "failed", FAILED, NOCT_FAILED),
    (A + "settle.corrupted", "start", A_START, ARUE_START_SETTLE),
    (A + "settle.corrupted", "held", HELD, NOCT_HELD),
    (A + "settle.corrupted", "answer", A_ANSWER, ARUE_ANSWER),
    (A + "settle.corrupted", "refused", A_REFUSED, ARUE_REFUSED),
    (A + "settle.corrupted", "failed", FAILED, NOCT_FAILED),
    (A + "retry.redeemed", "held", HELD, NOCT_HELD_RETRY),
    (A + "retry.redeemed", "failed", RETRY_FAILED, NOCT_RETRY_FAILED),
    (A + "retry.corrupted", "start", A_START, ARUE_START_RETRY),
    (A + "retry.corrupted", "held", HELD, NOCT_HELD_RETRY),
    (A + "retry.corrupted", "answer", A_ANSWER, ARUE_ANSWER),
    (A + "retry.corrupted", "refused", A_REFUSED, ARUE_REFUSED),
    (A + "retry.corrupted", "failed", RETRY_FAILED, NOCT_RETRY_FAILED),
    (S, "queen_reply", "[PROSE PENDING: nocticula - want court precedence / separately answer through her acquired seal and assert her priority / tolerate her lover's public counterclaim]", QUEEN_REPLY),
    # shamira_reply is written in z_j03_contracts.py (her full false-justice letter); this row writes only the queen.
]

# (scene prefix, old substring, new substring, minimum hits)
SUBS = [
    (G, '"Have your clerk learn whom he addresses before he petitions me."',
     '"Teach your clerk whom he addresses, Commander, or send him to me and I will teach him. He will not need the lesson twice. He will not need a tongue for it, either."', 2),
    (G, '"You were told to waive this levy. You will refund your demand and surrender its collection to another. Try selling my protection twice again, and I shall collect from you personally."',
     '"You were told to waive this levy. Refund it. Then come to the Harem, on your knees, and explain to me why my protection was for sale twice. Bring the hand you collected with; you will not be taking it home."', 6),
]


def register(payload, scenes, refs):
    by = {s["Id"]: s for s in payload["Scenes"]}
    for sid, nid, old, new in NODES:
        node = next((n for n in by[sid]["Nodes"] if n["Id"] == nid), None) if sid in by else None
        if node is None:
            raise ValueError(f"nocticula pairs: missing {sid}:{nid}")
        if node["Text"].strip() != old:
            raise ValueError(f"nocticula pairs: {sid}:{nid} no longer carries its placeholder")
        node["Text"] = new
    for prefix, old, new, minimum in SUBS:
        hits = 0
        for s in payload["Scenes"]:
            if not s["Id"].startswith(prefix):
                continue
            for node in s["Nodes"]:
                if old in node["Text"]:
                    node["Text"] = node["Text"].replace(old, new)
                    hits += 1
        if hits < minimum:
            raise ValueError(f"nocticula pairs: {prefix}: expected {minimum} hits, got {hits}: {old[:50]!r}")
