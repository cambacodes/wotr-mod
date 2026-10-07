"""Reviewed Terendelev references cannot exempt a new physical cameo."""
import hashlib
import json
from pathlib import Path
import re
import unittest

from tests.story_fixture import fresh_story
from tools.crossroute_checks.mention_context import live_mentions


class TerendelevReferenceContextsTests(unittest.TestCase):
    def test_classifications_match_reviewed_text_and_fail_closed_on_new_cameos(self):
        data = json.loads((Path(__file__).resolve().parents[1] / "tools" /
                           "terendelev_reference_contracts.json").read_text(encoding="utf-8"))
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        for context in data["contexts"]:
            with self.subTest(context=context):
                scene = scenes[context["scene"]]
                node = next(n for n in scene["Nodes"] if n["Id"] == context["node"])
                slot = context["slot"]
                block = node if slot == "text" else node[
                    "Paragraphs" if slot.startswith("paragraph") else "Choices"][int(slot.split("[")[1][:-1])]
                text = block["Text"]
                self.assertEqual(hashlib.sha256(text.encode("utf-8")).hexdigest(), context["text_sha256"])
                woman = context["woman"]
                pattern = re.compile(woman + ("|Inheritor" if woman == "iomedae" else ""), re.I)
                self.assertEqual(live_mentions(text, pattern, scene_id=scene["Id"]), [])
                self.assertTrue(live_mentions(text + " {n}" + woman.capitalize() + " stands beside you.{/n}",
                                             pattern, scene_id=scene["Id"]))

    def test_live_queen_at_pyre_and_knight_cameos_keep_their_guards(self):
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        self.assertIn("crossroute.galfrey.unavailable", scenes["terendelev.trickster.bones.restitution"]["Forbids"])
        self.assertNotIn("crossroute.galfrey.unavailable", scenes["terendelev.trickster.late.the_wound_calls"]["Forbids"])
        for name in ("watch", "late", "debt"):
            page = scenes["terendelev.trickster.epilogue." + name]["Nodes"][0]
            self.assertIn("crossroute.irabeth.available", page["Paragraphs"][28]["Requires"])
            self.assertIn("terendelev.payoff.ordinary", page["Paragraphs"][32]["Requires"])
