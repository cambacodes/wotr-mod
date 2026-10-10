"""Heat-pass helpers (HEAT, Directive 12): text-only edits of build-up nodes.

A heat layer extends the build-up node of an explicit slot so the scene's desire, situation and appetite reach the
START of the act. It never writes the act: the slot node (filled later by a separate model) and its exits stay as
they are. No scene, node or choice id, choice position, Next, Set, gate or check changes. Every target must resolve
and every replaced snippet must occur exactly once, or the build fails.
"""
from story_format import p
from authoring.generation_errors import record


def _node(payload, scene_id, node_id):
    scenes = [s for s in payload["Scenes"] if s["Id"] == scene_id]
    if len(scenes) != 1:
        record("heat.scene_resolution", scene=scene_id, node=node_id, detail=str(len(scenes)))
        return None
    nodes = [x for x in scenes[0]["Nodes"] if x["Id"] == node_id]
    if len(nodes) != 1:
        record("heat.node_resolution", scene=scene_id, node=node_id, detail=str(len(nodes)))
        return None
    return nodes[0]


def swap(payload, targets, old, new):
    """Replace one snippet (exactly once) in each target node's text."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node is None:
            continue
        if node["Text"].count(old) != 1:
            record("heat.swap_snippet", scene=scene_id, node=node_id, detail=old[:70])
            continue
        node["Text"] = node["Text"].replace(old, new)


def extend(payload, targets, last, addition):
    """Keep the node text up to and including `last` (which must end the text) and append `addition`."""
    for scene_id, node_id in targets:
        node = _node(payload, scene_id, node_id)
        if node is None:
            continue
        if node["Text"].count(last) != 1 or not node["Text"].rstrip().endswith(last):
            record("heat.extend_tail", scene=scene_id, node=node_id, detail=last[:70])
            continue
        node["Text"] = node["Text"].rstrip() + "\n" + addition.strip()


def paragraph(payload, scene_id, node_id, text, requires=(), forbids=()):
    """Append one flag-gated paragraph after the node's existing paragraphs."""
    node = _node(payload, scene_id, node_id)
    if node is not None:
        node.setdefault("Paragraphs", []).append(p(text, requires=requires, forbids=forbids))
