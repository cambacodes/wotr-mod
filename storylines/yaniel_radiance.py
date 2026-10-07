"""Yaniel: Radiance in hand, not in the stash (Writer/handoffs/trickster/yaniel.md, Polish pass residual 2).

`yaniel.radiance_held` (trickster_world, Derived over the five InventoryItems forms) holds while Radiance is in the party
inventory OR the shared stash (Main.BuildState reads both for InventoryItems). The scenes where Yaniel looks at the
Commander's hip, or where the Commander draws Radiance or puts it in her hand, need the sword on the party. This module adds
a party-only read (E10 PartyItems: Player.Inventory only, which holds every party member's equipped items, never the
shared stash) and moves those gates to it, append-only: no node, choice or scene is added, removed or reordered; only the
listed gates read the new key (each paired "empty" branch forbids the new key, so exactly one branch still shows). The
epilogue's hall-peg paragraph (p4: the sword hung in the hall after the war) keeps the broad read.
This late integration point also appends the route's Joran memorials after the Last Call pages have been assembled.
"""
from storylines import yaniel_trickster as yt

HELD = yt.HELD                                       # yaniel.radiance_held (any form, party or stash)
IN_HAND = "yaniel.radiance_in_party"                 # Derived: any form in the party inventory (equipped included)

# PartyItems keys mirror the InventoryItems forms (trickster_world 'yaniel.radiance_*').
PARTY_ITEMS = {
    "yaniel.radiance_party.masterwork": "3b2df06a731030d49a1240b763cb6069",   # RadianceMasterwork
    "yaniel.radiance_party.plus1": "de1fc233ad934a0a93a17ebed3ec0cfb",        # RadiancePlus1ITem
    "yaniel.radiance_party.plus2": "6a80e629e9a5ca74da1dabc2984bba3b",        # RadiancePlus2
    "yaniel.radiance_party.ha4": "0ff011d62af77e9428e12ac08f63709e",          # Yaniel_Longsword4HolyAvenger
    "yaniel.radiance_party.ha6": "cf5c1a507825f184dacbc3abe14b9db1",          # Yaniel_Longsword6HolyAvenger
}
DERIVED = {IN_HAND: [[key] for key in PARTY_ITEMS]}

# Where the sword must be on the Commander: (scene, node) -> choice indices whose HELD reads move to IN_HAND; paragraphs by
# index; "scene" for the scene's own Requires.
CHOICES = {
    ("yaniel.trickster.late.wall", "wall"): (0, 1, 3),            # cuff_sword: she draws it into the emptied hand / cuff_empty / unseen
    ("yaniel.trickster.ch5.found", "start"): (1, 2),              # her eyes find the hilt on your hip, or nothing
    ("yaniel.trickster.ch5.found_late", "msg"): (2, 3),
    ("yaniel.trickster.verdict.hands", "start"): (0, 1, 2, 3, 4), # "Still on your hip" / "Show me": you draw Radiance
    ("yaniel.trickster.commit.trade", "room"): (1, 2),            # she looks at the hilt on your hip
    ("yaniel.trickster.beat.staunton", "brand"): (1, 2),          # you draw Radiance to the firelight
    ("yaniel.trickster.beat.raid", "start"): (2, 3),              # you draw Radiance on the parapet
}
EPILOGUES = ("together", "commit", "broken", "unasked", "distrusted", "unsettled", "declined")
# The epilogues' gate paragraphs (back from the Threshold, "she looked at the Commander's hip"), found by that text: their
# positions differ per page. Each page must have exactly the two (sword there / not there).
EPILOGUE_PAGES = tuple("yaniel.trickster.epilogue." + e for e in EPILOGUES)
HIP = "she looked at the Commander's hip"
SCENE_REQUIRES = ("yaniel.trickster.beat.drill",)                 # the drill in the court behind the gate tower


def _swap(keys):
    return [IN_HAND if k == HELD else k for k in keys]


def integrate(payload):
    """Bind the party-only read, move the listed gates and apply memorials after Last Call and trickster_world."""
    items = payload.setdefault("PartyItems", {})
    for key, guid in PARTY_ITEMS.items():
        if items.get(key, guid) != guid:
            raise ValueError("yaniel_radiance: conflicting PartyItems binding " + key)
        items[key] = guid
    derived = payload.setdefault("Derived", {})
    for key, groups in DERIVED.items():
        if derived.get(key) not in (None, groups):
            raise ValueError("yaniel_radiance: conflicting derived key " + key)
        derived[key] = [list(g) for g in groups]
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    def node(scene_id, node_id):
        scene = by_id.get(scene_id)
        if scene is None:
            raise ValueError("yaniel_radiance: scene missing " + scene_id)
        found = [n for n in scene["Nodes"] if n["Id"] == node_id]
        if len(found) != 1:
            raise ValueError("yaniel_radiance: node missing %s/%s" % (scene_id, node_id))
        return found[0]

    for (scene_id, node_id), indices in CHOICES.items():
        choices = node(scene_id, node_id)["Choices"]
        for i in indices:
            c = choices[i]
            if HELD not in c["Requires"] + c["Forbids"]:
                raise ValueError("yaniel_radiance: %s/%s choice %d no longer reads %s" % (scene_id, node_id, i, HELD))
            c["Requires"], c["Forbids"] = _swap(c["Requires"]), _swap(c["Forbids"])
    for scene_id in EPILOGUE_PAGES:
        gate = [p for p in node(scene_id, "page")["Paragraphs"] if HIP in p["Text"]]
        # The pages share their paragraph objects (one list in yaniel_trickster), so a page met later may already read IN_HAND.
        if len(gate) != 2 or any(HELD not in p["Requires"] + p["Forbids"] and IN_HAND not in p["Requires"] + p["Forbids"] for p in gate):
            raise ValueError("yaniel_radiance: %s no longer has the two hip paragraphs reading %s" % (scene_id, HELD))
        for p in gate:
            p["Requires"], p["Forbids"] = _swap(p["Requires"]), _swap(p["Forbids"])
    for scene_id in SCENE_REQUIRES:
        scene = by_id[scene_id]
        if HELD not in scene["Requires"]:
            raise ValueError("yaniel_radiance: %s no longer requires %s" % (scene_id, HELD))
        scene["Requires"] = _swap(scene["Requires"])

    # Route-owned memorial prose: Last Call has been assembled by this late integration point.
    yt.integrate_partner_memory(payload)
    _reconcile_lastcall(payload)

def _reconcile_lastcall(payload):
    """Route-owned callbacks, after shared Last Call assembly; no Threshold receipt is inferred."""
    from story_format import p
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = next(n for n in by_id["yaniel.lastcall.page"]["Nodes"] if n["Id"] == "page")
    paragraphs = page["Paragraphs"]
    # Keep all saved paragraph addresses. Holy custody is not proof of an Iz song.
    holy = paragraphs[3]
    holy["Text"] = ('{n}Radiance was on her hip on the wall that night. It did not sing. '
                    'She checked its edge by lamplight before the watch changed.{/n}')
    holy["Forbids"] = list(dict.fromkeys(holy.get("Forbids", []) + [yt.Y + "iz_song_reported", yt.HANDED_LATE]))
    oath = paragraphs[5]
    oath["Text"] = ('{n}After Iz, Yaniel heard the Commander\'s account and let the sword oath stand. '
                    'The march to the Threshold was still ahead of them.{/n}')
    paragraphs.extend((
        p('{n}The oath had been sworn underground, beside the hook in the Midnight Fane.{/n}',
          requires=(yt.OATH_STANDS,), forbids=(yt.LATE,)),
        p('{n}The oath had been sworn on her wall in Drezen, before the march to Iz.{/n}',
          requires=(yt.OATH_STANDS, yt.LATE), forbids=(yt.OATH_THRESHOLD,)),
        p('{n}Radiance was on her hip during the last watch. At Iz it had sung in her hands; '
          'she had told the Commander herself when she returned to Drezen.{/n}',
          requires=(yt.CARRIES, yt.HOLY, yt.Y + "iz_song_reported"), forbids=(yt.HANDED_LATE,)),
        p('{n}Radiance was on her hip during the last watch. The Commander had put it back in her hands '
          'after Iz. She had not carried it into that battle.{/n}',
          requires=(yt.CARRIES, yt.HOLY, yt.HANDED_LATE)),
        p('{n}The Commander had heard Radiance sing over Iz. Yaniel listened to the account '
          'from her place on the wall.{/n}', requires=(yt.JUDGES, yt.SANG), forbids=(yt.CARRIES,)),
    ))
    call = by_id["yaniel.lastcall.call"]
    for node in call["Nodes"]:
        if "You have carried her iron since the Midnight Fane" in node["Text"]:
            node["Text"] = node["Text"].replace("You have carried her iron since the Midnight Fane:",
                                               "You hold the iron you took from her wrist:")
            node["Text"] = node["Text"].replace("held a gate until the last cart was through",
                                               "held a gate while the last carts fled")
    ledger = payload["Books"]["trickster.ledger"]
    entry = next(e for e in ledger["Entries"] if e["Id"] == "owed.yaniel")
    entry["Text"] = ("{n}I took the iron from Yaniel's wrist. She kept Radiance, or charged me to carry it "
                     "to Deskari's heart. Taking the cuff did not finish that bargain.{/n}")
    entry["Lines"].extend((
        p("{n}I worked the pin out in the Midnight Fane, beside the hook.{/n}", forbids=(yt.LATE,)),
        p("{n}I worked the pin out on her wall in Drezen.{/n}", requires=(yt.LATE,)),
        p("{n}She offered the trade-back. We chose to keep what we had.{/n}",
          requires=(yt.COMMITTED, yt.SHACKLE), forbids=(yt.VIGIL,)),
        p("{n}After I refused the trade, we stood the vigil together. She gave me the iron again.{/n}",
          requires=(yt.VIGIL, yt.SHACKLE)),
    ))
    for rel in payload["Relationships"].values():
        for journal in rel.get("JournalEntries", []):
            if journal.get("Id") == "owed.yaniel":
                journal["Description"] = entry["Text"][3:-4]
