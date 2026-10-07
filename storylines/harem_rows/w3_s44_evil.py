"""Authored S44 fallen extension, withheld until coordinator metadata review.

HAREM-SHEETS-42-47 row 44 supplies the entire gameplay contract. The shipped
schedule still caps both branches at respect; do not export above that ceiling.
No runtime approval flag, new price, return, echo or reconciliation is invented.
"""
import copy
import json
from pathlib import Path

from story_format import c, n
from storylines import household
from storylines.harem_rows import s44

P = s44.P
ARC = P + "evil"
SCROLL = "89e10c3f21fa50c4b8719e004c7628d3"
STEPS = ("cover", "counterstroke", "choice", "morning")


def flags(*suffixes):
    return tuple(P + suffix for suffix in suffixes)


def metadata_ready():
    """Build-time review only. Missing/old metadata emits nothing.

    The coordinator must approve BOTH the branch ceilings and four-step arc
    allocation in row 44. Merely changing rom cannot activate the extension.
    """
    path = Path(__file__).resolve().parents[2] / "tools/harem-schedule.json"
    row = json.loads(path.read_text(encoding="utf-8"))["rows"]["44"]
    return (row.get("rom") is True and
            row.get("branch_ceilings") == {"arueshalae.redeemed": "respect/respect",
                                          "arueshalae.corrupted": "lover/lover"} and
            row.get("optional_arc") == {"id": ARC, "chapter": 5, "steps": 4})


def result(step, node, speaker, text, suffixes, answer):
    # These deeds are still proposed. Only the terminal answer enacts them;
    # result-node Abort never leaks a secret or earns a witness.
    return n(node, speaker, text,
             c(answer, flags=flags(step + ".seen", *suffixes)), s44.later())


def optional_nodes():
    cover = [
        n("start", "Arueshalae", '''{n}A courtier blocks the upper stair with a purse. Below him, soldiers shout over tomorrow's march to the Worldwound. Shamira turns her returned bracelet on her wrist.{/n}
"He wants to hear how she nearly landed on her face. Offered me gold for it." {n}Arueshalae catches his sleeve before he can approach Shamira.{/n} "I could make the whole tavern laugh. Or I could keep him downstairs. She did open her hand when I asked."''',
          c("[Leave them the quiet side of the court.]", "kept"),
          c('"Make your case to the whole tavern."', "public"), s44.later()),
        result("cover", "kept", "Arueshalae", '''"An ally who can get inside a man's skull is worth more than his purse." {n}Arueshalae tightens her grip on the courtier's sleeve, ready to turn him toward the stairs.{/n} "I'll send him off hungry. You can laugh at somebody else tonight, Shamira."
"Arueshalae," {n}Shamira says, tasting the name.{/n} "I have several candidates."''',
               ("cover.arueshalae_kept", "cost.arueshalae_humiliation_forgone"),
               "[Send the courtier downstairs; Arueshalae keeps the story.]"),
        result("cover", "public", "Shamira", '''{n}The courtier waits with his purse open. Shamira looks from it to you.{/n}
"Tell him, then. Let him choke laughing." {n}Her hand closes around the bracelet.{/n} "But do not come upstairs afterward."''',
               ("cover.exposed", "lust.closed_by_player"),
               "[Tell the courtier about the landing.]"),
    ]
    counterstroke = [
        n("start", "Arueshalae", '''{n}The courtier has returned, buying drinks for soldiers bound for the Worldwound. Arueshalae leans toward Shamira, keeping her voice below the noise.{/n}
"I once had a mortal begging to be ruined. Such a delicious fool. I'll tell you his name upstairs — and what he begged for."
{n}Shamira glances at the drinkers.{/n} "And give me something to tell them when you become tiresome? How generous."''',
          c("[Stay out of their business.]", "kept"),
          c("[Give Shamira the story as ammunition.]", "spoiled"), s44.later()),
        result("counterstroke", "kept", "Shamira", '''"I could have them laughing at you instead. Another succubus with a mouth full of mortal scraps." {n}Shamira steps aside to leave the upper stair clear.{/n} "Tell me upstairs, Arueshalae. I want an ally who bites. I have servants enough."
"Then keep your little audience hungry." {n}Arueshalae smiles, showing her teeth.{/n} "I'm not feeding them for you."''',
               ("counterstroke.shamira_kept", "cost.shamira_ammunition_forgone"),
               "[Leave; Arueshalae tells her privately, and Shamira keeps the boast.]"),
        result("counterstroke", "spoiled", "Shamira", '''{n}Shamira looks toward the courtier and his waiting listeners.{/n}
"You wish to sell her boast? Very well. Call them over."
"Enjoy your audience," {n}Arueshalae says.{/n} "You won't have me upstairs."''',
               ("counterstroke.exposed", "lust.closed_by_player"),
               "[Advertise the boast; Shamira uses it before the court.]"),
    ]
    choice = [
        n("start", "Shamira", '''{n}The soldiers have gone to their billets ahead of the march on the Worldwound. Upstairs, Shamira takes off her bracelet and lays it on the rail beside the cushions. Arueshalae watches her hands.{/n}
"You kept my weakness. I kept yours. Tonight I want you, Arueshalae. No servants. No audience."
"And nobody's creature." {n}Arueshalae draws a claw down the borrowed coat, without touching skin.{/n} "I want what's inside that. Bring the chapel reader and a Death Ward scroll, Commander. Unless you're keeping the gallery for yourself."''',
          c("[Give them the gallery and send for the chapel reader.]", "warded",
            requires=("arueshalae.ward_held",)),
          c('"I want the gallery tonight."', "ordinary"), s44.later()),
        n("warded", "Shamira", '''{n}The chapel reader waits with an open prayer book. Your Death Ward scroll is still rolled. Shamira holds out her hand to the reader; Arueshalae waits beyond arm's reach.{/n}
"Seven minutes," {n}Shamira says.{/n} "Spend your evening elsewhere, Commander. She and I have better uses for mine."
"Then stop wasting it." {n}Arueshalae lets the coat slip from one shoulder.{/n}''',
          c("[Have the reader spend the scroll on Shamira; leave the gallery to them.]",
            "household.pair.shamira_arueshalae.choice.explicit.1",
            flags=flags("choice.seen", "choice.both_yes", "choice.ward_spent", "cost.commander_gallery"),
            requires=("arueshalae.ward_held",), remove_item=SCROLL), s44.later()),
        result("choice", "ordinary", "Arueshalae", '''{n}Arueshalae draws the coat back over her shoulder. Shamira takes her bracelet from the rail.{/n}
"Keep your cushions, then. I'll find my own amusement."
"And I mine," {n}Shamira says.{/n} "The courtier will be disappointed. He still has neither story."''',
               ("choice.declined", "choice.respectful_distance"), "[Keep your evening.]"),
        # Preserve the previously reserved node ID and text exactly. The ward
        # has already been applied by the sole incoming committing answer.
        copy.deepcopy(s44.EXPLICIT_SLOT),
    ]
    choice[-1]["Choices"] = [c("Continue", "after")]
    choice.append(n("after", "Narrator", '''{n}They remain in the empty gallery until the ward's short span is spent. Before it ends, they draw apart. Shamira takes the narrow couch; Arueshalae carries the cushions to the opposite bench.{/n}'''))
    morning = [
        result("morning", "start", "Shamira", '''{n}Dawn brings boots and shouted orders for the Worldwound column below the gallery. Shamira fastens her bracelet. Across the room, Arueshalae sits on the best cushions, pulling her coat into place. Neither has approached the other's bare skin since the ward expired.{/n}
"Those cushions are mine, Arueshalae."
"So was that lovely story. I let you keep it." {n}Arueshalae hugs a cushion against her clothed chest.{/n} "The mortal downstairs would still pay to hear how you stumbled."
"And I could still have him laughing at your little feast." {n}Shamira takes the cushion left on her couch.{/n} "Keep one. Bring the others back before my court assembles."
"Ask nicely." {n}Arueshalae tosses her the smallest.{/n}''',
               ("morning.done", "morning.name_kept"),
               "[Let them finish the quarrel over the cushions.]"),
    ]
    return dict(zip(STEPS, (cover, counterstroke, choice, morning)))


def register(payload, scenes, refs):
    if not metadata_ready():
        return
    # Approval cannot silently raise the existing structural load ceiling.
    # Check the proposed four-step allocation before changing any registry.
    from tools import harem_schedule_lint
    by_id = {s["Id"]: s for s in [*payload.get("Scenes", []), *scenes, *household.ENTRIES]}
    for step in STEPS:
        sid = P + step
        by_id[sid] = dict(Id=sid, HouseholdCategory="pair", RestAllowance="household.pair",
            HouseholdWitness=sid + ".seen", HouseholdArc=ARC,
            HouseholdArcStart=step == "cover", Chapters=[5], MinChapter=5, MaxChapter=5)
    data = json.loads(harem_schedule_lint.DEFAULT_DATA.read_text(encoding="utf-8"))
    load_errors = harem_schedule_lint.scene_load_errors({"Scenes": list(by_id.values())}, data)
    budget_errors = [e for e in load_errors if "optional step sum" in e or "arc has no registered start" in e]
    if budget_errors:
        raise ValueError("S44 optional allocation needs coordinator review: " + "; ".join(budget_errors))
    derived = payload.setdefault("Derived", {})
    negatives = payload.setdefault("DerivedForbids", {})
    for a, b, stage, witnesses in (
        ("shamira", "arueshalae", "friend", ("cover.arueshalae_kept", "arueshalae_ornament_returned")),
        ("arueshalae", "shamira", "friend", ("counterstroke.shamira_kept", "shamira_released")),
        ("shamira", "arueshalae", "lover", ("choice.both_yes", "cover.arueshalae_kept", "counterstroke.shamira_kept")),
        ("arueshalae", "shamira", "lover", ("choice.both_yes", "cover.arueshalae_kept", "counterstroke.shamira_kept")),
    ):
        key = a + ".harem.attitude." + b + "." + stage
        pending = payload.setdefault("PendingHooks", [])
        if key not in pending:
            pending.append(key)
        derived[key] = [["arueshalae.corrupted", *flags(*witnesses)]]
        negatives[key] = [P + "suppressed." + woman for woman in s44.PAIR]
        if stage == "friend":
            lover = a + ".harem.attitude." + b + ".lover"
            negatives[key].append(lover)
            respect = a + ".harem.attitude." + b + ".respect"
            for higher in (key, lover):
                if higher not in negatives.setdefault(respect, []):
                    negatives[respect].append(higher)
    respect = tuple(a + ".harem.attitude." + b + ".respect" for a, b in (s44.PAIR, s44.PAIR[::-1]))
    friend = tuple(a + ".harem.attitude." + b + ".friend" for a, b in (s44.PAIR, s44.PAIR[::-1]))
    lover = tuple(a + ".harem.attitude." + b + ".lover" for a, b in (s44.PAIR, s44.PAIR[::-1]))
    deeds = flags("shamira_released", "arueshalae_ornament_returned")
    contract = {
        "cover": (P + "shamira_released", deeds + respect, flags("retry.declined"), 48),
        "counterstroke": (P + "cover.arueshalae_kept", deeds + flags("cover.arueshalae_kept"), (), 48),
        "choice": (P + "counterstroke.shamira_kept", friend + flags("cover.arueshalae_kept", "counterstroke.shamira_kept"), lover + flags("choice.declined"), 48),
        "morning": (P + "choice.both_yes", flags("choice.both_yes"), (), 8),
    }
    ids = {s["Id"] for s in household.ENTRIES}
    for step, nodes in optional_nodes().items():
        sid = P + step
        if sid in ids:
            continue
        trigger, require, forbid, delay = contract[step]
        body = household.table_entry(sid, "A private advantage", "[Shamira and Arueshalae: the upper gallery]",
            nodes, pair=s44.PAIR, trigger=trigger,
            requires=s44.REQUIRES + ("arueshalae.corrupted",) + require,
            forbids=s44.FORBIDS + flags(step + ".seen", "lust.closed_by_player") + forbid,
            chapters=(5,), delay=delay,
            ParticipantWomen=list(s44.PAIR), RestAllowance="household.pair",
            HouseholdCategory="pair", HouseholdWitness=P + step + ".seen",
            HouseholdArc=ARC, HouseholdArcStart=step == "cover",
            RequiresAnyGroups=[["arueshalae.evil_recruited"]],
            ForbidOverrides={"shamira.killed": "shamira.trickster.returned"})
        # Only starts read Counts; the existing caps pass adds the start guard.
        if step == "cover":
            body["Forbids"].append("household.cap.ch5.arcs")
