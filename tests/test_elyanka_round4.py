"""Round-4 histories: inquiry evidence and official visits are independent."""
import itertools
import unittest

from tests.story_fixture import fresh_story


class ElyankaRound4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s['Id']: s for s in fresh_story()['Scenes']}

    @staticmethod
    def enabled(item, flags):
        return (set(item.get('Requires', ())) <= flags
                and not set(item.get('Forbids', ())) & flags
                and all(set(group) & flags for group in item.get('AnyGroups', ())))

    def rendered_page(self, ending, flags):
        node = self.scenes['elyanka.trickster.epilogue.' + ending]['Nodes'][0]
        return node['Text'] + '\n' + '\n'.join(
            p['Text'] for p in node.get('Paragraphs', ()) if self.enabled(p, flags))

    def test_chalk_requires_inquiry_in_every_shared_ending(self):
        for ending, prayed, inquiry in itertools.product(
                ('claim', 'debt', 'lock', 'left_free'), (False, True),
                (None, 'told_seelah', 'misled', 'hers')):
            flags = {'elyanka.trickster.gave_dead'}
            if prayed:
                flags.add('elyanka.trickster.seelah_prayed')
            if inquiry:
                flags.add('elyanka.trickster.inquiry.' + inquiry)
            text = self.rendered_page(ending, flags)
            with self.subTest(ending=ending, prayed=prayed, inquiry=inquiry):
                self.assertEqual(bool(inquiry), 'chalk marks' in text)
                self.assertEqual(prayed, 'counting them, row by row, before the carts went' in text)

    def test_no_authority_assertion_excludes_all_writ_and_inquiry_outcomes(self):
        for writ, inquiry in itertools.product(
                (None, 'upheld', 'lied', 'hers'), (None, 'told_seelah', 'misled', 'hers')):
            flags = {'trickster.secret.elyanka_rites', 'elyanka.trickster.gave_dead'}
            if writ:
                flags.add('elyanka.trickster.writ.' + writ)
            if inquiry:
                flags.add('elyanka.trickster.inquiry.' + inquiry)
            text = self.rendered_page('claim', flags)
            with self.subTest(writ=writ, inquiry=inquiry):
                self.assertEqual(not (writ or inquiry), 'nobody in authority ever came' in text)
                if writ:
                    self.assertIn('chaplains who came with a writ', text)


if __name__ == '__main__':
    unittest.main()
