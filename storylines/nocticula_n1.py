"""N1 structure from Claude N0 §4; authored dream device, prose reserved for N2–N5.

This module changes only the Nocticula graph. Existing choices retain their
indices and effects; newly authored beats are visibly unfinished placeholders.
"""
from copy import deepcopy

from story_format import c, n, p

RETIRED = frozenset("lamp_measure white_shoes voices_in_glass cost_of_return after_the_lamps mask_and_bell closed_gallery counterseal".split())
RETIRED_TEXT = "{n}(Retired: this meeting is folded into the next live meeting.){/n}"
NEW_FLAGS = tuple("noct." + x for x in "retired flower_real_seen orren_lie_caught orren_hand_taken captain_sold crimson_mark mark_shown mark_hidden ilvara_shamed orren_carries returned_sold returned_harem returned_released orren_lamp orren_given orren_run laulieh_rewarded sentence_overruled ilvara_executed native_trials_seen quarry_istrava quarry_suth quarry_guests lodge_given_rhez wager_won wager_lost".split())
REWIRES = {
    "captains_reply": ("method_chosen", "witness_heard"),
    "demonstration": ("meeting_planned", "evening_kept"),
    "return_count": ("crossing_ready", "next_measure"),
    "another_place": ("aftermath_heard", "crossing_finished"),
    "uninvited_guest": ("lodge_method_ready", "lodge_proposed"),
    "unborrowed_evening": ("lodge_answer_sent", "lodge_hunt_ended"),
    "no_applause": ("lodge_debt_answered", "lodge_judgment_finished"),
}


def f(*names):
    return tuple("noct." + x for x in names)


def placeholder(sid):
    return "{n}[N2 PROSE PENDING: " + sid + "]{/n}"


def page(s, key):
    return next(x for x in s["Nodes"] if x["Id"] == key)


def add(s, key, *choices):
    s["Nodes"].append(n(key, "Narrator", placeholder(s["Id"]), *choices, portrait="Nocticula"))


def answer(s, key, index=0):
    return page(s, key)["Choices"][index]


def append(s, key, text="Continue", next=None, flags=(), **kwargs):
    page(s, key)["Choices"].append(c(text, next, flags=f(*flags), **kwargs))


def bridge(s, key, *flags, next=None):
    a = answer(s, key)
    a["Set"].extend(x for x in f(*flags) if x not in a["Set"])
    if next is not None:
        a["Next"] = next


def check(skill, dc, success, failure):
    return dict(Skill=skill, DC=dc, Success=success, Failure=failure, CommanderOnly=True)


def retire(s):
    if "noct.retired" not in s["Requires"]:
        s["Requires"].append("noct.retired")
    s["Kind"] = "memory"  # retained manuscript, no live sending
    for node in s["Nodes"]:
        node["Text"] = RETIRED_TEXT


def scaffold(scenes):
    """Before partner wrappers: append only, preserving all old live text."""
    by = {s["Id"].removeprefix("noct."): s for s in scenes}
    for key in RETIRED:
        retire(by[key])
    for key, (old, new) in REWIRES.items():
        s = by[key]
        s["Requires"][s["Requires"].index("noct." + old)] = "noct." + new
    titles = dict(unlit_quay="The thief on the quay", sixth_passenger="The chair, again",
                  captains_reply="What the captain owns", demonstration="A trick for the court",
                  return_count="Everything that crosses", another_place="Her dressing room",
                  hearing="The trial", last_buyer="The tour", empty_chair="A mask from a vassal",
                  uninvited_guest="The hostess hunt", unborrowed_evening="After the hunt",
                  bell_without_master="The spoils", no_applause="How far a bird gets")
    for key, title in titles.items():
        by[key]["Title"] = title

    s = by["unlit_quay"]
    append(s, "start", "[Look at the stitching on the flower.]", check=check("SkillPerception", 28, "stitch", "offer"))
    append(s, "start", "[Demon] Let me open him up.", "demon", mythic="Demon")
    add(s, "stitch", c("Continue", "offer", flags=f("flower_real_seen")))
    add(s, "demon", c("Continue", "offer"))

    s = by["sixth_passenger"]
    append(s, "start", "[Watch him while she works.]", check=check("SkillPerception", 30, "read_lie", "missed_lie"))
    append(s, "theft", '"Take the hand he stole with."', "terms", ("asked_instrument", "orren_hand_taken"), alignment=("Evil", 1))
    for a in page(s, "terms")["Choices"]:
        a["Next"] = "sentence"
    add(s, "read_lie", c("Continue", "terms", flags=f("orren_lie_caught")))
    add(s, "missed_lie", c("Continue", "terms"))
    add(s, "sentence",
        c('"Keep him. Squeeze him until he is dry."', flags=f("method_chosen", "ledger_read")),
        c('"Send him home wearing your flower."', flags=f("method_chosen", "bait_sent")),
        c('"Let him sell the captain two lies."', flags=f("method_chosen", "double_offer"), requires=("trickster",)))

    s = by["captains_reply"]
    append(s, "start", '"What did Orren give up?"', "ledger", ("method_chosen", "ledger_read"), requires=f("witness_heard"), forbids=f("ledger_read", "bait_sent", "double_offer"))
    append(s, "dessa", '"Put him on the block instead."', "sold", ("dessa_safe", "captain_sold"), alignment=("Evil", 1))
    add(s, "sold", c("Continue", "waking"))
    for key in ("lease", "threat"):
        answer(s, key)["Next"] = "waking"
    waking(s, ("lann", "woljif", "greybor"))

    s = by["her_own_face"]
    add(s, "mark",
        c('"Leave it where it shows."', "morning", flags=f("crimson_mark", "mark_shown")),
        c('"Cover it."', "morning", flags=f("crimson_mark", "mark_hidden")))
    answer(s, "morning")["Next"] = "waking"
    waking(s, ("daeran", "wenduag", "seelah", "woljif"), "noct.mark_shown")

    s = by["demonstration"]
    demands = ("demand_release", "demand_instrument", "demand_seventh")
    for index, (key, flag) in enumerate(zip(("release", "instrument", "seventh"), demands)):
        append(s, "start", answer(s, "start", index)["Text"], key, ("meeting_planned", flag), forbids=f(*demands), requires=("trickster",) if index == 2 else ())
        answer(s, key)["Next"] = "court"
    add(s, "court", c("[Tell the court how her trick works.]", check=check("SkillKnowledgeArcana", 32, "exposed", "laughed")),
        c('"That flower is yours."', "exposed", requires=f("flower_real_seen")), c("[Say nothing.]", "price"))
    add(s, "exposed", c("Continue", "price", flags=f("ilvara_shamed")))
    add(s, "laughed", c("Continue", "price"))
    bridge(s, "witness", "ilvara_sent")
    bridge(s, "leverage", "volunteer_requested", "orren_carries")

    s = by["return_count"]
    answer(s, "start", 1)["Forbids"].extend(f("orren_carries"))
    append(s, "start", '"Send the thief in."', "orren", requires=f("orren_carries"))
    append(s, "start", "[Choose the carrier.]", "carrier", forbids=f("ilvara_sent", "volunteer_requested"))
    add(s, "orren", c("Continue", "strain"))
    add(s, "carrier", c('"Ilvara."', "ilvara", flags=f("ilvara_sent")), c('"The thief."', "orren", flags=f("volunteer_requested", "orren_carries")))
    doors = ("door_reinforced", "door_unreinforced", "door_limited")
    for i, (key, flag) in enumerate(zip(("reinforced", "unreinforced", "limited"), doors)):
        append(s, "strain", ("Burn your flower into the door.", "Hold it narrow.", "One crossing per coin.")[i], key, (flag,), forbids=f(*doors), requires=("trickster",) if i == 2 else ())
        bridge(s, key, "crossing_planned", "crossing_ready", "aftermath_heard", next="assign")
    add(s, "assign", c('"Sell them."', "orren_end", flags=f("returned_sold"), alignment=("Evil", 1), crusade=("Finances", 300)),
        c('"Your Harem."', "orren_end", flags=f("returned_harem")),
        c('"Let them go."', "orren_end", flags=f("returned_released"), alignment=("Good", 1)),
        c('"Let them go, under your protection."', "orren_end", flags=f("returned_released"), mythic="Angel"))
    add(s, "orren_end", c('"Give the door Orren."', flags=f("orren_lamp"), alignment=("Evil", 1)),
        c('"Give him to the people he sold."', flags=f("orren_given")),
        c('"Let him run."', flags=f("orren_run"), requires=f("orren_lie_caught")),
        c('"Let him run."', flags=f("orren_run"), requires=f("orren_hand_taken"), forbids=f("orren_lie_caught")))

    s = by["another_place"]
    for key in ("laulieh", "departure", "courier"):
        append(s, key, "[Let her be rewarded here.]", s["Id"] + ".explicit.1", ("laulieh_rewarded",), requires=("nocticula.partner_terms",))
    add(s, s["Id"] + ".explicit.1", c("Continue", s["Id"] + ".aftermath.1"))
    add(s, s["Id"] + ".aftermath.1", c("Continue", "others"))

    s = by["hearing"]
    answer(s, "start")["Check"]["Skill"] = "CheckIntimidate"
    append(s, "start", '"She broke once in this hall already."', "contradiction", requires=f("ilvara_shamed"))
    for key, flags, extra in (
        ("overruled", ("hearing_finished", "ilvara_exiled", "sentence_overruled"), dict(alignment=("Good", 1))),
        ("execute", ("hearing_finished", "ilvara_executed"), dict(alignment=("Evil", 1))),
        ("demon_ask", ("hearing_finished", "ilvara_executed"), dict(mythic="Demon")),
        ("aeon", ("hearing_finished", "ilvara_commissioned"), dict(mythic="Aeon")),
    ):
        append(s, "terms", {"overruled": '"Let her go."', "execute": '"Execute her."', "demon_ask": '"Give her to me."', "aeon": '"Bound to the door she made."'}[key], key, flags, **extra)
        add(s, key, c("Continue", "waking"))
    for key in ("confine", "commission", "exile"):
        answer(s, key)["Next"] = "waking"
    # A separate cue, never an epilogue paragraph on a live page.
    append(s, "aeon", "Continue", "aeon.native_trials", requires=f("native_trials_seen"))
    add(s, "aeon.native_trials", c("Continue", "waking"))
    waking(s, ("regill", "seelah", "lann"))

    s = by["last_buyer"]
    answer(s, "start")["Check"]["Skill"] = "CheckBluff"
    answer(s, "cost")["Crusade"] = dict(Resource="Favors", Amount=-100)

    s = by["empty_chair"]
    for key in ("vow_guard", "vow_ledger"):
        answer(s, key)["Next"] = "entrance"
    add(s, "entrance", c('"As guests."', flags=f("lodge_guest_entry", "lodge_method_ready")),
        c("[Silence the bell.]", check=check("SkillUseMagicDevice", 34, "entrance.silence", "entrance.fracture")),
        c('"Send her an invitation to herself."', flags=f("lodge_self_invitation", "lodge_method_ready"), requires=("trickster",)))
    add(s, "entrance.silence", c(flags=f("lodge_silent_bell", "lodge_method_ready")))
    add(s, "entrance.fracture", c(flags=f("lodge_bell_read_failed", "lodge_guest_entry", "lodge_method_ready")))

    s = by["uninvited_guest"]
    append(s, "start", "[Enter as guests.]", "guest", ("lodge_guest_entry", "lodge_method_ready"), forbids=f("lodge_silent_bell", "lodge_guest_entry", "lodge_self_invitation"))
    answer(s, "gallery")["Next"] = "bell"
    add(s, "bell", c('"Ring it for her."', "hunt.istrava", flags=f("quarry_istrava")),
        c('"Ring it for Suth."', "hunt.suth", flags=f("quarry_suth")),
        c('"Ring it for all of them."', "hunt.guests", flags=f("quarry_guests"), alignment=("Evil", 1)))
    add(s, "hunt.istrava", c("[Find her.]", check=check("SkillPerception", 32, "caught.clean", "caught.costly")))
    for key in ("caught.clean", "caught.costly", "hunt.suth", "hunt.guests"):
        add(s, key, c("Continue", "held"))
    bridge(s, "held", "lodge_offer_bounded", "lodge_answer_sent", next="waking")
    append(s, "held", '"Make her name every patron first."', "waking", ("lodge_hunt_ended", "lodge_offer_bait", "lodge_answer_sent"))
    waking(s, ("wenduag", "greybor", "daeran"))

    s = by["unborrowed_evening"]
    append(s, "close", "[Let her have what the hunt left her hungry for.]", s["Id"] + ".explicit.1")
    add(s, s["Id"] + ".explicit.1", c("Continue", s["Id"] + ".aftermath.1"))
    add(s, s["Id"] + ".aftermath.1", c("Continue", "want"))

    s = by["bell_without_master"]
    append(s, "start", "[Hear what the list gave her.]", "bounded", ("lodge_offer_bounded",), forbids=f("lodge_offer_bounded", "lodge_offer_bait"))
    append(s, "judgment", '"Give it to Rhez."', "rhez", ("lodge_kept_house", "lodge_given_rhez"))
    add(s, "rhez", c("Continue", "last"))
    bridge(s, "last", "lodge_debt_denied", "lodge_debt_answered")
    append(s, "last", '"Buy him. He collects for you now."', flags=("lodge_judgment_finished", "lodge_debt_purchased", "lodge_debt_answered"))

    s = by["no_applause"]
    append(s, "debt_report", "[Hear what became of Suth.]", "debt_refused", ("lodge_debt_denied",), forbids=f("lodge_debt_denied", "lodge_debt_purchased"))
    for key in ("wound", "agent", "agent_announcement"):
        answer(s, key)["Next"] = "wager"
    add(s, "wager",
        c('"They are dragged back before the gate."', "run.caught", flags=f("wager_won"), requires=f("lodge_debt_purchased")),
        c('"They are dragged back before the gate."', "run.free", flags=f("wager_lost"), requires=f("lodge_debt_denied")),
        c('"They make the docks."', "run.free", flags=f("wager_won"), requires=f("lodge_debt_denied")),
        c('"They make the docks."', "run.caught", flags=f("wager_lost"), requires=f("lodge_debt_purchased")))
    add(s, "run.caught", c("Continue", "credit"))
    add(s, "run.free", c("Continue", "credit"))
    for a in list(page(s, "credit")["Choices"]):
        twin = deepcopy(a)
        twin["Requires"].extend(f("wager_won"))
        twin["Crusade"] = dict(Resource="Finances", Amount=200)
        a["Forbids"].extend(f("wager_won"))
        page(s, "credit")["Choices"].append(twin)

    s = by["what_she_keeps"]
    append(s, "disposition", "[Look at the empty hook.]", "executed", requires=f("ilvara_executed"))
    add(s, "executed", c("Continue", "ambition"))


def waking(s, companions, trigger=None):
    choices = []
    higher = []
    for who in companions:
        choices.append(c("Continue", "waking." + who,
                         requires=(who + ".in_party",) + ((trigger,) if trigger else ()),
                         forbids=tuple(higher)))
        higher.append(who + ".in_party")
    # Sheet §1.5 explicitly retains an ungated Continue for every history.
    choices.append(c())
    add(s, "waking", *choices)
    for who in companions:
        add(s, "waking." + who, c())


def finish_partners(payload):
    """After legacy partner wrappers/slots: route-only splices at stable IDs."""
    by = {s["Id"]: s for s in payload["Scenes"]}
    s = by["noct.her_own_face"]
    answer(s, "noct.her_own_face.aftermath.1")["Next"] = "mark"
    s = by["noct.second_door"]
    answer(s, "end", 3)["Forbids"].append("noct.mark_shown")
    append(s, "end", "[Return to the waking world.]", "partner_discovery.end.0",
           requires=("nocticula.partner_stance.secret", "nocticula.partner.letters_burned", "noct.mark_shown"),
           forbids=("nocticula.partner_secret_exposed",))
    # Keep the old completion effects on every discovery/ordinary exit.
    for node in s["Nodes"]:
        for a in node["Choices"]:
            if not a["Next"] and not a.get("Check") and not a["Abort"] and "noct.complete" in a["Set"]:
                a["Next"] = "waking"
    waking(s, ("arueshalae", "daeran", "seelah"), "noct.mark_shown")
    for sid, s in by.items():
        if sid.removeprefix("noct.") in RETIRED:
            retire(s)
    for sid in ("noct.ending_company", "noct.ending_alliance", "noct.ending_limit"):
        page(by[sid], "end").setdefault("Paragraphs", []).append(
            p(placeholder(sid), requires=("noct.redeemed_epilogue",)))


def bypass_retained_copy(payload):
    """After NM1 folds: keep all copied nodes, bypass only the retired letter."""
    by = {s["Id"]: s for s in payload["Scenes"]}
    retire(by["noct.acq.the_retained_copy"])
    s = by["noct.acq.the_paid_address"]
    for node in s["Nodes"]:
        if node["Id"].startswith("the_retained_copy."):
            node["Text"] = RETIRED_TEXT
        for a in list(node["Choices"]):
            if a["Next"] == "the_retained_copy.arrives":
                # Rules.Validate follows structural edges even when their gate
                # is impossible. Preserve an appended archival edge for parked
                # saves and retain every copied node without offering it live.
                parked = deepcopy(a)
                parked["Requires"].append("noct.retired")
                node["Choices"].append(parked)
                a["Next"] = "an_answer_of_her_own.arrives"
                a["Set"].append("noct.acq.the_retained_copy_done")
