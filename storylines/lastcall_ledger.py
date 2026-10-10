"""The Trickster's Ledger as data (08-TRICKSTER-HOUSEHOLD.md §2.1), shaped to the RRT book contract
(09-RRT-BOOK-UI.md §3-§4: payload["Books"]["trickster.ledger"], glossary links {g|RRT_Key}words{/g}).

Two consumers:
- journal_entries(): the E15 journal objectives of the `lastcall` quest (built now, and the native entry point). Plain text:
  journal descriptions carry no glossary links.
- book(): the paged book for the shared RRT book component (claude/eng-ui). It is NOT registered on this branch, because the
  Books engine arrives with that merge. After both merge, add one line to lastcall.integrate:
  `payload.setdefault("Books", {})["trickster.ledger"] = lastcall_ledger.book()`.

Sections follow 09 §4. Debts is built. Guest List, Seating Notes and Secrets are declared but stay empty until the household
pass. Their ids are reserved in RESERVED, and a section with nothing visible is hidden on the contents page.
"""

from storylines import lastcall_partners as partners

BOOK_ID = "trickster.ledger"
SECTIONS = ["Debts", "Guest List", "Seating Notes", "Secrets"]
ACTIVE = "lastcall.active"

# Reserved for the household pass (05 §2.2, 08 §3, the coordinator's Secrets rule). Nothing sets these flags yet.
RESERVED = {
    "Guest List": "guest.<rel>: visible on <rel>.harem.eligible; RRT_Tolerated on tolerated lines",
    "Seating Notes": "seating.<rel_a>.<rel_b>: a friction from the registry; settled/failed in Lines",
    "Secrets": "secret.<k>: reads trickster.secret.<k>; witnesses trickster.secret.<k>.witness.<rel>; RRT_SecretRisk in text",
}

# Portrait keys (CustomNpcPortraits Scenes/<key>.png); "" falls back to the book's picture. A debt shows its holder partner.
HOLDER_PORTRAIT = {"socoth": "Anevia", "baphomet": "Minagho", "nocticula": "Nocticula", "ramisa": "Nurah", "herrax": "Chivarro",
                   "abadar": "Arsinoe", "sunhammer": "Kiana", "mutasafen": "Hepzamirah", "wintersun": "Soana",
                   "nocticula_summons": "Arueshalae", "whispering_way": "Elyanka"}
PARTNER_PORTRAIT = {"irabeth": "Irabeth", "jerribeth": "Jerribeth", "konomi": "Konomi", "vellexia": "Vellexia", "aranka": "Aranka",
                    "gesmerha": "Gesmerha", "seelah": "Seelah", "dorgelinda": "Dorgelinda", "eritrice": "Eritrice",
                    "areelu": "Areelu", "chadali": "Chadali", "camellia": "Camellia", "arueshalae": "Arueshalae",
                    "shamira": "Shamira", "iomedae": "Iomedae"}

OPENING = ("{n}The accounts of the Commander of the Fifth Crusade, kept by the Commander, since nobody else would believe "
           "them. Every {g|RRT_Debt}debt{/g} below is a thread from the world into my chest, and a creditor does not let a "
           "debtor die unpaid. Settle them before the last joke, or let them settle me.{/n}")


def _line(text, requires=(), forbids=(), any_groups=()):
    return dict(Text=text, Requires=list(requires), Forbids=list(forbids), AnyGroups=[list(g) for g in any_groups])


def _settlement_line(receipts):
    if not receipts:
        return _line("{n}No payment or release is recorded here. The call alone settles nothing.{/n}", requires=[ACTIVE])
    if len(receipts) == 1:
        return _line("{n}A payment or release is recorded. Continuing terms remain on their own account.{/n}", requires=receipts[0])
    # Multiple alternatives here are independent single receipts.
    return _line("{n}A payment or release is recorded. Continuing terms remain on their own account.{/n}",
                 any_groups=[[g[0] for g in receipts]])


def _debt_entries():
    out = []
    for debt in partners.DEBTS:
        holders = sorted({k for g in debt["groups"] for k in g})
        lines = [_line("{n}Called in at the rift.{/n}", any_groups=[debt["called_by"]])]
        if debt.get("outlived"):
            lines.append(_line("{n}Outlived. There is nobody left to collect it.{/n}", any_groups=[debt["outlived"]]))
        receipts = partners.settlements(debt)
        lines.append(_settlement_line(receipts))
        if debt["key"] == "wintersun":
            lines.extend([
                _line("{n}The blood was given at Wintersun. Calling the account does not demand a second portion.{/n}", requires=[partners.S + "cost.blood_given"]),
                _line("{n}The guardian paid for the return. The strand still tied to my life remains its own obligation.{/n}", requires=[partners.S + "cost.guardian_paid", partners.S + "cost.knot_bearer"]),
            ])
        out.append(dict(Id="debt." + debt["key"], Section="Debts", Portrait=HOLDER_PORTRAIT[debt["key"]],
                        Title=debt["ledger_title"], Text="{n}" + debt["ledger_text"] + "{/n}", Lines=lines,
                        Requires=[], Forbids=[], AnyGroups=[holders], Tooltip="RRT_Debt"))
    for part in partners.PARTNERS:
        if not part.get("ledger_title"):
            continue
        deal = sorted({k for g in part["deal"] for k in g})
        out.append(dict(Id="owed." + part["key"], Section="Debts", Portrait=PARTNER_PORTRAIT.get(part["key"], ""),
                        Title=part["ledger_title"], Text="{n}" + part["ledger_text"] + "{/n}",
                        Lines=([_line("{n}Called in at the rift.{/n}", requires=[part["rel"] + ".lastcall.called"])] if part["call"] else [])
                              + [_settlement_line(partners.settlements(part))],
                        Requires=[], Forbids=[], AnyGroups=[deal], Tooltip="RRT_Debt"))
        if part["rel"] == "horzalah":
            out[-1]["Lines"].extend([
                _line("{n}Her report from the Guild placed the trophy above the old hall in Alushinyrra. Its masters accepted her story.{/n}",
                      requires=[partners.HZ + "cost.ear", partners.HZ + "primed", partners.HZ + "returned"]),
                _line("{n}The ear is paid. No report has come from the Guild; I do not know where she keeps it or whether her masters believed her.{/n}",
                      requires=[partners.HZ + "cost.ear"], forbids=[partners.HZ + "returned"]),
            ])
    return out


# Early threads (15b-EARLY-THREADS.md): each route registers its own book entry here at import time (the reader that
# holds whether or not the player ever reaches the route's payoff). Appended after the debts, in registration order.
EARLY = []


def early(entry):
    """Register one early-thread book entry (the BookEntry contract: Id, Section, Portrait, Title, Text, Lines, Requires,
    Forbids, AnyGroups, Tooltip)."""
    if any(e["Id"] == entry["Id"] for e in EARLY):
        raise ValueError("Duplicate early Ledger entry: " + entry["Id"])
    if entry["Section"] not in SECTIONS:
        raise ValueError("Unknown Ledger section: " + entry["Section"])
    EARLY.append(entry)


# Route-owned Ledger entries (Q11): a route appends dict(Id, Section, Portrait, Title, Text, Lines, Requires, Forbids,
# AnyGroups, Tooltip) at import; book() shows them after the debts.
EXTRA_ENTRIES = []


def book():
    """payload["Books"]["trickster.ledger"] per 09-RRT-BOOK-UI.md §3."""
    return dict(Title="The Trickster's Ledger", Opening=OPENING, Portrait="", Sections=list(SECTIONS),
                Entries=_debt_entries() + [dict(e) for e in EARLY] + [dict(e) for e in EXTRA_ENTRIES])


def journal_entries():
    """The E15 journal objectives, one per Debts entry. Each is given when the debt is made, and completed when it is
    paid or released by a specific receipt, or its creditor is outlived."""
    out = []
    for debt in partners.DEBTS:
        out.append(dict(Id="debt." + debt["key"], Title=debt["ledger_title"], Description=debt["ledger_text"],
                        OpenWhen=[list(g) for g in debt["groups"]],
                        SettledWhen=partners.settlements(debt) + [[k] for k in debt.get("outlived", ())]))
    for part in partners.PARTNERS:
        if part.get("ledger_title"):
            out.append(dict(Id="owed." + part["key"], Title=part["ledger_title"], Description=part["ledger_text"],
                            OpenWhen=[list(g) for g in part["deal"]],
                            SettledWhen=partners.settlements(part)))
    return out


# fix15: the wound is earned at restitution; a care routine and oath are not.
_fix15_debt_entries = _debt_entries
def _debt_entries():
    out = _fix15_debt_entries()
    for entry in out:
        if entry["Id"] != "owed.terendelev":
            continue
        old = "{n}" + partners.TE_LEDGER_OATH + "{/n}"
        entry["Text"] = "{n}I opened my wound over her bones and it has never closed. Whatever that bought, I owe it: a thread of my blood runs in her now, and I do not get to call the account settled.{/n}"
        entry["Lines"].extend([
            _line(old, requires=[partners.TE + "dressing", "terendelev.lastcall.oath_recorded"]),
            _line("{n}She has laid linen on the wound with her own hands. No sworn watch is written on any page I keep, and I will not write one for her.{/n}", requires=[partners.TE + "dressing"], forbids=["terendelev.lastcall.oath_recorded"]),
        ])
    return out
