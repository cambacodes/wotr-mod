"""Native facilities: fail closed at export, preserve migrations, scope history."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from storylines import native_facts as facts, native_overrides as overrides  # noqa: E402
from tools import native_contradictions as report  # noqa: E402
from tools.game_blueprints import find_bindings  # noqa: E402

CUE = "164c14743ee768f409a04f93a040e678"


def world():
    return dict(Scenes=[dict(Id="her.variant", Relationship="her", Nodes=[dict(Id="line", Text="She lives.")])],
                Relationships={"her": dict(StartedFlag="her.started", ClosedFlag="her.closed", CommittedFlag="her.committed")},
                Derived={"trickster.now": [["trickster"]], "her.recovered": [["her.committed"]]})


def spec():
    return dict(Parent="2330b54637738fe4fb92b6cd80eb68f7", Dialog="63f11843f40edd54795fcc0af3f6a20e",
                Key="8e520736-4eaa-4077-aea9-6e4b9a05e854", Replacement="her.variant",
                When=[["trickster.now", "her.recovered"]])


class NativeOverridesTests(unittest.TestCase):
    def test_unsafe_types_and_unreviewed_targets_fail_before_mutation(self):
        for kind, action in (("answer", "REPLACE"), ("objective", "REPLACE"), ("objective", "HIDE"),
                             ("bark", "REPLACE"), ("cue", "SLIDE-SWAP")):
            payload = world()
            with self.assertRaisesRegex(ValueError, "safe|unsupported"):
                overrides.declare(payload, source="test", target=CUE, target_type=kind, action=action, spec=spec())
            self.assertNotIn("NativeOverrides", payload)
        with self.assertRaisesRegex(ValueError, "cue-policy contract"):
            overrides.declare(world(), source="test", target="0" * 32, target_type="cue", action="REPLACE", spec=spec())

    def test_every_state_group_needs_path_and_known_history(self):
        for when, error in (([["trickster.now", "her.recovered"], ["her.committed"]], "every When"),
                            ([["trickster.now", "her.unearned"]], "unknown state")):
            payload = world()
            edited = dict(spec(), When=when)
            overrides.declare(payload, source="test", target=CUE, target_type="cue", action="REPLACE", spec=edited)
            with self.assertRaisesRegex(ValueError, error):
                overrides.finalize(payload, archive="not-needed.zip")

    def test_bypass_and_duplicate_target_are_rejected(self):
        payload = world()
        payload["NativeEpilogueEdits"] = {CUE: spec()}
        with self.assertRaisesRegex(ValueError, "unregistered"):
            overrides.finalize(payload, archive="not-needed.zip")
        del payload["NativeEpilogueEdits"]
        overrides.declare(payload, source="test", target=CUE, target_type="cue", action="REPLACE", spec=spec())
        with self.assertRaisesRegex(ValueError, "conflicting"):
            overrides.declare(payload, source="other", target=CUE, target_type="cue", action="REPLACE", spec=spec())

    def test_missing_and_mistyped_guids_name_evidence(self):
        with tempfile.TemporaryDirectory(prefix="rrt-q6b-") as temp:
            archive = Path(temp) / "blueprints.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("cue.jbp", json.dumps(dict(AssetId=CUE, Data={"$type": "id, BlueprintCue"})))
            with self.assertRaisesRegex(ValueError, CUE + ": expected BlueprintAnswer, found BlueprintCue"):
                find_bindings(archive, {CUE: "BlueprintAnswer"})
            with self.assertRaisesRegex(ValueError, "missing from"):
                find_bindings(archive, {"0" * 32: "BlueprintCue"})

    def test_registered_specs_are_copies_and_keep_variant_order(self):
        payload = world()
        edited = dict(spec(), Variants=[dict(Replacement="second", When=[["trickster.now", "her.committed"]])])
        old = copy.deepcopy(edited)
        overrides.register_legacy(payload, "test", edits={CUE: edited})
        self.assertEqual(payload["NativeEpilogueEdits"][CUE], old)
        edited["When"][0].append("changed")
        self.assertEqual(payload["NativeEpilogueEdits"][CUE], old)


class NativeFactsTests(unittest.TestCase):
    def test_neutral_branch_is_disjoint_without_mutating_choices(self):
        original = dict(Text="Remember it.", Next="remembered", Requires=["her.committed"])
        neutral = dict(Text="Go on.", Next="neutral")
        remembered, neutral = facts.recollection_choices(original, neutral, "eggs.manually_smashed")
        flag = facts.key("eggs.manually_smashed")
        self.assertIn(flag, remembered["Requires"])
        self.assertIn(flag, neutral["Forbids"])
        self.assertEqual(original["Requires"], ["her.committed"])
        with self.assertRaisesRegex(ValueError, "Unknown native-history"):
            facts.key("her.authored_return")

    def test_distinct_causes_and_herald_outcomes_are_not_collapsed(self):
        names = ("eggs.manually_smashed", "eggs.golem_wrong_password", "eggs.commanded_destruction", "eggs.watched_crushing")
        self.assertEqual(len({facts.FACTS[n].guids for n in names}), len(names))
        herald = ("herald.heart_restored", "herald.returned_to_heaven", "herald.exiled")
        self.assertEqual(len({facts.FACTS[n].guids for n in herald}), len(herald))

    def test_history_citation_drift_fails_build(self):
        with tempfile.TemporaryDirectory(prefix="rrt-q6b-") as temp:
            archive = Path(temp) / "blueprints.zip"
            with ZipFile(archive, "w") as z:
                z.writestr("observed.jbp", json.dumps(dict(AssetId=CUE, Data={"$type": "id, BlueprintCue"})))
            wrong = facts.Fact("SelectedAnswers", (CUE,), "Selected the answer", ("observed.jbp",), "audit.json")
            with self.assertRaisesRegex(ValueError, "GUID/type mismatch"):
                facts.verify(archive, {"bad": wrong})
            with ZipFile(archive, "a") as z:
                z.writestr("unrecorded.jbp", json.dumps(dict(AssetId=CUE, Data={"$type": "id, BlueprintAnswer", "AddToHistory": False})))
            unrecorded = facts.Fact("SelectedAnswers", (CUE,), "Selected the answer", ("unrecorded.jbp",), "audit.json")
            with self.assertRaisesRegex(ValueError, "not recorded in native history"):
                facts.verify(archive, {"unrecorded": unrecorded})


class ContradictionReportTests(unittest.TestCase):
    def test_shared_text_pronoun_slide_coverage_and_unreturned_route(self):
        payload = dict(Relationships={"her": {"TricksterAccess": {"dead": {"Returned": "her.returned"}}},
                                      "other": {}}, Scenes=[], NativeOverrides=[{"Target": "covered"}])
        records = [("World/Dialogs/Epilogues/BookPage_1.jbp", {"AssetId": "page", "Data": {
                    "$type": "id, BlueprintBookPage", "Cues": ["!bp_name", "!bp_pronoun", "!bp_covered"]}})]
        for guid, key in (("name", "name"), ("pronoun", "death"), ("covered", "covered")):
            records.append(("World/Dialogs/Epilogues/" + guid + ".jbp", {"AssetId": guid, "Data": {
                "$type": "id, BlueprintCue", "Text": {"m_Key": "", "Shared": {"stringkey": key}}}}))
        # Another page's death must not borrow this woman's name.
        records.append(("World/Dialogs/Epilogues/unrelated.jbp", {"AssetId": "unrelated", "Data": {
            "$type": "id, BlueprintCue", "Text": {"m_Key": "death"}}}))
        routes, candidates, covered = report.scan(payload, records, {"name": "Her survived.", "death": "She died.", "covered": "Her vanished."})
        self.assertEqual(set(routes), {"her"})
        self.assertEqual([c["guid"] for c in candidates["her"]], ["pronoun"])
        self.assertEqual(covered["her"], 1)

    def test_a_hub_does_not_assign_all_deaths_to_every_woman_it_mentions(self):
        payload = dict(Relationships={route: {"UnavailableOverrides": {"dead": route + ".returned"}}
                                      for route in ("her", "other")}, Scenes=[])
        records = [("World/Dialogs/NPC_Common/Her/" + guid + ".jbp", {"AssetId": guid, "Data": {
                    "$type": "id, BlueprintCue", "Text": {"m_Key": guid}}}) for guid in ("name", "death")]
        _, candidates, _ = report.scan(payload, records, {"name": "Other smiles.", "death": "She died."})
        self.assertEqual([row["guid"] for row in candidates["her"]], ["death"])
        self.assertFalse(candidates["other"])

    def test_indirect_native_mourning_and_completed_life_language(self):
        lines = {"irabeth": "It's sad that Irabeth won't come into the kitchen.",
                 "terendelev": "We all know how Terendelev's story ended.",
                 "arueshalae": "Arueshalae's wandering had only just begun."}
        payload = dict(Relationships={route: {"UnavailableOverrides": {"dead": route + ".returned"}} for route in lines}, Scenes=[])
        records = [("World/Dialogs/Hub/" + route + ".jbp", {"AssetId": route, "Data": {
                    "$type": "id, BlueprintCue", "Text": {"m_Key": route}}}) for route in lines]
        _, candidates, _ = report.scan(payload, records, lines)
        for route in lines:
            self.assertEqual([row["guid"] for row in candidates[route]], [route])


class ShippedNativeMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.payload = expansion.make_expansion()

    def test_all_existing_native_specs_are_registered_and_unchanged(self):
        from storylines import devarra_native, kiana_native, camellia_native, areelu_afterlogue, wenduag_native, galfrey_queen_slide, arueshalae_rounds
        payload = self.payload
        # eng8-q8e begin: only declared ending eligibility changes during migration.
        from tools.native_contradictions import ending_contracts, ending_when
        rows = {(r["Field"], r["Target"]): r for r in ending_contracts()["Rows"]}
        scenes = {s["Id"]: s for s in payload["Scenes"]}
        def final_spec(field, cue, original):
            expected = copy.deepcopy(original)
            row = rows.get((field, cue))
            if row:
                outcomes = [scenes[id] for id in row["Outcomes"]]
                if field == "NativeEpilogueSuppressions":
                    expected["When"] = [group for s in outcomes for group in ending_when(s)]
                else:
                    for variant, outcome in zip([expected, *expected.get("Variants", [])], outcomes):
                        variant["When"] = ending_when(outcome)
            return expected
        # eng8-q8e end
        for module in (devarra_native, kiana_native, camellia_native, areelu_afterlogue, wenduag_native, galfrey_queen_slide, arueshalae_rounds):
            for cue, expected in module.NATIVE_EPILOGUE_EDITS.items():
                self.assertEqual(payload["NativeEpilogueEdits"][cue], final_spec("NativeEpilogueEdits", cue, expected), cue)
        for cue, expected in camellia_native.NATIVE_EPILOGUE_SUPPRESSIONS.items():
            self.assertEqual(payload["NativeEpilogueSuppressions"][cue], final_spec("NativeEpilogueSuppressions", cue, expected), cue)
        actual = {(row["Field"], row["RuntimeKey"]) for row in payload["NativeOverrides"]}
        expected = {(field, key) for field in overrides.FIELDS for key in payload.get(field, {})}
        self.assertEqual(actual, expected)

    def test_verified_history_is_read_only_and_uses_existing_readers(self):
        for name, fact in facts.FACTS.items():
            flag = facts.key(name)
            self.assertIn(flag, self.payload[fact.reader])
            if fact.reader == "Etudes":
                self.assertIn(flag, self.payload["PermanentEtudes"])
        sets = {flag for scene in self.payload["Scenes"] for node in scene["Nodes"]
                for choice in node.get("Choices", []) for flag in choice.get("Set", [])}
        self.assertFalse(any(flag.startswith(facts.PREFIX) for flag in sets))


if __name__ == "__main__":
    unittest.main()
