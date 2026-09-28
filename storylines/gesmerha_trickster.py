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
SLOW = P + "cost.campaign_slow"
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
    "gesmerha.presence": dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=SMITH, Side="left", Distance=2.5),
                              Requires=["trickster.ever", RETURNED], Forbids=[CLOSED, COMMITTED],
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
    nar("pyre", '''{n}A Wintersun boy finds your camp at noon, out of breath and trying not to look at anyone. The carvers have laid Gesmerha out on their own ground, among the statues she tended, with her chisels crossed on her breast and her own knife taken away. They light her pyre at dusk.{/n}
{n}Her apprentices sent him, he says, reciting it. She spoke of you before the chief took her: the stranger who asked the questions nobody else would. They are putting on her fire whatever each of them owed her, so that she does not go to her ancestors short, and they want to know whether you owed her anything.{/n}
{n}Her uncut block is still on her bench, he says. Nobody has dared move it.{/n}''',
        c('[Send a purse for the fire, and a coin to drive into her uncut block, and have both laid beside her] "Tell her the statue\'s not finished, carver. Nobody leaves work on the bench."',
          mythic="Trickster", crusade=("Finances", -300), alignment=("Chaotic", 1), flags=(PRIMED, LATE, LAUGHED)),
        c('"I owed her nothing. Let them burn her. She chose it."', flags=(CLOSED,))),
    ], requires=("trickster", LATCH), forbids=(PRIMED, RETURNED, CLOSED), delay=24, last=3, Relationship="gesmerha",
    Chapters=[3], Remote=True, TricksterDevice=True, TricksterState="dead"))

# 4c. The payoff: a letter carried by the same boy. She is at the Lady's statue in Wintersun; nobody walks into the camp.
SCENES.append(scene(P + "dead.unfinished_work", "Splinters", "Gesmerha", 3, "", [
    nar("start", "{n}A runner at the edge of camp: the same Wintersun boy, thinner than before, with ash still in the seams of his boots. He asks for you by name this time.{/n}",
        c("Continue", "late", requires=(LATE,)),
        c("Continue", "paid", forbids=(LATE,))),
    nar("late", '''{n}They laid the block beside her as you asked, he says, with your coin driven into the grain. The fire went round it the way water goes round a stone, and round her with it. Three torches, and then the carvers stopped trying. On the third dawn Gesmerha got off the pyre by herself, her palms full of splinters, the block under her arm. The carvers pushed her away from the ground with poles, not hands. She is at the Lady's statue now, and they will not have her back among the houses. She sent him with this, word for word.{/n}
"Tell the stranger: you threw coin on my fire and a joke after it. The wood would not take either one."''',
        c("Continue", "terms_raised")),
    nar("paid", '''{n}He will not stop looking at you while he tells it. Her apprentices laid her out with the birch block from her bench under her hands, the one with your coin in it, because nobody could get the coin out. On the third morning, before anyone had lit a torch, Gesmerha sat up with her palms full of splinters and the block still in her grip. Half the carvers ran. The ones who stayed will not have her back among the houses. She is at the Lady's statue. She sent him with this, word for word.{/n}
"Tell the stranger: you heard me say *hands*, in my own yard, among my own statues, and the next thing you did was pay for them. I swore I would never shame my ancestors. You knew that too, didn't you."''',
        c("Continue", "terms")),
    g("terms", '''"The ancestors came for me in the old tongue. I will not pretend I understood all of it; the dead are not tidy talkers. I understood this much. There was paid work on my bench, with your coin in its heart, and my line does not come home with work on the bench. So they sent me back to it.
*Finish, daughter.* That is what they said. My hands are theirs until the last cut. If I put the chisel down for anything else, they take the hands back, and me with them. What they want with the finished thing, they did not say. I did not ask. You do not ask the dead for reasons."
"What is the world coming to, stranger, when the dead cannot even stay dead in peace?"''',
        c("Continue", "answer")),
    g("terms_raised", '''"The ancestors came for me in the old tongue, and they were angry. I did not need every word for that. You paid for my work over my ashes, not before them, and the dead do not like a bargain struck at their own fire.
*Finish, daughter.* My hands are theirs until the last cut, and because I was bought late there is more to cut: the journeymen's pretty Lady comes down first, by my hands, before anything new goes into the wood. If I put the chisel down for anything else, they take the hands back, and me with them. They did not say why. I did not ask."''',
        c("Continue", "answer")),
    nar("answer", "{n}The boy waits for your answer. He has plainly been told to remember it exactly, and to bring it back whatever it is.{/n}",
        c('[Send for her] "Tell her to bring her chisels to Drezen. The smith there makes better ones than the ones she lost, and I want to see the work."',
          flags=(RETURNED, DEBT, STARTED)),
        c('"Tell her to rest. Tell her ancestors they can have her back."', flags=(CLOSED,))),
    ], requires=("trickster.ever", PRIMED, LATCH), forbids=(RETURNED, CLOSED), delay=72, last=5,
    Relationship="gesmerha", Chapters=[3, 5], Remote=True, TricksterDevice=True, TricksterState="dead"))

# 4d. The middle beat and her test, in person, 24 hours after she is sent for.
in_yard(P + "returned.yard", "The smith's yard", '"Gesmerha."', [
    g("start", '''{n}Gesmerha has taken the corner of the smith's yard farthest from the forge: a log on two trestles, a roll of new chisels, a bucket of water for her palms. The splinters are out. The marks they left are not. The smith has given up arguing with her.{/n}
"Your step, stranger. I would know it in a crowd now. Paid-for hands work slower than free ones; they keep stopping to ask whose they are."
"The ancestors want it finished. They did not say *what*. So you tell me: what am I carving?"''',
        c('"Carve the monster. Let them see what Wintersun worshipped."', "hold", flags=(STATUE_TRUE,)),
        c('"Carve something new. Not the Lady. You."', "hold", forbids=(LATE,), flags=(STATUE_NEW,)),
        c('"Carve something new. Not the Lady. You."', "lie_first", requires=(LATE,))),
    g("lie_first", '''"No. You bought me over ashes, and the price was the lie first. The monster comes out of this wood before anything of mine goes in. Then we will see what is left of the log, and of me."''',
        c("Continue", "hold", flags=(STATUE_TRUE,))),
    g("hold", '''{n}She sets the chisel against the log, then takes your hands one at a time and lays them flat on the wood, either side of the blade, close enough that you can feel the steel's cold through the bark.{/n}
"Hold it. Don't move. I cut by sound, and I cannot hear your fingers."''',
        c("[Hold still]", "after", flags=(HELD,)),
        c("[Pull your hands away]", "pulled", flags=(FLINCHED,))),
    nar("pulled", '''{n}Your hands come off the wood before the mallet falls. It falls anyway, on the steel, where your left thumb was. Gesmerha does not stop the stroke and does not say anything about it. She moves the log with her own knee and cuts on.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}The mallet comes down four times. A curl of wood lands on your boot. She runs her palm over the cut, reading it.{/n}
"There. Something is looking out of it already."''',
        c('"And when it\'s finished?"', "not_yet"),
        c("[Leave her to the wood]", flags=(YARD,))),
    g("not_yet", '''{n}Her hands stop. For a moment she is listening to something that is not in the yard.{/n}
"Finish first. Then ask me what comes after. They are listening, stranger, and they have my hands."''',
        c("[Leave her to the wood]", flags=(YARD,))),
    ], requires=("trickster.ever", RETURNED), forbids=(YARD, CLOSED), delay=24)

# The commit night (heat up to the cut; the cut lands at the start of the act) and the morning after.
NIGHT = '''{n}She dries her hands on her apron, slowly, and holds them out to you palm up, as she does to a new block.{/n}
"Two things in this yard I have cut without eyes. The original I have not touched yet. Stand still. You are good at that now."
{n}Her fingers find your jaw first, then the corners of your mouth, then a scar you had forgotten you owned, reading you the way she reads grain: pressing where it gives, lingering where it resists. At your collar she unlaces you by feel and lays her palm flat over your heart to count it.{/n}
"Fast. Good. I have wanted this since your step first came through that gate, and I will not be the only one who wanted it."
{n}She kisses you the way she tests an edge, once, lightly; then again, harder, as if it had passed. Her hands go on reading, lower and surer. She draws you down onto the bench by your belt, into the shavings, and her hair falls around you both like a curtain.{/n}'''
MORNING = '''{n}Morning. There is sawdust in your hair and a curl of pine in your collar. Gesmerha is already at the trestles, bare-armed in the cold, and on a new block in front of her a face is coming out of the wood: one you have seen in mirrors.{/n}
"My hands remembered. Nobody paid them for last night, so what they make of it is mine. I will not sell it." {n}The corner of her mouth moves; she does not stop cutting.{/n} "Go and fight your war, stranger. Walk loudly when you come back. I like to hear it from the gate."'''

in_yard(P + "returned.bench", "What comes after", '"You said to ask you when it was finished."', [
    nar("start", '''{n}Late. The forge is banked and the yard is dark except for a lamp she does not need and has lit for you.{/n}''',
        c("Continue", "monster", requires=(STATUE_TRUE,)),
        c("Continue", "new", requires=(STATUE_NEW,))),
    g("monster", '''{n}The thing on the trestles is not a Lady of anything. It has too many joints and a smile that goes on past where a smile should stop. The smith will not stand near it, and has hung a sack over it twice; twice she has taken the sack off.{/n}
"Put your hand here. That is what we prayed to. My chisel knew it before any of us did."
{n}She lets out a long breath and puts the mallet down, and nothing takes it from her.{/n} "It is finished. My hands are mine again."''',
        c("Continue", "ask")),
    g("new", '''{n}The figure on the trestles is a woman with her head tipped back, listening. There are no eyes in it. There is no need of them.{/n}
"Put your hand here. You wanted *me*. That is what I sound like."
{n}She lets out a long breath and puts the mallet down, and nothing takes it from her.{/n} "It is finished. My hands are mine again."''',
        c("Continue", "ask")),
    g("ask", '''"The ancestors said *finish*. They did not say what comes after. I have been deciding, with my hands in cold water, and I will tell you what I decided when you ask."''',
        c('[Stay at the bench] "Then let me be what comes after."', "terms", forbids=(FLINCHED,)),
        c('[Stay at the bench] "Then let me be what comes after."', "flinch", requires=(FLINCHED,)),
        c('"Finish your life without me, carver. You\'ve earned it."', flags=(CLOSED,))),
    g("terms", '''"Then hear my terms, because my hands are mine again and that means they can refuse. I will not be paid for this. Not in coin, and not in jokes. If you ever buy me again, stranger, I will know it by your step before you open your mouth, and I will not be here when you do."''',
        c('"No more purses. Not for you. I swear it."', "night", flags=(COMMITTED,)),
        c('"I can\'t swear that. Buying things is what I do."', "postpone")),
    g("postpone", '''"Then you are honest, which is worse. Go. Come back when you have thought about what you would have to stop being. The bench will still be here. So will I, probably."''',
        c("[Go]", flags=(DECLINED,))),
    g("flinch", '''"You pulled your hands away in this yard, stranger. I heard it; I cut by sound. The mallet came down on nothing, where your thumb had been. I cannot carve beside someone who flinches, and I cannot lie down beside one either. Ask me again when you won't."''',
        c("[Go]", flags=(DECLINED,))),
    g("night", NIGHT, c("Continue", "morning")),
    g("morning", MORNING, c("[Go]")),
    ], requires=("trickster.ever", RETURNED, YARD), forbids=(COMMITTED, CLOSED, DECLINED), delay=72)

# 4f. The one priced second ask after her soft no. Not coin: she has forbidden purses. Three days of the Commander's war.
in_yard(P + "returned.second_ask", "A pair that were never for sale", '"About what comes after."', [
    g("start", '''{n}She is waiting for you this time, a fresh log on the trestles and nothing yet cut.{/n}
"The second asking costs more. That is fair; I learned it from you. Give me your hands. Three days, here, in the yard, while I carve them. Every hour you sit still, your war waits. Then I will have a pair that were never for sale, and you can have mine."''',
        c("Continue", "price", forbids=(FLINCHED,)),
        c("Continue", "price_flinched", requires=(FLINCHED,))),
    g("price_flinched", '''"And you will not pull them away. Three days of it. If you can do that, you can lie still for anything."''',
        c("Continue", "price")),
    g("price", '''{n}She holds out her open palms and waits.{/n}''',
        c("[Sit for her for three days]", "sat", crusade=("Favors", -100), flags=(COMMITTED, HANDS)),
        c('"Not like this."', flags=(CLOSED,))),
    nar("sat", '''{n}Three days. Couriers come to the yard gate and are sent away by the smith, who has decided which side he is on. Your hands ache, then stop aching, then stop feeling like yours. On the third evening she sets down the knife, runs her fingertips over the wooden pair and then over your real ones, back and forth, comparing, until she is satisfied with both.{/n}''',
        c("Continue", "night")),
    g("night", NIGHT, c("Continue", "morning")),
    g("morning", MORNING, c("[Go]")),
    ], requires=("trickster.ever", RETURNED, DECLINED), forbids=(COMMITTED, CLOSED), delay=96)


# --- State 2, the missed window: wrong footsteps (F04, claimed, not implanted) ----------------------------------------------

def footsteps(suffix, lists, areas, extra):
    SCENES.append(scene(P + "missed.wrong_footsteps_" + suffix, "Wrong footsteps", "Gesmerha", 5,
        '[Claim the unfinished game] "You know my step, carver. Ten afternoons at your board, and a game we never finished."', [
        g("start", '''{n}Her hands stop on the wood. She tilts her head toward your feet, the way she listens for a crack in the grain.{/n}
"I know this step. I heard it once, in Wintersun, when I did not know it at all. Once, stranger. Not ten times. You are lying, and you are doing it to a blind woman who can hear you do it."
"But you say it like someone who believes it. So sit. I cut half the squares of a board I never finished. If we played ten afternoons, you know the rule I changed. Play, and I will hear the lie in your hands the way I heard it in your feet."''',
            c("[Sit down and play as if you remember]", "game"),
            c('"All right. It was a lie. I wanted a reason to sit here."', "honest"),
            c('"Never mind."', abort=True)),
        g("game", '''{n}You play. On the fourth move your hand goes to a square before she has named the rule, and her fingers close on your wrist.{/n}
"There. You knew that. Nobody knows that; I have not told it to anyone." {n}She lets go slowly.{/n} "I don't believe your ten afternoons. I believe you will come back to lose the eleventh. The loser pays for the pieces, Commander. Count them."''',
            c("[Pay for the pieces]", crusade=("Finances", -50), alignment=("Chaotic", 1), flags=("gesmerha.campaign_kept", CATCHUP, SLOW))),
        g("honest", '''"Then you have one. Honest liars pay for the pieces too. Sit."''',
            c("[Sit down]", flags=("gesmerha.campaign_kept", CATCHUP))),
        ], requires=("trickster", "trickster.ever", "gesmerha.wintersun_resolved", "gesmerha.met", *extra),
        forbids=("gesmerha.campaign_kept", DEAD, CLOSED, CATCHUP, "inhuman"), delay=0, last=5, Relationship="gesmerha",
        Chapters=[5], RequiresAny=["gesmerha.truth", "gesmerha.illusions"], AnswerLists=lists, ContactUnit=UNIT,
        Areas=areas, EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="missed"))


footsteps("home", [HOME_LIST], [WINTERSUN], ())
footsteps("capital", [CAPITAL_LIST], [DREZEN], ("gesmerha.capital_guest",))


# --- Epilogue pages (no mythic, alignment or crusade effects) ---------------------------------------------------------

STATUE_PARAGRAPHS = (
    p("The thing with too many joints stood in the smith's yard until the spring, when the Wintersun survivors asked for it "
      "back. They set it up where the Lady's statue had been, so that nobody would forget what they had knelt to.",
      requires=(STATUE_TRUE,)),
    p("The listening woman went nowhere. The smith kept her by his gate, and swore that she turned her head a little toward "
      "anyone who came in walking loudly.", requires=(STATUE_NEW,)),
    p("She kept the wooden hands on a shelf by her bed, palms up. She said they were the only pair in Drezen that had never "
      "been bought.", requires=(HANDS,)),
    p("Nobody in Wintersun ever spoke to the Commander about the pyre. Some debts, the carvers said, are paid by never being "
      "mentioned.", requires=(LAUGHED,)),
)


def page(id, title, text, requires, forbids, paragraphs=(), **extra):
    SCENES.append(scene(P + "epilogue." + id, title, "Epilogue", 1, "", [nar("start", text, c(), paragraphs=paragraphs)],
                        requires=requires, forbids=forbids, last=99, Relationship="gesmerha", **extra))


page("bench", "What came after", '''{n}Gesmerha never carved on commission again. She kept the corner of the smith's yard for as long as the war lasted and a good while after, and it became the corner of the city where people came to have the truth cut out of wood for them, whether they liked it or not.{/n}
{n}The Commander kept the oath about purses, which surprised everyone who knew the Commander. She could tell the Commander's step from anyone's, in any crowd, and she let it be known that she always heard it a long time before it reached the door.{/n}''',
     requires=(RETURNED, COMMITTED), forbids=(CLOSED,), paragraphs=STATUE_PARAGRAPHS)

page("commit", "The Commander's door", '''{n}Gesmerha finished the Commander's carving in the spring after Threshold, in a borrowed corner of a Drezen smithy, and then she walked the width of the city by ear to find out what came after. The smith swore she stopped at the Commander's door and listened for a long time before she knocked. She never said what she decided. She never carved on commission again.{/n}''',
     requires=("trickster.ever", RETURNED), forbids=(COMMITTED, CLOSED, DECLINED), paragraphs=STATUE_PARAGRAPHS,
     RequiresAnyGroups=[[YARD, PRESENCE_FAILED]])

page("unvisited", "The corner of the yard", '''{n}Gesmerha finished the carving her ancestors had sold her back for, alone, in a corner of a Drezen smith's yard that the Commander never once walked into. When it was done she put her hands in cold water for a long time, and then she took them out and went home to whatever was left of Wintersun. The smith said she stopped at the gate and listened, as if for a step, and then went on.{/n}''',
     requires=("trickster.ever", RETURNED), forbids=(YARD, PRESENCE_FAILED, COMMITTED, CLOSED, DECLINED),
     paragraphs=STATUE_PARAGRAPHS)

page("refusal", "Paid for", '''{n}Gesmerha finished the carving and left it in the smith's yard with a note in a journeyman's hand: *Paid for. Collect it.* The Commander never swore off buying things. She never asked a third time.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), paragraphs=STATUE_PARAGRAPHS)

page("finished", "Her own life", '''{n}Gesmerha finished the work she had been paid for, as her ancestors required, and then she finished her life as the Commander had told her to: without the Commander. She went north after the Wintersun survivors with a roll of good Drezen chisels and a bag of her own shavings, and did not send word back.{/n}''',
     requires=("trickster.ever", RETURNED, CLOSED), forbids=(COMMITTED,), paragraphs=STATUE_PARAGRAPHS)


# --- Reactions (exactly Ulbrig, Lann and Anevia) ----------------------------------------------------------------------

LANN = dict(requires=("lann.in_party",), forbids=("lann.dead", "lann.kicked_out"))
ULBRIG = dict(requires=("ulbrig.in_party",), forbids=("ulbrig.dead", "ulbrig.kicked_out"))

REACTIONS = [
    reaction("Lann", P + "react.lann_pyre", (LAUGHED, *LANN["requires"]),
             '''"You sent a joke to a funeral. In Sarkoris. The boy who carried it looked like he wanted to be sick." {n}Lann scratches the back of his neck.{/n} "What did it say? No. Don't tell me. I'll hear about it anyway."''',
             answer_list=LANN_HUB, forbids=LANN["forbids"], chapter=3, last=3, delay=24, entry='"About the carver\'s pyre..."'),
    reaction("Ulbrig", P + "react.ulbrig_return", (RETURNED, *ULBRIG["requires"]),
             '''"A Wintersun carver got up off the carvers' ground, they're saying, and went straight back to work." {n}Ulbrig sets his mug down, which he does not do lightly.{/n} "Where I come from, the dead don't come back for love. They come back for unfinished business, and they don't leave till it's done. Pray she finishes slow, warchief."''',
             answer_list=ULBRIG_HUB, forbids=ULBRIG["forbids"], chapter=3, last=5, delay=24, entry='"About the carver from Wintersun..."'),
    reaction("Anevia", P + "react.anevia_return", (RETURNED,),
             '''"The smith came to me about a blind woman in his yard. Won't give his corner back, won't let his boys near her log, and says you owe her the good chisels." {n}Anevia shrugs.{/n} "I told him that sounded about right."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "anevia_dead"), chapter=3, last=5, delay=24,
             entry='"About the smith\'s yard..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
    reaction("Lann", P + "react.lann_footsteps", (CATCHUP, *LANN["requires"]),
             '''"The carver says she caught you lying about ten afternoons, and then you beat her at her own game anyway." {n}Lann grins.{/n} "I've never seen you sit still for ten minutes."''',
             answer_list=LANN_HUB, forbids=LANN["forbids"], chapter=5, last=5, delay=24, entry='"About the carver..."'),
    reaction("Anevia", P + "react.anevia_footsteps", (CATCHUP,),
             '''"The carver says you two go back. Ten afternoons at her bench." {n}Anevia gives you a long look.{/n} "I keep your calendar, Commander. I'd remember ten afternoons."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "anevia_dead"), chapter=5, last=5, delay=24,
             entry='"About the carver..."', ForbidOverrides={"anevia_gone": "anevia.trickster.returned"}),
]
SCENES.extend(REACTIONS)


# --- The registered route ---------------------------------------------------------------------------------------------

# The alive chain: if she lived through the ambush with a commission paid, she carves it.
COMMISSION_PARAGRAPH = p("She carved the Commander's commission in the end, years after it was paid for: a small thing in "
                         "black oak, which she would not describe to anyone. She said a commission is a commission, and "
                         "that her line had never left paid work on the bench.", requires=(COMMISSIONED,), forbids=(RETURNED,))
BORROWED_PARAGRAPH = p("She never believed in the ten afternoons. She kept count of the real ones instead, and told the "
                       "Commander once that they had long since passed ten, and that the borrowed ones were paid back.",
                       requires=(SLOW,))
ALIVE_ENDINGS = ("gesmerha.ending_living_reunion", "gesmerha.ending_unmet_again", "gesmerha.late_ending_lovers",
                 "gesmerha.late_ending_friends", "gesmerha.late_ending_open", "gesmerha.late_ending_closed",
                 "gesmerha.late_ending_unfinished")
LATE_LIVING = ("gesmerha.late_ending_lovers", "gesmerha.late_ending_friends", "gesmerha.late_ending_open")
LOSS_PAGES = ("gesmerha.ending_loss", "gesmerha.late_ending_loss")

# The trust step the claimed afternoons add to the registered late chain's first visit.
CATCHUP_NODE = g("catchup", '''{n}Her fingers become still against the wood.{/n}
"The eleventh game. You came back to lose it, then." {n}She does not move the blanket yet.{/n} "Before you sit, tell me one true thing about where you were all the afternoons you did not spend here. Not a pretty thing. A true one. I will hear the difference."
{n}You tell her. It takes longer than you meant it to. When you have finished she moves the folded blanket from the chest and tells you where to sit.{/n}
"There. That was the first afternoon. We will count from it."''',
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
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered."""
    rel = payload["Relationships"]["gesmerha"]
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

    # The first late visit: a Commander who only claimed the afternoons is asked for one true thing before sitting. The
    # registered "too long since our last afternoon" answer is retired for that Commander by a gate, not removed.
    first = _scene(by_id, "gesmerha.the_things_still_here")
    start = next(x for x in first["Nodes"] if x["Id"] == "start")
    without = next(ch for ch in start["Choices"] if ch.get("Next") == "without_court")
    if CATCHUP not in without["Forbids"]:
        without["Forbids"].append(CATCHUP)
    start["Choices"].append(c('"I came back to lose the eleventh game."', "catchup", requires=(CATCHUP,),
                              forbids=("gesmerha.reunion_kept",)))
    first["Nodes"].append(dict(CATCHUP_NODE, Portrait="Gesmerha"))
