"""eng7-l09 / E-Q7-24: authored aftermath wiring for the nine audited nights.

These are local encounter consequences, not new romance requirements or prices.
All native and authored return/closure gates stay on their existing hosts.
"""
import copy
from story_format import c, n

PREFIX = "camellia.trickster.encounter."
MORNINGS = {
    "not_today": ('{n}At dawn the knife is still buried in the window frame. Camellia wakes before the muster bell and tests its edge with her thumb.{/n} '
                  '"Not today," {n}she says, looking at you rather than the blade.{/n} "You may keep yesterday. I shall decide about tomorrow."'),
    "all": ('{n}Morning finds the knife under the bed. Camellia retrieves it, then draws three small crosses on the back of your hand with her fingertip.{/n} '
            '"Three truths. I intend to collect them in front of company." {n}The muster bell interrupts her. She dresses with a pleased, calculating smile.{/n}'),
    "mine": ('{n}Camellia wakes with her knife beside the pillow. She lays its flat against your wrist, watches your pulse, and laughs softly.{/n} '
             '"Still a little afraid. Good. Do not lose that on my account." {n}Outside, soldiers are assembling for the muster. She lifts the knife and lets you rise.{/n}'),
    "knife_off": ('{n}At dawn Camellia steps over the guttered candles and retrieves the knife from the floor. She buckles it high on her thigh while you watch.{/n} '
                  '"You were very careful with my fingers last night. Be as careful in the field. I have further use for yours."'),
    "knife_on": ('{n}The muster bell wakes you on the bare boards. Camellia is already fastening her collar. The knife has never left its strap.{/n} '
                 '"You slept beside it." {n}Her smile widens.{/n} "I watched. You should have seen your face when I moved."'),
}
CALLBACKS = {
    "not_today": '"The knife left a mark in your window frame. Do not have it mended. I like seeing where I put it instead of you."',
    "all": '"You owe me three truths in front of company. I have been choosing the company. Someone who will choke on their breakfast, I think."',
    "mine": '"Your pulse was very quick against my knife that morning. I could feel it through the steel. You need not pretend otherwise."',
    "knife_off": '"I found candle wax on the buckle after our dance. You took such care with it. Next time I shall make you do it in the dark."',
    "knife_on": '"You slept with my knife still strapped to my thigh after the dance. Such confidence. I have been wondering how long you would keep it if I drew the blade."',
}


def integrate(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for suffix in ("", "_camp", "_alive"):
        for family, cuts in (("bond.not_today", {"night": "not_today"}),
                             ("cards.two_lies_again", {"all": "all", "mine": "mine"}),
                             ("day.the_second_dance", {"end": None})):
            host = scenes["camellia.trickster." + family + suffix]
            nodes = {n["Id"]: n for n in host["Nodes"]}
            if family.startswith("day."):
                for node, outcome in (("strap", "knife_off"), ("leave", "knife_on")):
                    nodes[node]["Choices"][0]["Set"].append(PREFIX + outcome)
                    if outcome == "knife_off":
                        nodes[node]["Choices"][0]["Set"].append(host["Id"] + ".knife_off")
            for cut, outcome in cuts.items():
                choice = nodes[cut]["Choices"][0]
                choice["Next"] = "morning." + (outcome or "dance")
                if outcome:
                    choice["Set"].append(PREFIX + outcome)
                    host["Nodes"].append(n(choice["Next"], "Camellia", MORNINGS[outcome],
                                           c("[Rise for the muster.]", flags=(PREFIX + outcome + ".morning",))))
                else:
                    host["Nodes"].append(n("morning.dance", "Narrator", "{n}The muster bell sounds at dawn.{/n}",
                        c("Continue", "morning.knife_off", requires=(host["Id"] + ".knife_off",)),
                        c("Continue", "morning.knife_on", forbids=(host["Id"] + ".knife_off",))))
                    for variant in ("knife_off", "knife_on"):
                        host["Nodes"].append(n("morning." + variant, "Camellia", MORNINGS[variant],
                                               c("[Rise for the muster.]", flags=(PREFIX + variant + ".morning",))))
        # The existing optional breakfast can be played after these encounters.
        # Its old answer and node remain; appended variants read only actual nights.
        breakfast = scenes["camellia.trickster.evening.breakfast" + suffix]
        opening = breakfast["Nodes"][0]
        opening["Choices"][0]["Text"] = '"What did you tell the cook?"'
        original = copy.deepcopy(opening["Choices"][0])
        opening["Choices"][0]["Forbids"].extend(PREFIX + outcome + ".morning" for outcome in MORNINGS)
        for outcome in MORNINGS:
            answer = copy.deepcopy(original)
            answer["Text"] = {
                "not_today": '"Did you look at the mark in the window frame this morning?"',
                "all": '"Have you chosen who will hear my three truths?"',
                "mine": '"Are you still thinking about my pulse against your knife?"',
                "knife_off": '"Was the candle wax on the buckle difficult to remove?"',
                "knife_on": '"Did you enjoy watching me sleep beside your knife?"',
            }[outcome]
            answer["Next"] = "encounter." + outcome
            answer["Requires"].append(PREFIX + outcome + ".morning")
            opening["Choices"].append(answer)
            breakfast["Nodes"].append(n("encounter." + outcome, "Camellia", CALLBACKS[outcome], c('"And what did you tell the cook?"', "cook")))
    from storylines import camellia_round2
    camellia_round2.integrate(payload)
