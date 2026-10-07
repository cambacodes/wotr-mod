"""Nenio on the Trickster path: "A name for a name" (Writer/handoffs/trickster/nenio.md for the canon research; the binding
plan is 11-ROSTER-PLAN-2 §2, the Nenio block and its build sheet, rewritten after the Astra design review r3).

Canon: a kitsune scholar, "physically, I'm approximately four thousand years old" (CompanionDialogues/Nenio/Cue_0422),
future author of the Encyclopedia Golarionnica, "one hundred volumes, one thousand pages each" (Cue_0106), of which she has
written "no more than one percent" (Cue_0109). Her follower is to walk behind her "writing down my deepest thoughts" (Cue_0008).
She forgets on purpose whatever she ranks irrelevant, the Commander's name included: "On the grand scale of world history,
your name is irrelevant" (Cue_0052); "The secret is to stop thinking about the thing you want to forget" (Cue_0066). Her
friendship list has a point five, "friends sometimes copulate" (Answer_0353), and ends with friendship "the most foolish of all
occupations" (Cue_0372). In the Enigma (Ch5) Areshkagal calls her "the anomaly", a Tian Xia cultist's recreated body
(AreshkaConfrontation/Cue_0017, Cue_0018); in FoxMyself she weighs two truths (Cue_0009) and needs two arguments: the first
ends in the ShowOnce Cue_0019 ("the risk... is too high"), the second in Cue_0020 ("I will accept your point of view as the
truth. After all, I like it more than the other one"). Her quest's trap asked "Who are you?", and "merely stating my name
failed to satisfy it" (FoxReveal/Cue_0044). She thanks the Commander by name once, at the end (FoxMyself/Cue_0032), and later
denies it: "0.01%" (Cue_0406); a scientist must be above "irrational sentiment" (Cue_0407).

The device (earned, and hers): in FoxMyself the Commander poses a riddle in the Sphinx's own statue idiom (FoxReveal/Cue_0055)
whose only answer is her name, and names the stake aloud: a name for a name. It is the Commander's gamble, never a rule of the
Sphinx. If she answers, she keeps hers and files the Commander's where not even she can reach it; the answer counts as one of
her two native arguments. Told the answer, she declines ("The absence of an answer is an answer too", FoxReveal/Cue_0002).
Cost: she never has the Commander's name again (cost.name_filed). Loss worlds (build sheet): the Sphinx's grey servant reclaims
a dead vessel for her trunks of unpublished notes; recreates a Ch1-killed one, without her memory; a sent-away or
kicked-out Nenio comes back to correct the record, on probation.
The commit is a question she did not mean to ask, answered as a hypothesis and tested by her own canon method: one night of
deliberate forgetting. She decides. The Commander's tampering voids the test; a confession earns a replication; a denial ends it.
The spine (the dictation sessions, the Abyss, page one) is nenio_folios.
"""
from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "nenio"
P = "nenio.trickster."
F = "nenio.folio."
UNIT = "1b893f7cf2b150e4f8bc2b3c389ba71d"          # Nenio_Companion (her hub, and the Revivals unit)
COPY_UNIT = "49e6676f68337114985a22bd548a8a4d"     # Nenio_NPC_Level1 (the presence copy)
HUB = "1ab909cc3a6194840b1475b99547c263"           # CompanionDialogues/Nenio/AnswersList_0015
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
EXOTIC = "bad9f602b81a80047ac470b01ebe65a9"        # ExoticCapitalTrader (Aranka's copy stands in front of him at 2.5 m)
JEWELER = "bc1093231b1577a4485a730c29595195"       # JewelerCapitalTrader (arcade fallback)
FOX_LIST = "d0eed6e4ca8dd5f478810c3ee59228de"      # c5/AreshkagalTomb/FoxMyself/AnswersList_0004
FOX_RETURN = "cfae2454cb77dc8479ff0b044158e067"    # FoxMyself/Cue_0002 "It is pointless to doubt the axiom..." (clean, back to 0004)
FOX_ONE = "357224f06cf28804294c737124e66c29"       # FoxMyself/Cue_0019 "Yes. I wish..." (the first argument; ShowOnce)
FOX_TWO = "e7831690d3ccf5f4594e842cb7b8af9e"       # FoxMyself/Cue_0020 "I will accept your point of view as the truth..."
SOSIEL_HUB = "129b55b8b5d50974f84f7c607d894fd0"    # CompanionDialogues/Sosiel/AnswersList_0002
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"    # NPC_Common/Anevia/AnswersList_0003

STARTED = "nenio.started"
CLOSED = "nenio.closed"
COMMITTED = "nenio.committed"
# Native state (trickster_world BINDINGS, and the three keys bound in integrate below).
ASKED_TO_LEAVE = "nenio.asked_to_leave"            # FoxMyself/Answer_0006 "Let's leave this place, Nenio."
FOX_ARGUED = "nenio.fox_argued"                    # SeenCues FoxMyself/Cue_0019 (her first argument already made)
ASKED_FORGETTING = "nenio.asked_forgetting"        # SelectedAnswers CompanionDialogues/Nenio/Answer_0061
ASKED_GIFT = "nenio.asked_gift"                    # SelectedAnswers FoxMyself/Answer_0012
FOX_REVEALED = "nenio.fox_revealed"                # SeenCues FoxReveal/Cue_0031 "I am a kitsune."
FRIEND_DONE = "nenio.friendship_concluded"         # SeenCues Cue_0372
DEAD = "nenio.dead"
KILLED = "nenio.killed_by_commander"
SENT_AWAY = "nenio.sent_away"
KICKED_OUT = "nenio.kicked_out"
DISSOLVED = "nenio.dissolved"                      # FoxMyself/Cue_0003: the real loss; no override, ever
DEAD_L = "nenio.dead.latched"
KILLED_L = "nenio.killed.latched"
AWAY_L = "nenio.away.latched"
# The device.
RIDDLE_DONE = P + "riddle_done"
RIDDLE_DECLINED = P + "riddle_declined"            # only this wager closes; never her no to the romance
NAME_FILED = P + "cost.name_filed"
NAME_GONE = P + "name_gone"                        # Derived: the completed filing receipt only
NAME_STAKED = P + "name_staked"                    # the riddle answered: the stake taken (filed after her native farewell)
WHO_SILENT = F + "who_are_you.silent"              # the Commander told her of refusing the void (not a loophole)
SILENCE_CLAUSE = P + "cost.silence_clause"        # the Sphinx's axiom written into the debt's terms at the bargain (Sol r3 TRK)
ENIGMA_RESOLVED = "nenio.enigma_resolved"          # SeenCues FoxMyself/Cue_0032 (she thanks the Commander by name)
# The answer owed to the Sphinx, collected in Chapter 6 (Sol TRK).
DEBT_PAID = P + "debt.paid"                        # the true answer given; the Sphinx keeps it
DEBT_EVADED = P + "debt.evaded"                    # paid in the Sphinx's own coin: the absence of an answer
DEBT_DEFAULTED = P + "debt.defaulted"              # refused: volume one taken instead
DEBT_SETTLED = (DEBT_PAID, DEBT_EVADED, DEBT_DEFAULTED)
RIDDLE_REBUILT = P + "riddle_rebuilt"
# Loss worlds.
RETURNED = P + "returned"
LET_REST = P + "let_rest"
BODY_KEPT = P + "body_kept"                        # Derived: her retained unit can be raised (revive.nenio.available)
MANUSCRIPT = P + "cost.manuscript_surrendered"
OWES = P + "cost.owes_an_answer"
RECREATED = P + "cost.recreated"
UNREMEMBERED = P + "cost.unremembered"
PRIMED_AWAY = P + "primed_away"
DEMOTED = P + "cost.demoted"
TOLD_THEFT = P + "cost.confessed"
THIEF_HUNTED = P + "cost.thief_hunted"
VISITOR = P + "visitor"                            # Derived (trickster_world): recreated, unremembered, or primed_away
PRESENCE = "nenio.presence"
ARCADE = "nenio.presence.arcade"
FAILED = "nenio.presence.failed"                   # runtime: the trader's awning is not in the capital
# The commit.
SCRIBE = P + "scribe"                              # she has a scribe: the Commander takes her dictation
MARGIN = P + "margin"                              # Derived: at least one session after the first (the blank has been noticed)
TEST = P + "test_running"
TAMPERED = P + "tampered"
DECLINED = P + "declined"                          # her ruling on a contaminated night; a replication stays open
CONFESSED = P + "confessed"
FIRST_NIGHT = P + "first_night"
REPLICATED = P + "replicated"
REFUSED = P + "refused_her"                        # the Commander refused her conclusion (the Commander's no)
LATE_COMMITTED = P + "late_committed"              # Derived (trickster_world): trickster.ever + started
# Moral pivot (the Architect's entry, nenio_folios): recorded here for the pages and reactions.
ARCH_DEAD = F + "architect.the_dead"
ARCH_AGREED = F + "architect.agreed"
ARCH_TRICK = F + "architect.footnote"
# The killed world's box marked KENABRES? (nenio_folios): told, or lied to (a Ledger secret).
TOLD_BITE = "nenio.told_bite"                      # SelectedAnswers CompanionDialogues/Nenio/Answer_0132 ("I can bite hard enough, too!")

KENABRES_SAID = F + "stranger.kenabres_said"        # the Commander named Kenabres to the recreated stranger (the box's source)
KENABRES_TOLD = F + "kenabres_box.told"
KENABRES_PENDING = F + "kenabres_judgment.pending"
KENABRES_JUDGMENTS = (F + "kenabres_judgment_visitor", F + "kenabres_judgment_arcade")
POETRY_FAILED = "nenio.native.poetry_failed"
GOSSIP_PREPARED = "nenio.native.gossip_prepared"
GOSSIP_UNIVERSAL = "nenio.native.gossip_universal"
BROUGHT_SAFE = "nenio.native.brought_to_safety"
RECRUITMENT_REFUSED = "nenio.native.recruitment_refused"
FRIEND_SKETCH = "nenio.native.friend_sketch"  # drawing begun; not an inventory receipt
FRIEND_TONGUE = "nenio.native.friend_tongue"
FRIEND_CREDIT = "nenio.native.friend_credit"
FRIEND_REFUSED = "nenio.native.friend_refused"
KENABRES_LIED = F + "kenabres_box.lied"
KENABRES_SECRET = "trickster.secret.nenio_kenabres"
KENABRES_SECRET_KNOWN = KENABRES_SECRET + ".known.nenio"

ENTRY_FLAGS = (STARTED,)

RELATIONSHIP = dict(
    Title="A Name for a Name",
    Description=("Nenio, a kitsune scholar some four thousand years old, is writing an encyclopedia of everything on "
                 "Golarion and needs someone to hold the pen. She files what matters and forgets the rest. My name, she "
                 "says, is in the second pile."),
    Objective="Take Nenio's dictation",
    Guidance=("On the Trickster path. Keep Nenio in your company and let her dictate to you. In the Enigma, if she "
              "hesitates between two truths, you can pose her a riddle only she can answer, if you are willing to stake "
              "something on it. If she asks you a question she did not mean to ask, answer it the way a scientist would "
              "want it answered, and then leave her results alone."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, KILLED, SENT_AWAY, KICKED_OUT, DISSOLVED], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED, KILLED: RETURNED, SENT_AWAY: RETURNED, KICKED_OUT: RETURNED},
    TricksterAccess={
        "enigma": dict(detect=[ASKED_TO_LEAVE], device=P + "taken.riddle", returned=RIDDLE_DONE),
        DEAD: dict(detect=[DEAD], device=P + "dead.the_price", returned=RETURNED),
        KILLED: dict(detect=[KILLED], device=P + "killed.recreated", returned=RETURNED),
        "nenio.away": dict(detect=[SENT_AWAY, KICKED_OUT], device=P + "away.correction", returned=RETURNED),
    },
)

REVIVALS = {"nenio": dict(Relationship=REL, Unit=UNIT, DeathFlag=DEAD)}

GREETING = ("{n}In the lane beside the spice trader's stall a woman in a scholar's grey coat has turned two of his crates into a desk "
            "and a third into a chair. Her hair is pinned up with a pencil, and she is measuring the passers-by with her "
            "eyes and writing the numbers down.{/n}")
PRESENCES = {
    # A spawned copy of her Chapter 1 unit behind the exotic trader's awning in the market (build sheet): 5 m from Aranka's
    # copy, which stands in front of the same trader. Never at Fye's bar, the yard or the smith.
    PRESENCE: dict(Unit=COPY_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=EXOTIC, Offset=[7.0, -4.0]),
                   Requires=["trickster.ever", VISITOR], Forbids=[CLOSED, FAILED], MinChapter=3, MaxChapter=5,
                   AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # If the trader's stall is not in the capital: the jeweller's arcade, right of the jeweller at 2.5 m (at least 3.2 m from
    # Arueshalae's evil fallback in front at 2.0, 5 m from Nidalynn's widow on his left; Mielarah is not at this unit).
    ARCADE: dict(Unit=COPY_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=JEWELER, Side="right", Distance=2.5),
                 Requires=["trickster.ever", VISITOR, FAILED], Forbids=[CLOSED], MinChapter=3, MaxChapter=5,
                 AnswerLists=[], Dialog="hub",
                 Greeting="{n}Under the jeweller's arcade, a woman in a scholar's grey coat has claimed the dry end of the "
                          "step. She is weighing a refugee's copper torc in one hand and a stone in the other, and writing "
                          "down which is heavier.{/n}"),
}

# Where a beat is played: her own hub while she travels with you, or her copy in the market when she has come back without
# her place in the company. The spice trader's crates, or the jeweller's step if his stall is gone.
PLACES = {
    "hub": dict(suffix="", texts={
        "@DESK@": "a drum case with a plank across it",
        "@WHERE@": "at the edge of the camp",
        "@AROUND@": "the camp",
        "@SEAT@": "a coil of rope",
    }),
    "visitor": dict(suffix="_visitor", texts={
        "@DESK@": "two of the spice trader's crates",
        "@WHERE@": "behind the spice trader's awning",
        "@AROUND@": "the market",
        "@SEAT@": "a third crate, which the trader has given up asking for",
    }),
    "arcade": dict(suffix="_arcade", texts={
        "@DESK@": "the dry end of the jeweller's step",
        "@WHERE@": "under the jeweller's arcade",
        "@AROUND@": "the arcade",
        "@SEAT@": "the step beside her",
    }),
}


def nen(id, text, *choices, **kw):
    return n(id, "Nenio", text, *choices, portrait="Nenio", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Nenio", **kw)


def grey(id, text, *choices, **kw):
    """The Faceless Sphinx's servant: a guiser in a grey robe and a plain white mask (FoxReveal/Cue_0001; Cue_0042)."""
    return n(id, "Faceless servant", text, *choices, portrait="Nenio", **kw)


def fit(text, place):
    for token, value in PLACES[place]["texts"].items():
        text = text.replace(token, value)
    return text


def placed(nodes, place):
    return [dict(node, Text=fit(node["Text"], place),
                 Choices=[dict(ch, Text=fit(ch["Text"], place)) for ch in node["Choices"]]) for node in nodes]


def twin_ids(id):
    return tuple(id + spec["suffix"] for spec in PLACES.values())


def meet(id, title, entry, nodes, requires, forbids=(), delay=24, chapter=3, optional=True, places=("hub", "visitor", "arcade"),
         into=None, **extra):
    """A physical beat, on her hub while she is in the party and on her copy in the market while she visits; each place is
    its own scene id, and each Forbids the others, so the beat plays once."""
    ids = tuple(id + PLACES[place]["suffix"] for place in places)
    for place in places:
        spec = PLACES[place]
        req = ("trickster.ever", *requires)
        forb = (CLOSED, *ids, *forbids)
        if place == "hub":
            where = dict(AnswerLists=[HUB], ContactUnit=UNIT)
            forb = (*forb, VISITOR)
        elif place == "visitor":
            where = dict(ContactUnit=COPY_UNIT, InteractionHub=PRESENCE, Areas=[DREZEN])
            req = (*req, VISITOR)
            forb = (*forb, FAILED)
        else:
            where = dict(ContactUnit=COPY_UNIT, InteractionHub=ARCADE, Areas=[DREZEN])
            req = (*req, VISITOR, FAILED)
        (SCENES if into is None else into).append(scene(id + spec["suffix"], title, "Nenio", chapter, fit(entry, place), placed(nodes, place),
                            requires=tuple(dict.fromkeys(req)), forbids=tuple(dict.fromkeys(forb)), delay=delay, last=5,
                            optional=optional, Relationship=REL, Chapters=[3, 5] if chapter == 3 else [5], **where, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, kind="visit", chapters=(3, 5), optional=True, into=None, **extra):
    """A rest-delivered scene: a night in which she is there in person, a letter, or a Commander-only event."""
    req = tuple(dict.fromkeys(requires if "trickster" in requires else ("trickster.ever", *requires)))
    (SCENES if into is None else into).append(scene(id, title, "Nenio", min(chapters), "", nodes, requires=req,
                        forbids=tuple(dict.fromkeys((CLOSED, id, *forbids))), delay=delay, last=max(chapters),
                        optional=optional, Relationship=REL, Remote=True, Kind=kind, Chapters=list(chapters), **extra))


# --- Chapter 5, the Enigma: a riddle only she can answer (inline on FoxMyself, before her two native arguments are spent). --

RIDDLE_TEXT = '''"Here it is. I am the zero on a shoulder and the pencil behind an ear. I was a mask before I was a face. I plan a hundred volumes and carry one bound working draft. I forget what does not matter. I keep the name I chose. Your Sphinx says I am nothing. What am I?"'''

SCENES.append(scene(P + "taken.riddle", "A riddle only she can answer", "Nenio", 5,
    '[Pose her a riddle] "You love riddles. You said so at the Nameless Ruins. Answer me one, and only one."',
    [nen("start", '''{n}The kitsune turns her head toward you without turning anything else. Her face is perfectly calm, the calm of a lake with nothing living in it.{/n}
"A riddle is a question wearing a mask. The anomaly has taken its mask off. It does not answer questions. It has no reason to." {n}Somewhere under the flat voice, very faintly, like a word pencilled under an erasure, something that sounds like Nenio says: "I love riddles." The face does not move.{/n}
"Ask, grain of sand. The universe listens to everything. It rarely replies."''',
         c('[Knowledge (World)] Build it the way the statues at the Nameless Ruins were built, out of everything she ever told you she was.',
           check=dict(Skill="SkillKnowledgeWorld", DC=32, Success="posed", Failure="tangled"), forbids=(ASKED_FORGETTING, ASKED_GIFT)),
         c('[Knowledge (World)] Build it on the one thing she once told you she does: stop thinking about whatever she means to lose.',
           check=dict(Skill="SkillKnowledgeWorld", DC=26, Success="posed", Failure="tangled"), requires=(ASKED_FORGETTING,)),
         c('[Knowledge (World)] Build it on what she told you just now: that the Sphinx\'s followers rule knowledge and forgetting in their own memories.',
           check=dict(Skill="SkillKnowledgeWorld", DC=26, Success="posed", Failure="tangled"), requires=(ASKED_GIFT,),
           forbids=(ASKED_FORGETTING,)),
         c("[Let it go.]", abort=True)),
     nar("posed", '''{n}You build the riddle around the scholar: her pencil, her working draft, the name she chose. The words must distinguish her from the mistress who would make her a mask again.{/n}
''' + RIDDLE_TEXT,
         c("Continue", "stake")),
     nen("stake", '''{n}She listens with her head a little on one side. When you finish, her eyes go to the tattoo on her own shoulder, the circle she once called a zero, and come back.{/n}
"The riddle has one answer." {n}Flatly.{/n} "And the anomaly will not give it. An answer is knowledge, and knowledge is not given away. The Faceless Sphinx does not share what she knows. She collects it. Power in exchange for service. Meaning in exchange for usefulness. Nothing for nothing."
{n}It is Areshkagal's law in her mouth. It is also an opening. She has just told you the one thing she will still do: trade.{/n}''',
         c('[Offer the stake] "Then trade. A name for a name. Answer me, and keep yours. Take mine for it. File it wherever you file what you\'ll never look at again, and never say it to me again."',
           "answer"),
         c('[Tell her the answer] "It\'s you, Nenio. The answer is Nenio. Say it."', "told"),
         c("[Let it go.]", abort=True)),
     nen("answer", '''{n}Nothing happens. Then her hand moves, on its own, to her sleeve, where there is always a crumpled page, and stops halfway, because there is nothing written on it that she needs.{/n}
"A name. For a name." {n}She says it the way she would read a figure off a scale.{/n} "The grain of sand stakes its label. A label is only sounds. The grain of sand knows it is only sounds. It stakes it anyway." {n}Her ears move, very slightly, forward.{/n} "That is irrational. That is... interesting."
"Very well. An exchange."
{n}Her lips move once without sound, as if she is checking the word before she spends it.{/n} "The answer is Nenio."''',
         c("Continue", "filed")),
     nen("filed", '''{n}Something goes out of her shoulders, the way a held breath goes. She blinks at you, twice, fast.{/n}
"The riddle is answered. The stake is taken." {n}She studies your face with enormous care, like a page she means to copy out before it is taken away.{/n} "I have your name still. I shall file it tonight, when we are out of this place, the way I file everything: I think of it once, completely, and then I stop. By morning it will be gone." {n}Quietly, and not in the anomaly's voice at all:{/n} "Until then I may spend it once or twice. Do not count."''',
         c("[Let her go on.]", native_next=FOX_ONE, forbids=(FOX_ARGUED,), flags=(RIDDLE_DONE, STARTED, NAME_STAKED)),
         c("[Let her go on.]", native_next=FOX_TWO, requires=(FOX_ARGUED,), flags=(RIDDLE_DONE, STARTED, NAME_STAKED))),
     nen("told", '''{n}Her gaze settles on you, level and empty.{/n}
"The absence of an answer is an answer too." {n}It is exactly what the masked woman said to you among the statues, long ago, and she says it in exactly the same voice.{/n}
"A riddle told is a riddle spent. The grain of sand has given the answer away, and received nothing for it. The universe notes the waste."''',
         c("[Step back from the riddle.]", flags=(RIDDLE_DECLINED,))),
     nar("tangled", '''{n}You begin: "I wear a face that hides what I am. I keep knowledge others cannot have. What am I?" Halfway through, the mistake is plain. You have described Nenio's secrets and her mistress's hoard.{/n}''',
         c("Continue", "tangled_her")),
     nen("tangled_her", '''"Two answers. The anomaly. The Faceless Sphinx. Your question distinguishes neither." {n}Her eyes remain fixed on you.{/n} "Try again, grain of sand."''',
         c('[Lore (Religion)] "The inscription says to tear the mask away. What took its own name instead of remaining the Sphinx\'s mask?"',
           check=dict(Skill="SkillLoreReligion", DC=24, Success="rebuilt", Failure="lost")),
         c("[Let it go.]", flags=(RIDDLE_DECLINED,))),
     nar("rebuilt", '''{n}You discard the two vague lines and rebuild the riddle around the scholar: the zero on her shoulder, the pencil, the hundred projected volumes, the name she chose for herself. It no longer asks what hides behind a mask. It asks who stopped being only a mask.{/n}''',
         c("Continue", "stake")),
     nen("lost", '''{n}You try. The words come out in the right order and mean the wrong thing. She waits until you have finished, with the courtesy of a stone.{/n}
"Two answers still. The riddle is a failure." {n}A pause.{/n} "Failed experiments are also data. That is what somebody used to say. The anomaly does not remember who."''',
         c("[Step back from the riddle.]", flags=(RIDDLE_DECLINED,)))],
    requires=("trickster", ASKED_TO_LEAVE), forbids=(RIDDLE_DONE, RIDDLE_DECLINED, DISSOLVED), last=5, Relationship=REL,
    Chapters=[5], AnswerLists=[FOX_LIST], NativeReturnCue=FOX_RETURN, EntryMythic="PlayerIsTrickster", TricksterDevice=True,
    TricksterState="enigma"))


# The first conversation after the Enigma, on her hub: the shape of the place where the name was.
meet(P + "after_enigma", "The shape of a name", '"You keep looking at me as if I were a misprint."', [
    nar("open", '''{n}Nenio sits on @SEAT@ with an empty sheet on her knee. She looks at your face, then your sleeve, then the sheet.{/n}
"A name for a name. I have kept mine. Now I shall file yours. Do not say it while I work."
{n}She closes her eyes. Her lips form a word without sound. Then she opens her eyes, studies your face again, and leaves the pencil poised above the sheet.{/n} "No name. Let me check the rest."''',
        c("Continue", "missing")),
    nen("missing", '''"Filed. Your face still supplies no name. Your sleeve supplies no name. It is gone." {n}She taps the pencil against the blank sheet.{/n} "Everything else is where I left it. Areshkagal, the Enigma, the grain of sand, the mask, the chicken and the egg, which I never got to ask about. The way back, which I could draw for you blindfolded. Your face, your equipment, the way you stand beside my notes."
"Your name is not. There is a hole the shape of it. I can feel the edges. It is like putting your tongue where a tooth was."''',
        c('"You said it once, at the end. You thanked me."', "thanked"),
        c('"You never used it anyway."', "never"),
        c('"Do you want it back?"', "back")),
    nen("thanked", '''"Did I?" {n}She considers it with real interest.{/n} "Then that was the last withdrawal before the account closed. Good. I would hate to think I wasted it." {n}Her ears go back a fraction.{/n} "No. That is untrue. I would hate to think I did not."''',
        c("Continue", "law")),
    nen("never", '''"Irrelevant. I did not use it because I did not need to, not because I did not have it. A book on a shelf you never open is still a book on a shelf." {n}She sniffs.{/n} "An empty shelf is a different object altogether. It is an empty shelf."''',
        c("Continue", "law")),
    nen("back", '''"No." {n}At once, and then more slowly.{/n} "It was a stake. You offered it and I took it. If I could give it back it would not have been a stake, it would have been a loan. That was not my offer." {n}She frowns at the paper.{/n} "Also I do not know where I put it, which makes returning it technically difficult."''',
        c("Continue", "law")),
    nen("law", '''"The interesting part is this." {n}She holds the pencil up like a pointer.{/n} "I have forgotten a great many things on purpose. Kings, arcane schools, my own species, once, for several centuries. None of them ever left a hole. I stop thinking about them and they are simply not there, the way the sea is not there when you are standing in a desert."
"This left a hole. Hypothesis: a thing that leaves a hole was load-bearing." {n}She writes it down, and underlines it, and then looks at what she has written as if it had been rude to her.{/n} "I dislike that hypothesis. I am going to leave it on the page until it apologises."''',
        c('[Flirt] "Load-bearing. I\'ll take that."', "flirt"),
        c('"What am I to you now, then? Without the name."', "call"),
        c("[Leave her with her page.]", flags=(NAME_FILED,))),
    nen("flirt", '''"You will take it because it was not offered to you. That is very like you." {n}She does not quite smile.{/n} "Follower. I shall call you follower, which is accurate, and {mf|boy|girl} when you are being tiresome, which is also accurate."''',
        c("[Leave her with her page.]", flags=(NAME_FILED,))),
    nen("call", '''"Follower. It was always accurate. Now it is also sufficient." {n}She taps the sheet.{/n} "The Encyclopedia will have to make do. Under 'Crusade, Commander of the', there will be a space, and after the space a great many adjectives, most of them provisional."''',
        c("[Leave her with her page.]", flags=(NAME_FILED,))),
], requires=(RIDDLE_DONE, ENIGMA_RESOLVED), forbids=(NAME_FILED,), delay=12, chapter=5, places=("hub",))


# --- Loss worlds (build sheet): the Sphinx's servant, and the follower's field report. --------------------------------------

visit(P + "dead.the_price", "The vessel belongs to the Sphinx", [
    nar("open", '''{n}They have laid Nenio out on a trestle in the cold room behind the chapel, with her pencil in her fist, because nobody could get it out of her fingers. The chaplain has tied her hands together over her chest with a strip of linen, and her sleeves are still full of crumpled paper. One sheet has slid out onto the floor. It says, in her impossible hand, "Hypothesis:", and nothing after.{/n}
{n}There is somebody standing over her who was not there when you came in.{/n}''',
        c("Continue", "claim", forbids=(ENIGMA_RESOLVED,)),
        c("Continue", "claim_after", requires=(ENIGMA_RESOLVED,))),
    grey("claim_after", '''{n}A grey robe, frayed at the hem. A plain white mask with two slits in it. The figure does not turn when you come closer; it simply begins to speak, as if it had been waiting for an audience of exactly one.{/n}
"I am the answer, but what is the question?" {n}The mask tilts toward the body.{/n} "The anomaly's vessel was recreated to serve a purpose on Golarion. It served it: the worthy one was shown the way, and walked it. A tool that has done its work goes back to the one who made it. It belongs to the Faceless Sphinx. It is reclaimed."''',
        c('"She isn\'t yours. She took her mask off years ago."', "nothing"),
        c('"What does your mistress want for her?"', "nothing")),
    grey("claim", '''{n}A grey robe, frayed at the hem. A plain white mask with two slits in it. The figure does not turn when you come closer; it simply begins to speak, as if it had been waiting for an audience of exactly one.{/n}
"I am the answer, but what is the question?" {n}The mask tilts toward the body.{/n} "The anomaly's vessel was recreated to serve a purpose on Golarion. The vessel is spent before its purpose. It belongs to the Faceless Sphinx. It is reclaimed."''',
        c('"She isn\'t yours. She took her mask off years ago."', "nothing"),
        c('"What does your mistress want for her?"', "nothing")),
    grey("nothing", '''"The anomaly is nothing. Nothing has no owner but the one who made it." {n}The servant lays one grey sleeve across Nenio's bound hands, lightly, like a librarian marking a place.{/n} "Unless the grain of sand has something to offer the Sphinx that the Sphinx does not already know. That is a short list."''',
        c('[Offer the notes for the vessel] "Her notes. Every trunk of them: the whole of the Encyclopedia Golarionnica that is not yet written, everything she has observed and never shown anyone. Your mistress hoards secrets. Here is everything she has not published."',
          "terms", mythic="Trickster"),
        c('"Take the body. She\'d want it studied."', "rest")),
    grey("terms", '''{n}For a while the mask does nothing at all. Then, very slowly, it turns toward the trunks against the wall, the ones she dragged across half of Mendev and never let anyone lift.{/n}
"The grain of sand offers the anomaly's scribblings for the anomaly. Knowledge for a vessel." {n}A sound like a page turning, from somewhere inside the robe.{/n} "The Sphinx finds this acceptable, and insufficient. The grain of sand will also owe the Sphinx one answer, when she asks. Any question. The true answer. Not a riddle."''',
        c('[Hand over the notes] "Her notes, and one answer, when she asks. Give her back."', "raised"),
        c('[Refuse] "Not her life\'s work. Not for her. She\'d never forgive me."', "rest"),
        c('[Bargain over the terms] "One answer. And your mistress\'s own rule goes in the terms with it: the absence of an answer is an answer too."',
          "clause", mythic="Trickster")),
    grey("clause", '''{n}The mask stops. For the first time it looks at you instead of through you.{/n}
"The grain of sand quotes the Sphinx to her servant, over the body, in the middle of a bargain." {n}A page turns inside the robe.{/n} "She values that more than the scribblings. It goes in the terms. But a clause is not free. If the grain of sand ever pays in silence, whatever it withholds becomes the Sphinx's. It will never be able to say those words, to anyone, in any tongue."''',
        c('[Hand over the notes] "Her notes, one answer, and the clause. Give her back."', "raised", flags=(SILENCE_CLAUSE,))),
    nar("raised", '''{n}The servant does not lift the trunks. It rests one hand on the lid of the first, and they are simply lighter, the way a room is lighter when somebody has left it. When you look again the mask is gone, and the trunks are empty except for the first, which holds one bound book: volume one, the only volume she ever had bound, its spine cracked from being opened too often.{/n}
{n}On the trestle, Nenio sneezes. Then she sits up, looks at the linen on her wrists, looks at the chaplain in the doorway, and says with great indignation, "Who tied me up? This is not a knot. This is an insult to knots."{/n}''',
        c("[Untie her hands.]", revive="nenio", flags=(RETURNED, STARTED, MANUSCRIPT, OWES))),
    nar("rest", '''{n}The servant inclines its mask to you, a small, exact courtesy, the kind a clerk gives a customer who has decided not to buy.{/n}
{n}In the morning the trestle is empty. The linen is folded on it, very neatly, and on top of the linen lies the sheet that fell from her sleeve. Someone has finished it. "Hypothesis: nothing." It is not her handwriting.{/n}''',
        c("[Fold the sheet away.]", flags=(LET_REST,))),
], requires=("trickster", DEAD, DEAD_L), forbids=(RETURNED, LET_REST), delay=24, kind="event", chapters=(3, 5),
    Recovery="nenio", TricksterDevice=True, TricksterState=DEAD, Areas=[DREZEN])

visit(P + "dead.the_price_recreated", "A new vessel", [
    nar("open", '''{n}There was nothing left to bury. The report says so plainly, in a clerk's round hand: the scholar Nenio, kitsune, lost with the rearguard; no remains recovered. Somebody has written "Encyclopedia?" in the margin, and somebody else has crossed it out.{/n}
{n}Her trunks came back with the baggage. You are sitting on one of them, with the report on your knee, when you notice the grey figure in the corner of the tent.{/n}''',
        c("Continue", "claim")),
    grey("claim", '''"I am the answer, but what is the question?" {n}A plain white mask, a frayed grey robe.{/n} "The anomaly's vessel is spent, and scattered. The Sphinx made it once, from a pilgrim's dust. The Sphinx could make it again. The Sphinx does nothing for nothing."''',
        c('[Offer the notes for a new vessel] "Her notes, every trunk of them, the whole unwritten Encyclopedia, and every secret in them she never let anybody read. Make her again."',
          "terms", mythic="Trickster"),
        c('"Let her be. She would hate being made twice."', "rest")),
    grey("terms", '''"Knowledge for a new vessel. The old one is spent." {n}The mask turns to the trunks under you, and you feel them grow lighter through the wood.{/n} "And the grain of sand will owe the Sphinx one answer, when she asks. The new vessel will come on its own feet. It will not march in the grain of sand's army. It was not bought for the army."''',
        c('[Hand over the notes] "Her notes, and one answer. Make her."', "made",
          flags=(RETURNED, STARTED, MANUSCRIPT, OWES, RECREATED)),
        c('[Refuse] "Not her life\'s work."', "rest"),
        c('[Bargain over the terms] "One answer. And your mistress\'s own rule goes in the terms with it: the absence of an answer is an answer too."',
          "clause", mythic="Trickster")),
    grey("clause", '''{n}The mask stops. For the first time it looks at you instead of at the trunks.{/n}
"The grain of sand quotes the Sphinx to her servant, in the middle of a bargain." {n}A page turns inside the robe.{/n} "She values that more than the scribblings. It goes in the terms. But a clause is not free. If the grain of sand ever pays in silence, whatever it withholds becomes the Sphinx's. It will never be able to say those words, to anyone, in any tongue."''',
        c('[Hand over the notes] "Her notes, one answer, and the clause. Make her."', "made",
          flags=(RETURNED, STARTED, MANUSCRIPT, OWES, RECREATED, SILENCE_CLAUSE))),
    nar("made", '''{n}The servant lays its hand on the last trunk. When it lifts the hand, the trunk is empty too.{/n} "The vessel is made. It stands on the road outside Drezen with the bound draft. It will not join your army. The grain of sand owes the answer." {n}The mask turns toward the campaign map, then the figure disappears.{/n}''',
        c("[Fold the report away.]")),
    nar("rest", '''{n}The grey figure bows exactly as far as courtesy requires, and is gone. The trunks stay heavy. You never open them. Nobody could have read them anyway.{/n}''',
        c("[Leave the trunks closed.]", flags=(LET_REST,))),
], requires=("trickster", DEAD, DEAD_L), forbids=(RETURNED, LET_REST, BODY_KEPT), delay=24, kind="event",
    chapters=(3, 5), TricksterDevice=True, TricksterState=DEAD)   # Sol r3 COX: an Abyss loss waits for Drezen (R2-5)

# Chapter 5, in person (Sol r1 COX: no new rest delivery): the Sphinx's servant collects the answer owed, in front of her.
# The question is her own trap's ("Who are you?", which "merely stating my name failed to satisfy", FoxReveal/Cue_0044).
# The prepared loophole is bargained at the debt itself (Sol r3 TRK): the Commander wrote the Sphinx's axiom ("The absence of
# an answer is an answer too", FoxReveal/Cue_0002) into the terms, at a price named then: the withheld words become hers.
meet(P + "debt.collected", "The question", '"Nenio? Who is that behind you?"', [
    nar("open", '''{n}Nenio is at @DESK@ with her pencil stopped halfway through a word, looking past you. There is a grey figure standing @WHERE@ where nobody was a moment ago: a frayed robe, a plain white mask.{/n}
{n}"It is for you," she says, very quietly, without taking her eyes off it. "Do not mind me. I am taking notes."{/n}''',
        c("Continue", "ask")),
    grey("ask", '''"I am the answer, but what is the question?" {n}The mask tilts, from you to her and back.{/n} "Today the question is the Sphinx's, and the answer is owed. One question. The true answer. Not a riddle."
"Who is the anomaly?" {n}A pause, exactly long enough.{/n} "She was asked the same among the statues, and her name did not satisfy. It will not satisfy now. A false answer, or a partial one, and the Sphinx takes back what she made."''',
        c("[Pay] Answer it truly, all of it, with her listening.", "paid"),
        c("[Pay in the Sphinx's coin] Say nothing, as the terms allow, and hold the mask's eyes.", "coin",
          requires=(SILENCE_CLAUSE,), mythic="Trickster"),
        c('[Refuse] "Not to you. Take something else."', "default")),
    nar("paid", '''{n}You tell it. It takes a long time, because the true answer is long, and the mask does not hurry you. What she is: a kitsune who forgot she was one, four thousand years old, a pilgrim's dust made over by a Sphinx, a scholar with a hand nobody can read. What she is to you. What you gave for her. Behind you her pencil has stopped moving altogether.{/n}''',
        c("Continue", "kept")),
    grey("kept", '''"The answer is true and complete." {n}Something inside the robe turns a page.{/n} "The Sphinx keeps what she is given. The grain of sand will find that those words are hers now. It may say other words to the anomaly. Not those. Never those again."
{n}Then there is nobody there.{/n}''',
        c("Continue", "heard")),
    nen("heard", '''"I heard it." {n}She has not written a word.{/n} "Once. That is the whole print run, then: one copy, and I have it, and it is not for the Encyclopedia." {n}Her ears are flat against her hair.{/n} "Do not try to say it again. I would not be able to bear watching you find out that you cannot."''',
        c("[Sit down beside her, and say other things.]", flags=(DEBT_PAID,))),
    nar("coin", '''{n}You say nothing. The clause is in the terms; you put it there yourself, and the servant took it. You do not look away from the slits in the mask, and you do not fill the silence, though it goes on long enough to become a sound of its own.{/n}''',
        c("Continue", "contested")),
    grey("contested", '''"Silence is the Sphinx's coin. It is also a refusal wearing a mask." {n}The mask does not move.{/n} "But the clause is the Sphinx's own, and she does not contradict herself. She takes the coin, at the price named when it was written."
"A coin is struck from metal. This one is struck from what the grain of sand would have said. The Sphinx takes the metal. The grain of sand keeps nothing: it will never be able to say those words, to anyone."''',
        c("[Hold its eyes. Pay the metal.]", "coin_done"),
        c("[Pay after all] Answer it truly, all of it.", "paid")),
    nen("coin_done", '''{n}Then there is nobody there, and Nenio lets out a breath she seems to have been holding since the Nameless Ruins.{/n}
"You paid her in her own coin, and she bit it, and it rang true." {n}She looks at you with enormous interest.{/n} "So the Sphinx has nothing about me. And you have nothing to say about me, ever, in so many words." {n}She picks up the pencil.{/n} "I can live with the second. I discard most people's words anyway. I shall have to watch what you do instead, which was always the better data."''',
        c("[Let her watch.]", flags=(DEBT_EVADED,))),
    grey("default", '''"The grain of sand defaults." {n}No anger in it. A clerk noting a sum.{/n} "A debt unpaid is collected from the security. The security is the vessel. The Sphinx does not want the vessel; it has a purpose still. She will take what the vessel values most that is not the vessel."
{n}Then there is nobody there.{/n}''',
        c("Continue", "default_after")),
    nen("default_after", '''{n}Her hand goes to @DESK@, to where volume one always lies. It is not there. She lifts the papers, and the stone, and looks under them, and it is not there either.{/n}
"My book." {n}It is not a question.{/n} "You owed her an answer, and you did not give it, and she took my book instead." {n}Her ears are flat.{/n} "I would have told you to give it. I would have told you in very long words. You did not ask."''',
        c("[Let her be angry.]", flags=(DEBT_DEFAULTED,))),
], requires=(OWES, SCRIBE, P + "night"), forbids=(*DEBT_SETTLED, DISSOLVED), delay=48, chapter=5)   # Sol r3: after night one


# In person, once she is back in the party: the surrendered notes.
meet(P + "dead.welcome_back", "Every trunk", '"Nenio. You look... well."', [
    nar("open", '''{n}Nenio has all her trunks open around her like a fortress with the walls knocked down. They are empty. Every note she carried is gone, every bundle, every string. She is sitting in the middle of them with volume one of the Encyclopedia Golarionnica on her knees, the only volume she ever had bound, holding it with both hands, as if it might also try to leave.{/n}''',
        c("Continue", "theft")),
    nen("theft", '''"The notes for the Encyclopedia Golarionnica are missing. All of them." {n}She says it very calmly, which is worse than shouting.{/n} "Hypothesis one: theft. The thief left volume one. Hypothesis two: the thief has taste. The bound draft remains; the loose notes cannot be rebuilt from memory. The thief wished me to suffer exactly as much as possible and no more."
"Hypothesis three is that I am dead and this is an afterlife for scholars, but the tea is too bad for that." {n}She lifts her eyes to you.{/n} "Do you know anything about this, {mf|boy|girl}?"''',
        c('[Tell her] "You died. A servant of the Sphinx came for your body. I bought you back with your notes."', "told",
          flags=(TOLD_THEFT, SCRIBE)),
        c('[Say nothing] "I\'ll ask around."', "silent", flags=(THIEF_HUNTED, SCRIBE))),
    nen("told", '''{n}She does not move for some time. Her thumb goes back and forth over the cracked spine of volume one.{/n}
"You sold my life's work to the Faceless Sphinx for my life." {n}She counts something on her fingers, loses count, and starts again.{/n} "Every note I ever took. Every trunk. For one kitsune who cannot even keep a pencil sharp."
"That is the worst trade I have ever heard of, and I am including the time a man in Absalom sold me a map to his own house." {n}Her voice wobbles and she frowns at it until it stops.{/n} "What did the servant's hands look like? Describe them. Precisely. I intend to steal it all back one day, and I will need to recognise the shelf."''',
        c("Continue", "begin")),
    nen("silent", '''"Ask around." {n}She gives you the expression she keeps for a sample that has lied about its weight.{/n}
"Very well." {n}She opens volume one at the flyleaf, takes the pencil out of her hair, and writes across the top of the page in capitals: THIEF. Then she underlines it twice.{/n} "I shall find them. I have a great deal of free time now. It used to be full of notes."''',
        c("Continue", "begin")),
    nen("begin", '''"Now. The notes are gone, so I shall have to observe everything again, and write it down again, and I cannot do it with my own hand. Nobody can read it, including, on bad days, me." {n}She holds the pencil out to you, point first.{/n}
"You will. From dictation. Starting with corrections to the bound draft. 'Babau'. The loose notes are gone; the first volume is still unfinished. You have a legible hand. It is the only thing about you I have ever envied."''',
        c('[Take the pencil.] "Corrections to volume one."'),
        c('[Take the pencil.] "You were dead, Nenio. I\'d have given more."', "more")),
    nen("more", '''"Then you are a very bad negotiator and I shall have to supervise all your future trades." {n}She sniffs, and turns the page so hard it nearly tears.{/n} "Babau. A demon. Smells of vinegar and a tannery. Write that down before I forget it on purpose."''',
        c("[Write it down.]")),
], requires=(RETURNED, MANUSCRIPT), forbids=(RECREATED,), delay=24, places=("hub",))

# The recreated vessel, at the market: she has her volume one and no army.
meet(P + "dead.market", "Made twice", '"Nenio?"', [
    nen("open", '''{n}She looks up from @DESK@ with a pencil between her teeth, and takes it out to speak.{/n}
"Correct, and I did not tell you. Interesting. You have the look of somebody who has been to my funeral." {n}She squints.{/n} "Do not deny it. People who have been to a funeral always stand as if they are still holding their hat."''',
        c("Continue", "made")),
    nen("made", '''"I woke on the road outside Drezen with my bound working draft and an instruction not to join armies. The instruction remains. My notes do not." {n}She pats volume one.{/n} "My notes are gone, all of them. I suspect the Faceless Sphinx. I have no proof. I dislike having no proof about my own biography."
"Did you do something?"''',
        c('[Tell her] "I paid for you with your notes. Every trunk of them."', "told", flags=(TOLD_THEFT, SCRIBE)),
        c('[Say nothing] "I\'m just glad to see you."', "silent", flags=(THIEF_HUNTED, SCRIBE))),
    nen("told", '''"You paid for me." {n}She looks at the book, and at you, and at the book.{/n} "With my own work. Without asking me." {n}Her ears flatten.{/n} "I would have said no. I would definitely have said no. I would have said it in very long words."
"And then I would have been dead, and unable to say anything, which is a weakness in my position." {n}She sets the pencil down with great precision.{/n} "Sit. I cannot join your army. But the Encyclopedia does not care about armies, and it needs a hand that people can read."''',
        c("[Sit on @SEAT@.]")),
    nen("silent", '''"Glad." {n}She writes the word down, looks at it, crosses it out hard, and writes THIEF over the top of it.{/n} "I shall find out who took my notes. Meanwhile you may be useful. The Encyclopedia needs a hand that people can read, and I need somebody who is glad, as a control."''',
        c("[Sit on @SEAT@.]")),
], requires=(RETURNED, RECREATED), delay=24, places=("visitor", "arcade"))


visit(P + "killed.recreated", "What is the question?", [
    nar("open", '''{n}You are writing the report on Kenabres for the Queen's archivists, late, by one lamp. It is a long report. It has a great many names in it of people who are dead, and a section headed "the cultist suspected of" that you have never finished.{/n}
{n}Someone is reading it over your shoulder, and has been for some time.{/n}''',
        c("Continue", "mask")),
    grey("mask", '''"I am the answer, but what is the question?" {n}A frayed grey robe. A plain white mask with nothing painted on it. The voice has no age.{/n}
"The Faceless Sphinx sent her servants to Golarion to find the worthy one and show the worthy one the path to the Enigma. One of them was given a pilgrim's body, and a mind of its own, which was a mistake. The grain of sand ended that servant's mission in Kenabres, before it had shown anybody anything."''',
        c('"Nenio. The one who asked too many questions."', "purpose"),
        c('"I did what I had to do in Kenabres."', "purpose")),
    grey("purpose", '''"The grain of sand did what it did. The universe keeps no account of 'had to'." {n}The mask tilts to the unfinished line on your page.{/n} "The path was not shown. The purpose is unserved. The Sphinx is patient. She will send another servant, in time. In a century. In ten."''',
        c('[Knowledge (Arcana)] "Your mistress doesn\'t throw away a tool that\'s half used. The vessel was made once. The purpose is still open, and the only one who ever came close to serving it was that one. Make her again, and let her finish the job."',
          check=dict(Skill="SkillKnowledgeArcana", DC=24, Success="argued", Failure="argued_badly"), mythic="Trickster"),
        c('"Then let her rest."', "rest")),
    grey("argued", '''{n}The mask regards you for as long as it takes a candle to gutter and recover.{/n}
"A hammer can be used on more than one nail. The grain of sand has read the Sphinx's own thoughts back to her." {n}A pause.{/n} "It is impudent. It is also correct. The vessel was recreated once. It can be recreated again."''',
        c("Continue", "terms")),
    grey("argued_badly", '''{n}You make the argument badly: too long, too clever, full of words the servant clearly thinks you do not understand. It hears you out anyway.{/n}
"The grain of sand's reasoning is poor." {n}A pause.{/n} "The conclusion is not. The purpose remains unserved. The vessel can be recreated. The Sphinx does not pay for arguments. She weighs conclusions, and this one stands without its argument."''',
        c("Continue", "terms")),
    grey("terms", '''"The grain of sand will owe the Sphinx one answer, when she asks. And the anomaly will not remember the grain of sand. Not Kenabres, not the blade, not the face. Memory was not purchased. Memory is extra."''',
        c('[Accept] "Then she won\'t remember me. Make her anyway."', "made", flags=(RETURNED, STARTED, UNREMEMBERED, OWES)),
        c('[Refuse] "No. Some entries stay closed."', "rest"),
        c('[Bargain over the terms] "One answer. And your mistress\'s own rule goes in the terms with it: the absence of an answer is an answer too."',
          "clause", mythic="Trickster")),
    grey("clause", '''{n}The mask stops. For the first time it looks at you instead of at the page.{/n}
"The grain of sand quotes the Sphinx to her servant, in the middle of a bargain." {n}A page turns inside the robe.{/n} "It goes in the terms. But a clause is not free. If the grain of sand ever pays in silence, whatever it withholds becomes the Sphinx's. It will never be able to say those words, to anyone, in any tongue."''',
        c('[Accept] "Then she won\'t remember me, and the clause stands. Make her anyway."', "made",
          flags=(RETURNED, STARTED, UNREMEMBERED, OWES, SILENCE_CLAUSE))),
    nar("made", '''"The vessel is made. It stands on the road outside Drezen with its book. It does not remember the grain of sand. The answer is owed." {n}The lamp flickers. The servant is gone. On the report, someone has written "Source restored" in a hand you do not recognize.{/n}''',
        c("[Put the report away.]")),
    nar("rest", '''{n}The mask inclines itself to you and is gone. You finish the report. Under "the cultist suspected of" you write, at last, the truth, and it takes longer than you expected, and there is no one to read it over your shoulder.{/n}''',
        c("[Seal the report.]", flags=(LET_REST,))),
], requires=("trickster", KILLED, KILLED_L), forbids=(RETURNED, LET_REST), delay=24, kind="event", chapters=(3, 5),
    TricksterDevice=True, TricksterState=KILLED)

# The recreated scholar at the market: she has never met the Commander, and hires a follower.
meet(P + "killed.stranger", "A follower wanted", '"Excuse me. Are you measuring me?"', [
    nen("open", '''"Yes. Stay where you are. Your equipment has altered your balance, and I want to see how." {n}She holds a knotted string in one hand and a pencil in the other.{/n} "You are nobody I know. That is not a criticism; I know almost nobody. I arrived with one volume of my work and no memory of the road here. Unless we have met? You seem to know something I do not."''',
        c('[Lie] "Never. I\'d remember you."', "never"),
        c('"We met once. In Kenabres. It went badly."', "kenabres", flags=(KENABRES_SAID,)),
        c('"I\'m the Commander of the crusade."', "commander")),
    nen("never", '''"Everyone says that and nobody does. Memory is a very unreliable instrument; that is why I write things down." {n}She makes a small note.{/n} "You lie with your left shoulder. Most people use their eyes. It is quite charming."''',
        c("Continue", "offer")),
    nen("kenabres", '''"Kenabres." {n}She waits for the word to mean something. It does not.{/n} "I have no record of Kenabres. That is an extraordinary gap for me; I have records of places I have never been." {n}She writes KENABRES? in the margin and draws a box round it.{/n} "If it went badly, I have probably decided to forget it. That is what I do with things that go badly. It saves a great deal of time."''',
        c("Continue", "offer")),
    nen("commander", '''"Are you." {n}She looks you up and down with scientific disappointment.{/n} "Thus far I see no scientific evidence of your exceptionality. But I have only been looking for a quarter of an hour, and I am told you have been busy."''',
        c("Continue", "offer")),
    nen("offer", '''"Here is my situation. I have one bound working draft for a projected hundred volumes, and no notes for the rest, which is not how I remember leaving them, except that I do not remember leaving them at all. My handwriting cannot be read by any living person, which is a safeguard against plagiarism and an obstacle to publication. I require a follower who can hold a pencil, walk behind me, write down my deepest thoughts, and admire the profundity of my intellect at reasonable intervals."
{n}She rubs her nose with the pencil.{/n} "You will do. You have been admiring it for some minutes already."''',
        c('"I accept."', flags=(SCRIBE,)),
        c('[Flirt] "What does the follower get?"', "gets", flags=(SCRIBE,))),
    nen("gets", '''"The follower gets to be present at the greatest scholarly undertaking of the age, which is more than most people get from anything." {n}She considers.{/n} "Also I will not measure you without asking. Often."''',
        c("[Take the pencil.]")),
], requires=(RETURNED, UNREMEMBERED), delay=48, places=("visitor", "arcade"))


visit(P + "away.field_report", "A field report", [
    nar("open", '''{n}Between the crusade's dispatches you write eleven pages on the Worldwound: rifts, demon tracks, and measurements copied from the scouts' reports. The envelope is addressed to Nenio, author of the Encyclopedia Golarionnica, care of the scholars' hostels on the road to Absalom. Page six has room for a vrock.{/n}''',
        c('[Make the diagram on page six wrong, in a way only she would notice.]', "wrong", mythic="Trickster"),
        c('[Make it all correct, and sign it plainly.]', "correct")),
    nar("wrong", '''{n}You draw its wings backwards, carefully, and add measurements. At the foot of the page: "Findings unverified. Verification requires the author in person." A scout would call it a bad drawing. Nenio will want to know whether the drawing or the demon is wrong.{/n}''',
        c("Continue", "reply", flags=(PRIMED_AWAY,))),
    nar("correct", '''{n}The diagrams agree with the scouts' measurements. You sign the report. There is no unanswered question in it and no request for Nenio to come to Drezen. You can send it as it stands, or redraw page six before sealing the envelope.{/n}''',
        c("[Send the correct report.]", "sent_correct"),
        c("[Redraw page six with the wings backwards.]", "wrong", mythic="Trickster")),
    nen("reply", '''{n}You seal the false report and put it in the courier's pouch. The address is repeated on every sheet. If Nenio finds page six, she will know where to bring her objections.{/n}''',
        c("[Send the report.]")),
    nar("sent_correct", '''{n}The report goes out with the dispatches. Whether Nenio reads it or not, nothing in it calls her back.{/n}''',
        c("[Return to the dispatches.]")),
], requires=("trickster", AWAY_L), forbids=(PRIMED_AWAY, RETURNED), delay=0, kind="letter", chapters=(3, 5),
    TricksterDevice=True, TricksterState="nenio.away", RequiresAnyGroups=[[SENT_AWAY, KICKED_OUT]])

meet(P + "away.correction", "Erratum", '"You came."', [
    nen("open", '''{n}She does not get up from @DESK@. She has your eleven pages spread across it, weighted with a stone at each corner, and page six on top.{/n}
"I did not come. I was sent for, by an observation. There is a difference and it is the entire difference." {n}She taps the backwards vrock.{/n} "This is wrong."''',
        c('"I know."', "known"),
        c('"Is it?"', "known")),
    nen("known", '''"You drew a wrong vrock on purpose, with measurements, and sent it to me. I came to see the specimen. Instead, I find you."''',
        c("Continue", "sent", requires=(SENT_AWAY,)),
        c("Continue", "kicked", forbids=(SENT_AWAY,))),
    nen("sent", '''"In Kenabres I offered to hire you. You declined. You were the twenty-eighth rejection, which made the result statistically irritating. Now you have sent me a specimen that does not exist. Your second application is worse than your first."''',
        c("Continue", "record_sent")),
    nen("kicked", '''"You dismissed me from your company. I left. Then this arrived, and I had to decide whether you had become less accurate in my absence. The evidence is compelling."''',
        c("Continue", "record_kicked")),
    nen("record", '''"I will correct the record. Here is the correction." {n}She produces a sheet from her sleeve, the paper soft with folding, and reads from it without needing to.{/n}
"The new entry is 'follower, probationary'. You will not tidy my notes. You will answer every question I ask, with numbers. The probation may be extended at the author's discretion, which is infinite." {n}She lifts her chin.{/n} "Say yes, or I leave on the next cart, and I shall not come back for any quantity of backwards vrocks."''',
        c('[Accept the probation] "Yes. Follower, probationary."', "yes", flags=(RETURNED, STARTED, DEMOTED, SCRIBE)),
        c('[Refuse her] "No. I wanted you back, not a probation."', "no", flags=(CLOSED,))),
    nen("yes", '''"Good." {n}She writes it down.{/n} "Your first duty is to sit on @SEAT@ and hold this stone on page six so that it does not blow away. It is an important stone. I have been using it as a control."''',
        c("[Hold the stone.]")),
    nen("no", '''{n}She nods, as if you had confirmed a figure she had already written down.{/n}
"Then the record stands as it was." {n}She gathers up your eleven pages, squares them, and hands them back.{/n} "Keep them. The vrock is still wrong. I shall think about it on the cart."''',
        c("[Take the pages.]")),
    nen("record_sent", '''"Your old entry says 'prospective follower'. I shall correct it."''', c("Continue", "record")),
    nen("record_kicked", '''"Your old entry says 'former follower'. I shall correct it."''', c("Continue", "record")),
], requires=(PRIMED_AWAY,), forbids=(RETURNED,), delay=48, places=("visitor", "arcade"),
    RequiresAnyGroups=[[SENT_AWAY, KICKED_OUT]], TricksterDevice=True, TricksterState="nenio.away")


# --- The commit: a question she did not mean to ask, a hypothesis, and her own test. ----------------------------------------

meet(P + "commit.hypothesis", "A space for a name", '"Go on. \'Crusade, Commander of the.\' I\'m ready."', [
    nar("open", '''{n}She is dictating the crusade. Not a battle, not a demon: the crusade itself, the whole unwieldy animal, for the letter C. She walks up and down in front of @DESK@ with her hands behind her back and her tail of papers trailing out of one sleeve, and you write.{/n}
{n}"Crusade, the. Fifth of that name. Composition: knights, priests, mercenaries, the desperate and the bored. Morale: variable. Commander of the..." She stops. "Leave a space," she says, as she always says, and you leave it, as you always do.{/n}
{n}Then she does not go on. She stands with one finger raised, as if she had been about to make a point and it had got away from her.{/n}''',
        c("Continue", "filed_q", requires=(NAME_GONE,)),
        c("Continue", "kept_q", forbids=(NAME_GONE, NAME_STAKED)),
        c("Continue", "staked_q", requires=(NAME_STAKED,), forbids=(NAME_GONE,))),
    nen("filed_q", '''"Why does my page keep a space for your name?" {n}She looks from the blank to you.{/n} "I filed it after we left the Enigma. It is gone. Yet whenever I dictate 'Commander', I tell you to leave room for it. I cannot fill the space. I keep checking its width."''',
        c("Continue", "unmeant")),
    nen("kept_q", '''"Why do I keep leaving room for you? I dictate 'Commander' and stop. The page would be perfectly legible without the blank." {n}She holds the pencil over it.{/n} "I put it there. Now I want to know why."''',
        c("Continue", "unmeant")),
    nen("unmeant", '''"That was meant to be a marginal note." {n}She looks at you with something close to alarm.{/n} "I did not intend to ask it aloud. A scientist of my standing does not ask the subject why the data are behaving strangely. The subject cannot know. The subject is the data."
{n}But she does not take the question back. She stands there with it, and waits.{/n}''',
        c('[Offer it as a hypothesis] "Hypothesis: I\'m relevant. You\'re the scientist. Test it."', "method"),
        c('[State it as fact] "Because you\'re in love with me, Nenio. It\'s obvious."', "dictated"),
        c('"I don\'t know. That\'s your department."', "dodge")),
    nen("dodge", '''"It is my department." {n}She says it with some bitterness.{/n} "Every department is my department. That is the trouble with writing everything down. Nobody else is ever responsible for anything."
{n}She looks at the space on the page, and then at you.{/n} "You have an opinion. You always have an opinion; you just keep it behind your teeth like a card. Put it on the table."''',
        c('[Offer it as a hypothesis] "Hypothesis: I\'m relevant. Test it."', "method"),
        c('[State it as fact] "You\'re in love with me. There. On the table."', "dictated"),
        c("[Keep the card behind your teeth.]", abort=True)),
    nen("dictated", '''"No." {n}She takes the pencil out of your hand, not roughly, and puts it behind her own ear.{/n}
"Conclusions are observed, follower, not dictated. You may dictate a great many things to me: where we march, whom we fight, when I may have supper. You may not dictate a result." {n}She squares the pages on @DESK@.{/n} "We will stop there for today. The entry is incomplete. So is the question."''',
        c("[Let her keep the pencil.]", abort=True)),
    nen("method", '''{n}Her whole face changes. It is the look she gets at the edge of a ruin nobody has catalogued: pure, undignified greed.{/n}
"A hypothesis. Yes. That, I can do something with." {n}She paces, fast, three steps each way.{/n} "Hypothesis: you are relevant. Method: tonight I forget everything else."
"Everything. I will sit in a room and stop thinking about the crusade, the Worldwound, demons, kings, weather, the war, supper, all of it, one thing at a time, the way I always do. Whatever is irrelevant will go. If you are still here in the morning, somebody will have to decide what that means, follower, and it will be me."''',
        c("Continue", "conditions")),
    nen("conditions", '''"Conditions." {n}She counts them off on her fingers.{/n} "You will not come near me tonight. You will not send me anything. You will not leave anything of yours where I might trip over it and be reminded. The control must be clean, or the result is worthless, and I refuse to run an experiment twice when once would have done."
{n}She hesitates.{/n} "And you will not be offended if the answer is 'damp'. Some things persist because they are important. Some things persist because they are damp. I shall be honest about which."''',
        c('[Leave her to it] "Clean. I\'ll keep away."', "clean", flags=(TEST, STARTED)),
        c("[Agree, and that night, while she sleeps over her notes, make sure she can't forget you: your initials in the margins of volume one, a sketch of your face folded into her sleeve.]",
          "tamper", flags=(TEST, STARTED, TAMPERED))),
    nen("clean", '''"Good." {n}She gathers her papers into her arms like a heap of laundry.{/n} "Go away now. You are already making it harder. I can hear you breathing."''',
        c("[Go away.]")),
    nar("tamper", '''{n}She agrees to your agreement, gathers her papers and goes. You give it an hour past the last lamp.{/n}
{n}Her door is not locked; she does not believe in locks, which she says are a confession that something is worth stealing. She is asleep at her table with her cheek on volume one and a pencil still in her fist. You work by the light from the corridor: your initials in a margin here, another there, small, in her own brown pencil. A little sketch of your own face, not a bad likeness, folded twice and slipped into her sleeve among the rest.{/n}
{n}If she forgets you tonight, you tell yourself, she will find you again in the morning. It is not cheating. It is a footnote.{/n}''',
        c("[Leave before she wakes.]")),
    nen("staked_q", '''"Your name is still here. I took it as a stake, and I have yet to finish filing it." {n}She taps her forehead, then the blank.{/n} "That accounts for the name. It does not account for this. Why do I keep making room for something I agreed to lose?"''',
        c("Continue", "unmeant")),
], requires=(STARTED, SCRIBE, MARGIN), forbids=(COMMITTED, TEST, DECLINED, REFUSED), delay=24)


meet(P + "commit.result", "What survived the night", '"So. What\'s left of the world?"', [
    nar("open", '''{n}Nenio has a list spread across @DESK@. She turns it toward you before you have finished your question.{/n}''',
        c("Continue", "void", requires=(TAMPERED,)),
        c("Continue", "clean", forbids=(TAMPERED,))),
    nen("clean", '''{n}Her eyes are red. The list runs onto the back of the sheet; she has been writing through the night.{/n}
"Report." {n}She reads without looking at the list.{/n} "Forgotten overnight, on purpose: the name of the Queen of Mendev, again; the eight arcane schools, which I shall have to look up, to my shame; the number of bones in a vrock's wing; the price of pepper in Drezen; a song my mother may have sung, if I had a mother, which is not established; four hundred and twelve minor facts about the Worldwound, which I regret; and tea."
"Retained: the Worldwound itself, because I cannot forget a thing I am writing about; the Encyclopedia; my own name; and you."''',
        c("Continue", "you")),
    nen("you", '''"Your face. Your equipment. The way you hold the sheet while I dictate. I can explain remembering useful observations. I spent an hour trying to remove you, between three and four in the morning. You kept returning."''',
        c("Continue", "decides")),
    nen("decides", '''{n}She unfolds a working note headed FOLLOWER: USEFUL, then puts it beside the overnight list.{/n} "That explanation was sufficient for hiring you. I am checking whether it still fits."''',
        c("Continue", "variable", forbids=("trickster.ever",)),
        c("Continue", "receipt_kiss", requires=(F + "pulse.kissed",), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "receipt_bite", requires=(F + "teeth.bitten",), forbids=(F + "pulse.kissed", UNREMEMBERED, RECREATED)),
        c("Continue", "receipt_scribe", forbids=(F + "pulse.kissed", F + "teeth.bitten", UNREMEMBERED, RECREATED)),
        c("Continue", "receipt_scribe", requires=(UNREMEMBERED,)),
        c("Continue", "receipt_scribe", requires=(RECREATED,), forbids=(UNREMEMBERED,))),
    nen("variable", '''{n}She puts the list aside and catches your wrist, checking the pulse with her thumb.{/n} "There it is again. I want a reading from both of us this time." {n}She moves closer, watching your mouth.{/n} "Tonight. My room. I intend to be in the experiment."''',
        c('[Accept her conclusion] "Then it\'s decided."', "tonight", flags=(COMMITTED, FIRST_NIGHT)),
        c("[Kiss her, and let that be the answer.]", "kissed", flags=(COMMITTED, FIRST_NIGHT)),
        c('[Refuse to be her conclusion] "No. I don\'t want to be your result, Nenio."', "refused", flags=(REFUSED, CLOSED)),
        c('"Enough experiments. Give me a final answer now."', "postponed")),
    nen("tonight", '''"Good. Decided." {n}She says it as if she were closing a book, and then, not at all as if she were closing a book:{/n} "Tonight, then. My room. Bring nothing. I have instruments."''',
        c("[Leave her to her list.]")),
    nar("kissed", '''{n}She pulls you closer by the wrist before your mouth reaches hers. Her hand closes in your shirt; she kisses you again as the list slides off @DESK@.{/n}
"Tonight," {n}she says against your mouth.{/n} "My room. Leave the list. I know what it says."''',
        c("[Leave her to her list.]")),
    nen("refused", '''{n}She takes it the way she takes a failed experiment: she writes it down.{/n}
"Noted. The subject declines to be the result." {n}Her pencil does not shake, quite.{/n} "That is permitted. Subjects are permitted to do all sorts of things. It is one of the great inconveniences of the field."
"Then I shall stop thinking about it." {n}She sits back down behind @DESK@.{/n} "It may take some time. Go away while it does."''',
        c("[Go.]")),
    nen("void", '''{n}Her hair is flattened against one cheek. Volume one lies open beside a sketch she has taken from her sleeve. Every mark has been circled.{/n}
{n}She holds up volume one, open, and turns it toward you. In the margin of page forty, very small, in her own brown pencil, are your initials. She turns to page two hundred and six. There they are again. Then she takes a folded sketch out of her sleeve, opens it, and lays it on the desk between you, face up. It is your face. It is not a bad likeness.{/n}
"Contaminated." {n}Her voice is perfectly level.{/n} "The result is void."''',
        c("Continue", "void_her")),
    nen("void_her", '''"I forgot you at a quarter past three. Completely. For a quarter of an hour the experiment was clean. Then I shifted in my sleep and found volume one under my cheek. Your initials were there. I remembered you, and now I cannot tell whether you would have returned without them." {n}She closes the book.{/n} "That was what I wanted to find out. You have spoiled the result."''',
        c('[Accept her ruling] "Then it\'s void."', flags=(DECLINED,)),
        c('[Lie] "Somebody else must have been in your room."', "lie", flags=(DECLINED,))),
    nen("lie", '''"Somebody else." {n}She looks at the sketch, and at you, with no expression whatever.{/n}
"Yes. Somebody else may have been in my room. I shall find out who. I am very good at finding things out; it is most of what I am." {n}She puts the sketch back in her sleeve.{/n} "The result is void either way."''',
        c("[Leave her with it.]")),
    nen("postponed", '''"No." {n}She takes her hand back and retrieves the list.{/n} "I proposed a working hypothesis. You heard an order you could issue. We stop here. When I decide to conclude, I shall tell you."''',
        c("[Leave her with the list.]", flags=(DECLINED,))),
    nen("receipt_kiss", '"The pulse trial: I kept holding your wrist after you kissed me. The watch was still running. No dictation to preserve; no measurement worth keeping." {n}She strikes through USEFUL.{/n} "A poor explanation. I wanted another kiss. I still do."', c("Continue", "variable")),
    nen("receipt_bite", '"The bite trial: I had the observation and still wanted your mouth near my arm. That does not improve an entry on teeth." {n}She strikes through USEFUL.{/n} "I wanted the further study for myself. I still do."', c("Continue", "variable")),
    nen("receipt_scribe", '"You accepted the pencil. That explains why I retained a follower while dictating. Last night I dictated nothing. You persisted anyway." {n}She strikes through USEFUL.{/n} "Employment does not account for that. Nor for wanting you here now, with no pencil."', c("Continue", "variable")),
], requires=(TEST,), forbids=(COMMITTED, DECLINED, REFUSED), delay=24)


meet(P + "commit.replication", "Replication", '"Nenio. About the margins."', [
    nar("open", '''{n}She has laid out the evidence on @DESK@ the way a magistrate would: volume one open at page forty, then at page two hundred and six, the folded sketch, and beside them three sheets of her own notes, dense with comparisons of pencil strokes. She has been at it for three days. You can tell because she has stopped wearing her hair up and is using the pencil for the notes instead.{/n}''',
        c("Continue", "asks")),
    nen("asks", '''"The pencil pressure matches yours. The sketch was folded to fit my sleeve. Whoever placed it knew where I kept my notes." {n}She looks up from the pages.{/n} "Did you do it?"''',
        c('[Confess] "Yes. I was afraid you\'d forget me. So I cheated."', "confessed"),
        c('[Deny it] "No. It wasn\'t me."', "denied")),
    nen("confessed", '''"Afraid I would forget you. That explains the initials. It does not make them evidence." {n}She gathers the marked pages.{/n} "No conclusion tonight. I will repeat the test. You will leave the book and the results alone. If I retain you without help, I shall decide what to do with you. If you want me to decide now, the study is over."''',
        c("[Leave the book and the decision with her.]", "night"),
        c('"You have my confession. That should be enough."', "terms_refused")),
    nar("night", '''{n}She ties a small bell to her door and puts the book inside. You leave her to the test. The bell remains still.{/n}''',
        c("[Leave her to the test.]", flags=(CONFESSED,)),
        c("Continue", "morning", forbids=("trickster.ever",))),
    nen("morning", '''{n}In the morning she is at @DESK@ with her list, exactly as before, but shorter.{/n}
"Replicated." {n}She taps the page.{/n} "The Queen's name went. The arcane schools went, again; I shall have to write them on my wrist. Tea went. You did not." {n}Her voice is not quite steady and she does not seem to mind this time.{/n} "Not at a quarter past three. Not at four. I tried very hard and you did not go. No margins, no sketches, no bell. Just you, being persistent, entirely without help."
"No margins. No sketches. You remained. I want the next observation to include both of us."''',
        c('[Accept her conclusion] "Then we\'re decided."', "yes", flags=(COMMITTED, FIRST_NIGHT, CONFESSED, REPLICATED)),
        c("[Kiss her, and let that be the answer.]", "yes_kiss", flags=(COMMITTED, FIRST_NIGHT, CONFESSED, REPLICATED)),
        c('[Refuse to be her conclusion] "No. Not after what I did."', "refused", flags=(REFUSED, CLOSED)),
        # Saved answer index 3, also copied to the visitor and arcade hosts.
        c("[Leave.]", forbids=("trickster.now",), abort=True)),
    nen("yes", '''"Decided." {n}She closes the book.{/n} "Tonight. My room. The bell has been removed. It turned out to be a very poor instrument for measuring what I wanted to measure."''',
        c("[Leave her to her list.]")),
    nar("yes_kiss", '''{n}She catches your wrist, then abandons the pulse to pull you close for another kiss.{/n} "Tonight. The bell is coming down."''',
        c("[Leave her to her list.]")),
    nen("refused", '''"That is not your decision to make for me." {n}Sharply, for her.{/n} "But it is your decision to make for you. Very well." {n}She writes something at the foot of the list and does not show it to you.{/n} "The study is closed. The data stand. They will always stand. That is the trouble with data."''',
        c("[Go.]")),
    nen("denied", '''{n}She writes one word on the top sheet. You cannot read it upside down; you cannot read it the right way up either. Then she stacks the evidence neatly, the sketch on top, and puts her hand flat on it.{/n}
"Then the result stays void. And so does the study." {n}Her voice is quite even.{/n} "I have always been able to forget what I decide is irrelevant, follower. This time I shall have to keep checking the decision. It will take me some time. You will not help it by being here."''',
        c("[Leave her.]", flags=(CLOSED,))),
    nen("terms_refused", '''"It is enough to identify the interference. It is not an answer to my question." {n}She closes the book on the sketch.{/n} "You still want to supply the result. I decline. Find somebody else's margins."''',
        c("[Go.]", flags=(CLOSED,))),
], requires=(DECLINED, TAMPERED), forbids=(COMMITTED, REFUSED), delay=72)


# The night: the room she requisitioned for the Encyclopedia. Stopwatch, the pulse counted aloud, the cut at the first motion.
visit(P + "night", "Night one", [
    nar("open", '''{n}She has taken a storeroom in the citadel for the Encyclopedia and told the quartermaster it was for the war effort, which he believed because she said it very loudly. There are planks across trestles along every wall.{/n}''',
        c("Continue", "shelves", forbids=(MANUSCRIPT, UNREMEMBERED)),
        c("Continue", "bare", requires=(MANUSCRIPT,)),
        c("Continue", "bare", requires=(UNREMEMBERED,), forbids=(MANUSCRIPT,))),
    nar("shelves", '''{n}On the planks, in their trunks, lie her notes: bundles of paper tied with string, labelled in a hand nobody can read, and at the end of the row volume one, her bound working draft.{/n}
{n}One candle. A cleared space on the floor with a blanket spread over it, and a cushion taken from somebody's chapel. On the nearest plank, in a row, as if for an examination: a stopwatch, a ruler, a pencil, a clean sheet headed NIGHT ONE.{/n}''',
        c("Continue", "friend_note", requires=(FRIEND_DONE,)),
        c("Continue", "begin", forbids=(FRIEND_DONE,))),
    nar("bare", '''{n}The planks are empty all along the walls, where the notes used to be, except one, where volume one lies on its own like the last tooth in a jaw, and beside it, in a row, as if for an examination: a stopwatch, a ruler, a pencil, a clean sheet headed NIGHT ONE. One candle. A blanket on the floor, and a cushion taken from somebody's chapel.{/n}''',
        c("Continue", "friend_note", requires=(FRIEND_DONE,)),
        c("Continue", "begin", forbids=(FRIEND_DONE,))),
    nar("friend_note", '''{n}She has left room beneath NIGHT ONE for a cross-reference.{/n}''',
        c("Continue", "begin", forbids=("trickster.ever",)),
        c("Continue", "friend_declined", requires=(FRIEND_DONE, FRIEND_REFUSED), forbids=(UNREMEMBERED, RECREATED)),
        c("Continue", "friend_drawing", requires=(FRIEND_DONE, FRIEND_SKETCH), forbids=(FRIEND_REFUSED, UNREMEMBERED, RECREATED)),
        c("Continue", "friend_uncertain", requires=(FRIEND_DONE,), forbids=(FRIEND_REFUSED, FRIEND_SKETCH, UNREMEMBERED, RECREATED)),
        c("Continue", "begin", requires=(UNREMEMBERED,)),
        c("Continue", "begin", requires=(RECREATED,), forbids=(UNREMEMBERED,)),
        c("Continue", "begin", forbids=(UNREMEMBERED, RECREATED, FRIEND_DONE))),
    nen("begin", '''{n}Nenio is sitting cross-legged on the blanket with the stopwatch in her hand. She has taken the pencil out of her hair, and her hair has come down, a great deal of it, dark and heavy, and she has plainly forgotten that it would.{/n}
"Sit. Here. No, closer. The instrument has a short range." {n}She holds the stopwatch up.{/n} "Baseline first. I will take your pulse at rest, and then not at rest. This is the follow-up to your hypothesis, conducted properly, with instruments. I have been designing it since the morning. The written accounts disagree. I have decided to investigate for myself. No dictation tonight; you would get ink on the blanket."''',
        c("[Sit close.]", "count"),
        c('[Flirt] "And your pulse? Who\'s measuring that?"', "hers")),
    nen("hers", '''"Nobody. That is the flaw in the design." {n}She takes your hand and puts two of your fingers on the inside of her own wrist, where the skin is thin and warm and very fast.{/n} "There. You are measuring it. Do not tell me the number. I will only argue with it."''',
        c("Continue", "count")),
    nar("count", '''{n}She finds your pulse at the wrist without looking, the way she finds a page. Her thumb settles on it. She starts the watch.{/n}
{n}"One. Two. Three." She counts aloud, low, in the voice she uses for measurements, and while she counts she looks at you, which she does not usually do; she usually looks at what she is writing. "Eleven. Twelve. You are fast." Her other hand, the one without the watch, goes to the collar of your shirt and undoes the top of it, and then the next, as if it were a page she needed to turn to go on reading.{/n}''',
        c("Continue", "tail", requires=(FOX_REVEALED,)),
        c("Continue", "no_tail", forbids=(FOX_REVEALED,))),
    nar("tail", '''{n}Something warm and soft slides across your forearm and wraps your wrist, once, twice, over her fingers. Her tail. She has let it out without seeming to decide to, the way people forget to hold in a breath; it is heavy and silky and it tightens when your pulse jumps, as if it were keeping count too.{/n}
{n}"Twenty," she says. "Twenty-one. Ignore the tail. It is not part of the apparatus. It is a confounding variable."{/n}''',
        c("Continue", "undress")),
    nar("no_tail", '''{n}Her fingers close around your wrist and stay there, cool at the tips and warm everywhere else, and tighten when your pulse jumps, as if they were keeping count on their own.{/n}
{n}"Twenty," she says. "Twenty-one. My hand is not part of the apparatus. Ignore it. It is a confounding variable."{/n}''',
        c("Continue", "undress")),
    nar("undress", '''{n}You draw her coat off her shoulders. Nenio frees one sleeve herself and drops it over the papers, then catches your hand at the buttons of her shirt. She guides it to the next one. Her count breaks when your mouth meets the circle on her bare shoulder.{/n}
"Thirty-four. Thirty..." {n}She pulls your face back toward hers.{/n} "Never mind. Come here."''',
        c("Continue", "lose")),
    nen("lose", '''{n}She kisses you in the middle of a number and presses you down onto the blanket. Her bare shoulder is warm beneath your hand; she catches that hand and draws it closer.{/n} "I am stopping the measurement." {n}Her breath breaks against your throat. She pushes the watch aside.{/n} "I want this. The number can wait."''',
        c("Continue", "watch")),
    nar("watch", '''{n}She leaves the watch on the blanket, still ticking, and neither of you reaches for it. She is over you, her hair falling around both your faces like a curtain around a lamp, her knees either side of your hips, pulling the last of your clothes away with more determination than skill, and she looks down at you the way she looks at a ruin nobody has catalogued: as if everything in it were about to be hers.{/n}
{n}"Night one," she says. "Beginning now."{/n}''',
        c("[Let the watch run down.]")),
    nar("friend_declined", '''{n}She writes: "SEE ALSO: FRIENDSHIP, POINT FIVE. PREVIOUS TRIAL DECLINED. PRESENT TRIAL: CHOSEN."{/n}''', c("Continue", "begin")),
    nar("friend_drawing", '''{n}She writes: "SEE ALSO: FRIENDSHIP, POINT FIVE. DOCUMENTATION REPLACED EXPERIMENT. NOT THIS TIME."{/n}''', c("Continue", "begin")),
    nar("friend_uncertain", '''{n}She writes: "SEE ALSO: FRIENDSHIP, POINT FIVE. PREVIOUS CONCLUSION REQUIRES FURTHER STUDY."{/n}''', c("Continue", "begin")),
], requires=(FIRST_NIGHT,), forbids=(P + "night",), delay=4, chapters=(3, 5), optional=False, Areas=[DREZEN])


meet(P + "morning", "Subject: [blank]", '"You left before I woke."', [
    nar("open", '''{n}Nenio is at @DESK@, dressed, her pencil back in her hair. The abandoned watch lies beside her notes. She rubs a stiff place in her neck, gets ink from her wrist onto her collar, and turns a sheet toward you.{/n} "A defective cushion. I shall requisition another. Look at this."''',
        c("Continue", "entry_filed", requires=(NAME_GONE,)),
        c("Continue", "entry_kept", forbids=(NAME_GONE,))),
    nar("entry_filed", '''{n}It is a private sheet, in the capitals she uses when she wants to be read. "SUBJECT: [          ]. STATUS: MINE." Under it, in her own illegible hand, a great deal more, and at the bottom, legible again: "Name not recoverable. Irrelevant. See above."{/n}''',
        c("Continue", "her")),
    nar("entry_kept", '''{n}It is a private sheet, in the capitals she uses when she wants to be read. "SUBJECT: [          ]. STATUS: MINE." Under it, in her own illegible hand, a great deal more, and at the bottom, legible again: "Name known. Withheld. The Encyclopedia does not print what it does not need."{/n}''',
        c("Continue", "her")),
    nen("her", '''"I left the blank on purpose. The name can stay out of this." {n}She taps STATUS: MINE.{/n} "The study continues. I shall need you here again. Frequently."
{n}A boot scrapes past outside. She turns the detailed observations face down before the door opens.{/n} "The quartermaster gets the requisition. Absalom gets the crusade. Neither gets this sheet."''',
        c('[Flirt] "What\'s in the illegible part?"', "illegible"),
        c('"Mine?"', "mine"),
        c("[Kiss the top of her head, over the pencil.]", "kiss")),
    nen("illegible", '''"Observations. Detailed ones." {n}She keeps her palm over the diagram.{/n} "I invented a notation during the night. It needs work. I shall correct it myself."
{n}She folds the sheet inward and slips it into her coat.{/n} "It stays with me. A printer would put it in a supplement, then ask me to label the diagram. I have no intention of doing either."''',
        c("Continue", "war")),
    nen("mine", '''"Yes. My study. I intend to repeat it." {n}She catches the front of your shirt and draws you down until her mouth brushes yours.{/n} "You may stop looking so pleased. The investigator has work to do."''',
        c("Continue", "war")),
    nen("kiss", '''{n}She tilts her face up before your kiss can land above the pencil. Her fingers catch your collar; she holds you there for another kiss, then releases you with a tug that straightens the cloth.{/n} "That observation requires replication. Later. The scouts are waiting."''',
        c("Continue", "war")),
    nen("war", '''{n}She turns the sheet back over and pulls another toward her, a map of the Worldwound's edge, dense with her notes.{/n}
"Now go and win your war. I have discovered that I would like it won." {n}She frowns, surprised at herself.{/n} "Not for the Encyclopedia. For no reason at all. I shall have to think about what that means. Later. There is a great deal to think about later, now."''',
        c("[Leave her to the map.]", flags=(P + "morning_after",))),
], requires=(P + "night", FIRST_NIGHT), delay=6)


# --- Epilogue pages (Owner NenioEpilogue; appended in authored order; no page effects). ------------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}She never had the Commander's name again. She called {mf|him|her} \"follower\" in private and \"the Commander\" in print, and when a Mendevian herald once shouted the name across a banqueting hall she turned round to see who was meant, and then turned back, perfectly content, and went on eating.{/n}", requires=(NAME_GONE,)),
    p("{n}She knew the Commander's name. She withheld it from the published proofs. When asked why, she said that the Encyclopedia did not print what it did not need, and that she did not need it; she had the original.{/n}", forbids=(NAME_GONE, UNREMEMBERED)),
    p("{n}She never recovered the notes the Commander had traded away for her. She rebuilt the missing entries around the bound working draft, observing everything a second time, in the Commander's hand. The new notes soon filled more trunks than the old ones. She made a point of mentioning this to the Faceless Sphinx, in writing, every year.{/n}", requires=(MANUSCRIPT,)),
    p("{n}Somewhere in the Enigma an answer is still owed. The Sphinx's servant never came to collect it during the war, and has not come since. The answer remained unpaid. The Sphinx had yet to name her question.{/n}", requires=(OWES,), forbids=DEBT_SETTLED),
    p("{n}The Sphinx's question was answered in full. She heard those words once, when the Commander answered the Sphinx's servant in front of her, and never again; they were no longer the Commander's to say. She noticed, and wrote down every other word instead, and said once that it made for a longer study and a better one.{/n}", requires=(DEBT_PAID,)),
    p("{n}The Sphinx's question was answered in her own coin: nothing at all. Nenio, who had watched it, laughed about it afterwards until she had to sit down, and then wrote to the Faceless Sphinx every year afterwards, asking whether she had enjoyed the silence, and never received a reply, which she said proved the point.{/n}", requires=(DEBT_EVADED,)),
    p("{n}The Sphinx took volume one for the Commander's unpaid answer. Nenio began it again from the letter A, in the Commander's hand, and made the Commander write the entry on Abadar twice, as a penance, because it was the entry nobody had asked for.{/n}", requires=(DEBT_DEFAULTED,)),
    p("{n}She never recovered the memory of Kenabres. She kept the Commander's account, including the line that named the killer. She had chosen to continue their work after reading it again. Whenever an editor tried to shorten the account, she restored that line herself.{/n}", requires=(UNREMEMBERED, KENABRES_TOLD), any_groups=(KENABRES_JUDGMENTS,)),
    p("{n}She never remembered Kenabres. The box she had drawn round the word in volume one stayed there, around an account of an arrest at a gate that fitted very neatly. Once in a great while, when she could not sleep, she opened the book at the flyleaf and looked at it, and the Commander, watching her, did not say anything.{/n}", requires=(UNREMEMBERED, KENABRES_LIED), forbids=(DEBT_DEFAULTED,)),
    p("{n}She never remembered Kenabres, or what had happened to her there. She kept the word in a box in the margin of volume one, and never opened it, and said that a box was a promise that the thing was still there.{/n}", requires=(UNREMEMBERED, KENABRES_SAID), forbids=(KENABRES_TOLD, KENABRES_LIED, DEBT_DEFAULTED)),
    p("{n}She never remembered the road to Drezen, or anything before it. She said once that a scholar who wakes on a road with one book and no past has two choices, to be frightened or to be interested, and that she had never once been able to manage the first.{/n}", requires=(UNREMEMBERED,), forbids=(KENABRES_SAID,)),
    p("{n}The probation was never lifted. Nenio extended it by a year every spring, at the author's discretion, and made the Commander say yes each time, out loud, with numbers.{/n}", requires=(DEMOTED,)),
    p("{n}She kept the sketch of the Commander's face that she had found in her sleeve. She had been angry about it. She kept it anyway, in volume one, at page forty, and when anyone asked about the initials in the margin she said they were a printer's error.{/n}", requires=(CONFESSED,), forbids=(DEBT_DEFAULTED,)),
    p("{n}Her entry on Areelu's work carried a list of the dead of Sarkoris as long as the entry itself. She put it there because a follower had once made her read it aloud, and she left it there because an entry without its costs was a sloppy entry. It did not soften a word of her admiration. Scholars in Absalom have been arguing for years about which half of the entry she meant.{/n}", requires=(ARCH_DEAD,)),
    p("{n}Her entry on Areelu's work remained the most admiring in the Encyclopedia. Scholars in Absalom walked out of her lectures over it, and she let them go, and went on, and never once apologised.{/n}", requires=(ARCH_AGREED,)),
    p("{n}Her entry on Areelu's work has a footnote longer than the entry, in a legible hand, listing every Sarkorian town by name. Nobody knows who wrote it. Nenio claimed it was a printer's error, too.{/n}", requires=(ARCH_TRICK,)),
    p('{n}On her return she unfolded the slip from their wartime study. "When this war is over, what do you want?" This time the Commander had an answer. She listened without reaching for a pencil, then said, "Good. I have a question about that as well."{/n}', requires=(F + "longitudinal.ask_after",)),
)
# Sol r4 INT: epilogues bypass UnavailableFlags; each living page guards every loss, lifted only by her Trickster return.

LOSSES = (DEAD, KILLED, SENT_AWAY, KICKED_OUT)

LOSS_BACK = {k: RETURNED for k in LOSSES}



SCENES.append(scene(P + "epilogue.article", "", "NenioEpilogue", 6, "", [
    nar("page", '''{n}After her research journeys, Nenio returned to the Commander with a bundle of proofs and fresh errors to correct. The legible hand was still useful. She put the first proof down, caught the Commander\'s collar, and kissed {mf|him|her} before beginning dictation.{/n}
{n}Her account now contained forty pages on the Fifth Crusade and nine pages of footnotes. None contained the folded diagram she kept inside her coat. When a publisher asked for more personal material, she sent six pages on vrock teeth. The Commander helped correct those too.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, DISSOLVED, "sacrifice", *LOSSES),
    ForbidOverrides={"sacrifice": "trickster.commander_back", **LOSS_BACK}, **EP))

# AUTHORED late encounter: the appended slot owns the cut and morning.
# The legacy page exit remains inert; readers may continue through the new answer.
SCENES.append(scene(P + "epilogue.commit", "", "NenioEpilogue", 6, "", [
    nar("page", '''{n}On her return, Nenio brought the Commander the result of their unfinished experiment. "Retained," she announced. "I repeated the test. The other entries required corrections. Yours required a visit." She put down the sheet and caught the Commander's collar for a kiss. "I want you. Now."{/n}
{n}Inside, she dropped her coat on a chair. The Commander unfastened her shirt; Nenio drew {mf|him|her} closer, then moved the candle beyond reach. "Fire would spoil the result." She backed toward the bed, pulling the Commander with her. The pencil rolled under the chair; she left it there.{/n}
{n}In the morning the stopwatch lay beside the observations. "No duration recorded," she said. "We shall have to repeat it." She pressed the Commander's hand against her waist. "Stay." Her new sheet began "Subject: Commander. Study ongoing". She folded it into her coat before leaving, then came back for the pencil beneath the chair — and another kiss.{/n}''',
        paragraphs=(
            p("{n}She still did not have the Commander's name. She said the door had been the right one anyway, which was more than could be said for most names.{/n}", requires=(NAME_GONE,)),
            p("{n}Volume one came with her. It was the only volume she had left, and she put it on the Commander's shelf as if she had always meant it to live there.{/n}", any_groups=(twin_ids(F + "volume_one"),), forbids=(DEBT_DEFAULTED,)),
            *KEPT_PARAS[2:],
        ))],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMMITTED, CLOSED, DECLINED, REFUSED, DISSOLVED, "sacrifice", *LOSSES),
    ForbidOverrides={"sacrifice": "trickster.commander_back", **LOSS_BACK}, **EP))

SCENES.append(scene(P + "epilogue.void", "", "NenioEpilogue", 6, "", [
    nar("page", '''{n}Nenio's account of the Fifth Crusade went to the printers. Her private study had no conclusion.{/n}''', paragraphs=(
            p('{n}Nenio never concluded. The Encyclopedia Golarionnica contains an entry on the Commander of the Fifth Crusade, cross-referenced to "forgetting, deliberate, method of", which ends: "Result void. Replication pending. See margin."{/n}\n{n}There is nothing written in the margin. In every copy she ever supervised, the margin is left clean, and the printers were given strict instructions to leave it so, and never told why.{/n}', requires=(TAMPERED,)),
            p('{n}Beside the last observation she wrote "insufficient data". The publisher asked her to remove the blank beneath it. She refused, and sent a corrected proof with more room.{/n}', forbids=(TAMPERED,)),
        ))],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED, DISSOLVED, *LOSSES), ForbidOverrides=dict(LOSS_BACK), **EP))

SCENES.append(scene(P + "epilogue.closed", "", "NenioEpilogue", 6, "", [
    nar("page", '''{n}When their work together ended, Nenio took her papers to Absalom. Her account of the Fifth Crusade was thorough, admiring, and impersonal. She corrected the proofs herself, including the entries she no longer discussed with the Commander.{/n}''',
        paragraphs=(
            p("{n}Under \"Crusade, Commander of the\", there is a name. It is spelled correctly. She checked the spelling herself before returning the proof.{/n}", forbids=(NAME_GONE,)),
            p("{n}Under \"Crusade, Commander of the\", there is a blank, carefully ruled. Editors in Absalom have tried three times to fill it in. Each time the proofs came back from the author with the name struck out and the blank restored, and a note in the margin: \"Not recoverable. Leave it.\"{/n}", requires=(NAME_GONE,)),
            p("{n}The private study remained among her papers. Beneath its last observation she wrote \"concluded\", and declined to give the publisher an explanation. She did not resume it.{/n}", requires=(COMMITTED,)),
        ))],
    requires=("trickster.ever", STARTED, CLOSED), forbids=(DISSOLVED, *LOSSES), ForbidOverrides=dict(LOSS_BACK), **EP))


# --- Reactions: Sosiel and Anevia (ledger 05 §3.1 row 32; the build sheet). -------------------------------------------------

SCENES.append(reaction("Sosiel", P + "react.sosiel_point_five", (P + "night",),
    '''{n}Sosiel has his sketchbook open on his knee, and he closes it rather quickly when he sees you.{/n}
"Nenio came to me yesterday for a professional opinion. She had a drawing she wanted checked for proportion. I told her I paint landscapes and Shelyn's saints, mostly, and she said the principles were the same and the subject was less holy." {n}He clears his throat.{/n}
"I checked it. It was very good. It was also you. I said so. She said 'correct' and took it back and went away humming." {n}A slow smile.{/n} "She had drawn every crease in the blanket, then asked whether the figure was recognisable. I told her the proportions needed work. She asked which ones, and made me point. I think she intends to redraw it. You might want to ask her where she plans to keep the drawing."''',
    answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=3, last=5, Chapters=[3, 5],
    entry='"You look as though you\'ve seen something."', portrait="Sosiel", delay=12))

SCENES.append(reaction("Anevia", P + "react.anevia_gate", (RETURNED, KILLED),
    '''"The gate log says: Nenio, kitsune, scientist, came in on the south road at the change of the watch." {n}Anevia taps the ledger with one finger.{/n}
"The last entry under that name in anybody's log is a burial detail. Kenabres. Your name's on it, Commander. I was there when they wrote it; there wasn't much of Kenabres left to write on." {n}She looks at you for a while without saying anything.{/n}
"She doesn't know you. I asked her, at the gate, just to see. She said she'd never met the Commander and hoped the experience would be educational. I've read that burial line three times this week. It hasn't changed. Neither has she."''',
    answer_list=ANEVIA_HUB, forbids=("anevia_gone",), ForbidOverrides={"anevia_gone": "anevia.trickster.returned"},
    chapter=3, last=5, Chapters=[3, 5], entry='"Anything odd at the gate?"', portrait="Anevia"))


SCENES.append(reaction("Sosiel", P + "react.sosiel_no_name", (NAME_FILED,),
    '''"Nenio asked me to paint your portrait." {n}Sosiel turns a brush over in his fingers.{/n} "Just your face. Small, for the frontispiece of an entry. Under it she wants a blank plate, gilded."
"She said you staked it on a riddle in the Enigma. Afterwards she filed it, and now she wants the blank painted as carefully as your face." {n}He turns the brush between his fingers.{/n} "I offered an inscription. She asked for more gold on the empty plate."''',
    answer_list=SOSIEL_HUB, forbids=("sosiel.dead", "sosiel.kicked_out"), chapter=5, last=5, Chapters=[5],
    entry='"Have you talked to Nenio lately?"', portrait="Sosiel", delay=12))



# Reviewed polish: Nenio concludes a clean postponement on her own initiative.
meet(P + "commit.review", "A conclusion without instructions", '"Have you finished with the list?"', [
    nen("open", '''{n}Nenio places the same list on @DESK@. Beside 'relevant' she has written 'retained'.{/n} "I have finished. Without instructions from the subject. I want you in my room tonight. The list stays here."''',
        c('"Then tonight. Your conclusion."', "yes", flags=(COMMITTED, FIRST_NIGHT)),
        c("[Kiss her.]", "kissed", flags=(COMMITTED, FIRST_NIGHT)),
        c('"No. I do not want this."', "no", flags=(REFUSED, CLOSED))),
    nen("yes", '"Correct. Bring yourself. I have everything else."', c("[Leave her to her work.]")),
    nen("kissed", '''{n}She catches your collar and keeps you close for a second kiss. The list stays untouched.{/n} "Tonight. I have work to finish first."''', c("[Leave her to her work.]")),
    nen("no", '''"Then the study ends here." {n}She writes beneath the last entry and folds the sheet away.{/n} "The result stands. The invitation does not."''', c("[Leave her to her work.]")),
], requires=(STARTED, DECLINED), forbids=(COMMITTED, REFUSED, TAMPERED, KENABRES_PENDING), delay=72)

# The clean repeat has finished before the next physical contact can offer a yes.
_replication = next(s for s in SCENES if s["Id"] == P + "commit.replication")
_repeat_nodes = []
for _node in _replication["Nodes"]:
    if _node["Id"] not in ("morning", "yes", "yes_kiss", "refused"):
        continue
    _text = _node["Text"]
    for _token, _value in PLACES["hub"]["texts"].items():
        _text = _text.replace(_value, _token)
    _repeat_nodes.append(dict(_node, Text=_text))
meet(P + "commit.replication_result", "The clean repeat", '"What remained this time?"', _repeat_nodes,
     requires=(STARTED, DECLINED, TAMPERED, CONFESSED), forbids=(COMMITTED, REFUSED, KENABRES_PENDING), delay=24)

SCENES.append(scene(P + "epilogue.kenabres_pending", "", "NenioEpilogue", 6, "", [
    nar("page", '''{n}Nenio kept the account of her death beside her notes on the Fifth Crusade. She compared dates and handwriting, asked questions, and supplied no private conclusion. When the Commander asked about their study, she returned to the account and said she had not finished examining it.{/n}''')],
    requires=("trickster.ever", KENABRES_PENDING), forbids=(CLOSED, DISSOLVED, "sacrifice", *LOSSES),
    ForbidOverrides={"sacrifice": "trickster.commander_back", **LOSS_BACK}, **EP))

# Pending testimony pauses romantic conclusions, while ordinary dictation stays open.
for _consumer in SCENES:
    if _consumer["Id"].startswith(tuple(P + stem for stem in (
            "commit.hypothesis", "commit.result", "commit.review", "commit.replication_result", "night",
            "epilogue.article", "epilogue.commit"))):
        _consumer["Forbids"] = list(dict.fromkeys([*_consumer.get("Forbids", []), KENABRES_PENDING]))


# --- Registration helpers ------------------------------------------------------------------------------------------------

household.secret("nenio_kenabres", "An arrest at the gate",
                 "She asked me what happened in Kenabres, where the Sphinx's servant says I ended her mission and she does not "
                 "remember it. I told her she was arrested at the gate and that I did not help. She wrote it beside the box in "
                 "her volume one. It fits very neatly. Anevia keeps a gate log with her burial line in it.",
                 portrait="Nenio", witnesses=("nenio",), risk="medium")

# Three native keys the build sheet names that no other route reads yet (checked in blueprints.zip and enGB), and the kitsune
# reveal that decides whether her tail is in the night scene.
NATIVE = {
    "SeenCues": {FOX_ARGUED: [FOX_ONE], FOX_REVEALED: ["5db28e499fd812848b92d6ac7b26e234"],
                 ENIGMA_RESOLVED: ["c214b2d290676f344a9227a2711393a6"],
                 POETRY_FAILED: ["3f9250674b4b8964583cd43c1dc2b7c4"],
                 GOSSIP_PREPARED: ["1c227b4093d74df489234b8e541a8b3e", "54ce8fab48409ca4eac54c02e95c6c71"],
                 GOSSIP_UNIVERSAL: ["54ce8fab48409ca4eac54c02e95c6c71"],
                 BROUGHT_SAFE: ["2cf370e2b4cdba2418ce7473ea858764"],
                 RECRUITMENT_REFUSED: ["8735d2087d3723b47b3692ea9dfa16df"],
                 FRIEND_SKETCH: ["9684eade0e1c5f043a3c780b1f644de5", "caecc9b04ee4bb940a165251c7b6054c",
                                 "35e565c7dac6c714e973cafc50942fde", "c1390044127cbbf428e7fb96cde940dc"],
                 FRIEND_TONGUE: ["caecc9b04ee4bb940a165251c7b6054c"],
                 FRIEND_CREDIT: ["c1390044127cbbf428e7fb96cde940dc"],
                 FRIEND_REFUSED: ["b95a7017fd1cc6b40a23b9e7e9c54c88"]},
    "SelectedAnswers": {ASKED_FORGETTING: "ece25c57e50c9e0458c6cd47a143d8fe", ASKED_GIFT: "9763b3f979b4cce449e5ca1d28f50eed",

                        TOLD_BITE: "20a557207800252419c55049322943c4"},
}

DERIVED = {
    VISITOR: [[RECREATED], [UNREMEMBERED], [PRIMED_AWAY]],
    # Filing is completed by after_enigma, after the native thanks.
    NAME_GONE: [[NAME_FILED]],
    KENABRES_PENDING: [[KENABRES_TOLD]],
    LATE_COMMITTED: [["trickster.ever", STARTED]],
    BODY_KEPT: [["revive.nenio.available"]],
    # 05 §2.5 voice note: she joins, and she will want a control group.
    "nenio.harem.voice.principal_investigator": [[COMMITTED]],
}


def margin_groups():
    """MARGIN: any dictation session after the first (every place twin), the talk after the Enigma, or the first session of a
    returned scholar: the space for the name has been left more than once."""
    from storylines import nenio_folios
    ids = [s["Id"] for s in nenio_folios.SCENES if s["Id"] not in nenio_folios.FIRST_IDS and not s.get("Reaction")
           and not s["Owner"].endswith("Epilogue")]
    ids += [s["Id"] for s in SCENES if s["Id"].startswith((P + "after_enigma", P + "dead.welcome_back", P + "dead.market",
                                                             P + "killed.stranger", P + "away.correction"))]
    return [[i] for i in dict.fromkeys(ids)]


def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register her derived keys, presences, revival and the native keys only this route reads. Scenes are added by expansion.py."""
    derived = dict(DERIVED)
    derived[MARGIN] = margin_groups()
    for key, groups in derived.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("DerivedForbids", {})[KENABRES_PENDING] = [CLOSED, *KENABRES_JUDGMENTS]
    for kind, table in NATIVE.items():
        _bind(payload, kind, table)
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    revivals = payload.setdefault("Revivals", {})
    if "nenio" in revivals and revivals["nenio"] != REVIVALS["nenio"]:
        raise ValueError("Conflicting revival: nenio")
    revivals.update({k: dict(v) for k, v in REVIVALS.items()})
    # eng7-f3: authored research visit, not companion recruitment or a romance window.
    # ThresholdOutdoor (10c4b0e2...) and the camp's Arsinoe anchor are native:
    # World/Areas/Act_6_Threshold/ThresholdOutdoor/ThresholdOutdoor.jbp;
    # World/Encounters/ThresholdOutdoor/ConditionsHolders/Arsinoe_Camp_Conditions01/02.jbp.
    # A returned scholar follows the impossible shadow to the siege camp to measure it.
    # Only Nocticula's existing earned reaction is attached; the Drezen windows stay intact.
    reaction_id = "nocticula.trickster.reaction.nenio"
    reaction_scene = next(s for s in payload["Scenes"] if s["Id"] == reaction_id)
    payload["Presences"]["nenio.presence.threshold"] = dict(
        Unit=COPY_UNIT, Area="10c4b0e2af186ba46ab4d238d00a40a8", Mode="spawn-copy",
        At=dict(NearUnit="a609ed9b2205d034bb3bb04d2a255681", Side="right", Distance=2.5),
        Requires=list(dict.fromkeys(("trickster.ever", VISITOR, RETURNED, *reaction_scene["Requires"]))),
        Forbids=[CLOSED, DISSOLVED, reaction_id, "sacrifice"], MinChapter=6, MaxChapter=6,
        AnswerLists=[], Dialog="hub", ReactionScenes=[reaction_id],
        Greeting=('{n}Nenio has wedged her folio beneath a stone beside the camp stores. The wind off Threshold '
                  'keeps lifting its pages.{/n} "The fortifications can wait. I came to measure the Wound. Stand still."'))
    # end eng7-f3
    # eng8-q8e begin: authored return replaces only the incompatible no-friend slide.
    from storylines.native_overrides import register_legacy
    register_legacy(payload, __name__, edits={
        "b6c0fb4c102cfb84f83a772e2dbb8a14": dict(Page="f1b5cd57aa76be44b9f754a208854ee7",
            Sequence="fec3b6f28610c8a48a239f148ed3ed60", Key="185ff9f7-34e0-4806-83fd-9df14b95e269",
            Replacement=P + "epilogue.native_commit", When=[["trickster.now", LATE_COMMITTED]],
            KeepNativeImage=False, Variants=[dict(Replacement=P + "epilogue.native_article",
                When=[["trickster.now", COMMITTED]], KeepNativeImage=False)])})
    # eng8-q8e end


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'nenio.trickster.away.correction_arcade',
    'nenio.trickster.away.correction_visitor',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
# eng8-q8d: the night is a physical visit on her companion/visitor hubs.
# Keep the original night ID and append only the two placement twins.
_eng8_night = next(s for s in SCENES if s['Id'] == P + 'night')
_eng8_nights = []
meet(_eng8_night['Id'], _eng8_night['Title'], '[Go with Nenio to her room.]', _eng8_night['Nodes'],
     requires=(FIRST_NIGHT,), forbids=(P + 'night', KENABRES_PENDING), delay=4, optional=False, into=_eng8_nights)
_eng8_night.clear()
_eng8_night.update(_eng8_nights[0])
for _eng8_twin in _eng8_nights[1:]:
    for _eng8_node in _eng8_twin['Nodes']:
        for _eng8_choice in _eng8_node['Choices']:
            if not _eng8_choice.get('Next') and not _eng8_choice.get('Abort'):
                _eng8_choice['Set'] = list(dict.fromkeys(_eng8_choice['Set'] + [P + 'night']))
    SCENES.append(_eng8_twin)
# end eng8-q8d


# eng8-q8e begin: E14 one-node slides reuse the authored return, without paragraph appenders.
NATIVE_ENDING_SCENES = []
for _ending_suffix in ("commit", "article"):
    import copy as _ending_copy
    _original = next(s for s in SCENES if s["Id"] == P + "epilogue." + _ending_suffix)
    _slide = _ending_copy.deepcopy(_original)
    _slide["Id"] = P + "epilogue.native_" + _ending_suffix
    _slide["Nodes"][0].pop("Paragraphs", None)
    NATIVE_ENDING_SCENES.append(_slide)
# eng8-q8e end
# eng8-q8h begin: proposing the existing experiment is pursuit; employment is not.
DERIVED[LATE_COMMITTED] = [["trickster.ever", TEST]]
SCENES.insert(next(i for i, s in enumerate(SCENES) if s["Id"] == P + "epilogue.closed") + 1, scene(P + "epilogue.scholar", "", "NenioEpilogue", 6, "", [
    nar("page", '{n}After the war Nenio set out with a trunk of notes on the Fifth Crusade. She sent the Commander proofs from Absalom, with errors marked and corrections demanded. The Encyclopedia Golarionnica grew by three supplements before its first volume reached the printers.{/n}')
], requires=("trickster.ever", STARTED),
   forbids=(COMMITTED, CLOSED, DECLINED, REFUSED, TEST, DISSOLVED, "sacrifice", *LOSSES),
   ForbidOverrides={"sacrifice": "trickster.commander_back", **LOSS_BACK}, **EP))
# end eng8-q8h

# Round 2 AUTHORED situation staging. Save IDs and old terminal answers stay
# in place. New slot destinations/choices append; no flags arise from slots.
for _physical in SCENES:
    if _physical["Id"].startswith(tuple(P + stem for stem in (
            "commit.hypothesis", "commit.result", "commit.review",
            "commit.replication", "night", "morning"))):
        _physical["Areas"] = [DREZEN]
    if _physical["Id"] in twin_ids(P + "night"):
        _watch = next(node for node in _physical["Nodes"] if node["Id"] == "watch")
        _slot_id = _physical["Id"] + ".explicit.1"
        # Brief: Nenio abandons measurement for her first chosen encounter.
        _cut = '{n}Still astride you, Nenio bends to kiss you. Her hands settle on your shoulders; she holds you close as the kiss deepens. The watch keeps ticking beside the blanket.{/n} "Leave it. I want you here."'
        import copy as _slot_copy
        _exit = _slot_copy.deepcopy(_watch["Choices"][0])
        _watch["Choices"][0]["Forbids"] = list(dict.fromkeys([*_watch["Choices"][0]["Forbids"], "trickster.ever"]))
        _watch["Choices"].append(c("Continue", _slot_id))
        _physical["Nodes"].append(nar(_slot_id, _cut, _exit))


# Round 3: append a real slot without changing the saved ending exit.
_late = next(s for s in SCENES if s["Id"] == P + "epilogue.commit")
_page = _late["Nodes"][0]
_buildup, _morning = _page["Text"].rsplit("\n", 1)
_page["Text"] = _buildup
_page["Choices"][0]["Id"] = "continue"
_late_slot = P + "epilogue.commit.explicit.1"
_page["Choices"].append(c("[Read on.]", _late_slot))
# Brief: first chosen encounter after her return; third-person past narration.
_late_cut = ('{n}Nenio sat on the bed and drew the Commander down beside her. '
             'She caught {mf|his|her} face in both hands and kissed {mf|him|her} again, '
             'then pulled {mf|him|her} close enough that neither could reach the notes.{/n} '
             '"The library can wait until morning."')
_late["Nodes"].append(nar(_late_slot, _late_cut, c("Continue", "morning_after")))
_late["Nodes"].append(nar("morning_after", _morning))

# Native public summary and supplementary private consequence are different
# passages. No extra suppression/edit, ending gate, or saved exit is introduced.
for _slide in NATIVE_ENDING_SCENES:
    if _slide["Id"] == P + "epilogue.native_article":
        _slide["Nodes"][0]["Text"] = ('{n}The Encyclopedia Golarionnica carried Nenio\'s account of the Fifth Crusade: '
            'forty pages, nine of them footnotes. She sent the proofs to the Commander for corrections, '
            'then left on another research journey. The publisher received no private observations.{/n}')
    else:
        # Public continuation of the native journey; the supplementary page
        # owns the private result and first night, so neither is replayed.
        _slide["Nodes"][0]["Text"] = ('{n}Nenio set out after the war to measure how long it took to visit '
            'the nations of Golarion. Eighteen months later she returned with a pile of notes for her follower. '
            'Among them was the completed result of a private experiment begun during the Fifth Crusade. '
            'That sheet did not go to the publisher.{/n}')
