"""S05 safe historical branch: real knowledge, no invented live outcome."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s05
from storylines import foresight
from tools import rrt_verify, savecompat

ROOT = Path(__file__).resolve().parents[1]


class S05Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = fresh_story(include_harem=False)

    def setUp(self):
        consumers = dict(foresight.CONSUMERS)
        self.addCleanup(self.restore_consumers, consumers)
        self.story = copy.deepcopy(self.original)
        s05.register(self.story, self.story["Scenes"], self.story["Etudes"])
        self.model = rrt_verify.Model(self.story)
        self.scene = self.model.by_id[s05.P + "precedence"]

    @staticmethod
    def restore_consumers(consumers):
        foresight.CONSUMERS.clear()
        foresight.CONSUMERS.update(consumers)

    def state(self, chapter=5, extra=(), omit=()):
        state = rrt_verify.SimState(chapter, 1000)
        state.flags.update({"trickster", "trickster.now", "foresight.page_taken",
                            "household.stance_eligible", "household.table.kept",
                            s05.LOVERS_SEEN} - set(omit))
        state.flags.update(extra)
        return state

    def test_paid_page_and_seen_native_account_are_independent_requirements(self):
        self.assertTrue(rrt_verify.sim_available(self.model, self.scene, self.state()))
        for key in ("trickster", "foresight.page_taken", "household.table.kept", s05.LOVERS_SEEN):
            with self.subTest(key=key):
                self.assertFalse(rrt_verify.sim_available(self.model, self.scene, self.state(omit=(key,))))
        # An affair, meeting Shyka or hearing Socothbenoth's plan buys no knowledge.
        state = self.state(omit=(s05.LOVERS_SEEN,), extra=(
            "nocticula.partner_secret_exposed", "shamira.partner.secret_exposed",
            "noct.socoth_plan_exposed", "trickster.ever"))
        self.assertFalse(rrt_verify.sim_available(self.model, self.scene, state))
        self.assertEqual(self.story["SeenCues"][s05.LOVERS_SEEN], [s05.LOVERS_CUE])

    def test_historical_record_never_becomes_a_live_reply_after_loss(self):
        for losses in (("noct.closed", "shamira.closed"),
                       ("noct.dead", "shamira.killed"),
                       ("noct.acq.council_fight", "shamira.trickster.cost.kept_captive"),
                       ("shamira.trickster.returned", "shamira.trickster.cast_out")):
            with self.subTest(losses=losses):
                self.assertTrue(rrt_verify.sim_available(self.model, self.scene, self.state(extra=losses)))
        body = next(s for s in self.story["Scenes"] if s["Id"] == self.scene["Id"])
        self.assertEqual(body["Participants"], [])
        self.assertEqual(body["ParticipantWomen"], [])
        self.assertTrue(all(n["Speaker"] == "Narrator" for n in body["Nodes"]))
        writes = {f for n in body["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertEqual(writes, {s05.P + "precedence.seen", s05.P + "historical"})

    def test_chapter_failure_exhaustion_and_later(self):
        for chapter in (3, 4, 6):
            self.assertFalse(rrt_verify.sim_available(self.model, self.scene, self.state(chapter)))
        for flag in ("trickster.failed", "fool_king.gone", s05.P + "precedence.seen"):
            self.assertFalse(rrt_verify.sim_available(self.model, self.scene, self.state(extra=(flag,))))
        body = s05.historical_scene()
        later = body["Nodes"][0]["Choices"][1]
        self.assertTrue(later["Abort"])
        self.assertFalse(later["Set"])
        self.assertIsNone(later["Next"])
        self.assertEqual(body["RestAllowance"], "household.protected")
        self.assertFalse(body.get("HouseholdArcStart", False))

    def test_registration_is_append_only_and_repeatable(self):
        old = savecompat.inventory(self.original)
        self.assertEqual(savecompat.check(self.story, old), [])
        before = copy.deepcopy(self.story)
        s05.register(self.story, self.story["Scenes"], self.story["Etudes"])
        self.assertEqual(before, self.story)

    def test_bodily_slot_and_reconciliation_remain_blocked(self):
        brief = json.loads((ROOT / "tools/route_packs/explicit_slots/harem/blocked/nocticula_shamira" /
                            (s05.SLOT_ID + ".json")).read_text(encoding="utf-8"))
        self.assertEqual(brief["status"], "blocked")
        self.assertEqual(brief["id"], s05.SLOT_ID)
        self.assertEqual(s05.BLOCKED_SLOT["Text"], brief["default"])
        self.assertNotIn(s05.SLOT_ID, self.model.by_id)
        self.assertFalse(any("explicit" in n["Id"] for n in self.scene["Nodes"]))
        self.assertNotIn(s05.P + "retry", self.model.by_id)
        self.assertFalse(any(s05.P + "exposure_answered" in str(v)
                             for v in self.story.get("Derived", {}).values()))


if __name__ == "__main__":
    unittest.main()
