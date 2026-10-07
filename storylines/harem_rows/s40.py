"""S40 registration through the auto-discovered row seam."""

def register(payload, scenes, refs):
    from storylines import household_pair_iomedae_nocticula as row
    row.prepare(payload)
