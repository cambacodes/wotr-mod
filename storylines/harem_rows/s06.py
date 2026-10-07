"""S06 registration through the auto-discovered row seam."""
import copy


def register(payload, scenes, refs):
    from storylines import household_pair_minagho_chivarro as row
    payload["Scenes"].extend(copy.deepcopy(row.SCENES))
    payload.setdefault("Derived", {}).update(copy.deepcopy(row.DERIVED))
    payload.setdefault("DerivedForbids", {}).update(copy.deepcopy(row.DERIVED_FORBIDS))
