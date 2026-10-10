"""Reproduce fix16b counterexamples against disposable UTF-8 export copies.

Run: python -m tests.fix16b_mutations /path/to/export.json
Controls with preserved owner conflicts are reported as failures. A mutation
must add a failure beyond that control; a pre-existing failure is not proof.
"""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from tests import story_fixture


CASES = (
    ('tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_frozen_scene_reader_and_shared_producer_contracts', 'scene_gate'),
    ('tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_all_nine_endings_keep_existing_paragraph_indices', 'exit_effect'),
    ('tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_frozen_prefixes_and_exact_appends', 'earned_append'),
    ('tests.test_contract_j01.J01Tests.test_reference_manifest_is_exact_and_never_exempts_new_live_action', 'live_reference'),
    ('tests.test_contract_j01.J01Tests.test_s08_seal_reply_remains_a_channel_and_is_not_emitted_by_j01', 'reply_body'),
    ('tests.test_endings_job4.EndingsJob4Tests.test_repeated_pair_summaries_only_follow_selected_terminal', 'early_summary'),
    ('tests.test_iomedae_round2.IomedaeRound2Tests.test_slots_have_one_first_night_and_history_specific_mornings', 'wrong_morning'),
    ('tests.test_horzalah_polish.HorzalahPolishTests.test_knife_and_missed_chamber_endings_have_no_retroactive_receipts', 'retroactive_chamber'),
    ('tests.test_herrax_round2.HerraxRound2Tests.test_all_four_briefs_have_reachable_default_nodes', 'herrax_edge'),
    ('tests.test_nurah_round2.NurahRoundTwoTests.test_slots_are_reachable_and_legacy_ending_exits_keep_their_effects', 'nurah_edge'),
)


def mutate(story, kind):
    scenes = {s['Id']: s for s in story['Scenes']}
    def node(sid, nid):
        return next(n for n in scenes[sid]['Nodes'] if n['Id'] == nid)
    salt = 'nidalynn.trickster.epilogue.salt'
    if kind == 'scene_gate':
        scenes[salt]['Requires'].remove('trickster.ever')
    elif kind == 'exit_effect':
        node(salt, 'page')['Choices'][0]['Set'] = ['nidalynn.closed']
    elif kind == 'earned_append':
        gate = 'household.pair.nidalynn_areelu.accounted'
        page = node(salt, 'page')
        page['Paragraphs'] = [p for p in page['Paragraphs'] if gate not in p['Requires']]
    elif kind == 'live_reference':
        manifest = json.loads(Path('tools/route_packs/plans/j01-reference-contexts.json').read_text(encoding='utf-8'))
        entry = manifest['contexts'][0]
        target = scenes[entry['scene']] if entry['slot'] in ('Entry', 'ReturnText') else node(entry['scene'], entry['node'])
        field = entry['slot'] if entry['slot'] in ('Entry', 'ReturnText') else 'Text'
        if entry['slot'].startswith('choice'):
            target = target['Choices'][int(entry['slot'][6:])]
        target[field] = entry['woman'] + ' stands here now.'
    elif kind == 'reply_body':
        scenes['household.pair.arueshalae_nocticula.settle.redeemed']['ParticipantContacts']['nocticula']['Kind'] = 'body'
    elif kind == 'early_summary':
        sid = 'minagho_chivarro.trickster.epilogue.commit'
        summary = copy.deepcopy(next(p for p in node(sid, 'went')['Paragraphs']
                                     if p['Requires'] == ['minagho_chivarro.partner_stance.share']))
        node(sid, 'start')['Paragraphs'].append(summary)
    elif kind == 'wrong_morning':
        sid = 'iomedae.trickster.epilogue.platform'
        node(sid, sid + '.explicit.1')['Choices'][0]['Next'] = 'night_quiet'
    elif kind == 'retroactive_chamber':
        sid = 'horzalah.trickster.epilogue.together'
        next(p for p in node(sid, 'page')['Paragraphs'] if p.get('Id') == sid + '.explicit.1')['Forbids'] = []
    elif kind in ('herrax_edge', 'nurah_edge'):
        target = ('herrax.trickster.madam.reachable.explicit.1' if kind == 'herrax_edge'
                  else 'nurah.trickster.prison.terms.explicit.1')
        for scene in scenes.values():
            for page in scene['Nodes']:
                for choice in page['Choices']:
                    if choice.get('Next') == target:
                        choice['Next'] = None
    else:
        raise ValueError(kind)


def run_test(test_id, export):
    with patch.dict(os.environ, RRT_TEST_STORY=str(export)):
        story_fixture._assembled.cache_clear()
        suite = unittest.defaultTestLoader.loadTestsFromName(test_id)
        result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
    story_fixture._assembled.cache_clear()
    return result


def main(source):
    payload = Path(source).read_bytes()
    story = json.loads(payload.decode('utf-8-sig'))
    evidence = {'export_sha256': hashlib.sha256(payload).hexdigest(), 'cases': []}
    with tempfile.TemporaryDirectory(prefix='fix16b-mutations-') as folder:
        control = Path(folder) / 'control.json'
        control.write_text(json.dumps(story, ensure_ascii=False), encoding='utf-8', newline='')
        for test_id, kind in CASES:
            baseline = run_test(test_id, control)
            broken = copy.deepcopy(story)
            mutate(broken, kind)
            export = Path(folder) / (kind + '.json')
            export.write_text(json.dumps(broken, ensure_ascii=False), encoding='utf-8', newline='')
            result = run_test(test_id, export)
            before = len(baseline.failures) + len(baseline.errors)
            after = len(result.failures) + len(result.errors)
            detected = (len(result.failures) > len(baseline.failures)
                        and len(result.errors) == len(baseline.errors))
            row = dict(test=test_id, mutation=kind, control_failures=len(baseline.failures),
                       mutation_failures=len(result.failures), detected=detected,
                       control_errors=len(baseline.errors), mutation_errors=len(result.errors))
            evidence['cases'].append(row)
            print(json.dumps(row), flush=True)
    evidence['all_detected'] = all(row['detected'] for row in evidence['cases'])
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8', newline='')
    return 0 if evidence['all_detected'] else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1]))
