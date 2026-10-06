"""Areelu Vorlesh on the Trickster path: the Architect's wager (Writer/handoffs/trickster/areelu-vorlesh.md, family F20,
the epilogue rewrite). Replaces the unregistered draft areelu_trickster_rivalry_opening (AREELU-01/04/06/12 superseded),
which is kept for reference in reference/retired-drafts/.

Canon: in Alushinyrra she admits she watched the Commander "from birth. From before that, even. And I kept detailed notes"
(c4/Palace/Audience_Areelu/Cue_0103 9e9b0200) and calls the Commander her creation (Cue_0013 bcc023d9). At Iz she says
"Regret poisons the will and the mind. I've long since forgotten what regret feels like." (c5/Iz/AreeluIntro/Cue_0010
891a8c1c), "I'm interested in neither praise nor reproach." (Cue_0024 dbea944b) and "Until then, I'll continue to follow
you..." (Cue_0041 af9687ff). Her projection in the laboratory cell says "One of us must burn so that the other may live
and the Wound may be eliminated..." (c5/AreeluLabAgain/AreeluCell/Cue_0037 a4b8a109) and, of the Commander's wound, "It was
my mistake. My failure." (Audience_Areelu/Cue_0097 c3cdce20). Defeated at Threshold she says "Let us finish this experiment
here and now." (c6/SecondFloor/GrandFinal/Cue_0001 d309c305); the Trickster finale uses "Areelu's life to open new rifts"
(Answer_0055 91c5eca8), and the native Trickster rewrite ends "allow me to finish writing up my report on this
experiment" (Epilogues/Cue_0179 7fbdff97). Her unrepentant method: "This experiment may fail, but that simply means I
need to make further adjustments. I'll try again." (c6/AeonFinal/AreeluLetsFinalFight_Aeon/Cue_0035 00591dd8).

Authored, and labelled as authored: the Commander asking for a copy of her file; the lens and the frost letters; the
wager and its terms (the wound, never the soul or the remains; ledger rows 6 and 16); the report the epilogue pages
write, and everything in it after Threshold. "Decrepit heap of flesh" (Audience_Areelu/Cue_0111) is Lann's line, not
hers, and is not used.
"""
from story_format import c, n, p, reaction, scene

SCENES = []

# Native hooks (every GUID verified in blueprints.zip; see the module notes in trickster/areelu-vorlesh.md).
AUDIENCE_LIST = "199a940b97b11664aace4101733cd963"    # c4/Palace/Audience_Areelu/AnswersList_0030 (her questions)
AUDIENCE_RETURN = "46603da28aa69bf49840cd15040e82f5"  # Cue_0029 "Very well, then. Ask your questions and I will answer."
IZ_LIST = "09b8d5eb5dae3634d9dc3d8c7bdd6e9d"          # c5/Iz/AreeluIntro/AnswersList_0002
IZ_RETURN = "c000ae3d47250b943953b1bd25333f30"        # Cue_0009 "I wish I could answer them now, but I cannot..."
IZ_WARNING = "f4eee511a0c0f9e4cace9e0ced47bfba"       # Cue_0014 "I am here to give you a warning..." (every Iz objective)
CELL_LIST = "74989c07fc5fd8a42b18b333dc40acc1"        # c5/AreeluLabAgain/AreeluCell/AnswersList_0003
CELL_RETURN = "3d63aae9686620845acc8be95e490c26"      # Cue_0035 "So be it." The witch nods. "So be it..."
CELL_FAREWELL = "13e9433101b3586488df88c296d91ed2"    # Cue_0038 "Farewell, then. Threshold awaits!"
WELCOME_LIST = "bb3528754c7e741438acef95ec3b6430"     # c6/ThresholdExterior/AreeluThresholdWelcome/AnswersList_0002
WELCOME_RETURN = "6b4c8a08d22268f41badc455825b3082"   # Cue_0027 "Nothing at all," the witch answers
WELCOME_ON = "7afb59b5619513d40b73f9299393f95c"       # Cue_0009 "...cross this threshold. I'll be waiting for you..."
TRUTH_LIST = "64af2f5bd9de92a469b6a8b63219206e"       # c6/AreeluDemiplane/AreeluAllTruth/AnswersList_0020 (after the hunters)
TRUTH_RETURN = "1635402f363fa764a96f442ccb039a81"     # Cue_0012 "Because they saw {mf|him|her} with a scroll..."
TRUTH_ON = "6c39117f5ee77c34681c4cee77de75b8"         # Cue_0028 "Look around you. This demiplane..." (every answer leads here)
RIFT_LIST = "90861396a1375684eb5bf894bedecff3"        # c6/SecondFloor/AreeluLetsFinalFight/AnswersList_0003 (at the rift)
RIFT_RETURN = "c4f9dac3d26416d43b3c1662d07a99c0"      # Cue_0047 "How strange. You are a kindred spirit... But no. No."
FINAL_LIST = "f56a69dc64a48b14096a557697f43f2a"       # c6/SecondFloor/GrandFinal/AnswersList_0003 (defeated, bleeding)
FINAL_RETURN = "{n}Areelu waits, bleeding, for your answer.{/n}"
TRICKSTER_PAGE = "fb42f8bd123bf1f40a448f6dbc66cbbe"   # Epilogues/BookPage_0147 (the Trickster ending; "What kind of an ending...")
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"       # CompanionDialogues/Seelah/AnswersList_0003
NENIO_HUB = "1ab909cc3a6194840b1475b99547c263"        # CompanionDialogues/Nenio/AnswersList_0015
EMBER_HUB = "f2a35965e9bc601449498bd022b04d9d"        # CompanionDialogues/Ember hub (friendship only)

STARTED = "areelu.started"
CLOSED = "areelu.closed"
COMMITTED = "areelu.committed"
P = "areelu.trickster."
PRIMED = P + "primed"
BET = P + "bet_offered"
LENS = P + "rivalry.lens"
STRUCK = P + "wager_struck"
DECLINED = P + "declined"
STAKE_ONLY = P + "stake_only"
NOTICED = P + "noticed"                 # variant only: the Commander asked for a copy of the file in Alushinyrra
REMINDED = P + "threshold_reminded"     # variant only: the wager named at the gate of Threshold
REAL_HAND = P + "real_hand_asked"       # variant only: "Bring the real hand to Threshold."
LENS_HELD = P + "lens_held"             # the Commander holds her lens (Chapter 5 correspondence)
LENS_ASKED = P + "lens.asked"            # her three questions answered through the lens
NAMED = P + "stake_named"               # the loophole: "what is left of her" is her notes (cell joke, late terms, Threshold)
WOUND_CEDED = P + "cost.wound_ceded"    # the price of the term at Threshold: the Commander's wound is hers, win or lose
SURVIVES = P + "survives"               # Derived: [the Trickster finale + the stake collected] or [the punchline]
DRAWN = P + "graft_drawn"               # the stake collected on screen: the Abyss siphoned into the soul cauldron
CAULDRON = "council.cauldron_given"     # Council_5-1/Cue_0041: the Trickster's soul cauldron (world binding)
BURNED = P + "commander_burned"         # Derived: the Commander sacrificed at a Wound-closed finale (ledger row 16)
WITCH_BET = P + "cost.bet_with_the_witch"
LATE = P + "cost.late"
ON_SCREEN = P + "rivalry_on_screen"     # Derived (world): bet_offered | rivalry.lens; the route reads WAGERED
LATE_COMMITTED = P + "late_committed"   # Derived: trickster.ever + wager_struck (R2-6)
DIED = "areelu.died_at_finale"          # Derived: the five native fate etudes
CHEATED = "trickster.cheated_death"     # Derived (engine): the Trickster punchline endings
SAC_TRICK = "areelu.sacrifice_trickster"
FIGHT = "areelu.dead_fight"             # Ending_AreeluDead 936af394: a general death key (the Trickster sacrifice starts it too)
INCINERATED = "areelu.incinerated"
SAC_WOUND = "areelu.sacrifice_wound"
SAC_BEFORE = "areelu.sacrifice_before"
ASCENDED = "areelu.ascended"
NOTES_TOLD = "areelu.notes_told"        # Audience_Areelu/Answer_0031 "You followed me." (-> "I kept detailed notes")
CRIB_SAD = "areelu.crib.sadness"        # AreeluCell/Answer_0013 "Sadness."
CRIB_RAGE = "areelu.crib.rage"          # AreeluCell/Answer_0014 "Rage."
CRIB_MYSTERY = "areelu.crib.mystery"    # AreeluCell/Answer_0015 "Closeness to mystery."
YEARS_ASKED = "areelu.years_asked"      # LetsFinalFight/Answer_0054 -> Cue_0055 "Years, or decades, perhaps."
TRICKSTER_ENDINGS = ("ending.trickster", "ending.trickster_allplanes", "ending.trickster_allplanes_fw", "ending.trickster_full")
NENIO_GONE = ("nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out", "nenio.dissolved")
NENIO_BACK = "nenio.trickster.returned"   # Nenio's Trickster return (nenio_trickster); G6(b) overrides only, never read otherwise

UNPRIMED = P + "cost.unprimed"          # the wager first offered at Threshold, defeated: her harshest terms (Sol INT)
LIFE_TERM = P + "term.life"             # "Your life. Nothing less." at Threshold: no work to collect in her place
# Sol quality pass: current possession, never the historical hand-over. The Council gives the empty siphon
# (Council_5-1/Cue_0041 d66b1fdc) and fills it; Shyka_Offer/Cue_0031 removes the filled one if the path is abandoned.
SIPHON_EMPTY = "areelu.siphon.empty"            # InventoryItems TricksterCouncil/Items/EmptySyphon
SIPHON_COUNCIL = "areelu.siphon.council"        # InventoryItems SyphonWithCouncilNoShyka
SIPHON_SHYKA = "areelu.siphon.council_shyka"    # InventoryItems SyphonWithCouncilShyka
SIPHON_SHAMIRA = "areelu.siphon.shamira"        # InventoryItems SyphonWithShamira
CAULDRON_HELD = P + "cauldron_held"             # Derived: any of the four siphons in the inventory now
CAULDRON_FULL = P + "cauldron_full"             # Derived: a filled siphon (the graft goes in on top of its essence)
DAGGER_HELD = "areelu.dagger_held"              # InventoryItems CrystalDaggerItem d9385822 (her Kenabres crystal)
WARDSTONE_CLEANSED = "areelu.wardstone_cleansed"  # Wardstone_BookEvent/Answer_0021: the cleansing spends the dagger
WAGERED = P + "wager_on_screen"         # Derived: the bet offered at Iz, through the lens, or first at Threshold
REWRITTEN = P + "rewritten"             # Derived: the Trickster finale rewritten on the collected stake
RETIRED = (P + "react.seelah_objects",)

DERIVED = {SURVIVES: [[SAC_TRICK, DRAWN], [CHEATED]], BURNED: [["sacrifice", "ending.wound_closed"]],
           CAULDRON_HELD: [[SIPHON_EMPTY], [SIPHON_COUNCIL], [SIPHON_SHYKA], [SIPHON_SHAMIRA]],
           CAULDRON_FULL: [[SIPHON_COUNCIL], [SIPHON_SHYKA], [SIPHON_SHAMIRA]],
           WAGERED: [[BET], [LENS], [UNPRIMED]],
           REWRITTEN: [[SAC_TRICK, DRAWN]]}

INVENTORY = {
    SIPHON_EMPTY: "d66b1fdc9d313784ca51712640e210c7",
    SIPHON_COUNCIL: "f873b21424513e64eabe1a0e138812ba",
    SIPHON_SHYKA: "e26fec918fd8e774ba241955f03d4b9d",
    SIPHON_SHAMIRA: "cfc7c93f8e93340469287afc905371c2",
    DAGGER_HELD: "d9385822b9871ac468e00aa01b68d45a",
}

SELECTED_ANSWERS = {
    YEARS_ASKED: "73f857edb12933948b735e0364fcf1ca",
    NOTES_TOLD: "f6c5054ceccd00046b23f1ead6af0a83",
    CRIB_SAD: "0853df779fb798c4dbf2d6e106674170",
    CRIB_RAGE: "f0d826fb7b99a1e4c9e23e46534a2993",
    CRIB_MYSTERY: "9c9655606788f8b4cb039e48b2739c25",
    WARDSTONE_CLEANSED: "91a0b72bdcd5809409760cb25ad7d8c3",
}

RELATIONSHIP = dict(
    Title="The Architect's wager",
    Description="Areelu Vorlesh and I have a wager: one of us burns at Threshold, or neither does. She does not accept jokes as collateral.",
    Objective="Settle the wager with Areelu",
    Guidance=("On the Trickster path, offer Areelu a bet when she finds you at Iz; if you miss it, look for what she left "
              "among the ruins. Strike the wager in her laboratory cell after she tells you that one of you must burn, "
              "and raise the stakes at Threshold, before the final choice."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED, UnavailableFlags=[], FailureFlags=[],
)


def ar(id, text, *choices, **kw):
    return n(id, "Areelu", text, *choices, portrait="Areelu", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Areelu", **kw)


def inline(id, title, chapter, entry, nodes, requires, forbids, lists, return_cue, **extra):
    SCENES.append(scene(id, title, "Areelu", chapter, entry, nodes, requires=requires, forbids=forbids, last=chapter,
                        optional=True, Relationship="areelu", Chapters=[chapter], AnswerLists=list(lists),
                        NativeReturnCue=return_cue, **extra))


def at_threshold(id, title, entry, nodes, requires, forbids):
    """E14b: beside her native answers while she stands defeated at Threshold, returning to that list."""
    SCENES.append(scene(id, title, "Areelu", 6, entry, nodes, requires=requires, forbids=forbids, last=6, optional=True,
                        Relationship="areelu", Chapters=[6], AnswerLists=[FINAL_LIST], ReturnToList=True,
                        ReturnText=FINAL_RETURN))


# --- Chapter 4, Alushinyrra: the subject asks for a copy (optional primer; a variant read only) -----------------------
# Physical in Chapter 4 is allowed: Rules.Available blocks Chapter 4 physical scenes only for relationship "tirabade".

inline("areelu.trickster.audience.notes", "The subject's file", 4,
    '[Ask for your file] "Detailed notes, from before I was born. I\'m the subject. I\'d like a copy."', [
    ar("start", '''{n}Areelu raises an eyebrow.{/n} "A copy? So that you can pick apart my work at your leisure? No. Ask your questions. I will decide what you need to know."''',
        c('''"Then I'm contaminated already. You have just told me who made me. What else is in the file?"''', "contaminated"),
        c('[Joke] "If I\'m your creation, every joke I make is technically yours. Congratulations. You\'re funnier than you look."', "yours"),
        c('[Joke] "I\'ll trade you. I\'ve been keeping notes on you too. Mine are shorter."', "trade"),
        c('"Never mind. Tell me what I came to hear."', abort=True)),
    ar("contaminated", '''"Everything." {n}Her gaze does not leave you.{/n} "The first fever. The first lie you told that was believed. The crevice in Kenabres, where I saved you and your unfortunate companions, and you never knew who to thank."
"And a gap. Some while ago the notes stopped agreeing with you. You began to do things I had not written down. That is not your triumph, Commander. It is my error, and I have been correcting errors since before your grandparents were born."''',
        c("Continue", "offer")),
    ar("yours", '''"Then I have made something that wastes my time. Your power was my gift. The jokes are yours." {n}She looks you over.{/n} "I should like to know how you have made them dangerous. That is not in my notes."''',
        c("Continue", "offer")),
    ar("trade", '''"You keep notes on me." {n}It is not quite a question. She tilts the mirror toward you as if it might show her the page.{/n} "Read me the first entry."''',
        c('"\'Arrived uninvited before I was born. Stayed. Still hasn\'t explained herself.\'"', "entry"),
        c('"\'Turned herself into half a demon to win an argument with the gods. Still losing.\'"', "losing")),
    ar("entry", '''"Accurate, and useless. You have written down what you saw. You still do not know why I did it." {n}She lowers the mirror.{/n} "That ignorance will matter at Threshold."''',
        c("Continue", "offer")),
    ar("losing", '''{n}Her smile vanishes.{/n} "Do not mistake survival for surrender. I have been arguing with the gods since before your birth, and I am still here. You may keep score when you understand the wager."''',
        c("Continue", "offer")),
    ar("offer", '''"No. You may not have a copy." {n}She lifts the mirror, considers her own reflection in it, and lowers it again.{/n}
"But I will give you something rarer than my notes. An entry of your own." {n}She speaks as if dictating to someone who is not in the room.{/n} "'In Alushinyrra, the subject asked to read the file. Unprecedented. Further observation required.'"''',
        c('"Further observation. I\'ll hold you to that."', flags=(NOTICED,)),
        c('[Joke] "You spelled \'unprecedented\' wrong."', "spelled"),
        c('"If your notes are so good, predict what I\'ll say next."', "predict")),
    ar("predict", '''"You will make a joke about my mirror. When I do not laugh, you will try something ruder. Then you will ask what you came here to learn." {n}She folds her hands.{/n} "Go on. Prove me wrong."''',
        c('[Say nothing at all, and smile.]', "silent"),
        c('"Your mirror\'s smudged."', "smudged"),
        c('"Why me? Out of everyone in Golarion, why did you choose me?"', "child")),
    ar("silent", '''{n}A gong sounds elsewhere in the palace. Areelu waits until it falls silent.{/n} "Nothing? You came all this way to waste an answer? Very well. I will remember that you can keep quiet when it costs you something."''',
        c("Continue", "spelled")),
    ar("smudged", '''{n}Areelu turns the mirror toward the light and wipes its edge with her thumb.{/n} "A fault easily corrected. You should bring me more of those." {n}Her gaze returns to you.{/n} "Now the real question."''',
        c("Continue", "spelled")),
    ar("child", '''{n}The mirror in her hand goes dark.{/n} "That answer waits at Threshold. I will not give it to you for a joke." {n}She lowers the mirror.{/n} "You know where to put the knife, Commander. I will remember that too."''',
        c("[Let her go on.]", flags=(NOTICED,))),
    ar("spelled", '''"I did not write it down." {n}Her mouth twitches.{/n} "I will remember it. Ask your questions before I change my mind about answering them."''',
        c("[Let her go on.]", flags=(NOTICED,))),
], requires=("trickster", NOTES_TOLD), forbids=(NOTICED,), lists=(AUDIENCE_LIST,), return_cue=AUDIENCE_RETURN,
   EntryMythic="PlayerIsTrickster")


# --- Chapter 5, Iz: the bet (R2-2 primer, before the finale it answers) ----------------------------------------------

inline("areelu.trickster.rivalry.iz_bet", "My money's on neither", 5,
    '[Offer the Architect a bet] "One of us has to die so the other can live and the Wound can close. I\'ll take that bet. My money\'s on \'neither\'."', [
    ar("start", '''{n}Areelu's gaze sharpens, the way it does over a specimen.{/n} "Neither."
{n}Behind her the sky over Iz is the colour of an old bruise. Somewhere below the square something large is breaking stone, slowly, as if it has all the time in the world.{/n}
"You have not understood the Wound at all. It is not a riddle with a clever answer. It is a debt. At Threshold, you will find out what it costs."''',
        c('"Debts get paid by whoever can\'t get out of them. I always get out of them."', "debts"),
        c('"You don\'t sound certain. You sound like someone who checked her sums twice."', "sums"),
        c('"You said you\'d need further observation. Here I am. Observe."', "observed", requires=(NOTICED,)),
        c('[Joke] "Then I\'ll owe you. I\'m very good at owing."', "owing"),
        c("[Let it go.]", abort=True)),
    ar("owing", '''"I have your file. You owe the crusade a victory, and the Abyss would like to collect you before you deliver it." {n}She glances toward the burning city.{/n} "Offer your creditors a joke and see what they do with it. I intend to hear a stake."''',
        c("Continue", "stake")),
    ar("debts", '''{n}She glances toward the burning streets.{/n} "You have escaped several attempts on your life. Deskari has made a better one here. I came to warn you, Commander. I would prefer my work survive long enough to settle this wager."''',
        c("Continue", "stake")),
    ar("sums", '''{n}The wound above her heart pulses.{/n} "I have checked them for a hundred years. If you mean to contradict me, Commander, bring more than a cheerful face."''',
        c("Continue", "stake")),
    ar("observed", '''"You are being observed. You are also standing in a trap that Deskari built for you, which rather spoils the experiment." {n}Her mouth thins.{/n}
"In Alushinyrra you asked for your file. Now you offer me a wager. You are making this worth the interruption. Name your stake."''',
        c("Continue", "stake")),
    ar("stake", '''"Very well. I accept that you have made an offer. I do not accept its terms." {n}She glances past you: toward the camp, the burning temple, the city folding in on itself like wet paper.{/n}
"State your stake when you know what you can afford to lose. You will not learn it here. Here, you are about to lose a great deal."''',
        c('"Then tell me about the trap."', native_next=IZ_WARNING, flags=(PRIMED, BET))),
], requires=("trickster",), forbids=(BET, PRIMED), lists=(IZ_LIST,), return_cue=IZ_RETURN, EntryMythic="PlayerIsTrickster")


QUESTION_THREE = '''{n}The frost clears. Nothing forms in it; the lamp gutters twice. Then:{/n}
"Third. When you look at me through this glass, Commander, what do you see? Be precise. I will know if you are being kind."'''

# The lens's night (the one Chapter 5 letter on either path; letters_max.5 = 1): her three questions, then where she was.
LENS_NIGHT = [
    ar("first", '''"Now that you have the glass, I have questions. First: why are you not afraid of Threshold? I have watched you plan the march. You have not stopped to make a different plan." {n}The letters crowd the rim.{/n} "I know what waits there. I would like to know what makes you willing to meet it."''',
        c('''[Joke] "Because I have an escape plan. A bad one. You would hate it."''', "read"),
        c('"I am. I just hide it better than you do."', "hide"),
        c('"Because you\'ll be there."', "there"),
        c('"Because I\'ve already died once. It didn\'t take."', "died")),
    ar("died", '''"I kept you alive in the caves. The wound would have killed you without the crystal." {n}The answer appears quickly.{/n} "If you have learned another way to survive since then, I hope you have tested it. I will not be helping you for the same reason at Threshold."''',
        c("Continue", "second")),
    ar("read", '''"Then I hope you have tested it." {n}The frost thickens along the rim.{/n} "There will be no time to improve it at Threshold. I would prefer you arrive in one piece. I have not finished with you."''',
        c("Continue", "second")),
    ar("hide", '''"Then I have missed something." {n}The letters stop. New frost covers the old sentence.{/n} "Fear has not kept you from coming. I will watch what you do with it when you reach Threshold."''',
        c("Continue", "second")),
    ar("there", '''{n}The frost goes blank. For a long time nothing forms in it at all.{/n}
"That is not an answer. That is a provocation. I will record it as one." {n}Then, smaller, in the corner of the glass:{/n} "Recorded."''',
        c("Continue", "second")),
    ar("second", '''"Second. What is a soul, to a Trickster? The priests say it is a thing to be weighed. The demons say it is a thing to be eaten. I have spent a hundred years treating it as a thing to be mended, and I have not managed it. What do you say it is?"''',
        c('"A joke the gods haven\'t finished telling."', "unfinished"),
        c('"Something that belongs to whoever it\'s in."', "belongs"),
        c('[Joke] "Honestly? A lot of paperwork."', "paperwork")),
    ar("unfinished", '''"They have had a hundred years to finish mine. I am tired of waiting." {n}The frost cuts across the glass in a hard white line.{/n} "At Threshold I will interrupt them. You are already part of that argument."''',
        c("Continue", "third")),
    ar("belongs", '''"Whoever it is in." {n}The frost cracks, very faintly, along one edge of the glass.{/n}
"You do not know what you have said. You will, at Threshold. Remember that you said it, Commander. I will."''',
        c("Continue", "third")),
    ar("paperwork", '''"Paperwork." {n}A long pause.{/n} "The Lady of Graves keeps it, and she has never once lost a page. I know. I have looked for the one I wanted."
"Do not joke about that particular ledger. Not to me. Not yet."''',
        c("Continue", "third")),
    ar("third", QUESTION_THREE,
        c('"A woman who hasn\'t slept in a hundred years."', "slept"),
        c('"The only person who\'s ever taken notes on me."', "notes"),
        c('[Joke] "Mostly frost."', "frost")),
    ar("slept", '''"Accurate." {n}The frost holds the word a long time, as if she were looking at it.{/n}
"I have not slept properly since the hunters came to my house. Most people who notice that try to kill me for it."
"Go to sleep, Commander. One of us should."''',
        c("Continue", "acc_start", flags=(LENS_ASKED,))),
    ar("notes", '''"Mine are the notes that made you possible." {n}The letters lean along one side of the glass.{/n} "The crusaders see their saviour. The demons see something worth devouring. I would prefer they leave my work alone. Do not mistake that for sentiment."''',
        c("Continue", "acc_start", flags=(LENS_ASKED,))),
    ar("frost", '''"A poor answer." {n}The glass clouds, clears, and clouds again.{/n} "You have my attention, Commander. Try to deserve it."''',
        c("Continue", "acc_start", flags=(LENS_ASKED,))),
    nar("acc_start", '''{n}The frost fades, and before she can clear the glass again it is you who breathes on it, and writes in the mist with a fingertip: "Where were you, all those years you were watching?"{/n}
{n}The answer is a long time coming. When it comes, the letters fill the whole lens, edge to edge, and she has to clear it twice to finish.{/n}''',
        c("Continue", "accounts"),
        c("[Put the lens away for the night.]")),
    ar("accounts", '''"In Kenabres, when you fell into the crevice, I saved you and your companions. At the Gray Garrison I distracted Minagho. In Drezen I wore Yaniel's face and led you toward the Sword of Valor. I had work to do, and you needed to reach it." {n}The letters crowd the rim of the glass.{/n} "Do not thank me. You would not like what I intended to collect."''',
        c('[Joke] "Thank you. You were a terrible Yaniel, by the way."', "yaniel"),
        c('"Why tell me again?"', "again"),
        c('"You kept me alive so you could kill me at Threshold."', "alive"),
        c('"And in Drezen, lately? Were you watching when I crowned the Fool King?"', "fool_king",
          requires=("fool_king.ever_crowned",)),
        c('"What\'s the last thing you watched me do, before I asked?"', "last")),
    ar("last", '''"Sleep." {n}The letters come at once.{/n} "You lay on your left side, with one hand under the pillow. I could not see what you were keeping there. You spoke once. I could not make out the word." {n}The next line forms more slowly.{/n} "The wound warmed this glass while you slept. I wrote down the hour. When you come to Threshold, I intend to learn what answered it."''',
        c("Continue", "bait", forbids=("areelu.one_must_burn",)),
        c("Continue", "bait_after", requires=("areelu.one_must_burn",))),
    ar("fool_king", '''{n}The frost thickens until the lens is almost white.{/n}
"I was watching. The Commander of the Fifth Crusade, in the capital that crusaders bled for, put a crown on a fool and made the city kneel to him. The priests wept. The knights drank. The fool, I am told, gave a very good speech."
"I have seen demon lords crowned, Commander. I have seen them uncrowned. None of them made me laugh." {n}A pause.{/n} "Do not ask whether I laughed. I am not going to tell you."''',
        c("Continue", "bait", forbids=("areelu.one_must_burn",)),
        c("Continue", "bait_after", requires=("areelu.one_must_burn",))),
    ar("yaniel", '''"You went where she led you. That is what I required of the disguise." {n}The frost clears and returns.{/n} "You may dislike the performance now. It served me well enough."''',
        c("Continue", "bait", forbids=("areelu.one_must_burn",)),
        c("Continue", "bait_after", requires=("areelu.one_must_burn",))),
    ar("again", '''"You asked. And I would like you to remember who kept you alive before you name your stake." {n}The next line is smaller.{/n} "You are not the only one who can make a wager unpleasant."''',
        c("Continue", "bait", forbids=("areelu.one_must_burn",)),
        c("Continue", "bait_after", requires=("areelu.one_must_burn",))),
    ar("alive", '''"Yes." {n}No hesitation at all.{/n} "I kept you alive so that you would be whole when it mattered. A vessel that breaks too early is useless."
"You wanted me to say something softer. I do not have anything softer. I have this, which is true."''',
        c("Continue", "bait", forbids=("areelu.one_must_burn",)),
        c("Continue", "bait_after", requires=("areelu.one_must_burn",))),
    ar("bait", '''"Bring the wager to Threshold. If you find my projection before then, speak to it. I would like to hear you say 'neither' while I am looking at you." {n}The frost clears and does not form again that night.{/n}''',
        c("[Put the lens away.]")),
    ar("bait_after", '''"You have heard my projection. Bring what you mean to wager to Threshold, and say it to my face." {n}The frost clears and does not form again that night.{/n}''',
        c("[Put the lens away.]")),
]


def lens_night(opening):
    """The letter's own opening nodes, then the shared night through the frost."""
    return [*opening, *LENS_NIGHT]


# --- Chapter 5, the lens (R2-2 late fallback when the Iz bet was missed: the one letter) ----------------------------

SCENES.append(scene("areelu.trickster.rivalry.lens", "Knock knock", "Areelu", 5, "", lens_night([
    nar("start", '''{n}A lens of dark glass has appeared among your campaign maps. Its silver ring is cold. Nobody admits to leaving it there.{/n}
{n}When you hold it to your eye you do not see the tent around you. You see your tent from above, as a bird would, and a woman's hand at a desk, writing notes about it. The hand is steady. The margins are full of small, neat corrections.{/n}''',
        c('[Tap the lens twice] "Knock knock. You\'ve been watching me since Kenabres. Rude not to say hello."', "reply",
          mythic="Trickster"),
        c("[Hold the lens up to the lamp and read her notes backwards.]", "backwards"),
        c("[Wrap it in cloth and put it away.]", abort=True)),
    nar("backwards", '''{n}Held to the lamp, the notes read backwards through the glass. Most of them are about you: your hours, your rations, which of your companions you laugh with and which you only answer. At the bottom, underlined twice: "Subject remains unpredictable. Correction scheduled for Threshold."{/n}
{n}The hand stops writing. Then, very deliberately, it adds: "Subject is reading this."{/n}''',
        c('[Breathe on the glass and write in the mist] "Correction? I prefer \'punchline\'."', "reply2", mythic="Trickster")),
    ar("reply", '''{n}The lens frosts over. Letters form, small and precise.{/n} "Knock knock. How childish. Yes, I have been watching. You should know that by now." {n}A hand wipes away the frost from the other side.{/n} "Make your offer, Commander. I have not given you this much of my time to read greetings."''',
        c('"Then measure this. One of us is supposed to burn at the end. My money\'s on neither."', "terms"),
        # The Long Con's Areelu crossing (doc 15 section 4a, PP8): appended; [0] -> terms is unchanged.
        c("[Ask what she concluded in Drezen.]", "drezen_memory", requires=("trickster", "areelu.early.mask_counted"))),
    ar("drezen_memory", '''{n}The frost thickens, clears, and thickens again, as though she were deciding how much of a file to show you.{/n} "Drezen."''',
        c("Continue", "drezen_silent", requires=("areelu.early.read_silent",)),
        c("Continue", "drezen_offered", requires=("areelu.early.read_offered",), forbids=("areelu.early.read_silent",)),
        c("Continue", "drezen_counted", forbids=("areelu.early.read_silent", "areelu.early.read_offered"))),
    ar("drezen_silent", '''"You said nothing. I have not mistaken that for an answer."''',
        c('"Then measure this. One of us is supposed to burn at the end. My money\'s on neither."', "terms")),
    ar("drezen_offered", '''"You gave me an explanation. I have not decided whether to believe it."''',
        c('"Then measure this. One of us is supposed to burn at the end. My money\'s on neither."', "terms")),
    ar("drezen_counted", '''"You counted my pauses in that cell. I noticed you counting."''',
        c('"Then measure this. One of us is supposed to burn at the end. My money\'s on neither."', "terms")),
    ar("reply2", '''{n}Letters form in the frost.{/n} "Punchline. If you mean to make one of Threshold, you had better have something prepared. I will not die for a phrase."''',
        c('"Then here\'s a line you didn\'t write. One of us is supposed to burn. My money\'s on neither."', "terms")),
    ar("terms", '''"Neither. And you make the offer through my own lens." {n}The glass stays clear for several breaths.{/n} "Very well. Bring your wager to Threshold. Keep the glass until then. I would like to watch what you do with the time you have left."''',
        c("[Keep the lens, and keep looking.]", "keep_looking", flags=(PRIMED, LENS, LATE, LENS_HELD)),
        c("[Keep the lens, and put it away.]", flags=(PRIMED, LENS, LATE, LENS_HELD)),
        c('"Why would you give your enemy a window into your study?"', "window")),
    ar("window", '''"Because it works both ways. When you look, I learn when you are awake, when you are alone, and what makes you put the glass away." {n}The frost briefly hides the hand beyond it.{/n} "I have given my enemy a window. My enemy keeps using it."''',
        c("[Keep the lens, and keep looking.]", "keep_looking", flags=(PRIMED, LENS, LATE, LENS_HELD)),
        c("[Keep the lens, and put it away.]", flags=(PRIMED, LENS, LATE, LENS_HELD))),
    nar("keep_looking", '''{n}You do not put it away. The frost clears, and forms again, faster, as if the hand on the other side had been waiting.{/n}''',
        c("Continue", "first")),
]), requires=("trickster", "areelu.met"), forbids=(PRIMED, STRUCK), last=5, optional=True, Relationship="areelu",
   Remote=True, Chapters=[5]))


# --- Chapter 5, the lens between Iz and her cell: "Until then, I'll continue to follow you..." (Cue_0041) -------------

def lens_letter(id, title, nodes, requires, forbids=(), delay=48):
    SCENES.append(scene(id, title, "Areelu", 5, "", nodes, requires=requires, forbids=(STRUCK, CLOSED, *forbids),
                        delay=delay, last=5, optional=True, Relationship="areelu", Remote=True, Chapters=[5]))


# The bet was offered at Iz: she leaves her lens on the Commander's table (the late-primer path already holds it).
lens_letter("areelu.trickster.lens.watched", "The glass on the table", lens_night([
    nar("start", '''{n}A lens of dark glass in a silver ring lies on your camp table, on top of the maps. It is cold enough to chill the paper beneath it.{/n}
{n}Nobody admits to having put it there. Nobody, when you ask, remembers seeing it at all.{/n}''',
        c("[Look through it.]", "look"),
        c("[Turn it face down.]", "facedown")),
    nar("facedown", '''{n}You turn the lens face down on the table. After a moment the silver ring grows cold enough to frost the wood around it, and letters form in the frost, reversed, so that you have to read them in your shaving mirror:{/n}
"Face down. As if that has ever stopped me. You offered me a wager at Iz, Commander. Pick me up."''',
        c("[Pick it up.]", "look")),
    ar("look", '''{n}Through the glass you see your own tent from above, as a bird would see it, and a woman's hand at a desk, writing. The hand pauses. Frost creeps across the lens from the other side, and letters form in it.{/n}
"You offered me a wager at Iz. I am told gamblers like to watch their opponents' faces. Here is mine. Try not to waste it."''',
        c('"You could have knocked."', "knocked"),
        c('[Joke] "Your handwriting is terrible. Is that the Abyss, or just you?"', "script"),
        c('[Breathe on the glass and write] "Show me your face."', "face")),
    ar("face", '''{n}The frost clears completely. For one long moment the glass shows you nothing but a desk, a lamp, and the edge of a sleeve. Then the sleeve moves, and the lamp is turned, deliberately, so that the light falls away from whoever is sitting there.{/n}
"No." {n}The letters form slowly this time.{/n} "You have seen my face at Iz, and you will see it again at Threshold. Here you may have my hand. It is the part of me that has done the most damage. It seems fair that it is the part you should watch."''',
        c("Continue", "knocked")),
    ar("script", '''"It is Sarkorian, and it was thought very fine, once, by people who are now in the Wound." {n}The frost thickens with something that might be irritation.{/n}
"You mock the hand that opened the Worldwound. Most people are too busy being frightened of what it wrote."''',
        c("Continue", "knocked")),
    ar("knocked", '''"I did knock. At Kenabres, at Drezen, in Alushinyrra. You were always too busy being alive to answer."
{n}The frost clears, and forms again.{/n} "Keep the lens. I will watch you through it, as I always have. You may watch me through it, if you can bear to. We will see which of us learns more before Threshold."''',
        c("[Keep the lens, and keep looking.]", "keep_looking", flags=(LENS_HELD,)),
        c("[Keep the lens, and put it away.]", flags=(LENS_HELD,))),
    nar("keep_looking", '''{n}You do not put it away. The frost clears, and forms again, faster, as if the hand on the other side had been waiting.{/n}''',
        c("Continue", "first")),
]), requires=(BET, "areelu.met"), forbids=(LENS_HELD,), delay=24)


# --- Chapter 5, her laboratory cell: the wager struck, after "One of us must burn" -----------------------------------

TERMS_CHOICES = (
    c('[Name your stake] "You stake what is left of you. I stake my wound. Whoever burns at Threshold pays up."', "sealed",
      mythic="Trickster", alignment=("Chaotic", 1)),
    c('[Refuse the Betrayer\'s bet] "I don\'t gamble with the woman who opened the Wound."', native_next=CELL_FAREWELL,
      flags=(CLOSED,)),
)

inline("areelu.trickster.wager.struck", "Whoever burns pays up", 5, '"One of us must burn. About that: I have a bet for you."', [
    ar("start", '''"A bet." {n}The projection folds its arms. Her outline shivers in the crystal's light.{/n}
"You have been saving it, I think. Well? Put it on the table. Mine is the only table left in the Abyss that you have not overturned."''',
        c('"You heard it at Iz. One of us burns, you say. I say neither."', "iz", requires=(BET,)),
        c('"You read it in the frost. One of us burns, you say. I say neither."', "frost", requires=(LENS,), forbids=(BET,)),
        c('"You asked me three questions through the frost. Here\'s the answer to a fourth: neither of us burns."', "fourth",
          requires=(LENS_ASKED,)),
        c("[Change your mind.]", abort=True)),
    ar("fourth", '''"A fourth question. I did not ask it." {n}The projection tilts its head.{/n} "Insolence, or guesswork. Neither. You have made that offer. Now name what you mean to wager. I do not accept jokes as collateral."''',
        c('"Then name what you would accept."', "terms")),
    ar("iz", '''"Neither." {n}She tastes the word the way she tasted it at Iz, and likes it no better.{/n}
"I have had since Iz to consider it. It is not a wager, Commander. It is a joke with the stake missing. I do not accept jokes as collateral."''',
        c('"Then name what you would accept."', "terms")),
    ar("frost", '''"Neither. You made the offer through my lens. Now say what you will put behind it." {n}Her outline steadies in the crystal's light.{/n} "I do not accept jokes as collateral."''',
        c('"Then name what you would accept."', "terms")),
    ar("terms", '''{n}She looks at you the way she looks at the Wound: from a great height, and very closely.{/n}
"If you burn, I keep the wound. For study." {n}Her hand of smoke gestures at your chest, where the old wound from Kenabres has never quite closed.{/n} "It was my mistake. I do not leave my mistakes to strangers."
"Those are my terms. And you are the first variable I could not predict, Commander. I intend to correct that, by measurement, before Threshold."''',
        *TERMS_CHOICES,
        c('"What\'s a joke, to you? Scientifically."', "joke"),
        c('"Don\'t you want to know why I\'d bet with you at all?"', "why_bet"),
        c('"You asked me what I felt at the crib. Ask me what I feel now."', "crib_sadness", requires=(CRIB_SAD,)),
        c('"You asked me what I felt at the crib. Ask me what I feel now."', "crib_rage", requires=(CRIB_RAGE,), forbids=(CRIB_SAD,)),
        c('"You asked me what I felt at the crib. Ask me what I feel now."', "crib_mystery", requires=(CRIB_MYSTERY,),
          forbids=(CRIB_SAD, CRIB_RAGE))),
    ar("why_bet", '''"No." {n}The answer comes too quickly, and she hears it come too quickly, and her mouth tightens.{/n}
"Yes. Very well. Yes. Everyone else who has stood in this cell came to kill me, or to beg me, or to ask me why. You came to gamble. I would like to know what you think you can win from a woman who has already lost everything that could be taken."''',
        c('"A reason to find out what you\'re like when you\'re not at war."', "not_war"),
        c('[Joke] "Your notes. I hear they\'re very thorough."', "her_notes")),
    ar("not_war", '''"I have not been anything but at war for a hundred years, Commander." {n}The projection looks down at its own hands of smoke.{/n}
"I do not know what I am like when I am not. Nobody does. I killed or outlived everyone who might have told you."
"That is a very poor prize to gamble for. You will be disappointed." {n}She lifts her chin.{/n} "Name your stake, or go."''', *TERMS_CHOICES),
    ar("her_notes", '''"My notes." {n}Something in the projection flickers, like a candle when a door opens.{/n}
"There are a great many of them. Most would kill you to read. A few would kill you to understand. One of them is about you, and it is the longest thing I have ever written."
"If you win, you may have it. You will not enjoy it. Name your stake, or go."''', *TERMS_CHOICES),
    ar("joke", '''"You arrange an experiment, withhold the result, and let someone else discover it at their expense. I recognise the method." {n}The projection steadies.{/n} "The world laughs when you do it. When I opened the Wound, it screamed. Name your stake."''', *TERMS_CHOICES),
    ar("crib_sadness", '''"You said sadness. I had enough of that beside the crib. It did not bring my child back." {n}The projection's hands remain still.{/n} "I found something else to do. Name your stake."''', *TERMS_CHOICES),
    ar("crib_rage", '''"You said rage. I recognised it." {n}She glances toward the ruined room.{/n} "I wanted the hunters dead. Then I wanted what they had taken. Killing them would not have been enough. Name your stake."''', *TERMS_CHOICES),
    ar("crib_mystery", '''"You said closeness to mystery. I would have preferred you look at the empty crib." {n}The projection turns back to you.{/n} "At Threshold you will learn why I kept it. Name your stake."''', *TERMS_CHOICES),
    ar("sealed", '''{n}For a moment the projection is perfectly still. Then she laughs, once, without any pleasure in it, and the device hums as if it had been struck.{/n}
"What is left of me. You do not even know what that is. Neither do I, any longer." "Very well."
{n}She holds out a hand of smoke and light. There is nothing there to shake, and she knows it. She waits anyway, to see whether you will pretend.{/n}''',
        c("[Shake the hand that isn't there.]", native_next=CELL_FAREWELL, flags=(STRUCK, STARTED, WITCH_BET)),
        c('[Joke] "I\'ll shake when you\'re here in person. Bring the real hand to Threshold."', native_next=CELL_FAREWELL,
          flags=(STRUCK, STARTED, WITCH_BET, REAL_HAND)),
        c("[Put your hand into the light where hers should be.]", "into"),
        c('[Joke] "Sure I know. Your notes. You\'re mostly paper by now."', "paper")),
    ar("paper", '''{n}The projection goes very still. Then, slowly, the corner of her mouth moves.{/n}
"Paper." "A century of it: the calculations on my cell wall, the soul research, every ledger of every crystal. And the graft. I knitted my own soul to the Abyss, Commander; that was a working, the longest I ever ran, and a working is work. Everything else I was went into the Wound." {n}She considers it the way she considers everything, from the end backwards, and you can see her decide that it is true.{/n}
"Very well. What is left of me is my notes. Remember that you said it, Commander. I always hold people to the terms they choose."''',
        c("[Shake the hand that isn't there.]", native_next=CELL_FAREWELL, flags=(STRUCK, STARTED, WITCH_BET, NAMED))),
    ar("into", '''{n}Your hand passes into the projection up to the wrist. There is nothing there: only a faint cold, like putting your hand into a stream in early spring, and the hum of the device in your bones.{/n}
{n}She does not move. She looks down at your hand inside hers, and her face gives you nothing at all to read.{/n}
"That is new," {n}she says at last.{/n} "The others struck at it, or wept at it, or smashed the device. You shook hands with a ghost to seal a bet. I will remember it. I remember everything that is done to me."''',
        c('"Until Threshold."', native_next=CELL_FAREWELL, flags=(STRUCK, STARTED, WITCH_BET))),
], requires=("trickster", "trickster.ever", PRIMED, "areelu.one_must_burn"), forbids=(STRUCK, CLOSED),
   lists=(CELL_LIST,), return_cue=CELL_RETURN)


# --- Chapter 6, the gate of Threshold: the wager named before she lets you in (a variant read only) -----------------

inline("areelu.trickster.threshold.welcome", "The wager stands", 6, '"Before I come in: the wager stands?"', [
    ar("start", '''"Stands?" {n}Areelu lowers her welcoming arms. The glow in her wound brightens and dims, like a slow breath.{/n}
"I have thought of little else, which annoys me. I made this prison into a laboratory, Commander, and the laboratory into a trap, and the trap into a door. And all the while, at the back of my mind, a voice saying: neither."''',
        c('"Sounds like you\'re losing sleep over me."', "sleep"),
        c('"Then you know I\'m not coming in to lose."', "lose"),
        c('[Joke] "Double or nothing?"', "double"),
        c('"You said you\'d keep my file until Threshold. Is it in there with you?"', "file", requires=(NOTICED,))),
    ar("file", '''"Every page." {n}She glances back over her shoulder at the black walls, as if she could see through them to a desk.{/n}
"It is the largest file I have ever kept, larger than the one on the Wound. The last entry is from last night. It says: 'Subject approaches. Subject will ask whether the wager stands.'" {n}Her smile is thin, and very old.{/n}
"You see? Sometimes I am right about you. Come in, and let us find out how often."''',
        c('"See you inside."', native_next=WELCOME_ON, flags=(REMINDED,))),
    ar("double", '''"Double of what?" {n}She looks you up and down, openly, the way a jeweller looks at a stone somebody else has overvalued.{/n}
"You have nothing left to stake that I do not already have a claim on. Your power is my gift. Your wound is my mistake. Your soul..." {n}She stops.{/n} "Your soul is a matter for inside."
"No. The wager stands as it was struck. I do not gamble twice on the same throw."''',
        c('"See you inside."', native_next=WELCOME_ON, flags=(REMINDED,))),
    ar("sleep", '''"I have slept badly for a hundred years. You have not improved it." {n}The smile she gives you is thin, and very old.{/n}
"Be flattered, if it pleases you. It is the last pleasure you will be offered in this place."''',
        c('"See you inside."', native_next=WELCOME_ON, flags=(REMINDED,))),
    ar("lose", '''"Nobody comes to Threshold to lose. Everyone who ever came here meant to win: the hunters, the jailers, the knights of every crusade, and I."
{n}She glances up at the black walls, and her mouth is very nearly fond.{/n} "The prison kept all of us. It will keep whichever of us burns."
"I built my door out of its stones, Commander. Every wall you pass inside was once a wall that held me. Look at them as you go. I would like somebody, once, to look."''',
        c('"See you inside."', native_next=WELCOME_ON, flags=(REMINDED,))),
], requires=("trickster.ever", STRUCK), forbids=(CLOSED, REMINDED), lists=(WELCOME_LIST,), return_cue=WELCOME_RETURN)


# --- Chapter 6, her demiplane: after she tells how the hunters came (a beat between the wager and the fight) ----------

inline("areelu.trickster.truth.the_desk", "At the desk", 6,
    '"You were at your desk, writing, when they came. You\'ve been sitting at that desk ever since."', [
    ar("start", '''{n}Areelu goes very still. In the demiplane the distant voices fall silent all at once, as if a hand had been laid over their mouths.{/n}
"Yes." {n}She says it the way one confirms a measurement that has been checked too many times.{/n}
"Recording my observations, as was my habit. I have never stopped. If I stop, Commander, I will have to get up from the desk, and go outside, and see."''',
        c('"Then don\'t get up yet. Finish the entry. I\'ll wait."', "wait"),
        c('"Threshold\'s hunters wanted a witch to burn. A hundred years on, they still haven\'t got one."', "witch"),
        c('"In your cell you said you did it because you made a promise. That was the promise, wasn\'t it?"', "promise"),
        c('"What were you writing? That night, at the desk."', "writing"),
        c('[Joke] "Whatever you burn today, I hope it\'s the paperwork."', "paperwork")),
    ar("paperwork", '''{n}For a moment you think you have misjudged it badly. Her face goes perfectly still.{/n}
"The paperwork." {n}Then the line of her mouth gives, very slightly.{/n} "A hundred years of it. Calculations on walls, on skin, on the backs of death warrants. If you could burn only that, Commander, and leave the rest of me standing, you would be the first person in history to settle an argument with the Abyss by losing its files."
"Do not look so pleased. It was not a compliment. It was a hypothesis."''',
        c("[Let her go on.]", native_next=TRUTH_ON)),
    ar("writing", '''{n}She answers at once, as if she had read it every day since.{/n}
"An observation about a moth. It had come in through the window and was beating itself against the lamp, and I wanted to know how many times it would strike the glass before it understood that the glass would not give."
"Forty-one." {n}Her voice does not change at all.{/n} "It understood at forty-one. I wrote the number down. Then I heard the noise outside."''',
        c("[Let her go on.]", native_next=TRUTH_ON)),
    ar("promise", '''"Yes." {n}Her hands, which have been still, close into fists.{/n}
"I held my child at the door, and I promised. I did not promise revenge. Revenge is small; anyone can have it. I promised that the world would not stay as it was, a world where that could happen and the gods would call it justice."
"I have kept it, Commander. Look around you. Every promise I make, I keep. Remember that, when you hold me to our wager."''',
        c("[Let her go on.]", native_next=TRUTH_ON)),
    ar("wait", '''{n}She looks at you. Something in her face that has been held shut for a century moves, very slightly, like a door in a draught.{/n}
"You will wait." "Everyone else came through the door. The hunters, the jailers, the knights of every crusade. You would stand outside it. That is either courtesy or strategy, and in you I cannot tell them apart."
{n}She turns away before you can see what her face does next.{/n} "Do not do that again. I do not have the time to study it."''',
        c("[Let her go on.]", native_next=TRUTH_ON)),
    ar("witch", '''{n}Her laugh is short, and dreadful to hear.{/n} "They have wanted one since before your crusade had a name."
"Very well. If I burn today, I will burn as your wager, Commander, and not as their witch. It is a small distinction." {n}Her mouth tightens.{/n} "I find, to my irritation, that I prefer it."''',
        c("[Let her go on.]", native_next=TRUTH_ON)),
], requires=("trickster.ever", STRUCK), forbids=(CLOSED,), lists=(TRUTH_LIST,), return_cue=TRUTH_RETURN)


# --- Chapter 6, at the rift before the fight: what she will do with the stake ----------------------------------------

inline("areelu.trickster.rift.odds", "What the winner keeps", 6,
    '"Before we fight: if you win the wager, what will you do with my wound?"', [
    ar("start", '''{n}Areelu turns from the rift. The violet light makes her look as if she were carved out of it.{/n}
"Study it." {n}She says it at once, without pleasure, the way one gives a figure.{/n}
"I will cut it out of what is left of you, very carefully, and keep it in my laboratory, and learn from it everything I failed to learn while it was open. It was my mistake. I do not leave my mistakes lying on a battlefield."''',
        c('"And if neither of us burns?"', "neither"),
        c('[Joke] "That\'s the most romantic thing anyone\'s ever said to me."', "romantic"),
        c('"And if I win? What do I get?"', "win"),
        c('"You keep looking at my belt."', "belt", requires=(CAULDRON_HELD,)),
        c('[Joke] "If I win, can I keep your notes? As a souvenir."', "souvenir")),
    ar("souvenir", '''"A souvenir." {n}She says it as though tasting something she has never been offered before and does not trust.{/n}
"A century of the most dangerous research ever done on Golarion, bound in the skins of things you do not want to know about, and you would put it on a shelf beside a seashell." "No. If you win, the notes burn. I will not leave my method for the first fool who can read it."''',
        c('"And if neither of us burns?"', "neither")),
    ar("belt", '''"At the Council's cauldron. Yes." {n}Her eyes stay on it, the way a physician's stay on a blade.{/n}
"It drinks the essence of another plane; that is what they built it for, and it does it well. I am half another plane, Commander. I sewed the Abyss into my own soul at the edge of this rift. Put that crystal against me and it would drink, and I do not know whether it would stop."
"If you ever mean to find out, tell me first. I will want to watch."''',
        c('"And if neither of us burns?"', "neither")),
    ar("win", '''"If you win, I burn, and you get what is left of me." {n}She spreads her hands, and the violet light runs over them like water.{/n}
"Look closely. A wound that will not close. A century of notes nobody else can read. Two demon lords who would like me dead, and a goddess who has been waiting for my page since before your crusade was born."
"That is my stake, Commander. You may find, when you collect it, that you have won a great deal of trouble."''',
        c('"And if neither of us burns?"', "neither")),
    ar("romantic", '''"Then you have been courted badly." {n}Her gaze returns to your chest.{/n} "Every hour I spend on you is an hour I do not spend on my child. I resent the expense. I have not yet decided to stop paying it."''',
        c('"And if neither of us burns?"', "neither")),
    ar("neither", '''"Then I will have lost." {n}The wound above her heart pulses once, brightly.{/n}
"And I do not lose, Commander. I adjust the initial conditions, and I try again. But you ask as though you have already arranged it." {n}She studies your face.{/n} "Have you?"''',
        c('"Ask me after."', "after"),
        c('[Joke] "I never arrange anything. I just leave the door open and see who walks in."', "doors"),
        c('"You said I was costing you hours. Am I?"', "feelings")),
    ar("feelings", '''{n}The violet light throws her shadow between you.{/n} "I want you alive when this is over. I had other plans for you. I have not abandoned them." {n}She looks toward the rift.{/n} "If you mean to make something of that, survive long enough to try."''',
        c('"It\'ll matter after."', "after"),
        c("[Say nothing, and hold her gaze.]", "after")),
    ar("after", '''"After." {n}She repeats the word as if it belonged to a language she used to speak, a long time ago.{/n}
"Very well. I will ask you after. One of us will be there to answer."
{n}She turns back to the violet flames, and adds, without looking at you, so quietly that you almost miss it:{/n} "I find that I would like it to be both."''',
        c("[Let her turn back to the rift.]")),
    ar("doors", '''"Doors." {n}She glances at the rift behind her: the greatest open door in the world, which she made.{/n}
"Yes. I know something about doors, Commander. I know what walks in."''',
        c("[Let her turn back to the rift.]")),
], requires=("trickster.ever", STRUCK), forbids=(CLOSED,), lists=(RIFT_LIST,), return_cue=RIFT_RETURN)


# --- Chapter 6, the respite after the first fight: the clause about burning by one's own hand -------------------------

inline("areelu.trickster.witch.the_clause", "The clause", 6,
    '"Whatever you\'ve hidden in this room, remember our terms. Whoever burns pays up. That includes burning yourself."', [
    ar("start", '''"The terms." {n}Areelu is swaying on her feet. Her hands will not keep still; she wrings them, and looks at them, and wrings them again.{/n}
"You would stand in the ruin of everything I built and quote my own wager at me, like a clerk reading a contract to a debtor."''',
        c('"If you burn by your own hand, you lose. In front of a witness."', "clause"),
        c('"You\'d rather die than let me win?"', "rather"),
        c('[Joke] "I\'d hate to win by forfeit. It\'s so undignified."', "forfeit")),
    ar("forfeit", '''"Undignified." {n}The word comes out of her like a cough.{/n} "You stand in my fortress, over my ruin, with my blood on your weapon, and you are worried about dignity."
"Very well. I will not hand you a forfeit. If I burn, you will have to earn it." {n}Her hands go still at last.{/n} "Remember that you asked for the hard way."''',
        c("[Wait.]")),
    ar("rather", '''"I would rather die than let anyone win. I have been doing it for a hundred years." {n}Her voice cracks on the last word, and she hates that it does.{/n}
"You are not special, Commander. You are merely the last."''',
        c('"Then you\'d lose twice. Once to me, and once to the rules you wrote."', "clause")),
    ar("clause", '''{n}She stops wringing her hands.{/n}
"You would hold me to that. Now. Here." {n}Something that is almost a laugh escapes her, and it hurts her to let it out.{/n} "It is a very good clause. I wrote it myself, and did not read it back."''',
        c('"Then don\'t lose."', "dont_lose"),
        c('[Joke] "Read the small print. Burning yourself counts double."', "double")),
    ar("dont_lose", '''{n}She looks at you with something very like hatred, and something else under it that she will not name.{/n}
"I will do exactly as I please with my own life, Commander. It is the only thing in this fortress that was ever mine." "But I will remember that you said it."''',
        c("[Wait.]")),
    ar("double", '''"There is no small print." {n}A pause.{/n} "...There is now. I can see it on your face."
{n}She closes her eyes. When she opens them the madness in them has banked, a little, like a fire someone has decided to keep until morning.{/n} "Very well. It is noted. Do not expect me to thank you for the footnote."''',
        c("[Wait.]")),
], requires=("trickster.ever", STRUCK), forbids=(CLOSED,), lists=("34fc03a7642d21642a4fb2bb7a0e056e",),
   return_cue="3e52b05af622f5945905b2be5ed9ac5a")   # AreeluBurnTheWitch/AnswersList_0003; Cue_0041 "a grim, lifeless smile"


# --- Chapter 6, defeated at Threshold (E14b): the late wager and the wager raised (the commit, in play) ---------------

LATE_TAKE = c('[Take her terms] "You stake what is left of you. I stake my wound. Whoever burns at Threshold pays up."',
              mythic="Trickster", alignment=("Chaotic", 1), flags=(STRUCK, STARTED, WITCH_BET, LATE))
LATE_REFUSE = c('[Refuse] "No bets with you."', flags=(CLOSED,))

at_threshold("areelu.trickster.wager.at_threshold", "Terms, and worse", '"Before this ends, Areelu: I still have a bet for you."', [
    ar("start", '''"A bet, now? Here?" {n}She laughs, and it costs her. The wound above her heart bleeds afresh.{/n}
"You never brought the wager to a conclusion. So the terms are mine, and they are worse. If you burn, I keep the wound. If I burn, you keep nothing: not my notes, not my name. Well?"''',
        LATE_TAKE, LATE_REFUSE,
        c('"Why worse?"', "worse"),
        c('[Joke] "Worse terms? I love a bargain."', "bargain"),
        c("[Say nothing.]", abort=True)),
    ar("bargain", '''"This is not a bargain. This is a woman bleeding on the floor of her own prison, offering you the last thing she owns at a terrible price." {n}She coughs, and there is blood in it.{/n}
"I have offered better terms to demon lords. They had the good manners to be on time." "Take it or leave it, Commander. I will not be asking twice."''',
        LATE_TAKE, LATE_REFUSE),
    ar("worse", '''"Because you came late, and I have never rewarded lateness. Because I am bleeding and you are not."
{n}She presses her palm to the wound, looks at the blood on it with professional detachment, and wipes it on her robe.{/n}
"And because the only thing I have left to wager is my name. I will not stake that on a clown who waits until the last moment to name a stake."''',
        LATE_TAKE, LATE_REFUSE,
        c('"Your name? What would I do with your name?"', "name")),
    ar("name", '''"Nothing. That is the point." {n}She laughs, and it turns into a cough.{/n}
"Everyone who has ever wanted my name wanted it for a gallows or a chronicle. Mendev would burn it. Sarkoris's ghosts would curse it. Your crusade would carve it over a door so that people could spit as they passed."
"If I burn, you keep none of it. It goes into the fire with me, and nobody has it, and that is the only mercy I am prepared to show you. Take the terms, or leave them."''',
        LATE_TAKE, LATE_REFUSE),
], requires=("trickster", PRIMED), forbids=(STRUCK, CLOSED))

# Sol quality pass (INT): the Commander who never offered the bet at Iz and never kept the lens still has one entry, here,
# with the live Trickster. Her terms are the harshest in the route: the wound is ceded before anything else is said.
UNPRIMED_TAKE = c('[Take her terms] "My wound now, your work if you burn, and I keep nothing. Done."', mythic="Trickster",
                  alignment=("Chaotic", 1), flags=(PRIMED, STRUCK, STARTED, WITCH_BET, LATE, NAMED, WOUND_CEDED, UNPRIMED))
UNPRIMED_REFUSE = c('[Refuse] "Not at that price."', flags=(CLOSED,))

at_threshold("areelu.trickster.wager.unprimed", "No credit at this table",
    '''"One of us burns so the other lives. I have a bet for you. My money's on neither."''', [
    ar("start", '''"Neither." {n}She is on her knees in her own blood, and she looks at you as though you had tried to pay a physician in buttons.{/n}
"You never brought me a wager. Not to my cell, not through my glass. You fought your way through my fortress without a word about it, and now, with my life on the end of your blade, you would like to gamble." {n}Her mouth thins.{/n} "A wager is struck between parties who can both still lose. Only one of us can lose now, and it is not you."''',
        c('"Then make it so I can lose. Name a price."', "price"),
        c('[Joke] "I\'m a late bloomer."', "bloomer"),
        c("[Say nothing.]", abort=True)),
    ar("bloomer", '''"You are a late payer. Bloom somewhere else." {n}She coughs, and wipes her mouth, and looks at the red on her fingers with more interest than she gives you.{/n}
"But you have come to the right creditor. I set terms for people who arrive with nothing. I have done it for demons."''',
        c('"Then set them."', "price")),
    ar("price", '''"Very well. The wound in your chest is mine. Not if you lose: now, before I say another word, win or lose, for study, for the rest of your life. That is the entry fee."
"Then the wager. If I burn, you collect what is left of me, which is my work, and the graft that is part of it; and you keep nothing of mine afterwards. Not a page. Not my name." {n}She holds your eyes.{/n} "If you want neither, Commander, you will have to arrange it. I will not help you, and I will not thank you."''',
        UNPRIMED_TAKE, UNPRIMED_REFUSE,
        c('"Why the wound first?"', "why")),
    ar("why", '''"Because you are late, and people who are late do not pay afterwards. They leave." {n}She presses her palm flat to her own wound and holds it there.{/n}
"I have held collateral from better gamblers than you. I have never once been paid by someone who was allowed to settle at the end."''',
        UNPRIMED_TAKE, UNPRIMED_REFUSE),
], requires=("trickster",), forbids=(PRIMED, STRUCK, CLOSED))

SETTLED = c('[Shake on it] "Then it\'s settled."', flags=(COMMITTED,))

at_threshold("areelu.trickster.wager.collect", "Into the cauldron", '[Take out the soul cauldron] "Time to collect the stake."', [
    ar("start", '''{n}Areelu looks at the crystal in your hands: the Council's soul cauldron, a diamond in a gold cradle, made to draw the essence of another plane.{/n}
"The Council's toy." {n}Her gaze moves from the crystal to her wound.{/n} "What is left of me is my work, we said. The graft is work. It is the essence of another plane, sewn into a Sarkorian woman's soul, and that thing was made to drink exactly that."
"And you have paid for the substitution. Your wound is mine, win or lose; my work goes into your crystal in place of my life, if the rift will take it. Those are the terms. I will not hear them improved." {n}She looks at the diamond again.{/n} "You mean to take the Abyss out of me with a trinket, here, before you choose."''',
        c('"Will the rift take it in your place?"', "contest"),
        c("[Put the cauldron away.]", abort=True)),
    ar("contest", '''"I do not know." {n}She says it as if it were the most interesting sentence she has spoken in a century.{/n}
"Two hypotheses. If the rift wants a quantity of the Abyss, it will take what is in the cauldron and be satisfied. If it wants a life, it will take me anyway, the cauldron will have hurt me for nothing, and you will have lost the bet and kept nothing." "I accept the experiment. I intend to see which answer survives." {n}She lifts her chin, and the wound above her heart pulses once, violet.{/n} "Well? Collect."''',
        c('[Collect the stake] "Whoever burns pays up. Pay into this."', "drawn", mythic="Trickster"),
        c("[Put the cauldron away.]", abort=True)),
    ar("drawn", '''{n}You set the cradle against the wound above her heart. For a moment nothing happens. Then the violet light comes out of her like blood from a cut: slowly, then all at once, pouring into the diamond until it glows like a small, furious star.{/n}
{n}She does not scream until the end. When it comes, it is the sound of something a century old being unstitched. The crimson goes out of her eyes. She stays on her feet, because she refuses to do anything else.{/n}''',
        c("Continue", "after", forbids=(CAULDRON_FULL,)),
        c("Continue", "full", requires=(CAULDRON_FULL,))),
    ar("after", '''"There." {n}Her voice is hoarse now, very tired, and nothing moves in the shadows when she speaks.{/n}
"The cauldron holds a life's worth of the Abyss. Whether it holds a life, we will learn at the rift, and not before." {n}The diamond is cracked along one face; a thread of violet light leaks from the crack and fades.{/n} "It held. It may not hold long enough. If it does not, the rift will take me anyway, and you will have paid for a trinket with the only part of me that did not hurt." {n}She looks at her own hands, and they are shaking, and she lets them.{/n} "It hurts, Commander. I had forgotten that anything could."''',
        c("[Turn to the final choice.]", flags=(DRAWN,))),
    ar("full", '''{n}Two lights turn inside the diamond: what the Council poured into it, and what came out of her. A crack opens along one face.{/n} "It held both. For now. Do not put it away and leave me standing here without the power you just took. Choose."''',
        c("Continue", "after")),
], requires=("trickster.ever", STRUCK, NAMED, WOUND_CEDED, CAULDRON_FULL), forbids=(DRAWN, CLOSED, STAKE_ONLY, DECLINED, LIFE_TERM))   # the CommittedFlag producer (node her_choice, choice 0)

at_threshold("areelu.trickster.wager.raised", "A longitudinal experiment", '"The wager, Areelu."', [
    ar("start", '''"The wager stands, Commander. One of us burns." {n}Areelu does not lower her chin. Blood runs from the wound above her heart, and she does not look at it.{/n}
"Unless you have come to change the terms. You have that look."''',
        c('''[Raise the stakes] "If neither of us burns, you keep studying me. At close range. For as long as you choose to stay."''',
          "thirty", requires=(WAGERED,), forbids=(LATE,)),
        c('''[Raise the stakes on your late terms] "Keep your terms. If neither of us burns, you keep studying me, at close range, for as long as you choose to stay."''',
          "late_raise", requires=(WAGERED, LATE)),
        c('"At the gate you said you\'d thought of little else. Neither had I."', "gate", requires=(REMINDED,)),
        c('[Ask her to raise them] "Raise them? Here? You\'d have to trust me."', "refused"),
        c('[Collect the stake only] "Only the stake. Nothing more."', flags=(STAKE_ONLY,)),
        c("[Leave it for now.]", abort=True)),
    ar("late_raise", '''"You came late to the wager, Commander, and now you wish to raise it." {n}She wipes the blood from her lip with the back of her hand.{/n}
"The late terms stand. If I burn, you keep nothing: not my notes, not my name. I will not improve them because you have a pleasant voice and I am losing."
"But you may raise. Raising is a different matter. I have never refused to hear a higher bid."''',
        c("Continue", "thirty")),
    ar("gate", '''"I said it at the gate. I remember everything I say at gates." {n}Something in her face, under the blood and the exhaustion, turns very faintly toward you.{/n}
"Neither had you. You say it as though it were a confession. It is not. It is a data point."
"Well? You did not come all this way to agree with me. Say what you came to say."''',
        c('''[Raise the stakes] "If neither of us burns, you keep studying me. At close range. For as long as you choose to stay."''',
          "thirty", requires=(WAGERED,)),
        c('[Ask her to raise them] "Raise them? Here? You\'d have to trust me."', "refused")),
    ar("thirty", '''"As long as I choose." {n}She wipes the blood from her palm.{/n} "You offer me time you cannot guarantee. Very well. Tell me what happens if I burn."''',
        c('''"Then hear my stake."''', "collect", forbids=(YEARS_ASKED,)),
        c('''"You said years or decades. I want the time you have."''', "decades", requires=(YEARS_ASKED,)),
        c('''[Joke] "You can object to my company after we survive."''', "collect")),
    ar("decades", '''"Years, or decades. I did not say which. If we leave here alive, I intend to use them." {n}She looks toward the rift.{/n} "First we must settle what you collect."''',
        c("Continue", "collect")),
    ar("collect", '''"And if I burn, Commander?" {n}Her eyes do not leave your face.{/n} "You have never said what you collect. 'What is left of me' is not a quantity. I will not accept a term I cannot measure."''',
        c('"Your notes. A century of them. That\'s what\'s left of you."', "priced", forbids=(NAMED,)),
        c('"We named it in your cell. Your notes."', "priced_known", requires=(NAMED, "areelu.trickster.wager.struck")),
        c('"Your life. Nothing less."', "life", forbids=(DRAWN,)),
        # Sol PP8 r1 (CAN): the stake was named here at Threshold, never in her cell (appended).
        c('"Your notes. As we agreed, here."', "priced_agreed", requires=(NAMED,), forbids=("areelu.trickster.wager.struck",))),
    ar("priced_agreed", '''"My work, then. The notes, and the graft with them. I made myself, Commander. What I made is work." {n}Blood runs from her wound.{/n} "Your wound is mine, win or lose. Those are the terms for letting the paper burn in my place. Agree, or name another stake."''',
        c('"Agreed."', "her_choice", flags=(NAMED, WOUND_CEDED)),
        c('"No. Not the wound."', "life")),
    ar("priced", '''"My notes." {n}She is silent, and you can watch her test it, the way she tests everything: from the end backwards.{/n}
"Yes. A century of paper. That is exactly what is left of me; everything else went into the Wound." {n}She touches the wound above her heart.{/n} "And the graft that holds the Abyss in me. I made myself, Commander. That was a working too, and a working is work. If you collect my work, you collect the stitch." "Very well. If you collect my work in place of my life, you pay for the privilege. Your wound is mine, win or lose. For study."''',
        c('"Agreed."', "her_choice", flags=(NAMED, WOUND_CEDED)),
        c('"No. Not the wound."', "life")),
    ar("priced_known", '''"My notes. Yes. You said so in my cell, and I have thought of little else. The notes, and the graft with them: I made myself, and what I made is work." {n}Blood runs from her wound; she does not look at it.{/n}
"Then this is what it costs you, to let paper burn in my place. Your wound is mine, win or lose. For study. You will not get a better term from me, and you will not get this one twice."''',
        c('"Agreed."', "her_choice", flags=(NAMED, WOUND_CEDED)),
        c('"No. Not the wound."', "life")),
    ar("life", '''"My life, then." {n}She nods, once, as if a sum had come out the way she expected.{/n}
"That is the term the hunters wanted, and the Queen's knights, and the Lady of Graves. You are in good company, Commander. If I burn, I burn, and you collect nothing but ash."''',
        c("Continue", "her_choice", flags=(LIFE_TERM,))),
    ar("her_choice", '''{n}Areelu studies your face. Her hand remains pressed to the wound.{/n} "You have me beaten, and you are bargaining. I would like to know why. If neither of us burns, I stay close enough to find out. You keep my company, and I keep my notes."
"Do not mistake that for surrender. When it ceases to serve me, I leave." {n}She holds out her bloody hand.{/n} "Very well. I accept."''',
        SETTLED,
        c("[Take her hand. The real one, this time.]", "hand", requires=(REAL_HAND,)),
        c("[Kiss her.]", "kiss")),
    ar("kiss", '''{n}You cup her face and kiss her. She catches the back of your neck, pulling you hard against her mouth. Her palm leaves a smear of blood along your jaw. When she breaks the kiss, her hand stays where it is.{/n} "That was not in the wager." {n}Her eyes return to your mouth.{/n} "Put it in."''',
        c('"Then it\'s settled."', flags=(COMMITTED,))),
    ar("hand", '''{n}Her hand is cold, slick with her own blood, and much stronger than it looks. She grips back hard enough to hurt, and does not let go when a sensible person would.{/n}
"There. The real one, as you asked in my cell." {n}She lets go at last.{/n} "You will find, Commander, that I keep every appointment I make."''',
        c('"Then it\'s settled."', flags=(COMMITTED,)),
        c("[Raise her hand to your mouth.]", "kissed")),
    ar("kissed", '''{n}You kiss the back of her bloody hand. Her fingers close on yours.{/n} "You have chosen a strange time to court me." {n}She does not pull away.{/n} "Do it again after Threshold. I would like to see whether you still mean it."''',
        c('"Then it\'s settled."', flags=(COMMITTED,))),
    ar("refused", '''"No." {n}She says it without heat.{/n}
"I do not renegotiate at the edge of the Wound, with a sword at my throat. The wager stands as it was struck. Collect your stake, if you win it. Nothing more."''',
        c('[Accept her refusal] "Then nothing more."', flags=(DECLINED,)),
        c('"You\'re afraid you\'d lose."', "afraid")),
    ar("afraid", '''"I am afraid of nothing that can be calculated." {n}The blood has reached her wrist. She lets it.{/n}
"You cannot be calculated. That is the whole of my objection, Commander, and it is enough. The answer is no."''',
        c('[Accept her refusal] "Then nothing more."', flags=(DECLINED,))),
], requires=("trickster.ever", STRUCK), forbids=(COMMITTED, CLOSED, DECLINED, STAKE_ONLY))


# After "Here are my last words - I regret nothing." (GrandFinal/Cue_0050), beside the final choice (E14b).
SCENES.append(scene("areelu.trickster.wager.last_words", "Nothing to regret", "Areelu", 6,
    '''"Regret nothing? Good. You'll want a clear head for what comes after."''', [
    ar("start", '''{n}Areelu raises her chin. Blood has dried on it.{/n} "You speak as if there will be time after this. Choose, Commander. I would like to find out whether you are right."''',
        c('''"We will."''', "will"),
        c('''[Joke] "The small print says we survive."''', "print"),
        c('"Whatever I choose now, the wager stands."', "stands")),
    ar("stands", '''"The wager stands." {n}She says it the way a priest says the end of a prayer: not hoping, only confirming.{/n}
"Whoever burns pays up. I have not forgotten a single clause, Commander, and I will not begin now." {n}She looks past you, at whatever you are about to do.{/n} "Go on. I am watching. I have always been watching."''',
        c("[Turn to the final choice.]")),
    ar("will", '''"Then choose. I will not beg, and I will not flinch. If your wager works, I intend to be awake to see it."''',
        c("[Turn to the final choice.]")),
    ar("print", '''{n}She looks down at the blood drying on her hand.{/n} "You would add a clause now. Very well. Choose, Commander. If there is an afterwards, I intend to collect."''',
        c("[Turn to the final choice.]")),
], requires=("trickster.ever", STRUCK), forbids=(CLOSED, STAKE_ONLY), last=6, optional=True, Relationship="areelu",
   Chapters=[6], AnswerLists=["b6bc1d5fb28e115499b8bcbbc0d541f9"], ReturnToList=True,   # GrandFinal/AnswersList_0052
   ReturnText="{n}Areelu waits for your choice. She regrets nothing.{/n}"))


# --- Reactions (ledger 05 section 3.1 row 4: exactly Nenio and Ember) --------------------------------------------------

SCENES.extend([
    reaction("Nenio", "areelu.trickster.react.nenio_two_drafts", (STRUCK,),
             '''"I have written two drafts of the Architect's entry for my encyclopaedia." {n}Nenio holds up two sheets, one in each hand, like a scale.{/n}
"One says 'deceased'. The other says 'bankrupt'. I will publish whichever one your joke makes true."
{n}She lowers them, and her ears flatten a little.{/n} "I have also left a third sheet blank. I do not like the third sheet. It is the only entry in the whole encyclopaedia that I cannot finish by research."''',
             answer_list=NENIO_HUB, forbids=("nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out"),
             chapter=5, last=6, entry='"I made a wager with Areelu."',
             # G6(b), added with Nenio's route: her Trickster return lifts every loss but the dissolution.
             ForbidOverrides={k: NENIO_BACK for k in NENIO_GONE if k != "nenio.dissolved"}),
    reaction("Ember", "areelu.trickster.react.ember_regret", (BET,),
             '''"You made a bet with the sad lady." {n}Ember twists a strand of hair around one finger.{/n} "She wants something so much that she hurts everyone trying to reach it. If you win, will you listen to what she wanted? You don't have to let her hurt anyone else to listen."''',
             answer_list=EMBER_HUB, forbids=("ember_dead", "ember_gone"), chapter=5, last=6, entry='"About Areelu..."'),
    reaction("Seelah", "areelu.trickster.react.seelah_objects", (COMMITTED,),
             '''{n}Seelah hears it from someone else first, and comes to find you with her holy symbol in her fist and her jaw set.{/n}
"Areelu Vorlesh. The woman who opened the Worldwound. Who made the Wound in you, and in me, and in every child in Sarkoris who never grew up."
"I am not going to tell you what to do with your heart, Commander. The Inheritor never told me what to do with mine. But I will not stand at your side and call it anything but what it is. If she lays a hand on you that I do not like, I will cut it off, and I will pray for her afterwards, and I will mean both."''',
             answer_list=SEELAH_HUB, forbids=("seelah_dead", "seelah_gone"), chapter=6, last=6,
             # G6(b): a Seelah who died or left and came back on her own Trickster route is on her hub again.
             ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"},
             entry='"About Areelu..."'),
])


# --- The finale pages (F20, the epilogue rewrite; R2-0e: no page sets a flag, none carries mythic or alignment) -------
#
# One ordered chain in the native PlayerFinalChoice sequence, right after the Trickster ending page (BookPage_0147):
# rewrite -> after -> survived -> the report. Each page carries its own gates; a page whose gates fail is skipped and the
# chain keeps its order (E14h anchors are positions, not requirements).

COMMITTED_ANY = [COMMITTED, LATE_COMMITTED]
ROMANCE_FORBIDS = (DECLINED, STAKE_ONLY, CLOSED, BURNED)
ROMANCE_OVERRIDES = {DECLINED: COMMITTED}
MORTAL = (DRAWN,)                         # her body after Threshold: the graft drawn into the siphon (rewrite or punchline)
RETIRED = RETIRED + (P + "report.afterword",)   # folded into the promise page's own branches (Sol BEL); gated off


def page(id, title, nodes, requires, forbids=(), any_groups=(), after=None, sequence=True, overrides=None):
    extra = dict(Relationship="areelu")
    if any_groups:
        extra["RequiresAnyGroups"] = [list(g) for g in any_groups]
    if overrides:
        extra["ForbidOverrides"] = dict(overrides)
    if sequence:
        extra["EpilogueSequence"] = "PlayerFinalChoice"
        extra["EpilogueAfter"] = after or TRICKSTER_PAGE
    SCENES.append(scene(id, title, "Epilogue", 1, "", nodes, requires=requires, forbids=forbids, last=99, **extra))


NATIVE_DEATHS = (SAC_TRICK, FIGHT, INCINERATED, SAC_WOUND, SAC_BEFORE)   # the members of DIED (a Derived key cannot be overridden)


def report(id, title, nodes, after, any_group=None, forbids=()):
    """A page of her report after Threshold: she survived, drawn (mortal: no magic, ageing) or not (the half-demon witch).
    A native death is lifted only by the rewrite on the collected stake (Sol INT: CHEATED alone never revives her)."""
    # A one-flag any_group is a plain requirement (gate lint E2a): it joins Requires rather than becoming a group.
    single = tuple(any_group) if any_group and len(any_group) == 1 else ()
    groups = (COMMITTED_ANY,) + ((tuple(any_group),) if any_group and not single else ())
    page(id, title, nodes, requires=("trickster.ever", STRUCK, WAGERED, SURVIVES) + single,
         forbids=ROMANCE_FORBIDS + NATIVE_DEATHS + tuple(forbids), any_groups=groups, after=after,
         overrides=dict(ROMANCE_OVERRIDES, **{SAC_TRICK: REWRITTEN, FIGHT: REWRITTEN}))


page("areelu.trickster.finale.rewrite", "What burned", [
    nar("end", '''{n}The soul cauldron burst at the edge of the rift. Its sparks caught Areelu and dragged her toward the opening. She braced one hand against the stone; the other closed over the wound in her chest.{/n}''',
        c("[Wait while she takes her inventory.]", "inventory"),
        c("[Joke] \"Welcome to being mortal. The food's better than you'd think.\"", "mortal"),
        paragraphs=(
            p('''{n}The violet light tore past her into the rift. The Commander had drawn her graft into the Council's vessel before the final choice. When the crystal broke, the rift took that stored essence and left the woman on the stone. She watched until the last spark vanished.{/n} "It took the quantity," {n}she said.{/n} "I want that recorded."'''),
            p("{n}The laboratories of Threshold burned in the same fire: a century of notes, the soul research, the "
              "Nahyndrian ledgers, every page she had written in that prison. She watched them go from the edge of the "
              "rift and did not try to save one. They had been part of the stake too.{/n}"),
            p("{n}It cost the Commander the wound. That had been her price at Threshold for letting the cauldron take the "
              "Abyss in her place: win or lose, the Commander's wound was hers to keep, for study. She collected it the "
              "same night, with a silver probe, and it never closed again for anyone but her.{/n}", requires=(WOUND_CEDED,)),
            p("{n}It cost her the stake she had put on the table herself. The Commander had come late to the wager, and had "
              "agreed to worse terms: whatever burned, the Commander was to keep nothing of hers. The Commander kept "
              "nothing. She kept the rest.{/n}", requires=(LATE,)),
            p("{n}The lens she had sent the Commander cracked straight across in that same moment, in a pack on the "
              "floor of Threshold, with a sound like a small bone breaking. Nobody noticed but the Commander.{/n}",
              requires=(LENS_HELD,)),
            p("{n}The woman walked out of the smoke with grey at her temples, no magic at all, and ink on her fingers that "
              "would not wash off.{/n}"),
            p("{n}She did not take the hand the Commander held out. She looked at it: the real one, as asked for in her "
              "cell.{/n} \"Not yet,\" {n}she said.{/n} \"I am taking an inventory.\"", requires=(REAL_HAND,)),
            p('''{n}She watched the smoke above the workrooms, then turned toward the way out. "Go. I have paid. I will not stand here while you admire it."{/n}'''),
        )),
    nar("inventory", '''{n}She sat in the ash and tried a word of power. Nothing. A gesture that had once split stone. Nothing. Last she counted her own pulse, holding her wrist so tightly that her fingers left white marks.{/n} "Gone." {n}She pressed her shaking hands together until they steadied.{/n} "I would like a moment before you tell me I should be grateful."''',
        c("Continue", "terms")),
    nar("mortal", '''{n}"Mortal." She tried a word of power on the Commander, very deliberately, to see what would happen. Nothing happened. "You took a century from me with a crystal and a pun, and you are recommending the food."{/n}
{n}Her hands were shaking. She held them up between them and looked at them, and let the Commander see her look.{/n}''',
        c("Continue", "terms")),
    nar("terms", '''{n}When she stood up, her face was composed again, and colder than the Commander had ever seen it.{/n}
{n}"Here is what I will do," said Areelu Vorlesh. "I will follow you until I understand how you did it. Not because I want to. Because I lost, and I do not leave an experiment until I know why it failed. You will not read my notes. You will not pity me. When you cease to interest me, I will go, and I will not say goodbye."{/n}''',
        c('"Deal."'),
        c("[Say nothing. Hold out your hand again.]", "hand_again")),
    nar("hand_again", '''{n}She takes the offered hand and pulls herself to her feet. Her grip hurts.{/n} "I lost the wager. I have not agreed to be carried."''')],
    requires=("trickster.ever", STRUCK, SAC_TRICK, DRAWN, WAGERED), forbids=ROMANCE_FORBIDS, any_groups=(COMMITTED_ANY,),
    overrides=ROMANCE_OVERRIDES)

page("areelu.trickster.finale.after", "The bet is still open", [
    nar("end", '''"You reduced a century of work to a pun, and took the Abyss out of me. How thorough."
{n}She did not thank the Commander. Nobody had expected her to.{/n}
"You lost the bet," {n}said the Commander.{/n} "I lost my notes," {n}said Areelu Vorlesh.{/n} "The bet is still open. I have whatever years are left. That is more than enough to learn how you did it, and I will not share what I find."
{n}She took the rooms across the hall because they were the nearest place from which to observe the Commander, and said so. She paid for them herself, from somewhere, and would not say where.{/n}''',
        paragraphs=(
            p("{n}A kitsune scholar arrived within the week, with calipers and a folio, to measure her. Areelu allowed it "
              "exactly once, and corrected the arithmetic.{/n}", forbids=NENIO_GONE),
            p("{n}A kitsune scholar arrived within the week, with calipers, a folio and a list of questions she had brought "
              "back with her from further off than most scholars travel. Areelu allowed the measuring exactly once, and "
              "corrected the arithmetic.{/n}", requires=(NENIO_BACK,), forbids=("nenio.dissolved",)),
            p("{n}The first inquisitors who came looking for the Architect of the Worldwound found a tired woman with ink on "
              "her hands and no magic about her at all, living under the Commander's roof, and went away again without "
              "her and without believing her. She watched them go from an upstairs window, and wrote down how long it "
              "took them to stop looking back. It was a long time.{/n}"),
            p("{n}She did not sleep the first night. She sat by the window of the Commander's lodging with a borrowed pen and "
              "wrote, from memory, the first page of the report she had been writing all her life, the one the "
              "Commander's joke had burned. Then she tore it up.{/n} \"Wrong,\" {n}she said.{/n} \"All of it. I shall have to "
              "start again. You have given me a great deal of work.\""),
            p("{n}The late terms had promised the Commander nothing of hers if she burned. She held the Commander to them "
              "with great precision for the rest of her life: the Commander was never once allowed to keep a page she had "
              "written, and every note she left on the Commander's pillow was taken back by breakfast.{/n}", requires=(LATE,)),
            p("{n}Among the few things she kept was the entry she had dictated in Alushinyrra, which she had never written "
              "down and did not need to:{/n} \"Further observation required.\" {n}She wrote it on the first page of the new "
              "notebook, and underlined it twice.{/n}", requires=(NOTICED,)),
        ))],
    requires=("trickster.ever", STRUCK, SAC_TRICK, DRAWN), forbids=ROMANCE_FORBIDS, any_groups=(COMMITTED_ANY,),
    after="scene:areelu.trickster.finale.rewrite", overrides=ROMANCE_OVERRIDES)

# The failure path: the wager was struck, but what she staked was never named, so there is nothing for the rewrite to
# collect in place of her life. Her canon fate stands (on every other path it always does).
page("areelu.trickster.finale.unnamed", "Uncollected", [
    nar("end", '''{n}The wager was left unsettled at Threshold. The Commander had chosen an ending in which she did not return.{/n}''',
        paragraphs=(
            p('''{n}The wager had called the stake "what is left of her." Neither party had named her work as a substitute before the final choice.{/n}''', forbids=(NAMED,)),
            p('''{n}Her work had been named as the stake. Her graft had not been collected. The final choice came with no substitute prepared.{/n}''', requires=(NAMED,), forbids=(DRAWN,)),
            p('''{n}The Commander had drawn her graft into the cauldron, then chosen a fate that the stored essence did not spare her.{/n}''', requires=(DRAWN,)),
            p("{n}She fell in the fight, before the wager could be settled, as she had always said one of them would.{/n}",
              requires=(FIGHT,), forbids=(SAC_TRICK, INCINERATED, SAC_WOUND, SAC_BEFORE)),
            p("{n}She burned at the Commander's word, in the end, as the hunters had always wanted. The wager said that "
              "whoever burned would pay. It did not say who would light the fire, and the Commander had chosen to.{/n}",
              requires=(INCINERATED,)),
            p('''{n}She went into the Wound to close it, and it closed. No stored essence was substituted for her in that ending.{/n}''',
              any_groups=((SAC_WOUND, SAC_BEFORE),)),
            p("{n}Among what was found in her cell under Threshold was a notebook with a single page written in it, dated "
              "the night of the wager:{/n} \"Stake not yet collected. One of us will regret it.\" {n}It did not say which.{/n}"),
        ))],
    requires=("trickster.ever", STRUCK, DIED), forbids=(SURVIVES, *ROMANCE_FORBIDS), any_groups=(COMMITTED_ANY,),
    after="scene:areelu.trickster.finale.after", overrides=ROMANCE_OVERRIDES)

page("areelu.trickster.finale.survived", "Neither", [
    nar("end", '''{n}Neither of them burned, which was the bet the Commander had made: "My money's on neither."{/n}''',
        paragraphs=(
            p("{n}Areelu Vorlesh paid what she owed on the bet in person. She burned her own notes in front of the Commander, "
              "page by page, without comment, for a whole night. What was left of her she kept, as the raised terms "
              "allowed, to spend on learning how the Commander had done it: the Abyss still in her veins, and the wound "
              "still glowing above her heart.{/n}", forbids=(DRAWN,)),
            p("{n}The Abyss had gone into the Council's crystal before the final choice, and it did not come back to her. "
              "What walked out of Threshold was a Sarkorian woman with grey coming into her hair, no magic in her at all, "
              "and the wound above her heart gone dull as an old burn. She paid what she still owed on the bet in person: "
              "she burned her own notes in front of the Commander, page by page, without comment, for a whole night. The "
              "rest of her she kept, as the raised terms allowed, to spend on learning how the Commander had done it.{/n}",
              requires=(DRAWN,)),
            p("{n}A week later she came to the Commander's door with a proposal, set out as she would have put it to a patron "
              "funding a study: rooms across the hall, unrestricted access to the subject, and the right to leave without "
              "notice. The Commander set one condition of their own, that she knock. She took an hour to consider it, and "
              "accepted, and moved in that evening with a fresh notebook.{/n}"),
            p("{n}She objected, on principle, to the fact that the winner was now partly Shyka the Many, and required every "
              "observation to be initialled twice: once for each of them.{/n}", requires=("ending.trickster_allplanes_fw",),
              forbids=("lastcall.h1",)),
            p("{n}She had been told that the winner would come back partly Shyka the Many, and had prepared a second column "
              "for the initials. The Commander came back one person, badly behaved, with Shyka's share of the bargain "
              "left in a bottle. She struck out the second column without comment, and kept the page.{/n}",
              requires=("ending.trickster_allplanes_fw", "lastcall.h1")),
            p("{n}Nenio offered to buy the ashes for her encyclopaedia. Areelu sold them to her at a price that made the "
              "kitsune's ears go flat.{/n}", forbids=NENIO_GONE),
            p("{n}Nenio, who had come back from further off than most scholars travel, offered to buy the ashes for her "
              "encyclopaedia. Areelu sold them to her at a price that made the kitsune's ears go flat.{/n}", requires=(NENIO_BACK,), forbids=("nenio.dissolved",)),
            p("{n}She kept every appointment she made. The first was at the Commander's door, the morning after Threshold, "
              "with her hand held out: the real one.{/n}", requires=(REAL_HAND,)),
            p("{n}Some of the pages she burned the Commander recognised. The notes from Kenabres. The observations from "
              "Drezen, in Yaniel's borrowed hand. A thick bundle tied with black ribbon, labelled only with the "
              "Commander's name and a date from before the Commander was born. She burned that one last, and slowest, "
              "and watched it until the ribbon was ash.{/n}"),
            p('''{n}The lens she had sent she did not burn. She took it back without asking, polished it on her sleeve, and set it on the windowsill between the two rooms, where it stayed.{/n}''', requires=(LENS_HELD,)),
            p("{n}The Commander, as the report records with some irritation, fell asleep in a chair before she was halfway "
              "through, and she burned the rest by the light of the Commander's snoring.{/n} \"The subject,\" {n}she wrote,{/n} "
              "\"does not know how to watch a thing end. That is either why it won, or how.\""),
        ))],
    requires=("trickster.ever", CHEATED, STRUCK, WAGERED), forbids=(DIED, *ROMANCE_FORBIDS), any_groups=(COMMITTED_ANY,),
    after="scene:areelu.trickster.finale.unnamed", overrides=ROMANCE_OVERRIDES)


# --- The report (after Threshold): her notes on the longitudinal experiment, page by page -------------------------------
#
# Every page reads both survivals: the rewrite (MORTAL: her life's work burned instead of her life; no magic, ageing) and
# the punchline (neither burned: still the half-demon witch, who paid her stake by burning her notes herself).

report("areelu.trickster.report.rooms", "The report: the rooms across the hall", [
    nar("start", '''{n}The report resumed in a fresh notebook. Areelu took the room across the hall and left her door open while she worked. When the Commander passed it, her pen stopped. Neither of them mentioned it.{/n}''',
        c("[Knock.]", "knock_mortal", requires=MORTAL),
        c("[Knock.]", "knock_witch", forbids=MORTAL),
        c("[Walk in without knocking.]", "walk_mortal", requires=MORTAL),
        c("[Walk in without knocking.]", "walk_witch", forbids=MORTAL),
        c("[Slide a note under her door instead.]", "note"),
        paragraphs=(
            p("{n}She had no magic left to ward her door with, and did not pretend otherwise. Every night she wedged a chair "
              "under the handle. Every morning she moved it back before the Commander could see, and every morning the "
              "Commander saw.{/n}", requires=MORTAL),
            p("{n}She did not rely on the chair. Within the week she had three false names registered in three cities, a "
              "forger in Nerosyan who owed her a favour from before the crusade, and a standing arrangement with a "
              "chandler to warn her of anyone asking after a grey-haired Sarkorian woman. None of it was the Commander's "
              "doing, and she made sure the Commander knew that.{/n}", requires=MORTAL),
            p("{n}She warded her door with three sigils that the Commander could not read, and one that the Commander could. "
              "It said, in plain Common: Knock.{/n}", forbids=MORTAL),
        )),
    nar("knock_mortal", '''{n}"Enter." She clears a place beside the lamp. A silver probe and a sand-glass lie among the papers.{/n} "Sit down. I want to look at the wound." {n}She takes the Commander's wrist and does not release it when the sand runs out.{/n}''',
        c("Continue", "hands")),
    nar("knock_witch", '''{n}The sigils flared at the first knock and went out at the second. "Enter," she said, and the door opened by itself, which she clearly thought was funnier than the Commander did.{/n}
{n}She did not need instruments. She laid two fingers against the Commander's wrist and one against the old wound from Kenabres, closed her eyes, and listened, the way she had once listened to the Worldwound. "Your blood is louder than it should be," she said. "Your soul is quieter. Sit down. This will take all night."{/n}''',
        c("Continue", "hands")),
    nar("walk_mortal", '''{n}She stands at the window with a vial held to the light. Inside is a drop of the Commander's blood.{/n} "Taken while you slept. You had been moving all evening." {n}She sets it among her papers and finally turns.{/n} "If you intend to break something, leave the vial alone. I have not finished with it."''',
        c("Continue", "hands")),
    nar("walk_witch", '''{n}The sigils hissed like a kettle as the Commander stepped through them, and did nothing else. She had keyed them, it turned out, to everyone in Golarion but one.{/n}
{n}"You did not knock," said Areelu, from the far side of a table covered in the Commander's own hair, nail parings and old bandages, labelled and pinned. "Good. I wanted to see whether you would. It is in the file now. Everything you do is in the file. Do not touch that; it is a cast of your left thumb."{/n}''',
        c("Continue", "hands")),
    nar("note", '''{n}The note said: Knock knock.{/n}
{n}The answer came back under the Commander's own door the next morning, in a hand as small and even as a row of stitches: "Who is there. (Do not answer. I have already written it down. I have written down everything you will say for the next week, and I will be interested to see how much of it you manage to say differently.)"{/n}
{n}By the end of the week the Commander had said four things she had not predicted. She wrote them on a separate sheet and pinned it above her desk, like a list of charges.{/n}''',
        c("Continue", "hands")),
    nar("hands", '''{n}She sketches the Commander's hand beside a diagram of the cauldron. When the Commander makes a coin vanish over the open page, she catches the wrist before the second flourish.{/n} "Again. Slowly. I would like to see what my notes missed."''',
        c("[Make the coin disappear.]", "coin"),
        c("[Take the pen out of her hand.]", "pen"),
        c('"And where does it happen in you?"', "hers"),
        c("[Make her laugh.]", "laugh")),
    nar("laugh", '''{n}The Commander tried. A joke about the Worldwound, which she corrected. A joke about Deskari, which she improved. Then, out of nowhere, a very old joke from the border taverns about a paladin, a demon and a goat, in which the goat wins because nobody thought to ask it anything.{/n}
{n}She did not laugh. She put her pen down. "The goat," she said, "is the clans. Nobody asked them either. Your paladin and your demon argued over their valleys for a hundred years, and at the end of the joke the goat is still standing there, and everyone laughs because it has no idea what just happened. It had every idea. I was there." She picked the pen up again. "Tell it at a dinner in Mendev. I will watch their faces, not yours, and I will write down who laughs first."{/n}''',
        c("Continue", "end")),
    nar("coin", '''{n}The Commander makes the coin vanish again. Areelu follows the empty hand, then catches it and opens the fingers herself.{/n} "Nothing. Very well. Again." {n}After the twentieth attempt she pushes the notebook aside and watches with both elbows on the table.{/n}''',
        c("Continue", "end")),
    nar("pen", '''{n}The Commander takes her pen. She keeps hold of the wrist that took it.{/n} "Give it back." {n}Her thumb presses against the pulse.{/n} "Or keep it and stay. I have not finished with either of you."''',
        c("Continue", "end")),
    nar("hers", '''{n}"I thought I knew what you would do. I had built enough of you to be certain." She turns the pen between her fingers.{/n} "Then you brought me a wager I did not know how to win. I would like to make fewer mistakes about you. Sit still."''',
        c("Continue", "end")),
    nar("end", '''{n}By the end of the month, the chair beside her desk had acquired the Commander's cloak. She complained when it covered her papers. She did not move it to the other room.{/n}'''),
], after="scene:areelu.trickster.finale.survived")

report("areelu.trickster.report.hunters", "The report: the hunters", [
    nar("start", '''{n}In the second season, the hunters came.{/n}''',
        c("[Joke] \"Leave this to me. I have a scarecrow and a spare robe.\"", "scarecrow"),
        c("[Let her answer them herself.]", "herself_mortal", requires=MORTAL),
        c("[Let her answer them herself.]", "herself_witch", forbids=MORTAL),
        c("[Stand in the doorway beside her.]", "doorway_mortal", requires=MORTAL),
        c("[Stand in the doorway beside her.]", "doorway_witch", forbids=MORTAL),
        c("[Hide her in the cellar.]", "cellar"),
        paragraphs=(
            p("{n}They came from Mendev with a writ and a fire-blessed brand, looking for the Architect of the Worldwound. "
              "What they found at the Commander's door was a greying woman with ink on her hands and papers in another "
              "woman's name. They did not like the papers. The eldest of them did not like her face, either; he had seen "
              "it once, painted, in a chapterhouse in Mendev, forty years younger and a great deal crueller.{/n}",
              requires=MORTAL),
            p("{n}They came from Mendev with a writ and a fire-blessed brand, and they knew exactly whom they were looking "
              "for. The Architect of the Worldwound had been seen alive after Threshold, and there were men in Mendev who "
              "had waited all their lives for the chance.{/n}", forbids=MORTAL),
            p("{n}Areelu watched them from the window, and, alone of all the days the Commander had known her, she did "
              "not write anything down. The last time witch-hunters had come to her door, she had been at her desk, "
              "recording her observations, and her child had been outside.{/n}"),
        )),
    nar("scarecrow", '''{n}Three days later the hunters reach a burnt farmhouse on the Sarkorian border. A straw witch in a scorched robe waits inside, with a note pinned to its chest in the Commander's hand.{/n} "Neither," {n}the captain reads. The doll is burned, the note copied, and a rider sent back toward the Commander's house. The detour has bought three days. The captain can now put the Commander's name beside hers.{/n}''',
        c("Continue", "scarecrow_after")),
    nar("scarecrow_after", '''{n}The broadsheet prints the captain's account and the note beneath it. Areelu reads both.{/n} "He knows it was straw. He knows who sent him after it. Your joke has cost us the front door." {n}She folds the paper inside her notebook.{/n} "Three days. I can use those."''',
        c('"Do you want to know what the note said?"', "note_said"),
        c("Continue", "end")),
    nar("note_said", '''{n}"Neither. I read it." She taps the printed note.{/n} "Next time disguise the hand as well as the witch. I would prefer he spend longer finding us."''',
        c("Continue", "end")),
    nar("herself_mortal", '''{n}She went down to them herself, in a plain grey dress, with her papers in her hand: a widow of Nerosyan, registered, stamped, three years old. The inquisitor read them twice and handed them back. "Good papers," he said. "I have seen a great many good papers."{/n}
{n}"I knew the woman you want," Areelu told him. "She was cleverer than you, and crueller, and she did everything you say she did, and more. What is left of her lives under the Commander's roof, and the Commander's seal is on this door." He looked past her at the seal, and at the Commander on the stairs, and did the arithmetic every inquisitor in Mendev had learned since the war: what it would cost the Order to break down the door of the one person the Queen could not afford to anger. He wrote her false name in his book, and her description beside it, and went. "I will come back," he said at the gate. "When the Commander is dead, or out of favour. One of those always happens."{/n}''',
        c("Continue", "herself_mortal_after")),
    nar("herself_mortal_after", '''{n}She came back upstairs with her face very still.{/n}
{n}"He did not believe a word of it," she said. "Good. A man who believes me is a fool, and fools come back with more fools. That one will come back alone, and slowly, and he will be patient." Her hands were shaking. She looked at them with the same detached interest she gave everything else, and wrote down how long it took them to stop. Then she wrote down his name.{/n}''',
        c("Continue", "end")),
    nar("herself_witch", '''{n}She went down to them herself, and the lamps in the street went out one by one as she passed.{/n}
{n}"You want the Architect," said Areelu Vorlesh. "Here she is. I have not changed my mind about anything, and I have not forgotten your order. Your grandfathers came to my house once. Go home, and tell your children that you saw me, and that I let you go."{/n}
{n}She did let them go. All but the one who drew his brand; him she left in the street for his brothers to carry home, and nobody in Mendev ever learned what she had done to his eyes.{/n}''',
        c("Continue", "herself_witch_after")),
    nar("herself_witch_after", '''{n}She returns upstairs without a mark on her.{/n} "Do not call it mercy. The others will describe what happened to the one who drew his brand. I need them frightened enough to be believed." {n}She adds his name to her list.{/n}''',
        c("Continue", "end")),
    nar("doorway_mortal", '''{n}The Commander stood in the doorway beside her, with nothing in either hand, and let the inquisitors look.{/n}
{n}"You will want to arrest the Commander of the crusade as well, I suppose," said Areelu, pleasantly, from behind the Commander's shoulder. "Do. I should like to watch you try." They did not try. They looked from the Commander to the grey-haired woman with ink on her hands and understood exactly what they were looking at, and understood as well what it would cost the Order to drag her out of the Commander's own house in front of the whole street. They went. Their captain left a man in the tavern opposite, and the man was still there at midwinter.{/n}''',
        c("Continue", "doorway_after")),
    nar("doorway_witch", '''{n}The Commander stood in the doorway beside her, with nothing in either hand, and let the inquisitors look.{/n}
{n}"You will want to arrest the Commander of the crusade as well, I suppose," said Areelu, pleasantly. "Do. I should like to watch you try." They did not try. The Commander had walked out of Threshold alive, which in Mendev was reckoned the more frightening of the two, and the witch at the Commander's side was smiling in a way that made the fire-blessed brand go out in its holder.{/n}''',
        c("Continue", "doorway_after")),
    nar("cellar", '''{n}She let herself be hidden. That was the part the Commander never forgot afterwards: the Architect of the Worldwound going down the cellar steps without a word, with her notebook under her arm, and sitting among the apple barrels in the dark while the hunters searched the house above her.{/n}
{n}They did not find her. When the Commander went down to tell her so, she was writing by the light of a single candle, and did not look up.{/n}''',
        c("Continue", "cellar_after")),
    nar("cellar_after", '''{n}"The last time they came," she said, "I did not hide. I did not know to. I was at my desk, and I did not hear them until it was over."{/n}
{n}She closed the notebook. "This time I heard every step. I counted them. Forty-one, in the room above, and three on the cellar door, and then they went away." She stood up, and brushed the dust from her skirt. "Do not do that again. I do not like knowing how it would have felt."{/n}''',
        c("Continue", "end")),
    nar("doorway_after", '''{n}When they had gone, she stayed in the doorway a while longer, looking at the empty street.{/n}
{n}"The last time they came to my house," she said, "nobody stood in the door." She did not say anything else. That night the entry in her notebook was one line long, and the Commander was not allowed to read it.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}The hunters kept her name. Some returned with better writs; others hired men who would enter a cellar before announcing themselves. She kept their names too, and what each visit had cost. No visit went unrecorded.{/n}'''),
], after="scene:areelu.trickster.report.rooms")

report("areelu.trickster.report.grey", "The report: the grey", [
    nar("start", '''{n}In the second winter she fell ill.{/n}
{n}It was nothing: a cough, a fever, the kind of thing that goes through a city every winter and kills the old and the unlucky. The woman who had opened the Worldwound had not been ill in a hundred years. She lay in bed with her notebook on her chest and recorded her own temperature every hour, in a hand that got smaller and smaller, until she could not hold the pen.{/n}''',
        c("[Sit with her through the night.]", "sit"),
        c("[Fetch a healer.]", "healer"),
        c('[Joke] "The Architect of the Worldwound, laid low by a cold. Nobody\'s going to believe this."', "cold"),
        c('"You could let it take you. You always said you wanted to beat death, not dodge it."', "dare")),
    nar("dare", '''{n}She opened her eyes, and for a moment they were the eyes the Commander remembered from Threshold, entirely without mercy.{/n}
{n}"Let it take me," she repeated. "In a bed, of a cough, a hundred years late, because you made a pun." She laughed, and it turned into coughing. "No. If death wants me it will have to earn me properly. I will not give it the satisfaction of a cold." She lived, the Commander was sure afterwards, mostly out of spite.{/n}''',
        c("Continue", "after")),
    nar("sit", '''{n}The Commander sat with her. Near midnight she woke, and saw who it was, and did not tell the Commander to go.{/n}
{n}"This is what you did," she said. Her voice was a thread. "Death. Weakness. Separation. I made war on all three for a century, and you handed me back to them with a joke. I want you to understand that I know exactly what you did."{/n}
{n}"I know." "Good." She closed her eyes. "Then stay. It is only fair that you watch."{/n}''',
        c("Continue", "after")),
    nar("healer", '''{n}The healer the Commander found was a priest of the Lady of Graves, because that was who was awake at that hour.{/n}
{n}Areelu opened her eyes, saw the grey robe and the spiral at his throat, and laughed so hard she started coughing and could not stop. "Take him away," she managed, at last. "Pay him. Pay him double. But if he touches me I will live another thirty years out of spite, and he can explain that to his goddess."{/n}
{n}The priest, to his credit, did not leave at once. He looked at her a while, and then at the Commander, and said only: "She will live. The Lady has told me nothing about this house, and I have learned not to ask." He took his double fee and went, and she laughed about him for a week.{/n}''',
        c("Continue", "after")),
    nar("cold", '''{n}"Nobody will," she agreed, from behind a wall of blankets. "That is the most dangerous kind of truth. Write it down for me. My hand is shaking."{/n}
{n}The Commander wrote it down. She dictated the rest of the night's entry through chattering teeth, correcting the Commander's spelling, and once, near dawn, laughed at something the Commander had written that was not meant to be funny, and would not say what.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}The fever breaks on the third day. At the mirror she parts the grey at her temple and finds white beneath it. She pulls one hair free and holds it against the lamp.{/n} "More of it. So this is what the years do when the Abyss no longer answers." {n}She pins the hair into the notebook. For the rest of the winter her hand shakes in the evenings, and the Commander writes while she dictates.{/n} "Do not apologise. Write."'''),
], after="scene:areelu.trickster.report.hunters", any_group=(DRAWN,))

report("areelu.trickster.report.graft", "The report: the other half", [
    nar("start", '''{n}In the second winter the Commander woke one night and found her gone.{/n}
{n}She had not paid the Abyss back when she paid her stake. It was still in her, the half of her she had sewn to her own soul at the edge of the Wound a century ago, and it was hungry the way the Abyss is always hungry. Some nights she did not sleep. Some nights she went out.{/n}''',
        c("[Follow her.]", "follow"),
        c("[Wait up for her.]", "wait"),
        c("[Go back to sleep. She will come back.]", "sleep")),
    nar("follow", '''{n}The Commander found her at the edge of the city, where the old walls gave out onto open ground, standing perfectly still with her face turned toward the north, toward the Wound. The wound above her heart was burning violet in the dark.{/n}
{n}"Go home," she said, without turning. "This is not a thing you need to see." And then, when the Commander did not go: "It calls. It has always called. I am standing here so that I can hear it and not answer. That is all I do, on these nights. I stand and I do not answer."{/n}''',
        c("[Stand beside her, and do not answer either.]", "stand"),
        c('"I have one too. You put it there."', "mine"),
        c('"What does it say, when it calls?"', "says")),
    nar("says", '''{n}"That I was right." Her eyes stayed on the north. "That everything I did was correct, and there is more to do, and I am wasting the Abyss in me on a kitchen and a notebook and a Commander who makes jokes."{/n}
{n}"It is not wrong," she said. "That is what makes it difficult. It has never once lied to me. It simply does not understand why I have stopped listening, and neither, some nights, do I."{/n}''',
        c("[Stand beside her, and do not answer either.]", "stand")),
    nar("stand", '''{n}The Commander stood beside her until the sky went grey. Neither of them said anything. Once, near dawn, something under the Commander's breastbone stirred in answer to the north: the soul the Commander shared with her child, and the gift she had knitted round it, which still knew the voice they had been made beside. She noticed, and her hand closed very briefly around the Commander's wrist, hard enough to bruise.{/n}
{n}"There," she said. "Now you know what I stand out here with. It is not a comfort. It is a fact."{/n}''',
        c("Continue", "after")),
    nar("mine", '''{n}"Yes." She turned at last, and her crimson eyes were very bright. "I changed myself by sewing my soul to the Abyss, and then I changed you. Those fits of rage in Kenabres were the other half of your soul beginning to wake."{/n}
{n}"So do not look at me as if I were a stranger standing in the dark. I am your maker in this, Commander, and in nothing else, and it is the one thing between us I will not deny. Come here. Listen. And do not answer."{/n}''',
        c("Continue", "stand")),
    nar("wait", '''{n}She came back an hour before dawn, with frost in her hair and nothing in her hands. She saw the Commander sitting up in the dark, and stopped in the doorway.{/n}
{n}"You waited," she said. "I did not ask you to." She sat down on the end of the bed and began, methodically, to take the frost out of her hair. "I have not killed anyone. I have not answered it. Write that down. I want it in your hand, not mine."{/n}''',
        c("Continue", "after")),
    nar("sleep", '''{n}The Commander went back to sleep, and she came back, and in the morning there was a new entry in her notebook in a hand that was not quite as steady as usual.{/n}
{n}"Went out. Did not answer. Subject slept through it, which is either trust or stupidity. Recording both."{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}It happened perhaps twice a year. She never answered. Once, near the end of the report, she wrote: "A hundred years ago I would have gone. The difference is not virtue. The difference is that I now have somewhere to come back to, and I dislike leaving an experiment unattended."{/n}'''),
], after="scene:areelu.trickster.report.grey", any_group=(CHEATED,), forbids=(DRAWN,))

report("areelu.trickster.report.sarkoris", "The report: the clan roll", [
    nar("start", '''{n}In the third year a woman came to the house from the refugee camps on the old Sarkorian border. She carried a roll of birch bark as long as she was tall, wound on a staff, and she asked for the Architect by name.{/n}
{n}It was a clan roll: the names of her people, every family of her grandmother's valley, written in the old way by a god-caller who had not lived to finish it. The Wound had swallowed the valley in its first year. The roll ended in the middle of a name.{/n}''',
        c("[Bring her to Areelu.]", "met"),
        c("[Send her away before Areelu sees her.]", "away")),
    nar("met", '''{n}Areelu looked at the roll for a long time without touching it.{/n}
{n}"I know how many," she said at last. "I counted them when I opened it. I have always known the number. I have never needed the names."{/n}
{n}The woman from the camps said nothing. She had come a long way to say nothing to that particular face, and she did it well.{/n}''',
        c("[Ask Areelu to read the names aloud.]", "names"),
        c("[Ask the woman what she came for.]", "wants"),
        c('[Joke] "Just tell her you\'re sorry. It\'s a very short speech."', "sorry"),
        c("[Let the silence stand.]", "silence")),
    nar("names", '''{n}Areelu read the names aloud. All of them, the whole length of the staff, in a flat, clear voice, without stopping and without apology. It took the whole night.{/n}
{n}When she reached the end, where the god-caller's hand had stopped in the middle of a name, she stopped too. She did not finish it. She did not pretend to know how it ended.{/n}''',
        c("Continue", "names_after")),
    nar("names_after", '''{n}The woman from the camps wound the bark back onto its staff and left without a word. At the door she turned, once, and looked at Areelu the way one looks at weather: something that has happened, and will happen again.{/n}
{n}"She wanted me to weep," Areelu said afterwards. "I read her the names instead. It was the only honest thing I had to give her. Do not look at me as if it were more than that."{/n}''',
        c("Continue", "end")),
    nar("wants", '''{n}"I came for her name," said the woman from the camps. "The roll is of everyone the valley lost. She is the last thing the valley lost. She was one of us, before."{/n}
{n}Areelu went white, and then very still. She drew the roll closer.{/n}''',
        c("Continue", "wants_after")),
    nar("wants_after", '''{n}She took the roll. She wrote at the bottom of it, under the god-caller's unfinished name, in the old Sarkorian letters the woman recognised: "Areelu Vorlesh, of Sarkoris. Lost in the first year, by her own hand."{/n}
{n}"Now go," she said, and the woman went. Afterwards Areelu sat at the kitchen table until the candle burned out, and when the Commander came in she said only: "It was correct. I checked it twice."{/n}''',
        c("Continue", "end")),
    nar("sorry", '''{n}"No." Areelu did not even glance at the Commander. "Do not joke about the clans. It is the one subject on which I will not be your audience."{/n}
{n}She turned back to the woman from the camps. "I am not sorry. I would do it again, and I would do it better. You may write that at the bottom of your roll, if there is room. There is not much room."{/n}
{n}The woman wrote it. It fitted.{/n}''',
        c("Continue", "end")),
    nar("silence", '''{n}The Commander said nothing, and so neither did anyone else. The three of them sat in the kitchen with the roll across the table until the candle burned down.{/n}
{n}When the woman from the camps stood to go, Areelu spoke without looking up. "The last name. The one the god-caller did not finish. Do you know how it ends?" The woman did. She told her. Areelu wrote it down, and never read it aloud, and never crossed it out.{/n}''',
        c("Continue", "end")),
    nar("away", '''{n}The Commander met the woman at the gate and sent her back to the camps with money and a lie.{/n}
{n}Areelu had watched it all from the window. "You protected me from a list," she said. "How sentimental. I opened the Wound, Commander. I do not need to be shielded from its paperwork." For a week afterwards she spoke to the Commander only in measurements.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}After that visit, the wound entries in her notebook were in Sarkorian. When the Commander asked for a copy in Common, she covered the page with her hand.{/n} "No. These are mine. If a Mendevian clerk wants my account, let the clerk learn to read it." {n}She returned to work.{/n}'''),
], after="scene:areelu.trickster.report.graft")

report("areelu.trickster.report.participation", "The report: participation", [
    nar("start", '''{n}In the fourth winter, she comes to the Commander's door with her hair loose and the notebook tucked under one arm. She shuts it before she knocks.{/n}''',
        c("[Let her in.]", "in_mortal", requires=MORTAL),
        c("[Let her in.]", "in_witch", forbids=MORTAL),
        c("[Take the notebook out from under her arm.]", "notebook"),
        c('"Is that what you want? Not what you\'re measuring. What you want."', "want"),
        c("[Close the door gently between you.]", "closed"),
        paragraphs=(
            p('''{n}She was mortal now, and cold at night in a way she had forgotten a body could be. She said so, as a fact, standing in the Commander's doorway with her notebook under her arm and her hair loose over her shoulders.{/n}''', requires=MORTAL),
            p('''{n}The wound above her heart glowed faintly in the dark, as it had at Threshold. She stood in the Commander's doorway with her notebook under her arm and her hair loose over her shoulders, and the light of the wound showed exactly how little else she was wearing.{/n}''', forbids=MORTAL),
            p('''"Well?" {n}said Areelu Vorlesh.{/n} "Open the door, Commander. I did not come to take your pulse."'''),
        )),
    nar("in_mortal", '''{n}She unbuttons your shirt and pushes it off your shoulders. Her fingers are cold; her mouth is warm. At the wound from Kenabres she pauses, presses her lips beside it, then looks up at you without moving away.{/n} "Still mine." {n}Her hand closes on your bare back and pulls you against her.{/n}''',
        c("Continue", "in_mortal_2")),
    nar("in_mortal_2", '''{n}She lets the grey dress fall. In the lamplight you can see the marks the graft left, the lines at her mouth, the heat rising along her throat.{/n} "Look. I want you to see what is left." {n}She kisses you before you can answer, drives you back onto the bed and climbs over you, her loose hair brushing your face. The notebook falls open on the floor. Her hands leave your chest to draw you closer.{/n}''',
        c("Continue", "morning")),
    nar("in_witch", '''{n}Her hand closes over yours and brings it to the fastening of her robe. She watches you undo it. Beneath the cloth, the wound above her heart burns violet.{/n} "You wanted close enough to study. Come here." {n}Her mouth meets yours, hungry and hard; the hand at your back is hot enough to make you gasp.{/n}''',
        c("Continue", "in_witch_2")),
    nar("in_witch_2", '''{n}She pulls off your shirt and lets her robe slip after it. The violet light spills over both of you. At the bed she rolls you beneath her and catches your wrists against the pillow. Her hair falls around your faces, hiding the room.{/n} "Look at me, Commander." {n}You do. Her grip tightens; then one hand releases yours and draws you into the dark beneath her.{/n}''',
        c("Continue", "morning")),
    nar("want", '''{n}"Yes." She sets the closed notebook on the floor.{/n} "I want you. Do you require a cleaner answer than that? I will not give you one. I have not stopped wanting what brought us to Threshold." {n}She stays in the doorway, watching you.{/n} "Tonight I came for this."''',
        c("[Let her in.]", "in_mortal", requires=MORTAL),
        c("[Let her in.]", "in_witch", forbids=MORTAL),
        c("[Close the door gently between you.]", "closed")),
    nar("notebook", '''{n}She holds the notebook out. You take it and set it on the floor. Two fingers settle against your throat, and her thumb tilts your chin toward her.{/n} "There. The pulse I kept beating in the caves. It has become inconveniently easy to miss." {n}She kisses you, follows when you step back to the bed, and straddles your lap. Her dress loosens under your hands.{/n} "Keep looking at me." {n}She takes your face between her palms and pulls you down with her.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}At dawn she sits beside you, barefoot, writing on her knee. When you stir, she closes the notebook against your reaching hand.{/n} "No. This page is mine." {n}She lays it aside and returns her palm to the wound she kissed in the night.{/n} "You may stay awake while I look. I find I prefer it."''',
        c("Continue", "morning_after"),
        c("[Read the entry aloud.]", "aloud"),
        paragraphs=(
            p('''{n}At breakfast Nenio looks from Areelu's loose hair to the two cups at the Commander's place and opens her folio. "A new observation—" Areelu lays a hand over the page. "An unpublished one." Nenio waits until the hand moves before writing anything.{/n}''',
              forbids=NENIO_GONE),
            p('''{n}At breakfast Nenio looks from Areelu's loose hair to the two cups at the Commander's place and opens her folio. "A new observation—" Areelu lays a hand over the page. "An unpublished one." Nenio waits until the hand moves before writing anything.{/n}''',
              requires=(NENIO_BACK,), forbids=("nenio.dissolved",)),
        )),
    nar("aloud", '''{n}The Commander reaches for the notebook again. Areelu catches it first and closes it.{/n} "You have heard what I want. That does not give you my notes." {n}She puts it in the locked drawer and pockets the key. When she turns back, she is smiling.{/n} "You will have to remember the night without my assistance."''',
        c("Continue", "morning_after")),
    nar("morning_after", '''{n}That afternoon she went back across the hall and moved her own desk under the one window of her room that faced the street, where she could see who came to the Commander's door before the Commander did, with its back to the wall.{/n}
{n}"Your name on this door does what no ward of mine can: it makes the hunters ask permission," she said, when the Commander found it there. Then, because it was not the whole of it, and she had never in her life been able to leave a sum unfinished: "And nobody comes to your door that I have not seen first. The last time hunters came to a door of mine, I was at my desk with my back to the window." She looked at the desk as if it had spoken out of turn. "Strike that. It is a sound position." Her travelling case stayed packed beside it, and she did not hide that either.{/n}''',
        c('"Stay, then. On your terms."', "stay"),
        c('"Under my roof, the case goes in the cupboard."', "rules"),
        c('"Keep your door open, then. I will keep mine."', "door"),
        c('"Move your desk into my rooms. Share them."', "propose")),
    nar("propose", '''{n}She did not answer at once. She took out her notebook and wrote the proposal down, word for word, and read it back to herself.{/n}
{n}"Conditions," she said. "The desk goes under your window, not mine, and nobody moves it. The notebook is never read, asleep or awake. I choose the nights. And the case stays packed, in plain sight, for the day I leave. Agree to all four, or none."{/n}''',
        c('"All four."', "shared"),
        c('"Not the nights. Those are both of ours."', "refused")),
    nar("shared", '''{n}She moves the desk that evening and sets the packed case beside it.{/n} "I want the bed. The notebook stays on my side of it." {n}She hangs the four agreed conditions above the desk.{/n}
{n}Some weeks later the Commander came in near dawn and found her asleep at that desk, the pen still in her hand, turned in her chair toward the bed rather than the door. The entry in front of her stopped in the middle of a word. She never finished it, and she never tore the page out; and when the Commander asked, she said she had been observing, and did not say what.{/n}''',
        c("Continue", "letters")),
    nar("refused", '''{n}"Then no." She closed the notebook without heat.{/n}
{n}"I did not survive a century by sharing the choice of when I am vulnerable, Commander. I will not start because you asked nicely. Ask me again when you have a better counter-offer; I will still be across the hall." She was, most nights. It did not end anything. It only meant that every night began with a knock, and that she was the one who decided to answer it.{/n}''',
        c("Continue", "letters")),
    nar("stay", '''{n}"On my terms." She read the sentence back to herself, as if checking it for a clause she had missed. "Very well. Two conditions. I leave the day you bore me, and I take my notes when I go." The case stayed packed. It was the first thing she looked at every morning.{/n}''',
        c("Continue", "letters")),
    nar("rules", '''{n}"Your roof," she repeated, and unpacked the case, slowly, item by item, onto her own bed: a knife, a vial of something that smoked, three forged letters of passage to three different countries, and a change of clothes. "There," she said. "Now you know what I keep ready. It changes nothing. I will still go when I choose." The case went into the cupboard. The letters of passage did not.{/n}''',
        c("Continue", "letters")),
    nar("door", '''{n}"Very well." She wedged her own door open with the desk that same evening, so that she could see the Commander's across the hall.{/n}
{n}"You wanted a door," she said. "You have one. It is open. The choice of who walks through it is not only yours." Most nights, it was her.{/n}''',
        c("Continue", "letters")),
    nar("letters", '''{n}Within the month she had read every letter in the Commander's desk, and put each one back exactly as it had been, and said so at breakfast, to the Commander's face.{/n}
{n}"I do not share well. I never have; ask the Wound." She set down her cup. "So these are my conditions, and they are mine, not a treaty. I will not be lied to about where you sleep. Nothing and nobody comes into the room with my notes. And whatever you want of me, you ask for in words, not by leaving a door open and waiting to see what I do."{/n}
{n}"I will read no more of your letters. I have learned what I needed." She moves the cup away from the papers.{/n} "Tell me where you sleep. I would prefer to hear the answer from you."'''),
    nar("closed", '''{n}The Commander closed the door gently between them.{/n}
{n}Through the wood, after a while, came a dry sound that might have been a laugh. "Subject declined," said Areelu Vorlesh. "Noted." Her footsteps went back across the hall.{/n}
{n}She did not knock again that winter, and she did not seem, in the mornings, to hold it against anyone. She only wrote more.{/n}
{n}In spring she knocks once and leaves a page of wound observations beneath the door. She waits for the Commander to speak of that winter first.{/n}'''),
], after="scene:areelu.trickster.report.sarkoris")

report("areelu.trickster.report.wound", "The report: the wound", [
    nar("start", '''{n}In the fifth year the wound from Kenabres opened again, as the old wound of an unclosed Worldwound will. It opened in the night, without warning, and the Commander woke in a bed full of blood.{/n}''',
        c("[Let her work.]", "work"),
        c('"This is what you bet for. Take it, if you want it."', "take"),
        c('[Joke] "Is this the part where you tell me to be brave?"', "brave"),
        paragraphs=(
            p("{n}She had no magic left to hold it shut with. She had a century of method, which the cauldron had not been "
              "able to take, because it had never been written anywhere. It was in her hands.{/n}", requires=MORTAL),
            p("{n}She held it shut the first night with a word in a language the Commander had never heard. It cost her "
              "something; the Commander could see it in her face the next morning, and she would not say what.{/n}",
              forbids=MORTAL),
            p('"I keep the wound," {n}said Areelu Vorlesh, rolling up her sleeves.{/n} "Those were the terms. For study. I did '
              'not say I would let it keep you."'),
            p("{n}It had been her price at Threshold, and the Commander had paid it without haggling. She had never once let "
              "the Commander forget it.{/n}", requires=(WOUND_CEDED,)),
        )),
    nar("take", '''{n}She looked at the Commander with pure contempt.{/n}
{n}"You think I bet on your wound so that I could cut it out of you in your sickbed, like a thief? I bet on it so that nobody else would have it. Not the Lady of Graves, not the Abyss, not you. Lie down."{/n}''',
        c("Continue", "work")),
    nar("brave", '''{n}"No. Breathe when I tell you." She presses her palm down until the bleeding slows.{/n} "And keep your hand away. I cannot stitch around both of us."''',
        c("Continue", "work")),
    nar("work", '''{n}She worked through the night, and she talked while she worked, the way some people hum: about the Worldwound, of which this was a reflection; about the night she opened it; about what she had got wrong.{/n}
{n}"My mistake," she said, somewhere near dawn, to the wound rather than the Commander. "My failure. I have been looking at the large one for a hundred years. I should have been looking at this one."{/n}''',
        c("Continue", "work_mortal", requires=MORTAL),
        c("Continue", "work_witch", forbids=MORTAL),
        c('"Tell me about the night you opened it."', "night")),
    nar("night", '''{n}She was quiet for so long that the Commander thought she would not answer.{/n}
{n}"It was cold," she said at last, stitching. "That is what nobody writes. They write about the light and the screaming, and there was light, and there was screaming, later. But at the moment it opened it was only very cold, and very quiet, and I thought: there. Now nothing will ever be the same, and nobody will ever again be able to tell me that it has to be." She tied off the thread. "I was right. I have never regretted being right."{/n}''',
        c("Continue", "work_mortal", requires=MORTAL),
        c("Continue", "work_witch", forbids=MORTAL)),
    nar("work_mortal", '''{n}By morning it had closed. Not healed: held, with silk and salt and a paste she would not name, and a patience the Commander had not known she had.{/n}
{n}Her hands, when she finally took them away, were shaking with the plain exhaustion of a woman who had been awake for a day and a night. She looked at them with interest. "That," she said, "is what it costs without the Abyss. I had forgotten. It is very instructive."{/n}''',
        c('"Why are you really doing this?"', "why"),
        c('"How long can you keep doing this?"', "how_long"),
        c("[Sleep.]", "end")),
    nar("how_long", '''{n}"Until my hands fail." She holds them up, stained with blood and beginning to spot with age.{/n} "The Wound will not wait for that. Someone else must be able to hold it shut." {n}She draws the notebook toward her.{/n} "Every stitch, every paste, every hour. I will write the method while I can still demonstrate it. Do not lose these pages."''',
        c("[Sleep.]", "end")),
    nar("work_witch", '''{n}By morning it had closed. Not healed: held, with a working that made the lamps burn violet and the Commander's teeth ache, and something of hers laid into it that the Commander could feel afterwards, like a cold coin under the skin.{/n}
{n}"Do not touch it," she said. "It is not a gift. It is a lien. I have put a little of the Abyss back where the Abyss came from, and it will want to come out again. When it does, I will put it back."{/n}''',
        c('"Why are you really doing this?"', "why"),
        c("[Sleep.]", "end")),
    nar("why", '''{n}"Because it is mine." She said it at once, as if the answer had been waiting. "The Wound in the world is mine. This one is mine. You are the only record of my work that I have not burned, Commander, and I will not have it spoiled by something as stupid as bleeding to death."{/n}
{n}She wiped her hands, finger by finger, on a clean cloth. "Also, you have not yet told me how you did it. I refuse to lose my only witness before I have taken the evidence."{/n}''',
        c("[Sleep.]", "end")),
    nar("end", '''{n}Afterwards she wrote for a long time. The Commander, lying very still, read the heading upside down: "The Wound: Observations. Volume One." There would be others. It opened again the next year, and the year after, and every time she was already awake.{/n}'''),
], after="scene:areelu.trickster.report.participation", any_group=TRICKSTER_ENDINGS)

report("areelu.trickster.report.crossroads", "The report: the crossroads", [
    nar("start", '''{n}In the sixth year she asked to see the Wound.{/n}
{n}It was not the Worldwound any longer. The Commander's joke had seen to that: it had become the Crossroads of Worlds, open to every outsider at once, and angels and demons walked its edges among the merchants, scholars and treasure hunters who crowded in to sell each other pieces of it.{/n}''',
        c("[Take her there.]", "there"),
        c('[Joke] "It\'s very popular now. You\'d hate it."', "hate")),
    nar("hate", '''{n}"I intend to hate it thoroughly and in person," said Areelu. "Fetch the horses."{/n}''',
        c("Continue", "there")),
    nar("there", '''{n}She stood on the lip of the thing she had made and looked down into it for a long time, while the noise of the market came up at them like steam: hawkers, bells, and somewhere an angel and something with too many legs haggling over the price of a drink.{/n}
{n}A stall at the edge was selling pages. "Genuine notes of the witch Areelu Vorlesh," the sign said, "rescued from Threshold. Ten gold a leaf."{/n}''',
        c("[Buy one for her.]", "buy"),
        c('[Joke] "Tell him they\'re forgeries. Loudly."', "loud"),
        c("[Watch what she does.]", "watch"),
        c("[Walk with her down to the rift itself.]", "rift")),
    nar("rift", '''{n}They went down past the last stall and the last tent, to where the ground was glass and the air tasted of iron, and stood at the edge of the opening itself. Far below, something vast turned over in its sleep. At the horizon, very small, an angel and a demon were playing dice on a rock, with great care.{/n}
{n}"I stood here," she said. "A little to the left. It was quieter then." She held out her hand over the edge, palm down, as if feeling for warmth from a stove. "It does not know me. I made it, and it does not know me at all. It has no use for its maker now."{/n}''',
        c("Continue", "rift_after")),
    nar("rift_after", '''{n}She took her hand back and put it in her pocket, and they walked up out of the Crossroads without speaking.{/n}
{n}At the top she stopped, and looked back once. "When you made it into a market," she said, "I was angry. I have decided I am not angry. They have found a use for it I did not intend." A pause. "Do not tell anyone I said so. They will want to sell that too."{/n}''',
        c("Continue", "end")),
    nar("buy", '''{n}The Commander bought a leaf and put it in her hand.{/n}
{n}It was a forgery, of course. She read it through twice, took out her pen, and corrected it: the arithmetic, the Sarkorian, and a conclusion about Nahyndrian crystals that would have killed anyone foolish enough to follow it. Then she handed it back to the stallholder. "Now it is worth ten gold," she said. "Charge twenty."{/n}''',
        c("Continue", "buy_mortal", requires=MORTAL),
        c("Continue", "buy_witch", forbids=MORTAL)),
    nar("buy_mortal", '''{n}On the ride home she was silent for an hour, and then said, to the road: "I could not make anything the real one describes, now. I corrected it from memory; the fire took the pages and the cauldron took the power, and memory is what is left." She looked at her ink-stained fingers. "That forger has more of my work in his stall than I have in my head. I find that I do not mind as much as I expected. Write that down; I want to know, in ten years, whether it was true."{/n}''',
        c("Continue", "end")),
    nar("buy_witch", '''{n}The stallholder took the leaf back, and looked at the corrections, and looked up at the woman who had made them, and saw something in her crimson eyes that made him sit down very suddenly on his own stock.{/n}
{n}"He knows," the Commander said, on the ride home. "Yes," said Areelu. "He will sell twice as many, and never say why, and tell his grandchildren on his deathbed. That is the kind of fame I prefer, Commander: the kind that is too frightened to speak."{/n}''',
        c("Continue", "end")),
    nar("loud", '''{n}"Forgeries!" the Commander announced, to the whole market. "The Architect never wrote a page that bad in her life!"{/n}
{n}Heads turned. The stallholder went red. Areelu stood very still beside the Commander with her hood up and her face perfectly blank, and the Commander could feel her trembling with something that was either fury or laughter and was not going to be allowed to be either in public.{/n}
{n}She did not speak until they were a mile out of the Crossroads. Then she said: "He will sell twice as many now. You have made him famous. You have made me famous for bad handwriting."{/n}''',
        c("Continue", "end")),
    nar("watch", '''{n}She did not buy anything. She read the forged leaves over the stallholder's shoulder, one after another, with the expression of a teacher marking a hopeless class, and moved on.{/n}
{n}At the very edge of the Crossroads, where the market thinned out and the rift began, she stopped and took a stone from the ground: an ordinary stone, grey, cracked by the heat. She put it in her pocket. The Commander never asked why, and she never said, but it sat on her desk for the rest of her life, holding down the pages of the report.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}Entry, the sixth year: "Visited the site of the original experiment. It has been colonised by merchants. The angels and demons are still at its edges, doing business instead of war, which is to say the result is unchanged and the method is worse. Subject found this amusing. Observer did not. Observer is revising that position."{/n}''',
        paragraphs=(
            p('''{n}She rode home in silence with her hands in her lap, and did not once look back at the rift. At the ridge she put up her hood and let the road hide it.{/n}''', requires=MORTAL),
            p("{n}She rode home with the wound above her heart burning violet under her collar the whole way, and did not "
              "once touch it. The Commander asked, at the gate, whether it hurt.{/n} \"It recognised me,\" {n}she said.{/n} "
              "\"Even if the rift did not. That is worse.\"", forbids=MORTAL),
        )),
], after="scene:areelu.trickster.report.wound", any_group=("ending.trickster_allplanes", "ending.trickster_allplanes_fw"))

report("areelu.trickster.report.prison", "The report: the prison", [
    nar("start", '''{n}In the autumn of the sixth year she went back to Threshold.{/n}
{n}Past the burnt workrooms, to the surviving cells: the cells where Sarkoris had kept its mages, where she had been kept, and from which she had slipped away at night to the demiplane where she first decided to open the Wound. The Commander went with her, because she did not ask.{/n}''',
        c("[Follow her down to her old cell.]", "cell"),
        c("[Ask to see where she used to slip away.]", "away"),
        c('[Joke] "Do you want me to lock the door behind you? For old times\' sake."', "lock"),
        c("[Wait at the top of the stairs.]", "wait")),
    nar("lock", '''{n}She stopped on the stair and looked back, and for a moment the Commander thought the joke had gone too far.{/n}
{n}"Yes," she said. "Do. I want to see whether I can still get out." Then, before the Commander could decide whether she meant it: "No. I have been locked in by better jailers than you, Commander. Come down. I want a witness."{/n}''',
        c("Continue", "cell")),
    nar("wait", '''{n}The Commander waited at the top of the stairs for an hour, and then another, while the torchlight below moved from cell to cell and stopped.{/n}
{n}When she came up at last, there was dust on her knees and her face was perfectly composed. "You should have come down," she said. "It was very instructive. I have decided that I do not need to see it again. I needed to see it once, with somebody waiting at the top."{/n}''',
        c("Continue", "end")),
    nar("away", '''{n}She took the Commander to a place in the wall of the third corridor that looked like every other place in the wall, and pressed two stones, and nothing happened.{/n}
{n}"It is closed," she said. "The door to my demiplane. It was never more than a crack, and I was the only one who could see it. When you broke the fortress, the crack went with it." She stood with her palm flat on the stone for a long time. "Good. There is nothing left in there that I want. There never was. That was the whole problem." Then she took the Commander down to her cell.{/n}''',
        c("Continue", "cell")),
    nar("cell", '''{n}Her cell was smaller than the Commander had imagined: a stone shelf for a bed, a slit for a window, and on the wall, scratched into the stone so faintly that the Commander would never have seen it without her lamp, rows and rows of tiny marks.{/n}
{n}"Calculations," she said. "I had no paper. I had no ink. I had a nail, and the wall, and a great deal of time. Most of what the world calls the Worldwound was worked out on this wall." She laid her palm flat against the marks. "They whitewashed it once. I did it all again, from memory, in a week."{/n}''',
        c("Continue", "cell_mortal", requires=MORTAL),
        c("Continue", "cell_witch", forbids=MORTAL)),
    nar("cell_mortal", '''{n}She reads the marks to the end.{/n} "The calculation was right. I cannot supply its power now. A century of the Abyss had grown through my craft. When your cauldron pulled it out, it brought the rest down with it. I tested what remained the first week. Nothing answered." {n}She sets the Commander's hand beside the marks.{/n} "Here. Before the demon lords, before the crystals. This is what I had when I began."''',
        c("Continue", "end")),
    nar("cell_witch", '''{n}She read the wall aloud, quickly, the way a scholar reads a proof she has checked a hundred times: numbers, and the names of planes, and the words of a ritual that made the lamp gutter and the Commander's old wound throb in answer.{/n}
{n}Halfway through she stopped. "No," she said. "Not here. Not with you listening." She took her hand off the wall. "I kept every promise I made in this cell. I did not promise to repeat myself. Come. We are finished here."{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}On the way out she stopped at the gate of the prison, where the hunters of Threshold had once brought her in chains, and looked at it for a long time. Then she took out her notebook, and wrote something, and tore the page out, and left it wedged in the gate for whoever came next. The Commander never learned what it said.{/n}'''),
], after="scene:areelu.trickster.report.crossroads")

report("areelu.trickster.report.cult", "The report: old masters", [
    nar("start", '''{n}In the seventh year her old masters remembered her.{/n}
{n}She had served Deskari and Baphomet, and not merely as the lowest in the pecking order. When the war ended, the Locust Lord's surviving cultists went looking for the one mortal who knew how to make a Nahyndrian crystal from the blood of a living demon lord. They found the Commander's house.{/n}''',
        c("[Joke] \"Tell them the Architect is out. Tell them to leave a message.\"", "message"),
        c("[Ask what they want from her, before anyone draws a knife.]", "ask"),
        c("[Look for who else is watching.]", "watchers"),
        c("[Let her deal with them.]", "deal_mortal", requires=MORTAL),
        c("[Let her deal with them.]", "deal_witch", forbids=MORTAL)),
    nar("message", '''{n}The message is pinned to the door with a knife and written in blood. Areelu pulls it free.{/n} "He would not use that title. These fools have not spoken to their master." {n}She writes one sentence beneath the threat and pins it back.{/n} "Let them come for the answer. I want to know who sent them."''',
        c("Continue", "deal_mortal", requires=MORTAL),
        c("Continue", "deal_witch", forbids=MORTAL)),
    nar("ask", '''{n}The one who spoke for them had eyes like a swarm of bees behind glass. "The method," he said. "The crystal from living blood. The Locust Lord remembers who taught his servants. He would have it written down."{/n}
{n}"Would he." Areelu considered him with something like professional sympathy. "Then he should have kept his servant alive."{/n}''',
        c("[Offer to sell them the method yourself.]", "sell"),
        c("Continue", "deal_mortal", requires=MORTAL),
        c("Continue", "deal_witch", forbids=MORTAL)),
    nar("sell", '''{n}"I'll sell it to you," said the Commander. "Her whole method, written out fair. Name a price."{/n}
{n}Areelu turned and looked at the Commander, slowly, with an expression the Commander had not seen on her face since Threshold: the one she used to wear for a very promising specimen. "You would sell my work to Deskari's vermin," she said. "In my own kitchen." A pause. "For how much?"{/n}
{n}They settled on a sum that made the swarm-eyed man's hands shake. She wrote the method out herself. It was correct in every particular but one.{/n}''',
        c("Continue", "sold")),
    nar("sold", '''{n}Six weeks later, in a cave somewhere in the Abyss-scarred hills, the cultists followed the method exactly as written, and what grew in their vessel was not a crystal. It was hungry, and it ate every one of them before it starved.{/n}
{n}Areelu counted the money twice and gave the Commander exactly half. "You took their gold and I took their lives," she said. "That is a fair division of labour. Do not do it again without asking me first. You undercharged."{/n}''',
        c("Continue", "end")),
    nar("deal_mortal", '''{n}She had no magic to meet them with. She sat down at the kitchen table instead and wrote the method out for them, in full, in her small neat hand, while they watched.{/n}
{n}It was correct in every particular but one. Six weeks later, in a cave somewhere in the Abyss-scarred hills, the cultists followed it exactly as written, and what grew in their vessel was not a crystal. It was hungry, and it ate every one of them before it starved.{/n}''',
        c("Continue", "deal_mortal_after")),
    nar("deal_mortal_after", '''{n}Six weeks later a broadsheet reports the bodies found at the cave. Areelu clips the account and keeps it beside the method she gave them.{/n}
{n}"You gave them a trap," said the Commander. "I gave them a method," said Areelu Vorlesh. "They did not check my calculations. I would not have hired them either." She did not look sorry. She did not look pleased. She looked like someone who had finished a piece of work, and put it away.{/n}''',
        c("Continue", "end")),
    nar("deal_witch", '''{n}She met them at the door, and the night came in behind her like a dog at her heel.{/n}
{n}"I served your master when you were eggs," said Areelu Vorlesh. "I taught him what he knows about crystals, and I did not teach him everything. Tell him the Architect is retired. Tell him she is not taking students."{/n}
{n}One of them laughed. She looked at him, and he stopped laughing, and then, in a way the Commander never afterwards liked to describe, he stopped.{/n}''',
        c("Continue", "deal_witch_after")),
    nar("deal_witch_after", '''{n}The others went. She shut the door and leaned on it, and for a moment she looked every one of her years.{/n}
{n}"I could have taught them," she said. "It would have been easy. It is always easy, the first time." She pushed herself off the door. "Write down that I did not. Write it in your own hand. I want a witness who is not me."{/n}''',
        c("Continue", "end")),
    nar("watchers", '''{n}The Commander looked past the cultists at the door, to the far end of the street, and found what Areelu had already found: a figure in a horned hood, very still, who had not come with the Locust Lord's people and was not leaving with them.{/n}
{n}"Baphomet's," she said quietly. "He sends a watcher whenever Deskari sends a knife. They have been watching each other for longer than these cultists have lived. I used to find it amusing." She did not take her eyes off the cultists. "Tonight I find it useful. Whatever I do to these, the watcher will carry home. Let us give him a good story."{/n}''',
        c("Continue", "deal_mortal", requires=MORTAL),
        c("Continue", "deal_witch", forbids=MORTAL)),
    nar("end", '''{n}The swarm did not come back. Neither did Baphomet's people, who had been watching from further off, and who drew their own conclusions from what they had seen. Her name went back into the dark it had come from, with a warning written under it.{/n}'''),
], after="scene:areelu.trickster.report.prison")

report("areelu.trickster.report.incursion", "The report: the incursion", [
    nar("start", '''{n}In the seventh summer something came up out of the open Wound that the angels and the demons at its edges had both missed, and it came south.{/n}
{n}It came as a swarm: locusts the size of dogs, and under them something larger that moved like weather. By the time the bells rang in the town where the Commander and the Architect lived, it was a day away, and the garrison was forty spears and a captain who had never seen a demon.{/n}''',
        c("Continue", "plan_mortal", requires=MORTAL),
        c("Continue", "plan_witch", forbids=MORTAL)),
    nar("plan_mortal", '''{n}She had no magic. She had something the captain had never had: a century of watching Deskari's children eat the world.{/n}
{n}She took over the captain's table without asking and drew the swarm for him on the back of a map, faster than he could follow: how it would come, where it would split, what it would eat first and why, and which bell tower it would go round rather than over. "It is not clever," she told him. "It is hungry. Hunger is predictable. I should know."{/n}''',
        c('[Joke] "And what\'s my part in this? Bait?"', "bait"),
        c("[Do exactly as she says.]", "obey"),
        c("[Change one thing in her plan.]", "change")),
    nar("plan_witch", '''{n}She stood at the top of the bell tower in the hot wind and watched it come, and the Commander watched her watch it, and neither of them said what they were both thinking: that she could call it off, or turn it, or make it hers.{/n}
{n}"I could," she said, without looking round. "It would take a word. Deskari would hear the word, and he would know where I am, and he would never stop sending things like this until the town was a crater. Or I could fight it the slow way, with you, and nobody in the Abyss would ever know I was here."{/n}''',
        c('"The slow way."', "slow"),
        c('"Say the word. We\'ll deal with Deskari when he comes."', "word"),
        c('[Joke] "Or we could just move. I hear Absalom is nice this time of year."', "absalom")),
    nar("bait", '''{n}"Yes," she said, without looking up from the map. "Obviously. It has been hunting you since Kenabres; it can smell what I put in your soul. You will stand in the square and be the most interesting thing it has ever seen, and while it looks at you, the captain will do his job."{/n}
{n}She glanced up. "You asked. You always ask, and then you do it anyway. I have enough notes on it."{/n}''',
        c("Continue", "held")),
    nar("obey", '''{n}The Commander leaves the line where Areelu drew it. Bells, barricades and pitch defend the square. The road to the orphans' hall remains outside the wall of spears. The captain protests once.{/n} "Guard that road and lose the square," {n}she tells him. He sends two runners to get the children out. Only one returns.{/n}
{n}The square holds. The hall burns beyond the line. In the morning the returning runner names the children who got out and those who did not. Areelu records both lists without changing the plan.{/n}''',
        c("Continue", "held")),
    nar("change", '''{n}The Commander moves the barricade to cover the road to the orphans' hall. Areelu sees the gap left at the east wall.{/n} "That costs you men." {n}The Commander leaves it where it stands. She tears the east side off her sketch and draws it again.{/n} "Put the veterans here. No runners. They hold until the children are inside."
{n}The children reach the gate. Nine of the veterans die holding the altered line. Their bodies lie at the east wall when the captain comes to thank the Commander. Areelu turns the notebook so he can read the names before he speaks.{/n}''',
        c("Continue", "held")),
    nar("held", '''{n}By dawn the survivors are dragging the dead clear of the gates. The largest locusts lie in the square, around the place where the Commander stood; smaller bodies clog the burnt barricades. Areelu walks the line with her notebook. Nobody asks her to count twice.{/n}''',
        c("Continue", "end")),
    nar("slow", '''{n}They did it the slow way: with bells, and pitch, and the garrison's forty spears, and the Architect of the Worldwound on the bell tower picking out the largest of the things with small, precise workings that looked, from the ground, like nothing at all, and left nothing where they touched.{/n}
{n}Nobody in the town ever knew what she had done. That was the point. Deskari never learned where she was.{/n}''',
        c("Continue", "end")),
    nar("word", '''{n}She said the word.{/n}
{n}The swarm stopped in the air a mile from the walls, all at once, like a held breath, and then turned, all at once, and went back north the way it had come. The garrison cheered. She did not. "He heard," she said. "He knows where I am now, and that I spoke to his children, and that they listened. You have bought one summer, Commander, and paid for it with every summer after. I hope it was worth it."{/n}''',
        c("Continue", "word_after")),
    nar("word_after", '''{n}They moved house that autumn, and twice more in the years after, each time a little ahead of something coming south. She never complained about it. She kept a map of the moves in the back of the notebook, with a date beside each, and a note at the bottom: "Price of one summer, paid in instalments. Acceptable."{/n}''',
        c("Continue", "end")),
    nar("absalom", '''{n}"Absalom." She turned, and for a moment she was genuinely, openly appalled. "A city full of priests, all of whom would recognise me. No." And then, because the joke had done what the Commander meant it to, and broken whatever had been tightening in her: "The slow way, then. Fetch the captain. And stop looking at me as if I might say the word. I might. Keep talking."{/n}''',
        c("Continue", "slow")),
    nar("end", '''{n}Entry, the seventh summer: "Incursion from the Wound. Repelled. Losses within tolerance. Observer's contribution not recorded, by the observer's request." Beneath it, in the laughing hand: "She was magnificent. She will cross this out." She did not.{/n}'''),
], after="scene:areelu.trickster.report.cult", any_group=TRICKSTER_ENDINGS)

report("areelu.trickster.report.dagger", "The report: the dagger", [
    nar("start", '''{n}In the eighth spring she asked for the dagger.{/n}
{n}In Kenabres she had left the Commander a dagger made from Deskari's freshly shed blood. It had proved that her method could draw a crystal from a living demon lord.{/n}''',
        c("[Give it to her.]", "give", requires=(DAGGER_HELD,)),
        c('"Why now?"', "why", requires=(DAGGER_HELD,)),
        c('[Joke] "Finders keepers."', "keepers", requires=(DAGGER_HELD,)),
        c('[Joke] "I\'ve been using it to open letters."', "letters", requires=(DAGGER_HELD,)),
        c('"It\'s gone. You knew that."', "gone", forbids=(DAGGER_HELD,)),
        c('[Joke] "Would you settle for a letter-opener?"', "gone_joke", forbids=(DAGGER_HELD,)),
        paragraphs=(
            p("{n}The Commander still had it. She knew exactly where.{/n}", requires=(DAGGER_HELD,)),
            p('''{n}The Commander did not have it. It had gone into the wardstone at the Gray Garrison during the assault, to cut the corruption out of the stone with the fallen angels inside it, and the crystal had been spent in the cut. She knew that too. She asked anyway.{/n}''', requires=(WARDSTONE_CLEANSED,),
              forbids=(DAGGER_HELD,)),
            p("{n}The Commander did not have it. Somewhere between Kenabres and Threshold it had been sold, or traded, or "
              "left in a pack on a battlefield, and the Commander could not have said which. She knew that too. She asked "
              "anyway.{/n}", forbids=(DAGGER_HELD, WARDSTONE_CLEANSED)),
        )),
    nar("gone_joke", '''{n}"A letter-opener." She held out her hand anyway, palm up, and left it there until the Commander understood that there was nothing to put in it, and said where the dagger had gone.{/n}''',
        c("Continue", "gone")),
    nar("gone", '''"I knew. I wanted to hear you say it." {n}She leaves her hand open for another moment, then lowers it.{/n} "I left that blade for you in Kenabres. I would have liked to examine it again."''',
        c("Continue", "end_gone"),
        paragraphs=(
            p('''"On a wardstone," {n}she said.{/n} "On angels. The crystal I drew from Deskari's living blood, and you used it to mend a crusader's fence." {n}A pause.{/n} "It is the best joke anyone has made with my work, and I did not make it. I dislike that more than the loss."''', requires=(WARDSTONE_CLEANSED,)),
            p("\"Sold,\" {n}she said.{/n} \"Or lost. You do not even know which.\" {n}A pause.{/n} \"I spent a century making a thing "
              "nobody could make, and you mislaid it. I find I do not mind as much as I should, and I intend to find out "
              "why.\"", forbids=(WARDSTONE_CLEANSED,)),
        )),
    nar("end_gone", '''{n}Entry, the eighth spring: "Asked for the Kenabres blade. Not in the subject's custody. Method recalled regardless; it is in my hands, not in the knife." And, beneath it, smaller: "Subject did not lie about it. That is rarer than the crystal."{/n}'''),
    nar("letters", '''{n}She closed her eyes for a moment, the way she did when a calculation came out wrong in a way she found personally insulting.{/n}
{n}"The crystal I drew from Deskari's living blood," she said. "A century of work. The proof that the laws of the Abyss could be broken. And you have been opening your correspondence with it." She opened her eyes. "Give it to me before you use it to butter bread. I know you. You were going to."{/n}''',
        c("Continue", "give")),
    nar("keepers", '''{n}"I left it for you to find," she said. "That is not the same thing as giving it to you. Read the terms, Commander. You taught me that."{/n}
{n}She held out her hand, and waited, and did not blink, and after a while the Commander found that it was easier to give her the dagger than to go on being looked at like that.{/n}''',
        c("Continue", "give")),
    nar("why", '''{n}"Because I made it, and I want it in my hands again." She looks toward the Commander's boot.{/n} "The fire took my records. I would like to see what I can recover from the crystal. Give it here."''',
        c("[Give it to her.]", "give"),
        c("[Keep it.]", "keep")),
    nar("give", '''{n}She turned it over in her hands for a long time, with her thumb against the gold fitting, turning the crystal toward the lamp.{/n}''',
        c("Continue", "give_mortal", requires=MORTAL),
        c("Continue", "give_witch", forbids=MORTAL)),
    nar("give_mortal", '''{n}"It is only a knife now," she said at last. "To me. I can see the work in it and I cannot feel it. You did that, with the Council's crystal." She laid it on the table between them. "Keep it. It is yours. It always was; I only made it."{/n}
{n}She never asked for it again. But the Commander noticed, over the years, that she always knew which room it was in.{/n}''',
        c("Continue", "end")),
    nar("give_witch", '''{n}The blade woke in her hand. The Commander felt it across the room: a low, eager hum, like a swarm heard through a wall, and her crimson eyes went bright with something that was not quite hunger and not quite memory.{/n}
{n}Then she put it down. "Yes," she said. "I still know how. That is all I wanted to know." She pushed it back across the table with one finger. "Take it away. Put it somewhere I do not know. I would like, for once, not to know something."{/n}''',
        c("Continue", "end")),
    nar("keep", '''{n}"Very well," she said, and did not argue, which was worse than arguing.{/n}
{n}Three nights later the Commander woke to find her sitting on the end of the bed in the dark, with the dagger across her knees, looking at it. She had not taken it out of its sheath. "I only wanted to hold it," she said. "I have held it. Go back to sleep." In the morning it was back in the Commander's boot, and she did not mention it again.{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}Entry, the eighth spring: "Examined the Kenabres blade. Method recalled. Method not used. Subject retains custody." And, beneath it, smaller: "Subject would have given it back. That is the problem with the subject."{/n}'''),
], after="scene:areelu.trickster.report.incursion")

report("areelu.trickster.report.lady", "The report: the Lady's clerk", [
    nar("start", '''{n}In the autumn of the eighth year a grey bird came to the window and did not leave.{/n}
{n}It was not a bird. It sat on the sill for three days without eating, and looked at the Commander with one eye and then the other, and on the third evening it spoke. "The Lady of Graves keeps an appointment book," it said, in a voice like pages turning. "The Commander's appointment is overdue. The Lady does not hurry. She does, eventually, collect."{/n}''',
        c('[Joke] "Tell her I\'ve been meaning to reschedule."', "reschedule"),
        c("[Let Areelu answer it.]", "answer"),
        c('"I cheated fair and square. What does she want?"', "fair")),
    nar("reschedule", '''{n}"Everyone has been meaning to reschedule," said the bird. "The Lady has heard it before. She has heard everything before."{/n}
{n}Areelu sets down her pen. She watches the bird until it turns toward her. Then she draws the notebook closer.{/n}''',
        c("Continue", "answer")),
    nar("fair", '''{n}"The Lady does not want. The Lady records," said the bird. "A thing that should have ended has not ended. The Lady would like the book to balance."{/n}
{n}Areelu sets down her pen. She watches the bird until it turns toward her. Then she draws the notebook closer.{/n}''',
        c("Continue", "answer")),
    nar("answer", '''{n}"Your Lady's claim on every soul is a law I have spent a century trying to break," said Areelu Vorlesh, to the bird. "I have not changed my opinion of it. It is a bad law, and I would break it tomorrow if I could."{/n}
{n}"I cannot. I have learned the difference between a law I despise and a creditor who can enforce it. She is owed the Commander, and she is owed me; my page has waited a hundred years. I have not come to argue with her justice. I have come to trade."{/n}''',
        c("Continue", "ledger_mortal", requires=MORTAL),
        c("Continue", "ledger_witch", forbids=MORTAL)),
    nar("ledger_mortal", '''{n}She sits at the kitchen table with no magic left to lend weight to the offer.{/n} "I left souls in vessels, in laboratories the crusade found and others it missed. I know where I put them and how to open the seals. The sequence that closed them will open them by hand. Your collectors can search every ruin. Or I can give them the record and go myself." {n}She puts her hand over the closed notebook.{/n} "I expect that work to be worth something."''',
        c("Continue", "ledger")),
    nar("ledger_witch", '''{n}The lamp burns violet as she speaks. The bird does not move.{/n} "I left souls in vessels, in laboratories the crusade found and others it missed. I know where I put them and how to open the seals. Your collectors can search every ruin. Or I can give them the record and go myself." {n}She lets the flame subside.{/n} "I am making an offer."''',
        c("Continue", "ledger")),
    nar("ledger", '''{n}"The Lady knows where every soul goes," says the bird. "Do not sell us her own knowledge. You offer the record of your thefts and the work of fetching what remains. Give the method to her clerks as well." Areelu's fingers stop on the cup.{/n} "My method. A century." {n}She draws the notebook toward her.{/n} "Very well."
{n}She keeps her hand on the notebook. "Every vessel I made, found and opened with my own hands, and what is in each sent to her river; and the method, in full, to her clerks. It will take me the rest of my life. For it, the Commander's appointment keeps its natural date, not an hour earlier. And my own page closes without appeal: when she sends for me, I go before her without a plea and without a single clause." She turned to the Commander. "A hundred years of arguments, and my life's research. I am selling both for your death on time."{/n}''',
        c("[Let it stand.]", "stand"),
        c('"No. Keep your arguments. You\'ll need them."', "refuse"),
        c('[Joke] "Can we pick the date? I have a very full calendar."', "date")),
    nar("date", '''{n}The bird turns one grey eye on the Commander.{/n}
{n}"The Lady does not negotiate dates," it said. "She keeps them. That is what is being bought: that she keeps this one." It considered Areelu at length, one eye and then the other. "If one vessel is still sealed when your page closes, the terms fall, and she collects both pages the same night." "I know what I built," said Areelu. It was the first thing she had said to the bird that sounded like a threat.{/n}''',
        c("Continue", "stand")),
    nar("stand", '''{n}The bird bowed its head, once, and went. Where it had been sitting, the sill was covered in a fine grey dust, like ash, and in the dust, written as if with the tip of a feather: two names, and beneath them a number the Commander did not want to read.{/n}
{n}Areelu wiped it away with her sleeve. "I have not bought your life, Commander. I have bought your death on time, which everyone else is given for nothing. You had spent yours. I intend to keep what I spent so long making."{/n}''',
        c("Continue", "end")),
    nar("refuse", '''{n}"Keep them for what?" said Areelu. "For the day she sends for me, and I stand in front of her with a hundred years of clauses, and win, and you are already in her garden?" She did not look at the Commander. She looked at the bird. "Write it as I said. I am not asking."{/n}
{n}The bird wrote it. When it had gone she sat for a long time with her hands flat on the table. "Do not ever tell me what I may spend," she said at last. "I have been deciding that for myself since before your grandparents were born."{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}They went for the first vessel that spring, to a cellar under a burned farmhouse near the old Sarkorian border, where she had once kept a laboratory nobody else had found. It took her a day to remember the sequence and an hour to open it, with the Commander holding the lamp. What came out of it the Commander did not see, only felt: a cold that went past them both, up the cellar steps, toward a river nobody living can see.{/n}
{n}"You think it is a gift," she said, on the road home. "It is not a gift. It is a debt I have owed since before you were born. I have only found somebody who will take it in payment for yours."{/n}''',
        c("Continue", "entry")),
    nar("entry", '''{n}Entry, the eighth year, underlined: "Terms agreed. Every vessel, in my hand. The method, to her clerks. Appeal waived. Opened: one." And beneath it, in a hand the Commander did not recognise and would not have wished to: "Received."{/n}'''),
], after="scene:areelu.trickster.report.dagger", any_group=(CHEATED,))

report("areelu.trickster.report.visitors", "The report: visitors", [
    nar("start", '''{n}People began to come to the house on purpose: not hunters, not cultists, but the curious. Some of them had known the Commander in the war. Areelu kept a list of them too, in a separate column.{/n}''',
        c("[Let Nenio in.]", "nenio", forbids=NENIO_GONE),
        c("[Let Ember in.]", "ember", forbids=("ember_dead", "ember_gone")),
        c("[Let the old knight in.]", "knight"),
        c("[Let Daeran in.]", "daeran", forbids=("daeran.dead", "daeran.kicked_out", "trickster.ever")),   # retired (ledger: Nenio, Ember)
        c("[Let the girl with the drum in.]", "drum"),
        c("[Close the door on the curious.]", "shut"),
        # G6(b), added with Nenio's route (append-only): she comes back on the Trickster path; never after the dissolution.
        c("[Let Nenio in.]", "nenio", requires=(NENIO_BACK,), forbids=("nenio.dissolved",))),
    nar("nenio", '''{n}Nenio arrives with calipers and forty questions.{/n} "The Worldwound has ceased to behave as you intended. I would like your account of the failure." {n}Areelu draws a second chair to the desk.{/n} "Which failure? Be precise." {n}Nenio sits. Neither asks whether the Commander intends to stay awake.{/n}''',
        c("Continue", "nenio_after")),
    nar("nenio_after", '''{n}They argued until three in the morning about the classification of planar wounds, and neither of them conceded a single point, and the Commander fell asleep in a chair listening to them.{/n}
{n}When Nenio finally left, Areelu stood in the doorway watching the kitsune go down the street with her folio clutched to her chest. "She is wrong about nearly everything," she said. "Invite her back."{/n}''',
        c("Continue", "nenio_mortal", requires=MORTAL),
        c("Continue", "nenio_witch", forbids=MORTAL)),
    nar("nenio_mortal", '''{n}Nenio came back every year after that, with a new list of questions and a new pair of calipers, and measured the Architect's ageing as carefully as Areelu measured it herself. They compared notes. Areelu's were better. Nenio's were funnier. Neither of them ever admitted either.{/n}''',
        c("Continue", "end")),
    nar("nenio_witch", '''{n}Nenio came back every year after that, and every year asked to measure the wound above Areelu's heart, and every year was refused. On the ninth visit Areelu let her, for exactly one minute, by the sand-glass. Nenio wrote for six hours afterwards and would not show anyone what, and Areelu, for once, did not ask.{/n}''',
        c("Continue", "end")),
    nar("ember", '''{n}Ember brings apples and a cat that does not belong to her.{/n} "You look tired. I thought you might want these." {n}She sets the basket beside the notebook.{/n} "I still think there's something you regret. You don't have to tell me what it is."''',
        c("Continue", "ember_after")),
    nar("ember_after", '''{n}Areelu leaves the apples beside her papers until Ember goes. Then she cuts the bruised part from one with her knife.{/n} "She expects me to repent over a basket of fruit. I would do it again. I would not lose the soul this time." {n}She pushes the basket away from the notebook and resumes writing.{/n}''',
        c("Continue", "end")),
    nar("daeran", '''{n}Daeran arrived with two bottles of wine and no apology, and looked at the Architect of the Worldwound across the Commander's kitchen table with open, delighted interest, as if at a rare animal in a menagerie.{/n}
{n}"My dear," he said. "You opened a hole in the world and let the Abyss pour through it for a century, and here you are, darning. I have never been so happy to be wrong about a woman." "You are not wrong," said Areelu. "You are merely early. Sit down. I have heard about you. I have questions about Mendev."{/n}''',
        c("Continue", "daeran_after")),
    nar("daeran_after", '''{n}They drank both bottles and a third, and he told her things about Mendev's inquisition that the Commander had not known, and she told him things about the Abyss that made him go quiet for almost a minute, which the Commander had never seen before.{/n}
{n}At the door, very late, he kissed her hand. She let him. "Do come again," she said, "when you are prepared to be honest." "My dear," said Daeran, "I shall never be prepared for that." "Then come anyway," said Areelu Vorlesh, and shut the door.{/n}''',
        c("Continue", "end")),
    nar("knight", '''{n}He had fought at the edge of the Worldwound for forty years, he said, and he had never once seen the face of the woman who made it. He did not want to hurt her. He was too old. He only wanted to look.{/n}
{n}Areelu let him. She sat very straight at the kitchen table and let him look for as long as he liked, and looked back. When he had finished, he said, "You're smaller than I thought." "You expected something else?" said Areelu Vorlesh. He laughed, which surprised them all, and went.{/n}
{n}"Forty years," she said, when the door had closed. "He was eighteen when he came to the Wound, and he is fifty-eight now, and every year in between belongs to me. He did not even want to hit me." She sat very still. "I would have preferred it if he had."{/n}''',
        c("Continue", "end")),
    nar("drum", '''{n}She was perhaps fifteen, Sarkorian by her braids, and she carried a spirit drum that was far too old for her. She had come, she said, from the camps. The god-caller who had taught her was dead. Nobody else would teach her the old calls, because nobody else remembered them.{/n}
{n}"Except you," she said to Areelu. "They say you were one of us, before."{/n}''',
        c("Continue", "drum_after")),
    nar("drum_after", '''{n}Areelu looked at the drum for a long time. Then she said, "No. I will not teach you. What I would teach you would not be the old calls. It would be mine." She wrote a list on a sheet of paper, fast, in Sarkorian: names of spirits, of places, of words the girl might still find in the camps if she asked the oldest people there. "Go and ask them. Not me."{/n}
{n}The girl went. Areelu did not watch her go. The Commander did, and saw her stop at the corner, and unfold the list, and start, very softly, to beat the drum.{/n}''',
        c("Continue", "end")),
    nar("shut", '''{n}The Commander closed the door on the curious, and after a while they stopped coming.{/n}
{n}"You did that for me," said Areelu, not looking up. "Do not. I have been stared at by better people than these, and by worse. Let them look. It costs me nothing, and I learn something from every face."{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}Her list of visitors grows beside the wound observations. Some names acquire a date for another visit. Others are crossed out. She keeps the list in Sarkorian, and writes the questions she intends to ask them next.{/n}'''),
], after="scene:areelu.trickster.report.lady")

report("areelu.trickster.report.name", "The report: a name", [
    nar("start", '''{n}In the ninth winter she said a name in her sleep.{/n}
{n}It was not the Commander's name. It was short, and old, and Sarkorian, and she said it the way people say a name they have said ten thousand times into the dark, without expecting an answer. Then she woke, and saw the Commander's face, and knew at once that it had been heard.{/n}''',
        c("[Ask whose name it was.]", "ask"),
        c("[Say nothing, and let her go back to sleep.]", "nothing"),
        c("[Say the name back to her, softly.]", "back")),
    nar("ask", '''{n}She sits up and pulls the blanket around her shoulders.{/n} "You know whose name it is. You heard it while I slept. That does not make it yours." {n}She looks at the Commander now.{/n} "My {mf|son|daughter}. The Wound took everything else. I will not give you this too. Do not ask me to say it for you."''',
        c("Continue", "end")),
    nar("nothing", '''{n}The Commander said nothing. After a long time she lay down again, with her back to the Commander, very straight.{/n}
{n}Near dawn her hand found the Commander's in the dark, and held it, hard, the way she had held it at Threshold. Neither of them mentioned it in the morning. The entry for that night, when the Commander looked later, was a single blank line, ruled very carefully, as if something were meant to be written on it and never had been.{/n}''',
        c("Continue", "end")),
    nar("back", '''{n}The Commander said the name back to her, softly, once.{/n}
{n}She went white to the lips. For a moment the Commander saw in her face exactly what the hunters must have seen, a hundred years ago, when they turned from the door and found her there. Then it passed. "Never," she said, very quietly, "do that again." And then, after a long time, even more quietly: "You said it wrong. The second sound is softer. Nobody has said it aloud in a hundred years but me."{/n}''',
        c("Continue", "end")),
    nar("end", '''{n}The name does not appear anywhere in the report. Scholars who have searched for it have found only a single place, in the ninth winter, where a word has been written and scraped away so thoroughly that the knife went through the page.{/n}'''),
], after="scene:areelu.trickster.report.visitors")

report("areelu.trickster.report.promise", "The report: the promise", [
    nar("start", '''{n}In the spring after that winter, the Commander found the other notebook.{/n}
{n}It was hidden where she hid nothing else: inside the one she wrote in every day, cut into the binding. Its pages were dated from the first week after Threshold. They were about the soul the Commander shared with her child: whether she could extract her child's share without losing the Commander.{/n}''',
        c("[Put it on the table between you, and wait.]", "confront"),
        c("[Put it back where you found it.]", "back"),
        paragraphs=(
            p('''{n}Diagrams proposed a working to draw out her child's share and hold it without a vessel. Figures in the margins estimated what the Commander would lose. Several estimates were crossed out; one was circled. Beside it, in her small hand:{/n} "I'll try again."'''),
        )),
    nar("confront", '''{n}She saw it on the table and did not pretend.{/n}
{n}"Yes," she said. "Every morning. I read it every morning, and every morning I put it away." Then: "Do not look at me as if I had forgotten. You share a soul with my {mf|son|daughter}. I did not stop wanting {mf|him|her} back because I lost a bet. I stopped being willing to kill you for it, which is not the same thing, and I will not pretend it is." She laid her hand on the page. "When the method can take {mf|him|her} out without costing me my only witness, and my only proof that the bet was won, I will take {mf|him|her}. Every morning I do the arithmetic again. Every morning it says: not today."{/n}''',
        c("[Burn it.]", "burn_mortal", requires=MORTAL),
        c("[Burn it.]", "burn_witch", forbids=MORTAL),
        c('"Then let\'s do it properly. Not to me. We take the case to the Lady of Graves."', "join"),
        c("[Take her hand, and leave the notebook where it is.]", "keep"),
        c('"Why haven\'t you done it?"', "why")),
    nar("why", '''{n}"Because of the promise." She said it at once, as if she had been waiting nine years for somebody to ask.{/n}
{n}"I held my child at the door and I promised that the world would not stay as it was. I have kept it. Nothing else I promised anyone survived the Wound." She laid one hand flat on the notebook. "If I take {mf|him|her} out of you now, I have my child back, a Commander who may not survive it, and a bet I lost. That is a worse result than the one I have. The arithmetic does not come out. When it does, I will not ask you first."{/n}''',
        c("[Burn it.]", "burn_mortal", requires=MORTAL),
        c("[Burn it.]", "burn_witch", forbids=MORTAL),
        c('"Then let\'s do it properly. Not to me. We take the case to the Lady of Graves."', "join"),
        c("[Take her hand, and leave the notebook where it is.]", "keep")),
    nar("back", '''{n}The Commander returns the notebook to its hiding place. That evening Areelu lays it on the table. A fine hair hangs from the binding, its ends no longer joined.{/n} "You opened it. And put it back." {n}She holds the broken hair between two fingers.{/n} "I would like to know why you left me the method."''',
        c("Continue", "kept")),
    nar("burn_mortal", '''{n}The Commander burned it in the kitchen grate, page by page, as a century of her notes had once burned after Threshold. She watched without moving.{/n}
{n}"You understand," she said, when it was ash, "that I remember every word. You took my magic and my graft with a crystal, and I let you. You do not get to take this as well." She left the next morning with nothing but the notebook she wrote in every day, and did not say where she was going.{/n}''',
        c("Continue", "burned")),
    nar("burn_witch", '''{n}The Commander burned it in the kitchen grate, page by page, as she had once burned a century of notes to pay her stake. She watched without moving, and the fire in the grate burned violet the whole time, because she was holding it very still.{/n}
{n}"You understand," she said, when it was ash, "that I remember every word, and that I could write it again tonight. I paid my stake in full. This was not part of it." She left the next morning with nothing but the notebook she wrote in every day, and did not say where she was going.{/n}''',
        c("Continue", "burned")),
    nar("burned", '''{n}Letters came for a while: from Nex, and from Geb, and once from somewhere that was not on any map. Each was a single line of observation about the Commander, sent from very far away, and each was correct. Then they stopped.{/n}
{n}The last entry of the report, found years later among the Commander's papers, is in her hand: "Subject intervened. Experiment terminated by the subject. The bet is still open."{/n}''',
        c("Continue", "burned_mortal", requires=MORTAL),
        c("Continue", "burned_witch", forbids=MORTAL)),
    nar("burned_mortal", '''{n}The last of the letters came in a hand so unsteady that the Commander did not recognise it at first: an old woman's hand, spotted with ink, pressing too hard. It said only, "Still correct. Still not today." There was no address. The Commander never learned whether "not today" had been about the notebook, or about something else, and supposed, in the end, that it had been about both.{/n}'''),
    nar("burned_witch", '''{n}The last of the letters came up out of the ground, one winter night, through the floor of the Commander's study, written in frost on the inside of a window that faced nowhere. "Still correct," it said. "Still watching. Do not look for me. I have gone somewhere the Lady keeps no pages, to see whether it is true." The frost melted before morning. The Commander copied it out before it did.{/n}'''),
    nar("join", '''{n}"Together." She said the word as if testing whether it would bear weight, and found that it would not.{/n}
{n}"No. You would make it a joke, and the Lady would laugh, and I would lose {mf|him|her} a second time to a punchline. The claim is for {mf|him|her}, and {mf|he|she} is in you. I will not have you carry your own evidence into her court." She closed the notebook. "The claim is mine. I will file it myself, priced and argued, the way her own clerks argue, in my own name. You may carry it to the door of the Boneyard, if you like. You may not come in."{/n}''',
        c("Continue", "filed")),
    nar("filed", '''{n}She spent the rest of her years on it. What she built, and what she bargained, and what it cost her, the report does not say; those pages are missing, and whoever took them out did it with a very steady hand. The Commander carried the petition to the door, once, and waited outside, as agreed.{/n}
{n}The last line of the report is in her hand: "The case is filed. It has not been heard." Beneath it, every year until the report ends, a date, and the same two words: "Not heard." The Commander never wrote in that column. It was not the Commander's.{/n}''',
        c("Continue", "afterword")),
    nar("keep", '''{n}The Commander left the notebook on the table between them, open, and did not touch it.{/n}
{n}"You are a fool," said Areelu Vorlesh. "You will wake one morning and wonder whether today is the day the arithmetic comes out differently." "Every morning." "Good," she said, and drew the notebook back across the table to her own side. "So will I. The notebook stays on my side of the table."{/n}''',
        c("Continue", "kept")),
    nar("kept", '''{n}She read the method every morning for the rest of her life, and every morning she put it away. She never explained it, and the report never records a reason. It records only the date of each reading, in a column that runs to the last page, and beside each date the same word.{/n}
{n}The last entry of the report is dated the morning she died, if she died. It reads: "Not today."{/n}''',
        c("Continue", "afterword")),
    nar("afterword", '''{n}Inside the report's back cover, the Commander writes beneath a line she left blank:{/n} "I did not know whether we would survive Threshold. I wanted enough time to find out who I had wagered with."''',
        c("[Add a line of your own.]", "aw_line"),
        c("[Leave the cover as it is.]", "aw_leave")),
    nar("aw_line", '''{n}There is one more line beneath it, added later, in the same laughing hand: "Neither. Told you so."{/n}
{n}And beneath that, in her small neat hand, her answer: "Result: neither. Experiment continues. The bet is still open, and I intend to win it."{/n}'''),
    nar("aw_leave", '''{n}The Commander left the cover as it was. Nobody has added anything since.{/n}
{n}Scholars who have handled the report say that the back cover is worn smooth in one place, as if someone had rested a thumb there, often, for many years: over the Commander's note.{/n}'''),
], after="scene:areelu.trickster.report.name")


page("areelu.trickster.report.afterword", "Afterword, in another hand", [
    nar("start", '''{n}The report ends where it ends. But on the inside of its back cover, in a hand that is not hers, someone has written a note of their own, and she did not cross it out.{/n}
{n}"For the record, since the observer never allowed it into the text: the subject knew, at Iz, when the bet was made. Not how it would end. Only that it would be worth it."{/n}''',
        c("[Add a line of your own.]", "line"),
        c("[Leave the cover as it is.]", "leave")),
    nar("line", '''{n}There is one more line beneath it, added later, in the same laughing hand: "Neither. Told you so."{/n}
{n}And beneath that, in her small neat hand, the last thing she ever wrote in any of her notebooks: "Result: neither. Experiment continues. The bet is still open, and I intend to win it."{/n}'''),
    nar("leave", '''{n}The Commander left the cover as it was. Nobody has added anything since.{/n}
{n}Scholars who have handled the report say that the back cover is worn smooth in one place, as if someone had rested a thumb there, often, for many years: over the words "worth it".{/n}'''),
], requires=("trickster.ever", STRUCK, WAGERED, SURVIVES), forbids=ROMANCE_FORBIDS, any_groups=(COMMITTED_ANY,),
    after="scene:areelu.trickster.report.promise", overrides=ROMANCE_OVERRIDES)


# Ledger row 16: when the Commander burned closing the Wound, the wager is settled the other way. The Commander burned;
# she keeps the wound, subordinate to the Lady's prior claim on the soul. (Iomedae's Appointment is one such world; her
# route can add its own variant when iomedae.appointment_kept has a producer.)
page("areelu.trickster.finale.prior_lien", "You burned", [
    nar("end", '''{n}"You burned." Areelu wrote it at the top of a clean page, and underlined it.{/n}
{n}"The Lady of Graves had the prior lien. She always does; I have spent a century reading her books and I have never once found a page she did not collect. The soul went where souls go. I keep the wound, as agreed."{/n}
{n}"It is enough to study for the rest of my life, and I intend to."{/n}''',
        paragraphs=(
            p("{n}She kept it in a jar of her own design, in a room nobody else was allowed to enter, and on the day each "
              "year that the Commander had first offered her the bet she did not open the room at all.{/n}", any_groups=(COMMITTED_ANY,)),
            p("{n}She did not thank anyone. Nobody who knew her expected her to. But the report she wrote afterwards, which "
              "is long, and precise, and entirely about a wound, ends with a single line that is not about the wound at "
              "all:{/n} \"The subject won the argument and lost the bet. I would have preferred the reverse.\""),
        ))],
    requires=("trickster.ever", BURNED, STRUCK), forbids=(CLOSED, DIED, "trickster.commander_back", "iomedae.appointment_kept"), sequence=False)


# Last Call H2 (lastcall.py): the Commander burned closing the Wound and came back, the death corked in her own flask. The
# wager is settled the same way (the Commander burned and pays the wound), but the report goes on: the Wound is closed.
page("areelu.trickster.finale.lien_bottled", "You burned, and came back", [
    nar("end", '''{n}"You burned." Areelu wrote it at the top of a clean page, and underlined it, and then, below it, in smaller letters: "And did not stay burned."{/n}
{n}"The Lady of Graves had the prior lien. She always does. You paid her collector with my crystal: the death that should have gone to her was in my flask with the cork in, and the Wound, when it closed on you, closed on an empty hook." She looked at the flask as if it had been stolen from her, which it had. "I made that. I did not make it for this. I am recording that it worked."{/n}
{n}"The terms stand. Whoever burned pays. You burned. I keep the wound, as agreed: a closed scar on a closed rift, which I can measure and cannot open. It is enough to study for the rest of my life, and I intend to."{/n}''',
        c("Continue", "across", forbids=(DECLINED, STAKE_ONLY)),
        c("Continue", "stands", requires=(DECLINED,)),
        c("Continue", "stands", requires=(STAKE_ONLY,), forbids=(DECLINED,)),
        paragraphs=(
            p('''{n}She did not go back to a laboratory. She took the rooms across the hall from the Commander's instead, with a fresh notebook and a lamp she kept burning later than anyone in the house, and on the first night she measured the scar with one hand and wrote the figure down twice, once for each of them.{/n}''',
              any_groups=(COMMITTED_ANY,)),
            p('''{n}The flask stays with the Commander, corked, its contents undisturbed. Once a month she asks the Commander to hold it toward the lamp. She lays two fingers against the glass long enough to read its temperature, then withdraws them and writes down the figure. The cork is never touched.{/n}'''),
        )),
    nar("across", '''{n}She comes across the hall with a lamp and leaves it on the washstand.{/n} "The scar. Show me." {n}The Commander loosens the shirt. She pushes it from both shoulders and lays her palm over the closed scar.{/n} "You were dead. I could do nothing. I did not care for it." {n}Her mouth follows her hand; then she catches the Commander's face and kisses hard enough to stop the next breath. Her dress falls beside the bed. She pulls the Commander down with her, bare skin hot against hers, and catches the wrist bearing the flask against the pillow.{/n} "Stay here." {n}She draws the Commander close, her hair falling over both faces.{/n}''',
        c("[Let her.]", "morning"),
        c("[Catch her hand.] \"Not like this. Not as a measurement.\"", "stopped")),
    nar("morning", '''{n}At dawn she is across the hall, writing. When the Commander passes the door, she catches the wrist bearing the flask, feels the warmth beneath it and lets go.{/n} "Still here. I would like you to remain so." {n}She leaves the door open.{/n}'''),
    nar("stopped", '''{n}She went very still. Then she sat back on her heels, and took her hand away, and looked at it.{/n}
{n}"It was not a measurement," she said. "That is what I cannot forgive you for making me say." She took the lamp and went back across the hall, and the next evening she knocked, which she had never done, and waited to be let in.{/n}'''),
    nar("stands", '''{n}The report on the wound was long and precise and entirely about the wound. She sent a copy to the Commander's door, bound, with an invoice for the binding.{/n}''')],
    requires=("trickster.ever", BURNED, STRUCK, "trickster.commander_back"), forbids=(CLOSED, DIED, "iomedae.appointment_kept"), sequence=False)


# --- The other outcomes of the wager (ordinary epilogue pages) ---------------------------------------------------------

page("areelu.trickster.finale.stake_only", "Exactly as struck", [
    nar("end", '''{n}The wager was settled exactly as it had been struck, and not one word more.{/n}''',
        paragraphs=(
            p('''{n}Areelu died at Threshold. The Commander had asked for the stake and nothing more. She did not return.{/n}''', requires=(DIED,)),
            p('''{n}She lived. She paid what was left of her the only way it could be paid: a century of notes, delivered to the Commander's door in a cart, with an invoice. She had never been interested in praise or reproach, and she was not interested in the Commander's company either. She said so, in writing, and was never seen in Drezen again.{/n}''', forbids=(DIED,)),
            p("{n}The Commander had asked for the stake and nothing more, and had got exactly that. Years later a scholar "
              "asked the Commander what the Architect had been like, close to. The Commander thought about it for a long "
              "time and said: punctual.{/n}"),
            p("{n}The cart of notes the Commander never opened. It sat in a locked cellar for the rest of the Commander's life "
              "and was burned, unread, at the Commander's own instruction, afterwards: the one stake in the whole wager "
              "that nobody collected.{/n}", forbids=(DIED,)),
        ))],
    requires=("trickster.ever", STAKE_ONLY), forbids=(CLOSED,), sequence=False)

page("areelu.trickster.finale.report_stands", "The report stands", [
    nar("end", '''{n}Areelu held the wager to its terms, as she had said she would. What the report says of her after Threshold, it says plainly, and the Commander let it stand.{/n}''',
        paragraphs=(
            p('''{n}She died at Threshold.{/n}''', requires=(DIED,)),
            p('''{n}She lived, and she paid her stake to the last page, in front of the Commander, in a single night. Then she left. The bet, she wrote, had been won fairly; nothing had ever been said about staying.{/n}''',
              forbids=(DIED,)),
            p("{n}At the very edge of the Threshold she had turned back, once.{/n} \"You asked me to raise the stakes,\" {n}she "
              "said,{/n} \"with a sword at my throat. Ask me again some year when you are not holding one, and I will tell "
              "you no again, and we will both know I considered it.\" {n}The Commander never asked.{/n}"),
        ))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), sequence=False)

# AUTHORED: the intimate report entry follows shared ascent, leaving TE_Final's crystal sequence uninterrupted (K28).
page("areelu.trickster.finale.ascended", "Unsettled", [
    nar("end", '''{n}They had ascended together. In the first entry of her new report, Areelu wrote both names. That night she closed the notebook and looked at the Commander.{/n} "I have recorded what the crystals did. Now I want you."
{n}If there is a last page to that report, nobody below has read it. The Commander's name is on it, and hers, and a single word between them in her small neat hand, and the word is not "neither". It is "both".{/n}''',
        c("[Leave her to her report.]"),
        c("[Stay with her.]", "asc_night")),
    nar("asc_night", '{n}She takes your hand from the notebook and places it at the fastening of her gown. When you undo it, she steps close enough for the loosened cloth to brush your skin.{/n} "Look at me." {n}Her mouth catches yours. She draws your shirt from your shoulders, lets the gown fall, and holds you against her with a palm at the back of your neck. At the bed she kisses your bare chest, then your mouth again.{/n} "I did not come this far to watch you from across a room." {n}She pulls you down after her.{/n}',
        c("[Go with her.]", "asc_morning"),
        c('[Draw back.] "Stay with me. Let the rest wait."', "asc_stopped")),
    nar("asc_morning", '{n}In the morning her gown lies over your discarded shirt. She reaches for the notebook, then leaves it closed and draws your hand back beneath the blanket.{/n} "Stay. I have work waiting. I prefer this for the moment."\n{n}The wager remains in her report, beside both names. She has not forgotten it.{/n}'),
    nar("asc_stopped", '{n}She settles beside you and pulls the blanket over both of you.{/n} "Very well. Stay here." {n}In the morning she retrieves the notebook, then moves the lamp so you can read the new heading beside her.{/n} "Both names. Do not touch the rest."\n{n}The wager remains in her report, beside both names. She has not forgotten it.{/n}')],
    requires=("trickster.ever", STRUCK, ASCENDED), forbids=ROMANCE_FORBIDS, any_groups=(COMMITTED_ANY,),
    overrides=ROMANCE_OVERRIDES, sequence=False)


# Ledger row 16, R6 (iomedae_trickster): Iomedae's bridge world. The Commander went into the Wound and the lock took the key,
# but the key walked back out across her banner before it burned: the prior-lien page is gated off there, and this sibling
# page settles the wager in her voice. (Iomedae is not named: Areelu would not give her the satisfaction.)
page("areelu.trickster.finale.not_burned", "Not burned", [
    nar("end", '''{n}"You did not burn." Areelu wrote it at the top of a clean page, and did not underline it, because she was not yet certain it was true.{/n}
{n}"The lock took the key, exactly as designed. I measured the seam afterwards: it holds, and what holds it is everything I put into the subject, and the Abyss with it. That part burned. The rest of the subject came back over the edge on something I did not build, and I will not name its maker in my own report."{/n}
{n}"The wager is therefore unsettled. Neither of us burned. I dislike an experiment with an outside variable. I will be studying this one for the rest of my life, and I intend to be difficult about it."{/n}''',
        # Sol PP8 r1 (BEL cap): a committed Areelu's night in this world. [0] is the original page end, kept for the others.
        c("Continue", forbids=(COMMITTED, LATE_COMMITTED)),
        c("Continue", "nb_across", requires=(COMMITTED,), forbids=(DECLINED, STAKE_ONLY)),
        c("Continue", "nb_across", requires=(LATE_COMMITTED,), forbids=(COMMITTED, DECLINED, STAKE_ONLY)),
        c("Continue", requires=(DECLINED,)),
        c("Continue", requires=(STAKE_ONLY,), forbids=(DECLINED,))),
    nar("nb_across", '''{n}She comes to the Commander's rooms with a lamp and a notebook. Both go on the floor, the notebook closed.{/n} "Where the wound was. Show me." {n}She takes the loosened shirt from the Commander's shoulders and presses her palm to the pale skin beneath it.{/n} "Something brought you back that I did not build. I intend to find out what it left." {n}She kisses the place her hand covered, then the Commander's mouth. Her dress loosens under the Commander's hands. She lets it fall, pushes the Commander onto the bed and climbs after, a knee on either side. Her teeth graze the unmarked chest; she raises her head to meet the Commander's eyes.{/n} "Here. I want you here." {n}She pulls the Commander against her.{/n}''',
        c("[Let her.]", "nb_morning"),
        c('[Catch her wrist.] "Not as an experiment."', "nb_stopped")),
    nar("nb_morning", '''{n}In the morning the notebook is still closed on the floor. She picks it up, then stops at the door.{/n} "I will come back tonight. If that patch of skin changes before then, send for me." {n}She looks once toward the bed before taking the lamp across the hall.{/n}'''),
    nar("nb_stopped", '''{n}She went still, and took her hand away, and looked at it as though it belonged to a colleague who had disappointed her.{/n}
{n}"It was not an experiment," she said. "I would not have said so if you had not made me." The next evening she knocked, which she had never done, and waited to be let in.{/n}''')],
    requires=("trickster.ever", "iomedae.appointment_kept", STRUCK), forbids=(CLOSED, DIED), sequence=False)


# --- Path fit (13 directive update 2026-09-29 / ROUTE-BRIEF-R §2; recorded in PP8). --------------------------------------
# Every scene here is the wager (the device) or reads a flag only it sets, so all are T. 14-PATH-FIT §3 fits her romance
# only on Dragon (the canon redemption, Ending_AreeluRedeemed) and maybe Demon, Legend and Lich; on most paths she dies at
# Threshold. No v2 candidate in this module: a Dragon-path romance needs its own redemption premise (v2).
# Pacing (PP8): Ch2 3 in person, the Long Con's Areelu crossing (longcon.py: areelu.early.two_masks on the fake Yaniel's
# list; courtesy_freed / courtesy_refused on her unmasked list), read back at Ch5 in rivalry.lens reply [1]. Ch3 none: she
# is absent (her lab projection is Ch5). Ch4 1, Ch5 4 + 2, Ch6 10.
PATH_FIT = {s["Id"]: "T" for s in SCENES}
PATH_FIT_V2 = {}


def integrate(payload):
    """Native keys this route reads that the world bindings do not carry yet, and its Derived survival key."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting Areelu derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    for key, guid in SELECTED_ANSWERS.items():
        have = payload.setdefault("SelectedAnswers", {}).get(key)
        if have is not None and have != guid:
            raise ValueError("Conflicting Areelu binding: " + key)
        payload["SelectedAnswers"][key] = guid
    for key, guid in INVENTORY.items():
        have = payload.setdefault("InventoryItems", {}).get(key)
        if have is not None and have != guid:
            raise ValueError("Conflicting Areelu item binding: " + key)
        payload["InventoryItems"][key] = guid
    # Sol quality pass (COX): Seelah's objection is outside the ledger's reactor allocation for Areelu (exactly Nenio and
    # Ember). Retired by gating, never deleted.
    for s in payload["Scenes"]:
        if s["Id"] in RETIRED:
            s["Forbids"].append("trickster.ever")
