"""Authored edge-job-4 graph from jerribeth-rebuild.md §§5,9,11.

Existing prose and save identities are retained for the following writing job.
All added pages are deliberately placeholders. No native state is written.
"""
import copy

from story_format import c, n

RETIRED = (
    "small_print", "purchaser_answer", "counterfeit_hinge",
    "counterfeit_clerk", "counterfeit_after", "settlement_visit", "ordinary",
)
VISITS = ("commission", "offered_signature", "counterfeit_guest",
          "counterfeit_audience", "room_measure")
DREZEN = "2570015799edf594daf2f076f2f975d8"
# Cue_0019 carries de70b6ee and explains the mark. Cue_0023 applies it;
# mark_seen alone must not be used as proof that the Commander received it.
MARK_CUE = "e47232b2878eff849ac002d2f323cbad"
ARUESHALAE_PARTY = "c3ddb9898f4aaa34486d4d0b12e14ab8"


def flag(name):
    return "jerribeth." + name


def node(event, name):
    return next(page for page in event["Nodes"] if page["Id"] == name)


def pending(event, name, *choices):
    page = n(name, "Jerribeth", "[PROSE PENDING: %s]" % event["Id"],
             *choices, portrait="Jerribeth")
    event["Nodes"].append(page)
    return page


def answer(event, name, index=0):
    return node(event, name)["Choices"][index]


def add_flags(choice, *names):
    choice["Set"].extend(flag(name) for name in names
                         if flag(name) not in choice["Set"])


def check(skill, dc, success, failure):
    return dict(Skill=skill, DC=dc, Success=success, Failure=failure,
                CommanderOnly=True)


def option(event, target=None, **kw):
    return c("[PROSE PENDING: %s]" % event["Id"], target, **kw)


def companions(event, host, resume, names):
    # Optional, history-gated reaction pages; no conditional campaign paragraphs.
    saved = copy.deepcopy(node(event, resume)["Choices"])
    for name in names:
        nid = "companion_" + name
        node(event, host)["Choices"].append(option(
            event, nid, requires=(name + ".in_party",)))
        pending(event, nid, *copy.deepcopy(saved))


def integrate(payload):
    events = {s["Id"].removeprefix("jerribeth."): s
              for s in payload["Scenes"] if s["Id"].startswith("jerribeth.")}
    # Verified read-only observations from /wrath/blueprints.zip and enGB.json.
    payload.setdefault("SeenCues", {})[flag("mark_seen")] = [MARK_CUE]
    payload.setdefault("Etudes", {})["arueshalae.in_party"] = ARUESHALAE_PARTY

    for name in RETIRED:
        event = events[name]
        event["Forbids"].append("chapter_later")
        # Authored kind wins over the shared historical override; do not edit it.
        event["Kind"] = "sending"
    for name in VISITS:
        events[name].update(Kind="visit", Remote=True, Areas=[DREZEN])

    for name, old, new in (
        ("unsold_evening", "sale_terms_set", "counteroffer_sent"),
        ("counterfeit_guest", "consequences_kept", "unsold_evening_kept"),
        ("counterfeit_audience", "counter_clerk_dealt", "counter_invited"),
        ("room_measure", "settlement_visited", "counter_spoils_settled"),
        ("farewell", "ordinary", "future"),
        ("farewell_review", "ordinary", "future"),
    ):
        event = events[name]
        assert flag(old) in event["Requires"], (name, old)
        event["Requires"] = [flag(new) if key == flag(old) else key
                             for key in event["Requires"]]

    # Absorbed receipts: sweep original and split live terminals alike.
    bridges = {
        "offered_signature": ("counteroffer_sent", "sale_terms_set", "consequences_kept"),
        "unsold_evening": ("consequences_kept",),
        "counterfeit_guest": ("consequences_kept", "counter_mechanism_known", "counter_clerk_dealt"),
        "room_measure": ("settlement_visited", "counteroffer_kept"),
        "farewell": ("ordinary",),
    }
    receipts = {"offered_signature": "counteroffer_sent",
                "unsold_evening": "unsold_evening_kept",
                "counterfeit_guest": "counter_invited",
                "room_measure": "settlement_kept", "farewell": "farewell_kept"}
    for name, names in bridges.items():
        for page in events[name]["Nodes"]:
            for choice in page["Choices"]:
                if flag(receipts[name]) in choice["Set"]:
                    add_flags(choice, *names)

    event = events["commission"]
    for index, skill, dc, ok, fail in (
        (0, "CheckDiplomacy", 24, "yard_talk_ok", "yard_talk_fail"),
        (1, "SkillPerception", 20, "yard_seam", "yard_talk_fail"),
    ):
        choice = answer(event, "beauty", index)
        choice["Next"] = None
        choice["Check"] = check(skill, dc, ok, fail)
    node(event, "beauty")["Choices"].append(option(event, check=check(
        "CheckDiplomacy", 22, "yard_demon", "yard_talk_fail"),
        flags=(flag("yard_played"),), crusade=("Favors", -100)))
    node(event, "ask")["Choices"].extend((
        option(event, "cell_given", flags=(flag("yard_prisoner_given"),), alignment=("Evil", 1)),
        option(event, "cell_refused", flags=(flag("yard_confessed"),)),
    ))
    for name in ("yard_talk_ok", "yard_talk_fail", "yard_seam", "yard_demon", "cell_given", "cell_refused"):
        pending(event, name, c(next="keep", flags=(flag("yard_broken"),)
                if name in ("yard_talk_ok", "yard_seam") else ()))
    companions(event, "beauty", "beauty", ("seelah", "regill", "wenduag"))

    event = events["refuge"]
    for host in ("need", "anger"):
        node(event, host)["Choices"].extend((
            option(event, "footstool_kept", flags=(flag("refuge_footstool_kept"),)),
            option(event, "footstool_freed", flags=(flag("refuge_footstool_freed"),)),
        ))
    pending(event, "footstool_kept", c(next="stay"))
    pending(event, "footstool_freed", c(next="stay"))

    event = events["offered_signature"]
    for index, name in ((0, "widow_pinned"), (1, "widow_husband")):
        add_flags(answer(event, "ownership.reply.1", index), name)
    answer(event, "ownership.reply.1", 0)["Alignment"] = dict(Direction="Evil", Value=1)
    node(event, "ownership.reply.1")["Choices"].append(option(event, "break"))
    pending(event, "break", option(event, check=check(
        "SkillKnowledgeArcana", 32, "break_ok", "break_fail")))
    for name in ("break_ok", "break_fail"):
        effects = [flag(x) for x in (*bridges["offered_signature"], "offer_design", "sale_withdrawn")]
        if name == "break_ok":
            effects.append(flag("widow_exposed"))
        pending(event, name, option(event, flags=effects,
                **({"crusade": ("Favors", -100)} if name == "break_fail" else {})))
    # Existing performance/design answers already carry their distinct receipt.
    # All non-break live terminals record the corrected sale.
    for page in event["Nodes"]:
        if page["Id"] not in ("break_ok", "break_fail"):
            for choice in page["Choices"]:
                if flag("counteroffer_sent") in choice["Set"]:
                    add_flags(choice, "sale_corrected")
    node(event, "performance.reply.1")["Choices"].append(option(
        event, "widow_fee", flags=(flag("widow_fee_shared"),), crusade=("Finances", 100)))
    pending(event, "widow_fee", c(next="send.reply.1"))
    companions(event, "offer", "ownership.reply.1", ("regill", "seelah"))

    event = events["counterfeit_guest"]
    for skill in ("SkillPerception", "SkillKnowledgeWorld"):
        node(event, "square")["Choices"].append(option(event, check=check(
            skill, 30, "scout_known", "scout_unknown")))
    for name in ("scout_known", "scout_unknown"):
        pending(event, name, option(event, "attend", flags=(flag("vardess_known"),)
                if name == "scout_known" else ()))
    pending(event, "attend", option(event, "keep.reply.1"),
            option(event, "keep.reply.1", flags=(flag("vardess_reported"),)))

    event = events["counterfeit_audience"]
    node(event, "challenge")["Choices"].append(option(event,
        forbids=tuple(flag("counter_clerk_" + x) for x in ("witness", "rehearsal", "hidden")),
        check=check("SkillAthletics", 30, "chase_ok", "chase_fail")))
    for name in ("chase_ok", "chase_fail"):
        pending(event, name, c(next="leverage.reply.1"))
    answer(event, "leverage.reply.1", 0)["Crusade"] = dict(Resource="Favors", Amount=100)
    answer(event, "leverage.reply.1", 1)["Forbids"].append(flag("vardess_reported"))
    node(event, "leverage.reply.1")["Choices"].append(option(event,
        requires=(flag("vardess_reported"),), check=check(
            "CheckDiplomacy", 32, "raid_dismissed", "raid_kept")))
    pending(event, "raid_dismissed", c(next="archive", flags=(flag("counter_private_archive"),)))
    pending(event, "raid_kept", c(next="expose", flags=(flag("counter_public_account"),), crusade=("Favors", 100)))
    companions(event, "entrance", "challenge", ("regill", "lann", "wenduag"))

    event = events["counterfeit_spoil"]
    agreements = (flag("counter_return_agreement"), flag("counter_hold_agreement"))
    node(event, "start")["Choices"].extend((
        option(event, "drawer_pinned", requires=(flag("counter_private_archive"),), forbids=agreements),
        option(event, "drawer_empty", requires=(flag("counter_public_account"),), forbids=agreements),
    ))
    pending(event, "drawer_pinned", c(next="price.reply.1"))
    pending(event, "drawer_empty", option(event, "price.reply.1", flags=(flag("specimen_owed"),)),
            option(event, "price.reply.1", flags=(flag("specimen_owed"),)))
    for name in ("vardess_speaks", "vardess_blinded"):
        node(event, "price.reply.1")["Choices"].append(option(
            event, name, requires=(flag("counter_private_archive"),), flags=(flag(name),)))
        pending(event, name, c(next="end.reply.2"))

    event = events["room_measure"]
    for host, names in (
        ("public_result", ("inspection_visible", "inspection_removed", "inspection_refused")),
        ("private_result", ("catalogue_play", "catalogue_comedy", "catalogue_declined")),
    ):
        node(event, host)["Choices"].append(option(event, "shelves", forbids=tuple(map(flag, names))))
    pending(event, "shelves", c(next="floor"))
    add_flags(answer(event, "floor", 0), "cabinet_hidden")
    add_flags(answer(event, "floor", 1), "cabinet_moved")
    node(event, "floor")["Choices"].extend((
        option(event, check=check("CheckDiplomacy", 30, "cabinet_freed", "cabinet_refused")),
        option(event, "cabinet_token", flags=(flag("cabinet_token"),)),
    ))
    for name in ("cabinet_freed", "cabinet_refused", "cabinet_token"):
        pending(event, name, c(next="private", flags=(flag("cabinet_freed"),)
                if name == "cabinet_freed" else ()))
    companions(event, "floor", "floor", ("seelah", "regill", "wenduag", "ulbrig", "greybor", "arueshalae"))

    event = events["farewell"]
    for host in ("start", "want"):
        node(event, host)["Choices"].append(option(event, "traitor"))
    pending(event, "traitor",
            option(event, "traitor_hanged", flags=(flag("chancery_hanged"),), crusade=("Favors", 100)),
            option(event, "traitor_given", flags=(flag("chancery_given"),), alignment=("Evil", 1)),
            option(event, check=check("SkillKnowledgeWorld", 30, "traitor_fed", "traitor_failed")))
    for name in ("traitor_hanged", "traitor_given", "traitor_fed", "traitor_failed"):
        pending(event, name, c(next="return", flags=(flag("chancery_fed"),)
                if name == "traitor_fed" else ()))
    # Same four native fate precedence rules as the partner layer. No fifth fate.
    from storylines.jerribeth_partner import fate_guards
    for fate, guards in fate_guards().items():
        name = "discovery_" + fate
        for host in ("start", "want"):
            node(event, host)["Choices"].append(option(event, name,
                requires=(flag("partner_stance.secret"), *guards.get("requires", ())),
                forbids=(flag("partner.careful"), flag("partner_secret_exposed"), *guards.get("forbids", ()))))
        extra = ("partner_exposure." + fate,) if fate in ("plant", "chief") else ()
        effects = tuple(flag(x) for x in ("partner_secret_exposed", *extra))
        pending(event, name, option(event, "return", flags=effects),
                option(event, flags=(*effects, flag("closed"), flag("trickster.parted"))))

    # Prose for every page and answer added above (edge job 10).
    from storylines import jerribeth_voice
    jerribeth_voice.fill(payload)
