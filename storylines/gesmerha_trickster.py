"""Gesmerha on the Trickster path (Writer/handoffs/trickster/gesmerha.md; F04, the last order / the unfinished work).

Canon: she dies only by her own blade in the Marhevok ambush, when the Commander watches in silence
(MarhevokAmbush/Cue_0008 fca1955f: "You took my eyes, chief, but not my heart... Ancestors, embrace me!"; StartEtude
BlindCarver_Dead 49839ba1), after Marhevok's threat to take her hands (Cue_0004 9cc9b813). Before it she says so herself:
"I already lost my eyes, and I know what he will take next: my hands." (BlindCarver/Cue_0028 13f2b37e). Her oath: "I come
from an ancient line of craftsmen and women and I swear that I have done everything to avoid bringing shame to my
ancestors' memory" (Cue_0017 47d2c4b9). Marhevok cut out her eyes and journeymen finished the statue (Cue_0018 0365c24e);
"we do not 'make' something out of it, we give the wood a new birth" (Cue_0016 f440f602). She knows people by their step
(Cue_0001 1e9af596; PeacefulWoodCarver/Cue_0001 597b7e82). Kyado: "your tricks somehow become the truth" (Cue_0109).

Two states. Dead: the Commander pays for her hands before the ambush (the commission, on her own hub) or at her pyre (the
late fallback, dearer); her line does not take a woodshaper with paid work on the bench, and her ancestors send her back
at a price in their own voice. The ambush itself plays exactly as canon. Missed: a Trickster who never sat at her bench
claims ten afternoons; she hears the lie in the footsteps and makes the Commander play her unfinished game.
Authored and labelled (spec §1): "work on the bench", the carvers' ground and its pyre, the ancestors' old tongue.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
UNIT = "3ba3a0ff8575be8419159221177c1411"          # BlindCarver_Wintersun (no dialog component; the presence copy)
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
WINTERSUN = "0a5654e7dc18f074d9356009d55eb51b"     # WintersunOutdoor
SMITH = "15f754455d1d87c42a4e14df456d5415"         # BlacksmithCapitalTrader (E12b anchor: the carvers' corner of his yard)
HER_LIST = "dc306897f75a31c4aaf9483ebdff0585"      # BlindCarver/AnswersList_0008 (her hub before the ambush)
HER_RETURN = "05d66664080144c4bb8fc08b90cc700b"    # BlindCarver/Cue_0031 "What do you want with blind Gesmerha, stranger?"
HOME_LIST = "2063ee21356b772408f5c9cfb3ed5bd0"     # PeacefulWoodCarver/AnswersList_0005 (Wintersun, alive)
CAPITAL_LIST = "fb3a88e8ed751214c9136f87891ec07b"  # KTC_WintersunHelp/AnswersList_0027 (Drezen, as a guest)
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"      # CompanionDialogues/Lann/AnswersList_0003
ULBRIG_HUB = "0a50c9c878844ed4a69b8d6131304c5e"    # DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"    # CompanionDialogues/Anevia/AnswersList_0003

DEAD = "gesmerha.dead"
LATCH = "gesmerha.dead.latched"
CLOSED = "gesmerha.closed"
COMMITTED = "gesmerha.committed"
STARTED = "gesmerha.started"
P = "gesmerha.trickster."
PRIMED = P + "primed"
COMMISSIONED = P + "commissioned"
RETURNED = P + "returned"
DECLINED = P + "declined"
YARD = P + "yard_seen"
STATUE_TRUE = P + "statue_true"
STATUE_NEW = P + "statue_new"
HELD = P + "held_still"
ADVANCE = P + "cost.advance_paid"
LATE = P + "cost.late"
LAUGHED = P + "cost.laughed_at_grave"
DEBT = P + "cost.ancestor_debt"
FLINCHED = P + "cost.flinched"
HANDS = P + "cost.hands_carved"
CATCHUP = P + "cost.catchup"
FIRSTMET = P + "cost.first_meeting"      # a Commander who never met her before the resolution meets her on screen in Chapter 5
NIGHT_YARD = P + "night_yard"            # a returned night in the smith's yard, recorded on the morning's terminal choice
SLOW = P + "cost.campaign_slow"
LIKENESS = P + "cost.likeness_owed"         # the Commander's face left unfinished on her bench, to be sat for after Threshold
LIKENESS_DONE = P + "cost.likeness_cut"     # cut from memory before Threshold: a grave-post whether the Commander returns or not
WORK_FINISHED = P + "returned.bench"  # existing scene-completion receipt, never romantic acceptance
PRESENCE_FAILED = "gesmerha.presence.failed"

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        "dead": dict(detect=[DEAD], device=P + "dead.unfinished_work", returned=RETURNED),
        "missed": dict(detect=["gesmerha.wintersun_resolved", "!gesmerha.campaign_kept", "!" + DEAD],
                       device=P + "missed.wrong_footsteps_home", returned=None),
    })
PRESENCES = {
    # Her native unit died in the ambush, so reuse-native has nothing to unhide: a copy of it is spawned beside the Drezen
    # smith, whose yard she borrows. The copy has no dialog component; Dialog "hub" makes it talkable. If the smith is
    # absent the anchor fails, gesmerha.presence.failed is raised and the epilogue page carries the commit (no letter twin:
    # the Chapter 5 letter cap).
    "gesmerha.presence": dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", ManageNative=True, At=dict(NearUnit=SMITH, Side="left", Distance=2.5),
                              Requires=["trickster.ever", RETURNED], Forbids=[CLOSED],
                              MinChapter=3, MaxChapter=5, AnswerLists=[], Dialog="hub",
                              Greeting="{n}Gesmerha has taken the corner of the smith's yard farthest from the forge. "
                                       "She tilts her head toward the gate before you reach it.{/n} \"Your step, stranger. "
                                       "Come and stand where I can hear you properly.\""),
}


def g(id, text, *choices, **kw):
    return n(id, "Gesmerha", text, *choices, portrait="Gesmerha", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Gesmerha", **kw)


def in_yard(id, title, entry, nodes, requires, forbids, delay):
    """A scene on the returned Gesmerha's presence in the smith's yard (Chapters 3 and 5; Drezen only)."""
    SCENES.append(scene(id, title, "Gesmerha", 3, entry, nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="gesmerha", Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub="gesmerha.presence"))


# --- State 1, dead in the ambush: the unfinished work (F04) --------------------------------------------------------------

# 4a. The primer, on her own hub before the ambush. The entry is gated on SeenCues gesmerha.feared_hands (Cue_0028) or
# gesmerha.took_risk (Cue_0024): it appears on AnswersList_0008 only once she has said what Marhevok will take next.
# The trick is physical: the Commander drives a coin into the uncut block on her bench, so that "work on the bench" is a
# fact her oath (Cue_0017) cannot step around. Kyado Cue_0109: "your tricks somehow become the truth".
SCENES.append(scene(P + "dead.commission", "Paid in advance", "Gesmerha", 3,
    '[Pay her in advance] "A carving for the Commander, woodshaper. Paid now, in full."', [
    g("start", '''{n}You put a purse in her hand. Her fingers stop on it, then turn it over twice, weighing it the way she weighs a block before she decides which way the grain wants to run. She does not give it back.{/n}
"You pay a blind woman for work she may never deliver. Either you are a fool, stranger, or you heard more than I meant to say."
{n}On the bench beside her lies an uncut block of pale birch, the one her fingers keep returning to.{/n}''',
        c('[Press the purse into her hands, and drive a coin into the block on her bench] "The statue\'s not finished, carver. Nobody leaves work on the bench."', "took",
          crusade=("Finances", -150), alignment=("Chaotic", 1), flags=(PRIMED, COMMISSIONED, ADVANCE)),
        c('"Never mind. Keep your hands to yourself."', abort=True)),
    g("took", '''{n}The coin goes into the birch with a sound she hears before you have finished pushing. She puts out a hand, finds the rim of it standing proud of the grain, and does not pull it out.{/n}
"The statue? That statue is finished, stranger. Journeymen finished it, with my eyes still wet on Marhevok's knife. It was never mine."
{n}Her thumb finds the knot of the purse strings and stays there.{/n}
"But I will take your coin, and I will leave the other one where you put it. A commission is a commission. My line has never once gone to its ancestors with paid work on the bench, not in all the generations since the first of us picked up a chisel. Remember that you insisted."''',
        c("Leave her to the wood.")),
    ], requires=("trickster",), forbids=(COMMISSIONED, DEAD, PRIMED), last=3, Relationship="gesmerha", Chapters=[3],
    RequiresAnyGroups=[["gesmerha.feared_hands", "gesmerha.took_risk"]], AnswerLists=[HER_LIST],
    NativeReturnCue=HER_RETURN, EntryMythic="PlayerIsTrickster"))

# 4b. The late fallback: her pyre, in Chapter 3 only (by Chapter 5 Wintersun is gone, KTC_WintersunHelp/Cue_0040).
SCENES.append(scene(P + "dead.pyre", "The carvers' ground", "Gesmerha", 3, "", [
    nar("pyre", '''{n}A carrier from Wintersun finds your camp with a bundle of charcoal and a message from Gesmerha's apprentices. Her funeral has passed. They still bring unpaid work and gifts to the memorial fire on the carvers' ground.{/n}
"You were in the chief's hall. You heard her last words. Was there work she owed you? Her uncut birch is still on the bench. Nobody has dared move it."
{n}He waits with the charcoal dust black on his fingers.{/n}''',
        c('[Send a purse for the memorial fire, and a coin to drive into her uncut birch] "Tell her the statue\'s not finished, carver. Nobody leaves work on the bench."',
          mythic="Trickster", crusade=("Finances", -300), alignment=("Chaotic", 1), flags=(PRIMED, LATE, LAUGHED)),
        c('"I owed her nothing. Leave her ashes alone."', flags=(CLOSED,))),
    ], requires=("trickster", LATCH), forbids=(PRIMED, RETURNED, CLOSED), delay=24, last=3, Relationship="gesmerha",
    Chapters=[3], Remote=True, TricksterDevice=True, TricksterState="dead"))

# 4c. The payoff: a letter carried by the same boy. She is at the Lady's statue in Wintersun; nobody walks into the camp.
SCENES.append(scene(P + "dead.unfinished_work", "Splinters", "Gesmerha", 3, "", [
    nar("start", '''{n}A Wintersun carrier waits at the edge of camp, ash in the seams of his boots. The message from the carvers' ground is addressed to you alone.{/n}''',
        c("Continue", "late", requires=(LATE,)),
        c("Continue", "paid", forbids=(LATE,))),
    nar("late", '''{n}The carrier unfolds a cloth, showing the charcoal that never burned. They laid the birch on the memorial fire with your coin driven into it. Three torches failed to catch. On the second night the apprentices heard three knocks, the count a master uses to call a carver back to unfinished work. Nobody held a mallet.{/n}
{n}On the third dawn they found Gesmerha sitting among the ashes, her palms full of splinters. Her fingers would not release the block until she promised aloud to finish it. The carvers backed away. Their eldest shut his door: Wintersun had trusted enough marvels. She waits outside the houses with the birch and has sent her answer.{/n}
"Tell the stranger: you threw coin on my ashes and a joke after it. The wood would not take either one."''',
        c("Continue", "terms_raised")),
    nar("paid", '''{n}Her apprentices laid the paid birch under her hands. They could not remove your coin. On the second night they heard three knocks from the empty workshop, the count a master uses to call a carver back to unfinished work.{/n}
{n}Before the funeral torches were lit, Gesmerha sat up with splinters in her palms. Her fingers would not release the block until she promised to finish it. The carvers fled; their eldest shut his door. Wintersun had trusted enough marvels. She waits outside the houses, refusing to leave the birch behind. The carrier repeats her message carefully.{/n}''',
        c("Continue", "paid_hands", requires=("gesmerha.feared_hands",)),
        c("Continue", "paid_risk", forbids=("gesmerha.feared_hands",))),
    nar("paid_hands", '"Tell the stranger: you heard me say *hands*, in my own yard, among my own statues, and the next thing you did was '
        'pay for them. I swore I would never shame my ancestors. You knew that too, didn\'t you."',
        c("Continue", "terms")),
    nar("paid_risk", '"Tell the stranger: I told you Marhevok\'s anger was terrible to behold, and that I would risk it anyway, and the '
        'next thing you did was pay me for work I might not live to finish. I swore I would never shame my ancestors. You knew '
        'that too, didn\'t you."',
        c("Continue", "terms")),
    g("terms", '''"There was your coin in the birch, and paid work left on my bench. My ancestors sent me back to finish it. They spoke in the old tongue. I understood enough.
I can sleep. I can travel. But until the last cut, every piece of wood I take up is this commission. Try asking these hands for another carving: they close on the birch again."
"The eldest carver shut his door. I will not force him to watch me work. Send your answer, stranger. If you still want the carving, find me a bench where a dead woman will not frighten the apprentices away."''',
        c("Continue", "answer")),
    g("terms_raised", '''"The ancestors were angry. You paid over my ashes, and they sent me back for the work. But I cannot choose its shape now. This birch must show the Lady as my chisel first found her: the monster, every joint and every tooth. No pretty face to please the clan.
I can rest and travel. Until that carving is finished, my hands close on the birch whenever I try to take up other work. That is what you bought late."
"The eldest carver shut his door. I will not force the others to watch another marvel. Find me a bench where I can finish the truth you paid for."''',
        c("Continue", "answer")),
    nar("answer", "{n}The boy waits for your answer. He has plainly been told to remember it exactly, and to bring it back whatever it is.{/n}",
        c('[Send for her] "Tell her to bring her chisels to Drezen. The smith there makes better ones than the ones she lost, and I want to see the work."',
          flags=(RETURNED, DEBT, STARTED)),
        c('"Tell her to rest. Tell her ancestors they can have her back."', flags=(CLOSED,))),
    ], requires=("trickster.ever", PRIMED, LATCH), forbids=(RETURNED, CLOSED), delay=72, last=5,
    Relationship="gesmerha", Chapters=[3, 5], Remote=True, TricksterDevice=True, TricksterState="dead"))

# 4d. The middle beat and her test, in person, 24 hours after she is sent for.
in_yard(P + "returned.yard", "The smith's yard", '"Gesmerha."', [
    g("start", '''{n}A pale birch log rests in cradles on two trestles, far from the forge. Gesmerha's new chisels lie beside a bucket. The splinters have gone from her palms; their marks remain.{/n}
"Your step. The smith says his boys hear it whenever another regiment is missing. Come here, stranger."
{n}She puts aside a scrap she tried to shape. Her fingers return to the birch.{/n}
"Still this one. The ancestors want it finished. What do you want out of it?"''',
        c('"Carve the monster. Let them see what Wintersun worshipped."', "hold", flags=(STATUE_TRUE,)),
        c('"Carve something new. Not the Lady. You."', "hold", forbids=(LATE,), flags=(STATUE_NEW,)),
        c('"Carve something new. Not the Lady. You."', "lie_first", requires=(LATE,))),
    g("lie_first", '''"No. You paid late. This birch must show the monster we worshipped. Something of mine can wait until these hands are free."''',
        c("Continue", "hold", flags=(STATUE_TRUE,))),
    g("hold", '''{n}She checks the cradles beneath the log, then guides your hands to its far end. The chisel rests well beyond your fingers, its edge pointing away from them.{/n}
"Brace this end. Keep it from turning. If you need to let go, say so and I will stop."
{n}She finds the chisel head with the mallet before lifting it.{/n}''',
        c("[Keep your hands on the wood]", "after", flags=(HELD,)),
        c("[Pull your hands away]", "pulled", flags=(FLINCHED,))),
    nar("pulled", '''{n}You withdraw without warning. The log turns in its cradle and the stroke tears a notch across the grain. Gesmerha stops at the sound. She feels the torn edge, lowers the mallet, and wedges the log firmly herself.{/n}
"That was a week's cutting you nearly took off. Stand back. I will brace it."''',
        c("Continue", "after")),
    nar("after", '''{n}With the log braced, four short strokes lift a curl onto your boot. Gesmerha feels the new cut.{/n}
"There. Something is looking out already. Leave the mallet where it is."''',
        c('"And when it\'s finished?"', "not_yet"),
        c("[Leave her to the wood]", flags=(YARD,))),
    g("not_yet", '''{n}Her hands stop. For a moment she is listening to something that is not in the yard.{/n}
"Finish first. Then ask me what comes after. They are listening, stranger, and they have my hands."''',
        c("[Leave her to the wood]", flags=(YARD,))),
    ], requires=("trickster.ever", RETURNED), forbids=(YARD, CLOSED), delay=24)

# The commit night (heat up to the cut; the cut lands at the start of the act) and the morning after.
NIGHT = '''{n}She hangs the chisels out of reach, spreads a folded cloth over the bench, and turns back to you. Her damp palms rest against your cheeks.{/n}
"One commission finished. And you stayed to hear what I wanted when it was done. Come closer. I have had enough patrons."
{n}She kisses you, then draws you back for a second kiss that leaves her breathing hard. Her fingers find your belt; she opens it, laughing when you catch the buckle before it falls. She pulls off her shift and guides your hands to her waist.{/n}
"Here. The bench will hold us. I checked."
{n}She draws you down with her onto the cloth. Beyond the yard a patrol passes toward the walls; she keeps you close until its boots fade.{/n}'''
NIGHT_REPAIRED = NIGHT.replace(
    "One commission finished. And you stayed to hear what I wanted when it was done. Come closer. I have had enough patrons.",
    "The commission and the wooden hands. Both finished. You have spent three days here; I want this night with you too.")
NIGHT_FLINCHED = NIGHT_REPAIRED.replace(
    "The commission and the wooden hands. Both finished. You have spent three days here; I want this night with you too.",
    "You told me when you needed to move. I could finish the hands without guessing. That quarrel is done. Now come closer. I want you.")
MORNING = '''{n}The forge is still banked. Gesmerha sits beside the trestles with a small block in her lap. She reaches back for your hand when she hears you wake, and presses it to the rough mouth she has carved.{/n}
"Yours. This one stays with me. The big paid work can go where it is owed; nobody gets this with it."
{n}She draws you close enough to kiss, then retrieves her apron from beneath your shoulder.{/n}
"The smith will want his yard. And you have a war. Come back when you can stay, stranger. I have more of this face to find."'''

in_yard(P + "returned.bench", "What comes after", '"You said to ask you when it was finished."', [
    nar("start", '''{n}Late. The forge is banked and the yard is dark except for a lamp she does not need and has lit for you.{/n}''',
        c("Continue", "monster", requires=(STATUE_TRUE,)),
        c("Continue", "new", requires=(STATUE_NEW,))),
    g("monster", '''{n}The birch on the trestles has too many joints, and a smile that runs past the edges of its face. Gesmerha guides your palm over it, then takes both hands away.{/n}
"That is what we prayed to. No journeyman has smoothed the teeth away this time."
{n}She works the coin out of the base and lays it beside the finished carving. Then she washes her palms. They stay open when she lifts them from the bucket.{/n}
"The truthful carving. Finished, as they demanded. These hands are mine."''',
        c("Continue", "ask")),
    g("new", '''{n}The birch on the trestles is a woman listening, her head tilted back. Gesmerha guides your hand over its face, then takes both hands away.{/n}
"You paid for a carving. Here it is. Even the turn of the head is mine."
{n}She works the coin out of the base and lays it beside the finished figure. Then she washes her palms. They stay open when she lifts them from the bucket.{/n}
"Finished. The ancestors have their work. These hands are mine."''',
        c("Continue", "ask")),
    g("ask", '''{n}The smith takes his supper home. Gesmerha wraps the mallet and sets the roll aside, away from the completed birch.{/n}
"I could take another block now. Or nothing at all. I tried it this morning: sat with empty hands until the smith asked if I was ill."
{n}She laughs once, softly.{/n}
"You asked what comes after. Have you come for the carving, or will you stay to hear my answer?"''',
        c('[Stay at the bench] "Then let me be what comes after."', "terms", forbids=(FLINCHED,)),
        c('[Stay at the bench] "Then let me be what comes after."', "flinch", requires=(FLINCHED,)),
        c('"Finish your life without me, carver. You\'ve earned it."', flags=(CLOSED, "gesmerha.parted"))),
    g("terms", '''"I want you here when the work is done. In my bed, stranger. You listen when I curse the grain, and you came back to hear me without another order ready. I have been wanting you for days."
{n}She reaches for your hand and draws it against her waist.{/n}
"Leave the purse outside. I will not have another coin driven into anything of mine. Can you do that?"''',
        c('"No more purses. Not for you. I swear it."', "night", flags=(COMMITTED,)),
        c('"I can\'t swear that. Buying things is what I do."', "postpone")),
    g("postpone", '''"Then you are honest, which is worse. Go. Come back when you have thought about what you would have to stop being. The bench will still be here. So will I, probably."''',
        c("[Go]", flags=(DECLINED,))),
    g("flinch", '''"You let the log turn without a word. I heard the cut tear. I have had work spoiled for me before, stranger. I will not lie down with that quarrel still between us."
{n}She touches your wrist, then releases it.{/n}
"I wanted you to stay. I still do. But tonight I would keep hearing that stroke. Go. Let me think."''',
        c("[Go]", flags=(DECLINED,))),
    g("night", NIGHT, c("Continue", "morning")),
    g("morning", MORNING, c("[Go]", flags=(NIGHT_YARD,))),
    ], requires=("trickster.ever", RETURNED, YARD), forbids=(COMMITTED, CLOSED, DECLINED), delay=72)

# 4f. After her soft no she asks, in her own craft: not a price but a trade of hands. The Commander's war waits three days.
in_yard(P + "returned.second_ask", "A pair that were never for sale", '"About what comes after."', [
    g("start", '''{n}The paid carving stands apart from the trestles. Gesmerha has brought a fresh block and two stools.{/n}
"I will not ask for the purse oath again. Give me three days instead. Sit while I carve your hands. No commander buying my time, no carver selling it. I want to know these hands when they are doing nothing for the crusade."
{n}She taps the nearer stool.{/n}
"I have missed you. Sit, and let me finish being cross."''',
        c("Continue", "price", forbids=(FLINCHED,)),
        c("Continue", "price_flinched", requires=(FLINCHED,))),
    g("price_flinched", '''"Tell me before you move. We can stop for a meal or stretch our backs; the wood will wait. I want to finish a piece with you beside me without hearing it tear again."''',
        c("Continue", "price")),
    g("price", '''{n}She holds out her open palms and waits.{/n}''',
        c("[Sit for her for three days]", "sat", crusade=("Favors", -100), flags=(COMMITTED, HANDS)),
        c('"Not like this."', flags=(CLOSED,))),
    nar("sat", '''{n}For three days the smith brings couriers to the gate while she sets your hands against a folded cloth. Between sittings you eat, stretch, and hear their reports. Each time you return she finds the pose again by touch.{/n}
{n}On the third evening she compares the wooden hands with yours and puts the knife away. She keeps your hands in hers.{/n}
"Done. I will keep these. And I want you to stay tonight. I have been thinking about it through every damned finger."''',
        c("Continue", "night", forbids=(FLINCHED,)),
        c("Continue", "night_flinched", requires=(FLINCHED,))),
    g("night", NIGHT_REPAIRED, c("Continue", "morning")),
    g("morning", MORNING, c("[Go]", flags=(NIGHT_YARD,))),
    g("night_flinched", NIGHT_FLINCHED, c("Continue", "morning")),
    ], requires=("trickster.ever", RETURNED, DECLINED), forbids=(COMMITTED, CLOSED), delay=96)

# 4g. The second work (COX, Sol 2026-09-30): the ancestors' commission is finished on the bench before Threshold. The face
# she began the morning after the night is hers, unpaid, and still on her bench; Last Call reads what became of it
# (LIKENESS: left unfinished for the Commander to sit for; LIKENESS_DONE: cut from memory; neither: never discussed).
in_yard(P + "returned.likeness", "The face on the second block", '"The face on your new block..."', [
    g("start", '''{n}The new block stands on the trestles where the finished work stood. The face that came out of it the morning after is further along now: the brow, the set of the mouth, a scar you had forgotten you owned. The eyes are two smooth hollows. Her chisel lies beside it, clean, as if it has not been lifted for days.{/n}
"You walk like someone going somewhere they may not walk back from. The whole yard hears it. The smith's boys have started saying goodbye to you."
{n}She sets her palm flat on the wooden brow.{/n}
"This is not the ancestors' work. Nobody paid for it, and nobody will. But it is on my bench, and you know what my line does about work on the bench. I will not cut the last of a face whose owner is walking into the demons' country. From memory I would be carving a grave-post, and I cut enough of those for Wintersun."''',
        c('[Lay your hand on the block beside hers] "Then leave it unfinished. I\'ll come back and sit for the last cuts."', "owed",
          flags=(LIKENESS,)),
        c('"Finish it now, from memory. If I don\'t come back, you\'ll have the face."', "memory", flags=(LIKENESS_DONE,))),
    g("owed", '''"Then sit for it when you return. I will feel your face before I pick up the chisel. Keep that war of yours outside my yard for an afternoon."
{n}She covers the small likeness and knots the cloth. Her palm stays on its brow.{/n}
"This stays with me. The paid birch is finished. This face can wait for its owner."''',
        c("[Go]")),
    g("memory", '''"My hands remember what my eyes cannot see."
{n}She picks up the chisel. Two cuts, and the hollows are eyes, and they are yours, and the face on the block has finished with you.{/n}
"There. Now it is a grave-post whether you come back or not. Go on. Walk loudly."''',
        c("[Go]")),
    ], requires=("trickster.ever", RETURNED, COMMITTED), forbids=(LIKENESS, LIKENESS_DONE, CLOSED), delay=48)


# --- State 2, the missed window: wrong footsteps (F04, claimed, not implanted) ----------------------------------------------

def footsteps(suffix, lists, areas, extra):
    SCENES.append(scene(P + "missed.wrong_footsteps_" + suffix, "Wrong footsteps", "Gesmerha", 5,
        '[Claim the unfinished game] "You know my step, carver. Ten afternoons at your board, and a game we never finished."', [
        g("start", '''{n}Her hands stop on the wood as she recognizes your step.{/n}
"Ten afternoons? I remember the visits you made, stranger. Do not add visits with your mouth."
{n}She sets a bowl of pieces between you.{/n}
"If you want a game, ask for one. Here is the rule: an outer-row piece must come inward on its next move. Say your moves aloud. I want to hear you lose properly."''',
            c("[Sit down and play as if you remember]", "game"),
            c('"All right. It was a lie. I wanted a reason to sit here."', "honest"),
            c('"Never mind."', abort=True)),
        g("game", '''{n}You name your moves. On the fourth, you try to keep a piece in the outer row. Her fingers close briefly on your wrist.{/n}
"Inward. I told you."
{n}You move it back. She takes it two turns later, and wins the game.{/n}
"There. A real game, and you lost it. We can add that to the visits you actually made. The loser pays for the pieces."''',
            # gesmerha.campaign_slow: the courtship the late chain reads (an unresolved romance, as the registered slow start);
            # SLOW (cost.campaign_slow) marks only the trick itself.
            c("[Pay for the pieces]", crusade=("Finances", -50), alignment=("Chaotic", 1), forbids=("gesmerha.friendship",),
              flags=("gesmerha.campaign_kept", "gesmerha.campaign_slow", CATCHUP, SLOW)),
            # PP7 (Sol BEL): a friendship she already named in Wintersun stays a friendship.
            c("[Pay for the pieces]", crusade=("Finances", -50), alignment=("Chaotic", 1), requires=("gesmerha.friendship",),
              flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends", CATCHUP, SLOW))),
        g("honest", '''"Then say that next time. I remember your real visits; you need not embroider them. Sit. We can play while the demons are busy elsewhere. The loser pays for the pieces."''',
            c("[Pay for the pieces, and sit down]", crusade=("Finances", -50), forbids=("gesmerha.friendship",),
              flags=("gesmerha.campaign_kept", "gesmerha.campaign_slow", CATCHUP)),
            c("[Pay for the pieces, and sit down]", crusade=("Finances", -50), requires=("gesmerha.friendship",),
              flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends", CATCHUP))),
        ], requires=("trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.met", *extra),
        forbids=("gesmerha.campaign_kept", DEAD, CLOSED, CATCHUP, "inhuman"), delay=0, last=5, Relationship="gesmerha",
        Chapters=[5], RequiresAny=["gesmerha.truth", "gesmerha.illusions"], AnswerLists=lists, ContactUnit=UNIT,
        Areas=areas, EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="missed"))


footsteps("home", [HOME_LIST], [WINTERSUN], ())
footsteps("capital", [CAPITAL_LIST], [DREZEN], ("gesmerha.capital_guest",))


def first_meeting(suffix, lists, areas, extra):
    """Sol round 2 (INT): the footsteps need her one pre-resolution meeting (gesmerha.met). A live Trickster who resolved
    Wintersun without ever speaking to her meets her here, for the first time, and invents no earlier visit."""
    SCENES.append(scene(P + "missed.first_meeting_" + suffix, "A step she does not know", "Gesmerha", 5,
        '"You are the woodshaper. I never came to your bench."', [
        g("start", '''{n}Her hands stop on the wood as your step reaches the bench. She tilts her head toward it, the way she listens for a crack in the grain, and does not find what she is listening for.{/n}
"A step I do not know. Heavy in the heel, in a hurry, and pretending not to be."''',
            c("Continue", "known_truth", requires=("gesmerha.truth",)),
            c("Continue", "known_illusions", requires=("gesmerha.illusions",), forbids=("gesmerha.truth",))),
        g("known_truth", '''{n}Her mouth tightens.{/n} "The clan says the Commander who tore the mask off our Lady walked through Wintersun and never once came near my bench. Is that you?"''',
            c('"It is. I should have come sooner."', "board"),
            c('"Never mind."', abort=True)),
        g("known_illusions", '''{n}She lowers her voice.{/n}
"You left the village its dream. I know what the Lady is. Not everyone needed to hear it from me. Was that kindness, Commander, or were you in a hurry to leave?"''',
            c('"It is. I should have come sooner."', "board"),
            c('"Never mind."', abort=True)),
        g("board", '''"Sooner, later. The dead of Wintersun do not care which."
{n}She pushes a half-cut board across the bench toward you: rows notched along one edge, pieces in a bowl.{/n}
"I made this for two people and no army. Half the rules are mine, and half have been winning arguments with me for years. Sit. Play badly. I want to hear what a Commander's hands do when nobody is asking them for anything."''',
            c("[Sit down and play]", "game")),
        g("game", '''{n}You lose the first game in a dozen moves and the second in rather more. She makes you name every row before you move, and catches you once reaching for a corner she has already taken.{/n}
"There. Now I know your step and your hands both. The loser pays for the pieces, Commander. That is the one rule nobody has ever argued with me about."''',
            c("[Pay for the pieces]", crusade=("Finances", -50),
              flags=("gesmerha.campaign_kept", "gesmerha.campaign_slow", FIRSTMET))),
        ], requires=("trickster", "trickster.ever", "gesmerha.wintersun_resolved", *extra),
        forbids=("gesmerha.campaign_kept", "gesmerha.met", DEAD, CLOSED, CATCHUP, FIRSTMET, "inhuman"), delay=0, last=5,
        Relationship="gesmerha", Chapters=[5], RequiresAny=["gesmerha.truth", "gesmerha.illusions"], AnswerLists=lists,
        ContactUnit=UNIT, Areas=areas, EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="missed"))


first_meeting("home", [HOME_LIST], [WINTERSUN], ())
first_meeting("capital", [CAPITAL_LIST], [DREZEN], ("gesmerha.capital_guest",))


# --- Epilogue pages (no mythic, alignment or crusade effects) ---------------------------------------------------------

# Native KTC/Cue_0026: carver dead, forest dead, Marhevok not chief.
CLAN_DESTROYED = "gesmerha.trickster.clan_destroyed"
STATUE_PARAGRAPHS = (
    p("{n}The truthful monster stood in the smith's yard until spring. Surviving Wintersun carvers took it home and set it where the Lady had stood. Gesmerha made them feel the teeth before they covered it for the journey.{/n}",
      requires=(STATUE_TRUE,), forbids=(CLAN_DESTROYED,)),
    p("{n}The listening woman stayed by the smith's gate. When he offered to sell her, Gesmerha named a price he could not pay and laughed at his answer.{/n}", requires=(STATUE_NEW,)),
    p("{n}She kept the wooden hands beside her chisels. Between the three days of sittings they had eaten and argued over couriers' reports. Nobody had bought her time at that bench.{/n}", requires=(HANDS,)),
    p("{n}The surviving carvers never mentioned the memorial fire to the Commander again. Gesmerha did, whenever anyone tried to order work she had not agreed to do.{/n}", requires=(LAUGHED,), forbids=(CLAN_DESTROYED,)),
    p("{n}No one came from Wintersun for the monster. The clan was dead. Gesmerha kept it in Drezen and named the people who had knelt before that smile. She refused the smith's sack; their memorial would show its teeth.{/n}",
      requires=(STATUE_TRUE, CLAN_DESTROYED)),
    p("{n}With the Wintersun carvers dead, Gesmerha alone remembered the coin sent over her ashes. She kept it beside the completed work, away from the pieces she chose to make.{/n}", requires=(LAUGHED, CLAN_DESTROYED)),
)


def page(id, title, text, requires, forbids, paragraphs=(), **extra):
    SCENES.append(scene(P + "epilogue." + id, title, "Epilogue", 1, "", [nar("start", text, c(), paragraphs=paragraphs)],
                        requires=requires, forbids=forbids, last=99, Relationship="gesmerha", **extra))


page("bench", "What came after", '''{n}Gesmerha kept the corner of the smith's yard after the war. On the Commander's first return she finished the cut under her hand, wrapped the knife, and came to the gate herself. The small likeness stood beside her cup. She pressed the Commander's hand against its mouth, then kissed the living one and led the way inside.{/n}
"You can tell me about the war tomorrow. Tonight I want you here."
{n}The smith learned to knock on the gate before entering his own yard.{/n}''',
     requires=(RETURNED, COMMITTED), forbids=(CLOSED, "sacrifice"), ForbidOverrides={"sacrifice": "trickster.commander_back"},
     paragraphs=(
         p("{n}The Commander kept the oath about purses, which surprised everyone who knew the Commander.{/n}", forbids=(HANDS,)),
         p("{n}The Commander never swore off buying things, and she never asked again. Three days of sittings in her yard "
           "had been kept instead. The wooden hands stayed beside her tools; on later visits she found the living pair "
           "and held them while she spoke.{/n}",
           requires=(HANDS,)),
     ) + STATUE_PARAGRAPHS)

page("commit", "The Commander's door", '''{n}After Threshold, Gesmerha finished the paid birch in the smith's yard. She had it delivered to the Commander's door with the coin laid beside it. The smith offered to take her tools too. She refused.{/n}
"I promised a carving. The tools stay here. So do I, until I choose another bench."
{n}There was no private likeness among the things delivered, and no invitation owed with the payment.{/n}''',
     requires=("trickster.ever", RETURNED), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"), paragraphs=STATUE_PARAGRAPHS,
     RequiresAnyGroups=[[YARD, PRESENCE_FAILED]], ForbidOverrides={"sacrifice": "trickster.commander_back"})

# The Commander genuinely died at Threshold (sacrifice without a Trickster return): the commission is resolved, and no
# postwar meeting is implied.
page("commit_mourned", "Paid work, delivered", '''{n}Gesmerha finished the paid birch after Threshold, for a patron who would not collect it. She set the coin beside the work. She asked the smith to put a small shaving on the grave instead. The finished carving stayed where people could touch it.{/n}
{n}She had paid the ancestors' debt. What she made next was hers to choose.{/n}''',
     requires=("trickster.ever", RETURNED, "sacrifice"), forbids=(COMMITTED, CLOSED, DECLINED, "trickster.commander_back"),
     paragraphs=STATUE_PARAGRAPHS, RequiresAnyGroups=[[YARD, PRESENCE_FAILED]])

page("bench_mourned", "The face with its eyes", '''{n}When word came from Threshold, Gesmerha asked the messenger to leave her alone. She sat beside the small private likeness until the forge went cold. In the morning she unwrapped her tools and began the work she had chosen for herself.{/n}''',
     requires=(RETURNED, COMMITTED, "sacrifice"), forbids=(CLOSED, "trickster.commander_back"), paragraphs=STATUE_PARAGRAPHS)

page("unvisited", "The corner of the yard", '''{n}Gesmerha finished the paid birch alone in the smith's yard. When her hands were free, she put them in cold water for a long time, then took up a scrap she had been unable to shape while the commission waited. The smith asked what it would be. She told him she had not decided.{/n}''',
     requires=("trickster.ever", RETURNED), forbids=(YARD, PRESENCE_FAILED, COMMITTED, CLOSED, DECLINED),
     paragraphs=STATUE_PARAGRAPHS)

page("refusal", "Paid for", '''{n}Gesmerha finished the paid birch and left it in the smith's yard. A journeyman wrote her directions for its delivery. What she had asked for at the bench had not been given; she did not ask again. She took up work of her own.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), paragraphs=STATUE_PARAGRAPHS)

page("finished", "Her own life", '''{n}Gesmerha finished the paid work, wrapped her chisels, and left the yard. She had kept the distance the Commander asked for. The commission did not buy another meeting, and she sent no message back.{/n}''',
     requires=("trickster.ever", RETURNED, CLOSED), forbids=(COMMITTED,), paragraphs=STATUE_PARAGRAPHS)


# --- Reactions (exactly Ulbrig, Lann and Anevia) ----------------------------------------------------------------------

LANN = dict(requires=("lann.in_party",), forbids=("lann.dead", "lann.kicked_out"))
ULBRIG = dict(requires=("ulbrig.in_party",), forbids=("ulbrig.dead", "ulbrig.kicked_out"))

REACTIONS = [
    reaction("Lann", P + "react.lann_pyre", (LAUGHED, *LANN["requires"]),
             '''"You sent a joke to a funeral. In Sarkoris. The boy who carried it looked like he wanted to be sick." {n}Lann scratches the back of his neck.{/n} "What did it say? No. Don't tell me. I'll hear about it anyway."''',
             answer_list=LANN_HUB, forbids=LANN["forbids"], chapter=3, last=3, delay=24, entry='"About the carver\'s pyre..."'),
    reaction("Ulbrig", P + "react.ulbrig_return", (RETURNED, *ULBRIG["requires"]),
             '''"A Wintersun carver got up off the carvers' ground, they're saying, and went straight back to work." {n}Ulbrig sets his mug down, which he does not do lightly.{/n} "Unfinished work brought her back? Then I want to know what happens when she puts the chisel down. I would be there for the last cut, warchief."''',
             answer_list=ULBRIG_HUB, forbids=(*ULBRIG["forbids"], WORK_FINISHED), chapter=3, last=5, delay=24, entry='"About the carver from Wintersun..."'),
    reaction("Anevia", P + "react.anevia_yard_night", (NIGHT_YARD,),
             '''"The smith came to me again. Not about his corner this time." {n}Anevia keeps a straight face for as long as she can manage it, which is not long.{/n} "He banked the forge, went home, came back at dawn, and found the Commander of the crusade asleep in his shavings with sawdust in places he wouldn't name to a married woman. He wants to know whether he can charge you rent. I told him to ask the carver. He went a very interesting colour."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "anevia_dead"), chapter=3, last=5, delay=24,
             entry='"About the smith\'s yard, again..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
    reaction("Anevia", P + "react.anevia_return", (RETURNED,),
             '''"The smith came to me about a blind woman in his yard. Won't give his corner back, won't let his boys near her log, and says you owe her the good chisels." {n}Anevia shrugs.{/n} "I told him that sounded about right."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "anevia_dead"), chapter=3, last=5, delay=24,
             entry='"About the smith\'s yard..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
    # The footsteps reactions read the branch actually played: the trick (SLOW: she caught the lie, the Commander knew one
    # rule and paid for the pieces as the loser) or the confession (CATCHUP without SLOW: the lie owned before the game).
    reaction("Lann", P + "react.lann_footsteps", (CATCHUP, SLOW, *LANN["requires"]),
             '''"The blind carver's telling everyone you sat down at her board and swore you'd played there ten afternoons. She says she explained the rule and you broke it anyway. Then she beat you." {n}Lann grins.{/n} "And you paid for the pieces. Like a loser. I've never seen you sit still for ten minutes, never mind lose sitting down."''',
             answer_list=LANN_HUB, forbids=LANN["forbids"], chapter=5, last=5, delay=24, entry='"About the carver..."'),
    reaction("Anevia", P + "react.anevia_footsteps", (CATCHUP, SLOW),
             '''"The Wintersun carver's telling anyone who'll listen that you claimed ten afternoons at her bench. She says she remembers the real visits, and explained the rule twice before you lost." {n}Anevia gives you a long look.{/n} "I keep your calendar, Commander. I'd remember ten afternoons. I would have asked for a rematch."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "anevia_dead"), chapter=5, last=5, delay=24,
             entry='"About the carver..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
    reaction("Lann", P + "react.lann_confessed", (CATCHUP, *LANN["requires"]),
             '''"Heard you walked up to the blind carver, told her you'd spent ten afternoons at her board, and took it back before she'd finished calling you a liar." {n}Lann scratches his jaw.{/n} "She made you pay for the pieces anyway. Honest liars pay too, she says. I'm writing that one down."''',
             answer_list=LANN_HUB, forbids=(SLOW, *LANN["forbids"]), chapter=5, last=5, delay=24, entry='"About the carver..."'),
    reaction("Anevia", P + "react.anevia_confessed", (CATCHUP,),
             '''"The carver says you lied to her about ten afternoons and then owned up to it before the first move." {n}Anevia gives you a long look.{/n} "I keep your calendar, Commander, so I knew about the ten. Owning up is the part I'd never have guessed."''',
             answer_list=ANEVIA_HUB, forbids=(SLOW, "anevia_gone", "anevia_dead"), chapter=5, last=5, delay=24,
             entry='"About the carver..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
]
SCENES.extend(REACTIONS)


# --- The registered route ---------------------------------------------------------------------------------------------

# The alive chain: if she lived through the ambush with a commission paid, she carves it.
COMMISSION_PARAGRAPH = p("{n}She carved the Commander's commission in the end, years after it was paid for: a small thing in "
                         "the pale birch from her Wintersun bench, with the coin still in it, which she would not describe to anyone. She said a commission is a commission, and "
                         "that her line had never left paid work on the bench.{/n}", requires=(COMMISSIONED,), forbids=(RETURNED,))
BORROWED_PARAGRAPH = p("{n}She never believed in the ten afternoons. She kept count of the real ones instead, and told the "
                       "Commander once that they had long since passed ten, and that the borrowed ones were paid back.{/n}",
                       requires=(SLOW,))
ALIVE_ENDINGS = ("gesmerha.ending_living_reunion", "gesmerha.ending_unmet_again", "gesmerha.late_ending_lovers",
                 "gesmerha.late_ending_friends", "gesmerha.late_ending_open", "gesmerha.late_ending_closed",
                 "gesmerha.late_ending_unfinished")
LATE_LIVING = ("gesmerha.late_ending_lovers", "gesmerha.late_ending_friends", "gesmerha.late_ending_open")
LOSS_PAGES = ("gesmerha.ending_loss", "gesmerha.late_ending_loss")

# The trust step the claimed afternoons add to the registered late chain's first visit.
CATCHUP_NODE = g("catchup", '''{n}Gesmerha keeps the folded blanket on the chest.{/n}
"You came back. Good. Leave the invented afternoons outside. I remember the real ones. Before you sit, tell me something true about Wintersun. You came there with an army; what did you find?"''',
    c('[Sit where she has made room.]', "work"))


# The same trust step for a Commander who met her for the first time in Chapter 5 (one afternoon, two lost games).
FIRST_MET_NODE = g("first_met", '''{n}Gesmerha rests her hand on the folded blanket.{/n}
"The Commander who loses at my board. Before we play again, tell me something true about Wintersun. You came there with an army; what did you find?"''',
    c('[Sit where she has made room.]', "work"))


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Gesmerha Trickster integration missing scene: " + id)
    return by_id[id]


def _paragraphs(scene_, paragraphs):
    for node in scene_["Nodes"]:
        if all(ch.get("Next") is None for ch in node["Choices"]):
            node.setdefault("Paragraphs", []).extend(dict(x) for x in paragraphs)


def integrate(payload):
    # Authored phase-4 ix-b reactions; appended without changing saved scene references.
    import copy
    from storylines.trickster_interactions_ix_b import SCENES as interactions
    payload["Scenes"].extend(copy.deepcopy(interactions))
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered."""
    rel = payload["Relationships"]["gesmerha"]
    rel["Objective"] = "Speak with Gesmerha"
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(x) for k, x in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Gesmerha who died with paid work on her bench may not stay dead; look for "
                        "her in the Drezen smith's yard. A Trickster who never sat at her bench in Wintersun may still claim "
                        "to have.")
    payload.setdefault("Presences", {}).update({k: dict(x) for k, x in PRESENCES.items()})
    by_id = {x["Id"]: x for x in payload["Scenes"]}

    # G6(b): every registered scene that Forbids her death lifts it after a return; the loss pages belong to a Gesmerha
    # who stayed dead.
    for s in payload["Scenes"]:
        if s.get("Relationship") == "gesmerha" and not s["Id"].startswith(P) and DEAD in s["Forbids"]:
            s.setdefault("ForbidOverrides", {})[DEAD] = RETURNED
    for id in LOSS_PAGES:
        loss = _scene(by_id, id)
        if RETURNED not in loss["Forbids"]:
            loss["Forbids"].append(RETURNED)

    # The commission leaves a mark on the living endings; the claimed afternoons on the late ones.
    for id in ALIVE_ENDINGS:
        _paragraphs(_scene(by_id, id), (COMMISSION_PARAGRAPH,))
    for id in LATE_LIVING:
        _paragraphs(_scene(by_id, id), (BORROWED_PARAGRAPH,))

    court = _scene(by_id, "gesmerha.the_voice_at_court")
    for key in (CATCHUP, FIRSTMET):
        if key not in court["Forbids"]:
            court["Forbids"].append(key)

    # The first late visit: a Commander who only claimed the afternoons is asked for one true thing before sitting. The
    # registered "too long since our last afternoon" answer is retired for that Commander by a gate, not removed.
    first = _scene(by_id, "gesmerha.the_things_still_here")
    start = next(x for x in first["Nodes"] if x["Id"] == "start")
    without = next(ch for ch in start["Choices"] if ch.get("Next") == "without_court")
    for key in (CATCHUP, FIRSTMET):
        if key not in without["Forbids"]:
            without["Forbids"].append(key)
    start["Choices"].append(c('"I came back to lose the eleventh game."', "catchup", requires=(CATCHUP,),
                              forbids=("gesmerha.reunion_kept",)))
    first["Nodes"].append(dict(CATCHUP_NODE, Portrait="Gesmerha"))
    start["Choices"].append(c('"I came back, as I said I would."', "first_met", requires=(FIRSTMET,),
                              forbids=("gesmerha.reunion_kept", CATCHUP)))
    first["Nodes"].append(dict(FIRST_MET_NODE, Portrait="Gesmerha"))

    _round2(payload, by_id)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'gesmerha.trickster.dead.unfinished_work',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]


def _round2(payload, by_id):
    """Authored SP1–6 revisions. Existing receipts, costs and answer positions stay intact."""
    payload.setdefault("Derived", {})[CLAN_DESTROYED] = [[DEAD, "soana.forest_dead"]]
    payload.setdefault("DerivedForbids", {})[CLAN_DESTROYED] = ["gesmerha.marhevok_rules"]

    def nodes(sid):
        return {x["Id"]: x for x in by_id[sid]["Nodes"]}

    # Inline capital audiences finish before the native cutscene completes the guest etude.
    for sid in ("gesmerha.the_voice_at_court", P + "missed.wrong_footsteps_capital",
                P + "missed.first_meeting_capital"):
        s = by_id[sid]
        # KTC/Cue_0047 is unconditional and reopens this list without actions.
        # NativeReturnCue keeps the pre-existing cue/answer GuidFor namespace.
        s["NativeReturnCue"] = "de348517119791d4e9f7de7de0beab25"
        # Inline speakers are the native audience participants, not queued contacts.
        s.pop("ContactUnit", None)
        for x in s["Nodes"]:
            if x["Speaker"] == "Gesmerha":
                x["SpeakerUnit"] = UNIT

    # The first kept authored visit is also a meeting; native introduction is not the only evidence.
    for suffix in ("home", "capital"):
        known = by_id[P + "missed.wrong_footsteps_" + suffix]
        known["Requires"].remove("gesmerha.met")
        known.setdefault("RequiresAnyGroups", []).append(["gesmerha.met", "gesmerha.invited"])
        first = by_id[P + "missed.first_meeting_" + suffix]
        first["Forbids"].append("gesmerha.invited")
        if suffix == "capital":
            x = nodes(first["Id"])["known_illusions"]
            x["Text"] = ('{n}She lowers her voice.{/n} "I left most of the clan its dream. I told the warriors the truth '
                         'and taught them to hear it without trusting their eyes. They were the ones who would have to fight. '
                         'You left us peace, Commander. I had to prepare for its end."')
            x["Choices"][0]["Text"] = '\"I should have come to hear you sooner.\"'
        if suffix == "home":
            x = nodes(first["Id"])["known_illusions"]
            x["Text"] = '{n}She lowers her voice.{/n} "You left the village its dream. I know what the Lady is. Not everyone needed to hear it from me. Was that kindness, Commander, or were you in a hurry to leave?"'
            # Existing two answers retain their positions, now answering her actual question.
            x["Choices"][0]["Text"] = '"I wanted to spare them. I should have come to hear you."'
            # Marhevok's retained leadership has its own account, never hers as chief.
            start = nodes(first["Id"])["start"]
            start["Choices"][1]["Forbids"].append("gesmerha.marhevok_rules")
            start["Choices"].append(c("Continue", "chief_illusions", requires=("gesmerha.illusions", "gesmerha.marhevok_rules"),
                                     forbids=("gesmerha.truth",)))
            first["Nodes"].append(g("chief_illusions",
                '{n}She lowers her voice.{/n} "Marhevok still rules, and the Lady still smiles for the village. The chief says you left us that peace. I have heard his account. Now I would hear yours."',
                c('"I wanted to spare the village. I should have come to hear you."', "board"),
                c('"Another time."', abort=True)))

    # A true statement is selected by the player. It pays the stated narrative debt without a new mechanic.
    first = by_id["gesmerha.the_things_still_here"]
    ns = nodes(first["Id"])
    for nid in ("catchup", "first_met"):
        ns[nid]["Choices"][0]["Text"] = '"I came hunting demons. I found people praying to one."'
        ns[nid]["Choices"][0]["Next"] = "true_account"
        ns[nid]["Choices"].append(c('"I cannot stay to tell it properly. Another afternoon."', abort=True))
    first["Nodes"].append(g("true_account",
        '{n}Gesmerha moves the blanket from the chest.{/n} "That much I know too. Sit. Tell me what you did with the people you found. I want your account, not the one they repeat about you."',
        c('[Sit and tell her about the Wintersun expedition.]', "work")))

    # Her answer to the slower lover follows an actual spoken proposal, not narrated agreement.
    room = by_id["gesmerha.the_room_she_chose"]
    ns = nodes(room["Id"])
    ns["slow"]["Choices"][0]["Text"] = '"I want to be your lover, when our roads bring us together."'
    ns["slow"]["Choices"][0]["Next"] = "lover_answer"
    room["Nodes"].append(g("lover_answer",
        '"Yes. I want that too. I will keep my road, and I will keep the evenings I promise you. Come here before I start another speech."',
        c('[Kiss her.]', "first_kiss")))
    ns["first_kiss"]["Choices"][0]["Text"] = '[Keep the relationship and an unhurried evening.]'
    ns["after_night"]["Text"] = ns["after_night"]["Text"].replace('back in my bed', 'in my bed')

    # GES-02/04: a small private likeness is hers, never a reward or a further obligation.
    future = by_id["gesmerha.the_work_left_finished"]
    ns = nodes(future["Id"])
    ns["offer"]["Text"] += ('\n{n}She takes a small rough likeness from her bundle and sets it beside her cup.{/n} '
        '"I began this from memory, between the crates and the army\'s wagons. It stays with me. The commissioned pieces go to their owners; this one has no buyer."')
    # Her testimony names only what the run knows; the paid monster is already available to touch.
    likeness = by_id[P + "returned.likeness"]
    ns = nodes(likeness["Id"])
    ns["start"]["Text"] = ('{n}The small likeness stands on the trestles. Gesmerha feels its brow, then touches your face '
        'with empty hands before returning to the wood. The eyes remain smooth hollows.{/n}\n'
        '"Sit still a moment, Commander. This one stays with me. The paid work is finished; I can sell it, send it away, '
        'or refuse an offer without losing these hands. This face is nobody\'s commission."\n'
        '{n}She puts the chisel down.{/n} "You are going to Threshold. Shall I wait for you to sit for the eyes, or finish them from memory?"')
    # Conditional paragraphs are epilogue-only. A normal dialogue uses an inline branch instead.
    bench = by_id[P + "returned.bench"]
    monster = nodes(bench["Id"])["monster"]
    monster["Choices"][0]["Forbids"].append("gesmerha.truth")
    monster["Choices"].append(c("Continue", "truth_testimony", requires=("gesmerha.truth",)))
    bench["Nodes"].append(g("truth_testimony",
        '"Jerribeth gave them a beautiful face to kneel to. They cut out my eyes when the wood showed what was behind it. '
        'That carving will keep its teeth. I will not make her bargain pretty for anyone."', c("Continue", "ask")))

    # Authored r3: Threshold farewell belongs after the Iz expedition, in Chapter 5.
    likeness["MinChapter"] = 5
    likeness["Chapters"] = [5]
    likeness["Requires"].append("iz.done")

    # Explicit slots append to node lists; all original answers and aftermath receipts retain their indices/effects.
    def slot(sid, before, after, number):
        s = by_id[sid]
        nid = sid + ".explicit." + str(number)
        x = nodes(sid)[before]
        assert x["Choices"][0]["Next"] == after, (sid, before)
        # The slot IS the existing threshold, not a second draw-down after it.
        # Saved threshold nodes remain intact and still lead to their aftermath.
        for node in s["Nodes"]:
            for choice in node["Choices"]:
                if choice.get("Next") == before:
                    choice["Next"] = nid
        # An inert appended arc keeps the saved node structurally reachable.
        s["Nodes"].append(g(nid, x["Text"], c("Continue", after),
                                c("Continue", before, requires=("trickster.now",), forbids=("trickster.now",))))

    # Brief: workshop pallet, her initiative; the barred door keeps clan errands outside.
    slot("gesmerha.what_she_asks", "private", "after_private", 1)
    # Brief: sorting-hall reunion after the box and lesson; her own evening.
    slot(room["Id"], "night", "after_night", 1)
    # Brief: the slow lover accepts her first sexual night; distinct commitment aftermath.
    slot(room["Id"], "first_night", "after_first_night", 2)
    # Brief: one completed ancestral commission, paid work set apart; she owns the invitation.
    slot(bench["Id"], "night", "morning", 1)
    # Brief: three-day alternative sitting completed; two carved works, unpaid chosen night.
    slot(P + "returned.second_ask", "night", "morning", 1)
    # Brief: spoiled cut repaired through patient sittings with breaks; no bodily endurance test.
    slot(P + "returned.second_ask", "night_flinched", "morning", 2)

    # Collect the actual likeness and no-purses/sitting debts, rather than recarving eyes twice.
    mourning = by_id[P + "epilogue.bench_mourned"]["Nodes"][0]
    mourning.setdefault("Paragraphs", []).extend((
        p('{n}The eyes were already finished. She carried the small likeness to the grave without cutting it again, then brought it home to her bench. Nobody else would have that face.{/n}', requires=(LIKENESS_DONE,)),
        p('{n}The sitter would not return. She finished the waiting eyes from memory, sat with the likeness through the night, and kept it beside her cup.{/n}', requires=(LIKENESS,), forbids=(LIKENESS_DONE,)),
        p('{n}They had never settled how she would finish the face. She made the last cuts when she could bear to touch it again, and kept it in her own corner of the yard.{/n}', forbids=(LIKENESS, LIKENESS_DONE)),
        p('{n}No more purses had passed between them. The last coin lay beside the paid birch, far from her private likeness.{/n}', forbids=(HANDS,)),
        p('{n}The three-day sitting had been kept. She set the wooden hands beside the face; the likeness belonged to the afternoons she had chosen.{/n}', requires=(HANDS,)),
    ))
    living = by_id[P + "epilogue.bench"]["Nodes"][0]
    living.setdefault("Paragraphs", []).extend((
        p('{n}The Commander sat again, and she finished the waiting eyes by touch. On later visits the face stood beside her cup, finished and hers.{/n}', requires=(LIKENESS,), forbids=(LIKENESS_DONE,)),
        p('{n}The finished grave-post never went to a grave. She kept it beside her cup and complained that its living owner would not keep the same expression.{/n}', requires=(LIKENESS_DONE,)),
    ))
    # Every independent destination follows the clan state; her return does not resurrect Wintersun.
    for suffix in ("unvisited", "finished", "refusal", "commit_mourned"):
        s = by_id[P + "epilogue." + suffix]
        s["Nodes"][0].setdefault("Paragraphs", []).extend((
            p('{n}With the clan dead, she went north to find another Sarkorian settlement. She carried her chisels; Drezen kept the finished work.{/n}', requires=(CLAN_DESTROYED,)),
            p('{n}She went north to find the surviving Wintersun carvers, with good Drezen chisels and work of her own to show them.{/n}', forbids=(CLAN_DESTROYED,)),
        ))
    # Authored job-2 sacrifice conclusions carry the same clan destinations.
    for suffix in ("unvisited_mourned", "refusal_mourned", "finished_mourned"):
        s = by_id[P + "epilogue." + suffix]
        s["Nodes"][0]["Paragraphs"].extend((
            p('{n}With the clan dead, she went north to find another Sarkorian settlement. She carried her chisels; Drezen kept the finished work.{/n}', requires=(CLAN_DESTROYED,)),
            p('{n}She went north to find the surviving Wintersun carvers, with good Drezen chisels and work of her own to show them.{/n}', forbids=(CLAN_DESTROYED,)),
        ))

    # Continuing living codas show a real return appropriate to the chosen relationship.
    for sid, text in (
        ("gesmerha.ending_living_reunion", '{n}When the road finally brought the Commander to her new bench, she set out the game they had carried from Wintersun. This time nobody asked them for a clan report before the first move.{/n}'),
        ("gesmerha.late_ending_lovers", '{n}One autumn the Commander found her with the small private likeness beside her cup. She wrapped the knife, felt the familiar face, and kissed it. Supper went cold while she led the way to bed. In the morning she returned to the cut she had left waiting.{/n}'),
        ("gesmerha.late_ending_friends", '{n}On the next visit she laid the pieces out on the old playing rows and reminded the Commander of the outer-row rule. The second game lasted through supper.{/n}'),
        ("gesmerha.late_ending_open", '{n}The Commander returned with the unflattering story she had requested. She laughed, moved her cup to make room, and asked for the parts still being left out.{/n}'),
    ):
        by_id[sid]["Nodes"][0]["Text"] += "\n" + text


# Authored job-2 commission conclusions; sacrifice grants no reconciliation.
MOURNING_STATUE_PARAGRAPHS = tuple({**paragraph, "Text": paragraph["Text"].replace(
    "The surviving carvers never mentioned the memorial fire to the Commander again.",
    "The surviving carvers remembered the coin sent to the memorial fire.")}
    for paragraph in STATUE_PARAGRAPHS)
page("unvisited_mourned", "The work that remained",
     '{n}News of Threshold reached Gesmerha before the Commander ever entered the yard. '
     'She finished the paid birch alone and put the coin beside it. She had known a patron, '
     'not a lover. With the work done, she took her hands out of the cold water and chose another piece.{/n}',
     requires=("trickster.ever", RETURNED, "sacrifice"),
     forbids=("trickster.commander_back", YARD, PRESENCE_FAILED, COMMITTED, CLOSED, DECLINED),
     paragraphs=MOURNING_STATUE_PARAGRAPHS)
page("refusal_mourned", "Paid for, without a promise",
     '{n}The Commander died at Threshold. Gesmerha finished the paid birch and gave the '
     'journeyman directions for its delivery. The answer at her bench had been no. She '
     'wrapped her tools and began work of her own; she carved no private likeness.{/n}',
     requires=("trickster.ever", RETURNED, DECLINED, "sacrifice"),
     forbids=("trickster.commander_back", COMMITTED, CLOSED), paragraphs=MOURNING_STATUE_PARAGRAPHS)
page("finished_mourned", "The commission ended",
     '{n}Gesmerha heard of Threshold after the Commander had ended their meetings. She '
     'finished the paid work and left delivery to the smith. She kept the distance she '
     'had been asked to keep, wrapped her chisels and chose another bench.{/n}',
     requires=("trickster.ever", RETURNED, CLOSED, "sacrifice"),
     forbids=("trickster.commander_back", COMMITTED), paragraphs=MOURNING_STATUE_PARAGRAPHS)
