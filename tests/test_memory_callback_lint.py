import copy
from tests.story_fixture import fresh_story
import json
import unittest
from tools import memory_callback_lint as lint


class MemoryCallbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = fresh_story()

    def test_every_incoming_choice_and_twin(self):
        result = lint.check(self.story)
        self.assertFalse(result["hard"], result["hard"])
        # eng8-q8f: gameplay now supplies the awning twin; both sold-memory edges must execute.
        self.assertEqual(len(result["executed"]), 8)
        self.assertEqual(result["no_change_needed"], [])
        # end eng8-q8f

    def test_absent_third_bell_twin_is_checked_if_supplied_as_fixture(self):
        # eng8-q8f: remove the shipped twin before supplying the isolated mutation fixture.
        fixture = {"Scenes": [s for s in self.story["Scenes"]
                              if s["Id"] != "terendelev.trickster.watch.third_bell_awning"]}
        # end eng8-q8f
        twin = copy.deepcopy(next(s for s in self.story["Scenes"] if s["Id"] == "terendelev.trickster.watch.third_bell"))
        twin["Id"] += "_awning"
        fixture["Scenes"].append(twin)
        result = lint.check(fixture)
        self.assertFalse(result["hard"], result["hard"])
        self.assertEqual(len(result["executed"]), 8)
        twin["Nodes"] = [n for n in twin["Nodes"] if n["Id"] != "gap.gate"]
        self.assertTrue(lint.check(fixture)["hard"])

    def test_all_prices_heard_and_unheard(self):
        from storylines import foresight as f
        scenes = {s["Id"]: s for s in self.story["Scenes"]}
        for contract in json.loads(lint.CONTRACTS.read_text(encoding="utf-8")):
            if contract["scene"] not in scenes:
                continue
            nodes = {n["Id"]: n for n in scenes[contract["scene"]]["Nodes"]}
            for via, index in contract["vias"]:
                old = nodes[via]["Choices"][index]
                for price in (None, f.COST_PROMISE, f.COST_SQUARE, f.COST_CAVES):
                    for heard in (False, True):
                        flags = {"trickster.ever", f.ACCEPTED}
                        if price:
                            flags.add(price)
                        if heard:
                            flags.add("terendelev.voice_heard")
                        for key, groups in f.DERIVED.items():
                            if any(set(group).issubset(flags) for group in groups):
                                flags.add(key)
                        flags.update(old["Requires"])
                        incoming = [i for n, i in contract["vias"] if n == via]
                        alternatives = [c for c in nodes[via]["Choices"]
                                        if c.get("Next") == "gap." + contract["node"]]
                        self.assertEqual(len(alternatives), len(incoming))
                        twin = alternatives[incoming.index(index)]
                        self.assertEqual(lint.structural(twin), lint.structural({
                            **old, "Next": "gap." + contract["node"],
                            "Requires": list(dict.fromkeys(old["Requires"] + ["trickster.ever", contract["gone"]])),
                            "Forbids": [f for f in old["Forbids"] if f != contract["gone"]]}))
                        candidates = [old, twin]
                        shown = [c for c in candidates if set(c["Requires"]).issubset(flags) and not set(c["Forbids"]) & flags]
                        self.assertEqual(len(shown), 1, (contract["scene"], via, price, heard))
                        expected = "gap." + contract["node"] if f.GONE_SQUARE in flags else contract["node"]
                        self.assertEqual(shown[0]["Next"], expected)

    def test_guard_continuation_and_twin_mutations(self):
        contracts = json.loads(lint.CONTRACTS.read_text(encoding="utf-8"))
        for contract in contracts:
            if not any(s["Id"] == contract["scene"] for s in self.story["Scenes"]):
                continue
            for mutation in ("guard", "gap", "continuation"):
                story = {"Scenes": [copy.deepcopy(s) if s["Id"] == contract["scene"] else s for s in self.story["Scenes"]]}
                nodes = {n["Id"]: n for n in next(s for s in story["Scenes"] if s["Id"] == contract["scene"])["Nodes"]}
                if mutation == "guard":
                    via, index = contract["vias"][0]
                    nodes[via]["Choices"][index]["Forbids"].remove(contract["gone"])
                elif mutation == "gap":
                    nodes["gap." + contract["node"]]["Id"] = "missing_gap"
                else:
                    nodes["gap." + contract["node"]]["Choices"] = []
                self.assertTrue(lint.check(story, [contract])["hard"], mutation)
