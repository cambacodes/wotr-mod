"""Kiana on the Trickster path: the property that isn't there (Writer/handoffs/trickster/kiana.md, families F14 and F02).

Canon: Darek Sunhammer, "a popular jeweler and an honorable master" (string 6364a8db), put demon-trapped gems in the wedding
jewellery and meant to use the souls "as leverage to coerce people into doing my bidding" (JewelerFinal/Cue_0020 dca9b720).
At the wedding "even the poor dog's" soul went into the cup (ElanIsDesperate/Cue_0006 d852d08d); the victims' bodies lie
in a Drezen hospital "under the patronage of the churches of Iomedae, Torag, and Abadar" (string c96376e6), kept by
Arsinoe and guarded by Houndhearts (string 1a8a489f). Kiana laughs at what frightens her: "The best way to stop being
afraid of something is to laugh at it" (KyanaWelcome/Cue_0014 2b07731a); an officer's complaint is "basically an
invocation" (TricksterRankUp_1/Cue_0007 b1da045d). Authored, and labelled as authored: Sunhammer's apprentice and his
master's price; the whole pouch sold or none; the marriage licence and the postponement; Kiana's unfinished page.

Polish batch 9 (no mythic-power solutions): the soul-gem is freed by a con and a chisel, not by an appraisal that makes
a crack real. A trapped soul goes free when its gem is broken (the soul-trapping rule of Pathfinder's trap the soul);
Arsinoe audits jewellers for Abadar and carries a cleaving chisel, and every stone has a grain. "Paste" is the insult that
gets the stone into the Commander's hand and the Bluff that sends the apprentice home believing his master's work
failed; with the honest forger's counterfeit (DarekSunhammersFake) the stone is palmed and he never knows. The dog's
sample is broken with a sword pommel in front of Kiana. The chosen TricksterKnowledgeArcanaTier3 only lowers the Bluff
DC ("you know stones better than he does"). No other romance is required: Arsinoe acts as the hospital's keeper.
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
ARCANA = "trickster.arcana_tier3"                   # MainCharacterFacts: TricksterKnowledgeArcanaTier3Feature 5e26c673, the chosen trick
HELD = "kiana.counterfeit_held"
BOUGHT = "kiana.trickster.guests_bought_back"         # the revised terms, paid: the rest of the pouch comes home
APOLOGY = "kiana.trickster.cost.apology"
VOW = "kiana.trickster.pouch_vow"                     # the revised terms, refused: the Commander's word to fetch them
LASTCALL_CALLED = "kiana.lastcall.called"             # Last Call settled Sunhammer's account (lastcall_partners); read only

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
    nar("start", '''{n}Arsinoe's clerk brings it with the morning dispatches, apologising before he has set it down. The hospital's lost-letters box was emptied yesterday, which nobody had done since the siege; this was at the bottom, under a requisition for bandages and a love letter to a Houndheart that nobody has claimed.{/n}
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
"So. I was a stone." {n}She looks at Arsinoe, then at you.{/n} "A *broken* stone, Arsinoe tells me. Split down the middle like a walnut! I was married for about a quarter of an hour, and then I was a stone with a crack in it."
{n}Her hands are shaking. She looks at them as if they belong to a guest who has had too much wine.{/n}
"The best way to stop being afraid of something is to laugh at it. So I'm going to laugh at this until they stop."
{n}They do not stop. She laughs anyway. Then she looks down the row of cots at the others, still breathing, still empty, and the laugh runs out.{/n}
"...We never even got our wedding night. Damned demons."'''

letter("kiana.trickster.possessed.fake_gem", "Paste", [
    ars("start", '''{n}The hospital for Darek Sunhammer's victims smells of lamp oil, tallow and three kinds of incense. The churches of Iomedae, Torag and Abadar share its roof and have agreed on nothing else. The bodies lie in rows under clean blankets, breathing, empty. Two Houndhearts keep the door.{/n}
{n}At the end of the last row, beside the cot where Kiana lies in what is left of her wedding dress, a young man in a jeweller's leather apron is holding a pale stone up to the lamp, turning it the way his master must have taught him. Arsinoe stands between him and the cot. From the set of her shoulders she has been standing there for some time.{/n}
"Commander. He says this is Kiana." {n}She does not take her eyes off the stone.{/n} "Abadar forgive me, I have checked. He is not lying." {n}Her voice drops.{/n} "I audit jewellers for the temple, Commander. I cannot tell you how his stones hold what they hold. I can tell you two things. A soul shut in a stone goes free when the stone breaks, and every body in this ward lies under a ward of Abadar's that I laid myself, so that what comes loose comes home to its own flesh and nowhere else. And every stone has a grain, even his. Strike along it, and the finest diamond in Mendev comes apart in your hand." {n}Her fingers rest on the leather case at her belt, where an auditor of jewellers keeps her loupe and her cleaving chisel.{/n} "He will not let it out of his hand for me. I have asked."''',
      c("Continue", "terms")),
    nar("terms", '''{n}The apprentice bows to you exactly as low as a shopkeeper bows to a customer who has not yet paid.{/n}
"Master Sunhammer sends his compliments, Commander, and his terms. A craftsman honours every commission. The bride's stone is the sample; the rest of the wedding party is in here." {n}He touches the pouch at his belt. It is heavy, and it does not chink like coin.{/n} "The lot, for a thousand crowns in crusade gold and one small favour, to be named when it pleases him. He sells them all, or none."
{n}He tilts the stone so the lamplight moves inside it.{/n}
"He asked me to say that he is a patient man. Every soul in this pouch is a door into a house in Mendev, and he has the key to every one. He would hate for yours to be the one door he had to break."
{n}The two Houndhearts at the door could have him on the floor before he finished the sentence. He knows it. He glances at them, and then at you, with the calm of a man whose master will start knocking on doors at the fourth bell if he is not back on the square to say otherwise.{/n}''',
      c('[Appraise the soul-gem out loud] "Paste. Cheap paste. I wouldn\'t trade a boot for it."', "appraisal",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Palm the real stone first] "Let me see that. Closer."', "swapped", requires=(HELD,)),
      c('[Pay his master\'s price] "Done. A thousand crowns. Tell him he\'ll get his favour."', "paid",
        crusade=("Finances", -1000)),
      c('[Not yet] "Not yet. Keep him here."', abort=True), portrait="Arsinoe"),
    nar("appraisal", '''{n}You say it the way you would say it to a fence on the Kenabres docks: bored, and a little sorry for him. Then you go on, the way a pawnbroker goes on to bring the price down. Glass under the table. Lead in the colour. The kind of stone a sutler sells to a homesick soldier for his girl. His master, you suggest, has been sending the boy out with the shop's seconds.{/n}
{n}It is the finest stone in the room, and he knows it, and you are insulting the only thing he is proud of. His face goes red to the ears. "Paste scratches," he says. "Paste chips. Try it, Commander, if you know a tool from a teaspoon." And he holds it out to you, flat on his palm, the way a craftsman holds out his work to a customer who is about to be made a fool of.{/n}
{n}You take it. You turn it to the lamp as if you meant to scratch it, and Arsinoe, who has understood you a sentence ago, has her case open and her cleaving chisel in your other hand before the apprentice has seen her move. You find the grain the way she told you, a faint line of light along the table. You set the edge on it. You strike it once with the heel of your hand.{/n}
{n}The stone comes apart in two clean halves, and out of the break, slow as oil, runs a pale light that beads on your fingers and falls, not to the floor, but toward the cot. Arsinoe steps sideways, easily, into the apprentice's line of sight, and says under her breath, to you or to her god: "Let it be her."{/n}
{n}The apprentice stares at the two halves on your palm. Now that there is nothing in them they have gone dull and milky all the way through, like the glass a sutler sells to homesick soldiers.{/n}''',
      c('[Keep a straight face] "...Paste."',
        check=dict(Skill="CheckBluff", DC=20, Success="sold", Failure="bolted", CommanderOnly=True), forbids=(ARCANA,)),
      c('[Keep a straight face; you know stones better than he does] "...Paste. Look at the grain."',
        check=dict(Skill="CheckBluff", DC=15, Success="sold", Failure="bolted", CommanderOnly=True), requires=(ARCANA,)),
      portrait="Arsinoe"),
    nar("sold", '''{n}He believes you. More to the point, he believes his own eyes. He swears at his master's craftsmanship in a guild cant you do not know, drops the two halves of the ruined stone back into the pouch with the rest, and goes, to take it up with the jeweller in person. The other stones go with him. You let them.{/n}
{n}The broken stone is empty. Whatever it held is not in the pouch any more. The lamp by the cot flickers once and steadies, and Kiana draws in a breath like someone coming up from deep water.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_sold"), portrait="Arsinoe"),
    nar("bolted", '''{n}He looks from the broken stone to your face, and past Arsinoe's shoulder to the cot, and sees the grin you did not quite manage to keep off it. He goes white. Then he runs, through the Houndhearts before they can close the door and out into the street, pouch and all, and the other stones with it.{/n}
{n}By tonight, somewhere in Mendev, a dwarf with a jeweller's hands will know exactly whose trick that was.{/n}
{n}On the cot, Kiana draws in a breath like someone coming up from deep water.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_bolted"), portrait="Arsinoe"),
    nar("swapped", '''{n}He hands it over. Of course he does: a craftsman likes his work admired. You turn it to the lamp, and turn it back, and hand him the other one, the counterfeit of Sunhammer's work you have been carrying, cut by some honest forger to pass for his master's. He never feels the difference.{/n}
{n}Then you turn away to the cot, as if to compare the stone with the bride, and lean over her with your back to him. Arsinoe has already set her open case on the blanket by the bride's hand, without a word, the way a nurse sets out a tray before the surgeon asks. You take the chisel out of it, find the grain by feel, set the edge on it against the bedframe, and lean your weight on it. The stone parts in your fist with a sound no louder than a knuckle cracking. When you open your hand, the pale light that lived in it has already run out through the break, into the warm air above the cot.{/n}
{n}You tell him, over your shoulder, that there is a bubble in his stone just off centre. The apprentice squints at the counterfeit between his own fingers, and finds one, because the honest forger who cut it was honest about that much. Now, and not before, he looks unsure of his trade.{/n}''',
      c('[Send him back to his master] "Take your stone back to Sunhammer. Tell him the Commander said it was flawed."', "woke_swapped",
        mythic="Trickster", alignment=("Chaotic", 1), remove_item=COUNTERFEIT, requires=(HELD,)),
      portrait="Arsinoe"),
    nar("paid", '''{n}He counts it twice, the whole thousand, coin by coin, with the patience of a man paid by the piece. Then he holds out his right hand, palm up, the way a guild master seals a commission with no price named. "One favour, owed." You lay your palm on his. It is cold, and he does not let go until you look him in the eye.{/n}
{n}Arsinoe watches you do it and says nothing, and her silence is worse than the price.{/n}
{n}He empties the pouch onto the blanket, stones in a row, like rings laid out on a jeweller's velvet, and sets the pale one over Kiana's heart. Arsinoe kneels at the bedside with her cleaving chisel and takes them one at a time, the way a jeweller cuts a row of stones for a necklace: grain, edge, one clean tap. Each stone parts with a sound like a knuckle cracking, and down the ward, one after another, the sleepers breathe in. A boy sits up and asks, very loudly, where his ring went. Somewhere a dog barks, and somebody laughs, and somebody else starts to cry.{/n}''',
      c('[Watch her wake] "Kiana?"', "woke_paid"), portrait="Arsinoe"),
    k("woke_sold", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, H_MARRIED))),
    k("woke_bolted", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, MARKED, H_MARRIED))),
    k("woke_swapped", TRICK_WAKE,
      c('[Sit with her until her hands are still.]', flags=(PRIMED, RETURNED, ROBBED, SPENT, H_MARRIED))),
    k("woke_paid", '''{n}She sits up last, and too fast, and grabs the edge of the cot, and looks down the ward at everyone else doing the same.{/n}
"You paid him." {n}It isn't a question. She laughs, a little too high.{/n} "The Commander of the crusade bought a whole wedding back from a jeweller. Like a ring out of pawn. I'm going to put that in a play, and nobody is going to believe it."
{n}Then she sees your palm flat on the apprentice's, the guild way, and she stops laughing.{/n}
"What did you promise him?"''',
      c('[Tell her it is your debt, not hers.]', flags=(RETURNED, FAVOUR, RANSOMED, H_MARRIED))),
], requires=("trickster", "trickster.ever", "chapter_later", SOUL_LOST), forbids=(RETURNED, Q3),
   TricksterDevice=True, TricksterState="possessed_no_rescue")


# --- State awake_no_rescue: the dog's stone (F14) ---------------------------------------------------------------------

letter("kiana.trickster.awake.dog_collar", "The sample", [
    nar("start", '''{n}Kiana is at the hospital, where she has been every day since the wedding: on a stool between two cots, reading aloud to people who cannot hear her. Her friend's dog lies at the foot of one of them, breathing and empty, and does not lift its head when you come in.{/n}
{n}Sunhammer's apprentice is waiting for you by the door, in a jeweller's leather apron, with a pouch at his belt and a small bejewelled collar dangling from one finger.{/n}
"Commander. Master Sunhammer sends his compliments." {n}He holds the collar up so the stone in it catches the lamplight.{/n} "The dog's. A sample, free of charge, so that you know the master's work is genuine. The rest of the wedding party is in the pouch. A thousand crowns in crusade gold for the lot, and one small favour, to be named when it pleases him. He sells them all, or none."
{n}Behind you Kiana has stopped reading. She has heard every word.{/n}
{n}The Houndhearts at the door could take the pouch off him by force. He knows that too, and tells you, pleasantly, what his master does to the houses behind those doors if his boy is not back on the square by the fourth bell.{/n}''',
      c('[Appraise the dog\'s stone out loud] "Paste. Cheap paste. I wouldn\'t trade a boot for it."', "bark",
        mythic="Trickster", alignment=("Chaotic", 1)),
      c('[Pay for the guests] "All of them. The thousand, and his favour."', "paid", crusade=("Finances", -1000)),
      c('[Not yet] "Not yet."', abort=True)),
    k("bark", '''{n}You say it bored, the way a pawnbroker does: glass under the table, lead in the colour, a sutler's trinket. It is a free sample, and he has just been told in front of a witness that it is worth nothing. He tosses the collar to you, stung, the way a craftsman tosses his work to a doubter. "Keep it, then, Commander. Scratch it and see."{/n}
{n}You do not scratch it. You lay the collar on the flagstones, stone up, draw your sword an inch, and bring the pommel down on it with your whole weight.{/n}
{n}The stone bursts like a hailstone on a roof. A thread of pale light runs out of the powder and along the floor, toward the foot of the cot. At the foot of the cot the dog sneezes, sits up, and barks at nothing, furiously, as if it has a great deal to catch up on.{/n}
{n}The apprentice looks at the powder on the flagstones, and at the dog, and at you, and takes a step back and puts his hand over the pouch, the way you put your hand over something that has nearly been bitten. He does not stay to haggle. The pouch goes with him.{/n}
"You saved the *dog*." {n}Kiana's voice cracks halfway up.{/n} "Of everyone in that cup, you saved the dog."
{n}She laughs until she has to sit down on the floor, and the dog climbs into her lap to help.{/n}
"Oh, gods. Elan is going to be *furious*. I love it. I love it, and there are still..." {n}She looks along the cots, and the laugh stops.{/n}''',
      c('[Let her laugh] "Best appraisal I ever made."', flags=(PRIMED, RETURNED, ROBBED, DOG, H_MARRIED))),
    k("paid", '''{n}He counts it twice. Then he holds out his palm, the guild way, "One favour, owed," and you strike it, and he empties the pouch onto the nearest blanket: stones in a row, like rings laid out on a jeweller's velvet. Arsinoe kneels at the bedside with her cleaving chisel and takes them one at a time, the way a jeweller cuts a row of stones for a necklace: grain, edge, one clean tap. Down the ward, one after another, the sleepers breathe in. The dog sneezes.{/n}
"Every one of them." {n}Kiana does not laugh. She takes your hand instead and holds it hard enough to hurt.{/n} "You paid for every one of them. Do you know what you've promised him?"''',
      c('[Count the stones with her] "No. I\'ll find out when he asks."', flags=(RETURNED, FAVOUR, RANSOMED, H_MARRIED))),
], requires=("trickster", "trickster.ever", "chapter_later", "kiana.q2_done"), forbids=(RETURNED, Q3, SOUL_LOST),
   TricksterDevice=True, TricksterState="awake_no_rescue")


# --- State wedding_never_happened: the licence postponed (F02) --------------------------------------------------------

letter("kiana.trickster.no_wedding.postponed", "Postponed", [
    nar("desk", '''{n}The clerk brings the week's marriage licences for liberated Drezen and stacks them at your elbow. Somebody has to sign them. In a city at war, it turns out, that somebody is you.{/n}
{n}The third one reads: *Elan, knight of the crusade, and Kiana. Rite of Abadar. Pledge: one ring, from the Sunhammer shop on the square.*{/n}
{n}The clerk has already stamped two others from the same shop this week. He mentions it as a point in the jeweller's favour.{/n}
{n}The pen is in your hand. So is the stamp.{/n}''',
      c('[Take it to the King: POSTPONED BY ROYAL DECREE] "His Majesty forbids these three weddings until the King is sober."',
        "king", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -300),
        requires=("fool_king.crowned",), forbids=("fool_king.gone",)),
      c('[Order it at the war council: HELD] "Every licence pledged with a Sunhammer ring is held until his shop has been searched."',
        "order", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -100), forbids=("fool_king.crowned",)),
      c('[Order it at the war council: HELD] "Every licence pledged with a Sunhammer ring is held until his shop has been searched."',
        "order", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -100), requires=("fool_king.crowned", "fool_king.gone")),
      c('[Sign it] "Approved. Tell them congratulations."', "signed")),
    nar("signed", '''{n}You sign it, and stamp it, and the clerk takes it away with the others. A week later there is a wedding in Drezen: vampire costumes, red wine for blood, a priestess of Abadar so that nobody's god is offended. You are invited. The ring is very fine.{/n}''',
      c('[Send your congratulations.]', flags=(SIGNED, "kiana.closed"))),
    nar("king", '''{n}The Fool King hears you out from his throne, which today is a barrel. He reads the three licences upside down, then the right way up, then asks what's in it for him. You tell him: his fee, and the best joke in Drezen. He takes the fee.{/n}
{n}"POSTPONED," he declares, and stamps it himself. "By royal decree! No weddings for these three until the King is sober!" He thinks about it. "That's never, by the way. Put that in. 'Which is never.'"{/n}
{n}The herald reads it out in the square at noon, including the last part. Drezen, which has been at war for a very long time, laughs until it hurts. By evening the other two couples are outside the chancery, still in their good clothes, and neither of them is laughing. A baker and a crossbowman ask you to your face whether the King will ever be sober. You have no answer that isn't the King.{/n}''',
      c("Continue", "complaint_king")),
    nar("order", '''{n}You read it into the minutes of the war council, in front of every officer at the table: *Standing order. Every marriage licence pledged with a ring from the Sunhammer shop is held until the shop and its stock have been searched.* The officers look at one another. Three licences, a jeweller nobody has complained about, and no evidence you are willing to name. The council backs it anyway, because it is the Commander's word and it costs the crusade nothing, and because nobody at that table wants to be the one who argued for a jeweller and was wrong.{/n}
{n}By evening the other two couples are outside the chancery, still in their good clothes. A baker and a crossbowman ask you to your face what their ring has done. You have no answer for them that isn't a hunch.{/n}
{n}The search takes four days and turns the shop on the square inside out. The stock is flawless. The ledger is not: the baker's ring and the crossbowman's are entered, priced and paid for, and the ring pledged on Kiana's licence is not in it at all. The shop's boy says it was a gift from the master, to the bride, with his compliments. Nobody on the council can remember the last time a jeweller gave a bride a stone for nothing.{/n}
{n}The council releases the other two licences and minutes it without comment. The crusade pays both couples' forfeited deposits out of its own purse, and every officer at the table remembers whose word cost it. The third licence stays held until someone can say what the master's compliments were for. The clerk stamps it POSTPONED and sands it.{/n}''',
      c("Continue", "complaint_order")),
    k("complaint_king", '''{n}Two days later a letter comes, written so hard that the nib has gone through the paper twice.{/n}
"So I'm not a wife. I am *betrothed*. Again. Because the KING has banned our wedding until he is SOBER. Which, as his herald was kind enough to tell the entire square, is NEVER."
"Elan is furious. The priestess of Abadar has returned our deposit with a note of condolence. I have lost another wedding night to this war, Commander, and I know exactly whose idea it was, because the King told everybody."
{n}The next line has been crossed out and rewritten three times.{/n}
"...I laughed. I didn't want to. Come and explain yourself. Bring no speeches."''',
      c('[Write back] "I heard. Which is never."', flags=(PRIMED, RETURNED, POSTPONED, KING, H_BETROTHED))),
    k("complaint_order", '''{n}Two days later a letter comes, written so hard that the nib has gone through the paper twice.{/n}
"So I'm not a wife. I am *betrothed*. Again. Because the Commander of the crusade had the war council hold every licence with a Sunhammer ring on it, and the other two got theirs back on Thursday, and ours did not, because our ring is *not in his ledger*. It was a gift. The master gave it to me himself, with compliments. Apparently that is suspicious now. I asked a sergeant what it meant. He looked at my hand for a very long time and would not say."
"Elan wants to challenge you to a duel. I told him the baker and the crossbowman already tried, and got their licences back instead. The priestess of Abadar has returned our deposit with a note of condolence."
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
"They're all awake. Every one. The dog bit a Houndheart this morning; he says it was an honour." {n}She stops smiling.{/n} "And you owe a man who put our souls in a cup. Arsinoe won't tell me what you promised. She says it's between you and your conscience. I told her you might not have one. She said that was what worried her."''',
      c("Continue", "pivot")),
    k("dog", '''{n}Kiana is on the floor of the ward between two cots, with her friend's dog asleep across her feet. He will not let her stand up. She has stopped trying.{/n}
"He sits on me. Every time. I think he's decided I'm his now, since his own mistress is..." {n}She strokes his ears. The collar is gone, and nobody has put another on him.{/n} "I've been reading to them, Commander. All of them, every day. I think now I've been reading to them for the dog."''',
      c("Continue", "pivot")),
    k("ransomed_awake", '''{n}The ward behind the curtain is loud. People who have been empty for months are demanding their shoes, their families and their jewellery back, and then, remembering, not their jewellery. Kiana is going from cot to cot with a jug of water and a list, and the dog is following her.{/n}
"Every one of them, Commander. I keep counting in case one of them is a mistake." {n}She puts the jug down.{/n} "And you owe him. The man who did this. Arsinoe won't say what you promised."''',
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
    k("told_robbed", '''{n}She listens to all of it without interrupting, which you suspect is a first. When you get to the part about the chisel she puts her hand over her mouth.{/n}
"You called me cheap. To his face. And then you broke me in half in front of him, and he *thanked* you." {n}She lowers the hand. She isn't laughing now.{/n} "And the rest of them walked out of here in his pouch, because there was one stone within reach that day and you spent it on me."
{n}She is quiet for a while.{/n}
"I don't know whether to kiss you or hit you. I'm going to do neither until I've written it down. Then I'll know which one the scene wants."''',
      c("Continue", "page")),
    k("told_dog", '''"I heard. I was sitting right there." {n}She scratches the dog behind the ears; he groans with pleasure.{/n} "I wanted to hear you say it anyway, without an audience. You had one stone within reach, and you spent it on a dog, and the rest of them walked out of here in a pouch."
"I'm not angry. I don't think I'm angry. I'm going to write it down until I find out."''',
      c("Continue", "page")),
    k("told_ransomed", '''"A thousand crowns and a favour. To him." {n}She repeats it the way you would repeat the price of a horse you could not believe anyone had paid.{/n} "You know he'll come for it. Men like that always come for it, at the worst moment, in front of everyone. It's how they get an audience."
{n}She takes your hand, turns it over and looks at it, as if she expected to find the ink still on it.{/n}
"Then when he does, I want to be there. Somebody ought to laugh at him."''',
      c("Continue", "page")),
    k("told_late", '''"So you tricked a jeweller's boy, and Seelah did the rest the honest way." {n}She laughs, properly this time.{/n} "Between the two of you I don't know which one to write as the hero. I'll give Seelah the sword and you the good lines. She won't want them anyway."''',
      c("Continue", "page")),
    k("spared", '''{n}She looks at you, and keeps looking.{/n}
"That's kind." {n}A small, crooked smile.{/n} "It's also a speech, and I said no speeches. I'll let you off, once. It's been a very long month, and I've decided I'm owed a few things going my way."''',
      c("Continue", "page")),
    k("told_licence", '''"A hunch." {n}She stares at you.{/n} "You held three weddings in a city at war on a *hunch* about a jeweller."
{n}Then, slowly, she looks at her left hand, where the ring from the shop on the square is not.{/n}
"...Elan paid a great deal for that ring. The man in the shop was charming. He asked me all sorts of questions about the guests." {n}She shakes herself.{/n} "No. I am not going to be frightened of a *ring*. I'm going to be furious with you instead. It's much more satisfying, and you can watch."''',
      c("Continue", "page")),
    k("spared_licence", '''"A joke." {n}She considers this.{/n} "A joke that cost me a wedding and made half of Drezen laugh at me. It was a very good joke. I hate that it was a very good joke."
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


# --- The pouch: Sunhammer's revised terms for the guests the trick left behind ------------------------------------------

SCENES.append(scene("kiana.trickster.pouch.second_offer", "Revised terms", "Kiana", 5,
                    '"Sunhammer\'s apprentice is back, I hear."', [
    ars("start", '''{n}He is at Arsinoe's counter, the same young man in the same leather apron, with the same pouch at his belt, lighter by one stone. Arsinoe has not offered him a chair.{/n}
"Commander." {n}He bows exactly as low as before.{/n} "Master Sunhammer received my report of the stone that split at the lamp, and of what it was called. He was displeased, and when my master is displeased he revises his terms. The rest of the wedding party: a thousand crowns and the favour, as before." {n}He clears his throat.{/n} "And an apology, in your own voice, for the insult to his craft. He has written the words himself. I am to carry them back exactly as you say them, and he intends to have them read out at the guild's feast, every year, for as long as there is a guild."
{n}Behind the curtain somebody has stopped moving. Kiana is standing in the gap in her borrowed robe, listening.{/n}
"Don't you dare," {n}she says.{/n} "Don't you *dare* apologise to him." {n}Then, much more quietly, looking at the pouch:{/n} "...Unless that's what it costs."''',
        c('[Pay, and say the apology] "A thousand crowns. The favour. And his words, in my mouth."', "paid",
          crusade=("Finances", -1000)),
        c('[Refuse] "Tell your master the Commander doesn\'t buy back flawed stones. I\'ll come for them myself."', "refused"),
        c('[Not today] "Wait outside. I haven\'t decided."', abort=True)),
    k("paid", '''{n}You say it, every word he wrote, in front of Arsinoe and the whole ward. The apprentice repeats it back twice to be sure he has it, stores it away behind his eyes as carefully as a gem, counts the coin twice, and empties the pouch onto the counter: stones in a row, like rings on a jeweller's velvet. Arsinoe comes round the counter with her cleaving chisel and takes them one at a time, the way a jeweller cuts a row of stones for a necklace: grain, edge, one clean tap. Down the ward, one after another, the sleepers breathe in. A boy asks, very loudly, where his ring went.{/n}
{n}Kiana does not look at the stones. She looks at you.{/n}
"He's going to have that read out at his feasts." {n}Her voice shakes, and she lets it.{/n} "Somewhere in Mendev, every year, a room full of jewellers is going to drink to your apology and laugh. For us." {n}She takes your hand in both of hers.{/n} "I'm putting it in the play. Word for word. The audience is going to cry, and he'll never know why."''',
      c('[Let her keep your hand.]', flags=(BOUGHT, FAVOUR, APOLOGY))),
    k("refused", '''{n}The apprentice bows, exactly as low as before, and goes without another word. The pouch goes with him, and the stones in it.{/n}
{n}Arsinoe opens her ledger and writes in red ink, under the column headed *Sunhammer. Outstanding*, your promise, word for word, and the date.{/n}
"You'll come for them yourself." {n}Kiana says it back to you slowly, trying the words for weight, the way she tries a line.{/n} "Good. Then I'm holding you to it. Every one of them. I'll keep the list." {n}She does not smile.{/n} "And if you don't, Commander, that goes in the play too."''',
      c('[Give her your word.]', flags=(VOW,))),
], requires=("trickster.ever", ROBBED, MET), forbids=(Q3, "kiana.closed"), delay=72, last=5, optional=True,
   Relationship="kiana", Areas=[DREZEN], Chapters=[5], ContactUnit=ARSINOE, AnswerLists=[ARSINOE_HUB]))


# --- The betrothed history: a registered-route beat of its own (absorbs kiana.answer in that world) ---------------------

SCENES.append(scene("kiana.betrothal", "What betrothal is for", "Kiana", 5, "", [
    k("start", '''{n}Kiana has taken down the cliff and the paper moon. The borrowed castle is a storeroom again, with two chairs in it, and she is sitting in one of them with the postponed licence on her knee.{/n}
"A woman who is only betrothed can still change her mind. That's the whole point of betrothals. It's the only good thing about them." {n}She smooths the licence flat.{/n} "So tell me, Commander, and don't be charming about it. Did you stamp this to save a war, or to keep me unmarried?"''',
      c('[Tell her to marry him] "Marry him, Kiana. When the war lets you."', "marry"),
      c('[Tell her the truth] "I want you. I also want you to have your wedding. I don\'t know how both work."', "truth")),
    k("marry", '''{n}She studies you as if you were a line she cannot decide to cut. Then she folds the licence in half, and in half again, and tucks it into her bodice over her heart, where a soldier keeps a letter from home.{/n}
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
      requires=(MET, ROBBED), forbids=(Q3, MARKED, BOUGHT, VOW, LASTCALL_CALLED)),
    p("Sunhammer's pouch never came back to Drezen. Kiana kept a list of the other names from her wedding, and read it "
      "aloud every year on the anniversary in a temple of Abadar. Every year, at the back of the temple, a young man in "
      "a jeweller's apron stood and listened, and left before the end.", requires=(MET, ROBBED, MARKED),
      forbids=(Q3, BOUGHT, VOW, LASTCALL_CALLED)),
    p("The rest of Kiana's wedding guests came home from Sunhammer's pouch for a thousand crowns and an apology said aloud "
      "in the Commander's own voice. Every year the jewellers' guild of Mendev hears it again at its feast, recited by an "
      "apprentice who has it by heart. Kiana put it in her play, word for word, and audiences wept at it without knowing why.",
      requires=(MET, BOUGHT)),
    p("The Commander's promise to fetch the other stones stood in red ink in Arsinoe's ledger for the rest of the war. "
      "Kiana kept the list of names beside it and read it aloud every year on the anniversary, and each year, after the "
      "last name, she looked up.", requires=(MET, VOW), forbids=(Q3, LASTCALL_CALLED)),
    p("Somewhere in Mendev a jeweller's apprentice remembered the cold of the Commander's palm on his, and his master kept "
      "the three words that went with it in a ledger: One favour, owed. Kiana knew. Every so often, at supper, she asked whether he had called it in yet, and watched "
      "the Commander's face while they answered.", requires=(MET, FAVOUR), forbids=(LASTCALL_CALLED, Q3)),
    p("Darek Sunhammer died with the Commander's favour still owed him, and nobody else ever came to collect it. Kiana "
      "said it was the only debt she had ever seen cancelled by a funeral, and that she approved.", requires=(MET, FAVOUR, Q3),
      forbids=(LASTCALL_CALLED,)),
    p("Elan and Kiana stayed friends, which surprised everyone but Elan.", requires=(MET, H_MARRIED),
      forbids=("kiana.widowed",)),
    p("The marriage licence stayed postponed. Kiana had it framed.", requires=(MET, H_BETROTHED)),
    p("The hold on Kiana's licence was lifted the day the Wound closed, and the gift ring went to Arsinoe's temple, to be "
      "broken on an auditor's bench. The baker and the crossbowman had been married since the spring, and sent the "
      "Commander a slice of each cake, with no note.", requires=(POSTPONED,), forbids=(KING,)),
    p("The Fool King's decree against weddings was lifted the day the Wound closed, by royal proclamation, once the King "
      "was sober. He was not. Three weddings went ahead that week anyway, and Kiana went to every one.",
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
    nar("start", '''{n}Kiana married Elan the week the Wound closed and the hold on the Sunhammer licences was lifted, with a plain silver ring from a smith in the lower town. The Commander stood at the back and looked guilty, as promised. Kiana cried at her own vows and laughed at them in the same breath, which the priestess of Abadar said she had never seen anyone manage before.{/n}''',
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
            '''"The hospital's lost-letters box, Commander. I emptied it this week. Nobody had touched it since the siege. One of the letters in it was addressed to you, in Kiana's hand, and dated the day she woke."
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
"The crowns I can bear. They are a number. The favour is a promise with no price written into it, and unpriced promises are how temples go bankrupt, Commander. And crusades."'''),
    reaction("Irabeth", "kiana.trickster.possessed.react_irabeth", (MARKED,),
             '''"A jeweller's boy walked into our hospital with a pouch full of souls, and out again, and nobody stopped him."
{n}Irabeth's jaw sets.{/n}
"Next time you insult a demon collaborator's jewellery, Commander, send for me first. I'd have liked to see his face. Then I'd have liked to see him in irons."''',
             answer_list=IRABETH_HUB, forbids=("irabeth_dead",), chapter=5, last=5, portrait="Irabeth",
             entry='"About Kiana..."', Areas=[DREZEN], Chapters=[5],
             ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"}),
    anevia("kiana.trickster.possessed.react_anevia", (RETURNED, SOUL_LOST, ROBBED),
           '''"You told a jeweller's boy his stone was paste, broke it in half in front of him, and he went home believing you."
{n}Anevia looks at you sidelong, the way she looks at a lock she has not picked yet.{/n}
"I spent twenty years learning to lie to people. I never once thought of lying to a man while I broke his things in his hand. I can't decide whether to be impressed or to start checking my own rings."''', forbids=(MARKED, SPENT)),
    arsinoe("kiana.trickster.awake.react_arsinoe", (ROBBED, DOG),
            '''"A dog, Commander. I have a ward of sleeping wedding guests, and the one patient who woke up is a dog."
{n}She holds up what is left of a quill.{/n}
"He ate this. I am choosing to regard it as a sign, although I have not yet decided of what."'''),
    anevia("kiana.trickster.awake.react_anevia", (RETURNED, DOG),
           '''"Heard you saved a dog from a cursed collar and let the rest walk out the door."
{n}Anevia shrugs, not quite as lightly as she means to.{/n}
"I've had worse days at work. Not many. You'll want to go and get the rest back, you know. Whatever you told the jeweller's boy."'''),
    arsinoe("kiana.trickster.no_wedding.react_arsinoe", (POSTPONED,),
            '''"Three contracts of marriage, suspended by order. I shall honour the order."
{n}Arsinoe dips her pen.{/n}
"I shall also invoice the crusade for the deposits, to the last copper of the flowers, and for the priestesses' time, and for one wedding cake, which was already baked and has since been eaten by the Houndhearts."'''),
    anevia("kiana.trickster.no_wedding.react_anevia", (POSTPONED,),
           '''"You held three weddings over a jeweller?" {n}Anevia whistles.{/n} "Beth's ring is from a smith in the lower town, thank the gods. Don't you dare go looking at it. And go and talk to those other two couples some evening. They had cakes ordered."'''),
]
SCENES.extend(REACTIONS)


# --- The registered route -----------------------------------------------------------------------------------------------

ENTRY_ONLY = ("kiana.invitation", "kiana.rehearsal")          # the Q3 entry keeps its own quest prerequisite
COMPANY = ("kiana.stagecraft", "kiana.marriage", "kiana.widow")
MARRIED_ONLY = ("kiana.marriage", "kiana.widow", "kiana.answer")
COMMITTED_ENDINGS = ("kiana.ending_together", "kiana.ending_bereaved", "kiana.ending_ascended", "kiana.ending_promised")
ARSINOE_WEDDING = [
    ars("wedding", '''{n}She turns back one page, to a column headed in red ink: *Sunhammer. Outstanding.*{/n}
"Before we come to the pledge. Your paste and my chisel brought one soul home from that man's stones. The other wedding guests still lie in my hospital without theirs." {n}She runs a finger down the column. It is not a short column.{/n} "That is not a debt you owe me, Commander. I do not bill for what I cannot price. I mention it so that you remember it, because I will."''',
        c("Continue", "rider", requires=("konomi.trickster.cost.recalled",)),
        c("Continue", "pledge", forbids=("konomi.trickster.cost.recalled",))),
    ars("wedding_dog", '''{n}She turns back one page, to a column headed in red ink: *Sunhammer. Outstanding.*{/n}
"Before we come to the pledge. Your paste and my chisel brought one soul home from that man's stones. It belonged to a dog. The wedding guests still lie in my hospital without theirs." {n}She runs a finger down the column. It is not a short column.{/n} "That is not a debt you owe me, Commander. I do not bill for what I cannot price. I mention it so that you remember it, because I will."''',
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

    # The registered kiss offer scripts her consent in the Commander's mouth; on the path the offer is made, and she answers.
    attraction = _node(_scene(by_id, "kiana.marriage"), "attraction")
    _gate(attraction["Choices"][1], forbids=("trickster.ever",))
    attraction["Choices"].append(c('[Step close enough to kiss her, and wait.]', "kiss", requires=("trickster.ever",),
                                   forbids=("inhuman",)))

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
