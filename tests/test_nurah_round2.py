"""Nurah round-two receipts, refusals and branch continuity."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.fix16b_structure import declared_host, reachable_nodes

from storylines import nurah_continuation as continuation
from storylines import nurah_trickster as route


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NurahRoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s['Id']: s for s in route.SCENES + continuation.SCENES}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]['Nodes'] if n['Id'] == nid)

    def test_accepted_prisoner_cannot_buy_a_competing_late_run(self):
        for suffix in ('', '_late'):
            primer = self.scenes['nurah.trickster.ran_off.second_draft' + suffix]
            self.assertIn(route.ACCEPTED, primer['Forbids'])
        for suffix in ('', '_night'):
            terms = self.scenes['nurah.trickster.ran_off.terms' + suffix]
            self.assertIn(route.ACCEPTED, terms['Requires'])
            self.assertIn(route.PROOFS, terms['Requires'])
            self.assertNotIn(route.ACCEPTED, terms['Forbids'])

    def test_all_four_early_refusals_have_a_matching_preproof_ending(self):
        for sid, nid, index, ending in (
            ('nurah.trickster.prison.night_out', 'start', 3, 'owned_line'),
            ('nurah.trickster.prison.night_out_late', 'start', 3, 'owned_line'),
            ('nurah.trickster.ran_off.terms_by_post', 'letter_one', 3, 'last_word'),
            ('nurah.trickster.ran_off.terms_by_post_late', 'letter', 3, 'last_word'),
        ):
            selected = next(c for c in self.node(sid, nid)['Choices'] if c['Next'] == 'refused')
            page = self.scenes['nurah.trickster.epilogue.' + ending]
            history = {'trickster.ever', *selected['Set']}
            self.assertTrue(set(page['Requires']) <= history)
            self.assertNotIn(route.PROOFS, page['Requires'])
            self.assertTrue(set(route.DEATHS) <= set(page['Forbids']))
            self.assertIsNone(only(self.node(sid, 'refused')['Choices'])['Next'])

    def test_print_payment_is_not_a_zero_delay_circulated_copy(self):
        for sid in ('nurah.trickster.react.irabeth_draft',
                    'nurah.trickster.react.camellia_draft', route.VEILED_DRAFT):
            scene = self.scenes[sid]
            self.assertIn([route.PRINTER_PAID, route.PUBLISHED], scene['RequiresAnyGroups'])
            self.assertGreaterEqual(scene['DelayHours'], 48)
        for suffix in ('', '_late'):
            for nid in ('letter', 'letter_one'):
                for choice in self.node('nurah.trickster.ran_off.terms_by_post' + suffix, nid)['Choices']:
                    self.assertIn(route.PUBLISHED, choice['Set'])
                    self.assertNotIn(route.COMPLETE, choice['Set'])

    def test_disclosure_guards_standalone_and_folded_appetite(self):
        self.assertEqual(continuation.SEEN_CUES[route.DISCLOSED],
                         ['c2d5a4b359e17bc42aca9dc22b9369d3'])
        for sid in ('nurah.trickster.react.camellia_pardon',
                    'nurah.trickster.react.camellia_draft', route.VEILED_DRAFT):
            self.assertIn(route.DISCLOSED, self.scenes[sid]['Requires'])
            self.assertIn(route.DISCLOSED, self.scenes[sid + '_discreet']['Forbids'])
            self.assertIn(sid, only(only(self.scenes[sid + '_discreet']['Nodes'])['Choices'])['Set'])
        packet = self.scenes['nurah.trickster.after.proofs']
        for nid in ('trusted', 'signed'):
            choices = self.node(packet['Id'], nid)['Choices']
            overt = next(c for c in choices if c['Next'] == 'card_draft')
            discreet = next(c for c in choices if c['Next'] == 'card_draft_discreet')
            self.assertIn(route.DISCLOSED, overt['Requires'])
            self.assertIn(route.DISCLOSED, discreet['Forbids'])

    def test_slots_are_reachable_and_legacy_ending_exits_keep_their_effects(self):
        brief_dir = Path(__file__).resolve().parents[1] / 'tools/route_packs/explicit_slots/nurah'
        briefs = list(brief_dir.glob('*.json'))
        scenes = {scene['Id']: scene for scene in fresh_story()['Scenes']}
        self.assertTrue(briefs)
        for brief in briefs:
            data = json.loads(brief.read_text(encoding='utf-8'))
            sid, nid = declared_host(brief.stem, data, scenes)
            with self.subTest(brief=brief.stem, scene=sid, node=nid):
                self.assertIn(nid, reachable_nodes(scenes[sid]))
                slot = next(n for n in scenes[sid]['Nodes'] if n['Id'] == nid)
                if nid == brief.stem:
                    self.assertTrue(only(slot['Choices'])['Next'])
                    self.assertFalse(only(slot['Choices'])['Set'])
        near_exit = only(self.node('nurah.the_letter_she_wrote', 'near')['Choices'])
        self.assertIsNone(near_exit['Next'])
        self.assertEqual(near_exit['Set'], ['nurah.letter_faced'])
        for nid in ('read', 'went'):
            exit = only(self.node('nurah.trickster.epilogue.commit', nid)['Choices'])
            self.assertIsNone(exit['Next'])
            self.assertFalse(exit['Set'])
        quiet = only(self.node('nurah.a_margin_for_you', 'quiet')['Choices'])
        self.assertEqual(quiet['Next'], 'morning')
        self.assertEqual(quiet['Set'], ['nurah.private_quiet'])

    def test_mail_and_unwritten_receipts_do_not_invent_presence_or_reading(self):
        mail = self.scenes['nurah.borrowed_name']
        self.assertEqual((mail['Kind'], mail['Parcel'], mail['Sender']), ('letter', True, 'Nurah'))
        paragraphs = self.node('nurah.trickster.epilogue.unwritten', 'start')['Paragraphs']
        witness = next(p for p in paragraphs if 'irabeth.present_now' in p['Requires'])
        neutral = next(p for p in paragraphs if 'irabeth.present_now' in p['Forbids'])
        self.assertIn('irabeth.present_now', witness['Requires'])
        self.assertIn('irabeth.present_now', neutral['Forbids'])


if __name__ == '__main__':
    unittest.main()
