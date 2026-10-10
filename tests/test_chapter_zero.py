"""E-new 0: chapter 0 (the Prologue) in rrt_verify's reachability walk, the rest simulator and the matrix rules tests, and
the harness-only probe story (storylines/harness_probes.py never reaches development/Story.json)."""
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
sys.path.insert(0, str(ROOT))
import rrt_verify as rv
import matrix_rules
LIST, RETURN = ('a55fc20c6f0ff56439b40d6ba53cb8d7', '159c4442a8672334c9394d9579cfd8f9')

def inline(id, lo, hi, chapters=(), requires=(), sets=()):
    return dict(Id=id, Title=id, Owner='Anevia', Relationship='zero', MinChapter=lo, MaxChapter=hi, Chapters=list(chapters), Requires=list(requires), AnswerLists=[LIST], NativeReturnCue=RETURN, Nodes=[dict(Id='start', Text='x', Choices=[dict(Text='Continue', Set=list(sets))])])

def story(*scenes):
    epilogue = dict(Id='zero.ending', Title='e', Owner='Epilogue', Relationship='zero', MinChapter=0, MaxChapter=99, Requires=['zero.committed'], Nodes=[dict(Id='start', Text='x', Choices=[dict(Text='Continue')])])
    return dict(Scenes=[epilogue] + list(scenes), Etudes={'trickster': '9f486a9c0c9abfc4a952bb22e88a7e96'}, Relationships={'zero': dict(Title='Zero', StartedFlag='zero.started', ClosedFlag='zero.closed', CommittedFlag='zero.committed')})
PROLOGUE = story(inline('zero.pro', 0, 5, chapters=[0], sets=['zero.pro_done']), inline('zero.next', 1, 5, requires=['zero.pro_done'], sets=['zero.committed']), inline('zero.later', 0, 5, requires=['chapter_later']), inline('zero.mythic', 0, 5, chapters=[0], requires=['trickster']))

class ReachTests(unittest.TestCase):

    def test_prologue_walked_only_when_a_scene_opens_there(self):
        self.assertTrue(rv.Model(PROLOGUE).prologue)
        plain = story(inline('zero.one', 1, 5, sets=['zero.committed']))
        model = rv.Model(plain)
        self.assertFalse(model.prologue, "an epilogue page's MinChapter 0 must not add a Prologue walk")
        self.assertEqual(rv.Reach(model, rv.mythic_world(None, model)).reached, {'zero.one': 1, 'zero.ending': 1})

    def test_prologue_reach(self):
        model = rv.Model(PROLOGUE)
        reach = rv.Reach(model, rv.mythic_world('trickster', model))
        self.assertEqual(reach.reached['zero.pro'], 0)
        self.assertEqual(reach.reached['zero.next'], 1, 'a Prologue flag carries into Chapter 1')
        self.assertEqual(reach.reached['zero.later'], 2, 'the Prologue holds no chapter_later')
        self.assertNotIn('zero.mythic', reach.reached, 'no mythic path is chosen in the Prologue')

class SimulatorTests(unittest.TestCase):

    def test_rest_budget_plays_the_prologue(self):
        model = rv.Model(PROLOGUE)
        result = rv.simulate_rest_budget(model)
        self.assertEqual(result['chapters'][0]['chapter'], 0)
        self.assertEqual(result['chapter_days'][0], rv.SIM_PROLOGUE_DAYS)
        zero = [r for r in result['relationships'] if r['relationship'] == 'zero'][0]
        self.assertTrue(zero['committed'] and (not zero['missed']), "the Prologue scene's flag did not carry into Chapter 1: %r" % zero)

    def test_rest_budget_unchanged_without_a_prologue_scene(self):
        model = rv.Model(story(inline('zero.one', 1, 5, sets=['zero.committed'])))
        result = rv.simulate_rest_budget(model)
        self.assertEqual([c['chapter'] for c in result['chapters']], sorted(rv.SIM_CHAPTER_DAYS))

class MatrixTests(unittest.TestCase):

    def test_world_chapter_zero(self):
        model = rv.Model(PROLOGUE)
        self.assertEqual(matrix_rules.execute_test(model, {'world': ['chapter:0'], 'expect_available': ['zero.pro'], 'expect_unavailable': ['zero.next']}, 't'), [])
        self.assertEqual(matrix_rules.execute_test(model, {'world': ['chapter:1', 'zero.pro_done'], 'expect_available': ['zero.next'], 'expect_unavailable': ['zero.pro']}, 't'), [])

class ProbeIsolationTests(unittest.TestCase):

    def test_probe_never_ships(self):
        from storylines import harness_probes
        shipped = json.loads((ROOT / 'development' / 'Story.json').read_text(encoding='utf-8'))
        ids = {s['Id'] for s in shipped['Scenes']}
        self.assertFalse(ids & set(harness_probes.PROBE_IDS), 'a harness probe is in development/Story.json')
        import ast
        tree = ast.parse((ROOT / 'expansion.py').read_text(encoding='utf-8'))
        imports = {a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names}
        self.assertNotIn('harness_probes', imports)
        self.assertNotIn('storylines.harness_probes', imports)
        reviewed = {'anevia.early.watch', 'seelah.early.pack', 'camellia.early.blood'}
        self.assertEqual(sorted((s['Id'] for s in shipped['Scenes'] if rv.opens_in_prologue(rv.norm_scene(copy.deepcopy(s))) and s['Id'] not in reviewed)), [], 'a shipped scene opens in the Prologue; review it (retcheck, replay text) and list it here')

    def test_probe_story(self):
        sys.path.insert(0, str(ROOT / 'tools'))
        import importlib.util
        spec = importlib.util.spec_from_file_location('build_harness_probes', ROOT / 'tools' / 'build-harness-probes.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        base = story(inline('zero.one', 1, 5))
        built = builder.build(base)
        self.assertEqual({s['Id'] for s in built['Scenes']}, {s['Id'] for s in base['Scenes']} | {'pacing.e0.probe'})
        probe = built['Scenes'][-1]
        self.assertEqual((probe['Id'], probe['MinChapter'], probe['MaxChapter'], probe['Chapters']), ('pacing.e0.probe', 0, 0, [0]))
        self.assertEqual((probe['AnswerLists'], probe['NativeReturnCue']), ([LIST], RETURN))
        self.assertEqual([c['Set'] for n in probe['Nodes'] for c in n['Choices']], [[]], 'the probe sets no flag')
        with self.assertRaises(ValueError):
            builder.build(built)
if __name__ == '__main__':
    unittest.main()
