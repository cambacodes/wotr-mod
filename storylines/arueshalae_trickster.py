"""Arueshalae on the Trickster path: "Treatment" (Writer/handoffs/trickster/arueshalae.md; family F18, the sneaky quack).

A new native adapter. It reads ArueshalaeRomance d6a90c0f and never starts or completes it; her native romance stands on
every path. Device redesign (2026-10-01, coordinator Option A, "Prevention, not resurrection"): nothing in this route
returns her from death. The Trickster keeps her through preparation made in life:
- her drain: a real spell. Death Ward 0413915f makes its subject "immune to energy drain" (enGB 952800ab), and her caress
  is a drain (hub Cue_0083 0cb8bb69, "Any caress, of any kind, sucks the life from mortals"). It is spent as a Scroll of
  Death Ward 89e10c3f, sold by the native Chapter 3 and 5 scroll vendors; the engine removes one scroll per protected touch,
  and with no scroll there is no touch. The ward lasts minutes; the scenes are timed to it;
- dead in the party: the crusade's own Raise Dead a0fc99f0 and Resurrection 80a1a388 work on any dead companion; the mod
  adds nothing. The old return ("Starving, not dead") and its "Insurance" are retired by gating;
- fallen at her lair (Ch5): the quack's house call leads into the native Trickster recruitment (Answer_0009 -> Cue_0011
  -> Cue_0014 starts EvilArushaRecruited), and the fallen courtship continues on her evil hub. Killing her there closes the
  route by the player's own choice (coordinator ruling). The old referral to her queen is retired by gating;
- romance failed: the crusade's new chaplain, appointed out loud at the shrine at the hour the second company kneels:
  a piece of staging that she then has to live up to with her own hands.
The living courtship on her own hub is arueshalae_treatment and arueshalae_rounds; the other paths' middle beats are
arueshalae_chapel, arueshalae_hours and arueshalae_notes. Scenes after the retired returns (the aftertaste, the count, the
reunion, the arcade) stay only for saves that already hold arueshalae.trickster.returned.

Canon (blueprints.zip / enGB): her hunger, Arueshalae_Jailed/Cue_0026 5942af3e ("I devoured, degraded, and drained their
souls dry... this unholy hunger inside me"); "Everything demons do is a sort of cannibalism. Each devours mortals and
other demons in their own way" (hub Cue_0105 07b4c786). The Trickster's Lore (Religion) rank 1, TricksterLoreReligionTier1Feature
04177c4d (read as MainCharacterFacts trickster.religion_tier1), only lowers the DC of the reading; it protects nothing.

Placement (06-ROUTE-REGISTRY §3): the evil Arueshalae's Drezen beats are at the jeweller's arcade after dark, beside the
capital jeweller (JewelerCapitalTrader bc109323, unused by any other route), with the tailor's awning (TailorCapitalTrader
253cdb8f) as the fallback copy. The crowded anchors (Fye, Wilcer Garms, the smith) are left alone.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
P = "arueshalae.trickster."
UNIT = "a352873d37ec6c54c9fa8f6da3a6b3e1"          # Arueshalae_Companion
HUB = "03ebad9587cbea0438d901a0f8df44f1"           # CompanionDialogues/Arueshalae/AnswersList_0003
EVIL_UNIT = "e3bc95db7e2181d41847b3a1d858258d"     # EvilArueshalae_Companion (faction Player)
EVIL_NPC = "2c8caedd0a558524ca0ed1ab3132fae1"      # CR20_EvilArueshalae_NPC: the second body, for the awning copy
LAIR = "fe9eaf819cf03424a9108aa8b777694d"          # DemonicCommando_Lair
LAIR_LOCATOR = "8b58ebe0-42a8-4be6-96dc-75926e191cb6"  # "Arusha", from Fight_Against_Arusha TranslocateUnit ae8bb680
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
JEWELER = "bc1093231b1577a4485a730c29595195"       # JewelerCapitalTrader (the arcade; no other route's anchor)
TAILOR = "253cdb8f434e5a6469b75e18428316e3"        # TailorCapitalTrader (the fallback awning)
MEET_EVIL_LIST = "3ef227bb0ba84104387fd9b4865a4ce0"  # MeetEvilArusha/AnswersList_0002 ([Attack] is Answer_0010)
TASTE_CUE = "480082b0c04099540be2ed84be7c9536"     # MeetEvilArusha/Cue_0015 "I've wanted to taste you ever since..."
GANG_CUE = "f95980a82d410e143a748c412da887fa"      # MeetEvilArusha/Cue_0006 (clean return to her lair list)
SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"    # CompanionDialogues/Sosiel/AnswersList_0002
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"      # CompanionDialogues/Lann/AnswersList_0003

STARTED = "arueshalae.started"
CLOSED = "arueshalae.closed"
COMMITTED = "arueshalae.committed"
DEAD = "arueshalae_dead"
EVIL_DEAD = "arueshalae.evil_dead"
FAILED = "arueshalae.failed"
RECRUITED = "arueshalae.evil_recruited"
CLAIMED = "arueshalae.nocticula_claimed"
RETURNED = P + "returned"
DECLINED = P + "declined"
PRIMED = P + "primed"
AFTERTASTE = P + "aftertaste"
REUNITED = P + "reunited"
ALLY = P + "ally"
FED_ON_YOU = P + "cost.fed_on_you"
FED_ON_PRISONER = P + "cost.fed_on_prisoner"
FED_ON_DEMON = P + "cost.fed_on_demon"
CHAPLAIN = P + "cost.chaplain"
WARD_FEE = P + "cost.warded_fee"         # the recruited fallen's fee paid behind a real ward: a scroll burned for nothing
LATE = P + "cost.late"
DEBT = P + "cost.nocticula_debt"
FAVOUR = P + "cost.nocticula_favour"
UNANSWERED = P + "cost.unanswered"
HUNGRY = P + "cost.sent_away_hungry"
OPEN_DOOR = P + "cost.open_door"
NO_SECOND_JOKE = P + "cost.no_second_joke"
SAINT_ONLY = P + "cost.saint_only"
NO_STAGING = P + "cost.no_staging"       # the chaplain's week: no more public appointments to keep her"
EVERY_TIME = P + "said_every_time"
IF_ASKED = P + "said_if_asked"
LATE_COMMITTED = P + "late_committed"
GIFT = P + "gift_held"                 # "Insurance": she set her profane gift in the Commander's wrist
ELYSIUM_DONE = "arueshalae.changed"   # StartedDialogs BestEnding (bound in arueshalae_treatment's world keys)
GIFT_TORN = P + "cost.gift_torn"       # the gift carried life the wrong way along it, and tore out of the keeper
IN_HIDING = "noct.defeated_not_dead"          # text-read only (ledger 2): never a scene or choice gate
QUEEN_HIDING = P + "queen_in_hiding"          # Derived node-read alias of IN_HIDING (the second opinion's first page)
FOOLED = "noct.fooled"                        # text-read only
QUEEN_FOOLED = P + "queen_fooled"             # Derived node-read alias of FOOLED
FAVOUR_SETTLED = "nocticula.trickster.favour_called.arueshalae"   # Nocticula's court.arueshalae collected the favour
DEAD_LATCH = "arueshalae_dead.latched"
EVIL_LATCH = "arueshalae.evil_dead.latched"
LAIR_PRESENCE = "arueshalae.presence.evil"
TAVERN_PRESENCE = "arueshalae.presence.evil_drezen"   # the jeweller's arcade after dark
YARD_PRESENCE = "arueshalae.presence.evil_awning"     # the tailor's awning (fallback)
LAIR_FAILED = LAIR_PRESENCE + ".failed"        # runtime: her lair copy is wanted but the locator did not resolve
TAVERN_FAILED = TAVERN_PRESENCE + ".failed"    # runtime: the jeweller's unit is not in the capital
YARD_FAILED = YARD_PRESENCE + ".failed"        # runtime: the tailor's awning did not resolve either (PP2: the letter's gate)
# PP2: a presence's .failed is observed only while its own area is loaded, so the Drezen reunion and the lipstick note read
# latches recorded at the moment of failure (Story.Latches: runtime-derived sources), which survive travel and reloads.
LAIR_LATCHED = "arueshalae.lair_unplaced.latched"
YARD_LATCHED = "arueshalae.awning_unplaced.latched"
LATCHES = {LAIR_LATCHED: [LAIR_FAILED], YARD_LATCHED: [YARD_FAILED]}
# The arcade staging that the tailor's-awning copies must not repeat (applied in integrate()).
YARD_STAGING = (
    ("She slides off the counter,", "She slides off the cutting table,"),
    ("She is standing on the jeweller's counter, which puts her head above yours",
     "She is standing on the tailor's cutting table, which puts her head above yours"),
    ("She steps off the counter into your arms", "She steps off the table into your arms"),
    ("the arcade drops away beneath your boots", "the awning drops away beneath your boots"),
    ("stolen from the jeweller's back room", "stolen from the tailor's back room"),
)
SACRIFICE_GUARDED = (P + "epilogue.commit", P + "epilogue.kept", P + "epilogue.kept_fallen", P + "epilogue.fallen")
NIGHT_DONE = P + "evil.dawn"
# The arcade and its fallback use two different bodies (presences sharing a unit and area must exclude each other).
DREZEN_PLACES = ((TAVERN_PRESENCE, "", (), EVIL_UNIT), (YARD_PRESENCE, "_yard", (TAVERN_FAILED,), EVIL_NPC))

# Device redesign (2026-10-01, coordinator Option A, "Prevention, not resurrection"). Nothing in this route returns her from
# death. Dead in the party, the crusade's own Raise Dead a0fc99f0 and Resurrection 80a1a388 work on any dead companion
# (AbilityTargetIsDeadCompanion, no creature-type limit; ArueshalaeNotInParty_Dead 580a89c5 is CompanionInParty with
# MatchWhenDead), so the mod adds nothing there. Fallen at her lair, the native Trickster line recruits her (Answer_0009
# 2afdcec9 -> Cue_0011 68cfcd11 -> Cue_0014 a12a569b starts EvilArushaRecruited 005c2284); killing her there closes the route
# by the player's choice. Her drain ("Any caress, of any kind, sucks the life from mortals", hub Cue_0083 0cb8bb69) is met by a
# real spell: Death Ward 0413915f ("immune to energy drain", enGB 952800ab), spent as a Scroll of Death Ward 89e10c3f from
# the native Chapter 3 and 5 scroll vendor tables (Scroll_Chapter3VendorTable d33d4c73, Scroll_Chapter5VendorTable 5b73c93d).
# The engine removes one scroll per protected touch (RemoveItemFromPlayer); no scroll, no touch.
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"        # ScrollOfDeathWard (Items/Scrolls/Level4), m_Cost 700
WARD_HELD = "arueshalae.ward_held"                 # InventoryItems: the party holds at least one Scroll of Death Ward
RETIRED = (P + "dead.starving", P + "insurance", P + "evil.diagnosis", P + "evil.late_referral", P + "evil.second_opinion",
           P + "evil.wager", P + "evil.wager_yard", "arueshalae.treatment.the_glover")
REFUSED = P + "terms_refused"                      # her own refusal key on every closing answer (read by her Last Call coda)
RETIRED_TEXT = "{n}(Retired 2026-10-01: nothing in this route returns her from death.){/n}"

RELATIONSHIP = dict(
    Title="Treatment",
    Description=("Arueshalae is hungry. She has always been hungry. I have read the chaplains' books on wards, and I have "
                 "decided to treat it as a medical condition, one scroll at a time."),
    Objective="Speak with Arueshalae",
    Guidance=("On the Trickster path, read up on her drain in the shrine library and take her pulse at her own hub in "
              "Chapter 3; the sessions continue in Chapters 3 to 5. A protected touch needs a Scroll of Death Ward from the "
              "scroll merchants, and spends it. If she dies in the party, the crusade's own rites can raise her. If she "
              "falls, you can bring her back to the party at her lair; killing her there ends this road. If her romance "
              "fails, the shrine still needs a chaplain. Her native romance stands beside all of it."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, EVIL_DEAD, "arueshalae.kicked_out", "arueshalae.kicked_out_evil"], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED, EVIL_DEAD: RETURNED},
    TricksterAccess={
        "dead": dict(detect=[DEAD], device=P + "dead.starving", returned=RETURNED),
        "evil_dead": dict(detect=[EVIL_DEAD], device=P + "evil.second_opinion", returned=RETURNED),
        "failed": dict(detect=[FAILED], device=P + "failed.chaplain", returned=None),
    },
)
REVIVALS = {"arueshalae": dict(Relationship="arueshalae", Unit=UNIT, DeathFlag=DEAD)}

GREET_LAIR = ("{n}Arueshalae is sitting on the rubble of her own lair with her chin in her hand and her wings folded "
              "like a closed book, watching the door as if she has been waiting for you to finish your rounds.{/n}")
GREET_ARCADE = ("{n}The jeweller's arcade, after the lamps are out. The shutters are down and the jeweller has gone home, "
                "and a woman in black is sitting on his counter with her boots crossed, turning a stolen ring on one "
                "finger to catch the moonlight.{/n}")
GREET_AWNING = ("{n}The jeweller's arcade is boarded up. Under the tailor's striped awning, among the bolts of undyed "
                "wool, a woman in black is draped across the cutting table like a length of expensive silk.{/n}")
PRESENCES = {
    LAIR_PRESENCE: dict(Unit=EVIL_UNIT, Area=LAIR, Mode="spawn-copy", At=dict(Locator=LAIR_LOCATOR),
                        Requires=["trickster.ever", RETURNED, EVIL_DEAD], Forbids=[CLOSED, REUNITED], RequiresAnyGroups=[[DEBT, FAVOUR]],
                        MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREET_LAIR),
    TAVERN_PRESENCE: dict(Unit=EVIL_UNIT, Area=DREZEN, Mode="spawn-copy",
                          At=dict(NearUnit=JEWELER, Side="front", Distance=2.0),
                          Requires=["trickster.ever", RETURNED, EVIL_DEAD], Forbids=[CLOSED, ALLY, NIGHT_DONE],
                          RequiresAnyGroups=[[REUNITED, LAIR_LATCHED]],   # PP2 (Sol COX): the reunion moves here when the lair fails
                          MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREET_ARCADE),
    YARD_PRESENCE: dict(Unit=EVIL_NPC, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TAILOR, Side="front", Distance=2.0),
                        Requires=["trickster.ever", RETURNED, EVIL_DEAD, TAVERN_FAILED],
                        Forbids=[CLOSED, ALLY, NIGHT_DONE], RequiresAnyGroups=[[REUNITED, LAIR_LATCHED]],
                        MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub",
                        Greeting=GREET_AWNING),
}

DERIVED = {
    LATE_COMMITTED: [["trickster.ever", AFTERTASTE], ["trickster.ever", CHAPLAIN], ["trickster.ever", REUNITED]],
    # node-read only (ledger 2): the bill owed to a queen in hiding
    UNANSWERED: [[DEBT, IN_HIDING], [FAVOUR, IN_HIDING]],
    # node-read only (ledger 2): the queen is in hiding while the letter is written (audit 2026-09-29: UNANSWERED needs
    # the debt this very letter creates, so it could never select the hiding branch)
    QUEEN_HIDING: [[IN_HIDING]],
    # node-read alias (ledger 2): the queen was fooled at the Council
    QUEEN_FOOLED: [[FOOLED]],
}


def a(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Arueshalae", **kw)


def noc(id, text, *choices, **kw):
    return n(id, "Nocticula", text, *choices, portrait="Nocticula", **kw)


def hub(id, title, chapter, entry, nodes, requires, forbids=(), delay=0, last=5, chapters=None, **extra):
    """A physical scene on her own companion hub (her unit is in the party)."""
    SCENES.append(scene(id, title, "Arueshalae", chapter, entry, nodes, requires=requires, forbids=forbids, delay=delay,
                        last=last, Relationship="arueshalae", AnswerLists=[HUB], ContactUnit=UNIT,
                        Chapters=list(chapters or range(chapter, last + 1)), **extra))


def letter(id, title, chapter, nodes, requires, forbids=(), delay=0, last=5, chapters=None, **extra):
    SCENES.append(scene(id, title, "Arueshalae", chapter, "", nodes, requires=requires, forbids=forbids, delay=delay,
                        last=last, Relationship="arueshalae", Remote=True, Chapters=list(chapters or range(chapter, last + 1)),
                        **extra))


def presence_scene(id, title, entry, nodes, requires, forbids, delay, hub_key, areas, unit=EVIL_UNIT, **extra):
    SCENES.append(scene(id, title, "Arueshalae", 5, entry, nodes, requires=requires, forbids=forbids, delay=delay, last=5,
                        Relationship="arueshalae", Areas=[areas], Chapters=[5], ContactUnit=unit, InteractionHub=hub_key,
                        **extra))


def drezen_pair(id, title, entry, nodes, requires, forbids, delay):
    """An evil-path beat at the arcade, and its copy under the tailor's awning when the jeweller is gone."""
    for hub_key, suffix, extra, unit in DREZEN_PLACES:
        presence_scene(id + suffix, title, entry, [dict(nd) for nd in nodes], (*requires, *extra), forbids, delay, hub_key,
                       DREZEN, unit=unit)


# --- 4. Dead in the party: the crusade's own rites (device redesign 2026-10-01) ------------------------------------------
# RETIRED by gating (ids, nodes and choice indices kept for old saves): the old "Starving, not dead" return and its
# "Insurance". A companion who dies in the party is raised by the crusade's own Raise Dead or Resurrection; the mod adds
# nothing, and the treatment continues on her hub. The scenes downstream of the old return (aftertaste, the count, the
# hundred, Sosiel's offer, terms_again and their reactions) are reachable only from saves that already hold
# arueshalae.trickster.returned, and stay for them.
R = RETIRED_TEXT
letter(P + "dead.starving", "Diagnosis", 3, [
    nar("start", R,
        c('[Treat her like a patient] "You\'re not dead. You\'re starving. Eat."', "treat", mythic="Trickster",
          requires=("trickster.religion_tier1", GIFT), forbids=(GIFT,)),
        c("[Let her rest.]", abort=True),
        c('[Treat her like a patient] "You\'re not dead. You\'re starving. Eat."', "wake", mythic="Trickster",
          requires=(GIFT,), forbids=("trickster.religion_tier1", GIFT)),
        c('[Treat her like a patient] "You\'re not dead. You\'re starving. Eat."', "thread", mythic="Trickster",
          requires=(GIFT,))),
    nar("treat", R, c("Continue", "work", requires=(CLAIMED,)), c("Continue", "work", forbids=(CLAIMED,))),
    nar("wake", R, c("[Lie down beside her, skin to skin, and let her take]",
                     check={"Skill": "SkillLoreReligion", "DC": 22, "Success": "rite_holds", "Failure": "rite_fails"})),
    nar("rite_holds", R, c("Continue", "claimed", requires=(CLAIMED,)), c("Continue", "plea", forbids=(CLAIMED,))),
    nar("rite_fails", R, c("[Get warm. Try again tomorrow.]", abort=True)),
    nar("work", R, c("[Hold on, and keep count of your own heart]",
                     check={"Skill": "SkillLoreReligion", "DC": 16, "Success": "rite_holds", "Failure": "rite_fails"})),
    nar("thread", R, c("Continue", "claimed", requires=(CLAIMED,), flags=(GIFT_TORN,)),
        c("Continue", "plea", forbids=(CLAIMED,), flags=(GIFT_TORN,))),
    a("claimed", R, c("Continue", "plea")),
    a("plea", R,
        c('[Give her your wrist] "Doctor\'s orders."', flags=(RETURNED, FED_ON_YOU, STARTED)),   # retired: no revive
        c('[Have the guards drag a condemned cultist to her] "Not me. Him."',
          alignment=("Evil", 2), flags=(RETURNED, FED_ON_PRISONER, STARTED)),
        c("[Let her keep her vow.]", "vow", flags=(DECLINED,))),
    nar("vow", R, c()),
], requires=("trickster", "trickster.ever", DEAD, DEAD_LATCH),
    forbids=(RETURNED, DECLINED, EVIL_DEAD, CLOSED, "arueshalae.kicked_out", "arueshalae.kicked_out_evil"), delay=24,
    chapters=(3, 5),   # retired: no Recovery (nothing in the route revives her; the native rites do)
    TricksterDevice=True, TricksterState="dead")

hub(P + "returned.aftertaste", "Aftertaste", 3, '"How do you feel?"', [
    a("start", '''{n}She will not quite meet your eyes. She has taken to standing where she can see the door, and to keeping her hands behind her back.{/n}
"I can still taste it. Every time I close my eyes. I thought the worst thing would be the wanting. It isn't. It's that I'm not hungry any more, and I can feel how good that is, and I know exactly what it cost."''',
      c("Continue", "you", requires=(FED_ON_YOU,), forbids=(GIFT_TORN,)),
      c("Continue", "him", forbids=(FED_ON_YOU, GIFT_TORN)),
      c("Continue", "gift", requires=(FED_ON_YOU, GIFT_TORN)),
      c("Continue", "gift_him", requires=(GIFT_TORN,), forbids=(FED_ON_YOU,))),
    a("gift_him", '''{n}She takes your wrist before you can stop her and turns it over. The place where she set her gift is a small white scar now, like a burn from a candle.{/n}
"It's gone. It came back to me down the only road there was, and it brought half your voice with it. The quartermaster asked me yesterday whether you'd been ill." {n}She lets your wrist go.{/n} "That part I won't be sorry for; you told me not to be. The rest of it is another matter."''',
      c("Continue", "him")),
    a("gift", '''{n}She takes your wrist before you can stop her and turns it over. The place where she set her gift is a small white scar now, like a burn from a candle.{/n}
"It's gone. I can feel it's gone. I didn't take it back; it came back on its own, down the only road there was, and it brought half of you with it." {n}She listens to you breathe as if she were counting.{/n} "Your voice is thinner. Did you know? You used to fill a room. The quartermaster asked me yesterday whether you'd been ill." {n}She says it with a professional's bitterness: she knows exactly what was torn out of you, because she used to tear it out of people for a living.{/n} "It grows back, slowly, they say. The thread doesn't; that road's gone. That was mine to take back, and it took itself. I'm not sorry. You told me not to be."''',
      c("Continue", "you")),
    a("you", '''"Do you remember any of it? You were on the chapel floor by the end, and I was holding your hand to my cheek. The chaplain says I made no sound. I thought I was screaming."
{n}Her eyes go to your hands. They have not quite stopped shaking since, and the bandage on your wrist is fresh again this morning.{/n} "You let me take too much. You knew I would. You lay there and let me." {n}She rubs her mouth with the back of her hand.{/n}
"You made me eat. You made me want it, and then you smiled like a surgeon who'd done a clever stitch." {n}A small, shocked laugh escapes her.{/n} "Only you would call my death a bad diet. The novices think you performed a miracle. I didn't have the heart to tell them it was your wrist and a very bad bedside manner."''',
      c("Continue", "test")),
    a("him", '''"They brought him up gagged. A Deskari lay preacher, condemned at the assize. I told you not to watch and you watched." {n}Her hands shake. She puts them flat against her thighs to stop them.{/n}
"He screamed, you know. I didn't hear it at the time. I hear it now, whenever it's quiet. He's still breathing, in the east cells. He'll never be anybody again. You gave me back my life with a stranger's in my mouth, and I don't know whether to thank you."''',
      c("Continue", "test")),
    a("test", '''{n}She makes herself look up.{/n} "Tell me the truth. Not the joke, the truth. If I die again, will you do it again?"''',
      c('"Every time."', "again", flags=(AFTERTASTE, EVERY_TIME)),
      c('"Only if you ask me to."', "ask", flags=(AFTERTASTE, IF_ASKED))),
    a("again", '''{n}She nods slowly, as if you've confirmed a diagnosis she was afraid of.{/n} "Every time. Then hear my side of it, because it isn't a question. You don't do it again unless I ask. If I wake a second time with your wrist in my mouth and no say in it, I walk out of this crusade that same night, and you don't follow me."''', c()),
    a("ask", '''"Good. Then it's mine to ask." {n}Something in her shoulders comes down an inch, and then goes straight back up.{/n} "Which means one day I'll have to. Out loud. With my mouth still tasting of the last time." {n}She wipes her lips with the back of her hand, hard, though there is nothing on them.{/n}''', c()),
], requires=("trickster.ever", RETURNED), forbids=(AFTERTASTE, EVIL_DEAD, CLOSED), delay=24, chapters=(3, 5))

# RETIRED by gating (2026-10-01): the profane gift asked for in life as insurance. Nothing in the route returns her now.
hub(P + "insurance", "Insurance", 3, '"If you died tomorrow, what would happen?"', [
    a("start", R, c("[Ask for the one thing of hers a mortal can carry.]", "gift"), c("[Let it go.]", abort=True)),
    a("gift", R, c("Continue", "reason"), c("[Let it go.]", abort=True)),
    a("reason", R, c("[Agree.]", "given", flags=(GIFT, STARTED)), c("[Let it go.]", abort=True)),
    a("given", R, c()),
], ("trickster", "trickster.ever"), forbids=(GIFT, DEAD, EVIL_DEAD, RECRUITED, RETURNED, CLOSED, "arueshalae.kicked_out",
                                            "arueshalae.kicked_out_evil"), delay=24, chapters=(3, 5))


# --- 5. Evil at the lair (Ch5): bring her home, or close the road -----------------------------------------------------
# Coordinator ruling (2026-10-01): killing the fallen Arueshalae at her lair closes her route by the player's own choice.
# On Trickster the native line recruits her instead (Answer_0009 2afdcec9 -> Cue_0011 68cfcd11, "I had a lot of fun with
# you -- I even missed you a little", -> Cue_0014 a12a569b starts EvilArushaRecruited 005c2284), and the fallen courtship
# below (fallen.house_call / lock / roof) continues from there. The house call at the lair is the quack's own way into that
# native line. The old referral to her queen (diagnosis, late_referral, second_opinion) is RETIRED by gating, ids, nodes and
# choice indices kept; the reunion, arcade and window scenes after it stay only for saves that already hold its return.
SCENES.append(scene(P + "evil.diagnosis", "Bedside manner", "Arueshalae", 5, '[Take her pulse from across the room]', [
    a("start", R, c("[Brace yourself.]", native_next=TASTE_CUE, flags=(PRIMED,))),
], requires=("trickster",), forbids=(PRIMED, EVIL_DEAD, RECRUITED), last=5, Relationship="arueshalae", Chapters=[5],
    AnswerLists=[MEET_EVIL_LIST], NativeReturnCue=GANG_CUE, EntryMythic="PlayerIsTrickster",
    TricksterDevice=True, TricksterState="evil_dead"))

letter(P + "evil.late_referral", "A referral, posthumously", 5, [
    nar("start", R, c("[Send the referral.]", "sent", mythic="Trickster", flags=(PRIMED, LATE)),
        c("[Let it go.]", "gone", flags=(DECLINED,))),
    nar("sent", R, c()),
    nar("gone", R, c()),
], requires=("trickster", EVIL_DEAD, EVIL_LATCH), forbids=(PRIMED, DEBT, FAVOUR, DECLINED), delay=24, chapters=(5,),
    TricksterDevice=True, TricksterState="evil_dead")

QUEEN_CHOICES = (
    c("[Pay the Queen's price.]", "pay", flags=(RETURNED, DEBT, STARTED)),
    c("[Argue the fine print.]", "raised", flags=(RETURNED, FAVOUR, STARTED)),
    c("[Refuse her price.]", "refused", flags=(DECLINED, CLOSED, REFUSED)))
letter(P + "evil.second_opinion", "A second opinion", 5, [
    nar("start", R,
        c("Continue", "unanswered", requires=(QUEEN_HIDING,)),
        c("Continue", "fooled", requires=(QUEEN_FOOLED,), forbids=(QUEEN_HIDING,)),
        c("Continue", "late", requires=(LATE,), forbids=(QUEEN_HIDING, QUEEN_FOOLED)),
        c("Continue", "queen", forbids=(QUEEN_HIDING, QUEEN_FOOLED, LATE))),
    noc("queen", R, *QUEEN_CHOICES),
    noc("late", R, *QUEEN_CHOICES),
    noc("fooled", R, *QUEEN_CHOICES),
    nar("unanswered", R,
        c("[Send back one word: yes.]", "pay_hiding", flags=(RETURNED, DEBT, STARTED)),
        c("[Put it on yourself.]", "raised_hiding", flags=(RETURNED, FAVOUR, STARTED)),
        c("[Send nothing back.]", "refused_hiding", flags=(DECLINED, CLOSED, REFUSED))),
    noc("pay", R, c()),
    noc("raised", R, c()),
    noc("refused", R, c()),
    nar("pay_hiding", R, c()),
    nar("raised_hiding", R, c()),
    nar("refused_hiding", R, c()),
], requires=("trickster.ever", PRIMED, EVIL_DEAD), forbids=(DEBT, FAVOUR, DECLINED), delay=72, chapters=(5,),
    TricksterDevice=True, TricksterState="evil_dead")

# The house call at the lair (new, 2026-10-01): the quack's pulse joke, then straight into the native offer cue. One terminal
# choice only, so nothing replays her gang line (Cue_0006 stays the validated return; retcheck OK); [Attack] and the native
# Answer_0009 stand beside it on the list. This is the pivotal node of her fallen state: bring her home, or kill her.
OFFER_CUE = "68cfcd112d6060141a492949392692aa"   # MeetEvilArusha/Cue_0011 "Hmm... A tempting offer. I had a lot of fun with you"
HOME_VISIT = P + "evil.home_visit"
SCENES.append(scene(HOME_VISIT, "Bedside manner", "Arueshalae", 5,
    '[Take her pulse from across the room] "Pale, feverish, homicidal. Classic case. I didn\'t come to cure you. I came to bring you home."', [
    a("start", '''{n}Arueshalae stares at you. The balor behind her stares at you. Then she throws back her head and laughs, delighted, the way she used to laugh at the mess-tent jokes she pretended not to understand.{/n}
"Home? Darling, I am home. I have a lair, and boys who'd die for me, and a balor who sits outside my door at night." {n}She licks her lip, slowly, and looks you over the way she used to look over a crowded street.{/n} "And you walked all the way down here to take my pulse. You still remember what my hand costs, and you're still holding yours out. That's either very brave or very stupid, doctor. It was always one or the other with you."''',
      c('[Keep your hand out, palm up] "Then come and take it. The war\'s more fun than this hole, and you know it."',
        native_next=OFFER_CUE, flags=(P + "evil.home_offered",))),
], requires=("trickster",), forbids=(EVIL_DEAD, RECRUITED, HOME_VISIT), last=5, Relationship="arueshalae", Chapters=[5],
    AnswerLists=[MEET_EVIL_LIST], NativeReturnCue=GANG_CUE, EntryMythic="PlayerIsTrickster"))

REUNION_OPEN ='''"A second opinion." {n}She smiles with too many teeth.{/n} "You bought me back from her on credit. Don't ever let me see the bill."
"I had a lot of fun with you, Commander. I even missed you a little, which was humiliating. Let's see if you can still keep up."'''
# Her terms are evil terms (08 §2.3): she wants a life. Oblige with your own, oblige with a condemned man's, find the
# third way a Trickster finds (canon: demons devour "other demons in their own way", hub Cue_0105), or refuse her.
REUNION_CHOICES = (
    c('[Let her feed] "Just a taste."', "taste", flags=(REUNITED, FED_ON_YOU)),
    c('[Drag a bound cultist forward] "Not me. Him."', "cultist", alignment=("Evil", 2), flags=(REUNITED, FED_ON_PRISONER)),
    c('[Have the vrock courier caught when it comes back for its fee, and hand her its chain] "Demons eat demons. Eat the messenger."', "demon",
      requires=(LATE,), flags=(REUNITED, FED_ON_DEMON)),
    c('[Refuse her] "Not a drop."', "refuse", flags=(REUNITED, HUNGRY)),
    c('[Send a patrol into the rubble for a live one of her gang] "One of your boys survived. Eat him."', "babau",
      forbids=(LATE,), flags=(REUNITED, FED_ON_DEMON)))
REUNION_ENDS = [
    nar("taste", '''{n}She takes her time. She holds your wrist carefully, the way a good thing would hold it, and then she does not hold it that way at all. When she lets go, she licks her lip and looks at you as if you'd passed an exam you didn't know you were sitting.{/n}
"Still sweet. You'll need to sit down in a moment. Don't be embarrassed. Everybody does."''', c()),
    a("cultist", '''"A cultist. How thoughtful." {n}She looks at him, and then at you, and something in her face goes very flat.{/n} "You do know I can tell the difference? No. Of course you don't. Eat your vegetables, darling, and let me eat mine."
{n}She does. You watch. She wants you to watch.{/n}''', c()),
    a("demon", '''{n}She looks at the vrock, hunched at the end of its chain with its broken beak, and then at you, and bursts out laughing.{/n}
"Oh, that's low. That's beautifully low. You brought your own postman." {n}She takes the chain. The vrock makes a noise like a hinge.{/n} "It's like eating gravel with a sauce on it, you know. It'll hold me for a week. It won't feed me. And you've lost the only thing in the Abyss that would carry a letter for you." {n}Her smile widens.{/n} "Clever. Expensive. I like it."''', c()),
    a("babau", '''{n}Your soldiers drag it in on a chain: a babau from her own gang, the one that ran when the balor fell, which they dug out of the rubble alive this morning on your orders. It sees her sitting up on the stones and makes a sound like a kettle.{/n}
"Oh, Skritch." {n}She sounds almost fond.{/n} "You ran. I saw you." {n}She takes the chain.{/n} "It's like eating gravel with a sauce on it. It'll hold me for a week. It won't feed me." {n}She looks at you over the babau's head, and her smile widens.{/n} "You had them dig one of my boys out alive just for this. That's the nastiest thing you've ever done, darling. I adore it."''', c()),
    a("refuse", '''"No?" {n}She tilts her head, interested rather than hurt.{/n} "Then I'll find someone who says yes. There are always people who say yes. That was the whole trouble with you. You never did."
"Don't wait up."''', c()),
]
presence_scene(P + "evil.reunion", "The patient sits up", '"You look well, for a corpse."', [
    a("start", REUNION_OPEN + "\n" + "\"But first: I'm starving, and you're the one who prescribed it.\"",
      c("Continue", "hiding", requires=(QUEEN_HIDING,)),
      c("Continue", "price", forbids=(QUEEN_HIDING,))),
    a("hiding", '''"She's hiding, you know. Our Lady. First time in a thousand years nobody's watching me eat." {n}She says it lightly, and her eyes go to the dark corners of the lair anyway, as if the dark might be listening. In the Midnight Isles, it usually is.{/n}''',
      c("Continue", "price")),
    a("price", '''"So. The fee for a house call, doctor." {n}She stretches out one bare foot and taps your boot with it.{/n} "Somebody's life, a little of it. Yours or anyone's; I'm not fussy. Choose."''', *REUNION_CHOICES),
    *REUNION_ENDS,
], ("trickster.ever", RETURNED, EVIL_DEAD), (REUNITED, CLOSED, P + "evil.reunion_letter"), 24, LAIR_PRESENCE, LAIR,
    RequiresAnyGroups=[[DEBT, FAVOUR]])   # the queen's price was paid: not a redeemed return from an earlier death

letter(P + "evil.reunion_letter", "A note in lipstick", 5, [
    nar("start", '''{n}A note in lipstick on a pressed black moth wing, pushed under your door by something that did not use the stairs:{/n}
"You didn't come to the lair. Rude. I'm hungry. Leave your window open tonight, or leave a cultist tied to the gate, or leave nothing, and find out what I do about nothing. A."''',
        c("[Leave the window open.]", "window", flags=(REUNITED, FED_ON_YOU)),
        c("[Leave a cultist tied to the gate.]", "gate", alignment=("Evil", 2), flags=(REUNITED, FED_ON_PRISONER)),
        c("[Have a patrol dig a live one of her gang out of the lair rubble, and chain it to the gate instead.]", "vrock", flags=(REUNITED, FED_ON_DEMON)),
        c("[Leave nothing, and let her do what she threatened.]", "nothing", flags=(REUNITED, HUNGRY))),
    nar("window", '''{n}You wake at the hour before the first bell, colder than you went to sleep, with a black feather on the pillow and the taste of someone else's lipstick on your mouth.{/n}''', c()),
    nar("gate", '''{n}In the morning the gate guard reports that the prisoner tied there overnight has gone mad and will not stop weeping. Nobody saw anything. Nobody ever does.{/n}''', c()),
    nar("vrock", '''{n}In the morning there is an empty chain at the gate and a smear of something grey and sticky on the cobbles, and a lipstick mark on the gatepost at exactly the height of a woman leaning against it, laughing.{/n}''', c()),
    nar("nothing", '''{n}In the morning a patrol sergeant of the third company does not report for duty. They find him at noon, smiling, and he never wakes up. There is a black feather tucked into his cuff, addressed to you, and on it, in lipstick: "You chose nothing. Nothing has a name now. It's on your account, darling, not mine."{/n}''', c()),
], requires=("trickster.ever", RETURNED, EVIL_DEAD, LAIR_LATCHED, YARD_LATCHED), forbids=(P + "evil.reunion", REUNITED, CLOSED),
    RequiresAnyGroups=[[DEBT, FAVOUR]],
    delay=120, chapters=(5,))

# PP2 (Sol COX, ledger tier B: two Chapter 5 deliveries): when her lair copy cannot be placed, she is carried to Drezen as
# the queen said ("I shall have her carried to the gate") and the reunion is met in person at the jeweller's arcade, or
# under the tailor's awning when the jeweller is gone. The lipstick note is left only for a world where all three anchors
# fail, so the late-referral branch (late_referral, second_opinion) stays at two deliveries when the lair fails.
CITY_REUNION = [
    a("start", REUNION_OPEN + "\n" + "\"But first: I'm starving, and you're the one who prescribed it.\"",
      c("Continue", "hiding", requires=(QUEEN_HIDING,)),
      c("Continue", "price", forbids=(QUEEN_HIDING,))),
    a("hiding", '''"She's hiding, you know. Our Lady. For once nobody's watching me eat." {n}She says it lightly, and her eyes go to the dark under the shutters anyway, as if the dark might be listening. In the Midnight Isles, it usually is.{/n}''',
      c("Continue", "price")),
    a("price", '''"They left me at your gate like a parcel, and I've been sitting in your city all day waiting to be collected. So. The fee for a house call, doctor." {n}She stretches out one bare foot and taps your boot with it.{/n} "Somebody's life, a little of it. Yours or anyone's; I'm not fussy. Choose."''', *REUNION_CHOICES),
    *REUNION_ENDS,
]
CITY_DROPPED = ("babau", "demon")
for _hub, _suffix, _extra, _unit in DREZEN_PLACES:
    _nodes = [nd for nd in copy.deepcopy(CITY_REUNION) if nd["Id"] not in CITY_DROPPED]
    for _node in _nodes:
        _node["Choices"] = [ch for ch in _node["Choices"] if ch.get("Next") not in CITY_DROPPED]
    for _node in _nodes:
        _node["Text"] = _node["Text"].replace(
            "Your soldiers drag it in on a chain: a babau from her own gang, the one that ran when the balor fell, which they dug "
            "out of the rubble alive this morning on your orders. It sees her sitting up on the stones and makes",
            "Your soldiers bring it up from the cells on a chain: a babau from her own gang, the one that ran when the balor fell, "
            "which your people dragged alive out of the lair rubble the day you found her gone from it. It sees her and makes")
        for _ch in _node["Choices"]:
            if _ch["Text"].startswith("[Send a patrol into the rubble for a live one of her gang]"):
                _ch["Text"] = "[Have the babau you dragged out of the lair rubble brought up from the cells] \"One of your boys survived. Eat him.\""
    presence_scene(P + "evil.reunion_city" + _suffix, "The patient sits up", '"You look well, for a corpse."', _nodes,
                   ("trickster.ever", RETURNED, EVIL_DEAD, LAIR_LATCHED, *_extra),
                   (REUNITED, CLOSED, P + "evil.reunion", P + "evil.reunion_letter"), 24, _hub, DREZEN, unit=_unit,
                   RequiresAnyGroups=[[DEBT, FAVOUR]])

TERMS_OPEN = [
    a("terms", '''"I won't wear your colours, and I won't bless anything. I'll come when I'm hungry, and you'll open the door. That's the arrangement. Don't look at me like that. It's the only arrangement I've ever kept."''',
      c("Continue", "debt", requires=(DEBT,)),
      c("Continue", "favour", forbids=(DEBT, FAVOUR_SETTLED)),
      c("Continue", "favour_paid", requires=(FAVOUR_SETTLED,), forbids=(DEBT,))),
    a("favour_paid", '''"And she came for what you owed her, in her own court, and I stood in the doorway and watched you pay it." {n}Her smile is slow.{/n} "I wanted to see what a Trickster looks like when they're the one being collected. Now I know. I've thought about it every night since. It's the best thing I own."''',
      c("Continue", "hungry", requires=(HUNGRY,)),
      c("Continue", "hiding", requires=(QUEEN_HIDING,), forbids=(HUNGRY,)),
      c("Continue", "ask", forbids=(HUNGRY, QUEEN_HIDING))),
    a("debt", '''"And when she calls, I'll go. Don't sulk. You said yes to it. And don't ever try to stop me: lock a door, hire a priest, stand in my way. I'll go through you to get to her, and I won't be gentle, because she won't let me be."''',
      c("Continue", "hungry", requires=(HUNGRY,)),
      c("Continue", "hiding", requires=(QUEEN_HIDING,), forbids=(HUNGRY,)),
      c("Continue", "ask", forbids=(HUNGRY, QUEEN_HIDING))),
    a("favour", '''"And when she comes for what you owe her, I'll be watching. I want to see your face. I want to see what a Trickster looks like when they're the one being collected. And if you try to wriggle out of it, she won't come to you. She'll come to me, and ask me to fetch it."''',
      c("Continue", "hungry", requires=(HUNGRY,)),
      c("Continue", "hiding", requires=(QUEEN_HIDING,), forbids=(HUNGRY,)),
      c("Continue", "ask", forbids=(HUNGRY, QUEEN_HIDING))),
    a("hungry", '''"You sent me away hungry once. I ate a patrol sergeant. Consider that my second opinion."''',
      c("Continue", "hiding", requires=(QUEEN_HIDING,)),
      c("Continue", "ask", forbids=(QUEEN_HIDING,))),
    a("hiding", '''"She's in hiding. She'll come out. Queens always do. Think about that before you lock any door."''',
      c("Continue", "ask")),
    a("ask", '''{n}She slides off the counter, takes the stolen ring off her finger and puts it on yours, and closes your hand over it.{/n} "So. Is the door open, darling, or do I have to steal the key?"''',
      c('[Open the door] "It\'s never locked."', "open", flags=(COMMITTED, OPEN_DOOR)),
      c('[Ask her to stay instead] "Don\'t visit. Stay."', "stay", flags=(ALLY,)),
      c('"No."', "no", flags=(CLOSED, REFUSED))),
    a("open", '''"Good. Leave it unlocked. I hate knocking." {n}She stands, and for a moment, with her back to the moonlight, she is not smiling at all.{/n} "And leave a lamp. I like to see what I'm doing."''', c()),
    a("stay", '''"Stay? Darling, I don't stay. I visit." {n}Her smile does not move, but her voice does.{/n} "Ask me that again and I'll stop visiting."''', c()),
    a("no", '''"Then lock it." {n}She takes her ring back off your finger, slowly, and puts it on her own.{/n} "I'll know."''', c()),
]
drezen_pair(P + "evil.terms", "House calls", '"You\'re sitting on the jeweller\'s counter."', TERMS_OPEN,
            ("trickster.ever", RETURNED, EVIL_DEAD, REUNITED), (CLOSED, COMMITTED, ALLY), 48)


# --- 6. Romance failed: "The crusade's new chaplain" (staging: a public appointment, then her own work) ---------------------

hub(P + "failed.chaplain", "Chaplain", 3,
    '[Announce it to the whole shrine] "Meet the crusade\'s new chaplain. She starts tomorrow."', [
    a("start", '''{n}You chose the hour on purpose: vespers, with the second company kneeling at the rail and every acolyte in the shrine lighting lamps. The words carry further than they should. The shrine has good bones for sound; it was built by people who expected to be heard by a goddess. By vespers the acolytes are calling her "Chaplain" to her face, and the second company is queuing at the altar rail with their swords laid across their palms. Nobody wrote it down. Nobody needed to.{/n}
"Take it back." {n}She has you by the sleeve in the vestry, whispering, furious.{/n} "They'll look at me every day. A succubus, blessing their swords. Do you know what they'll say? Do you know what I was, before, to men who knelt in front of me?"''',
      c("Continue", "sword")),
    a("sword", '''{n}She doesn't leave, though. When the first soldier at the rail clears his throat, she goes out to him. She takes his sword in both hands as if it might burn her, and says the words she has heard the Desnan priests say over travellers, and hands it back. He thanks her. She stands there looking at her own hands.{/n}
"He thanked me," she says, when she comes back. "He didn't know what I am, and he thanked me. Is that what you wanted? Is that the joke?"''',
      c('"Then do it anyway. That\'s the job."', "job", alignment=("Chaotic", 1), flags=(CHAPLAIN, STARTED)),
      c('"It was a joke. I\'ll strike it out."', abort=True)),
    a("job", '''"That's the job." {n}She repeats it the way people repeat a sentence in a foreign language, to see how it sits in the mouth.{/n} "They'll kneel to me, and I'll have to stand there and want nothing from any of them. Every morning." {n}She looks down at the hands that held the sword.{/n} "All right. All right. Tomorrow at sunrise, then. Somebody has to tell me which end of a censer is which."''', c()),
], ("trickster", "trickster.ever", FAILED), forbids=(CHAPLAIN, CLOSED, DEAD, RECRUITED), chapters=(3, 5), Areas=[DREZEN],
    EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="failed")


# --- 7. Commit, redeemed and chaplain worlds (spec §7) ---------------------------------------------------------------

hub(P + "terms", "Both of me", 5, '"You wanted to ask me something."', [
    nar("start", '''{n}She is on the chapel steps after the evening blessing, a blade still across her knees. The soldiers have gone; the lamplighter has not come yet. It is the one hour in Drezen when nobody needs anything from either of you.{/n}''',
        c("Continue", "fed", requires=(AFTERTASTE,), forbids=(ELYSIUM_DONE,)),
        c("Continue", "chaplain", forbids=(AFTERTASTE,)),
        c("Continue", "fed_e", requires=(AFTERTASTE, ELYSIUM_DONE))),
    a("fed_e", '''"I used to count. Days since I last wanted to bite someone." {n}She turns the blade over, looking at her reflection in it.{/n} "Since the Abyss let go of me I keep losing count, because nothing happens to make me start again. A novice cut his hand on the altar rail yesterday, and I bound it, and that was all. That was all, Commander."''',
      c("Continue", "question")),
    a("fed", '''"I've been counting. Days since I last wanted to bite someone. The number keeps going back to zero." {n}She turns the blade over, looking at her reflection in it.{/n} "It went back to zero yesterday. A novice cut his hand on the altar rail, and I had to go and stand in the well-house until it stopped smelling of him."''',
      c("Continue", "question")),
    a("chaplain", '''"The second company calls me Chaplain now. Not one of them asked what I used to be. They bring me their swords and their bad dreams and once, a boy from Nerosyan brought me a letter for his mother because he couldn't write." {n}She wipes the blade clean, although it is already clean.{/n} "I think that's the cruellest thing you've ever done to me. I think it might also be the kindest. I haven't decided."''',
      c("Continue", "question")),
    a("question", '''"So I have a question for you. Only one, and you can't answer it with a joke, because I'll know." {n}She lays the blade down on the step between you.{/n} "Will you still want me when I'm good? Or only when I'm hungry?"''',
      c('"Both. Always both."', "both", flags=(COMMITTED,)),
      c('"Only the good days."', "saint", flags=(SAINT_ONLY, DECLINED), forbids=(ELYSIUM_DONE,)),
      c('[Let her keep her answer for now] "Then I\'ll ask again."', "not_yet", flags=(DECLINED,)),
      c('"Neither."', "neither", flags=(CLOSED, REFUSED)),   # PP2: her own refusal key, read by her Last Call coda (G5)
      c('"Only the good days."', "saint_e", flags=(SAINT_ONLY, DECLINED), requires=(ELYSIUM_DONE,))),
    a("saint_e", '''{n}She lays the blade down very carefully.{/n} "The hunger is gone. My sins aren't. Desna knows every one of them, and so do you." {n}Her voice is gentle and does not move.{/n} "If you can't bear to hear of them, don't kiss me. No."''', c()),
    a("both", '''"Both." {n}She closes her eyes.{/n} "I was afraid you'd say that. I hoped you would."
{n}She reaches for your hand, stops an inch short, and leaves her fingers there, in the air, where you can see them not touching you.{/n} "Both. All right. Both."''', c()),
    a("saint", '''"Only the good days, then." {n}She nods, and something shutters in her face so smoothly you almost miss it.{/n} {n}She picks the blade back up and holds it the way she holds it at the rail, as if it might cut her.{/n} "The hunger is in the good days too. It's in the blessing, and the bread, and in your hand when you pass me the cup. I can't send it into the next room while you visit." {n}Very quietly:{/n} "No. I'm sorry. I am. If you ever find you can bear the rest of me, I'll be on these steps."''', c()),
    a("not_yet", '''"Don't answer yet. You've got the look of someone who's going to be clever, and I can't bear clever tonight." {n}She picks the blade back up.{/n} "Ask me when I've gone a week without wanting to eat anyone. I'll tell you then. I promise I will."''', c()),
    nar("neither", '''{n}She lays the blade down very carefully on the step between you, as if it were the answer and she were giving it back, and goes inside.{/n}''', c()),
], ("trickster.ever",), forbids=(EVIL_DEAD, CLOSED, DECLINED, COMMITTED, RECRUITED), delay=72, chapters=(5,),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]], Areas=[DREZEN])   # the chapel steps

hub(P + "terms_again", "Seven days", 5, '"It\'s been a week."', [
    a("start", '''"Seven days. I counted twice, and then I made Sosiel count, because I didn't trust myself." {n}She doesn't smile.{/n}
"Before I answer, I want one promise from you, and you won't like it. The next time I'm dying, you don't decide for me. No wrist held out like a bowl while I'm too far gone to spit it out, and nobody dragged up from the cells to be eaten. If you want a thread in me for next time, you come and ask for it while I'm alive to bite you for asking, and look me in the eye while you do it."''',
      c('[Promise] "No more doctoring you in your sleep. I swear it."', "yes", flags=(COMMITTED, NO_SECOND_JOKE)),
      c('"I can\'t promise that."', "no", flags=(CLOSED, REFUSED))),
    a("yes", '''{n}She watches you the way she watches strangers in the market, trying to read what they are.{/n} "Then yes. All of it. For as long as what you didn't kill of me lasts." {n}She almost laughs.{/n} "Which is a terrible thing to say to someone you love. I'll work on it."''', c()),
    a("no", '''"Then we're done asking each other things." {n}She says it gently. That is the worst part.{/n}''', c()),
], ("trickster.ever", DECLINED, AFTERTASTE), forbids=(EVIL_DEAD, CLOSED, COMMITTED, RECRUITED), delay=168, chapters=(5,),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]])

# The chaplain never died and was never fed: her week ends on the thing that was done to her, the public appointment.
hub(P + "terms_again_chaplain", "Seven days at the rail", 5, '"It\'s been a week."', [
    a("start", '''"Seven days. I counted twice, and then I made Sosiel count, because I didn't trust myself." {n}She doesn't smile. She is still wearing the stole the second company bought her, and she has not stopped touching its fringe.{/n}
"Before I answer, I want one promise from you, and you won't like it. You made me their chaplain in front of a kneeling company, at vespers, so that I couldn't refuse without shaming every one of them. It worked. I'm keeping it. But it's mine now. They kneel to me now, and I can't bear to disappoint a single one of them, and you knew I wouldn't." {n}Her fingers stop on the fringe.{/n} "Don't ever do that to me again. If you want something of me, ask me where only Desna can hear us, not in front of a kneeling company."''',
      c('[Promise] "No more staging. Your altar, and your door."', "yes", flags=(COMMITTED, NO_STAGING), forbids=(ELYSIUM_DONE,)),
      c('"I can\'t promise that."', "no", flags=(CLOSED, REFUSED)),
      # Sol r4 (CAN): after her release from the Abyss the yes is about the appointment she keeps, not a hunger she fights.
      c('[Promise] "No more staging. Your altar, and your door."', "yes_e", flags=(COMMITTED, NO_STAGING), requires=(ELYSIUM_DONE,))),
    a("yes", '''{n}She watches you the way she watches strangers in the market, trying to read what they are.{/n} "Then yes. All of it. For as long as I can stand at that rail without wanting to bite the hands on it." {n}She almost laughs.{/n} "Which is a terrible thing to say to someone you love. I'll work on it."''', c()),
    a("yes_e", '''{n}She watches you the way she watches strangers in the market, trying to read what they are.{/n} "Then yes. All of it." {n}She smooths the fringe of the stole flat.{/n} "I'm keeping the rail. Not because you put me there; because they still come, and I still want to be the one they come to. And I'm keeping you, because I've looked at every other road and I want this one." {n}She almost laughs.{/n} "The Abyss let go of me, and the first two things I chose were an altar rail and a quack. Desna must be laughing."''', c()),
    a("no", '''"Then we're done asking each other things." {n}She says it gently, and folds the stole over her arm. That is the worst part.{/n}''', c()),
], ("trickster.ever", DECLINED, CHAPLAIN), forbids=(EVIL_DEAD, CLOSED, COMMITTED, AFTERTASTE, RECRUITED), delay=168, chapters=(5,))


# --- The fallen's night: over the roofs of Drezen (heat to the cut; the cut lands at the start of the act) ---------

NIGHT_NODES = [
    a("start", '''"Your window was open. You weren't in it. So I came to find you." {n}She is standing on the jeweller's counter, which puts her head above yours, and she is enjoying that.{/n}
"You left it unlocked for me. Do you know how many doors have been left unlocked for me? Thousands. Do you know how many I walked through twice?"''',
        c("Continue", "up")),
    nar("up", '''{n}She does not wait for an answer. She steps off the counter into your arms, and then her wings open, and the arcade drops away beneath your boots. The roofs of Drezen go past below in the rain: the chapel, the barracks, the long black line of the wall. She puts you down on the wet slates of the old basilica's roof, where the gargoyles lean out over the city, and lands astride the ridge beside you.{/n}
"Look at all those windows. I could choose any of them." {n}Rain runs off her hair.{/n} "Every window in the city, lit or dark. Every sleeper in them. And tonight I've chosen."''',
        c("Continue", "choose")),
    a("choose", '''{n}She takes your face in both hands. Her nails are very long and very clean.{/n}
"This is the part where you remember what I am. Every caress costs. Every one. I'm not going to pretend otherwise, and I'm not going to be careful. If you want careful, you know where the scroll-sellers keep their stalls."''',
        c("Continue", "cured", requires=("trickster.religion_tier1",), forbids=("trickster.religion_tier1",)),   # retired 2026-10-01
        c("[Let her take what she takes.]", "paid")),   # legacy window only: the recruited roof has its own choose (below)
    nar("cured", '''{n}You get the seal open with your thumb and read the ward over yourself in the rain, fast, the ink running, while she watches with her chin on her fist as if you were a street performer she had not decided to pay. Then her mouth finds yours, and the cold comes looking for you and finds the door shut. She pulls back an inch, astonished, furious, laughing.{/n}
"You came to my roof in armour." {n}Her wings open behind her and cut the rain off both of you.{/n} "A death ward. On a date. Oh, you're a coward, and you're clever, and I could eat you for both." {n}Her nails are in your shoulders.{/n} "It won't last, you know. Minutes. I can count too. And when they're gone you're mine to take, and the only thing between you and the bottom of me is how long I can make myself hold my breath. Count for me. Out loud."''',
        c("[Start counting.]", "cut")),
    nar("paid", '''{n}Her mouth finds yours and the cold goes through you like a key turning, and you let it. There is no ward on you tonight. There is only the choice to stay on the roof in the rain and take it. She feels that too, and something in her goes still and sharp and very interested.{/n}
"You're letting me." {n}Her wings open behind her and cut the rain off both of you.{/n} "You know what it costs, and you're still here. You're just letting me."''',
        c("[Let her.]", "cut")),
    nar("cut", '''{n}She pushes you back against the wet slates with one hand flat on your chest, unhurried, the gargoyles leering over her shoulders, and kneels over you with her hair falling round both your faces like a curtain against the rain. Far below, a watchman calls the hour. She reaches back and unhooks the last clasp of her own dress, and lets it go, and the rain runs down her bare skin and onto yours. She tears your shirt open the rest of the way with two fingers, settles her weight astride your hips as if she owned the roof, and bends down until her mouth is against your throat. "Now," she says against it. "Don't you dare lose count." And the city goes.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}You wake in your own bed with the first bell ringing, colder than you went to sleep and warmer than you have any right to be, and with no memory of how you got down off the basilica roof. The window is open. There is a black feather on the pillow, and under it, in lipstick, on a pressed moth wing:{/n}
"Still sweet. Same time next month. Don't lock it. A."''', c(flags=(NIGHT_DONE,))),
]
drezen_pair(P + "evil.window", "The roofs of Drezen", '"You kept the door."', NIGHT_NODES,
            ("trickster.ever", RETURNED, EVIL_DEAD, COMMITTED, OPEN_DOOR), (CLOSED, NIGHT_DONE), 24)


# --- 5b. Fallen and recruited, alive (Ch5, T): the native recruitment (MeetEvilArusha Answer_0009 -> Cue_0014 starts
# EvilArushaRecruited 005c2284) leaves her in the party, never dead, so no device is needed: the fallen courtship plays on
# her own evil companion hub (EvilArueshalaeCompanion_Dialogue AnswersList_0003 7d6ad178, verified in blueprints.zip).
# Voice anchors (enGB, that dialog): Cue_0025 eb9b5dc9 "From now on I worship only one deity. Myself. My desires. My
# pleasures."; Cue_0027 57858226 "Everyone who has tasted my sweetness said it was worth it. Those who could still speak,
# of course."; Cue_0034 8affae04 "What could be more beautiful than power?"
EVIL_HUB = "7d6ad178bd7a1ef4ca737ab167570c79"      # EvilArueshalaeCompanion/AnswersList_0003 (her companion hub)
FALLEN_MET = P + "fallen.house_call"
FALLEN_NIGHT = P + "fallen.roof"
TREATED = "arueshalae.treatment.mealtimes"       # she kept the treatment's daybook before she fell (variant read)


def evil_hub(id, title, entry, nodes, requires=(), forbids=(), delay=0, **extra):
    """A physical scene on her evil companion hub (the recruited, living, fallen Arueshalae is in the party)."""
    SCENES.append(scene(id, title, "Arueshalae", 5, entry, nodes, requires=("trickster", "trickster.ever", RECRUITED, *requires),
                        forbids=(CLOSED, DEAD, EVIL_DEAD, *forbids), delay=delay, last=5, Relationship="arueshalae",
                        AnswerLists=[EVIL_HUB], ContactUnit=EVIL_UNIT, Chapters=[5], **extra))


FALLEN_ASK = [
    a("ask", '''{n}She hooks one finger in your belt and pulls you the last half-step in, close enough that you can feel the cold coming off her skin like the air off a cellar door.{/n} "So. Is your door open tonight, doctor, or do I have to steal the key? I'm very good at keys."''',
      c('[Open the door] "It\'s never locked."', "open", flags=(COMMITTED, OPEN_DOOR, FALLEN_MET)),
      c('"Not tonight."', "later", flags=(FALLEN_MET,)),
      c('"No. Never."', "never", flags=(CLOSED, FALLEN_MET, REFUSED))),
    a("open", '''"Never locked." {n}She lets go of your belt one finger at a time.{/n} "Liar. You lock everything. You'll unlock this one, though, and you'll lie awake listening to it not open, and that will be the best part of my evening." {n}She walks away backwards, smiling.{/n} "Leave a lamp. I like to see what I'm eating."''', c()),
    a("later", '''"Not tonight." {n}She tastes the words and finds them interesting.{/n} "That isn't no. You'd have said no; you love saying no to people. You said 'not tonight', which is a doctor's way of saying 'come back when it's worse'." {n}She turns away.{/n} "It will be worse. I'll come back."''', c()),
    a("never", '''{n}For a moment she says nothing at all, and you see exactly what she looked like on the other side of the Upper City's long table, when a guest had said the wrong thing and did not know it yet.{/n} "Never." {n}Then she smiles, sweetly.{/n} "Then I'll fight your war for the fun of it, and eat your enemies, and never think of you once. You'll hate how little it costs me."''', c()),
]

evil_hub(FALLEN_MET, "House call", '[Take her wrist through her sleeve before she can stop you] "Pale, feverish, homicidal. Let me look at you."', [
    a("start", '''{n}She lets you take it, through the black silk of her sleeve. That is the first surprise. The second is that she laughs, low and delighted, and does not pull away while you count.{/n}
"Oh, look at you. Still playing doctor." {n}She leans in until her mouth is at your ear.{/n} "I'm cured, darling. Not of the hunger. Of the cure. I worship one god now, and she's standing right here, and she's starving."''',
      c("Continue", "candles", requires=(TREATED,)),
      c("Continue", "price", forbids=(TREATED,))),
    a("candles", '''"All that reading in the shrine library at the second bell. All those prices worked out in the margins." {n}She runs one long nail down the inside of your wrist, over the pulse, the way you used to.{/n} "I burned the daybook, you know. In the lair, the night I came back to myself. It went up beautifully. All those little lists of things I wanted that weren't people." {n}She smiles with too many teeth.{/n} "They were all people, doctor. Every one. I was just too frightened to eat them."''',
      c("Continue", "price")),
    a("price", '''"So. Since you insist on making house calls." {n}She sits on the edge of the map table, crosses her legs, and looks at you the way she looks at a crowded street.{/n} "There's a fee. Somebody's life, a little of it. Yours, or anyone's; I'm not fussy. You keep a whole citadel full of people who'd never be missed. Choose."''',
      c('[Hold out your wrist] "Just a taste."', "taste", flags=(FED_ON_YOU,), requires=(FED_ON_YOU,), forbids=(FED_ON_YOU,)),   # retired
      c('[Have the guards bring up a condemned cultist from the cells] "Not me. Him."', "cultist", alignment=("Evil", 2),
        flags=(FED_ON_PRISONER,)),
      c('[Refuse her] "Not a drop."', "refuse", flags=(HUNGRY,)),
      # 2026-10-01 (Sol verify: no unapplied drain): the Commander's own wrist only behind a real ward; her fee is the scroll.
      c('[Spend a Scroll of Death Ward: step out to the chapel, come back warded, and hold out your wrist] "Just a taste. If you can find one."',
        "taste_warded", requires=(WARD_HELD,), remove_item=SCROLL, flags=(WARD_FEE,))),
    a("taste_warded", '''{n}She smells the chaplain's ink on you before you are through the door. She takes your wrist anyway, slowly, the way she would take a cup she had been promised, and puts her mouth to the inside of it, and drinks, and nothing comes. You watch her find the ward the way a thief finds a bolted shutter: with her whole body, and then with her temper.{/n}
"You came to my fee in armour." {n}She lets go of you one finger at a time, and she is laughing, and her eyes are not.{/n} "Then that's the fee, darling. Every time I come to your door, you burn one of those for nothing, and I take nothing, and we both know exactly what it cost you. I'll find my dinner elsewhere. You'll pay for the privilege of not being it."''',
      c("Continue", "terms")),
    nar("taste", '''{n}She takes her time. She holds your wrist as if it were a cup she had been looking forward to all day, and the cold goes into you in long, unhurried swallows, and she watches your face over it to see when you start to sway. You start to sway. She lets go exactly then, not a breath later, and licks her lip.{/n}
"Still sweet. Everyone who's tasted me says it was worth it. Nobody's ever said it about the other way round." {n}She steadies you with one hand on your chest, a little too long.{/n} "Sit down before you fall down. Don't be embarrassed."''',
      c("Continue", "terms")),
    a("cultist", '''{n}They bring him up gagged, a Deskari lay preacher with the brand of the assize still raw on his cheek. She looks at him, and then at you, and her smile goes very flat and very pleased.{/n}
"You do know I can tell the difference, darling? Between a gift and leftovers?" {n}She takes him by the jaw.{/n} "No matter. Leftovers are still dinner." {n}She does not ask you to leave. She wants you to watch, so you do, and when it is finished there is a man on the floor breathing who will never be anyone again.{/n}''',
      c("Continue", "terms")),
    a("refuse", '''"No?" {n}She tilts her head, interested rather than hurt.{/n} "Then I'll find someone who says yes. There's always someone who says yes. A sergeant at the back of Fye's, for instance. Red beard, kind when he's drunk." {n}She slides off the table.{/n} "I've had my eye on him for months. He'll never know what he paid for your 'no'. You will."''',
      c("Continue", "terms")),
    a("terms", '''"Now. Terms, since you like them." {n}She counts on her fingers, the way she used to count days.{/n} "I fight for you because killing demons is fun and you're winning. Don't confuse that with love. I won't wear your colours, I won't bless anything, and I won't sit and wait while you read your little scrolls. I'll come to your bed when I'm hungry, and you'll open the door, and you'll pay what it costs, and you won't ask me to be sorry."''',
      c("Continue", "ask")),
    *FALLEN_ASK,
], forbids=(FALLEN_MET, COMMITTED), EntryMythic="PlayerIsTrickster")

evil_hub(P + "fallen.lock", "The lock", '"You\'ve been at my door."', [
    a("start", '''"Every night since you said 'not tonight'." {n}She does not even pretend otherwise. She holds up a thin hooked wire, the kind a Kenabres housebreaker carries in his collar.{/n} "I could have opened it the first night. I didn't. I stood outside and listened to you not sleeping, and it was delicious, and I wanted to see how long you'd last." {n}She tucks the wire away.{/n} "Longer than most. Not as long as you think."''',
      c("Continue", "ask")),
    *[dict(nd) for nd in FALLEN_ASK],
], requires=(FALLEN_MET,), forbids=(COMMITTED, P + "fallen.lock"), delay=72)

# A second 'not tonight' leaves the lock replayable: her promise to come back keeps a reachable yes.
for _node in SCENES[-1]["Nodes"]:
    if _node["Id"] == "later":
        for _choice in _node["Choices"]:
            _choice["Abort"] = True

FALLEN_WARDED = P + "fallen.warded"     # the recruited roof night: the ward read at the chapel before she flies him up
FALLEN_NIGHT_NODES = [
    a("start", '''"Your door was open. You weren't behind it. So I came to find you." {n}She is sitting on the sill of the war-room window with one knee drawn up and the rain at her back, as if she had always been there.{/n}
"Do you know how many doors have been left unlocked for me? Thousands. Do you know how many I walked through twice?"''',
      c('[Spend a Scroll of Death Ward: "Wait." Go down to the chapel, have the ward read over you, and come back up]', "warded_up",
        requires=(WARD_HELD,), remove_item=SCROLL, flags=(FALLEN_WARDED,)),
      c('[You have no ward on you] "Not tonight."', "no_ward", forbids=(WARD_HELD,))),
    a("warded_up", '''{n}She waits. She does not wait for anyone, and she waits for you, on the sill in the rain, and when you come back up the stair with the ward cold on your skin she breathes in as you come close, and smiles with too many teeth.{/n}
"Chaplain's ink. You went to a priest before you came to me." {n}She sounds delighted.{/n} "Seven minutes of armour. I can count too."''',
      c("Continue", "up")),
    a("no_ward", '''{n}She looks you over, and you watch her see that there is no ink on you, and decide what to do about it.{/n}
"No armour, and you still left the door open." {n}She swings her legs back out over the rain.{/n} "Tempting. Too tempting; I'd enjoy it too much, and then you'd be no use to me at all. Buy one. I'll be back. I'm always back."''',
      c("[Let her go.]", abort=True)),
    nar("up", '''{n}She does not wait for an answer. She takes you round the waist, steps backwards off the sill, and her wings open before you have time to shout. The roofs of Drezen go past below in the rain: the chapel, the barracks, the long black line of the wall. She puts you down on the wet slates of the old basilica's roof, where the gargoyles lean out over the city, and lands astride the ridge beside you.{/n}
"Look at all those windows. I could choose any of them." {n}Rain runs off her hair.{/n} "Every window in the city, lit or dark. Every sleeper in them. And tonight I've chosen."''',
      c("Continue", "choose")),
    a("choose", '''{n}She takes your face in both hands. Her nails are very long and very clean, and she does not hurry, because she does not need to: the ward is on you, and she has decided to enjoy finding out exactly where it ends.{/n}
"This is the part where you remember what I am. Every caress costs. Every one. You've paid a priest to make tonight's free, and I'm going to make you feel every minute of it running out."''',
      c("Continue", "cured", requires=("trickster.religion_tier1",), forbids=("trickster.religion_tier1",)),   # retired 2026-10-01
      c("[Let her take what she takes.]", "paid", requires=(FALLEN_WARDED,), forbids=(FALLEN_WARDED,)),   # retired: no unwarded night
      c("[Let her find where it ends.]", "cured", requires=(FALLEN_WARDED,))),
    nar("cured", '''{n}Her mouth finds yours, and the cold comes looking for you and finds the door shut. She pulls back an inch, astonished, furious, laughing.{/n}
"A coward, and clever, and I could eat you for both." {n}Her wings open behind her and cut the rain off both of you.{/n} "When it's gone you're mine to take, and the only thing between you and the bottom of me is how long I can make myself hold my breath." {n}Her nails are in your shoulders.{/n} "Count for me. Out loud."''',
      c("[Start counting.]", "cut")),
    nar("paid", RETIRED_TEXT, c("[Let her.]", "cut")),
    *[dict(nd) for nd in NIGHT_NODES if nd["Id"] == "cut"],
    nar("after", '''{n}You wake in your own bed with the first bell ringing, warmer than you have any right to be, and with no memory of how you got down off the basilica roof. The window is open. There is a black feather on the pillow.{/n}
{n}At the muster she is already in her place among your companions, sharpening nothing in particular. She wishes everyone good morning but you. When you pass her, she says, without looking up:{/n} "Seven. I counted. I let go at seven." {n}She tests the edge with her thumb.{/n} "Next time I might not." {n}The whole column hears it.{/n}''',
      c(flags=(NIGHT_DONE,))),
]
evil_hub(FALLEN_NIGHT, "The roofs of Drezen", '"You kept the door."', FALLEN_NIGHT_NODES,
         requires=(COMMITTED, OPEN_DOOR, FALLEN_MET), forbids=(NIGHT_DONE,), delay=24, Areas=[DREZEN])


# --- 8. Epilogue pages (ArueshalaeEpilogue; no system effects) -------------------------------------------------------

EP = dict(last=6, Relationship="arueshalae")
SCENES.append(scene(P + "epilogue.commit", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Arueshalae answered the Commander's question, so she answered it afterwards.{/n}''',
        paragraphs=(
            p('''{n}She answered it on the chapel steps in Drezen, with a blade across her knees and the second company's swords stacked in the vestry behind her: all of her, the hunger and the prayer in one knot, for as long as she could hold it. She held it. Nobody who knew her was surprised, except her.{/n}''',
              forbids=(EVIL_DEAD,)),
            p('''{n}The Commander's voice took the best part of a year to come back from the chapel, and the white scar on the wrist never went at all. She never asked whether it had been worth it.{/n}''',
              requires=(GIFT_TORN,)),
            p('''{n}She came through the Commander's window the first night after Threshold, sat on the sill with one knee drawn up, and said she had decided to keep visiting. It was the closest thing to a vow she ever made, and she kept it.{/n}''',
              requires=(EVIL_DEAD,)),
        ))],
    requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED, ALLY, RECRUITED),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN, REUNITED]], **EP))
SCENES.append(scene(P + "epilogue.kept", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}After the Worldwound was closed, Arueshalae stayed in Drezen, because the Commander was there, and because she had decided to.{/n}''',
        paragraphs=(
            p('''{n}She kept the stole the second company had bought her and the altar rail they knelt at, and she blessed their swords for years after there was nothing left to use them on, because they kept asking.{/n}''',
              requires=(CHAPLAIN,)),
            p('''{n}She kept her count of days in a soldier's tally book, and every morning she found the Commander's pulse first, before her own coffee, to be sure of what she had been given back.{/n}''',
              requires=(AFTERTASTE,)),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, RECRUITED, EVIL_DEAD, "arueshalae.treatment.intake"),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]], **EP))
SCENES.append(scene(P + "epilogue.kept_fallen", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}After the Worldwound was closed, Arueshalae kept visiting. The Commander's window was never locked, and the city learned to count its sergeants after she had passed through a street. She never pretended to be anything but what she was, and the Commander never asked her to.{/n}''')],
    requires=("trickster.ever", COMMITTED, EVIL_DEAD, REUNITED), forbids=(CLOSED, RECRUITED), **EP))
SCENES.append(scene(P + "epilogue.declined", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}Arueshalae never finished counting her week, and when anyone asked her about the Commander she said she was still deciding.{/n}''',
        paragraphs=(
            p('''{n}She served as the crusade's chaplain until the end, and blessed the swords of the second company and the lamps of the field hospital.{/n}''',
              requires=(CHAPLAIN,)),
            p('''{n}She stayed with the crusade until the end, kept her count in a daybook, and never once let anyone hand her a knife at supper.{/n}''',
              forbids=(CHAPLAIN,)),
        ))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, RECRUITED), RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]], **EP))
SCENES.append(scene(P + "epilogue.fallen", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}Arueshalae fought the rest of the war at the Commander's side, for the fun of it, and never once pretended otherwise. She ate what the Commander gave her and a good deal that the Commander did not, and the crusade learned to count its sergeants after she had passed through a town.{/n}''',
        paragraphs=(
            p('''{n}The Commander's door was never locked. Some nights she came through it hungry and left before the first bell, and the Commander was grey at the morning council and would not say why. She never apologised for one of them, and she never once took more than she had decided to.{/n}''',
              requires=(FED_ON_YOU,)),
            p('''{n}The Commander's door was never locked, and the Commander never once met her at it without the chaplain's ink still drying. She made a game of it: every visit cost a scroll, and she drank nothing, and she called it the dearest kiss in Drezen. She ate elsewhere. The Commander knew where, and paid that bill too, in sergeants.{/n}''',
              requires=(WARD_FEE,)),
            p('''{n}The cells under the citadel emptied faster than the assizes could fill them. Nobody wrote down where the condemned went. Everybody knew.{/n}''',
              requires=(FED_ON_PRISONER,)),
            p('''{n}A red-bearded sergeant of the third company went to sleep at the back of Fye's one night and did not wake. She told the Commander about it herself, at breakfast, as if reporting the weather.{/n}''',
              requires=(HUNGRY,)),
        ))],
    requires=("trickster.ever", COMMITTED, RECRUITED, OPEN_DOOR), forbids=(CLOSED, EVIL_DEAD), **EP))
SCENES.append(scene(P + "epilogue.ally", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}She kept visiting. She never once stayed the night, and she never once missed a month. The Commander's window was never locked again, and the Commander's household learned not to mention the black feathers.{/n}''')],
    requires=("trickster.ever", ALLY), forbids=(COMMITTED, CLOSED), **EP))


# --- 10. Companion lines (ledger 05 §3.1: exactly Sosiel and Lann), each behind its reactor's guard ----------------

SOSIEL = dict(answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"))
LANN = dict(answer_list=LANN_HUB, forbids=("lann.dead", "lann.kicked_out"))
SCENES.extend([
    reaction("Sosiel", P + "react.sosiel_fed", (RETURNED, FED_ON_YOU),
             '''"She fed on you." {n}Sosiel says it quietly, so that nobody at the next fire hears.{/n} "She won't forgive herself for it, so I'll say it for her: thank you. And if she needs it again, come to me first. I would rather it were mine. Shelyn knows I have more of it to spare than you do."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Lann", P + "react.lann_prisoner", (RETURNED, FED_ON_PRISONER),
             '''"The east cells are one short and nobody's asking." {n}Lann doesn't look up from his fletching.{/n} "You fed her a man so she'd live. I think I'd have done the same. I'm not proud of thinking it. Don't ask me to be."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **LANN),
    reaction("Lann", P + "react.lann_deal", (RETURNED, EVIL_DEAD, "arueshalae.lann_refused_queen"),
             '''"The queen offered me anything I wanted, and I told her I'd rather die than wear a debt." {n}He finally looks at you.{/n} "You went and took one out for a succubus who tried to eat you. That's either very noble or very stupid. I'm going with stupid. Mostly."''',
             chapter=5, last=5, entry='"About Arueshalae..."', **LANN),
    reaction("Sosiel", P + "react.sosiel_evil", (RETURNED, EVIL_DEAD),
             '''"I prayed for her the night she died at the lair." {n}Sosiel turns his cup in his hands.{/n} "I'm not sorry she's back. I'm afraid of what you promised to bring her, and I'll pray about that too. Every night, if you'll let me. Even if you won't."''',
             chapter=5, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Sosiel", P + "react.sosiel_chaplain", (CHAPLAIN, P + "chaplain.the_dying"),   # Sol r3 INT: after the vigil it recalls
             '''"I've been helping her with the sermons." {n}Sosiel smiles, which is not something he does lightly about sermons.{/n} "She stayed with a dying pikeman until the lamps burned low, last night. I would have been glad of her at my own bedside."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Sosiel", P + "react.sosiel_gift", (RETURNED, GIFT_TORN),
             '''"Your voice." {n}Sosiel says it before you have finished your first sentence, and puts his cup down.{/n} "It's gone thin, like a man's after a fever. She told me what she gave you, and what came back down it." {n}He looks at your wrist, and then, carefully, not at it.{/n} "It comes back with time, they say, slowly. The scar won't. I'd have warned you, if you'd asked me first. I think you knew that. I think that's why you didn't ask."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Lann", P + "react.lann_chaplain", (CHAPLAIN,),
             '''"She blessed my bow this morning. It didn't catch fire." {n}Lann holds it up as evidence.{/n} "I checked twice. Then I went back and asked her to do the arrows. Don't tell her I said so."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **LANN),
])


# Q11: after the native Elysium ending her touch no longer drains: the drinking return, the gift, and the hunger that follows
# a return are not restaged (native resurrection remains); the terms read her changed state.
for _scene in SCENES:
    if _scene["Id"] in (P + "dead.starving", P + "insurance", P + "returned.aftertaste") and ELYSIUM_DONE not in _scene["Forbids"]:
        _scene["Forbids"].append(ELYSIUM_DONE)


# Device redesign (2026-10-01, coordinator rulings): nothing in this route returns her from death. The Ledger says so
# truthfully while she lies dead and unraised (the native Raise Dead clears arueshalae_dead, and the entry with it), and
# records the lair kill, which closes her route by the Commander's own choice.
from storylines import lastcall_ledger as _ledger
_ledger.EXTRA_ENTRIES.append(dict(
    Id="lost.arueshalae", Section="Debts", Portrait="Arueshalae", Title="Arueshalae: the crusade's rites",
    Text=("{n}Arueshalae died in my service. The crusade's rites can call her back: a chaplain on his knees, a raising "
          "prayer, a scroll from the reliquary. I have no trick that can. Every touch I ever bought her cost a scroll and was over in minutes, and "
          "none of them was for this.{/n}"),
    Lines=[], Requires=["trickster.ever", DEAD], Forbids=[RETURNED], AnyGroups=[], Tooltip="RRT_Debt"))
_ledger.EXTRA_ENTRIES.append(dict(
    Id="lost.arueshalae_lair", Section="Debts", Portrait="Arueshalae", Title="Arueshalae: the lair",
    Text=("{n}I found her at her lair with her gang around her, and she laughed at me, and I could have held out my hand. I "
          "drew instead. She died on the rubble of her own house, and nobody is coming back from that one. I chose it. I "
          "write it down so that I remember I chose it.{/n}"),
    Lines=[], Requires=["trickster.ever", EVIL_DEAD], Forbids=[RETURNED], AnyGroups=[], Tooltip="RRT_Debt"))


def integrate(payload):
    """Register her revival, presences and derived keys. Scenes are added by expansion.py; world keys bind on demand."""
    payload.setdefault("Revivals", {}).update({k: dict(v) for k, v in REVIVALS.items()})
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    # Device redesign (2026-10-01): the Scroll of Death Ward is the only removable item of this route, read through
    # arueshalae.ward_held; and the retired device scenes are gated off (ids, nodes and choice indices kept).
    if payload.setdefault("InventoryItems", {}).get(WARD_HELD, SCROLL) != SCROLL:
        raise ValueError("Conflicting binding: " + WARD_HELD)
    payload["InventoryItems"][WARD_HELD] = SCROLL
    removable = payload.setdefault("RemovableItems", [])
    if SCROLL not in removable:
        removable.append(SCROLL)
    # Retirement gate (Targona precedent): the runtime holds chapter_later in every chapter >= 2, and every retired scene
    # opens in Chapter 3 or later, so a Forbid on it never lets them open again (their ids, nodes and indices stay).
    for scene_ in payload["Scenes"]:
        if scene_["Id"] in RETIRED and "chapter_later" not in scene_["Forbids"]:
            assert scene_["MinChapter"] >= 2, scene_["Id"]
            scene_["Forbids"].append("chapter_later")
    # PP2 (Sol r1, CAN cap): the tailor's-awning copies (_yard) are met where the jeweller is gone; stage them there.
    # (Sol r1, INT) the Sosiel conversation needs his offer to have been made and him alive and in the crusade; the
    # committed endings honour the binding sacrifice guard (as treatment.epilogue.together does).
    for scene_ in payload["Scenes"]:
        if scene_.get("Relationship") != "arueshalae":
            continue
        if scene_["Id"].endswith("_yard"):
            scene_["Entry"] = scene_["Entry"].replace("the jeweller's counter", "the tailor's cutting table")
            for node in scene_["Nodes"]:
                for old, new in YARD_STAGING:
                    node["Text"] = node["Text"].replace(old, new)
        if scene_["Id"] == P + "returned.sosiel":
            scene_["Requires"] = list(dict.fromkeys(scene_["Requires"] + [P + "react.sosiel_fed"]))
            scene_["Forbids"] = list(dict.fromkeys(scene_["Forbids"] + ["sosiel.dead", "sosiel.kicked_out"]))
        if scene_["Id"] in SACRIFICE_GUARDED and "sacrifice" not in scene_["Forbids"]:
            scene_["Forbids"].append("sacrifice")
            scene_.setdefault("ForbidOverrides", {})["sacrifice"] = "trickster.commander_back"
    latches = payload.setdefault("Latches", {})
    for key, sources in LATCHES.items():
        if latches.get(key, sources) != sources:
            raise ValueError("Conflicting latch: " + key)
        latches[key] = list(sources)
    # Nocticula_main/Cue_0521: Lann refuses the queen's offer (the reaction quotes it only where it was shown)
    payload.setdefault("SeenCues", {})["arueshalae.lann_refused_queen"] = ["00f8570585529f54ba41157ac66574f4"]
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
