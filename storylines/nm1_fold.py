"""NM1 (2026-10-01): fold a later rest-delivered scene into the delivery before it, save-safely.

Used to keep a route's rest deliveries inside its allocation without cutting content. The guest scene's nodes are
copied into the host after a short narrated wait (node ids prefixed with the guest's key), and the host's terminal
choices continue into them. The copies keep the guest's flags, including the `_done`/progress flag the guest's own
standalone scene forbids, so the standalone scene never arrives a second time. Nothing is renamed or removed: every
scene, node and choice id and every choice index is kept, and a save that already stands between the two scenes still
receives the guest standalone.
"""
import copy

from story_format import c, n


def fold(host, guest, gate, wait, key, *, every_terminal=False, portrait=""):
    """Fold `guest` into `host`.

    gate: the flag the guest's standalone scene requires from the host (checked).
    every_terminal: hook every non-abort terminal choice of the host (the caller's tests prove each one holds `gate`);
    otherwise only the terminal choices that set `gate` themselves are hooked.
    """
    if gate not in guest["Requires"]:
        raise ValueError("nm1_fold: %s no longer waits on %s" % (guest["Id"], gate))
    ids = {node["Id"] for node in guest["Nodes"]}

    def moved(node_id):
        return key + "." + node_id if node_id in ids else node_id

    copies = []
    for node in guest["Nodes"]:
        clone = copy.deepcopy(node)
        clone["Id"] = moved(node["Id"])
        for choice in clone["Choices"]:
            if choice.get("Next"):
                choice["Next"] = moved(choice["Next"])
            if choice.get("Check"):
                for side in ("Success", "Failure"):
                    if choice["Check"].get(side):
                        choice["Check"][side] = moved(choice["Check"][side])
        copies.append(clone)
    bridge = n(key + ".arrives", "Narrator", wait, c("Continue", moved(guest["Nodes"][0]["Id"])), portrait=portrait)
    taken = {node["Id"] for node in host["Nodes"]}
    if taken & ({x["Id"] for x in copies} | {bridge["Id"]}):
        raise ValueError("nm1_fold: folded node ids collide in " + host["Id"])
    hooks = 0
    for node in host["Nodes"]:
        for choice in node["Choices"]:
            if choice.get("Next") or choice.get("Abort") or choice.get("Check"):
                continue
            if every_terminal or gate in choice.get("Set", []):
                choice["Next"] = bridge["Id"]
                hooks += 1
    if not hooks:
        raise ValueError("nm1_fold: no terminal choice of %s leads on to %s" % (host["Id"], guest["Id"]))
    host["Nodes"].append(bridge)
    host["Nodes"].extend(copies)
