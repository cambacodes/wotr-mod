"""S34 reservation: the reviewed sheet forbids activation without its job contract.

See tools/route_packs/harem/s34-blockers.md. No deed, stage, attendance, or
affection is inferred from the native rank/punishment voice anchors.
"""


def register(payload, scenes, refs):
    """Leave the existing reserved S34 schedule unchanged pending owner inputs."""
    return None
