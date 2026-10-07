"""Authored audit repairs: judgment, accepted proposals and played histories.

No native dragon customs or powers are added. Native anchors remain the lair
tariff, Xanthir's captive clutch and the existing death/egg observations.
All legacy records and answer positions survive; variants append.
"""
from copy import deepcopy

from story_format import c, n, p, scene
from storylines.devarra_round2 import _add, _nodes, _scene, _voice

P = 'devarra.trickster.'
T = 'devarra.tower.'
CLAIMED = P + 'ending_claimed'
REFUSED = P + 'judgment_refused'
ANSWERED = P + 'judgment_answered'
LATE_YES = P + 'late_accepted'
VOLUNTARY = T + 'battle_offered'
PURCHASED = T + 'battle_price_accepted'


def judgment_guard(record):
    _add(record, 'Forbids', CLAIMED, REFUSED)
    record.setdefault('ForbidOverrides', {}).update({CLAIMED: ANSWERED, REFUSED: ANSWERED})


def spine(scenes):
    lair = _scene(scenes, P + 'after.lair')
    nodes = _nodes(lair)
    for sid, nid in ((P + 'after.tithe', 'ending_free'),
                     (P + 'after.lair', 'second_question_free')):
        target = _nodes(_scene(scenes, sid))[nid]
        target['Choices'].append(c(
            '[Give her the conqueror\'s ending] "The thief takes the leash from the stone. Now the dragon fights where the thief points."',
            'verdict' if sid == lair['Id'] else None, flags=(P + 'tested', CLAIMED)))
    for answer in nodes['verdict']['Choices']:
        _add(answer, 'Forbids', CLAIMED)
    nodes['verdict']['Choices'].append(c('Continue', 'claimed', requires=(CLAIMED,)))
    lair['Nodes'].append(_voice('claimed',
        '"Another hand on the leash." {n}Her claw drives through the parapet beside you.{/n} '
        '"Vang had my eggs. What have you? A story? Take it down the mountain before I feed it to you."',
        c('[Go down the mountain.]', flags=(REFUSED,))))

    # Correction costs her existing 48-hour wait and an account delivered in person.
    # No new resource price, attraction test or reconciliation requirement.
    for remote in (False, True):
        copied = deepcopy([nodes[key] for key in ('terms', 'bitten', 'no', 'left', 'bitten_free')])
        copied[1]['Text'] = ('"Not the sword arm." {n}She studies the arm, then your face.{/n} '
                            '"Keep it. I will send for you when I want it. Come yourself."')
        copied[-1]['Text'] = copied[1]['Text']
        correction = scene(P + 'after.corrected_ending' + ('_remote' if remote else ''),
            'The ending she rejected', 'Devarra', 3,
            '' if remote else '"I will take her a different ending. Myself."', [
                n('climb', 'Narrator', '{n}You climb to the tower. The broken parapet still lies across the path. '
                  'Devarra watches you step over it.{/n}', c('Continue', 'answer')),
                _voice('answer', '"Well? Whose hand holds the leash now?"',
                    c('"Nobody\'s. The dragon comes because she wants to. The thief has to ask."',
                      'terms', flags=(ANSWERED,)),
                    c('"Keep your mountain. I am finished asking."', 'no',
                      flags=('devarra.closed', P + 'refused'))),
                *copied], requires=('trickster.ever', P + 'returned', REFUSED),
            forbids=('devarra.closed', ANSWERED, *(() if remote else ('storyteller.dead',))),
            delay=48, last=5, Relationship='devarra', Chapters=[3, 5],
            **({'Remote': True, 'RequiresAnyGroups': [['storyteller.dead']]} if remote else
               {'AnswerLists': ['2f5b7e0b76d3c5a42a431e1e33a8db09'],
                'NativeReturnCue': '34a0d078b4ac51547a8f5e0e1c8e1e2c'}))
        _add(correction, 'Requires', 'devarra.present_now')
        scenes.append(correction)

    # A late yes is played, never derived from a submitted story or fate page.
    proposal = scene(P + 'after.late_proposal', 'The answer she came for', 'Devarra', 5, '', [
        n('arrival', 'Narrator', '{n}A grey shadow crosses Drezen\'s north wall. Devarra lands on the road '
          'outside the gate, blocking the supply carts. You go out to meet her. The sentries stop following '
          'when she lowers her head and shows her teeth.{/n}',
          c('Continue', 'offer')),
        _voice('offer', '"The old man brought me your ending. I have come for your answer myself. '
               'My tower. You, alone. Once a year, one small bite, from the arm without the sword. '
               'The eggs remain my business. Well, crusader?"',
            c('[Bare your forearm] "Once a year. Not the sword arm."', 'accepted',
              flags=('devarra.committed', P + 'cost.bitten', LATE_YES)),
            c('"No. Your feeding arrangement is all we have."', 'refused',
              flags=('devarra.closed', P + 'refused')),
            c('"I have no answer yet."', 'waiting', flags=(P + 'left_hungry',))),
        _voice('accepted', '{n}She turns her head, keeping your bare arm within reach.{/n} '
               '"Spring. My ridge. I will have the rest of your story there. And you."', c('[Return to the war council.]')),
        _voice('refused', '"Then keep that arm. Keep the rest of you well away from my teeth." '
               '{n}She lifts her head and spreads her wings.{/n}', c('[Watch her leave.]')),
        _voice('waiting', '"Still unfinished." {n}Her claw gouges the road beside your boot.{/n} '
               '"I will keep this part. Bring me the next yourself."', c('[Return to the preparations.]')),
    ], requires=('trickster.ever', P + 'returned', P + 'tested'),
       forbids=('devarra.committed', 'devarra.closed', P + 'declined', P + 'left_hungry'),
       last=5, Chapters=[5], Remote=True, Relationship='devarra')
    judgment_guard(proposal)
    _add(proposal, 'Requires', 'devarra.present_now')
    scenes.append(proposal)

    commit = _scene(scenes, P + 'epilogue.commit')
    _add(commit, 'Requires', P + 'returned', LATE_YES, 'devarra.committed')
    commit['Forbids'].remove('devarra.committed')
    judgment_guard(commit)
    commit['Nodes'][0]['Text'] = (
        '{n}In spring Devarra returned to the north ridge. The Commander climbed to her fire '
        'and bared the arm promised before the march to Threshold. She took her first small bite '
        'and watched the Commander bind it.{/n} "You kept me waiting long enough. Stay." '
        '{n}The Commander stayed until dawn. At the next spring\'s appointment she was already on the ridge.{/n}')
    _add(_scene(scenes, P + 'epilogue.woken'), 'Forbids', LATE_YES)

    pending = scene(P + 'epilogue.pending', '', 'DevarraEpilogue', 6, '', [
        n('page', 'Narrator', '{n}Devarra kept the north ridge and the food sent up from Drezen. '
          'The Commander\'s story remained unfinished. When the carts stopped, she hunted the old Wound '
          'and came back with demon flesh between her teeth. No annual appointment had been made.{/n}')],
        requires=('trickster.ever', P + 'returned', P + 'tested'),
        forbids=('devarra.committed', 'devarra.closed', P + 'left_hungry'), last=6, Relationship='devarra')
    judgment_guard(pending)
    _add(pending, 'Requires', 'devarra.present_now')
    scenes.append(pending)
    scenes.append(scene(P + 'epilogue.claimed', '', 'DevarraEpilogue', 6, '', [
        n('page', 'Narrator', '{n}The ending sent to Devarra remained unanswered. She hunted beyond the north ridge, '
          'far from the crusade\'s banners. No general pointed her toward a battle. No Commander climbed '
          'to collect a dragon promised by a story.{/n}')],
        requires=('trickster.ever', P + 'returned', CLAIMED, 'devarra.present_now'),
        forbids=(ANSWERED, 'devarra.closed'), last=6, Relationship='devarra'))

    refused = _scene(scenes, P + 'epilogue.refused')['Nodes'][0]
    refused['Text'] = ('{n}A grey woundwyrm hunted the old Wound for years. She passed over Drezen once, '
                       'high above the north wall. She did not land.{/n}')
    refused.setdefault('Paragraphs', []).extend([
        p('{n}The tower stair kept the marks of the Commander\'s visits, with no new line beside them.{/n}',
          requires=(T + 'climbed',)),
        p('{n}The teamsters stopped taking food to her ridge after the first cart returned '
          'scorched and empty.{/n}', forbids=(T + 'climbed',)),
    ])
    # Canon closures need no invented rescue; native observations select the account.
    scenes.append(scene(P + 'epilogue.canon_fate', '', 'DevarraEpilogue', 6, '', [
        n('page', 'Narrator', '{n}The dragon who had attacked the crusade did not live to see its end.{/n}',
          paragraphs=(
            p('{n}Her hunters left her dead in her lair. No wings carried her to the Ivory Sanctum.{/n}',
              requires=('devarra.dead_lair',)),
            p('{n}She died in the Ivory Sanctum, outside the chamber where Xanthir\'s stone servants '
              'held her eggs. Their orders could not make her rise.{/n}',
              requires=('devarra.dead_sanctum',), forbids=('devarra.dead_lair',)),
            p('{n}Her clutch went into the citadel kitchens. The soldiers ate well that day.{/n}', requires=('eggs.omelet',)),
            p('{n}Druids carried her clutch away. Its young would never know the mother who had fought for it.{/n}',
              requires=('eggs.druids',), forbids=('eggs.omelet',)),
            p('{n}Broken shells lay beneath the stone fists. Nothing hatched from them.{/n}',
              requires=('eggs.destroyed',), forbids=('eggs.omelet', 'eggs.druids')),
            p('{n}The eggs were carried into Drezen\'s vaults, beyond her reach.{/n}',
              requires=('eggs.project',), forbids=('eggs.omelet', 'eggs.druids', 'eggs.destroyed')),
            p('{n}The Storyteller remembered the dragon who had held him prisoner. He offered no lament.{/n}',
              forbids=('storyteller.dead',)),
          ))], requires=('trickster.ever',), RequiresAnyGroups=[['devarra.dead_lair', 'devarra.dead_sanctum']],
        forbids=(P + 'returned',), last=6, Relationship='devarra'))


def tower(scenes):
    for record in scenes:
        judgment_guard(record)
    book = _scene(scenes, T + 'the_garrison_book')
    nodes = _nodes(book)
    # A public landing remains a meaningful wager after either private city visit.
    old = nodes['start']['Choices'][1]
    _add(old, 'Forbids', T + 'vault_opened', P + 'cook_given')
    old_tell = nodes['tell']['Text']
    nodes['tell']['Text'] = old_tell.replace('The book on her coming down into the city', 'The book on her landing before the north watch')
    for suffix, required, blocked, recollection in (
        ('vault', T + 'vault_opened', (), 'She came into your vault under guard. The north watch saw no landing.'),
        ('cook', P + 'cook_given', (T + 'vault_opened',), 'She came for the cook. Nobody is betting on another visit to the kitchens.'),
    ):
        nodes['start']['Choices'].append(c('"What are the odds on her?"', 'on_her_' + suffix,
                                           requires=(required,), forbids=blocked))
        book['Nodes'].append(n('on_her_' + suffix, 'conversant',
            '"' + recollection + ' Now the wager is whether she will land on the citadel roof '
            'in full view of the garrison. A hundred to one. No takers."', c('Continue', 'tell_her')))
    # Preserve the old offer flag/mechanics; classify which terms were accepted.
    generals = _nodes(_scene(scenes, T + 'the_generals'))
    _add(generals['ask']['Choices'][0], 'Set', VOLUNTARY)
    _add(generals['bargain']['Choices'][0], 'Set', PURCHASED)


def epilogue(page):
    for paragraph in page.get('Paragraphs', []):
        if T + 'one_battle_sold' in paragraph.get('Requires', []):
            _add(paragraph, 'Requires', PURCHASED)
    page.setdefault('Paragraphs', []).append(p(
        '{n}Devarra chose her battlefield and broke a demon host before dawn. The generals learned '
        'of it from the survivors. She returned to her ridge before anyone could thank her; '
        'she had asked for neither a dispatch nor a story in payment.{/n}', requires=(VOLUNTARY,), forbids=(PURCHASED,)))


def integrate(payload):
    # All consumers (household, ordinary payoff and Last Call) now read a played yes.
    payload['Derived']['devarra.outcome.late_accepted'] = [[LATE_YES, 'devarra.committed']]
    payload['Derived'][P + 'late_committed'] = [[
        'trickster.ever', P + 'tested', 'devarra.outcome.deferred_judgment',
        'devarra.outcome.late_accepted']]
    payload.setdefault('DerivedForbids', {}).pop(P + 'late_committed', None)
    # Shared file is read-only; only this route's named Last Call entry is adjusted
    # before its factory assembles the pages later in expansion.make_expansion.
    from storylines import lastcall_partners
    partner = lastcall_partners._history_partners['devarra']
    partner['page_forbids'] = tuple(dict.fromkeys((*partner['page_forbids'], CLAIMED, REFUSED)))
    partner['page_forbid_overrides'].update({CLAIMED: ANSWERED, REFUSED: ANSWERED})


def accepted_ending(event):
    """Retire the merged effect-free proposal after a campaign yes; keep its IDs."""
    page = event['Nodes'][0]
    page['Text'] = ('{n}In spring Devarra returned to the north ridge. The Commander climbed to her fire '
        'and bared the arm promised before the march to Threshold. She took her first small bite '
        'and watched the Commander bind it.{/n} "You kept me waiting long enough. Stay."')
    for answer in page['Choices'][1:3]:
        _add(answer, 'Forbids', LATE_YES)
    page['Choices'].append(c('Continue', 'late_accepted', requires=(LATE_YES,)))
    accepted = _nodes(event)['late_accepted']
    accepted['Text'] = ('{n}The Commander stayed until dawn. The stair bore a fresh scratch when '
                        'Devarra returned the following spring; the appointment had been kept.{/n}')
    for paragraph in accepted.get('Paragraphs', []):
        paragraph['Text'] = ('{n}Before the march, Devarra had come for the answer herself. '
                             'The Commander had accepted then. Threshold changed neither her tariff '
                             'nor the appointment on her ridge.{/n}')
