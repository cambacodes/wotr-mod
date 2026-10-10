"""Replay fix17b counterexamples through unittest against disposable exports.

Usage: RRT_TEST_STORY=/path/to/export.json python -m unittest tests.test_fix17b_mutations
The JSON result and subprocess logs are written to system temp.
"""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ('nidalynn_partner_claim', 'NidalynnPartnerClaimTests', 'test_frozen_scene_reader_and_shared_producer_contracts', 'chaplain_producer'),
    ('nidalynn_partner_claim', 'NidalynnPartnerClaimTests', 'test_all_nine_endings_keep_existing_paragraph_indices', 'departure_presence'),
    ('nidalynn_partner_claim', 'NidalynnPartnerClaimTests', 'test_frozen_prefixes_and_exact_appends', 'chaplain_reader'),
    ('contract_j01', 'J01Tests', 'test_reference_manifest_is_exact_and_never_exempts_new_live_action', 'new_live_action'),
    ('eliandra_round2', 'EliandraRoundTwoTests', 'test_all_five_slot_briefs_match_their_live_defaults', 'eliandra_unreachable'),
    ('eritrice_round4', 'EritriceRoundFourTests', 'test_repeat_night_and_morning_share_position', 'morning_unearned'),
    ('herrax_round2', 'HerraxRound2Tests', 'test_late_return_remembers_completed_punishments', 'punishment_unearned'),
    ('nocticula_round2', 'NocticulaRound2Tests', 'test_acquisition_visit_is_optional_read_only_and_channel_limited', 'visit_writes_commitment'),
    ('nocticula_round2', 'NocticulaRound2Tests', 'test_paid_refusal_and_inn_collect_without_changing_legacy_exits', 'payment_inverted'),
    ('camellia_round2', 'CamelliaRound2Tests', 'test_slots_are_reachable_and_keep_each_branch_successor', 'camellia_wrong_successor'),
]


def mutate(story, kind):
    scenes = {s['Id']: s for s in story['Scenes']}

    def node(sid, nid):
        return next(n for n in scenes[sid]['Nodes'] if n['Id'] == nid)

    if kind == 'chaplain_producer':
        node('nidalynn.trickster.kiln.the_chaplain', 'leave')['Choices'][0]['Set'] = []
    elif kind == 'departure_presence':
        scenes['nidalynn.trickster.epilogue.apart']['Requires'].append('nidalynn.present_now')
    elif kind == 'chaplain_reader':
        page = node('nidalynn.trickster.epilogue.salt', 'page')
        block = next(p for p in page['Paragraphs'] if p['AnyGroups'] == [[
            'nidalynn.trickster.chaplain_prayed', 'nidalynn.trickster.chaplain_sent_away']])
        block['AnyGroups'] = [['nidalynn.trickster.chaplain_prayed']]
    elif kind == 'new_live_action':
        node('herrax.trickster.madam.reachable', 'cut')['Text'] += ' Chivarro stands here now.'
    elif kind == 'eliandra_unreachable':
        for c in node('eliandra.trickster.visit.star_heart', 'charts')['Choices']:
            c['Next'] = 'morning'
    elif kind == 'morning_unearned':
        scenes['eritrice.council.second_morning']['Requires'].remove('eritrice.council.twice_nightly_carried')
    elif kind == 'punishment_unearned':
        page = scenes['herrax.trickster.epilogue.after_hours.invitation']['Nodes'][0]
        block = next(p for p in page['Paragraphs'] if p['Requires'] == ['herrax.trickster.bait_taken'])
        block['Requires'] = []
    elif kind == 'visit_writes_commitment':
        node('noct.acq.epilogue.correspondence', 'arrival')['Choices'][0]['Set'] = ['noct.complete']
    elif kind == 'payment_inverted':
        for p in node('nocticula.trickster.epilogue.commit', 'inn')['Paragraphs']:
            if p['Requires'] == ['nocticula.trickster.cost.shade_paid']:
                p['Requires'] = ['nocticula.trickster.refused_page']
    elif kind == 'camellia_wrong_successor':
        sid = 'camellia.trickster.cards.the_deck_again'
        node(sid, sid + '.explicit.1')['Choices'][0]['Next'] = 'wont_close'
    else:
        raise ValueError(kind)


def main():
    source = Path(os.environ["RRT_TEST_STORY"]).resolve()
    story = json.loads(source.read_text(encoding='utf-8-sig'))
    output = Path(tempfile.mkdtemp(prefix='fix17b-mutations-'))
    results = []
    for module, cls, function, mutation in CASES:
        target = f'tests.test_{module}.{cls}.{function}'
        argv = [sys.executable, '-m', 'unittest', target]
        result = {'test': target, 'mutation': mutation, 'argv': argv}
        for variant in ('control', 'mutant'):
            fixture = source
            if variant == 'mutant':
                payload = copy.deepcopy(story)
                mutate(payload, mutation)
                fixture = output / (mutation + '.json')
                fixture.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
            env = dict(os.environ, RRT_TEST_STORY=str(fixture), PYTHONHASHSEED='0')
            run = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                 text=True, encoding='utf-8', timeout=120)
            log = output / (mutation + '.' + variant + '.log')
            log.write_text(run.stdout + run.stderr, encoding='utf-8')
            result[variant] = {'exit': run.returncode, 'fixture': str(fixture), 'log': str(log),
                               'assertion_failure': 'FAIL:' in run.stderr and 'ERROR:' not in run.stderr}
        results.append(result)
        print(target, result['control']['exit'], result['mutant']['exit'], flush=True)
    receipt = output / 'evidence.json'
    receipt.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(receipt, flush=True)
    return 0 if all(r['control']['exit'] == 0 and r['mutant']['exit'] == 1 and r['mutant']['assertion_failure'] for r in results) else 1


class Fix17bMutationTests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get('RRT_TEST_STORY'), 'requires runner supplied export')
    def test_controls_pass_and_behavior_mutations_fail(self):
        self.assertEqual(0, main())


if __name__ == '__main__':
    unittest.main()
