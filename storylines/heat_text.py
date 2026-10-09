"""Heat-pass helpers (HEAT, Directive 12): text-only edits of build-up nodes.

A heat layer extends the build-up node of an explicit slot so the scene's desire, situation and appetite reach the
START of the act. It never writes the act: the slot node (filled later by a separate model) and its exits stay as
they are. No scene, node or choice id, choice position, Next, Set, gate or check changes. Every target must resolve
and every replaced snippet must occur exactly once, or the build fails.
"""
from story_format import p


def _node(payload, scene_id, node_id):
    scenes = [s for s in payload["Scenes"] if s["Id"] == scene_id]
    if len(scenes) != 1:
        raise KeyError("heat layer: scene %s resolves to %d scenes" % (scene_id, len(scenes)))
    nodes = [x for x in scenes[0]["Nodes"] if x["Id"] == node_id]
    if len(nodes) != 1:
        raise KeyError("heat layer: node %s/%s resolves to %d nodes" % (scene_id, node_id, len(nodes)))
    return nodes[0]


def swap(payload, targets, old, new):
    """Replace one snippet (exactly once) in each target node's text."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node["Text"].count(old) != 1:
            raise ValueError("heat layer: snippet not found exactly once in %s/%s: %r" % (scene_id, node_id, old[:70]))
        node["Text"] = node["Text"].replace(old, new)


def extend(payload, targets, last, addition):
    """Keep the node text up to and including `last` (which must end the text) and append `addition`."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node["Text"].count(last) != 1 or not node["Text"].rstrip().endswith(last):
            raise ValueError("heat layer: %s/%s does not end with %r" % (scene_id, node_id, last[:70]))
        node["Text"] = node["Text"].rstrip() + "\n" + addition.strip()


def paragraph(payload, scene_id, node_id, text, requires=(), forbids=()):
    """Append one flag-gated paragraph after the node's existing paragraphs."""
    _node(payload, scene_id, node_id).setdefault("Paragraphs", []).append(p(text, requires=requires, forbids=forbids))
