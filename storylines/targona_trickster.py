"""Targona on the Trickster path (Writer/handoffs/trickster/targona.md).

Device (quality pass Q6, 2026-09-30; supersedes the scroll described below, which is retired by gating: the campaign has
one raise, Irabeth's chapel diamond, and Targona's route uses none). Killed state: **Areelu's sleep, kept for her.** Canon:
the Echo of Deskari left her to die, and Areelu "brought me here from the brink of death" (TargonaWings, "How did you end
up here?"); "she put me into a deep sleep. A healing sleep, she said. It was necessary to allow my new, abominable wing to
settle in. I have been in that sleep until now" (Cue_0033 3ab1909d); the barrier round "the frozen angel" (Cue_0029
0047e99c) is "created from the essence of the Abyss and reinforced with spells repelling any living creature not of this
dark plane" (Cue_0038 1cfe35cb); the Suture's Key to the Abyss Barriers (AbyssalKey b5b0214f, read as InventoryItems
targona.abyss_key_held) removes it, and [Destroy the barrier] (Answer_0031) is the only native branch that hides the field
and lifts the hold on her (HoldMonsterVisualOnlyBuff_Cutscene 163b3dad); [Attack] (Cue_0035) does neither. The
Commander's plan, made with her at the barrier before the blow: a real fight, her fall at the ring, her own crawl back into
the sleep that held her once, the key kept in the Commander's pack while the whole company sees an angel die, and a return
alone to break the ring. Whether the sleep will hold a dying body twice is the Commander's gamble and her risk, never stated
as a rule. Costs: she chooses to lie down again in her torturer's work, where "even the goddess cannot hear me"
(Cue_0017), and wakes with the black wing further settled into her; she tells Heaven; the lists still name her dead. An
unprepared [Attack] is the Commander's own choice of a non-partner's death and stands (11-ROSTER-PLAN-2 section 5 ruling
#2); the no-kill branch is [Destroy the barrier]. Earlier design notes follow, kept for history.

Targona on the Trickster path: spend it again, unnoticed (Writer/handoffs/trickster/targona.md; F16).

Canon: the Silver Twins are "two angels who emerged from one soul" (c1/EstrodTower/Teldon/Cue_3 67eb3b5e); the Hand says
"They called each other brother and sister because one soul was used to create them" (string 49d154d6). Lariel met his
end under Kenabres, and when his sword vanished at the Commander's touch "a part of its power entered your soul"
(glossary). The Trickster's own unlock, TricksterUseMagicDeviceTier2Feature 1383f215, lets the Commander "use items so
delicately that their use is completely unnoticed. Wands you use no longer lose charges from use". The device is the
Trickster answering a scripted fate with the one remedy the game allows after a death, prepared before the blow: the
crusade's Scroll of Resurrection (6169a9e1; Resurrection 80a1a388 restores "life and complete strength to any deceased
creature", which in Wrath's own rules covers an outsider as raise dead does not), read over her body in
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
HERALD_KILLED = "herald.killed"     # HeraldKilled 348dfb40 (ImportantNPCs_fate): the Hand is dead; reports go to the chapel
DRAWN = P + "drawn"                 # Q6 r4: in the freed state she stays because the Commander asked her to, not only for the wounded
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
CRYPT = P + "cost.raised_from_the_crypt"   # Chapter 5 fallback: no primer, no Chapter 3 retrieval; raised from the Hand's crypt
TESTED = P + "washed_the_dead"      # death branch: she asked the Commander's hands to wash a dead man with her, and they did
DEAD_SEEN = "targona.dead_lab.latched"   # the laboratory death, latched when first observed: one_soul's three days run from it
PARENT_ROMANCED = P + "parent_romanced"    # derived: RanRomance's Angelic Treatment completed as a romance (its own route runs)
SACRIFICE_GUARD = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})
# Quality pass Q6: Areelu's sleep, kept for her (no raise of any kind).
KEY_HELD = "targona.abyss_key_held"          # InventoryItems AbyssalKey b5b0214f, "Key to the Abyss Barriers" (the Suture's)
SLEEP = P + "cost.her_sleep"                 # she agreed to lie down again in Areelu's sleep, and did
LONG = P + "cost.slept_through_the_abyss"    # the Abyss took the Commander before the ring was broken: she lay there for months
RETIRED = "chapter_later"                    # retired by gating: the runtime holds chapter_later in every chapter >= 2 (Main.BuildState, Rules.ChapterFlag), so these Chapter 3/5 scenes never open

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
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
# game itself allows after a death for any creature, an outsider included: resurrection ("restore life and complete strength
# to any deceased creature", Resurrection 80a1a388), from the crusade's own Scroll of Resurrection (6169a9e1). The Trickster's Use
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
"Resurrection is not mercy, Commander. I have watched chaplains use it. It gives back the body whole, every hair of it, and nothing of what the dying was like. And you are asking me to let them mourn me. My healers in Heaven. The Hand, who has already buried my brother. Everyone who ever prayed beside me."
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
           '''{n}You show her what is inside your sleeve: a scroll of resurrection from the crusade's reliquary, signed out against your name for next month's relic tithe. It was written for a chaplain's hands. Your hands have learned to use any made thing as if it had been made for them, and so lightly that nobody ever sees them do it.{/n}
{n}"If you fall," you tell her, "I will read it over you before they carry anyone out, and nobody in this room will know. And I'll have my hand on you while I read, with his light in it. You made the sword it came from. Whatever you are when the scroll finds you, you'll know that. You will wake alone, and whole, and you will remember all of it. Stay down until we are gone."{/n}''',
           (PRIMED, LAB_LINE, TOLD), ("trickster", UMD2), (PRIMED, FREE, DEAD, CONDEMNED, RETIRED))   # retired by gating (Q6)

lab_primer(P + "dead.setup_open",
           '[Spend it again, openly] "Whatever strikes you in this room, I\'ll read you back in. In front of everyone, if I have to."',
           '''{n}You show her what is inside your sleeve: a scroll of resurrection from the crusade's reliquary, signed out against your name for next month's relic tithe. You have no gift for hiding the use of a thing, and no right to read a chaplain's scroll at all: the old chaplain who signed it out has come down into the ruin with your company for exactly this, and if it comes to it he will read it on his knees over her body, aloud, with every soul in this room watching.{/n}
{n}"If you fall," you tell her, "he will bring you back where you fell, and my hand will be on you with his light in it. You made the sword it came from; you'll know it. They will see me do it. You will wake whole, and they will know why."{/n}''',
           (PRIMED, LAB_LINE, TOLD, OPEN), ("trickster",), (PRIMED, FREE, DEAD, CONDEMNED, UMD2, RETIRED))   # retired (Q6)


# Quality pass Q6: the new primer. Same hook (her own laboratory list, non-inline, before the native choice), one scene for
# every Trickster: the plan is nerve and preparation, not a chosen trick. It needs the Suture's key in the Commander's pack,
# because the key is the only thing that opens the ring again (a Commander without it can fetch it and come back).
SCENES.append(scene(P + "dead.setup_sleep", "Her sleep", "Targona", 3, '"Before anything else. Look at me."', [
    nar("start", '''{n}Behind the barrier the angel lifts her head. The black wing twitches, as if something in the room has startled it.{/n}
"You... carry something of my brother. I can feel it, like a lamp left burning in another room. Under Kenabres, in the rock where he died. It went into you." {n}Her voice does not break, but it thins.{/n} "Lariel is gone. I felt him go."''',
        c('"The Echo left you to die among your dead. How are you still alive?"', "sleep"),
        c('"Nothing. Forget I spoke."', abort=True)),
    t("sleep", '''"Because she wanted me alive." {n}She does not say the name. She looks past you at the purple fire that rings her in.{/n}
"Areelu found me on that field with my wing torn off and brought me here from the brink of death. She put me to sleep in this ring. A healing sleep, she said, so that her wing could settle into me. I did not breathe in it, I think. I did not dream anything of my own. I have been in it until you came."
{n}The black wing draws tight against her back.{/n} "It is still there. I can feel it under me, like cold water waiting for me to lie back down."''',
        c('[Keep her sleep for her] "Then lie back down in it, if you have to. Listen."', "plan", mythic="Trickster", alignment=("Chaotic", 1)),
        c('"Then we\'ll get you out of it."', abort=True)),
    nar("plan", '''{n}You tell her quietly, with your back to your company.{/n}
{n}If you break the barrier, she walks out free, and Heaven calls her home to its finest healers, as the Hand has already promised it will; she will spend years being mended in the halls of Heaven while Drezen's wounded die in rows. Heaven does not call home an angel it believes dead.{/n}
{n}So it ends in blood, and real blood. You will not pull a single blow, because your company would see it, and so would she. When she falls, she falls by the ring, and while your people are still turning to the door you roll her back over its line into Areelu's sleep, the way it took her the first time. Nothing living can follow her in there; Areelu built the fire to keep the living out. Your company will see an angel die and a ring of fire that will not give up her body, and they will leave her to it, because you will tell them to.{/n}
{n}The Suture's key stays in your pack. In three nights you come back down alone, break the ring with it, and wake her.{/n}
{n}"I can't promise the sleep will hold you twice," you tell her. "It held you once, from further down than I'll put you."{/n}''',
        c("Continue", "resist")),
    t("resist", '''"No." {n}She says it at once, and then she makes herself look at the fire properly.{/n}
"You are asking me to lie down again in the thing she made of me. In a room where even the goddess cannot hear me. I prayed every hour I was awake in here to be let out of it, and you want me to crawl back in with my own hands."
"And my healers in Heaven will mourn me. The Hand, who has already buried my brother. Everyone who ever prayed beside me." {n}The black wing shivers.{/n} "Tell me why I should do that."''',
        c('[The wounded] "Because Drezen\'s infirmary loses a man every hour, and none of them will ever reach Heaven\'s healers. They could reach you."', "chooses"),
        c('[The truth] "Because I want you alive. That\'s all. I won\'t dress it up."', "chooses"),
        c('"Then I won\'t ask it of you."', abort=True)),
    t("chooses", '''{n}She is quiet. Somewhere below, in Areelu's cells, something is screaming, and she turns her head towards it the way a healer does, without thinking.{/n}
"I believe this is a test for me," she says at last. "I did not think I would be the one setting it." {n}She looks back at you.{/n} "If I wake, I will not hide. I will go to the Hand first, and to my healers, and I will tell them what we did and why, and let them judge it, whatever it costs you."
"Then hear my conditions. No fire on me, and no blow at my head; I will need it. When I go down, you stand over me and let no one finish me. And it is your hands that put me back in her fire. No one else's."
"And if I do not wake, do not come back for the body. Leave me in her fire. I will have chosen it."
{n}She lowers her head, as she did before, and waits for you to choose.{/n}''',
        c('[Accept her price] "Tell them everything."', flags=(PRIMED, LAB_LINE, TOLD, SLEEP))),
], requires=("trickster", KEY_HELD), forbids=(PRIMED, FREE, DEAD, CONDEMNED, RETIRED), last=3, optional=True, Relationship="targona",
   AnswerLists=[LAB_LIST], EntryMythic="PlayerIsTrickster"))   # retired by gating (Q6 r3): see the note below

# Q6 r3: the killed state has no device. Native [Attack] (Answer_0034 -> Cue_0035) starts a real, lethal fight and the
# etude TargonaIsWasKilledInAreeluLab; no primer can make that fight survivable without a raise (the campaign's one raise
# is Irabeth's) or an engine interception of native combat, and Areelu's sleep is not a mechanism the barrier renews.
# The attack is the Commander's own open-eyed choice against a woman who is not yet a partner, so canon stands
# (11-ROSTER-PLAN-2 section 5, coordinator ruling #2, user-confirmed 2026-09-28: "canon stands; a player-chosen kill of a
# non-partner is not fate"). Her Trickster route is the freed state: [Destroy the barrier], the wand night, the furlough.
# Every killed-state scene (setup, setup_open, setup_sleep, late_light, late_crypt, one_soul, long_sleep and their
# consequences) keeps its ids and is unreachable: no primer can set `primed`.

def ring_nodes():
    """Quality pass Q6: the laboratory as it happened, and the night the Commander went back down with the key."""
    return [
        nar("ring", '''{n}The laboratory. You have lived it again every night since:{/n}
{n}You give the word, and she keeps her promise. She fights with everything she has and Iomedae's name in her mouth, and you do not pull a single blow. She falls by the ring and lies still, the way the dead lie. You stand over her as she asked. While your company turns to the door and whatever Areelu has left waiting there, you kneel, and with your own hands roll her back over the purple line. The fire closes over her, and her breath stops the way it stopped for all those months before you came.{/n}
{n}Your company sees an angel die. The first man who reaches in to carry her out is thrown back across the floor with his gauntlet smoking. "Leave her," you say. "Areelu's fire keeps its dead." Nobody argues. The Suture's key stays in your pack.{/n}''',
            c("Continue", "down")),
        nar("down", '''{n}On the third night you go back down alone, with a lantern and the key, and nobody asks where.{/n}
{n}She lies inside the ring as you first found her, face tranquil, chest still. Where your company's blows went in, the skin has closed, the way the seams of the black wing closed the first time. The wing has shifted a finger's width from where it fell. Nothing else in the room has moved.{/n}
{n}The key breaks the ring. The fire goes out. For three breaths nothing happens, and you have time to think of what you will say at her pyre. Then the angel awakens, as she woke the day you first came into her laboratory, and her first breath is a sob.{/n}''',
            c("Continue", "woken")),
        t("woken", '''"It held." {n}She says it to the ceiling, not to you.{/n}
"I dreamed her dreams again. Hers, not mine." {n}She looks down at the black wing, which has folded itself against her side before she told it to.{/n} "And it has had three more nights to settle into me. I can feel it listening now."
{n}She gets up on her own, and will not take your arm. At the stair she stops.{/n} "Take me to your wounded, Commander. I lay down in her fire for them. I would like them to have the worth of it."''',
            c("Continue", "news_ring")),
        nar("news_ring", '''{n}She goes to the field infirmary behind the quartermaster's stores before dawn and asks for water and a basin, and by first light she is washing wounds.{/n}
{n}By noon Heaven's envoy to the crusade has heard it from the Commander's own officers: the angel they watched die in Areelu's laboratory is changing bandages in Drezen. Half of them saw the fight. None of them can say how. The envoy withholds his blessing from the next muster until someone gives him an answer he can carry back to Heaven.{/n}''',
            c('[Go to her] Go down to the infirmary.', crusade=("Favors", -150), flags=(RETURNED, STARTED, STRUCK, SHARD))),
    ]


# R2-2 late fallback: no scroll was prepared. The act is performed now and paid for: her body is carried out of the ruin
# and brought back the hard way, days late, on the crusade's last Scroll of Resurrection (6169a9e1).
letter(P + "dead.late_light", "The hard way back", [
    nar("start", '''{n}You did not think of it in the laboratory. You think of it now, with a report on your table that lists her among the dead and says her body was left where she fell.{/n}
{n}Somewhere under the city a demon army is regrouping. Going back into Areelu's ruin for one body will cost blood and favours you cannot spare.{/n}''',
        c('[Send them back for her] "Bring her out. The chaplain reads; I hold her."', "raise", mythic="Trickster", crusade=("Favors", -300)),
        c('"Let her rest."', abort=True)),
    nar("raise", '''{n}Four volunteers go back into the ruin and come out with her wrapped in a Mendevian cloak. All four come out. One of them leaves an arm down there, and the other three do not speak of what is still down there. At the chapel the old chaplain reads the reliquary's scroll of resurrection over her, at the hour the priests call the thin one, with his eyes shut on the hard words, while you kneel on the other side of the bier with your palm flat on her heart and her brother's light in it. It is the last scroll the crusade has, and the treasurer will want to know why.{/n}
{n}The breath goes into her like a blade. The scroll gives her body back whole, the black wing and all, and gives her nothing back of the days she lay in the ruin.{/n}''',
        c('[Stay until she breathes.]', flags=(PRIMED, LATE, ECHO_SPENT))),
], requires=("trickster", DEAD), forbids=(PRIMED, RETURNED, RETIRED), delay=0, chapters=(3,),   # retired by gating (Q6)
   )   # Q6 r4: dormant, no longer an advertised device or TricksterState

# Sol quality pass (INT): the same fallback after the Abyss, for a Commander who never prepared the scroll and never sent
# back into the ruin in Chapter 3. Dearer, and later: the Hand's chaplains carried her out of the ruin themselves and have
# kept her in the chapel crypt while Heaven decides where an angel is buried (authored).
letter(P + "dead.late_crypt", "The crypt under the chapel", [
    nar("start", '''{n}The crusade's chaplains keep a crypt under the chapel for the dead whose orders have not yet said where they are to be buried. Since Areelu's laboratory they have kept an angel in it, on a bier, under a Mendevian shroud, waiting for Heaven to answer a letter about her. Heaven has not answered.{/n}
{n}You have come back up out of the Abyss with the war nearly over and her name still on a list of the dead. There is one scroll of resurrection left in Drezen: the chaplains' reliquary holds it as the crusade's relic tithe, sealed and promised to Heaven's envoy, who is to carry it back to the Upper Planes after the Threshold as proof that the crusade kept faith.{/n}''',
        c('[Break the tithe seal] "Open the crypt. You read, I hold her, and the envoy can take it up with me."', "raise",
          mythic="Trickster", crusade=("Favors", -500)),
        c('"Let her rest."', abort=True)),
    nar("raise", '''{n}The chaplain-captain opens the reliquary with a face like a shut door and makes you break the envoy's seal with your own thumb. By nightfall the envoy will know whose thumb it was, and he will take his blessing off the Threshold muster, and every officer in Drezen will know why.{/n}
{n}In the crypt you turn back the shroud. She looks as she did on the laboratory floor. The crypt is cold, and the chaplains have been careful with her. He reads the scroll over her by one lamp, because he is sworn to and you are not able, and you kneel at her side with your palm flat on her heart and her brother's light in it. It goes to ash in his hands at the last word. The breath goes into her like a blade, and she opens her eyes on a stone ceiling and your face.{/n}''',
        c("Continue", "wake")),
    t("wake", '''{n}It is a long time before she can speak, and when she can, it is only a whisper.{/n}
"Whose scroll?" {n}She hears the answer out. The black wing moves once against the bier.{/n}
"Heaven's tithe. You broke Heaven's tithe for an angel you killed." {n}She closes her eyes.{/n} "I would have told you to leave me. You knew that. It is why you did not wait until I could."
"Then I will not be carried to a crypt again for nothing. Take me up to the infirmary, Commander. If I am to cost that much, the wounded had better get the worth of it."''',
        c('[Carry her up the crypt stair.]', flags=(PRIMED, LATE, CRYPT, RETURNED, STARTED, STRUCK, SHARD))),
], requires=("trickster", DEAD), forbids=(PRIMED, RETURNED, RETIRED), delay=0, chapters=(5,),   # retired by gating (Q6)
   )   # Q6 r4: dormant, no longer an advertised device or TricksterState

letter(P + "dead.one_soul", "Read back in", [
    nar("start", '''{n}A runner comes up from the field infirmary behind the quartermaster's stores, out of breath, with his cap in his hand.{/n}''',
        c("Continue", "quiet", forbids=(ECHO_SPENT, OPEN, PRIMED)),     # retired by gating (Q6; index kept)
        c("Continue", "open", requires=(OPEN,), forbids=(ECHO_SPENT, PRIMED)),   # retired (Q6)
        c("Continue", "cold", requires=(ECHO_SPENT,), forbids=(PRIMED,)),       # retired (Q6)
        c("Continue", "ring", requires=(KEY_HELD,)),
        c("Continue", "no_key", forbids=(KEY_HELD,))),
    nar("no_key", '''{n}You reach into your pack for the Suture's key, as you have every night since the laboratory, and your fingers close on nothing. Without it the ring will not open for anyone living. You send the runner away with a coin and no answer, and go through every pack and chest you own.{/n}''',
        c("[Find the key before you go down.]", abort=True)),
    nar("quiet", '''{n}The laboratory. You have lived it again every night since:{/n}
{n}You give the word, and the fight goes the way the story always meant it to, and she falls. The room turns towards the door and whatever Areelu has left waiting there. You kneel beside her as if to close her eyes, and under your breath, no louder than a prayer for the dead, you read the scroll from your sleeve to its last word, with your other palm flat over her heart and her brother's light in it, turned down to the warmth of a hand. It crumbles to ash against your palm. For one breath the light under your hand stings the way it stung in the rock under Kenabres, when his sword went out at your touch and left its fire in you, and then it is only warm. Nobody turns round. Her chest does not move. You leave her there, as she asked.{/n}''',
        c("Continue", "news")),
    nar("open", '''{n}The laboratory. You have lived it again every night since:{/n}
{n}You give the word, and the fight goes the way the story always meant it to, and she falls. You are on your knees beside her before anyone can move, your hand on her heart and her brother's light coming out through your fingers white and plain as day, and the old chaplain is kneeling on her other side with the scroll open, reading aloud. Every face in the room turns to you. Someone by the door says your name like a question. The last word, and the scroll goes to ash in his hands, and her chest does not move, and you stand up and say, "Leave her. She'll come," and walk out past all of them. Nobody asks you what they saw. They will ask each other for months.{/n}''',
        c("Continue", "news_open")),
    nar("news_open", '''{n}The runner says that an angel with one black wing is up and washing wounds. Her hands shake on the basin. She asked whether the Knight-Commander was awake.{/n}
{n}Half the officers in Drezen already know whose hand was on her heart; they were in the room. By noon Heaven's envoy has heard it from three of them, and he does not ask by whose hand. He asks why the crusade's relic tithe was spent on an angel the Commander had just ordered cut down, and he withholds his blessing from the next muster until someone gives him an answer he can carry back to Heaven.{/n}''',
        c('[Go to her] Go down to the infirmary, past the soldiers who saw.', requires=(OPEN,), crusade=("Favors", -300),
          flags=(RETURNED, STARTED, STRUCK, SHARD))),
    nar("cold", '''{n}You remember the chapel exactly: the scroll, the breath going into her like a blade, the chaplain praying with his eyes shut. She did not wake while you were there. The priests carried her down to the infirmary on a litter, as one more wounded thing.{/n}''',
        c("Continue", "news")),
    nar("news", '''{n}The runner says that an angel with one black wing is up and washing wounds. Her hands shake on the basin. She has not said her name. She asked whether the Knight-Commander was awake.{/n}
{n}By noon Heaven's envoy to the crusade has heard, and by evening the Queen's chaplains have: an angel the lists call dead is changing bandages in Drezen, and nobody can say by whose hand. The envoy withholds his blessing from the next muster until someone explains it.{/n}''',
        c('[Go to her] Go down to the infirmary.', forbids=(OPEN,), crusade=("Favors", -150), flags=(RETURNED, STARTED, STRUCK, SHARD)),
        c('[Go to her] Go down to the infirmary, past the soldiers who saw.', requires=(OPEN,), crusade=("Favors", -300),
          flags=(RETURNED, STARTED, STRUCK, SHARD))),
    *ring_nodes(),
], requires=("trickster.ever", PRIMED, DEAD, DEAD_SEEN), forbids=(RETURNED,), delay=72, chapters=(3,),
   )   # Q6 r4: dormant, no longer an advertised device or TricksterState

# Quality pass Q6: the Abyss took the Commander before the three nights were up. The ring is broken in Chapter 5, after
# months, and costs more to reach. One delivery; one_soul never follows it.
letter(P + "dead.long_sleep", "Months in her fire", [
    nar("start", '''{n}You meant to go back down on the third night. The Abyss took you first, and the key to Areelu's ring went into the Abyss with you, in your pack, and came out again with you, months later.{/n}
{n}Nobody has been down to the laboratory since. The reports on your table still list her among the dead, and the one officer who asked what became of the body was told that Areelu's fire keeps its own. The ruin has had months to fill up with what crawls out of the Wound.{/n}''',
        c('[Go back down for her] "Twelve volunteers to the ruin gate. I go in alone."', "ring", mythic="Trickster", crusade=("Favors", -300),
          requires=(KEY_HELD,)),
        c('"Not yet."', abort=True),
        c("[Look for the Suture's key first. Without it the ring will not open.]", abort=True, forbids=(KEY_HELD,))),
    nar("ring", '''{n}The volunteers hold the ruin gate for a night and a day and lose two men to what comes up the stair. You go down past them alone, with a lantern and the Suture's key.{/n}
{n}The purple ring is burning as it burned the day you left it, and she lies inside it as you first found her, silver hair, one wing white and one wing black, her face tranquil, her chest still. Months. The wounds your company gave her are closed, as the wing's seams closed the first time. The black wing is not folded the way it fell. It has moved, in all those months, on its own.{/n}
{n}The key breaks the ring the way it would have broken it the first day. The fire goes out. For three breaths nothing happens, and then the angel awakens, as she woke the day you first came into her laboratory, and her first breath is a sob.{/n}''',
        c("Continue", "wake")),
    t("wake", '''"How long?" {n}You tell her. She lies still and takes it in.{/n}
"I dreamed her dreams the whole time. Hers, not mine. Her grand experiment, her second opening, over and over." {n}She turns her head and looks at the black wing, which has folded itself against her side before she asked it to.{/n}
"It knows me better than it did. I can feel it listening to me." {n}She gets up on her own, and will not take your arm.{/n} "Two men at the gate, you said. Then take me to the infirmary, Commander, and let me earn them."''',
        c('[Walk her up out of the ruin.]', crusade=("Favors", -150), flags=(RETURNED, STARTED, STRUCK, SHARD, LONG))),
], requires=("trickster.ever", PRIMED, SLEEP, DEAD, DEAD_SEEN), forbids=(RETURNED,), delay=0, chapters=(5,),
   )   # Q6 r4: dormant, no longer an advertised device or TricksterState


ward(P + "dead.furlough", "A fever that broke at dawn", '"Targona."', [
    nar("start", '''{n}Wilcer Garms points you past the stores with his quill. "She's at the cots, Commander. Hasn't slept. Hasn't asked for a thing but water."{/n}
{n}He lowers his voice. "The Third Company marched out for the east wall this morning without the envoy's blessing. First time since Kenabres. The chaplains stood on the steps and said nothing, and the men noticed. Two of them are on her cots already."{/n}
{n}The angel does not stand when you reach her. She finishes binding a pikeman's hand first, and ties the knot, and only then looks up.{/n}''',
        c("Continue", "pikeman", requires=(TOLD,)),
        c("Continue", "pikeman_late", forbids=(TOLD,))),
    t("pikeman", '''"Commander. There was a pikeman in your infirmary last night with a fever that would not break. It broke at dawn. I thought you should know that first."
{n}She nods at the two new cots.{/n} "Those men went to the wall unblessed because of me. Heaven's envoy will not bless what he cannot explain, and he cannot explain me. I have told them I am sorry. They did not know what for."
{n}The black wing folds against her back as if it too is listening.{/n}
{n}She sets the basin down with both hands. It is only half full, and still it shakes.{/n}
"I remember your face when you gave the word. I remember every blow, and the floor, and the line of her fire under my hands. Then her sleep, cold, the way it was the first time, with her dreams in it instead of mine. Then your lantern." {n}She flexes her fingers.{/n} "The wounds closed in there. The wing settled a little further into me. I still lie down in that ring every night when I close my eyes."
"I went to the Hand's chaplain before I came here, as I said I would. I told him what was done, and by whom. He let the candle burn down a finger's width before he spoke. Then he blessed me, and not you."''',
      c('[Tell her the truth] "I struck you. I\'d rather you hear it from me than from Heaven."', "truth"),
      c('[Make light of it] "It was a joke. You\'re alive. That\'s the punchline."', "joke"),
      c('[Lie] "Areelu turned my hand. It was never my blow."', "lie")),
    t("pikeman_late", '''"Commander. There was a pikeman in your infirmary last night with a fever that would not break. It broke at dawn. I thought you should know that first."
{n}She nods at the two new cots.{/n} "Those men went to the wall unblessed because of me. Heaven's envoy will not bless what he cannot explain, and he cannot explain me. I have told them I am sorry. They did not know what for."
{n}The black wing folds against her back as if it too is listening.{/n}
{n}She sets the basin down with both hands. It is only half full, and still it shakes.{/n}
"I remember your face when you gave the word. I remember every blow, and the floor, and the line of her fire under my hands. Then her sleep, cold, the way it was the first time, with her dreams in it instead of mine. Then your lantern." {n}She flexes her fingers.{/n} "The wounds closed in there. The wing settled a little further into me. I still lie down in that ring every night when I close my eyes."
"Before I would let them carry me to the cots, I sent for the Hand's chaplain. Nobody asked me to. I had not promised anyone. But I will not live on a lie, and I told him what was done, and by whom. He let the candle burn down a finger's width before he spoke. Then he blessed me, and not you."''',
      c('[Tell her the truth] "I struck you. I\'d rather you hear it from me than from Heaven."', "truth"),
      c('[Make light of it] "It was a joke. You\'re alive. That\'s the punchline."', "joke"),
      c('[Lie] "Areelu turned my hand. It was never my blow."', "lie")),
    t("truth", '''"Yes. And now Heaven will hear that you said so without being asked." {n}She wrings out the cloth, and her hands are not quite steady.{/n}
"I still see your face over me when I close my eyes. I saw it at the fourth bell last night, with this man's fever in my hands, and I had to stop and pray before I could go on." {n}She looks at the two unblessed soldiers, and then at you.{/n}
"Iomedae, give me the strength to mean this. I forgive you, Commander. Now hold his arm still while I bind it. For those men's sake I will not pretend it is easy."''',
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

# Sol quality pass (BEL): after forgiveness and before the vigil, one beat in which she moves first and tests the hands that
# killed her with a concrete act (washing a dead soldier, the rite his own comrades would have done). The ward waits on it.
ward(P + "after.the_washing", "Wash him with me", '"Targona?"', [
    t("start", '''{n}The man on the end cot died at the fourth bell. Targona has drawn the blanket up over his face and set a basin of warm water and a folded length of linen on the stool beside him. She does not look up when you come in.{/n}
"His company is on the east wall and the chaplains are with them. In Iomedae's orders a knight is washed for burial by his comrades, so that he goes to her clean and not alone. He has no comrades here." {n}She holds out the second cloth. Her hand is steady; she has made it steady.{/n}
"Help me, Commander."''',
      c('[Kneel and take the cloth.]', "wash"),
      c('"I\'ll send for a chaplain."', "chaplain")),
    nar("wash", '''{n}You wash him together, the way she shows you: the face first, then the hands, then the rest, and his ring left on. She sings under her breath, not a hymn you know. Twice she stops singing to watch your hands, the hands she last saw over her in Areelu's laboratory, as they move on a body that cannot fight them off, and twice she starts again.{/n}
{n}When he is clean she folds his arms and lays the linen over him, and then she takes your wet hands in hers and dries them herself, finger by finger, longer than drying takes.{/n}''',
        c("Continue", "after")),
    t("after", '''"I wanted to see what they did near a body that could not stop them." {n}She does not let go.{/n} "They were careful. You closed his eyes before I asked."
"I have been forgiving you for days, Commander, because I said I would. Tonight is the first time I have wanted to know anything about you." {n}Her thumb moves once over your knuckles.{/n} "What do these do, when there is no war in them? No. Do not tell me now. Come back when the ward is quiet, and sit with whoever is dying, and I will watch."''',
      c('[Let her keep your hands a moment longer.]', flags=(TESTED,))),
    t("chaplain", '''"They are on the wall, and he is here." {n}She takes the cloth back.{/n}
"Go, then. I will wash him myself. I have done it alone before." {n}She turns down the blanket, and does not watch you leave.{/n}''',
      c('[Leave her to it.]', abort=True)),
], requires=("trickster.ever", FORGIVEN), forbids=(CLOSED, COMMITTED, TESTED, MET), delay=48)


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
{n}By dawn every cot has had its charge, and three empty wands lie on the table by the door.{/n}''',
        c('[Finish at dawn] Put the empty wands away.', "report_hand", forbids=(HERALD_KILLED,)),
        c('[Finish at dawn] Put the empty wands away.', "report_chapel", requires=(HERALD_KILLED,))),
    nar("report_hand", '''{n}The infirmary chaplain writes it into his weekly report to the Hand of the Inheritor, as he writes everything: three wands, one Commander, no deaths by morning. The Hand reads such reports aloud to Heaven's healers. It is the only road there is from a field infirmary to the halls of Heaven, and this time somebody on the far end of it is listening.{/n}''',
        c('[Let the report go up.]', flags=(PRIMED, WAND, CHARGES))),
    nar("report_chapel", '''{n}The infirmary chaplain writes it into his weekly report, as he writes everything: three wands, one Commander, no deaths by morning. Since the Hand fell, the reports go to the chapel of the Inheritor, where the priests read every name of the living and the dead at the altar, for whatever in Heaven still listens. This time something does.{/n}''',
        c('[Let the report go up.]', flags=(PRIMED, WAND, CHARGES))),
], requires=("trickster", FREE), forbids=(WAND, PARENT_ROMANCED, DEAD), delay=0)

ward(P + "free.furlough", "Greetings, my rescuer", '"There\'s an angel in the wards."', [
    nar("start", '''{n}Wilcer Garms clears his throat. "There's an angel in the wards, Commander. I didn't requisition her."{/n}
{n}She has a basin of water, one wing black and twisted, the other folded tight. She is going down the same rows you went down last night, and she stops at each cot as if the man in it were the only one.{/n}''',
        c("Continue", "greet_lab", requires=(LAB_LINE,), forbids=(TREATED, SLEEP)),        # the legacy scroll primer only

        c("Continue", "greet", forbids=(LAB_LINE, TREATED)),
        c("Continue", "greet_treated", requires=(TREATED,)),
        c("Continue", "greet_lab_sleep", requires=(LAB_LINE, SLEEP), forbids=(TREATED,))),
    t("greet_treated", '''"Commander. Greetings, my rescuer, and my physician." {n}She does not smile.{/n}
"You have treated this wing, and argued with it, and sat with me while it was dressed. I thought I knew what kind of soul you were. Then someone worked these rows all night with a healer's wand and would not stop, and word of it reached me in the halls of Heaven, and I came down to see whether it was the same one."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("greet_lab_sleep", '''"Commander. Greetings, my rescuer." {n}She does not smile.{/n}
"Behind the barrier you asked me to lie back down in her sleep if it came to blood, and I said yes. Then you broke the barrier instead, and I went home to Heaven's healers after all. And then someone worked these rows all night with a healer's wand and would not stop. I came to see who would do such a thing, and why."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("greet_lab", '''"Commander. Greetings, my rescuer." {n}She does not smile.{/n}
"Behind the barrier you showed me a scroll up your sleeve and asked me to let everyone mourn me. I said yes. And then you did not need it: you broke the barrier instead. And then someone worked these rows all night with a healer's wand and would not stop. I came to see who would do such a thing, and why."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("greet", '''"Commander. Greetings, my rescuer." {n}She does not smile.{/n}
"Someone worked these rows all night with a healer's wand and would not stop, and word of it reached me in the halls of Heaven. I came to see who would do such a thing, and why."''',
      c('[Explain] "They were dying. I had a light."', "why")),
    t("why", '''"For the wounded." {n}She considers you with sad, clear eyes.{/n}
"Then I will stay, for the wounded. Heaven can spare me for a season, and Heaven's healers have been very kind to me, and very patient with this." {n}The black wing shifts.{/n} "Here nobody has time to be patient with it. I find I prefer that.
"And I would like to know what kind of person uses a dead angel's light to sit up all night with strangers. I have not decided whether I approve."''',
      c('[Welcome her] "Stay as long as they need you."', flags=(MET, STARTED)),
      c('[Say the rest] "Stay for the wounded. And stay because I asked you to."', "drawn", flags=(MET, STARTED, DRAWN))),
    t("drawn", '''{n}She looks at you for a long moment over the basin, and the black wing, which has been folded tight since she came in, loosens a little.{/n}
"That is not a reason Heaven gives furloughs for." {n}She wrings out the cloth.{/n} "It may be a reason I stay anyway. Ask me again when the ward is quiet, Commander, and not over a dying man."''',
      c("[Leave her to the rows.]")),
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
   RequiresAnyGroups=[[TESTED, MET]])

ward(P + "after.quiet_ward", "A quiet ward", '"The ward is quiet."', [
    t("start", '''{n}The ward is quiet. The sergeant has gone back to his company on the east wall. Targona is folding bandages, and she does not stop when you come in.{/n}
"Ask, then. But first promise me something. My brother's light, the part of him that is in you: never spend it on cheating death. I have seen what it can do in your hands. I know what you would be tempted to do with it beside a dying man. Not unnoticed, not for me, not for anyone. If I fall, let me go. My brother went. I would rather be where he is than be the reason you keep cheating."''',
      c('[Promise, and ask her] "I promise. Stay with me."', "promised", flags=(COMMITTED, SEALED)),
      c('[Refuse the promise] "I can\'t promise that."', "unpromised", flags=(CLOSED,))),
    t("promised", '''{n}She puts the last bandage on the pile and squares it with both hands, very neatly, the way she does when she is trying not to let them shake.{/n}
"Then I will hold you to it. I am told that is what Tricksters hate most." {n}She almost smiles.{/n} "Yes."''',
      c("Continue", "threshold")),
    t("unpromised", '''"No. I did not think you could." {n}She goes on folding.{/n}
"You would do it one day, for a stranger with a fever, and you might even be right to, and I would never know when it was coming. I cannot live beside that. I am sorry."''',
      c('[Leave her the ward.]')),
    *night_nodes(),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), delay=72)


# --- Epilogue pages (R2-6; ordered siblings, no page effects) -------------------------------------------------------

LIGHT_PARAGRAPHS = (
    p("Heaven's lists still name her among the dead of Areelu's laboratory. Targona never asked to have the entry "
      "struck. She said it was the most honest thing anyone had written about her, and that the angel on that list had "
      "earned her rest.", requires=(SHARD,)),
    p("She never again slept where a purple light could reach her. She kept a lamp of plain yellow oil burning by her bed, "
      "and the black wing, which had settled into her in Areelu's sleep, learned to fold itself round her before she woke.",
      requires=(SLEEP,), forbids=(LONG,)),
    p("She had lain in Areelu's sleep through all the Commander's months in the Abyss, and dreamed the Architect's dreams "
      "the whole time. She learned the names of the two men who died holding the ruin gate for her, and prayed for them at "
      "every compline, and would not let anyone call the black wing hers, though it folded to her now like a hand.",
      requires=(LONG,)),
    p("The Commander kept the promise made in the quiet ward, never to spend her brother's light on cheating death. It was "
      "harder than any vow they had broken, and Targona knew it, and said so, once.", requires=(SEALED,),
      forbids=("targona.lastcall.called",)),
    p("The Commander broke the promise made in the quiet ward, once, at the rift, and spent her brother's light after "
      "all. She did not leave. She did not pretend it had not happened, either.", requires=(SEALED, "targona.lastcall.called")),
    p("She told Heaven the truth about the laboratory, as she had said she would, and she told it that the Commander "
      "had told it first. Heaven, she reported afterwards, was not amused. She was.", requires=(FORGIVEN,), forbids=(SEALED,)),
)


# The wand night belongs to the freed state only; the death-return ward never had it.
WARD_PARAGRAPHS = (
    p("The wounded who passed through it still told new arrivals about the night the Commander worked the rows with a "
      "wand that never ran down. Afterwards its wands ran down like anyone's, and she rationed every charge, and never once "
      "sent for the Commander to do it again.", requires=(WAND,), forbids=(CHARGES,)),
    p("Three empty wands hung on a nail by its door, from the night the Commander emptied the stores for strangers. "
      "The treasurer's bill for them hung beside them, receipted, and she would not let anyone take either down.",
      requires=(CHARGES,)),
)


def page(id, title, text, requires, forbids=(), paragraphs=(), **extra):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [nar("end", text, paragraphs=paragraphs)], requires=requires,
                        forbids=forbids, last=99, Relationship="targona", **extra))


page(P + "epilogue.commit", "When the ward was quiet",
     '''{n}Targona did not go back to Heaven when the war ended. She stayed in Drezen's field infirmary until the last cot was folded, and on the morning the tents came down she found the Commander and asked the question herself, because, she said, she had waited for the ward to be quiet, and it finally was.{/n}
{n}She did not wait for the answer in words. She took the Commander up the ladder into the empty drying loft, where the last of the bandages still hung in rows from the rafters, and said, "I have tended every body in this city. I want one that is mine to want." She pulled the plain smock over her head and let it fall, and opened both wings, the white and the black, so that the linen swayed all down the row, and drew the Commander down onto the blanket under them and settled astride, and bent to kiss the Commander with her hair falling round both their faces.{/n}
{n}In the morning Wilcer Garms found a black feather on the ladder and wrote something in his ledger. When the new infirmary opened, in a street near the Commander's house, she hung that feather over the door.{/n}''',
     requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"), paragraphs=LIGHT_PARAGRAPHS,
     RequiresAnyGroups=[[TESTED, DRAWN]], **SACRIFICE_GUARD)

# Q6 r4 (TRK/BEL): a freed angel who stayed only for the wounded is a colleague, not a lover, when the war ends first.
page(P + "epilogue.colleague", "The next cot",
     '''{n}Targona stayed in Drezen's field infirmary until the last cot was folded, for the wounded, as she had said. She and the Commander worked the rows together on the bad nights, and argued about wands, and never once about anything else.{/n}
{n}When the tents came down she went back to Heaven's healers with the black wing folded tight, and a letter came to the Commander at midwinter, as correct as a report, asking after the drummer with the fever. At the bottom, in a smaller hand, she had written that the ward was quiet now, if anyone ever wanted to ask her anything that was not about wands.{/n}''',
     requires=("trickster.ever", MET), forbids=(COMMITTED, CLOSED, DECLINED, DRAWN), paragraphs=WARD_PARAGRAPHS)

page(P + "epilogue.ally", "The ward's other chair",
     '''{n}Targona forgave the Commander in front of the whole ward, and meant it, and never went further than that. She stayed in Drezen until the last cot was folded. When the Commander came to the infirmary, she handed over a basin or a roll of linen without being asked, and talked about the wounded, and about her brother, and never about the laboratory. People who saw them together took them for old comrades. In a way they were.{/n}''',
     requires=("trickster.ever", FORGIVEN), forbids=(TESTED, MET, COMMITTED, CLOSED, DECLINED), paragraphs=LIGHT_PARAGRAPHS[:3])

page(P + "epilogue.declined", "The stool by the last cot",
     '''{n}Targona returned to the halls of Heaven with the last of the wounded she could not leave. She never did hear the question asked without a trick in it. In Drezen's infirmary there is still a stool beside the last cot that nobody sits on.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(COMMITTED,))

page(P + "epilogue.furlough", "A wand that never ran down",
     '''{n}Heaven granted Targona her furlough, and then another, and then stopped counting. She kept a ward in Drezen with the Commander's name over the door.{/n}''',
     requires=("trickster.ever",), forbids=(CLOSED, DECLINED, "sacrifice"), paragraphs=WARD_PARAGRAPHS + LIGHT_PARAGRAPHS,
     RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED]],
     ForbidOverrides={DECLINED: COMMITTED, "sacrifice": "trickster.commander_back"})

# The Commander's sacrifice at the Threshold, with no way back (native Epilogues/Cue_0116 records the death): no reunion.
page(P + "epilogue.sacrifice", "The name over the door",
     '''{n}The Commander did not come back from the Threshold. Targona heard it in the infirmary, from a runner who did not know what he was telling her, and she finished binding the arm in front of her before she sat down.{/n}
{n}She asked Heaven for no more furloughs, and Heaven, for once, did not argue. She kept the ward in Drezen with the Commander's name over the door until the last cot was folded, and prayed for the Commander at every compline, and when her superiors in Heaven asked her where she wished to be sent next, she said: wherever the dying are, and nobody sits with them.{/n}''',
     requires=("trickster.ever", "sacrifice"), forbids=(CLOSED, DECLINED, "trickster.commander_back"),
     paragraphs=LIGHT_PARAGRAPHS[:3], RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED]])


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
    # Sol quality pass (BEL): the unspent wand exists only after the quiet wand night; the other histories get their own line.
    reaction("Ember", P + "react.ember_wand", (IN_DREZEN, WAND),
             '''"The angel has a sad wing and a happy face. She let me hold the wand while she worked."
{n}Ember turns her empty hands over.{/n}
"It never got lighter. Things always get lighter when you use them. Not that one. I think it's being kind on purpose."''',
             answer_list=EMBER_HUB, forbids=("ember_dead", "ember_gone", CHARGES), chapter=3, last=5, Chapters=[3, 5],
             entry='"What have you been up to?"'),
    reaction("Ember", P + "react.ember_empty_wands", (IN_DREZEN, CHARGES),
             '''"There are three empty wands on a nail by the angel's door. She says you used them all up in one night, on people you didn't know."
{n}Ember touches the nail with one finger, very gently, as if it might still be warm.{/n}
"She keeps them there so nobody forgets. I think that's a nice thing to keep. Most people keep the full ones."''',
             answer_list=EMBER_HUB, forbids=("ember_dead", "ember_gone"), chapter=3, last=5, Chapters=[3, 5],
             entry='"What have you been up to?"'),
    reaction("Ember", P + "react.ember_bandages", (IN_DREZEN, RETURNED),
             '''"I've been rolling bandages for the angel with the sad wing. She showed me how. You roll them tight so they don't come undone in the bag."
{n}Ember holds up a finished roll, a little lopsided, and looks at it with great seriousness.{/n}
"She says she was asleep in a demon's fire and everybody thought she was dead. She doesn't seem to mind talking about it. She minds a lot about the bandages being tight."''',
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
    rel["Guidance"] += (" On the Trickster path, free her in the laboratory: destroy her barrier with the Suture's key "
                        "(a blow there kills her). Then work Drezen's field infirmary through a night with healing wands, "
                        "and look for Targona at the cots behind the quartermaster's stores in Chapter 3 or Chapter 5.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    etudes = payload.setdefault("Etudes", {})
    if etudes.get(HERALD_KILLED, "348dfb40784b436cbe21347f8e0f08ce") != "348dfb40784b436cbe21347f8e0f08ce":
        raise ValueError("Conflicting binding: " + HERALD_KILLED)
    etudes[HERALD_KILLED] = "348dfb40784b436cbe21347f8e0f08ce"   # HeraldKilled (ImportantNPCs_fate)
    # A completed Angelic Treatment runs RanRomance's own route only when it ended as a romance; a friendship-only treatment
    # history can still be courted on Trickster (Sol quality pass, INT).
    derived = payload.setdefault("Derived", {})
    groups = [[TREATED, "targona.ran_romance"]]
    if derived.get(PARENT_ROMANCED, groups) != groups:
        raise ValueError("Conflicting derived key: " + PARENT_ROMANCED)
    derived[PARENT_ROMANCED] = groups
