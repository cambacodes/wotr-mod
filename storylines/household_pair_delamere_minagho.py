"""S38: authored seized-dispatch docket, HAREM-SHEETS-36-41 row 38.

Native evidence and integration instructions are in tools/route_packs/harem/S38.md.
No native event is altered; no romance, attitude or reconciliation is produced.
Call integrate after household.integrate, before scene_kinds.integrate.
"""
import copy

from story_format import c, n, p, scene

PREFIX = "household.pair.delamere_minagho."
AREA = "2570015799edf594daf2f076f2f975d8"
ARRIVED = "minagho_chivarro.trickster.minagho_in"
RETURNED = "minagho_chivarro.trickster.returned_minagho"


def key(suffix):
    return PREFIX + suffix


WRITES = {
    "ready": ("open.seen", "open.ready", "known.dispatch"),
    "dismissed": ("open.seen", "open.dismissed", "known.dispatch", "permanent_refusal"),
    "seized": ("interception.seen", "proof.dispatch_seized", "claim.withdrawn", "resolved",
               "cost.delamere_shelter_watch", "cost.minagho_runner_exposed", "cost.commander_denounced"),
    "custody": ("interception.seen", "proof.prisoner_in_custody", "claim.withdrawn", "resolved",
               "cost.delamere_shelter_watch", "cost.minagho_quarry_yielded", "cost.commander_guard_duty"),
    "unsettled": ("interception.seen", "interception.unsettled", "unsettled", "cost.commander_key_offer_refused"),
    "delivered": ("repair.seen", "proof.dispatch_seized", "proof.prisoner_in_custody", "claim.withdrawn", "resolved",
                  "cost.delamere_shelter_watch", "cost.minagho_runner_exposed", "cost.minagho_quarry_yielded",
                  "cost.commander_contact_lost"),
    "declined": ("repair.seen", "repair.declined", "permanent_refusal"),
}


def terminal(id, speaker, text):
    return n(id, speaker, text, c(flags=[key(f) for f in WRITES[id]]))


def visit(step, title, nodes, requires=(), forbids=(), minagho=False):
    needs = ["trickster", "foresight.page_taken", "household.table.kept", "delamere.harem.eligible",
             "delamere.trickster.returned", *[key(f) for f in requires]]
    exclusions = ["delamere.closed", "inhuman", key(step + ".seen"), *[key(f) for f in forbids]]
    overrides = {}
    if minagho:
        needs += ["minagho.harem.eligible", ARRIVED]
        exclusions += ["minachiv.closed", "minagho.dead"]
        overrides["minagho.dead"] = RETURNED
    return scene(key(step), title, "Delamere" if not minagho else "Minagho", 5,
                 "[Visit the sanctuary dispatch docket.]", nodes, requires=needs, forbids=exclusions,
                 delay=48 if step != "open" else 0, last=5, Relationship="household", Chapters=[5],
                 Remote=True, ManualOnly=True, Areas=[AREA], RestAllowance="household.protected",
                 ForbidOverrides=overrides, HouseholdCategory="protected", HouseholdWitness=key(step + ".seen"),
                 Kind="visit")


SCENES = [
    visit("open", "A hunter's warrant", [
        n("start", "Delamere", '''{n}A pilgrim waits beside his wagon in Drezen. Delamere lays a copied dispatch across its tailboard. The seal bears a hooked personal mark.{/n}
"Minagho's runner wants my crypt key. His quarry is in the shelter: a cult jailer who fled his masters when their patrol broke. He brought this copy with him. Now he wants Erastil to forget what he did."
{n}She folds the copy around her finger, leaving the mark exposed.{/n}
"He can answer for his crimes without her hound dragging him over my threshold. The original goes through the relay here. Stop it, or take him into crusade custody before it reaches the temple."''',
          c('"Keep the copy. I\'ll stop the message before the runner reaches the shelter."', "ready"),
          c('"A jailer hiding in a shrine is her affair."', "dismissed"), c("[Later.]", abort=True)),
        terminal("ready", "Delamere", '''"The pilgrim will bring him here in the wagon. He knows the road; your guards need not leave the war to find it."
{n}She gives the pilgrim his instructions, then keeps the dispatch beneath her belt.{/n}
"I remember whose altar Zanedra defiled. This mark is another matter. I want this message stopped."'''),
        terminal("dismissed", "Delamere", '''{n}Delamere takes back the copy.{/n}
"Then I will keep the key, and meet her hound myself. Do not call this settled when she asks."
{n}The pilgrim turns his wagon toward the temple. The dispatch's original is still on its way.{/n}'''),
    ]),
    visit("interception", "The message at the relay", [
        n("start", "Minagho", '''{n}Minagho waits in her Drezen lodging. A fresh trickle of blood has dried beneath the brand on her brow. She scrapes it away with a nail.{/n}
"He hid from me in a priestess's pantry. How pious of him. He kept prisoners for the cult; he knows who is hunting me now. I want names. He can scream the rest."
{n}She sets her runner's mark beside the copied dispatch you brought.{/n}
"Delamere has a key. I have a man who can use it. What have you brought me besides her indignation?"''',
          c("[Seize the runner's original dispatch at the Drezen relay.]", "seized"),
          c("[Bring the marked man and the copied dispatch under crusade guard.]", "custody"),
          c('"I\'ll give her the key and call it a private quarrel."', "unsettled"), c("[Later.]", abort=True)),
        terminal("seized", "Narrator", '''{n}At the relay you wait until the runner opens his dispatch pouch, then pin the original beneath your hand. Its mark matches Delamere's copy. He shouts that the Commander protects a cult jailer; the soldiers waiting for field orders hear every word. You impound the message and send him back empty-handed.{/n}
{n}Minagho tears her remaining sanctuary order down the middle when you return.{/n}
"There. My useful little messenger is everyone's demon spy now. Keep the jailer breathing. Your interrogators can bring me his names."
{n}At the wagon, Delamere assigns the shelter watch to guards Harl and Osem, then takes the first watch herself. Her bow stays unstrung; the evening hunt passes without her.{/n}
"The message is stopped. Baphomet's servant still has no welcome at my altar."'''),
        terminal("custody", "Narrator", '''{n}The pilgrim's wagon arrives with the former jailer crouched under its canvas. You escort him to the crusade cells, lodge the copy with the custodian, and stand the prison watch until relief arrives. Minagho's runner is turned away at the gate.{/n}
{n}In her lodging, Minagho crosses the sanctuary order through.{/n}
"Your prisoner, then. Have your custodian ask him about the pursuit. I want his answers. If he ever walks free, he had better walk faster than my men."
{n}Delamere names Harl and Osem to the shelter roster and takes its first watch, missing her hunt.{/n}
"He has a cell instead of her knife. He has earned neither pardon nor a bed among the pilgrims."'''),
        terminal("unsettled", "Narrator", '''{n}Delamere closes her fist around the real key before your hand reaches it.{/n}
"You offered what was never yours. No."
{n}You return to Minagho without it. Her mouth twists.{/n}
"A key you cannot deliver. How very like a crusade promise. My runner will keep his order."
{n}The shelter remains locked against him. The dispatch and its claim remain outstanding.{/n}'''),
    ], requires=("open.ready",), minagho=True),
    visit("repair", "A source spent", [
        n("start", "Minagho", '''"Has the priestess finally lent you her key?"
{n}Minagho's runner waits outside her lodging with the dispatch pouch at his hip.{/n}
"No? Then stop dangling it. My jailer knows the cult's pursuit orders. Every day he hides, those orders get closer to me."
{n}At the relay, a clerk offers you a way into the dispatch store. The pilgrim's wagon waits in the yard with the marked man inside. You can still stop the message and put its quarry beyond the runner's warrant.{/n}''',
          c("[Deliver the intercepted message and place the marked man in guarded custody.]", "delivered"),
          c('"Leave her runner in place."', "declined"), c("[Later.]", abort=True)),
        terminal("delivered", "Narrator", '''{n}You recruit the relay clerk, Tovan, to retrieve the original through his locked sorting hatch. The runner catches you with it and demands a source. You name Tovan before the waiting couriers. The clerk empties his drawer and leaves the service; his secret access is spent.{/n}
{n}You impound the dispatch and escort the jailer from the wagon to the crusade cells. Delamere posts Harl and Osem at the shelter, taking the first watch herself instead of her hunt.{/n}
"You found something you could deliver," {n}she says.{/n} "Keep him there. I will keep her out."
{n}Minagho cancels her runner's sanctuary order.{/n}
"Two useful men wasted on one miserable jailer. Your custodian will bring me the pursuit names. Do not expect me to thank your priestess."
{n}The brand still bleeds beneath her fingers.{/n}'''),
        terminal("declined", "Minagho", '''"Then he carries my order. Tell Delamere that, if you can stomach another refusal."
{n}The runner closes his pouch. At the shelter Delamere keeps the real key and her bow beside her. Neither woman calls the claim withdrawn.{/n}'''),
    ], requires=("interception.unsettled",), forbids=("resolved", "permanent_refusal"), minagho=True),
]

COST_TEXT = {
    "cost.delamere_shelter_watch": "Delamere gave up her hunt and took the shelter's first watch.",
    "cost.minagho_runner_exposed": "Minagho's runner lost his cover at the Drezen relay.",
    "cost.minagho_quarry_yielded": "Minagho withdrew her private warrant; the jailer went into crusade custody.",
    "cost.commander_denounced": "The runner denounced me before the soldiers awaiting field orders.",
    "cost.commander_guard_duty": "I stood the jailer's prison watch until relief came.",
    "cost.commander_key_offer_refused": "I offered Delamere's key. She did not give it to me.",
    "cost.commander_contact_lost": "I exposed Tovan to recover the dispatch. He left the relay service.",
}


def integrate(payload):
    """Append S38 only; caller supplies an assembled household and Last Call."""
    if any(s["Id"] == key("open") for s in payload["Scenes"]):
        raise ValueError("S38 is already registered")
    derived = payload.setdefault("Derived", {})
    excludes = payload.setdefault("DerivedForbids", {})
    for state in ("alive", "returned"):
        flag = "household.minagho.eligible_" + state
        tail = [RETURNED] if state == "returned" else []
        derived[flag] = [["minachiv.complete", future, *tail]
                         for future in ("minachiv.future_minagho", "minachiv.future_two")]
        excludes[flag] = ["minachiv.closed", "inhuman"] + (["minagho.dead"] if state == "alive" else [])
    derived["minagho.harem.eligible"] = [["household.minagho.eligible_alive"], ["household.minagho.eligible_returned"]]
    excludes["minagho.harem.eligible"] = ["minachiv.closed", "inhuman"]
    reader = "household.reader.delamere.open"
    if reader in derived and derived[reader] != [["delamere.harem.eligible"]]:
        raise ValueError("Conflicting shared Delamere reader: " + reader)
    derived[reader] = [["delamere.harem.eligible"]]
    payload.setdefault("DerivedOpenRoutes", {})[reader] = ["delamere"]
    bodies = copy.deepcopy(SCENES)
    route = payload["Relationships"]["delamere"]
    for body in bodies:
        for flag in [route["ClosedFlag"], *route.get("UnavailableFlags", [])]:
            if flag not in body["Forbids"]:
                body["Forbids"].append(flag)
        body["ForbidOverrides"].update(route.get("UnavailableOverrides", {}))
        body["ForbidOverrides"].pop(route["ClosedFlag"], None)
    payload["Scenes"].extend(bodies)
    from storylines import foresight
    for body in bodies:
        foresight.CONSUMERS[body["Id"]] = "foresight.page_taken"
        payload.setdefault("ForesightConsumers", {})[body["Id"]] = "foresight.page_taken"
    lines = [p("{n}Minagho's present message was brought to me. Zanedra's old deed was not hers.{/n}", requires=[key("known.dispatch")]),
             p("{n}The sanctuary claim was withdrawn. Their fixed objection remained.{/n}", requires=[key("resolved")]),
             p("{n}I left the sanctuary claim unsettled.{/n}", requires=[key("unsettled")], forbids=[key("resolved"), key("permanent_refusal")]),
             p("{n}I recovered the dispatch and delivered the jailer into custody.{/n}", requires=[key("repair.seen"), key("resolved")]),
             p("{n}I left the shelter on her runner's route. The claim remained unanswered.{/n}", requires=[key("permanent_refusal")])]
    lines += [p("{n}" + text + "{/n}", requires=[key(flag)]) for flag, text in COST_TEXT.items()]
    for destination, section in (("ledger", "Guest List"), ("seating", "Seating Notes")):
        payload["Books"]["trickster.ledger"]["Entries"].append(dict(
            Id=key("reader." + destination), Section=section, Portrait="", Title="The sanctuary dispatch",
            Text="{n}Delamere and Minagho: a present claim, kept apart.{/n}", Lines=copy.deepcopy(lines),
            Requires=[key("known.dispatch")], Forbids=[], AnyGroups=[]))
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    for woman, host in (("delamere", "delamere.lastcall.page"), ("minagho", "trickster.lastcall.page.last_word")):
        node = next(n for n in by_id[host]["Nodes"] if n["Id"] == "page")
        attendance = [reader, "delamere.trickster.returned"] if woman == "delamere" else ["minagho.harem.eligible", ARRIVED]
        outcomes = [
            ("resolved", 'Delamere says, "The claim was withdrawn. My altar still has no welcome for her."' if woman == "delamere"
             else 'Minagho says, "The priestess kept her key. I still want the pursuit names from your custodian."'),
            ("permanent_refusal", 'Delamere says, "You left her runner on the road to my shelter. I kept the key."' if woman == "delamere"
             else 'Minagho says, "My runner kept his order. Your priestess kept her door shut."'),
            ("unsettled", 'Delamere says, "You offered my key once. You never received it."' if woman == "delamere"
             else 'Minagho says, "I am still waiting for something more useful than that borrowed key."'),
            ("open.ready", 'Delamere says, "The message was brought to you. You never stopped it."' if woman == "delamere"
             else 'Minagho says, "You took her copy and left my messenger alone."'),
        ]
        for flag, text in [*outcomes, *COST_TEXT.items()]:
            forbidden = []
            if flag in ("unsettled", "open.ready"):
                forbidden += [key("resolved"), key("permanent_refusal")]
            if flag == "open.ready":
                forbidden += [key("interception.seen")]
            requirements = [*attendance, key(flag)]
            for returned in (False, True):
                block = p("{n}" + text + "{/n}",
                          requires=requirements + (["sacrifice", "trickster.commander_back"] if returned else []),
                          forbids=forbidden + ([] if returned else ["sacrifice"]))
                # Build labels only, never state flags or additional scene IDs.
                block["Label"] = key("reader.lastcall." + woman + "." + flag
                                     + (".returned" if returned else ".living"))
                node.setdefault("Paragraphs", []).append(block)
