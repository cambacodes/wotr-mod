"""The guide is an executable choice contract, including visible player directions."""
import json
import unittest

from tools import run_guide_check as guide


class RunGuideCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = guide.model_from(guide.ROOT / "development/Story.json")
        cls.text = guide.GUIDE.read_text(encoding="utf-8")
        cls.trace = guide.run_kit()
        cls.sources = guide.manifest()

    def check(self, text, trace=None):
        return guide.validate(text, self.model, self.trace if trace is None else trace, self.sources)

    def test_entire_ordered_campaign_matches_guide_and_earns_last_call(self):
        self.assertEqual(self.check(self.text), len(self.trace["log"]))

    def mutate_first_step(self, change):
        match = guide.STEP.search(self.text)
        record = json.loads(match.group(1))
        change(record)
        return self.text[:match.start(1)] + json.dumps(record) + self.text[match.end(1):]

    def test_deleted_scene_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown scene"):
            self.check(self.mutate_first_step(lambda r: r.update(scene="seelah.guide_missing")))

    def test_missing_node_and_changed_choice_index_are_rejected(self):
        for value in (["missing", 0], ["start", 999], ["start", -1]):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "Unknown choice"):
                self.check(self.mutate_first_step(lambda r: r["choices"].__setitem__(0, value)))

    def test_unknown_flag_in_handwritten_walkthrough_is_rejected(self):
        changed = self.text.replace("`ember.present`", "`ember.guide_typo`", 1)
        with self.assertRaisesRegex(ValueError, "Unknown flag"):
            self.check(changed)

    def test_wrong_visible_dc_and_cost_are_rejected(self):
        for old, new in (("PASS SkillAthletics DC 12", "PASS SkillAthletics DC 99"),
                         ("crusade Finances -200", "crusade Finances -1")):
            self.assertIn(old, self.text)
            with self.subTest(old=old), self.assertRaisesRegex(ValueError, "Visible choices"):
                self.check(self.text.replace(old, new, 1))

    def test_kit_order_and_branch_drift_are_rejected(self):
        for mutate in (lambda rows: rows.reverse(), lambda rows: rows[0]["choices"].pop()):
            changed = json.loads(json.dumps(self.trace))
            mutate(changed["log"])
            with self.assertRaisesRegex(ValueError, "ordered scenes/choices"):
                self.check(self.text, changed)

    def test_stale_rules_or_kit_input_requires_review(self):
        changed = dict(self.sources, **{"src/Story.cs": "changed"})
        with self.assertRaisesRegex(ValueError, "Rules/verifier/active kit changed"):
            guide.validate(self.text, self.model, self.trace, changed)

    def test_missing_last_call_creditor_is_rejected(self):
        changed = json.loads(json.dumps(self.trace))
        changed["log"] = [e for e in changed["log"] if e["id"] != "delamere.lastcall.call"]
        with self.assertRaisesRegex(ValueError, "all 22 Last Call call-ins"):
            self.check(self.text, changed)

    def test_historical_commitment_without_current_presence_is_rejected(self):
        changed = json.loads(json.dumps(self.trace))
        changed["final_flags"].remove("participant.chivarro.available")
        with self.assertRaisesRegex(ValueError, "earned presence is missing"):
            self.check(self.text, changed)

    def test_commitment_delayed_past_chapter_boundary_is_rejected(self):
        changed = json.loads(json.dumps(self.trace))
        changed["result"]["commit_hours"]["delamere"] = changed["result"]["commit_hours"]["lastcall"]
        with self.assertRaisesRegex(ValueError, "Chapter 3 commitment checkpoint"):
            self.check(self.text, changed)

    def test_stale_recovery_pointer_does_not_hide_exported_return_siblings(self):
        # The old away-device ID is absent, but the field report and actual
        # primary/fallback Erratum scenes earn Nenio's return in this export.
        self.assertNotIn("nenio.trickster.away.correction", self.model.by_id)
        recovery = guide.render_routes(self.model)
        for sid in ("nenio.trickster.away.field_report", "nenio.trickster.away.correction_visitor",
                    "nenio.trickster.away.correction_arcade"):
            self.assertIn("`" + sid + "`", recovery)
        self.assertIn("nenio.trickster.cost.demoted", recovery)


if __name__ == "__main__":
    unittest.main()
