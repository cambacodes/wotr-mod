"""Camellia on the Trickster path: "Go on, then. Die convincingly." (Writer/handoffs/trickster/camellia.md; family F12,
the spoken death).

Canon: Camellia Gwerm, spirit shaman, Horgus's illegitimate daughter, who kills only those who considered her a friend,
"so that I can see the disbelief and dread in my victims' eyes" (FinalTruth/Cue_0042 f53d2eeb), and who tells the Commander
at the end of her lies: "You are an excellent liar, perhaps even better than I am" (Cue_0029 b5485676). Her spirit Mireya is
her own invention (Cue_0012 6aa5270c: "There is no Mireya. I made her up."; hub Cue_0107 1b515274). The device is a
bargain with her battle spirits, paid in the Commander's blood (before the kill, or late over the coffin on dearer
terms); the line at the kill only tells her the plan. She dies, is buried, and walks back into Drezen veiled, calling
herself Mireya.

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
RAISED = P + "raised"                    # her spirits give her back on the third night: she breathes again
BARGAINED = P + "spirits_bargained"      # before the kill, the Commander bled into her bowl and bargained with her spirits
BARGAIN_COST = P + "cost.blood_bargain"  # the Commander's blood, given to her battle spirits, owed again each new moon
BY_ORDER = P + "primed_by_order"
RET = P + "returned"
DECLINED = P + "declined"
TERMS = P + "terms_named"
LATE = P + "cost.late"
KNOWS = P + "cost.knows_you_tried"
OWED = P + "cost.spirits_owed"
INVESTIGATED = P + "cost.investigated"
COVERED = P + "cost.covered_murder"
BLED = P + "cost.bled"                  # her price: the Commander's blood, from her knife, when she asks
MARKED = P + "cost.marked"
OATH_FED = P + "cost.oath_fed"
GUARD = P + "cost.called_guard"
TAME = P + "cost.asked_her_tame"
LOOPHOLE = P + "oath_loophole"
THREATENED = P + "oath_threatened"
PRESENCE = "camellia.presence"
PRESENCE_FAILED = PRESENCE + ".failed"
PERFORMANCE = P + "killed.performance"
BARGAIN_LATE = P + "cost.bargain_late"   # the unprepared bargain, struck over her open coffin on the third night

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
MIREYA_KNOWN = P + "mireya_known"          # authored/native exposure, selects dialogue only
UNMASKED = "camellia.mireya_unmasked"    # FinalTruth/Cue_0012 seen: "There is no Mireya. I made her up."
WILL_GIVEN = "camellia.will_given"       # Camelia/Cue_0174 seen: Horgus's will, acknowledging her, handed to her
FILLED = P + "cost.grave_filled"        # the Commander put something in her empty coffin with their own hands
GALLOWS = P + "cost.gallows"            # ...a hanged deserter, cut down from the gallows and carried to her grave
FRIEND_WARNED = P + "friend.warned"      # the Commander frightened her new friend away with a lie
FRIEND_WATCHED = P + "cost.friend_kept"  # the Commander let the friendship run, and watches

GONE = (KILLED, DEAD, KICKED)
REGILL_GONE = ("regill.dead", "regill.kicked_out", "regill.left_plot")

RELATIONSHIP = dict(
    Title="A dead woman's hand",
    Description=("Camellia kills the friends who trust her. She says so herself, when she is in the mood to be honest. She "
                 "has decided, for now, that I am more interesting alive. She has not said for how long."),
    Objective="Answer Camellia",
    Guidance=("On the Trickster path, play her games at camp and learn her dance; she will choose the hour. If you turn on "
              "her instead, tell her to die convincingly; if her body fell some other way, tell it that it's overacting. A "
              "veiled woman may then ask for you at the end of Fye's bar in Drezen."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[KILLED, DEAD, KICKED], FailureFlags=[],
    # Q8 (Sol INT): the native Q3 kill also starts CamelliaNotInParty_KickedOut, so a kicked_out flag held WITH her
    # killed state is the kill, not a dismissal. A dismissal alone (no kill) still closes the route (recorded ruling).
    UnavailableOverrides={KILLED: RET, DEAD: RET, KICKED: P + "killed_held"},
    TricksterAccess={
        "killed_by_commander": dict(detect=[KILLED, DEAD], device=PERFORMANCE, returned=RET),
        "dead_otherwise": dict(detect=[DEAD, "!" + KILLED], device=P + "dead.overacting", returned=RET),
    },
)
REVIVALS = {"camellia": dict(Relationship=REL, Unit=UNIT, DeathFlag=DEAD)}
SEEN_CUES = {UNMASKED: ["6aa5270c8474fc14487e6ad42b278339"],   # FinalTruth/Cue_0012 (her Q3 confession about Mireya)
             WILL_GIVEN: ["320802ce6b647e942aaf33d96ed9321d"]}  # Camelia/Cue_0174 (the will, acknowledging her)
PRESENCES = {
    # Her native unit was Unrecruited and killed, so a copy of her companion blueprint sits veiled at the far end of Fye's
    # bar, on his left beyond Seelah and Vellexia (Aranka keeps his right). Her native dialog would greet a living
    # companion, so Dialog "hub" makes the copy talkable through her own scenes only (E12c). If the anchor fails,
    # camellia.presence.failed opens the letter twin, and the epilogue page carries the commit.
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=FYE, Side="left", Distance=6.0),
                   Requires=["trickster.ever", KILLED, PRIMED, RAISED], Forbids=[CLOSED, DECLINED], MinChapter=3, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   Greeting="{n}At the far end of Fye's bar sits a woman in black lace to the chin, with a glass of wine "
                            "she has not touched and a bunch of lilies laid along the counter like a sleeping cat. Nobody "
                            "sits within two stools of her. Nobody could say why.{/n}"),
}
DEATH_OBSERVED = P + "death_observed"
KILLED_CORPSE = P + "killed_corpse_observed"
DERIVED = {
    MIREYA_KNOWN: [[UNMASKED], [AMULET_KEPT]],
    KILLED_CORPSE: [[KILLED, DEAD]],
    # ledger 05 row 12, her own kills only: Nurah, Soana and (since the Kaylessa route produces her return) Kaylessa.
    "camellia.kill_returned": [["nurah.trickster.returned", "nurah.dead_camellia"],
                               ["soana.trickster.returned", "soana.killed_by_camellia"],
                               ["kaylessa.trickster.returned", "kaylessa.camellia_killed"]],
    # The oath routes one pair per world, in ledger order (Nurah, Soana, Kaylessa): the Kaylessa branch steps aside when an
    # earlier pair holds. Added with the Kaylessa route (its producer), save-safe: new keys, the new choice appended.
    "camellia.kill_returned.soana": [["soana.trickster.returned", "soana.killed_by_camellia"]],
    "camellia.kill_returned.earlier": [["nurah.trickster.returned", "nurah.dead_camellia"],
                                       ["soana.trickster.returned", "soana.killed_by_camellia"]],
    # R2-6: the last completed beat before the commit.
    P + "late_committed": [["trickster.ever", TERMS]],
    P + "killed_held": [[KILLED]],   # authored twin of camellia.killed for the kicked_out override (Q8)
}
# Other routes' Camellia reactions sit on her companion hub. A Camellia raised from a retained death is back in the party
# and on that hub once her current death state clears. The veiled Camellia at Fye's has no native hub (her
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


def _branch(nodes, mode):
    """The twin's own copy of the nodes. mode "killed" (the veiled Camellia at her presence), "camp" (raised from a
    retained death, on her companion hub) or "alive" (never killed, on her companion hub). Choices gated on another branch
    are dropped (by camellia.killed, her return, or her retained death), then nodes no longer reachable."""
    nodes = copy.deepcopy(nodes)

    def keep(ch):
        req, forb = set(ch["Requires"]), set(ch["Forbids"])
        if mode == "killed":
            return KILLED not in forb and RET not in forb
        if mode == "camp":
            return KILLED not in req and RET not in forb
        return not req & {KILLED, RET, DEAD}
    for node in nodes:
        node["Choices"] = [ch for ch in node["Choices"] if keep(ch)]
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
        alive_ok=False, living=None, living_groups=None, living_entry=None, living_title=None):
    """A physical scene in up to three hosts that never overlap. The veiled Camellia (killed) is met at her presence at the
    end of Fye's bar in Drezen; a Camellia raised from a retained death is back on her own companion hub (_camp). With
    `living` (extra requires), a third twin (_alive) gives the same scene to a Camellia who was never killed, on her
    companion hub: death is never the entry price of her romance. alive_ok is the older form for scenes the living and the
    raised Camellia share in one twin (the oath)."""
    groups = dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}
    SCENES.append(scene(id, title, "Camellia", 3, entry, _branch(nodes, "killed"),
                        requires=tuple(dict.fromkeys((*requires, KILLED, RET))), forbids=(CLOSED, *forbids),
                        delay=delay, last=5, optional=optional, Relationship=REL, Chapters=[3, 5], ContactUnit=UNIT,
                        Areas=[DREZEN], InteractionHub=PRESENCE, **groups))
    SCENES.append(scene(id + "_camp", title, "Camellia", 3, camp_entry or entry, _branch(nodes, "alive" if alive_ok else "camp"),
                        requires=tuple(dict.fromkeys(requires if alive_ok else (*requires, RET))),
                        forbids=(CLOSED, KILLED, *((DEAD,) if alive_ok else ()), *forbids), delay=delay, last=5,
                        optional=optional, Relationship=REL, AnswerLists=[HUB_LIST], ContactUnit=UNIT, **groups))
    if living is not None:
        lgroups = living_groups if living_groups is not None else any_groups
        lextra = dict(RequiresAnyGroups=[list(g) for g in lgroups]) if lgroups else {}
        SCENES.append(scene(id + "_alive", living_title or title, "Camellia", 3, living_entry or camp_entry or entry,
                            _branch(nodes, "alive"),
                            requires=tuple(dict.fromkeys((*[r for r in requires if r != RET], *living))),
                            forbids=(CLOSED, KILLED, DEAD, RET, *forbids), delay=delay, last=5, optional=optional,
                            Relationship=REL, AnswerLists=[HUB_LIST], ContactUnit=UNIT, **lextra))


def in_drezen(*ids):
    """Q8 (Sol CAN): a living-courtship scene staged in Drezen (the funeral below the citadel, the tavern by the gate) is
    kept to Drezen in Chapters 3 and 5; her companion hub travels with the party."""
    for s in SCENES:
        if s["Id"] in ids:
            s["Areas"] = [DREZEN]
            s["Chapters"] = [ch for ch in (s.get("Chapters") or [3, 5]) if ch != 4] or [5]


def city(*ids):
    """Q8 (Sol CAN/INT): scenes staged in Drezen (her quarters, the citadel, the lower city) keep their hub twins (_camp,
    _alive) to Drezen in Chapters 3 and 5, as the veiled twin already is: the companion hub travels with the party."""
    wanted = {i + suffix for i in ids for suffix in ("_camp", "_alive")}
    for s in SCENES:
        if s["Id"] in wanted:
            s["Areas"] = [DREZEN]
            s["Chapters"] = [ch for ch in (s.get("Chapters") or [3, 5]) if ch != 4] or [5]


# --- The line at the kill (P1 primers). Owlcat's inline mythic answers are the tone target. ---------------------------

JOKE = '[Play a cruel trick on Camellia] "Go on, then. Die convincingly. I\'ll know if you don\'t."'

SCENES.append(scene(P + "killed.setup_hub", "Die convincingly", "Camellia", 3, JOKE, [
    cam("start", '''{n}For a moment Camellia simply looks at you, head tilted, as if you had praised her gown in a language she does not speak. Then one corner of her mouth lifts.{/n}
"Convincingly? My friend, I have never done anything any other way."''',
        c("Continue", "spirits", requires=(BARGAINED,)),
        c("Continue", "game", requires=(GAME,), forbids=(BARGAINED,)),
        c("[Draw your weapon]", native_next=KILL_NEXT, forbids=(GAME,), flags=(PRIMED,))),
    cam("spirits", '''{n}Something at her back goes still, the way a hall goes still when the band stops. Her eyes flick to the bandage on your palm, and back to your face.{/n} "Oh," {n}she says softly.{/n} "Oh, you've been talking to them. Behind my back." {n}Her smile deepens.{/n} "Very well. Convincingly."''',
        c("Continue", "game", requires=(GAME,)),
        c("[Draw your weapon]", native_next=KILL_NEXT, forbids=(GAME,), flags=(PRIMED,))),
    cam("game", '''"Two lies and a truth, then, one last time." {n}She draws her knife and holds it up to the light, as if to judge its colour.{/n} "You are going to kill me. I am going to let you. I have never been so pleased with anyone in my life. Guess which one I made up."''',
        c("[Draw your weapon]", native_next=KILL_NEXT, flags=(PRIMED,)),
        c('"The last one. You\'ve been more pleased with a new pair of gloves."', "guess_pleased"),
        c('"The second. You\'re not going to let me. You\'re going to make me work for it."', "guess_let")),
    cam("guess_pleased", '''{n}She laughs, delighted, and shakes her head.{/n} "Wrong. The gloves were lovely, but they never told me to die convincingly." {n}She turns the knife so the light runs down it.{/n} "The lie was the second. I'm not going to let you. I'm going to make you earn every inch, and look you in the eye while you do. Otherwise how would I know you meant it?"''',
        c("[Draw your weapon]", native_next=KILL_NEXT, flags=(PRIMED,))),
    cam("guess_let", '''{n}Her smile goes very still, the way it does when a reading comes out right.{/n} "Oh, well done. Nobody ever guesses that one. They think a woman who says she'll let them means it." {n}She sets her feet.{/n} "So. You know the lie, and I know you know it. That makes the rest of this honest, which is more than most endings are."''',
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
"Convincingly. Commander, dead's dead. Where I come from we don't grade it." {n}She shrugs, and her hand is already on the knife at her belt.{/n} "Fine. I'll tell her. Might even be the last thing she hears."
''',
      c("[Give the order]", native_next=Q1_NEXT, flags=(PRIMED, BY_ORDER)), portrait="Anevia"),
    ], requires=("trickster",), forbids=(PRIMED, KILLED, DEAD), last=5, Relationship=REL, AnswerLists=[Q1_LIST],
    NativeReturnCue=Q1_RETURN, EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1),
    TricksterDevice=True, TricksterState="killed_by_commander"))


# --- The late fallback (R2-2): no line at the kill, so the Commander says it to the corpse, now, and pays for the lid. ---
# Chapters 3 and 5: a kill taken through the native verdict in Chapter 5 (FinalTruth) comes here on the same terms.

SCENES.append(scene(P + "killed.late_curtain", "Wrong flowers", "Memory", 3, "", [
    *lead([("start", nar, '{n}The crusade buried Camellia under a plain stone at the edge of the Drezen cemetery, with a wrong bunch of flowers: lilies, the white wedding kind. Tonight you stand over the stone with the sexton, a stooped man with a lantern, who wants a hundred crusade gold for opening the grave and forgetting what he finds.{/n}', None),
           ("lilies", nar, '''{n}You promised her, once, the wrong flowers on purpose. Somebody got there first, by accident. It feels like being robbed of a punchline.{/n}''', FUNERAL)],
          "choose"),
    nar("choose", '''{n}The sexton spits on his palms and waits.{/n}''',
        c("[Pay the sexton and lift the lid]", "coffin", crusade=("Finances", -100), flags=(P + "cost.sexton_paid",)),
        c('[Let the grave keep her] "Put the spade down. Leave her."', flags=(DECLINED, CLOSED))),
    nar("coffin", '''{n}The lid comes up with a groan of wet wood. She lies exactly as she was laid out, hands folded over the bone snake at her throat, chin lifted a fraction, like an actress who knows where the light falls. There is no smell. The sexton notices that, and crosses himself, and does not say anything.{/n}''',
        c('[Play a cruel trick on Camellia] "Go on, then. Die convincingly. This time I\'m watching."', "scroll",
          mythic="Trickster", flags=(PRIMED, LATE)),
        c('[Close the lid] "No. Let her stay dead."', flags=(DECLINED, CLOSED))),
    nar("scroll", '''{n}You cut your palm over her mouth and address the spirits that accompanied her in battle. There was no bargain to keep her. They answer slowly. A palm's blood will not buy a return now. You open the vein at your wrist, and the lantern dims at the edges of your sight. They take the rest as a promise: blood at every new moon, for as long as she chooses. Her chest moves. The sexton backs away from the coffin.{/n}''',
        c("Continue", "shut", flags=(BARGAIN_COST, BARGAINED, BARGAIN_LATE, RAISED))),
    nar("shut", '''{n}Camellia looks up from the coffin.{/n} "Put the lid back. If he is asked, he has seen nothing unusual." {n}She turns to the sexton.{/n} "Leave it loose. I have finished dying for tonight." {n}He lowers the lid with shaking hands. A breath escapes through the gap.{/n}''',
        c("[Walk back to the citadel]", "walk")),
    nar("walk", '''{n}The sexton walks with you to the cemetery gate, holding the lantern high. He stops there and asks you to find somebody else for the next burial. Nothing has ever laughed in one of his coffins before. He goes home without looking back. Later, you hear that his shutters stayed closed for three days.{/n}''',
        c("[Go home]")),
    ], requires=("trickster", KILLED, KILLED_CORPSE, "trickster.now"),
    forbids=(PRIMED, RET, DECLINED, BARGAINED, RAISED, P + "killed.late_curtain_prepared"), last=5, Relationship=REL, Remote=True,
    Chapters=[3, 5], Areas=[DREZEN], TricksterDevice=True, TricksterState="killed_by_commander"))   # PP2 (Sol CAN): the Drezen cemetery


# --- The third night (primed): the scroll read over her coffin. The device's operation, on the page. -----------------

SCENES.append(scene(P + "killed.third_night", "The third night", "Memory", 3, "", [
    nar("start", '''{n}Camellia's grave lies at the edge of the Drezen cemetery. The white lilies have begun to rot. Beside you, the sexton rests his spade against the stone and holds out a dirty hand. A hundred crusade gold for the digging, the lid, and his silence.{/n}''',
        c("[Pay the sexton 100 crusade gold and have him dig]", "coffin",
          crusade=("Finances", -100), flags=(P + "cost.sexton_paid",)),
        c('[Let the grave keep her] "Leave it. She stays where she is."', flags=(DECLINED, CLOSED))),
    nar("coffin", '{n}The sexton plants his spade beside the stone and begins to dig. Earth strikes the path at your feet.{/n}',
        c("[Dig]", "dug", requires=(BARGAINED,)),
        c("[Dig]", "unbargained", forbids=(BARGAINED,))),
    nar("unbargained", '''{n}The earth is silent all the way down. You lift the lid, and she lies exactly as she was laid out, hands folded over the bone snake at her throat. She is dead. A line spoken at a killing keeps nobody alive; nothing was ever asked of the spirits at her back to keep her.{/n}''',
        c("[Cut your palm over her mouth and bargain with her spirits now, on dearer terms]", "late_bargain", requires=("trickster",),
          flags=(BARGAIN_COST, BARGAINED, BARGAIN_LATE), alignment=("Evil", 1)),
        c('[Close the lid] "No. Let her stay dead."', flags=(DECLINED, CLOSED))),
    nar("late_bargain", '''{n}You speak to the spirits of battle she swore were always at her side, with your blood running between her lips. They are slow to answer, and when they do they name a dearer rate than they would have taken before she died: blood at every new moon, as she would have had it, and the first of it now, from the vein and not the palm, until the lantern-light goes grey at the edges. You open the vein. Her chest moves.{/n}''',
        c("Continue", "breath", flags=(RAISED,))),
    nar("dug", '''{n}As the spade reaches the coffin, something scratches against the wood. The sexton drops his lantern, retrieves it, and prises up the lid. Camellia's fingers catch its edge. The nails are torn; blood and pale pine splinters cling to the tips. She is breathing. She looks from you to the man holding the spade.{/n}''',
        c("Continue", "breath", flags=(RAISED,))),
    nar("breath", '''{n}Camellia lifts her chin. Her breath catches, then steadies. She smiles.{/n} "Wedding lilies. In this weather. You might at least have buried me with something fresh." {n}She looks past you at the sexton.{/n} "Put the lid back. If anybody asks, you found exactly what you expected. Go on. I shall find you when I am fit to be seen."''',
        c("[Put the lid back]", "home")),
    nar("home", '''{n}You walk the sexton back to the cemetery gate. He does not say anything. When you look back from the gate the lid is already a little askew, and the lilies on the grave have been rearranged, very neatly, by somebody with a strong opinion about flowers.{/n}''',
        c("[Go home]")),
    ], requires=("trickster.ever", PRIMED, KILLED, KILLED_CORPSE), forbids=(LATE, RAISED, RET, DECLINED), delay=72, last=5, Relationship=REL,
    Remote=True, Chapters=[3, 5], Areas=[DREZEN], TricksterDevice=True, TricksterState="killed_by_commander"))   # PP2: the cemetery


# --- The return, in person (R2-3): the veiled mourner at the end of Fye's bar. ---------------------------------------

PERFORMANCE_LEADS = [
    ("order", cam, '''"You sent that charming Mendevian thief to kill me, and a message with her. She delivered both. I must say, she was very thorough with the first, and she stumbled a little over the word 'convincingly'. I forgave her. One cannot expect poetry from a sergeant."''', BY_ORDER),
    ("late", cam, '"You bought a sexton\'s spade and his silence so you could address my corpse. I have been composing my reply since I woke. Do sit down. I intend to be very rude."', LATE),
    ("named", cam, '''"You once offered to give my poor spirit a name. I have taken one for myself instead." {n}The smile under the lace widens.{/n} "You will allow that I have a better claim to it than anyone."''', NAMED),
    ("invented", cam, '''"You made up a sergeant for me once, with a limp and a wife in Nerosyan and a laugh like a mule falling downstairs. I have made up a widow from Nerosyan. I thought you would appreciate the symmetry."''', INVENTED),
    ("kept_name", cam, '''"You told me once that Mireya was mine to keep. I have kept her. I am wearing her." {n}She touches the edge of the veil.{/n} "It suits me better than it ever suited her."''', NAME_LEFT),
    ("outlive", cam, '"You said you would rather I did not need a funeral. The sexton tells me mine was very well attended. I hope you were suitably disappointed."', OUTLIVE),
    ("wrong", cam, '"Your promised lilies were there. The sexton told me the chaplain wept. I asked whether he wept before or after collecting his fee." {n}She adjusts the veil.{/n} "I wish I had seen his face."', FUNERAL),
]
SCENES.append(scene(PERFORMANCE, "The veiled mourner", "Camellia", 3,
    '[Speak to the veiled mourner] "You\'re a long way from any grave I know of."', [
    cam("start", '''{n}The woman at the end of the bar wears black lace to the chin and carries lilies, the wrong ones. When she lifts the veil a finger's width, the smile under it is Camellia's, and so is the way she licks her lips before she speaks.{/n}
"Call me Mireya today. Camellia has a gravestone. I should hate to confuse the sexton."''',
        c("Continue", "who")),
    *lead([("who", cam, '"Do sit. Fye is pretending I am a widow from Nerosyan who drinks nothing and tips in silver. He is quite good at it. He has not asked my name. I shall keep tipping him while that lasts."', None),
           *PERFORMANCE_LEADS], "how"),
    cam("how", '''{n}Camellia loosens one black glove and lays it beside her untouched glass.{/n} "I suppose you want to know what you paid for."''',
        c("Continue", "how_late", requires=(LATE,)),
        c("Continue", "how_before", forbids=(LATE, BARGAIN_LATE)),
        c("Continue", "how_coffin", requires=(BARGAIN_LATE,), forbids=(LATE,))),
    cam("how_before", '''{n}She lays her hand on the bar. Strips of linen cover the fingertips; dried blood marks each one.{/n} "The spirits kept me three nights. Then I woke inside a nailed coffin. You had not mentioned that part." {n}She flexes her fingers and winces.{/n} "Next time, have the lid lifted before I ruin my hands."''',
        c("Continue", "why")),
    cam("how_coffin", '''"You told me to die convincingly, and I did, and nobody had asked my spirits for anything. So on the third night you came with a sexton and a spade and found me properly dead, and opened your own vein over my mouth, and haggled with them on their terms instead of yours." {n}She runs her tongue over her teeth.{/n} "I knew nothing about it until I woke with your blood in my mouth. You might have warned me. Whatever you meant by 'die convincingly', it wasn't this. I find I like this better."''',
        c("Continue", "why")),
    cam("how_late", '''"You told my corpse to die convincingly. How thoughtful of you." {n}She runs her tongue across her teeth.{/n} "The sexton told me you paid him to open the grave. I hope he asked enough. He looked quite ill when I breathed."''',
        c("Continue", "why")),
    cam("why", '''"The spirits gave me back because you paid. Coming here was my decision." {n}She turns the glass between two fingers.{/n} "I woke with your bargain fulfilled and my name on a gravestone. You had made quite a fool of me, my friend. I wanted to look at you while I decided whether to be offended." {n}Her smile widens.{/n} "I am still deciding."''',
        c("Continue", "primed")),
    cam("primed", '''"You told me to die convincingly, and I did. The sexton has given me a full account. The gravediggers complained about the weight. The chaplain wept. Everyone was convinced, except you, and the spirits who have had your blood."
{n}She presses something into your palm under the lilies: a small, clean knife, still warm from her glove.{/n} "Keep it. Next time, use it properly. And do not look for me. I shall find you. A dead woman keeps very flexible hours."
{n}Under the lace her mouth curves.{/n} "Do look disappointed when you leave. Fye is watching, and I have told him you promised to buy the widow supper."''',
        c('[Keep the knife] "I\'ll keep it close. Closer than you\'d like."', "register", flags=(RET, KNOWS, STARTED)),
        c('[Hand the knife back, point first] "Stay dead. It suits you."', "back")),
    cam("register", '''"One more thing, and then I'll let you go." {n}She turns her glass a quarter turn.{/n} "Camellia Gwerm is dead. That's the price of the trick, and it's mine to pay: whatever claim I had on my father's name and his house went into the ground with the lilies. I shall never be her again."
"But there's an empty box under that stone, and an empty box is a question. Sooner or later a sexton's boy or a grave-robber lifts the lid, and then somebody clever starts asking. It has to have something in it. Put it there yourself. Tonight."''',
        c("Continue", "will", requires=(WILL_GIVEN,)),
        c("Continue", "fill", forbids=(WILL_GIVEN,))),
    cam("will", '''"You gave me papa's will. He finally acknowledged his bastard, and now I am supposed to be dead." {n}She laughs into her glass.{/n} "I cannot present myself to his lawyers without spoiling your work. How tiresome. He recognized me at last, and I cannot enjoy it."''',
        c("Continue", "fill")),
    cam("fill", '''"There's a deserter hanging at the west gate, three days up, about my height once the crows have finished. Nobody will claim him. Or there are stones in the chapel wall, if you're squeamish, and you can hope nobody ever weighs the box." {n}She smiles.{/n} "I know which one I would do."''',
        c("[Cut the deserter down and carry him to her grave yourself]", "gallows", flags=(FILLED, GALLOWS), alignment=("Evil", 1)),
        c("[Weigh the coffin down with stones from the chapel wall]", "stones", flags=(FILLED,)),
        c('[Refuse] "No. I\'ve done enough digging for you."', "unsigned")),
    nar("gallows", '''{n}You do it after midnight, alone, with a borrowed cart and a knife for the rope. He is lighter than you expected. At the cemetery you open her grave with a spade, lift the lid on the empty box that still smells of lilies, and put him in it, and fold his ruined hands over his chest the way hers were folded. Then you fill it in. It takes until the bells. Nobody sees. You are nearly sure nobody sees.{/n}''',
        c("[Go and wash]")),
    nar("stones", '''{n}You do it after midnight, alone, prising loose stones from the back of the chapel wall where the mortar has gone soft, and carrying them to her grave in a sack, four trips. You open the box that still smells of lilies and lay them in it in the shape of a woman, and fill the grave in. It takes until the bells. The box is the right weight. Probably.{/n}''',
        c("[Go and wash]")),
    cam("unsigned", '''{n}She looks at you, and then folds her hands in her lap.{/n}
"How very correct." {n}The smile does not reach anywhere near her eyes.{/n} "Then somebody clever will open that box one day, and the dead woman at the end of Fye's bar will have to go somewhere nobody opens anything. Goodbye, my friend. It was a wonderful trick. You simply wouldn't finish it."''',
        c("[Let her go]", flags=(DECLINED, CLOSED))),
    cam("back", '''{n}She takes the knife by the blade, carefully, the way one takes a letter one has decided not to read.{/n}
"How disappointing. I was dead for you, my friend, and you did not even come to see the second act." {n}The veil comes down. When you look up from your hands, the stool is empty and the lilies are on the floor.{/n}''',
        c("[Let her go]", flags=(DECLINED, CLOSED))),
    ], requires=("trickster.ever", PRIMED, KILLED, RAISED), forbids=(RET, DECLINED), delay=0, last=5, Relationship=REL,
    Chapters=[3, 5], ContactUnit=UNIT, Areas=[DREZEN], InteractionHub=PRESENCE, TricksterDevice=True,
    TricksterState="killed_by_commander"))

# The letter twin, only when the presence failed (E12b runtime observation): one letter carries her return and her price.
SCENES.append(scene(P + "killed.performance_letter", "A letter from Mireya", "Memory", 3, "", [
    *lead([("start", nar, '''{n}The letter is on your pillow, which nobody could have reached without passing two guards and a locked door. The paper smells of lilies. Folded inside it, point down, is a small, clean knife. It is signed "Mireya".{/n}
"My friend. You told me to die convincingly, and I did. Everyone was convinced, except you. I would have told you so in person, but the tavern keeper you chose for me has gone somewhere, and I refuse to haunt an empty bar."''', None),
           ("order_l", cam, '''"You sent your Mendevian thief with a message. She delivered it very thoroughly. Tell her I bear her no grudge. Yet."''', BY_ORDER),
           ("late_l", cam, '"Your sexton showed me what you paid him. He seemed to think I ought to be grateful. I told him you were paying for his discretion, and asked how much of it he meant to sell me."', LATE)],
          "letter_why"),
    cam("letter_why", '''"I have been sleeping in the loft above a chandler's, among the tallow, very comfortably. The landlord thinks I am waiting for a husband with the Third Company. I have watched you twice from the window cross the square below, and you did not look up either, and I was quite hurt."
"But I forgive you. You told me to die convincingly. A person who asks for that deserves to be taken at their word, and then some."''',
        c("Continue", "price")),
    cam("price", '''"Since I cannot trust you to find me, my price for staying comes by post. Camellia Gwerm is dead, her name and her father's house with her; that part of the trick is mine to pay. I have seen to the empty box myself, with stones, and ruined a perfectly good pair of gloves doing it. So: your blood, or your name. Your blood from my knife whenever the flies want it, or your name at the top of my list, the first friend I kill if I ever need one. Write which on the back of this and leave it on your pillow. I shall know."''',
        c('[Write back "My blood"] "Whenever you ask. From your knife. I won\'t flinch."',
          flags=(RET, KNOWS, STARTED, BLED, TERMS)),
        c('[Write back your own] "If you ever need to kill a friend, start with me."',
          flags=(RET, KNOWS, STARTED, MARKED, TERMS)),
        c("[Burn the letter]", flags=(DECLINED, CLOSED))),
    ], requires=("trickster.ever", PRIMED, KILLED, RAISED, PRESENCE_FAILED), forbids=(PERFORMANCE, RET, DECLINED), delay=96,
    last=5, Relationship=REL, Remote=True, Chapters=[3, 5], TricksterDevice=True, TricksterState="killed_by_commander"))


# --- Dead otherwise: the same spoken-death lie, told at the body. She names her price before she rises. ---------------

SCENES.append(scene(P + "dead.overacting", "Curtain call", "Memory", 3, "", [
    nar("start", '''{n}The report is two lines long: the shaman Camellia Gwerm, fallen in the rearguard action, body retained with the baggage for burial at the next halt. The chaplain has written "may she find peace" at the bottom, and then, apparently on reflection, crossed out "peace" and written "rest".{/n}''',
        c("[Go to the wagons]", "wagons")),
    nar("wagons", '''{n}They have laid Camellia out under a cloak by the supply wagons. Even dead she looks as though she is waiting for applause: one hand at her throat, one flung out, her hair arranged by nobody. The spirits she fed have gone very quiet around her. The camp's dogs will not come near the wagons.{/n}''',
        c('[Tell the corpse it\'s overacting] "Get up, Camellia. You\'re overdoing it, and the audience is leaving."',
          "waking", mythic="Trickster", forbids=(BARGAINED,)),
        c('[Let her lie] "Take your bow. The curtain\'s down."', flags=(DECLINED, CLOSED)),
        c('[Tell the corpse it\'s overacting] "Get up, Camellia. You\'re overdoing it, and the audience is leaving."',
          'waking_paid', mythic='Trickster', requires=(BARGAINED,))),
    cam("waking", '''{n}Her eyes stay shut. Her lips barely move.{/n}
"Rude. I was resting." {n}A pause, like a held breath that has nowhere to go.{/n} "My spirits were promised a death, my friend. Mine. If you take it back from them, they will want paying, and they are very particular. Not with some stranger. With you."
"Your blood, in my bowl, from my knife, every new moon for as long as I choose. And you will keep your hand flat on the table, and your eyes on mine."''',
        c('[Agree to her price] "Every new moon. Just get up."', revive="camellia", flags=(RET, OWED, STARTED)),
        c('[Refuse her price] "No. Not my blood, not for this."', "refused")),
    cam("refused", '''"Then I shall stay exactly where I am. It is quieter here than it has been in years." {n}The corner of her mouth moves, very slightly.{/n} "You have interrupted a most agreeable silence. How like you. Now go away, and let me enjoy it."''',
        c("[Let her lie]", flags=(DECLINED, CLOSED))),

    cam("waking_paid", '''{n}Her eyes remain shut. Her lips move.{/n} "You made a bargain for your own hand, or your own order. This was neither. How disappointing for you." {n}A faint smile.{/n} "If you want me back from this, you must ask me. Your blood, in my bowl, from my knife, every new moon for as long as I choose. Keep your hand flat on the table. I want to watch your face."''',
        c('[Agree to her price] "Every new moon. Just get up."', revive="camellia", flags=(RET, OWED, STARTED)),
        c('[Refuse her price] "No. Not my blood, not for this."', "refused")),
], requires=("trickster", "trickster.ever", DEAD), forbids=(KILLED, RET, DECLINED),
    last=5, Relationship=REL, Remote=True, Chapters=[3, 5], Recovery="camellia", TricksterDevice=True,
    TricksterState="dead_otherwise"))


# --- Her price (terms) and her test (the commit). Both in person; her refusal is reachable on every branch. -----------

TERMS_LEADS = [
    ("bowl", cam, '"You held the bowl and watched me pour it out again. Not a drop missing. You were very attentive, my friend. I wondered what you would do with what you saw."', BOWL_HELD),
    ("fed", cam, '''"In the Abyss, when the flies were loud, you sent me east to bleed demons, as if that would quiet them. It didn't. Demons aren't friends; there's nothing in their eyes when they understand. But you knew exactly what I was, and you pointed. I have been waiting ever since to see whether you would pretend otherwise."''', FED),
    ("dug", cam, '''"Your little thief is still digging after that porter in the lower city. She is very good. Tell her to stop before she reaches the bottom, or I will have to be very good too."''', INVESTIGATED),
    ("covered", cam, '''"'Deserters.' You wrote it yourself. I read it in the register and laughed until the spirits hushed me. You lie beautifully for a murderer, my friend."''', COVERED),
    ("steady", cam, '''"You held my knife at my throat, and your hand did not shake. I have been thinking about your hand ever since. It is a very inconvenient thing to think about."''', STEADY),
    ("flinched", cam, '''"You flinched, when I put my knife in your hand and my throat under it. I have forgiven you. I forgive very little, so you may treasure it."''', FLINCHED),
]
met(P + "returned.terms", "What a dead woman wants", '"You said you would find me. You didn\'t. I found you."', [
    cam("start", '''"The friends I kill are the only thing that quiets the flies. Not all of them. The right ones, at the right moment, when they understand." {n}She says "flies" the way other women say "my headaches", with a small apologetic flutter of the hand.{/n} "You are still alive, which is unusual. And I find the flies are very loud."''',
        c("Continue", "flies")),
    cam("flies", '''"I called it the spirits' hunger because people were so willing to excuse it." {n}She taps her temple.{/n} "The noise is mine. Killing an enemy does nothing. I want the moment a friend understands, and I want to be close enough to watch. You know that now. Decide what you intend to do with it."''',
        c("Continue", "lead")),
    *lead([("lead", cam, '''"So I have been thinking about what to do with you. I think best in cemeteries and knife shops, and I have visited both."''', None),
           *TERMS_LEADS], "price"),
    cam("price", '''"So. My price for staying. Your blood, or your name."
{n}She leans in until the lace of her sleeve brushes your wrist.{/n} "Your blood: from my knife, into my bowl, whenever the flies want it, and you keep your hand on the table and watch me take it. Or your name: the promise that if I ever need to kill a friend, I start with you. Either is a gift. I will know which one you meant."''',
        c('[Give her your blood] "Whenever you ask. From your knife. I won\'t flinch."', "named", flags=(BLED, TERMS)),
        c('[Give her yours] "If you ever need to kill a friend, start with me. I\'ll make it interesting."', "mine",
          flags=(MARKED, TERMS)),
        c('"No names. No knives. Not in my crusade."', "none")),
    cam("named", '''"Your blood." {n}She takes your wrist and turns it to the lamp, and runs her thumbnail very lightly along the vein, the way a jeweller runs a nail along a seam.{/n} "You didn't even hesitate. That's either very brave or very foolish, and I shall find out which." {n}She lets go, and stands.{/n} "Three nights. Wear something with a loose sleeve."
{n}At the door she turns.{/n} "How generous. I shall discover whether your generosity survives the knife."''',
        c("[Watch her go]")),
    cam("mine", '''{n}For once she has no answer ready. She studies your mouth, then your hands, and whatever she is looking for, she seems to find it, because she laughs, softly, and only once.{/n}
"Oh, you are dreadful. Nobody has ever offered before. They only ever found out." {n}She stands.{/n} "Three nights. Sleep lightly."
{n}At the door she turns, and looks at your throat for a long moment.{/n} "You understand what you've done? You've put yourself at the top of my list. Do try to justify the distinction. I should be most disappointed if you became dull."''',
        c("[Watch her go]")),
    cam("none", '''"Not in your crusade." {n}She repeats it, smoothing her cuff.{/n} "Very well. I shall continue killing demons for you. You need not trouble yourself about whom I visit afterward. Our little arrangement is over."''',
        c('[End the arrangement]', flags=(CLOSED,))),
], requires=("trickster.ever", RET, LESSON), forbids=(TERMS,), delay=48, living=(),
   living_entry='"Camellia. You said you had a price."', living_title="What she wants")

TEST_LEADS = [
    ("knife", cam, '''"You found the knife under my skirt when we danced, and you did not pretend you hadn't. Nobody asks. They only ever find out."''', KNIFE_NOTICED),
    ("touched", cam, '''"You touched me once in the salle by lying with your whole body. I have wanted to know ever since what your body says when it is not lying."''', TOUCHED),
    ("she_won", cam, '''"You lost my game once. Two lies and a truth, and you let the lie walk straight past you. Let us see whether you lose this one."''', SHE_WON),
    ("danced", cam, '''"You danced with me once, with this under my skirt. You never once looked down. I noticed that. I notice everything that does not look down."''', DANCED),
    ("out_lied", cam, '''"You beat me at my own game once, with three truths I took for lies. I have been waiting ever since to see whether your face can lie as well as your mouth."''', OUT_LIED),
]
met(P + "returned.test", "A knife at the right height", '"Come to your quarters tonight. Alone. Bring the knife I gave you."', [
    nar("start", '''{n}Your quarters are dark, and not empty.{/n}''',
        c("Continue", "bowl", requires=(BLED,)),
        c("Continue", "throat", forbids=(BLED,))),
    cam("bowl", '''{n}The silver bowl is on your table, polished, empty. Camellia sits on the edge of your bed with your wrist in her lap and her small clean knife laid along the inside of it, flat, cold, not yet cutting.{/n}
"You promised me your blood whenever I asked. I'm asking now." {n}She turns the blade, very slowly, until the edge rests on the vein.{/n} "I want to watch your face while I take it. I want to see how much you'll let me have before you stop me. Don't disappoint me, my friend."''',
        c("Continue", "lead_c")),
    cam("throat", '''{n}You wake to a weight on your chest and cold steel under your jaw. She is smiling, and her eyes are wide open, watching for the thing she has always watched for.{/n}
"You told me to start with you. I am a woman of my word."''',
        c("Continue", "lead_t")),
    *lead([("lead_c", nar, '''{n}The first cut is shallow and very neat. The blood runs down into the silver, and she does not watch it. She watches you.{/n}''', None), *TEST_LEADS], "judge_c"),
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
    cam("steady", '''"There. That face. Not dread. Not fury. Interest." {n}The knife goes away. She ties a strip of her own lace round your wrist, very tightly, whether or not anything there is bleeding, and does not once look at her own handiwork.{/n}
"I have killed every friend I ever had. I haven't decided about you. Let's call it an experiment, and see how long it runs."''',
        c('[Ask her to stay] "Then stay."', "yes", requires=(RET,)),
        c('[Ask her to stay] "Then stay."', "yes_a", forbids=(RET,)),
        c("[Ask her to put the knife away for good]", "no")),
    cam("blade", '''"Oh, good." {n}Neither of you moves. Two points, one breath.{/n} "Someone who cuts back. You have no idea how rare that is. The spirits are quite beside themselves. So am I, a little."''',
        c('[Ask her to stay] "Then stay."', "yes", requires=(RET,)),
        c('[Ask her to stay] "Then stay."', "yes_a", forbids=(RET,)),
        c("[Ask her to put the knife away for good]", "no")),
    cam("guard", '''"Guards. How terribly ordinary." {n}By the time the door opens, the window is open instead, and the lace caught on the sill is the only thing left of her.{/n}''',
        c("[Let her go]", flags=(GUARD, CLOSED))),
    cam("yes", '''"Stay? My friend, I never left. I simply stopped lying down." {n}She slides her knife into your belt, hilt first, and leaves her hand there.{/n} "Keep it close. One day I shall want it back, and you will know the day, because I shall be smiling."''',
        c("[Keep it]", "threshold", flags=(COMMITTED,))),
    cam("yes_a", '''"Stay?" {n}She laughs, softly, as if you had said something charming in a language she is still learning.{/n} "I've been staying all along, my friend. You simply never asked me in so many words." {n}She slides her knife into your belt, hilt first, and leaves her hand there.{/n} "Keep it close. One day I shall want it back, and you will know the day, because I shall be smiling."''',
        c("[Keep it]", "threshold", flags=(COMMITTED,))),
    nar("threshold", '''{n}She does not take her hand away. She takes your belt instead, and walks you backwards by it until the edge of the bed stops you, and then she pushes you down onto it and leans over you with her skirts in her fists and the knife's hilt digging into both of you.{/n}
{n}She kisses the way she talks, politely and then not at all. Her teeth find your lower lip and test it, exactly as hard as she means to. Her breath is quick and hot and smells of lilies and iron. When your hands find the laces at her back she makes a small, pleased sound and does not help, and when the last one gives she catches your wrist and holds your palm flat over her heart, so you can count it with her. It is going very fast.{/n}
"Beat," {n}she whispers against your mouth.{/n} "Beat. Beat."
{n}You count with her. Then she is done counting. She tears the last knot of her laces out herself and shoves the dress down off her shoulders, and the lamp finds the white skin and the old fine scars, and she lets you look for exactly as long as she chooses. Her hands go to your belt, with a thief's quick economy, and she watches your face while she undoes it, lips parted, the tip of her tongue just visible.{/n}
"Still beating," {n}she whispers, hoarse, and the polish is entirely gone.{/n} "Mine is going to burst out of my chest. Tell me I am not the only one."''',
        c("[Put out the lamp.]", "morning")),
    nar("morning", '''{n}Grey light. The knife is on the pillow between you, point towards the door, where she put it some time in the night. She is awake, lying on her side, watching your face with her chin on her folded hands.{/n}
"You slept," {n}she says, as if reporting a fault in a lock.{/n} "With me in the bed and my knife on the pillow. You slept like a child. The others lay awake. I could always hear them lying awake, and I always knew why."
{n}She reaches out and touches your eyelid with one fingertip, very lightly, as if to make sure it is real, and then lets it rest there, on the thin skin over your eye, the way she rests her thumb on a blade to feel its edge.{/n} "Next time I shall stay awake and watch you do it. I want to know how long a person can sleep beside a knife before it stops being bravery and becomes a habit. Habits are so much easier to break."''',
        c("[Close your eyes again]")),
    cam("no", '''{n}Her smile does not move, which is worse than if it had.{/n}
"Without the knife? You want the woman and not the appetite. There is no such woman. There was, once, and her name was Mireya, and I made her up."''',
        c("[Watch her go]", flags=(TAME, CLOSED))),
], requires=("trickster.ever", RET, TERMS), forbids=(COMMITTED,), delay=72, living=())
city(P + "returned.terms", P + "returned.test")


# --- Optional: the oath (ledger 05 row 12): a woman Camellia herself killed, walking again. --------------------------

NR, ND = "nurah.trickster.returned", "nurah.dead_camellia"

met(P + "kills_answered.oath", "The kill that didn't take", '"You look like someone who has been told a secret. Tell me."', [
    cam("start", '''"I remember the taste of that death. I remember it very clearly. And yet I hear..."''',
        # Exactly one route is ever shown: Nurah first, then Soana, then Kaylessa (the pairs of Derived kill_returned).
        c("Continue", "nurah", requires=(NR, ND)),
        c("Continue", "soana", requires=("camellia.kill_returned.soana",), forbids=(ND,)),
        c("Continue", "soana", requires=(ND, "camellia.kill_returned.soana"), forbids=(NR,)),
        c("Continue", "kaylessa", requires=("kaylessa.trickster.returned", "kaylessa.camellia_killed"),
          forbids=("camellia.kill_returned.earlier",)),
        # Structural fallback, never shown in a real world (kill_returned always carries one of the pairs above): it keeps
        # the old default (Soana) for a bare kill_returned key.
        c("Continue", "soana", forbids=(ND, "camellia.kill_returned.soana", "kaylessa.trickster.returned"))),
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
    cam("kaylessa", '''"...that the poor elf I helped on her way is sitting under a tailor's awning in the market, wrapped to the eyes, watching everybody's hands. I gave her such privacy, you know. At the end she looked at me as though I were the first honest person she had met in years. It was very touching." {n}Camellia sighs.{/n} "And now she watches my hands, of all people's. You did this. Of course you did."''',
        c("Continue", "ask")),
], requires=("trickster.ever", "camellia.kill_returned"), delay=0, optional=True, alive_ok=True)


# --- Epilogue pages (Owner CamelliaEpilogue; ordered siblings; no effects). -------------------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}The crusade's chroniclers wrote that once the war had ended Camellia grew bored, and on a moonless night simply vanished. She read the line over the Commander's shoulder and was enormously pleased with it. She had vanished from the chroniclers, which was all she had ever wanted from them, and she went on vanishing every evening into the Commander's rooms.{/n}", forbids=(KILLED,)),
    p("{n}The same chroniclers wrote that years later she came back, and left again, because she was afraid of what she wanted to do to the one she loved. The Commander read that page aloud to her at breakfast. She said it was the only true line in the book, and that the leaving was a detail.{/n}", requires=(ROMANCE,), forbids=(KILLED,)),
    p("{n}Once a year she named a date, and the Commander found her a stranger nobody would miss, as promised over a glass of wine a lifetime ago. Neither of them ever said who.{/n}", requires=(OATH_FED,)),
    p("{n}She kept the Commander's name as her price, and said so at dinner parties, and everyone laughed, and she did not.{/n}", requires=(MARKED,)),
    p("{n}The Commander wore long sleeves in every season, and never said why. Under them, along the inside of one wrist, ran a ladder of fine white scars, one for every time she had asked.{/n}", requires=(BLED,)),
    p("{n}Somewhere in Drezen a body was found, one year, with no wounds but one, very neat, right where a friend would stand. The report said deserters. It was in the Commander's hand.{/n}", requires=(COVERED,)),
    p("{n}Anevia never stopped looking for the lower-city killer. She never found anyone, and she never quite believed that.{/n}", requires=(INVESTIGATED,)),
    p("{n}Once, when the Commander had been gone a season, she was found in the dark of the citadel with a knife in one hand and the other flat on the Commander's empty pillow, counting. Nobody asked her what.{/n}", requires=(NOT_TODAY,)),
    p("{n}She had been entered in the crusade's register as dead, and never troubled to correct it. Every year on the date of her funeral she laid wrong lilies on her own grave, and read the stone aloud, and corrected the spelling.{/n}", requires=(KILLED,)),
    p("{n}The grave at the edge of the Drezen cemetery still bears her name. The Gwerm estate went to a cousin the lawyers found. What lies in her coffin, only two people ever knew, and she never once asked for her name back.{/n}", requires=(FILLED,)),
    p("{n}Some nights the Commander still dreamed of the weight of a hanged man on a borrowed cart.{/n}", requires=(GALLOWS,)),
    p("{n}In Nerosyan, a widow named Mireya Voss kept a rented house for many years, and paid her taxes, and was said to have been married to a wine merchant who died of eels. Nobody ever saw her husband's grave.{/n}", requires=(NEW_NAME,)),
    p("{n}Over the Commander's bed hung a charcoal rubbing of a gravestone, framed. Guests who asked about it were told it was a family memorial, and that the family member in question was in the next room.{/n}", requires=(OLD_NAME,)),
    p("{n}The cells under the citadel were never quite used again. The guards said a prisoner had died down there of a failure of the heart, and that the last one to hear him had heard him laughing, and then not laughing.{/n}", requires=(PRISONER_HERS,)),
    p("{n}She never stopped asking. Once a season she would find a prisoner nobody loved and bring the Commander to the cell door and ask. The Commander said no. She said thank you, and waited for the next one. She was very good at waiting.{/n}", requires=(PRISONER_SPARED,)),
    p("{n}She kept the list on the Commander's shelf all her life. Nobody on it ever changed.{/n}", requires=(LIST_KEPT,)),
    p("{n}On a shelf in the Commander's rooms hung a little bone snake on a cord. Visitors were told it held a very old and very beautiful spirit. The Commander never said otherwise.{/n}", requires=(AMULET_KEPT,)),
    p("{n}A witness who had once seen a dead woman in church lived to a great age in Drezen, telling children about the singing ghost with the dog made of mist.{/n}", requires=(WITNESS_LIED, KILLED)),
    p("{n}There was a railing on the river steps now. People said somebody had fallen there, once, in the dark.{/n}", requires=(WITNESS_HERS,)),
    p("{n}A banner-mender named Ilse married her sergeant of the Third Company and kept, all her life, a horror of coughing ladies. She never knew why she had once been told to stay away. She lived to see her grandchildren.{/n}", requires=(FRIEND_WARNED,)),
    p("{n}A banner-mender named Ilse took walks every evening with a veiled lady for three years. Every evening the Commander waited for her to come home, and watched her face when she did. Ilse married her sergeant in the spring. Camellia sent the flowers: white lilies, the wedding kind. Whether that was a gift or a promise, nobody ever found out. Least of all Ilse.{/n}", requires=(FRIEND_WATCHED,)),
)
SCENES.append(scene(P + "epilogue.kept", "", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}Camellia Gwerm stayed at the Commander's side through the Threshold and after it, a lady in black whom no one could quite remember being introduced to, and she kept the small clean knife where the Commander could always see it. She never killed the Commander. She never said she wouldn't.{/n}
{n}She took no new friends, or said she took none. Once a year, on a date she would never explain, she brought the Commander breakfast on the point of a knife, and the Commander ate it without looking, and she watched, and neither of them ever grew tired of it.{/n}
{n}People who dined with the two of them in later years said it was the most courteous evening they had ever sat through, and that they could never afterwards remember what either of them had said, only that both of them had been smiling, and that neither had once looked away from the other.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED, KILLED, DEAD, KICKED),
    ForbidOverrides={"sacrifice": "trickster.commander_back", KILLED: RET, DEAD: RET, KICKED: P + "killed_held"}, **EP))   # Q8: and she is still with us

SCENES.append(scene(P + "epilogue.kept_on_record", "", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}When the Commander was entered among the dead of the Threshold, a veiled woman came to the memorial with lilies, the wrong ones, and stood at the back, and did not weep. Afterwards the chaplain found her knife laid on the altar, point towards the door. Those who knew Camellia said it was the only time she ever gave anything back.{/n}''')],
    requires=("trickster.ever", COMMITTED, "sacrifice"), forbids=("trickster.commander_back", CLOSED, KILLED, DEAD, KICKED),
    ForbidOverrides={KILLED: RET, DEAD: RET, KICKED: P + "killed_held"}, **EP))

SCENES.append(scene(P + "epilogue.commit", "The knife, returned", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Camellia finished her test. She finished it anyway. On one moonless night the next spring she let herself into the Commander's rooms, laid a small clean knife on the pillow, point towards the door, and sat down to wait. She was still there in the morning. She said she had decided, on her own terms, that the Commander was more interesting alive. She did not say for how long.{/n}
{n}She stayed. She kept the knife on the pillow between them, point towards the door, every night of her life, and every morning she looked at the Commander asleep, and at the knife, and was never sure which of them she was waiting on.{/n}
{n}In the first spring of the peace a name was crossed off the list she carried in her sleeve, in her small schoolroom hand. It was a stranger's. The Commander's stayed where she could see it.{/n}''')],
    requires=("trickster.ever", TERMS), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice", KILLED, DEAD, KICKED),
    ForbidOverrides={"sacrifice": "trickster.commander_back", KILLED: RET, DEAD: RET, KICKED: P + "killed_held"}, **EP))

# Q8 (Sol INT): her test was never finished, and the Commander stayed dead.
SCENES.append(scene(P + "epilogue.commit_on_record", "The knife, unreturned", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}The war ended before Camellia finished her test, and the Commander was entered among the dead of the Threshold before she could set it. She came to the memorial veiled, with lilies, the wrong ones, and stood at the back through every prayer. The chaplain said afterwards that she had been the only mourner in the hall with dry eyes, and the only one who stayed until the candles were out. Nobody ever saw her in Drezen again. A small clean knife was found on the Commander's empty pillow, point towards the door, and nobody could say who had left it.{/n}''')],
    requires=("trickster.ever", TERMS, "sacrifice"), forbids=(COMMITTED, CLOSED, DECLINED, "trickster.commander_back", KILLED, DEAD, KICKED),
    ForbidOverrides={KILLED: RET, DEAD: RET, KICKED: P + "killed_held"}, **EP))

SCENES.append(scene(P + "epilogue.refused", "Lace on the sill", "CamelliaEpilogue", 6, "", [
    nar("page", '''{n}Camellia never came back. Each year, on the day she left, someone laid lilies on the Commander's step: the wrong ones, for a wedding. The guards stopped asking who.{/n}''',
        paragraphs=(p("{n}The Commander kept the knife she had given, and never learned whether it had been a gift or a reminder.{/n}", requires=(KNOWS,)),
                    p("{n}The Commander carried a row of thin white scars across one wrist all their life, one for every new moon of a single winter, paid to spirits who were never collected.{/n}", requires=(OWED,)),
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
    ], requires=(RET, LESSON), forbids=("anevia_gone", DEAD, INVESTIGATED, COVERED), delay=24, last=5, Relationship=REL,
    Reaction=True, Chapters=[3, 5], AnswerLists=[ANEVIA_LIST], ForbidOverrides={"anevia_gone": "anevia.trickster.returned", DEAD: RET}))

SCENES.append(reaction("Regill", P + "react.regill_grave", (RET, KILLED, "regill.in_party"),
    '''"The Gwerm woman is walking Drezen in a veil. The crusade's register lists her as buried." {n}Regill does not raise his voice. He never needs to.{/n} "Your register contradicts your own watch, Commander. I have ordered the discrepancy investigated, and I have noted whatever she is."''',
    answer_list=REGILL_LIST, forbids=REGILL_GONE, entry='"About Camellia..."', chapter=3, last=5, portrait="Regill"))
SCENES.append(reaction("Regill", P + "react.regill_quarters", (COMMITTED, "regill.in_party"),
    '''"The Gwerm woman sleeps in your quarters now. The watch reports your door barred from the inside, and the lamp lit past the second bell." {n}Regill's voice does not change. It never does.{/n} "I do not care whom you share a pillow with, Commander. I care that people she smiles at have a habit of turning up in alleys with one wound, very neat. I have told the watch to knock twice at your door. If nobody answers the second knock, they are to break it."''',
    answer_list=REGILL_LIST, forbids=(*REGILL_GONE, DEAD), entry='"About Camellia..."', chapter=3, last=5, portrait="Regill",
    ForbidOverrides={DEAD: RET}))
SCENES.append(reaction("Regill", P + "react.regill_covered", (COVERED, "regill.in_party"),
    '''"A body in the lower city with one wound and a clerk's note that says 'deserters'. Deserters run, Commander. They are not laid out." {n}He folds his hands behind his back.{/n} "You signed a lie over a murder. I will not ask by whom. I will remember that you did not."''',
    answer_list=REGILL_LIST, forbids=(*REGILL_GONE, DEAD), entry='"About the lower city..."', chapter=3, last=5, portrait="Regill",
    ForbidOverrides={DEAD: RET}))
SCENES.append(reaction("Regill", P + "react.regill_dug", (INVESTIGATED, "regill.in_party"),
    '''"Your sergeant is digging after the lower-city killer. Good. Tell her to take two of mine." {n}He considers the map on the wall as though it had disappointed him.{/n} "Whoever did that has done it before, and will not stop at the one."''',
    answer_list=REGILL_LIST, forbids=(*REGILL_GONE, DEAD), entry='"About the lower city..."', chapter=3, last=5, portrait="Regill",
    ForbidOverrides={DEAD: RET}))


def integrate(payload):
    """Register the relationship's own keys, its presence, its revival and derived keys; keep current death blocking the
    nine other-route Camellia reactions (condition-only, engine-q3)."""
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    # eng3-ab already observes the native retained-death etude in a timed latch.
    # Read that receipt directly: Derived flags have no persisted timestamp.
    # Current KILLED_CORPSE still excludes unresolved combat and living actors.
    for host in payload["Scenes"]:
        if host["Id"] in (P + "killed.third_night", P + "killed.late_curtain_prepared"):
            host["Requires"].append(P + "native_death_observed")
    seen = payload.setdefault("SeenCues", {})
    for key, cues in SEEN_CUES.items():
        if seen.get(key, cues) != cues:
            raise ValueError("Conflicting seen-cue binding: " + key)
        seen[key] = list(cues)
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
            # CamelliaNotInParty_Dead reads current life, not her historical kill.
            # Resurrection clears it; a later death must block these nine hub reactions again.
            scene_.setdefault("ForbidOverrides", {}).pop(DEAD, None)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'camellia.trickster.killed.performance',
    'camellia.trickster.killed.performance_letter',
    'camellia.trickster.killed.third_night',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
# eng8-q8d: Chapter 5 failed placement gets the reunion and its existing price
# at the coffin, inside the delivery that paid for her breath. Chapter 3 stays.
def _eng8_coffin_reunion():
    import copy
    letter = next(s for s in SCENES if s['Id'] == P + 'killed.performance_letter')
    letter['MaxChapter'] = 3
    letter['Chapters'] = [3]
    for sid, terminal in [('killed.third_night', 'home'), ('killed.late_curtain', 'walk')]:
        host = next(s for s in SCENES if s['Id'] == P + sid)
        end = next(n for n in host['Nodes'] if n['Id'] == terminal)
        old = end['Choices'][0]
        old['Forbids'] = list(dict.fromkeys(old['Forbids'] + ['irabeth.chapter_five']))
        end['Choices'].append(c('[Go home]', requires=('irabeth.chapter_five',), forbids=(PRESENCE_FAILED,)))
        end['Choices'].append(c('[Turn back to the coffin]', 'eng8.reunion',
                                requires=('irabeth.chapter_five', PRESENCE_FAILED)))
        price = copy.deepcopy(next(n for n in letter['Nodes'] if n['Id'] == 'price'))
        price['Id'] = 'eng8.price'
        price['Text'] = ('"Then hear my price here. Camellia Gwerm is dead, her name and her father\'s house with her; '
                         'that part of the trick is mine to pay. Stones will keep my place in the box. Your blood '
                         'from my knife whenever the flies want it, or your name at the top of my list: the first '
                         'friend I kill if I ever need one. Choose."')
        for ch in price['Choices']:
            ch['Text'] = ch['Text'].replace('[Write back "My blood"]', '[Offer your blood]').replace('[Write back your own]', '[Offer your name]').replace('[Burn the letter]', '[Leave her]')
        host['Nodes'].extend([
            cam('eng8.reunion', '''{n}She has lifted the lid again. When you turn back, her fingers close around your wrist.{/n} "No. Stay. I have no wish to hunt you through a city full of crusaders tonight."''', c('Continue', 'eng8.price')),
            price])

_eng8_coffin_reunion()
# end eng8-q8d


# Authored history variant: preparation keeps the paid three-night promise even without the taunt.
_late_original = next(s for s in SCENES if s["Id"] == P + "killed.late_curtain")
_late_prepared = copy.deepcopy(_late_original)
_late_prepared["Id"] = P + "killed.late_curtain_prepared"
_late_prepared["Requires"] = list(dict.fromkeys([*_late_original["Requires"], BARGAINED]))
_late_prepared["Forbids"] = [k for k in _late_original["Forbids"] if k not in (BARGAINED, _late_prepared["Id"])]
_late_prepared["Forbids"].append(_late_original["Id"])
_late_prepared["DelayHours"] = 72
_prepared_nodes = {node["Id"]: node for node in _late_prepared["Nodes"]}
_prepared_nodes["start"]["Text"] = "{n}Camellia's grave lies at the edge of the Drezen cemetery. The white lilies have begun to rot. Beside you, the sexton rests his spade against the stone and holds out a dirty hand. A hundred crusade gold for the digging, the lid, and his silence.{/n}"
_prepared_nodes["scroll"]["Text"] = "{n}You uncover the bowl's old scar on your palm. The spirits' three nights are over. Camellia draws a breath and opens her eyes. She watches you lower your uncut hand.{/n}"
_prepared_nodes["scroll"]["Choices"][0]["Set"] = [BARGAINED, BARGAIN_COST, RAISED]
SCENES.append(_late_prepared)

# The living terms/test refusal is personal closure, not native dismissal.
_refused = next(s for s in SCENES if s["Id"] == P + "epilogue.refused")
SCENES.append(scene(P + "epilogue.refused_living", "Lace on the sill", _refused["Owner"], 6, "", [
    nar("page", '''{n}Camellia continued fighting in the crusade after the Commander ended their arrangement. In company she remained impeccably courteous. The guards still checked the alleys behind the citadel, and nobody mistook her courtesy for forgiveness.{/n}''',
        paragraphs=tuple(copy.deepcopy(para) for para in _refused["Nodes"][0]["Paragraphs"]
                         if TAME in para["Requires"] or GUARD in para["Requires"]))],
    requires=("trickster.ever", CLOSED, "camellia.life.available", "camellia.present_now"),
    RequiresAnyGroups=[[P + "returned.terms_alive", P + "returned.test_alive"]],
    forbids=(RET, DECLINED, KILLED, DEAD, KICKED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))
