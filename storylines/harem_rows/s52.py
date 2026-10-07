"""Authored S52 supply diversion; the native execution remains irreversible.

Evidence: Logistics_5 Answer_0006 e0c8aca7fe35b844a8ab76f96f2b3372
selects Cue_0048 513decde8a1bc7143bb2828521dad79f (Wenduag).
Cue_0028 b0e4bc74a55e1024785a9ebc830e7883 proposes Nerosyan hard labor;
Cue_0061 bd4c3ac7125e66e4ca0105cab06bb71f is Bartley's plague account;
Cue_0074 753c00e6878e7d548aea19a9b44f75af records the other thefts.
Verified against /wrath/blueprints.zip and enGB.json, 2026-10-07.
No intimacy, stance transition, resurrection, page purchase or native rewrite.
The protected historical channel intentionally needs neither romance nor page.
Participants is reserved by the runtime for romantic household eligibility;
these independent office audiences instead use current DerivedOpenRoutes.
"""
from story_format import c, n, p, scene
from storylines.dorgelinda_trickster import DREZEN, HUB, UNIT

P = "household.pair.wenduag_dorgelinda."
SELECTED = "household.s52.execution_selected"
VERDICT = "dorgelinda.verdict_hanged_wenduag"
OPEN = P + "office_open"
LIVE = P + "wenduag_here"
WENDUAG_UNIT = "ae766624c03058440a036de90a7f2009"
ACK = ("verdict_acknowledged", "cost.wenduag_advice_retained")
LOAD = ("provisioned", "load_received", "cost.dorgelinda_ward_shift",
        "cost.commander_private_supply", "cost.commander_name_kept")


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


def d(key, text, *answers):
    return n(key, "Dorgelinda", text, *answers, portrait="Dorgelinda", speaker_unit=UNIT)


def docket(live=False):
    opening = '''{n}Dorgelinda hooks a thumb beneath the lid of a crate beside her office door. Outside, a cart waits under the Commander's colors. Wine, clean blankets, good soap: supplies meant for your quarters.{/n}
"Bartley's company. Remember the plague? Men rotting in their bunks, and too few potions. That's what he told us. Then we found his other thefts, and his bloody warehouse."
{n}She lays the old order across the crate. The executions are marked in red.{/n}
"I asked for hard labor in Nerosyan. Wenduag said hang them. You gave the order. Some of the sick lived. They still need stores. Shall I open your cart?"'''
    if live:
        opening += '''
{n}Wenduag catches the lid before Dorgelinda can close it.{/n}
"I said hang them. They hung. Feed the survivors if they can still fight. But don't call the rope a mistake."
"And don't tell me which wounded soldier deserves a blanket," {n}Dorgelinda snaps.{/n}'''
    else:
        opening += '''
"Her approval's there beside your order. Neither name's coming off."'''
    nodes = [d("start", opening,
        c('"The order was mine. Open my cart; I will inspect the load."',
          check=dict(Skill="SkillPerception", DC=20, Success="received", Failure="short", CommanderOnly=True)),
        c('"The order was mine. Buy an inspected replacement from my allocation."',
          flags=flags("docket.seen", *ACK, *LOAD, "cost.commander_replacement_paid"),
          crusade=("Materials", -150)),
        c('"The sentence stands. I owe no load."', "refused"),
        c('[Lie] "It was your hanging, quartermaster."', "blame"),
        c("[Later.]", abort=True)),
        d("received", '''{n}Under the top layer of blankets lie sacks of chaff. You pull one out and split it on the threshold. Dorgelinda swears, climbs onto the cart, and has you uncover every crate before she takes anything. The blankets, soap and wine go to the sick; the chaff stays at your door.{/n}
"I'll spend my shift getting this to the wards. Your quarters can go without. The dead stay dead, Commander. This load is for the living."''',
          c("[Hand over the inspected stores.]", flags=flags("docket.seen", *ACK, *LOAD))),
        d("short", '''{n}Dorgelinda tears the cover from a sack. Chaff pours across her boots. Beneath the folded blankets, the cart is nearly empty.{/n}
"Someone's skimmed your fine gift down to a handful. Keep it here. In two days I can have a replacement ready — if you're paying. The wards aren't getting rubbish because it came on your cart."''',
          c("[Keep the short load for replacement.]", flags=flags("docket.seen", *ACK, "docket.failed", "cost.commander_short_load"))),
        d("refused", '''{n}Dorgelinda pushes the cart back from her threshold.{/n}
"Then take your wine home. I'll find something for the wards. If you change your mind, come back in two days. The execution order stays exactly as it was."''',
          c("[Send the cart back.]", flags=flags("docket.seen", *ACK, "docket.refused"))),
        d("blame", '''"Don't rub my name over yours. I asked for chains and a road to Nerosyan. You chose the rope."
{n}Dorgelinda taps your signature, then rolls the order shut. She leaves your cart outside.{/n}
"I'll keep that lie with it. Let anyone who hears you say it look at the order."''',
          c("[Leave the accusation on record.]", flags=flags("docket.seen", *ACK, "blame_shifted", "unanswered", "cost.commander_lie_on_record")))]
    return office("docket", nodes, live, forbids=(P + "docket.seen",))


def retry(live=False):
    text = '''{n}The replacement cart stands at Dorgelinda's door with its crates open. She holds up a blanket, shakes it out, and drops it onto the good soap and ward supplies beneath.{/n}
"Full load this time. Two hundred in materials from your allocation, and you walk it to the wards with me. I'll spend the shift assigning it myself. Nobody gets to skim it between here and the sickbeds."
{n}The old execution order lies on her desk, unchanged.{/n}'''
    if live:
        text += '''
"All that fuss over men who couldn't hold on to their own stores," {n}Wenduag says.{/n}
"You can carry a crate or get out of its way," {n}Dorgelinda answers, lifting it herself.{/n}'''
    nodes = [d("start", text,
        c('"Buy the full replacement. I will escort it."',
          flags=flags("retry.seen", *LOAD, "cost.commander_replacement_paid"), crusade=("Materials", -200)),
        c('"No load."', "refused"),
        c("[Later.]", abort=True)),
        d("refused", '''"Then there's nothing more to fetch from you."
{n}Dorgelinda shuts the crates. The wards will have to manage with what she can spare from elsewhere.{/n}''',
          c("[Leave without supplying the wards.]", flags=flags("retry.seen", "retry.refused", "unanswered")))]
    return office("retry", nodes, live, forbids=(P + "retry.seen", P + "provisioned"),
                  delay=48, RequiresAnyGroups=[[P + "docket.failed", P + "docket.refused"]])


def office(step, nodes, live, forbids, delay=0, **extra):
    # Both wrappers publish the same deed clock and spend the same allowance.
    # Enmity never hides this independent consequence; no joint invitation.
    return scene(P + step + (".live" if live else ""), "The Fellows' survivors", "Dorgelinda", 5,
                 ('"Wenduag, hear this too. About the Fellows."' if live else
                  '"About the Fellows, and the surviving sick."'), nodes,
                 requires=("trickster", P + "ready", OPEN, "dorgelinda.present") + ((LIVE,) if live else ()),
                 forbids=forbids, delay=delay, last=5,
                 Relationship="household", Chapters=[5], Areas=[DREZEN], AnswerLists=[HUB],
                 ContactUnit=UNIT, AdditionalContactUnits=[WENDUAG_UNIT] if live else [],
                 ReturnToList=True, Participants=[],
                 RestAllowance="household.protected", HouseholdCategory="protected",
                 HouseholdWitness=P + step + ".seen", **extra)


def register(payload, scenes, refs):
    payload.setdefault("SelectedAnswers", {})[SELECTED] = "e0c8aca7fe35b844a8ab76f96f2b3372"
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [[SELECTED, VERDICT]]
    # The Playing-only officer etude belongs on the area-bound scene, never
    # inside a global Derived reader. Each office wrapper requires it directly.
    derived[OPEN] = [["trickster", "dorgelinda.present_now"]]
    # InParty includes detached/remote companions and excludes the route's
    # returned off-party body. AdditionalContactUnits supplies the local body
    # check for either legitimate channel; present_now/RouteOpen read losses.
    derived[LIVE] = [["trickster", "wenduag.present_now"]]
    payload.setdefault("DerivedOpenRoutes", {}).update({OPEN: ["dorgelinda"], LIVE: ["wenduag"]})
    scenes.extend([docket(), docket(True), retry(), retry(True)])
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        ledger["Entries"].append(dict(
            Id=P + "record", Section="Seating Notes", Portrait="Dorgelinda",
            Title="The Fellows' survivors", Requires=["trickster", P + "verdict_acknowledged"],
            Text="{n}Wenduag advised execution. I ordered it. Dorgelinda had proposed hard labor in Nerosyan. That dispute remains.{/n}",
            Lines=[dict(Text="{n}" + text + "{/n}", Requires=list(flags(*keys))) for keys, text in (
                (("cost.wenduag_advice_retained",), "Wenduag's approval remains attached to the sentence."),
                (LOAD, "Dorgelinda received my diverted stores for the surviving sick and spent her shift assigning them. My quarters went without. The sentence stayed in my name."),
                (("docket.failed", "cost.commander_short_load"), "The first cart carried a substituted load. I kept the shortfall."),
                (("unanswered",), "I sent no load. The execution order remains in my name."),
                (("blame_shifted", "cost.commander_lie_on_record"), "I called it Dorgelinda's sentence. She kept my accusation beside the order I gave."),
                (("cost.commander_replacement_paid",), "I paid for the inspected replacement from my allocation."))]))
    # Only the existing epilogue hosts accept conditional paragraphs. Their
    # current route/payoff guards remain intact; ordinary dialogue gets none.
    by_id = {s["Id"]: s for s in scenes}
    for sid, paragraph in (
        ("wenduag.lastcall.page", p(
            '{n}Wenduag never disowned her advice on the Fellows. The Commander\'s stores for the surviving sick did not change her opinion of the thieves. She still thought they had deserved the rope.{/n}',
            requires=("trickster", *flags("cost.wenduag_advice_retained", "provisioned")))),
        ("dorgelinda.lastcall.page", p(
            '{n}Dorgelinda remembered the cart diverted from the Commander\'s quarters, and the shift she spent getting its stores to the wards. She also kept the execution order. The blankets had gone to the survivors; the names on the sentence had stayed where they belonged.{/n}',
            requires=("trickster", *flags(*LOAD)))),
        ("dorgelinda.lastcall.page", p(
            '{n}The Commander\'s attempt to call the hanging her sentence remained beside the original order. Dorgelinda had proposed hard labor. She let the signature answer the accusation.{/n}',
            requires=("trickster", *flags("cost.commander_lie_on_record"))))):
        host = by_id.get(sid)
        if host is not None and host.get("Owner") == "Epilogue":
            host["Nodes"][0].setdefault("Paragraphs", []).append(paragraph)
