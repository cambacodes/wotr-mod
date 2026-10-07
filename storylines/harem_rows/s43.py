"""S43: authored Ch5 trail erasure, Kaylessa / Anevia; respect ceiling.

The scout, shrine, drop and personal courier are additions, not native history.
Native anchors (blueprints.zip + enGB.json, checked 2026-10-07):
Kaylessa_main/Cue_0084 5f306afcd4d305b41a611a59cc35e274: Anevia destroys the amulet.
Cue_0056 462478faddd1eab45a4e55739d81e6f7: Kaylessa removes her own mask.
Cue_0093 ea4d827995a68b24381d590724973965: Anevia's watched trap, not prior cooperation.
Cue_0073 425898fabfef36844b7b21801a205274: Kaylessa's 'soldier' address.
No native event is altered; no echo, return, marriage term or closure is produced.
"""
import copy

from story_format import c, n, p, scene
from storylines import household

P = "household.pair.kaylessa_anevia."
PAIR_MEMBER = P + "anevia_pair_member"
STAGE_PRODUCERS = {
    "kaylessa.harem.attitude.w.anevia.respect": [[P + "anevia_drop_destroyed", P + "cost.anevia_buyer_lost"]],
    "tirabade.harem.attitude.anevia.kaylessa.respect": [[P + "kaylessa_route_shown", P + "cost.kaylessa_private_route", P + "used_pair_seat"]],
    "anevia.harem.attitude.kaylessa.respect": [[P + "kaylessa_route_shown", P + "cost.kaylessa_private_route", P + "used_solo_seat"]],
}
UNRESOLVED_INPUT = P + "trail_unsettled"  # integrator's first-wins input; failure is pending
SUCCESS = ("anevia_drop_destroyed", "kaylessa_route_shown", "cost.anevia_buyer_lost", "cost.kaylessa_private_route")


def terminal(step, node, text, flags, seat):
    writes = [P + step + ".seen", *(P + f for f in flags)]
    if "anevia_drop_destroyed" in flags:
        writes.append(P + "used_" + seat + "_seat")
    return n(node, "Narrator", text,
             c("[Return to Drezen.]" if step == "settle" else "[Return.]", flags=writes),
             c("[Later.]", abort=True))


def nodes(step, seat):
    later = c("[Later.]", abort=True)
    if step == "retry":
        return [
            n("start", "Anevia", '''{n}At the corner table Anevia lays down a splinter from the shrine's broken door.{/n}
"Still watchin' it. They know somebody's been there. My lookout can't go back once we smash it in front of 'em."
{n}Kaylessa pushes the splinter away.{/n} "Then he doesn't go back. I'll show you my way out. Once. After tonight I'll need another."
"And your courier?" {n}Anevia turns to you.{/n} "Send 'em home after this. They won't stay unknown with that lot lookin' for them."
{n}The courier waits by the door, your unopened personal letter still in hand. Outside, crusade patrols are returning through Drezen's gates.{/n}''',
              c("[Give Anevia the courier and destroy the watched drop openly.]", "closed"),
              c('"Keep watching it. I won\'t spend the contact."', "refused"), later),
            terminal(step, "closed", '''{n}The courier waits for your order to give Anevia the drop's hiding place and leave your service. At the roadside shrine, her lookout has a clear path away; Kaylessa waits to lead you down her escape route.{/n}
"We go now, we lose the buyer and the lookout's way in," {n}Anevia says.{/n} "I'll break the hiding place myself."
"And I change my road," {n}Kaylessa answers.{/n} "Watch where I take you, soldier. You won't walk it twice."
{n}Anevia lifts the hammer. Your signal will bring it down.{/n}''',
                     ("retry.done", *SUCCESS, "cost.commander_courier", "cost.anevia_lookout_burned", "contact_spent"), seat),
            terminal(step, "refused", '''"Right. I'll keep the watch." {n}Anevia puts the splinter in her pocket.{/n}
"Not on my road." {n}Kaylessa pulls her hood up and leaves ahead of you. Anevia makes no move to follow her.{/n}''',
                     ("retry.declined", "trail_unsettled"), seat),
        ]
    return [
        n("start", "Anevia", '''{n}Anevia has caught Kaylessa's sleeve before she can leave the corner table. Kaylessa looks at the hand until it releases her.{/n}
"A scout's been askin' about that cloak. He's left Drezen. I've got someone watchin' the drop at the old roadside shrine. Let him collect, we get his buyer."
"He has my face," {n}Kaylessa says.{/n} "By the time you find your buyer, someone else has it. Break the trail tonight."
{n}Your private courier waits nearby with an unpaid personal letter. Anevia nods toward them.{/n}
"They know that drop. Used to shelter there before the crusade took this road. If sneakin' fails, they can show me where to smash it. Then they go home for good."
"Lose your buyer," {n}Kaylessa says,{/n} "and I'll show you the road I keep for myself."
"I can lose one buyer. I can't protect a road you won't show me."''',
          c("[Break the trail while Anevia takes the lookout.]", check=dict(Skill="SkillStealth", DC=27, Success="broken", Failure="spotted")),
          c("[Give Anevia your own courier contact.]", "contact"),
          c('"Follow it. Kaylessa can wait."', "declined"), later),
        terminal(step, "broken", '''{n}At the disused shrine outside Drezen, you reach the hollow beneath the altar unseen. The scout's scratched directions and the strip of cloth matching Kaylessa's cloak lie within. You hold them over your lamp. Nothing has burned yet.{/n}
{n}Anevia signals that the lookout is facing away. Kaylessa points toward a narrow gully.{/n}
"Then walk behind me, soldier. And remember which turns I let you see."
"I won't follow the buyer," {n}Anevia says.{/n} "Burn it. Then show me."
{n}One movement will erase the scout's directions. Kaylessa waits to lead you both away.{/n}''',
                 ("settle.done", *SUCCESS), seat),
        terminal(step, "contact", '''{n}Outside Drezen, your courier waits beside the shrine's altar. They know the hiding place; at your signal they will show Anevia where to strike. She tests the weight of her hammer.{/n}
"Home after this," {n}Anevia tells the courier.{/n} "You won't be carryin' the Commander's private letters again."
"And no buyer," {n}Kaylessa says.{/n}
"No buyer. Now show me your road."
{n}Kaylessa waits to lead you away. The courier waits for your dismissal; Anevia waits for the signal to smash the drop.{/n}''',
                 ("settle.done", *SUCCESS, "cost.commander_courier", "contact_spent"), seat),
        terminal(step, "spotted", '''{n}Gravel slides beneath your foot. The lookout turns. Anevia pulls you back behind the shrine before he can see your face.{/n}
"Bugger. He'll watch that stone till sunrise now."
{n}Kaylessa has her bow half drawn. Anevia catches the arrow's shaft, not her wrist.{/n} "Not a corpse on the crusade road. That'll bring more of 'em."
{n}Kaylessa lowers the bow.{/n} "Two days, soldier. Then we break it while they're looking. I'm not showing her my road with that trail still open."
{n}The drop remains intact. Neither woman has yielded her advantage.{/n}''',
                 ("settle.failed", "drop_watched"), seat),
        terminal(step, "declined", '''"Can I?" {n}Kaylessa's eyes settle on you. Then she turns to Anevia.{/n} "Watch your buyer. You won't get my road as well."
"Didn't expect I would." {n}Anevia lets her pass. She stays by the table, thinking about the shrine.{/n}
{n}The scout's trail remains open. Kaylessa leaves with her escape route still her own.{/n}''',
                 ("settle.declined", "trail_unsettled"), seat),
    ]


def register(payload, scenes, refs):
    """Register once on the assembled expansion payload, after household integration.

    'scenes' and 'refs' are accepted for the coordinator's common row API.
    Qualified seat membership reads existing commitment terms, never Beth's body.
    """
    if any(s["Id"] == P + "settle.pair" for s in payload["Scenes"]):
        return
    derived = payload.setdefault("Derived", {})
    derived[PAIR_MEMBER] = copy.deepcopy(derived["tirabade.harem.eligible"])
    payload.setdefault("DerivedForbids", {})[PAIR_MEMBER] = [payload["Relationships"]["tirabade"]["ClosedFlag"], "anevia.closed"]
    payload.setdefault("DerivedOpenRoutes", {})[PAIR_MEMBER] = ["anevia"]
    derived.update(copy.deepcopy(STAGE_PRODUCERS))
    for seat in ("pair", "solo"):
        b = "tirabade" if seat == "pair" else "anevia"
        incoming = "kaylessa.harem.enmity.w.anevia"
        outgoing = ("tirabade.harem.enmity.anevia.kaylessa" if seat == "pair" else "anevia.harem.enmity.kaylessa")
        overrides = {
            incoming: "kaylessa.harem.reconciled.w.anevia",
            outgoing: ("tirabade.harem.reconciled.anevia.kaylessa" if seat == "pair" else "anevia.harem.reconciled.kaylessa"),
            "kaylessa.dead": "kaylessa.trickster.returned",
            "anevia_gone": "anevia.trickster.returned",
        }
        pending = payload.setdefault("PendingHooks", [])
        for key in (incoming, outgoing, overrides[incoming], overrides[outgoing]):
            if key not in pending:
                pending.append(key)
        for step in ("settle", "retry"):
            requires = ["trickster", "trickster.now", household.PAGE_TAKEN, household.KEPT, household.STANCE_ELIGIBLE,
                        "kaylessa.harem.eligible", "kaylessa.trickster.returned", "kaylessa.trickster.clock_named",
                        "kaylessa.present_now", "anevia.present_now", "kaylessa.trickster.presence_on",
                        PAIR_MEMBER if seat == "pair" else "anevia.harem.eligible",
                        "kaylessa.committed" if step == "settle" else P + "settle.failed"]
            forbids = ["kaylessa.closed", "kaylessa.trickster.left_free", "inhuman", "kaylessa.dead",
                       "anevia.closed", "anevia_dead", "anevia_gone", "swarm", "true_lich", incoming, outgoing,
                       P + "retry.seen", P + ("settle.seen" if step == "settle" else "settle.declined")]
            if seat == "solo":
                forbids.append(PAIR_MEMBER)
            body = scene(P + step + "." + seat, "A trail outside Drezen", "Kaylessa", 5,
                         "[Kaylessa and Anevia: the scout's trail]" if step == "settle" else "[Kaylessa and Anevia: the watched drop]",
                         nodes(step, seat), requires=requires, forbids=forbids, delay=0 if step == "settle" else 48,
                         last=5, Relationship="household", Chapters=[5], Areas=[household.DREZEN],
                         InteractionHub=household.TABLE_HUB, Participants=["kaylessa", b], Pair=["kaylessa", b],
                         ParticipantWomen=["anevia"] if seat == "pair" else [], ForbidOverrides=overrides,
                         RestAllowance="household.protected", HouseholdCategory="protected",
                         HouseholdWitness=P + step + ".seen")
            payload["Scenes"].append(body)
    add_readers(payload)


def add_readers(payload):
    """Historical book record; guarded coda paragraphs; append-only outdoor reply."""
    line = household._line
    payload["Books"]["trickster.ledger"]["Entries"].append(dict(
        Id=P + "record", Section="Seating Notes", Portrait="Kaylessa", Title="The shrine's trail",
        Text="{n}Kaylessa and Anevia, on the road outside Drezen.{/n}", Requires=[P + "settle.seen"], Forbids=[], AnyGroups=[],
        Lines=[
            line("{n}The drop was watched. The trail is still open.{/n}", [P + "settle.failed"], [P + "retry.seen"]),
            line("{n}Anevia kept the buyer in sight. Kaylessa kept her own way out. Neither handed the other anything.{/n}", [UNRESOLVED_INPUT]),
            line("{n}A buyer lost to the spy, an escape revealed by the fugitive. They closed the trail together.{/n}", [P + "anevia_drop_destroyed", P + "kaylessa_route_shown"]),
            line("{n}My private courier went home for good.{/n}", [P + "cost.commander_courier"]),
            line("{n}Anevia's lookout lost the way into that drop.{/n}", [P + "cost.anevia_lookout_burned"]),
        ]))
    by = {s["Id"]: s for s in payload["Scenes"]}
    for sid in ("anevia.lastcall.page", "tirabade.lastcall.page"):
        if sid not in by:
            continue
        node = by[sid]["Nodes"][0]
        node.setdefault("Paragraphs", []).extend([
            p("{n}Anevia never learned who meant to buy the fugitive's trail. She had broken the shrine's drop herself, or helped burn what lay inside it. When another scout came asking, she could put her watchers on a different road. Kaylessa had shown her the turns.{/n}",
              requires=(P + "cost.anevia_buyer_lost", P + "kaylessa_route_shown", "anevia.present_now")),
            p("{n}The lookout never used that shrine again. Anevia found another place for him; the access she had burned stayed burned.{/n}",
              requires=(P + "cost.anevia_lookout_burned", "anevia.present_now")),
        ])
    for sid in ("kaylessa.trickster.epilogue.commit", "kaylessa.trickster.epilogue.ally"):
        if sid in by:
            by[sid]["Nodes"][0].setdefault("Paragraphs", []).append(p(
                "{n}Kaylessa changed the escape route she had shown Anevia. The spy knew where it had been, and why it had moved; she never sold those turns. Kaylessa still checked behind her when she took the new road.{/n}",
                requires=(P + "cost.kaylessa_private_route", "kaylessa.present_now")))
    host = by.get("kaylessa.clearing.grey_light")
    if host:
        next(node for node in host["Nodes"] if node["Id"] == "now")["Choices"].append(c('"Did you change the road you showed Anevia?"', "s43_road",
            requires=(P + "cost.kaylessa_private_route", "kaylessa.present_now")))
        host["Nodes"].append(n("s43_road", "Kaylessa", '''"Of course. She knows where I used to go. That's enough."
{n}Kaylessa looks down the slope, toward the crusade road.{/n} "She gave up her buyer. I gave up a hiding place. Don't mistake that for giving her all of them, soldier."''', c("[Return to the clearing.]", "now")))
