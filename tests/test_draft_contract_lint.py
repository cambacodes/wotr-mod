"""eng7-f6d: dormant mechanical contracts are strict; draft prose stays advisory."""
import unittest
from tools import draft_contract_lint as lint


class DraftContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = lint.inventory()

    # eng7-f6d begin: repaired drafts are now a mandatory mechanical gate.
    def test_all_dormant_contracts_are_clean(self):
        self.assertEqual(lint.check(self.inventory), [])

    def test_completion_branches_and_deferred_waits(self):
        scenes = {s["Id"]: s for s in self.inventory["terendelev_continuation"]["scenes"]}
        for name in ("inspection_day", "kenabres_vigil", "private_aftercare", "scale_evening"):
            scene = scenes["terendelev.continuation." + name]
            incoming = [c for n in scene["Nodes"] for c in n["Choices"] if c.get("Next") == "end"]
            self.assertEqual(len(incoming), 3, name)
            broken = __import__("copy").deepcopy(scene)
            for node in broken["Nodes"]:
                for choice in node["Choices"]:
                    if choice.get("Next") == "end": choice["Next"] = None
            self.assertTrue(any(r["code"] == "unreachable-producer" for r in lint.check_scene(broken)))
        for name in ("escape_boundary", "trickster_native_lead"):
            wait = next(n for n in scenes["terendelev.continuation." + name]["Nodes"] if n["Id"] == "wait")
            self.assertTrue(wait["Choices"][0]["Abort"], name)
        pending = next(n for n in scenes["terendelev.continuation.escape_boundary"]["Nodes"] if n["Id"] == "result_pending")
        self.assertTrue(any(c["Abort"] and not c["Requires"] for c in pending["Choices"]))

    def test_physical_attachments_preserve_proofs_and_exact_actor(self):
        import importlib
        from tools.game_blueprints import find_bindings, game_dir
        units = {}
        for name in ("terendelev_continuation", "targona_trickster_acquisition",
                     "galfrey_all_path_continuation", "wenduag_relationship_network"):
            module = importlib.import_module("storylines." + name)
            for scene in module.SCENES:
                if scene.get("Remote"): continue
                presence = module.PRESENCES[scene["InteractionHub"]]
                self.assertEqual(scene["ContactUnit"], presence["Unit"])
                self.assertEqual(presence["Mode"], "reuse-native")
                self.assertTrue(set(presence["Requires"]).issubset(scene["Requires"]))
                units[presence["Unit"]] = "BlueprintUnit"
        self.assertEqual(len(find_bindings(game_dir() / "blueprints.zip", units)), 4)

    def test_integration_preserves_live_relationship_and_dormancy(self):
        import copy, expansion
        from storylines import terendelev_continuation as draft
        payload = expansion.make_expansion()
        before = copy.deepcopy(payload["Relationships"]["terendelev"])
        draft.integrate(payload)
        self.assertEqual(payload["Relationships"]["terendelev"], before)
        prefixes = ("terendelev.continuation.", "targona.trickster_acq.", "wenduag.vellexia_network.")
        self.assertFalse(any(s["Id"].startswith(prefixes) for s in payload["Scenes"]))
        self.assertFalse(any(s["Id"].endswith(".the_space_between_orders") for s in payload["Scenes"]))

    def test_strict_verifier_rejects_a_dormant_contract_regression(self):
        import contextlib, io, tempfile
        from pathlib import Path
        from unittest.mock import patch
        from tools import rrt_verify as verify
        for rows in ([], [dict(code="missing-target", scene="draft", location="lost")]):
            report = dict(validate_errors=[], no_producer_required=[],
                          runtime=dict(duplicate_names=[], retry_dups=[]), drafts=dict(contracts=rows))
            with tempfile.TemporaryDirectory(prefix="rrt-eng7-f6d-strict-") as temp:
                args = ["rrt_verify.py", "--strict", "--text", str(Path(temp) / "report.txt")]
                with patch.object(verify.sys, "argv", args), patch.object(verify, "run", return_value=(report, "")), contextlib.redirect_stdout(io.StringIO()):
                    if rows:
                        with self.assertRaises(SystemExit) as failed: verify.main()
                        self.assertEqual(failed.exception.code, 1)
                    else:
                        verify.main()
    # eng7-f6d end

    def test_valid_dormant_graph_and_retired_stub(self):
        scene = {"Id": "dormant", "Remote": True, "Entry": '"Speak."', "Nodes": [
            {"Id": "start", "Choices": [{"Next": "end"}]}, {"Id": "end", "Choices": [{}]},
            {"Id": "old", "Choices": [{"Abort": True}]}], "RetiredNodes": {"old": "Retained old answer target, no entry in current graph."}}
        self.assertFalse(lint.check_scene(scene))
        scene["Nodes"][2]["Choices"][0]["Set"] = ["completion"]
        self.assertTrue(lint.check_scene(scene))

    def test_mutation_and_request_defer(self):
        scene = {"Id": "defer", "Remote": True, "Entry": '"Try."', "Nodes": [{"Id": "start", "Choices": [
            {"Set": ["test.requested"]}, {"Set": ["test.authorized"], "Abort": True}]}]}
        self.assertFalse(lint.check_scene(scene))
        scene["Nodes"][0]["Choices"][1]["Abort"] = False
        self.assertTrue(any(r["code"] == "deferred-once-completion" for r in lint.check_scene(scene)))

    def test_text_lints_inspect_unregistered_drafts(self):
        from tools import player_text_lint, text_structure_lint
        for name in ("galfrey_all_path_continuation", "terendelev_continuation"):
            story = {"Scenes": self.inventory[name]["scenes"]}
            self.assertTrue(player_text_lint.check(story, draft=True)["review"])
        result = text_structure_lint.check({"Scenes": self.inventory["terendelev_continuation"]["scenes"]}, draft=True)
        self.assertEqual(result["hard"], [])

    def test_every_mapped_draft_text_finding_has_a_diagnostic(self):
        import json
        from pathlib import Path
        from tools import player_text_lint, text_structure_lint
        manuscript = {"Scenes": [s for d in self.inventory.values() for s in d.get("scenes", [])]}
        player = player_text_lint.check(manuscript, draft=True)["review"]
        structure = text_structure_lint.check(manuscript, draft=True)
        findings = json.loads((Path(__file__).resolve().parents[1] / "tools/engine_backlog.json").read_text(encoding="utf-8"))["findings"]
        for f in findings:
            if f.get("item_id") not in {"E-Q7-20", "E-Q7-21"} or not f["snapshot_evidence"].get("draft_finding"):
                continue
            if f["item_id"] == "E-Q7-21":
                self.assertTrue(any(r["scene"] == f["scene"] for r in player), f["id"])
            else:
                self.assertFalse(any(r["scene"] == f["scene"] for r in structure["hard"]), f["id"])
