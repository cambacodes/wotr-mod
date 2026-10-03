"""Replay Delamere's audited callbacks from the assembled, folded story."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from expansion import make_expansion

P = "delamere.trickster."


def matches(item, flags):
    return (all(flag in flags for flag in item.get("Requires", []))
            and not any(flag in flags for flag in item.get("Forbids", []))
            and all(any(flag in flags for flag in group)
                    for group in item.get("AnyGroups", [])))


def page_text(node, flags):
    return "\n".join([node["Text"], *(
        p["Text"] for p in node.get("Paragraphs", []) if matches(p, flags))])


def play(scene, flags, *, choices=None, mobility="Success"):
    """Follow actual answer indices and check targets; default to the first open answer."""
    flags = set(flags)
    nodes = {node["Id"]: node for node in scene["Nodes"]}
    node_id = scene["Nodes"][0]["Id"]
    seen = set()
    text = []
    while node_id:
        if node_id in seen:
            raise AssertionError("Replay loop: " + node_id)
        seen.add(node_id)
        node = nodes[node_id]
        text.append(page_text(node, flags))
        open_answers = [(i, c) for i, c in enumerate(node["Choices"]) if matches(c, flags)]
        index = (choices or {}).get(node_id, open_answers[0][0] if open_answers else -1)
        answer = next((c for i, c in open_answers if i == index), None)
        if answer is None:
            raise AssertionError("No open answer: " + node_id)
        flags.update(answer["Set"])
        check = answer.get("Check")
        node_id = (check[mobility if check["Skill"] == "SkillMobility" else "Success"]
                   if check else answer["Next"])
    return flags, "\n".join(text)


class DelamerePolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = make_expansion()
        cls.scenes = {scene["Id"]: scene for scene in cls.story["Scenes"]}

    def test_mobility_outcomes_through_first_frost(self):
        waking = self.scenes[P + "crypt.stag"]
        for outcome in ("Success", "Failure"):
            with self.subTest(outcome=outcome):
                flags, _ = play(waking, {"delamere.tomb_opened"}, mobility=outcome)
                flags.update({P + "second_hunt_offered", P + "told_truth"})
                flags, _ = play(self.scenes[P + "woods.second_hunt"], flags)
                self.assertIn("delamere.committed", flags)
                flags, text = play(self.scenes[P + "woken.day_owed"], flags)
                self.assertIn(P + "first_frost", flags)
                self.assertIn("You take to the roofs", text)
                if outcome == "Success":
                    self.assertIn("Worse than the first time", text)
                    self.assertNotIn("Further than three strides", text)
                else:
                    self.assertIn("Further than three strides", text)
                    self.assertNotIn("Worse than the first time", text)
                    self.assertNotIn("You are getting slow", text)

    def test_first_meat_in_both_folds_and_standalone(self):
        for count in ("woken.count", "woken.count_late"):
            with self.subTest(count=count):
                flags, text = play(self.scenes[P + count], set())
                self.assertIn(P + "first_meat", flags)
                _, standalone = play(self.scenes[P + "woken.first_meat"], flags)
                for rendered in (text, standalone):
                    if count.endswith("_late"):
                        self.assertNotIn("Abyss already", rendered)
                        self.assertIn("blood dripping from the haunches", rendered)
                    else:
                        self.assertIn("Abyss already", rendered)
                        self.assertNotIn("blood dripping from the haunches", rendered)

    def test_immediate_refusal_from_every_waking(self):
        for waking in ("crypt.stag", "crypt.stag_alone", "crypt.stag_late", "drezen.stag"):
            for mobility in ("Success", "Failure"):
                with self.subTest(waking=waking, mobility=mobility):
                    scene = self.scenes[P + waking]
                    flags, _ = play(scene, {"delamere.tomb_opened"},
                                    choices={"lady": 2}, mobility=mobility)
                    self.assertIn("delamere.closed", flags)
                    self.assertNotIn(P + "returned", flags)
                    self.assertEqual(P + "woke_in_drezen" in flags, waking == "drezen.stag")
                    for ending in ("never", "never_sacrifice"):
                        text = page_text(self.scenes[P + "epilogue." + ending]["Nodes"][0], flags)
                        expected = "woke in Drezen" if waking == "drezen.stag" else "woke in the Temple of Delamere"
                        wrong = "woke in the Temple of Delamere" if waking == "drezen.stag" else "woke in Drezen"
                        self.assertIn(expected, text)
                        self.assertNotIn(wrong, text)
                    for node in scene["Nodes"]:
                        if node["Id"] in ("lift", "fumble"):
                            self.assertTrue(all(P + "woke_in_drezen" not in c["Set"]
                                                for c in node["Choices"]))


if __name__ == "__main__":
    unittest.main()
