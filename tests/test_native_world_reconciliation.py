"""eng7-l04: serialized/native fixtures and negative adapter/target mutations."""
import copy
import json
from pathlib import Path
import re
import unittest

from expansion import make_expansion
from storylines import native_overrides as registry
from tools import native_gate_contract_lint as gate

ROOT = Path(__file__).resolve().parents[1]


class NativeWorldInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = make_expansion()
        cls.found = registry.finalize(cls.story)

    def test_every_mapped_site_is_registered_with_native_evidence(self):
        targets = {registry.BURIAL, registry.PRISON, registry.ESCAPE, *registry.JOURNALS}
        rows = {r["Target"]: r for r in self.story["NativeOverrides"] if r["Field"] == "NativeWorldReconciliations"}
        self.assertEqual(set(rows), targets)
        self.assertEqual(set(self.story["NativeWorldReconciliations"]), targets)
        for target in targets:
            self.assertEqual(rows[target]["Evidence"], self.found[target]["path"])
            self.assertTrue(rows[target]["Authored"])
        source = (ROOT / "src/NativeWorldReconciliation.cs").read_text()
        ids = re.findall(r'"([a-f0-9-]{36})"', source.split("CorpseIds =", 1)[1].split("};", 1)[0])
        self.assertEqual(tuple(ids), registry.CORPSE_IDS)

    def test_burial_native_fixture_contains_exactly_four_target_displays_and_keeps_siblings(self):
        data = self.found[registry.BURIAL]["data"]
        displays = [r for r in registry._walk(data) if r.get("$type", "").endswith(", HideMapObject")]
        all_ids = {r["MapObject"]["MapObject"]["_entity_id"] for r in displays}
        self.assertTrue(set(registry.CORPSE_IDS) < all_ids)  # Several unrelated native displays also exist.
        self.assertEqual(len([r for r in displays if r["MapObject"]["MapObject"]["_entity_id"] in registry.CORPSE_IDS]), 4)
        self.assertTrue(all(r["Unhide"] for r in displays if r["MapObject"]["MapObject"]["_entity_id"] in registry.CORPSE_IDS))
        # The production visibility lease's reload/disable/save-transition checks run in RulesTests.

    def test_world_target_drift_rejected_before_publication(self):
        for target in self.story["NativeWorldReconciliations"]:
            found = copy.deepcopy(self.found)
            data = found[target]["data"]
            if target == registry.BURIAL:
                row = next(r for r in registry._walk(data) if r.get("$type", "").endswith(", HideMapObject")
                           and r["MapObject"]["MapObject"]["_entity_id"] in registry.CORPSE_IDS)
                row["MapObject"]["MapObject"]["SceneAssetGuid"] = "0" * 32
            elif target == registry.PRISON:
                trigger = next(t for t in data["Components"] if t.get("Comment") == "Spawn Minagho in cell")
                trigger["Actions"]["Actions"][1]["ScriptZone"]["_entity_id"] = "unreviewed"
            elif target == registry.ESCAPE:
                data["EnterActions"]["Actions"][0]["m_Cutscene"] = "!bp_" + "0" * 32
            else:
                data["Description"]["m_Key"] = "unreviewed"
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "evidence differs"):
                registry.verify_world_targets(self.story, found)

    def test_minagho_fixture_retirement_is_only_the_prison_trigger_and_escape_guard(self):
        native = self.found[registry.PRISON]["data"]
        triggers = [c for c in native["Components"] if c.get("Comment") == "Spawn Minagho in cell"]
        self.assertEqual(len(triggers), 1)
        actions = triggers[0]["Actions"]["Actions"]
        self.assertEqual([a["$type"].split(", ")[-1] for a in actions], ["Spawn", "ScriptZoneActivate"])
        self.assertEqual(actions[0]["Spawners"][0]["_entity_id"], "9bf297f2-559f-4823-8471-c9761999538a")
        # Death etude and all unrelated prison triggers remain in the original native record.
        self.assertTrue(any(c["$type"].endswith(", EvaluatedUnitDeathTrigger") for c in native["Components"]))
        zone = self.found[registry.ESCAPE]["data"]
        self.assertEqual(zone["EnterActions"]["Actions"][0]["m_Cutscene"], "!bp_ee638b3fc29d95848aee5bdb74821aaf")
        for target in (registry.PRISON, registry.ESCAPE):
            self.assertEqual(self.story["NativeWorldReconciliations"][target]["When"],
                             [["trickster.now", "minagho_chivarro.trickster.minagho_in"]])

    def test_journal_keys_are_reviewed_and_partial_does_not_select_paid_descriptions(self):
        for target, spec in self.story["NativeWorldReconciliations"].items():
            if target not in registry.JOURNALS:
                continue
            native = self.found[target]["data"]
            self.assertEqual(registry.text_key(native["Description"]), spec["DescriptionKey"])
            if spec["TitleKey"]:
                self.assertEqual(registry.text_key(native["Title"]), spec["TitleKey"])
            self.assertFalse(registry.world_group_supported(target, "kiana", list(gate.requirements()[1])))
            for group in spec["When"]:
                self.assertTrue(registry.world_group_supported(target, "kiana", group))
                self.assertFalse(registry.world_group_supported(target, "kiana", [f for f in group if f != "trickster.now"]))
        # Q3 progress/XP/addendums/locations are read, not serialized as replacement state.
        for spec in self.story["NativeWorldReconciliations"].values():
            self.assertFalse({"Components", "m_FinishParent", "m_Objectives", "m_NextObjectives"}.intersection(spec))

    def test_unreviewed_types_actions_and_earned_states_fail(self):
        spec = self.story["NativeWorldReconciliations"][registry.BURIAL]
        with self.assertRaisesRegex(ValueError, "reviewed world"):
            registry.declare({}, source="mutation", target=registry.BURIAL, target_type="quest", action="HIDE-OBJECTS", spec=spec)
        with self.assertRaisesRegex(ValueError, "reviewed world"):
            registry.declare({}, source="mutation", target="0" * 32, target_type="etude", action="HIDE-OBJECTS", spec=dict(spec, Target="0" * 32))
        for target, spec in self.story["NativeWorldReconciliations"].items():
            self.assertFalse(registry.world_group_supported(target, spec["Relationship"], ["trickster.now"]))


class NativeGateParityTests(unittest.TestCase):
    def test_supported_full_partial_and_unsupported_groups(self):
        full, partial = gate.requirements()
        for group in (["trickster.now", f] for f in full):
            self.assertTrue(gate.supported(group))
        self.assertTrue(gate.supported(list(partial)))
        for group in (["trickster.ever", full[0]], *([f for f in partial if f != omitted] for omitted in partial),
                      ["trickster.now", "kiana.trickster.unreviewed"]):
            self.assertFalse(gate.supported(group))
            with self.assertRaisesRegex(ValueError, "NG14"):
                gate.validate({"NativeGates": {"kiana.q3_recovery": dict(Target="2b4a5c01a192d1f4aa8c9d32aa149727",
                    Relationship="kiana", When=[group])}})

    def test_route_merge_still_declares_only_earned_full_recovery(self):
        from storylines.kiana_native import NATIVE_GATES
        self.assertEqual(NATIVE_GATES["kiana.q3_recovery"]["When"], [["trickster.now", flag] for flag in gate.requirements()[0]])
        gate.validate({"NativeGates": NATIVE_GATES})


if __name__ == "__main__":
    unittest.main()
