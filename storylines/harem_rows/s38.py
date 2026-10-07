"""S38: integrate against the assembled household payload."""


def register(payload, scenes, refs):
    from storylines import household_pair_delamere_minagho as row
    row.integrate(payload)
