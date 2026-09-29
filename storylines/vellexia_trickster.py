"""Vellexia on the Trickster path: the joke told backwards (Writer/handoffs/trickster/vellexia.md; F08, F11 secondary).

Canon: a Trickster Commander can turn Vellexia into a mirror with her own spell (Velexia_Third_Date/Answer_0071 c80a4ad4 and
Answer_0091 14f0b9d2, MythicRequirement PlayerIsTrickster; Cue_0079 42429350: "a magnificent mirror stands before you, its
surface shrouded in a dark, mysterious haze", OnStop VellexiaKilled). Cue_0067 cf9bb281 invites it ("Perhaps you are also
eligible for some compensation?"). Cue_0075 834295fb names the price of undoing her work ("leave my house with bare walls").
Cue_0136 e3f0b327: a crude copy leaves "part of [the soul] still lost somewhere". Her thesis on love is self-deception that
ends with one throat opened (Velexia_Main/Cue_0085 ec58f45a); Jerribeth: "Vellexia's greatest enemy is her own boredom"
(Jerribeth_Velexia/Cue_0015 10053d3c). Authored, and labelled so in the spec: the mirror crated as compensation; the
unpainted hands of her enchanted portrait; the Storyteller's guess that part of her stayed in it; Orrel Vask, a cambion
haulier and wine-factor between the Upper City and Drezen. She is a demon of the Upper City: she prices, punishes the
dull, is never grateful, and can end it.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"
UNIT = "a32a07903e428d34cb0e98a804d40569"          # Vellexia_Default (no dialog component; the presence copy)
FYE = "0f12118177d102f428a3b30b15b132eb"           # Fye_Bartender, the presence anchor
ST_HUB = "2f5b7e0b76d3c5a42a431e1e33a8db09"        # NPC_Common/StoryTeller_MainDialogue/AnswersList_0004
ST_RETURN = "34a0d078b4ac51547a8f5e0e1c8e1e2c"     # StoryTeller_MainDialogue/Cue_0880 "The Storyteller nods, saying nothing."
QM_HUB = "3c58e83a970a0f643a88e15f2323c805"        # NPC_Common/Vendor_Quartermaster/AnswersList_0003 (Wilcer Garms)
FINNEAN_HUB = "615ef80243cfc184ba42286395880b0e"   # CompanionDialogues/Finnean/AnswersList_0003
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"    # CompanionDialogues/Daeran/AnswersList_0003

MIRROR = "vellexia.mirrored"
DEAD = "vellexia.dead"
PRIMED = "vellexia.trickster.primed"
DECLINED = "vellexia.trickster.declined"
RETURNED = "vellexia.trickster.returned"
UNMIRRORED = "vellexia.trickster.unmirrored"
KEPT = "vellexia.trickster.kept_as_mirror"
PRESUMED = "vellexia.trickster.presumed_dead"
ENTRY = "vellexia.trickster.entry"
MARKED = "vellexia.trickster.portrait_marked"
LATE = "vellexia.trickster.cost.late"
BARE = "vellexia.trickster.cost.bare_walls"
WATCHED = "vellexia.trickster.cost.watched"
DIMINISHED = "vellexia.trickster.cost.diminished"
PREDICTED = "vellexia.trickster.cost.predicted"
TRICK_KEPT = "vellexia.trickster.cost.trick_kept"
LESSON = "vellexia.trickster.lesson_given"
VISITED = "vellexia.trickster.visited"
COURTING = "vellexia.trickster.courting"
LATE_COMMITTED = "vellexia.trickster.late_committed"
KNOWN = "vellexia.prediction_known"
STARTED = "vellexia.started"
FAILED = "trickster.failed"
ST_DEAD = "storyteller.dead"
OWN = ("vellexia.closed", "inhuman")
DAERAN_GONE = ("daeran.dead", "daeran.kicked_out")

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED, "vellexia.early_fight": RETURNED, "vellexia.final_fight": "vellexia.fight_survived"},
    TricksterAccess={
        MIRROR: dict(detect=[MIRROR, DEAD, "vellexia.final_fight"], device="vellexia.trickster.mirrored.speaks", returned=RETURNED),
        DEAD: dict(detect=[DEAD, "vellexia.early_fight", "vellexia.final_fight"], device="vellexia.trickster.sword.portrait",
                   returned=RETURNED),
    })
# Every registered scene that Forbids her death or the mirror lifts it after a return (G6(b)); the spared world lifts
# final_fight through fight_survived (VEL-02).
FO = {DEAD: RETURNED, "vellexia.early_fight": RETURNED, "vellexia.final_fight": "vellexia.fight_survived", MIRROR: RETURNED}
PRESENCES = {
    # A spawned copy of her Upper City unit (CutsceneNeutrals, no dialog) beside Fye's bar; Dialog "hub" makes it
    # talkable. If Fye has left the capital the anchor fails and vellexia.presence.failed opens the quarters twin.
    "vellexia.presence": dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FYE, Side="front", Distance=2.0),
                              Requires=["trickster.ever", "vellexia.trickster.in_person"],
                              Forbids=["vellexia.closed", KEPT, VISITED], MinChapter=5, MaxChapter=5, AnswerLists=[],
                              Dialog="hub",
                              Greeting="{n}Vellexia is leaning on Fye's bar as if she had bought it. Judging by Fye's face, "
                                       "she is considering it.{/n}"),
}


def v(id, text, *choices, **kw):
    return n(id, "Vellexia", text, *choices, portrait="Vellexia", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Vellexia", **kw)


def teller(id, text, *choices):
    """The Storyteller speaking inline in his own dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


def glass(id, text, *choices):
    """Vellexia's voice in the Storyteller scenes: her own unit's name and portrait inline (E14f), narrated on book pages.
    Inline, a node spoken by the scene owner would otherwise borrow the native return cue's speaker (the Storyteller)."""
    return n(id, "Vellexia", text, *choices, portrait="Vellexia", speaker_unit=UNIT)


def letter(id, title, nodes, requires, forbids, delay, chapters=(5,), area=DREZEN, **extra):
    SCENES.append(scene(id, title, "Vellexia", min(chapters), "", nodes, requires=requires, forbids=(*OWN, *forbids),
                        delay=delay, last=max(chapters), optional=True, Relationship="vellexia", Areas=[area],
                        Chapters=list(chapters), Remote=True, **extra))


def storyteller(id, title, entry, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Vellexia", 5, entry, nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="vellexia", Chapters=[5], AnswerLists=[ST_HUB],
                        NativeReturnCue=ST_RETURN, **extra))


def stores(id, title, entry, nodes, requires, forbids, delay, **extra):
    SCENES.append(scene(id, title, "Vellexia", 5, entry, nodes, requires=requires, forbids=(*OWN, *forbids), delay=delay,
                        last=5, optional=True, Relationship="vellexia", Areas=[DREZEN], Chapters=[5],
                        AnswerLists=[QM_HUB], **extra))


# --- State mirrored: the joke told backwards (F08) ------------------------------------------------------------------

letter("vellexia.trickster.mirrored.speaks", "Compensation", [
    nar("start", '''{n}The Nexus, the night after the prank. Two of your people have come back from the Upper City with her dust sheet folded over one arm, as if it were evidence.{/n}
{n}The mirror is still standing in her salon. The looters who went in after her guests fled came out again quickly, and would not say why.{/n}''',
      c("Continue", "finnean", requires=("finnean.objected",)),
      c("Continue", "crate", forbids=("finnean.objected",))),
    nar("finnean", '''{n}Finnean has not said a word since the salon. Now, from the scabbard, very quietly:{/n}
"She's awake in there, Commander. You can tell by the way it doesn't reflect anything. I know what that's like. I'm just saying."''',
      c("Continue", "crate")),
    nar("crate", '''"It's heavy, Commander," says the quartermaster who went back for it. "Heavy as a wardrobe, and warm, like somebody's been leaning on it. The haze moves when you talk near it. Do we crate it for Drezen, or leave it for the looters?"''',
      c('[Have the mirror crated for Drezen] "I wasn\'t entertained either. She\'s my compensation."', "crated"),
      c('[Throw a sheet over the glass and leave it] "Goodnight, Lady Vellexia."', "sheet")),
    nar("crated", '''{n}They crate it face to the planks, on your orders, with straw packed against the glass. By morning the straw is warm right through.{/n}
{n}Just before they nail the lid down, the haulers hear it: a single tap from inside, like a fingernail on glass, testing whether anyone is listening.{/n}''',
      c('"Mind the corners."', flags=(PRIMED, STARTED))),
    nar("sheet", '''{n}Your people go back and throw the sheet over the glass. Under it, the haze goes still.{/n}
{n}A mirror stands in an empty salon in Alushinyrra, and the looters leave it alone. Whoever buys the house will get a mirror nobody likes to look into.{/n}''',
      c('"Leave her there."', flags=(DECLINED,))),
], requires=("trickster.ever", MIRROR, DEAD), forbids=(PRIMED, DECLINED, RETURNED), delay=0, chapters=(4,), area=NEXUS,
   TricksterDevice=True, TricksterState=MIRROR)

letter("vellexia.trickster.mirrored.fetch", "A mirror nobody will loot", [
    nar("start", '''{n}Drezen. A cambion haulier named Orrel Vask, who moves furniture between the Upper City and anyone who pays, sends word up from the rift camp with a sample of Alushinyrran red.{/n}
{n}A certain mirror, his note says, is still standing in a certain empty salon. The looters will not touch it, because it watches them. He can have it out through the Nexus portals within the week. He names a price, and then, in a second hand, a surcharge "for the eyes".{/n}''',
      c('[Pay the haulers double to bring it out] "Double, if it arrives uncracked. It\'s a lady."', "paid",
        crusade=("Finances", -200)),
      c('[Let the Upper City keep its mirror] "Somebody else can look at her."', "left")),
    nar("paid", '''{n}Vask's crate comes up the rift road on the ninth day, packed in straw that is warm to the touch. He will not unload it himself. His porters set it down in the corner of your stores and back away from it as if it had spoken.{/n}
{n}Perhaps it had. None of them will say.{/n}''',
      c('"Put it in the stores. I\'ll deal with her."', flags=(PRIMED, LATE, STARTED))),
    nar("left", '''{n}You send Vask a single line: no. He sends back a single line of his own, which is his invoice for the letter.{/n}
{n}In Alushinyrra, a mirror stands under a sheet in an empty salon, and goes on standing there.{/n}''',
      c('"Pay the man for his ink."', flags=(DECLINED,))),
], requires=("trickster.ever", MIRROR, DEAD), forbids=(PRIMED, DECLINED, RETURNED), delay=0,
   TricksterDevice=True, TricksterState=MIRROR)

NICE_FLAGS = (RETURNED, UNMIRRORED, BARE, PRESUMED, KNOWN, STARTED)
CRUEL_FLAGS = (RETURNED, KEPT, WATCHED, PRESUMED, KNOWN, STARTED)
NICE_JOKE = '[Play a nice trick on Vellexia] "Stay just so. I\'m going to tell it backwards."'
CRUEL_JOKE = '[Play a cruel trick on Vellexia] "Stay a mirror. You\'ll never be bored. Everyone looks at you."'


def unmirror_nodes():
    """The shared close of both unmirrorings: the joke told backwards, or kept as it is."""
    return [
        glass("glass", '''{n}A face forms in the haze, pale and furious and very interested.{/n}
"Oh, do go on. Tell {mf|him|her} the part where I was magnificent."''',
              c(NICE_JOKE, "nice", mythic="Trickster", alignment=("Chaotic", 1), forbids=(FAILED,)),
              c(CRUEL_JOKE, "cruel", mythic="Trickster", alignment=("Evil", 1), forbids=(FAILED,)),
              c('[Tell it backwards, without the sparks] "Stay just so. I\'m going to tell it backwards."', "no_sparks",
                alignment=("Chaotic", 1), requires=(FAILED,)),
              c('[Leave her in the glass] "Stay a mirror. You\'ll never be bored. Everyone looks at you."', "no_sparks_cruel",
                alignment=("Evil", 1), requires=(FAILED,)),
              c('[Cover the mirror again] "Not yet."', abort=True)),
        nar("no_sparks", '''{n}Your fingers find no sparks. The joke, it seems, remembers how it went.{/n}''', c("Continue", "nice")),
        nar("no_sparks_cruel", '''{n}Your fingers find no sparks. You do not need any. You only have to walk away.{/n}''',
            c("Continue", "cruel")),
        nar("nice", '''{n}You say her spell backwards: the last word first, the way you heard her say it to a juggler who bored her. The haze curdles into a shoulder, a knee, a fistful of blonde hair, and then an extremely angry succubus is sitting on the floor in a heap of mahogany splinters.{/n}
{n}Far away in the Upper City, in a salon with nobody in it, a great many chairs stand up.{/n}''',
            c("Continue", "undone")),
        glass("undone", '''"How thrilling. You undid me. Nobody undoes me."
{n}She gets up without taking the hand nobody offered her, and shakes a splinter out of her sleeve.{/n}
"You will show me how, and then you will do it again, slowly, so I can learn it. And then, sweetheart, we will discuss what you owe me for my furniture. I heard every chair in my house walk out of the door. Every one."''',
          c('"Welcome back, Lady Vellexia."', flags=NICE_FLAGS)),
        nar("cruel", '''{n}The haze thins. For a moment you see only your own reflection, looking very pleased with itself.{/n}
{n}Behind it, two enormous eyes are wide awake.{/n}''', c("Continue", "watched")),
        glass("watched", '''"You will regret this for a very long time, Golarian. And I will be watching you do it."''',
              c('"Hang her somewhere with a good view."', flags=CRUEL_FLAGS)),
    ]


storyteller("vellexia.trickster.mirrored.unmirror", "The joke told backwards",
    '[Have the crated mirror brought in] "This was a succubus, once. Tell me its story."', [
    teller("start", '''{n}The old elf has the porters stand the crate against his shelves. He lifts the sheet himself and looks into the haze until the lamp beside it starts to gutter.{/n}
"Mahogany that remembers being skin. She was bored, Commander. Then she was surprised. Then she was this." {n}He lets the sheet fall back halfway.{/n} "I read the story forwards. I cannot read it any other way. You, I think, can."''',
           c("Continue", "glass")),
    *unmirror_nodes(),
], requires=("trickster.ever", PRIMED, MIRROR, DEAD), forbids=(RETURNED, DECLINED, ST_DEAD), delay=24,
   TricksterDevice=True, TricksterState=MIRROR)

# The Storyteller is dead: the crate has stood in the quartermaster's stores since it arrived. Fye leaves the capital
# when the tavern is lost (Fye_Bartender_NotInCapital 60d1237d), so the stores host this twin, not his bar.
stores("vellexia.trickster.mirrored.unmirror_stores", "Behind the lamp oil",
    '[Ask about the crate in the corner] "That mirror. Take the straw off it."', [
    nar("start", '''"Your glass, Commander." {n}Wilcer Garms has had the crate stood in the far corner of the stores, behind the lamp oil, as far from the door as it will go.{/n} "It hums when the stores go quiet. The boys won't count stock near it after dark. I'd like it gone, or I'd like it paid for."
{n}There is nobody left in Drezen who reads the stories in things. You will have to tell this one yourself, from the end.{/n}''',
        c("Continue", "glass")),
    *unmirror_nodes(),
], requires=("trickster.ever", PRIMED, MIRROR, DEAD, ST_DEAD), forbids=(RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState=MIRROR)


# --- State killed_by_sword: the unfinished likeness (F08) ------------------------------------------------------------

letter("vellexia.trickster.sword.portrait", "The one with no hands", [
    nar("start", '''{n}The Nexus, the night she died. Her manor is being stripped before it is cold. Your people bring back an inventory, because you asked for one.{/n}''',
      c("Continue", "freed", requires=("vellexia.slaves_freed",)),
      c("Continue", "gallery", forbids=("vellexia.slaves_freed", "vellexia.returned_picture")),
      c("Continue", "bought_back", requires=("vellexia.returned_picture",), forbids=("vellexia.slaves_freed",))),
    nar("freed", '''{n}When she fell, every chair, lamp and footstool in her house stood up and walked out of the door on two legs. The inventory is very short.{/n}
{n}One item did not walk. It was never anyone. The unfinished portrait still hangs in the gallery where you last saw it, the hands still bare underpaint, and on the back, your chalk mark.{/n}''',
      c("Continue", "choice")),
    nar("gallery", '''{n}The inventory runs to eleven pages of furniture that watches the looters work. Near the bottom, in a clerk's cramped hand: one portrait, unfinished, hands unpainted, chalk mark on reverse. Gallery.{/n}''',
      c("Continue", "choice")),
    nar("bought_back", '''{n}Near the bottom of the inventory, in a clerk's cramped hand: one portrait, unfinished, hands unpainted, chalk mark on reverse. Gallery.{/n}
{n}She sent it back to its artist, the afternoon you told her to. Then, it seems, she bought it back from him at twice his price. She never mentioned it.{/n}''',
      c("Continue", "choice")),
    nar("choice", '''"Everything else in that house used to be somebody," says the soldier who brought the list. "That thing never was. The looters want it for the frame. Take it, or let them burn the canvas?"''',
      c('[Take the portrait you marked] "The only thing in that house that was never anyone. I\'ll have it."', "taken"),
      c('[Put the portrait to the torch] "Burn it. She\'s had enough admirers."', "burned")),
    nar("taken", '''{n}They roll the canvas off its stretcher and bring it back in an oilcloth. It is heavier than a canvas should be, and it does not like being rolled. By morning it has straightened itself inside the cloth.{/n}''',
      c('"Keep it dry."', flags=(PRIMED, STARTED))),
    nar("burned", '''{n}The canvas goes up quickly. The frame burns slowly. The soldiers who watched it say, afterwards, that the painted face did not change at all, and that they wish it had.{/n}''',
      c('"Enough."', flags=(DECLINED,))),
], requires=("trickster.ever", DEAD, MARKED), forbids=(MIRROR, PRIMED, DECLINED, RETURNED), delay=0, chapters=(4,),
   area=NEXUS, TricksterDevice=True, TricksterState=DEAD)

letter("vellexia.trickster.sword.late_portrait", "A likeness by the yard", [
    nar("start", '''{n}Drezen. Orrel Vask, the cambion haulier who strips dead lords' houses in the Upper City, is selling Lady Vellexia's gallery by the yard through the rift camp. His list reaches you with the morning dispatches and a note about Alushinyrran red.{/n}''',
      c("Continue", "marked", requires=(MARKED,)),
      c("Continue", "unmarked", forbids=(MARKED,))),
    nar("marked", '''{n}You tell him which canvas you want. He already knows which one. It is the one with a chalk mark on the back, in your hand, and he has been holding it back from the other buyers to see what you would pay.{/n}''',
      c("Continue", "price")),
    nar("unmarked", '''{n}Most of the list is paintings of her. One entry is not like the others: "Likeness, unfinished. Nobody sat for it. The hands were never painted. The lady kept it facing the wall." Vask has underlined it, and written "cheap" beside it, and then crossed out "cheap".{/n}''',
      c("Continue", "price")),
    nar("price", '''{n}His price for that one canvas is the price of a good warhorse. His postscript says he is charging for the frame he will not be sending.{/n}''',
      c('[Pay Orrel Vask to cut one portrait out of her gallery] "The one with no hands. Leave the frame."', "paid",
        crusade=("Finances", -200)),
      c('[Let the gallery burn with the rest] "She\'s had enough admirers."', "refused")),
    nar("paid", '''{n}The canvas comes up the rift road rolled in oilcloth, and Vask's porter will not hand it over until you have counted his master's second fee into his palm. It is heavier than a canvas should be.{/n}''',
      c('"Keep it dry."', flags=(PRIMED, LATE, STARTED))),
    nar("refused", '''{n}You write back one word. Vask sells the rest of the gallery to a factor from the Fleshmarkets, and the unfinished one goes into a brazier on a wharf.{/n}''',
      c('"Enough."', flags=(DECLINED,))),
], requires=("trickster", DEAD), forbids=(MIRROR, PRIMED, DECLINED, RETURNED), delay=0,
   TricksterDevice=True, TricksterState=DEAD)

LIKENESS_JOKE = '[Play a nice trick on Vellexia\'s portrait] "Everyone in her house used to be someone. Her turn."'
LIKENESS_FLAGS = (RETURNED, DIMINISHED, PRESUMED, KNOWN, STARTED)


def likeness_nodes():
    return [
        nar("spell", '''{n}Sparks come off your fingers, the same ones you watched come off hers in the Upper City. The canvas takes on the weight of flesh. Paint becomes a throat, a breath, a woman sitting up in the lamplight with her skirts still wet at the hem.{/n}''',
            c("Continue", "wake")),
        glass("wake", '''"...Oh."
{n}She lifts her hands. They are flawless, and nothing comes of them: no spark, no warmth, only paint-deep perfection.{/n}
"He never finished them. You brought me back unfinished. How dare you. How wonderful." {n}She flexes the fingers, watching them do nothing.{/n} "Finish me, sweetheart, or I will find out who can."''',
          c('"Welcome back, Lady Vellexia."', flags=LIKENESS_FLAGS)),
        nar("no_sparks", '''{n}No sparks come. You do it the long way instead: her spell, word for word, the way you heard her say it to a juggler who bored her, and your hand flat on the painted throat until the paint is warm.{/n}''',
            c("Continue", "spell")),
    ]


LIKENESS_CHOICES = (
    c(LIKENESS_JOKE, "spell", mythic="Trickster", alignment=("Chaotic", 1), forbids=(FAILED,)),
    c('[Cast her spell from memory] "I watched you do this to a juggler. Stay where you are."', "no_sparks",
      alignment=("Chaotic", 1), requires=(FAILED,)),
)

storyteller("vellexia.trickster.sword.likeness", "The unfinished likeness",
    '[Unwrap the unfinished portrait] "She\'s dead. This isn\'t. Tell me what you see."', [
    teller("start", '''{n}The Storyteller holds the canvas at arm's length, then close, then at arm's length again.{/n}
"A likeness nobody sat for. The painter reached the eyes and the smile and never the hands. And something in it did not go where the rest of her went."
{n}He sets it down very carefully.{/n} "I read that as a guess, Commander. I would not bet my life on it. You might bet hers."''',
           *LIKENESS_CHOICES,
           c('"She told me herself: a crude copy leaves something behind. This is a very crude copy."', "foresight",
             requires=("vellexia.bungler_explained",)),
           c('[Wrap it up again] "Not yet."', abort=True)),
    teller("foresight", '''"Did she." {n}The old elf looks at the canvas again, as if it had interrupted him.{/n} "Then you are not guessing. You are collecting on something she said to you. That is a different kind of story, and I do not think it ends kindly for anyone in it."''',
           *LIKENESS_CHOICES,
           c('[Wrap it up again] "Not yet."', abort=True)),
    *likeness_nodes(),
], requires=("trickster.ever", PRIMED, DEAD), forbids=(MIRROR, RETURNED, DECLINED, ST_DEAD), delay=24,
   TricksterDevice=True, TricksterState=DEAD)

stores("vellexia.trickster.sword.likeness_stores", "Paint that watches",
    '[Ask about the canvas in the oilcloth] "That portrait. Unroll it."', [
    nar("start", '''"She's been staring at the boys for a week, Commander." {n}Wilcer Garms has pinned the canvas to the wall of the stores with four nails and hung a sack over it, and the sack keeps sliding off.{/n} "The eyes follow you. The hands don't. I'd take it kindly if you did whatever you're going to do with it somewhere else."
{n}There is nobody left in Drezen who reads the stories in things. You will have to trust your own guess.{/n}''',
        *LIKENESS_CHOICES,
        c('[Leave it on the wall] "Not yet."', abort=True)),
    *likeness_nodes(),
], requires=("trickster.ever", PRIMED, DEAD, ST_DEAD), forbids=(MIRROR, RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState=DEAD)


# --- State never_visited: an invitation to a party she has not yet decided to throw (F11) ---------------------------

letter("vellexia.trickster.never_visited.invitation", "A party in your honour", [
    nar("start", '''{n}Officers over Alushinyrran red in Drezen, the night the walls hold. The wine came up through the rifts with a cambion factor named Orrel Vask, who sells the Upper City its gossip on the way back down.{/n}
{n}Somebody asks whether you met the famous Lady Vellexia while you were in the Abyss. The one who collects guests, and keeps the ones who bore her as furniture.{/n}''',
      c('[Boast about the Upper City, and tip the wine-factor to carry it word for word] "Lady Vellexia? Charming. She\'s throwing a party in my honour. She just doesn\'t know it yet."',
        "card", mythic="Trickster", crusade=("Finances", -100)),
      c('[Change the subject] "The Abyss? I don\'t talk about the Abyss."', "silent")),
    nar("card", '''{n}Vask laughs, pockets the coin, and repeats it back to you word for word, twice, so there can be no mistake.{/n}
{n}Nine days later he is back, with lilac on his cuffs and a card he will not let anyone else touch. It invites you to a party that its hostess, by her own admission in the postscript, has not yet decided to throw.{/n}
{n}"Tell me who told you I would," the postscript ends. "I should like to have them upholstered."{/n}''',
      c('"Tell her I\'ll come."', flags=(ENTRY, PRIMED, PREDICTED, KNOWN, STARTED))),
    nar("silent", '''{n}The table moves on to the siege. Vask sells the rest of his red to the quartermaster, and takes no message back down the rift with him.{/n}''',
      c('"Pour."', flags=(DECLINED,))),
], requires=("trickster", "chapter_later"), forbids=("vellexia.greeted", DEAD, ENTRY, DECLINED), delay=0)


# --- After any return: the test in person (R2-1, R2-3) -----------------------------------------------------------------

SHELL = '''{n}She sets a silver-rimmed shell on the bar, the size of her palm, with a cover of cloudy glass. It is warm from her hand.{/n}
"An echo shell. Open it and it asks for me. I may answer. I may be busy. I am going home, sweetheart. My house is a ruin and I am told I am dead, and I have decided to find both restful, for a season." {n}She does not look back from the door.{/n}'''
SHELL_HELD = '''{n}She taps the silver rim of the shell at your belt, the one she gave you in her manor, the day she decided you might be worth an afternoon.{/n}
"You kept it. Good. Keep it open. I may answer. I may be busy. I am going home, sweetheart. My house is a ruin and I am told I am dead, and I have decided to find both restful, for a season." {n}She does not look back from the door.{/n}'''


def visit_nodes(place_text):
    return [
        nar("start", place_text,
            c("Continue", "unmirrored", requires=(UNMIRRORED,)),
            c("Continue", "diminished", requires=(DIMINISHED,), forbids=(UNMIRRORED,)),
            c("Continue", "entry", requires=(ENTRY,), forbids=(UNMIRRORED, DIMINISHED))),
        v("unmirrored", '''"Show me. Now, here, with the whole room watching." {n}She turns on the stool so the room can see her do it.{/n} "If you can make a woman into a thing and back again, you can make a tavern into a stage for an hour. Everyone in the Upper City thinks I am dead. I would like one person to see me being alive."''',
          c('[Show her how the trick works] "Watch my hands. Not my face. Everyone watches the face."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("diminished", '''"Look at them." {n}She lays her perfect, useless hands on the bar, palms up, where the lamplight can find every flaw in them. There are none. That is the flaw.{/n}
"I have tried every spell I know. They move like hands and they do nothing like mine. You will finish me. Or you will tell me who can. Choose which one you would like me to believe."''',
          c('[Show her how the trick works] "It was your spell. I said it from memory. Watch my mouth, not my hands."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("entry", '''"So this is the prophet." {n}She looks you over the way she looks over furniture.{/n} "I came to see who predicted me. Nobody predicts me. It has put me in a very bad mood, and I have come a long way to enjoy it."
"Predict me, sweetheart. What do I do next?"''',
          c('[Tell her how it was done] "A wine-factor, a boast and nine days. That\'s all a prophecy is."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        nar("gave", '''{n}She watches as you explain it, and not your face. When you finish she says nothing at all, which is the most frightening thing you have seen her do.{/n}''',
            c("Continue", "gave_end")),
        v("gave_end", '''"Again. Slower."
{n}You do it again. She mouths it with you, the way a duellist mirrors a lesson, and her eyes do not leave you once.{/n}
"There. Now I own it too. How generous of you. Generosity is so rarely interesting; I shall have to decide what it means."''',
          c("Continue", "shell_held", requires=("vellexia.seal_agreed",)),
          c("Continue", "shell", forbids=("vellexia.seal_agreed",))),
        v("kept", '''"Oh, good." {n}She is delighted, and it is not a pleasant sight.{/n}
"Keep it, then. I shall take it from you eventually. It will be so much more fun than being given it. Do you know how long it has been since anyone kept anything from me? Neither do I."''',
          c("Continue", "kept_shell_held", requires=("vellexia.seal_agreed",)),
          c("Continue", "kept_shell", forbids=("vellexia.seal_agreed",))),
        nar("shell", SHELL, c('[Take the shell.]', flags=(VISITED, LESSON))),
        nar("shell_held", SHELL_HELD, c('[Let her go.]', flags=(VISITED, LESSON))),
        nar("kept_shell", SHELL, c('[Take the shell.]', flags=(VISITED, TRICK_KEPT))),
        nar("kept_shell_held", SHELL_HELD, c('[Let her go.]', flags=(VISITED, TRICK_KEPT))),
    ]


SCENES.append(scene("vellexia.trickster.after.visit", "Beside the bar", "Vellexia", 5,
    '"Lady Vellexia. You look well, for a dead woman."', visit_nodes(
        '''{n}She is sitting at Fye's bar in the middle of a siege as if it were a salon, in a borrowed cloak with the lining turned out to show the silk. Every soldier in the room is pretending not to look at her. Fye has put a clean cup in front of her and is standing as far away from it as the bar allows.{/n}'''),
    requires=("trickster.ever",), forbids=(*OWN, KEPT, VISITED), delay=24, last=5, optional=True, Relationship="vellexia",
    Areas=[DREZEN], Chapters=[5], ContactUnit=UNIT, InteractionHub="vellexia.presence",
    RequiresAnyGroups=[[UNMIRRORED, DIMINISHED, ENTRY]]))

# The anchor failed (Fye has left the capital): she comes to the Commander's quarters instead, the same test in person.
letter("vellexia.trickster.after.visit_quarters", "A guest who was not invited", visit_nodes(
    '''{n}Fye's is shut and boarded, so she has come to your quarters instead. The sentry at your door let her in. He will not be able to explain why, afterwards, and he will not try very hard.{/n}
{n}She is sitting in your chair with her feet on your maps of the Worldwound, and she has already read them.{/n}'''),
    requires=("trickster.ever", "vellexia.presence.failed"), forbids=(KEPT, VISITED, "vellexia.trickster.after.visit"),
    delay=48, RequiresAnyGroups=[[UNMIRRORED, DIMINISHED, ENTRY]])


# --- The first call: her price, spoken; the registered evenings follow (return_kept) -----------------------------------

letter("vellexia.trickster.after.voice", "Bare walls", [
    nar("start", '''{n}The shell lights on your table in the small hours, while the watch is changing on the walls. When you open it, Vellexia is sitting in a room with nothing in it but her.{/n}''',
      c("Continue", "bare", requires=(UNMIRRORED,)),
      c("Continue", "hands", requires=(DIMINISHED,), forbids=(UNMIRRORED,)),
      c("Continue", "predicted", requires=(PREDICTED,), forbids=(UNMIRRORED, DIMINISHED))),
    v("bare", '''"My house has bare walls, darling. Every chair I ever made has walked off to find its mother. The looters took the curtains. The Upper City has held two memorial feasts for me and I was not invited to either."
{n}She turns the shell so you can see the room: a floor, a window, a woman standing in the middle of both.{/n}
"I am told I am dead. I have decided to find that restful. It is costing me a fortune."''',
      c("Continue", "trick")),
    v("hands", '''{n}She holds up her hands to the glass. They are flawless, and nothing comes of them.{/n}
"I went to a painter. A very good one. He looked at them for an hour and then he wept, and I had him thrown down the stairs, and then I had him carried back up to finish weeping. Nobody in the Upper City can finish me. Finish me."''',
      c("Continue", "trick")),
    v("predicted", '''"You predicted me. Nobody predicts me." {n}She lets that sit, on the far side of the glass.{/n}
"Say something dull now and I will know it was luck."''',
      c('"Then I won\'t say anything. Guess what I\'m thinking."', "trick"),
      c('"I\'m glad you came to Drezen."', "dull")),
    v("dull", '''"There. Luck." {n}Her face goes smooth and polite, which is worse than anger.{/n} "One. People who bore me get three, and nobody has ever had three. Do not become the first."''',
      c("Continue", "trick", flags=("vellexia.trickster.cost.bored_once",))),
    v("trick", '''"And you still owe me the trick." {n}Her mouth curls.{/n}''',
      c("Continue", "trick_given", requires=(LESSON,)),
      c("Continue", "trick_kept", requires=(TRICK_KEPT,))),
    v("trick_given", '''"I tried your lesson on a footstool. It stood up and ran down the stairs, which I am told is progress. I had it caught and brought back. It is a footstool again. I am learning."''',
      c("Continue", "ask")),
    v("trick_kept", '''"You kept your little secret. I have been practising on the furniture I have left. None of it has stood up yet. When it does, sweetheart, I will come and show you, and you will not enjoy it."''',
      c("Continue", "ask")),
    v("ask", '''"So. Now we come to it." {n}She sits down on the bare floor as if it were a throne.{/n}
"What do you want from me, Commander? Choose carefully. I remember everything anyone has ever wanted from me, and I have been bored by almost all of it."''',
      c('"You. Not a debt, not a trick. You."', "want"),
      c('"Your company. Your worst opinions. Nothing I\'d have to explain to a priest."', "company"),
      c('[Collect] "You owe me your life. I\'m collecting."', "collect")),
    v("want", '''"Me." {n}She laughs, low and genuinely surprised, and for a moment she looks her age, which is very old.{/n}
"Do you remember what I told you about that game? Somebody always bares their throat. Somebody always decides to bite."
"Very well. Call me. I shall decide each time whether to answer, and I shall answer more often than is good for either of us."''',
      c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_slow", COURTING))),
    v("company", '''"My worst opinions. How greedy." {n}She stretches out on the floor with the shell propped on her knees.{/n}
"I have a great many. Most of them are about people who are still alive, which I intend to correct. Call me when you want to hear them. I may even let you disagree."''',
      c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_company"))),
    v("collect", '''{n}Her face does not change at all.{/n}
"You undid me once, sweetheart. Do not mistake that for owning me. Everything that ever owned me is furniture."
"We are finished, and I am the one who says so."
{n}The glass clouds over. It does not light again.{/n}''',
      c('[Close the shell.]', flags=("vellexia.closed",))),
], requires=("trickster.ever", VISITED), forbids=(KEPT, "vellexia.return_kept"), delay=24)


# --- The glass (the cruel branch): kept, never committed ----------------------------------------------------------------

letter("vellexia.trickster.glass.uncovered", "Everyone looks at her", [
    nar("start", '''{n}The mirror hangs in your quarters, because nowhere else in Drezen will have it. The servants dust it with their eyes shut. On the eve of the march it is the last thing you see before you blow out the lamp.{/n}
{n}You lift the cloth anyway.{/n}''',
      c("Continue", "speaks")),
    v("speaks", '''"There you are." {n}The eyes in the haze are exactly where they were the day you left her there, and they have not blinked since.{/n}
"You look tired. You look frightened. You look at me every night before you sleep, did you know that? Everyone looks at me. You saw to it."
"I have counted every one of your breaths since the Storyteller's shop, sweetheart. I will count the last one."''',
      c('[Cover the glass.]', "covered")),
    nar("covered", '''{n}The cloth goes back over the glass. Under it, the haze does not go still.{/n}''',
      c('"Goodnight, Lady Vellexia."', flags=("vellexia.farewell_kept",))),
], requires=("trickster.ever", KEPT), forbids=("vellexia.farewell_kept",), delay=24)


# --- After the commit: less glass between us (the intimate beat, Directive 12) -----------------------------------------

letter("vellexia.trickster.after.night", "Less glass", [
    nar("start", '''{n}The night before the march. The wind off the Worldwound rattles the shutters of your quarters, and when you turn from the lamp she is already inside, standing by your bed in a dress the colour of a fresh bruise.{/n}''',
      c("Continue", "hands", requires=(DIMINISHED,)),
      c("Continue", "arrived", forbids=(DIMINISHED,))),
    v("arrived", '''"You said the next part might be difficult to come back from. I dislike waiting to find out whether I shall be bored by your corpse." {n}She takes the lamp out of your hand and sets it down.{/n}
"So I came through three portals and a rift camp that smells of mules. Less glass between us, I believe I said."''',
      c("Continue", "threshold")),
    v("hands", '''"You said the next part might be difficult to come back from. I dislike waiting to find out whether I shall be bored by your corpse." {n}She holds up her unfinished hands.{/n}
"These still do nothing. So you will have to do the undressing, sweetheart. All of it. I shall watch, and I shall tell you when you are doing it wrong."''',
      c("Continue", "threshold")),
    nar("threshold", '''{n}She is warm the way a banked fire is warm. When she kisses you it is slow and thorough and completely without mercy, and her teeth find the corner of your mouth, sharp enough to make you understand they are not a human woman's.{/n}
{n}The dress goes to the floor in one whisper of silk. She stands in the lamplight in nothing but her skin and lets you look, and watches you look, with the open, greedy pleasure of a collector who has finally been given the piece she wanted. Then she pushes you back onto your own bed, climbs over you with her knees either side of your hips, and settles astride you, and bends down until her hair falls around both your faces like a curtain.{/n}
"Bare your throat, sweetheart," she breathes against it. "Let us see which of us bites."''',
      c("Continue", "morning")),
    nar("morning", '''{n}Morning. The bed is empty and the shutters are open. There is a bruise on your throat the exact shape of her mouth, and a note on your maps of the Worldwound in handwriting that slopes like a laugh.{/n}
{n}"Come back alive. I have not finished with you, and I refuse to be bored by a monument."{/n}''',
      c('[Wind a scarf over the bruise.]', flags=("vellexia.trickster.night_kept",))),
], requires=("trickster.ever", VISITED, "vellexia.committed"), forbids=(KEPT, "vellexia.trickster.night_kept"), delay=12)


# --- Epilogue: the late commit (R2-6) and paragraphs on her registered endings ------------------------------------------

TRICKSTER_PARAGRAPHS = (
    p("The Upper City never learned she had come back. It went on toasting her memory at every feast she was not invited "
      "to, and she sent anonymous corrections to the speeches.", requires=(PRESUMED,), forbids=(KEPT,)),
    p("She furnished the manor again from nothing, slowly, and every chair in it was only ever a chair. Guests found this "
      "the most unsettling thing about the house.", requires=(BARE,)),
    p("Her hands were never finished. She wore gloves in company and took them off only for the Commander, who knew what "
      "the gloves were for.", requires=(DIMINISHED,)),
    p("She told everyone she met that the Commander was the only guest who had ever predicted her. She said it the way "
      "other women describe a scar.", requires=(PREDICTED,)),
    p("She learned the Commander's trick in the end, as she had promised, and never said how. Several footstools in the "
      "Upper City now walk.", requires=(TRICK_KEPT,)),
    p("She never forgot the one dull sentence the Commander said to her, and reminded the Commander of it at intervals, "
      "always in company.", requires=("vellexia.trickster.cost.bored_once",)),
)
MIRROR_PARAGRAPHS = (
    p("The Commander kept the glass covered after the war, in a locked room, and never slept in the next one. The haze "
      "behind the cloth never went still. \"I will be watching you do it,\" she had said, and she was.",
      requires=(KEPT, WATCHED)),
)

SCENES.append(scene("vellexia.trickster.epilogue.commit", "Kept waiting", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Vellexia finished the conversation after the war, in her own time and at her own party. She sent for the Commander the way she sent for everyone, and was kept waiting, which nobody could remember happening to her before. She found this so novel that she did not have the Commander upholstered.{/n}
{n}The terms she named that night were hers. The Commander agreed to them, which she found almost as surprising.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS)],
    requires=(LATE_COMMITTED,), forbids=("vellexia.committed", "vellexia.closed", DECLINED, KEPT, "vellexia.farewell_kept"),
    last=99, Relationship="vellexia"))


# --- Reactions (05 section 3.1: exactly the Storyteller, Finnean and Daeran) -------------------------------------------

REACTIONS = [
    reaction("Storyteller", "vellexia.trickster.reaction.storyteller", ("vellexia.trickster.mirrored.unmirror",),
             '''"I have read a great many mirrors, Commander. That is the first one that read me back."''',
             answer_list=ST_HUB, forbids=(ST_DEAD,), chapter=5, last=5, delay=24,
             entry='"About the mirror..."'),
    reaction("Storyteller", "vellexia.trickster.reaction.storyteller_likeness", ("vellexia.trickster.sword.likeness",),
             '''"A portrait that was never anyone, until you. I will not ask what it cost her. I suspect she will tell you."''',
             answer_list=ST_HUB, forbids=(ST_DEAD,), chapter=5, last=5, delay=24,
             entry='"About the portrait..."'),
    reaction("Storyteller", "vellexia.trickster.reaction.storyteller_invitation", (ENTRY,),
             '''"You told a story about a woman before she had lived it, and she came to see how it ends. Be careful, Commander. That is how I got into this trade."''',
             answer_list=ST_HUB, forbids=(ST_DEAD,), chapter=5, last=5, delay=24,
             entry='"About Lady Vellexia..."'),
    reaction("Finnean", "vellexia.trickster.reaction.finnean_freed", (UNMIRRORED, "finnean.objected"),
             '''"You turned her back? Huh. Good. She's awful, she'd make a hat out of me, but nobody should be stuck as a thing. Trust me."''',
             answer_list=FINNEAN_HUB, chapter=5, last=5, delay=24, entry='"About Vellexia..."'),
    reaction("Finnean", "vellexia.trickster.reaction.finnean_kept", (KEPT, "finnean.objected"),
             '''"She's still in there, isn't she? I can hear her. Every night. I know what that's like, Commander. Please."''',
             answer_list=FINNEAN_HUB, chapter=5, last=5, delay=24, entry='"About Vellexia..."'),
    reaction("Daeran", "vellexia.trickster.reaction.daeran", (UNMIRRORED,),
             '''"You made the most tasteful woman in the Abyss into a dressing mirror, and then you made her back? Without me? I'd have paid for a seat. I'd have paid for the mirror."''',
             answer_list=DAERAN_HUB, forbids=DAERAN_GONE, chapter=5, last=5, delay=24, entry='"About Lady Vellexia..."'),
    reaction("Daeran", "vellexia.trickster.reaction.daeran_likeness", (DIMINISHED,),
             '''"She came out of a painting with unfinished hands, and the first thing she did was ask for a better painter. My dear, that is not a demon. That is an aristocrat."''',
             answer_list=DAERAN_HUB, forbids=DAERAN_GONE, chapter=5, last=5, delay=24, entry='"About Lady Vellexia..."'),
    reaction("Daeran", "vellexia.trickster.reaction.daeran_invitation", (ENTRY,),
             '''"An invitation from Lady Vellexia? People have died for less. Then they were upholstered."''',
             answer_list=DAERAN_HUB, forbids=DAERAN_GONE, chapter=5, last=5, delay=24, entry='"About Lady Vellexia..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route ----------------------------------------------------------------------------------------------

HANDS_NODE = nar("hands", '''{n}You look a third time. The room has changed again, and the dress, and the expression. The hands have not. In every version they are the same: two pale shapes in underpaint, the one part of her the artist never reached.{/n}
{n}Vellexia follows your eyes and laughs, delighted to have been insulted so precisely.{/n}
"You would leave a woman unfinished? How presumptuous. How very Golarian." {n}She hands you a stub of chalk from the table.{/n} "Mark it, then, so you will know it again. I shall hold you to 'one day'. I have a long memory and nothing but time."''',
    c('"It may be showing what the person looking expects to see."', "hands_expectation"),
    c('"Then make a wager with me. Let us find something it cannot flatter."', "hands_wager"))
# The mark is recorded on the scene's terminal answers (copies of the registered expectation/wager pages), never mid-scene.
HANDS_CHOICE = c('[Look at the painted hands] "It changes everything but the hands. Leave them bare. I\'ll finish them one day."',
                 "hands", mythic="Trickster", requires=("trickster",))
ORDINARY_ENDINGS = ("lovers", "friends", "slow", "interrupted", "closed", "ascent", "sacrifice", "changed")


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Vellexia Trickster integration missing scene: " + id)
    return by_id[id]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _forbid(scene_, *flags):
    scene_["Forbids"] = [*scene_["Forbids"], *[f for f in flags if f not in scene_["Forbids"]]]


def _paragraphs(scene_, paragraphs):
    for node in scene_["Nodes"]:
        if all(ch.get("Next") is None for ch in node["Choices"]):
            node.setdefault("Paragraphs", []).extend(dict(x) for x in paragraphs)


def integrate(payload):
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered. The primer choice
    is appended; the two registered evenings after a return drop only requirements their predecessor already implies."""
    rel = payload["Relationships"]["vellexia"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(x) for k, x in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Vellexia turned into a mirror or struck down may be told back into "
                        "herself, at a price she names; and one never met may hear that the Commander predicted her.")
    payload.setdefault("Presences", {}).update({k: dict(x) for k, x in PRESENCES.items()})
    # ER-1: the final_fight override is a Derived composite (spared OR returned); override values are not scene reads,
    # so trickster_world would not bind it on demand.
    payload.setdefault("Derived", {})["vellexia.fight_survived"] = [["vellexia.spared"], [RETURNED]]
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    # R2-2 primer: the unpainted hands, marked before any fight, on her own gallery interlude.
    likeness = _scene(by_id, "vellexia.unfinished_likeness")
    _node(likeness, "picture_changed")["Choices"].append(HANDS_CHOICE)
    likeness["Nodes"].append(HANDS_NODE)
    for registered in ("expectation", "wager"):
        page = copy.deepcopy(_node(likeness, registered))
        page["Id"] = "hands_" + registered
        for choice in page["Choices"]:
            if choice.get("Next") is None and not choice.get("Abort"):
                choice["Set"] = [*choice["Set"], MARKED]
        likeness["Nodes"].append(page)

    # The evenings after a return: each needs only its predecessor beat (the old path's native keys are implied by it).
    for id, previous in (("vellexia.two_unremarkable_pleasures", "vellexia.return_kept"),
                         ("vellexia.the_cover_before_the_battle", "vellexia.private_kept")):
        s = _scene(by_id, id)
        s["Requires"] = [previous]
        s["ForbidOverrides"] = dict(FO)
    _scene(by_id, "vellexia.the_voice_after_the_abyss")["ForbidOverrides"] = dict(FO)

    # Endings: grief only while she stays dead; the mirror only while she stays glass (G6).
    _forbid(_scene(by_id, "vellexia.ending_dead"), RETURNED)
    mirror = _scene(by_id, "vellexia.ending_mirror")
    _forbid(mirror, UNMIRRORED)
    _paragraphs(mirror, MIRROR_PARAGRAPHS)
    _forbid(_scene(by_id, "vellexia.ending_hostility"), "vellexia.spared", RETURNED)
    for name in ORDINARY_ENDINGS:
        s = _scene(by_id, "vellexia.ending_" + name)
        s["ForbidOverrides"] = dict(FO)
        _forbid(s, KEPT)
        _paragraphs(s, TRICKSTER_PARAGRAPHS)
    _forbid(_scene(by_id, "vellexia.ending_interrupted"), LATE_COMMITTED)
