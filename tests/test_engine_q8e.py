"""eng8-q8e: inventory omissions, implicit staging and native fixture fidelity."""
import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from tools import native_contradictions as endings
from tools.crossroute_checks import other_woman
from tools.crossroute_checks.common import Proof, blocks
from tools import rrt_verify as V
from tools.game_blueprints import find_bindings, game_dir, text_key

ROOT = Path(__file__).resolve().parents[1]


class EngineQ8eTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import expansion
        cls.story = expansion.make_expansion()
        cls.implicit = json.loads((ROOT / 'tools/implicit_participant_inventory_contracts.json').read_text())

    def implicit_findings(self, story, scene):
        model = V.Model(story)
        nominated = {row['scene'] for row in self.implicit['consumers']}
        model.scenes = [s for s in model.scenes if s['Id'] in nominated]
        # Only L1 is needed; the whole lint's other classes are independent.
        return [f for f in other_woman.check(model, list(blocks(model)), Proof(model))
                if f['scene'] == scene and f['subject'].startswith('participant.')]

    def test_all_implicit_consumers_and_spawns_are_mutation_sensitive(self):
        for row in self.implicit['consumers']:
            self.assertFalse(self.implicit_findings(self.story, row['scene']), row['finding'])
            bad = copy.deepcopy(self.story)
            scene = next(s for s in bad['Scenes'] if s['Id'] == row['scene'])
            if row['kind'] == 'scene':
                scene['Requires'].remove(row['reader'])
            else:
                for node in scene['Nodes']:
                    for choice in node['Choices']:
                        if choice.get('Next') == row['node']:
                            choice['Requires'].remove(row['reader'])
            self.assertTrue(self.implicit_findings(bad, row['scene']), row['finding'])
            for presence in row.get('presences', []):
                bad = copy.deepcopy(self.story)
                bad['Presences'][presence]['Requires'].remove(row['reader'])
                self.assertTrue(self.implicit_findings(bad, row['scene']), presence)

    def test_departure_table_inputs_are_real_current_dependencies(self):
        model = V.Model(self.story)
        proof = Proof(model)
        from tools.crossroute_checks.common import lit
        for reader, losses in self.implicit['readers'].items():
            for loss in losses:
                self.assertTrue(proof.implies(lit(reader), lit(loss, False)), (reader, loss))
        self.assertEqual(len(self.implicit['review']), 5)
        bad = copy.deepcopy(self.story)
        bad['DerivedForbids']['participant.chivarro.available'].remove('minagho_chivarro.trickster.chivarro_sent_back')
        self.assertTrue(self.implicit_findings(bad, 'herrax.trickster.chivarro_seen'))

    def test_every_ending_target_and_history_is_required(self):
        contract = endings.ending_contracts()
        self.assertEqual(endings.check_endings(self.story), 13)
        for row in contract['Rows']:
            bad = copy.deepcopy(self.story)
            del bad[row['Field']][row['Target']]
            with self.assertRaisesRegex(ValueError, 'missing ending target'):
                endings.check_endings(bad)
            bad = copy.deepcopy(self.story)
            bad[row['Field']][row['Target']]['When'] = [['trickster.now', 'unearned.return']]
            with self.assertRaisesRegex(ValueError, 'incomplete.*histories'):
                endings.check_endings(bad)
            if row['Field'] == 'NativeEpilogueEdits':
                bad = copy.deepcopy(self.story)
                scene = next(s for s in bad['Scenes'] if s['Id'] == row['Replacements'][0])
                if scene['Id'] != row['Outcomes'][0]:
                    scene['Requires'].append('camellia.trickster.returned')
                    with self.assertRaisesRegex(ValueError, 'replacement unavailable'):
                        endings.check_endings(bad)
        bad = copy.deepcopy(contract)
        bad['Rows'].pop()
        with self.assertRaisesRegex(ValueError, 'omitted'):
            endings.check_endings(self.story, bad)

    def test_all_native_targets_and_continuations_match_archive_and_localization(self):
        fixtures = endings.ending_contracts()['Fixtures']
        actual = find_bindings(game_dir() / 'blueprints.zip', {g: f['Type'] for g, f in fixtures.items()})
        strings = json.loads((game_dir() / 'Wrath_Data/StreamingAssets/Localization/enGB.json').read_text())['strings']
        for guid, f in fixtures.items():
            record = actual[guid]
            self.assertEqual(f['Path'], record['path'])
            self.assertEqual(f['Key'], text_key(record['data'].get('Text')))
            self.assertEqual(f['DataSha256'], hashlib.sha256(json.dumps(record['data'], sort_keys=True).encode()).hexdigest())
            self.assertEqual(f['Text'], endings.localization_text(strings, record['data'].get('Text')))
            self.assertEqual(f['Data'], {k: record['data'][k] for k in f['Data']})

    def test_parent_mod_departure_checker_is_preserved(self):
        policy = endings.ending_contracts()['ParentPolicy']
        source = (ROOT / 'reference/canon-review/aranka-AranEpil.cs').read_text()
        self.assertIn('"' + policy['Etude'] + '", negate: true', source)
        self.assertIn('"' + policy['Target'] + '")).Conditions.Conditions[0] = conditionsBuilder4.Build()', source)

    def test_native_history_identity_is_mutation_sensitive(self):
        import re
        from tools import kiana_native_policy
        source_path = ROOT / 'src/NativeEpilogueEdit.cs'
        source = source_path.read_text()
        read_text = Path.read_text
        for target in endings.ending_contracts()['IdentityPreservingTargets']:
            bad_source = re.sub(r'(\["' + target + r'"\] = new Evidence.*?), textOnly: true', r'\1', source, count=1, flags=re.S)
            self.assertNotEqual(source, bad_source, target)
            def altered(path, *args, **kwargs):
                return bad_source if path == source_path else read_text(path, *args, **kwargs)
            with patch.object(Path, 'read_text', altered):
                with self.assertRaisesRegex(ValueError, 'text-only runtime inventory'):
                    kiana_native_policy.expected()
        bad = copy.deepcopy(endings.ending_contracts())
        bad['IdentityPreservingTargets'].pop()
        with self.assertRaisesRegex(ValueError, 'omitted native history'):
            endings.check_endings(self.story, bad)


if __name__ == '__main__':
    unittest.main()
