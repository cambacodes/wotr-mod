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

Polish batch 9 (no mythic-power solutions). The mirror is the native Trickster prank (her own spell turned on her), but
the Trickster's sparks no longer undo it. Mirror: every piece of furniture her spell ever made is still furniture though
she has cast nothing since she became glass, so she is still holding the working closed herself, and letting go of one
lets go of all (Cue_0075: undoing her work leaves "bare walls"). She chooses a mirror in a full house over a woman in an
empty one. The Commander buys the house out from under her through Orrel Vask (Finances), so that holding on keeps
nothing but her own prison; she lets go, and pays with the whole collection (cost.bare_walls). Likeness: the portrait's
older receptive charm (vellexia_opening: the silver wire, the pale stone, the three notches) holds what stayed of her.
The Commander has Vask fetch the artist who sold it to her and pays his real fee, a one-night sitting: he paints the
part of the Commander nobody has seen and keeps it to sell (cost.sat_for_painter). He opens the charm to the first
notch, "a portrait that contradicts its subject", and never paints the hands (cost.diminished). Both are authored and
labelled so; no Trickster ability does either step.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"
UNIT = "a32a07903e428d34cb0e98a804d40569"          # Vellexia_Default (no dialog component; the presence copy)
FYE = "0f12118177d102f428a3b30b15b132eb"           # Fye_Bartender (no longer her anchor: Seelah and Camellia stand there)
STORYTELLER = "da4c28dd01413694f82b08b728a8c6e5"   # the Storyteller's unit (the one in DrezenCapital_Default), her presence anchor
ST_HUB = "2f5b7e0b76d3c5a42a431e1e33a8db09"        # NPC_Common/StoryTeller_MainDialogue/AnswersList_0004
ST_RETURN = "34a0d078b4ac51547a8f5e0e1c8e1e2c"     # StoryTeller_MainDialogue/Cue_0880 "The Storyteller nods, saying nothing."
QM_HUB = "3c58e83a970a0f643a88e15f2323c805"        # NPC_Common/Vendor_Quartermaster/AnswersList_0003 (Wilcer Garms)
FINNEAN_HUB = "615ef80243cfc184ba42286395880b0e"   # CompanionDialogues/Finnean/AnswersList_0003
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"    # CompanionDialogues/Daeran/AnswersList_0003

MIRROR = "vellexia.mirrored"
FREED = "vellexia.slaves_freed"                     # native: she freed her guests at the Commander's asking (Cue_0095)
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
SAT = "vellexia.trickster.cost.sat_for_painter"     # the painter's fee: a likeness of the Commander, his to keep and sell
LESSON = "vellexia.trickster.lesson_given"
VISITED = "vellexia.trickster.visited"
COURTING = "vellexia.trickster.courting"
LATE_COMMITTED = "vellexia.trickster.late_committed"
PROVOKED = "vellexia.trickster.provoked"          # Q11: greeted, living, no continuation; Vask carried her an insult
UNPAID = "vellexia.trickster.unpaid"              # Q11 r5: shell and prediction in hand, native affair abandoned; she bills it
INVITED = "vellexia.invited"                        # Q11: the Commander asked her to Drezen (two_unremarkable_pleasures / the cover)
NIGHT_KEPT = "vellexia.trickster.night_kept"
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
    # A spawned copy of her Upper City unit (CutsceneNeutrals, no dialog) beside the Storyteller, whose shelves already
    # hold her story (her Trickster beats run on his hub); Dialog "hub" makes it talkable. If the Storyteller is dead or
    # gone the anchor fails and vellexia.presence.failed opens the quarters twin.
    "vellexia.presence": dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=STORYTELLER, Side="right", Distance=2.0),
                              Requires=["trickster.ever", "vellexia.trickster.in_person"],
                              Forbids=["vellexia.closed", KEPT, VISITED], MinChapter=5, MaxChapter=5, AnswerLists=[],
                              Dialog="hub",
                              Greeting="{n}Vellexia is reading the spines on the Storyteller's shelves as if she were pricing them. Judging "
                                       "by the old elf's face, she is.{/n}"),
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
    nar("start", '''{n}At the Nexus, word arrives from the Upper City. Two of your people have come back from the Upper City with her dust sheet folded over one arm, as if it were evidence.{/n}
{n}The mirror is still standing in her salon. The looters who went in after her guests fled came out again quickly, and would not say why.{/n}''',
      c("Continue", "finnean", requires=("finnean.objected",)),
      c("Continue", "crate", forbids=("finnean.objected",))),
    nar("finnean", '''{n}Finnean has not said a word since the salon. Now, from the scabbard, very quietly:{/n}
"She's awake in there, Commander. You can tell by the way it doesn't reflect anything. I know what that's like. I'm just saying."''',
      c("Continue", "crate")),
    nar("crate", '''"It's heavy, Commander," {n}says the quartermaster who went back for it.{/n} "Heavy as a wardrobe, and warm, like somebody's been leaning on it. The haze moves when you talk near it. Do we crate it for Drezen, or leave it for the looters?"''',
      c('[Have the mirror crated for Drezen] "I wasn\'t entertained either. She\'s my compensation."', "crated"),
      c('[Throw a sheet over the glass and leave it] "Goodnight, Lady Vellexia."', "sheet")),
    nar("crated", '''{n}They crate it face to the planks, on your orders, with straw packed against the glass. By morning the straw is warm right through. When the crate is lifted, a footstool underneath it scrapes across the floor. The porters strap it beside the mirror: it came from her salon, and none of them will sit on it.{/n}
{n}Just before they nail the lid down, the haulers hear it: a single tap from inside, like a fingernail on glass, testing whether anyone is listening.{/n}''',
      c('"Mind the corners."', flags=(PRIMED, STARTED))),
    nar("sheet", '''{n}Your people go back and throw the sheet over the glass. Under it, the haze goes still.{/n}
{n}A mirror stands in an empty salon in Alushinyrra, and the looters leave it alone. Whoever buys the house will get a mirror nobody likes to look into.{/n}''',
      c('"Leave her there."', flags=(DECLINED,))),
], requires=("trickster.ever", MIRROR, DEAD), forbids=(PRIMED, DECLINED, RETURNED), delay=0, chapters=(4,), area=NEXUS,
   TricksterDevice=True, TricksterState=MIRROR)

stores("vellexia.trickster.mirrored.fetch", "A mirror nobody will loot", '"Garms, what is that bottle doing on your counter?"', [
    nar("start", '''{n}"Sample," Wilcer Garms says, pushing a bottle of Alushinyrran red and a folded note across the counter. "From a cambion named Orrel Vask, down at the rift camp. He moves furniture between the Upper City and anyone who pays. The note's for you."{/n}
{n}Vask found the mirror in Lady Vellexia's empty salon. The looters would not touch it: it watched them. His porters have since crated it at the rift camp, where it has waited a week for a buyer. He names a price, then a surcharge "for the eyes".{/n}''',
      c('[Pay the haulers double to bring it out] "Double, if it arrives uncracked. It\'s a lady."', "paid",
        crusade=("Finances", -200)),
      c('[Leave the crate with Vask] "Somebody else can look at her."', "left")),
    nar("paid", '''{n}Vask's crate comes up from the rift camp the next morning, packed in straw that is warm to the touch. He will not unload it himself. His porters set it down in the corner of your stores and back away from it as if it had spoken.{/n}
{n}Perhaps it had. None of them will say. A footstool from her salon is strapped beside the frame; Vask would not keep it either.{/n}''',
      c('"Put it in the stores. I\'ll deal with her."', flags=(PRIMED, LATE, STARTED))),
    nar("left", '''{n}You send Vask a single line: no. He sends back a single line of his own, which is his invoice for the letter.{/n}
{n}The mirror remains in his crate at the rift camp. The straw pressed against the glass is still warm.{/n}''',
      c('"Pay the man for his ink."', flags=(DECLINED,))),
], ("trickster.ever", MIRROR, DEAD), (PRIMED, DECLINED, RETURNED), 0,
   TricksterDevice=True, TricksterState=MIRROR)

NICE_FLAGS = (RETURNED, UNMIRRORED, BARE, PRESUMED, KNOWN, STARTED, "vellexia.trickster.guests_released")
CRUEL_FLAGS = (RETURNED, KEPT, WATCHED, PRESUMED, KNOWN, STARTED)
NICE_JOKE = '[Play a nice trick on Vellexia] "I bought your house, Lady Vellexia. Every chair in it. Let go."'
NICE_JOKE_FREED = '[Play a nice trick on Vellexia] "I bought your house back, Lady Vellexia. Walls and roof. Come out and sign for it."'
CRUEL_JOKE = '[Play a cruel trick on Vellexia] "Stay a mirror. You\'ll never be bored. Everyone looks at you."'


def unmirror_nodes():
    """The shared close of both unmirrorings: the house bought out from under her so that she lets go, or the glass kept."""
    return [
        glass("glass", '''{n}A face forms in the haze, pale and furious and very interested.{/n}
"Oh, do go on. Tell {mf|him|her} the part where I was magnificent."''',
              c(NICE_JOKE, "nice", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -300), forbids=(FAILED, FREED)),
              c(CRUEL_JOKE, "cruel", mythic="Trickster", alignment=("Evil", 1), forbids=(FAILED,)),
              c('[Show the glass the bill of sale] "I bought your house, Lady Vellexia. Every chair in it. Let go."', "no_sparks",
                alignment=("Chaotic", 1), crusade=("Finances", -300), requires=(FAILED,), forbids=(FREED,)),
              c('[Leave her in the glass] "Stay a mirror. You\'ll never be bored. Everyone looks at you."', "no_sparks_cruel",
                alignment=("Evil", 1), requires=(FAILED,)),
              c('[Cover the mirror again] "Not yet."', abort=True),
              c(NICE_JOKE_FREED, "nice_freed", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -300),
                requires=(FREED,), forbids=(FAILED,)),
              c('[Show the glass the deed] "I bought your house back, Lady Vellexia. Walls and roof. Come out and sign for it."',
                "nice_freed", alignment=("Chaotic", 1), crusade=("Finances", -300), requires=(FAILED, FREED))),
        nar("no_sparks", '''{n}Whatever the Trickster's road once put in your hands is gone. You did not buy the house with it.{/n}''', c("Continue", "nice")),
        nar("no_sparks_cruel", '''{n}Whatever the Trickster's road once put in your hands is gone. You do not need it. You only have to walk away.{/n}''',
            c("Continue", "cruel")),
        nar("nice", '''{n}You hold the paper up to the haze so that she can read it. Orrel Vask's hand, Orrel Vask's seal, and under them an inventory eleven pages long: the contents of one salon in the Upper City, lately the property of a lady presumed dead, knocked down at the looters' auction to the crusade's agent for rather more than the looters expected and rather less than the frame of this mirror is worth. Every chair. Every lamp. Every footstool that used to be a juggler.{/n}
{n}You show her the inventory: every chair still holds a victim, although she has cast nothing since the prank. You have seen the shared binding loosen. Releasing it will free her and the collection together. The paper makes the rest plain. The house and its collection belong to you. She can stay shut in your crate, guarding furniture she no longer owns, or let go.{/n}
{n}The haze goes very still. For a while nothing happens at all, and you begin to wonder whether you have read her wrong. Then, from inside the glass, very quietly and very precisely, she says a word you do not catch, and then another: her spell, the last word first, the way she would say it to a juggler she had finished being bored by. The haze curdles into a shoulder, a knee, a fistful of blonde hair, and then an extremely angry succubus is sitting on the floor in a heap of mahogany splinters.{/n}
{n}The footstool beside the frame becomes a trembling figure and scrambles for the door.{/n}
{n}Far away in the Upper City, in a salon with nobody in it, a great many chairs stand up.{/n}''',
            c("Continue", "undone")),
        glass("undone", '''"How thrilling. You bought me out of my own house. Nobody has ever bought me."
{n}She gets up without taking the hand nobody offered her, and shakes a splinter out of her sleeve.{/n}
"You will show me how you put me in there, and then you will do it again, slowly, so I can learn it. And then, sweetheart, we will discuss what you owe me for my furniture. You paid a looter for it, and I let it go, and I heard every chair in my house walk out of the door. Every one. That was mine to spend, and you made me spend it."''',
          c('"Welcome back, Lady Vellexia."', flags=NICE_FLAGS)),
        nar("nice_freed", '''{n}You hold the paper up to the haze so that she can read it. Orrel Vask's hand, Orrel Vask's seal: one manor in the Upper City, lately the property of a lady presumed dead, stripped to the plaster, knocked down at the looters' auction to the crusade's agent over the bid of a Fleshmarket factor who wanted it for a slave pen. Walls, roof, stairs. Nothing inside them.{/n}
{n}The deed gives her back walls, roof and stairs as soon as she comes out and signs. Otherwise, the Fleshmarket factor gets the manor on the first of next month, while she watches from your stores. She has already released her guests; this time only she remains to be freed.{/n}
{n}The haze goes very still. For a while nothing happens at all. Then, from inside the glass, very quietly and very precisely, she says her own spell, the last word first. The haze curdles into a shoulder, a knee, a fistful of blonde hair, and then an extremely angry succubus is sitting on the floor in a heap of mahogany splinters, holding out one hand for the pen.{/n}''',
            c("Continue", "undone_freed")),
        glass("undone_freed", '''"A house. You bought me an empty house, and I came out of a mirror for it, like a cat for a saucer." {n}She signs without reading, which you suspect she has never done in her life, and shakes a splinter out of her sleeve.{/n}
"You will show me how you put me in there, and then you will do it again, slowly, so I can learn it. And then, sweetheart, we will discuss what I owe you for my walls. I dislike owing. I shall make you regret being owed."''',
          c('"Welcome back, Lady Vellexia."', flags=NICE_FLAGS)),
        nar("cruel", '''{n}The haze thins. For a moment you see only your own reflection, looking very pleased with itself.{/n}
{n}Behind it, two enormous eyes are wide awake.{/n}''', c("Continue", "watched")),
        glass("watched", '''"You will regret this for a very long time, Golarian. And I will be watching you do it."''',
              c('"Hang her somewhere with a good view."', flags=CRUEL_FLAGS)),
    ]


storyteller("vellexia.trickster.mirrored.unmirror", "The joke told backwards",
    '[Have the crated mirror brought in] "This was a succubus, once. Tell me its story."', [
    teller("start", '''{n}The old elf has the porters stand the crate against his shelves. The porters unstrap the footstool and set it beside the opened crate. He lifts the sheet himself and looks into the haze until the lamp beside it starts to gutter.{/n}
"Mahogany that remembers being skin. She was bored, Commander. Then she was surprised. Then she was this." {n}He lets the sheet fall back halfway.{/n}''',
           c("Continue", "reading", forbids=(FREED,)),
           c("Continue", "reading_freed", requires=(FREED,))),
    glass("reading", '''{n}The footstool's carved feet scrape with the tightening haze. Vellexia speaks a clipped word; the wood softens into a heel while a finger presses out of the glass. She stops. Both harden again.{/n}
"One binding. I gathered the lesser spells into it centuries ago. Your joke caught me in the same knot. I can undo it, sweetheart. Then every piece of my collection walks out with me. I have no intention of paying that price for an empty house."''',
           c("Continue", "glass")),
    teller("reading_freed", '''"I read the story forwards, and there is an odd page in it. She let her guests go once already, at your asking; every chair in that house walked out of the door before you ever played your joke on her. So she knows how to untie her own work, and this is her own work, whoever said it aloud. She has not untied it."
"I think I know why. The house she would walk back into has been stripped to the plaster by looters, and the Upper City has already held her memorial feast. A demon of the Upper City with nothing is not a lady, Commander. She is a meal. A mirror, at least, is worth something. That is her story. I cannot change a story. I only notice where it could be bought."''',
           c("Continue", "glass")),
    *unmirror_nodes(),
], requires=("trickster.ever", PRIMED, MIRROR, DEAD), forbids=(RETURNED, DECLINED, ST_DEAD), delay=24,
   TricksterDevice=True, TricksterState=MIRROR)

# The Storyteller is dead: the crate has stood in the quartermaster's stores since it arrived. Fye leaves the capital
# when the tavern is lost (Fye_Bartender_NotInCapital 60d1237d), so the stores host this twin, not his bar.
stores("vellexia.trickster.mirrored.unmirror_stores", "Behind the lamp oil",
    '[Ask about the crate in the corner] "That mirror. Take the straw off it."', [
    nar("start", '''"Your glass, Commander." {n}Wilcer Garms has had the crate stood in the far corner of the stores, behind the lamp oil, as far from the door as it will go.{/n} "It hums when the stores go quiet. The boys won't count stock near it after dark. I'd like it gone, or I'd like it paid for."
{n}Garms pulls the footstool from the crate and leaves it beside the mirror. There is nobody left in Drezen who reads the stories in things, so you will have to read this one yourself.{/n}''',
        c("Continue", "reading", forbids=(FREED,)),
        c("Continue", "reading_freed", requires=(FREED,))),
    glass("reading", '''{n}The footstool's carved feet scrape with the tightening haze. Vellexia speaks a clipped word; the wood softens into a heel while a finger presses out of the glass. She stops. Both harden again.{/n}
"One binding. I gathered the lesser spells into it centuries ago. Your joke caught me in the same knot. I can undo it, sweetheart. Then every piece of my collection walks out with me. I have no intention of paying that price for an empty house."''',
        c("Continue", "glass")),
    nar("reading_freed", '''{n}She let her guests go once already, at your asking, before you ever played your joke on her; she knows how to untie her own work, and this is her own work, whoever said it aloud. She has not untied it. The house she would walk back into has been stripped to the plaster, and the Upper City has held her memorial feast. A demon of the Upper City with nothing is not a lady. She is a meal. A mirror, at least, is worth something.{/n}''',
        c("Continue", "glass")),
    *unmirror_nodes(),
], requires=("trickster.ever", PRIMED, MIRROR, DEAD, ST_DEAD), forbids=(RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState=MIRROR)


# --- State killed_by_sword: the unfinished likeness (F08) ------------------------------------------------------------

letter("vellexia.trickster.sword.portrait", "The one with no hands", [
    nar("start", '''{n}At the Nexus, word arrives that looters are stripping her manor. Your people bring back an inventory, because you asked for one.{/n}''',
      c("Continue", "freed", requires=("vellexia.slaves_freed",), forbids=("vellexia.returned_picture",)),
      c("Continue", "gallery", forbids=("vellexia.slaves_freed", "vellexia.returned_picture")),
      c("Continue", "bought_back", requires=("vellexia.returned_picture",), forbids=("vellexia.slaves_freed",)),
      c("Continue", "freed_bought_back", requires=("vellexia.slaves_freed", "vellexia.returned_picture"))),
    nar("freed_bought_back", '''{n}By the time the inventory was taken, the people she had made into chairs, lamps and footstools were free. The inventory is very short.{/n}
{n}One item did not walk. It was never anyone. She sent the unfinished portrait back to its artist, the afternoon you told her to; and then, it seems, she bought it back from him at twice his price, frame and stone and all, and hung it in the gallery where you first saw it, and never mentioned it. The hands are still bare underpaint. On the back, your chalk mark.{/n}''',
      c("Continue", "choice")),
    nar("freed", '''{n}By the time the inventory was taken, the people she had made into chairs, lamps and footstools were free. The inventory is very short.{/n}
{n}One item did not walk. It was never anyone. The unfinished portrait still hangs in the gallery where you last saw it, the hands still bare underpaint, and on the back, your chalk mark.{/n}''',
      c("Continue", "choice")),
    nar("gallery", '''{n}The inventory runs to eleven pages of furniture that watches the looters work. Near the bottom, in a clerk's cramped hand: one portrait, unfinished, hands unpainted, chalk mark on reverse. Gallery.{/n}''',
      c("Continue", "choice")),
    nar("bought_back", '''{n}Near the bottom of the inventory, in a clerk's cramped hand: one portrait, unfinished, hands unpainted, chalk mark on reverse. Gallery.{/n}
{n}She sent it back to its artist, the afternoon you told her to. Then, it seems, she bought it back from him at twice his price. She never mentioned it.{/n}''',
      c("Continue", "choice")),
    nar("choice", '''"Everything else in that house used to be somebody," {n}says the soldier who brought the list.{/n} "That thing never was. The looters want it for the frame. Take it, or let them burn the canvas?"''',
      c('[Take the portrait you marked] "The only thing in that house that was never anyone. I\'ll have it."', "taken"),
      c('[Put the portrait to the torch] "Burn it. She\'s had enough admirers."', "burned")),
    nar("taken", '''{n}They bring it back frame and all, crated in an oilcloth, because the soldier who tried to cut the canvas out found a pale stone set in silver wire in the back of the frame, warm to the touch, and decided he did not want to be the one who separated them. It is heavier than a portrait should be. By morning the cloth over its face has slipped, and nobody admits to touching it.{/n}''',
      c('"Keep it dry."', flags=(PRIMED, STARTED))),
    nar("burned", '''{n}The canvas goes up quickly. The frame burns slowly. The soldiers who watched it say, afterwards, that the painted face did not change at all, and that they wish it had.{/n}''',
      c('"Enough."', flags=(DECLINED,))),
], requires=("trickster.ever", DEAD, MARKED), forbids=(MIRROR, PRIMED, DECLINED, RETURNED), delay=0, chapters=(4,),
   area=NEXUS, TricksterDevice=True, TricksterState=DEAD)

stores("vellexia.trickster.sword.late_portrait", "A likeness by the yard", '"Is that a sale list under your ledger, Garms?"', [
    nar("start", '''{n}"Orrel Vask's," Wilcer Garms says, and slides it over with a bottle of Alushinyrran red on top to hold it down. "The cambion haulier who strips dead lords' houses in the Upper City. He's selling Lady Vellexia's gallery by the yard through the rift camp. He asked me to make sure you saw it. He was very particular that it should be you."{/n}''',
      c("Continue", "marked", requires=(MARKED,)),
      c("Continue", "unmarked", forbids=(MARKED,))),
    nar("marked", '''{n}You tell him which canvas you want. He already knows which one. It is the one with a chalk mark on the back, in your hand, and he has been holding it back from the other buyers to see what you would pay.{/n}''',
      c("Continue", "price")),
    nar("unmarked", '''{n}Most of the list is paintings of her. One entry is not like the others: "Likeness, unfinished. Nobody sat for it. The hands were never painted. The lady kept it facing the wall." Vask has underlined it, and written "cheap" beside it, and then crossed out "cheap".{/n}''',
      c("Continue", "price")),
    nar("price", '''{n}His price for that one portrait is the price of a good warhorse. His postscript says the frame is extra, because there is a stone set in the back of it that his porters will not carry without being paid to, and that he will not separate canvas and frame, "for reasons the lady would understand".{/n}''',
      c('[Pay Orrel Vask to take one portrait out of her gallery, frame and stone and all] "The one with no hands. All of it."', "paid",
        crusade=("Finances", -200)),
      c('[Let the gallery burn with the rest] "She\'s had enough admirers."', "refused")),
    nar("paid", '''{n}The portrait comes up the rift road in its frame, crated in straw, and Vask's porter will not hand it over until you have counted his master's second fee into his palm. The back of the crate is warm where the stone sits. When you uncover it and name Vellexia, the warmth spreads along the wire. A painted finger pushes against the canvas, then subsides. You cover it again before the porters see.{/n}''',
      c('"Keep it dry."', flags=(PRIMED, LATE, STARTED))),
    nar("refused", '''{n}You write back one word. Vask sells the rest of the gallery to a factor from the Fleshmarkets, and the unfinished one goes into a brazier on a wharf.{/n}''',
      c('"Enough."', flags=(DECLINED,))),
], ("trickster", DEAD), (MIRROR, PRIMED, DECLINED, RETURNED), 0,
   TricksterDevice=True, TricksterState=DEAD)

LIKENESS_JOKE = '[Send Orrel Vask for the man who painted it] "Everyone in her house used to be someone. Her turn."'
LIKENESS_FLAGS = (RETURNED, DIMINISHED, PRESUMED, KNOWN, STARTED)


def likeness_nodes():
    return [
        nar("spell", '''{n}Orrel Vask, it turns out, has had the man who made it waiting in the rift camp for a week, meaning to sell him to whoever bought the portrait; he brings him up the hill within the hour, for the price of a second warhorse: a thin man with paint under his nails and a very good coat, the same artist who once sold Lady Vellexia a portrait that would reveal a part of her she had never seen. He looks at the canvas and goes grey.{/n}
{n}"The older work under mine is a receptive charm," he says. "It keeps something of whoever looks into it longest. She kept looking; she complained to me that it never showed her anything new. I had set the last notch to hide what she would dislike." He turns the frame over. The pale stone in its silver wire is warm. "Something of her is still here. My paint has given it her shape. The first notch opens the older charm. What it kept may take that shape, but I cannot promise the shape will hold." He looks at you. "I will not do it for crowns. Crowns I can get from anybody."{/n}
{n}His fee is a sitting. One night, you in his chair from dusk until the lamps gutter, with the older charm open on the easel beside you, so that he can paint the part of you that you have never seen and keep it, and sell it when he likes, to whom he likes. You have heard what he thinks his customers' privacy is worth.{/n}''',
            c('[Accept the sitting] "Paint me. Then open her charm."', "sitting"),
            c('[Postpone] "Keep your brushes dry. I have not agreed to that."', abort=True)),
        glass("wake", '''"...Oh."
{n}She lifts her hands. They are flawless, and nothing comes of them: no spark, no warmth, only paint-deep perfection.{/n}
"He never finished them. You brought me back unfinished. How dare you. How wonderful." {n}She flexes the fingers, watching them do nothing.{/n} "Finish me, sweetheart, or I will find out who can."''',
          c('"Welcome back, Lady Vellexia."', flags=LIKENESS_FLAGS)),
        nar("no_sparks", '''{n}Whatever the Trickster's road once put in your hands is gone, and it would not have helped. What the canvas needs is the man who painted it, and a fee he will take.{/n}''',
            c("Continue", "spell")),
        nar("sitting", '''{n}You take the painter's chair. He opens the older charm beside you and works until the lamps gutter, keeping your canvas turned away from you.{/n}
{n}In the small hours he sets down his brush, turns her frame over, moves the catch to the first notch, and steps back as if from a fire. The canvas takes on the weight of flesh. Paint becomes a throat, a breath, a woman sitting up in the lamplight with her skirts still wet at the hem. He never reached the hands the first time. He does not reach them now.{/n}''',
            c("Continue", "wake", flags=(SAT,))),
    ]


LIKENESS_CHOICES = (
    c(LIKENESS_JOKE, "spell", mythic="Trickster", alignment=("Chaotic", 1), crusade=("Finances", -200), forbids=(FAILED,)),
    c('[Send Orrel Vask for the man who painted it] "Everyone in her house used to be someone. Her turn."', "no_sparks",
      alignment=("Chaotic", 1), crusade=("Finances", -200), requires=(FAILED,)),
)

storyteller("vellexia.trickster.sword.likeness", "The unfinished likeness",
    '[Unwrap the unfinished portrait] "She\'s dead. This isn\'t. Tell me what you see."', [
    teller("start", '''{n}The Storyteller holds the framed portrait at arm's length, then close, then at arm's length again, and runs one finger over the back of the frame where the stone sits in its silver wire.{/n}
"A likeness nobody sat for. The painter reached the eyes and the smile and never the hands. And something in it did not go where the rest of her went."
{n}He sets it down very carefully.{/n} "I read that as a guess, Commander. I would not bet my life on it. You might bet hers."''',
           *LIKENESS_CHOICES,
           c('"She said a crude transformation could leave something behind. Could that have happened here?"', "foresight",
             requires=("vellexia.bungler_explained",)),
           c('[Wrap it up again] "Not yet."', abort=True)),
    teller("foresight", '''"She was speaking of Finnean, Commander. This is a different working."
{n}The old elf touches the silver wire at the back of the frame.{/n}
"Something remains in it. I cannot tell you how much. Find the painter who sold it to her. He worked over this older charm; he may know how to open it."''',
           *LIKENESS_CHOICES,
           c('[Wrap it up again] "Not yet."', abort=True)),
    *likeness_nodes(),
], requires=("trickster.ever", PRIMED, DEAD), forbids=(MIRROR, RETURNED, DECLINED, ST_DEAD), delay=24,
   TricksterDevice=True, TricksterState=DEAD)

stores("vellexia.trickster.sword.likeness_stores", "Paint that watches",
    '[Ask about the portrait against the wall] "That portrait. Turn it round."', [
    nar("start", '''"She's been staring at the boys since she came in, Commander." {n}Wilcer Garms has stood the portrait against the wall of the stores, frame and all, with its face to the bricks; the back of the frame, where a pale stone sits in silver wire, is warm enough to dry socks on, and the boys have stopped doing so.{/n} "The eyes follow you. The hands don't. I'd take it kindly if you did whatever you're going to do with it somewhere else."
{n}There is nobody left in Drezen who reads the stories in things. You will have to trust your own guess.{/n}''',
        *LIKENESS_CHOICES,
        c('[Leave it facing the bricks] "Not yet."', abort=True)),
    *likeness_nodes(),
], requires=("trickster.ever", PRIMED, DEAD, ST_DEAD), forbids=(MIRROR, RETURNED, DECLINED), delay=24,
   TricksterDevice=True, TricksterState=DEAD)


# --- State never_visited: an invitation to a party she has not yet decided to throw (F11) ---------------------------

letter("vellexia.trickster.never_visited.invitation", "A party in your honour", [
    nar("start", '''{n}Officers over Alushinyrran red in Drezen, on a quiet night on the walls. The wine came up through the rifts with a cambion factor named Orrel Vask, who sells the Upper City its gossip on the way back down.{/n}
{n}Somebody asks whether you met the famous Lady Vellexia while you were in the Abyss. The one who collects guests, and keeps the ones who bore her as furniture.{/n}''',
      c('[Boast about the Upper City, and tip the wine-factor to carry it word for word] "Lady Vellexia? Charming. She\'s throwing a party in my honour. She just doesn\'t know it yet."',
        "card", mythic="Trickster", crusade=("Finances", -100)),
      c('[Change the subject] "The Abyss? I don\'t talk about the Abyss."', "silent")),
    nar("card", '''{n}Vask laughs, pockets the coin, and repeats it back to you word for word, twice, so there can be no mistake. Then he sends it down the camp road with the boy who carries his ledgers.{/n}
{n}Lady Vellexia, it seems, keeps a page of her own at the rift camp, to hear whatever is said about her in Drezen. Before the night is out the boy is back, with lilac on his cuffs and a card he will not let anyone else touch. It invites you to a party that its hostess, by her own admission in the postscript, has not yet decided to throw.{/n}
{n}"Tell me who told you I would," the postscript ends. "I should like to have them upholstered."{/n}''',
      c('"Tell her I\'ll come."', flags=(ENTRY, PRIMED, PREDICTED, KNOWN, STARTED))),
    nar("silent", '''{n}The table moves on to the war. Vask sells the rest of his red to the quartermaster, and takes no message back down the rift with him.{/n}''',
      c('"Pour."', flags=(DECLINED,))),
], requires=("trickster", "chapter_later"), forbids=("vellexia.greeted", DEAD, ENTRY, DECLINED), delay=0)


# --- State greeted but never continued: a provocation by the yard (Q11; live Trickster, Chapter 5) ---------------------
# A Vellexia the Commander met in her manor, still alive, whose native affair was left unfinished or finished without the
# shell (no prediction_known), has no other road. Vask carries an insult worth crossing the portals for; she answers in
# person (after.visit, where she gives the shell), never by a letter.

letter("vellexia.trickster.reacquire.provocation", "Bored, by report", [
    nar("start", '''{n}Officers over Alushinyrran red in Drezen, a quiet night on the walls. The wine came up through the rifts with a cambion factor named Orrel Vask, who sells the Upper City its gossip on the way back down and buys it fresh on the way up.{/n}''',
      c("Continue", "unfinished", forbids=("vellexia.native_finished",)),
      c("Continue", "finished", requires=("vellexia.native_finished",))),
    nar("unfinished", '''{n}Somebody asks about the famous Lady Vellexia. You have been in her house; you left it in the middle of her entertainment, with her curiosity unpaid, and the Upper City has noticed. Vask has noticed that it noticed. He is waiting, with the patience of a man who sells messages by the word, to see whether you have one.{/n}''',
      c("Continue", "offer")),
    nar("finished", '''{n}Somebody asks about the famous Lady Vellexia. Your affair with her ended in the Upper City the way her affairs end, and nothing she ever gave you has spoken a word on her behalf since. Vask has heard the end of that story from three different footmen. He is waiting, with the patience of a man who sells messages by the word, to see whether you have one.{/n}''',
      c("Continue", "offer")),
    nar("offer", '''{n}"A message to a lady," Vask says, "costs what the lady will do to the messenger. Choose your words accordingly."{/n}''',
      c('[Tip the wine-factor to carry it word for word] "Tell Lady Vellexia the crusader she found so diverting left her house bored, and has not thought of her since."',
        "sent", mythic="Trickster", crusade=("Finances", -100)),
      c('[Let the Upper City keep its gossip] "Pour."', "silent")),
    nar("sent", '''{n}Vask goes grey under the cambion red, repeats it back to you twice, and asks for his fee in advance. Then he whistles up the boy who carries his ledgers through the rifts, and sends your words down the camp road before his nerve can fail.{/n}
{n}The boy is back before the last bottle is empty, with lilac on his cuffs and one finger splinted. Lady Vellexia, it seems, keeps a page of her own at the rift camp to hear whatever is said about her in Drezen. Her answer is not a card and not a letter. It is a single line the boy has been made to learn by heart: "Tell the crusader I am coming to see what boredom looks like, and that I shall know if it lies to me again."{/n}''',
      c('"Let her come."', flags=(PROVOKED, KNOWN, STARTED))),
    nar("silent", '''{n}The table moves on to the war. Vask sells the rest of his red to the quartermaster, and takes no message back down the rift with him.{/n}''',
      c('"Pour."', flags=(DECLINED,))),
], requires=("trickster", "trickster.ever", "vellexia.greeted"),
    forbids=(DEAD, MIRROR, "vellexia.early_fight", "vellexia.final_fight", "vellexia.native_coercion", KNOWN, PROVOKED, ENTRY,
             DECLINED, RETURNED),
    delay=0, ForbidOverrides={"vellexia.final_fight": "vellexia.fight_survived"})


# Q11 r5: the Commander took her shell and heard the prediction seller's claim, then walked out of her entertainment for
# good (the native dates never finished). Nothing else can open in Chapter 5; the shell she gave carries her bill.
letter("vellexia.trickster.reacquire.unpaid", "An entertainment, unpaid for", [
    nar("start", '''{n}The shell lights on your table in Drezen, for the first time since the Upper City. When you open it, Vellexia is sitting in her salon with an account book on her knee and a pen she is plainly longing to use on someone.{/n}''',
      c("Continue", "bill")),
    v("bill", '''"You left in the middle of my entertainment. Nobody leaves in the middle of my entertainment; the last guest who tried it is a hat-stand in my hall, and he was more entertaining than you, while he lasted." {n}She turns a page.{/n} "I have costed it. The musicians, the wine, the guests I had chosen to bore you with, and my disappointment, which is very expensive. You will pay. The only question is whether you pay here, through a shell, like a coward, or in person, where I can watch you count it out."''',
      c('[Trickster] "In person. Come to Drezen and collect it, if you dare the road."', "come", mythic="Trickster"),
      c('[Close the shell] "Put it on my account."', "refuse")),
    v("come", '''"If I dare the road." {n}Her smile is slow and not at all kind.{/n} "Oh, sweetheart. I shall come, and you will pay me in front of whoever you love best in that miserable city, and you will thank me for the invoice." {n}The glass clouds before you can answer.{/n}''',
      c('"I\'ll be waiting."', flags=(UNPAID, STARTED))),
    v("refuse", '''"On your account." {n}She closes the book.{/n} "Then I shall add the interest myself, in my own time, and you will not enjoy the way I collect it." {n}The glass clouds.{/n}''',
      c('[Let it go dark.]', flags=(DECLINED,))),
], requires=("trickster", "trickster.ever", "vellexia.greeted", "vellexia.seal_agreed", KNOWN),
    forbids=(DEAD, MIRROR, "vellexia.early_fight", "vellexia.final_fight", "vellexia.native_coercion", "vellexia.native_finished",
             "vellexia.case_opened", UNPAID, PROVOKED, ENTRY, DECLINED, RETURNED, VISITED),
    delay=0)


# --- After any return: the test in person (R2-1, R2-3) -----------------------------------------------------------------
# Q11: the staging is the place's own (the Storyteller's shelves, or the Commander's quarters when his anchor failed), and
# the first question of the old first call ("What do you want from me?") is asked here, in person, before she leaves:
# one Trickster delivery fewer on every return branch (the old remote after.voice is never reached after this visit).

PLACES = {
    "shelves": dict(
        watch="the whole doorway watching",
        perch="She turns on the old man's reading stool so that the soldiers in the doorway can see her do it.",
        stage="a blind man's shop",
        surface="the Storyteller's reading table",
        door="the shop door"),
    "quarters": dict(
        watch="your sentry listening at the door",
        perch="She swings her feet down off your maps and sits up, so that the sentry outside can hear every word.",
        stage="a crusader's bedroom",
        surface="your maps of the Worldwound",
        door="your door"),
}


def shell_text(where, held, voice):
    pl = PLACES[where]
    if held:
        first = '''{n}She taps the silver rim of the shell at your belt, the one she gave you in her manor, the day she decided you might be worth an afternoon.{/n}
"You kept it. Good. Keep it open.'''
    else:
        first = '''{n}She sets a silver-rimmed shell on %s, the size of her palm, with a cover of cloudy glass. It is warm from her hand.{/n}
"An echo shell. Open it and it asks for me.''' % pl["surface"]
    return first + ''' I may answer. I may be busy. I am going home, sweetheart. %s" {n}She stops at %s, and turns.{/n}''' % (voice, pl["door"])


DEAD_VOICE = "My house is a ruin and I am told I am dead, and I have decided to find both restful, for a season."
ENTRY_VOICE = "I came a very long way to be predicted, and I intend to spend the whole journey back deciding whether I enjoyed it."
PROVOKED_VOICE = "I came a very long way to be insulted, and I intend to spend the whole journey back deciding whether I enjoyed it."
UNPAID_VOICE = "I came a very long way to collect on an evening you walked out of, and I shall keep collecting it for as long as it amuses me."


# Authored responses to the five existing acquisitions; no new price or gate.
LESSON_REPLIES = {
    "diminished": (
        '\"The first notch. Show me that catch again.\" {n}She follows your fingers, then flexes her own. Nothing answers.{/n} \"The charm did the work. These pretty things still will not cast. I shall have the painter show me what else he hid before I decide which of his hands to keep.\"',
        '\"Keep it, then. The charm is still in its frame, and the painter still has a tongue. One of them will explain what you will not.\"'),
    "entry": (
        '\"So you bought a boast and had it carried to my own spy.\" {n}She laughs.{/n} \"I shall tell Vask you have promised me another visit. Let us see how quickly my prophecy brings you crawling back.\"',
        '\"Vask heard your prophecy before I did. I shall ask him who supplied it. If he lies badly, I shall keep him somewhere he can hear every rumour and repeat none of them.\"'),
    "provoked": (
        '\"You counted on my vanity. How vulgar. How accurate.\" {n}Her smile sharpens.{/n} \"Next time the Upper City hears that I have forgotten you, see how long you can stay away.\"',
        '\"Keep it. I shall send Vask back with something about you. Something your officers will enjoy repeating. Then I shall watch which of us comes running.\"'),
    "unpaid": (
        '\"You left an evening unfinished so I would follow.\" {n}She closes the book on one finger.{/n} \"Very well. I shall leave you waiting halfway through something you want. Then you may show me how patiently you bear your own little trick.\"',
        '\"Keep it. I shall ask every guest who saw you leave what you looked at before the door. Someone noticed what you wanted. I shall enjoy offering it to you, then getting bored halfway through.\"'),
}


def visit_nodes(place_text, where):
    pl = PLACES[where]
    nodes = [
        nar("start", place_text,
            c("Continue", "unmirrored", requires=(UNMIRRORED,)),
            c("Continue", "diminished", requires=(DIMINISHED,), forbids=(UNMIRRORED,)),
            c("Continue", "entry", requires=(ENTRY,), forbids=(UNMIRRORED, DIMINISHED)),
            c("Continue", "provoked", requires=(PROVOKED,), forbids=(UNMIRRORED, DIMINISHED, ENTRY)),
            c("Continue", "unpaid", requires=(UNPAID,), forbids=(UNMIRRORED, DIMINISHED, ENTRY, PROVOKED))),
        v("unmirrored", '''"Show me. Now, here, with %s." {n}%s{/n} "My collection walked away. The looters took the curtains. I was not invited to either of my memorial feasts. It is costing me a fortune to be dead. If you can make a woman into a thing, and then buy her house out from under her until she walks out of it, you can make %s into a stage for an hour. Everyone in the Upper City thinks I am dead. I would like one person to see me being alive."''' % (pl["watch"], pl["perch"], pl["stage"]),
          c('[Show her how the trick works] "Watch my hands. Not my face. Everyone watches the face."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("diminished", '''"Look at them." {n}She lays her perfect, unfinished hands on %s, palms up, where the lamplight can find every flaw in them. There are none. That is the flaw.{/n}
"They move. They will not cast. I tried another painter. He wept over them, so I had him thrown down the stairs, then carried back up to finish weeping. Nobody in the Upper City can finish me. Do not promise me another painter. Show me what the first one did."''' % pl["surface"],
          c('[Show her how it was done] "Your painter, my face, and a working he swore was secret. I watched him do it. Watch my hands."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("entry", '''"So this is the prophet." {n}She looks you over the way she looks over furniture.{/n} "I came to see who predicted me. Nobody predicts me. It has put me in a very bad mood, and I have come a long way to enjoy it."
"Predict me, sweetheart. What do I do next?"''',
          c('[Tell her how it was done] "A wine-factor, a boast, and a ledger boy who runs faster than gossip. That\'s all a prophecy is."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("provoked", '''"Bored." {n}She says the word as if tasting a wine she means to send back.{/n} "You sent word with a wine-factor that I bore you. The whole Upper City has heard it. I have had to come to your war to find out whether it is true, and I broke your messenger's finger on the way, which you may add to my bill."
{n}She looks you over the way she looks over furniture she has not yet decided to keep.{/n} "Bore me, then. I dare you. Tell me how you got me here."''',
          c('[Tell her how it was done] "A wine-factor and one lie about your vanity. It brought you across three portals."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        v("unpaid", '''"Here I am, and here is the bill." {n}She lays the account book open in front of you, every line in her own hand: the musicians, the wine, the guests chosen to bore you, and at the bottom, underlined twice, her disappointment.{/n} "You walked out of my house in the middle of the evening, and the Upper City laughed for a week. Pay it, or tell me how you dared. One of those I shall enjoy."''',
          c('[Tell her how you dared] "I left because I knew you would come after me. You did."', "gave"),
          c('[Keep the trick] "A trick explained is a trick spent. Guess."', "kept")),
        nar("gave", '''{n}She watches as you explain it, and not your face. When you finish she says nothing at all, which is the most frightening thing you have seen her do.{/n}''',
            c("Continue", "gave_end")),
        v("gave_end", '''"Again. Slower."
{n}You do it again. She mouths it with you, the way a duellist mirrors a lesson, and her eyes do not leave you once.{/n}
"There. Now I own it too. I shall practice. When the next footstool runs down my stairs, I shall have it caught and start again."''',
          c("Continue", "shell_held", requires=("vellexia.seal_agreed",), forbids=(ENTRY, PROVOKED, UNPAID)),
          c("Continue", "shell", forbids=("vellexia.seal_agreed", ENTRY, PROVOKED)),
          c("Continue", "shell_entry_held", requires=("vellexia.seal_agreed", ENTRY)),
          c("Continue", "shell_entry", requires=(ENTRY,), forbids=("vellexia.seal_agreed",)),
          c("Continue", "shell_prov_held", requires=("vellexia.seal_agreed", PROVOKED), forbids=(ENTRY,)),
          c("Continue", "shell_prov", requires=(PROVOKED,), forbids=("vellexia.seal_agreed", ENTRY)),
          c("Continue", "shell_unpaid", requires=(UNPAID,), forbids=(ENTRY, PROVOKED))),
        v("kept", '''"Oh, good." {n}She watches the hands you have hidden, smiling.{/n}
"Keep it, then. I shall practice on what remains of my furniture. I shall take it from you eventually. It will be so much more fun than being given it. Do you know how long it has been since anyone kept anything from me? Neither do I."''',
          c("Continue", "kept_shell_held", requires=("vellexia.seal_agreed",), forbids=(ENTRY, PROVOKED, UNPAID)),
          c("Continue", "kept_shell", forbids=("vellexia.seal_agreed", ENTRY, PROVOKED)),
          c("Continue", "kept_shell_entry_held", requires=("vellexia.seal_agreed", ENTRY)),
          c("Continue", "kept_shell_entry", requires=(ENTRY,), forbids=("vellexia.seal_agreed",)),
          c("Continue", "kept_shell_prov_held", requires=("vellexia.seal_agreed", PROVOKED), forbids=(ENTRY,)),
          c("Continue", "kept_shell_prov", requires=(PROVOKED,), forbids=("vellexia.seal_agreed", ENTRY)),
          c("Continue", "kept_shell_unpaid", requires=(UNPAID,), forbids=(ENTRY, PROVOKED))),
        nar("shell", shell_text(where, False, DEAD_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, LESSON))),
        nar("shell_held", shell_text(where, True, DEAD_VOICE), c('[Let her go.]', "ask", flags=(VISITED, LESSON))),
        nar("kept_shell", shell_text(where, False, DEAD_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("kept_shell_held", shell_text(where, True, DEAD_VOICE), c('[Let her go.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("shell_entry", shell_text(where, False, ENTRY_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, LESSON))),
        nar("shell_entry_held", shell_text(where, True, ENTRY_VOICE), c('[Let her go.]', "ask", flags=(VISITED, LESSON))),
        nar("kept_shell_entry", shell_text(where, False, ENTRY_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("kept_shell_entry_held", shell_text(where, True, ENTRY_VOICE), c('[Let her go.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("shell_prov", shell_text(where, False, PROVOKED_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, LESSON))),
        nar("shell_prov_held", shell_text(where, True, PROVOKED_VOICE), c('[Let her go.]', "ask", flags=(VISITED, LESSON))),
        nar("kept_shell_prov", shell_text(where, False, PROVOKED_VOICE), c('[Take the shell.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("kept_shell_prov_held", shell_text(where, True, PROVOKED_VOICE), c('[Let her go.]', "ask", flags=(VISITED, TRICK_KEPT))),
        nar("shell_unpaid", shell_text(where, True, UNPAID_VOICE), c('[Let her go.]', "ask", flags=(VISITED, LESSON))),
        nar("kept_shell_unpaid", shell_text(where, True, UNPAID_VOICE), c('[Let her go.]', "ask", flags=(VISITED, TRICK_KEPT))),
        v("ask", '''"One more thing, before I go, since you have made me come all this way to ask it in person." {n}She leans in the doorway as if it belonged to her.{/n}
"What do you want from me, Commander? Choose carefully. I remember everything anyone has ever wanted from me, and I have been bored by almost all of it."''',
          c('"You. Not a debt, not a trick. You."', "want"),
          c('"Your company. Your worst opinions. Nothing I\'d have to explain to a priest."', "company"),
          c('[Collect] "You owe me your life. I\'m collecting."', "collect", requires=(RETURNED,)),
          c('"I\'m glad you came to Drezen."', "dull", requires=(PREDICTED,))),
        v("dull", '''"There. Luck." {n}Her face goes smooth and polite, which is worse than anger.{/n} "One. People who bore me get three, and nobody has ever had three. Do not become the first. Now: what do you want from me?"''',
          c('"You. Not a debt, not a trick. You."', "want", flags=("vellexia.trickster.cost.bored_once",)),
          c('"Your company. Your worst opinions."', "company", flags=("vellexia.trickster.cost.bored_once",))),
        v("want", '''"Me." {n}She laughs, low and genuinely surprised, and for a moment she looks her age, which is very old.{/n}
"Then keep looking at me. You have been watching your clever hands all afternoon, and I intend to become a more expensive distraction."
"Very well. Call me. I shall decide each time whether to answer. When your war is over, come to my party. I want you there, sweetheart. I shall choose the room, and you may attempt to keep me waiting."''',
          c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_slow", COURTING))),
        v("company", '''"My worst opinions. How greedy." {n}She pulls her cloak around her, ready for the road.{/n}
"I have a great many. Most of them are about people who are still alive, which I intend to correct. Call me when you want to hear them. I may even let you disagree."''',
          c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_company"))),
        v("collect", '''{n}Her face does not change at all.{/n}
"You undid me once, sweetheart. Do not mistake that for owning me. Everything that ever owned me is furniture."
"We are finished, and I am the one who says so." {n}She does not look back from %s.{/n}''' % pl["door"],
          c('[Let her go.]', flags=("vellexia.closed", "vellexia.parted"))),
    ]
    by = {node["Id"]: node for node in nodes}
    histories = (("unmirrored", UNMIRRORED), ("diminished", DIMINISHED),
                 ("entry", ENTRY), ("provoked", PROVOKED), ("unpaid", UNPAID))
    for index, (history, flag) in enumerate(histories):
        requires = (flag,)
        forbids = tuple(prior for _, prior in histories[:index])
        if index == 0:
            by["gave"]["Choices"][0]["Requires"] = list(requires)
            by["gave"]["Choices"][0]["Forbids"] = list(forbids)
            continue
        given, withheld = LESSON_REPLIES[history]
        nodes.append(glass("gave_" + history, given, *copy.deepcopy(by["gave_end"]["Choices"])))
        nodes.append(glass("kept_" + history, withheld, *copy.deepcopy(by["kept"]["Choices"])))
        by["gave"]["Choices"].append(c("Continue", "gave_" + history, requires=requires, forbids=forbids))
        by[history]["Choices"][1]["Next"] = "kept_" + history
    return nodes



SCENES.append(scene("vellexia.trickster.after.visit", "Among the shelves", "Vellexia", 5,
    '"Lady Vellexia. Drezen suits you better than I expected."', visit_nodes(
        '''{n}She is sitting among the Storyteller's shelves with the war outside as if they were her salon, in a crusader officer's mantle with the badge torn off and the silk lining turned out, a book open face-down on her knee. Every soldier who passes the door is pretending not to look at her. The Storyteller has put a clean cup at her elbow and is standing as far from it as his shelves allow.{/n}''',
        "shelves"),
    requires=("trickster.ever",), forbids=(*OWN, KEPT, VISITED), delay=24, last=5, optional=True, Relationship="vellexia",
    Areas=[DREZEN], Chapters=[5], ContactUnit=UNIT, InteractionHub="vellexia.presence",
    RequiresAnyGroups=[[UNMIRRORED, DIMINISHED, ENTRY, PROVOKED, UNPAID]]))

# The anchor failed (the Storyteller is dead or gone): she comes to the Commander's quarters instead, the same test in
# person. Q11: a physical scene, entered through the quartermaster (the ledger's always-present anchor), not a letter.
stores("vellexia.trickster.after.visit_quarters", "A guest who was not invited", '"Is something wrong, Garms? Your boys look shaken."', visit_nodes(
    '''{n}"There's a lady in your quarters, Commander," Wilcer Garms says, without looking up from his ledger. "The sentry let her in. He can't say why. He's asked to be moved to the north wall."{/n}
{n}The Storyteller's shelves stand empty and under dust sheets, so she has come to your quarters instead. She is sitting in your chair with her feet on your maps of the Worldwound, and she has already read them.{/n}''',
    "quarters"),
    requires=("trickster.ever", "vellexia.presence.failed"), forbids=(KEPT, VISITED, "vellexia.trickster.after.visit"),
    delay=48, RequiresAnyGroups=[[UNMIRRORED, DIMINISHED, ENTRY, PROVOKED, UNPAID]])


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
"I went to another painter. A very good one. He looked at them for an hour and then he wept, and I had him thrown down the stairs, and then I had him carried back up to finish weeping. Nobody in the Upper City can finish me. Finish me."''',
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
"Then keep looking at me. You have been watching your clever hands all afternoon, and I intend to become a more expensive distraction."
"Very well. Call me. I shall decide each time whether to answer. When your war is over, come to my party. I want you there, sweetheart. I shall choose the room, and you may attempt to keep me waiting."''',
      c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_slow", COURTING))),
    v("company", '''"My worst opinions. How greedy." {n}She stretches out on the floor with the shell propped on her knees.{/n}
"I have a great many. Most of them are about people who are still alive, which I intend to correct. Call me when you want to hear them. I may even let you disagree."''',
      c('"I\'ll call."', flags=("vellexia.return_kept", "vellexia.renewed_company"))),
    v("collect", '''{n}Her face does not change at all.{/n}
"You undid me once, sweetheart. Do not mistake that for owning me. Everything that ever owned me is furniture."
"We are finished, and I am the one who says so."
{n}The glass clouds over. It does not light again.{/n}''',
      c('[Close the shell.]', flags=("vellexia.closed", "vellexia.parted"))),
], requires=("trickster.ever", VISITED), forbids=(KEPT, "vellexia.return_kept"), delay=24)

# Authored follow-through: each lesson keeps its original subject at the shell.
LESSON_FOLLOWUPS = {
    "diminished": (
        '\"I have been turning that catch. It answers more readily than my fingers do. The painter had better pray there is something left in it he can use.\"',
        '\"The painter keeps his little secrets too. I shall put him and the charm in the same room and see which gives up first.\"'),
    "entry": (
        '\"Vask is waiting for my next prophecy. I thought I might predict what you would send me. Something expensive, sweetheart.\"',
        '\"Vask goes pale whenever I ask about your prophecy. I am beginning to enjoy asking.\"'),
    "provoked": (
        '\"I have been considering which rumour would bring you running. Tell me what your officers laugh at, sweetheart.\"',
        '\"You will hear my answer from Vask. I want your officers to hear it first.\"'),
    "unpaid": (
        '\"I have chosen the entertainment I shall interrupt. No, I will not tell you which part. You may wait.\"',
        '\"My guests remember you leaving. I shall find out what they remember you wanting, too.\"'),
}

# Keep the legacy mirror callback nodes and append acquisition-specific echoes.
_call_nodes = SCENES[-1]["Nodes"]
_call_by = {node["Id"]: node for node in _call_nodes}
for _index, (_history, _flag) in enumerate((("unmirrored", UNMIRRORED), ("diminished", DIMINISHED),
                                          ("entry", ENTRY), ("provoked", PROVOKED), ("unpaid", UNPAID))):
    _prior = [UNMIRRORED, DIMINISHED, ENTRY, PROVOKED][:_index]
    for _choice, _key, _column in ((0, LESSON, 0), (1, TRICK_KEPT, 1)):
        _base = "trick_given" if _column == 0 else "trick_kept"
        if _index == 0:
            _call_by["trick"]["Choices"][_choice]["Requires"].append(_flag)
            continue
        _target = _base + "_" + _history
        _call_nodes.append(v(_target, LESSON_FOLLOWUPS[_history][_column], c("Continue", "ask")))
        _call_by["trick"]["Choices"].append(c("Continue", _target, requires=(_key, _flag), forbids=tuple(_prior)))



# --- The glass (the cruel branch): kept, never committed ----------------------------------------------------------------

letter("vellexia.trickster.glass.uncovered", "Everyone looks at her", [
    nar("start", '''{n}The mirror hangs in your quarters, because nowhere else in Drezen will have it. The servants dust it with their eyes shut. Each night it is the last thing you see before you blow out the lamp.{/n}
{n}Tonight you lift the cloth.{/n}''',
      c("Continue", "speaks")),
    v("speaks", '''"There you are." {n}The eyes in the haze are exactly where they were the day you left her there, and they have not blinked since.{/n}
"You look tired," {n}she says.{/n} "You look frightened. You look at me every night before you sleep, did you know that? Everyone looks at me. You saw to it."
"I have counted every one of your breaths since you hung me here, sweetheart. I will count the last one."''',
      c('[Cover the glass.]', "covered")),
    nar("covered", '''{n}The cloth goes back over the glass. Under it, the haze does not go still.{/n}''',
      c('"Goodnight, Lady Vellexia."', flags=("vellexia.farewell_kept",))),
], requires=("trickster.ever", KEPT), forbids=("vellexia.farewell_kept",), delay=24)


# --- After the commit: less glass between us (the intimate beat, Directive 12) -----------------------------------------

stores("vellexia.trickster.after.night", "Less glass", '"Anything I should know tonight, Garms?"', [
    nar("start", '''{n}"A lady came up the rift road at dusk with no papers and three portals' worth of dust on her hem," Wilcer Garms says, and does not look up from his ledger. "The sentries let her through. None of them can say why. She asked which door was yours. I told her. I'm not proud of it."{/n}
{n}The wind off the Worldwound rattles the shutters of your quarters. When you turn from the lamp, Vellexia is already inside, standing by your bed in a dress the colour of a fresh bruise.{/n}''',
      c("Continue", "hands", requires=(DIMINISHED,)),
      c("Continue", "arrived", forbids=(DIMINISHED,))),
    v("arrived", '''"I dislike waiting to find out whether I shall be bored by your corpse." {n}She takes the lamp from you and sets it down.{/n}
"Three portals and a rift camp that smells of mules. You had better be worth the journey, sweetheart. I see your war has taken the table. Move those maps. I came at this hour because you would never have chosen it. Less glass between us. I intend to enjoy the difference."''',
      c("Continue", "threshold")),
    v("hands", '''"I dislike waiting to find out whether I shall be bored by your corpse."
{n}She holds up her unfinished hands and flexes them. No spark follows.{/n}
"They move. They will not cast. You will do the undressing, sweetheart. All of it. I shall watch, and tell you when you are doing it wrong."''',
      c("Continue", "threshold")),
    nar("threshold", '''{n}Vellexia catches your lower lip between her teeth, then kisses the small hurt she has made. She watches your face as you unlace her gown. The silk slips down her body and pools at her feet.{/n}
"Slowly, darling. I came all this way to be looked at."
{n}She stands naked in the lamplight while you shed your own clothes. When you reach for her, she draws you down onto the bed. Her hair brushes your bare chest. She bends close enough for you to feel her breath against your throat.{/n}
"Bare it. I want to see whether you still trust me with it."
{n}You tilt your head back. She takes your throat between her teeth, not gently, and sucks until the skin burns and the mark is certain. The sound that comes out of you makes her purr against it. Her clawed hands go down your ribs, nails dragging, and she presses her whole length to you, hot and hungry and without the slightest shame.{/n}
"Mine for the night, darling. The war can have you back at dawn, and not before." {n}She pins your wrist above your head against the pillow with the unhurried certainty of a woman who has never been refused anything she wanted.{/n}''',
      c("Continue", "vellexia.trickster.after.night.explicit.1")),
    nar("morning", '''{n}At dawn she sits on the edge of the bed, watching you discover the bruise on your throat. Your abandoned clothes cover the Worldwound map. She lifts one corner, finds the lip-paint print beneath it, and laughs.{/n}
"Leave it. Your officers can argue over that position next."
{n}She takes her cloak from the chair and bends to kiss the unmarked side of your throat before leaving.{/n}
"Come back alive. I have not finished with you, and I refuse to be bored by a monument."''',
      c('[Wind a scarf over the bruise.]', flags=("vellexia.trickster.night_kept",))),
    # Explicit-slot brief: her possessive first bodily night; external prose only.
    nar("vellexia.trickster.after.night.explicit.1", '{n}Vellexia draws you against her, and the war goes out of your head along with the lamp. There is her mouth, her nails and her low delighted laugh in the dark, and she does not once let you set the pace. Your abandoned clothes lie across the Worldwound map; she leaves them there.{/n}',
        c("Continue", "morning")),
], ("trickster.ever", "vellexia.committed", "vellexia.farewell_lovers"), (KEPT, NIGHT_KEPT), 12,
    # Q11: the peaceful commit reaches the night as well as the recovery; she comes because she was asked to Drezen
    # (INVITED) or because she has already come once in person (VISITED, whose commit at the cover also invites her).
    RequiresAnyGroups=[[VISITED, INVITED]])


# --- Epilogue: the late commit (R2-6) and paragraphs on her registered endings ------------------------------------------

# Q11 r4: a paragraph about the life they go on sharing never plays on an ended correspondence, a friendship, a dead or
# changed Commander (the native "sacrifice" ending is its own page; a Commander who came back is not "sacrifice" there).
CONTINUING_NOT = ("vellexia.closed", "vellexia.parted", "vellexia.farewell_friends", "vellexia.farewell_slow", "sacrifice",
                  "inhuman", "ascended")
TRICKSTER_PARAGRAPHS = (
    p('{n}For a while the Upper City toasted her memory. She sent anonymous corrections to the speeches and enjoyed hearing which guests had mourned her badly.{/n}', requires=(PRESUMED,), forbids=(KEPT,)),
    p("{n}She furnished the manor again from nothing, slowly. For a season every chair was only a chair. Guests found this "
      "the most unsettling thing about the house. Then a new footstool appeared, and nobody asked where she had found it.{/n}", requires=(BARE,)),
    p('{n}Her hands were never finished. One painter tried and wept over them; she had him thrown down the stairs. No other painter accepted the commission.{/n}', requires=(DIMINISHED,)),
    p('{n}She wore gloves in company. In private, she made the Commander take them off and look at what remained unfinished.{/n}',
      requires=(DIMINISHED,), forbids=CONTINUING_NOT, any_groups=[["vellexia.farewell_lovers", LATE_COMMITTED]]),
    p("{n}She told everyone she met that the Commander was the only guest who had ever predicted her. She said it the way "
      "other women describe a scar.{/n}", requires=(PREDICTED,)),
    p("{n}She learned the Commander's trick in the end, as she had promised, and never said how. Several footstools in the "
      "Upper City now walk.{/n}", requires=(TRICK_KEPT, UNMIRRORED)),
    p("{n}She learned the Commander's trick in the end, as she had promised, and never said how. The painter who had sold her "
      "the portrait never worked in the Upper City again, and nobody would say why.{/n}", requires=(TRICK_KEPT, DIMINISHED),
      forbids=(UNMIRRORED,)),
    p("{n}She learned the Commander's trick in the end, as she had promised, and never said how. For a year every gossip in "
      "the Upper City found a lilac-scented card on the pillow predicting, word for word, what they would say about her "
      "next; most of them stopped saying it.{/n}", requires=(TRICK_KEPT,), forbids=(UNMIRRORED, DIMINISHED)),
    p("{n}She never forgot the one dull sentence the Commander said to her, and reminded the Commander of it at intervals, "
      "always in company.{/n}", requires=("vellexia.trickster.cost.bored_once",), forbids=CONTINUING_NOT, any_groups=[["vellexia.farewell_lovers", LATE_COMMITTED]]),
    p("{n}A portrait of the Commander changed hands in the Upper City three times before the war was over, each time for more. "
      "Nobody who bought it would say what it showed. Vellexia bought it in the end, and never said either.{/n}", requires=(SAT,)),
)
TRICKSTER_PARAGRAPHS += tuple(
    {**copy.deepcopy(paragraph),
     "Requires": [*paragraph["Requires"], "sacrifice", "trickster.commander_back"],
     "Forbids": [flag for flag in paragraph["Forbids"] if flag != "sacrifice"]}
    for paragraph in (TRICKSTER_PARAGRAPHS[3], TRICKSTER_PARAGRAPHS[8])
)
MIRROR_PARAGRAPHS = (
    p("{n}The Commander kept the glass covered after the war, in a locked room, and never slept in the next one. The haze "
      "behind the cloth never went still.{/n} \"I will be watching you do it,\" {n}she had said, and she was.{/n}",
      requires=(KEPT, WATCHED)),
)

SCENES.append(scene("vellexia.trickster.epilogue.commit", "Kept waiting", "Epilogue", 5, "", [
    nar("start", '''{n}Lady Vellexia finished the conversation after the war, in her own time and at her own party. She sent for the Commander the way she sent for everyone, and was kept waiting, which nobody could remember happening to her before. She found this so novel that she did not have the Commander upholstered.{/n}''',
      c(), paragraphs=(
          # Q11 r3: her collection survives only where nothing walked out of her house.
          p('{n}She drew the Commander away from the party into a room whose furniture had been guests once and still watched. At her glance, the Commander locked the door and slipped the key down the front of her gown. Vellexia laughed and leaned back against the bed, letting the Commander remove {mf|his|her} own coat. It landed on a chair that flinched.{/n}', forbids=(BARE, FREED)),
          p('{n}She drew the Commander away from the party into the one room of her new house she had finished: a bed, a lamp, bare walls. At her glance, the Commander locked the door and slipped the key down the front of her gown. Vellexia laughed and leaned back against the bed, letting the Commander remove {mf|his|her} own coat. It landed on the floor.{/n}', any_groups=[[BARE, FREED]]),
          p('{n}She ordered more wine sent to the room, then shut the door herself. The Commander unlaced her gown at her direction. Vellexia made {mf|him|her} stop halfway so that she could enjoy the impatience on {mf|his|her} face. Then the silk fell. She watched the Commander strip, smiling at every hurried movement. She drew {mf|him|her} onto the bed and followed, naked. Her hands went down the Commander\'s bare skin, nails first, claiming it in long strokes over ribs and hip, and she took the Commander\'s hand and laid it against her own hip, holding it there, setting her own pace, smiling as she watched {mf|his|her} face. Her mouth found {mf|his|her} throat.{/n}\n"You kept me waiting," {n}she said against it.{/n} "Now pay."'),
          p('{n}In the morning there was a bruise on the Commander\'s throat. Vellexia was still in bed, watching {mf|him|her} discover it.{/n}\n"Again. I have decided."'),
          p("{n}Daeran, who saw the bruise at breakfast the next week, said only that he had never known her to bill a guest in "
                         "person, and asked whether the Commander would be needing a scarf.{/n}", requires=("daeran.in_party",), forbids=DAERAN_GONE),
                       *({**TRICKSTER_PARAGRAPHS[0], "Text": '{n}Her guests had toasted her memory. At her party she made them repeat the speeches to her face, correcting the dull parts herself.{/n}'}, *TRICKSTER_PARAGRAPHS[1:])))],
    requires=(LATE_COMMITTED,),
    forbids=("vellexia.committed", "vellexia.closed", DECLINED, KEPT, "vellexia.farewell_kept", "vellexia.farewell_friends", "vellexia.farewell_slow", NIGHT_KEPT, "sacrifice", "inhuman", "ascended"),
    # Q11 r3: a genuine sacrifice is mourned (ending_sacrifice) and nothing else; a Commander who came back keeps the romance.
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=99, Relationship="vellexia"))


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
    # Q11: the night's aftermath (Directive 12): Daeran sees the bruise. Never on friendship or the kept mirror.
    reaction("Daeran", "vellexia.trickster.reaction.daeran_night", (NIGHT_KEPT,),
             '''{n}Daeran's eyes go to your scarf, and stay there, and he smiles the way a man smiles at a rival's bill.{/n} "Lady Vellexia came to Drezen, then. Through the war, to your quarters. The sentries are still arguing about the dress." {n}He tugs the scarf an inch lower with one finger, inspects the bruise, and lets it fall back.{/n} "I have collected every rumour about her for twenty years, and in none of them does she make a house call. Do keep breathing, Commander. She hates to lose a piece before she has finished with it."''',
             answer_list=DAERAN_HUB, forbids=(*DAERAN_GONE, KEPT, "vellexia.farewell_friends", "vellexia.closed"), chapter=5, last=5,
             delay=6, entry='"About Lady Vellexia..."'),
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


# --- Path fit (13 directive update 2026-09-29 / ROUTE-BRIEF-R §2; recorded in PP8). --------------------------------------
# Every scene here stands on the Trickster device (the mirror let go, the likeness woken) or on a flag only the device
# sets (the Storyteller, Finnean and Daeran reactions read unmirrored/likeness/entry), so all are T. Her non-Trickster
# courtship is the registered route (vellexia_opening, vellexia_campaign), path-neutral; 14-PATH-FIT §3 fits it on Demon
# (Y; her Ch5 Drezen presence is Demon-only) and maybe Devil and Lich. Canon fate off Trickster: killed or spared in Ch4.
# Pacing (PP8): Ch4 8 in person + 3 remote, Ch5 18 + 14; she is absent before Ch4, so there is no early beat. T5
# (Vellexia via Arueshalae) is deferred to the household pass (15b).
PATH_FIT = {s["Id"]: "T" for s in SCENES}
PATH_FIT_V2 = {}


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
    payload.setdefault("Etudes", {})["daeran.in_party"] = "e49732bbb3126ec4280cf7f12946abad"
    payload.setdefault("DerivedForbids", {})[LATE_COMMITTED] = ["vellexia.farewell_friends", "vellexia.farewell_slow"]
    payload.setdefault("Derived", {})["vellexia.fight_survived"] = [["vellexia.spared"], [RETURNED]]
    # Q11: a provoked guest comes to Drezen in person, as an unmirrored, diminished or predicted one does.
    payload["Derived"]["vellexia.trickster.in_person"] = [[UNMIRRORED], [DIMINISHED], [ENTRY], [PROVOKED], [UNPAID]]
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
        s.pop("RequiresAnyGroups", None)   # Q11: the native-ending group is implied by the predecessor (or by a return)
        s["ForbidOverrides"] = dict(FO)
    _scene(by_id, "vellexia.the_voice_after_the_abyss")["ForbidOverrides"] = dict(FO)

    # Endings: grief only while she stays dead; the mirror only while she stays glass (G6).
    _forbid(_scene(by_id, "vellexia.ending_dead"), RETURNED)
    mirror = _scene(by_id, "vellexia.ending_mirror")
    _forbid(mirror, UNMIRRORED)
    _paragraphs(mirror, MIRROR_PARAGRAPHS)
    _node(mirror, "start").setdefault("Paragraphs", []).extend(_node(mirror, "start").pop("_Round2Receipts", []))
    _node(mirror, "start")["Paragraphs"].append(
        p("{n}She had promised to watch the Commander regret it. Behind the glass, she had time.{/n}",
          requires=(WATCHED,)))
    _forbid(_scene(by_id, "vellexia.ending_hostility"), "vellexia.spared", RETURNED)
    for name in ORDINARY_ENDINGS:
        s = _scene(by_id, "vellexia.ending_" + name)
        # Q11: a Commander who came back (the native punchline, Last Call) is not mourned and keeps the ordinary ending.
        s["ForbidOverrides"] = ({**FO, "sacrifice": "trickster.commander_back"} if "sacrifice" in s["Forbids"] else dict(FO))
        if name == "sacrifice":
            _forbid(s, "trickster.commander_back")
        _forbid(s, KEPT)
        consequences = copy.deepcopy(TRICKSTER_PARAGRAPHS)
        if name == "interrupted":
            # Preserve the old paragraph slots, retire recurring private contact.
            for i in (3, 8, 10, 11):
                consequences[i]["Forbids"].append("vellexia.prediction_known")
        new_receipts = _node(s, "start").pop("_Round2Receipts", [])
        _paragraphs(s, consequences)
        _node(s, "start").setdefault("Paragraphs", []).extend(new_receipts)
    _forbid(_scene(by_id, "vellexia.ending_interrupted"), LATE_COMMITTED)
    # Cloud voice-owner pass (villain-route-vellexia): text and read-only paragraphs, applied last.
    from storylines import vellexia_cloud
    vellexia_cloud.integrate(payload)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'vellexia.trickster.mirrored.fetch',
    'vellexia.trickster.mirrored.speaks',
    'vellexia.trickster.mirrored.unmirror',
    'vellexia.trickster.mirrored.unmirror_stores',
    'vellexia.trickster.sword.likeness',
    'vellexia.trickster.sword.likeness_stores',
    'vellexia.trickster.sword.portrait',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
