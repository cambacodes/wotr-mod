"""eng7-l09: traverse declared intimate outcomes, mornings and later readers."""
import json
from pathlib import Path
from tools.draft_contract_lint import targets

CONTRACTS = Path(__file__).with_name("intimacy_contracts.json")


def walks(scene, flags=(), start=None):
    nodes = {n["Id"]: n for n in scene["Nodes"]}
    def visit(node, held, path):
        if node not in nodes or node in path:
            return
        path = path + (node,)
        for choice in nodes[node].get("Choices", []):
            if not set(choice.get("Requires", [])).issubset(held) or set(choice.get("Forbids", [])) & held:
                continue
            after = held | set(choice.get("Set", []))
            outgoing = targets(choice)
            if outgoing:
                for target in outgoing:
                    yield from visit(target, after, path)
            elif not choice.get("Abort"):
                yield path, after
    yield from visit(start or scene["Nodes"][0]["Id"], set(flags), ())


def check(story, contracts=None):
    contracts = json.loads(CONTRACTS.read_text(encoding="utf-8")) if contracts is None else contracts
    scenes = {s["Id"]: s for s in story["Scenes"]}
    failures, executed = [], []
    for contract in contracts:
        key = contract["scene"] + "/" + contract["outcome"]
        host = scenes.get(contract["scene"])
        callback = scenes.get(contract["callback_scene"])
        if not host or not callback:
            failures.append(key + ": missing host/callback")
            continue
        paths = [(p, f) for p, f in walks(host, contract["flags"]) if contract["cut"] in p and contract["flag"] in f]
        if not paths or any(contract["morning"] not in p for p, _ in paths):
            failures.append(key + ": cut has no morning continuation")
            continue
        for path, flags in paths:
            later = [(p, f) for p, f in walks(callback, flags) if contract["callback_node"] in p]
            node = next((n for n in host["Nodes"] if n["Id"] == contract["morning"]), {})
            reader = next((n for n in callback["Nodes"] if n["Id"] == contract["callback_node"]), {})
            guarded = any(contract["flag"] in c.get("Requires", []) and c.get("Next") == contract["callback_node"]
                          for n in callback["Nodes"] for c in n["Choices"])
            if not later or not guarded or not node.get("Text") or not reader.get("Text"):
                failures.append(key + ": missing reachable outcome-specific callback")
                break
        else:
            executed.append(dict(contract=key, path=list(paths[0][0]), morning=node["Text"], callback=reader["Text"]))
    return dict(hard=sorted(set(failures)), executed=executed)
