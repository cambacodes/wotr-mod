"""D2: append inline history readers without changing saved answer targets."""
from copy import deepcopy

from story_format import c, n


# Scene, host, appended node, positive history, negative history, node text.
PURCHASED = ("""{n}Before you can answer, she drags something across the floor with one claw and lets it fall at your feet: a saddle, the staff picket's brand burned into the skirt, the girth still wet.{/n}
"Your generals bought a battle from me. I have not chosen one. I will not. Nothing in this war has been worth my wings." {n}A horse's skull lies in the row of small bones by the door, the brand grinning on its cheek, and beside it a pair of cavalry boots set down neatly, sorted with the rest.{/n} "I told them I would take the difference out of them while I decided. A horse a week. The last who climbed up here to complain brought me the horse himself, to save time." {n}She licks her teeth.{/n} "He walked down. Only just. They can keep waiting. Waiting is good for generals.\"""")
VOLUNTARY = ("""{n}Before you can answer, she lifts her head, and the smell reaches you ahead of the words: char, and under it fat, and something sweet that used to be a man.{/n}
"Your scouts found a road on the Wound side burned black for a mile. A demon column was standing in it. Cooked." {n}Her claws open on the stone, and a scrap of blackened mail drops from between them.{/n} "That was my battle. Where I chose, when I chose, against what I chose. I took them in the dark with their fires lit and their sentries watching each other's backs, and I did not hurry. The ones in front I burned where they stood. The ones behind ran, and I was fond of the ones who ran." {n}She works something loose from a back tooth.{/n} "Nobody thanked me. Good. Do not start.\"""")
WARNING = ("""{n}Her tail takes your legs out from under you before you can answer. She pins you to the floor among the small bones with one claw across your chest, not quite hard enough to break anything, and lets the edge of it rest where you can feel it.{/n}
"That is twice, crusader. I said once." {n}A rib creaks. She leans one more finger's weight into it and holds it there, watching your face while the bone bends.{/n} "You say that word to me as though I might come to like it. I do not. I like you, a little, and I am beginning to resent that." {n}The weight lifts. Something small cracks under her foot as she steps off you, and she does not look down.{/n} "The third time I will not be speaking.\"""")
HONEST = ("""{n}Then she hooks the smallest coin out of the heap, a clipped copper nobody would stoop for in a gutter, and flicks it at your chest. It stings. It leaves a mark.{/n}
"For the chamber. For the stone with your hand in its mouth. You told me I owed you." {n}Her lip lifts off one long tooth.{/n} "Dragons are owed. Dragons do not owe. But a dragon pays what she decides she must, in the coin she chooses, and that is the coin." {n}It rolls across the floor to your boot and stops.{/n} "I told you that you would not like it. Spend it on something small, crusader. I will know what you bought.\"""")
STEAL = ("""{n}A second coin follows the Queen without her looking at it, a clipped copper, and rings off your cuff.{/n}
"And that settles what you said I owed you, for the stone in the chamber. You took your payment out of my own heap with my eye on you. It saves me the insult of choosing it." {n}Her tail slides along the floor and rests across your ankle, not tight.{/n} "Be glad it was only a coin you took. I count everything I own. I have counted you in.\"""")
ASK = ("""{n}A second coin follows the first, a clipped copper, and rings off your boot.{/n}
"That one is not a gift. That is what I owed you, for the chamber and the stone. You said I owed. I pay what I owe in the coin I choose, and I choose this one, and now you can never say I did not pay." {n}Her eye opens a slit.{/n} "Put them in the same pocket. Let them rub together. Let them remember what each was for.\"""")
READERS = (
    ("before_the_end", "climb", "rubric2_purchased_battle",
     ("devarra.tower.one_battle_sold", "devarra.tower.battle_price_accepted"), (), PURCHASED),
    ("before_the_end", "climb", "rubric2_voluntary_battle",
     ("devarra.tower.battle_offered",), ("devarra.tower.battle_price_accepted",), VOLUNTARY),
    ("the_dwarf", "protect", "rubric2_protection_warning",
     ("devarra.tower.warned",), (), WARNING),
    ("the_hoard", "honest_her", "rubric2_clutch_debt_honest_her",
     ("devarra.trickster.debt_claimed",), (), HONEST),
    ("the_hoard", "steal_her", "rubric2_clutch_debt_steal_her",
     ("devarra.trickster.debt_claimed",), (), STEAL),
    ("the_hoard", "ask_her", "rubric2_clutch_debt_ask_her",
     ("devarra.trickster.debt_claimed",), (), ASK),
)


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    grouped = {}
    for suffix, host, node, requires, forbids, beat in READERS:
        grouped.setdefault((suffix, host), []).append((node, requires, forbids, beat))
    for (suffix, host), readers in grouped.items():
        scene = scenes["devarra.tower." + suffix]
        if any(node["Id"] == readers[0][0] for node in scene["Nodes"]):
            continue
        target = next(node for node in scene["Nodes"] if node["Id"] == host)
        original = deepcopy(target["Choices"])
        keys = []
        for node_id, requires, forbids, beat in readers:
            key = "devarra.rubric2." + node_id
            payload.setdefault("Derived", {})[key] = [list(requires)]
            if forbids:
                payload.setdefault("DerivedForbids", {})[key] = list(forbids)
            keys.append(key)
            # The host's path/presence guards and each saved answer's gates
            # remain authoritative on both sides of this mandatory readback.
            target["Choices"].append(c("Continue", node_id, requires=(key,)))
            scene["Nodes"].append(n(node_id, "Devarra",
                beat, *deepcopy(original)))
        for choice in target["Choices"][:len(original)]:
            choice["Forbids"].extend(keys)
