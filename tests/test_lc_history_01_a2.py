"""Late Last Call append safety and current-quarrel history coverage."""
import copy
import unittest

from storylines.harem_rows.zz_lc_history import register
from tests import test_struct3_d as acceptance

D = 'dorgelinda.trickster.'
L = 'dorgelinda.ledger.'


class LateAppendTests(unittest.TestCase):
    def test_missing_or_non_epilogue_host_is_untouched(self):
        for scenes in ([], [dict(Id='another.page', Owner='Epilogue')],
                       [dict(Id='dorgelinda.lastcall.page', Owner='Dialogue')]):
            with self.subTest(scenes=scenes):
                old = copy.deepcopy(scenes)
                register({'Scenes': scenes}, scenes, {})
                self.assertEqual(old, scenes)

    def test_existing_fields_and_paragraph_positions_are_untouched(self):
        node = dict(Id='page', Text='Existing opener',
                    Paragraphs=[dict(Text=f'Existing {i}', Requires=['old.flag'])
                                for i in range(7)],
                    Choices=[dict(Text='Existing exit', Next=None)])
        host = dict(Id='dorgelinda.lastcall.page', Owner='Epilogue', Nodes=[node])
        old = copy.deepcopy(host)
        scenes = [host]
        register({'Scenes': scenes}, scenes, {})
        self.assertEqual(old['Nodes'][0]['Paragraphs'], node['Paragraphs'][:7])
        self.assertEqual(11, len(node['Paragraphs']))
        del node['Paragraphs'][7:]
        self.assertEqual(old, host)


class ExportHistoryTests(acceptance.Structure3DTests):
    # Include the unchanged shared acceptance suite in this job's selected tests.

    def test_current_quarrel_variant_covers_both_closures_and_repair(self):
        paras = self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
        variants = [p for p in paras if
                    [L + 'cold_unmended', L + 'quarrel_unmended'] in p.get('AnyGroups', ())]
        self.assertEqual(1, len(variants))
        for history, expected in (((), False), ((L + 'quarrel_cold',), True),
                                  ((L + 'quarrel_unmended',), True),
                                  ((L + 'quarrel_cold', L + 'quarrel_mended'), False)):
            with self.subTest(history=history):
                flags = self.flags('dorgelinda.committed',
                                           D + 'cost.audit_hostile', *history)
                self.assertEqual(expected, acceptance.enabled(variants[0], flags))


if __name__ == '__main__':
    unittest.main()
