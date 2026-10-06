"""Round-2 negative histories against the assembled export, including folded copies."""
import itertools
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from storylines import horzalah_trickster as route


def shown(block, flags):
    return (set(block.get("Requires", ())) <= flags
            and not set(block.get("Forbids", ())) & flags
            and all(set(group) & flags for group in block.get("AnyGroups", ())))


class HorzalahRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}

    def node(self, suffix, nid):
        return next(n for n in self.scenes[route.H + suffix]["Nodes"] if n["Id"] == nid)

    def test_cut_checkpoint_resumes_remainder_without_paid_outcome(self):
        for suffix, opening in (("mercy.gift", "guess"), ("unmet.knife", "start"), ("late.at_night", "start")):
            cut = self.node(suffix, "cut")
            if self.scenes[route.H + suffix].get("NativeReturnCue"):
                self.assertFalse(cut.get("EnterSet"))
                incoming = [answer for node in self.scenes[route.H + suffix]["Nodes"]
                            for answer in node["Choices"] if answer["Next"] == "cut"]
                self.assertTrue(incoming)
                self.assertTrue(all(route.EAR in answer["Set"] for answer in incoming))
                flags = set(incoming[0]["Set"])
            else:
                flags = set(cut["EnterSet"])
            self.assertIn(route.EAR, flags)
            self.assertNotIn(route.PRIMED, flags)
            self.assertNotIn(route.RETURNED, flags)
            choices = [c for c in self.node(suffix, opening)["Choices"] if shown(c, flags)]
            self.assertEqual([c["Next"] for c in choices], ["no_priest" if suffix == "late.at_night" else "box"])
            flags.add(route.PRIMED)
            self.assertFalse(any(shown(c, flags) for c in self.node(suffix, opening)["Choices"]))

    def test_folded_arrival_and_sister_state_in_actual_export(self):
        current = "participant.hepzamirah.available"
        departed = route.H + "sister_departed"
        for suffix in ("unmet.knife", "late.at_night"):
            arrival = self.node(suffix, "eng8.guild.arrival")
            self.assertIn("Threshold camp", arrival["Text"])
            self.assertNotIn("steps", self.node(suffix, "eng8.guild.start")["Text"])
            self.assertEqual(arrival["Choices"][0]["Next"], "eng8.guild.start")
            for present, left in itertools.product((False, True), repeat=2):
                flags = {route.HEPZ_BACK}
                if present:
                    flags.add(current)
                if left:
                    flags.add(departed)
                choices = [c for c in self.node(suffix, "eng8.guild.hall")["Choices"]
                           if (c.get("Next") or "").startswith("eng8.guild.sister") and shown(c, flags)]
                target = "eng8.guild.sister" + ("" if present else "_departed" if left else "_unavailable")
                self.assertEqual([c["Next"] for c in choices], [target])
                if not present:
                    self.assertNotIn("eating onions", self.node(suffix, target)["Text"])
                if not present and not left:
                    self.assertNotIn("has left", self.node(suffix, target)["Text"])

    def test_unpaid_endings_cannot_grant_guild_authority(self):
        for suffix in ("epilogue.closed", "epilogue.mourned"):
            page = self.node(suffix, "page")
            self.assertNotIn("kept the Assassins", page["Text"])
            self.assertNotIn("masters", page["Text"])
            flags = {route.STARTED, route.CLOSED}
            text = " ".join(p["Text"] for p in page["Paragraphs"] if shown(p, flags))
            self.assertNotIn("take her orders", text)
            self.assertNotIn("back to their contracts", text)
            self.assertNotIn("box", text)
            self.assertTrue("none said whether" in text.lower() or "knew nothing" in text.lower())

    def test_legacy_ending_exits_and_chamber_travel(self):
        for suffix in ("together", "commit", "decided", "unanswered", "left_free", "ally", "scarred", "closed", "mourned"):
            choices = self.node("epilogue." + suffix, "page")["Choices"]
            self.assertEqual(len(choices), 1)
            self.assertEqual(choices[0]["Set"], [])
            self.assertIsNone(choices[0]["Next"])
            self.assertFalse(choices[0]["Abort"])
        for nid in ("morning2", "doorway"):
            node = self.node("visit.chamber", nid)
            self.assertIn("passage", node["Text"])
            terminal = node["Choices"][0]
            self.assertEqual(terminal["Set"], [route.CHAMBER, route.MORNING])
            self.assertIsNone(terminal["Next"])

    def test_slots_have_briefs_and_one_first_night_per_history(self):
        directory = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/horzalah"
        briefs = [json.loads(p.read_text(encoding="utf-8")) for p in directory.glob("*.json")]
        self.assertEqual(len(briefs), 4)
        slots = {n["Id"] for s in self.scenes.values() for n in s["Nodes"] if ".explicit." in n["Id"]}
        slots.update(p["Id"] for s in self.scenes.values() for n in s["Nodes"]
                     for p in n.get("Paragraphs", ()) if ".explicit." in p.get("Id", ""))
        self.assertTrue({b["slot_id"] for b in briefs} <= slots)
        together = self.node("epilogue.together", "page")
        first = next(p for p in together["Paragraphs"] if p.get("Id") == route.H + "epilogue.together.explicit.1")
        self.assertTrue(shown(first, set()))
        self.assertFalse(shown(first, {route.CHAMBER}))


if __name__ == "__main__":
    unittest.main()
