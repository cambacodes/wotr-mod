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

    def test_late_return_remembers_completed_punishments(self):
        visit = SCENES[route.H + "epilogue.after_hours.invitation"]
        arrival = visit["Nodes"][0]
        offer = next(n for n in visit["Nodes"] if n["Id"] == "madam_offer")
        self.assertNotIn("You stood where I told you", offer["Text"])
        cases = [({route.BAIT}, "had described the cutting in her letter"),
                 ({route.BLOWN}, "had cut him anyway"),
                 ({route.RESTORED, route.DECLINED, route.LESSON}, "performed her delayed punishment"),
                 ({route.RESTORED, route.DECLINED, route.LESSON, "herrax.house.a_night_late"}, "face bore the cut")]
        for flags, expected in cases:
            shown = [p["Text"] for p in arrival["Paragraphs"] if available(p, flags)
                     and all(any(f in flags for f in group) for group in p.get("AnyGroups", ()))]
            self.assertIn(expected, " ".join(shown))
            if "herrax.house.a_night_late" in flags:
                self.assertNotIn("performed her delayed punishment", " ".join(shown))
            self.assertNotIn("She cut him herself", " ".join(shown))
            self.assertNotIn("Herrax gathered it now", " ".join(shown))

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


    def test_court_question_has_local_answers_before_packet_continues(self):
        event = SCENES[house.COURIER]
        for node_id in ("b_lady", "b_lady_hiding"):
            for lover, closed in ((False, False), (True, False), (True, True)):
                flags = {route.COMMITTED}
                if closed:
                    flags.add("noct.closed")
                if lover:
                    flags.add("noct.complete")
                nodes = {n["Id"]: n for n in event["Nodes"]}
                question = nodes[node_id]
                self.assertEqual("b_news", question["Choices"][0]["Next"])
                self.assertEqual("b_news.morevet_absent", question["Choices"][1]["Next"])
                choices = [a for a in question["Choices"][2:] if available(a, flags)]
                self.assertEqual(3, len(choices))
                truth = next(a for a in choices if house.L + "court.truth" in a["Set"])
                self.assertEqual(lover and not closed, house.L + "court.lover" in truth["Set"])
                self.assertEqual(closed, house.L + "court.former" in truth["Set"])
                for answer in choices:
                    receipt = nodes[answer["Next"]]
                    self.assertTrue(any(available(a, flags) and a.get("Next", "").startswith("b_news") for a in receipt["Choices"]))

    def test_morevet_absence_preserves_sentence_case_and_separate_observer(self):
        import re
        for event in SCENES.values():
            for node in event["Nodes"]:
                for text in [node["Text"], *(p["Text"] for p in node.get("Paragraphs", ()))]:
                    self.assertIsNone(re.search(r'(^|[.!?]\s+|\n|["“])the girl who keeps the arch', text), (event["Id"], node["Id"]))
        night = SCENES[route.H + "madam.the_night"]
        absent = next(n for n in night["Nodes"] if n["Id"] == "arch.morevet_absent")
        self.assertIn("an attendant with her lips parted", absent["Text"])
        self.assertNotIn("the girl who keeps the arch;", absent["Text"])

    def test_all_four_briefs_have_reachable_default_nodes(self):
        folder = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/herrax"
        files = list(folder.glob("*.json"))
        # Four reserved slot nodes; later briefs map to an existing host node (host_scene/host_node).
        self.assertGreaterEqual(len(files), 4)
        nodes = {n["Id"] for event in SCENES.values() for n in event["Nodes"]}
        reserved = 0
        for brief in files:
            data = json.loads(brief.read_text(encoding="utf-8-sig"))
            if brief.stem in nodes:
                reserved += 1
            else:
                host = SCENES[data["host_scene"]]
                self.assertIn(data["host_node"], {n["Id"] for n in host["Nodes"]}, brief.stem)
            self.assertEqual(["a man", "a woman"], data["commander_variants"])
            self.assertIn("last_line", data)
        self.assertEqual(4, reserved)


if __name__ == "__main__":
    unittest.main()
