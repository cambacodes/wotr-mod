"""J02: approved directional stages and first-final-failure publication.

No suffix-based failure inference, scene allocation, return, price or forgiveness.
See tools/route_packs/plans/j02-policy.json for the exhaustive E4 dispositions.
The last registrar consumes the assembled row terminals, including wrappers.
"""
import copy
import json
from pathlib import Path

from storylines.harem_rows import s03a, s03b, s10, s13, s21, s29, s30

POLICY = Path(__file__).resolve().parents[2] / "tools/route_packs/plans/j02-policy.json"
STAGES = ("rival", "respect", "friend", "lover")


def policy():
    return json.loads(POLICY.read_text(encoding="utf-8"))


def owner(key):
    """Canonical actual claimant, without borrowing either composite partner."""
    prefix, target = key.split(".harem.enmity.")
    if prefix == "minagho_chivarro":
        woman, target = target.split(".", 1)
        return prefix + ".harem.enmity." + woman + "_any"
    if prefix == "tirabade":
        woman, target = target.split(".", 1)
        return "household.controller." + woman + ".enmity_any"
    if prefix == "anevia":
        return "household.controller.anevia.enmity_any"
    return prefix + ".harem.enmity_any"


def _receipt(key):
    return key.replace(".harem.enmity.", ".harem.reconciled.")


def _stages(payload, scenes):
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    groups = {}
    # S03a starts as friendship; the only warmer group is the reviewed mutual
    # deed/cost contract. A later fall selects S03b without deleting that history.
    for a, b in (s03a.PAIR, s03a.PAIR[::-1]):
        groups[(a, b, "friend")] = [[s03a.p("ready"), "arueshalae.redeemed"]]
    groups.update(copy.deepcopy(s03a.STAGE_INPUTS))
    for (a, b, stage), witnesses in s03b.STAGE_INPUTS.items():
        groups.setdefault((a, b, stage), []).extend(
            group + ["arueshalae.corrupted"] for group in witnesses)
    # S13's approved refusal obstacle and exact directional deeds, including
    # the currently retired optional ladder. Inert scenes stay inert.
    for a, b in (s13.PAIR, s13.PAIR[::-1]):
        for stage in ("friend", "lover"):
            groups[(a, b, stage)] = copy.deepcopy(derived[s13.P + a + "." + stage])
    # Friendship-only rows supply their specific deeds and costs. One witness
    # or merely attending cannot stand in for the whole conjunction.
    for row, pair, receipts in (
        (s10, ("seelah", "nenio"), s10.ANSWERED[1:]),
        (s21, s21.PAIR, s21.KEPT[1:]),
        (s29, s29.PAIR, s29.HELPED[1:]),
        (s30, ("eliandra", "targona"), s30.ANSWERED[1:]),
    ):
        for a, b in (pair, pair[::-1]):
            groups[(a, b, "friend")] = [list(receipts)]
        # The deed cannot require its own resulting stage. All unrelated gates
        # (page, stance, Table, actual channels, costs and losses) remain intact.
        own = {a + ".harem.attitude." + b + ".friend" for a, b in (pair, pair[::-1])}
        for body in scenes:
            if body["Id"].startswith(row.PREFIX if hasattr(row, "PREFIX") else row.P):
                body["Requires"] = [flag for flag in body["Requires"] if flag not in own]
    # S20 reads the existing interactive account, never a new meeting, charge
    # or an offer made on Jannah's behalf.
    for a, b in (("seelah", "jannah"), ("jannah", "seelah")):
        groups[(a, b, "friend")] = [["jannah.circle.seelah", "jannah.circle.seelah.herself"]]
    for (a, b, stage), witnesses in groups.items():
        key = a + ".harem.attitude." + b + "." + stage
        derived[key] = witnesses
        blocked = "household.controller." + a + "." + b + ".blocked"
        reverse = "household.controller." + b + "." + a + ".blocked"
        for first, second, guard in ((a, b, blocked), (b, a, reverse)):
            enmity = first + ".harem.enmity." + second
            derived[guard] = [[enmity]]
            forbids[guard] = [_receipt(enmity)]
        forbids[key] = [blocked, reverse]
        if "arueshalae" in (a, b) and (a, b, stage) not in s03b.STAGE_INPUTS:
            forbids[key].append("arueshalae.corrupted")
        forbids[key].extend(a + ".harem.attitude." + b + "." + higher
                            for higher in STAGES[STAGES.index(stage) + 1:]
                            if (a, b, higher) in groups)


def _publish(payload, scenes, rules):
    """Split only exact approved terminal choices; saved index 0 stays index 0.

    Choice-level branching already exists in Rules. No deferred observer may
    choose an owner from module order, timestamps or an unrelated .failed.
    """
    locks = json.loads((POLICY.parents[1] / "voice_locks.json").read_text(encoding="utf-8"))["locked"]
    for rule in rules:
        enmity = rule["enmity"]
        aggregate = owner(enmity)
        for body in scenes:
            if not body["Id"].startswith(rule["prefix"]):
                continue
            for node in body["Nodes"]:
                for index, choice in enumerate(list(node["Choices"])):
                    if (choice.get("Id") or "").startswith("j02.history."):
                        continue
                    if not set(rule["terminal"]) <= set(choice["Set"]) or choice.get("Abort"):
                        continue
                    if enmity in choice["Set"]:
                        continue
                    if body["Id"] in locks:
                        raise ValueError("J02 terminal needs voice-owner attachment: " + body["Id"])
                    if choice.get("Check"):
                        raise ValueError("J02 final incident cannot commit before a check: " + body["Id"])
                    history = copy.deepcopy(choice)
                    history.setdefault("Requires", []).append(aggregate)
                    history["Id"] = "j02.history." + str(index)
                    # Reuse the existing terminal label; no newly voiced line.
                    choice.setdefault("Forbids", []).append(aggregate)
                    choice["Set"].extend([enmity, rule["stance"]])
                    node["Choices"].append(history)


def register(payload, scenes, refs):
    data = policy()
    pending = payload.setdefault("PendingHooks", [])
    enmities = [hook for hook in data["hooks"] if ".harem.enmity." in hook]
    enmities.extend(rule["enmity"] for rule in data["failures"])
    for hook in [*data["hooks"], *enmities, *map(_receipt, enmities)]:
        if hook not in pending:
            pending.append(hook)
    # Historical first targets survive their matching reconciliation.
    aggregates = {}
    for hook in enmities:
        if hook not in data["aliases"]:
            aggregates.setdefault(owner(hook), []).append([hook])
    derived = payload.setdefault("Derived", {})
    for key, groups in aggregates.items():
        derived[key] = list({tuple(group): group for group in [
            *derived.get(key, []), *groups]}.values())
        receipt_any = key.replace(".enmity.", ".reconciled.").replace(".enmity_any", ".reconciled_any")
        derived[receipt_any] = [[_receipt(group[0])] for group in groups]
    _stages(payload, scenes)
    # Ruling 32: the source contract names this breach but the current emitter
    # omits it from the betrayal Set. Bind only the actual irreversible kill,
    # never a later failure, stage or prisoner absence.
    prefix = "household.pair.seelah_wenduag."
    for body in scenes:
        if body["Id"] != prefix + "debt_repayment":
            continue
        for node in body["Nodes"]:
            for choice in node["Choices"]:
                if {prefix + "debt.betrayed", prefix + "captive.rusk_dead"} <= set(choice["Set"]):
                    if prefix + "boundary.breached" not in choice["Set"]:
                        choice["Set"].append(prefix + "boundary.breached")
    _publish(payload, scenes, data["failures"])
    # The only supported receipt among the listed 59: S36's specific paid
    # replacement after this old target. No old target means no reconciliation.
    receipt = "hepzamirah.harem.reconciled.melazmera"
    payload["Derived"][receipt] = [[
        "hepzamirah.harem.enmity.melazmera",
        "household.pair.melazmera_hepzamirah.replacement.held",
        "household.pair.melazmera_hepzamirah.cost.melazmera_hunt_yielded",
        "household.pair.melazmera_hepzamirah.cost.hepzamirah_guards_detoured",
        "household.pair.melazmera_hepzamirah.cost.commander_watch_kept",
        "household.pair.melazmera_hepzamirah.cost.replacement_carried",
    ]]
