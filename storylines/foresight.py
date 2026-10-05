"""Shyka's page: the Trickster's one foresight through-line (Writer/handoffs/12-TRICKSTER-FORESIGHT.md, §2, §4, §7, and
§2.4a, the echoes, added 2026-10-03).

Canon: Shyka the Many sees every branch (Council_Shyka/Cue_0013 7e183baf) and refuses to share foresight, because "if we get
things mixed up and give you answers that don't belong to the world in which you live... An entire reality might collapse"
(Cue_0021 7c1c2c83). Shyka keeps "forgetfulness and absent-mindedness" for itself (Cue_0025 57faab7d), finds this timeline
"less interesting than some of the others" (TricksterRankUp_4/Cue_0023 058786a4), and one of Shyka's selves is the Commander
(Shyka_Offer/Cue_0024 a55d5848, Cue_0035 a48bb45a).

Authored (RRT, labelled): the bargain Shyka may refuse, for one Prologue memory every Commander has (Terendelev's promise,
KenabresSquare/WelcomeDialogue Cue_0039 f5651757 / Cue_0042 92456eff; the festival square, Cue_0052 2918b526; waking in the
caves, CavesUnderKenabres/MeetSeelahAnevia Cue_0004 159c4442); the page of the Commander's own other endings, each spoiled
on purpose, plus a fire from no world (the east gate); Shyka's "collecting" of a memory as an archive curiosity.

The page is the lock-in gate of the Trickster's fate-bending timeline (user rule 2026-10-03; 12 §2.8): gated consumers
may require it (echo beats, echo-informed preparations, foresight-leaning devices, later the household stance, W0c), but
it opens the road and never walks it: every gated outcome keeps its own checks and costs. The page is read only through the
public keys below, by the consumers listed in READERS and CONSUMERS (tests/ForesightTests.cs: Foresight_GateContract).
Route echoes (§2.4a, §2.9) export only when the coordinator allocates the slot (ALLOCATED, 06 "Echo slots"); Devarra's
and Terendelev's remain inactive proposals: colour never warrants allocation. A slot requires a documented, unresolved
believability problem that the woman's existing canon clues cannot solve. Each continues with the host node's own choices.

Scenes (Relationship "foresight", a framework: never a romance, never closed; Shyka is a non-romance ally):
  trickster.foresight.page          Ch3 or Ch5 (while Shyka is present), inline on Council_Shyka AnswersList_0003
  trickster.foresight.memory        a rest-delivered memory page: Shyka's handwriting where the memory was
  trickster.foresight.fire_watch    Ch3/Ch5, inline on Thaberdine's tavern lists: the east-gate misstep (Favors -50)
  trickster.foresight.offer_line    Ch5, inline on Shyka_Offer AnswersList_0011: the false gate named, the cost, the wager
  trickster.foresight.noticed.*     the witnesses: Anevia and Seelah (the caves), Thaberdine (a toast he never gave)
  + Last Call Block A paragraphs (Areelu's report), and the Ledger's "What I no longer remember" journal lines.
"""
import copy
import re

from story_format import c, n, p, reaction, scene

SCENES = []
REL = "foresight"
P = "trickster.foresight."

# --- Keys (12 §2.3, §4) ---------------------------------------------------------------------------------------------------
ACCEPTED = P + "accepted"
RAISED = P + "raised"
COST_PROMISE = P + "cost.promise"
COST_SQUARE = P + "cost.square"
COST_CAVES = P + "cost.caves"
COSTS = (COST_PROMISE, COST_SQUARE, COST_CAVES)
GATE_FIRE = P + "gate_fire"            # the page held the east gate (set at the end of the page; the CommittedFlag)
GATE_WATCH = P + "gate_watch"          # the misstep: Thaberdine's drunks posted at the east gate
WAGER = P + "wager"                    # the Commander's wager stands: Shyka cannot name what comes after the page
COUNTER = P + "counter"                # §7.2: the counteroffer; Shyka's wager left unsettled, collected in Chapter 5
MEMORY_TOLD = P + "memory_told"        # §7.3: the Chapter 5 line read the receipt (no rest came first)
SHYKA_ESSENCE = P + "shyka_essence"    # latch: the Council's siphon held with Shyka's essence in it (native item)
PAGE_SCENE = P + "page"
MEMORY_SCENE = P + "memory"
WATCH_SCENE = P + "fire_watch"
OFFER_SCENE = P + "offer_line"
# Public keys for echo(), gap(), and registered CONSUMERS (12 §2.4a).
# PAGE_TAKEN and GATE_BELIEVED require the current path; sold memories persist on trickster.ever.
PAGE_TAKEN = "foresight.page_taken"                          # the page was taken
GATE_BELIEVED = "foresight.gate_believed"                    # the page's false fire was believed (the drunks were posted)
GONE_SQUARE = "foresight.memory_gone.square_morning"         # Terendelev's promise or the festival square was paid
GONE_CAVES = "foresight.memory_gone.caves"                   # waking in the caves was paid

# --- Hosts ----------------------------------------------------------------------------------------------------------------
SHYKA_LIST = "e7236a1fe9273ba498b96b9616b3f379"     # c3/Mythic_Trickster/Council_Shyka/AnswersList_0003
SHYKA_BACK = "cd2b35a474db55544a63f59a67ac67bf"     # Council_Shyka/Cue_0002 (clean return to her list; Kaylessa's too)
OFFER_LIST = "d3d0efb4dfcc1964c923d7b2d6e0dc77"     # c5/Mythic_Trickster/Shyka_Offer/AnswersList_0011
# Shyka_Offer/Cue_0010 "Each of the Council members have given you their essence..." -> AnswersList_0011 (Shamira's return).
# Doc 12 §4 named Cue_0022; its replay ("We do not find it worthwhile to discuss these timelines") would contradict a scene
# in which Shyka has just discussed the page, so the coherent return is used instead (retcheck OK for both).
OFFER_BACK = "5d6810f1e0eb8204fa4c3211fc603769"
KING_C3 = "1a17d8053a3be7f47a7908eb6706f2fe"        # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0009 (Chapter 3)
KING_C5 = "6dccfd39947ef4242a8afbe36b21a46c"        # FoolKing_Tavern/AnswersList_0054 (Chapter 5)
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"     # NPC_Common/Anevia/AnswersList_0003
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"     # CompanionDialogues/Seelah/AnswersList_0003
SIPHON_SHYKA = "areelu.siphon.council_shyka"        # InventoryItems SyphonWithCouncilShyka (bound by areelu_trickster)
KAYLESSA_PRICE = "kaylessa.trickster.cost.shyka_price"   # §2.6: the other transaction with Shyka (read for one line only)
COUNCIL_GONE = ("shyka.gone", "council.fought", "council.fought_nocta_allied")

RELATIONSHIP = dict(
    Title="Shyka's page",
    Description=("I bought a page of my own other endings from Shyka the Many, and paid for it with a morning I can no "
                 "longer remember. Some of it was mine. Some of it was spoiled on purpose. Some of it was never mine at all."),
    Objective="Live past the page",
    Guidance=("On the Trickster path, in Chapter 3, offer Shyka the Many at the Council something no branch has shown them. "
              "Shyka may refuse, or raise the price. The page is never a map."),
    StartedFlag=ACCEPTED, ClosedFlag=P + "closed", CommittedFlag=GATE_FIRE, UnavailableFlags=["trickster.failed"],
    FailureFlags=[], JournalEntries=[])

# The memory names, in Shyka's receipts and in Areelu's report. One combination holds in any world: a single cost at the
# base price (or the counteroffer), exactly two distinct costs at the raised price (12 §2.3).
MEMORY = {"p": COST_PROMISE, "s": COST_SQUARE, "c": COST_CAVES}
COMBOS = (("p", (COST_PROMISE,), (RAISED,)), ("s", (COST_SQUARE,), (RAISED,)), ("c", (COST_CAVES,), (RAISED,)),
          ("ps", (RAISED, COST_PROMISE, COST_SQUARE), ()), ("pc", (RAISED, COST_PROMISE, COST_CAVES), ()),
          ("sc", (RAISED, COST_SQUARE, COST_CAVES), ()))


def combo_choices(prefix, text="Continue", flags=(), forbids=()):
    """Six mutually exclusive Continue choices, one per paid combination, to nodes `<prefix><combo>`."""
    return [c(text, prefix + key, requires=req, forbids=forb + tuple(forbids), flags=flags) for key, req, forb in COMBOS]


def shy(id, text, *choices):
    return n(id, "Shyka", text, *choices, portrait="Shyka")


def nar(id, text, *choices, portrait="Shyka"):
    return n(id, "Narrator", text, *choices, portrait=portrait)


def king(id, text, *choices):
    """Thaberdine, inline in his own tavern dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


# --- 1. The page (Chapter 3, Council_Shyka): the bargain Shyka can refuse ------------------------------------------------

UNCERTAIN = ('''"And hear this before you say yes, because afterwards we will not repeat it. We will not give you anything '''
             '''whole. Some of it is yours, some of it is spoiled, and some of it belongs to a Drezen that is not yours. You '''
             '''will not know which. That is the price of asking us at all."''')

PICK_TEXT = '''"Three, and you choose." {n}The face is a pawnbroker's, then a midwife's, then nobody's.{/n} "The silver dragon who knelt over you in the festival square, and what she promised you. The square itself: the bunting, the noise, the people wondering why anyone had dragged a wounded fighter into the middle of a party. Or waking in the dark beneath Kenabres, and the two women who found you there. Every Commander has all three. Pick the one you will miss least. You will be wrong about that, too."'''

READ = {
    "p": '''"A silver dragon, kneeling, so close that her breath was warm on my face. Her name was Terendelev. She was the protector of the city. She said: you will recover, I promise you that."''',
    "s": '''"Bunting. Somebody's elbow in my ribs. A voice above me asking why anyone would drag a wounded fighter into the middle of the festival square. Honey cakes, and my own blood, and music that would not stop."''',
    "c": '''"Dark, and dripping. A knight with her hand on her sword, and then off it: you're the one Terendelev healed today, right? And somebody small under the boulders, swearing at the both of us."''',
}
GONE = {
    "p": "the silver dragon's promise in the festival square",
    "s": "the festival square itself, the bunting and the noise",
    "c": "the waking in the caves beneath Kenabres",
}
RECEIPT = {
    "p": "Received of the Commander: one promise, made by a silver dragon in a festival square. Kept by us. Very good condition.",
    "s": "Received of the Commander: one festival square, with bunting, one wounded fighter and a smell of honey cakes. Kept by us.",
    "c": "Received of the Commander: one waking, in the dark under Kenabres, with two women and a quantity of boulders. Kept by us.",
}


def _read_node(key):
    readings = "\n".join(READ[k] for k in key)
    pair = len(key) == 2
    return shy("read_" + key, '''{n}Shyka reaches out, and does not touch you, and speaks in your voice: the voice you had that day, hoarse and young.{/n}
''' + readings + '''
{n}You hear ''' + ("both of them" if pair else "every word") + ''' for the last time. When Shyka closes its mouth you reach for the morning it described and find, where it was, a neat line of handwriting that is not yours.{/n}
"''' + ("Twice. You were dull, but you pay promptly." if pair else "Delicious. A little salty. Mortals always are.") + '''"''',
        c("Continue", "g_punchline"))


def _pick(id, flags):
    return shy(id, PICK_TEXT,
               c('[Give up the dragon\'s promise.]', "read_p", flags=(ACCEPTED, COST_PROMISE) + flags),
               c('[Give up the festival square.]', "read_s", flags=(ACCEPTED, COST_SQUARE) + flags),
               c('[Give up waking in the caves.]', "read_c", flags=(ACCEPTED, COST_CAVES) + flags))


def _second(id, first, others):
    labels = {"p": "[And the dragon's promise.]", "s": "[And the festival square.]", "c": "[And waking in the caves.]"}
    return shy(id, '''"And the second. Not the same one twice; we are absent-minded, not greedy."''',
               *(c(labels[k], "read_" + "".join(sorted(first + k, key="psc".index)),
                   flags=(MEMORY[first], MEMORY[k], ACCEPTED, RAISED)) for k in others))


SCENES.append(scene(PAGE_SCENE, "Shyka's page", "Shyka", 3, "[Offer Shyka something no branch has shown them]", [
    shy("start", '''{n}Shyka is turning something over in their hands. It is a teacup, then a small skull, then a teacup again.{/n} "Something no branch has shown us? How bold. Mortals say that in nine hundred branches out of a thousand, and in all nine hundred they offer us their firstborn, which we have seen, or a song, which we have heard."
{n}A face that is, briefly, a bored clerk's looks up at you.{/n} "Go on, then. We keep forgetfulness for ourselves precisely so that we can still be surprised. Do not waste it."''',
        c('[Make your case] "Show me my own endings. As many as you can spare. Then watch what I do with them. That is the branch you haven\'t seen."',
          check=dict(Skill="CheckDiplomacy", DC=26, Success="pitch_ok", Failure="pitch_fail")),
        c('[Offer Shyka a wager instead] "I\'ll bet you can\'t name what I do after I\'ve seen them."',
          check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="wager_ok", Failure="wager_fail")),
        c("[Leave it.]", abort=True)),
    shy("pitch_ok", '''{n}The face stops changing for almost a whole breath. You suspect it is a compliment.{/n}
"A Trickster who has seen their own endings, and goes on anyway. We see the seeing. We do not see the after. There is a little blind spot, just here," {n}a finger, then a claw, then a quill taps the air beside your temple,{/n} "and we have been itching at it for some time."''',
        c("Continue", "offer1")),
    nar("wager_ok", '''{n}You lay it out the way a chronomancer would, and not the way a gambler would. A branch that exists only after a choice not yet made cannot be read; it can only be waited for. Shyka can see every page of the book but the one you have not turned. Bet against that, and Shyka bets against its own blindness.{/n}''',
        c("Continue", "wager_ok2")),
    shy("wager_ok2", '''"Oh, you nasty little thing." {n}Every face it wears in the next breath is delighted, one after another.{/n} "You are right. We look, and where your next morning should be there is a fog, and the fog is shaped like you. We accept. We shall lose, or we shall not, and either way we shall enjoy finding out. That is more than this timeline has offered us in a while."''',
        c("Continue", "offer1w")),
    shy("pitch_fail", '''"That we have heard." {n}A yawn passes across several faces in turn, like a wave along a crowd.{/n} "In eleven branches. In one of them you even did the hand gesture. You bored us twice, Commander; you will pay us twice. Boredom is the only thing we are ever short of, and we bill for it."''',
        c("Continue", "offer2")),
    shy("wager_fail", '''"A wager! Against us! In our own hall!" {n}The face is a child's, appalled and thrilled.{/n} "Then we name it, at once: you will look at the page, and you will make a plan, and the plan will be cold, and you will tell no one. There. Named. You bet against us with a coin we minted."
{n}The child is an old man now, and wagging a finger.{/n} "Insults are billed double. You will pay us twice."''',
        c("Continue", "offer2")),
    shy("offer1", '''"Here is the bargain. We show you your own other endings: a page of them, not the archive. The archive kills mortals with boredom, and we would miss you. For it, you give us one memory. Not any memory: one that every Commander has, in every branch, so that we can taste from the inside a thing we have only ever watched from the outside."
''' + UNCERTAIN,
        c('[Accept] "Done. Name the memories."', "m1_pick"),
        c('[Decline] "Not for that."', abort=True)),
    shy("offer1w", '''"Here is the bargain. We show you your own other endings: a page of them, not the archive. For it, one memory, one that every Commander has, so that we can taste from the inside a thing we have only ever watched. And the wager stands. We will settle it when we see you next, which we already have, and have not."
''' + UNCERTAIN,
        c('[Accept] "Done. Name the memories."', "m1_pick_w"),
        c('[Decline] "Not for that."', abort=True)),
    shy("offer2", '''"Two memories, for the same page." {n}The face is a pawnbroker's, and it is enjoying itself.{/n} "Or, since we are generous in this branch: one memory, and a wager left on our table, unsettled. We wager that we can name what you will do after the page. We will tell you when we have won it. You will not like how we tell you."
''' + UNCERTAIN,
        c('[Pay twice] "Two, then. Name them."', "m2_first"),
        c('[Take the counteroffer] "One memory. Leave your wager on the table."', "m1_pick_c"),
        c('[Decline] "Not for that."', abort=True)),
    _pick("m1_pick", ()),
    _pick("m1_pick_w", (WAGER,)),
    _pick("m1_pick_c", (COUNTER,)),
    shy("m2_first", PICK_TEXT.replace("Pick the one you will miss least.", "Pick the first of two.").replace(
        " You will be wrong about that, too.", " There is no going back once we have it in our mouth."),
        c('[Give up the dragon\'s promise.]', "m2_second_p"),
        c('[Give up the festival square.]', "m2_second_s"),
        c('[Give up waking in the caves.]', "m2_second_c")),
    _second("m2_second_p", "p", ("s", "c")),
    _second("m2_second_s", "s", ("p", "c")),
    _second("m2_second_c", "c", ("p", "s")),
    *(_read_node(key) for key, _, _ in COMBOS),
    # Commander sacrifice: GrandFinal/Answer_0011 10e6b2a8c754dae4b81e55ad6d0918b2.
    # Answer_0055 91c5eca80c8779c4a8bd5754f5533cad sacrifices Areelu; it is not this glimpse.
    nar("g_punchline", '''{n}The page is not paper. It is the inside of your own eyelids, and Shyka turns it.{/n}
{n}Threshold. You know it the way you know a room from a dream: the rift, the light, a sound like laughter coming up from underneath the world. A Commander who looks very like you is laughing at something enormous, and the joke lands, and it lands on the Commander, who goes down and does not get up. It is raining. The rain is wrong. It does not rain there; Shyka has put the rain in, the way a forger leaves one letter crooked so that the forgery can be found.{/n}
"That one is yours," {n}says Shyka.{/n} "Mostly."''',
        c("Continue", "g_shyka")),
    nar("g_shyka", '''{n}A wedding: bells, a long table, flowers nobody would grow in Mendev. The face at the head of the table is yours, and it is saying "we". Everyone is smiling, and every smile is the same smile. There was no wedding. Shyka has dressed something else in white, so that you cannot look at it straight.{/n}
"Also yours. Someone will ask you about it quite soon. Try to look surprised."''',
        c("Continue", "g_funeral")),
    nar("g_funeral", '''{n}A cathedral, full to the doors. Drezen drinking to the Commander's death: a fine funeral, the kind you would have loved, with a fat man on a pew making the toast and the tankards going round the nave. Every chair that matters is empty. It ought to be a tavern; Shyka has moved it into a cathedral and forgotten to move the tankards.{/n}
"Not an ending, that one. A joke people will tell about you. We heard it in so many branches that we began to believe it."''',
        c("Continue", "g_gate")),
    nar("g_gate", '''{n}Drezen's east gate, burning, on the night the wind turns. Sparks across the lower town, men running with buckets, a bell. It is vivid and very particular, and something about it is wrong in every part at once, the way a word stops meaning anything if you say it often enough.{/n}
"And that one," {n}says Shyka, and the face is a child's again, and delighted,{/n} "we will not explain. Close the page. It will leak a little afterwards; pages do. Crumbs of other people's branches stick to it, and fall off at odd hours. They will be wrong. Do not trust them. Do not throw them away."
{n}You close it. Three endings and a fire, and no name in any of them but yours. Before you are out of the hall you have decided, coldly and in some detail, that you will not have any of them.{/n}''',
        c("[Close the page.]", flags=(GATE_FIRE,))),
], requires=("trickster",), forbids=COUNCIL_GONE + (ACCEPTED,), last=5, optional=True, Relationship=REL, Chapters=[3, 5],
    AnswerLists=[SHYKA_LIST], NativeReturnCue=SHYKA_BACK, EntryMythic="PlayerIsTrickster"))


# --- 2. The memory (a rest-delivered memory page; §2.3, §7.1) ------------------------------------------------------------

def _receipt(key):
    lines = "\n".join("{n}" + RECEIPT[k] + "{/n}" for k in key)
    return nar("r_" + key, '''{n}It happens as you are falling asleep, the way the tongue finds a missing tooth. You reach for the morning in Kenabres, without meaning to, and it is not there. Not dark, not blurred: replaced. Where it was there is a line of handwriting, neat and looping, in an ink that changes colour while you read it.{/n}
''' + lines + '''
{n}Signed with an S, and a small drawing of a teacup, or a skull.{/n}
{n}You still know the facts. Anyone could tell you the facts; several people already have. But they are the facts of a story someone once told you about yourself, and you cannot get behind them any more.{/n}''',
        c("[Let it go.]"))


SCENES.append(scene(MEMORY_SCENE, "Shyka's handwriting", "Shyka", 3, "", [
    nar("start", '''{n}Night, and a cot, and the ordinary weight of a day.{/n}''', *combo_choices("r_")),
    *(_receipt(key) for key, _, _ in COMBOS),
], requires=("trickster.ever", ACCEPTED), forbids=(MEMORY_TOLD,), delay=1, last=5, optional=True, Relationship=REL,
    Remote=True, Kind="memory", Chapters=[3, 4, 5], RequiresAnyGroups=[list(COSTS)]))


# --- 3. The misstep (§2.4, §7.4): one scene on two native tavern lists, in Chapters 3 and 5 --------------------------------

SCENES.append(scene(WATCH_SCENE, "A royal watch", "Thaberdine", 3,
    '"How many of your drinking companions could stand a night watch?"', [
    king("ask", '''"A watch! My court!" {n}Thaberdine looks at you over his mug with real alarm.{/n} "My court stands up very badly after dark, Commander, that's the whole point of a court. Where? And don't say the cellar. Everybody says the cellar."''',
        c('[Post his drunks at the east gate] "The east gate. Every night until I say otherwise. If the wind turns and you see one spark, ring every bell in the lower town."',
          "posted", crusade=("Favors", -50)),
        c('[Never mind] "Forget I asked."', abort=True)),
    king("posted", '''"The east gate! Every night!" {n}He announces it to the room, which cheers without knowing why.{/n} "A royal watch, against a royal fire that hasn't happened. I like it. Very forward-looking. The beer goes on your tab, mind; watching is thirsty work. And when nothing burns, I'll tell everyone it was us that stopped it."
{n}By the next morning the soldiers on the east gate have heard that the Commander has posted the town's drunks on their gate, and they are telling anyone who will listen what that says about their Commander's trust in them.{/n}''',
        c("Continue", flags=(GATE_WATCH,))),
], requires=("trickster.now", GATE_FIRE), forbids=(GATE_WATCH, "fool_king.gone"), last=5, optional=True, Relationship=REL,
    Chapters=[3, 5], AnswerLists=[KING_C3, KING_C5], ReturnToList=True,
    ReturnText="{n}Thaberdine has already found something else to toast.{/n}"))


# --- 4. The Chapter 5 payoff (§2.7), inline on Shyka's offer -----------------------------------------------------------

COST_LINE = {
    "p": '''"You do not remember what the dragon promised you. We do. She meant it."''',
    "s": '''"You do not remember the festival. We do. The honey cakes were stale."''',
    "c": '''"You do not remember waking in the dark. We do. You were very frightened, and you hid it badly."''',
}


def _late_receipt(key):
    lines = " ".join(RECEIPT[k] for k in key)
    return shy("lr_" + key, '''"Before anything else, our receipt. You never rested long enough to find it, so we will read it to you." {n}Shyka recites, in the dry voice of a clerk:{/n} "''' + lines + '''"
{n}And you reach for the morning in Kenabres and find that Shyka is right: it is not there. Only the receipt, in Shyka's voice, where it was.{/n}''',
        c("Continue", "gate"))


def _cost_node(key):
    text = "\n".join(COST_LINE[k] for k in key)
    if len(key) == 2:
        text += '\n"You paid twice. We have not forgotten. We have not forgotten either of them."'
    return shy("cost_" + key, text,
               c("Continue", "won_yours", requires=(WAGER,)),
               c("Continue", "won_ours", requires=(COUNTER,)),
               c("Continue", "ask", forbids=(WAGER, COUNTER)))


SCENES.append(scene(OFFER_SCENE, "The page, settled", "Shyka", 5, '"Before you ask me anything: the page."', [
    shy("start", '''{n}Shyka lowers the glowing diamond and looks at you along it, as a jeweller looks at a flaw.{/n} "The page. Yes. We wondered when you would ask. We wondered it in several places at once."''',
        *(c("Continue", "lr_" + key, requires=req, forbids=forb + (MEMORY_SCENE, MEMORY_TOLD), flags=(MEMORY_TOLD,))
          for key, req, forb in COMBOS),
        c("Continue", "gate", requires=(MEMORY_SCENE,)),
        c("Continue", "gate", requires=(MEMORY_TOLD,), forbids=(MEMORY_SCENE,))),
    *(_late_receipt(key) for key, _, _ in COMBOS),
    shy("gate", '''"The gate never burned. That was a Drezen that is not yours. We told you some of it would not be."''',
        c("Continue", "gate_watched", requires=(GATE_WATCH,)),
        *combo_choices("cost_", forbids=(GATE_WATCH,))),
    shy("gate_watched", '''"Your drunks stood on the east gate for a week. Two of them got married. One of them is still up there; we think he has forgotten why. We are rather fond of him. You paid for a fire that belonged to someone else, and you paid in your own soldiers' good opinion. That is what a page from another world costs, when you believe it."''',
        *combo_choices("cost_")),
    *(_cost_node(key) for key, _, _ in COMBOS),
    shy("won_yours", '''"And your wager." {n}The faces flicker, and settle on one that looks almost sulky.{/n} "We still cannot name what you did after the page. We have looked. There is a fog, and it is shaped like you, and it has been doing things in Drezen and in the Abyss that we did not see coming. We concede. It is the most fun we have had in a century, or several."''',
        c("Continue", "ask")),
    shy("won_ours", '''"And our wager, which you left on our table." {n}The face is a pawnbroker's again, and very pleased.{/n} "We said we could name what you would do after the page. Here you are: in front of the second glimpse, with the choice in your hand, exactly where we said. We win. Do not argue. It spoils it."''',
        c("Continue", "ask")),
    shy("ask", '''"Soon we will ask you a question. You saw it on the page, dressed up as a wedding. When we ask it, you may say no." {n}A small shrug, passed from shoulder to shoulder of several bodies.{/n} "The page was never a map. We would know. We drew it."''',
        c("Continue", "count", requires=(KAYLESSA_PRICE,)),
        c("[Go on.]", forbids=(KAYLESSA_PRICE,))),
    shy("count", '''"You have taken from us twice now: once a branch, once a page. We are keeping count, little key. So is the other you."''',
        c("[Go on.]")),
], requires=("trickster.now", ACCEPTED), forbids=("shyka.gone",), last=5, optional=True, Relationship=REL, Chapters=[5],
    AnswerLists=[OFFER_LIST], NativeReturnCue=OFFER_BACK, EntryMythic="PlayerIsTrickster", RequiresAnyGroups=[list(COSTS)]))


# --- 5. The witnesses (§2.3): the people who were there notice the gap. Reactions only; nothing is set. ---------------------

REMEMBERED = [[MEMORY_SCENE, MEMORY_TOLD]]   # one group: the memory has been found missing (the page, or Shyka's reading)

SCENES.append(reaction("Anevia", P + "noticed.anevia", ("trickster.ever", ACCEPTED, COST_CAVES),
    '''{n}Anevia is halfway through a story when you sit down, and she doesn't stop for you.{/n} "...and that was you, the first time I ever saw you, I swear it. Down in the caves, grey as a fish, and Seelah with her hand on her sword because she thought you were a cultist come to finish me off. You remember her face? Gods, her face."
{n}She waits for you to laugh. You can't. There is nothing there to laugh at, only a neat line of someone else's handwriting. She sees it; Anevia always sees it.{/n}
"...You don't remember." {n}It isn't a question.{/n} "Huh. Well. I do. I was under a rock at the time, mind, so I had a good long while to look at you." {n}She lets it go, the way she lets go of things she means to come back to.{/n}''',
    answer_list=ANEVIA_HUB, relationship=REL, forbids=("anevia_dead", "anevia_gone"), chapter=3, last=5, delay=12,
    entry='"Tell me about Kenabres. The bit with me in it."', portrait="Anevia", RequiresAnyGroups=REMEMBERED,
    ForbidOverrides={"anevia_dead": "anevia.trickster.returned", "anevia_gone": "anevia.trickster.returned"}))

SCENES.append(reaction("Seelah", P + "noticed.seelah", ("trickster.ever", ACCEPTED, COST_CAVES),
    '''{n}Seelah is oiling her sword, and she grins at you over it.{/n} "Do you know I nearly drew this on you, in the caves? You came out of the dark looking like something that eats people. Then I got a proper look at your face and thought: oh, that's the one Terendelev healed. And then you helped me get Anevia out from under all that rock, and I thought, well, that's that, then."
{n}She waits. You have nothing to give her. Where the caves were there is only Shyka's neat handwriting.{/n}
"...You don't remember. Do you." {n}She puts the sword down, carefully, the way she puts down anything she might want again.{/n} "That's all right. I remember enough for both of us. I'll tell it to you some other time, the way I tell it. It's better my way. I'm in it more."''',
    answer_list=SEELAH_HUB, relationship=REL, forbids=("seelah_dead", "seelah_gone"), chapter=3, last=5, delay=12,
    entry='"You found me in the caves. What did you think?"', portrait="Seelah", RequiresAnyGroups=REMEMBERED,
    ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"}))

_toast = reaction("Thaberdine", P + "noticed.king", ("trickster.ever", ACCEPTED),
    '''"The night you came to Kenabres!" {n}Thaberdine slaps the table and slops his beer.{/n} "I was there, you know. In the festival square. I stood on a barrel and gave a toast to the wounded hero, the best toast of my life; there wasn't a dry eye in the square. You remember it. You must. You were right there, bleeding on the bunting."
{n}You weren't, or you were, or he wasn't. You do not know. You cannot contradict a word of it, and he watches you not contradicting it with enormous satisfaction.{/n}
"There! The hero remembers! A royal toast is never forgotten."''',
    answer_list=KING_C3, relationship=REL, forbids=("fool_king.gone",), chapter=3, last=5, delay=12, speaker="conversant",
    entry='"Thaberdine. Were you ever in Kenabres?"', RequiresAnyGroups=REMEMBERED)
_toast["AnswerLists"] = [KING_C3, KING_C5]
_toast["Chapters"] = [3, 5]
_toast["ReturnToList"] = True
_toast["ReturnText"] = "{n}Thaberdine is still telling the room about his toast.{/n}"
SCENES.append(_toast)


# --- 6. Last Call (§2.7): Areelu's report, one paragraph per paid combination, and Shyka at the table ----------------------

def _report(key):
    gone = " and ".join(GONE[k] for k in key)
    return p("{n}" + ('''I record one more irregularity, because I am thorough. In the third year of the war the Commander bought a page of {mf|his|her} own other endings from Shyka the Many, looked at every one of them, and decided, coldly, not to have any of them. {mf|He|She} paid for the page with a morning in Kenabres: ''' + gone + '''. I have that morning in my notes, in some detail. The Commander does not have it anywhere.''') + "{/n}",
             requires=("trickster.ever", ACCEPTED) + tuple(MEMORY[k] for k in key) + ((RAISED,) if len(key) == 2 else ()),
             forbids=(() if len(key) == 2 else (RAISED,)))


def _unread(key):
    lines = " ".join(RECEIPT[k] for k in key)
    return p("{n}" + ('''Among the Commander's effects I found, folded very small, a receipt in a hand that was not {mf|his|hers}: "''' + lines + '''" It had never been opened. I read it aloud to {mf|him|her}. {mf|He|She} listened as one listens to an account of someone else's debts, and could not tell me what had been bought.''') + "{/n}",
             requires=("trickster.ever", ACCEPTED) + tuple(MEMORY[k] for k in key) + ((RAISED,) if len(key) == 2 else ()),
             forbids=(MEMORY_SCENE, MEMORY_TOLD) + (() if len(key) == 2 else (RAISED,)))


# §7.3: the unread receipt comes first (no rest and no Chapter 5 line ever delivered it), then the report, then Shyka.
LASTCALL_PARAGRAPHS = tuple(_unread(key) for key, _, _ in COMBOS) + tuple(_report(key) for key, _, _ in COMBOS) + (
    p('''{n}Shyka, whose essence went into the Wound with the rest of the Council's, came to the Commander's table afterwards wearing the Commander's own face, and recited the lost morning aloud, word for word, as a story about somebody else. The Commander listened politely, and laughed in the right places, and asked at the end who it had happened to. I record the question. I do not record the answer, because Shyka did not give one.{/n}''',
      requires=("trickster.now", ACCEPTED, SHYKA_ESSENCE)),
)
LASTCALL_PAGES = ("trickster.lastcall.page.interrupted", "trickster.lastcall.page.heroic")


# --- 7. The Ledger's journal lines (§4): "What I no longer remember", never settled ---------------------------------------

JOURNAL = [dict(Id="foresight.forgot." + k, Title="What I no longer remember",
                Description=("I paid Shyka the Many for a page of my own other endings with " + GONE[k] + ". I know it "
                             "happened. People have told me. I cannot get behind their telling to the thing itself."),
                OpenWhen=[[ACCEPTED, MEMORY[k]]], SettledWhen=[])
           for k in ("p", "s", "c")]


# --- 8. The echoes (§2.4a, §2.9): the page's residue, as optional appended beats in routes, on a strict budget ------------------------------

ECHOES = []
ECHO_ENTRIES = set()
# 12 §2.9 Echo discipline: the mod-wide budget and the registry axes. Allocation is the coordinator's (06 "Echo slots").
ECHO_CAP_TOTAL, ECHO_CAP_ROUTE, ECHO_CAP_CHAPTER = 8, 1, 2
# Mirror of 06-ROUTE-REGISTRY "Echo slots": route -> host scene of the ALLOCATED slot. A registered echo whose route and host
# are not here stays inactive (kept in ECHOES as a proposal, absent from the export). Only the coordinator adds rows,
# with a documented, unresolved believability problem that existing canon clues cannot solve, never merely for colour.
ALLOCATED = {"wenduag": "wenduag.trickster.echo.abyss.prepare"}
SENSES = ("sight", "sound", "smell", "taste", "touch")


def variant(text, requires=(), forbids=()):
    """One wording of an echo. The variants of one echo must be mutually exclusive (a key one requires, another forbids)."""
    return dict(Text=text.strip(), Requires=tuple(requires), Forbids=tuple(forbids))


def _echo_axes(sense, misstep):
    """Compare sensory sets and missteps without case, spacing or punctuation differences."""
    senses = re.findall(r"[^\W_]+", sense.casefold())
    mechanic = re.findall(r"[^\W_]+", misstep.casefold())
    return tuple(sorted(set(senses))), tuple(mechanic)


def echo(rel, host, node, entry, *variants, sense, wrong, misstep, cost, existing=False):
    """Register one route echo (12 §2.4a, §2.9): an answer `entry` (an ACTION, never speech about foresight), appended LAST
    to node `node` of scene `host`, selectable only on a Trickster run where the page was taken (foresight.page_taken). It
    leads to a one-node beat in the chosen variant's text, whose choices are copies of the host node's own choices: the
    page opens the road and never walks it, so every check and cost of the host stays.

    `sense` (one of SENSES, or "a + b"), `wrong` (the wrong detail) and `misstep` (the mechanic of the misreading) are the
    registry axes of 06 "Echo slots"; no two echoes share a sense and a misstep. `cost` is the misreading's real price, a
    crusade resource change on the entry answer, e.g. ("Finances", -100). Enforced at integrate(): at most 8 echoes
    mod-wide, 1 per route, 2 per chapter; unique entries; mutually exclusive variants. Injected echoes never set a flag.
    existing=True registers an already-authored scene without adding choices, checks or costs."""
    if not variants:
        raise ValueError("echo %s/%s: no variants" % (host, node))
    if entry in ECHO_ENTRIES:
        raise ValueError("echo entry reused (sameness): " + entry)
    senses, mechanic = _echo_axes(sense, misstep)
    if not senses or not set(senses).issubset(SENSES) or not wrong.strip() or not mechanic:
        raise ValueError("echo %s: sense, wrong detail and misstep are required (12 §2.9)" % host)
    if any(_echo_axes(e["sense"], e["misstep"]) == (senses, mechanic) for e in ECHOES):
        raise ValueError("echo %s repeats a sense and misstep (12 §2.9)" % host)
    ECHO_ENTRIES.add(entry)
    ECHOES.append(dict(rel=rel, host=host, node=node, entry=entry, variants=list(variants), sense=sense, wrong=wrong,
                       misstep=misstep, cost=cost, existing=existing))


def _chapters(s):
    return list(s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"] + 1))


def _exclusive(a, b):
    return bool(set(a["Requires"]) & set(b["Forbids"])) or bool(set(b["Requires"]) & set(a["Forbids"]))


def active_echoes():
    return [e for e in ECHOES if ALLOCATED.get(e["rel"]) == e["host"]]


def integrate_echoes(payload):
    axes = set()
    for e in ECHOES:
        key = _echo_axes(e["sense"], e["misstep"])
        if key in axes:
            raise ValueError("echo %s repeats a sense and misstep (12 §2.9)" % e["host"])
        axes.add(key)
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    active = [e for e in active_echoes() if not e["existing"] or e["host"] in scenes]
    if len(active) > ECHO_CAP_TOTAL:
        raise ValueError("12 §2.9: %d route echoes, the cap is %d" % (len(active), ECHO_CAP_TOTAL))
    per_route, per_chapter = {}, {}
    for e in active:
        target = scenes[e["host"]]
        if (target.get("Relationship") or "tirabade") != e["rel"]:
            raise ValueError("echo %s: host belongs to %s" % (e["host"], target.get("Relationship")))
        per_route.setdefault(e["rel"], []).append(e["host"])
        if len(per_route[e["rel"]]) > ECHO_CAP_ROUTE:
            raise ValueError("12 §2.9: more than one echo for %s: %s" % (e["rel"], per_route[e["rel"]]))
        for ch in _chapters(target):
            per_chapter.setdefault(ch, []).append(e["host"])
            if len(per_chapter[ch]) > ECHO_CAP_CHAPTER:
                raise ValueError("12 §2.9: more than two echoes in chapter %d: %s" % (ch, per_chapter[ch]))
        for a in range(len(e["variants"])):
            for b in range(a + 1, len(e["variants"])):
                if not _exclusive(e["variants"][a], e["variants"][b]):
                    raise ValueError("echo %s: variants %d and %d can both show" % (e["host"], a, b))
        if e["existing"]:
            if target["Entry"] != e["entry"] or not {"trickster.now", PAGE_TAKEN}.issubset(target["Requires"]):
                raise ValueError("echo %s: existing entry needs the current path and paid page" % e["host"])
            host = next(nd for nd in target["Nodes"] if nd["Id"] == e["node"])
            if len(e["variants"]) != 1 or host["Text"] != e["variants"][0]["Text"]:
                raise ValueError("echo %s: existing registration must match its authored beat" % e["host"])
            choices = [ch for nd in target["Nodes"] for ch in nd["Choices"]]
            if not any(ch.get("Crusade") == dict(Resource=e["cost"][0], Amount=e["cost"][1]) for ch in choices):
                raise ValueError("echo %s: existing misstep cost is missing" % e["host"])
            for choice in choices:
                choice["Requires"] = list(dict.fromkeys(choice["Requires"] + ["trickster.now", PAGE_TAKEN]))
            continue
        host = next(nd for nd in target["Nodes"] if nd["Id"] == e["node"])
        if any(str(ch.get("Next") or "").startswith("echo.") for ch in host["Choices"]):
            raise ValueError("echo %s/%s: the node already carries an echo" % (e["host"], e["node"]))
        original = copy.deepcopy(host["Choices"])
        for v, var in enumerate(e["variants"]):
            node_id = "echo.%d" % v
            if any(nd["Id"] == node_id for nd in target["Nodes"]):
                raise ValueError("echo %s: node id %s taken" % (e["host"], node_id))
            host["Choices"].append(c(e["entry"], node_id, requires=("trickster.now", PAGE_TAKEN) + var["Requires"],
                                     forbids=var["Forbids"], crusade=e["cost"]))
            target["Nodes"].append(dict(Id=node_id, Speaker="Narrator", Text=var["Text"], Choices=copy.deepcopy(original),
                                        Portrait=host.get("Portrait", "")))


GAPS = []


def gap(rel, host, vias, replaces, text, gone, choices=None):
    """A memory-gap variant (12 §2.4a): a route scene that relives one of the three Prologue mornings in the Commander's own
    senses must not contradict a memory sold to Shyka. Each (node, index) in `vias` is a choice that leads to node
    `replaces`; it is gated off (Forbids `gone`, index kept) and a copy is appended last that Requires `gone` and leads to
    a new node `gap.<replaces>` with `text`, whose choices are `choices` or copies of the replaced node's. Nothing is set;
    the scene rejoins its own path. `gone` is GONE_SQUARE or GONE_CAVES."""
    if gone not in (GONE_SQUARE, GONE_CAVES):
        raise ValueError("gap %s: unknown memory key %s" % (host, gone))
    GAPS.append(dict(rel=rel, host=host, vias=list(vias), replaces=replaces, text=text.strip(), gone=gone,
                     choices=None if choices is None else list(choices)))


def integrate_gaps(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for g in GAPS:
        target = scenes[g["host"]]
        if (target.get("Relationship") or "tirabade") != g["rel"]:
            raise ValueError("gap %s: host belongs to %s" % (g["host"], target.get("Relationship")))
        nodes = {nd["Id"]: nd for nd in target["Nodes"]}
        new_id = "gap." + g["replaces"]
        if new_id in nodes:
            raise ValueError("gap %s: node %s taken" % (g["host"], new_id))
        replaced = nodes[g["replaces"]]
        for node_id, index in g["vias"]:
            choice = nodes[node_id]["Choices"][index]
            if choice.get("Next") != g["replaces"]:
                raise ValueError("gap %s: %s[%d] does not lead to %s" % (g["host"], node_id, index, g["replaces"]))
            alt = copy.deepcopy(choice)
            choice["Forbids"] = list(dict.fromkeys(list(choice["Forbids"]) + [g["gone"]]))
            alt["Next"] = new_id
            alt["Requires"] = list(dict.fromkeys(list(alt["Requires"]) + ["trickster.ever", g["gone"]]))
            nodes[node_id]["Choices"].append(alt)
        target["Nodes"].append(dict(Id=new_id, Speaker=replaced.get("Speaker", "Narrator"), Text=g["text"],
                                    Choices=copy.deepcopy(g["choices"] or replaced["Choices"]),
                                    Portrait=replaced.get("Portrait", "")))


# --- Registration -----------------------------------------------------------------------------------------------------------

DERIVED = {PAGE_TAKEN: [["trickster.now", ACCEPTED]],
           GATE_BELIEVED: [["trickster.now", GATE_WATCH]],
           GONE_SQUARE: [[ACCEPTED, COST_PROMISE, "trickster.ever"], [ACCEPTED, COST_SQUARE, "trickster.ever"]],
           GONE_CAVES: [[ACCEPTED, COST_CAVES, "trickster.ever"]]}
PUBLIC = (PAGE_TAKEN, GATE_BELIEVED, GONE_SQUARE, GONE_CAVES)
LATCHES = {SHYKA_ESSENCE: [SIPHON_SHYKA]}
# Every scene that may read trickster.foresight.* (12 §2.8, Foresight_NeverGates). Echo choices read only PAGE_TAKEN.
READERS = {PAGE_SCENE, MEMORY_SCENE, WATCH_SCENE, OFFER_SCENE, P + "noticed.anevia", P + "noticed.seelah", P + "noticed.king",
           *LASTCALL_PAGES}
# Gated consumers outside this module: scene id -> the public key required by the scene or its paragraphs.
# Exported as acceptance metadata; tests/ForesightTests.cs checks each with/without the page and after path loss.
# Echo and gap choices are consumers by construction (registered through echo()/gap()).
CONSUMERS = {}
# Path fit (v1): every scene here is T (the page is Trickster-only; the Council is the Trickster's).
PATH_FIT = {s["Id"]: "T" for s in SCENES}


def integrate(payload):
    """After Last Call (its pages and its Ledger quest) and after every route (the echo hosts)."""
    payload["Relationships"][REL] = copy.deepcopy(RELATIONSHIP)
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
    for key, sources in LATCHES.items():
        payload.setdefault("Latches", {})[key] = list(sources)
    pages = {s["Id"]: s for s in payload["Scenes"] if s["Id"] in LASTCALL_PAGES}
    for page_id in LASTCALL_PAGES:
        node = pages[page_id]["Nodes"][0]
        node.setdefault("Paragraphs", []).extend(copy.deepcopy(list(LASTCALL_PARAGRAPHS)))
    payload["Relationships"]["lastcall"].setdefault("JournalEntries", []).extend(copy.deepcopy(JOURNAL))
    integrate_echoes(payload)
    integrate_gaps(payload)
    # Later integrations also register consumers; serialize the completed registry.
    payload["ForesightConsumers"] = CONSUMERS
