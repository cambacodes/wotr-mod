"""S36 registration through the auto-discovered row seam."""
from functools import wraps


def register(payload, scenes, refs):
    from storylines import household, household_pair_melazmera_hepzamirah as row
    if getattr(household.integrate, "_s36", False):
        return
    original = household.integrate

    @wraps(original)
    def integrate(assembled):
        original(assembled)
        row.integrate(assembled)

    integrate._s36 = True
    household.integrate = integrate
