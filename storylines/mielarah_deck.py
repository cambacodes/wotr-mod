"""Mielarah, Chapter 5: Starcatcher over Drezen (the courtship on her presence; 11 §2).

She comes north through the Worldwound's sky with cargo, as she said she would, and moors her ship high over the city
where nobody has to stand near her. Every beat opens from her presence beside the tiefling trader's stall in the lower
town (or the jewellers' arcade when he is not in the capital), and most of them go up through her portal onto her
deck (Tumberd/Cue_0075: "just use this portal. It will drop you right onto the deck").

The beats: the cargo (her arrival, per voyage), the nearest (what the Commander did or meant to do with her curse, and
her one demand), the best job in the whole world (Lann's line, Cue_0079), special cargo (the tombs she will not talk
about in the Bad Luck, AirAdventures/Cue_0418), disciplinary thought-correction (Cue_0054, the amulets of Cue_0328: the
pivotal moral node), the market (her curse in Drezen, and what the Commander will spend to keep her there), the wheel
(the commit: in flight she lets go of the wheel, the mirror of Cue_0426, and the Commander holds the course), the
quarterdeck above the clouds (the intimate beat), the morning (the Gravedragger has noticed the Commander), and the
other captains.
"""
import copy

from story_format import c, n, scene
from storylines.mielarah_trickster import (LANN_HEARD, 
    CLOSED, COMMITTED, CONTACT, CHARTER, CORRECTED, DECLINED, DOCKED, DREZEN, FLOWN, FREED, HUB, HUB_FAILED, HUB_FB,
    KILLED, LANDFALL, LAUGHING, LIED, MEANT, MINDER, MORNING, NIGHT, NOTICED, OSKEL_DEAD, P, RECKONED, REL, RETURNED,
    SECRET_KNOWN, SHIP_LOST, TIGHTENED, TOLD, UNIT, KERZ, NOCTA, D, SAID_USE, CUT, DEAD_LATCH, LANN_GUARD, WOLJIF_GUARD,
    STORM_OWNED, STORM_BLAMED, PAID, CUT_DOWN, ZYPHUS_MARK, STORM, AMULETS, PATTERN, SELF, REFUSED)

SCENES = []

WOULD = D + "would_have"                # an honest hypothetical, with no minder ever posted
SETTLED = D + "oskel_settled"           # Derived: his name painted (dead) or his question answered (alive)
COURTSHIP = "mielarah.route.courtship"   # the shared ledger's name for the commit (05 item 30), set with COMMITTED
PROMISED = D + "promised"
NO_PROMISE = D + "no_promise"
STAND = D + "stand_there"
CARGO_TOLD = D + "cargo_told"
KEPT = D + "crew_kept"
MARKET = D + "market"
ESCORTED = D + "escorted"
PRISONER = D + "offered_prisoner"
STAYS = D + "stays_in_the_city"
CAPTAINS = D + "captains"
OSKEL_ALIVE = (OSKEL_DEAD, SHIP_LOST)   # Oskel is aboard unless the curse took him or the storm took her whole crew


def mi(id, text, *choices, **kw):
    return n(id, "Mielarah", text, *choices, portrait="Mielarah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Mielarah", **kw)


PLACES = ((HUB, "", ()), (HUB_FB, ".arcade", (HUB_FAILED,)))
# PP9 (Sol INT): the arcade twin reads where it happens. The jeweller anchor replaces the tiefling's stall in the staging.
ARCADE_TEXT = (
    ("the tiefling trader has dragged his trestle back against the wall of the lower town to keep out of it, and looks as though "
     "he would drag the wall back too, if he could.",
     "the jewellers either side of her have pulled their trays back behind their counters to keep out of it, and look as though "
     "they would pull the arcade's pillars back too, if they could."),
    ("behind the tiefling's stall", "behind the jewellers' counters"),
    ("beside the tiefling's stall", "among the jewellers' counters"),
    ("the trader has put a bucket under it", "a jeweller has put a bucket under it"),
    ("cobbles", "flagstones"),
    ("The tiefling trader makes a small noise", "A jeweller makes a small noise"),
)


def arcade(nodes):
    for node in nodes:
        for old, new in ARCADE_TEXT:
            node["Text"] = node["Text"].replace(old, new)
    return nodes


def deck(id, title, entry, nodes, requires, forbids=(), delay=0, **fields):
    """A beat opened from her presence (the tiefling's stall, or the arcade when he is gone): the same scene
    on each hub, each forbidding the other's completion."""
    for hub, suffix, extra in PLACES:
        twin = id + ("" if suffix else ".arcade")
        delivery = arcade(copy.deepcopy(nodes)) if suffix else copy.deepcopy(nodes)
        if id in (D + "wheel", D + "quarterdeck"):
            threshold = next(node for node in delivery if node["Id"] == "threshold")
            threshold["Choices"][0]["Next"] = "explicit.1"
            # Explicit brief: first night on her coat, after her initiation; sleep before morning.
            delivery.append(nar("explicit.1", "{n}She draws you down onto her coat, her mouth still on yours. The watch stays forward; above the rail, the lashed wheel holds its course. When the cold wakes you, she has pulled the coat over you both.{/n}", c("Continue")))
        SCENES.append(scene(id + suffix, title, "Mielarah", 5, entry, delivery,
                            requires=("trickster.ever", CONTACT, *requires, *extra),
                            forbids=(CLOSED, KILLED, twin, *forbids), delay=delay, last=5, Relationship=REL, Chapters=[5],
                            Areas=[DREZEN], ContactUnit=UNIT, InteractionHub=hub, **copy.deepcopy(fields)))


# --- 1. The cargo: Starcatcher over Drezen. ------------------------------------------------------------------------

deck(D + "cargo", "Cargo for the market", '"You came through the Worldwound."', [
    nar("start", '''{n}Mielarah looks up from the bill of lading. The circle of empty cobbles around her is a good three strides across; the tiefling trader has dragged his trestle back against the wall of the lower town to keep out of it, and looks as though he would drag the wall back too, if he could.{/n}
{n}She sees you, and her face does something complicated, and then settles on courtesy, which is where it always settles.{/n}''',
        c("Continue", "third", requires=(LANDFALL,), forbids=(RETURNED,)),
        c("Continue", "scarf", requires=(RETURNED,), forbids=(SHIP_LOST,)),
        c("Continue", "fourth", requires=(SHIP_LOST,)),
        c("Continue", "charter", forbids=(LANDFALL, RETURNED, SHIP_LOST))),
    mi("third", '''"Through the Worldwound, yes. As promised." {n}She points up with her pencil, without looking. High over the citadel, small as a toy against the clouds, a ship hangs at anchor in the sky: Starcatcher the Third, her sails furled, her lanterns lit in the afternoon.{/n}
"The sky over the Wound is the colour of a week-old bruise and full of things with wings. My crew prayed to four gods on the way through. One of them answered, but I couldn't tell you which." {n}She ticks a line.{/n} "Cold iron from the Isles, Abyssal salts for your alchemists, and six passengers from Alushinyrra who wanted any sky but that one. I set them down outside the walls. Your gate sergeant was very rude about it."''',
       c("Continue", "oskel_told", requires=(MEANT,), forbids=(*OSKEL_ALIVE, PAID)),
       c("Continue", "oskel_paid", requires=(PAID,), forbids=OSKEL_ALIVE),
       c("Continue", "body", forbids=(MEANT,)),
       c("Continue", "body", requires=(OSKEL_DEAD,))),
    mi("oskel_told", '''"Oskel is aboard, before you ask. He brought her through the Wound with me. He does not stand at my elbow any more." {n}She turns a page.{/n}
"I told him why he did. It seemed only honest, and I have been honest with Oskel for six years, which is more than I can say for his head." {n}A pause.{/n} "He thought about it for a whole watch. Then he said, 'Figured.' That was all. He has been exactly as good a bosun since. I have no idea what to make of that, and neither, I think, does he."''',
       c("Continue", "body")),
    mi("oskel_paid", '''"Oskel is aboard, before you ask. He brought her through the Wound with me. He does not sit at my elbow any more; I gave the order the day we landed at Colyphyr, and he picked up his stool and carried it forward without a word." {n}She turns a page.{/n}
"He still has the purse. He has not spent a copper of it. I asked him once what he was waiting for, and he said he'd know it when he saw it." {n}A pause.{/n} "I have no idea what to make of that, and neither, I think, does he."''',
       c("Continue", "body")),
    mi("scarf", '''{n}She is wearing the scarf high around her throat, even here, even in the Drezen afternoon. Above the citadel a ship rides at anchor in the sky, her lanterns lit: Starcatcher the Third.{/n}
"Through the Worldwound, yes. With a new crew, hired in Alushinyrra at double wages. I have not put a hand in any of their heads yet." {n}She ticks a line.{/n} "I'm told the captains of the Midnight Isles have been laughing about Vazglar. Kerz sent me a length of good hemp rope, tied in a bow, with his compliments. I sold it. It fetched a decent price."
{n}Her pencil moves on down the page.{/n} "Cold iron, Abyssal salts for your alchemists, and six passengers from Alushinyrra who wanted any sky but that one. I set them down outside your walls."''',
       c("Continue", "body")),
    mi("fourth", '''"Through the Worldwound, yes. In that." {n}She points up, and does not bother to hide the pride or the wince. High over the citadel a ship hangs at anchor in the sky: small, broad in the beam, patched in three colours of canvas, with a new name painted on her bow in letters much too large for her.{/n}
"Starcatcher the Fourth. Twenty years old, she leaks like a colander, and she rolls in a crosswind like a drunk bishop. Five hands, all of them new, all of them paid in advance, none of them within two strides of me." {n}She ticks a line.{/n} "She got us through the Wound. I have decided that she is beautiful, and I'll hear no argument."''',
       c("Continue", "body")),
    mi("charter", '''"Through the Worldwound, yes, as chartered." {n}She points up with her pencil. High over the citadel a ship hangs at anchor in the sky: Starcatcher the Third, lanterns lit in the afternoon.{/n}
"You went to Colyphyr with another captain and came back alive, which I understand is a thing you make a habit of. I have decided not to take it personally. I am a professional." {n}She ticks a line, a little harder than it needs.{/n} "Cold iron, Abyssal salts for your alchemists, and six passengers from Alushinyrra who wanted any sky but that one. I set them down outside your walls. Your gate sergeant was very rude about it."''',
       c("Continue", "body")),
    mi("body", '''"Your city is at war, Commander. I can smell it from up there: pitch and horses and too many people in too few streets. So it has a use for an honest ship." {n}She lowers her voice, though nobody is near enough to hear; nobody is ever near enough.{/n}
"It also has a use for a cursed one, apparently, since you asked me here. Three days, and a porter has dropped a crate of my cold iron on his own foot, and a cart horse has bolted in this square and put a man through a shop window. Nobody dead." {n}Her mouth tightens.{/n} "Yet. That is the most accurate word in my vocabulary. Yet."''',
       c('[Step inside her circle of empty cobbles.]', "circle"),
       c('"You keep everyone at arm\'s length out here."', "arms")),
    mi("circle", '''{n}The tiefling trader makes a small noise, as if you had stepped off a roof.{/n}
"Nobody comes inside the circle." {n}She does not step back. She has to lift her chin a little to look at you, and looks at you over the folded bill of lading.{/n} "Everybody in this city has heard the rule by now. The porters have. And you walk in anyway."
"Hold this end of the bill, then. You are inside the circle; you might as well be useful." {n}She shifts the paper between you, keeping your shoulder beside hers.{/n}''',
       c("Continue", "moored")),
    mi("arms", '''"Out here, and everywhere." {n}She taps the bill of lading against the edge of a crate.{/n} "In Alushinyrra, nobody minded. People die in Alushinyrra of all sorts of things; my contribution was hardly noticed. Here, they notice. Your crusaders cross themselves when I pass. A priest of Iomedae has asked me, very politely, to buy my bread at a different baker."
{n}She does not seem hurt by it. She seems to find it correct.{/n}''',
       c("Continue", "moored")),
    mi("moored", '''"So I have moored Starcatcher a hundred fathoms up, where the only people near me are my crew, and they are paid for it. I come down to trade, and I go back up, and your city keeps its porters." {n}She folds the bill of lading, and folds it again.{/n}
"There is a portal on the deck that comes out behind this stall, and another behind it that goes back. If you wanted to come up and see her, I would not stop you." {n}The smile arrives, quick and a little sharp.{/n} "Don't read anything into it. It is a professional courtesy. I show all my best customers the ship."''',
       c('"I\'ll come up."', "close", flags=(DOCKED,)),
       c('[Flirt] "All your best customers? I\'d like to meet the competition."', "competition", flags=(DOCKED,))),
    mi("close", '''"Tomorrow, then. I will be busy today being rude to your quartermasters." {n}She tucks the bill of lading into her coat.{/n} "Mind the step when you come through. There is always a step, with portals. Nobody believes me until they've fallen over it."''',
       c("[Leave her to her crates.]")),
    mi("competition", '''"There isn't any. I have never had a best customer in my life; I have had passengers, and cargo, and a great many funerals." {n}She says it lightly, and then hears it, and her colour rises a shade.{/n}
"Tomorrow. Come up tomorrow. And mind the step; there is always a step, with portals."''',
       c("[Leave her to her crates.]")),
], requires=(), forbids=(DOCKED,))


# --- 2. The nearest: what was done with her curse, and her one demand. ----------------------------------------------

deck(D + "nearest", "The nearest", '"I came to see the ship."', [
    nar("start", '''{n}You step through a door of salt light behind the tiefling's stall and fall over the step, exactly as promised, onto a deck a hundred fathoms above Drezen. The wind up here is clean and very cold. The city below is a map of itself.{/n}
{n}Mielarah does not show you the ship. She takes you into her cabin, which is small and brass-bound and scrupulously neat, and shuts the door, and pours two cups of something, and sits down on the far side of her chart table.{/n}''',
        c("Continue", "dead", requires=(OSKEL_DEAD,), forbids=(CUT_DOWN,)),
        c("Continue", "alive", requires=(MINDER, PAID, TOLD), forbids=OSKEL_ALIVE),
        c("Continue", "alive", requires=(MINDER, SECRET_KNOWN), forbids=(TOLD, *OSKEL_ALIVE)),
        c("Continue", "secret", requires=(MINDER,), forbids=(TOLD, SECRET_KNOWN, *OSKEL_ALIVE)),
        c("Continue", "none", requires=(PATTERN,), forbids=(MINDER, OSKEL_DEAD, CUT_DOWN, ZYPHUS_MARK)),
        c("Continue", "dead_cut", requires=(CUT_DOWN, OSKEL_DEAD)),
        c("Continue", "marked", requires=(ZYPHUS_MARK,), forbids=(OSKEL_DEAD,)),
        c("Continue", "none_unread", forbids=(MINDER, OSKEL_DEAD, CUT_DOWN, ZYPHUS_MARK, PATTERN))),
    mi("none_unread", '''"I have been going through my records." {n}She opens the sailcloth book at the front, and turns it round so that you can read it.{/n} "Not who died. Where they were standing. The steward, on the stair below me. My mate, across the binnacle. The girl with the apples, across her counter, taking my copper. Every one of them was the nearest thing to me when it happened. Six years, and I never once added up where they stood."
"Nearest. It takes the nearest." {n}She shuts the book.{/n} "I have been thinking about little else. And the thing I keep coming back to is not the rule. It's you. You're a Trickster, the broadsheets say; the kind that makes a joke and the world goes along with it." {n}She lifts her eyes.{/n} "So tell me, honestly. What would you have done with it, if I had flown you anywhere with a hanging at the end?"''',
       c('"I\'d have put the most dangerous man on your ship at your elbow. And let it take him."', "honest",
         flags=(WOULD, PATTERN)),
       c('"I\'d have stood there myself."', "myself", flags=(PATTERN,)),
       c('[Lie] "Nothing. It\'s your curse."', "nothing", flags=(PATTERN,))),
    mi("marked", '''{n}She does not pour for you at once. She looks at your shoulder, at the place under your coat where the grey spade is, as if she could see through the cloth.{/n}
"I have kept accurate records for six years, Commander. Every name. The steward, my mate, the girl with the apples. Every one of them I put beside me without knowing what I was doing." {n}She pushes the cup across.{/n} "There is no name for that night. There is a line with nothing in it but a date and a place, and in the margin: the Commander, nearest; marked. I did not know how else to write it. I have entered the injury. I shall not enter a death while you are sitting across my table."''',
       c("Continue", "demand")),
    mi("dead", '''{n}A bosun's whistle lies on the chart table between the cups: brass, dented, on a cord gone black with handling.{/n}
"His." {n}She does not touch it.{/n} "It came up out of the sea tangled in the rigging, and none of the crew would take it. I have been carrying it about for weeks like a fool."
"I have kept accurate records for six years, Commander. Every name. The steward, my mate, the girl with the apples. Every one of them I put beside me without knowing what I was doing." {n}Now she picks the whistle up, and turns it over.{/n} "Oskel is the only name on my list that somebody put there on purpose."''',
       c("Continue", "demand")),
    mi("dead_cut", '''{n}A bosun's whistle lies on the chart table between the cups: brass, dented, on a cord gone black with handling.{/n}
"His." {n}She does not touch it.{/n} "The crew took it off him before they put him over the side at Colyphyr, and then none of them would keep it. I have been carrying it about for weeks like a fool."
"I have kept accurate records for six years, Commander. Every name. The steward, my mate, the girl with the apples. Every one of them I put beside me without knowing what I was doing." {n}Now she picks the whistle up, and turns it over.{/n} "Oskel is the only name on my list that somebody sent. Out along my own main yard, with a knife in his teeth, on an order given in two words."''',
       c("Continue", "demand")),
    mi("alive", '''"Oskel is on deck, splicing a line, two dozen strides from me. That is where he stays now. I made it an order." {n}She turns her cup by the handle.{/n}
"I have kept accurate records for six years, Commander. Every name. The steward, my mate, the girl with the apples. Every one of them I put beside me without knowing what I was doing, and I have hated myself for all of them."
"Oskel is alive. So there is no name for him on my list. But there is a space where it would have gone, and you are the one who ruled the line."''',
       c("Continue", "demand")),
    mi("secret", '''"Oskel is on deck, splicing a line." {n}She turns her cup by the handle.{/n} "He stood at my elbow for the whole of the voyage, as you asked, and nothing happened to him. I have been thinking about that."
"I am a magister of the Arcanamirium, Commander. I sit in this cabin at night with nothing but my records, and my records say that the most dangerous man on my ship stood nearest me for three weeks because you asked for the most dangerous man." {n}She lifts her eyes.{/n} "Tell me again why it had to be Oskel. Slowly, this time. I should like to hear it twice."''',
       c('[Tell her the truth] "Because your curse takes the nearest. I wanted it to take him instead of you."', "confess",
         flags=(SECRET_KNOWN, MEANT)),
       c('[Lie] "Because the crew watched him. I told you that in the Bad Luck, and it was true."', "believed")),
    mi("confess", '''{n}She sets the cup down so carefully that it does not make a sound.{/n}
"There." {n}Very quietly.{/n} "That's the figure I kept coming to, and kept rubbing out."
"You lied to me at my own table. I thanked you for it. I told you that you thought like a quartermaster." {n}A breath, held and let go.{/n} "He's alive. That is the only reason this door is still shut and you are still on the right side of it. But I will say it now, once, so that you know it was said: I will not be lied to again about my own curse. Not by you."''',
       c("Continue", "demand")),
    mi("believed", '''{n}She looks at you for the space of three breaths, which is as long as she ever looks at anybody.{/n}
"All right." {n}She drinks.{/n} "I'll take that. I'd rather take it than the other thing." {n}Whether she believes it is not written anywhere on her face; she has had six years of practice keeping things off it.{/n}
"But hear this anyway, whatever you meant by him. It is the thing I brought you up here to say."''',
       c("Continue", "demand")),
    mi("none", '''"Nearest. That is the pattern we have to reckon with. I have checked it against my book until I could recite the entries in the dark."
"I have been thinking about little else. And the thing I keep coming back to is not the rule. It's you. You're a Trickster, the broadsheets say; the kind that makes a joke and the world goes along with it." {n}She lifts her eyes.{/n} "So tell me, honestly. What would you have done with it, if I had flown you anywhere with a hanging at the end?"''',
       c('"I\'d have put the most dangerous man on your ship at your elbow. And let it take him."', "honest",
         flags=(WOULD,)),
       c('"I\'d have stood there myself."', "myself"),
       c('[Lie] "Nothing. It\'s your curse."', "nothing")),
    mi("honest", '''{n}She does not flinch. She had the figure already, you think; she only wanted to hear you read it out.{/n}
"Yes. That is what I would have done too, if I had known. That is the worst of it." {n}She drinks.{/n} "Thank you for not dressing it up."''',
       c("Continue", "demand")),
    mi("myself", '''"You'd have stood there yourself." {n}She repeats it the way she repeats a wrong answer, but her voice has gone uneven.{/n} "That is either the most romantic or the most idiotic thing anyone has ever said in this cabin, and this cabin has carried pirates."''',
       c("Continue", "demand")),
    mi("nothing", '''"Nothing." {n}Her mouth quirks.{/n} "A Trickster with a rule in hand, and nothing. I have flown with pirates, Commander. I know what a lie looks like when it's sitting in my cabin drinking my brandy."
"Never mind. I didn't bring you up here to catch you out. I brought you up here to say one thing."''',
       c("Continue", "demand")),
    mi("demand", '''{n}She leans forward, and puts both hands flat on the chart table, the way a captain leans on a rail in weather.{/n}
"Never again. Whatever my curse is, it is not a tool. It is not a lever or a knife or a clever arrangement of the seating. Nobody stands at my elbow who did not choose to stand there, knowing why. Not a sailor, not a prisoner, not some poor fool you don't care about." {n}Her voice is quite steady.{/n}
"My code is three lines long. You have made me add a fourth. Promise me."''',
       c('[Promise] "Never again. Nobody stands nearest you who didn\'t choose it."', "promised",
         flags=(RECKONED, PROMISED), alignment=("Lawful", 1)),
       c('"I won\'t promise that. If it keeps you alive, I\'ll do it again."', "refused", flags=(RECKONED, NO_PROMISE)),
       c('"Then I\'ll choose it. I\'ll stand there myself."', "stand", flags=(RECKONED, STAND))),
    mi("promised", '''{n}She holds your eyes for a while, looking for the joke. There isn't one, and she sees there isn't, and sits back.{/n}
"A Trickster's promise." {n}She almost smiles.{/n} "I have been told they are worth less than the paper they aren't written on. I am going to believe this one, because I have decided to, and I am a stubborn woman." {n}She picks up her cup again, and her hand is not quite steady.{/n} "Now come and look at the ship. I have been dying to show you the ship."''',
       c("[Go and look at the ship.]")),
    mi("refused", '''"No." {n}She says it for you, as if checking the answer.{/n} "No, you wouldn't promise that. You'd do it again. You'd do it tomorrow, if it came to it, and look me in the eye afterwards."
{n}She sits back, and for a while she only looks at you, and it is not a warm look, and it is not a cold one either.{/n}
"Then I'll watch you. I'll watch everyone who comes near me, and I'll watch you watching them. That's what I've got instead of a promise." {n}She stands.{/n} "Come and look at the ship. I didn't bring you up a hundred fathoms to quarrel."''',
       c("[Go and look at the ship.]")),
    mi("stand", '''"That's not a promise. That's a threat." {n}But her hands have come off the table, and her voice has gone somewhere it has not been in front of you before.{/n}
"You'd stand there. At my elbow. Knowing. Every storm, every market, every stupid dropped crate." {n}She laughs, very quietly, at nothing.{/n} "Six years. Six years of people walking round me like water round a rock, and you want to stand in the way of it."
{n}She gets up, abruptly.{/n} "Come and look at the ship. Before I say something a magister of the Arcanamirium would be embarrassed to have said."''',
       c("[Go and look at the ship.]")),
], requires=(DOCKED,), forbids=(RECKONED,), delay=24)


# --- 3. The best job in the whole world (a flight over Drezen; Lann's line). ---------------------------------------

LANN_ALIVE_CHOICE = c("Continue", "lann", requires=(LANN_HEARD,), forbids=LANN_GUARD)
LANN_NEW_CHOICE = c("Continue", "lann_new", forbids=(*LANN_GUARD, LANN_HEARD))

deck(D + "best_job", "The best job in the whole world", '"You said you\'d show me what she can do."', [
    nar("start", '''{n}This time she does not take you to the cabin. She takes you to the wheel.{/n}
{n}Starcatcher slips her anchor-chains with a noise like a sigh, and the city tilts away beneath you, and then there is nothing under the keel but wind and a long way down. Drezen goes by below, all roofs and smoke and the citadel standing up out of it like a knuckle. To the north the sky over the Worldwound is a lid of red cloud, lit from underneath.{/n}''',
        c("Continue", "wheel", forbids=(SHIP_LOST,)),
        c("Continue", "fourth", requires=(SHIP_LOST,))),
    mi("wheel", '''"The most technologically advanced vessel in the Midnight Isles." {n}She says it the way other women introduce a daughter.{/n} "Alchemical lift-bladders in the hold, three of my own sigils in the keel, and a set of sails cut by a tailor in Absalom who charged me more than the ship. She has been to the Rift of Repose, where the dead demon lords rot in their statues, and come back without a scratch on her paint."
{n}Her hands are easy on the spokes. You have never seen her hands easy before.{/n} "Put yours here. And here. No, don't grip it. She knows what she's doing. You only have to agree with her."''',
       c("Continue", "joy")),
    mi("fourth", '''"She is not the most technologically advanced vessel in the Midnight Isles." {n}She says it with enormous dignity, while the Fourth wallows through a crosswind like a barge.{/n} "She is twenty years old and ugly, and her lift-bladders are patched with a sailcloth I would not have used to wipe the Third's decks. She is also the only ship in the Abyss that will carry me, and she got us through the Wound, and I love her more than is reasonable."
{n}Her hands are easy on the spokes. You have never seen her hands easy before.{/n} "Put yours here. And here. Don't grip. She is old and knows her business. You only have to agree with her."''',
       c("Continue", "joy")),
    nar("joy", '''{n}You put your hands where she says, and the ship comes alive under them: a pull and a lean and a long patient push against the wind, like holding the reins of something much larger than a horse that has decided, for now, to be polite.{/n}
{n}Mielarah stands at your shoulder with her hands behind her back and says nothing for a while. When you glance at her she is not looking at the sky. She is looking at you, holding her ship, and she smiles as the ship answers your hands. Then she checks the northern sky again.{/n}''',
        LANN_ALIVE_CHOICE,
        c("Continue", "sky", requires=("lann.dead",)),
        c("Continue", "sky", requires=("lann.kicked_out",)),
        LANN_NEW_CHOICE),
    mi("lann_new", '''"Your mongrel archer came up yesterday, with a message from your quartermaster that could have gone by runner. He asked if he could hold her. I let him, for a count of ten." {n}She shakes her head.{/n}
"Then he asked me what it was like, being a real captain. I told him the truth: it's the best job in the whole world. He went red to the ears and said he was going to steal that, and say it to everyone." {n}Her smile goes crooked.{/n} "I let him keep it. It's true, whoever says it."''',
       c("Continue", "sky")),
    mi("lann", '''"Your mongrel archer came up yesterday, with a message from your quartermaster that could have gone by runner. He asked if he could hold her. I let him, for a count of ten." {n}She shakes her head.{/n}
"He told me it was the best job in the whole world. I said that was my line, and he'd stolen it, and he went red to the ears and said he'd heard me say it to him in the Bad Luck, the first real captain he ever asked." {n}Her smile goes crooked.{/n} "I'd forgotten. He hadn't. I let him keep it. It's true, whoever says it."''',
       c("Continue", "sky")),
    mi("sky", '''"Now watch." {n}She points north, to where the red lid of the Worldwound's sky comes down to the horizon in a grey curtain of rain, shot through with lightning.{/n} "A squall line, off the Wound. It'll be over Drezen by midnight. Sensible captains turn for home."
{n}She reaches past you and brings the wheel round, gently, a quarter-turn, and the ship heels away from the weather and begins the long curve back toward the city.{/n} "I am a sensible captain now. I didn't use to be."''',
       c('"You flew into storms once."', "storms"),
       c('[Flirt] "You\'re a terrible liar. You want to fly into it."', "want")),
    mi("storms", '''"All the time. Starcatcher the First and I flew into everything the sky had. It was a point of pride." {n}She takes the wheel back from you, gently, spoke by spoke.{/n}
"Then the curse, and the storm that took her, and I came up out of the sea on a hen-coop without a bruise and forty people drowned around me. Since then, I fly round." {n}She does not look at you.{/n} "Every time I see weather now, I hear a spade. Isn't that stupid? A spade, in wet earth, somewhere behind me. I turn the wheel before I've decided to."''',
       c("Continue", "home")),
    mi("want", '''{n}She laughs out loud, and the helmsman on the main deck looks up, startled, as though he had never heard the sound.{/n}
"Of course I want to fly into it. I'm an aeronaut. It's the finest thing there is: the ship on her ear and the rain coming sideways and the whole sky trying to throw you out of it." {n}The laugh goes out of her.{/n} "And every time I see weather now I hear a spade, somewhere behind me, in wet earth. So I turn the wheel before I've decided to."''',
       c("Continue", "home")),
    mi("home", '''"There." {n}Drezen comes up under the keel again, roofs and smoke and the citadel's knuckle.{/n} "That is what she can do. That is the best job in the whole world, and I have spent six years doing half of it."
{n}She glances at you sidelong, as the anchor-chains go down.{/n} "You held her very well, for a landsman. Mind the compass while you congratulate yourself. She was being polite."''',
       c('"She was. So were you."', flags=(FLOWN,)),
       c('"Next time, the storm."', flags=(FLOWN,))),
], requires=(RECKONED,), forbids=(FLOWN,), delay=24)


# --- 3b. Special cargo: the tombs, the Arcanamirium and the Gravedragger (optional; somewhere with fewer ears). ----

deck(D + "special_cargo", "Special cargo", '"There is more to your work for the Arcanamirium than carrying passengers."', [
    mi("start", '''{n}You are in her cabin again, with the door shut and the wind going over the deck above like a hand over a drum. She has taken off her hat and her coat, and without them she looks like what she is under the captaincy: a scholar, thin and precise, with ink on the side of her second finger.{/n}
"Shut the door." {n}She pours, and does not drink.{/n} "There are things the Academy preferred its couriers not to discuss in taverns."
"Very well. Before the curse I was a courier for the Arcanamirium. The Academy digs, you understand. Old sites, sealed vaults, tombs with bad reputations. Somebody has to go in first and carry out what the magisters want, and bring it home without dropping it, and without opening it."''',
       c('"Special cargo."', "cargo")),
    mi("cargo", '''"Special cargo." {n}Something like a smile.{/n} "That's what we called it. I was very good at it. I had a light hand and no imagination, and I could smell a pressure plate through three inches of dust."
"There is a way of walking in a tomb, Commander. You do not hurry, and you do not touch, and you do not read the inscriptions aloud, and when something in the dark says your name you keep walking. The dead are very jealous of their things. Most of them have nothing else left."
{n}She turns her cup.{/n} "I carried out a great many things that were meant to stay where they were. Some of them are in the Academy's vaults. Some of them are not anywhere any more, because the Academy was very sorry to discover what they did."''',
       c('"And Abaddon?"', "abaddon")),
    mi("abaddon", '''"And Abaddon." {n}She sets the cup down.{/n} "A party of Pathfinders went in after something they should not have wanted, and got themselves caught. The Society asked the Academy for a ship that could fly where ships do not fly, and a captain who could walk where they had been. The Academy sent me."
"He was standing over them when I came down the ramp. The Gravedragger. I can tell you he was tall, taller than the room should have allowed, and that something dragged behind him. I never let myself look at it properly, and I will not describe what I did not see. He was taking them one at a time, slowly, not because he had to but because he enjoyed the waiting."
{n}Her voice has gone to that cold, far place, as if it came up out of a grave.{/n} "I walked in the way you walk in a tomb. I did not hurry. I did not look at him. And I took them out from under his hands, every one still breathing, and walked them up my own ramp and flew away."''',
       c("Continue", "spite")),
    mi("spite", '''"He could have killed me on the ramp. He didn't. He watched me go, the whole way up. I think he was deciding how to make it last." {n}She spreads her hands.{/n} "Six years. The steward, the mate, the Pathfinder on my step. I keep counting them, and I am still here to do it. I have come to think that is the joke." {n}She looks at you across the table.{/n} "Now we have put a pattern to it. I have checked it against my dead, and you have come aboard knowing what it means. I think he has noticed that too."''',
       c('"A joke is a thing that can be told differently."', "differently"),
       c('[Take her hand across the table.]', "hand")),
    mi("differently", '''"Spoken like a Trickster." {n}But she is listening.{/n} "Told differently how? Tell me the other version, then. I've heard his a thousand times."''',
       c('"The woman who walked out untouched finds someone to stand beside her who knows the rule. And he has to watch that."', "version",
         flags=(CARGO_TOLD,)),
       c('"I don\'t know yet. I\'ll know when I get there."', "version", flags=(CARGO_TOLD,))),
    mi("hand", '''{n}Her hand is cold, and ink-stained, and for a moment it goes rigid in yours, like a line taking a strain. Then it doesn't.{/n}
"Most people will not even take my hand." {n}She looks at your fingers over hers on the chart.{/n} "You are still here. I wish I could stop waiting for something to fall."
{n}She does not take the hand away.{/n} "You are going to make this very difficult for me, aren't you."''',
       c('"Yes."', "version", flags=(CARGO_TOLD,))),
    mi("version", '''{n}She is quiet for a while. The wind goes over the deck. Somewhere forward a sailor is singing, badly, about a girl in Absalom.{/n}
"I like your version better than his," {n}she says at last.{/n} "I have no reason to think it's true. But I like it better."''',
       c("[Stay until the singing stops.]")),
], requires=(FLOWN,), forbids=(CARGO_TOLD,), delay=12)


# --- 4. Disciplinary thought-correction (the pivotal moral node: what she does to her crew's minds). --------------

deck(D + "correction", "Disciplinary thought-correction", '"I heard shouting on your deck."', [
    nar("start", '''{n}You come up through the portal into the middle of it: two sailors on the main deck, a spilled hand of cards, and a knife out. The crew have made a ring around them the way crews always do, and nobody is stopping it.{/n}
{n}Mielarah comes down the quarterdeck ladder without hurrying. She does not raise her voice. She looks at the man with the knife, and her eyes darken, and something passes between them that you feel in your own teeth like a change in the weather.{/n}
{n}The man puts the knife down on the deck, very neatly, and picks up the cards, and hands them to the other man, and goes forward to the bow with an empty face and stands there looking at nothing.{/n}''',
        c("[Follow her to her cabin.]", "cabin")),
    mi("cabin", '''{n}She sits down on the edge of her bunk as though her strings have been cut, and presses the heels of her hands into her eyes.{/n}
"Disciplinary thought-correction." {n}Her voice is muffled.{/n} "That is what I call it. A tidy phrase for going into a man's head and taking the knife out of his hand from the inside."
"He'll be fine by supper. He won't remember wanting to kill anybody. He never does." {n}She lowers her hands.{/n} "I have done that to every sailor on this ship, Commander. Most of them more than once. Some of them every day."''',
       c("Continue", "amulets", requires=(AMULETS,)),
       c("Continue", "box_first", forbids=(AMULETS,))),
    mi("box_first", '''{n}She reaches under the bunk and brings out a lacquered box, and does not open it.{/n}
"And when there are too many of them at once, I have these. Amulets. Twenty men at a time, like dolls on one string. I have opened this box twice in six years, and both times I was sick over the rail afterwards." {n}Her fingers stay well away from the lid.{/n} "I hate them more than I hate the curse. The curse, at least, is not something I chose."
"Kerz keeps his crew by terror. Nocticula's captains keep theirs with the Lady's name. I keep mine with this, and I tell myself it's kinder, because at least nobody gets flogged." {n}She looks up at you.{/n} "You've seen the whole of it now. The captain with the honest reputation. Tell me what you would do."''',
       c('[Try higher wages] "Double their pay. See whether they can keep the peace without daily correction."', "freed",
         flags=(CORRECTED, FREED), alignment=("Good", 1)),
       c('"Tighten it. A crew is cargo; you said so yourself. Make sure the cargo never shifts."', "tightened",
         flags=(CORRECTED, TIGHTENED), alignment=("Evil", 1)),
       c('[Teach them limericks] "Let me have your crew for an evening. I know a better way to take the knife out of a man\'s hand."', "laughing",
         flags=(CORRECTED, LAUGHING), mythic="Trickster", alignment=("Chaotic", 1)),
       c('"Your crew, your call. I won\'t tell you how to keep your ship."', "kept", flags=(CORRECTED, KEPT))),
    mi("amulets", '''{n}She reaches under the bunk and brings out a lacquered box, and does not open it.{/n}
"And when there are too many of them at once, I have these." {n}The amulets, the ones she wore when the crew rose; you know them by the way her fingers avoid the lid.{/n} "Twenty men like dolls on one string. I hate them more than I hate the curse. The curse, at least, is not something I chose."
"Kerz keeps his crew by terror. Nocticula's captains keep theirs with the Lady's name. I keep mine with this, and I tell myself it's kinder, because at least nobody gets flogged." {n}She looks up at you.{/n} "You've seen the whole of it now. The captain with the honest reputation. Tell me what you would do."''',
       c('[Try higher wages] "Double their pay. See whether they can keep the peace without daily correction."', "freed",
         flags=(CORRECTED, FREED), alignment=("Good", 1)),
       c('"Tighten it. A crew is cargo; you said so yourself. Make sure the cargo never shifts."', "tightened",
         flags=(CORRECTED, TIGHTENED), alignment=("Evil", 1)),
       c('[Teach them limericks] "Let me have your crew for an evening. I know a better way to take the knife out of a man\'s hand."', "laughing",
         flags=(CORRECTED, LAUGHING), mythic="Trickster", alignment=("Chaotic", 1)),
       c('"Your crew, your call. I won\'t tell you how to keep your ship."', "kept", flags=(CORRECTED, KEPT))),
    mi("freed", '''"They are paid already, Commander. Wages do not keep a knife out of a man's hand." {n}She taps her temple.{/n} "I keep them from doing things they cannot undo. The last crew I left alone put the Second on the rocks of Alinythia. I fought my own friends until I was the last one standing."
{n}A shout comes through the cabin door. She listens, then pushes the lacquered box under the bunk.{/n} "But that knife is down. I shall try double wages and a berth ashore for anyone who wants one. No daily correction while they keep the peace. Let us see whether they can manage a watch without it."
{n}She opens the door and calls the bosun over to give him the new orders.{/n} "If they draw steel again, I shall stop them. You may dislike my methods; I still have to get this crew home."''',
       c("Continue", "after", forbids=(AMULETS,)),
       c("Continue", "after_amulets", requires=(AMULETS,))),
    mi("tightened", '''{n}For a moment she only looks at you, and you watch her decide that she heard what she heard.{/n}
"Cargo." {n}She looks from you to the lacquered box.{/n} "I honour the cargo entrusted to me. You would have me use that to excuse making dolls of my crew."
{n}She opens the lacquered box, and takes out one of the amulets, and closes her fist on it.{/n} "It would work. That's the terrible thing. They would never shift again. They'd never mutiny, never quarrel, never laugh either." {n}Her knuckles are white. Then she puts the amulet back and shuts the lid.{/n}
"No. I am not going to fly a ship of dolls because a customer thinks it tidier. But I won't pretend I'm above it, either; the last crew I let alone put the Second on the rocks." {n}She sets the box on the shelf over her bunk, where she can reach it without bending.{/n} "The box stays out. Any man who draws steel on my deck from tonight goes under the amulet on the spot, for one watch, in front of everyone, and his name goes in the log. That is my order, not yours. You would make a very good pirate, Commander. I have met a great many, and I have decided not to become one."''',
       c("Continue", "after", forbids=(AMULETS,)),
       c("Continue", "after_amulets", requires=(AMULETS,))),
    mi("laughing", '''"Limericks." {n}She stares at you.{/n} "You are going to stand on my main deck and recite obscene verse to a crew of Midnight Isles cutthroats, and you think that will..."
{n}She stops. Something is happening at the corner of her mouth, against her will.{/n} "Yes. All right. I should like to hear what you can say to this lot that I cannot." {n}She puts the lacquered box back under the bunk.{/n} "One evening. If anyone draws a knife, I'm going in with my head, and you will not say a word about it afterwards."
{n}That evening you recite, from the rigging, for two hours. By the end the crew is teaching you verses you did not know, and one of them is about her.{/n}''',
       c("Continue", "after", forbids=(AMULETS,)),
       c("Continue", "after_amulets", requires=(AMULETS,))),
    mi("kept", '''"Quite." {n}She puts the box under the bunk and rises at another shout from the deck.{/n} "There are men aboard who would have cut a throat over that card game. Now they will eat supper together. I would rather correct a thought than bury a sailor."
{n}At the door she calls for the two gamblers. Neither is willing to meet her eye.{/n} "Separate watches for you both. And the knife stays in the galley."
{n}She turns back to you.{/n} "They came out of the Abyss. Some of them may yet make decent sailors. That is why I took them aboard, and why I bother. They are still my crew." {n}She takes the gamblers up to their new watch stations.{/n} "Let us see them earn their supper."''',
       c("Continue", "after", forbids=(AMULETS,)),
       c("Continue", "after_amulets", requires=(AMULETS,))),
    mi("after", '''{n}Mielarah stands and straightens her coat. Her fingers catch on one button; she starts again.{/n}
"That is how the honest ship keeps an honest crew. I reach into their heads. The other captains would laugh themselves sick if they knew how much I hate doing it."
{n}At the cabin door she stops.{/n} "Thank you for listening. Now go down. I have orders to give, and I would rather give them without an audience."''',
       c("[Go back through the portal.]")),

    mi("after_amulets", '''{n}Mielarah stands and straightens her coat. Her fingers catch on one button; she starts again.{/n}
"You saw the amulets on the voyage. The men went back to their lines. Their ringleader walked off the rail. He woke before he hit the water."
"I went below because I could still feel it. Then I had to come back and give the next order. That is how I keep an honest ship."
{n}She opens the cabin door.{/n} "Go down, Commander. I have a crew to deal with."''',
       c("[Go back through the portal.]")),

], requires=(FLOWN,), forbids=(CORRECTED,), delay=24)


# --- 5. The market: her curse in Drezen, and what the Commander will spend to keep her here. -----------------------

deck(D + "market", "Nearest, in Drezen", '"Something happened in the market."', [
    nar("start", '''{n}Something has. The crowd in the market square has pulled back into a ragged ring, and inside it, where the scaffolding round the mason's yard used to stand, there is a heap of timber and a smell of plaster dust, and a boy's boot sticking out from under it at the wrong angle.{/n}
{n}Mielarah is standing three strides from the heap with her hands at her sides. She had been buying rope. The coil is still over her shoulder.{/n}
{n}Nobody else was touched. Of everyone in the square, the mason's apprentice had simply been the closest: he had stepped in under the scaffold to ask whether the foreign captain wanted her rope carried.{/n}''',
        c("Continue", "crowd")),
    nar("crowd", '''{n}A crusader officer pushes through the ring with two of his men behind him and stops a careful distance from her. You know his type: a decent man, frightened, and ashamed of being frightened in front of his soldiers.{/n}
{n}"Commander." He salutes you, and does not look at her. "Beg your pardon. The people are saying the Abyss captain brings death with her. That's the third accident in the square in a week. They want her gone. I'd not ask it, but I've got a street full of them, and they've lost their boy."{/n}
{n}Mielarah says nothing. She has lowered the rope from her shoulder, and is holding it in both hands, like a mourner holding flowers.{/n}''',
        c('"She stays. The city answers to me, and so do its funerals."', "stays", flags=(MARKET, STAYS)),
        c('"Then when she comes down, she\'ll have a condemned man from the cells at her elbow. Let the curse take someone who has it coming."', "prisoner",
          flags=(MARKET, PRISONER), alignment=("Evil", 1)),
        c('"Then I walk beside her. Every time she comes down, I\'m the nearest thing to her in the square."', "escort",
          flags=(MARKET, ESCORTED))),
    mi("stays", '''{n}Before the officer can salute, Mielarah lifts the coil of rope between you.{/n}
"Your order will not stop another scaffold falling. I left my home rather than keep burying people who happened to meet me."
{n}She hands the coil to the officer at its full length.{/n} "I shall trade from above the walls. My crew can bring the cold iron through the portal without me. No porters aboard while I am loading; no passengers near the helm. Tell your quartermaster he gets his cargo at the gate. I am not coming into this square again."
{n}The officer nods and sends a soldier to fetch the quartermaster. She looks up toward Starcatcher.{/n} "Your wounded still need a ship. That is reason enough to stay within reach. Fewer loads, more journeys, and I pay the crew for them. You can come aboard; I shall not bring my curse to your neighbours for the pleasure of seeing you."''',
       c("Continue", "boy")),
    mi("prisoner", '''{n}The officer blinks, and looks at you, and then at her, and does not quite understand what he has been told. She understands at once.{/n}
"No." {n}The word comes out of her like something breaking.{/n} "No. Not a sailor, not a prisoner, not some poor fool you don't care about. I said it in my cabin. I said it as plainly as I have ever said anything."
"You want to walk a condemned man through the square beside me like a dog on a leash and wait for a cornice to fall on him. You'd make a gallows of me." {n}Her hands are shaking on the rope.{/n} "I will moor so high your city will need a glass to see my lanterns. I will come down when the square is empty. And I will never, ever let you choose who stands beside me again."''',
       c("Continue", "worked_out", requires=(LIED,), forbids=(SECRET_KNOWN,)),
       c("Continue", "boy", requires=(SECRET_KNOWN,)),
       c("Continue", "boy", forbids=(LIED,))),
    mi("worked_out", '''{n}And then something else crosses her face, slowly, like the shadow of a cloud crossing a deck.{/n}
"A man at my elbow. Chosen by you. For the curse to take instead of me." {n}She is not looking at the officer any more. She is looking at you.{/n} "You've done this before. You did it in the Bad Luck, with a pencil in my hand, and you told me it was to steady the crew."
"Oskel." {n}Her voice is almost gentle.{/n} "You lied to me about Oskel. A bodyguard, you said. I wanted that to be all he was. Now I know why it had to be him." {n}She breathes out.{/n} "Thank you for showing me. I would never have been sure, otherwise."''',
       c("Continue", "boy", flags=(SECRET_KNOWN, MEANT))),
    mi("escort", '''{n}The officer looks at you as though you had announced you would take a walk inside a burning barn. Then he salutes, and goes, and the crowd goes with him, slowly, looking back.{/n}
"You'll walk beside me." {n}She has not moved.{/n} "In the market. Every time. The nearest thing to me in the square, with the scaffolds and the cart horses and the cornices." {n}Her voice has gone thin.{/n} "You know what you are volunteering for. I will have to watch it coming for you."
"I'll moor higher all the same. I'll come down when the square is empty, and I'll send for you first, and you'll come, because you've said you will, and I'll spend every minute of it listening for the spade." {n}She looks at the boot under the timber.{/n} "That's what it costs me. Remember it."''',
       c("Continue", "boy")),
    mi("boy", '''{n}She kneels down by the heap of timber, out of habit, at the distance she always keeps, and then, deliberately, closer.{/n}
"What was his name? Does anybody know his name?" {n}She asks the square, not you. A woman at the edge of the ring says something, and Mielarah repeats it under her breath, twice, the way you would fix a bearing.{/n}
"Somebody find his mother. Tell her the captain of Starcatcher pays for the burial, and the timber, and whatever else she asks for, and tell her it was an accident." {n}She stands.{/n} "It was. That's the worst of it."''',
       c("[Help clear the timber.]")),
], requires=(CORRECTED,), forbids=(MARKET,), delay=24)


# --- 6. The wheel (the commit): she lets go in flight, and the Commander holds the course. ---------------------------

INTIMACY = [
    nar("lash", '''{n}She takes a becket from its peg and lashes the wheel, two turns and a hitch, without looking at her hands, the way she has done it a thousand times on a thousand quiet watches. She checks the compass, then the forward watch. Starcatcher holds steady.{/n}
{n}Up here, above the clouds, there is nobody. The watch is forward, the crew below; the quarterdeck is open to the whole sky, and the whole sky is stars. It is very cold. Her breath smokes, and so does yours.{/n}
"Six years," {n}she says, and does not finish it, and puts her hands on your coat.{/n}''',
        c("[Kiss her.]", "kiss"),
        c('"Six years of what?"', "years")),
    mi("years", '''"Six years of watching people edge away." {n}She works the buckles of your coat, pulls it open, and presses her cold fingers beneath your collar.{/n} "I have had enough of distances, Commander. I want your mouth on mine." {n}She draws you against her.{/n} "Stop talking."''',
       c("[Kiss her.]", "kiss")),
    nar("kiss", '''{n}Her mouth warms against yours. She catches your lower lip, then kisses you harder, both hands under your coat. Her hat strikes the planks. She leaves it there.{/n}
{n}A shout comes from the forward watch: steady wind. She listens, nods, and pulls your coat off your shoulders. Her fingers return beneath your collar at once.{/n}''',
        c("[Undo her coat.]", "coat")),
    nar("coat", '''{n}Her captain's coat has more buttons than any garment has a right to, and she laughs at you for the second half of them and then does the last three herself, impatiently, and shrugs it off and drops it in the lee of the rail, brass buttons rattling on the planks.{/n}
{n}She presses against you, warm through her shirt. Your mouth finds her throat; she tips her head back, then catches your collar and brings your mouth to hers again. Her fingers fumble once at a buckle. She swears under her breath and tries again.{/n}''',
        c("Continue", "threshold")),
    mi("threshold", '''{n}She pulls you down with her onto the coat and the cold planks, into the lee of the rail, and the ship sways under you both, and she holds on as if you might be the thing that rolls overboard.{/n}
"If anything falls," {n}she breathes against your throat, fierce and unsteady,{/n} "a block, a spar, a star, I don't care, if anything falls tonight I want it to fall on both of us. Do you hear me? Both of us or neither."
{n}Her hands are at your belt. Yours are at hers. Above you the lashed wheel creaks a quarter-turn and holds, and the stars wheel over the mast, and she pulls you down the last of the way.{/n}''',
        c("[The ship holds her course.]", flags=(NIGHT,))),
]

deck(D + "wheel", "Hold her", '"You are taking Starcatcher out tonight?"', [
    nar("start", '''{n}She is waiting at the wheel when you come through the portal. It is night. The anchor is already up. Starcatcher is standing north toward the Worldwound, and ahead of her, where the stars should be, there is a wall.{/n}
{n}Grey, and higher than mountains, and lit from inside by lightning that has no sound yet. The squall line off the Wound, the one she turned away from last time.{/n}
{n}"I said I'd show you something," she says, without turning round. "It's on the other side of that. I have not flown into weather of my own choosing in six years. I'm going to fly into this."{/n}''',
        c("Continue", "why")),
    mi("why", '''"I put the crew ashore in Drezen at sunset, all but four who asked to come and know what for, at triple pay. I told them the truth. Two of them laughed." {n}She does not.{/n} "Don't ask me why. I have been turning it over since our flight, and the best answer I have is that you held her very well, for a landsman, and I want to know what happens next." {n}Her hands are easy on the spokes. They will not stay that way.{/n}
"Stand where you're standing. There. At my elbow." {n}She glances at you once, sidelong.{/n} "You know what that place is. You know what it's for. Stand there anyway."''',
       c("[Stand at her elbow.]", "storm")),
    nar("storm", '''{n}The storm takes the ship like a fist. Rain comes sideways, hard as gravel, and the deck goes up on its ear, and the rigging howls, and somewhere below a sailor is praying out loud to a god you don't recognise.{/n}
{n}Mielarah flies it. She flies it the way she must have flown the First, before everything: bare-headed, soaked to the skin, laughing into the wind, the wheel spinning under her hands and coming back, the ship climbing and climbing through the dark. For a while it is the finest thing you have ever seen anyone do.{/n}
{n}Then the lightning shows you her face, and it has gone the colour of the rain.{/n}''',
        c("Continue", "spade", requires=(STORM,)),
        c("Continue", "spade_first", forbids=(STORM,))),
    mi("spade_first", '''"Do you hear it?" {n}She has to shout.{/n} "Tell me you hear it."
{n}And you do: under the wind, patient and slow and very far down, the sound of a spade going into wet earth. Once. Again.{/n}
"This is how the First went down. Weather like this, and that sound under it, and I walked away from her and counted the dead afterwards." {n}Her knuckles are white on the spokes. The ship is shuddering.{/n} "I have been afraid for six years that one day it will come up behind me at a wheel and my hands will open on their own. I can feel them wanting to."
"So listen to me." {n}She turns her head, and her eyes are wide and very clear.{/n} "I'm going to let go. On purpose, before they do it for me. Take her. Hold her."''',
        c("Continue", "letgo")),
    mi("spade", '''"Do you hear it?" {n}She has to shout.{/n} "Tell me you hear it."
{n}And you do: under the wind, patient and slow and very far down, the sound of a spade going into wet earth. Once. Again.{/n}
"This is where I let go." {n}Her knuckles are white on the spokes. The ship is shuddering.{/n} "The last time. I felt it come up behind me and I felt my hands open and I watched them do it. I am going to feel it again. I am feeling it now."
"So listen to me." {n}She turns her head, and her eyes are wide and very clear.{/n} "I'm going to let go. On purpose, this time. Take her. Hold her."''',
       c("Continue", "letgo")),
    nar("letgo", '''{n}Her hands open. She lets go of the wheel.{/n}
{n}It spins. The ship heels over hard, and the whole storm leans on the rudder, and every loose thing on the deck begins to slide toward the rail, and she stands there with her empty hands at her sides, nearest, in the rain, and does not reach for it again.{/n}''',
        c('[Hold the course] Take the wheel, and hold her head into the storm.', "held", flags=(COMMITTED, COURTSHIP)),
        c('[Turn her for home] Take the wheel, and bring her round out of the weather.', "home", flags=(DECLINED,))),
    nar("held", '''{n}You take the wheel. It fights you like a living thing, and you do not grip it, and you agree with it, and you hold her.{/n}
{n}The ship comes up. Something cracks aloft and a block comes down out of the dark and splits on the deck a hand's breadth from your boot, and nothing else happens. The spade goes into the earth once more, far off, and then the wind takes the sound and does not give it back.{/n}
{n}And then the storm is under you. Starcatcher breaks out of the top of it into silence and starlight, into a sky so clear and cold and full that it looks like a spilled jewel box, with the whole grey roof of the storm spread out below the keel, lightning moving in it like fish.{/n}''',
        c("Continue", "above")),
    mi("above", '''{n}She has not moved. She is standing exactly where she stood, at your elbow, soaked, with her hands open, looking at you and not at the stars.{/n}
"You held her." {n}She looks at the split block on the deck, and at your boot beside it, and back.{/n} "It fell beside your boot. I saw it coming. I could not take my hands back."
{n}She puts her hand over yours on the spokes, the way she corrects a helmsman: two fingers, a little pressure, a quarter-spoke to port. The ship answers. She does not take the hand away.{/n} "Stay there," {n}she says.{/n} "That's an order. I'm captain again; I've decided."''',
        c("[Kiss her.]", "kiss_first"),
        c('"I\'m staying."', "kiss_first")),
    nar("kiss_first", '''{n}She comes the last half-step on her own, soaked and shaking and laughing a little, and kisses you over the wheel with her cold hands on either side of your face. The ship holds her course without either of you. She has always been a good ship.{/n}''',
        c("[Stay up here with her.]", "lash"),
        c("[Take her home.]", "take_home")),
    mi("take_home", '''"Home." {n}She says it as though she had never heard the word applied to Drezen before, and is considering it.{/n} "Yes. Take her down, Commander. Slowly. I want to watch you do it."
{n}She stands at your elbow the whole way down, and does not take the wheel back once.{/n}''',
        c("[Bring her down to Drezen.]")),
    mi("home", '''{n}You bring her round. The ship comes out of the weather into the lee of it, rolling, and the lightning falls behind, and the sound of the spade falls behind with it.{/n}
{n}Mielarah takes the wheel back from you. Her hands are perfectly steady now.{/n}
"That was sensible." {n}She says it without any expression at all.{/n} "It was exactly what a sensible captain does. It's what I've been doing for six years." {n}She does not look at you.{/n} "I didn't want sensible from you. I wanted... never mind what I wanted. I shouldn't have asked it of anyone."''',
        c("Continue", "home_after")),
    mi("home_after", '''"Don't look like that. You didn't do anything wrong. You kept my ship off the bottom. I am not going to complain about that." {n}She brings Starcatcher down toward the city's lights.{/n}
"I'll be over Drezen a while yet. There's cargo." {n}A pause, the length of a breath.{/n} "Perhaps when there's no war and no curse and no storm, I'll ask you something else. Don't hold your breath, Commander. I'm very slow about everything but flying."''',
        c("[Say nothing.]")),
    *INTIMACY,
], requires=(MARKET,), forbids=(COMMITTED, DECLINED, OSKEL_DEAD, MEANT), delay=48,
    ForbidOverrides={OSKEL_DEAD: SETTLED, MEANT: SETTLED})


# --- 6b. The quarterdeck, another night (after a commit that ended on the ground). -------------------------------

deck(D + "quarterdeck", "Above the clouds", '"Starcatcher\'s going up tonight?"', [
    mi("start", '''"She is. No storms. I checked the sky three times, which I never do, and my crew think I have gone soft." {n}She is waiting at the wheel with her hat under her arm, and she does not give you the wheel this time. She takes you up herself, through the thin cloud over Drezen, until the city is a smudge of lamplight under a white floor and there is nothing above you but the stars.{/n}
"I brought you here to show you this, the other night. I didn't get round to it." {n}She looks up, and then at you.{/n} "That's a lie. I got round to all sorts of things. I simply didn't get round to this."''',
       c("Continue", "lash")),
    *INTIMACY,
], requires=(COMMITTED,), forbids=(NIGHT,), delay=12)


# --- 7. The morning: the block on the planks, and the Gravedragger's regard. -------------------------------------

deck(D + "morning", "The block on the planks", '[Wake on the quarterdeck.]', [
    nar("start", '''{n}You wake under her captain's coat, stiff with cold, with frost on the rail and the sun coming up over a floor of cloud so white it hurts. The ship is still holding her course. The lashed wheel has not moved.{/n}
{n}Mielarah is already up and dressed, bare-headed, standing at the rail with her arms folded. She is looking at something on the planks.{/n}
{n}It is a block: a heavy ironwood pulley from the main yard, split clean in two. It lies on the deck exactly where your head was, a foot to the left.{/n}''',
        c("Continue", "block")),
    mi("block", '''"It came down in the night." {n}She does not look up from it.{/n} "I heard it. I was awake. It hit the planks there, where you'd been lying, and you'd rolled over in your sleep a moment before and taken most of my coat with you."
"You were nearest. You were the nearest thing to me on this whole ship, all night." {n}She crouches, and picks up half the block, and weighs it in her hand.{/n} "And it missed."
{n}She looks at you, then, and you see she has not slept, and that she has been standing at that rail since the block fell, with something going through her like a tide.{/n} "You must be special. I would like a better explanation than that. I have been standing here since the block fell, and I have not found one."''',
       c('[Joke] "I rolled over. That\'s the whole trick."', "joke"),
       c('"Come here."', "come")),
    mi("joke", '''"You rolled over." {n}She laughs, and it cracks halfway, and she puts the half-block down very gently on the planks as if it could still hurt somebody.{/n}
"You rolled over and took my coat. He dropped a block on the place you had just left." {n}She laughs again, unsteadily.{/n} "I spent the rest of the night watching the rigging. You slept through the whole damned thing." {n}She wipes her eyes with the back of her wrist, briskly.{/n}''',
       c("Continue", "spade")),
    mi("come", '''{n}She comes, and sits down against you in the lee of the rail, under the coat, and puts her cold face in your neck and stays there, breathing.{/n}
"I stood there all night listening for it to try again," {n}she says into your collar.{/n} "It didn't. It tried once and missed and it didn't try again."''',
       c("Continue", "spade")),
    mi("spade", '''"But I heard something else. Before the sun." {n}Her voice changes; it goes to the cold far place.{/n} "The spade. Not behind me, where it always is. Somewhere else, and slow, and not digging for me at all."
"The Gravedragger has noticed you. I have met him once, in Abaddon, and I have lived six years inside his joke. That is all the acquaintance I can claim, and it is enough. You know the pattern. You held my wheel through that weather, and the block missed." {n}She looks out at the white floor of the clouds.{/n} "He is Zyphus's herald, and heralds do not forget being made fools of. He cursed me for taking those Pathfinders out of his hands in Abaddon. I don't know what he'll do about you. I know he'll take his time."''',
       c('"Let him dig."', "shield"),
       c('[Trickster] "Then I\'ll have to keep standing where he can\'t reach me."', "shield")),
    mi("shield", '''{n}She turns toward you under the coat. Her face is tired; the smile reaches her eyes.{/n}
"I have walked away from wrecks that killed the people around me." {n}She taps her own breastbone.{/n} "Still breathing. I don't know how long he means to let that last. I'm a magister; I'll call it an observation, and keep observing."
"So here's mine. If the observation holds, then whatever he sends for you will have to come past me first. I'm going to be the nearest thing to you, Commander, for as long as I can manage it." {n}She pulls the coat up over both of you.{/n} "Let him dig round that."''',
       c("Continue", "crew", forbids=OSKEL_ALIVE),
       c("Continue", "crew_new", requires=(OSKEL_DEAD,)),
       c("Continue", "crew_new", requires=(SHIP_LOST,), forbids=(OSKEL_DEAD,))),
    nar("crew", '''{n}When the two of you finally come down the quarterdeck ladder, the crew are extraordinarily busy with ropes that do not need coiling. Nobody looks up. The cook whistles a limerick under his breath and stops, too late.{/n}
{n}Oskel is at the foot of the mainmast, splicing. He looks at the two of you, and at the distance between you, which is no distance at all, and nods once to you, the way a bosun nods to a new officer.{/n}
{n}"Ma'am's elbow's taken, then," he says, to nobody in particular, and goes back to his splice.{/n}''',
        c("[Go back down to Drezen.]", flags=(MORNING, NOTICED))),
    nar("crew_new", '''{n}When the two of you finally come down the quarterdeck ladder, the crew are extraordinarily busy with ropes that do not need coiling. Nobody looks up. The cook whistles something under his breath and stops, too late.{/n}
{n}The half-block lies where it fell. Mielarah picks it up on the way past, and weighs it, and puts it in her coat pocket.{/n}
{n}"Ballast," she says, to nobody, and opens the portal for you herself.{/n}''',
        c("[Go back down to Drezen.]", flags=(MORNING, NOTICED))),
], requires=(NIGHT,), forbids=(MORNING,), delay=6)


# --- 8. The other captains (after the morning): the wager in the Bad Luck. ---------------------------------------

deck(D + "captains", "The other captains", '"You\'ve had post from the Midnight Isles."', [
    mi("start", '''{n}She has. It came through the little portal on her chart table: three letters and a parcel, all from the Bad Luck, and she has read the letters twice and not opened the parcel at all.{/n}
"The captains of the Midnight Isles have heard about you." {n}She hands you the top letter between two fingers.{/n} "They have opened a book. On how long you last."
{n}The odds are written in a clumsy hand, and underneath them the names of the bettors: half the sky-captains of Alushinyrra, a quartermaster of the Lady in Shadow, and one entry in blood-brown ink with a knife drawn beside it.{/n}''',
       c("Continue", "kerz")),
    mi("kerz", '''"Kerz." {n}She taps the knife.{/n} "Got-Stabbed. He has bet a hundred gold that you'll be dead by the spring, and another hundred that it'll be something stupid, like a dropped anchor. He has written, very kindly, that he would be happy to take me off your hands afterwards, and that he has always admired a woman who can't be killed."
{n}Her lip curls, and for a moment she is exactly the woman in the Bad Luck who wanted pirates hanged from the yardarm.{/n} "Every pirate in the Midnight Isles has tried to buy my ship. Kerz is the only one who ever tried to buy it with a compliment. I have never been so insulted in my life."''',
       c('[Trickster] "Take his bet. Put everything on me."', "bet"),
       c('"What\'s in the parcel?"', "parcel")),
    mi("bet", '''{n}She looks at you, and then she laughs until she has to sit down.{/n}
"Everything on you. Against Kerz." {n}She wipes her eyes.{/n} "You know he'll try to rig it. He'll hire somebody to drop an anchor on your head from a great height."
"All right. Everything I've got on you, and I'm writing to tell him so, and I'm going to enjoy every word." {n}She pulls a sheet of paper toward her and begins, in the small upright magister's hand, and says without looking up:{/n} "Open the parcel, would you? I haven't had the nerve."''',
       c("Continue", "parcel")),
    nar("parcel", '''{n}Inside the parcel, wrapped in oilcloth, is a length of blue silk: a captain's sash of the Midnight Isles, the kind the aeronauts' guild of Alushinyrra gives when a captain has flown a ship through somewhere nobody flies. There is a note pinned to it in a round, unfamiliar hand.{/n}
{n}"For Starcatcher, through the Wound. The captains drank to it. Some of us even meant it."{/n}''',
        c("Continue", "sash")),
    mi("sash", '''{n}She holds it for a long time without speaking. When she does, her voice is not quite in order.{/n}
"Six years. They gave me their respect because I was stubborn and their ire because I was honest, and they left a stool empty at every table I sat at." {n}She runs the silk through her fingers.{/n} "And now they've drunk to me, because I flew somewhere stupid."
"Your crusade is going to march on something soon, Commander. Everybody in the city says so; the quartermasters are buying rope as if it were bread. When it goes, it will need carrying. Supplies up, wounded back." {n}She folds the sash, carefully, and puts it away.{/n} "Starcatcher carries cargo. I'll go where you go. At my usual rates."''',
       c('"Minus nothing?"', "rates", flags=(CAPTAINS,)),
       c('"I\'ll want you nearest."', "rates", flags=(CAPTAINS,))),
    mi("rates", '''"Minus everything." {n}The smile, quick and sharp.{/n} "You're not a customer any more. You're the one who stands at my elbow. I am told there is no rate for that in any guild schedule in the Midnight Isles, and I checked."
{n}She goes back to her letter to Kerz, and writes a line, and reads it over, and adds another with enormous satisfaction.{/n} "There is room on this ship for a great many passengers, Commander. There is exactly one wheel. Remember that, whoever else you carry."''',
       c("[Leave her to her letter.]")),
], requires=(MORNING,), forbids=(CAPTAINS,), delay=48)



# --- Optional beats between the flights: the captain's table, a stowaway, Oskel, the stern, the eve of the march. ----

SUPPER = D + "supper"
STOWAWAY = D + "stowaway"
OSKEL_SPOKE = D + "oskel_spoke"
STERN = D + "stern"
LAST_NIGHT = D + "last_night"

deck(D + "supper", "The captain's table", '"Your crew eats at the captain\'s table?"', [
    nar("start", '''{n}They do, at the end of the first dog-watch, with the sky going red over Drezen below the keel.{/n}''',
        c("Continue", "chair", forbids=(SHIP_LOST,)),
        c("Continue", "crate", requires=(SHIP_LOST,))),
    mi("chair", '''{n}The officers eat in the great cabin under the quarterdeck, with the stern windows open: a navigator with ink to the elbows, a sailmaker with a voice like a rusty hinge, and a first mate, a grey-winged tiefling woman who says nothing whatever and eats as if the food had insulted her. And there is a chair at the captain's right hand, pulled out a little from the table, laid with a plate and a cup, and nobody sits in it. The steward serves round it as if it were a pillar.{/n}
"The Commander's chair," {n}she says, quite lightly, to the table, as you come in.{/n} "Or anybody's. It's always laid. It's never sat in. The crew have a superstition about it, which is not a superstition at all, since every man who ever sat in it is dead."
{n}The navigator coughs into his wine. The first mate goes on eating.{/n} "Sit wherever you like, Commander. The sailmaker's elbow is very safe. He has survived three shipwrecks and a marriage."''',
       c("[Sit in the empty chair.]", "sat"),
       c("[Sit at the sailmaker's elbow.]", "safe")),
    mi("crate", '''{n}The Fourth has no great cabin, only a space behind the helm with a canvas roof and a crate for a table. Five hands and a captain eat off it with their plates on their knees. But there is still a crate at her right hand with a cup set on it, and nobody sits on that crate.{/n}
"The Commander's crate," {n}she says, to the four new faces and the one bored one, as you duck under the canvas.{/n} "Or anybody's. The crew have a superstition about it, which is not a superstition. They've heard what happened to the Third, and to everyone who ever sat near me on her."''',
       c("[Sit on the empty crate.]", "sat"),
       c("[Sit on the deck with the crew.]", "safe")),
    nar("sat", '''{n}You sit. Everyone goes perfectly silent. Somewhere below a pump thumps and stops. The lamp overhead sways on its chain, a finger's width, back and forth, and every eye at supper watches it except hers.{/n}
{n}She moves your cup an inch from the table's edge and picks up her fork.{/n}
{n}"The Commander," she says, "has been told the rule, and chooses to ignore it. Pass the salt, and stop looking at the lamp, the lot of you."{/n}''',
        c("Continue", "rift")),
    nar("safe", '''{n}You take the safe place. Nobody says anything, and nobody needs to; you watch the relief go round the supper like a draught of wine.{/n}
{n}Mielarah says nothing either. But once, halfway through the meal, while two of her people are arguing about a wind, you see her look at the empty place at her right hand, and then at you, with an expression you cannot read, and then away.{/n}''',
        c("Continue", "rift")),
    mi("rift", '''"Somebody always wants to know about the Rift of Repose." {n}She says it with the air of a woman who has been asked the same question at every supper for three years.{/n} "Everyone wants to know about the Rift of Repose. The place where the dead demon lords go to rot inside their own statues."
"We went in on a charter for a scholar who wanted a sketch of one of the statues. We sketched it. On the way out, the statue opened its eyes and asked the scholar, very politely, to stay." {n}A sip of wine.{/n} "He stayed. We did not. I flew Starcatcher out of that rift sideways, at a speed she was not built for, with my hat in my teeth. I have never once been able to describe it at supper without somebody telling me I've got the wind wrong."''',
       c('[Toast her] "To the manoeuvre."', "toast"),
       c('"And the scholar?"', "scholar")),
    mi("scholar", '''"Still there, I expect. Sketching." {n}She does not smile.{/n} "He was not nearest me when it happened. He was nearest the statue. I have always found that a comfort, which tells you what sort of comfort I've had to make do with."''',
       c('[Toast her anyway] "To the manoeuvre."', "toast")),
    nar("toast", '''{n}Everyone drinks. Afterwards the crew return to their watches. Mielarah stays at the table, turning her cup between two fingers.{/n}
"Absalom's harbour smelled of tar and oranges. At night the Arcanamirium had a lamp in every window. You could come in after midnight and still find someone to quarrel with."
{n}She sets the cup down. A watchman calls from the bow.{/n}
"I miss it. There. That is the part I dislike saying aloud. Pour me another before I start listing the people I miss."''',
        c("[Stay and listen.]", flags=(SUPPER,))),
], requires=(FLOWN,), forbids=(SUPPER,), delay=8)


deck(D + "stowaway", "The stowaway", '"Is that Woljif in your hold?"', [
    nar("start", '''{n}It is. Mielarah comes up out of the forward hatch dragging him by the back of his coat, the way a cook drags a sack of onions, and deposits him on the deck at your feet. He has a pistol in each hand. Both of them are hers.{/n}
{n}"Chief! Chief. Tell her. Tell her I was lookin' after 'em for her."{/n}''',
        c("Continue", "know")),
    mi("know", '''"I know you." {n}She takes the pistols back, one at a time, without looking at them, and checks that each is still loaded.{/n} "You drank on credit at the Bad Luck for a month and paid the barman in coins that turned into beetles on the Toilday. The barman still talks about you. He keeps a jar of the beetles behind the bar."
{n}Woljif looks at you with an expression of enormous dignity, ruined somewhat by the cobweb in his hair. "Them beetles was a misunderstandin', Cap'n."{/n}''',
       c("Continue", "threat")),
    mi("threat", '''"Of course they were." {n}She crouches, at the distance she always keeps, and looks at him with polite academic interest, and her eyes darken very slightly.{/n} "I could reach into your head, Master Woljif, and tidy up the part of it that thinks my pistols are its business. It would take me a moment. You'd hardly notice. You'd simply never want to steal from me again."
{n}Woljif goes the colour of old porridge. "Chief."{/n}''',
       c('[Vouch for him] "He\'s mine, Captain. I\'ll answer for him."', "vouch"),
       c('"Let her tidy it. He\'ll thank you later."', "scare"),
       c('[Trickster] "I\'ll bet you he can lift your hat off your head before you finish the spell."', "bet",
         mythic="Trickster")),
    mi("vouch", '''"You'll answer for him." {n}She straightens, and the darkness goes out of her eyes.{/n} "Then you owe me two pistols' worth of trust, Commander, and I shall collect it at a time of my choosing."
"And you." {n}This to Woljif, who is sidling toward the portal.{/n} "If you want to see an airship, you ask the captain, like a person. I show all my best customers the ship."
{n}He stops sidling. "...Yeah? Could I hold the wheel?" She looks at him, and at you, and sighs.{/n} "For a count of ten."''',
       c("[Let him have his count of ten.]", flags=(STOWAWAY,))),
    mi("scare", '''{n}She checks the pistols once more and puts them in her belt.{/n}
"No. He is not my crew. I have my guns back. There is nothing left to correct." {n}She looks toward Woljif, who is inching toward the portal.{/n} "But he need not know that. Master Woljif, try my hold again and you will learn how I deal with thieves."
{n}He goes through the portal so fast he trips over the step on the far side. You hear him swearing all the way across the market.{/n}''',
       c("[Watch him go.]", flags=(STOWAWAY,))),
    nar("bet", '''{n}Mielarah raises an eyebrow and begins a word in some tongue that makes your teeth ache. Woljif does not wait for the second syllable. His hand goes up and back and down again, and her tricorn is in it, feather and all, and he is holding it to his chest like a baby.{/n}
{n}There is a silence on the deck. Then the helmsman laughs, and the lookout laughs, and after a moment, helplessly, so does Mielarah.{/n}
{n}"Keep it," she tells him, still laughing. "No, don't keep it, that's my good hat. Give it back and I'll give you a count of ten on the wheel, you appalling little thief."{/n}''',
        c("[Let him have his count of ten.]", flags=(STOWAWAY,))),
], requires=(DOCKED,), forbids=(STOWAWAY, *WOLJIF_GUARD), delay=24)


deck(D + "oskel", "What he was for", '"Oskel wants a word?"', [
    nar("start", '''{n}He does, though he does not say so. He is on the main deck when you come up through the portal, splicing a line, and he does not look up, and he does not move out of your way either. You understand that this is how a bosun asks for a word.{/n}
{n}Up close he is even bigger than he looked in the Bad Luck. The slaver's brand on his neck is old and white and very neat. Somebody took a great deal of care with it.{/n}''',
        c("Continue", "why")),
    nar("why", '''{n}"Captain says you picked me." He goes on splicing. His voice is low and careful, like a man carrying something full to the brim. "For the elbow. Because I'm the one'd do it."{/n}
{n}He tucks a strand, pulls it tight, and looks at you at last. His eyes are yellow and perfectly calm.{/n}
{n}"Figured. Man learns what he's for, on a slaver's deck. They teach it with a hot iron. I was cargo before I was crew." He puts the fid down. "So I'm askin'. Was you right? Would I have?"{/n}''',
        c('"Yes. On a bad enough day, with her in your head and her attention somewhere else, you would have."', "yes"),
        c('"I don\'t know. I didn\'t have to find out. That was the point."', "dont_know"),
        c('"No. I think you\'d have caught the rope. But I couldn\'t take the chance."', "no")),
    nar("yes", '''{n}He nods, slowly, as if you had confirmed the price of rope.{/n}
{n}"Yeah. Me too." He picks up the fid again. "Six years she was in my head, keeping me decent. Hated it some days. Other days I was glad, 'cause I knew what was under." He works the fid into the lay. "Nobody else ever paid me. Not a copper. Only her."{/n}''',
        c("Continue", "ask")),
    nar("dont_know", '''{n}He grunts. It might be a laugh.{/n}
{n}"Didn't have to find out. That's clever." He picks up the fid. "Clever's what they are in the palaces in Alushinyrra. Didn't like 'em much." A pause. "Six years she kept me decent from inside my own head. Nobody else ever paid me. Not a copper. Only her."{/n}''',
        c("Continue", "ask")),
    nar("no", '''{n}He looks at you a while, as if deciding whether you are the kind of person who says kind things for no reason. Then he looks at his splice.{/n}
{n}"Maybe." He picks up the fid. "Six years she was in my head, keeping me decent. Still can't tell which bits is me." He works it into the lay. "Nobody else ever paid me, though. Not a copper. Only her. I'd have caught the rope. I think."{/n}''',
        c("Continue", "ask")),
    nar("ask", '''{n}He finishes the splice, and rolls it under his boot, and stands up, which takes a while, like watching a building decide to stand.{/n}
{n}"Captain's got nobody at her elbow now. Made it an order. Twenty strides, she says. For my own good." He does not look toward the quarterdeck, where she is. "Somebody should stand there. Somebody as knows why. Not me. Not somebody picked."{/n}
{n}He looks at you with his calm yellow eyes. "You, maybe. Seein' as you know the rule so good."{/n}''',
        c('"I intend to."', "end", flags=(OSKEL_SPOKE,)),
        c('"That\'s her choice, not mine."', "end", flags=(OSKEL_SPOKE,))),
    nar("end", '''{n}"Right," says Oskel, and picks up his coil, and goes forward, twenty strides from his captain, exactly.{/n}
{n}On the quarterdeck Mielarah has watched the whole of it with her glass under her arm, too far off to hear. When Oskel passes below her she says one word to him, and he answers with one word, and she nods, and turns back to the northern sky as if she had been waiting for somebody's permission to look at it.{/n}''',
        c("[Leave him to his work.]")),
], requires=(RECKONED, MEANT), forbids=(OSKEL_SPOKE, *OSKEL_ALIVE), delay=12)


deck(D + "stern", "A name on the stern", '"You asked for a steady pair of hands?"', [
    nar("start", '''{n}She did. She is sitting in a bosun's chair slung over Starcatcher's stern, a hundred fathoms above Drezen, with a paint pot hooked to the rope beside her and a brush in her hand, and she wants somebody at the rail to pay out the line and not drop her.{/n}
{n}"The crew won't do it," she calls up, over the wind. "They say it's bad luck to paint a dead man's name. They're sailors of the Midnight Isles. They say everything is bad luck. They are usually right."{/n}''',
        c("[Take the line.]", "paint", forbids=(CUT_DOWN, STORM)),
        c("[Take the line.]", "paint_cut", requires=(CUT_DOWN,)),
        c("[Take the line.]", "paint_storm", requires=(STORM,), forbids=(CUT_DOWN,))),
    mi("paint_cut", '''{n}You pay out the line, and she goes down the stern a little at a time, and under the ship's name, in small white letters, she begins to paint another.{/n}
"O. S. K." {n}She talks while she paints, not to you exactly, in the rasp the rope left her.{/n} "He could not read. I taught him his own name, the first year, with chalk on the capstan. He was so angry that it only had five letters. He'd thought it would be longer, a man that size."
"He liked sweet things. He stole sugar from the galley and pretended he hadn't. He sang, badly, in the heads, where he thought nobody could hear." {n}The brush moves.{/n} "He stood at the rail at Vazglar and did nothing, and then he flew ashore for you, and went up to my yard and cut me down. He was nearest. Somebody sent him."''',
       c('"I sent him."', "you_cut"),
       c("[Hold the line and say nothing.]", "quiet")),
    mi("you_cut", '''"You did." {n}She does not look up.{/n} "I was at the end of a rope at the time, so I cannot say I let you. But I have asked you to hold this one, and I thought that was fair. You can let go any time, you know. The crew say I would survive the fall. They're probably right about that as well."
{n}She finishes the last letter, and blows on it, which does nothing at all at this height, and then sits back in the chair and looks at it, swinging gently over the drop.{/n}''',
       c("Continue", "done")),
    mi("paint", '''{n}You pay out the line, and she goes down the stern a little at a time, and under the ship's name, in small white letters, she begins to paint another.{/n}
"O. S. K." {n}She talks while she paints, not to you exactly.{/n} "He could not read. I taught him his own name, the first year, with chalk on the capstan. He was so angry that it only had five letters. He'd thought it would be longer, a man that size."
"He liked sweet things. He stole sugar from the galley and pretended he hadn't. He sang, badly, in the heads, where he thought nobody could hear." {n}The brush moves.{/n} "At Vazglar he had the noose on me before I'd finished a sentence, because he was nearest. He always was. Then the block split, and the line took him over the rail instead. He was nearest, and somebody put him there."''',
       c('"I put him there."', "you"),
       c("[Hold the line and say nothing.]", "quiet")),
    mi("paint_storm", '''{n}You pay out the line, and she goes down the stern a little at a time, and under the ship's name, in small white letters, she begins to paint another.{/n}
"O. S. K." {n}She talks while she paints, not to you exactly.{/n} "He could not read. I taught him his own name, the first year, with chalk on the capstan. He was so angry that it only had five letters. He'd thought it would be longer, a man that size."
"He liked sweet things. He stole sugar from the galley and pretended he hadn't." {n}The brush moves.{/n} "When my hands came off the wheel in the hurricane, his went on. He held her a whole minute, head into the wind, all by himself. Then the mast came down across the helm. He was nearest, and somebody put him there."''',
       c('"I put him there."', "you"),
       c("[Hold the line and say nothing.]", "quiet")),
    mi("you", '''"You did." {n}She does not look up.{/n} "And I let you. I've put the brush in your hand, as it were, by asking you to hold this rope. I thought that was fair. You can let go any time, you know. The crew say I would survive the fall. They're probably right about that as well."
{n}She finishes the last letter, and blows on it, which does nothing at all at this height, and then sits back in the chair and looks at it, swinging gently over the drop.{/n}''',
       c("Continue", "done")),
    mi("quiet", '''{n}She finishes the last letter, and blows on it, which does nothing at all at this height, and sits back in the chair, swinging gently over the drop, looking at the small white name under the large gold one.{/n}
"Accurate records." {n}Her voice is not quite steady.{/n} "Every one of the others, I kept in a book. Him I wanted somewhere the whole sky could read."''',
       c("Continue", "done")),
    mi("done", '''"Pull me up, Commander. Slowly." {n}And as you haul her up hand over hand, and she comes over the rail with paint on her cuffs:{/n} "Thank you for not dropping me. And for not letting go of the rope, when I told you that you could."
{n}She stands close for a moment, closer than she needs to, with the brush still in her hand.{/n} "I would not have taken you into weather with his name still in a book in my cabin, where nobody else could read it. I want you to know that. The next time I put your hands on my wheel, it will be because this is done." {n}Then she goes to wash the brush.{/n}''',
       c("[Coil the line.]", flags=(STERN,))),
], requires=(RECKONED, OSKEL_DEAD), forbids=(STERN,), delay=12)


deck(D + "last_night", "Before the march", '"The quartermasters say the crusade marches soon."', [
    nar("start", '''{n}They do, and the quartermasters are right, and Starcatcher is loading. For three days the portal behind the tiefling's stall has not closed: crates of bandages, barrels of pitch, cold-iron arrowheads in straw, all going up through a door of salt light into a hold a hundred fathoms over the city. Mielarah stands beside it with her bill of lading and ticks everything off in her small upright hand, and the porters bring the crates to a chalk line on the cobbles and go no further.{/n}
{n}She sees you, and finishes the line she is writing, and puts the pencil behind her ear, which you have learned means she is going to say something she has rehearsed.{/n}''',
        c("Continue", "carry")),
    mi("carry", '''"Supplies up, wounded back, for as long as your war needs carrying. I have told your quartermasters so, and they have written it down, and one of them tried to negotiate my rates and has gone to lie down." {n}She looks at the portal, and not at you.{/n}
"I'll be over whatever field you're on. You won't see me, most days. You'll see my lanterns. If you look up at night and there are three lanterns in a line where there shouldn't be a star, that is Starcatcher, and I am at the wheel, and I am not flying round anything."''',
       c("Continue", "token")),
    mi("token", '''{n}She takes something out of her coat pocket and puts it in your hand, and closes your fingers over it with both of hers, briskly, like a captain handing over a sealed order.{/n}
"Don't open your hand until I've finished. I'm a magister; I'm entitled to one dramatic gesture a year."''',
       c("Continue", "whistle", requires=(OSKEL_DEAD,)),
       c("Continue", "block", forbids=(OSKEL_DEAD,))),
    mi("whistle", '''{n}It is a bosun's whistle: brass, dented, on a cord gone black with handling.{/n}
"His. I've carried it long enough. I'd like it carried by somebody who's still standing where he stood." {n}Her hands stay closed over yours a moment longer.{/n} "If it's bad, blow it. I won't hear it, I'll be a hundred fathoms up. But you'll remember that somebody would have come, and that is most of what a whistle is for."''',
       c("Continue", "end")),
    mi("block", '''{n}It is half of an ironwood pulley block, split clean, with the grain showing white where it broke.{/n}
"It fell beside you after our night above the clouds. I heard it hit. I've been carrying it about like a saint's knucklebone." {n}Her hands stay closed over yours a moment longer.{/n} "Keep it in your pocket. When you're standing somewhere stupid, with something coming down on you, put your hand on it and remember that it missed once."''',
       c("Continue", "end")),
    mi("end", '''"He's still digging, you know." {n}She says it very quietly, under the noise of the porters.{/n} "Every night, somewhere a long way down. I don't know what he's digging, and I don't know who he'll send when he's finished. But when it comes to the end of all this, Commander, whatever the end is, I'll be the nearest thing to you that I can manage to be."
{n}She lets go of your hands, and takes the pencil from behind her ear, and is the captain again.{/n} "Go on. You have a war to finish, and I have forty crates of pitch to count, and one of these porters is about to drop something."''',
       c("[Leave her counting.]", flags=(LAST_NIGHT,))),
], requires=(CAPTAINS,), forbids=(LAST_NIGHT,), delay=48)



# --- Path beats: the Fourth (after the storm), the other voyage (after a charter), and after her soft no. ---------

FOURTH = D + "fourth"
OTHER_VOYAGE = D + "other_voyage"
AFTER_NO = D + "after_no"

deck(D + "fourth", "Starcatcher the Fourth", '"Your ship is leaking on my market."', [
    nar("start", '''{n}She is. A thin, steady drizzle comes down out of a clear sky onto the cobbles behind the tiefling's stall, and the trader has put a bucket under it with an expression of deep personal injury.{/n}
{n}When you come up through the portal, Mielarah is on her knees on the Fourth's deck with her coat off and her sleeves rolled, driving oakum into a seam with a mallet and a caulking iron. Her hands are black with pitch to the wrist. She does not get up.{/n}
"Hold this," {n}she says, and hands you the pitch pot, and goes on hammering.{/n}''',
        c("Continue", "seam")),
    mi("seam", '''"Twenty years old. Every seam in her opens a finger's width in a crosswind and closes again in a calm, like a mouth deciding whether to speak." {n}The mallet comes down, and down.{/n} "The Third never leaked. The Third was the finest ship in the Midnight Isles. I had her charts in my cabin going back six years, and a figurehead of Desna that a carver in Absalom made with my face on it, which I pretended to be embarrassed by."
"All of it's at the bottom of the Ishiar now. The charts, the figurehead, the sketches from the Rift. My good hat." {n}She sits back on her heels.{/n} "I had my hands on her wheel, and I let go."''',
       c("Continue", "owned", requires=(STORM_OWNED,)),
       c("Continue", "blamed", forbids=(STORM_OWNED,))),
    mi("owned", '''"You said it was the wrong order. You said it to my face with salt still in my hair, and I have been living on that like hardtack." {n}She takes the pitch pot back from you.{/n} "It was the wrong order. And I was the wrong captain for it. Both of those can be true. Magisters are trained to hold two contradictory results at once and wait for a third experiment."''',
       c("Continue", "third_exp")),
    mi("blamed", '''"You said I let go of the wheel. You were right. You're the only person who has ever said it to my face, and I think it is the kindest thing anyone has done for me since Abaddon, because nobody else would say it and I needed somebody to." {n}She takes the pitch pot back from you.{/n} "Everybody else says it wasn't my fault. It was my fault. I would like very much to be allowed to have done something."''',
       c("Continue", "third_exp")),
    mi("third_exp", '''{n}She looks along the Fourth's deck: the patched sails, the pumps, the five new hands doing their best not to be within two strides of her.{/n}
"But she got us through the Wound. And she's mine. I bought her with the fare you paid for a voyage I didn't finish, which means, strictly speaking, that you own a share in her." {n}The quick, sharp smile.{/n} "I'll send you an account of her running costs. It will make you weep."''',
       c('[Take the mallet] "Show me where the next seam is."', "caulk", flags=(FOURTH,)),
       c('"She\'s ugly. I like her."', "ugly", flags=(FOURTH,))),
    nar("caulk", '''{n}She shows you. You caulk the next seam badly, and she takes the mallet back and does it again properly, and then, without comment, hands it back to you for the one after that. By the time the drizzle over the market has stopped, your hands are as black as hers, and she has told you about every seam on the ship by name, as if they were crew.{/n}''',
        c("[Wash your hands in the rain-barrel.]")),
    mi("ugly", '''"She is ugly." {n}Fiercely.{/n} "She is the ugliest ship that has ever flown through the Worldwound, and she did it with a cursed captain and five terrified hands and a hold full of cold iron, and the Third never did anything half so brave." {n}She puts her pitch-black hand flat on the deck, gently, the way you might put a hand on a horse's neck.{/n} "Say it again, Commander. She likes it."''',
       c("[Say it again.]")),
], requires=(DOCKED, SHIP_LOST), forbids=(FOURTH,), delay=24)


deck(D + "other_voyage", "The ship you chose", '"You wanted to hear about the voyage."', [
    mi("start", '''"I did not want to hear about it. I wanted to hear about it without asking." {n}She is in her cabin, with the charts of the Midnight Isles spread across the table and a glass weighting each corner.{/n} "But you are here, and I am a professional, and professionals learn from their competitors. Tell me. Who flew you to Colyphyr instead of me?"''',
       c("Continue", "kerz", requires=(KERZ,)),
       c("Continue", "nocta", forbids=(KERZ,))),
    mi("kerz", '''"Kerz." {n}She says the name as if it had a smell.{/n} "Got-Stabbed. You sailed to Colyphyr with a man who sells his passengers' fingers back to them at a markup. And you are alive, and I understand you came back with all your fingers."
"I have been trying to decide whether that makes you very clever or Kerz very stupid. I have settled on both." {n}She moves a glass on the chart.{/n} "Was it the price? Tell me it was the price. I could bear it being the price."''',
       c('"It was the price."', "price"),
       c('"I wanted to know what you\'d do if I didn\'t hire you."', "test")),
    mi("nocta", '''"One of the Lady in Shadow's ships." {n}She says it very evenly.{/n} "A captain hand-picked by Nocticula, a crew of her sky wolves, her banner at the masthead. The safest ship in the Midnight Isles, and the most expensive, because what you pay her is not in gold."
"I have been trying to decide whether you are very clever or very much in debt. I have settled on both." {n}She moves a glass on the chart.{/n} "Was it the safety? Tell me it was the safety. I could bear it being the safety. I am not, by any measure, safe."''',
       c('"It was the safety."', "price"),
       c('"I wanted to know what you\'d do if I didn\'t hire you."', "test")),
    mi("price", '''"Of course it was." {n}She lets out a breath.{/n} "A sensible passenger. Everyone told me you were a Trickster, and you went and made the one sensible decision available to you in the whole of Alushinyrra." {n}Something in her face eases, and something else does not.{/n}
"Well. You're here now, and so am I, and I flew through the Worldwound to get here, which none of them would do. I'll take that as the result of the experiment."''',
       c("[Help her roll up the chart.]", flags=(OTHER_VOYAGE,))),
    mi("test", '''{n}She stares at you. Then she puts both hands over her face and laughs into them, helplessly, for quite a long time.{/n}
"You sailed with somebody else," {n}she says through her fingers,{/n} "to find out whether I would come anyway."
"And I did. Through the Worldwound, with a hold full of rope, because you sent for an honest ship after sailing with {n}(her voice climbs){/n} somebody worse." {n}She takes her hands away.{/n} "That is the most outrageous thing anyone has ever done to me, and I have been cursed by a herald of Zyphus. Help me roll up this chart before I throw it at you."''',
       c("[Help her roll up the chart.]", flags=(OTHER_VOYAGE,))),
], requires=(DOCKED, CHARTER), forbids=(OTHER_VOYAGE, LANDFALL, RETURNED), delay=24)


deck(D + "after_no", "Your gloves", '"You kept something of mine?"', [
    mi("start", '''"Your gloves. You left them on the binnacle, the night of the storm." {n}She holds them out across the full width of her circle of empty cobbles, at arm's length, the way she hands everybody everything.{/n} "I have had them cleaned. The salt was ruining them."
{n}She is perfectly pleasant. She is wearing the courteous smile, the one from the Bad Luck, the one that settles on her face like a hat.{/n}''',
       c('"Are we all right?"', "right"),
       c("[Take the gloves.]", "gloves")),
    mi("right", '''"We are perfectly all right. You are my best customer, and Starcatcher will carry your crusade's cargo for as long as it needs carrying. I am a professional." {n}The smile does not move.{/n}
"You turned for home. It was the sensible thing and I asked for something else, and that was my mistake, not yours. I have made worse ones. I made one in Abaddon that I have been paying for ever since." {n}She holds the gloves out a little further.{/n} "Take your gloves, Commander. My arm is getting tired."''',
       c("[Take the gloves.]", "gloves")),
    mi("gloves", '''{n}You take them. Her fingers do not touch yours; she has held them by the very ends of the cuffs.{/n}
"I will not ask you to hold that course again." {n}She says it lightly, and it isn't light.{/n} "I asked once, in the only way I know how to ask anything, and you answered. If you ever want to give a different answer, you know where my ship is. It is the only thing in the sky over Drezen with three lanterns in a line."
{n}She turns back to her crates.{/n} "Good day, Commander."''',
       c("[Leave her to her crates.]", flags=(AFTER_NO,))),
], requires=(DECLINED,), forbids=(AFTER_NO, COMMITTED), delay=24)



# --- A war beat: wounded from the Wound (her code against her curse; optional, after the correction). -------------

WOUNDED = D + "wounded"
WOUNDED_CARRIED = D + "wounded_carried"
WOUNDED_LEFT = D + "wounded_left"

deck(D + "wounded", "Those in distress", '"A column was cut up in the Wound. They need a ship."', [
    nar("start", '''{n}They do. A supply column was caught in the open two days north of the walls, in the red-lit badlands where nothing good grows, and the riders who got back say there are forty men lying in a dry streambed with a demon warband between them and the wagons.{/n}
{n}Mielarah hears it from you beside the tiefling's stall, standing in her circle of empty cobbles, and her face does the complicated thing and then does not settle on courtesy at all.{/n}
"Forty wounded," {n}she says,{/n} "and six passenger places. Five stretchers if you come. We shall have to keep flying until they are all out."''',
        c("Continue", "sum", forbids=(P + "rock.slavers_refused",)),
       c("Continue", "sum_refused", requires=(P + "rock.slavers_refused",))),
    mi("sum", '''"You know what happens near me. So do I." {n}She is speaking fast, and very evenly.{/n} "Six at a time. Another landing under arrows for every load. A stretcher slips. A lantern falls. A splinter in the wrong place, a fever that should have broken. We may go for forty and bring home thirty-five. Thirty."
"And my code says I never ignore those in distress." {n}Her hands have gone still at her sides.{/n} "I can keep them forward and stay at the wheel. Every sortie still puts wounded men aboard a cursed ship. Tell me what you would do. Quickly."''',
       c('"Fly. Put them in the forward hold, as far from the wheel as the ship allows. I\'ll stay at your elbow on every sortie."', "carry",
         flags=(WOUNDED, WOUNDED_CARRIED)),
       c('"Leave them to the wagons. Five dead on your ship is five your curse took. You don\'t owe the Wound that."', "left",
         flags=(WOUNDED, WOUNDED_LEFT))),
    nar("carry", '''{n}She flies. You go with her. Three lanterns above the red badlands mark the ship to the men below; she orders them lowered close to the streambed before the first landing.{/n}
{n}Five stretchers on each load, leaving your place at the helm. The crew haul from the forward hatch, beyond your station; the surgeon stays with the patients. You remain half a stride from Mielarah through loading, flight and unloading. When a line jams aft, she brings the ship down before anyone approaches.{/n}
{n}A block falls beside your boot on the fourth sortie and bounces overboard. The lanterns stay lit. By dawn the streambed is empty. One man dies of his wound before the hospital, despite the surgeon's work. Thirty-nine come home.{/n}''',
        c("Continue", "home")),
    mi("home", '''{n}She brings Starcatcher down over the hospital yard at dawn and stands at the wheel while the stretchers go out, and does not come down off the quarterdeck until the last one is gone.{/n}
"Thirty-nine." {n}Her voice is hoarse. She has not sat down in a day and a night.{/n} "I counted them off. I count everything. Thirty-nine."
"And one, who would have died anyway. I asked the surgeon twice. I made him swear it on his mother." {n}She looks at you, standing where you stood all night.{/n} "You stayed nearest on every flight. The block fell beside you, not into the stretchers. It missed. I am recording what happened, not promising what happens next." {n}She shakes her head, slowly.{/n} "I'm going to have to write a paper about you, Commander. The Arcanamirium will think I've gone mad."''',
       c("[Help her down the ladder.]")),
    mi("left", '''{n}She stares at you. You watch her hear it, and hear it again, and put it down on the scale beside the other thing, and watch the scale not move.{/n}
"The wagons." {n}Very quietly.{/n} "The wagons are two days away and there's a warband in the road."
"No. You're right, and it's sensible, and I'm going anyway." {n}She is already turning toward the portal.{/n} "Six on each flight. I'll put them forward. I'll lash myself to the wheel and I won't come off the quarterdeck. If the curse takes five, it takes five, and I'll write their names down, and they'll be five names instead of forty." {n}At the portal she stops.{/n} "My code has three lines, Commander. I don't get to keep only the convenient ones. Neither, I think, do you."''',
       c("Continue", "alone")),
    nar("alone", '''{n}She goes without you. Starcatcher comes and goes through a day and a night, six stretchers at most on each flight. At dawn her last load reaches the hospital yard. Her captain stands at the wheel while the surgeon counts the survivors.{/n}
{n}Thirty-six. You hear it from the surgeon, not from her. She does not come down from her ship that day, or the next.{/n}''',
        c("[Let her be.]")),

    mi("sum_refused", '''"Forty wounded, and a warband between them and the wagons. I am going."
{n}She takes the loading list from her coat and turns it over.{/n} "I told you I would not ask you about my code again. I have not changed my mind. The wounded go in the forward hold, as far from the wheel as I can put them."
"I am asking whether you will come. Stand at my elbow on every sortie while we bring them home. You know what might fall on you."''',
       c('"Fly. Put them in the forward hold, as far from the wheel as the ship allows. I\'ll stay at your elbow on every sortie."', "carry",
         flags=(WOUNDED, WOUNDED_CARRIED)),
       c('"You will have to fly without me."', "left_refused", flags=(WOUNDED, WOUNDED_LEFT))),

    mi("left_refused", '''"Very well. The forward hold, and I stay at the wheel."
{n}She turns toward the portal, folding the list as she goes.{/n} "I shall bring back as many as I can. Tell the hospital to have stretchers ready."''',
       c("Continue", "alone")),

], requires=(CORRECTED,), forbids=(WOUNDED,), delay=12)



# --- After the morning: the place at her elbow, set in brass (optional). -------------------------------------------

THE_PLACE = D + "the_place"

deck(D + "the_place", "The Commander's place", '"Why is your carpenter cutting up the quarterdeck?"', [
    nar("start", '''{n}Because she has told him to. When you come up through the portal the ship's carpenter is on his knees beside the wheel with a chisel and a rule, cutting a shallow groove across the planks half a stride to the right of the helm, and Mielarah is standing over him with her arms folded, correcting the angle.{/n}
{n}Beside him on the deck lies a strip of brass as long as your forearm, polished bright.{/n}''',
        c("Continue", "brass")),
    mi("brass", '''"Half a stride from the wheel. Close enough that I can find you without turning my head." {n}She looks at the groove, then at the carpenter's hands.{/n} "I have spent enough time watching who stands there."
"I'm having it marked. A brass strip in the planking. Nobody is posted there. Nobody is ordered there. Nobody stands on it at all, ever, unless they have chosen to, knowing why."''',
       c("Continue", "measure")),
    mi("measure", '''{n}The carpenter sets the brass in the groove and taps it home with the heel of his chisel, and gets up, and backs away from it and from her at the same time, which takes some doing.{/n}
"The crew have already started calling it something." {n}The quick, sharp smile.{/n} "I won't tell you what. Sailors of the Midnight Isles have filthy minds. The polite version is 'the Commander's place', and I have decided to allow the polite version on my deck and fine anyone who uses the other one a day's rum."
"I need somebody to stand on it. To see if it's in the right place." {n}She looks at you at last.{/n} "Get on it, Commander. That's an order. It's my deck."''',
       c("[Stand on the brass.]", "stand"),
       c('[Trickster] "It\'s a quarter-inch too far aft. I can tell by standing on it with my eyes shut."', "joke")),
    nar("stand", '''{n}You step onto the brass. It is half a stride from the wheel, to the right, exactly where her hand falls when she reaches out without looking; you know, because she does it, and her hand finds your sleeve and stays there.{/n}
{n}The carpenter finds urgent business forward. The helmsman, who has the wheel, suddenly needs to study the weather very closely in the opposite direction.{/n}
{n}"It's in the right place," she says, after a while, and does not take her hand away.{/n}''',
        c("[Stay on it.]", flags=(THE_PLACE,))),
    mi("joke", '''"A quarter-inch." {n}She looks at the brass, and at you, and at the carpenter, who is looking at the brass with the face of a man whose rule has just been insulted.{/n}
"Stand on it, then. With your eyes shut. Let us test your quarter-inch." {n}You do. Her hand, reaching out without looking, the way it always has, finds your sleeve exactly where it expects to.{/n}
"It's in the right place," {n}she says, very softly, so that only you can hear, and does not take her hand away.{/n} "Don't let the carpenter hear you were joking. He has a temper."''',
       c("[Keep your eyes shut a moment longer.]", flags=(THE_PLACE,))),
], requires=(MORNING,), forbids=(THE_PLACE,), delay=24)



# --- After the market: her book of the dead, and the page at the back (optional). ---------------------------------

NAMES = D + "names"
NAMED = D + "named"

deck(D + "names", "Accurate records", '"You wrote his name down. The boy under the scaffold."', [
    nar("start", '''{n}She did. You find her in her cabin with the lamp trimmed low and a book open on the chart table: a thick ledger bound in old sailcloth, its corners worn round, its spine mended twice with sail-twine. The pen lies beside it, parallel to the edge of the page.{/n}
{n}She leaves the book open and lays her pen beside the newest entry.{/n}
"Aldo Venn," {n}she says, without looking up.{/n} "Apprentice to the mason on the east side of the square. Fourteen. He wanted to carry my rope because I was foreign and he had never seen an airship close to. His mother told me that. She told me a great deal, standing on the far side of the timber, and I wrote down all of it."''',
        c("Continue", "book")),
    mi("book", '''"You may look. I would rather you looked than stood there wondering whether you're allowed." {n}She turns the book round on the table so that it faces you.{/n}
{n}The entries are small, upright and very clear. Each entry has a line to itself, ruled in pencil: a name, a date by the Absalom calendar, a place, and a few words of manner. A steward: tea, the east stair, his neck. A first mate: lightning out of a clear sky, across the binnacle. A Pathfinder: a carriage horse, on her own step. A girl: apples.{/n}
{n}There are pages of them. Near the front the ink has gone brown and the lines are crowded, as if they were written in a hurry by someone who expected to need the room. Later they spread out, one to a line, with space between, the hand of a woman who has understood that she will be doing this for the rest of her life and has decided to do it properly.{/n}''',
       c("Continue", "column")),
    nar("column", '''{n}Down the right-hand edge of every page, in fresher ink than the rest, runs a column that was not there when the pages were ruled. It has been squeezed into the margin afterwards, in a hand made even smaller than usual to fit.{/n}
{n}Half a stride, on the stair below. Across the binnacle, an arm's length. The step below mine. Across the counter. At my elbow. At my elbow. At my elbow.{/n}
{n}She has gone back through six years of her dead and written down where each of them was standing.{/n}''',
        c('"When did you do this?"', "when"),
        c("[Turn the pages. Say nothing.]", "pages")),
    mi("when", '''"After I learned it had a rule. I took the book out at night and went through the entries one at a time. Where was the steward? On the stair below me, with the tray. Where was my mate? Across the binnacle, leaning over the chart with me. The girl with the apples?" {n}She touches the page, very lightly, not quite on the ink.{/n} "Across a counter no wider than this table. I could have reached out and taken the apple from her hand."
"Magisters are taught to record the observation first and the theory afterwards. I had six years of observations and no theory. Then I had a theory, and I had to go back and see whether my own records agreed with it." {n}A small, dry breath.{/n} "They did. Every page. I have never in my life wanted so badly to be wrong about a result."''',
       c("Continue", "last")),
    nar("pages", '''{n}You turn them. She lets you. The ship leans under the table, a long slow lean and back, and the lamp swings on its chain, and the columns of names swing with it.{/n}
{n}Some entries carry more than the manner, a few words after, in the same hand. He owed me four silver and I never asked for it. She had a son in Kerse. I did not know his name until the inquest; I have added it. One line has been written, scored through, and written again underneath more neatly, as if the first attempt had not been accurate enough.{/n}
{n}Toward the end the lines grow crowded again. These are the Midnight Isles: sailors, mostly, and dock hands, and a harbour clerk of Alushinyrra entered as the clerk with the green seal, name not known, enquiries made. Three times over, enquiries made.{/n}''',
        c("Continue", "last")),
    mi("last", '''{n}The newest entry is darker than the rest, the ink not yet gone matte. Aldo Venn, mason's apprentice. Drezen, the market square. A scaffold. He asked to carry my rope. And in the margin, in the new column: three strides; he stepped in.{/n}
"He stepped in." {n}She reads it aloud, flatly, as if checking a figure against an instrument she does not trust.{/n} "Three strides was where I was keeping everyone. I had drawn the line on the cobbles in my head, and I kept it, and a boy who wanted to be kind to a stranger walked over it."
"That is what the column cannot hold, Commander. I can write down where they stood. I cannot write down why they came closer. The steward came closer because I had asked for tea. Aldo came closer because he was fourteen."''',
       c("Continue", "oskel", requires=(OSKEL_DEAD,), forbids=(CUT_DOWN,)),
       c("Continue", "space", requires=(MEANT,), forbids=(OSKEL_DEAD,)),
       c("Continue", "blank", forbids=(OSKEL_DEAD, MEANT, SELF, REFUSED)),
       c("Continue", "oskel_cut", requires=(CUT_DOWN, OSKEL_DEAD)),
       c("Continue", "blank_self", requires=(SELF,), forbids=(OSKEL_DEAD, MEANT)),
       c("Continue", "blank_withdrawn", requires=(REFUSED,), forbids=(SELF, OSKEL_DEAD, MEANT))),
    mi("oskel_cut", '''{n}She turns back a few pages, into the Midnight Isles, and lays a finger beside one line without touching it. Oskel, bosun. And in the margin, where every other line says where somebody was standing, his says: on the main yard; sent up.{/n}
"Every other entry in this book says where they stood. His is the only one that says who sent him there." {n}She does not say your name. She does not need to.{/n} "I wrote it with my own neck still purple. I thought about leaving the column empty, the way I leave it for a stranger whose name I never learned. That would not have been accurate."''',
       c("Continue", "last_page")),
    mi("oskel", '''{n}She turns back a few pages, into the Midnight Isles, and lays a finger beside one line without touching it. Oskel, bosun. And in the margin, where every other line says where somebody was standing, his says: at my elbow; posted there.{/n}
"Every other entry in this book says where they stood. His is the only one that says who put him there." {n}She does not say your name. She does not need to.{/n} "I wrote it the night after. I thought about leaving the column empty, the way I leave it for a stranger whose name I never learned. That would not have been accurate."''',
       c("Continue", "last_page")),
    mi("space", '''"Oskel is not in here." {n}She turns back a few pages, into the Midnight Isles, to a place where the ruled pencil lines leave a gap a little wider than the others.{/n} "But there is room for him. I didn't mean to leave it. I noticed afterwards, when I came to rule the next line, that my hand had left a space exactly the width of one name."
"I'm not going to rub it out. It is an accurate record of something." {n}Her mouth tightens.{/n} "I only don't know what to call it yet."''',
       c("Continue", "last_page")),
    mi("blank", '''"There is nobody in here you put there." {n}She checks the open page once more.{/n} "I went through them all. I wanted to be sure before I let you nearer."
"There is no name in your hand. I am glad of it. I shall judge what you do next when you do it."''',
       c("Continue", "last_page")),
    mi("last_page", '''{n}She turns to the back of the book. The last leaf has been ruled like the rest, name and date and place, but the right-hand column has a heading, written in the new, small hand: chose to stand there.{/n}
{n}There is room beneath the heading.{/n}
"The book is for the dead. But a magister should keep her records in one place, so I have given the living a page at the back." {n}She lays the pen beside it, parallel to the edge of the paper, and does not push it toward you.{/n} "I don't know yet whether it's a record or a superstition. I have left room for a name."''',
       c("[Take the pen and write your name.]", "wrote", flags=(NAMES, NAMED)),
       c('"Not yet. When I write in it, I want to have earned the column."', "later", flags=(NAMES,)),
       c('"That page is yours to fill, not mine."', "hers", flags=(NAMES,))),
    nar("wrote", '''{n}You write it. The pen is good and the paper takes the ink cleanly, and your hand is less steady than hers.{/n}
{n}In the right-hand column you write nothing. The heading says it already.{/n}
{n}Mielarah looks at it for a while without speaking. Then she takes the blotter and presses it down over your name, carefully, as if it could smudge, and lifts it, and closes the book.{/n} "Accurate records," {n}she says, and her voice is not steady at all.{/n}''',
        c("[Leave her with the book.]")),
    mi("later", '''"Earned." {n}She turns the word over like a coin of doubtful mint.{/n} "You walked into my circle on the cobbles, and you want to earn a column." {n}She almost smiles.{/n} "Very well. I shall leave the pen here. Try not to come back while I am counting cargo."''',
       c("[Leave her with the book.]")),
    mi("hers", '''{n}She looks at the empty page, and then at you, and something in her face gives very slightly, like a line easing under a load.{/n}
"Mine." {n}She picks up the pen and holds it and does not write.{/n} "I have spent six years writing other people into the front of this book. It had not occurred to me that I might be allowed to write anyone into the back of it." {n}She closes the book over the pen, to keep the place.{/n} "Go on up, Commander. I want to think about who."''',
       c("[Leave her with the book.]")),

    mi("blank_self", '''"There is no name in here that you put at my elbow. You asked for Oskel. Then you chose to stand there yourself."
{n}She rests her finger beside the column.{/n} "I remember the answer. I shall not pretend you were never asked."''',
       c("Continue", "last_page")),

    mi("blank_withdrawn", '''"You asked to put Oskel at my elbow. We spoke about what that meant, and you took the order back."
{n}She turns back to the newest entry.{/n} "That is not in the column. I remember it all the same."''',
       c("Continue", "last_page")),

], requires=(MARKET,), forbids=(NAMES,), delay=12)


# Round 2 authored situations: variants append to the frozen node/answer inventory.
def _round2_deck():
    for beat in SCENES:
        nodes = {node["Id"]: node for node in beat["Nodes"]}
        stem = beat["Id"].removesuffix(".arcade")
        if stem == D + "nearest":
            nodes["myself"]["Text"] = '"You would have stood there yourself." {n}She puts her cup down and reaches across the chart table. Her fingers stop short of your wrist.{/n} "Then tomorrow you can stand beside the helm while I show you what that means. I shall be flying. You will be keeping your feet."'
        if stem == D + "wheel":
            # The existing emergence still leads to her own kiss, after the weather.
            emerge = next(node for node in beat["Nodes"] if any(c.get("Next") == "above" for c in node["Choices"]))
            emerge["Choices"][0]["Forbids"] += [P + "repeated", D + "wounded_carried"]
            emerge["Choices"].extend([
                c("Continue", "above_repeat", requires=(P + "repeated",)),
                c("Continue", "above_rescue", requires=(D + "wounded_carried",), forbids=(P + "repeated",)),
            ])
            for nid, opening in (
                ("above_repeat", '"The knife in the Bad Luck, and now this. In that weather."'),
                ("above_rescue", '"The block over the streambed, and now another. You stayed nearest both times."'),
            ):
                beat["Nodes"].append(mi(nid, '{n}She looks from the split block to your boot. Her hands are still open.{/n} ' + opening + ' {n}She lays two fingers over your hand on the spokes, correcting the course. She leaves them there.{/n} "I wanted to know whether I could let go without losing my ship. I did. Stay there, Commander. I am captain again; I have decided."', c("[Kiss her.]", "kiss_first"), c('"I am staying."', "kiss_first")))
            nodes["home_after"]["Text"] = '"You kept my ship off the bottom. I can hardly quarrel with that." {n}She brings Starcatcher down toward the city lights. When your sleeve brushes hers, she shifts to the other side of the wheel.{/n} "There is cargo tomorrow. Come if you want to talk about cargo. I am done with weather tonight."'
        if stem == D + "morning":
            nodes["start"]["Choices"][0]["Forbids"] += [P + "repeated", D + "wounded_carried"]
            nodes["start"]["Choices"].extend([
                c("Continue", "block_repeat", requires=(P + "repeated",)),
                c("Continue", "block_rescue", requires=(D + "wounded_carried",), forbids=(P + "repeated",)),
            ])
            for nid, memory in (("block_repeat", '"We watched the knife miss in the Bad Luck. I kept thinking about that."'), ("block_rescue", '"I saw a block miss you while we brought the wounded home. I kept thinking about that."')):
                beat["Nodes"].append(mi(nid, memory + ''' {n}She crouches beside the broken pulley.{/n} "Last night you were asleep. You rolled over and dragged my coat with you, and this struck the place your head had been. No watch, no hand on a spoke. I lay there listening to you breathe."
{n}She looks up, tired and flushed.{/n} "I wanted to wake you. For something rather less scholarly than this. But I wanted to hear you go on breathing more."''', c('[Joke] "I rolled over. That is the whole trick."', "joke"), c('"Come here."', "come")))
        if stem == D + "captains":
            nodes["kerz"]["Text"] = nodes["kerz"]["Text"].replace('I have never been so insulted in my life.', 'Kerz can keep his compliments. I will choose my own crew.')
            nodes["rates"]["Text"] = '''"Your passage? Nothing. The quartermasters still pay for theirs. Cold iron does not become lighter because I like your mouth." {n}She folds the loading list and tucks it into her coat.{/n} "One hour ashore. Then I have a ship to load."
{n}After that hour she walks you back to the mooring, correcting your account of the squall with increasing indignation.{/n} "Port spoke. Your left hand. I was there, Commander." {n}She catches your collar and kisses you hard enough to interrupt your answer, then steps onto the ladder.{/n} "Now let me work. I shall be back before your quartermaster learns to count."'''
        if stem == D + "the_place":
            for nid in ("stand", "joke"):
                nodes[nid]["Text"] = nodes[nid]["Text"].replace('her hand finds your sleeve and stays there', 'her hand finds your waist and draws you against her').replace('finds your sleeve exactly where it expects to', 'finds your waist and draws you against her')

_round2_deck()

# Round 3: the evacuation's departure and return are separate world events.
WOUNDED_JOINED = D + "wounded_joined"
WOUNDED_RESOLVED = D + "wounded_resolved"


def _round3_wounded():
    from storylines import mielarah_trickster as route
    by = {beat["Id"]: beat for beat in SCENES}
    for suffix in ("", ".arcade"):
        departure = by[D + "wounded" + suffix]
        ns = {node["Id"]: node for node in departure["Nodes"]}
        carried = copy.deepcopy(ns["carry"])
        home = copy.deepcopy(ns["home"])
        alone = copy.deepcopy(ns["alone"])
        for nid in ("sum", "sum_refused"):
            answer = ns[nid]["Choices"][0]
            answer["Set"] = []
            ns[nid]["Choices"][1]["Set"] = []
        ns["carry"]["Text"] = (
            "{n}She opens the portal. You take your station half a stride from the wheel while the surgeon and crew secure the forward hold. Three lanterns hang above the bow; she orders them lowered for the first landing.{/n}\n"
            "{n}Starcatcher turns toward the red badlands. Five stretchers per load, and forty men to fetch. The hospital lanterns are still behind you.{/n}")
        ns["carry"]["Choices"][0]["Next"] = "home"
        ns["carry"]["Choices"][0]["Text"] = "[Fly with her.]"
        ns["home"]["Text"] = "{n}The lanterns above the streambed come into view. Mielarah brings the bow around while the crew ready their lines. You stay at her elbow for the first landing.{/n}"
        ns["home"]["Choices"][0]["Text"] = "[Stay at the helm.]"
        ns["home"]["Choices"][0]["Set"] = [WOUNDED, WOUNDED_JOINED]
        ns["alone"]["Text"] = (
            "{n}She goes without you. Starcatcher turns toward the Wound, six stretchers ready in the forward hold. Below her, the hospital staff clear the yard for the first load.{/n}")
        ns["alone"]["Choices"][0]["Set"] = [WOUNDED, WOUNDED_LEFT]
        carried["Id"] = "start"
        home["Choices"][0]["Set"] += [WOUNDED_CARRIED, WOUNDED_RESOLVED]
        alone["Id"] = "start"
        alone["Choices"][0]["Set"].append(WOUNDED_RESOLVED)
        alone["Text"] = alone["Text"].replace(
            "She does not come down from her ship that day, or the next.",
            "She sends word that she will stay aboard today and tomorrow. The crew bring her meals to the wheel.")
        for name, result, required in (
                ("wounded.return", [carried, home], WOUNDED_JOINED),
                ("wounded.return_alone", [alone], WOUNDED_LEFT)):
            SCENES.append(scene(D + name + suffix, "Back from the Wound", "Mielarah", 5, "", result,
                requires=("trickster.ever", WOUNDED, required),
                forbids=(CLOSED, KILLED, WOUNDED_RESOLVED), delay=24, last=5,
                Relationship=REL, Chapters=[5], Remote=True, Kind="event"))

    # Both placements share the same clocks: one day flying, then two aboard if refused.
    # ContactWindows restore presence automatically; there is no extra reconciliation demand.
    windows = [dict(Flag=WOUNDED, MinAgeHours=24),
               dict(Flag=WOUNDED_LEFT, MinAgeHours=72)]
    for presence in route.PRESENCES.values():
        presence.setdefault("ContactWindows", []).extend(copy.deepcopy(windows))


_round3_wounded()

# Round 4 authored callbacks: only an actual crew experiment warrants its recall.
for _beat in SCENES:
    if _beat["Id"].removesuffix(".arcade") == D + "stowaway":
        _nodes = {node["Id"]: node for node in _beat["Nodes"]}
        _nodes["threat"]["Choices"][1]["Forbids"] += [FREED, LAUGHING]
        _nodes["threat"]["Choices"].extend([
            c("\"Let her tidy it. He'll thank you later.\"", "scare_freed", requires=(FREED,)),
            c("\"Let her tidy it. He'll thank you later.\"", "scare_laughing", requires=(LAUGHING,)),
        ])
        for _nid, _policy in (
            ("scare_freed", "I am trying wages without daily correction aboard. I shall hardly begin with your thief."),
            ("scare_laughing", "Your obscene verses kept my crew busy for an evening. Perhaps you can find him a verse about keeping his hands to himself."),
        ):
            _beat["Nodes"].append(mi(_nid,
                '"No. He is not my crew. ' + _policy + '" '
                '{n}She holsters the recovered pistols and turns to Woljif.{/n} '
                '"Master Woljif, I have both my guns. Do not make me check what else you have in your pockets." '
                '{n}He dives through the portal, catches his foot on the step, and swears from the market below.{/n}',
                c("[Watch him go.]", flags=(STOWAWAY,))))
