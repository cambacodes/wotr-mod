"""Targona on the Trickster path: spend it again, unnoticed (Writer/handoffs/trickster/targona.md; F16).

Canon: the Silver Twins are "two angels who emerged from one soul" (c1/EstrodTower/Teldon/Cue_3 67eb3b5e); the Hand says
"They called each other brother and sister because one soul was used to create them" (string 49d154d6). Lariel met his
end under Kenabres, and when his sword vanished at the Commander's touch "a part of its power entered your soul"
(glossary). The Trickster's own unlock, TricksterUseMagicDeviceTier2Feature 1383f215, lets the Commander "use items so
delicately that their use is completely unnoticed. Wands you use no longer lose charges from use". The device is the
Trickster answering a scripted fate with the one remedy the game allows after a death, prepared before the blow: the
crusade's Scroll of Raise Dead (a43d2960; "Coming back from the dead is an ordeal", 3355d508), read over her body in
Areelu's laboratory by a Commander who is no cleric, unnoticed (the chosen Use Magic Device Tier 2 trick, read
natively). A Trickster without the trick reads it aloud in front of everyone and pays for the witnesses. Her price is
that she will tell Heaven what was done. The late fallback is the same rite, days later, after her body is carried out
of the ruin. Heaven is never bargained with.
What makes it hers (polish pass 2026-09-28, memory rrt-unique-devices; a raise stays the mechanism because canon offers no
other way back, and the invented alternative was rejected at audit): the twins forged holy weapons for each other
(string 435f6b3c), Lariel's sword was one, and its light is in the Commander: when the sword vanished at the Commander's
touch under Kenabres, "a part of its power entered your soul" (glossary). As the scroll is read, that light is the one thing in the
room her soul knows, and she turns towards it. Shown, never stated as a rule. Voice: compassionate, earnest, humble ("I believe this is a test for me. A hard test, but a necessary one.",
TargonaWings/Cue_0023 40db6d5f). The Commander is the question she has to answer, never the reason she came.
Her Drezen actor and dialog are Angel-only, so on this path she works in a field infirmary behind the quartermaster's
stores (authored) and is met through a spawned copy of her laboratory unit, anchored at Wilcer Garms.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
UNIT = "81297c673b63b60448ef88a10db6bc78"           # AngelTargona (AreeluLab; no dialog component: the presence copy)
DREZEN = "2570015799edf594daf2f076f2f975d8"
QUARTERMASTER = "a380d926e92f70e429681eb9654478f9"  # DrezenCapital_Quartermaster, "Wilcer Garms", always in the capital
LAB_LIST = "2a75fbc8e86fd514e82117c99fc9e528"       # c3/AreeluLaboratory/TargonaWings/AnswersList_0003 ([Attack] Answer_0034)
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"     # CompanionDialogues/Seelah/AnswersList_0003
SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"     # CompanionDialogues/Sosiel/AnswersList_0002 ("Tell me about yourself.")
EMBER_HUB = "f2a35965e9bc601449498bd022b04d9d"      # CompanionDialogues/Ember hub

HUB = "targona.presence"
P = "targona.trickster."
PRIMED = P + "primed"
LAB_LINE = P + "told_in_lab"
RETURNED = P + "returned"
MET = P + "met"
FORGIVEN = P + "forgiven"
DECLINED = P + "declined"
NIGHT = P + "night_kept"
LATE_COMMITTED = P + "late_committed"
IN_DREZEN = P + "in_drezen"
STRUCK = P + "cost.struck_down"
UNFORGIVEN = P + "cost.unforgiven"
LIED = P + "cost.lied"
SHARD = P + "cost.left_for_dead"
LATE = P + "cost.late"
ECHO_SPENT = P + "cost.raised_the_hard_way"
WAND = P + "cost.wand_unspent"
SEALED = P + "cost.light_sealed"
LEFT = P + "cost.left_the_ward"
STARTED = "targona.started"
CLOSED = "targona.closed"
COMMITTED = "targona.committed"
DEAD = "targona.dead_lab"
FREE = "targona.free"
CONDEMNED = "targona.condemned"
TREATED = "targona.ran_treatment_completed"
UMD2 = "trickster.umd_tier2"   # MainCharacterFacts: TricksterUseMagicDeviceTier2Feature 1383f215, a chosen trick
CHARGES = P + "cost.charges_spent"
OPEN = P + "cost.raised_openly"     # the no-trick prepared route: the scroll read aloud, in front of everyone
TOLD = P + "cost.she_told_heaven"   # her price at the barrier: she tells the Hand and her healers what was done

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        DEAD: dict(detect=[DEAD], device=P + "dead.one_soul", returned=RETURNED),
        "freed_in_heaven": dict(detect=[], device=P + "free.spent_light", returned=MET),
    })
PRESENCES = {
    # A spawned copy of her laboratory unit among the infirmary cots behind the quartermaster's stores. Aranka's yard copy
    # stands in front of Wilcer when Fye's is lost; Targona stands behind him, among the cots.
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=QUARTERMASTER, Side="behind", Distance=3.0),
              Requires=["trickster.ever", IN_DREZEN], Forbids=[CLOSED], MinChapter=3, MaxChapter=5,
              AnswerLists=[], Dialog="hub",
              Greeting="{n}Behind the quartermaster's stores the field infirmary runs to three rows of cots under patched "
                       "canvas. An angel is kneeling at the nearest one with a basin of water, one wing white, the other "
                       "black and wrong, folded tight against her back as if it were ashamed of itself.{/n}"),
}


def t(id, text, *choices):
    return n(id, "Targona", text, *choices, portrait="Targona")


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Targona", **kw)


def letter(id, title, nodes, requires, forbids, delay, chapters=(3, 5), **extra):
    SCENES.append(scene(id, title, "Targona", min(chapters), "", nodes, requires=requires, forbids=forbids, delay=delay,
                        last=max(chapters), optional=True, Relationship="targona", Areas=[DREZEN],
                        Chapters=list(chapters), Remote=True, **extra))


def ward(id, title, entry, nodes, requires, forbids, delay, **extra):
    """An in-person beat among the infirmary cots: her presence hub behind Wilcer Garms's stores."""
    SCENES.append(scene(id, title, "Targona", 3, entry, nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        optional=True, Relationship="targona", Areas=[DREZEN], Chapters=[3, 5], ContactUnit=UNIT,
                        InteractionHub=HUB, **extra))


JOKE = ('[Spend it again, quietly] "Whatever strikes you in this room, I\'ll take it back before anyone sees it '
        'was spent."')
FREED_JOKE = '[Spend it again, quietly] "Lariel left me a light in Kenabres. I\'ll use it all night. It won\'t run down."'


# --- State killed_in_lab: the ending read over her, unnoticed (F16) -------------------------------------------------

# The native death is a scripted fate: TargonaIsWasKilledInAreeluLab starts from the [Attack] branch and nothing native
# interrupts it. The Trickster does not claim to stop it. The Commander prepares, before the blow, the one thing the
# game itself allows after a death: raise dead ("You restore life to a deceased party member... Coming back from the dead
# is an ordeal", SpellsRaiseDead 3355d508), from the crusade's own Scroll of Raise Dead (a43d2960). The Trickster's Use
# Magic Device trick is what makes it a trick: "use items so delicately that their use is completely unnoticed ... and
# ... equip any magical items possible, regardless of requirements" (TricksterUseMagicDeviceTier2Feature 1383f215, read
# natively as trickster.umd_tier2). A Commander who took the trick reads a cleric's scroll over her body and nobody sees;
# one who did not has a prepared route too: the same scroll, read aloud, in front of everyone, and paid for.
# R2-2 primers, before the blow, on her own laboratory list. Non-inline: the list is conditioned and its only return cue
# (Cue_0010 d9898ae6) has a Continue, so the entry closes the dialog; the player talks to her again and chooses the
# native outcome ([Attack] Answer_0034 -> Cue_0035, or [Destroy the barrier] Answer_0031).

def lab_primer(id, joke, scroll_text, flags, requires, forbids):
    SCENES.append(scene(id, "Something of my brother", "Targona", 3, '"Before anything else. Look at me."', [
        nar("start", '''{n}Behind the barrier the angel lifts her head. The black wing twitches, as if something in the room has startled it.{/n}
"You... carry something of my brother. I can feel it, like a lamp left burning in another room. Under Kenabres, in the rock where he died. It went into you." {n}Her voice does not break, but it thins.{/n} "Lariel is gone. I felt him go."''',
            c(joke, "scroll", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Favors", -100)),
            c('"Nothing. Forget I spoke."', abort=True)),
        nar("scroll", scroll_text, c("Continue", "resist")),
        t("resist", '''"No." {n}She says it at once, and then she makes herself look at the scroll properly.{/n}
"Raise dead is not mercy, Commander. I have watched chaplains use it. It takes something out of whoever it brings back, and it does not give it back. And you are asking me to let them mourn me. My healers in Heaven. The Hand, who has already buried my brother. Everyone who ever prayed beside me."
{n}The black wing draws tight against her back.{/n} "Tell me why I should let you make liars of all of them."''',
          c('[The wounded] "Because Drezen\'s infirmary loses a man every hour, and none of them will ever reach Heaven\'s healers. They could reach you."', "chooses"),
          c('[The truth] "Because I want you alive. That\'s all. I won\'t dress it up."', "chooses"),
          c('"Then I won\'t ask it of you."', abort=True)),
        t("chooses", '''{n}She is quiet. Somewhere below, in Areelu's cells, something is screaming, and she turns her head towards it the way a healer does, without thinking.{/n}
"If I wake," she says at last, "I will not hide. I will go to the Hand first, and to my healers, and I will tell them what we did and why, and I will let them judge it, whatever it costs you. I will not be raised on a lie."
{n}She lowers her head, as she did before, and waits for you to choose.{/n}''',
          c('[Accept her price] "Tell them everything."', flags=flags)),
    ], requires=requires, forbids=forbids, last=3, optional=True, Relationship="targona",
       AnswerLists=[LAB_LIST], EntryMythic="PlayerIsTrickster"))


lab_primer(P + "dead.setup",
           '[Spend it again, quietly] "Whatever strikes you in this room, I\'ll read you back in before anyone reaches the ending."',
           '''{n}You show her what is inside your sleeve: a scroll of raise dead from the crusade's chaplains, signed out against your name for next month's relic tithe. It is a cleric's scroll, and you are no cleric. Your hands have learned to use any made thing as if it had been made for them, and so lightly that nobody ever sees them do it.{/n}
{n}"If you fall," you tell her, "I will read it over you before they carry anyone out, and nobody in this room will know. And I'll have my hand on you while I read, with his light in it. You made the sword it came from. Whatever you are when the scroll finds you, you'll know that. You will wake alone, and you will wake weaker. Stay down until we are gone."{/n}''',
           (PRIMED, LAB_LINE, TOLD), ("trickster", UMD2), (PRIMED, FREE, DEAD, CONDEMNED))

lab_primer(P + "dead.setup_open",
           '[Spend it again, openly] "Whatever strikes you in this room, I\'ll read you back in. In front of everyone, if I have to."',
           '''{n}You show her what is inside your sleeve: a scroll of raise dead from the crusade's chaplains, signed out against your name for next month's relic tithe. You have no gift for hiding the use of a thing. If you read it, you will read it on your knees over her body, aloud, with every soul in this room watching.{/n}
{n}"If you fall," you tell her, "I will bring you back where you fell, with my hand on you and his light in it. You made the sword it came from; you'll know it. They will see me do it. You will wake weaker, and they will know why."{/n}''',
           (PRIMED, LAB_LINE, TOLD, OPEN), ("trickster",), (PRIMED, FREE, DEAD, CONDEMNED, UMD2))

# R2-2 late fallback: no scroll was prepared. The act is performed now and paid for: her body is carried out of the ruin
# and raised the hard way, days late (Scroll of Raise Dead a43d2960; SpellsRaiseDead 3355d508, "an ordeal").
letter(P + "dead.late_light", "The hard way back", [
    nar("start", '''{n}You did not think of it in the laboratory. You think of it now, with a report on your table that lists her among the dead and says her body was left where she fell.{/n}
{n}Somewhere under the city a demon army is regrouping. Going back into Areelu's ruin for one body will cost blood and favours you cannot spare.{/n}''',
        c('[Send them back for her] "Bring her out. I\'ll read it myself."', "raise", mythic="Trickster", crusade=("Favors", -300)),
        c('"Let her rest."', abort=True)),
    nar("raise", '''{n}Four volunteers go back into the ruin and come out with her wrapped in a Mendevian cloak. All four come out. One of them leaves an arm down there, and the other three do not speak of what is still down there. At the chapel you read a scroll of raise dead over her yourself, at the hour the priests call the thin one, while the chaplain kneeling at the altar keeps his eyes shut.{/n}
{n}Coming back from the dead is an ordeal. The breath goes into her like a blade. Whatever she was before the laboratory, she will be less of it for a long while.{/n}''',
        c('[Stay until she breathes.]', flags=(PRIMED, LATE, ECHO_SPENT))),
], requires=("trickster", DEAD), forbids=(PRIMED, RETURNED), delay=0, chapters=(3,),
   TricksterDevice=True, TricksterState=DEAD)

letter(P + "dead.one_soul", "Read back in", [
    nar("start", '''{n}Three days after Areelu's laboratory, a runner comes up from the field infirmary behind the quartermaster's stores.{/n}''',
        c("Continue", "quiet", forbids=(ECHO_SPENT, OPEN)),
        c("Continue", "open", requires=(OPEN,), forbids=(ECHO_SPENT,)),
        c("Continue", "cold", requires=(ECHO_SPENT,))),
    nar("quiet", '''{n}The laboratory. You have lived it again every night since:{/n}
{n}Your blade goes in. She falls, the way the story always meant her to. The room turns towards the door and whatever Areelu has left waiting there. You kneel beside her as if to close her eyes, and under your breath, no louder than a prayer for the dead, you read the scroll from your sleeve to its last word, with your other palm flat over her heart and her brother's light in it, turned down to the warmth of a hand. It crumbles to ash against your palm. For one breath the light under your hand stings the way it stung in the rock under Kenabres, when his sword went out at your touch and left its fire in you, and then it is only warm. Nobody turns round. Her chest does not move. You leave her there, as she asked.{/n}''',
        c("Continue", "news")),
    nar("open", '''{n}The laboratory. You have lived it again every night since:{/n}
{n}Your blade goes in. She falls, the way the story always meant her to. You are on your knees beside her before anyone can move, the scroll open, reading aloud, your other hand on her heart, and her brother's light coming out through your fingers white and plain as day. Every face in the room turns to you. Someone by the door says your name like a question. The last word, and the scroll goes to ash, and her chest does not move, and you stand up and say, "Leave her. She'll come," and walk out past all of them. Nobody asks you what they saw. They will ask each other for months.{/n}''',
        c("Continue", "news")),
    nar("cold", '''{n}You remember the chapel exactly: the scroll, the breath going into her like a blade, the chaplain praying with his eyes shut. She did not wake while you were there. The priests carried her down to the infirmary on a litter, as one more wounded thing.{/n}''',
        c("Continue", "news")),
    nar("news", '''{n}The runner says that an angel with one black wing is up and washing wounds. She can barely lift the basin. She has not said her name. She asked whether the Knight-Commander was awake.{/n}
{n}By noon Heaven's envoy to the crusade has heard, and by evening the Queen's chaplains have: an angel the lists call dead is changing bandages in Drezen, and nobody can say by whose hand. The envoy withholds his blessing from the next muster until someone explains it.{/n}''',
        c('[Go to her] Go down to the infirmary.', forbids=(OPEN,), crusade=("Favors", -150), flags=(RETURNED, STARTED, STRUCK, SHARD)),
        c('[Go to her] Go down to the infirmary, past the soldiers who saw.', requires=(OPEN,), crusade=("Favors", -300),
          flags=(RETURNED, STARTED, STRUCK, SHARD))),
], requires=("trickster.ever", PRIMED, DEAD), forbids=(RETURNED,), delay=72, TricksterDevice=True, TricksterState=DEAD)


ward(P + "dead.furlough", "A fever that broke at dawn", '"Targona."', [
    nar("start", '''{n}Wilcer Garms points you past the stores with his quill. "She's at the cots, Commander. Hasn't slept. Hasn't asked for a thing but water."{/n}
{n}He lowers his voice. "The Third Company marched out for the east wall this morning without the envoy's blessing. First time since Kenabres. The chaplains stood on the steps and said nothing, and the men noticed. Two of them are on her cots already."{/n}
{n}The angel does not stand when you reach her. She finishes binding a pikeman's hand first, and ties the knot, and only then looks up.{/n}''',
        c("Continue", "pikeman")),
    t("pikeman", '''"Commander. There was a pikeman in your infirmary last night with a fever that would not break. It broke at dawn. I thought you should know that first."
{n}She nods at the two new cots.{/n} "Those men went to the wall unblessed because of me. Heaven's envoy will not bless what he cannot explain, and he cannot explain me. I have told them I am sorry. They did not know what for."
{n}The black wing folds against her back as if it too is listening.{/n}
{n}She sets the basin down with both hands. It is only half full, and still it shakes.{/n}
"I remember your blade. I remember the laboratory, and Areelu's glass, and the floor. Then nothing, and in the nothing, a light I made with my own hands, a long time ago, for my brother. I went towards it. Then I was breathing, and every breath hurt." {n}She flexes her fingers.{/n} "I cannot lift what I lifted a week ago. That is what raising costs. I knew it would."
"I went to the Hand's chaplain before I came here, as I said I would. I told him what was done, and by whom. He let the candle burn down a finger's width before he spoke. Then he blessed me, and not you."''',
      c('[Tell her the truth] "I struck you. I\'d rather you hear it from me than from Heaven."', "truth"),
      c('[Make light of it] "It was a joke. You\'re alive. That\'s the punchline."', "joke"),
      c('[Lie] "Areelu turned my hand. It was never my blow."', "lie")),
    t("truth", '''"Yes. And now Heaven will hear that you said so without being asked." {n}She wrings out the cloth.{/n}
"My brother always said the truth was the hardest gift to give. He was wrong. It is the second hardest. The hardest is forgiving it." {n}She looks at the two unblessed soldiers, and then at you.{/n} "I forgive you, Commander. For those men's sake I will not pretend it is easy."''',
      c('[Promise] "I\'ll try."', flags=(FORGIVEN,))),
    t("joke", '''{n}The basin goes still in her hands.{/n}
"A punchline. I see."
{n}She does not raise her voice. She does not need to.{/n}
"I have work, Commander. Men are dying who never struck anyone."''',
      c('[Go] Leave her to her work.', flags=(UNFORGIVEN,))),
    t("lie", '''{n}She looks at you the way she looked at the wing when Areelu first showed it to her: as a wound she will have to live with.{/n}
"I was there, Commander. I saw your face. It was yours."
{n}She turns back to the pikeman.{/n}
"You are lying to me at the foot of a dying man's cot." {n}She does not lower her voice, and the pikeman in the next cot turns his head.{/n} "Go now. Come back when you can say it."''',
      c('[Go] Leave her to her work.', flags=(UNFORGIVEN, LIED))),
], requires=("trickster.ever", RETURNED, STRUCK), forbids=(CLOSED, FORGIVEN, UNFORGIVEN), delay=0)

ward(P + "dead.second_asking", "The boy with one leg", '"Targona. A word."', [
    t("start", '''{n}She is sitting with a sleeping boy whose left leg is not there any more. A drummer, by the sticks under his pillow. She has her hand on his chest and is counting his breaths under her own. She does not look up.{/n}
"You came back. Have you come to apologise, or to tell me another joke?"''',
      c('[Apologise] "I\'m sorry. I killed you, and I\'m sorry."', "sorry"),
      c('[Send her away] "Go back to Heaven, then."', "sent", flags=(CLOSED,))),
    t("sorry", '''{n}For a moment nothing. Then her hand moves on the boy's chest, very lightly, as if she has felt him turn over in his sleep.{/n}
"There. That was not so hard." {n}It was, and she knows it was.{/n}
"I forgive you, Commander. Not because it is owed. Because I would rather carry this than carry that."''',
      c('"Thank you."', flags=(FORGIVEN,))),
    t("sent", '''"Heaven has healers enough." {n}She tucks the blanket higher round the boy's shoulders.{/n}
"This ward has me. When the war is over I will go home, and I will tell my brother's memory everything, and you will not be in it."''',
      c('[Leave the ward.]')),
], requires=("trickster.ever", UNFORGIVEN), forbids=(CLOSED, FORGIVEN), delay=96)


# --- State freed_in_heaven: the wand that does not run down (F16) ---------------------------------------------------

letter(P + "free.spent_light", "The last wand", [
    nar("start", '''{n}The field infirmary behind the quartermaster's stores is down to its last wand of healing, and the wounded from the day's fighting on the walls are still coming in. The surgeons are rationing it by the charge: one for a lung, none for a hand.{/n}''',
        c(FREED_JOKE, "night", requires=(UMD2,), mythic="Trickster", crusade=("Favors", -300)),
        c('[Spend every charge] "Give it here. And send to the quartermaster for another."', "night_spent", forbids=(UMD2,),
          crusade=("Finances", -500)),
        c('"Leave the rationing to the surgeons."', abort=True)),
    nar("night", '''{n}You take the wand yourself and work down the rows all night, with Lariel's light in your chest behind every word. By dawn every cot has had its charge. The wand has not lost one.{/n}
{n}The chaplains are paid to remember it as an ordinary night. Far above, in the halls of Heaven, someone made from the same soul looks up.{/n}''',
        c('[Finish at dawn] Put the wand away. It is still full.', flags=(PRIMED, WAND))),
    nar("night_spent", '''{n}You take the wand yourself and work down the rows all night. It runs dry before midnight. Wilcer Garms opens the stores and signs out a second one against the war chest without being asked, and then a third, and the crusade's treasurer will hear about it by noon.{/n}
{n}By dawn every cot has had its charge, and three empty wands lie on the table by the door. Far above, in the halls of Heaven, someone who has spent her whole life healing strangers looks up.{/n}''',
        c('[Finish at dawn] Put the empty wands away.', flags=(PRIMED, WAND, CHARGES))),
], requires=("trickster", FREE), forbids=(WAND, TREATED, DEAD), delay=0)

ward(P + "free.furlough", "Greetings, my rescuer", '"There\'s an angel in the wards."', [
    nar("start", '''{n}Wilcer Garms clears his throat. "There's an angel in the wards, Commander. I didn't requisition her."{/n}
{n}She has a basin of water, one wing black and twisted, the other folded tight. She is going down the same rows you went down last night, and she stops at each cot as if the man in it were the only one.{/n}''',
        c("Continue", "greet_lab", requires=(LAB_LINE,)),
        c("Continue", "greet", forbids=(LAB_LINE,))),
    t("greet_lab", '''"Commander. Greetings, my rescuer." {n}She does not smile.{/n}
"Behind the barrier you showed me a scroll up your sleeve and asked me to let everyone mourn me. I said yes. And then you did not need it: you broke the barrier instead. And then someone worked these rows all night with a healer's wand and would not stop. I came to see who would do such a thing, and why."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("greet", '''"Commander. Greetings, my rescuer." {n}She does not smile.{/n}
"Someone worked these rows all night with a healer's wand and would not stop. I felt it in the halls of Heaven, like a hand on my shoulder. I came to see who would do such a thing, and why."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("why", '''"For the wounded." {n}She considers you with sad, clear eyes.{/n}
"Then I will stay, for the wounded. Heaven can spare me for a season, and Heaven's healers have been very kind to me, and very patient with this." {n}The black wing shifts.{/n} "Here nobody has time to be patient with it. I find I prefer that.
"And I would like to know what kind of person uses a dead angel's light to sit up all night with strangers. I have not decided whether I approve."''',
      c('[Welcome her] "Stay as long as they need you."', flags=(MET, STARTED))),
], requires=("trickster.ever", WAND, FREE), forbids=(MET, CLOSED), delay=0)


# --- Shared: the ward (the commit, both states; R2-1) ---------------------------------------------------------------

def night_nodes(prefix=""):
    """Directive 12: the threshold (heat up to the cut, at the start of the act) and the morning after."""
    return [
        nar(prefix + "threshold", '''{n}She does not sleep in the ward. She takes the lamp and leads you up the ladder behind the stores into the drying loft, where the day's washed bandages hang in long rows from the rafters, warm from the stove chimney that runs up through the floor. It is the one warm room in the infirmary that no wounded man needs. She has a blanket up here, and a folded habit for a pillow, and nothing else. She sets the lamp on a crate, and her hands, which have not been empty since the laboratory, are empty.{/n}
{n}"The wing," she says. She turns, so that you can see it: bone and scab and something like torn silk. "Everyone looks away from it. Don't."{/n}
{n}You don't. You put your hand on it, and she shudders from her shoulders to her heels, and kisses you as if she has been holding her breath since the laboratory.{/n}
"I have tended every body in this ward," she says against your mouth. "I want one that is mine to want. Tonight I want yours." {n}She is warm, warmer than anything mortal, and she pulls the plain infirmary smock over her head and lets it fall, and then she is undoing your buckles with a healer's quick, certain hands, and laughing under her breath when one sticks.{/n}
{n}Both wings open over the two of you, one white and one black, and brush the hanging linen so that it sways all down the row. She draws you down under them onto the blanket, and settles over you, and takes your hands and puts them on her hips, and holds them there, and bends to kiss you again with her hair falling round both your faces.{/n}''',
            c("Continue", prefix + "morning")),
        nar(prefix + "morning", '''{n}When the first watch is called she is already back at the cots, sleeves rolled, and when you come down the ladder every man in the ward who can see is suddenly very interested in the canvas overhead.{/n}
{n}There is a black feather on your cloak. Wilcer Garms picks it off at the stores without a word, looks at it, and writes something in his ledger.{/n}
{n}Targona does not look up from the drummer she is feeding. "Go and fight your war, Commander. Come back to me when it lets you."{/n}''',
            c('[Keep the feather.]', flags=(NIGHT,))),
    ]


ward(P + "after.ward", "Sit with this man", '"Is it quiet tonight?"', [
    t("start", '''{n}Wilcer hands you a lamp at the stores without being asked. It is late. There is one lamp lit in the ward, and one man in it who is not sleeping: a Mendevian sergeant, grey in the face, breathing in short pulls. Arrow in the lung, from the east wall.{/n}
"Sit with this man until dawn," Targona says. "Then ask me."''',
      c('[Sit with him until dawn] Sit down on the stool beside the cot.', "dawn"),
      c('[Ask her now] "Ask you now."', "refused"),
      c('[Leave before dawn] "I have a war to run."', "left", flags=(LEFT, CLOSED))),
    t("dawn", '''{n}You hold his hand when he cannot breathe, and talk to him about nothing when he can. Towards the fourth hour he asks for his mother, and you answer him as if you were her. Targona comes and goes and does not interrupt.{/n}
{n}Dawn comes grey through the canvas. The sergeant is asleep, truly asleep, the grey gone out of his lips. Targona puts her hand on his forehead, then takes it away and looks at you.{/n}
"Now you may ask."''',
      c('[Ask her] "Stay with me. Not for a season."', "yes", forbids=(MET,), flags=(COMMITTED,)),
      c('[Ask her whether it was the trick] "Was that you, or something up my sleeve?"', "refused_dawn"),
      c('[Ask her] "Stay with me. Not for a season."', "yes_free", requires=(MET,), flags=(COMMITTED,))),
    t("refused", '''"Not while he's still dying." {n}Her hand stays on the sergeant's chest, counting.{/n}
"Ask me when the ward is quiet. And ask me without a trick in your pocket. I will know."''',
      c('[Accept her answer] "I\'ll wait."', flags=(DECLINED,))),
    t("refused_dawn", '''{n}She looks down at the sergeant. He is sleeping with his mouth open, the way soldiers sleep when nothing hurts enough to wake them.{/n}
"He is asleep, Commander. His lung eased a little before the fourth hour, and after that someone held his hand every time he woke. There was nothing up your sleeve in it, and nothing up mine." {n}She draws the blanket to his chin.{/n}
"You sat all night beside a man who was dying, and when he lived you asked me which trick it was. Iomedae keep me, I do not know whether to laugh or weep. Ask me again when you can believe that a night was only a night."''',
      c('[Accept her answer] "I\'ll wait."', flags=(DECLINED,))),
    t("left",'''"Of course you do." {n}She takes the lamp from you and sets it by the sergeant's head.{/n}
"Then run it, Commander. I will stay with him. Someone should."''',
      c('[Go.]')),
    t("yes", '''{n}She does not answer at once. She washes her hands in the basin, slowly, as if the answer were in the water.{/n}
"One night does not undo the laboratory. Or the men who went to the wall unblessed because of me. Or the chaplain who blessed me and would not bless you." {n}She dries her hands.{/n} "But I watched you all night, and you did not reach for your sleeve once. I have decided to believe that is who you are when the war lets you be. I may be wrong. I would rather find out beside you than from Heaven."
"Yes, Commander. Not for a season."''',
      c("Continue", "threshold")),
    t("yes_free", '''{n}She does not answer at once. She washes her hands in the basin, slowly, and watches the water cloud.{/n}
"The morning after your wand night I came down from the halls of Heaven to judge you. I told my healers so. A season, I said, to see what kind of soul sits up all night with strangers and a dead angel's light." {n}She dries her hands on her smock.{/n}
"Tonight you had no wand. You had a stool, and his hand, and a mother's voice that is not yours. I have judged you at every cot in this ward since, and I keep finding the same thing, and I am tired of pretending it is still a question." {n}The black wing lifts a little behind her, and she lets it.{/n}
"I will write to Heaven and ask for more than a season. Yes, Commander. Not for a season."''',
      c("Continue", "threshold")),
    *night_nodes(),
], requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED), delay=96,
   RequiresAnyGroups=[[FORGIVEN, MET]])

ward(P + "after.quiet_ward", "A quiet ward", '"The ward is quiet."', [
    t("start", '''{n}The ward is quiet. The sergeant has gone back to his company on the east wall. Targona is folding bandages, and she does not stop when you come in.{/n}
"Ask, then. But first promise me something. Whatever you keep up your sleeve, do not use it on death again. Not unnoticed, not for me, not for anyone. If I fall again, let me go. My brother went. I would rather be where he is than be the reason you keep cheating."''',
      c('[Promise, and ask her] "I promise. Stay with me."', "promised", flags=(COMMITTED, SEALED)),
      c('[Refuse the promise] "I can\'t promise that."', "unpromised", flags=(CLOSED,))),
    t("promised", '''{n}She puts the last bandage on the pile and squares it with both hands, very neatly, the way she does when she is trying not to let them shake.{/n}
"Then I will hold you to it. I am told that is what Tricksters hate most." {n}She almost smiles.{/n} "Yes."''',
      c("Continue", "threshold")),
    t("unpromised", '''"No. I did not think you could." {n}She goes on folding.{/n}
"You would do it again for a stranger with a fever, and you might even be right to, and I would never know when it was coming. I cannot live beside that. I am sorry."''',
      c('[Leave her the ward.]')),
    *night_nodes(),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), delay=72)


# --- Epilogue pages (R2-6; ordered siblings, no page effects) -------------------------------------------------------

LIGHT_PARAGRAPHS = (
    p("Heaven's lists still name her among the dead of Areelu's laboratory. Targona never asked to have the entry "
      "struck. She said it was the most honest thing anyone had written about her, and that the angel on that list had "
      "earned her rest.", requires=(SHARD,)),
    p("She came back the hard way, through the chapel and the raise dead scroll, and it took her a year to lift a full "
      "basin again. Four volunteers went into Areelu's ruin for her body. She learned their names, and tended the one "
      "who lost his arm there until the day he died, old, in his bed.", requires=(ECHO_SPENT,)),
    p("The Commander kept the promise made in the quiet ward. It was harder than any vow they had broken, and "
      "Targona knew it, and said so, once.", requires=(SEALED,)),
    p("She told Heaven the truth about the laboratory, as she had said she would, and she told it that the Commander "
      "had told it first. Heaven, she reported afterwards, was not amused. She was.", requires=(FORGIVEN,), forbids=(SEALED,)),
)


# The wand night belongs to the freed state only; the death-return ward never had it.
WARD_PARAGRAPHS = (
    p("The wounded who passed through it swore that its one wand of healing never ran down. She never let the Commander "
      "use it.", requires=(WAND,), forbids=(CHARGES,)),
    p("Three empty wands hung on a nail by its door, from the night the Commander emptied the stores for strangers. "
      "The treasurer's bill for them hung beside them, receipted, and she would not let anyone take either down.",
      requires=(CHARGES,)),
)


def page(id, title, text, requires, forbids=(), paragraphs=(), **extra):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [nar("end", text, paragraphs=paragraphs)], requires=requires,
                        forbids=forbids, last=99, Relationship="targona", **extra))


page(P + "epilogue.commit", "When the ward was quiet",
     '''{n}Targona did not go back to Heaven when the war ended. She stayed in Drezen's field infirmary until the last cot was folded, and on the morning the tents came down she found the Commander and asked the question herself, because, she said, she had waited for the ward to be quiet, and it finally was.{/n}''',
     requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED), paragraphs=LIGHT_PARAGRAPHS,
     RequiresAnyGroups=[[FORGIVEN, MET]])

page(P + "epilogue.declined", "The stool by the last cot",
     '''{n}Targona returned to the halls of Heaven with the last of the wounded she could not leave. She never did hear the question asked without a trick in it. In Drezen's infirmary there is still a stool beside the last cot that nobody sits on.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(COMMITTED,))

page(P + "epilogue.furlough", "A wand that never ran down",
     '''{n}Heaven granted Targona her furlough, and then another, and then stopped counting. She kept a ward in Drezen with the Commander's name over the door.{/n}''',
     requires=("trickster.ever",), forbids=(CLOSED, DECLINED), paragraphs=WARD_PARAGRAPHS + LIGHT_PARAGRAPHS,
     RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED]], ForbidOverrides={DECLINED: COMMITTED})


# --- Reactions (ledger 05 section 3.1 row 39: exactly Seelah, Sosiel and Ember) -------------------------------------

REACTIONS = [
    reaction("Seelah", P + "react.seelah_furlough", (RETURNED,),
             '''"There's an angel in the infirmary changing bandages. She asked me not to kneel. I knelt anyway."
{n}Seelah turns her helmet over in her hands.{/n}
"...She says you killed her once. Is that true? No. Don't answer. I'll ask Iomedae, and then I'll ask you, and one of you had better have a good story."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone"), chapter=3, last=5, Chapters=[3, 5],
             # G6(b): a Seelah who died or left and came back on her own Trickster route is on her hub again.
             ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"},
             entry='"You\'ve been to the infirmary."'),
    reaction("Sosiel", P + "react.sosiel_forgiven", (FORGIVEN,),
             '''"She forgave you in front of the whole ward."
{n}Sosiel is quiet for a moment, the brush idle in his hand.{/n}
"I don't think she meant it as mercy, Commander. I think she meant it as a debt. The kind you pay back by becoming someone who deserved it."''',
             answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=3, last=5, Chapters=[3, 5],
             entry='"You look thoughtful."'),
    reaction("Ember", P + "react.ember_wand", (IN_DREZEN,),
             '''"The angel has a sad wing and a happy face. She let me hold the wand while she worked."
{n}Ember turns her empty hands over.{/n}
"It never got lighter. Things always get lighter when you use them. Not that one. I think it's being kind on purpose."''',
             answer_list=EMBER_HUB, forbids=("ember_dead", "ember_gone"), chapter=3, last=5, Chapters=[3, 5],
             entry='"What have you been up to?"'),
]
SCENES.extend(REACTIONS)


def integrate(payload):
    """Save-safe: the registered correspondence route is untouched (no id, node or choice changed). Adds the Trickster
    access, the laboratory override, the presence and one Guidance sentence."""
    rel = payload["Relationships"]["targona"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Commander who uses Lariel's light without spending it, in Areelu's "
                        "laboratory or in Drezen's field infirmary, may find Targona at the cots behind the "
                        "quartermaster's stores in Chapter 3 or Chapter 5.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
