"""EDGE screens must preserve attribution and never enforce advisory prose debt."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import edge_lint as edge


TARGETS = {"women": {"Minagho": {"register": "foul"},
                     "Camellia": {"register": "zero"}}}


def fixture_scene(sid="minachiv.visit", route="minagho_chivarro", speaker="Minagho", dialogue=""):
    return {"Id": sid, "Relationship": route, "Title": "", "Nodes": [
        {"Id": "start", "Speaker": speaker, "Text": dialogue, "Choices": []}]}



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

def check_layer(item):
    diagnostics = edge.layer(item)
    return diagnostics


def check_locked_regressions(*args):
    diagnostics = edge.locked_regressions(*args)
    return diagnostics


class EdgeLintTests(unittest.TestCase):
    def test_classes_and_quoted_addresses_include_conditional_siblings(self):
        s = fixture_scene(dialogue='"Read the ledger. The door works. You may also decline."')
        s["Title"] = "Doctor's intake"
        s["Nodes"][0]["Paragraphs"] = [{"Text": '"Her dignity deserves restitution. May I spare him if you permit?"'}]
        report = edge.check({"Scenes": [s]}, TARGETS)
        codes = {r["code"] for r in report["findings"]}
        self.assertLessEqual({"business", "exit", "therapy_clinic", "modern_ethics", "moral_authority"}, codes)
        self.assertTrue(report["routes"][0]["business_exceeds_menace"])
        self.assertIsNone(report["routes"][0]["business_to_menace"])
        for finding in report["findings"]:
            self.assertEqual("minachiv.visit", finding["scene"])
            self.assertIn(finding["match"], finding["quote"])
        self.assertTrue(any(r["location"] == "start/paragraph/0" for r in report["findings"]))

    def test_player_refusals_and_narration_do_not_become_demon_ethics(self):
        s = fixture_scene(dialogue='{n}The bitch demands dignity.{/n} "I kill whomever I please."')
        s["Nodes"][0]["Choices"] = [{"Text": '"You may leave. Ask my permission. Her rights matter, shit."'}]
        report = edge.check({"Scenes": [s]}, TARGETS)
        self.assertFalse(any(r["code"] in {"modern_ethics", "moral_authority", "exit"} for r in report["findings"]))
        self.assertEqual(0, next(r for r in report["profanity"] if r["woman"] == "Minagho")["count"])
        self.assertEqual(2, report["routes"][0]["counts"]["profanity"])

    def test_native_register_and_base_trickster_split(self):
        story = {"Scenes": [fixture_scene(dialogue='"Damn you, bitch."'),
            fixture_scene("minagho_chivarro.trickster.visit", dialogue='"I cut your throat."'),
            fixture_scene("camellia.visit", "camellia", "Camellia", '"A delight."')]}
        report = edge.check(story, TARGETS)
        self.assertEqual({"base", "trickster"}, {r["layer"] for r in report["routes"]})
        mouths = {r["woman"]: r for r in report["profanity"]}
        self.assertEqual(2, mouths["Minagho"]["count"])
        self.assertFalse(mouths["Camellia"]["review"])
        self.assertFalse(mouths["Minagho"]["review"])
        self.assertTrue(next(r for r in mouths["Minagho"]["layers"] if r["layer"] == "trickster")["review"])
        totals = {r["route"]: r for r in report["route_totals"]}
        self.assertEqual(2, totals["minagho_chivarro"]["scenes"])
        self.assertEqual(2, totals["minagho_chivarro"]["counts"]["profanity"])
        self.assertEqual("fallen", check_layer(fixture_scene("arueshalae.trickster.epilogue.kept_fallen")))
        self.assertEqual("fallen", check_layer(fixture_scene("arueshalae.trickster.evil.home_visit")))
        self.assertEqual("fallen", check_layer(fixture_scene("arueshalae.trickster.react.sosiel_evil")))
        self.assertEqual("acquisition", check_layer(fixture_scene("noct.acq.address")))

    def test_tenderness_repeats_across_routes_not_just_scenes(self):
        report = edge.check({"Scenes": [fixture_scene(dialogue="{n}For one heartbeat she stays there.{/n}"),
            fixture_scene("camellia.visit", "camellia", "Camellia", "{n}For one heartbeat she stays there.{/n}")]}, TARGETS)
        self.assertEqual(2, len(report["repeated_tenderness"]))
        self.assertEqual(["camellia", "minagho_chivarro"], report["repeated_tenderness"][0]["routes"])

    def test_prim_targets_flag_excess_without_inventing_numeric_rates(self):
        report = edge.check({"Scenes": [fixture_scene("camellia.visit", "camellia", "Camellia", '"Fuck."')]}, TARGETS)
        mouth = next(r for r in report["profanity"] if r["woman"] == "Camellia")
        self.assertTrue(mouth["review"])
        self.assertTrue(mouth["layers"][0]["review"])
        self.assertFalse(edge.mouth_review("regal", 100, 0))
        self.assertFalse(edge.mouth_review("near_zero", 100, 1))
        self.assertFalse(edge.mouth_review("foul", 0, 0))

    def test_class_variants_keep_exact_evidence_and_combine_stock_cadence(self):
        story = {"Scenes": [fixture_scene(dialogue="{n}Her shoulder comes to rest against yours. For a heartbeat she doesn’t let go.{/n}"),
            fixture_scene("camellia.visit", "camellia", "Camellia", "{n}Her shoulder against yours. For one heartbeat she does not let go.{/n}"),
            fixture_scene("jerribeth.visit", "jerribeth", "Jerribeth", '"I will stop waiting for an invitation. Before you reach for me, tell me if this is where you want to be."')]}
        report = edge.check(story, TARGETS)
        self.assertEqual(3, len(report["repeated_tenderness"]))
        self.assertTrue(any(r["code"] == "exit" and r["scene"] == "jerribeth.visit" for r in report["findings"]))
        self.assertEqual(2, next(r for r in report["route_totals"] if r["route"] == "jerribeth")["counts"]["therapy_clinic"])
        self.assertTrue(any("doesn’t" in r["quote"] for r in report["findings"]))

    def test_locks_preserve_text_allow_structure_and_catch_removal(self):
        story = {"Scenes": [fixture_scene(dialogue='"The door works."')]}
        frozen = edge.baseline(story, edge.check(story, TARGETS), "test")
        changed = copy.deepcopy(story)
        changed["Scenes"][0]["Requires"] = ["earned"]
        changed["Scenes"][0]["Nodes"][0]["Choices"].append({"Text": ""})
        # Empty structural surfaces add no prose; actual new displayed text does.
        self.assertEqual([], check_locked_regressions(changed, frozen, ["minachiv.visit"]))
        saved_answer(changed["Scenes"][0]["Nodes"][0]["Choices"], 0)["Text"] = "New answer"
        self.assertTrue(check_locked_regressions(changed, frozen, ["minachiv.visit"]))
        approved = {"scenes": ["minachiv.visit"], "scene_text_sha256": {
            "minachiv.visit": edge.text_hash(changed["Scenes"][0])}}
        self.assertEqual([], check_locked_regressions(changed, frozen, approved))
        changed["Scenes"][0]["Nodes"][0]["Choices"].clear()
        self.assertEqual([], check_locked_regressions(changed, frozen, {"scenes": ["minachiv.visit"]}))
        changed["Scenes"][0]["Nodes"][0]["Text"] = '"The door works. Room to move."'
        self.assertTrue(check_locked_regressions(changed, frozen, ["minachiv.visit"]))
        self.assertEqual([], check_locked_regressions(changed, frozen, []))
        self.assertTrue(check_locked_regressions({"Scenes": []}, frozen, ["minachiv.visit"]))
        self.assertEqual("missing baseline", check_locked_regressions(story, frozen, ["unknown"])[0]["reason"])

    def test_cli_report_strict_and_utf8_roundtrip(self):
        with tempfile.TemporaryDirectory(prefix="rrt-edge-test-") as tmp:
            root = Path(tmp)
            story_path, target_path, frozen_path, locks_path, output = [root / n for n in
                ("Story.json", "targets.json", "baseline.json", "locks.json", "report.json")]
            story = {"Scenes": [fixture_scene(dialogue='"You may refuse — I’m asking you, bitch."')]}
            story_path.write_text(json.dumps(story, ensure_ascii=False), encoding="utf-8")
            target_path.write_text(json.dumps(TARGETS), encoding="utf-8")
            args = ["--story", str(story_path), "--targets", str(target_path), "--baseline", str(frozen_path),
                    "--locks", str(locks_path), "--json", str(output), "--summary"]
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, edge.main(args + ["--write-baseline", "--revision", "test"]))
                self.assertEqual(0, edge.main(args + ["--strict"]))  # no locks yet
                locks_path.write_text(json.dumps(["minachiv.visit"]), encoding="utf-8")
                self.assertEqual(0, edge.main(args + ["--strict"]))
                story["Scenes"][0]["Nodes"][0]["Text"] += " New words."
                story_path.write_text(json.dumps(story, ensure_ascii=False), encoding="utf-8")
                self.assertEqual(0, edge.main(args))
                self.assertEqual(1, edge.main(args + ["--strict"]))
            quoted = json.loads(output.read_text(encoding="utf-8"))["findings"]
            self.assertIn("—", quoted[0]["quote"])

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        make_fixture = fixture_scene
        def altered(*args, **kwargs):
            scene = make_fixture(*args, **kwargs)
            if scene['Id'] == 'arueshalae.trickster.epilogue.kept_fallen':
                scene['Id'] = 'arueshalae.visit'
            return scene
        with patch(__name__ + '.fixture_scene', altered):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_native_register_and_base_trickster_split()


if __name__ == "__main__":
    unittest.main()
