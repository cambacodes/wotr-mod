"""Shamira on the Trickster path: "Dreams for a body" (Writer/handoffs/11-ROSTER-PLAN-2.md §2 as revised by the
coordinator on 2026-09-29 after the independent review: the flask capture is dropped, and Areelu's flask stays Last
Call's alone. The spec Writer/handoffs/trickster/shamira.md is used for canon and hooks only.)

Canon (blueprints.zip / enGB):
- She is "Nocticula's longtime lover and ally... she dreams of having a demon lord's power and true dominion over
  Alushinyrra... a fallen celestial" (C5_FinalLaugh/Obj_3_ShamiraEssence efacfcbd). Born in Heaven "to sow dreams and
  delightful fantasies among mortals" (Shamira_dialogue/Cue_0118 885716ed), "my fiery wings carried me" (Cue_0068
  48f94a01); "A dream is a bird, not a horse. You can't restrain it, you can only hurt it with your reins." (Cue_0076
  4439415b); Nocticula "came for me and shrouded me in her shadows" (Cue_0077 06b5cce2). Her throne-light "blinds,
  withers, makes a person burn with fever" (Cue_0100 fb749b1a).
- She reads minds and speaks into them: "use your mind instead of your flapping lips!" (Cue_0006 76f6e121), "Shamira's
  voice whispers inside your mind," (Cue_0157 817101b5); she strips a mind "as efficiently and ruthlessly as a hunter
  dressing a carcass" (Cue_0106 43bb7ca8), or is thrown out of one (Cue_0055 b15365b6, Cue_0058 0e929c72).
- The Commander can let her in, natively, in her Chapter 4 audience: "[Imagine the mysterious mine...] Look into my mind"
  (Answer_0008 c64d3f7e), "[Think to yourself] Nahyndrian crystals are..." (Answer_0031 33f75e11), "Fine. I'll tell you
  everything." (Answer_0044 3a9a8c16, read in "your open mind", Cue_0137 fc42e958), "[Submit to the more powerful demon and
  answer in your mind]" (Answer_0178 d5c0eb02).
- Socothbenoth orders her death: "Kill her and take her essence. Easy." (SocothBriefing/Cue_0012 e5a9d6bb). The kill is
  compulsory to reach Council 5-2 (SocothInCloset/Answer_0007 7b0b6c9d, ItemsEnough SyphonWithShamira). Nocticula, told:
  "She coveted my throne. You've saved me the trouble of having to deal with her." (Nocticula/Cue_0021 84df3b22).
- Closets: "You can step inside one, and exit from another" (SocothBriefing/Cue_0011 2f4be0bd); "my spells will keep you
  hidden from her eyes and ears" (Cue_0012). The Fleshmarkets are "one of the largest slave markets in the Abyss"
  (enGB 43b30e23); "Sarzaksys, who rules the Fleshmarkets" (157ce42a).

The device: at the compulsory kill the syphon takes the Nirvana in her, and what is left of her, the demon without her
fire, flees into the one mind she was ever let into: the Commander's. Earned: the Commander let her read them in her
Harem (the native answers above, or the authored open mind of ch4.read), and at the briefing leaves that door open on
purpose; a Commander who never let her in may open it for the first time there, blind, which is a real risk. Unprimed,
she grabs the mind of the one who killed her anyway, and is drowning in it by the first rest: the Commander makes room,
on worse terms, or lets her go under. The shell is stolen from Ramisa's hothouse in the Fleshmarkets (shamira_mind); she walks out of
the Commander's dream into it, and it lives on the Commander's dreams. The cost: the Commander never dreams alone again.
The commit is her game, "think of anything but me", lost on purpose (shamira_dream).

Authored, and labelled as authored: a dying demon's self fleeing into a mind it has been let into (Shamira calls it a
whisper of her court, never tested); Ramisa's hothouse of grown shells (she is canon, the hothouse is not); the road from the Drezen wardrobe through the Council chamber to Socothbenoth's house in Alushinyrra; the
fire the syphon kept; the Commander's dreams as the only fire a stolen shell will take.

Delivery. No Shamira blueprint carries a dialog component (66e12264, ec9802dd and 4b7429fa checked), and on a Trickster
run the Commander never walks Alushinyrra in Chapter 5 (the boudoir is one visit through Socothbenoth's closet, shut once
the essence objective completes; 06a-NATIVE-PREREQS). The Chapter 4 beats are inline on her own audience list; the setup
and the first words are inline on Socothbenoth's briefing and closet lists, where he speaks. While she has no body she
lives behind the Commander's eyes, and those nights are sendings, folded into four pages (tier B, 05 §4.2). Once she has
a body she is a spawn-copy of her own unit with a click-to-talk hub (ERRATA, Presence.Dialog "hub") at the Fool King's
corner table in Drezen (shamira_dream), and the courtship after the waking is played there.
Nothing here reads, fills or removes Areelu's flask (SoulJar_Trickster): that bottle is Last Call's.
"""
from story_format import c, n, p, reaction, scene
from storylines import lastcall_ledger

SCENES = []
REL = "shamira"
P = "shamira.trickster."

HUB4 = "d138954fd7cdb2d4e90bb28cbd76235e"          # c4/HaremOfArdentDream/Shamira_dialogue/AnswersList_0003 (her audience)
HUB4_RETURN = "64fdd0fed0509db42b073f8ef7503d45"   # Cue_0069 "I was happy to satisfy your curiosity, you annoying and talkative mortal."
BRIEFING = "5266a3d8bc5b0714eaaf77dfa5c20695"      # c5/Mythic_Trickster/SocothBriefing/AnswersList_0002
BRIEFING_RETURN = "2f4be0bde527a7d4cb7c73131ab551db"  # SocothBriefing/Cue_0011 "Closets grant you freedom..."
CLOSET = "db7f69fa013c7ec49b651e7ad26c67de"        # c5/Mythic_Trickster/SocothInCloset/AnswersList_0003 (the hand-over)
CLOSET_RETURN = "e52a1d81a098a2843aa5f1f35481ddc1"  # SocothInCloset/Cue_0002 (Socothbenoth peeks out: "...Do you have it now?")
SHYKA_LIST = "d3d0efb4dfcc1964c923d7b2d6e0dc77"    # c5/Mythic_Trickster/Shyka_Offer/AnswersList_0011
SHYKA_RETURN = "5d6810f1e0eb8204fa4c3211fc603769"  # Shyka_Offer/Cue_0010 (returns to AnswersList_0011)
ARUESHALAE_HUB = "03ebad9587cbea0438d901a0f8df44f1"  # CompanionDialogues/Arueshalae/AnswersList_0003
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"    # CompanionDialogues/Daeran/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"    # CompanionDialogues/Woljif/AnswersList_0003
REGILL_LIST = "2366a8db6481070439fee222c0c52e45"   # CompanionDialogues/Regill/AnswersList_0002

STARTED = "shamira.started"
CLOSED = "shamira.closed"
COMMITTED = "shamira.committed"
KILLED = "shamira.killed"                          # Etude ShamiraKilled dd6731e2 (trickster_world)
PLAN = "shamira.plan_known"                        # SeenCue SocothBriefing/Cue_0012 (trickster_world)
HANDED = "shamira.cauldron_shown.latched"          # Latch on SocothInCloset/Answer_0007 (trickster_world)
NOCT_KNOWS = "nocticula.trickster.secret_known.shamira"   # nocticula_trickster court.shamira (read in node text only)
NOCT_HIDING = "noct.defeated_not_dead"             # read in node text only (ledger row 2)
SOCOTH_GONE = "socot.gone"
# Keys only this route reads (bound in integrate()).
LET_MINE = "shamira.let_in.mine"                   # Answer_0008 "[Imagine the mysterious mine...] Look into my mind."
LET_THOUGHT = "shamira.let_in.thought"             # Answer_0031 "[Think to yourself] Nahyndrian crystals are..."
LET_TOLD = "shamira.let_in.told"                   # Answer_0044 "Fine. I'll tell you everything." (her mind-duel, yielded)
LET_SUBMIT = "shamira.let_in.submitted"            # Answer_0178 "[Submit to the more powerful demon and answer in your mind]"
THREW_OUT = "shamira.threw_out"                    # Cue_0055 / Cue_0058: the Commander forced her out, in public
STRIPPED = "shamira.stripped"                      # Cue_0106: she tore the answer out by force
NO_MORE = "shamira.no_more_ch4"                    # Etude ShamiraNoMoreDialogues 9772be00 (the duel, either way)
CRYSTALS = "shamira.crystals_told"                 # Etude ShamiraKnowsAboutCrystalls 14a0d188 (she fought stronger in Ch5)
MASSACRE = "fleshmarket.massacre"                  # Etude FleshMarketMassacre bee15cff (variant read only)
STEALTH1 = "trickster.stealth_tier1"               # MainCharacterFacts TricksterStealthTier1Feature 4e1948fe
SELECTED = {LET_MINE: "c64d3f7e4a58fad43bd2bf135ab2b29e", LET_THOUGHT: "33f75e114857c6945b931801f0943051",
            LET_TOLD: "3a9a8c16a93db5844901ed3e1e5f5bed", LET_SUBMIT: "d5c0eb028f41da648bfbdd5a1ac2dc97"}
SEEN = {THREW_OUT: ["b15365b6241c82f4e9d6345c7a0ca77e", "0e929c72172ec654d9f70fd7d37947ce"],
        STRIPPED: ["43bb7ca856321be409cf22bfe89c28b5"]}
ETUDES = {NO_MORE: "9772be00ff3505440bb4937198c19c06", CRYSTALS: "14a0d1887eeab174dbe3a77382123899",
          MASSACRE: "bee15cff021828c4c92f09e8f771dbb2"}
FACTS = {STEALTH1: "4e1948fed4201cf46b88836457c3bad8"}

# Chapter 4 (alive).
READ = P + "read"                     # she read the Commander's mind at their invitation (authored)
LET_IN = P + "let_in"                 # Derived: she was ever let in (native answers, or READ)
HID = P + "hid"                       # the Commander hid something under the moonshine recipes
THOUGHT_WAR = P + "thought_war"
THOUGHT_HER = P + "thought_her"
BIRD = P + "bird"                     # "A dream is a bird"
INVITED = P + "invited"               # the Commander invited her into a dream
WARNED_OFF = P + "warned_off"
TASTED = P + "tasted"                 # she walked one of the Commander's dreams while alive
# Chapter 5, the device.
PRIMED = P + "primed"                 # the door she knows, left open into the boudoir
OPENED_BLIND = P + "cost.opened_blind"  # opened for the first time at the briefing, to a woman one is about to kill
VEIL = P + "veil"                     # Socothbenoth's hiding spell lent for the Fleshmarkets
FOUND = P + "heard"                   # the Commander has heard her inside
RETURNED = P + "returned"
MADE_ROOM = P + "made_room"           # the late road: room made for her in a head she was drowning in
DECLINED = P + "declined"             # let her go under
KEPT = P + "cost.kept_captive"        # locked in the back of the Commander's head for good
HONEST = P + "told_honest"
BARGAIN = P + "bargain"
LATE = P + "cost.late"
READ_ALL = P + "cost.read_all"        # she went through everything in the Commander's head, coming in
# The courtship and the waking (shamira_mind, shamira_dream) set these; epilogues and reactions read them.
NIGHT1 = P + "first_night"
SHELL = P + "shell"
TORN = P + "cost.shell_torn"
RAMISA_STORY = P + "cost.ramisa_story"     # Ramisa Sloughed Skin owns the story of the theft, with names
RAMISA_FOOLED = P + "ramisa_fooled"
DREAM2 = P + "dreamed"
FUEL = P + "fuel_set"
BARRACKS = P + "cost.barracks"        # the evil demand met: a barracks' dreams for her fire
REFUSED_BARRACKS = P + "refused_barracks"
CAST_OUT = P + "cast_out"             # thrown out of the Commander's head into the Abyss's mouth
EMBODIED = P + "embodied"
NEVER_ALONE = P + "cost.never_alone"  # the Commander never dreams alone again
CITY = P + "city"
VISITED = P + "visited"
GAME = P + "game_proposed"
ALLY = P + "ally"
LOST_GAME = P + "lost_on_purpose"
THRONE = P + "throne_told"
STAND = P + "throne.stand"
NOT_NOCT = P + "throne.not_her"
LIED_HER = P + "throne.lied"
LATE_COMMITTED = P + "late_committed"
SECRET = "trickster.secret.shamira_barracks"
# Early thread T3 (15b-EARLY-THREADS.md, PP9): what the paper-eater swallowed, bought with his freedom (Chapter 3).
TELMER_HUB = "ca6d1fdb3b2e1cd42a995788f05efdb2"      # c3/IvorySanctum/CultCamp_CultistFromEstrod/AnswersList_0002
TELMER_RETURN = "0ff9dfa1944f90b4cb8fb2ceaefadf4b"   # Cue_0024 "Maybe you could let me go, and I... will tell you..."
TELMER_RELEASE = "51e53730da8c07443be9a463ed33edcd"  # Cue_0013 (he sobs and wanders off; OnStop plays his departure)
INTERROGATION = "shamira.early.telmer_interrogation"  # the scene id (completion), distinct from the success flag
INTERROGATION_SEEN = INTERROGATION + ".seen"
INTERROGATION_DECLINED = INTERROGATION + ".declined"
NOTES = "shamira.early.telmer_notes"                 # set only by the release that bought the tally
EXPOSED = "shamira.early.telmer_exposed"             # set with the release: he tells every cult fire who let him go
TELMER_FAILED = "shamira.early.telmer_failed"
TELMER_LETTER = "shamira.early.telmer_letter"
TELMER_LETTER_SEEN = TELMER_LETTER + ".seen"
LETTER_BURNED = TELMER_LETTER + ".burned"
LETTER_KEPT = TELMER_LETTER + ".kept"
XANTHIR_DEAD = "xanthir.dead"                        # SeenCue Xanthir_after/Cue_0038 (his death; OnStop Kill)
MANIFEST = P + "manifest_shown"
SEEN[XANTHIR_DEAD] = ["101f336e917865649aca9e074fde5be5"]
# The native releases of the same half-elf (each Answer of the verdict list or hub that lets him go), and every release.
SPARED = {"telmer.spared_0012": "dfc736a14d7a5184c9579533d3d90803",   # Answer_0012 "Get out of here."
          "telmer.spared_0015": "514f660014964d0409d18eb5bb94e0f5",   # Answer_0015 "Renounce the demons..."
          "telmer.spared_0017": "73cefa3ea5b79b54ebf9e84562d3eecf",   # Answer_0017 "Go wherever you will..."
          "telmer.spared_0018": "d2b603cf4319b5847a24ad9e402384c6"}   # Answer_0018 [Point at the cauldron] (he eats it)
SELECTED.update(SPARED)
LIVE = (CLOSED, KEPT, CAST_OUT)

DERIVED = {
    # The earning: she was let in, natively in her Chapter 4 audience or by the Commander's open mind (ch4.read).
    LET_IN: [[LET_MINE], [LET_THOUGHT], [LET_TOLD], [LET_SUBMIT], [READ]],
    # R2-6: she proposed the game; if the war ends first, the epilogue carries the answer (Last Call, household).
    LATE_COMMITTED: [["trickster.ever", GAME]],
    # 05 §2.5 voice note: she keeps a harem; she is not kept in one.
    "shamira.harem.voice.keeps_a_harem": [[COMMITTED], [LATE_COMMITTED]],
    # T3: the scribe walked free, natively or for the tally (native_next leaves no native dialog history).
    "telmer.released": [["telmer.spared_0012"], ["telmer.spared_0015"], ["telmer.spared_0017"], ["telmer.spared_0018"], [NOTES]],
    # The Ledger's Secrets page reads trickster.secret.<k> (08 §2.1), held once the tally is bought.
    "trickster.secret.telmer_tally": [[NOTES]],

}

RELATIONSHIP = dict(
    Title="Dreams for a Body",
    Description=("Socothbenoth wanted Shamira's essence, and he got it. I left a door open in my head when I killed her, "
                 "the door she had already been through once, and what was left of her came through it. Now the Ardent Dream "
                 "lives behind my eyes, and wants a body, and says only my dreams will wake one."),
    Objective="Find Shamira a body",
    Guidance=("On the Trickster path, let Shamira into your mind in her Harem in Chapter 4. When Socothbenoth tells you to "
              "kill her, ask him what happens to the rest of her, and leave that door open. After the kill, listen at his "
              "closet. A body can be taken from the Fleshmarkets through his closets; she will tell you what wakes it."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[KILLED], FailureFlags=[],
    UnavailableOverrides={KILLED: RETURNED},
    TricksterAccess={
        "killed": dict(detect=[KILLED], device=P + "killed.voice", returned=RETURNED),
        "cold": dict(detect=[KILLED], device=P + "killed.drowning", returned=RETURNED),
    },
)


def sh(id, text, *choices, **kw):
    """Shamira speaking on a page (her portrait)."""
    return n(id, "Shamira", text, *choices, portrait="Shamira", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Shamira", **kw)


def conv(id, text, *choices):
    """The native conversant of the list the scene sits on: Shamira on her audience list, Socothbenoth on his."""
    return n(id, "conversant", text, *choices)


def audience(id, title, entry, nodes, requires, forbids=(), delay=0):
    """A physical Chapter 4 scene on her own audience list (her live unit speaks), returning to it."""
    SCENES.append(scene(id, title, "Shamira", 4, entry, nodes, requires=requires, forbids=(KILLED, NO_MORE, *forbids),
                        delay=delay, last=4, Relationship=REL, Chapters=[4], AnswerLists=[HUB4], NativeReturnCue=HUB4_RETURN))


def page(id, title, nodes, requires, forbids=(), delay=0, chapters=(5,), kind="sending", into=None, **extra):
    (SCENES if into is None else into).append(scene(
        id, title, "Shamira", min(chapters), "", nodes, requires=requires, forbids=forbids, delay=delay,
        last=max(chapters), Relationship=REL, Chapters=sorted(set(chapters)), Remote=True, Kind=kind, **extra))


WHISPER = "{n}Shamira's voice whispers inside your mind,{/n} "


# --- Early thread T3 (15b-EARLY-THREADS.md, PP9; T, the live Trickster): "What did you eat this morning?" ---------------
# Canon: the half-elf scribe Telmer (Ch1 Cue_0004 15b76999) eats paper (Ch1 Cue_0008); in Chapter 3 he offers Xanthir's
# secrets for his freedom (Cue_0024 0ff9dfa1), and the camp barks say a student's notebook went missing, "the chewed-up
# cover lying next to Paper-muncher's bedroll" (11fc5403). Jerribeth (JerribetnFinal/Cue_0013 bbd3bba7): the crystals come
# from the Midnight Isles with Nocticula's approval, and Hepzamirah oversees the shipments. AUTHORED, labelled: that the
# notebook held a crystal-loading tally, and every number and word of it. No canon links Telmer to Shamira; the thread is
# the information. Telmer's dialog exists only while DemonScriptorAlive plays, so no extra binding gates it.

def telmer(id, text, *choices):
    """The half-elf scribe, the native conversant of his camp dialog."""
    return n(id, "conversant", text, *choices)


SCENES.append(scene(INTERROGATION, "What the paper-eater swallowed", "Shamira", 3,
    '"Not what you were doing. What you *ate*. This morning. The notebook."', [
    telmer("start", '''{n}The half-elf goes green, then white, then a sort of hopeful grey.{/n} "I... it was an accident! It was lying there, and the cover was already loose, and I had not eaten since the day before yesterday, and it was *delicious*... I mean... What notebook?"''',
        c('"Recite it. Every line you swallowed."', check=dict(Skill="CheckIntimidate", DC=18, Success="recite", Failure="garbled"),
          flags=(INTERROGATION_SEEN,)),
        c('"Forget it."', abort=True, flags=(INTERROGATION_DECLINED, INTERROGATION_SEEN))),
    telmer("recite", '''{n}He shuts his eyes and recites in the sing-song of a student who has had his lessons beaten into him:{/n} "'Consignment seven. Forty-one crates sent, by Hepzamirah's word, under the Lady in Shadow's seal. Forty received at the camp, counted and loaded. The forty-first not accounted.' Then a drawing of a crate. A bad one."
{n}He wipes his mouth on his sleeve.{/n} "That's all. That's all of it, I swear on my own stomach. It was a very short notebook. Poor Telmer has an excellent memory and a terrible life."''',
        c('"Walk. Now. Before I change my mind."', native_next=TELMER_RELEASE, flags=(NOTES, EXPOSED), alignment=("Chaotic", 1))),
    telmer("garbled", '''{n}He recites. It goes on for some time. There are crates in it, then cauldrons, then a recipe for lentils, then what is plainly a love poem to a girl in the Sanctum's kitchens, rhymed badly.{/n} "...and that is every word, I swear it."
{n}It is not. Whatever he swallowed this morning, he is not going to give it up to someone he is not more afraid of than his own masters.{/n}''',
        c("[Let him babble.]", flags=(TELMER_FAILED,))),
    ], requires=("trickster",), forbids=(INTERROGATION, INTERROGATION_SEEN), last=3, optional=True, Relationship=REL,
    Chapters=[3], AnswerLists=[TELMER_HUB], NativeReturnCue=TELMER_RETURN))

# The released scribe writes (Chapter 3, so always before her audience): a letter, two days after the release. The text
# follows the verified Xanthir outcome at delivery, not an assumed chronology. Carrier (authored): a camp follower who
# deserted the cult camp, paid in chewed coins.
TELMER_SIGN = "Your servant, who told nobody anything,\nT."
SCENES.append(scene(TELMER_LETTER, "Who told nobody anything", "Telmer", 3, "", [
    nar("carrier", '''{n}A camp follower in a blanket stiff with filth turns up at the edge of your camp asking for "the one who lets people go". She ran from the cult camp below the Ivory Sanctum, she says, the night after you came through it, and she was paid to carry this. She shows you her pay: three copper coins, every one of them chewed.{/n}
{n}The letter is written on the inside of a ration wrapper in a scribe's beautiful hand gone shaky. One corner has been nibbled.{/n}''',
        c("Continue", "dead", requires=(XANTHIR_DEAD,), flags=(TELMER_LETTER_SEEN,)),
        c("Continue", "alive", forbids=(XANTHIR_DEAD,), flags=(TELMER_LETTER_SEEN,))),
    n("dead", "Telmer", '''"Most merciful Commander,
They know you let me go. The cauldron-masters who are left think I sold them to you. I told them *nothing*. I told them I ran, which is true, and that you were terrible, which is also true, and they threw my bedroll in the latrine trench anyway.
They say Master Xanthir is dead. I wept. I am not certain for whom.
I have not eaten a single page since the camp. I am sending you this one instead, which surely proves my discretion. If you ever need a scribe with an excellent memory and an iron stomach, the girl who carries this knows where poor Telmer sleeps.
''' + TELMER_SIGN + '"',
        c("[Burn it.]", flags=(LETTER_BURNED,)),
        c("[Keep it.]", flags=(LETTER_KEPT,))),
    n("alive", "Telmer", '''"Most merciful Commander,
They know you let me go. The Plagued One knows. I told him *nothing*. I have not been anywhere near him, which is how I intend to go on telling him nothing. Please remember that I told him nothing.
I have not eaten a single page since the camp. I am sending you this one instead, so that somebody outside the Sanctum knows I said nothing, in case Master Xanthir decides I said something. He decides things like that. Then he decides what to do with the people who said them.
''' + TELMER_SIGN + '"',
        c("[Burn it.]", flags=(LETTER_BURNED,)),
        c("[Keep it.]", flags=(LETTER_KEPT,))),
    ], requires=("trickster", NOTES), forbids=(TELMER_LETTER_SEEN,), delay=48, last=3, Relationship=REL, Chapters=[3],
    Remote=True, Kind="letter"))

# The durable reader: a Secrets page in the Ledger, whether or not her Chapter 4 audience is ever reached.
lastcall_ledger.early(dict(
    Id="early.telmer", Section="Secrets", Portrait="Shamira", Title="A paper-eater's freedom",
    Text="{n}At the cult camp below the Ivory Sanctum you let Xanthir's scribe walk free, for a crate tally he had eaten "
         "that morning: forty-one crates sent under the Lady in Shadow's seal, forty received.{/n}",
    Lines=[lastcall_ledger._line("{n}A paper-eater tells every cult fire who traded his freedom for a crate count.{/n}",
                                 requires=[EXPOSED]),
           lastcall_ledger._line("{n}A paper-eater owes you his life, and knows you know it.{/n}", requires=[LETTER_KEPT])],
    Requires=["trickster.secret.telmer_tally"], Forbids=[], AnyGroups=[], Tooltip="RRT_Secret"))


# --- Chapter 4: her audience, while she lives ------------------------------------------------------------------------

audience(P + "ch4.read", "An open mind", '[Open your mind to her] "Everyone in this city wants what\'s in my head. You may as well be first."', [
    conv("start", '''{n}Shamira does not move on her throne. The light around her does not so much as flicker. Only her eyes change: they stop looking at you and start looking into you, and the heat of the Harem gathers behind your forehead like a fever coming on.{/n}
"Freely? How novel. Mortals usually make me take it, and then they weep about it for a week." {n}She props her chin on one hand.{/n} "Keep quiet inside, Golarian. I dislike a mind that fidgets."''',
        c("Continue", "war")),
    conv("war", '''{n}It is not like being read. It is like being searched by someone who owns the house: drawers pulled out, letters shaken open, a boot turned over to see what falls from it. Kenabres goes past, burning. A silver dragon falls out of a smoky sky. Drezen's walls, the war tables, a hundred faces you owe something to.{/n}
"The war, the war, the war." {n}Her lip curls.{/n} "Every Golarian I have ever opened is furnished entirely with the war. It is like visiting a man who owns one chair."''',
        c("Continue", "door")),
    conv("door", '''{n}She stops in the middle of you, as if she had found a window left open in a house she had thought was shut.{/n}
"And you let me in. That is the part I cannot get over." {n}She sits up.{/n} "Understand where you are, Golarian. A demon who dies here, in the Abyss, stays dead. No priest calls us back. No judge weighs us. The Abyss is a mouth, and it swallows its own." {n}She considers you.{/n} "And I leave a thread in every mind I open. Just a thread, at the back, where you'd never look. It's how I find a head again when I want it; it's how I'll walk into your dreams tonight, from here, if I feel like it." {n}Her fingers drum the arm of the throne.{/n} "In my court they whisper that a thread like that is a door out of the Abyss's mouth, if the one on the other end holds it open. Nobody I know has lived to say whether it is true. I have always meant to find out, on someone else." {n}Her laughter is low and delighted.{/n} "And you just opened yours to me, in front of my court, for fun."''',
        c('"Is that a threat?"', "dreams"),
        c('"Then I\'ll know where to find you."', "dreams")),
    conv("dreams", '''{n}She goes deeper, idly, the way a bored woman turns the pages of a book she has already decided not to buy, and then she finds something she does like. Her breath catches, very slightly.{/n}
"Your dreams." {n}The word comes out of her slow and warm.{/n} "Crude. Loud. Much too bright. You dream the way children shout in a temple. Did nobody tell you not to dream so loudly in the Abyss? Things come to listen."''',
        c('"Things like you?"', "game"),
        c('"Get out of my dreams."', "game")),
    conv("game", '''"Things much worse than me. I am merely the one sitting closest." {n}She gestures, and the heat behind your eyes eases just enough to let you think.{/n}
"A game, since you came to amuse me. Think of something I cannot find. One thing. Hide it anywhere you like in that cluttered little attic. If I find it, you will admit you are exactly as simple as every other Golarian. If I don't..." {n}She shrugs one shoulder.{/n} "Then I will be surprised. Nobody has surprised me in a very long time."''',
        c("[Think of the war, and nothing else.]", "found_war", flags=(READ, STARTED, THOUGHT_WAR)),
        c("[Think of her. Only her, on her throne, burning.]", "found_her", flags=(READ, STARTED, THOUGHT_HER)),
        c("[Think of moonshine recipes, loudly and in detail, and hide something small under them.]", "recipes",
          mythic="Trickster", flags=(READ, STARTED, HID)),
        # T3 payoff (15b, PP9): appended, so [0]-[2] keep their indices.
        c("[Think of a crate tally a paper-eater once recited, and let her find it.]", "manifest", requires=(NOTES,),
          flags=(READ, STARTED, MANIFEST))),
    conv("found_war", '''"The war. Of course it's the war." {n}She sounds almost disappointed in you.{/n} "You put it in the front of your head and stood in front of it waving. That is not hiding, Golarian. That is showing."
{n}The heat withdraws. She waves you off with two fingers.{/n} "Go. Take your war with you. Try not to die somewhere I can't hear it."''',
        c("[Bow, and leave her to her court.]")),
    conv("found_her", '''{n}For a heartbeat something passes over her face that is not boredom. Then it is boredom again.{/n}
"Everyone thinks of me. It is the first thing anyone does in this room. I did not have to look; I could have smelled it from the door." {n}She lets the heat withdraw slowly, as if she is not in a hurry to be out of you.{/n}
"You burn me a little too brightly, though. Most of them make me softer. Curious." {n}She waves you off.{/n} "Go on. I've seen enough of your attic."''',
        c("[Bow, and leave her to her court.]")),
    conv("recipes", '''{n}She goes looking. She finds mash, and yeast, and the exact proportion of wormwood that makes a Mendevian sergeant cry. She finds a still, and the way to seal its joints with rye dough, and a long argument with yourself about copper. She digs under it and finds more mash.{/n}
"Stop that." {n}Her nails whiten on the arm of her throne.{/n} "Stop thinking about barley at me. Something is under there, I can feel it moving like a mouse under a rug."''',
        c("Continue", "idiot")),
    conv("idiot", '''{n}The heat pulls out of you all at once, like a hand out of cold water. She is smiling, and it is not a pleasant smile, and it is not an entirely unpleasant one either.{/n}
"Either you are an idiot, or you have learned to hide from me, and a mortal who can hide from me in my own Harem is a mortal I will have to kill one day, or keep." {n}She points at the doors.{/n} "Leave. Come back when I have forgotten about you, which will be never. I will find out what was under the barley, Golarian. I always do."''',
        c("[Bow, and leave her to her court.]")),
    # T3 payoff: she finds the tally where the Commander left it. Political leverage in Alushinyrra, not her crystal task
    # (that is Ziforian and the mine, Cue_0122); the servants who would sell her interest are her own canon (Cue_0094 062cb2f1).
    conv("manifest", '''{n}She plucks it out of you like a hair from a sleeve.{/n} "'By Hepzamirah's word, under the Lady in Shadow's seal.' Forty-one sent, forty arrived." {n}Her eyes narrow, and something in them is delighted.{/n}
"Nocticula seals the crates of Baphomet's daughter, and one of them is missing from the tally, if your paper-eater remembered it right. Stolen, diverted, or *given*. I shall enjoy finding out which."
{n}She lets that settle.{/n} "You carried that into my house, and you let me take it. My own servants would have sold it to my enemies before they sold it to me. Either you are a fool, or you are buying me."''',
        c("Continue", "manifest_exposed", requires=(EXPOSED,)),
        c("Continue", "manifest_letter", requires=(LETTER_KEPT,), forbids=(EXPOSED,)),
        c("[Bow, and leave her to her court.]", forbids=(EXPOSED, LETTER_KEPT))),
    conv("manifest_exposed", '''"And you paid for it with the paper-eater's freedom." {n}She finds that too, a little deeper, and laughs.{/n} "He will be telling every cult cook-fire who let him go. So the Abyss will know you trade mercy for paper. How *public* of you."''',
        c("Continue", "manifest_letter", requires=(LETTER_KEPT,)),
        c("[Bow, and leave her to her court.]", forbids=(LETTER_KEPT,))),
    conv("manifest_letter", '''"...And a letter from a paper-eater who thinks you will protect him. On a ration wrapper." {n}Her lip curls, the way a cat's does over something small and still moving.{/n} "How *sweet*. You collect debtors the way I collect secrets."''',
        c("[Bow, and leave her to her court.]")),
], requires=("trickster",), forbids=(READ,))

audience(P + "ch4.bird", "A dream is a bird", '"You said my dreams were loud. What does a demon want with a mortal\'s dreams?"', [
    conv("start", '''{n}Shamira considers the question for so long that the courtiers nearest the throne begin to edge away, in case the answer is them.{/n}
"Want? Nothing. I have a queen who wants nothing she cannot take, a court that wants nothing but my chair, and a city full of sleeping mortals under my windows. I am fed very well, thank you." {n}She examines her nails.{/n} "But you ask what they are. That, I will tell you, because it is the one thing in this city nobody else can."''',
        c("Continue", "sower")),
    conv("sower", '''"Before I was this, I was a sower. I carried dreams down out of Heaven on my wings and dropped them into sleeping heads the way a farmer throws seed: a song into a girl who could not sing yet, a city into a boy who had never seen one. I lit fires in people. That is what I was for."
{n}Her voice has gone quieter. The light around her throne dims with it, as if it were listening too.{/n} "Some of the fires burned too hot. I let them. It was very beautiful to watch."''',
        c("Continue", "bird")),
    conv("bird", '''"A dream is a bird, not a horse. You can't restrain it, you can only hurt it with your reins. My masters wanted reins. I wanted to see how high the birds would fly." {n}She smiles at something you cannot see.{/n} "One of them caught like a wildfire. A dream so bright that making it real took atrocities, and the dreamers did them, one after another, gladly. I could have stopped it with a word. I watched it all the way up instead. And then I did not go home."
"Nocticula found me afterwards, blazing on the black water like a shipwreck. She came out across the sea for me and wrapped me in her shadows, and I have been cool ever since."''',
        c('"And now you eat what you used to sow."', "eat"),
        c('"You miss it."', "miss")),
    conv("eat", '''"Now I taste. There is a difference." {n}She wets her lips, slowly, to show you the difference.{/n} "The demons in this room want my throne every hour they are awake. I read it on them when they bow; that is manners, not a meal. Demons do not dream. The meal is in mortal heads, asleep. Envy tastes of iron. Lust tastes of salt. Yours..." {n}Her eyes narrow.{/n}''',
        c("Continue", "eat_barley", requires=(HID,)),
        c("Continue", "eat_war", requires=(THOUGHT_WAR,), forbids=(HID,)),
        c("Continue", "eat_her", requires=(THOUGHT_HER,), forbids=(HID, THOUGHT_WAR)),
        c("Continue", "chair", forbids=(HID, THOUGHT_WAR, THOUGHT_HER))),
    conv("eat_barley", '''"Yours tasted of burning barley and a dragon falling. I haven't decided if I liked it."''',
        c("Continue", "chair")),
    conv("eat_war", '''"Yours tasted of smoke and a dragon falling, over and over, like a man chewing the same crust. One chair, Golarian. I told you."''',
        c("Continue", "chair")),
    conv("eat_her", '''"Yours tasted of me." {n}She says it lightly, and does not quite manage it.{/n} "Too hot. Much too bright. I haven't decided if I liked it."''',
        c("Continue", "chair")),
    conv("miss", '''"Miss it?" {n}The light around her flares, hot enough that you feel it on your face, and dies back.{/n} "I have not dreamed since I fell, Golarian. Demons don't. We live on other people's. Do not ever again ask me if I miss something. It is the kind of question that ends with me pulling out your tongue to see how it was attached."''',
        c("Continue", "chair")),
    conv("chair", '''{n}A courtier drifts too close to the dais, a thin smiling thing in a silver mask, and Shamira does not look at him. She does not need to. He drifts away again with his hands pressed to his temples.{/n}
"There. That one wants my chair, and so, sometimes, do I. Hers." {n}She says it lightly and watches whether you catch it. When you do, her face does something small and dangerous, a crack in a mask, and closes again.{/n}
"You heard nothing. Nobody hears anything in the Harem."''',
        c('[Flirt] "Walk in my dreams, then. Tonight. See if you like them better from inside."', "invite", flags=(BIRD, INVITED)),
        c('"Stay out of my head, Shamira. I mean it."', "warned", flags=(BIRD, WARNED_OFF))),
    conv("invite", '''{n}She laughs, a real laugh, surprised out of her, and the court goes quiet to hear it.{/n}
"You invite me. Into your sleep. In my own city." {n}She leans forward, and her voice drops to something only you can hear, although her lips have stopped moving.{/n} "I do not walk where I am invited, Golarian. I walk where I like. Sleep, and find out whether I liked it."''',
        c("[Leave, a little warmer than you came.]")),
    conv("warned", '''"No." {n}She says it pleasantly, the way you would decline a second cup of tea.{/n}
"You came into my Harem with a head like a bonfire and you expect me not to warm my hands? Keep your door shut if you can. You can't. Nobody can." {n}She waves you away.{/n} "Now go, before I decide you are rude as well as loud."''',
        c("[Leave her to her court.]")),
], requires=("trickster", READ), forbids=(BIRD,), delay=8)

page(P + "ch4.first_taste", "Someone in the dream", [
    nar("sleep", '''{n}You dream of Kenabres again. You always dream of Kenabres: the square, the smoke, the dragon coming down out of the sky with her wings on fire, and your own legs refusing to run.{/n}
{n}Tonight there is someone else in the square. A red-haired woman sits on the lip of the dry fountain with her legs crossed, watching the dragon fall the way a noblewoman watches a play she has paid too much for.{/n}''',
        c("Continue", "critic", requires=(INVITED,)),
        c("Continue", "uninvited", forbids=(INVITED,))),
    sh("uninvited", '''"You told me to stay out." {n}She does not turn her head. She sounds pleased with herself, the way a cat sounds pleased on a forbidden cushion.{/n} "You told me in my own Harem, in front of my court, as if I were a dog you could send off a bed. So I waited until you were asleep, where your telling is worth nothing." {n}She finally looks at you.{/n} "Don't sulk. You would have let me in eventually. Everyone does."''',
        c("Continue", "critic")),
    sh("critic", '''"Is this the one you have every night?" {n}She does not get up. The ash falls around her and does not touch her.{/n} "It's badly staged. The dragon falls too slowly. You keep the sky too red, as if you're afraid I won't notice it's a tragedy. And you, standing there, rooted to the spot." {n}She tilts her head.{/n} "Dreamers always root themselves. It is the first thing I used to cut."''',
        c('"This isn\'t yours to fix."', "fix"),
        c('"Then fix it."', "fix")),
    sh("fix", '''{n}She lifts one finger, and the dream shifts. The smoke thins. The dragon's fall slows until she hangs in the air like a banner, wings spread, every scale lit. And your feet come loose from the stones.{/n}
"There. Now you can run, or you can stand and watch, and it will be your choice either way." {n}The ghost of a smile.{/n} "That is all a dream wants, Golarian. A choice. I used to give them away by the thousand."''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake with a taste of cinders and cinnamon in your mouth and your heart going too fast. The tent is dark. Nobody is there.{/n}
{n}For the rest of the day you catch yourself looking at red-haired women in the camp. None of them is her. All of them, for a moment, are.{/n}''',
        c("[Get up. There's a war.]", flags=(TASTED,))),
], requires=("trickster",), forbids=(TASTED, KILLED), delay=12, chapters=(4,), RequiresAnyGroups=[[INVITED, WARNED_OFF]])


# --- Chapter 5: the setup at Socothbenoth's briefing (physical, inline; he speaks) ------------------------------------

SCENES.append(scene(P + "killed.setup", "What's left of her", "Shamira", 5,
    '[Touch your temple] "Her essence goes in your cauldron. What happens to the rest of her?"', [
    conv("rest", '''{n}Socothbenoth blinks his black eyes at you, twice, as if you had asked him where the sun goes at night.{/n}
"The rest? The rest of Shamira? Oh, darling. Nothing happens to the rest of her. That is rather the point." {n}He waves a hand, and his rings clatter.{/n} "Demons who die at home stay dead. The Abyss is a mouth; it chews and it swallows and it does not give back. The Nirvana goes in my cauldron, the rest goes down the Abyss's throat, and my sister sleeps alone for once in an age. Delicious."''',
        c("Continue", "her_words", requires=(LET_IN, READ)),
        c("Continue", "never_in", forbids=(LET_IN,)),
        c("Continue", "her_native", requires=(LET_IN,), forbids=(READ,))),
    n("her_words", "Narrator", '''{n}"The Abyss is a mouth, and it swallows its own." You have heard it before, or something very like it, in her Harem, with the heat of her behind your forehead and the whole court watching.{/n}
{n}And you have felt it since: something left at the back of your head where she was, fine as a hair. On bad nights it tugs, the way a line tugs when something on the far end turns over in its sleep. She has been in your head. There is a thread in you tied to her. A dying thing goes for the nearest door it knows, and holds on to whatever line it has.{/n}''',
        c('"She\'s been inside my head, Socothbenoth. She knows the way. What if I leave that door open while I kill her?"', "open", flags=(PRIMED, STARTED)),
        c('[Keep it to yourself] "Just curious."', abort=True)),
    n("her_native", "Narrator", '''{n}She has been in your head. You let her in, in her Harem, in front of her court: she went through you like a hand through a drawer, and took what she came for, and went.{/n}
{n}Not all of her went. On bad nights something tugs at the back of your head, fine as a hair, the way a line tugs when something on the far end turns over in its sleep. Nobody has told you what it is. You can guess. And if the Abyss swallows its own, a thing that dying might reach for the nearest door it already knows; that is your guess too, and nothing more.{/n}''',
        c('"She\'s been inside my head, Socothbenoth. She knows the way. What if I leave that door open while I kill her?"', "open", flags=(PRIMED, STARTED)),
        c('[Keep it to yourself] "Just curious."', abort=True)),
    n("never_in", "Narrator", '''{n}She has never been in your head. Not freely. You kept her out, or she never asked, or she took what she wanted by force and went away again. There is no door in you that she knows.{/n}
{n}But a door can be opened from the inside. You could open one now, and keep it open through the fight, for a woman who will know, the moment she looks in, exactly what you have come to do.{/n}''',
        c('"What if I open my head to her, and keep it open while I kill her? Somewhere for the rest of her to go."', "blind", flags=(PRIMED, STARTED, OPENED_BLIND)),
        c('[Keep it to yourself] "Just curious."', abort=True)),
    conv("blind", '''{n}For a moment the Silken Sin says nothing at all, which you did not know he could do.{/n}
"Open your mind. To Shamira. Now, of all times. While you kill her." {n}He presses his hands to his chest.{/n} "Darling, she reads minds the way I read the tailors' bills. She will look in, and see the knife, and see the plan, and see you, and she will come in through that door with everything she has left, all at once, like a drowning woman up a rope. It may not be only the rest of her that comes in. It may be the whole of her, and angry." {n}He beams.{/n} "If she tears you open, darling, do try to keep your eyes open. I want the whole story."''',
        c("Continue", "carpets")),
    conv("open", '''{n}For a moment the Silken Sin says nothing at all, which you did not know he could do.{/n}
"You'd let her in. On purpose. While she's dying, and furious, and knows exactly whose hand did it." {n}He presses his hands to his chest.{/n} "I send you to fetch my sister's favourite toy's heart in a cauldron, and you plan to bring the toy home as well, inside your own skull, for company. Oh, you are wasted on Golarion. You are wasted on the whole Material Plane."''',
        c("Continue", "carpets")),
    conv("carpets", '''{n}Then he frowns, as prettily as he does everything.{/n} "One tiny problem. My spells keep you hidden from my sister's eyes and ears. They don't do a thing for the inside of your head. If you leave a door open in there, Shamira will look through it. If she sees 'I am here to kill you and keep the leftovers', she will kill your friends first to make a point."
"So. Think of anything but the plan. Carpets. Carpets are marvellous; my sister has hideous ones. Keep the door open at the back, where she won't look until she has to."''',
        c("Continue", "hid", requires=(HID,)),
        c("Continue", "story", forbids=(HID,))),
    conv("hid", '''"You've hidden from her before? Under what? No, don't tell me. Just remember it. Whatever you put on top of the thought last time, put twice as much on it this time. She'll be fighting for her life. Nothing reads a room like a woman fighting for her life."''',
        c("Continue", "story")),
    conv("story", '''"And afterwards, I want to hear about it. Every detail. In the closet." {n}He is already enjoying it.{/n} "Or you'll come back with a stranger in your head and no story at all, and I will have to make one up, and mine are always filthier."''',
        c('"While you\'re lending me spells: I\'ll need one more closet. Into the Fleshmarkets."', "market"),
        c('"And the closet you\'re lending me. How does that work, exactly?"')),
    conv("market", '''"The Fleshmarkets!" {n}He actually sways.{/n} "Where do you think sinful silks come from, darling? I keep a wardrobe by the bone-carvers' stalls, and under the last stall is Ramisa's hothouse. Ramisa Sloughed Skin, the marilith who only ever shows up as a picture of herself. She grows her custom orders down there in the dark, the way she used to grow her screaming little plants: planted in something dead, and watered, until they sit up." {n}He studies you.{/n} "A voice in your head is a lodger. A voice in a body is a guest. You want a guest."''',
        c('"I want a body nobody will miss."', "veil"),
        c('"I want to see what your wardrobe looks like."', "veil")),
    conv("veil", '''"Then you'll have my veil for that too. The same spell. It keeps you hidden from eyes and ears. Mind her mandragoras; I never could do anything about plants." {n}He lays two fingers on your forehead, and they are cold and smell of violets.{/n}
"Go through your own wardrobe in Drezen to my Council, and through my Council to my house in the city, the way I came to you with my closet on my back. Steal something beautiful. And bring me back the story."''',
        c('"And the closet you\'re lending me for tonight. How does that work, exactly?"', flags=(VEIL,))),
], requires=("trickster", PLAN), forbids=(PRIMED, KILLED, MADE_ROOM), last=5, Relationship=REL, Chapters=[5],
    AnswerLists=[BRIEFING], NativeReturnCue=BRIEFING_RETURN, EntryMythic="PlayerIsTrickster"))


# --- The return: her first words, at Socothbenoth's closet (physical, inline), or its letter twin ---------------------

def voice_nodes(place):
    """Her first words after the kill. `place` is "closet" (Socothbenoth peeks out and speaks) or "letter" (a rest)."""
    closet = place == "closet"
    opening = (conv("start", '''{n}Socothbenoth peeks out of his closet with his hair in his eyes, sees your face, and stops mid-grin.{/n}
"You have it? You have it! Give it... wait. Why are you holding your head like that? You look like a man with two hangovers."''',
                    c("Continue", "heavy"))
               if closet else
               nar("start", '''{n}You handed Socothbenoth the cauldron, you sat through his Council, and you came home, and all the way home you did not think about the boudoir once. You thought about carpets.{/n}
{n}Tonight, lying in the dark, you stop thinking about carpets, and something in your head that has been holding very still begins to move.{/n}''',
                   c("Continue", "heavy")))
    heavy = nar("heavy", '''{n}There is a second heartbeat behind your eyes. It has been there since the boudoir, you realise, keeping perfectly in time with yours so that you would not notice it. Now it falls out of step.{/n}
{n}Something at the back of your head, where you left the door open, turns over like a sleeper, and there is a smell in your nose that is not in the room: cinders, and cinnamon.{/n}''' if closet else
                '''{n}There is a second heartbeat behind your eyes, and it falls out of step with yours. There is a smell in the room that nothing in the room could make: cinders, and cinnamon.{/n}''',
                c("[Listen.]", "moment"))
    moment = nar("moment", '''{n}And now you remember the instant she fell, the one you would not let yourself think about in the boudoir.{/n}
{n}Under the carpets, at the back of your head, something went taut, like a line when a fish takes the hook. You did not pull. You did not let go. You held the door open the way you had told Socothbenoth you would, and something came up the line into you, hot and fast and furious, and settled, and kept perfectly still, so that you would not notice it until you were home.{/n}''',
                c("Continue", "voice"))
    voice = sh("voice", WHISPER + '''"Carpets."
{n}The voice is hers, and it is coming from inside your own skull, and it is shaking with a rage so complete that it has gone quiet.{/n}
"The whole fight. I was tearing at your friends with everything I had, and I reached into your head for your plan, and all I could find was carpets. My lady's carpets. You thought about the pattern." {n}The heat behind your eyes rises.{/n} "And then I was dying, and there was a door open at the back of you, the door I already knew, and I went through it before I could think. I have never in my existence done anything before I could think."''',
        c("Continue", "hid_before", requires=(HID,)),
        c("Continue", "blind_before", requires=(OPENED_BLIND,), forbids=(HID,)),
        c("Continue", "cold", forbids=(HID, OPENED_BLIND)))
    hid_before = sh("hid_before", '''"You hid from me once before. Under barley. In my own Harem. I let you, because I was curious what a mortal could keep from me." {n}A sound like a fingernail drawn down glass, somewhere under your skull.{/n} "Look where curiosity put me. Behind the eyes of the clown who killed me."''',
        c("Continue", "cold"))
    blind_before = sh("blind_before", '''"You never let me in. Not once. You threw me out of your head in my own Harem, or you never came, and then tonight, with a knife in your hand, you opened a door I had never seen and held it open while I died." {n}The heat behind your eyes is almost unbearable.{/n} "I saw the knife through it. I saw the plan. I came through anyway. I tore half your hallway down coming in, and I am not sorry."''',
        c("Continue", "cold", flags=(READ_ALL,)))
    cold = sh("cold", '''"And I am cold." {n}She says it as if it is the worst thing, worse than dead.{/n} "Do you understand? I have been warm since before your world had a name. My fire came down out of Nirvana with me. It was the last thing of Heaven I kept, and I kept it out of spite." {n}Silence.{/n} "It's in his diamond now. I felt it go. The cauldron pulled the fire out of me like a thread out of a hem, and whatever was left over came through your door. Whatever was left over is me."''',
        *((c("Continue", "socoth"),) if closet else NOCT_OR_CHOOSE))
    socoth = conv("socoth", '''{n}Socothbenoth has come all the way out of the closet. He is staring at your face with his hands clasped under his chin, like a child at a sweetshop window.{/n}
"Is that her? Is that Shamira? In there?" {n}He leans in and sniffs at your ear.{/n} "Oh, it is. You smell of her from the inside, like a room somebody has been smoking in. My cauldron has her fire, and you have the sulk that went with it." {n}He dabs at an inky tear.{/n} "Nobody has ever given me a better present, and it isn't even for me."''',
        *NOCT_OR_CHOOSE)
    choose = sh("choose", '''"So. You have me." {n}The second heartbeat pulses, once, like a heart deciding whether to go on.{/n} "Say why. And choose your words, Golarian. I can hear the ones you don't say, and I will know which of them you meant. I am standing right behind them."''',
        c('"I killed you because he asked, and because I needed his Council. I kept you because I don\'t like waste."', "honest", flags=(RETURNED, FOUND, STARTED, HONEST)),
        c('"You\'re alive, more or less. Behave, and I\'ll find you a body."', "bargain", flags=(RETURNED, FOUND, STARTED, BARGAIN)),
        c('[Push her into the back of your head and shut the door] "You were a better steward than you\'ll be a conversation. Stay back there. Be quiet."', "kept",
          flags=(RETURNED, FOUND, STARTED, KEPT, CLOSED), alignment=("Evil", 1)))
    honest = sh("honest", '''{n}Silence. Then, of all things, a laugh: short, cracked, and real.{/n}
"Waste." {n}She tastes the word.{/n} "You murdered me on a demon lord's errand and kept the leftovers because it offended your sense of economy. That is the most honest thing anyone has thought at me in centuries, and I can see all the way to the bottom of it. There is nothing under it. Not even pity." {n}Her voice drops.{/n} "Good. I would have hated pity."''',
        c("Continue", "after"))
    bargain = sh("bargain", '''"Behave." {n}The word comes back at you twice as cold.{/n} "I have had queens tell me to behave, and gods, and once a solar with a sword the size of your house. I behaved for none of them." {n}The heat behind your eyes flickers.{/n}
"But a body. Yes. Find me a body. A good one. Not a corpse: I will not wear rot. Not a crusader: they pray in their sleep and I can't bear the noise. Find me something worthy of me, and then we will talk about behaving."''',
        c("Continue", "after"))
    kept = sh("kept", '''"Oh, don't you d..." {n}You push. It is like shutting a door on a draught: there is resistance, and a howl, and then a click. The second heartbeat goes on at the back of your head, faster, angrier, and then settles into a slow sullen beat under your own.{/n}
{n}From very far back, through a door you will never open again, one word:{/n} "...taste."''' + (
        '''
{n}Socothbenoth claps, slowly, delighted.{/n}''' if closet else ""),
        c("[Leave her there.]"))
    after_closet = conv("after", '''{n}Socothbenoth wipes his eyes on his sleeve.{/n} "I'm going to tell everyone. No. I'm not going to tell anyone. It's funnier if nobody knows." {n}He looks at you slyly.{/n} "Think quietly in my Council, darling. Some of my brother Council members can hear a thought across a room, and some of them would pay a great deal for a piece of the Ardent Dream."
{n}Then, brightly:{/n} "Now. Do you have my cauldron?"''',
        c('"About that closet into the Fleshmarkets..."', "market", forbids=(VEIL,)),
        c("[Say nothing.]"))
    market = conv("market", '''"Oh! A body for her!" {n}He sways.{/n} "Ramisa's hothouse, darling, under the bone-carvers' stalls. Sloughed Skin grows her custom orders down there in the dark, planted in something dead and watered until they sit up. Go through your own wardrobe to my Council, through my Council to my house in the city, and down." {n}Two cold fingers on your forehead, smelling of violets.{/n} "My veil, for the stealing. Mind her mandragoras. Bring me the story."''',
        c("[Say nothing.]", flags=(VEIL,)))
    after_letter = nar("after", '''{n}The second heartbeat goes on beside yours in the dark. After a while its warmth is the only warm thing in the room, and you fall asleep with it, the way you would fall asleep beside someone.{/n}''',
        c("[Sleep.]"))
    nodes = [opening, heavy, moment, voice, hid_before, blind_before, cold]
    if closet:
        nodes.append(socoth)
    nodes += [noct_node(), choose, honest, bargain, kept]
    nodes += [after_closet, market] if closet else [after_letter]
    return nodes


NOCT_OR_CHOOSE = (c("Continue", "noct", requires=(NOCT_KNOWS,)), c("Continue", "choose", forbids=(NOCT_KNOWS,)))


def noct_node():
    """What she heard after the kill, when Nocticula smelled her in the Commander in the boudoir (Nocticula's
    court.shamira); otherwise the scene goes straight to her question."""
    return sh("noct", '''"And I heard her." {n}Her voice has changed. It is not quieter; it is thinner, the way ice is thinner in the middle of a lake.{/n} "My lady. After. You stood in her audience chamber with me behind your eyes, and she smelled me on you, and she bent close enough that I could feel her through your skin, and she said hello."
"Hello. The way you would greet a dog in a kennel." {n}A breath with no lungs behind it.{/n} "And then she thanked you. You had saved her the trouble."''',
        c("Continue", "choose"))


VOICE_REQUIRES = ("trickster.ever", KILLED, PRIMED)
SCENES.append(scene(P + "killed.voice", "Someone behind your eyes", "Shamira", 5,
    '[Put a hand to your head. There is a second heartbeat in it.] "Wait. Before we go anywhere."', voice_nodes("closet"),
    requires=VOICE_REQUIRES, forbids=(FOUND, SOCOTH_GONE), last=5, Relationship=REL, Chapters=[5],
    AnswerLists=[CLOSET], NativeReturnCue=CLOSET_RETURN, TricksterDevice=True, TricksterState="killed"))

page(P + "killed.voice_letter", "Someone behind your eyes", voice_nodes("letter"),
     requires=VOICE_REQUIRES + (HANDED,), forbids=(FOUND,), delay=12, TricksterDevice=True, TricksterState="killed")


# --- The late road: killed with no door left open. She is drowning in the Commander's head by the first rest -------------

page(P + "killed.drowning", "Someone drowning", [
    nar("start", '''{n}You come back from the boudoir with the cauldron full and the Council waiting, and you do everything a victorious clown does. You do not notice anything wrong until you lie down.{/n}
{n}Then there are two heartbeats in your head, and one of them is not yours.{/n}''',
        c("Continue", "drowning")),
    sh("drowning", WHISPER + '''"...door, a door, where is the..."
{n}It is her voice, and it is not speaking to you. It is the voice of someone going under in black water, grabbing at anything. It grabs at your memories. Kenabres tears in your head like wet paper. Your mother's face comes loose and floats away and comes back wrong.{/n}
"Let me in, let me in, there's no room, let me..."''',
        c("Continue", "why_known", requires=(LET_IN,)),
        c("Continue", "why_killer", forbids=(LET_IN,))),
    sh("why_known", '''{n}She finds the edges of herself for a moment and holds on.{/n} "You. Of course it's you." {n}Every word costs her something; you can feel the cost in your own teeth.{/n} "When I fell, there was no door open in that room. Only one mind I had ever been let into. I went for it like a drowning woman goes for a spar, and it was shut, and I got in anyway, round the edges, like water."
"I can't stay like this. A live head with its doors shut pushes me out with every breath, and when I go out, the Abyss will have me."''',
        c("Continue", "choose")),
    sh("why_killer", '''{n}She finds the edges of herself for a moment and holds on.{/n} "You. The one with the knife." {n}Every word costs her something; you can feel the cost in your own teeth.{/n} "I was never inside you. I didn't know the way. But your hand was on me when I died, and your mind was the closest, and I went into it the only way there was: through the wound."
"I can't stay like this. A live head with its doors shut pushes me out with every breath, and when I go out, the Abyss will have me."''',
        c("Continue", "choose")),
    nar("choose", '''{n}You can feel it: a pressure behind your eyes like a held breath, a woman clinging to the inside of your skull by her fingernails, and your own mind, without asking you, pushing her away the way a body pushes out a splinter.{/n}
{n}You could stop pushing. You do not know what it will cost. You know she will go through everything in you on her way in, because she has no choice, and neither will you.{/n}''',
        c("[Stop pushing. Make room.]", "in", flags=(RETURNED, FOUND, STARTED, MADE_ROOM, LATE, READ_ALL)),
        c("[Keep pushing, and let her go under.]", "gone", flags=(DECLINED, CLOSED))),
    sh("in", '''{n}You let go, and she comes in: not through a door but through everything at once, a heat and a taste of cinders and cinnamon, down the back of your throat and up behind your eyes, and you are on your knees on the floor of the tent with your hands over your face. It takes a long time. It hurts in places that have no names.{/n}
"Less of me." {n}Her voice, thin and furious, from somewhere that is suddenly settled.{/n} "Bits of me went down that throat on the way. Some song. Some face. I don't know which." {n}A pause.{/n} "And I have been through every room in your head, Golarian. Every one. I know what you did to get here. I know what you haven't told anybody."''',
        c("Continue", "in_end")),
    sh("in_end", '''"Find me a body, clown. Find it fast. And never, ever again, leave a door shut that I might need." {n}The second heartbeat steadies beside yours.{/n} "Now sleep. You look like something I would have put out of its misery."''',
        c("[Sleep.]")),
    nar("gone", '''{n}She goes. You feel her go: not like a door closing but like a hand letting go of a rope. The second heartbeat stops. Kenabres settles back into place in your head, a little crooked, and your mother's face comes back almost right.{/n}
{n}Somewhere very far down, something swallows.{/n}''',
        c("[Lie back down.]")),
], requires=("trickster", "trickster.ever", KILLED), forbids=(PRIMED, FOUND, MADE_ROOM, DECLINED, "trickster.failed"), delay=0,
    TricksterDevice=True, TricksterState="cold")


# --- Reactions (05 §3.1 row 37: Shyka, Socothbenoth, Arueshalae). Socothbenoth speaks inside the setup and the first words;
# the Daeran, Regill and Woljif reactions of the first build are retired by gating (the barracks witness is folded into her
# own event, mind.barracks_after), never deleted. ------------------------------------------------------------------------------

ARUESHALAE = ("arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out", "arueshalae.kicked_out_evil")
# G6(b): an Arueshalae who died and came back on her own Trickster road is present again (her death flag stays set).
A_BACK = {"arueshalae_dead": "arueshalae.trickster.returned", "arueshalae.evil_dead": "arueshalae.trickster.returned"}
DAERAN = ("daeran.dead", "daeran.kicked_out")
WOLJIF = ("woljif.dead", "woljif.kicked_out")
REGILL = ("regill.dead", "regill.kicked_out", "regill.left_plot")

SCENES.append(reaction("Shyka", P + "react.shyka", ("trickster.ever", RETURNED),
    '''{n}Shyka turns the glowing diamond in their fingers, then lets their eyes drift, unhurried, to your face, and a little behind it.{/n}
"The Nirvana is all here. We checked; we always check. And the rest of her is there, looking out at us." {n}A small, many-voiced smile, aimed not quite at you.{/n} "Good evening, Lady Shamira. We have never been introduced. You will forgive us if we do not shake hands." {n}Then, to you, as if nothing had happened:{/n} "Shall we go on?"''',
    answer_list=SHYKA_LIST, forbids=("shyka.gone",), chapter=5, last=5, entry="[Let Shyka look at you, and at whoever is looking out.]",
    NativeReturnCue=SHYKA_RETURN))

SCENES.append(reaction("Arueshalae", P + "react.arueshalae_inside", ("trickster.ever", RETURNED, "shamira.saw_arueshalae"),
    '''{n}Arueshalae will not meet your eyes across the fire. When you ask, she laughs, not very well.{/n}
"You have Shamira in there. Behind your eyes. I can feel her looking out; every succubus in Alushinyrra knows that look. When she saw me with you in her throne room she told the whole court I'd fallen low." {n}She hugs her knees.{/n} "She isn't asleep in there. She's listening. She always listened hardest when she looked bored. Just... count your thoughts after you talk to her. All of them."''',
    answer_list=ARUESHALAE_HUB, forbids=(EMBODIED, CLOSED) + ARUESHALAE, chapter=5, last=5, ForbidOverrides=A_BACK,
    entry='"You won\'t look at me."'))

SCENES.append(reaction("Arueshalae", P + "react.arueshalae_inside_unseen", ("trickster.ever", RETURNED),
    '''{n}Arueshalae will not meet your eyes across the fire. When you ask, she laughs, not very well.{/n}
"You have Shamira in there. Behind your eyes. I can feel her looking out; every succubus in Alushinyrra knows that look. I grew up under her court. She had girls flayed for looking at her too long." {n}She hugs her knees.{/n} "She isn't asleep in there. She's listening. She always listened hardest when she looked bored. Just... count your thoughts after you talk to her. All of them."''',
    answer_list=ARUESHALAE_HUB, forbids=(EMBODIED, CLOSED, "shamira.saw_arueshalae") + ARUESHALAE, chapter=5, last=5, ForbidOverrides=A_BACK,
    entry='"You won\'t look at me."'))

SCENES.append(reaction("Arueshalae", P + "react.arueshalae_walking", ("trickster.ever", EMBODIED),
    '''"She's out. I can feel it." {n}Arueshalae touches the black pearl at her throat without seeming to notice.{/n} "Everyone who grew up in that city can feel it, the way you feel a storm in a bad knee. The Ardent Dream is walking around again in a body she didn't grow."
{n}She looks at you, and her face does something complicated.{/n} "And she comes back every night, doesn't she. Into your sleep. I can smell her on you in the mornings." {n}She looks away.{/n} "I used to pray to be left alone in my dreams. I hope you didn't give that away cheaply."''',
    answer_list=ARUESHALAE_HUB, forbids=ARUESHALAE, chapter=5, last=6, entry='"Something on your mind?"', ForbidOverrides=A_BACK))

SCENES.append(reaction("Daeran", P + "react.daeran_sleep", ("trickster.ever", NEVER_ALONE),
    '''{n}Daeran swirls his wine and considers you over the rim with frank, delighted clinical interest.{/n}
"You talk in your sleep now, my dear. Everyone in the corridor has heard it. And every night, somebody answers you. A woman. Very bored, very rude, and I know the voice." {n}He sips.{/n} "I stood in her throne room in Alushinyrra while she told us her life story, and I called it a bad novel, to her face. I should like to revise my review. It appears to have a sequel, and I am living next door to it."''',
    answer_list=DAERAN_HUB, forbids=DAERAN + (EMBODIED,), chapter=5, last=6, entry='"You\'re staring at me, Daeran."'))

SCENES.append(reaction("Regill", P + "react.regill_barracks", ("trickster.ever", BARRACKS),
    '''{n}Regill has a report on his knee and does not look up from it.{/n} "The north barracks. Two hundred men. Their drill is perfect and their sergeants have nothing to report, and that is my report." {n}He turns a page.{/n} "Men in a war complain, Commander. They gamble, they fight, they dream aloud and wake their bunkmates. These have stopped. All at once, on one night, the night you stood in their doorway until dawn." {n}Now he looks up.{/n} "I have not written down where you were standing. I will, if I am asked."''',
    answer_list=REGILL_LIST, forbids=REGILL + (FUEL,), chapter=5, last=6, entry='"You have something to report, Regill."'))

SCENES.append(reaction("Woljif", P + "react.woljif_voice", ("trickster.ever", RETURNED),
    '''"Boss. Boss. You been talkin' to yourself." {n}Woljif has taken a whole step back from you, cup and all.{/n} "Not like normal folk do. In two voices. And one of 'em, when I got close, said inside my head, 'Try to pick that pocket and I'll make you dream of your mother'."
{n}He is not joking. His tail has gone round his leg.{/n} "Boss, last time a demon talked inside somebody's head around me, it was Voetiel, and it was about my soul. I know what it sounds like when one of 'em's moved in. Whatever you got in there, you ask it nice to stay out of mine."''',
    answer_list=WOLJIF_HUB, forbids=(EMBODIED, FOUND) + WOLJIF, chapter=5, last=5, entry='"Something wrong, Woljif?"'))


# --- Epilogue pages (ordered siblings; read-only) -------------------------------------------------------------------

EPI = "ShamiraEpilogue"


ALIVE_AFTER = "trickster.commander_back"   # native Trickster survival or Last Call's bottle


def epilogue(id, text, requires, forbids=(), paragraphs=(), living=True):
    """living: the page narrates the Commander's life after the war, so it Forbids sacrifice unless the Commander came back."""
    extra = dict(ForbidOverrides={"sacrifice": ALIVE_AFTER}) if living else {}
    SCENES.append(scene(P + "epilogue." + id, "", EPI, 6, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=tuple(forbids) + (("sacrifice",) if living else ()),
                        last=6, Relationship=REL, **extra))


SHELL_PARAGRAPHS = (
    p('''{n}She wore the stolen body with a thin white seam across the collarbone where the last root had torn it on the way out of the earth. Everything else about that body she shaped as she pleased; the seam would not shape, as she had known the morning she woke. So she cut her gowns to show it, and let the court call it a duelling scar, and killed the three who believed it.{/n}''', requires=(TORN,)),
    p('''{n}Ramisa Sloughed Skin told the story of the theft at every sale for a hundred years, with names, as she had promised: the clown who stole a body from her garden for the woman the clown had killed. It became her favourite. It sold a great many bodies. Shamira never forgave her for it, and never managed to find where she was hiding.{/n}''', requires=(RAMISA_STORY,)),
    p('''{n}Ramisa Sloughed Skin sent Socothbenoth a bill for the tall woman with the long hands every season for the rest of his existence, and he paid none of them, because he had never ordered her, and she never once believed him.{/n}''', requires=(RAMISA_FOOLED,)),
    p('''{n}There had been less of her after the Commander's head than before. Nobody who had known her could have said what was missing: a song, perhaps, or a face she had once loved. She could not say either. It was the only thing she was ever afraid of.{/n}''', requires=(LATE,)),
)

epilogue("kept", '''{n}The chroniclers of the Fifth Crusade agree that Shamira the Ardent Dream died in the Lady in Shadow's own bedchamber, at the hand of the Commander, and that her essence burned in the syphon at Threshold with everything else it held. The chroniclers did not look behind the Commander's eyes.{/n}
{n}Nobody could say, afterwards, when a red-haired woman had first been seen in the Harem of Ardent Dreams again. Only that she wore the room as if it had never been emptied.{/n}''',
    requires=(EMBODIED, COMMITTED), forbids=(CLOSED,), paragraphs=(
        p('''{n}On the night before the rift she came into the Commander's sleep as she always did, and for once she did not warm her hands. "Come out of the hole, clown," she said, in the throne-room voice, and under it something that was not. "I have already died of one trick this year. I will not lose you to a hole in the ground. It would be a very poor joke, and you are not allowed to tell poor jokes. Not to me." Then she sat down at the edge of the dream and did not leave it until the drums.{/n}'''),
    ) + SHELL_PARAGRAPHS + (
        p('''{n}The light around her throne was dimmer than it had been, and did not wither anyone who looked at it. Her court learned to look.{/n}''', forbids=(BARRACKS,)),
        p('''{n}Wherever the Commander slept, Shamira knew the way in. She came for the warmth that kept her stolen body alive, and watched every door for signs that it might close against her. The Commander could ask for a night alone. She had made the price plain.{/n}'''),
        p('''{n}She kept to the edge of the Commander's dreams, her back turned as she had been told. By noon her hands were cold. She showed them at court, and let everyone wonder who had made the Ardent Dream pay so dearly for her body.{/n}''', requires=(P + "terms.edge",)),
        p('''{n}The light around her throne came back brighter than anyone remembered, fed on a barracks of Mendevian soldiers who never dreamed again, and it withered whatever looked at it, as it always had. Of the men of that barracks, eleven deserted within the year, two hanged themselves, and one became a very great painter, and none of them could have said why.{/n}''', requires=(BARRACKS,)),
        p('''{n}She never stopped wanting her lady's throne. The Commander never helped her take it, and never tried to stop her, and stood where she could see, which was all she had asked.{/n}''', requires=(STAND,)),
        p('''{n}She wanted her lady's throne all her life, and the Commander told her to her face that no help would come from that quarter, not against Nocticula. She sulked for a decade, in public. In private she wrote letters in her own hand to names the Commander never asked about, and the wax on the Harem's wine-jars was never the same colour twice. She stayed.{/n}''', requires=(NOT_NOCT,)),
        p('''{n}The Commander once told her, with a perfectly straight face, that of course they would help her take the Midnight Isles. She laughed until the Harem shook. Nobody in the Abyss had ever lied to her so badly, or so fondly.{/n}''', requires=(LIED_HER,)),
        p('''{n}The Lady in Shadow knew. She had known since the night she bent close to the Commander in her audience chamber and said hello to what was looking out. She never said a word to her steward about it, and her steward never asked what she knew, and the whole city watched the two of them not asking with enormous enjoyment.{/n}''', requires=(NOCT_KNOWS,)),
        p('''{n}The captain of the north postern kept his post to the end of the war and sold the templars of the Ivory Labyrinth a door every week, and every door was a wall of crossbows. His daughter came home in the second spring, in an exchange he had arranged himself. He never knew who had written his lists for him. Shamira always said it was the best joke she had ever been part of.{/n}''', requires=(P + "spy.turned",)),
        p('''{n}The captain of the north postern lived out the war, and a long life after it, a dull, loyal, careful man who never dreamed and never wondered why.{/n}''', requires=(P + "spy.fed",)),
        p('''{n}The chaplains of the crusade never forgave the Commander for the north barracks. They never said so; they only stopped praying aloud when the Commander walked into a room.{/n}''', requires=(P + "barracks.told",)),
        p('''{n}In the Harem of Ardent Dreams the Commander was always her fool: bowed in, bowed out, never assassinated, because nobody in the Abyss kills a joke. The Commander had to be funny every visit for the rest of {mf|his|her} life. It was, by general agreement, the hardest duty of the Fifth Crusade.{/n}''', requires=(P + "court.fool",)),
        p('''{n}In the Harem of Ardent Dreams the Commander was always her guest, who drank her wine without asking, and whom she had not yet killed. The court of Alushinyrra speculated about it for a hundred years and never once came near the truth.{/n}''', requires=(P + "court.guest",)),
        p('''{n}In the Harem of Ardent Dreams the Commander stood at her right hand, where a steward stands, where a lover stands, and Alushinyrra knew exactly what it was looking at, and was afraid of it.{/n}''', requires=(P + "court.equal",)),
        p('''{n}They say the throne of the Midnight Isles stood empty after the war, with its mistress somewhere in the shadows. They say Shamira sat in it, once, alone, at night, and got up again before morning, and never told anyone how it had felt.{/n}''', requires=(NOCT_HIDING,)),
    ))

epilogue("late", '''{n}The war ended before the Ardent Dream could finish her game. She came to the Commander's window a month after Threshold with her red hair full of the smell of the Abyss and sat on the sill with her legs crossed, and said that she was owed a round, and that she had come to win it.{/n}
{n}She won it. The Commander did not even try to hide her; she went through that head room by room and found herself in every one, and said afterwards that it was the least sporting victory of her long life, and the best. Nobody asked the Commander why a chair in the corner of the bedroom was always turned to face the wardrobe.{/n}''',
    requires=(LATE_COMMITTED, EMBODIED), forbids=(COMMITTED, CLOSED, ALLY), paragraphs=SHELL_PARAGRAPHS)

epilogue("ally", '''{n}Shamira the Ardent Dream went back to her city after the war in a body the Commander had stolen for her, and sat her throne in the Harem of Ardent Dreams as if she had never been dead.{/n}
{n}She had lost one game in her life that she had meant to win, and she never played it again with anyone. She still came into the Commander's sleep every night, because the body would not live without it, and she sat at the far edge of every dream with her back turned, and never once looked round. She paid her debts exactly, and not one favour more.{/n}''',
    requires=(EMBODIED, ALLY), forbids=(COMMITTED,), paragraphs=(
        p('''{n}On the night before the rift she spoke in the Commander's sleep for the first time since the game. "You won. I said I would never ask you anything again, and I won't. This isn't asking. This is telling. Come back out of the hole, Golarian. I owe you a life, and I pay my debts, and I can't pay a corpse."{/n}'''),
    ) + SHELL_PARAGRAPHS)

epilogue("closed_door", '''{n}Shamira the Ardent Dream went back to her city after the war in a body the Commander had stolen for her, and never spoke the Commander's name again. The Commander had shut a door on her in her own Harem. In the Abyss, some things are forgiven. That is not one of them.{/n}
{n}She still came into the Commander's sleep every night; the body would have died without it. She never said a word there, either. The Commander never dreamed alone again, and never once had company.{/n}''',
    requires=(EMBODIED, CLOSED), forbids=(COMMITTED,), paragraphs=SHELL_PARAGRAPHS)

epilogue("captive", '''{n}The Commander never opened that door again. Behind it, at the back of the Commander's head, something went on beating alongside the Commander's heart for the rest of the Commander's life: slow, sullen, patient, a second pulse that would not stop. On the nights Nocticula's name was spoken aloud it went faster.{/n}
{n}In Alushinyrra nobody said Shamira's name in front of the Commander. They had all heard the Commander say it in two voices.{/n}''',
    requires=(KEPT,), forbids=(EMBODIED, CAST_OUT))

epilogue("cast_out", '''{n}What the Commander carried behind {mf|his|her} eyes for a few nights in the Fifth Crusade's last spring went out of {mf|him|her} one night on a wardrobe floor in Drezen, and did not come back, because the Abyss is a mouth and it had been waiting.{/n}
{n}Nobody in the camp ever knew. The Commander's head was quiet afterwards, for the rest of {mf|his|her} life. It was a long time before the Commander stopped listening for a second heartbeat.{/n}''',
    requires=(CAST_OUT,), forbids=(EMBODIED,))

epilogue("drowned", '''{n}For a night after the boudoir, the Commander carried two heartbeats. By morning there was one. What had grabbed at the Commander's memories in the dark let go of them, and went down, and the Abyss swallowed what the syphon had not wanted.{/n}
{n}The Commander's mother's face never came back quite right.{/n}''',
    requires=(DECLINED,), forbids=(RETURNED,))

epilogue("never", '''{n}The Ardent Dream once searched the Commander's mind in her Harem. She found the war, and an invitation she had not expected. The Commander left her alive. She never learned whether it was caution, indifference, or another game.{/n}
{n}She had her servants watch for the mortal whenever strangers came through her doors.{/n}''',
    requires=(READ,), forbids=(KILLED,))

epilogue("walked", '''{n}Shamira walked out of the Commander's wardrobe in a stolen body and returned to her Harem. She took her chair back and let the courtiers discover for themselves how much of her had survived.{/n}
{n}Every night she entered the Commander's sleep for the warmth that kept that body alive. Sometimes she spoke. Sometimes she sat without a word, listening to thoughts the Commander had not meant to share.{/n}''',
    requires=(EMBODIED,), forbids=(COMMITTED, CLOSED, ALLY, GAME), paragraphs=SHELL_PARAGRAPHS)

epilogue("unhoused", '''{n}The war ended with the Ardent Dream still behind the Commander's eyes, waiting for a body that never came. She talked, at first. Then she sulked. Then, for long stretches, she only listened, and the second heartbeat went on beside the Commander's own, patient as a cat at a mousehole.{/n}
{n}Nobody else ever heard her. Everyone who stood too close to the Commander, though, found themselves thinking of her.{/n}''',
    requires=(FOUND,), forbids=(EMBODIED, KEPT, CAST_OUT, CLOSED))

epilogue("mourned", '''{n}On the night the rift took the Commander, the coal in Shamira's chest went out before morning. She sent her court away and sat on her throne, listening for a dream that did not come.{/n}
{n}By the first dawn her fingertips were white. She had every lamp in the Harem lit, then went out into Alushinyrra. For three days she searched the city, entering mortal sleepers' dreams, one after another, looking for a fire the stolen body would take. None would kindle it. The cold crept past her wrists; she could still move, and kept looking.{/n}
{n}At dawn after the third night, they found the shell three streets from the Harem, sitting in a doorway. Its face was blank again. Frost covered its long hands. No one in her court went to fetch it.{/n}''',
    requires=(EMBODIED, "sacrifice"), forbids=(ALIVE_AFTER, CLOSED), living=False)


# --- Path fit (13 directive update 2026-09-29 / ROUTE-BRIEF-R §2; recorded in PP9). --------------------------------------
# PATH_FIT is the scene's class today: T (a device, or gated on the Trickster), N-all, or N-fit. PATH_FIT_V2 names the
# scenes whose content would hold on her fitting paths (14-PATH-FIT §3), with those paths; they keep their Trickster gate
# until the v2 pass replaces it with a path gate and writes her non-Trickster ending under canon fate.
# Shamira is killed at the compulsory Trickster boudoir visit; on Demon and Legend she lives (14 §3: Dem Y, Leg Y, Dev and
# Lic M). Her Chapter 4 audience beats read her and the Commander only, so their content holds there (minus the
# [Trickster] recipes choice and the T3 tally choice, which stay Trickster-gated); everything from the briefing on is the
# device and stays T. shamira_mind and shamira_dream are all T.
PATH_FIT = {s["Id"]: "T" for s in SCENES}
PATH_FIT_V2 = {P + "ch4.read": "N-fit: Demon, Legend", P + "ch4.bird": "N-fit: Demon, Legend",
               P + "ch4.first_taste": "N-fit: Demon, Legend"}


def integrate(payload):
    """Her own native reads and Derived keys. The shared world keys (shamira.killed, plan_known, the hand-over latch)
    bind on demand in trickster_world."""
    for kind, keys in (("Etudes", ETUDES), ("MainCharacterFacts", FACTS), ("SelectedAnswers", SELECTED)):
        for key, guid in keys.items():
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != guid:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = guid
    for key, guids in SEEN.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != guids:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(guids)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'shamira.trickster.killed.voice',
    'shamira.trickster.killed.voice_letter',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
