"""J05's unlocked S18X/S26 hosts, with distinct physical action witnesses.

All objects and actions here are authored ordinary restitution, not canon
items, cures or reconciliation. The locked Hepzamirah surrender attachment
is withheld: see tools/route_packs/plans/j05-material-contracts.json. Its absence
does not produce instructions. No extra scene, clock, retry or debit is added.
"""
from story_format import c, n
from storylines.harem_rows import s18x, s26


H = s18x.P
G = s26.P
H_PROOF = (s18x.REMEDY_READY, H + "instructions.carried",
           H + "cost.hepzamirah_trap_knowledge")
H_DELIVERED = (s18x.SEEN, H + "horzalah_captivity_named",
               H + "captivity_remedy_delivered", H + "instructions.destroyed",
               H + "cost.horzalah_inspection", H + "cost.horzalah_destruction")
G_PROOF = (G + "cache.disclosed", G + "recipients.selected",
           G + "cache_retrieved", G + "cache.delivered", s26.REMEDY,
           G + "cost.jerribeth_cache_surrendered", G + "cost.commander_retrieval")
G_DELIVERED = (G + "account.seen", G + "gesmerha_account_named",
               G + "remedy.delivered", G + "material_relief_verified",
               G + "cost.gesmerha_inspection")


def _node(body, key):
    return next(node for node in body["Nodes"] if node["Id"] == key)


def _captivity(body):
    if any(node["Id"] == "j05_instructions_destroyed" for node in body["Nodes"]):
        return
    # Index 0 still points to remedy; the saved unresolved continuation remains.
    # The pending hook alone cannot substitute for actual surrender and carrying.
    _node(body, "start")["Choices"][0]["Requires"].extend(H_PROOF[1:])
    _node(body, "remedy")["Choices"].append(c(
        '[Let Horzalah examine and burn the surrendered trap instructions.]',
        "j05_instructions_destroyed", requires=H_PROOF))
    body["Nodes"].append(n("j05_instructions_destroyed", "Horzalah",
        "[PROSE PENDING: Horzalah - keep the captivity accusation / inspect and destroy her sister's surrendered mundane trap instructions / spend her inspection and destruction while the jailer's lost knowledge buys no pardon]",
        c('[Record the destruction; retain the accusation.]', flags=H_DELIVERED,
          requires=H_PROOF, forbids=(s18x.SEEN,)),
        c('[Leave without recording a delivery.]', "unresolved")))


def _wintersun(body):
    if any(node["Id"] == "j05_cache_offer" for node in body["Nodes"]):
        return
    # This old answer can now be reached after actual unloading but before
    # inspection. Keep its identity/effects; distinguish inspection from aid.
    _node(body, "unresolved")["Choices"][0]["Text"] = (
        '"Your account is recorded. No remedy has been inspected."')
    _node(body, "start")["Choices"].append(c(
        '"Make her yield something your people can use. Timber and food."',
        "j05_recipients", requires=(s26.REPLY,),
        forbids=(s26.CLAN_DESTROYED, G + "cache.disclosed", G + "retrieval.failed")))
    # On reload after a real intermediate action, resume at its actual stage.
    # These are trailing answers, not a second allowance or retry allocation.
    _node(body, "start")["Choices"].extend([
        c('[Retrieve the cache Jerribeth surrendered.]', "j05_cache_route",
          requires=(G + "cache.disclosed", G + "recipients.selected"),
          forbids=(G + "cache_retrieved", G + "retrieval.failed", s26.CLAN_DESTROYED)),
        c('[Deliver the recovered timber and food.]', "j05_cache_return",
          requires=(G + "cache_retrieved", G + "recipients.selected"),
          forbids=(G + "cache.delivered", G + "retrieval.failed", s26.CLAN_DESTROYED)),
    ])
    # Retire the old no-remedy terminal by gating; preserve its saved destination.
    _node(body, "remedy_reserved")["Choices"][0]["Forbids"].append(s26.REMEDY)
    _node(body, "remedy_reserved")["Choices"].extend([
        c('[Let Gesmerha inspect the delivery.]', "j05_relief_inspected",
          requires=G_PROOF, forbids=(s26.CLAN_DESTROYED,)),
        c('[Leave the account unsettled.]', flags=s26.WITNESSES,
          requires=(s26.REMEDY,), forbids=(G + "cache.delivered",)),
        c('[Later.]', abort=True),
    ])
    body["Nodes"].extend([
        n("j05_recipients", "Gesmerha", '''"The families still at Wintersun. Food for their pots, wood for their roofs. Not a feast for her amusement."
{n}Gesmerha names the households and tells you where to take the loads. The crusade's wagons rattle past the smith's yard.{/n}
"Bring it to them. I will ask what arrived."''',
          c('[Ask Jerribeth for the cache.]', "j05_cache_offer", requires=(s26.REPLY,),
            forbids=(s26.CLAN_DESTROYED,)),
          c('[Leave the remedy owed.]', "unresolved"), c('[Later.]', abort=True)),
        n("j05_cache_offer", "Jerribeth",
          '''{n}The answer comes behind your left eye before you have finished asking. Gesmerha goes on carving; she hears only the forge.{/n}
"Timber and grain. For Wintersun. From me." {n}The laughter is high and abrasive and goes on a little too long.{/n} "Oh, I have a store. Every good host keeps a larder her guests do not know about. North of the worked fields, under the second ridge, there is a cellar the clan dug years ago and forgot, because I made them forget it. Roof beams. Grain. Enough for the families she named, if the damp has been kind."
"Take it. I give it to you, Commander. Not to her, and not to them. They will eat my bread and roof their houses with my timber, and every one of them will know whose larder it came from, because you will have to tell them."
{n}Something turns over in your memory, idly, like a guest picking up an ornament and putting it back in the wrong place.{/n}
"And when they thank you, think of me. I shall be listening."''',
          c('[Take the directions and carry Gesmerha\'s instructions.]', "j05_cache_route",
            flags=(G + "cache.disclosed", G + "recipients.selected",
                   G + "cost.jerribeth_cache_surrendered"),
            requires=(s26.REPLY,), forbids=(s26.CLAN_DESTROYED, G + "cache.disclosed")),
          c('[Leave the remedy owed.]', "unresolved"), c('[Later.]', abort=True)),
        n("j05_cache_route", "Narrator", '''{n}You follow Jerribeth's directions north. Beyond Wintersun's worked fields, the hidden store contains stacked roof timber and sacks of grain. Some sacks have taken damp. Getting the sound supplies to Gesmerha's families means hauling them along roads still watched by demons.{/n}''',
          c('[Load the timber and sound grain for Gesmerha\'s recipients.]', "j05_cache_return",
            flags=(G + "cache_retrieved", G + "cost.commander_retrieval"),
            requires=(G + "cache.disclosed", G + "recipients.selected"),
            forbids=(s26.CLAN_DESTROYED, G + "cache_retrieved", G + "retrieval.failed")),
          c('[Abandon the retrieval.]', "unresolved", flags=(G + "retrieval.failed",)),
          c('[Later.]', abort=True)),
        n("j05_cache_return", "Narrator", '''{n}You bring the loaded timber and grain to the living families Gesmerha named. They meet you beside their damaged roofs. You compare her directions with the doors before opening the first sack; the grain has survived the journey.{/n}''',
          c('[Unload the supplies into the recipients\' hands.]', "j05_cache_delivered",
            flags=(G + "cache.delivered", s26.REMEDY),
            requires=(G + "cache.disclosed", G + "cache_retrieved", G + "recipients.selected"),
            forbids=(s26.CLAN_DESTROYED, G + "cache.delivered", G + "retrieval.failed")),
          c('[Keep the supplies; leave the account owed.]', "unresolved"),
          c('[Later.]', abort=True)),
        n("j05_cache_delivered", "Narrator", '''{n}The families carry the grain indoors and stack the timber beside the damaged roofs. Your loads are empty. When you return to Gesmerha, she has their account of what reached them; she asks you to put the empty sacks where her hands can find them.{/n}''',
          c('[Present the delivered relief for inspection.]', "remedy_reserved",
            requires=G_PROOF), c('[Leave the account owed.]', "unresolved")),
        n("j05_relief_inspected", "Gesmerha", '''{n}Gesmerha feels the sacks, then follows your account of the timber against the families' messages. She stops you once to ask which roof received the longest beams.{/n}
"They have food. They have wood. That is something she no longer has."
{n}She pushes an empty sack aside and takes up her chisel.{/n}
"Write that it reached them. Leave the rest of her debt where it is."''',
          c('[Record the inspected material relief.]', flags=G_DELIVERED,
            requires=G_PROOF, forbids=(s26.CLAN_DESTROYED, G + "account.seen")),
          c('[Leave the inspection unfinished.]', "unresolved")),
    ])


def register(payload, scenes, refs):
    by_id = {body["Id"]: body for body in scenes}
    for sid in (H + "account", H + "account_table"):
        _captivity(by_id[sid])
    _wintersun(by_id[G + "account"])
    # Only the blocked surrender witnesses are producerless. In particular,
    # approval, native testimony, truce and paid foresight never create them.
    pending = payload.setdefault("PendingHooks", [])
    for flag in H_PROOF:
        if flag not in pending:
            pending.append(flag)
    entries = payload.get("Books", {}).get("trickster.ledger", {}).get("Entries", [])
    original = next((entry for entry in entries if entry["Id"] == G + "account"), None)
    if original and G + "remedy.delivered" not in original["Forbids"]:
        original["Forbids"].append(G + "remedy.delivered")
        original["Text"] = (
            "{n}Gesmerha named what was done to Wintersun. Marhevok blinded her; "
            "Jerribeth bewitched the clan. No remedy was inspected.{/n}")
    if original and not any(entry["Id"] == G + "material_relief" for entry in entries):
        entries.append(dict(Id=G + "material_relief", Section="Debts", Portrait="Gesmerha",
            Title="Wintersun: material relief delivered",
            Text="{n}Gesmerha inspected the timber and food delivered from Jerribeth's surrendered cache to Wintersun's living families. Her blindness, the enchantment's harm and her accusation remain.{/n}",
            Requires=list(G_DELIVERED), Forbids=[], AnyGroups=[], Lines=[]))
