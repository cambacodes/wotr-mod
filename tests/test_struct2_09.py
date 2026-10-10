"""struct2-09: exported hosting, returned-ending and pending-prose contracts."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tools import prose_pending_lint

ROOT = Path(__file__).resolve().parents[1]



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

class Structure09Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {scene["Id"]: scene for scene in cls.story["Scenes"]}

    def test_ember_afternoons_use_current_drezen_companion(self):
        for suffix in ("drawing", "visitor", "rain", "paper_bird", "missing_cloth",
                       "courtyard_play", "after_applause", "second_ending"):
            scene = self.scenes["ember." + suffix]
            with self.subTest(scene=scene["Id"]):
                self.assertFalse(scene.get("Remote"))
                self.assertNotIn("Kind", scene)
                self.assertEqual(["2570015799edf594daf2f076f2f975d8"], scene["Areas"])
                self.assertEqual("2779754eecffd044fbd4842dba55312c", scene["ContactUnit"])
                self.assertEqual(["f2a35965e9bc601449498bd022b04d9d"], scene["AnswerLists"])
                self.assertIn("ember.present_now", scene["Requires"])
                self.assertTrue({"ember.closed", "ember_dead", "ember_gone", "ember.absent"}
                                <= set(scene["Forbids"]))

    def test_all_returned_living_departed_and_absent_ember_siblings(self):
        for suffix in ("good_friend", "law_friend", "friend", "unfinished", "care",
                       "care_unfinished", "departed", "absent"):
            scene = self.scenes["ember.ending_" + suffix]
            self.assertIn("sacrifice", scene["Forbids"])
            self.assertEqual("trickster.commander_back", scene["ForbidOverrides"]["sacrifice"])
        self.assertIn("trickster.commander_back", self.scenes["ember.ending_sacrifice"]["Forbids"])
        self.assertNotIn("sacrifice", self.scenes["ember.ending_aeon"].get("ForbidOverrides", {}))

    def test_kiana_outings_are_physical_and_invitation_remains_postal(self):
        for suffix in ("rehearsal", "stagecraft", "date", "morning", "guest_table",
                       "market_weather", "lenna_door", "blue_room", "bakery_stairs",
                       "last_page", "first_readers", "ink_after", "working_room",
                       "kept_evening", "borrowed_name", "yard_evening", "unborrowed_evening",
                       "a_place_afterward", "betrothal"):
            scene = self.scenes["kiana." + suffix]
            with self.subTest(scene=scene["Id"]):
                self.assertFalse(scene.get("Remote"))
                self.assertNotIn("Kind", scene)
                self.assertEqual("180b0eaa5dce387458d2ebf0ee943985", scene["ContactUnit"])
                self.assertEqual("kiana.presence", scene["InteractionHub"])
                self.assertIn("kiana.present_now", scene["Requires"])
        presence = self.story["Presences"]["kiana.presence"]
        self.assertNotIn("trickster.ever", presence["Requires"])
        self.assertNotIn("trickster.now", presence["Requires"])
        self.assertIn(["kiana.trickster.returned", "kiana.trickster.met", "kiana.aftermath_seen"],
                      presence["RequiresAnyGroups"])
        self.assertTrue(self.scenes["kiana.invitation"]["Remote"])
        self.assertTrue(self.scenes["kiana.another_page"]["Remote"])
        self.assertNotIn("InteractionHub", self.scenes["kiana.seelah"])
        self.assertTrue(self.scenes["kiana.trickster.late_question_letter"]["Remote"])

    def test_cairn_requires_lann_at_act_three_neathholm(self):
        scene = self.scenes["wenduag.trickster.killed.cairn"]
        self.assertFalse(scene.get("Remote"))
        self.assertNotIn("Kind", scene)
        self.assertEqual(["3091eaedc174f2c45a95a9e9743e9b09"], scene["Areas"])
        self.assertEqual("cb29621d99b902e4da6f5d232352fbda", scene["ContactUnit"])
        self.assertEqual(["66385ad77fa743e4bb1234078dbd804c"], scene["AnswerLists"])
        self.assertIn("lann.in_party", scene["Requires"])
        self.assertTrue({"lann.dead", "lann.kicked_out", "lann.plot_absent"} <= set(scene["Forbids"]))
        self.assertIn("wenduag.trickster.staged", scene["Requires"])
        self.assertEqual(2, scene["DelayHours"])

    def test_exclusive_refusal_preserves_saved_terminal_and_has_distinct_ending(self):
        for suffix in ("court.claim", "court.claim_in_person"):
            node = next(node for node in self.scenes["wenduag.trickster." + suffix]["Nodes"]
                        if node["Id"] == "partner_exclusive_refused")
            choice = by_contract(node['Choices'], [{'Next': None, 'Requires': [], 'Forbids': [], 'Set': ['wenduag.partner_stance.exclusive', 'wenduag.partner.exclusive_refused', 'wenduag.closed'], 'Abort': False}])
            self.assertIsNone(choice["Next"])
            self.assertEqual(["wenduag.partner_stance.exclusive", "wenduag.partner.exclusive_refused",
                              "wenduag.closed"], choice["Set"])
        new = self.scenes["wenduag.trickster.epilogue.exclusive_refused"]
        self.assertIn("wenduag.partner.exclusive_refused", new["Requires"])
        self.assertNotIn("wenduag.trickster.court.claim_refused", new["Requires"])
        self.assertIn("wenduag.trickster.court.claim_refused",
                      self.scenes["wenduag.trickster.epilogue.refused"]["Requires"])
        self.assertNotEqual(new['Id'], self.scenes["wenduag.trickster.epilogue.refused"]['Id'])
        pending = json.loads((ROOT / "tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        self.assertEqual([], prose_pending_lint.check(self.story, pending, integration=True))

    def test_already_fixed_hunt_and_clearing(self):
        for suffix in ("court.hunt", "court.hunt.native_visit"):
            scene = self.scenes["wenduag.trickster." + suffix]
            self.assertFalse(scene.get("Remote"))
            self.assertNotIn("Kind", scene)
        self.assertEqual(24, self.scenes["kaylessa.clearing.where_i_was_meant_to_die"]["DelayHours"])


