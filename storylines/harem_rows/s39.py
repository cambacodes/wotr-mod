"""S39 registration through the auto-discovered row seam."""
from functools import wraps


def register(payload, scenes, refs):
    from storylines import household, household_pair_galfrey_nocticula as row
    if getattr(household.integrate, "_s39", False):
        return
    original = household.integrate

    @wraps(original)
    def integrate(assembled):
        original(assembled)
        row.integrate(assembled)
        assembled.setdefault("ForesightConsumers", {}).update(
            {s["Id"]: "foresight.page_taken" for s in assembled["Scenes"]
             if s["Id"].startswith(row.PREFIX)})

    integrate._s39 = True
    household.integrate = integrate
