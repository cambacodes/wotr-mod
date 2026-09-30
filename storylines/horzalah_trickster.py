"""Horzalah on the Trickster path: "The ear in the gift box" (Writer/handoffs/trickster/horzalah.md for the canon research;
the binding plan is 11-ROSTER-PLAN-2 §2, Horzalah block and build sheet, rewritten 2026-09-29 after Astra design review r4.
It supersedes the spec's collar rename, the priest's raise, the contract test and the priced second ask).

Canon (Greybor's Q2 and Q3; Prison_Baph):
- a nephilim daughter of Baphomet, "an advance payment" given to Yozz as a concubine because "my father did not value me
  highly" (YozzDying/Cue_0042 2186d862), with "the collar-shaped scar on her throat" (Cue_0049 7dce8fdd); she owns Yozz
  ("Take care not to ruin my property", Cue_0019 b7f797a2) and sends gifts boxed with a white ribbon (Cue_0058 c200758b,
  the canary, Hepzamirah_main/Cue_0017 49356164);
- in Chapter 5 her seals are gone, Yozz "belongs to me... and so does his guild" (Horzalah_Ambush/Cue_0061 bfe4e3da), and
  she wants the Commander's head to win her father's favour (Cue_0012 aece9071); she has agents in Drezen (Greybor,
  Horzalah_Mercy/Cue_0011 ae22177b); beaten, she has "Nothing. Once my father hears of my failure, he'll take everything
  from me... even the guild." (Cue_4 4a3f22ae);
- Baphomet: "Horzalah bet everything - and lost. She invoked my name when she was on the brink of defeat, but I did not
  answer. ... Why should I nourish the shoots of the weaker branch?" (Prison_Baph/Cue_0122 03997856). He knows she lost,
  so no head can fool him: the con is never aimed at him, and his silence stands on every branch.

Device (a con aimed at her own Guild; an authored premise, labelled as the Commander's guess on the page): at the mercy
node the Commander guesses that a father who did not answer her call will not bother to take her Guild; her own assassins
will, on the word "failure". The Commander offers her a story for Alushinyrra: she goes home as the only master who ever
took a piece of the Knight Commander and let them live to wear the loss. She decides (Diplomacy). Success: she cuts off the
Commander's left ear herself and boxes it in a white ribbon. The lie is hers, told in her own hall; the Commander stages
nothing. Failure, dismissal or letting her go: the Guild circles, as guessed, and she comes back at night with a knife.
Cost: the ear, for good (her agents in Drezen watch for a regrown one). A player-chosen kill closes the route (§5 #2).
Commit: she shows the scar on her terms (unveiling a scar). The courtship on her presence lives in horzalah_guild.

Path fit (ROUTE-BRIEF-R, v1): every scene is tagged in PATH_FIT. T scenes are gated on the Trickster; the two Chapter 4
build-up beats are N-all and carry no Trickster gate. No non-Trickster commit or ending is written yet (v2).
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
REL = "horzalah"
H = "horzalah.trickster."

UNIT = "38f0acf8ba7c3b64b87369d478014fda"            # GreyborQ3/Horzalah (in person; CutsceneNeutrals, no dialog): presence copy
PROJECTION = "b7b3a7ce5bf8b4c49a2187e42e07a99a"      # her Chapter 4 projection (YozzDying, HorzalahFirst)
PORTRAIT_GUID = "5cf92593747540e29b285b16d23cbf16"    # the in-person unit's m_Portrait (fallback until custom art ships)
DREZEN = "2570015799edf594daf2f076f2f975d8"
STORYTELLER = "da4c28dd01413694f82b08b728a8c6e5"      # Units/.../BlackWingRuins/Storyteller (Vellexia stands right 2.0 m)
YOZZ_LIST = "9652bd6d33d394a498bb7a1c28693cc6"        # YozzDying/AnswersList_0039 (her questions, Chapter 4)
SCAR_CUE = "7dce8fddc72c85d49a9520a9bc1ac85f"         # YozzDying/Cue_0049: "...the collar-shaped scar on her throat" (clean)
MERCY_LIST = "8373a8ede2c5483e9a734dfea046fe2d"       # Horzalah_Mercy/AnswersList_0001 (loyal Greybor)
MERCY_RET = "4a3f22ae70e441d9b27ce67974f632d5"        # Cue_4: "Nothing. ... even the guild." (clean; answers only 0001)
FAREWELL = "c12bda4e0a95464db71e9f9f79e765de"         # Cue_0007: "...Farewell!" (OnStop: the HorzalaTPOut cutscene)
GREYBOR_LIST = "174d6c94b6725f44aad1d2a76993a926"     # CompanionDialogues/Grimbor/AnswersList_0002
WENDUAG_HUB = "ced27e744d2dded40bbb5adf17816dbb"      # CompanionDialogues/Wenduag/AnswersList_0003
Q3_FAIL = "e60797a42f8d33c4581cfe3bb37b5d2f"          # InterrogationAfterAssasination/Cue_0016 (fails Q3: HiddenObjective_Fail 528bc8a8)

STARTED = "horzalah.started"
CLOSED = "horzalah.closed"
COMMITTED = "horzalah.committed"

# Native keys (trickster_world binds the verified ones on demand; greybor.q3_failed is bound here).
KILLED = "horzalah.killed"
KILLED_B = "horzalah.killed_b"
DEAD = "horzalah.dead"                                # Derived: [killed], [killed_b], [killed_unmet]
DISMISSED = "horzalah.dismissed.latched"
MET_A = "horzalah.met_q3_a"
MET_B = "horzalah.met_q3_b"
MET_Q2 = "horzalah.met_q2"
SCAR_SEEN = "horzalah.scar_seen"
CANARY = "horzalah.gift_delivered"
NAMED = "baphomet.named_horzalah"
HEPZ_BACK = "hepzamirah.trickster.returned"           # node variants only (build sheet: no Requires/Forbids on hepzamirah.*)
Q2_DONE = "greybor.q2_done"
Q3_FAILED = "greybor.q3_failed"
SEALS_SEEN = "horzalah.seals_seen"    # HorzalahFirst/Cue_0001: the projection's "flaming seals of Baphomet" (Ch4)
SPAWN_TOLD = "baphomet.spawn_told"     # Prison_Baph/Cue_0121: "I could spawn hundreds, thousands more"
RESCUE_TOLD = "horzalah.rescue_refused_told"  # YozzDying/Cue_0051 "He refused to rescue me back then..." (her own words, Ch4)
LAPSED = "horzalah.q3_lapsed"                         # Derived: Greybor dead, kicked out, away, Q3 failed, or Chapter 6
GREY_IN = "greybor.in_party"
GREY_GONE = ("greybor.dead", "greybor.kicked_out")

# The route.
SCAR_NOTED = H + "scar_noted"          # Ch4: looked at the scar, not the seals
BOX_KEPT = H + "box_kept"              # Ch4: kept her empty box
BOX_BURNED = H + "box_burned"
PRIMED = H + "primed"                  # she took the story (and the ear)
EAR = H + "cost.ear"                   # the Commander's left ear, in her box, for good
LATE = H + "cost.late"                 # taken at night in the Commander's quarters; Drezen heard
LET_GO = H + "let_go"                  # the Greybor-less night: the Commander let her go without an offer
REFUSED = H + "refused"                # her no to the story (or "Let her go"): the Guild circles
CAME = H + "came_herself"              # the Greybor-less night: she came for the head in person
KILLED_UNMET = H + "killed_unmet"
GUARD = H + "guard_called"
RETURNED = H + "returned"              # the Guild kept, and she came back to see what she bought
WANTS = H + "wants_heard"
LEFT_FREE = H + "left_free"
THREATENED = H + "threatened"          # the Commander threatened to take her lie back (Evil): she cut and left
TESTED = H + "tested"
FREED = H + "cost.gift_freed"          # her gift freed in front of her (Good): she is insulted, and impressed
ALLY = H + "ally"                      # her gift accepted (Evil): an owner of people would own her too
DECLINED = H + "declined"              # the soft no at the collar: reached like a buyer, or asked whose mark it was
CHAMBER = H + "chamber_seen"
MORNING = H + "morning_seen"
# Keepsakes from the courtship on her presence (horzalah_guild), read by the pages and her Last Call coda.
P_KNIFE = H + "beat.knife_won"         # the Commander took her knife off her in the lesson: the one that cut the ear
P_WHISTLE = H + "beat.whistle_taken"   # the dwarf's rune whistle (Horzalah_Ambush/Cue_0057), stolen for her in the street
P_RIBBON = H + "beat.ribbon_tied"      # the Commander learned her bow, and ties it badly
LATE_COMMITTED = H + "late_committed"  # R2-6: she said what she wants; the page after the Threshold answers it

PRESENCE = "horzalah.presence"
PRESENCE_FAILED = "horzalah.presence.failed"

RELATIONSHIP = dict(
    Title="A Gift with a Ribbon",
    Description=("Horzalah, Baphomet's daughter, master of the Assassins' Guild in Alushinyrra, wanted my head for her "
                 "father. She did not get it. She got something else of mine, and she keeps it in a box with a white ribbon "
                 "on a shelf in her hall."),
    Objective="See what Horzalah does with what she took",
    Guidance=("On the Trickster path, when Horzalah lies beaten at the Dry Crossroads, ask her what she has left and do not "
              "kill her. If Greybor never brings you there, she will come for your head herself. Looking at her scar in "
              "Yozz's hall in Alushinyrra, or hearing her father speak of her in his prison, may help her listen."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD], FailureFlags=[], UnavailableOverrides={},
    TricksterAccess={
        "mercy": dict(detect=["!" + DEAD], device=H + "mercy.gift", returned=PRIMED),
        "unmet": dict(detect=["!" + DEAD], device=H + "unmet.knife", returned=PRIMED),
        "late": dict(detect=["!" + DEAD], device=H + "late.at_night", returned=PRIMED),
    },
)

DERIVED = {
    # 11 §2 build sheet: both extend the merged keys (trickster_world); a kill in the Greybor-less night is her death too.
    DEAD: [[KILLED], [KILLED_B], [KILLED_UNMET]],
    LAPSED: [["greybor.dead"], ["greybor.kicked_out"], ["greybor.away"], [Q3_FAILED], ["chapter.six"]],
    LATE_COMMITTED: [["trickster.ever", WANTS]],
    # 05 §2.5 voice note: she joins as an owner who keeps what she takes; the household is never her property's keeper.
    "horzalah.harem.voice.keeps_what_she_takes": [[COMMITTED]],
}
# The objective itself (QuestObjectives [528bc8a8..., "Failed"]) does not resolve as a standalone blueprint at load, so the
# failure is read from the cue that sets it: Greybor's "We've lost an important lead" after the assassin dies unquestioned.
SEEN_CUES = {Q3_FAILED: [Q3_FAIL], RESCUE_TOLD: ["fc5119d8d4a54e047b07338764beb346"],
             SEALS_SEEN: ["fc1030e8724b086479d7ec2a52aae2a5"], SPAWN_TOLD: ["0cdc1a24d29c77f4490900d3a9418afc"]}

# Path fit (ROUTE-BRIEF-R 2026-09-29, v1): T = device or Trickster-only; N-all = any path; N-fit = the fitting paths.
PATH_FIT = {}


def tag(scene_id, fit):
    PATH_FIT[scene_id] = fit


def hz(id, text, *choices, **kw):
    """Horzalah on a rest-delivered page or at her presence (her portrait)."""
    return n(id, "Horzalah", text, *choices, portrait="Horzalah", **kw)


def hzi(id, text, *choices, **kw):
    """Horzalah inside a Greybor quest dialog: the in-person unit's own portrait and name (E14f)."""
    return n(id, "Horzalah", text, *choices, speaker_unit=UNIT, **kw)


def proj(id, text, *choices, **kw):
    """Her Chapter 4 projection inside YozzDying (E14f)."""
    return n(id, "Horzalah", text, *choices, speaker_unit=PROJECTION, **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def pitch(text, success, failure):
    """The Diplomacy check: DC 22 with her father's contempt heard, 24 after the scar was looked at, 26 otherwise."""
    return (
        c(text, check=dict(Skill="CheckDiplomacy", DC=22, Success=success, Failure=failure), requires=(NAMED,)),
        c(text, check=dict(Skill="CheckDiplomacy", DC=24, Success=success, Failure=failure), requires=(SCAR_NOTED,),
          forbids=(NAMED,)),
        c(text, check=dict(Skill="CheckDiplomacy", DC=26, Success=success, Failure=failure), forbids=(NAMED, SCAR_NOTED)),
    )


# --- 1. Chapter 4 (N-all): the scar in Yozz's hall, and the box after Colyphyr. ------------------------------------------

SCENES.append(scene(H + "ch4.scar", "The collar-shaped scar", "Horzalah", 4, "[Look at the scar on her throat, not at the seals.]", [
    proj("look", '''{n}Her hand is still at her throat. The seals burn all over the projection's skin, a crowd of little fires, and the eye goes to them the way it goes to a burning house. Yours goes to the one mark on her that is not burning: a pale band around her neck, two fingers wide, with the ghost of a buckle pressed into one side of it.{/n}
{n}She sees where you are looking. The hand comes down at once.{/n}
"The seals are more interesting, mortal. Everyone says so. My father's work is very fine; demons come from other layers to admire it."''',
         c('"Everyone looks at the seals. I was looking at you."', "you"),
         c('"Who puts a collar on Baphomet\'s daughter?"', "who"),
         c("[Say nothing, and look at the seals like everyone else.]", abort=True)),
    proj("you", '''{n}The projection flickers, the way a candle flickers when a door opens somewhere else in the house.{/n}
"At me." {n}Her voice drops to the aggrieved whisper she used for her own name.{/n} "Do you know how many people in this Guild have looked at me, in all the years I stood behind Yozz's chair? Yozz looked at me the way he looked at his cufflinks. The clients looked at the seals and wondered what I had done to earn them. My father..." {n}She stops.{/n}
"You are standing in a room full of corpses, in my Guild, and you are wasting my time. I will remember that you wasted it on the wrong thing."''',
         c("[Let her go back to her questions.]", flags=(SCAR_NOTED,))),
    proj("who", '''"Who?" {n}Dark flames move behind her eyes.{/n} "My father made the collar. It was the only seal he ever put on me that did not hurt; it simply said *mine*. Then he sold me with it, and Yozz held the leash. He had it gilded. He liked gold."
"When Yozz grew tired of walking me through his parties on a chain, the collar came off. It left that." {n}Her mouth twists.{/n} "Nothing that was taken from me has ever come back whole, mortal. Not even my own neck. Look at the seals. They are prettier, and they are none of your business either."''',
         c("[Let her go back to her questions.]", flags=(SCAR_NOTED,)))],
    requires=(SCAR_SEEN,), forbids=(SCAR_NOTED,), last=4, Relationship=REL,
    AnswerLists=[YOZZ_LIST], NativeReturnCue=SCAR_CUE))
tag(H + "ch4.scar", "N-all")

BOX_NODES = [
    nar("start", '''{n}It is waiting on your camp table when you come back from the day's business, and nobody on watch saw who left it: a neat little box wrapped in black paper and tied with a white ribbon in a perfect bow. When you lift it, it weighs almost nothing. When you shake it, nothing moves.{/n}''',
        c("Continue", "canary", requires=(CANARY,)),
        c("Continue", "plain", forbids=(CANARY,))),
    nar("canary", '''{n}You have seen that ribbon before. You carried a box tied with it all the way down into the mines of Colyphyr, and watched a dead canary come out of it with her voice in its beak, and turn into a spear of fire, and fly at her sister's face.{/n}
{n}You hold this one a little further from your own.{/n}''',
        c("[Untie the bow.]", "open")),
    nar("plain", '''{n}The bow is tied the way a jeweller ties one, the ends cut on the slant so they will not fray. Whoever tied it took a great deal of trouble over something that weighs nothing.{/n}''',
        c("[Untie the bow.]", "open")),
    hz("open", '''{n}Inside, on a bed of black silk, there is nothing at all. Under the silk there is a card, written in a hand as sharp as a row of nails.{/n}
"Hepzamirah is dead in the mines of Colyphyr, and they tell me it was you who put her there. My father has already remembered that he has another daughter. My seals came off this morning. It hurt a great deal less than it did going on.
In gratitude, I send you exactly what you have earned from me. Look carefully. It is all there.
Horzalah. Not Hepzamirah."''',
       c("[Look carefully.]", "careful"),
       c("[Keep the box, and the ribbon.]", "kept", flags=(BOX_KEPT,)),
       c("[Put the whole thing in the stove.]", "burned", flags=(BOX_BURNED,))),
    nar("careful", '''{n}You look carefully. You lift the silk and look under it, and turn the box over, and run a thumb along the seams. It is very good black silk, the kind the Midnight Isles sell by the finger's width, and it is wrapped around nothing, perfectly.{/n}
{n}On the back of the card, in a different ink and a hurried hand, as if it had been added at the door:{/n} "You looked. I knew you would. Keep the ribbon; I have plenty."''',
        c("[Keep the box, and the ribbon.]", "kept", flags=(BOX_KEPT,)),
        c("[Put the whole thing in the stove.]", "burned", flags=(BOX_BURNED,))),
    nar("kept", '''{n}You put the empty box in the bottom of your pack, under the maps, with the ribbon tied round it again. It is a ridiculous thing to carry to war. It takes up almost no room.{/n}''',
        c("Continue")),
    nar("burned", '''{n}The paper goes up at once. The silk takes longer and smells of the Isles, of incense and something sweeter underneath. The ribbon does not burn at all. You find it in the ashes in the morning, white and whole, and throw it out with them.{/n}''',
        c("Continue"))]
# At the first rest of Chapter 5, before the ambush (Greybor's third quest waits for Iz): Hepzamirah is dead in Colyphyr by
# then on every path, so no hepzamirah.* key is read, and her rest budget allows no Chapter 4 letter.
SCENES.append(scene(H + "ch5.nothing", "A box with a white ribbon", "Horzalah", 5, "", copy.deepcopy(BOX_NODES),
    requires=(MET_Q2,), forbids=(BOX_KEPT, BOX_BURNED, MET_A, MET_B, PRIMED, REFUSED, CLOSED), delay=0, last=5,
    Relationship=REL, Remote=True, Kind="letter", Chapters=[5], optional=True))
tag(H + "ch5.nothing", "N-all")


# --- 2. The mercy node (T): the guess, the story, and her knife. ---------------------------------------------------------

BOX_ROAD = '''{n}She makes a small gesture, the one she made in Yozz's hall, and a neat box appears on her palm, black paper and black silk and a white ribbon. She lays your ear on the silk as carefully as a jeweller lays down a stone, and ties the bow one-handed. The ends are cut on the slant, so they will not fray.{/n}
"Listen to me, mortal, with the one you have left. I have people in your city. The dwarf will tell you so; he worked it out on his own. The day one of them writes to me that the Knight Commander has two ears again, I will know you made a fool of me, and so will every knife that ever bowed to this box."
"No priest touches that. Not ever. It is mine now."'''
BOX_ROOM = '''{n}She makes a small gesture, and a neat box appears on her palm out of nothing, black paper and black silk and a white ribbon. She lays your ear on the silk as carefully as a jeweller lays down a stone, and ties the bow one-handed. The ends are cut on the slant, so they will not fray.{/n}
"Listen to me, mortal, with the one you have left. I have people in your city. How do you think I found your bed? The day one of them writes to me that the Knight Commander has two ears again, I will know you made a fool of me, and so will every knife that ever bows to this box."
"No priest touches that. Not ever. It is mine now."'''


def _ear_nodes(prefix, native):
    """Her yes: she chooses the ear, cuts it herself and boxes it. native=True ends in her own farewell (Cue_0007)."""
    ends = (dict(native_next=FAREWELL) if native else dict())
    speaker = hzi if native else hz
    return [
        speaker(prefix + "ear", '''{n}She stares at you as if you had begun speaking in the tongue of the Lawful planes.{/n}
"A piece of you. Given. To lie with." {n}She tastes the words.{/n} "Nobody gives Baphomet's daughter anything, mortal. They sell, or they pay, or they bleed. My father sold me. Yozz paid for me. Everyone else bled."
{n}Her eyes move over you the way a butcher's move over a carcass: not the hand, which the Guild would say you lost in battle; not an eye, which they would call a curse.{/n} "The ear," {n}she decides.{/n} "The left one. Everyone who looks you in the face will see where it was."''',
            c("[Kneel, and turn your head for her.]", prefix + "cut"),
            c('"Take it, then."', prefix + "cut")),
        nar(prefix + "cut", '''{n}She does it herself. Her fingers close in your hair and pull your head over, not roughly, the way a barber holds a head he is being paid well to shave. The knife is small and very sharp. There is a sound like a boot going through thin ice, and a pressure, and then a cold place on the side of your skull that is suddenly very large.{/n}
{n}The pain arrives a heartbeat later, all at once, and fills the whole left side of the world.{/n}''',
            c("Continue", prefix + "box")),
        speaker(prefix + "box", BOX_ROAD if native else BOX_ROOM,
            c('"It\'s yours."', prefix + "exit"),
            c('"Bandages are allowed, I hope."', prefix + "bandage")),
        speaker(prefix + "bandage", '''"Bandages." {n}Her mouth twitches, the nearest thing to a smile you have seen on it that did not have someone's death behind it.{/n} "Wrap it in cloth of gold if you like. Wear a hat. Grow your hair. I do not care what your face looks like, mortal, so long as the ear is in my box and not on your head."''',
            c('"Understood."', prefix + "exit")),
    ] + ([
        hzi(prefix + "exit", '''{n}She tucks the box inside her armour, against her ribs. Then she arranges her face, and you watch her do it: the sullen mouth, the lowered eyes, the look of a woman beaten in the dust of a road. For the dwarf. For anyone of hers still breathing among the bodies. For herself, perhaps, so the lie will be easier to carry home.{/n}''',
            c("[Let her have her exit.]", flags=(PRIMED, EAR, STARTED), **ends)),
    ] if native else [
        hz(prefix + "exit", '''{n}She tucks the box inside her armour, against her ribs, and looks at the door, where the guards have stopped hammering and started to use an axe.{/n}
"Tell them I came for your head and left with a souvenir. It is even true." {n}The air folds round her like a curtain drawn by a hand you cannot see, and she is gone, and the lamp is guttering, and your pillow is ruined.{/n}''',
           c("[Open the door to your guards.]", flags=(PRIMED, EAR, STARTED, CAME))),
    ])


def _refused(prefix, native):
    speaker = hzi if native else hz
    text = '''{n}She looks at you for the space of a breath, and then she spits, very precisely, on your boot.{/n}
"Mercy from you is worse than the knife." {n}She is shaking; you cannot tell whether it is fury or blood loss.{/n}
"You want me to walk into my own hall carrying a present from the {mf|man|woman} who beat me, and call it a trophy. You want me to lie to my own knives with your blood on my hands and your pity in my pocket. No. I will take my chances with the truth, mortal. It is the only thing I have left that nobody gave me."'''
    if native:
        return [speaker(prefix + "refused", text, c("[Let her go.]", flags=(REFUSED, STARTED), native_next=FAREWELL))]
    return [speaker(prefix + "refused", text, c("Continue", prefix + "refused_go")),
            hz(prefix + "refused_go", '''{n}The air folds round her like a curtain drawn by a hand you cannot see. When the guards get the door open there is nobody in the room but you, a guttering lamp and a great deal of blood that is mostly hers.{/n}''',
               c("[Let them in.]", flags=(REFUSED, STARTED, CAME)))]


MERCY_PITCH = ('[Offer her a better story] "Then don\'t go home beaten. Go home with a piece of the Knight Commander in a box, '
               'and tell them you let me live to wear the loss."')

SCENES.append(scene(H + "mercy.gift", "What she has left", "Horzalah", 5, '"Here is a guess, since you say you have nothing left: your father won\'t take your Guild. He won\'t bother."', [
    hzi("guess", '''{n}Horzalah stops laughing. She looks up at you from the dust of the Dry Crossroads with blood in her teeth, and for a heartbeat she is as still as a snake is before it decides.{/n}
"A guess." {n}Her voice drips with contempt.{/n} "A mortal guesses what the Lord of Beasts will bother to do. How generous of you. Go on, then. Guess some more, since I am in no position to leave."''',
        c('"I\'ve been in his prison. He told me what he thinks of you: \'Why should I nourish the shoots of the weaker branch?\'"',
          "branch", requires=(NAMED,)),
        c('"He left you in your sister\'s cell and sold you to Yozz. A father like that doesn\'t cross the Abyss to take back a Guild."',
          "called", requires=(RESCUE_TOLD,)),
        c('"Listen to yourself. You\'re asking what he\'ll take, not whether he\'ll come for you. You already know he won\'t."', "called")),
    hzi("branch", '''{n}The words land. You watch them land. Her hand goes to her throat, to the collar-shaped scar, and stays there.{/n}
"The weaker branch." {n}She says it very quietly, and then she laughs, a dry sound with nothing inside it.{/n} "He said that to you. To a crusader, in his own house, as if he were remarking on the weather."
"Yes. That is Father. He does not pluck a weed he has already stopped watering. Why would he come all the way to Alushinyrra to take a Guild off a daughter he cannot even be bothered to hate?"''',
        c("Continue", "guild")),
    hzi("called", '''{n}She bares her teeth at you.{/n} "He will come when it pleases him. He hears everything said in his name. He simply..." {n}She stops, because there is no end to that sentence she can bear to say aloud with the dwarf listening.{/n}
"You know nothing of my father, mortal. That is a stranger's guess, and a stupid one. The Lord of Beasts takes back what he gives. It is the one thing he has always been good at."''',
        c("Continue", "guild")),
    hzi("guild", '''{n}She looks past you, at her own people lying on the road with their throats open.{/n}
"But you are right about one thing, and only because it is obvious. The Guild does not wait for Father's verdict. The Guild bows to strength and eats failure. A dozen of my knives are lying here tonight, and the ones who stayed home will hear by morning that their master was beaten on a crossroads by one mortal and a dwarf."
"By the next night, someone will be sitting in my chair, wondering whether my head would look better on the notice board or over the door."''',
        *pitch(MERCY_PITCH, "ear", "refused"),
        c('"Then I suppose you\'d better think of something."', abort=True)),
    *_ear_nodes("", True),
    *_refused("", True)],
    requires=("trickster",), forbids=(PRIMED, REFUSED, CLOSED), last=5, Relationship=REL,
    AnswerLists=[MERCY_LIST], NativeReturnCue=MERCY_RET, EntryMythic="PlayerIsTrickster",
    TricksterDevice=True, TricksterState="mercy"))
tag(H + "mercy.gift", "T")


# --- 3. Greybor never brings her to the Dry Crossroads (T): she comes for the head herself. --------------------------------

UNMET_PITCH = ('[Offer her a better story] "Then don\'t go home with nothing. Take a piece of the Knight Commander home in a box, '
               'and tell them you let me live to wear the loss."')

SCENES.append(scene(H + "unmet.knife", "Hired help is so disappointing", "Horzalah", 5, "", [
    nar("start", '''{n}The first you know of it is the lamp. It was burning when you lay down, and now it is not, and the dark in the room has a shape standing in it, tall and lean, with a knife.{/n}''',
        c("Continue", "met", requires=(MET_Q2,)),
        c("Continue", "stranger", forbids=(MET_Q2,))),
    hz("met", '''{n}You know the voice before the lamp flares up again under her hand. The projection from the Guild in Alushinyrra, in the flesh this time: no seals now, no flames, only skin, and a pale band around her throat where a collar used to be.{/n}
"Horzalah," {n}she says,{/n} "not Hepzamirah. We spoke over a pile of corpses in my Guild, and you left with Yozz's bounty and your life. I let you keep both. I have since learned that my father values your head rather more than I did."''',
       c("Continue", "demise")),
    hz("stranger", '''{n}The lamp flares up again under her hand. A demon-woman, thin to the point of hunger, with a nephilim's horns and not a single brand on her skin; only a pale band around her throat where a collar used to be.{/n}
"Horzalah," {n}she says,{/n} "not Hepzamirah. You killed my sister in Colyphyr, and for that I will give you... nothing. My father gave me back my power and took his seals off me, and I took Yozz's Guild for myself. Now he will give me his favour, when I bring him your head."''',
       c("Continue", "demise")),
    hz("demise", '''"I have hired knives for you, Commander. Hired help is so disappointing: they take the money in advance and lose their nerve in the corridor." {n}She turns her blade so the lamplight runs along it.{/n}
"So I came myself. I wanted to personally witness your demise!"''',
       c("[Throw the blanket at her face and go for your sword.]", "fight"),
       c('"You could have knocked."', "fight")),
    nar("fight", '''{n}It is short and ugly, and the room does not survive it. She is faster than anything you have fought in a bedchamber, and stronger than she looks, and she fights like someone who has been told her whole life that she is the lesser of two: every blow is meant to prove somebody wrong.{/n}
{n}It is not enough. When she goes down against the wall, with your blade under her chin and her own knife somewhere under the bed, she does not look at you. She looks up, past the ceiling, and screams a name. "Father! FATHER!"{/n}
{n}Nothing answers. Outside, your guards have started hammering on the door.{/n}''',
        c("Continue", "beaten")),
    hz("beaten", '''{n}She sags against the wall. Her eyes come down from the ceiling slowly, as if they had to be fetched.{/n}
"This is not how it was supposed to end," {n}she says, to nobody.{/n} "Why are you so strong, mortal? Nobody told me you were so strong." {n}Then, to you, flat:{/n} "Go on. I have nothing left. When my father hears of this, he will take everything from me. Even the Guild."''',
       c('[Tell her your guess] "He won\'t. He didn\'t answer you just now, and he won\'t come for your Guild either. Your own knives will."',
         "guess", mythic="Trickster"),
       c('[Let her go] "Get out. Go home and tell them whatever you like."', "go"),
       c('[Kill her] "You shouldn\'t have come here."', "kill")),
    hz("guess", '''{n}Her head comes up.{/n} "A guess." {n}Blood runs from her lip into the pale band at her throat.{/n} "A crusader in a nightshirt guesses what the Lord of Beasts will bother to do."
"...And guesses right. That is the insulting part." {n}She shuts her eyes.{/n} "The Guild bows to strength and eats failure. I went out alone, in the night, to kill one mortal in bed, and I am sitting on the floor of {mf|his|her} room. By tomorrow night somebody will be sitting in my chair, polishing a spike for my head."''',
       c('"He called you the weaker branch, in his prison. He won\'t waste a trip on you. Your masters will."', "branch",
         requires=(NAMED,)),
       *pitch(UNMET_PITCH, "ear", "refused"),
       c('[Let her go] "Then go home and take your chances."', "go")),
    hz("branch", '''{n}She flinches, as she did not flinch from your sword.{/n}
"The weaker branch." {n}Her fingers find the scar at her throat.{/n} "Yes. He would say that. To you, in his house, as if he were talking about the weather." {n}Her eyes open, and something in them has gone very cold and very clear.{/n}
"Then say the rest, mortal. You did not stop me on the floor of your room to insult me. You have a use for me. What is it?"''',
       *pitch(UNMET_PITCH, "ear", "refused"),
       c('[Let her go] "No use. Go home and take your chances."', "go")),
    *_ear_nodes("", False),
    *_refused("", False),
    hz("go", '''{n}She gets up slowly, one hand on the wall. She finds her knife under the bed without looking for it, and puts it away.{/n}
"You will regret this mercy, mortal. Not because I will come back for you; because you will never know if I am coming." {n}The air folds around her like a curtain drawn by a hand you cannot see, and when your guards break the door in, there is nobody in the room but you.{/n}''',
       c("[Let them in.]", flags=(REFUSED, STARTED, CAME, LET_GO))),
    nar("kill", '''{n}You do it quickly, which is more than she came to do for you. She does not call her father's name again. By the time your guards break the door in, there is nothing left to guard you from, and nobody in Alushinyrra will ever know which of the Knight Commander's nights was the one she did not come home from.{/n}''',
        c("Continue", flags=(KILLED_UNMET, CLOSED)))],
    requires=("trickster", "iz.done", "coronation.seen"),
    forbids=(PRIMED, REFUSED, CLOSED, MET_A, MET_B, Q2_DONE), ForbidOverrides={Q2_DONE: LAPSED},
    last=6, Relationship=REL, Remote=True, Kind="visit", TricksterDevice=True, TricksterState="unmet"))
tag(H + "unmet.knife", "T")


# --- 4. The Guild circles, as guessed (T): she comes back at night. -------------------------------------------------------

SCENES.append(scene(H + "late.at_night", "Three nights", "Horzalah", 5, "", [
    nar("start", '''{n}She does not use the window. You wake because the air in the room has folded, the way it folded around her when she left you last, and when it unfolds she is standing at the foot of your bed with a knife in her hand and three nights without sleep in her face.{/n}''',
        c("Continue", "refused", requires=(REFUSED,), forbids=(CAME,)),
        c("Continue", "refused_offer", requires=(REFUSED, CAME), forbids=(LET_GO,)),
        c("Continue", "refused_room", requires=(LET_GO,)),
        c("Continue", "dismissed", forbids=(REFUSED,))),
    hz("refused_offer", '''"You had me on the floor of this room with your blade under my chin," {n}she says,{/n} "and you made me an offer, and I spat on it." {n}Her mouth twists.{/n}
"Father has said nothing since. Not a word, not a whisper, not a cultist at the door. And for three nights three of my own masters have followed me from room to room in my own hall, smiling. They heard before I was home that I went out alone to take one mortal's head and came back without it. They are waiting to see who says the word 'failure' first, and they are beginning to think it will not need to be Father."''',
       c("Continue", "head")),
    hz("refused_room", '''"You let me go," {n}she says.{/n} "You sat me on the floor of this room with your blade under my chin, and then you let me walk out through the wall, and told me to take my chances." {n}Her mouth twists.{/n}
"I took them. Father has said nothing. Not a word, not a whisper, not a cultist at the door. And for three nights three of my own masters have followed me from room to room in my own hall, smiling. They heard before I was home that I went out alone to take one mortal's head and came back without it. They are waiting to see who says the word 'failure' first, and they are beginning to think it will not need to be Father."''',
       c("Continue", "head")),
    hz("refused", '''"You guessed," {n}she says.{/n} "I lay there bleeding on that crossroads and you guessed, and you guessed right, and I spat on your boot for it."
"Father has said nothing. Not a word, not a whisper, not a cultist at the door. And for three nights three of my own masters have followed me from room to room in my own hall, smiling. They are waiting for someone to say the word first. They would prefer it to be Father. They are beginning to think they do not need him to."''',
       c("Continue", "head")),
    hz("dismissed", '''"'Get out of my sight,' you said." {n}Her voice is hoarse, as if she had been shouting for days, or not using it at all.{/n} "I got out. It did not help."
"Father has said nothing. Not a word, not a whisper, not a cultist at the door. And for three nights three of my own masters have followed me from room to room in my own hall, smiling. They heard about the crossroads before I was home. They are waiting to see who says the word 'failure' first, and they are beginning to think it will not need to be Father."''',
       c("Continue", "head")),
    hz("head", '''{n}The knife point comes up, not quite toward you.{/n}
"So I came back for your head. It is the only thing that would shut their mouths. I have been standing here long enough to take it twice." {n}She does not move.{/n} "And I keep thinking that a woman who could not take it the first time, when she had every advantage, does not walk into her hall with it three days later. They would ask how. I would have to lie. They would smell it."''',
       c('[Offer it again] "Then take the other thing. What I offered you before. It\'s still on the table."', "take",
         requires=(REFUSED,), forbids=(LET_GO,)),
       c('[Offer her a better story] "They\'d smell a head. They won\'t smell an ear. Take a piece of me home and tell them you let me live to wear the loss."',
         "take", forbids=(REFUSED,)),
       c("[Call the guard.]", "guard"),
       c('[Offer her a better story] "They\'d smell a head. They won\'t smell an ear. Take a piece of me home and tell them you let me live to wear the loss."',
         "take", requires=(LET_GO,))),
    hz("take", '''{n}She looks at you for the length of three slow breaths. Then she sits down on the edge of your bed, as if her legs had decided it for her.{/n}
"I hate you," {n}she says, conversationally.{/n} "I want you to know that. I will hate you for this for longer than your whole line will live." {n}She takes a fistful of your hair.{/n} "The left one. Everyone who looks you in the face will see where it was."''',
       c("[Turn your head for her.]", "cut")),
    nar("cut", '''{n}The knife is small and very sharp. There is a sound like a boot going through thin ice, and then a cold place on the side of your skull that is suddenly very large, and then the pain, all at once, filling the whole left side of the world. Your blood goes everywhere. It is a great deal of blood for one ear.{/n}
{n}She makes a box out of the air, black paper and a white ribbon, and ties the bow over your ear one-handed, and is gone before your shout brings the guard.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}By noon the whole citadel knows that a demon walked through the Knight Commander's door at night, past every sentry, and walked out again with a piece of the Knight Commander in her hand. The quartermaster doubles the watch. Two of the lords who lend the crusade their men write to ask whether their sons are safer at home. A priest comes to your door with his hands already glowing.{/n}''',
        c('"No priest. Leave it as it is."', "no_priest")),
    hz("no_priest", '''{n}The priest goes away offended. That night there is a note on your pillow, pinned through with a knife so thin you did not hear it go in. The hand is as sharp as a row of nails.{/n}
"My people in your city tell me you sent the priest away. Good. The day they tell me otherwise, I will know you made a fool of me, and so will every knife that ever bows to that box. It is mine now. H."''',
       c("[Pull the knife out of your pillow.]", flags=(PRIMED, EAR, LATE, STARTED), crusade=("Favors", -100))),
    hz("guard", '''{n}You shout. She does not flinch at it. She only looks at you as though you had shown her something she had expected all along, and found it disappointing anyway.{/n}
"Then keep your guards, mortal. Keep your head. See how long either lasts." {n}The air folds round her, and your door bursts open on an empty room.{/n}''',
       c("Continue", flags=(GUARD, CLOSED)))],
    requires=("trickster",), RequiresAnyGroups=[[DISMISSED, REFUSED]], forbids=(PRIMED, CLOSED),
    delay=24, last=6, Relationship=REL, Remote=True, Kind="visit", TricksterDevice=True, TricksterState="late"))
tag(H + "late.at_night", "T")


# --- 5. The Guild kept (T): she comes to see what she bought. The pivot. -------------------------------------------------

SCENES.append(scene(H + "guild.kept", "The Guild bowed to the box", "Horzalah", 5, "", [
    nar("start", '''{n}The air in your room folds and unfolds, and she is there: taller than you remember, without a mark on her, in black leather cut close, with a new high collar buckled up to her jaw. She does not greet you. She walks straight to you and lifts your hair off the side of your head with two fingers, and looks.{/n}''',
        c("Continue", "looks")),
    hz("looks", '''"Healed badly," {n}she says.{/n} "Puckered. The priest never touched it. Good." {n}She lets your hair fall.{/n}
"I came home through the front door, mortal, in the middle of the evening, when the hall is full. I did not hurry. I walked to the notice board where we post the contracts, and I pinned the box to it, over the contract on your head, and I untied the ribbon in front of every master of the Guild."''',
       c("Continue", "hall")),
    hz("hall", '''"They passed it from hand to hand. Nobody said anything. One of them sniffed it. One of them, who had been sitting in my chair when I came in, got up and put the chair back where it was." {n}She smiles, thinly.{/n} "I let him live. He will be grateful for a very long time. Grateful men make excellent knives."
"The Guild bowed to the box." {n}A pause.{/n} "And Father said nothing. Not a whisper, not a dream, not a cultist on the stair. He does not know, or he does not care, and I find I cannot tell the difference any more. And that I do not need to."''',
       c("Continue", "came", requires=(CAME,)),
       c("Continue", "late", requires=(LATE,), forbids=(CAME,)),
       c("Continue", "box", requires=(BOX_KEPT,), forbids=(LATE, CAME)),
       c("Continue", "sister", requires=(HEPZ_BACK,), forbids=(LATE, BOX_KEPT, CAME)),
       c("Continue", "pivot", forbids=(LATE, BOX_KEPT, HEPZ_BACK, CAME))),
    hz("came", '''"They asked me how. My masters. A woman goes out alone at night to kill one mortal in bed, and comes home without the head, with a box instead." {n}She smiles, thinly.{/n}
"I told them the truth. I said: I stood over the Knight Commander's bed with my knife, and I took what I pleased, and I left the rest of {mf|him|her} breathing, because a corpse forgets and a scar remembers. They liked that. They wrote it down." {n}Her eyes go to your ear.{/n} "It is even true. Most of it."''',
       c("Continue", "late", requires=(LATE,)),
       c("Continue", "box", requires=(BOX_KEPT,), forbids=(LATE,)),
       c("Continue", "sister", requires=(HEPZ_BACK,), forbids=(LATE, BOX_KEPT)),
       c("Continue", "pivot", forbids=(LATE, BOX_KEPT, HEPZ_BACK))),
    hz("late", '''"Your own city did half my work for me. By the time I was home, every tavern in the Lower City had heard that the Knight Commander woke in a bloody bed with a piece missing, and that a woman in a collar had walked past every sentry to take it." {n}She sounds pleased, and faintly offended.{/n} "They doubled your watch, I hear. They should have. It would not have helped."''',
       c("Continue", "box", requires=(BOX_KEPT,)),
       c("Continue", "sister", requires=(HEPZ_BACK,), forbids=(BOX_KEPT,)),
       c("Continue", "pivot", forbids=(BOX_KEPT, HEPZ_BACK))),
    hz("box", '''{n}Her eyes go to your pack, where it lies in the corner. To the bottom of it, where there is an empty box under the maps with a white ribbon round it.{/n}
"You kept my nothing." {n}Something moves in her face that she puts away at once.{/n} "My people told me. I did not believe them. Nobody keeps an empty box, mortal. Everybody looks inside and throws it away."''',
       c("Continue", "sister", requires=(HEPZ_BACK,)),
       c("Continue", "pivot", forbids=(HEPZ_BACK,))),
    hz("sister", '''"And my sister walks again, they tell me. Dead in Colyphyr, and now she stands in your city by a smith's forge, in a body some butcher grew her, eating onions." {n}Her lip curls back from her teeth.{/n}
"I will not ask how. I do not care how. Keep her away from my box. If she so much as breathes on that ear, I will send her something else with a ribbon on it, and this time it will not be a canary."''',
       c("Continue", "pivot")),
    hz("pivot", '''{n}She folds her arms and looks at you, down the length of her nose, the way she looks at a contract she has not yet decided to accept.{/n}
"So. The Guild is mine. My father is silent. My knives are grateful. I have everything I had before you beat me, and one ear more." {n}She tilts her head.{/n} "I came to see what I bought with your blood, mortal. I have seen. Now tell me why I should not simply go home and never think of you again."''',
       c('[Hear what she wants] "Because you came. You didn\'t have to. What do you want?"', "wants"),
       c('[Let her go for good] "You shouldn\'t. You have your Guild. Go home, and keep the ear."', "free"),
       c('[Threaten to take it back] "Because I know what\'s really in that box. One letter to your masters, and the story is mine again."',
         "threat", alignment=("Evil", 1))),
    hz("wants", '''{n}When she speaks it is slowly, as if she were reading terms off a contract she had not written.{/n}
"I want to come and go in your city as I please, and have no one follow me. I want to stand where I like. I want your soldiers to step off the path when I walk it, and not to know why." {n}Her eyes go to the side of your head.{/n} "And I want to look at that whenever I choose, because it is mine."
"Everything I have ever had, I took. My Guild. Yozz. My own name back. I do not know what to do with a thing that was handed to me." {n}She turns toward the air, which is already beginning to fold.{/n} "I am going to stand in your street and think about it. Do not have me watched."''',
       c('"Nobody will watch you."', flags=(RETURNED, WANTS))),
    hz("free", '''{n}She stares at you as if you had struck her. Then, slowly, she laughs, and it breaks somewhere in the middle.{/n}
"You are giving me the door. You. Everyone I have ever belonged to kept me as long as I was useful, and you are giving me the door before I have been any use at all." {n}She draws herself up.{/n}
"Then I am taking it. Do not look for me. If you ever see me again, mortal, it will be because I chose it, and you will not like the reason."''',
       c('"Choose well."', flags=(RETURNED, LEFT_FREE))),
    hz("threat", '''{n}She does not answer. The knife is in her hand before you see her reach for it, and then it is across your cheek, from the corner of your mouth to the ruin of your ear, and gone again.{/n}
"Now you own my lie." {n}Her voice is perfectly level.{/n} "Everything that has ever owned me, mortal, I have outlived: my father's seals, Yozz's leash, my sister's cell. I will outlive you too. Keep the scar. It is the last thing you will ever have from me."''',
       c("Continue", "threat_end")),
    nar("threat_end", '''{n}The air folds around her, and she is gone. You stand there with your hand to your face and blood running between your fingers, and in the morning, when you look, there is nothing on your pillow at all.{/n}''',
        c("Continue", flags=(THREATENED, CLOSED)))],
    requires=("trickster.ever", PRIMED), forbids=(RETURNED, CLOSED), delay=48, last=6, Relationship=REL, Remote=True,
    Kind="visit"))
tag(H + "guild.kept", "T")


# --- 6. Her presence in Drezen (T): the test, the collar and the second move. -------------------------------------------

GREETING = ("{n}Beside the Storyteller's shelves a tall, thin demon-woman in a high black collar stands with her arms folded, "
            "reading the spines upside down. She has been there since the morning bell. The Storyteller has stopped pretending "
            "he is not nervous, and the soldiers coming up the street step off the path when they reach her, and do not know "
            "why.{/n}")
PRESENCES = {
    # A spawned copy of her in-person unit (CutsceneNeutrals, no dialog), left of the Storyteller; Vellexia's copy stands
    # right of him at 2.0 m, so the two are 4 m apart. If the Storyteller is gone the anchor fails and
    # horzalah.presence.failed opens the night twins of the test and both commits.
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=STORYTELLER, Side="left", Distance=2.0),
                   Requires=["trickster.ever", WANTS], Forbids=[CLOSED, LEFT_FREE], MinChapter=5, MaxChapter=5,
                   AnswerLists=[], Dialog="hub", Greeting=GREETING),
}


def _resite(nodes, subs):
    """The night twin's own copy of the nodes: every street, shelf or rampart detail replaced by the Commander's room."""
    nodes = copy.deepcopy(nodes)
    for old, new in subs:
        hits = [node for node in nodes if old in node["Text"]]
        if len(hits) != 1:
            raise ValueError("night substitution must hit exactly one node: " + old)
        hits[0]["Text"] = hits[0]["Text"].replace(old, new)
    return nodes


def presence(id, title, entry, opening, nodes, requires, forbids=(), delay=24, optional=False, night=None, night_subs=(),
             **extra):
    """A scene on her presence by the Storyteller (Chapter 5). night=(opening node) also registers the <id>_night twin,
    a rest-delivered visit used only when the presence anchor failed; each forbids the other's completion."""
    SCENES.append(scene(id, title, "Horzalah", 5, entry, [opening, *nodes],
                        requires=("trickster.ever", *requires), forbids=(CLOSED, id + "_night", *forbids), delay=delay,
                        last=5, optional=optional, Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=UNIT,
                        InteractionHub=PRESENCE, **extra))
    tag(id, "T")
    if night is not None:
        # When the presence failed, or when the chain reaches Chapter 6 (the Greybor-less night after Q3 lapsed), she comes
        # to the Commander's room instead.
        SCENES.append(scene(id + "_night", title, "Horzalah", 5, "", [night, *_resite(nodes, night_subs)],
                            requires=("trickster.ever", *requires), forbids=(CLOSED, id, *forbids),
                            RequiresAnyGroups=[[PRESENCE_FAILED, "chapter.six"]],
                            delay=delay, last=6, optional=optional, Relationship=REL, Chapters=[5, 6], Remote=True,
                            Kind="visit", **extra))
        tag(id + "_night", "T")


presence(H + "test.the_gift", "A gift in the Abyss's idiom", '"Who is your friend?"',
    hz("start", '''{n}She is not alone by the shelves today. A man stands a step behind her: grey at the temples, very well dressed, with a thin gold chain running from a cuff on his wrist to a ring on her smallest finger. He keeps his eyes on the cobbles.{/n}
"Not a friend, mortal. A gift." {n}She lifts the hand with the ring, and the chain lifts with it.{/n}''',
       c("Continue", "gift")),
    [
        hz("gift", '''"Where I come from, a suitor who arrives empty-handed is a beggar, and I do not court beggars. Nor do I come as one."
"This is Yozz's dresser. For twenty years he laced that fool into his coats and powdered his wigs and told him he looked magnificent, which took more courage than anything Yozz ever did. When Yozz became my property, so did everything Yozz owned." {n}She holds out the end of the chain to you.{/n} "He is the best tailor in the Lower City. Take care not to ruin him."''',
           c('[Decline] "I don\'t collect people."', "decline"),
           c('[Free him on the spot] "Then he\'s mine to do with as I like. Take off the cuff, sir. Go home, wherever that is."',
             "free", alignment=("Good", 1)),
           c('[Accept him] "A good tailor is hard to find. I\'ll take him."', "accept", alignment=("Evil", 1))),
        hz("decline", '''{n}The chain stays in her hand. She looks at it, and then at you, and her face does something complicated.{/n}
"Nobody refuses my gifts. They are usually too afraid of what is in the box." {n}She winds the chain slowly back around her fingers until the dresser is standing at her shoulder again.{/n}
"You do not collect people." {n}She tries the words as if she were testing the edge on a blade.{/n} "Good. A collector of people I would have had to collect back, sooner or later. I have had enough owners, mortal. I do not want another one in my bed."''',
           c("Continue", "decline_end")),
        hz("decline_end", '''"He stays with me, then. He will make my collars." {n}She touches the high black leather at her throat.{/n} "He made this one. He is the only man in Alushinyrra who has ever put something round my neck that I asked for." {n}To the dresser, without looking at him:{/n} "Come."''',
           c("[Watch them go.]", flags=(TESTED,))),
        hz("free", '''{n}The dresser does not move. He looks at you, and then at her, and then at the cobbles again, as a man does who has been freed before, by someone who did not own him.{/n}
{n}Horzalah has gone very still. Her face flushes dark, from the collar up. For a heartbeat her other hand is at the knife in her belt, and the Storyteller, behind her, puts a book down very carefully.{/n}
"You gave away my gift," {n}she says softly.{/n} "In front of me. To *him*."''',
           c('"It was mine to give. You said so."', "free2")),
        hz("free2", '''{n}She draws a breath, and lets it go. Then she slips the ring off her smallest finger, chain and all, and drops it at the dresser's feet.{/n}
"You heard. Go on. Before one of us changes our mind." {n}He picks up the chain and goes, not quickly, not looking back, with the gold still hanging from his wrist.{/n}
"That is the rudest thing anyone has done to me since my sister put me in a cell." {n}She watches him go.{/n} "I find I do not mind it nearly as much. Do not do it again, mortal. I will not be so pleasant the second time."''',
           c("[Let her have the last word.]", flags=(TESTED, FREED))),
        hz("accept", '''{n}She smiles, very pleasantly, and puts the end of the chain in your hand. The dresser does not look up. He has had a great deal of practice at not looking up.{/n}
"Then we are what my father and Yozz were," {n}she says.{/n} "Two owners, doing business with the things we own. It is a respectable arrangement. It is how the Abyss is run."''',
           c("Continue", "accept2")),
        hz("accept2", '''"You will have my knives when you need them, at the Guild's rates, and you will pay on time." {n}She steps back, out of reach, the way she keeps her distance from anything she has put a price on.{/n}
"And that is all you will have. I was bought once, mortal. I know exactly what happens to a thing that is bought: it goes on a shelf. I will not go on yours."''',
           c("[Keep hold of the chain.]", flags=(ALLY,))),
    ],
    requires=(WANTS,), forbids=(TESTED, ALLY, LEFT_FREE), delay=48,
    night_subs=(("For a heartbeat her other hand is at the knife in her belt, and the Storyteller, behind her, puts a book down very carefully.",
                 "For a heartbeat her other hand is at the knife in her belt, and the candle on your table gutters as if a door had opened somewhere."),),
    night=hz("start", '''{n}The air in your room folds, and she is standing by your table, and she is not alone: a man stands a step behind her, grey at the temples, very well dressed, with a thin gold chain running from a cuff on his wrist to a ring on her smallest finger. He keeps his eyes on your floor.{/n}
"Not a friend, mortal. A gift." {n}She lifts the hand with the ring, and the chain lifts with it.{/n}''',
             c("Continue", "gift")))


_COLLAR = [
    hz("look", '''{n}She turns her face into the wind and unbuckles the high black collar, one strap and then the next, without hurrying. When it comes away, the scar is there: a band of pale, glossy skin all round her throat, two fingers wide, with the ghost of a buckle pressed into one side of it. It is the only mark left on her. Her father lifted everything else.{/n}
"The only thing on me he ever bothered to mark," {n}she says.{/n} "Not to punish. Not to hurt. Just to say *mine*."
"I am letting you see it. Look. Do not touch until I say, or you are just another buyer."''',
       c("[Wait for her word.]", "word"),
       c("[Reach for it.]", "buyer"),
       c('[Ask whose mark it is] "Whose mark is it, really? Your father\'s, or Yozz\'s?"', "brand")),
    nar("word", '''{n}You wait. The wind comes over the wall and pulls at her hair and yours. Down in the yard a sergeant is shouting the same order over and over at a line of recruits who cannot get it right. She watches your hands, and then your face, and then your hands again, and your hands do nothing at all.{/n}
{n}It takes a long time. She lets it.{/n}''',
        c("Continue", "word2")),
    hz("word2", '''{n}Then she takes your hand in hers. Her fingers are cool and dry and very strong, and she lifts your hand and lays it on the scar herself, flat, and holds it there.{/n}
{n}The skin is smoother than the rest of her, and cooler, and under it her pulse is going very fast.{/n}
"Now," {n}she says.{/n} "Now you may."''',
       c("Continue", "word3")),
    hz("word3", '''"Everyone who ever touched that, mortal, touched it to tighten something. You waited to be told." {n}Her hand stays over yours.{/n} "I have decided. Do not make that face; I decide things. It is the only way anything has ever been mine."
{n}She leans in until her mouth is beside your ruined ear, where it can be heard by the one you have left.{/n} "Tomorrow night I will come for you. Not for your head. I am going to take you somewhere nobody can sell either of us, and then we shall see what you are like when you are told."''',
       c("[Keep your hand where she put it.]", flags=(COMMITTED,)),
       c('"I\'ll be waiting."', flags=(COMMITTED,))),
    hz("buyer", '''{n}Your hand gets halfway there. Then there is a knife, flat against the inside of your wrist, cold, not cutting. You did not see her draw it.{/n}
"You reach like a buyer." {n}Her voice has gone perfectly flat.{/n} "Every man in Yozz's hall reached like that. As if it were already theirs, and they were only checking the quality."
{n}She buckles the collar back up, one strap and then the next, as unhurried as she was taking it off, and the knife goes away.{/n} "No. Not today. Perhaps not ever. I will think about whether you can be taught."''',
       c("[Let her go.]", flags=(DECLINED,))),
    hz("brand", '''{n}Her face closes, the way a book closes: all at once, with a sound.{/n}
"You looked at his brand," {n}she says,{/n} "and not at me. I take off the one thing I keep covered, and you want to know whose name is on it."
{n}She buckles the collar back up, one strap and then the next, as unhurried as she was taking it off.{/n} "It is mine, mortal. Whoever put it there. That was the whole point of showing it to you. I will think about whether you are too stupid to be worth the trouble."''',
       c("[Let her go.]", flags=(DECLINED,))),
]

presence(H + "commit.collar", "The collar", '"Walk with me."',
    hz("start", '''"Not here." {n}She glances back at the Storyteller, who is pretending to dust.{/n} "The old elf listens with both ears. Come up on your walls."
{n}She walks you up the stair to the ramparts, where the wind comes off the Worldwound with ash in it and nobody stands close enough to overhear. She stops at an embrasure and looks out over the camp for a while, as if she were counting it.{/n}''',
       c("Continue", "freed", requires=(FREED,)),
       c("Continue", "noted", requires=(SCAR_NOTED,), forbids=(FREED,)),
       c("Continue", "look", forbids=(FREED, SCAR_NOTED))),
    [
        hz("freed", '''"The dresser opened a stall by your west gate," {n}she says, without turning round.{/n} "He sells hats. He still wears the cuff. He says it is the finest gold he has ever owned, and that he is keeping it to remember." {n}Her mouth twists.{/n} "You gave away my gift, and it walked off and became a hatter. I have thought of very little else for two days. Be quiet now."''',
           c("Continue", "look")),
        hz("noted", '''"In Yozz's hall, over the bodies, you looked at this and not at the seals." {n}Her fingers are on the buckle of her collar.{/n} "I told you it was none of your business. It was not. I am about to make it so. Be quiet now."''',
           c("Continue", "look")),
        *_COLLAR,
    ],
    requires=(TESTED,), forbids=(COMMITTED, DECLINED), delay=24,
    night_subs=(("She turns her face into the wind and unbuckles the high black collar,",
                 "She turns her face to the dark window and unbuckles the high black collar,"),
                ("The wind comes over the wall and pulls at her hair and yours. Down in the yard a sergeant is shouting the same order over and over at a line of recruits who cannot get it right.",
                 "The candle burns down a finger's width. Somewhere below your window a sentry calls the hour, and later calls the next one.")),
    night=hz("start", '''{n}The air in your room folds, and she is by the window with her back to you, looking out at the lamps of the camp as if she were counting them.{/n}
"Not the Storyteller's shelves tonight," {n}she says.{/n} "The old elf listens with both ears. Your own room will do."''',
             c("Continue", "freed", requires=(FREED,)),
             c("Continue", "noted", requires=(SCAR_NOTED,), forbids=(FREED,)),
             c("Continue", "look", forbids=(FREED, SCAR_NOTED))))


presence(H + "commit.her_move", "Her move", '"Well, have you decided?"',
    hz("start", '''{n}Yesterday there was a knife in the lintel of your door, high up, pinning a note: *I am deciding. Do not come looking for me. Do not reach for anything. If you are wondering whether that means no, it does not mean anything yet.*{/n}
{n}Today she is back by the Storyteller's shelves. She does not look up when you come, and she does not answer at once. She finishes the spine she is reading, and the one after it.{/n}''',
       c("Continue", "decided")),
    [
        hz("decided", '''"A day and a night," {n}she says.{/n} "I have spent a day and a night deciding whether you are a buyer. I have watched how you speak to your soldiers, and to your quartermaster, and to that grovelling priest who still wants to put his hands on your head. I have had my people watch the rest."
"You are not a buyer. You are a clumsy {mf|man|woman} who has never been shown a thing and told to wait. That can be mended. Most things can, if you do not let a priest near them."''',
           c("Continue", "move")),
        hz("move", '''{n}She puts the book back on the shelf, spine out, exactly where it was. Then she turns and takes your hand, without asking, and draws it up under the edge of her collar, and holds it there against the band of smooth skin, where the Storyteller cannot see and everyone else can guess.{/n}
"That is how it is done," {n}she says.{/n} "I choose. Then you may. Do you understand now, or shall I cut it into you?"''',
           c("[Wait for her.]", "yes"),
           c('[Tell her to go] "I understand. And I don\'t want it. Go home, Horzalah."', "go")),
        hz("yes", '''{n}You leave your hand where she put it, and you do nothing with it at all. After a while you feel her pulse go quick against your fingers, and then quicker, and she lets out a breath through her teeth as if something had hurt her.{/n}
"Good," {n}she says.{/n} "Tomorrow night I will come for you. Not for your head. And you will wait for me exactly like that."''',
           c('"Exactly like that."', flags=(COMMITTED,))),
        hz("go", '''{n}She takes her hand away, and yours falls. For a moment she only looks at you.{/n}
"Nobody has ever sent me home before," {n}she says.{/n} "They sold me, and they kept me, and they locked me up. Nobody ever said *go home*." {n}She buckles her collar a notch tighter.{/n} "Very well. I am going. Remember that I chose to."''',
           c("[Watch her go.]", flags=(LEFT_FREE,))),
    ],
    requires=(DECLINED,), forbids=(COMMITTED, LEFT_FREE), delay=24,
    night_subs=(("She puts the book back on the shelf, spine out, exactly where it was. Then she turns and takes your hand, without asking, and draws it up under the edge of her collar, and holds it there against the band of smooth skin, where the Storyteller cannot see and everyone else can guess.",
                 "She puts your letter back on the pile, face down, exactly where it was. Then she stands, and takes your hand, without asking, and draws it up under the edge of her collar, and holds it there against the band of smooth skin."),),
    night=hz("start", '''{n}Yesterday there was a knife in the lintel of your door, high up, pinning a note: *I am deciding. Do not come looking for me. Do not reach for anything.*{/n}
{n}Tonight the air in your room folds, and she is sitting in your chair with her boots on your table, reading one of your letters. She finishes it, and the one under it, before she looks up.{/n}''',
             c("Continue", "decided")))


# --- 7. Her chamber in Alushinyrra (T): the intimacy, and the morning. ---------------------------------------------------

SCENES.append(scene(H + "visit.chamber", "Everything I own, I took", "Horzalah", 5, "", [
    nar("start", '''{n}She comes after midnight, as she said she would, through no door at all. She does not speak. She holds out her hand, and when you take it the room folds shut around the two of you like a fan, and opens again somewhere hot and dark that smells of lamp oil, ink and cold iron.{/n}''',
        c("Continue", "room")),
    nar("room", '''{n}The Guild master's chamber in Alushinyrra is long and low and lined with strongboxes: iron chests stacked to the ceiling, each with a brass plate and a name. Each one is a contract. Each one is somebody's life, bought and not yet collected. Through the floor you can hear the Guild at its business below, voices, a laugh, a scream cut off.{/n}
{n}On a shelf by the bed, on its own, sits a small box wrapped in black paper, tied with a white ribbon in a perfect bow.{/n}''',
        c("[Look at the box.]", "box"),
        c("[Read a name on one of the strongboxes.]", "names"),
        c("[Look at her.]", "her")),
    hz("names", '''{n}The nearest plate says a name you know: a Mendevian lord who dined with the Queen at your coronation. The one above it, a priest. The one above that, a name you do not know, followed by a sum that could buy a small town.{/n}
"Do not read my ledger," {n}she says from behind you, not angrily.{/n} "It is bad manners. And it will spoil your evening; you will lie awake wondering which of them you ought to warn." {n}Her hand closes on the back of your neck.{/n} "Tonight you will not warn anyone. Tonight you are not a crusader. Turn round."''',
       c("[Turn round.]", "her")),
    hz("box", '''"Yes," {n}she says, before you can ask.{/n} "It is still in there. I take it out sometimes, when the masters are being tiresome. They go very quiet." {n}She comes up behind you, close enough that you feel the heat of her through your shirt.{/n}
"Do not touch it. It is the only thing in this room I did not buy, inherit or take off a corpse."''',
       c("[Turn round.]", "her")),
    hz("her", '''{n}She is standing very close. She unbuckles the high collar and lets it drop onto the nearest strongbox, where it lands across somebody's name.{/n}
"Everything I own, I took," {n}she says.{/n} "The Guild. This room. Yozz, and his dresser, and his debts. My own name back from my sister's mouth. Everything." {n}She lifts a hand and sets her claws, very lightly, in your hair.{/n}
"You, I am asking for."''',
       c('"Then ask."', "ask"),
       c("[Say nothing. Wait for her, as she taught you.]", "wait")),
    hz("ask", '''{n}Her claws tighten in your hair, and her eyes narrow, and for a heartbeat she looks as if she might cut you for your insolence. Then she laughs, low, against your mouth.{/n}
"I just did, mortal. You were not listening. You never are, on that side."''',
       c("Continue", "threshold")),
    nar("wait", '''{n}You wait. She watches you do it, as she did on the wall, and something goes out of her shoulders that has been there, you think, for a very long time: since a collar went on, perhaps, or since a cell door closed on her in the Ivory Labyrinth.{/n}''',
        c("Continue", "threshold")),
    nar("threshold", '''{n}She kisses you like a woman taking something she has decided is hers: slowly, thoroughly, with her claws holding your head exactly where she wants it. Her mouth goes from yours to your jaw, and along it, and finds the puckered ruin where your ear used to be, and stays there, her breath hot on the scar, her tongue tracing the edge of it as though she were reading her own signature.{/n}
{n}Your hands find the laces of her leathers, and she lets you undo them, one at a time, and says nothing, and then says, "Faster," and you are.{/n}''',
        c("Continue", "threshold2")),
    nar("threshold2", '''{n}She is lean and hard and very hot under your hands, all long muscle and sharp bone, and there is not a brand or a seal left on her anywhere; her father took them all back. There is only the band of pale skin around her throat. When your mouth finds it she makes a sound you would not have believed she could make, and her claws go down your back, not quite gently.{/n}
"Mine," {n}she says into your hair.{/n} "The ear, and the rest of you with it. Say it."''',
        c('"Yours."', "cut"),
        c('"Tonight, anyway."', "cut_tonight")),
    nar("cut", '''{n}She pulls you down onto the bed among the strongboxes, and rolls you under her, and the ribboned box watches from its shelf, and below you the Guild goes on about its business and never once looks up.{/n}''',
        c("Continue", "morning")),
    nar("cut_tonight", '''{n}"We will see about tonight," she says, and bites your shoulder for it, and pulls you down onto the bed among the strongboxes, and rolls you under her. The ribboned box watches from its shelf. Below you, the Guild goes on about its business and never once looks up.{/n}''',
        c("Continue", "morning")),
    nar("morning", '''{n}There is no dawn in the Guild master's chamber; there are no windows. There is a bell, somewhere below, that rings for the change of watch, and she is already up when it does, buckling on her collar in front of a mirror of black glass.{/n}
{n}She does not send you home the way she brought you. She walks you down the main stair, past the masters' tables, past the notice board with its contracts and its one empty patch of wall where a box was pinned, to the front door, in full view of every knife in the Guild.{/n}''',
        c("Continue", "morning2")),
    hz("morning2", '''{n}Nobody speaks. Somebody drops a cup. At the top of the stair she snaps her fingers once, not loudly, and the grey-bearded master nearest the stair looks at her, and at you, and puts down his quill and stands. Then all of them are standing, because the alternative is to be the one who did not.{/n}
"Let them look," {n}she says, at the door, quietly enough that only you hear it.{/n} "They know whose ear is in that box. Now they know whose the rest of you is. It will do them good." {n}She opens the door on the red light of the Middle City.{/n} "Go back to your war, Knight Commander. I will come for you when I choose."''',
       c('"I\'ll be waiting."', flags=(CHAMBER, MORNING)),
       c("[Kiss her in the doorway, where they can all see.]", "doorway")),
    hz("doorway", '''{n}She lets you. She even, for a moment, lets you hold her there, in her own doorway, in front of her whole Guild, with the Middle City going by in the street behind you and a demon in a litter craning its neck to stare.{/n}
"Showing off," {n}she says, when she has decided it is enough. Her eyes are very bright.{/n} "That is my trade, mortal. Leave it to me. Go."''',
       c("[Go.]", flags=(CHAMBER, MORNING)))],
    requires=("trickster.ever", COMMITTED), forbids=(CHAMBER, CLOSED), delay=24, last=6, Relationship=REL, Remote=True,
    Kind="visit"))
tag(H + "visit.chamber", "T")


# --- 8. Epilogue pages (Owner HorzalahEpilogue, Chapter 6; no effects, no page Requires another). ------------------------

EP = dict(last=6, Relationship=REL)
SAC = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})   # H2 (Last Call's bottle) as well as the native endings
COMMON = (
    p("{n}The Commander never let a priest touch the side of that head. In later years people who had never been to the Abyss would stare at the puckered scar where an ear had been, and the Commander would tell them it was a gift, and let them decide whether that was a joke.{/n}", requires=(EAR,)),
    p("{n}In Drezen they still tell the story of the night a demon walked past every sentry in the citadel and out again with a piece of the Knight Commander, and in Alushinyrra they tell it better.{/n}", requires=(LATE,)),
    p("{n}Somewhere at the bottom of the Commander's pack, all through the war and long after it, there was an empty box tied with a white ribbon. Nobody was ever allowed to open it. There was nothing in it. That was, the Commander said, the whole point.{/n}", requires=(BOX_KEPT,)),
    p("{n}A hatter by the west gate of Drezen wore a gold cuff on his wrist to the end of his days, and sold very good hats, and never once said a word against the woman who had given him away.{/n}", requires=(FREED,)),
)

SCENES.append(scene(H + "epilogue.together", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}Horzalah kept the Assassins' Guild of Alushinyrra long after the war, through three attempts on her chair and more on her life than anyone bothered to count. On the notice board in her hall, among the contracts, a small box with a white ribbon hung for years in a place of honour. No master of the Guild ever took down a contract on the Knight Commander. Several were offered. None of them was accepted twice.{/n}
{n}Baphomet never spoke of his younger daughter again, to anyone. She never spoke of him either. When the Lord of Beasts' name was mentioned in her hall, she would touch the high black collar at her throat, and smile, and change the subject.{/n}
{n}She came to Drezen when she chose, through no door at all, and she left the same way. Nobody who knew her ever called what was between her and the Commander anything. She would not have let them. But every master in her Guild knew whose ear was in the box, and every sentry in Drezen learned to step off the path when a thin woman in a collar walked it, and not to ask why.{/n}''',
        paragraphs=(*COMMON,
                    p("{n}Her assassins remembered the morning the Knight Commander walked down the Guild's main stair and out of the front door, and the masters remembered standing up for it. It was, they agreed afterwards, the most frightening thing any of them had ever seen her do.{/n}", requires=(MORNING,)),
                    p("{n}The Commander never once reached for her collar. She took the Commander's hand and put it there herself, whenever she chose, and she chose more often than anyone in Alushinyrra would have believed.{/n}", forbids=(DECLINED,)),
                    p("{n}The Commander learned to wait. She said it took the longest of any lesson she had ever taught, and that she had once taught a wizard's apprentice to hold his breath until he died.{/n}", requires=(DECLINED,)),
                    p("{n}On the night before the Threshold there was a knife in the pole of the Commander's tent, above the Commander's head, pinning a sheet of black paper tied with a badly tied bow. The bets in her hall stood at eleven days, it said. She had placed none. She had bought up, through third parties, every wager that the Commander would not come back, so that she would be very rich and very angry, or a great many demons would owe her money and never know why. *Come back with everything else attached. I have one piece of you. I do not intend to settle for it.*{/n}"),
                    p("{n}She wore a white ribbon at her collar in her hall every day of her reign, tied in a bow that was very slightly lopsided. No master of the Guild ever mentioned it. The Commander tied it, when the Commander was there, and practised on the maps when not.{/n}", requires=(P_RIBBON,)),
                    p("{n}The Commander carried a very thin knife with no maker's mark through the rest of the war and never once cleaned it. Horzalah said that was the most romantic thing anyone had ever done for her, and that she would kill anyone who repeated it.{/n}", requires=(P_KNIFE,)),
                    p("{n}A certain dwarf never did get his whistle back. It hung at Horzalah's throat on a white ribbon for years, and whenever he came into a room where she was, she would lift it to her lips, and not blow it, and neither of them ever said a word about it.{/n}", requires=(P_WHISTLE,)),
                    p("{n}She never said what she had come to the Commander's room to do on the night she came alone. She did not have to. She kept the knife she had brought, and it hung over the bed in her chamber, and the Commander slept beneath it more soundly than anywhere else in the world.{/n}", requires=(CAME,))))],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"), **SAC, **EP))
tag(H + "epilogue.together", "T")

SCENES.append(scene(H + "epilogue.commit", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Horzalah had finished thinking about what she wanted. She finished it anyway, the spring after the Threshold, in her own time and on her own terms.{/n}
{n}She came to Drezen through no door at all, stood in the Commander's rooms until she was noticed, and unbuckled her collar. The Commander waited, as the Commander had learned to do around her, and she took the Commander's hand and put it on the scar herself.{/n}
{n}She brought a gift, as she had always meant to: a grey-haired man on a thin gold chain, Yozz's dresser, held out across the Commander's table. What the Commander did with the chain, she never told anyone. She only ever said that she had been bought once, and knew what a buyer looked like, and had not seen one.{/n}
{n}That night she did not leave. She let the Commander unbuckle her collar, and every lace after it, and when the last of her leathers was on the floor she took two fistfuls of the Commander's shirt and fell back onto the bed and pulled the Commander down with her, and the candle went out.{/n}
{n}After that she came and went as she pleased, and nobody in Drezen was ever quite sure whether she was a guest, a visitor or a threat, and nobody dared to ask her which. In the Guild's hall in Alushinyrra, a small box with a white ribbon hung on the notice board in a place of honour, and the masters who had known what was in it grew old and careful in her service.{/n}''',
        paragraphs=(p("{n}Before the Threshold there had been a note, pinned to the pole of the Commander's tent by a knife: *I have not finished thinking about what I want. You are going to your war before I have finished. That is very inconsiderate of you. Come back, and I will tell you.* The Commander came back. She told.{/n}"), *COMMON))],
    requires=("trickster.ever", LATE_COMMITTED),
    forbids=(COMMITTED, DECLINED, LEFT_FREE, ALLY, CLOSED, "sacrifice"), **SAC, **EP))
tag(H + "epilogue.commit", "T")

SCENES.append(scene(H + "epilogue.decided", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}Horzalah took a long time to decide whether the Commander could be taught. The war ended first. She went on deciding in Alushinyrra, in her own hall, among the contracts, with the ribboned box on the notice board where every master could see it.{/n}
{n}In the spring she came to Drezen through no door at all and found the Commander at the window. She did not say what she had decided. She took the Commander's hand, without asking, and put it under the edge of her collar, and held it there until the Commander understood, and waited.{/n}
{n}She said afterwards that it was the slowest lesson she had ever given, and the only one she had ever given for nothing.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, LEFT_FREE, CLOSED, "sacrifice"), **SAC, **EP))
tag(H + "epilogue.decided", "T")

SCENES.append(scene(H + "epilogue.left_free", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}Horzalah kept the Assassins' Guild of Alushinyrra long after the war, and kept it well. Her father never spoke of her. She was seen in the Midnight Isles and in Absalom and once, it is said, in Katapesh, on business nobody ever lived to describe. She owned a great many people, and a great many more feared that she would. Nobody owned her.{/n}
{n}Once, years after the Threshold, a small box wrapped in black paper arrived in Drezen with no note. It was tied with a white ribbon in a perfect bow, the ends cut on the slant so they would not fray. Inside, on black silk, there was nothing at all.{/n}
{n}The Commander understood it perfectly.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", LEFT_FREE), forbids=(COMMITTED,), **EP))
tag(H + "epilogue.left_free", "T")

SCENES.append(scene(H + "epilogue.ally", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}Horzalah served the Commander to the end of the war at the Guild's rates, and not a day longer. Her knives were always where the Commander needed them, and her bills were always paid on time, and she never once came through a door without knocking.{/n}
{n}The Commander kept Yozz's dresser, who was very good at his work and never looked up. Horzalah never asked after him. When the war was over she closed the account in person, took her last payment, and went back to Alushinyrra, and she never spoke to the Commander again. She had been bought once. She knew exactly what happened to things that were bought.{/n}''',
        paragraphs=COMMON)],
    requires=("trickster.ever", ALLY), forbids=(CLOSED, COMMITTED), **EP))
tag(H + "epilogue.ally", "T")

SCENES.append(scene(H + "epilogue.scarred", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}The Commander carried two scars from Horzalah for the rest of a long life: the ruin of an ear, and a thin white line from the corner of the mouth to meet it. The first was a gift. The second was a receipt.{/n}
{n}Nobody ever saw her again. The Guild in Alushinyrra went on under a master who never showed her face, and once, years later, a contract on the Commander's head appeared on its notice board, was taken down that same night, and never appeared again. Nobody knew what it meant. The Commander thought about it often.{/n}''')],
    requires=("trickster.ever", THREATENED), **EP))
tag(H + "epilogue.scarred", "T")

SCENES.append(scene(H + "epilogue.closed", "", "HorzalahEpilogue", 6, "", [
    nar("page", '''{n}Horzalah kept the Assassins' Guild of Alushinyrra, or it kept her; nobody in the Midnight Isles was ever quite sure which. The Commander never saw her again.{/n}
{n}For years afterwards the sentries on the Commander's door were doubled every night, on the Commander's own order, and every night nothing came through it. The Commander said that was the point, and slept badly anyway.{/n}''',
        paragraphs=(p("{n}Somewhere in Alushinyrra, on a shelf in a master's chamber, a small box with a white ribbon sat unopened for a very long time. The Commander never asked what she had done with it.{/n}", requires=(EAR,)),))],
    requires=("trickster.ever", STARTED, CLOSED), forbids=(COMMITTED, THREATENED, KILLED_UNMET), **EP))
tag(H + "epilogue.closed", "T")


# --- 9. Reactions (named companions with a stake: Greybor, whose contract she held; Wenduag). ------------------------------

GREY_GUARD = dict(forbids=GREY_GONE)
# Wenduag must be with the Commander to speak on her own list. Her Trickster return (wenduag.trickster.returned) has no
# producer until her route is built (the build rejects an override value nothing sets), so the G6 return override is added
# with her route (R6); until then a killed or dismissed Wenduag simply has no line, as in every merged route's guard.
WEN_GUARD = dict(forbids=("wenduag.killed", "wenduag.kicked_out"))
WEN_IN = "wenduag.in_party"

SCENES.append(reaction("Greybor", H + "react.greybor_witness", ("trickster.ever", GREY_IN, EAR, MET_A),
    '''{n}Greybor runs a whetstone along a blade, slowly, with the particular care of a man who has decided not to look at the side of your head.{/n}
"I have seen a great many deals struck over a beaten enemy, Commander. Gold for a life. A name for a life. Once, a very good horse." {n}He turns the blade to the light.{/n} "I have never before seen the loser walk off with a piece of the winner, wrapped with a bow, and the winner pleased about it."
"I saw nothing on that road, of course. I value my reputation too much to have seen anything. But if anyone ever asks me who took the Knight Commander's ear, I will tell them it was Horzalah, and that she was magnificent, and I will charge them for the story."''',
    answer_list=GREYBOR_LIST, chapter=5, last=5, entry='"About Horzalah."', portrait="Greybor", **GREY_GUARD))
tag(H + "react.greybor_witness", "T")

SCENES.append(reaction("Greybor", H + "react.greybor_ear", ("trickster.ever", GREY_IN, EAR),
    '''{n}Greybor studies the side of your head without a word, the way he looks at a job someone else botched.{/n}
"Horzalah. The one who put a price on you in Alushinyrra." {n}He sets down the whetstone.{/n} "They say in the taverns she took that and let you live. They say it like a song. Somebody in that Guild is paying for the song, Commander, and it is not you."
"A professional takes the head, or takes nothing. An ear is a signature." {n}He picks the whetstone up again.{/n} "I would very much like to know what you bought with it. No, don't tell me. I would only have to charge you for keeping quiet."''',
    answer_list=GREYBOR_LIST, chapter=5, last=5, entry='"About Horzalah."', portrait="Greybor",
    forbids=(*GREY_GONE, MET_A)))
tag(H + "react.greybor_ear", "T")

SCENES.append(reaction("Wenduag", H + "react.wenduag_morning", ("trickster.ever", WEN_IN, MORNING),
    '''{n}Wenduag watches the thin demon-woman in the collar, whenever she appears in the citadel, the way a hunter watches a wolf that has left its pack and not died of it.{/n}
"You went down into her den, {mf|master|mistress}, and she walked you out of the front door in front of all her killers. In the Darklands we did that with a captive we meant to keep. We showed the whole tribe, so no one would try to take it." {n}A grim, approving grin.{/n}
"Her own father threw her away. She took his leavings and made a knife of them. I know that walk." {n}Her eyes narrow.{/n} "Do not turn your back on her. I would think less of her if she let you."''',
    answer_list=WENDUAG_HUB, chapter=5, last=5, entry='"The woman in the collar."', portrait="Wenduag", **WEN_GUARD))
tag(H + "react.wenduag_morning", "T")

SCENES.append(reaction("Wenduag", H + "react.wenduag_gift", ("trickster.ever", WEN_IN, FREED),
    '''{n}Wenduag is sharpening a blade. She does not stop.{/n}
"The soldiers say you gave away a slave the demon brought you. Unchained him in front of her." {n}The whetstone scrapes.{/n} "In the Darklands a gift is a test. If you give it away, you are saying the giver is weak."
"And she let you live." {n}She tests the edge on her thumb and looks at you with something like respect, and something like pity.{/n} "Then she wants you very badly, {mf|master|mistress}. That is more dangerous than if she hated you. I would know."''',
    answer_list=WENDUAG_HUB, chapter=5, last=5, entry='"Something on your mind?"', portrait="Wenduag", **WEN_GUARD))
tag(H + "react.wenduag_gift", "T")


SCENES.append(reaction("Greybor", H + "react.greybor_morning", ("trickster.ever", GREY_IN, MORNING),
    '''{n}Greybor does not look up from the whetstone.{/n}
"Word came up the Wound roads from Alushinyrra, Commander. They say the masters of the Assassins' Guild stood up from their tables when you came down the main stair of her hall, at a snap of her fingers, and that nobody in that Guild has stood up for anyone in a hundred years, snap or no snap." {n}The stone scrapes.{/n}
"I have been inside that hall. I know those tables. They do not stand for anyone, not for the Lady in Shadow's own messengers." {n}He finally looks at you.{/n} "Whatever you did in there, do not ever do it to me. I would not survive the embarrassment."''',
    answer_list=GREYBOR_LIST, chapter=5, last=6, entry='"About Horzalah."', portrait="Greybor", forbids=GREY_GONE))
tag(H + "react.greybor_morning", "T")

SCENES.append(reaction("Wenduag", H + "react.wenduag_ally", ("trickster.ever", WEN_IN, ALLY),
    '''{n}Wenduag watches the grey-haired man who follows you now, two steps behind with his eyes on the ground and a gold cuff on his wrist.{/n}
"You took a slave from the demon-woman." {n}She says it without judgement, the way she would say you took a sword off a corpse.{/n} "In the Darklands we would say you won. She gave, you took; you are stronger."
"But she does not look at you like a woman who lost, {mf|master|mistress}. She looks at you like a merchant who has just been paid." {n}Her eyes narrow.{/n} "Be careful what else she sells you."''',
    answer_list=WENDUAG_HUB, chapter=5, last=5, entry='"You\'re watching my new servant."', portrait="Wenduag", **WEN_GUARD))
tag(H + "react.wenduag_ally", "T")


SCENES.append(reaction("Greybor", H + "react.greybor_amateur", ("trickster.ever", GREY_IN, CAME),
    '''{n}Greybor looks at the new mortar on your door frame, where the guards took an axe to it to get in, and then at the side of your head.{/n}
"She came in person. To your bedchamber. Alone." {n}He shakes his head slowly, with the pained expression of a craftsman looking at somebody else's joinery.{/n}
"A master of the Guild. Doing her own work, at night, without a second knife on the stair." {n}He shakes his head again.{/n} "And you let her walk out with a piece of you. I have no idea which of you is the bigger amateur, Commander, and I would pay good money to find out."''',
    answer_list=GREYBOR_LIST, chapter=5, last=6, entry='"About Horzalah."', portrait="Greybor", forbids=(*GREY_GONE, MET_A, MET_B)))
tag(H + "react.greybor_amateur", "T")

SCENES.append(reaction("Wenduag", H + "react.wenduag_cheek", ("trickster.ever", WEN_IN, THREATENED),
    '''{n}Wenduag looks at the new cut on your face, from the corner of your mouth to where your ear used to be, and does not laugh, which is worse.{/n}
"You threatened the demon-woman, and she did that, and left." {n}She nods slowly.{/n} "In the Darklands we would say you were lucky. She could have taken your throat. She took your face instead, so you would remember every morning in the water."
"You tried to put a collar on her, {mf|master|mistress}. I know what that looks like from the other side." {n}Her voice goes flat.{/n} "She did right."''',
    answer_list=WENDUAG_HUB, chapter=5, last=6, entry='"Something on your mind?"', portrait="Wenduag", **WEN_GUARD))
tag(H + "react.wenduag_cheek", "T")


# --- Registration --------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the relationship's own native read (Greybor's failed Q3), its Derived keys (they extend the merged
    trickster_world keys and bind before them), its presence and its portrait fallback. Scenes are added by expansion.py;
    the verified world keys (horzalah.*, greybor.*, baphomet.named_horzalah...) bind on demand in trickster_world."""
    _bind(payload, "SeenCues", SEEN_CUES)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    # trickster_world binds a Derived key's sources only when it binds the key itself; these keys bind here first, so their
    # verified native sources (horzalah.killed, greybor.dead, chapter.six...) are bound here from the same table.
    from storylines import trickster_world
    for key in sorted({k for groups in DERIVED.values() for g in groups for k in g}):
        if key in trickster_world.BINDINGS:
            kind, guid, _ = trickster_world.BINDINGS[key]
            value = [guid] if kind in trickster_world.LIST_KINDS and isinstance(guid, str) else guid
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != value:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = value
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)
    payload.setdefault("PortraitFallbacks", {}).setdefault("Horzalah", PORTRAIT_GUID)
