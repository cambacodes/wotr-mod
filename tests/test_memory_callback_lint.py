import copy
from tests.story_fixture import fresh_story
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from tests.structure import without_prose
from tools import memory_callback_lint as lint
from tools.memory_callback_lint import inventory as check_inventory

class MemoryCallbackTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = fresh_story()

    def test_every_incoming_choice_and_twin(self):
        result = lint.check(self.story)
        self.assertFalse(result["callback_hard"], result["callback_hard"])
        # eng8-q8f: gameplay now supplies the awning twin; both sold-memory edges must execute.
        self.assertEqual({(r['scene'], r['via'], r['index'], r['sold_node'], r['unsold_node'])
                          for r in result['executed']}, {
            ('terendelev.trickster.bones.restitution', 'call', 0, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution', 'call', 1, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution', 'shift', 0, 'gap.wings', 'wings'),
            ('terendelev.trickster.bones.restitution_irabeth', 'call', 0, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution_irabeth', 'call', 1, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution_irabeth', 'shift', 0, 'gap.wings', 'wings'),
            ('terendelev.trickster.watch.third_bell', 'talk', 1, 'gap.gate', 'gate'),
            ('terendelev.trickster.watch.third_bell_awning', 'talk', 1, 'gap.gate', 'gate'),
        })
        self.assertEqual(result["no_change_needed"], [])

    def test_absent_third_bell_twin_is_checked_if_supplied_as_fixture(self):
        # eng8-q8f: remove the shipped twin before supplying the isolated mutation fixture.
        fixture = {"Scenes": [s for s in self.story["Scenes"]
                              if s["Id"] != "terendelev.trickster.watch.third_bell_awning"]}
        # end eng8-q8f
        twin = copy.deepcopy(next(s for s in self.story["Scenes"] if s["Id"] == "terendelev.trickster.watch.third_bell"))
        twin["Id"] += "_awning"
        fixture["Scenes"].append(twin)
        result = lint.check(fixture)
        self.assertFalse(result["callback_hard"], result["callback_hard"])
        self.assertEqual({(r['scene'], r['via'], r['index'], r['sold_node'], r['unsold_node'])
                          for r in result['executed']}, {
            ('terendelev.trickster.bones.restitution', 'call', 0, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution', 'call', 1, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution', 'shift', 0, 'gap.wings', 'wings'),
            ('terendelev.trickster.bones.restitution_irabeth', 'call', 0, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution_irabeth', 'call', 1, 'gap.voice', 'voice'),
            ('terendelev.trickster.bones.restitution_irabeth', 'shift', 0, 'gap.wings', 'wings'),
            ('terendelev.trickster.watch.third_bell', 'talk', 1, 'gap.gate', 'gate'),
            ('terendelev.trickster.watch.third_bell_awning', 'talk', 1, 'gap.gate', 'gate'),
        })
        twin["Nodes"] = [n for n in twin["Nodes"] if n["Id"] != "gap.gate"]
        self.assertTrue(lint.check(fixture)["callback_hard"])

    def test_all_prices_heard_and_unheard(self):
        from storylines import foresight as f
        scenes = {s['Id']: s for s in self.story['Scenes']}
        for contract in json.loads(lint.CONTRACTS.read_text(encoding='utf-8')):
            if contract['scene'] not in scenes:
                continue
            nodes = {n['Id']: n for n in scenes[contract['scene']]['Nodes']}
            for via in dict.fromkeys(n for n, _ in contract['vias']):
                originals = [c for c in nodes[via]['Choices'] if c.get('Next') == contract['node']]
                alternatives = [c for c in nodes[via]['Choices'] if c.get('Next') == 'gap.' + contract['node']]
                expected = [lint.structural({**old, 'Next': 'gap.' + contract['node'],
                            'Requires': list(dict.fromkeys(old['Requires'] + ['trickster.ever', contract['gone']])),
                            'Forbids': [flag for flag in old['Forbids'] if flag != contract['gone']]}) for old in originals]
                self.assertTrue(originals)
                self.assertEqual([lint.structural(twin) for twin in alternatives], expected)
                for old, twin in zip(originals, alternatives):
                    for price in (None, f.COST_PROMISE, f.COST_SQUARE, f.COST_CAVES):
                        for heard in (False, True):
                            flags = {'trickster.ever', f.ACCEPTED}
                            if price: flags.add(price)
                            if heard: flags.add('terendelev.voice_heard')
                            for key, groups in f.DERIVED.items():
                                if any(set(group) <= flags for group in groups): flags.add(key)
                            flags.update(old['Requires'])
                            shown = [c for c in (old, twin) if set(c['Requires']) <= flags and not set(c['Forbids']) & flags]
                            target = 'gap.' + contract['node'] if f.GONE_SQUARE in flags else contract['node']
                            self.assertEqual([c['Next'] for c in shown], [target])

    def test_guard_continuation_and_twin_mutations(self):
        contracts = json.loads(lint.CONTRACTS.read_text(encoding="utf-8"))
        for contract in contracts:
            if not any(s["Id"] == contract["scene"] for s in self.story["Scenes"]):
                continue
            for mutation in ("guard", "gap", "continuation"):
                story = {"Scenes": [copy.deepcopy(s) if s["Id"] == contract["scene"] else s for s in self.story["Scenes"]]}
                nodes = {n["Id"]: n for n in next(s for s in story["Scenes"] if s["Id"] == contract["scene"])["Nodes"]}
                if mutation == "guard":
                    via, index = contract["vias"][0]
                    nodes[via]["Choices"][index]["Forbids"].remove(contract["gone"])
                elif mutation == "gap":
                    nodes["gap." + contract["node"]]["Id"] = "missing_gap"
                else:
                    nodes["gap." + contract["node"]]["Choices"] = []
                self.assertTrue(lint.check(story, [contract])["callback_hard"], mutation)

def registry_fixture(text='"Good evening."'):
    story = {"Scenes": [{"Id": "fixture", "Owner": "B", "Nodes": [
        {"Id": "start", "Speaker": "B", "Text": text, "Choices": [{"Text": "Leave.", "Next": None}]}]}]}
    registry = lint.extract(story)
    for row in registry["surfaces"]:
        row["subjects"] = ["b"]
        row["review"] = {"reviewer": "fixture prose owner", "disposition": "verified"}
    return story, registry

def bind_fixture_claim(story, registry, text, kind="references"):
    """A real existing producer, not a registry-created success flag."""
    story["Scenes"].insert(0, {"Id": "rescue", "Owner": "B", "Nodes": [
        {"Id": "done", "Text": "The rescue is over.", "Choices": [
            {"Text": "Bring her home.", "Set": ["rescue.done"], "Next": None},
            {"Text": "Refuse the rescue.", "Next": None}]}]})
    story["Scenes"][1]["Nodes"][0]["Text"] = text
    refreshed = lint.extract(story)
    registry["surfaces"] = refreshed["surfaces"]
    for row in registry["surfaces"]:
        row["subjects"] = ["b"]
        row["review"] = {"reviewer": "fixture prose owner", "disposition": "verified"}
    surface = next(row for row in registry["surfaces"] if row["address"] == {
        "kind": "scene", "scene": "fixture", "node": "start", "slot": "text"})
    surface["claims"] = ["claim.rescue"]
    review = {"reviewer": "fixture semantic reviewer", "disposition": "verified"}
    registry["facts"] = [{"fact_id": "fact.rescue", "meaning": "The rescue succeeded.",
        "time_scope": "past", "subject": "b", "predicate": [["rescue.done"]],
        "producers": [{"scene": "rescue", "node": "done", "choice": 0}], "invalidators": [],
        "evidence": "The Bring her home answer produces the existing receipt.", "review": review}]
    registry["claims"] = [{"claim_id": "claim.rescue", "surface": surface["surface_id"],
        "span": [0, len(text)], "speaker": "b", "kind": kind, "facts": ["fact.rescue"],
        "time_scope": "past", "knowledge": {"mode": "none", "facts": []},
        "appearance": {"form": "none", "subject": "b", "facts": []},
        "statement": None, "exception": None, "review": review}]

class NarrativeRegistryTests(unittest.TestCase):

    def assert_valid(self, story, registry):
        before = copy.deepcopy(story)
        result = lint.check(story, contracts=[], registry=registry)
        self.assertFalse(result['hard'], result['hard'])
        self.assertTrue(result['consistency']['complete'])
        self.assertEqual(result['consistency']['proof_status'], 'not-evaluated')
        self.assertEqual([s['Id'] for s in story['Scenes']], [s['Id'] for s in before['Scenes']])
        self.assertEqual([n['Id'] for s in story['Scenes'] for n in s['Nodes']], [n['Id'] for s in before['Scenes'] for n in s['Nodes']])

    def assert_invalid(self, story, registry, expected):
        result = lint.check(story, contracts=[], registry=registry)
        self.assertTrue(result["hard"])
        self.assertIn(expected, " ".join(result["hard"]))
        self.assertFalse(result["consistency"]["complete"])

    def test_zero_claim_review_and_unreviewed_reference_siblings(self):
        story, registry = registry_fixture()
        self.assert_valid(story, registry)
        story["Scenes"][0]["Nodes"].append({"Id": "memory", "Text": "You remember the rescue.", "Choices": []})
        self.assert_invalid(story, registry, "unreviewed")
        # Discovery does not certify a zero-claim surface or an indirect claim.
        for text in ("Again, she takes your hand.", "Your mercy brought her here.", "The empty chair.", "What we agreed."):
            story, registry = registry_fixture(text)
            self.assert_invalid(story, lint.extract(story), "not verified")

    def test_changed_paragraph_gate_wording_and_locator_are_stale(self):
        story, registry = registry_fixture()
        node = story["Scenes"][0]["Nodes"][0]
        node["Paragraphs"] = [{"Text": "She came home.\r\nYou waited.", "Requires": ["rescue.done"]}]
        registry = lint.extract(story)
        for row in registry["surfaces"]:
            row["review"] = {"reviewer": "fixture owner", "disposition": "verified"}
        self.assert_valid(story, registry)
        for mutation in ("text", "gate", "move", "newline"):
            changed = copy.deepcopy(story)
            para = changed["Scenes"][0]["Nodes"][0]["Paragraphs"][0]
            if mutation == "text":
                para["Text"] += " Again."
            elif mutation == "newline":
                para["Text"] = para["Text"].replace("\r\n", "\n")
            elif mutation == "gate":
                para["Requires"] = []
            else:
                changed["Scenes"][0]["Nodes"][0]["Paragraphs"].insert(0, {"Text": "A new paragraph."})
            self.assert_invalid(changed, registry, "stale")

    def test_known_fact_unknown_fact_and_unproduced_event_bindings(self):
        story, registry = registry_fixture()
        bind_fixture_claim(story, registry, 'You remember the rescue.')
        self.assert_valid(story, registry)
        for mutation in ('fact', 'predicate', 'producer', 'arm', 'invalidator'):
            broken = copy.deepcopy(registry)
            if mutation == 'fact':
                broken['claims'][0]['facts'] = ['fact.unknown']
            elif mutation == 'predicate':
                broken['facts'][0]['predicate'] = [['registry.invented_success']]
            elif mutation == 'producer':
                broken['facts'][0]['producers'][0]['choice'] = 99
            elif mutation == 'invalidator':
                broken['facts'][0]['invalidators'] = ['registry.invented_loss']
            else:
                broken['facts'][0]['predicate'].append(['registry.invented_success'])
            self.assert_invalid(story, broken, 'registry')
        refused = copy.deepcopy(story)
        ordered_answer_2, *_ = refused['Scenes'][0]['Nodes'][0]['Choices']
        ordered_answer_2.pop('Set')
        self.assert_invalid(refused, registry, 'unknown engine flag')

    def test_appearance_witness_obligation_and_correction_bindings(self):
        story, registry = registry_fixture()
        bind_fixture_claim(story, registry, '"I saw the rescue."', kind="reacts_to")
        claim = registry["claims"][0]
        claim["knowledge"] = {"mode": "witnessed", "facts": ["fact.rescue"]}
        claim["appearance"] = {"form": "speech_now", "subject": "b", "facts": ["fact.rescue"]}
        claim["statement"] = {"family": "rescue-history", "value": "succeeded", "time_scope": "past"}
        claim["exception"] = {"kind": "correction", "reason": "Her earlier report was mistaken.", "facts": ["fact.rescue"]}
        registry["obligations"] = [{"obligation_id": "callback.rescue", "trigger": {
            "scene": "rescue", "node": "done", "choice": 0}, "owed": "acknowledge rescue", "observer": "b",
            "targets": [claim["surface"]], "window": {"delivery": "automatic", "deadline": "chapter_close"},
            "cancellations": [], "fallback": [], "review": claim["review"]}]
        self.assert_valid(story, registry)
        for field in ("knowledge", "appearance", "exception"):
            broken = copy.deepcopy(registry)
            broken["claims"][0][field]["facts"] = []
            self.assert_invalid(story, broken, "binding")
        for field in ("trigger", "targets", "window"):
            broken = copy.deepcopy(registry)
            if field == "trigger":
                broken["obligations"][0][field]["node"] = "missing"
            elif field == "targets":
                broken["obligations"][0][field] = ["missing.callback"]
            else:
                broken["obligations"][0][field]["delivery"] = "reachable_means_delivered"
            self.assert_invalid(story, broken, "registry")

    def test_complete_inventory_typed_paths_and_digests(self):
        story, _ = registry_fixture('fixture')
        scene = story['Scenes'][0]
        scene.update(Entry='fixture', Title='fixture', ReturnText='fixture')
        scene['Nodes'][0]['Paragraphs'] = [{'Text': 'fixture'}]
        sections = ('Books', 'Journals', 'Relationships', 'Glossary', 'Openers', 'NativeTextEdits', 'NativeAnswerEdits', 'NativeWorldReconciliations', 'ParentEpilogueEdits', 'ParentEpilogueLossRules')
        for section in sections:
            story[section] = {'key/with/slashes': {'Title': 'fixture', 'Text': 'fixture', 'Opening': 'fixture', 'Variants': [{'Text': 'fixture'}]}}
        story['Books']['key/with/slashes']['Sections'] = ['fixture']
        diagnostics = list(check_inventory(story))
        addresses = [row['address'] for row in diagnostics]
        expected = [{'kind': section, 'path': ['key/with/slashes', field]} for section in sections for field in ('Title', 'Text', 'Opening')]
        expected.extend({'kind': section, 'path': ['key/with/slashes', 'Variants', 0, 'Text']} for section in sections)
        expected.append({'kind': 'Books', 'path': ['key/with/slashes', 'Sections', 0]})
        expected.extend({'kind': 'scene', 'scene': 'fixture', 'slot': field} for field in ('entry', 'Title', 'ReturnText'))
        expected.extend([{'kind': 'scene', 'scene': 'fixture', 'node': 'start', 'slot': 'text'}, {'kind': 'scene', 'scene': 'fixture', 'node': 'start', 'slot': 'paragraph', 'index': 0}, {'kind': 'scene', 'scene': 'fixture', 'node': 'start', 'slot': 'choice', 'index': 0}])
        self.assertCountEqual(addresses, expected)
        self.assertCountEqual([json.dumps(a, sort_keys=True) for a in addresses], set(json.dumps(a, sort_keys=True) for a in addresses))

    def test_stable_ids_and_reviewed_span_inventory(self):
        story, registry = registry_fixture()
        bind_fixture_claim(story, registry, '"She returned."')
        callback = next((r for r in registry['surfaces'] if r['claims']))
        callback['surface_id'] = 'semantic.rescue.callback'
        registry['claims'][0]['surface'] = 'semantic.rescue.callback'
        self.assert_valid(story, registry)
        changed = copy.deepcopy(story)
        changed['Scenes'][1]['Nodes'][0]['Text'] += ' Again.'
        proposal = lint.extract(changed, registry)
        self.assert_invalid(changed, proposal, 'not verified')
        for mutation in ('duplicate', 'span', 'orphan', 'unlisted', 'extra', 'address', 'type'):
            broken = copy.deepcopy(registry)
            if mutation == 'duplicate':
                broken['claims'].append(copy.deepcopy(broken['claims'][0]))
            elif mutation == 'span':
                broken['claims'][0]['span'] = [0, 999]
            elif mutation == 'orphan':
                broken['claims'][0]['surface'] = 'missing.surface'
            elif mutation == 'unlisted':
                next((r for r in broken['surfaces'] if r['claims']))['claims'] = []
            elif mutation == 'extra':
                broken['surfaces'][0]['grant_flags'] = ['rescue.done']
            elif mutation == 'address':
                broken['surfaces'][0]['address']['kind'] = 'native_campaign'
            else:
                broken['version'] = True
            self.assert_invalid(story, broken, 'registry')

    def test_strict_loading_and_cli_report_extraction_and_check(self):
        story, registry = registry_fixture()
        with tempfile.TemporaryDirectory() as temp:
            source, sidecar = Path(temp) / "story.json", Path(temp) / "registry.json"
            source.write_text(json.dumps(story, ensure_ascii=False), encoding="utf-8")
            sidecar.write_text(json.dumps(registry), encoding="utf-8")
            argv = [sys.executable, "-m", "tools.memory_callback_lint", str(source), "--registry", str(sidecar)]
            def run(*args):
                return subprocess.run([*argv, *args], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run().returncode, 0)
            source.write_text(json.dumps(registry_fixture("An unreviewed rescue.")[0]), encoding="utf-8")
            proposed = json.loads(run("--mode", "extract").stdout)
            sidecar.write_text(json.dumps(proposed), encoding="utf-8")
            report = run("--mode", "report")
            self.assertEqual(report.returncode, 0)
            self.assertFalse(json.loads(report.stdout)["complete"])
            self.assertEqual(run().returncode, 1)
            for text in ('{"version":1,"version":2}', '{"version":NaN}', '{'):
                sidecar.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    lint.load_registry(sidecar)
                self.assertEqual(run().returncode, 1)
            sidecar.unlink()
            self.assertEqual(run().returncode, 1)
