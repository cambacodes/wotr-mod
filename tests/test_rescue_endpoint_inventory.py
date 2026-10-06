"""eng8-q8h: mutations cannot bless retirement while losing the live plan."""
import copy
import json
from pathlib import Path
import unittest

from tools.obligation_flow_lint import rescue_endpoint_errors, lint

ROOT = Path(__file__).resolve().parents[1]


class RescueEndpointInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contracts = json.loads((ROOT / 'tools/rescue_endpoint_inventory_contracts.json').read_text(encoding="utf-8"))
        payload = json.loads((ROOT / 'development/Story.json').read_text(encoding="utf-8"))
        ids = set(cls.contracts['retired_offers']) | set(cls.contracts['live_plan'].values())
        cls.story = {'Scenes': [s for s in payload['Scenes'] if s['Id'] in ids]}

    def test_live_inventory_and_mapped_coverage(self):
        self.assertEqual(rescue_endpoint_errors(self.story), [])
        self.assertEqual(len(self.contracts['retired_offers']), 6)
        self.assertEqual(len(self.contracts['finding_ids']), 7)

    def test_reopening_each_unsupported_success_is_hard(self):
        for sid in self.contracts['retired_offers']:
            with self.subTest(scene=sid):
                broken = copy.deepcopy(self.story)
                scene = next(s for s in broken['Scenes'] if s['Id'] == sid)
                scene['Forbids'].remove('trickster.ever')
                self.assertTrue(rescue_endpoint_errors(broken))

    def test_retirement_alone_cannot_pass_without_surviving_endpoint(self):
        for key in ('producer', 'endpoint', 'return'):
            with self.subTest(surface=key):
                sid = self.contracts['live_plan'][key]
                broken = copy.deepcopy(self.story)
                broken['Scenes'] = [s for s in broken['Scenes'] if s['Id'] != sid]
                self.assertTrue(rescue_endpoint_errors(broken))

    def test_incompatible_endpoint_and_missing_preparation_are_hard(self):
        broken = copy.deepcopy(self.story)
        pickup = next(s for s in broken['Scenes'] if s['Id'] == self.contracts['live_plan']['endpoint'])
        pickup['Forbids'].append(self.contracts['live_plan']['receipt'])
        self.assertTrue(rescue_endpoint_errors(broken))
        pickup['Forbids'].remove(self.contracts['live_plan']['receipt'])
        pickup['Requires'].remove(self.contracts['live_plan']['receipt'])
        self.assertTrue(rescue_endpoint_errors(broken))

    def test_shared_obligation_lint_enforces_endpoint_inventory(self):
        broken = copy.deepcopy(self.story)
        broken['Scenes'] = [s for s in broken['Scenes'] if s['Id'] != self.contracts['live_plan']['endpoint']]
        contracts = {'obligations': [], 'rescue_endpoint_inventory': 'rescue_endpoint_inventory_contracts.json'}
        self.assertTrue(lint(broken, contracts)['hard'])
