"""Late Last Call append safety and current-quarrel history coverage."""
import copy
import unittest
from tests.structure import without_prose
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
        node = dict(Id='page', Text='', Paragraphs=[dict(Id='old.memory', Text='', Requires=['old.flag'])], Choices=[dict(Id='old.exit', Text='', Next=None)])
        host = dict(Id='dorgelinda.lastcall.page', Owner='Epilogue', Nodes=[node])
        scenes = [host]
        register({'Scenes': scenes}, scenes, {})
        self.assertEqual([n['Id'] for n in host['Nodes']], ['page'])
        self.assertEqual([c['Id'] for c in node['Choices']], ['old.exit'])
        self.assertEqual([c['Next'] for c in node['Choices']], [None])
        memory = next(p for p in node['Paragraphs'] if p.get('Id') == 'old.memory')
        self.assertEqual(memory['Requires'], ['old.flag'])
        requirements = {flag for p in node['Paragraphs'] for flag in p.get('Requires', [])}
        self.assertIn(D + 'cost.told_all', requirements)
        self.assertTrue(any([L + 'cold_unmended', L + 'quarrel_unmended'] in p.get('AnyGroups', []) for p in node['Paragraphs']))

class ExportHistoryTests(acceptance.Structure3DTests):

    def test_current_quarrel_variant_covers_both_closures_and_repair(self):
        paras = self.node('dorgelinda.lastcall.page', 'page')['Paragraphs']
        variants = [p for p in paras if [L + 'cold_unmended', L + 'quarrel_unmended'] in p.get('AnyGroups', ())]
        quarrel_account, = variants
        self.assertIn([L + 'cold_unmended', L + 'quarrel_unmended'], quarrel_account['AnyGroups'])
        for history, expected in (((), False), ((L + 'quarrel_cold',), True), ((L + 'quarrel_unmended',), True), ((L + 'quarrel_cold', L + 'quarrel_mended'), False)):
            with self.subTest(history=history):
                flags = self.flags('dorgelinda.committed', D + 'cost.audit_hostile', *history)
                self.assertEqual(expected, acceptance.enabled(quarrel_account, flags))
if __name__ == '__main__':
    unittest.main()
