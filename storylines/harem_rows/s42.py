"""S42: authored supply diversion, Kaylessa / Camellia; respect ceiling.

No native event is rewritten. The deliberate Kaylessa killing order remains
disqualifying. Attitude and first-wins policy are owned by the integrator;
their exact witness contract is tools/route_packs/harem/s42.md.
"""
from story_format import c, n, p
from storylines import household

P = "household.pair.kaylessa_camellia."
PAIR = ("kaylessa", "camellia")
REQUIRES = (
    "kaylessa.trickster.returned", "kaylessa.trickster.clock_named",
    "kaylessa.present_now", "camellia.present_now",
)
FORBIDS = (
    "fool_king.gone", "trickster.failed", "kaylessa.closed",
    "kaylessa.trickster.left_free", "inhuman", "kaylessa.dead",
    "kaylessa.epoch_unavailable", "camellia.closed", "camellia.killed",
    "camellia.dead", "camellia.kicked_out", "camellia.epoch_unavailable",
    "kaylessa.camellia_killed",
)
OVERRIDES = {
    "kaylessa.dead": "kaylessa.trickster.returned",
    "camellia.killed": "camellia.trickster.cost.knows_you_tried",
    "camellia.dead": "camellia.trickster.coffin_life",
    "camellia.kicked_out": "camellia.trickster.killed_held",
}
SUCCESS = (
    "camellia_copy_destroyed", "kaylessa_clasp_returned",
    "cost.camellia_shipment", "cost.kaylessa_cover_changed",
)
TERMINALS = {
    "settle": {
        "landed": ("settle.seen", "settle.done", *SUCCESS),
        "carried": ("settle.seen", "settle.done", *SUCCESS,
                    "cost.commander_evening", "carried_personally"),
        "missed": ("settle.seen", "settle.failed", "carrier_suspicious"),
        "declined": ("settle.seen", "settle.declined", "exposure_unsettled"),
    },
    "retry": {
        "sealed": ("retry.seen", "retry.done", *SUCCESS,
                   "cost.commander_evening", "carrier_burned"),
        "refused": ("retry.seen", "retry.declined", "exposure_unsettled"),
    },
}


def _later():
    return c("[Later.]", abort=True)


def _result(step, node, text, action):
    # Actions stay prospective in the node. The committing answer performs
    # the two deeds and pays their costs together; Abort has nothing to undo.
    label = "[Leave them to pack what remains.]" if step == "settle" else "[Go.]"
    return n(node, "Narrator", text,
             c(label + " " + action, flags=tuple(P + f for f in TERMINALS[step][node])),
             _later())


def _nodes(step):
    if step == "retry":
        return [
            n("start", "Narrator", '''{n}Kaylessa waits beside the tavern's back door, wearing a courier's grey cloak. Camellia has brought the perfume chest. Outside, wagons creak towards Drezen's gate, past wounded crusaders coming in.{/n}
"Your carrier recognized the false passenger," {n}Kaylessa says.{/n} "He hasn't seen my face. Keep it that way."
"He has become quite tiresome," {n}Camellia replies.{/n} "Burn the chest where he can see it. Let him chase you instead. I shall have to find someone else to carry my little purchases."
"The northern caravan, soldier. I'll give you a different coat. And you can explain every turn before we leave."''',
              c("[Burn the shipment and take the decoy route yourself.]", "sealed"),
              c('"No. Let the carrier keep asking."', "refused"), _later()),
            _result("retry", "sealed", '''{n}The northern caravan is ready to leave. Taking its road will cost your evening at the Fool King's court. Kaylessa lays a dark coat over the chest, keeping its collar turned away from Camellia.{/n}
"No magic. No lies to me," {n}she says.{/n} "He follows your coat, not mine."
"And I lose my perfume, my powder, and a useful fool." {n}Camellia holds her copy of the description over the candle.{/n} "Do bring back my clasp. I would hate to leave him something prettier to follow."
{n}Kaylessa opens her palm. The silver clasp lies there.{/n}''',
                    "[Burn the chest. Camellia burns her copy; Kaylessa returns the clasp and retires her old cover. Walk the decoy road.]"),
            _result("retry", "refused", '''{n}Camellia closes the chest without locking it.{/n}
"He will ask again. People who think they have found something valuable always do."
"Then I won't use that road," {n}Kaylessa says.{/n} "And I won't forget whose man is watching it."
{n}The caravan's departure bell sounds outside. Neither woman moves.{/n}''',
                    "[Leave the carrier's question unanswered.]"),
        ]
    return [
        n("start", "Narrator", '''{n}A perfume chest stands beneath the corner table. Camellia slides a merchant's description across its lid: a hooded elf, her coat, the market road she takes. Kaylessa reads it without touching the paper. Beyond the tavern windows, a cart carries broken crusader shields to the smithy.{/n}
"My carrier knows someone who buys such observations," {n}Camellia says.{/n} "I haven't sent it. Yet."
"Tell me where the load is going, soldier. Then tell me what you left out."
{n}Camellia taps the chest.{/n} "My powder and perfume. A dreadful waste, but he can be made to follow the wrong passenger."
"You," {n}Kaylessa says, looking at you.{/n} "Not some fool you found outside. I'll choose your coat. No spells, and nothing hidden from me."''',
          c("[Switch the carrier's loads.]", check=dict(Skill="SkillThievery", DC=28,
                                                        Success="landed", Failure="missed")),
          c("[Take the shipment out yourself.]", "carried"),
          c('"Keep your bargains out of her tent."', "declined"), _later()),
        _result("settle", "landed", '''{n}The lashings can be switched without leaving a mark. The ordinary outbound caravan will take the chest and description away from Kaylessa's market road; you will wear her chosen coat past the carrier's window.{/n}
"That turn, then the gate. Show him the collar," {n}Kaylessa says.{/n} "I'll stop using the grey cloak."
"How resourceful." {n}Camellia lifts her remaining copy towards the candle.{/n} "I could have bought a very fine dress with what this costs me."
{n}Kaylessa weighs the carrier's silver clasp in her hand.{/n} "You get this back when that burns. Not before."''',
                "[Divert the shipment with yourself as decoy. Camellia burns her copy; Kaylessa returns the clasp and abandons the old cover.]"),
        _result("settle", "carried", '''{n}The chest is light enough to carry. Escorting it to the outbound caravan will take the evening you had left free for the Fool King's court.{/n}
"The dark coat," {n}Kaylessa says.{/n} "Walk slowly past his window. Let him get a good look at the wrong elf."
"There goes my perfume." {n}Camellia holds her copy beside the flame.{/n} "And my carrier. He won't be welcome at my door after this."
"Nor at mine." {n}Kaylessa offers the clasp.{/n} "Burn that first. Then I won't have a reason to keep this."''',
                "[Spend the court evening walking the chest out. Camellia burns her copy; Kaylessa returns the clasp and retires her old cover.]"),
        _result("settle", "missed", '''{n}The lashings will not pass inspection. A loose end betrays the switch; the coat intended for the false passenger is still lying beside the chest. Kaylessa remains inside, out of the carrier's sight.{/n}
"Too curious," {n}Camellia murmurs.{/n} "He used to know better."
"He'll learn a coat, not my face," {n}Kaylessa says.{/n} "Don't send me down that road. Give him time to stop watching the gate, then we'll use another."
{n}The shipment can still be held back. Neither the paper nor the clasp has changed hands.{/n}''',
                "[Hold the shipment. Give the suspicious carrier two days before trying another road.]"),
        _result("settle", "declined", '''{n}Camellia rests one gloved hand on the description.{/n}
"A gallant speech. How unfortunate that my man cannot hear it."
"Keep the paper, then," {n}Kaylessa says.{/n} "You won't get the road I take tomorrow."
{n}Camellia smiles at her. Kaylessa does not smile back. Outside, another wounded patrol passes the windows.{/n}''',
                "[Leave their dispute unsettled. The carrier keeps his question.]"),
    ]


def _readers(payload):
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        lines = [
            dict(Text="{n}The carrier noticed the switch. The decoy needs another road.{/n}",
                 Requires=[P + "settle.failed"], Forbids=[P + "retry.seen", P + "exposure_unsettled"], AnyGroups=[]),
            dict(Text="{n}A shipment lost, a disguise changed. Neither woman kept the other's means of exposure.{/n}",
                 Requires=[P + f for f in SUCCESS], Forbids=[], AnyGroups=[]),
            dict(Text="{n}The carrier still has a question. Kaylessa keeps her disguise, and Camellia still has a use for the answer.{/n}",
                 Requires=[P + "exposure_unsettled"], Forbids=[], AnyGroups=[]),
        ]
        ledger["Entries"].append(dict(Id=P + "notes", Section="Seating Notes", Portrait="Kaylessa",
                                      Title="The diverted shipment",
                                      Text="{n}The merchant's description and Camellia's perfume chest.{/n}", Lines=lines,
                                      Requires=[P + "settle.seen"], Forbids=[], AnyGroups=[]))
        ledger["Entries"].append(dict(Id=P + "paid_labour", Section="Debts", Portrait="",
            Title="An evening on the caravan road",
            Text="{n}Paid labour: I walked the decoy road instead of spending the evening at the Fool King's court.{/n}",
            Lines=[], Requires=[P + "cost.commander_evening"], Forbids=[], AnyGroups=[]))
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    # Conditional prose is legal only on existing epilogue pages. Kaylessa has
    # no Last Call page in this base: her existing commitment ending reads it.
    for sid, cost, text in (
        ("camellia.lastcall.page", "cost.camellia_shipment",
         '{n}Camellia passed Kaylessa at the feast without a word about the merchant or his carrier. "I still miss that perfume," she told the Commander later. "The next man who asks about an elf had better bring me something worth losing it for."{/n}'),
        ("kaylessa.trickster.epilogue.no_lamb", "cost.kaylessa_cover_changed",
         '{n}Kaylessa never used the grey courier disguise from the diverted shipment again. Camellia had burned the description; she had returned Camellia\'s clasp. She still checked the market corners before crossing. "She can keep her secrets, soldier. I\'ll keep my eyes open."{/n}'),
    ):
        if sid in by_id:
            by_id[sid]["Nodes"][0].setdefault("Paragraphs", []).append(p(
                text, requires=("trickster", "foresight.page_taken", P + cost,
                                "kaylessa.present_now", "camellia.present_now"),
                forbids=("kaylessa.closed", "camellia.closed", "kaylessa.camellia_killed")))
    clearing = by_id.get("kaylessa.clearing.where_i_was_meant_to_die")
    if clearing:
        opening = next(node for node in clearing["Nodes"] if node["Id"] == "open")
        # Append-only variant: preserve every original answer index and target.
        original = [dict(answer, Requires=list(answer["Requires"]), Forbids=list(answer["Forbids"]))
                    for answer in opening["Choices"]]
        for answer in opening["Choices"]:
            answer["Forbids"].append(P + "cost.kaylessa_cover_changed")
        opening["Choices"].append(c("[Follow her by the other market road.]", "s42_cover",
                                    requires=(P + "cost.kaylessa_cover_changed",)))
        clearing["Nodes"].append(n("s42_cover", "Narrator", '''{n}Kaylessa wears a dark coat without the courier's collar. At the market she takes the narrow passage behind the tailor's instead of her old road.{/n}
"That carrier can watch the grey cloak until it rots," {n}she says.{/n} "And Camellia can buy her own perfume."
{n}She listens for footsteps before leading you towards the gate and the clearing.{/n}''', *original))


def register(payload, scenes, refs):
    """Register against the assembled payload; never mutate shared source files."""
    if any(s["Id"] == P + "settle" for s in scenes):
        return
    for step, trigger, delay, forbids in (
        ("settle", "kaylessa.committed", 0, ("settle.seen", "retry.seen")),
        ("retry", P + "settle.failed", 48, ("retry.seen", "settle.declined")),
    ):
        body = household.table_entry(
            P + step, "The wrong passenger" if step == "settle" else "Another road",
            "[Kaylessa and Camellia: the shipment]" if step == "settle" else "[Kaylessa and Camellia: the carrier]",
            _nodes(step), PAIR, trigger, requires=REQUIRES,
            forbids=FORBIDS + tuple(P + f for f in forbids), chapters=(5,), delay=delay,
            RestAllowance="household.protected",
            ForbidOverrides=OVERRIDES, HouseholdCategory="protected",
            HouseholdWitness=P + step + ".seen")
        # table_entry records entries for household.integrate as well as
        # returning the scene. This API is called on the assembled payload;
        # remove only our just-created pending entry to avoid double emission.
        household.ENTRIES.remove(body)
        scenes.append(body)
    from storylines import foresight
    consumers = {P + step: household.PAGE_TAKEN for step in TERMINALS}
    foresight.CONSUMERS.update(consumers)
    payload.setdefault("ForesightConsumers", {}).update(consumers)
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, tuple(reversed(PAIR))):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    _readers(payload)


def require_shown_retry(payload):
    """Run after the voice overlay; completion requires witnessing the carrier."""
    scene = next(s for s in payload["Scenes"] if s["Id"] == P + "retry")
    sealed = next(node for node in scene["Nodes"] if node["Id"] == "sealed")
    shown = P + "carrier_cruelty_shown"
    sealed["Text"] = """{n}The northern caravan is ready to leave. Taking its road will cost your evening at the Fool King's court. Kaylessa lays a dark coat over the chest, keeping its collar turned away from Camellia.{/n}"""
    sealed["Paragraphs"] = [
        p("""{n}Camellia has not taken her eyes off the tannery lane across the yard, where the carrier's boots show under the drying hides.{/n}
"Not at the gate, where the guard can count his fingers," {n}she says.{/n} "In there. Come, soldier. I want you to see how I close an account."
"I'll walk the grey cloak past his window," {n}Kaylessa says.{/n} "Don't let him see my face, and don't make me watch the end of it."
{n}She turns up her collar and goes. Camellia picks up the chest herself.{/n}""", forbids=(shown,)),
        p("""{n}The tannery lane stinks of lime and old blood, and now of something burnt. Kaylessa waits at the mouth of it with her hood down over her eyes and a hand pressed flat against the wall, not looking where she does not need to look.{/n}
"It is done," {n}Camellia says, drying her blade on a clean corner of the carrier's own coat.{/n} "Quite neatly, I thought. Now the coat, Kaylessa. The dark one."
{n}Kaylessa's hand comes away from the wall. The silver clasp lies in it.{/n} "He's the last thing that road will take from me. Walk it with me, soldier.\"""", requires=(shown,)),
    ]
    completion = sealed["Choices"][0]
    completion["Requires"] = [*completion.get("Requires", []), shown]
    completion["Text"] = "[Go.] [Walk the decoy road with Kaylessa, the carrier dead behind you. The chest burns; she returns the clasp and retires her old cover. The evening at the Fool King's court is spent.]"
    sealed["Choices"].append(c("Continue", "carrier_shown", forbids=(shown,)))
    scene["Nodes"].append(n(
        "carrier_shown", "Narrator",
        """{n}Camellia takes you into the tannery lane by the sleeve, past vats of lime and stretched hides and a drain that has not run clear in years. The carrier is at the far end with his back to you, watching a grey cloak move along the street beyond, the one he has been told to follow. He does not hear Camellia set the chest down on the cobbles. He hears the lid.{/n}
"Don't turn," {n}she says, very gently.{/n} "You would only spoil your own manners. Who bought the last description from you?"
{n}He gives a name before she has finished asking. She waits for the rest of it, and gets that too. At the mouth of the lane Kaylessa stands in her courier's cloak with her face turned to the wall, one hand lifted: stop, or hurry. It is not clear which.{/n}
"Burn the chest where he can see it," {n}Camellia murmurs, to you now.{/n} "I did say I would."
{n}She tips the oil over the perfume and the powder and the paper, and lights it with the carrier's own lamp. He watches it take, on his knees in the lime, and begins to understand what his usefulness cost. Then her hand closes in his hair, and the blade goes in beneath the jaw, slowly, at the angle she chose, and she holds him while it finishes with the light of the burning chest in her face and her mouth a little open. It takes longer than the reports will say.{/n}
"There," {n}she says, wiping the knife on his collar.{/n} "Tiresome people always do die so politely, at the end. Kaylessa. The lane is yours."
{n}Kaylessa does not look at the body. She looks at you, and at the knife, and turns up her collar. The hides smoke. Your evening is spent.{/n}""",
        c("Continue", "sealed", flags=(shown, P + "carrier_burned", P + "cost.commander_evening"))))
