"""History-sensitive dialogue and voluntary payment at both recovery hosts."""
import unittest

from tests.story_fixture import fresh_story


def available(choice, flags):
    return (set(choice.get("Requires", ())) <= flags
            and not set(choice.get("Forbids", ())) & flags)


class VellexiaRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}

    def nodes(self, suffix):
        return {n["Id"]: n for n in self.scenes["vellexia." + suffix]["Nodes"]}

    def test_each_lesson_and_refusal_matches_acquisition_at_both_hosts(self):
        histories = (("unmirrored", "unmirrored", "footstool"),
                     ("diminished", "cost.diminished", "charm"),
                     ("entry", "entry", "Vask"),
                     ("provoked", "provoked", "Upper City"),
                     ("unpaid", "unpaid", "halfway"))
        for host in ("after.visit", "after.visit_quarters"):
            nodes = self.nodes("trickster." + host)
            for history, flag, anchor in histories:
                flags = {"vellexia.trickster." + flag}
                with self.subTest(host=host, history=history):
                    start = [c for c in nodes["start"]["Choices"] if available(c, flags)]
                    self.assertEqual([history], [c["Next"] for c in start])
                    lesson = nodes[nodes[history]["Choices"][0]["Next"]]
                    replies = [c for c in lesson["Choices"] if available(c, flags)]
                    self.assertEqual(1, len(replies))
                    given = nodes[replies[0]["Next"]]
                    kept = nodes[nodes[history]["Choices"][1]["Next"]]
                    self.assertIn(anchor, given["Text"])
                    if history != "unmirrored":
                        self.assertNotIn("footstool", given["Text"] + kept["Text"])
                    if history == "diminished":
                        self.assertIn("will not cast", given["Text"])
                        self.assertIn("painter", kept["Text"])
                    # Both responses still pay their original lesson/secret latch
                    # at the shell, before the player chooses a relationship.
                    for response, latch in ((given, "lesson_given"), (kept, "cost.trick_kept")):
                        exits = [c for c in response["Choices"] if available(c, flags)]
                        self.assertTrue(exits)
                        for exit in exits:
                            shell = nodes[exit["Next"]]
                            self.assertIn("vellexia.trickster." + latch, shell["Choices"][0]["Set"])

    def test_later_shell_does_not_turn_social_lessons_into_magic(self):
        nodes = self.nodes("trickster.after.voice")
        for flag in ("cost.diminished", "entry", "provoked", "unpaid"):
            for latch in ("lesson_given", "cost.trick_kept"):
                flags = {"vellexia.trickster." + flag, "vellexia.trickster." + latch}
                choices = [c for c in nodes["trick"]["Choices"] if available(c, flags)]
                self.assertEqual(1, len(choices))
                text = nodes[choices[0]["Next"]]["Text"]
                self.assertNotIn("footstool", text)
                self.assertNotIn("practising on the furniture", text)

    def test_painter_disclosure_has_a_refusal_without_return(self):
        for host in ("sword.likeness", "sword.likeness_stores"):
            nodes = self.nodes("trickster." + host)
            disclosure = nodes["spell"]
            self.assertNotIn("You sit.", disclosure["Text"])
            self.assertNotIn("weight of flesh", disclosure["Text"])
            accept, decline = disclosure["Choices"]
            self.assertEqual("sitting", accept["Next"])
            self.assertTrue(decline["Abort"])
            self.assertFalse(decline["Set"])
            self.assertFalse(accept["Set"])
            self.assertIn("vellexia.trickster.cost.sat_for_painter", nodes["sitting"]["Choices"][0]["Set"])
            self.assertIn("vellexia.trickster.returned", nodes["wake"]["Choices"][0]["Set"])

    def test_vellexia_owns_the_demonstration_and_unload_is_staged(self):
        for host in ("mirrored.unmirror", "mirrored.unmirror_stores"):
            nodes = self.nodes("trickster." + host)
            for node in ("reading", "undone"):
                self.assertEqual("Vellexia", nodes[node]["Speaker"])
                self.assertEqual("a32a07903e428d34cb0e98a804d40569", nodes[node]["SpeakerUnit"])
            self.assertIn("footstool", nodes["start"]["Text"])
        for host, node in (("mirrored.speaks", "crated"), ("mirrored.fetch", "paid")):
            self.assertIn("footstool", self.nodes("trickster." + host)[node]["Text"])

    def test_mirror_threat_is_an_earned_memory(self):
        page = self.nodes("ending_mirror")["start"]
        self.assertNotIn("promised to watch", page["Text"])
        memory = next(p for p in page["Paragraphs"] if "promised to watch" in p["Text"])
        self.assertEqual([["vellexia.trickster.cost.watched", "vellexia.trickster.kept_as_mirror"]], memory["AnyGroups"])

    def test_merged_last_call_is_safe_for_the_kept_mirror(self):
        call = self.scenes["vellexia.lastcall.call"]
        text = " ".join(n["Text"] for n in call["Nodes"])
        for bodily in ("sits up", "reaches for", "never bored"):
            self.assertNotIn(bodily, text)
        self.assertIn("voice answers", text)
        coda = self.scenes["vellexia.lastcall.page"]
        self.assertIn("vellexia.trickster.kept_as_mirror", coda["Forbids"])


if __name__ == "__main__":
    unittest.main()
