"""NM1 (2026-10-01): Delamere's courtship at a rest, inside the shared load.

Coordinator ruling (allocation exception, recorded in her spec and 06 row): her visits were manual reads from the mod
menu (Q6 r2), which a beta cannot rely on. They now arrive at a rest like every other route's. To keep her deliveries
down, the spine is folded (nm1_fold) into three deliveries: the count with the first meat, the feasting table with the white
stag, and Red with her woods. Every folded terminal holds the next visit's prerequisite (the
route's tests walk them). Ids, nodes and choice indices are kept; a save between two visits still gets the next one.
"""
from storylines.nm1_fold import fold

P = "delamere.trickster."

FOLDS = (
    # (host, guest, the guest's prerequisite, the narrated wait). Pairs, not triples: a delivery stays a readable length.
    ("woken.count", "woken.first_meat", P + "counted",
     '''{n}She does not come back that night, or the next. On the third night you stop listening for her, which is when she comes.{/n}'''),
    ("woken.count_late", "woken.first_meat", P + "counted",
     '''{n}She does not come back that night, or the next. On the third night you stop listening for her, which is when she comes.{/n}'''),
    ("woken.feasting_table", "woken.white_stag", P + "feasting_table",
     '''{n}For two days there is no word from the hills. On the third evening you see a fire on the ridge above the city, and you know whose it is.{/n}'''),
    ("woken.red_blood", "woken.my_woods", P + "red_blood",
     '''{n}She is gone before the bells. You do not see her for two days, and then, looking for something else, you do.{/n}'''),
)


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for host, guest, gate, wait in FOLDS:
        fold(scenes[P + host], scenes[P + guest], gate, wait, guest.split(".")[-1], every_terminal=True, portrait="Delamere")
