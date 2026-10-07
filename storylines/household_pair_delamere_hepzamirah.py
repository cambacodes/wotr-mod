"""S37: authored private-guard requisition; HAREM-SHEETS-36-41, row 37.

Canon anchors and limits are documented in tools/route_packs/harem/S37.md.
This X docket supplies only its own deed/cost witnesses, never household policy.
The page permits the business; it supplies neither evidence nor a remedy.
"""
import copy

from story_format import c, n, p, scene

PREFIX = "household.pair.delamere_hepzamirah."
DREZEN = "2570015799edf594daf2f076f2f975d8"


def key(suffix):
    return PREFIX + suffix


def terminal(step, *outcomes, **effects):
    return c("Continue", flags=tuple(key(s) for s in (step + ".seen",) + outcomes), **effects)


def visit(step, title, nodes, requires=(), forbids=(), delay=0):
    women = ["delamere"] if step == "open" else ["delamere", "hepzamirah"]
    return scene(key(step), title, "Delamere", 5, "[Visit: %s]" % title, nodes,
                 requires=("trickster", "foresight.page_taken", "household.table.kept",
                           "delamere.harem.eligible", "delamere.trickster.returned",
                           "hepzamirah.trickster.returned") +
                          (() if step == "open" else ("hepzamirah.harem.eligible",)) +
                          tuple(key(s) for s in requires),
                 forbids=tuple(f for w in women for f in (w + ".closed", w + ".epoch_unavailable")) +
                         ("sacrifice", key(step + ".seen")) +
                         tuple(key(s) for s in forbids), delay=delay, last=5,
                 Relationship="household", Chapters=[5], Areas=[DREZEN], Remote=True,
                 ManualOnly=True, Participants=women, RestAllowance="household.protected",
                 HouseholdCategory="protected", HouseholdWitness=key(step + ".seen"),
                 ForbidOverrides={"sacrifice": "trickster.commander_back"})


SCENES = [
    visit("open", "A claim on the temple", [
        n("start", "Delamere", '''{n}A pilgrim waits beside Delamere's door with a chipped temple stone wrapped in sacking. Across its carved antlers someone has gouged a maze. He lays a fresh requisition beside it: food, a storeroom, and recruits, demanded in Hepzamirah's name. Outside, the lower-wall scouts are mustering.{/n}
"The stone came from the occupation. The paper came yesterday. A captain she has taken into her service says my temple will feed his new guard."
{n}Delamere holds the paper flat with an arrowhead.{/n}
"This does not put her beside Zanedra. It puts her name on a demand. Take that to her."''',
          c('"Keep the stone and the requisition. I\'ll take her the claim in her own name."', "impounded"),
          c('"There are enough enemies here. Burn it."', "suppressed"),
          c("[Later.]", abort=True)),
        n("impounded", "Narrator", '''{n}The pilgrim leads you to the captain's cart in Drezen. Under a tarpaulin lie two serviceable mail shirts and six iron-headed hunting spears, taken from the temple storeroom. You impound them and assign them to the next lower-wall scout patrol. The captain keeps his office and his freedom to answer the accusation. The pilgrim's stone stays wrapped beside Delamere's door.{/n}''',
          terminal("open", "open.ready", "known.present_claim", "goods.equipment_impounded")),
        n("suppressed", "Delamere", '''{n}You feed the requisition to the brazier. Delamere pulls the stone clear before the sacking catches. The pilgrim backs toward the door.{/n}
"Keep your captain, then. Tell your scouts to watch his carts. He has learned what he can take here."''',
          terminal("open", "open.suppressed", "known.present_claim", "permanent_refusal")),
    ]),
    visit("hearing", "The captain's requisition", [
        n("start", "Delamere", '''{n}Delamere has kept the scarred stone. The pilgrim unfolds the requisition on her threshold; you have brought the impounded cart's inventory. The scout patrol is due to leave Drezen with its new equipment.{/n}
"Two shirts. Six spears. The captain took them from a village shrine to arm men against the same villagers. I want the goods back and his claim struck out."
{n}She taps the inventory.{/n}
"If your scouts keep these, carry a replacement to the pilgrim. I will count it myself. Then take the captain's paper to his mistress."''',
          c("[Return the recovered temple stone to Delamere and revoke the captain's requisition in his presence.]", "relic"),
          c("[Complete the store-restoration job instead.]", "stores"),
          c('"Call it an old quarrel and leave his claim standing."', "unsettled"),
          c("[Later.]", abort=True)),
        n("relic", "Hepzamirah", '''{n}You cancel the scout allocation and carry both mail shirts, all six spears and the stone to Delamere. She sets her bow aside to guard them until the pilgrim can take them home. In the captain's Drezen office you strike out his requisition before him. You then bring him and the cancelled paper to Hepzamirah's yard.{/n}
"He offered me a useful guard. Now I find he has been recruiting masters for me."
{n}She seizes his collar and hauls him close.{/n}
"Vorlesh wears my old office. You thought you could sell me a village and put another leash on my neck? Get out of my service before I tear yours open."
{n}He leaves without the equipment. Hepzamirah drops the paper at your feet.{/n}
"The claim is dead. I will find men who can steal without making promises in my name."
{n}You carry her answer back to Delamere. She does not put down her bow.{/n}
"Let her find them. If they come to my temple, I will bury them."''',
          terminal("hearing", "proof.relic_returned", "claim.revoked", "resolved",
                   "cost.delamere_stone_received", "cost.hepzamirah_captain_dismissed",
                   "cost.commander_prize_yielded")),
        n("stores", "Hepzamirah", '''{n}You draw a measured replacement allocation from the crusade's stores, costing 150 Materials, and deliver it into the pilgrim's custody. Delamere counts and guards it herself. At the captain's office you remove his occupation markers and cancel his requisition. The two mail shirts and six spears remain with the scouts. You carry the cancelled paper to Hepzamirah's yard.{/n}
"My guard will draw nothing from that temple."
{n}She drives her nail through the paper and pins it to a post before her remaining men.{/n}
"You heard me. Take your plunder elsewhere. Anyone offering this shrine in my name will answer with his tongue."
{n}She turns back to you.{/n}
"Those supplies would have armed useful men. You have bought your huntress a quiet door. Do not expect me to kneel outside it."
{n}At Delamere's lodging, you report the withdrawn claim.{/n}
"The village can eat this winter. She can keep her men and her distance."''',
          terminal("hearing", "proof.stores_restored", "claim.revoked", "resolved",
                   "cost.delamere_stores_guarded", "cost.hepzamirah_guard_claim_yielded",
                   "cost.commander_stores_replaced", crusade=("Materials", -150))),
        n("unsettled", "Delamere", '''{n}You leave the requisition in force. In her yard, Hepzamirah hears your decision and keeps the captain in her service. Back at Delamere's lodging, the pilgrim rolls up the unanswered claim.{/n}
"An old quarrel? He took those shirts this week. Your patrol will wear them."
{n}She puts the stone into the pilgrim's hands.{/n}
"Tell the villagers whose protection bought that guard. I will watch the road myself."''',
          terminal("hearing", "hearing.unsettled", "unsettled")),
    ], requires=("open.ready", "goods.equipment_impounded"), delay=48),
    visit("repair", "The withheld goods", [
        n("start", "Delamere", '''{n}The captain's requisition is still nailed above his office door. Delamere brings the impounded cart's inventory to you, with the pilgrim's mark beside each missing piece. A lower-wall patrol has already been ordered to draw the two shirts and six spears.{/n}
"You know where the goods are. Cancel your order. Bring every piece here, and make her throw that captain out."
{n}She sets the list across your patrol orders.{/n}
"I will not ask the villagers to pay twice."''',
          c("[Recover the captain's held temple goods and carry them to Delamere yourself.]", "returned"),
          c('"He can keep them."', "refused"),
          c("[Later.]", abort=True)),
        n("returned", "Hepzamirah", '''{n}You cancel the scout allocation and carry both impounded mail shirts and all six iron-headed spears to Delamere. She inventories and guards them until the pilgrim takes custody. You revoke the same captain's requisition before him, then bring him to Hepzamirah's yard.{/n}
"You let him trade on my name. Now you want him gone."
{n}Hepzamirah strips his badge from his coat, taking cloth and skin with it.{/n}
"He is gone. If I catch him recruiting for me again, I will hang his hide from this post. I can still use brutal men. I have no use for this one."
{n}At her lodging, Delamere hears the report with her bow across her knees.{/n}
"The village has its goods. She has fewer men to send against it. Keep her away from my door."''',
          terminal("repair", "proof.goods_returned", "claim.revoked", "resolved",
                   "cost.delamere_goods_received", "cost.hepzamirah_captain_dismissed",
                   "cost.commander_prize_yielded")),
        n("refused", "Delamere", '''{n}Delamere takes the inventory back. Outside, the patrol's boots strike the cobbles; the disputed equipment remains under your allocation.{/n}
"Then I have your answer. His claim stays. Mine does too."
{n}She shoulders her bow and goes to find the pilgrim.{/n}''',
          terminal("repair", "repair.declined", "permanent_refusal")),
    ], requires=("hearing.unsettled", "goods.equipment_impounded"),
       forbids=("resolved", "permanent_refusal"), delay=48),
]

COSTS = {
    "delamere_stone_received": "Delamere gave up a hunt hour to guard the returned sacred stone for the pilgrim.",
    "delamere_stores_guarded": "Delamere counted and guarded the replacement allocation herself.",
    "delamere_goods_received": "Delamere counted and guarded the returned shirts and spears herself.",
    "hepzamirah_captain_dismissed": "Hepzamirah lost a trained captain and his promised equipment.",
    "hepzamirah_guard_claim_yielded": "Hepzamirah relinquished the temple supplies as a source for her private guard.",
    "commander_prize_yielded": "I cancelled the scout allocation and surrendered both mail shirts and all six spears to Delamere.",
    "commander_stores_replaced": "I delivered the replacement allocation myself, at a cost of 150 Materials.",
}


def records():
    lines = [
        p("{n}The old temple wound and this new claim were separate.{/n}", requires=[key("known.present_claim")]),
        p("{n}I burned the evidence she brought me.{/n}", requires=[key("open.suppressed")]),
        p("{n}The present claim was revoked. Delamere's hostility toward Hepzamirah remained.{/n}", requires=[key("resolved")]),
        p("{n}The captain still claimed the temple; I left the objection unanswered.{/n}", requires=[key("known.present_claim")], forbids=[key("resolved")]),
        p("{n}I finally left the disputed goods under the scout allocation and the captain's claim standing.{/n}", requires=[key("repair.declined")]),
        p("{n}Two serviceable mail shirts and six iron-headed hunting spears were impounded and allocated to the lower-wall scouts.{/n}", requires=[key("goods.equipment_impounded")]),
    ]
    lines += [p("{n}" + text + "{/n}", requires=[key("cost." + suffix)]) for suffix, text in COSTS.items()]
    return lines


def register(payload):
    """Register this row via existing data registries; shared modules stay untouched."""
    from storylines import foresight, lastcall_ledger, lastcall_partners
    payload["Scenes"] = list(payload["Scenes"]) + copy.deepcopy(SCENES)
    for woman in ("delamere", "hepzamirah"):
        reader = "household.reader." + woman + ".open"
        payload.setdefault("Derived", {})[reader] = [[woman + ".harem.eligible"]]
        payload.setdefault("DerivedOpenRoutes", {})[reader] = [woman]
        payload.setdefault("DerivedForbids", {})[reader] = [woman + ".epoch_unavailable"]
    for body in SCENES:
        foresight.CONSUMERS[body["Id"]] = "foresight.page_taken"
    existing = {entry["Id"] for entry in lastcall_ledger.EXTRA_ENTRIES}
    for destination in ("ledger", "seating"):
        identity = key("reader." + destination)
        if identity not in existing:
            lastcall_ledger.EXTRA_ENTRIES.append(dict(
                Id=identity, Section="Debts" if destination == "ledger" else "Seating Notes", Portrait="Delamere",
                Title="The temple requisition" if destination == "ledger" else "Delamere and Hepzamirah",
                Text="{n}Separate visits to Delamere's lodging and Hepzamirah's yard in Drezen.{/n}",
                Lines=records(), Requires=[key("known.present_claim")], Forbids=[], AnyGroups=[]))
    # This registration is called on each export; never append the readers twice.
    for woman in ("delamere", "hepzamirah"):
        part = next(part for part in lastcall_partners.PARTNERS if part["key"] == woman)
        if any(para.get("Id", "").startswith(key("reader.lastcall.")) for para in part["paragraphs"]):
            continue
        resolved = {
            "delamere": 'Delamere recalled the revoked requisition. "The villagers kept their shrine. I still watch for her men on the road."',
            "hepzamirah": 'Hepzamirah recalled the revoked requisition. "I gave up that temple, Commander. I have other places to recruit. Keep your huntress out of my yard."',
        }
        unresolved = {
            "delamere": 'Delamere recalled the captain\'s unanswered claim. "You heard his demand. You left it standing. The villagers heard your answer too."',
            "hepzamirah": 'Hepzamirah recalled the unanswered claim against her guard. "You left his demand standing. Do not send the huntress to collect an apology from me."',
        }
        rows = [("resolved", resolved[woman], []),
                ("known.present_claim", unresolved[woman], [key("resolved")])]
        rows += [("cost." + suffix, text, []) for suffix, text in COSTS.items()]
        for witness, text, exclusions in rows:
            # Costs involving the other woman are historical recollections, not fresh replies.
            requires = [key(witness), "household.reader." + woman + ".open", woman + ".trickster.returned"]
            for suffix, additional, forbids in (
                ("living", [], exclusions + ["sacrifice"]),
                ("returned", ["sacrifice", "trickster.commander_back"], exclusions),
            ):
                para = p("{n}" + text + "{/n}", requires=requires + additional, forbids=forbids)
                para["Id"] = key("reader.lastcall." + woman + "." + witness + "." + suffix)
                part["paragraphs"] += (para,)
