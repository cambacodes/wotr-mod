"""S38 registration through the auto-discovered row seam."""
from functools import wraps


def register(payload, scenes, refs):
    from storylines import household, household_pair_delamere_minagho as row
    if getattr(household.integrate, "_s38", False):
        return
    original = household.integrate

    @wraps(original)
    def integrate(assembled):
        original(assembled)
        row.integrate(assembled)

    integrate._s38 = True
    household.integrate = integrate
