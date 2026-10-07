"""S40: authored captive delivery; HAREM-SHEETS-36-41, row 40.

No native event is altered. Iomedae uses her earned banner channel; Nocticula
uses correspondence. This module supplies deeds, never attitude or enmity.
"""
import copy

from story_format import c, n, p, scene

P = "household.pair.iomedae_nocticula."
PAIR = ("iomedae", "nocticula")
BANNERS = ("iomedae.banner_in_hand", "iomedae.trickster.order_banner")
COMMON = ("trickster", "foresight.page_taken", "household.table.kept",
          "iomedae.harem.eligible", "nocticula.harem.eligible",
          "iomedae.trickster.first_spoken")
HELD = ("delivery.seen", "delivery.held", "resolved", "proof.six_alive",
        "cost.iomedae_credit_named", "cost.iomedae_sanctuary_watch",
        "cost.nocticula_patronage_burned", "cost.commander_last_man_carried")


def terminal(id, text, flags, cost=None):
    return n(id, "Narrator", text, c(flags=tuple(P + f for f in flags), crusade=cost))


def visit(step, title, nodes, requires=(), forbids=(), delay=0):
    return scene(P + step, title, "Iomedae", 5, "[Visit the banner platform: %s.]" % title,
                 nodes, requires=COMMON + tuple(P + f for f in requires),
                 forbids=(P + step + ".seen",) + tuple(P + f for f in forbids),
                 delay=delay, last=5, Relationship="household", Chapters=[5],
                 Remote=True, ManualOnly=True, Areas=["2570015799edf594daf2f076f2f975d8"],
                 RequiresAnyGroups=[list(BANNERS)], Participants=list(PAIR), Pair=list(PAIR),
                 RestAllowance="household.protected", HouseholdCategory="protected",
                 HouseholdWitness=P + step + ".seen")


RECEPTION = '''{n}The courier reads Nocticula's order aloud beside the receiving wagon.{/n}
"My broker has mistaken my protection for his property. Return his protection payment. Deliver Orren, Davit, Hald, Marten, Venn and Rul. Alive. Should he find this ruinous, remind him what my displeasure costs."
{n}The attendants check each man against his name and wounds. Rul cannot stand. You carry him into the sanctuary, his filthy bandage soaking your sleeve. The invitation to tonight's court entertainment lies unopened beside the wagon.{/n}
{n}A sword-shaped gleam crosses the banner. Iomedae's voice reaches you beneath it.{/n}
"Nocticula ordered their release. Record that. Record also who sold them. My sanctuary will keep watch over these six. Her markets remain an abomination."
{n}The courier takes down her words, including the last sentence.{/n}'''

SCENES = [
    visit("open", "Six names", [
        n("start", "Narrator", '''{n}You bring the captive list to Drezen's banner platform. Six crusaders, six descriptions: Orren's broken front tooth, Davit's branded wrist, Hald's crooked finger, Marten's scalp wound, Venn's missing ear, Rul's splinted leg. The courier has brought a reply bearing Nocticula's seal.{/n}
"My broker keeps them under my protection. How tiresome of him to forget whose protection it is. I will deprive him of six profitable possessions. Let the goddess name who gave the order. You will pay the crossing."
{n}Light gathers along the banner's sword. Iomedae speaks through it.{/n}
"Six names were given. I will receive six living men. Bring their wounds into the account, too. I will not have this trade hidden beneath a gracious gesture."''',
          c('"Six names, six men. I\'ll pay the crossing and meet the last one."', "commissioned"),
          c('"Let her send a token of goodwill. Leave the prisoners out of it."', "refused"),
          c("[Later.]", abort=True)),
        terminal("commissioned", '''{n}You pay the courier and book the planar crossing and receiving wagon. The sanctuary attendants copy the six names; you take the list that records their wounds. The courier leaves with your undertaking to meet the transport yourself.{/n}
"Do not send a servant in your place," {n}Iomedae says through the banner.{/n} "The last man will need carrying."''',
                 ("open.seen", "open.ready", "known.six_names", "cost.crossing_booked",
                  "cost.commander_reception_promised"), ("Finances", -200)),
        terminal("refused", '''{n}The light on the banner hardens.{/n}
"A token will not empty a cage. Keep your gesture."
{n}The courier folds the request without dispatching it. Six names remain on the captive list.{/n}''',
                 ("open.seen", "open.token_substituted", "permanent_refusal")),
    ]),
    visit("delivery", "The receiving wagon", [
        n("start", "Narrator", '''{n}The paid transport has reached Drezen. Four men answer to their names. Two more lie under blankets, scarcely breathing. The broker's escort urges the attendants to carry them inside before anyone examines them. Beside the banner, Nocticula's courier holds a sealed release order.{/n}
"The broker asks five hundred for an inspected release," {n}he says.{/n} "Or you may accept his manifest."
{n}You unfold the list of wounds. Iomedae's voice comes from the banner.{/n}
"Call their names. Look at their faces. No man here is ballast for your account."''',
          c("[Expose the slaver's attempt to substitute two dying men for two valuable prisoners.]",
            check=dict(Skill="SkillPerception", DC=24, Success="six", Failure="short", CommanderOnly=True)),
          c("[Pay the inspected ransom for the six named prisoners and conduct the reception yourself.]", "paid"),
          c('"Accept the substitutes. Six bodies will look the same in the account."', "falsified"),
          c("[Later.]", abort=True)),
        terminal("six", '''{n}The man called Venn has both ears. The other man's legs are sound. You confront the escort with the list before the wagon can be unloaded. The courier breaks Nocticula's seal. Her order sends the escort back through the paid crossing for the two men he withheld; the sick substitutes go to the healers as well.{/n}
''' + RECEPTION, HELD),
        terminal("paid", '''{n}You authorize the inspected ransom. The escort must fetch Venn and Rul before he receives it. The sick strangers are taken to the healers; neither is allowed to stand for a missing name.{/n}
''' + RECEPTION, HELD + ("cost.ransom_paid",), ("Finances", -500)),
        terminal("short", '''{n}You let the escort finish unloading before checking the wounds. His wagon is already returning through the crossing when the attendants discover that neither stranger is Venn or Rul. The four named men and the sick strangers receive care; the sanctuary's reception remains incomplete.{/n}
"You let the broker depart with a false count," {n}Iomedae says.{/n} "Nocticula's broker still holds Venn and Rul. Fetch them."
{n}The courier records your delay for his queen. Her unopened release order remains beside the list.{/n}''',
                 ("delivery.seen", "delivery.failed", "unsettled", "proof.manifest_short",
                  "cost.commander_reception_delayed")),
        terminal("falsified", '''"Six bodies?" {n}The banner snaps in the still air.{/n} "You were given six names. I will not bless a lie over two men's cages."
{n}The attendants take the sick strangers into care and strike out your false count. The courier leaves with no acknowledgment for his queen.{/n}''',
                 ("delivery.seen", "delivery.account_falsified", "permanent_refusal")),
    ], requires=("open.ready",), delay=48),
    visit("ransom", "The two withheld men", [
        n("start", "Narrator", '''{n}You return to the banner with an inspected crossing booked in your own name. The broker still holds Venn and Rul. His demand has risen to seven hundred. Nocticula's courier brings her order separately; there is no meeting between the queen and the goddess.{/n}
"He imagines delay has made him indispensable. Commander, pay the ransom. The broker's protection ends with this delivery. I shall enjoy explaining that to him."
{n}Iomedae's voice reaches you through the banner.{/n}
"Four men are under our watch. Two are still in his cages. I have kept their places."''',
          c("[Retrieve the two withheld men through the inspected paid crossing.]", "complete"),
          c('"Four is enough."', "declined"),
          c("[Later.]", abort=True)),
        terminal("complete", '''{n}You pay for the inspected crossing and take the last escort yourself. Venn has the missing ear on your list; Rul's splint has cut into his leg. You bring both to the wagon. The courier reads the release order only when their captor has surrendered them.{/n}
''' + RECEPTION,
                 ("ransom.seen", "ransom.held") + HELD[2:] + ("cost.late_crossing_paid",),
                 ("Finances", -700)),
        terminal("declined", '''"Enough for whom?" {n}Iomedae asks through the banner.{/n}
{n}The attendants keep tending the four men. Venn's and Rul's places remain empty. You dismiss the courier without commissioning their retrieval.{/n}''',
                 ("ransom.seen", "ransom.declined", "permanent_refusal")),
    ], requires=("delivery.failed",), forbids=("resolved", "permanent_refusal"), delay=48),
]

COSTS = {
    "crossing_booked": "I paid two hundred for the courier and receiving transport.",
    "commander_reception_promised": "I undertook to meet the last prisoner myself.",
    "iomedae_credit_named": "Iomedae named Nocticula's release order without excusing her market.",
    "iomedae_sanctuary_watch": "Iomedae assigned the sanctuary's watch to the six rescued crusaders.",
    "nocticula_patronage_burned": "Nocticula surrendered the broker's protection payment and stripped him of six men's resale value.",
    "commander_last_man_carried": "I carried Rul into care and missed the evening's court entertainment.",
    "commander_reception_delayed": "My failed inspection delayed the reception; Venn and Rul remained captive.",
    "ransom_paid": "The inspected ransom cost five hundred.",
    "late_crossing_paid": "The correction cost seven hundred for the inspected crossing.",
}
OUTCOMES = (
    ("resolved", "All six named crusaders were received alive into sanctuary.", ()),
    ("delivery.failed", "Two names still lacked their men after my failed inspection.", (P + "resolved",)),
    ("ransom.held", "I retrieved Venn and Rul after the failed reception.", ()),
    ("open.token_substituted", "I asked for a gesture instead of the men.", ()),
    ("delivery.account_falsified", "She refused my false count.", ()),
    ("ransom.declined", "Two remained in the slaver's claim when I abandoned their retrieval.", ()),
)


def reader_key(woman):
    return P + "reader." + woman + ".open"


def living_paragraphs(woman):
    """Separate Commander survival variants; contact readers never override closure."""
    texts = {
        "iomedae": 'Through the banner, Iomedae recalls the six names. "The queen gave the order. The sanctuary kept the men. Neither deed makes her market righteous."',
        "nocticula": 'Nocticula sends a recollection of her broker\'s loss. "The goddess named me. He paid for the privilege of hearing it. I found both quite satisfactory."',
    }
    out = []
    for flag, text, forbids in OUTCOMES:
        req = [P + flag, reader_key(woman)]
        groups = [BANNERS] if woman == "iomedae" else []
        # Outcome history is recollected by this woman alone, never a new absent reply.
        prose = "{n}" + (texts[woman] if flag == "resolved" else text) + "{/n}"
        out.extend((p(prose, requires=req, forbids=[*forbids, "sacrifice"], any_groups=groups),
                    p(prose, requires=[*req, "sacrifice", "trickster.commander_back"],
                      forbids=forbids, any_groups=groups)))
    for cost, text in COSTS.items():
        req = [P + "cost." + cost, reader_key(woman)]
        groups = [BANNERS] if woman == "iomedae" else []
        out.extend((p("{n}" + text + "{/n}", requires=req, forbids=["sacrifice"], any_groups=groups),
                    p("{n}" + text + "{/n}", requires=[*req, "sacrifice", "trickster.commander_back"],
                      any_groups=groups)))
    return out


_registered = False


def prepare(payload):
    """Called by story.make_story; register only S40 scenes and existing reader entries."""
    global _registered
    from storylines import household, lastcall_ledger, lastcall_partners, foresight

    derived = payload.setdefault("Derived", {})
    route_guards = payload.setdefault("DerivedOpenRoutes", {})
    for woman in PAIR:
        key = reader_key(woman)
        derived[key] = [[woman + ".harem.eligible", "iomedae.trickster.first_spoken"]] if woman == "iomedae" else [
            [P + "reader.nocticula.before_council"], [P + "reader.nocticula.returned"]]
        route_guards[key] = [woman]
    for suffix, group in (("before_council", ["nocticula.harem.eligible"]),
                          ("returned", ["nocticula.harem.eligible", "nocticula.trickster.returned"])):
        key = P + "reader.nocticula." + suffix
        derived[key] = [group]
        route_guards[key] = ["nocticula"]
    payload.setdefault("DerivedForbids", {})[P + "reader.nocticula.before_council"] = ["noct.acq.council_fight"]

    # RouteOpen checks declared availability dynamically. Also export the exact route
    # guards for ordinary scene tooling; the owner's Council silence is additional.
    from storylines import iomedae_trickster, nocticula_trickster, nocticula_continuation
    guards = {"iomedae": iomedae_trickster.RELATIONSHIP,
              "nocticula": dict(nocticula_continuation.RELATIONSHIP,
                                **nocticula_trickster.RELATIONSHIP_PATCH)}
    for body in copy.deepcopy(SCENES):
        body["ForbidOverrides"] = {"noct.acq.council_fight": "nocticula.trickster.returned"}
        body["Forbids"].append("noct.acq.council_fight")
        for woman, route in guards.items():
            body["Forbids"].extend([route["ClosedFlag"], *route.get("UnavailableFlags", ())])
            body["ForbidOverrides"].update(route.get("UnavailableOverrides", {}))
        payload["Scenes"].append(body)
        household.CONSUMERS[body["Id"]] = foresight.PAGE_TAKEN
        foresight.CONSUMERS[body["Id"]] = foresight.PAGE_TAKEN
    if _registered:
        return
    _registered = True
    lines = [p("{n}" + text + "{/n}", requires=[P + flag], forbids=forbids)
             for flag, text, forbids in OUTCOMES]
    lines.extend(p("{n}" + text + "{/n}", requires=[P + "cost." + cost]) for cost, text in COSTS.items())
    for suffix, section in (("ledger", "Guest List"), ("seating", "Seating Notes")):
        lastcall_ledger.EXTRA_ENTRIES.append(dict(
            Id=P + "reader." + suffix, Section=section, Portrait="", Title="Six names",
            Text="{n}The captive delivery: visits to the banner platform and receiving wagon in Drezen.{/n}",
            Lines=copy.deepcopy(lines), Requires=[P + "open.seen"], Forbids=[], AnyGroups=[], Tooltip=""))
    for woman in PAIR:
        part = next(part for part in lastcall_partners.PARTNERS if part["key"] == woman)
        if woman == "nocticula":
            # Her owner appends these during expansion, after make_story. Initialize
            # the same idempotent template additions first so S40 remains last and
            # every existing paragraph index and payoff contract stays unchanged.
            from storylines import nocticula_partners
            if not any(nocticula_partners.P + "share" in x["Requires"] for x in part["paragraphs"]):
                part["paragraphs"] = (*part["paragraphs"], *nocticula_partners.ending_paragraphs())
            nocticula_partners.add_acquisition_coda({"Scenes": []}, lastcall_partners, part)
        part["paragraphs"] = tuple(part["paragraphs"]) + tuple(living_paragraphs(woman))
