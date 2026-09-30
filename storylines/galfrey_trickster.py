"""Queen Galfrey on the Trickster path: "The Queen dies; Kitrane walks out" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, rewritten
2026-09-29 (R4) after the Astra design review r4, with its build sheet; it supersedes the permit device, the F19 drill and the
priced second ask of Writer/handoffs/trickster/galfrey.md, whose canon table and reactors stay valid).

Canon (blueprints.zip / enGB):
- Kitrane is hers: "I have introduced myself as Kitrane, an old friend of yours. I am a knight of a minor order, the Green
  Crows." (Galfrey_Incognito/Cue_0001 19d217c3); "It's been a long time since I traveled like this, as just another face in
  the crowd..." (Cue_0004 d5133def); "Don't forget, here I am Kitrane the knight." (Cue_0013 ee76d13d).
- Her life was never hers to spend: "the decision to prolong my life was not mine. It was the decision of the church of
  Iomedae. The sun orchid elixirs have been paid for by the church." (Cue_0010 85cfdab6); she weighs her own death
  politically: "My death or abduction would sow chaos among our forces." (Cue_0017 876d2164).
- Iz: the deathbed, "You have returned after all." (GalfreyOnTheEdge/Cue_0011_GalfreyDies 963c942b) and its list
  (AnswersList_0019 13487ef2); "It is no use. The dragon's sorcery has not merely wounded my body, it has rent my soul."
  (Cue_0073 a3167386, the clean return cue); Seelah at the bed: "Your Majesty! How did this...?" (Cue_0079 95037d69); the
  farewell, "Look, Commander. I am already knocking on Pharasma's door." (Cue_0053 a5e30e29) -> Cue_0061_ReturnLexicon ->
  Cue_0056 (GalfreyDead). The knight after it: "The Queen... is dead." (IrabethSurvives/Cue_0001 6c730e6c).
- Drezen after: "The Queen is gone. Even these words sound like heresy..." (Hulrun/Cue_0001 2bb2f939). Her farewell letter,
  found by the Storyteller's goblet: "I don't know where you are now. Are you even still alive? ... Forgive me."
  (GalfreyGoodbyeMessage e03b3cfc; StorytellerDangerousDrezen/Cue_0039 c0cf7ea6).

The device, and what is authored (labelled on the page as the Commander's gamble, never as a rule of the sorcery): the dragon's
sorcery has rent the soul of the Queen of Mendev, whose very life the church bought for the office. If the Queen dies in public
and the woman answers to another name, it may let go. Nobody knows. She chooses: asked for Mendev she refuses, asked for
herself she takes it. The native death plays; her last command, as Queen, sends the wounded knight Kitrane to the rear; a
Crows knight who died beside her goes home to Nerosyan in the Queen's sealed coffin. What the Commander saw at the bed decides
when the rending lets go: on the road (read), or only when Drezen proclaims her dead (blind: the tear stays in her voice).

Path fit (ROUTE-BRIEF-R, v1): the Chapter 2-4 beats are N-all (no Trickster gate, no flag the other paths lack); everything
from the offer at the deathbed on is T. Her fitting paths and her canon ending there are in the spec's "Path fit" section.
Where she lives, the native romance comes first: RRT only reads it (galfrey.romance_active), and Last Call and the Ledger count
her through galfrey.trickster.partner.
"""
from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "galfrey"
P = "galfrey.trickster."
E = "galfrey.early.kitrane"                         # the Chapter 2 scene (its id is also a flag once played)

DREZEN = "2570015799edf594daf2f076f2f975d8"         # DrezenCapital
DISGUISED = "a8b7f6fd39ff2974f8b5fbf944a7f735"      # QueenGalfreyDisguised: the Green Crows knight's plain armour
PORTRAIT_GUID = "a3ba06b4723c7a74fb5054ccb2289efb"  # the Galfrey book-picture fallback (rrt_portraits)
INCOGNITO_LIST = "f1225677b6e455a4db45f2ce77533816"  # NPC_Common/Galfrey_Incognito/AnswersList_0005 (Chapter 2 war camp)
INCOGNITO_BACK = "d5133deffe0362548bd2563ee5291eef"  # Galfrey_Incognito/Cue_0004 "...as just another face in the crowd..."
ARRIVES_LIST = "44704bddb6223b84989dd26bcf20b601"    # c3/Drezen_C3/GalfreyArrives/AnswersList_0004
ARRIVES_BACK = "21467e29a21d22b438eac99a34d8c09b"    # GalfreyArrives/Cue_0066, her re-greeting ("Are you ready?")
EDGE_LIST = "13487ef288faa30459888cdcce979b51"       # c5/Iz/GalfreyOnTheEdge/AnswersList_0019 (the deathbed)
EDGE_BACK = "a316738673dc6524eaeeb3feda0e9fe7"       # GalfreyOnTheEdge/Cue_0073 "It is no use. The dragon's sorcery..."
EDGE_FAREWELL = "a5e30e29364069446926ff78a73a026d"   # GalfreyOnTheEdge/Cue_0053 "...knocking on Pharasma's door" (-> GalfreyDead)
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"     # NPC_Common/Irabeth/AnswersList_0009
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"      # CompanionDialogues/Seelah/AnswersList_0003
HULRUN_HUB = "c9c1f633ee0f94e45b546c6243e251c2"      # c5/DrezenMain_C5/Hulrun/AnswersList_0005
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"      # Daeran's companion hub (as Terendelev's reaction uses it)
KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"         # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_BACK = "7b050ba0745bf144e815632e39b34853"    # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"

STARTED = "galfrey.started"
CLOSED = "galfrey.closed"
COMMITTED = "galfrey.committed"
# Native reads.
DEAD = "galfrey.dead"                     # GalfreyDead
KILLED = "galfrey.killed_by_commander"    # GalfreyKilledByCommander (a player-chosen kill closes the route: §5 ruling #2)
DYING = "galfrey.dying_seen"              # SeenCues GalfreyOnTheEdge/Cue_0011_GalfreyDies
ROMANCE = "galfrey.romance_active"        # GalfreyRomance_Active (read only; never started or completed here)
FINAL = "galfrey.final"
FINISHED = "galfrey.romance_finished"     # GalfreyRomance_Finished (133f3b1b), set at Threshold: the native romance completed
MANU = "iz.manuscripts"                   # GalfreyGoesToManuscripts (4b3f1b15): she was wounded by the priestess, not the dragon                   # Galfrey_Final: she is alive at the Coronation and after (activation: not dead)
LEFT_EARLY = "iz.left_early"              # DidntVisitedEvents: the Commander never came to Iz
MET = "galfrey.incognito_met"             # SeenCues Galfrey_Incognito/Cue_0001: "I have introduced myself as Kitrane"
SEELAH_BED = "galfrey.seelah_at_bed"      # SeenCues GalfreyOnTheEdge/Cue_0079: "Your Majesty! How did this...?"
FAREWELL = "galfrey.farewell_found"       # SeenCues StorytellerDangerousDrezen/Cue_0039: her hidden farewell letter
KC_KEPT = "galfrey.kc_after_fane"         # PlayerIsKnightCommanderAfterFane (the Commander kept the title into the Abyss)
CORONATION = "coronation.seen"
SIGHT = "trickster.perception_tier1"      # TricksterPerceptionTier1Feature (bound by Terendelev's route)
TERENDELEV_BACK = "terendelev.trickster.returned"   # read in node variants only
# Authored: Chapters 2 to 4 (N-all).
E_MOOTED = E + ".mooted"
E_REFUSED = E + ".refused"
CROWS = P + "ch3.crows"
CROWS_MOOTED = P + "crows_mooted"
CROWS_REFUSED = P + "crows_refused"
PRESSED = P + "crows_pressed"             # the Commander asked her to think again, as a friend
PRESSED_GENERAL = P + "crows_pressed_general"   # ...or as her general
LETTER = P + "ch4.letter"
LETTER_MOOTED = P + "letter_mooted"
LETTER_REFUSED = P + "letter_refused"
LETTER_BURNED = P + "letter_burned"
PLANTED = P + "kitrane_planted"
ADDRESS = P + "address_heard"             # Ch4: a hag of the Midnight Isles says a curse is an address (a market saying, labelled)
CARRIED_IRABETH = P + "carried.irabeth"   # who took the Queen's last command: Irabeth
CARRIED_CROWS = P + "carried.crows"       # ...or the Crows (Irabeth dead, or left in Drezen: PlayerIsKnightCommanderAfterFane)
CROWS_DREZEN = P + "carried.crows_drezen"  # the Crows carried her because Irabeth was holding Drezen (not because she was dead)
REPLIED = P + "iz.alone_replied"
LATE_FOUND = P + "cost.found_late"          # unprepared: found on the bier at Drezen, three days dead, the sergeant bought or faced          # the Commander wrote back to her letter from the rubble
NATIVE_REFUSED = "galfrey.native_refused" # SeenCues DrezenMain_C5/Galfrey/Cue_0041: "friendship is all I can offer you" (the Trickster's native answer)
BRIEFED_ID = P + "ch3.standing_orders"
BRIEFED = P + "crows_briefed"             # T, Chapter 3: the Commander gave the Crows standing orders (the offscreen escape needs it)
# Authored: the device (T).
OFFER = P + "iz.offer"
READ = P + "sorcery_read"                 # the dark light in the wound answered the title, and stilled at "Kitrane"
BLIND = P + "blind"                       # the Commander offered on nerve alone
OFFER_REFUSED = P + "offer_refused"       # asked for Mendev first; she refused, and named her condition
TAKEN = P + "kitrane_taken"
LET_DIE = P + "let_die"
RENT = P + "cost.rent_scar"               # blind or alone: the rending let go late; the tear in her voice for good
ALONE = P + "cost.alone"                  # she took the old offer by herself, with no Commander at her side
COFFIN = P + "cost.coffin"                # Sir Anselm Wray of the Crows went home to Nerosyan in her coffin, under her name
EULOGY = P + "cost.eulogy"                # the Commander's: the Queen's eulogy, delivered knowing it false
EULOGY_TRUE = P + "eulogy.true"
EULOGY_LEGEND = P + "eulogy.legend"
EULOGY_SIGN = P + "eulogy.sign"           # a line in it meant for one listener (Hulrun may have heard it too)
ROAD = P + "iz.road"
RETURNED = P + "returned"
PARTNER = P + "partner"                   # Derived: committed, or the native romance alive to the end (Last Call, the Ledger)
LIVED = P + "lived"                       # Derived: she lives past the Coronation, native romance or not
LATE_COMMITTED = P + "late_committed"
SECRET_KEY = "galfrey_eulogy"
SECRET = "trickster.secret." + SECRET_KEY
# Read from the courtship module (galfrey_kitrane); declared here so the pages and reactions can name them.
SWORN = P + "sworn"
DRILL = P + "morning_drill"
TENT = P + "tent_seen"
FOREVER = P + "kitrane_forever"
CROWN = P + "crown_reclaimed"
NAMED = P + "coffin.named"                # the Commander said Sir Anselm should have his name back one day
KEPT = P + "coffin.kept"                  # ...or that he chose to guard her, and still does
REFUSED_ORDER = P + "ride.refused_order"  # she refused an order of the Commander's at the ford (the prisoners)
DECLINED = P + "declined"                 # reserved: never set (her soft no is `sworn`); Last Call's declined slot

BINDINGS = {
    "SeenCues": {MET: ["19d217c3503c0304db4bec29c9882bc9"], NATIVE_REFUSED: ["36f61641ac48bb242b831fe30085ef40"],
                 SEELAH_BED: ["95037d694c52c964a8bf7b121b309caa"],
                 FAREWELL: ["c0cf7ea6c8f13434fa36671b3b81a2ab"]},
    "Etudes": {FINAL: "e9205b9f9e8ecd04c92852d72d09ca86", FINISHED: "133f3b1b38f04fa44be3200b786e437f",
               MANU: "4b3f1b15817e2034f85d7fa7b2a6f20a",
               KC_KEPT: "37a2df11c979ed446b6716142b2b01f5"},
}

DERIVED = {
    PLANTED: [[E_MOOTED], [CROWS_MOOTED], [LETTER_MOOTED]],
    # Last Call and the Ledger: the Kitrane world counts her by her commit; where she lives, by the native romance kept to
    # the end (Galfrey_Final plays only while she is alive, from the Coronation on).
    PARTNER: [[COMMITTED], [FINISHED, FINAL]],
    LIVED: [[FINAL]],
    # R2-6: she came back, and the war ended before the oath was answered either way.
    LATE_COMMITTED: [["trickster.ever", RETURNED, P + "first_morning"]],
    # 05 §2.5 voice note: she joins a household the way she joined the war camp, as one face in the crowd she chose.
    "galfrey.harem.voice.a_face_in_the_crowd": [[COMMITTED], [FINISHED, FINAL]],
}

RELATIONSHIP = dict(
    Title="Kitrane",
    Description=("In the war camp before Drezen, Queen Galfrey rode among the minor orders as Kitrane of the Green Crows, "
                 "an old friend of mine, and said it had been a long time since she had been just another face in the "
                 "crowd. Kitrane had no lands, no crown and no enemies. The Queen had all three."),
    Objective="Find out what is left of Kitrane",
    Guidance=("On the Trickster path, if the Queen lies dying at Iz, be at her side before she goes. What she has said of "
              "Kitrane before then, and what you see in her wound, will matter. If she lives, what she chooses with you is "
              "her own affair, and no business of any trick."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, KILLED], FailureFlags=[DEAD, KILLED],
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        # She died at Iz, at the Commander's side or alone; never when the Commander struck her down (canon stands).
        "dead": dict(detect=[DEAD, "!" + KILLED], device=P + "return.kitrane", returned=RETURNED),
    },
)

# Path fit tags (ROUTE-BRIEF-R v1): T = Trickster only (gated on trickster/trickster.ever); N-all = every path, no gate.
PATH_FIT = {}


def tag(scene_id, fit):
    PATH_FIT[scene_id] = fit


def conv(id, text, *choices):
    """Galfrey speaking inside her own native dialog."""
    return n(id, "conversant", text, *choices)


def ga(id, text, *choices, **kw):
    return n(id, "Galfrey", text, *choices, portrait="Galfrey", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Galfrey", **kw)


def page(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="visit", owner="Galfrey", **extra):
    SCENES.append(scene(id, title, owner, min(chapters), "", nodes, requires=tuple(dict.fromkeys(requires)),
                        forbids=tuple(dict.fromkeys(forbids)), delay=delay, last=max(chapters), Relationship=REL,
                        Chapters=list(chapters), Remote=True, Kind=kind, **extra))


# --- Chapter 2 (N-all, inline on her incognito list): the Kitrane question ------------------------------------------------

SCENES.append(scene(E, "Kitrane of the Green Crows", "Galfrey", 2, '"How is Kitrane finding the war camp?"', [
    conv("start", '''{n}The Queen's mouth twitches. She glances along the lines of the minor orders' tents, where a banner of three black birds on green is drying on a spear.{/n} "Kitrane finds it muddy, loud and badly provisioned, and she has never been so content. Her boots have been stolen twice. Nobody has ever stolen the Queen's boots." {n}She seems genuinely pleased about it.{/n} "Yesterday a sergeant of the Eagle Watch told her to get her shield off his firewood. I very nearly thanked him."''',
        c('"Has anyone guessed?"', "guessed"),
        c('"You sound as though you like her better than the Queen."', "like")),
    conv("guessed", '''"Anevia." {n}A dry smile.{/n} "She looked at me for about as long as it takes to count a purse, and then went off whistling. She has not said a word to anyone. That is how I know she knows." {n}The Queen flexes her fingers on the pommel of a very plain sword.{/n} "I have been found out, Commander, and I am being kept. It is a novel sensation."''',
        c("Continue", "like")),
    conv("like", '''"Like her." {n}She considers the word as if it had been handed to her on a tray.{/n} "I hardly know her. She is two weeks old. She sleeps under canvas, she queues for her supper, and when she says something foolish nobody writes it down." {n}Her gaze drifts over the camp: a quartermaster shouting, a boy leading two mules, knights of a dozen poor orders mending harness in the drizzle.{/n} "A queen is a thing that is watched. Kitrane is a thing that watches. I had forgotten how much there is to see."''',
        c("Continue", "romance", requires=("galfrey.romance_active",)),
        c("Continue", "ask", forbids=("galfrey.romance_active",))),
    conv("romance", '''{n}Then her eyes come back to you, and narrow a little.{/n} "Kitrane is also not in the habit of being flirted with by her commander in the middle of a supply line. I would take it kindly if you remembered that, in public." {n}A pause, precisely measured.{/n} "In public."''',
        c("Continue", "ask")),
    conv("ask", '''"But you did not come to ask after my boots." {n}She tilts her head.{/n} "You have the look of someone turning a thing over. Out with it, Commander. I have had a century of courtiers who approach a question by the long road."''',
        c('[As a friend] "Keep her. When this war is done, Kitrane could outlive the Queen. She has earned a longer life."', "mooted",
          flags=(E_MOOTED,)),
        c('[As her general] "If the Queen ever falls, Mendev could use a Kitrane in reserve to hold the line."', "refused",
          flags=(E_REFUSED,)),
        c('"Nothing. I only wanted to hear her laugh."', "laugh")),
    conv("mooted", '''{n}The Queen does not answer at once. The camp goes on around you both, the mules and the shouting and the drizzle, and for a breath she is only a tired woman in plain armour listening to it.{/n}
"Kitrane has no lands, no crown and no enemies." {n}She says it slowly, as though reading it off a ledger she did not expect to find.{/n} "Some days I envy her."''',
        c("Continue", "mooted_end")),
    conv("mooted_end", '''{n}Then she straightens, and the Queen is back in the set of her shoulders.{/n} "Idle talk. A monarch who envies her own disguise should take more exercise." {n}The corner of her mouth betrays her.{/n} "Don't forget, here I am Kitrane the knight. You may ask after her again, if you like. She will be here, stealing back her boots."''',
        c("[Leave Kitrane to her camp.]")),
    conv("refused", '''{n}The warmth goes out of her face as neatly as a blade goes into a scabbard.{/n} "A queen who rehearses her funeral has begun it." {n}She lets that stand a moment.{/n} "Mendev does not need a spare queen, Commander. It needs this one alive, which is a matter for my sword and your army, not for a borrowed name. I came here as Kitrane so that the demons would not know where the Queen was. I did not come here to practise being dead."''',
        c('"Understood, Your Majesty."', "refused_end"),
        c('"It was a question, not a plan."', "refused_end")),
    conv("refused_end", '''"Then it has an answer, and we need not speak of it again." {n}A breath, and something less stern.{/n} "You think like a general. I asked for one. I should not complain when I get one." {n}She nods toward the tents.{/n} "Go. Kitrane has a harness to mend, and she is very bad at it."''',
        c("[Leave her to it.]")),
    conv("laugh", '''{n}She does, which seems to surprise her more than you: a short, real laugh, too loud for a queen, that makes a knight at the next fire look up and then quickly down again.{/n} "That is either very gallant or very impudent. In this camp I am not obliged to decide which." {n}She shakes her head, still smiling.{/n} "Go on with you, Commander."''',
        c("[Leave her smiling.]")),
], requires=(MET,), forbids=(E_MOOTED, E_REFUSED), last=2, Relationship=REL, Chapters=[2],
    AnswerLists=[INCOGNITO_LIST], NativeReturnCue=INCOGNITO_BACK))
tag(E, "N-all")


# --- Chapter 3 (N-all, inline on GalfreyArrives): the Green Crows, mustered out ---------------------------------------------

SCENES.append(scene(CROWS, "The Green Crows", "Galfrey", 3, '"Did Kitrane come with you to Drezen, Your Majesty?"', [
    conv("start", '''{n}Something eases around the Queen's eyes for the space of a breath, and is put away again.{/n} "Kitrane was mustered out at the gates of Drezen. A short ceremony. I held it in my own tent, and I was the only one present." {n}She smooths a crease out of the Mendevian blue at her shoulder.{/n} "This city waited seventy years for its Queen to come through the gate. It did not deserve a knight of three black birds and a borrowed name. It deserved the crown, and so the crown came."''',
        c("Continue", "remember", requires=(E_MOOTED,)),
        c("Continue", "refused_before", requires=(E_REFUSED,)),
        c("Continue", "first", forbids=(E_MOOTED, E_REFUSED))),
    conv("remember", '''"And then you ask after her, as though she were a friend who had gone home on leave." {n}Her voice drops.{/n} "In the war camp you told me she could outlive the Queen. I have caught myself thinking about it at odd hours. It is a very poor habit in a monarch, Commander. I do not thank you for it."''',
        c('"But you haven\'t stopped thinking about it."', "admit"),
        c('"Then I apologise for the habit, and not for the thought."', "admit")),
    conv("admit", '''"No." {n}Very quietly.{/n} "Kitrane has no crown to fall off her head when she falls. There is something restful in that. I have told no one else so, and I shall deny it to anyone who asks, including you." {n}She looks toward the Fane, where the demons' barrier shimmers over the lower town, and back.{/n} "Keep her name for me, then. Somebody should."''',
        c('"I\'ll keep it."', "end", flags=(CROWS_MOOTED,)),
        c('[Trickster] "I keep all sorts of things. Most of them I stole."', "end", flags=(CROWS_MOOTED,), mythic="Trickster")),
    conv("refused_before", '''"You asked me once, in the war camp, whether Kitrane might hold the line if the Queen fell." {n}Cool, without heat.{/n} "I told you what I thought of rehearsing funerals. Nothing about Drezen has changed my mind. If you mean to ask me again, Commander, think carefully about how you ask."''',
        c("Continue", "frame")),
    conv("first", '''"Why do you ask? Kitrane was a convenience. A name for a camp." {n}She studies you, the prosecutor at her trial again.{/n} "Or do you mean something by it? You have the look you had at the war council, when you had seen a road nobody else had noticed."''',
        c("Continue", "frame")),
    conv("frame", '''{n}The Queen waits, one gauntleted hand resting on the hilt of her sword. Behind her, the tower where the Fane's barrier hums over the rooftops throws a cold light across the square.{/n}''',
        c('[As a friend] "Don\'t retire her. Kitrane deserves a longer war than the Queen will be given."', "mooted", flags=(CROWS_MOOTED,)),
        c('[As her general] "Keep her in reserve. If the Queen falls at the Fane, Kitrane could hold the line."', "refused",
          flags=(CROWS_REFUSED,)),
        c('"Only that I liked her. Forgive me, Your Majesty."', "liked")),
    conv("mooted", '''{n}She is silent long enough that a knight crossing the square slows, sees the Queen's face, and walks on faster.{/n}
"Kitrane has no lands, no crown and no enemies." {n}She speaks as if she has said it to herself before, in a tent, with nobody present.{/n} "Some days I envy her." {n}Then, crisply:{/n} "And some days I have a demon lord's temple to break open. Today is the second sort."''',
        c("[Say nothing more about it.]", "end")),
    conv("refused", '''"A queen who rehearses her funeral has begun it." {n}The words come out flat and practised; she has said them before, perhaps to herself.{/n} "Mendev does not keep a spare, Commander. It keeps faith. If I fall at the Fane, I shall fall as what I am, and the crusade will go on because it must, not because I left a costume in a trunk."''',
        c('[Let it go.] "As you say."', "end"),
        c('[Press her, as a friend] "Then forget Mendev for a moment. Think about it for yourself, and tell me after the Fane."', "pressed",
          flags=(PRESSED,)),
        c('[Press her, as her general] "Think about it anyway. Mendev can\'t afford a sentimental queen."', "pressed_general",
          flags=(PRESSED_GENERAL,))),
    conv("pressed", '''{n}Her eyebrows rise. For a moment she looks as if she might rebuke you; then something in her face turns inward, like a key in a lock.{/n} "For myself." {n}She says it as though it were a word in a foreign tongue.{/n} "For myself. That was hardly what I expected from my Commander." {n}She nods, once.{/n} "Very well. After the Fane. If there is an after."''',
        c("[Leave her to her thoughts.]", "end")),
    conv("pressed_general", '''"Sentimental." {n}The Queen's voice goes very even, which in Galfrey is worse than shouting.{/n} "I have buried three generations of knights in the Worldwound, Commander. I know exactly what Mendev can afford." {n}A pause.{/n} "But you are my general, and you have asked. I shall think on it tonight, as a general's advice. You will have your answer."''',
        c("[Bow, and leave her.]", "end")),
    conv("liked", '''"Liked her." {n}The Queen tilts her head, and very nearly smiles.{/n} "So did I. It is a pity she was so short-lived. Two weeks in the mud, and then a crown fell on her." {n}She lets the smile go.{/n} "Now. We were speaking of the Fane."''',
        c("[Return to the business of the Fane.]", "end")),
    conv("end", '''{n}Galfrey straightens her cloak and turns back toward the tower, and she is the Queen of Mendev again, entirely, from her boots to the set of her jaw.{/n}''',
        c("Continue")),
], requires=(), forbids=(CROWS_MOOTED, CROWS_REFUSED, DEAD), last=3, Relationship=REL, Chapters=[3],
    AnswerLists=[ARRIVES_LIST], NativeReturnCue=ARRIVES_BACK))
tag(CROWS, "N-all")


# --- Chapter 3 (T, a visit): standing orders for the Crows ----------------------------------------------------------------------
# The Trickster's preparation for the worst case (a death the Commander is not there for): orders, gold and a plan, given to the
# old sergeant of her bodyguard. Planned, not magical; the offscreen escape needs it.

page(BRIEFED_ID, "Standing orders", [
    nar("start", '''{n}The Green Crows who ride with the Queen keep a tent at the edge of the Drezen camp, apart from the grand orders, where nobody asks what three old knights and a squire are guarding. The sergeant is sixty, grey as a badger, and sharpening a sword that does not need it.{/n}
{n}He knows who you are. He knows, you suspect, exactly why you have come alone after dark.{/n}''',
        c('"If the Queen ever falls where I cannot reach her, I want the Crows to have orders."', "orders")),
    n("orders", "Crows' sergeant", '''"Orders." {n}He does not stop sharpening.{/n} "The Crows have one order, Commander. Stand next to her. We do it very badly; she will ride in front." {n}The stone stops.{/n} "Go on, then. What orders?"''',
        c('"If she is dying, and she calls herself Kitrane, you carry out Kitrane. Not the Queen. Whatever it costs, and whoever asks."', "why")),
    n("why", "Crows' sergeant", '''{n}He looks at you for some while.{/n} "She told us about that. The name. In the war camp. She said it like a woman says she would like to see the sea." {n}He sets the sword across his knees.{/n} "You want me to carry off the Queen of Mendev under a false name if she asks for it, and lie to every knight in the crusade." {n}A breath.{/n} "No. You want me to be ready to. She would have to ask. That is different."''',
        c("[Put a purse on his knee.] \"For a cart, a cloak, and a surgeon who does not know her face.\"", "take", flags=(BRIEFED,)),
        c('"She would have to ask. I want you ready if she does."', "take", flags=(BRIEFED,)),
        c('"Forget I came."', abort=True)),
    n("take", "Crows' sergeant", '''{n}He does not touch the purse, if there is one; he nods at it, the way a man nods at a debt he means to pay.{/n} "If she asks, it will be done. If she does not, I never saw you." {n}He goes back to his sword.{/n} "Sir Anselm will want to know. He is deaf. He will make me shout it. I shall tell him you came to buy a horse."''',
        c("[Leave the Crows to their tent.]")),
], requires=("trickster",), forbids=(BRIEFED, DEAD), delay=24, chapters=(3,), kind="visit", RequiresAnyGroups=[[E_MOOTED, CROWS_MOOTED, PRESSED]])
tag(BRIEFED_ID, "T")


# --- Chapter 4 (N-all, a memory in the Abyss): another face in the crowd ------------------------------------------------------

page(P + "ch4.crowd", "Another face in the crowd", [
    nar("start", '''{n}Alushinyrra never sleeps, but it dims. In the hour when the lanterns along the harbour burn lowest, you sit on a stone balcony above a market where half the faces are glamours and the other half are masks, and nobody is who they are selling.{/n}
{n}A succubus goes by below in the shape of a grey-haired matron. A mortal slaver goes by in the shape of nobody at all. You find you are thinking of the Queen of Mendev.{/n}''',
        c("Continue", "kept", requires=(KC_KEPT,)),
        c("Continue", "stripped", forbids=(KC_KEPT,))),
    nar("kept", '''{n}The last you saw of her, she was sending you into the Abyss with your title still yours, which half her court had called a mistake and the other half a punishment. She had not looked at you while she did it. She had looked at the wall behind you, the way people look at a map.{/n}''',
        c("Continue", "camp", requires=(MET,)),
        c("Continue", "queen", forbids=(MET,))),
    nar("stripped", '''{n}The last you saw of her, she was sending you into the Abyss with your rank taken from you in front of her court. She had done it cleanly, without a tremor in her voice, and she had not looked at you while she did it. She had looked at the wall behind you, the way people look at a map.{/n}''',
        c("Continue", "camp", requires=(MET,)),
        c("Continue", "queen", forbids=(MET,))),
    nar("camp", '''{n}Before that there was the war camp, and a knight in plain armour who had her boots stolen twice and laughed about it. Kitrane of the Green Crows: an old friend of yours, she told everyone, from a minor order nobody had heard of. "It's been a long time since I traveled like this," she said, "as just another face in the crowd."{/n}
{n}You look down at the market full of borrowed faces and wonder which of them are happy in them.{/n}''',
        c("Continue", "mooted", requires=(PLANTED,)),
        c("Continue", "refused", requires=(CROWS_REFUSED,), forbids=(PLANTED,)),
        c("Continue", "plain", forbids=(PLANTED, CROWS_REFUSED))),
    nar("queen", '''{n}Before that there was the Queen in Drezen, holding court in the square below the Fane: a woman of a hundred and more who looked nowhere near it, because the church of Iomedae had paid for every year of it. You spoke to her like a crowned head, and she answered like one, and you never saw anything else of her.{/n}
{n}You look down at the market full of borrowed faces and wonder what the Queen of Mendev would look like with nobody watching.{/n}''',
        c("Continue", "plain")),
    nar("mooted", '''{n}"Kitrane has no lands, no crown and no enemies," she said to you once, as if reading it off a ledger. "Some days I envy her." A careful person would write that down. You have. You are not entirely sure yet what you mean to do with it, which is how you know it matters.{/n}''',
        c("Continue", "address")),
    nar("refused", '''{n}"A queen who rehearses her funeral has begun it," she told you, when you asked her whether Kitrane could hold the line. It was a good answer. It was the answer of a woman who knows exactly what a queen's death is worth to her kingdom, and will not spend it as a hedge.{/n}''',
        c("Continue", "address")),
    nar("plain", '''{n}Somewhere up there, in Drezen or in Nerosyan, she is being the Queen of Mendev at somebody. You hope, a little to your own surprise, that she has an hour in the day when she is not.{/n}''',
        c("Continue", "address")),
    nar("address", '''{n}Below the balcony a masked woman is haggling with an old hag of the market over a charm against the evil eye. The hag laughs at her, not unkindly, and says a thing you find you remember: that in the Midnight Isles a curse is only an address. It finds you by what you answer to. That, she says, is what the masks are for.{/n}
{n}It is the sort of thing markets say. You turn it over anyway, the way you turn over everything, and put it away somewhere you will be able to find it again.{/n}''',
        c("[Watch the market until the lanterns brighten.]", flags=(ADDRESS,))),
], requires=(), forbids=(P + "ch4.crowd", DEAD), delay=24, chapters=(4,), kind="memory", owner="Memory")
tag(P + "ch4.crowd", "N-all")


# --- Chapter 4 (N-all, a letter): what she wrote the night before the Fane ----------------------------------------------------
# Written in Drezen before the assault, and put in the Commander's kit to be read after the battle; the Commander finds it at
# the first rest in the Abyss. It never crossed the Abyss by any post: nothing of hers could have (her farewell letter says she
# did not know where the Commander was).

page(LETTER, "A letter in your kit", [
    nar("open", '''{n}At the bottom of your kit, under a spare shirt you have not had occasion to change into since the Fane, there is a letter you did not pack. Folded in four, sealed with plain green wax and no device at all. On the outside, in a firm, old-fashioned hand: "To be read after the battle. K."{/n}
{n}It must have gone into your kit in Drezen, the night before the assault. You have carried it through the Fane and down into the Abyss without knowing it was there.{/n}''',
        c("[Break the green seal.]", "friend", requires=(PRESSED,)),
        c("[Break the green seal.]", "general", requires=(PRESSED_GENERAL,), forbids=(PRESSED,))),
    ga("friend", '''"Commander,
"You asked me to think about it for myself. I have been doing so since supper, which is why this is written by candlelight and not by a clerk.
"The Queen will do what she must tomorrow, and after tomorrow, whatever that turns out to be. Kitrane is writing tonight so that you know the Queen did not want to."''',
        c("Continue", "friend2")),
    ga("friend2", '''"Kitrane has no lands, no crown and no enemies. Some days I envy her. There, it is in ink, and I cannot take it back, and I find I do not wish to.
"If I fall, do not make a legend of it. Legends are for people who cannot come to the door. And if you ever again have the look you had in the square, the look of someone who has seen a road nobody else has, then tell me where it goes. I should like, once, to be told.
"K."''',
        c("[Fold it into your jacket, over the heart.]", flags=(LETTER_MOOTED,)),
        c("[Burn it. Nothing that could name her should be carried in the Abyss.]", flags=(LETTER_MOOTED, LETTER_BURNED))),
    ga("general", '''"Commander,
"You asked, as my general, and I promised you an answer. Here it is, considered.
"No. A spare queen is a queen who has already agreed to die. I will not keep a costume in a trunk against the day, nor ask my knights to lie over a grave that is not mine. If I fall, let Mendev have its chaos honestly. It has survived worse, and it has survived it with the truth."''',
        c("Continue", "general2")),
    ga("general2", '''"I do not say this in anger. You were right to ask; it is what I made you for. But there are questions a general may put to a queen and questions only a friend may, and you chose which to be.
"Whatever the Queen must do after tomorrow, she will do.
"K."''',
        c("[Fold it away.]", flags=(LETTER_REFUSED,)),
        c("[Burn it. Nothing that could name her should be carried in the Abyss.]", flags=(LETTER_REFUSED, LETTER_BURNED))),
], requires=(), forbids=(LETTER_MOOTED, LETTER_REFUSED, DEAD), delay=12, chapters=(4,), kind="letter",
    RequiresAnyGroups=[[PRESSED, PRESSED_GENERAL]])
tag(LETTER, "N-all")


# --- Chapter 5 (T, inline on the deathbed list at Iz): the offer ---------------------------------------------------------------
# After "You have returned after all." (Cue_0011). The return cue is Cue_0073; every ending choice continues into her native
# farewell (Cue_0053 -> the Lexicon -> Cue_0056, GalfreyDead), so the Queen dies exactly as she does in canon.

WATCH = (
    c('[Perception DC 18] Watch the wound as you say it, the way she would want it said: "Your Majesty."', requires=(PLANTED,),
      check=dict(Skill="SkillPerception", DC=18, Success="read", Failure="blind", CommanderOnly=True)),
    c('[Perception DC 22] Watch the wound as you say it, the way she would want it said: "Your Majesty."', forbids=(PLANTED,),
      check=dict(Skill="SkillPerception", DC=22, Success="read", Failure="blind", CommanderOnly=True)),
    c("[Stay where you are. Let her be.]", abort=True, forbids=(MANU,)),
)

SCENES.append(scene(OFFER, "The Queen's last hour", "Galfrey", 5, "[Kneel beside her.]", [
    n("start", "Narrator", '''{n}Close to, the wound is worse than it looked from across the rubble. It runs from her collarbone down beneath the ruined breastplate, and in the depths of it there is something that is not blood: a slow, dark light, like a coal seen through smoke. Her knights have bound it three times. Each binding has gone black.{/n}
{n}Galfrey watches you kneel. Her gaze is still clear, and still stern, and it takes her a visible effort to keep it so.{/n}''',
      c("Continue", "seelah", requires=(SEELAH_BED,)),
      c("Continue", "watch", forbids=(SEELAH_BED,))),
    n("seelah", "Narrator", '''{n}Seelah's cry is still in the air: "Your Majesty!" You were looking at the wound when she said it, only because you were looking at everything. You are not sure what you saw. Something in the dark light moved, as a sleeping dog's ear moves at its name.{/n}''',
      c("Continue", "watch")),
    n("watch", "Narrator", '''{n}The Queen's breath goes in and out, shallow and careful. Whatever the enemy's sorcery has its teeth in, it has them in deep. Nobody around the bed is looking at the wound any more; they are looking at her face, the way people do at the end.{/n}''',
      *WATCH),
    n("read", "Narrator", '''{n}"Your Majesty." You say it plainly, as a knight would. The dark light in the wound brightens the way a coal brightens under breath, and her whole body tightens against it.{/n}
{n}You wait until it dulls. Then, very quietly, so that only she can hear: "Kitrane."{/n}
{n}Nothing. The light lies still as a stone in a stream. You try the title again, and it flares; the name again, and it sleeps. Whatever rent her soul knows the crown. It does not seem to know the knight at all.{/n}''',
      c("Continue", "sight", requires=(SIGHT,)),
      c("Continue", "offer", forbids=(SIGHT,), flags=(READ,))),
    n("sight", "Narrator", '''{n}You have seen more than other people since the path took you: the tell in a card player's thumb, the join in a wall. You see this the same way. Every thread of the sorcery runs to one knot, and the knot is tied around a title, the way a leash is tied to a collar and not to the dog.{/n}''',
      c("Continue", "offer", flags=(READ,))),
    n("blind", "Narrator", '''{n}"Your Majesty." You say it, and watch, and see nothing you could swear to before a priest: a dark light in a bad wound, a dying woman's breath going in and out. If the sorcery answers to anything, it will not show you what.{/n}
{n}You have planned campaigns on less. Not many.{/n}''',
      c("Continue", "offer_blind", flags=(BLIND,))),
    n("offer", "conversant", '''{n}Galfrey has felt it too. Her eyes have gone to the wound, and back to you, and there is something in them that is not quite fear.{/n} "What are you doing, Commander?"''',
      c('[Offer her another name] "Your Majesty, the thing in you knows the Queen. It flinches at her title and sleeps through Kitrane. Let the Queen die. Walk out as Kitrane."',
        "weigh", mythic="Trickster")),
    n("offer_blind", "conversant", '''{n}Galfrey watches your face, not the wound.{/n} "You are looking at me the way you looked at the map in the war room. What are you doing, Commander?"''',
      c('[Offer her another name] "I can\'t see whether it would work. I\'m offering it anyway. Let the Queen die here. Walk out as Kitrane."',
        "weigh", mythic="Trickster")),
    n("weigh", "conversant", '''"Another name." {n}A breath that costs her.{/n} "You would have me die in a mask." {n}She closes her eyes, and opens them.{/n} "Tell me what you think you have seen. Quickly, and plainly. I have very little patience left, and less of everything else."''',
      c("Continue", "pitch")),
    n("pitch", "Narrator", '''{n}You tell her, and it is not much. That the church of Iomedae bought every year of the Queen's life for the office, and the office has worn it like armour. That the thing which rent her soul was made to guard Iz against the crusade, and struck at the crusade's Queen. That it seems to hold her by the crown.{/n}
{n}That if the Queen of Mendev dies here, in front of her knights, and her name goes into a sealed coffin and is carried home and grieved over and buried, and the woman in the cart answers only to another, the sorcery may follow the name into the box and let go of what is left. You are proposing, in short, to lie to a curse. Or it may not work. Nobody knows. You say that too.{/n}''',
      c("Continue", "address", requires=(ADDRESS,)),
      c("Continue", "planted", requires=(PLANTED,), forbids=(ADDRESS,)),
      c("Continue", "refusedbefore", requires=(LETTER_REFUSED,), forbids=(PLANTED, ADDRESS)),
      c("Continue", "mendev", forbids=(PLANTED, LETTER_REFUSED, ADDRESS))),
    n("address", "Narrator", '''{n}And you tell her where the thought came from, because she will ask: a hag in a market in the Abyss, laughing at a masked girl, saying that a curse is only an address and finds you by what you answer to. It is a market saying. It is also, as far as you can see, exactly what the wound has just done in front of you.{/n}''',
      c("Continue", "planted", requires=(PLANTED,)),
      c("Continue", "refusedbefore", requires=(LETTER_REFUSED,), forbids=(PLANTED,)),
      c("Continue", "mendev", forbids=(PLANTED, LETTER_REFUSED))),
    n("planted", "conversant", '''"Kitrane has no lands, no crown and no enemies." {n}It is almost a laugh.{/n} "I said that to you. I suppose you wrote it down. You write everything down." {n}Her hand finds your sleeve and holds it.{/n} "I said it as a woman says she would like to see the sea. I did not think anyone would take me at my word."''',
      c("Continue", "mendev")),
    n("refusedbefore", "conversant", '''"I wrote you my answer before the Fane." {n}Her voice is thin, but the steel is all there.{/n} "No spare queens. No costumes in trunks. I have not changed my mind because I happen to be dying. That is when a person's mind should change least."''',
      c("Continue", "mendev")),
    n("mendev", "conversant", '''"My death sows chaos among our forces. I have known it for a hundred years; I have planned for it." {n}Her grip tightens on your sleeve.{/n} "So tell me, Commander. What becomes of Mendev?"''',
      c('[For her] "You never chose your own life. The church chose it, for the Queen. Choose this one yourself."', "accept_rent",
        requires=(BLIND,), flags=(TAKEN, STARTED, RENT)),
      c('[For her] "You never chose your own life. The church chose it, for the Queen. Choose this one yourself."', "accept",
        forbids=(BLIND,), flags=(TAKEN, STARTED)),
      c('[For Mendev] "Mendev keeps its Queen\'s legend and loses nothing it can see. Kitrane\'s death sows no chaos at all."',
        "for_mendev", forbids=(OFFER_REFUSED,)),
      c('[Let her die as the Queen] "...No. You were the Queen of Mendev. Die as her."', "let_die", flags=(LET_DIE, CLOSED))),
    n("for_mendev", "conversant", '''"For Mendev." {n}Something in her face shuts, the way a gate shuts at dusk.{/n} "Then let Mendev have its chaos honestly. It has survived worse, and it survived it with the truth." {n}She turns her head on the rolled cloak under it, away from you, and then back, because she is not a woman who looks away from anything.{/n}
"Listen to me. I have been asked for Mendev every day for a hundred years. Every elixir. Every marriage I did not make. Every knight I sent into the Wound. Ask me as your friend, Commander. Not as my general. It is the only way I have never been asked."''',
      c('[As her friend] "Then as your friend: you never chose your own life. The church chose it, for the Queen. Choose this one yourself."',
        "accept_rent", requires=(BLIND,), flags=(OFFER_REFUSED, TAKEN, STARTED, RENT)),
      c('[As her friend] "Then as your friend: you never chose your own life. The church chose it, for the Queen. Choose this one yourself."',
        "accept", forbids=(BLIND,), flags=(OFFER_REFUSED, TAKEN, STARTED)),
      c('[Let her die as the Queen] "...Then die as her, Your Majesty."', "let_die", flags=(OFFER_REFUSED, LET_DIE, CLOSED))),
    n("accept_rent", "conversant", '''"Choose." {n}Her lips move on the word as if tasting it.{/n} "You cannot even see whether it would work. You are offering me a door in the dark, and telling me it is dark." {n}A breath.{/n} "An honest gamble, then. I prefer it to a false promise."''',
      c("Continue", "accept")),
    n("accept", "conversant", '''"For me." {n}The Queen of Mendev looks at you for as long as her breath allows.{/n} "The Queen has had a century. She may have the dying; she has earned it. And if there is anything left over when she is done..." {n}Her hand turns under yours and grips it, hard, a sword-hand still.{/n} "Kitrane will take it. She is not proud. She will take scraps."''',
      c("Continue", "command_romance", requires=(ROMANCE,)),
      c("Continue", "command", forbids=(ROMANCE,))),
    n("command_romance", "conversant", '''{n}Her thumb moves once across your knuckles.{/n} "We never had our conversation. I kept putting it off until after the next battle. There was always a next battle." {n}Very low:{/n} "If this works, Commander, Kitrane will want it. She is much less patient than I am."''',
      c("Continue", "command")),
    n("command", "conversant", '''{n}She lifts her head a finger's breadth, and her voice changes. It is the voice she uses on parade grounds, and it carries.{/n} "Knight Tirabade. To me."''',
      c("Continue", "irabeth", forbids=("irabeth_dead", KC_KEPT), flags=(CARRIED_IRABETH,)),
      c("Continue", "crows", requires=("irabeth_dead",), flags=(CARRIED_CROWS,)),
      c("Continue", "crows_drezen", requires=(KC_KEPT,), forbids=("irabeth_dead",), flags=(CARRIED_CROWS, CROWS_DREZEN))),
    n("crows_drezen", "Narrator", '''{n}Nobody answers to the name. The Queen remembers, a heartbeat late: Knight Tirabade is in Drezen, where the Queen left her to hold the city. Her mouth tightens. "The Crows, then." Two knights in green surcoats with three black birds on the breast come through the ring and kneel, the older of them bleeding from the scalp and not troubling to wipe it.{/n}''',
      c("Continue", "order")),
    n("irabeth", "Narrator", '''{n}Irabeth comes through the ring of knights like a woman walking into a gale, her face grey, her blade still in her hand because she has forgotten it is there. She kneels on the Queen's other side. She does not look at you.{/n}''',
      c("Continue", "order")),
    n("crows", "Narrator", '''{n}Nobody answers to the name. The Queen remembers, a heartbeat late, and her mouth tightens. "The Crows, then. Whoever of them still stands." Two knights in green surcoats with three black birds on the breast come through the ring and kneel, the older of them bleeding from the scalp and not troubling to wipe it.{/n}''',
      c("Continue", "order")),
    n("order", "conversant", '''"Hear the last command of your Queen." {n}Every knight within ten paces goes still.{/n} "The knight Kitrane of the Green Crows is wounded. Carry her to the rear in a Crows' cloak, and let no priest near her who does not know her. Sir Anselm Wray fell beside me today. He goes home to Nerosyan in my armour, in my coffin, sealed, and he will be buried with honours. He has earned them twice over."
"You will report that the Queen fell at Iz. You saw her fall. You will say so, and nothing else, to anyone, ever."''',
      c("Continue", "obey")),
    n("obey", "Narrator", '''{n}There is a silence in which a whole order of knighthood decides whether it heard what it heard.{/n}
{n}"...Your Majesty," says a voice at the Queen's shoulder, and it cracks on the second word, and steadies. "It will be as you command."{/n}
{n}Galfrey lets her head fall back onto the cloak. She is very pale now. The dark light in the wound is burning steadily, patient as a lantern in a window.{/n}''',
      c("Continue", "last")),
    n("last", "conversant", '''"There." {n}The ghost of her dry smile.{/n} "That is the Queen's last order, and it is a lie, and it is mine. You will not carry it for me, Commander. I carry my own." {n}Her eyes find you, and hold.{/n} "Now let the old woman finish. She has a speech. She has had it ready for twenty years, and she would hate to waste it."''',
      c("[Hold her hand, and let the Queen die.]", native_next=EDGE_FAREWELL),
      c("[Kiss her brow, and let the Queen die.]", requires=(ROMANCE,), native_next=EDGE_FAREWELL)),
    n("let_die", "conversant", '''{n}Something eases in her face, and something else goes out of it.{/n} "As the Queen." {n}She breathes, and it rattles.{/n} "Thank you. I think I should have said yes. And I think I should have been ashamed of it every day of whatever life it bought." {n}Her fingers close on your sleeve, and open.{/n} "You were a better general than I deserved, Commander. Let me go."''',
      c("[Let her go.]", native_next=EDGE_FAREWELL)),
], requires=("trickster", DYING), forbids=(TAKEN, LET_DIE, CLOSED, KILLED), last=5, Relationship=REL, Chapters=[5],
    AnswerLists=[EDGE_LIST], NativeReturnCue=EDGE_BACK, TricksterDevice=True, TricksterState="dead"))
tag(OFFER, "T")


# --- Chapter 5 (T, a visit on the march): the road out of Iz ----------------------------------------------------------------
# The first rest after Iz. Device scenes from here to the return pass the death etude they serve (ER-2): each records a cost.

page(ROAD, "The road out of Iz", [
    nar("start", '''{n}The column goes out of Iz at a walking pace, because the wounded cannot go faster. Behind the Queen's banner, furled now and bound with black, a cart carries a coffin of plain Mendevian oak, sealed with lead at every seam. Knights ride on either side of it with their visors down.{/n}
{n}Three carts back, among the wounded, a knight of the Green Crows lies under a green cloak with three black birds on the breast. Nobody gives her a second look. There are a great many wounded knights.{/n}''',
        c("[Ride up beside the coffin.]", "irabeth", requires=(CARRIED_IRABETH,)),
        c("[Ride up beside the coffin.]", "sergeant", requires=(CARRIED_CROWS,)),
        c("[Drop back to the wounded.]", "cart")),
    n("irabeth", "Irabeth", '''{n}Irabeth rides at the coffin's head. She lifts her visor when you come alongside, and her face under it is the colour of old ash.{/n} "Commander." {n}She looks straight ahead.{/n} "I have told eleven people since dawn that the Queen fell at Iz. It was true every time. I watched her fall." {n}Her jaw works.{/n} "I have never told a lie in my life. I have just found out that I did not need to. I do not know what that makes me."''',
        c('"It makes you the only person she trusted with it."', "irabeth2"),
        c('"If it gets too heavy, tell me. I\'ll carry my share."', "irabeth2"),
        c('"It makes you useful. Keep it that way."', "irabeth2"),
        portrait="Irabeth"),
    n("irabeth2", "Irabeth", '''"It is not mine to put down, or yours." {n}She lowers the visor again.{/n} "It's hers. She gave it to me because I do not lie, and she knew I would not have to." {n}A long breath through the steel.{/n} "Sir Anselm used to tell her she was too old to ride at the front. She used to tell him he was too deaf to hear her say so. That is who is in the box, Commander. I would like somebody besides me to know it."''',
        c("[Drop back to the wounded.]", "cart"),
        portrait="Irabeth"),
    nar("sergeant", '''{n}A sergeant of the Crows rides at the coffin's head, a grizzled man with a bandaged scalp who will not meet your eye. When you ask him how it goes, he says, "Well enough, Commander. The Queen fell at Iz. I saw her fall," in the tone of a man reciting a password, and then, lower: "Sir Anselm's in there. He'd have laughed. He always said he'd end up in a better box than he deserved."{/n}''',
        c("[Drop back to the wounded.]", "cart")),
    nar("cart", '''{n}The cart smells of blood and wet wool. A Crows' squire walks beside it with a hand on the tailboard, watching the road the way a dog watches a door.{/n}''',
        c("Continue", "read", requires=(READ,)),
        c("Continue", "fever", forbids=(READ,))),
    ga("read", '''{n}She is awake. Her face is grey with fatigue and there is a crust of dried blood along her jaw, but when the wheel jolts over a stone she swears at it, fluently, in a voice nobody in Mendev has ever heard its Queen use.{/n} "Commander." {n}She does not try to sit up.{/n} "I am told I was dead for the better part of an hour. The Crows' surgeon had given up; he was praying over me. Then the sergeant hammered the lead seal onto the Queen's coffin, with her name on the lid, and it let go. Like a hand opening." {n}Her fingers move on the cloak, as if to show you.{/n} "I heard the hammer. I have been nobody for nine hours since. It is the longest holiday I have taken since my coronation."''',
        c('"How does it feel?"', "feel"),
        c('"You swear like a sergeant."', "swear")),
    ga("swear", '''"I learned from sergeants. A queen is not permitted to use it." {n}Something that is very nearly a grin.{/n} "Kitrane may do as she likes. I have been practising since the milestone. The squire is scandalised, but he is a Crow, and the Crows are very discreet."''',
        c("Continue", "feel")),
    ga("feel", '''"Light." {n}She considers it with care, the way she considers everything.{/n} "And wrong. There is a coffin three carts ahead with my name on it, and a good man in it who has no name at all now." {n}She looks up at the sky, which is the colour of a bruise.{/n} "Sir Anselm Wray. Sixty-one. Deaf in the left ear. He joined my guard because, he said, he could not hear the demons coming anyway, so he might as well stand next to someone who could."''',
        c("Continue", "anselm")),
    ga("anselm", '''"His daughter keeps his house in Nerosyan. She will be told that he is missing at Iz. That is the kindest lie available, and it is mine, and I shall answer for it." {n}Her mouth tightens.{/n} "Do not tell me he would have wanted it. He would have. That is not the point."''',
        c('"Then what is the point?"', "point"),
        c("[Ride beside the cart in silence for a while.]", "silence")),
    ga("point", '''"That I let him." {n}She closes her eyes.{/n} "A hundred years, Commander, and I have let a great many people pay for me. I had thought, lying here, that Kitrane might be the first of me who did not. She has been alive nine hours and she has already buried a friend under her own name." {n}A breath.{/n} "Go on ahead. I need to be nobody for a little longer, and nobody does not ride with the Commander."''',
        c("[Ride on ahead.]", flags=(COFFIN,))),
    nar("silence", '''{n}You ride beside the cart until the column halts to water the horses. She does not speak again. Once, when a knight of the Eagle Watch rides by calling out that the Queen's coffin will lie in state in Drezen, she turns her face into the green cloak and stays that way until he has gone.{/n}''',
        c("[Ride on ahead.]", flags=(COFFIN,))),
    nar("fever", '''{n}She is not awake. Her heart stopped at Iz for the better part of an hour, the Crows' surgeon tells you, and came back, faintly, when the Queen's coffin was sealed; since then the fever has had her. Her lips move on words you cannot hear, and under the fresh bandage at her collarbone there is still, faint as a coal under ash, a dark light.{/n}
{n}The squire watches you look at it.{/n} "It's no worse, Commander. It's no better. The sergeant says we're not to say... the old title. Near her. It hurts her when we do." {n}He swallows.{/n} "A knight at the ford said it passing, meaning well, and she came up off the boards like she'd been branded."''',
        c("Continue", "fever2")),
    ga("fever2", '''{n}Her eyes open, unfocused, and find you after a while.{/n} "Not yet." {n}It is barely a whisper.{/n} "It is waiting to be told. It will not believe a knight in a cart. It wants to hear it said where the Queen was loved." {n}Her hand closes on your wrist with the whole of her remaining strength, which is not much.{/n} "Tell them, Commander. Tell them well."''',
        c('"I will."', "fever_end"),
        c("[Say nothing. Lay her hand back on the cloak.]", "fever_end")),
    nar("fever_end", '''{n}She is asleep again before you have finished. Three carts ahead, the coffin creaks on its axle. Sir Anselm Wray of the Green Crows, the squire tells you when you ask, was sixty-one and deaf in one ear, and would have thought all of this very funny.{/n}''',
        c("[Ride on ahead.]", flags=(COFFIN,))),
], requires=("trickster.ever", TAKEN, DEAD), forbids=(ALONE, RETURNED, CLOSED), delay=10,
    TricksterDevice=True, TricksterState="dead")
tag(ROAD, "T")


# --- Chapter 5 (T, an event in Drezen): the Queen's eulogy ---------------------------------------------------------------------
# The Commander's cost, and the proclamation that the rending of a blind offer waits for.

page(P + "iz.eulogy", "The Queen lies in state", [
    nar("start", '''{n}Drezen keeps its vigil for the Queen in the chapel of the citadel, before the coffin goes home to Nerosyan. The oak box stands before the altar of the Inheritor under the blue and silver of Mendev, with her sword laid along its lid. It is the only thing of hers in the box. The knight who carried her out is wearing Sir Anselm's, and nobody who knows the difference is going to say so.{/n}
{n}The chapel is full to the doors, and the square outside is full, and the walls. It falls to the Commander of the crusade to speak.{/n}''',
        c("Continue", "hulrun", forbids=("hulrun.dead", "hulrun.away_c5")),
        c("Continue", "chaplain", requires=("hulrun.dead",)),
        c("Continue", "chaplain", requires=("hulrun.away_c5",), forbids=("hulrun.dead",))),
    nar("hulrun", '''{n}Inquisitor Hulrun has said the prayers. His voice broke twice; both times he went on. Now he steps back from the altar and looks at you, red-eyed, the way a man looks at the last wall standing between him and the dark.{/n}''',
        c("Continue", "speak")),
    nar("chaplain", '''{n}The chaplain of the citadel has said the prayers, in a thin voice, because the Inquisitor who should have said them is not in Drezen to say them. Now he steps back from the altar and looks at you, and so does everyone else.{/n}''',
        c("Continue", "speak")),
    nar("speak", '''{n}You have given speeches before battles. You have never given one over a coffin you know to be the wrong one, to a crowd that is weeping for a woman you know to be breathing. You find you have planned this one as carefully as a siege, and that it does not help at all.{/n}''',
        c("[Tell them the truth about her. Every word, but one.]", "true", flags=(EULOGY, EULOGY_TRUE, SECRET)),
        c("[Give Drezen the legend it needs to go on fighting.]", "legend", flags=(EULOGY, EULOGY_LEGEND, SECRET)),
        c("[Hide one line in it, for one listener.]", "sign", flags=(EULOGY, EULOGY_SIGN, SECRET), mythic="Trickster")),
    nar("true", '''{n}You tell them about the Queen you knew. That she was curious, and could not sit still, and came to the crusade because her blade had been in its scabbard long enough. That she was hard on her Commander and harder on herself. That she thought of her soldiers first. That she was proud, and knew it, and served anyway.{/n}
{n}Every word of it is true, except the one in the middle that makes it a eulogy. When you are done the chapel is so quiet you can hear the candles.{/n}''',
        c("Continue", "after")),
    nar("legend", '''{n}You give them the Queen of the chronicles: the paladin chosen by the Inheritor, the century of vigil on the edge of the Wound, the last charge at Iz against the servants of the Lord of Locusts. You give them a queen who never doubted and never slept and died with the goddess's name on her lips.{/n}
{n}It is a very good speech. The knights weep openly. It is also, you reflect, as you step down, a portrait of a woman who would have despised it.{/n}''',
        c("Continue", "after")),
    nar("sign", '''{n}You tell them about the Queen, and it is a good speech, and in the middle of it you tell them one small thing more: that she once said she envied a knight of a minor order, who had no lands, no crown and no enemies, and slept under canvas, and had her boots stolen twice.{/n}
{n}A few people laugh through their tears, as you meant them to.{/n}''',
        c("Continue", "sign_hulrun", forbids=("hulrun.dead", "hulrun.away_c5")),
        c("Continue", "after", requires=("hulrun.dead",)),
        c("Continue", "after", requires=("hulrun.away_c5",), forbids=("hulrun.dead",))),
    nar("sign_hulrun", '''{n}The Inquisitor does not laugh. He looks at you for rather longer than a grieving man needs to, and then down at his hands.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}The bells of Drezen ring for the Queen of Mendev, all of them together, the way they rang when the city was retaken. The crowd in the square goes to its knees in a long rustle like wind in wheat.{/n}''',
        c("Continue", "present", requires=(READ,), forbids=(ALONE,)),
        c("Continue", "tent", requires=(RENT,)),
        c("Continue", "done", forbids=(READ, RENT))),
    nar("present", '''{n}At the very back of the chapel, among the common soldiers, a knight in plain armour with a grey hood drawn close stands with her hands folded on the pommel of an old sword. When the choir sings the Queen's name, she does not flinch. When the bells begin, she bows her head, the way any knight would.{/n}
{n}She is gone before the doors are opened.{/n}''',
        c("Continue", "done")),
    nar("tent", '''{n}Outside the walls, in a Crows' tent in the field camp, a knight who has not been lucid in days hears the bells. The squire who sits with her will tell you later that she said, "There," quite clearly, as if a door had been shut in the next room, and that the dark light under the bandage went out like a candle pinched between two fingers.{/n}
{n}She slept through the night after, the squire says. It is the first thing about any of this that has made him weep.{/n}''',
        c("Continue", "done")),
    nar("done", '''{n}Afterwards, alone in your quarters, you find that your hands are shaking, and that you are not certain whether it is from what you have done or from how well you did it.{/n}
{n}Half of Drezen will remember that eulogy for the rest of their lives. You will remember that it was a lie, and who it was for, and that somebody in that chapel may have heard it for what it was.{/n}''',
        c("[Put out the lamp.]")),
], requires=("trickster.ever", TAKEN, DEAD), forbids=(RETURNED, CLOSED), delay=30, kind="event", owner="Commander", Areas=[DREZEN],
    TricksterDevice=True, TricksterState="dead")
tag(P + "iz.eulogy", "T")

household.secret(
    SECRET_KEY, "The Queen's eulogy",
    "I stood before the altar in Drezen and grieved for the Queen of Mendev in front of the whole city, knowing she was alive "
    "in a Crows' tent outside the walls, and that the coffin held a knight called Sir Anselm Wray. The knights who carried "
    "her out know. The Inquisitor prays for the Queen every night, and he was in the chapel when I spoke.",
    portrait="Galfrey", witnesses=("irabeth", "seelah"), risk="medium")


# --- Chapter 5 (T, a letter): the Commander never came --------------------------------------------------------------------------
# DidntVisitedEvents: she fought the dragon without the Commander and died off the page. Only if she had mooted Kitrane does she
# take the old offer herself; otherwise canon stands and nothing here opens.

page(P + "iz.alone", "A letter sealed in green", [
    nar("open", '''{n}The letter comes by a Crows' courier who will not give his name, sealed in plain green wax with no device. The hand is firm and old-fashioned, and in places it shakes so badly that the pen has gone through the paper.{/n}''',
        c("[Break the seal.]", "letter")),
    ga("letter", '''"Commander,
"You did not come to Iz. I do not reproach you for it. I sent you into the Abyss, and a commander goes where the war is, not where the Queen happens to be dying.
"I went into Iz without you. The enemy's sorcery went into me like a hook into a fish. My knights bound the wound three times. I lay in the rubble with Pharasma's door in front of me and I thought, quite calmly: so this is how the Queen ends."''',
        c("Continue", "letter2")),
    ga("letter2", '''"And then, because I am an old woman and my mind wanders, I thought of a knight of a minor order who had her boots stolen twice in the war camp. You once told me she could outlive the Queen. I said some days I envied her.
"So I tried it. Nobody offered; you were not there to. But your old sergeant had his orders and his cart and his purse, and he knelt in the rubble and waited for me to say the word. I offered it to myself. I do not recommend it; it is very lonely."''',
        c("Continue", "irabeth", forbids=("irabeth_dead", KC_KEPT), flags=(CARRIED_IRABETH,)),
        c("Continue", "crows", requires=("irabeth_dead",), flags=(CARRIED_CROWS,)),
        c("Continue", "crows", requires=(KC_KEPT,), forbids=("irabeth_dead",), flags=(CARRIED_CROWS, CROWS_DREZEN))),
    ga("irabeth", '''"The old sergeant of the Crows had your orders; he told me so, kneeling in the rubble, as if confessing. I gave Knight Tirabade the last command of her Queen. The Queen fell at Iz; the wounded knight Kitrane goes to the rear; Sir Anselm Wray, who died beside me, goes home to Nerosyan in my coffin, under my name. She obeyed. She will not lie for me, and she will not have to. She saw me fall."''',
        c("Continue", "letter3")),
    ga("crows", '''"I gave the last command of the Queen to the two Crows who still stood, as you had arranged with them. The Queen fell at Iz; the wounded knight Kitrane goes to the rear; Sir Anselm Wray, who died beside me, goes home to Nerosyan in my coffin, under my name. They obeyed. They are very discreet men."''',
        c("Continue", "letter3")),
    ga("letter3", '''"It has not let go. It has loosened, the way a hand loosens when its owner is listening for something. I think it is waiting to hear the Queen's death proclaimed where she was loved. I have no way to make that happen. You do.
"If this reaches you, Commander, I am alive, and nobody. If it does not, then I tried, and that will have to do.
"Kitrane."''',
        c("Continue", "post")),
    nar("post", '''{n}Underneath, in a different ink, as if added days later: "It does not let one hide from oneself. I have looked. K."{/n}''',
        c('[Write back at once] "Hold on. I\'m coming back to Drezen, and I\'ll make sure it\'s said."',
          flags=(TAKEN, RENT, ALONE, STARTED, COFFIN, REPLIED)),
        c("[Fold the letter away, and start planning the vigil.]", flags=(TAKEN, RENT, ALONE, STARTED, COFFIN))),
], requires=("trickster", LEFT_EARLY, DEAD, PLANTED, BRIEFED), forbids=(DYING, KILLED, TAKEN, CLOSED), delay=24, kind="letter",
    TricksterDevice=True, TricksterState="dead")
tag(P + "iz.alone", "T")


# --- Chapter 5 (T, a visit in Drezen): the cortege, the lid not yet sealed ------------------------------------------------------
# The late recovery for the offscreen death when nothing was prepared (no Kitrane mooted, no standing orders; or the letter from
# the rubble never came). She fell at Iz with no Commander at her side; her knights carry her home to Nerosyan by way of Drezen,
# and the lead seal goes onto the coffin there. The rending holds her in a death that will not finish: the Crows' surgeon notices
# she does not stiffen. The Commander reaches the chapel before the seal, on nerve alone, and offers the old name to a woman who
# is barely there; she decides. Dearer than the prepared ways: the rent voice, the lost weeks, the Crows' sergeant bought or
# faced down in front of his dead Queen, and a second body to find for the box.

page(P + "iz.cortege", "The lid not yet sealed", [
    nar("start", '''{n}The Queen's cortege comes through the gate of Drezen at dusk, three days out of Iz: a cart draped in blue and silver, knights walking beside it bareheaded, and the whole of the lower town lining the road in silence. It will lie one night in the citadel chapel. In the morning the lead seal goes on, and it goes home to Nerosyan.{/n}
{n}You were not at Iz. You have been hearing that sentence in other people's mouths for three days.{/n}''',
        c("Continue", "surgeon")),
    n("surgeon", "Crows' sergeant", '''{n}An old knight in a green surcoat with three black birds on the breast is standing guard at the chapel door, and does not step aside for you.{/n} "Commander." {n}His voice is hoarse.{/n} "The surgeon says it is the Wound's cold that keeps her. She has not stiffened. Three days, and she has not stiffened, and she has not breathed either, that anyone can swear to." {n}He looks at you as if you were to blame for all of it, and perhaps you are.{/n} "They seal her at first light."''',
        c("[Diplomacy DC 24] \"Let me in. There's a thing she said once, in the war camp, about a knight of your order. I need to say it back to her.\"",
          check=dict(Skill="CheckDiplomacy", DC=24, Success="in", Failure="barred", CommanderOnly=True)),
        c("[Pay him] \"Then let me sit a vigil. Here: for the Crows, for the road home.\"", "bought", crusade=("Finances", -300)),
        c("[Leave the Queen to her knights.]", abort=True)),
    n("barred", "Crows' sergeant", '''"No." {n}Flat as a blade.{/n} "You were not at Iz. You do not get to be at this." {n}And then, because he is an old soldier and knows what a purse is for, he looks at your belt and away again.{/n}''',
        c("[Pay him] \"For the Crows, and the road home.\"", "bought", crusade=("Finances", -300)),
        c("[Leave the Queen to her knights.]", abort=True)),
    n("bought", "Crows' sergeant", '''{n}He takes it. He hates himself for taking it, and hates you worse, and it is all there in his face.{/n} "One hour. And if you do anything to her, Commander, I will know."''',
        c("[Go in.]", "in")),
    nar("in", '''{n}The chapel is cold. She lies on the bier in her ruined armour with her sword on her breast, and the wound at her collarbone is bound in linen that has gone black, and under the linen, if you look long enough, there is something that is not blood: a slow dark light, still burning, patient as a lantern in a window.{/n}
{n}She is not dead. She is not anything. Whatever took her at Iz is still holding on, and it is holding on to the Queen of Mendev.{/n}''',
        c("[Kneel, and say it close to her ear.] \"Your Majesty.\"", "flare")),
    nar("flare", '''{n}The dark light brightens. Her hand, on the sword, closes by a hair.{/n}
{n}You have nothing: no seed, no plan, no knight of a minor order she ever told you she envied. You have what you saw in a war camp and the name she chose for herself there, and the fact that it is the only name in the world this thing does not know.{/n}''',
        c('[Offer her another name] "Kitrane. Kitrane of the Green Crows. You told everyone you were my old friend. Come back as her."', "wake", mythic="Trickster")),
    ga("wake", '''{n}It takes a long time. Her lips move before her eyes open, and her eyes, when they open, do not find you at once.{/n} "Commander." {n}Barely a breath.{/n} "You were not at Iz." {n}A longer silence.{/n} "Kitrane. That was a joke. For the war camp." {n}Her fingers move on the sword hilt.{/n} "I am so tired. Tell me why I should wake up as a joke."''',
        c('"Because the Queen is finished, and you are not. Choose it. Nobody chose your life for you this time."', "choose"),
        c('[Let her go] "...Then do not. Rest, Your Majesty."', "rest", flags=(LET_DIE, CLOSED))),
    ga("choose", '''"Choose." {n}Something that was almost a laugh once.{/n} "In a cold chapel, three days dead, with the lid on the floor. You pick your moments, Commander." {n}Her hand turns on the hilt and finds yours.{/n} "Very well. The Queen is in the box. Put someone in it with her name; the Crows lost a man at Iz, Sir Anselm, and he would think this very funny." {n}Her eyes close again.{/n} "Seal it at first light, with every bell. It wants to hear it said. And then carry out a knight."''',
        c("[Call the sergeant in, and tell him what she said.]", "sergeant")),
    n("sergeant", "Crows' sergeant", '''{n}He comes in with his hand on his sword, and stops, and sees her eyes open, and goes down on both knees on the chapel stones as if his legs had been cut.{/n} "Your Maj..." {n}He stops himself. He is not a stupid man.{/n} "Kitrane." {n}A long breath.{/n} "Anselm is in the cart. We were taking him home. He will be taking her home instead." {n}He looks up at you, and whatever was in his face at the door is not gone, and never will be.{/n} "First light, Commander. With every bell."''',
        c("[Stay until first light.]", flags=(TAKEN, RENT, ALONE, STARTED, COFFIN, LATE_FOUND))),
    ga("rest", '''{n}The fingers on the sword loosen.{/n} "Thank you." {n}It is hardly a word.{/n} "You were not at Iz. You were here. That will have to do."''',
        c("[Sit with her until the light goes out.]")),
], requires=("trickster", LEFT_EARLY, DEAD), forbids=(DYING, KILLED, TAKEN, CLOSED), delay=60, Areas=[DREZEN],
    TricksterDevice=True, TricksterState="dead")
tag(P + "iz.cortege", "T")


# --- Chapter 5 (T, a visit): Kitrane comes to find the Commander -------------------------------------------------------------
# 48 hours after the Coronation when the Commander saw the sorcery answer the title; 96 when the offer was made blind or she
# made it to herself. One return per world: the twins forbid each other.

def return_nodes(scarred):
    voice = ('''{n}Her voice is lower than you remember it, and there is a catch in it now, a faint tearing at the edge of certain words, like cloth that has been mended where you cannot see.{/n} '''
             if scarred else '')
    return [
        nar("start", '''{n}It is a bright, cold morning, and Drezen is still hung with black for its Queen. A knight in plain armour is waiting for you at the foot of the citadel steps: a green surcoat with three black birds on the breast, an old sword, a face you know from a hundred portraits and a dozen war councils, with nothing above it now but the cold sky.{/n}
{n}The sentries at the gate have already told her twice to move along. She has not moved along.{/n}''',
            c("Continue", "name")),
        ga("name", voice + '''"Kitrane. Of the Green Crows." {n}She inclines her head exactly as far as a knight of a minor order inclines it to the Commander of the crusade, and not a hair further.{/n} "An old friend of yours, I am told."''',
            c('"Your Majesty."', "majesty"),
            c('"Kitrane. You\'re late."', "late"),
            c("[Say nothing. Look at her.]", "look")),
        ga("majesty", '''{n}She does not flinch. You watch for it, and it does not come.{/n} "No." {n}Very quietly.{/n} "That word does nothing to me now. I tried it on myself in the tent, every morning, like a man pressing a bruise. Nothing." {n}A breath.{/n} "But do not say it again. Not because it hurts. Because it is not true, and a great many people in this city are wearing black because it is not."''',
            c("Continue", "heard")),
        ga("late", '''"Late." {n}One eyebrow.{/n} "I have been dead, Commander. It takes a little while to arrange one's affairs." {n}The corner of her mouth moves.{/n} "Also I walked. A knight of the Green Crows does not own a horse. I had not appreciated how far it is from the field camp to the citadel when one's boots have been stolen. Twice."''',
            c("Continue", "heard")),
        nar("look", '''{n}She lets you. She stands in the cold sunlight with the black crepe of her own mourning snapping on the gate behind her, and lets you look at her the way people rarely look at a queen: without a crown to look at instead.{/n}
{n}"Well, Commander," she says at last, dry as dust. "Am I what you ordered?"{/n}''',
            c("Continue", "heard")),
        ga("heard", '''"I know about the vigil." {n}She says it flatly, the way one reports a casualty.{/n}''',
            c("Continue", "e_true", requires=(EULOGY_TRUE,)),
            c("Continue", "e_legend", requires=(EULOGY_LEGEND,)),
            c("Continue", "e_sign", requires=(EULOGY_SIGN,)),
            c("Continue", "e_none", forbids=(EULOGY_TRUE, EULOGY_LEGEND, EULOGY_SIGN))),
        ga("e_true", '''"You told them the truth about me." {n}She looks away, at the black on the gate.{/n} "All of it. Proud, and hard, and could not sit still." {n}Her voice roughens.{/n} "It was the most honest thing said over that coffin, and it was said over the wrong coffin. I have been trying for three days to decide whether to thank you."''',
            c("Continue", "why")),
        ga("e_legend", '''"The Queen of the chronicles. Chosen of the Inheritor, never doubted, never slept." {n}Dry as dust.{/n} "The knights wept. I expect half of them will name daughters after that woman. I should very much like to meet her. She sounds exhausting." {n}A pause.{/n} "It was well done, Commander. It was what Drezen needed. Do not ever do it to me again."''',
            c("Continue", "why")),
        ga("e_sign", '''"And the line about the boots." {n}Something happens at the corner of her mouth that she does not permit to become a smile.{/n} "A knight of a minor order, who slept under canvas. Before the altar of the Inheritor and half of Drezen." {n}She shakes her head slowly.{/n} "You are a very dangerous person to be dead near, Commander. I laughed when I heard it. I am told that is not what one does about one's own vigil."''',
            c("Continue", "why")),
        ga("e_none", '''"Drezen rang every bell it had. They could hear it in the field camp; they could hear it in Kenabres, I should think." {n}She is quiet.{/n} "I stood outside the walls with a Crows' squire and listened to a city grieve for me. I do not recommend it either. It is very hard to know what to do with one's hands."''',
            c("Continue", "why")),
        ga("why", '''"So. Here I am." {n}She squares her shoulders, knight to Commander.{/n} "I have no lands, no crown and no enemies. I have an old sword, a green surcoat, and a name that was two weeks old in the war camp. And I have discovered that I still stand in the square at the hour of petitions, every morning, waiting for somebody to need a ruling. Nobody does." {n}She meets your eyes.{/n} "Mendev buried a queen. I would like, just once, to be a face in your crowd that you look for."''',
            c("Continue", "alone", requires=(ALONE, REPLIED)),
            c("Continue", "alone_silent", requires=(ALONE,), forbids=(REPLIED, LATE_FOUND)),
            c("Continue", "alone_found", requires=(LATE_FOUND,)),
            c("Continue", "refused", requires=(OFFER_REFUSED,), forbids=(ALONE,)),
            c("Continue", "romance", requires=(ROMANCE,), forbids=(ALONE, OFFER_REFUSED)),
            c("Continue", "end", forbids=(ALONE, OFFER_REFUSED, ROMANCE))),
        ga("alone", '''{n}Her gaze hardens, just perceptibly.{/n} "You were not at Iz. I have forgiven you that; I wrote so, and I meant it." {n}A beat.{/n} "I have not yet forgiven myself for how glad I was to see your hand on the letter that came back. A queen does not wait by a window for the post, Commander. Kitrane, it seems, does."''',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("alone_found", '''{n}Her gaze hardens, just perceptibly.{/n} "You were not at Iz. You found me three days later on a bier in Drezen, with the lid on the floor and a bribed sergeant at the door." {n}A beat.{/n} "I have not decided whether to forgive you the first part. I find I cannot hold the second against you at all. A queen would have kept those accounts separately, Commander. Kitrane, it seems, does not."''',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("alone_silent",'''{n}Her gaze hardens, just perceptibly.{/n} "You were not at Iz. I have forgiven you that; I wrote so, and I meant it." {n}A beat.{/n} "You did not write back. I told myself that was prudence: letters are read. I told myself so every morning for a week, at the window, waiting for the post like a fool. A queen does not do that, Commander. Kitrane, it seems, does."''',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("refused", '''"You asked me for Mendev first." {n}She does not raise her voice; she has never needed to.{/n} "I lay dying and you asked me for Mendev. And then you asked me for myself, when I told you how. I have not decided which of those I shall remember longer." {n}A pause.{/n} "Both, probably. I am old. I have room."''',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("romance", '''{n}Then, lower, so that the sentries cannot hear:{/n} "And we never had our conversation. I put it off until after the Fane, and after the Abyss, and after Iz." {n}She looks at you steadily.{/n} "The Queen had reasons to wait. Kitrane has none that I can find. That frightens me a good deal more than anything at Iz did."''',
            c("Continue", "end")),
        ga("end", '''"I shall be in the market. By the curio stall, where the crowd is thickest; I have found I like crowds." {n}She turns to go, and turns back.{/n} "Don't forget, here I am Kitrane the knight. Come and find me when the war allows. I have nothing but time. It is the most extraordinary sensation."''',
            c('"I\'ll find you."', flags=(RETURNED, STARTED)),
            c('[Flirt] "I\'ll look for you in every crowd, then."', flags=(RETURNED, STARTED)),
            c('"Go and buy yourself a pair of boots, Kitrane."', flags=(RETURNED, STARTED))),
    ]


page(P + "return.kitrane", "A knight of the Green Crows", return_nodes(False),
     requires=("trickster.ever", TAKEN, DEAD, CORONATION, EULOGY), forbids=(RETURNED, CLOSED, RENT, P + "return.kitrane_scarred"),
     delay=48, TricksterDevice=True, TricksterState="dead", Areas=[DREZEN])
page(P + "return.kitrane_scarred", "A knight of the Green Crows", return_nodes(True),
     requires=("trickster.ever", TAKEN, DEAD, CORONATION, RENT, EULOGY), forbids=(RETURNED, CLOSED, P + "return.kitrane"),
     delay=96, TricksterDevice=True, TricksterState="dead", Areas=[DREZEN])
tag(P + "return.kitrane", "T")
tag(P + "return.kitrane_scarred", "T")


# --- Reactions: named companions and NPCs with a real stake in her -----------------------------------------------------------
# Irabeth carried the order; Seelah said the title at the bed; Hulrun prays for her; Daeran is her cousin; the King drinks with
# her. Each is one node on the reactor's own list, and none gates on another woman's state except through its own guard.

IRABETH_GUARD = dict(forbids=("irabeth_dead", CLOSED), ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned"})

SCENES.append(reaction("Irabeth", P + "react.irabeth.carried", (RETURNED, CARRIED_IRABETH),
    '''{n}Irabeth is at the duty roster with a pen in her hand, and she does not write anything for some time after you come in.{/n} "The knight of the Green Crows came through the gate this morning. On foot. She had bought new boots." {n}Her pen hovers.{/n} "I carried her out of Iz in a Crows' cloak, Commander, on my own horse, with her head against my back. She said nothing the whole way. Neither did I." {n}She sets the pen down very precisely.{/n} "I have told everyone who asked that the Queen fell. I saw her fall. I will be saying it on my deathbed. I only wanted one person in this citadel to know that I know what I am saying."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **{**IRABETH_GUARD, "forbids": IRABETH_GUARD["forbids"] + (ALONE,)}))

SCENES.append(reaction("Irabeth", P + "react.irabeth.alone", (RETURNED, ALONE, CARRIED_IRABETH),
    '''{n}Irabeth does not look up from the duty roster.{/n} "You were not at Iz. So you will not know what she looked like when she gave me that order." {n}Her pen has stopped.{/n} "Lying in the rubble with that sorcery in her, alone but for me and two old Crows, telling us in her parade-ground voice that the Queen had fallen and a knight called Kitrane needed carrying. She did it herself, Commander. Nobody offered her anything. She offered it to herself." {n}Now she looks up.{/n} "I have never been so proud of anyone, or so angry. I have not decided which of those I owe you."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Irabeth", P + "react.irabeth.after_death", (RETURNED, CARRIED_CROWS, "irabeth.trickster.returned"),
    '''{n}Irabeth has the duty roster open and has not written on it since you came in.{/n} "The old sergeant of the Green Crows came to see me last night. Drunk, which he never is. He told me who is buying boots in the market." {n}Her voice is very even.{/n} "I was dead when she fell, Commander. I had been dead an hour. She called my name with her last command in her mouth, he says, and two old men came instead." {n}She closes the roster.{/n} "We both came back. Neither of us came back as what we were. I shall not be telling her that I know. I think she would rather be one secret I do not carry."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **{**IRABETH_GUARD, "forbids": IRABETH_GUARD["forbids"] + (CROWS_DREZEN,)}))

SCENES.append(reaction("Irabeth", P + "react.irabeth.learned", (RETURNED, CROWS_DREZEN),
    '''{n}Irabeth has the duty roster open and has not written on it since you came in.{/n} "The old sergeant of the Green Crows came to see me last night. Drunk, which he never is. He told me who is buying boots in the market." {n}Her voice is very even.{/n} "I was holding Drezen when she fell. She did not send for me; she sent for two old men and a cart." {n}She closes the roster.{/n} "I have been angry about it all morning, Commander. I think it was the kindest thing she ever did to me. I shall not be telling her either."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Irabeth", P + "react.irabeth.drill", (DRILL, P + "kitrane.squire_sworn"),
    '''"I rode past the Crows' tent this morning with the Eagle Watch." {n}Irabeth says it to the roster, not to you.{/n} "She was drilling a girl from the eel stall in the mud behind it. Badly. The girl, I mean. Not her." {n}A pause.{/n} "Forty knights rode past, and not one of them saluted a knight of a minor order at her drill. They were right not to. That is the whole of the Queen's last command." {n}Her jaw works.{/n} "I saluted. From the road, where she could not see. I will not do it again. But I wanted somebody to know that I did it once."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"Anything to report, knight?"', chapter=5, last=5, delay=12,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Seelah", P + "react.seelah.majesty", (RETURNED, SEELAH_BED),
    '''{n}Seelah is sitting on the edge of the practice ring, spinning a copper on her knuckle and not catching it.{/n} "I said it. At Iz. 'Your Majesty!' I shouted it like an idiot, the way you'd shout at somebody about to fall off a roof." {n}The copper drops. She leaves it.{/n} "And I saw the wound move when I said it, Commander, and I told myself I didn't." {n}She looks up.{/n} "I was a street thief before I was a paladin. I know a disguise when I see one buying boots in the market. I'm not going to say anything. I'm just going to pray very hard that the Inheritor thinks what you did was mercy, because I've decided that I do."''',
    answer_list=SEELAH_HUB, relationship=REL, forbids=("seelah_dead", "seelah_gone", CLOSED),
    ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"},
    entry='"You look like you\'ve seen a ghost, Seelah."', chapter=5, last=5, delay=24, portrait="Seelah"))

SCENES.append(reaction("Hulrun", P + "react.hulrun.door", (RETURNED,),
    '''{n}The Inquisitor's eyes are still red, and he has not shaved.{/n} "There is a knight of some minor order who stands at the chapel door at the ninth bell, Commander, while I pray for Her Majesty. In a grey hood. Every night." {n}His hands tighten on his ledger.{/n} "I have not turned round. A man at his prayers should not be spied upon, and neither, I think, should a knight at hers." {n}A long breath.{/n} "But I am an Inquisitor. I notice. Tell your Crows, if they are yours, that the chapel has a front pew, and nobody is using it."''',
    answer_list=HULRUN_HUB, relationship=REL, forbids=("hulrun.dead", "hulrun.away_c5", EULOGY_SIGN, CLOSED),
    entry='"Inquisitor. You look tired."', chapter=5, last=5, delay=48, portrait=""))

SCENES.append(reaction("Hulrun", P + "react.hulrun.ledger", (RETURNED, EULOGY_SIGN),
    '''{n}Hulrun does not greet you. He opens his ledger to a page near the back and turns it round so that you can read it: a single line in his cramped, furious hand. "A knight of a minor order. No lands. No crown. No enemies."{/n} "You said that over her coffin, Commander. I wrote it down that night; I write everything down." {n}His voice is very low.{/n} "And now there is a knight of a minor order at my chapel door every night who stands exactly as she stood, and has her hands." {n}He closes the ledger.{/n} "I have not turned round. I will not, while the war lasts. After the war, Commander, you and I are going to have a conversation, and I am going to need a great deal of it explained to me by someone other than a demon."''',
    answer_list=HULRUN_HUB, relationship=REL, forbids=("hulrun.dead", "hulrun.away_c5", CLOSED),
    entry='"Inquisitor. You look tired."', chapter=5, last=5, delay=48, portrait=""))

SCENES.append(reaction("Daeran", P + "react.daeran.cousin", (RETURNED,),
    '''{n}Daeran is lounging with a glass of something that costs more than a Crow's yearly wage, and he raises it to you with the air of a man who has been waiting all morning to do so.{/n} "My dear Commander. My cousin is buying boots in the market." {n}He savours your face.{/n} "Oh, don't. I have known that jaw since I was four years old and it was telling me to take my elbows off the table. She passed me in the square and looked straight through me, beautifully. I nearly applauded." {n}He swirls the glass.{/n} "I shan't tell a soul. It is the first genuinely interesting thing she has done in a century, and I refuse to spoil it. Do give her my love. She'll hate that."''',
    answer_list=DAERAN_HUB, relationship=REL, forbids=("daeran.dead", "daeran.kicked_out", CLOSED),
    entry='"You look amused, Daeran."', chapter=5, last=5, delay=24, portrait="Daeran"))

SCENES.append(reaction("Thaberdine", P + "react.king", (P + "kitrane.king_seen", "fool_king.available"),
    '''"That knight of yours! The green one! With the birds!" {n}The King bangs his tankard on the table.{/n} "Drinks like a queen, Commander. Holds her cup like there's a painter in the corner. Cheats at dice like a peasant, which I respect." {n}He leans in, conspiratorial, and breathes beer on you.{/n} "I knighted her with a sausage. Best knighting I ever did. She took it very seriously. Knelt and everything." {n}He sits back, satisfied.{/n} "If you ever need a queen, Commander, I know where you can find one. Ha! Only joking. Another round!"''',
    answer_list=KING_C5, speaker="conversant", NativeReturnCue=KING_C5_BACK, relationship=REL,
    forbids=("fool_king.gone", CLOSED), entry='"How\'s the court, Your Majesty?"', chapter=5, last=5, Chapters=[5], delay=12))

SCENES.append(reaction("Irabeth", P + "react.irabeth.drill_alone", (DRILL,),
    '''"I rode past the Crows' tent this morning with the Eagle Watch." {n}Irabeth says it to the roster, not to you.{/n} "She was at her forms in the mud behind it, alone, cut and guard and cut, the way the old knights of Mendev used to drill." {n}A pause.{/n} "Forty knights rode past, and not one of them saluted a knight of a minor order at her drill. They were right not to. That is the whole of the Queen's last command." {n}Her jaw works.{/n} "I saluted. From the road, where she could not see. I wanted somebody to know that I did it once."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"Anything to report, knight?"', chapter=5, last=5, delay=12,
    portrait="Irabeth", **{**IRABETH_GUARD, "forbids": IRABETH_GUARD["forbids"] + (P + "kitrane.squire_sworn",)}))

for rid in (P + "react.irabeth.carried", P + "react.irabeth.alone", P + "react.irabeth.drill", P + "react.irabeth.learned",
            P + "react.irabeth.drill_alone", P + "react.irabeth.after_death", P + "react.seelah.majesty",
            P + "react.hulrun.door", P + "react.hulrun.ledger", P + "react.daeran.cousin", P + "react.king"):
    tag(rid, "T")


# --- Epilogue pages (T; ordered siblings; read-only) ---------------------------------------------------------------------------

EPI = "GalfreyEpilogue"


def epilogue(id, title, text, requires, forbids=(), paragraphs=(), survived=True):
    """survived: the page is a shared life, so it waits for the Commander to have lived (or cheated death)."""
    extra = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"}) if survived else {}
    SCENES.append(scene(P + "epilogue." + id, title, EPI, 6, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=tuple(forbids) + (("sacrifice",) if survived else ()),
                        last=6, Relationship=REL, **extra))
    tag(P + "epilogue." + id, "T")


KITRANE_PARAGRAPHS = (
    p('''{n}After Threshold she rode to Nerosyan in a green surcoat, walked into the cathedral in the middle of the spring vigil, and had the royal crypt opened in front of the bishops, the regents and half the court. She named the man inside it: Sir Anselm Wray, of the Green Crows, who had died beside her at Iz. Then she took off her hood. His daughter buried her father that summer with every honour Mendev had. The Queen stood at the graveside in plain armour, and nobody in Mendev ever forgot it.{/n}''',
      requires=(CROWN,)),
    p('''{n}When the church offered to buy her a third cup of the elixir, she refused it at the altar, in front of them all, and Mendev watched its Queen grow old after a century of standing still, one grey hair and one stiff winter at a time. When she was tired, she abdicated. She said she had always meant to try being a knight of some small order nobody had heard of.{/n}''',
      requires=(CROWN,)),
    p('''{n}Mendev never forgave the Commander for it entirely. There were inquiries, and sermons, and one very long letter from the Inquisitor Hulrun. The Commander answered all of them, in person, for years.{/n}''',
      requires=(CROWN,), forbids=("hulrun.dead",)),
    p('''{n}Mendev never forgave the Commander for it entirely. There were inquiries, and sermons, and one very long letter from the bishops of Nerosyan. The Commander answered all of them, in person, for years.{/n}''',
      requires=(CROWN, "hulrun.dead")),
    p('''{n}She stayed Kitrane. The Queen of Mendev lay in the crypt at Nerosyan, and Sir Anselm Wray kept her place there, and every year on the day of Iz his daughter found a purse at her door from a knight who owed him a debt. She never learned who sent it. It came every year until the knight was very old indeed.{/n}''',
      requires=(FOREVER,)),
    p('''{n}She grew old without a third cup of the church's elixir, in the ordinary way, and complained about her knees, and was delighted by every one of her grey hairs, and made the Commander count them on bad nights.{/n}''',
      requires=(FOREVER,)),
    p('''{n}Whether she would ever take the crown back she did not say, and the Commander never asked. Some years she seemed close to it. Most years she was drilling squires in the mud behind a tent that leaked on the left.{/n}''',
      forbids=(CROWN, FOREVER)),
    p('''{n}The tear in her voice never mended. She stopped making speeches. When she had something to say to a crowd, she said it to one person in it, and let them pass it on.{/n}''',
      requires=(RENT,)),
    p('''{n}She never quite forgave the Commander for not coming to Iz, or herself for writing the letter anyway. They argued about it once a year, on the anniversary, and neither of them ever won.{/n}''',
      requires=(ALONE,)),
    p('''{n}The Green Crows grew, slowly. The girl from the eel stall was knighted in the third year after the war, by a knight of the order in plain armour, in a field, with nobody watching but a mule. She was the first Crow in a century who had never lied about anything.{/n}''',
      requires=(P + "kitrane.squire_sworn",)),
    p('''{n}At the eastern ford she had refused an order of the Commander's, and six people hanged anyway. She never pretended afterwards that she had forgiven it. Every year on that day she and the Commander walked down to a grave in the lower town of Drezen with a tallow candle, and stood there together, and neither of them ever said it was enough.{/n}''',
      requires=(REFUSED_ORDER, P + "ride.answered")),
    p('''{n}At the eastern ford she had refused an order of the Commander's, and six people hanged anyway, and the Commander never went down to the tallow-seller's. She served to the end all the same. She never once spoke of the ford again, and never once, afterwards, rode where the Commander could order her to stand beside a rope.{/n}''',
      requires=(REFUSED_ORDER,), forbids=(P + "ride.answered",)),
    p('''{n}Every morning of the rest of her life she drilled at first light, and nobody saluted. She said it was the best part of the day.{/n}''',
      requires=(DRILL,)),
    p('''{n}The Inquisitor Hulrun never turned round at the chapel door. After the war he came to the Crows' tent one evening with his ledger under his arm, sat down on the mule's feed-box, and said nothing at all for an hour. Then he said, "Your Majesty," once, very quietly, and went away. Neither of them ever mentioned it again.{/n}''',
      requires=(P + "kitrane.hulrun_seen",), forbids=("hulrun.dead",)),
    p('''{n}On Thursdays she played dice in the Fool King's tavern and lost, loudly, to a drunkard in a paper crown, and was, the tavern agreed, the worst knight the kingdom of the tavern had ever sausaged.{/n}''',
      requires=(P + "kitrane.king_seen",)),
    p('''{n}A treatise on the campaign for Threshold, written in Absalom a decade later, devoted a chapter to "the unknown knight of the Green Crows" whose advice was said to have saved the army at the dry riverbed. She read it aloud to the Commander in bed, in a variety of silly voices.{/n}''',
      requires=(P + "kitrane.war_table",)),
    p('''{n}She kept the letter she had once hidden in a wall in the lid of her armour chest, with Sir Anselm's broadsheet, and never read it again. Once, very late, she told the Commander what it said, word for word, and then laughed at the Queen who wrote it.{/n}''',
      requires=(P + "kitrane.letter_returned",)),
    p('''{n}The letter she had once hidden in a wall stayed where the Commander kept it. Every few years she asked to read it again, and every time she laughed at the Queen who wrote it, and every time she kept the Commander's hand for a while afterwards.{/n}''',
      requires=(P + "kitrane.letter_kept",)),
)

epilogue("kitrane", "Kitrane", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan. Mendev mourned her for a year and a day.{/n}
{n}A knight of the Green Crows named Kitrane, of no lands, no crown and no enemies, lived a great deal longer. She followed the Commander to the end of the war as a knight of the Crows, and on its last night she kept the walls of Drezen among the soldiers who had not been sent to Threshold, in the crowd, where she had asked to be; and the Commander, whatever else became of the world, never once failed to look for her there.{/n}''',
         requires=(RETURNED, COMMITTED), forbids=(CLOSED,), paragraphs=KITRANE_PARAGRAPHS)

epilogue("sworn", "Kitrane, sworn", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan.{/n}
{n}Kitrane of the Green Crows served the Commander of the Fifth Crusade to the end of the war, as she had sworn: correctly, promptly, and without once laughing where the Commander could hear. She was the best knight the Commander ever had. When the war was over she asked, in writing, to be released from her oath, and the Commander released her the same day, and she rode away from Drezen at a walk with a squire and a mule, and did not look back more than once.{/n}''',
         requires=(RETURNED, SWORN), forbids=(COMMITTED, CLOSED), paragraphs=KITRANE_PARAGRAPHS)

epilogue("late", "Kitrane, late", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan.{/n}
{n}The war ended before the knight of the Green Crows had sworn her sword to anyone. On the evening after Threshold she found the Commander on the citadel wall, and stood beside them for a long time without speaking, and then asked, as herself and nobody else, whether there was room in the Commander's crowd for one more face. She said it was the first question she had ever asked for her own sake. She did not seem to mind the answer being slow.{/n}''',
         requires=(P + "late_committed",), forbids=(COMMITTED, SWORN, CLOSED), paragraphs=KITRANE_PARAGRAPHS)

epilogue("widow", "Kitrane, after", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan.{/n}
{n}The Commander of the Fifth Crusade did not come back from Threshold. A knight of the Green Crows named Kitrane kept the walls of Drezen that night, as she had asked to, and was there when the news came in the morning. She did not weep where anyone could see. She walked down to the chapel, and stood at the back, as she had once stood for her own vigil, and stayed until the candles went out.{/n}
{n}She lived a long time after, as nobody in particular, and grew old without a third cup of the church's elixir. Every year on the day of Threshold she went up onto the walls of Drezen at dusk and stood in the crowd, and looked, out of old habit, for a face that was not there.{/n}''',
         requires=(RETURNED, COMMITTED, "sacrifice"), forbids=("trickster.commander_back", "lastcall.active", CLOSED), survived=False)

epilogue("alive", "The Queen and the knight", '''{n}Queen Galfrey of Mendev did not die at Iz. She came home from the Worldwound with her crown on her head, and ruled, and was severe and exact with the world, and trusted the Commander of the Fifth Crusade as a queen trusts her general, and no further; she had said so, and she was a woman who meant what she said.{/n}
{n}On certain nights, a knight of the Green Crows with loose hair and an old sword was seen going into the Commander's quarters after the ninth bell, and coming out before first light, and nobody in Drezen or Nerosyan ever put a name to her. Kitrane had no lands, no crown and no enemies. She had one plan kept, and then another, and in time she stopped counting.{/n}''',
         requires=(FINAL, COMMITTED), forbids=(DEAD, RETURNED, CLOSED))

epilogue("native", "The Queen and the Trickster", '''{n}Queen Galfrey of Mendev did not die at Iz. Shortly after the war she laid down the crown, as the chronicles record, and left Nerosyan to spend the rest of her long life with the one who had shown her there was more to life than duty; and Mendev, which had expected to bury her, did not quite know what to do with her alive and uncrowned.{/n}
{n}What she and the Commander were to each other was her own affair, and she made sure everyone understood it. She was severe and exact with the world to the end of her days, and with one person she was neither.{/n}''',
         requires=(FINISHED, FINAL), forbids=(DEAD, RETURNED, CLOSED), paragraphs=(
             p('''{n}On the rare evenings she could be persuaded into the Fool King's tavern, she held her cup like somebody who was used to being watched, and spilled some early, on purpose, so that everybody could stop waiting for it. The Commander's strange court of jesters and drunkards took her in without a word, the way it took in everyone, and she found, to her lasting surprise, that she liked it there.{/n}''',
               requires=("fool_king.available",), forbids=("fool_king.gone",)),
             p('''{n}The Commander's strange court had no king in it by then, only a tavern bench where one had once sat, and she sat on it now and then, as if keeping it warm for somebody.{/n}''',
               requires=("fool_king.gone",)),
         ))

epilogue("queen", "The Queen", '''{n}Queen Galfrey of Mendev died at Iz, as the Queen, with her Commander at her side and her knights around her. At the very end she had been offered another name, and she had not taken it. She was buried with honours in Nerosyan, in her own armour, and Mendev mourned her for a year and a day.{/n}
{n}The Commander did not speak at her vigil. Somebody asked, afterwards, whether there had been anything the Commander could have done. The Commander said that there had, and that she had been asked, and that she had been right.{/n}''',
         requires=(LET_DIE,), forbids=(RETURNED, LEFT_EARLY))

epilogue("queen_bier", "The Queen", '''{n}Queen Galfrey of Mendev died at Iz, as the Queen, with her knights around her and her Commander elsewhere. Three days later, on a bier in the citadel chapel of Drezen, she was offered another name, and she did not take it. The lead seal went on at first light, with every bell in the city, and she was buried with honours in Nerosyan, in her own armour.{/n}
{n}The Crows' sergeant who had kept the chapel door never spoke to the Commander again. When he was asked, years later, what had passed in there that night, he said only that the Queen had been asked, and had answered, and that it was more than most people got.{/n}''',
         requires=(LET_DIE, LEFT_EARLY), forbids=(RETURNED,))


def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Her native reads (the incognito meeting, Seelah at the bed, the farewell letter found, Galfrey_Final, the rank kept),
    her Derived keys and the book-picture fallback. Other world keys bind on demand in trickster_world."""
    for kind, table in BINDINGS.items():
        _bind(payload, kind, table)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("PortraitFallbacks", {}).setdefault("Galfrey", PORTRAIT_GUID)
    # A completed native romance and the Iz branch taken stay true once observed.
    payload["PermanentEtudes"] = sorted(set(payload.get("PermanentEtudes", [])) | {FINISHED, MANU, KC_KEPT})
