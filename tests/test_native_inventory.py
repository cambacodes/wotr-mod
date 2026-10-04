"""eng7-l03: mapped inventory omissions/drift fail; unresolved prose stays visible."""
import copy
import hashlib
import json
from pathlib import Path
import unittest

from storylines.native_overrides import inventory, finalize
from tools.game_blueprints import find_bindings, game_dir, text_key
from tools.native_contradictions import render_inventory, localization_text

ROOT = Path(__file__).resolve().parents[1]


class NativeInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.payload = expansion.make_expansion()
        cls.expected = json.loads((ROOT / "tools/native_inventory_expectations.json").read_text(encoding="utf-8"))
        cls.backlog = json.loads((ROOT / "tools/engine_backlog.json").read_text(encoding="utf-8"))

    def test_all_45_findings_and_cited_guids_are_accounted_for(self):
        rows = inventory(self.payload, self.expected, self.backlog)
        self.assertEqual(len({r["Finding"] for r in rows}), 45)
        report, failures = render_inventory(self.payload, self.expected, self.backlog)
        self.assertGreater(failures, 0)  # a complete queue is not a clean bill of native consistency
        self.assertIn("FAIL_UNCOVERED", report)
        for row in rows:
            self.assertIn(row["Target"], report)
            self.assertIn(row["Finding"], report)
        self.assertGreater(len(self.expected["Siblings"]), 100)
        for guid in self.expected["Siblings"]:
            self.assertIn(guid, report)
        repairs = self.expected["ExistingRepairs"]
        self.assertEqual(len(repairs), 4)
        registered = {r["Target"] for r in self.payload["NativeOverrides"]}
        for guid in repairs:
            self.assertIn(guid, registered)
            self.assertIn("Data", self.expected["Fixtures"][guid])
            self.assertIn(guid, report)
        routes = {row["Route"].replace("minagho-and-chivarro", "minagho_chivarro") for row in rows}
        for scene in self.payload["Scenes"]:
            if scene.get("Relationship") in routes and scene.get("Owner", "").endswith("Epilogue"):
                self.assertIn(scene["Id"], report)  # includes unfinished, refused and late commitment outcomes

    def test_missing_duplicate_guid_dependency_and_sibling_mutations_fail(self):
        mutations = (
            lambda d: d["Findings"].pop(),
            lambda d: d["Findings"].append(copy.deepcopy(d["Findings"][0])),
            lambda d: d["Findings"][0].update(Targets=[]),
            lambda d: d["Findings"][0].update(Dependency=[["trickster.ever", "unearned.return"]]),
            lambda d: d["Findings"][0].update(Dependency=[["irabeth.trickster.returned"]]),
            lambda d: d["Fixtures"].pop(d["Siblings"][0]),
        )
        for mutate in mutations:
            data = copy.deepcopy(self.expected)
            mutate(data)
            with self.assertRaises(ValueError):
                inventory(self.payload, data, self.backlog)

    def test_serialized_native_fixtures_match_archive_and_localization(self):
        fixtures = self.expected["Fixtures"]
        native = find_bindings(game_dir() / "blueprints.zip", {g: f["Type"] for g, f in fixtures.items()})
        strings = json.loads((game_dir() / "Wrath_Data/StreamingAssets/Localization/enGB.json").read_text(encoding="utf-8"))["strings"]
        for guid, fixture in fixtures.items():
            actual = native[guid]
            self.assertEqual(fixture["Path"], actual["path"], guid)
            self.assertEqual(fixture["Key"], text_key(actual["data"].get("Text")), guid)
            self.assertEqual(fixture["DataSha256"], hashlib.sha256(json.dumps(actual["data"], sort_keys=True).encode()).hexdigest(), guid)
            self.assertEqual(fixture["TextSha256"], hashlib.sha256(localization_text(strings, actual["data"].get("Text")).encode()).hexdigest(), guid)
            if "Data" in fixture:
                self.assertEqual(fixture["Data"], {key: actual["data"][key] for key in fixture["Data"]}, guid)

    def test_q6b_registry_still_enforces_reviewed_delivery_and_actions(self):
        payload = copy.deepcopy(self.payload)
        finalize(payload)
        # Neither cue-policy omission nor localization drift can become a declaration.
        bad = copy.deepcopy(self.payload)
        bad["NativeEpilogueEdits"]["4bb3706172f1ed54ca11db96254c4638"]["Key"] = "drift"
        with self.assertRaisesRegex(ValueError, "localization key differs"):
            finalize(bad)

    def test_preserved_native_morale_does_not_claim_reconciled_authored_history(self):
        cue = "cba964e33d0a0704d847629be452b359"
        coverage = dict(Evaluations=[dict(Target=cue, Passed=True, Cases=[])])
        report, _ = render_inventory(self.payload, self.expected, self.backlog, coverage)
        rows = [line for line in report.splitlines() if line.startswith("| irabeth:002") and cue in line]
        self.assertEqual(len(rows), 1)
        self.assertIn("FAIL_UNCOVERED", rows[0])

    def test_variant_fixtures_consume_known_q6b_readers_and_paid_flags(self):
        from storylines.native_overrides import _known
        known = _known(self.payload)
        contracts = json.loads((ROOT / "tools/native_variant_inventory_contracts.json").read_text(encoding="utf-8"))
        for row in contracts["Cases"]:
            self.assertFalse(set(row["Flags"]) - known, row["Name"])


if __name__ == "__main__":
    unittest.main()
