"""Anevia on the Trickster path: the wardrobe in Kenabres (Writer/handoffs/trickster/anevia.md, family F01 Closets).

Canon: at the Coronation, with Irabeth dead, Anevia says "This is where my crusade ends, Commander. Without Beth, I don't
belong here." and looks as if she wants to add something, then turns away (Coronation/Cue_0421 575f7925). AneviaGone
09f46662 starts AneviaNotInDrezen 6125c108, which hides her capital unit at once. Socothbenoth loves closets ("You can
hide in a closet and peep through its doors", SocothBriefing/Cue_0010 53de89fc) and gives the Commander his treasure
closet ("You have earned the right to use this closet!", Cue_0001 dde6e995). Anevia's Trickster trust: "Your crazy
stunts somehow make me think that, just maybe, this whole nightmare might suddenly end, by pure fluke, on a positive
note" (NPC_Common/Anevia/Cue_0071 8e206818). Where she goes is authored: canon says only that she leaves. She goes back
to Kenabres, to the Defender's Heart, the tavern where the crusaders held out and where the Commander once slept.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
ANEVIA = "b5e867e13503c6f41bb1316705efb4a2"             # AneviaTirabade_DrezenCapital (AneviaNotInDrezen only hides it)
HUB = "33960c7f7af40cd43b7f801a76c87a0b"                # NPC_Common/Anevia/AnswersList_0003
SMITH = "15f754455d1d87c42a4e14df456d5415"              # BlacksmithCapitalTrader, the forge by the gate (E12b anchor)
KONOMI_OFFICER = "0dc8b8604bb33c846a63f3eb62443674"     # Crusade/RankUps/Diplomacy/Diplomacy_Officer/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"         # CompanionDialogues/Woljif/AnswersList_0003

PRIMED = "anevia.trickster.primed"
RETURNED = "anevia.trickster.returned"
DECLINED = "anevia.trickster.declined"
GATE = "anevia.trickster.gate_seen"
LISTEN = "anevia.trickster.cost.socoth_listening"
WRONG = "anevia.trickster.cost.wrong_door"
STOLEN = "anevia.trickster.cost.stolen_door"
CRATED = "anevia.trickster.cost.crated"
NAILED = "anevia.trickster.cost.wardrobe_nailed"
THROWN = "anevia.trickster.cost.thrown_out"
KEY = "anevia.trickster.cost.her_key"
BARGAIN = "anevia.trickster.cost.knows_the_bargain"
ACCOUNT = "anevia.trickster.cost.accounting"
EXPOSED = "anevia.trickster.cost.lie_exposed"
JOKE_TOLD = "anevia.trickster.told_the_joke"
TERMS = "anevia.trickster.terms_kept"
FRIENDS = "anevia.trickster.friends"
SHARES = "anevia.trickster.shares_beth"
I_RET = "irabeth.trickster.returned"
I_DECLINED = "irabeth.trickster.declined"
I_REWRITTEN = "irabeth.trickster.blow_rewritten"
I_LIED = "irabeth.trickster.cost.accounting_lied"
I_UNDER = "irabeth.trickster.cost.under_orders"
I_ASKED = "irabeth.trickster.asked_nevi"         # Irabeth asked Anevia herself (her commit's "talked", or the pen)
KILLED = "anevia.irabeth_killed_by_commander"
LEFT = "irabeth_gone"                            # native IrabethGone: both Tirabades left at the Coronation, Beth alive
SAID = "anevia.trickster.said_it"                # Sol r1 BEL: the murder named to her face, and her penance paid
PENANCE = "anevia.trickster.cost.muster_confession"
OUTLIVED = ("socot.gone", "council.fought", "council.fought_nocta_allied")
OWN = ("anevia.closed",)

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={"anevia_gone": RETURNED},
    TricksterAccess={"gone": dict(detect=["anevia_gone"], device="anevia.trickster.gone.setup", returned=RETURNED)})
PRESENCES = {
    # Her capital actor is hidden by AneviaNotInDrezen; reuse-native unhides it out on the road side of the smithy by the
    # gate, seven paces in front of the smith (polish b6b: clear of Gesmerha and Hepzamirah at his sides; he watches her
    # over his anvil). She will not come inside: the gate is the line she chose. An unresolved anchor raises
    # anevia.presence.failed.
    "anevia.presence": dict(Unit=ANEVIA, Area=DREZEN, Mode="reuse-native",
                            At=dict(NearUnit=SMITH, Side="front", Distance=7.0),
                            Requires=["trickster.ever", RETURNED], Forbids=["anevia.closed"],
                            MinChapter=5, MaxChapter=5, AnswerLists=[HUB]),
}


def physical(id, title, entry, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Anevia", 5, entry, nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="anevia", Areas=[DREZEN], Chapters=[5], ContactUnit=ANEVIA,
                        AnswerLists=[HUB], **extra))


def letter(id, title, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Anevia", 5, "", nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="anevia", Chapters=[5], Remote=True, **extra))


def a(id, text, *choices):
    return n(id, "Anevia", text, *choices, portrait="Anevia")


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices, portrait="Anevia")


def to_beth(back, widow, forbids=(), killer=None, left=None):
    """Continue to the Beth-first page that fits Irabeth's state: back from the dead, dead by the Commander's own
    sword (when the scene has a page for it), dead, or (left=) alive and gone with Anevia since the Coronation. The
    left page is appended last so the older choice indices stay where they were."""
    gone = (LEFT,) if left else ()
    tail = (c("Continue", left, requires=(LEFT,), forbids=(*forbids, I_RET)),) if left else ()
    if killer is None:
        return (c("Continue", back, requires=(I_RET,), forbids=forbids),
                c("Continue", widow, forbids=(*forbids, I_RET, *gone)), *tail)
    return (c("Continue", back, requires=(I_RET,), forbids=forbids),
            c("Continue", killer, requires=(KILLED,), forbids=(*forbids, I_RET, *gone)),
            c("Continue", widow, forbids=(*forbids, I_RET, KILLED, *gone)), *tail)


# --- State gone_after_coronation: the wardrobe in Kenabres -----------------------------------------------------------

# Remote by design: Coronation Cue_0421 has no answer list and its OnShow starts AneviaGone, which hides her unit at
# once, so there is no native moment to hook. The letter is delivered by the post bag from the Coronation on. The paid knock needs a Socothbenoth who is still at the Council;
# the kept closet needs his doctrine heard (Cue_0011) and his absence; with neither, the Commander is posted south.
letter("anevia.trickster.gone.setup", "Don't", [
    nar("start", '''{n}Her rooms in the citadel are empty by nightfall. She took her knives and her good boots and left the rest: the bed made to regulation, Beth's spare surcoat folded over the chair, and the wardrobe standing open, the way you leave a door for someone you have decided will not come.{/n}
{n}At the Coronation she looked as if she meant to say something more, then pressed her lips together and turned away. Pinned inside the wardrobe door, in her plain, upright hand, is the something more. It is one word.{/n}
"Don't."''',
      c('[Knock on the back of the wardrobe and ask his price] "A door to wherever she\'s sleeping tonight. Name it."',
        "socoth", forbids=OUTLIVED),
      c('[Knock on the back of the wardrobe]', "door", requires=("closets.door_kept",)),
      c('[Knock on the back of the wardrobe]', "crate", requires=("anevia.socoth_absent",), forbids=("closets.door_kept",)),
      c('[Fold the note away] "Not yet."', abort=True)),
    n("socoth", "Socothbenoth", '''{n}You knock. Among the hangers, something laughs, and the laugh smells of attar of roses.{/n}
"A spymaster's bedroom in Kenabres, and she has told you in writing not to come? Oh, darling, you've brought me a present. Do you know how rarely anyone knocks? People simply barge through my closets as if they were corridors."
{n}The voice comes from the dark at the back of the wardrobe, where there ought to be nothing but cedar.{/n}
"My price is small. My side of the door stays open. Whatever is said in that room, I hear it: every sigh, every quarrel, every creak of the bed, if you're lucky. I'm not ashamed of wanting it, and you shouldn't be ashamed of paying it."''',
      c('[Pay it] "Done. Open the door."', "paid", mythic="Trickster", alignment=("Chaotic", 1), forbids=OUTLIVED,
        flags=(PRIMED, "anevia.started", LISTEN)),
      c('[Haggle] "One door. No audience. I\'ll owe you a story instead."', "haggled", mythic="Trickster",
        forbids=OUTLIVED, flags=(PRIMED, "anevia.started", WRONG))),
    n("paid", "Socothbenoth", '''"Splendid. Give me a day to find the right wardrobe; a spy on the road doesn't sleep in the same room twice. When the door opens, walk in as if you owned the place."
{n}The laugh again, further off.{/n}
"You don't, of course. I do."''',
      c('"A day, then."')),
    n("haggled", "Socothbenoth", '''"A story? From *you*? Accepted, darling. You'll tell it to me in a closet one day, and I'll decide whether it was worth the door."
{n}A pause, and the rustle of silk being arranged to its best advantage.{/n}
"And since you've haggled with me in my own closet, I choose which wardrobe opens first. Consider it a small tour of the sillier bedrooms of Mendev."''',
      c('"...Fine."')),
    nar("door", '''{n}You knock. Nobody answers. The Silken Sin's closets have been quiet since he quit the Council.{/n}
{n}But the closet he gave you is still yours. "You have earned the right to use this closet," he said, and patted its door like a favourite horse. It opens only onto rooms you have stood in. Her letter to the quartermaster, the one she thinks nobody read, is addressed "the Heart, upstairs, the room the Commander slept in, since nobody else will take it": the room over the taproom where you slept the night the crusaders held the Defender's Heart.{/n}
{n}Stepping through will cost you the war council tomorrow. Your sealed notice goes on the council docket before you step through. The adjutant will read it to people who do not believe in closets.{/n}''',
      c('[Open the closet Socothbenoth gave you] "He said I\'d earned it. Let\'s find out what for."', "door_open",
        mythic="Trickster", crusade=("Favors", -100), requires=("closets.door_kept", "trickster"),
        flags=(PRIMED, "anevia.started", STOLEN))),
    nar("door_open", '''{n}You do not open it. A closet that opens onto a room once is a closet you want to open onto the right room, at the right hour, with the tavern asleep below. You rest your palm on the cedar and give the Heart until tomorrow night to close.{/n}''',
      c('"Tomorrow."')),
    nar("crate", '''{n}You knock. Nobody answers, and no closet of yours opens onto anything but coats.{/n}
{n}The quartermaster's wagon for the south leaves at dawn, and Anevia still gets her post the way she always has: through a dead drop at the Defender's Heart in Kenabres, the third crate from the back. It is, technically, a very large dead drop.{/n}''',
      c('[Nail yourself into a supply crate addressed to her dead drop] "She taught me dead drops. Let\'s see if they take live mail."',
        "crated", mythic="Trickster", crusade=("Materials", -100), requires=("anevia.socoth_absent",),
        forbids=("closets.door_kept",), flags=(PRIMED, "anevia.started", CRATED))),
    nar("crated", '''{n}The quartermaster signs for one crate of "salt pork, Commander's personal", looks at the air holes, looks at you, and decides he has not seen the air holes. Three wagons of rations go south short that week. Somebody will have to make up the difference.{/n}''',
      c('"Mind the bumps."')),
], requires=("trickster", "anevia_gone"), forbids=(PRIMED, RETURNED), delay=0,
   RequiresAnyGroups=[["closets.known", "socot.gone", "council.expired"]], TricksterDevice=True, TricksterState="gone")

CANDLE = '''"Get out."
{n}She doesn't move. Neither does the knife.{/n}
"...No. Sit. You've got till the candle's done. Then you go back in there, and I'm nailin' it shut."'''

letter("anevia.trickster.gone.wardrobe", "A live drop", [
    nar("start", '''{n}Kenabres. What the demons left of the Defender's Heart still has its upstairs rooms, and one of them is rented by the week to a woman who paid in advance and gave no name.{/n}''',
      c("Continue", "wrong", requires=(WRONG,)),
      c("Continue", "hinges", forbids=(WRONG, CRATED)),
      c("Continue", "lid", requires=(CRATED,))),
    nar("wrong", '''{n}It is the fourth wardrobe. The first three belonged to a chandler, a convent, and a magistrate who was not alone and was very surprised. You have a wimple on your head and do not know how it got there.{/n}''',
      c("Continue", "hinges")),
    a("hinges", '''{n}This one smells of cedar and somebody else's winter coats. Its door opens from the inside, onto a narrow room over the taproom. Anevia is sitting on the bed with a knife in her hand. She has had it there since the hinges creaked.{/n}
"I rode outta Drezen to be somewhere you weren't. Clearly didn't ride far enough."''',
      c('[Step out of the wardrobe with your hands up] "You taught me dead drops. This is a live one."', "candle",
        mythic="Trickster")),
    a("lid", '''{n}The crate lid comes up an inch at a time. Anevia is on the other side of it, in a cellar that smells of spilled ale, with a pry bar in one hand and a knife in the other.{/n}
"I rode outta Drezen to be somewhere you weren't. Clearly didn't ride far enough."''',
      c('[Climb out with your hands up] "You taught me dead drops. This is a live one."', "candle_crate",
        mythic="Trickster")),
    a("candle", CANDLE,
      c("Continue", "wimple", requires=(WRONG,)),
      c("Continue", "stolen", requires=(STOLEN,)),
      *to_beth("beth_back", "beth_dead", forbids=(WRONG, STOLEN), killer="killer", left="beth_left")),
    a("candle_crate", '''"Get out."
{n}She doesn't move. Neither does the knife.{/n}
"...No. Sit. On the crate, where I can see you. You've got till the candle's done. Then you go back in, and I'm nailin' the lid on and postin' you north as salt pork."''',
      *to_beth("beth_back", "beth_dead", killer="killer", left="beth_left")),
    a("wimple", '''"You're late, you smell of incense, and there's a wimple on your head. I'm not gonna ask."
{n}She asks with her eyebrows anyway.{/n}''',
      *to_beth("beth_back", "beth_dead", killer="killer", left="beth_left")),
    nar("stolen", '''{n}The closet door sighs shut behind you. It will not open onto this room a second time; you know it the way you know the cold.{/n}''',
      *to_beth("beth_back", "beth_dead", killer="killer", left="beth_left")),
    a("beth_back", '''"And don't tell me about Beth. I've had a letter. In her hand, sayin' she's back on watch in Drezen with a sword she's sworn to keep by her. I read it eleven times, and I still think it's a forgery."
{n}She looks at the knife as if she has only just noticed it.{/n}
"It's not a forgery. Is it."''',
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN,),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,))),
    a("beth_dead", '''"You came through furniture for me."
{n}Her voice does not rise. It gets quieter, which is worse.{/n}
"You didn't come through anythin' for Beth."''',
      c("Continue", "rest", requires=(I_DECLINED,)),
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN, I_DECLINED),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,),
        forbids=(I_DECLINED,))),
    a("rest", '''"...No. That's not fair. They told me. You could've done somethin', some trick, and you let her rest instead."
{n}She wipes her eyes with the back of the knife hand, carefully, blade out.{/n}
"Good. Somebody in this family should get to."''',
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN,),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,))),
    a("killer", '''{n}The report from Iz reached Kenabres before you did.{/n}
"You put your sword through my wife."
{n}The knife doesn't shake. Her voice does, once, and then it doesn't.{/n}
"And now you turn up where I went to get away from you, like it's a joke. Sit down. Not 'cause I forgive you. 'Cause I want to look at you while I decide what you are."''',
      c("Continue", "owned", requires=(I_DECLINED,)),
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN, I_DECLINED),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,),
        forbids=(I_DECLINED,))),
    a("owned", '''"They say you wouldn't let the chaplain write it any other way. That you stood there and said 'I did it' while he wrote."
{n}She turns the knife over, once, and looks at the blade instead of you.{/n}
"That's the only reason you're still breathin'."''',
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN,),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,))),
    a("named", '''{n}The candle burns down. She talks for most of it, about nothing: the price of a room in Kenabres, a dog in the street that barks at priests, how bad the ale has got. She never once puts the knife down.{/n}
{n}When the wick starts to gutter, she stands.{/n}
"Not here. Not anywhere with furniture. The Drezen gate, outside the walls. Give me two nights on the road. Ask the watch for my message when you get back. I'm not comin' in. You come out."''',
      c("Continue", "nail", forbids=(CRATED,)), c("Continue", "nail_crate", requires=(CRATED,))),
    a("thrown_out", '''{n}Anevia stops in the middle of a sentence and looks at the coats.{/n}
"Someone's breathin' in there. Not you."
{n}The coats go very still. It does not help.{/n}
"...You brought a *demon* to listen?"
{n}She doesn't wait for an answer. She is already reaching for the hammer.{/n}
"Out. Both of you. I'll leave word at the Drezen gate where I'll be. Don't come through anythin' to get there."''',
      c('[Go back into the wardrobe before the knife moves] "Going."', "nail",
        flags=(RETURNED, "anevia.started", NAILED, THROWN))),
    nar("nail", '''{n}When you step back into the wardrobe, you hear the first nail go in before the door has quite closed.{/n}''',
      c('"At the gate, then."')),
    nar("nail_crate", '''{n}You climb back into the crate. The first nail goes into the lid before you have finished folding your knees. Somewhere above, a voice you know tells a carter, very sweetly, that this one is going back north and that he is to hit every pothole on the road.{/n}''',
      c('"At the gate, then."')),
    # Both left at the Coronation (Cue_0310): Beth is alive, broken by the Commander's betrayal, and on the road with her.
    a("beth_left", '''"Keep your voice down. Beth's asleep through that wall. First time in three nights she's slept without the sword in her hand."
{n}She does not look at the wall. She looks at you, the way she looks at a man she has already decided to report.{/n}
"You came through furniture for me. For her you couldn't even keep faith in your own hall. Whatever you did to her in Drezen, she hasn't stood up straight since. I'm takin' her as far from Mendev as the roads go."''',
      c('[Sit until the candle\'s done] "Till the candle\'s done, then."', "named", forbids=(LISTEN,),
        flags=(RETURNED, "anevia.started", NAILED)),
      c('[Sit, and hope the coats keep quiet] "...Nobody else is here."', "thrown_out", requires=(LISTEN,))),
], requires=("trickster.ever", "anevia_gone", PRIMED), forbids=(RETURNED,), delay=24,
   TricksterDevice=True, TricksterState="gone")


# --- State gone_irabeth_returned: she wouldn't come back without me ------------------------------------------------

letter("anevia.trickster.gone.fetched", "Two letters and a bootlace", [
    nar("start", '''{n}Two letters come up the south road in one packet, tied together with a bootlace.{/n}''',
      c("Continue", "beth")),
    n("beth", "Irabeth", '''{n}The first is in Irabeth's hand, square and slow, pressed so hard the nib has gone through the paper twice.{/n}
"Found her. Kenabres, over what's left of the Heart. She threw a boot at me. Then the other boot. Coming home by the long road. Don't send anyone. I.T."''',
      c("Continue", "nevi"), portrait="Irabeth"),
    a("nevi", '''{n}The second is in Anevia's hand, and it isn't addressed to anyone.{/n}
"She walked into the Heart with a sword on her hip and her hand on it. Wouldn't take the hand off it to hold me. Held me anyway, one-armed, like an idiot, in front of the whole taproom. Said it was your fault."''',
      c("Continue", "bargain", requires=(I_UNDER,), forbids=(KILLED,)), c("Continue", "close", forbids=(I_UNDER, KILLED)),
      c("Continue", "killer_back", requires=(KILLED,))),
    a("killer_back", '''"She told me the rest on the road, 'cause I made her. You put your sword through her at Iz. Then you had the chaplain write it in his book in your own words, and spent some boy's diamond callin' her back to read it."
{n}The ink is heavier on the next line.{/n}
"I don't know what you are. I know she's alive, and it's your doin' both ways. I'm gonna need a while with that."''',
      c("Continue", "bargain", requires=(I_UNDER,)), c("Continue", "close", forbids=(I_UNDER,))),
    a("bargain", '''"She says the chaplain called her 'cause you told him she was still on your roster, and she came 'cause she was. She says somebody paid for it, and she's told me who, and I'm not puttin' it in a letter. She swore at the altar before she came up to you. Won't let it out of reach, not to eat, not to sleep, not to hold her wife with both arms. Not till the Wound's shut. She says it's cheap. She's lyin', and she knows I know."
{n}The ink is heavier on the next line.{/n}
"I'm grateful. Gods, I'm grateful. I'm also never lettin' you give me an order. Not one. Not even 'pass the salt'."''',
      c("Continue", "close")),
    a("close", '''"We're outside Drezen. Beth's got her sword out again; she says she's inspectin' the gate. She's missed it, the stubborn cow. I'll leave word with the watch. Come out when they tell you. I'm not sure yet I'll go any further."''',
      c('[Write back: stay at the edge of it] "I\'ll wait outside."', flags=(RETURNED, "anevia.started", BARGAIN)),
      c('[Write back: tell her it was a joke] "It was a joke, Anevia. The world laughed."',
        flags=(RETURNED, "anevia.started", BARGAIN, JOKE_TOLD))),
], requires=("trickster.ever", "anevia_gone", I_RET), forbids=(PRIMED, RETURNED, I_REWRITTEN), delay=24,
   TricksterDevice=True, TricksterState="gone")


# --- State gone_after_blow_rewritten: the confession stands --------------------------------------------------------

letter("anevia.trickster.gone.confession", "The version that hurts", [
    n("start", "Irabeth", '''{n}Irabeth brings the letter herself. She does not sit. She stands in the doorway with the sword in her hand and her eyes on the floor, as if she were reporting a loss.{/n}
"Nevi's at an inn a day south. She won't come any closer. She gave me this, and she said I'm to watch your face while you read it."''',
      c("Continue", "letter"), portrait="Irabeth"),
    a("letter", '''"She says she stepped. She also says she remembers your blade goin' in. I'm a spy, Commander. When a story's got two endings, I believe the one that hurts.
So you're gonna tell me. Your own words, in writing. Beth carries it back. And if it's the tidy version, I'll know."''',
      c('[Tell her everything] "I struck her down to kill. Then I sent men back to dig her out. Both are true."', "truth",
        flags=(RETURNED, "anevia.started", ACCOUNT, "anevia.trickster.heard_the_truth")),
      c('[Lie] "The report is right. She fell."', "exposed", requires=(I_LIED,))),
    n("truth", "Irabeth", '''{n}Irabeth reads it over your shoulder. She does not pretend otherwise. When she has finished she folds it once, very precisely, and puts it inside her breastplate.{/n}
"She'll come as far as the gate. That's what the truth buys, with Nevi. Not forgiveness. The gate."''',
      c('"Then I\'ll be at the gate."'), portrait="Irabeth"),
    a("exposed", '''{n}The answer comes back two days later, by the same hand. Irabeth will not look at you while you read it.{/n}
"Beth told me that one already. Same words. Same order. You two rehearsed it, and she's a worse liar than you, which is sayin' somethin'.
Don't write back. It's the most honest thing you'll do all week. I'll be at the gate anyway, 'cause she asked me to. Don't mistake it for anythin'."''',
      c('[Say nothing] "..."', flags=(RETURNED, "anevia.started", ACCOUNT, EXPOSED))),
], requires=("trickster.ever", "anevia_gone", I_REWRITTEN), forbids=(PRIMED, RETURNED), delay=24,
   TricksterDevice=True, TricksterState="gone")


# --- After the return: the gate, the commit, her no -----------------------------------------------------------------

BETH_WIDOW = '''"Beth used to stand watch right there. Left foot forward, 'cause of the old knee. I can't look at that gate without her in it."
{n}She doesn't look at it. She looks at you.{/n}
"So before you say anythin' soft: she comes first. She's always gonna come first. If that's a problem, go back in."'''
BETH_BACK = '''"Beth's inside those walls, givin' orders. I can hear her from here. And I'm out here, with you."
{n}She kicks at the mud line with the toe of her boot.{/n}
"Explain that to me, 'cause I can't. And before you try: she comes first. She's always gonna come first."'''
GATE_CHOICES = (
    c('[Take her hand and wait] "Tell me about her. I\'m listening."', "told", flags=(GATE, "anevia.trickster.hand_taken")),
    c('[Stay on your side of the line] "Your road. Your call."', "line", flags=(GATE, FRIENDS)))

physical("anevia.trickster.gone.gate", "The line in the mud", '"You said the gate. I came out."', [
    a("start", '''{n}Anevia is already waiting on the smith's side of the cart ruts. The relief sentries pass her without stopping. She waits for the hammer to strike, then calls you out of the gate's shadow.{/n}
"Here. Where I can see who's comin'."
{n}She has put the lantern on the road side, beside her boot. When you approach, she moves it farther from the citadel.{/n}
"You got your visit. This one's mine."''',
      c("Continue", "coats", requires=(THROWN,)),
      c("Continue", "joke", requires=(JOKE_TOLD,)),
      c("Continue", "one_truth", requires=(EXPOSED,)),
      *to_beth("beth_back", "beth_widow", forbids=(THROWN, JOKE_TOLD, EXPOSED), left="beth_left")),
    a("coats", '''"And the coats. Tell me the coats aren't listenin'."
{n}She glances at the guardhouse door, which has no coats behind it, and does not relax.{/n}''',
      *to_beth("beth_back", "beth_widow", left="beth_left")),
    a("joke", '''"You wrote me it was a joke. Beth read it over my shoulder and laughed till she cried. I didn't."''',
      *to_beth("beth_back", "beth_widow", left="beth_left")),
    a("one_truth", '''"One true thing tonight. Just one. Then we'll see."''',
      *to_beth("beth_back", "beth_widow", left="beth_left")),
    a("beth_widow", BETH_WIDOW, *GATE_CHOICES),
    a("beth_back", BETH_BACK, c("Continue", "beth_terms")),
    a("beth_terms", '''{n}She watches the gate a while longer. When she speaks again it is in her report voice, flat and exact, the one she uses for things she has already decided.{/n}
"And she looks at you. Don't pretend she doesn't; I know that look of hers. So here's my terms for that, too, same as mine. If Beth wants you, she asks me first. To my face. Not you askin' for her, not an order, not some trick. Her."
{n}She kicks the mud line once.{/n}
"And when she asks, I'll say yes. I'd rather share than bury. I've tried burying. I'm no good at it."''',
      c('[Take her hand and wait] "Tell me about her. I\'m listening."', "told", flags=(GATE, "anevia.trickster.hand_taken", SHARES)),
      c('[Stay on your side of the line] "Your road. Your call."', "line", flags=(GATE, FRIENDS, SHARES))),
    a("told", '''{n}So she tells you. Not the war: the small things. That Beth snores like a siege engine and denies it under oath. That she folds her socks in pairs and then, for no reason anyone has discovered, in threes. That she sang at their wedding, badly and on purpose, so Anevia would stop crying and laugh.{/n}
{n}The smith stops to inspect his work. Anevia falls silent with him, listening to the guard call the next watch. Her hand stays in yours.{/n}''',
      c('"I\'ll come back. Same gate?"')),
    a("line", '''{n}She nods once, the way she nods at a report that says what she expected.{/n}
"Good. Keep it that way till I say otherwise."''',
      c('"Understood."')),
    # Both left at the Coronation: Beth is alive and waiting down the road; nothing here speaks of her as dead.
    a("beth_left", '''"Beth's a day down the road, at an inn with a bad roof. She doesn't know I'm here. Or she does, and she's lettin' me pretend she doesn't. That's new. She never used to let anybody pretend anythin'."
{n}She kicks at the mud line with the toe of her boot.{/n}
"That's what you did to her. So before you say anythin' soft: she comes first. When she's ready to ride, I ride with her, and I won't be askin' you where to."''',
      c('[Take her hand and wait] "Tell me about her. I\'m listening."', "told_left", flags=(GATE, "anevia.trickster.hand_taken")),
      c('[Stay on your side of the line] "Your road. Your call."', "line", flags=(GATE, FRIENDS))),
    a("told_left", '''{n}So she tells you. Not the war: the small things. That Beth snores like a siege engine and denies it under oath. That she still folds her socks in pairs and then in threes, every night, even in a room she will leave at dawn. That last night she woke shouting a knight's name, and then apologised to the wall.{/n}
{n}Her hand stays in yours the whole time. She doesn't seem to notice. When she does, she doesn't let go.{/n}''',
      c('"I\'ll come back. Same gate?"')),
], requires=("trickster.ever", RETURNED), forbids=(GATE,), delay=48)

TERMS_TEXT = '''"Here's how it goes. I don't come inside. You come out. No closets, no wardrobes, no demons breathin' in the coats. You knock on a real door, like a person."
{n}She holds up one finger.{/n}
"And the first time you lie to me, I'm gone. And this time I'll be better at it."'''
THRESHOLD = '''{n}She doesn't wait for you to decide. She kisses you before the lantern stops swinging, both hands flat on your chest as if she were checking you for a knife, like someone who has been rationing it all the way up the road. Round the side of the gatehouse there is a real door. She raps on it twice with her knuckles, for form's sake, then kicks it shut behind you.{/n}
"Real door. I knocked. Now shut up and get that shirt off before I lose my nerve. And I never lose my nerve."
{n}Her fingers find every buckle on the first try, a spy's hands, and your coat hits the floor. She kicks your cloak out flat across the gatehouse floor, under the lantern hook, and takes the lantern down so she can see your face. Her breath is warm and ragged against your neck, one leg hooks hard round yours, and she drags you down onto the cloak with a sound that is half a laugh and half something she has not let herself say since the Coronation.{/n}'''

physical("anevia.trickster.gone.commit", "A real door", '"Same gate. Same line."', [
    a("start", '''{n}Same gate, same mud line, a colder night. She has brought a lantern and set it down on her side.{/n}
"Guard asked me if I was a deserter. Told him I'm retired. He didn't believe me either."''',
      c("Continue", "share", requires=(I_RET, I_ASKED)),
      c("Continue", "widow_killed", requires=(KILLED,), forbids=(I_RET,)),
      c("Continue", "widow", forbids=(I_RET, KILLED, LEFT)),
      c("Continue", "share_quiet", requires=(I_RET,), forbids=(I_ASKED,)),
      c("Continue", "left", requires=(LEFT,), forbids=(I_RET, KILLED))),
    a("widow", '''"I buried her in my head a hundred times on the road. Every time, you were standin' at the graveside with your hands in your pockets like you knew somethin'."
{n}She breathes out, and it smokes in the cold.{/n}
"You didn't. Nobody did. That's what makes it bearable."''',
      c('[Ask her to stay] "Stay. Not in there. Here, with me."', "terms"),
      c('[Say nothing and wait] "..."', "terms")),
    a("widow_killed", '''"I buried her in my head a hundred times on the road. Every time, it was your sword in her."
{n}She breathes out, and it smokes in the cold.{/n}
"I don't know what it says about me that I came back to this gate anyway. I'm not gonna pretend it doesn't say somethin'."
{n}She picks up the lantern and holds it between you, at the height of your face.{/n}
"So before anythin' else: say it. Not 'Iz'. Not 'the dragon'. Not 'what happened'. Say what you did."''',
      c('[Say it] "I killed her. At Iz. With my own hand."', "said"),
      c('[Ask her to stay] "Stay. Not in there. Here, with me."', "no"),
      c('[Say nothing and wait] "..."', "no")),
    a("said", '''{n}The lantern does not move for a long time.{/n}
"Nobody's said it to me like that. Everybody else says it sideways, like it's somethin' that fell on her."
{n}She sets the lantern down on her side of the line.{/n}
"I'm not forgivin' you. Not tonight. Maybe not ever. But you said it to my face, and I'm still standin' here, so I'd better hear the rest."''',
      c("Continue", "terms", forbids=(KILLED,)),          # retired by gating (index kept): her penance comes first
      c("Continue", "penance", requires=("anevia.lover",)),
      c("Continue", "stranger", forbids=("anevia.lover",))),
    a("stranger", '''"Here's the rest. Tomorrow at muster you say it again, in front of her knights. And that's all you'll ever have from me: a widow who knows what you did and says it back to you whenever she likes. You were never anythin' to me before Iz, Commander. You don't get to be somethin' now 'cause you found a way to follow me."''',
      c('[Accept it] "Then that\'s what I am to you."', flags=(FRIENDS,)),
      c('[Refuse] "Not in front of them."', "no")),
    a("penance", '''"Here's the rest. Tomorrow, at muster, in the yard, in front of every knight who carried her out of Iz, you say it again. Same words. Your mouth, not a clerk's. Then you stand there while they look at you."
{n}She lifts the lantern an inch, so she can see all of your face.{/n}
"And don't ask me why I haven't walked yet. I don't know. I'll find out on the wall, watchin' you say it."''',
      c('[Agree] "Tomorrow, at muster. My mouth."', "terms", flags=(SAID, PENANCE), forbids=(KILLED,)),   # retired
      c('[Refuse] "Not in front of them."', "no"),
      c('[Agree] "Tomorrow, at muster. My mouth."', "promise", flags=(SAID,))),
    a("promise", '''"Then say it. After, come out to the gate. Not before, and not instead."
{n}She picks up the lantern and walks back down the road without looking round.{/n}''',
      c('"After muster."')),
    a("share", '''"Beth asked me. Like I said she had to: to my face, in the gatehouse, with her helmet under her arm like she was reportin' a fire. I said yes. Then she went red and walked into a door."
{n}She lets that sit.{/n}
"So."''',
      c('[Ask her to stay] "Stay. Not in there. Here, with me."', "terms"),
      c('[Say nothing and wait] "..."', "terms")),
    a("share_quiet", '''"Beth's inside those walls givin' orders, and she hasn't said one word to me about you. I told her she'd have to ask me first, if she ever wanted to. She hasn't asked. Could be she never will. That's hers."
{n}She lets that sit.{/n}
"So this is about me. Just me. Say what you came out here to say."''',
      c('[Ask her to stay] "Stay. Not in there. Here, with me."', "terms"),
      c('[Say nothing and wait] "..."', "terms")),
    a("terms", TERMS_TEXT,
      c('[Agree to her terms] "A real door. No coats. No lies."', "answer"),
      c('[Tell her you need her inside the walls] "Drezen needs its spymaster. I need her."', "no")),
    a("answer", '''"...Fine."
{n}She picks the lantern up, then sets it down again on your side of the line.{/n}
"Then come here, before I think better of it."''',
      c('[Kiss her] "I\'m knocking. See?"', "yes", requires=(I_RET,), flags=("anevia.committed", TERMS)),
      c('[Take her hand and wait] "Your call, Nevi."', "yes", flags=("anevia.committed", TERMS)),
      c('[Let go of her hand] "I can\'t promise that."', "no")),
    a("yes", '''{n}For a moment she only looks at you, the way she looks at a lock she has already decided to pick.{/n}''',
      c("Continue", "coats", requires=(LISTEN,)), c("Continue", "threshold", forbids=(LISTEN,))),
    a("coats", '''"If your friend in the coats is listenin', let him. I've been listened to by worse."''',
      c("Continue", "threshold")),
    a("threshold", THRESHOLD,
      c("Continue", "morning_back", requires=(I_RET, I_ASKED), forbids=("irabeth.closed", "irabeth.trickster.friends")),
      c("Continue", "morning", forbids=(I_RET, LEFT)),
      c("Continue", "morning_quiet", requires=(I_RET,), forbids=(I_ASKED,)),
      c("Continue", "morning_quiet", requires=(I_RET, I_ASKED, "irabeth.closed")),
      c("Continue", "morning_quiet", requires=(I_RET, I_ASKED, "irabeth.trickster.friends"), forbids=("irabeth.closed",)),
      c("Continue", "morning_left", requires=(LEFT,), forbids=(I_RET,))),
    a("morning", '''{n}Grey light. She is already dressed and lacing her boots, the lantern relit.{/n}
"If Beth ever walks back through that gate, she'll know the second she looks at me. I'd give a lot to have to make that speech."
{n}She stands, and taps the door twice with her knuckles on the way out.{/n}
"Same door. Knock."''',
      c('"Same door."')),
    a("morning_back", '''{n}Grey light. She is already dressed and lacing her boots, the lantern relit.{/n}
"Beth's got my word about her nights. She's gettin' me home for breakfast."
{n}She stands, and there it is: her old crooked grin, a little rusty.{/n}
"She'll want a turn yellin' at you. Let her. Then she'll want to know if you're good enough for the both of us, and she'll ask you herself. I'm not answerin' for her."''',
      c('"I\'ll knock."')),
    a("morning_quiet", '''{n}Grey light. She is already dressed and lacing her boots, the lantern relit.{/n}
"Beth's got my word about her nights. She's gettin' me home for breakfast."
{n}She stands, and there it is: her old crooked grin, a little rusty.{/n}
"She wrote her terms down. Don't make her come lookin' for you with that letter in her hand."''',
      c('"I\'ll knock."')),
    a("no", '''"Then we're done for tonight. I'm not sayin' never. I'm sayin' not like this. Come back when you can knock."
{n}She picks up the lantern and walks back down the road without looking round.{/n}''',
      c('[Let her walk back to the road] "Then I\'ll learn to knock."', flags=(DECLINED,))),
    a("left", '''"Beth asked me where I go at night. I told her the truth: the gate. She didn't say a word. She cleaned her sword instead, all of it, twice."
{n}She breathes out, and it smokes in the cold.{/n}
"I'm not askin' your leave and I'm not askin' hers. I'm tellin' you what it costs. Say what you came out here to say."''',
      c('[Ask her to stay] "Stay. Not in there. Here, with me."', "terms"),
      c('[Say nothing and wait] "..."', "terms")),
    a("morning_left", '''{n}Grey light. She is already dressed and lacing her boots, the lantern relit.{/n}
"Beth's gonna know the second she looks at me. She won't say it. That's worse."
{n}She stands, and taps the door twice with her knuckles on the way out.{/n}
"Same door. Knock. And when she's ready to ride, I'm gone with her. You knew that last night."''',
      c('"Same door."')),
], requires=("trickster.ever", RETURNED, GATE), forbids=("anevia.committed", DECLINED), delay=96)

# E12b letter twin: only if the smith anchor cannot be resolved, so the gate beats cannot be staged in person.
letter("anevia.trickster.gone.commit_letter", "Beth first", [
    a("start", '''{n}A letter in her plain hand. There is no furniture in it anywhere.{/n}
"Gate's watched. I'm not standin' in front of a whole garrison to say this. So: Beth first. Always Beth first. If you can live with that, and with a door you knock on like a person, say so. If you can't, don't write back."''',
      c("Continue", "share", requires=(I_RET,)), c("Continue", "reply", forbids=(I_RET,))),
    a("share", '''"If Beth ever wants you, she asks me first. To my face. And I'll say yes: I'd rather share than bury. I'm tellin' you so you know where it stands."''',
      c("Continue", "reply")),
    nar("reply", '''{n}There is room at the bottom of the page for an answer, and nothing else.{/n}''',
      c('[Write back: take her hand] "Your call, Nevi. I\'ll wait at whatever door you name."', "later",
        flags=(GATE, TERMS)),
      c('[Write back: kiss the page] "I\'m knocking. See?"', "later", requires=(I_RET,), flags=(GATE, TERMS)),
      c('[Write back: let her go] "Then I\'ll learn to knock."', flags=(DECLINED, GATE))),
    a("later", '''{n}Her answer comes back folded small, three lines in the plain hand.{/n}
"Good. Not by post, though. I'm not sayin' yes to a piece of paper.
When this is over, find a real door and knock on it. I'll be on the other side.
Don't make me wait too long. I'm a spy, not a saint."''',
      c('"A real door."')),
], requires=("trickster.ever", RETURNED, "anevia.presence.failed"),
   forbids=("anevia.committed", DECLINED, "anevia.trickster.gone.gate", "anevia.trickster.gone.commit"), delay=96)

physical("anevia.trickster.gone.second_ask", "Something true", '"I knocked."', [
    a("start", '''{n}You knock on the guardhouse door. A sentry points you round the corner. Anevia waits there with her lantern, on the road side of the line.{/n}
"You knocked. On the guardhouse door, like an idiot, in front of half the watch. All right. I heard you."''',
      c("Continue", "price", forbids=(KILLED,)),
      c("Continue", "price", requires=(KILLED, I_RET)),
      c("Continue", "price", requires=(KILLED, PENANCE), forbids=(I_RET,)),
      c("Continue", "say_it", requires=(KILLED, "anevia.lover"), forbids=(I_RET, SAID)),
      c("Continue", "no_door", requires=(KILLED,), forbids=(I_RET, "anevia.lover")),
      c("Continue", "wait_muster", requires=(KILLED, SAID, "anevia.lover"), forbids=(I_RET, PENANCE))),
    a("no_door", '''"No. Not you. You were never anythin' to me before Iz, and you put your sword through my wife. Go home, Commander."
{n}She does not wait to see whether you go.{/n}''',
      c('"Goodbye, Anevia."', flags=("anevia.closed",))),
    a("promise_again", '''"Then go and say it where her knights can hear. After, come out to the gate."''',
      c('"After muster."', abort=True)),
    a("wait_muster", '''"You know where muster is. I'm not hearin' another word from you till you've said the first one in the yard."''',
      c('"After muster."', abort=True)),
    a("say_it", '''"No. Not a secret. I don't want somethin' nobody knows. I want the thing everybody knows and you won't say."
{n}She holds up the lantern, the way she did at the gate.{/n}
"Say what you did at Iz. Then tomorrow you say it at muster, in front of her knights. Then we'll talk about doors."''',
      c('[Say it] "I killed her. At Iz. With my own hand. Tomorrow, at muster, I\'ll say it again."', "price", flags=(SAID, PENANCE),
        forbids=(KILLED,)),                                # retired by gating (index kept): the muster comes first
      c('[Say it] "I killed her. At Iz. With my own hand. Tomorrow, at muster, I\'ll say it again."', "promise_again", flags=(SAID,)),
      c('[Keep it] "Some things stay mine."', "kept", flags=("anevia.closed",))),
    a("price", '''"Door's paid for. Now you pay for me. Tell me somethin' true about you that nobody in Drezen knows. Not your mythic nonsense. Somethin' that'd cost you if I sold it."
{n}She holds out her hand, palm up, the way a fence waits for a coin.{/n}
"I'll never use it. Probably. But you'll never again be sure what I know about you. You know where I go when I don't want you near me. Now I get somethin' you can't take back, too."''',
      c('[Tell her something true] "All right. Lean in."', "key",
        flags=("anevia.committed", KEY)),
      c('[Keep it] "Some things stay mine."', "kept", flags=("anevia.closed",))),
    a("kept", '''"Then that's that."
{n}She closes the hand, slowly, and puts it in her pocket.{/n}
"Good luck, Commander. I mean it."''',
      c('"Goodbye, Anevia."')),
    a("key", '''{n}You tell her. She listens the way she listens to a confession she means to keep: no expression at all, then one slow nod, as if a lock had turned somewhere behind her eyes. She closes the empty hand and puts it in her pocket.{/n}
"Probably never use it."''',
      c("Continue", "night")),
    a("night", '''{n}That night there is a knock at your door: three knocks, like a person.{/n}
"Changed my mind about comin' in. Didn't change it about knockin'."
{n}You have not reached the latch when it lifts on its own.{/n}
{n}She is across the room before you are out of the chair, and she does not bother with the lantern. Her hands are cold from the road and then they are not. She has your shirt half over your head when she laughs, low, into your mouth, and says "Probably" as if it were the filthiest word she knows, and pushes you back onto the bed and follows you down.{/n}''',
      c("Continue", "dawn")),
    a("dawn", '''{n}Grey light, and her side of the bed is cold. Your shirt lies over the chair. Under your cup is a folded scrap in her plain hand.{/n}
"Probably."
{n}Nothing else. Not a word of what you told her. You tuck the scrap away before the first runner knocks.{/n}''',
      c('"Probably."')),
], requires=("trickster.ever", RETURNED, DECLINED), forbids=("anevia.committed",), delay=96)


# Sol r2 BEL: the public confession is played, the knights answer it, and only then does she open a door.
physical("anevia.trickster.gone.muster", "Muster", '"After muster. You said."', [
    nar("yard", '''{n}Muster, in the citadel yard, in the grey before the bell. You stand on the step where the orders of the day are read and say it in the same words: "I killed Irabeth Tirabade. At Iz. With my own hand."{/n}
{n}Nobody moves. Then a knight of Irabeth's old company takes off his helmet and holds it under his arm, the way a man stands at a grave. Another turns her back on you and stays that way until the bell. A third spits on the step, precisely, and walks off without being dismissed. Nobody stops him. You don't either.{/n}''',
      c("Continue", "gate")),
    a("gate", '''{n}She is at the gate afterwards, on her side of the line, with the lantern. She was on the wall for all of it; you saw her there.{/n}
"You didn't say it sideways. Not once." {n}She keeps the lantern on her side of the line.{/n} "I'm still not forgivin' you. I don't think I'm built for it. But I asked for a thing, and you paid it where it cost. That buys you the gate. Not the door. Not yet."''',
      c('[Kiss her] "I\'m knocking. See?"', "threshold", flags=("anevia.committed", TERMS, PENANCE), forbids=(KILLED,)),  # retired
      c('[Take her hand and wait] "Your call, Nevi."', "threshold", flags=("anevia.committed", TERMS, PENANCE), forbids=(KILLED,)),
      c('[Walk her back to the road] "The gate, then. For now."', flags=(PENANCE, DECLINED)),
      c('[Step back] "Not tonight."', flags=(PENANCE, DECLINED))),
    a("threshold", THRESHOLD, c("Continue", "morning")),
    a("morning", '''{n}Grey light. She is already dressed and lacing her boots. On the table, face down, is the little portrait of Beth she carries everywhere; she turned it over last night and has not turned it back.{/n}
"Don't look at that. I'll turn it up when you've gone. Every time."
{n}She stands, and taps the door twice with her knuckles on the way out.{/n}
"Same door. Knock."''',
      c('"Same door."')),
], requires=("trickster.ever", RETURNED, KILLED, SAID, "anevia.lover"),
   forbids=(PENANCE, "anevia.committed"), delay=12)


# --- The shared route: three at the table again ---------------------------------------------------------------------

def table(id, title, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Irabeth", 5, "", nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship="tirabade", Chapters=[5], Remote=True, **extra))


CHAIRS = (c('[Pull out the third chair] "Three. I\'ve already stolen the third one."',
            flags=("started", "tirabade.trickster.third_chair")),
          c('[Stay standing] "Two. I only came to see you both sitting down."', flags=("tirabade.trickster.two_chairs",)))

table("tirabade.trickster.table_again", "Two chairs or three", [
    n("start", "Irabeth", '''{n}A camp table has appeared on the road side of the Drezen gate, where the cartwheels have worn a line into the mud. Somebody has carried three chairs out of the guardhouse and set two of them.{/n}
"Nevi says you walked out of her wardrobe. I told her that's not possible."
{n}Irabeth sets the sword across her knees, because she has sworn to keep it within reach.{/n}
"She says neither am I."''',
      c("Continue", "accounting", requires=(I_REWRITTEN,), forbids=(ACCOUNT,)),
      c("Continue", "chairs", forbids=(I_REWRITTEN,)),
      c("Continue", "chairs", requires=(ACCOUNT,)),
      portrait="Irabeth"),
    a("accounting", '''"Before anyone sits. Beth says she stepped inside your blade at Iz. Beth also remembers it goin' in. I've heard her side. I haven't heard yours."
{n}Irabeth looks at the table. Anevia looks at you.{/n}
"Tell me what happened. All of it. Then we'll talk about chairs."''',
      c('[Tell her everything] "I struck her down. Then I sent men back to dig her out. Both are true."', "chairs",
        flags=(ACCOUNT, "anevia.trickster.heard_the_truth")),
      c('[Refuse] "Not tonight."', "refused", flags=("tirabade.trickster.two_chairs",))),
    a("refused", '''"Then it's two chairs."
{n}She pulls the third one away from the table and sits on it herself, with her back to you.{/n}''',
      c('"Two chairs."')),
    a("chairs", '''"Two chairs or three, Commander. And think before you answer, 'cause she's got a sword she's sworn to keep by her."''',
      *CHAIRS),
], requires=("trickster.ever", I_RET, RETURNED), forbids=(), delay=24)

table("tirabade.trickster.third_chair", "Deal the cards", [
    n("start", "Irabeth", '''{n}A night at the camp table on the road side of the gate, three chairs this time, both women armed. Anevia has a pack of cards that is missing the Queen of Coins. Irabeth has a sword across her knees and her boots on the third chair, which she takes down, slowly, when you arrive.{/n}''',
      c("Continue", "run"), portrait="Irabeth"),
    a("run", '''"Last chance to run, Commander."''', c("Continue", "kindly")),
    n("kindly", "Irabeth", '''"She means it kindly. Mostly."''',
      c('[Sit] "Deal the cards."', "dealt", flags=("committed",)),
      c('[Leave the chair empty tonight] "Not yet. Keep it for me."', "kept", flags=("tirabade.trickster.declined",)),
      portrait="Irabeth"),
    a("dealt", '''{n}Anevia deals. Irabeth cheats, badly and one-handed, and denies it under oath. Nobody finds the Queen of Coins. At some point the watch changes behind you, and nobody at the table notices, and then the lantern is the only light on the road and all three of you are still there.{/n}
"Same time tomorrow," {n}Anevia says.{/n} "Same chairs. Knock first."''',
      c('"Same chairs."')),
    n("kept", "Irabeth", '''"Then it stays here. We'll put a cup on it."
{n}Anevia is already pouring.{/n}''',
      c('"Keep it warm."'), portrait="Irabeth"),
], requires=("trickster.ever", "tirabade.trickster.third_chair"), forbids=(), delay=72)


# --- Epilogue: one page, or paragraphs on her registered ending ----------------------------------------------------

LATE = "anevia.trickster.late_committed"


def ret(text, requires=(), forbids=()):
    """A paragraph about the returned Anevia: never shown on a registered ending of an Anevia who stayed."""
    return p(text, requires=(RETURNED, *requires), forbids=forbids)


PARAGRAPHS = (
    ret("{n}She never again owned a wardrobe she had not nailed shut, and she never again went through a door without "
      "knocking on it first.{/n}", requires=(NAILED,), forbids=(CRATED,)),
    ret("{n}The wardrobe in the room over the Defender's Heart stayed nailed shut until the Heart was rebuilt, and then the "
      "carpenters found it and could not work out why anyone had used so many nails.{/n}", requires=(NAILED,), forbids=(CRATED,)),
    ret("{n}She kept the crate lid, the one with the air holes, and used it as a tray for the rest of her life. Anyone who "
      "asked about the holes was told they were for ventilation, which was true.{/n}", requires=(CRATED,)),
    ret("{n}Somewhere south of Drezen a quartermaster still tells the story of the crate marked{/n} \"salt pork, Commander's "
      "personal\"{n}, and nobody believes him.{/n}", requires=(CRATED,)),
    ret("{n}Whenever the Commander asked, she said she had come back because Beth had fetched her. Whenever Beth was in "
      "the room, she said it was the other way round.{/n}", requires=(BARGAIN, "irabeth.present_now")),
    ret("{n}She kept the certified copy of the report from Iz in a drawer, the version that hurt, and never once took it "
      "out.{/n}", requires=(ACCOUNT,), forbids=(EXPOSED,)),
    ret("{n}She never again took anything the Commander said on trust. She said it was restful.{/n}", requires=(EXPOSED,)),
    ret("{n}The spring after Threshold, somebody knocked on the Commander's door in Nerosyan: a real door, three times, "
      "like a person. She had a lantern in one hand and no knife in the other, and the conversation from the gate "
      "picked up exactly where she had left it. On her terms. It was always going to be on her terms.{/n}",
      requires=(LATE,), forbids=("anevia.committed", "anevia.closed", DECLINED, FRIENDS)),
    ret("{n}Irabeth came with her, carrying both their packs and pretending very hard to be somewhere else.{/n}",
      requires=(LATE, I_RET, "irabeth.present_now"), forbids=("anevia.committed", "anevia.closed", DECLINED, FRIENDS)),
    ret("{n}She kept to the door rule for the rest of her life, and made the Commander keep it too: a real door, three "
      "knocks, and no furniture.{/n}", requires=(TERMS,)),
    ret("{n}She kept the one secret the Commander ever handed her, and never once used it. Probably.{/n}", requires=(KEY,)),
    p("{n}She never forgave the Commander for Iz, and never pretended to. She kept her own terms anyway: a real door, three "
      "knocks, and Beth's name said out loud every time she came through it. Whatever the two of them had, they built it "
      "beside that grave and not over it, and she would not let either of them forget which side of it they stood on.{/n}",
      requires=(RETURNED, KILLED), forbids=(I_RET, "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record"), any_groups=([TERMS, KEY],)),
    p("{n}Beth stayed dead. Anevia kept her side of the bed cold on purpose for a year, and said so, and then one winter "
      "night she didn't, and said that too. She never once let the Commander pretend the two things were the same "
      "kind of love, and never once let either of them be ashamed of the second.{/n}",
      requires=(RETURNED, "irabeth_dead"), forbids=(I_RET, KILLED, "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record"), any_groups=([TERMS, KEY],)),
    p("{n}At muster the morning after the gate, the Commander said it in the yard, in front of Beth's knights, in the same "
      "words:{/n} \"I killed her. At Iz. With my own hand.\" {n}Nobody in Drezen ever said it sideways again.{/n}",
      requires=(RETURNED, PENANCE)),
    ret("{n}She kept her word and never came inside. Letters reached the Commander now and then from towns on the road "
      "south, unsigned, in a hand nobody else could read. None of them was a yes. None of them was quite a no.{/n}",
      requires=(DECLINED,), forbids=("anevia.committed", "anevia.closed")),
    ret("{n}She came to the gate once more, to say goodbye properly, and did not come again.{/n}", requires=("anevia.closed",)),
    ret("{n}She and the Commander stayed on their own sides of the line in the mud, by agreement, and found that they "
      "liked it there.{/n}", requires=(FRIENDS,), forbids=("anevia.committed", "anevia.closed", LATE)),
    ret("{n}Beth stood watch at the Drezen gate until the Wound was closed, left foot forward, and Anevia stood on the "
      "road side of it and talked to her through the whole of every watch.{/n}", requires=(I_RET, "irabeth.present_now")),
)
PAGE = '''{n}Anevia Tirabade came back as far as the Drezen gate, and for a long while no further.{/n}'''
TOGETHER = {"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}


def epilogue(id, requires, forbids, **extra):
    SCENES.append(scene(id, "The line in the mud", "Epilogue", 0, "", [
        n("end", "Narrator", PAGE, portrait="Anevia", paragraphs=PARAGRAPHS)],
        requires=requires, forbids=("trying", "committed", *forbids), last=99, Relationship="anevia",
        ForbidOverrides=dict(TOGETHER, **extra.pop("ForbidOverrides", {})), **extra))


# One Anevia page per history. A non-lover gets this page; a registered lover keeps her registered ending (with the
# paragraphs) except in the two histories that have none: committed at the gate, or closed at the secret.
FATES = ("sacrifice", "ascended", "inhuman")
epilogue("anevia.trickster.epilogue.nailed_wardrobe", (RETURNED,), ("anevia.lover",))
epilogue("anevia.trickster.epilogue.nailed_wardrobe_lover", (RETURNED, "anevia.lover", "anevia.committed"),
         ("anevia.future_chosen", "anevia.developed", "anevia.survivor_continues", "irabeth_dead", *FATES),
         ForbidOverrides={"irabeth_dead": "irabeth.present_now", "anevia.survivor_continues": I_RET, "sacrifice": "trickster.commander_back"})
epilogue("anevia.trickster.epilogue.nailed_wardrobe_closed", (RETURNED, "anevia.lover", "anevia.closed"),
         ("anevia.parted", "anevia.committed", *FATES), ForbidOverrides={"sacrifice": "trickster.commander_back"})
# Sol INT: the registered "wife killed" ending denies the night she chose after her return; this history gets its own
# page (the registered ending Forbids her renewed terms instead).
epilogue("anevia.trickster.epilogue.nailed_wardrobe_widow", (RETURNED, "anevia.lover", "irabeth_dead"),
         (I_RET, KILLED, "anevia.closed", "ascended", "inhuman"), RequiresAnyGroups=[[TERMS, KEY]])
epilogue("anevia.trickster.epilogue.nailed_wardrobe_unforgiven", (RETURNED, "anevia.lover", KILLED, "irabeth_dead"),
         (I_RET, "anevia.closed", "ascended", "inhuman"), RequiresAnyGroups=[[TERMS, KEY]])


# E14d extension: the native Tirabade slide BookPage_0307 Cue_0311 (IrabethDead + AneviaGone Playing, which the Trickster
# never ends): "Now alone, Anevia left - quietly, unnoticed, leaving no notes or traces. No one ever saw her again." A
# returned Anevia (or a returned Irabeth, irabeth_trickster.NATIVE_SOUTH) contradicts it, committed or not. The first
# variant whose When holds replaces it; otherwise the native slide plays. With Beth back the page keeps its pair picture;
# while Beth is dead (or Anevia stays away) the native cue's own image change runs, as on the native departure cues.
TIRABADE_SLIDE = "3a3e561c6b05a284d93eb3bff7b712a6"    # World/Dialogs/Epilogues/Cue_0311
TIRABADE_PAGE = "ae1f824fe248d9f4aac7d39ec2e12140"     # World/Dialogs/Epilogues/BookPage_0307
SPECIAL = "f8d7f50e3bb88c143834d234c0b24474"           # World/Dialogs/Epilogues/CueSequence_Special
NATIVE_TOGETHER = "anevia.trickster.epilogue.native_tirabade_together"
NATIVE_BACK = "anevia.trickster.epilogue.native_tirabade_back"
NATIVE_WIDOW_COMMITTED = "anevia.trickster.epilogue.native_tirabade_widow_committed"
NATIVE_WIDOW = "anevia.trickster.epilogue.native_tirabade_widow"
I_NATIVE_SOUTH = "irabeth.trickster.epilogue.native_tirabade_south"   # irabeth_trickster.py

LEFT_A_WIDOW = "Anevia quit Drezen at the Coronation. Her wife was dead; her destination remained her own. Irabeth did not stay dead."
LEFT_ALONE = ("Alone after Beth's death, Anevia left Drezen. It was not enough to lose the "
              "Commander, who found her anyway, by a road no one else would have thought to take.")


def native_slide(id, text, requires):
    SCENES.append(scene(id, "", "AneviaEpilogue", 6, "", [nar("page", "{n}" + text + "{/n}", c())],
                        requires=requires, last=99, Relationship="anevia"))


native_slide(NATIVE_TOGETHER, LEFT_A_WIDOW + " Irabeth came back from Iz, and Anevia came back as far as the Drezen gate, "
             "and in time through a door beside it, one she knocked on first. The Tirabades kept their own house and their "
             "own counsel. What Anevia shared with the Commander, she shared on her own terms, and Beth always came first.",
             (RETURNED, "anevia.committed", I_RET))
native_slide(NATIVE_BACK, LEFT_A_WIDOW + " Irabeth came back from Iz, and Anevia came back as far as the Drezen gate, though "
             "rarely any further. Whatever else the Tirabades lost to the Fifth Crusade, they did not lose each other, and "
             "Anevia never let the Commander forget how close it had come.",
             (RETURNED, I_RET))
native_slide(NATIVE_WIDOW_COMMITTED, LEFT_ALONE + " She came back as far as the Drezen gate, and in time through a door "
             "beside it, but only on her own terms, and Beth's name was always the first thing said between them.",
             (RETURNED, "anevia.committed"))
native_slide(NATIVE_WIDOW, LEFT_ALONE + " She came back as far as the Drezen gate to tell the Commander what she thought of "
             "that, to the Commander's face. Where she went after that was her own decision, and she made sure everyone knew it.",
             (RETURNED,))

# The other departure cue on the same page, Cue_0310 (IrabethGone + AneviaGone: both left at the Coronation after the
# Commander's betrayal): "...She barely resisted when Anevia came to take her as far away from Mendev as possible, but they
# could never escape their nightmares of the Fifth Crusade." The wardrobe reaches that Anevia too (its setup needs only
# anevia_gone). Irabeth has no Trickster return from that departure, so only Anevia's return changes the slide. Beth is
# alive but gone from Drezen with her, so the native departure picture stays.
TIRABADE_LEFT_SLIDE = "ccd140dbf2603734aa323261c2445bec"   # World/Dialogs/Epilogues/Cue_0310
NATIVE_LEFT_COMMITTED = "anevia.trickster.epilogue.native_tirabade_left_committed"
NATIVE_LEFT = "anevia.trickster.epilogue.native_tirabade_left"
LEFT_TOGETHER = ("The Commander's betrayal and the humiliation she had suffered in Drezen eroded Irabeth's fighting spirit, "
                 "and Anevia meant to take her as far away from Mendev as she could.")
native_slide(NATIVE_LEFT_COMMITTED, LEFT_TOGETHER + " They had not got far enough to keep the Commander from "
             "finding her. Anevia came back as far as the Drezen gate, and in time through a door beside it, on her "
             "own terms. She never forgave the betrayal, and Beth always came first.",
             (RETURNED, "anevia.committed"))
native_slide(NATIVE_LEFT, LEFT_TOGETHER + " They had not got far enough to keep the Commander from "
             "finding her. Anevia came back as far as the Drezen gate to say what she thought of that, and then she went back "
             "to her wife. Neither of them ever escaped the nightmares of the Fifth Crusade, and she never pretended otherwise.",
             (RETURNED,))

NATIVE_EPILOGUE_EDITS = {
    TIRABADE_LEFT_SLIDE: dict(Page=TIRABADE_PAGE, Sequence=SPECIAL, Key="cc716238-3702-4913-977d-6189665672b7",
                              Replacement=NATIVE_LEFT_COMMITTED, When=[["trickster.ever", RETURNED, "anevia.committed"]], KeepNativeImage=True,
                              Variants=[dict(Replacement=NATIVE_LEFT, When=[["trickster.ever", RETURNED]], KeepNativeImage=True)]),
    TIRABADE_SLIDE: dict(Page=TIRABADE_PAGE, Sequence=SPECIAL, Key="4c278ba4-5217-4fae-afec-47c6f6597e00",
                         Replacement=NATIVE_TOGETHER, When=[["trickster.ever", RETURNED, "anevia.committed", I_RET]], KeepNativeImage=False,
                         Variants=[dict(Replacement=NATIVE_BACK, When=[["trickster.ever", RETURNED, I_RET]], KeepNativeImage=False),
                                   dict(Replacement=NATIVE_WIDOW_COMMITTED, When=[["trickster.ever", RETURNED, "anevia.committed"]], KeepNativeImage=True),
                                   dict(Replacement=NATIVE_WIDOW, When=[["trickster.ever", RETURNED]], KeepNativeImage=True),
                                   dict(Replacement=I_NATIVE_SOUTH, When=[["trickster.ever", I_RET]], KeepNativeImage=True)]),
}


REACTIONS = [
    reaction("Konomi", "anevia.trickster.gone.react_konomi", (RETURNED, PRIMED),
             '''{n}Lady Konomi does not look up from her ledger. She turns it round so that you can read the line she has just written.{/n}
"'The Commander was absent from the war council on account of travel arrangements of an irregular nature.' I wrote that myself, Commander, in front of the Queen's envoy, without laughing. I would like you to know what it cost me."''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead", STOLEN), chapter=5, last=5,
             entry='"About the war council I missed."'),
    reaction("Konomi", "anevia.trickster.gone.react_konomi_closet", (RETURNED, STOLEN),
             '''{n}Lady Konomi does not look up from her ledger.{/n}
"Your Commander missed a war council. Officially, a wardrobe was blamed. I have minuted it. I have also spent a week of other people's goodwill explaining the wardrobe to them, and I am afraid the account is overdrawn."''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead"), chapter=5, last=5,
             entry='"About the war council I missed."'),
    reaction("Woljif", "anevia.trickster.gone.react_woljif", (RETURNED, PRIMED),
             '''"Chief. Chief. You went into a wardrobe in Drezen and came out in a lady's bedroom in Kenabres."
{n}Woljif sits down on the nearest barrel as if his knees have given out.{/n}
"I've been climbin' drainpipes like a sucker my whole life."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out", CRATED), chapter=5, last=5,
             entry='"You heard about Anevia."'),
    reaction("Woljif", "anevia.trickster.gone.react_woljif_crate", (RETURNED, CRATED),
             '''"A crate. You posted yourself. In a crate. Addressed to a dead drop."
{n}Woljif wipes his eyes.{/n}
"Chief, I'm gonna cry. That's the most beautiful thing I ever heard, and I was raised by thieves."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out"), chapter=5, last=5,
             entry='"You heard about Anevia."'),
    reaction("Woljif", "anevia.trickster.gone.react_woljif_fetched", ("anevia.trickster.gone.fetched",),
             '''"Chief, the Knight-Captain rode out with one horse and came back with two horses and a wife. I asked her how. She said 'orders'."
{n}He shudders.{/n}
"I'm never askin' her anything again."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out"), chapter=5, last=5,
             entry='"You heard about Anevia."'),
    reaction("Konomi", "anevia.trickster.gone.react_konomi_fetched", ("anevia.trickster.gone.fetched",),
             '''"The Tirabades are both off the books and both on them, Commander. I have stopped asking how. I have not stopped writing it down."''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead"), chapter=5, last=5,
             entry='"The Tirabades are back."'),
    reaction("Woljif", "anevia.trickster.gone.react_woljif_confession", ("anevia.trickster.gone.confession",),
             '''"Chief. The spy lady asked me if I'd ever seen you lie. I said no. She said 'good answer, wrong question' and walked off."
{n}He is still sweating.{/n}
"That was an hour ago."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out"), chapter=5, last=5,
             entry='"You heard about Anevia."'),
    reaction("Konomi", "anevia.trickster.gone.react_konomi_confession", ("anevia.trickster.gone.confession",),
             '''"Mistress Tirabade requested a certified copy of the incident report from Iz. I gave her the chancery's, which says 'fell in action', and the chaplain's, which says whose action. She kept the one that hurt, and returned mine with a note."
{n}Konomi produces it. Two words, in a plain hand: "Tidy. Wrong."{/n}''',
             answer_list=KONOMI_OFFICER, forbids=("konomi.dismissed", "konomi.retained_dead"), chapter=5, last=5,
             entry='"The Tirabades are back."'),
]
SCENES.extend(REACTIONS)


# G6 on the registered route (save-safe: conditions and paragraphs only, no id, node or choice changes).
IRABETH_DEAD_LIFTED = (  # G6(b): the scenes that Forbid irabeth_dead lift it once Irabeth has returned
    "anevia.unborrowed_hour", "anevia.a_question_at_home", "anevia.one_truth", "anevia.beths_question",
    "anevia.beths_answer", "anevia.her_own_answer", "anevia.a_place_of_our_own", "anevia.an_invitation_afterward",
    "anevia.borrowed_signature", "anevia.the_paper_seller", "anevia.the_woman_with_the_basket",
    "anevia.the_counting_room", "anevia.what_the_warning_cost", "anevia.the_evening_without_a_case",
    "anevia.departure_note", "anevia.the_life_she_lived", "anevia.a_key_that_is_hers",
    "anevia.the_last_ordinary_thing", "anevia.ending_kept", "anevia.ending_open", "anevia.ending_unfinished",
    "anevia.ending_promised", "anevia.ending_wife_absent")
ANEVIA_GONE_LIFTED = (   # G6(b): her endings that Forbid anevia_gone lift it once she has returned (ANE-02: survivor)
    "anevia.ending_kept", "anevia.ending_open", "anevia.ending_unfinished", "anevia.ending_promised",
    "anevia.ending_parted", "anevia.ending_grief_unanswered", "anevia.ending_wife_absent", "anevia.ending_sacrifice",
    "anevia.ending_survivor")
GRIEF_PAGES = ("anevia.a_grief_with_a_name", "anevia.ending_grief_unanswered", "anevia.ending_wife_killed",
               "anevia.ending_survivor")   # G6(a): no grief over a wife who has come back
WITH_PARAGRAPHS = ("anevia.ending_kept", "anevia.ending_open", "anevia.ending_unfinished", "anevia.ending_promised",
                   "anevia.ending_parted", "anevia.ending_survivor", "anevia.ending_grief_unanswered",
                   "anevia.ending_wife_killed", "anevia.ending_sacrifice", "anevia.ending_ascended",
                   "anevia.ending_changed_power")
TIRABADE_ENDINGS = ("ending_promised", "ending_ascend_promised")
COURTSHIP_OPENING = ("anevia.unborrowed_hour", "anevia.a_question_at_home", "anevia.one_truth", "anevia.beths_question",
                     "anevia.beths_answer", "anevia.her_own_answer", "anevia.a_place_of_our_own",
                     "anevia.an_invitation_afterward")
LIVING_ENDINGS = ("anevia.ending_kept", "anevia.ending_open", "anevia.ending_unfinished", "anevia.ending_promised")
TIRABADE_PARAGRAPH = p("{n}They had both been lost once, one to Iz and one to the road south, and both had come back by "
                       "routes that did not bear close inspection. At the Tirabade table there were three chairs, and "
                       "Anevia's rule for the third was the same as for every door: knock first.{/n}",
                       requires=(RETURNED, I_RET))
# Sol pol INT: the registered "wife killed" ending, for an Anevia who came back but never renewed her terms. Her no at
# the gate was "not like this", not never; exactly one of these (with the independent module's never-returned closure)
# says where it was left. The muster and unsigned-letter paragraphs follow from PARAGRAPHS.
WIFE_KILLED_RETURNED = (
    p("{n}Her last word at the gate had been{/n} \"Come back when you can knock,\" {n}and she had meant both halves of it. The knock "
      "she wanted was Iz, said plainly in the Commander's own voice, in the yard where Beth's knights could hear it. It "
      "was never said there. She did not shut the gate, and she did not forgive a word of it.{/n}",
      requires=(RETURNED, DECLINED), forbids=(PENANCE,)),
    p("{n}She called the muster what it was: the price of the gate, not of the door. She held to that. The lantern stayed on "
      "her side of the line, the Commander still knew how to knock, and she never once said she would not answer.{/n}",
      requires=(RETURNED, DECLINED, PENANCE)),
    p("{n}She came back as far as the Drezen gate with Beth's name still the first thing out of her mouth. Whatever passed "
      "between them afterward, she never let Iz be told as an accident, and never let her coming back be mistaken for a "
      "pardon.{/n}",
      requires=(RETURNED,), forbids=(DECLINED,)),
)


def integrate(payload):
    """Relationship patch, presence, the G6 guards and paragraphs on her registered route, and the tirabade return."""
    rel = payload["Relationships"]["anevia"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, an Anevia who has left the crusade can still be reached, though not by "
                        "any ordinary door. After her return, look for her outside the Drezen gate, by the smithy.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    # E14d extension: the native Tirabade slide. Irabeth's own variant joins only when her route (and its scene) is built.
    present = {s["Id"] for s in payload["Scenes"]}
    from storylines.native_overrides import register_legacy
    edits = {}
    for cue, edit in NATIVE_EPILOGUE_EDITS.items():
        built = {k: ([list(g) for g in v] if k == "When" else v) for k, v in edit.items() if k != "Variants"}
        built["Variants"] = [{k: ([list(g) for g in v] if k == "When" else v) for k, v in variant.items()}
                             for variant in edit["Variants"] if variant["Replacement"] in present]
        edits[cue] = built
    register_legacy(payload, __name__, edits=edits)
    ours = {s["Id"] for s in SCENES}
    tirabade = payload["Relationships"]["tirabade"]
    tirabade.setdefault("UnavailableOverrides", {}).update({"irabeth_dead": I_RET, "anevia_gone": RETURNED})
    for s in payload["Scenes"]:
        if s["Id"] in IRABETH_DEAD_LIFTED:
            s.setdefault("ForbidOverrides", {})["irabeth_dead"] = "irabeth.present_now"
        if s["Id"] in ANEVIA_GONE_LIFTED:
            s.setdefault("ForbidOverrides", {})["anevia_gone"] = RETURNED
        if s["Id"] in GRIEF_PAGES:
            s["Forbids"].append(I_RET)
        if s["Id"] == "anevia.ending_gone":
            s["Forbids"].append(RETURNED)
        if s["Id"] in COURTSHIP_OPENING:
            s["Forbids"].extend((TERMS, KEY))
        if s["Id"] in ("anevia.ending_wife_killed", "anevia.ending_grief_unanswered", "anevia.ending_survivor"):
            s["Forbids"].extend((TERMS, KEY))
        # Sol COX: the shared finale's surviving Commander is not mourned (as Irabeth, Dorgelinda and Eliandra).
        if s["Id"] == "anevia.ending_sacrifice":
            s["Forbids"].append("trickster.commander_back")
        if s["Id"] in LIVING_ENDINGS:
            s.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"
        # Sol INT: a returned Anevia resumes her physical scenes although the native absence (AneviaNotInDrezen) holds.
        if s.get("Relationship") == "anevia" and "anevia_away" in s.get("Forbids", ()) and s["Id"] not in ours:
            s.setdefault("ForbidOverrides", {})["anevia_away"] = RETURNED
        if s["Id"] in WITH_PARAGRAPHS:
            for node in s["Nodes"]:
                if all(ch.get("Next") is None for ch in node["Choices"]):
                    if s["Id"] == "anevia.ending_wife_killed":
                        node.setdefault("Paragraphs", []).extend(dict(x) for x in WIFE_KILLED_RETURNED)
                    node.setdefault("Paragraphs", []).extend(dict(x) for x in PARAGRAPHS)
        if s.get("Relationship") == "tirabade" and s["Id"] in TIRABADE_ENDINGS:
            s.setdefault("ForbidOverrides", {}).update({"irabeth_dead": I_RET, "anevia_gone": RETURNED})
            for node in s["Nodes"]:
                if all(ch.get("Next") is None for ch in node["Choices"]):
                    node.setdefault("Paragraphs", []).append(dict(TIRABADE_PARAGRAPH))

    # Round 2a: route-local commitment stances and current wife-state codas.
    from storylines import anevia_partner_stance
    anevia_partner_stance.integrate(payload)
    from storylines import anevia_round2
    anevia_round2.integrate(payload)



# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'anevia.trickster.gone.confession',
    'anevia.trickster.gone.fetched',
    'anevia.trickster.gone.wardrobe',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]

# eng7-l08: authored timing variants for the fetched road (E-Q7-18,
# anevia:009). The letters put both women outside Drezen after four days of
# travel; the remaining meetings are appointments. The widow's original
# 24 + 48 + 96 hour mourning schedule (anevia:010) remains intact.
import copy as _timing_copy
_fetched_id = "anevia.trickster.gone.fetched"
next(s for s in SCENES if s["Id"] == _fetched_id)["DelayHours"] = 96
for _old_id, _new_id, _hours in (
        ("anevia.trickster.gone.gate", "anevia.trickster.gone.fetched_gate", 12),
        ("anevia.trickster.gone.commit", "anevia.trickster.gone.fetched_commit", 6),
        ("anevia.trickster.gone.second_ask", "anevia.trickster.gone.fetched_second_ask", 6)):
    _appointment = _timing_copy.deepcopy(next(s for s in SCENES if s["Id"] == _old_id))
    _appointment["Id"] = _new_id
    _appointment["DelayHours"] = _hours
    _appointment["Requires"].append(_fetched_id)
    _appointment["Forbids"].append(_old_id)
    for _node in _appointment["Nodes"]:
        for _answer in _node["Choices"]:
            if not _answer.get("Next") and not _answer.get("Check") and not _answer.get("Abort"):
                _answer.setdefault("Set", []).append(_old_id)
    SCENES.append(_appointment)
# end eng7-l08
