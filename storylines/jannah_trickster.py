"""Jannah Aldori on the Trickster path: "First blood" (Writer/handoffs/trickster/jannah.md for the canon research; the binding
plan is 11-ROSTER-PLAN-2 §2 with the coordinator's correction: duel law she honours, never a word made true).

Canon: a half-elf recruit of the Eagle Watch from Mivon, "an apprentice of a famous fencing master" (Seelah Q1 3f001f86)
who "won every encounter, I always won" (Deserter/Cue_0018 fb323aad) and signed up "four days before the demon attack! Am
I lucky, or what?" (52169bb4). Seelah: "She couldn't have become an Aldori otherwise" (a955505e). She ran at the
Houndheart camp ambush, north toward Numeria (e2c02200, 78c0efc7), and the vrocks caged her in the Molten Scar: "It was my
first real battle against actual demons" (Deserter/Cue_0015 423ff883). The [Attack] answer (Answer_0026 3dce20ad) plays
Cue_0027 199d4dbf: "Her fencer's instincts allow Jannah to react to the danger, but the cage is too small and she cannot
evade your weapon. Jannah falls to the floor dead, her eyes wide and unseeing." Alive, she returns in Seelah's Q3 "calm
and collected... a scar on her right temple, jagged and fresh" (ktc_DeserterJoins/Cue_0001 7f36934a), afraid of being
"written out of my own life story" (Cue_0022 cfcafcf2); refused, she goes back to the Condemned (Cue_0030 7fc6b68e).

Devices, earned in play:
- killed worlds: "Aldori terms". Before the native [Attack], a Knowledge (World) check names the Aldori forms (to the first
  blood; the one who bleeds lays down her blade and lies where she falls, eyes open, until the victor quits the circle).
  Her pride accepts; the Commander passes her own sword through the bars; the native blow lands as first blood along her
  right temple. A scalp cut sheets her face in blood, and a yielded Aldori lying still with open eyes is a corpse to anyone
  who does not know the forms. She yielded; the Commander walks away knowing it. In Chapter 5 she turns herself in at the
  Drezen cells (her canon JannaInPrison_Locator) to have the unclaimed yield claimed.
- living worlds: "a duel of stories". She has put herself in those cells to wait for the Condemned wagon and will take no
  pardon. Her master's wine-hour game, blood and tale: each tells the other's part of the Houndheart ambush, and the first
  lie caught is first blood. The Commander wins by catching the lie she tells against herself (or cheats a false catch, a
  Ledger secret), or loses, and she serves the posting and comes back on her own word.
Cost: her unbeaten record (the cage, or the story) and the scar; the Commander's public yield if she draws first blood at
the muster. The commit is hers: a public Aldori challenge with the stake named first ("If I draw first blood, you're
mine"); the first touch, win or lose, is the yes; throwing the bout is her no (only over a lie the Commander keeps).
The spine between return and commit is jannah_circle (the forms, Houndheart, the wall).
"""
from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "jannah"
P = "jannah.trickster."
C = "jannah.circle."
UNIT = "4880d0b16ca74fa46a167914e2b44bcc"          # CR4_DeserterJanna (the cage, the Drezen cell, Seelah's Q3)
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
LOCATOR = "e595a2a6-e8ca-4d13-9010-f482088a4a27"   # JannaInPrison_Locator (JannaInPrison_Drezen 478931ef, Janna_Prison 1e069277)
PRESENCE = "jannah.presence"
CAGE_LIST = "170fd7a11f66c88428bc27bfba3a569f"     # c3/MoltenScar/Deserter/AnswersList_0021 ([Open the cage] x2, [Attack])
CAGE_CUE = "423ff8833653bf94cb4bd8fb047578a8"      # Deserter/Cue_0015 "I know you're angry with me because I ran."
KILL_CUE = "199d4dbffb5a53a4cb73578307cbb4a9"      # Deserter/Cue_0027 (the native blow; starts JannaDead_SeelahDoesntKnow)
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"   # NPC_Common/Irabeth/AnswersList_0009
KING_C5 = household.KING_C5                        # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
KING_C5_RETURN = household.KING_C5_RETURN          # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"

STARTED = "jannah.started"
CLOSED = "jannah.closed"
COMMITTED = "jannah.committed"
# Native state (trickster_world BINDINGS).
DEAD = "jannah.dead"                              # JannaDead_SeelahDoesntKnow f8129442 (Cue_0027)
DEAD_KNOWN = "jannah.dead_known"                  # JannaDead_SeelahKnows 699b1ad8 (Seelah told, Cue_0105 166223b5)
DEAD_L = "jannah.dead.latched"
FREE = "jannah.free"                              # JannaFree d99770b1
PRISON = "jannah.prison"                          # JannaInPrison 59632e17
CONDEMNED = "jannah.condemned"                    # JannaInCondemned 46f4524c
JOINED = "jannah.joined"                          # ktc_DeserterJoins/Cue_0019 651ecf0c (Seelah's Q3)
REFUSED = "jannah.refused_q3"                     # ktc_DeserterJoins/Answer_0017 e66c11e6 "You need to leave Drezen."
Q3_STARTED = "seelah.q3_started"                  # WeightOfMySword_SeelahQ3_quest 5a5a533c (started)
SOULS = "seelah.souls_returned"                   # the same quest, completed
ELAN_DEAD = "seelah.elan_dead"
SEELAH_DEAD = "seelah_dead"
SEELAH_GONE = "seelah_gone"
SEELAH_BACK = "seelah.trickster.returned"

# The device, killed worlds.
PRIMED = P + "primed"                             # the forms named, her sword passed, the blow struck as first blood
BOTCHED = P + "cage.botched"                      # the forms garbled; the cage is only an execution now
ASH_SILENT = P + "ash.said_nothing"
ASH_SAID = P + "ash.said_sentence"
COST_ASH = P + "cost.left_in_ash"
CLAIMED = P + "yield.claimed"
RELEASED = P + "yield.released"
NAMELESS = P + "cost.nameless"                    # dead on the rolls, kept so (the Evil claim)
SCAR = P + "cost.temple_scar"
# The device, living worlds.
IN_CELLS = P + "alive.in_cells"
Q3_SETTLED = P + "alive.q3_settled"
POSTED = P + "alive.posted"                       # she won the story; the Condemned wagon took her north
CAUGHT = P + "alive.caught_her"                   # the Commander caught the lie she told against herself
LIED = P + "alive.false_blood"                    # a false catch, bluffed: the Ledger secret below
SECRET = "trickster.secret.jannah_false_blood"
SECRET_KNOWN = SECRET + ".known.jannah"
STORY_LOST = P + "cost.story_lost"                # the Commander lost the story; she came back on her own word
POSTING = P + "cost.posting"
# Both worlds.
RETURNED = P + "returned"
FIRST_LOSS = P + "cost.first_loss"                # her unbeaten record, gone
GONE = P + "gone"
DECLINED = P + "declined"                         # she threw the bout
CONFESSED = P + "confessed"
HELD_LIE = P + "held_the_lie"
YOU_FIRST = P + "bout.commander_first"
SHE_FIRST = P + "bout.her_first"
PUBLIC_YIELD = P + "cost.public_yield"            # the Commander lay down in the sand before the muster
REFUSED_YIELD = P + "refused_the_yield"
LATE_YES = P + "chalk_circle.walked_in"
LATE_COMMITTED = P + "late_committed"
PRESENCE_ON = P + "presence_on"
# The spine (jannah_circle); scene ids double as flags once the scene completes.
FORMS = C + "forms"
HOUNDHEART = C + "houndheart"
WALLS = C + "walls"
NIGHT = P + "circle_night"
MORNING = P + "morning"
HH_HONEST = C + "hh.honest"
HH_LUCKY = C + "hh.lucky"
HH_STAND = C + "hh.stand"
WALL_SALUTE = C + "walls.saluted"
WALL_SHIELD = C + "walls.shielded"
WALL_WATCHED = C + "walls.watched"
SEELAH_HERSELF = C + "seelah.herself"
SEELAH_FOR_HER = C + "seelah.told_for_her"
SEELAH_KEPT = C + "seelah.kept"
MIVON_TRUTH = C + "mivon.truth"
MIVON_LEGEND = C + "mivon.legend"

RELATIONSHIP = dict(
    Title="First blood",
    Description=("Jannah Aldori, a half-elf duellist of Mivon who never lost a bout and ran from one battle. She keeps "
                 "the Aldori forms the way other people keep a faith. I have had to learn them."),
    Objective="Answer Jannah Aldori",
    Guidance=("On the Trickster path. At the Molten Scar, if you mean to strike the deserter in the cage, know the Aldori "
              "forms first and offer them to her. If she lives, look for her in Chapter 5 in the old cells under the "
              "Drezen citadel, where she has put herself. She fights her own duels, and she may throw one."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, DEAD_KNOWN], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED, DEAD_KNOWN: RETURNED},
    TricksterAccess={
        "killed": dict(detect=[DEAD], device=P + "killed.yield", returned=RETURNED),
        "killed_known": dict(detect=[DEAD_KNOWN], device=P + "killed.yield", returned=RETURNED),
        "alive": dict(detect=["!" + DEAD, "!" + DEAD_KNOWN], device=P + "alive.stories", returned=RETURNED),
    },
)

PRESENCES = {
    # A copy of her own unit at her own canon Drezen mark: the last cell of the old gaol, where Janna_Prison translocates
    # her in Chapter 3 (that native placement runs in Chapter 3 only; this one is Chapter 5 only). No other presence uses
    # this locator; a later route that does must stand at least 2 m off it.
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(Locator=LOCATOR, Offset=[0.0, 0.0]),
                   Requires=["trickster.ever", PRESENCE_ON], Forbids=[CLOSED, GONE], MinChapter=5, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   Greeting="{n}In the last cell of the old gaol, with its door standing open, a half-elf in a patched "
                            "gambeson sits on the bunk with a long, slightly curved blade across her knees. She has "
                            "scratched a circle into the floor stones with its point, three paces across, and she keeps "
                            "her boots out of it.{/n}"),
}

DERIVED = {
    # Killed worlds: she is in the cell from Chapter 5 once the forms were kept at the cage; living worlds: once she is out
    # of the story duel (or back from the wagon). The posting keeps her off the locator until she walks back in.
    PRESENCE_ON: [[DEAD_L, PRIMED], [RETURNED]],
    # A Seelah's Q3 in progress is left to finish before she writes from the cells.
    Q3_SETTLED: [[JOINED], [REFUSED], [SOULS]],
    # R2-6: the war can end between the wall and the muster; her page answers it after the Threshold.
    LATE_COMMITTED: [["trickster.ever", WALLS]],
    # 05 §2.5 voice note (morning after): she joins, but she will have it remembered who chalked the circle first.
    "jannah.harem.voice.first_blood": [[COMMITTED]],
}


def jan(id, text, *choices, **kw):
    return n(id, "Jannah", text, *choices, portrait="Jannah", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Jannah", **kw)


def meet(id, title, entry, nodes, requires, forbids=(), delay=24, optional=False, **extra):
    """A physical scene at her cell (Chapter 5; the gaol is under the capital's citadel)."""
    SCENES.append(scene(id, title, "Jannah", 5, entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, *forbids))), delay=delay, last=5,
                        optional=optional, Relationship=REL, Chapters=[5], ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, kind="visit", chapter=5, optional=False, **extra):
    """A rest-delivered scene: a letter from her, or a night in which she is there in person."""
    SCENES.append(scene(id, title, "Jannah", chapter, "", nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))) if "trickster" not in requires
                        else tuple(dict.fromkeys(requires)),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, *forbids))), delay=delay, last=chapter,
                        optional=optional, Relationship=REL, Remote=True, Kind=kind, Chapters=[chapter], **extra))


# --- Killed worlds, Chapter 3: the forms at the cage (inline, before the native [Attack]). -----------------------------

SCENES.append(scene(P + "cage.terms", "The forms", "Jannah", 3,
    '"In Kenabres you boasted of a fencing master in Mivon. Did he teach you the forms?"',
    [jan("start", '''{n}The word reaches her somewhere under the fear. Her chin comes up a finger's breadth, the way a fencer's does when she sees a salute begin.{/n}
"He taught me everything. The salute, the measure, the forms. Seven years in his salle above the dyers' yards." {n}Her voice cracks on the last word. You watch her hate that it cracked.{/n}
"Why? Nobody gives the forms to a deserter. You give a deserter a rope."''',
         c('[Knowledge (World)] "Then hear them from me, the way he would have said them."',
           check=dict(Skill="SkillKnowledgeWorld", DC=22, Success="named", Failure="garbled")),
         c("[Step back from the cage.]", abort=True)),
     nar("named", '''{n}You give them to her whole. The salute, flat of the blade to the brow. The circle, and nobody steps out of it unbloodied. To the first blood and no further: the one who bleeds lays down her blade and lies where she falls, eyes open, until the victor has quit the circle. Whatever the victor says over her is the end of the matter. Whatever the victor leaves unsaid, she owes until it is said.{/n}''',
         c("Continue", "named_her")),
     jan("named_her", '''"Nobody in Mendev knows that. Nobody north of the River Kingdoms knows the last part." {n}Something in her face, which the vrocks spent weeks emptying out, fills back up. It isn't hope. It's older than hope, and it stands up straighter.{/n}
"You'd fight me. In a cage a pace and a half across, where I can't take one step." {n}She laughs, short and ugly.{/n} "They'll call it an execution with a bow in front of it."''',
         c('"They will. You and I will know better."', "accept"),
         c('"You\'d rather they called it one? Say so, and I\'ll step back."', "accept"),
         c("[Step back from the cage.]", abort=True)),
     jan("accept", '''{n}She looks past you at the sword lying in the ash beyond the bars, where the vrocks tossed it: a long Aldori blade, slightly curved, its grip wound in leather gone black with handling.{/n}
"That's what you're counting on, isn't it? That I'd rather lose a bout than be butchered. That I'm still that proud." {n}She wipes her face with the back of a filthy wrist and gets up off the floor of the cage, one hand on the bars.{/n}
"You're right. Give me my blade."''',
         c("[Pass her sword through the bars, hilt first.]", "guard"),
         c('"No. I\'ve changed my mind."', abort=True)),
     nar("guard", '''{n}She takes the hilt the way other women take a hand at a dance. The cage leaves her no footwork at all, so she sets her rear heel against the bars, sinks her weight, and brings the long blade up into the high Aldori guard, the only line the bars allow. Then she salutes you through the gap, flat of the blade to her brow, and her eyes above it are perfectly dry.{/n}
"Jannah Aldori. Of Mivon." {n}Her voice doesn't shake now.{/n} "Ready."''',
         c('[Attack] "To the first blood."', native_next=KILL_CUE, flags=(PRIMED,)),
         c("[Lower your blade, and take her sword back through the bars.]", abort=True)),
     nar("garbled", '''{n}You get the salute right and everything after it wrong: the circle, the count, what the one who bleeds must do and for how long. Jannah listens the way a master listens to a first-year student murder a verse.{/n}''',
         c("Continue", "garbled_her")),
     jan("garbled_her", '''"No. That's a tavern brawl with a bow in front of it." {n}The pride goes back wherever it was hiding, and what is left is a frightened girl in a cage.{/n}
"If you mean to kill me, Commander, kill me. Just don't call it the forms."''',
         c("[Step back from the cage.]", flags=(BOTCHED,)))],
    requires=("trickster",), forbids=(PRIMED, BOTCHED), last=3, Relationship=REL, Chapters=[3],
    AnswerLists=[CAGE_LIST], NativeReturnCue=CAGE_CUE, EntryMythic="PlayerIsTrickster"))


# The same night, alone: where the blade went (a memory; the Commander knows what the companions saw, and what they didn't).
visit(P + "cage.ash", "Where the blade went", [
    nar("open", '''{n}That night, by the light of a camp lamp at the edge of the Scar, you clean her blood off your blade and go over the bout the way she would have: cut by cut, in order.{/n}
{n}Her guard came up where the forms put it and the bars allowed it, high and forward. Your cut rode down the flat of her sword to the hilt, turned off the crossguard, and opened her right temple from the brow to above the ear. Not deep. Scalp wounds never need to be deep. They bleed as if the whole head were emptying.{/n}''',
        c("Continue", "fall")),
    nar("fall", '''{n}She went down on her back with her face a red mask and her eyes wide open, fixed on the roof of the cage. An Aldori who has yielded does not close her eyes, does not wipe away the blood, does not move a finger until the victor has quit the circle. She breathed through her teeth, shallow as a sleeper, and the smoke of the Scar did the rest.{/n}
{n}Your companions saw an execution. Nobody went into the cage to be sure. Nobody wanted to touch a deserter.{/n}''',
        c("[Remember that you said nothing over her, and walked out of the circle.]", "silent", flags=(ASH_SILENT, COST_ASH)),
        c('[Remember what you said over her] "Sentence carried out."', "sentence", flags=(ASH_SAID, COST_ASH))),
    nar("silent", '''{n}Under the forms, a yield the victor leaves unspoken is owed until it is spoken. You left hers lying in the ash with her. Whether she ever comes to collect it is hers to decide.{/n}
{n}Out in the dark the vrocks are circling back to their cages and their ritual. You hope she remembers to be dead for them too.{/n}''',
        c("[Put out the lamp.]")),
    nar("sentence", '''{n}You said it loud enough for everyone to hear, and the forms heard it too. Whatever the victor says over the yield is the end of the matter. The sentence was death to deserters, and it has been carried out: Jannah Aldori, recruit of the Eagle Watch, is dead. What the woman lying in the ash does with that is hers to decide.{/n}
{n}Out in the dark the vrocks are circling back to their cages and their ritual. You hope she remembers to be dead for them too.{/n}''',
        c("[Put out the lamp.]")),
], requires=("trickster.ever", DEAD_L, PRIMED), forbids=(RETURNED,), delay=6, kind="memory", chapter=3, optional=True,
    TricksterDevice=True)


# --- Killed worlds, Chapter 5: the unclaimed yield, in her own cell. -------------------------------------------------

meet(P + "killed.yield", "An unclaimed yield", '"The turnkey says there\'s a dead woman in my cells."', [
    nar("open", '''{n}The turnkey swears she walked in off the street at the change of the watch, gave a name that is on the Eagle Watch's roll of the dead, and asked for a cell. He gave her the last one because it was empty and because, he says, she had the look of someone who would take one anyway.{/n}
{n}She is standing when you come down the steps, in a patched gambeson with a long Aldori blade at her hip. A scar runs from her right brow to above the ear, pink and badly knitted: your blade's work, and nobody's healing.{/n}''',
        c("Continue", "salute")),
    jan("salute", '''{n}She salutes you, flat of the blade to the brow, and sheathes again before you can decide whether to return it.{/n}
"Commander. Jannah Aldori, of Mivon. I yielded to you in the Molten Scar."''',
        c("Continue", "unsaid", forbids=(ASH_SAID,)),
        c("Continue", "said", requires=(ASH_SAID,))),
    jan("unsaid", '''"You quit the circle without a word over me. Under the forms, a yield nobody claims is owed until somebody does. I've been owing you since the Scar." {n}She says it like a debt to a moneylender.{/n}
"I don't like owing. So I came to hear what you'd say."''',
        c("Continue", "how")),
    jan("said", '''"You said the sentence was carried out, and quit the circle. So it was. Jannah Aldori of the Eagle Watch is on the rolls of the dead. I read her name on the board by the chapel on my way in. They spelled it wrong."
{n}Something dry happens at the corner of her mouth.{/n} "So I came to ask who that leaves standing in your cells."''',
        c("Continue", "how")),
    jan("how", '''"You'll want to know how. I lay in the ash until your boots were out of hearing. Then I counted to a thousand, because my master used to say a victor's field is exactly as big as a victor's pride, and I didn't know how proud you were."
"The vrocks came back before I'd finished. I was dead for them too. One of them turned my head with a claw and went off to argue with the others about something. Then I tied up my temple with my shirt and walked south along the lava channels, by night, with my sword and nothing else."''',
        c('"And after that?"', "after"),
        c('"You could have kept walking."', "after")),
    jan("after", '''"I hired on with a salt caravan to Nerosyan under a name I made up and was bad at answering to. I guarded salt all winter. Nobody asked me a single thing." {n}She touches the scar, not the way people touch a wound: the way a fencer checks her guard.{/n}
"Then word came up the road that the Commander was back out of the Abyss, and I found I couldn't go on being a salt guard called nothing while I still owed you a yield."''',
        c("Continue", "record")),
    jan("record", '''"Seven years in the circles of Mivon, and I never once bled first. Not in a tournament, not in a quarrel, not against the bandits on the river roads. You were the first."
"I want you to know I haven't forgiven you for it. I'm not sure I want to."''',
        c("Continue", "seelah_known", requires=(DEAD_KNOWN,)),
        c("Continue", "claim", forbids=(DEAD_KNOWN,))),
    jan("seelah_known", '''"The turnkey says Seelah came down to the gaol after the Scar, asking whether anybody had brought in a body. Nobody had." {n}Her jaw sets.{/n}
"Don't tell her. Not yet. I'll do it myself, when I can look at her without being sick."''',
        c("Continue", "claim")),
    jan("claim", '''"So. Say it now. Whatever you say over me is the end of the matter, and I'll keep it. I'm an Aldori. That's all the Scar left me."''',
        c('[Claim the yield] "Then here it is. You live, under your own name, and you stay where I can find you."', "claimed",
          flags=(CLAIMED, RETURNED, STARTED, FIRST_LOSS, SCAR)),
        c('[Release the yield] "I release it. You owe me nothing. Go wherever you like."', "released",
          flags=(RELEASED, RETURNED, STARTED, FIRST_LOSS, SCAR)),
        c('[Claim it for yourself] "You\'re dead on the rolls. Stay dead. You\'ll fight where I send you, under no name at all."',
          "nameless", flags=(NAMELESS, CLAIMED, RETURNED, STARTED, FIRST_LOSS, SCAR), alignment=("Evil", 1)),
        c('[Dismiss her] "You\'re nothing to me. Get out of my gaol."', "dismissed", flags=(CLOSED, GONE))),
    jan("claimed", '''"Under my own name." {n}She repeats it the way you'd test an edge on a thumbnail.{/n}
"The Watch has me dead. Irabeth will have views. You'll have to tell her, because I'm not going to." {n}She sits down on the bunk, and only then does she look tired.{/n}
"All right. I'll stay where you can find me. I thought that would be harder to say."''',
        c("[Leave her to the cell.]")),
    jan("released", '''"Released." {n}She takes it like a blow she had been warned about.{/n}
"In Mivon that's an honour. The victor saying the loser owes nothing; they paint it on the salle wall. Here it just means you're done with me."
{n}She doesn't move toward the steps.{/n} "I'm staying anyway. Not because I owe you. Because I chose it, and that's the first thing I've done since the Houndheart camp that my legs didn't choose for me."''',
        c("[Leave her to the cell.]")),
    jan("nameless", '''{n}It lands. You watch it land. Then she straightens, heels together, the way a recruit stands for a sentence.{/n}
"As you say. No name." {n}Her voice is perfectly even.{/n}
"I'll keep it. Under the forms I have to. Don't expect me to like you for it, Commander."''',
        c("[Leave her to the cell.]")),
    nar("dismissed", '''{n}You turn your back on her and climb the steps. Behind you there is no sound at all: an Aldori does not move until the victor has quit the circle.{/n}
{n}In the morning the last cell is empty. On its floor someone has scratched a circle into the stones with a sword's point, and in the middle of it one word: PAID.{/n}''',
        c("[Let her go.]")),
], requires=(DEAD_L, PRIMED), forbids=(RETURNED,), delay=24, TricksterDevice=True)


# --- Living worlds, Chapter 5: the letter from the cells, and the duel of stories. -----------------------------------

visit(P + "alive.letter", "From the last cell", [
    nar("open", '''{n}The letter is folded small and sealed with candle wax, no signet. The hand is upright and exact, every stroke finished, like someone who was taught to write by the same master who taught her to cut.{/n}''',
        c("Continue", "joined", requires=(JOINED,)),
        c("Continue", "refused", requires=(REFUSED,), forbids=(JOINED,)),
        c("Continue", "condemned", requires=(CONDEMNED,), forbids=(JOINED, REFUSED)),
        c("Continue", "prison", requires=(PRISON,), forbids=(JOINED, REFUSED, CONDEMNED)),
        c("Continue", "free", requires=(FREE,), forbids=(JOINED, REFUSED, CONDEMNED, PRISON)),
        c("Continue", "unmet", forbids=(JOINED, REFUSED, CONDEMNED, PRISON, FREE))),
    jan("joined", '''"Commander. The jeweller is dead and the souls are home, and my parole was for the length of the hunt. I gave my word I'd go back to the Condemned when it ended. It's ended."
"I didn't run. Not once, all the way into that hole and out again. I'd like that written down somewhere, and you're the only one who writes things down who might believe it."''',
        c("Continue", "wagon")),
    jan("refused", '''"Commander. You told me to leave Drezen. I didn't. I've put myself in the old cells under the citadel instead."
"The cells aren't Drezen. They're the crusade's. And I was never going to run twice."''',
        c("Continue", "wagon")),
    jan("condemned", '''"Commander. My Condemned company came through Drezen on its way to the north gate. The sergeant lets us sleep in the gaol when we're in a town, so he can count us in the morning. I'm writing from the last cell."
"He says I'm the only one of his who ever asked to be counted."''',
        c("Continue", "wagon")),
    jan("prison", '''"Commander. I've been in your cells since the Molten Scar. Nobody moved me. I think the clerk who had my papers died in the siege, and nobody else wanted them."
"I've asked for the Condemned. This time I mean to be sent."''',
        c("Continue", "wagon")),
    jan("free", '''"Commander. You let me go at the Molten Scar. I went to Kenabres and tried to be nobody. It didn't take. I'm bad at being nobody; I was raised to be looked at."
"So I came back and gave the gaol my name, and they didn't know what to do with it, so they gave me a cell."''',
        c("Continue", "wagon")),
    jan("unmet", '''"Commander. The last you saw of me I was running north from the Houndheart camp in the rain. The vrocks had me in a cage in the Molten Scar after that. A Mendevian patrol cut the cages open in the winter. Everyone else in them was dead."
"I walked here, and gave the gaol my name, and asked for a cell. They gave me one. I think they were too surprised to argue."''',
        c("Continue", "wagon")),
    jan("wagon", '''"The Condemned wagon goes north at the ninth bell of Oathday, and I mean to be on it. I'm writing so you'll hear it from me and not from a turnkey, and not think I ran again."''',
        c("Continue", "sign")),
    nar("sign", '''{n}It is signed "J. Aldori, of Mivon", and under the name, very small, a circle with one stroke through it: her old salle's mark, the kind of thing a student draws in the margins for years after she has left.{/n}''',
        c("[Fold the letter.]", flags=(IN_CELLS,))),
], requires=("trickster",), forbids=(DEAD, DEAD_KNOWN, RETURNED, IN_CELLS, Q3_STARTED), delay=24, kind="letter",
    ForbidOverrides={Q3_STARTED: Q3_SETTLED}, RequiresAnyGroups=[[JOINED, REFUSED, "coronation.seen"]])


visit(P + "alive.stories", "Blood and tale", [
    nar("open", '''{n}The old gaol under the citadel smells of wet straw and lamp oil. The last cell's door stands open; the turnkey has given up on the lock. Jannah sits on the bunk in a patched gambeson with her back to the wall, her boots on the blanket and a borrowed practice sword across her knees. She has scratched a circle into the floor stones with its point.{/n}''',
        c("Continue", "start")),
    jan("start", '''"You got my letter." {n}She doesn't get up.{/n} "Then you know what I'll say to a pardon, so don't waste the ink."''',
        c('[Offer her a pardon] "Signed and sealed. You walk out of here tonight."', "pardon"),
        c('[Order her out] "You\'re not getting on that wagon. That\'s an order."', "order"),
        c('"Why the Condemned? You could simply leave."', "why")),
    jan("pardon", '''"No. A pardon is somebody else writing the end of my story. I was written out of it once already, at the Houndheart camp, by my own feet." {n}She turns the practice sword over on her knees.{/n}
"I'm writing the rest of it myself, thank you."''',
        c("Continue", "choose")),
    jan("order", '''"You can order me out of a cell. You can't order me into your crusade and have it mean anything." {n}She shrugs one shoulder.{/n}
"The Condemned will take me on nobody's order but mine. That's the one good thing about them."''',
        c("Continue", "choose")),
    jan("why", '''"Because I ran. Because the Condemned go wherever it's worst, and I want to stand somewhere bad and not run, just once, where somebody can see it."
{n}She looks at the scratched circle, not at you.{/n} "And because nobody in the Condemned looks at me the way Seelah does. As if I'm forgiven. I can't stand being forgiven."''',
        c("Continue", "choose")),
    jan("choose", '''{n}She waits, with the patience of a woman who has already decided and is only being polite.{/n}''',
        c('[Challenge her] "Then fight me for it. If I win, you stay."', "challenge"),
        c('[Let her go to the wagon] "Then go. Good luck, Jannah."', "let_go")),
    jan("challenge", '''"Fight you. In here?" {n}She looks round the cell: the bunk, the bucket, the circle she scratched.{/n}
"With what? They took my blade at the gate, and a stick against the Commander of the crusade is a joke I'm too tired to tell."
{n}Then something changes in her face, the way it once did in Kenabres when somebody mentioned a lost cart of beer.{/n} "Wait. There's a game."''',
        c("Continue", "rules")),
    jan("rules", '''"My master's salle played it on wet nights, when nobody could cross blades. Blood and tale. Two fencers tell the same bout, and each tells the other's part: you tell what I did, I tell what you did. The first one caught in a lie has bled first, and yields. He used to say a fencer who lies about a bout will lie with a blade, so you might as well find out over wine."
"We'll tell Houndheart. You were there."''',
        c("Continue", "stake")),
    jan("stake", '''{n}She lays the practice sword down inside the scratched circle, carefully, as if it were a real one.{/n}
"If I draw first blood, I'm on the wagon at the ninth bell, and you send nobody after it. If you do, I walk out of this cell, and you can say what comes next. That's the forms."''',
        c('"Agreed. I\'ll tell yours first."', "your_tale"),
        c('[Let her go to the wagon] "No. Go, if you have to."', "let_go")),
    nar("your_tale", '''{n}She settles against the wall, cross-legged, and waits the way a judge waits.{/n}
{n}You tell her part of Houndheart: the demons coming out of the rain, the wagons drawn up, the fire, Elan shouting for shields. And then her.{/n}''',
        c('[Tell it true] "You ran. Before it was over, you ran north into the rain, and you didn\'t come back for any of us."', "true"),
        c('[Tell it kinder] "You went for help, and got lost in the rain."', "kind_lie")),
    jan("kind_lie", '''"No." {n}She says it before you've finished.{/n}
"That's a kind lie, and it's the worst sort. First blood to me."''',
        c("Continue", "won")),
    jan("true", '''{n}She nods once, as if you had touched her on the guard and not the body. No blood.{/n}
"My turn. Your part." {n}She tells it fast and flat, like a report.{/n} "You came over the wagon tongue with your weapon already out. You killed the first thing out of the rain before Elan had his shield up, and you shouted for us to form on the fire. I was on your left. I remember thinking you looked like somebody painted on a temple wall, and hating you a little for it."''',
        c("Continue", "her_tale")),
    jan("her_tale", '''"Then the second wave came, and you turned to meet it, and I dropped my sword in the mud before the first of them was over the barricade, and I ran."
{n}She stops, and waits for you to find the lie, if there is one.{/n}''',
        c("[Perception] Go back over that night, stroke by stroke, and look for the lie in hers.",
          check=dict(Skill="SkillPerception", DC=20, Success="caught", Failure="missed")),
        c('[Let her finish] "No blood. It\'s true."', "drawn")),
    nar("caught", '''{n}You remember the mud, the fire, the second wave. You remember a half-elf on your left with an Aldori blade, and the blade was not in the mud. It was in the first demon over the barricade, to the hilt, and she had to put her boot on its chest to get it back out. She ran after that. Not before.{/n}''',
        c('"You didn\'t drop your sword. You killed the first one over the barricade, and then you ran. You\'ve been telling it worse than it was."', "yield")),
    jan("yield", '''{n}She opens her mouth to say no, and nothing comes out. You watch her go back through it herself: the mud, the fire, her boot on its chest.{/n}
"...First blood." {n}She says it very quietly.{/n} "To you. Seven years in the circles of Mivon and I never bled first, and I lose my record in a cell, to a story, on a lie I told against myself."
{n}She leaves the practice sword where it lies inside the circle.{/n} "Say it, then. What comes next."''',
        c('"You walk out of this cell. The wagon goes without you."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS)),
        c('"You stay in Drezen, where I can watch you not running."', "stay", flags=(CAUGHT, RETURNED, STARTED, FIRST_LOSS))),
    jan("stay", '''"The wagon goes without me." {n}She gets off the bunk and stands, and doesn't seem to know what to do with her hands.{/n}
"All right. By the forms. Don't expect me to be grateful. The forms don't say anything about grateful."''',
        c("[Leave her the cell for the night.]")),
    nar("missed", '''{n}You go back over it and find nothing. The mud, the fire, the second wave: it all sits where she put it. If there is a lie in her telling, it is buried deeper than your memory reaches.{/n}''',
        c('[Bluff] Name a lie anyway: "The fire was on the right, not the left. You weren\'t where you say you were."',
          check=dict(Skill="CheckBluff", DC=26, Success="false_blood", Failure="false_caught")),
        c('[Let her finish] "No blood. It\'s true."', "drawn")),
    jan("false_blood", '''{n}She frowns. You watch her go back over the camp, looking for the fire, and not be sure.{/n}
"...Maybe. Maybe it was on the right. I've told it to myself so many ways I can't find the edges any more." {n}Her mouth twists.{/n}
"Then that's first blood. To you. My record, gone in a cell, over a campfire."''',
        c('"You walk out of this cell. The wagon goes without you."', "stay_false", flags=(LIED, SECRET, RETURNED, STARTED, FIRST_LOSS))),
    jan("stay_false", '''"The wagon goes without me." {n}She sits there a while longer, frowning at the circle as if it had cheated her and she can't work out how.{/n}
"By the forms, then. I'll stay. And I'll think about that fire."''',
        c("[Leave her the cell for the night.]")),
    jan("false_caught", '''{n}Her eyes come up off the floor and fix on you, and for a heartbeat she looks exactly like what she is: a duellist who has seen a feint.{/n}
"No. The fire was on the left. I had its smoke in my face the whole time." {n}She almost smiles.{/n} "That's a lie, Commander. First blood to me."''',
        c("Continue", "won")),
    jan("drawn", '''"No blood?" {n}She looks at you with something close to pity.{/n}
"Then the tale's drawn, and a drawn bout goes to the one who was challenged. That's me."''',
        c("Continue", "won")),
    jan("won", '''"So. The wagon." {n}She picks the practice sword up out of the circle and lays it across her knees again.{/n}
"You fought fair enough. You just lost. It happens. It happened to me at Houndheart, only there I didn't stay to lose properly."''',
        c("[Let the forms stand.]", flags=(POSTED,))),
    jan("let_go", '''{n}She nods, the small nod of a fencer acknowledging a touch she saw coming.{/n}
"Thank you. I mean it." {n}She leans her head back against the wall.{/n} "Go on, Commander. Somebody up there needs you more than a deserter in a cell does."''',
        c("[Leave her to the wagon.]", flags=(CLOSED, GONE))),
], requires=(IN_CELLS,), forbids=(DEAD, DEAD_KNOWN, RETURNED, POSTED), delay=12,
    TricksterDevice=True, TricksterState="alive")


visit(P + "alive.wagon", "The ninth bell, and after", [
    nar("open", '''{n}Twelve days after the Condemned wagon went north, the gate sergeant sends up word that one of it has come back.{/n}
{n}She comes into your quarters grey with road dust, her gambeson slit along one sleeve and sewn shut again with a Condemned surgeon's black thread.{/n}''',
        c("Continue", "old_scar", requires=(JOINED,)),
        c("Continue", "old_scar", requires=(REFUSED,), forbids=(JOINED,)),
        c("Continue", "new_scar", forbids=(JOINED, REFUSED))),
    nar("old_scar", '''{n}The old scar on her right temple has a new one across it now, still angry, badly knitted. She stands in front of your table and waits to be looked at.{/n}''',
        c("Continue", "ford")),
    nar("new_scar", '''{n}There is a cut on her right temple from the brow to above the ear, still angry and badly knitted. She stands in front of your table and waits to be looked at.{/n}''',
        c("Continue", "ford")),
    jan("ford", '''"Half the wagon came back. We held a ford on the north road for three days against things with too many legs, and nobody in my file ran. I didn't either." {n}She touches the stitches at her temple, briefly, like a fencer touching the button on a foil.{/n}
"I'd like that written down too."''',
        c("Continue", "said")),
    jan("said", '''"I won in your cell. You yielded. Under the forms the winner says the end of the matter, and I didn't say it before the wagon left, because I didn't know it yet."
"I do now. I'm staying. Not because you won; you didn't. Because I did, and it's mine to say."''',
        c('"Then stay."', "stay", flags=(RETURNED, STARTED, STORY_LOST, POSTING)),
        c('"Good. I was about to send somebody after the wagon."', "cheat", flags=(RETURNED, STARTED, STORY_LOST, POSTING)),
        c('[Refuse her] "You won. You went. That was the end of it."', "refused", flags=(CLOSED, GONE))),
    jan("stay", '''"Good." {n}She sits down on the corner of your table without being asked, as if she has been sitting there for years.{/n}
"I'll take the old cell back. Nobody else wants it, and I've got used to the way the turnkey snores."''',
        c("[Let her have the cell.]")),
    jan("cheat", '''"Then you'd have lost twice, and cheated once, and I'd have had to challenge you properly." {n}The corner of her mouth goes up.{/n}
"I'll take the old cell back. Nobody else wants it."''',
        c("[Let her have the cell.]")),
    jan("refused", '''{n}She takes it standing, the way she took the wagon: heels together, chin up.{/n}
"All right. That's a fair reading of the forms. Not the only one." {n}She salutes you, flat of the blade to the brow, and goes out the way she came in, not running.{/n}''',
        c("[Let her go.]")),
], requires=(POSTED,), forbids=(RETURNED,), delay=144, TricksterDevice=True, TricksterState="alive")


# --- The commit (her proposal, in public): the challenge at the muster. -----------------------------------------------

meet(P + "challenge", "If I draw first blood", '"You look like someone about to do something in public."', [
    nar("open", '''{n}She is on the bunk with her sword across her knees, rolling a stick of fencer's chalk between her fingers. The blade has been cleaned and oiled and the grip rewound in new leather. She has done her hair, which you have never seen her bother to do.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Muster's at the fourth bell. The whole yard: your sergeants, Irabeth's Watch, the smith's boys on the smithy roof, anyone with a reason to be late for drill." {n}She tosses the chalk and catches it.{/n}
"I'm going to challenge you. There, in front of all of them. By the forms, the way it's done in Mivon, where everybody can see who asked and who answered."''',
        c("Continue", "lie", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "why", forbids=(LIED,)),
        c("Continue", "why", requires=(LIED, CONFESSED))),
    jan("lie", '''"One thing first, before I chalk a circle with you in it." {n}She stops rolling the chalk.{/n}
"In my cell you caught me in a lie about the fire at Houndheart. I've gone over it every night since. The fire was on the left. I had its smoke in my face. You caught me in a lie I never told, and I gave you my record for it."
"I'm not asking you anything. I'm telling you I know. You can say so now, or you can say nothing, and I'll still walk out to that muster."''',
        c('[Confess] "Yes. I lied. I missed the real one, and I wanted you out of that cell more than I wanted to win clean."',
          "confessed", flags=(CONFESSED, SECRET_KNOWN)),
        c('"The fire was on the right."', "held", flags=(HELD_LIE, SECRET_KNOWN))),
    jan("confessed", '''"There." {n}She lets out a breath she seems to have been holding since the cell.{/n}
"That's what it looks like when somebody's caught in a lie and says so. My master called it the only honest yield there is. I'll take it." {n}She points the chalk at you.{/n} "The real one was mine, by the way. I found it. I'm not telling you where."''',
        c("Continue", "why")),
    jan("held", '''{n}She looks at you exactly as long as it takes a fencer to decide a feint isn't worth answering.{/n}
"All right." {n}She puts the chalk in her pocket and stands.{/n} "Fourth bell."''',
        c("Continue", "yard")),
    jan("why", '''"You want to know why." {n}She doesn't wait for you to say it.{/n}''',
        c("Continue", "why_cage", requires=(SCAR,)),
        c("Continue", "why_cell", requires=(FIRST_LOSS,), forbids=(SCAR,)),
        c("Continue", "why_won", forbids=(FIRST_LOSS,))),
    jan("why_cage", '''"Because I lost to you in a cage, and everybody who saw it thinks they watched an execution. Nobody in Drezen has seen Jannah Aldori cross blades with anyone. They've only heard about her running, and then about her dying."
"They're going to see. And they're going to hear what I put on it."''',
        c("Continue", "stake")),
    jan("why_cell", '''"Because I lost to you in a cell, to a story, and the only one who saw it was a turnkey. Nobody in Drezen has seen Jannah Aldori cross blades with anyone. They've only heard about her running."
"They're going to see. And they're going to hear what I put on it."''',
        c("Continue", "stake")),
    jan("why_won", '''"Because I beat you in a cell and the only one who saw it was a turnkey. Nobody in Drezen has seen Jannah Aldori cross blades with anyone. They've only heard about her running."
"They're going to see. And they're going to hear what I put on it."''',
        c("Continue", "stake")),
    jan("stake", '''{n}She puts the chalk in your hand and closes your fingers over it.{/n}
"When I name the stake, it will be this: if I draw first blood, you're mine. Out loud, at the muster. The Commander of the crusade, staked on a bout with a deserter."
"If you draw first, you say what you like over me, and I'll know what you mean by it." {n}The corner of her mouth moves.{/n} "Either way, the first touch is the answer. You'll know to which question."''',
        c('"Fourth bell. I\'ll be there."', "yard"),
        c('[Flirt] "And if I\'d rather lose?"', "rather"),
        c('"Not in front of the muster. Ask me somewhere else."', "not_there")),
    jan("rather", '''"Then you'd better be very good at it, because I'll know." {n}She takes the chalk back out of your hand.{/n}
"Don't you dare throw a bout of mine, Commander. Not that one. Not ever."''',
        c("Continue", "yard")),
    jan("not_there", '''"No. Somewhere else is where I ran." {n}She takes the chalk back.{/n}
"It's the muster or nothing. Come and find me when you've got the nerve for it. I'll be here. Obviously."''',
        c("[Leave her with the chalk.]", abort=True)),
    nar("yard", '''{n}The yard at the fourth bell is full the way only a yard with a rumour in it gets full. Sergeants who should be drilling. The Eagle Watch in their blue. The smith's boys on the smithy roof with their legs dangling. Irabeth at the barracks door, with her arms folded and her face arranged into nothing at all.{/n}
{n}Jannah walks into the middle of it and draws a circle on the sand with her chalk, three paces across, in one stroke, without looking down. The yard goes quiet.{/n}''',
        c("Continue", "challenge")),
    jan("challenge", '''{n}She steps into the circle and draws. The long blade comes up to her brow in the salute, and she says it loud enough for the gate guards to hear:{/n}
"Jannah Aldori, of Mivon, recruit of the Eagle Watch, who ran at the Houndheart camp. I challenge the Commander of the crusade, by the forms, to the first blood."
"The stake: if I draw first blood, you're mine."
{n}On the smithy roof somebody drops a hammer.{/n}''',
        c("[Step into the circle and salute.]", "bout", forbids=(HELD_LIE,)),
        c("[Step into the circle and salute.]", "thrown", requires=(HELD_LIE,))),
    nar("bout", '''{n}She comes at you the way she must have come at everyone in Mivon for seven years: on the balls of her feet, the blade low and quick and never where you are looking. She isn't trying to hit you. She's trying to take the sword out of your hand, the Aldori way, and twice she very nearly does.{/n}''',
        c("[Mobility] Stay out of her measure and wait for her to overreach.",
          check=dict(Skill="SkillMobility", DC=28, Success="you_first", Failure="her_first")),
        c("[Athletics] Bind her blade and drive through it.",
          check=dict(Skill="SkillAthletics", DC=28, Success="you_first", Failure="her_first")),
        c("[Leave a line open and let her take it.]", "no_gift")),
    jan("no_gift", '''{n}She sees the opening, and doesn't take it. She steps back out of measure and lowers her blade, and the whole yard hears her:{/n}
"Don't you dare. Fight me, or get out of my circle."''',
        c("[Take your guard again.]", "bout_again")),
    nar("bout_again", '''{n}She comes in again, faster, angrier, and now she is trying to hit you.{/n}''',
        c("[Mobility] Stay out of her measure and wait for her to overreach.",
          check=dict(Skill="SkillMobility", DC=28, Success="you_first", Failure="her_first")),
        c("[Athletics] Bind her blade and drive through it.",
          check=dict(Skill="SkillAthletics", DC=28, Success="you_first", Failure="her_first"))),
    nar("you_first", '''{n}She overreaches by a hand's breadth. It's enough. Your point takes her high on the sword arm, through the gambeson, and a line of red opens on the sleeve. First blood.{/n}
{n}She lays her blade down on the sand, lies back inside the chalk, and fixes her eyes on the sky. The whole yard waits for the Commander to say something over her.{/n}''',
        c('"Mine."', "you_mine", flags=(COMMITTED, YOU_FIRST, FIRST_LOSS)),
        c('"You fought well. Get up."', "you_up", flags=(COMMITTED, YOU_FIRST, FIRST_LOSS))),
    jan("you_mine", '''{n}Flat on the sand, eyes on the sky, Jannah Aldori laughs: the old laugh from the tavern in Kenabres, much too loud for a yard full of soldiers.{/n}
"That wasn't the stake." {n}She doesn't move a finger.{/n} "Help me up. I'm not allowed to do it myself until you've quit the circle, and you're not quitting it, are you?"''',
        c("[Pull her up off the sand.]", "after")),
    jan("you_up", '''{n}She gets up. The yard is staring. She ignores it, sheathes, touches two fingers to the cut on her arm and then to your mouth, in front of every one of them.{/n}
"First touch," she says. "You know to which question."''',
        c("Continue", "after")),
    nar("her_first", '''{n}You never see it coming. A turn of her wrist, a flicker of steel inside your guard, and a sting along your jaw; when you touch it your fingers come away red. First blood.{/n}
{n}Jannah stands inside the chalk with her blade lowered, breathing hard, and waits to see what the Commander of the crusade does with the forms in front of the whole muster.{/n}''',
        c("[Lay down your weapon, lie back inside the circle, and keep your eyes on the sky.]", "her_mine",
          flags=(COMMITTED, SHE_FIRST, PUBLIC_YIELD)),
        c("[Wipe the blood off your jaw and walk out of the circle.]", "walked_off", flags=(REFUSED_YIELD, CLOSED))),
    jan("her_mine", '''{n}Four hundred soldiers watch their Commander lie down on {mf|his|her} back in the sand inside a deserter's chalk circle, eyes open, not moving. It is so quiet you can hear the smith's forge breathing.{/n}
"Mine," Jannah says, to you. Then, louder, to the yard: "The Commander is mine. By the forms. Does anybody here want to argue with an Aldori?"
{n}Nobody on the smithy roof wants to. She quits the circle, as the forms require, so that you're allowed to move. Then she steps straight back into it and pulls you up by both hands.{/n}''',
        c("Continue", "after")),
    jan("walked_off", '''{n}The yard watches you walk out of the chalk with blood on your jaw, as if the forms were a game she had made up to pass the time in a cell.{/n}
{n}Jannah doesn't follow. She stands in the middle of the circle with her blade lowered and says, quite clearly, so that everyone hears it: "Then it wasn't a bout. It was a brawl, and I don't give my stakes to brawlers."{/n}''',
        c("[Keep walking.]")),
    jan("after", '''{n}Later, when the muster has been dismissed three times and still hasn't gone anywhere, she walks you round behind the barracks to the practice yard. There is nobody in it: sand, a trough, a rack of blunted blades.{/n}
"Tonight. Here. Bring your sword and leave your rank in the barracks." {n}She looks at the sand, and then at you, and her ears have gone pink at the points.{/n} "I'll bring the chalk."''',
        c("[Watch her go.]")),
    nar("thrown", '''{n}She comes at you exactly as she promised, fast and low, and for three passes it is the best bout the yard has ever seen. Then, in the middle of the fourth, her guard simply isn't there. She leaves the line open and walks onto your point, and it opens her forearm from the wrist to the elbow.{/n}
{n}Four hundred soldiers see Jannah Aldori lose. A few of the Eagle Watch see her throw it. You see her throw it.{/n}''',
        c("Continue", "thrown_her")),
    jan("thrown_her", '''{n}She lays her blade on the sand and lies back with her eyes on the sky, as the forms require, and bleeds.{/n}
"First blood to the Commander," she says, to nobody at all. "Say what you like over me. I won't be listening."''',
        c("[Quit the circle.]", flags=(DECLINED,))),
], requires=(WALLS,), forbids=(COMMITTED, DECLINED, REFUSED_YIELD), delay=24)


# The intimacy: the chalked duelling circle in the practice yard at night, the swords on the sand.
visit(P + "circle_night", "Inside the chalk", [
    nar("open", '''{n}At night the practice yard behind the barracks is sand, a water trough, a rack of blunted blades and a sky stained by the Worldwound's wrong-coloured light. The circle is already chalked when you come in. Three paces across, one stroke.{/n}
{n}Jannah is standing in the middle of it in her shirt and breeches, barefoot on the cold sand, with her sword drawn and its point resting between her feet.{/n}''',
        c("Continue", "salute_or")),
    jan("salute_or", '''"Salute, or leave the circle." {n}It is not entirely a joke.{/n}''',
        c("[Draw, and salute her.]", "saluted"),
        c("[Lay your sword on the sand at her feet.]", "laid")),
    nar("saluted", '''{n}She returns it, flat of the blade to the brow, and then lays her sword on the sand. After a moment you lay yours across it, and the two blades lie there crossed, catching the red light.{/n}''',
        c("Continue", "close")),
    jan("laid", '''"No salute?" {n}She looks at your blade lying at her feet, and something in her face gives way.{/n}
"That's a salute too, in Mivon. The oldest one. You just don't know it." {n}She lays her own sword across yours.{/n}''',
        c("Continue", "close")),
    jan("close", '''{n}She steps in, inside measure, where nobody who knows the forms ever stands unless they mean to finish something.{/n}
"In Mivon I never let anyone this close. You don't, if you want to stay unbeaten." {n}Her breath is quick and she isn't hiding it.{/n} "I'm not unbeaten any more. I find I don't mind."''',
        c("Continue", "mark_jaw", requires=(SHE_FIRST,)),
        c("Continue", "mark_arm", requires=(YOU_FIRST,)),
        c("Continue", "mark_late", forbids=(SHE_FIRST, YOU_FIRST))),
    nar("mark_jaw", '''{n}Her thumb finds the cut she gave you at the muster, along the line of your jaw, and follows it all the way, slowly, the way you'd follow the edge of a blade you were proud of.{/n}
"Mine," she says against your mouth, as if testing whether the word still works in private. It does.''',
        c("Continue", "kiss")),
    nar("mark_arm", '''{n}She takes your hand and puts it on her sword arm, on the bandage over the cut you gave her at the muster, and presses until it hurts, and watches your face while it does.{/n}
"You did that. In front of everyone. Nobody ever did that in front of everyone." {n}Her voice has gone low.{/n} "Do it again. Not with the sword."''',
        c("Continue", "kiss")),
    nar("mark_late", '''{n}She takes your hand and lays it on her bandaged forearm, where your point went in when she walked onto it, and holds it there.{/n}
"I threw that one. Never again. From now on, everything in this circle is meant." {n}Her voice has gone low.{/n}''',
        c("Continue", "kiss")),
    nar("kiss", '''{n}She kisses the way she fences: no wasted motion, then everything at once. Her hands are hard from seven years of hilts and they know exactly where your buckles are. Your belt goes. Your coat goes, onto the sand outside the chalk, because she won't have anything in the circle that doesn't belong there.{/n}
{n}You pull her shirt over her head. The Worldwound's light lies red along her ribs. There is almost nothing on her, for a fencer: seven years of circles and she never bled first. The only marks on her are new ones, and she guides your mouth to each of them in turn.{/n}''',
        c("Continue", "down")),
    jan("down", '''"This is where I'd take your sword," she says, breathing hard, her forehead against yours, "if you'd brought it into measure." {n}She pushes her breeches down off her hips with one hand and doesn't let go of you with the other.{/n}
"You did. So I will."''',
        c("[Let her.]", "cut"),
        c("[Take hers first.]", "cut")),
    nar("cut", '''{n}She hooks your heel with hers, the oldest trick in any salle, and takes you down onto the cold sand inside the chalk. The circle smears under your shoulder. Neither of you cares about the forms after that.{/n}''',
        c("[Go down with her.]")),
], requires=(COMMITTED,), forbids=(NIGHT,), delay=0)


meet(MORNING, "A scuffed circle", '"You\'ve got sand in your hair."', [
    nar("open", '''{n}She is back in the last cell, rewinding her sword's grip with a strip of new leather and humming something from Mivon under her breath. She stops humming the moment she sees you. There is sand in her hair and she knows it.{/n}''',
        c("Continue", "talk_yielded", requires=(PUBLIC_YIELD,)),
        c("Continue", "talk_won", requires=(YOU_FIRST,)),
        c("Continue", "talk_late", forbids=(PUBLIC_YIELD, YOU_FIRST))),
    jan("talk_yielded", '''"The whole garrison knows. The sergeants are calling it the Commander's Yield. The Eagle Watch have a song about it already. It rhymes 'Aldori' with 'sorry', and it's terrible, and I've heard it four times since breakfast."''',
        c("Continue", "told")),
    jan("talk_won", '''"The whole garrison knows. They're saying the Commander put the deserter on her back in front of the muster." {n}She pulls the leather tight.{/n} "They're not wrong. They're only talking about the wrong time of day."''',
        c("Continue", "told")),
    jan("talk_late", '''"Half the garrison still thinks I lost to you fairly at that muster. The other half saw me throw it. Neither half has any idea what happened last night, and I intend to keep it that way for at least a week."''',
        c("Continue", "told")),
    jan("told", '''"I've been told three times this morning that you could do better than a deserter. Once by a sergeant, once by a priest, and once by a woman selling pies. I told all three the same thing: the forms don't care what they think."
{n}She tests the grip in her palm.{/n} "Whoever else you've got, Commander, and I've heard things, none of them chalked a circle in front of your muster. I did. You'll remember that."''',
        c('"I\'ll remember."', "houndheart"),
        c('[Flirt] "You hum when you\'re happy."', "hum"),
        c('"Irabeth is going to want a word with me."', "irabeth")),
    jan("hum", '''"I do not." {n}She does, and she knows it, and the points of her ears go pink.{/n} "It's a drinking song from the river docks. It's about a boatman's wife. You wouldn't like the third verse."''',
        c("Continue", "houndheart")),
    jan("irabeth", '''"Irabeth has already had a word with me. She said she spoke for me once, in Kenabres, four days before the demons came, and that she'd like to know what she's speaking for now." {n}Jannah shrugs.{/n}
"I told her: a fencer. She didn't laugh. I think that means she was satisfied."''',
        c("Continue", "houndheart")),
    jan("houndheart", '''{n}She stops working the grip.{/n}
"I didn't think about Houndheart once, last night. Not once. Do you know how long it's been since I went a whole night without it? Since before the cage." {n}She looks at the scratched circle on the cell floor.{/n}
"It'll come back. It always does. But it's got competition now."''',
        c("[Leave her to her grip.]")),
], requires=(NIGHT,), delay=6)


# Her no, answered: a circle left chalked in the yard (no price, no second ask; the truth, said inside it).
visit(P + "chalk_circle", "A circle in the yard", [
    nar("open", '''{n}Three nights after the muster, the practice yard behind the barracks has a circle chalked on its sand, three paces across, in one stroke. Her sword lies across the middle of it.{/n}
{n}She's sitting on the yard wall in the dark with her bandaged forearm across her knees, watching. She doesn't call down.{/n}''',
        c('[Step into the circle] "I lied to you in your cell. I named a lie you never told, because I missed the one you did, and I wanted you out of that cell more than I wanted to win clean."',
          "walked_in", flags=(CONFESSED, COMMITTED, LATE_YES)),
        c("[Leave the circle as it is.]", "left", flags=(CLOSED, GONE))),
    jan("walked_in", '''{n}She comes down off the wall and walks into the chalk, and stops inside measure.{/n}
"That's all I wanted. Not sorry. Just the truth, said out loud, inside the circle, where it counts." {n}She picks up her sword and lays it at your feet.{/n}
"My master would say you owe me a bout. I'm going to collect it somewhere else."''',
        c("[Let her collect.]")),
    nar("left", '''{n}You leave it. In the morning the circle has been scuffed out and the sword is gone, and so is she. The gate sergeant saw a half-elf with her arm in a sling walk out on the south road at first light, alone.{/n}
{n}Not running, he says. He's quite sure. He watched her until she was out of sight.{/n}''',
        c("[Let her go.]")),
], requires=(DECLINED,), forbids=(COMMITTED,), delay=72)


# --- Epilogue pages (Owner JannahEpilogue; appended in authored order; no effects). --------------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}She kept the scar on her temple where it could be seen, and let the Commander trace it exactly once a year, on the anniversary of the Molten Scar, and never on any other day.{/n}", requires=(SCAR,)),
    p("{n}The Eagle Watch never did correct its roll of the dead. Jannah Aldori, recruit, is listed there still, killed in the Molten Scar. She went to look at it sometimes, when she was in a bad mood, and came away cheerful.{/n}", requires=(SCAR,), forbids=(NAMELESS,)),
    p("{n}She fought the rest of the war under no name, as she had been told to, and after the war the Commander offered to give her own back. She said she would think about it. She was still thinking about it years later, and making the Commander ask.{/n}", requires=(NAMELESS,)),
    p("{n}She liked to tell people that the Commander had released her from a yield once, which in Mivon is the highest honour one fencer can pay another, and that she had stayed anyway, which in Mivon is called being a fool.{/n}", requires=(RELEASED,)),
    p("{n}Of the Condemned company she rode north with, half came home. She kept their names on a strip of leather wound under her sword's grip, and rewound it every spring.{/n}", requires=(POSTING,)),
    p("{n}She never let the Commander forget that she had won blood and tale in a gaol cell. When they argued, she would say, \"Drawn bouts go to the one who was challenged,\" and the argument would be over, whether or not anybody had been challenged.{/n}", requires=(STORY_LOST,)),
    p("{n}Every year at the muster she challenged the Commander again, in front of whoever was watching, and named the same stake. The Commander never drew first blood again. Nobody who had seen the first bout believed that was an accident, and nobody said so to her face.{/n}", requires=(PUBLIC_YIELD,)),
    p("{n}Every year at the muster she challenged the Commander again, in front of whoever was watching, and named the same stake, and lost more often than she won, and enjoyed losing enormously, which in Mivon would have been a scandal.{/n}", requires=(YOU_FIRST,)),
    p("{n}She wrote her father the truth about Houndheart. He wrote back that fate had brought her to Mendev, and she wrote back that fate had nothing to do with it. They kept up that argument by letter for the rest of his life, and neither of them ever gave an inch.{/n}", requires=(MIVON_TRUTH,)),
    p("{n}Her father in Mivon died believing his daughter had never lost a bout and never taken a step backwards. She never corrected him. She said some stories belong to the people who need them.{/n}", requires=(MIVON_LEGEND,)),
    p("{n}She and Seelah stayed friends, the kind who argue about everything and turn up for each other anyway. Seelah hit her exactly once, the day she learned Jannah was alive, and never mentioned it again.{/n}", requires=(SEELAH_HERSELF,)),
    p("{n}Seelah learned that Jannah was alive from the Commander, not from Jannah. It took the two of them a long time to find their way back to the tavern table, and they did it without any help from the Commander.{/n}", requires=(SEELAH_FOR_HER,)),
    p("{n}She told the Commander once that on the wall, with the vrocks coming, she had heard the salute called and remembered who she was. She never said whose voice it had been. She didn't have to.{/n}", requires=(WALL_SALUTE,)),
    p("{n}She never quite forgave the Commander for standing on the wall and watching to see whether she would run. She did not run. She said that was the only thing about that night that mattered, and that the watching was the Commander's own business, to carry.{/n}", requires=(WALL_WATCHED,)),
    p("{n}She kept the question of the fire at Houndheart to herself for the rest of her life. Once, very late at night, she told the Commander where her own lie had been in that telling. She made the Commander swear never to repeat it, and the Commander never has.{/n}", requires=(CONFESSED,)),
)
SCENES.append(scene(P + "epilogue.first_blood", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Jannah Aldori, of Mivon, stayed at the Commander's side through the Threshold and after it. She never again wore the Eagle Watch's blue and never asked to; she said a tabard was a promise, and she had broken one already.{/n}
{n}After the war she chalked a circle in a yard and taught the forms to anyone who would stand in it: soldiers, orphans, a one-armed priest, the children of people who had run. She taught the salute, the measure and the yield. She did not teach anyone to stay unbeaten. She said it was a bad habit, and that she was glad to be rid of it.{/n}
{n}She was never cured of Houndheart. Some nights it came back and sat on the end of the bed, and she let it sit there, and did not run from it either.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.commit", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Jannah Aldori got her muster. She had the chalk in her pocket on the day of the Threshold, and she was angry about it for a month.{/n}
{n}In the first spring after, she walked into the yard of the Commander's house at the hour when the household was up and about and drew a circle on the gravel in one stroke. She named the stake loud enough for the neighbours: if I draw first blood, you're mine.{/n}
{n}Who drew first blood is between the two of them. The neighbours said the bout lasted a very long time, and ended with both of them sitting in the gravel inside the chalk, laughing, and that nobody could say afterwards who had yielded to whom.{/n}''',
        paragraphs=(
            p("{n}She kept the scar on her temple where it could be seen.{/n}", requires=(SCAR,)),
            p("{n}Of the Condemned company she rode north with, she kept the names under her sword's grip.{/n}", requires=(POSTING,)),
        ))],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.declined", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Jannah Aldori stayed in Drezen until the war was over, in the last cell of the old gaol, with its door open. She trained with the Eagle Watch, fought where she was sent and never ran, and never once crossed blades with the Commander again.{/n}
{n}When the crusade broke up she went home to Mivon. People who knew her there said she had come back quieter, and a better fencer than when she left, and that she would not talk about the man or woman who had beaten her with a lie.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), **EP))

SCENES.append(scene(P + "epilogue.gone", "", "JannahEpilogue", 6, "", [
    nar("page", '''{n}Nobody in Drezen saw Jannah Aldori again. A half-elf fencer with a scar on her temple was said to be teaching the forms in a river town far to the south, in a salle above a dye-works, and to be very hard on students who ran from a bout.{/n}
{n}She was said to be unbeaten, too, though the people who said so had never seen her lose, which is not the same thing.{/n}''')],
    requires=("trickster.ever", GONE), forbids=(COMMITTED,), **EP))


# --- Reactions: exactly the allocated two reactors (ledger 05 §3.1 row 24): Irabeth, and King Thaberdine. ------------------

IRABETH_GONE = ("irabeth_dead",)
IRABETH_BACK = {"irabeth_dead": "irabeth.trickster.returned"}
KING = dict(answer_list=KING_C5, speaker="conversant", NativeReturnCue=KING_C5_RETURN, forbids=("fool_king.gone",),
            chapter=5, last=5, Chapters=[5])

SCENES.append(reaction("Irabeth", P + "react.irabeth_rolls", (RETURNED, DEAD_L),
    '''{n}Irabeth has a ledger open in front of her and has not turned a page since you came in.{/n}
"The Eagle Watch struck Jannah Aldori from its rolls in the winter. Dead in the Molten Scar, by your hand. I signed it. Now there's a half-elf in your gaol giving that name and wearing a scar I'd know anywhere, because I've seen your blade work."
"I'll need to know what to write, Commander. 'Came back' isn't a column."''',
    answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=5, last=5, Chapters=[5], entry='"About the deserter in the gaol..."',
    portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Irabeth", P + "react.irabeth_wagon", (RETURNED,),
    '''{n}Irabeth doesn't look up from her dispatches.{/n}
"The Condemned sergeant came to me this morning. One short on his roll, and the one missing is sitting in your gaol on your leave. I spoke for that girl once, when she appealed to the Queen. I thought she'd earned a chance to die usefully."
{n}She sets down the pen.{/n} "Now she's earned a chance to live usefully, apparently. See that she does."''',
    answer_list=IRABETH_HUB, forbids=(*IRABETH_GONE, DEAD_L), chapter=5, last=5, Chapters=[5],
    entry='"About the deserter in the gaol..."', portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Irabeth", P + "react.irabeth_sand", (PUBLIC_YIELD,),
    '''"You lay down in the sand in front of my sergeants." {n}Irabeth says it the way she would read out a charge.{/n}
"The whole muster. Flat on your back inside a deserter's chalk, with your eyes on the sky, because she cut your jaw and some rule from Mivon said you had to."
{n}She is quiet a moment.{/n} "I've never seen anything like it. Half of them think less of you for it. The other half would walk into the Worldwound behind you tomorrow. I haven't decided which half I'm in."''',
    answer_list=IRABETH_HUB, forbids=IRABETH_GONE, chapter=5, last=5, Chapters=[5], entry='"You heard about the muster."',
    portrait="Irabeth", ForbidOverrides=dict(IRABETH_BACK)))

SCENES.append(reaction("Thaberdine", P + "react.king_gaol", (RETURNED, "fool_king.available"),
    '''"Commander! Is it true? A woman walked into the gaol and asked for a cell?" {n}The King is appalled.{/n}
"In my kingdom people ask to be let out of them. Usually through me. Usually drunk. I've issued a decree: the half-elf in the last cell is to have the good blanket, on account of she's the only honest prisoner in the realm and it's making the others look bad."''',
    entry='"Your Majesty. Heard any news from the gaol?"', **KING))

SCENES.append(reaction("Thaberdine", P + "react.king_muster", (COMMITTED, "fool_king.available"),
    '''"I saw it! From the roof of the tavern, with a glass! Well. A bottle. Pointed the right way." {n}The King waves his mug at the ceiling.{/n}
"A circle in the sand! Swords! A stake called out loud in front of the whole garrison! That's how it should be done, Commander. None of this whispering in corridors. I'd knight her, if I remembered how, and if she wouldn't cut me for it."''',
    entry='"You were at the muster, Your Majesty?"', **KING))


# --- Registration helpers ------------------------------------------------------------------------------------------------

household.secret("jannah_false_blood", "The fire at Houndheart",
                 "In the gaol, playing her master's game, I missed the lie she told against herself and named one she "
                 "never told: the fire, left or right. She believed me, and gave me her record for it. She is in Drezen "
                 "on the strength of a campfire I moved.", portrait="Jannah", witnesses=("jannah",), risk="high")


def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the relationship's own derived keys, its presence and its portrait fallback. Scenes are added by
    expansion.py; world keys the matrix already verified (jannah.dead, joined, seelah.q3_started...) bind on demand."""
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    # The unit's own BlueprintPortrait (CR4_DeserterJanna m_Portrait) until custom art ships; a custom PNG always wins.
    payload.setdefault("PortraitFallbacks", {}).setdefault("Jannah", "550a859fc62244ceadeb40d79ca4d261")
