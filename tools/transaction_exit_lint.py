"""eng7-l09: declared failed-check charges must survive generated payment exits."""


CONTRACTS = [{"scene": "arsinoe.trickster.cauldron.lease", "failure": "raised",
              "liability": "arsinoe.trickster.cost.rent_raised",
              "settled": "arsinoe.trickster.cost.rent_surcharge_paid"}]


def check(story, contracts=None):
    contracts = CONTRACTS if contracts is None else contracts
    failures = []
    for scene in story.get("Scenes", []):
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        for node in scene["Nodes"]:
            for choice in node.get("Choices", []):
                roll = choice.get("Check")
                if not roll:
                    continue
                failed = nodes.get(roll["Failure"], {})
                charges = [c for c in failed.get("Choices", []) if (c.get("Crusade") or {}).get("Amount", 0) < 0]
                for contract in contracts:
                    if contract["scene"] != scene["Id"] or contract["failure"] != roll["Failure"]:
                        continue
                    liabilities = {contract["liability"]}
                    key = scene["Id"] + "/" + node["Id"]
                    if not any(contract["settled"] in c.get("Set", []) for c in charges):
                        failures.append(key + ": missing paid settlement producer")
                    if not liabilities.issubset(failed.get("EnterSet", [])):
                        failures.append(key + ": failure liability is recorded only upon payment")
                    if not liabilities.issubset(choice.get("Forbids", [])):
                        failures.append(key + ": failed check can be rerolled")
                    if any(c.get("Next") != roll["Failure"] and not liabilities.issubset(c.get("Forbids", []))
                           for c in node.get("Choices", [])):
                        failures.append(key + ": agreement can bypass unpaid failure")
                    for liability in liabilities:
                        if not any(liability in c.get("Requires", []) and c.get("Next") == roll["Failure"]
                                   for c in scene["Nodes"][0].get("Choices", [])):
                            failures.append(key + ": no unpaid-failure re-entry")
    return sorted(set(failures))


# --- eng8-q8c / E-Q8-09: receipt/exclusion/payment inventory ---
import json
from pathlib import Path

INVENTORY = Path(__file__).with_name("transaction_inventory2_contracts.json")
_failed_charge_check = check


def _selectable(choice, flags):
    return set(choice.get("Requires", [])).issubset(flags) and not flags.intersection(choice.get("Forbids", []))


def _reachable(nodes, first, flags):
    """Possible continuations after OnShow, including payment-abort boundaries.

    Resource availability is tested by RulesTests. Here a charge is potentially
    affordable; guarding every unpaid path is stricter than one funded trace.
    """
    seen, todo = set(), [(first, frozenset(flags))]
    while todo:
        node_id, held = todo.pop()
        if (node_id, held) in seen or node_id not in nodes:
            continue
        seen.add((node_id, held))
        node = nodes[node_id]
        current = set(held) | set(node.get("EnterSet", []))
        yield node_id, node, current
        for choice in node.get("Choices", []):
            if not _selectable(choice, current):
                continue
            next_flags = current | set(choice.get("Set", []))
            targets = ([choice["Next"]] if choice.get("Next") else [])
            if choice.get("Check"):
                targets += [choice["Check"]["Success"], choice["Check"]["Failure"]]
            todo.extend((target, frozenset(next_flags)) for target in targets)


def check_inventory(story, contracts=None):
    contracts = (json.loads(INVENTORY.read_text(encoding="utf-8"))["eng8-q8c"]["contracts"]
                 if contracts is None else contracts)
    scenes = {scene["Id"]: scene for scene in story.get("Scenes", [])}
    failures = []
    for contract in contracts:
        sid = contract["scene"]
        if sid not in scenes:
            failures.append(sid + ": missing transaction scene")
            continue
        scene = scenes[sid]
        nodes = {node["Id"]: node for node in scene["Nodes"]}
        root = scene["Nodes"][0]
        prefix = sid + ": "

        def require(ok, message):
            if not ok:
                failures.append(prefix + message)

        kind = contract["kind"]
        if kind == "exclusive-selection":
            host = nodes.get(contract["node"], {})
            choices = host.get("Choices", [])
            receipts = {s["receipt"] for s in contract["selections"]}
            for selection in contract["selections"]:
                flag, target, index = selection["receipt"], selection["target"], selection["index"]
                choice = choices[index] if index < len(choices) else {}
                require(choice.get("Next") == target and set(choice.get("Set", [])) & receipts == {flag},
                        flag + " missing indexed selection receipt")
                require(receipts.issubset(choice.get("Forbids", [])), flag + " missing selection exclusion")
                resumes = [c for c in choices[len(receipts):] if c.get("Next") == target
                           and flag in c.get("Requires", []) and not (set(c.get("Set", [])) & receipts)]
                require(any(set(c.get("Requires", [])) == {flag}
                            and set(c.get("Forbids", [])) == receipts - {flag} for c in resumes),
                        flag + " missing disjoint resume")
                for _, node, held in _reachable(nodes, root["Id"], {flag}):
                    for c in node.get("Choices", []):
                        if _selectable(c, held):
                            require(not ((set(c.get("Set", [])) & receipts) - {flag}), flag + " can acquire another pledge")
                require(any(nid == contract["node"] for nid, _, _ in _reachable(nodes, root["Id"], {flag})),
                        flag + " cannot reach resume selector")
        elif kind == "check-outcomes":
            initial = contract["initial"]
            initial_choices = nodes.get(initial["node"], {}).get("Choices", [])
            initial_index = initial["index"]
            payment = initial_choices[initial_index] if initial_index < len(initial_choices) else {}
            require(payment.get("Crusade") == initial["payment"] and contract["paid"] in payment.get("Set", [])
                    and contract["paid"] in payment.get("Forbids", []), "missing original initial payment/receipt/exclusion")
            choices = nodes.get(contract["node"], {}).get("Choices", [])
            index = contract["index"]
            roll = choices[index].get("Check", {}) if index < len(choices) else {}
            receipts = {o["receipt"] for o in contract["outcomes"]}
            for outcome in contract["outcomes"]:
                flag, target = outcome["receipt"], outcome["target"]
                require(roll.get(outcome["branch"]) == target, flag + " missing check branch")
                require(flag in nodes.get(target, {}).get("EnterSet", []), flag + " missing entry receipt")
                require(all(flag in c.get("Forbids", []) for c in choices), flag + " can reroll/bypass result")
                held = {contract["paid"], flag}
                resumes = [c for c in root.get("Choices", []) if _selectable(c, held)]
                require(bool(resumes) and all(c.get("Next") == target for c in resumes), flag + " missing outcome re-entry")
                for _, node, current in _reachable(nodes, root["Id"], held):
                    for c in node.get("Choices", []):
                        if _selectable(c, current):
                            require(not c.get("Check"), flag + " reaches a reroll")
                            require(not ((set(c.get("Set", [])) & receipts) - {flag}), flag + " acquires opposite receipt")
                    require(not ((set(node.get("EnterSet", [])) & receipts) - {flag}), flag + " reaches opposite outcome")
            grace = contract["outcomes"][0]["receipt"]
            for consumer in contract["consumers"]:
                require(consumer in scenes and any(grace in p.get("Requires", [])
                        for n in scenes.get(consumer, {}).get("Nodes", []) for p in n.get("Paragraphs", [])),
                        consumer + " missing concession consumer")
        elif kind == "irreversible-settlement":
            receipts = set(contract["entry_receipts"])
            act, settled = contract["act"], contract["settled"]
            paid_receipts = set(contract["paid_receipts"])
            require(receipts.issubset(nodes.get(act, {}).get("EnterSet", [])), "missing irreversible entry receipts")
            require(not paid_receipts.intersection(nodes.get(act, {}).get("EnterSet", [])), "unpaid act records paid outcome")
            choices = nodes.get(contract["payment_node"], {}).get("Choices", [])
            index = contract["payment_index"]
            payment = choices[index] if index < len(choices) else {}
            require(payment.get("Crusade") == contract["payment"] and paid_receipts.issubset(payment.get("Set", []))
                    and not payment.get("Next") and not payment.get("Check") and not payment.get("Abort"),
                    "missing original terminal payment/receipt")
            require(settled in scene.get("Forbids", []), "paid act can replay scene")
            held = receipts
            require(_selectable(payment, held), "original settlement is blocked after injury")
            resumes = [c for c in root.get("Choices", []) if _selectable(c, held)]
            require(bool(resumes) and all(c.get("Next") == contract["resume"] for c in resumes), "missing injury settlement re-entry")
            for nid, node, current in _reachable(nodes, root["Id"], held):
                require(nid != act, "injury replays irreversible act")
                for c in node.get("Choices", []):
                    if _selectable(c, current) and settled in c.get("Set", []):
                        require(c is payment, "unpaid bypass produces settled outcome")
            # Every continuation from the act must keep the original charge on
            # the terminal receipt. Alternate paid or free outcomes are defects.
            for _, node, current in _reachable(nodes, act, set()):
                for c in node.get("Choices", []):
                    if _selectable(c, current) and not c.get("Next") and not c.get("Check") and not c.get("Abort"):
                        require(c is payment, "irreversible continuation bypasses original settlement")
        else:
            raise ValueError("Unknown transaction contract: " + kind)
    return sorted(set(failures))


def check(story, contracts=None):
    # Legacy focused callers supply failed-check contracts explicitly.
    result = _failed_charge_check(story, contracts)
    return sorted(set(result + (check_inventory(story) if contracts is None else [])))
# end eng8-q8c
