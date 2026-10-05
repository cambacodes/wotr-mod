"""eng8-q8c / E-Q8-09: every registered receipt/exclusion/payment mutation fails."""
from tests.story_fixture import fresh_story
import copy
import unittest
from tools import transaction_exit_lint as lint


class TransactionInventory2LintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = fresh_story()

    def test_registered_inventory_and_negative_mutations(self):
        self.assertFalse(lint.check(self.story))
        for sid in ("arsinoe.trickster.cauldron.collection", "arsinoe.trickster.cauldron.lease", "horzalah.trickster.late.at_night"):
            missing = copy.deepcopy(self.story)
            missing["Scenes"] = [s for s in missing["Scenes"] if s["Id"] != sid]
            self.assertTrue(lint.check(missing), sid)
        for index in range(3):
            for field in ("Set", "Forbids", "resume-requires", "resume-forbids"):
                story, nodes = self.changed("arsinoe.trickster.cauldron.collection")
                choice = nodes["pledge"]["Choices"][index + (3 if field.startswith("resume") else 0)]
                choice[{"resume-requires": "Requires", "resume-forbids": "Forbids"}.get(field, field)] = []
                self.assertTrue(lint.check(story), (index, field))
        for outcome in ("discount", "raised"):
            story, nodes = self.changed("arsinoe.trickster.cauldron.lease")
            nodes[outcome]["EnterSet"] = []
            self.assertTrue(lint.check(story), outcome)
        for field in ("Set", "Forbids", "Crusade"):
            story, nodes = self.changed("arsinoe.trickster.cauldron.lease")
            nodes["terms"]["Choices"][0][field] = [] if field != "Crusade" else {"Resource": "Finances", "Amount": -499}
            self.assertTrue(lint.check(story), ("initial payment", field))
        for index in (0, 1):
            for receipt in ("arsinoe.trickster.cost.rent_grace", "arsinoe.trickster.cost.rent_raised"):
                story, nodes = self.changed("arsinoe.trickster.cauldron.lease")
                nodes["rent"]["Choices"][index]["Forbids"].remove(receipt)
                self.assertTrue(lint.check(story), (index, receipt))
        for target in ("discount", "raised"):
            story, nodes = self.changed("arsinoe.trickster.cauldron.lease")
            nodes["start"]["Choices"] = [c for c in nodes["start"]["Choices"] if c.get("Next") != target]
            self.assertTrue(lint.check(story), target)
        for consumer in ("arsinoe.trickster.epilogue.bill_to_threshold", "arsinoe.trickster.epilogue.pot_returned"):
            story, nodes = self.changed(consumer)
            nodes["end"]["Paragraphs"] = [p for p in nodes["end"]["Paragraphs"] if "arsinoe.trickster.cost.rent_grace" not in p.get("Requires", [])]
            self.assertTrue(lint.check(story), consumer)
        for receipt in ("horzalah.trickster.cost.ear", "horzalah.trickster.cost.late"):
            story, nodes = self.changed("horzalah.trickster.late.at_night")
            nodes["cut"]["EnterSet"].remove(receipt)
            self.assertTrue(lint.check(story), receipt)
        for mutation in ("payment", "amount", "receipt", "resume", "guard", "paid-scene", "unpaid-entry", "bypass"):
            story, nodes = self.changed("horzalah.trickster.late.at_night")
            pay = nodes["no_priest"]["Choices"][0]
            if mutation == "payment": pay.pop("Crusade")
            if mutation == "amount": pay["Crusade"]["Amount"] = -99
            if mutation == "receipt": pay["Set"].remove("horzalah.trickster.primed")
            if mutation == "resume": nodes["start"]["Choices"].pop()
            if mutation == "guard": nodes["start"]["Choices"][3]["Forbids"].remove("horzalah.trickster.cost.ear")
            if mutation == "paid-scene": next(s for s in story["Scenes"] if s["Id"] == "horzalah.trickster.late.at_night")["Forbids"].remove("horzalah.trickster.primed")
            if mutation == "unpaid-entry": nodes["cut"]["EnterSet"].append("horzalah.trickster.primed")
            if mutation == "bypass": nodes["cut"]["Choices"].append({"Text": "Free completion", "Set": ["horzalah.trickster.primed"]})
            self.assertTrue(lint.check(story), mutation)

    def changed(self, sid):
        story = copy.deepcopy(self.story)
        scene = next(s for s in story["Scenes"] if s["Id"] == sid)
        return story, {n["Id"]: n for n in scene["Nodes"]}
