"""eng7-l06: reject paid return -> contact -> same return dependency cycles (not L1 leaks)."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.presence_exception_schema import relationship_for

OWNED_ROUTES = {"aranka", "camellia", "irabeth", "kaylessa", "nurah", "minagho_chivarro", "nenio", "galfrey"}


def check(story, relationships=None):
    scenes = story.get("Scenes") or []
    rels = story.get("Relationships") or {}
    derived = story.get("Derived") or {}
    setters = {}
    active_losses = set()
    for scene in scenes:
        # Completing a scene is also a producer, even when its terminal answer sets no explicit flags.
        setters.setdefault(scene["Id"], []).append((scene, {}))
        for node in scene.get("Nodes") or []:
            for choice in node.get("Choices") or []:
                for flag in choice.get("Set") or []:
                    setters.setdefault(flag, []).append((scene, choice))

    def needs(key, target, seen=()):
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
                groups = derived.get(blocked, [])
                if groups and any(set(g) <= active_losses for g in groups):
                    lifts = (story.get("DerivedForbids") or {}).get(blocked, [])
                    if lifts and all(needs(lift, target, seen) for lift in lifts):
                        return True
            return False
        if key in setters:
            def setter_needs(scene, choice):
                if any(needs(k, target, seen) for k in [*scene.get("Requires", []), *choice.get("Requires", [])]):
                    return True
                candidates = [(name, p) for name, p in (story.get("Presences") or {}).items()
                              if p.get("Unit") == scene.get("ContactUnit") and scene.get("ContactUnit")
                              and (not scene.get("InteractionHub") or scene["InteractionHub"] == name)]
                return bool(candidates) and all(any(needs(k, target, seen) for k in p.get("Requires", []))
                                                for _, p in candidates)
            return all(setter_needs(s, c) for s, c in setters[key])
        return False

    hard = []
    for scene in scenes:
        if relationships is not None and scene.get("Relationship") not in relationships:
            continue
        unit = scene.get("ContactUnit")
        if not unit:
            continue
        rel = rels.get(scene.get("Relationship")) or {}
        outputs = {f for n in scene.get("Nodes") or [] for c in n.get("Choices") or [] for f in c.get("Set") or []}
        for name, presence in (story.get("Presences") or {}).items():
            if presence.get("Unit") != unit or relationship_for(name) != scene.get("Relationship"):
                continue
            if scene.get("InteractionHub") and scene["InteractionHub"] != name:
                continue
            losses = set(scene.get("Requires") or []) | set(presence.get("Requires") or [])
            active_losses = losses
            declaration = (story.get("PresenceExceptions") or {}).get(name) or {}
            for loss, returned in (rel.get("UnavailableOverrides") or {}).items():
                if loss not in losses or returned not in outputs or loss in declaration.get("AbsentLosses", {}):
                    continue
                bootstrap = declaration.get("Overrides", {}).get(loss, {}).get("Flag")
                if not bootstrap or needs(bootstrap, returned):
                    hard.append("PD1 %s: %s requires contact %s before producing %s; no independent earned bootstrap"
                                % (scene["Id"], loss, name, returned))
    return hard


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", default="development/Story.json")
    parser.add_argument("--all", action="store_true", help="also inventory routes outside this lane's authorized wiring")
    args = parser.parse_args()
    hard = check(json.loads(Path(args.story).read_text(encoding="utf-8")), None if args.all else OWNED_ROUTES)
    for error in hard:
        print(error)
    print("presence dependencies: %d hard" % len(hard))
    return bool(hard)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    raise SystemExit(main())
