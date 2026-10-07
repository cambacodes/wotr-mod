"""S40 registration through the auto-discovered row seam."""

def register(payload, scenes, refs):
    from storylines import household_pair_iomedae_nocticula as row
    registered = row._registered
    try:
        # Each payload owns its Ledger and paragraphs, even in one interpreter.
        row._registered = False
        row.prepare(payload)
    finally:
        row._registered = registered
