"""eng7-f5 serialized slide fixtures: archive provenance and complete deterministic state coverage."""
import json
from pathlib import Path
import unittest

def localization_key(record):
    from tools.game_blueprints import text_key
    return text_key(record)
from tools.game_blueprints import text_key
from tools.native_epilogue_inventory import make_cases
ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / 'tests/native-cue-policy-fixtures'

class NativeCuePolicyInventoryTests(unittest.TestCase):

    def test_state_corpus_is_current_and_deterministic(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        actual = json.loads((FIXTURES / "states.json").read_text(encoding="utf-8"))
        self.assertEqual(make_cases(story), actual, "Regenerate with tools/native_epilogue_inventory.py")
        targets = set(story["NativeEpilogueEdits"])
        for control in ("off-Trickster", "unpaid", "closed", "unreturned-sacrifice", "degraded", "native-ineligible"):
            self.assertEqual(targets, {c["Target"] for c in actual["Cases"] if c["Id"].endswith("/control/" + control)})
        for case in actual["Cases"]:
            if case["Id"].endswith("/control/off-Trickster"):
                self.assertFalse(any(f == "trickster" or f.startswith("trickster.") for f in case["Flags"]))
            if case["Id"].endswith("/control/native-ineligible"):
                self.assertEqual([], case["NativeEligible"])

    def test_policy_fixture_preserves_serialized_native_evidence(self):
        fixture = json.loads((FIXTURES / 'policy.json').read_text(encoding='utf-8'))
        for target, spec in fixture['Specs'].items():
            cue = fixture['Assets'][target]
            self.assertEqual('BlueprintCue', cue['type'])
            self.assertFalse(cue['data']['ShowOnce'])
            self.assertEqual([], cue['data']['OnStop']['Actions'])
            if spec.get('Page'):
                page = fixture['Assets'][spec['Page']]['data']
                self.assertEqual([cue for cue in page['Cues'] if cue == '!bp_' + target], ['!bp_' + target])
                sequence = fixture['Assets'][spec['Sequence']]['data']
                self.assertEqual([cue for cue in sequence['Cues'] if cue == '!bp_' + spec['Page']], ['!bp_' + spec['Page']])
        arue = fixture['Assets']['78ae1bdc3b0824b4ca2ed618782f1faa']['data']
        self.assertEqual([], arue['Continue']['Cues'])
        self.assertEqual(['959237a34dfe436eb8f088b4be259daa'], fixture['ParentMutation']['Continue'])
        for target in ('ccd140dbf2603734aa323261c2445bec', '3a3e561c6b05a284d93eb3bff7b712a6'):
            spec = fixture['Specs'][target]
            self.assertNotEqual('fec3b6f28610c8a48a239f148ed3ed60', spec['Sequence'])
            actions = fixture['Assets'][target]['data']['OnShow']['Actions']
            self.assertEqual(1, len(actions))
            self.assertEqual('f96ad5fa9c59d7549adff4c90f0703ab', actions[0]['m_Image']['AssetId'])
if __name__ == '__main__':
    unittest.main()
