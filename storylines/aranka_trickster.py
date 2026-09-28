"""Aranka on the Trickster path: the boast made true (Writer/handoffs/trickster/aranka.md; F05).

Canon: in Kenabres Aranka gives the Commander a song, "We call it 'Starward Gaze,' and it came to us from the true
servants of Desna from her domain in Elysium" (c1/KenabresBurning/DesnaTempleFinal/Cue_0020 f21279d1), and Ilkes asks the Commander to remember it
(Cue_0029 3af7086c). On the Azata island she is still rearranging it ("a new arrangement for our song"). In the Trickster's
Chapter 3 tavern the Fool King sings a ballad "off-key, but with great emotion" (FoolKing_Tavern/Cue_0001 d81c823d, Cue_0002
0b01da77) that he calls "an ancient Sarkorian ballad ... My pops used to sing when he was in his cups" (Cue_0046 a55c2fab).
Authored, and labelled so in the spec: on a non-Azata run she has no native presence after Chapter 1 (her later actor
Azata_Aranka_DesnaPriest 430cba78 has no dialog component), so her life as a Desnan singer on the crusade's roads is
invented here; the device is the Commander's own paid boast in a native Trickster venue, not Desna's luck. She keeps the
billing, tours the camps every night and chooses whether to come back, and she can refuse, or be sent to a real stage.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
UNIT = "430cba7801b149b4e8494ace6baf4f7c"           # Azata_Aranka_DesnaPriest (no dialog component; the presence copy)
DREZEN = "2570015799edf594daf2f076f2f975d8"
FYE = "0f12118177d102f428a3b30b15b132eb"            # Fye_Bartender, the presence anchor ("Fye the Tavern Keeper")
YARD_UNIT = "bd0c4fe722aeef94b8495ac284b96bc8"      # Azata_Aranka_RankupSpeaker: her Chapter 3 look, a second unit for the yard
QUARTERMASTER = "a380d926e92f70e429681eb9654478f9"  # DrezenCapital_Quartermaster (Wilcer Garms), always in the capital
KING_C3 = "1a17d8053a3be7f47a7908eb6706f2fe"        # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0009
KING_C3_RETURN = "814dd1a078a1c2849aefc85e2e15b2d2" # FoolKing_Tavern/Cue_0008 "Oh, Commander! Nice of you to stop by."
KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"        # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_RETURN = "7b050ba0745bf144e815632e39b34853" # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"     # NPC_Common/Anevia/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"     # CompanionDialogues/Woljif/AnswersList_0003
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"       # CompanionDialogues/Lann/AnswersList_0003

HUB = "aranka.presence"
YARD = "aranka.presence.yard"
FYE_GONE = "aranka.presence.failed"  # runtime: her copy is wanted but Fye is not in the capital
PRIMED = "aranka.trickster.primed"
ANSWERED = "aranka.trickster.answered"
RETURNED = "aranka.trickster.returned"
DUET = "aranka.trickster.duet_sung"
DECLINED = "aranka.trickster.declined"
NEROSYAN = "aranka.trickster.gone_to_nerosyan"
NIGHT = "aranka.trickster.night_kept"
LATE_COMMITTED = "aranka.trickster.late_committed"
STARTED = "aranka.extension_started"
CLOSED = "aranka.extension_closed"
KEPT = "aranka.extension_kept"
ROUND = "aranka.trickster.cost.round_bought"
LATE = "aranka.trickster.cost.late"
ANNOUNCED = "aranka.trickster.cost.announced"
SANG_ALONE = "aranka.trickster.cost.sang_alone"
CREDITED = "aranka.trickster.cost.credited"
VAIN = "aranka.trickster.cost.vain"
DENIED = "aranka.trickster.cost.denied"
MOCKING = "aranka.trickster.cost.mocking_verse"
FAILURE = "aranka.ran_failure"
ROMANCE = "aranka.ran_romance"
QUEST = "aranka.ran_quest_complete"
GAVE_SONG = "aranka.gave_song"
CROWNED = "fool_king.crowned"
KING_GONE = "fool_king.gone"
# Derived twin of fool_king.gone: a ForbidOverride value must be authored or Derived, never a native key. The late
# fallbacks Forbid the crown unless the King is gone, so they open only when no King is left to sing to: the King
# is gone, or the Coronation has passed and he was never crowned (then no Chapter 5 King scene exists).
NO_KING = "aranka.trickster.king_gone"
NO_KING_GATE = dict(RequiresAnyGroups=[[KING_GONE, "coronation.seen"]], ForbidOverrides={CROWNED: NO_KING})

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={FAILURE: RETURNED},
    TricksterAccess={
        "never_entered": dict(detect=[], device="aranka.trickster.verse.kings_tavern", returned=ANSWERED),
        FAILURE: dict(detect=[FAILURE], device="aranka.trickster.failure.mocking_verse", returned=RETURNED),
        "parent_done_non_azata": dict(detect=[], device="aranka.trickster.touring.boast", returned=ANSWERED),
    })
PRESENCES = {
    # A spawned copy of her Azata-island actor at the end of Fye's counter. Vellexia's copy stands on his left in
    # Chapter 5, so Aranka takes the right.
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FYE, Side="right", Distance=2.0),
              Requires=["trickster.ever", "aranka.trickster.in_drezen"], Forbids=[CLOSED], MinChapter=3, MaxChapter=5,
              AnswerLists=[], Dialog="hub",
              Greeting="{n}A woman in Desnan blue is sitting on the end of Fye's counter with a lute across her knees, "
                       "and the tavern has gone quiet to hear her tune it.{/n}"),
    # Fye leaves the capital when the tavern is lost (Fye_Bartender_NotInCapital 60d1237d hides his unit), which raises
    # aranka.presence.failed. She then sings in the quartermaster's yard instead: a copy of a different unit of hers,
    # beside Wilcer Garms, who never leaves. The same four in-person beats have yard copies (ids ending _yard).
    YARD: dict(Unit=YARD_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=QUARTERMASTER, Side="front", Distance=2.5),
               Requires=["trickster.ever", "aranka.trickster.in_drezen", FYE_GONE], Forbids=[CLOSED], MinChapter=3,
               MaxChapter=5, AnswerLists=[], Dialog="hub",
               Greeting="{n}Fye's is boarded up. A woman in Desnan blue is sitting on the tailgate of a supply wagon in the "
                        "quartermaster's yard, with a lute across her knees, and the carters have stopped unloading to "
                        "hear her tune it.{/n}"),
}


def a(id, text, *choices, **kw):
    return n(id, "Aranka", text, *choices, portrait="Aranka", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Aranka", **kw)


def king(id, text, *choices):
    """Thaberdine, speaking inline in his own tavern dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


def letter(id, title, nodes, requires, forbids, delay, chapters=(3, 5), **extra):
    SCENES.append(scene(id, title, "Aranka", min(chapters), "", nodes, requires=requires, forbids=forbids, delay=delay,
                        last=max(chapters), optional=True, Relationship="aranka", Areas=[DREZEN],
                        Chapters=list(chapters), Remote=True, **extra))


def tavern(id, title, entry, nodes, requires, forbids, chapter, hub, back, **extra):
    SCENES.append(scene(id, title, "Aranka", chapter, entry, nodes, requires=requires, forbids=forbids, delay=0,
                        last=chapter, optional=True, Relationship="aranka", AnswerLists=[hub], NativeReturnCue=back,
                        **extra))


PLACES = {
    "fye": dict(suffix="", hub=HUB, unit=UNIT, requires=(), texts={
        "@OPEN@": "{n}Fye leans across the counter as you come in.{/n} \"She's been tuning that thing for an hour and nobody's ordered a drink since. Do something.\"",
        "@SEAT@": "the end of Fye's counter",
        "@PAPER@": "the back of Fye's bill of fare",
        "@STOVE@": "Fye's stove",
        "@STAGE@": "Fye's bar",
        "@ROOM@": "She has a room above Fye's, rented by the week, with a bed too narrow for two and a window onto the latrine pits.",
        "@HOUSE@": "The whole of Fye's",
        "@BILL@": "There is a bill under the door in Fye's hand",
        "@CROWD@": "every man at the counter",
    }),
    "yard": dict(suffix="_yard", hub=YARD, unit=YARD_UNIT, requires=(FYE_GONE,), texts={
        "@OPEN@": "{n}Fye's is boarded up, so the quartermaster's yard has become a tavern without a roof. Wilcer Garms meets you at the gate.{/n} \"She's been tuning that thing for an hour and my carters haven't lifted a crate since. Do something.\"",
        "@SEAT@": "the tailgate of a supply wagon",
        "@PAPER@": "the back of a quartermaster's requisition",
        "@STOVE@": "the carters' brazier",
        "@STAGE@": "the wagon bed",
        "@ROOM@": "She has a room in a carters' lodging house by the south gate, rented by the week, with a bed too narrow for two and a window onto the mule lines.",
        "@HOUSE@": "The whole lodging house",
        "@BILL@": "There is a bill under the door in the landlady's hand",
        "@CROWD@": "every carter at the long table",
    }),
}


def fit(text, place):
    for token, value in PLACES[place]["texts"].items():
        text = text.replace(token, value)
    return text


def placed(nodes, place):
    return [dict(node, Text=fit(node["Text"], place), Choices=[dict(ch) for ch in node["Choices"]]) for node in nodes]


def counter(id, title, entry, nodes, requires, forbids, delay, **extra):
    """An in-person beat on her presence hub: at Fye's counter, and a yard copy for when Fye has left the capital."""
    for place, spec in PLACES.items():
        SCENES.append(scene(id + spec["suffix"], title, "Aranka", 3, entry, placed(nodes, place),
                            requires=(*requires, *spec["requires"]), forbids=forbids, delay=delay, last=5, optional=True,
                            Relationship="aranka", Areas=[DREZEN], Chapters=[3, 5], ContactUnit=spec["unit"],
                            InteractionHub=spec["hub"], **extra))


JOKE = '[Follow your instincts] "Aranka\'s song, second verse, the good one. I finally found a rhyme for \'Thaberdine\'. Everybody!"'
FAILURE_JOKE = '[Follow your instincts] "The verse about me, the one where I lose. Everybody! Louder on the rhyme."'
TOURING_JOKE = '[Follow your instincts] "Tonight my court poet sings in Drezen. She doesn\'t know it yet."'


# --- State never_entered: the boast made true in the Fool King's tavern (F05) --------------------------------------

def king_nodes(open_text, crowned_text, uncrowned_text=None):
    """The King's round. Chapter 5's scene requires his crown (fool_king.crowned), so it has no uncrowned page."""
    return [
        nar("start", open_text,
            c("Continue", "known", requires=(GAVE_SONG,)),
            c("Continue", "unknown", forbids=(GAVE_SONG,))),
        nar("known", '''{n}You know that tune, or something very like it. You last heard it in Kenabres, in Desna's burning temple, sung by a priestess called Aranka who had just put it into your keeping, while her friend Ilkes made you promise to remember it. Hers had words that went all the way through. His has a hole in the middle where a verse should be.{/n}''',
            c(JOKE, "round", mythic="Trickster", crusade=("Finances", -100)),
            c('"Never mind. Carry on, Your Majesty."', abort=True)),
        nar("unknown", '''{n}You know that tune, or something very like it. Half the Desnan refugees on the road out of Kenabres were humming it, and the ones who knew the words called it Starward Gaze and said a priestess named Aranka had carried it out of the burning city. Theirs went all the way through. His has a hole in the middle where a verse should be.{/n}''',
            c(JOKE, "round", mythic="Trickster", crusade=("Finances", -100)),
            c('"Never mind. Carry on, Your Majesty."', abort=True)),
        nar("round", '''{n}You climb onto the bench, pay for every mug on every table, and sing the King's ballad back at him with the words of a Desnan hymn you have no right to and a second verse of your own. The rhyme for 'Thaberdine' is 'tambourine'. It is a dreadful rhyme. The room adores it.{/n}
{n}A sapper learns your verse first, then the one-eyed carter by the door, then the girl who carries the King's mugs, who has a better voice than any of them. By the third round the whole room is singing Starward Gaze with your second verse, and the rhyme lands like a dropped tray every time. By the fifth they are correcting each other's words, and every one of them swears their grandmother sang it exactly that way.{/n}
{n}One old woman by the fire does not sing. There is a faded Desnan star stitched on her shawl, and she watches you all the way through the fifth round, and then she leaves without finishing her cup.{/n}''',
            *([c("Continue", "crowned", requires=(CROWNED,)), c("Continue", "uncrowned", forbids=(CROWNED,))]
              if uncrowned_text else [c("Continue", "crowned")])),
        king("crowned", crowned_text, c('"Once more, from the top. Everybody!"', flags=(PRIMED, ROUND))),
        *([king("uncrowned", uncrowned_text, c('"Once more, from the top. Everybody!"', flags=(PRIMED, ROUND)))]
          if uncrowned_text else []),
    ]


KING_WEEPS = '''"My pops learned this one from a Desnan girl with a voice like a lark! Or she learned it from him! One of 'em did!"'''

tavern("aranka.trickster.verse.kings_tavern", "A rhyme for Thaberdine", '"Your Majesty. That ballad of yours."', king_nodes(
    '''{n}Thaberdine is on his third chorus of the ancient Sarkorian ballad his pops used to sing, and on his fourth mug. The tune is a good one. The words are not: somewhere in the second verse he loses them every time, hums through the gap with enormous feeling, and bangs his mug on the table where the rhyme ought to be.{/n}''',
    '''{n}Thaberdine weeps openly into his crown, which is too big to be a handkerchief and is being used as one anyway.{/n}
"That's it! That's the one! That's how pops sang it!" ''' + KING_WEEPS + '''
{n}He blinks at you through the tears as if you had only just walked in.{/n}''',
    '''{n}Thaberdine weeps openly into his mug, and then drinks from it anyway.{/n}
"That's it! That's the one! That's how pops sang it!" ''' + KING_WEEPS + '''
{n}He blinks at you through the tears as if you had only just walked in.{/n}'''),
    requires=("trickster",), forbids=(PRIMED, ROMANCE, FAILURE), chapter=3, hub=KING_C3, back=KING_C3_RETURN)

tavern("aranka.trickster.verse.kings_tavern_c5", "A rhyme for Thaberdine", '"Your Majesty. That ballad of yours."', king_nodes(
    '''{n}The King's court has come back from the war louder, fewer and a great deal drunker. Thaberdine is still singing the ballad his pops used to sing, and he still loses the words in the second verse, and the court still bangs its mugs through the gap as if that were how it went.{/n}''',
    '''{n}Thaberdine takes off his crown, weeps into it, and puts it back on wet.{/n}
"That's it! That's the one! That's how pops sang it!" ''' + KING_WEEPS + '''
{n}He raises his mug to you, and then to the pig, and then to you again, as if you had only just walked in.{/n}'''),
    requires=("trickster", CROWNED), forbids=(PRIMED, ROMANCE, FAILURE, KING_GONE), chapter=5, hub=KING_C5, back=KING_C5_RETURN)

def her_letter_choices(*extra):
    """Her letter's two answers (fresh dicts per page); the late fallback folds the primer and its cost into them."""
    return (c('[Confess] "Guilty. I needed a rhyme for \'Thaberdine\'."', flags=(*extra, ANSWERED, STARTED, CREDITED)),
            c('[Lie] "Never heard it. Must be the Desnans."', flags=(*extra, ANSWERED, STARTED, DENIED)))


letter("aranka.trickster.verse.any_tavern", "Every mug in the house", [
    nar("start", '''{n}There is no King left to sing to, and no tavern of his to sing in. So you climb onto a table in the worst camp tavern in Drezen instead, pay for every mug in the house, and teach a room full of sappers and quartermasters Starward Gaze with a second verse of your own. Nobody in the room has heard of Thaberdine. You rhyme him with 'tambourine' anyway.{/n}
{n}It takes all night and most of the camp's beer. By dawn the sappers are singing it on the walls, and by the following week the song has walked out of Drezen on its own, in the packs of every courier and carter on the north road.{/n}''',
        c(JOKE, "reply", mythic="Trickster", crusade=("Finances", -150)),
        c('"...On second thought, buy them one round and let them sing what they like."', abort=True)),
    nar("reply", '''{n}Nine days later a letter arrives, in a round, flourishing hand that has pressed hard enough to tear the paper in two places.{/n}''',
        c("Continue", "reply_known", requires=(GAVE_SONG,)),
        c("Continue", "reply_unknown", forbids=(GAVE_SONG,))),
    a("reply_known", '''"Somebody has changed my song! Every camp from here to the Worldwound is singing Starward Gaze with a verse I never wrote, and they all swear it was always sung that way, and it wasn't, and it's better, which is the worst part!"
"It came to us from the true servants of Desna, from her domain in Elysium, and I carried it out of Kenabres in one piece. I gave it to you in one piece, Commander, and Ilkes asked you to remember it, not to improve it. The carters say it started in Drezen. I am coming to Drezen to find the thief."''',
      *her_letter_choices(PRIMED, LATE)),
    a("reply_unknown", '''"To the Knight-Commander of Drezen, from Aranka, who sings for Desna and would like a word."
"Somebody has changed my song! Every camp from here to the Worldwound is singing Starward Gaze with a verse I never wrote, and they all swear it was always sung that way, and it wasn't, and it's better, which is the worst part! The carters say it started in your city, in a tavern, with somebody paying for the beer. I am coming to Drezen to find the thief. Please have them ready."''',
      *her_letter_choices(PRIMED, LATE)),
], requires=("trickster",), forbids=(PRIMED, ROMANCE, FAILURE, CROWNED), delay=0, **NO_KING_GATE)
# The act is performed on the page now, and dearer than the King's round; her reply is folded in so the route spends
# one letter, and its answers record the primer and the late cost as well (R2-2).

letter("aranka.trickster.verse.her_letter", "Somebody changed my song", [
    nar("start", '''{n}The letter is in a round, flourishing hand that has pressed hard enough to tear the paper in two places. It smells faintly of road dust and lamp oil, and someone has used it as a coaster.{/n}''',
        c("Continue", "known", requires=(GAVE_SONG,)),
        c("Continue", "unknown", forbids=(GAVE_SONG,))),
    a("known", '''"Somebody has changed my song! Everyone swears it was always sung that way, and it wasn't, and it's better, which is the worst part! A tavern king in Drezen is telling the whole city his pops learned it from me. I have never met his pops. I have never met him. Old Marit heard it in his tavern and walked four days to tell me, and she was crying, and I could not tell whether it was the good kind."
"It came to us from the true servants of Desna, Commander. I carried it out of Kenabres in one piece and I put it into your hands in one piece, and Ilkes asked you to remember it. I did not ask you to rhyme it with a tambourine. I am coming to Drezen to find the thief."''',
      *her_letter_choices()),
    a("unknown", '''"To the Knight-Commander of Drezen, from Aranka, who sings for Desna and would like a word."
"Somebody has changed my song! Everyone swears it was always sung that way, and it wasn't, and it's better, which is the worst part! A tavern king in your city is telling everyone his pops learned it from me. I have never met his pops. I have never met him. Old Marit, one of our pilgrims, heard it in his tavern and walked four days to tell me. She says the new verse arrived with a Knight-Commander standing on a bench and paying for the beer."
"I am coming to Drezen to find the thief. Please have them ready."''',
      *her_letter_choices()),
], requires=("trickster.ever", PRIMED), forbids=(ANSWERED, ROMANCE, FAILURE), delay=72)


# --- In person, at Fye's counter (R2-1, R2-3) ----------------------------------------------------------------------

counter("aranka.trickster.verse.duet", "Second verse, the good one", '"You wanted the thief. Here I am."', [
    nar("start", '''@OPEN@
{n}The woman on @SEAT@ is in Desnan blue, road-dusty to the knee, with a lute across her lap and a cup of the worst wine in Drezen she has not touched. Every head in the room is turned towards her, and she knows it, and she is enjoying it more than she would ever admit.{/n}''',
        c("Continue", "mocking", requires=(MOCKING,)),
        c("Continue", "posters", requires=(ANNOUNCED,), forbids=(MOCKING,)),
        c("Continue", "denied", requires=(DENIED,), forbids=(MOCKING, ANNOUNCED)),
        c("Continue", "vandal", forbids=(MOCKING, ANNOUNCED, DENIED))),
    a("vandal", '''"You! Oh, you wonderful vandal."
{n}She presses both hands to her cheeks, and then remembers she is angry and puts them back on the lute.{/n}
"There is no rhyme for Thaberdine. I tried, you know. Afterwards. I sat up two nights. There wasn't one, until you, and now there is, and it's 'tambourine', and I will never get it out of my head as long as I live."''',
      c('[Sing it] "Second verse. The good one."', "duet")),
    a("denied", '''"The Desnans, you said." {n}She does not smile.{/n} "I am the Desnans. Three camps and a ferryman pointed me at you, Commander, and the ferryman did an impression."
"So. You never heard it. Sing it for me, then. The second verse. If you can't, I'll know you lied once. If you can, I'll know you lied twice."''',
      c('[Sing it] "Second verse. The good one."', "duet")),
    a("mocking", '''{n}She puts the lute down, walks the length of the counter, and slaps you. Not hard. Precisely.{/n}
"There. I decided. I have been deciding since the letter." {n}She shakes out her hand.{/n} "I wrote that song to hurt you. You stood on a bench and made a whole tavern sing it louder, and now it's the most requested song between here and the river, and every time they sing it they're laughing with you, not at you. You stole my revenge and made it scan."
"Now sing it with me. The verse where you lose. I'll take the harmony."''',
      c('[Sing it] "The one where I lose. From the top."', "duet")),
    a("posters", '''"You put me on a poster before you put me in a letter." {n}She lays a torn corner of one on the counter: KNIGHT-COMMANDER'S COURT POET, and half of TONIGHT.{/n}
"You billed a song, Commander, so now you will have to earn the billing. Starward Gaze came to us from the true servants of Desna, and nobody I know has ever dared add a verse to it. You're going to. Here. In front of all of them. And then I'm going to decide how badly you did it."''',
      c('[Sing it] "A second verse. Mine."', "duet")),
    a("duet", '''"You owe me a duet for this. And an apology. Mostly the duet."
{n}She hands you the second verse, and takes the harmony herself, and for three minutes nobody in Drezen is at war. Nobody moves. A sapper by the gate takes his helmet off without knowing he has done it.{/n}
{n}When it ends there is the kind of silence that is worth more than applause, and then the applause, and she soaks up every bit of it with her eyes closed.{/n}
"My name goes first on every copy. Yours goes underneath. In small letters. Very small."''',
      c('[Sign under her name] "Small letters. Agreed."', "signed"),
      c('[Argue the billing] "Put mine first. It\'s my verse."', "billing")),
    a("signed", '''"Good." {n}She writes both names on @PAPER@, hers in a round hand like a lark on a wire and yours underneath, so small it could be a flaw in the paper.{/n}
"I'm singing it in every camp between here and the river. Every night. I'll decide each morning whether to come back and tell you how it went."''',
      c('"I\'ll be here."', flags=(DUET, CREDITED))),
    a("billing", '''"Your verse." {n}She laughs, delighted and not at all moved.{/n} "Your verse is eleven words and a tambourine, Commander. My name goes first. Argue with me again and it goes first in capitals."
{n}She writes both names on @PAPER@ anyway, yours underneath, and underlines hers twice.{/n}
"I'm singing it in every camp between here and the river. Every night. I'll decide each morning whether to come back and tell you how it went."''',
      c('"I\'ll be here."', flags=(DUET, VAIN))),
], requires=("trickster.ever", ANSWERED), forbids=(CLOSED, DUET), delay=72)


def night_nodes():
    """The intimate beat after the commit (Directive 12): the threshold, the cut at the start of the act, the morning."""
    return [
        nar("threshold", '''{n}@ROOM@ She does not seem to notice either. She sets the lute against the wall with more care than she takes over anything else, and turns round, and there is nothing careful left in her at all.{/n}
{n}She kisses you the way she sings, all breath and no hurry, and hums against your mouth when you pull her closer, a low, rising phrase you feel in your own chest before you hear it. The Desnan blue comes off over her head. She is warm as a hearth underneath it, and she takes your hands and sets them on her where she wants them, and makes a small sound, and holds them there.{/n}
{n}"Count me in," she whispers, and pulls you down onto the narrow bed, and climbs astride you with her hair falling round both your faces.{/n}''',
            c("Continue", "morning")),
        nar("morning", '''{n}Dawn. @HOUSE@ hears her singing through the floorboards at first light, something new and unfinished that stops and starts again, and by the time you come down @CROWD@ is very busy looking at his breakfast.{/n}
{n}@BILL@: the room, the broken slat in the bed, "lost custom", and a line at the bottom that only says "Noise." Aranka reads it over your shoulder, laughs until she has to sit down, and pays it herself.{/n} "Don't you dare take it off the war chest. I earned every copper of that."''',
            c('[Keep the bill.]', flags=(NIGHT,))),
    ]


counter("aranka.trickster.verse.encore", "An offer from Nerosyan", '"You came back again."', [
    nar("start", '''{n}She is on @SEAT@ again, lute across her knees, with a letter in her hand that has a Mendevian seal on it. She has read it enough times to soften the folds.{/n}''',
        c("Continue", "offer")),
    a("offer", '''"A troupe in Nerosyan wants me. A real stage, a real hall, a hundred people a night who have paid to sit still. They want Starward Gaze, the new one. With your verse."
{n}She looks at the letter, and then at you, and then at the letter.{/n}
"I went round every camp this week. I sang it in all of them. The pikemen at the ford made me sing it three times and then sang it back to me wrong. And every night I came back here. I haven't decided why."''',
      c("Continue", "vain", requires=(VAIN,)),
      c("Continue", "denied", requires=(DENIED,), forbids=(VAIN,)),
      c("Continue", "lovers", requires=(ROMANCE,), forbids=(VAIN, DENIED)),
      c("Continue", "choice", forbids=(VAIN, DENIED, ROMANCE))),
    a("vain", '''"And before you say it: no, the Nerosyan bill does not put your name first either. I asked. They laughed. I liked them for it."''',
      c("Continue", "choice")),
    a("denied", '''"You lied to me about the verse, the first time. I haven't forgotten. I have decided to find it interesting, which is not the same as forgiving it."''',
      c("Continue", "choice")),
    a("lovers", '''"The last time I went, you stood in the door and let me, and I sang the whole road north pretending that was what I wanted." {n}Her thumb worries the edge of the seal.{/n} "I'm a very good singer, Commander. I'm a terrible liar. Ask the road."''',
      c("Continue", "choice")),
    a("choice", '''"So tell me, Commander. Is there a reason to stay that isn't a song?"''',
      c('[Ask her to stay] "Stay. Sing it with me. Every night we get."', "stay", flags=(KEPT,)),
      c('[Charm her] "Stay, and I\'ll rhyme you anything."', "not_yet"),
      c('[Tell her to take the stage] "Go. A song that stays in one tavern dies."', "stage", flags=(CLOSED, NEROSYAN))),
    a("not_yet", '''"That's a pretty line." {n}She folds the Mendevian letter very small, and then smaller.{/n}
"Too pretty. You wrote a verse for a king and a verse for a crowd. Write one for me, and mean it, and ask me again. Not tonight."''',
      c('[Accept her terms] "Then I\'ll write it."', flags=(DECLINED,))),
    a("stage", '''{n}She is quiet for a long time. When she speaks, her voice is steady, and it costs her.{/n}
"That's the kindest thing anyone has ever said to me, and I hate it." {n}She tucks the Mendevian letter into her bodice and stands, and settles the lute on her back.{/n}
"I'll sing your verse every night. And every night I'll tell them who wrote it. In small letters."''',
      c('"Go on. They\'re waiting."')),
    a("stay", '''{n}She looks at you for a long moment, the way she looked at the room before the duet, as if she were deciding how it will sound.{/n}
"Every night we get." {n}She drops the Mendevian letter into @STOVE@ without looking at it.{/n} "That's a better line than the verse. I'm stealing it."''',
      c("Continue", "threshold")),
    *night_nodes(),
], requires=("trickster.ever", DUET), forbids=(CLOSED, KEPT, DECLINED), delay=72)

counter("aranka.trickster.verse.third_verse", "The third verse", '"I wrote it."', [
    a("start", '''"Well?" {n}She has cleared a space on @STAGE@, and the whole crowd is watching, and she has made sure of that.{/n}
"The third verse. For me. You sing it alone, in front of all of them, badly, and you sign it under your own name. Big letters. Then ask."''',
      c('[Sing it alone] "...Everybody. Quiet. This one\'s mine."', "sung", crusade=("Favors", -100), flags=(KEPT, SANG_ALONE)),
      c('[Refuse] "I don\'t sing alone."', "refused", flags=(CLOSED,))),
    nar("sung", '''{n}You sing it alone. Your voice cracks on the second line, and a sergeant at the back laughs out loud, and then stops laughing. By the end the room is silent in a way it has not been since the duet, and the story of the Knight-Commander singing a love song, badly, on @STAGE@, will outlive both of you in every barracks in Drezen.{/n}''',
        c("Continue", "answer")),
    a("answer", '''{n}She is crying, and furious about it, and laughing.{/n} "That was terrible. That was the worst verse anyone has ever written for me. Sign it. Big letters. And yes. Obviously yes."''',
      c("Continue", "threshold")),
    a("refused", '''"Then you're a very good thief, Commander, and nothing else." {n}She takes her lute off @STAGE@ and does not look back.{/n}''',
      c('"Aranka..."')),
    *night_nodes(),
], requires=("trickster.ever", DECLINED), forbids=(CLOSED, KEPT), delay=72)


# --- State parent_failure: the verse where you lose (F05) -----------------------------------------------------------

def mocking_nodes():
    return [
        nar("start", '''{n}Somebody at the back of the King's tavern starts the camp's favourite song about you: the one Aranka wrote after everything between you went wrong, the one where the Knight-Commander trips over their own banner and the demons laugh too hard to fight. The room goes quiet and looks at you.{/n}''',
            c("Continue", "king")),
        king("king", '''"Sing it, Majesty! Sing the one where you lose!" {n}Thaberdine beams at you with perfect, drunken goodwill. He thinks you are both kings.{/n}''',
             c(FAILURE_JOKE, "loud", mythic="Trickster"),
             c('"Not tonight, Your Majesty."', abort=True)),
        nar("loud", '''{n}You climb onto the bench and lead it. You sing the banner verse louder than anyone, and trip over an imaginary banner on the rhyme, and the tavern howls. By the third round they are singing it with you, not at you, and by the fifth it has become a drinking song about the one commander in the world who can take a joke.{/n}''',
            c("Continue", "after")),
        king("after", '''"Now THAT'S a king!" {n}Thaberdine wipes his eyes.{/n} "Pops always said, a king who can't sing his own defeats won't live to see many victories. Or was it the other way round? One of 'em!"''',
             c('"Again. Louder on the rhyme."', flags=(PRIMED, MOCKING))),
    ]


tavern("aranka.trickster.failure.mocking_verse", "The verse where you lose", '"What are they singing back there?"',
       mocking_nodes(), requires=("trickster", FAILURE), forbids=(PRIMED,), chapter=3, hub=KING_C3, back=KING_C3_RETURN,
       TricksterDevice=True, TricksterState=FAILURE)

# Chapter 5, while the crowned King still holds court: the same verse on his Chapter 5 list (the late fallback Forbids
# his crown, so without this a failure-state Commander would have no setup until the King left).
tavern("aranka.trickster.failure.mocking_verse_c5", "The verse where you lose", '"What are they singing back there?"',
       mocking_nodes(), requires=("trickster", FAILURE, CROWNED), forbids=(PRIMED, KING_GONE), chapter=5, hub=KING_C5,
       back=KING_C5_RETURN, TricksterDevice=True, TricksterState=FAILURE)

letter("aranka.trickster.failure.mocking_verse_any", "Louder on the rhyme", [
    nar("start", '''{n}The camp's favourite song about you is the one Aranka wrote after everything between you went wrong: the Knight-Commander trips over their own banner, and the demons laugh too hard to fight. The sappers sing it when they think you can't hear.{/n}
{n}There is no King's tavern left to lead it in. So you walk into the worst camp tavern in Drezen, pay for every mug in the house, and climb onto a table.{/n}''',
        c(FAILURE_JOKE, "reply", mythic="Trickster", crusade=("Finances", -150)),
        c('[Walk out again.]', abort=True)),
    nar("reply", '''{n}You lead it until dawn, and trip over an imaginary banner on every rhyme. By the next week the song has changed its meaning on every road out of Drezen.{/n}
{n}Nine days later a letter comes, in a round hand you know, with a blot in the middle as if the writer stopped for a long while.{/n}''',
        c("Continue", "her_reply")),
    a("her_reply", '''"You sang the verse where you lose. Out loud, on purpose, and made them sing it louder. Nobody has ever done that with one of my songs. I wrote it to hurt you. You made it yours. I am coming to Drezen, and I haven't decided yet whether to slap you."''',
        c('[Answer her] "Come and decide."', flags=(PRIMED, LATE, MOCKING, RETURNED, ANSWERED, STARTED))),
], requires=("trickster", FAILURE), forbids=(PRIMED, CROWNED), delay=0, **NO_KING_GATE,
   TricksterDevice=True, TricksterState=FAILURE)

letter("aranka.trickster.failure.second_verse", "A blot in the middle", [
    a("start", '''"I heard what you did in the King's tavern. You sang the verse where you lose. Out loud, on purpose, and you made them sing it louder."
{n}A blot, as if she stopped writing for a while.{/n}
"Nobody has ever done that with one of my songs. I wrote it to hurt you. You made it yours, and now it's the most requested song between here and the river, and I can't sing it anywhere without somebody raising a cup to you."
"I am coming to Drezen, and I haven't decided yet whether to slap you."''',
      c('[Answer her] "Come and decide."', flags=(RETURNED, ANSWERED, STARTED))),
], requires=("trickster.ever", FAILURE, PRIMED), forbids=(RETURNED,), delay=72, TricksterDevice=True, TricksterState=FAILURE)


# --- State parent_done_non_azata: billed before she was asked (F05) ------------------------------------------------

letter("aranka.trickster.touring.boast", "Court poet", [
    nar("start", '''{n}Aranka is three camps away, singing for pikemen. You have not seen her since your story together reached its end, and she has not written. The crusade's printers, on the other hand, owe you a favour.{/n}''',
        c(TOURING_JOKE, "posters", mythic="Trickster", crusade=("Finances", -100)),
        c('[Let her keep her road.]', abort=True)),
    nar("posters", '''{n}By morning every wall in Drezen carries a poster: STARWARD GAZE, SUNG BY THE KNIGHT-COMMANDER'S COURT POET, TONIGHT. The paste is still wet. The printers spelled her name right on the first try, because you stood over them.{/n}
{n}Aranka is three camps away and has agreed to nothing. The posters travel faster than she does.{/n}''',
        c('"Put one up at the ford, too."', flags=(PRIMED, ANNOUNCED))),
], requires=("trickster", ROMANCE, QUEST), forbids=(PRIMED, "azata", FAILURE), delay=0)

counter("aranka.trickster.touring.arrives", "Court poet", '"You came."', [
    a("start", '''{n}She is standing under one of the posters with it half torn off the wall in her fist.{/n}
"Court poet. I have never been anybody's court anything. I came here to shout at you in person, because a letter wouldn't be loud enough, and because I wanted to see your face when I did it."''',
      c('"Then shout."', "shout"),
      c('"You spelled it right. I checked."', "shout")),
    a("shout", '''"I am. This is shouting. I'm a singer, I don't have to be loud to be shouting." {n}She smooths the poster out against her knee, and reads it again, and something in her face gives way.{/n}
"...It's a very good poster. You spelled my name right. Nobody spells my name right."
"Fine. One night. I sing. You listen. And after that we talk about who owns what, because I don't remember agreeing to be owned by anyone, least of all by you, and least of all in capital letters."''',
      c('[Agree to her terms] "One night. You sing. I listen."', flags=(ANSWERED, STARTED))),
], requires=("trickster.ever", PRIMED, ROMANCE), forbids=(ANSWERED, "azata"), delay=48)


# --- Epilogue pages (R2-6; ordered siblings, no page effects) -------------------------------------------------------

VERSE_PARAGRAPHS = (
    p("She sang the thief's verse herself, to the end of her days, and before it she always told the hall that the "
      "thief had said it must be the Desnans. The halls always laughed. The Commander never did.", requires=(DENIED,)),
    p("The third verse, the one the Knight-Commander sang alone and badly on Fye's bar, is printed under the other two "
      "in every copy. It has never once been sung well. Aranka would not allow it.", requires=(SANG_ALONE,)),
    p("The verse where the Knight-Commander trips over their own banner is still the most requested of the three.",
      requires=(MOCKING,)),
)


def page(id, title, text, requires, forbids=(), paragraphs=(), **extra):
    SCENES.append(scene(id, title, "Epilogue", 1, "", [nar("end", text, paragraphs=paragraphs)], requires=requires,
                        forbids=forbids, last=99, Relationship="aranka", **extra))


page("aranka.trickster.epilogue.commit", "The last night in Nerosyan",
     '''{n}After Threshold Aranka took the Nerosyan stage for a single season. On its last night she sang Starward Gaze with a third verse nobody had heard before, and then she told the hall she was going home to Drezen, where the second verse had been written, and to the person who had written it. She did not say anything else. She did not need to.{/n}''',
     requires=("trickster.ever", LATE_COMMITTED), forbids=(KEPT, CLOSED, DECLINED), paragraphs=VERSE_PARAGRAPHS)

page("aranka.trickster.epilogue.declined", "Two verses",
     '''{n}The third verse was never written. Aranka sang Starward Gaze for the rest of her life with two verses, and at the end of the second she always stopped, and waited a heartbeat, as though somebody in the back of the hall might still stand up and sing.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(KEPT,))

page("aranka.trickster.epilogue.verse", "Two names",
     '''{n}Starward Gaze outlived the crusade. Every printed copy carries two names: hers first, in a hand like a lark on a wire, and underneath, in letters so small you need a candle, the Commander's.{/n}''',
     requires=("trickster.ever",), forbids=(CLOSED, DECLINED), paragraphs=VERSE_PARAGRAPHS,
     RequiresAnyGroups=[[KEPT, LATE_COMMITTED]], ForbidOverrides={DECLINED: KEPT})

page("aranka.trickster.epilogue.nerosyan", "Twenty years on a stage",
     '''{n}Aranka took the Nerosyan stage and kept it for twenty years. She sang the Commander's verse every night, and every night she said who wrote it. In small letters, she always added. Very small.{/n}''',
     requires=("trickster.ever", NEROSYAN))


# --- Reactions (ledger 05 section 3.1 row 3: exactly Anevia, Woljif and Lann) --------------------------------------

ANEVIA_GUARD = dict(ForbidOverrides={"anevia_gone": "anevia.trickster.returned"})
WOLJIF_GONE = ("woljif.dead", "woljif.kicked_out")
LANN_GONE = ("lann.dead", "lann.kicked_out")

REACTIONS = [
    reaction("Anevia", "aranka.trickster.react.anevia_verse", (PRIMED,),
             '''"Half the garrison's singing that star song wrong. Beth's humming it on watch. Tambourine. Honestly." {n}Anevia shakes her head, and hums two bars of it before she can stop herself.{/n} "I'm blaming you."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "irabeth_dead"), chapter=3, last=5, Chapters=[3, 5],
             entry='"Something wrong with the garrison?"',
             ForbidOverrides={"anevia_gone": "anevia.trickster.returned", "irabeth_dead": "irabeth.trickster.returned"}),
    reaction("Anevia", "aranka.trickster.react.anevia_verse_alone", (PRIMED, "irabeth_dead"),
             '''"Half the garrison's singing that star song wrong." {n}Anevia looks at the wall, at the place where the night watch used to stand.{/n} "I caught myself humming it up there last night. Don't. I'm blaming you, that's all."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "irabeth.trickster.returned"), chapter=3, last=5,
             Chapters=[3, 5], entry='"Something wrong with the garrison?"', **ANEVIA_GUARD),
    reaction("Woljif", "aranka.trickster.react.woljif_billing", (DUET,),
             '''"Chief, there's copies going round. Her name up top, big as a barn, and yours underneath in letters so small I had to lick my thumb to read 'em." {n}Woljif grins.{/n} "I'm charging people a copper to see the fine print."''',
             answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
             entry='"You look pleased with yourself."'),
    reaction("Woljif", "aranka.trickster.react.woljif_mocking", (MOCKING,),
             '''"Chief, they're singing the one where you trip over your own banner." {n}Woljif looks genuinely shaken.{/n} "You LED it. That's the part I don't get. Nobody leads the one about themselves. That's, like, the first rule."''',
             answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
             entry='"Something on your mind?"'),
    reaction("Lann", "aranka.trickster.react.lann_verse", (ANSWERED,),
             '''"The whole camp knows your verse now." {n}Lann shrugs.{/n} "Tambourine. Really. I'll only sing it when you're winning."''',
             answer_list=LANN_HUB, forbids=LANN_GONE, chapter=3, last=5, Chapters=[3, 5],
             entry='"Heard any good songs lately?"'),
]
SCENES.extend(REACTIONS)


def integrate(payload):
    """Save-safe: the registered island route is untouched (no id, node or choice changed). Adds the Trickster access,
    the failure override, the presence and one Guidance sentence."""
    rel = payload["Relationships"]["aranka"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Commander who gives Starward Gaze a second verse in a tavern, or leads "
                        "the verse where they lose, or bills her as their court poet, may meet Aranka at Fye's counter "
                        "in Drezen, in Chapter 3 or Chapter 5.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    payload.setdefault("Derived", {})[NO_KING] = [[KING_GONE]]
