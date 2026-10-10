"""Targona's earned branches, slot continuations and unavailable endings."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools.crossroute_checks.common import Proof, fields, lit, verify



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result


def only(items):
    """Require a single structural outcome, rejecting gaps and overlap."""
    try:
        outcome, = items
    except ValueError as error:
        raise AssertionError('Expected one structural outcome') from error
    return outcome

class TargonaRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.proof = Proof(verify.Model(cls.story))

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]["Nodes"] if n["Id"] == node)

    def test_all_continuing_endings_reject_incompatible_departure(self):
        for suffix in ("commit", "colleague", "colleague_lost", "ally", "declined",
                       "refused_promise", "furlough", "sacrifice"):
            scene = self.scenes["targona.trickster.epilogue." + suffix]
            gate = fields(scene, overrides=True)
            for loss in ("swarm", "demon", "lich", "devil", "targona.condemned",
                         "targona.dead_lair", "targona.returned_actor_lost"):
                with self.subTest(ending=suffix, loss=loss):
                    self.assertTrue(self.proof.implies(gate, lit(loss, False)))

    def test_refused_promise_remains_a_closed_farewell(self):
        scene = self.scenes["targona.trickster.epilogue.refused_promise"]
        self.assertIn("targona.closed", scene["Requires"])
        self.assertNotIn("targona.outcome.route_open", scene["Requires"])
        self.assertEqual("targona.trickster.returned",
                         scene["ForbidOverrides"]["targona.dead_lab"])

    def test_slots_do_not_create_acceptance_or_night_receipts(self):
        for scene_id, target in (("targona.trickster.after.ward", "morning"),
                                 ("targona.trickster.after.quiet_ward", "morning"),
                                 ("targona.ward_evening", "bell")):
            node = self.node(scene_id, scene_id + ".explicit.1")
            self.assertIsNotNone(only(node["Choices"]))
            answer = by_contract(node['Choices'], [{'Next': 'morning', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}, {'Next': 'bell', 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])
            self.assertEqual(target, answer["Next"])
            self.assertEqual([], answer["Set"])
            self.assertEqual([], answer["Requires"])
            self.assertEqual([], answer["Forbids"])
            self.assertFalse(answer["Abort"])
        for scene_id in ("targona.trickster.after.ward", "targona.trickster.after.quiet_ward"):
            self.assertEqual(["targona.trickster.night_kept"],
                             by_contract(self.node(scene_id, 'morning')['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['targona.trickster.night_kept'], 'Check': None, 'Abort': False, 'Crusade': None}])["Set"])

    def test_first_nights_are_alternatives_and_costs_stay_distinct(self):
        ward = self.scenes["targona.trickster.after.ward"]
        quiet = self.scenes["targona.trickster.after.quiet_ward"]
        self.assertIn("targona.trickster.declined", ward["Forbids"])
        self.assertIn("targona.trickster.declined", quiet["Requires"])
        for scene in (ward, quiet):
            self.assertIn("targona.committed", scene["Forbids"])
        self.assertEqual(["targona.committed"], by_contract(self.node(ward['Id'], 'dawn')['Choices'], [{'Next': 'yes_free', 'Requires': ['targona.trickster.met', 'trickster.now'], 'Forbids': [], 'Set': ['targona.committed'], 'Check': None, 'Abort': False, 'Crusade': None}])["Set"])
        self.assertEqual(["targona.committed", "targona.trickster.cost.light_sealed"],
                         by_contract(self.node(quiet['Id'], 'start')['Choices'], [{'Next': 'promised', 'Requires': ['trickster.now'], 'Forbids': [], 'Set': ['targona.committed', 'targona.trickster.cost.light_sealed'], 'Check': None, 'Abort': False, 'Crusade': None}])["Set"])
        self.assertEqual(["targona.closed"], by_contract(self.node(quiet['Id'], 'start')['Choices'], [{'Next': 'unpromised', 'Requires': [], 'Forbids': [], 'Set': ['targona.closed'], 'Check': None, 'Abort': False, 'Crusade': None}])["Set"])
        spent = self.node("targona.trickster.free.spent_light", "start")["Choices"]
        self.assertEqual(("Favors", -300), (by_contract(spent, [{'Next': 'night', 'Requires': ['trickster.umd_tier2'], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': {'Resource': 'Favors', 'Amount': -300}}])["Crusade"]["Resource"], by_contract(spent, [{'Next': 'night', 'Requires': ['trickster.umd_tier2'], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': {'Resource': 'Favors', 'Amount': -300}}])["Crusade"]["Amount"]))
        self.assertEqual(("Finances", -500), (by_contract(spent, [{'Next': 'night_spent', 'Requires': [], 'Forbids': ['trickster.umd_tier2'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': {'Resource': 'Finances', 'Amount': -500}}])["Crusade"]["Resource"], by_contract(spent, [{'Next': 'night_spent', 'Requires': [], 'Forbids': ['trickster.umd_tier2'], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': {'Resource': 'Finances', 'Amount': -500}}])["Crusade"]["Amount"]))
        self.assertTrue(by_contract(spent, [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': True, 'Crusade': None}])["Abort"])
        self.assertEqual([], by_contract(spent, [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': True, 'Crusade': None}])["Set"])

    def test_text_paragraph_slots_preserve_legacy_exit_mechanics(self):
        from storylines import targona_opening, targona_trickster
        for module, sid, nid in ((targona_opening, "targona.the_open_threshold", "buckles"),
                                  (targona_trickster, "targona.trickster.epilogue.commit", "end")):
            node = self.node(sid, nid)
            self.assertIn(sid + ".explicit.1", module.EXPLICIT_PARAGRAPHS)
            self.assertIsNotNone(only(node["Choices"]))
            self.assertIsNone(by_contract(node['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])["Next"])
            self.assertEqual([], by_contract(node['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])["Set"])
            self.assertFalse(by_contract(node['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])["Abort"])
            self.assertEqual([], by_contract(node['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': [], 'Check': None, 'Abort': False, 'Crusade': None}])["Requires"])

    def test_five_briefs_match_the_production_addresses(self):
        root = Path(__file__).resolve().parents[1] / "tools/route_packs"
        addresses = json.loads((root / "plans/targona-slot-addresses.json").read_text(encoding="utf-8"))
        briefs = [json.loads(p.read_text(encoding="utf-8"))
                  for p in (root / "explicit_slots/targona").glob("*.json")]
        self.assertEqual(set(addresses), {b["slot_id"] for b in briefs})

        for brief in briefs:
            address = addresses[brief["slot_id"]]
            node = self.node(address["scene"], address["node"])
            self.assertEqual(address["node"], node["Id"])
            self.assertTrue(node["Choices"])


if __name__ == "__main__":
    unittest.main()
