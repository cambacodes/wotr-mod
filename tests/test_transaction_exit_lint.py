import copy
from tests.story_fixture import fresh_story
from tools.rrt_verify import Model as check_model, Reach as check_reach
import unittest
from tools import transaction_exit_lint as lint


class TransactionExitLintTests(unittest.TestCase):
    def test_node_entry_is_a_producer_before_an_unselectable_payment(self):
        from tools import rrt_verify as verifier
        fixture_data = {"Scenes": [{"Id": "fixture", "Relationship": "fixture", "Remote": True, "Nodes": [
            {"Id": "start", "Text": "{n}A bill.{/n}", "EnterSet": ["debt"],
             "Choices": [{"Text": "[Pay.]", "Requires": ["debt"], "Crusade": {"Resource": "Finances", "Amount": -200}}]}]}],
            "Relationships": {"fixture": {"StartedFlag": "started", "ClosedFlag": "closed", "CommittedFlag": "committed"}}}
        model = check_model(fixture_data)
        self.assertIn(("fixture", "start", "enter"), model.producers["debt"])
        reach = check_reach(model, verifier.mythic_world("trickster", model))
        self.assertIn("debt", reach.held)
        self.assertIn(("fixture", "start", "enter"), reach.choices)

    @classmethod
    def setUpClass(cls):
        import expansion
        cls.scene = next(s for s in fresh_story()["Scenes"] if s["Id"] == lint.CONTRACTS[0]["scene"])

    def test_contract_and_mutations(self):
        self.assertFalse(lint.check({"Scenes": [self.scene]}, lint.CONTRACTS))
        for mutation in ("entry", "settlement", "reroll", "agreement", "reentry"):
            scene = copy.deepcopy(self.scene)
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            if mutation == "entry":
                nodes["raised"]["EnterSet"] = []
            elif mutation == "settlement":
                nodes["raised"]["Choices"][0]["Set"] = []
            elif mutation in {"reroll", "agreement"}:
                nodes["rent"]["Choices"][int(mutation == "reroll")]["Forbids"] = []
            else:
                nodes["start"]["Choices"] = [c for c in nodes["start"]["Choices"] if c.get("Next") != "raised"]
            self.assertTrue(lint.check({"Scenes": [scene]}, lint.CONTRACTS), mutation)
