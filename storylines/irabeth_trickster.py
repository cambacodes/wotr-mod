"""Irabeth on the Trickster path: relieved, not dismissed (Writer/handoffs/trickster/irabeth.md, families F04 and F19).

Canon: at Iz she reports "Your Majesty. Commander. Irabeth Tirabade... stands relieved." (IrabethDies/Cue_0001 f7d10f44) and
dies with "Anevia. Tell her I love her. Take care... of my Nevi." (Cue_0013 1f6f05c7). The native relief is Answer_0015
741681b4 "I relieve you." -> Cue_0016 dc5a8da4 "That means I can go with a clear conscience." The Trickster takes her at her
word and not one word further: relieved of duty, never dismissed, so she reports back in person. If the Commander struck her
down at Iz instead, she comes back only if she was drilled beforehand to step inside a blade (the Mobility dodge of
TricksterMobilityTier3Feature 6db3651d). Her Trickster judgment: "Your orders seem crazy sometimes, but they lead us to
victory." (Irabeth_C3_Intro/Cue_0124 2302cb7c).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"            # IrabethTirabade_DrezenCapital (IrabethDead only hides it)
HUB = "871af36f2ab2b1f40b5de77976c54276"                # NPC_Common/Irabeth/AnswersList_0009
DEATHBED = "09b65ca563cc63141aebf70b7abe7270"           # c5/Iz/IrabethDies/AnswersList_0005
DEATHBED_RETURN = "12f0d4c8dc3024a4cb86ab222ed3be66"    # Cue_0003 "Just win this war", answers -> AnswersList_0005
CLEAR_CONSCIENCE = "dc5a8da498d2cd945a50f4e6a107e6fc"   # Cue_0016, the native reply to "I relieve you."
STORYTELLER = "06184e4f0a65650488e36600d8274d26"        # c5/Drezen_Under_Siedge/StorytellerDangerousDrezen/AnswersList_0005
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"         # CompanionDialogues/Seelah/AnswersList_0003

PRIMED = "irabeth.trickster.primed"
RETURNED = "irabeth.trickster.returned"
DECLINED = "irabeth.trickster.declined"
DRILLED = "irabeth.trickster.drilled"
STANDING = "irabeth.trickster.standing_order"
LATE = "irabeth.trickster.cost.late"
UNDER_ORDERS = "irabeth.trickster.cost.under_orders"
BLOW = "irabeth.trickster.cost.remembers_the_blow"
LIED = "irabeth.trickster.cost.accounting_lied"
SIGNED = "irabeth.trickster.cost.signed_request"
BLOW_STANDS = "irabeth.trickster.blow_stands"
KILLED = "anevia.irabeth_killed_by_commander"
A_RET = "anevia.trickster.returned"
SHARES = "anevia.trickster.shares_beth"   # Anevia's own terms, said at the gate
SOUL_TORN = "irabeth.trickster.soul_wound_told"
OWN = ("irabeth.closed",)

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={"irabeth_dead": RETURNED},
    TricksterAccess={
        "dead": dict(detect=["irabeth_dead", "!" + KILLED], device="irabeth.trickster.dead.setup", returned=RETURNED),
        "killed": dict(detect=["irabeth_dead", KILLED], device="irabeth.trickster.killed.blow_missed", returned=RETURNED),
    })
PRESENCES = {
    # One presence (engine rule): the vigil before her report and her service after it, merged in presence_on.
    "irabeth.presence": dict(Unit=IRABETH, Area=DREZEN, Mode="reuse-native",
                             Requires=["trickster.ever", "irabeth.trickster.presence_on"],
                             Forbids=["irabeth.closed", BLOW_STANDS], MinChapter=5, MaxChapter=5, AnswerLists=[HUB]),
}
SEEN_CUES = {
    # IrabethDies Cue_0020 / Cue_0021 (after "Isn't there some way to help you?"): "it's ripping apart my soul".
    SOUL_TORN: ["056e1df95bf941243b31265a46c05e1d", "a207da6cc9abfeb4190ab9600b8d9aed"],
    # IrabethDies Cue_0019a: Seelah's prayer at the deathbed.
    "irabeth.trickster.seelah_prayed": ["be7fbe9847c4a944fafc750ee5aed807"],
}


def physical(id, title, entry, nodes, requires, forbids, delay, chapters=(5,), **extra):
    SCENES.append(scene(id, title, "Irabeth", min(chapters), entry, nodes, requires=requires, forbids=(*OWN, *forbids),
                        delay=delay, last=max(chapters), optional=True, Relationship="irabeth", Areas=[DREZEN],
                        Chapters=list(chapters), ContactUnit=IRABETH, AnswerLists=[HUB], **extra))


def letter(id, title, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Irabeth", 5, "", nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="irabeth", Chapters=[5], Remote=True, **extra))


def i(id, text, *choices):
    return n(id, "Irabeth", text, *choices, portrait="Irabeth")


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices, portrait="Irabeth")


# --- Primers, planted while she lives ------------------------------------------------------------------------------

# Directive 9 foresight: the Storyteller has just said "The Queen is in mortal danger, at the crossroads of her fate, and
# her every step may prove fatal." (Cue_0024 fa01a4a4). Non-inline: every cue on this list has a Continue.
SCENES.append(scene("irabeth.trickster.dead.standing_order", "A standing order", "Irabeth", 5,
    '"When we reach the Queen, you\'ll stand in front of her. I know you. Fine. Afterwards you report to me. In person. '
    'That order doesn\'t lapse until I sign it off."', [
    i("start", '''"In person."
{n}Irabeth does not look at the Storyteller. She looks at you, the way she looks at a dispatch she suspects of carrying a second meaning.{/n}
"Commander, I always report in person. You know that. Why say it now?"''',
      c('[Hold her gaze] "In person."', "roster")),
    i("roster", '''"That isn't an order a knight can promise to keep."
{n}Her eyes go to the old elf, then back to you. Her jaw sets.{/n}
"But it's an order. Understood. It goes in the duty roster tonight, in my hand, so nobody can say you made it up afterwards. And if you're planning something, Commander, I'd rather you planned it where I can see."''',
      c('[Let her write it into the roster] "Your hand. Your roster. I\'ll sign it off when I sign it off."', flags=(STANDING,)),
      c('"Forget I said it."', abort=True)),
], requires=("trickster", "storyteller.asked_queen"), forbids=(*OWN, "irabeth_dead", STANDING, PRIMED), last=5,
   optional=True, Relationship="irabeth", Chapters=[5], AnswerLists=[STORYTELLER], EntryMythic="PlayerIsTrickster"))

physical("irabeth.trickster.killed.drill", "A step, not a block",
         '"Got an hour, Knight-Captain? I want to teach you something the Trickster taught me."', [
    i("start", '''"A trick. With a sword."
{n}She has her gauntlets half off already, which is how you know she means to humor you.{/n}
"I block, Commander. I've blocked for thirty years. Demons, cultists, one very determined goat. It's the one thing I'm good at that isn't paperwork."''',
      c('"Stand there. I\'m going to swing at you. Don\'t block. Step."',
        check=dict(Skill="SkillMobility", DC=20, Success="stepped", Failure="bruised", CommanderOnly=True))),
    i("stepped", '''{n}The blade goes where she was. She is half a pace to the left, inside your guard, close enough to break your wrist, and she looks as surprised as you do.{/n}
"...I didn't decide to do that."
{n}She rolls her shoulder, frowning at her own feet as if they had disobeyed an order.{/n}
"Again. If I'm going to have a bad habit, I want it drilled properly."''',
      c('"Again. Until you do it without thinking."', flags=(DRILLED, "irabeth.started"))),
    i("bruised", '''{n}She blocks on instinct. Steel rings, your feet go out from under you, and you both end up on the flagstones.{/n}
"Thirty years, Commander."
{n}She offers you a hand up and does not let go of it quite at once.{/n}
"Come back when you've got thirty more. Or tomorrow. Tomorrow would do."''',
      c('"Tomorrow, then."', abort=True)),
], requires=("trickster",), forbids=("irabeth_dead", KILLED, DRILLED, "irabeth_away"), delay=0, chapters=(3, 5),
   EntryMythic="PlayerIsTrickster")


# --- State dead_at_iz: relieved, not dismissed ---------------------------------------------------------------------

# Inline at the deathbed: a sibling of "I relieve you." after her report "Irabeth Tirabade... stands relieved."
SCENES.append(scene("irabeth.trickster.dead.setup", "Relieved", "Irabeth", 5,
    '"Relieved of duty, Knight-Captain. Not dismissed. You still have my order: take care of your Nevi."', [
    n("start", "Irabeth", '''{n}Her hand has already started the salute. It stops halfway, because you are not returning it.{/n}
"Relieved..."
{n}She says the word the way she reads an order: twice, to be sure of it. Her eyes are going somewhere past your shoulder, and you cannot tell whether she heard the rest.{/n}''',
      c('[Refuse her salute] "Not dismissed, Irabeth. You hear me? Not dismissed."', native_next=CLEAR_CONSCIENCE,
        alignment=("Chaotic", 1), flags=(PRIMED, "irabeth.started"))),
], requires=("trickster", "irabeth.deathbed"), forbids=(*OWN, PRIMED), last=5, optional=True,
   Relationship="irabeth", Chapters=[5], AnswerLists=[DEATHBED], NativeReturnCue=DEATHBED_RETURN,
   EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="dead"))

letter("irabeth.trickster.dead.late_order", "An empty bunk", [
    nar("start", '''{n}Her bunk in the barracks has been stripped to the ropes. Someone has set her boots under it anyway, toes to the wall, the way she always left them.{/n}
{n}The knights on watch have a bottle between them and are not drinking it.{/n}''',
      c("Continue", "roster", requires=(STANDING,)),
      c("Continue", "alone", requires=("iz.left_early",), forbids=(STANDING,)),
      c("Continue", "cup", forbids=(STANDING, "iz.left_early"))),
    nar("roster", '''{n}The duty roster hangs on its nail by the door. Under her name, in her own square hand, is the order you gave her in the siege: "To report to the Commander in person. Not to be struck off except by the Commander."{/n}
{n}Nobody has struck it off. Nobody has dared.{/n}''', c("Continue", "cup")),
    nar("alone", '''{n}Nobody was with her at the end. The report from Iz lists her among the dead in the same clerk's hand as the quartermaster's losses, between a broken wagon axle and forty spears.{/n}''',
      c("Continue", "cup")),
    nar("cup", '''{n}One of the knights holds out the bottle to you without a word. The chaplain on duty watches from the doorway, his hands folded over his book.{/n}''',
      c('[Raise a cup to the empty bunk] "Knight-Captain Irabeth: absent without leave. Report at dawn."', "toast",
        mythic="Trickster", alignment=("Chaotic", 1), crusade=("Favors", -150),
        flags=(PRIMED, LATE, "irabeth.started")),
      c('[Let her rest] "...No. She earned it."', "rest", flags=(DECLINED,))),
    nar("toast", '''{n}The knights stare at you. Then one of them, very slowly, answers for her: "Present." Another laughs, badly, and stops.{/n}
{n}The chaplain sets down his cup untouched and writes something in his own ledger. By morning the whole citadel has heard that the Commander took a roll call of the dead as a joke. The priests of Iomedae will not forget it soon.{/n}''',
      c('"Dawn, Knight-Captain."')),
    nar("rest", '''{n}You drink. The knights drink. Nobody says anything clever, and the boots stay under the bunk until morning, when the quartermaster takes them away.{/n}''',
      c('"Goodbye, Irabeth."')),
], requires=("trickster", "irabeth_dead", "irabeth.dead.latched"), forbids=(PRIMED, RETURNED, DECLINED, KILLED), delay=24,
   TricksterDevice=True, TricksterState="dead")

physical("irabeth.trickster.dead.relieved_not_dismissed", "Reporting in person", '"Knight-Captain?"', [
    nar("start", '''{n}The clerk strikes her name from the duty roster at dusk. At dawn it is back, in a square, patient hand, under "On watch". He strikes it again. It comes back again, underlined.{/n}
{n}On the third night the knight keeping vigil over her body finds the bier empty and the burial whites gone. The Knight-Captain is in the throne room, at attention before your chair, waiting to report.{/n}''',
      c("Continue", "report")),
    i("report", '''"Knight-Captain Tirabade, reporting in person. As ordered."
{n}Her voice is hoarse, and very irritated. The burial whites are belted over her arming coat. Her sword is in her hand.{/n}
"The chaplain says I was dead two days. The chaplain also says my discharge was 'misplaced'. I have never misplaced a form in my life, Commander."''',
      c("Continue", "torn", requires=(SOUL_TORN,)),
      c("Continue", "standing", requires=(STANDING,), forbids=(SOUL_TORN,)),
      c("Continue", "toasted", requires=(LATE,), forbids=(SOUL_TORN, STANDING)),
      c("Continue", "discharge", forbids=(SOUL_TORN, STANDING, LATE))),
    i("torn", '''"That dragon's magic went through my soul like a saw. I told you so at Iz. I felt it come apart."
{n}She flexes her sword hand. The knuckles are white.{/n}
"It's held together now. With your order. I can feel exactly where the stitches are."''',
      c("Continue", "standing", requires=(STANDING,)),
      c("Continue", "toasted", requires=(LATE,), forbids=(STANDING,)),
      c("Continue", "discharge", forbids=(STANDING, LATE))),
    i("standing", '''"I wrote that order into the roster myself. 'In person.' I thought you were being sentimental. You were being a lawyer."''',
      c("Continue", "toasted", requires=(LATE,)), c("Continue", "discharge", forbids=(LATE,))),
    i("toasted", '''"And somebody toasted my empty bunk and called it a roll call. The chaplains are still complaining. I'd complain too, if I weren't standing here."''',
      c("Continue", "discharge")),
    nar("discharge", '''{n}She holds out her hand, palm up, for the paper that would let her go. She does not look at it. She looks at you.{/n}''',
      c('[Hold out the unsigned discharge] "Your discharge needs my signature. I\'ve misplaced my pen. For two days."',
        "answer", forbids=(LATE,), flags=(RETURNED, "irabeth.started", UNDER_ORDERS)),
      c('[Hold out the unsigned discharge] "Your discharge needs my signature. I\'ve misplaced my pen. I\'m still looking."',
        "answer", requires=(LATE,), flags=(RETURNED, "irabeth.started", UNDER_ORDERS))),
    i("answer", '''{n}Her jaw works.{/n}
"...Crazy orders. Every time. And every time we win."
{n}She does not smile.{/n}
"Don't you ever do that to me again, Commander. Not to me, and not to her. Now tell me where Nevi is."''',
      c('"She left at the Coronation. South, I think."', "south", requires=("anevia_gone",), forbids=(A_RET,)),
      c('"Here. In Drezen. She never left."', "home", forbids=("anevia_gone",)),
      c('"At the gate. Outside the walls. She won\'t come in."', "gate", requires=("anevia_gone", A_RET))),
    nar("south", '''{n}She hears it standing at attention, and she stays that way a long moment after you have finished.{/n}
"South. Of course south. She never could sit in a house with a draught in it."
{n}She is gone before noon on a borrowed horse, riding south after her wife with the sword still in her hand. She does not say when she will be back, and nobody is fool enough to ask.{/n}''',
      c('"Welcome back, Knight-Captain."')),
    nar("home", '''{n}She is out of the throne room before you finish the sentence, burial whites and all, with the sword in her hand because she cannot put it down.{/n}
{n}Nobody in the citadel sees that meeting. The guard at the stair reports only that the Knight-Captain's wife said one word, loudly, and that it was not a word for a chapel.{/n}''',
      c('"Welcome back, Knight-Captain."')),
    nar("gate", '''{n}She doesn't ride anywhere. Anevia is at the gate, on the road side of the line the cartwheels have worn into the mud. Irabeth walks out to her in her burial whites, without her helmet, holding the sword she cannot put down well out to one side.{/n}
{n}The watch on the gate finds something very interesting to look at in the other direction, and goes on looking at it for some time.{/n}''',
      c('"Welcome back, Knight-Captain."')),
], requires=("trickster.ever", "irabeth_dead", PRIMED, "coronation.seen"), forbids=(RETURNED, KILLED), delay=24,
   TricksterDevice=True, TricksterState="dead")


# --- State killed_by_commander: the step she learned ---------------------------------------------------------------

letter("irabeth.trickster.killed.late_step", "The report of the day", [
    nar("start", '''{n}The chaplain who came back from Iz is writing the report of the day by candlelight. He has written "Knight-Captain Irabeth Tirabade, slain by" and stopped.{/n}
{n}He is looking at you. So is the knight holding the candle.{/n}''',
      c('[Dictate the step] "Write it down. I swung. She stepped. Everyone saw her step."', "lie", mythic="Trickster",
        alignment=("Chaotic", 1), crusade=("Favors", -200), flags=(DRILLED, LATE, "irabeth.started")),
      c('[Let the blow stand] "No. It happened. I did it."', "stands", flags=(DECLINED,))),
    nar("lie", '''{n}He writes it. His hand shakes on "stepped", and the word comes out crooked. When he is done he sands the page, folds it, and gives it to the knight to carry to the archive.{/n}
"I will remember the other one, Commander," he says, very quietly. "Every day. So will he."
{n}The knight with the candle does not say anything. By the end of the week the whole order has heard some version of it, and no two versions agree.{/n}''',
      c('"Remember what you like. File what I said."')),
    nar("stands", '''{n}He finishes the line in your words. He does not soften them. When he is done he looks at the page for a long time, then at you, and nods once, as if you had passed something.{/n}''',
      c('"File it."')),
], requires=("trickster", "irabeth_dead", KILLED, "irabeth.dead.latched"), forbids=(DRILLED, RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState="killed")

physical("irabeth.trickster.killed.blow_missed", "The step she learned", '"Knight-Captain?"', [
    nar("start", '''{n}She is in the throne room with her sword in her hand. There is a fresh seam in her surcoat, over the ribs, where your blade went in.{/n}
{n}The report of the day at Iz, in the archive, says the Knight-Captain stepped inside the Commander's blow, fell into the ruins and was dug out alive on the second morning.{/n}''',
      c("Continue", "shaken", requires=(LATE,)), c("Continue", "both", forbids=(LATE,))),
    nar("shaken", '''{n}The chaplain's hand shook on "stepped". You can see it from here, in the way she keeps touching the seam.{/n}''',
      c("Continue", "both")),
    i("both", '''"I remember your blade in me. I remember the cold, after. I also remember stepping, the way you taught me, half a pace left and inside."
{n}Her knuckles whiten on the hilt.{/n}
"Both are true, Commander. I hate both of them."''',
      c('[Remember it the other way] "I swung. You stepped. Everybody saw you step."', "accounting", mythic="Trickster"),
      c('[Let the blow stand] "No. I did it. I won\'t take it back."', "salute", flags=(DECLINED, BLOW_STANDS))),
    i("accounting", '''"Everybody saw what you told them to see. I know how this works now."
{n}She takes one step closer. It is a very precise step.{/n}
"So which one did you mean, Commander? The swing, or the lesson?"''',
      c('"I meant it. At Iz, I meant it. I don\'t now."', "truth",
        flags=(RETURNED, "irabeth.started", "irabeth.trickster.blow_rewritten", BLOW,
               "irabeth.trickster.accounting_truth", "irabeth.accounting_kept")),
      c('[Lie] "It was the dragon\'s sorcery. It wasn\'t me."', "lie",
        flags=(RETURNED, "irabeth.started", "irabeth.trickster.blow_rewritten", BLOW, LIED))),
    i("truth", '''{n}She takes it like a blow she saw coming. She does not step away from it.{/n}
"Good. I'd have known if you lied. I've questioned cultists who lied better than you, and I hanged them."
{n}She sheathes the sword. Her hand stays on the hilt.{/n}
"I'm back on duty. Don't mistake that for forgiveness."''',
      c('"Understood, Knight-Captain."')),
    i("lie", '''{n}Something shuts behind her eyes, the way a gate shuts.{/n}
"The dragon. Of course."
{n}She sheathes the sword, very carefully, and keeps her hand on the hilt.{/n}
"I'm back on duty, Commander. I'll serve. Don't ask me for more than that."''',
      c('"Dismissed."')),
    nar("salute", '''{n}She salutes. It is a perfect salute, the one she gives the Queen.{/n}
{n}When you look up, the throne room is empty, and the report from Iz in the archive says what it always said.{/n}''',
      c('"...Goodbye, Irabeth."')),
], requires=("trickster.ever", "irabeth_dead", KILLED, DRILLED, "coronation.seen"),
   forbids=(RETURNED, "trickster.failed", DECLINED), delay=24, TricksterDevice=True, TricksterState="killed")


# --- After the return: the test, the commit, her no ---------------------------------------------------------------

physical("irabeth.trickster.back_on_duty", "Back on duty", '"Knight-Captain. A word."', [
    nar("start", '''{n}She is at her post in the throne room as if she never left it. The sword is in her hand. It has been in her hand since she came back.{/n}''',
      c("Continue", "hymn", forbids=(BLOW,)), c("Continue", "blow", requires=(BLOW,))),
    i("hymn", '''"They sang for me, Commander. The whole hall. I'm not walking back in there to tell them they wasted a good hymn, so I'm standing here instead."''',
      c("Continue", "sword")),
    nar("blow", '''{n}She keeps the sword between you, point down, and does not pretend otherwise.{/n}''', c("Continue", "sword")),
    i("sword", '''"I can't put this down. I tried, to shave. It won't leave my hand for longer than a breath. The chaplain thinks it's a curse. I think it's a clause."
{n}She lifts it an inch: steel, and a hand that will not open.{/n}
"Until the Wound is shut, apparently. Your joke has fine print, Commander. I'd like to have read it first."''',
      c("Continue", "question"),
      c('[Offer to sign her discharge now] "Then I\'ll sign it. You\'re free."', "unsigned")),
    i("unsigned", '''"The chaplain thought of that, the first night. Sign it and I'm discharged, Commander. All the way. Back to wherever I was for those two days."
{n}She holds out her free hand for the pen anyway, palm up, perfectly steady.{/n}
"Your call. It's always been your call. That's the part I can't forgive."
{n}You do not give her the pen. After a while she lowers the hand.{/n}''',
      c("Continue", "question")),
    i("question", '''"One question, and you answer it straight. Did you do it for the crusade, or for me?"
{n}She waits.{/n}
"There's a right answer. I'm not telling you which."''',
      c('"Because the crusade needs its Knight-Captain."',
        flags=("irabeth.trickster.back_on_duty", "irabeth.trickster.answered_crusade")),
      c('"Because I needed you back. Not the crusade. Me."',
        flags=("irabeth.trickster.back_on_duty", "irabeth.trickster.answered_her"))),
], requires=("trickster.ever", RETURNED), forbids=("irabeth.trickster.back_on_duty",), delay=48)

THRESHOLD = '''{n}She tries to set the sword down on the throne-room step. Her fingers will not open. She swears at it, short and furious, and holds the blade out to the side, point to the floor, the way you would hold a torch you cannot drop.{/n}
"I've wanted this since Iz, and I've been ashamed of it since Iz. I'm done being ashamed. Take the rest off me, Commander. One-handed is all I've got. Slowly. I want to remember it."
{n}Gauntlet, then vambrace, one arm at a time around a hilt she cannot let go. Her free hand stops working on the breastplate buckles and she lets you do it. Under the arming coat she is scar and muscle and heat. She kisses you hard enough that her tusks graze your lip, then drags you through the side door into her roster room, where nobody sits at the desk but her. She sweeps the duty lists off it with her free arm. Her sword arm stays flung out over the edge, the point grinding on the flagstones, and with the other she pulls you down onto the desk with her and hooks a leg behind yours.{/n}'''

MORNING_NOTE = '''{n}The watch changes under the window. She is back in armour, all but the gauntlet that will not go on over the hilt without help. She holds that hand out to you without a word. There is a white groove across her palm where the grip lay all night.{/n}
"Nevi will know. Nevi always knows. I'll write to her myself before breakfast, before anyone else can."
{n}You buckle it for her. She flexes the hand inside the steel, around the sword, and does not thank you.{/n}
"Knight-Captain Tirabade, reporting for duty. Don't look at me like that in front of the guard."'''

MORNING_HOME = '''{n}The watch changes under the window. She is back in armour, all but the gauntlet that will not go on over the hilt without help. She holds that hand out to you without a word. There is a white groove across her palm where the grip lay all night.{/n}
"Nevi will know. Nevi always knows. She'll laugh at me. Then she'll want to know every detail. Then she'll want her turn."
{n}You buckle it for her. She flexes the hand inside the steel, around the sword, and does not thank you.{/n}
"Knight-Captain Tirabade, reporting for duty. Don't look at me like that in front of the guard."'''

physical("irabeth.trickster.commit", "Off the record", '"Knight-Captain. Off the record."', [
    i("start", '''{n}Late. The throne room is empty but for the two of you and the sword she still cannot put down.{/n}
"You're going to say something I'll have to answer. I can see it on you. Go on, then."''',
      c("Continue", "her", requires=("irabeth.trickster.answered_her",)),
      c("Continue", "crusade", requires=("irabeth.trickster.answered_crusade",))),
    i("her", '''"You said 'for me'. Nobody's said that to me since Nevi. It was the right answer. I hate that it was the right answer."''',
      c("Continue", "lied", requires=(LIED,)), c("Continue", "answer", forbids=(LIED, SHARES)),
      c("Continue", "talked", requires=(SHARES,), forbids=(LIED,))),
    i("crusade", '''"You said 'for the crusade'. Honest. A month ago I'd have thrown you out for the other one."''',
      c("Continue", "lied", requires=(LIED,)), c("Continue", "answer", forbids=(LIED, SHARES)),
      c("Continue", "talked", requires=(SHARES,), forbids=(LIED,))),
    i("lied", '''"And you lied to me about Iz. I know you did. One more and I'm gone, orders or no orders."''',
      c("Continue", "answer", forbids=(SHARES,)), c("Continue", "talked", requires=(SHARES,))),
    i("talked", '''"I asked Nevi. At the gate, her side of the line, to her face, the way she told you I'd have to. I felt like a recruit asking for leave. She said yes before I'd finished. She said, and I'm quoting, 'I'd rather share than bury.'"
{n}The tips of her ears have gone dark.{/n}
"Then she told me to stop looking at my boots."''',
      c("Continue", "answer")),
    i("answer", '''{n}She waits for you to say it. Her sword hand is very still.{/n}''',
      c('[Salute] "Dismissed, Knight-Captain. For tonight."', flags=("irabeth.trickster.friends",)),
      c('"Something\'s stopping you. Say it."', "no", forbids=(A_RET,)),
      c('"Something\'s stopping you. Say it."', "no_home", requires=(SHARES,)),
      c('[Kiss her] "Irabeth." Not her rank. Her name.', "reckon", requires=(SHARES,), forbids=(LIED,),
        flags=("irabeth.committed",)),
      c('[Wait for her to decide] "Whatever you want. Not an order."', "decides", requires=(SHARES,),
        flags=("irabeth.committed",)),
      c('"Something\'s stopping you. Say it."', "no_gate", requires=(A_RET,), forbids=(SHARES,))),
    i("no", '''"Nevi's out on that road. I'm not doing this behind her back. Not while she's out there. Maybe not after."
{n}She looks at the empty throne, not at you.{/n}
"Ask me when she's home, and ask me like a person, not like a Commander. Until then I'm your knight, and that's all I am."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("no_home", '''"It isn't Nevi. Nevi said her piece; I asked her to her face and she said yes before I'd finished."
{n}She turns the sword a quarter-turn in her fist, the only fidget she allows herself.{/n}
"It's me. I was dead, Commander. Two days. Give me time to be alive before you ask me to be anything else."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("no_gate", '''"Nevi's at the gate, and she hasn't said a word to me about you. Not one. She's a spy; that silence is a message, and I haven't read it yet."
{n}She shifts her grip on the sword.{/n}
"I'm not doing this behind her back. When she's said her piece to me, to my face, ask me again."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("decides", '''{n}She reads you the way she reads an order: twice, to be sure of it.{/n}
"Not an order."
{n}Then she decides.{/n}''',
      c("Continue", "reckon")),
    i("reckon", '''{n}She doesn't move yet. The sword is still in her hand; it is always in her hand.{/n}
"Before anything. I was dead for two days, Commander. I came back holding a sword I can't put down, under an order I never asked for, to a wife who'd already buried me. None of that was a gift. Some of it's your fault."
{n}She looks at her sword hand, then at you.{/n}
"So understand what this is. Not gratitude. Not duty. I'm choosing it, with my eyes open."''',
      c("Continue", "reckon_blow", requires=(BLOW,)), c("Continue", "threshold", forbids=(BLOW,))),
    i("reckon_blow", '''"And I remember your blade going in. I'll remember it tomorrow, and the day after. I'm choosing you anyway, and I want you to know that's a choice, not a forgetting."''',
      c("Continue", "threshold")),
    nar("threshold", THRESHOLD, c("Continue", "morning")),
    i("morning", MORNING_HOME, c('"Dismissed, Knight-Captain."')),
], requires=("trickster.ever", "irabeth.trickster.back_on_duty"), forbids=("irabeth.committed", DECLINED), delay=72)

physical("irabeth.trickster.second_ask", "The pen", '"Knight-Captain. I\'m asking again."', [
    i("price", '''"You want to ask again. Not while you're holding that."
{n}She nods at your coat, at the inside pocket where the pen has lived since Iz. The pen you misplaced for two days, so her discharge could not be signed.{/n}
"As long as you've got it, I'm under orders whether I like it or not, and so is anything I say to you. Give it to me. I'll send it to Nevi. If she sends it back, the answer's no. If she keeps it, ask me."''',
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "sent",
        forbids=(A_RET,), flags=(SIGNED,)),
      c('"Some things I keep."', "refused", flags=("irabeth.closed",)),
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "sent_gate",
        requires=(SHARES,), flags=(SIGNED,)),
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "held",
        requires=(A_RET,), forbids=(SHARES,))),
    i("refused", '''"Then you're my Commander, and that's the end of it."
{n}She salutes, exactly as the regulations describe, and goes back to her post. The pen stays in your pocket. So does every order you ever gave her.{/n}''',
      c('"Understood."')),
    i("sent", '''{n}It is five days before she finds you again. The courier from the south road brought nothing back: no pen, no packet. Only a message he had been made to learn by heart and would not say until the Knight-Captain was standing in front of him.{/n}
"'Keeping it. Ask me to my face next time, Beth.'"
{n}She repeats it to you word for word, the way she repeats every report. Then she smiles, and you realise you have not seen it since Iz.{/n}''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered"))),
    nar("threshold", THRESHOLD, c("Continue", "morning", forbids=(A_RET,)), c("Continue", "morning_home", requires=(A_RET,))),
    i("morning", MORNING_NOTE, c('"Dismissed, Knight-Captain."')),
    i("sent_gate", '''{n}She is back within the hour, empty-handed, with mud from the gate road on her boots.{/n}
"She didn't laugh. She turned it over twice, the way I read orders, and put it in her boot. Then she told me to go back up the hill before she changed her mind about both of us."
{n}She holds out her empty hand to show you, as if the absence were the report. Then she smiles, and you realise you have not seen it since Iz.{/n}''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered"))),
    i("held", '''{n}She takes the pen, weighs it, and slides it into the cuff of her gauntlet instead of sending it.{/n}
"Nevi's at the gate and hasn't said her piece. I'm not walking your pen out to her before she has. That's not how it goes, not with her."
{n}She taps the cuff once.{/n}
"It stays here until she speaks. Then I'll carry it out to her myself."''',
      c('"Then we wait for her."', abort=True)),
    i("morning_home", MORNING_HOME, c('"Dismissed, Knight-Captain."')),
], requires=("trickster.ever", DECLINED, "irabeth.trickster.back_on_duty"), forbids=("irabeth.committed",), delay=96)


# --- Epilogue: one page, or paragraphs on her registered ending ----------------------------------------------------

UNDER_ORDERS_PARAGRAPHS = (
    p("She had come back under an order and not under a vow. In the Drezen roster, under 'On watch', her name stayed in "
      "her own square hand for the rest of the war, and no clerk ever tried to strike it again.", requires=(UNDER_ORDERS,)),
    p("She had come back remembering two things at once: the Commander's blade, and the step. She never pretended the "
      "first had not happened. She taught the step to every recruit who would hold their ground long enough to learn it.", requires=(BLOW,),
      forbids=(LIED,)),
    p("She served out the war exactly, and not one hour more. Of what happened at Iz she said only that the dragon had "
      "been blamed for enough already.", requires=(LIED,)),
    p("When the Wound closed, the sword opened her hand at last. Anevia took the Commander's pen out of her boot, "
      "where it had ridden out the war, and handed it to her wife without a word. Irabeth signed her own discharge "
      "with it, read it twice, the way she read every order, and put it in her pocket instead of the roster. What she "
      "did with the free hand was her own business, and she made sure everyone understood that.", requires=(SIGNED,)),
    p("When the Wound closed, Irabeth Tirabade put her sword down at last, flexed the hand, and asked the Commander "
      "the question she had been saving: not as a knight, and not under orders. She asked it out loud, in the kitchen "
      "of the house on the corner, with Anevia leaning in the doorway to hear it first.", requires=("irabeth.trickster.late_committed",),
      forbids=("irabeth.committed", "irabeth.closed", DECLINED, "irabeth.trickster.friends")),
    p("She stayed the Commander's knight until the Wound was closed: loyal, exact, and never once off the record.",
      requires=(DECLINED,), forbids=("irabeth.committed", "irabeth.closed")),
    p("She stayed the Commander's knight, and that was all. When the discharge was finally signed she saluted, took "
      "it, and did not look back.", requires=("irabeth.closed",)),
    p("She and the Commander stayed what they had agreed to be on the night of the salute: a Knight-Captain and her "
      "Commander, who knew exactly how far the other would go.", requires=("irabeth.trickster.friends",),
      forbids=("irabeth.committed", "irabeth.closed")),
)

SCENES.append(scene("irabeth.trickster.epilogue.under_orders", "Until the Wound is shut", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}Irabeth Tirabade served the crusade until the Worldwound was closed. She could not have stopped sooner if she had wanted to, and she complained about it at length, in writing, to anyone who would file it.{/n}''',
      portrait="Irabeth", paragraphs=UNDER_ORDERS_PARAGRAPHS)],
    requires=(RETURNED,), forbids=("irabeth.lover", "trying", "committed"), last=99, Relationship="irabeth",
    ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))


REACTIONS = [
    reaction("Seelah", "irabeth.trickster.dead.react_seelah", (RETURNED, "irabeth.trickster.seelah_prayed"),
             '''{n}Seelah does not sit down. She stands with her arms folded, and her holy symbol is in her fist.{/n}
"I asked the Inheritor to take her. I knelt in the mud at Iz and asked Her to welcome my sister into Her army. And you told Her Irabeth was still on shift."
{n}Her voice cracks on the last word.{/n}
"I'm going to be angry with you for a week, Commander. Then I'm going to hug her until she complains."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone", KILLED), chapter=5, last=5,
             entry='"Irabeth is back."'),
    reaction("Galfrey", "irabeth.trickster.dead.react_galfrey", (RETURNED,),
             '''{n}A letter under the Queen's seal, in the Queen's own hand.{/n}
"I wept for you in front of my knights, Knight Tirabade. I would do it again. You gave your life for mine at Iz, and I will not be told that the gift was a clerical error.
You owe me the dignity of an explanation. Your Commander owes me a better one.
Galfrey."''',
             remote=True, forbids=("galfrey.dead", "galfrey.killed_by_commander", KILLED), chapter=5, last=5,
             delay=24, title="A letter under the Queen's seal", Chapters=[5]),
    reaction("Seelah", "irabeth.trickster.killed.react_seelah", ("irabeth.trickster.blow_rewritten",),
             '''{n}Seelah's hands are shaking. She hides them behind her back, the way she did as a novice.{/n}
"Everyone says she stepped. The men who carried her out of Iz say they saw your sword go in. And now they remember her stepping too, and so do I, and I wasn't even there."
"Commander, I'm going to pray about this. And then I'm going to hit you."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone"), chapter=5, last=5,
             entry='"Irabeth is back."'),
]
SCENES.extend(REACTIONS)

# G6(b): her registered endings that Forbid irabeth_dead lift it once she has returned; G6(a): the loss page does not.
# G6(b): her scenes that Forbid anevia_gone lift it once Anevia has returned.
ANEVIA_GONE_LIFTED = ("irabeth.one_truth_to_tell", "irabeth.anevias_answer", "irabeth.the_evening_she_chose",
                      "irabeth.a_day_of_our_own", "irabeth.after_the_shared_answer")
RETURNING_ENDINGS = ("irabeth.anevias_answer", "irabeth.ending_lasting", "irabeth.ending_open", "irabeth.ending_friends",
                     "irabeth.ending_unfinished", "irabeth.ending_changed", "irabeth.ending_ascent", "irabeth.ending_sacrifice")


def integrate(payload):
    """Save-safe edits to the registered route (no id, node or choice changes): relationship patch, presence, grief
    overrides, the under-orders paragraphs on her registered endings, and the returned Irabeth kept out of her
    pre-Iz private scenes (they stay closed after IrabethDead, as before)."""
    rel = payload["Relationships"]["irabeth"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a fallen Irabeth may still be under the Commander's orders. After the "
                        "Coronation, look for her in the throne room.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    for key, cues in SEEN_CUES.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    ours = {s["Id"] for s in SCENES}
    for s in payload["Scenes"]:
        if s.get("Relationship") != "irabeth" or s["Id"] in ours:
            continue
        if s["Id"] in ANEVIA_GONE_LIFTED:
            s.setdefault("ForbidOverrides", {})["anevia_gone"] = A_RET
        if s["Id"] in RETURNING_ENDINGS:
            s.setdefault("ForbidOverrides", {})["irabeth_dead"] = RETURNED
            if s["Owner"].endswith("Epilogue"):
                for node in s["Nodes"]:     # the pages that end the ending: every choice closes it
                    if all(ch.get("Next") is None for ch in node["Choices"]):
                        node.setdefault("Paragraphs", []).extend(dict(x) for x in UNDER_ORDERS_PARAGRAPHS)
        elif s["Id"] == "irabeth.ending_loss":
            s["Forbids"].append(RETURNED)
        elif not s["Owner"].endswith("Epilogue") and "irabeth_dead" not in s["Forbids"] \
                and "irabeth_dead" not in s.get("Requires", []):
            s["Forbids"].append("irabeth_dead")
