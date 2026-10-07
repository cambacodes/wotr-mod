"""S07 registration through the auto-discovered row seam."""
import copy


def register(payload, scenes, refs):
    from storylines import household_pair_anevia_irabeth as row
    payload["Scenes"].extend(copy.deepcopy(row.SCENES))
