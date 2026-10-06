"""Reviewed Terendelev draft repairs preserve evidence and night consequences."""
import copy
import unittest
from unittest.mock import patch

from storylines import foresight, terendelev_watch as watch
from storylines import terendelev_continuation as draft


class TerendelevPolishDraftTests(unittest.TestCase):
    def scene(self, name):
        return next(s for s in draft.SCENES if s["Id"] == "terendelev.continuation." + name)

    def take(self, scene, node, index, flags):
        page = next(n for n in scene["Nodes"] if n["Id"] == node)
        answer = page["Choices"][index]
        self.assertTrue(set(answer["Requires"]) <= flags)
        self.assertFalse(set(answer["Forbids"]) & flags)
        flags.update(answer["Set"])
        return answer["Next"]

    def test_all_source_orders_hear_the_witness_before_comparison(self):
        scene = self.scene("scale_invitation")
        prefix = "terendelev.continuation.evidence."
        for first in ("claw", "storyteller", "witness"):
            for other in (("claw", "storyteller") if first == "witness" else (None,)):
                with self.subTest(first=first, other=other):
                    flags = {"terendelev.continuation.claw.possessed"}
                    index = {"claw": 0, "witness": 1, "storyteller": 2}[first]
                    self.assertEqual(self.take(scene, "accept", index, flags), first)
                    if first != "witness":
                        self.assertEqual(self.take(scene, first, 0, flags), "witness")
                    else:
                        self.assertEqual(self.take(scene, "witness", 2, flags), "accept")
                        self.assertEqual(self.take(scene, "accept", 0 if other == "claw" else 2, flags), other)
                        self.assertEqual(self.take(scene, other, 0, flags), "witness")
                    witness = next(n for n in scene["Nodes"] if n["Id"] == "witness")
                    available = [i for i, a in enumerate(witness["Choices"])
                                 if set(a["Requires"]) <= flags and not set(a["Forbids"]) & flags]
                    self.assertEqual(len(available), 1)
                    self.assertEqual(self.take(scene, "witness", available[0], flags), "compare")
                    self.assertIn(prefix + "witness", flags)
                    self.assertTrue({prefix + "claw", prefix + "storyteller"} & flags)

    def test_oath_receipts_follow_its_threshold_once_and_have_a_dawn(self):
        scene = self.scene("private_oath")
        flags = set()
        self.assertEqual(self.take(scene, "start", 2, flags), "desire")
        self.assertEqual(self.take(scene, "desire", 0, flags), "oath")
        self.assertEqual(self.take(scene, "oath", 0, flags), "threshold")
        self.assertNotIn("terendelev.continuation.oath.made", flags)
        self.assertEqual(self.take(scene, "threshold", 0, flags), "oath_dawn")
        self.assertIn("terendelev.continuation.oath.made", flags)
        self.assertNotIn("terendelev.continuation.intimacy.adult", flags)
        self.assertIsNone(self.take(scene, "oath_dawn", 0, flags))
        self.assertEqual(sum("terendelev.continuation.oath.made" in a["Set"]
                             for n in scene["Nodes"] for a in n["Choices"]), 1)

    def test_missing_result_keeps_a_wait_and_grants_no_observation(self):
        scene = self.scene("escape_boundary")
        flags = {"terendelev.continuation.escape.test.requested"}
        self.assertEqual(self.take(scene, "start", 2, flags), "result_pending")
        pending = next(n for n in scene["Nodes"] if n["Id"] == "result_pending")
        available = [a for a in pending["Choices"] if set(a["Requires"]) <= flags
                     and not set(a["Forbids"]) & flags]
        self.assertEqual(len(available), 1)
        self.assertTrue(available[0]["Abort"])
        self.assertFalse(available[0]["Set"])
        self.assertNotIn("terendelev.continuation.escape.test.observed", flags)

    def test_physical_scenes_still_require_confirmed_actor_and_remote_stays_remote(self):
        for name in ("returned_letter", "private_oath", "windward_evening", "private_aftercare"):
            scene = self.scene(name)
            self.assertFalse(scene["Remote"])
            self.assertIn(draft.RETURNED_ACTOR_CONFIRMED, scene["Requires"])
            self.assertEqual(scene["Areas"], [draft.DREZEN])
        for name in draft.REMOTE_SCENE_NAMES:
            self.assertTrue(self.scene(name)["Remote"])
            self.assertIsNone(self.scene(name)["ContactUnit"])

    def test_memory_answer_hook_consumes_shared_append_without_replacing_old_answers(self):
        hosts = [watch.P + "watch.third_bell" + suffix for suffix in ("", "_awning")]
        payload = {"Scenes": copy.deepcopy([s for s in watch.SCENES if s["Id"] in hosts])}
        original_targets = {s["Id"]: [a["Next"] for n in s["Nodes"] if n["Id"] == "talk"
                                    for a in n["Choices"]] for s in payload["Scenes"]}
        gaps = [g for g in foresight.GAPS if g["host"] in hosts]
        with patch.object(foresight, "GAPS", gaps):
            foresight.integrate_gaps(payload)
        memories = list(payload["Scenes"])
        rest = {"Id": watch.P + "epilogue.rest"}
        letter = {"Id": watch.P + "galfrey_letter_awning"}
        coda = {"Id": "terendelev.lastcall.page"}
        payload["Scenes"].extend((rest, letter, coda))
        watch.polish_memory_answers(payload)
        self.assertEqual(payload["Scenes"][-3:], [rest, coda, letter])
        for scene in memories:
            talk = next(n for n in scene["Nodes"] if n["Id"] == "talk")
            self.assertEqual([a["Next"] for a in talk["Choices"][:4]], original_targets[scene["Id"]])
            sold = talk["Choices"][4]
            self.assertEqual(sold["Next"], "gap.gate")
            self.assertIn(foresight.GONE_SQUARE, sold["Requires"])
            self.assertEqual(talk["Choices"].index(sold), 4)


if __name__ == "__main__":
    unittest.main()
