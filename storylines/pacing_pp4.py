"""Pacing pass PP4 (Writer/handoffs/13-PACING-PASS.md sections 4 and 7; 15b-EARLY-THREADS.md T1): Nocticula, Kiana, Jerribeth.

Three new scenes, each a single native moment with a real choice for her, plus the later scene in her merged route that reads
it (appended here; choices are append-only, so every existing index stays a save reference):

  nocticula.early.gresilla_credit  T1, "a borrowed credit" (15b, user-approved). Chapter 3, Midnight Fane, Gresilla's hub
                       NocticulaPriestess AnswersList_0005 8a69c5ac, once she has told the Commander about Darrazand's blockade
                       (SeenCues Cue_0014 0fd2a480) and only without her [Attack] (SelectedAnswers Answer_0003 23d2a8e4).
                       ReturnToList: Cue_0037 973acfd1 would replay "...you won't let that happen, I know" right after the
                       Commander has agreed to help. Requires the live Trickster (the path is chosen at the end of Ch2).
                       Owlcat's own cut line (enGB 25537bfd, used by no blueprint) has her ask for exactly this: "Let my
                       mistress hear the rumor that I used the Commander for my own ends."
                       Delivery: the story leaves with the way through the rift, after Darrazand falls. Read from the report to
                       the Queen (StartedDialogs MidnightFaneFinal_dialog 878ad160, whose FinishActions complete obj6
                       ReportGalfrey 48499b2b and FourthPart 24417ce4;
                       it starts only once Darrazand is dead), not the QuestObjectives reader 15b proposed: an
                       objective reader did not resolve at load for Horzalah (storylines/horzalah_trickster.py:138, commit 85d0bfd), so a
                       dialog reader is used.
                       Payoff: request [2]/[3] in noct.acq.audience_* (her Ch5 "What are you actually offering?"); the
                       pledge it may cost is called in at noct.acq.her_hand/terms, and the dupe's standing likewise; a
                       Secrets page in the Ledger holds whether or not the request is ever made.
  nocticula.ch4.hoard  Chapter 4 in person (13 section 4: her palace, before the Council politics), N-all. Nocticula_main
                       AnswersList_0019 09a3f210 (the "about you" questions), after she has told how she killed Nahyndri for
                       trying to add her to his hoard (SeenCues Cue_0206 018edb7d "No one has tried to make me their slave").
                       ReturnToList: every return on that list replays one of her answers (Cue_0017 "Recounting my whole
                       story...", Cue_0049, Cue_0050). Payoff: request [4]-[6] in the same Ch5 audience.
  kiana.wedding.cast   Chapter 3, Seelah's Q2 wedding (the wedding window), N-all. KyanaWelcome AnswersList_0005 ad91a2ae
                       (her greeting, the only list of that dialog), and only before the ceremony opens (SeenCues
                       WeddingUnexpected Cue_0001 7b2d088e). ReturnToList: Cue_0004 466c4a89 would replay her welcome speech.
                       Payoff: kiana.trickster.ward_rounds/start [4]-[6].

Jerribeth: no new beat. Her Chapter 3 (6 in person) and Chapter 4 (1 in person, Alushinyrra) already carry her (13 section 7
"verify"). Recorded in her 06 row.

No beat delays a native Chapter 3 romance key: all three are inline (no delay, no rest, no native time), set no native key, and
ride lists that belong to Gresilla's, Nocticula's and Kiana's own dialogs only (PacingPP4Tests).
"""
from story_format import c, n, scene

SCENES = []

GRESILLA_LIST = "8a69c5acce98db74d87ff06fdcf1b975"   # c3/MidnightFane/NocticulaPriestess/AnswersList_0005
NOCTICULA_LIST = "09a3f2100af13ae429e1dedf27e32a80"  # c4/Nocticula_main/AnswersList_0019 ("I want to know more about you.")
KIANA_LIST = "ad91a2aed6132554782ca2ad10a1ee2a"      # Seelah/Q2_TillDeathDoUsPart/KyanaWelcome/AnswersList_0005

# Native keys read (bound in trickster_world.BINDINGS).
DARRAZAND_HEARD = "gresilla.darrazand_heard"          # SeenCues NocticulaPriestess/Cue_0014
GRESILLA_ATTACKED = "gresilla.attacked"               # SelectedAnswers NocticulaPriestess/Answer_0003 [Attack]
FANE_DONE = "fane.darrazand_defeated"                 # StartedDialogs MidnightFaneFinal_dialog (the report to the Queen)
NAHYNDRI = "noct.ch4.nahyndri_told"                   # SeenCues Nocticula_main/Cue_0206
CEREMONY = "kiana.ceremony_begun"                     # SeenCues WeddingUnexpected/Cue_0001

# T1 flags (15b, exact strings).
CREDIT = "nocticula.early.gresilla_credit"
DELIVERED = "nocticula.early.gresilla_delivered"      # Derived: CREDIT + FANE_DONE
CREDITED = "nocticula.gresilla_credited"              # request [2]: the Commander keeps the dupe's standing
EXPOSED = "nocticula.gresilla_exposed"                # author: Gresilla sold out, a pledge given
AUTHOR = "noct.acq.author_offer"
COLLATERAL = "noct.acq.collateral_given"
PLEDGE_NAMES, PLEDGE_FEAR, PLEDGE_CON = "noct.acq.pledge_names", "noct.acq.pledge_fear", "noct.acq.pledge_con"
# The call-in (15b residual: a named later reader per pledge and for the retained standing), at her_hand/terms.
PLEDGE_PAID, PLEDGE_REFUSED = "noct.acq.pledge_paid", "noct.acq.pledge_refused"
HARP_SIGNED, HARP_UNSIGNED = "noct.acq.harp_signed", "noct.acq.harp_unsigned"
SECRET = "trickster.secret.gresilla_harp"             # the Ledger's Secrets page (08 section 2.1)

HOARD = "nocticula.ch4.hoard"
HOARD_OUT = tuple(HOARD + "." + v for v in ("appraised", "bitten", "spent", "declined"))
HOARD_RECALLED = "noct.acq.hoard_recalled"
CAST = "kiana.wedding.cast"
CAST_OUT = tuple(CAST + "." + v for v in ("captive", "hunter", "guest", "declined"))

BEATS = {CREDIT: (CREDIT, CREDIT + ".declined"), HOARD: HOARD_OUT, CAST: CAST_OUT}

DERIVED = {
    DELIVERED: [[CREDIT, FANE_DONE]],
    SECRET: [[DELIVERED]],
}

# Path fit (ROUTE-BRIEF-R section 2): T1 is T (15b: it requires the live Trickster); the other two are N-all.
PATH_FIT = {CREDIT: "T", HOARD: "N-all", CAST: "N-all"}


def seen(beat):
    return beat + ".seen"


# --- T1 · Nocticula <- Gresilla: "Tell her I used you" (Chapter 3, Midnight Fane) ----------------------------------------

S = seen(CREDIT)
SCENES.append(scene(CREDIT, "A borrowed credit", "Gresilla", 3,
    '"You want her praise. I can\'t give you a door out. I can give you a story to walk through it."', [
    n("ask", "conversant", '''{n}Gresilla leaves the tassel of her pillow alone and leans toward you. The languor is still there; under it, something has gone very attentive.{/n}
"A story." {n}She tastes the word.{/n} "Commander, you do know how to make a girl lean forward. Tell me this story. Slowly."''',
      c('"When Darrazand falls, it\'ll be on your orders, as far as anyone in the Abyss hears. Tell your sisters. Let it reach her: '
        'Gresilla played the Knight Commander like a harp."', "sent", flags=(CREDIT, S), alignment=("Chaotic", 1)),
      c('"Forget I said it."', abort=True, flags=(CREDIT + ".declined", S))),
    n("sent", "conversant", '''{n}Gresilla turns her head and says something low in Abyssal to the dark at the back of her chamber. One voice answers, young and eager.{/n}
"My littlest sister will sit by the rift. When Darrazand falls and the way opens, she flies first." {n}Her smile comes back, slow and very satisfied.{/n} "Stories travel faster than priestesses."''',
      c("Continue", "taken")),
    n("taken", "conversant", '''{n}She tilts her head and takes the gift apart, piece by piece, the way a courtesan takes apart a present to see what it cost.{/n}
"And what do you get, Commander? A demon's gratitude?" {n}A slow smile.{/n} "No... you get to be the fool in her court. The crusader a succubus led by the nose. How very *generous*."''',
      c('"The fool gets into rooms the hero never does."')),
], requires=("trickster", DARRAZAND_HEARD), forbids=(CREDIT, S, CREDIT + ".declined", GRESILLA_ATTACKED), last=3, optional=True,
   Relationship="nocticula", Chapters=[3], AnswerLists=[GRESILLA_LIST], ReturnToList=True,
   ReturnText="{n}Gresilla's eyes are bright. Somewhere in the dark behind her, one pair of wings settles to wait.{/n}"))


# --- Nocticula, Chapter 4 in person: the hoard (her palace, after the Nahyndri story) -------------------------------------

S = seen(HOARD)
SCENES.append(scene(HOARD, "A jewel for a hoard", "Nocticula", 4,
    '"Nahyndri wanted you for his hoard. Who\'s in yours?"', [
    n("start", "conversant", '''{n}For a moment the Lady in Shadow simply looks at you, the way a jeweller looks at a stone somebody has set down on her counter without asking. Then she laughs, low and pleased with you, which is not the same as being pleased.{/n}
"Everyone, crusader. Every island. Every dancer in my city, every knife in my city's guild, every fool who has knelt on that floor and called it devotion. They are mine."
{n}She lets the word lie between you.{/n}
"The difference is that Nahyndri mistook me for something he could keep. Everything I keep knows exactly whose it is." {n}Her eyes travel over you, unhurried, from your boots to your throat.{/n} "And now you are wondering whether I am appraising you for a shelf."''',
      c('"Are you?"', "appraised", flags=(S,)),
      c('"I\'d make a poor ornament. I bite."', "bitten", flags=(S,)),
      c('"I was wondering whom you\'d spend first, to keep Hepzamirah\'s war out of your palace."', "spent", flags=(S,)),
      c("[Let the question go.]", abort=True, flags=(S, HOARD + ".declined")),
      portrait="Nocticula"),
    n("appraised", "conversant", '''"Of course I am. I appraise everything that walks into this room. It is the only courtesy I extend to strangers."
{n}She tilts her head and takes her time about it.{/n}
"Mortal. Rough at the edges. You smell of a war you have not yet won and a city that still thinks it owns you." {n}A smile with nothing kind in it.{/n} "Not worth the room. Not yet. Win something worth having, and you may ask me again. I may have made room."''',
      c("[Return to the audience.]", flags=(HOARD + ".appraised",)), portrait="Nocticula"),
    n("bitten", "conversant", '''{n}Something very old and very amused moves behind her face.{/n}
"Everything worth keeping bites, at first." {n}She turns the thought over like wine on the tongue.{/n} "That is what the shelf is for. Teeth only tell me that a thing has not yet learned where it sits."
"Bite, then, if it comforts you. Only remember whose palace you are biting in."''',
      c('"I\'ll sit where I like."', flags=(HOARD + ".bitten",)), portrait="Nocticula"),
    n("spent", "conversant", '''{n}The laughter stops. What replaces it is attention, and it is much less comfortable.{/n}
"Spend." {n}She repeats it as if you had used a word from her own language.{/n} "Whichever servant costs me least to replace. Then the next. I do not sell my things, mortal. I spend them, in the order that buys the most, and I never once call it a sacrifice."
{n}She looks at you differently, the way one predator notes another at the edge of the same water.{/n} "If you wish to be useful to me, ask what I intend to buy."''',
      c("[Return to the audience.]", flags=(HOARD + ".spent",)), portrait="Nocticula"),
], requires=(NAHYNDRI,), forbids=(S, *HOARD_OUT), last=4, optional=True, Relationship="nocticula", Chapters=[4],
   AnswerLists=[NOCTICULA_LIST], ReturnToList=True,
   ReturnText="{n}Nocticula settles back among her cushions, and the audience is hers again.{/n}"))


# --- Kiana, Chapter 3: the vampire princess casts the Knight Commander (her wedding, before the ceremony) ----------------

S = seen(CAST)
SCENES.append(scene(CAST, "The princess's court", "Kiana", 3,
    '"Every vampire court needs a villain. Can you use a crusader?"', [
    n("start", "conversant", '''{n}Kiana's eyes go wide with delight and then narrow, theatrically, the way a princess narrows them at a peasant who has spoken out of turn.{/n}
"A crusader? In *my* castle? Oh, that's dreadful. That's perfect." {n}She takes your arm before you can think better of it and steers you toward the candlelit tables, where her friends in their black lace look up from the red wine.{/n}
"Now. You may be my prisoner: the great Knight Commander, taken alive and brought before the court in chains. Or you may be the hunter, come to slay the princess on her wedding day. Choose. The hunter dies horribly, I warn you. I've been practising."''',
      c('"Your prisoner, Highness. I surrender."', "captive", flags=(S,)),
      c('"The hunter. Somebody fetch me a stake."', "hunter", flags=(S,)),
      c('"Neither. I came as a guest, and a guest drinks the wine."', "guest", flags=(S,)),
      c("[Let her get back to her guests.]", abort=True, flags=(S, CAST + ".declined")),
      portrait="Kiana"),
    n("captive", "conversant", '''{n}She claps her hands. Somebody produces a velvet ribbon in place of chains, and Kiana knots it round your wrists with a competence that is not theatrical in the least.{/n}
"Behold!" {n}Her friends shriek and applaud. Somebody throws a rose.{/n} "The Knight Commander of the Crusade, captured by the court of Ustalav! What shall we do with such a prize? Drink to it, I think."
{n}She tips a cup of "blood" to your lips and, under the applause, says in her own voice:{/n} "Elan's knights have been glaring at our side all evening as if we'd started a riot. Now they'll have to come over here and rescue you. Thank you. Truly."
{n}Across the way, a Houndheart in his best surcoat lifts a cake knife and points it at your ribbon.{/n}''',
      c("[Bear your captivity with dignity.]", flags=(CAST + ".captive",)), portrait="Kiana"),
    n("hunter", "conversant", '''"A stake!" {n}Kiana cries, and somebody hands you a breadstick. She sweeps up her skirts, backs onto the nearest bench and bares a set of wax fangs she has produced from nowhere.{/n} "Strike, hunter, if you dare!"
{n}You strike. The breadstick breaks across her bodice. Kiana dies at enormous length: a gasp, a stagger, a hand to the brow, and a long swoon into the arms of two friends who have plainly done this before.{/n}
{n}From the floor, still dead, she opens one eye.{/n} "Half the guests think a vampire wedding is in poor taste, with demons at Drezen's gates. That's exactly why we're having one."''',
      c("[Help the corpse up.]", flags=(CAST + ".hunter",)), portrait="Kiana"),
    n("guest", "conversant", '''{n}Kiana gives you a look of profound and entirely theatrical disappointment, then puts a cup of the red wine into your hand anyway.{/n}
"A guest. How terribly sensible." {n}She touches her cup to yours.{/n} "Then drink to Elan and me, guest, and stop frowning. Half of Drezen is frowning at us already, and we'll have gloomy faces enough tomorrow. Tonight it's a wedding."''',
      c("[Drink to the couple.]", flags=(CAST + ".guest",)), portrait="Kiana"),
], forbids=(S, *CAST_OUT, CEREMONY), last=3, optional=True, Relationship="kiana", Chapters=[3],
   AnswerLists=[KIANA_LIST], ReturnToList=True,
   ReturnText="{n}Kiana sweeps back to the head of her table, every inch the vampire princess again.{/n}"))


# --- Consequences (appended to the reading scenes; new choices go last, new nodes after the existing ones) ----------------

def _noct(id, text, *choices):
    return n(id, "Nocticula", text, *choices, portrait="Nocticula")


def _kiana(id, text, *choices):
    return n(id, "Kiana", text, *choices, portrait="Kiana")


# T1 payoff and the Chapter 4 recall, at her Chapter 5 "What are you actually offering?" (request; [0] and [1] keep their
# places). author's pledges: [0] names, [1] fear, then [2] the Long Con's truth, appended only when a registered scene can set
# longcon.begun (doc 15's entry, PP8). 15b orders the con pledge first; it goes last here so the other indices never move.
REQUEST_CHOICES = [
    c('"You\'ve heard Gresilla\'s harp. The harp is asking."', "harp", requires=(DELIVERED,), forbids=(EXPOSED, CREDITED),
      flags=(CREDITED,)),
    c('"Gresilla didn\'t play me. I wrote her song. I can write you better ones."', "author", requires=(DELIVERED,),
      forbids=(CREDITED, EXPOSED)),
    c('"In Alushinyrra you told me to win something worth having and ask again. I\'m asking."', "hoard_appraised",
      requires=(HOARD + ".appraised",), forbids=(HOARD_RECALLED,), flags=(HOARD_RECALLED,)),
    c('"In Alushinyrra I told you I bite. I\'m not offering to sit on your shelf."', "hoard_bitten",
      requires=(HOARD + ".bitten",), forbids=(HOARD_RECALLED,), flags=(HOARD_RECALLED,)),
    c('"In Alushinyrra you told me you spend your things. I\'m offering to be worth spending."', "hoard_spent",
      requires=(HOARD + ".spent",), forbids=(HOARD_RECALLED,), flags=(HOARD_RECALLED,)),
]
PLEDGED = (EXPOSED, AUTHOR, COLLATERAL)
REQUEST_NODES = [
    _noct("harp", '''"Gresilla's instrument, come to play for itself."
{n}Her smile is patient and faintly insulting.{/n}
"My sisters are still humming you. A crusader who walked into my priestess's rooms and walked out with every string tuned to her hand. Do try to sound less like a harp while you bargain."''',
          c('"Then hear the account."', "price")),
    _noct("author", '''"...*Yours.*"
{n}Her laugh is low and entirely pleased, and then it stops.{/n}
"Then somebody will be corrected, if she is still breathing to be corrected. And you are a creature who sells its intermediaries." {n}She holds out her hand, palm up.{/n} "I will want something of yours in pledge, then, before I hear another word from you. Something you would not like my sisters to hum."''',
          c('[Tell her whom you trust most in Drezen.]', "price", flags=(*PLEDGED, PLEDGE_NAMES)),
          c('[Tell her what you are afraid of.]', "price", flags=(*PLEDGED, PLEDGE_FEAR))),
    _noct("hoard_appraised", '''"Did I say that." {n}It is not a question.{/n} "So I did. And what have you won? A closet that is not yours, a seat at a council that despises you, and a way into my rooms that my brother lent you for his own amusement."
{n}She weighs it.{/n} "Still not worth the room. A better story than most, though. You may go on."''',
          c('"Then hear the account."', "price")),
    _noct("hoard_bitten", '''"No. You are offering to bite somebody else on my behalf, and calling it independence."
{n}She sounds almost fond of the distinction.{/n} "I remember. You were rude in my own audience hall, and I let you leave with your tongue. I do that rarely enough that I keep a list. Go on, then. Bite."''',
          c('"Then hear the account."', "price")),
    _noct("hoard_spent", '''{n}For a heartbeat the Lady in Shadow looks at you with the full weight of her attention, and the lamps seem to lean toward her to watch.{/n}
"Worth spending." {n}She says it softly.{/n} "You remembered. Most mortals remember what I wore." {n}Then the smile, very slow.{/n} "Very well. Show me what you would buy, if I spent you."''',
          c('"Then hear the account."', "price")),
]
CON_PLEDGE = c('[Tell her the Goat\'s-man legend is a lie you built.]', "price", requires=("longcon.begun",),
               flags=(*PLEDGED, PLEDGE_CON))

# The call-in, at her_hand/terms: the original answer [0] is gated off for a pledged or credited Commander, and appended twins
# lead to the demand. Each answer still ends the letter with her_hand_done and correspondence_trial (the route's own flags).
TRIAL = ("noct.acq.her_hand_done", "noct.acq.correspondence_trial")
TERMS_CHOICES = [
    c("Keep the trial correspondence. Prepare an actual concession before asking for more.", "call_names",
      requires=(PLEDGE_NAMES,)),
    c("Keep the trial correspondence. Prepare an actual concession before asking for more.", "call_fear",
      requires=(PLEDGE_FEAR,)),
    c("Keep the trial correspondence. Prepare an actual concession before asking for more.", "call_harp",
      requires=(CREDITED,)),
]
TERMS_NODES = [
    _noct("call_names", '''{n}The wax has nearly cooled when the completed stroke turns again. She has decided to have the last word after all.{/n}
"One more thing. You told me whom you trust most in Drezen. Write that name under this letter, in your own hand, beside your own."
{n}You ask why.{/n}
"So that when your proposal fails me, I shall not have to go looking for whom to visit. I dislike looking. I am told it is undignified."''',
          c("[Write the name.]", flags=(*TRIAL, PLEDGE_PAID)),
          c('"You have the name. You do not get my hand on it as well."', "refused")),
    _noct("call_fear", '''{n}The wax has nearly cooled when the completed stroke turns again. She has decided to have the last word after all.{/n}
"One more thing. You told me what you are afraid of. Write it under this letter, in your own hand. Not prettily."
{n}You remind her that she already knows it.{/n}
"I know what you said. I want it written where your officers could read it. I may wish to show them one day what frightens their Commander."''',
          c("[Write it down, plainly.]", flags=(*TRIAL, PLEDGE_PAID)),
          c('"You have what I said. That will have to be enough."', "refused")),
    _noct("call_harp", '''{n}The wax has nearly cooled when the completed stroke turns again. When she speaks there is laughter under it, and none of it is yours.{/n}
"One more thing. My sisters have a song about you. Gresilla's harp. They sing it at the court in the evenings, and they would be so pleased if the harp would sign its letters to me that way."
{n}You ask what happens if you sign your own name.{/n}
"Then the song will need a new verse, and I shall write it myself. I shall decide which of your failures they sing about."''',
          c('[Sign it "Gresilla\'s harp".]', flags=(*TRIAL, HARP_SIGNED)),
          c("[Sign your own name.]", "unsigned")),
    _noct("refused", '''{n}For a moment nothing at all comes from the wax.{/n}
"How disappointing. And how interesting." {n}The stroke settles.{/n} "Keep your hand, then. I still hold what you gave me in my rooms. I shall decide what it is worth to me on a day you will not enjoy."''',
          c("[Fold the letter.]", flags=(*TRIAL, PLEDGE_REFUSED))),
    _noct("unsigned", '''"Your own name." {n}She sounds delighted.{/n} "Gresilla's harp refuses to be played. My sisters will adore that verse. You will not."''',
          c("[Fold the letter.]", flags=(*TRIAL, HARP_UNSIGNED))),
]

# Kiana's wedding, recalled on her ward rounds (kiana.trickster.ward_rounds/start; [0]-[3] keep their places).
ROUNDS_CHOICES = [
    c('"Your prisoner reports for rounds, Highness."', "court_captive", requires=(CAST + ".captive",)),
    c('"Shall I fetch a breadstick, or are you staying dead today?"', "court_hunter", requires=(CAST + ".hunter",)),
    c('"A guest, reporting. Is there wine on this ward?"', "court_guest", requires=(CAST + ".guest",)),
]
ROUNDS_NODES = [
    _kiana("court_captive", '''{n}Kiana stops with the list half collected. For a moment her face does something complicated.{/n}
"The ribbon." {n}She laughs, a little too loudly.{/n} "Elan's knights did come over to rescue you, you know. Three of them, terribly solemn, with a cake knife for a sword. I laughed until I had to sit down. That was the last good hour, before the cup came round."
{n}She presses half the list against your chest.{/n} "Left side, prisoner. You still owe the court an escape."''',
           c("[Do the left side.]", "rounds")),
    _kiana("court_hunter", '''"Staying alive today, thank you. The reviews of my last death were very good, and I don't want to spoil the run."
{n}She says it lightly. Her hand has gone to her bodice anyway, to the place where a breadstick broke, as if the crumbs might still be there.{/n}
"I died beautifully at my own wedding, Commander. Then the cup came round and spoiled the encore." {n}She shoves half the list at you.{/n} "Left side. Make them laugh. I'll keep the swoons."''',
           c("[Do the left side.]", "rounds")),
    _kiana("court_guest", '''"Water. This is a temple." {n}She narrows her eyes at you.{/n} "You drank to Elan and me like a proper guest. Very sensible. Then the cup came round, and I've been wondering ever since whether sensible would have helped."
{n}She lets that sit for exactly one breath and no longer.{/n} "So now I tell jokes on a ward instead. Left side, guest. If anybody asks, the wine was excellent."''',
           c("[Do the left side.]", "rounds")),
]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _append(scene_, node_id, choices, nodes):
    target = _node(scene_, node_id)
    have = {x["Id"] for x in scene_["Nodes"]}
    for node in nodes:
        if node["Id"] in have:
            raise ValueError("pacing_pp4: node %s already in %s" % (node["Id"], scene_["Id"]))
    target["Choices"].extend(dict(choice, Requires=list(choice["Requires"]), Forbids=list(choice["Forbids"]),
                                  Set=list(choice["Set"])) for choice in choices)
    scene_["Nodes"].extend({**node, "Choices": [dict(x) for x in node["Choices"]]} for node in nodes)


def integrate(payload):
    """Append the consequence choices and nodes to their reading scenes (save-safe: new choices go last), and register the
    keys and the Ledger page."""
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    longcon = any("longcon.begun" in ch["Set"] for s in payload["Scenes"] for nd in s["Nodes"] for ch in nd["Choices"])
    for id in ("noct.acq.audience_missed", "noct.acq.audience_rejected", "noct.acq.audience_patronage"):
        _append(scenes[id], "request", REQUEST_CHOICES, REQUEST_NODES)
        if longcon:
            _node(scenes[id], "author")["Choices"].append(dict(CON_PLEDGE))
    hand = scenes["noct.acq.her_hand"]
    terms = _node(hand, "terms")
    if len(terms["Choices"]) != 1:
        raise ValueError("pacing_pp4: noct.acq.her_hand/terms changed shape")
    for flag in (PLEDGE_NAMES, PLEDGE_FEAR, CREDITED):
        if flag not in terms["Choices"][0]["Forbids"]:
            terms["Choices"][0]["Forbids"].append(flag)
    _append(hand, "terms", TERMS_CHOICES, TERMS_NODES)
    if longcon:
        # The con pledge is called in like the names: in her hand, under the letter.
        terms["Choices"][0]["Forbids"].append(PLEDGE_CON)
        terms["Choices"].append(c(TERMS_CHOICES[0]["Text"], "call_con", requires=(PLEDGE_CON,)))
        hand["Nodes"].append(_noct("call_con", '''{n}The wax has nearly cooled when the completed stroke turns again. She has decided to have the last word after all.{/n}
"One more thing. You told me your Goat's-man is a lie you built. Write the truth of it under this letter, in your own hand. I may want the right people to recognise the hand."
{n}You tell her that it would end you.{/n}
"Only if I show it to anyone. Write."''',
            c("[Write the truth of it.]", flags=(*TRIAL, PLEDGE_PAID)),
            c('"You have what I said. You do not get it in ink."', "refused")))
    _append(scenes["kiana.trickster.ward_rounds"], "start", ROUNDS_CHOICES, ROUNDS_NODES)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("pacing_pp4: conflicting Derived " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    # The Ledger page reads the Derived secret; its delivery leg is not read by any scene, so it is bound here.
    payload.setdefault("StartedDialogs", {}).setdefault(FANE_DONE, "878ad1608527aec41b3a87bfe8afdbcd")


def _ledger():
    from storylines import lastcall_ledger as ledger
    ledger.early(dict(
        Id="early.gresilla_harp", Section="Secrets", Portrait="Nocticula", Title="Gresilla's harp",
        Text="{n}In the Midnight Fane you gave Nocticula's priestess a story to carry home: that Darrazand died on her orders, "
             "and that she had played the Knight Commander like a harp. Her littlest sister flew it through the rift.{/n}",
        Lines=[ledger._line("{n}In Nocticula's court they still hum Gresilla's harp. You're the harp.{/n}", forbids=[EXPOSED]),
               ledger._line("{n}You told Nocticula whose song it was, and paid for the claim with a secret. Somebody is to be corrected.{/n}", requires=[EXPOSED]),
               ledger._line("{n}Nocticula knows your legend is a lie. One word from her and the Abyss knows it too.{/n}",
                            requires=[PLEDGE_CON]),
               ledger._line("{n}Nocticula knows whom you trust most in Drezen.{/n}", requires=[PLEDGE_NAMES]),
               ledger._line("{n}Nocticula knows what you're afraid of.{/n}", requires=[PLEDGE_FEAR]),
               ledger._line("{n}She called the pledge in, and you gave it to her in your own hand.{/n}", requires=[PLEDGE_PAID]),
               ledger._line("{n}She called the pledge in. You refused her your hand on it. She is still deciding what that "
                            "was worth.{/n}", requires=[PLEDGE_REFUSED]),
               ledger._line("{n}You signed a letter to her \"Gresilla's harp\".{/n}", requires=[HARP_SIGNED]),
               ledger._line("{n}You refused to sign as the harp. She promised her court a new verse about you.{/n}", requires=[HARP_UNSIGNED])],
        Requires=[SECRET], Forbids=[], AnyGroups=[], Tooltip="RRT_Secret"))


_ledger()
