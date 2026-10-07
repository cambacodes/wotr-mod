"""S48: authored private non-aggression bargain, HAREM-SHEETS-48-52 rev. 2.

Herrax is a correspondent, Minagho the sole physical woman; Chivarro is discussed.
Native request: Cue_0045_KillChivarro, 49135105da5bc6c4f93e312e80286f91.
No native rewrite, return device, reconciliation or explicit interval is added.
Registration belongs after current presence/epoch contracts and before household
readers. The coordinator owns that shared discovery hook and K3 assembly.
"""
import copy

from story_format import c, n, p, scene
from storylines import household

P = "household.pair.herrax_minagho."
MC = "minagho_chivarro.trickster."
HUBS = ("minagho_chivarro.presence.minagho_spared", "minagho_chivarro.presence.minagho")
LETTERS = ("herrax.trickster.late.next_move", "herrax.trickster.owed.night", "herrax.letters.the_courier")
EDGES = {"herrax.harem.enmity.w.minagho": "herrax.harem.reconciled.w.minagho",
         "minagho_chivarro.harem.enmity.minagho.herrax": "minagho_chivarro.harem.reconciled.minagho.herrax"}
DEEDS = ("settled", "herrax_order_withdrawn", "minagho_hunters_recalled",
         "cost.herrax_contract_yielded", "cost.minagho_revenge_yielded")


def flags(*names):
    return tuple(P + name for name in names)


def success(step, paid=False):
    return flags(step + ".seen", *DEEDS, *(
        ("cost.commander_guarantor", "cost.escort_paid") if paid else ())) + (
            "household.friction.herrax.minagho.settled",)


def graph(step, unfinished=False, debt=False):
    """All venue/body variants share indices, terminal writes and step clocks."""
    later = c("[Later.]", abort=True)
    if step == "historical":
        return [n("start", "Minagho", '''{n}Outside the quartermaster's stores, Minagho holds the copy of Herrax's request by one corner. Ash from the Worldwound settles on the paper.{/n}
"So she asked you to kill Chivarro. And you let me learn it now."
{n}She folds the copy around her dagger's blade.{/n}
"Chivarro is no longer under your protection. Don't offer me an escort for her. Tell me whose mouth those words came out of."''',
                  c('"Herrax asked. I have brought you the request."',
                    flags=flags("notice.seen", "notice.historical", "target_unprotected")), later)]
    if step == "notice":
        earlier = ('{n}Beside the request lies the answer already carried to Herrax. Minagho pushes that answer aside with her knife.{/n}\n'
                   '"You dealt with her. You didn\'t tell me."\n') if unfinished else ""
        return [n("start", "Minagho", '''{n}Minagho reads the copy beside the quartermaster's stores while a wagon of wounded soldiers rattles past. She stops at Chivarro's name. Her dagger pins the paper to a crate.{/n}
"'My gratitude will know no bounds.' How generous. Does she charge extra to lick the blood off?"
''' + earlier + '''"Herrax gets an answer. My hunters can find her boys on the road out of the rift. Let's see how much she likes paying for knives when they're pointed at her."''',
                  c('"Send her your answer. I\'ll carry it."', "sent"),
                  c('"Leave the old contract alone."', "dismissed"), later),
                n("sent", "Minagho", '''{n}Minagho dictates a warning, naming Chivarro and the order against her. She seals it herself, then scratches a second message on a narrow scrap for her hunters.{/n}
"She withdraws her order, including whatever she whispered to hired hands. Then I recall mine. Her boys keep their throats. Chivarro keeps hers."
{n}She puts the sealed warning into your hand.{/n}
"Bring back her answer. A real one."''', c("[Carry the warning.]", flags=flags(
                    "notice.seen", "notice.sent", "cost.minagho_hunters_committed"))),
                n("dismissed", "Minagho", '''{n}Minagho tears the blank reply in half.{/n}
"Then keep out of it. When Herrax asks why her boys stopped coming home, she can pay someone else to listen."''',
                  c("Continue", flags=flags("notice.seen", "notice.dismissed")))]
    if step == "reply":
        return [n("start", "Narrator", '''{n}The returning courier brings Herrax's black wax seal, impressed with a gold coin. Her signed reply lies beside Minagho's warning.{/n}
"Keep her out of my house and your hunters off my boys. I can afford to let one bitch keep breathing. But I want the hunters recalled before my next messenger leaves."
{n}Minagho scrapes the seal off with her thumbnail.{/n}
"She keeps breathing because I am here. Don't flatter yourself."
{n}Minagho has her recall ready. Neither woman will send hers first; the courier waits beyond the stores, watching the crusade's sentries.{/n}''',
                  c('[Diplomacy] "Exchange the withdrawal and the recall through me."', check=dict(
                      Skill="CheckDiplomacy", DC=22, Success="exchanged", Failure="failed", CommanderOnly=True)),
                  c('"I will escort the exchange and answer for either of you breaking it."',
                    flags=success("reply", True), crusade=("Finances", -200)),
                  c('"Keep your knives. I\'m carrying no promises."', "refused"), later),
                n("exchanged", "Narrator", exchange_text(), c("Continue", flags=success("reply"))),
                n("failed", "Minagho", '''{n}The courier refuses to carry the withdrawal without a recall. Minagho snatches her message back before he can touch it.{/n}
"He wants a hostage. Give him your own hide."
{n}You must cover the courier's threatened journey; neither concession has changed hands.{/n}''',
                  c("[Take the courier's debt.]", flags=flags("reply.seen", "reply.failed", "cost.commander_courier_debt"))),
                n("refused", "Minagho", '''"Then stop wasting my hunters' time. Her boys are still on the road."
{n}She rolls the unsent recall tight and tucks it into her sleeve.{/n}''',
                  c("Continue", flags=flags("reply.seen", "reply.refused")))]
    if step == "retry":
        debt_line = ('"You already owe me for the last trip. This time I want the escort before I leave."\n'
                     if debt else '"Another trip costs more," {n}he says, looking towards the sentries.{/n}\n')
        return [n("start", "Narrator", '''{n}The courier has waited two days. His cloak is stiff with Worldwound ash. Herrax's sealed withdrawal remains in his hand; Minagho's hunters still have their orders.{/n}
''' + debt_line + '''
{n}Minagho lays her recall beside the withdrawal, keeping a claw on it.{/n}
"No pretty speeches this time. Your warning, your escort. Herrax can decide how much she wants to test you."''',
                  c('"Deliver my warning. I will pay for the escort."', flags=success("retry", True),
                    crusade=("Finances", -300)),
                  c('"No bargain."', "refused"), later),
                n("refused", "Minagho", '''{n}Minagho crushes her recall in her fist. The courier carries Herrax's sealed concession away.{/n}
"Good. Now she knows I know. Let's see which of her pets she sends next."
{n}The truce ends here. Neither woman has surrendered her order.{/n}''', c("Continue", flags=flags(
                    "retry.seen", "retry.refused", "unsettled") + ("household.friction.herrax.minagho.failed",)))]
    raise ValueError(step)


def exchange_text():
    return '''{n}Herrax's courier hands over the authenticated withdrawal. It names Chivarro and revokes every kill order and paid inducement Herrax controls, including those passed through intermediaries. Herrax has signed beneath the names.{/n}
"Chivarro doesn't get my chair. Or my house. If she wants a throne, she can climb onto your lap."
{n}Minagho sends her recall with the same courier. Her hunters' acknowledgments come back with the seal intact; neither Herrax nor her messengers remain their quarry over this contract.{/n}
"Tell her I can remember two things at once. A bargain, and who wanted Chivarro dead."'''


def paid_text():
    return '''{n}Your escort delivers the exchange under your warning. Herrax's authenticated withdrawal revokes every kill order and paid inducement she controls against Chivarro, including through intermediaries. Minagho's hunters answer her recall. Both messages return with their seals intact.{/n}
"Her chair is still mine," {n}Herrax has written beneath her signature.{/n}
{n}Minagho burns the hunters' acknowledgments over the stores' brazier.{/n}
"She can choke on it. Chivarro was never hers to sell."'''


def register(payload, scenes, refs):
    derived = payload.setdefault("Derived", {})
    pending = payload.setdefault("PendingHooks", [])
    for key in (*EDGES, *EDGES.values()):
        if key not in pending:
            pending.append(key)
    derived[P + "ready"] = [["herrax.asked_kill_chivarro", MC + outcome]
                            for outcome in ("reunited", "returned_chivarro")]
    derived[P + "minagho_eligible"] = [[MC + "committed", "minachiv.future_" + future]
                                      for future in ("minagho", "two")]
    derived[P + "herrax_channel"] = [[key, "herrax.reachable_by_letter"] for key in LETTERS]
    derived[P + "target_current"] = [["participant.chivarro.available", "chivarro.present_now"]]
    payload.setdefault("DerivedForbids", {})[P + "target_current"] = [
        "minachiv.closed", MC + "chivarro_sent_back", MC + "chivarro_declined"]
    for key, deeds in (
        ("herrax.harem.attitude.w.minagho.respect", ("settled", "minagho_hunters_recalled", "cost.minagho_revenge_yielded")),
        ("minagho_chivarro.harem.attitude.minagho.herrax.respect", ("settled", "herrax_order_withdrawn", "cost.herrax_contract_yielded")),
    ):
        derived[key] = [list(flags(*deeds))]
    common = ["trickster", P + "ready", "minagho.present_now", "participant.minagho.available",
              P + "herrax_channel"]
    forbidden = ["trickster.failed", "herrax.closed", "minachiv.closed", MC + "declined_minagho", "inhuman"]
    step_rules = {
        "notice": ([P + "target_current"], [P + "notice.seen"], [], 0),
        "historical": ([], [P + "notice.seen", P + "target_current"], [], 0),
        "reply": ([P + "notice.sent", P + "target_current"], [P + "reply.seen", P + "notice.dismissed"], [], 48),
        "retry": ([P + "target_current"], [P + "retry.seen", P + "settled", P + "notice.dismissed"],
                  [[P + "reply.failed", P + "reply.refused"]], 48),
    }
    added = []
    for hub_index, hub in enumerate(HUBS):
        presence = payload["Presences"][hub]
        for step, (required, vetoes, groups, delay) in step_rules.items():
            for variant_on in ((False, True) if step in ("notice", "retry") else (False,)):
                unfinished = step == "notice" and variant_on
                debt = step == "retry" and variant_on
                suffix = ("notice.historical" if step == "historical" else step)
                suffix += ".minagho" if hub_index else ""
                suffix += ".unfinished" if unfinished else ""
                suffix += ".debt" if debt else ""
                body_requires = ["trickster" if key == "trickster.ever" else key for key in presence.get("Requires", [])]
                variant = "herrax.trickster.cost.contract_unfinished" if step == "notice" else P + "cost.commander_courier_debt"
                extra_requires = [variant] if variant_on else []
                extra_forbids = [variant] if step in ("notice", "retry") and not variant_on else []
                overrides = {"minagho.dead": MC + "returned_minagho"} if hub_index else {}
                body = scene(P + suffix, "Whose knife?", "Minagho", 5,
                             '[The request against Chivarro.]', graph(step, unfinished, debt),
                             requires=tuple(dict.fromkeys([key for key in common if step != "historical" or key != P + "herrax_channel"] + required + body_requires + extra_requires)),
                             forbids=tuple(dict.fromkeys([key for key in forbidden if step != "historical" or key != "herrax.closed"] + vetoes + presence.get("Forbids", []) + extra_forbids + (["minagho.dead"] if hub_index else []))),
                             delay=delay, last=5, Relationship="household", Chapters=[5],
                             Areas=[presence["Area"]], ContactUnit=presence["Unit"], InteractionHub=hub,
                             Participants=["minagho_chivarro"] if step == "historical" else ["herrax", "minagho_chivarro"], ParticipantWomen=["minagho"],
                             RequiresAnyGroups=copy.deepcopy(presence.get("RequiresAnyGroups", [])) + groups,
                             ForbidOverrides=overrides, RestAllowance="household.protected")
                added.append(body)
    # K3 owns its eventual packet; these Table fallbacks share the singleton step witnesses.
    for step in ("reply", "retry"):
        required, vetoes, groups, delay = step_rules[step]
        for debt in ((False, True) if step == "retry" else (False,)):
            variant = P + "cost.commander_courier_debt"
            extra_requires = [variant] if debt else []
            extra_forbids = [variant] if step == "retry" and not debt else []
            added.append(household._table_scene(P + step + ".table" + (".debt" if debt else ""), "Whose knife?", "Minagho",
            '[Minagho and Herrax\'s reply.]', graph(step, debt=debt),
            requires=tuple(common + required + [household.KEPT, "herrax.harem.eligible", P + "minagho_eligible"] + extra_requires),
            forbids=tuple(forbidden + vetoes + [household.CLOSED, household.KING_GONE] + list(EDGES) + extra_forbids),
            delay=delay, chapters=(5,), Participants=["herrax", "minagho_chivarro"], ParticipantWomen=["minagho"],
            RequiresAnyGroups=groups, ForbidOverrides=dict(EDGES), RestAllowance="household.protected"))
    scenes.extend(added)
    ledger = payload["Books"]["trickster.ledger"]
    records = {
        "notice.dismissed": "Minagho learned whose knife was promised. I refused to carry her answer.",
        "notice.historical": "Minagho learned of the request after Chivarro was no longer in our protection. I offered no living target as a bargain.",
        "unsettled": "The contract had no truce. Herrax and Minagho dealt through me, if at all.",
        "settled": "Herrax withdrew the order. Minagho recalled her hunters. Chivarro's chair was never part of the bargain.",
        "cost.commander_courier_debt": "The failed exchange left me owing the courier protection on the road.",
        "cost.commander_guarantor": "I put my own retaliation behind their truce.",
        "cost.escort_paid": "The exchange's escort came out of the crusade's treasury. Herrax's authenticated withdrawal and the hunters' acknowledgments came back with their seals intact.",
        "cost.minagho_hunters_committed": "Minagho committed her hunters against Herrax's messengers over Chivarro's life.",
    }
    ledger["Entries"].append(dict(Id=P + "account", Section="Seating Notes", Portrait="Minagho", Title="Whose knife?",
        Text="{n}Herrax's request against Chivarro reached Minagho.{/n}", Requires=[P + "notice.seen"], Forbids=[], AnyGroups=[],
        Lines=[dict(Text="{n}" + text + "{/n}", Requires=[P + key], Forbids=[], AnyGroups=[]) for key, text in records.items()]))
    # Historical cost readers on existing destinations; no new Ch6 scenes.
    by_id = {body["Id"]: body for body in scenes}
    for host, text, cost in (
        ("herrax.lastcall.page", "Herrax withdrew every inducement she controlled against Chivarro's life. She kept the Delights' chair and lost the pleasure of promising Chivarro's head.", "cost.herrax_contract_yielded"),
        ("minachiv.lastcall.page", "Minagho recalled the hunters she had sent against Herrax and her messengers. She had obtained the withdrawal of the order against Chivarro; she had offered Herrax neither affection nor pardon.", "cost.minagho_revenge_yielded"),
    ):
        if host in by_id:
            by_id[host]["Nodes"][0].setdefault("Paragraphs", []).append(p(
                "{n}" + text + "{/n}", requires=("trickster",) + flags("settled", cost)))
