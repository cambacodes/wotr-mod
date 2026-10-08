"""Late text layer for villain-route-melazmera (cloud voice owner).

Runs after s36 (household_pair_melazmera_hepzamirah) has attached its Last Call
readers to melazmera.lastcall.page and after the contract controller, so the
route's text and her Last Call page are rewritten once, at the end. Text and
appended flag-gated paragraphs only; see storylines/melazmera_cloud.py.
The shared household.pair.melazmera_hepzamirah.* scenes belong to the higher
villain row (hepzamirah); they are not edited here.
"""


def register(payload, scenes, refs):
    from storylines import melazmera_cloud
    melazmera_cloud.integrate(payload)
