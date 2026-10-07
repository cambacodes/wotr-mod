"""Soana audit r2 repairs, applied to her entries after the shared ending pass.

Authored: relay follow-up, Corven's proposal response and the concealed stream
meeting. These expand existing situations; no new price, return or love gate.
Native marriage/children: Cue_0012 c6789b662ea5c404f957d9a20b68f5c7.
"""
from copy import deepcopy
import re
from story_format import c, n, p
from storylines import soana_partner as P

HOME = 'soana.partner.homecoming_kept'
FAMILY = 'soana.round2.family_reply'
FRIEND = 'soana.trickster.friends'
DISCLOSED = 'soana.round3.disclosed'
ARRANGEMENT = 'soana.round3.arrangement'
KNOWN = 'soana.round3.family_known'
PROPOSAL_SENT = 'soana.round4.proposal_sent'
PROPOSAL_READ = 'soana.round4.proposal_read'


def page(event, key):
    return next(x for x in event['Nodes'] if x['Id'] == key)


def add(block, field, *flags):
    block[field] = list(dict.fromkeys([*block.get(field, []), *flags]))


def predicates(payload):
    # Authored follow-up: the second letter travels by the same seven-day
    # southern relay as the wedding inquiry, in both living/returned hosts.
    from storylines.soana_round2 import correspondence_scene
    for returned in (False, True):
        followup = correspondence_scene(returned)
        followup['Id'] = 'soana.partner.proposal_reply' + ('.returned' if returned else '')
        followup['Title'] = 'The second fold'
        followup['Requires'] = [f for f in followup['Requires'] if f != P.PURSUED]
        add(followup, 'Requires', PROPOSAL_SENT, 'soana.present_now')
        followup['Forbids'] = [f for f in followup['Forbids'] if f != FAMILY]
        add(followup, 'Forbids', PROPOSAL_READ)
        followup['Nodes'] = [deepcopy(page(followup, k)) for k in ('start', 'share', 'accepted', 'friend')]
        start = page(followup, 'start')
        start['Text'] = '''{n}The scout brings a second fold from the southern relay, its edges stained by rain. He leaves to join the demon-road patrol while Soana opens it beside the cold pot.{/n}
"This time he has heard about you, hunter. Sit. I shall read his answer."'''
        start['Choices'] = [c('[Hear Corven answer the proposal she sent.]', 'share')]
        accepted = page(followup, 'accepted')
        accepted['Text'] = accepted['Text'].replace(
            'Her thumb rubs a callus on your palm. She does not let go until the scout has left.',
            'She catches your wrist and pulls you back from the path as the scout leaves.')
        for key in ('accepted', 'friend'):
            for answer in page(followup, key)['Choices']:
                add(answer, 'Set', PROPOSAL_READ)
        payload['Scenes'].append(followup)
    payload['Derived'][KNOWN] = [[P.CONFIRMED], [FAMILY], [HOME]]
    # The old together receipt also covered ordinary family reunion. His
    # romance terms require a shared stance and no chosen family friendship.
    payload['Derived'][ARRANGEMENT] = [[P.TOGETHER, P.SHARE]]
    payload.setdefault('DerivedForbids', {})[ARRANGEMENT] = [FRIEND, P.BROKEN]
    payload['Derived']['soana.round3.no_stance'] = [['availability.observed']]
    payload['DerivedForbids']['soana.round3.no_stance'] = [P.SHARE, P.SECRET, P.EXCLUSIVE]


def variant(event, key, replacement, requires=(), forbids=(), suffix='known'):
    """Retain old targets/indices; append history-selected continuations."""
    old = page(event, key)
    new = deepcopy(old)
    new['Id'] = key + '_r3_' + suffix
    new['Text'] = replacement
    for source in list(event['Nodes']):
        for answer in list(source['Choices']):
            if answer.get('Next') != key:
                continue
            copy = deepcopy(answer)
            copy.pop('Id', None)
            copy['Next'] = new['Id']
            add(copy, 'Requires', *requires)
            add(copy, 'Forbids', *forbids)
            # The negative complement is a single existing/derived receipt.
            add(answer, 'Forbids', *requires)
            source['Choices'].append(copy)
    event['Nodes'].append(new)
    return new


def family(scenes):
    for returned in ('', '.returned'):
        dispatch = scenes['soana.partner.dispatch' + returned]
        for answer in page(dispatch, 'sent')['Choices']:
            if answer['Next'] == 'sent_share':
                add(answer, 'Set', DISCLOSED)
        home = scenes['soana.partner.homecoming' + returned]
        proposal = deepcopy(page(home, 'share'))
        proposal['Id'] = 'family_proposal'
        proposal['Text'] = '''{n}Corven keeps hold of his pack. He looks at Soana, then at you.{/n}
"A suitor. Now, at my own door. Your letter asked about our wedding; it said nothing of this."
"I am saying it now," {n}Soana answers.{/n} "I want you home. I want this fool too. I have not asked you to guess."
{n}Their son steps back from the bedding.{/n} "Then answer each other. Leave me out of it."
"I still want my wife," {n}Corven says.{/n} "My bed stays mine. No children carrying messages between your beds. And you knock before you enter my house, hunter."'''
        # Proposal is being made here, rather than retconning its dispatch.
        answer = page(home, 'family_answer')['Choices'][0]
        add(answer, 'Requires', 'soana.closed')
        new = deepcopy(answer)
        new['Requires'].remove('soana.closed')
        new['Next'] = 'family_proposal'
        page(home, 'family_answer')['Choices'].append(new)
        home['Nodes'].append(proposal)
        # A shared stance may have been chosen after the authentication left.
        variant(home, 'share', proposal['Text'], requires=(P.PURSUED,),
                forbids=(DISCLOSED,), suffix='proposal')
        # Restore eligibility of the legacy share answer only for disclosure.
        for a in page(home, 'start')['Choices']:
            if a['Next'] == 'share':
                a['Forbids'] = [f for f in a['Forbids'] if f != P.PURSUED]
                add(a, 'Requires', DISCLOSED)

        reply = scenes['soana.partner.reply' + returned]
        page(reply, 'start')['Text'] = '''{n}Soana breaks the fold herself. Outside, a scout checks the demon road. She reads one line twice and touches the clasp.{/n}
"A thorn bush in a wedding wreath. I threw it twice. Nobody else heard him say it."
{n}She lays the answer beside Roan's old letter.{/n}
"He is alive, south of the Wound. Not at my door. Listen to what he actually wrote."'''
        # Retire the no-stance answer into the old romance reply; keep its ID.
        auth = page(reply, 'start')['Choices'][1]
        add(auth, 'Requires', 'soana.closed')
        page(reply, 'start')['Choices'].append(c('[Hear the family answer to her wedding question.]',
            'family_news', forbids=(DISCLOSED, P.SECRET, P.EXCLUSIVE)))
        add(page(reply, 'start')['Choices'][0], 'Requires', DISCLOSED)
        reply['Nodes'].extend((
            n('family_news', 'Soana', '''"He asks whether the spring still runs. Whether I kept his clasp. He wants news of the wood, and news for the children."
{n}She turns the letter over. There is no more writing.{/n}
"That was all I asked him for. He has not answered a question about you, hunter. I never sent one."
{n}She takes up the charcoal.{/n} "If you want more than these visits, say it. I shall put my own wanting beside yours."''',
              c('"Tell him we want each other. Let him answer for himself."', 'send_proposal',
                flags=(P.SHARE, P.DECIDED), forbids=(FRIEND,)),
              c('"Write your family news. I came as a friend."', 'family_friend')),
            n('send_proposal', 'Soana', '''{n}Soana writes beneath the family news. She reads the new lines to you, then folds the sheet into the scout's hand.{/n}
"I want my husband. I want you too. He shall hear both, from me."
{n}The scout takes it south with the next relay. Soana sets the charcoal down and watches him pass the bend.{/n}''',
              c('[Hear Corven answer the proposal she sent.]', 'share', flags=(DISCLOSED,), requires=('soana.closed',)),
              c('[Leave the proposal with the relay. Return for his answer.]',
                flags=(PROPOSAL_SENT, DISCLOSED, FAMILY))),
            n('family_friend', 'Soana', '''{n}She writes news of the spring and the forest, then gives the sheet to the waiting scout.{/n}
"A friend. Bring news of the demon road next time. And something worth eating."
{n}She puts Corven's answer inside her shawl.{/n}''',
              c('[Leave her family words with the relay.]', flags=(P.CONFIRMED, P.TOGETHER, FRIEND)), portrait='Soana'),
        ))
        burned = scenes['soana.partner.returned_letter' + returned]
        family_verdict = '''{n}Soana puts the courier's report beside Corven's letter. Her staff bars the place where you usually sit.{/n}
"I gave you a question for my husband. You burned his words before I could read them."
{n}She writes with the letter on her knees.{/n}
"He shall hear that from me. Our children too. Carry this one, and come back with his answer. After that, stay off my path."'''
        v = variant(burned, 'verdict', family_verdict,
                    requires=('soana.round3.no_stance',), suffix='family')
        for a in v['Choices']:
            add(a, 'Requires', 'soana.closed')
        v['Choices'].append(c('[Carry her family answer. Your visits are over.]', 'answer_family'))
        burned['Nodes'].append(n('answer_family', 'Narrator', '''{n}At the southern relay Corven reads Soana's account of the burned inquiry. He folds it before answering you.{/n}
"She asked about our wedding. You decided she should hear nothing. The relay knows where to find me. She can write by another hand."
{n}His answer reaches Soana unopened. She puts it inside her shawl and lifts her staff from your old place.{/n}
"Your last delivery. Go."''',
            c('[Leave. Corven remains her husband; she will write without you.]',
              flags=(P.DISTANT, P.CONFIRMED, P.BROKEN, 'soana.closed', 'soana.trickster.refused'))))


def histories(scenes):
    state_line = '''"Corven has answered. I know he lives. You heard what he said; don't put sweeter words in his mouth."'''
    name = scenes['soana.name_between']
    old = page(name, 'court')['Text']
    variant(name, 'court', old.replace('"And no tales about time burying Corven for me. If he is dead, he is dead. The years cannot tell me where he lies."', state_line)
            .replace('"I heard you."\n', ''), requires=(KNOWN,))
    old = page(name, 'round2_affair')['Text']
    variant(name, 'round2_affair', old.replace("Corven is my husband; I don't know where he is yet.",
            "Corven is my husband. I know he lives. He has not heard the truth about us."), requires=(KNOWN,))
    for node in name['Nodes']:
        for a in node['Choices']:
            if a['Next'] and (a['Next'].startswith('court') or a['Next'].startswith('round2_affair') or a['Next'] == 'wait'):
                add(a, 'Forbids', FRIEND)
    page(name, 'marriage')['Choices'].append(c('"I came as your friend. I shall keep that answer."',
        'friend', flags=('soana.friendship_chosen',), requires=(FRIEND,)))

    promise = scenes['soana.a_promise_still_spoken']
    page(promise, 'start')['Text'] = '''{n}Soana has charcoal on her skirt and a strip of bark on her lap. Outside, a hunter is calling warnings about the demon road. She leaves the tools beside your usual stone.{/n}
"Sit. I have words for you too, if you have brought ears instead of another sick beast."'''
    # Old uncertainty lives behind the original no-delivery choice, rather
    # than being asserted before the delivered continuation is selected.
    delivered = page(promise, 'delivered')
    delivered['Text'] = '''{n}The sheet Soana sent south is gone. She rubs charcoal from one thumb.{/n}
"My words went with the scout. Not yours. No kindly fool sanding my teeth down."
{n}She clears your usual stone with her arm.{/n}
"I wanted company without a bleeding beast at the door. I still want it. Say what you came for."'''
    h = page(promise, 'history')
    for a in list(h['Choices']):
        if 'no word from Corven' in a['Text']:
            new = deepcopy(a)
            new['Text'] = ('"I still want to court you. I heard his answer."' if a['Next'] == 'court'
                           else '"I heard his answer. I shall remain your friend."')
            add(new, 'Requires', KNOWN)
            if new['Next'] == 'court':
                add(new, 'Forbids', FRIEND)
            add(a, 'Forbids', KNOWN)
            h['Choices'].append(new)
        if a['Next'] == 'court':
            add(a, 'Forbids', FRIEND)
    h['Choices'].append(c('"I shall keep coming as your friend."', 'friend', requires=(FRIEND,)))
    road = scenes['soana.when_the_road_returns']
    old = page(road, 'saved')['Text']
    variant(road, 'saved', old.replace('I still have no news of him.',
        'Corven has answered me. I know he lives.').replace('A thing stealing his voice knew no more than I did.',
        'That thing stealing his voice brought me no word of him.'), requires=(KNOWN,))
    days = scenes['soana.the_days_she_counted']
    old = page(days, 'future')['Text']
    variant(days, 'future', old.replace('Corven gave me flowers, and I was his wife. Writing his name on bark has told me nothing of where he is now. You know that. I will not invent a grave to make you a welcome.',
        'Corven has answered. You heard him. Whatever you promise me now must fit the answer we gave him.'), requires=(KNOWN,))
    # State is heard before the invitation, not corrected after its false
    # premise. Separation takes precedence over a past arrival receipt.
    for event, key in ((name, 'court'), (name, 'round2_affair'), (road, 'saved'), (days, 'future')):
        known = page(event, key + '_r3_known')
        states = [('home', '"Corven is home. His pack is beside his bed. You heard my answer and his; keep them in your ears."')]
        if key != 'round2_affair':
            states.insert(0, ('separated', '"Corven is in the south. We have ended our vows. Our children heard both of us; you heard him too."'))
        for suffix, line in states:
            clone = deepcopy(known)
            clone['Id'] = key + '_r3_' + suffix
            clone['Text'] = line + '\n' + known['Text']
            if suffix == 'home':
                clone['Text'] = clone['Text'].replace('I know he lives.', 'He sleeps in his own house.')
            event['Nodes'].append(clone)
        for node in list(event['Nodes']):
            for answer in list(node['Choices']):
                if answer['Next'] != known['Id']:
                    continue
                for suffix, required, forbidden in (
                        ('separated', P.SEPARATED, ()), ('home', HOME, (P.SEPARATED,))):
                    if suffix == 'separated' and key == 'round2_affair':
                        continue
                    copy = deepcopy(answer)
                    copy.pop('Id', None)
                    copy['Next'] = key + '_r3_' + suffix
                    add(copy, 'Requires', required)
                    add(copy, 'Forbids', *forbidden)
                    node['Choices'].append(copy)
                add(answer, 'Forbids', P.SEPARATED, HOME)
        known['Text'] = '"Corven is alive in the south. His own words reached me; no letter has brought him here."\n' + known['Text']
    # Ordinary paths retain unknown native fate. The unresolved honest offer
    # must say it is an affair, rather than manufacture his participation.
    for event in scenes.values():
        if not event['Id'].startswith('soana.'):
            continue
        for node in list(event['Nodes']):
            if node['Id'].startswith('partner_share_'):
                if not event['Owner'].endswith('Epilogue'):
                    if 'I have no news of him.' in node['Text']:
                        variant(event, node['Id'], '''{n}Soana keeps hold of your wrist. Her thumb stops moving.{/n}
"Corven has answered. You heard him and me. His place has not become yours."
{n}She draws your hand against her throat.{/n}
"I still want you here, hunter. Keep the answer you gave."''',
                                requires=(KNOWN,), suffix='answered')
                    variant(event, node['Id'], node['Text'] + '\n"Until he hears and answers, this is an affair, hunter. We have not told him."',
                            requires=('soana.round2.ordinary_path',), suffix='unanswered')


def concealed(event):
    """Route the existing choices through a stream encounter, same effects.

    House dialogue may precede it; intimacy and its morning occur away from
    Corven. Clone nodes append, while original answer targets stay untouched.
    """
    originals = list(event['Nodes'])
    ids = {x['Id']: 'quiet_r3_' + x['Id'] for x in originals}
    slots = [x['Id'] for x in originals if x['Id'].startswith(event['Id'] + '.explicit.')]
    for i, key in enumerate(slots, len(slots) + 1):
        ids[key] = event['Id'] + '.explicit.' + str(i)
    clones = deepcopy(originals)
    for node in clones:
        node['Id'] = ids[node['Id']]
        # A narrow setting conversion, not a different ritual or romantic yes.
        replacements = {'Outside the cave': 'Beyond the bank', 'outside the cave': 'beyond the bank',
                        'cave mouth': 'stream bend', 'cave wall': 'rock above the stream',
                        'the hearth': 'the bank', 'cold hearth': 'cold ashes',
                        'my cave': 'this wood', 'the cave': 'the stream bank',
                        'her cave': 'the stream bend', 'the door': 'the bend',
                        'cave-bedroom': 'stream bank'}
        for old, new in replacements.items():
            node['Text'] = node['Text'].replace(old, new)
        # Active shelter/household staging changes with the encounter. Memories
        # of her actual cave (including the clay's ash) keep their provenance.
        for old, new in {
                'Come inside before I start sounding like him.': 'Sit before I start sounding like him.',
                'Come inside. I did not call you here to warm Varn\'s ears.': 'Sit close. I did not call you here to warm Varn\'s ears.',
                'She looks into the stream bank.': 'She looks along the bank.',
                'In my own cave? Bold already.': 'You came to silence me? Bold already.',
                'let those boots muddy my floor': 'let those boots share my blanket',
                'The cave gives the foolish words back in a faint echo.': 'The stream drowns the end of the foolish verse.',
                'the shawl from its peg': 'the shawl from beside the blanket',
                'hangs it on a peg': 'lays it beside the blanket',
                'to the entrance': 'to the bend',
                'at the entrance': 'at the bend',
                'At the entrance': 'At the bend',
                'across the entrance': 'across the path',
                'against the wall': 'against the rock',
                'in their new corner': 'under the rock',
                'leap out of the corner': 'leap out of the trees',
                'Then come in.': 'Then sit close.',
                'We have dry shelter.': 'I brought dry wool.',
                'if he ever comes to read it': 'when he reads it at home',
                'Corven. I finished what I began.': 'Corven. I finished what I began. He can read it when I go home.',
                'I will not dig him a grave to make room for you, and I will not pretend he never was.': 'He is home. We keep these visits from his door; I have not offered you his place.',
        }.items():
            node['Text'] = node['Text'].replace(old, new)
        for a in node['Choices']:
            if a['Next'] in ids:
                a['Next'] = ids[a['Next']]
        if node['Id'] == ids[originals[0]['Id']]:
            node['Text'] = '''{n}Soana meets you above the stream, out of sight of her house. She has brought the blanket and what she needs for the visit. No light shows through the trees behind her.{/n}
"Corven is home. We keep this away from his door. Follow me, hunter. The demon road can wait one evening."\n''' + node['Text']
        if 'morning' in node['Id']:
            node['Text'] += '\n{n}She rolls the blanket and goes home alone. You take the longer path. Nothing of yours is left in Corven\'s house.{/n}'
    start = originals[0]
    for a in start['Choices']:
        add(a, 'Forbids', P.QUIET_RETURN)
    start['Choices'].append(c('[Meet her away from Corven\'s house, above the stream.]',
        ids[start['Id']], requires=(P.QUIET_RETURN,)))
    event['Nodes'].extend(clones)


def late_locations(scenes):
    for kind in ('commit', 'luck_late', 'living_late'):
        event = scenes['soana.trickster.epilogue.' + kind]
        for node in event['Nodes']:
            if node['Id'] not in ('start', 'round2_vow') and not node['Id'].startswith('partner_'):
                continue
            # These pages retain their epilogue-local legacy exits. The shared
            # slot/morning variants already select bank versus home correctly.
            if not any(word in node['Text'] for word in ('blanket', 'furs', 'cord', 'house')):
                continue
            original = node['Text']
            quiet = original.replace('the furs', 'her cloak on the bank').replace('the blanket', 'her cloak')
            if node['Id'] == 'start':
                quiet = '''{n}Soana met the Commander above the stream. She left her house dark behind her.{/n}
"Corven is home. You come here, hunter. I have not offered you his door."\n''' + quiet
            node['Text'] = ('{n}That spring Soana met the Commander in Wintersun.{/n}' if node['Id'] == 'start'
                            else '{n}Soana took up the cord.{/n}' if node['Id'] == 'round2_vow'
                            else '{n}Soana heard the Commander\'s answer.{/n}')
            node.setdefault('Paragraphs', []).extend((
                p(original, forbids=(P.QUIET_RETURN,)),
                p(quiet, requires=(P.QUIET_RETURN,)),
            ))
    coda = page(scenes['soana.lastcall.page'], 'page')
    coda.setdefault('Paragraphs', []).append(p(
        '''{n}After the war Soana met the Commander above the stream. She caught {mf|his|her} collar and kissed {mf|him|her}, then shoved a basin into {mf|his|her} hands.{/n}
"Wash. You still stink of the road."
{n}She waited on the bank, with the blanket rolled beside her. Afterwards she went home to Corven alone; the Commander left by the longer path.{/n}''', requires=(P.QUIET_RETURN,)))


def endings(scenes):
    for event in scenes.values():
        if not event['Id'].startswith('soana.') or not event['Owner'].endswith('Epilogue'):
            continue
        for node in event['Nodes']:
            if event['Id'] == 'soana.partner.epilogue.broken':
                node['Text'] = node['Text'].replace(
                    'When visitors asked after the second bundle at her fire, she pointed them down the path. ', '')
            for block in list(node.get('Paragraphs', [])):
                if P.DISTANT in block.get('Requires', []):
                    block['Text'] = block['Text'].replace(
                        'There was no answer to either.',
                        'Corven remained in the south; the marriage had survived the rejected visitor.')
                if FAMILY in block.get('Requires', []):
                    block['Text'] = '{n}Corven was alive in the south. His answer to Soana\'s wedding question had reached her. The affair was absent from the question she had sent; his reply had brought no word of it to his door.{/n}'
                if P.TOGETHER not in block.get('Requires', []):
                    continue
                family = deepcopy(block)
                add(block, 'Requires', ARRANGEMENT)
                add(family, 'Forbids', ARRANGEMENT)
                if event['Id'] in P.LOSS_ENDINGS:
                    family['Text'] = ('{n}Corven had been home when Soana died. He took her clasp south and told their children himself. The Commander had visited as a friend.{/n}'
                                      if HOME in family['Requires'] else
                                      '{n}Corven had remained her husband in the south. The news of her death followed her family letters; he carried it to their children. The friendship had asked no lover\'s terms of Corven.{/n}')
                else:
                    family['Text'] = ('{n}Corven and Soana had kept their marriage. When the Commander came as a friend, Soana set out a cup and left the bedding rolled.{/n}'
                                      if event['Owner'] != 'AeonEpilogue' else
                                      '{n}In the erased history Corven and Soana had remained married, and the Commander had visited as a friend. That history brought no word of their lives in the world without the Wound.{/n}')
                add(family, 'Requires', FRIEND)
                node['Paragraphs'].append(family)
                refused = deepcopy(family)
                refused['Requires'].remove(FRIEND)
                add(refused, 'Forbids', FRIEND)
                refused['Text'] = '{n}Corven and Soana had kept their marriage. The Commander had refused Corven\'s terms and been sent away. No welcome as a lover survived that answer.{/n}'
                if event['Id'] in P.LOSS_ENDINGS:
                    refused['Text'] = '{n}Corven had remained Soana\'s husband after the Commander was sent away. Her death left their children his news to carry; the rejected hunter had no place in that mourning.{/n}'
                node['Paragraphs'].append(refused)
            if event['Id'] == 'soana.trickster.epilogue.unvowed':
                for block in list(node.get('Paragraphs', [])):
                    if 'She fed them, scolded them and took them to bed' not in block['Text']:
                        continue
                    quiet = deepcopy(block)
                    add(block, 'Forbids', P.QUIET_RETURN)
                    add(quiet, 'Requires', P.QUIET_RETURN)
                    quiet['Text'] = '''{n}The Commander had done the work by the graves, and Soana had called them back for herself. After Corven came home, she met her hunter above the stream. She brought food and a blanket, scolded them for being late and caught their belt. Afterwards she went home alone. She never let them near the knot.{/n} "You had your chance at that."'''
                    node['Paragraphs'].append(quiet)
            if event['Id'] == 'soana.trickster.epilogue.by_your_hand':
                node.setdefault('Paragraphs', []).append(p(
                    '{n}Corven learned who had killed Soana and refused every message bearing the Commander\'s name. Their children heard Corven\'s account. No hunter was welcomed at that family\'s fire again.{/n}', requires=(KNOWN,)))


def attributed_variants(scenes):
    # The legacy pages contain scripted Commander replies. New variants leave
    # the player's words to the answer buttons; retain only Soana's speech.
    commander_lines = (
        'You could have told me that first.', 'Like a tree?', 'And time for me?',
        'I am here, Soana.', 'You stayed to watch?', 'You expect him to look too.',
        'He remembered the marked camp.', 'You have no rite prepared?',
        'Only thought about it?', 'I would rather come back.', 'Of cord and clay?',
        'I was looking at the tools.', 'Almost?', 'Will you renew it?',
        'Anything else?', 'Worth sending them away with less?',
        'Did you say you were wrong?', 'And stopped?', 'The warning?', 'Which?',
        'Will you ask her again?', 'Another task?',
        'Nor have I stopped objecting because we share a fire.',
        'The forest is still in danger.', 'You could stop talking now.',
        'I will come back.', 'I can do that.', 'I meant it then.', 'I would not.',
        'And you will leave the lesson out?', 'The evening.',
        'What would you have me do?', 'I want to come back.',
        'Were you expecting one?', 'Save them.', 'I should hope to do better.',
        'No scolding?', 'I will.', 'It might be finished.',
    )
    for event in scenes.values():
        if not event['Id'].startswith('soana.'):
            continue
        for node in event['Nodes']:
            if '_r3_' not in node['Id']:
                continue
            for line in commander_lines:
                node['Text'] = node['Text'].replace('"' + line + '"\n', '')
            # A newline can separate different speakers. Keep quotations intact.
            repairs = {
                '"Until the grass eater lay down.': '"I stayed to watch until the grass eater lay down.',
                '"Let him. I stacked it myself.': '"Varn can inspect the kindling too. I stacked it myself.',
                'And you have reminded me twice.': 'And you have reminded me.',
                '"So far."': '"So far I have only thought about it."',
                '"They will survive a night without me.': '"The tools will survive a night without me.',
                '"When I want that ground kept.': '"I will renew the notch when I want that ground kept.',
                '"Two words. She tried to get a third.': '"I said I was wrong. Two words. She tried to get a third.',
                '"After I asked how many last sacks followed the first. She tied them.': '"She stopped after I asked how many last sacks followed the first. She tied them.',
                '"Left alone.': '"The warning was left alone.',
                '"If she comes. Until then,': '"If she comes, I shall ask her for another report. Until then,',
                '"Has it ever ceased? Sit down.': '"The forest is still in danger. Sit down.',
                '"You came to silence me? Bold already."': '"A place beside my blanket? You will have to bear my tongue as well, hunter."',
                '"At last, something simple from a Commander."': '"A simple request, even for a Commander."',
                '"How long?"': '"You came for the evening. Sit before it is gone."',
                'At the hour you named she rises.': 'Before the night is over she rises.',
                '"They will keep. Yours may not have."': '"My scoldings will keep. Fine promises might not survive that road."',
                '"Then stop boasting."': '"Come here. Give me something better to kiss."',
                'Do not spoil a perfectly good complaint.': 'Bloody fool. I had plenty left to say.',
            }
            for old, new in repairs.items():
                node['Text'] = node['Text'].replace(old, new)
            # These variants are Soana's monologues. The homecoming proposals
            # instead contain Corven, Soana and their son, with explicit turns.
            if not event['Id'].startswith('soana.partner.homecoming'):
                node['Text'] = re.sub(r'"\s*\n\s*"', ' ', node['Text'])


def dead_histories(scenes):
    """Select Corven's actual whereabouts before both dead and letter pages."""
    event = scenes['soana.the_days_she_counted']
    dead_choices = deepcopy(page(event, 'dead')['Choices'])
    states = (
        ('separated', P.SEPARATED, (), 'Corven is in the south. We ended our vows. He can read this with the family news.'),
        ('home', HOME, (P.SEPARATED,), 'Corven is home. He will have a fine long answer to give me when he reads this.'),
        ('known', KNOWN, (P.SEPARATED, HOME), 'Corven is alive in the south. This goes with the next relay; he will have a fine long answer to write.'),
    )
    for key in ('dead', 'letter'):
        original = page(event, key)
        for suffix, required, forbidden, line in states:
            replacement = original['Text'].replace(
                'Corven will have a fine long answer to give me, if he ever comes to read it.', line).replace(
                'Corven. I finished what I began.', 'Corven. I finished what I began. ' + line)
            if key == 'letter':
                replacement = '"' + line + '"\n' + replacement
            variant(event, key, replacement, requires=(required,), forbids=forbidden, suffix=suffix)
        # Variants of dead carry their corresponding letter, rather than
        # requiring the player to select history a second time.
    for suffix, _, _, _ in states:
        clone = page(event, 'dead_r3_' + suffix)
        clone['Choices'] = deepcopy(dead_choices)
        for answer in clone['Choices']:
            answer['Next'] = 'letter_r3_' + suffix


def finish(scenes):
    # Keep the existing 48-hour deed clock beside the current return reader.
    # Derived availability receipts have no stored timestamp of their own.
    add(scenes['soana.trickster.returned.graveyard'], 'Requires', P.RETURNED)
    family(scenes)
    histories(scenes)
    dead_histories(scenes)
    # A secret answer declares the affair on this very choice. Requiring its
    # stance beforehand made that first answer circular. Keep her invitation,
    # every price, and all gates on honest shared/exclusive arrangements.
    for event in scenes.values():
        if not event['Id'].startswith('soana.'):
            continue
        for node in event['Nodes']:
            for answer in node['Choices']:
                if P.SECRET in answer['Set'] and set(answer['Set']) & {
                        'soana.committed', 'soana.round2.postwar_accepted'} and \
                        'soana.round2.partner_answer' in answer['Requires']:
                    answer['Requires'] = [f for f in answer['Requires']
                                          if f != 'soana.round2.partner_answer']
                    add(answer, 'Forbids', P.BROKEN)
    # Keep a postponed visit selectable when the existing partner-answer gate
    # blocks intimacy. This neither completes the visit nor changes affection.
    for sid, key in (('soana.after_the_last_visitor', 'private'),
                     ('soana.before_the_far_road', 'beloved'),
                     ('soana.before_the_far_road', 'courtship')):
        page(scenes[sid], key)['Choices'].append(c(
            '[Return after she has heard the southern answer.]', abort=True))
    for sid in ('soana.after_the_last_visitor', 'soana.before_the_far_road',
                'soana.the_days_she_counted',
                'soana.trickster.returned.terms', 'soana.trickster.returned.second_ask',
                'soana.trickster.returned.rebind', 'soana.trickster.missed.bowl',
                'soana.trickster.missed.second_ask'):
        concealed(scenes[sid])
    endings(scenes)
    late_locations(scenes)
    attributed_variants(scenes)
