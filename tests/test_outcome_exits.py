"""Shared outcome fallbacks keep saved positions and one selectable exit."""
import unittest

from story_format import c
from storylines.earned_outcomes import _append_exit, _covers_exit
from tests.story_fixture import fresh_story


class OutcomeExitTests(unittest.TestCase):
    def test_preserved_morning_exit_keeps_its_index_and_retires_duplicate(self):
        key = "minagho_chivarro.outcome.eligible"
        original = c("[Leave.]", abort=True, forbids=(key,))
        node = {"Id": "morning", "Choices": [c(next="hand"), c(next="roof"), original]}
        _append_exit(node, key)
        self.assertIs(node["Choices"][2], original)
        self.assertEqual(len(node["Choices"]), 4)
        duplicate = node["Choices"][3]
        self.assertEqual(duplicate["Requires"], duplicate["Forbids"])
        self.assertEqual(duplicate["Requires"], [key])
        for flags in (set(), {key}):
            exits = [a for a in node["Choices"] if a["Abort"]
                     and set(a["Requires"]) <= flags and not set(a["Forbids"]) & flags]
            self.assertEqual(exits, [original] if not flags else [])

    def test_missing_exit_still_gets_a_selectable_fallback(self):
        key = "route.outcome.eligible"
        node = {"Choices": [c(next="reward", requires=(key,))]}
        _append_exit(node, key)
        self.assertEqual(node["Choices"][1], c("[Leave.]", abort=True, forbids=(key,)))

    def test_exit_coverage_requires_an_effect_free_unblocked_abort(self):
        key = "route.outcome.eligible"
        self.assertTrue(_covers_exit(c("[Leave.]", abort=True), key))
        self.assertTrue(_covers_exit(c("[Return to camp.]", abort=True), key))
        self.assertTrue(_covers_exit(c("[Leave.]", abort=True, forbids=(key,)), key))
        for fields in ({"Requires": [key]}, {"Forbids": ["other"]},
                       {"Set": ["reward"]}, {"Next": "later"},
                       {"Abort": False}, {"Mythic": "PlayerIsTrickster"},
                       {"RequiresAnyGroups": [["other"]]},
                       {"Crusade": {"Resource": "Finances", "Amount": -100}}):
            answer = c("[Leave.]", abort=True)
            answer.update(fields)
            self.assertFalse(_covers_exit(answer, key), fields)

    def test_export_retires_duplicate_fallbacks_without_removing_indices(self):
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        # These appender positions were exported before this fix. The later
        # engine pass may fold an outcome condition into trickster.now.
        for sid, nid, index in (
            ("anevia.trickster.gone.commit", "answer", 19),
            ("kiana.trickster.late_question", "partner_secret", 6),
            ("soana.trickster.missed.bowl", "partner_secret_terms", 4),
            ("nenio.trickster.commit.replication_result", "morning", 4),
        ):
            node = next(n for n in scenes[sid]["Nodes"] if n["Id"] == nid)
            answer = node["Choices"][index]
            self.assertEqual(answer["Text"], "[Leave.]")
            self.assertTrue(answer["Abort"])
            self.assertEqual(len(answer["Forbids"]), 1)
            key = answer["Forbids"][0]
            self.assertIn(key, answer["Requires"], (sid, nid, index))
            self.assertTrue(any(_covers_exit(previous, key)
                                for previous in node["Choices"][:index]))

    def test_c3_primer_keeps_native_observation_and_loss_gates(self):
        page = next(s for s in fresh_story()["Scenes"]
                    if s["Id"] == "minagho_chivarro.trickster.minagho_dead.setup_c3")
        self.assertNotIn("trickster.ever", page["Forbids"])
        self.assertIn("minagho.brand_told_c3", page["Requires"])
        self.assertIn("minagho.dead", page["Forbids"])
        self.assertIn("minagho_chivarro.trickster.primed", page["Forbids"])


if __name__ == "__main__":
    unittest.main()
