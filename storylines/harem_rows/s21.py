"""S21: authored friendship watch, hs-D §8d; no native rewrite or intimacy.

Native voice anchors (verified in /wrath/blueprints.zip and enGB.json):
TrueYaniel/Cue_0003, fd994112dc80453a954e9486f4668d36, key
3c028426-3eb5-4950-aeba-3e3ece492419 (Seelah's rescue acknowledgment);
TrueYaniel/Cue_2, 619dd81e8cd04918a2766a2920a6e351, key
40b33957-8853-440e-9123-93de74f1b691 (Yaniel's answer).
The existing yaniel.seelah_sister read belongs to Cue_0003, never Cue_2.
The watch and all its deed/cost witnesses are authored additions. Attitude,
disappointment and reconciliation producers remain the integrator's property.
"""
from story_format import c, n, scene
from storylines import household, foresight

P = "household.pair.seelah_yaniel."
PAIR = ("seelah", "yaniel")
FRIENDS = ("seelah.harem.attitude.yaniel.friend",
           "yaniel.harem.attitude.seelah.friend")
KEPT = tuple(P + suffix for suffix in (
    "watch.seen", "watch.kept", "deed.yaniel_directed_watch",
    "deed.seelah_followed_direction", "cost.yaniel_spent_legend",
    "cost.seelah_left_praise"))


def register(payload, scenes, refs):
    """Register once per payload and declare the paid-page consumer."""
    if any(s["Id"] == P + "watch" for s in scenes):
        return
    payload.setdefault("Derived", {})[P + "ready"] = [[
        "yaniel.trickster.returned", "seelah.harem.eligible", "yaniel.harem.eligible"]]
    pending = payload.setdefault("PendingHooks", [])
    edges = [household.enmity(a, b) for a, b in (PAIR, PAIR[::-1])]
    for flag in (*FRIENDS, *edges,
                 *(edge.replace(".enmity.", ".reconciled.") for edge in edges)):
        if flag not in pending:
            pending.append(flag)
    body = scene(P + "watch", "The veteran takes the watch", "Seelah", 5,
        '[Seelah and Yaniel: the gate watch]', [
        n("start", "Seelah", '''{n}Seelah has left her shield against the table. Yaniel stands beside it, still wearing her cloak. Outside, the relief bell rings over the tavern's noise.{/n}
"We're short on the east gate tonight. Yaniel offered to take it. I'd like to go with her."
{n}Yaniel pulls the cloak's clasp tight.{/n} "Offered? I told the sergeant I'd take it. Too many tired men staring toward the Wound, and nobody watching what comes through the gate. Come and see the post, Commander. Your paladin wants to help. I have work for her."''',
            c('"Take Yaniel\'s direction."', "history"),
            c('"Another watch."', "declined"),
            c('[Later.]', abort=True)),
        n("history", "Narrator", '''{n}They collect Seelah's shield and lead you out to the gate. A wagon waits beneath the arch; its wounded driver has fallen asleep against the reins. Yaniel wakes the corporal beside him and sends him to fetch the relief.{/n}''',
            c(next="sister", requires=("yaniel.seelah_sister",)),
            c(next="unheard", forbids=("yaniel.seelah_sister",))),
        n("sister", "Seelah", '''"When I called you sister in the Fane, I never thought we'd stand a watch together."
{n}Yaniel looks up the stair, where two sentries are arguing over a lantern.{/n} "We will, if you stop looking at me and climb."''', c(next="equipment")),
        n("unheard", "Seelah", '''"I've wanted to fight beside you for a long time."
{n}Yaniel points to the stair.{/n} "Then get up there. There's a gate between us and the demons. I'd like to keep it."''', c(next="equipment")),
        n("equipment", "Narrator", '''{n}At the parapet Yaniel checks the approach, then the men below. Seelah follows her gaze.{/n}''',
            c(next="veteran_blade", requires=("yaniel.trickster.carries",)),
            c(next="party_blade", requires=("yaniel.radiance_in_party",),
              forbids=("yaniel.trickster.carries",)),
            c(next="stored_blade", requires=("yaniel.radiance_held",),
              forbids=("yaniel.trickster.carries", "yaniel.radiance_in_party")),
            c(next="empty", forbids=("yaniel.trickster.carries", "yaniel.radiance_held",
                                     "yaniel.radiance_in_party"))),
        n("veteran_blade", "Seelah", '''{n}Radiance rests at Yaniel's hip. Seelah's eyes linger on the plain scabbard.{/n} "That sword, back on this wall..."
"That gate," {n}Yaniel interrupts.{/n} "Praise the sword when you've counted the men coming through it."''', c(next="directed")),
        n("party_blade", "Yaniel", '''{n}Yaniel glances at Radiance among your company's weapons, then turns Seelah toward the arch below.{/n} "The sword has someone to carry it. Those men need someone watching their backs. Count them."''', c(next="directed")),
        n("stored_blade", "Yaniel", '''"Radiance isn't here. We'll use what is. Count the men coming through that gate. The corporal waved the last wagon in without looking underneath it."''', c(next="directed")),
        n("empty", "Yaniel", '''{n}Yaniel takes a spear from the rack and tests its shaft against the stone.{/n} "This will do. Count the men coming through that gate. Watch their hands, too."''', c(next="directed")),
        n("directed", "Seelah", '''"Right. You take the left. I'll take the right."
{n}Seelah goes down to the arch. She stops the next wagon, crouches behind her shield and searches beneath its bed. Above her, Yaniel directs the sentries onto the unlit stretch of wall. A soldier starts to salute her; she puts him to work carrying the spare lantern instead.{/n}
"I can stay until the relief," {n}Seelah calls up.{/n}
"So can I. Tell the sergeant he can stop saving a chair for me."
{n}Yaniel settles beside the embrasure. Seelah gives her the count, then turns to the next wagon. Neither follows you back to the tavern.{/n}''', c(flags=KEPT)),
        n("declined", "Yaniel", '''"Then find the sergeant another pair of hands. He asked for two."
{n}Seelah takes up her shield.{/n} "We brought you a watch we could hold together. All right. I'll ask him where he needs me."
{n}Yaniel leaves first. Seelah waits long enough to sling her shield, then goes after her.{/n}''',
            c(flags=(P + "watch.seen", P + "watch.declined"))),
        ], requires=("trickster", household.PAGE_TAKEN, household.KEPT,
                     household.STANCE_ELIGIBLE, P + "ready", *FRIENDS,
                     "seelah.present_now", "yaniel.present_now", "yaniel.freed.latched",
                     "yaniel.trickster.returned"),
        forbids=("household.closed", "fool_king.gone", "trickster.failed",
                 "engine.l12.commander_unreturned", "yaniel.closed", "seelah.closed",
                 "yaniel.killed.latched", "yaniel.trickster.left_free",
                 "yaniel.presence.failed", P + "watch.seen", *edges),
        last=5, optional=True, Relationship="household", Chapters=[5],
        Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
        Participants=list(PAIR), Pair=list(PAIR), RestAllowance="household.pair",
        HouseholdCategory="dynamic", HouseholdWitness=P + "watch.seen",
        ForbidOverrides={edge: edge.replace(".enmity.", ".reconciled.") for edge in edges})
    scenes.append(body)
    foresight.CONSUMERS[body["Id"]] = household.PAGE_TAKEN
