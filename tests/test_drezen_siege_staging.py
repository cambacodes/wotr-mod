"""eng8-q8b: distinguish the Chapter 2 siege view from maps and memory."""
import copy
import json
from pathlib import Path
import unittest

from tools.crossroute_checks import location_staging as staging
from tools.crossroute_checks.common import Proof, blocks, verify
from tools.game_blueprints import find_bindings, game_dir


def fixture(text, areas=(), chapter=2):
    return {"Relationships": {"wenduag": {"StartedFlag": "wenduag.started", "ClosedFlag": "wenduag.closed", "CommittedFlag": "wenduag.committed"}}, "Scenes": [dict(
        Id="wenduag.trickster.early.walls", Relationship="wenduag", Owner="Wenduag",
        Requires=[], Forbids=[], Areas=list(areas), MinChapter=chapter, MaxChapter=chapter,
        Nodes=[dict(Id="start", Speaker="Narrator", Text=text, Choices=[dict(Text="Continue")])])]}


def findings(story):
    model = verify.Model(story)
    return staging.check(model, list(blocks(model)), Proof(model))


class DrezenSiegeStagingTests(unittest.TestCase):
    def test_native_area_evidence(self):
        expected = dict.fromkeys((*staging.SIEGE_AREAS, "7a25c101fe6f7aa46b192db13373d03b",
                                  "2570015799edf594daf2f076f2f975d8"), "BlueprintArea")
        evidence = find_bindings(game_dir() / "blueprints.zip", expected)
        for guid in staging.SIEGE_AREAS:
            self.assertEqual(evidence[guid]["path"], staging.SIEGE["blueprint_evidence"][guid].split(";")[0])
            self.assertIn("Act_2_SwordOfValor", evidence[guid]["path"])

    def test_original_never_before_seen_physical_view_is_not_history(self):
        text = "{n}Her whole face changes. You have never before seen her look at the city walls as a problem instead of a view.{/n}"
        self.assertTrue(findings(fixture(text)))
        for area in ("7a25c101fe6f7aa46b192db13373d03b", "2570015799edf594daf2f076f2f975d8", "unrelated"):
            self.assertTrue(findings(fixture(text, [area])))
        self.assertEqual(findings(fixture(text, staging.SIEGE_AREAS)), [])
        self.assertTrue(findings(fixture(text, [*staging.SIEGE_AREAS, "unrelated"])))

    def test_named_view_has_verified_siege_window_not_capital(self):
        text = "{n}She stands beneath Drezen's walls, watching the battlements.{/n}"
        story = fixture(text, staging.SIEGE_AREAS)
        story["Scenes"][0]["Id"] = "wenduag.other_siege_view"
        self.assertEqual(findings(story), [])
        story["Scenes"][0]["Areas"] = []
        self.assertTrue(findings(story))

    def test_maps_reports_memory_and_unrelated_camp_controls(self):
        for text in ("{n}She studies the walls on a scout's map of Drezen.{/n}",
                     "{n}She looks at a scout's report of Drezen's walls.{/n}",
                     "{n}She remembers standing beneath Drezen's walls.{/n}",
                     "{n}She recalls the siege of Drezen and its walls.{/n}",
                     "{n}She watches knights drill at the edge of the camp.{/n}"):
            self.assertEqual(findings(fixture(text)), [], text)
        for chapter in (3, 5):
            self.assertEqual(findings(fixture("{n}She stands beneath Drezen's walls.{/n}",
                                              ["2570015799edf594daf2f076f2f975d8"], chapter)), [])
        story = fixture("{n}She stands beneath Drezen's walls.{/n}", chapter=6)
        story["Scenes"][0]["Owner"] = "WenduagEpilogue"
        self.assertEqual(findings(story), [])

    def test_start_and_every_incoming_branch_are_checked(self):
        story = fixture("{n}She studies a scout's map of Drezen.{/n}")
        scene = story["Scenes"][0]
        scene["Nodes"][0]["Choices"] = [dict(Text="Plan", Next="view"), dict(Text="Look", Next="view")]
        scene["Nodes"].append(dict(Id="view", Speaker="Narrator", Text="{n}She looks at Drezen's walls beyond the camp.{/n}",
                                   Choices=[dict(Text="Continue")]))
        self.assertEqual({f["node"] for f in findings(story)}, {"view"})
        # A map branch cannot excuse a sibling present physical view.
        scene["Nodes"][1]["Text"] = "{n}She studies the walls on a map of Drezen.{/n}"
        self.assertEqual(findings(story), [])
        scene["Nodes"][0]["Text"] = "{n}Drezen's walls stand before you.{/n}"
        self.assertEqual({f["node"] for f in findings(story)}, {"start"})

    def test_generated_mapped_scene_uses_map_and_original_mutation_fails(self):
        story = json.loads(Path(__file__).resolve().parents[1].joinpath("development/Story.json").read_text())
        scene = copy.deepcopy(next(s for s in story["Scenes"] if s["Id"] == "wenduag.trickster.early.walls"))
        minimal = {"Relationships": {"wenduag": {"StartedFlag": "wenduag.started", "ClosedFlag": "wenduag.closed", "CommittedFlag": "wenduag.committed"}}, "Scenes": [scene]}
        self.assertEqual(findings(minimal), [])
        take = next(n for n in scene["Nodes"] if n["Id"] == "take")
        take["Text"] = "{n}You have never before seen her look at the city walls as a problem instead of a view.{/n}"
        self.assertTrue(findings(minimal))


if __name__ == "__main__":
    unittest.main()
