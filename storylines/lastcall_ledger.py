"""The Trickster's Ledger as data (08-TRICKSTER-HOUSEHOLD.md §2.1). One list of entries; the UI reads it, the journal reads it.

Each entry: Id (stable, save-safe), Section, Portrait (a portrait key), Title, Body (conditional lines in the E14c paragraph
shape: Text, Requires, Forbids, AnyGroups), Tooltip (a string key the book UI resolves), OpenWhen / SettledWhen (OR of
AND-groups, the E15 shape). The journal quest "The Trickster's Ledger" is the native entry point: every Debts entry becomes an
E15 journal objective. The paged book UI (the shared RRT book component, 09-RRT-BOOK-UI.md) is being built separately; when its
contract lands, adapt entries() and nothing else.

Sections:
  debts         built now: one line per creditor power and per partner who is owed.
  guests        the Guest List: stubbed. The ids are reserved; entries are emitted by the household pass (05/08).
  seating       Seating Notes (frictions): stubbed, reserved ids.
  secrets       Secrets: stubbed, reserved ids trickster.secret.<k> (witnesses, risk). None is set anywhere yet.
"""

from storylines import lastcall_partners as partners

SECTIONS = ("debts", "guests", "seating", "secrets")

# Reserved id patterns for the later household pass. Nothing sets these flags yet, and no entry reads them.
RESERVED = {
    "guests": "ledger.guest.<rel>",               # reads <rel>.harem.stance.joined / .tolerated (05 §2.2)
    "seating": "ledger.seating.<rel_a>.<rel_b>",   # a friction from the registry (08 §3)
    "secrets": "trickster.secret.<k>",             # plus trickster.secret.<k>.witness.<rel> and trickster.secret.<k>.risk.<n>
}

ACTIVE = "lastcall.active"

# Portrait keys for creditors that are not partners (the book UI maps them; the journal ignores them).
CREDITOR_PORTRAITS = {"socoth": "Socothbenoth", "baphomet": "Baphomet", "nocticula": "Nocticula", "ramisa": "Ramisa",
                      "herrax": "Herrax", "abadar": "Abadar", "sunhammer": "Sunhammer", "mutasafen": "Mutasafen",
                      "wintersun": "Soana"}
PARTNER_PORTRAITS = {"irabeth": "Irabeth", "jerribeth": "Jerribeth", "konomi": "Konomi", "vellexia": "Vellexia",
                     "aranka": "Aranka", "gesmerha": "Gesmerha", "seelah": "Seelah", "dorgelinda": "Dorgelinda",
                     "eritrice": "Eritrice", "areelu": "Areelu", "chadali": "Chadali"}


def entries():
    out = []
    for debt in partners.DEBTS:
        out.append(dict(Id="debt." + debt["key"], Section="debts", Portrait=CREDITOR_PORTRAITS[debt["key"]],
                        Title=debt["ledger_title"], Tooltip="ledger.tooltip.debt.power",
                        Body=[dict(Text=debt["ledger_text"], Requires=[], Forbids=[], AnyGroups=[])],
                        OpenWhen=[list(g) for g in debt["groups"]],
                        SettledWhen=[[k] for k in debt["called_by"]] + [[k] for k in debt.get("outlived", ())] + [[ACTIVE]]))
    for part in partners.PARTNERS:
        if not part.get("ledger_title"):
            continue
        out.append(dict(Id="owed." + part["key"], Section="debts", Portrait=PARTNER_PORTRAITS.get(part["key"], ""),
                        Title=part["ledger_title"], Tooltip="ledger.tooltip.debt.partner",
                        Body=[dict(Text=part["ledger_text"], Requires=[], Forbids=[], AnyGroups=[])],
                        OpenWhen=[list(g) for g in part["deal"]],
                        SettledWhen=[[part["rel"] + ".lastcall.called"], [ACTIVE]]))
    return out


def journal_entries():
    """The E15 journal objectives: every Debts entry, its title and first body line."""
    return [dict(Id=e["Id"], Title=e["Title"], Description=e["Body"][0]["Text"], OpenWhen=e["OpenWhen"], SettledWhen=e["SettledWhen"])
            for e in entries() if e["Section"] == "debts"]
