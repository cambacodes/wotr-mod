import copy
import json
import unittest
from pathlib import Path
from tools.presence_dependency_lint import check, OWNED_ROUTES


class PresenceDependencyTests(unittest.TestCase):
    def test_export_and_mutations(self):
        story = json.loads((Path(__file__).resolve().parents[1] / "development/Story.json").read_text(encoding="utf-8"))
        self.assertEqual([], check(story, OWNED_ROUTES))
        for name in ("camellia.presence", "irabeth.presence", "kaylessa.presence",
                     "minagho_chivarro.presence.minagho", "nurah.presence.cell"):
            bad = copy.deepcopy(story)
            bad["PresenceExceptions"].pop(name)
            self.assertTrue(check(bad), name)

    def test_circular_earned_flag_is_rejected(self):
        story = {"Relationships": {"woman": {"UnavailableOverrides": {"dead": "returned"}}},
                 "Presences": {"woman.presence": {"Unit": "unit", "Requires": ["dead"]}},
                 "Scenes": [{"Id": "return", "Relationship": "woman", "ContactUnit": "unit",
                             "Requires": ["dead"], "Nodes": [{"Choices": [{"Set": ["returned"]}]}]}],
                 "Derived": {"paid": [["returned"]]},
                 "PresenceExceptions": {"woman.presence": {"Overrides": {"dead": {"Flag": "paid"}}}}}
        self.assertTrue(check(story))
        story["Derived"]["paid"] = [["payment"]]
        self.assertEqual([], check(story))

    def test_bootstrap_producer_behind_same_contact_is_circular(self):
        story = {"Relationships": {"woman": {"UnavailableOverrides": {"dead": "returned"}}},
                 "Presences": {"woman.presence": {"Unit": "unit", "Requires": ["dead", "open"]}},
                 "Scenes": [{"Id": "return", "Relationship": "woman", "ContactUnit": "unit",
                             "Requires": ["dead"], "Nodes": [{"Choices": [{"Set": ["returned"]}]}]},
                            {"Id": "pay", "ContactUnit": "unit", "Requires": [],
                             "Nodes": [{"Choices": [{"Set": ["paid"]}]}]}],
                 "Derived": {"open": [["chapter_later"]]}, "DerivedOpenRoutes": {"open": ["woman"]},
                 "PresenceExceptions": {"woman.presence": {"Overrides": {"dead": {"Flag": "paid"}}}}}
        self.assertTrue(check(story))
        story["Scenes"][1].pop("ContactUnit")
        self.assertEqual([], check(story))
        story["Scenes"][1]["ContactUnit"] = "unit"
        story["Derived"]["paid"] = [["pay"]]
        story["Scenes"][1]["Nodes"] = [{"Choices": [{"Set": []}]}]
        self.assertTrue(check(story), "Implicit scene completion can also be circular")
