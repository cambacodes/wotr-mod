"""S21 contract: current participants, independent witnesses, exhaustive staging."""
import copy
import itertools
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s21
from tools import rrt_verify


class S21Watch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads((Path(__file__).resolve().parents[1] /
                                "development/Story.json").read_text(encoding="utf-8-sig"))
        # Also exercise the row in isolation when the coordinator's discovery
        # hook has not yet been installed in this integration base.
        s21.register(cls.story, cls.story["Scenes"], cls.story["Etudes"])
        cls.model = rrt_verify.Model(cls.story)
        cls.body = cls.model.by_id[s21.P + "watch"]
        cls.nodes = {n["Id"]: n for n in cls.body["Nodes"]}

    def state(self):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(self.body["Requires"])
        state.flags.update(["seelah.harem.eligible", "yaniel.harem.eligible"])
        return state

    def test_page_current_path_friendship_and_arrival_are_required(self):
        for key in ("trickster", "foresight.page_taken", *s21.FRIENDS,
                    "yaniel.trickster.returned", "yaniel.freed.latched",
                    "seelah.present_now", "yaniel.present_now"):
            with self.subTest(key=key):
                state = self.state()
                self.assertTrue(rrt_verify.sim_available(self.model, self.body, state))
                state.flags.remove(key)
                self.assertFalse(rrt_verify.sim_available(self.model, self.body, state))

    def test_old_returns_do_not_erase_closure_loss_or_failed_body(self):
        for key in ("yaniel.closed", "seelah.closed", "yaniel.killed.latched",
                    "yaniel.trickster.left_free", "yaniel.presence.failed",
                    "engine.l12.commander_unreturned", "seelah.epoch_unavailable",
                    "yaniel.epoch_unavailable"):
            with self.subTest(key=key):
                state = self.state()
                state.flags.update(["seelah.trickster.returned", key])
                self.assertFalse(rrt_verify.sim_available(self.model, self.body, state))

    def test_first_wins_enmity_uses_only_its_directional_override(self):
        for a, b in (s21.PAIR, s21.PAIR[::-1]):
            state = self.state()
            state.flags.add(a + ".harem.enmity." + b)
            state.flags.add(b + ".harem.reconciled." + a)
            self.assertFalse(rrt_verify.sim_available(self.model, self.body, state))
            state.flags.add(a + ".harem.reconciled." + b)
            self.assertTrue(rrt_verify.sim_available(self.model, self.body, state))

    def test_every_custody_and_rescue_history_has_exactly_one_continuation(self):
        keys = ("yaniel.trickster.carries", "yaniel.radiance_in_party",
                "yaniel.radiance_held", "yaniel.seelah_sister")
        for values in itertools.product((False, True), repeat=4):
            state = self.state()
            state.flags.update(k for k, value in zip(keys, values) if value)
            for node_id in ("history", "equipment"):
                selectable = [c for c in self.nodes[node_id]["Choices"]
                              if rrt_verify.sim_choice_available(c, state)]
                self.assertEqual(len(selectable), 1, (values, node_id))
        state = self.state()
        state.flags.add("yaniel.radiance_held")  # stash supplies no drawn blade
        selected = [c for c in self.nodes["equipment"]["Choices"]
                    if rrt_verify.sim_choice_available(c, state)]
        self.assertEqual(selected[0]["Next"], "stored_blade")

    def test_outcomes_abort_allowance_and_registration_are_separate(self):
        root = self.nodes["start"]["Choices"]
        self.assertEqual([c["Next"] for c in root], ["history", "declined", None])
        self.assertTrue(root[2]["Abort"])
        self.assertEqual(root[2]["Set"], [])
        writes = {node["Id"]: node["Choices"][0]["Set"] for node in self.body["Nodes"]}
        self.assertEqual(writes["directed"], list(s21.KEPT))
        self.assertEqual(writes["declined"], [s21.P + "watch.seen", s21.P + "watch.declined"])
        self.assertTrue(all(not flags for node, flags in writes.items()
                            if node not in ("directed", "declined")))
        state = self.state()
        state.rest_spent["household.pair"] = 1
        self.assertFalse(rrt_verify.sim_available(self.model, self.body, state))
        state.rest_spent.clear()
        state.flags.add(s21.P + "watch.seen")
        self.assertFalse(rrt_verify.sim_available(self.model, self.body, state))
        story = copy.deepcopy(self.story)
        before = len(story["Scenes"])
        s21.register(story, story["Scenes"], story["Etudes"])
        self.assertEqual(len(story["Scenes"]), before)
        self.assertEqual(self.body["HouseholdCategory"], "dynamic")
        self.assertNotIn("HouseholdArcStart", self.body)
        self.assertFalse(any(n.get("Paragraphs") for n in self.body["Nodes"]))


if __name__ == "__main__":
    unittest.main()
