"""Declarative current-availability gates; no new return, price or romance state.

The epoch observer in Rules orders native loss observations and existing earned
returns. These keys are observations, not authored choice effects or latches.
"""
import copy

BASE = [["availability.observed"]]


def require(spec, key):
    spec["Requires"] = list(dict.fromkeys([*spec.get("Requires", []), key]))


def install(story, contracts):
    derived = story.setdefault("Derived", {})
    forbids = story.setdefault("DerivedForbids", {})
    story["DepartureEpochs"] = {}
    derived.update(contracts.get("return_predicates", {}))
    # Explicit absence/recovery narration retains its historical body report;
    # permission to send fresh correspondence is a different reader.
    derived.update(contracts.get("absence_predicates", {}))
    forbids.update(contracts.get("absence_forbids", {}))
    for woman, contract in contracts["women"].items():
        route = contract["relationship"]
        if route not in story["Relationships"]:
            continue
        key = woman + ".present_now"
        blocked = woman + ".epoch_unavailable"
        story["DepartureEpochs"][woman] = {
            "Relationship": route, "Losses": contract["losses"],
            "Returns": contract["returns"], "Overrides": contract["overrides"], "UnavailableFlag": blocked,
            "NativeClearReturns": contract.get("native_clear_returns", {}),
            "ReturnTriggers": contract.get("return_triggers", {}),
            "AdditionalRelationships": contract.get("additional_relationships", []),
        }
        inputs = list(contract.get("body_requires", []))
        for i, loss in enumerate(contract["losses"]):
            clear = key + ".clear." + str(i)
            derived[clear] = copy.deepcopy(BASE)
            forbids[clear] = [loss]
            back = contract["overrides"].get(loss)
            if back:
                lifted = key + ".loss." + str(i)
                derived[lifted] = [[clear], [back]]
                inputs.append(lifted)
            else:
                inputs.append(clear)
        derived[key] = [g + inputs for g in BASE]
        forbids[key] = [blocked]
        # Default NO correspondence to an unavailable woman. Exceptions are
        # route-authored departure terms, recorded individually in the registry.
        letter = woman + ".reachable_by_letter"
        derived[letter] = [[key]]
        for permitted in contract.get("letter_terms", []):
            departed = letter + ".departed." + str(len(derived[letter]))
            derived[departed] = [permitted["requires"]]
            forbids[departed] = permitted["forbids"]
            derived[letter].append([departed])
        for participant_route in [route, *contract.get("additional_relationships", [])]:
            rel = story["Relationships"][participant_route]
            rel["EpochUnavailableFlags"] = list(dict.fromkeys([*rel.get("EpochUnavailableFlags", []), blocked]))
        alias = contracts.get("life_aliases", {}).get(woman)
        if alias:
            forbids[alias] = list(dict.fromkeys([*forbids.get(alias, []), blocked]))
        # Named seats remain independent of the other woman's availability.
        if woman in story.get("SeatWomen", {}):
            seat = story["SeatWomen"][woman]
            require(seat, key)
            seat["UnavailableFlags"] = list(dict.fromkeys([*seat.get("UnavailableFlags", []), blocked]))
        for name, presence in story.get("Presences", {}).items():
            if name in contract["presences"] and name not in contract.get("acquisition_presences", []):
                require(presence, key)
            elif name in contract.get("acquisition_presences", []):
                # A paid bootstrap may answer its nominated original loss;
                # it never answers a later departure or a saved actor death.
                presence["Forbids"] = list(dict.fromkeys([*presence.get("Forbids", []), woman + ".epoch_redeparted",
                                                         woman + ".returned_actor_lost"]))
        for surface in contract["surfaces"]:
            scene = next((s for s in story["Scenes"] if s["Id"] == surface["scene"]), None)
            if scene is None:
                continue
            target = scene
            if "paragraph" in surface or "choice" in surface:
                node = next(n for n in scene["Nodes"] if n["Id"] == surface["node"])
                target = node["Choices"][surface["choice"]] if "choice" in surface else node["Paragraphs"][surface["paragraph"]]
            require(target, letter if surface.get("letter") else key)
        for book in story.get("Books", {}).values():
            for entry in book.get("Entries", []):
                if entry["Id"] in contract["guests"]:
                    require(entry, key)
        # Existing live cross-route readers retain their older negatives and
        # now also read the current epoch. History readers are untouched.
        for live, gate in (("crossroute." + woman + ".available", key),
                           ("crossroute." + woman + ".correspondent", letter),
                           ("participant." + woman + ".available", key)):
            if live in derived:
                derived[live] = [g if gate in g else g + [gate] for g in derived[live]]

    # Existing independent named seats survive the other woman's absence.
    # Every joint depiction still reads both women's present_now gates.
    for route, women in contracts.get("seat_epoch_guards", {}).items():
        if route not in story["Relationships"]:
            continue
        guard = route + ".epoch_unavailable"
        members = [woman + ".epoch_unavailable" for woman in women]
        derived[guard] = [members]
        rel = story["Relationships"][route]
        rel["EpochUnavailableFlags"] = [key for key in rel["EpochUnavailableFlags"] if key not in members] + [guard]
