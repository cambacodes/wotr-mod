"""Round-2 situations: real decisions, result-specific memories and earned cuts."""
import json
from pathlib import Path
import unittest

from storylines import herrax_house as house
from storylines import herrax_trickster as route


SCENES = {s["Id"]: s for s in [*route.SCENES, *house.SCENES]}


def available(answer, flags):
    return set(answer.get("Requires", ())) <= flags and not set(answer.get("Forbids", ())) & flags


def walk(scene_id, flags, selections):
    event = SCENES[scene_id]
    nodes = {n["Id"]: n for n in event["Nodes"]}
    node = event["Nodes"][0]
    visited = []
    for _ in range(60):
        visited.append(node["Id"])
        answers = [(i, a) for i, a in enumerate(node["Choices"]) if available(a, flags)]
        if not answers:
            raise AssertionError((scene_id, node["Id"], "no selectable answer"))
        index = selections.get(node["Id"], answers[0][0])
        answer = node["Choices"][index]
        if not available(answer, flags):
            raise AssertionError((scene_id, node["Id"], index, "unavailable answer"))
        flags.update(answer.get("Set", ()))
        if not answer.get("Next"):
            return visited, flags
        node = nodes[answer["Next"]]
    raise AssertionError("loop")


class HerraxRound2Tests(unittest.TestCase):
    def test_both_first_nights_reach_slot_and_breakfast(self):
        for suffix, flags in [("reachable", {route.KNIFE_TAKEN, route.BAIT}),
                              ("reachable_restored", {route.RESTORED})]:
            sid = route.H + "madam." + suffix
            for scar_choice in (0, 1):
                visited, final = walk(sid, set(flags), {"offer": 0, "desire": scar_choice})
                self.assertIn(sid + ".explicit.1", visited)
                self.assertIn("morning2", visited)
                self.assertIn(route.COMMITTED, final)
                self.assertIn(route.MORNING, final)

    def test_refusal_never_reaches_intimacy(self):
        for suffix, flags in [("reachable", {route.KNIFE_TAKEN, route.BAIT}),
                              ("reachable_restored", {route.RESTORED})]:
            visited, final = walk(route.H + "madam." + suffix, flags, {"offer": 1})
            self.assertIn(route.CLOSED, final)
            self.assertNotIn(route.COMMITTED, final)
            self.assertFalse(any("explicit" in node for node in visited))

    def test_hand_return_receipt_counts_only_observed_coin_return(self):
        for coin in (False, True):
            flags = {route.HANDED, route.BLOWN}
            if coin:
                flags.add(route.COIN_BACK)
            visited, _ = walk(route.H + "madam.reachable", flags, {})
            self.assertIn("handed_blown" if coin else "handed_blown_no_coin", visited)

    def test_late_face_to_face_decision_precedes_act(self):
        sid = route.H + "epilogue.after_hours.invitation"
        for madam in (False, True):
            offer = "madam_offer" if madam else "rooms_offer"
            for refuse in (False, True):
                visited, flags = walk(sid, {route.MADAM} if madam else set(), {offer: int(refuse)})
                self.assertIn(offer, visited)
                self.assertEqual(refuse, route.CLOSED in flags)
                self.assertEqual(not refuse, route.H + "epilogue.after_hours.explicit.1" in visited)
                self.assertEqual(not refuse, "morning" in visited)
        ending = SCENES[route.H + "epilogue.after_hours"]
        self.assertEqual("scene:" + sid, ending["EpilogueAfter"])
        exit = ending["Nodes"][0]["Choices"][0]
        self.assertEqual("Continue", exit["Text"])
        self.assertFalse(any(exit.get(k) for k in ("Next", "Set", "Requires", "Forbids", "Check", "Abort")))

    def test_repeat_visit_reaches_repeat_slot(self):
        for choice in (0, 1):
            visited, _ = walk(house.STAIRS, {route.COMMITTED}, {"timed": 0, "close": choice})
            self.assertIn(house.STAIRS + ".explicit.1", visited)
            self.assertIn("return_morning", visited)

    def test_late_return_collects_the_missing_act_once(self):
        arrival = SCENES[route.H + "epilogue.after_hours.invitation"]["Nodes"][0]
        cases = [({route.BAIT}, "The sold invitation was still owed"),
                 ({route.BLOWN}, "Rokhorn had exposed the sale"),
                 ({route.RESTORED, route.DECLINED, route.LESSON}, "the house had never gathered"),
                 ({route.RESTORED, route.DECLINED, route.LESSON, "herrax.house.a_night_late"}, "face bore the cut")]
        for flags, expected in cases:
            shown = [p["Text"] for p in arrival["Paragraphs"] if available(p, flags)
                     and all(any(f in flags for f in group) for group in p.get("AnyGroups", ()))]
            self.assertIn(expected, " ".join(shown))
            if "herrax.house.a_night_late" in flags:
                self.assertNotIn("the house had never gathered", " ".join(shown))

    def test_bet_collection_does_not_depend_on_reading_the_packet(self):
        for suffix in ("reachable", "after_hours"):
            page = SCENES[route.H + "epilogue." + suffix]["Nodes"][0]
            receipts = [p for p in page["Paragraphs"] if "Battlebliss" in p["Text"]]
            self.assertTrue(receipts)
            for receipt in receipts:
                self.assertIn(house.BET_LOST, receipt["Requires"])
                self.assertNotIn(house.BUNDLE, receipt["Requires"])
                self.assertNotIn(house.BET_COLLECTED, receipt["Requires"])

    def test_morevet_death_has_no_live_entry_or_unguarded_incoming_edge(self):
        for event in SCENES.values():
            if route.MOREVET_DEAD in event["Forbids"]:
                continue
            self.assertNotIn("Morevet", event["Nodes"][0]["Text"], event["Id"])
            living = {n["Id"] for n in event["Nodes"] if "Morevet" in n["Text"]}
            for node in event["Nodes"]:
                for answer in node["Choices"]:
                    if answer.get("Next") in living or "Morevet" in answer["Text"]:
                        self.assertIn(route.MOREVET_DEAD, answer["Forbids"], (event["Id"], node["Id"]))
                for paragraph in node.get("Paragraphs", ()):
                    if "Morevet" in paragraph["Text"]:
                        self.assertIn(route.MOREVET_DEAD, paragraph["Forbids"])

    def test_folded_discovery_requires_current_body(self):
        for event in SCENES.values():
            for node in event["Nodes"]:
                for answer in node["Choices"]:
                    if answer.get("Next") in ("chiv", "b_chiv"):
                        self.assertIn("chivarro.present_now", answer["Requires"])

    def test_failed_sale_memories_do_not_award_a_sale(self):
        event = SCENES[house.L + "the_courier"]
        by = {n["Id"]: n for n in event["Nodes"]}
        self.assertIn("I tasted the lie", by["reply.con_blown"]["Text"])
        self.assertIn("tried to sell", by["b_offer.con_blown"]["Text"])
        self.assertNotIn("can't cut me", str(SCENES[house.B + "rokhorn.whole"]))

    def test_all_four_briefs_have_reachable_default_nodes(self):
        folder = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/herrax"
        files = list(folder.glob("*.json"))
        self.assertEqual(4, len(files))
        nodes = {n["Id"] for event in SCENES.values() for n in event["Nodes"]}
        for brief in files:
            data = json.loads(brief.read_text(encoding="utf-8-sig"))
            self.assertIn(brief.stem, nodes)
            self.assertEqual(["a man", "a woman"], data["commander_variants"])
            self.assertIn("last_line", data)


if __name__ == "__main__":
    unittest.main()
