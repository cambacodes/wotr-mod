"""Mielarah on the Trickster path: "Zyphus picks the nearest" (Writer/handoffs/11-ROSTER-PLAN-2.md §2; family F15).

Canon (blueprints.zip / enGB): Magister Mielarah of the Arcanamirium, captain of Starcatcher the Third, drinks at the
Bad Luck tavern in Alushinyrra (Tumberd/Cue_0001 10a7f195, repeat greeting Cue_0002 2437e93b, hub AnswersList_0003
5cb72103). She tore a party of Pathfinders out of the claws of the Gravedragger, "the herald of Zyphus, god of accidental
and pointless death" (Cue_0044 182bda45), and he cursed her: "People around me started dying... But nothing happened to
me" (Cue_0048 64c5dd0b). Her code: "I never ignore those in distress, I never attack other vessels, and I honor the
integrity of the cargo" (Cue_0057 1732e4ec). She keeps her crew decent with "disciplinary thought-correction" (Cue_0054
935e5b8a) and the amulets she hates (AirAdventures/Cue_0328 d2093a8b). Hired (Cue_0075 a67acc05, the portal to her deck)
she flies the Commander to Colyphyr; stepping through the portal starts CaptainMielara (Portal_ToColyphyr/Answer_0017).
Her fates on the voyage: the Vazglar raid, where her crew hangs her for protesting (Cue_0482 dbec675b, TumberdDead
90f2e0f1); the hurricane, where she lets the wheel slip and Starcatcher goes into the Ishiar (Cue_0426 1b4e7824; her
death is never stated); or the landfall at Colyphyr (Cue_0033 fd7b46bf, hub AnswersList_0034 ef7be5c1), where the
Commander may still kill her for the fare (Answer_0068 a98bbc6b: canon stands, never overridden).

The device (11 §2): having heard the curse story, the Commander reads its rule. The curse never aims; it takes whoever
stands nearest when trouble comes (a Lore (Religion) or Perception check, or the chosen TricksterPerceptionTier1 sight;
failing both, an evening sat at her elbow, paid in blood). Once she is hired, the Commander posts her bosun, the man
most likely to kill her, at her elbow for the voyage. At the hanging the curse takes the man on the rope first. The
cost is personal: the Commander spent (or meant to spend) a man of her own crew on her curse, a breach of her code, and
the Gravedragger has noticed who did the choosing. The curse is never passed to the Commander.
With nobody posted, the curse takes the first man to fit her noose, and the rest haul her up by the capstan from the
far side of the deck: a slow strangling, not a drop. In those minutes Oskel flies ashore to the Commander, who is with
the raiding party, and back; the Commander goes through the hangmen and sends Oskel up to cut her down (raid.wind); the
curse takes him, unpaid and unchosen. Or (11 §2's other choice) the Commander stands
nearest and cuts the line with a thrown knife, and the falling block breaks a collarbone and leaves a grey spade on the
Commander's shoulder that never fades (cost.zyphus_mark). Either way she keeps her life, and the rope keeps her voice.

The Chapter 5 courtship on her presence in Drezen is mielarah_deck (the commit: in flight she lets go of the wheel,
the mirror of Cue_0426, and the Commander holds the course).
"""
from story_format import c, n, p, reaction, scene

from storylines import household

SCENES = []
P = "mielarah.trickster."
D = "mielarah.deck."
REL = "mielarah"

UNIT = "9d9c523bc2b17434bb66df212b127187"          # Mielara (Act_4 BadLuck; no dialog component: the presence copy)
PORTRAIT_GUID = "55aaada6899b415c99227ec23aff520f"  # her BlueprintPortrait (BCT_Mielara), the book-picture fallback
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
TIEFLING = "23eabf5b6364d4a4e86202dc5d27600b"      # Vendor_Tiefling, the lower town (no other route's anchor; the tailor is Kaylessa's)
JEWELER = "bc1093231b1577a4485a730c29595195"       # JewelerCapitalTrader, the fallback (Arueshalae's arcade copy is front 2.0)
TAVERN_LIST = "5cb721033c29ca04dab453de7c13b607"   # Tumberd/AnswersList_0003 (the Bad Luck)
TAVERN_RETURN = "2437e93b015b82d47900667402e01a9c" # Tumberd/Cue_0002 "I'm glad to see you again!"
COLYPHYR_LIST = "ef7be5c16b82f734096f5a5f9fd497ce" # Tumberd/AnswersList_0034 (the landfall)
COLYPHYR_RETURN = "2f275eb40f32b5c4996bc077b597e5e3"  # Tumberd/Cue_0038 "I gave the crew a few minutes..."
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"      # CompanionDialogues/Lann/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"    # CompanionDialogues/Woljif/AnswersList_0003

STARTED = "mielarah.started"
CLOSED = "mielarah.closed"
COMMITTED = "mielarah.committed"
# Native world keys (trickster_world bindings, and the new ones in BINDINGS below).
DEAD = "mielarah.dead"                    # TumberdDead: the hanging (Cue_0482)
DEAD_LATCH = "mielarah.dead.latched"
STORM = "mielarah.storm_crash"            # Cue_0426 seen
STORM_LATCH = "mielarah.storm_crash.latched"
KILLED = "mielarah.killed_at_colyphyr"    # Answer_0068: the Commander's own choice, canon stands
EXPELLED = "mielarah.expelled"            # Aeon only
ARRIVED = "mielarah.arrived"              # Cue_0033 seen
TOLD_CURSE = "mielarah.told_curse"        # Cue_0048 seen
HIRED = "mielarah.hired"                  # Cue_0075 seen: paid, the portal opened
VOYAGE = "mielarah.voyage_begun"          # AirAdventures_BookEvent started (any captain)
AMULETS = "mielarah.amulets_used"         # AirAdventures/Answer_0316: the Commander made her calm the mutiny
LIMERICKS = "mielarah.limericks"          # AirAdventures/Answer_0472: the Trickster's limericks
RAIDED = "mielarah.raid_ordered"          # AirAdventures/Answer_0404
KERZ = "captain.kerz"
NOCTA = "captain.nocticula"
SIGHT = "trickster.perception_tier1"      # a chosen Trickster trick: "You see more than other people."
LANN_GUARD = ("lann.dead", "lann.kicked_out")
WOLJIF_GUARD = ("woljif.dead", "woljif.kicked_out")

# Authored flags.
PATTERN = P + "primed.pattern"            # the curse's rule read
MISSED = P + "pattern_missed"             # both readings failed at the table
CUT = P + "cost.cut"                      # the fallback: the Commander sat nearest and bled for the reading
MINDER = P + "primed.minder"              # Oskel posted at her elbow for the voyage
TOLD = P + "minder.told"
LIED = P + "minder.lied"
PAID = P + "minder.paid"                 # she told him and paid him his freedom; he chose to sit at her elbow
REFUSED = P + "minder.refused"           # the Commander withdrew the order: no minder (the late recovery at the yard)
SECRET_KEY = "mielarah_oskel"
SECRET = "trickster.secret." + SECRET_KEY
SECRET_KNOWN = SECRET + ".known.mielarah"
ROPE_KEY = "mielarah_rope"               # the death itself, kept from the household (ROUTE-BRIEF-R §2: a planned NPC sacrifice is a secret)
ROPE_SECRET = "trickster.secret." + ROPE_KEY
SAID_USE = P + "said_use"                 # the Commander called the rule a thing to be used, at the table
CHARTER = P + "charter"                   # a charter to Drezen, for a Commander who sails with another captain
LANDFALL = P + "landfall"
RETURNED = P + "returned"
RAID_OWNED = P + "raid.owned"
RAID_UNREPENTANT = P + "raid.unrepentant"
DEFLECTED = P + "deflected"
OSKEL_DEAD = P + "cost.oskel"             # the Commander's man took the curse's accident in her place
MEANT = P + "cost.meant"                  # the Commander meant to spend him, and she knows it
SHIP_LOST = P + "cost.ship_lost"
WORD = P + "primed.word"                  # storm: word left for her in every aeronauts' tavern
LATE = P + "cost.late"                    # storm: the rule worked out afterwards, or bought from a diviner
STORM_OWNED = P + "storm.owned"
STORM_BLAMED = P + "storm.blamed"
NOTICED = P + "cost.noticed"              # the Gravedragger has noticed the Commander (finale hook)
# The hanging with nobody posted (the late recovery, dearer than the minder): the curse took the man who fitted her
# noose, the crew hauled her up by the capstan from the far side of the deck, and the Commander, fetched from the raid
# by Oskel, came back in those minutes and sent him up to cut her down.
CUT_DOWN = P + "raid.cut_down"            # Oskel cut her down at the Commander's order, and the curse took him
HUNG = P + "cost.hung"                    # minutes on the rope: her voice left a rasp, and she knows nobody prepared
HANGMAN_KNIFE = P + "cost.hangman_knife"  # the Commander went through the hangmen and took a cleaver across the forearm
ZYPHUS_MARK = P + "cost.zyphus_mark"      # the Commander stood nearest and cut her down: the block's grey spade on the shoulder
SELF = P + "primed.self"                  # the Commander posted at her elbow for the voyage instead of Oskel (11 §2's other choice)
YARD_KEY = "mielarah_yard"
YARD_SECRET = "trickster.secret." + YARD_KEY
CONTACT = P + "contact"                   # Derived: she is coming to Drezen
DECLINED = P + "declined"
LATE_COMMITTED = P + "late_committed"
# Chapter 5 (mielarah_deck)
DOCKED = D + "docked"
RECKONED = D + "reckoned"
FLOWN = D + "flown"
CORRECTED = D + "corrected"
FREED = D + "crew_freed"
TIGHTENED = D + "crew_tightened"
LAUGHING = D + "crew_laughing"
NIGHT = D + "quarterdeck"
MORNING = D + "morning"
HUB = "mielarah.presence"
HUB_FB = "mielarah.presence.arcade"
HUB_FAILED = HUB + ".failed"

BINDINGS = {
    "Etudes": {},
    "SeenCues": {HIRED: ["a67acc05e448a134aa2e4de0a30c5a15"]},          # Tumberd/Cue_0075 (the portal to her deck)
    "StartedDialogs": {VOYAGE: "a07f6d1f93531e048928c5c9de328a92"},     # AirAdventures_BookEvent
    "SelectedAnswers": {AMULETS: "9e0edaeccb20fbb4eb23477c1aab6706",    # AirAdventures/Answer_0316
                        LIMERICKS: "4dea3c896793d784591ae398e902c739",  # AirAdventures/Answer_0472 (PlayerIsTrickster)
                        RAIDED: "1eececde9d7a70c44be526ea668f3ed4"},    # AirAdventures/Answer_0404
    "MainCharacterFacts": {SIGHT: "8bc2f9b88a0cf704ea72d86c2a3e2aef"},  # TricksterPerceptionTier1Feature
}

RELATIONSHIP = dict(
    Title="The nearest",
    Description=("Magister Mielarah, captain of Starcatcher the Third, carries the Gravedragger's curse: the people "
                 "around her die, pointlessly, and she never does. I asked her how they died, and where they were "
                 "standing. I think the curse has a rule. I mean to learn what it costs to stand beside her."),
    Objective="Stand beside Mielarah",
    Guidance=("On the Trickster path, ask Mielarah at the Bad Luck tavern how her curse's victims died, after she has "
              "told you of the Gravedragger. Hire her ship and the voyage to Colyphyr decides the rest: she may reach "
              "Colyphyr, hang at Vazglar, or lose her ship to the storm. In Chapter 5 Starcatcher comes to Drezen."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, KILLED, EXPELLED], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        "raid": dict(detect=[DEAD], device=P + "raid.rope", returned=RETURNED),
        "storm": dict(detect=[STORM], device=P + "storm.word", returned=RETURNED),
    },
)

DERIVED = {
    CONTACT: [[LANDFALL], [RETURNED], [CHARTER, KERZ], [CHARTER, NOCTA]],
    LATE_COMMITTED: [["trickster.ever", FLOWN]],
    D + "oskel_settled": [[D + "stern"], [D + "oskel_spoke"]],
}

GREETING = ("{n}Crates stamped with the anchor of Starcatcher stand stacked beside the tiefling trader's stall in the lower town, and the woman "
            "counting them off against a bill of lading keeps an arm's length of empty cobbles around her without "
            "seeming to try. The market has noticed. Nobody walks close.{/n}")
PRESENCES = {
    HUB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TIEFLING, Side="behind", Distance=2.5),
              Requires=["trickster.ever", CONTACT], Forbids=[CLOSED, KILLED, HUB_FAILED], MinChapter=5, MaxChapter=5,
              AnswerLists=[], Dialog="hub", Greeting=GREETING),
    HUB_FB: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=JEWELER, Side="behind", Distance=2.5),
                 Requires=["trickster.ever", CONTACT, HUB_FAILED], Forbids=[CLOSED, KILLED], MinChapter=5, MaxChapter=5,
                 AnswerLists=[], Dialog="hub",
                 Greeting=("{n}In the jewellers' arcade, behind the counters, a woman in a captain's coat is weighing "
                           "a pouch of Abyssal stones against a bill of lading. Customers step around her in a wide, "
                           "polite curve, the way water goes round a rock.{/n}")),
}

household.secret(
    SECRET_KEY, "Oskel at her elbow",
    "Mielarah's curse takes whoever stands nearest when trouble comes. Before the voyage to Colyphyr I posted her bosun "
    "at her elbow, the man most likely to put a rope round her neck, and I told her it was to steady a nervous crew. "
    "That was a lie. She is a magister of the Arcanamirium; she may work it out.",
    portrait="Mielarah", witnesses=("mielarah", "seelah", "irabeth"), risk="high")

household.secret(
    ROPE_KEY, "The man on the rope",
    "Mielarah's curse takes whoever stands nearest when trouble comes. I arranged for her bosun Oskel to be the nearest, "
    "and when it came, it took him and left her breathing. She knows what I did. My household does not, and there are "
    "paladins in it who would have a short, ugly word for it. Sailors talk in every tavern between the Midnight Isles and "
    "Drezen.",
    portrait="Mielarah", witnesses=("seelah", "irabeth"), risk="medium")

household.secret(
    YARD_KEY, "The main yard",
    "Mielarah hanged at Vazglar because I had prepared nothing for it. Her bosun Oskel fetched me from the raid, and I sent "
    "him up to the main yard to cut her down, knowing her curse takes whoever stands nearest when trouble comes. It took him and left "
    "her breathing. She knows. My household does not, and eleven hangmen put off on a rock in the Ishiar could tell them.",
    portrait="Mielarah", witnesses=("seelah", "irabeth"), risk="medium")


def mi(id, text, *choices, **kw):
    return n(id, "Mielarah", text, *choices, portrait="Mielarah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Mielarah", **kw)


def tavern(id, title, entry, nodes, requires, forbids=(), delay=0, device=True):
    """An inline scene on her own list at the Bad Luck, before the voyage (Chapter 4). The table scenes that read and use
    the curse are the raid state's devices (ER-2): they can only play before the voyage begins, which they forbid."""
    extra = dict(TricksterDevice=True, TricksterState="raid") if device else {}
    SCENES.append(scene(id, title, "Mielarah", 4, entry, nodes, requires=requires, forbids=(VOYAGE, *forbids), delay=delay,
                        last=4, Relationship=REL, Chapters=[4], AnswerLists=[TAVERN_LIST], NativeReturnCue=TAVERN_RETURN,
                        **extra))


def remote(id, title, nodes, requires, forbids=(), delay=0, chapters=(4, 5), kind="visit", **extra):
    SCENES.append(scene(id, title, "Mielarah", min(chapters), "", nodes, requires=requires, forbids=forbids, delay=delay,
                        last=max(chapters), Relationship=REL, Remote=True, Chapters=list(chapters), Kind=kind, **extra))


# --- 1. The Gravedragger's arithmetic: reading the rule (primer; inline at the Bad Luck, after Cue_0048). ------------

tavern(P + "tavern.arithmetic", "The Gravedragger's arithmetic",
       '"The people your curse took. Tell me how they died, and where they were standing."', [
    mi("start", '''{n}She does not look surprised. She has been asked before, you think, by people who wanted a story to take home and tell badly. She sets her cup down, turns it by the handle until the handle points at the door, and folds her hands on the table.{/n}
"Most people ask how many. You ask how. That is either very kind or very morbid. I should like to know which, before I answer."
{n}She takes a small book out of her coat, bound in sailcloth and gone soft at the corners, and opens it without needing to find the page.{/n} "None of them made the broadsheets. They're in here. The first was a steward of the Arcanamirium, the week I came home from Abaddon. He was bringing me tea on the east stair. The tray tipped, he trod on the spoon, and he broke his neck on the newel post." {n}A small, precise shrug.{/n} "Pointless. That is the Gravedragger's whole signature. Pointless."''',
       c("Go on.", "list")),
    mi("list", '''"My first mate on Starcatcher the First. Lightning out of a clear sky, while we had the charts spread on the binnacle between us. A Pathfinder I had pulled out of Abaddon came to my door in Absalom to thank me and was kicked by a carriage horse on my own step. A harbour clerk, stamping my papers. A girl who sold me apples, while I was counting out the copper."
{n}Her voice is quite even. The list has been said so often that it has worn smooth, like a prayer, or a road.{/n}
"Some of them I loved. Most of them I had never heard of until the inquest; the news of them followed me from port to port, as if it had been told where to find me. I kept their names. I have every one. It is the least a magister can do, to keep accurate records." {n}She picks the cup up again and does not drink from it.{/n} "There. Now you have a story to tell badly."
"Alushinyrra has its own version, of course. There are people in this city who have suggested, quite seriously, that the Lady send the servants who displease her to crew for me, and let fate deal with them. The Lady's own stewards will not let me past her gate." {n}A thin smile.{/n} "Demons are better natural philosophers than magisters. They don't ask why. They only watch who dies."''',
       c('[You see more than other people] Look past her shoulder, at what stands there.', "sight", requires=(SIGHT,),
         mythic="Trickster"),
       c('[Lore (Religion) DC 26] Think about what a herald of Zyphus would want with a tally.',
         check=dict(Skill="SkillLoreReligion", DC=26, Success="doctrine", Failure="fail_lore", CommanderOnly=True)),
       c('[Perception DC 26] Stop listening to the names. Watch the room around her.',
         check=dict(Skill="SkillPerception", DC=26, Success="watch", Failure="fail_eye", CommanderOnly=True)),
       c('"I\'m sorry. I shouldn\'t have asked."', abort=True)),
    nar("sight", '''{n}You have seen more than other people since the path took you. You let your eyes slide past her shoulder, and something is there.{/n}
{n}Not a shape: the idea of one, leaning on a spade that is not there either, patient as a gravedigger at the end of a long day. It is not looking at her. It has never been looking at her. Its blank regard rests on the serving girl who is filling Mielarah's cup, and when the girl steps back it turns, the way a compass needle turns, and settles on whoever is nearest.{/n}
{n}At the moment, that is you. It is a cold thing to be looked at by. You look back.{/n}''',
        c('"It isn\'t watching you. I don\'t think it ever was. It watches whoever stands closest to you."', "rule")),
    nar("doctrine", '''{n}You know a little of Zyphus. Everyone who has buried friends in the Worldwound learns a little. His priests hold that no death is written in advance; a death is an accident, and an accident is an offering. A curse from his herald would not aim. Aiming is for assassins and for fate. It would simply collect.{/n}
{n}And, as far as her own list tells it, every name on it died within arm's reach of her. Bringing tea. Leaning over the same chart. On her step. Stamping her papers. Taking her copper. Not the people she cared for most, not the people who hated her: the people who happened to be standing nearest when the dice fell.{/n}''',
        c('"I don\'t think it chooses. I think it takes whoever is standing nearest you."', "rule")),
    nar("watch", '''{n}You stop listening to the names and watch the room instead.{/n}
{n}A sailor at the next table has tipped his chair back on two legs to listen, so far that his head is almost at her shoulder. The rear leg finds the one soft board in the floor of the Bad Luck. He goes over backwards, and the back of his skull meets the edge of her table with a sound like a dropped melon, and he lies there blinking at the rafters with blood in his ear.{/n}
{n}Mielarah does not turn her head. You understand that she stopped turning her head years ago. And you understand something else: of everyone in the room, he was simply the closest.{/n}''',
        c('"I don\'t think it aims at anyone. I think it takes whoever is nearest you. That man was nearest."', "rule")),
    nar("fail_lore", '''{n}You reach for what you know of Zyphus and come up with a drinking song about a gravedigger's cart that tips over at every verse. It is not helpful. The silence goes on a beat too long, and she notices it.{/n}''',
        c('[Perception DC 26] Stop thinking. Watch the room around her instead.',
          check=dict(Skill="SkillPerception", DC=26, Success="watch", Failure="fail_both", CommanderOnly=True)),
        c("Let it go for tonight.", "fail_both")),
    nar("fail_eye", '''{n}You watch the room. It is a tavern in Alushinyrra: people drink, people lie, a demon in a good coat loses at cards and pretends to enjoy it. Nothing happens that tells you anything, and she catches you looking for it.{/n}''',
        c('[Lore (Religion) DC 26] Think instead about what a herald of Zyphus would want with a tally.',
          check=dict(Skill="SkillLoreReligion", DC=26, Success="doctrine", Failure="fail_both", CommanderOnly=True)),
        c("Let it go for tonight.", "fail_both")),
    mi("fail_both", '''"You're trying to solve it." {n}She says it quite kindly, which is worse.{/n} "Everyone tries, over their second drink. A Pathfinder witch tried. A priest of Pharasma tried, at twelve hundred gold the consultation. One very expensive demon in this very city tried and charged me for the privilege."
"I've entertained you enough for one evening, I think. Come back when you want a ship. That, I can do something about."''',
       c("[Leave her to her cup.]", flags=(MISSED,))),
    mi("rule", '''{n}For a moment she is entirely still. Then she laughs, a small, dry sound with nothing behind it.{/n}
"Nearest." {n}She says it the way a scholar repeats a wrong answer, to be sure she heard it.{/n} "That is a hypothesis, Commander, not a finding. I have read every treatise on curses in the Arcanamirium's library. I paid the priest, the witch and the demon. Not one of them suggested it had a pattern."
{n}Her hands have come apart on the table. She looks at them.{/n}
"But I have my records. The steward was on the stair below me. My mate was across the binnacle. The girl was across her counter, taking my copper." {n}Slowly, as if adding a column.{/n} "If it has a rule, then everyone who ever stood beside me, I put there. The steward. My mate. The girl with the apples. I wanted a cup of tea, and a second opinion on a chart, and an apple." {n}The smile comes back, badly.{/n} "Accurate records. Somebody should have told me what I was recording."''',
       c('"Then choose better who stands beside you."', "choose", flags=(PATTERN, STARTED)),
       c('[Flirt] "Or choose someone who knows the rule, and stands there anyway."', "brave", flags=(PATTERN, STARTED)),
       c('"A rule is a thing that can be used."', "used", flags=(PATTERN, STARTED, SAID_USE))),
    mi("choose", '''"Choose." {n}She turns the word over like a coin of doubtful mint.{/n} "You make it sound like seating a dinner. Perhaps it is. Put the people you love at the far end of the table and the people you would not miss beside you, and pass the salt."
{n}She finishes her drink at last.{/n} "That is a monstrous way to live, Commander. I shall probably think about nothing else for a month. Thank you. I mean that, and I also wish you hadn't said it."''',
       c("[Leave her with it.]")),
    mi("brave", '''{n}Her eyes go to the space between you, which is not very much space, and then back to your face.{/n}
"You are standing there now. And you know it." {n}A beat.{/n} "You are either very brave or very careless. Though I suppose it doesn't really matter which."
{n}She does not move her chair away. You notice that she considers it, and does not.{/n} "Magisters of the Arcanamirium are trained to distrust a result the first time it appears. Come and stand there again sometime, and we will see whether it repeats."''',
       c("[Stay where you are a little longer.]")),
    mi("used", '''{n}Something in her face shuts, like a hatch in weather.{/n}
"Used." {n}She sets the cup down very precisely.{/n} "Like a knife, you mean. I didn't tell you this so that you could find a use for it, Commander. People have died of this. Good people, and people who only wanted to sell me an apple."
{n}And then, because she is honest, and cannot help it:{/n} "...Though I'll grant it is the first useful thing anyone has said about it in six years. Don't make me regret having listened."''',
       c("[Let the matter rest.]")),
], requires=("trickster", TOLD_CURSE), forbids=(PATTERN, MISSED))


# --- 1b. The second look (the failed reading's fallback): an evening at her elbow, paid in blood. -------------------

tavern(P + "tavern.second_look", "At her elbow", '[Sit down beside her, closer than anyone.]', [
    nar("start", '''{n}You do not ask this time. You take the stool at her elbow, the one everyone else in the Bad Luck leaves empty, and you sit on it, close enough that your sleeve touches hers.{/n}
{n}Mielarah looks at the sleeve, and at you, and lifts one eyebrow the way a customs officer lifts a lid.{/n}''',
        c("Continue", "talk")),
    mi("talk", '''"That stool has a reputation. The last man who sat on it was a smuggler from Nahyndri. He is buried, in several places." {n}She does not tell you to move.{/n} "Are you testing a theory, Commander, or merely drinking?"
{n}So you drink, and she talks, a little: about Absalom, where the harbour smells of tar and oranges, and about Starcatcher's new rigging, which she explains in more detail than you asked for. For an hour nothing happens at all. The Bad Luck roars around the two of you and leaves you alone.{/n}''',
       c("[Keep your seat.]", "lamp")),
    nar("lamp", '''{n}Then a brawl two tables over sends a bottle spinning, end over end, the way bottles fly in every tavern in the multiverse. It is not thrown at anyone. It is not thrown at all. It simply leaves one quarrel and goes looking for somewhere to land.{/n}
{n}It comes straight at the stool you are sitting on. You get a hand up. The neck breaks against your palm and the rest goes past your ear, and a curl of green glass opens your hand from the heel to the base of the thumb.{/n}
{n}Nobody else is so much as splashed. Of everyone in the room, you were simply the closest.{/n}''',
        c("[Look at your hand. Then at her.]", "rule")),
    mi("rule", '''{n}She has your wrist before you have finished looking, and a clean handkerchief out of her sleeve, and she is binding the cut with quick, furious neatness, the way a sailor whips a rope's end.{/n}
"You sat there on purpose." {n}She is not asking.{/n} "You sat nearest, and you waited to see what came. That is the stupidest experiment I have ever watched, and I watched a gnome try to lift a curse by eating the cursed item."
{n}She ties the knot. Then she stops, with her fingers still on it.{/n} "Nearest. Not the brawlers. Not me. You." {n}Her voice drops.{/n} "It doesn't aim. It takes the nearest. Six years, and you worked it out with a bottle."''',
       c('"It cost me a hand. It\'ll heal."', "done", flags=(PATTERN, CUT, STARTED)),
       c('[Flirt] "Worth it. I got you to hold my hand."', "flirt", flags=(PATTERN, CUT, STARTED))),
    mi("done", '''"It will scar." {n}She lets go of your wrist at last, rather abruptly.{/n} "They always scar, the ones it leaves alive. I would know. I've been collecting other people's scars for years." {n}She gives your bandaged hand one more look, a professional look.{/n} "Move your stool back a little, Commander. Not far. Just enough that I don't have to watch it happen twice."''',
       c("[Move the stool an inch.]")),
    mi("flirt", '''"You are bleeding on my coat." {n}But she does not let go at once. Her thumb stays on the knot of the handkerchief a moment longer than a knot needs.{/n}
"That was a very poor joke, and a very brave one, and I shall be angry about both until it stops bleeding." {n}She lets go.{/n} "Don't do it again. And don't sit anywhere else."''',
       c("[Keep your seat.]")),
], requires=("trickster", TOLD_CURSE, MISSED), forbids=(PATTERN,), delay=8)


# --- 1b'. Does the result repeat? (the courtship at her table: standing nearest again, on purpose; optional). ------

REPEATED = P + "repeated"

tavern(P + "tavern.repeat", "Does it repeat?", '[Take the stool at her elbow again.]', [
    nar("start", '''{n}The stool at her elbow is empty, as it always is. You take it.{/n}
{n}Mielarah does not look up from the letter she is writing. She finishes the line, blots it, and sets the pen down parallel to the edge of the paper.{/n}
"Magisters of the Arcanamirium are trained to distrust a result the first time it appears," {n}she says to the letter.{/n} "I believe I said something of the kind. I did not expect to be taken at my word."''',
        c("Continue", "wait")),
    mi("wait", '''"Very well. The experiment is simple. You sit there. I sit here. We drink something bad and talk about something unimportant, and we see whether anything falls on you." {n}She signals for two cups.{/n} "I will note that no one has ever volunteered for this experiment twice."
{n}The serving girl brings the cups at arm's length, sets them down at the very edge of the table, and leaves at a pace just short of running. Mielarah pushes one toward you with a fingertip.{/n} "Your health. Such as it is."''',
       c('"What shall we talk about?"', "talk"),
       c('[Flirt] "You. I\'m told it\'s an unimportant subject."', "talk")),
    mi("talk", '''"Absalom, then. Everybody from Golarion wants to talk about Absalom; it saves them having to talk about wherever they actually come from." {n}And she does: the Arcanamirium's lamps, the harbour, a professor of transmutation who kept a tame octopus in his bath and lectured to it when his students did not attend.{/n}
{n}Halfway through the octopus, the knife comes. A cook two tables over is carving a joint for a demon who wants it thinner; the blade turns on a bone, leaves his hand, and comes spinning across the room at head height, not thrown, simply going.{/n}''',
       c("Continue", "knife")),
    nar("knife", '''{n}It goes between you. There is not much room between you, and it finds it, and buries itself a finger's depth in the wooden pillar behind your two stools with a noise like a door being knocked on, once.{/n}
{n}Nobody is touched. The knife hums in the wood. Across the room the cook is staring at his empty hand.{/n}
{n}Mielarah looks at the knife, and at the space between you, and then, very slowly, at you.{/n}''',
        c("Continue", "result")),
    mi("result", '''"It missed." {n}Her voice is perfectly flat, the voice of someone reading a figure off an instrument she does not trust.{/n} "It came for the nearest and it went between us, and it missed."
{n}She reaches up and pulls the knife out of the pillar with a small grunt of effort, and turns it over, and lays it on the table beside her pen, parallel to the edge of the paper.{/n}
"The result repeats." {n}And then, as if she cannot help it, she laughs: a real one, short and astonished, the kind that surprises the person it comes out of.{/n} "Six years. The result repeats."''',
       c('"Brave, or careless?"', "brave", flags=(REPEATED,)),
       c('"Or I\'m special."', "special", flags=(REPEATED,))),
    mi("brave", '''"Both. I have decided it is a single word in some language I don't speak." {n}She picks up her pen again, and does not write anything with it.{/n} "Go away, Commander. I have a letter to finish, and I cannot remember a single word of it, and it is entirely your fault."''',
       c("[Leave her the knife.]")),
    mi("special", '''"Don't." {n}But she is still smiling.{/n} "Don't say that. I have been waiting six years for someone to be special, and I will be very cross if it turns out to be a Trickster who thinks it's a joke."
{n}She picks up her pen, and does not write anything with it.{/n} "Go away. I have a letter to finish. I cannot remember who it is to."''',
       c("[Leave her the knife.]")),
], requires=("trickster", PATTERN), forbids=(REPEATED,), delay=12, device=False)


# --- 1c. The chart of the Midnight Isles (the courtship at her table, before the voyage; optional). ---------------

tavern(P + "tavern.charts", "The chart of the Midnight Isles", '"Show me the way to Colyphyr. The way you would fly it."', [
    mi("start", '''{n}Her face changes. It is a small change, and you would miss it if you had not watched her say the names of her dead: the tiredness goes out from under her eyes and something younger comes up in its place.{/n}
"The way I would fly it." {n}She pushes the cups aside with her forearm and unrolls a chart across the table, weighting one corner with the salt cellar and another with her own pistol.{/n} "Most passengers want to know how long. Nobody asks how. You keep asking how, Commander. It is a bad habit, and I approve of it."''',
       c("Go on.", "isles")),
    mi("isles", '''{n}The Midnight Isles are drawn in three inks: black for rock, blue for the Ishiar below, and red for everything that will try to kill you, which is most of it.{/n}
"Here we are. Alushinyrra. Here is Colyphyr, where you want to go, and where nobody sane has wanted to go in a century. Between them, the harpies of the coastal cliffs, who sing sailors off the rail; Mharah, where the air itself makes men quarrel; Alir, where the trees eat the watch; Nahyndri, where the slavers and Dagon's lunatics fly skin sails; and Vazglar, which is a rock with tombs on it and a village underneath, and nothing worth stopping for."
{n}Her finger moves across the chart without once touching the paper, a hair above it, the way a helmsman's hand hovers over the spokes.{/n}''',
       c('"Mharah. How do you keep a crew from killing each other over it?"', "mharah"),
       c('"Tombs on Vazglar. You said that like someone who knows tombs."', "vazglar"),
       c('"And the weather?"', "weather")),
    mi("mharah", '''"I go to my cabin for a quarter of an hour." {n}She says it lightly, and does not look at you.{/n} "When I come out, nobody wants to kill anybody. Nobody wants anything very much. It passes when the island passes."
"It is the same discipline I keep every day, only louder. I told you I recruit the not completely corrupted. Mharah is the place where 'completely' comes up for air." {n}She rolls a pencil under one finger.{/n} "You will see me come out of that cabin looking like a wrung cloth, Commander. Please don't comment on it."''',
       c('"Tombs on Vazglar. You said that like someone who knows tombs."', "vazglar"),
       c('"And the weather?"', "weather")),
    mi("vazglar", '''{n}The pencil stops rolling.{/n}
"I know a great many things. I am a magister of the Arcanamirium; knowing things is the qualification." {n}Her mouth goes thin, in the way it did when she spoke of the Gravedragger.{/n} "Tombs have doors that are meant to be shut, and people who open them and wish they hadn't. I have been one of those people. I will not be one again for you, and I will not talk about it in the Bad Luck."
{n}She moves the salt cellar two inches, as if the chart had shifted.{/n} "Ask me somewhere with fewer ears. Perhaps."''',
       c('"And the weather?"', "weather")),
    mi("weather", '''"The weather is the Abyss, and the Abyss does not have weather. It has moods." {n}She taps the blank space in the middle of the chart, where the Ishiar has no islands.{/n} "Out here the storms come up in an hour and last a week. Starcatcher the First went down in one. I do not fly into storms any more, if I can help it. I fly round them."
"If you order me into one, I'll do it. I'm a professional, and it will be your expedition." {n}She looks up.{/n} "But I would prefer that you didn't. I would prefer that very much."''',
       c('[Flirt] "You look happier over that chart than I\'ve seen anyone look in Alushinyrra."', "joy"),
       c('"I\'ll remember that."', "joy")),
    mi("joy", '''{n}She laughs, a real one, surprised out of her.{/n}
"I am happier over this chart than anyone in Alushinyrra has any right to be. That's the trouble with being an aeronaut. You can be cursed, exiled, twice shipwrecked and drinking in a demon's tavern, and the moment somebody unrolls a chart you're sixteen again and it's the best job in the whole world."
{n}She begins to roll it up, carefully, from the Colyphyr end.{/n} "Nobody asks how, Commander. I think I may have been waiting six years for somebody to ask how."''',
       c("[Help her roll up the chart.]", flags=(P + "charted",))),
], requires=("trickster", PATTERN), forbids=(P + "charted",), delay=8, device=False)


# --- 1d. Other ships (before hiring: her case against Kerz and the Lady's captains; optional). -------------------

CAPTAINS_HEARD = P + "captains_heard"

tavern(P + "tavern.captains", "Other ships", '"There are other ships for hire in Alushinyrra."', [
    mi("start", '''"There are." {n}She does not seem offended. She seems, if anything, pleased to have been asked, the way a scholar is pleased by a hostile question she has prepared for.{/n}
"There is Kerz, who will quote you a price and then renegotiate it over Ishiar, at a height, with a knife. There is the Lady in Shadow, who will lend you one of her own ships with a captain she has hand-picked for loyalty to her, and you will owe her for it for the rest of your life, which may not be long. And there are a dozen others, whom I will not dignify by name, who will sell you to the first slaver with a better offer."
{n}She lifts her cup.{/n} "And then there is me."''',
       c('"Tell me about Kerz."', "kerz"),
       c('"And what does it cost to sail with you?"', "cost")),
    mi("kerz", '''{n}Her lip curls, very slightly, and for a moment the courtesy slips.{/n}
"Got-Stabbed. He has been stabbed more times than anyone can count and it has not improved him. He tortures his prisoners for the pleasure of it and his passengers for the profit. On Golarion even the Shackles pirates would hang him from the yardarm, and they are not particular." {n}She puts the cup down.{/n}
"He will get you to Colyphyr, probably. He is good in a fight. Ask him what he keeps in the little box in his cabin, if you ever want to stop sleeping."''',
       c('"And what does it cost to sail with you?"', "cost")),
    mi("cost", '''"A hundred and fifty thousand in gold, unless you convince me your mission is noble, in which case I am a fool and it is less." {n}The quick smile.{/n} "And the curse. You know the curse. Some of my crew will die on the way, of stupid things, because they will be standing near me when stupid things happen. That is the honest price."
"The others will not tell you their honest price. That is the difference between us. I will carry you where you are going, I will not steal your boots, I will not sell you to anybody, and I will tell you to your face exactly how many people I expect to bury on the way." {n}She spreads her hands.{/n} "Two, on a good voyage. Four, on a bad one."''',
       c('[Flirt] "And how many passengers?"', "passengers", flags=(CAPTAINS_HEARD,)),
       c('"That\'s a fair price. I\'ll think about it."', "think", flags=(CAPTAINS_HEARD,))),
    mi("passengers", '''"None, so far." {n}She says it lightly, and then hears it, and considers it with a magister's frown.{/n}
"None. Isn't that odd? Six years, three ships, and I have never lost a passenger. Crew, yes. Harbour clerks. A girl with apples. But never anyone who paid a fare." {n}She taps the table.{/n} "I have no theory for that. I dislike having no theory. You'll have to come aboard so that I can study the question."''',
       c("[Promise to think about it.]")),
    mi("think", '''"Do. Take your time. Alushinyrra is full of ships and every one of them is a worse idea than mine." {n}She finishes her cup.{/n} "When you decide, you know where I sit. It is the table with nobody at the next one."''',
       c("[Leave her to her table.]")),
], requires=("trickster", "mielarah.met"), forbids=(CAPTAINS_HEARD, HIRED), device=False)


# --- 2. The bosun at her elbow (the device's preparation; after she is hired, before the portal). -------------------

tavern(P + "tavern.minder", "The bosun", '"Before we sail. Who is the most dangerous man on your crew?"', [
    mi("start", '''{n}The portal she opened for you still shimmers in the corner of the Bad Luck, a doorway of salt light that smells faintly of rope and weather. Mielarah is working through a supply list at her table with a pencil behind her ear.{/n}
"The most dangerous?" {n}She does not look up.{/n} "That is an odd question from a passenger. Most of my passengers ask where the privy is." {n}She makes a tick, and another.{/n} "Oskel. My bosun. Oskel, would you come here a moment?"''',
       c("Continue", "oskel")),
    nar("oskel", '''{n}The man who comes over from the door has to duck under the lintel of the Bad Luck and fold his wings to get through. A tiefling of the Midnight Isles, broad as a hatch cover, with a slaver's brand gone white on the side of his neck and a face that has been broken and set by amateurs more than once. He stops at a respectful distance from her. Everyone does.{/n}
"Ma'am." {n}His voice is low and careful, like a man carrying something full to the brim.{/n}
{n}"The Commander will be sailing with us," Mielarah tells him. "Tell the mess to lay one more place. That is all." He nods once, looks at you exactly as long as a bosun looks at new cargo, and goes.{/n}''',
        c("Continue", "who")),
    mi("who", '''"I took him off a slaver's deck off Nahyndri, six years ago. He had killed three men on that ship, and he would have killed me, and some days I think he still means to." {n}She says it the way she might describe a leak she has learned to live with.{/n}
"He is also the best bosun in the Midnight Isles. The crew would sail into a hurricane on his word. That is the disciplinary thought-correction at work: a little of me in his head, every day, so that the man who would cut my throat keeps choosing to be the man who keeps my ship." {n}A thin smile, and a tap at her temple.{/n} "Don't make that face. I told you I recruit the not completely corrupted. 'Not completely' is doing a great deal of work in that sentence."''',
       c('"Put him at your elbow for the voyage. Nearer to you than anyone, every hour, until we land."', "order")),
    mi("order", '''{n}The pencil stops.{/n}
"I beg your pardon?"
"You are not my captain, Commander. Not yet." {n}She glances at the portal.{/n} "When you step through that, for the length of the expedition, you are. That is the arrangement, and I honour arrangements. But on this side of it, you will tell me why you want the most dangerous man on my ship standing at my shoulder in a place where there is no one to hear me scream."''',
       c('[Tell her the truth] "Your curse takes whoever is nearest. If it has to take someone, let it take the man most likely to kill you."', "truth",
         flags=(TOLD,)),
       c('[Lie] "A cursed captain makes a crew nervous. Let them see the biggest man aboard standing at your back."', "lie",
         flags=(MINDER, LIED, SECRET)),
       c('"Forget I said it."', abort=True),
       c('[Stand nearest yourself] "Then not him. Me. I\'ll be at your elbow every hour until we land."', "self",
         flags=(SELF,))),
    mi("self", '''{n}The pencil stops again. This time she looks at you properly, the way she looked at the portal: as a thing that will take her somewhere she has not decided to go.{/n}
"You." {n}Flatly.{/n} "You have a war, Commander. You have a crusade that falls over if you do. And you want to spend the voyage standing where my steward stood with his tray."
"I won't pretend I don't know what you're doing. You think my curse has a rule, and you want to be the answer to it." {n}She makes a small, precise tick on her list, as if entering a cost.{/n} "Very well. It's your expedition. But I shall watch you every hour of it, and if anything comes down out of my rigging, I want you to know that I told you so, in the Bad Luck, in front of witnesses."''',
       c("[Let her finish her list.]")),
    mi("truth", '''{n}She puts the pencil down. For a while she says nothing at all, and the noise of the Bad Luck fills the space where her answer should be.{/n}
"You want to feed my curse my own bosun." {n}Very quietly.{/n} "I took him off a slaver's deck. I have spent six years in his head, keeping him decent. I promised him that one day I would pay him off with enough gold to buy a quiet life on some other plane, and he believed me, which I assure you is not a thing Oskel does."
"My code is three lines long, Commander. I never ignore those in distress. I never attack other vessels. I honour the cargo I carry. On my deck, my crew is the cargo."''',
       c('"And you are the ship. I\'d rather lose cargo than the ship."', "yield"),
       c('"Then keep him at your elbow and keep him decent. If nothing goes wrong, nothing happens to him."', "yield"),
       c('"You\'re right. It\'s your crew. Forget I asked."', "withdrawn", flags=(REFUSED,))),
    mi("yield", '''{n}She looks at the portal, and then at her list, and then, finally, at you.{/n}
"It's your expedition, and on the far side of that portal I'll take your orders. So hear mine first, while I'm still the captain." {n}She sets the pencil down, square to the edge of the list.{/n}
"I tell him myself. Tonight, all of it: the curse, your theory, and what you want him for. Then I pay him off. The gold I promised him for a quiet life, every coin of it, in his hand, before we sail. If he takes it and walks off my ship, there goes your lightning rod, and I'll fly you to Colyphyr without him, and you'll have deserved it."
"If he stays, he stays because he chose to, knowing why. Not because you arranged him like a chair at a dinner." {n}Her voice does not rise.{/n} "That is the only way Oskel stands at my elbow."''',
       c('"Pay him. Tell him everything."', "paid", flags=(MINDER, PAID, MEANT)),
       c('"Then leave it. I won\'t spend your gold on my theory."', "withdrawn", flags=(REFUSED,))),
    nar("paid", '''{n}She does it that night, at the table with nobody at the next one. You are not invited; you watch from the bar. She talks, and he listens with his big scarred hands flat on the table, and at the end she counts coins into a purse, all of them, and pushes it across to him.{/n}
{n}Oskel looks at the purse, and at her, and across the room at you. Then he puts the purse inside his shirt, stands, picks up his stool, carries it round the table, and sets it down at her elbow. He sits on it.{/n}
{n}When she comes to the bar afterwards her face has no expression at all.{/n} "He said, 'Figured.' Then he said a man doesn't retire on a debt, and he'll buy his quiet life after Colyphyr, out of his own wages, thank you." {n}She takes the cup out of your hand and finishes it.{/n} "I have just paid a man his freedom so that he can sit where my curse will reach him. If he dies at my elbow, Commander, I'll know whose theory put him there, and so will you, and neither of us will ever be able to pretend otherwise."''',
        c("[Leave her to her list.]")),
    mi("withdrawn", '''"Thank you." {n}She says it as though she means it, and as though it cost her something to find out that she does.{/n}
"You may be right, you know. About the curse. I'll think about it on every watch between here and Colyphyr." {n}She picks the pencil up again.{/n} "But I'll think about it with Oskel twenty strides away, where he belongs. Now let me finish my list. Your quartermaster has sent me a request for eleven barrels of something he calls wine, and I intend to be rude to him about it."''',
       c("[Leave her to her list.]")),
    mi("lie", '''{n}She considers it, and something in her shoulders comes down half an inch.{/n}
"The crew is nervous. They always are, the first week. They count the empty hammocks from the last voyage and they look at me." {n}She taps the pencil against her teeth.{/n} "Oskel at my back. They'll think I've finally hired a bodyguard. The pirates of the Midnight Isles will think I've gone soft."
"Very well. It's your expedition, and it's a sensible precaution, and I dislike that it's sensible." {n}She almost smiles.{/n} "You think like a quartermaster, Commander. That's a compliment. Mostly."''',
       c("[Let her think so.]")),
], requires=("trickster", PATTERN, HIRED), forbids=(MINDER, REFUSED, SELF))


# --- 2b. A charter to Drezen (for a Commander who reads her curse and sails with another captain). -----------------

tavern(P + "tavern.charter", "A charter for after", '"When this is over, Drezen will need a ship. Yours."', [
    mi("start", '''{n}She has her ledger open, and she closes it over one finger to keep the place.{/n}
"Drezen." {n}She pronounces it the way people in Absalom pronounce any town north of the Lake of Mists and Veils: politely, as a word that means cold.{/n} "I read the broadsheets, even here. Your crusade took a city back from the demons and now has to feed it. I imagine there are a great many people there who would like to be somewhere else, and a great many things that would like to be carried to them."''',
       c('"Refugees, wounded, medicine, cold iron. A ship that stops for people in distress."', "code")),
    mi("code", '''"You are quoting my code back at me." {n}She sounds more pleased than she wants to.{/n} "That is either flattery or research, and either way it is effective."
"But understand the cargo you are asking for. My curse does not stay behind when I sail. If Starcatcher comes to Drezen, people in Drezen will die of stupid things: a slipped plank, a runaway cart, a stair." {n}Her mouth tightens.{/n} "You know the rule now. You know it better than I do. Do you still want me there?"''',
       c('"I want you there. I\'ll keep the right people standing nearest."', "yes", flags=(CHARTER, STARTED)),
       c('"Not yet. Let me think about it."', abort=True)),
    mi("yes", '''"The right people." {n}She repeats it without inflection, and you are not sure whether she has decided to trust you or to watch you.{/n}
"Very well. When your business in the Abyss is finished, I will bring Starcatcher north, through the Wound, which no other captain in the Midnight Isles would be mad enough to fly. Cargo for your market and passengers for anywhere else. At my usual rates." {n}A small, crooked smile.{/n} "Minus nothing. You are not a noble mission. You are a customer."''',
       c("[Shake her hand on it.]")),
], requires=("trickster", PATTERN), forbids=(CHARTER, HIRED), device=False)


# --- 3. Landfall at Colyphyr (she arrived alive; inline on her Colyphyr list, before the farewell). -----------------

SCENES.append(scene(P + "colyphyr.landfall", "Landfall", "Mielarah", 4, '"Before you go back to your crew. A word."', [
    nar("start", '''{n}The crew are lashing Starcatcher to the stalagmites. Somewhere in the dark above the rocks, the thing that almost ate you on the approach is still circling, and every sailor on the deck keeps half an eye on the sky.{/n}
{n}Mielarah has taken off her hat. Without it she looks younger and more tired, and she is looking at you as if you were a column of figures that has, against all expectation, added up.{/n}''',
        c("Continue", "told", requires=(TOLD,)),
        c("Continue", "lied", requires=(MINDER,), forbids=(TOLD,)),
        c("Continue", "voyage", forbids=(MINDER,))),
    mi("told", '''"He's alive." {n}She nods along the deck, to where Oskel is coiling a line, never more than two strides from her. He has been at her elbow for the whole voyage, on his own stool, bought with her gold.{/n}
"He is alive, and I am alive, and you are alive, which on any ship of mine is a small miracle and on this voyage is three. Nothing went wrong enough. The curse never needed him."
{n}She does not smile.{/n} "But you would have spent him. I watched him every day and I knew exactly what he was for. I'm going to be angry about that for some time, Commander. I thought you should hear it from me before it turns into something else."''',
       c('"Be angry. You\'re both breathing."', "voyage", flags=(MEANT,)),
       c('"I\'d spend him again, if it kept you breathing."', "voyage", flags=(MEANT,))),
    mi("lied", '''"Oskel never left my elbow." {n}She glances down the deck at him, coiling a line two strides from her, as he has been every hour of the voyage.{/n} "The crew stopped counting the hammocks after the first week. You were right. They needed to see him there."
{n}And then, idly, because she is a magister and cannot leave a column of figures alone:{/n} "Though I've been wondering why it had to be Oskel. Any big man would have done for show. You asked me for the most dangerous one."''',
       c('[Tell her the truth] "Because your curse takes the nearest. I wanted it to take him and not you."', "confess",
         flags=(SECRET_KNOWN, MEANT)),
       c('[Lie] "The most dangerous man is the one the crew watches. That was the point."', "voyage")),
    mi("confess", '''{n}She does not move for a while. Oskel, down the deck, finishes coiling the line and starts another.{/n}
"You lied to me at my own table." {n}Very evenly.{/n} "You sat in the Bad Luck and told me a sensible thing, and I thanked you for it."
"He's alive. That is the only reason I am still speaking to you." {n}She breathes out.{/n} "And the worst of it is that I understand the arithmetic perfectly. I'd have done the same sum. I simply would never have done it to him."''',
       c("Continue", "voyage")),
    mi("voyage", '''"Well. We're here." {n}She looks out at the black rocks of Colyphyr and the lights of Hepzamirah's lair beyond them.{/n} "I pronounced the expedition complete. I have never pronounced it with such relief."
"I have been near a great many people when trouble came, Commander, and I have buried most of them. You stood on my deck through all of that, and you walked off it without a scratch."''',
       c('[Ask about the mutiny] "Your amulets. I made you use them."', "amulets", requires=(AMULETS,)),
       c('[Ask about the mutiny] "The limericks. Tell me they worked on you too."', "limericks", requires=(LIMERICKS,)),
       c("Continue", "tally", forbids=(PATTERN,)),
       c("Continue", "close", requires=(PATTERN,))),
    mi("amulets", '''{n}Her hand goes, without her meaning it to, to the pocket of her coat where the amulets are kept.{/n}
"You demanded that I calm them, and I did. Twenty men, all at once, like dolls on one string." {n}She takes the hand away.{/n} "The one who started it walked to the rail and stepped off. I felt him wake up halfway down. I will feel that for the rest of my life."
"You did the right thing as captain. I did the right thing as captain. It is a thing I would pay a great deal never to have done."''',
       c("Continue", "tally", forbids=(PATTERN,)),
       c("Continue", "close", requires=(PATTERN,))),
    mi("limericks", '''{n}Her mouth twitches, and she fights it, and loses.{/n}
"You climbed my rigging in front of twenty armed men and recited a limerick about the Lady in Shadow that I will not repeat, and then another about a demon lord and a goat, and they laughed until they wept." {n}She shakes her head.{/n} "In six years my amulets have never once made anybody laugh. They make them stop. That's all they do. They make them stop."
"I don't know whether to be grateful or professionally insulted."''',
       c("Continue", "tally", forbids=(PATTERN,)),
       c("Continue", "close", requires=(PATTERN,))),
    mi("tally", '''"I lost men on this voyage. That is a good voyage, for me: I can still count them on one hand." {n}She says it the way she said the list in the Bad Luck: worn smooth.{/n} "One fell from the yard on a calm morning with the sun out. One choked on a fishbone at my own table, at my elbow, while I was telling him a joke."
{n}You have heard enough of her list now to hear the shape inside it.{/n}''',
       c('[You see more than other people] Look at the space beside her.', "sight", requires=(SIGHT,), mythic="Trickster"),
       c('[Perception DC 24] Think about where each of them was standing.',
         check=dict(Skill="SkillPerception", DC=24, Success="rule", Failure="close", CommanderOnly=True)),
       c('[Lore (Religion) DC 24] Think about what a herald of Zyphus would want with a tally.',
         check=dict(Skill="SkillLoreReligion", DC=24, Success="rule", Failure="close", CommanderOnly=True)),
       c("[Say nothing.]", "close")),
    nar("sight", '''{n}Something leans at her shoulder, patient as a gravedigger, its blank regard resting not on her but on the nearest sailor at the rail. When he moves off, it turns to the next. You have seen this before, perhaps, without knowing what you saw.{/n}''',
        c('"It doesn\'t aim. It takes whoever is standing nearest you."', "rule")),
    mi("rule", '''"Nearest." {n}She hears it, and you watch her go back through six years of names in the space of a breath: the steward, the mate, the girl with the apples, the man with the fishbone.{/n}
"Nobody ever told me it had a rule." {n}Her voice has gone thin.{/n} "I am a certified specialist in resolving magic-related issues, Commander, and I have been sitting next to the answer for six years."''',
       c("Continue", "close", flags=(PATTERN,))),
    mi("close", '''{n}She puts her hat back on, and with it the captain.{/n}
"I will be flying back to the Midnight Isles tonight, before the thing in the sky decides it is hungry again." {n}A pause, as if she has come to the edge of a chart.{/n} "Unless there is some other destination you would like to recommend."''',
       c('"Drezen. When the Abyss is done with me, bring your ship north. My city needs a ship that stops for people in distress."', "north",
         flags=(LANDFALL, STARTED)),
       c('[Flirt] "Somewhere I can see you again without a demon lord\'s daughter in the next cave."', "flirt",
         flags=(LANDFALL, STARTED)),
       c('"Fair winds, Captain."', abort=True)),
    mi("north", '''"Through the Worldwound." {n}She says it the way another woman might say "through the fire".{/n} "No captain in the Midnight Isles would fly out through that sky. I have been wanting an excuse for years."
"I will come when my holds are full and my crew are paid. Cargo for your market, medicine for your hospitals, and passengers for anywhere that isn't a war." {n}She offers her hand, and it is a captain's grip: short, dry, final.{/n} "Look for my flag over your walls, Commander. And keep somebody sensible standing nearest you until then."''',
       c("[Let her go back to her crew.]")),
    mi("flirt", '''{n}She looks at you from under the brim of the hat, and for once the smile gets all the way to her eyes.{/n}
"That is a very poor line, and you are very lucky that I have spent six years among pirates, whose lines are worse." {n}She considers.{/n} "Your crusade has a city in Golarion, I'm told. Drezen. I have never flown out through the Worldwound. No sane captain has."
"When my holds are full, I'll come. Don't read anything into it. It will be business." {n}She turns away, and then back.{/n} "Mostly."''',
       c("[Let her go back to her crew.]")),
], requires=("trickster.ever", ARRIVED), forbids=(LANDFALL,), last=4, Relationship=REL, Chapters=[4],
    AnswerLists=[COLYPHYR_LIST], NativeReturnCue=COLYPHYR_RETURN))


# --- 3b. The landfall missed (she reached Colyphyr alive and the Commander left without a word): her letter. --------

remote(P + "colyphyr.letter", "A letter through a small door", [
    nar("start", '''{n}A portal no bigger than a dinner plate opens in the air beside your pack, lets a folded letter fall out, and closes again with a smell of tar and wind. The hand is a magister's, small and upright and very clear.{/n}''',
        c("Read it.", "letter")),
    mi("letter", '''"Commander. You left my deck at Colyphyr without the customary word, which I have decided to attribute to Hepzamirah rather than to manners. I am told you survived her, which is more than most people manage near me, and a great deal more than most manage near her."
"Starcatcher will be flying north by spring, through the Worldwound, with cargo for any city fool enough to buy it. Drezen is a city. If there is a berth for an honest ship over your walls, answer this. If not, don't; I dislike being refused in writing."
"Fair winds. M."''',
       c("[Write back: there is a berth for her ship over Drezen.]", "answered", flags=(LANDFALL, STARTED)),
       c("[Put the letter away and don't answer.]", flags=(CLOSED,))),
    nar("answered", '''{n}You write three lines. The small door opens beside your pack before the ink is dry, and takes them.{/n}''',
        c("[Close the pack.]")),
], requires=("trickster.ever", ARRIVED), forbids=(LANDFALL, KILLED), delay=72, kind="letter")


# --- 4. The raid: the curse takes the man on the rope (the device's payoff; her return, in person, in Chapter 4). ---

remote(P + "raid.rope", "The man on the rope", [
    nar("start", '''{n}A doorway of salt light opens beside your bedroll in the dark, and wind comes through it, and then Mielarah.{/n}
{n}She has a scarf wound high around her throat, and when she sits down on your pack without asking, the scarf slips. The rope has left a band of raw purple under her jaw, with the pattern of the lay pressed into it like a seal in wax. Her voice, when it comes, is a rasp.{/n}''',
        c("Continue", "rope")),
    mi("rope", '''"I protested your raid. You'll remember. I called you a pirate, and worse, in front of the whole crew." {n}She touches the scarf.{/n} "They smelt blood in the water. They came round me like dogs round a fallen horse, and I didn't have time for a single spell."
"Oskel had the noose on me before I'd finished the sentence. He was nearest, you see. He was always nearest. He threw the line over the main yard and he hauled, and my boots came off the deck."''',
       c("Continue", "block")),
    mi("block", '''"And the block at the yardarm split." {n}She says it with a kind of wonder.{/n} "Ironwood, three years old, rated for a ton. It came apart like a dropped plate. The yard swung down, the line went round his arm, and it took him over the rail."
"He had wings, Commander. He was the one man on that ship who could not die of a fall. His wings fouled in the ratlines as he went over, and he hung there by one arm and one wing, and then the line ran out, and he didn't."
{n}She is quiet.{/n} "The noose went slack. I was on the deck with my face in the tar, and I had exactly enough breath for the southern wind. So I called it. It blew all night."''',
       c("Continue", "crew")),
    mi("crew", '''"Nobody came near me after that. Not one of them. They stood at the far rail all night, watching me breathe, and in the morning they put their knives on the deck without being asked."
"At Colyphyr I didn't come out of my cabin. I heard you disembark. I didn't trust myself to look at you." {n}Her hand tightens on the scarf.{/n} "After, I put the eleven men who had held that rope off on the first rock with water on it. My code says I never ignore those in distress." {n}A very thin smile.{/n} "They weren't in distress until I left them there. I have decided that counts."''',
       c("Continue", "told", requires=(TOLD,)),
       c("Continue", "lied", forbids=(TOLD,))),
    mi("told", '''"You told me why, at my own table. I told him, and I paid him his freedom, and he spent it sitting next to me." {n}She looks at you, and her eyes are perfectly dry.{/n} "So we did it together, the three of us. You chose him, I paid him, and he stayed. And he's dead, and I'm alive, and his wings are somewhere at the bottom of the Ishiar, with my gold in his shirt."''',
       c("Continue", "raid")),
    mi("lied", '''"You told me a cursed captain makes a crew nervous." {n}Her voice is flat.{/n} "I lay on that deck all night with nothing to do but think, and I am a certified specialist in resolving magic-related issues, Commander. By morning I had it. The most dangerous man. Nearest. Always."
"You lied to me at my own table, so that my curse would take my bosun instead of me. And it did." {n}She breathes, carefully, around the bruise.{/n} "I should like very much to hate you for it. I'm finding it harder than it ought to be."''',
       c("Continue", "raid", flags=(SECRET_KNOWN,))),
    mi("raid", '''"And there is the raid. I haven't forgotten the raid. There were children in that village, Commander, and fishing nets, and nothing worth a single sack of flour to anyone but them." {n}She holds your eyes.{/n} "Tell me why I should be sitting here at all."''',
       c('"I ordered the raid. You protested, and you were right, and it nearly killed you."', "owned",
         flags=(RAID_OWNED,)),
       c('"I ordered the raid. I\'d order it again. Your crew just had worse manners than I did."', "unrepentant",
         flags=(RAID_UNREPENTANT,), alignment=("Evil", 1))),
    mi("owned", '''"Right." {n}She tastes the word.{/n} "I was right, and they hanged me for it, and you're sorry. That is more than any other captain in the Midnight Isles would have said. It is considerably less than I'd like."''',
       c("Continue", "oskel")),
    mi("unrepentant", '''"Worse manners than you." {n}She laughs, and it hurts her, and she does it anyway.{/n} "Kerz would have said that. Every pirate I have ever wanted to see hanged would have said exactly that."
"I'll remember you said it. I'm a magister; we keep accurate records."''',
       c("Continue", "oskel")),
    mi("oskel", '''"Now Oskel." {n}She unwinds the scarf, and folds it in her lap, and lets you look at the rope's work.{/n} "Say it. Whatever it is, say it to this."''',
       c('"I chose him. I\'d choose him again, if it kept you breathing."', "chose",
         flags=(RETURNED, STARTED, OSKEL_DEAD, NOTICED, ROPE_SECRET)),
       c('"It was your curse that took him. Not me."', "deflect",
         flags=(RETURNED, STARTED, OSKEL_DEAD, NOTICED, DEFLECTED, ROPE_SECRET))),
    mi("chose", '''{n}She nods slowly, as if you have confirmed a figure she already had.{/n}
"At least you don't lie about it now." {n}She winds the scarf back on.{/n} "My code is three lines. You have made me break the third of them. My crew was my cargo, and I let you spend a man of it, and I'm alive because of it, and I don't know what that makes me."''',
       c("Continue", "shovel")),
    mi("deflect", '''"My curse took him." {n}She says it back to you without heat.{/n} "Your hand put him there. A curse is a rock, Commander. You are the one who steered."
"Don't do that. You're better than that, and I have no patience left for people who are worse than they need to be."''',
       c("Continue", "shovel")),
    mi("shovel", '''"There's something else." {n}She hesitates, which you have not seen her do.{/n} "The night after, I dreamt of a spade. Not digging for me. It has never dug for me. It was digging somewhere else, slowly, like a man who has all the time in the world."
"I have met the Gravedragger once, in Abaddon, and I took a party of Pathfinders out of his hands. He never forgave it. I think he has noticed that somebody else has started stealing from him." {n}She looks at you.{/n} "I think it was digging for you."''',
       c('"Let it dig."', "north"),
       c('"Then I\'ll have to keep standing where it can\'t reach me."', "north")),
    mi("north", '''"Brave, or careless. I keep saying that about you." {n}She stands, and the portal brightens behind her.{/n}
"I'm flying Starcatcher north when your war goes home. I have cargo for Drezen, and passengers who would rather be anywhere else, and a hold full of rope I intend to sell." {n}At the threshold she stops.{/n} "Not for you. Don't flatter yourself."
{n}And then, without turning round:{/n} "Mostly not for you."
"One more thing. You keep paladins, I'm told. They will have a short word for what we did at Vazglar, and eleven sailors on a rock already know the story. I would rather your paladins heard it from you than from a drunk in a tavern." {n}The portal takes her.{/n}''',
       c("[Let her go.]")),
], requires=("trickster.ever", DEAD_LATCH, MINDER), forbids=(RETURNED,), delay=24,
    TricksterDevice=True, TricksterState="raid")


# --- 4b. The eleven on the rock (the raid's second beat: her code against her hangmen). ---------------------------

ROCK_SAVED = P + "rock.saved"
ROCK_LEFT = P + "rock.left"
ROCK_SLAVERS = P + "rock.slavers_refused"

remote(P + "raid.rock", "The eleven on the rock", [
    nar("start", '''{n}The door of salt light opens beside your bedroll again, a little after midnight, and she does not come through it. She stands on the far side, on her own deck, with the wind pulling at her coat and the scarf, and speaks across the threshold as if it were a rail between two ships.{/n}
"I went back to the rock." {n}Her voice is still a rasp, but steadier.{/n} "The one where I put the eleven off. I told myself I was checking the charts. I was not checking the charts."''',
        c("Continue", "rock")),
    mi("rock", '''"The water I left them is gone. They were drinking it too fast, the way men do when they're frightened, and the barrel split in the sun." {n}She does not say whose fault that was; she does not need to.{/n} "Two of them are dead already. One tried to fly for the next island and didn't reach it. The other one fell off the edge of the rock in his sleep. I heard about that one from the others, shouting it up at my hull."
"Nine left. They saw Starcatcher's lanterns and they stood on the edge of the rock and waved their shirts at me. The same men. The same hands." {n}She touches the scarf.{/n} "And I stood at my rail and I could not remember what my own code says."''',
       c("Continue", "code")),
    mi("code", '''"That's a lie. I remember it perfectly. I never ignore those in distress. They are in distress. It is not complicated." {n}She laughs, or tries to.{/n} "It is only that I have never before had the people in distress be the people who put a noose on me, while the man who ordered the raid they hanged me over is lying in his bedroll across the threshold, perfectly comfortable."
"You gave the order that started all of this, Commander. So you can help me finish it. Tell me what I do with them. I'll decide for myself in the end. But I want to hear what you'd say."''',
       c('"Take them off the rock. Put them ashore somewhere with bread and a harbour, and let them go."', "saved",
         flags=(ROCK_SAVED,), alignment=("Good", 1)),
       c('"Leave them. They made their choice when they picked up the rope."', "left", flags=(ROCK_LEFT,)),
       c('"Sell them to the slavers of Nahyndri. Their price will pay your new crew\'s wages."', "slavers",
         flags=(ROCK_SLAVERS,), alignment=("Evil", 1))),
    mi("saved", '''{n}She closes her eyes, briefly, like a woman setting down something heavy.{/n}
"Yes. That's what the code says. It's what I knew it said. I only wanted someone else to say it out loud, so I wouldn't be the only fool on this plane who believed it."
"I'll put them down on the quays at Alushinyrra, where there's a harbour and a chandler who owes me money. I'll give them a week's bread. I will not give them their knives back." {n}A thin smile.{/n} "And not one of them will ever stand within ten strides of me again, for their own sakes. I'm sure they'll understand."''',
       c("Continue", "after")),
    mi("left", '''"They made their choice." {n}She repeats it slowly, testing the weight of it.{/n} "Yes. They did. They picked up the rope and they hauled, and some of them were smiling."
{n}She stands there a long while, in the wind, on the other side of the door.{/n} "I'm going to fly past that rock twice more on the way home, Commander. They'll wave their shirts at me both times. And both times I'll hear my own voice, in the Bad Luck, telling a stranger that I never ignore those in distress."
"Maybe I'll stop. Maybe I won't. I haven't decided. You've given me your answer. It's a hard one, and it's honest, and I'll carry it for you."''',
       c("Continue", "after")),
    mi("slavers", '''{n}Her face goes perfectly still.{/n}
"Sell them." {n}She says it the way she said Nearest, in the Bad Luck, as though repeating a wrong answer.{/n} "To Nahyndri. I took Oskel off a Nahyndri slaver's deck with a brand on his neck and three dead men behind him, and you're telling me to put nine more on one, so I can pay my wages."
"No." {n}The word is very quiet and absolutely final.{/n} "I'll take them off the rock myself, and put them down somewhere with a harbour, and pay their bread out of my own pocket, and I will remember, for the rest of my life, that you told me to sell them." {n}She looks at you across the threshold.{/n} "I asked. That was my mistake. I won't ask you about my code again."''',
       c("Continue", "after")),
    mi("after", '''{n}The wind comes through the door and brings the smell of tar and cold sky into your camp.{/n}
"Go back to sleep, Commander." {n}She reaches for the edge of the portal, as if it were a door on a hinge.{/n} "I'll be over Drezen when your war goes home. I said I would. I keep my word, even to people who give me terrible advice."''',
       c("[Let the door close.]")),
], requires=("trickster.ever", RETURNED, DEAD_LATCH), forbids=(ROCK_SAVED, ROCK_LEFT, ROCK_SLAVERS, CLOSED), delay=48)


# --- 4b2. The Commander at her elbow (11 §2's other prepared choice): nearest at the hanging, the Commander cuts the
# line before the haul; the curse's accident finds the Commander and cannot finish a mythic body. Nobody else dies; the
# cost is the Gravedragger's mark for life, and his notice.

remote(P + "raid.elbow", "Nearest", [
    nar("start", '''{n}You remember it in pieces, afterwards. Her voice at Vazglar, calling you a pirate and worse in front of the whole crew. The crew closing round her like dogs round a fallen horse. And you, at her elbow, where you had said you would be every hour, so that when the slip noose went over her head you were the nearest living thing to her on the ship.{/n}
{n}Your knife was out before the line went taut. It parted the rope a hand above the knot, and she went down on the deck, and you went down with her, and the man on the other end of the line sat down hard with nothing to haul.{/n}''',
        c("Continue", "block")),
    nar("block", '''{n}Then the block at the end of the main yard, which had taken the line's first jerk, turned once, and its pin sheared, and it came down forty feet.{/n}
{n}It took you across the shoulder instead of the skull, because you are what the Wound made you and a sailor is not, and the collarbone went with a sound like a snapped oar. You did not let go of her. With the breath the noose had left her she called the southern wind, and the ship leaned away from Vazglar, and nobody on that deck came within ten strides of either of you again.{/n}
{n}When the bruise came up, it came up grey, the grey of turned earth, in the shape of a spade's blade. It has not faded.{/n}''',
        c("Continue", "cabin")),
    mi("cabin", '''{n}She comes to you the next night, in the cabin they gave you, with a scarf wound high round her throat, and sits on your sea chest without asking. Her voice is a rasp, but it is hers.{/n}
"I told you so. In the Bad Luck, in front of witnesses." {n}Her eyes go to your shoulder, to the place under the sling where the grey spade is.{/n} "I felt it come down. Six years I have watched the Gravedragger collect whoever stands nearest, and for the first time I watched him collect, and not finish."
"He has your measure now. He has put his mark on you like a surveyor's peg. Don't you dare think that was cheap."''',
        c("Continue", "eleven")),
    mi("eleven", '''"The eleven who held the rope, I'll put off on the first rock with water on it." {n}A very thin smile.{/n} "My code says I never ignore those in distress. They won't be in distress until I leave them there. I have decided that counts."
"And there is the raid. There were children in that village, Commander, and fishing nets, and nothing worth a single sack of flour to anyone but them. Tell me why I should be sitting here at all."''',
        c('"I ordered the raid. You protested, and you were right, and it nearly killed you."', "owned",
          flags=(RAID_OWNED,)),
        c('"I ordered the raid. I\'d order it again. Your crew just had worse manners than I did."', "unrepentant",
          flags=(RAID_UNREPENTANT,), alignment=("Evil", 1))),
    mi("owned", '''"Right." {n}She tastes the word.{/n} "I was right, and they tried to hang me for it, and you stood where the curse could reach you and you're sorry. That is more than any other captain in the Midnight Isles would have done. I haven't decided yet whether it's more than I'd like."''',
        c("Continue", "north")),
    mi("unrepentant", '''"Worse manners than you." {n}She laughs, and it hurts her, and she does it anyway.{/n} "Every pirate I ever wanted to see hanged would have said exactly that, and not one of them would have stood under my yard for it. I'm a magister; I keep accurate records. I'll put both in the book."''',
        c("Continue", "north")),
    mi("north", '''"I'm flying Starcatcher north when your war goes home, with a new crew, none of them within two strides of me." {n}She stands.{/n} "Cargo for Drezen. Passengers for anywhere else. Not for you." {n}At the door she stops.{/n} "Mostly not for you. Keep that shoulder out of the rain."''',
        c("[Let her go.]", flags=(RETURNED, STARTED, ZYPHUS_MARK, NOTICED))),
], requires=("trickster.ever", DEAD_LATCH, SELF), forbids=(MINDER, RETURNED, CLOSED), delay=24, chapters=(4, 5),
    TricksterDevice=True, TricksterState="raid")


# --- 4c. Nobody at her elbow: the hanging with no bosun posted (the late recovery, dearer than the minder). ----------
# Cue_0482 as the curse would play it with nobody posted: the first man to lay hands on her noose is the nearest, and
# the curse takes him (Cue_0044/0048: those near her die, and she does not). The rest will not go near her again, so
# they re-reeve the line to the capstan and haul from the far side of the deck: slow work, and a slow strangling rather
# than a drop. Those minutes are the whole recovery. The Commander is ashore with the raiding party they ordered, a
# quarter-mile off; Oskel, who stood at the rail, flies ashore with the word and back with the Commander. The rope is
# still a rope: whoever cuts her down stands nearest. The cost is heavier than the minder's: Oskel is spent by an order
# given on the spot, unpaid and unchosen; the rope had her long enough that her voice never comes back clear; and she
# knows the Commander prepared nothing.

remote(P + "raid.wind", "The capstan", [
    nar("start", '''{n}Afterwards, what you remember of Vazglar is the time. How little of it there was, and how much of it the crew of Starcatcher spent being afraid of her.{/n}
{n}You were ashore with the raiding party you had ordered down, a quarter-mile of shingle below the ship, when something big came down in the middle of the fishing village, folding its wings with a noise like a sail being struck. A tiefling of the Midnight Isles, broad as a hatch cover, with a slaver's brand gone white on the side of his neck. Oskel, her bosun. When she stood on her own quarterdeck and called you a pirate in front of the whole crew, he was at the rail. He was still at the rail when the crew came round her.{/n}
{n}"Commander." He is breathing hard, and his voice is low and careful, like a man carrying something full to the brim. "They're hanging the captain."{/n}''',
        c("[Listen.]", "head")),
    nar("head", '''{n}He says it fast, the way a bosun reports damage.{/n}
{n}"Hesk put the noose on her. Pulled it snug, stepped back onto the main hatch grating, and the grating went. Rotten, and none of us knew. He went into the hold head first and broke his neck on the ballast." He touches the back of his own neck, low down. "Six years every man aboard's seen that happen near her. Now they've seen it happen on the rope."{/n}''',
        c("Continue", "yard")),
    nar("yard", '''{n}"So nobody'll go near her. They're reeving the line through the block at the yardarm and down to the capstan, so's they can walk her up from the far side of the deck, eleven men on the bars at the full stretch of 'em." His yellow eyes are steady. "That's slow work, the reeving. And a capstan don't drop a body. It lifts her. That's a strangling, not a neck broke. Minutes, Commander. Not many."{/n}''',
        c("Continue", "rule", requires=(PATTERN,)),
        c("Continue", "folk", forbids=(PATTERN,))),
    nar("rule", '''{n}You read her rule at her own table in the Bad Luck. The curse does not aim. It takes whoever stands nearest when trouble comes, and it has never once taken her. It has never once saved her, either: it has only ever taken the people beside her. It took the man who fitted her noose, because he was nearest. It will do nothing at all about the rope. A rope is not an accident.{/n}
{n}What it has done is teach eleven frightened men to keep their distance, and distance is slow. That is all the time there is.{/n}''',
        c("Continue", "refused", requires=(REFUSED,)),
        c("Continue", "why", forbids=(REFUSED,))),
    nar("folk", '''{n}"Six years I sailed with her." Oskel says it quickly, as if he has been saying it to himself the whole way down. "Seen men go over the side next to her. Seen a mast come down either side of her. Seen a girl choke on an apple across a counter from her. Never a scratch on the captain."{/n}
{n}"Rope's different. Rope ain't an accident. Rope'll do what rope does, and she's on it."{/n}''',
        c("Continue", "why")),
    nar("refused", '''{n}You had more than the rule, once. You had a man to post at her elbow, and you took the order back because she asked you to. This is what the taking back has bought: a quarter-mile of shingle, a capstan, and nobody near enough to die for her.{/n}''',
        c("Continue", "why")),
    nar("why", '''{n}"Why me?" you ask him. "You could have cut her down yourself."{/n}
{n}"Past eleven knives, on my own, and nearest when I got there?" He does not look away. "'Cause you're captain till the expedition's done. That was the arrangement. 'Cause you gave the order for the raid." A pause. "'Cause I stood at the rail. Figured I'd better fetch somebody who didn't."{/n}''',
        c('[Take hold of his harness.] "Fly."', "moorings"),
        c('"She\'s dead, Oskel. Let her go."', "leave")),
    nar("leave", '''{n}He hears it without any change in his face. Then he nods once, the way a bosun acknowledges an order he did not want, and opens his wings, and goes.{/n}
{n}Nobody on Starcatcher goes near the mainmast that afternoon. The wind that gets up out of the south as the capstan stops blows all night long, and in the morning the crew tell you, carefully, from the far side of the deck, that the captain died in a few seconds.{/n}''',
        c("[Put it out of your mind.]", flags=(CLOSED,))),
    nar("moorings", '''{n}He takes you under the arms without another word and goes up. The village drops away, and the shingle, and a quarter-mile of grey surf goes under your boots with the wind tearing at your eyes, and then Starcatcher is below you, riding at anchor forty feet over the water.{/n}
{n}The capstan is going round. Eleven men lean on the bars at the full stretch of the deck, as far from the mainmast as the ship allows, and the pawls clack, one, and another, and up at the end of the main yard, with her hands tied behind her and her boots a man's height off the planking, Magister Mielarah of the Arcanamirium is being lifted by inches. Her heels are still moving. Her mouth is working at a word it has no breath to say.{/n}
{n}Oskel drops you on the quarterdeck. The man at the head of the bars is the quartermaster, a one-horned man called Dask, and he lets go with one hand and takes up a boarding cleaver.{/n}
{n}"Leave her be, passenger." His voice cracks. "Hesk's in the hold with his neck broke. Go near her and you're next. And if she comes down, she'll have the lot of us."{/n}''',
        c('[Intimidation DC 26] "Stand off the bars, Dask, or I put you on the rope beside her."',
          check=dict(Skill="CheckIntimidate", DC=26, Success="stood_down", Failure="knife", CommanderOnly=True)),
        c('[Diplomacy DC 26] "She\'s alive. When she wakes, she\'ll remember who let go of the bars, and who didn\'t."',
          check=dict(Skill="CheckDiplomacy", DC=26, Success="stood_down", Failure="knife", CommanderOnly=True)),
        c("[Draw steel and walk through them.]", "knife")),
    nar("stood_down", '''{n}Nobody moves. Then Dask takes his hands off the bar as if it had burned him, and the others let go after him, and the pawl drops and holds. The eleven go back along the deck, a step and another, until they are pressed against the forecastle rail.{/n}''',
        c("Continue", "foot")),
    nar("knife", '''{n}Dask comes at you first, because he is more frightened of her than of you. You put the man behind him on the deck, and the one behind that, and every one of them is a breath she does not take. Then the cleaver opens your forearm from wrist to elbow, down to the bone, and the deck is suddenly slick. Oskel takes Dask by the wrist and breaks it, quite slowly, the way a man breaks a stick for kindling, and the rest of them let go of the bars and go back to the forecastle rail and stay there. The pawl drops and holds.{/n}
{n}You bind the arm with a strip of sailcloth later. It will close. It will not close clean.{/n}''',
        c("Continue", "foot", flags=(HANGMAN_KNIFE,))),
    nar("foot", '''{n}At the foot of the mast you look up. Her heels have stopped. The line runs up to the block at the end of the yard and down to her, and the knot sits under her chin, where a man puts it when he fits a noose at arm's length and steps back quick. Walking the capstan back would take a minute she does not have, and someone would still have to take the knot off her on the deck. Somebody has to take her weight and cut, now. Whoever is holding her when the line parts will be the nearest living thing to her on this ship.{/n}
{n}Oskel looks at you. He knows the sum, and he knows you know it.{/n}''',
        c('[Give the order] "Go up, bosun. Cut her down, and hold her."', "cut",
          flags=(CUT_DOWN, OSKEL_DEAD, MEANT, NOTICED, HUNG, YARD_SECRET), alignment=("Evil", 1)),
        c('"No. Leave her where she is."', "leave"),
        c('[Mobility DC 24] "Stand clear, all of you." Stand under her yourself, nearest, and cut the line with a thrown knife.',
          check=dict(Skill="SkillMobility", DC=24, Success="thrown", Failure="climbed", CommanderOnly=True))),
    nar("thrown", '''{n}You send Oskel to the forecastle with the others and stand alone at the foot of the mast, directly under her, the only living thing within ten strides. The knife turns twice in the grey light and parts the line a hand above the knot.{/n}
{n}She comes down into your arms like a sack of wet sailcloth, and you go to your knees on the deck with her and get your fingers under the knot, and for one breath you are exactly where every name in her book once stood.{/n}''',
        c("Continue", "struck")),
    nar("climbed", '''{n}The first knife goes wide over the rail. The second bites the yard and hangs there. So you send Oskel to the forecastle with the others and go up the ratlines yourself, and out along the footrope with the line humming beside your face, and saw through it with your belt knife while you hold her against you with your other arm. Her face is dark and her lips are blue. You come down the backstay with her over your shoulder, burning your palm to the meat, and kneel on the deck with her and get your fingers under the knot, and for one breath you are exactly where every name in her book once stood.{/n}''',
        c("Continue", "struck")),
    nar("struck", '''{n}The block at the end of the yard has taken the jerk of the haul and every clack of the capstan without a creak. With nothing hanging from it, it turns once in the wind, and the pin that holds it shears, and it comes down forty feet.{/n}
{n}It takes you across the shoulder instead of the skull, because you are what the Wound made you and a sailor is not, and the collarbone goes with a sound like a snapped oar. You do not let go of her. Afterwards, when the bruise comes up, it comes up grey, the grey of turned earth, in the shape of a spade's blade, and it does not fade. The ship's surgeon at Colyphyr looks at it and will not touch it.{/n}''',
        c("Continue", "breath_marked", flags=(CUT_DOWN, ZYPHUS_MARK, NOTICED, HUNG))),
    nar("breath_marked", '''{n}Under your good hand, the knot comes loose, and she coughs.{/n}
{n}It is a terrible sound, dry and torn, like canvas ripping. Her chest heaves once, twice, and then she is breathing, in long ragged pulls, with her eyes open on the sky. The first breath she has any use of she spends, being who she is, on one cracked word of the Arcanamirium, and out over the sea the southern wind gets up. It blows all night long. After a while her eyes find the block on the deck beside you, and your shoulder, and then your face.{/n}
{n}She tries to speak again. Nothing comes. She takes your hand instead, and turns it over, and with one cold finger writes on your palm, one letter at a time, the way a magister writes in the margin of a text she disputes: W. H. Y.{/n}''',
        c("[Stay with her until morning.]")),
    nar("cut", '''{n}"Aye," says Oskel. That is all.{/n}
{n}He goes up on his wings with his knife in his teeth, and when he reaches her he does not hesitate at all. He takes her round the waist with one arm, lifts her an inch to slack the line, and cuts. Then he brings her down to the deck at your feet, slowly, the way you would lower a sleeping child, and kneels, and works the knot loose with his big scarred fingers, and straightens her collar.{/n}
{n}The block at the end of the yard has taken the jerk of the haul and every clack of the capstan without a creak. With nothing hanging from it, it turns once in the wind, and the pin that holds it shears, and it comes down forty feet and takes him on the back of the head.{/n}
{n}He dies on his knees beside her, with his hand still at her collar. It is quick. It is entirely pointless. Nothing on the ship moves.{/n}''',
        c("Continue", "breath")),
    nar("breath", '''{n}Under his hand, she coughs.{/n}
{n}It is a terrible sound, dry and torn, like canvas ripping. Her chest heaves once, twice, and then she is breathing, in long ragged pulls, with her eyes open on the sky. The first breath she has any use of she spends, being who she is, on one cracked word of the Arcanamirium, and out over the sea the southern wind gets up. It blows all night long. After a while her eyes find Oskel, and the block beside him, and then you.{/n}
{n}She tries to speak again. Nothing comes. She takes your hand instead, and turns it over, and with one cold finger writes on your palm, one letter at a time, the way a magister writes in the margin of a text she disputes: W. H. O.{/n}''',
        c('"I sent him up."', "told_her"),
        c("[Close your hand over hers. Say nothing.]", "silent")),
    nar("told_her", '''{n}She looks at you for the space of three breaths. Then she turns her head, and looks at Oskel, and does not look away again until the forecastle crew, at your order and from as far off as they can manage, come with a sailcloth to take him below.{/n}''',
        c("[Stay with her until morning.]")),
    nar("silent", '''{n}She does not need you to say it. She is a magister of the Arcanamirium and she can count, even now: the line, the knot, the yard, the one man on the ship who could reach it, and the passenger who brought him back. She takes her hand out of yours, and puts it on Oskel's sleeve, and leaves it there.{/n}''',
        c("[Stay with her until morning.]")),
], requires=("trickster.ever", DEAD_LATCH), forbids=(MINDER, SELF, RETURNED, CUT_DOWN, CLOSED), delay=24, chapters=(4,),
    TricksterDevice=True, TricksterState="raid")


remote(P + "raid.whisper", "What the rope kept", [
    nar("start", '''{n}A doorway of salt light opens beside your bedroll in the dark, and wind comes through it, and then Mielarah.{/n}
{n}She has a scarf wound high around her throat, and she sits down on your pack without asking. Above the scarf the rope has left her face grey and hollowed, and there are small burst vessels in the whites of her eyes, like red thread. When she speaks it is barely a whisper, and every word costs her.{/n}''',
        c("Continue", "voice")),
    mi("voice", '''"You'll have to lean in. This is all there is." {n}She touches the scarf.{/n} "The healers in Alushinyrra say it will come back, after a fashion: a rasp, never clear again. Orders I can manage, if the crew lean in. Spells are harder. Half of what I know has to be spoken clearly, and I am relearning it in this, like a child learning her letters."
"I have a portal left. You see I kept that one."''',
        c("Continue", "tidy")),
    mi("tidy", '''"I remember the capstan. One pawl, and another. I could not breathe, and I could feel every one of them in my head, the way I always feel them, leaning on the bars as far from me as my own deck allowed." {n}Her mouth twists.{/n} "So I tidied. It was the only thing I had left to do. And then one of them was not on the bars. He was going away from me, fast, over the water, and I knew where. Then nothing, until a hand on the knot."''',
        c("Continue", "oskel", requires=(OSKEL_DEAD,)),
        c("Continue", "marked", forbids=(OSKEL_DEAD,))),
    mi("marked", '''"And you stood under me yourself." {n}Her eyes go to your shoulder, to the place under your shirt where the grey spade is.{/n} "I felt that. It was the first thing I felt, coming back out of nothing: you, nearest, with your fingers under the knot, and the block coming down. It was the first time in six years I have felt the Gravedragger miss."
"It didn't miss, of course. It never misses. It only took less than it wanted, because you are not made of the same stuff as a steward with a tray." {n}Her whisper hardens.{/n} "He has your measure now. He has put his mark on you like a surveyor's peg. Don't you dare think that was cheap."''',
        c("Continue", "rule", requires=(PATTERN,), forbids=(REFUSED,)),
        c("Continue", "refused", requires=(REFUSED,)),
        c("Continue", "eleven", forbids=(PATTERN,))),
    mi("oskel", '''"He came back. That was the last thing I had before the nothing: a steady, careful sort of man in my head, coming back over the water to me, carrying something full to the brim. When I woke, his hand was on my collar." {n}She stops. The whisper will not do what she wants it to.{/n}
"You sent him. You stood at the foot of my mast and did the sum, and it came out Oskel, and you said so aloud." {n}Her eyes are perfectly dry.{/n} "He was the one man on my ship I had never paid, and he went for nothing, because you told him to."''',
        c("Continue", "rule", requires=(PATTERN,), forbids=(REFUSED,)),
        c("Continue", "refused", requires=(REFUSED,)),
        c("Continue", "eleven", forbids=(PATTERN,))),
    mi("rule", '''"And you had the rule. You read it at my table, in the Bad Luck, and I thanked you for it. And then you walked me to Vazglar with nobody at my elbow at all, and gave the order for a raid, and let the sum work itself out on my main yard." {n}A breath, very careful.{/n} "I am a magister of the Arcanamirium. I know the difference between an accident and a thing somebody did not trouble to prevent."''',
        c("Continue", "eleven")),
    mi("refused", '''"You had the rule, and a man, and you took it back because I asked you to. I asked. I will carry that half, Commander; it is mine." {n}Her fingers tighten on the scarf.{/n} "The other half is the rope. That half is yours."''',
        c("Continue", "eleven")),
    mi("eleven", '''"The eleven I put off on the first rock with water on it. Dask went with his wrist in a splint." {n}A very thin smile.{/n} "My code says I never ignore those in distress. They were not in distress until I left them there. I have decided that counts."''',
        c("Continue", "raid")),
    mi("raid", '''"And there is the raid. I haven't forgotten the raid. There were children in that village, and fishing nets, and nothing worth a single sack of flour to anyone but them." {n}She holds your eyes.{/n} "Tell me why I should be sitting here at all."''',
        c('"I ordered the raid. You protested, and you were right, and it nearly killed you."', "owned",
          flags=(RAID_OWNED,)),
        c('"I ordered the raid. I\'d order it again. Your crew just had worse manners than I did."', "unrepentant",
          flags=(RAID_UNREPENTANT,), alignment=("Evil", 1))),
    mi("owned", '''"Right." {n}She tastes the word.{/n} "I was right, and they hanged me for it, and you're sorry. That is more than any other captain in the Midnight Isles would have said. It is considerably less than I'd like."''',
        c("Continue", "two_nights")),
    mi("unrepentant", '''"Worse manners than you." {n}She laughs, and it tears in her throat, and she does it anyway.{/n} "Every pirate I ever wanted to see hanged would have said exactly that. I'm a magister; I keep accurate records. I'll remember you said it."''',
        c("Continue", "two_nights")),
    mi("two_nights", '''"I will forgive you the raid, one day. I can feel it coming, and I resent it." {n}She draws the scarf a little higher.{/n} "I don't know about the rope, nor about what it cost at the foot of my mast. I shall keep them where I keep everything, in the book, and look at them when I can bear to."
"The night after, I dreamt of a spade. It wasn't digging for me. It has never dug for me. It was digging somewhere else, slowly." {n}She looks at you.{/n} "Somebody has been stealing from the Gravedragger, and he has noticed who."''',
        c('"Let it dig."', "north", flags=(RETURNED, STARTED)),
        c('"Then I\'ll stand where it can\'t reach me."', "north", flags=(RETURNED, STARTED)),
        c('"Go home, Captain. You owe me nothing, and I\'ve cost you enough."', "gone", flags=(CLOSED,))),
    mi("north", '''"Brave, or careless. Everyone says one or the other about you." {n}She stands, and the portal brightens behind her.{/n}
"I'm flying Starcatcher north when your war goes home, with a new crew, hired at double wages, none of them within two strides of me. Cargo for Drezen. Passengers for anywhere else." {n}At the threshold she stops.{/n} "Not for you. Don't flatter yourself."
{n}And then, without turning round, in the whisper that is all she has for now:{/n} "Mostly not for you. And tell your paladins about the yard yourself, before a drunk in a tavern does it for you."''',
        c("[Let her go.]")),
    mi("gone", '''{n}She considers you, as if checking a figure she thought she had.{/n}
"You're right. I don't." {n}She stands, and the portal brightens behind her.{/n} "Fair winds, Commander. Keep somebody sensible standing nearest you. I shan't be there to count them."''',
        c("[Let her go.]")),
], requires=("trickster.ever", DEAD_LATCH, CUT_DOWN), forbids=(RETURNED, CLOSED), delay=48,
    TricksterDevice=True, TricksterState="raid")


# --- 5. The storm: word at the aeronauts' taverns (the Commander's act), then the survivor (her return). ------------

remote(P + "storm.word", "Word at the Bad Luck", [
    nar("start", '''{n}You dream of the wheel. Her hands on it, and the ship climbing into the eye of the storm, and her face getting darker minute by minute, as if something were coming up the companionway behind her that only she could hear. Then her hands opening. Then the Ishiar.{/n}
{n}You wake with salt in your mouth that isn't there. Starcatcher the Third is gone. Her crew went off toward the horizon on their own wings, the few who had them. Nobody saw what became of the captain.{/n}''',
        c("Continue", "known", requires=(PATTERN,)),
        c("Continue", "unknown", forbids=(PATTERN,))),
    nar("known", '''{n}But you think you know the rule, and nothing since has argued with it. Her curse does not aim, and it has never once aimed at her. Starcatcher the First went down in a storm and she walked away from it. Starcatcher the Second broke on the rocks and she walked away from that with a chipped tooth. Everything near her dies of accidents, and nothing happens to her. It never does.{/n}
{n}She is alive somewhere on the Ishiar. You would stake the crusade on it.{/n}''',
        c("[Send word to every aeronauts' tavern in the Midnight Isles: the passenger lived, and is waiting for the captain.]",
          flags=(WORD,)),
        c("[Let her go.]", "let_go")),
    nar("unknown", '''{n}You think about the story she told you in the Bad Luck: the Gravedragger, the curse, the two ships lost before this one. Starcatcher the First went down in a storm, and she walked away. Starcatcher the Second broke on the rocks, and she walked away from that too.{/n}
{n}Everything near her died, and nothing happened to her. If you could be sure of why, you would know whether to look for her.{/n}''',
        c('[Lore (Religion) DC 28] Work out what a herald of Zyphus would want with her.', requires=(TOLD_CURSE,),
          check=dict(Skill="SkillLoreReligion", DC=28, Success="reasoned", Failure="diviner", CommanderOnly=True)),
        c("[Pay a diviner of the Midnight Isles to look for her.]", "paid", crusade=("Finances", -300)),
        c("[Let her go.]", "let_go")),
    nar("reasoned", '''{n}Zyphus's priests hold that no death is written in advance; an accident does not aim, it collects. Her curse has never collected her. It collects whoever is standing nearest when trouble comes, and leaves her in the middle of the wreckage without a scratch, to count. She is alive. She is always alive.{/n}''',
        c("[Send word to every aeronauts' tavern in the Midnight Isles: the passenger lived, and is waiting for the captain.]",
          flags=(WORD, LATE, PATTERN))),
    nar("diviner", '''{n}You get as far as the Gravedragger and no further. What a herald of the god of pointless death wants with one woman is a question for priests you do not have.{/n}''',
        c("[Pay a diviner of the Midnight Isles to look for her.]", "paid", crusade=("Finances", -300)),
        c("[Let her go.]", "let_go")),
    nar("paid", '''{n}The diviner is a thing with too many eyes that works out of a teahouse in Alushinyrra and charges in advance. It looks into a bowl of seawater for a long time and then laughs, a wet little laugh.{/n}
{n}"The Gravedragger's pet? Of course she's alive. Nothing near her lives, and nothing kills her. She's floating on a hatch cover two hundred miles south, cursing in three languages." It holds out a hand for the rest of the fee.{/n}''',
        c("[Send word to every aeronauts' tavern in the Midnight Isles: the passenger lived, and is waiting for the captain.]",
          flags=(WORD, LATE))),
    nar("let_go", '''{n}She let go of the wheel. You let go of her. The Ishiar keeps what it is given.{/n}''',
        c("[Put it out of your mind.]", flags=(CLOSED,))),
], requires=("trickster.ever", STORM_LATCH), forbids=(WORD, RETURNED, CLOSED), delay=72, kind="event",
    TricksterDevice=True, TricksterState="storm")

remote(P + "storm.survivor", "The survivor", [
    nar("start", '''{n}She comes through a portal the size of a door, into your camp, in borrowed clothes: a sailor's jersey too big for her and a Midnight Isles oilskin with somebody else's name inked on the collar. Her hat is gone. Her hair has dried stiff with salt. There is not a mark on her.{/n}
"The Bad Luck gave me your message." {n}Her voice is flat and hoarse.{/n} "'The passenger lived.' Somebody had pinned it over the bar with a knife. You are a very peculiar person, Commander."''',
        c("Continue", "wheel")),
    mi("wheel", '''"You ordered me into that storm. You'll remember that. And I took the helm, and I nodded, and I meant it." {n}She sits, carefully, as if the ground might pitch.{/n}
"Then it came up behind me. I can't describe it better than that. Every captain I have ever lost, standing on the companionway at my back, and the wind in the sails sounding like a spade in wet earth. And I thought: it's going to be the passenger this time. The one who reads rules. I felt my hands open."
"I let go of the wheel, Commander. I have been flying ships since I was fourteen, and I let go of the wheel."''',
       c("Continue", "oskel", requires=(MINDER,)),
       c("Continue", "hatch", forbids=(MINDER,))),
    mi("oskel", '''"Oskel caught it." {n}She looks at her own hands.{/n} "He was at my elbow, where you'd put him, and when my hands came off the spokes his went on. He held her a whole minute, head into the wind, all by himself. I have never seen a man hold a wheel like that."
"Then the mainmast came down across the helm. It did not touch me. It never does." {n}Her voice does not change.{/n} "He was nearest. You knew he would be."''',
       c("Continue", "hatch", requires=(TOLD,)),
       c("Continue", "worked_out", forbids=(TOLD,))),
    mi("worked_out", '''"You told me a cursed captain makes a crew nervous. You told me to let them see a big man at my back." {n}She says it slowly, as if reading it off a slate.{/n}
"Three days on a hatch cover is a long time to think, Commander, and I am a certified specialist in resolving magic-related issues. You didn't want a bodyguard. You wanted a lightning rod. You lied to me at my own table so that my curse would have somebody to take who wasn't me." {n}Her hands close in her lap.{/n} "And it did."''',
       c("Continue", "hatch", flags=(SECRET_KNOWN,))),
    mi("hatch", '''"I came up under a hatch cover and held on to it for three days. Nothing ate me. Nothing ever does. On the fourth day a Nahyndri fishing skiff took me aboard, and on the fifth its mast snapped in a flat calm and killed the man who'd pulled me out of the water." {n}A small, terrible smile.{/n} "You see how it is."
"And now here you are, alive, and so am I. I've lost Starcatcher the Third. I have lost her crew. Tell me what you want to say about it, because I have been rehearsing both halves of this conversation for a week."''',
       c('"I ordered you into that storm. It was the wrong order."', "owned",
         flags=(RETURNED, STARTED, SHIP_LOST, STORM_OWNED, NOTICED, OSKEL_DEAD, ROPE_SECRET), requires=(MINDER,)),
       c('"I ordered you into that storm. It was the wrong order."', "owned",
         flags=(RETURNED, STARTED, SHIP_LOST, STORM_OWNED, NOTICED), forbids=(MINDER,)),
       c('"You let go of the wheel, Captain. Not me."', "blamed",
         flags=(RETURNED, STARTED, SHIP_LOST, STORM_BLAMED, NOTICED, OSKEL_DEAD, ROPE_SECRET), requires=(MINDER,)),
       c('"You let go of the wheel, Captain. Not me."', "blamed",
         flags=(RETURNED, STARTED, SHIP_LOST, STORM_BLAMED, NOTICED), forbids=(MINDER,))),
    mi("owned", '''"The wrong order." {n}She lets out a long breath.{/n} "Yes. It was. And I obeyed it, and then I failed at it. We are going to argue about which of those is worse for the rest of our lives, I expect."
{n}She looks down at her hands again, and turns them over.{/n} "It's a strange comfort, having somebody else to blame. I haven't had one in six years."''',
       c("Continue", "fourth")),
    mi("blamed", '''{n}She takes it without flinching. You suspect she has said it to herself every hour since the hatch cover.{/n}
"Yes. I did. You gave a stupid order and I carried it out, and then I let go." {n}Her jaw sets.{/n} "Since I was fourteen, and I let go. Say it as often as you like; you can't say it more often than I do."''',
       c("Continue", "fourth")),
    mi("fourth", '''"Something else, since we're being honest. On the hatch cover, the second night, I dreamt of a spade. It wasn't digging for me. It has never dug for me. It was digging somewhere far off, slowly, like a man with all the time in the world."
"I think the Gravedragger has noticed you, Commander. You stood on my deck and read his rule like a chart, and he doesn't like being read." {n}She gets up.{/n}
"You paid me a fare to Colyphyr and I didn't earn it. So I'm going to spend it. There is a sloop for sale in Alushinyrra, twenty years old and ugly as sin, and she will be Starcatcher the Fourth by the end of the month. And then I'm going to fly her north, to Drezen, and deliver you the rest of what you paid for."''',
       c('"I\'ll be waiting."', "go"),
       c('"Drezen\'s a long way through a bad sky."', "go")),
    mi("go", '''"Through the Worldwound. No captain in the Midnight Isles would fly out through that sky." {n}A thin, stubborn smile.{/n} "I have a great deal to prove, and nobody left to be careful for."
{n}The portal opens again behind her. She pauses in it.{/n} "Keep someone sensible standing nearest you, Commander. It's watching."''',
       c("[Let her go.]")),
], requires=("trickster.ever", WORD), forbids=(RETURNED, CLOSED), delay=48)


# --- 6. The charter, for a Commander who sailed with Kerz or Nocticula's captain (Chapter 5, her letter). ----------

remote(P + "charter.letter", "Through the Worldwound", [
    nar("start", '''{n}The letter is written on the back of a bill of lading from the Bad Luck. The hand is small and upright and very clear, and has pressed hard enough in two places to tear the paper.{/n}''',
        c("Read it.", "letter")),
    mi("letter", '''"Commander. You sat at my table and read my curse like a chart, which no one in six years had managed, and then you went to Colyphyr with" {n}a word is scratched out here, so hard that the nib went through{/n} "another captain. I hear you survived the voyage. I am told the voyage did not enjoy you."
"I hold no grudge; I am a professional. Starcatcher is flying north with cargo, through the Worldwound, which no captain in the Midnight Isles would dare. If Drezen wants an honest ship, write. If it doesn't, I shall sell my rope elsewhere. M."''',
       c("[Write back: Drezen wants an honest ship. And its captain.]", flags=(CHARTER, STARTED)),
       c("[Leave it unanswered.]", flags=(CLOSED,))),
], requires=("trickster.ever", PATTERN), forbids=(CHARTER, HIRED, CLOSED), delay=24, chapters=(5,), kind="letter",
    RequiresAnyGroups=[[KERZ, NOCTA]])


# --- 6b. The spade (Chapter 5, the Commander alone: the Gravedragger has noticed; the finale hook). ---------------

DREAMT = P + "cost.dreamt"

remote(P + "spade.dream", "The spade", [
    nar("start", '''{n}You dream of a grey plain under a grey sky, flat to every horizon, and of a sound.{/n}
{n}Somebody is digging. You can't see him at first. Then you can: far off, and very tall, with his back to you, driving a spade into the grey ground and lifting it out again with the unhurried patience of a man who is paid by the day and has no intention of finishing early. Behind him, on a chain, he drags something you do not let yourself look at.{/n}
{n}The hole he is digging is exactly your length. You can tell that from here.{/n}''',
        c("Continue", "measure")),
    nar("measure", '''{n}He stops. He does not turn round. He takes a knotted cord from somewhere about him and holds it up against the horizon, as if measuring the distance between the two of you, and counts the knots with a long grey finger, and puts it away.{/n}
{n}Then he goes back to digging. He is in no hurry. He has, you understand, all the time in the world, and he knows exactly where you are standing, and who is standing nearest you.{/n}''',
        c('[Call to him] "You\'ll need a longer cord. I don\'t keep still."', "wake"),
        c("[Say nothing. Watch him dig.]", "wake"),
        c('[Trickster] "Dig it a foot short. I\'ll lie in it with my knees up and ruin your whole morning."', "wake",
          mythic="Trickster")),
    nar("wake", '''{n}He does not answer. He does not have to. The spade goes into the grey earth, once, and again.{/n}
{n}You wake in Drezen with the taste of cold soil in your mouth, and there is grey grit under your fingernails that you did not put there. It washes off. It takes three washings.{/n}
{n}Somewhere a hundred fathoms over the city, a ship with three lanterns in a line rides at anchor, and her captain, you would bet the crusade on it, is awake too.{/n}''',
        c("[Wash your hands a third time.]", flags=(DREAMT,))),
], requires=("trickster.ever", NOTICED, MORNING), forbids=(DREAMT, CLOSED), delay=24, chapters=(5,), kind="event")


# --- 7. Reactions (Lann and Woljif, each behind their own availability guard). ------------------------------------

SCENES.append(reaction("Woljif", P + "react.woljif_oskel", (OSKEL_DEAD,),
    '''"Chief. Word in the Midnight Isles is, you put the biggest, meanest sailor in the sky next to the cursed lady on purpose. So he'd be the one it got." {n}Woljif rubs the back of his neck.{/n}
"That's the coldest thing I ever heard, and I grew up in Alushinyrra. Remind me never to stand next to you in a thunderstorm."''',
    answer_list=WOLJIF_HUB, forbids=(*WOLJIF_GUARD, CUT_DOWN), chapter=4, last=5, entry='"About Mielarah..."', portrait="Woljif"))

SCENES.append(reaction("Woljif", P + "react.woljif_yard", (CUT_DOWN, OSKEL_DEAD),
    '''"Chief. Word in the Midnight Isles is, the cursed lady's crew strung her up off her own yard at Vazglar, and nobody'd go near, and then you come flyin' back off the raid and sent her big bosun up there with a knife. Knowin'." {n}Woljif rubs the back of his neck.{/n}
"I grew up in Alushinyrra. I seen people do colder. I just never seen 'em do it so tidy. Remind me never to climb nothin' for you."''',
    answer_list=WOLJIF_HUB, forbids=WOLJIF_GUARD, chapter=4, last=5, entry='"About Mielarah..."', portrait="Woljif"))

SCENES.append(reaction("Lann", P + "react.lann_captain", (FLOWN,),
    '''"She let me take the wheel. For a count of ten." {n}Lann looks at his own hands as if they belong to someone luckier.{/n}
"I told her it's the best job in the whole world. She said I'd stolen her line, and that she'd let it go this once, and then she showed me how the ropes run. I'm keeping a place for a grumpy boatswain. Just so you know."''',
    answer_list=LANN_HUB, forbids=LANN_GUARD, chapter=5, last=5, Chapters=[5], entry='"You went up on Mielarah\'s ship?"',
    portrait="Lann"))

SCENES.append(reaction("Lann", P + "react.lann_spade", (NOTICED, MORNING),
    '''"Commander, don't laugh. Last night I dreamt about a man digging. Not a grave. Just digging, very slow, somewhere a long way down." {n}Lann scratches his ear.{/n}
"Mongrels don't dream much. I asked the captain about it. She went white and told me to sleep on the other side of the barracks from you. Is that a joke? Nobody ever tells me the jokes."''',
    answer_list=LANN_HUB, forbids=LANN_GUARD, chapter=5, last=5, Chapters=[5], entry='"Something bothering you?"',
    portrait="Lann"))


# --- 8. Epilogue pages (no effects; after the route's own flags). ------------------------------------------------

EP = dict(last=6, Relationship=REL)

SCENES.append(scene(P + "epilogue.committed", "", "MielarahEpilogue", 6, "", [
    nar("page", '''{n}After the war, Starcatcher flew the long routes: Absalom to the Mwangi, the Mwangi to the Shackles, and once, for a very great deal of money, the Worldwound's old sky to a Drezen that no longer needed defending. Her captain was a magister of the Arcanamirium who kept accurate records and would not carry slaves, and there were stories about her in every port, most of them about the curse.{/n}
{n}The stories left something out. On Starcatcher's quarterdeck there was a place at the captain's elbow, half a stride from the wheel, where no sailor was ever posted and no passenger was allowed to stand. The crew called it the Commander's place. When the Commander came aboard, the Commander stood there, nearest, for the whole of every voyage, and nothing happened. Nothing ever did.{/n}''',
        c("[Close the book.]"),
        paragraphs=(
            p("{n}Oskel's name was painted on the stern under the ship's own, in small white letters that were renewed every spring. She never explained it to passengers. The Commander never asked her to.{/n}", requires=(OSKEL_DEAD,)),
            p("{n}Oskel stayed aboard as bosun for eleven years and never once stood at her elbow again. When he retired to a quiet life on a quiet plane, it was on gold she paid him, and the last thing he said to the Commander was \"I know what I was for.\" It was not unkind. It was not kind either.{/n}", requires=(MEANT,), forbids=(OSKEL_DEAD,)),
            p("{n}Starcatcher the Fourth was an ugly sloop and stayed one. Her captain refused every offer to replace her. \"This one,\" she said, \"I keep.\"{/n}", requires=(SHIP_LOST,)),
            p("{n}Her crew served without amulets. Some of them deserted. Most of them stayed, and when they fought on deck it was over cards, and she let them.{/n}", requires=(FREED,)),
            p("{n}Her crew served with the amulets, closer than ever, and never once mutinied, and never once laughed. The Commander had asked for that. Neither of them spoke about it afterwards.{/n}", requires=(TIGHTENED,)),
            p("{n}On long night watches her crew recited limericks, badly and in rotation, and the worst offenders were made to climb the rigging to do it. Nobody on Starcatcher has stepped off the rail since.{/n}", requires=(LAUGHING,)),
            p("{n}Once a year, on the anniversary of Vazglar, she wore the scarf, and would not say why to anyone but the Commander.{/n}", requires=(RETURNED, DEAD_LATCH)),
            p("{n}The Commander carried a grey mark in the shape of a spade's blade on one shoulder for the rest of their life. Surgeons would not touch it. She would, sometimes, with two fingers, the way she corrected a helmsman.{/n}", requires=(ZYPHUS_MARK,)),
            p("{n}She gave her orders in a rasp for the rest of her life, and her crews learned to lean in. She never once told a passenger what had happened to her voice.{/n}", requires=(HUNG,)),
            p("{n}Nine men who had once hauled on a rope over Vazglar crewed honest ships in the Midnight Isles for the rest of their lives, and none of them would ever say her name in a tavern without standing up first.{/n}", requires=(ROCK_SAVED,)),
            p("{n}She flew past a certain rock in the Ishiar every year, and every year looked down at it, and never once let the Commander see her face while she did.{/n}", requires=(ROCK_LEFT,)),
            p("{n}She never again asked the Commander what her code required. She asked the Commander everything else.{/n}", requires=(ROCK_SLAVERS,)),
            p("{n}She had come to Drezen on a charter, as a professional, to a customer who had sailed with somebody worse. She never let the Commander forget it, and she never once charged the Commander a fare.{/n}", requires=(CHARTER,), forbids=(LANDFALL, RETURNED)),
            p("{n}She kept the Commander's promise in the same book as her dead, on its own page, and nobody who ever stood at her elbow again was put there by anyone but themselves.{/n}", requires=(D + "promised",)),
            p("{n}The Commander never promised, and she never asked again. She simply watched, every voyage, everyone who came near her, and the Commander watching them, and neither of them ever pretended otherwise.{/n}", requires=(D + "no_promise",)),
            p("{n}In Drezen they still tell the story of the Commander who walked through the market every week at the cursed captain's elbow, under the cornices and the scaffolds, on purpose, and never once had so much as a pot of geraniums fall on them.{/n}", requires=(D + "escorted",)),
            p("{n}She never forgot that the Commander had once offered to walk a condemned man beside her through a market like a dog on a leash. She forgave it, eventually. She kept a record of it anyway.{/n}", requires=(D + "offered_prisoner",)),
            p("{n}Some nights, when she could not sleep, she would take the half of a split ironwood block out of the Commander's coat pocket and turn it over in her hands, and put it back.{/n}", requires=(D + "last_night",), forbids=(OSKEL_DEAD,)),
            p("{n}Thirty-nine soldiers of the crusade came home from the Worldwound in her forward hold, and every one of them, when they could walk again, came to the hospital yard to stand under her ship and wave their hats at it. She never once came down to them. She counted the hats.{/n}", requires=(D + "wounded_carried",)),
            p("{n}She flew into the Wound for thirty-six soldiers without the Commander, and brought them home, and wrote four names in her book. It was a long time before she let the Commander read that page.{/n}", requires=(D + "wounded_left",)),
            p("{n}At the back of the book of her dead there was a page for the living, headed in her small hand: chose to stand there. It held one name for a long time. Later it held others, and she kept every one of them as carefully as the front.{/n}", requires=(D + "named",)),
            p("{n}And somewhere far below the clouds, patient as a man with all the time in the world, a spade went on digging for the Commander. It is digging still. It has not yet been allowed to finish.{/n}", requires=(NOTICED,)),
        )),
], requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.late", "", "MielarahEpilogue", 6, "", [
    nar("page", '''{n}The spring after Threshold, a ship with an anchor on her flag came down out of a clear sky over Drezen and hung there, a hundred feet up, while her captain let down a rope ladder and climbed to the bottom of it and did not step off.{/n}
"You turned for home, the last time I gave you my wheel," said Mielarah. "I have thought about it for a year. It was the right thing to do, and I have not forgiven you for it."
"I told you I would not ask you anything again, and I keep my word, even to you." {n}She did not hold out her hand. She only moved her boots to one side of the bottom rung, so that there was room on it for two.{/n} "I am not asking. I am telling you where the ladder is. The wheel is where you left it."''',
        c('[Take her hand and climb.]', "climb"),
        c('[Stay on the ground.]', "stay")),
    nar("climb", '''{n}The ladder swung under both of you all the way up, and she laughed at you the whole time, and at the top she put your hands on the spokes and took hers away. Starcatcher went north that afternoon, over the healed ground where the Worldwound had been, and held her course the whole way.{/n}'''),
    nar("stay", '''{n}She looked down at you for a while, swinging gently on the ladder over the rooftops. Then she nodded, as if a column of figures had come out the way she expected, and climbed back up. Starcatcher was over the horizon by evening. Every spring after that, a bill of lading arrived in Drezen for one passenger, fare paid, berth unassigned.{/n}'''),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))


def integrate(payload):
    """Register her presences, derived keys, world bindings and portrait fallback. Scenes are added by expansion.py."""
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    for kind, keys in BINDINGS.items():
        for key, value in keys.items():
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != value:
                raise ValueError("Conflicting world binding %s: %r vs %r" % (key, have, value))
            payload[kind][key] = value
    payload.setdefault("PortraitFallbacks", {}).setdefault("Mielarah", PORTRAIT_GUID)
