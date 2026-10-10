"""W4 Ch5 ensemble: playable action walks and earned current attendance."""
import copy
import unittest

from tests.story_fixture import fresh_story, row_registration_fixture
from storylines import household, harem_caps
from storylines.harem_rows import ensemble_ch5 as row
from tools import rrt_verify as v, savecompat, payoff_lint, departure_lint, player_text_lint


class EnsembleCh5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Row behavior is exercised before the final current-contact pass.
        cls.story = row_registration_fixture(row)
        cls.story["Counts"].pop("household.cap.ch5.dynamic", None)
        harem_caps.apply(cls.story)
        cls.model = v.Model(cls.story)
        cls.scene = cls.model.by_id[row.SCENE_ID]

    def state(self, extra=(), omit=(), chapter=5):
        state = v.SimState(chapter, 1000)
        state.flags.update({"trickster", "trickster.foresight.accepted",
            "trickster.foresight.cost.promise", household.KEPT,
            "nenio.committed", "nenio.trickster.test_running", "nenio.trickster.first_night",
            "nenio.in_party", "wenduag.in_party", "wenduag.romance_finished.latched",
            "delamere.committed", "delamere.trickster.second_hunt_offered",
            "delamere.trickster.caught", "delamere.trickster.returned"})
        state.flags.difference_update(omit)
        state.flags.update(extra)
        v.sim_complete(self.model, state)
        return state

    def available(self, **kwargs):
        return v.sim_available(self.model, self.scene, self.state(**kwargs))

    def test_full_export_delivers_earned_narrated_visit(self):
        story = fresh_story()
        model = v.Model(story)
        scene = model.by_id[row.SCENE_ID]
        self.assertTrue(scene["Remote"])
        self.assertEqual(scene["Kind"], "visit")
        self.assertTrue(scene["TableHosted"])
        self.assertFalse(scene["ParticipantContacts"])
        self.assertTrue(v.sim_available(model, scene, self.state()))

    def test_live_table_ch5_only_and_no_page_substitutes(self):
        self.assertTrue(self.available())
        for chapter in (3, 4, 6):
            self.assertFalse(self.available(chapter=chapter))
        for flag in ("trickster", "trickster.foresight.accepted", household.KEPT,
                     "delamere.trickster.returned"):
            self.assertFalse(self.available(omit=(flag,)), flag)
        for flag in ("fool_king.gone", "trickster.failed", "sacrifice"):
            self.assertFalse(self.available(extra=(flag,)), flag)
        self.assertTrue(self.available(extra=("sacrifice", "ending.trickster")))

    def test_all_named_women_need_open_current_bodies(self):
        self.assertEqual(self.scene["Participants"], list(row.WOMEN))
        self.assertEqual(self.scene["ParticipantWomen"], list(row.WOMEN))
        for woman in row.WOMEN:
            for suffix in (".closed", ".epoch_unavailable", ".returned_actor_lost"):
                self.assertFalse(self.available(extra=(woman + suffix,)), woman + suffix)
        for flag in ("nenio.in_party", "wenduag.in_party"):
            self.assertFalse(self.available(omit=(flag,)), flag)
        for flag in ("nenio.dissolved", "nenio.sent_away", "wenduag.q3_killed",
                     "wenduag.q3_sent_away", "wenduag.trickster.echo.abyss.unavailable"):
            self.assertFalse(self.available(extra=(flag,)), flag)

    def test_old_returns_never_override_later_losses(self):
        returned = ("nenio.dead", "nenio.trickster.cost.recreated", "nenio.trickster.returned")
        self.assertTrue(self.available(extra=returned))
        # Current shared body readers reject these non-party returned visitors.
        # Keep the scene fail-closed; do not invent a body/override in this unit.
        self.assertFalse(self.available(extra=returned, omit=("nenio.in_party",)))
        self.assertFalse(self.available(extra=(*returned, "nenio.presence.failed",
                                               "nenio.presence.arcade.failed"),
                                        omit=("nenio.in_party",)))
        for loss in ("nenio.dissolved", "nenio.closed", "nenio.returned_actor_lost",
                     "nenio.epoch_unavailable"):
            self.assertFalse(self.available(extra=(*returned, loss)), loss)
        returned = ("wenduag.dead_any", "wenduag.trickster.returned")
        self.assertTrue(self.available(extra=returned))
        self.assertFalse(self.available(extra=returned, omit=("wenduag.in_party",)))
        self.assertFalse(self.available(extra=(*returned, "wenduag.presence.failed"),
                                        omit=("wenduag.in_party",)))
        for loss in ("wenduag.q3_killed", "wenduag.closed", "wenduag.returned_actor_lost",
                     "wenduag.epoch_unavailable"):
            self.assertFalse(self.available(extra=(*returned, loss)), loss)

    def test_each_action_completes_once_and_defer_remains_available(self):
        start = self.scene["Nodes"][0]
        for index, suffix in enumerate(("shafts", "feathers")):
            state = self.state()
            choice = start["Choices"][index]
            terminal = next(n for n in self.scene["Nodes"] if n["Id"] == choice["Next"])
            answer = terminal["Choices"][0]
            self.assertIsNone(answer["Next"])
            self.assertEqual(answer["Set"], [row.SEEN, row.PREFIX + "arrows." + suffix])
            state.flags.update(answer["Set"])
            v.sim_complete(self.model, state)
            self.assertFalse(v.sim_available(self.model, self.scene, state))
        defer = start["Choices"][2]
        self.assertTrue(defer["Abort"])
        self.assertFalse(defer["Set"])
        self.assertTrue(self.available())
        state = self.state()
        state.rest_spent["household.pair"] = 1
        self.assertFalse(v.sim_available(self.model, self.scene, state))

    def test_existing_dynamic_cap_charges_only_actual_completions(self):
        cap = self.story["Counts"]["household.cap.ch5.dynamic"]
        self.assertEqual(cap["Min"], 3)
        self.assertIn(row.SEEN, cap["Of"])
        witnesses = [f for f in cap["Of"] if f != row.SEEN][:3]
        self.assertEqual(len(witnesses), 3)
        self.assertTrue(self.available(extra=witnesses[:2]))
        self.assertFalse(self.available(extra=witnesses))

    def test_no_ladder_intimacy_native_rewrite_or_conditional_dialogue(self):
        self.assertFalse(player_text_lint.check({"Scenes": [self.scene]})["review"])
        self.assertFalse(self.scene["Pair"])
        flags = {f for n in self.scene["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertEqual(flags, {row.SEEN, row.PREFIX + "arrows.shafts",
                                 row.PREFIX + "arrows.feathers"})
        for node in self.scene["Nodes"]:
            self.assertFalse(node["Paragraphs"])
            self.assertNotIn("explicit", node["Id"])
        self.assertFalse(self.scene["AnswerLists"])
        self.assertEqual(self.story["ForesightConsumers"][row.SCENE_ID], household.PAGE_TAKEN)

    def test_append_only_idempotent_registration_and_surface_classification(self):
        payload = copy.deepcopy(self.story)
        before = copy.deepcopy(payload)
        row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, before)
        self.assertFalse(savecompat.check(self.story))
        # This live household scene creates no route payoff, letter or book
        # surface. It needs attendance, not a new route-contract exception.
        self.assertFalse(payoff_lint.check(self.story))
        self.assertFalse(departure_lint.check(self.story))


if __name__ == "__main__":
    unittest.main()
