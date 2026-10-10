"""C1/C4 behavioral contracts through the expansion command and draft inventory."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from authoring import generation_errors as collector
from authoring.compiler import compile_story
from storylines import anevia_heat, elyanka_cloud, heat_text

ROOT = Path(__file__).resolve().parents[1]


def payload():
    return {"Scenes": [{"Id": sid, "Remote": True, "Nodes": [
        {"Id": "start", "Text": "old tail", "Choices": [{"Id": "choice", "Text": "choice", "Next": "end", "Set": ["proof"]}]},
        {"Id": "end", "Text": "done", "Choices": [], "Paragraphs": []}]} for sid in ("s1", "s2")]}


class CompleteGenerationTests(unittest.TestCase):
    def command(self, body=None, *, existing=None, startup_failure=False, writer_failure=False):
        # A fresh process runs the actual CLI dispatch, compiler and writer.
        # Replacing only assembly lets each failure address be independently known.
        with tempfile.TemporaryDirectory(prefix="rrt-modc-c1-") as folder:
            output = Path(folder) / "Story.json"
            report = Path(folder) / "report.json"
            if existing is not None:
                output.write_bytes(existing)
            env = {**os.environ, "RRT_STORY_OUTPUT": str(output), "RRT_GENERATION_REPORT": str(report),
                   "PYTHONDONTWRITEBYTECODE": "1"}
            if startup_failure:
                argv = [sys.executable, "-c", '\n'.join([
                    'import builtins, runpy',
                    'original = builtins.__import__',
                    'def importing(name, *args, **kwargs):',
                    '    if name == "story": raise RuntimeError("injected import failure")',
                    '    return original(name, *args, **kwargs)',
                    'builtins.__import__ = importing',
                    'runpy.run_path("expansion.py", run_name="__main__")'])]
            elif body is None:
                argv = [sys.executable, "expansion.py"]
            else:
                script = '''import runpy
from unittest.mock import patch
from tests.test_modc_c1c4 import payload
from storylines import heat_text
import expansion

def build(**kwargs):
    data = payload()
''' + body + '''\n    return data
with patch.object(expansion, "_make_expansion", build):
    runpy.run_path("expansion.py", run_name="__main__")
'''
                if writer_failure:
                    script = script.replace('with patch.object(expansion, "_make_expansion", build):', '\n'.join([
                        'def failing_writer(destination, compiled):',
                        '    destination.write_bytes(b"partial")',
                        '    raise OSError("injected write failure")',
                        'with patch.object(expansion, "_make_expansion", build), patch("authoring._serialization.write_story", failing_writer):']))
                argv = [sys.executable, "-c", script]
            completed = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, encoding="utf-8", timeout=600)
            raw = report.read_bytes()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
            result = json.loads(raw.decode("utf-8"))
            self.assertEqual(set(result), {"version", "complete", "export_written", "errors"})
            self.assertEqual(result["version"], 1)
            for error in result["errors"]:
                self.assertTrue(error["code"])
                self.assertLessEqual(set(error), {"code", "scene", "node", "source", "detail"})
            return completed.returncode, result, output.read_bytes() if output.exists() else None

    def test_real_cli_success(self):
        code, report, raw = self.command()
        self.assertEqual(code, 0)
        self.assertEqual(report["errors"], [])
        self.assertTrue(report["complete"])
        self.assertTrue(report["export_written"])
        self.assertGreater(len(json.loads(raw)["Scenes"]), 0)

    def test_two_overlay_failures_and_delivery_rules_in_one_run(self):
        code, report, raw = self.command('''    heat_text.swap(data, [("s1", "start"), ("s2", "start")], "missing", "new")
    data["Scenes"][0].update(EntryMythic="Trickster", EntryAlignment="Good")
    data["Scenes"][1].update(Kind="invalid", ContinueBefore="cue")''')
        self.assertNotEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertIsNone(raw)
        self.assertEqual([(e["code"], e["scene"], e.get("node")) for e in report["errors"]], [
            ("heat.swap_snippet", "s1", "start"), ("heat.swap_snippet", "s2", "start"),
            ("scene.delivery", "s1", None), ("scene.delivery", "s1", None),
            ("scene.delivery", "s2", None), ("scene.delivery", "s2", None)])

    def test_failure_preserves_existing_export(self):
        old = b'{"previous":true}\r\n'
        code, report, raw = self.command('    heat_text.swap(data, [("s1", "start")], "missing", "new")', existing=old)
        self.assertNotEqual(code, 0)
        self.assertFalse(report["export_written"])
        self.assertEqual(raw, old)

    def test_unanticipated_exception_keeps_errors_but_marks_incomplete(self):
        code, report, raw = self.command('''    heat_text.swap(data, [("s1", "start")], "missing", "new")
    raise RuntimeError("injected")''')
        self.assertNotEqual(code, 0)
        self.assertFalse(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertEqual([e["code"] for e in report["errors"]], ["heat.swap_snippet", "generation.exception"])
        self.assertIsNone(raw)

    def test_import_failure_also_produces_a_report(self):
        code, report, raw = self.command(startup_failure=True)
        self.assertNotEqual(code, 0)
        self.assertFalse(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertEqual([e["code"] for e in report["errors"]], ["generation.exception"])
        self.assertIsNone(raw)

    def test_writer_failure_leaves_no_partial_export(self):
        for previous in (None, b'{"previous":true}\r\n'):
            with self.subTest(previous=previous):
                code, report, raw = self.command('', existing=previous, writer_failure=True)
                self.assertNotEqual(code, 0)
                self.assertFalse(report["complete"])
                self.assertFalse(report["export_written"])
                self.assertEqual([e["code"] for e in report["errors"]], ["generation.exception"])
                self.assertEqual(raw, previous)

    def test_success_preserves_destination_newlines_and_utf8(self):
        code, report, raw = self.command('    data["Marker"] = "é"', existing=b'{}\r\n')
        self.assertEqual(code, 0)
        self.assertEqual(report["errors"], [])
        self.assertTrue(report["export_written"])
        self.assertIn(b"\r\n", raw)
        self.assertNotIn(b"\n", raw.replace(b"\r\n", b""))
        self.assertEqual(json.loads(raw)["Marker"], "é")

    def test_duplicate_resolution_and_snippets_collect_without_editing(self):
        data = payload()
        data["Scenes"].append(copy.deepcopy(data["Scenes"][0]))
        data["Scenes"][1]["Nodes"].append(copy.deepcopy(data["Scenes"][1]["Nodes"][0]))
        original = copy.deepcopy(data)
        with collector.collecting():
            heat_text.swap(data, [("s1", "start"), ("s2", "start")], "old", "new")
            self.assertEqual([e["code"] for e in collector.errors], ["heat.scene_resolution", "heat.node_resolution"])
            self.assertEqual(data, original)
        data = payload()
        data["Scenes"][0]["Nodes"][0]["Text"] = "tail tail"
        with collector.collecting():
            heat_text.swap(data, [("s1", "start")], "tail", "new")
            heat_text.extend(data, [("s1", "start")], "tail", "addition")
            self.assertEqual([e["code"] for e in collector.errors], ["heat.swap_snippet", "heat.extend_tail"])
            self.assertEqual(data["Scenes"][0]["Nodes"][0]["Text"], "tail tail")

    def test_all_private_node_helpers_use_the_shared_collector(self):
        import importlib
        names = ("arueshalae", "camellia", "devarra", "herrax", "horzalah", "jerribeth",
                 "melazmera", "minachiv", "nurah", "vellexia", "wenduag")
        for name in names:
            with self.subTest(module=name), collector.collecting():
                module = importlib.import_module("storylines." + name + "_cloud")
                for sid in ("s1", "s2"):
                    with collector.overlay_item():
                        module._node({}, sid, "start")
                expected = ["jerribeth.s1", "jerribeth.s2"] if name == "jerribeth" else ["s1", "s2"]
                self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors],
                                 [("overlay.scene_resolution", sid, "start") for sid in expected])
                self.assertTrue(all(e["source"] == "storylines/" + name + "_cloud.py" for e in collector.errors))

    def test_private_swap_and_paragraph_targets_keep_running(self):
        from storylines import horzalah_cloud as cloud
        data = payload()
        original = copy.deepcopy(data)
        with collector.collecting(), patch.multiple(cloud, TEXT={
                ("s1", "start"): ("missing-a", "new"), ("s2", "start"): ("missing-b", "new")},
                PARA={("s1", "end", (), ()): ("missing-p", "new")}, ADD={}, BOOK={}):
            cloud.integrate(data)
            self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors], [
                ("overlay.text_mismatch", "s1", "start"), ("overlay.text_mismatch", "s2", "start"),
                ("overlay.text_mismatch", "s1", "end")])
            self.assertEqual(data, original)

    def test_base_phase_errors_do_not_stop_expansion_phase(self):
        import expansion, story
        base = payload()
        base["Scenes"][0]["EntryMythic"] = "Trickster"
        def assemble(**kwargs):
            compiled = compile_story("base")
            heat_text.swap(compiled.payload, [("s2", "start")], "missing", "new")
            return compiled.payload
        with patch.object(story, "_make_story", return_value=base), patch.object(expansion, "_make_expansion", assemble):
            with self.assertRaises(collector.GenerationErrors):
                compile_story("expansion")
        self.assertEqual([e["code"] for e in collector.errors], ["scene.delivery", "heat.swap_snippet"])

    def test_private_row_overlays_collect_each_target(self):
        from storylines.harem_rows import zzz_hepzamirah_cloud as hep, zzz_minachiv_pairs as pairs
        data = payload()
        original = copy.deepcopy(data)
        targets = {("s1", "start"): "new", ("s2", "start"): "new"}
        with collector.collecting(), patch.multiple(hep, PLACEHOLDERS=targets, NODES={}, PARA_TEXT={}, PARAS={}):
            hep.register(data, {}, {})
            self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors], [
                ("overlay.text_mismatch", "s1", "start"), ("overlay.text_mismatch", "s2", "start")])
            self.assertEqual(data, original)
        with collector.collecting(), patch.object(pairs, "TEXTS", targets):
            pairs.register(data, {}, {})
            self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors], [
                ("overlay.text_mismatch", "s1", "start"), ("overlay.text_mismatch", "s2", "start")])
            self.assertEqual(data, original)

    def test_private_voice_helper_retains_exported_addresses(self):
        from storylines import jerribeth_voice as voice
        with collector.collecting():
            voice._apply({}, {("s1", "start"): "new", ("s2", "start"): "new"}, {}, {})
            self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors], [
                ("overlay.scene_resolution", "jerribeth.s1", "start"),
                ("overlay.scene_resolution", "jerribeth.s2", "start")])

    def test_unanticipated_system_exit_is_an_incomplete_failure(self):
        code, report, raw = self.command('    raise SystemExit(0)')
        self.assertNotEqual(code, 0)
        self.assertFalse(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertEqual([e["code"] for e in report["errors"]], ["generation.exception"])
        self.assertIsNone(raw)

    def test_all_physical_delivery_rules_are_collected(self):
        code, report, raw = self.command('    data["Scenes"][0].update(Remote=False, Kind="invalid", ManualOnly=True, TableHosted=True)')
        self.assertNotEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertIsNone(raw)
        self.assertEqual([(e["code"], e["scene"]) for e in report["errors"]], [("scene.delivery", "s1")] * 5)
        self.assertEqual(len({e["detail"] for e in report["errors"]}), 5)

    def test_private_overlay_failures_are_complete_through_cli(self):
        code, report, raw = self.command('''    from storylines import horzalah_cloud as cloud
    from unittest.mock import patch
    with patch.multiple(cloud, TEXT={("s1", "start"): ("absent-a", "new"), ("s2", "start"): ("absent-b", "new")}, PARA={}, ADD={}, BOOK={}):
        cloud.integrate(data)''')
        self.assertNotEqual(code, 0)
        self.assertTrue(report["complete"])
        self.assertFalse(report["export_written"])
        self.assertIsNone(raw)
        self.assertEqual([(e["code"], e["scene"], e["node"], e["source"]) for e in report["errors"]], [
            ("overlay.text_mismatch", "s1", "start", "storylines/horzalah_cloud.py"),
            ("overlay.text_mismatch", "s2", "start", "storylines/horzalah_cloud.py")])

    def test_flag_overlay_collects_bad_choices_and_keeps_valid_state(self):
        from storylines import yaniel_radiance as cloud
        data = payload()
        first = data["Scenes"][0]["Nodes"][0]["Choices"][0]
        first.update(Requires=[], Forbids=[])
        second = data["Scenes"][1]["Nodes"][0]["Choices"][0]
        second.update(Requires=[cloud.HELD], Forbids=[])
        with collector.collecting(), patch.multiple(cloud, PARTY_ITEMS={}, DERIVED={},
                CHOICES={("s1", "start"): [0, 3], ("s2", "start"): [0]},
                EPILOGUE_PAGES=[], SCENE_REQUIRES=[], _reconcile_lastcall=lambda data: None), \
                patch.object(cloud.yt, "integrate_partner_memory", lambda data: None):
            cloud.integrate(data)
            self.assertEqual([(e["code"], e["scene"], e["node"]) for e in collector.errors], [
                ("overlay.choice_gate", "s1", "start"), ("overlay.index_resolution", "s1", "start")])
        self.assertEqual(first["Requires"], [])
        self.assertEqual(second["Requires"], [cloud.IN_HAND])
        self.assertEqual(second["Set"], ["proof"])
        self.assertEqual(second["Next"], "end")
        self.assertEqual(second["Id"], "choice")

    def test_helper_siblings_resolution_tails_and_structure(self):
        data = payload()
        original = copy.deepcopy(data)
        with collector.collecting():
            heat_text.swap(data, [("lost", "start"), ("s1", "lost"), ("s1", "start")], "missing" * 20, "new")
            heat_text.extend(data, [("s1", "start"), ("s2", "start")], "old", "addition")
            anevia_heat.retail(data, [("lost", "start"), ("s1", "start")], "missing", "new")
            heat_text.paragraph(data, "s2", "lost", "ignored")
            self.assertEqual([e["code"] for e in collector.errors], [
                "heat.scene_resolution", "heat.node_resolution", "heat.swap_snippet",
                "heat.extend_tail", "heat.extend_tail", "heat.scene_resolution", "heat.retail_tail", "heat.node_resolution"])
            self.assertEqual(len(collector.errors[2]["detail"]), 70)
            self.assertEqual(data, original)
        with collector.collecting():
            heat_text.swap(data, [("s1", "start"), ("s2", "start")], "old", "new")
            heat_text.extend(data, [("s1", "start")], "tail", "added")
            anevia_heat.retail(data, [("s2", "start")], "tail", "replacement")
            heat_text.paragraph(data, "s1", "end", "added", requires=("proof",), forbids=("closed",))
            self.assertEqual(collector.errors, [])
        self.assertEqual(data["Scenes"][0]["Nodes"][0]["Text"], "new tail\nadded")
        self.assertEqual(data["Scenes"][1]["Nodes"][0]["Text"], "new replacement")
        for actual, before in zip(data["Scenes"], original["Scenes"]):
            self.assertEqual(actual["Id"], before["Id"])
            self.assertEqual([n["Id"] for n in actual["Nodes"]], [n["Id"] for n in before["Nodes"]])
            self.assertEqual(actual["Nodes"][0]["Choices"], before["Nodes"][0]["Choices"])
        self.assertEqual(data["Scenes"][0]["Nodes"][1]["Paragraphs"][0]["Requires"], ["proof"])

    def test_private_paragraph_overlay_collects_each_missing_entry(self):
        data = payload()
        with collector.collecting():
            elyanka_cloud._paragraphs(data, ["lost", "s1"], {"absent-a": "x", "absent-b": "y"})
            self.assertEqual([e["code"] for e in collector.errors], [
                "overlay.scene_resolution", "overlay.paragraph_snippet", "overlay.paragraph_snippet"])
            self.assertEqual({e["detail"] for e in collector.errors if "detail" in e}, {"absent-a", "absent-b"})
            self.assertTrue(all(e["source"] == "storylines/elyanka_cloud.py" for e in collector.errors))

    def test_compilation_sessions_do_not_leak(self):
        import expansion
        bad = payload()
        bad["Scenes"][0]["EntryMythic"] = "Trickster"
        with patch.object(expansion, "_make_expansion", return_value=bad):
            with self.assertRaises(collector.GenerationErrors):
                compile_story("expansion")
        with patch.object(expansion, "_make_expansion", return_value=payload()):
            self.assertEqual([s["Id"] for s in compile_story("expansion").payload["Scenes"]], ["s1", "s2"])
            self.assertEqual(collector.errors, [])


class CleanCheckoutTests(unittest.TestCase):
    def test_disposable_inventory_has_authoring_without_pythonpath(self):
        from tools import draft_contract_lint as lint
        # The production inventory itself creates the disposable checkout.
        # Clear both shortcuts so host path/cache cannot supply its packages.
        env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "RRT_GATE_DRAFT_INVENTORY")}
        with patch.dict(os.environ, env, clear=True):
            inventory = lint._build_inventory(ROOT)
        self.assertIn("terendelev_continuation", inventory)
        self.assertTrue(inventory["terendelev_continuation"]["scenes"])
        self.assertEqual(lint.check(inventory), [])
