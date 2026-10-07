"""eng7-l13: enforce existing outcome eligibility at generation, after integration.

No new prices or repairs. DerivedOpenRoutes preserves the relationship's exact
loss/return semantics; negative inputs stay live, never become history latches.
The same finite reward vocabulary is used by L4. The proof walker locates all
incoming edges, including check branches; node fields are never used as gates.
Exemptions describe historical/negative prose and are reviewed in the inventory.
"""
import json
import copy
from pathlib import Path

from story_format import c
from tools.crossroute_checks import late_commitment as policy
from tools.crossroute_checks.common import Proof, blocks, lit, scene_context, dependencies, verify

CONTRACTS = json.loads((Path(__file__).resolve().parents[1] /
                       "tools/earned_outcome_inventory_contracts.json").read_text(encoding="utf-8"))


def integrate(payload):
    # Authoring constants may share override dictionaries across sibling pages.
    # Detach only the surfaces this pass writes: reader changes must not mutate
    # authoring constants consumed by a later export. ForesightConsumers keeps
    # its intentional live registry reference for late consumer registration.
    for field in ("Derived", "DerivedForbids", "DerivedOpenRoutes", "Books", "Relationships"):
        if field in payload:
            payload[field] = copy.deepcopy(payload[field])
    payload["Scenes"] = [copy.deepcopy(s) for s in payload["Scenes"]]
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    open_routes = payload.setdefault("DerivedOpenRoutes", {})
    # Universal native chapter alternatives, rather than an authored free flag.
    always = [["chapter_one"], ["chapter_later"], ["trickster.ever"]]

    def negative(key, blocked):
        derived[key] = [g[:] for g in always]
        forbids[key] = list(blocked)
        return key

    def eligibility(route, repaired_now=False, woman=None):
        key = route + ".outcome.route_open"
        derived[key] = [g[:] for g in always]
        open_routes[key] = [route]
        if woman:
            # A named solo reward reads that woman's losses and the route's
            # common blockers, matching SeatWomen, rather than requiring a pair.
            key = route + ".outcome." + woman + "_open"
            rel = payload["Relationships"][route]
            other = "minagho" if woman == "chivarro" else "chivarro"
            excluded = payload["SeatWomen"][other]["UnavailableFlags"]
            inputs = []
            for flag in [rel["ClosedFlag"], *rel.get("UnavailableFlags", [])]:
                if flag in excluded:
                    continue
                clear = negative(key + ".not." + flag, [flag])
                back = rel.get("UnavailableOverrides", {}).get(flag)
                if back:
                    lifted = key + ".lifted." + flag
                    derived[lifted] = [[clear], [back]]
                    inputs.append(lifted)
                else:
                    inputs.append(clear)
            if woman == "chivarro":
                # Her own walk-out still needs its authored return. Minagho's
                # solo road never requires the absent partner to come back.
                inputs.append(route + ".outcome.pair_repaired")
            derived[key] = [inputs]
            return key
        rule = CONTRACTS["refusal_control"].get(route)
        if rule and not repaired_now:
            clear = negative(route + ".outcome.unrefused", [rule[0]])
            control = route + ".outcome.control"
            derived[control] = [[clear], [rule[1]]]
            key = route + ".outcome.eligible"
            derived[key] = [[route + ".outcome.route_open", control]]
        if route == "mielarah":
            clear = negative(route + ".outcome.no_sacrifice", ["mielarah.trickster.cost.meant"])
            control = route + ".outcome.consequence"
            derived[control] = [[clear], ["mielarah.deck.oskel_settled"]]
            key = route + ".outcome.eligible"
            derived[key] = [[route + ".outcome.route_open", control]]
        if route == "minagho_chivarro":
            clear = negative(route + ".outcome.not_walked", ["minagho_chivarro.trickster.chivarro_walked"])
            control = route + ".outcome.pair_repaired"
            derived[control] = [[clear], ["minagho_chivarro.trickster.cost.won_back"]]
            key = route + ".outcome.eligible"
            derived[key] = [[route + ".outcome.route_open", control]]
        return key

    # Register every route before proof construction, including ordinary routes:
    # their automatic Available guard already proves this key in live scenes.
    for route in payload["Relationships"]:
        eligibility(route)
    for woman in ("minagho", "chivarro"):
        eligibility("minagho_chivarro", woman=woman)

    # These keys offer the already-written late road. They are eligibility, not
    # proof that the player took its yes. Keep their existing preparation inputs.
    for key in list(derived):
        if key.endswith("late_committed"):
            route = key.split(".trickster.")[0]
            if route in payload["Relationships"]:
                gate = eligibility(route)
                derived[key] = [g if gate in g else g + [gate] for g in derived[key]]
                # Read existing late-page refusal forbids, never invent a new
                # refusal or reconciliation. Kaylessa and Jannah have explicit
                # repairs below/in eligibility; keep those repairs authoritative.
                if route not in ("kaylessa", "jannah"):
                    blockers = policy.late_refusals(payload, key, route)
                    for flag in sorted(blockers):
                        clear = negative(key + ".without." + flag, [flag])
                        if blockers[flag]:
                            lifted = key + ".refusal_lifted." + flag
                            derived[lifted] = [[clear], *[[back] for back in blockers[flag]]]
                            clear = lifted
                        derived[key] = [g + [clear] for g in derived[key]]
    # Kaylessa's existing second offer clears the earlier refusal through LATE_YES.
    clear = negative("kaylessa.outcome.not_declined", ["kaylessa.trickster.declined"])
    derived["kaylessa.outcome.refusal_repaired"] = [[clear], ["kaylessa.trickster.knife_picked_up"], ["kaylessa.committed"]]
    derived["kaylessa.trickster.late_committed"] = [
        g + ["kaylessa.outcome.refusal_repaired"] for g in derived["kaylessa.trickster.late_committed"]]

    scenes = {s["Id"]: s for s in payload["Scenes"]}
    # Discovery is itself the already-authored MEANT consequence, not just prose.
    for scene in payload["Scenes"]:
        if scene["Id"] in ("mielarah.deck.market", "mielarah.deck.market.arcade"):
            for node in scene["Nodes"]:
                if node["Id"] == "worked_out":
                    for choice in node["Choices"]:
                        if "mielarah.trickster.cost.meant" not in choice["Set"]:
                            choice["Set"].append("mielarah.trickster.cost.meant")
        # Kissing during the isolated test invalidates it. Keep the original
        # answer at its index for the ordinary folio, and append the in-test
        # variant with the existing TAMPERED consequence, never a clean result.
        if scene["Id"].startswith("nenio.folio.pulse"):
            node = next(n for n in scene["Nodes"] if n["Id"] == "result")
            original = node["Choices"][0]
            during_test = copy.deepcopy(original)
            original["Forbids"].append("nenio.trickster.test_running")
            during_test["Requires"].append("nenio.trickster.test_running")
            during_test["Set"].append("nenio.trickster.tampered")
            node["Choices"].append(during_test)

    # eng8-q8h begin: read actual late acceptance, preserving all existing coda guards.
    from storylines import kiana_followthrough
    kiana_followthrough.integrate_late_acceptance(payload)
    derived["arsinoe.trickster.partner"] = [["arsinoe.committed"], ["arsinoe.trickster.late_committed"]]
    coda = scenes["arsinoe.lastcall.page"]
    coda["Requires"] = ["arsinoe.trickster.partner" if flag == "arsinoe.committed" else flag for flag in coda["Requires"]]
    # An accepted spring appointment is remembered, never produced by the ending.
    coda["Nodes"][0].setdefault("Paragraphs", []).append({
        "Text": "{n}The spring after Threshold, Arsinoe kept the evening she had promised the Commander before the war ended. Her shop opened late the next morning.{/n}",
        "Requires": ["arsinoe.trickster.late_committed"], "Forbids": ["arsinoe.committed"]})
    # end eng8-q8h

    # Job 3's route-owned late graphs join the ordinary proof pass. Their local
    # choices carry no campaign yes; their new prose gets the same live guards.
    from storylines import endings_job3
    endings_job3.integrate(payload)

    # The generator only adds a gate when the current path does not prove it.
    model = verify.Model(copy.deepcopy(payload))
    proof = Proof(model)
    items = list(blocks(model))
    guarded_nodes = {}
    guarded_choices = {}

    def require(spec, key):
        if key not in spec.setdefault("Requires", []):
            spec["Requires"].append(key)

    for block in items:
        rel = model.rels.get(block.route) or {}
        reason = policy.reward(block, rel)
        mandatory = block.node["Id"] in CONTRACTS["mandatory_consumers"].get(block.scene["Id"], [])
        if (not reason and not mandatory) or block.scene["Owner"] == "AeonEpilogue":
            continue
        rule = CONTRACTS["refusal_control"].get(block.route)
        repair = bool(rule and block.slot.startswith("choice") and rule[1] in block.spec.get("Set", []))
        gate = eligibility(block.route, repaired_now=repair, woman=policy.outcome_woman(block))
        required = []
        # Model precedes any new per-block gate, but sees all shared definitions.
        if not proof.implies(block.context, lit(gate)):
            required.append(gate)
        new_act = reason and reason.startswith(("commitment ", "outcome ", "late commitment"))
        path_branch = policy.path_branch(block)
        if new_act and path_branch and not proof.implies(block.context, lit("trickster.now")):
            required.append("trickster.now")
        scene = scenes[block.scene["Id"]]
        # A guard just emitted on this scene also covers its unchanged pages.
        # Keep a consumer guard if any branch can mutate one of its inputs.
        # This avoids redundantly gating every epilogue paragraph after its
        # first page already acquired the identical live eligibility contract.
        required = [key for key in required if
                    dependencies(model, lit(key)).intersection(model.scene_sets[scene["Id"]])
                    or not proof.implies(scene_context(model, verify.norm_scene(copy.deepcopy(scene))), lit(key))]
        if not required:
            continue
        node = next((n for n in scene["Nodes"] if n["Id"] == block.node["Id"]), None)
        if block.slot.startswith("choice"):
            spec = node["Choices"][int(block.slot[7:-1])]
            for key in required:
                require(spec, key)
            guarded_choices.setdefault((scene["Id"], block.node["Id"]), set()).update(required)
        elif block.slot.startswith("paragraph"):
            spec = node["Paragraphs"][int(block.slot[10:-1])]
            for key in required:
                require(spec, key)
        elif block.node["Id"] == scene["Nodes"][0]["Id"]:
            for key in required:
                overrides = rel.get("UnavailableOverrides", {})
                direct = all((flag in model.authored or flag in model.native)
                             and back in model.authored and back not in model.composites
                             for flag, back in overrides.items())
                if key == block.route + ".outcome.route_open" and direct:
                    # Scene ForbidOverrides can express RouteOpen directly;
                    # preserve normal epilogue readers without a new latch.
                    for flag in [rel.get("ClosedFlag"), *rel.get("UnavailableFlags", [])]:
                        if flag and flag not in scene.setdefault("Forbids", []):
                            scene["Forbids"].append(flag)
                        returned = rel.get("UnavailableOverrides", {}).get(flag)
                        if returned:
                            scene.setdefault("ForbidOverrides", {})[flag] = returned
                else:
                    require(scene, key)
        elif block.slot == "text":
            guarded_nodes.setdefault((scene["Id"], block.node["Id"]), set()).update(required)
        else:
            for key in required:
                require(scene, key)

    for (sid, nid), keys in guarded_nodes.items():
        for node in scenes[sid]["Nodes"]:
            for choice in node["Choices"]:
                check = choice.get("Check") or {}
                if nid in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                    for key in sorted(keys):
                        require(choice, key)
                    guarded_choices.setdefault((sid, node["Id"]), set()).update(keys)
    # A lost gate must still allow the player to leave a page reached earlier.
    # Append only, abort without granting completion or changing old indices.
    for (sid, nid), keys in sorted(guarded_choices.items()):
        node = next(n for n in scenes[sid]["Nodes"] if n["Id"] == nid)
        for key in sorted(keys):
            _append_exit(node, key)

    normalize_lastcall(payload, eligibility)


def _append_exit(node, key):
    fallback = c("[Leave.]", forbids=(key,), abort=True)
    if any(_covers_exit(answer, key) for answer in node["Choices"]):
        # This generated position already exists in exported saves.
        # Retire the duplicate without shifting any later answer.
        fallback["Requires"].append(key)
    node["Choices"].append(fallback)


def _covers_exit(answer, missing_key):
    """An existing effect-free abort covers every history of this fallback."""
    if not answer.get("Abort"):
        return False
    if answer.get("Requires") or set(answer.get("Forbids", [])) - {missing_key}:
        return False
    return not any(value for field, value in answer.items()
                   if field not in {"Text", "Abort", "Requires", "Forbids"})


def normalize_lastcall(payload, eligibility):
    """E-Q7-07: actual paid stakes and authored late roads at every reader."""
    derived = payload["Derived"]
    for route in ("anevia", "nenio"):
        scene = next(s for s in payload["Scenes"] if s["Id"] == route + ".lastcall.page")
        scene["Requires"].remove(route + ".committed")
        scene.setdefault("RequiresAnyGroups", []).append([route + ".committed", route + ".trickster.late_committed"])
        scene["Requires"].append(eligibility(route))
    # NAME_GONE joins the native Enigma resolution with the stake, even when the
    # optional after_enigma discussion that sets name_filed was never played.
    old, actual = "nenio.trickster.cost.name_filed", "nenio.trickster.name_gone"
    for key in ("nenio.lastcall.callable",):
        derived[key] = [[actual if k == old else k for k in g] for g in derived[key]]
        derived[key] = [g + [eligibility("nenio")] for g in derived[key]]
    for scene in payload["Scenes"]:
        if scene["Id"] in ("nenio.lastcall.call", "nenio.lastcall.page"):
            scene["RequiresAnyGroups"] = [[actual if k == old else k for k in g] for g in scene.get("RequiresAnyGroups", [])]
            for node in scene["Nodes"]:
                for paragraph in node.get("Paragraphs", []):
                    paragraph["Requires"] = [actual if k == old else k for k in paragraph.get("Requires", [])]
    for book in payload.get("Books", {}).values():
        for entry in book.get("Entries", []):
            if entry["Id"] == "owed.nenio":
                entry["AnyGroups"] = [[actual if k == old else k for k in g] for g in entry["AnyGroups"]]
    for entry in payload["Relationships"]["lastcall"].get("JournalEntries", []):
        if entry["Id"] == "owed.nenio":
            entry["OpenWhen"] = [[actual if k == old else k for k in g] for g in entry["OpenWhen"]]
    # A built cairn is preparation; only the existing partner reader entitles a call.
    derived["wenduag.lastcall.callable"] = [g + ["wenduag.trickster.partner"] for g in derived["wenduag.lastcall.callable"]]
