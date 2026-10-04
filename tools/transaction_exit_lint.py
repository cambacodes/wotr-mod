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
