"""The guide is an executable choice contract, including visible player directions."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

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
        changed = "Handwritten reference: `ember.guide_typo`.\n\n" + self.text
        with self.assertRaisesRegex(ValueError, "Unknown flag"):
            self.check(changed)

    def test_wrong_visible_dc_and_cost_are_rejected(self):
        for old, new in (("PASS SkillAthletics DC 12", "PASS SkillAthletics DC 99"),
                         ("crusade Finances -200", "crusade Finances -1")):
            with self.subTest(old=old), self.assertRaisesRegex(ValueError, "Visible choices.*\n.*--update"):
                self.check(self.text.replace(old, new, 1))

    def test_update_refreshes_every_derived_block_and_manifest(self):
        changed = self.text
        for begin, end, _ in guide.derived_blocks(self.model, self.trace).values():
            start, stop = guide.block_bounds(changed, begin, end)
            changed = changed[:start] + "\nSTALE\n" + changed[stop:]
        changed = guide.META.sub('<!-- rrt-guide {"profile":"old","sources":{}} -->', changed)
        updated = guide.update_text(changed, self.model, self.trace, self.sources)
        self.assertEqual(self.check(updated), len(self.trace["log"]))
        self.assertEqual(json.loads("[" + ",".join(guide.STEP.findall(updated)) + "]"), guide.records(self.trace))
        self.assertEqual(json.loads(guide.META.search(updated).group(1))["sources"], self.sources)
        again = guide.update_text(updated, self.model, self.trace, self.sources)
        self.assertEqual(json.loads("[" + ",".join(guide.STEP.findall(again)) + "]"), guide.records(self.trace))
        self.assertEqual(self.check(again), len(self.trace["log"]))

    def test_unmarked_utf8_narrative_and_line_endings_are_preserved(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline), tempfile.TemporaryDirectory(prefix="rrt-guide-test-") as scratch:
                path = Path(scratch) / "guide.md"
                original = ("Handwritten — Shyka's bargain.\n\n" + self.text + "\nUnmarked ending: é.\n").replace("\n", newline)
                path.write_bytes(original.encode("utf-8"))
                before = path.stat()
                guide.update_guide(path, self.model, self.trace, self.sources)
                self.assertEqual(path.stat(), before)

    def test_mixed_newlines_in_unmarked_prose_are_preserved(self):
        with tempfile.TemporaryDirectory(prefix="rrt-guide-test-") as scratch:
            path = Path(scratch) / "guide.md"
            original = ("Handwritten LF — é.\n\n" + self.text.replace("\n", "\r\n") + "\nUnmarked LF ending.\n")
            path.write_bytes(original.encode("utf-8"))
            before = path.stat()
            guide.update_guide(path, self.model, self.trace, self.sources)
            self.assertEqual(path.stat(), before)

    def test_each_reference_section_rejects_stale_rendered_content(self):
        sections = (guide.render_resources(self.model, guide.records(self.trace)),
                    guide.render_steps(self.model, guide.records(self.trace)), guide.render_routes(self.model),
                    guide.render_presences(self.model), guide.render_native_plan(self.model))
        for section in sections:
            with self.subTest(section=section.splitlines()[0]):
                changed = self.text.replace(section, section + "\nStale direction.", 1)
                with self.assertRaisesRegex(ValueError, "Visible choices.*\n.*--update"):
                    self.check(changed)
                updated = guide.update_text(changed, self.model, self.trace, self.sources)
                self.assertEqual(self.check(updated), len(self.trace["log"]))

    def test_invalid_run_cannot_overwrite_guide(self):
        changed = json.loads(json.dumps(self.trace))
        changed["log"] = [row for row in changed["log"] if row["id"] != "delamere.lastcall.call"]
        with tempfile.TemporaryDirectory(prefix="rrt-guide-test-") as scratch:
            path = Path(scratch) / "guide.md"
            original = self.text.replace("PASS SkillAthletics DC 12", "PASS SkillAthletics DC 99", 1).encode("utf-8")
            path.write_bytes(original)
            before = path.stat()
            with self.assertRaisesRegex(ValueError, "all 22 Last Call call-ins"):
                guide.update_guide(path, self.model, changed, self.sources)
            self.assertEqual(path.stat(), before)

    def test_stale_checklists_and_calendar_are_rejected_with_update_hint(self):
        for name, (begin, end, _) in guide.derived_blocks(self.model, self.trace).items():
            if name == "checked":
                continue
            with self.subTest(block=name):
                start, stop = guide.block_bounds(self.text, begin, end)
                changed = self.text[:start] + "\nSTALE\n" + self.text[stop:]
                with self.assertRaisesRegex(ValueError, f"Derived {name} is stale.*\n.*--update"):
                    self.check(changed)

    def test_missing_or_reversed_markers_cannot_overwrite_narrative(self):
        begin, end, _ = guide.derived_blocks(self.model, self.trace)["calendar"]
        reversed_markers = self.text.replace(begin, "MARKER_SWAP", 1).replace(end, begin, 1).replace("MARKER_SWAP", end, 1)
        for text in (self.text.replace(end, "", 1), reversed_markers):
            with self.subTest(text=text[:80]), self.assertRaisesRegex(ValueError, "marker|pair"):
                guide.update_text(text, self.model, self.trace, self.sources)

    def test_cli_update_uses_current_trace_and_sources(self):
        with tempfile.TemporaryDirectory(prefix="rrt-guide-test-") as scratch:
            path = Path(scratch) / "guide.md"
            path.write_text(self.text.replace("PASS SkillAthletics DC 12", "PASS SkillAthletics DC 99", 1), encoding="utf-8")
            with patch("sys.argv", ["run_guide_check.py", "--update", "--guide", str(path)]), \
                    patch.object(guide, "run_kit", return_value=self.trace), \
                    patch.object(guide, "manifest", return_value=self.sources):
                self.assertEqual(guide.main(), 0)
            self.assertEqual(self.check(path.read_text(encoding="utf-8")), len(self.trace["log"]))

    def test_kit_order_and_branch_drift_are_rejected(self):
        for mutate in (lambda rows: rows.reverse(), lambda rows: rows[0]["choices"].pop()):
            changed = json.loads(json.dumps(self.trace))
            mutate(changed["log"])
            with self.assertRaisesRegex(ValueError, "ordered scenes/choices"):
                self.check(self.text, changed)

    def test_stale_rules_or_kit_input_requires_review(self):
        changed = dict(self.sources, **{"src/Story.cs": "changed"})
        with self.assertRaisesRegex(ValueError, "Rules/verifier/active kit changed.*\n.*--update"):
            guide.validate(self.text, self.model, self.trace, changed)

    def test_commitment_tables_follow_executed_witnesses(self):
        steps = guide.records(self.trace)
        for step in steps:
            if step["scene"] == "delamere.trickster.woods.second_hunt":
                step["chapter"] = 5
        self.assertEqual(guide.commitment_chapters(self.model, steps)["delamere"], 5)

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
