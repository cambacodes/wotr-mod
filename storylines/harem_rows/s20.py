"""S20: historical reader reuse, as specified by Group D fields 3–7.

AUTHORED RRT Ledger wording; no new meeting, circle outcome, attitude,
attendance, intimacy, completion or allowance charge. The route's account
already stages Jannah's decision. Records do not imply current living speakers.
"""
from copy import deepcopy


ACCOUNT = "jannah.circle.seelah"
OUTCOMES = tuple(ACCOUNT + suffix for suffix in (".herself", ".told_for_her", ".kept"))
ENTRY_ID = "seating.seelah.jannah"


def _entry():
    return dict(
        Id=ENTRY_ID, Section="Seating Notes", Portrait="Jannah",
        Title="Seelah and Jannah",
        Text="{n}Houndheart is Jannah's to answer for. Their circle has its own result.{/n}",
        Requires=["trickster.now", "foresight.page_taken", "household.table.kept", ACCOUNT],
        Forbids=[], AnyGroups=[list(OUTCOMES)], Tooltip="RRT_SeatingNotes",
        Lines=[
            dict(Text="{n}Jannah went to Seelah herself. She came back with a handprint on her cheek and a grin. Seelah made her tell the whole tale.{/n}",
                 Requires=[OUTCOMES[0]], Forbids=[], AnyGroups=[]),
            dict(Text="{n}I offered to tell Seelah what happened. Jannah asked me to give the facts and leave Seelah to judge them. That offer does not tell me whether they have spoken.{/n}",
                 Requires=[OUTCOMES[1]], Forbids=[], AnyGroups=[]),
            dict(Text="{n}We left Seelah out of it for the time being. Jannah turned the little cart on her tankard to the wall. We postponed her account.{/n}",
                 Requires=[OUTCOMES[2]], Forbids=[], AnyGroups=[]),
            dict(Text="{n}Jannah called for a public rematch. Calling for it did not settle the bout.{/n}",
                 Requires=["jannah.trickster.challenge"], Forbids=[], AnyGroups=[]),
            dict(Text="{n}At the muster I laid down my blade and yielded Jannah's circle before the salute. She called the yield aloud, then lay down beside me.{/n}",
                 Requires=["jannah.circle.yielded_the_circle", "jannah.circle.yielding_the_circle"], Forbids=[], AnyGroups=[]),
        ],
    )


def register(payload, scenes, refs):
    """Append only S20's historical entry after the shared Ledger is built.

    Deliberately leave scenes, refs, shared caps and every relationship alone.
    Repeat assembly is harmless; an incompatible prior registration is an error.
    """
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is None:
        raise ValueError("S20 registration requires the assembled Trickster Ledger")
    entry = _entry()
    existing = [item for item in ledger["Entries"] if item["Id"] == ENTRY_ID]
    if existing:
        if existing != [entry]:
            raise ValueError("Conflicting S20 Seating Notes registration")
        return
    ledger["Entries"].append(deepcopy(entry))
