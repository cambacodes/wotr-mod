"""S36: integrate against the assembled household payload."""


def register(payload, scenes, refs):
    from storylines import household_pair_melazmera_hepzamirah as row
    row.integrate(payload)
