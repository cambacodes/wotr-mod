"""S39: integrate against the assembled household payload."""


def register(payload, scenes, refs):
    from storylines import household_pair_galfrey_nocticula as row
    row.integrate(payload)
