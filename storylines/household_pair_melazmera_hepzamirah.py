"""S36: authored supply diversion; respect/respect ceiling, no intimate step.

Call integrate after household.integrate. Pair choices produce deeds and costs only;
the shared policy owner consumes POLICY_INPUTS. Canon evidence is in the row pack.
"""
import copy

from story_format import c, n, p, scene

P = "household.pair.melazmera_hepzamirah."
WOMEN = ("melazmera", "hepzamirah")
DREZEN = "2570015799edf594daf2f076f2f975d8"
TRUCE = "household.native.colyphyr_dragon_truce"
SEEN_CUES = {TRUCE: ["326fe8ba065fb9248992d419dd0d133d"]}
CONTACT = tuple(w + ".trickster.returned" for w in WOMEN)
COMMON = ("trickster", "trickster.now", "foresight.page_taken", "household.table.kept",
          *(w + ".harem.eligible" for w in WOMEN), *CONTACT)
ENMITIES = {a + ".harem.enmity." + b: a + ".harem.reconciled." + b
            for a, b in (WOMEN, WOMEN[::-1])}
POLICY_INPUTS = dict(failure=P + "diversion.failed", claimant="hepzamirah", target="melazmera",
                     reconciliation=P + "replacement.held", ceiling="respect")
RESPECT_GROUPS = [[P + "diversion.held"], [P + "replacement.held"]]


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


HELD = flags("diversion.seen", "diversion.held", "resolved", "cost.melazmera_hunt_yielded",
             "cost.hepzamirah_guards_detoured", "cost.commander_watch_kept")
TERMINALS = {
    ("open", "prepared", 0): flags("open.seen", "open.ready", "cost.commander_rear_wagon"),
    ("open", "start", 1): flags("open.seen", "open.declined", "permanent_refusal"),
    ("diversion", "held", 0): HELD,
    ("diversion", "lost", 0): flags("diversion.seen", "diversion.failed", "unsettled", "cost.commander_shipment_lost"),
    ("diversion", "escorted", 0): HELD + flags("cost.outriders_paid"),
    ("diversion", "start", 2): flags("diversion.seen", "diversion.declined", "permanent_refusal"),
    ("replacement", "carried", 0): flags("replacement.seen", "replacement.held", "resolved",
        "cost.melazmera_hunt_yielded", "cost.hepzamirah_guards_detoured", "cost.commander_watch_kept", "cost.replacement_carried"),
    ("replacement", "start", 1): flags("replacement.seen", "replacement.declined", "permanent_refusal"),
}


def terminal(step, node):
    cost = {("diversion", "escorted"): -300, ("replacement", "carried"): -400}.get((step, node))
    return c(flags=TERMINALS[step, node, 0], crusade=("Finances", cost) if cost else None)


def visit(step, title, nodes, requires=(), forbids=(), delay=0):
    direct = step != "replacement"
    return scene(P + step, title, "Melazmera", 5, "[Visit the outer stockyard.]", nodes,
        requires=COMMON + tuple(requires), forbids=flags(step + ".seen") + tuple(forbids)
        + tuple(ENMITIES if direct else ()), delay=delay, last=5, Relationship="household",
        Remote=True, ManualOnly=True, Areas=[DREZEN], Chapters=[5], Participants=list(WOMEN),
        Pair=list(WOMEN), RestAllowance="household.protected", Kind="visit",
        ForbidOverrides=dict(ENMITIES) if direct else {})


SCENES = [
    visit("open", "The ridge above the wagons", [
        n("start", "Narrator", '''{n}A wagon of meat waits outside Drezen's stockyard. Beyond the walls, demons still hunt the roads. Melazmera stands beside it in her folded woman-form, one grey nail sunk into the canvas. Hepzamirah's two hired guards keep their hands on their weapons.{/n}
"Your men walk over my supper, little princess," {n}Melazmera says, giggling.{/n} "The ridge leads to my hoard. Shall I leave a few bones to mark it?"
"Then eat farther up the hill. Those two are paid, and they stay mine." {n}Hepzamirah pulls the canvas free.{/n} "The low road leaves my stores exposed. If my guards escort them, who guards my door?"
"Send the Commander. The last wagon smells best."''',
            c('"I\'ll replace the meat and walk the diverted wagons myself."', "prepared"),
            c('"Use the ridge. Let the two of you sort it out."', "refused", flags=TERMINALS["open", "start", 1]),
            c("[Later.]", abort=True)),
        n("prepared", "Hepzamirah", '''"You take the rear. If something follows, you meet it before it reaches my men."
{n}She marks the low road on the wagon's side with a piece of charcoal. Melazmera scratches a second line toward an abandoned lime pit.{/n}
"The prowlers follow cattle blood. Give them something to sniff, thief. I will watch the ridge."
"And I will give the order to my guards," {n}Hepzamirah says.{/n} "After I see the road cleared."
{n}The last wagon has no covered seat. Its driver makes room for you among the sacks.{/n}''', terminal("open", "prepared")),
        n("refused", "Narrator", '''{n}Hepzamirah orders both guards back to her door. Melazmera follows their retreat with her eyes.{/n}
"They stay with me," {n}Hepzamirah says.{/n} "Find your meat elsewhere."
"Then keep them off my ridge, princess." {n}Melazmera pulls her nail out of the wagon's canvas, leaving a long tear.{/n}''', c()),
    ]),
    visit("diversion", "Blood on the low road", [
        n("start", "Narrator", '''{n}The wagons stand ready at dusk. A demon's cry carries from the low road. Hepzamirah checks the straps of her guards' shields; Melazmera watches the ridge with a hungry smile.{/n}
"Two passages," {n}Hepzamirah says.{/n} "This shipment and its replacement. My men leave your ridge for those. No more."
"And I let those wagons pass. I can count to two, princess."
{n}A bucket of cattle blood hangs from the rear axle. The driver looks from it to the lime pit, then to you.{/n}''',
            c("[Lay a false cattle trail toward the abandoned lime pit.]", check=dict(
                Skill="SkillPerception", DC=24, CommanderOnly=True, Success="held", Failure="lost")),
            c('"Keep the wagons on my route. I\'ll pay for outriders and give up the stores I set aside."', "escorted"),
            c('"Put prisoners on the ridge instead."', "refused", flags=TERMINALS["diversion", "start", 2]),
            c("[Later.]", abort=True)),
        n("held", "Narrator", '''{n}You find the prowlers' tracks and drag the bloody hide across them toward the pit. Their cries move away from the wagons. You walk at the rear until the last wheel clears the bend.{/n}
{n}Melazmera lets a guard pass beneath her hand. Her nails close on empty air.{/n}
"There goes a good mouthful. Keep the replacement off my ridge too."
"You heard her," {n}Hepzamirah tells her guards.{/n} "Take the low road for the replacement. Both of you."
{n}The guards turn downhill at her order. Melazmera stays above them, watching her hunting ground instead of following the meat.{/n}''', terminal("diversion", "held")),
        n("lost", "Narrator", '''{n}The hide crosses a fresh track you failed to notice. The prowlers come up behind the wagons. You cut a meat cart loose to draw them away; the driver escapes, but its load vanishes under claws.{/n}
"You led them straight to it!" {n}Hepzamirah drives her pick into the roadside earth.{/n} "Her hunting approach is untouched, my stores are gone, and you call this a diversion?"
"I called it supper," {n}Melazmera says. Her giggle stops when Hepzamirah turns on her.{/n}
"Keep your teeth away from my guards. Commander, you promised replacement meat. Carry it yourself. My men are staying with me."''', terminal("diversion", "lost")),
        n("escorted", "Narrator", '''{n}Your reserved stores fill the second wagon. Paid outriders take the low road ahead of the convoy while you keep the exposed rear watch. At the ridge, Melazmera steps aside. Neither guard is taken.{/n}
"Two passages," {n}she says, scraping a nail down the empty canvas.{/n} "I have yielded enough meat for two."
{n}Hepzamirah sends both guards down the detour, away from her own door.{/n}
"Escort the replacement by this road. If the outriders run, drag them back. They have been paid."
{n}She watches until her men reach the bend. Melazmera turns uphill toward her hoard.{/n}''', terminal("diversion", "escorted")),
        n("refused", "Narrator", '''"Prisoners?" {n}Melazmera gives a sharp giggle.{/n} "I asked for my hunting ground. Keep your scraps."
"And who commands the ridge while she eats them?" {n}Hepzamirah motions her guards away from the wagon.{/n} "She does. You have settled nothing."
{n}Neither woman gives way. The convoy remains in the yard.{/n}''', c()),
    ], requires=flags("open.ready"), delay=48),
    visit("replacement", "The Commander's load", [
        n("start", "Narrator", '''{n}The empty cart stands in Drezen's stockyard. Tooth marks gouge its axle. Hepzamirah has sent one guard to count what you bring; the other remains at her door. Melazmera waits farther up the track, out of his sight.{/n}
{n}The guard delivers Hepzamirah's words:{/n} "The Commander lost it. The Commander replaces it. No men from my door until the load is here."
{n}Above the yard, Melazmera calls down:{/n} "Bring your own back this time, thief. I want to see whether it bends."''',
            c('"My stores, my back, my night on the wagon."', "carried"),
            c('"The lost meat is your problem."', "refused", flags=TERMINALS["replacement", "start", 1]),
            c("[Later.]", abort=True)),
        n("carried", "Narrator", '''{n}You buy the missing provisions, shoulder the sacks and load the cart. The guard carries Hepzamirah's order back: both men will escort by the low road. You stand the rear watch through the night.{/n}
{n}At the ridge, Melazmera takes her hand off the wagon.{/n}
"Heavy? Good. That passage and the next are yours. My hoard stays mine."
{n}You bring the message to Hepzamirah after unloading. She orders her guards onto the detour for the next passage.{/n}
"She kept her claws to herself? Then I can spare them for one more escort. After that, she bargains again."
{n}Neither woman visits the other. The next convoy takes the low road; Melazmera lets it pass.{/n}''', terminal("replacement", "carried")),
        n("refused", "Narrator", '''{n}The guard leaves with your answer. Hepzamirah sends him back for the empty cart, with orders to bring no provisions for you.{/n}
{n}Later, on the ridge, Melazmera blocks your way with one grey hand.{/n} "Empty-handed? Then don't ask me to move."
{n}No escort takes the detour. The road beyond Drezen remains disputed.{/n}''', c()),
    ], requires=flags("diversion.failed"), forbids=flags("resolved", "permanent_refusal"), delay=48),
]

# Normal dialogue uses mutually exclusive answer gates, never epilogue paragraphs.
# Recollection is optional knowledge, not a new choice or an outcome producer.
KNOWN = '''{n}The slave master's account of a dragon truce on Colyphyr comes back to you. Melazmera catches your glance.{/n}
"Oh, that was me. Her miners were eating into my hunting ground."
"And you were eating the miners," {n}Hepzamirah says.{/n} "You got your truce. You will get no tribute here."'''
UNKNOWN = '''{n}Hepzamirah points at the wagon, then at the ridge.{/n}
"Your hoard is uphill. My stores are here. Keep your hunting away from this load."
"For two passages," {n}Melazmera says.{/n} "Don't mistake me for your hired guards."'''
# Duplicate the sole Continue at the preparation node; existing opening indices stay fixed.
prepared = SCENES[0]["Nodes"][1]
prepared["Choices"][0]["Next"] = "terms.known"
prepared["Choices"][0]["Requires"] = [TRUCE]
prepared["Choices"].append(c(next="terms.unknown", flags=TERMINALS["open", "prepared", 0], forbids=(TRUCE,)))
SCENES[0]["Nodes"].extend([
    n("terms.known", "Narrator", KNOWN, c()),
    n("terms.unknown", "Narrator", UNKNOWN, c()),
])

OUTCOMES = [
    ("resolved", "The wagons passed under the limited bargain. Neither woman yielded the ridge beyond those passages.", ("resolved",), ()),
    ("failed", "My false trail lost the meat. The ridge remained disputed.", ("diversion.failed",), ("resolved", "permanent_refusal")),
    ("repaired", "I carried the replacement and kept its rear watch. Separate messages secured the two passages.", ("replacement.held",), ()),
    ("open.declined", "I left the ridge disputed.", ("open.declined",), ()),
    ("diversion.declined", "Prisoner bait did not settle the road. Neither woman accepted it.", ("diversion.declined",), ()),
    ("replacement.declined", "The replacement never came. I left the lost meat to them.", ("replacement.declined",), ()),
]
COSTS = {
    "commander_rear_wagon": "I promised to take the dangerous last wagon.",
    "commander_watch_kept": "I kept the exposed rear watch.",
    "commander_shipment_lost": "My false trail cost us a cart of meat.",
    "replacement_carried": "I spent 400 Finances and hauled the replacement myself.",
    "outriders_paid": "The outriders cost 300 Finances; I also gave up my reserved stores.",
    "melazmera_hunt_yielded": "Melazmera yielded her hunting approach for the two convoy passages.",
    "hepzamirah_guards_detoured": "Hepzamirah sent both hired guards on the longer escort, leaving her door unguarded.",
}
REACTIONS = {
    "melazmera": {
        "resolved": 'Melazmera traces the ridge with a grey nail. "Those two loads passed. The next driver had better stop and ask."',
        "failed": 'Melazmera sniffs the empty cart. "Your trail spoiled a whole load, thief. Don\'t bring that trick near my hoard."',
        "repaired": 'Melazmera laughs at the Commander\'s stiff back. "You carried it after all. I let the next load through. Now take your wagons elsewhere."',
        "open.declined": 'Melazmera bares her teeth at the ridge. "If her guards come up, I hunt. You heard me."',
        "diversion.declined": 'Melazmera wrinkles her nose. "Prisoners? I asked for my hunting ground. Keep your scraps."',
        "replacement.declined": 'Melazmera scratches the empty cart. "No meat, no passage. Was that too difficult, thief?"',
    },
    "hepzamirah": {
        "resolved": 'Hepzamirah sends for her guards. "The two passages are finished. They guard my door again. She wants another bargain, she can ask."',
        "failed": 'Hepzamirah grips her pick. "You lost my provisions and left her approach intact. Replace them. I will not lose my men as well."',
        "repaired": 'Hepzamirah examines the unloaded cart. "You paid for what you lost. My guards took the detour. I owe her nothing beyond those passages."',
        "open.declined": 'Hepzamirah beckons her guards back. "Then my men stay with me. Let her hunt someone else\'s servants."',
        "diversion.declined": 'Hepzamirah strikes the ridge mark from the cart. "Bait leaves her in command of the approach. I did not ask you to fatten her."',
        "replacement.declined": 'Hepzamirah plants her pick beside the empty cart. "You broke your word. Do not ask me to lend you guards again."',
    },
}


def ledger_entries():
    """Historical records survive closure; available errands are identified separately."""
    lines = [p("{n}" + text + "{/n}", requires=flags(*req), forbids=flags(*ban))
             for _, text, req, ban in OUTCOMES]
    lines += [p("{n}" + text + "{/n}", requires=flags("cost." + key)) for key, text in COSTS.items()]
    return [dict(Id=P + "reader." + key, Section=section, Portrait="Melazmera",
                 Title="The ridge and the meat wagons", Text="{n}Stockyard visits and convoy errands in Drezen. I chose whether to undertake them.{/n}",
                 Requires=flags("open.seen"), Forbids=[], AnyGroups=[], Lines=copy.deepcopy(lines))
            for key, section in (("ledger", "Debts"), ("seating", "Seating Notes"))]


def living(text, woman, label, requires, forbids=()):
    required = [P + flag for flag in requires] + ["household.reader." + woman + ".open", woman + ".trickster.returned"]
    banned = [P + flag for flag in forbids]
    return [dict(p(text, requires=required, forbids=banned + ["sacrifice"]), Id=label + ".living"),
            dict(p(text, requires=required + ["sacrifice", "trickster.commander_back"], forbids=banned), Id=label + ".returned")]


def integrate(payload):
    """Coordinator attachment: after household.integrate, before final checks.

    Does not set attitudes, stance, enmity or reconciliation. The exact shared policy
    inputs are exported in the build sheet rather than silently inventing a producer.
    """
    if any(s["Id"].startswith(P) for s in payload["Scenes"]):
        raise ValueError("S36 already integrated")
    pages = {s["Id"]: s for s in payload["Scenes"]}
    for woman in WOMEN:
        pages[woman + ".lastcall.page"]  # require both existing destinations before mutation
    payload["Books"]["trickster.ledger"]
    scenes = copy.deepcopy(SCENES)
    for body in scenes:
        for woman in WOMEN:
            rel = payload["Relationships"][woman]
            body["Forbids"] = list(dict.fromkeys(body["Forbids"] + [rel["ClosedFlag"]] + rel.get("UnavailableFlags", [])))
            body["ForbidOverrides"].update(rel.get("UnavailableOverrides", {}))
            body["ForbidOverrides"].pop(rel["ClosedFlag"], None)
    payload["Scenes"].extend(scenes)
    # Same reserved-key contract as household.integrate: guards are known while
    # their producers remain exclusively the shared policy owner's responsibility.
    pending = payload.setdefault("PendingHooks", [])
    for key in (*ENMITIES, *ENMITIES.values()):
        if key not in pending:
            pending.append(key)
    payload.setdefault("SeenCues", {}).update(copy.deepcopy(SEEN_CUES))
    payload.setdefault("ForesightConsumers", {}).update({s["Id"]: "foresight.page_taken" for s in scenes})
    derived = payload.setdefault("Derived", {})
    for woman in WOMEN:
        reader = "household.reader." + woman + ".open"
        derived[reader] = [[woman + ".harem.eligible"]]
        payload.setdefault("DerivedOpenRoutes", {})[reader] = [woman]
        node = next(n for n in pages[woman + ".lastcall.page"]["Nodes"] if n["Id"] == "page")
        for key, _, requires, forbids in OUTCOMES:
            node.setdefault("Paragraphs", []).extend(living(
                "{n}" + REACTIONS[woman][key] + "{/n}", woman, P + "reader.lastcall." + woman + "." + key, requires, forbids))
        for key, text in COSTS.items():
            node["Paragraphs"].extend(living("{n}" + text + "{/n}", woman,
                P + "reader.lastcall." + woman + ".cost." + key, ("cost." + key,)))
    payload["Books"]["trickster.ledger"]["Entries"].extend(ledger_entries())
    validate(scenes)


def validate(scenes=SCENES):
    """Freeze S36 identities, outcome contracts and the class-wide gate discipline."""
    if [s["Id"] for s in scenes] != [P + step for step in ("open", "diversion", "replacement")]:
        raise ValueError("S36 scene identities/order changed")
    identities = {
        "open": [("start", 3), ("prepared", 2), ("refused", 1), ("terms.known", 1), ("terms.unknown", 1)],
        "diversion": [("start", 4), ("held", 1), ("lost", 1), ("escorted", 1), ("refused", 1)],
        "replacement": [("start", 3), ("carried", 1), ("refused", 1)],
    }
    written = {flag for values in TERMINALS.values() for flag in values}
    for body in scenes:
        step = body["Id"][len(P):]
        if [(node["Id"], len(node["Choices"])) for node in body["Nodes"]] != identities[step]:
            raise ValueError("S36 node identities or choice indices changed")
        if not set(COMMON) <= set(body["Requires"]):
            raise ValueError("S36 missing earned gates")
        if (body["MinChapter"], body["MaxChapter"], body["Chapters"], body["DelayHours"]) != (5, 5, [5], 0 if step == "open" else 48):
            raise ValueError("S36 chapter/clock changed")
        if body.get("Participants") != list(WOMEN) or body.get("RestAllowance") != "household.protected":
            raise ValueError("S36 attendance/allowance changed")
        if not body.get("Remote") or not body.get("ManualOnly") or body["Areas"] != [DREZEN]:
            raise ValueError("S36 manual visit changed")
        if step == "replacement" and set(ENMITIES) & set(body["Forbids"]):
            raise ValueError("Separate remedy suppressed by enmity")
        if step != "replacement" and (not set(ENMITIES) <= set(body["Forbids"])
                or any(body["ForbidOverrides"].get(key) != value for key, value in ENMITIES.items())):
            raise ValueError("S36 direct exchange missing enmity guards")
        clock = {"diversion": "open.ready", "replacement": "diversion.failed"}.get(step)
        if clock and P + clock not in body["Requires"]:
            raise ValueError("S36 missing preceding deed clock")
        nodes = {node["Id"]: node for node in body["Nodes"]}
        if not nodes["start"]["Choices"][-1]["Abort"]:
            raise ValueError("S36 opening must end with Later")
        for node in body["Nodes"]:
            if node.get("Paragraphs"):
                raise ValueError("S36 paragraphs outside epilogue")
            for answer in node["Choices"]:
                if any(flag not in written for flag in answer["Set"]):
                    raise ValueError("S36 may write only pair witnesses")
                if answer["Abort"] and node["Id"] != "start":
                    raise ValueError("S36 post-deed Abort")
                if answer["Abort"] and (answer["Set"] or answer.get("Crusade")):
                    raise ValueError("S36 Abort writes or spends")
                if answer.get("Next") and answer["Next"] not in nodes:
                    raise ValueError("S36 missing saved destination")
                cost = {("diversion", "escorted"): -300, ("replacement", "carried"): -400}.get((step, node["Id"]))
                expected_cost = dict(Resource="Finances", Amount=cost) if cost else None
                if answer.get("Crusade") != expected_cost:
                    raise ValueError("S36 price changed")
        for (terminal_step, node_id, index), expected in TERMINALS.items():
            if terminal_step != step:
                continue
            indices = (0, 1) if (step, node_id) == ("open", "prepared") else (index,)
            for actual_index in indices:
                if tuple(nodes[node_id]["Choices"][actual_index]["Set"]) != expected:
                    raise ValueError("S36 terminal witnesses changed")
    check = scenes[1]["Nodes"][0]["Choices"][0].get("Check")
    if check != dict(Skill="SkillPerception", DC=24, CommanderOnly=True, Success="held", Failure="lost"):
        raise ValueError("S36 check changed")
    return True
