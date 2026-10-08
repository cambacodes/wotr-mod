"""Mutations of the Gemory contract, without game/build dependencies."""
from contextlib import redirect_stdout
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import slot_brief_lint as lint


class SlotBriefLintTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="rrt-slot-lint-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.brief = dict(voice="Irabeth: direct, soldierly.", scene="Commander and Irabeth alone, intercourse.",
                          last_line="N: The watch changes.", speakers={"I": "Irabeth"},
                          example="N: She catches your hand.\nI: Come here.", facts="No extra physical facts.",
                          slot_id="night.explicit.1", commander_variants=["a man", "a woman"])
        self.story = {"Scenes": [{"Id": "night", "MinChapter": 3, "MaxChapter": 5,
                       "Nodes": [{"Id": "start", "Choices": [{"Next": "night.explicit.1"}]},
                                 {"Id": "night.explicit.1", "Choices": [{"Next": "morning"}]},
                                 {"Id": "morning", "Speaker": "Irabeth", "Text": "{n}The watch changes.{/n}\n\"Up.\""}]}]}

    def write(self, brief=None, route="irabeth", name="slot.json"):
        path = self.root / route / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.brief if brief is None else brief), encoding="utf-8")
        return path

    def codes(self, brief=None, story=None):
        findings, _ = lint.lint([self.write(brief)], story or self.story)
        return {f["code"] for f in findings if f["severity"] == "hard"}

    def test_valid_and_exact_boundary_mutation(self):
        self.assertEqual(set(), self.codes())
        self.assertIn("last_line", self.codes(dict(self.brief, last_line="N: Dawn breaks.")))

    def test_parse_required_and_schema(self):
        path = self.write()
        path.write_text("{", encoding="utf-8")
        self.assertEqual("parse", lint.lint([path], self.story)[0][0]["code"])
        for field in lint.REQUIRED:
            brief = dict(self.brief)
            del brief[field]
            self.assertIn("required", self.codes(brief), field)
        self.assertIn("schema", self.codes(dict(self.brief, facts=["Not accepted by Gemory"])))
        self.assertIn("schema", self.codes(dict(self.brief, scene={})))

    def test_missing_retired_and_disconnected_host(self):
        self.assertIn("host", self.codes(story={"Scenes": []}))
        for change in ({"Requires": ["paid"], "Forbids": ["paid"]}, {"Forbids": ["chapter_later"]}):
            story = copy.deepcopy(self.story)
            story["Scenes"][0].update(change)
            self.assertIn("retired", self.codes(story=story))
        story = copy.deepcopy(self.story)
        story["Scenes"][0]["Nodes"][0]["Choices"][0].update(Requires=["paid"], Forbids=["paid"])
        self.assertIn("retired", self.codes(story=story))

    def test_legitimate_earned_gate_is_allowed(self):
        story = copy.deepcopy(self.story)
        story["Scenes"][0].update(Requires=["trickster.now", "earned_return"], Forbids=["dead"],
                                 ForbidOverrides={"dead": "earned_return"})
        self.assertEqual(set(), self.codes(story=story))

    def test_skill_check_can_reach_slot(self):
        story = copy.deepcopy(self.story)
        story["Scenes"][0]["Nodes"][0]["Choices"] = [
            {"Check": {"Success": "night.explicit.1", "Failure": "morning"}}]
        self.assertEqual(set(), self.codes(story=story))

    def test_multiple_successors_are_all_checked(self):
        story = copy.deepcopy(self.story)
        story["Scenes"][0]["Nodes"][1]["Choices"].append({"Next": "other"})
        story["Scenes"][0]["Nodes"].append({"Id": "other", "Speaker": "Narrator", "Text": "{n}Another dawn.{/n}"})
        self.assertIn("last_line", self.codes(story=story))

    def test_branch_boundaries_are_exact_and_complete(self):
        story = copy.deepcopy(self.story)
        story["Scenes"][0]["Nodes"][1]["Choices"].append({"Next": "other"})
        story["Scenes"][0]["Nodes"].append({"Id": "other", "Speaker": "Narrator", "Text": "{n}Another dawn.{/n}"})
        brief = dict(self.brief, last_lines={"morning": "N: The watch changes.", "other": "N: Another dawn."})
        self.assertEqual(set(), self.codes(brief, story))
        brief["last_lines"]["other"] = "N: Wrong dawn."
        self.assertIn("last_line", self.codes(brief, story))
        brief["last_lines"] = {"morning": "N: The watch changes."}
        self.assertIn("last_line", self.codes(brief, story))
        self.assertIn("schema", self.codes(dict(self.brief, last_lines=[])))

    def test_short_host_address_and_inline_anchor(self):
        brief = dict(self.brief, host_scene="night", host_node="night.explicit.1")
        self.assertEqual(set(), self.codes(brief))
        story = copy.deepcopy(self.story)
        story["Scenes"][0]["Nodes"][1]["Text"] = "{n}She kisses you. The watch changes.{/n}"
        brief["after_text"] = "{n}She kisses you. "
        self.assertEqual(set(), self.codes(brief, story))
        brief["after_text"] = "Missing anchor"
        self.assertIn("host", self.codes(brief, story))
        brief["paragraph_index"] = 999
        self.assertIn("host", self.codes(brief, story))

    def test_evidenced_drop_cannot_hide_live_slot(self):
        index = {self.brief["slot_id"]: {"status": "dropped", "reason": "No encounter remains", "evidence": "route report"}}
        path = self.write()
        self.assertIn("index", {f["code"] for f in lint.lint([path], self.story, slot_index=index)[0]})
        self.assertEqual([], lint.lint([path], {"Scenes": []}, slot_index=index)[0])
        del index[self.brief["slot_id"]]["reason"]
        self.assertIn("index", {f["code"] for f in lint.lint([path], {"Scenes": []}, slot_index=index)[0]})

    def test_harem_rebuild_ownership_is_not_an_exemption(self):
        path = self.root / "harem" / "household.pair.camellia_vellexia.choice.explicit.1.json"
        self.assertEqual("camellia", lint.route_name(path))
        path = self.root / "harem" / "seelah_wenduag" / "household.pair.seelah_wenduag.choice.explicit.1.json"
        self.assertEqual("seelah_wenduag", lint.route_name(path))

    def test_duplicate_divergence_checks_both_owners(self):
        paths = [self.write(route="nocticula"), self.write(dict(self.brief, voice="Different."))]
        findings, _ = lint.lint(paths, self.story, known_rebuilds=True)
        duplicates = [f for f in findings if f["code"] == "duplicate"]
        self.assertEqual({"known", "hard"}, {f["severity"] for f in duplicates})
        self.assertEqual([], lint.lint([paths[0], self.write(route="irabeth", name="identical.json")], self.story)[0])

    def test_scope_and_anatomy(self):
        male = dict(self.brief, speakers={"I": "Irabeth", "E": "Elan"}, participants=["Irabeth", "Elan"])
        self.assertIn("scope", self.codes(male))
        male["scene"] = "Cuckold scene, Commander present with Irabeth and Elan."
        self.assertNotIn("scope", self.codes(male))
        male["commander"] = "absent"
        self.assertIn("scope", self.codes(male))
        male.pop("commander")
        male["scene"] = "Cuckold scene. Commander is absent; Irabeth and Elan are together."
        self.assertIn("scope", self.codes(male))
        brief = dict(self.brief)
        del brief["commander_variants"]
        self.assertIn("variants", self.codes(brief))
        self.assertIn("scope", self.codes(dict(self.brief, speakers={"E": "Ember"})))
        women = dict(self.brief, scene="Irabeth and Anevia alone.", commander="absent",
                     speakers={"I": "Irabeth", "A": "Anevia"})
        women.pop("commander_variants")
        self.assertEqual(set(), self.codes(women))

    def test_background_man_is_flagged_without_scope_failure(self):
        brief = dict(self.brief, scene="Commander and Irabeth alone; Daeran remains outside.")
        findings, _ = lint.lint([self.write(brief)], self.story)
        self.assertTrue(any(f["code"] == "male_mention" for f in findings))
        self.assertFalse(any(f["code"] == "scope" for f in findings))
        interrupted = dict(self.brief, scene="Commander and Irabeth alone; Elan calls from outside.",
                           speakers={"I": "Irabeth", "E": "Elan"})
        self.assertNotIn("scope", self.codes(interrupted))
        participating = dict(interrupted, scene="Commander and Irabeth are together. Elan joins them in bed.")
        self.assertIn("scope", self.codes(participating))
        self.assertIn("scope", self.codes(dict(self.brief, scene="Commander watches as Irabeth has sex with another man.")))
        self.assertNotIn("scope", self.codes(dict(self.brief, scene="Commander and Irabeth alone; she never has sex with another man.")))
        self.assertIn("scope", self.codes(dict(self.brief, speakers={"C": "Commander"}, participants=["Commander"])))

    def test_malformed_variants_do_not_crash(self):
        self.assertIn("variants", self.codes(dict(self.brief, commander_variants=[["a man"]])))

    def test_folded_copy_resolves_to_original_host(self):
        story = copy.deepcopy(self.story)
        duplicate = copy.deepcopy(story["Scenes"][0])
        duplicate["Id"] = "earlier_delivery"
        story["Scenes"].append(duplicate)
        self.assertNotIn("host", self.codes(story=story))

    def test_epilogue_paragraph_and_tense(self):
        story = copy.deepcopy(self.story)
        scene = story["Scenes"][0]
        scene["Owner"] = "IrabethEpilogue"
        scene["Nodes"] = [{"Id": "page", "Text": "{n}After the war.{/n}", "Paragraphs":
                           [{"Id": "night.explicit.1", "Text": "{n}She returned.{/n}"}], "Choices": []}]
        self.assertIn("narration", self.codes(story=story))
        self.assertEqual(set(), self.codes(dict(self.brief, narration="third-past"), story))

    def test_paragraph_boundary_respects_existing_history(self):
        story = copy.deepcopy(self.story)
        scene = story["Scenes"][0]
        scene["Owner"] = "IrabethEpilogue"
        scene["Nodes"] = [{"Id": "page", "Speaker": "Narrator", "Paragraphs": [
            {"Id": "night.explicit.1", "Text": "{n}The night.{/n}", "Requires": ["home"]},
            {"Text": "{n}The road.{/n}", "Forbids": ["home"]},
            {"Text": "{n}The watch changes.{/n}", "Requires": ["home"]},
            {"Text": "{n}Years later.{/n}"}], "Choices": []}]
        self.assertEqual(set(), self.codes(dict(self.brief, narration="third-past"), story))
        scene["Nodes"][0]["Paragraphs"][0].pop("Requires")
        self.assertIn("last_line", self.codes(dict(self.brief, narration="third-past"), story))

    def test_cli_counts_strict_and_explicit_known_rebuilds(self):
        self.write(dict(self.brief, last_line="Wrong"), route="areelu-vorlesh")
        story = self.root / "story.json"
        story.write_text(json.dumps(self.story), encoding="utf-8")
        args = ["--briefs", str(self.root), "--story", str(story)]
        # Story is outside the briefs directory.
        briefs = self.root / "areelu-vorlesh"
        args[1] = str(briefs)
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, lint.main(args))
            self.assertEqual(1, lint.main(args + ["--strict"]))
            self.assertEqual(0, lint.main(args + ["--strict", "--known-rebuilds"]))
        self.assertIn("1 briefs", output.getvalue())
        self.assertIn("known rebuild", output.getvalue())


if __name__ == "__main__":
    unittest.main()
