"""eng7-l09: authoring failures remain separate from shipped strict failures."""
import unittest
from tools import draft_contract_lint as lint


class DraftContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = lint.inventory()

    def test_mapped_delivery_and_graph_findings(self):
        rows = lint.check(self.inventory)
        for path in ("angel", "azata", "aeon", "trickster", "demon", "devil", "dragon", "legend"):
            codes = {r["code"] for r in rows if r["scene"] == "galfrey." + path + ".the_space_between_orders"}
            self.assertTrue({"no-physical-attachment", "literal-node-entry"}.issubset(codes))
        for scene in ("inspection_day", "kenabres_vigil", "private_aftercare", "scale_evening"):
            self.assertTrue(any(r["scene"] == "terendelev.continuation." + scene and r["code"] == "unreachable-producer" for r in rows), scene)
        self.assertTrue(any(r["scene"] == "terendelev.continuation.escape_boundary" and r["code"] == "deferred-once-completion" for r in rows))
        self.assertTrue(any(r["module"] == "terendelev_continuation" and r["code"] == "integration_error" for r in rows))

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
        self.assertTrue(any(r["code"] == "orphan-narration-closer" for r in result["hard"]))

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
            rows = player if f["item_id"] == "E-Q7-21" else structure["hard"] + structure["review"]
            self.assertTrue(any(r["scene"] == f["scene"] for r in rows), f["id"])
