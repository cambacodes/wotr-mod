"""Reviewed Terendelev references cannot exempt a new physical cameo."""
import hashlib
import json
from pathlib import Path
import re
import unittest

from tests.story_fixture import fresh_story
from tools.crossroute_checks.mention_context import live_mentions



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class TerendelevReferenceContextsTests(unittest.TestCase):
    def test_classifications_match_reviewed_text_and_fail_closed_on_new_cameos(self):
        data = json.loads((Path(__file__).resolve().parents[1] / 'tools' /
                           'terendelev_reference_contracts.json').read_text(encoding='utf-8'))
        scenes = {s['Id']: s for s in fresh_story()['Scenes']}
        for context in data['contexts']:
            with self.subTest(scene=context['scene'], node=context['node']):
                node_ids = {n['Id'] for n in scenes[context['scene']]['Nodes']}
                self.assertIn(context['node'], node_ids)
        for woman in ('iomedae', 'galfrey', 'irabeth'):
            pattern = re.compile(woman + ('|Inheritor' if woman == 'iomedae' else ''), re.I)
            self.assertEqual([], live_mentions('A memory of ' + woman.capitalize() + '.', pattern))
            self.assertTrue(live_mentions('{n}' + woman.capitalize() + ' stands beside you.{/n}', pattern))

    def test_live_queen_at_pyre_and_knight_cameos_keep_their_guards(self):
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        self.assertIn("crossroute.galfrey.unavailable", scenes["terendelev.trickster.bones.restitution"]["Forbids"])
        self.assertNotIn("crossroute.galfrey.unavailable", scenes["terendelev.trickster.late.the_wound_calls"]["Forbids"])
        for name in ("watch", "late", "debt"):
            page = by_contract(scenes['terendelev.trickster.epilogue.' + name]['Nodes'], [{'Id': 'page'}])
            self.assertIn("crossroute.irabeth.available", by_contract(page['Paragraphs'], [{'Requires': ['terendelev.trickster.watch.irabeth_message', 'irabeth_dead', 'irabeth.trickster.returned', 'crossroute.irabeth.available'], 'Forbids': [], 'AnyGroups': []}])["Requires"])
            self.assertIn("terendelev.payoff.ordinary", by_contract(page['Paragraphs'], [{'Requires': ['terendelev.trickster.night.seen', 'terendelev.committed', 'terendelev.payoff.ordinary', 'terendelev.present_now'], 'Forbids': [], 'AnyGroups': []}])["Requires"])
