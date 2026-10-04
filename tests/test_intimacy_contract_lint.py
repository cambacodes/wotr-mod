import copy
import unittest
from tools import intimacy_contract_lint as lint


class IntimacyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = expansion.make_expansion()

    def test_every_cut_declaration_and_knife_variant(self):
        result = lint.check(self.story)
        self.assertEqual(result["hard"], [])
        self.assertEqual(len(result["executed"]), 15)
        self.assertTrue(all(r["morning"] and r["callback"] for r in result["executed"]))

    def test_every_prior_history_and_no_callback_before_morning(self):
        import itertools
        import json
        scenes = {s["Id"]: s for s in self.story["Scenes"]}
        for contract in json.loads(lint.CONTRACTS.read_text()):
            host = scenes[contract["scene"]]
            prior = sorted({f for n in host["Nodes"] for c in n["Choices"] for f in c.get("Requires", []) + c.get("Forbids", [])
                            if not f.startswith("camellia.trickster.encounter.")})
            for mask in itertools.product((False, True), repeat=len(prior)):
                witness = {**contract, "flags": [f for f, held in zip(prior, mask) if held]}
                self.assertFalse(lint.check(self.story, [witness])["hard"], (contract["scene"], witness["flags"]))
            callback = scenes[contract["callback_scene"]]
            self.assertFalse(any(contract["callback_node"] in path for path, _ in lint.walks(callback)), contract["scene"])

    def test_deleting_morning_or_reader_fails_each_contract(self):
        import json
        contracts = json.loads(lint.CONTRACTS.read_text())
        for contract in contracts:
            for mutation in ("morning", "callback"):
                sid = contract["scene"] if mutation == "morning" else contract["callback_scene"]
                story = {"Scenes": [copy.deepcopy(s) if s["Id"] == sid else s for s in self.story["Scenes"]]}
                scene = next(s for s in story["Scenes"] if s["Id"] == sid)
                if mutation == "morning":
                    next(n for n in scene["Nodes"] if n["Id"] == contract["cut"])["Choices"][0]["Next"] = None
                else:
                    scene["Nodes"] = [n for n in scene["Nodes"] if n["Id"] != contract["callback_node"]]
                self.assertTrue(lint.check(story, [contract])["hard"], (contract["scene"], mutation))
