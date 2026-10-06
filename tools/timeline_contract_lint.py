"""E-Q7-18: explicit temporal assertions; diagnostics never grant an outcome.

Producer floors are optimistic bounds, not proof of a playable itinerary. Concrete
histories use arrival_hour and check_age with the actual held flags/timestamps.
Unsupported prose is REVIEW (route-owned); malformed contracts are HARD.
"""
import argparse
import copy
import json
from pathlib import Path

DEFAULT = Path(__file__).with_name("timeline_contracts.json")
NATIVE_TABLES = ("Etudes", "SeenCues", "SelectedAnswers", "StartedDialogs",
                 "CompletedQuests", "CompletedEtudes", "StartedQuests", "MainCharacterFacts",
                 "QuestObjectives", "InventoryItems", "PartyItems", "UnlockableFlags")

# eng8-q8d: validate cumulative executed ages, never independently aged flags.
def delivered_timeline(history):
    steps = history["steps"]
    hours = [step["hour"] for step in steps]
    if any(type(hour) is not int or hour < 0 for hour in hours) or hours != sorted(hours):
        return "nonchronological delivered history"
    if history.get("maximum_hours") is None:
        return None
    origin = history["origin"]
    witnesses = [step["hour"] for step in steps if origin in step.get("set", [])]
    if not witnesses:
        return "missing cumulative origin " + origin
    return check_age(dict(origins=[origin], maximum_hours=history["maximum_hours"]),
                     {origin}, {origin: witnesses[0]}, hours[-1])
# end eng8-q8d


def arrival_hour(scene, flags, times, hour=0):
    """Rules.Available's delay clock: all held OR-group members count.

    RequiresAny is an availability condition, but is not part of Owlcat/RRT's
    implemented delay clock. Unknown timestamps do not manufacture a wait.
    """
    if not set(scene.get("Requires", ())) <= flags:
        raise ValueError("missing prerequisite: " + scene["Id"])
    if scene.get("RequiresAny") and not flags.intersection(scene["RequiresAny"]):
        raise ValueError("missing RequiresAny: " + scene["Id"])
    if any(not flags.intersection(g) for g in scene.get("RequiresAnyGroups", ())):
        raise ValueError("missing OR producer: " + scene["Id"])
    overrides = scene.get("ForbidOverrides", {})
    if any(f in flags and overrides.get(f) not in flags for f in scene.get("Forbids", ())):
        raise ValueError("forbidden history: " + scene["Id"])
    clock = [*scene.get("Requires", ()),
             *(f for g in scene.get("RequiresAnyGroups", ()) for f in g if f in flags)]
    delay = scene.get("DelayHours", 0)
    last = max((times[f] for f in clock if f in times), default=hour - delay)
    return max(hour, last + delay)


def check_age(contract, flags, times, hour):
    """Fail closed for a claimed duration with an absent/invalid timestamp."""
    origins = contract.get("origins", [])
    held = [f for f in origins if f in flags]
    if not held:
        return "missing origin"
    if any(f not in times or times[f] < 0 or times[f] > hour for f in held):
        return "missing/future origin timestamp"
    # A callback naming alternatives must be true for every held origin.
    age = hour - max(times[f] for f in held)
    if age < contract.get("minimum_hours", 0):
        return f"{age}h below {contract['minimum_hours']}h minimum"
    if contract.get("maximum_hours") is not None and age > contract["maximum_hours"]:
        return f"{age}h exceeds {contract['maximum_hours']}h maximum"
    if contract.get("calendar_witness") and contract["calendar_witness"] not in flags:
        return "missing calendar witness"
    return None


def replay_schedule(story, schedule):
    """Replay declared timing witnesses through real choice producers.

    This is a timing walk: contacts/placement remain the C# acceptance's job.
    Initial authored composite/choice facts are forbidden. A check's two native
    outcomes are explored independently; no union of outcomes supplies a gate.
    """
    native = {f for table in NATIVE_TABLES for f in story.get(table, {})}
    seed = set(schedule["native"])
    if not seed <= native:
        raise ValueError("unbound/authored schedule seed: " + ",".join(sorted(seed - native)))
    state = dict(flags=seed, times={f: 0 for f in seed}, hour=0,
                 resources=dict(schedule.get("resources", {})))
    scenes = {s["Id"]: s for s in story["Scenes"]}
    trace = []
    # eng-final: each observation rebuilds live Derived readers. They are not
    # latches: a paid return must retire yesterday's unavailability, and a new
    # loss must retire yesterday's eligibility. Settle negative dependencies
    # before their consumers, as Rules.DerivedOrder does.
    derived = story.get("Derived", {})
    order, visited = [], set()
    def visit(key):
        if key in visited:
            return
        visited.add(key)
        inputs = [f for group in derived[key] for f in group]
        inputs += story.get("DerivedForbids", {}).get(key, [])
        for route in story.get("DerivedOpenRoutes", {}).get(key, []):
            rel = story["Relationships"][route]
            inputs += [rel["ClosedFlag"], *rel.get("UnavailableFlags", []),
                       *rel.get("UnavailableOverrides", {}).values()]
        for flag in inputs:
            if flag in derived:
                visit(flag)
        order.append(key)
    for key in derived:
        visit(key)
    def complete(at):
        if story.get("DepartureEpochs"):
            at["flags"].add("availability.observed")
        old_times = {key: at["times"][key] for key in derived if key in at["times"]}
        at["flags"].difference_update(derived)
        for key in derived:
            at["times"].pop(key, None)
        for _ in range(len(derived) + len(story.get("Latches", {})) + 1):
            changed = False
            for table in ("Latches", "Derived"):
                entries = story.get(table, {}).items() if table == "Latches" else ((key, derived[key]) for key in order)
                for flag, inputs in entries:
                    groups = [[f] for f in inputs] if table == "Latches" else inputs
                    if flag not in at["flags"] and any(set(g) <= at["flags"] for g in groups):
                        if set(story.get("DerivedForbids", {}).get(flag, [])) & at["flags"]:
                            continue
                        guards = story.get("DerivedOpenRoutes", {}).get(flag, [])
                        if any(story["Relationships"][r]["ClosedFlag"] in at["flags"] or any(
                                loss in at["flags"] and rel.get("UnavailableOverrides", {}).get(loss) not in at["flags"]
                                for loss in rel.get("UnavailableFlags", []))
                               for r in guards for rel in [story["Relationships"][r]]):
                            continue
                        at["flags"].add(flag)
                        at["times"][flag] = old_times.get(flag, at["hour"])
                        changed = True
            if not changed:
                break
    complete(state)
    for step in schedule["steps"]:
        scene = scenes[step["scene"]]
        state["hour"] = arrival_hour(scene, state["flags"], state["times"], state["hour"])
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        def walk(node_id, at, seen):
            if node_id in seen:
                return None
            for index, choice in enumerate(nodes[node_id].get("Choices", [])):
                if not set(choice.get("Requires", [])) <= at["flags"] or set(choice.get("Forbids", [])) & at["flags"]:
                    continue
                cost = choice.get("Crusade")
                if cost and cost["Amount"] < 0 and at["resources"].get(cost["Resource"], 0) < -cost["Amount"]:
                    continue
                after = copy.deepcopy(at)
                if cost:
                    resource = cost["Resource"]
                    after["resources"][resource] = after["resources"].get(resource, 0) + cost["Amount"]
                for flag in choice.get("Set", []):
                    if flag not in after["flags"]:
                        after["flags"].add(flag); after["times"][flag] = after["hour"]
                complete(after)
                targets = [choice["Next"]] if choice.get("Next") else []
                if choice.get("Check"):
                    targets += [choice["Check"][k] for k in ("Success", "Failure")]
                for target in targets:
                    found = walk(target, after, seen | {node_id})
                    if found:
                        return found[0], [(node_id, index), *found[1]]
                if not targets and not choice.get("Abort") and set(step["want"]) <= after["flags"]:
                    after["flags"].add(scene["Id"]); after["times"][scene["Id"]] = after["hour"]
                    return after, [(node_id, index)]
            return None
        found = walk(scene["Nodes"][0]["Id"], state, set())
        if not found:
            raise ValueError("no affordable completing producer: " + scene["Id"])
        state, path = found
        trace.append(dict(scene=scene["Id"], hour=state["hour"], path=path, produced=step["want"]))
    error = check_age(schedule, state["flags"], state["times"], state["hour"])
    return dict(name=schedule["name"], hour=state["hour"], trace=trace, failure=error)


def producer_floors(story):
    """Earliest optimistic timestamp by producer fixed point, including ORs.

    Choice branches are separate producers, never summed. This deliberately
    reports a lower bound: it cannot certify affordability, native chronology,
    mutually incompatible branch choices, contacts, or player travel.
    """
    times = {f: 0 for table in NATIVE_TABLES for f in story.get(table, {})}
    producers = []
    for scene in story.get("Scenes", []):
        base = set(scene.get("Requires", []))
        groups = list(scene.get("RequiresAnyGroups", []))
        if scene.get("RequiresAny"):
            groups = [*groups, scene["RequiresAny"]]
        nodes = {n["Id"]: n for n in scene.get("Nodes", [])}
        visited = set()
        def paths(node_id):
            if node_id in visited:
                return
            visited.add(node_id)
            node = nodes[node_id]
            for choice in node.get("Choices", []):
                # A floor deliberately ignores path-specific conditions. Using
                # them here would mistake flags earned earlier on this page for
                # external prerequisites. Concrete-history checks do not do so.
                effects = set(choice.get("Set", []))
                producers.append((effects, base, groups, scene))
                targets = [choice["Next"]] if choice.get("Next") else []
                if choice.get("Check"):
                    targets += [choice["Check"][k] for k in ("Success", "Failure")]
                if not targets and not choice.get("Abort"):
                    producers.append(({scene["Id"]}, base, groups, scene))
                for target in targets:
                    if target in nodes:
                        paths(target)
        if nodes:
            paths(next(iter(nodes)))
    trace = {}
    for _ in range(len(producers) + len(story.get("Derived", {})) + 1):
        changed = False
        def offer(flag, at, source):
            nonlocal changed
            if at < times.get(flag, float("inf")):
                times[flag], trace[flag], changed = at, source, True
        for table in ("Derived", "Latches"):
            for flag, groups in story.get(table, {}).items():
                if table == "Latches":
                    groups = [[f] for f in groups]
                for group in groups:
                    if all(f in times for f in group):
                        offer(flag, max((times[f] for f in group), default=0), {"inputs": group})
        for flags, req, groups, scene in producers:
            if not req <= times.keys() or any(not set(g).intersection(times) for g in groups):
                continue
            inputs = [*req, *(min((f for f in g if f in times), key=lambda f: times[f]) for g in groups)]
            clock_groups = scene.get("RequiresAnyGroups", [])
            clock = [*req, *(min((f for f in g if f in times), key=lambda f: times[f]) for g in clock_groups)]
            # RequiresAny can postpone availability without resetting the delay.
            ready = max((times[f] for f in inputs), default=0)
            at = max(ready, max(times[f] for f in clock) + scene.get("DelayHours", 0)) if clock else ready
            for flag in flags:
                offer(flag, at, {"scene": scene["Id"], "inputs": sorted(inputs)})
        if not changed:
            break
    return times, trace


def lint(story, contracts=None):
    contracts = contracts or json.loads(DEFAULT.read_text(encoding="utf-8"))
    scenes = {s["Id"]: s for s in story.get("Scenes", [])}
    floors, traces = producer_floors(story)
    result = {"hard": [], "review": [], "findings": [], "schedules": []}
    schedule_results = {}
    for schedule in contracts.get("schedules", []):
        try:
            witness = replay_schedule(story, schedule)
        except (ValueError, KeyError) as error:
            witness = dict(name=schedule["name"], failure=str(error))
        result["schedules"].append(witness)
        schedule_results.setdefault(schedule["finding"], []).append(witness)
        if witness["failure"]:
            result["hard"].append(witness)
    seen = set()
    for c in contracts["contracts"]:
        if (c["finding"] in seen or not c.get("origins")
                or any(type(c.get(k, 0)) is not int or c.get(k, 0) < 0
                       for k in ("minimum_hours", "maximum_hours"))
                or c.get("maximum_hours", float("inf")) < c.get("minimum_hours", 0)):
            result["hard"].append(c["finding"] + ": invalid timing contract")
            continue
        seen.add(c["finding"])
        scene = scenes.get(c["scene"])
        row = {"finding": c["finding"], "scene": c["scene"], "source": c["source"]}
        if scene is None:
            row.update(status="not_in_export", reason="retained source/draft must be reviewed before registration")
        else:
            nodes = [n for n in scene.get("Nodes", []) if not c.get("node") or n["Id"] == c["node"]]
            texts = [scene.get("Entry", ""), scene.get("Title", "")]
            if c.get("node"):
                texts = []
            texts += [n.get("Text", "") for n in nodes]
            texts += [p.get("Text", "") for n in nodes for p in n.get("Paragraphs", [])]
            texts += [a.get("Text", "") for n in nodes for a in n.get("Choices", [])]
            # Last Call carries its actual spoken callback in the call registry.
            texts += [v.get("Text", "") for v in story.get("LastCallCalls", {}).values()
                      if isinstance(v, dict) and v.get("Scene") == c["scene"]]
            active = any(c.get("claim", "").casefold() in t.casefold() for t in texts) if c.get("claim") else True
            if c["finding"] in schedule_results:
                witnesses = schedule_results[c["finding"]]
                row.update(status="verified" if all(not w["failure"] for w in witnesses) else "timing_failure",
                           witnesses=witnesses)
            elif not active:
                row.update(status="no_change_needed", reason="cited duration removed/qualified in current text")
            else:
                row.update(status="review", origins=c.get("origins", []), minimum_hours=c.get("minimum_hours"),
                           maximum_hours=c.get("maximum_hours"), calendar=c.get("calendar"),
                           producer_floors={f: floors.get(f) for f in c.get("origins", [])},
                           producer_trace={f: traces.get(f) for f in c.get("origins", [])},
                           reason="verify origin-relative age with a concrete producer history; no elapsed/calendar witness declared")
                result["review"].append(row)
        result["findings"].append(row)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--story", default=str(DEFAULT.parents[1] / "development/Story.json"))
    ap.add_argument("--contracts", type=Path, default=DEFAULT)
    args = ap.parse_args(argv)
    report = lint(json.loads(Path(args.story).read_text(encoding="utf-8")), json.loads(args.contracts.read_text(encoding="utf-8")))
    print(json.dumps(report, indent=2))
    return bool(report["hard"])


if __name__ == "__main__":
    raise SystemExit(main())
