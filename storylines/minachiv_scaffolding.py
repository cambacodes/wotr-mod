"""Authored job-4 structure from minachiv-rebuild §9; prose belongs to job 9.

Applied after the existing route overlays so retired nodes cannot be reanimated
by their old voice/slot patches. No native events or outcome gates are changed.
"""
from copy import deepcopy
from story_format import c, n

PREFIX = "minachiv."
RETIRED_TEXT = "{n}This meeting has passed.{/n}"
RETIRED = (
    "the_second_address", "a_factor_at_the_table", "the_answer_after_business",
    "the_key_in_your_hand", "the_paper_she_kept", "the_man_who_remembers",
    "the_entrance_she_wants", "who_keeps_the_house", "the_cost_in_daylight",
)
REWIRED = {
    "what_the_offer_bought": ("terms_sent", "offer_heard"),
    "minaghos_unfinished_sentence": ("business_finished", "evening_kept"),
    "a_room_she_likes": ("rehearsal_kept", "venture_begun"),
    "the_first_small_audience": ("musician_settled", "name_read"),
    "when_the_door_opens": ("ending_rehearsed", "preview_kept"),
    "what_she_will_take": ("venture_settled", "after_lamps_kept"),
}


def flags(*names):
    return tuple(PREFIX + name for name in names)


def integrate(payload):
    pages = {s["Id"][len(PREFIX):]: s for s in payload["Scenes"]
             if s["Id"].startswith(PREFIX)}
    # §11 conservative fallback: the available parent manifest proves outcome
    # etudes, not Book 1–3 action edges. Do not guess that a path broke the brand.
    payload.setdefault("Derived", {})[PREFIX + "brand_live"] = [["minagho.ran_complete"]]
    for sid in RETIRED:
        page = pages[sid]
        if "chapter_later" not in page["Forbids"]:
            page["Forbids"].append("chapter_later")
        page["Kind"] = "event"
        for node in page["Nodes"]:
            node["Text"] = RETIRED_TEXT
            node.pop("Paragraphs", None)
    for sid, (old, new) in REWIRED.items():
        pages[sid]["Requires"] = [PREFIX + new if f == PREFIX + old else f
                                   for f in pages[sid]["Requires"]]
    for sid in ("minaghos_unfinished_sentence", "when_the_door_opens"):
        pages[sid]["Kind"] = "visit"

    def nodes(sid):
        return {node["Id"]: node for node in pages[sid]["Nodes"]}

    def pending(sid):
        return "[PROSE PENDING: " + PREFIX + sid + "]"

    def answer(sid, next=None, **kwargs):
        return c(pending(sid), next, **kwargs)

    def add_node(sid, nid, *choices):
        for choice in choices:
            choice["Text"] = pending(sid)
        pages[sid]["Nodes"].append(n(nid, "Narrator", pending(sid), *choices))

    def bridge(sid, *names):
        for node in pages[sid]["Nodes"]:
            for choice in node["Choices"]:
                if not choice.get("Next") and not choice.get("Check") and not choice["Abort"]:
                    choice["Set"].extend(f for f in flags(*names) if f not in choice["Set"])

    sid = "the_remaining_customers"
    ns = nodes(sid)
    ns["document"]["Choices"][0]["Set"].extend(flags("terms_sent", "evidence_kept", "business_chosen"))
    for plan in ("bait_chosen", "refusal_chosen"):
        ns["document"]["Choices"].append(answer(sid, flags=flags("offer_heard", "terms_sent", "evidence_kept", plan)))
    ns["plans"]["Choices"].append(answer(sid, check=dict(
        Skill="CheckDiplomacy", DC=30, Success="source_named", Failure="source_hidden", CommanderOnly=True)))
    add_node(sid, "source_named", answer(sid, "document", flags=flags("source_found")))
    add_node(sid, "source_hidden", answer(sid, "document"))

    sid = "what_the_offer_bought"
    ns = nodes(sid)
    ns["start"]["Choices"].append(answer(sid, "late_plan", requires=flags("offer_heard"),
        forbids=flags("business_chosen", "bait_chosen", "refusal_chosen")))
    add_node(sid, "late_plan", *(answer(sid, dest, flags=flags(plan)) for plan, dest in
        (("business_chosen", "business"), ("bait_chosen", "bait"), ("refusal_chosen", "independent"))))
    ns["bait"]["Choices"].extend((answer(sid, "agent_killed"), answer(sid, "agent_handed_over")))
    add_node(sid, "agent_killed", answer(sid, flags=flags("offer_resolved", "agent_killed"), alignment=("Evil", 1)))
    add_node(sid, "agent_handed_over", answer(sid, flags=flags("offer_resolved", "agent_handed_over", "minagho_robbed"), crusade=("Favors", 100)))
    bridge(sid, "terms_sent", "evidence_kept", "names_sold")

    sid = "minaghos_unfinished_sentence"
    ns = nodes(sid)
    # earned_outcomes appends this legacy exit later in the original export.
    # Reserve its saved index before appending the street calls. The shared
    # appender may emit another exit afterward; its additional index is new.
    ns["morning"]["Choices"].append(c("[Leave.]", forbids=("minagho_chivarro.outcome.eligible",), abort=True))
    ns["morning"]["Choices"].extend((answer(sid, check=dict(Skill="CheckDiplomacy", DC=31,
        Success="protect_success", Failure="protect_failure", CommanderOnly=True), crusade=("Favors", -100)),
        answer(sid, "maim"), answer(sid, "abandon")))
    for nid, flag, effect in (("protect_success", "street_protected", {}),
                              ("protect_failure", "street_protected", {}),
                              ("maim", "survivor_maimed", {"alignment": ("Evil", 1)}),
                              ("abandon", "street_abandoned", {})):
        # Keep the old hand/roof answers and their intimacy conditions intact.
        add_node(sid, nid, answer(sid, "street_after", flags=flags(flag), **effect))
    add_node(sid, "street_after", *(deepcopy(a) for a in ns["morning"]["Choices"][:2]))
    for choice in ns["morning"]["Choices"][:2]:
        choice["Forbids"].append("chapter_later")
    bridge(sid, "business_finished")
    ns["hand"]["Choices"].append(answer(sid, PREFIX + sid + ".explicit.1",
        requires=(PREFIX + "minagho_chosen", "minagho_chivarro.outcome.eligible"),
        forbids=("minagho.ran_demon",)))
    add_node(sid, PREFIX + sid + ".explicit.1", answer(sid, "hand_after"))
    add_node(sid, "hand_after", deepcopy(ns["hand"]["Choices"][0]))

    sid = "the_performer_and_the_key"
    ns = nodes(sid)
    for choice in ns["fee"]["Choices"]:
        choice["Forbids"].append("chapter_later")
    for flag, effect in (("officer_names_bought", {"crusade": ("Finances", -100)}),
                         ("soldiers_barred", {}), ("house_tolerated", {})):
        ns["fee"]["Choices"].append(answer(sid, flag, **effect))
        add_node(sid, flag, answer(sid, flags=flags("venture_begun", flag)))
    bridge(sid, "rehearsal_kept")

    sid = "the_price_of_her_name"
    ns = nodes(sid)
    for nid in ("proof", "price", "question"):
        original = ns[nid]["Choices"][0]
        onward = answer(sid, "alley", flags=tuple(original["Set"]))
        original["Set"].extend(flags("forger_spared", "name_kept"))
        ns[nid]["Choices"].append(onward)
    add_node(sid, "alley",
        answer(sid, "book", flags=flags("forger_killed"), alignment=("Evil", 1)),
        answer(sid, "book", flags=flags("forger_maimed")),
        answer(sid, "book", flags=flags("forger_hanged"), crusade=("Favors", 50)))
    add_node(sid, "book", answer(sid, flags=flags("name_read", "name_kept")))

    sid = "the_first_small_audience"
    ns = nodes(sid)
    ns["counter"]["Choices"][0]["Set"].extend(flags("clerk_sold"))
    ns["counter"]["Choices"][0]["Alignment"] = dict(Direction="Evil", Value=1)
    ns["end"]["Choices"][0]["Set"].extend(flags("nerath_arrested"))
    ns["end"]["Choices"][0]["Crusade"] = dict(Resource="Favors", Amount=100)
    ns["proposal"]["Choices"].append(answer(sid, "outbid", crusade=("Finances", -200)))
    add_node(sid, "outbid", answer(sid, flags=flags("preview_kept", "open_booking", "clerk_bought")))
    bridge(sid, "name_kept", "musician_settled")

    sid = "when_the_door_opens"
    ns = nodes(sid)
    # Keep the saved pricing bypass indices; Chapter-5 play uses appended calls.
    legacy_callbacks = deepcopy(ns["first_scene"]["Choices"])
    for choice in ns["first_scene"]["Choices"]:
        choice["Forbids"].append("chapter_later")
    for flag, effect in (("door_paid", {"crusade": ("Finances", -100)}),
                         ("door_polished", {}), ("door_barred", {})):
        ns["first_scene"]["Choices"].append(answer(sid, "door_callback", flags=flags(flag), **effect))
    ns["first_scene"]["Choices"].append(answer(sid, check=dict(Skill="CheckDiplomacy", DC=32,
        Success="haggle_success", Failure="haggle_failure", CommanderOnly=True)))
    for nid, price in (("haggle_success", -50), ("haggle_failure", -200)):
        # The engine supplies its existing payment exit if this price is
        # unaffordable; no additional bargain or alternative price is invented.
        add_node(sid, nid,
            answer(sid, "door_callback", flags=flags("door_haggled"), crusade=("Finances", price)))
    for mythic in ("Legend", "Lich"):
        ns["first_scene"]["Choices"].append(answer(sid, "unread", mythic=mythic))
    ns["first_scene"]["Choices"].append(answer(sid, check=dict(Skill="CheckDiplomacy", DC=34,
        Success="unread", Failure="read", CommanderOnly=True)))
    add_node(sid, "unread", answer(sid, "door_callback", flags=flags("door_unread")))
    add_node(sid, "read", answer(sid, "door_callback"))
    add_node(sid, "door_callback", *legacy_callbacks)
    ns["ending"]["Choices"].append(answer(sid, "after", forbids=flags("winter_ending", "host_ending")))
    after = ns["after"]["Choices"][0]
    after["Set"].extend(flags("entrance_chosen", "ending_rehearsed", "after_show_promised"))
    after["Forbids"].extend(flags("door_barred"))
    twin = deepcopy(after)
    twin["Text"] = pending(sid)
    twin["Set"] = [PREFIX + "after_show_open" if f == PREFIX + "after_show_promised" else f for f in twin["Set"]]
    twin["Forbids"].remove(PREFIX + "door_barred")
    twin["Requires"].extend(flags("door_barred"))
    ns["after"]["Choices"].append(twin)

    sid = "after_the_last_lamp"
    nodes(sid)["start"]["Choices"].append(answer(sid, "rest", forbids=flags("after_show_promised", "after_show_open")))
    bridge("what_she_will_take", "venture_settled")
