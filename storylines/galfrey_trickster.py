"""Queen Galfrey on the Trickster path: "The Queen dies; Kitrane walks out" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, rewritten
2026-09-29 (R4) after the Astra design review r4, with its build sheet; it supersedes the permit device, the F19 drill and the
priced second ask of Writer/handoffs/trickster/galfrey.md, whose canon table and reactors stay valid).

Canon (blueprints.zip / enGB):
- Kitrane is hers: "I have introduced myself as Kitrane, an old friend of yours. I am a knight of a minor order, the Green
  Crows." (Galfrey_Incognito/Cue_0001 19d217c3); "It's been a long time since I traveled like this, as just another face in
  the crowd..." (Cue_0004 d5133def); "Don't forget, here I am Kitrane the knight." (Cue_0013 ee76d13d).
- She accepted the church's decision and responsibility: "the decision to prolong my life was not mine. It was the decision of the church of
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
sorcery has rent the soul of the Queen of Mendev, who accepted the church's decision to prolong her life. If the Queen dies in public
and the woman answers to another name, it may let go. Nobody knows. She chooses: asked for Mendev she refuses, asked for
herself she takes it. The native death plays; her last command, as Queen, sends the wounded knight Kitrane to the rear; a
Crows knight who died beside her goes home to Nerosyan in the Queen's sealed coffin. What the Commander saw at the bed decides
when the rending lets go: on the road (read), or only when Drezen proclaims her dead (blind: the tear stays in her voice).

Native Trickster precedent: the Fool King's invented pedigree becomes real (C3_FoolKing/Obj_025_ReadyForCrowning
3fb92b54fc950714799b3444672d39e6). This is a limited precedent for an impossible deception acquiring force, not proof
of name-sensitive sorcery, a permission to die, a new prerequisite or an echo. Galfrey has no Shyka-page consumer.

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
LEFT_EARLY = "iz.left_early"              # DidntVisitedEvents: unresolved Galfrey encounter, not absence from Iz
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
CORTEGE_PAID = P + "cortege.paid"           # Q12: the Commander bought the Crows' sergeant at the chapel door (not talked past him)
CORTEGE_TOLD = P + "cortege.name_told"      # Q12: the sergeant, not the Commander's memory, supplied the name Kitrane at the bier
LATE_FOUND = P + "cost.found_late"          # unprepared: found on the bier at Drezen; the sergeant persuaded or bought
NATIVE_REFUSED = "galfrey.native_refused" # SeenCues DrezenMain_C5/Galfrey/Cue_0041: personal distrust, not never-courted history
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
               MANU + ".live": "4b3f1b15817e2034f85d7fa7b2a6f20a",   # area Iz only: latch source (trickster_world LATCHES)
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
    conv("like", '"Like her?" {n}She looks along the tents.{/n} "I like eating my supper before someone brings me a petition. The stew is poor. For once it was still hot when I finished. In Nerosyan I could scarcely manage that."',
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
    conv("refused", '{n}The warmth goes out of her face as neatly as a blade goes into a scabbard.{/n} "If I tell the army I expect to die, I cannot expect them to fight as though I shall lead them home." {n}She lets that stand a moment.{/n} "Mendev does not need a spare queen, Commander. It needs this one alive, which is a matter for my sword and your army, not for a borrowed name. I came here as Kitrane so that the demons would not know where the Queen was. I did not come here to practise being dead."',
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
    conv("refused", '"If I tell the army I expect to die, I cannot expect them to fight as though I shall lead them home." {n}The words come out flat and practised; she has said them before, perhaps to herself.{/n} "Mendev does not keep a spare, Commander. It keeps faith. If I fall at the Fane, I shall fall as what I am, and the crusade will go on because it must, not because I left a costume in a trunk."',
        c('[Let it go.] "As you say."', "end"),
        c('[Press her, as a friend] "Then forget Mendev for a moment. Think about it for yourself, and tell me after the Fane."', "pressed",
          flags=(PRESSED,)),
        c('[Press her, as her general] "Think about it anyway. Mendev can\'t afford a sentimental queen."', "pressed_general",
          flags=(PRESSED_GENERAL,))),
    conv("pressed", '{n}Her eyebrows rise.{/n} "For myself. Very well. Ask me after the Fane, when I am not about to send men into a demon lord\'s temple."',
        c("[Leave her to her thoughts.]", "end")),
    conv("pressed_general", '''"Sentimental." {n}The Queen's voice goes very even, which in Galfrey is worse than shouting.{/n} "I have buried three generations of knights in the Worldwound, Commander. I know exactly what Mendev can afford." {n}A pause.{/n} "But you are my general, and you have asked. I shall think on it tonight, as a general's advice. You will have your answer."''',
        c("[Bow, and leave her.]", "end")),
    conv("liked", '''"Liked her." {n}The Queen tilts her head, and very nearly smiles.{/n} "So did I. It is a pity she was so short-lived. Back under canvas, and then a crown fell on her." {n}She lets the smile go.{/n} "Now. We were speaking of the Fane."''',
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
    n("take", "Crows' sergeant", '{n}He takes the purse and weighs it.{/n} "A cart, a cloak, and a surgeon. If she asks, they will be ready. If she does not, I never saw you." {n}He lays the purse under his sword-belt.{/n} "Anselm will ask what you bought. I shall tell him a horse. He will want to see it."',
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
    nar("camp", '{n}In the war camp she introduced herself as Kitrane, a knight of the Green Crows and an old friend of yours. Her bodyguards wore the same colours. Below the balcony, another masked woman pushes through the crowd.{/n}',
        c("Continue", "mooted", requires=(PLANTED,)),
        c("Continue", "refused", requires=(CROWS_REFUSED,), forbids=(PLANTED,)),
        c("Continue", "plain", forbids=(PLANTED, CROWS_REFUSED))),
    nar("queen", '{n}Before that there was the Queen in Drezen, holding court in the square below the Fane: a woman of a hundred and more who looked nowhere near it, because two cups of sun orchid elixir had kept her young. The court addressed her by her title.{/n}\n{n}You look down at the market full of borrowed faces and wonder what the Queen of Mendev would look like with nobody watching.{/n}',
        c("Continue", "plain")),
    nar("mooted", "{n}You had raised the possibility of a life under Kitrane's name. Galfrey had considered it. In Alushinyrra, where borrowed faces pass beneath your balcony, you recall the plain green surcoat she wore in the camp.{/n}",
        c("Continue", "address")),
    nar("refused", '{n}You offered her a name to keep in reserve. She refused it: the army needed her alive, and she would not prepare a substitute before the battle. Below your balcony, a slaver lifts a mask to count his money.{/n}',
        c("Continue", "address")),
    nar("plain", '''{n}Somewhere up there, in Drezen or in Nerosyan, she is being the Queen of Mendev at somebody. You hope, a little to your own surprise, that she has an hour in the day when she is not.{/n}''',
        c("Continue", "address")),
    nar("address", '{n}A masked woman bargains with a hag over a charm against the evil eye. The hag asks her name. The buyer will not give it. "Then give it someone else\'s," the hag says. "Let the curse go looking for them." The buyer laughs and keeps her purse closed.{/n}',
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
    c('[Perception DC 18] {n}Watch the wound as you say it, the way she would want it said:{/n} "Your Majesty."', requires=(PLANTED,),
      check=dict(Skill="SkillPerception", DC=18, Success="read", Failure="blind", CommanderOnly=True)),
    c('[Perception DC 22] {n}Watch the wound as you say it, the way she would want it said:{/n} "Your Majesty."', forbids=(PLANTED,),
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
    n("pitch", "Narrator", "{n}You explain the gamble. The sorcery struck the Queen at Iz and rent her soul. Perhaps it had fastened on the Queen it struck. A sealed coffin, her name on the lid, and a knight carried among the wounded might turn it aside. Neither of you knew whether the deception would loosen the spell.{/n}\n\n{n}The Queen's name would go home in the coffin. The woman in the cart would answer to Kitrane. Her knights would have to carry the lie, and she would have to live with it. The sorcery might still kill her.{/n}",
      c("Continue", "address", requires=(ADDRESS,)),
      c("Continue", "planted", requires=(PLANTED,), forbids=(ADDRESS,)),
      c("Continue", "refusedbefore", requires=(LETTER_REFUSED,), forbids=(PLANTED, ADDRESS)),
      c("Continue", "mendev", forbids=(PLANTED, LETTER_REFUSED, ADDRESS))),
    n("address", "Narrator", "{n}You repeat the hag's advice from the Midnight Isles market: give the curse someone else's name to follow. The buyer had laughed at it. You have no account of the spell that struck Galfrey, and you tell her that too.{/n}",
      c("Continue", "planted", requires=(PLANTED,)),
      c("Continue", "refusedbefore", requires=(LETTER_REFUSED,), forbids=(PLANTED,)),
      c("Continue", "mendev", forbids=(PLANTED, LETTER_REFUSED))),
    n("planted", "conversant", '''"Kitrane has no lands, no crown and no enemies." {n}It is almost a laugh.{/n} "I said that to you. I suppose you wrote it down. You write everything down." {n}Her hand finds your sleeve and holds it.{/n} "I said it as a woman says she would like to see the sea. I did not think anyone would take me at my word."''',
      c("Continue", "mendev")),
    n("refusedbefore", "conversant", '''"I wrote you my answer before the Fane." {n}Her voice is thin, but the steel is all there.{/n} "No spare queens. No costumes in trunks. I have not changed my mind because I happen to be dying. That is when a person's mind should change least."''',
      c("Continue", "mendev")),
    n("mendev", "conversant", '''"My death sows chaos among our forces. I have known it for a hundred years; I have planned for it." {n}Her grip tightens on your sleeve.{/n} "So tell me, Commander. What becomes of Mendev?"''',
      c('[For her] "You accepted Mendev\'s burden. I am asking whether you want to live when the Queen can no longer carry it."', "accept_rent",
        requires=(BLIND,), flags=(TAKEN, STARTED, RENT)),
      c('[For her] "You accepted Mendev\'s burden. I am asking whether you want to live when the Queen can no longer carry it."', "accept",
        forbids=(BLIND,), flags=(TAKEN, STARTED)),
      c('[For Mendev] "Mendev keeps its Queen\'s legend and loses nothing it can see. Kitrane\'s death sows no chaos at all."',
        "for_mendev", forbids=(OFFER_REFUSED,)),
      c('[Let her die as the Queen] "...No. You were the Queen of Mendev. Die as her."', "let_die", flags=(LET_DIE, CLOSED))),
    n("for_mendev", "conversant", '"For Mendev." {n}She turns her face away, then back.{/n} "If you need a Queen, look at me. You have no use for this one now." {n}Her grip tightens on the cloak.{/n} "I accepted the elixir. I accepted the crown. Do not tell me those choices were someone else\'s. If you want me to take this chance, ask for me. Here, now. You have commanded enough for one day."',
      c('[As her friend] "Then as your friend: I want you to live. Will you take this chance?"',
        "accept_rent", requires=(BLIND,), flags=(OFFER_REFUSED, TAKEN, STARTED, RENT)),
      c('[As her friend] "Then as your friend: I want you to live. Will you take this chance?"',
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
    ga("read", '{n}She is awake. Her face is grey with fatigue and there is a crust of dried blood along her jaw, but when the wheel jolts over a stone she swears at it, fluently, in a voice rough from the cold.{/n} "Commander." {n}She does not try to sit up.{/n} "I am told I was dead for the better part of an hour. The Crows\' surgeon had given up; he was praying over me. Then the sergeant hammered the lead seal onto the Queen\'s coffin, with her name on the lid, and it let go. Like a hand opening." {n}Her fingers move on the cloak, as if to show you.{/n} "I heard the hammer. I have been riding among the wounded since."',
        c('"How does it feel?"', "feel"),
        c('"You swear like a sergeant."', "swear")),
    ga("swear", '''"I learned from sergeants. A queen is not permitted to use it." {n}Something that is very nearly a grin.{/n} "Kitrane may do as she likes. I have been practising since the milestone. The squire is scandalised, but he is a Crow, and the Crows are very discreet."''',
        c("Continue", "feel")),
    ga("feel", '''"Light." {n}She considers it with care, the way she considers everything.{/n} "And wrong. There is a coffin three carts ahead with my name on it, and a good man in it who has no name at all now." {n}She looks up at the sky, which is the colour of a bruise.{/n} "Sir Anselm Wray. Sixty-one. Deaf in the left ear. He joined my guard because, he said, he could not hear the demons coming anyway, so he might as well stand next to someone who could."''',
        c("Continue", "anselm")),
    ga("anselm", '''"His daughter keeps his house in Nerosyan. She will be told that he is missing at Iz. That is the kindest lie available, and it is mine, and I shall answer for it." {n}Her mouth tightens.{/n} "Do not tell me he would have wanted it. He would have. That is not the point."''',
        c('"Then what is the point?"', "point"),
        c("[Ride beside the cart in silence for a while.]", "silence")),
    ga("point", '"That I let him." {n}She closes her eyes.{/n} "A hundred years, Commander, and I have let a great many people pay for me. I hoped this escape would cost no one else. His daughter will be looking for him while I buy boots. I shall have to answer for that." {n}A breath.{/n} "Go on ahead. I need to be nobody for a little longer, and nobody does not ride with the Commander."',
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
    nar("start", "{n}The Queen's coffin stands before the altar under the blue and silver of Mendev. Her sword lies along the lid. Sir Anselm is inside; Kitrane has his sword in the Crows' camp. The knights who carried them know the difference and keep their places beside the coffin.{/n}",
        c("Continue", "hulrun", forbids=("hulrun.dead", "hulrun.away_c5")),
        c("Continue", "chaplain", requires=("hulrun.dead",)),
        c("Continue", "chaplain", requires=("hulrun.away_c5",), forbids=("hulrun.dead",))),
    nar("hulrun", '''{n}Inquisitor Hulrun has said the prayers. His voice broke twice; both times he went on. Now he steps back from the altar and looks at you, red-eyed, the way a man looks at the last wall standing between him and the dark.{/n}''',
        c("Continue", "speak")),
    nar("chaplain", '''{n}The chaplain of the citadel has said the prayers, in a thin voice, because the Inquisitor who should have said them is not in Drezen to say them. Now he steps back from the altar and looks at you, and so does everyone else.{/n}''',
        c("Continue", "speak")),
    nar("speak", '{n}You stand before the closed coffin. The knights at its head know what lies inside; the congregation behind you does not. They wait for you to speak.{/n}',
        c("[Tell them the truth about her. Every word, but one.]", "true", flags=(EULOGY, EULOGY_TRUE, SECRET)),
        c("[Give Drezen the legend it needs to go on fighting.]", "legend", flags=(EULOGY, EULOGY_LEGEND, SECRET)),
        c("[Hide one line in it, for one listener.]", "sign", flags=(EULOGY, EULOGY_SIGN, SECRET), mythic="Trickster")),
    nar("true", '''{n}You tell them about the Queen you knew. That she was curious, and could not sit still, and came to the crusade because her blade had been in its scabbard long enough. That she was hard on her Commander and harder on herself. That she thought of her soldiers first. That she was proud, and knew it, and served anyway.{/n}
{n}Every word of it is true, except the one in the middle that makes it a eulogy. When you are done the chapel is so quiet you can hear the candles.{/n}''',
        c("Continue", "after")),
    nar("legend", "{n}You give them the Queen of the chronicles: the paladin chosen by the Inheritor, the century of vigil on the edge of the Wound, the last charge at Iz against the servants of the Lord of Locusts. You give them a queen who never doubted and never slept and died with the goddess's name on her lips.{/n}\n{n}The knights weep. The chaplain lowers his head over the coffin.{/n}",
        c("Continue", "after")),
    nar("sign", "{n}You speak of the Queen's sword and the soldiers who stood beside her at Iz. You name the Green Crows, who carried the wounded out while the enemy still held the ruins. Their sergeant raises his head. Several knights in the congregation straighten when they hear their order named.{/n}",
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
    nar("done", "{n}Afterwards the chapel empties slowly. You remain beside the coffin until the last prayer ends. Sir Anselm's name is absent from every one of them.{/n}",
        c("[Put out the lamp.]")),
], requires=("trickster.ever", TAKEN, DEAD), forbids=(RETURNED, CLOSED), delay=30, kind="event", owner="Commander", Areas=[DREZEN],
    TricksterDevice=True, TricksterState="dead")
tag(P + "iz.eulogy", "T")

household.secret(
    SECRET_KEY, "The Queen's eulogy",
    'I stood before the altar in Drezen and spoke for the Queen of Mendev, knowing that the coffin held Sir Anselm Wray and that Kitrane was breathing outside the walls. The knights who carried her know. The chapel heard my words; I cannot be certain how many heard the lie.',
    portrait="Galfrey", witnesses=("irabeth", "seelah"), risk="medium")


# --- Chapter 5 (T, a letter): the Commander never came --------------------------------------------------------------------------
# DidntVisitedEvents: she fought the dragon without the Commander and died off the page. Only if she had mooted Kitrane does she
# take the old offer herself; otherwise canon stands and nothing here opens.

page(P + "iz.alone", "A letter sealed in green", [
    nar("open", '''{n}The letter comes by a Crows' courier who will not give his name, sealed in plain green wax with no device. The hand is firm and old-fashioned, and in places it shakes so badly that the pen has gone through the paper.{/n}''',
        c("[Break the seal.]", "letter")),
    ga("letter", '"Commander,\n"You did not come to my aid at Iz. I do not reproach you for it. I sent you into the Abyss, and a commander goes where the war requires.\n"I fought without you beside me. The enemy\'s sorcery went into me like a hook into a fish. My knights bound the wound three times. I lay in the rubble with Pharasma\'s door in front of me and I thought, quite calmly: so this is how the Queen ends."',
        c("Continue", "letter2")),
    ga("letter2", '"And then, because I am an old woman and my mind wanders, I thought of a knight of a minor order who had her boots stolen twice in the war camp. You once told me she could outlive the Queen. I said some days I envied her.\n"So I tried it. Nobody offered; you were not there to. But your old sergeant had his orders and a cart, and he knelt in the rubble and waited for me to say the word. I offered it to myself. I do not recommend it; it is very lonely."',
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
    nar("start", "{n}The Queen's cortege comes through the gate of Drezen at dusk, three days out of Iz: a cart draped in blue and silver, knights walking beside it bareheaded, and the whole of the lower town lining the road in silence. It will lie one night in the citadel chapel. In the morning the lead seal goes on, and it goes home to Nerosyan.{/n}\n{n}You did not reach her before she fell. The knights at the gate leave room for the cart, and none for you.{/n}",
        c("Continue", "surgeon")),
    n("surgeon", "Crows' sergeant", '{n}An old knight in a green surcoat with three black birds on the breast is standing guard at the chapel door, and does not step aside for you.{/n} "Commander." {n}His voice is hoarse.{/n} "The surgeon says it is the Wound\'s cold that keeps her. She has not stiffened. Since they brought her in, she has not stiffened, and she has not breathed either, that anyone can swear to." {n}He looks at you as if you were to blame for all of it, and perhaps you are.{/n} "They seal her at first light."',
        c("[Diplomacy DC 24] \"Let me in. There's a thing she said once, in the war camp, about a knight of your order. I need to say it back to her.\"",
          check=dict(Skill="CheckDiplomacy", DC=24, Success="in", Failure="barred", CommanderOnly=True)),
        c("[Pay him] \"Then let me sit a vigil. Here: for the Crows, for the road home.\"", "bought", crusade=("Finances", -300), flags=(CORTEGE_PAID,)),
        c("[Leave the Queen to her knights.]", abort=True)),
    n("barred", "Crows' sergeant", '"No." {n}Flat as a blade.{/n} "You did not come to her aid. You do not get to walk past her guard now." {n}And then, because he is an old soldier and knows what a purse is for, he looks at your belt and away again.{/n}',
        c("[Pay him] \"For the Crows, and the road home.\"", "bought", crusade=("Finances", -300), flags=(CORTEGE_PAID,)),
        c("[Leave the Queen to her knights.]", abort=True)),
    n("bought", "Crows' sergeant", '''{n}He takes it. He hates himself for taking it, and hates you worse, and it is all there in his face.{/n} "One hour. And if you do anything to her, Commander, I will know."''',
        c("[Go in.]", "in")),
    nar("in", '''{n}The chapel is cold. She lies on the bier in her ruined armour with her sword on her breast, and the wound at her collarbone is bound in linen that has gone black, and under the linen, if you look long enough, there is something that is not blood: a slow dark light, still burning, patient as a lantern in a window.{/n}
{n}She is not dead. She is not anything. Whatever took her at Iz is still holding on, and it is holding on to the Queen of Mendev.{/n}''',
        c("[Kneel, and say it close to her ear.] \"Your Majesty.\"", "flare", requires=(MET,)),
        c("[Kneel, and say it close to her ear.] \"Your Majesty.\"", "flare_told", forbids=(MET,))),
    nar("flare_told", '{n}The dark light brightens. Her hand, on the sword, closes by a hair.{/n}\n{n}Behind you, at the door, the sergeant makes a sound like a man who has been hit.{/n} "Don\'t. Not that." {n}He comes two steps in, and stops, as if the chapel floor might not bear him.{/n} "In the war camp, before Drezen, she went about among our tents in our surcoat and called herself Kitrane. A knight of ours, she said, back from somewhere. She laughed when one of the squires called her Kitrane. He thought he had offended her." {n}His jaw works.{/n} "If you have to say something to her, Commander, say that."\n{n}You have no plan for this, and no time to make one. You have an old man\'s grief and a name she once chose for a joke, and the fact that it is the only name in the world this thing does not know.{/n}',
        c('[Offer her another name] "Kitrane. Kitrane of the Green Crows. Your sergeant remembers you. Come back as her."', "wake", mythic="Trickster", flags=(CORTEGE_TOLD,))),
    nar("flare", '''{n}The dark light brightens. Her hand, on the sword, closes by a hair.{/n}
{n}You have no plan for this, and no time to make one. You have what you saw in a war camp and the name she chose for herself there, and the fact that it is the only name in the world this thing does not know.{/n}''',
        c('[Offer her another name] "Kitrane. Kitrane of the Green Crows. You told everyone you were my old friend. Come back as her."', "wake", mythic="Trickster")),
    ga("wake", '{n}It takes a long time. Her lips move before her eyes open, and her eyes, when they open, do not find you at once.{/n} "Commander." {n}Barely a breath.{/n} "You did not come to me at Iz." {n}A longer silence.{/n} "Kitrane. That was a joke. For the war camp." {n}Her fingers move on the sword hilt.{/n} "I am so tired. Tell me why I should wake up as a joke."',
        c('"You accepted the crown and carried it through this war. I am asking you to live beyond it."', "choose"),
        c('[Let her go] "...Then do not. Rest, Your Majesty."', "rest", flags=(LET_DIE, CLOSED))),
    ga("choose", '''"Choose." {n}Something that was almost a laugh once.{/n} "In a cold chapel, three days dead, with the lid on the floor. You pick your moments, Commander." {n}Her hand turns on the hilt and finds yours.{/n} "Very well. The Queen is in the box. Put someone in it with her name; the Crows lost a man at Iz, Sir Anselm, and he would think this very funny." {n}Her eyes close again.{/n} "Seal it at first light, with every bell. It wants to hear it said. And then carry out a knight."''',
        c("[Call the sergeant in, and tell him what she said.]", "sergeant")),
    n("sergeant", "Crows' sergeant", '''{n}He comes in with his hand on his sword, and stops, and sees her eyes open, and goes down on both knees on the chapel stones as if his legs had been cut.{/n} "Your Maj..." {n}He stops himself. He is not a stupid man.{/n} "Kitrane." {n}A long breath.{/n} "Anselm is in the cart. We were taking him home. He will be taking her home instead." {n}He looks up at you, and whatever was in his face at the door is not gone, and never will be.{/n} "First light, Commander. With every bell."''',
        c("[Stay until first light.]", flags=(TAKEN, RENT, ALONE, STARTED, COFFIN, LATE_FOUND))),
    ga("rest", '{n}The fingers on the sword loosen.{/n} "Thank you." {n}It is hardly a word.{/n} "You were not beside me then. You are here now. That will have to do."',
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
        nar("start", "{n}The Crows' sergeant steps aside. A knight in their green surcoat is waiting behind him, her hands resting on an old sword. She lifts her head when you approach. You know the face printed on Drezen's mourning broadsheets.{/n}",
            c("Continue", "name")),
        ga("name", voice + '''"Kitrane. Of the Green Crows." {n}She inclines her head exactly as far as a knight of a minor order inclines it to the Commander of the crusade, and not a hair further.{/n} "An old friend of yours, I am told."''',
            c('"Your Majesty."', "majesty"),
            c('"Kitrane. You\'re late."', "late"),
            c("[Say nothing. Look at her.]", "look")),
        ga("majesty", '{n}She does not flinch. You watch for it, and it does not come.{/n} "No." {n}Very quietly.{/n} "That word does nothing to me now. I tried it on myself in the tent, after the fever broke, like a man pressing a bruise. Nothing." {n}A breath.{/n} "But do not say it again. Not because it hurts. Because it is not true, and a great many people in this city are wearing black because it is not."',
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
        ga("e_true", '''"You told them the truth about me." {n}She looks away, at the black on the gate.{/n} "All of it. Proud, and hard, and could not sit still." {n}Her voice roughens.{/n} "It was the most honest thing said over that coffin, and it was said over the wrong coffin. I have been trying to decide whether to thank you."''',
            c("Continue", "why")),
        ga("e_legend", '''"The Queen of the chronicles. Chosen of the Inheritor, never doubted, never slept." {n}Dry as dust.{/n} "The knights wept. I expect half of them will name daughters after that woman. I should very much like to meet her. She sounds exhausting." {n}A pause.{/n} "It was well done, Commander. It was what Drezen needed. Do not ever do it to me again."''',
            c("Continue", "why")),
        ga("e_sign", '"You remembered the Crows." {n}She looks toward the chapel.{/n} "I heard their name. The sergeant came back with his shoulders straight for the first time since Iz." {n}Her hand rests on Sir Anselm\'s sword.{/n} "He asked me whether I had heard. I had to make him repeat it before I could answer."',
            c("Continue", "why")),
        ga("e_none", '"Drezen rang every bell it had. They could hear it in the field camp." {n}She is quiet.{/n} "I stood outside the walls with a Crows\' squire and listened to a city grieve for me. I do not recommend it either. It is very hard to know what to do with one\'s hands."',
            c("Continue", "why")),
        ga("why", '"So. Here I am." {n}She squares her shoulders, knight to Commander.{/n} "I have no lands, no crown and no enemies. I have an old sword, a green surcoat, and a name I first wore in the war camp. And I have discovered that I still stand in the square at the hour of petitions, every morning, waiting for somebody to need a ruling. Nobody does." {n}She meets your eyes.{/n} "Mendev buried a queen. I would like, just once, to be a face in your crowd that you look for."',
            c("Continue", "alone", requires=(ALONE, REPLIED)),
            c("Continue", "alone_silent", requires=(ALONE,), forbids=(REPLIED, LATE_FOUND)),
            c("Continue", "alone_found", requires=(LATE_FOUND, CORTEGE_PAID)),
            c("Continue", "refused", requires=(OFFER_REFUSED,), forbids=(ALONE,)),
            c("Continue", "romance", requires=(ROMANCE,), forbids=(ALONE, OFFER_REFUSED)),
            c("Continue", "end", forbids=(ALONE, OFFER_REFUSED, ROMANCE)),
            c("Continue", "alone_found_talked", requires=(LATE_FOUND,), forbids=(CORTEGE_PAID,))),
        ga("alone_found_talked", '{n}Her gaze hardens, just perceptibly.{/n} "You did not come to me at Iz. You found me later on a bier in Drezen, with the lid on the floor, and you talked my own sergeant out of the doorway to do it." {n}A beat.{/n} "I have not decided whether to forgive you the first part. The second I cannot hold against you; he is a hard man to move, and I should like to know how you did it. I can remember that I waited in the rubble and still be glad you came to the chapel."',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("alone", '{n}Her gaze hardens, just perceptibly.{/n} "You did not come to me at Iz. I have forgiven you that; I wrote so, and I meant it." {n}A beat.{/n} "I watched for the courier. When your answer came, I read it twice before I let the sergeant take the seal."',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("alone_found", '{n}Her gaze hardens, just perceptibly.{/n} "You did not come to me at Iz. You found me later on a bier in Drezen, with the lid on the floor and a bribed sergeant at the door." {n}A beat.{/n} "I have not decided whether to forgive you the first part. I find I cannot hold the second against you at all. I can remember that I waited in the rubble and still be glad you came to the chapel."',
            c("Continue", "romance", requires=(ROMANCE,)),
            c("Continue", "end", forbids=(ROMANCE,))),
        ga("alone_silent",'{n}Her gaze hardens, just perceptibly.{/n} "You did not come to me at Iz. I have forgiven you that; I wrote so, and I meant it." {n}A beat.{/n} "You did not write back. I kept telling myself silence was prudence. Letters are read. I still watched for the courier, and I was angry with myself for it."',
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
    '{n}Irabeth does not look up from the duty roster.{/n} "You did not hear her last command. You will not know what she looked like when she gave it to me. So you will not know what she looked like when she gave me that order." {n}Her pen has stopped.{/n} "Lying in the rubble with that sorcery in her, alone but for me and two old Crows, telling us in her parade-ground voice that the Queen had fallen and a knight called Kitrane needed carrying. She did it herself, Commander. Nobody offered her anything. She offered it to herself." {n}Now she looks up.{/n} "I have never been so proud of anyone, or so angry. I have not decided which of those I owe you."',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Irabeth", P + "react.irabeth.after_death", (RETURNED, CARRIED_CROWS, "irabeth.trickster.returned"),
    '''{n}Irabeth has the duty roster open and has not written on it since you came in.{/n} "The old sergeant of the Green Crows came to see me last night. Drunk, which he never is. He told me who is buying boots in the market." {n}Her voice is very even.{/n} "I was dead when she fell, Commander. She called my name with her last command in her mouth, he says, and two old men came instead." {n}She closes the roster.{/n} "We both came back. Neither of us came back as what we were. I shall not be telling her that I know. I think she would rather be one secret I do not carry."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **{**IRABETH_GUARD, "forbids": IRABETH_GUARD["forbids"] + (CROWS_DREZEN,)}))

SCENES.append(reaction("Irabeth", P + "react.irabeth.learned", (RETURNED, CROWS_DREZEN),
    '''{n}Irabeth has the duty roster open and has not written on it since you came in.{/n} "The old sergeant of the Green Crows came to see me last night. Drunk, which he never is. He told me who is buying boots in the market." {n}Her voice is very even.{/n} "I was holding Drezen when she fell. She did not send for me; she sent for two old men and a cart." {n}She closes the roster.{/n} "I have been angry about it all morning, Commander. I think it was the kindest thing she ever did to me. I shall not be telling her either."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Irabeth", P + "react.irabeth.queen_night", (P + "alive.committed",),
    """{n}Irabeth is at the duty roster, and she does not look up.{/n} "The Eagle Watch had the postern last night. A knight of the Green Crows went out of the citadel after the ninth bell and came back in before first light, and when the sentry stopped her she told him his buckle was a disgrace to the order and he ought to be ashamed of it." {n}Her pen moves, very precisely.{/n} "He was. He still is. I have had his buckle seen to and his name moved to the day roster, where he will not see her again." {n}Now she looks up.{/n} "I serve the Queen, Commander. Whoever she is after the ninth bell is not mine to report. See that it never becomes mine.\"""",
    answer_list=IRABETH_HUB, relationship=REL, entry='"Anything to report, knight?"', chapter=5, last=5, delay=12,
    portrait="Irabeth", **IRABETH_GUARD))

SCENES.append(reaction("Irabeth", P + "react.irabeth.chapel", (RETURNED, LATE_FOUND),
    '''{n}Irabeth has the duty roster open and has not written on it since you came in.{/n} "The old sergeant of the Green Crows came to see me last night. Drunk, which he never is. He told me who is buying boots in the market, and who he let into the chapel the night before the lead went on." {n}Her voice is very even.{/n} "She lay on that bier, Commander, and nobody thought to look under the linen but you. I would have stood guard at that coffin and seen a dead woman." {n}She closes the roster.{/n} "I shall not be telling her that I know. I shall be standing a little straighter when I pass the curio stall. She will notice. She notices everything."''',
    answer_list=IRABETH_HUB, relationship=REL, entry='"You\'ve been quiet, knight."', chapter=5, last=5, delay=24,
    portrait="Irabeth", **{**IRABETH_GUARD, "forbids": IRABETH_GUARD["forbids"] + (CARRIED_IRABETH, CARRIED_CROWS)}))

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
    '{n}The Inquisitor\'s eyes are still red, and he has not shaved.{/n} "There is a knight of some minor order who stands at the chapel door at the ninth bell, Commander, while I pray for Her Majesty. In a grey hood. Every night." {n}His hands tighten on his ledger.{/n} "I have not called her forward. A man at his prayers should not be spied upon, and neither, I think, should a knight at hers." {n}A long breath.{/n} "But I am an Inquisitor. I notice. Tell your Crows, if they are yours, that the chapel has a front pew, and nobody is using it."',
    answer_list=HULRUN_HUB, relationship=REL, forbids=("hulrun.dead", "hulrun.away_c5", EULOGY_SIGN, CLOSED),
    entry='"Inquisitor. You look tired."', chapter=5, last=5, delay=48, portrait=""))

SCENES.append(reaction("Hulrun", P + "react.hulrun.ledger", (RETURNED, EULOGY_SIGN),
    '{n}Hulrun opens his ledger to the Crows\' muster.{/n} "You named the Green Crows. They carried the wounded out of Iz. I have begun with their muster." {n}His voice is very low.{/n} "And now there is a knight of a minor order at my chapel door who stands exactly as she stood, and has her hands. I have seen enough to ask questions. I have not asked them in front of the chapel." {n}He shuts the ledger.{/n} "While the war lasts, the soldiers need their Queen\'s courage. Afterwards you will tell me whose sorcery you used, and whose body went into that box. Do not expect a demon\'s assurances to suffice."',
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
            P + "react.hulrun.door", P + "react.hulrun.ledger", P + "react.daeran.cousin", P + "react.king",
            P + "react.irabeth.chapel", P + "react.irabeth.queen_night"):
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
    p("{n}She grew old without a third cup of the church's elixir. She complained about her knees and made the Crows inspect each new grey hair before drill.{/n}",
      requires=(FOREVER,)),
    p('''{n}Whether she would ever take the crown back she did not say, and the Commander never asked. Some years she seemed close to it. Most years she was drilling squires in the mud behind a tent that leaked on the left.{/n}''',
      forbids=(CROWN, FOREVER)),
    p('''{n}The tear in her voice never mended. She stopped making speeches. When she had something to say to a crowd, she said it to one person in it, and let them pass it on.{/n}''',
      requires=(RENT,)),
    p("{n}She had forgiven the Commander for failing to reach her at Iz. The memory of waiting in the rubble remained. On the anniversary she knelt in the chapel before first light, then went to the Crows' muster.{/n}",
      requires=(ALONE,), forbids=(LATE_FOUND,)),
    p('{n}She never blamed the Commander for reaching her in the chapel, though their failure to reach her battle still hurt. On the anniversary she woke before first light and listened for the bells. When the Commander stirred beside her, she took their hand.{/n}',
      requires=(LATE_FOUND,)),
    p('{n}The Green Crows grew, slowly. The girl from the eel stall was knighted in the third year after the war, by a knight of the order in plain armour, in a field, with nobody watching but a mule. The girl held the sword steady through the oath.{/n}',
      requires=(P + "kitrane.squire_sworn",)),
    p('''{n}At the eastern ford she had refused an order of the Commander's, and six people hanged anyway. She never pretended afterwards that she had forgiven it. Every year on that day she and the Commander walked down to a grave in the lower town of Drezen with a tallow candle, and stood there together, and neither of them ever said it was enough.{/n}''',
      requires=(REFUSED_ORDER, P + "ride.answered")),
    p('''{n}At the eastern ford she had refused an order of the Commander's, and six people hanged anyway, and the Commander never went down to the tallow-seller's. She served to the end all the same. She never once spoke of the ford again, and never once, afterwards, rode where the Commander could order her to stand beside a rope.{/n}''',
      requires=(REFUSED_ORDER,), forbids=(P + "ride.answered",)),
    p("{n}She kept the Crows' drill at first light. Some mornings a passing soldier saluted her; she returned it and went back to her sword. By the end of the exercise the sergeant usually had an objection.{/n}",
      requires=(DRILL,)),
    p("{n}Hulrun kept his questions out of the chapel while the war lasted. Afterwards he came to the Crows' tent with his ledger and sat on the mule's feed-box. He asked whose name belonged on the coffin. Kitrane answered him herself. He took the answer back to his prayers and his office.{/n}",
      requires=(P + "kitrane.hulrun_seen",), forbids=("hulrun.dead",)),
    p('''{n}On Oathdays she played dice in the Fool King's tavern and lost, loudly, to a drunkard in a paper crown, and was, the tavern agreed, the worst knight the kingdom of the tavern had ever sausaged.{/n}''',
      requires=(P + "kitrane.king_seen",)),
    p("{n}A later treatise credited an unknown knight of the Green Crows with proposing the riverbed approach. Kitrane read the chapter to the Crows and corrected the distances in the margin. She kept the author's letter inside the cover.{/n}",
      requires=(P + "kitrane.war_table", P + "kitrane.table_credited")),
    p("{n}The proposal went into the histories under the Commander's name. She read every one of them, and corrected the distances in the margins in a firm old-fashioned hand, and never once asked for the credit.{/n}",
      requires=(P + "kitrane.war_table",), forbids=(P + "kitrane.table_credited",)),
    p('''{n}She kept the letter she had once hidden in a wall in the lid of her armour chest, with Sir Anselm's broadsheet, and never read it again. Once, very late, she told the Commander what it said, word for word, and then laughed at the Queen who wrote it.{/n}''',
      requires=(P + "kitrane.letter_returned",)),
    p('''{n}The letter she had once hidden in a wall stayed where the Commander kept it. Every few years she asked to read it again, and every time she laughed at the Queen who wrote it, and every time she kept the Commander's hand for a while afterwards.{/n}''',
      requires=(P + "kitrane.letter_kept",)),
)

epilogue("kitrane", "Kitrane", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan. Mendev mourned her for a year and a day.{/n}
{n}A knight of the Green Crows named Kitrane, of no lands, no crown and no enemies, lived a great deal longer. She followed the Commander to the end of the war as a knight of the Crows, and on its last night she kept the walls of Drezen among the soldiers who had not been sent to Threshold, in the crowd, where she had asked to be; and the Commander, whatever else became of the world, never once failed to look for her there.{/n}''',
         requires=(RETURNED, COMMITTED), forbids=(CLOSED,), paragraphs=KITRANE_PARAGRAPHS)

epilogue("sworn", "Kitrane, sworn", "{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan.{/n}\n\n{n}Kitrane of the Green Crows kept her oath to the Commander through the last campaign. Her reports arrived on time; her objections were rarely welcome and usually worth hearing. In the market she still haggled over boots, laughed with her fellow knights, and joined the Crows' drill. After the war she requested release in writing. The Commander granted it, and she rode out of Drezen with the Crows' mule walking behind her.{/n}",
         requires=(RETURNED, SWORN), forbids=(COMMITTED, CLOSED), paragraphs=KITRANE_PARAGRAPHS)

epilogue("late", "Kitrane, late", "{n}The war ended before Kitrane of the Green Crows had settled every question between herself and the Commander. Her sword remained at the Crows' muster; her name remained off the royal roll.{/n}",
         requires=(P + "late_committed",), forbids=(COMMITTED, SWORN, CLOSED), paragraphs=KITRANE_PARAGRAPHS)

epilogue("widow", "Kitrane, after", '''{n}Queen Galfrey of Mendev died at Iz and was buried with honours in Nerosyan.{/n}
{n}The Commander of the Fifth Crusade did not come back from Threshold. A knight of the Green Crows named Kitrane kept the walls of Drezen that night, as she had asked to, and was there when the news came in the morning. She did not weep where anyone could see. She walked down to the chapel, and stood at the back, as she had once stood for her own vigil, and stayed until the candles went out.{/n}
{n}She lived a long time after, as nobody in particular, and grew old without a third cup of the church's elixir. Every year on the day of Threshold she went up onto the walls of Drezen at dusk and stood in the crowd, and looked, out of old habit, for a face that was not there.{/n}''',
         requires=(RETURNED, COMMITTED, "sacrifice"), forbids=("trickster.commander_back", "lastcall.active", CLOSED), survived=False)

epilogue("alive", "The Queen and the knight", '{n}Queen Galfrey returned from the Worldwound alive and still crowned. She ruled Mendev with the same exacting hand. The Commander learned to put plans on her desk before setting them in motion, and to expect objections in the margins.{/n}\n\n{n}People recognized the knight who left the citadel after the ninth bell. The sentries learned to record the green surcoat and let the woman answer to it. By morning the Queen was back at her dispatches. The Commander still received objections in the margins, and sometimes an invitation folded beneath them.{/n}',
         requires=(FINAL, COMMITTED), forbids=(DEAD, RETURNED, CLOSED, "iomedae.trickster.buried_alive"))

# R6 (iomedae_trickster): in the world where the Commander walked out of the Wound and stayed buried, the Queen's general is
# a grave; the knight finds the stranger instead. Appended sibling of "alive" (which Forbids that world).
epilogue("alive_buried", "The Queen and the stranger", '''{n}Queen Galfrey of Mendev did not die at Iz. She came home from the Worldwound with her crown on her head, and ruled, and was severe and exact with the world. The Commander of the Fifth Crusade did not come home at all. Drezen buried an empty coffin, and the Queen stood at the graveside as a queen stands at the grave of her best general, and said the words herself, and did not weep where anyone could see.{/n}
{n}On certain nights a knight of the Green Crows with loose hair and an old sword rode out of Nerosyan alone and came back before first light, and nobody asked where. Wherever the stranger was that year, on a road, at a waystation, behind somebody else's barricade, Kitrane found it. She said it was the one place in the world where neither of them had to be anybody.{/n}''',
         requires=(FINAL, COMMITTED, "iomedae.trickster.buried_alive"), forbids=(DEAD, RETURNED, CLOSED))

epilogue("native", "The Queen and the Trickster", '''{n}Queen Galfrey of Mendev did not die at Iz. Shortly after the war she laid down the crown, as the chronicles record, and left Nerosyan to spend the rest of her long life with the one who had shown her there was more to life than duty; and Mendev, which had expected to bury her, did not quite know what to do with her alive and uncrowned.{/n}
{n}What she and the Commander were to each other was her own affair, and she made sure everyone understood it. She was severe and exact with the world to the end of her days, and with one person she was neither.{/n}''',
         requires=(FINISHED, FINAL), forbids=(DEAD, RETURNED, CLOSED), paragraphs=(
             p('''{n}On the rare evenings she could be persuaded into the Fool King's tavern, she held her cup like somebody who was used to being watched, and spilled some early, on purpose, so that everybody could stop waiting for it. The Commander's strange court of jesters and drunkards took her in without a word, the way it took in everyone, and she found, to her lasting surprise, that she liked it there.{/n}''',
               requires=("fool_king.available",), forbids=("fool_king.gone",)),
             p('''{n}The Commander's strange court had no king in it by then, only a tavern bench where one had once sat, and she sat on it now and then, as if keeping it warm for somebody.{/n}''',
               requires=("fool_king.gone",)),
         ))

epilogue("queen", "The Queen", '{n}Queen Galfrey died at Iz with her Commander beside her. The Commander had offered another name, then withdrawn it and told her to die as Queen. Her last words admitted that she might have accepted. She was buried in Nerosyan in her own armour, with the honours of Mendev.{/n}\n\n{n}The Commander did not speak at her vigil. Asked afterwards whether anything could have been done, they said that there had been a chance, and that they had let it go.{/n}',
         requires=(LET_DIE,), forbids=(RETURNED, LEFT_EARLY))

epilogue("queen_bier", "The Queen", '{n}Galfrey fell at Iz before the Commander reached her. Later they found her on a bier in Drezen, with the enemy\'s sorcery still burning beneath the bandage. She asked why she should wake under another name. The Commander told her to rest. The lead seal went on at first light, and her knights took the coffin home to Nerosyan.{/n}\n\n{n}The Crows\' sergeant never spoke to the Commander again. When someone asked what had happened in the chapel, he said, "They told her to rest. I sealed the lid."{/n}',
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
    payload["PermanentEtudes"] = sorted(set(payload.get("PermanentEtudes", [])) | {FINISHED, KC_KEPT})   # MANU is latched in Iz (trickster_world LATCHES), not a permanent etude


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'galfrey.trickster.iz.eulogy',
    'galfrey.trickster.iz.road',
    'galfrey.trickster.return.kitrane',
    'galfrey.trickster.return.kitrane_scarred',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
# eng8-q8d: the road is the one rest delivery; the sergeant conducts the
# vigil and the arrival in person. Appended twins preserve every old node.
def _eng8_sergeant_visits():
    import copy
    unit = '8a23e71893cf8ab428e7ebd64b10ad27'
    for suffix in ('iz.eulogy', 'return.kitrane', 'return.kitrane_scarred'):
        host = next(s for s in SCENES if s['Id'] == P + suffix)
        host.pop('Kind', None)
        host.update(Remote=False, ContactUnit=unit, InteractionHub='galfrey.presence.sergeant',
                    Areas=[DREZEN], Entry='[Follow the Crows\' sergeant.]')
        if suffix.startswith('return.'):
            host['DelayHours'] = 36 if suffix.endswith('_scarred') else 24
        twin = copy.deepcopy(host)
        twin['Id'] += '_stall'
        twin['InteractionHub'] = 'galfrey.presence.sergeant_stall'
        twin['Requires'].append('galfrey.presence.sergeant.failed')
        twin['Forbids'].append(host['Id'])
        host['Forbids'].extend([twin['Id'], 'galfrey.presence.sergeant.failed'])
        SCENES.append(twin)
    for sid in ('react.daeran.cousin', 'react.king'):
        retired = next(s for s in SCENES if s['Id'] == P + sid)
        retired['Forbids'].append('trickster.ever')

_eng8_sergeant_visits()
# end eng8-q8d


# Reviewed route-local history and payment repairs. Shared life/entitlement
# readers and native reconciliation remain owned by the integration engine.
DERIVED["trickster.secret.galfrey_eulogy.known.irabeth"] = [
    [CARRIED_IRABETH], [P + "react.irabeth.learned"],
    [P + "react.irabeth.after_death"], [P + "react.irabeth.chapel"],
]


def _reviewed_history():
    for host in SCENES:
        sid = host["Id"].removesuffix("_stall")
        nodes = {node["Id"]: node for node in host["Nodes"]}
        for node in host["Nodes"]:
            for choice in node["Choices"]:
                if LET_DIE in choice.get("Set", []):
                    choice["Set"].append(P + "offer_withdrawn")
        if sid == P + "ch3.standing_orders":
            nodes["why"]["Choices"][0].update(
                Text='[Pay 100 Finances] "For a cart, a cloak, and a surgeon who does not know her face."',
                Crusade={"Resource": "Finances", "Amount": -100})
            nodes["why"]["Choices"][0]["Set"].append(P + "standing_orders.paid")
            nodes["why"]["Choices"][1].update(
                Text='"Keep a cart and a cloak with your wounded. If she asks, carry her out with them."', Next="take_supplies")
            host["Nodes"].append(n("take_supplies", "Crows' sergeant", '{n}He glances at the carts beyond the tent.{/n} "We can keep one with the wounded. The cloak is mine. If she asks, it will be done." {n}He picks up his whetstone.{/n} "Anselm will want to know why I am counting blankets. I shall tell him the mule ate one."'))
        elif sid == P + "iz.offer":
            for choice in nodes["last"]["Choices"]:
                choice["Set"].append(COFFIN)
            nodes["obey"]["Choices"][0]["Forbids"].append(SEELAH_BED)
            heard = dict(nodes["obey"]["Choices"][0])
            heard.update(Requires=[SEELAH_BED], Forbids=[],
                Set=[*heard["Set"], "trickster.secret.galfrey_eulogy.known.seelah"])
            nodes["obey"]["Choices"].append(heard)
            nodes["for_mendev"]["Text"] = '"For Mendev." {n}She turns her face away, then back.{/n} "If you need a Queen, look at me. You have no use for this one now." {n}Her grip tightens on the cloak.{/n} "I accepted the elixir. I accepted the crown. Do not tell me those choices were someone else\'s. If you want me to take this chance, ask for me. Here, now. You have commanded enough for one day."'
        elif sid == P + "iz.cortege":
            nodes["surgeon"]["Choices"][0].update(Text='[Diplomacy DC 24] "She introduced herself to me as Kitrane of the Green Crows. Let me see whether she can still hear that name."', Requires=[MET])
            unmet = dict(nodes["surgeon"]["Choices"][0])
            unmet.update(Text='[Diplomacy DC 24] "You guarded her at Iz. Let me see the wound and speak to the men who carried her. I may yet do more than sit a vigil."', Requires=[], Forbids=[MET])
            nodes["surgeon"]["Choices"].append(unmet)
        elif sid in (P + "react.seelah.majesty",):
            nodes["start"]["Choices"][0]["Set"].append("trickster.secret.galfrey_eulogy.known.seelah")
        elif sid in (P + "epilogue.kitrane", P + "epilogue.sworn", P + "epilogue.late"):
            # Each page has a private paragraph list; never alter shared guards.
            import copy
            paras = copy.deepcopy(nodes["page"]["Paragraphs"])
            paras[9]["Requires"].append(COMMITTED)
            paras.append(p("{n}On the anniversary of the night on the bier, Kitrane rose before the first bell and checked the Crows' muster. Then she went to the chapel alone. The sergeant left a place beside him and asked no questions.{/n}", requires=(LATE_FOUND,), forbids=(COMMITTED,)))
            if sid != P + "epilogue.kitrane":
                paras.extend([
                    p('{n}She rode with the Commander when the Crows were called, and found company among the knights when they were not. Neither mistook that loyalty for a promise she had declined to make.{/n}', requires=(P + "answer_ally",)),
                    p("{n}She had answered the Commander's courtship with a plain refusal. They kept their places in the crusade, and she never had to answer the question again.{/n}", requires=(P + "answer_refused",)),
                ])
            if sid == P + "epilogue.late":
                paras.append(p("{n}After Threshold she stood beside the Commander on Drezen's wall and asked whether there was room for another face in their crowd. The question remained hers to finish.{/n}", forbids=(P + "answer_ally", P + "answer_refused")))
            nodes["page"]["Paragraphs"] = paras
        elif sid == P + "epilogue.alive":
            nodes["page"]["Paragraphs"] = [
                p("{n}She had refused the Commander once, distrustful of their powers and decisions. She reconsidered after orders kept and objections answered. Neither conversation was forgotten.{/n}", requires=(NATIVE_REFUSED,)),
                p("{n}Their courtship began over dispatches, with a plan disclosed before dawn. She made the Commander earn her trust before she invited them anywhere less public.{/n}", forbids=(NATIVE_REFUSED,)),
            ]


_reviewed_history()

# Round 2: authored situations and history receipts. The invitation and survival
# requirements are unchanged; these readers distinguish what actually happened.
SERVICE = P + "native_incognito_service"
JOINED = P + "native_joined_march"
BINDINGS["SeenCues"][JOINED] = ["0c2f550f8d311e64a8c80ab23859a25f"]  # Tour_End_Queen/Cue_0009 starts GalfreyWithUs
DERIVED[SERVICE] = [[JOINED], [MET]]


def history_variant(host, nid, flag, alternate, suffix):
    """Append a text variant and selector; keep old nodes and answer indices.

    The original node is the flag-present history. Call only on non-entry nodes.
    Conversation variants use nodes, never conditional paragraphs.
    """
    import copy
    original = next(node for node in host["Nodes"] if node["Id"] == nid)
    variant = copy.deepcopy(original)
    variant.update(Id=nid + "." + suffix, Text=alternate)
    selector = nid + ".select." + suffix
    for node in host["Nodes"]:
        for choice in node["Choices"]:
            if choice.get("Next") == nid:
                choice["Next"] = selector
            for branch in ("Success", "Failure"):
                if choice.get("Check", {}).get(branch) == nid:
                    choice["Check"][branch] = selector
    host["Nodes"].extend([variant, nar(selector, "{n}There is a brief silence.{/n}",
        c("Continue", nid, requires=(flag,)),
        c("Continue", variant["Id"], forbids=(flag,)))])


def _round2_history():
    RELATIONSHIP["Description"] = ("Queen Galfrey has spent a century ruling Mendev and fighting its war. "
        "Kitrane of the Green Crows is a name she can choose for herself. Whether she keeps it, and whom she invites "
        "beside her, remains hers to decide.")
    for host in SCENES:
        sid = host["Id"].removesuffix("_stall")
        nodes = {node["Id"]: node for node in host["Nodes"]}
        if sid == E:
            nodes["ask"]["Text"] = ('{n}She takes a signed recommendation from beneath her cloak. A line below the military commendation requires a royal envoy at your councils. She strikes it out and folds the sheet.{/n} '
                '"My recommendation stands. That condition does not. If I visit, you shall hear the reason from me, not from a clerk." '
                '{n}She keeps the paper.{/n} "Now. You did not come to ask after my boots. Out with it, Commander."')
        elif sid == CROWS:
            host["Entry"] = '"Will you ride with the minor orders again, Your Majesty?"'
            nodes["start"]["Text"] = ('{n}Galfrey lays a signed recommendation on the table. Beneath the military commendation, a line requires a royal envoy at your councils. She crosses it out herself.{/n} '
                '"You have my recommendation. I shall decide when I visit you." {n}She folds the sheet and keeps it. Beyond the square the Fane\'s barrier glimmers.{/n} '
                '"As for riding among the minor orders: there is a name for that. Kitrane of the Green Crows."')
            history_variant(host, "first", SERVICE,
                '"I considered that disguise before the march. Plain armour, a minor order, an old friend of yours. I remained in Nerosyan instead." '
                '{n}Her finger rests on the folded recommendation.{/n} "Now you know her name. What would you ask of her?"', "new_name")
            history_variant(host, "liked", SERVICE,
                '"You like the sound of her." {n}Her mouth twitches.{/n} "So do I. A knight can finish her supper before someone brings her a petition. '
                'I shall have to try it." {n}She looks toward the barrier.{/n} "After the Fane, Commander. I have not forgotten what brought me here."', "new_name")
        elif sid == BRIEFED_ID:
            history_variant(host, "why", SERVICE,
                '{n}He lays the sword across his knees.{/n} "She spoke to us after her audience in Drezen. Kitrane, she said. A knight of ours, if she ever needed the name." '
                '{n}He studies you.{/n} "You want us ready to carry her among the wounded. She would have to ask. I will not steal her out from under her own command."', "drezen")
        elif sid == OFFER:
            # She supplies the unwitnessed name before either wound check uses it.
            old_watch = nodes["watch"]["Text"]
            history_variant(host, "watch", MET,
                '"If you have come to ask me to fight again, look at the breastplate." {n}Her fingers scrape the broken metal.{/n} '
                '"I had another name ready for plain armour. Kitrane, a knight of the Green Crows. A poor jest now." '
                '{n}She watches you look from her face to the wound.{/n}\n' + old_watch, "name_supplied")
        elif sid == P + "iz.alone":
            history_variant(host, "letter2", E_MOOTED,
                '"I remembered the name we discussed before the Fane. Kitrane. In the rubble I found I still wanted the life I had considered then. '
                'You were not there to offer it. The sergeant had your standing orders and a cart; he knelt and waited for mine. I gave them. '
                'I offered the chance to myself. It was a lonely business."', "later_seed")
            nodes["letter3"]["Text"] = ('"The cart and cloak were ready. The Crows\' surgeon worked over me while the others hammered the coffin shut. '
                'It has loosened, but not let go. I think it is waiting to hear the Queen\'s death proclaimed where she was loved. '
                'I cannot arrange that from a wounded man\'s cart. You can.\n'
                '"If this reaches you, Commander, I am alive. If it does not, I tried.\n"Kitrane."')
            history_variant(host, "letter3", P + "standing_orders.paid",
                '"There was no purse for a hired surgeon. The sergeant gave me his cloak and the cart kept for the wounded. '
                'Their own surgeon worked over me while they hammered the coffin shut. They had other wounded waiting. '
                'It has loosened, but not let go. I think it needs to hear the Queen\'s death proclaimed where she was loved. '
                'I cannot arrange that from this cart. You can.\n"If this reaches you, I am alive. If not, I tried.\n"Kitrane."', "crows_supplies")
        elif sid == P + "iz.cortege":
            nodes["start"]["Text"] = nodes["start"]["Text"].replace("three days out of Iz", "after the slow march from Iz")
            nodes["choose"]["Text"] = nodes["choose"]["Text"].replace("three days dead", "carried from Iz as a corpse")
            history_variant(host, "flare_told", SERVICE,
                '{n}The light brightens. At the chapel door the sergeant grips the frame.{/n} "Kitrane. She had a name ready before the march, '
                'if she ever rode with us in plain armour. Never used it. Told Anselm he\'d have to remember not to salute." '
                '{n}He comes closer to the bier.{/n} "Try it, Commander. She chose it herself." '
                '{n}It is a name, an old man\'s grief, and a gamble. You have nothing surer.{/n}', "unworn")
            history_variant(host, "wake", SERVICE,
                '{n}Her lips move before her eyes open. At last they find you.{/n} "Commander. You did not come to me at Iz." '
                '{n}Her fingers move on the sword.{/n} "Kitrane. I meant to wear that name with the Crows. Never thought it would have to get me out of a coffin. '
                'I am tired. Tell me why I should try."', "unworn")
        elif sid.startswith(P + "return.kitrane"):
            history_variant(host, "why", SERVICE,
                '"So. Here I am." {n}She squares her shoulders.{/n} "An old sword, a green surcoat, and the name I chose for the escape. '
                'I still stand in the square at the hour of petitions. Nobody brings one." {n}She meets your eyes.{/n} '
                '"Mendev buried its Queen. I should like you to look for me when you come through the crowd."', "chosen_late")
            nodes["romance"]["Text"] = ('{n}She lowers her voice.{/n} "We still have a conversation to finish. I kept finding a military reason to postpone it." '
                '{n}Her hand closes briefly on your sleeve.{/n} "Come to the market when your dispatches are done. I shall not send a herald."')
            nodes["end"]["Text"] = ('"The curio stall, where the crowd is thickest. I can watch for you from there." '
                '{n}She turns back toward the sergeant.{/n} "First I must see the Crows. They carried my command, and Anselm, and me. '
                'The regents have the Queen\'s seal now. They will be issuing orders of their own."')
        elif sid == P + "iz.road":
            # This optional rest delivery may arrive after the mandatory vigil.
            nodes["start"]["Text"] = ('{n}During a halt, the road out of Iz returns to you: the slow column, the furled royal banner, '
                'the sealed coffin, and three carts behind it a wounded Crow under a green cloak. The march gave you little time to speak.{/n}\n' + nodes["start"]["Text"])
        elif sid == P + "react.irabeth.queen_night":
            nodes["start"]["Text"] = ('{n}Irabeth puts the postern guard\'s report in your hand.{/n} "A Crow left after the ninth bell. The watch wanted to know whether to escort her." '
                '{n}She taps the blank order beneath it.{/n} "I left that decision to the knight. If you need the postern held open, tell the watch before they bar it. '
                'I will not have a sentry punished for failing to guess."')
        elif sid in (P + "react.irabeth.drill", P + "react.irabeth.drill_alone"):
            nodes["start"]["Text"] = ('{n}Irabeth spreads a patrol map between you.{/n} "The Crows were drilling when my column passed. '
                'Their tent is beside the route to the eastern ford. I asked Kitrane to watch that approach while we change the pickets." '
                '{n}She marks the place.{/n} "She agreed, and told me the younger squires remain in camp. I know better than to argue with her dispositions."')
        elif sid in (P + "epilogue.kitrane", P + "epilogue.sworn", P + "epilogue.late"):
            paras = nodes["page"]["Paragraphs"]
            for para in paras:
                if P + "kitrane.king_seen" in para["Requires"]:
                    para["Forbids"].append("fool_king.gone")
            paras.append(p('{n}When Thaberdine left Drezen, Kitrane kept the dice he had accused her of loading. On Oathdays she still told the Crows how he had knighted her with a sausage; the sergeant demanded to know where that put him in the muster.{/n}',
                requires=(P + "kitrane.king_seen", "fool_king.gone")))
            if sid == P + "epilogue.kitrane":
                nodes["page"]["Text"] = ('{n}Mendev mourned Galfrey after Iz. The Green Crows mustered a knight named Kitrane. '
                    'She kept Drezen\'s walls during the march to Threshold and came down to meet the Commander on their return, still in plain armour. '
                    'She kissed them before the sergeant could begin his report.{/n}')
                paras.append(p('{n}After a patrol she came back muddy and impatient, sent the muster to the Commander\'s desk, and went herself to their chamber. '
                    'She still corrected their hands on a difficult buckle. They learned to leave her evenings clear when the Crows were in camp.{/n}', requires=(TENT,)))
        elif sid == P + "epilogue.widow":
            nodes["page"]["Text"] = ('{n}The Commander did not return from Threshold. Kitrane received the news on Drezen\'s walls. '
                'She went to the chapel and stayed until the candles burned down. At the next muster she answered her name and took her place.{/n}')
            nodes["page"]["Paragraphs"] = [
                p('{n}She rode to Nerosyan as she had decided. Anselm\'s daughter received her father for burial; the regents received their Queen and an account of the coffin. '
                    'Galfrey answered the inquiry herself. She ruled again, refused the next elixir, and eventually abdicated. The Commander\'s place at her table remained empty.{/n}', requires=(CROWN,)),
                p('{n}She remained Kitrane. Anselm\'s daughter received his sword-belt and a purse every Iz anniversary. '
                    'The knight who sent them grew old in the Crows\' service. Each year after the Threshold muster she returned to Drezen\'s wall and stood there until dark.{/n}', requires=(FOREVER,)),
                p('{n}She had not settled the crown\'s future. For now she kept the Crows\' watch and Anselm\'s sword. '
                    'When she returned from patrol, she still looked first toward the Commander\'s window.{/n}', forbids=(CROWN, FOREVER)),
                p('{n}The rent in her voice remained. She gave the muster quietly, close enough for the sergeant to hear.{/n}', requires=(RENT,)),
                p('{n}On the ford anniversary she went to Tobin\'s grave herself. The Commander\'s death had not undone the order or the six hangings.{/n}', requires=(REFUSED_ORDER,)),
            ]
        elif sid == P + "epilogue.alive":
            nodes["page"]["Text"] = ('{n}Galfrey returned from Threshold still crowned. Plans reached her desk before they reached the quartermaster; her objections still came back in the margin. '
                'When the last dispatch was sealed she dismissed the clerks, went to find the Commander, and closed the door herself. '
                'By morning the next orders lay between them at breakfast.{/n}')
        elif sid == P + "epilogue.native":
            nodes["page"]["Text"] = ('{n}After the war Galfrey laid down the crown and left Nerosyan to share her life with the Commander. '
                'She still corrected their orders when they asked her advice. When she returned from a ride, she looked for them before putting away her sword; '
                'on quiet evenings they learned to leave the door barred. Mendev received her occasional letters in the same firm hand.{/n}')


_round2_history()



def _round3_rescue():
    # Authored Trickster intervention, not a native property of either Iz spell.
    # No new checks, costs, gates or effects: READ still buys the earlier release.
    for host in SCENES:
        nodes = {node["Id"]: node for node in host["Nodes"]}
        sid = host["Id"]
        if sid == BRIEFED_ID:
            setup = (' {n}You turn the sergeant\'s cloak inside out. For a moment its shadow wears a crown; '
                'then you fold that shadow into the lining. He drops the whetstone.{/n} '
                '"What the hell have you put in my cloak?" {n}You show him how to wrap the fallen Queen in it, '
                'turn the lining outward over her discarded armour, and carry the armour in the royal coffin. '
                'The trick leaves the dying Queen with the crown and carries the wounded knight away. '
                'Without you there to separate them cleanly, the Crows must finish the division at her vigil: '
                'name the Queen dead before the coffin, then call Kitrane out among the living. '
                'He makes you repeat it, and tries the folds himself.{/n} '
                '"Only if she commands it. I will not bury her while she can still give me an order."')
            for key in ("take", "take_supplies"):
                nodes[key]["Text"] += setup
        elif sid == OFFER:
            nodes["read"]["Text"] = ('{n}You lift the broken rim of her breastplate and lay its crowned crest '
                'against the bloodied cloak. Your shadow moves before your hand does. A second outline of Galfrey '
                'lies beneath the armour, dying; the woman beside it draws a sharp breath.{/n} '
                '{n}When you address the Queen, the dark light leaps toward the crest. When you call Kitrane, '
                'it stretches between the two outlines. You catch the single black strand joining them '
                'and wind it around the crest. Her fingers unclench. The armour must go into the royal coffin; '
                'you keep the strand pinned there until the knights lift it away.{/n}')
            nodes["sight"]["Text"] = ('{n}The doubled shadows have seams you can see as plainly as a loose stitch. '
                'The sorcery still grips the dying Queen beneath the crest. You have pulled the knight out '
                'of its reach; now the Crows must carry the two apart.{/n}')
            nodes["blind"]["Text"] = ('{n}You lay the crowned crest against the cloak. Your shadow reaches '
                'under the armour before your hand does, and another outline of Galfrey lies there. '
                'The dark light spreads between them. You cannot find where to divide it. '
                'Her breath catches; you stop before you tear away what remains of her soul.{/n}')
            nodes["offer"]["Choices"][0]["Text"] = ('[Offer her another name] "I have given it a dying Queen '
                'to hold. Let the Crows carry her armour away. Walk out as Kitrane."')
            nodes["pitch"]["Text"] = ('{n}You show her the two shadows, one beneath the crown, one beneath '
                'the Crows\' cloak. Neither the dragon nor the priestess struck at a title: you have made '
                'a second victim for the rending to follow. The Queen\'s armour must be buried under her name. '
                'If you have missed a strand, sealing the coffin will not finish it. At the vigil, '
                'her knights must proclaim the Queen dead and call Kitrane out of the mourners. '
                'Their voices will give the divided shadows separate places among the dead and living.{/n} '
                '{n}She watches the dark light pull at the crest. The crown, the coffin, and the lie '
                'would be hers to leave behind. The trick has not healed her; it might yet tear her apart.{/n}')
            nodes["address"]["Text"] = ('{n}You recall the hag\'s advice about giving a curse another name '
                'to follow. Advice alone would have done nothing. The doubled shadow under Galfrey\'s '
                'armour is your doing, and you cannot promise it will hold.{/n}')
        elif sid == P + "iz.road":
            nodes["read"]["Text"] = nodes["read"]["Text"].replace(
                'Then the sergeant hammered the lead seal onto the Queen\'s coffin, with her name on the lid, and it let go.',
                'The strand you wound around the crest stayed with my armour. The sergeant put it in the royal coffin, '
                'then hammered on the lead seal. Only then did it let go.')
            nodes["fever"]["Text"] += (' {n}The sergeant shows you the cloak\'s lining. Its shadow still '
                'reaches toward the sealed coffin. You could not separate those strands at Iz; '
                'he has kept the cloak folded as you left it. The vigil must finish the work.{/n}')
        elif sid == P + "iz.alone":
            for key in ("letter3", "letter3.crows_supplies"):
                nodes[key]["Text"] = nodes[key]["Text"].replace(
                    'I think it is waiting to hear the Queen\'s death proclaimed where she was loved.',
                    'The shadow in the cloak you left with the sergeant still pulls toward my armour in the coffin. '
                    'He showed me the folds, and repeated your instructions for the vigil. '
                    'Have the knights name the Queen dead, then call Kitrane among the living.')
                nodes[key]["Text"] = nodes[key]["Text"].replace(
                    'I think it needs to hear the Queen\'s death proclaimed where she was loved.',
                    'Your trick in the sergeant\'s cloak has left two shadows joined. He showed me, '
                    'and repeated your instructions: the knights must name the Queen dead at the vigil, '
                    'then call Kitrane among the living.')
        elif sid == P + "iz.cortege":
            nodes["surgeon"]["Choices"][0]["Text"] = ('[Diplomacy DC 24] "Your knights have another name for her. Let me try it."')
            nodes["surgeon"]["Text"] = ('{n}An old Crow guards the chapel door.{/n} "Commander. '
                'The surgeon packed the wound with salt and wrapped her for the road. We are taking her home '
                'before the rot takes her. You should have come to Iz." {n}His hand stays on his sword.{/n} '
                '"They seal her at first light."')
            nodes["in"]["Text"] = ('{n}She lies cold on the bier. Salt has crusted the linen at her collarbone. '
                'There is no breath, no movement. You put a hand beneath the broken breastplate. '
                'Your shadow reaches farther, through the black wound; when you draw it back, '
                'it holds a dark thread stretched taut beyond the chapel wall. You wind it around her sword. '
                'A breath rattles in the dead woman\'s throat, but her eyes remain shut. '
                'You cannot draw her through the wound that killed her. You need another way out.{/n}')
            for key in ("flare", "flare_told", "flare_told.unworn"):
                nodes[key]["Text"] = nodes[key]["Text"].replace(
                    'the fact that it is the only name in the world this thing does not know',
                    'the thread held on her sword, and a name she can answer without stepping back into the Queen\'s death')
                nodes[key]["Text"] += (' {n}You lay the crowned breastplate beside her and pull '
                    'your shadow across it. A second outline settles beneath the crest. The thread '
                    'divides between them; a hoarse breath escapes her lips. You keep your hand '
                    'on the sword while she finds her voice.{/n}')
            nodes["choose"]["Text"] = nodes["choose"]["Text"].replace(
                'It wants to hear it said.',
                'Have the Crows name the Queen dead, then call Kitrane out of the vigil. '
                'I felt the thread pull when you divided it. Do not leave me between them.')
            nodes["sergeant"]["Text"] += (' {n}You keep the divided shadow pinned to the sword until '
                'first light. The Crows lift her into the green cloak and put her armour on Anselm. '
                'The vigil must finish the division: name the Queen dead, then call Kitrane. '
                'Until then the thread still joins her shadow to the crest. He keeps the cloak folded. '
                'She coughs blood into the cloak, and he carries her straight to the surgeon.{/n}')
            nodes["rest"]["Text"] += (' {n}You ease the thread from the sword. Her hand goes still; '
                'the shadow slips away through the black wound.{/n}')


_round3_rescue()


# The vigil enacts the standing instructions; recollections use the same device.
for _host in SCENES:
    _nodes = {node["Id"]: node for node in _host["Nodes"]}
    if _host["Id"] == OFFER:
        _nodes["seelah"]["Text"] = ('{n}Seelah\'s cry is still in the air: "Your Majesty!" '
            'Galfrey struggles for breath. You look from the crowned crest on her broken armour '
            'to the green cloak beneath her. The Crows already have a name for a knight without that crown.{/n}')
    elif _host["Id"].removesuffix("_stall") == P + "iz.eulogy":
        _nodes["tent"]["Text"] = ('{n}At the bells the Crows\' sergeant stands before the coffin '
            'and names the Queen dead. Then he goes to the wounded woman in his tent and calls, '
            '"Kitrane. Your watch." The squire unfolds the cloak as you showed the sergeant. '
            'Its shadow parts from the coffin\'s; the dark light under her bandage goes out. '
            'She answers her name, hoarsely, and falls asleep. The squire stays beside her '
            'until morning, listening to her breathe.{/n}')
    if _host["Id"] in (P + "epilogue.kitrane", P + "epilogue.sworn", P + "epilogue.late", P + "epilogue.widow"):
        for _para in _nodes["page"].get("Paragraphs", []):
            if FOREVER in _para.get("Requires", []) and "purse" in _para["Text"]:
                _para["Text"] += (' {n}She sent Anselm\'s daughter an account signed by the surviving Crows. '
                    'It named the man in the royal crypt. The sergeant offered to accompany her '
                    'if she petitioned the cathedral to move him. Kitrane kept the regents\' crown '
                    'out of that letter; she did not keep his death out of it.{/n}')
del _host, _nodes
