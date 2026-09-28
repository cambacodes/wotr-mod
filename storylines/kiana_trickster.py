"""Kiana on the Trickster path: the property that isn't there (Writer/handoffs/trickster/kiana.md, families F14 and F02).

Canon: Darek Sunhammer, "a popular jeweler and an honorable master" (string 6364a8db), put demon-trapped gems in the wedding
jewellery and meant to use the souls "as leverage to coerce people into doing my bidding" (JewelerFinal/Cue_0020 dca9b720).
At the wedding "even the poor dog's" soul went into the cup (ElanIsDesperate/Cue_0006 d852d08d); the victims' bodies lie
in a Drezen hospital "under the patronage of the churches of Iomedae, Torag, and Abadar" (string c96376e6), kept by
Arsinoe and guarded by Houndhearts (string 1a8a489f). Kiana laughs at what frightens her: "The best way to stop being
afraid of something is to laugh at it" (KyanaWelcome/Cue_0014 2b07731a). The Trickster's arcana: "You can reveal item
properties that aren't even there" (TricksterKnowledgeArcanaTier3, string 08c5494d); an officer's complaint is "basically
an invocation" (TricksterRankUp_1/Cue_0007 b1da045d). Authored, and labelled as authored: Sunhammer's apprentice and his
master's price; the whole pouch sold or none; the marriage licence and the postponement; Kiana's unfinished page.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
ARSINOE = "a609ed9b2205d034bb3bb04d2a255681"          # Arsinoe's Drezen actor (her vendor hub's contact)
ARSINOE_HUB = "ecaf5cfe8087a4f45a2269974f4885c9"      # VendorArsinoe/AnswersList_0004: the list tied to the stolen souls
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"       # NPC_Common/Anevia/AnswersList_0003
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"      # NPC_Common/Irabeth/AnswersList_0009
KYANA = "180b0eaa5dce387458d2ebf0ee943985"            # the Q2 unit Kyana
COUNTERFEIT = "3e4ce583dc71401588f33f8192c252cd"      # DarekSunhammersFake, "Counterfeit Darek Sunhammer's Jewelry"

PRIMED = "kiana.trickster.primed"
RETURNED = "kiana.trickster.returned"
MET = "kiana.trickster.met"
ROBBED = "kiana.trickster.cost.guests_robbed"          # the trick freed one soul; the pouch walked out with the rest
MARKED = "kiana.trickster.cost.courier_marked"
FAVOUR = "kiana.trickster.cost.sunhammer_favour"
SPENT = "kiana.trickster.cost.counterfeit_spent"
LETTER_LATE = "kiana.trickster.cost.letter_late"
POSTPONED = "kiana.trickster.cost.betrothed"
RANSOMED = "kiana.trickster.guests_ransomed"          # the pay path bought the whole pouch
DOG = "kiana.trickster.dog_saved"
KING = "kiana.trickster.decree_king"
SIGNED = "kiana.trickster.licence_signed"
DEBT = "kiana.debt_claimed"                            # KIA-02's evil answer at the pivot
KEPT = "kiana.betrothed_kept"
LATE_COMMITTED = "kiana.trickster.late_committed"     # Derived (trickster_world): trickster.ever + met + lovers
H_MARRIED = "kiana.history_married"
H_WIDOW = "kiana.history_widow"
H_BETROTHED = "kiana.history_betrothed"
SOUL_LOST = "kiana.soul_lost"                          # latch: KianaIsPosessed or ElanIsDesperate/Cue_0008
Q3 = "seelah.souls_returned"
HELD = "kiana.counterfeit_held"
BOUGHT = "kiana.trickster.guests_bought_back"         # the revised terms, paid: the rest of the pouch comes home
APOLOGY = "kiana.trickster.cost.apology"
VOW = "kiana.trickster.pouch_vow"                     # the revised terms, refused: the Commander's word to fetch them

RELATIONSHIP_PATCH = dict(
    TricksterAccess={
        "aftermath_missed": dict(detect=[Q3], device="kiana.trickster.aftermath.letter_waited", returned=MET),
        "possessed_no_rescue": dict(detect=[SOUL_LOST], device="kiana.trickster.possessed.fake_gem", returned=RETURNED),
        "awake_no_rescue": dict(detect=["kiana.q2_done"], device="kiana.trickster.awake.dog_collar", returned=RETURNED),
        "wedding_never_happened": dict(detect=["chapter_later"], device="kiana.trickster.no_wedding.postponed",
                                       returned=RETURNED),
    })
PRESENCES = {
    # The spec's reuse-native Kyana: canon keeps her body in the Drezen hospital (ktc_ElanCalls/Cue_0010 3f29d60b). No
    # anchor: if the native unit is not in the capital, nothing is placed and the beat plays on Arsinoe's hub regardless.
    "kiana.presence": dict(Unit=KYANA, Area=DREZEN, Mode="reuse-native",
                           Requires=["trickster.ever", RETURNED], Forbids=["kiana.closed"],
                           MinChapter=5, MaxChapter=5, AnswerLists=[]),
}


def k(id, text, *choices, **kw):
    return n(id, "Kiana", text, *choices, portrait="Kiana", **kw)


def nar(id, text, *choices, portrait="Kiana", **kw):
    return n(id, "Narrator", text, *choices, portrait=portrait, **kw)


def ars(id, text, *choices, **kw):
    return n(id, "Arsinoe", text, *choices, portrait="Arsinoe", **kw)


def letter(id, title, nodes, requires, forbids, delay=0, **extra):
    SCENES.append(scene(id, title, "Kiana", 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship="kiana", Areas=[DREZEN], Chapters=[5], Remote=True, **extra))


# The unfinished page (the relationship's own premise): every Trickster entry ends with the Commander writing the last
# line, which the registered route reads (kiana.moon / kiana.guest) in kiana.last_page.
def page_choices(*flags):
    return (c('[Write: The princess stole the moon and discovered she had nowhere to put it.]',
              flags=(*flags, "kiana.moon", "kiana.started")),
            c('[Write: She locked the doors and asked one guest to stay.]',
              flags=(*flags, "kiana.guest", "kiana.started")))


# --- State aftermath_missed: the letter that waited (mechanical recovery, TT-14) ---------------------------------------

letter("kiana.trickster.aftermath.letter_waited", "The bottom of the box", [
    nar("start", '''{n}Arsinoe's clerk brings it with the morning dispatches, apologising before he has set it down. The hospital's lost-letters box was emptied yesterday for the first time since the siege; this was at the bottom, under a requisition for bandages and a love letter to a Houndheart that nobody has claimed.{/n}
{n}The seal is a smear of candle wax with a thumbprint in it. The date is the day the stolen souls came home.{/n}
"Commander. I owe you a wedding night's worth of thanks and I can't possibly afford it, so you'll have to take a play instead. There is a vampire princess in it. She is very mysterious and very badly housed. I have written all of it except the last line, which is blank, and which I am enclosing, because I would like you to fill it in and I would like you not to be sensible about it. Bring no speeches. K."
{n}The enclosed page is folded small. Its last line is empty.{/n}''',
      c('[Read it again] "She wrote the day she woke."', "married", forbids=("kiana.widowed",)),
      c('[Read it again] "She wrote the day she woke. Before she knew."', "widow", requires=("kiana.widowed",))),
    nar("married", '''{n}Weeks late. A month of her waiting for an answer, and you did not know there was a question. Under the signature, squeezed in after the ink had nearly dried, is a postscript: "PS. Elan says hello. He is pretending not to be embarrassed about the wedding night. He is failing."{/n}
{n}You take up a pen. The blank line waits.{/n}''',
      *page_choices(H_MARRIED, MET, LETTER_LATE)),
    nar("widow", '''{n}She wrote it in the first hour, before anyone had told her. Elan is in it twice. The second time is a postscript: "PS. Elan says hello. He is pretending not to be embarrassed about the wedding night. He is failing."{/n}
{n}By that evening she knew. The letter has been lying in a box ever since, being cheerful at nobody.{/n}
{n}You take up a pen. The blank line waits.{/n}''',
      *page_choices(H_WIDOW, MET, LETTER_LATE)),
], requires=("trickster.ever", Q3), forbids=("kiana.aftermath_seen", RETURNED, MET),
   TricksterDevice=True, TricksterState="aftermath_missed")


# --- State possessed_no_rescue: the fake gem (F14) --------------------------------------------------------------------

TRICK_WAKE = '''{n}She sits up too fast, grabs the edge of the cot, and laughs at herself before anyone else can.{/n}
"So. I was a stone." {n}She looks at Arsinoe, then at you.{/n} "A *flawed* stone, Arsinoe tells me. Bubbles! I was married for about a quarter of an hour, and then I was a stone with a bubble in it."
{n}Her hands are shaking. She looks at them as if they belong to a guest who has had too much wine.{/n}
"The best way to stop being afraid of something is to laugh at it. So I'm going to laugh at this until they stop."
{n}They do not stop. She laughs anyway. Then she looks down the row of cots at the others, still breathing, still empty, and the laugh runs out.{/n}
"...We never even got our wedding night. Damned demons."'''

letter("kiana.trickster.possessed.fake_gem", "Paste", [
    ars("start", '''{n}The hospital for Darek Sunhammer's victims smells of lamp oil, tallow and three kinds of incense. The churches of Iomedae, Torag and Abadar share its roof and have agreed on nothing else. The bodies lie in rows under clean blankets, breathing, empty. Two Houndhearts keep the door.{/n}
{n}At the end of the last row, beside the cot where Kiana lies in what is left of her wedding dress, a young man in a jeweller's leather apron is holding a pale stone up to the lamp, turning it the way his master must have taught him. Arsinoe stands between him and the cot. From the set of her shoulders she has been standing there for some time.{/n}
"Commander. He says this is Kiana." {n}She does not take her eyes off the stone.{/n} "Abadar forgive me, I have checked. He is not lying."''',
      c("Continue", "terms")),
    nar("terms", '''{n}The apprentice bows to you exactly as low as a shopkeeper bows to a customer who has not yet paid.{/n}
"Master Sunhammer sends his compliments, Commander, and his terms. A craftsman honours every commission. The bride's stone is the sample; the rest of the wedding party is in here." {n}He touches the pouch at his belt. It is heavy, and it does not chink like coin.{/n} "The lot, for a thousand crowns in crusade gold and one small favour, to be named when it pleases him. He sells them all, or none."
{n}He tilts the stone so the lamplight moves inside it.{/n}
"He asked me to say that he is a patient man. Every soul in this pouch is a door into a house in Mendev, and he has the key to every one. He would hate for yours to be the one door he had to break."''',
      c('[Appraise the soul-gem out loud] "Paste. Cheap paste. I wouldn\'t trade a boot for it."', "appraisal",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Palm the real stone first] "Let me see that. Closer."', "swapped", requires=(HELD,)),
      c('[Pay his master\'s price] "Done. A thousand crowns. Tell him he\'ll get his favour."', "paid",
        crusade=("Finances", -1000)),
      c('[Not yet] "Not yet. Keep him here."', abort=True), portrait="Arsinoe"),
    nar("appraisal", '''{n}You say it the way you would say it to a fence on the Kenabres docks: bored, and a little sorry for him.{/n}
{n}You name its faults as you go, the way a pawnbroker does to bring the price down: a bubble under the table, just off centre; a hairline flaw running from the girdle toward the heart; and last, the one fault that matters, said slowly so the room hears it as a verdict: *this stone holds nothing*. None of it is true. You are not describing the stone. You are pricing it, and the price is the Trickster's to set. It is the finest stone in the room.{/n}
{n}Then the apprentice holds it up to the lamp to prove you wrong, and it is all there. The bubble, exactly where you said. The flaw, fine as a hair. And the last fault, the one you gave it on purpose: it holds nothing. Whatever it was holding has nowhere left to be.{/n}
{n}The apprentice holds it up to the lamp again, and his face changes. Behind you Arsinoe makes a small sound that, in a lesser priestess, would have been a laugh.{/n}''',
      c('[Keep a straight face] "...Paste."',
        check=dict(Skill="CheckBluff", DC=20, Success="sold", Failure="bolted", CommanderOnly=True)), portrait="Arsinoe"),
    nar("sold", '''{n}He believes you. More to the point, he believes his own eyes. He swears at his master's craftsmanship in a guild cant you do not know, drops the ruined stone back into the pouch with the rest, and goes, to take it up with the jeweller in person. The other stones go with him. You let them.{/n}
{n}Glass holds nothing. Whatever was in that stone is not in the pouch any more. The lamp by the cot flickers once and steadies, and Kiana draws in a breath like someone coming up from deep water.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_sold"), portrait="Arsinoe"),
    nar("bolted", '''{n}He looks from the flaw to your face, and sees the grin you did not quite manage to keep off it. He goes white. Then he runs, through the Houndhearts before they can close the door and out into the street, pouch and all, and the other stones with it.{/n}
{n}By tonight, somewhere in Mendev, a dwarf with a jeweller's hands will know exactly whose trick that was.{/n}
{n}On the cot, Kiana draws in a breath like someone coming up from deep water.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_bolted"), portrait="Arsinoe"),
    nar("swapped", '''{n}He hands it over. Of course he does: a craftsman likes his work admired. You turn it to the lamp, and turn it back, and hand him the other one, the counterfeit of Sunhammer's work you have been carrying, cut by some honest forger to pass for his master's. He never feels the difference.{/n}
{n}Then you appraise the stone in your fist out loud, the way you would at any pawnbroker's counter: a bubble just off centre, a hairline flaw from the girdle to the heart, and last, deliberately, *this stone holds nothing*. When you open your hand, every fault you named is there, and the stone is no longer holding anything at all.{/n}
{n}The apprentice squints at the counterfeit between his own fingers. For the first time since he walked in, he looks unsure of his trade.{/n}''',
      c('[Send him back to his master] "Take your stone back to Sunhammer. Tell him the Commander said it was flawed."', "woke_swapped",
        mythic="Trickster", alignment=("Chaotic", 1), remove_item=COUNTERFEIT, requires=(HELD,)),
      portrait="Arsinoe"),
    nar("paid", '''{n}He counts it twice, the whole thousand, coin by coin, with the patience of a man paid by the piece. Then he takes a slip of paper from his apron, writes *One favour, owed* on it in a neat guild hand, and holds it out for your signature.{/n}
{n}You sign it. Arsinoe watches you do it and says nothing, and her silence is worse than the price.{/n}
{n}He empties the pouch onto the blanket, stones in a row, like rings laid out on a jeweller's velvet, and sets the pale one over Kiana's heart. They warm one by one. Down the ward, the sleepers breathe in. A boy sits up and asks, very loudly, where his ring went. Somewhere a dog barks, and somebody laughs, and somebody else starts to cry.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_paid"), portrait="Arsinoe"),
    k("woke_sold", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, H_MARRIED))),
    k("woke_bolted", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, MARKED, H_MARRIED))),
    k("woke_swapped", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, SPENT, H_MARRIED))),
    k("woke_paid", '''{n}She sits up last, and too fast, and grabs the edge of the cot, and looks down the ward at everyone else doing the same.{/n}
"You paid him." {n}It isn't a question. She laughs, a little too high.{/n} "The Commander of the crusade bought a whole wedding back from a jeweller. Like a ring out of pawn. I'm going to put that in a play, and nobody is going to believe it."
{n}Then she sees the slip of paper going into the apprentice's apron, with your name on it, and she stops laughing.{/n}
"What did you promise him?"''',
      c('[Tell her it is your debt, not hers.]', flags=(RETURNED, FAVOUR, RANSOMED, H_MARRIED))),
], requires=("trickster", "trickster.ever", "chapter_later", SOUL_LOST), forbids=(RETURNED, Q3),
   TricksterDevice=True, TricksterState="possessed_no_rescue")


# --- State awake_no_rescue: the dog's stone (F14) ---------------------------------------------------------------------

letter("kiana.trickster.awake.dog_collar", "The sample", [
    nar("start", '''{n}Kiana is at the hospital, where she has been every day since the wedding: on a stool between two cots, reading aloud to people who cannot hear her. Her friend's dog lies at the foot of one of them, breathing and empty, and does not lift its head when you come in.{/n}
{n}Sunhammer's apprentice is waiting for you by the door, in a jeweller's leather apron, with a pouch at his belt and a small bejewelled collar dangling from one finger.{/n}
"Commander. Master Sunhammer sends his compliments." {n}He holds the collar up so the stone in it catches the lamplight.{/n} "The dog's. A sample, free of charge, so that you know the master's work is genuine. The rest of the wedding party is in the pouch. A thousand crowns in crusade gold for the lot, and one small favour, to be named when it pleases him. He sells them all, or none."
{n}Behind you Kiana has stopped reading. She has heard every word.{/n}''',
      c('[Appraise the dog\'s stone out loud] "Paste. Cheap paste. I wouldn\'t trade a boot for it."', "bark",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Pay for the guests] "All of them. The thousand, and his favour."', "paid", crusade=("Finances", -1000)),
      c('[Not yet] "Not yet."', abort=True)),
    k("bark", '''{n}You name its faults, bored, the way a pawnbroker does: a bubble under the table, a hairline flaw to the heart, and last, flatly, *this stone holds nothing*. None of it was true until you said it. When the apprentice turns the collar to the lamp, all of it is, the last fault too. At the foot of the cot the dog sneezes, sits up, and barks at nothing, furiously, as if it has a great deal to catch up on.{/n}
{n}The apprentice looks at the flaw in the collar, and at the dog, and puts the collar away very carefully, the way you put away something that has bitten you. He does not stay to haggle. The pouch goes with him.{/n}
"You saved the *dog*." {n}Kiana's voice cracks halfway up.{/n} "Of everyone in that cup, you saved the dog."
{n}She laughs until she has to sit down on the floor, and the dog climbs into her lap to help.{/n}
"Oh, gods. Elan is going to be *furious*. I love it. I love it, and there are still..." {n}She looks along the cots, and the laugh stops.{/n}''',
      c('[Let her laugh] "Best appraisal I ever made."', flags=(PRIMED, RETURNED, ROBBED, DOG, H_MARRIED))),
    k("paid", '''{n}He counts it twice. Then he writes *One favour, owed* on a slip of paper in a neat guild hand, and you sign it, and he empties the pouch onto the nearest blanket: stones in a row, like rings laid out on a jeweller's velvet. They warm one by one. Down the ward, the sleepers breathe in. The dog sneezes.{/n}
"Every one of them." {n}Kiana does not laugh. She takes your hand instead and holds it hard enough to hurt.{/n} "You paid for every one of them. Do you know what you've promised him?"''',
      c('[Count the stones with her] "No. I\'ll find out when he asks."', flags=(RETURNED, FAVOUR, RANSOMED, H_MARRIED))),
], requires=("trickster", "trickster.ever", "chapter_later", "kiana.q2_done"), forbids=(RETURNED, Q3, SOUL_LOST),
   TricksterDevice=True, TricksterState="awake_no_rescue")


# --- State wedding_never_happened: the licence postponed (F02) --------------------------------------------------------

letter("kiana.trickster.no_wedding.postponed", "Postponed", [
    nar("desk", '''{n}The clerk brings the week's marriage licences for liberated Drezen and stacks them at your elbow. Somebody has to sign them. In a city at war, it turns out, that somebody is you.{/n}
{n}The third one reads: *Elan, knight of the crusade, and Kiana, of Ustalav. Rite of Abadar. Pledge: one ring, from the Sunhammer shop on the square.*{/n}
{n}The clerk has already stamped two others from the same shop this week. He mentions it as a point in the jeweller's favour.{/n}
{n}The pen is in your hand. So is the stamp.{/n}''',
      c('[Take it to the King: POSTPONED BY ROYAL DECREE] "His Majesty forbids all weddings until the King is sober."',
        "king", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -300),
        requires=("fool_king.crowned",), forbids=("fool_king.gone",)),
      c('[Order it at the war council: POSTPONED] "Standing order: no marriage leave for anyone under arms until the siege lines hold."',
        "order", mythic="Trickster", alignment=("Chaotic", 1), forbids=("fool_king.crowned",)),
      c('[Order it at the war council: POSTPONED] "Standing order: no marriage leave for anyone under arms until the siege lines hold."',
        "order", mythic="Trickster", alignment=("Chaotic", 1), requires=("fool_king.crowned", "fool_king.gone")),
      c('[Sign it] "Approved. Tell them congratulations."', "signed")),
    nar("signed", '''{n}You sign it, and stamp it, and the clerk takes it away with the others. A week later there is a wedding in Drezen: vampire costumes, red wine for blood, a priestess of Abadar so that nobody's god is offended. You are invited. The ring is very fine.{/n}''',
      c('[Send your congratulations.]', flags=(SIGNED, "kiana.closed"))),
    nar("king", '''{n}The Fool King hears you out from his throne, which today is a barrel. He reads the licence upside down, then the right way up, then asks what's in it for him. You tell him: his fee, and the best joke in Drezen. He takes the fee.{/n}
{n}"POSTPONED," he declares, and stamps it himself. "By royal decree! No weddings in my kingdom until the King is sober!" He thinks about it. "That's never, by the way. Put that in. 'Which is never.'"{/n}
{n}The herald reads it out in the square at noon, including the last part. Drezen, which has been at war for a very long time, laughs until it hurts. By evening there are fourteen couples outside the chancery, some still in their good clothes, and nobody laughing among them. A baker and a crossbowman ask you to your face whether the King will ever be sober. You have no answer that isn't the King.{/n}''',
      c("Continue", "complaint_king")),
    nar("order", '''{n}You read it into the minutes of the war council, in front of every officer at the table: *Standing order. No marriage leave for anyone under arms until the siege lines hold.* The quartermaster, who has been losing a sentry a week to wedding nights, nods before you have finished. For weeks the officers have been complaining that they are sick of fighting and doing nothing else; you have answered their prayer the wrong way round, and a few of them laugh, and then stop, because it is an order.{/n}
{n}By evening there are fourteen couples outside the chancery, some still in their good clothes. A baker and a crossbowman ask you to your face how long the lines will take to hold. You have no answer for them that isn't the order.{/n}
{n}The clerk stamps the licence POSTPONED and sands it. The word dries, and stays.{/n}''',
      c("Continue", "complaint_order")),
    k("complaint_king", '''{n}Two days later a letter comes, written so hard that the nib has gone through the paper twice.{/n}
"So I'm not a wife. I am a *fiancée*. Again. Because the KING has banned weddings until he is SOBER. Which, as his herald was kind enough to tell the entire square, is NEVER."
"Elan is furious. The priestess of Abadar has returned our deposit with a note of condolence. I have lost another wedding night to this war, Commander, and I know exactly whose idea it was, because the King told everybody."
{n}The next line has been crossed out and rewritten three times.{/n}
"...I laughed. I didn't want to. Come and explain yourself. Bring no speeches."''',
      c('[Write back] "I heard. Which is never."', flags=(PRIMED, RETURNED, POSTPONED, KING, H_BETROTHED))),
    k("complaint_order", '''{n}Two days later a letter comes, written so hard that the nib has gone through the paper twice.{/n}
"So I'm not a wife. I am a *fiancée*. Again. Because the Commander of the crusade has cancelled marriage leave for everyone under arms until the siege lines hold, in front of the whole war council, and Elan is under arms. Nobody will tell me when the lines will hold. I asked a sergeant. He laughed until he cried, and then he just cried; he was supposed to be married on Sunday."
"Elan wants to challenge you to a duel. I told him to get in line behind the other thirteen grooms. The priestess of Abadar has returned our deposit with a note of condolence."
{n}The next line has been crossed out and rewritten three times.{/n}
"...I laughed. It was only half a joke. Come and explain yourself. Bring no speeches."''',
      c('[Write back] "I heard. Which is never."', flags=(PRIMED, RETURNED, POSTPONED, H_BETROTHED))),
], requires=("trickster", "trickster.ever", "chapter_later"),
   forbids=("kiana.q2_done", "kiana.wedding_seen", SOUL_LOST, RETURNED),
   TricksterDevice=True, TricksterState="wedding_never_happened")


# --- The pivot (KIA-02): in person, on Arsinoe's hub --------------------------------------------------------------------

STONE_PIVOT = (
    ('[Tell her everything] "All of it. Sunhammer, his price, and what I did about it."', "told_robbed",
     dict(requires=(ROBBED,), forbids=(DOG, Q3))),
    ('[Tell her everything] "All of it. Sunhammer, his price, and what I did about it."', "told_dog",
     dict(requires=(DOG,), forbids=(Q3,))),
    ('[Tell her everything] "All of it. Sunhammer, his price, and what I did about it."', "told_ransomed",
     dict(requires=(RANSOMED,), forbids=(Q3,))),
    ('[Tell her everything] "All of it. Sunhammer, his price, and what I did about it."', "told_late",
     dict(requires=(Q3,))),
)


def stone_pivot():
    return nar("pivot", '''{n}She waits. She is, you realise, giving you the cue.{/n}''',
               *(c(text, next, **gate) for text, next, gate in STONE_PIVOT),
               c('[Spare her the details] "You\'re awake. That\'s the part that matters."', "spared"),
               c('[Remind her what it cost] "It cost something. Remember who paid it."', "claimed"))


PAGE = '''{n}She takes a folded page from her sleeve and presses it into your hand. It is the first scene of a play: a vampire princess, a castle, a court dismissed for being insufficiently mysterious. The last line is blank.{/n}
"Give her an ending. Don't be sensible about it. I'll know."'''

SCENES.append(scene("kiana.trickster.after.temple", "Behind the counter", "Kiana", 5, '"I came to ask after Kiana."', [
    ars("start", '''{n}Arsinoe looks up from her ledger, sees who it is, and points her pen at the curtain behind the counter without a word.{/n}''',
        c("Continue", "robbed", requires=(SOUL_LOST, ROBBED), forbids=(Q3,)),
        c("Continue", "ransomed_woke", requires=(SOUL_LOST, RANSOMED), forbids=(Q3,)),
        c("Continue", "dog", requires=(DOG,), forbids=(Q3,)),
        c("Continue", "ransomed_awake", requires=(RANSOMED,), forbids=(SOUL_LOST, Q3)),
        c("Continue", "late", requires=(Q3,)),
        c("Continue", "licence", requires=(H_BETROTHED,))),
    k("robbed", '''{n}Kiana is sitting on the edge of a temple cot in a borrowed robe, with her wedding shoes on because nobody could find her others. She is waking properly this time: colour in her face, and a look in her eye that is going to cost somebody.{/n}
"Arsinoe says only one stone came back from that apprentice. Mine." {n}She turns her wedding ring round and round on her finger.{/n} "Why only me? There's a boy out there who can't find his own ring. There's a dog. Commander, I want to know why only me."''',
      c("Continue", "pivot")),
    k("ransomed_woke", '''{n}Kiana is sitting on the edge of a temple cot in a borrowed robe. Out in the ward, people are complaining about the soup, which Arsinoe says is the surest sign of recovery she knows.{/n}
"They're all awake. Every one. The dog bit a Houndheart this morning; he says it was an honour." {n}She stops smiling.{/n} "And you owe a man who put our souls in a cup. Arsinoe won't tell me what you signed. She says it's between you and your conscience. I told her you might not have one. She said that was what worried her."''',
      c("Continue", "pivot")),
    k("dog", '''{n}Kiana is on the floor of the ward between two cots, with her friend's dog asleep across her feet. He will not let her stand up. She has stopped trying.{/n}
"He sits on me. Every time. I think he's decided I'm his now, since his own mistress is..." {n}She strokes his ears. The collar is gone, and nobody has put another on him.{/n} "I've been reading to them, Commander. All of them, every day. I think now I've been reading to them for the dog."''',
      c("Continue", "pivot")),
    k("ransomed_awake", '''{n}The ward behind the curtain is loud. People who have been empty for months are demanding their shoes, their families and their jewellery back, and then, remembering, not their jewellery. Kiana is going from cot to cot with a jug of water and a list, and the dog is following her.{/n}
"Every one of them, Commander. I keep counting in case one of them is a mistake." {n}She puts the jug down.{/n} "And you owe him. The man who did this. Arsinoe won't say what you signed."''',
      c("Continue", "pivot")),
    k("late", '''{n}Kiana is awake, dressed, and furious with a pile of get-well letters, most of which, she says, are addressed to a corpse and spell her name wrong. Seelah finished what she started: the stones came home, all of them, and the ward behind the curtain is emptying bed by bed.{/n}
"So your trick got to me first, and Seelah got to everyone else." {n}She tosses a letter onto the pile.{/n} "I can't decide whether that makes me lucky or first in the queue. Arsinoe says both."''',
      c("Continue", "pivot")),
    k("licence", '''{n}Kiana is at Arsinoe's back table, surrounded by forms, rebooking a wedding for the second time. From the look on Arsinoe's face she has been at it for an hour. From the look on Kiana's, she has enjoyed about ten minutes of it.{/n}
"The Commander!" {n}She rises with a curtsey that is both perfect and an insult.{/n} "The one who banned weddings. Arsinoe, may I throw something? A small thing. A pen."
{n}"No," says Arsinoe, without looking up.{/n}
"She's no fun." {n}Kiana sits back down, and the laugh goes out of her voice without warning.{/n} "Elan wants to fight you. I told him to wait his turn behind the officers. So. Here you are. Tell me why."''',
      c('[Tell her the truth] "I didn\'t trust the jeweller who made your ring. That\'s all I had."', "told_licence"),
      c('[Make light of it] "It was a joke. It got out of hand."', "spared_licence"),
      c('[Remind her who holds the stamp] "I hold the stamp, Kiana. Remember that."', "claimed_licence")),
    stone_pivot(),
    k("told_robbed", '''{n}She listens to all of it without interrupting, which you suspect is a first. When you get to the part about the bubble and the flaw she puts her hand over her mouth.{/n}
"You called me cheap. To his face. And it *worked*." {n}She lowers the hand. She isn't laughing now.{/n} "And the rest of them walked out of here in his pouch, because you had one joke in you that day and you spent it on me."
{n}She is quiet for a while.{/n}
"I don't know whether to kiss you or hit you. I'm going to do neither until I've written it down. Then I'll know which one the scene wants."''',
      c("Continue", "page")),
    k("told_dog", '''"I heard. I was sitting right there." {n}She scratches the dog behind the ears; he groans with pleasure.{/n} "I wanted to hear you say it anyway, without an audience. You had one joke, and you spent it on a dog, and the rest of them walked out of here in a pouch."
"I'm not angry. I don't think I'm angry. I'm going to write it down until I find out."''',
      c("Continue", "page")),
    k("told_ransomed", '''"A thousand crowns and a favour. To him." {n}She repeats it the way you would repeat the price of a horse you could not believe anyone had paid.{/n} "You know he'll come for it. Men like that always come for it, at the worst moment, in front of everyone. It's how they get an audience."
{n}She takes your hand, turns it over and looks at it, as if she expected to find the ink still on it.{/n}
"Then when he does, I want to be there. Somebody ought to laugh at him."''',
      c("Continue", "page")),
    k("told_late", '''"So you tricked a jeweller's boy, and Seelah did the rest the honest way." {n}She laughs, properly this time.{/n} "Between the two of you I don't know which one to write as the hero. I'll give Seelah the sword and you the good lines. She won't want them anyway."''',
      c("Continue", "page")),
    k("spared", '''{n}She looks at you for a long moment.{/n}
"That's kind." {n}A small, crooked smile.{/n} "It's also a speech, and I said no speeches. I'll let you off, once. It's been a very long month, and I've decided I'm owed a few things going my way."''',
      c("Continue", "page")),
    k("told_licence", '''"A hunch." {n}She stares at you.{/n} "You banned every wedding in a city at war on a *hunch* about a jeweller."
{n}Then, slowly, she looks at her left hand, where the ring from the shop on the square is not.{/n}
"...Elan paid a great deal for that ring. The man in the shop was charming. He asked me all sorts of questions about the guests." {n}She shakes herself.{/n} "No. I am not going to be frightened of a *ring*. I'm going to be furious with you instead. It's much more satisfying, and you can watch."''',
      c("Continue", "page")),
    k("spared_licence", '''"A joke." {n}She considers this.{/n} "A joke that cost me a wedding and made the whole city laugh at me in the square. It was a very good joke. I hate that it was a very good joke."
"If you're going to write my life for me, you can at least learn your lines."''',
      c("Continue", "page")),
    k("page", PAGE, *page_choices(MET)),
    k("claimed", '''{n}Something in her face closes, quietly, like a shutter on a shop at dusk.{/n}
"Oh, I'll remember." {n}She smooths the blanket over her knees.{/n} "I know exactly what I owe you now, Commander. I'll pay it. In coin, a little every week, until it's paid, and then we'll be square, and you can find somebody else to be grateful at you."
"That isn't a joke. You'll know when I'm joking. I'll be laughing."''',
      c('[Let her count out the first coin.]', flags=(MET, DEBT, "kiana.started", "kiana.closed"))),
    k("claimed_licence", '''"You hold the stamp." {n}She says it back to you slowly, trying the words for weight.{/n} "Then hold it. I'll marry Elan in a field outside your walls, where your stamp doesn't reach. And I'll send you an invitation, Commander, so that you can watch."
{n}She gathers her forms, every one, and does not hurry.{/n}''',
      c('[Let her go.]', flags=(MET, DEBT, "kiana.started", "kiana.closed"))),
], requires=("trickster.ever", RETURNED), forbids=(MET,), delay=24, last=5, optional=True, Relationship="kiana",
   Areas=[DREZEN], Chapters=[5], ContactUnit=ARSINOE, AnswerLists=[ARSINOE_HUB]))


# --- The pouch: Sunhammer's revised terms for the guests the joke left behind -------------------------------------------

SCENES.append(scene("kiana.trickster.pouch.second_offer", "Revised terms", "Kiana", 5,
                    '"Sunhammer\'s apprentice is back, I hear."', [
    ars("start", '''{n}He is at Arsinoe's counter, the same young man in the same leather apron, with the same pouch at his belt, lighter by one stone. Arsinoe has not offered him a chair.{/n}
"Commander." {n}He bows exactly as low as before.{/n} "Master Sunhammer received my report of the flaw, and of what his stone was called at the lamp. He was displeased, and when my master is displeased he revises his terms. The rest of the wedding party: a thousand crowns and the favour, as before." {n}He lays a sheet of paper on the counter, already written, with a space at the foot.{/n} "And an apology, in your hand, for the insult to his craft. He intends to frame it."
{n}Behind the curtain somebody has stopped moving. Kiana is standing in the gap in her borrowed robe, listening.{/n}
"Don't you dare," {n}she says.{/n} "Don't you *dare* apologise to him." {n}Then, much more quietly, looking at the pouch:{/n} "...Unless that's what it costs."''',
        c('[Pay, and sign the apology] "A thousand crowns. The favour. And my name under his words."', "paid",
          crusade=("Finances", -1000)),
        c('[Refuse] "Tell your master the Commander doesn\'t buy back flawed stones. I\'ll come for them myself."', "refused"),
        c('[Not today] "Wait outside. I haven\'t decided."', abort=True)),
    k("paid", '''{n}You sign it. The apprentice sands the ink, folds the apology into his apron as carefully as a gem, counts the coin twice, and empties the pouch onto the counter: stones in a row, like rings on a jeweller's velvet. Down the ward, one after another, the sleepers breathe in. A boy asks, very loudly, where his ring went.{/n}
{n}Kiana does not look at the stones. She looks at you.{/n}
"He's going to hang that on a wall." {n}Her voice shakes, and she lets it.{/n} "Somewhere in Mendev there's going to be a wall with your apology on it, and people are going to walk past it and laugh. For us." {n}She takes your hand in both of hers.{/n} "I'm putting it in the play. Word for word. The audience is going to cry, and he'll never know why."''',
      c('[Let her keep your hand.]', flags=(BOUGHT, FAVOUR, APOLOGY))),
    k("refused", '''{n}The apprentice takes the paper back, folds it along its old creases, and goes without another word. The pouch goes with him, and the stones in it.{/n}
{n}Arsinoe opens her ledger and writes in red ink, under the column headed *Sunhammer. Outstanding*, your promise, word for word, and the date.{/n}
"You'll come for them yourself." {n}Kiana says it back to you slowly, trying the words for weight, the way she tries a line.{/n} "Good. Then I'm holding you to it. Every one of them. I'll keep the list." {n}She does not smile.{/n} "And if you don't, Commander, that goes in the play too."''',
      c('[Give her your word.]', flags=(VOW,))),
], requires=("trickster.ever", ROBBED, MET), forbids=(Q3, "kiana.closed"), delay=72, last=5, optional=True,
   Relationship="kiana", Areas=[DREZEN], Chapters=[5], ContactUnit=ARSINOE, AnswerLists=[ARSINOE_HUB]))


# --- The betrothed history: a registered-route beat of its own (absorbs kiana.answer in that world) ---------------------

SCENES.append(scene("kiana.betrothal", "What a fiancée is for", "Kiana", 5, "", [
    k("start", '''{n}Kiana has taken down the cliff and the paper moon. The borrowed castle is a storeroom again, with two chairs in it, and she is sitting in one of them with the postponed licence on her knee.{/n}
"A fiancée can still change her mind. That's the whole point of fiancées. It's the only good thing about them." {n}She smooths the licence flat.{/n} "So tell me, Commander, and don't be charming about it. Did you stamp this to save a war, or to keep me unmarried?"''',
      c('[Tell her to marry him] "Marry him, Kiana. When the war lets you."', "marry"),
      c('[Tell her the truth] "I want you. I also want you to have your wedding. I don\'t know how both work."', "truth")),
    k("marry", '''{n}She looks at you for a long time. Then she folds the licence in half, and in half again, and tucks it into her bodice over her heart, where a soldier keeps a letter from home.{/n}
"All right. When the war lets us." {n}Her smile is real, and a little sad, and entirely for Elan.{/n} "You'll come, won't you? Somebody has to stand at the back and look guilty."''',
      c('[Promise to stand at the back.]', flags=(KEPT, "kiana.closed"))),
    k("truth", '''"You don't know how both work." {n}She laughs, and it catches.{/n} "Nobody does. That's why there are so many plays about it."
{n}She turns the licence over. On the back, in her own hand, there is already a line of writing, crossed out and rewritten.{/n}
"I talked to Elan before I came. I told him I didn't know what I wanted, and he said it was the first honest thing either of us had said since he proposed." {n}She sets the licence on the empty chair.{/n} "We're not getting married. Not now. Maybe not ever. He keeps the ring. I keep the dress, because it was mine first."
"So there's room. I don't know for what yet. Write to me. Slowly."''',
      c('[Write to her. Slowly.]', flags=("kiana.available", "kiana.attracted", "kiana.separated", "kiana.waited"))),
], requires=(H_BETROTHED, "kiana.rehearsed"), forbids=("kiana.available",), delay=72, last=5, optional=False,
   Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN]))


# --- The registered night, on the Trickster path (Directive 12) ---------------------------------------------------------

DATE_NODES = [
    k("threshold", '''{n}She breaks the kiss first, and only far enough to talk.{/n}
"Act three," {n}she says against your mouth.{/n} "The princess dismisses the guards, and the guest forgets every line. Come here and forget them."
{n}She shuts the door with her heel and stage-directs the rest: you, there, by the bed; the candle, here, where it will do her the most good. Then she unlaces the dark dress herself, slowly, one hook at a time, watching your face over her shoulder to see how each one lands and making you wait for the next. When you reach for her she catches both your wrists and kisses you until you forget what you were reaching for.{/n}
{n}The dress goes to the floor in a whisper of borrowed velvet. She steps out of it wearing nothing but the ribbon at her throat, and pushes you down onto the bed with one hand flat on your chest, a princess who has had quite enough of mystery. She climbs over you, knees either side of your hips, lets her hair fall around both your faces, and laughs, low and delighted, at whatever she finds in yours.{/n}
"No speeches," {n}she whispers, and settles astride you, and reaches down between you.{/n}''',
      c("Continue", "morning_after")),
    k("morning_after", '''{n}Morning. She is sitting up in bed with the blanket round her shoulders and ink on her fingers, writing on the back of a playbill, and she does not look up when you wake.{/n}
"It's staying in the play." {n}She crosses something out.{/n} "Heavily edited. There are children in Drezen." {n}Another line.{/n} "You were very good, so you get a bigger part. Don't let it go to your head. The princess still gets the last word."''',
      c('[Spend the morning together.]', flags=("kiana.lovers", "kiana.kissed"))),
]


# --- Epilogues ----------------------------------------------------------------------------------------------------------

PARAGRAPHS = (
    p("Sunhammer's pouch never came back to Drezen. Kiana kept a list of the other names from her wedding, and read it "
      "aloud every year on the anniversary in a temple of Abadar, where debts are remembered.",
      requires=(MET, ROBBED), forbids=(Q3, MARKED, BOUGHT, VOW)),
    p("Sunhammer's pouch never came back to Drezen. Kiana kept a list of the other names from her wedding, and read it "
      "aloud every year on the anniversary in a temple of Abadar. Every year, at the back of the temple, a young man in "
      "a jeweller's apron stood and listened, and left before the end.", requires=(MET, ROBBED, MARKED), forbids=(Q3, BOUGHT, VOW)),
    p("The rest of Kiana's wedding guests came home from Sunhammer's pouch for a thousand crowns and a letter of apology "
      "in the Commander's hand. Somewhere in Mendev it hangs on a wall. Kiana put it in her play, word for word, and "
      "audiences wept at it without knowing why.", requires=(MET, BOUGHT)),
    p("The Commander's promise to fetch the other stones stood in red ink in Arsinoe's ledger for the rest of the war. "
      "Kiana kept the list of names beside it and read it aloud every year on the anniversary, and each year, after the "
      "last name, she looked up.", requires=(MET, VOW), forbids=(Q3,)),
    p("Somewhere in Mendev a dwarf kept a slip of paper with the Commander's signature on it and three words above it: "
      "One favour, owed. Kiana knew. Every so often, at supper, she asked whether he had called it in yet, and watched "
      "the Commander's face while they answered.", requires=(MET, FAVOUR)),
    p("Elan and Kiana stayed friends, which surprised everyone but Elan.", requires=(MET, H_MARRIED),
      forbids=("kiana.widowed",)),
    p("The marriage licence stayed postponed. Kiana had it framed.", requires=(MET, H_BETROTHED)),
    p("The Commander's standing order against marriage leave was lifted the day the Wound closed. Drezen held forty-one "
      "weddings that week, fourteen of them long overdue. Kiana went to every one, cried at all of them, and laughed at most.",
      requires=(POSTPONED,), forbids=(KING,)),
    p("The Fool King's decree against weddings was lifted the day the Wound closed, by royal proclamation, once the King "
      "was sober. He was not. Drezen held forty-one weddings that week anyway, and Kiana went to every one.",
      requires=(POSTPONED, KING)),
)

SCENES.append(scene("kiana.trickster.epilogue.commit", "The last line", "Epilogue", 5, "", [
    nar("start", '''{n}Kiana wrote the last scene of her play after the war, in a room nobody had to lend her. At the end of it the princess asks the guest one question. She gave the Commander the only copy of the script, and the question was underlined twice.{/n}''',
        c('[Write the answer in the margin.]', "margin"),
        c('[Answer it out loud, on the opening night.]', "stage")),
    nar("margin", '''{n}The Commander wrote one word in the margin and handed the script back. Kiana read it, and read it again, and then crossed out the guest's exit and wrote the rest of the scene herself. It ran long. Nobody in the audience complained.{/n}''',
        c(), paragraphs=PARAGRAPHS),
    nar("stage", '''{n}On the opening night, in borrowed costumes, in front of half of Drezen, the princess asked her question, and the Commander stood up in the front row and answered it out loud. The princess forgot to be mysterious. The audience, which had paid for a tragedy, got something better, and asked for its money back anyway so that it could come again.{/n}''',
        c(), paragraphs=PARAGRAPHS),
], requires=("trickster.ever", LATE_COMMITTED), forbids=("kiana.committed", "kiana.closed", "kiana.morning"), last=99,
    Relationship="kiana"))

SCENES.append(scene("kiana.trickster.epilogue.debt", "Paid in full", "Epilogue", 5, "", [
    nar("start", '''{n}Kiana paid the Commander back a crown a week, every week, by courier, for as long as she judged it took. Each coin came wrapped in a page of the play she was writing. The Commander was not in it.{/n}''',
        c()),
], requires=(DEBT,), forbids=(H_BETROTHED,), last=99, Relationship="kiana"))

SCENES.append(scene("kiana.trickster.epilogue.debt_licence", "Outside the walls", "Epilogue", 5, "", [
    nar("start", '''{n}Kiana married Elan the spring after the war, in a field a stone's throw beyond the walls of Drezen, where no Commander's stamp could reach. The Commander was invited, as promised. The invitation was correct in every particular, and the seat it offered was at the very back.{/n}''',
        c()),
], requires=(DEBT, H_BETROTHED), last=99, Relationship="kiana"))

SCENES.append(scene("kiana.trickster.epilogue.betrothed_kept", "When the war let them", "Epilogue", 5, "", [
    nar("start", '''{n}Kiana married Elan the week the Wound closed and the ban on weddings was lifted, the first of forty-one weddings Drezen held that week. The Commander stood at the back and looked guilty, as promised. Kiana cried at her own vows and laughed at them in the same breath, which the priestess of Abadar said she had never seen anyone manage before.{/n}''',
        c()),
], requires=(KEPT,), last=99, Relationship="kiana"))


# --- Reactions (05 section 3.1: Arsinoe, Anevia, Irabeth) ----------------------------------------------------------------

def arsinoe(id, requires, text, forbids=()):
    return reaction("Arsinoe", id, requires, text, answer_list=ARSINOE_HUB, forbids=forbids, chapter=5, last=5,
                    portrait="Arsinoe", entry='"About Kiana..."', Areas=[DREZEN], Chapters=[5])


def anevia(id, requires, text, forbids=()):
    return reaction("Anevia", id, requires, text, answer_list=ANEVIA_HUB, forbids=("anevia_gone", *forbids), chapter=5,
                    last=5, portrait="Anevia", entry='"About Kiana..."', Areas=[DREZEN], Chapters=[5],
                    ForbidOverrides={"anevia_gone": "anevia.trickster.returned"})


REACTIONS = [
    arsinoe("kiana.trickster.aftermath_missed.react_arsinoe", (LETTER_LATE,),
            '''"The hospital's lost-letters box, Commander. I emptied it this week, for the first time since the siege. One of the letters in it was addressed to you, in Kiana's hand, and dated the day she woke."
{n}She closes the ledger on her finger to keep the place.{/n}
"I have reprimanded the orderly. I have also reprimanded myself, which was more unpleasant, because I know exactly where I keep the key."'''),
    anevia("kiana.trickster.aftermath_missed.react_anevia", (LETTER_LATE,),
           '''"Your vampire princess wrote you the day she woke, and the letter sat in a box for a month. You know what that's called, in my old trade? A dead drop nobody checked."
{n}Anevia shakes her head.{/n}
"Check them, Commander. Somebody's always writing to you from the bottom of a box."'''),
    arsinoe("kiana.trickster.possessed.react_arsinoe_stones", (SOUL_LOST, ROBBED),
            '''"A ward of beds, Commander, and one of them empty. I have entered it in the ledger as a recovery."
{n}She turns the ledger round so that you can see the column. It is a long column.{/n}
"Abadar keeps honest books. I will not write the others off as losses while their bodies are warm. But I should like it noted somewhere other than my ledger that the young man who walked out with their souls was allowed to."''',
            forbids=(Q3, BOUGHT)),
    arsinoe("kiana.trickster.possessed.react_arsinoe_ransom", (SOUL_LOST, FAVOUR),
            '''"A thousand crowns and a favour, to the man who put souls in wedding rings."
{n}Arsinoe sets her pen down very precisely.{/n}
"The crowns I can bear. They are a number. The favour is a blank line on a page you signed, and blank lines are how temples go bankrupt, Commander. And crusades."'''),
    reaction("Irabeth", "kiana.trickster.possessed.react_irabeth", (MARKED,),
             '''"A jeweller's boy walked into our hospital with a pouch full of souls, and out again, and nobody stopped him."
{n}Irabeth's jaw sets.{/n}
"Next time you insult a demon collaborator's jewellery, Commander, send for me first. I'd have liked to see his face. Then I'd have liked to see him in irons."''',
             answer_list=IRABETH_HUB, forbids=("irabeth_dead",), chapter=5, last=5, portrait="Irabeth",
             entry='"About Kiana..."', Areas=[DREZEN], Chapters=[5],
             ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"}),
    anevia("kiana.trickster.possessed.react_anevia", (RETURNED, SOUL_LOST, ROBBED),
           '''"You told a jeweller's boy his stone was fake, and it went fake."
{n}Anevia looks at you sidelong, the way she looks at a lock she has not picked yet.{/n}
"I spent twenty years learning to lie to people. You lie to *things*. I can't decide whether to be impressed or to start checking my own rings."'''),
    arsinoe("kiana.trickster.awake.react_arsinoe", (ROBBED, DOG),
            '''"A dog, Commander. I have a ward of sleeping wedding guests, and the one patient who woke up is a dog."
{n}She holds up what is left of a quill.{/n}
"He ate this. I am choosing to regard it as a sign, although I have not yet decided of what."'''),
    anevia("kiana.trickster.awake.react_anevia", (RETURNED, DOG),
           '''"Heard you saved a dog from a cursed collar and let the rest walk out the door."
{n}Anevia shrugs, not quite as lightly as she means to.{/n}
"I've had worse days at work. Not many. You'll want to go and get the rest back, you know. Whatever you told the jeweller's boy."'''),
    arsinoe("kiana.trickster.no_wedding.react_arsinoe", (POSTPONED,),
            '''"Fourteen contracts of marriage, suspended by order. I shall honour the order."
{n}Arsinoe dips her pen.{/n}
"I shall also invoice the crusade for the deposits, to the last copper of the flowers, and for the priestesses' time, and for one wedding cake, which was already baked and has since been eaten by the Houndhearts."'''),
    anevia("kiana.trickster.no_wedding.react_anevia", (POSTPONED,),
           '''"No weddings while the siege lasts?" {n}Anevia whistles.{/n} "Beth and I got in under the wire, then. Don't you dare make it retroactive. And go and look at the queue outside the chancery some evening. Those people had cakes ordered."'''),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------------

ENTRY_ONLY = ("kiana.invitation", "kiana.rehearsal")          # the Q3 entry keeps its own quest prerequisite
COMPANY = ("kiana.stagecraft", "kiana.marriage", "kiana.widow")
MARRIED_ONLY = ("kiana.marriage", "kiana.widow", "kiana.answer")
COMMITTED_ENDINGS = ("kiana.ending_together", "kiana.ending_bereaved", "kiana.ending_ascended", "kiana.ending_promised")
ARSINOE_WEDDING = [
    ars("wedding", '''{n}She turns back one page, to a column headed in red ink: *Sunhammer. Outstanding.*{/n}
"Before we come to the pledge. Your joke about paste brought one soul home from that man's stones. The other wedding guests still lie in my hospital without theirs." {n}She runs a finger down the column. It is not a short column.{/n} "That is not a debt you owe me, Commander. I do not bill for what I cannot price. I mention it so that you remember it, because I will."''',
        c("Continue", "rider", requires=("konomi.trickster.cost.recalled",)),
        c("Continue", "pledge", forbids=("konomi.trickster.cost.recalled",))),
    ars("wedding_dog", '''{n}She turns back one page, to a column headed in red ink: *Sunhammer. Outstanding.*{/n}
"Before we come to the pledge. Your joke about paste brought one soul home from that man's stones. It belonged to a dog. The wedding guests still lie in my hospital without theirs." {n}She runs a finger down the column. It is not a short column.{/n} "That is not a debt you owe me, Commander. I do not bill for what I cannot price. I mention it so that you remember it, because I will."''',
        c("Continue", "rider", requires=("konomi.trickster.cost.recalled",)),
        c("Continue", "pledge", forbids=("konomi.trickster.cost.recalled",))),
]


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Kiana Trickster integration missing scene: " + id)
    return by_id[id]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _gate(choice, forbids=(), requires=()):
    choice["Forbids"] = [*choice["Forbids"], *[f for f in forbids if f not in choice["Forbids"]]]
    choice["Requires"] = [*choice["Requires"], *[r for r in requires if r not in choice["Requires"]]]


def _any_of(scene_, flag, alternative):
    """Replace a hard prerequisite with a one-group alternative (save-safe: gating only)."""
    scene_["Requires"] = [r for r in scene_["Requires"] if r != flag]
    groups = scene_.setdefault("RequiresAnyGroups", [])
    if [flag, alternative] not in groups:
        groups.append([flag, alternative])


def integrate(payload):
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered. New choices are
    appended; the choices they replace on a Trickster run are gated off."""
    rel = payload["Relationships"]["kiana"]
    rel["TricksterAccess"] = {k_: dict(v) for k_, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path in Chapter 5, word of Kiana may reach you from the hospital for "
                        "Sunhammer's victims even without Seelah's soul quest, or from the marriage licences on your "
                        "desk. Afterwards, ask after her at Arsinoe's counter in Drezen.")
    payload.setdefault("Presences", {}).update({k_: dict(v) for k_, v in PRESENCES.items()})
    removable = payload.setdefault("RemovableItems", [])
    if COUNTERFEIT not in removable:
        removable.append(COUNTERFEIT)
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    # KIA-01: the whole registered spine opens on a Trickster entry (kiana.trickster.met) as well as on Q3.
    for s in payload["Scenes"]:
        if s.get("Relationship") == "kiana" and s["Id"] not in ENTRY_ONLY and not s["Id"].startswith("kiana.trickster.") \
                and Q3 in s["Requires"]:
            _any_of(s, Q3, MET)
    for id in COMPANY:
        _any_of(_scene(by_id, id), "kiana.company", MET)
    # No double entry if Q3 completes after a device (the COX seam).
    _scene(by_id, "kiana.invitation")["Forbids"].extend((MET, RETURNED))
    # The betrothed world has its own beat (kiana.betrothal) in place of the married and widowed ones.
    for id in MARRIED_ONLY:
        _scene(by_id, id)["Forbids"].append(H_BETROTHED)
    # KIA-14: Seelah speaks while she is in the party, with no Forbid on her death or departure.
    seelah = _scene(by_id, "kiana.seelah")
    seelah["Forbids"] = [f for f in seelah["Forbids"] if f not in ("seelah_dead", "seelah_gone")]
    seelah["Requires"].append("seelah.in_party")

    # Directive 12, the Trickster variant of the registered night (kiana.date -> kiss).
    date = _scene(by_id, "kiana.date")
    kiss = _node(date, "kiss")
    _gate(kiss["Choices"][0], forbids=("trickster.ever",))
    kiss["Choices"].append(c("Continue", "threshold", requires=("trickster.ever",)))
    date["Nodes"].extend(DATE_NODES)

    # TT-21 letter caps (per relationship <= 8 in Chapter 5): a Trickster entry arrives late in Chapter 5, so the long
    # post-commitment chains (kiana_consequences and everything after it) do not open for it; its committed Kiana ends
    # on kiana.ending_promised, with this route's paragraphs. A Q3 entry keeps the whole registered route.
    _scene(by_id, "kiana.guest_table")["Forbids"].append(MET)

    # R2-6: a Trickster entry whose spine ran out before kiana.morning gets the late-commit page; one that reached
    # kiana.morning and heard her "then don't promise it" (kiana.uncertain) keeps the unfinished ending, as its twin.
    unfinished = _scene(by_id, "kiana.ending_unfinished")
    unfinished["Forbids"].append(MET)
    payload["Scenes"].insert(payload["Scenes"].index(unfinished) + 1, {
        **unfinished, "Id": "kiana.trickster.ending_unfinished", "Requires": [*unfinished["Requires"], MET],
        "Forbids": [*[f for f in unfinished["Forbids"] if f != MET], "kiana.lovers"],
        "ForbidOverrides": {"kiana.lovers": "kiana.morning"},
        "Nodes": [dict(x, Choices=[dict(ch) for ch in x["Choices"]]) for x in unfinished["Nodes"]]})
    for id in COMMITTED_ENDINGS:
        for node in _scene(by_id, id)["Nodes"]:
            node.setdefault("Paragraphs", []).extend(dict(x) for x in PARAGRAPHS)

    # Arsinoe's collection bills the wedding (her deferred backlog node, ledger row 8).
    collection = _scene(by_id, "arsinoe.trickster.cauldron.collection")
    start = _node(collection, "start")
    for choice in start["Choices"][:2]:
        _gate(choice, forbids=(ROBBED,))
    start["Choices"].extend([
        c("Continue", "wedding", requires=(ROBBED, SOUL_LOST), forbids=(Q3, BOUGHT)),
        c("Continue", "wedding_dog", requires=(ROBBED, DOG), forbids=(Q3, BOUGHT)),
        c("Continue", "pledge", requires=(ROBBED, Q3), forbids=("konomi.trickster.cost.recalled",)),
        c("Continue", "rider", requires=(ROBBED, Q3, "konomi.trickster.cost.recalled")),
        c("Continue", "pledge", requires=(ROBBED, BOUGHT), forbids=(Q3, "konomi.trickster.cost.recalled")),
        c("Continue", "rider", requires=(ROBBED, BOUGHT, "konomi.trickster.cost.recalled"), forbids=(Q3,)),
    ])
    collection["Nodes"].extend(dict(x) for x in ARSINOE_WEDDING)
