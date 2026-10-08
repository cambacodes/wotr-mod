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
Authored R4 D05-D06: a visiting Nerosyan troupe-master hears the duet while her players perform for the garrison;
she delivers the invitation locally. No journey to Nerosyan and back is needed for the Chapter 5 offer.
"""
import copy

from story_format import c, n, p, reaction, scene

# Authored ordinary correspondence, grounded in DesnaAdepts/Cue_0004-0007.
# Thall's interest is one-sided; no return, former partnership or island is created.
THALL_SAFE = "aranka.thall.left_kenabres"  # DesnaAdept3/Cue_0026: rescued, goes to temple
THALL_CALL = "{n}The song brings no news of Thall, the quiet Desnan adept from Kenabres: neither his whereabouts nor his fate. No second voice joins it beneath the roar.{/n}"  # legacy shared cleanup token
THALL_REQUESTED = "aranka.thall.letter_sent"
THALL_ANSWERED = "aranka.thall.parting_spoken"
THALL_ENDING = '{n}Thall sent Aranka a hymn with the low part marked. She sent it back with his name beside the melody and three corrections. The next packet contained four.{/n}'
THALL_CALLBACK = '{n}Among her new songs was the hymn Thall had sent. His corrections still crowded the margin; she sang his low part without trying to improve it.{/n}'

THALL_DEAD = "aranka.thall.dead"  # native TallDead_in_Fane, verified in blueprints.zip
COMMANDER_STAYS = "aranka.commander.stays"
COMMANDER_LEAVES = "aranka.commander.leaves"
THALL_MEMORY = p("""{n}When word of Thall's death in the Midnight Fane reached her, she put aside the song she had meant to send him. She sang the low part herself, once, and could not finish it.{/n}""", requires=(THALL_DEAD,))

SCENES = []
UNIT = "430cba7801b149b4e8494ace6baf4f7c"           # Azata_Aranka_DesnaPriest (no dialog component; the presence copy)
DREZEN = "2570015799edf594daf2f076f2f975d8"
MARKET = "bad9f602b81a80047ac470b01ebe65a9"         # ExoticCapitalTrader: the spice-and-curio stall, no other route's anchor
YARD_UNIT = "bd0c4fe722aeef94b8495ac284b96bc8"      # Azata_Aranka_RankupSpeaker: her Chapter 3 look, a second unit for the yard
QUARTERMASTER = "15f754455d1d87c42a4e14df456d5415"  # F9: capital blacksmith, ordinary Traders mechanics; authored yard placement
KING_C3 = "1a17d8053a3be7f47a7908eb6706f2fe"        # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0009
KING_C3_RETURN = "814dd1a078a1c2849aefc85e2e15b2d2" # FoolKing_Tavern/Cue_0008 "Oh, Commander! Nice of you to stop by."
KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"        # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_RETURN = "7b050ba0745bf144e815632e39b34853" # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"     # NPC_Common/Anevia/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"     # CompanionDialogues/Woljif/AnswersList_0003
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"       # CompanionDialogues/Lann/AnswersList_0003

HUB = "aranka.presence"
YARD = "aranka.presence.yard"
FYE_GONE = "aranka.presence.failed"  # runtime: her copy is wanted but the market stall is not in the capital (id kept)
PRIMED = "aranka.trickster.primed"
ANSWERED = "aranka.trickster.answered"
RETURNED = "aranka.trickster.returned"
# Polish (coordinator ruling 2026-10-02, item 1): the parent failure is lifted only by answering her moral objection in
# person (failure.reckoning/bought), never by the song alone. RETURNED stays a legacy reply record (ValidateDevice).
MORAL_REPAIRED = "aranka.trickster.moral_repaired"
PROVISIONS = "aranka.trickster.cost.provisions_bought"
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
CONTEST_WON = "aranka.kenabres_contest_won"   # SeenCues DesnaAdept2/Cue_15 dd66b8ab: "you've outmatched me, I admit it!" (PP3)
CROWNED = "fool_king.crowned"
TABLET_TRUE = "fool_king.tablet_true"  # SeenCue FoolKing_Tavern/Cue_0038: the tablet's letters repeat his words
KING_GONE = "fool_king.gone"
# Derived twin of fool_king.gone: a ForbidOverride value must be authored or Derived, never a native key. The late
# fallbacks Forbid the crown unless the King is gone, so they open only when no King is left to sing to: the King
# is gone, or the Coronation has passed and he was never crowned (then no Chapter 5 King scene exists).
NO_KING = "aranka.trickster.king_gone"
# Q8 (Sol TRK/CAN/INT): the Commander attacked the Desnan adepts in Kenabres (DesnaTempleFinal/Answer_0026 3259064c,
# "[Attack] ...I'm going to kill you."; Cue_0027 8b066a9c starts the fight). Aranka died there; no living copy, letter or
# page may follow. Bound as SelectedAnswers and added to her relationship's UnavailableFlags (pages forbid it directly,
# since epilogue availability skips relationship flags).
KENABRES_ATTACKED = "aranka.kenabres_attacked"
KENABRES_ATTACK_ANSWER = "3259064c6a1ac284c80ecc7d3fad6135"
NO_KING_GATE = dict(RequiresAnyGroups=[[KING_GONE, "coronation.seen"]], ForbidOverrides={CROWNED: NO_KING})

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={FAILURE: MORAL_REPAIRED},
    TricksterAccess={
        "never_entered": dict(detect=[], device="aranka.trickster.verse.kings_tavern", returned=ANSWERED),
        FAILURE: dict(detect=[FAILURE], device="aranka.trickster.failure.mocking_verse", returned=MORAL_REPAIRED),
        "parent_done_non_azata": dict(detect=[], device="aranka.trickster.touring.boast", returned=ANSWERED),
    })
PRESENCES = {
    # A spawned copy of her Azata-island actor busking on the crates by the spice trader's stall in the market (polish
    # 2026-09-28: off Fye's counter, where other routes already stand). A singer on the road plays where the coin is,
    # not in the one tavern everybody else drinks in.
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=MARKET, Side="front", Distance=3.5),
              Requires=["trickster.ever", "aranka.trickster.in_drezen"], Forbids=[CLOSED], MinChapter=3, MaxChapter=5,
              AnswerLists=[], Dialog="hub",
              Greeting="{n}A woman in Desnan blue is sitting on a stack of spice crates by the curio stall with a lute "
                       "across her knees, and half the market has stopped haggling to hear her tune it.{/n}"),
    # If the market stall is not in the capital, aranka.presence.failed is raised and she sings in the quartermaster's
    # yard instead: a copy of a different unit of hers, beside the ordinary capital blacksmith (F9). The same four in-person
    # beats have yard copies (ids ending _yard).
    YARD: dict(Unit=YARD_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=QUARTERMASTER, Offset=[5.0, -7.0]),
               Requires=["trickster.ever", "aranka.trickster.in_drezen", FYE_GONE], Forbids=[CLOSED], MinChapter=3,
               MaxChapter=5, AnswerLists=[], Dialog="hub",
               Greeting="{n}The market is shuttered. A woman in Desnan blue is sitting on the tailgate of a supply wagon in the "
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
        "@OPEN@": "{n}The spice trader catches your sleeve before you reach his stall.{/n} \"She's been tuning that thing on my crates for an hour and nobody's bought so much as a pinch of pepper since. Do something.\"",
        "@SEAT@": "a stack of the spice trader's crates",
        "@PAPER@": "the back of the spice trader's tally-slip",
        "@STOVE@": "the spice trader's brazier",
        "@STAGE@": "the crates",
        "@ROOM@": "She has a room above the market, rented by the week, and she walks straight past its door. The outside stair goes on up to a flat roof, and the sky over Drezen is thick with stars for once.",
        "@HOUSE@": "The whole market row",
        "@BILL@": "There is a note nailed to the stair door in the watch-sergeant's hand",
        "@CROWD@": "every stallholder putting up his awning",
        "@DOWN@": "stair",
    }),
    "yard": dict(suffix="_yard", hub=YARD, unit=YARD_UNIT, requires=(FYE_GONE,), texts={
        "@OPEN@": "{n}The market is shuttered, so the quartermaster's yard has become a tavern without a roof. A carter catches you at the gate.{/n} \"She's been tuning that thing for an hour and my carters haven't lifted a crate since. Do something.\"",
        "@SEAT@": "the tailgate of a supply wagon",
        "@PAPER@": "the back of a quartermaster's requisition",
        "@STOVE@": "the carters' brazier",
        "@STAGE@": "the wagon bed",
        "@ROOM@": "She has a room in a carters' lodging house by the south gate, and she walks straight past its door. A ladder goes on up to the flat roof over the mule lines, and the sky over Drezen is thick with stars for once.",
        "@HOUSE@": "The whole lodging house",
        "@BILL@": "There is a note nailed to the ladder in the landlady's hand",
        "@CROWD@": "every carter at the long table",
        "@DOWN@": "ladder",
    }),
}


def fit(text, place):
    for token, value in PLACES[place]["texts"].items():
        text = text.replace(token, value)
    return text


def placed(nodes, place):
    return [dict(node, Text=fit(node["Text"], place), Choices=[dict(ch) for ch in node["Choices"]]) for node in nodes]


def counter(id, title, entry, nodes, requires, forbids, delay, **extra):
    """An in-person beat on her presence hub: by the market stall, and a yard copy for when the stall is not in the capital."""
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
        nar("known", '''{n}You know that tune, or something very like it. You last heard it in Kenabres, in Desna's temple while the city burned, sung by a priestess called Aranka who had just put it into your keeping. Hers had words that went all the way through. His has a hole in the middle where a verse should be.{/n}''',
            c(JOKE, "round", mythic="Trickster", crusade=("Finances", -100)),
            c('"Never mind. Carry on, Your Majesty."', abort=True)),
        nar("unknown", '''{n}You know that tune, or something very like it. Half the Desnan refugees on the road out of Kenabres were humming it, and the ones who knew the words called it Starward Gaze and said a priestess named Aranka had carried it out of the burning city. Theirs went all the way through. His has a hole in the middle where a verse should be.{/n}''',
            c(JOKE, "round", mythic="Trickster", crusade=("Finances", -100)),
            c('"Never mind. Carry on, Your Majesty."', abort=True)),
        nar("round", '''{n}You climb onto the bench and pay for every mug on every table. The sapper nearest you drums his empty mug against the wood.{/n}
{n}You sing the King's ballad back at him with the words of a Desnan hymn you have no right to and a second verse of your own. The rhyme for 'Thaberdine' is 'tambourine'. It is a dreadful rhyme. A sapper learns it first, then the one-eyed carter by the door, then the girl who carries the King's mugs, who has a better voice than any of them.{/n}''',
            c("Continue", "sheet")),
        nar("sheet", '''{n}Thaberdine fishes inside his shirt and brings out the greasy, folded song-sheet his pops left him, the one thing he owns that is older than his debts, and smooths it on the table to show you how the ballad really goes.{/n}
{n}There is a gap in the second verse, a blank where the ink gave out. The King licks a stub of charcoal and writes your verse into it himself, 'tambourine' and all, in letters that lean like drunks, and then holds the sheet up to the room and swears on his pops' tankard it was always there. Nobody at his table is sober enough to argue.{/n}''',
            c("Continue", "stone", requires=(TABLET_TRUE,)),
            c("Continue", "pilgrim", forbids=(TABLET_TRUE,))),
        nar("stone", '''{n}You have seen him do this before, at this same table, with the moss-covered stone from Pulura's Fall that repeated his words because you told him it would. He has decided this sheet is the same kind of miracle, and in the King's tavern that is as good as proof.{/n}''',
            c("Continue", "pilgrim")),
        nar("pilgrim", '''{n}By the fifth round they are correcting each other's words from the sheet, and every one of them swears their grandmother sang it exactly that way.{/n}
{n}One old woman by the fire does not sing. There is a faded Desnan star stitched on her shawl. She leans over the King's shoulder, reads the sheet, and goes white.{/n} {n}"Those aren't the words," she says, to nobody. "I sang it in Kenabres." She leaves without finishing her cup.{/n}''',
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
    nar("start", '''{n}There is no King left to sing to, and no tavern of his to sing in. The worst camp tavern in Drezen is full of sappers and quartermasters, and the one Desnan song half of them know is Starward Gaze, hummed wherever the words run out. Nobody in the room has heard of Thaberdine.{/n}''',
        c(JOKE, "reply", mythic="Trickster", crusade=("Finances", -150)),
        c('[Leave them to their beer.]', abort=True)),
    nar("reply", '''{n}You climb onto a table, pay for every mug in the house, and teach a room full of sappers and quartermasters Starward Gaze with a second verse of your own. Nobody in the room has heard of Thaberdine. You rhyme him with 'tambourine' anyway.{/n}
{n}You keep them singing all night, until the tavern has almost no beer left. In the grey of the morning somebody has chalked your verse under the Desnan broadsheet the refugees nailed by the door last spring, 'tambourine' and all, and underlined it twice. By noon the carters on the north road have it, and most of the people who learn it from them never knew it without the verse.{/n}
{n}That evening a letter comes back down the north road with a returning carter, in a round, flourishing hand that has pressed hard enough to tear the paper in two places.{/n}''',
        c("Continue", "reply_known", requires=(GAVE_SONG,)),
        c("Continue", "reply_unknown", forbids=(GAVE_SONG,))),
    a("reply_known", '''"Somebody has changed my song! The carters came into our camp this noon singing Starward Gaze with a verse I never wrote, and they all swear it was always sung that way, and it wasn't, and it's better, which is the worst part!"
"It came to us from the true servants of Desna, from her domain in Elysium, and I carried it out of Kenabres in one piece. I gave it to you in one piece, Commander, to remember, not to improve. The carters say it started in Drezen. I am coming to Drezen to find the thief."
{n}The driver brought more than her letter. Aranka rode back beside him, her lute wrapped against the dust. She is unloading her bag in Drezen now, asking which stall sells charcoal and where the Commander has hidden.{/n}''',
      *her_letter_choices(PRIMED, LATE)),
    a("reply_unknown", '''"To the Knight-Commander of Drezen, from Aranka, who sings for Desna and would like a word."
"Somebody has changed my song! The carters came into our camp this noon singing Starward Gaze with a verse I never wrote, and they all swear it was always sung that way, and it wasn't, and it's better, which is the worst part! The carters say it started in your city, in a tavern, with somebody paying for the beer. I am coming to Drezen to find the thief. Please have them ready."
{n}The driver brought more than her letter. Aranka rode back beside him, her lute wrapped against the dust. She is unloading her bag in Drezen now, asking which stall sells charcoal and where the Commander has hidden.{/n}''',
      *her_letter_choices(PRIMED, LATE)),
], requires=("trickster",), forbids=(PRIMED, ROMANCE, FAILURE, CROWNED), delay=0, **NO_KING_GATE)
# The act is performed on the page now, and dearer than the King's round; her reply is folded in so the route spends
# one letter, and its answers record the primer and the late cost as well (R2-2).

letter("aranka.trickster.verse.her_letter", "Somebody changed my song", [
    nar("start", '''{n}The letter is in a round, flourishing hand that has pressed hard enough to tear the paper in two places. It smells faintly of road dust and lamp oil, and someone has used it as a coaster.{/n}''',
        c("Continue", "known", requires=(GAVE_SONG,)),
        c("Continue", "unknown", forbids=(GAVE_SONG,))),
    a("known", '''"Somebody has changed my song! Everyone swears it was always sung that way, and it wasn't, and it's better, which is the worst part! A tavern king in Drezen is telling the whole city his pops learned it from a Desnan girl with a voice like a lark, and the whole city has decided the girl was me. I have never met his pops. I have never met him. Old Marit heard it in his tavern and begged a seat on the next supply wagon out to tell me. She says he has his pops' song-sheet with your verse scrawled into it in charcoal, and swears on his pops' tankard it was always there. She was crying, and I could not tell whether it was the good kind."
"It came to us from the true servants of Desna, Commander. I carried it out of Kenabres in one piece and I put it into your hands in one piece. I did not ask you to rhyme it with a tambourine. I am coming to Drezen to find the thief."
{n}The driver brought more than her letter. Aranka rode back beside him, her lute wrapped against the dust. She is unloading her bag in Drezen now, asking which stall sells charcoal and where the Commander has hidden.{/n}''',
      *her_letter_choices()),
    a("unknown", '''"To the Knight-Commander of Drezen, from Aranka, who sings for Desna and would like a word."
"Somebody has changed my song! Everyone swears it was always sung that way, and it wasn't, and it's better, which is the worst part! A tavern king in your city is telling everyone his pops learned it from a Desnan girl, and everyone has decided the girl was me. I have never met his pops. I have never met him. Old Marit, one of our pilgrims, heard it in his tavern and begged a seat on the next supply wagon out to tell me. She says he has an old song-sheet with the new verse scrawled into it, and that the verse arrived the night a Knight-Commander stood on a bench and paid for the beer."
"I am coming to Drezen to find the thief. Please have them ready."
{n}The driver brought more than her letter. Aranka rode back beside him, her lute wrapped against the dust. She is unloading her bag in Drezen now, asking which stall sells charcoal and where the Commander has hidden.{/n}''',
      *her_letter_choices()),
], requires=("trickster.ever", PRIMED), forbids=(ANSWERED, ROMANCE, FAILURE), delay=72)


# --- In person, busking in the market (R2-1, R2-3) ----------------------------------------------------------------------

counter("aranka.trickster.verse.duet", "Second verse, the good one", '"You wanted the thief. Here I am."', [
    nar("start", '''@OPEN@
{n}The woman on @SEAT@ is in Desnan blue, road-dusty to the knee, with a lute across her lap and a cup of the worst wine in Drezen she has not touched. Every head within earshot is turned towards her, and she knows it, and she is enjoying it more than she would ever admit.{/n}
{n}Beside @STAGE@, a visiting Nerosyan troupe-master listens with the soldiers. Her players have come to entertain the garrison; she stays when their wagon leaves.{/n}''',
        c("Continue", "mocking", requires=(MOCKING,)),
        c("Continue", "posters", requires=(ANNOUNCED,), forbids=(MOCKING,)),
        c("Continue", "denied", requires=(DENIED,), forbids=(MOCKING, ANNOUNCED)),
        c("Continue", "vandal", forbids=(MOCKING, ANNOUNCED, DENIED))),
    a("vandal", '''"You! Oh, you wonderful vandal."
{n}She presses both hands to her cheeks, and then remembers she is angry and puts them back on the lute.{/n}
"There is no rhyme for Thaberdine. I tried, you know. Afterwards. I sat up two nights. There wasn't one, until you, and now there is, and it's 'tambourine', and I will never get it out of my head as long as I live."''',
      c('[Sing it] "I am sorry. Second verse. The good one."', "duet", forbids=(CONTEST_WON,)),
      c('[Sing it] "I am sorry. Second verse. The good one."', "duet_rival", requires=(CONTEST_WON,))),
    a("denied", '''"The Desnans, you said." {n}She does not smile.{/n} "I am the Desnans. Three camps and a ferryman pointed me at you, Commander, and the ferryman did an impression."
"So. You never heard it. Sing it for me, then. The second verse. If you can't, I'll know you lied once. If you can, I'll know you lied twice."''',
      c('[Sing it] "I am sorry. Second verse. The good one."', "duet", forbids=(CONTEST_WON,)),
      c('[Sing it] "I am sorry. Second verse. The good one."', "duet_rival", requires=(CONTEST_WON,))),
    a("mocking", '''{n}She sees you coming and lifts the lute off @SEAT@ to make room beside her.{/n}
"You came back. Good! I've been trying to decide whether the banner should trip you once or twice. Twice is funnier, but you have to breathe somewhere."
{n}She tries the phrase, stops, and shakes her head.{/n}
"I have never sung Starward Gaze with words of yours in it. Tonight it gets a second verse, and you're going to make it up, here, out of the one where you lose: the banner, the trip, the demons laughing, all of it turned round. Then I'll take the harmony, and we'll see whose song it is."
"Come on, join in! This time I'll catch you before the fall. In the song, at least."''',
      c('[Sing it] "I am sorry. The banner verse, turned round. From the top."', "duet", forbids=(CONTEST_WON,)),
      c('[Sing it] "I am sorry. The banner verse, turned round. From the top."', "duet_rival", requires=(CONTEST_WON,))),
    a("posters", '''"You put me on a poster before you put me in a letter." {n}She presses a torn corner of one into your palm: KNIGHT-COMMANDER'S COURT POET, and half of TONIGHT.{/n}
"You billed a song, Commander, so now you will have to earn the billing. Starward Gaze came to us from the true servants of Desna. If you want your name near it, you'll add a verse to it yourself. Here. In front of all of them. And then I'm going to decide how badly you did it."''',
      c('[Sing it] "I am sorry about the posters. A second verse. Mine."', "duet", forbids=(CONTEST_WON,)),
      c('[Sing it] "I am sorry about the posters. A second verse. Mine."', "duet_rival", requires=(CONTEST_WON,))),
    a("duet", '''"Apology accepted. Now the duet!"
{n}She gives you the first note. You miss it. Her eyebrows go up, and then she finds whatever note you did hit, lays the harmony under it, and walks you back up to the tune a step at a time.{/n}
"There you are! Again. I shall make a singer of you yet."
{n}A sapper at the back beats time on his helmet. Two porters stop to listen; a third shoulders past them with a sack, complaining that the Knight-Commander has found another way to block the road. She takes the hard turn in the middle herself and leaves you the last rhyme.{/n}
{n}The sapper starts clapping before the chord is finished. She holds it a little longer, eyes closed, and makes him wait. The troupe-master joins the applause.{/n}
"My name goes first every time it's sung. Yours comes after. Quietly. Very quietly."''',
      c('[Take the harmony, not the credit] "Yours first. Mine after, quietly."', "signed"),
      c('[Argue the billing] "Put mine first. It\'s my verse."', "billing")),
    a("signed", '''"Good." {n}She turns to the crowd and gives them the song's name and her own, clear as a bell, and then yours, into her cup, so quietly the front row has to lean in to catch it.{/n}
"I'm singing it in every camp between here and the river. Every night. I'll decide each morning whether to come back and tell you how it went."
{n}She leans close, lowering her voice beneath the crowd's applause.{/n} {n}Her eyes stray to your mouth.{/n} "I know very well who I want to kiss. That duet is paid. Next time, I want you singing beside me again. If the war takes you away, leave me your road. I can find an inn."''',
      c('"I\'ll be here. If I take the road, I\'ll leave you the route."', flags=(DUET, CREDITED))),
    a("billing", '''"Your verse." {n}She laughs, delighted and not at all moved.{/n} "Your verse is a bad rhyme and a great deal of nerve, Commander. My name goes first. Argue with me again and it goes first in capitals."
{n}She tells the crowd both names anyway, hers twice and loud, yours once and into her sleeve.{/n}
"I'm singing it in every camp between here and the river. Every night. I'll decide each morning whether to come back and tell you how it went."
{n}She leans close, lowering her voice beneath the crowd's applause.{/n} {n}Her eyes stray to your mouth.{/n} "I know very well who I want to kiss. That duet is paid. Next time, I want you singing beside me again. If the war takes you away, leave me your road. I can find an inn."''',
      c('"I\'ll be here. If I take the road, I\'ll leave you the route."', flags=(DUET, VAIN))),
    # Audit pol3 (VOI): the bard who outsang her in the Count's parlour (Cue_15) is no pupil; she makes it a contest again.
    a("duet_rival", '''"Apology accepted. Now the duet!"
{n}She looks at you properly, and you watch her place you: the Count's parlour, the bard who outsang her with the demons hardly cold on the carpet.{/n} "Oh, it's you! Then you take the tune, and don't you dare show off."
{n}You take the tune. She shows off. She climbs over your line in the second verse, throws in a run nobody wrote, and dares you with her eyebrows to follow it. A sapper at the back beats time on his helmet; a porter with a sack complains that the Knight-Commander has found another way to block the road. On the last rhyme she gives you the note and takes the harmony a third above it, so that nobody can say afterwards whose note it was. The troupe-master joins the applause.{/n}
"My name goes first every time it's sung. You had your victory in Kenabres. This one's mine."''',
      c('[Take the harmony, not the credit] "Yours first. Mine after, quietly."', "signed"),
      c('[Argue the billing] "Put mine first. It\'s my verse."', "billing")),
], requires=("trickster.ever", ANSWERED), forbids=(CLOSED, DUET), delay=72)


def night_nodes():
    """The intimate beat after the commit (Directive 12): the threshold, the cut at the start of the act, the morning."""
    return [
        nar("threshold", '''{n}@ROOM@ She does not seem to notice either. She sets the lute against the wall and turns round, and her breathing has gone the way it goes before a high note she is not sure of: short, high in the chest, held.{/n}
{n}She kisses you the way she sings, all breath and no hurry, and hums against your mouth when you pull her closer, a low, rising phrase you feel in your own chest before you hear it. The Desnan blue comes off over her head. She is warm as a hearth underneath it, and she takes your hands and sets them on her where she wants them, and makes a small sound, and holds them there.{/n}
{n}"Count me in," she whispers, and pulls you down onto her cloak spread over the sun-warm tiles, under more of Desna's stars than Drezen has shown anyone all year, and hums the second verse against your throat, loses the tune halfway and does not go back for it, and climbs onto you.{/n}''',
            c("Continue", "morning")),
        nar("morning", '''{n}@HOUSE@ wakes to her singing from the roof, something new and unfinished that stops and starts again, and by the time you come down the @DOWN@ @CROWD@ is very busy looking at the sky.{/n}
{n}@BILL@: a fine for "singing on a roof after the bell", and a line at the bottom that only says "Also the other noise." Aranka reads it over your shoulder, laughs until she has to sit down on the step, and pays it herself.{/n} "Don't you dare take it off the war chest. I earned every copper of that."''',
            c('[Keep the bill.]', flags=(NIGHT,))),
    ]


counter("aranka.trickster.verse.encore", "An offer from Nerosyan", '"You came back again."', [
    nar("start", '''{n}She is on @SEAT@ again, lute across her knees, with a letter in her hand that has a Mendevian seal on it. She has read it enough times to soften the folds.{/n}''',
        c("Continue", "offer")),
    a("offer", '''"A troupe in Nerosyan wants me. A real stage, a real hall, a hundred people a night who have paid to sit still. Their troupe-master heard our duet here. She brought me this invitation herself this morning. They want Starward Gaze, the new one. With your verse."
{n}She looks at the letter, and then at you, and then at the letter.{/n}
"I went round the camps these last few nights. I sang it in all of them. The pikemen at the ford made me sing it three times and then sang it back to me wrong. And every night I came back here. I haven't decided why."''',
      c("Continue", "vain", requires=(VAIN,)),
      c("Continue", "denied", requires=(DENIED,), forbids=(VAIN,)),
      c("Continue", "lovers", requires=(ROMANCE,), forbids=(VAIN, DENIED)),
      c("Continue", "choice", forbids=(VAIN, DENIED, ROMANCE))),
    a("vain", '''"And before you say it: no, the Nerosyan bill does not put your name first either. I asked. They laughed. I liked them for it."''',
      c("Continue", "choice")),
    a("denied", '''"You lied to me about the verse, the first time. I'll sing it anyway. And every time I do, I'll tell them who lied about it."''',
      c("Continue", "choice")),
    a("lovers", '''"The last time I went, you let me go, and I sang the whole road north pretending that was what I wanted." {n}Her thumb worries the edge of the seal.{/n} "I'm a very good singer, Commander. I'm a terrible liar. Ask the road."''',
      c("Continue", "choice")),
    a("choice", '''"So tell me, Commander. Is there a reason to stay that isn't a song?"''',
      c('[Ask her to stay] "Stay. Sing it with me. Every night we get."', "stay", flags=(KEPT,)),
      c('[Charm her] "Stay, and I\'ll rhyme you anything."', "not_yet"),
      c('[Tell her to take the stage] "Go. Let them hear you in Nerosyan."', "stage", flags=(CLOSED, NEROSYAN))),
    a("not_yet", '''"That's a pretty line." {n}She folds the Mendevian letter very small, and then smaller.{/n}
"Too pretty. You gave a crowd a verse. So I'm going to write one. For you. When I sing it, you'll know what I'm asking, and I'll know what you answer. Not tonight."''',
      c('[Let her write it] "Then I\'ll listen for it."', flags=(DECLINED,))),
    a("stage", '''{n}She says nothing while the crowd around you orders another round and forgets to drink it. When she speaks, her voice is steady, and it costs her.{/n}
"That's the kindest thing you could have said, and I hate it." {n}She tucks the Mendevian letter into her bodice and stands, and settles the lute on her back.{/n}
"I'll sing your verse every night. And every night I'll tell them who wrote it. In small letters."''',
      c('"Go on. They\'re waiting."')),
    a("stay", '''{n}She studies you the way she studied the crowd before the duet, as if she were deciding how it will sound.{/n}
"Every night we get." {n}She drops the Mendevian letter into @STOVE@ without looking at it.{/n} "That's a better line than the verse. I'm stealing it."''',
      c("Continue", "threshold")),
    *night_nodes(),
], requires=("trickster.ever", DUET), forbids=(CLOSED, KEPT, DECLINED), delay=72)

counter("aranka.trickster.verse.third_verse", "The third verse", '"You said you were writing something."', [
    a("start", '''{n}She has cleared a space on @STAGE@, and the whole crowd is watching, and she has made sure of that. She does not look at you once while she sings.{/n}
"I have sung for the clouds and I've sung for the rain,
I have walked every road there and back again.
I have one verse left over and nowhere to stay,
So sing me a reason, or sing me away."
{n}She lifts her hand off the strings on the last word and lets it hang in the air, unanswered, and waits.{/n}
"That one's yours to rhyme. Out loud. Alone."''',
      c('[Finish the verse alone] "...Everybody, quiet. Then stay. I\'ll sing it out loud, and badly, every day."', "sung", flags=(KEPT, SANG_ALONE)),
      c('[Let the rhyme hang] "...I can\'t."', "refused", flags=(CLOSED,))),
    nar("sung", '''{n}You finish it alone. Your voice cracks on the rhyme. A sergeant at the back laughs out loud, and Aranka turns her head and looks at him, once, and he stops. She keeps the beat for you with her heel and leaves the last word where it is, for you to reach.{/n}
{n}When you reach it, somebody calls for it again. Aranka shakes her head so hard that the lute knocks against her knee. Then she puts it down on @STAGE@ and comes to you.{/n}''',
        c("Continue", "answer")),
    a("answer", '''{n}She is crying, and furious about it, and laughing.{/n} "That was terrible. That was the worst line anyone has ever sung to me. Say your name before it next time, loud, so they all know whose it is. And yes. Obviously yes."''',
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
        nar("loud", '''{n}You climb onto the bench and lead it. You sing the banner verse louder than anyone, and trip over an imaginary banner on the rhyme, and the tavern howls. By the third round they are singing it with you, not at you, and by the fifth they are pounding their mugs on the tables to demand it again.{/n}''',
            c("Continue", "after")),
        king("after", '''"Now THAT'S a king!" {n}Thaberdine wipes his eyes.{/n} "You fell right on the rhyme! I didn't even spill my beer. Let's have the one with the banner again!"''',
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
{n}There is no King's tavern left to lead it in. The worst camp tavern in Drezen is full tonight, and somebody at the back is already humming the banner verse under his breath.{/n}''',
        c(FAILURE_JOKE, "reply", mythic="Trickster", crusade=("Finances", -150)),
        c('[Leave them to it.]', abort=True)),
    nar("reply", '''{n}You pay for every mug in the house, climb onto a table and lead it until dawn, tripping over an imaginary banner on every rhyme. By noon the carters have taken it up the north road, singing the banner verse and laughing at the fall.{/n}
{n}That evening a letter comes back down the north road, in a round hand you know, with a blot in the middle as if the writer stopped for a long while.{/n}''',
        c("Continue", "her_reply")),
    a("her_reply", '''"You sang the verse where you lose. Out loud, on purpose! The carter who brought this tried to show me the fall and nearly put his boot in our supper."
"But I didn't leave you because you were a poor sport, Commander. I left because you told me evil was necessary. That is the kind of thinking that lets people like Hulrun murder innocent people, and a drinking song hasn't changed my answer."
"I am coming to Drezen. You may sing when I have finished talking."
{n}The returning wagon brought its writer too. Aranka climbed down at the capital gate with the letter still unsealed. She has gone to find the Desnan pilgrims among the carters; the lute stays wrapped.{/n}''',
        c('[Answer her] "Come and decide."', flags=(PRIMED, LATE, MOCKING, RETURNED, ANSWERED, STARTED))),
], requires=("trickster", FAILURE), forbids=(PRIMED, CROWNED), delay=0, **NO_KING_GATE,
   TricksterDevice=True, TricksterState=FAILURE)

letter("aranka.trickster.failure.second_verse", "A blot in the middle", [
    a("start", '''"I heard what you did in the King's tavern. You sang the verse where you lose, out loud, on purpose, and you made them sing it louder. Oh, I wish I had been there for the banner!"
{n}A blot, as if she stopped writing for a while. Below it the hand starts again, smaller and harder.{/n}
"But I didn't leave you because you were a poor sport, Commander. I left because you told me evil was necessary. That is the kind of thinking that lets people like Hulrun murder innocent people, and a drinking song hasn't changed my answer."
"I am coming to Drezen. You may sing when I have finished talking."
{n}The returning wagon brought its writer too. Aranka climbed down at the capital gate with the letter still unsealed. She has gone to find the Desnan pilgrims among the carters; the lute stays wrapped.{/n}''',
      c('[Answer her] "Come and decide."', flags=(RETURNED, ANSWERED, STARTED))),
], requires=("trickster.ever", FAILURE, PRIMED, MOCKING), forbids=(RETURNED, ANSWERED), delay=72, TricksterDevice=True, TricksterState=FAILURE)


# --- State parent_done_non_azata: billed before she was asked (F05) ------------------------------------------------

letter("aranka.trickster.touring.boast", "Court poet", [
    nar("start", '''{n}Aranka is at a pilgrims' camp near the first ford, singing for pikemen. You have not seen her since your story together reached its end, and she has not written. The crusade's printers, on the other hand, owe you a favour.{/n}''',
        c(TOURING_JOKE, "posters", mythic="Trickster", crusade=("Finances", -100)),
        c('[Let her keep her road.]', abort=True)),
    nar("posters", '''{n}By morning every wall in Drezen carries a poster: STARWARD GAZE, SUNG BY THE KNIGHT-COMMANDER'S COURT POET, TONIGHT. The paste is still wet. The printers spelled her name right on the first try, because you stood over them.{/n}
{n}Aranka has agreed to nothing. You send a mounted courier to the ford with a roll of posters, directions to her camp and orders to bring back her answer. By nightfall he is back without one, and Aranka is riding beside him. She dismounts at the citadel gate, reads the poster pasted to the gatepost, and will not say a word to anyone from the citadel.{/n}''',
        c('"Let her read it. She can shout when she\'s ready."', flags=(PRIMED, ANNOUNCED))),
], requires=("trickster", ROMANCE, QUEST), forbids=(PRIMED, "azata", FAILURE), delay=0)

counter("aranka.trickster.touring.arrives", "Court poet", '"You came."', [
    a("start", '''{n}She is standing by @SEAT@ with a poster half torn off the wall in her fist. She spent two days reading your boasts before coming here, and has not let anyone fetch you.{/n}
"Court poet. I have never been anybody's court anything. I came here to shout at you in person, because a letter wouldn't be loud enough, and because I wanted to see your face when I did it."''',
      c('"Then shout."', "shout"),
      c('"You spelled it right. I checked."', "shout")),
    a("shout", '''"I am. This is shouting. I'm a singer, I don't have to be loud to be shouting." {n}She smooths the poster out against her knee, and reads it again, and something in her face gives way.{/n}
"...It's a very good poster. You spelled my name right. Nobody spells my name right."
"Fine. One night. I sing. You listen, like everyone else. Court poet! Next you'll be ordering my songs by the yard, in capital letters."''',
      c('[Take her at her word] "One night. You sing. I listen."', flags=(ANSWERED, STARTED))),
], requires=("trickster.ever", PRIMED, ROMANCE, ANNOUNCED), forbids=(ANSWERED, "azata"), delay=48)


# --- Epilogue pages (R2-6; ordered siblings, no page effects) -------------------------------------------------------

VERSE_PARAGRAPHS = (
    p("{n}She sang the thief's verse herself, to the end of her days, and before it she always told the hall that the "
      "thief had said it must be the Desnans. The halls always laughed. The Commander never did.{/n}", requires=(DENIED,)),
    p("{n}The third verse, the one Aranka wrote as a question and the Knight-Commander answered alone and badly, is printed under the other two "
      "in every copy. It has never once been sung well. Aranka would not allow it.{/n}", requires=(SANG_ALONE,)),
    p("{n}The verse where the Knight-Commander trips over their own banner is still the most requested verse of the song.{/n}",
      requires=(MOCKING,)),
)


def thall_ending(id):
    # One terminal conclusion: late reunion owns it instead of the song slide;
    # the shared coda owns it when Last Call is active.
    guards = ["aranka.thall.coda_delivered"] if id.endswith((".commit", ".verse")) else []
    if id.endswith(".verse"):
        guards.append(LATE_COMMITTED)
    endings = {
        "declined": '{n}Aranka sent Thall the two-verse arrangement. His reply asked about the missing verse. She wrote that she had other songs to finish, and sent him one of those instead.{/n}',
        "unanswered": '{n}Aranka sent Thall songs from her travels. He returned them with the low parts marked, but declined her invitation to join the tour. She stopped asking him to perform and kept sending the songs.{/n}',
        "nerosyan": '{n}Thall declined Aranka\'s invitation to sing in Nerosyan. She sent him the arrangements instead. His corrections arrived between engagements; she complained about them and tried every one.{/n}',
    }
    return (
        p(endings.get(id.rsplit(".", 1)[-1], THALL_ENDING), requires=(THALL_ANSWERED,), forbids=(THALL_DEAD, *guards)),
        p('{n}Aranka left her letter to Thall with the Desnan pilgrims. No reply reached her before she moved on. At each stop she asked after him before unpacking her lute.{/n}', requires=(THALL_REQUESTED,), forbids=(THALL_ANSWERED, THALL_DEAD, *guards)),
        dict(THALL_MEMORY, Forbids=guards),
    )


def page(id, title, text, requires, forbids=(), paragraphs=(), **extra):
    # Polish (R2-6): Chapter 6 only, in the data as well as through the native epilogue attachment.
    SCENES.append(scene(id, title, "Epilogue", 6, "", [nar("end", text, paragraphs=(*paragraphs, *thall_ending(id)))], requires=requires,
                        forbids=(*forbids, KENABRES_ATTACKED), last=6, Relationship="aranka", Chapters=[6], **extra))


page("aranka.trickster.epilogue.commit", "The last night in Nerosyan",
     '''{n}After Threshold Aranka took the Nerosyan stage for one season. On its last night she announced her own next engagement: a duet with the Commander. She left with a full song satchel before the applause had finished.{/n}''', requires=("trickster.ever", LATE_COMMITTED),
     forbids=(KEPT, CLOSED, DECLINED, "sacrifice", FAILURE), paragraphs=(
         p("""{n}The night mail-coach brought her to Drezen, dusty to the knee. She found the Commander under a lamp, writing requisitions, sat on the papers and took the pen away. Her mouth caught the beginning of a protest. She put the Commander's hand on her bodice lacing and pulled the knot loose.{/n}""", requires=(COMMANDER_STAYS,), forbids=(COMMANDER_LEAVES,)),
         p("""{n}The Commander had left Mendev. Aranka followed the itinerary they had agreed on before the final march and caught up at a roadside inn. She dropped her satchel beside the luggage, pushed the travel map off the table and kissed the Commander before the road dust had settled. Her fingers found the bodice knot; she pulled it loose herself.{/n}""", requires=(COMMANDER_LEAVES,)),
         p("""{n}Aranka found the Commander at their agreed lodging with a satchel full of songs and no patience for introductions. She put the lute down safely, took the Commander's hands and kissed away the first question about Nerosyan.{/n}""", forbids=(COMMANDER_STAYS, COMMANDER_LEAVES)),
         # User-supplied reunion insertion: her chosen return, road dust, wanted intimacy.
         dict(p("""{n}She drew the Commander down after her by the collar. The songs spilled unopened onto the floor. At dawn, Aranka retrieved her satchel and began to sing.{/n}"""), Id='aranka.trickster.epilogue.commit.explicit.1'),
         p("""{n}The north-wall sentries learned the new tune by week's end. Aranka took it to the camp survivors herself, and came back that evening to demand the Commander's harmony.{/n}""", requires=(COMMANDER_STAYS,), forbids=(COMMANDER_LEAVES,)),
         p("""{n}The innkeeper learned the new tune before breakfast. Aranka packed her songs with the Commander's map and insisted on singing the steepest stretch of their next day's road.{/n}""", requires=(COMMANDER_LEAVES,)),
         *VERSE_PARAGRAPHS,
     ), ForbidOverrides={"sacrifice": "trickster.commander_back", FAILURE: MORAL_REPAIRED})

page("aranka.trickster.epilogue.declined", "Two verses",
     '''{n}The third verse was never written. Aranka sang Starward Gaze for the rest of her life with two verses, and at the end of the second she always stopped, and waited a heartbeat, as though somebody in the back of the hall might still stand up and sing.{/n}''',
     requires=("trickster.ever", DECLINED), forbids=(KEPT, CLOSED))

# Q8 (Sol BEL): the hard no after the third verse was sung. The verse exists; only its last rhyme was never answered.
page("aranka.trickster.epilogue.unanswered", "The hanging rhyme",
     '''{n}For a few years Aranka sang the third verse in every hall that would have her, and at its last line she let the rhyme hang a heartbeat too long before she went on. Then one night in Nerosyan a tenor tried to finish it for her, flat, and she laughed, corrected his pitch from the stage, and sang it with his line in it after all.{/n}
{n}She took the road again that spring, south and then west, collecting songs the way other pilgrims collect relics: a lullaby from a Mendevian ferryman, a drinking round from the Absalom docks, a hymn to Desna nobody in the north had heard. She did not travel alone for long. Starward Gaze stayed in her repertoire with three verses, and it was never again the last song of the night.{/n}''',
     requires=("trickster.ever", DECLINED, CLOSED), forbids=(KEPT,), paragraphs=VERSE_PARAGRAPHS)

page("aranka.trickster.epilogue.verse", "Two names",
     '''{n}Starward Gaze outlived the crusade. Every printed arrangement carries two names: hers first, in a hand like a lark on a wire, and underneath, in letters so small you need a candle, the Commander's.{/n}''',
     requires=("trickster.ever",), forbids=(CLOSED, DECLINED, FAILURE), paragraphs=VERSE_PARAGRAPHS,
     RequiresAnyGroups=[[KEPT, LATE_COMMITTED]], ForbidOverrides={DECLINED: KEPT, FAILURE: MORAL_REPAIRED})

page("aranka.trickster.epilogue.nerosyan", "Twenty years on a stage",
     '''{n}Aranka took the Nerosyan stage and kept it for twenty years. She sang the Commander's verse every night, and every night she said who wrote it. In small letters, she always added. Very small.{/n}''',
     requires=("trickster.ever", NEROSYAN))


# --- Reactions (ledger 05 section 3.1 row 3: exactly Anevia, Woljif and Lann) --------------------------------------

ANEVIA_GUARD = dict(ForbidOverrides={"anevia_gone": "anevia.trickster.returned"})
WOLJIF_GONE = ("woljif.dead", "woljif.kicked_out")
LANN_GONE = ("lann.dead", "lann.kicked_out")

REACTIONS = [
    reaction("Anevia", "aranka.trickster.react.anevia_verse", (PRIMED,),
             '''"Half the garrison's singing that star song wrong. Beth's humming it on watch. Honestly." {n}Anevia shakes her head, and hums two bars of it before she can stop herself.{/n} "I'm blaming you."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "irabeth_dead", MOCKING), chapter=3, last=5, Chapters=[3, 5],
             entry='"Something wrong with the garrison?"', RequiresAnyGroups=[[ROUND, CREDITED, DENIED]],
             ForbidOverrides={"anevia_gone": "anevia.trickster.returned", "irabeth_dead": "irabeth.trickster.returned"}),
    reaction("Anevia", "aranka.trickster.react.anevia_verse_alone", (PRIMED, "irabeth_dead"),
             '''"Half the garrison's singing that star song wrong." {n}Anevia looks at the wall, at the place where the night watch used to stand.{/n} "I caught myself humming it up there last night. Don't. I'm blaming you, that's all."''',
             answer_list=ANEVIA_HUB, forbids=("anevia_gone", "irabeth.trickster.returned", MOCKING), chapter=3, last=5,
             Chapters=[3, 5], entry='"Something wrong with the garrison?"', RequiresAnyGroups=[[ROUND, CREDITED, DENIED]],
             **ANEVIA_GUARD),
    reaction("Woljif", "aranka.trickster.react.woljif_billing", (DUET,),
             '''"Chief, there's copies going round. Her name up top, big as a barn, and yours underneath in letters so small I had to lick my thumb to read 'em." {n}Woljif grins.{/n} "I'm charging people a copper to see the fine print."''',
             answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
             entry='"You look pleased with yourself."'),
    reaction("Woljif", "aranka.trickster.react.woljif_mocking", (MOCKING,),
             '''"Chief, they're singing the one where you trip over your own banner." {n}Woljif looks genuinely shaken.{/n} "You LED it. That's the part I don't get. I'd have found somewhere else to drink."''',
             answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
             entry='"Something on your mind?"'),
    reaction("Lann", "aranka.trickster.react.lann_verse", (ANSWERED,),
             '''"The whole camp knows your verse now." {n}Lann shrugs.{/n} "It's a terrible rhyme. I'll only sing it when you're winning."''',
             answer_list=LANN_HUB, forbids=(*LANN_GONE, MOCKING), chapter=3, last=5, Chapters=[3, 5],
             entry='"Heard any good songs lately?"', RequiresAnyGroups=[[ROUND, CREDITED, DENIED]]),
]
SCENES.extend(REACTIONS)


# --- Chapter 5 twins (polish, R2-6 seven-day window) ------------------------------------------------------------------
# After the Coronation the chain must fit inside a week, so the Chapter 3 beats keep their ids, prose and 72/48-hour
# clocks but close at Chapter 3, and each gains an appended Chapter 5 twin on a 24-hour clock: a deep copy with the
# same relationship, gates, device metadata, nodes, choice order, effects and venue. Shared progress flags (answered,
# duet_sung, declined, kept) carry across the chapter boundary; each twin also Forbids its original's id, so a save that
# finished the original in Chapter 5 before this split never replays it. Only travel lines that a day cannot carry change.
LATE_DELAY = 24
LATE_TEXT = {
    # her letter: Marit rides the dawn wagon out to a camp a day away, and the driver carries the answer back
    ("aranka.trickster.verse.her_letter", "known"): (
        "Old Marit heard it in his tavern and begged a seat on the next supply wagon out to tell me. She says",
        "Old Marit heard it in the King's tavern and rode the dawn supply wagon out to our camp at the first ford to tell me; its driver is carrying this back. Marit says"),
    ("aranka.trickster.verse.her_letter", "unknown"): (
        "Old Marit, one of our pilgrims, heard it in his tavern and begged a seat on the next supply wagon out to tell me. She says",
        "Old Marit, one of our pilgrims, heard it in the King's tavern and rode the dawn supply wagon out to our camp at the first ford; its driver is carrying this back. Marit says"),
    # the encore: one night at the ford, not a week of camps
    ("aranka.trickster.verse.encore", "offer"): (
        "\"I went round the camps these last few nights. I sang it in all of them. The pikemen at the ford made me sing it three times and then sang it back to me wrong. And every night I came back here. I haven't decided why.\"",
        "\"I sang it at the ford last night. The pikemen made me sing it three times and then sang it back to me wrong. I could have slept there. I came back on a wagon full of turnips instead. I haven't decided why.\""),
    # the touring arrival: the courier brought her in the night the posters went up, not two days before
    ("aranka.trickster.touring.arrives", "start"): (
        "{n}She is standing by @SEAT@ with a poster half torn off the wall in her fist. She spent two days reading your boasts before coming here, and has not let anyone fetch you.{/n}\n\"Court poet.",
        "{n}She is standing by @SEAT@ with a poster half torn off the wall in her fist. The torn edge is still tacky with paste.{/n}\n\"Court poet!"),
}


def late_twin(source_id):
    """Close a Chapter 3/5 beat at Chapter 3 and append its Chapter 5 twin (deep copy, 24-hour clock)."""
    source = next(s for s in SCENES if s["Id"] == source_id)
    twin = copy.deepcopy(source)
    source.update(MinChapter=3, MaxChapter=3, Chapters=[3])
    twin.update(Id=source_id + "_late", MinChapter=5, MaxChapter=5, Chapters=[5], DelayHours=LATE_DELAY)
    twin["Forbids"].append(source_id)
    base = source_id[:-len("_yard")] if source_id.endswith("_yard") else source_id
    place = "yard" if source_id.endswith("_yard") else "fye"
    for node in twin["Nodes"]:
        change = LATE_TEXT.get((base, node["Id"]))
        if change:
            old, new = change
            old = fit(old, place)
            if old not in node["Text"]:
                raise ValueError("late twin %s: the travel line moved in node %s" % (twin["Id"], node["Id"]))
            node["Text"] = node["Text"].replace(old, fit(new, place))
    SCENES.append(twin)


for _id in ("verse.her_letter", "verse.duet", "verse.duet_yard", "verse.encore", "verse.encore_yard", "verse.third_verse",
            "verse.third_verse_yard", "failure.second_verse", "touring.arrives", "touring.arrives_yard"):
    late_twin("aranka.trickster." + _id)


# --- The reckoning (coordinator ruling 2026-10-02, item 1) ------------------------------------------------------------
# The parent failure was her moral refusal ("Evil is never a necessity"), not wounded pride. The song brings her to
# Drezen; only this in-person answer, a new deed with a real price, reopens the courtship (MORAL_REPAIRED). Holding the
# old justification closes the route by the player's choice; deferring leaves the reckoning open. Old saves holding the
# legacy RETURNED (even with KEPT) play this before courtship resumes; earned flags are never cleared.
counter("aranka.trickster.failure.reckoning", "Necessary", '"You said you had something to say to me."', [
    a("start", '''{n}Aranka has put the lute down on @SEAT@ and is standing between a Desnan pilgrim and a crusade carter. The pilgrim, an old man with a star stitched on his sleeve, holds a sack of meal shut with both hands. The carter holds a requisition with the crusade's seal on it and looks as if he would rather be anywhere else.{/n}
"The army needs his meal. It says so on the paper. Necessary." {n}She looks at you, not at the carter.{/n}
"I keep hearing that word, Commander. The last time you said it to me I couldn't bear to stay in the same room with you. Have you come to say it again, with a better tune?"''',
      c('[Strike out the requisition] "What I defended was evil. Let him keep his meal. The crusade will buy its own."', "bought",
        crusade=("Finances", -200), alignment=("Good", 1)),
      c('"It was necessary then. It is necessary now."', "unchanged"),
      c('"I\'ll come back when I have an answer worth hearing."', abort=True)),
    a("bought", '''{n}You strike the requisition through and write an order to buy the meal at market price instead. The carter reads the sum back to you twice before he believes it. The pilgrim takes his sack away without thanking anyone, which Aranka seems to think is exactly right.{/n}
"There! He keeps his supper, and your soldiers will have theirs. Let the carter carry your order instead of the pilgrim's sack."
{n}She picks up the lute and rests her hand on its neck without sounding a string.{/n}
"I haven't forgotten what you said. I don't think I ever will. But I heard what you said today, too. So I'll hear you sing again, and we'll see whether you remember it when there's nobody here to applaud."''',
      c('"Then I\'ll sing. And the meal stays his."', flags=(RETURNED, MORAL_REPAIRED, PROVISIONS))),
    a("unchanged", '''"Then you've given me your answer." {n}For once she has nothing to add to it.{/n} "Oh, Commander. I did hope for a different one."
{n}She settles the lute on her back and goes after the pilgrim. This time she leaves without singing.{/n}''',
      c('"Go, then."', flags=(CLOSED,))),
], requires=("trickster.ever", FAILURE, MOCKING, ANSWERED), forbids=(MORAL_REPAIRED, CLOSED, KENABRES_ATTACKED), delay=0,
    TricksterDevice=True, TricksterState=FAILURE)


# Audit polr4 (BEL, Directive 12): a companion answers the night itself, not the song. Woljif (an allotted reactor, ledger
# 05 3.1) runs the camp's rumours for coin; the fine for "the other noise" is exactly the kind of news he trades in.
SCENES.append(reaction("Woljif", "aranka.trickster.react.woljif_roof", (NIGHT,),
    '''"Chief. Word is somebody paid a fine this morning for singing on a roof after the bell. And for 'the other noise'." {n}Woljif studies the ceiling with great innocence.{/n} "I'm not saying I was running a book on whether the bard'd stick around. I'm saying if I was, I'd be rich today, and nobody else would."
{n}Then the grin goes, just for a moment.{/n} "She could have stayed out at the ford, Chief. She came back here. That's the part I didn't put money on."''',
    answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5], entry='"You heard something."'))


def integrate(payload):
    """Save-safe: the registered island route is untouched (no id, node or choice changed). Adds the Trickster access,
    the failure override, the presence and one Guidance sentence."""
    rel = payload["Relationships"]["aranka"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    if KENABRES_ATTACKED not in rel["UnavailableFlags"]:
        rel["UnavailableFlags"].append(KENABRES_ATTACKED)
    if NEROSYAN not in rel["UnavailableFlags"]:
        rel["UnavailableFlags"].append(NEROSYAN)
    answers = payload.setdefault("SelectedAnswers", {})
    if answers.get(KENABRES_ATTACKED, KENABRES_ATTACK_ANSWER) != KENABRES_ATTACK_ANSWER:
        raise ValueError("Conflicting binding: " + KENABRES_ATTACKED)
    answers[KENABRES_ATTACKED] = KENABRES_ATTACK_ANSWER
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    # Q8 (Sol INT): one journal text for both venues, the island continuation and a fresh Trickster meeting.
    rel["Description"] = ("Aranka sings Starward Gaze for Desna, and whatever is between us is being written the same "
                          "way: a verse at a time, wherever she happens to be singing it.")
    rel["Objective"] = "Hear Aranka sing"
    rel["Guidance"] += (" On the Trickster path, a Commander who gives Starward Gaze a second verse in a tavern, or leads "
                        "the verse where they lose, or bills her as their court poet, may meet Aranka busking by the "
                        "spice trader's stall in the Drezen market, in Chapter 3 or Chapter 5.")
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    payload.setdefault("Derived", {})[NO_KING] = [[KING_GONE]]
    payload.setdefault("SeenCues", {})[THALL_SAFE] = ["7d3c179096d67b24a962c3e77a82c416"]
    payload.setdefault("Etudes", {}).update({
        COMMANDER_STAYS: "84e00414803841e428c3d47572c7d588",
        COMMANDER_LEAVES: "7fde872463d2d2647b159a733d40ea98",
        THALL_DEAD: "49c99adbf91a0c84aaa550061a60cb19",
    })

    # The framework emits its pages after this route integrates. Change only
    # Aranka's named text surfaces through its existing partner record;
    # keep the shared source, gates, choices and every other record untouched.
    # Idempotent because make_expansion may be called repeatedly in one process.
    from storylines import lastcall_partners
    part = next(row for row in lastcall_partners.PARTNERS
                if row["key"] == "aranka" and row["rel"] == "aranka")
    part["opener"] = (
        "{n}After Threshold, Aranka took her songs through the camps the crusade had left behind. "
        "She came back with mud on her hem and a new harmony she insisted the Commander learn "
        "before hearing a single tale of the road. She put the lute between them and counted in.{/n}")
    if THALL_MEMORY not in part["paragraphs"]:
        part["paragraphs"] = (*part["paragraphs"], p(THALL_CALLBACK, requires=(THALL_ANSWERED,), forbids=(THALL_DEAD,)), THALL_MEMORY)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'aranka.trickster.failure.reckoning',
    'aranka.trickster.failure.reckoning_yard',
    'aranka.trickster.failure.second_verse',
    'aranka.trickster.failure.second_verse_late',
    'aranka.trickster.touring.arrives',
    'aranka.trickster.touring.arrives_late',
    'aranka.trickster.touring.arrives_yard',
    'aranka.trickster.touring.arrives_yard_late',
    'aranka.trickster.verse.her_letter',
    'aranka.trickster.verse.her_letter_late',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]


# Authored round-2 roof staging. Every slot returns to the original morning;
# original commitment and morning receipts remain at their saved indices.
for _roof in SCENES:
    if _roof["Id"].startswith(("aranka.trickster.verse.encore", "aranka.trickster.verse.third_verse")):
        _nodes = {node["Id"]: node for node in _roof["Nodes"]}
        _slot = _roof["Id"] + ".explicit.1"
        _nodes["threshold"]["Choices"][0]["Next"] = _slot
        # User-supplied roof insertion: she leads, loses the tune, resumes at dawn.
        _roof["Nodes"].append(nar(_slot,
            '{n}Below the roof, the first carts begin to move.{/n}',
            c("Continue", "morning")))
        _nodes["morning"]["Text"] += '\n{n}Her voice is rough; your cloak still holds the cold of the tiles. She tests a new line about the noise, then grins at your expression.{/n}'
        _nodes["morning"]["Choices"].append(c(
            '\"Leave my name out of that verse. The garrison can guess.\"', "song_counter"))
        _roof["Nodes"].append(a("song_counter",
            '\"Your name? I can do better than your name!\" {n}She sings the line again, replacing your rank with a traveller and the stair with a roadside hedge. A carter at the gate chokes on his tea.{/n} \"There. Let them quarrel over who it was. You still owe me the harmony.\"',
            c('[Keep the bill and the new tune.]', flags=(NIGHT,))))


# Round 3 authored contact: ordinary pilgrims carry the question and reply.
# Optional throughout; correspondence never earns romance or revives Thall.
counter("aranka.thall.question", "The Wallflower", '\"What about Thall? He seemed fond of you.\"', [
    a("start", '''"My Wallflower! Such a voice, and he hides it in his scrolls. I wanted him to sing with me. He wanted... well, he never said."
{n}She sets down the lute.{/n} "I like him. I don't want his kisses. Yours are becoming a dreadful distraction."
"The pilgrims take letters between the camps. I could send him the new verse. And tell him who I keep coming back to see."''',
      c('"Send it. Let him hear it from you."', "sent"),
      c('"Leave the letter for now. Sing with me."', abort=True)),
    a("sent", '''{n}She writes on the back of a song sheet, then folds it with the verse inside.{/n} "There. No ballad about two tragic lovers. He'll know what I mean."
{n}She takes it to the pilgrims waiting beside the supply wagon and asks them to pass it to Thall. When she returns, she catches your sleeve.{/n} "Now. Where were we?"''',
      c("Continue", flags=(THALL_REQUESTED,))),
], requires=("trickster.ever", DUET, "aranka.present_now"), forbids=(CLOSED, THALL_REQUESTED, THALL_DEAD, KENABRES_ATTACKED), delay=0)

letter("aranka.thall.reply", "The low part", [
    a("start", '''{n}The returning pilgrims bring a folded sheet. Aranka recognizes the hand before she opens it. She reads aloud.{/n}
"Aranka. I had hoped you might... No. You have told me plainly. Thank you. I would rather you hadn't put it beside that rhyme. I had to read both twice."
"I won't sing in front of your Commander. Or anyone else. But I have enclosed the hymn you asked about. Don't change the low part. Please."
{n}Aranka reads the last line again, more quietly. She puts the letter beneath the hymn.{/n} "I did ask him. Before all this. I'll write back. About the hymn this time."
{n}She tries its first phrase, stops, and leaves the low part as written.{/n}''',
      c('[Listen to the hymn.]', flags=(THALL_ANSWERED,))),
], requires=("trickster.ever", THALL_REQUESTED, THALL_SAFE, "aranka.present_now"), forbids=(CLOSED, THALL_ANSWERED, THALL_DEAD, KENABRES_ATTACKED), delay=24)
