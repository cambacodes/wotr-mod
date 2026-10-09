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
        page_p("{n}The Commander's account was entered as paid in full. Dorgelinda filed the confession with its receipts and let no clerk reopen the line. She went on checking every requisition the Commander sent, and found nothing in them to hold against the old debt.{/n}",
               requires=(D + "cost.told_all",)),
        page_p("{n}The quarrel over the seal stood unmended. Dorgelinda filled each of the Commander's requisitions and signed it at her desk with a clerk in the room. Nothing else passed between them, and she did not ask for more.{/n}",
               any_groups=[[L + "cold_unmended", L + "quarrel_unmended"]]),
        page_p("{n}The call reached Drezen after the account was already closed. She had nothing left to ask. She read the dispatch once, entered the date beside the paid line, and went back to the stores.{/n}",
               requires=("dorgelinda.lastcall.called", D + "cost.told_all")),
        # Retain the authored opener held by lc-history-01 as an unsettled
        # paragraph; no new prose, and no displacement of S52's slots.
        p(next(part["opener"] for part in PARTNERS if part["key"] == "dorgelinda"),
          forbids=(D + "cost.told_all",)),
    ))
