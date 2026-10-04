"""eng7-l06: serialized, per-contact bootstrap guards shared by all readers."""
import re


def relationship_for(name):
    match = re.fullmatch(r"(.+?)\.presence(?:\.[a-z0-9_]+)?", name)
    return match[1] if match else None


def guard_fields(rel, relationship, declaration=None):
    declaration = declaration or {}
    key = declaration.get("Guard", rel + ".presence.route_open")
    fields = {"Derived": {key: [["chapter_one"], ["chapter_later"]]}}
    if not declaration:
        fields["DerivedOpenRoutes"] = {key: [rel]}
        return fields
    blockers = [relationship["ClosedFlag"]]
    forbids = fields["DerivedForbids"] = {}
    for flag in relationship.get("UnavailableFlags") or []:
        if flag in declaration.get("AbsentLosses", {}):
            continue
        blocked = key + ".blocked." + flag
        fields["Derived"][blocked] = [[flag]]
        blockers.append(blocked)
        lifts = list(filter(None, [(relationship.get("UnavailableOverrides") or {}).get(flag)]))
        entry = declaration.get("Overrides", {}).get(flag)
        if entry:
            # These are existing earned histories. Actual new return acts retain their current-path gates.
            lifts.append(entry["Flag"])
        if lifts:
            forbids[blocked] = list(dict.fromkeys(lifts))
    forbids[key] = blockers
    return fields


def errors(story):
    errors = []
    declarations = story.get("PresenceExceptions") or {}
    for name, decl in declarations.items():
        rel = relationship_for(name)
        relationship = (story.get("Relationships") or {}).get(rel)
        if name not in (story.get("Presences") or {}) or not relationship:
            errors.append("P1 declaration has no contact: " + name)
            continue
        losses = set(relationship.get("UnavailableFlags") or [])
        if (set(decl) != {"Guard", "Overrides", "AbsentLosses"}
                or not isinstance(decl.get("Guard"), str) or not decl["Guard"].startswith(rel + ".presence.")):
            errors.append("P1 malformed declaration: " + name)
            continue
        for loss, entry in decl["Overrides"].items():
            if (loss not in losses or set(entry) != {"Flag", "Reason"}
                    or not isinstance(entry.get("Flag"), str) or not entry["Flag"]
                    or not isinstance(entry.get("Reason"), str) or not entry["Reason"].strip()):
                errors.append("P1 bootstrap needs a registered loss, earned flag and reason: " + name + "/" + loss)
            if entry.get("Flag") in {"trickster", "trickster.ever", "trickster.was", "trickster.now"} and not (
                    name == "nurah.presence.cell" and loss == "nurah.prison" and entry["Flag"] == "trickster.now"):
                errors.append("P1 a path latch is not an earned bootstrap: " + name + "/" + loss)
        for loss, reason in decl["AbsentLosses"].items():
            # Only these paired contacts have an independently absent woman.
            own = "chivarro.dead" if name.endswith(".chivarro") else "minagho.dead"
            if (rel != "minagho_chivarro" or loss not in losses or loss == own
                    or not isinstance(reason, str) or not reason.strip()):
                errors.append("P1 unrelated-loss exception is not an absent partner: " + name + "/" + loss)
    for name, presence in (story.get("Presences") or {}).items():
        rel = relationship_for(name)
        relationship = (story.get("Relationships") or {}).get(rel)
        if not relationship:
            continue
        decl = declarations.get(name)
        try:
            expected = guard_fields(rel, relationship, decl)
        except (KeyError, TypeError):
            errors.append("P1 malformed bootstrap: " + name)
            continue
        guard = (decl or {}).get("Guard", rel + ".presence.route_open")
        if guard not in (presence.get("Requires") or []):
            errors.append("P1 missing declared guard: " + name)
        for field in ("Derived", "DerivedOpenRoutes", "DerivedForbids"):
            for key in expected["Derived"]:
                if (story.get(field) or {}).get(key) != expected.get(field, {}).get(key):
                    errors.append("P1 guard differs from serialized declaration: " + name + "/" + key)
    return errors
