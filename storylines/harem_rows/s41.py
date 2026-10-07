"""S41 registration through the auto-discovered row seam."""
import copy


def register(payload, scenes, refs):
    from storylines import household_pair_iomedae_areelu as row
    payload["Scenes"].extend(copy.deepcopy(row.SCENES))
