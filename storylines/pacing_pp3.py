"""Pacing pass PP3 (Writer/handoffs/13-PACING-PASS.md sections 2, 2a, 2b, 4, 7 and the PP3 addendum): Aranka, Nurah, Jannah.

Early beats, each one native moment with a real choice for her, plus Nurah's Chapter 4 packet; and the later scene in her
merged route that reads each one (the consequence, appended here; choices are append-only). Ids are save references.
Path tags (13 errata 2026-09-29): every early beat is N-all (no Trickster gate, no romance promise, no native key set);
the Chapter 4 packet is T (her prison branch of the Trickster route). Ember is paused (v2) and is not touched here.

Hosts (each list is referenced by one dialog only; blueprint reference scan, 2026-10-01). Return-to-list beats carry no
checks (Rules.Validate, E14b); the two Nurah beats return to a clean native cue (retcheck OK, replay text read) and keep theirs.
  aranka.early.duet    Chapter 1, Count Arendae's party house: DesnaAdept2 AnswersList_0002 2373bef6, her hub for the whole
                       visit. Pinned against the one moment it must not follow: the bards' contest WON (Cue_15 dd66b8ab, she
                       is outmatched and needs to rescue nothing). After a failed contest (Cue_0015 2c10c9d0, "your voice
                       sounds clumsy and uncertain"; its OnShow gives a potion, so retcheck UNSAFE) she picks up the very song
                       the Commander chose (SelectedAnswers Answer_0006 / Answer_0007 / Answer_9). A Commander who never sang
                       (the contest is offered only to Performers, ClassGroups/Performers 9267ebac) is invited to one verse,
                       and the smoke of the burning city cracks it. Return-to-list: Cue_14 b58f507c and Cue_0013 ff8b18ff
                       are clean (retcheck OK) but replay her "never mind" and her "stick around here" lines, so ReturnToList.
  nurah.early.hands    Chapter 2, the cornered branch after the siege (every path): Nurah_After_Battle AnswersList_0018
                       f392d579 (her verdict list; opened by Cue_0001 a8f5baca, "wipes her bloody hands on her clothes").
                       Return Cue_0022 9b8d5443, "Spare me the sermon... don't try to get into my head!"; retcheck OK, and
                       every terminal choice is a Commander line it answers.
  nurah.early.hanging  Chapter 2, the accomplice branch (NurahIsOurFriendNow 5301ffc4, set by Final_Battle_Before
                       Answer_0026): AnswersList_0003 2ce412d7, pinned after "Stay with me" (SelectedAnswers Answer_0005
                       9f05ff7a -> Cue_0010 3e3e02b2, "They'll drag me out of my tent some night and hang me from a tree").
                       Return Cue_0016 217204ec, "What's wrong with you? What do you really want?"; retcheck OK.
  jannah.early.laugh   Chapter 1, the League's table at the Defender's Heart: Ch1_SeelahMeetsFriends AnswersList_0033
                       7d40d237 (the getting-to-know-you list), pinned after "Have you been serving in the Eagle Watch for
                       long, Jannah?" (SelectedAnswers Answer_0034 d01295db -> her own Cue_0038 6428870e, "Am I lucky, or
                       what?"). ReturnToList, because the clean Ch1_SeelahMeetsFriends/Cue_0049 f66ef6e1 replays her Mivon introduction.
  jannah.early.bout    Chapter 2, the Houndheart camp, on arrival: Seelah Q1 KnightCamp AnswersList_0008 9995876f (after
                       Elan's Cue_0007; Jannah's own tease is Cue_0005 4cce7d43). ReturnToList, because KnightCamp/Cue_0014 ed2d60fd is
                       Elan's apology and KnightCamp/Cue_0011 2100f41a continues (retcheck UNSAFE).
  nurah.trickster.abyss.sky  Chapter 4, remote: a packet she slipped into the Commander's map case on one of her pardoned
                       night walks (night_out), opened at the first camp in the Abyss (c4 Nexus_Camp/HeraldLetsGo Cue_0018
                       ef968178; no courier crosses the planes, the PP5 precedent).
Retcheck (Writer/tools/retcheck.py, 2026-10-01): f392d579:9b8d5443 OK, 2ce412d7:217204ec OK, 2373bef6:2c10c9d0 UNSAFE
(cue.OnShow, AddItemToPlayer of the healing potion), 2373bef6:ff8b18ff and 2373bef6:b58f507c OK (incoherent replays),
7d40d237:f66ef6e1 OK (replays her introduction).
The night_out recall nodes repeat that scene's own four answers (tempers and the ownership refusal, cost.owned_line), so
the flags they set are the scene's existing outcomes, not new producers.
Consequences (one observable later change each): aranka.trickster.verse.duet (+ yard copy) node duet, four appended billing
answers; nurah.trickster.prison.night_out (+ its Chapter 5 twin) node start, six appended answers to "Why?"; Nurah's book
pages (the_margin, book_only, unanswered, bereaved, refused) one paragraph per sky; jannah.trickster.alive.stories node
start, five appended lines (the first meeting in her cell in every living world).
Not built: Jannah Chapter 4 (no canon moment: she is a deserter in a Drezen cell, gone from the Scar, or dead, and nothing
of hers can reach the Abyss; exception proposed to the coordinator). Aranka Chapter 4 (absent off the Azata path).
"""
from story_format import c, n, p, scene
from storylines.nurah_trickster import tempers

SCENES = []

# Hosts and returns.
ADEPT_LIST = "2373bef62ea65d741a8f54ba95f9a8b2"      # c1/KenabresBurning/OraclePartyHouse/DesnaAdept2/AnswersList_0002
SIEGE_CORNERED = "f392d579b9aac6947b65a2473775ffc9"  # c2_vs/DrezenSiege/Nurah_After_Battle/AnswersList_0018
SIEGE_SERMON = "9b8d54436ef3a9a4597223caacb31e71"    # Nurah_After_Battle/Cue_0022 "Spare me the sermon..." (clean)
SIEGE_FRIEND = "2ce412d70ca0f40468252bec95ab2881"    # Nurah_After_Battle/AnswersList_0003 (NurahIsOurFriendNow branch)
SIEGE_WHAT = "217204ecd2fdaa74ab397f04a30acc77"      # Nurah_After_Battle/Cue_0016 "What do you really want?" (clean)
TABLE_LIST = "7d40d23732cd28b4db2079945eadb89e"      # Seelah Q1 Ch1_SeelahMeetsFriends/AnswersList_0033
CAMP_LIST = "9995876fa83c0f049a84df4ca349f4af"       # Seelah Q1 KnightCamp/AnswersList_0008

ARANKA_UNIT = "b85fdd8481f26f54f9c504fc4d2e031f"     # Units/.../KenabresBurning/Aranka_DesnaPriest
JANNAH_DH = "588418cb0dfd7cb45b6e6d370ef42bea"       # Units/.../DefendersHeart/DH_SeelasFriend_DeserterJanna
JANNAH_CAMP = "4880d0b16ca74fa46a167914e2b44bcc"     # Units/.../Seelah_Q1/CR4_DeserterJanna (her KnightCamp cues)
SEELAH = "54be53f0b35bf3c4592a97ae335fe765"          # Units/Companions/Seelah/Seelah_Companion

# Native keys read (bound in trickster_world.BINDINGS).
VOICE_FAILED = "aranka.kenabres_voice_failed"        # SeenCues DesnaAdept2/Cue_0015
CONTEST_WON = "aranka.kenabres_contest_won"          # SeenCues DesnaAdept2/Cue_15
SONG_MARCH = "aranka.kenabres_song_march"            # SelectedAnswers DesnaAdept2/Answer_0006
SONG_TAVERN = "aranka.kenabres_song_tavern"          # SelectedAnswers DesnaAdept2/Answer_0007
SONG_BALLAD = "aranka.kenabres_song_ballad"          # SelectedAnswers DesnaAdept2/Answer_9
SONGS = (SONG_MARCH, SONG_TAVERN, SONG_BALLAD)
ASKED_TO_STAY = "nurah.siege_asked_to_stay"          # SelectedAnswers Nurah_After_Battle/Answer_0005 "Stay with me."
ASKED_SERVICE = "jannah.asked_watch_service"         # SelectedAnswers SeelahMeetsFriends/Answer_0034

# Outcome flags: every terminal path sets exactly one; every first-node choice sets the beat's .seen.
DUET = "aranka.early.duet."
DUET_OUT = tuple(DUET + v for v in ("shared", "stolen", "hers", "declined"))
HANDS = "nurah.early.hands."
HANDS_OUT = tuple(HANDS + v for v in ("bound", "fumbled", "rag", "bled"))
HANGING = "nurah.early.hanging."
HANGING_OUT = tuple(HANGING + v for v in ("promised", "doubted", "bargained"))
LAUGH = "jannah.early.laugh."
LAUGH_OUT = tuple(LAUGH + v for v in ("honest", "bravado", "let_be"))
BOUT = "jannah.early.bout."
BOUT_OUT = tuple(BOUT + v for v in ("accepted", "deferred", "refused"))
SKY = "nurah.trickster.abyss.sky"
SKY_OUT = tuple(SKY + "_" + v for v in ("plain", "pretty", "blank"))

BEATS = {"aranka.early.duet": DUET_OUT, "nurah.early.hands": HANDS_OUT, "nurah.early.hanging": HANGING_OUT,
         "jannah.early.laugh": LAUGH_OUT, "jannah.early.bout": BOUT_OUT}

# Nurah's route keys (nurah_trickster), read only.
RELEASED = "nurah.trickster.released"
ACCEPTED = "nurah.trickster.accepted"
RETURNED = "nurah.trickster.returned"
COMPLETE = "nurah.complete"
CLOSED = "nurah.closed"
DEATHS = ("nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism")


def seen(beat):
    return beat + ".seen"


def beat(id, title, owner, chapter, entry, nodes, relationship, outcomes, exclusive=(), **extra):
    """One early beat: its host chapter only, optional, once (its own outcomes and .seen forbidden)."""
    forbids = tuple(extra.pop("forbids", ())) + (seen(id),) + tuple(outcomes) + tuple(exclusive)
    requires = extra.pop("requires", ())
    SCENES.append(scene(id, title, owner, chapter, entry, nodes, requires=requires, forbids=forbids, last=chapter,
                        optional=True, Relationship=relationship, Chapters=[chapter], **extra))


def ara(id, text, *choices):
    return n(id, "Aranka", text, *choices, portrait="Aranka", speaker_unit=ARANKA_UNIT)


def nu(id, text, *choices):
    return n(id, "Nurah", text, *choices, portrait="Nurah")


def jan(id, text, *choices, unit=JANNAH_DH):
    return n(id, "Jannah", text, *choices, portrait="Jannah", speaker_unit=unit)


def page(id, speaker, text, *choices):
    """A node of a reading scene on a presence hub: spoken like its neighbours there (no inline speaker unit)."""
    return n(id, speaker, text, *choices, portrait=speaker)


# --- Aranka, Chapter 1: "Keep the rhythm" -----------------------------------------------------------------------------
# Her agency: she carries the tune, and at the last line she decides whether to hand it back or take it.

S = seen("aranka.early.duet")
DUET_CHOICES = (
    c("[Keep the rhythm, and let her carry the tune.]", "shared"),
    c("[Take the tune back. You can carry it.]", "stolen"),
    c("[Beat time on the table, and let her have the verse.]", "hers"),
    c('"Once was enough for one day."', "declined"),
)
beat("aranka.early.duet", "Keep the rhythm", "Aranka", 1, '"Sing with me. One verse, properly."', [
    n("start", "Narrator", '''{n}The young bard's eyebrows go up, and so does one corner of her mouth.{/n}''',
      c("Continue", "march", flags=(S,), requires=(VOICE_FAILED, SONG_MARCH)),
      c("Continue", "tavern", flags=(S,), requires=(VOICE_FAILED, SONG_TAVERN), forbids=(SONG_MARCH,)),
      c("Continue", "ballad", flags=(S,), requires=(VOICE_FAILED, SONG_BALLAD), forbids=(SONG_MARCH, SONG_TAVERN)),
      c("Continue", "cracked", flags=(S,), requires=(VOICE_FAILED,), forbids=SONGS),
      c("Continue", "fresh", flags=(S,), forbids=(VOICE_FAILED,)),
      portrait="Aranka"),
    ara("march", '''"Properly? After that?" {n}She laughs, not unkindly, and before you can take it back she is singing your own march at you, half a beat slower and a little higher, so that it stops sounding like a parade ground and starts sounding like a song.{/n} "Let's go along, a proper song strikes harder than a spear..."
{n}She breaks off and points at you.{/n} "Your words are fine. Your breath ran out on 'spear', that's all. Keep the rhythm. I've got the words."''', *DUET_CHOICES),
    ara("tavern", '''"The one about the seventh pint?" {n}She is already tapping it out on the back of a gilded chair, and then she sings it back at you, swinging it the way a drinking song ought to swing.{/n} "I've met some demons from far and near..."
"You were rushing. Nobody rushes the seventh pint." {n}She grins.{/n} "Keep the rhythm. I've got the words."''', *DUET_CHOICES),
    ara("ballad", '''"The ballad?" {n}Her cheeks go pink, and she does not seem to mind in the least.{/n} "Oh, that one deserves a second chance."
{n}She sings your line back to you, soft where you were loud, and holds the last note until the Count's crystal hums along with it.{/n} "From death I have delivered this wonderful creation... That's how it goes when you mean it. And if the wonderful creation is me, I'd like it sung better."
"Keep the rhythm. I've got the words."''', *DUET_CHOICES),
    ara("cracked", '''"Properly? After that?" {n}She laughs, not unkindly, and hums your tune back at you, half a beat slower, until it starts to sound like something.{/n}
"Your words are fine. Your breath ran out, that's all. Keep the rhythm. I've got the words."''', *DUET_CHOICES),
    ara("fresh", '''"One verse? With the whole of Kenabres on fire?" {n}She looks past you at the glow over the rooftops, and back, and her blue eyes are glittering.{/n} "That's exactly when."
{n}She sings a line she seems to be making up as she goes, about a hard day and a warm song, simple and a little awkward and somehow charming, and nods at you to take the next. You try. The smoke you have been breathing all day has scraped your throat raw, and the note comes out cracked in two.{/n}
"Oh, that's the smoke, not you." {n}She waves it away.{/n} "Keep the rhythm. I've got the words."''', *DUET_CHOICES),
    ara("shared", '''{n}You keep the rhythm. She carries the words, and the tune with them, and you discover that a cracked voice sounds a great deal less cracked with hers laid over it. At the last line she stops dead, eyebrows up, and holds the gap open for you like a door.{/n}
{n}You land it. Not beautifully. On the note.{/n}
"There!" {n}She claps her hands.{/n} "That's what a last line is for. Somebody has to finish it who didn't think they could."''',
        c("[Bow to her.]", flags=(DUET + "shared",))),
    ara("stolen", '''{n}You take the tune back. For two lines it holds. On the third it cracks in exactly the same place, as if the note had been lying in wait for you.{/n}
{n}Aranka doesn't let it fall. She sweeps the verse out from under you and sings the rest herself, much louder than the room needs, finishes on a flourish nobody wrote, and winks at you over the last note.{/n}
"Sorry! It was about to land on the floor, and I can't bear it when they land on the floor. You can have the next one."''',
        c('"I\'ll hold you to that."', flags=(DUET + "stolen",))),
    ara("hers", '''{n}You beat time on the table with the flat of your hand. She hesitates half a breath, understands, and sings it alone.{/n}
{n}It is a simple verse, and she sings it as though the house were full and every seat paid for. When she finishes she stays quite still, listening to the last of it go.{/n}
"You let me have it." {n}She sounds surprised.{/n} "Most people want the last line. I'll remember that."''',
        c("[Smile, and say nothing.]", flags=(DUET + "hers",))),
    ara("declined", '''"Fair!" {n}She laughs and lifts her cup to you instead.{/n} "Then I'll keep your verse for you until you want it back. I'm very good at keeping songs. It's half of what I'm for."''',
        c('"Keep it safe."', flags=(DUET + "declined",))),
], "aranka", DUET_OUT, forbids=(CONTEST_WON,), AnswerLists=[ADEPT_LIST], ReturnToList=True,
    ReturnText="{n}Aranka sets her cup down, still humming the last line under her breath.{/n}")


# --- Nurah, Chapter 2: the cornered branch, every path ----------------------------------------------------------------
# Her agency: she reads the linen as a master's care for stock, and decides what the Commander's hands are worth.

S = seen("nurah.early.hands")
beat("nurah.early.hands", "Clean linen", "Nurah", 2, '[Hold out a strip of clean linen.] "Your hand is bleeding."', [
    nu("start", '''{n}Nurah looks at the linen, then at you, and does not take it.{/n} "Oh, how thoughtful. Mustn't let the stock spoil before you've decided what it's worth. Going to look at my teeth next?"
{n}She turns her right hand over. The palm is split across the heel, and not all the blood on her is somebody else's.{/n} "Go on, then. Tidy up the traitor for the headsman. Or don't. I'd rather bleed than be grateful."''',
       c("[Lore (Nature) DC 14] [Take her wrist and bind it.]", flags=(S,),
         check=dict(Skill="SkillLoreNature", DC=14, Success="bound", Failure="fumbled")),
       c("[Drop the linen at her feet, and step back.]", "rag", flags=(S,)),
       c('"Bleed, then. Whatever I decide about you, it won\'t be because your hands were clean."', "bled", flags=(S,))),
    nu("bound", '''{n}You take her wrist before she can pull it away. She lets you the way a cat lets you, every muscle ready. You clean the cut with water from your flask and bind it tight across the palm and twice round the wrist, and she watches your fingers the whole while, the way a forger watches somebody else sign a name.{/n}
"Neat." {n}She flexes the hand. The binding holds.{/n} "Somebody used to tie knots like that on me, so I could carry the inkwell in the morning." {n}She takes the hand back.{/n} "Pretty work. Does the headsman get to unwrap it?"''',
       c('"Whatever you did, nobody should have sold you."', flags=(HANDS + "bound",))),
    nu("fumbled", '''{n}You take her wrist. The linen slides, the knot slips, and the cut opens again under your thumb. Nurah snatches the strip out of your fingers.{/n}
"Give it here. Honestly. You'd lose a war to a bandage." {n}She binds it herself in three quick turns, one end in her teeth, and ties it off without looking.{/n} "There. That's how it's done when nobody's going to do it for you."''',
       c('"You learned that somewhere hard."', flags=(HANDS + "fumbled",))),
    nu("rag", '''{n}You let the linen fall on the flagstones between you and step back.{/n}
{n}Nurah stares at it. Then she bends, quick as a sparrow, snatches it up, and binds her own hand in three tight turns, one end in her teeth.{/n} "Hm." {n}She ties it off.{/n} "Nobody ever let me tie my own bandage before. They always wanted to watch me be grateful."
"Don't think it buys you anything."''',
       c('"Who made you be grateful?"', flags=(HANDS + "rag",))),
    nu("bled", '''{n}Nurah stares at you, and then she laughs, short and hoarse and honestly amused.{/n} "Finally. Somebody in this army who doesn't pretend."
{n}She wipes the hand on her clothes again, slowly, on purpose, one long red smear.{/n} "Fine. I'll bleed. You decide."''',
       c('"Somebody should have done better by you, once. It won\'t be me tonight."', flags=(HANDS + "bled",))),
], "nurah", HANDS_OUT, exclusive=(seen("nurah.early.hanging"),), AnswerLists=[SIEGE_CORNERED], NativeReturnCue=SIEGE_SERMON)


# --- Nurah, Chapter 2: the accomplice branch ("They'll hang me from a tree") ---------------------------------------
# Her agency: she prices any promise at once, and the only coin she has is her pen.

S = seen("nurah.early.hanging")
beat("nurah.early.hanging", "Worth more alive", "Nurah", 2, '"Nobody is hanging you from a tree."', [
    nu("start", '''"No? And who'll stop them, you?" {n}She laughs, and it comes out wrong.{/n} "You'll be up in the citadel being thanked. I'll be in a tent with a knife under the pillow, listening for boots. Your soldiers saw which side I was standing on, Commander. Somebody always sees."''',
       c("[Persuasion DC 14] \"Nobody hangs you while I'm in command.\"", flags=(S,),
         check=dict(Skill="CheckDiplomacy", DC=14, Success="promised", Failure="doubted")),
       c('"They might. Make yourself worth more to me alive than dead."', "bargained", flags=(S,))),
    nu("promised", '''{n}She looks at you a while, measuring, the way she measures a sentence before she decides to keep it.{/n} "...You mean that. How very odd."
{n}Then, because she cannot help herself, she prices it.{/n} "All right. Here's what you've bought. When this is over, I'll write your war. All of it, the wrong side included, and nobody who starts it will be able to put it down. Every commander wants a book. You'll be the only one who gets an honest one."''',
       c('"I\'ll hold you to that."', flags=(HANGING + "promised",))),
    nu("doubted", '''"That's what everyone says." {n}Nurah wipes her nose on the back of her wrist.{/n} "Right up to the morning they hand you the rope and tell you it's for the best. I've read a great deal of history, Commander. Promises like yours are what footnotes are for."''',
       c('"Then I\'ll be a very long footnote."', flags=(HANGING + "doubted",))),
    nu("bargained", '''{n}Something wakes up in her face. It is not gratitude. It is business.{/n} "Worth more alive. Now you're speaking my language."
{n}She counts it off on bloody fingers.{/n} "I'm a historian. I write things down, and people read them for a hundred years. Keep me breathing and I'll write you: your whole fool's crusade, from the wrong side, which is the only side worth reading. Let them hang me, and the only account of you will be the Queen's, and she'll make you sound like a hymn."
"That's my price. Take it, or fetch the rope yourself."''',
       c('"Done. Write me."', flags=(HANGING + "bargained",))),
], "nurah", HANGING_OUT, exclusive=(seen("nurah.early.hands"),), requires=(ASKED_TO_STAY,), AnswerLists=[SIEGE_FRIEND],
    NativeReturnCue=SIEGE_WHAT)


# --- Jannah, Chapter 1: "Four days" -----------------------------------------------------------------------------------
# Her agency: the proud duellist turns the question into a challenge, or lets one honest line out and covers it again.

S = seen("jannah.early.laugh")
beat("jannah.early.laugh", "Four days", "Jannah", 1, '"Four days. That isn\'t luck."', [
    jan("start", '''{n}The laugh stops as if somebody had cut its string. Jannah sets her mug down, very precisely, and looks at you along the table the way she might look along a blade.{/n}
"No? Then what is it?" {n}One eyebrow goes up.{/n} "Want to find out if it's skill?"''',
        c('"I think the laugh was louder than the joke."', "honest", flags=(S,)),
        c('"Skill, then. Show me, sometime."', "bravado", flags=(S,)),
        c('"Then you\'re lucky. Drink to it."', "let_be", flags=(S,))),
    jan("honest", '''{n}For a heartbeat she looks as though she will laugh again. She doesn't.{/n}
"Four days." {n}She says it low, under Curl's chatter, so that only you hear it.{/n} "I'd unpacked my good shirt. I didn't know the names of the streets yet. When it all came down I ran the wrong way twice, because I didn't know which way was the wrong way." {n}She turns the mug in a slow circle on the table.{/n} "In Mivon you always know where the edge of the circle is."
{n}Then the grin comes back, all at once and a little too wide, and she lifts the mug to the whole table.{/n} "Lucky! To luck!"''',
        c("[Drink with her.]", flags=(LAUGH + "honest",))),
    jan("bravado", '''"Sometime?" {n}She is grinning now, the real one.{/n} "I'll hold you to that. When this is done, when they've put the city back together and there's a floor that isn't on fire: a bout. To the first touch, like civilised people."
{n}She points at you with the mug.{/n} "Seelah, you're witness. This one owes me a bout."''',
        c("[Look at Seelah.]", "witness")),
    n("witness", "Seelah", '''{n}Seelah, who has heard every word, raises her own mug with tremendous solemnity.{/n} "Witnessed! And I want a seat at the front."''',
      c('"I\'ll be there."', flags=(LAUGH + "bravado",)), portrait="Seelah", speaker_unit=SEELAH),
    jan("let_be", '''{n}Something in her shoulders comes down an inch.{/n} "To luck." {n}She knocks her mug against yours, much too hard, and drinks half of it.{/n}
"You're all right. Seelah said you would be."''',
        c("[Drink.]", flags=(LAUGH + "let_be",))),
], "jannah", LAUGH_OUT, requires=(ASKED_SERVICE,), AnswerLists=[TABLE_LIST], ReturnToList=True,
    ReturnText="{n}Jannah wipes the foam from her lip and turns back to the table, already louder than she needs to be.{/n}")


# --- Jannah, Chapter 2: "After the ring" (the Houndheart camp, on arrival) ---------------------------------------------
# Dramatic irony only: she will run before the ring is found. Nothing she says here foretells it.

S = seen("jannah.early.bout")
BOUT_CHOICES = (
    c('"After the ring, then. Flat ground."', "accepted"),
    c('"If you still want it when we\'re done here."', "deferred"),
    c('"Not with a friend of Seelah\'s. I might win."', "refused"),
)
beat("jannah.early.bout", "After the ring", "Jannah", 2, '"Marked by Iomedae, am I? You sound like you\'d like to test that."', [
    n("start", "Narrator", '''{n}Jannah turns, hands still on her hips.{/n}''',
      c("Continue", "owed", flags=(S,), requires=(LAUGH + "bravado",)),
      c("Continue", "fresh", flags=(S,), forbids=(LAUGH + "bravado",)), portrait="Jannah"),
    jan("owed", '''"Test it? You already owe me a bout from the Defender's Heart, and now you've gone and got famous on me." {n}She looks you up and down, delighted.{/n}
"I'm not fencing a legend in a camp full of junk. After the ring. Elan finds his bauble, and you and I find a bit of flat ground."''',
        *BOUT_CHOICES, unit=JANNAH_CAMP),
    jan("fresh", '''"Would I!" {n}Jannah's grin flashes.{/n} "Half of Mendev says the hero of Kenabres can't be touched. I'd like to be the one who touches them first."
"A bout. After the ring: Elan finds his bauble, and you and I find a bit of flat ground."''',
        *BOUT_CHOICES, unit=JANNAH_CAMP),
    jan("accepted", '''"Done!" {n}She claps her hands once.{/n} "Seelah, you heard it. Elan, you heard it. If the Commander tries to wriggle out, I want witnesses."
{n}Elan looks pained. Seelah looks delighted.{/n}''',
        c("[Go and find the ring.]", flags=(BOUT + "accepted",)), unit=JANNAH_CAMP),
    jan("deferred", '''"Oh, I'll still want it." {n}She laughs, loud enough to lift a crow off the nearest tent.{/n} "I always want it. Ask anyone in Mivon. Ask the ones who lost."''',
        c("[Go and find the ring.]", flags=(BOUT + "deferred",)), unit=JANNAH_CAMP),
    jan("refused", '''"You might win!" {n}Jannah laughs so hard that Elan glances round to see what he missed.{/n} "That's the nicest thing anyone's said to me since Kenabres. Fine. Keep your record. I'll keep mine, and find somebody with fewer scruples."''',
        c("[Go and find the ring.]", flags=(BOUT + "refused",)), unit=JANNAH_CAMP),
], "jannah", BOUT_OUT, AnswerLists=[CAMP_LIST], ReturnToList=True,
    ReturnText="{n}Jannah turns back to the others, still grinning, and rolls her sword shoulder as though the bout were already chalked out.{/n}")


# --- Nurah, Chapter 4 (T): the packet in the map case --------------------------------------------------------------
# Her prison branch: pardoned (she walks out at night and back before the bell) and accepted. She cannot follow the army
# into the Abyss she once took the demons' side for, so she sends her corrections, and asks for the sky.

SKY_CHOICES = (
    c("[Write it down plainly: the colour, the movement, the smell, and nothing else.]", "plain"),
    c("[Write it as well as you can. She should have the real thing.]", "pretty"),
    c("[Keep her corrections, and leave her page blank.]", "blank"),
)
SKY_NOTE = '''"Commander."
"I'm told the army goes down tomorrow. I'm told nothing else, because I'm a prisoner, and prisoners hear things last, when they hear them at all."
"Enclosed: the three volumes of demonology the Drezen archive lends to officers, with my corrections in the margins. Most of the margins are full. Two chapters are copied out of a worse book, and one was written by a man who had plainly never met a demon, only a priest who had. Read my notes, not his."
"I spent years on the Abyss's side and never once saw the place. You will. So here is my fee for the corrections: write down the sky. What colour it is. Whether it moves. What it smells of, if a sky can smell. Write it plainly. If you make it pretty I'll know, and I'll print it exactly as you wrote it, and so will everybody else."'''
SCENES.append(scene(SKY, "The sky, exactly", "Nurah", 4, "", [
    n("open", "Narrator", '''{n}At camp in the Abyss, unrolling your maps by a fire that burns the wrong colour, you find a packet you did not pack: three officers' books wrapped in oilcloth and a sheaf of paper sealed with candle wax, wedged into the bottom of the map case, where only somebody who had walked through your rooms at night would think to put it. The outer fold says, in a cramped hand: "Open when you get there. Unless you've died. In that case leave it alone."{/n}''',
      c("Continue", "note_kept", requires=(COMPLETE,)), c("Continue", "note", forbids=(COMPLETE,)), portrait="Nurah"),
    nu("note", SKY_NOTE + '''
{n}It is signed with a single N, in a hand so small it looks like stitching.{/n}''', *SKY_CHOICES),
    nu("note_kept", SKY_NOTE + '''
{n}It is signed with a single N, in a hand so small it looks like stitching. Under the N, smaller still:{/n} "Come back. The book wants an ending, and I've decided it's you. Don't make me write it from the casualty lists."''',
       *SKY_CHOICES),
    n("plain", "Narrator", '''{n}You write it by the wrong-coloured fire, a page and a half in your worst hand, with no adjective you can catch yourself using. It is harder than it sounds. The sky here does not want to be described plainly, and you describe it plainly anyway, and fold the page in with her corrections to carry home.{/n}''',
      c("[Seal it.]", flags=(SKY + "_plain",)), portrait="Nurah"),
    n("pretty", "Narrator", '''{n}You write it as well as you have ever written anything, and the page fills with things you did not know you had noticed until you had to find words for them. It is the best thing you have written. It is not what she asked for. You fold it in with her corrections to carry home.{/n}''',
      c("[Seal it.]", flags=(SKY + "_pretty",)), portrait="Nurah"),
    n("blank", "Narrator", '''{n}You read every one of her corrections, some of them twice, and they are right more often than the books are. The page she asked for you leave empty. Somewhere in Drezen a halfling is scratching days into a cell wall in rows of five.{/n}''',
      c("[Put the packet away.]", flags=(SKY + "_blank",)), portrait="Nurah"),
], requires=("trickster.ever", RELEASED, ACCEPTED, "nurah.prison"),
    forbids=(CLOSED, RETURNED, "nurah.ran_off", *DEATHS, *SKY_OUT), delay=24, last=4, optional=True, Relationship="nurah",
    Chapters=[4], Remote=True, Kind="letter"))

SKY_PARAGRAPHS = (
    p("The chapter on the Abyss was the only one in the book she had not seen for herself. She printed the Commander's page "
      "as it came, ugly and exact, and wrote in the preface that she had never in her life been so jealous of a paragraph.",
      requires=(SKY + "_plain",)),
    p("In the chapter on the Abyss she struck out every adjective the Commander had sent her and printed what was left, with "
      "a footnote: \"The Commander thinks the Abyss is beautiful. The Commander should be watched.\"",
      requires=(SKY + "_pretty",)),
    p("The chapter on the Abyss she wrote from the archive's three volumes and her own corrections. A footnote explained "
      "that her eyewitness had been given a blank page, and had returned it in perfect condition.", requires=(SKY + "_blank",)),
)


# --- Consequences: appended choices and nodes in the named reading scenes ---------------------------------------------

def _owned_line():
    return c('"Because you\'re mine now. The pardon says so."', "refused", flags=(CLOSED, "nurah.trickster.cost.owned_line"))


def _why(node_id, text):
    """A recalled night in the citadel, then her question again, and the same answers (the temper, or her hard no)."""
    return nu(node_id, text, *tempers((RELEASED,)), _owned_line())


NIGHT_OUT = [
    (c('"Because in the citadel I bound your hand, and I hate to waste good linen."', "siege_bound",
       requires=(HANDS + "bound",)),
     _why("siege_bound", '''{n}She looks down at her palm. The scar runs across the heel of it, thin and straight, because it was bound straight.{/n} "It healed flat. I noticed. I notice everything that's done to me; it's the one lesson the stick taught me that I kept."
{n}She closes the hand.{/n} "That's a reason for a bandage. Give me the real one."''')),
    (c('"Because in the citadel I botched your bandage and you finished it better. Then I botched you a pardon, and you did it again."', "siege_fumbled",
       requires=(HANDS + "fumbled",)),
     _why("siege_fumbled", '''"Ha." {n}She holds up the palm. The scar is crooked where her own teeth pulled the knot.{/n} "At least the linen didn't have your seal on it upside down. That's a reason to hire a clerk, Commander. Try again."''')),
    (c('"Because in the citadel I dropped the linen and let you tie your own hand. I want to see what else you do when nobody holds the bandage."',
       "siege_rag", requires=(HANDS + "rag",)),
     _why("siege_rag", '''{n}For once she has no answer ready. She turns the pardon over on her knee, and over again.{/n} "That is either the best thing anybody has ever said to me, or the cleverest. I can't tell which, and I can always tell."
"Say the rest of it."''')),
    (c('"Because in the citadel I let you bleed and didn\'t pretend otherwise. You liked that."', "siege_bled",
       requires=(HANDS + "bled",)),
     _why("siege_bled", '''"I did." {n}Her mouth twists.{/n} "An honest crusader. I thought I'd dreamed it, bleeding."
"So be honest again. Why?"''')),
    (c('"At the siege I told you nobody would hang you. Nobody has."', "siege_promised",
       requires=(seen("nurah.early.hanging"),), forbids=(HANGING + "bargained",)),
     _why("siege_promised", '''"Nobody has. Yet." {n}She taps the gaol ledger's copy of her sentence.{/n} "You said it like somebody who'd never opened a history book. I wrote it down that night, word for word, so I could laugh at it later. I haven't."
"That's still not why."''')),
    (c('"You sold me a book at the siege. I\'m collecting."', "siege_bargained", requires=(HANGING + "bargained",)),
     _why("siege_bargained", '''"Collecting." {n}She grins with every one of her teeth.{/n} "So that's what I am. An advance."
{n}Then the grin goes.{/n} "Trezbot bought me for my handwriting too. Be very careful how you answer the next part."''')),
]

DUET_READER = [
    (c('[Kenabres] "In the Count\'s parlour you held the last line open for me. Have the first one now."', "parlour_shared",
       requires=(DUET + "shared",)),
     page("parlour_shared", "Aranka", '''{n}She stops with her cup halfway to her mouth.{/n} "The cracked voice. In the Count's house, with the demons hardly cold on the carpet." {n}She stares at you as if you had walked out of a song.{/n} "That was you? You landed it on the note and looked so surprised. Oh, this is much better."
"First, then. And you'll sing the last line tonight, because it seems to be yours."''', c("Continue", "signed"))),
    (c('[Kenabres] "You stole my last line once, in the Count\'s parlour. Take the billing too."', "parlour_stolen",
       requires=(DUET + "stolen",)),
     page("parlour_stolen", "Aranka", '''"The Count's parlour!" {n}She claps a hand over her mouth and laughs through it.{/n} "The voice that broke on the same note twice! I took the ending off you, and I'd do it again. It was falling."
{n}She puts her hand on your arm, briefly.{/n} "First, then. Mine. And tonight I'll leave you the last note. Don't you dare drop it."''',
         c("Continue", "signed"))),
    (c('[Kenabres] "In the Count\'s parlour I beat time and let you have the verse. Have the song."', "parlour_hers",
       requires=(DUET + "hers",)),
     page("parlour_hers", "Aranka", '''{n}She goes very quiet, for her.{/n} "You were the one with your hand on the table." {n}She turns her cup round once.{/n} "Most people want the last line. You didn't. And now you've given me a whole song with your verse in it, and I don't know what to do with you."
{n}Then, briskly, because the crowd is listening:{/n} "First. Mine. Thank you."''', c("Continue", "signed"))),
    (c('[Kenabres] "You kept a verse for me in the Count\'s parlour. I\'ve come to collect it."', "parlour_declined",
       requires=(DUET + "declined",)),
     page("parlour_declined", "Aranka", '''"Kept a..." {n}She looks at you properly, and you watch her find you: the parlour, the cracked note, the stranger who wouldn't try again.{/n} "'Once was enough for one day'! And then you went off and wrote a second verse for my song instead."
{n}She laughs.{/n} "Then we're square. My name first. And from now on you sing with me, because I'm not keeping any more of your verses for you."''',
         c("Continue", "signed"))),
]

STORIES_READER = [
    (c('"At the Defender\'s Heart you told me you ran the wrong way twice. I remembered."', "heart_honest",
       requires=(LAUGH + "honest",)),
     page("heart_honest", "Jannah", '''{n}She goes still on the bunk.{/n} "I'd forgotten I told you that."
"No. I hadn't. I've thought about it every night since Houndheart: that I said it out loud to you, at a table, with a mug in my hand, and then went and did it again." {n}She looks back down at the scratched circle.{/n} "Go on. Say what you came to say."''',
         c("Continue", "choose"))),
    (c('"You still owe me a bout. To the first touch, like civilised people."', "heart_bravado",
       requires=(LAUGH + "bravado",)),
     page("heart_bravado", "Jannah", '''"I said that in front of Seelah, so I couldn't forget it if I tried." {n}The ghost of the old grin comes and goes.{/n}
"I'd have fought you then. I'd have won, probably. That was somebody else, with a floor that wasn't on fire."''',
         c("Continue", "choose"))),
    (c('"At the Defender\'s Heart I let you keep your laugh. I\'m not here to take it now."', "heart_let_be",
       requires=(LAUGH + "let_be",)),
     page("heart_let_be", "Jannah", '''{n}She looks at you sidelong.{/n} "You were the only one at that table who didn't ask what was under it." {n}She almost smiles.{/n}
"Don't start now. There's nothing under it any more but straw."''',
         c("Continue", "choose"))),
    (c('"Flat ground, after the ring. You owe me a bout."', "camp_bout", requires=(seen("jannah.early.bout"),),
       forbids=(BOUT + "refused",)),
     page("camp_bout", "Jannah", '''{n}Her face does something complicated.{/n} "After the ring." {n}She laughs once, with none of the old noise in it.{/n}
"There wasn't an after the ring. There was a quasit and a lot of coloured light, and then I was running north through the scrub, and somewhere behind me there was a bit of flat ground with nobody standing on it. I've owed you that bout in every cell since."''',
         c("Continue", "choose"))),
    (c('"At Houndheart you told me to keep my record."', "camp_record", requires=(BOUT + "refused",)),
     page("camp_record", "Jannah", '''"I kept it." {n}Her mouth twists.{/n} "Not one touch in seven years in the circles of Mivon. I've still got it: a perfect record and a deserter's name. You'd be amazed how little the one does for the other."''',
         c("Continue", "choose"))),
]

CONSEQUENCES = {
    "nurah.trickster.prison.night_out": ("start", NIGHT_OUT),
    "nurah.trickster.prison.night_out_late": ("start", NIGHT_OUT),     # its Chapter 5 twin, deep-copied before this pass
    "aranka.trickster.verse.duet": ("duet", DUET_READER),
    "aranka.trickster.verse.duet_yard": ("duet", DUET_READER),          # the copy for a shuttered market
    "aranka.trickster.verse.duet_late": ("duet", DUET_READER),          # the Chapter 5 twins (polish), copied before this pass
    "aranka.trickster.verse.duet_yard_late": ("duet", DUET_READER),
    "jannah.trickster.alive.stories": ("start", STORIES_READER),
}
SKY_PAGES = ("nurah.trickster.epilogue.the_margin", "nurah.trickster.epilogue.book_only",
             "nurah.trickster.epilogue.unanswered", "nurah.trickster.epilogue.bereaved", "nurah.trickster.epilogue.refused")


def integrate(payload):
    """Append the consequence choices and nodes to their reading scenes, and the sky paragraphs to Nurah's book pages
    (save-safe: new choices and nodes go last; nothing is renamed, removed or reordered)."""
    import copy
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for scene_id, (node_id, rows) in CONSEQUENCES.items():
        target = scenes[scene_id]
        nodes = {node["Id"]: node for node in target["Nodes"]}
        for choice, node in rows:
            if node["Id"] in nodes:
                raise ValueError("pacing_pp3: node %s already in %s" % (node["Id"], scene_id))
            node = copy.deepcopy(node)
            nodes[node_id]["Choices"].append(copy.deepcopy(choice))
            target["Nodes"].append(node)
            nodes[node["Id"]] = node
    for page_id in SKY_PAGES:
        start = next(node for node in scenes[page_id]["Nodes"] if node["Id"] == "start")
        start.setdefault("Paragraphs", []).extend(copy.deepcopy(list(SKY_PARAGRAPHS)))
