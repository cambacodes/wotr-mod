"""Earned situation receipts and transparent heated-cut slots."""
import json
from pathlib import Path
import unittest

from storylines import minagho_round2 as route
from tools import rrt_verify

ROOT = Path(__file__).resolve().parents[1]


class MinaghoRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8-sig"))
        cls.pages = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = rrt_verify.Model(cls.story)

    def state(self, *flags):
        state = rrt_verify.SimState(5, 5000)
        state.flags.update(("chapter_later", "trickster", "trickster.ever", *flags))
        rrt_verify.sim_complete(self.model, state)
        return state

    def test_killer_cannot_buy_affection_with_scar_or_transfer(self):
        base = ("chivarro.dead", "chivarro.exile_objective_done", route.P + "minagho_in",
                route.P + "cost.palm_scar", route.P + "cost.scar_burned")
        self.assertNotIn(route.RECEIPT, self.state(*base).flags)
        self.assertIn(route.RECEIPT, self.state(*base, route.RINGS).flags)
        self.assertIn(route.RECEIPT, self.state(*base, route.P + "chivarro_deposit").flags)
        for page in self.pages.values():
            if page["Id"].startswith(route.P + "alone.minagho"):
                for node in page["Nodes"]:
                    for answer in node["Choices"]:
                        if "minachiv.complete" in answer["Set"]:
                            self.assertIn(route.RECEIPT, answer["Requires"], (page["Id"], node["Id"]))

    def test_rings_receipt_is_produced_only_after_her_burial(self):
        producers = [(s["Id"], n["Id"], a) for s in self.story["Scenes"] for n in s["Nodes"]
                     for a in n["Choices"] if route.RINGS in a["Set"]]
        self.assertEqual(len(producers), 4)
        for sid, nid, _ in producers:
            self.assertEqual(nid, "rings_burial")
            page = self.pages[sid]
            nodes = {n["Id"]: n for n in page["Nodes"]}
            offer = next(a for a in page["Nodes"][0]["Choices"] if a["Next"] == "rings_demand")
            self.assertIn("chivarro.dead_confirmed", offer["Requires"])
            self.assertIn(route.P + "chivarro_deposit", offer["Forbids"])
            self.assertNotIn(route.RINGS, nodes["rings_purchase"]["Choices"][0]["Set"])
            self.assertTrue(nodes["rings_purchase"]["Choices"][1]["Abort"])

    def test_departure_gets_both_answers_only_after_rejection(self):
        page = self.pages[route.P + "reunion.wardrobe"]
        nodes = {n["Id"]: n for n in page["Nodes"]}
        for nid in ("which", "which_debt"):
            answer = next(a for a in nodes[nid]["Choices"] if route.P + "chivarro_sent_back" in a["Set"])
            self.assertIn(route.P + "chivarro_sent_back", answer["Set"])
            self.assertEqual(answer["Next"], "departure_answer")
        self.assertIn("Not from me", nodes["departure_answer"]["Text"])

    def test_all_46_briefs_have_reachable_slots_and_no_new_effect(self):
        paths = sorted((ROOT / "tools/route_packs/explicit_slots/minagho").glob("*.json"))
        self.assertEqual(len(paths), 46)
        for path in paths:
            brief = json.loads(path.read_text(encoding="utf-8"))
            page = self.pages[brief["source"]["scene"]]
            nodes = {n["Id"]: n for n in page["Nodes"]}
            slot = nodes[brief["slot_id"]]
            self.assertTrue(any(a["Next"] == slot["Id"] for n in page["Nodes"] for a in n["Choices"]))
            self.assertIn(brief["default_text"], slot["Text"])
            self.assertTrue(all(not a["Set"] and not a.get("Crusade") for a in slot["Choices"]))

    def test_years_rent_refusal_refunds_and_letter_nights_pay_once(self):
        page = self.pages[route.P + "alone.chivarro_when_it_scars"]
        nodes = {n["Id"]: n for n in page["Nodes"]}
        debit = nodes["start"]["Choices"][0]["Crusade"]["Amount"]
        refund = nodes["chv"]["Choices"][1]["Crusade"]["Amount"]
        self.assertEqual(debit + refund, 0)
        self.assertNotIn("send a runner", nodes["start"]["Text"])
        page = self.pages[route.P + "alone.chivarro_letter"]
        for node in page["Nodes"]:
            for answer in node["Choices"]:
                if route.P + "night.chivarro" in answer["Set"]:
                    self.assertEqual(answer["Crusade"], dict(Resource="Finances", Amount=-100))

    def test_later_commitment_cannot_overwrite_trickster_arrangement(self):
        self.assertIn(route.P + "committed", self.pages["minachiv.before_the_last_road"]["Forbids"])


if __name__ == "__main__":
    unittest.main()
