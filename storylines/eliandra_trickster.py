"""Eliandra on the Trickster path: "A sacrifice in her place" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, Eliandra block and
build sheet, rewritten 2026-09-29 (R4) after Astra design review r4; it supersedes the lapsing century and the tablet and
epitaph device of Writer/handoffs/trickster/eliandra.md, whose canon research stays valid). Replaces the unregistered draft
eliandra_trickster_opening.py, whose ids were never merged or registered.

Canon (blueprints.zip / enGB):
- PuluraFall_Eliandra (e349079a, ChaoticGood aasimar), high priestess of Pulura. "She has never married or had a family, but
  has devoted herself entirely to service. In return, the Shimmering Maiden has rewarded Eliandra for her sacrifice - she
  has always been the strongest of Pulura's priestesses." (HeraldPulura/Cue_0009 24d719b4). "That was when I learned this
  difficult task would take a century to complete, and that it would require us to make many sacrifices. But I was
  willing." (Elyandra_main/Cue_0033_EliAree f47a3ba1; its Ch5 twin PuluraLeaderSaved/Cue_0021 17680734).
- "My Lady hid this place from unfriendly eyes, and prolonged the lives of everyone inside" (PuluraLeaderSaved/Cue_0026
  cb48db97, the hub's return cue); "Whether it is day or night, the stars are always visible within the heart of this
  sanctuary" (Elyandra_main/Cue_0024 f295b069); the veil, as her enemy describes it: "colorful flashes, magic that deflects
  the gaze, and obscures the vision... Pulura, the mistress of bright lights" (EchoChapel/Cue_0011 b32ce500); "The mistress
  of the Aurora Iobara" (HeraldPulura/Cue_0004 e002c87d).
- Her ban on love: Vestari and Cristry, "five quarrels and six reconciliations all between one moonrise and the next... I
  decided to forbid all romantic relationships in the temple" (Elyandra_main/Cue_0050 09ace5be; Cue_0002 c9f74d93).
- Ch5, after Mutasafen's raid: "we will have to leave. Our mission is finished." (Katair, Cue_0029 7ca8fc49) or, when he is
  not there, her own "It breaks my heart to leave this place... Someday, our waterfalls will sing again..." (Cue_0030
  28e3b35d). The epilogue she keeps on every path: "Eliandra, who had given almost her entire life over to duty, devoted
  herself to the revival of the former lands of Sarkoris." (Epilogues/Cue_0529 05d756a2).

What the Trickster actually meets (verified in the etudes; the build sheet assumed a Ch3 meeting):
- Ch3: Pulura_NPC_Eliandra_DefaultActor (a048f51d) hides her on every path; only the Angel Pulura_Stage_* etudes unhide her.
  The Trickster reaches the chiefs' ground below her dry fall for the Fool King's tablet (FoolKing_Tavern Answer_0025) and
  never sees the shrine. So the first meeting is Ch5 (PuluraLeaderSaved/Cue_0001, "for everyone"), and the build sheet's
  Ch3 beats (the terms, the rite) move to her Ch5 hub; RangerAlarm/Cue_0003 ("It worked!") is Angel-only and is not read.
- Ch5: Pulura_Chapter05_Mechanics spawns Katair only when Eliandra was stolen (Angel), so off the Angel path he is away and
  her own Cue_0030 plays for "What will happen to the sanctuary now?"; eliandra.shrine_left binds Cue_0029 or Cue_0030. The
  same etude lays out the corpses of Regnard (RegnardTrained never set), Taeriell (TaerillOK), Vestari and Cristry
  (LoversAllowed): off the Angel path they died in the raid. Odden lives.
- Authored and labelled in her voice: Katair was beyond the walls (he "goes out alone"; the Stone Tree talk is Taeriell's,
  Taerill/Cue_0025), and comes back.

The device (11 §2, R4): a sacrifice in her place, inside Pulura's own rule that what is given up for her is answered. The
Commander makes an offering in her last rite at the star-heart, for her leave from the vow only her Lady can lift. Earned
access: the terms (Lore Religion 20) or one evening observation; the Ch3 memory of the chiefs' ground shows the Commander
the Maiden's lights through her veil. Gold is refused; a hand kept behind the back ends the rite; the lights, offered in
form, are taken (Lore Religion 24, 18 with the terms), or a counteroffer read in the basin takes her Lady's reward too, and
she chooses. Refused, walked away or caught: 48 hours later she makes the offering herself. No raise, no death, nothing
written. Pulura never speaks on the page. Cost: the Commander never sees Pulura's lights again (her veil, turned on one
person); on the counteroffer or her own offering she is no longer the strongest of her Lady's priestesses.

Path fit (ROUTE-BRIEF-R §2, v1): scenes are tagged in PATH_FIT. N-fit build-up at the shrine carries no Trickster gate and
is shut on Demon, Devil, Lich and Swarm (a Chaotic Good priestess of the stars) and on Angel (where she was met in Ch3 and
Katair and the dead differ); T scenes need the Trickster. No non-Trickster commit or ending is written here (v2).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
REL = "eliandra"
E = "eliandra.trickster."

UNIT = "e349079a648cb15448a27f9049344bf1"            # PuluraFall_Eliandra
PORTRAIT_GUID = "613e7ca6932b447694754f02d043454c"   # BCT_EliandraFinal (her unit's m_Portrait)
KATAIR_PORTRAIT = "19f87509cfcd401a97518a71f1651996" # BCT_Katair (PuluraFall_Katair 4659d2d7)
ODDEN_PORTRAIT = "bbfb558ba59741b687279c0f6afddc1b"  # BCT_Pulura_Odden (PuluraFall_Odden 0620c22a)
DREZEN = "2570015799edf594daf2f076f2f975d8"          # DrezenCapital
HUB = "6073e28cab0691542b85a24436ed919c"             # c5/PuluraFallsC5/PuluraLeaderSaved/AnswersList_0008
RET = "cb48db9773f775b428f0a5f20757145e"             # PuluraLeaderSaved/Cue_0026 "This is Pulura's Fall..." (clean return)
RETURN_TEXT = "{n}Eliandra folds her hands and waits, tired and patient, for whatever you mean to ask next.{/n}"

STARTED = "eliandra.started"
CLOSED = "eliandra.closed"
COMMITTED = "eliandra.committed"
# Native keys.
DEAD = "eliandra.dead"                    # EliandraDead (Angel-only producer; never true on Trickster)
MET = "eliandra.met_ch5"                  # PuluraLeaderSaved Cue_0001/0002/0003 (trickster_world)
SHRINE_LEFT = "eliandra.shrine_left"      # PuluraLeaderSaved Cue_0029 (Katair) or Cue_0030 (hers) (trickster_world)
TABLET = "fool_king.tablet_brought"       # FoolKing_Tavern/Answer_0025: the stone from the chiefs' ground near her shrine
SIGHT = "trickster.perception_tier1"      # TricksterPerceptionTier1Feature: "You see more than other people."
LIGHTS_LIT = "eliandra.northern_lights_awakened"   # NorthernLights/Answer_0003 "[Awaken the artifact]" at Threshold (page variant)
# Path gates (story.py bindings): N-fit build-up is shut on the paths that do not fit her, and on Angel, whose Ch5 differs.
UNFIT = ("demon", "devil", "lich", "swarm", "angel")

# Chapter 3 and 4 (the Commander alone).
LIGHTS_SEEN = E + "lights_seen"           # watched the Maiden's lights through the veil at the chiefs' ground (Ch3)
WINE_LEFT = E + "wine_left"               # ...and left the King's wine at the foot of the dry fall for whoever watched
ABYSS_DARK = E + "abyss_dark"             # looked for them under the Abyss's red sky (Ch4)
# Chapter 5, the shrine (N-fit build-up).
DEAD_NAMED = E + "dead_named"
LIGHTS_TOLD = E + "lights_told"           # told her the Commander saw her Lady's lights from outside
LOVERS_TRUTH = E + "lovers.truth"         # told her plainly that her rule kept the lovers apart
LOVERS_SPOKEN = E + "lovers.spoken"
FLIRTED = E + "flirted"                   # the Commander said, at her observation, that it was not the stars being watched
OBSERVED = E + "observed"
SARKORIS_TOLD = E + "sarkoris.told"
SARKORIS_LIE = E + "sarkoris.kind_lie"
REMEMBRANCE = E + "remembrance"
TOASTED = E + "toasted"
HEALING_SEEN = E + "healing_seen"
# The device.
TERMS_READ = E + "terms_read"
TERMS_GUESSED = E + "terms_guessed"
OFFER_REFUSED = E + "offer_refused"
LEAVE = E + "leave_granted"
NO_LEAVE = E + "no_leave"
REFUSED_FOR_HER = E + "refused_for_her"
TRIED_TO_CHEAT = E + "cost.tried_to_cheat"
LIGHTS_GIVEN = E + "cost.lights_given"    # the Commander never sees Pulura's lights again
REWARD_RETURNED = E + "cost.reward_returned"  # no longer the strongest of her Lady's priestesses
# The commit and after.
DECLINED = E + "declined"
LETTER_ANSWERED = E + "letter_answered"
HEART_SEEN = E + "heart_seen"
CHARTS = E + "charts"                     # the morning after: Katair finds the charts rolled up wrong
LATE_COMMITTED = E + "late_committed"

PATH_FIT = {}                             # scene id -> "T" | "N-fit" | "N-all" (ROUTE-BRIEF-R §2, path fit v1)

BINDINGS = {
    "Etudes": {# Pulura_MutasafenStoleProject: the demon got away with the stargazers' work (read for variants only).
               "eliandra.research_stolen": "c946f95a3f79eaa429799db96538fc07"},
    # c6/ThresholdExterior/NorthernLights/Answer_0003 "[Awaken the artifact] It is time to clear the sky over Threshold!"
    "SelectedAnswers": {LIGHTS_LIT: "984d9d1432ea89044a6515be61a22125"},
    # RamienPulura/Cue_0007: the Desnan's dream of the northern lights and a priestess at the waterfall (a Drezen beat reads it).
    "SeenCues": {"eliandra.ramien_dream": ["cb2989159fadb0f48a7c5d0affdedfe2"]},
    "MainCharacterFacts": {SIGHT: "8bc2f9b88a0cf704ea72d86c2a3e2aef"},
}

DERIVED = {
    # R2-6: after the soft no, her letter from the fords kept and its answer promised for after the war; the late page answers it.
    LATE_COMMITTED: [["trickster.ever", E + "letter_kept"]],
    # 05 §2.5 voice note: she joins asking, every morning, the thing she once never asked anyone.
    "eliandra.harem.voice.asks_every_morning": [[COMMITTED]],
}

RELATIONSHIP = dict(
    Title="A Sacrifice in Her Place",
    Description=("Eliandra kept Pulura's hidden shrine for a hundred years and gave her Lady everything she had when she was "
                 "thirteen. Her Lady answered with strength. The shrine is found now, and the stargazers are leaving it, and "
                 "the vow still holds her. Only the Maiden can let her go."),
    Objective="Ask the Shimmering Maiden to let Eliandra go",
    Guidance=("On the Trickster path, in Chapter 5, after the demons' raid on Pulura's Fall. Ask Eliandra who was lost, "
              "learn how her Lady takes an offering, or watch her last evening observation. Then ask her for one last rite "
              "at the star-heart."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD], FailureFlags=[], UnavailableOverrides={},
    TricksterAccess={
        "vow": dict(detect=[MET], device=E + "ch5.last_rite", returned=LEAVE),
        "no_leave": dict(detect=[NO_LEAVE], device=E + "ch5.self_offering", returned=LEAVE),
    },
)


def el(id, text, *choices, **kw):
    """Eliandra, inline in her own Ch5 dialog (the native conversant)."""
    return n(id, "conversant", text, *choices, **kw)


def nar(id, text, *choices, **kw):
    """Narration inside her native dialog."""
    return n(id, "Narrator", text, *choices, **kw)


def ep(id, text, *choices, **kw):
    """Eliandra on a rest-delivered page."""
    return n(id, "Eliandra", text, *choices, portrait="Eliandra", **kw)


def pn(id, text, *choices, portrait="Eliandra", **kw):
    """Narration on a rest-delivered page."""
    return n(id, "Narrator", text, *choices, portrait=portrait, **kw)


def kt(id, text, *choices, **kw):
    """Katair on a rest-delivered page (he is never spawned off the Angel path in Chapter 5)."""
    return n(id, "Katair", text, *choices, portrait="Katair", **kw)


def shrine(id, title, entry, nodes, requires, forbids=(), fit="N-fit", delay=0, **extra):
    """A beat inline on her Ch5 hub (PuluraLeaderSaved/AnswersList_0008, back to Cue_0026). N-fit: no Trickster gate,
    shut on the paths that do not fit her; T: the live Trickster."""
    gate = ("trickster",) if fit == "T" else ()
    shut = UNFIT if fit != "T" else ()
    PATH_FIT[id] = fit
    # Cue_0026 (her "This is Pulura's Fall..." exposition) is engine-safe but reads oddly replayed after grief or the rite's
    # aftermath, so scenes without a check return to her list with a short line instead (E14b); scenes with a check, which
    # ReturnToList cannot carry, keep the clean native return.
    has_check = any(ch.get("Check") for nd in nodes for ch in nd["Choices"])
    back = dict(NativeReturnCue=RET) if has_check else dict(ReturnToList=True, ReturnText=RETURN_TEXT)
    SCENES.append(scene(id, title, "Eliandra", 5, entry, nodes,
                        requires=tuple(dict.fromkeys((*gate, MET, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, DEAD, *shut, *forbids))), delay=delay, last=5,
                        Relationship=REL, Chapters=[5], AnswerLists=[HUB], **back, **extra))


def page(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="visit", owner="Eliandra", fit="T", **extra):
    """A rest-delivered page (the mailbag)."""
    PATH_FIT[id] = fit
    SCENES.append(scene(id, title, owner, min(chapters), "", nodes,
                        requires=tuple(dict.fromkeys(requires)), forbids=tuple(dict.fromkeys((CLOSED, DEAD, *forbids))),
                        delay=delay, last=max(chapters), Relationship=REL, Chapters=list(chapters), Remote=True, Kind=kind,
                        **extra))


# --- Chapter 3 (a memory; Trickster: the Fool King's tablet trip): the lights over the dry fall ------------------------------

page(E + "ch3.chiefs_ground", "Lights over a dry fall", [
    pn("start", '''{n}The stone tablet is the King's now. It sits behind his bar under a cloth that he lifts for anyone who buys a round, and every time he lifts it you think of the place it came from.{/n}
{n}The chiefs' ground lay on the slope below a dead waterfall, at the ragged edge of the Worldwound: grey cairns, cracked grave-stones, the dry lip of a fall that had not run in a hundred years. The dead there did not stay down. You fought your way to the stone through things in old armour that had once been the chiefs of clans, and when it was over you sat on a cairn to get your breath back, and looked up.{/n}''',
       c("Continue", "flash")),
    pn("flash", '''{n}Above the dry fall, at noon, in a sky the colour of ash, a light was moving. Green first, then a thin blade of rose, then a white so clean it hurt: a curtain of colour, rippling, the way the northern lights ripple over Mendev on the coldest nights of the year. Nobody else in your company so much as glanced up.{/n}
{n}And when you tried to look at the cliff beneath it, your eye slid off. Not a trick of the light. A trick of the looking: every time you set your gaze on that stretch of rock, it found something else to be interested in. A crow. A stone. Your own boot.{/n}''',
       c("[Trust your eyes] Look hard at the thing your eyes keep refusing.", "sight", requires=(SIGHT,)),
       c("[Watch the lights instead.]", "lights"),
       c("[Pack the tablet and go.]", "gone")),
    pn("sight", '''{n}Whatever the power in you is, it has taught your eyes to notice what they are being steered away from. They are being steered now. Somebody behind that rock is doing to an entire valley what a good cardsharp does to a table, and doing it beautifully.{/n}
{n}You cannot get through it. You can only admire it, the way one cardsharp admires another across a table: the patience of it, the craft. Whoever is behind the veil has been there a very long time. The lights overhead, you think, must be what it looks like from outside when something holy keeps a secret.{/n}''',
       c("Continue", "lights")),
    pn("lights", '''{n}So you watched the lights. There was no reason to. There was a war, a king to crown, a cart to load. You sat on a dead chieftain's cairn with your sword across your knees for as long as the colours lasted, and when they faded you felt it in your chest like a door closing.{/n}
{n}You never told anyone. It did not seem like the kind of thing a commander tells.{/n}''',
       c("[Leave a bottle of the King's wine at the foot of the dry fall.]", "wine", flags=(LIGHTS_SEEN, WINE_LEFT)),
       c("[Take one last look, and go.]", "end", flags=(LIGHTS_SEEN,))),
    pn("wine", '''{n}It seemed only polite. If someone had watched you rob their neighbours' graves all afternoon, they were owed something for the show. You left the bottle upright in the dust where the water used to fall, with the King's crown scratched into the wax, and did not look back.{/n}
{n}You have wondered since, once or twice, whether anyone drank it.{/n}''',
       c("Continue", "end")),
    pn("gone", '''{n}You packed the tablet in straw, turned the cart for Drezen and did not look up again. Whatever was behind that rock had kept itself to itself for a long time. It could keep itself a while longer.{/n}''',
       c("[Let the memory go.]")),
    pn("end", '''{n}The candle in your room in Drezen gutters. Somewhere below the window the King is singing, the tablet is under its cloth, and the light over the chiefs' ground is, presumably, still moving for no one.{/n}''',
       c("[Sleep.]")),
], requires=("trickster", TABLET), forbids=(E + "ch3.chiefs_ground",), delay=24, chapters=(3,), kind="memory", owner="Memory")


# --- Chapter 4 (a memory; the Abyss): no lights in a red sky ----------------------------------------------------------------

page(E + "ch4.red_sky", "A sky without them", [
    pn("start", '''{n}The Abyss has no night. The sky over the camp goes from red to a darker red and calls that evening, and the sentries call the hours by guesswork.{/n}
{n}You wake from a dream you cannot keep hold of. It had colour in it: green, and rose, and a white like frost on a blade. You lie on your back and look for it overhead, out of habit, and find only the red, the same red it was when you shut your eyes.{/n}''',
       c('"There\'s no sky down here worth the name."', "sky"),
       c("[Go and find the sentry with the brandy.]", "sentry")),
    pn("sky", '''{n}There are no stars in the Abyss. You knew that. You did not know, until tonight, that you had been looking for them every time you woke. It is a strange thing to learn about yourself at the bottom of the world: that you are someone who looks up.{/n}''',
       c("Continue", "end")),
    pn("sentry", '''{n}The sentry has brandy and no conversation, which suits you. You drink with your back to a rock and your face to the red. "Nothing up there, Commander," she says at last, following your eyes. "I've checked." You tell her to check again in an hour, and she does, and there is still nothing.{/n}''',
       c("Continue", "end")),
    pn("end", '''{n}You think of the chiefs' ground, and the light over the dry fall that nobody else looked at. If you never saw it again, you think, you would mind. It is a surprising thing to mind in the middle of a war. You put it away with the other things you would mind, and try to sleep.{/n}''',
       c("[Sleep.]", flags=(ABYSS_DARK,))),
], requires=("trickster", LIGHTS_SEEN), forbids=(E + "ch4.red_sky",), delay=48, chapters=(4,), kind="memory", owner="Memory")


# --- Chapter 5, the shrine after the raid (N-fit build-up, inline on her hub) -----------------------------------------------

shrine(E + "ch5.first_words", "Who was lost", '"Who did you lose?"', [
    el("start", '''{n}Eliandra does not answer at once. She looks past you, down the corridor, to where the wardens are laying sheets over shapes on the floor.{/n}
"Regnard. Taeriell. Vestari and Cristry." {n}She says the names the way one sets down stones, one after another, carefully, so that none of them rolls.{/n} "Regnard took up a sword against them. He had practised alone at night for years, badly, with no one to teach him; he begged Katair for lessons, and Katair always said he was too young." {n}Her hand goes to her heart and stays there.{/n} "He was a hundred and twenty years old, Commander. He was too young."''',
       c('"I\'m sorry. I should have come sooner."', "sooner"),
       c('"Where is Katair?"', "katair"),
       c('"How did they find you, after a hundred years?"', "found")),
    el("sooner", '''"Sooner?" {n}Something that is almost a smile.{/n} "You did not know we existed. Nobody did. That was the whole of our defence, and it was a good one, for a hundred years. You came on the day it failed." {n}She lets her hand fall from her heart.{/n} "I do not know how to ask for more than that. I have never been good at asking, for myself."''',
       c('"Where is Katair?"', "katair"),
       c('"How did they find you?"', "found")),
    el("katair", '''"Beyond the walls." {n}Her composure cracks, a hairline, and closes again.{/n} "Katair goes out alone. He always has. The others think he goes to the Stone Tree, where he was married, and some of them resent it. I have never asked him where he goes. He was outside when the demons came, and he will come back to find this." {n}She looks at the sheets.{/n}
"Taeriell had not spoken to him in seventy years. Now he never will. Katair will count that among his failures, and he will be wrong, and he will not listen to me."''',
       c('"How did they find you?"', "found")),
    el("found", '''"I do not know." {n}She seems to hate the words.{/n} "My Lady hid this place from every unfriendly eye for a century. Then one morning a demon walked in through our door as though it had always stood open. He wanted our research. He wants a Wound of his own." {n}Her mouth tightens.{/n} "We studied the Worldwound for a hundred years so that it could be closed. He came to learn how to make another. I think that is the thing I will not forgive."''',
       c("Continue", "watched", requires=(TABLET,)),
       c("Continue", "end", forbids=(TABLET,))),
    el("watched", '''"There is something else." {n}She studies your face as if checking it against a memory.{/n} "I have seen you before, Commander. Last autumn you came to the chiefs' ground below our fall with a cart, and fought the dead there, and carried a stone away from among the cairns. We watched you from behind my Lady's veil. From inside it, one can see out."''',
       c('"You could have said hello."', "hello"),
       c('[Tell her the truth] "I knew someone was watching. I sat on a cairn and watched your lights instead."', "lights", requires=(LIGHTS_SEEN,)),
       c('"Did anyone drink the wine?"', "wine", requires=(WINE_LEFT,)),
       c('"The stone was for a king. It\'s a long story."', "stone")),
    el("hello", '''"And undone a century's work for the sake of manners?" {n}Her voice is dry.{/n} "Katair wanted to go out and break your cart. I would not let him. You were robbing the dead, Commander, but you were robbing them carefully, and you set the other stones back as you found them."''',
       c("Continue", "end")),
    el("lights", '''{n}Eliandra is very still.{/n} "You saw them," she says. "From outside. Through the veil." {n}She repeats it the way one repeats an unlikely piece of news.{/n}
"My Lady's lights stand over this place at every hour. They are the one part of her gift the veil cannot hide, because they are the veil, seen from the wrong side. In a hundred years I do not think anyone ever sat down on purpose to look at them."''',
       c("Continue", "end", flags=(LIGHTS_TOLD,))),
    el("wine", '''"Odden." {n}The ghost of a smile.{/n} "I forbade anyone to touch it. It might have been poisoned; it might have been bait. Odden went out after moonset and brought it in under his coat, and I pretended not to hear the cork. He has been saving the bottle for an occasion." {n}The smile goes.{/n} "He has one now, I suppose."''',
       c("Continue", "end")),
    el("stone", '''"A king." {n}She does not ask which.{/n} "Sarkoris had no kings, Commander. It had clans, and chiefs, and a great deal of arguing in the meeting-houses. Whoever lies under that cairn would have laughed at you." {n}She lets out a breath.{/n} "But you put the other stones back. I noticed."''',
       c("Continue", "end")),
    el("end", '''"Forgive me. You saved what is left of us, and I stand here reading you a list of the dead." {n}She straightens, the high priestess again, tired to the bone.{/n} "Ask me anything you like, Commander. I will try to answer without weeping."''',
       c("[Leave her to her dead.]", flags=(DEAD_NAMED,))),
], requires=(), forbids=(DEAD_NAMED,))


shrine(E + "ch5.lovers", "My dear rebels", '"Tell me about Vestari and Cristry."', [
    el("start", '''{n}Eliandra lowers herself onto the edge of a bench, carefully, like a woman much older than she looks.{/n}
"My dear rebels." {n}She says it with great tenderness.{/n} "They loved each other for as long as I have known them, and they fought about it for as long as I have known them. Five quarrels and six reconciliations between one moonrise and the next. Stargazers are meant to share what they see. For a month at a time they would not share a word."
"So I forbade it. All of it: love, courtship, every quarrel that comes with them. We were a handful of people shut in a cave for a century. I thought a heart was a thing that could set the whole place alight."''',
       c("Continue", "rooms")),
    el("rooms", '''"They obeyed me. That is the part I cannot put down." {n}Her hands are folded in her lap, very tightly.{/n} "They obeyed me so well that when the demons came, Vestari was in the library and Cristry was in her cell, at opposite ends of the shrine, because that is where I had taught them to be. They died apart. In their hearts they had not been apart for a hundred years, and they died in different rooms, because of me."''',
       c('"Your rule didn\'t kill them. The demons did."', "demons"),
       c('[Tell her the truth] "Your rule kept them apart. You know it, or you wouldn\'t be telling me."', "truth", flags=(LOVERS_TRUTH,)),
       c('"And you? Whom did you forbid yourself?"', "herself")),
    el("demons", '''"Yes. That is what Katair will say when he comes back, and he will say it kindly." {n}She looks up at you.{/n} "It is true, and it is not enough. I made a rule for other people's hearts because I did not trust them. Before I die, I should like to have been wrong about fewer things."''',
       c('"And you? Whom did you forbid yourself?"', "herself")),
    el("truth", '''{n}She flinches, very slightly, and does not deny it.{/n} "No. I would not." {n}A long breath.{/n} "I made the rule for Odden, and Taeriell, and Katair, who had given up their wives and children for the mission; it was not fair that two of us should flaunt what the rest had surrendered. I still think that was a real reason. But I kept those two apart for a century to spare other people's grief, and the price of it was theirs." {n}She looks at her hands.{/n} "I should have found another way. I did not look for one."''',
       c('"And you? Whom did you forbid yourself?"', "herself")),
    el("herself", '''"Myself?" {n}The question seems to startle her more than anything you have said.{/n} "Nobody. There was nothing to forbid. I gave my Lady my whole life when I was thirteen, and she gave me back more strength than any priestess of hers before me. That is the bargain. It is not a rule. It is simply what I am."
"Or what I was. The sanctuary is found, the work of a century is scattered, and our mission is finished. I have not yet worked out what that makes me."''',
       c('"Someone who gets to decide."', "decide", flags=(LOVERS_SPOKEN,)),
       c('[Flirt] "Someone who could stand to be asked a question or two."', "flirt", flags=(LOVERS_SPOKEN, FLIRTED)),
       c('"Tired. Get some sleep, Eliandra."', "sleep", flags=(LOVERS_SPOKEN,))),
    el("decide", '''"Decide." {n}She turns the word over like a stone from a river she used to know.{/n} "I decided things for a hundred people for a hundred years, Commander. Not once for myself. I am not sure I would know how to begin." {n}She stands, and smooths her robe.{/n} "Perhaps I will learn on the road. There will be a great deal of road."''',
       c("[Leave her with it.]")),
    el("flirt", '''{n}Eliandra looks at you. It is a measuring look, the kind a stargazer gives a light she has not charted before, and for once she seems to have no idea what it means.{/n}
"Commander," she says at last, very gently, "there are four of my people under sheets in the next room." {n}A pause.{/n} "Ask me again when there are not."''',
       c("[Let it rest.]")),
    el("sleep", '''"Sleep." {n}She almost laughs.{/n} "I have not slept since the demons came, and I will not until they are buried. But you are kind to say it, and you are the first person today who has told me what to do. It is restful. Do it again some time."''',
       c("[Leave her to her vigil.]")),
], requires=(DEAD_NAMED,), forbids=(LOVERS_SPOKEN,))


shrine(E + "ch5.observe", "The evening reading", '"May I watch your evening observation?"', [
    el("start", '''"Tonight?" {n}She looks at you as though you had asked to watch her pray, which is perhaps what you have done.{/n} "The stargazers are dead or packing. Someone must still take the evening's reading. It has been taken every evening for a hundred years, and I will not let the demons end that too." {n}She considers you.{/n} "Come, then. Say nothing unless I ask, and touch nothing made of brass."''',
       c("[Follow her to the heart of the sanctuary.]", "heart")),
    nar("heart", '''{n}The heart of the sanctuary is a round chamber cut from the living rock, with no roof that you can find. Overhead, where a ceiling should be, there are stars. Not painted stars, not a trick of lamps: the true sky, deep and black and burning, though outside it is the middle of the afternoon and the sky over the Worldwound is the colour of a bruise.{/n}
{n}Instruments stand round the walls under dust-sheets: astrolabes, lenses in brass rings, a great bronze basin brimming with still water in which the stars lie as clearly as they do overhead. Half the charts are already rolled and tied. The rest are pinned out on a long table, weighted at the corners with river stones.{/n}''',
        c("Continue", "reading")),
    el("reading", '''"My Lady's gift," says Eliandra. "Day or night, the stars are always visible here. It is why we could do our work at all. If we leave, the work of a hundred years is lost; that is what we used to say. And now we are leaving." {n}She sets a lens to her eye and does not speak again for some time. Her lips move. Her pen moves. The crusade's best scribes would envy hands so steady.{/n}''',
       c("[Watch her hands.]", "hands"),
       c("[Watch the sky.]", "sky")),
    nar("hands", '''{n}Her hands are long and ink-stained, very still between movements, and they do not shake once, though she has spent the day washing her dead. When she makes an error she does not cross it out. She writes the correction beside it, small and exact, and leaves the error where it is.{/n}
{n}"Nothing is erased," she says without looking up, as if she had felt you wondering. "An observation that was wrong is still an observation. It tells you where the eye goes astray."{/n}''',
        c("Continue", "century")),
    nar("sky", '''{n}The sky moves, very slowly, as a true sky does. After a while you notice that the stars in the basin move with it, a heartbeat behind, as if the water were remembering them rather than reflecting them. Once, at the rim, you think you see a thread of green light cross the water and vanish. When you look up, there is nothing there.{/n}''',
        c("Continue", "century")),
    el("century", '''{n}At last she lowers the lens and sits back, and simply looks up, the way a tired woman looks out of a window.{/n}
"A hundred years," she says. "Every evening. I used to think I would feel it when it ended: a sign, a last star, some word from my Lady. Instead a demon came in through the door for our books." {n}She rolls the night's chart, ties it, and lays it with the others.{/n} "That was my last reading in this room. I am glad someone saw it."''',
       c('"Thank you for letting me."', "rest", flags=(OBSERVED,)),
       c('"It was worth seeing."', "rest", flags=(OBSERVED,)),
       c('[Flirt] "I wasn\'t watching the stars."', "flirted", flags=(OBSERVED, FLIRTED))),
    el("flirted", '''{n}Eliandra turns her head, and the starlight lies along her cheek like frost.{/n}
"No," she says. "I know. I felt it." {n}She does not seem displeased, only puzzled, as if a star she had charted for a century had moved a hair's breadth in the wrong direction.{/n} "Go and sleep, Commander. The guard room is warm. Someone should sleep in this place tonight."''',
       c("[Leave her under her stars.]")),
    el("rest", '''"Go and rest, Commander. The guard room is still warm, and the corruption of the Abyss cannot reach you here." {n}She glances up at the open sky.{/n} "Not tonight, at least. I cannot promise tomorrow."''',
       c("[Leave her under her stars.]")),
], requires=(DEAD_NAMED,), forbids=(OBSERVED,))


shrine(E + "ch5.sarkoris", "Where the road goes", '"Where will you take them, when you go?"', [
    el("start", '''"Somewhere safe. That is what I tell them." {n}Eliandra smooths a fold of her robe that does not need smoothing.{/n} "Drezen, I suppose, since it is yours and it has walls. After that I do not know. There is no Sarkoris to go home to. You have ridden across it. You know what it is now."''',
       c('"Ash, mostly. And the Wound."', "ash"),
       c('"Tell me what it was. I\'ll tell you what\'s left."', "trade")),
    el("ash", '''"Yes." {n}She does not flinch from it.{/n} "When the Wound opened, my Lady sent her priests a vision and an order to run and hide. Many of my brothers and sisters would not. They would not leave their homes, their families, the lake. They died fighting. I obeyed." {n}A pause.{/n} "I have had a hundred years to wonder which of us was braver. I have not decided."''',
       c("Continue", "after")),
    el("trade", '''"A bargain." {n}Something eases in her face.{/n} "Very well. Below Iz there was a lake as wide as a morning, with barges on it painted every colour a Kellid can steal from a dye-merchant. The chiefs went to their rest on those barges, down the river and over our falls. Now: your turn."''',
       c('"The lake is a salt pan. The barges are ribs in the mud."', "truth"),
       c('[Lie kindly] "Some of the barges are still there. You can see the paint."', "lie", flags=(SARKORIS_LIE,))),
    el("truth", '''{n}She closes her eyes.{/n} "Thank you." {n}She means it.{/n} "There were black pines on the ridges, so thick that at noon it was dusk beneath them, and the needles lay a foot deep and smelled of resin when you walked. My turn is done. Yours."''',
       c('"Stumps. Burned black. Some of them still stand."', "stumps")),
    el("stumps", '''"Still stand." {n}She holds on to the two words as if you had handed her something small and valuable.{/n} "Then there is something to begin with. Stumps put out shoots, if they are left alone long enough. So do people."''',
       c("Continue", "after")),
    el("lie", '''{n}Eliandra opens her eyes and looks at you with enormous fondness.{/n} "You lie very kindly, Commander," she says, "and very badly. I will pretend to believe you until I see it for myself. Then I will pretend I never believed you at all, and we will both be comfortable."''',
       c("Continue", "after")),
    el("after", '''"Wherever we go, I would like to be of use to it. Whatever is left of Sarkoris will need healers, and people who remember what it was. I am both. That is not nothing." {n}She almost smiles.{/n} "And someday, perhaps, the waterfalls will sing again. It is the one prayer I have left that is not for the dead."''',
       c("[Leave her to her prayer.]", flags=(SARKORIS_TOLD,))),
], requires=(DEAD_NAMED,), forbids=(SARKORIS_TOLD,))


shrine(E + "ch5.remembrance", "A cup for the dead", '"Odden is pouring wine for the dead. Will you drink with them?"', [
    el("start", '''"Wine." {n}Eliandra's brows rise.{/n} "Stargazers do not drink. A stargazer who sees double is of no use to anyone; Odden himself has said so a thousand times, usually while looking at a bottle." {n}She glances down the hall, to where the old dwarf has set cups on the feasting table he kept laid for a hundred years for guests who never came.{/n} "He wants a day of remembrance. He has wanted one for decades, for the families we left behind. I always told him later."''',
       c('"It\'s later."', "later"),
       c('"Is that my wine he\'s pouring?"', "mine", requires=(WINE_LEFT,))),
    el("mine", '''{n}Her mouth twitches.{/n} "It is. He kept it a year in his boot-chest against an occasion, and he says a demon raid is the only occasion we have had in a century." {n}She looks at you sidelong.{/n} "You should know he has drunk your health every solstice since. He calls you our anonymous benefactor. I have not had the heart to tell him you were robbing a grave at the time."''',
       c("Continue", "later")),
    nar("later", '''{n}The feasting table is a long slab of cave-stone laid with the good plates: chipped, mismatched, and polished to a shine for a century of birthdays nobody came to. Odden stands at its head with the bottle in both hands and his beard braided for the occasion. The survivors come in one by one and find a cup. There are not many of them.{/n}
{n}Odden says the names of the dead. Then he says the names of the living who are not here: wives, sons, and a daughter called Ranhild who would be a hundred and twenty-five this year, if she is anything at all. Then he pours, and his hand shakes, and nobody mentions it.{/n}''',
        c("Continue", "cup")),
    el("cup", '''{n}Eliandra takes a cup. The whole room notices; you see it go through them like wind through grass. She holds it in both hands, the way she holds a lens.{/n}
"To Regnard, who wanted to be a warrior," she says, "and was one, for as long as it took. To Taeriell, who kept his grudge and his watch together. To Vestari and Cristry, who were never apart in the only way that mattered." {n}She drinks. It is clearly the first wine she has tasted in a very long time, and she does not quite cough.{/n}''',
       c("[Drink with them.]", "after"),
       c('[Raise your cup to her] "And to the one who kept the rest of them alive."', "toast", flags=(TOASTED,))),
    nar("toast", '''{n}There is a small silence. Then Odden bangs his cup on the table and roars her name, and the rest take it up, raggedly, and drink.{/n}
{n}Eliandra stands among them with her cup and no idea at all what to do with her face. In the end she lays her hand on her heart, as she does, and bows to her own people, and when she straightens her eyes are wet and she is, astonishingly, laughing.{/n}''',
        c("Continue", "after")),
    el("after", '''{n}Later, when the cups are empty and Odden is asleep with his head on his arms, she comes to stand beside you.{/n}
"Thank you," she says. "I would not have let them do this if you had not been here. I would have said later, again." {n}She looks down at her empty cup.{/n} "I think I have said later to a great many things."''',
       c("[Set your cup down beside hers.]", flags=(REMEMBRANCE,))),
], requires=(DEAD_NAMED,), forbids=(REMEMBRANCE,))


shrine(E + "ch5.healer", "The strongest of her servants", '"You should rest. You\'ve been healing since the fighting stopped."', [
    nar("start", '''{n}Eliandra is kneeling beside a warden with a belly wound that would have killed him within the hour in any camp you know. She has one hand flat on the wound and the other on his forehead, and she is speaking very low, in a Kellid dialect you do not know.{/n}
{n}Light comes out of her. Not the hot gold of a paladin's hands: something cooler, greener, a shimmer that moves over the man the way light moves on water. The wound closes under her palm. The warden sleeps. She moves to the next.{/n}''',
        c("Continue", "talk")),
    el("talk", '''"Rest," she says, not looking up. "When they are all asleep." {n}A burned stargazer; a girl with a broken arm who is, from the look of her, not a stargazer at all but a scullion; a warden with no wound anyone can see who will not stop shaking. Eliandra takes each of them the same way, one hand on the hurt and one on the head, and the light takes each of them.{/n}
"My Lady has always been generous with me," she says between the scullion and the warden. "I have never understood why. There are better women. There are certainly kinder ones."''',
       c('"They say you\'re the strongest of her priestesses."', "strongest"),
       c('"Maybe she likes you."', "likes")),
    el("strongest", '''"They say it." {n}She does not deny it.{/n} "I never married. I never had a family. I gave her everything a woman can give, when I was thirteen and did not know what everything was. She answered with this." {n}She lifts her hand from the warden's head, and the green light lifts with it, and goes out.{/n} "I have always believed that is how she works: what is given up for her, she answers. Perhaps that is only what a girl of thirteen needed to believe."''',
       c("Continue", "end")),
    el("likes", '''{n}Eliandra laughs, surprised into it, and the light under her hand flares and steadies.{/n} "Perhaps. Katair says she likes stubbornness." {n}She moves to the next pallet.{/n} "I gave her my whole life at thirteen, before I knew what that meant, and I never asked for any of it back. She answers what is given up for her. That is how I have always understood her."''',
       c("Continue", "end")),
    nar("end", '''{n}When the last of them is asleep she sits back on her heels. She is grey with exhaustion, and yet you have the impression that she could do it all again if she were asked, and again after that. The strength is simply there, the way a spring is there under a rock.{/n}
{n}"There," she says. "Now I will rest."{/n}''',
        c("[Help her to her feet.]", flags=(HEALING_SEEN,)),
        c("[Let her rise on her own.]", flags=(HEALING_SEEN,))),
], requires=(DEAD_NAMED,), forbids=(HEALING_SEEN,))


shrine(E + "ch5.regnard", "Regnard's swords", '"Regnard\'s cell is full of swords."', [
    el("start", '''"Chiefs' swords." {n}Eliandra does not need to ask which cell you mean.{/n} "Regnard collected the history of Sarkoris. He said we all needed a way to escape the monotony of this place, or we would lose our minds, and his was the dead. The cultists of the Lord of Ghouls woke the chiefs we had sent to their rest below our falls, and the guards cut them down, and Regnard, who was never let outside the walls, begged the guards for whatever the chiefs had been buried with."
{n}She is quiet.{/n} "He had a whole wall of them. He never used one. He practised at night with a plain sword of his own, badly, where he thought no one could see. Until yesterday."''',
       c('"He wanted to fight?"', "fight"),
       c('"What will you do with them?"', "swords")),
    el("fight", '''"He wanted to change." {n}She says it as though the words had been waiting a long time.{/n} "He told me so once, in the ninetieth year. We don't get old, he said. We don't get sick. And we don't change. The same conversations, the same jokes, the same food, the same arguments. A guard cannot become a stargazer and a stargazer cannot become a guard. He said everything here had to stay as it was on the first day, and it was killing him slowly, and could I please let him out to fight."
"I told him his talent was needed here." {n}Her hand goes to her heart.{/n} "It was true. It was also the answer I gave everyone, to everything, for a hundred years."''',
       c('"He got his fight in the end."', "end_fight"),
       c('"You kept him alive for a century. That counts."', "end_alive")),
    el("end_fight", '''"He did. With his own sword, the plain one, not any of the chiefs'. He would not have thought himself worthy of a chief's." {n}She closes her eyes.{/n} "The wardens found him at the library door. Vestari was on the other side of it. I think he was trying to reach him."''',
       c("Continue", "swords")),
    el("end_alive", '''"Alive." {n}She weighs it.{/n} "Yes. I kept all of them alive, and kept them exactly as they were, and called that the same thing as keeping them well. Regnard knew better. He told me so. I did not listen." {n}A breath.{/n} "I am listening now. It is a poor time to begin."''',
       c("Continue", "swords")),
    el("swords", '''"The swords will go back. Every one of them, to the chiefs' ground below our fall, laid on the cairns they came from, if Odden can remember which. Regnard kept a record. Of course he did." {n}Almost a smile.{/n} "It will take a day we do not have. We will take it anyway."''',
       c('"I\'ll lend you hands. The crusade can spare a day."', "hands"),
       c('"Keep one. For him."', "keep")),
    el("hands", '''"Thank you." {n}She inclines her head, the full formal bow of the high priestess, and then, a little awkwardly, simply touches your arm.{/n} "Tell your soldiers to lay them with the blades pointing north, towards the lights. It is the old way. Regnard would have written down every one they got wrong, and been very happy."''',
       c("[Leave her with his wall of swords.]", flags=(E + "regnard_swords", E + "regnard_swords_home"))),
    el("keep", '''{n}She is quiet a long while.{/n} "One," she says at last. "The plain one. The one he died with. I will carry it into Sarkoris and put it on the first wall we build, and tell every child who asks that the man who owned it wanted to change so badly that he practised with it every night for years, alone, with nobody to teach him, and then used it." {n}She looks at you.{/n} "That is a better thing to tell children than that he obeyed me."''',
       c("[Leave her with his wall of swords.]", flags=(E + "regnard_swords", E + "regnard_sword_kept"))),
], requires=(DEAD_NAMED,), forbids=(E + "regnard_swords",))


shrine(E + "ch5.veil", "Seen from inside", '"How did your Lady hide this place? What does the veil actually do?"', [
    el("start", '''"It turns the eye aside." {n}Eliandra lifts one hand and makes a small gesture, as though brushing a curtain.{/n} "Not a wall. Not an illusion of rock where there is none. The rock is really there, and so is the door, and so are we. The veil only persuades whoever looks that there is something more interesting a little to one side. A crow. A stone. Their own feet."
"Katair calls it the only lie my Lady has ever told. He means it as praise."''',
       c('"And from inside?"', "inside"),
       c('"It sounds like good stagecraft."', "stage")),
    el("stage", '''"Stagecraft." {n}She considers the word, turns it over, and seems to decide she likes it.{/n} "Yes. My Lady is the mistress of the lights of the north, Commander. She has been making people look up at the right moment since before there was a Sarkoris. It is the same art, turned the other way: making them look elsewhere."''',
       c('"And from inside?"', "inside")),
    el("inside", '''"From inside, one sees out perfectly well. That was the cruelty of it." {n}Her voice does not change, but her hands fold together.{/n} "We watched the clans die. Not all of it; the veil covers only the valley. But enough. Odden watched a band of refugees go past the dry fall, a day's walk from where his daughter should have been, and could not call out, because a call would have undone the veil. Taeriell charted every time Katair left the walls. We saw everything, and were seen by nothing, for a hundred years."''',
       c('"Could anyone see through it?"', "through"),
       c('"That sounds like a prison."', "prison")),
    el("prison", '''"It was a vow." {n}Gently corrected.{/n} "Which is a prison one chooses, and must go on choosing, every morning. That is the difference. It is not always a large one."''',
       c('"Could anyone see through it?"', "through")),
    el("through", '''"No one ever did, that I know of. Some saw the lights above it: the veil cannot hide those, because the lights are the veil, seen from the wrong side. Travellers sometimes stopped to look up, and then felt foolish, and went on." {n}She looks at you with frank curiosity.{/n} "It must be strange, for someone like you. You live by making people look at the wrong thing. What would you do, if a god turned the trick on you?"''',
       c('"Admire it. Then look for the seam."', "seam", flags=(E + "veil_known",)),
       c('"Pray I never find out."', "pray", flags=(E + "veil_known",))),
    el("seam", '''{n}Eliandra laughs, a small real laugh.{/n} "There is no seam. I have looked for a hundred years, from both sides, to make sure no one else could find one. But I believe you would look. I think you would look for the rest of your life." {n}The laugh fades into something more thoughtful.{/n} "My Lady takes only what is freely given, Commander. If she ever turns it on you, it will be because you asked her to."''',
       c("[Let that settle.]")),
    el("pray", '''"Pray to whom?" {n}Gently amused.{/n} "No. I do not think you are the praying sort. But you need not fear it. My Lady takes only what is freely given. If she ever turned her veil on you, it would be because you had asked her to, and I cannot imagine why anyone would."''',
       c("[Let that settle.]")),
], requires=(DEAD_NAMED,), forbids=(E + "veil_known",))


shrine(E + "ch5.thirteen", "What she gave at thirteen", '"How old were you, when you made your vow?"', [
    el("start", '''"Thirteen." {n}Eliandra answers at once, as though she has been asked it before, and then pauses, as though she has not.{/n} "I found my gift that year. A boy from the next clan fell through the lake ice in the spring thaw, and they pulled him out blue, and I put my hands on him because nobody else was doing anything, and he coughed up the lake and sat up and asked for his mother."
"By the autumn every clan on the lake knew. By the winter I was in the temple of Pulura at Iz, with my hair cut short, making my vow."''',
       c('"What did you vow?"', "vow"),
       c('"And the boy?"', "boy")),
    el("boy", '''{n}The ghost of a smile.{/n} "He married a girl from his own clan and had eleven children and was, I am told, a very bad fisherman. I blessed three of the children. He never once thanked me, and he always sent the first catch of the year to the temple, and they were always very small fish."
{n}She is quiet.{/n} "That is not the story you were asking for. I know. I like it better."''',
       c('"What did you vow?"', "vow")),
    el("vow", '''"Everything." {n}She says it simply.{/n} "That is the Sarkorian way, with my Lady. Some priests give her their voice, some their sleep, some a season of every year. I gave her all of it: no marriage, no family, no house of my own, no child, no one I would put before her service. I did not know what I was giving. How could I? I was thirteen. I knew only that the gift was there, and that I wanted to be worthy of it."
"And she answered. She has answered every day since. The strongest of her servants, they say."''',
       c('"Do you ever think about what you gave up?"', "gave"),
       c('"Would you make the same vow again?"', "again")),
    el("gave", '''"Not often. It is not a thing one misses, if one never had it." {n}A pause.{/n} "That is what I used to say. I said it to Vestari and Cristry, the night I forbade them. I told them it was possible to live without it, because I had." {n}Her hands are very still in her lap.{/n} "I think now that I was a woman who had given her own heart away before she knew what it was, telling two people who had kept theirs what hearts were for. I think they knew it. I think that is why they laughed, afterwards, when they thought I could not hear."''',
       c("Continue", "believe")),
    el("again", '''"Yes." {n}No hesitation.{/n} "Knowing what it would cost, yes. The shrine needed a priestess who would not leave it, and I was that, and a hundred people are alive because of it." {n}Then, more slowly:{/n} "But I would like to have been asked. Nobody asked me whether I was sure. They were so glad I was willing."''',
       c("Continue", "believe")),
    el("believe", '''"My Lady answers what is given up for her. I have believed that my whole life. If I took back what I gave, I would be taking back the sacrifice, and the answer would go with it. My strength. The thing my people need most on the road." {n}She looks at her hand.{/n} "So it is not mine to take back. Only she could release me. And I have never asked her for anything, and never will."''',
       c('"Never is a long time."', "never", flags=(E + "vow_told",)),
       c("[Say nothing. File it away.]", "filed", flags=(E + "vow_told",))),
    el("never", '''"It is exactly as long as I have been alive." {n}Dry as dust.{/n} "I know how long never is, Commander. I have been doing it for a century." {n}Then, unexpectedly, she looks up at you, and something in her face is not dry at all.{/n} "Why? Do you know a shorter road?"''',
       c("[Let the question hang.]")),
    nar("filed", '''{n}You say nothing. Eliandra watches you not saying it, and seems to understand that something is being put away for later, carefully, the way she rolls a chart.{/n}
{n}"You have a way of listening," she says at last, "as if you were counting. I have not decided whether I like it."{/n}''',
        c("[Leave her to decide.]")),
], requires=(DEAD_NAMED,), forbids=(E + "vow_told",))


shrine(E + "ch5.packing", "A hundred years in crates", '"Can I help with the packing?"', [
    nar("start", '''{n}The library of Pulura's Fall is going into crates. Stargazers who survived the raid move among the shelves with armfuls of scrolls, and a warden with a hammer nails each crate shut with a sound like a door slamming, over and over. Eliandra stands in the middle of it with a ledger, saying where each thing goes, and none of them needs to be told twice.{/n}''',
        c("Continue", "her")),
    el("her", '''"Help?" {n}She looks at your hands as if assessing them for fine work.{/n} "Can you lift a chart case without bending the corners? Can you tell the difference between a lens and a paperweight? Odden cannot, and he has been here a hundred years." {n}She hands you a stack of scroll cases.{/n} "The blue cords are observations. The red are calculations. The black are the ones I would save first, if the roof came down."''',
       c("[Pack them carefully, blue with blue.]", "careful"),
       c("[Pack them fast, and let her correct you.]", "fast")),
    nar("careful", '''{n}You pack them carefully, blue with blue, red with red, the black on top where they can be found. When you look up she is watching you, not the crate, with her ledger forgotten against her chest.{/n}
{n}"You have done this before," she says. "Packed a life into boxes and left." It is not quite a question.{/n}''',
        c('"A few times. You learn what to leave behind."', "leave"),
        c('"Never a life this long."', "long")),
    nar("fast", '''{n}You pack them fast. She corrects you three times without looking, by some sense of hearing that tells her a red cord has gone in with the blue, and the fourth time she comes over and does it herself, her hands brushing yours in the straw, and stays there a breath longer than the correction needs.{/n}
{n}"You are very bad at this," she says, and does not move away.{/n}''',
        c('"I\'m better at unpacking."', "unpack"),
        c('"I\'ll learn. I\'ve got a good teacher."', "teacher")),
    el("leave", '''"What to leave behind." {n}She looks around the half-empty library.{/n} "Everything in this room was written by someone who is alive, or was yesterday. I cannot leave any of it. I do not know how." {n}She marks the crate in her ledger.{/n} "Teach me, one day. Not today. Today I am carrying everything."''',
       c("Continue", "end")),
    el("long", '''"No. Few people have." {n}She lays her hand on the lid of the crate.{/n} "A hundred years, in how many boxes? Forty-one. I counted last night, when I could not sleep. That is not very many, for a century. I thought there would be more."''',
       c("Continue", "end")),
    el("unpack", '''{n}The colour comes up in her face so quickly that she seems startled by it herself.{/n} "Commander," {n}she says, in the voice she presumably keeps for stargazers who whisper during the evening reading,{/n} "this is a library." {n}But she is not looking at the scroll cases when she says it, and she does not correct the next crate either.{/n}''',
       c("Continue", "end")),
    el("teacher", '''"Flattery." {n}She sounds pleased and faintly suspicious, as if she has been handed a coin she cannot quite place.{/n} "I have not been flattered in a hundred years. Nobody here would dare. Katair would think it a sign of fever." {n}She moves your hand, and a red cord, into the right place.{/n} "Do it again later. I want to see whether I like it the second time."''',
       c("Continue", "end")),
    nar("end", '''{n}By evening the library is bare to the shelves. The warden with the hammer has gone to find more nails. Eliandra writes the last line in her ledger, closes it, and stands looking at the empty room, the ledger held against her chest like a shield.{/n}
{n}"Thank you," she says, without turning round. "I would have done it alone, and it would have been worse."{/n}''',
        c("[Leave her in the empty library.]", flags=(E + "packed",))),
], requires=(DEAD_NAMED, SHRINE_LEFT), forbids=(E + "packed",))


shrine(E + "ch5.burial", "Below the dry fall", '"Where will you bury them?"', [
    el("start", '''"Below the fall, on the chiefs' ground. There is nowhere else." {n}Eliandra is already in a plain grey robe, her sleeves tied back.{/n} "It is where Sarkorians have always sent their dead, from this valley: on barges, once, down the river and over the water. There is no river now, and no water, and no barges. There is still the ground." {n}She looks at you.{/n} "You know the place. Will you come?"''',
       c("[Go down to the chiefs' ground with the stargazers.]", "ground")),
    nar("ground", '''{n}They carry the dead out through the hidden door on boards, in the grey of the afternoon: four shapes under sheets, and a handful of stargazers and wardens to carry them. Outside the veil the air is thin and cold and smells of the Wound. The cairns of the chiefs stand crooked on the slope below the dry fall, where they have stood for a century, some broken, some re-set by careful hands.{/n}
{n}The survivors dig. Nobody has dug a grave in Pulura's Fall in a hundred years; the dead were rare, and went into the rock. They do it badly, and slowly, and Eliandra digs with them, in her grey robe, until her hands bleed.{/n}''',
        c("Continue", "place", requires=(TABLET, LIGHTS_SEEN)),
        c("Continue", "place_plain", requires=(TABLET,), forbids=(LIGHTS_SEEN,)),
        c("Continue", "lovers", forbids=(TABLET,))),
    nar("place", '''{n}You know this slope. You fought across it for a king's stone, and sat on that cairn, there, with your sword across your knees, looking up. There is a gap in the line of stones where the tablet stood. The stargazers dig beside it without comment. One of the wardens glances at you, and then very carefully at nothing.{/n}''',
        c("Continue", "lovers")),
    nar("place_plain", '''{n}You know this slope. You fought across it for a king's stone. There is a gap in the line of stones where the tablet stood. The stargazers dig beside it without comment. One of the wardens glances at you, and then very carefully at nothing.{/n}''',
        c("Continue", "lovers")),
    el("lovers", '''{n}When the graves are dug she stands at the head of the second one, which is wider than the others.{/n}
"Vestari and Cristry together," she says. "It is the first thing I have allowed them in a century, and it is too late, and I am doing it anyway." {n}Her voice is perfectly steady. Her bloodied hands are not.{/n} "Regnard beside them, because he died trying to reach them. Taeriell at the end of the row, facing the Stone Tree, because that is where he spent seventy years looking."''',
       c('"Do you want me to say something?"', "say"),
       c("[Take up a spade and fill in the graves with them.]", "spade")),
    el("say", '''"No." {n}Gently.{/n} "Thank you. They did not know you. It would be a stranger's words over them, and they had too few strangers in their lives to waste one now." {n}She looks at the four graves.{/n} "But stand here with me while I say mine. I have said the words over a great many Sarkorians. I have never said them over my own."''',
       c("Continue", "words")),
    nar("spade", '''{n}You take up a spade. Nobody stops you. The earth of the chiefs' ground is dry and full of stones, and the work is heavy and quiet, and after a while one of the wardens begins to hum something under his breath, a slow Kellid tune, and the others take it up one by one, until the whole slope is humming. Eliandra does not hum. She works beside you, and when you straighten to ease your back, she has stopped to watch you, and does not pretend otherwise.{/n}''',
        c("Continue", "words")),
    el("words", '''{n}She stands at the head of the row with her hands at her sides and speaks the old words, in Kellid first and then, for your sake, in the common tongue.{/n}
"You were given to the water, and there is no water. You were given to the lights, and the lights are here. Go north, where they hang. We will look up, and know where you are." {n}She stops. Then, not in the old words at all:{/n} "I am sorry. I was wrong. You were right, all four of you, and I would give a great deal for you to have lived to tell me so."''',
       c("[Stand with her until the last stone is set.]", flags=(E + "buried",))),
], requires=(DEAD_NAMED,), forbids=(E + "buried",))


RESEARCH_BURN = E + "research.burn"
RESEARCH_KEEP = E + "research.keep"

shrine(E + "ch5.research", "What the demon wanted", '"Tell me what he wanted from your research. Exactly."', [
    el("start", '''"Exactly." {n}Eliandra seems to approve of the word.{/n} "A hundred years of the Worldwound, observed from inside its borders. How it breathes. How it grows and shrinks with the seasons of the Abyss. Where the veil between the worlds is thinnest, and when. We wrote it all down so that someone, one day, would know how to close it."
{n}Her mouth thins.{/n} "Anyone who knows how a door is closed knows how it is opened. We knew that. We thought no one would ever find us to read it."''',
       c('"If he got away with any of it, what do you want done with it?"', "ask")),
    el("ask", '''"Burned." {n}She says it without hesitation, and then, being who she is, checks the answer.{/n} "No. That is the frightened answer. The work is our life, and it was meant for closing the Wound, and whatever is left of it should go to whoever is closing it. That is you." {n}She looks at you steadily.{/n} "But if the demon has it, or has copied it, then burn his. Every page. I would rather lose a century of work than see it open another Wound in the world."''',
       c('"Then I\'ll burn whatever I find in his hands. On my word."', "burn", flags=(RESEARCH_BURN,)),
       c('"I\'ll decide when I see it. If it can win the war, I\'ll use it."', "keep", flags=(RESEARCH_KEEP,))),
    el("burn", '''"Thank you." {n}She lets out a breath.{/n} "You say on your word the way other people say it on their honour. I have noticed that about you. You do not swear by things you do not have." {n}A pause.{/n} "It is a small thing to ask, and I do not like to ask for things. But I am glad I asked this one."''',
       c("[Leave it there.]")),
    el("keep", '''{n}She is quiet for a while. Then she inclines her head, the careful bow she gives to a portent she dislikes but cannot argue with.{/n}
"That is an honest answer," she says. "It is the answer Areelu would have given, if anyone had asked her, before Threshold. It is also the answer of every general who ever won a war." {n}She looks at you with something that is not quite disapproval.{/n} "Decide carefully, Commander. You are the only one of them I have met who seems to know the difference."''',
       c("[Leave it there.]")),
], requires=(DEAD_NAMED,), forbids=(RESEARCH_BURN, RESEARCH_KEEP))


shrine(E + "ch5.maiden", "The Shimmering Maiden", '"Tell me about your Lady. Not the prayers. Her."', [
    el("start", '''"Her." {n}Eliandra seems to find the request unexpectedly pleasant, like a stargazer asked about the stars rather than the calendar.{/n} "She is the Shimmering Maiden, the mistress of the Aurora Iobara, the lights that hang over the far north in winter. The Sarkorians loved her because the north was always the direction of home. Sailors and caravan-masters prayed to her for a clear sky and a true star to steer by. The clans prayed to her for the long nights to end."
"She is one of the empyreal lords: not a great goddess, not a small one. She keeps company with Desna, as the northern lights keep company with the stars. She is vain, a little. She likes to be looked at."''',
       c('"Vain? That\'s a strange thing for a high priestess to say."', "vain"),
       c('"What does she want from the people who pray to her?"', "want")),
    el("vain", '''"It is a true thing, and she has never minded the truth." {n}The ghost of a smile.{/n} "Why else put her lights in the sky at all, where everyone can see them? She could have been a goddess of hidden things; she has the gift for it, as you can see from this shrine. Instead she hangs herself over the whole north every winter and waits for people to stop in the road and look up. That is vanity, Commander. It is the kindest kind."''',
       c('"What does she want from the people who pray to her?"', "want")),
    el("want", '''"Attention. Honesty. That you look up." {n}She considers.{/n} "And that what you give her is really given. She has no patience with bargains made with one eye on the way out. My brothers used to say she could see a cheat coming from the far side of the Lake of Mists and Veils, and they said it with great respect."
"She is generous to those who give. She has been generous to me. I have never understood the whole of why."''',
       c('"Maybe she likes being looked at by you."', "looked"),
       c('"Does she ever speak to you?"', "speak")),
    el("looked", '''{n}Eliandra laughs, a real laugh, startled.{/n} "Perhaps. I have looked at her every evening for a hundred years. That must count for something, even with a goddess." {n}She sobers.{/n} "She shows me things, sometimes, in the water or in dreams. She has never once spoken. I think she thinks words are for people who cannot make lights."''',
       c("[Leave her with her Lady.]", flags=(E + "maiden_told",))),
    el("speak", '''"Never in words. In visions, sometimes, in the water or in dreams. That is how she told us to hide, when the Wound opened, and that is how she told me what the work would cost." {n}She is quiet.{/n} "A century, and many sacrifices. I said I was willing. I did not ask how many. I think she liked that about me, and I am no longer sure she should have."''',
       c("[Leave her with her Lady.]", flags=(E + "maiden_told",))),
], requires=(DEAD_NAMED,), forbids=(E + "maiden_told",))


PLANNED = E + "planned"


# --- The device: the terms, the last rite, her own offering (T) ----------------------------------------------------------

shrine(E + "ch5.terms", "What the Maiden takes", '"What does your Lady take, in return for what she gives?"', [
    el("start", '''{n}Eliandra considers you. It is the look a priestess keeps for questions that are not quite the question being asked.{/n}
"That depends on who is asking, and why," she says. "My Lady is not a merchant. But she is no fool either, and she has never given anything for nothing. What is it you want to know, Commander?"''',
       c('[Lore (Religion)] "How is an offering made to Pulura? Properly. The Sarkorian way."',
         check=dict(Skill="SkillLoreReligion", DC=20, Success="taught", Failure="guessed")),
       c('"Only curious. Forget I asked."', abort=True)),
    el("taught", '''"Properly." {n}She seems pleased by the word.{/n} "Then I will tell you as I was taught it, in the temple where I made my vow. Half the pilgrims who came to us got it wrong, and my Lady forgave them, and gave them nothing.
"An offering to the Shimmering Maiden is made under the open stars, never under a roof. It is named aloud, once, so there can be no mistaking what is given. It must be something the giver loves; she has no use for what you would throw away. And it must belong to her own domain: light, the night sky, the far north where her lights hang. Or the sight of them."''',
       c("Continue", "taught2")),
    el("taught2", '''"Gold is not hers. Deeds are not hers; deeds belong to whoever needed them done. My brothers used to leave her silver, and she let it tarnish on the altar." {n}Her eyes narrow, very slightly.{/n} "Why do you want to know? You are not a Sarkorian, and I do not think you are a pious {mf|man|woman}."''',
       c('"I like to know the rules before I play."', "rules"),
       c('"Because I\'ve seen her lights. From outside."', "seen", requires=(LIGHTS_SEEN,)),
       c('"Because you won\'t ask her for anything. Someone should."', "someone")),
    el("rules", '''"A game." {n}She says it without heat.{/n} "Everyone who comes to my Lady thinks it is a game, at first. It is not. But the rules are the same either way: she takes only what is truly given, and what she takes, she keeps."''',
       c("Continue", "warn", flags=(TERMS_READ, STARTED))),
    el("seen", '''{n}She is quiet for a breath.{/n} "Then you already know what she values," she says. "Most people have to be told. Most people, told, still bring silver."''',
       c("Continue", "warn", flags=(TERMS_READ, STARTED))),
    el("someone", '''{n}Eliandra goes still.{/n} "I have never asked my Lady for anything," she says. "Not in a hundred years. Not when my brothers died at the lake, not when Regnard took up his sword. I will not begin now by haggling with her."
"But you are right that nobody else will. I had not thought of that as a thing that could be true."''',
       c("Continue", "warn", flags=(TERMS_READ, STARTED))),
    el("guessed", '''"Properly." {n}She begins to explain: something about the open sky, and naming a thing aloud. You nod along. You are thinking about the crusade's treasury, and what the Maiden's temples would look like rebuilt in marble, and how much of that the Council could be talked into paying for.{/n}
"...and so," she finishes, "she has no use for what you would throw away. Do you understand?"''',
       c('"Perfectly. Gold, and good works, and plenty of both."', "wrong", flags=(TERMS_GUESSED, STARTED))),
    el("wrong", '''{n}Eliandra looks at you with an expression you cannot read. Then she inclines her head, very slightly, as one does to a child who has recited a lesson with great confidence and every word in the wrong order.{/n}
"Perhaps," she says. "My Lady has surprised me before."''',
       c("Continue", "warn")),
    el("warn", '''"If you mean to try her, Commander, try her honestly. She has turned aside the eyes of demons for a century. She will see a cheat coming a very long way off."''',
       c("[Leave it there.]"),
       c("[That night, work out on paper what you could give, and what it would cost.]", "list")),
    nar("list", '''{n}That night you sit down with a lamp, a sheet of paper and a pencil, and write down what you have. It is not a long list. Everything you own of any value is either the crusade's, or borrowed, or already promised to somebody.{/n}''',
       c("Continue", "rules_read", requires=(TERMS_READ,)),
       c("Continue", "rules_guessed", forbids=(TERMS_READ,))),
    nar("rules_read", '''{n}Under it you write her rules, the way she told them to you. Under the open stars. Named aloud, once. Something the giver loves. Of the Maiden's own domain: light, the night sky, the far north, the sight of her lights.{/n}
{n}Then you cross things off. Gold: not hers, and not yours either, strictly. The crusade's luck, such as it is: not hers. Your name, your voice, a year of your life: yours, but not of her domain, and you suspect a goddess of the northern lights has no use for a Trickster's voice. You sit and look at what is left for some time.{/n}''',
       c("Continue", "left")),
    nar("rules_guessed", '''{n}Under it you write what you remember of her rules, which is not much: something about the open sky, and naming a thing aloud, and gold. Gold, certainly; gold always works. You write down the crusade's treasury and underline it twice.{/n}
{n}And then you go back over the conversation in your head and find a line you had skated over: she has no use for what you would throw away. You look at the treasury. You would throw it at almost anything. You leave the underline, but you add a question mark.{/n}''',
       c("Continue", "left")),
    nar("left", '''{n}What is left is a memory, and you did not expect it to be on the list at all.{/n}''',
       c("Continue", "cairn", requires=(LIGHTS_SEEN,)),
       c("[Remember a night you saw them, somewhere in the north.]", "mendev", forbids=(LIGHTS_SEEN,)),
       c("[You have never really looked at them. Admit it.]", "never", forbids=(LIGHTS_SEEN,))),
    nar("never", '''{n}You have never really looked. You know what they are, the way everyone in the north knows; you have never stopped for them. That is the trouble with the list: the one thing on it that is hers is something you have not yet learned to love.{/n}
{n}Tomorrow night, at the basin, she will call them into the water. You will look at them then, properly, for as long as it takes, and you will see whether what you feel is enough. It is a gamble. You write it down as one.{/n}''',
        c("Continue", "decide")),
    nar("cairn", '''{n}A dead chieftain's cairn below a dry fall. A sword across your knees. Green, then rose, then a white like frost on a blade, moving over a cliff your eyes would not stay on. You never told anyone.{/n}
{n}It is the only thing you own that is truly yours and truly hers at the same time. That is not an accident, you think. That is what she meant by the rules.{/n}''',
       c("Continue", "decide")),
    nar("mendev", '''{n}You have seen them: some cold night, from some wall or some road, a sky that moved, green and rose and white, and you stopped, as everyone stops, until your feet were numb. You have not thought about it in a long time. It surprises you how clearly you remember it.{/n}
{n}It is the only thing you own that is truly yours and truly hers at the same time. That is not an accident, you think. That is what she meant.{/n}''',
       c("Continue", "decide")),
    nar("decide", '''{n}A careful planner does not make an offering without knowing the price. You write it out plainly, the way you would write the cost of an assault: never to see them again. Not once. Not over Sarkoris in winter, not over whatever is left of the world when the war is done. You read it three times.{/n}
{n}Then you look at it the way a buyer looks at a contract. A goddess who turns eyes aside can take a sight without breaking anything: she need only turn one more pair of eyes. It costs her nothing to collect, and it costs you everything to pay, and that is exactly the kind of price a power accepts. You would ask it yourself, in her place.{/n}
{n}You fold the paper and hold it over the lamp until it catches, because some plans should not exist in writing, and go to bed.{/n}''',
       c("[Sleep on it.]", flags=(PLANNED,))),
], requires=(), forbids=(TERMS_READ, TERMS_GUESSED), fit="T")


NAME_IT = '"My sight of her lights. I give it up, for good, in Eliandra\'s place."'

shrine(E + "ch5.last_rite", "The last rite", '"Will you hold one last rite at the star-heart? For yourself, this time."', [
    el("start", '''"For myself." {n}Eliandra repeats it slowly, as if the words belonged to a language she had studied and never spoken.{/n} "What would I ask her for, Commander? My shrine is broken. My people are packing. I am alive, and I have work to do."''',
       c('"Your leave. From the vow. So there can be a life for you after it."', "leave"),
       c('[Flirt] "Your leave. So I can stop pretending I come here for the view."', "leave")),
    el("leave", '''{n}She does not answer for a while. Somewhere nearby someone is nailing a stargazers' crate shut, and every blow is very loud.{/n}
"You have understood more than I told you," she says at last. "Yes. There is a vow. I made it at thirteen, and my Lady answered it, and the answer is this." {n}She turns her hand palm up, and a faint green shimmer crosses it and goes.{/n}
"To take for myself what I gave up for her would be to take my sacrifice back, and my people will need that strength on the road. Only she can release me. And I have never asked her for anything, Commander. I will not begin by haggling."''',
       c('"Then don\'t haggle. Let me make the offering. In your place."', "place"),
       c('"Forget I asked."', abort=True)),
    el("place", '''{n}Eliandra looks at you as she looked at the stars in the basin: as if you had moved, very slightly, in a direction she had not predicted.{/n}
"In my place," she says. "You would give her something of yours, so that she releases me from what is mine." {n}She is quiet.{/n} "I gave my Lady a century and never once asked what it cost me. You asked. I think that is why I am letting you pay."
"Come to the star-heart at nightfall. I will hold the rite, and you will make the offering, aloud, under the open stars." {n}Her voice hardens, very slightly, into the voice that once forbade a whole shrine to love.{/n} "And, Commander: if you have come to cheat her, go now."''',
       c("[Go to the star-heart at nightfall.]", "heart_known", requires=(OBSERVED,)),
       c("[Go to the star-heart at nightfall.]", "heart_new", forbids=(OBSERVED,))),
    nar("heart_new", '''{n}The heart of the sanctuary has no roof. Where a roof should be there is sky: the true sky, black and burning, its stars sharper than any you have seen since Mendev, though the hour is barely past sunset outside. The instruments round the walls are crated, and a few last charts lie half rolled on a long table. A great bronze basin remains, brimming with still water, and in it the stars lie as clearly as they lie overhead.{/n}
{n}Eliandra kneels at the basin in her white robes with her hair unbound. She does not look up when you come in.{/n}''',
        c("Continue", "rite")),
    nar("heart_known", '''{n}The star-heart is emptier than the evening you watched her take her reading. The lenses are crated and most of the charts rolled and gone; only her last few lie half rolled on the long table, weighted with river stones. Only the basin remains, brimming, and the sky overhead, black and burning, and in the water the stars a heartbeat behind their own movement, as you remember them.{/n}
{n}Eliandra kneels at the basin in her white robes with her hair unbound. She does not look up when you come in.{/n}''',
        c("Continue", "rite")),
    el("rite", '''"Kneel across from me," she says. "Keep your hands where I can see them. When I have called her, you will name what you give. Aloud. Once." {n}She dips her fingers in the water and touches them to her eyelids, her lips, her heart.{/n}
"Shimmering Maiden, mistress of the lights of the north. Your servant has never asked you for anything. She does not ask now. Someone else has come to ask for her." {n}The water in the basin shivers, though nothing has touched it.{/n}''',
       c("[Kneel across the basin from her.]", "planned", requires=(PLANNED,)),
       c("[Kneel across the basin from her.]", "name", forbids=(PLANNED,))),
    nar("planned", '''{n}You kneel. The paper you burned over the lamp is still in your head, every line of it, the price written out plain the way you would write the cost of an assault. You know what you are going to say. You have known since the lamp caught. That does not make it easier; it only makes it yours.{/n}''',
        c("Continue", "name")),
    nar("name", '''{n}Eliandra's eyes are open and fixed on the water, and very far away. When she speaks again her voice is her own, but slow, as if she were reading from a page that turned as she read it.{/n}
{n}"She is here," she says. "She is listening. Name it."{/n}''',
        c('[Offer the crusade\'s gold for her temples] "A temple of Pulura in every town of Sarkoris we take back. Gold, stone, priests. Whatever it costs."',
          "gold", forbids=(TERMS_READ, OFFER_REFUSED)),
        c("[Offer your sight of her lights] " + NAME_IT,
          check=dict(Skill="SkillLoreReligion", DC=24, Success="taken", Failure="counter"), forbids=(TERMS_READ,)),
        c("[Offer your sight of her lights] " + NAME_IT,
          check=dict(Skill="SkillLoreReligion", DC=18, Success="taken", Failure="counter"), requires=(TERMS_READ,)),
        c('[Offer the lights, and keep one hand behind your back] "My sight of her lights."', "cheat", mythic="Trickster"),
        c("[Walk away from the basin.]", "walk")),
    nar("gold", '''{n}The stars go out of the basin. All of them, at once, as if a hand had been laid over the water. Overhead the sky burns on, untouched. In the bronze bowl there is only black.{/n}
{n}Eliandra does not move. "She does not sell," she says, in the slow, reading voice. "She never has. Offer her something that is yours, or go."{/n}
{n}One by one the stars come back into the water.{/n}''',
        c("[Try again.]", "name_again", flags=(OFFER_REFUSED,))),
    nar("name_again", '''{n}The water is still again. Eliandra has not moved; only her lips, which are counting something, or praying. Overhead the sky burns on.{/n}
{n}"Name it," she says. "Something that is yours."{/n}''',
        c("[Offer your sight of her lights] " + NAME_IT,
          check=dict(Skill="SkillLoreReligion", DC=24, Success="taken", Failure="counter"), forbids=(TERMS_READ,)),
        c("[Offer your sight of her lights] " + NAME_IT,
          check=dict(Skill="SkillLoreReligion", DC=18, Success="taken", Failure="counter"), requires=(TERMS_READ,)),
        c('[Offer the lights, and keep one hand behind your back] "My sight of her lights."', "cheat", mythic="Trickster"),
        c("[Walk away from the basin.]", "walk")),
    nar("taken", '''{n}You say it aloud, under the open stars: that you give up your sight of her lights, for good, in Eliandra's place. Your voice sounds very small in the round room. Nothing happens.{/n}
{n}Then the water moves. Light runs across it from rim to rim: green first, then rose, then a white like frost on a blade. It rises out of the basin in a slow curtain and hangs in the air of the chamber between you and her, rippling, the northern lights brought indoors.{/n}''',
        c("Continue", "remember", requires=(LIGHTS_SEEN,)),
        c("Continue", "veil", forbids=(LIGHTS_SEEN,))),
    nar("remember", '''{n}You know them. You watched them from a dead chieftain's cairn with your sword across your knees. You look at them now as hard as you can, because you understand, a heartbeat before it happens, that this is the last time.{/n}''',
        c("Continue", "abyss", requires=(ABYSS_DARK,)),
        c("Continue", "veil", forbids=(ABYSS_DARK,))),
    nar("abyss", '''{n}You looked for them once under the red sky of the Abyss, and found nothing, and minded. You will mind for the rest of your life. You knew that when you named them.{/n}''',
        c("Continue", "veil")),
    nar("veil", '''{n}The lights draw together, and turn, and come towards you. You do not flinch. They pass over your face like cool water, and your eyes sting, and then there is a feeling you know: the slide, the gentle wrongness of a gaze that has been told to look elsewhere. The same veil that hid her shrine from every unfriendly eye for a century, turned now on one pair of eyes.{/n}
{n}When you look up again the stars are still there. The lights are not. Eliandra is staring at the air above the basin where they must, for her, still be hanging, and there are tears on her face.{/n}''',
        c("Continue", "granted")),
    el("granted", '''"She has taken it," she says. Her voice is her own again, and it shakes. "She turned her veil on you. Her lights will stand over Sarkoris every winter for as long as there is a sky, and you will never see them again. Wherever you look for them, your eyes will look somewhere else." {n}She lets out a breath that is half a sob.{/n} "And she has let me go. I felt it. Like a knot I had forgotten was tied."''',
       c('"Then it was a fair price."', "fair"),
       c('"Describe them to me. Just once."', "describe")),
    el("fair", '''"Fair." {n}She wipes her face with the heel of her hand, without ceremony.{/n} "You gave her the one thing in her domain you loved, and you gave it for someone else. It was more than fair. It was the best offering anyone has made in this room in a hundred years, and it was not even yours to need."''',
       c("Continue", "after")),
    el("describe", '''"Now?" {n}She wipes her face with the heel of her hand, without ceremony, and looks up at the empty air.{/n} "Green at the edges, like new leaves held up to the sun. Rose in the folds. And at the heart a white so clean it hurts to look at, moving, always moving, as if the whole sky were breathing out." {n}She stops.{/n} "I will tell you every winter. I promise you that. I will be very tiresome about it."''',
       c("Continue", "after")),
    el("after", '''"Go and sleep," she says. "I will put out the basin. I need to be alone with her a little while. I have never once thanked her for anything, either."''',
       c("[Leave her at the basin.]", flags=(LEAVE, LIGHTS_GIVEN), alignment=("Good", 1))),
    nar("counter", '''{n}You say it aloud: that you give up your sight of her lights, in Eliandra's place. The water moves. Green light runs across it rim to rim, and rises, and hangs in the air between you.{/n}
{n}And then it falters. In the basin the lights begin to sink, like a lamp let down a well, and something else goes down with them: a second light, softer, greener, the colour of the shimmer that lay on Eliandra's hand when she healed the wounded. It goes down and down into the black water, and the stars close over it.{/n}''',
        c("Continue", "reading")),
    el("reading", '''{n}Eliandra is white to the lips. She stares into the water a long while before she speaks, and when she does it is slowly, choosing each word like a foothold.{/n}
"You named it, and she heard you, but it was not enough, or not in the right shape. That is how I read it." {n}She swallows.{/n} "She showed me my own light going down into the water with yours: the strength she gave me at thirteen, for what I gave up. If I take back what I gave, the gift goes back with it. Your lights, and my strength. That is her answer."
"I would still be a priestess. I would still heal. Only not as I did. Not the strongest of her servants. Just one of them."''',
       c("[Let her choose.]", "choose"),
       c('[Refuse it for her] "No. You\'re not paying for this. I\'ll find another way."', "refused")),
    el("choose", '''{n}She looks at you across the basin, and then down at her hands, and you watch her decide. It does not take long. Perhaps she decided a century ago and has only been waiting for someone to ask.{/n}
"Yes," she says to the water. "Take it. Take them both." {n}The water stills. The stars come back into it, and for a heartbeat there is a green thread among them, and then there is not.{/n}''',
       c("Continue", "veil2")),
    nar("veil2", '''{n}The lights that hung in the air turn and come towards you and pass over your face like cool water, and your eyes sting, and then there is the slide, the gentle wrongness of a gaze told to look elsewhere. When you look up, the stars are there. The lights are not.{/n}
{n}Eliandra sits back on her heels. She looks smaller than she did, and very tired, and oddly light, like a woman who has set down a pack she carried so long she forgot it had weight.{/n}''',
        c("Continue", "after2")),
    el("after2", '''"It is done," she says. "She has let me go. I felt the knot come undone." {n}She holds out her hand and looks at it. No shimmer comes.{/n} "And that is gone. Well. I carried it for a hundred years. It will be strange, being ordinary. I think I shall be very bad at it for a while."''',
       c("[Take her hand.]", flags=(LEAVE, LIGHTS_GIVEN, REWARD_RETURNED), alignment=("Good", 1)),
       c("[Leave her with the water.]", flags=(LEAVE, LIGHTS_GIVEN, REWARD_RETURNED), alignment=("Good", 1))),
    el("refused", '''"Refuse it for me." {n}Something in her face closes, gently, like a door drawn to against a draught.{/n} "It was offered to me, Commander. It was mine to take or not." {n}She rises, and the water in the basin is only water.{/n} "But you meant it kindly. I know you did. Go and sleep. My Lady will not be asked twice tonight."''',
       c("[Go.]", flags=(NO_LEAVE, REFUSED_FOR_HER))),
    nar("cheat", '''{n}You say it aloud, under the open stars, with your left hand out of her sight behind your back and two fingers crossed, the way a child crosses them on a lie. You have a plan for afterwards; you always have a plan. Take the leave now, and later find the loophole that gives the lights back.{/n}
{n}The water goes black. Not dark: black, a hole in the floor of the world. Across it Eliandra's face turns grey. She looks at your left arm, and then at your face.{/n}''',
        c("Continue", "caught")),
    el("caught", '''"I told you," she says, very quietly. "She has turned aside the eyes of demons for a hundred years. Did you think she would not see your hand?" {n}She rises. Her hands are shaking.{/n}
"Get out of the heart of my shrine, Commander. Now. Before she remembers your face."''',
       c("[Go.]", flags=(NO_LEAVE, TRIED_TO_CHEAT))),
    nar("walk", '''{n}You stand up. Eliandra's eyes follow you, but she does not speak; she does not stop you, and she does not ask. Behind you the water in the basin settles, and the stars in it go on burning, a heartbeat behind the sky.{/n}''',
       c("[Leave the star-heart.]", flags=(NO_LEAVE,))),
], requires=(), forbids=(LEAVE, NO_LEAVE), fit="T",
    RequiresAnyGroups=[[TERMS_READ, OBSERVED]], TricksterDevice=True, TricksterState="vow")



# --- The night after the rite (T; inline): the eyes that paid ---------------------------------------------------------------

shrine(E + "ch5.night_after", "The night after the rite", '"My eyes are still stinging."', [
    el("start", '''"They will, until morning." {n}Eliandra is still in the white robes of the rite, with her hair unbound; she has not slept either. She takes up a bowl of water and a folded cloth as if she had been waiting for you to say it.{/n} "It was the same for my brothers, when they saw my Lady's lights for the last time before the veil closed over us. It passes. Come to the guard room and sit down. I have washed the eyes of the dying for a century. I can wash the eyes of one living fool."''',
       c("[Let her.]", "wash"),
       c('"Fool?"', "fool")),
    el("fool", '''"Fool." {n}She sounds almost fond.{/n} "You knelt in a cave and gave a goddess something you loved, for a woman you have known a handful of days, who asked you for nothing. I have seen many offerings in a hundred years. I have never seen a more foolish one." {n}She holds the door of the guard room.{/n} "Sit."''',
       c("[Sit.]", "wash")),
    nar("wash", '''{n}You sit on the edge of a guard's cot and she kneels in front of you and lays the wet cloth across your eyes, and holds it there, lightly, with the flat of her hand. She does not speak. Through the cloth you can feel her fingers, and through her fingers something that might be a prayer, or might only be her pulse.{/n}
{n}After a while she lifts the cloth away. The stinging is less. The room is dark except for the starlight that comes, somehow, even here, through a crack in the rock overhead.{/n}''',
        c("Continue", "kiss")),
    el("kiss", '''"I cannot ask you for anything yet," she says. "I have not learned how. I asked my Lady for nothing for a hundred years, and she has let me go, and I do not know what to do with my hands." {n}She looks at them, folded on your knee, and then at your face.{/n}
"So I will not ask. I will only do this, which I have wanted to do since you knelt at the basin, and you may tell me in the morning that I was wrong."''',
       c("Continue", "eyes")),
    nar("eyes", '''{n}She rises on her knees and kisses your eyes: the left, and then the right, where the lights went in. Her lips are cool from the water and not at all steady. She stays there, close, her unbound hair falling round both your faces like a curtain, her breath warm against your lashes.{/n}
{n}Then she sits back on her heels, very straight, with colour high in her face and the composure of a high priestess everywhere else.{/n}''',
        c('"You weren\'t wrong."', "right", flags=(FLIRTED,)),
        c("[Reach out and touch her face.]", "touch", flags=(FLIRTED,))),
    el("right", '''"No," she says. "I did not think so. But I have been wrong about so many things lately, Commander, that I have got into the habit of checking." {n}She rises, takes up the bowl.{/n} "Sleep. The column leaves soon, and I have a great deal to carry, and I would like you to be awake for it."''',
       c("[Sleep.]", flags=(E + "eyes_kissed",))),
    nar("touch", '''{n}Her skin is warm under your fingers. She goes very still, the way she went still over the lens in the star-heart, measuring something at the edge of what can be seen. Then she turns her face into your palm, briefly, and closes her eyes.{/n}
"Not tonight," {n}she says against your hand.{/n} "Not in this place, with our dead so close. But I wanted you to know that I am counting." {n}She rises, takes up the bowl, and at the door she stops.{/n} "Sleep. Before we leave, I am going to ask you something. I am practising."''',
        c("[Sleep.]", flags=(E + "eyes_kissed",))),
], requires=(LEAVE, LIGHTS_GIVEN), forbids=(E + "eyes_kissed", COMMITTED, DECLINED), fit="T", delay=0)


# --- The commit's letter (T). The first mile and the star-heart are hosted on her Drezen presence (eliandra_stars). ------

LIED_ABOUT_HAND = E + "lied_about_hand"   # asked on the road what the hidden hand meant, the Commander lied again
LETTER_KEPT = E + "letter_kept"           # the road letter kept, its answer reserved for after the war (the R2-6 late yes)

page(E + "ch5.road_letter", "A letter from the fords", [
    ep("start", '''{n}The letter is written on the back of a star chart, in a small exact hand that has been corrected twice and nowhere crossed out.{/n}
"Commander. We are four days from Pulura's Fall, on the old road to the Drezen fords, and the mule has bitten Odden again. I am writing because I said I would, and because I have not stopped thinking about what I asked you, or what you answered."''',
       c("[Read on.]", "alone", forbids=(LIED_ABOUT_HAND,)),
       c("[Read on.]", "hand", requires=(LIED_ABOUT_HAND,))),
    ep("alone", '''"You were not wrong to want me alone. I think that is what wanting is, and I have not practised it. But I spent a century making rules about other people's hearts, and I will not make one now that says my people come second, or that you do. I have decided that I do not have to choose. It is a very new idea, and I am rather proud of it."''',
       c("[Read on.]", "ask")),
    ep("hand", '''"You lied to me on the road about your hand. I have thought about it for four days, which is three more than it deserved and fewer than I needed. I have decided that a person who lies to protect a plan is not the same as a person who lies for pleasure, and that I would rather know which one I am dealing with than guess. So I am going to ask you, in writing, where you cannot see my face: what did you mean to do with it? And then the other question, the one I did not ask."''',
       c("[Read on.]", "ask")),
    ep("ask", '''"So I am asking again, which I have never done in my life. Drezen, or the road? I will not ask a third time, but I will not stop hoping, either; I find I have no talent for that yet.
"One thing more. I did not close the heart of the shrine when we left. I told Odden I forgot. I did not forget. Write to me at the fords; the carrier knows the way. E."''',
       c('[Write back: either] "Either. Both. Bring them all. Ask me every morning."', flags=(COMMITTED, LETTER_ANSWERED),
         forbids=(LIED_ABOUT_HAND,)),
       c('[Write back the truth, and then: either] "I meant to cheat her and get the lights back. I\'m sorry. Either. Both. Ask me every morning."',
         flags=(COMMITTED, LETTER_ANSWERED), requires=(LIED_ABOUT_HAND,)),
       c('[Keep the letter. Write that you will answer when the war is done.]', flags=(LETTER_KEPT,))),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED,), delay=48, kind="letter")


# --- Reactions (T; ledger 05 §3.1 row 13, exactly King Thaberdine and Ulbrig): the King's one list entry, Ulbrig after ---

KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"          # FoolKing_Tavern/AnswersList_0054 (Chapter 5; shared with the Table)
KING_C5_RETURN = "7b050ba0745bf144e815632e39b34853"   # FoolKing_Tavern/Cue_0065 "Beer is a noble drink!"
ULBRIG_HUB = "0a50c9c878844ed4a69b8d6131304c5e"       # DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001


def react(id, *args, **kw):
    PATH_FIT[id] = "T"
    SCENES.append(reaction(*args[:1], id, *args[1:], relationship=REL, **kw))


react(E + "react.king_stone", "Thaberdine", ("trickster.ever", LEAVE, TABLET, "fool_king.available"),
    '''"Commander! There was a priestess in here last night. A real one. Glowing, very nearly." {n}The King lowers his voice to what he believes is a whisper.{/n}
"She asked to see my stone. Very polite. Looked at it for an hour and never touched it, and when I said my ancestors are buried under it, probably, she said: 'Probably.' Just like that. 'Probably.'" {n}He takes a long, wounded drink.{/n} "Then she paid for her water. Nobody pays for water in my tavern. I have decided she's the most frightening woman in Drezen, and I'm having the stone dusted."''',
    answer_list=KING_C5, speaker="conversant", NativeReturnCue=KING_C5_RETURN, forbids=("fool_king.gone", CLOSED),
    chapter=5, last=5, Chapters=[5], entry='"Your Majesty. Anyone interesting in tonight?"')

react(E + "react.ulbrig_priestess", "Ulbrig", ("trickster.ever", HEART_SEEN, LIGHTS_GIVEN, "ulbrig.in_party"),
    '''"The priestess from the dry fall, eh. The Maiden's woman." {n}Ulbrig turns his cup round on the table, and round again.{/n}
"My gran used to take us up the ridge in winter to see the Maiden's lights. She'd say: the Shimmering One gives nothing for nothing, so if you want something of her, give her something you'd miss." {n}He looks at you, not unkindly.{/n} "You gave her your eyes for that woman, warchief. Folk say so round the fires. My gran would've called that a fair price and a daft one, both at once, and then she'd have sat you down by the fire and told you the lights were green tonight, so you'd know."''',
    answer_list=ULBRIG_HUB, forbids=("ulbrig.dead", "ulbrig.kicked_out", CLOSED), chapter=5, last=5, delay=24,
    entry="\"You look like you've heard something, Ulbrig.\"")

react(E + "react.ulbrig_ordinary", "Ulbrig", ("trickster.ever", HEART_SEEN, "ulbrig.in_party"),
    '''"The priestess from the dry fall, eh. The Maiden's woman." {n}Ulbrig turns his cup round on the table, and round again.{/n}
"She healed a lad of ours with a split hand yesterday. Took her an age. Had to sit on the step after, grey as a stone." {n}He drinks.{/n} "My gran used to say the Shimmering One gives nothing for nothing. That one gave something back, warchief, and folk round the fires say it was so she could have you. I've known Kellid women to give up a good deal less for a good deal worse." {n}A grin, slow.{/n} "Mind you're worth the walk to her."''',
    answer_list=ULBRIG_HUB, forbids=("ulbrig.dead", "ulbrig.kicked_out", CLOSED, LIGHTS_GIVEN), chapter=5, last=5, delay=24,
    entry="\"You look like you've heard something, Ulbrig.\"")

# --- Epilogue pages (Chapter 6; no page effects) ---------------------------------------------------------------------------

EPI = "EliandraEpilogue"
EP_GUARD = dict(forbids=("sacrifice",), ForbidOverrides={"sacrifice": "trickster.commander_back"})


def epilogue(id, text, requires, forbids=(), paragraphs=(), any_groups=()):
    sid = E + "epilogue." + id
    PATH_FIT[sid] = "T"
    extra = dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}
    SCENES.append(scene(sid, "", EPI, 6, "", [n("page", "Narrator", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=(*forbids, *EP_GUARD["forbids"]), last=6,
                        Relationship=REL, ForbidOverrides=dict(EP_GUARD["ForbidOverrides"]), **extra))


EPILOGUE_PARAGRAPHS = (
    p('''{n}When the stargazers' artifact set the northern stars ablaze over Threshold, every soldier in the siege lines looked up. The Commander saw the stars blaze, every one of them, and did not see the Maiden's lights that rose among them; the eye slid off them to the stars, as it always would. That winter, and every winter after, Eliandra described the lights over Sarkoris aloud, in great detail, until she was begged to stop, and then for a little longer.{/n}''',
      requires=(LIGHTS_GIVEN, LIGHTS_LIT)),
    p('''{n}Every winter the Maiden's lights stood over the ruins of Sarkoris, and every winter the Commander looked up at a sky of plain stars while Eliandra described them aloud, in great detail, until she was begged to stop, and then for a little longer. She had promised to be tiresome about it. She was a woman who kept her promises.{/n}''',
      requires=(LIGHTS_GIVEN,), forbids=(LIGHTS_LIT,)),
    p('''{n}She was never again the strongest of her Lady's priestesses. She healed as other priestesses heal, one wound at a time, and slept afterwards, and complained about it. The temples she reopened filled with priests who could do more than she could, and she ordered every one of them about.{/n}''',
      requires=(REWARD_RETURNED,)),
    p('''{n}Katair kept the charts she had rolled wrong on the shrine's last night, and never unrolled them. He said they were the record of an observation, and nothing is erased.{/n}''',
      requires=(CHARTS,)),
    p('''{n}The first rule she made for the new temple of Pulura at Iz was that nobody in it would ever be forbidden to love anyone. When the old stargazers asked why, she said she had it on good authority that she had been wrong, and would not say whose.{/n}''',
      requires=(LOVERS_TRUTH,)),
    p('''{n}When she finally stood on the shore of the lake below Iz, it was a salt pan, as it had always been going to be, and there were no painted barges. She was quiet a long while. Then she said, "There. I knew you were lying," and took the Commander's hand, and did not let go of it all the way back.{/n}''',
      requires=(SARKORIS_LIE,)),
    p('''{n}Odden kept his day of remembrance every year after, on the day the demons came. He laid the good plates, braided his beard, and poured the first cup for the stargazers who were not there. The second, every year, was for the anonymous benefactor who had left a bottle at the foot of the dry fall.{/n}''',
      requires=(REMEMBRANCE, WINE_LEFT)),
    p('''{n}Odden kept his day of remembrance every year after, on the day the demons came, and every year Eliandra took one cup, and every year the room noticed.{/n}''',
      requires=(REMEMBRANCE,), forbids=(WINE_LEFT,)),
    p('''{n}She liked to tell the young stargazers that in a hundred years her Lady's veil had been seen from outside exactly once, by somebody sitting on a dead chieftain's cairn with a stolen stone in a cart, and that this was why one should always look up.{/n}''',
      requires=(LIGHTS_TOLD,)),
    p('''{n}She never again let the Commander near an altar of Pulura's with a hand out of sight. It became a joke between them, and then it stopped being a joke, and then it was a joke again.{/n}''',
      requires=(TRIED_TO_CHEAT,)),
    p('''{n}Whenever the Commander tried to spare her something, she would say, "It was mine to take," and take it. It was, the Commander eventually admitted, the most useful thing anyone had ever said to them in an argument.{/n}''',
      requires=(REFUSED_FOR_HER,)),
    p('''{n}Odden roared her name at the first feast in the new temple, as he had in the cave, and the room took it up, and she laughed exactly as she had then, with her hand on her heart and no idea what to do with her face.{/n}''',
      requires=(TOASTED,)),
    p('''{n}When the war was done the Commander carried the King's stone back to the chiefs' ground below the dry fall and set it up again in the gap it had left. The King came with a cart of beer and made a speech to the cairns, which went on for some time. The dead had heard worse. Eliandra said so, afterwards, and the King took it as a compliment.{/n}''',
      requires=(E + "drezen.stone_home",)),
    p('''{n}The spring after the war Katair went back to the Stone Tree, and this time he did not go alone. He took a cup, and the Commander, and poured the first measure over the stone with his own name on it, and said that it could stop lying for him now. Then he stood there a long while, and nobody hurried him.{/n}''',
      requires=(E + "drezen.katair_grave",)),
    p('''{n}The first spring, the Commander walked the road to Iz beside her, as asked and answered. It was ash most of the way, and green in places, and at the old meeting-ground of the elders she stopped and wept for a long time, and then set up a table and began, immediately, to argue with the local priests.{/n}''',
      requires=(E + "drezen.road_promised",)),
    p('''{n}She asked again, the first spring, as she had said she would. The war had decided by then; what it decided, and whether the Commander walked the road to Iz with her, the chroniclers do not agree. She did not ask a third time. She never needed to.{/n}''',
      requires=(E + "drezen.road_open",), forbids=(E + "drezen.road_promised",)),
    p('''{n}Regnard's plain sword hung on the first wall of the new temple at Iz. Every child who asked was told that its owner had wanted to change so badly that he practised with it every night for years, alone, and then used it.{/n}''',
      requires=(E + "regnard_sword_kept",)),
    p('''{n}The chiefs' swords lay on their cairns below the dry fall, blades to the north, every one where Regnard's record said it belonged. The crusaders who laid them had got four wrong. Katair corrected them the next spring, and wrote the corrections in the margin of Regnard's record, and crossed nothing out.{/n}''',
      requires=(E + "regnard_swords_home",)),
    p('''{n}She saw the sea at last, the second summer after the war: a lake with no other side, exactly as the trader had promised. She stood in it to her knees in her grey robe and would not come out, and said that she had been right not to believe him, because he had not described it properly at all.{/n}''',
      requires=(E + "drezen.sea",)),
    p('''{n}Whatever the demon had carried off from Pulura's Fall, the Commander burned where it was found, every page, as promised. Eliandra never asked what it had cost to find. She only asked, every year on that day, whether it had all burned. It had.{/n}''',
      requires=(RESEARCH_BURN, "eliandra.research_stolen")),
    p('''{n}The demon had carried nothing of theirs away; the Commander had seen to that at the shrine, and there was nothing in his hands to burn. The stargazers' work went to the crusade's scholars as she had wanted, in chests under her own seal, and she read every report they wrote from it, and corrected the margins.{/n}''',
      requires=(RESEARCH_BURN,), forbids=("eliandra.research_stolen",)),
    p('''{n}What was left of the stargazers' work went to the crusade's scholars, and some of it, it is said, helped at Threshold. Eliandra never asked what the rest was used for. Once a year she asked the Commander whether they had decided carefully, and listened to the answer with great attention.{/n}''',
      requires=(RESEARCH_KEEP,)),
)

epilogue("together", '''{n}Eliandra, who had given almost her entire life over to duty, gave the rest of it to Sarkoris. The temples of Pulura and the old Sarkorian gods opened their doors again, one ruined town at a time, and their priests went out to heal the wounds of the people and the land. She led them, from a mule, a cart, a borrowed room, and more often than not from the side of the road.{/n}
{n}Some mornings she was in Drezen. Some mornings the Commander was on the road with her, in the ash and the new green. Every morning she asked one question, and never the same one twice, and the Commander was never once allowed to give the same answer.{/n}''',
         requires=(COMMITTED,), forbids=(CLOSED,), paragraphs=EPILOGUE_PARAGRAPHS)

epilogue("late", '''{n}Her letter from the fords stayed in the Commander's coat through Threshold, as promised, with its answer owed. The day after the war ended, the Commander wrote it: either, both, bring them all, ask me every morning.{/n}
{n}She came to Drezen a month later with Odden, the girl with the sling, and a mule that bit everyone. She said she had not asked a third time, as she had promised, and that she had not stopped hoping either, as she had also promised, and that she hoped the Commander appreciated how difficult it had been to keep both. Then she gave the rest of her life to Sarkoris, as she had meant to all along, and to the Commander, which she had not.{/n}
{n}The night she came, in the Commander's rooms in Drezen, she unpinned the grey cloak herself and let it fall, and stood a moment in the lamplight in the white robes of an office she no longer owed anyone, and then unlaced those too, tie by tie, looking at the Commander the whole while. "I have waited through a war," she said. "I am not waiting through the lamp." She put it out with two fingers, took the Commander's face in both hands, and drew them down onto the bed with her.{/n}
{n}In the morning Odden, delivering a message nobody had asked him to deliver, found the door unbarred and the high priestess of Pulura asleep with her hair across the Commander's pillow, and went away again, and told the entire cooper's shop by noon.{/n}''',
         requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED), paragraphs=EPILOGUE_PARAGRAPHS)

epilogue("unasked", '''{n}The war moved faster than the stargazers' carts, and the question she had carried away from the basin was never asked on the road. The day after Threshold she came to the Commander's door in Drezen, with the hood of her travelling cloak thrown back and the dust of Sarkoris on her boots, and asked it there: Drezen, or the road?{/n}
{n}The Commander said either. She said that would do to begin with, and that she would ask again every morning.{/n}
{n}That night, in the Commander's rooms in Drezen, she unpinned the grey cloak herself and let it fall, and stood a moment in the lamplight in the white robes of an office she no longer owed anyone, and then unlaced those too, tie by tie, looking at the Commander the whole while. "I have waited through a war," she said. "I am not waiting through the lamp." She put it out with two fingers, took the Commander's face in both hands, and drew them down onto the bed with her.{/n}
{n}In the morning Odden, delivering a message nobody had asked him to deliver, found the door unbarred and the high priestess of Pulura asleep with her hair across the Commander's pillow, and went away again, and told the entire cooper's shop by noon.{/n}
{n}Then she gave the rest of her life to the revival of Sarkoris, as she had always meant to, and to the Commander, which she had not.{/n}''',
         requires=(LEAVE,), forbids=(COMMITTED, DECLINED, CLOSED), paragraphs=EPILOGUE_PARAGRAPHS,
         any_groups=((FLIRTED,),))
epilogue("released", '''{n}Eliandra led the stargazers into what was left of Sarkoris, released from her vow, and gave herself to its revival. The Commander had given what was needed at the basin, or watched her give it, and had been a friend to her and her people when they had none; but whatever might have been between them was never spoken, by either of them, and the war ended before it could be. She wrote once, after Threshold, to thank the Commander for the rite. The letter was warm, and exact, and asked nothing.{/n}''',
         requires=(LEAVE,), forbids=(COMMITTED, DECLINED, CLOSED, FLIRTED))

epilogue("own_offering", '''{n}The stargazers took the road still bound by their high priestess's vow, and she carried it as far as the fords. There, in the spring after Threshold, under the open stars and with no one to see it, she gave her Lady back the strength she had been given at thirteen, and asked for nothing in return, and was let go.{/n}
{n}She was never again the strongest of Pulura's priestesses. She devoted herself to the revival of Sarkoris anyway, one wound at a time, and wrote to the Commander about it every week, in a small exact hand, correcting herself in the margins and never crossing anything out.{/n}''',
         requires=(NO_LEAVE,), forbids=(LEAVE, CLOSED))

epilogue("vowed", '''{n}Eliandra, who had given almost her entire life over to duty, devoted herself to the revival of the former lands of Sarkoris. The temples of Pulura and the old Sarkorian gods opened their doors again, and their priests went out to heal the wounds of the people and the land.{/n}
{n}She remained the strongest of her Lady's priestesses to the end of her life, and she remained her Lady's alone. Once, near the end of it, a young stargazer asked her whether she had ever regretted her vow. She said that someone had asked her, once, what her Lady took in return, and that she had thought about the question for a great many years afterwards, and had never quite finished.{/n}''',
         requires=(STARTED,), forbids=(LEAVE, NO_LEAVE, CLOSED))

epilogue("declined", '''{n}Eliandra led the stargazers to the fords and beyond, into what was left of Sarkoris, and gave herself to its revival. She had asked once, on the first mile, and had not been given an answer she could take.{/n}''',
         requires=(DECLINED,), forbids=(COMMITTED, CLOSED, E + "letter_kept"), paragraphs=(
    p('''{n}She asked again from the fords, in writing, and was answered with nothing. She did not ask a third time. She had said she would not.{/n}''',
      requires=(E + "ch5.road_letter",)),
    p('''{n}She had said she would write when she knew where they were. The war moved faster than the stargazers' carts, and whatever she wrote never found the Commander's hands.{/n}''',
      forbids=(E + "ch5.road_letter",)),
    p('''{n}She was an ordinary priestess now, or near enough, and a busy one, and slept after every healing like anyone else.{/n}''',
      requires=(REWARD_RETURNED,)),
    p('''{n}She was still the strongest of her Lady's priestesses, and the busiest; the lights the Commander had given up stood over every temple she opened.{/n}''',
      forbids=(REWARD_RETURNED,)),
    p('''{n}When travellers from Drezen came through her temples she asked after the Commander, briefly and exactly, the way she took an evening's reading, and wrote the answers down.{/n}'''),
))

epilogue("closed", '''{n}Eliandra led the last of the stargazers out of Pulura's Fall and into what was left of Sarkoris, and gave the rest of her life to its revival. Temples of Pulura opened their doors again in the ash, and in each of them, at the evening reading, the name of the Commander who had knelt at her basin was spoken among the names of those who had helped her people when no one else knew they existed.{/n}
{n}Pulura's children remembered, as she had promised. So did she.{/n}''',
         requires=(CLOSED, LEAVE))


# --- Registration ------------------------------------------------------------------------------------------------------

def integrate(payload):
    """Her native reads (the stargazers' artifact over Threshold, the Trickster's sight), her Derived keys and the
    book-picture fallbacks (Eliandra, Katair, Odden). The shared world keys (eliandra.met_ch5, eliandra.shrine_left,
    fool_king.*) bind on demand in trickster_world."""
    for kind, table in BINDINGS.items():
        for key, value in table.items():
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != value:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = value
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    fallbacks = payload.setdefault("PortraitFallbacks", {})
    fallbacks.setdefault("Eliandra", PORTRAIT_GUID)
    fallbacks.setdefault("Katair", KATAIR_PORTRAIT)
    fallbacks.setdefault("Odden", ODDEN_PORTRAIT)
