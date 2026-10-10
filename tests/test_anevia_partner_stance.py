"""Round 2a state/graph contracts; prose is reviewed independently."""
import copy
import json
from pathlib import Path
import unittest
from storylines import anevia_independent, anevia_trickster
from storylines import anevia_partner_stance as stance

def holds(answer, flags):
    return set(answer.get('Requires', ())) <= flags and (not set(answer.get('Forbids', ())) & flags)

def walk(book, initial):
    nodes = {node['Id']: node for node in book['Nodes']}
    pending = [(book['Nodes'][0]['Id'], set(initial))]
    endings = []
    while pending:
        node_id, flags = pending.pop()
        answers = [answer for answer in nodes[node_id]['Choices'] if holds(answer, flags)]
        if not answers:
            raise AssertionError('Page has no selectable answers: ' + node_id)
        for answer in answers:
            state = flags | set(answer.get('Set', ()))
            if answer.get('Next'):
                pending.append((answer['Next'], state))
            elif not answer.get('Abort'):
                endings.append(state)
    return endings

class AneviaStanceTests(unittest.TestCase):

    def test_ordinary_stances_and_append_only_layout(self):
        old = next((book for book in anevia_independent.SCENES if book['Id'] == 'anevia.a_key_that_is_hers'))
        new = copy.deepcopy(old)
        stance.ordinary_commit(new)
        self.assertEqual([node['Id'] for node in [new_node for old_node, new_node in zip(old['Nodes'], new['Nodes'])]], [node['Id'] for node in old['Nodes']])
        for before, after in zip(old['Nodes'], new['Nodes']):
            self.assertEqual([a.get('Next') for a in [new_answer for old_answer, new_answer in zip(before['Choices'], after['Choices'])]], [a.get('Next') for a in before['Choices']])
        outcomes = walk(new, set())
        for flag in (stance.SHARE, stance.SECRET):
            self.assertTrue(any((flag in state and 'anevia.committed' in state for state in outcomes)))
        exclusive = [state for state in outcomes if stance.EXCLUSIVE in state]
        self.assertTrue(exclusive)
        self.assertTrue(all(('anevia.closed' in state and 'anevia.committed' not in state for state in exclusive)))
        self.assertTrue(all((len({stance.SHARE, stance.EXCLUSIVE, stance.SECRET} & state) <= 1 for state in outcomes)))

    def test_secret_uses_existing_farewell_and_closes_only_anevia(self):
        book = copy.deepcopy(next((book for book in anevia_independent.SCENES if book['Id'] == 'anevia.the_last_ordinary_thing')))
        stance.farewell_discovery(book)
        initial = {stance.SECRET, 'anevia.committed', 'irabeth.lover', 'seelah.committed'}
        outcomes = walk(book, initial)
        self.assertTrue(outcomes)
        for state in outcomes:
            self.assertTrue({stance.EXPOSED, 'anevia.closed', 'anevia.parted'} <= state)
            self.assertFalse({'closed', 'irabeth.closed', 'irabeth_dead', 'irabeth_gone'} & state)
            self.assertTrue(initial <= state)

    def test_gate_stances_respect_death_departure_survival_and_original_price(self):
        for scene_id in ('commit', 'second_ask', 'fetched_commit', 'fetched_second_ask'):
            book = copy.deepcopy(next((book for book in anevia_trickster.SCENES if book['Id'] == 'anevia.trickster.gone.' + scene_id)))
            old = copy.deepcopy(book)
            stance.gate_commit(book)
            for before, after in zip(old['Nodes'], book['Nodes']):
                self.assertEqual([a.get('Next') for a in [new_answer for old_answer, new_answer in zip(before['Choices'], after['Choices'])]], [a.get('Next') for a in before['Choices']])
            for partner_flags in ({'irabeth_dead'}, {'irabeth_gone'}, {'irabeth_dead', stance.RETURN}, {'irabeth_dead', stance.DUG}, {'irabeth_dead', stance.RAISED}):
                with self.subTest(scene=scene_id, partner=partner_flags):
                    outcomes = walk(book, partner_flags)
                    committed = [state for state in outcomes if 'anevia.committed' in state]
                    self.assertTrue(committed)
                    if partner_flags == {'irabeth_dead'}:
                        self.assertTrue(all((not {stance.SHARE, stance.SECRET, stance.EXCLUSIVE} & state for state in outcomes)))
                    else:
                        for page in book['Nodes']:
                            for suffix in ('_exclusive', '_secret_offer'):
                                offers = [choice for choice in page['Choices'] if (choice.get('Next') or '').endswith(suffix)]
                                if offers:
                                    offer, = [a for a in offers if holds(a, partner_flags)]
                                    self.assertTrue(offer.get('Next').endswith(suffix))
                        self.assertTrue(any((stance.SHARE in state for state in committed)))
                        self.assertTrue(any((stance.SECRET in state and stance.EXPOSED in state and ('anevia.closed' in state) for state in committed)))
                    if 'second_ask' in scene_id:
                        self.assertTrue(all((anevia_trickster.KEY in state for state in committed)))

    def test_partner_state_paragraphs_are_exclusive_and_complete(self):
        state_paragraphs = stance.partner_states()
        for flags in (set(), {'irabeth_away'}, {'irabeth_gone'}, {'irabeth_dead'}, {'irabeth_dead', 'irabeth_gone'}, {stance.RETURN, 'irabeth_dead', 'irabeth_gone'}, {stance.DUG, 'irabeth_dead'}, {stance.RAISED, 'irabeth_dead'}, {stance.RETURN, stance.DUG, stance.RAISED, 'irabeth_dead'}, {stance.DUG, 'irabeth_dead', 'irabeth_gone'}, {stance.RETURN, 'irabeth_dead', 'irabeth_away'}):
            selected, = [p for p in state_paragraphs if holds(p, flags)]
            self.assertTrue(holds(selected, flags))

    def test_native_variants_keep_indices_and_plain_text_contract(self):
        original = copy.deepcopy(next((book for book in anevia_trickster.SCENES if book['Id'] == 'anevia.trickster.epilogue.native_tirabade_left_committed')))
        edit = dict(Replacement=original['Id'], When=[['trickster.ever', 'anevia.trickster.returned', 'anevia.committed']], Variants=[], KeepNativeImage=True)
        payload = dict(Scenes=[original], NativeEpilogueEdits={'native': edit})
        stance.native_stance_variants(payload)
        self.assertEqual(edit['Replacement'], original['Id'])
        self.assertEqual(payload['Scenes'][-1]['Id'], original['Id'])
        retained, = [b for b in payload['Scenes'] if b['Id'] == original['Id']]
        self.assertEqual(retained['Id'], original['Id'])
        books = {book['Id']: book for book in payload['Scenes']}
        for variant in edit['Variants']:
            book = books[variant['Replacement']]
            dispatch_1, = book['Nodes']
            self.assertFalse(book['Nodes'][0].get('Paragraphs'))
            self.assertTrue(all(('trickster.ever' in group for group in variant['When'])))
        for partner in (set(), {'irabeth_dead'}, {'irabeth_gone'}, {'irabeth_away'}, {'irabeth_dead', stance.RETURN}, {'irabeth_dead', stance.DUG}, {'irabeth_dead', stance.RAISED}):
            flags = partner | {stance.SHARE, 'trickster.ever', 'anevia.trickster.returned', 'anevia.committed'}
            matches = [variant for variant in edit['Variants'] if any((all((flag[1:] not in flags if flag.startswith('!') else flag in flags for flag in group)) for group in variant['When']))]
            dispatch_2, = matches

    def test_final_export_keeps_current_state_and_stance_readers(self):
        from tests.story_fixture import fresh_story
        story = fresh_story()
        books = {book['Id']: book for book in story['Scenes']}
        order = [book['Id'] for book in story['Scenes']]
        self.assertLess(order.index('anevia.trickster.epilogue.native_tirabade_left'), order.index('anevia.lastcall.page'))
        self.assertLess(order.index('anevia.lastcall.page'), order.index('anevia.trickster.gone.react_konomi'))
        for suffix, node_id, index in (('commit', 'answer', 3), ('second_ask', 'price', 2), ('fetched_commit', 'answer', 3), ('fetched_second_ask', 'price', 2)):
            node = next((n for n in books['anevia.trickster.gone.' + suffix]['Nodes'] if n['Id'] == node_id))
            for ordinal, choice in enumerate(node['Choices']):
                if ordinal == index:
                    self.assertTrue(choice['Abort'])
                    self.assertIsNone(choice.get('Next'))
                    self.assertEqual(choice.get('Forbids'), ['trickster.now'])
                    break
            else:
                self.fail('Saved abort choice is absent')
        for scene_id in ('anevia.lastcall.page', 'anevia.ending_kept', 'anevia.ending_death', 'anevia.ending_gone', 'anevia.ending_parted', 'anevia.ending_sacrifice'):
            paragraphs = books[scene_id]['Nodes'][0].get('Paragraphs', [])
            for expected in stance.ending_paragraphs():
                self.assertTrue(any((paragraph.get('Requires', [])[:len(expected['Requires'])] == expected['Requires'] and paragraph.get('Forbids', []) == expected['Forbids'] for paragraph in paragraphs)), scene_id)
        native_ids = {variant['Replacement'] for edit in story['NativeEpilogueEdits'].values() for variant in (edit, *edit.get('Variants', []))}
        variants = [books[identity] for identity in native_ids if identity.startswith('anevia.') and '.partner_' in identity]
        self.assertTrue(variants)
        for book in variants:
            page, = book['Nodes']
            self.assertEqual(page['Id'], 'page')
if __name__ == '__main__':
    unittest.main()
