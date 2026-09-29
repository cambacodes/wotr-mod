"""Arueshalae on the Trickster path: "Treatment" (Writer/handoffs/trickster/arueshalae.md; family F18, the sneaky quack).

A new native adapter. It reads ArueshalaeRomance d6a90c0f and never starts or completes it; her native romance stands on
every path. The Trickster layer answers her three losses with the quack's diagnosis:
- dead in the party: "You're not dead. You're starving. Eat." (Revivals; she feeds, and what she ate is paid for);
- evil, killed at the lair (Ch5): a referral for a second opinion to the only physician a succubus has, her queen, who
  bills for the consultation (Nocticula_main/Cue_0520, Cue_0523). The queen's terms are evil terms: pay them, shift them
  onto yourself, or refuse, and each has a cost that stays;
- romance failed: the crusade's new chaplain, appointed out loud at the shrine at the hour the second company kneels:
  a piece of staging that she then has to live up to with her own hands.
The living courtship on her own hub is arueshalae_treatment and arueshalae_rounds; the other paths' middle beats are
arueshalae_chapel, arueshalae_hours and arueshalae_notes.

Canon (blueprints.zip / enGB): her hunger, Arueshalae_Jailed/Cue_0026 5942af3e ("I devoured, degraded, and drained their
souls dry... this unholy hunger inside me"); "Everything demons do is a sort of cannibalism. Each devours mortals and
other demons in their own way" (hub Cue_0105 07b4c786); "Any caress, of any kind, sucks the life from mortals" (hub
Cue_0083 0cb8bb69). The quack's power is the Trickster's own Lore (Religion) rank 1, TricksterLoreReligionTier1Feature
04177c4d: "Your treat affliction ability removes... any negative conditions affecting the target" (a chosen trick, read
as MainCharacterFacts trickster.religion_tier1).

Placement (06-ROUTE-REGISTRY §3): the evil Arueshalae's Drezen beats are at the jeweller's arcade after dark, beside the
capital jeweller (JewelerCapitalTrader bc109323, unused by any other route), with the tailor's awning (TailorCapitalTrader
253cdb8f) as the fallback copy. The crowded anchors (Fye, Wilcer Garms, the smith) are left alone.
"""
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
LATE = P + "cost.late"
DEBT = P + "cost.nocticula_debt"
FAVOUR = P + "cost.nocticula_favour"
UNANSWERED = P + "cost.unanswered"
HUNGRY = P + "cost.sent_away_hungry"
OPEN_DOOR = P + "cost.open_door"
NO_SECOND_JOKE = P + "cost.no_second_joke"
SAINT_ONLY = P + "cost.saint_only"
EVERY_TIME = P + "said_every_time"
IF_ASKED = P + "said_if_asked"
LATE_COMMITTED = P + "late_committed"
IN_HIDING = "noct.defeated_not_dead"          # text-read only (ledger 2): never a scene or choice gate
FOOLED = "noct.fooled"                        # text-read only
DEAD_LATCH = "arueshalae_dead.latched"
EVIL_LATCH = "arueshalae.evil_dead.latched"
LAIR_PRESENCE = "arueshalae.presence.evil"
TAVERN_PRESENCE = "arueshalae.presence.evil_drezen"   # the jeweller's arcade after dark
YARD_PRESENCE = "arueshalae.presence.evil_awning"     # the tailor's awning (fallback)
LAIR_FAILED = LAIR_PRESENCE + ".failed"        # runtime: her lair copy is wanted but the locator did not resolve
TAVERN_FAILED = TAVERN_PRESENCE + ".failed"    # runtime: the jeweller's unit is not in the capital
NIGHT_DONE = P + "evil.dawn"
# The arcade and its fallback use two different bodies (presences sharing a unit and area must exclude each other).
DREZEN_PLACES = ((TAVERN_PRESENCE, "", (), EVIL_UNIT), (YARD_PRESENCE, "_yard", (TAVERN_FAILED,), EVIL_NPC))

RELATIONSHIP = dict(
    Title="Treatment",
    Description=("Arueshalae is hungry. She has always been hungry. I have read the Desnan rites and the Trickster's own "
                 "lore, and I have decided to treat it as a medical condition, one night at a time."),
    Objective="Speak with Arueshalae",
    Guidance=("On the Trickster path, take Arueshalae's pulse at her own hub in Chapter 3 and begin her treatment; "
              "the sessions continue in Chapters 3 to 5. If she dies in the party, falls to evil and is killed at her "
              "lair, or her romance fails, the Trickster has an answer for each. Her native romance stands beside all "
              "of it."),
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
                        Requires=["trickster.ever", RETURNED, EVIL_DEAD], Forbids=[CLOSED, REUNITED],
                        MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREET_LAIR),
    TAVERN_PRESENCE: dict(Unit=EVIL_UNIT, Area=DREZEN, Mode="spawn-copy",
                          At=dict(NearUnit=JEWELER, Side="front", Distance=2.0),
                          Requires=["trickster.ever", RETURNED, REUNITED, EVIL_DEAD], Forbids=[CLOSED, ALLY, NIGHT_DONE],
                          MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub", Greeting=GREET_ARCADE),
    YARD_PRESENCE: dict(Unit=EVIL_NPC, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TAILOR, Side="front", Distance=2.0),
                        Requires=["trickster.ever", RETURNED, REUNITED, EVIL_DEAD, TAVERN_FAILED],
                        Forbids=[CLOSED, ALLY, NIGHT_DONE], MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub",
                        Greeting=GREET_AWNING),
}

DERIVED = {
    LATE_COMMITTED: [["trickster.ever", AFTERTASTE], ["trickster.ever", CHAPLAIN], ["trickster.ever", REUNITED]],
    # node-read only (ledger 2): the bill owed to a queen in hiding
    UNANSWERED: [[DEBT, IN_HIDING], [FAVOUR, IN_HIDING]],
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


# --- 4. Dead in party: "Starving, not dead" (Revivals; remote: a dead retained companion has no clickable unit) ------

letter(P + "dead.starving", "Diagnosis", 3, [
    nar("start", '''{n}They have laid Arueshalae out in the chapel with her wings folded. The chaplains washed her face and did not know what to do with the rest of her, so they left her in her travelling clothes, with a sprig of something green between her hands.{/n}
{n}Without the careful stillness she wore in life, she looks younger. And hungrier. The hollows under her cheekbones are deeper than they were at the last camp. You have seen that look on the faces of the Kenabres refugees queuing at the soup kettles.{/n}
{n}She died of her wounds. But you know the other thing, the one that will be waiting for her if she ever opens her eyes again: a hunger held on a short chain for so long that it has worn her to the bone, and that will have her by the throat before she has finished her first breath.{/n}''',
        c('[Treat her like a patient] "You\'re not dead. You\'re starving. Eat."', "treat", mythic="Trickster",
          requires=("trickster.religion_tier1",)),
        c("[Let her rest.]", abort=True),
        c('[Treat her like a patient] "You\'re not dead. You\'re starving. Eat."', "wake", mythic="Trickster",
          forbids=("trickster.religion_tier1",))),
    nar("treat", '''{n}The chaplain on duty has already said it plainly, with the tiredness of a man who has said it before. The raising rites call a soul home to its body. She is an outsider, Abyss to the bone, and when her kind die there is no home to call; the rite has nothing to hold on to. It is not a question of diamonds. It is a question of there being nothing there.{/n}
{n}You read one sentence differently from him. Your lore heals the soul as well as the body: your treatment removes any negative condition affecting the one you treat. Any. The words do not say "short of death". They do not say "except demons". You have been waiting for the rule to notice the door it left open, and it has not noticed yet.{/n}
{n}Death is a negative condition. It is affecting her. You put your palm flat on her breastbone and treat it the way you would treat a fever: you name it, and you lift it.{/n}
{n}It is heavier than any poison you have ever lifted, and colder, and for a long moment the rule seems to notice after all; the lore drags at the whole of you, as if it means to take its fee in kind. Then something under your palm goes from stone to skin. The sprig slides out of her hands.{/n}
{n}You lifted her death. You did not lift her hunger, because the hunger is not a condition; it is what she is. She wakes with it, exactly as starved as she died, and her eyes find your throat before they find your face. You cut your wrist on the edge of the bier and put it in her way, and her body drinks before she can stop it: three swallows, four, before she tears her mouth off you with a sound like cloth ripping.{/n}''',
        c("Continue", "claimed", requires=(CLAIMED,)),
        c("Continue", "plea", forbids=(CLAIMED,))),
    nar("wake", '''{n}The chaplain on duty has already said it plainly: the raising rites call a soul home to its body, and she is an outsider, Abyss to the bone. For her kind the rite has nothing to hold on to.{/n}
{n}You know the reading a Trickster with the right lore would make: call death one more negative condition, and lift it. You have not got that lore. You make the same diagnosis anyway, by main force, with what any field healer has: the chaplain's commentary open on the bier, every litany against wasting and fever you can drag out of memory, a candle, your hands on her, and the one remedy her body has always answered to, which is to be fed. You will have to name the thing exactly, verse by verse, and keep your wrist at her lips for as long as it takes. It may not be enough. It may cost more blood than you have.{/n}''',
        c('[Work the litanies over her, and cut your wrist on the edge of the bier]',
          check={"Skill": "SkillLoreReligion", "DC": 22, "Success": "rite_holds", "Failure": "rite_fails"})),
    nar("rite_holds", '''{n}You keep the thread: wasting named, fever named, the hunger named last and longest. By the end the words are only yours, and the room has gone grey at the edges. You hold your wrist to her lips and keep it there while the chaplain protests, and her body, which was built to drink before its owner can stop it, drinks. Something under your hand goes from stone to skin. The sprig slides out of her hands.{/n}
{n}Her eyes open. They find your throat before they find your face.{/n}''',
        c("Continue", "claimed", requires=(CLAIMED,)),
        c("Continue", "plea", forbids=(CLAIMED,))),
    nar("rite_fails", '''{n}You lose the thread on the third litany. The candle gutters and goes out, and the blood on her lips is only blood. The chaplain lays a hand on your arm and says, not unkindly, that the body will keep until tomorrow, and that you should bandage that.{/n}''',
        c("[Bandage the wrist. Try again tomorrow.]", abort=True)),
    a("claimed", '''{n}Very quietly, as if there were someone else in the chapel:{/n} "Our Lady in Shadow will have felt that. She counts us, you know. Like coins in a purse. One of hers just rolled back out from under the table."''',
        c("Continue", "plea")),
    a("plea", '''"No. No, I swore. Every day, I swore. I kept count, Commander, every day since the Tender of Dreams sent me back, I kept..." {n}Her voice cracks on the count. She is shaking, and her fingers have closed on the edge of the bier hard enough to splinter it.{/n}
"Don't you dare make me. Don't you dare make me want it and then call it medicine."''',
        c('[Keep your wrist where it is] "Doctor\'s orders."', revive="arueshalae",
          flags=(RETURNED, FED_ON_YOU, STARTED)),
        c('[Take your wrist back, and have the guards drag a condemned cultist to her] "Not me. Him."', revive="arueshalae",
          alignment=("Evil", 2), flags=(RETURNED, FED_ON_PRISONER, STARTED)),
        c("[Let her keep her vow.]", "vow", flags=(DECLINED,))),
    nar("vow", '''{n}You take your wrist away. You put the sprig back between her hands and fold her fingers over it. The chaplain on duty looks at you, and then away, and says a prayer to Desna that he clearly had not expected to say over a demon.{/n}
{n}She keeps her vow. It is the last thing that was entirely hers.{/n}''', c()),
], requires=("trickster", "trickster.ever", DEAD, DEAD_LATCH),
    forbids=(RETURNED, DECLINED, EVIL_DEAD, CLOSED, "arueshalae.kicked_out", "arueshalae.kicked_out_evil"), delay=24,
    chapters=(3, 5), Recovery="arueshalae",
    TricksterDevice=True, TricksterState="dead")

hub(P + "returned.aftertaste", "Aftertaste", 3, '"How do you feel?"', [
    a("start", '''{n}She will not quite meet your eyes. She has taken to standing where she can see the door, and to keeping her hands behind her back.{/n}
"I can still taste it. Every time I close my eyes. I thought the worst thing would be the wanting. It isn't. It's that I'm not hungry any more, and I can feel how good that is, and I know exactly what it cost."''',
      c("Continue", "you", requires=(FED_ON_YOU,)),
      c("Continue", "him", forbids=(FED_ON_YOU,))),
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


# --- 5. Evil, killed at the lair: "A second opinion" (Ch5; Directive 9) -------------------------------------------

SCENES.append(scene(P + "evil.diagnosis", "Bedside manner", "Arueshalae", 5,
    '[Take her pulse from across the room] "Pale, feverish, homicidal. Classic case. I\'m referring you for a second opinion."', [
    a("start", '''{n}Arueshalae stares at you. The balor behind her stares at you. Then she throws back her head and laughs, delighted, the way she used to laugh at the mess-tent jokes she pretended not to understand.{/n}
"A referral? To whom, darling? There's only one physician for my kind, and she doesn't make house calls." {n}She licks her lip, slowly.{/n} "Oh, you're adorable. You always were. Boys, the doctor is in."''',
      c("[Brace yourself.]", native_next=TASTE_CUE, flags=(PRIMED,))),
], requires=("trickster",), forbids=(PRIMED, EVIL_DEAD, RECRUITED), last=5, Relationship="arueshalae", Chapters=[5],
    AnswerLists=[MEET_EVIL_LIST], NativeReturnCue=GANG_CUE, EntryMythic="PlayerIsTrickster",
    TricksterDevice=True, TricksterState="evil_dead"))

letter(P + "evil.late_referral", "A referral, posthumously", 5, [
    nar("start", '''{n}Her body lies where it fell, wings spread over the bones of her boys. It has not rotted, and nothing in the lair has touched it. The rubble around her is thick with scavengers, and every one of them gives her a wide berth, as if something far away had already laid a claim to her.{/n}
{n}In the rubble a vrock with a broken beak is picking through the dead for rings. It owes you its life from the fight; you let it crawl away. You catch it by the scruff of its feathered neck.{/n}''',
        c('[Give the vrock the referral, word for word] "Say this to your queen: patient, one succubus, deceased, misdiagnosed. Requesting a second opinion. Now say it back to me."',
          "sent", mythic="Trickster", flags=(PRIMED, LATE)),
        c("[Let it go without a message.]", "gone", flags=(DECLINED,))),
    nar("sent", '''{n}It says it back to you three times, in a voice like a hinge, until it has every word. Then it goes, flapping badly into the purple sky, and looks back once as if to ask whether you are serious. You are. It is the most serious referral you have ever written.{/n}''', c()),
    nar("gone", '''{n}You let it go. It scuttles off into the rubble with its rings. You leave her where she fell. It is the only thing about her that you never tried to fix.{/n}''', c()),
], requires=("trickster", EVIL_DEAD, EVIL_LATCH), forbids=(PRIMED, RETURNED, DECLINED), delay=24, chapters=(5,),
    TricksterDevice=True, TricksterState="evil_dead")

QUEEN_FEE = ('"My fee: once, when I call, she comes. You will not know when, and you will not stop her. Do not haggle. '
             'It bores me."')
QUEEN_CHOICES = (
    c("[Pay the Queen's price.]", "pay", flags=(RETURNED, DEBT, STARTED)),
    c('[Argue the fine print] "The patient is mine. Put the debt on me."', "raised", flags=(RETURNED, FAVOUR, STARTED)),
    c('[Refuse her price] "Keep her, then. I\'ll find a cheaper specialist."', "refused", flags=(DECLINED, CLOSED)))
letter(P + "evil.second_opinion", "A second opinion", 5, [
    nar("start", '''{n}The answer comes back on the third morning, and it is not the vrock. It is a moth the size of your hand, black as a closed eye, and it settles on your knuckles and unfolds into a letter that smells of night-blooming flowers.{/n}''',
        c("Continue", "unanswered", requires=(UNANSWERED,)),
        c("Continue", "fooled", requires=(FOOLED,), forbids=(UNANSWERED,)),
        c("Continue", "late", requires=(LATE,), forbids=(UNANSWERED, FOOLED)),
        c("Continue", "queen", forbids=(UNANSWERED, FOOLED, LATE))),
    noc("queen", '''"A referral. How very civilised. You killed my succubus, Commander, and before the blade had even landed you were recommending me as her physician." {n}The hand is beautiful and not quite steady, as if the writer were laughing.{/n}
"I am not a physician. I am the reason there are succubi. She is here. She is tedious. She talks about you. I will send her back." ''' + QUEEN_FEE,
        *QUEEN_CHOICES),
    noc("late", '''"You did not refer her, Commander. You mislaid her, and then you sent a vrock to ask where. I charge extra for carelessness, and I charge the patient, because it is her carelessness that I find interesting: she let you watch her die and did not ask you to stop."
"She is here. She is tedious. She talks about you. I will send her back." ''' + QUEEN_FEE,
        *QUEEN_CHOICES),
    noc("fooled", '''"You have made a fool of me once already, Commander. I read this referral twice. Then I had it read to me by someone who hates you, to see what he would find in it. He found a joke. So did I. That is the insulting part."
"She is here. She is tedious. She talks about you. I will send her back." ''' + QUEEN_FEE,
        *QUEEN_CHOICES),
    nar("unanswered", '''{n}It is not the queen's hand. The queen is in hiding, and nobody in Alushinyrra answers for her while she is. It is a hand you know from the lair, in lipstick, on the back of a pressed moth's wing:{/n}
"She hasn't answered, so nobody said no. I'm sitting up. She'll bill you when she crawls out, and I know her rates: one summons, once. Say yes, doctor, or I lie back down. A."''',
        c("[Send back one word: yes.]", "pay_hiding", flags=(RETURNED, DEBT, STARTED)),
        c('[Send back: "Put it on me, not you."]', "raised_hiding", flags=(RETURNED, FAVOUR, STARTED)),
        c("[Send nothing back.]", "refused_hiding", flags=(DECLINED, CLOSED))),
    noc("pay", '''"Then it is done. Somewhere in my city a succubus is sitting up on a slab and complaining about the draught. I shall have her carried to the gate." {n}A last line, smaller, as if added after the ink had dried:{/n} "She asked whether you had paid. When I told her the price she laughed until she cried. I have not seen one of mine cry in a very long time. You may keep that, too. No charge."''', c()),
    noc("raised", '''"How gallant. Very well: not her summons. Yours. One favour, Commander, of my choosing, at my hour. I told you haggling bores me. Now it will cost you."
{n}There is a postscript in a different hand, rounder, pressing too hard:{/n} "You idiot. You absolute idiot. Don't ever let me see the bill. A."''', c()),
    noc("refused", '''"There are no cheaper specialists, Commander. There are only worse ones. Keep your diagnosis." {n}The letter folds itself back into a moth and flies out of the window. It does not come back.{/n}''', c()),
    nar("pay_hiding", '''{n}You send back one word. Somewhere in the Midnight Isles a debt settles into the dark like a coin into a well, which is exactly the kind of debt that is always collected.{/n}''', c()),
    nar("raised_hiding", '''{n}You send it back. The next moth brings nothing but a smear of lipstick, and under it:{/n} "Idiot. She'll pick the hour and she'll pick it to hurt. A."''', c()),
    nar("refused_hiding", '''{n}You send nothing back. Nobody writes again.{/n}''', c()),
], requires=("trickster.ever", PRIMED, EVIL_DEAD), forbids=(RETURNED, DECLINED), delay=72, chapters=(5,),
    TricksterDevice=True, TricksterState="evil_dead")

REUNION_OPEN = '''"A second opinion." {n}She smiles with too many teeth.{/n} "You bought me back from her on credit. Don't ever let me see the bill."
"I had a lot of fun with you, Commander. I even missed you a little, which was humiliating. Let's see if you can still keep up."'''
# Her terms are evil terms (08 §2.3): she wants a life. Oblige with your own, oblige with a condemned man's, find the
# third way a Trickster finds (canon: demons devour "other demons in their own way", hub Cue_0105), or refuse her.
REUNION_CHOICES = (
    c('[Let her feed] "Just a taste."', "taste", flags=(REUNITED, FED_ON_YOU)),
    c('[Drag a bound cultist forward] "Not me. Him."', "cultist", alignment=("Evil", 2), flags=(REUNITED, FED_ON_PRISONER)),
    c('[Hand her the vrock courier\'s chain] "You said demons eat demons. Eat the messenger."', "demon",
      requires=(LATE,), flags=(REUNITED, FED_ON_DEMON)),
    c('[Refuse her] "Not a drop."', "refuse", flags=(REUNITED, HUNGRY)),
    c('[Have the babau you took alive from her gang dragged in] "One of your boys survived. Eat him."', "babau",
      forbids=(LATE,), flags=(REUNITED, FED_ON_DEMON)))
REUNION_ENDS = [
    nar("taste", '''{n}She takes her time. She holds your wrist the way she held it in a chapel, once, in another life, and then she does not hold it that way at all. When she lets go, she licks her lip and looks at you as if you'd passed an exam you didn't know you were sitting.{/n}
"Still sweet. You'll need to sit down in a moment. Don't be embarrassed. Everybody does."''', c()),
    a("cultist", '''"A cultist. How thoughtful." {n}She looks at him, and then at you, and something in her face goes very flat.{/n} "You do know I can tell the difference? No. Of course you don't. Eat your vegetables, darling, and let me eat mine."
{n}She does. You watch. She wants you to watch.{/n}''', c()),
    a("demon", '''{n}She looks at the vrock, hunched at the end of its chain with its broken beak, and then at you, and bursts out laughing.{/n}
"Oh, that's low. That's beautifully low. You brought your own postman." {n}She takes the chain. The vrock makes a noise like a hinge.{/n} "It's like eating gravel with a sauce on it, you know. It'll hold me for a week. It won't feed me. And you've lost the only thing in the Abyss that would carry a letter for you." {n}Her smile widens.{/n} "Clever. Expensive. I like it."''', c()),
    a("babau", '''{n}Your soldiers drag it in on a chain: the babau from her own gang, the one that ran when the balor fell and was dug out of the rubble alive. It sees her sitting up on the stones and makes a sound like a kettle.{/n}
"Oh, Skritch." {n}She sounds almost fond.{/n} "You ran. I saw you." {n}She takes the chain.{/n} "It's like eating gravel with a sauce on it. It'll hold me for a week. It won't feed me." {n}She looks at you over the babau's head, and her smile widens.{/n} "You kept one of my boys alive just for this. That's the nastiest thing you've ever done, darling. I adore it."''', c()),
    a("refuse", '''"No?" {n}She tilts her head, interested rather than hurt.{/n} "Then I'll find someone who says yes. There are always people who say yes. That was the whole trouble with you. You never did."
"Don't wait up."''', c()),
]
presence_scene(P + "evil.reunion", "The patient sits up", '"You look well, for a corpse."', [
    a("start", REUNION_OPEN + "\n" + "\"But first: I'm starving, and you're the one who prescribed it.\"",
      c("Continue", "hiding", requires=(IN_HIDING,)),
      c("Continue", "price", forbids=(IN_HIDING,))),
    a("hiding", '''"She's hiding, you know. Our Lady. First time in a thousand years nobody's watching me eat." {n}She says it lightly, and her eyes go to the dark corners of the lair anyway, as if the dark might be listening. In the Midnight Isles, it usually is.{/n}''',
      c("Continue", "price")),
    a("price", '''"So. The fee for a house call, doctor." {n}She stretches out one bare foot and taps your boot with it.{/n} "Somebody's life, a little of it. Yours or anyone's; I'm not fussy. Choose."''', *REUNION_CHOICES),
    *REUNION_ENDS,
], ("trickster.ever", RETURNED, EVIL_DEAD), (REUNITED, CLOSED, P + "evil.reunion_letter"), 24, LAIR_PRESENCE, LAIR)

letter(P + "evil.reunion_letter", "A note in lipstick", 5, [
    nar("start", '''{n}A note in lipstick on a pressed black moth wing, pushed under your door by something that did not use the stairs:{/n}
"You didn't come to the lair. Rude. I'm hungry. Leave your window open tonight, or leave a cultist tied to the gate, or leave nothing, and find out what I do about nothing. A."''',
        c("[Leave the window open.]", "window", flags=(REUNITED, FED_ON_YOU)),
        c("[Leave a cultist tied to the gate.]", "gate", alignment=("Evil", 2), flags=(REUNITED, FED_ON_PRISONER)),
        c("[Chain the babau from her gang to the gate instead.]", "vrock", flags=(REUNITED, FED_ON_DEMON)),
        c("[Leave nothing, and let her do what she threatened.]", "nothing", flags=(REUNITED, HUNGRY))),
    nar("window", '''{n}You wake at the hour before the first bell, colder than you went to sleep, with a black feather on the pillow and the taste of someone else's lipstick on your mouth.{/n}''', c()),
    nar("gate", '''{n}In the morning the gate guard reports that the prisoner tied there overnight has gone mad and will not stop weeping. Nobody saw anything. Nobody ever does.{/n}''', c()),
    nar("vrock", '''{n}In the morning there is an empty chain at the gate and a smear of something grey and sticky on the cobbles, and a lipstick mark on the gatepost at exactly the height of a woman leaning against it, laughing.{/n}''', c()),
    nar("nothing", '''{n}In the morning a patrol sergeant of the third company does not report for duty. They find him at noon, smiling, and he never wakes up. There is a black feather tucked into his cuff, addressed to you, and on it, in lipstick: "You chose nothing. Nothing has a name now. It's on your account, darling, not mine."{/n}''', c()),
], requires=("trickster.ever", RETURNED, EVIL_DEAD, LAIR_FAILED), forbids=(P + "evil.reunion", REUNITED, CLOSED, LATE),
    delay=120, chapters=(5,))

TERMS_OPEN = [
    a("terms", '''"I won't wear your colours, and I won't bless anything. I'll come when I'm hungry, and you'll open the door. That's the arrangement. Don't look at me like that. It's the only arrangement I've ever kept."''',
      c("Continue", "debt", requires=(DEBT,)),
      c("Continue", "favour", forbids=(DEBT,))),
    a("debt", '''"And when she calls, I'll go. Don't sulk. You said yes to it. And don't ever try to stop me: lock a door, hire a priest, stand in my way. I'll go through you to get to her, and I won't be gentle, because she won't let me be."''',
      c("Continue", "hungry", requires=(HUNGRY,)),
      c("Continue", "hiding", requires=(IN_HIDING,), forbids=(HUNGRY,)),
      c("Continue", "ask", forbids=(HUNGRY, IN_HIDING))),
    a("favour", '''"And when she comes for what you owe her, I'll be watching. I want to see your face. I want to see what a Trickster looks like when they're the one being collected. And if you try to wriggle out of it, she won't come to you. She'll come to me, and ask me to fetch it."''',
      c("Continue", "hungry", requires=(HUNGRY,)),
      c("Continue", "hiding", requires=(IN_HIDING,), forbids=(HUNGRY,)),
      c("Continue", "ask", forbids=(HUNGRY, IN_HIDING))),
    a("hungry", '''"You sent me away hungry once. I ate a patrol sergeant. Consider that my second opinion."''',
      c("Continue", "hiding", requires=(IN_HIDING,)),
      c("Continue", "ask", forbids=(IN_HIDING,))),
    a("hiding", '''"She's in hiding. She'll come out. Queens always do. Think about that before you lock any door."''',
      c("Continue", "ask")),
    a("ask", '''{n}She slides off the counter, takes the stolen ring off her finger and puts it on yours, and closes your hand over it.{/n} "So. Is the door open, darling, or do I have to steal the key?"''',
      c('[Open the door] "It\'s never locked."', "open", flags=(COMMITTED, OPEN_DOOR)),
      c('[Ask her to stay instead] "Don\'t visit. Stay."', "stay", flags=(ALLY,)),
      c('"No."', "no", flags=(CLOSED,))),
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
"Take it back." {n}She has you by the sleeve in the vestry, whispering, furious.{/n} "They'll look at me every day. A succubus, blessing their swords. Do you know what they'll say? Do you know what I'll want, with every one of them kneeling in front of me?"''',
      c("Continue", "sword")),
    a("sword", '''{n}She doesn't leave, though. When the first soldier at the rail clears his throat, she goes out to him. She takes his sword in both hands as if it might burn her, and says the words she has heard the Desnan priests say over travellers, and hands it back. He thanks her. She stands there looking at her own hands.{/n}
"He thanked me," she says, when she comes back. "He didn't know what I am, and he thanked me. Is that what you wanted? Is that the joke?"''',
      c('"Then do it anyway. That\'s the job."', "job", alignment=("Chaotic", 1), flags=(CHAPLAIN, STARTED)),
      c('"It was a joke. I\'ll strike it out."', abort=True)),
    a("job", '''"That's the job." {n}She repeats it the way people repeat a sentence in a foreign language, to see how it sits in the mouth.{/n} "All right. All right. Tomorrow at sunrise, then. Somebody has to tell me which end of a censer is which."''', c()),
], ("trickster", "trickster.ever", FAILED), forbids=(CHAPLAIN, CLOSED, DEAD), chapters=(3, 5),
    EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="failed")


# --- 7. Commit, redeemed and chaplain worlds (spec §7) ---------------------------------------------------------------

hub(P + "terms", "Both of me", 5, '"You wanted to ask me something."', [
    nar("start", '''{n}She is on the chapel steps after the evening blessing, a blade still across her knees. The soldiers have gone; the lamplighter has not come yet. It is the one hour in Drezen when nobody needs anything from either of you.{/n}''',
        c("Continue", "fed", requires=(AFTERTASTE,)),
        c("Continue", "chaplain", forbids=(AFTERTASTE,))),
    a("fed", '''"I've been counting. Days since I last wanted to bite someone. The number keeps going back to zero." {n}She turns the blade over, looking at her reflection in it.{/n} "It went back to zero yesterday. A novice cut his hand on the altar rail, and I had to go and stand in the well-house until it stopped smelling of him."''',
      c("Continue", "question")),
    a("chaplain", '''"The second company calls me Chaplain now. Not one of them asked what I used to be. They bring me their swords and their bad dreams and once, a boy from Nerosyan brought me a letter for his mother because he couldn't write." {n}She wipes the blade clean, although it is already clean.{/n} "I think that's the cruellest thing you've ever done to me. I think it might also be the kindest. I haven't decided."''',
      c("Continue", "question")),
    a("question", '''"So I have a question for you. Only one, and you can't answer it with a joke, because I'll know." {n}She lays the blade down on the step between you.{/n} "Will you still want me when I'm good? Or only when I'm hungry?"''',
      c('"Both. Always both."', "both", flags=(COMMITTED,)),
      c('"Only the good days."', "saint", flags=(COMMITTED, SAINT_ONLY)),
      c('[Let her keep her answer for now] "Then I\'ll ask again."', "not_yet", flags=(DECLINED,)),
      c('"Neither."', "neither", flags=(CLOSED,))),
    a("both", '''"Both." {n}She closes her eyes.{/n} "That is the most frightening answer, and the only one I'd have believed. If you'd said only the good days, I'd have spent the rest of my life hiding the others from you. If you'd said only the hungry ones, I'd have hated you by morning."
{n}She reaches for your hand, stops an inch short, and leaves her fingers there, in the air, where you can see them not touching you.{/n} "Both. All right. Both."''', c()),
    a("saint", '''"Only the good days, then." {n}She nods, and something shutters in her face so smoothly you almost miss it.{/n} "I'll keep the rest out of your sight. I'm very good at that. I did it for centuries, the other way round. You won't thank me for it, one day. But you'll have what you asked for."''', c()),
    a("not_yet", '''"Don't answer yet. You've got the look of someone who's going to be clever, and I can't bear clever tonight." {n}She picks the blade back up.{/n} "Ask me when I've gone a week without wanting to eat anyone. I'll tell you then. I promise I will."''', c()),
    nar("neither", '''{n}She lays the blade down very carefully on the step between you, as if it were the answer and she were giving it back, and goes inside.{/n}''', c()),
], ("trickster.ever",), forbids=(EVIL_DEAD, CLOSED, DECLINED, COMMITTED), delay=72, chapters=(5,),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]])

hub(P + "terms_again", "Seven days", 5, '"It\'s been a week."', [
    a("start", '''"Seven days. I counted twice, and then I made Sosiel count, because I didn't trust myself." {n}She doesn't smile.{/n}
"Before I answer, I want one promise from you, and you won't like it. The next time I'm dying, you let me die. No diagnosis. No joke. No wrist held out like a bowl. You stand there and you let it be a death, because if you won't, I'll never know which of my days are mine and which are yours."''',
      c('[Promise] "No more jokes at your deathbed. I swear it."', "yes", flags=(COMMITTED, NO_SECOND_JOKE)),
      c('"I can\'t promise that."', "no", flags=(CLOSED,))),
    a("yes", '''{n}She watches you the way she watches strangers in the market, trying to read what they are.{/n} "Then yes. All of it. For as long as what you didn't kill of me lasts." {n}She almost laughs.{/n} "Which is a terrible thing to say to someone you love. I'll work on it."''', c()),
    a("no", '''"Then we're done asking each other things." {n}She says it gently. That is the worst part.{/n}''', c()),
], ("trickster.ever", DECLINED), forbids=(EVIL_DEAD, CLOSED, COMMITTED), delay=96, chapters=(5,),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN]])


# --- The fallen's night: over the roofs of Drezen (heat to the cut; the cut lands at the start of the act) ---------

NIGHT_NODES = [
    a("start", '''"Your window was open. You weren't in it. So I came to find you." {n}She is standing on the jeweller's counter, which puts her head above yours, and she is enjoying that.{/n}
"You left it unlocked for me. Do you know how many doors have been left unlocked for me? Thousands. Do you know how many I walked through twice?"''',
        c("Continue", "up")),
    nar("up", '''{n}She does not wait for an answer. She steps off the counter into your arms, and then her wings open, and the arcade drops away beneath your boots. The roofs of Drezen go past below in the rain: the chapel, the barracks, the long black line of the wall. She puts you down on the wet slates of the old basilica's roof, where the gargoyles lean out over the city, and lands astride the ridge beside you.{/n}
"This is where I used to sit, in the old days, choosing." {n}Rain runs off her hair.{/n} "Every window in the city, lit or dark. Every sleeper in them. I'd sit here and choose."''',
        c("Continue", "choose")),
    a("choose", '''{n}She takes your face in both hands. Her nails are very long and very clean.{/n}
"This is the part where you remember what I am. Every caress costs. Every one. I'm not going to pretend otherwise, and I'm not going to be careful. If you want careful, you know which saint to go and pray to."''',
        c("Continue", "cured", requires=("trickster.religion_tier1",)),
        c("Continue", "paid", forbids=("trickster.religion_tier1",))),
    nar("cured", '''{n}Her mouth finds yours and the cold goes through you like a key turning. You do the thing you learned, the quack's trick: you name the drain a negative condition and treat it, once. It holds for one breath, and then there is nothing left in you to treat it with. She feels the second one land. She pulls back an inch, astonished, furious, laughing.{/n}
"You cheated once." {n}Her wings open behind her and cut the rain off both of you.{/n} "Once. And now you're mine to take, and I'm starving, and the only thing between you and the bottom of me is how long I can make myself hold my breath." {n}Her nails are in your shoulders.{/n} "Count for me. Out loud. When you reach ten, push me off the roof."''',
        c("[Start counting.]", "cut")),
    nar("paid", '''{n}Her mouth finds yours and the cold goes through you like a key turning, and you let it. You have no trick for this. You have only the choice to stay on the roof in the rain and take it. She feels that too, and something in her goes still and sharp and very interested.{/n}
"You're letting me." {n}Her wings open behind her and cut the rain off both of you.{/n} "Nobody lets me. They beg, or they fight, or they pray. You're just letting me."''',
        c("[Let her.]", "cut")),
    nar("cut", '''{n}She pushes you back against the wet slates with one hand flat on your chest, unhurried, the gargoyles leering over her shoulders, and kneels over you with her hair falling round both your faces like a curtain against the rain. Far below, a watchman calls the hour. She reaches back and unhooks the last clasp of her own dress, and it goes, and the city goes with it.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}You wake in your own bed with the first bell ringing, colder than you went to sleep and warmer than you have any right to be, and with no memory of how you got down off the basilica roof. The window is open. There is a black feather on the pillow, and under it, in lipstick, on a pressed moth wing:{/n}
"Still sweet. Same time next month. Don't lock it. A."''', c(flags=(NIGHT_DONE,))),
]
drezen_pair(P + "evil.window", "The roofs of Drezen", '"You kept the door."', NIGHT_NODES,
            ("trickster.ever", RETURNED, EVIL_DEAD, COMMITTED, OPEN_DOOR), (CLOSED, NIGHT_DONE), 24)


# --- 8. Epilogue pages (ArueshalaeEpilogue; no system effects) -------------------------------------------------------

EP = dict(last=6, Relationship="arueshalae")
SCENES.append(scene(P + "epilogue.commit", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Arueshalae answered the Commander's question, so she answered it afterwards.{/n}''',
        paragraphs=(
            p('''{n}She answered it on the chapel steps in Drezen, with a blade across her knees and the second company's swords stacked in the vestry behind her: all of her, the hunger and the prayer in one knot, for as long as she could hold it. She held it. Nobody who knew her was surprised, except her.{/n}''',
              forbids=(EVIL_DEAD,)),
            p('''{n}She came through the Commander's window the first night after Threshold, sat on the sill with one knee drawn up, and said she had decided to keep visiting. It was the closest thing to a vow she ever made, and she kept it.{/n}''',
              requires=(EVIL_DEAD,)),
        ))],
    requires=("trickster.ever",), forbids=(COMMITTED, CLOSED, DECLINED, ALLY),
    RequiresAnyGroups=[[AFTERTASTE, CHAPLAIN, REUNITED]], **EP))
SCENES.append(scene(P + "epilogue.declined", "", "ArueshalaeEpilogue", 6, "", [
    nar("page", '''{n}Arueshalae never finished counting her week. She served as the crusade's chaplain until the end, blessed the swords of the second company and the lamps of the field hospital, and when anyone asked her about the Commander she said she was still deciding.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), **EP))
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
    reaction("Lann", P + "react.lann_deal", (RETURNED, EVIL_DEAD),
             '''"The queen offered me anything I wanted, and I told her I'd rather die than wear a debt." {n}He finally looks at you.{/n} "You went and took one out for a succubus who tried to eat you. That's either very noble or very stupid. I'm going with stupid. Mostly."''',
             chapter=5, last=5, entry='"About Arueshalae..."', **LANN),
    reaction("Sosiel", P + "react.sosiel_evil", (RETURNED, EVIL_DEAD),
             '''"I prayed for her the night she died at the lair." {n}Sosiel turns his cup in his hands.{/n} "I'm not sorry she's back. I'm afraid of what you promised to bring her, and I'll pray about that too. Every night, if you'll let me. Even if you won't."''',
             chapter=5, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Sosiel", P + "react.sosiel_chaplain", (CHAPLAIN,),
             '''"I've been helping her with the sermons." {n}Sosiel smiles, which is not something he does lightly about sermons.{/n} "She's better at forgiveness than any of us. She practises on herself every day. She hasn't got the hang of that one yet."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **SOSIEL),
    reaction("Lann", P + "react.lann_chaplain", (CHAPLAIN,),
             '''"She blessed my bow this morning. It didn't catch fire." {n}Lann holds it up as evidence.{/n} "I checked twice. Then I went back and asked her to do the arrows. Don't tell her I said so."''',
             chapter=3, last=5, entry='"About Arueshalae..."', **LANN),
])


def integrate(payload):
    """Register her revival, presences and derived keys. Scenes are added by expansion.py; world keys bind on demand."""
    payload.setdefault("Revivals", {}).update({k: dict(v) for k, v in REVIVALS.items()})
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
