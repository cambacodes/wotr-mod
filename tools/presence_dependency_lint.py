"""Reject contact/return bootstrap cycles across every route (eng7-f4; not L1 leaks)."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.presence_exception_schema import relationship_for
# Retained for callers that explicitly request the original l06 inventory. The CLI and
# strict verifier always check all routes.
OWNED_ROUTES = {"aranka", "camellia", "irabeth", "kaylessa", "nurah", "minagho_chivarro", "nenio", "galfrey"}


def check(story, relationships=None):
    scenes = story.get("Scenes") or []
    rels = story.get("Relationships") or {}
    derived = story.get("Derived") or {}
    latches = story.get("Latches") or {}
    counts = story.get("Counts") or {}
    presences = story.get("Presences") or {}
    receipts = {entry["Flag"]: entry for entry in (story.get("PresenceFailureReceipts") or {}).values()}
    # eng7-f4: failure evidence is produced only by an eligible physical presence.
    receipt_contacts = {entry["Flag"]: name for name, entry in (story.get("PresenceFailureReceipts") or {}).items()}
    # eng7-f4 end
    setters = {}
    active_losses = set()
    independent = set()
    loss_flags = {f for rel in rels.values() for f in rel.get("UnavailableFlags") or []}
    for scene in scenes:
        # Completing a scene is also a producer, even when its terminal answer sets no explicit flags.
        setters.setdefault(scene["Id"], []).append((scene, None, {}))
        for node in scene.get("Nodes") or []:
            for choice in node.get("Choices") or []:
                for flag in choice.get("Set") or []:
                    setters.setdefault(flag, []).append((scene, node, choice))

    def chapter_retired(scene):
        chapters = scene.get("Chapters") or range(scene.get("MinChapter", 0), scene.get("MaxChapter", 6) + 1)
        return bool(chapters) and all(
            (ch >= 2 and "chapter_later" in (scene.get("Forbids") or []))
            or (ch == 1 and "chapter_one" in (scene.get("Forbids") or [])) for ch in chapters)

    # Retirement by a permanent chapter contradiction is deliberate and save-safe.
    # Do not resurrect its consumers to repair a hypothetical development-save cycle.
    retired = set()
    changed = True
    while changed:
        changed = False
        for key in set(setters) | set(derived) | set(latches):
            if key in retired:
                continue
            if key in derived:
                dead = bool(derived[key]) and all(any(k in retired for k in g) for g in derived[key])
            elif key in latches:
                dead = bool(latches[key]) and all(k in retired for k in latches[key])
            else:
                dead = all(chapter_retired(s) or any(k in retired for k in [
                    *(s.get("Requires") or []), *(c.get("Requires") or [])]) for s, _, c in setters[key])
            if dead:
                retired.add(key)
                changed = True

    def sources(key):
        """Primitive producers of a return, including composite/latch/count returns."""
        found, seen = set(), set()
        def visit(source):
            if source in seen:
                return
            seen.add(source)
            if source in derived:
                for group in derived[source]:
                    for member in group:
                        visit(member)
            elif source in latches:
                for member in latches[source]:
                    visit(member)
            elif source in counts:
                for member in counts[source].get("Of", []):
                    visit(member)
            elif source in setters:
                found.add(source)
        visit(key)
        return found

    def held(key, seen=()):
        """Positive evidence forced by this loss history, not merely a possible flag."""
        if key in active_losses:
            return True
        if key in seen:
            return False
        if key in derived:
            return any(all(held(k, (*seen, key)) for k in g) for g in derived[key])
        if key in latches:
            return any(held(k, (*seen, key)) for k in latches[key])
        return False

    def contacts(scene):
        units = [scene.get("ContactUnit"), *(scene.get("AdditionalContactUnits") or [])]
        for unit in filter(None, units):
            candidates = [(name, p) for name, p in presences.items() if p.get("Unit") == unit
                          and (not scene.get("InteractionHub") or unit != scene.get("ContactUnit")
                               or scene["InteractionHub"] == name)]
            if candidates:
                yield unit, candidates

    def conditions_need(obj, target, seen):
        if any(needs(k, target, seen) for k in obj.get("Requires") or []):
            return True
        any_flags = obj.get("RequiresAny") or []
        if any_flags and all(needs(k, target, seen) for k in any_flags):
            return True
        if any(all(needs(k, target, seen) for k in g) for g in obj.get("RequiresAnyGroups") or []):
            return True
        for blocked in obj.get("Forbids") or []:
            if held(blocked):
                lift = (obj.get("ForbidOverrides") or {}).get(blocked)
                if not lift or needs(lift, target, seen):
                    return True
        return False

    def presence_needs(name, p, target, seen):
        declaration = (story.get("PresenceExceptions") or {}).get(name) or {}
        rel = rels.get(relationship_for(name)) or {}
        for loss in active_losses & set(rel.get("UnavailableOverrides") or {}):
            if loss in declaration.get("AbsentLosses", {}):
                continue
            bootstrap = declaration.get("Overrides", {}).get(loss, {}).get("Flag")
            # A declared bootstrap is itself a dependency, even in a malformed export
            # whose physical guard has accidentally omitted it.
            if bootstrap and needs(bootstrap, target, seen):
                return True
            if not declaration:
                return True
        return conditions_need(p, target, seen) or any(
            needs(w["Flag"], target, seen) for w in p.get("ContactWindows") or [])

    def node_needs(scene, node, target, seen):
        # A setter in a later node also depends on the selectable edges that reach it.
        nodes = scene.get("Nodes") or []
        if not nodes:
            return False
        reachable = {nodes[0].get("Id")}
        changed = True
        while changed:
            changed = False
            for parent in nodes:
                if parent.get("Id") not in reachable:
                    continue
                for choice in parent.get("Choices") or []:
                    if conditions_need(choice, target, seen):
                        continue
                    check = choice.get("Check") or {}
                    for nxt in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                        if nxt and nxt not in reachable:
                            reachable.add(nxt)
                            changed = True
        # eng7-f4: an implicit scene flag needs a reachable, selectable completion,
        # including its final answer's guards. Aborts never complete the scene.
        if node is None:
            return not any(parent.get("Id") in reachable and not conditions_need(choice, target, seen)
                           and not choice.get("Next") and not choice.get("Check") and not choice.get("Abort")
                           for parent in nodes for choice in parent.get("Choices") or [])
        # eng7-f4 end
        return node.get("Id") not in reachable

    def needs(key, target, seen=()):
        if key in independent:
            return False
        result = needs_uncached(key, target, seen)
        # Only cache an independent witness. A recursive failure is provisional:
        # another producer may break the cycle, so caching it could hide that road.
        if not result:
            independent.add(key)
        return result

    def needs_uncached(key, target, seen=()):
        if key == target:
            return True
        if key in seen:
            # A mandatory cycle has no independent producer; it cannot bootstrap a physical contact.
            return True
        seen = (*seen, key)
        if key in derived:
            if all(any(needs(k, target, seen) for k in group) for group in derived[key]):
                return True
            for rel in (story.get("DerivedOpenRoutes") or {}).get(key, []):
                for loss, returned in rels.get(rel, {}).get("UnavailableOverrides", {}).items():
                    if loss in active_losses and needs(returned, target, seen):
                        return True
            # A live loss blocker is false only when at least one of its earned lifts is independently reachable.
            for blocked in (story.get("DerivedForbids") or {}).get(key, []):
                if held(blocked):
                    lifts = (story.get("DerivedForbids") or {}).get(blocked, [])
                    if not lifts or all(needs(lift, target, seen) for lift in lifts):
                        return True
            return False
        if key in latches:
            return all(needs(k, target, seen) for k in latches[key])
        if key in counts:
            spec = counts[key]
            return sum(not needs(k, target, seen) for k in spec.get("Of", [])) < spec.get("Min", 1)
        if key in receipts:
            # eng7-f4: match RecordPresenceFailure's receipt AND PresenceWanted checks.
            name = receipt_contacts[key]
            return conditions_need(receipts[key], target, seen) or (
                name in presences and presence_needs(name, presences[name], target, seen))
            # eng7-f4 end
        if key.endswith(".failed") and key[:-7] in presences:
            name = key[:-7]
            return presence_needs(name, presences[name], target, seen)
        if key in setters:
            def setter_needs(scene, node, choice):
                if (conditions_need(scene, target, seen) or conditions_need(choice, target, seen)
                        or node_needs(scene, node, target, seen)):
                    return True
                return any(all(presence_needs(name, p, target, seen) for name, p in candidates)
                           for _, candidates in contacts(scene))
            return all(setter_needs(s, n, c) for s, n, c in setters[key])
        return False

    def dependency_contacts(scene, node, choice, target, seen=()):
        """Also follow a remote return's mandatory prerequisites to physical producers."""
        found = set()
        for _, candidates in contacts(scene):
            if all(presence_needs(name, p, target, ()) for name, p in candidates):
                found.update(name for name, _ in candidates)
        objects = [scene, choice]
        if node_needs(scene, node, target, ()):
            objects += [c for n in scene.get("Nodes") or [] for c in n.get("Choices") or []]
        # eng7-f4: follow mandatory dependencies, preserving independent OR roads.
        keys = set()
        for obj in objects:
            keys.update(obj.get("Requires") or [])
            groups = [obj.get("RequiresAny") or [], *(obj.get("RequiresAnyGroups") or [])]
            for group in groups:
                if group and all(needs(k, target) for k in group):
                    keys.update(group)
            for blocked, lift in (obj.get("ForbidOverrides") or {}).items():
                if blocked in (obj.get("Forbids") or []) and held(blocked):
                    keys.add(lift)
        # eng7-f4 end

        def visit(key, path):
            if key in path or key == target or not needs(key, target):
                return
            path = (*path, key)
            # eng7-f4: a remote fallback still needs an eligible failed placement.
            # Follow both transient observations and durable receipt eligibility.
            if key in receipts:
                name = receipt_contacts[key]
                if name in presences:
                    found.add(name)
                for member in receipts[key].get("Requires") or []:
                    visit(member, path)
            elif key.endswith(".failed") and key[:-7] in presences:
                found.add(key[:-7])
            # eng7-f4 end
            if key in setters:
                for s, n, c in setters[key]:
                    found.update(dependency_contacts(s, n, c, target, path))
            for member in [*(k for g in derived.get(key, []) for k in g), *latches.get(key, []),
                           *(counts.get(key) or {}).get("Of", [])]:
                visit(member, path)
        for key in keys:
            visit(key, seen)
        return found

    hard = []
    for rel_name, rel in rels.items():
        if relationships is not None and rel_name not in relationships:
            continue
        returns = set((rel.get("UnavailableOverrides") or {}).items())
        # Some routes advertise an earned return in TricksterAccess without using
        # an UnavailableOverride (e.g. a physical arrival, release or audience).
        for access in (rel.get("TricksterAccess") or {}).values():
            returned = access.get("Returned", access.get("returned"))
            if returned:
                detects = [k for k in access.get("Detect", access.get("detect", [])) if not k.startswith("!")]
                returns.update((loss, returned) for loss in detects or [None])
        for loss, returned in returns:
            for scene, node, choice in [p for key in sources(returned) for p in setters[key]]:
                if chapter_retired(scene) or any(k in retired for k in scene.get("Requires") or []):
                    continue
                # Each authored device serves only its declared native histories.
                # An away correction is not a resurrection; the living wagon is
                # not a return from a player-chosen cage execution.
                state = scene.get("TricksterState")
                access = rel.get("TricksterAccess") or {}
                if state is not None and state in access:
                    detects = access[state].get("Detect", access[state].get("detect", []))
                    if loss is not None and loss not in detects:
                        continue
                # Preparations forbidden in the loss history can be earned beforehand.
                if loss in (scene.get("Forbids") or []) and loss not in (scene.get("ForbidOverrides") or {}):
                    continue
                active_losses = ({loss} if loss else set()) | (set(scene.get("Requires") or []) & loss_flags)
                independent.clear()
                for name in dependency_contacts(scene, node, choice, returned):
                    hard.append("PD1 %s: %s/%s requires contact %s before producing %s; no independent earned bootstrap"
                                % (scene["Id"], rel_name, loss, name, returned))
    return sorted(set(hard))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", default="development/Story.json")
    parser.add_argument("--all", action="store_true", help="compatibility alias; all routes are always checked")
    parser.add_argument("--strict", action="store_true", help="fail on any cycle (also the default)")
    args = parser.parse_args()
    hard = check(json.loads(Path(args.story).read_text(encoding="utf-8")))
    for error in hard:
        print(error)
    print("presence dependencies: %d hard" % len(hard))
    return bool(hard)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    raise SystemExit(main())
