"""Nurah on the Trickster path: the record made true (Writer/handoffs/trickster/nurah.md; F03, with F24 for her death).

Canon: after the siege she is held in the Drezen capital's cell, "Come to gloat?" (Nurah-Prison/Cue_0001 255504a2), or, if
she was the Trickster's accomplice, "So you've remembered that pawn you put back in the box" (Cue_0002 ea5213ee). The
Commander frees her ("You are free. Go wherever you want.", Answer_0056 -> NuraRanOffAfterDrezen a86ab44f), executes her
("your blow takes her life", Cue_0070 01592bbd) or gives her to Camellia ("Nurah is yours.", Camelia/Answer_0131 ->
NurahKilledByCamellia 739b9fe9, Ch3 only). She was bought as a secretary by Lord Axilar Trezbot, wrote his biography
("Without a Shadow of a Doubt, Expecting Nothing in Return"), and on the Trickster path the epilogue gives her a book
"To the Abyss and Back: The Crusade Through the Eyes of a Former Cultist" (Epilogues/Cue_15 f06a0653).
Ramisa, "a true artist of the slave trade", shows "projections" of her slaves first and delivers "only after they're sold"
(FleshMarket/HologramSlaver Cue_0003 dad3c081, Cue_0013 11789a3f).

Authored, and labelled as authored: a pardon forged so badly that a forger cannot sleep beside it, so she corrects it
herself in the night (the Trickster bets on her pride, not on magic); a larva sold under the Abyss's own law of property
and raised by the crusade's chaplains on the name, hour and place the Commander gives, at the price of her name; a
dedication forged into a whole edition by hand, and kept in the printer's forme by a quartermaster's purse.
She sets her own terms, she can refuse, and ownership is the one thing she never forgives.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
UNIT = "f999fc37ddb225640b7f98c0a05d6948"             # NurahCapital: the capital cell's actor (spawner c2b298fc)
LOCATOR = "7b94948a-1954-428f-82d0-94b2adcb1380"       # the capital locator the parent meeting translocates her to
CELL_A = "01d00f006e0e16543b7507ff38e9fb8a"            # NPC_Common/Nurah-Prison/AnswersList_0003 (after Cue_0001)
CELL_B = "6201570ac1b1d8c4b878f935a7b0160e"            # Nurah-Prison/AnswersList_0004 (after Cue_0002, recruited only)
CELL = [CELL_A, CELL_B]
SHRUG = "c852cfeeaf0fa4744ade8f3e36e01d74"             # Nurah-Prison/Cue_0035 "Nurah shrugs without saying a word." (clean, -> CELL_A)
ASK = "9aab5c83956171d4c8a017dcff3a1554"               # Nurah-Prison/Cue_0055 "If you think of anything else, just ask." (clean, -> CELL_B)
RAMISA = "52cca621c1d850641abdde32373ca592"            # c4/FleshMarket/HologramSlaver/AnswersList_0004
RAMISA_AGAIN = "96301374cccd56d438a5a5069d4821f0"      # HologramSlaver/Cue_0014 "Ah, you again, outsider." (clean)
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"       # NPC_Common/Irabeth/AnswersList_0009
CAMELLIA_HUB = "589d83230bbbfd04bb1220ee4fef1ce1"      # CompanionDialogues/Camelia/AnswersList_0030

PRIMED = "nurah.trickster.primed"
RELEASED = "nurah.trickster.released"
RETURNED = "nurah.trickster.returned"
ACCEPTED = "nurah.trickster.accepted"
PROOFS = "nurah.trickster.proofs_seen"
RUMOUR = "nurah.trickster.larva_rumour"
COMPLETE = "nurah.complete"
CLOSED = "nurah.closed"
RECRUITED = "nurah.trickster_recruited"
RAN_OFF = "nurah.ran_off"
LEDGER = "nurah.trickster.cost.ledger_lie"
GHOST = "nurah.trickster.cost.ghostwritten"
LATE = "nurah.trickster.cost.late"
SIGNED = "nurah.trickster.cost.signed_proofs"
FEE = "nurah.trickster.cost.ramisa_fee"
AUDIENCE = "nurah.trickster.cost.ramisa_audience"
IN_YOUR_NAME = "nurah.trickster.cost.bill_in_your_name"
EVIL = "nurah.trickster.temper_evil"
LATE_COMMITTED = "nurah.trickster.late_committed"
DEATHS = ("nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism")
CAMELLIA_KILL = "nurah.dead_camellia"

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={"nurah.prison": RELEASED, "nurah.dead_drezen": RETURNED, "nurah.dead_camellia": RETURNED,
                          "nurah.killing_mechanism": RETURNED},
    TricksterAccess={
        "prison": dict(detect=["nurah.prison"], device="nurah.trickster.prison.pardon", returned=RELEASED),
        # NuraInPrisonAfterDrezen stops playing once a death etude plays, but the device ignores it anyway.
        "dead": dict(detect=[*DEATHS, "nurah.prison"], device="nurah.trickster.dead.rumour", returned=RETURNED),
        "ran_off": dict(detect=[RAN_OFF], device="nurah.trickster.ran_off.second_draft", returned=ACCEPTED),
    })
PRESENCES = {
    # Ran off: her capital actor lives on, hidden once NuraInPrisonAfterDrezen ends; reuse-native unhides it at the
    # locator the parent private meeting uses. Raised: NurahKilledInDrezen killed that actor, so a copy is spawned there.
    # The parent romance owns the same actor, so both presences stand aside for it.
    "nurah.presence": dict(Unit=UNIT, Area=DREZEN, Mode="reuse-native", At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                           Requires=["trickster.ever", ACCEPTED, RAN_OFF, PROOFS],
                           Forbids=[CLOSED, COMPLETE, RETURNED, "nurah.parent_romance"], MinChapter=5, MaxChapter=5,
                           Dialog="hub", Greeting="{n}A small figure in a pedlar's hood is sitting on the steps with a "
                           "parcel of paper on her knees, reading the Commander's own proclamation on the wall opposite "
                           "and moving her lips at the grammar.{/n}"),
    "nurah.presence.raised": dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                                  Requires=["trickster.ever", RETURNED, PROOFS],
                                  Forbids=[CLOSED, COMPLETE, "nurah.parent_romance"], MinChapter=5, MaxChapter=5,
                                  Dialog="hub", Greeting="{n}The halfling in the chaplains' grey shift is sitting on the "
                                  "steps with a parcel of paper on her knees. She is eating an apple with enormous "
                                  "concentration, the way people do who have recently had no mouth.{/n}"),
}


def nu(id, text, *choices, **kw):
    return n(id, "Nurah", text, *choices, portrait="Nurah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Nurah", **kw)


def ramisa(id, text, *choices, **kw):
    return n(id, "Ramisa", text, *choices, **kw)


def cell(id, title, entry, nodes, requires, forbids, delay, **extra):
    """A beat at her cell: E13 devices on both native Nurah-Prison lists (non-inline: no NativeReturnCue)."""
    SCENES.append(scene(id, title, "Nurah", 3, entry, nodes, requires=requires, forbids=(CLOSED, *forbids), delay=delay,
                        last=5, optional=True, Relationship="nurah", AnswerLists=list(CELL), TricksterDevice=True,
                        TricksterState="prison", **extra))


def letter(id, title, chapter, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Nurah", chapter, "", nodes, requires=requires, forbids=(CLOSED, *forbids),
                        delay=delay, last=chapter, optional=True, Relationship="nurah", Chapters=[chapter], Remote=True,
                        **extra))


# --- The prison branch: the pardon that wasn't forged (F03; every beat at her cell) --------------------------------

PARDON_READ = '''{n}She holds the paper up to the lamp by one corner, as if it might bite.{/n} "Your 'Q' has a tail. Your seal is upside down. This is the worst forgery I have ever seen, and I have seen my own juvenilia."
{n}She squints at the date, and something in her face sharpens.{/n} "...And it's dated tomorrow. Clever. Nobody hangs a woman holding a pardon dated tomorrow. They'd have to wait a day and check."'''


def pardon(id, answer_list, return_cue, lead, requires, forbids):
    SCENES.append(scene(id, "A pardon in the off hand", "Nurah", 3,
        '[Slide a terrible forgery under the bars] "Your pardon, madam. I signed it with my off hand."', [
        nu("start", lead, c("Continue", "read")),
        nu("read", PARDON_READ,
           c("[Leave her the paper.]", flags=(PRIMED, LEDGER, "nurah.started")),
           c('[Take it back.] "On second thought, the seal really is upside down."', abort=True)),
    ], requires=requires, forbids=(CLOSED, *DEATHS, LEDGER, *forbids), last=5, optional=True, Relationship="nurah",
        AnswerLists=[answer_list], NativeReturnCue=return_cue, EntryMythic="PlayerIsTrickster",
        EntryAlignment=dict(Direction="Chaotic", Value=1), TricksterDevice=True, TricksterState="prison"))


pardon("nurah.trickster.prison.pardon", CELL_A, SHRUG,
       '''{n}Nurah takes the paper without getting up from the bunk.{/n} "Come to watch the traitor rot? It's slow work, Commander. You should have brought a chair."''',
       ("trickster", "nurah.prison"), (RECRUITED,))
pardon("nurah.trickster.prison.pardon_recruited", CELL_B, ASK,
       '''{n}Nurah rolls onto one elbow on the bunk and does not smile.{/n} "The pawn remembers the hand that put it back in the box. You came with a candle and that face, so either you've come to execute me or to cheat at cards."
{n}Her eyes go to your sword hand, then to the paper in the other.{/n} "If it's cards, I'm dealing."''',
       ("trickster", "nurah.prison", RECRUITED), ())


def tempers(extra):
    return (
        c('"Because you can still write this war properly."', "end", flags=(*extra, ACCEPTED, "nurah.trickster.temper_good")),
        c('"Because it\'s funnier with you in it."', "end", flags=(*extra, ACCEPTED, "nurah.trickster.temper_chaos")),
        c('"Because you\'d sell them all again, and I\'d like to watch."', "end", alignment=("Evil", 1),
          flags=(*extra, ACCEPTED, EVIL)))


cell("nurah.trickster.prison.night_out", "Professional disgust", '"Sleep well, madam?"', [
    nu("start", '''{n}Nurah is sitting on the bunk exactly where you left her. There is rampart grit on her shoes, and the pardon lies across her knee, face up.{/n} "I didn't sleep. I couldn't, with that thing in the room. Around the second bell I scraped the tail off your 'Q' with a bent nail. Then I lifted your seal with lamp-heat and set it back the right way up. Then I changed the date to today, because a pardon dated tomorrow is an insult to the profession."
{n}She holds up her hands. The ink is under every nail.{/n} "I forged my own pardon, Commander. Out of professional disgust. I suspect that was your whole plan."
{n}She taps the gaol ledger's copy of her sentence, which still says: imprisoned.{/n} "So I went for a walk. The door opens for a pardoned woman, it turns out, and nobody in Drezen looks at a halfling after dark. I read your casualty lists in the archive and came back before the guard changed, because I wanted to ask you one thing to your face.
"You could have just opened the door. I'd have run to the nearest demon with a library. You'd rather keep me. Why?"''',
       *tempers((RELEASED,)),
       c('"Because you\'re mine now. The pardon says so."', "refused", flags=(CLOSED, "nurah.trickster.cost.owned_line"))),
    nu("end", '''"Hm. Good answer. Wrong, but good."
{n}She folds the pardon into quarters and tucks it into her bodice, where a guard would have to be very brave to look for it.{/n} "I'll keep the cell. It's the only room in Drezen where nobody thinks to look for me, and the rent is excellent."''',
       c("[Leave her to it.]")),
    nu("refused", '''{n}She folds the pardon very small.{/n} "Lord Trezbot said that. He had a paper too. It had a better seal."
"Keep your joke, Commander. I'll keep my cell, and you can have me executed any morning you like. I am done being anyone's property." {n}She turns to the wall, and she does not turn back.{/n}''',
       c("[Leave.]")),
], requires=("trickster.ever", LEDGER, "nurah.prison"), forbids=(*DEATHS, RELEASED), delay=24)

PROOFS_CHOICES = (
    c('[Leave the gap] "Your book. You decide what I was."', "trusted", flags=(PROOFS,)),
    c("[Write your own name in the gap.]", "signed", flags=(PROOFS, SIGNED)))
PROOFS_TAIL = [
    nu("trusted", '''{n}She reads the blank twice, then turns the page over as if the name might be hiding on the back.{/n} "Trezbot never once left me a blank. Every line of his book had him in it before I'd picked up the pen. I don't know what to do with one."
"That is a compliment. Don't get used to it."''', c("[Leave her the proofs.]")),
    nu("signed", '''{n}The name sits in the gap as if the page had been cut to fit it.{/n} "Of course. And it will say exactly that, in every copy. You are going to hate how accurate I am."''',
       c("[Leave her the proofs.]")),
]

cell("nurah.trickster.prison.proofs", "Chapter one, from the wrong side", '"What are you writing?"', [
    nu("start", '''{n}The cell has become a scriptorium: candle ends, a plank across two buckets for a desk, and forty pages in a hand so small it looks like stitching.{/n} "The war. From the wrong side, which is the only side worth reading. I've been on both. Proofs of chapter one."
{n}She pushes them through the bars. Halfway down the first page, where your name should be, there is a gap exactly one name wide.{/n} "Fill it in, if you still think paper does what you tell it. Or leave it blank, and let me decide what you were."''',
       *PROOFS_CHOICES),
    *PROOFS_TAIL,
], requires=("trickster.ever", RELEASED, ACCEPTED), forbids=(RETURNED, RAN_OFF, PROOFS), delay=72)

TERMS_TEXT = '''"Terms. Author's terms, which nobody in my life has ever let me set. My name on the cover. Yours nowhere unless I put it there, and I decide how. You don't touch a word, and you don't read it until it's bound."'''
TERMS_CHOICES = (
    c('"Done."', "done", flags=(COMPLETE,)),
    c('"Put my name on the cover too. Next to yours."', "partners", requires=(EVIL,),
      flags=(COMPLETE, "nurah.trickster.cost.coauthor")),
    c('"Put my name on it too. Above yours."', "refused", flags=(CLOSED, "nurah.trickster.cost.name_above")))
DONE = '''"Then we have a book." {n}She says it the way other people say a prayer, quickly, before anyone can take it back.{/n}'''
PARTNERS = '''"Co-authors. Partners in crime, in print, in the same typeface." {n}She grins, all teeth.{/n} "Trezbot would choke on it. Do that again sometime."'''
REFUSED = '''"No." {n}Not angry. Final.{/n}
"Lord Axilar Trezbot's name is on the cover of the best book I ever wrote. His name, his deeds, his glorious story for future generations, in my hand, every word. I did not climb out from under that name to climb under yours. Keep your joke, Commander. There's no book."'''

cell("nurah.trickster.prison.terms", "Author's terms", '"Is it finished?"', [
    nu("start", '''{n}The manuscript is tied up with the string from her bunk. She sits on it, as if it might try to leave.{/n}
''' + TERMS_TEXT,
       c("Continue", "terms_signed", requires=(SIGNED,)), c("Continue", "terms", forbids=(SIGNED,))),
    nu("terms_signed", '''"You signed chapter one, so you're in it. You don't get to be in the title."''', *TERMS_CHOICES),
    nu("terms", '"Take them or leave them. Nobody has ever let me say that to anyone before, so do me the courtesy of pretending to think about it."', *TERMS_CHOICES),
    nu("done", DONE, c("Continue", "threshold")),
    nu("partners", PARTNERS, c("Continue", "threshold")),
    nar("threshold", '''{n}She sets the manuscript on the plank desk and squares its edges with both hands. Then she climbs onto the bunk, so that for once she is the taller of you.{/n}
"Author's terms cover the rest of the evening too. I lead. If you're very good, I'll let you think it was your idea."
{n}Her fingers are black to the second knuckle with ink. She uses them to undo the hooks of your coat one at a time, as carefully as breaking the seal on someone else's letter, and she watches your face the whole while, the way she watches anything she means to describe later. She does not kiss carefully. She bites your lip, laughs into your mouth, and pulls you down onto a straw mattress built for one small prisoner. When the candle gutters, she pinches it out herself.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}The turnkey on the dawn watch finds the cell door ajar, the prisoner asleep, and the Commander's cloak spread over her like a banner over a taken wall. He closes the door very quietly and writes nothing at all in the gaol ledger.{/n}
{n}Nurah does not open her eyes.{/n} "Chapter two. I've changed your name. Nobody will recognise you. Everybody will."''',
        c("[Let her sleep.]")),
    nu("refused", REFUSED, c("[Leave the cell.]")),
], requires=("trickster.ever", RELEASED, PROOFS), forbids=(RETURNED, RAN_OFF, COMPLETE), delay=72)


# --- The dead branch: the bill of sale (F24 secondary; a priced deal with Ramisa, in her own market) -----------------

PRICE = (
    c('[Pay the marilith\'s price] "Five hundred in crusade gold. Hold the lot, and nobody touches her."', "dull",
      crusade=("Finances", -500), flags=(RUMOUR, PRIMED, FEE, "nurah.started")),
    c('[Sell her a story instead] "The last night of this war. Whatever I do in it, you\'ll have the only seat."',
      "classic", mythic="Trickster", flags=(RUMOUR, PRIMED, AUDIENCE, "nurah.started")),
    c('"Not interested."', abort=True))

SCENES.append(scene("nurah.trickster.dead.rumour", "A custom order", "Ramisa", 4,
    '"What\'s in your pens today, madam artist?"', [
    ramisa("start", '''{n}The projection tilts her head, and a second, smaller projection flickers into being beside her: a pale, fat larva with a halfling's face, glaring.{/n} "I show the goods first and deliver after the sale, outsider. You know this one, I think. It used to belong to you."''',
      c("Continue", "sword", forbids=(CAMELLIA_KILL,)), c("Continue", "knife", requires=(CAMELLIA_KILL,))),
    ramisa("sword", '"Before you put it to the sword."', c("Continue", "offer")),
    ramisa("knife", '''"Before you handed it to a woman who wanted to find out what a halfling tastes like." {n}It flinches, she adds, whenever anyone smiles with too many teeth. Ramisa smiles with all of hers.{/n}''',
      c("Continue", "offer")),
    ramisa("offer", '''"It corrects the spelling on its own price tag, and it has opinions about your prose. Someone taught it to write, and nobody has managed to teach it to stop. Petitioners are currency here, but this one I would sell as a curiosity.
"Everyone asks what a thing costs. The right question is what it is worth. Gold is dull, but gold will do. Or you could pay me properly."''', *PRICE),
    ramisa("dull", '"Dull. Accepted. My paperwork will find your camp."', c("Continue")),
    ramisa("classic", '''"A story that hasn't happened yet." {n}The marilith runs her tongue along her lips.{/n} "Futures are the finest stock. They never spoil before delivery. Some would call it cliché. I call it classic. I shall bring the quill myself."''',
      c("Continue")),
], requires=("trickster",), forbids=(CLOSED, RUMOUR, RETURNED), last=4, optional=True, Relationship="nurah",
    Chapters=[4], RequiresAnyGroups=[list(DEATHS)], AnswerLists=[RAMISA], NativeReturnCue=RAMISA_AGAIN,
    TricksterDevice=True, TricksterState="dead"))

CHAPLAINS = '''{n}The rite has a price of its own. The Chaplain-General will not raise a traitor on a marilith's paper alone: the crusade must buy the diamond the rite consumes, and the woman raised will not be Nurah Dendiwhar. The chaplains strike that name from the living before the rite begins, on the Commander's word, and she wakes under no name at all. She may live. She may not be herself again, anywhere the crusade's priests are heard.{/n}'''
PAY_CHAPLAINS = c("[Buy the diamond, and give the word that strikes her name.]", crusade=("Finances", -300),
                  flags=("nurah.trickster.cost.chaplains_writ",))
BILL_FREE = (RETURNED, RELEASED, ACCEPTED, "nurah.trickster.cost.larva_memory", "nurah.trickster.pseudonym")
FORGE = '[Forge the bill of sale] "Owner of record: the author herself. Dead or not, she still owns herself."'

letter("nurah.trickster.dead.bill_of_sale", "Owner of record", 4, [
    nar("start", '''{n}The air over your camp table in the Abyss wrinkles like heat over stone. Ramisa's projection coils into being with a cage and a ledger, the mandragora shrieking at her elbow. The larva in the cage is pale and fat and furious. It has a halfling's face, and it is reading the bill of sale upside down.{/n}''',
        c("Continue", "ledger", requires=(LEDGER,)), c("Continue", "price", forbids=(LEDGER,))),
    nu("ledger", '''"You. You pardoned me, and then they killed me anyway. Do you know what that makes your pardon? A first draft."''',
       c("Continue", "price")),
    ramisa("price", '''"Souls are property here, crusader. Property has an owner, and the owner of record is whoever holds the bill." {n}She slides a blank one across the ledger, and a quill after it.{/n}''',
           c(FORGE, "free", mythic="Trickster", alignment=("Chaotic", 1), requires=(AUDIENCE,)),
           c(FORGE, "surcharge", mythic="Trickster", alignment=("Chaotic", 1), requires=(FEE,), forbids=(AUDIENCE,)),
           c('[Write your own name on the bill] "Owner of record: me."', "owned", alignment=("Evil", 2), flags=(IN_YOUR_NAME,)),
           c('"Keep her."', "stock", flags=(CLOSED, "nurah.trickster.cost.left_in_stock"))),
    ramisa("surcharge", '''{n}She reads the bill twice. She has sold forgeries across the Midnight Isles, and she knows one when it is handed to her.{/n} "A forgery, paid for in gold. Gold is what you give a clerk. You are asking me to put my ledger under a lie, and a lie is art, and art is dearer. The price just went up."''',
           c("[Pay the forger's surcharge.]", "free", crusade=("Finances", -250)),
           c('[Pay her in story instead] "The last night of this war, then. Front row."', "free", flags=(AUDIENCE,)),
           c('"She isn\'t worth it."', "stock", flags=(CLOSED, "nurah.trickster.cost.left_in_stock"))),
    nu("owned", '''"Oh, well done. Out of the Abyss and straight back into service. Lord Trezbot would have loved you."
{n}The larva presses its face to the bars.{/n} "Burn it, or leave me in the cage."''',
       c("[Burn the bill.]", "free"),
       c('"I\'m keeping it."', "stock", flags=(CLOSED,))),
    ramisa("free", '''{n}The marilith's quill writes "the author herself" and then refuses to be put down.{/n} "A slave who owns herself, freed by the hand that killed her."''',
           c("Continue", "rite", forbids=(CAMELLIA_KILL,)), c("Continue", "rite_camellia", requires=(CAMELLIA_KILL,))),
    ramisa("rite_camellia", '"Freed by the hand that gave her away, I should say."', c("Continue", "rite")),
    ramisa("rite", '''{n}She laughs until the mandragora shrieks.{/n} "Your priests will want a name, an hour and a place, or they will raise the wrong halfling. Give them to me, and I shall deliver her where they want her."''',
           c('"Nurah Dendiwhar. The Drezen gaol. The hour I gave the order."', "delivered", forbids=(CAMELLIA_KILL,), flags=BILL_FREE),
           c('"Nurah Dendiwhar. The Drezen gaol, by Camellia\'s hand, on my word."', "delivered", requires=(CAMELLIA_KILL,),
             flags=BILL_FREE)),
    ramisa("delivered", '''"Take her. I've been paid."
{n}The larva looks at you through the bars for the last time as a larva.{/n} "I'm dead on your record," {n}it says.{/n} "Fine. I'll write as somebody else."''',
           c("Continue", "duplicate", requires=(IN_YOUR_NAME,)), c("Continue", "sent", forbids=(IN_YOUR_NAME,))),
    ramisa("duplicate", '''"Every sale has two copies, outsider. I keep the other one. For my collection."''', c("Continue", "sent")),
    nar("sent", '''{n}The projection winks out, and the cage with it. By the next courier from Drezen, the chaplains of the citadel write that a soul has been delivered to their altar with a bill of sale pinned to it, in a hand none of them can read without feeling watched.{/n}
''' + CHAPLAINS,
        PAY_CHAPLAINS),
    ramisa("stock", '''"Then she's stock." {n}The projection winks out. The larva does not.{/n}''', c("[Put the ledger away.]")),
], requires=("trickster.ever", PRIMED, RUMOUR), forbids=(RETURNED,), delay=24, RequiresAnyGroups=[list(DEATHS)],
   TricksterDevice=True, TricksterState="dead")

COURIER_LATE = (PRIMED, RUMOUR, FEE, LATE, "nurah.started")
letter("nurah.trickster.dead.rumour_courier", "Late collection", 5, [
    nar("start", '''{n}One of Ramisa's couriers reaches Drezen with a sealed crate that breathes, and a letter in a beautiful, curling hand:{/n} "One larva, halfling, argumentative. It spells 'Commander' with two m's, and one of them is rude. Late collection carries a price. Ramisa, called Sloughed Skin."''',
        c("Continue", "reserved", requires=(RUMOUR,)), c("Continue", "price", forbids=(RUMOUR,))),
    ramisa("reserved", '"The lot you reserved in my market and never collected. Storage is extra."',
           c("[Pay the storage.]", "bill", crusade=("Finances", -250)), c('"Not interested."', abort=True)),
    ramisa("price", '"Seven hundred and fifty in crusade gold. Stories are for customers who come to my market in person."',
           c("[Pay the late price.]", "bill", crusade=("Finances", -750)), c('"Not interested."', abort=True)),
    nar("bill", "{n}Under the crate's lid: a blank bill of sale, Ramisa's quill, and a chaplain's form pinned to it asking for a name, an hour and a place.{/n}",
        c(FORGE, "freed", mythic="Trickster", alignment=("Chaotic", 1), flags=BILL_FREE + COURIER_LATE),
        c('[Write your own name on the bill] "Owner of record: me."', "owned", alignment=("Evil", 2))),
    nu("owned", '''"Out of the Abyss and straight back into service. Lord Trezbot would have loved you." {n}The voice comes through the slats.{/n} "Burn it, or leave me in the crate."''',
       c("[Burn the bill.]", "freed", flags=BILL_FREE + COURIER_LATE + (IN_YOUR_NAME,)),
       c('"I\'m keeping it."', "stock", flags=(CLOSED, IN_YOUR_NAME) + COURIER_LATE)),
    nar("freed", '''{n}Ramisa's quill writes "the author herself" and refuses to be put down until the chaplain's form is filled in too. The crate goes to the chapel that afternoon.{/n}
''' + CHAPLAINS,
        PAY_CHAPLAINS),
    nu("stock", '"Then I\'m stock." {n}The courier nails the lid back down and takes the crate away.{/n}', c("[Watch it go.]")),
], requires=("trickster",), forbids=(RETURNED,), delay=0, RequiresAnyGroups=[list(DEATHS)],
   TricksterDevice=True, TricksterState="dead")


# --- The ran-off branch: the dedication (F03) ------------------------------------------------------------------------

cell("nurah.trickster.ran_off.dedication", "A dedication in her own hand",
     '[Borrow her manuscript for the night] "Your dedication page is blank. Allow me."', [
    nu("start", '''{n}She hands it over with two fingers, as if it were already on fire.{/n} "If you so much as fold a corner, I will write you into chapter nine as a hunchback with a lisp."''',
       c("Continue", "write")),
    nar("write", '''{n}By candlelight, on the blank page after the title, you write in her own small stitched hand, practising the loops until they are hers: "To the Commander, who kept me because I had stopped being funny. N. D." You leave the manuscript on her bunk before the bell.{/n}''',
        c("[Leave it on her bunk.]", flags=(PRIMED, GHOST, "nurah.started"))),
], requires=("trickster", "nurah.prison"), forbids=(*DEATHS, RAN_OFF, GHOST), delay=0,
    EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1))

letter("nurah.trickster.ran_off.second_draft", "Two hundred copies", 3, [
    nar("start", '''{n}A pedlar bound south stops at the Drezen gate with a crate of fresh pamphlets: "The Pawn Who Left the Board", by N. D. The dedication page is blank.{/n}''',
        c("[Buy the whole run, pay the printer, and write the dedication into every copy.]", "forged", mythic="Trickster",
          crusade=("Finances", -200), flags=(PRIMED, GHOST, LATE, "nurah.started")),
        c('"Let the pedlar go."', abort=True)),
    nar("forged", '''{n}Two hundred copies, one night, one candle. By the fortieth you are forging her hand better than she does: "To the Commander, who kept me because I had stopped being funny. N. D." The pedlar leaves at dawn with the crate and no idea. The printer in the lower city keeps the line locked in his forme for the next edition, and a quartermaster's purse keeps him from remembering who asked.{/n}''',
        c("[Go to bed.]")),
], requires=("trickster", RAN_OFF), forbids=(*DEATHS, GHOST), delay=0, TricksterDevice=True, TricksterState="ran_off")

letter("nurah.trickster.ran_off.terms_by_post", "I am extremely funny", 3, [
    nar("start", '''{n}The envelope is addressed in a hand so furious the nib went through twice.{/n}''',
        c("Continue", "pardoned", requires=(RELEASED,)), c("Continue", "letter", forbids=(RELEASED,))),
    nu("pardoned", '''"You pardoned me, then opened the door, then followed me with THIS. Make up your mind."''', c("Continue", "letter")),
    nu("letter", '''"I did not write that. I checked every copy. I wrote it in every copy, apparently, in my own hand, better than I write it. I burned an edition, and the next one came off the press with the same line, because somebody had paid my printer to keep it locked in the forme. He is a very bad liar. The purse had a crusade quartermaster's knot on it. It is an insult in my own handwriting, Commander, and you paid good money to make it outlive us both.
"And I am funny. I am extremely funny. So why would you even want to keep a woman you think isn't?"''',
       *tempers(()),
       c('"Because I wanted the last word in your book."', "refused", flags=(CLOSED, "nurah.trickster.cost.last_word"))),
    nu("end", '''"Fine. Prove it wrong, then. I'll send you proofs. Don't make me regret the postage."''', c("[Fold the letter away.]")),
    nu("refused", '''"You've had it. It's printed in every copy I will ever make. That is all the room in my life you get. Don't write again."''',
       c("[Fold the letter away.]")),
], requires=("trickster.ever", PRIMED, GHOST, RAN_OFF), forbids=(ACCEPTED,), delay=48, TricksterDevice=True,
   TricksterState="ran_off")


# --- The shared test and commit for the dead and ran-off branches ------------------------------------------------

letter("nurah.trickster.after.proofs", "Chapter one, by post", 5, [
    nar("start", '''{n}A parcel of proofs, forty pages in a hand so small it looks like stitching.{/n}''',
        c("Continue", "raised", requires=(RETURNED,)), c("Continue", "courier", forbids=(RETURNED,))),
    nar("raised", '''{n}They come wrapped in a chaplain's receipt: one resurrection, one halfling, name and hour and place as supplied. Someone has corrected the chaplain's spelling in the margin.{/n}''',
        c("Continue", "proofs")),
    nar("courier", '''{n}They come by a courier in no livery at all, who does not know what he carries and would rather not be told.{/n}''',
        c("Continue", "proofs")),
    nu("proofs", '''"Chapter one. The war from the wrong side, which is the only side worth reading. I've been on both, and one of them had a larva's-eye view.
"There is a gap on the first page exactly one name wide, where you go. Fill it in and send it back, if you still think paper does what you tell it. Or leave it blank, and let me decide what you were."''',
       *PROOFS_CHOICES),
    *PROOFS_TAIL,
], requires=("trickster.ever", ACCEPTED), forbids=(PROOFS,), delay=72, RequiresAnyGroups=[[RETURNED, RAN_OFF]])


def terms_in_person(id, hub, arrival, threshold, morning, requires, forbids):
    SCENES.append(scene(id, "Author's terms", "Nurah", 5, '"You came yourself."', [
        nu("start", arrival + "\n" + TERMS_TEXT,
           c("Continue", "terms_signed", requires=(SIGNED,)), c("Continue", "terms", forbids=(SIGNED,))),
        nu("terms_signed", '''"You signed chapter one, so you're in it. You don't get to be in the title."''', *TERMS_CHOICES),
        nu("terms", '"Take them or leave them. Nobody has ever let me say that to anyone before, so do me the courtesy of pretending to think about it."', *TERMS_CHOICES),
        nu("done", DONE, c("Continue", "threshold")),
        nu("partners", PARTNERS, c("Continue", "threshold")),
        nar("threshold", threshold, c("Continue", "morning")),
        nar("morning", morning, c("[Let her write.]")),
        nu("refused", REFUSED, c("[Let her go.]")),
    ], requires=("trickster.ever", ACCEPTED, PROOFS, *requires), forbids=(CLOSED, COMPLETE, LATE, *forbids), delay=72,
        last=5, optional=True, Relationship="nurah", Chapters=[5], InteractionHub=hub))


terms_in_person("nurah.trickster.terms", "nurah.presence.raised",
    '''{n}She does not get up. She finishes the apple, core and all, and wipes her fingers on the chaplains' shift.{/n} "I've had a mouth again since the chaplains stopped arguing with me about my own name. I'm catching up.
"The chaplains wanted me to stay in the chapel and be grateful. I told them I'd been property of the crusade, property of a marilith, and property of nobody, in that order, and that I preferred the last one. Then I walked out. You had them strike my name from the living, Commander. I woke up as nobody. It's the best disguise I've ever had, and I didn't even have to forge it."
{n}She holds up the parcel: the whole manuscript, tied with chapel string.{/n}''',
    '''{n}She takes you by the hand as if leading a mark to the card table, and she does not let go until your own door is shut behind you both. Then she climbs onto your writing desk, scattering your dispatches, so that she can look down at you.{/n}
"I spent a season as a thing in a cage that could not touch anything. Author's terms: tonight I touch everything."
{n}She means it. Her hands are everywhere at once, quick and ink-stained and greedy, learning you the way she learns a city, by getting lost in it on purpose. The chaplains' shift goes over her head and onto the floor. She is warm, warmer than she has any right to be, and when you lift her off the desk she wraps her legs around you and laughs against your throat as if she has just won a very large bet.{/n}''',
    '''{n}Dawn finds her at your desk in your shirt, which comes to her knees, writing fast with your best pen.{/n} "Chapter nine," she says without looking up. "I'm taking out the hunchback. I'm putting in something much worse. You'll love it."
{n}Two days later the chaplains send the rest of their account: one grey shift, not returned. It has been paid already, in a small, stitched hand, with money you are fairly sure used to be yours, and made out in a name that is not hers.{/n}''',
    (RETURNED,), ())

terms_in_person("nurah.trickster.ran_off.terms", "nurah.presence",
    '''{n}She pushes the hood back just far enough for you to see her grin.{/n} "Came in on a pedlar's cart, under a crate of my own pamphlets. Nobody searches a crate of pamphlets. Nobody reads them either, which is a separate grievance.
"I've come to set terms, and I don't do that by post. Not with you. You forge."
{n}She holds up the parcel: the whole manuscript, with the insulting dedication still on its first page, in her own hand, where it will always be.{/n}''',
    '''{n}She leads you up the back stair to your own rooms as if she had drawn the plans of the citadel herself, which, as its historian, she more or less did. Once the door is shut she drops the hood, then the pedlar's coat, then, with a look that dares you to comment, a great deal more.{/n}
"Author's terms. I spent a year writing about other people's nights. Tonight I'm doing the research."
{n}She climbs onto the bed to be taller than you and kisses you as if she is trying to read what you meant by the dedication off your tongue. Her hands are ink-stained and quick and very sure of themselves. When you pull her down she comes gladly, laughing, and bites your shoulder hard enough to leave a mark she clearly intends to describe.{/n}''',
    '''{n}Dawn finds the bed empty and the window open. On your pillow is a single proof sheet: last night, in a hand so small it looks like stitching, with every name changed and not one detail missing.{/n}
{n}Across the top she has written: "Research. Not for publication. Probably."{/n}''',
    (RAN_OFF,), (RETURNED,))


# --- Epilogue: her own pages (R2-6) --------------------------------------------------------------------------------

EPILOGUE_PARAGRAPHS = (
    p("The book was called 'To the Abyss and Back', and in her case the title was a matter of record. Somewhere in the "
      "Midnight Isles a marilith keeps a bill of sale for the author herself, and has never once been able to collect on it.",
      requires=(RETURNED,)),
    p("The crusade's rolls list Nurah Dendiwhar among the dead of Drezen, struck off on the Commander's word. The author "
      "of 'To the Abyss and Back' put another name on every copy, and the inquisitors who hunted her never once "
      "thought to look for a dead woman.", requires=("nurah.trickster.cost.chaplains_writ",)),
    p("Every copy she ever printed opened with the same dedication, in her own hand: 'To the Commander, who kept me "
      "because I had stopped being funny. N. D.' She never managed to remove it: every printer she went to had already "
      "been paid to keep it. After a while she stopped trying, and began "
      "adding a footnote to it instead, a different one in every edition.", requires=(GHOST,)),
    p("The Drezen gaol kept her cell exactly as she left it, plank desk and all. The turnkeys still tell new recruits that "
      "the prisoner in it forged her own pardon out of professional disgust, and that the Commander had counted on it.",
      requires=(LEDGER, RELEASED), forbids=(RETURNED,)),
    p("The Commander's name appeared once, on the first page, exactly where she had decided it should go.",
      forbids=(SIGNED,)),
    p("The Commander's name appeared once, on the first page, in the Commander's own hand. She never let anyone forget "
      "whose idea that had been.", requires=(SIGNED,)),
    p("Ramisa of the Fleshmarkets was seen, for one night only, in the front row of something. She never said what.",
      requires=(AUDIENCE,)),
)

SCENES.append(scene("nurah.trickster.epilogue.commit", "The author herself", "Epilogue", 5, "", [
    nar("start", '''{n}A book came out of the River Kingdoms the spring after the war: the crusade from the wrong side, told by a halfling who had been a slave, a traitor, a prisoner and, for a season, worse. It was banned in several countries, and a bounty was put on its author's head. The inquisitors never found her. They never thought to look in the Commander's house.{/n}
{n}She had finished the negotiation by herself, on her own terms, with no one's name above hers. The first bound copy reached the Commander wrapped in a sheet of paper with one line on it: "Now you may read it."{/n}''',
        c("[Read it that night, cover to cover.]", "read"),
        c("[Go to her before you have read a word.]", "went")),
    nar("read", '''{n}She arrived at the last page, which is to say at dawn, and found the Commander still reading it. She took the book away, closed it with a snap, and climbed into the Commander's lap to deliver her review of the reader in person. It was a long review, and a thorough one, and she did not trouble to close the door first.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS),
    nar("went", '''{n}She opened her door with the book's twin in her other hand and looked at the Commander's empty hands.{/n} "You haven't read it." {n}She pulled the Commander inside by the sleeve.{/n} "Good. I'll read you the best parts myself. Slowly. With demonstrations."''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMPLETE, CLOSED), last=99, Relationship="nurah"))

SCENES.append(scene("nurah.trickster.epilogue.refused", "No review", "Epilogue", 5, "", [
    nar("start", '''{n}The last chapter never reached Drezen. Nurah Dendiwhar, who had been owned once and meant never to be again, published it under a name nobody could trace, and anyone who asked about the Commander was told that the Commander had wanted a name above hers, and that this was the whole of the review.{/n}''',
        c(), paragraphs=EPILOGUE_PARAGRAPHS)],
    requires=("trickster.ever", PROOFS, CLOSED), forbids=(COMPLETE,), last=99, Relationship="nurah"))


# --- Reactions (ledger 05 section 3.1: exactly Irabeth and Camellia) --------------------------------------------------

IRA = dict(forbids=("irabeth_dead",), ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"})
CAMELLIA_GONE = ("camellia.killed", "camellia.dead", "camellia.kicked_out")

REACTIONS = [
    # Hand-built: two terminal answers.
    scene("nurah.trickster.react.irabeth_night", "Literate rats", "Irabeth", 3, '"Anything to report, Knight-Captain?"', [
        n("start", "Irabeth", '''{n}Irabeth does not look up from the watch report.{/n} "The night watch swears a halfling was in the archive last night, reading the casualty lists by a stolen candle and laughing at the spelling. The cell was locked. I checked it. Twice."
{n}Now she looks up.{/n} "Commander. Is there something about that prisoner I should know before I have to explain it to the Queen?"''',
          c('[Lie] "Rats. Big ones. Literate."', flags=("nurah.trickster.cost.irabeth_lied_to",)),
          c('"Let it go, Beth."', flags=("nurah.trickster.cost.seen",)), portrait="Irabeth")],
        requires=(LEDGER, RELEASED), last=5, Relationship="nurah", AnswerLists=[IRABETH_HUB], Reaction=True, **IRA),
    reaction("Irabeth", "nurah.trickster.react.irabeth_raised", (RETURNED,),
             '''"The chaplains raised a halfling this morning. She corrected their spelling of her own name before she had finished breathing."
{n}Irabeth sets down her quill.{/n} "I signed Nurah Dendiwhar's death report myself, Commander. I'd like to know what I signed, and what you've done to it."''',
             answer_list=IRABETH_HUB, chapter=5, last=5, entry='"About the chapel..."', **IRA),
    reaction("Irabeth", "nurah.trickster.react.irabeth_draft", (GHOST, RAN_OFF),
             '''"The traitor's pamphlet is going round the officers' mess. The dedication is about you, and it isn't kind to her."
{n}Irabeth's mouth twitches, very slightly, and is disciplined back into line.{/n} "I'm told it's selling. I'm told I bought one. I'm told I'm on page six, and I come out of it better than you do."''',
             answer_list=IRABETH_HUB, chapter=3, last=5, entry='"About that pamphlet..."', **IRA),
    reaction("Camellia", "nurah.trickster.react.camellia_pardon", (LEDGER, RELEASED),
             '''{n}Camellia is sharpening something that does not need it.{/n} "You gave the little traitor a pardon. How merciful of you."
{n}The whetstone stops.{/n} "Mireya was so looking forward to tasting a halfling. I told her you were saving it for later. You are saving it for later, aren't you, Commander?"''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, entry='"About Nurah..."'),
    reaction("Camellia", "nurah.trickster.react.camellia_market", (RETURNED, RUMOUR),
             '''"You bought a soul from that marilith in the Fleshmarkets? And I was told the Abyss was a place of monstrous temptation."
{n}Camellia presses her fingertips together, and does not quite hide her smile behind them.{/n} "It is... truly terrible."''',
             answer_list=CAMELLIA_HUB, forbids=(*CAMELLIA_GONE, CAMELLIA_KILL), chapter=4, last=5, entry='"About Nurah..."'),
    reaction("Camellia", "nurah.trickster.react.camellia_supper", (RETURNED, RUMOUR, CAMELLIA_KILL),
             '''"You bought my supper back from a marilith."
{n}Camellia says it very softly, the way she says the names of flowers.{/n} "I did ask you first, Commander. You said she was mine. I suppose a gift can be taken back. It is only that nobody has ever dared take one back from me before. How... truly terrible."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=4, last=5, entry='"About Nurah..."'),
    reaction("Camellia", "nurah.trickster.react.camellia_draft", (GHOST, RAN_OFF),
             '''"Your runaway halfling is selling pamphlets with an insult to herself on the first page, in her own hand."
{n}Camellia turns a page of one; she has a copy.{/n} "I would simply have eaten her. Your way is so much more... literary."''',
             answer_list=CAMELLIA_HUB, forbids=CAMELLIA_GONE, chapter=3, last=5, entry='"About Nurah..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------

def integrate(payload):
    """Save-safe edits: the relationship patch, the two presences and the grief overrides on her registered visits
    (G6: a pardoned or raised Nurah is no longer held back by the flags her return lifted). No id, node or choice of the
    registered route is renamed, removed or reordered."""
    rel = payload["Relationships"]["nurah"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, an imprisoned Nurah may find her pardon better than it looked; a dead "
                        "one may turn up for sale in the Fleshmarkets of Alushinyrra; and one who ran may find you have "
                        "written in her book.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    ours = {s["Id"] for s in SCENES}
    for s in payload["Scenes"]:
        if s.get("Relationship") != "nurah" or s["Id"] in ours:
            continue
        overrides = s.setdefault("ForbidOverrides", {})
        if "nurah.prison" in s["Forbids"]:
            overrides["nurah.prison"] = RELEASED
        for flag in DEATHS:
            if flag in s["Forbids"]:
                overrides[flag] = RETURNED
