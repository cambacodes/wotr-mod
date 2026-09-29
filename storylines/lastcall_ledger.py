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
                   "nocticula_summons": "Arueshalae"}
PARTNER_PORTRAIT = {"irabeth": "Irabeth", "jerribeth": "Jerribeth", "konomi": "Konomi", "vellexia": "Vellexia", "aranka": "Aranka",
                    "gesmerha": "Gesmerha", "seelah": "Seelah", "dorgelinda": "Dorgelinda", "eritrice": "Eritrice",
                    "areelu": "Areelu", "chadali": "Chadali", "camellia": "Camellia", "arueshalae": "Arueshalae",
                    "shamira": "Shamira"}

OPENING = ("{n}The accounts of the Commander of the Fifth Crusade, kept by the Commander, since nobody else would believe "
           "them. Every {g|RRT_Debt}debt{/g} below is a thread from the world into my chest, and a creditor does not let a "
           "debtor die unpaid. Settle them before the last joke, or let them settle me.{/n}")


def _line(text, requires=(), forbids=(), any_groups=()):
    return dict(Text=text, Requires=list(requires), Forbids=list(forbids), AnyGroups=[list(g) for g in any_groups])


def _debt_entries():
    out = []
    for debt in partners.DEBTS:
        holders = sorted({k for g in debt["groups"] for k in g})
        lines = [_line("{n}Called in at the rift.{/n}", any_groups=[debt["called_by"]])]
        if debt.get("outlived"):
            lines.append(_line("{n}Outlived. There is nobody left to collect it.{/n}", any_groups=[debt["outlived"]]))
        lines.append(_line("{n}Settled, one way or another. The book stays open anyway.{/n}", requires=[ACTIVE]))
        out.append(dict(Id="debt." + debt["key"], Section="Debts", Portrait=HOLDER_PORTRAIT[debt["key"]],
                        Title=debt["ledger_title"], Text="{n}" + debt["ledger_text"] + "{/n}", Lines=lines,
                        Requires=[], Forbids=[], AnyGroups=[holders], Tooltip="RRT_Debt"))
    for part in partners.PARTNERS:
        if not part.get("ledger_title"):
            continue
        deal = sorted({k for g in part["deal"] for k in g})
        out.append(dict(Id="owed." + part["key"], Section="Debts", Portrait=PARTNER_PORTRAIT.get(part["key"], ""),
                        Title=part["ledger_title"], Text="{n}" + part["ledger_text"] + "{/n}",
                        Lines=[_line("{n}Called in at the rift.{/n}", requires=[part["rel"] + ".lastcall.called"]),
                               _line("{n}Settled, one way or another.{/n}", requires=[ACTIVE])],
                        Requires=[], Forbids=[], AnyGroups=[deal], Tooltip="RRT_Debt"))
    return out


def book():
    """payload["Books"]["trickster.ledger"] per 09-RRT-BOOK-UI.md §3."""
    return dict(Title="The Trickster's Ledger", Opening=OPENING, Portrait="", Sections=list(SECTIONS), Entries=_debt_entries())


def journal_entries():
    """The E15 journal objectives, one per Debts entry. Each is given when the debt is made, and completed when it is called
    in, outlived, or the ending plays."""
    out = []
    for debt in partners.DEBTS:
        out.append(dict(Id="debt." + debt["key"], Title=debt["ledger_title"], Description=debt["ledger_text"],
                        OpenWhen=[list(g) for g in debt["groups"]],
                        SettledWhen=[[k] for k in debt["called_by"]] + [[k] for k in debt.get("outlived", ())] + [[ACTIVE]]))
    for part in partners.PARTNERS:
        if part.get("ledger_title"):
            out.append(dict(Id="owed." + part["key"], Title=part["ledger_title"], Description=part["ledger_text"],
                            OpenWhen=[list(g) for g in part["deal"]],
                            SettledWhen=[[part["rel"] + ".lastcall.called"], [ACTIVE]]))
    return out
