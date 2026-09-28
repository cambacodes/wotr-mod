"""Camellia on the Trickster path: "Go on, then. Die convincingly." (Writer/handoffs/trickster/camellia.md; family F12,
the spoken death).

Canon: Camellia Gwerm, spirit shaman, Horgus's illegitimate daughter, who kills only those who considered her a friend,
"so that I can see the disbelief and dread in my victims' eyes" (FinalTruth/Cue_0042 f53d2eeb), and who tells the Commander
at the end of her lies: "You are an excellent liar, perhaps even better than I am" (Cue_0029 b5485676). Her spirit Mireya is
her own invention (Cue_0012 6aa5270c: "There is no Mireya. I made her up."; hub Cue_0107 1b515274). The Trickster's words
become true (Kyado Cue_0109 509eac82; CalebFooled 25d3d486). At the moment the Commander turns on her, the joke makes her
death a performance: she dies, is buried, and walks back into Drezen veiled, calling herself Mireya.

This relationship is a native adapter: it reads CamelliaRomance (89f8c2f1) and never starts or completes it. Her life with
the Commander before the kill, the days between her return and her price, and the life after her answer are camellia_masks.
Authored and labelled as authored: the performed death, the veiled mourner, the grave, its sexton and its lid.
"""
import copy

from story_format import c, n, p, reaction, scene

SCENES = []
REL = "camellia"
P = "camellia.trickster."
UNIT = "397b090721c41044ea3220445300e1b8"         # Camelia_Companion (her companion blueprint; the presence copy)
HUB_LIST = "589d83230bbbfd04bb1220ee4fef1ce1"     # Dialgoue_CameliaMain/AnswersList_0030 (her companion root hub)
DREZEN = "2570015799edf594daf2f076f2f975d8"       # DrezenCapital
FYE = "0f12118177d102f428a3b30b15b132eb"          # Fye_Bartender, the Drezen tavern keeper (E12b anchor)
KILL_LIST = "74f66c9edaa71a644ba091fb1ff4a435"    # Camelia/AnswersList_0045, after Answer_0043 "I cannot tolerate your atrocities"
KILL_RETURN = "6f6ceeffe5e77dc42896e3e8b937b752"  # Camelia/Cue_0044 "This is not how I imagined our friendship would end."
KILL_NEXT = "e433ac35761daa84b86b6b5e5c4fae11"    # Camelia/Cue_0049 "You want to take my life? Go ahead and try!" (Unrecruit)
Q3_LIST = "2199689753593844a8caceef5150ff4e"      # FinalTruth/AnswersList_0039 (the verdict)
Q3_RETURN = "1d0757c2ccde7034baa737419150bacd"    # FinalTruth/Cue_0031 "So, what is your verdict, my friend?"
Q3_NEXT = "be5af575d343fdb49badcd32d8336996"      # FinalTruth/Cue_0047 "Well, you can give it a try, my friend!"
Q1_LIST = "d977fae7974bb88419e51e2c33876aac"      # Q1_NobleIntent/AneviaResults/AnswersList_0002
Q1_RETURN = "794e654ae10d09d41860cf90335f0244"    # AneviaResults/Cue_0001 "Well, Commander? Have you solved the problem?"
Q1_NEXT = "6d583904c4659fe478c2e26e9305ad4d"      # AneviaResults/Cue_0009 "If that's your decision - then gladly."
ANEVIA_LIST = "33960c7f7af40cd43b7f801a76c87a0b"  # NPC_Common/Anevia/AnswersList_0003
REGILL_LIST = "2366a8db6481070439fee222c0c52e45"  # CompanionDialogues/Regill/AnswersList_0002

STARTED = "camellia.started"
CLOSED = "camellia.closed"
COMMITTED = "camellia.committed"
KILLED = "camellia.killed"
DEAD = "camellia.dead"
KICKED = "camellia.kicked_out"
ROMANCE = "camellia.romance"                      # CamelliaRomance (read only)
PRIMED = P + "primed"
BY_ORDER = P + "primed_by_order"
RET = P + "returned"
DECLINED = P + "declined"
TERMS = P + "terms_named"
LATE = P + "cost.late"
KNOWS = P + "cost.knows_you_tried"
OWED = P + "cost.spirits_owed"
INVESTIGATED = P + "cost.investigated"
COVERED = P + "cost.covered_murder"
ACCOMPLICE = P + "cost.accomplice"
MARKED = P + "cost.marked"
OATH_FED = P + "cost.oath_fed"
GUARD = P + "cost.called_guard"
TAME = P + "cost.asked_her_tame"
LOOPHOLE = P + "oath_loophole"
THREATENED = P + "oath_threatened"
PRESENCE = "camellia.presence"
PRESENCE_FAILED = PRESENCE + ".failed"
PERFORMANCE = P + "killed.performance"

# The life before the kill (camellia_masks), read by the return, her price, her test and the pages.
GAME = P + "masks.game"                   # two lies and a truth, played
OUT_LIED = P + "masks.out_lied"           # the Commander won her game
NAMED = P + "masks.named_spirit"          # the Commander offered her spirit a name
QUIET = P + "masks.quieted"               # the Commander talked the voices down in the Abyss
FUNERAL = P + "masks.funeral_promised"    # the wrong lilies, promised
DANCED = P + "masks.danced"               # the dance, and the knife she wore to it
SHE_WON = P + "masks.she_won"             # she won her game
NAME_LEFT = P + "masks.name_left"         # the Commander left Mireya her name
INVENTED = P + "masks.invented_friend"    # the Commander made up a friend for her, on the spot
FED = P + "masks.voices_fed"              # in the Abyss, the Commander sent her to bleed demons
OUTLIVE = P + "masks.outlive_promised"    # "I'd rather you didn't need one"
KNIFE_NOTICED = P + "masks.knife_noticed"  # the Commander named, or lifted, the knife she danced with
# The days after the return (camellia_masks).
GRAVE = P + "beat.grave"                  # she took the Commander to her grave (killed)
DUE = P + "beat.spirits_due"              # she named the spirits' due (dead otherwise)
LESSON = P + "beat.lesson"                # where a friend would stand
STEADY = P + "lesson.steady"
FLINCHED = P + "lesson.flinched"
# After her answer (camellia_masks).
SHELF = P + "bond.shelf"
LIST_KEPT = P + "bond.list_kept"
LIST_BURNED = P + "bond.list_burned"
WITNESS_LIED = P + "bond.witness_lied"
WITNESS_HERS = P + "cost.witness"
NOT_TODAY = P + "bond.not_today"
TOUCHED = P + "salle.touched"            # the Commander scored the touch she wanted, by lying with the whole body
PRISONER_HERS = P + "cost.prisoner"      # the Commander let her have the prisoner in the cells
PRISONER_SPARED = P + "prisoner_spared"  # the Commander sent the prisoner to trial instead
NEW_NAME = P + "gift.new_name"           # the Commander gave her papers as Mireya Voss
OLD_NAME = P + "gift.her_stone"          # the Commander gave her a rubbing of her own gravestone
BOWL_HELD = P + "masks.bowl_held"        # the Commander held Mireya's bowl, or said grace over it
AMULET_KEPT = P + "amulet_kept"          # she gave the Commander the amulet of a spirit she never had
UNMASKED = "camellia.mireya_unmasked"    # FinalTruth/Cue_0012 seen: "There is no Mireya. I made her up."
FRIEND_WARNED = P + "friend.warned"      # the Commander frightened her new friend away with a lie
FRIEND_WATCHED = P + "cost.friend_kept"  # the Commander let the friendship run, and watches

GONE = (KILLED, DEAD, KICKED)
REGILL_GONE = ("regill.dead", "regill.kicked_out", "regill.left_plot")

RELATIONSHIP = dict(
    Title="A dead woman's hand",
    Description=("Camellia is officially dead. The crusade buried her under a plain stone with the wrong flowers. She is "
                 "not staying that way on my account, she says, and she has not said on whose."),
    Objective="Answer Camellia",
    Guidance=("On the Trickster path, when you turn on Camellia, tell her to die convincingly. If her body fell some other "
              "way, tell it that it's overacting. A veiled woman may then ask for you at the end of Fye's bar in Drezen. "
              "Camellia chooses the hour."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[KILLED, DEAD, KICKED], FailureFlags=[],
    UnavailableOverrides={KILLED: RET, DEAD: RET},
    TricksterAccess={
        "killed_by_commander": dict(detect=[KILLED, DEAD], device=PERFORMANCE, returned=RET),
        "dead_otherwise": dict(detect=[DEAD, "!" + KILLED], device=P + "dead.overacting", returned=RET),
    },
)
REVIVALS = {"camellia": dict(Relationship=REL, Unit=UNIT, DeathFlag=DEAD)}
SEEN_CUES = {UNMASKED: ["6aa5270c8474fc14487e6ad42b278339"]}    # FinalTruth/Cue_0012 (her Q3 confession about Mireya)
PRESENCES = {
    # Her native unit was Unrecruited and killed, so a copy of her companion blueprint sits veiled at the far end of Fye's
    # bar, on his left beyond Seelah and Vellexia (Aranka keeps his right). Her native dialog would greet a living
    # companion, so Dialog "hub" makes the copy talkable through her own scenes only (E12c). If the anchor fails,
    # camellia.presence.failed opens the letter twin, and the epilogue page carries the commit.
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FYE, Side="left", Distance=3.5),
                   Requires=["trickster.ever", KILLED, PRIMED], Forbids=[CLOSED, DECLINED], MinChapter=3, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   Greeting="{n}At the far end of Fye's bar sits a woman in black lace to the chin, with a glass of wine "
                            "she has not touched and a bunch of lilies laid along the counter like a sleeping cat. Nobody "
                            "sits within two stools of her. Nobody could say why.{/n}"),
}
DERIVED = {
    # ledger 05 row 12, her own kills only. The Kaylessa pair [kaylessa.trickster.returned, kaylessa.camellia_killed] and
    # its oath node wait for Kaylessa's route to produce her return flag (backlog; an unproduced flag is a dead gate).
    "camellia.kill_returned": [["nurah.trickster.returned", "nurah.dead_camellia"],
                               ["soana.trickster.returned", "soana.killed_by_camellia"]],
    # R2-6: the last completed beat before the commit.
    P + "late_committed": [["trickster.ever", TERMS]],
}
# Other routes' Camellia reactions sit on her companion hub. A Camellia raised from a retained death is back in the party
# and on that hub, so they lift her death once she has returned. The veiled Camellia at Fye's has no native hub (her
# presence is an RRT hub, which only hosts her own relationship's scenes), so her killed state stays closed to them.
FOREIGN_REACTIONS = (
    "jerribeth.trickster.reaction.camellia", "jerribeth.trickster.reaction.camellia_host",
    "nurah.trickster.react.camellia_pardon", "nurah.trickster.react.camellia_market",
    "nurah.trickster.react.camellia_supper", "nurah.trickster.react.camellia_draft",
    "soana.trickster.react.camellia_portion", "soana.trickster.react.camellia_knot",
    "minagho_chivarro.trickster.react.camellia_bill",
)


def cam(id, text, *choices, **kw):
    return n(id, "Camellia", text, *choices, portrait="Camellia", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Camellia", **kw)


def lead(seq, then):
    """Lead-in nodes before a decision node. seq = [(id, fn, text, flag)], the first with flag None. Continue walks through
    every later node whose flag is held, in order, and then to `then`, so the decision node keeps fixed choice indices."""
    nodes = []
    for i, (nid, fn, body, _) in enumerate(seq):
        rest = seq[i + 1:]
        flags = [v[3] for v in rest]
        choices = [c("Continue", rest[j][0], requires=(flag,), forbids=tuple(flags[:j])) for j, flag in enumerate(flags)]
        choices.append(c("Continue", then, forbids=tuple(flags)))
        nodes.append(fn(nid, body, *choices))
    return nodes


def _branch(nodes, killed):
    """The twin's own copy of the nodes: drop choices gated on the other branch (camellia.killed), then drop nodes that are
    no longer reachable from the first node."""
    nodes = copy.deepcopy(nodes)
    for node in nodes:
        node["Choices"] = [ch for ch in node["Choices"]
                           if not (killed and KILLED in ch["Forbids"]) and not (not killed and KILLED in ch["Requires"])]
        if not node["Choices"]:
            raise ValueError("branch pruning emptied node " + node["Id"])
    by_id = {node["Id"]: node for node in nodes}
    seen, stack = set(), [nodes[0]["Id"]]
    while stack:
        nid = stack.pop()
        if nid in seen:
            continue
        seen.add(nid)
        stack += [ch["Next"] for ch in by_id[nid]["Choices"] if ch.get("Next")]
    return [node for node in nodes if node["Id"] in seen]


def met(id, title, entry, nodes, requires, forbids=(), delay=24, optional=False, any_groups=(), camp_entry=None,
        alive_ok=False):
    """A physical scene after her return, in two hosts that never overlap. The veiled Camellia (killed) is met at her
    presence at the end of Fye's bar in Drezen; a Camellia raised from a retained death is back on her own companion hub.
    Both carry the same nodes; branch text is chosen inside the nodes by camellia.killed. On her companion hub the scene
    requires her return, unless alive_ok (a scene the living, never-killed Camellia may also have), which forbids her death."""
    groups = dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}
    SCENES.append(scene(id, title, "Camellia", 3, entry, _branch(nodes, True),
                        requires=tuple(dict.fromkeys((*requires, KILLED, RET))), forbids=(CLOSED, *forbids),
                        delay=delay, last=5, optional=optional, Relationship=REL, Chapters=[3, 5], ContactUnit=UNIT,
                        Areas=[DREZEN], InteractionHub=PRESENCE, **groups))
    SCENES.append(scene(id + "_camp", title, "Camellia", 3, camp_entry or entry, _branch(nodes, False),
                        requires=tuple(dict.fromkeys(requires if alive_ok else (*requires, RET))),
                        forbids=(CLOSED, KILLED, *((DEAD,) if alive_ok else ()), *forbids), delay=delay, last=5,
                        optional=optional, Relationship=REL, AnswerLists=[HUB_LIST], ContactUnit=UNIT, **groups))


# --- The joke, at the kill (P1 primers). Owlcat's inline mythic answers are the tone target. ---------------------------

JOKE = '[Play a cruel trick on Camellia] "Go on, then. Die convincingly. I\'ll know if you don\'t."'

SCENES.append(scene(P + "killed.setup_hub", "Die convincingly", "Camellia", 3, JOKE, [
    cam("start", '''{n}For a moment Camellia simply looks at you, head tilted, as if you had praised her gown in a language she does not speak. Then one corner of her mouth lifts.{/n}
"Convincingly? My friend, I have never done anything any other way."''',
        c("Continue", "game", requires=(GAME,)),
        c("[Draw your weapon]", native_next=KILL_NEXT, forbids=(GAME,), flags=(PRIMED,))),
    cam("game", '''"Two lies and a truth, then, one last time." {n}She draws her knife and holds it up to the light, as if to judge its colour.{/n} "You are going to kill me. I am going to let you. I have never been so pleased with anyone in my life. Guess which one I made up."''',
        c("[Draw your weapon]", native_next=KILL_NEXT, flags=(PRIMED,))),
    ], requires=("trickster",), forbids=(PRIMED, KILLED, DEAD), last=5, Relationship=REL, AnswerLists=[KILL_LIST],
    NativeReturnCue=KILL_RETURN, EntryMythic="PlayerIsTrickster", TricksterDevice=True,
    TricksterState="killed_by_commander"))

SCENES.append(scene(P + "killed.setup_q3", "Die convincingly", "Camellia", 5, JOKE, [
    cam("start", '''{n}Camellia's laugh is short and genuinely delighted, the first true sound she has made all evening.{/n}
"A performance review, at a time like this? Very well. I shall give you a death worth remembering. Do try to keep your eyes open. It is the only part I ever cared about."''',
        c("[Draw your weapon]", native_next=Q3_NEXT, flags=(PRIMED,))),
    ], requires=("trickster",), forbids=(PRIMED, KILLED, DEAD), last=5, Relationship=REL, Chapters=[5], AnswerLists=[Q3_LIST],
    NativeReturnCue=Q3_RETURN, EntryMythic="PlayerIsTrickster", TricksterDevice=True,
    TricksterState="killed_by_commander"))

# Directive 9 foresight: in Q1 it is the Commander who sends Anevia's hunters (native Answer_0008 e133d4f4), so the trick is
# laid before the death. host_reason: AneviaResults is the dialog where the order is natively given; Anevia speaks here.
SCENES.append(scene(P + "killed.setup_q1", "A message for the killer", "Anevia", 3,
    '[Play a cruel trick on Camellia] "The killer is in the building. Tell her from me: die convincingly. I\'ll know if she doesn\'t."', [
    n("start", "Anevia", '''{n}Anevia turns the word over like a coin she suspects of being shaved.{/n}
"Convincingly. Commander, dead's dead. Where I come from we don't grade it." {n}She shrugs, and her hand is already on the knife at her belt.{/n} "Fine. I'll tell her. Might even be the last thing she hears."''',
      c("[Give the order]", native_next=Q1_NEXT, flags=(PRIMED, BY_ORDER)), portrait="Anevia"),
    ], requires=("trickster",), forbids=(PRIMED, KILLED, DEAD), last=5, Relationship=REL, AnswerLists=[Q1_LIST],
    NativeReturnCue=Q1_RETURN, EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1),
    TricksterDevice=True, TricksterState="killed_by_commander"))


# --- The late fallback (R2-2): no line at the kill, so the Commander says it to the corpse, now, and pays for the lid. ---

SCENES.append(scene(P + "killed.late_curtain", "Wrong flowers", "Memory", 3, "", [
    *lead([("start", nar, '''{n}The crusade buried Camellia under a plain stone at the edge of the Drezen cemetery, with a wrong bunch of flowers: lilies, the white wedding kind. Tonight you stand over the stone with the sexton, a stooped man with a lantern, who wants forty gold to lift the lid and a hundred more to forget that he did.{/n}''', None),
           ("lilies", nar, '''{n}You promised her, once, the wrong flowers on purpose. Somebody got there first, by accident. It feels like being robbed of a punchline.{/n}''', FUNERAL)],
          "choose"),
    nar("choose", '''{n}The sexton spits on his palms and waits.{/n}''',
        c("[Pay the sexton and lift the lid]", "coffin", crusade=("Finances", -100)),
        c('[Let the grave keep her] "Put the spade down. Leave her."', flags=(DECLINED, CLOSED))),
    nar("coffin", '''{n}The lid comes up with a groan of wet wood. She lies exactly as she was laid out, hands folded over the bone snake at her throat, chin lifted a fraction, like an actress who knows where the light falls. There is no smell. The sexton notices that, and crosses himself, and does not say anything.{/n}''',
        c('[Play a cruel trick on Camellia] "Go on, then. Die convincingly. This time I\'m watching."', "shut",
          mythic="Trickster", flags=(PRIMED, LATE)),
        c('[Close the lid] "No. Let her stay dead."', flags=(DECLINED, CLOSED))),
    nar("shut", '''{n}Nothing happens. You did not expect it to. You nod to the sexton, and he lowers the lid on a woman who is, by every measure he knows, dead, and you both pretend very hard not to have heard the small, delighted exhalation from inside the box as it closed.{/n}''',
        c("[Walk back to the citadel]", "walk")),
    nar("walk", '''{n}The sexton walks back with you as far as the cemetery gate, very fast, holding the lantern high. At the gate he stops, and says, not looking at you, that he has buried a great many people in this ground and that none of them ever laughed at him before, and he would like it very much if the Commander did not bring him any more work of that kind. Then he goes home, and, you learn later, does not come out again for three days.{/n}''',
        c("[Go home]")),
    ], requires=("trickster", KILLED), forbids=(PRIMED, RET, DECLINED), last=3, Relationship=REL, Remote=True,
    Chapters=[3], TricksterDevice=True, TricksterState="killed_by_commander"))


# --- The return, in person (R2-3): the veiled mourner at the end of Fye's bar. ---------------------------------------

PERFORMANCE_LEADS = [
    ("order", cam, '''"You sent that charming Mendevian thief to kill me, and a message with her. She delivered both. I must say, she was very thorough with the first, and she stumbled a little over the word 'convincingly'. I forgave her. One cannot expect poetry from a sergeant."''', BY_ORDER),
    ("late", cam, '''"You paid a sexton a hundred gold to open my coffin, so that you could tell my corpse it was not convincing. Of all the reviews I have ever received, that is the only one I minded. I lay there for three days composing a reply."''', LATE),
    ("named", cam, '''"You once offered to give my poor spirit a name. I have taken one for myself instead." {n}The smile under the lace widens.{/n} "You will allow that I have a better claim to it than anyone."''', NAMED),
    ("invented", cam, '''"You made up a sergeant for me once, with a limp and a wife in Nerosyan and a laugh like a mule falling downstairs. I have made up a widow from Nerosyan. I thought you would appreciate the symmetry."''', INVENTED),
    ("kept_name", cam, '''"You told me once that Mireya was mine to keep. I have kept her. I am wearing her." {n}She touches the edge of the veil.{/n} "It suits me better than it ever suited her."''', NAME_LEFT),
    ("outlive", cam, '''"You said you would rather I didn't need a funeral. I didn't, as it turned out. I simply had one. It was very well attended."''', OUTLIVE),
    ("wrong", cam, '''"And the lilies. You promised me the wrong flowers, and someone brought the wrong flowers, and I lay under them and laughed at every mourner who wept. The chaplain thought the wind was in the trees."''', FUNERAL),
]
SCENES.append(scene(PERFORMANCE, "The veiled mourner", "Camellia", 3,
    '[Speak to the veiled mourner] "You\'re a long way from any grave I know of."', [
    cam("start", '''{n}The woman at the end of the bar wears black lace to the chin and carries lilies, the wrong ones. When she lifts the veil a finger's width, the smile under it is Camellia's, and so is the way she licks her lips before she speaks.{/n}
"Call me Mireya today. It seems only fair: you made up my death, so I have made up my name."''',
        c("Continue", "who")),
    *lead([("who", cam, '''"Do sit. Fye is pretending I am a widow from Nerosyan who drinks nothing and tips in silver. He is quite good at it. Everyone in this city is quite good at not seeing the dead."''', None),
           *PERFORMANCE_LEADS], "why"),
    cam("why", '''"You're wondering why I came back. Everyone wonders that about the dead. Nobody ever asks us."
{n}She turns her glass a quarter turn.{/n} "I came back because it was the first time in my life that somebody lied to me better than I could lie to them. You told me to die convincingly, and I died, and the whole time I was lying in that box I could hear you not believing it. Do you know how rare that is? To be disbelieved by someone who's right?"
"I couldn't possibly stay dead after that. It would have been so rude."''',
        c("Continue", "primed")),
    cam("primed", '''"You told me to die convincingly, and I did. The gravediggers complained about the weight. The chaplain wept, which I thought was a nice touch. Everyone was convinced, except you, of course."
{n}She presses something into your palm under the lilies: a small, clean knife, still warm from her glove.{/n} "Keep it. Next time, use it properly. And do not look for me. I shall find you. A dead woman keeps very flexible hours."
{n}Under the lace her mouth curves.{/n} "Oh, and do look a little sad when you leave. Fye is watching, and the widow from Nerosyan has been stood up by her gentleman. It would be a pity to spoil the story."''',
        c('[Keep the knife] "I\'ll keep it close. Closer than you\'d like."', flags=(RET, KNOWS, STARTED)),
        c('[Hand the knife back, point first] "Stay dead. It suits you."', "back")),
    cam("back", '''{n}She takes the knife by the blade, carefully, the way one takes a letter one has decided not to read.{/n}
"How disappointing. I was dead for you, my friend, and you did not even come to see the second act." {n}The veil comes down. When you look up from your hands, the stool is empty and the lilies are on the floor.{/n}''',
        c("[Let her go]", flags=(DECLINED, CLOSED))),
    ], requires=("trickster.ever", PRIMED, KILLED), forbids=(RET, DECLINED), delay=72, last=5, Relationship=REL,
    Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN], InteractionHub=PRESENCE, TricksterDevice=True,
    TricksterState="killed_by_commander"))

# The letter twin, only when the presence failed (E12b runtime observation): one letter carries her return and her price.
SCENES.append(scene(P + "killed.performance_letter", "A letter from Mireya", "Memory", 3, "", [
    *lead([("start", nar, '''{n}The letter is on your pillow, which nobody could have reached without passing two guards and a locked door. The paper smells of lilies. Folded inside it, point down, is a small, clean knife. It is signed "Mireya".{/n}
"My friend. You told me to die convincingly, and I did. Everyone was convinced, except you. I would have told you so in person, but the tavern keeper you chose for me has gone somewhere, and I refuse to haunt an empty bar."''', None),
           ("order_l", cam, '''"You sent your Mendevian thief with a message. She delivered it very thoroughly. Tell her I bear her no grudge. Yet."''', BY_ORDER),
           ("late_l", cam, '''"You paid a sexton to open my coffin. I heard every coin. I shall not forget the sound."''', LATE)],
          "letter_why"),
    cam("letter_why", '''"I have been sleeping in the loft above a chandler's, among the tallow, very comfortably. Nobody looks up in Drezen. I have watched you twice from the window cross the square below, and you did not look up either, and I was quite hurt."
"But I forgive you. You told me to die convincingly. A person who asks for that deserves to be taken at their word, and then some."''',
        c("Continue", "price")),
    cam("price", '''"Since I cannot trust you to find me, my price for staying comes by post. Give me a name, or give me yours. Write it on the back of this and leave it on your pillow. I shall know."''',
        c('[Write back a name] "The quartermaster\'s clerk. Nobody will miss him."', alignment=("Evil", 2),
          flags=(RET, KNOWS, STARTED, ACCOMPLICE, TERMS)),
        c('[Write back your own] "If you ever need to kill a friend, start with me."',
          flags=(RET, KNOWS, STARTED, MARKED, TERMS)),
        c("[Burn the letter]", flags=(DECLINED, CLOSED))),
    ], requires=("trickster.ever", PRIMED, KILLED, PRESENCE_FAILED), forbids=(PERFORMANCE, RET, DECLINED), delay=96,
    last=5, Relationship=REL, Remote=True, Chapters=[3, 5], TricksterDevice=True, TricksterState="killed_by_commander"))


# --- Dead otherwise: the same spoken-death lie, told at the body. She names her price before she rises. ---------------

SCENES.append(scene(P + "dead.overacting", "Curtain call", "Memory", 3, "", [
    nar("start", '''{n}The report is two lines long: the shaman Camellia Gwerm, fallen in the rearguard action, body retained with the baggage for burial at the next halt. The chaplain has written "may she find peace" at the bottom, and then, apparently on reflection, crossed out "peace" and written "rest".{/n}''',
        c("[Go to the wagons]", "wagons")),
    nar("wagons", '''{n}They have laid Camellia out under a cloak by the supply wagons. Even dead she looks as though she is waiting for applause: one hand at her throat, one flung out, her hair arranged by nobody. The spirits she fed have gone very quiet around her. The camp's dogs will not come near the wagons.{/n}''',
        c('[Tell the corpse it\'s overacting] "Get up, Camellia. You\'re overdoing it, and the audience is leaving."',
          "waking", mythic="Trickster"),
        c('[Let her lie] "Take your bow. The curtain\'s down."', flags=(DECLINED, CLOSED))),
    cam("waking", '''{n}Her eyes stay shut. Her lips barely move.{/n}
"Rude. I was resting." {n}A pause, like a held breath that has nowhere to go.{/n} "My spirits were promised a death, my friend. Mine. If you take it back from them, you owe them another. Someone in Drezen. I choose whom, and you do not ask."
{n}Her lips curve, very slightly, though her eyes stay closed.{/n} "Don't look so grave. You've always known what I cost. You've simply never had to pay it yourself. Now you do. Isn't that fair? You're the one who wants me back."''',
        c('[Agree to her price] "Choose, then. Just get up."', revive="camellia", flags=(RET, OWED, STARTED)),
        c('[Refuse her price] "No one else pays for you."', "refused")),
    cam("refused", '''"Then I shall stay exactly where I am. It is quieter here than it has been in years." {n}The corner of her mouth moves, very slightly.{/n} "You were always the only one who could make it quiet. Now go away, and let me enjoy it."''',
        c("[Let her lie]", flags=(DECLINED, CLOSED))),
    ], requires=("trickster", "trickster.ever", DEAD), forbids=(KILLED, RET, DECLINED),
    last=5, Relationship=REL, Remote=True, Chapters=[3, 5], Recovery="camellia", TricksterDevice=True,
    TricksterState="dead_otherwise"))


# --- Her price (terms) and her test (the commit). Both in person; her refusal is reachable on every branch. -----------

TERMS_LEADS = [
    ("bowl", cam, '''"You held Mireya's bowl for me once, in the snow, while she drank. You didn't leave. I have thought about that more than about anything anyone has ever said to me."''', BOWL_HELD),
    ("fed", cam, '''"In the Abyss, when the flies were loud, you sent me east to bleed demons until they were quiet. You knew exactly what I was, and you pointed. I have been waiting ever since to see whether you would pretend otherwise."''', FED),
    ("dug", cam, '''"Your little thief is still digging up my spirits' supper. She is very good. Tell her to stop before she reaches the bottom, or I will have to be very good too."''', INVESTIGATED),
    ("covered", cam, '''"'Deserters.' You wrote it yourself. I read it in the register and laughed until the spirits hushed me. You lie beautifully for a murderer, my friend."''', COVERED),
    ("steady", cam, '''"You held my knife at my throat, and your hand did not shake. I have been thinking about your hand ever since. It is a very inconvenient thing to think about."''', STEADY),
    ("flinched", cam, '''"You flinched, when I put my knife in your hand and my throat under it. I have forgiven you. I forgive very little, so you may treasure it."''', FLINCHED),
]
met(P + "returned.terms", "What a dead woman wants", '"You said you would find me. You didn\'t. I found you."', [
    cam("start", '''"Every friend I have ever had, I have killed. It is the only thing that quiets the flies." {n}She says "flies" the way other women say "my headaches", with a small apologetic flutter of the hand.{/n} "You are the first friend I have kept past the point where I usually stop. And I find the flies are very loud."''',
        c("Continue", "flies")),
    cam("flies", '''"You've never asked me what the flies are. Everyone who stays long enough asks, eventually. Then they stop staying."
{n}She taps her temple with one manicured nail.{/n} "They're the voices. The spirits, if you like; I have called them that for so long that I no longer know what else to call them. They're a buzzing, all day, all night, at the window of my head. And there is only one thing that makes them stop."
"It isn't blood. I told everyone it was blood. It's the look. The moment a friend understands what I am. When I see that, everything goes quiet, like snow."''',
        c("Continue", "lead")),
    *lead([("lead", cam, '''"So I have been thinking about what to do with you. I think best in cemeteries and knife shops, and I have visited both."''', None),
           *TERMS_LEADS], "price"),
    cam("price", '''"So. My price for staying. Give me a name, or give me yours."
{n}She leans in until the lace of her sleeve brushes your wrist.{/n} "A name: someone nobody will miss, and I shall not ask you twice. Or yours: the promise that if I ever need to kill a friend, I start with you. Either is a gift. I will know which one you meant."''',
        c('[Give her a name] "The quartermaster\'s clerk. Nobody will miss him."', "named", alignment=("Evil", 2),
          flags=(ACCOMPLICE, TERMS)),
        c('[Give her yours] "If you ever need to kill a friend, start with me. I\'ll make it interesting."', "mine",
          flags=(MARKED, TERMS)),
        c('"No names. No knives. Not in my crusade."', "none")),
    cam("named", '''"The clerk." {n}She tastes it.{/n} "A small name. A tidy name. You did not even hesitate, which is either very kind or very cruel, and I shall find out which." {n}She stands, and smooths her skirt.{/n} "Three nights. Wear something you can move in."
{n}At the door she turns.{/n} "You don't know anything about him, do you? You chose a man you had never looked at. That's the part I like best."''',
        c("[Watch her go]")),
    cam("mine", '''{n}For once she has no answer ready. She looks at you for a long moment, and whatever she is looking for, she seems to find it, because she laughs, softly, and only once.{/n}
"Oh, you are dreadful. Nobody has ever offered before. They only ever found out." {n}She stands.{/n} "Three nights. Sleep lightly."
{n}At the door she turns, and her voice is almost shy.{/n} "You understand what you've done? You've made yourself the first name on my list and the last. There's nobody else on it now who matters. Everyone else is only practice."''',
        c("[Watch her go]")),
    cam("none", '''"Not in your crusade." {n}She repeats it like a phrase in a foreign grammar book, carefully, to be sure of the endings.{/n} "Then I am not in your crusade either, my friend. What a pity. It was such a nice crusade."''',
        c("[Let her go]", flags=(CLOSED,))),
], requires=("trickster.ever", RET, LESSON), forbids=(TERMS,), delay=48)

TEST_LEADS = [
    ("knife", cam, '''"You found the knife under my skirt when we danced, and you did not pretend you hadn't. Nobody asks. They only ever find out."''', KNIFE_NOTICED),
    ("touched", cam, '''"You touched me once in the salle by lying with your whole body. I have wanted to know ever since what your body says when it is not lying."''', TOUCHED),
    ("she_won", cam, '''"You lost my game once. Two lies and a truth, and you let the lie walk straight past you. Let us see whether you lose this one."''', SHE_WON),
    ("danced", cam, '''"You danced with me once, with this under my skirt. You never once looked down. I noticed that. I notice everything that does not look down."''', DANCED),
    ("out_lied", cam, '''"You beat me at my own game once, with three lies I believed. I have been waiting ever since to see whether your face can lie as well as your mouth."''', OUT_LIED),
]
met(P + "returned.test", "A knife at the right height", '"Come to your quarters tonight. Alone. Bring the knife I gave you."', [
    nar("start", '''{n}Your quarters are dark, and not empty.{/n}''',
        c("Continue", "clerk", requires=(ACCOMPLICE,)),
        c("Continue", "throat", forbids=(ACCOMPLICE,))),
    cam("clerk", '''{n}The quartermaster's clerk sits in your chair, very still and very alive, his ink-stained hands flat on his knees. Camellia stands behind him, one hand in his hair, her small clean knife resting under his ear. He is weeping without a sound.{/n}
"You gave me his name. I wanted to watch your face while I used it. Don't disappoint me, my friend."
{n}The clerk's lips move. "My girl," he whispers, to you, not to her. "The orphanage by the gate. Every seventh day. Please." Camellia tilts her head and listens to that too, with great attention, the way she listens to everything.{/n}''',
        c("Continue", "lead_c")),
    cam("throat", '''{n}You wake to a weight on your chest and cold steel under your jaw. She is smiling, and her eyes are wide open, watching for the thing she has always watched for.{/n}
"You told me to start with you. I am a woman of my word."''',
        c("Continue", "lead_t")),
    *lead([("lead_c", nar, '''{n}The clerk's eyes find yours and beg. Camellia's find yours and wait.{/n}''', None), *TEST_LEADS], "judge_c"),
    *lead([("lead_t", nar, '''{n}The knife does not press. It does not need to.{/n}''', None),
           *[(k + "_t", f, t, flag) for k, f, t, flag in TEST_LEADS]], "judge_t"),
    nar("judge_c", '''{n}Nobody moves.{/n}''',
        c("[Hold her gaze and say nothing]", "steady"),
        c("[Put your own knife to her ribs]", "blade"),
        c("[Shout for the guard]", "guard")),
    nar("judge_t", '''{n}Nobody moves.{/n}''',
        c("[Lie still and smile back]", "steady"),
        c("[Put your own knife to her ribs]", "blade"),
        c("[Shout for the guard]", "guard")),
    cam("steady", '''"There. That face. Not dread. Not fury. Interest." {n}The knife goes away. So, shaking, does the clerk, if there was one, out of the door and down the stair, and he will tell nobody anything for the rest of his life.{/n}
"I have killed every friend I ever had. I find I would rather keep you on a shelf a while longer."''',
        c('[Ask her to stay] "Then stay."', "yes"),
        c("[Ask her to put the knife away for good]", "no")),
    cam("blade", '''"Oh, good." {n}Neither of you moves. Two points, one breath.{/n} "Someone who cuts back. You have no idea how rare that is. The spirits are quite beside themselves. So am I, a little."''',
        c('[Ask her to stay] "Then stay."', "yes"),
        c("[Ask her to put the knife away for good]", "no")),
    cam("guard", '''"Guards. How terribly ordinary." {n}By the time the door opens, the window is open instead, and the lace caught on the sill is the only thing left of her.{/n}''',
        c("[Let her go]", flags=(GUARD, CLOSED))),
    cam("yes", '''"Stay? My friend, I never left. I simply stopped lying down." {n}She slides her knife into your belt, hilt first, and leaves her hand there.{/n} "Keep it close. One day I shall want it back, and you will know the day, because I shall be smiling."''',
        c("[Keep it]", "threshold", flags=(COMMITTED,))),
    nar("threshold", '''{n}She does not take her hand away. She takes your belt instead, and walks you backwards by it until the edge of the bed stops you, and then she climbs into your lap with her skirts in her fists and the knife's hilt digging into both of you.{/n}
{n}She kisses the way she talks, politely and then not at all. Her teeth find your lower lip and test it, exactly as hard as she means to. Her breath is quick and hot and smells of lilies and iron. When your hands find the laces at her back she makes a small, pleased sound and does not help, and when the last one gives she catches your wrist and holds your palm flat over her heart, so you can count it with her. It is going very fast.{/n}
"Beat," {n}she whispers against your mouth.{/n} "Beat. Beat."''',
        c("[Put out the lamp.]", "morning")),
    nar("morning", '''{n}Grey light. The knife is on the pillow between you, point towards the door, where she put it some time in the night. She is awake, lying on her side, watching your face with her chin on her folded hands, the way she watched the funeral from the parapet.{/n}
"You slept," {n}she says, wonderingly.{/n} "With me in the bed and my knife on the pillow. You slept like a child. Nobody has ever done that. They lie awake. I can always hear them lying awake."
{n}She reaches out and touches your eyelid with one fingertip, very lightly, as if to make sure it is real.{/n} "I'm going to have to think about this for a very long time."''',
        c("[Close your eyes again]")),
    cam("no", '''{n}Her smile does not move, which is worse than if it had.{/n}
"Without the knife? You want the woman and not the appetite. There is no such woman. There was, once, and her name was Mireya, and I made her up."''',
        c("[Watch her go]", flags=(TAME, CLOSED))),
], requires=("trickster.ever", RET, TERMS), forbids=(COMMITTED,), delay=72)


# --- Optional: the oath (ledger 05 row 12): a woman Camellia herself killed, walking again. --------------------------

NR, ND = "nurah.trickster.returned", "nurah.dead_camellia"

met(P + "kills_answered.oath", "The kill that didn't take", '"You look like someone who has been told a secret. Tell me."', [
    cam("start", '''"I remember the taste of that death. I remember it very clearly. And yet I hear..."''',
        # Exactly one route is ever shown: Nurah first, then Soana (the pairs of Derived kill_returned).
        c("Continue", "nurah", requires=(NR, ND)),
        c("Continue", "soana", forbids=(ND,)),
        c("Continue", "soana", requires=(ND,), forbids=(NR,))),
    cam("nurah", '''"...that the little writer I was given is walking about Drezen, correcting people's spelling. I remember her eyes at the end, you know. They were so surprised. She had written about so many deaths and never once imagined her own." {n}Camellia sighs.{/n} "And now she's walking about with those same eyes. You did this. Of course you did."''',
        c("Continue", "ask")),
    cam("soana", '''"...that the Wintersun woman is back in her forest, scolding the crows. I bled her myself. I felt her stop. She never once looked afraid, you know. Only disappointed, as if I'd tracked mud onto her floor. I've always resented her for that." {n}She taps the glass.{/n} "You did this. Of course you did."''',
        c("Continue", "ask")),
    cam("ask", '''{n}She turns her wine glass slowly by the stem, a quarter turn, and another, as if it were a key in a lock she has not yet decided to open.{/n}
"What am I to do with a kill that will not stay killed? It is like a debt that pays itself back. I find it obscurely insulting."''',
        c('[Invoke the fine print] "You killed her once. Nobody promised you twice."', "loophole"),
        c('[Offer her someone else] "Leave her. I\'ll find you someone nobody will miss."', "fed", alignment=("Evil", 1)),
        c('[Threaten her] "Touch her again and I\'ll show you how convincingly I can kill."', "threat")),
    cam("loophole", '''"...Once. How lawyerly of you." {n}She sets the glass down, delighted despite herself.{/n} "Very well, my friend. Once. I have always kept to the terms of my own games. It is the only thing that makes them games."''',
        c("[Leave it there]", flags=(LOOPHOLE,))),
    cam("fed", '''"How generous." {n}She licks her lips, slowly.{/n} "I'll hold you to it. I shall not even tell you when."''',
        c("[Leave it there]", flags=(OATH_FED,))),
    cam("threat", '''"Oh, now you're just flirting." {n}But she takes her hand off the knife, and she does not put it back for the rest of the evening.{/n}''',
        c("[Leave it there]", flags=(THREATENED,))),
], requires=("trickster.ever", "camellia.kill_returned"), delay=0, optional=True, alive_ok=True)


# --- Epilogue pages (Owner CamelliaEpilogue; ordered siblings; no effects). -------------------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}She kept the Commander's name as her price, and said so at dinner parties, and everyone laughed, and she did not.{/n}", requires=(MARKED,)),
    p("{n}A clerk of the quartermaster's office resigned the week after the Threshold and took holy orders in Absalom. He never said why. He never slept with his back to a door again.{/n}", requires=(ACCOMPLICE,)),
    p("{n}Somewhere in Drezen a body was found, one year, with no wounds but one, very neat, right where a friend would stand. The report said deserters. It was in the Commander's hand.{/n}", requires=(COVERED,)),
    p("{n}Anevia never stopped looking for the lower-city killer. She never found anyone, and she never quite believed that.{/n}", requires=(INVESTIGATED,)),
    p("{n}Once, when the Commander had been gone a season, she was found in the dark of the citadel with a knife in one hand and the other flat on the Commander's empty pillow, counting. Nobody asked her what.{/n}", requires=(NOT_TODAY,)),
    p("{n}Every year on the date of her funeral she laid wrong lilies on her own grave, and read the stone aloud, and corrected the spelling.{/n}", requires=(KILLED,)),
    p("{n}In Nerosyan, a widow named Mireya Voss kept a house in the Lantern Quarter for many years, and paid her taxes, and was said to have been married to a wine merchant who died of eels. Nobody ever saw her husband's grave.{/n}", requires=(NEW_NAME,)),
    p("{n}Over the Commander's bed hung a charcoal rubbing of a gravestone, framed. Guests who asked about it were told it was a family memorial, and that the family member in question was in the next room.{/n}", requires=(OLD_NAME,)),
    p("{n}The cells under the citadel were never quite used again. The guards said a prisoner had died down there of a failure of the heart, and that the last one to hear him had heard him laughing, and then not laughing.{/n}", requires=(PRISONER_HERS,)),
    p("{n}She never stopped asking. Once a season she would find a prisoner nobody loved and bring the Commander to the cell door and ask. The Commander said no. She said thank you, and waited for the next one. She was very good at waiting.{/n}", requires=(PRISONER_SPARED,)),
    p("{n}She kept the list on the Commander's shelf all her life. Nobody on it ever changed.{/n}", requires=(LIST_KEPT,)),
    p("{n}On the same shelf, beside the list, hung a little bone snake on a cord. Visitors were told it held a very old and very beautiful spirit. The Commander never said otherwise.{/n}", requires=(AMULET_KEPT,)),
    p("{n}A witness who had once seen a dead woman in church lived to a great age in Drezen, telling children about the singing ghost with the dog made of mist.{/n}", requires=(WITNESS_LIED,)),
    p("{n}There was a railing on the river steps now. People said somebody had fallen there, once, in the dark.{/n}", requires=(WITNESS_HERS,)),
    p("{n}A banner-mender named Ilse married her sergeant of the Third Company and kept, all her life, a horror of coughing ladies. She never knew why she had once been told to stay away. She lived to see her grandchildren.{/n}", requires=(FRIEND_WARNED,)),
    p("{n}A banner-mender named Ilse took walks every evening with a veiled lady for three years. Every evening the Commander waited for her to come home, and watched her face when she did. Ilse married her sergeant in the spring. Camellia sent the flowers: white lilies, the wedding kind. Whether that was a gift or a promise, nobody ever found out. Least of all Ilse.{/n}", requires=(FRIEND_WATCHED,)),
)
SCENES.append(scene(P + "epilogue.kept", "", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}Camellia Gwerm was entered in the crusade's register as dead, and never troubled to correct it. She stayed at the Commander's side through the Threshold and after it, a veiled woman whom no one could quite remember being introduced to, and she kept the small clean knife where the Commander could always see it. She never killed the Commander. She never said she wouldn't.{/n}
{n}She took no new friends, or said she took none. Once a year, on the date of her funeral, she brought the Commander breakfast on the point of a knife, and the Commander ate it without looking, and she watched, and neither of them ever grew tired of it.{/n}
{n}People who met them together in later years said they were the most courteous couple they had ever dined with, and that they could never afterwards remember what either of them had said, only that both of them had been smiling, and that neither had once looked away from the other.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.kept_on_record", "", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}When the Commander was entered among the dead of the Threshold, a veiled woman came to the memorial with lilies, the wrong ones, and stood at the back, and did not weep. Afterwards the chaplain found her knife laid on the altar, point towards the door. Those who knew Camellia said it was the only time she ever gave anything back.{/n}''')],
    requires=("trickster.ever", COMMITTED, "sacrifice"), forbids=("trickster.cheated_death", CLOSED), **EP))

SCENES.append(scene(P + "epilogue.commit", "The knife, returned", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Camellia finished her test. She finished it anyway. On one moonless night the next spring a veiled woman let herself into the Commander's rooms, laid a small clean knife on the pillow, point towards the door, and sat down to wait. She was still there in the morning. She said she had decided, on her own terms, that the Commander was more interesting alive. She did not say for how long.{/n}
{n}She stayed. She kept the knife on the pillow between them, point towards the door, every night of her life, and every morning she was surprised to find that it was still there, and so was she.{/n}''')],
    requires=("trickster.ever", TERMS), forbids=(COMMITTED, CLOSED, DECLINED), **EP))

SCENES.append(scene(P + "epilogue.refused", "Lace on the sill", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}Camellia never came back. Each year, on the date of her funeral, someone left lilies on her grave: the wrong ones, for a wedding. The gravediggers stopped asking who.{/n}''',
        paragraphs=(p("{n}The Commander kept the knife she had given, and never learned whether it had been a gift or a reminder.{/n}", requires=(KNOWS,)),
                    p("{n}A lower-city physician was found dead the winter after, with one wound, very neat. The spirits, it seemed, had been paid by someone.{/n}", requires=(OWED,)),
                    p("{n}The Commander once asked her to put the knife away for good. She did. She put it away in someone else, in Nerosyan, the following spring, and sent the Commander the report, folded small, with a pressed camellia inside.{/n}", requires=(TAME,)),
                    p("{n}The guard who answered the Commander's call that night rose to sergeant, and then to captain, and never once walked past an open window without looking out of it.{/n}", requires=(GUARD,))))],
    requires=("trickster.ever", RET, CLOSED), **EP))


# --- Reactions: exactly Anevia and Regill (ledger 05 §3.1 row 7). -----------------------------------------------------

# Hand-built one-node reaction (R2-0 l): two terminal choices, each its own cost. Anevia speaks on her own hub about a body.
SCENES.append(scene(P + "react.anevia_body", "Another body", "Anevia", 3,
    '[Anevia] "Got a minute, Commander? It\'s about a body."', [
    n("start", "Anevia", '''"Another body in the lower city, Commander. No wounds but one, very neat, right where a friend would stand. Poor sod was a porter, owed nobody, drank with everybody." {n}She taps the cane against her boot.{/n} "You want me to dig, or you want me to stop digging?"''',
      c('"Dig."', flags=(INVESTIGATED,)),
      c('[Lie] "Deserters. Close it."', flags=(COVERED,)), portrait="Anevia"),
    ], requires=(OWED,), forbids=("anevia_gone", DEAD, INVESTIGATED, COVERED), delay=24, last=5, Relationship=REL,
    Reaction=True, Chapters=[3, 5], AnswerLists=[ANEVIA_LIST], ForbidOverrides={"anevia_gone": "anevia.trickster.returned", DEAD: RET}))

SCENES.append(reaction("Regill", P + "react.regill_grave", (RET, KILLED, "regill.in_party"),
    '''"The Gwerm woman is walking Drezen in a veil. The crusade's register lists her as buried." {n}Regill does not raise his voice. He never needs to.{/n} "Under the Order, a false entry in a register of the dead is a crime of its own, Commander, separate from whatever she is. I have noted both."''',
    answer_list=REGILL_LIST, forbids=REGILL_GONE, entry='"About Camellia..."', chapter=3, last=5, portrait="Regill"))
SCENES.append(reaction("Regill", P + "react.regill_covered", (COVERED, "regill.in_party"),
    '''"A body in the lower city with one wound and a clerk's note that says 'deserters'. Deserters run, Commander. They are not laid out." {n}He folds his hands behind his back.{/n} "You signed a lie over a murder. I will not ask by whom. I will remember that you did not."''',
    answer_list=REGILL_LIST, forbids=(*REGILL_GONE, DEAD), entry='"About the lower city..."', chapter=3, last=5, portrait="Regill",
    ForbidOverrides={DEAD: RET}))
SCENES.append(reaction("Regill", P + "react.regill_dug", (INVESTIGATED, "regill.in_party"),
    '''"Your sergeant is digging after the lower-city killer. Good. Tell her to take two of mine." {n}He considers the map on the wall as though it had disappointed him.{/n} "Whoever did that has done it before, and will not stop at the one."''',
    answer_list=REGILL_LIST, forbids=(*REGILL_GONE, DEAD), entry='"About the lower city..."', chapter=3, last=5, portrait="Regill",
    ForbidOverrides={DEAD: RET}))


def integrate(payload):
    """Register the relationship's own keys, its presence, its revival and derived keys; lift her retained death on the
    other routes' Camellia reactions (condition-only, G6(b))."""
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    seen = payload.setdefault("SeenCues", {})
    if seen.get(UNMASKED, SEEN_CUES[UNMASKED]) != SEEN_CUES[UNMASKED]:
        raise ValueError("Conflicting seen-cue binding: " + UNMASKED)
    seen[UNMASKED] = list(SEEN_CUES[UNMASKED])
    revivals = payload.setdefault("Revivals", {})
    if "camellia" in revivals and revivals["camellia"] != REVIVALS["camellia"]:
        raise ValueError("Conflicting revival: camellia")
    revivals.update(copy.deepcopy(REVIVALS))
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    for id in FOREIGN_REACTIONS:
        scene_ = by_id.get(id)
        if scene_ is None:
            continue
        if DEAD in scene_["Forbids"]:
            scene_.setdefault("ForbidOverrides", {})[DEAD] = RET
