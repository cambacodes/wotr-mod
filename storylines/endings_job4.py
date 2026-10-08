"""Authored endings-plan job 4: delivery order and terminal summaries.

Use the existing scene anchors; serialized scene/node/answer order stays intact.
No acceptance, cost, return, or household state is introduced here.
"""
from copy import deepcopy


def terminal(page):
    return all(answer.get('Next') is None for answer in page['Choices'])


def integrate(story):
    scenes = {event['Id']: event for event in story['Scenes']}
    # The campaign lover's reunion has the same chronology as the late yes:
    # arrival, night, morning, then the winter and lifetime accounts.
    from storylines.eliandra_trickster import EPILOGUE_PARAGRAPHS
    eliandra = scenes['eliandra.trickster.epilogue.together']['Nodes'][0]
    history = len(EPILOGUE_PARAGRAPHS)
    blocks = eliandra.get('Paragraphs', [])
    eliandra['Paragraphs'] = blocks[history:] + blocks[:history]
    from storylines import jerribeth_partner, minagho_chivarro_stance
    summaries = {block['Text'] for block in jerribeth_partner.partner_paragraphs()}
    pair_summaries = {block['Text'] for block in minagho_chivarro_stance.continuity()}
    for event in story['Scenes']:
        if not event['Owner'].endswith('Epilogue'):
            continue
        if event.get('Relationship') == 'jerribeth':
            late = event['Id'] == 'jerribeth.trickster.epilogue.commit'
            for page in event['Nodes']:
                # New local terminal predecessors already own resolved notes.
                selected = page['Id'].startswith('job3_local_') and (
                    terminal(page) or all(answer.get('Next') in ('collected', 'torn', 'torn_mind',
                        'night_after', 'night_mind_after') for answer in page['Choices']))
                if late and terminal(page) and not page['Id'].startswith(('job3_local_', 'late_local_')):
                    # Its compiled predecessor owns the encounter and all its
                    # consequences. This saved exit keeps its ID and mechanics.
                    page['Text'] = '{n}Their answer stood.{/n}'
                for block in page.get('Paragraphs', []):
                    retire_terminal = late and terminal(page) and not page['Id'].startswith(('job3_local_', 'late_local_'))
                    if retire_terminal or block['Text'] in summaries and (not terminal(page) or late) and not selected:
                        block['Forbids'] = list(dict.fromkeys([*block.get('Forbids', []), 'trickster.ever']))
        if event['Id'] == 'minagho_chivarro.trickster.epilogue.commit':
            for page in event['Nodes']:
                if not terminal(page):
                    for block in page.get('Paragraphs', []):
                        if block['Text'] in pair_summaries:
                            block['Forbids'] = list(dict.fromkeys([*block.get('Forbids', []), 'trickster.ever']))

    # A saved Continue still ends immediately. Read-on paths take the same
    # history after their morning, instead of before the encounter.
    for sid, morning in (('nenio.trickster.epilogue.commit', 'morning_after'),
                         ('iomedae.trickster.epilogue.after', 'vigil_morning')):
        event = scenes[sid]
        page = event['Nodes'][0]
        after = next(node for node in event['Nodes'] if node['Id'] == morning)
        blocks = page.get('Paragraphs', [])
        # Nenio's volume/name arrive with her. Iomedae's burial and ninth-year
        # vigil precede this reunion; neither is a later lifetime account.
        after.setdefault('Paragraphs', []).extend(deepcopy(blocks[2:]))
        page['Paragraphs'] = blocks[:2]

    # Native replacements live in their native slots, not the RRT add sequence.
    replacements = {variant['Replacement'] for spec in story.get('NativeEpilogueEdits', {}).values()
                    for variant in (spec, *spec.get('Variants', [])) if variant.get('Replacement')}
    pages = [event for event in story['Scenes'] if event['Owner'].endswith('Epilogue')
             and event['Owner'] != 'AeonEpilogue' and event.get('EpilogueSequence') is None
             and event['Id'] not in replacements]
    from storylines.lastcall_partners import PARTNERS
    codas = {part['key'] + '.lastcall.page' for part in PARTNERS}
    for part in PARTNERS:
        coda = scenes[part['key'] + '.lastcall.page']
        endings = [event for event in pages if (event.get('Relationship') or 'tirabade') == part['rel']
                   and event['Id'] not in codas]
        if endings:
            coda['EpilogueAfter'] = 'scene:' + endings[-1]['Id']
    # Last Word waits for every later-authored ending. Earlier-positioned codas
    # become ready before it; insertion keeps them together after their anchors.
    last = scenes['trickster.lastcall.page.last_word']
    endings = [event for event in pages if event['Id'] not in codas and event is not last]
    last['EpilogueAfter'] = 'scene:' + endings[-1]['Id']
