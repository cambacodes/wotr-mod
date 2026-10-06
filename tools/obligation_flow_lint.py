"""E-Q7-23: trace declared promises and unbound negative reads.

This report requests route review; it never invents quests, rewards, or producers.
It visits serialized gates in scenes, Books, paragraphs, journals, and registries.
Drafts are supplied explicitly by the caller and kept separate from shipped data.
"""
import argparse
import json
from pathlib import Path

DEFAULT = Path(__file__).with_name("obligation_flow_contracts.json")
GATES = {"Requires", "Forbids", "RequiresAny", "RequiresAnyGroups", "When", "SettledWhen",
         "Derived", "DerivedForbids", "Latches", "ForbidOverrides",
         "UnavailableOverrides", "DerivedOpenRoutes", "Counts"}
PRODUCER_TABLES = {"Etudes", "SeenCues", "SelectedAnswers", "StartedDialogs",
                   "CompletedQuests", "CompletedEtudes", "StartedQuests", "MainCharacterFacts",
                   "QuestObjectives", "InventoryItems", "PartyItems", "UnlockableFlags",
                   "Derived", "Latches", "Counts", "DerivedAvailableContacts"}


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)


def retired(value):
    return bool(set(value.get("Requires", [])) & (set(value.get("Forbids", []))
                - set(value.get("ForbidOverrides", {}))))


def index(story):
    producers, consumers, negatives, revisits = {}, {}, {}, set()
    def add(table, flag, path):
        table.setdefault(flag, []).append(path)
    for table in PRODUCER_TABLES:
        for flag in story.get(table, {}):
            add(producers, flag, table + "/" + flag)
    def walk(value, path):
        if isinstance(value, list):
            for i, item in enumerate(value):
                walk(item, path + "/" + str(i))
        elif isinstance(value, dict):
            if retired(value):
                return  # retained branch retired by a contradictory gate
            for key, item in value.items():
                here = path + "/" + key
                if key in GATES:
                    for raw in strings(item):
                        flag = raw.lstrip("!")
                        add(consumers, flag, here)
                        if key in {"Forbids", "DerivedForbids"} or raw.startswith("!"):
                            add(negatives, flag, here)
                if key == "Set":
                    for flag in item:
                        add(producers, flag, here)
                        if value.get("Abort"):
                            revisits.add(flag)
                if key == "Nodes" and "Id" in value:
                    nodes = {n["Id"]: n for n in item}
                    reached = set()
                    def visit(node_id):
                        if node_id in reached or node_id not in nodes:
                            return
                        reached.add(node_id)
                        for choice in nodes[node_id].get("Choices", []):
                            if retired(choice):
                                continue
                            if choice.get("Next"):
                                visit(choice["Next"])
                            if choice.get("Check"):
                                for outcome in ("Success", "Failure"):
                                    visit(choice["Check"][outcome])
                    if item:
                        visit(item[0]["Id"])
                    for i, node in enumerate(item):
                        if node["Id"] in reached:
                            walk(node, here + "/" + str(i))
                else:
                    walk(item, here)
    walk(story, "story")
    # Scene completion is a real producer only if a reachable terminal completes.
    for scene in story.get("Scenes", []):
        if retired(scene):
            continue
        nodes = {n["Id"]: n for n in scene.get("Nodes", [])}
        def reachable(node_id, seen):
            if node_id in seen or node_id not in nodes:
                return False
            for choice in nodes[node_id].get("Choices", []):
                if retired(choice):
                    continue
                targets = [choice["Next"]] if choice.get("Next") else []
                if choice.get("Check"):
                    targets += [choice["Check"][k] for k in ("Success", "Failure")]
                if not targets and not choice.get("Abort"):
                    return True
                if any(reachable(t, seen | {node_id}) for t in targets):
                    return True
            return False
        if nodes and reachable(next(iter(nodes)), set()):
            add(producers, scene["Id"], "Scenes/" + scene["Id"] + "/completion")
    # A consumer must actually reference an input, not just the key of a binding.
    for table in ("Derived", "DerivedForbids", "Latches"):
        for flag, inputs in story.get(table, {}).items():
            for source in strings(inputs):
                add(consumers, source, table + "/" + flag)
    return producers, consumers, negatives, revisits


def lint(story, contracts=None, drafts=None):
    contracts = contracts or json.loads(DEFAULT.read_text(encoding="utf-8"))
    result = {"hard": [], "review": [], "findings": [], "unbound_forbids": []}
    # eng8-q8h begin: a live promise needs an actual surviving endpoint.
    if contracts.get("rescue_endpoint_inventory"):
        result["hard"].extend(rescue_endpoint_errors(story))
    # end eng8-q8h
    shipped = index(story)
    draft_index = index(drafts or {})
    for c in contracts["obligations"]:
        flag = c["flag"]
        if c.get("archival") and not c.get("reason"):
            result["hard"].append(flag + ": archival exemption needs a reason")
        p, readers, _, revisit = draft_index if c.get("draft") else shipped
        row = {"finding": c["finding"], "flag": flag, "scene": c["scene"],
               "source": c["source"], "draft": bool(c.get("draft")),
               "producers": sorted(set(p.get(flag, []))), "consumers": sorted(set(readers.get(flag, [])))}
        if c.get("archival") and c.get("reason"):
            row.update(status="archival", reason=c["reason"])
        elif not row["producers"] and not row["consumers"]:
            row.update(status="no_change_needed", reason="flag absent from current serialized contract")
        elif not row["producers"]:
            row.update(status="missing_producer")
        elif not row["consumers"] and flag not in revisit:
            row.update(status="dead_obligation")
        elif flag in revisit and not row["consumers"]:
            row.update(status="revisit", reason="deferred choice aborts; original offer remains replayable")
        else:
            # Gates are a trace, not evidence that the promised payoff is reachable.
            row.update(status="consumer_review", reason="validate the listed reader's reachable resolution in route acceptance")
        if row["status"] in {"missing_producer", "dead_obligation", "consumer_review"}:
            result["review"].append(row)
        result["findings"].append(row)
    p, _, negatives, _ = shipped
    exemptions = contracts.get("negative_exemptions", {})
    for flag, paths in sorted(negatives.items()):
        if flag in p:
            continue
        if flag in exemptions:
            if not exemptions[flag]:
                result["hard"].append(flag + ": negative exemption needs a reason")
            continue
        result["unbound_forbids"].append({"flag": flag, "consumers": sorted(set(paths))})
    return result


# eng8-q8h begin: retained save graphs are not live successful plans.
def rescue_endpoint_errors(story, contracts=None):
    contracts = contracts or json.loads(Path(__file__).with_name("rescue_endpoint_inventory_contracts.json").read_text(encoding="utf-8"))
    scenes = {s["Id"]: s for s in story.get("Scenes", [])}
    errors = []
    for sid in contracts["retired_offers"]:
        scene = scenes.get(sid)
        if scene is None or not retired(scene):
            errors.append(sid + ": unsupported rescue promise must be explicitly retired")
    plan = contracts["live_plan"]
    for key in ("producer", "endpoint", "return"):
        scene = scenes.get(plan[key])
        if scene is None or retired(scene):
            errors.append(plan[key] + ": sole earned endpoint/producer missing or retired")
    for key, receipt in (("producer", "receipt"), ("endpoint", "rescue_receipt"), ("return", "return_receipt")):
        scene = scenes.get(plan[key], {})
        if not any(plan[receipt] in c.get("Set", []) for n in scene.get("Nodes", []) for c in n.get("Choices", [])):
            errors.append(plan[key] + ": no authored successful receipt")
    producer = scenes.get(plan["producer"], {})
    endpoint = scenes.get(plan["endpoint"], {})
    returned = scenes.get(plan["return"], {})
    # This shared lint checks the immutable successful plan; native custody and
    # encounter observations are replayed by the mandatory rules inventory.
    producer_sets = {f for n in producer.get("Nodes", []) for c in n.get("Choices", []) for f in c.get("Set", [])}
    if producer_sets & set(endpoint.get("Forbids", [])):
        errors.append(plan["endpoint"] + ": producer conflicts with endpoint forbids")
    if plan["receipt"] not in endpoint.get("Requires", []):
        errors.append(plan["endpoint"] + ": endpoint bypasses preparation")
    if plan["rescue_receipt"] not in returned.get("Requires", []):
        errors.append(plan["return"] + ": return bypasses successful rescue")
    return errors
# end eng8-q8h


def load_drafts():
    from storylines import terendelev_continuation
    return {"Scenes": terendelev_continuation.SCENES}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--story", default=str(DEFAULT.parents[1] / "development/Story.json"))
    ap.add_argument("--drafts", action="store_true")
    args = ap.parse_args(argv)
    if args.drafts:
        import sys
        sys.path.insert(0, str(DEFAULT.parents[1]))
    report = lint(json.loads(Path(args.story).read_text(encoding="utf-8")), drafts=load_drafts() if args.drafts else None)
    print(json.dumps(report, indent=2))
    return bool(report["hard"])


if __name__ == "__main__":
    raise SystemExit(main())
