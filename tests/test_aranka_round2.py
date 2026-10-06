"""Round-2 Aranka graph continuity and saved payoff receipts."""
import json
import runpy
from story_format import c, n, scene as make_scene
from pathlib import Path
import unittest

from storylines import aranka_continuation as island, aranka_trickster as route


ROOT = Path(__file__).resolve().parents[1]
SCENES = {s["Id"]: s for s in [*route.SCENES, *island.SCENES]}


def nodes(scene):
    return {n["Id"]: n for n in scene["Nodes"]}


class ArankaRound2Tests(unittest.TestCase):
    def test_every_brief_has_one_state_free_slot_and_the_exact_bridge(self):
        briefs = list((ROOT / "tools/route_packs/explicit_slots/aranka").glob("*.json"))
        self.assertEqual(len(briefs), 11)
        for brief in briefs:
            slot_id = brief.stem
            scene = SCENES[slot_id.rsplit(".explicit.", 1)[0]]
            slots = [n for n in scene["Nodes"] if n["Id"] == slot_id]
            slots += [p for n in scene["Nodes"] for p in n.get("Paragraphs", [])
                      if p.get("Id") == slot_id]
            with self.subTest(slot=slot_id):
                self.assertEqual(len(slots), 1)
                data = json.loads(brief.read_text(encoding="utf-8"))
                self.assertIn(data["last_line"].removeprefix("N: "), slots[0]["Text"])
                for choice in slots[0].get("Choices", []):
                    self.assertEqual(choice["Set"], [])
                    self.assertFalse(choice["Abort"])

    def test_all_roof_siblings_return_to_the_saved_morning_receipt(self):
        roofs = [s for s in route.SCENES if s["Id"].startswith(
            ("aranka.trickster.verse.encore", "aranka.trickster.verse.third_verse"))]
        self.assertEqual(len(roofs), 8)
        for scene in roofs:
            graph = nodes(scene)
            slot_id = scene["Id"] + ".explicit.1"
            self.assertEqual(graph["threshold"]["Choices"][0]["Next"], slot_id)
            self.assertEqual(graph[slot_id]["Choices"][0]["Next"], "morning")
            self.assertEqual(graph["morning"]["Choices"][0]["Set"], [route.NIGHT])
            self.assertIsNone(graph["morning"]["Choices"][0]["Next"])
            self.assertEqual(graph["song_counter"]["Choices"][0]["Set"], [route.NIGHT])
            self.assertEqual(scene["DelayHours"], 24 if scene["Id"].endswith("_late") else 72)

    def test_commitment_and_closure_choices_keep_their_indices_and_effects(self):
        for scene in route.SCENES:
            if scene["Id"].startswith("aranka.trickster.verse.encore"):
                choice = nodes(scene)["choice"]["Choices"]
                self.assertEqual([(c["Next"], c["Set"]) for c in choice],
                                 [("stay", [route.KEPT]), ("not_yet", []),
                                  ("stage", [route.CLOSED, route.NEROSYAN])])
            elif scene["Id"].startswith("aranka.trickster.verse.third_verse"):
                choice = nodes(scene)["start"]["Choices"]
                self.assertEqual([(c["Next"], c["Set"]) for c in choice],
                                 [("sung", [route.KEPT, route.SANG_ALONE]),
                                  ("refused", [route.CLOSED])])

    def test_all_letter_receipts_follow_bodily_arrival(self):
        deliveries = [s for s in route.SCENES if s["Id"] in (
            "aranka.trickster.verse.her_letter", "aranka.trickster.verse.her_letter_late",
            "aranka.trickster.verse.any_tavern", "aranka.trickster.failure.second_verse",
            "aranka.trickster.failure.second_verse_late", "aranka.trickster.failure.mocking_verse_any")]
        self.assertEqual(len(deliveries), 6)
        for scene in deliveries:
            for node in scene["Nodes"]:
                if any(route.ANSWERED in c["Set"] for c in node["Choices"]):
                    self.assertTrue("Aranka rode back" in node["Text"]
                                    or "Aranka climbed down" in node["Text"], scene["Id"])
                    self.assertNotIn(route.MORAL_REPAIRED,
                                     [f for c in node["Choices"] for f in c["Set"]])

    def test_each_duet_pays_apology_before_the_same_billing_receipts(self):
        for scene in route.SCENES:
            if not scene["Id"].startswith("aranka.trickster.verse.duet"):
                continue
            graph = nodes(scene)
            for opening in ("vandal", "denied", "mocking", "posters"):
                self.assertEqual(len(graph[opening]["Choices"]), 2)
                for choice in graph[opening]["Choices"]:
                    self.assertIn("sorry", choice["Text"])
            self.assertEqual(graph["signed"]["Choices"][0]["Set"], [route.DUET, route.CREDITED])
            self.assertEqual(graph["billing"]["Choices"][0]["Set"], [route.DUET, route.VAIN])

    def test_island_night_keeps_legacy_exit_and_deferral_bypasses_hollow_slot(self):
        graph = nodes(SCENES["aranka.no_encore_needed"])
        self.assertEqual(graph["desire"]["Choices"][0]["Next"], "night_initiation")
        self.assertEqual(graph["night"]["Choices"][0]["Set"],
                         ["aranka.extension_night", "aranka.extension_kept"])
        for name, flag in (("kiss", "extension_kiss"), ("quiet", "extension_quiet")):
            self.assertEqual(graph[name]["Choices"][0]["Set"], ["aranka." + flag, route.KEPT])
        graph = nodes(SCENES["aranka.the_story_that_follows"])
        self.assertEqual(graph["private"]["Choices"][0]["Next"],
                         "aranka.the_story_that_follows.explicit.1")
        self.assertIsNone(graph["private"]["Choices"][1]["Next"])
        self.assertEqual(graph["hollow_morning"]["Choices"][0]["Set"],
                         ["aranka.story_conversation_done"])

    def test_native_reunion_locations_are_mutually_exclusive_and_exit_unchanged(self):
        page = SCENES["aranka.trickster.epilogue.commit"]["Nodes"][0]
        self.assertEqual(page["Id"], "end")
        self.assertEqual(page["Choices"], [dict(Text="Continue", Next=None, Set=[],
                                              Requires=[], Forbids=[], Abort=False)])
        parts = page["Paragraphs"]
        stay = next(p for p in parts if "writing requisitions" in p["Text"])
        leave = next(p for p in parts if "roadside inn" in p["Text"])
        self.assertEqual(stay["Requires"], [route.COMMANDER_STAYS])
        self.assertEqual(stay["Forbids"], [route.COMMANDER_LEAVES])
        self.assertEqual(leave["Requires"], [route.COMMANDER_LEAVES])
        self.assertNotIn("requisitions", leave["Text"])
        self.assertIn("sacrifice", SCENES["aranka.trickster.epilogue.commit"]["Forbids"])

    def test_thall_contact_is_native_living_and_does_not_create_a_partner(self):
        self.assertNotIn("aranka.thall.answer", SCENES)
        scene = runpy.run_path(str(ROOT / "tools/route_packs/plans/aranka-thall-contact.py"),
                              init_globals=dict(scene=make_scene, n=n, c=c,
                                                BLOCKED=island.BLOCKED, AREA=island.AREA,
                                                ANSWERS=island.ANSWERS))["THALL_CONTACT_PROPOSAL"]
        self.assertEqual(scene["ContactUnit"], "8fb65bd79574771429526eaef26762a9")
        self.assertEqual(scene["Areas"], [island.AREA])
        self.assertIn(route.THALL_DEAD, scene["Forbids"])
        self.assertEqual(scene["Nodes"][0]["Choices"][0]["Set"], [])
        self.assertEqual(scene["Nodes"][0]["SpeakerUnit"], scene["ContactUnit"])

    def test_route_sources_keep_crlf_and_no_scripted_commander_dialogue(self):
        for file in ("aranka_continuation.py", "aranka_trickster.py"):
            raw = (ROOT / "storylines" / file).read_bytes()
            self.assertNotIn(b"\n", raw.replace(b"\r\n", b""))
        for scene in island.SCENES:
            for node in scene["Nodes"]:
                self.assertNotIn("{n}you say", node["Text"])
                self.assertNotIn("{n}you remind", node["Text"])


if __name__ == "__main__":
    unittest.main()
