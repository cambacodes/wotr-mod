"""eng7-f6c: native contract preservation and the complete departure ledger."""
from tests.story_fixture import fresh_story
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from storylines import engine_f6c
from storylines.native_overrides import _delivery, inventory
from tools.remote_allocation_lint import lint

ROOT = Path(__file__).resolve().parents[1]



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EngineF6cTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from expansion import make_expansion
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.expectations = json.loads((ROOT / "tools/native_inventory_expectations.json").read_text(encoding="utf-8"))

    def test_terendelev_future_question_keeps_its_native_continuation_without_old_evidence(self):
        question = self.expectations["Fixtures"]["fd39fd84212de2047b6b887c9a9cf28e"]["Data"]
        self.assertEqual(question["OnSelect"]["Actions"], [])
        self.assertEqual(question["NextCue"]["Cues"], ["!bp_ca71b79bc9a45b741bcc6599ef017fe7"])
        edit = self.story["NativeEpilogueEdits"]["ca71b79bc9a45b741bcc6599ef017fe7"]
        replacement = self.scenes[edit["Replacement"]]
        self.assertFalse(any(c["Set"] for n in replacement["Nodes"] for c in n["Choices"]))
        self.assertEqual(self.story["SeenCues"]["terendelev.voice_heard"], ["ca71b79bc9a45b741bcc6599ef017fe7"])
        self.assertNotIn("fd39fd84212de2047b6b887c9a9cf28e", self.story["SelectedAnswers"].values())

    def test_once_only_introduction_uses_a_condition_hide_without_sequence_replacement(self):
        cue = "21b10801b6c2b194d92506a137ef1307"
        original = self.expectations["Fixtures"][cue]["Data"]
        self.assertTrue(original["ShowOnce"])
        self.assertEqual(original["ParentAsset"], "a52fcdb99e9bfca459613b989a9760f9")
        for action in ("OnShow", "OnStop"):
            self.assertEqual(original[action]["Actions"], [])
        self.assertEqual(original["Answers"], [])
        self.assertEqual(original["Continue"]["Cues"], [])
        self.assertNotIn(cue, self.story["NativeEpilogueEdits"])
        spec = self.story["NativeGates"]["terendelev.funeral_introduction"]
        self.assertEqual(spec, dict(Target=cue, Relationship="terendelev",
                                   When=[["trickster.now", "terendelev.trickster.returned"]]))
        rows = inventory(self.story, self.expectations, json.loads((ROOT / "tools/engine_backlog.json").read_text(encoding="utf-8")))
        self.assertEqual(next(r for r in rows if r["Finding"] == "terendelev:001")["Status"], "registered_unevaluated")
        with self.assertRaisesRegex(ValueError, "cue-policy contract"):
            _delivery(cue, "cue", "REPLACE", None, {})

    def test_terendelev_dependencies_require_current_trickster(self):
        for target in ("c68d9b3a2b887f645ac539f996a63a92", "ca71b79bc9a45b741bcc6599ef017fe7"):
            spec = self.story["NativeEpilogueEdits"][target]
            for group in spec["When"]:
                self.assertIn("trickster.now", group)
                self.assertIn("terendelev.trickster.returned", group)
                # A returned dragon and historical Trickster power do not
                # select the replacement after the Commander changes path.
                legend = set(k for k in group if not k.startswith("!")) - {"trickster.now"}
                legend.update(("trickster.ever", "legend"))
                self.assertFalse(all(k in legend if not k.startswith("!") else k[1:] not in legend for k in group))
                current = legend - {"legend"} | {"trickster.now"}
                self.assertTrue(all(k in current if not k.startswith("!") else k[1:] not in current for k in group))
        hide = self.story["NativeGates"]["terendelev.funeral_introduction"]["When"]
        self.assertEqual(hide, [["trickster.now", "terendelev.trickster.returned"]])

    def test_departure_has_one_actual_remote_delivery_for_all_existing_roads(self):
        request = self.scenes["irabeth.return_request"]
        reply = self.scenes["irabeth.return_reply"]
        meeting = self.scenes["irabeth.return_first_words"]
        self.assertFalse(request["Remote"])
        self.assertEqual(request["ContactUnit"], "8692bff6041c47a0b13158d5977f291b")
        self.assertEqual(request["AnswerLists"], ["fa57cf97ea01bf34e9a30f6ad444381e"])
        self.assertTrue(reply["Remote"])
        self.assertEqual(reply["DelayHours"], 48)
        self.assertFalse(meeting["Remote"])
        for purpose in ("public", "trap"):
            for evidence in ("precise", "uncertain"):
                for decision in ("accepted", "declined"):
                    trace = [dict(name="/".join((purpose, evidence, decision)), character="Irabeth", chapter=5,
                                  deliveries=[request["Id"], reply["Id"], meeting["Id"]])]
                    report = lint(self.story, histories=trace)
                    self.assertEqual(report["hard"], [])
                    self.assertEqual(report["histories"][0]["pages"], [reply["Id"]])
        bad = copy.deepcopy(self.story)
        next(s for s in bad["Scenes"] if s["Id"] == request["Id"])["Remote"] = True
        self.assertTrue(lint(bad, histories=trace)["hard"])

    def test_every_added_replacement_has_no_authored_outcome_effect(self):
        for cue, relationship, suffix, location, when, text in engine_f6c.EDITS:
            with self.subTest(cue=cue):
                edit = self.story["NativeEpilogueEdits"][cue]
                expected_when = when
                if relationship == "irabeth":
                    # The stance merge keeps these published selectors for
                    # the original wife state; appended variants read the others.
                    retirement = ["!irabeth.partner_stance.share", "!irabeth.partner_stance.secret",
                                  "!irabeth.partner_stance.exclusive", "!anevia_dead",
                                  "!anevia.trickster.returned", "!anevia_gone"]
                    expected_when = [group + retirement for group in when]
                scene = self.scenes[edit["Replacement"]]
                live = [key for key in scene.get("Requires", [])
                        if ".payoff." in key or key.endswith((".present_now", ".reachable_by_letter"))]
                self.assertEqual(edit["When"], [list(dict.fromkeys([*group, *live])) for group in expected_when])
                original = self.expectations["Fixtures"][cue]
                self.assertEqual(original["Key"], edit["Key"])
                self.assertFalse(original["Data"]["ShowOnce"])
                scene = self.scenes[edit["Replacement"]]
                self.assertTrue(scene["Owner"].endswith("Epilogue"))
                self.assertFalse(saved_answer(scene["Nodes"][0]["Choices"], 0)["Set"])
                self.assertEqual(scene["Nodes"][0].get("Paragraphs", []), [])
                self.assertTrue(all({"trickster.now", "trickster.ever"} & set(g) for g in edit["When"]))

    def test_independent_native_histories_cannot_stage_a_living_commander(self):
        from tools import rrt_verify
        from tools.crossroute_checks import commander_alive
        from tools.crossroute_checks.common import Proof, blocks
        for identity in ("horzalah.native.eng7_f6c.guild", "horzalah.native.eng7_f6c.trio",
                         "irabeth.native.eng7_f6c.service", "irabeth.native.eng7_f6c.retired"):
            sample = dict(self.story, Scenes=[copy.deepcopy(self.scenes[identity])])
            model = rrt_verify.Model(sample)
            self.assertEqual(commander_alive.check(model, list(blocks(model)), Proof(model)), [])
            sample["Scenes"][0]["Nodes"][0]["Text"] += " {n}You stand beside her after the war.{/n}"
            model = rrt_verify.Model(sample)
            self.assertTrue(commander_alive.check(model, list(blocks(model)), Proof(model)))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        cue = engine_f6c.EDITS[0][0]
        scene = self.scenes[self.story['NativeEpilogueEdits'][cue]['Replacement']]
        choice = scene['Nodes'][0]['Choices'][0]
        with patch.dict(choice, Set=['unexpected.commitment']):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_every_added_replacement_has_no_authored_outcome_effect()


if __name__ == "__main__":
    unittest.main()
