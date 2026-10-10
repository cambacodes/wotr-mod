"""Residual Areelu reader blocked by the cross-route engine's text classification.

All replacements and other readers live in their builders. This historical
Iomedae paragraph must stay after the engine to preserve its original flags.
"""
from story_format import p


def integrate(payload):
    host = next(scene for scene in payload["Scenes"] if scene["Id"] == "areelu.lastcall.page")
    node = next(node for node in host["Nodes"] if node["Id"] == "page")
    node.setdefault("Paragraphs", []).append(p('''{n}The Commander once wrote an apology in my name and read it to Iomedae. It is the only forgery of me I have ever found offensive. It was badly argued.{/n}''',
                requires=('household.pair.iomedae_areelu.cost.commander_false_apology',),
                forbids=('household.pair.iomedae_areelu.cost.areelu_records_opened',)))
