"""Irabeth on the Trickster path: relieved, not dismissed (Writer/handoffs/trickster/irabeth.md, families F04 and F19).

Canon: at Iz she reports "Your Majesty. Commander. Irabeth Tirabade... stands relieved." (IrabethDies/Cue_0001 f7d10f44) and
dies with "Anevia. Tell her I love her. Take care... of my Nevi." (Cue_0013 1f6f05c7). The native relief is Answer_0015
741681b4 "I relieve you." -> Cue_0016 dc5a8da4 "That means I can go with a clear conscience." The Trickster takes her at her
word and not one word further: relieved of duty, never dismissed. Polish 9b (no mythic-power solution): the order is
why her soul answers, never what raises her. After Iz the chapel has diamond for one raise, and the Commander strikes a
young knight's name off the chaplain's list and writes hers above it (`dead.raise_list`); the chaplain calls her once,
and she answers because she is still on the roster. The boy stays dead; she swears at his bier to carry his share of the
war, sword never out of reach, until the Wound is shut (her own vow, the Trickster echo of DLC1 Anevia Cue_0037 f397cfe1, where
Iomedae binds her sword; here nobody binds it but her). If the Commander struck her down at Iz, the Mobility step drilled
before Iz (her hub; TricksterMobilityTier3Feature 6db3651d is only the lesson's source) turns the blade under the ribs,
and the Commander sends diggers and a healer back to the ruin (`killed.dig`). Undrilled, the only way back is the same
raise list, with the kill written into the chapel's record in the Commander's words (`killed.late_step`). Her
Trickster judgment: "Your orders seem crazy sometimes, but they lead us to victory." (Irabeth_C3_Intro/Cue_0124 2302cb7c).
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
VELL = "irabeth.trickster.cost.vell"             # polish 9b: the raise list; Teodor Vell's diamond, and her vow for it
DUG = "irabeth.trickster.cost.dug_out"                # polish 9b: the drilled step, and the diggers the Commander sent
K_RAISED = "irabeth.trickster.raised_on_record"  # polish 9b: undrilled; raised on the list, the kill on the record
ASKED = "irabeth.trickster.asked_nevi"           # Irabeth asked Anevia herself (read by Anevia's route)
CONFESSED = "irabeth.trickster.told_the_other_story"
PEN_SENT = "irabeth.trickster.pen_sent"
BOUGHT = "irabeth.trickster.cost.second_diamond"  # Sol r1: the boy is called too; the crusade pays for her diamond
HEALER = "irabeth.trickster.cost.hired_healer"     # Sol r1: the column keeps a healer; the treasury pays for it
TRUSTED = "irabeth.trickster.slept_under_her_sword" # Sol r1: after a deliberate blow, her trust test before any yes
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

# Polish 9b: the decisive act. The order does not raise her; a chaplain does, with the crusade's diamond. The Commander
# either takes the one diamond from the boy at the top of the list, or buys a second at a price the treasury feels. Her
# soul still has to answer (a raise calls, it does not drag). Sol r1: the boy's death is never the compulsory price.
RAISE_LIST_START = '''{n}The chapel keeps a list after every battle. After Iz it is eleven names long: the fallen whose bodies came home whole enough to call back, in the order the chaplains mean to call them. Beside it lies the crusade's strongbox, open. There is diamond enough in it for one.{/n}
{n}The first name is Teodor Vell, nineteen, knighted in the mud at Iz for holding a stair with a broken shield. Irabeth Tirabade is fourth. The chaplain has already ground the first diamond; the bowl is on the altar, and he is waiting for dark.{/n}'''
CALL_TEXT = '''"I will call her. Once. A raise is a summons, not a leash; if she went to the Inheritor with a clear conscience she will not come back for a general's convenience, and I will not ask twice. If she answers, the diamond was hers. If she does not, you will have wasted it."
{n}At the door he stops.{/n}
"She will ask whose it was. I will not lie to her."'''
BOUGHT_TEXT = '''{n}The Queen's household keeps a jeweller in Drezen for the crown's use. He does not keep diamonds of that size for anyone else's, and he names a price for the one he has that makes the treasurer sit down.{/n}
"Two, then," {n}the chaplain says, when it is on the altar beside the first.{/n} "The boy first, as the list says. Then her, if she will come." {n}He looks at the second stone, and then at you.{/n} "That is a great deal of the crusade's bread, Commander, for one knight's answer."'''


def list_nodes(p, argue):
    """The chapel's list as nodes (prefix p): strike the boy, buy a second diamond, or let the list stand. argue: the
    Continue choices from the struck page to the page that argues she is still on duty."""
    return [
        nar(p + "list", RAISE_LIST_START,
            c('[Strike Vell\'s name and write hers above it] "She was never dismissed. Call her first."', p + "struck"),
            c('[Leave the list as it stands] "Call the boy."', p + "boy", flags=(DECLINED,)),
            c('[Buy a second diamond from the Queen\'s jeweller] "Call them both. The crusade will find the money."',
              p + "bought")),
        nar(p + "struck", '''{n}The chaplain does not take the pen from you. He watches you use it.{/n}
"Sir Teodor has a mother in Nerosyan, Commander. I wrote to her this morning that he would be home by the spring."''',
            *argue),
        nar(p + "call", CALL_TEXT,
            c('"Don\'t. Tell her his name."', flags=(VELL, "irabeth.started"), crusade=("Favors", -100))),
        nar(p + "bought", BOUGHT_TEXT,
            c('"Call them both."', p + "call_both")),
        nar(p + "call_both", CALL_TEXT,
            c('"Tell her. Tell her the price too."', flags=(VELL, BOUGHT, "irabeth.started"), crusade=("Finances", -600))),
        nar(p + "boy", '''{n}The chaplain nods, once, as if you had passed something. At midnight Teodor Vell sits up on the altar coughing grave-dust, asks whether they held the stair, and weeps when they tell him.{/n}
{n}Irabeth's name stays fourth. The strongbox is empty by morning.{/n}''',
            c('"Goodbye, Irabeth."')),
    ]


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
      c('"Dawn, Knight-Captain."', forbids=("irabeth_dead",)),     # retired by gating (index kept): the list follows
      c('[Follow the chaplain back to his chapel] "Dawn, Knight-Captain. Chaplain, a word."', "l_list")),
    nar("rest", '''{n}You drink. The knights drink. Nobody says anything clever, and the boots stay under the bunk until morning, when the quartermaster takes them away.{/n}''',
      c('"Goodbye, Irabeth."')),
    # Sol r1 COX (letter budget): the late toast and the chapel's list are one delivery.
    *list_nodes("l_", (c("Continue", "l_argue"),)),
    nar("l_argue", '''"And you will tell me she is still on duty because a drunk knight answered 'present' for her at your toast."
{n}You tell him exactly that. You also tell him who signs the chapel's requisitions.{/n}''',
      c("Continue", "l_call")),
], requires=("trickster", "irabeth_dead", "irabeth.dead.latched"), forbids=(PRIMED, RETURNED, DECLINED, KILLED), delay=24,
   TricksterDevice=True, TricksterState="dead")

letter("irabeth.trickster.dead.raise_list", "Diamond for one", [
    nar("start", RAISE_LIST_START,
      c('[Strike Vell\'s name and write hers above it] "She was never dismissed. Call her first."', "struck"),
      c('[Leave the list as it stands] "Call the boy."', "boy", flags=(DECLINED,)),
      c('[Buy a second diamond from the Queen\'s jeweller] "Call them both. The crusade will find the money."', "bought")),
    nar("struck", '''{n}The chaplain does not take the pen from you. He watches you use it.{/n}
"Sir Teodor has a mother in Nerosyan, Commander. I wrote to her this morning that he would be home by the spring."''',
      c("Continue", "roster", requires=(STANDING,)),
      c("Continue", "toast", requires=(LATE,), forbids=(STANDING,)),
      c("Continue", "salute", forbids=(STANDING, LATE))),
    nar("roster", '''{n}You have the duty roster brought over from the barracks and laid open beside his list. Under her name, in her own square hand: "To report to the Commander in person. Not to be struck off except by the Commander."{/n}
"She wrote that herself," {n}he says.{/n} "I know the hand." {n}He reads it twice, the way she would have.{/n}''',
      c("Continue", "call")),
    nar("toast", '''"And you will tell me she is still on duty because a drunk knight answered 'present' for her at your toast."
{n}You tell him exactly that. You also tell him who signs the chapel's requisitions.{/n}''',
      c("Continue", "call")),
    nar("salute", '''"You refused her salute at Iz. I heard of it. The whole column heard of it." {n}He looks at the name you have written, and at the one you have struck through.{/n} "That is not a reason, Commander. It is a wager."''',
      c("Continue", "call")),
    nar("call", CALL_TEXT,
      c('"Don\'t. Tell her his name."', flags=(VELL, "irabeth.started"), crusade=("Favors", -100))),
    nar("boy", '''{n}The chaplain nods, once, as if you had passed something. At midnight Teodor Vell sits up on the altar coughing grave-dust, asks whether they held the stair, and weeps when they tell him.{/n}
{n}Irabeth's name stays fourth. The strongbox is empty by morning.{/n}''',
      c('"Goodbye, Irabeth."')),
    nar("bought", BOUGHT_TEXT, c('"Call them both."', "call_both")),
    nar("call_both", CALL_TEXT,
      c('"Tell her. Tell her the price too."', flags=(VELL, BOUGHT, "irabeth.started"), crusade=("Finances", -600))),
], requires=("trickster", "irabeth_dead", PRIMED), forbids=(RETURNED, DECLINED, KILLED, VELL), delay=12,
   TricksterDevice=True, TricksterState="dead")

physical("irabeth.trickster.dead.relieved_not_dismissed", "Reporting in person", '"Knight-Captain?"', [
    nar("start", '''{n}The chaplain calls her name over the bier at the second bell of the night, once, with the diamond dust smoking in the bowl. The knight keeping vigil swears afterwards that she answered before her eyes were open, and that the word was "Reporting".{/n}
{n}She spends a day on a chapel cot, weak as a kitten and furious about it. The morning after, the Knight-Captain is in the throne room, at attention before your chair, waiting to report.{/n}''',
      c("Continue", "report")),
    i("report", '''"Knight-Captain Tirabade, reporting in person. As ordered."
{n}Her voice is hoarse, and very irritated. The burial whites are belted over her arming coat. There is a sword in her hand that is not hers.{/n}
"The chaplain says I was dead long enough to be sung for. The chaplain also says my discharge was 'misplaced'. I have never misplaced a form in my life, Commander."''',
      c("Continue", "torn", requires=(SOUL_TORN,)),
      c("Continue", "standing", requires=(STANDING,), forbids=(SOUL_TORN,)),
      c("Continue", "toasted", requires=(LATE,), forbids=(SOUL_TORN, STANDING)),
      c("Continue", "vell", forbids=(BOUGHT, SOUL_TORN, STANDING, LATE)),
      c("Continue", "vell_bought", requires=(BOUGHT,), forbids=(SOUL_TORN, STANDING, LATE))),
    i("torn", '''"Whatever they threw at me at Iz went through my soul like a saw. I told you so. I felt it come apart."
{n}She flexes her sword hand. The knuckles are white.{/n}
"The chaplain says it knits. Slowly, like a bone. I can feel exactly where the break was."''',
      c("Continue", "standing", requires=(STANDING,)),
      c("Continue", "toasted", requires=(LATE,), forbids=(STANDING,)),
      c("Continue", "vell", forbids=(BOUGHT, STANDING, LATE)),
      c("Continue", "vell_bought", requires=(BOUGHT,), forbids=(STANDING, LATE))),
    i("standing", '''"I wrote that order into the roster myself. 'In person.' I thought you were being sentimental. You were being a lawyer. The chaplain read it out over me, the fool, and I heard it, wherever I was, and I thought: that's my hand. I'm on watch."''',
      c("Continue", "toasted", requires=(LATE,)), c("Continue", "vell", forbids=(LATE, BOUGHT)),
      c("Continue", "vell_bought", requires=(BOUGHT,), forbids=(LATE,))),
    i("toasted", '''"And somebody toasted my empty bunk and called it a roll call. The chaplains are still complaining. I'd complain too, if I weren't standing here."''',
      c("Continue", "vell", forbids=(BOUGHT,)), c("Continue", "vell_bought", requires=(BOUGHT,))),
    i("vell", '''"And the chaplain told me whose diamond it was. He said you told him to."
{n}She does not raise her voice. That is worse.{/n}
"Teodor Vell. Nineteen. He held a stair at Iz with half a shield. I went and stood at his bier before I came up here, and I swore on his sword, since he won't be needing it: his share of this war and mine, and it doesn't leave arm's reach until the Wound is shut. Not to eat. Not to sleep. That's what I cost, Commander. I want you to see it every time you look at me."''',
      c("Continue", "discharge")),
    i("vell_bought", '''"And the chaplain told me what I cost. A diamond from the Queen's own jeweller, so the boy at the top of the list got his too. Teodor Vell. Nineteen. He sat up an hour before I did, asking about his stair."
{n}She does not raise her voice. That is worse.{/n}
"That's a winter's bread for a company, Commander, spent on one knight's answer. I swore at the altar before I came up here: I fight the rest of this war for what I cost, and this sword doesn't leave arm's reach until the Wound is shut. Not to eat. Not to sleep. I want you to see it every time you look at me."''',
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
    nar("south", '''{n}She hears it standing at attention, and she stays that way after you have finished.{/n}
"South. Of course south. She never could sit in a house with a draught in it."
{n}She is gone before noon on a borrowed horse, riding south after her wife with the sword at her hip. She does not say when she will be back, and nobody is fool enough to ask.{/n}''',
      c('"Welcome back, Knight-Captain."')),
    nar("home", '''{n}She is out of the throne room before you finish the sentence, burial whites and all, with the sword at her hip, where she has sworn to keep it.{/n}
{n}Nobody in the citadel sees that meeting. The guard at the stair reports only that the Knight-Captain's wife said one word, loudly, and that it was not a word for a chapel.{/n}''',
      c('"Welcome back, Knight-Captain."')),
    nar("gate", '''{n}She doesn't ride anywhere. Anevia is at the gate, on the road side of the line the cartwheels have worn into the mud. Irabeth walks out to her in her burial whites, without her helmet, with the sword she has sworn to keep by her slung across her back.{/n}
{n}The watch on the gate finds something very interesting to look at in the other direction, and goes on looking at it for some time.{/n}''',
      c('"Welcome back, Knight-Captain."')),
], requires=("trickster.ever", "irabeth_dead", PRIMED, VELL, "coronation.seen"), forbids=(RETURNED, KILLED), delay=24,
   TricksterDevice=True, TricksterState="dead")


# --- State killed_by_commander: the step she learned ---------------------------------------------------------------

letter("irabeth.trickster.killed.late_step", "The report of the day", [
    nar("start", '''{n}The chaplain who came back from Iz is writing the report of the day by candlelight. He has written "Knight-Captain Irabeth Tirabade, slain by" and stopped.{/n}
{n}He is looking at you. So is the knight holding the candle.{/n}''',
      # Polish 9b: the dictated step (a report that rewrote the blow) is retired by gating; its index is kept for saves.
      c('[Dictate the step] "Write it down. I swung. She stepped. Everyone saw her step."', "lie", mythic="Trickster",
        alignment=("Chaotic", 1), crusade=("Favors", -200), flags=(DRILLED, LATE, "irabeth.started"),
        forbids=("irabeth_dead",)),
      c('[Let the blow stand] "No. It happened. I did it."', "stands", flags=(DECLINED,)),
      c('[Finish his line for him, then take his list] "Slain by me. Write it. Then put her name at the top of your raise list."',
        "record")),
    nar("lie", '''{n}He writes it. His hand shakes on "stepped", and the word comes out crooked. When he is done he sands the page, folds it, and gives it to the knight to carry to the archive.{/n}
"I will remember the other one, Commander," {n}he says, very quietly.{/n} "Every day. So will he."
{n}The knight with the candle does not say anything. By the end of the week the whole order has heard some version of it, and no two versions agree.{/n}''',
      c('"Remember what you like. File what I said."')),
    nar("stands", '''{n}He finishes the line in your words. He does not soften them. When he is done he looks at the page, then at you, and nods once, as if you had passed something.{/n}''',
      c('"File it."')),
    nar("record", '''{n}He writes "the Commander" in a steady hand and underlines it. Then he looks at the list beside the report: eleven names, the fallen of Iz whose bodies came home whole enough to call back, and diamond in the strongbox for one, promised to the boy at the top of it.{/n}
"You want the woman you killed called back. The crusade's diamond is the boy's. You will buy her one of your own from the Queen's jeweller, at his price, and I will not strike a name to save you the money."
{n}He sets the pen down. He is not a young man, and his hands are very steady.{/n}
"And a knight struck down by her own Commander is called before her Commander may ask anything of her, because somebody must be alive to testify against you. That will be the entry, in your words. I will call her once. If she will not come back to serve under you, I would not blame her, and neither will the Inheritor."''',
      c('[Let him write it] "Write every word. Then call her."', mythic="Trickster", crusade=("Favors", -200),
        flags=(K_RAISED, VELL, LATE, BLOW, "irabeth.started"), forbids=("irabeth_dead",)),   # retired by gating
      c('[Let him write it, and pay the jeweller] "Write every word. Then call her."', mythic="Trickster",
        crusade=("Finances", -600), flags=(K_RAISED, LATE, BLOW, "irabeth.started"))),
], requires=("trickster", "irabeth_dead", KILLED, "irabeth.dead.latched"), forbids=(DRILLED, RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState="killed")

# Polish 9b: the drill pays off in the flesh. She stepped, so the blade went under the ribs, and she fell into the ruin
# alive; the Commander, who taught her the step, is the one who sends men back to dig.
letter("irabeth.trickster.killed.dig", "Half a pace left", [
    nar("start", '''{n}The report of the day at Iz lies on your camp table, waiting for your seal. Among the dead: "Knight-Captain Irabeth Tirabade, struck down by the Commander's hand, fell into the lower ruin, body not recovered." The column marches north at first light. The ruin is already behind it, and full of broken stone.{/n}
{n}You taught her the step: half a pace left and inside, into whatever cover the ground gives. At Iz, when you struck her down, she was already moving. She went down into the broken stone of the lower ruin, out of sight, and nobody went in after her.{/n}''',
      c('[Send two sappers and the column\'s best healer back to the ruin] "She stepped. I taught her to. Dig."', "dig",
        crusade=("Favors", -150), flags=(DUG, "irabeth.started")),
      c('[Let the blow stand] "No. It happened. I did it."', "stands", flags=(DECLINED,)),
      c('[Buy the column a surgeon from the Mendevian baggage train first, then send the sappers and the healer] "She stepped. I taught her to. Dig."',
        "dig_paid", crusade=("Finances", -400), flags=(DUG, HEALER, "irabeth.started"))),
    nar("dig_paid", '''{n}The Mendevian baggage master has a surgeon to spare and a price for him that he does not bother to make polite. You pay it. The column keeps its healing; the healer goes back to the ruin with two sappers and their picks.{/n}
{n}On the second morning a rider catches the column up. They found the Knight-Captain in a cellar of the lower ruin, under a fallen lintel, alive, with the wound packed with her own tabard and her sword in her fist. Your blow took her in the side, under the ribs, where she had stepped to, and not in the heart, where she had stood. Half a pace.{/n}''',
      c('"Bring her home."')),
    nar("dig", '''{n}The healer argues. There are forty wounded in the wagons, and she is the one who keeps them breathing on the road. You send her anyway, with two sappers and their picks, and the column marches without them. Two men in the wagons die on the road who would have lived with her beside them. Nobody offers you their names. You ask for them.{/n}
{n}On the second morning a rider catches the column up. They found the Knight-Captain in a cellar of the lower ruin, under a fallen lintel, alive, with the wound packed with her own tabard and her sword in her fist. Your blow took her in the side, under the ribs, where she had stepped to, and not in the heart, where she had stood. Half a pace.{/n}''',
      c('"Bring her home."')),
    nar("stands", '''{n}You seal the report as it is written. The column marches at first light, and the lower ruin stays as it is.{/n}''',
      c('"File it."')),
], requires=("trickster", "irabeth_dead", KILLED, DRILLED, "irabeth.dead.latched"), forbids=(DUG, RETURNED, DECLINED), delay=0,
   TricksterDevice=True, TricksterState="killed")

physical("irabeth.trickster.killed.blow_missed", "The step she learned", '"Knight-Captain?"', [
    nar("start", '''{n}She is in the throne room with a sword in her hand. There is a fresh seam in her surcoat, over the ribs, where your blow took her.{/n}''',
      c("Continue", "shaken", requires=(LATE,)), c("Continue", "dug", forbids=(LATE,))),
    nar("dug", '''{n}The report of the day at Iz, in the archive, says the Knight-Captain stepped inside the Commander's blow, fell into the lower ruin and was dug out alive on the second morning by men the Commander sent back for her. Every word of it is true.{/n}''',
      c("Continue", "both")),
    nar("shaken", '''{n}The chapel's book of Iz has two lines under her name, in the same steady hand. "Struck down by the Commander." And below it: "Called back on the Commander's order, the Commander's confession entered above." She has read it. You can tell by the way she stands.{/n}''',
      c("Continue", "both", forbids=(LATE,)), c("Continue", "raised")),
    i("both", '''"I remember your blow. I remember the cold, after. I also remember stepping, the way you taught me, half a pace left and inside. That's why it took me in the side and not the heart, and why I went down into a cellar and not onto the street with the others."
{n}Her knuckles whiten on the hilt.{/n}
"You taught me the one thing that would save me from you. I hate that more than the blow."''',
      c('[Tell it the way the report does] "I swung. You stepped. Everybody saw you step."', "accounting", mythic="Trickster"),
      c('[Let the blow stand] "No. I did it. I won\'t take it back."', "salute", flags=(DECLINED, BLOW_STANDS))),
    i("accounting", '''"Everybody saw what happened. The report's true. That's what makes it worse."
{n}She takes one step closer. It is a very precise step.{/n}
"So which one did you mean, Commander? The swing, or the lesson?"''',
      c('"I meant it. At Iz, I meant it. I don\'t now."', "truth",
        flags=(RETURNED, "irabeth.started", "irabeth.trickster.blow_rewritten", BLOW,
               "irabeth.trickster.accounting_truth", "irabeth.accounting_kept")),
      c('[Lie] "It was the dragon\'s sorcery. It wasn\'t me."', "lie",
        flags=(RETURNED, "irabeth.started", "irabeth.trickster.blow_rewritten", BLOW, LIED))),
    i("truth", '''{n}She takes it like a blow she saw coming. She does not step away from it.{/n}
"Good. I'd have known if you lied. I've questioned cultists who lied better than you, and I hanged them."
{n}She rests her hand on the sword at her hip. It has not been out of her reach since the ruin.{/n}
"I swore something down there with a lintel on my chest. This stays within reach until the Wound is shut. The next time you swing at me, I'll have it. I'm back on duty. Don't mistake that for forgiveness."''',
      c('"Understood, Knight-Captain."')),
    i("lie", '''{n}Something shuts behind her eyes, the way a gate shuts.{/n}
"The dragon. Of course."
{n}She rests her hand on the sword at her hip. It has not been out of her reach since the ruin.{/n}
"I'm back on duty, Commander. I'll serve. This stays within reach until the Wound is shut, and you can work out for yourself who it's for. Don't ask me for more than that."''',
      c('"Dismissed."')),
    nar("salute", '''{n}She salutes. It is a perfect salute, the one she gives the Queen.{/n}
{n}Before noon her request for a posting on the southern wall is on your desk, in her square hand, with a space left for your seal. It is the only paper she has ever asked you to sign. You sign it. When you look up from it, the throne room is empty.{/n}''',
      c('"...Goodbye, Irabeth."')),
    i("raised", '''"I remember your blow landing. I remember the cold. Then a voice calling me by my rank, once, and yours behind it, and I thought: I'm not finished with that one."
{n}She has a sword in her hand that is not hers.{/n}
"You killed me, Commander. Then you had a priest write it down and bought a diamond from the Queen's jeweller to fetch me back to read it. I swore at the altar with the chaplain for witness: this sword doesn't leave my reach until the Wound is shut. You'll never again find me without it."
{n}She takes one very precise step closer.{/n}
"So I'll ask once. Which did you mean? Iz, or the list?"''',
      c('"I meant it. At Iz, I meant it. I don\'t now."', "truth_raised",
        flags=(RETURNED, "irabeth.started", BLOW, UNDER_ORDERS, "irabeth.trickster.accounting_truth", "irabeth.accounting_kept")),
      c('[Let the blow stand] "Iz. I won\'t take it back."', "salute", flags=(DECLINED, BLOW_STANDS))),
    i("truth_raised", '''{n}She hears it the way she hears a casualty list: all the way to the end.{/n}
"Good. It's in the chapel's book in your words already. I wanted it in mine, to my face."
"I'm back on duty, Commander. Somebody has to be alive to watch you. Don't mistake that for forgiveness."''',
      c('"Understood, Knight-Captain."')),
], requires=("trickster.ever", "irabeth_dead", KILLED, "coronation.seen"),
   forbids=(RETURNED, "trickster.failed", DECLINED), delay=24, TricksterDevice=True, TricksterState="killed",
   RequiresAnyGroups=[[DUG, K_RAISED]])


# --- After the return: the test, the commit, her no ---------------------------------------------------------------

# Q12 (Sol BEL): with no lover's history behind her, the killed history needs a reason for desire, not only vigilance. She
# watches the Commander read the Iz line aloud at the muster, the one thing she would have done herself, and she is the one
# who moves. Required (DRAWN) before her own trust test on that branch; a lover's history already has its grounds.
DRAWN = "irabeth.trickster.drawn"
physical("irabeth.trickster.killed.the_roll", "The roll of the dead", '"I\'ll read the roll tonight."', [
    nar("start", '''{n}The roll of the week's dead is read in the throne room at the evening muster, as it always is, by a clerk. Tonight you take the list out of the clerk's hands and read it yourself: every name, rank and company, and how each one died. At the head of the old page, never corrected, is the line from Iz, and you read that too, in the same voice. "Knight-Captain Irabeth Tirabade. Struck down by the Commander."{/n}
{n}Two hundred soldiers hear it. Nobody moves. At her post beside the throne, Irabeth does not move either.{/n}''',
      c("Continue", "stair")),
    i("stair", '''{n}She finds you on the back stair afterwards, where the torches are out, and takes you by the wrist hard enough to hurt.{/n}
"You read it out. In front of my company. In front of recruits who think the sun comes up out of your boots." {n}Her grip does not ease.{/n} "Every officer I ever served under would have let the clerk lose that line. You read it like any other."
{n}Then she pulls you in by the wrist and kisses you, once, furious, with her sword hilt jammed between your ribs and hers, and lets go.{/n}
"That's the first thing you've done since Iz that I'd have done myself. Don't read anything into it."''',
      c('[Catch her wrist before she goes] "Too late."', "caught", flags=(DRAWN,)),
      c('[Let her go] "Goodnight, Knight-Captain."', "gone", flags=(DRAWN,)),
      c('"That was a mistake, Knight-Captain."', "mistake")),
    i("caught", '''{n}She stops. She looks at your hand on her wrist, then at you, and for one breath she leans in.{/n}
"Not on a back stair like a pair of recruits." {n}She takes her wrist back, unhurried.{/n} "If you want something from me, Commander, you'll ask for it where I can see your hands."''',
      c('"Goodnight, Knight-Captain."')),
    nar("gone", '''{n}She goes down the stair two steps at a time and does not look back. On the landing below she stops for a moment with one hand flat on the wall, as if the stone had moved, and then she is gone.{/n}''',
      c('"Goodnight."')),
    i("mistake", '''"Probably." {n}She salutes, precisely.{/n} "I make one a year. That was this year's."''',
      c('"Dismissed."', abort=True)),
], requires=("trickster.ever", RETURNED, BLOW, "irabeth.trickster.back_on_duty"),
   forbids=("irabeth.lover", DRAWN, BLOW_STANDS, "irabeth.committed"), delay=24)


# Sol r1 BEL: after the Commander's own blade, no yes without a test she sets and the Commander passes.
physical("irabeth.trickster.killed.the_watch", "Under her sword", '"Knight-Captain. You wanted me?"', [
    i("start", '''{n}She is in the guardroom off the throne room, where the night watch sleeps in shifts. One cot is made up. Beside it is a stool, and she is sitting on the stool with the sword across her knees.{/n}
"You want something from me. I can see it on you. Before you ask it, you're going to sleep here. Tonight. Unarmed. And I'm going to sit on this stool with this until the bell, and you're going to find out whether you can close your eyes."
"I did, at Iz. I closed them for one breath, and you struck. Your turn."''',
      c('[Unbuckle your sword belt, hand it to her, and lie down]', "night", flags=(TRUSTED,)),
      c('"Not tonight."', abort=True)),
    nar("night", '''{n}You lie down. She does not move. The lamp burns low; the watch changes twice beyond the door. Every time you open your eyes she is exactly where she was, the blade across her knees, watching you the way she watches a road at night.{/n}
{n}Near dawn you sleep, properly, for an hour. When you wake she has laid your belt and its gear across your chest and gone. On the stool is a scrap of duty roster with one line on it, in her square hand: "Slept. Didn't die. Neither did I."{/n}''',
      c('"Neither did I."')),
], requires=("trickster.ever", RETURNED, BLOW, "irabeth.trickster.back_on_duty"),
   forbids=(TRUSTED, BLOW_STANDS, "irabeth.committed"), delay=24, RequiresAnyGroups=[["irabeth.lover", DRAWN]])

physical("irabeth.trickster.back_on_duty", "Back on duty", '"Knight-Captain. A word."', [
    nar("start", '''{n}She is at her post in the throne room as if she never left it. The sword is at her hip. It has been within her reach every hour since she came back.{/n}''',
      c("Continue", "hymn", forbids=(BLOW,)), c("Continue", "blow", requires=(BLOW,))),
    i("hymn", '''"They sang for me, Commander. The whole hall. I'm not walking back in there to tell them they wasted a good hymn, so I'm standing here instead."''',
      c("Continue", "sword")),
    nar("blow", '''{n}She keeps the sword between you, point down, and does not pretend otherwise.{/n}''', c("Continue", "sword")),
    i("sword", '''"It doesn't leave my reach. I sleep with it on the chair by the bed and I shave with it propped against the basin. The chaplain says Iomedae asks for no such thing. I told him I wasn't asking Her."
{n}She sets her palm on the pommel, the way another woman might touch a wedding ring.{/n}
"Until the Wound is shut. Your joke had fine print, Commander, and I'm the one who wrote it. I'd still like to have read yours first."''',
      c("Continue", "question"),
      c('[Offer to sign her discharge now] "Then I\'ll sign it. You\'re free."', "unsigned")),
    i("unsigned", '''"And do what? Go home and sit in a chair with a sword across my knees until the Wound shuts without me? I swore to see it shut. A discharge doesn't unswear anything, Commander. It just takes my post away."
{n}She holds out her free hand for the pen anyway, palm up, perfectly steady, to see whether you will. You put it in her palm. She weighs it, then tucks it back into your coat pocket herself.{/n}
"No. Your call. It's always been your call, and I'll not have it said I took it off you the first week I was back. That's the part I can't forgive."''',
      c("Continue", "question")),
    i("question", '''"One question, and you answer it straight. Did you do it for the crusade, or for me?"
{n}She waits.{/n}
"There's a right answer. I'm not telling you which."''',
      c('"Because the crusade needs its Knight-Captain."',
        flags=("irabeth.trickster.back_on_duty", "irabeth.trickster.answered_crusade")),
      c('"Because I needed you back. Not the crusade. Me."',
        flags=("irabeth.trickster.back_on_duty", "irabeth.trickster.answered_her"))),
], requires=("trickster.ever", RETURNED), forbids=("irabeth.trickster.back_on_duty",), delay=24)

THRESHOLD = '''{n}Irabeth pulls you through the side door into her roster room. She sweeps the duty lists off the desk, unbuckles her sword belt, and lays it along the far edge, the hilt within reach. Then she swears, short and furious, at a breastplate buckle.{/n}
"I've wanted this since Iz, and I've been ashamed of it since Iz. I'm done being ashamed. Take the rest off me, Commander. Slowly. I want to remember it."
{n}Gauntlet, then vambrace. Her fingers fumble at the breastplate and she lets you finish. The plate hits the floor. She opens her arming coat; old scars lie pale across hot skin and hard muscle. She catches your mouth, her tusks grazing your lip, then hauls you onto the cleared desk with her, hooks a leg behind yours, and reaches for your belt.{/n}'''

MORNING_NOTE = '''{n}At dawn the watch changes under the window. Irabeth is back in armour, all but one gauntlet. The sword belt still lies along the edge of the desk, within reach. She holds out her bare hand to you without a word.{/n}
"Nevi will know. Nevi always knows. I'll write to her myself before breakfast, before anyone else can."
{n}You buckle the gauntlet for her. She picks up the sword belt and fastens it herself.{/n}
"Knight-Captain Tirabade, reporting for duty. Don't look at me like that in front of the guard."'''

MORNING_HOME = '''{n}At dawn the watch changes under the window. Irabeth is back in armour, all but one gauntlet. The sword belt still lies along the edge of the desk, within reach. She holds out her bare hand to you without a word.{/n}
"Nevi will know. Nevi always knows. She'll laugh at me. Then she'll want to know every detail, and she'll get most of them."
{n}You buckle the gauntlet for her. She picks up the sword belt and fastens it herself.{/n}
"Knight-Captain Tirabade, reporting for duty. Don't look at me like that in front of the guard."'''

REASONS_NEW = '''"You lay down under my sword and handed me yours. I've served three commanders. Not one of them would have done it, and every one of them would have been right not to."
{n}Her jaw sets.{/n}
"And since that back stair I've wanted you. I didn't before Iz. I don't like that I do now, and I'm not going to thank you for it."'''

REASONS_TEXT = '''"You lay down under my sword and handed me yours. Nobody at Iz would have bet on that. Least of all me."
{n}Her jaw sets.{/n}
"And I wanted you before Iz. I buried it under the duty lists and it didn't stay buried. That's the part I can't forgive either of us for."'''

THRESHOLD_BLOW = '''{n}She takes you into the roster room, sweeps the duty lists off the desk, and lays her sword belt along the far edge. She keeps a hand on the hilt until you look at it.{/n}
"Take the rest off me, Commander. Slowly. And leave that where it is."
{n}Gauntlet, then vambrace. The breastplate comes away beneath your hands. She opens her arming coat, exposing hot skin and hard muscle, old scars and the wound you left at Iz. She presses your palm over it and holds it there. Her kiss is fierce; she catches your lower lip between her teeth before letting you breathe. Then she pulls you down onto the cleared desk with her, hooks a leg behind yours, and reaches for your belt. The sword lies beside her hand.{/n}'''

MORNING_HOUSE = '''{n}At dawn the watch changes under the window. Irabeth is back in armour, all but one gauntlet. The sword belt still lies along the edge of the desk, within reach. She holds out her bare hand to you without a word.{/n}
"Nevi will know the second I walk into the kitchen. She'll laugh at me, and then she'll put me to work on the bread and ask questions until it's proved."
{n}You buckle the gauntlet for her. She picks up the sword belt and fastens it herself.{/n}
"Knight-Captain Tirabade, reporting for duty. Don't look at me like that in front of the guard."'''

def her_answer(mornings):
    """Sol r3 HOW/BEL: Nevi's answer licenses the ask; it is not Irabeth's. She is asked, and she can say no. The
    killed history (remembers_the_blow) keeps its own reasons and threshold here too."""
    return [
        i("her_answer", '''"Nevi's said her piece. That's hers. This part's mine."
{n}She waits, and does not help you.{/n}''',
          c('[Ask her] "Irabeth. Not your rank. You."', "yes"),
          c('[Ask her as her Commander] "Knight-Captain. I\'m asking."', "no_rank")),
        i("yes", '''{n}She doesn't answer. She crosses the room and kisses you instead, hard, and that is the answer.{/n}''',
          c("Continue", "threshold", forbids=(BLOW,), flags=("irabeth.committed",)),
          c("Continue", "reasons", requires=(BLOW, "irabeth.lover"), flags=("irabeth.committed",)),
          c("Continue", "reasons_new", requires=(BLOW,), forbids=("irabeth.lover",), flags=("irabeth.committed",))),
        i("no_rank", '''"There it is."
{n}She steps back, and salutes, and it is a perfect salute.{/n}
"You asked my Commander's way, with my wife's answer in your pocket like a signed order. No. I'll serve you till the Wound's shut. That's what you asked for."''',
          c('"...Understood."', flags=("irabeth.trickster.asked_as_commander",))),
        i("reasons", REASONS_TEXT, c("Continue", "threshold_blow")),
        i("reasons_new", REASONS_NEW, c("Continue", "threshold_blow")),
        nar("threshold_blow", THRESHOLD_BLOW, *mornings),
    ]


physical("irabeth.trickster.commit", "Off the record", '"Knight-Captain. Off the record."', [
    i("start", '''{n}Late. The throne room is empty but for the two of you and the sword she will not let out of reach.{/n}
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
      c("Continue", "answer", forbids=(SHARES,)),       # retired by gating (index kept): the ask now sets ASKED
      c("Continue", "answer", flags=(ASKED,))),
    i("answer", '''{n}She waits for you to say it. Her sword hand is very still.{/n}''',
      c('[Salute] "Dismissed, Knight-Captain. For tonight."', flags=("irabeth.trickster.friends",)),
      c('"Something\'s stopping you. Say it."', "no", requires=("anevia_gone",), forbids=(A_RET,)),
      c('"Something\'s stopping you. Say it."', "no_home", requires=(SHARES,)),
      c('[Kiss her] "Irabeth." {n}Not her rank. Her name.{/n}', "reckon", requires=(SHARES,), forbids=(LIED,),
        flags=("irabeth.committed",)),
      c('[Wait for her to decide] "Whatever you want. Not an order."', "decides", requires=(SHARES,)),
      c('"Something\'s stopping you. Say it."', "no_gate", requires=(A_RET,), forbids=(SHARES,)),
      c('"Something\'s stopping you. Say it."', "no_house", forbids=("anevia_gone",))),
    i("no", '''"Nevi's out on that road. I'm not doing this behind her back. Not while she's out there. Maybe not after."
{n}She looks at the empty throne, not at you.{/n}
"Ask me when she's home, and ask me like a person, not like a Commander. Until then I'm your knight, and that's all I am."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("no_home", '''"It isn't Nevi. Nevi said her piece; I asked her to her face and she said yes before I'd finished."
{n}She turns the sword a quarter-turn in its scabbard at her hip, the only fidget she allows herself.{/n}
"It's me. I was a name on the list of the dead, Commander. Give me time to be alive before you ask me to be anything else."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("no_house", '''"Nevi. She's four streets off, in the house on the corner, making up a bed I haven't slept in since Iz. I haven't asked her. I'm not doing this behind her back, and I'm not doing it by letter when I could walk there before the bell."
{n}She turns the sword a quarter-turn in its scabbard at her hip, the only fidget she allows herself.{/n}
"I'll ask her. To her face. Then you can ask me again, and I'll know what I'm answering."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("no_gate", '''"Nevi's at the gate, and she hasn't said a word to me about you. Not one. She's a spy; that silence is a message, and I haven't read it yet."
{n}She rests her hand on the hilt at her hip.{/n}
"I'm not doing this behind her back. When she's said her piece to me, to my face, ask me again."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("decides", '''"Not an order."
{n}She comes round the desk and takes your face in both hands.{/n}''',
      c("Continue", "reckon", forbids=(LIED,), flags=("irabeth.committed",)),
      c("Continue", "not_tonight", requires=(LIED,))),
    i("not_tonight", '''"No. Not tonight."
{n}She says it evenly, the way she reports a loss.{/n}
"You told me a story about Iz, and I let you, because I wanted to be alive more than I wanted to be right. I'm not deciding anything else on a story. Ask me again when you've told me the other one."''',
      c('[Step back] "Then I\'ll ask again. Not as your Commander."', flags=(DECLINED,))),
    i("reckon", '''{n}She doesn't move yet. The sword is at her hip; it is always at her hip.{/n}
"Before anything. I came back to a vow I can't set down and a wife who'd already buried me. Some of that's your fault, and I'm not thanking you for it."
{n}She looks at her sword hand, then at you, and her mouth goes crooked.{/n}
"This isn't thanks. Don't you dare take it for thanks."''',
      c("Continue", "reckon_blow", requires=(BLOW,)), c("Continue", "threshold", forbids=(BLOW,))),
    i("reckon_blow", '''"And I remember your blow landing. I'll remember it tomorrow, and the day after. I'm here anyway. Work out what that says about me on your own time."''',
      c("Continue", "threshold", forbids=(BLOW,)),          # retired by gating (index kept): the blow has its own approach
      c("Continue", "reasons", requires=("irabeth.lover",)),
      c("Continue", "reasons_new", forbids=("irabeth.lover",))),
    i("reasons_new", REASONS_NEW, c("Continue", "threshold_blow")),
    i("reasons", REASONS_TEXT,
      c("Continue", "threshold_blow")),
    nar("threshold_blow", THRESHOLD_BLOW,
      c("Continue", "morning")),
    nar("threshold", THRESHOLD, c("Continue", "morning")),
    i("morning", MORNING_HOME, c('"Dismissed, Knight-Captain."')),
], requires=("trickster.ever", "irabeth.trickster.back_on_duty"), forbids=("irabeth.committed", DECLINED, BLOW), delay=24,
   ForbidOverrides={BLOW: TRUSTED})

physical("irabeth.trickster.second_ask", "The pen", '"Knight-Captain. I\'m asking again."', [
    i("price", '''"You want to ask again. Not while you're holding that."
{n}She nods at your coat, at the inside pocket where the pen has lived since Iz. The pen you misplaced for two days, so her discharge could not be signed.{/n}
"You asked me once as my Commander, and I said no to my Commander. Ask twice with my discharge in your pocket and it stops being a question. Give it to me. I'll send it to Nevi. If she sends it back, the answer's no. If she keeps it, ask me."''',
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "sent",
        requires=("anevia_gone",), forbids=(A_RET,), flags=(SIGNED,)),
      c('"Some things I keep."', "refused", flags=("irabeth.closed",)),
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "sent_gate",
        requires=(SHARES,), flags=(SIGNED,)),
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "held",
        requires=(A_RET,), forbids=(SHARES,)),
      c('[Hand her the pen] "It\'s yours. So is the discharge. Nevi decides."', "sent_home",
        forbids=("anevia_gone",), flags=(SIGNED,))),
    i("refused", '''"Then you're my Commander, and that's the end of it."
{n}She salutes, exactly as the regulations describe, and goes back to her post. The pen stays in your pocket. So does every order you ever gave her.{/n}''',
      c('"Understood."')),
    i("sent", '''{n}She wraps the pen in a strip of oilcloth, seals it with her own seal, and walks it down to the south-road courier herself. She makes him learn a message by heart, and she will not tell you what it says.{/n}
"Three days there and back, if the rider changes horses at Kenabres. Don't ask me in the meantime. I'll know which way it went when he's standing in front of me."''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered"),
        forbids=("irabeth.trickster.back_on_duty",)),   # retired by gating (index kept): the reply is its own scene now
      c('"Three days, then."', flags=(PEN_SENT,))),
    nar("threshold", THRESHOLD, c("Continue", "morning", requires=("anevia_gone",), forbids=(A_RET,)),
        c("Continue", "morning_home", requires=(A_RET,)), c("Continue", "morning_house", forbids=("anevia_gone",))),
    i("morning", MORNING_NOTE, c('"Dismissed, Knight-Captain."')),
    i("sent_gate", '''{n}She is back within the hour, empty-handed, with mud from the gate road on her boots.{/n}
"She didn't laugh. She turned it over, and put it in her boot. Then she told me to go back up the hill before she changed her mind about both of us."
{n}She holds out her empty hand to show you, as if the absence were the report. Then she smiles, and you realise you have not seen it since Iz.{/n}''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered"),
        forbids=(SHARES,)),                             # retired by gating (index kept): the ask now sets ASKED
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered", ASKED),
        forbids=("irabeth.trickster.back_on_duty",)),     # retired by gating (index kept): her own answer follows
      c("Continue", "her_answer", flags=("irabeth.trickster.nevi_answered", ASKED))),
    i("held", '''{n}She takes the pen, weighs it, and slides it into the cuff of her gauntlet instead of sending it.{/n}
"Nevi's at the gate and hasn't said her piece. I'm not walking your pen out to her before she has. That's not how it goes, not with her."
{n}She taps the cuff once.{/n}
"It stays here until she speaks. Then I'll carry it out to her myself."''',
      c('"Then we wait for her."', abort=True)),
    i("morning_home", MORNING_HOME, c('"Dismissed, Knight-Captain."')),
    i("sent_home", '''{n}She is back before the bell, with flour on her sleeve and the pen gone.{/n}
"She was baking. Nevi doesn't bake. She was baking because she knew I'd come. She took it out of my hand before I'd said a word, stuck it behind her ear and went on kneading. Then she said, 'Took you long enough, Beth,' and threw me out."
{n}She holds out her empty hand as if the absence were the report. Then she smiles, and you realise you have not seen it since Iz.{/n}''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered", ASKED),
        forbids=("irabeth.trickster.back_on_duty",)),     # retired by gating (index kept): her own answer follows
      c("Continue", "her_answer", flags=("irabeth.trickster.nevi_answered", ASKED))),
    i("morning_house", MORNING_HOUSE, c('"Dismissed, Knight-Captain."')),
    *her_answer((c("Continue", "morning", requires=("anevia_gone",), forbids=(A_RET,)),
                 c("Continue", "morning_home", requires=(A_RET,)), c("Continue", "morning_house", forbids=("anevia_gone",)))),
], requires=("trickster.ever", DECLINED, "irabeth.trickster.back_on_duty"), forbids=("irabeth.committed", LIED),
   delay=24, ForbidOverrides={LIED: CONFESSED})

# Sol BEL: a lie about Iz is not forgiven by omission. She said "Ask me again when you've told me the other one."
physical("irabeth.trickster.the_other_story", "The other story", '"Knight-Captain. About Iz."', [
    i("start", '''{n}She is at her post. She does not turn round when you come up beside her.{/n}
"If this is another story, Commander, save it for the Queen's envoy. He likes them."''',
      c('[Tell her the other one] "It wasn\'t the dragon. It was me. I meant it."', "told"),
      c('"No story. I came to stand the watch with you."', abort=True)),
    i("told", '''{n}She hears it at attention, eyes front, the way she took the news from Kenabres. When you have finished she stays that way.{/n}
"I knew. I've known since the ruin. I wanted to hear you say it without a sword in it."
{n}She breathes out through her nose, once.{/n}
"That's the story I'll decide on. Ask me again when you like. I haven't said what I'll say."''',
      c('"Understood, Knight-Captain."', flags=(CONFESSED,))),
], requires=("trickster.ever", RETURNED, LIED, DECLINED, "irabeth.trickster.back_on_duty"),
   forbids=(CONFESSED, "irabeth.committed"), delay=48)

# Sol HOW: the courier's five days are real hours, not a line of narration inside one scene.
physical("irabeth.trickster.nevi_reply", "Keeping it", '"The south-road courier is back."', [
    i("start", '''{n}It is three days before she finds you again. The courier from the south road brought nothing back: no pen, no packet. Only a message he had been made to learn by heart and would not say until the Knight-Captain was standing in front of him.{/n}
"'Keeping it. Ask me to my face next time, Beth.'"
{n}She tells you it as the courier told it, flat, and then she smiles, and you realise you have not seen it since Iz.{/n}''',
      c("Continue", "threshold", flags=("irabeth.committed", "irabeth.trickster.nevi_answered", ASKED),
        forbids=(PEN_SENT,)),                             # retired by gating (index kept): her own answer follows
      c("Continue", "her_answer", flags=("irabeth.trickster.nevi_answered", ASKED))),
    nar("threshold", THRESHOLD, c("Continue", "morning")),
    i("morning", MORNING_NOTE, c('"Dismissed, Knight-Captain."')),
    *her_answer((c("Continue", "morning"),)),
], requires=("trickster.ever", PEN_SENT), forbids=("irabeth.committed", "irabeth.trickster.asked_as_commander"), delay=72)


# --- Epilogue: one page, or paragraphs on her registered ending ----------------------------------------------------

UNDER_ORDERS_PARAGRAPHS = (
    p("{n}She had come back because she was still on the Drezen roster, and she stayed under a vow she had sworn over "
      "Teodor Vell's bier. His sword never left her side until the Wound was shut. Then she carried it to his mother in "
      "Nerosyan herself, and stood in the doorway with her helmet under her arm until she was let in.{/n}", requires=(VELL,),
      forbids=(BOUGHT,)),
    p("{n}She had come back because she was still on the Drezen roster, on a diamond the crusade could not spare. Teodor "
      "Vell, called back the same night, served in her company for the rest of the war and never learned what the second "
      "stone had cost; she saw to that, and saw to it that the company ate.{/n}", requires=(BOUGHT,)),
    p("{n}She had come back remembering two things at once: the Commander's blow, and the step. She never pretended the "
      "first had not happened. She taught the step to every recruit who would hold their ground long enough to learn it.{/n}", requires=(BLOW,),
      forbids=(LIED, K_RAISED)),
    p("{n}The chapel's book of Iz kept both lines under her name for as long as there was a chapel in Drezen: struck down "
      "by the Commander, called back on the Commander's order. She read them once a year, on the day, and never asked "
      "for either to be struck.{/n}", requires=(K_RAISED,)),
    p("{n}She served out the war exactly, and not one hour more. Of what happened at Iz she said only that the dragon had "
      "been blamed for enough already.{/n}", requires=(LIED,)),
    p("{n}When the Wound closed, she kept her vow to the hour and set the sword down at last. Anevia took the "
      "Commander's pen from wherever she had kept it through the war and handed it to her wife without a word. Irabeth signed her own discharge "
      "with it, and put it in her pocket instead of the roster. What she "
      "did with the free hand was her own business, and she made sure everyone understood that.{/n}", requires=(SIGNED,)),
    p("{n}When the Wound closed, Irabeth Tirabade put her sword down at last, flexed the hand, and asked the Commander "
      "the question she had been saving: not as a knight, and not under orders. She asked it out loud, in the kitchen "
      "of the house on the corner, with Anevia leaning in the doorway to hear it first.{/n}", requires=("irabeth.trickster.late_committed",),
      forbids=("irabeth.committed", "irabeth.closed", DECLINED, "irabeth.trickster.friends", "anevia_gone")),
    p("{n}When the Wound closed, Irabeth Tirabade put her sword down at last, walked out of the gate to where her wife was "
      "waiting on the road side of the line, and came back with an answer from both of them. She asked the Commander "
      "the question she had been saving: not as a knight, and not under orders.{/n}", requires=("irabeth.trickster.late_committed", A_RET),
      forbids=("irabeth.committed", "irabeth.closed", DECLINED, "irabeth.trickster.friends")),
    p("{n}The south-road courier caught her up after the Wound was closed, with the answer she had sent him for. Nevi had "
      "kept the pen. Irabeth went to find the Commander "
      "without her sword.{/n}", requires=(PEN_SENT,), forbids=("irabeth.committed", "irabeth.closed")),
    p("{n}She stayed the Commander's knight until the Wound was closed: loyal, exact, and never once off the record.{/n} "
      "{n}The pen stayed with Nevi.{/n}", requires=("irabeth.trickster.asked_as_commander",), forbids=("irabeth.committed",)),
    p("{n}She stayed the Commander's knight until the Wound was closed: loyal, exact, and never once off the record.{/n}",
      requires=(DECLINED,), forbids=("irabeth.committed", "irabeth.closed", "irabeth.trickster.asked_as_commander")),
    p("{n}She stayed the Commander's knight, and that was all. When the discharge was finally signed she saluted, took "
      "it, and did not look back.{/n}", requires=("irabeth.closed",)),
    p("{n}She and the Commander stayed what they had agreed to be on the night of the salute: a Knight-Captain and her "
      "Commander, who knew exactly how far the other would go.{/n}", requires=("irabeth.trickster.friends",),
      forbids=("irabeth.committed", "irabeth.closed")),
)

SCENES.append(scene("irabeth.trickster.epilogue.under_orders", "Until the Wound is shut", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}Irabeth Tirabade served the crusade until the Worldwound was closed. She had sworn not to stop sooner, and she kept her word to the letter, complaining about it at length, in writing, to anyone who would file it.{/n}''',
      portrait="Irabeth", paragraphs=UNDER_ORDERS_PARAGRAPHS)],
    requires=(RETURNED,), forbids=("irabeth.lover", "irabeth.committed", "trying", "committed"), last=99, Relationship="irabeth",
    ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))

SCENES.append(scene("irabeth.trickster.epilogue.off_the_record", "Off the record", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}Irabeth Tirabade served the crusade until the Worldwound was closed, and the Commander's bed when she was off duty, and she never once confused the two in front of the guard. She kept her own quarters, her own roster and her own counsel, and she argued with the Commander in council exactly as hard as before, which was very hard.{/n}
{n}When the war was over she did not ask for a title or a manor. She asked for a week, the three of them or the two of them as the house on the corner saw fit, with no duty lists in it, and she got it.{/n}''',
      portrait="Irabeth", paragraphs=UNDER_ORDERS_PARAGRAPHS)],
    requires=(RETURNED, "irabeth.committed"), forbids=("irabeth.campaign_kept", "trying", "committed", "sacrifice"), last=99,
    Relationship="irabeth",
    ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed",
                     "sacrifice": "trickster.commander_back"}))


# E14d extension: her variant of the native Tirabade slide Cue_0311 (anevia_trickster.NATIVE_EPILOGUE_EDITS): Beth is back
# from Iz and Anevia never came back to Drezen ("No one ever saw her again" no longer holds). Anevia's own variants win
# once she has returned.
NATIVE_SOUTH = "irabeth.trickster.epilogue.native_tirabade_south"
SCENES.append(scene(NATIVE_SOUTH, "", "IrabethEpilogue", 6, "", [
    nar("page", '''{n}Anevia left Drezen at the Coronation a widow, quietly, leaving no notes or traces. She did not stay one for long: Irabeth came back from Iz, and the word went down the south road after her. Anevia never came back to Drezen, and nobody who knew her expected her to. But the Tirabades were not lost to each other, and a letter in Irabeth's square, slow hand went south with every courier until the Wound was closed.{/n}''', c())],
    requires=(RETURNED,), last=99, Relationship="irabeth"))


REACTIONS = [
    reaction("Seelah", "irabeth.trickster.dead.react_seelah", (RETURNED, "irabeth.trickster.seelah_prayed"),
             '''{n}Seelah does not sit down. She stands with her arms folded, and her holy symbol is in her fist.{/n}
"I asked the Inheritor to take her. I knelt in the mud at Iz and asked Her to welcome my sister into Her army. And you told the chaplain Irabeth was still on shift."
{n}Her voice cracks on the last word.{/n}
"I'm going to be angry with you for a week, Commander. Then I'm going to hug her until she complains."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone", KILLED), chapter=5, last=5,
             entry='"Irabeth is back."'),
    reaction("Galfrey", "irabeth.trickster.dead.react_galfrey", (RETURNED,),
             '''{n}Irabeth holds out a letter under the Queen's seal, in the Queen's own hand, and does not let go of it while you read.{/n}
"I wept for you in front of my knights, Knight Tirabade. I would do it again. You gave your life for mine at Iz, and I will not be told that the gift was a clerical error.
You owe me the dignity of an explanation. Your Commander owes me a better one.
Galfrey."
{n}She folds it along its creases and puts it inside her surcoat.{/n} "I've written mine. She's still waiting for yours, Commander."''',
             answer_list=HUB, speaker="Irabeth", portrait="Irabeth", entry='"Anything to report, Knight-Captain?"',
             forbids=("galfrey.dead", "galfrey.killed_by_commander", KILLED), chapter=5, last=5,
             delay=24, title="A letter under the Queen's seal", Chapters=[5], RequiresAnyGroups=[["irabeth.sacrificed"]]),
    # Q12 (Sol INT): the Queen who came back as Kitrane (galfrey.trickster.returned) cannot write under a seal she gave up.
    # She stops Irabeth in the market instead, and Irabeth reports it on her own hub: inline, no delivery.
    reaction("Irabeth", "irabeth.trickster.dead.react_kitrane", (RETURNED, "galfrey.trickster.returned"),
             '''"A knight of the Green Crows stopped me in the market this morning. Grey hood. Old sword." {n}Irabeth's voice is very level.{/n} "She looked at me the way she looks at a dispatch she's been waiting a week for, and she said, 'You were dead, Knight Tirabade. So was I. Neither of us is to make a habit of it.' Then she bought me a pie and walked off."
{n}She sets the pie, untouched, on the duty roster.{/n} "I've taken orders in that voice since I was a squire, Commander. I'm not going to say whose it is. I'm going to eat the pie."''',
             answer_list=HUB, forbids=(KILLED,), chapter=5, last=5, delay=24, entry='"Anything to report, Knight-Captain?"',
             Chapters=[5]),
    reaction("Irabeth", "irabeth.trickster.killed.react_kitrane", (RETURNED, KILLED, "galfrey.trickster.returned"),
             '''"A knight of the Green Crows stopped me in the market this morning. Grey hood. Old sword." {n}Irabeth's voice is very level.{/n} "She looked at the seam in my surcoat, and then at me, and she said, 'I am told your Commander struck you down at Iz and then had you brought back. I have been put down and taken up again myself, lately. It does less for one's opinion of the hand that did it than one would like.' Then she walked off."
{n}Her hand rests on the pommel at her hip.{/n} "I've taken orders in that voice since I was a squire, Commander. I'm not going to say whose it is. I'm going to think about what she said for a week."''',
             answer_list=HUB, chapter=5, last=5, delay=24, entry='"Anything to report, Knight-Captain?"', Chapters=[5]),
    reaction("Seelah", "irabeth.trickster.killed.react_seelah", ("irabeth.trickster.blow_rewritten",),
             '''{n}Seelah's hands are shaking. She hides them behind her back, the way she did as a novice.{/n}
"The sappers you sent back say they dug her out from under a lintel with your blow's wound in her side. She says she stepped, the way you taught her, and that's why it missed her heart."
"You taught her to dodge you, Commander. Before Iz. I'm going to pray about what that means. And then I'm going to hit you."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone"), chapter=5, last=5,
             entry='"Irabeth is back."'),
    reaction("Seelah", "irabeth.trickster.killed.react_seelah_raised", (RETURNED, K_RAISED),
             '''{n}Seelah has the chapel's book of Iz open on her knees. She has plainly been reading the same page for some time.{/n}
"'Struck down by the Commander.' And under it: 'Called back on the Commander's order, the Commander's confession entered above.' Same ink. Same hand. The chaplain says you stood over him while he wrote it, and paid the Queen's jeweller for the diamond himself." {n}She closes the book.{/n}
"You killed my sister, and then you went and told the Inheritor so, in writing, so she'd come back. I don't know what to do with that, Commander. I'm going to pray until I do. And then I'm going to hit you."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone", "irabeth.trickster.blow_rewritten"), chapter=5, last=5,
             entry='"Irabeth is back."',
             ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"}),
]
SCENES.extend(REACTIONS)

# G6(b): her registered endings that Forbid irabeth_dead lift it once she has returned; G6(a): the loss page does not.
# G6(b): her scenes that Forbid anevia_gone lift it once Anevia has returned.
ANEVIA_GONE_LIFTED = ("irabeth.one_truth_to_tell", "irabeth.anevias_answer", "irabeth.the_evening_she_chose",
                      "irabeth.a_day_of_our_own", "irabeth.after_the_shared_answer")
RETURNING_ENDINGS = ("irabeth.anevias_answer", "irabeth.ending_lasting", "irabeth.ending_open", "irabeth.ending_friends",
                     "irabeth.ending_unfinished", "irabeth.ending_changed", "irabeth.ending_ascent", "irabeth.ending_sacrifice")
# Sol COX: the shared finale's surviving Commander (trickster.commander_back) never gets the mourning page; the living
# endings that Forbid `sacrifice` lift it through that flag instead (as Dorgelinda and Eliandra do).
LIVING_ENDINGS = ("irabeth.ending_lasting", "irabeth.ending_open", "irabeth.ending_friends", "irabeth.ending_unfinished")


def integrate(payload):
    """Save-safe edits to the registered route (no id, node or choice changes): relationship patch, presence, grief
    overrides, the under-orders paragraphs on her registered endings, and the returned Irabeth kept out of her
    pre-Iz private scenes (they stay closed after IrabethDead, as before)."""
    rel = payload["Relationships"]["irabeth"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a fallen Irabeth is still on the Commander's roster, and the chapel "
                        "keeps a list of the dead it can call back. After the Coronation, look for her in the throne room.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    for key, cues in SEEN_CUES.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    ours = {s["Id"] for s in SCENES}
    for s in payload["Scenes"]:
        if s.get("Relationship") != "irabeth" or s["Id"] in ours:
            continue
        if s["Id"] in ANEVIA_GONE_LIFTED:
            s.setdefault("ForbidOverrides", {})["anevia_gone"] = A_RET
        if s["Id"] == "irabeth.ending_sacrifice":
            s["Forbids"].append("trickster.commander_back")
        if s["Id"] in LIVING_ENDINGS:
            s.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"
        if s["Id"] == "irabeth.ending_unfinished":
            s["Forbids"].append("irabeth.trickster.recommitted")
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


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'irabeth.trickster.dead.relieved_not_dismissed',
    'irabeth.trickster.killed.blow_missed',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
