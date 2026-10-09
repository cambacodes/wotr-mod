"""Heat calibration, batch g (Claude prose, 2026-10-09): official-register rewrite.

Owner direction: every intimate scene matches the heat of the official in-game WotR romances (see
knowledge/lore/canon-heat-reference.md in the Writer repo). The act is never narrated; the narration keeps to skin, lips,
breath, hands, hips and clothes; the cut sits right after the first heated contact and is one short second-person
paragraph that may name the peak of pleasure but no parts; the characters talk frankly while the narration stays
restrained; the morning after is short and in character.

Scenes: Gesmerha (4), Arsinoe (4), Eritrice (5), Arueshalae (4), Eliandra (5), Delamere (4).

Text only, applied last (expansion._make_expansion, after heat_g4). No scene, node, paragraph or choice id, choice
position, Requires, Forbids, Set, Next, check or cost changes. Every target must resolve and every replaced text must
begin or contain the reviewed fragment, or the build fails. Slot nodes (`.explicit.N`) keep their ids; they stay the
cut beat. Where a default node duplicates its slot node (the slot default), both get the same text.
"""
from storylines.heat_text import _node, swap


def put(payload, sid, nid, expect, new):
    """Replace the whole node text (the old text must start with `expect`)."""
    node = _node(payload, sid, nid)
    if not node["Text"].startswith(expect):
        raise ValueError("heat cal g: %s/%s drifted from the reviewed text (%r)" % (sid, nid, expect[:60]))
    node["Text"] = new.strip()


def tail(payload, sid, nid, marker, new):
    """Replace the node text from `marker` (exactly once) to its end."""
    node = _node(payload, sid, nid)
    if node["Text"].count(marker) != 1:
        raise ValueError("heat cal g: %s/%s marker not found exactly once (%r)" % (sid, nid, marker[:60]))
    node["Text"] = node["Text"][:node["Text"].index(marker)] + new.strip()


def para(payload, sid, nid, pid, expect, new):
    """Replace one paragraph text, found by paragraph Id (the old text must start with `expect`)."""
    hits = [x for x in _node(payload, sid, nid).get("Paragraphs", []) if x.get("Id") == pid]
    if len(hits) != 1 or not hits[0]["Text"].startswith(expect):
        raise ValueError("heat cal g: %s/%s paragraph %s drifted (%r)" % (sid, nid, pid, expect[:60]))
    hits[0]["Text"] = new.strip()


def para_tail(payload, sid, nid, index, marker, new):
    """Replace one paragraph text from `marker` (exactly once) to its end, by paragraph index."""
    x = _node(payload, sid, nid)["Paragraphs"][index]
    if x["Text"].count(marker) != 1:
        raise ValueError("heat cal g: %s/%s paragraph %d marker not found (%r)" % (sid, nid, index, marker[:60]))
    x["Text"] = x["Text"][:x["Text"].index(marker)] + new.strip()


def integrate(payload):
    _gesmerha(payload)
    _arsinoe(payload)
    _eritrice(payload)
    _arueshalae(payload)
    _eliandra(payload)
    _delamere(payload)


# ---------------------------------------------------------------------------------------------------- Gesmerha
def _gesmerha(payload):
    # Workshop afternoon: the slot default (private) and its slot node carry one text.
    pallet = '''
{n}You bar the workshop door. Gesmerha takes your hand and leads you to the pallet behind the curtain, ducking beneath the low shelf.{/n}
"Mind your head. I refuse to explain this to a healer."
{n}She kisses you before you can answer, and her fingers work your belt loose with the speed of long practice. When your hands find the hem of her shift she pulls it off herself and presses close, warm skin against yours, her breath short against your mouth.{/n}
"Stay. The clan has had me since dawn. I want this afternoon, and I want to learn what these hands do when they are not holding a tool."
{n}She draws you down onto the pallet, and the light through the shutter goes on moving across the wall without either of you.{/n}'''
    for nid in ("private", "gesmerha.what_she_asks.explicit.1"):
        put(payload, "gesmerha.what_she_asks", nid, "{n}You bar the workshop door.", pallet)

    room = "gesmerha.the_room_she_chose"
    swap(payload, [(room, "lover")],
         "Her thumb crosses your hip bone and then lower, and rests there.{/n}",
         "Her thumb crosses your hip bone and stays there, a plain statement that needs no words.{/n}")
    night = '''
"Then stay."
{n}She frees her braid and pulls off her shift. Her chin lifts toward your breath.{/n}
"Come here. I have been wanting you all day."
{n}Her rough palms pass over your shoulders and down your back, and her mouth finds yours in the lamplight. She undoes your belt herself, then draws you into bed. A board creaks; she laughs against your lips, and the blanket comes up over you both, skin warm against skin, her heartbeat going hard beneath your hand.{/n}'''
    for nid in ("night", "gesmerha.the_room_she_chose.explicit.1"):
        put(payload, room, nid, '"Then stay."', night)
    for nid in ("first_night", "gesmerha.the_room_she_chose.explicit.2"):
        swap(payload, [(room, nid)],
             "Her hand rests at your waist as she draws closer.{/n}",
             "Her hand rests at your waist as she draws closer, and then there is only the blanket, the creaking bed and the "
             "sound of her breath catching in the dark.{/n}")

    # Bench / second ask: one cut paragraph shared by the defaults and the slot nodes.
    old = ("{n}She draws you down with her onto the cloth. Beyond the yard a patrol passes toward the walls; "
           "she keeps you close until its boots fade.{/n}")
    new = ("{n}She draws you down with her onto the cloth. Beyond the yard a patrol passes toward the walls, and she goes still "
           "against you, listening, her breath held against your throat, until its boots fade; then she laughs, low and ragged, "
           "and does not trouble to be quiet again.{/n}")
    swap(payload, [("gesmerha.trickster.returned.bench", "night"),
                   ("gesmerha.trickster.returned.bench", "gesmerha.trickster.returned.bench.explicit.1"),
                   ("gesmerha.trickster.returned.second_ask", "night"),
                   ("gesmerha.trickster.returned.second_ask", "night_flinched"),
                   ("gesmerha.trickster.returned.second_ask", "gesmerha.trickster.returned.second_ask.explicit.1"),
                   ("gesmerha.trickster.returned.second_ask", "gesmerha.trickster.returned.second_ask.explicit.2")],
         old, new)


# ---------------------------------------------------------------------------------------------------- Arsinoe
def _arsinoe(payload):
    sid = "arsinoe_the_unprofitable_hour"
    tail(payload, sid, "kiss", "{n}She kisses you again beside the table.", '''
{n}She kisses you again beside the table. The book lies open, the drinks unfinished. Her fingers catch in your collar and work it loose, then find your belt, and she smiles against your jaw at how quickly your breath goes.{/n}
"You could stay. I have no intention of reading another page tonight."
{n}She backs you against the table edge, takes your hand and presses it flat to the silk at her throat, over her heartbeat. Her breath comes short. She chose her clasps tonight and counted every one of them, and she wants every one of them undone.{/n}
"Decide, Commander. Walk out, or stay and be thorough."''')
    put(payload, sid, sid + ".explicit.1", "{n}Arsinoe leaves the book open", '''
{n}Arsinoe leaves the book open and draws you to the bed. The silk slides from her shoulders as though it had only been waiting for the order, and she strips you with quick, impatient hands, skin to skin before the lamp has finished steadying. She pulls you down with her, and for a while the only sound is her breath and the bell of some distant hour that neither of you counts.{/n}
"The shop can wait until morning. Look at me properly. I did not buy the silk for the shelf."''')

    sid = "arsinoe_the_window_opens"
    cut = '''
{n}Her kiss is slow until your hands close on her waist. Then she draws you to the bed by your belt, and the slowness goes. She strips you with the same exacting attention she gave her robes and far less patience, her mouth at your throat, your collarbone. Her skin is warm beneath your palms, and when you kiss her neck she says your name like a correction.{/n}
"Not slowly now. I have been watching you all evening."
{n}She pulls you down with her by a fist in your shirt, holds your gaze in the lamplight, and the room narrows to heat and breath and the sound of her laughing against your mouth.{/n}'''
    for nid in ("window_invitation", "window_return"):
        tail(payload, sid, nid, "{n}Her kiss is slow until your hands close on her waist.", cut)
    put(payload, sid, sid + ".explicit.1", "{n}Arsinoe keeps her hand", '''
{n}The lamp stays lit. Her nails trail down your back, her eyes never leave yours, and when the peak takes her she says your name once, low and unguarded, with none of the clerk left in it.{/n}
"Leave the lamp burning. Let the street wonder."''')

    sid = "arsinoe.trickster.cauldron.collection"
    cut = '''
{n}She takes your hand and pulls you close. Her mouth is warm and deliberate; the second kiss leaves her breathing harder. She pushes the ledger aside and the pen rolls off the counter, unmourned. She backs you against the cleared edge, works your buttons open one-handed, and when your hands find her bare waist she makes a short, unladylike sound and kisses you again to hear it twice.{/n}
"I keep an exact account of what I want, Commander. Do not round it down."
{n}She drags your clothes aside, impatient where she is always exact, her teeth at your lower lip while the counter complains under both of you, and the shop's one candle gutters and nobody trims it.{/n}'''
    for nid in ("threshold", "threshold_return"):
        tail(payload, sid, nid, "{n}She takes your hand and pulls you close.", cut)
    put(payload, sid, sid + ".explicit.1", "{n}Still astride your lap", '''
{n}The candle burns down unattended. When the peak takes her she bites back a cry against your shoulder, a priestess of Abadar swearing in a language no temple taught her, and afterwards she keeps your hand pressed to her waist and gives the ledger no further attention.{/n}
"The ledger stays shut tonight."''')

    sid = "arsinoe.trickster.late.commit"
    cut = '''
{n}She undid the rest herself and let the robes fall. Her hair came loose as she pushed the Commander back toward the bed. She put their hands on her bare waist and held them there until their fingers tightened, then bent to their mouth, and her composure broke on a breath.{/n}
"Higher. I have wanted your hands there since the roof above Tovin's shop."
{n}She stripped them with the exactness she gave a ledger and none of the patience, kissing down their throat while their hands knotted in her loosened hair, flushed and shaking with the effort of not hurrying, her gold eyes never leaving theirs.{/n}'''
    for nid in ("night", "late_return"):
        tail(payload, sid, nid, "{n}She undid the rest herself and let the robes fall.", cut)
    put(payload, sid, sid + ".explicit.1", "{n}Arsinoe remained over the Commander", '''
{n}The robes lay where they fell. Arsinoe's fingers closed around theirs against her waist, and when the peak took her she said the Commander's name like a verdict, low and unguarded, with every ledger in Drezen forgotten.{/n}
"Tomorrow, you may tell me how patient I was."''')
    tail(payload, sid, "deferred_evening", "{n}She caught the Commander's sleeve, kissed them and led them toward the bed.", '''
{n}She caught the Commander's sleeve, kissed them and led them toward the bed. Halfway there she stopped to kiss them again against the wall, her robes already open, her breath ragged against their mouth. She had been composed all day and was composed no longer.{/n}
"Four weeks. I have been insufferable all day. Take your clothes off."
{n}The Commander did, and she watched every inch of it with open appetite. She drew them down onto the bed and let the robes slide off her shoulders, hair falling around both their faces, flushed and smiling, savouring the moment she had waited a month for.{/n}''')
    put(payload, sid, sid + ".explicit.2", "{n}Arsinoe stayed poised", '''
{n}The bottle stayed unopened. Arsinoe's laugh broke against the Commander's throat, and the wait of a month ended in one long, unguarded moan, the best-kept books in Drezen forgotten.{/n}
"You have kept me waiting long enough."''')


# ---------------------------------------------------------------------------------------------------- Eritrice
def _eritrice(payload):
    sid = "eritrice.trickster.epilogue.commit"
    tail(payload, sid, "aye", "Her mouth followed her hands,", '''
Her mouth followed her hands, over throat and chest, tawny and heavy and burning, her claws sheathed only just against the Commander's ribs. She stripped the Commander with the exactness she gave a motion, and the forty letters slid unregarded to the floor. "I have been very patient on paper," she said. "In person I find I am not." Her robe went after the letters, and the lamp burned on over a study that had never held so loud a session.{/n}''')
    para(payload, sid, "aye", "eritrice.trickster.epilogue.commit.explicit.1", "{n}She kisses the Commander again", '''
{n}She kisses the Commander again, drawing them down onto the desk with her, and time stops being a thing the chair keeps. When the peak takes her she growls the Commander's name into their shoulder, claws sheathed with great care. Her robe lies over the back of the chair; the scroll rests safely beyond their reach.{/n}''')

    # (suffix, table as the cut names it, table as the council scene names it, chair)
    for sfx, table, chair in ((".drezen", "the borrowed table", "the chair beside the table"),
                              ("", "the Council's table", "Alichino's chair")):
        sid = "eritrice.minutes.adjourned" + sfx
        swap(payload, [(sid, "armour")], "and stands between your knees, and looks at you in the lamplight",
             "and stands close in front of you, and looks at you in the lamplight")
        put(payload, sid, "cut", "{n}She comes the whole way", '''
{n}She comes the whole way: one hand spread on your chest, pushing you flat on TABLE among the inkwells. She reaches past you, without taking her eyes from yours, and turns the lamp down to nothing; and in the last of its light you see her other hand move the scroll recording your two ayes to safety at the far end of the table, even now, even then.{/n}
{n}Then the proud hand returns. It closes in your hair and drags your mouth to hers, and she kisses you with open, snarling hunger, a rumble in her chest like a lion in the next room. Her gown is already off her shoulders; she shrugs the rest of it down, and in the dark the heavy warmth of her presses against you, tawny and strong, her claws held in against your ribs with a care that makes your pulse jump. She finds your belt and strips you with no ceremony at all.{/n}
"I do not say this lightly," {n}she says, low, her mouth against your ear.{/n} "I want you. Not the vote. Not the minutes. You."'''.replace("TABLE", table))
        put(payload, sid, "eritrice.minutes.adjourned.explicit.1", "{n}She draws you against her", '''
{n}The last light goes out. There is only the heat of her, the rumble in her chest climbing past a purr into something with no name in the Council's minutes, her claws held in against your ribs until the peak takes her and, for once, they are not held in quite enough. The scroll lies untouched at the far end of the table.{/n}
"Strike that from the record," {n}she says afterwards, hoarse, and does not lift her cheek from your chest.{/n} "No. Keep it. Keep all of it."''')

        sid = "eritrice.council.twice_nightly" + sfx
        put(payload, sid, "carried", '"Carried."', '''
"Carried." {n}She pushes the scroll off her knees, turns to face you and pulls you to the edge of TABLE with a creak of old wood and a rumble in her chest that is very nearly a purr. She takes your hands and sets them on the belt at her waist, and holds them there until you pull it loose. Only then, with her mouth already on yours and her gown sliding off one shoulder, does she reach back and pinch out the candle.{/n}
{n}The minutes slide from the table. This time she leaves them where they fall. "I shall write it down in the morning," she murmurs against your mouth. "Give me something worth the ink."{/n}
{n}Her gown is off your hands and off her shoulders before the last page lands, TABLE creaking under her weight. She is all muscle under the cloth, tawny and heavy and hot, and her claws, sheathed with great care, rake down your back while the rumble in her chest climbs into something that is no longer very much like a purr.{/n}
"Again. As the last time. And not slowly; I have been minuting my own impatience since morning." {n}She tears your belt the rest of the way open and pushes you back among the fallen papers.{/n}'''.replace("TABLE", table))
        put(payload, sid, "eritrice.council.twice_nightly.explicit.1", "{n}Her gown falls across", '''
{n}Her gown falls across the abandoned scroll, and TABLE takes the rest of the night's weight. In the dark the rumble in her chest breaks, once, into a cry the empty room hands back to her.{/n}
"Minute that," {n}she says into your shoulder, a long while later.{/n} "Tomorrow. The fallen scroll can wait beneath CHAIR until morning."'''.replace("TABLE", table).replace("CHAIR", chair))


# ---------------------------------------------------------------------------------------------------- Arueshalae
def _arueshalae(payload):
    # The roof (fallen / evil): one cut shared by three scenes.
    roof_cut = '''
{n}She pushes you back against the wet slates with one hand flat on your chest, unhurried, the gargoyles leering over her shoulders, and her hair falls round both your faces like a curtain against the rain. Far below, a watchman calls the hour. She reaches back and unhooks the last clasp of her own dress, and lets it go, and the rain runs down her bare skin and onto yours. She tears your shirt open the rest of the way with two fingers and bends down until her mouth is against your throat.{/n}
{n}Her teeth close on the tendon there, just short of drawing blood, and a shudder goes through her that you feel in your own bones. Her hands strip you with a courtier's contempt for buttons, the rain drums on your bare skin, and her wings spread over you both like a tent against the rain.{/n}
"You've no idea," {n}she says, in the sweet, mocking hostess's voice,{/n} "how long it has been since I took something that wanted to be taken. Now. Don't you dare lose count." {n}Her mouth comes down on yours, the gargoyles grinning over her shoulder, and the cold begins to come looking for you.{/n}'''
    for sid in ("arueshalae.trickster.evil.window", "arueshalae.trickster.evil.window_yard", "arueshalae.trickster.fallen.roof"):
        put(payload, sid, "cut", "{n}She pushes you back against the wet slates", roof_cut)
    peak = ("{n}The count goes out of your head, and out of hers. She takes what she takes with her teeth and her whole hungry "
            "weight, and when the peak breaks over her she laughs, loud and cruel and delighted, over the sleeping rooftops. ")
    for sid in ("arueshalae.trickster.evil.window", "arueshalae.trickster.evil.window_yard"):
        put(payload, sid, sid + ".explicit.1", "{n}She pulls you close against the wet slates",
            peak + "Later she draws back from you, rain running off her wings, her mouth the colour of a bruise, and you are "
            "colder than you have any right to be.{/n}")
    put(payload, "arueshalae.trickster.fallen.roof", "arueshalae.trickster.fallen.roof.explicit.1",
        "{n}She pulls you close on the wet slates",
        peak + "Before the ward expires she lets go, as though it cost her a limb, and gathers you into the shelter of her wings.{/n}")

    # Bell tower (redeemed): the ward-limited slot and the released one.
    sid = "arueshalae.treatment.night"
    swap(payload, [(sid, "undress")], "and settles over you, one hand braced beside your head.{/n}",
         "and leans close, her hair a curtain round your face.{/n}")
    tail(payload, sid, "undress", "{n}She peels the rest of her own clothes away", '''
{n}She peels the rest of her own clothes away without ceremony, with the old expertise of a woman who once did this to ruin people, and lets you see her under the stars, bare and unhurried, her wings half unfurled behind her like a canopy. She watches your face take her in. The corner of her mouth lifts, hungry and a little frightening. Then she strips you to the skin with those quick, certain hands, and the wind off the Worldwound raises gooseflesh along your arms until her wings come round to cover it.{/n}
"Hold still." {n}Her palms slide down your chest, and she takes her time, discovering you the way she once discovered a mark, with her fingertips and her eyes. A low, shaky laugh escapes her.{/n} "Oh. You want me too. Good. Say it with your hands."
{n}She draws your hands to her hips and holds them there, and the old expertise goes out of her all at once. Her mouth hovers an inch above yours, her whole body trembling on the edge of it.{/n}''')
    put(payload, sid, sid + ".explicit.1", "{n}She draws you down onto the cloak", '''
{n}She draws you down onto the cloak, counting under her breath between kisses, and the numbers come apart as the heat takes her: four, five, a gasp where six should be. At seven she tears herself away and drags the cloak between your skin and hers, panting, furious at the clock, her whole body still shaking with what she stopped short of.{/n}''')
    put(payload, sid, sid + ".explicit.2", "{n}She answers your kiss with another", '''
{n}Her wings close around you on the cloak, and time stops being something she counts. When she reaches the peak she moans your name against your throat, and for one breath the old broken stone smells of flowers that have never grown on it. Later she settles her ear against your chest and listens to your heartbeat.{/n}''')


# ---------------------------------------------------------------------------------------------------- Eliandra
def _eliandra(payload):
    sid = "eliandra.trickster.epilogue.together"
    para_tail(payload, sid, "page", 1, "then sat down on the edge and drew the Commander between her knees.{/n}",
              "then drew the Commander down onto the bed with her, skin warm in the candlelight.{/n}")
    para(payload, sid, "page", "eliandra.trickster.epilogue.together.explicit.1", "{n}Eliandra keeps hold of your wrist", '''
{n}Eliandra keeps hold of your wrist, her breath warm against your ear, and the candle burns down while the road map lies forgotten beyond it. When the peak takes her she laughs, startled, like a woman who has watched a star move, and holds on.{/n}''')

    sid = "eliandra.trickster.epilogue.late"
    tail(payload, sid, "late_accepted", '"Both. I have brought them all. Tonight I want you."', '''
"Both. I have brought them all. Tonight I want you."
{n}She bars the door, hangs her damp cloak by the fire and stands a moment looking at you the way she once looked at a chart she meant to get right. Then her hands go to the clasp at her throat, and the white robes loosen from her shoulders.{/n}
"A hundred years of duty, and I find my list of wants is very short. You are on it twice." {n}She draws you to the bed by your belt.{/n}''')
    para(payload, sid, "late_accepted", "eliandra.trickster.epilogue.late.explicit.1", "{n}Eliandra keeps her hand where it is", '''
{n}Her forehead rests against yours and she does not let go of your gaze. The candle gutters beside the bed; her breath comes unevenly, and when the peak reaches her she holds your eyes through it, unguarded, as she holds nothing else.{/n}''')

    sid = "eliandra.trickster.epilogue.unasked"
    para_tail(payload, sid, "late_accepted", 0, "She was lean and pale and entirely without apology;", '''
She was lean and pale and entirely without apology; she put the Commander's hand to her bare waist and said, in the tone she used for directions, "I want the lamp lit. I want to learn this properly. Show me where, and then I will show you what I do when I know." Her breath was already unsteady. She pulled them down beside her and drew them close, watching their face.{/n}''')
    para(payload, sid, "late_accepted", "eliandra.trickster.epilogue.unasked.explicit.1", "{n}Eliandra keeps her hand low", '''
{n}Eliandra's breath goes ragged against your mouth and the lamp stays lit; she wants to see all of it. When the peak takes her she says your name as if learning a word in a new tongue.{/n}''')

    for sid in ("eliandra.trickster.visit.star_heart", "eliandra.trickster.visit.star_heart_mark"):
        swap(payload, [(sid, "learn")], "Her thigh presses between yours; the loosened white robes gather at her hips.",
             "The loosened white robes gather at her hips.")
        swap(payload, [(sid, "charts")], "then draws you between her knees at the edge of the bare table.{/n}",
             "then draws you against the edge of the bare table.{/n}")
        tail(payload, sid, "charts", "{n}Her hands go to your belt before you have finished obeying", '''
{n}Her hands go to your belt before you have finished obeying, exact and unembarrassed, the way she handles every difficult task. The white robes slip lower at her waist, and the starlight finds her bare shoulders and the pale skin above her collar. She takes your hand from her waist and draws it along her ribs, and watches your face while you learn her.{/n}
"Not so careful," {n}she says, a little breathless, and bites at your lower lip.{/n} "I have spent a hundred years being careful. Harder. There."
{n}She arches against your hands with her head tipped back and the lights of the dead shrine going over her throat. When she cannot stand any more of it she drags your clothes open and pulls you in against her until nothing is left between you but the next breath.{/n}''')
        put(payload, sid, sid + ".explicit.1", "{n}Eliandra holds you there", '''
{n}Her breath breaks hard against your mouth, and the starlight comes down over the two of you. When the peak takes her she says your name, and then, startled, laughs at herself, a priestess with her whole sky looking on. The last chart slips from the table.{/n}''')


# ---------------------------------------------------------------------------------------------------- Delamere
def _delamere(payload):
    cut = '''
{n}She makes a sound that is almost a growl, and her hands are at your belt, and the embers flare in a gust of wind off the water, and the whole blind smells of smoke and blood and frost and her.{/n}
{n}She has you out of your coat and your shirt before you have finished answering, and the cold on your skin lasts as long as it takes her to lie down against you. Her mouth finds your throat and bites. Her hands go everywhere a hunter's hands go when she has run the quarry to ground: ribs, shoulders, the old wound in your leg, which she grips once, hard, as if to remember whose arrow it was.{/n}
"You are shaking, stag." {n}She is not laughing now.{/n} "So am I. Look at me. Look. I want you looking."
{n}She takes your wrist and lays your hand along the long white scar at her side, and holds it there while her breath comes harder, cursing under it in Kellid. Her eyes go over what she has caught with a hunter's plain greed.{/n}
"Mine, for tonight. I do not say forever. I say tonight."
{n}Her hair comes down around both your faces and shuts out the fire, and she is fierce and alive and wanting, with not one thing in her face that belongs to the dead.{/n}'''
    slot = '''
{n}Time goes the way the fire does. Her teeth, her hands, her breath hot and ragged against your throat, the hide rough beneath you and her skin burning above the frost; when the peak takes her she shouts into the dark, a hunter's cry, long and unashamed, and the blind has no wall left to hold it. She draws you against her on the warm hide, her mouth still hungry on yours. By dawn the fire is ash.{/n}'''
    for sid in ("delamere.trickster.woods.second_hunt", "delamere.trickster.woods.second_hunt_page",
                "delamere.trickster.woods.second_hunt_late"):
        put(payload, sid, "cut", "{n}She makes a sound that is almost a growl", cut)
        put(payload, sid, sid + ".explicit.1", "{n}She draws you against her on the warm hide", slot)

    sid = "delamere.trickster.epilogue.late"
    tail(payload, sid, "page", "{n}The Commander came.", '''
{n}The Commander came. She hauled the Commander's shirt over their head and tore the rest away with the rough speed of a woman who had skinned stags in the dark, bare to the waist in the glow of the embers, scarred and broad-shouldered. She pinned the Commander's wrists flat against the fur and bit along their collarbone.{/n}
"I was dead, and then I waited out a war for you. Lie still and let me have what I hunted."
{n}Her breath came in gasps against their throat, her teeth bared at the roof of the blind, and she let go of the wrists only to take the Commander's hands and set them hard on her hips.{/n}''')
    para(payload, sid, "page", "delamere.trickster.epilogue.late.explicit.1", "{n}She draws the hide over you both", '''
{n}The fire sinks. Her cry goes up through the roof of the blind and out over the new-moon woods, unashamed, and somewhere a night bird falls silent. She draws the hide over you both, her mouth still on yours; at dawn she takes up her bow and leads you home.{/n}''')
