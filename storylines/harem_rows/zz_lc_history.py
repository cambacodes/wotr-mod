"""Late paragraphs on shared Last Call pages go in a zz_ row so earlier positions never move."""

from story_format import p
from storylines.lastcall_partners import PARTNERS, page_p

D = "dorgelinda.trickster."
L = "dorgelinda.ledger."


def register(payload, scenes, refs):
    host = next((s for s in scenes if s["Id"] == "dorgelinda.lastcall.page"), None)
    if host is None or host.get("Owner") != "Epilogue":
        return
    host["Nodes"][0].setdefault("Paragraphs", []).extend((
        page_p("[PROSE PENDING: Dorgelinda - Last Call settled account]",
               requires=(D + "cost.told_all",)),
        page_p("[PROSE PENDING: Dorgelinda - Last Call current seal quarrel]",
               any_groups=[[L + "cold_unmended", L + "quarrel_unmended"]]),
        page_p("[PROSE PENDING: Dorgelinda - Last Call called after completed disclosure]",
               requires=("dorgelinda.lastcall.called", D + "cost.told_all")),
        # Retain the authored opener held by lc-history-01 as an unsettled
        # paragraph; no new prose, and no displacement of S52's slots.
        p(next(part["opener"] for part in PARTNERS if part["key"] == "dorgelinda"),
          forbids=(D + "cost.told_all",)),
    ))
