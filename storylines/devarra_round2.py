"""Authored Devarra set-piece repairs (SP1–6), not native dragon customs.

Applied to this route's own records before export. Existing records and answer
positions stay in place; history variants append. Native evidence is read-only:
native_facts.py's four egg causes, Greybor death/dismissal, actual deactivation,
coronation, and Nidalynn's earned custody/hatching/departure. See the copied TP
and set-piece sheets for the native GUID ledger and authored boundaries.
"""
from copy import deepcopy

from story_format import c, n, p

P = 'devarra.trickster.'
T = 'devarra.tower.'
FLOWN = P + 'flown'
LEASH = P + 'leash_cut'
EGG_BILL = P + 'cost.egg_withheld'
EGG_OWED = 'nidalynn.trickster.egg_owed'
HATCHED = 'nidalynn.trickster.hatched'
NORTH = 'nidalynn.trickster.left_with_it'
INTEREST = P + 'cost.second_ask_story'
INTEREST_PAID = T + 'second_ask_story_paid'
REPORTED = T + 'book_reported'
UNREPORTED = T + 'book_unreported'
BOOK_CLOSED = T + 'city_book_closed'
CAUSES = tuple('native.history.eggs.' + suffix for suffix in (
    'manually_smashed', 'commanded_destruction', 'golem_wrong_password', 'watched_crushing'))
TERMINAL = ('eggs.omelet', 'eggs.druids', 'eggs.destroyed')


def _scene(scenes, suffix):
    return next(s for s in scenes if s['Id'] == suffix)


def _nodes(scene):
    return {node['Id']: node for node in scene['Nodes']}


def _add(record, field, *values):
    record[field] = list(dict.fromkeys(record.get(field, []) + list(values)))


def _voice(id, text, *choices):
    return n(id, 'Devarra', text, *choices, portrait='Devarra',
             speaker_unit='c540d81c08822c14da75761493427e4c')


def _fork(scene, source, index, id, text, requires=(), forbids=()):
    """Retain the old answer/target; append the mutually exclusive sibling."""
    nodes = _nodes(scene)
    old = nodes[source]['Choices'][index]
    alt = deepcopy(old)
    _add(old, 'Forbids', *requires)
    _add(old, 'Requires', *forbids)
    _add(alt, 'Requires', *requires)
    _add(alt, 'Forbids', *forbids)
    target = deepcopy(nodes[old['Next']])
    target.update(Id=id, Text=text)
    alt['Next'] = id
    nodes[source]['Choices'].append(alt)
    scene['Nodes'].append(target)
    return target


def _fate_choices(node):
    """Accumulated native histories: omelet > transfer > destroyed > project."""
    for answer in node['Choices']:
        req = answer.get('Requires', [])
        if 'eggs.druids' in req:
            _add(answer, 'Forbids', 'eggs.omelet')
        elif 'eggs.destroyed' in req:
            _add(answer, 'Forbids', 'eggs.omelet', 'eggs.druids')
        elif 'eggs.project' in req:
            _add(answer, 'Forbids', *TERMINAL)


def _destruction(scene, node_id, texts):
    """Old target becomes truthful fallback; causes append in stable order."""
    nodes = _nodes(scene)
    old = nodes[node_id]
    old['Text'] = texts[-1]
    # Every incoming destruction answer uses the same cause priority.
    incoming = [(node, answer) for node in scene['Nodes']
                for answer in list(node['Choices']) if answer.get('Next') == node_id]
    for node, answer in incoming:
        original = deepcopy(answer)
        _add(answer, 'Forbids', *CAUSES)
        for index, cause in enumerate(CAUSES):
            alt = deepcopy(original)
            alt['Next'] = node_id + '.' + str(index + 1)
            _add(alt, 'Requires', cause)
            _add(alt, 'Forbids', *CAUSES[:index])
            node['Choices'].append(alt)
    for index, text in enumerate(texts[:-1]):
        new = deepcopy(old)
        new.update(Id=node_id + '.' + str(index + 1), Text=text)
        scene['Nodes'].append(new)


def polish_spine(scenes):
    """SP1 verified escape, SP2 accounting, SP6 first versus later payment."""
    visit = _scene(scenes, P + 'flight.eggs')
    visit['Kind'] = 'visit'  # Physical road encounter; retain the remote hub fallback.
    nodes = _nodes(visit)
    # She can count a missing life without knowing its keeper. Debt is never love.
    nodes['stone']['Choices'][1]['Next'] = 'count'
    nodes['failed']['Choices'][0]['Next'] = 'count'
    visit['Nodes'].extend([
        _voice('count', '"Before you begin: how many?" {n}One claw taps the cart. The sentries draw farther back.{/n}',
               c('Continue', 'missing', requires=(EGG_OWED,), flags=(EGG_BILL,)),
               c('Continue', 'which_eggs', forbids=(EGG_OWED,))),
        _voice('missing', '"Eleven accounted for. I laid twelve." {n}The claw punches through the cart plank.{/n} '
               '"One life missing from my clutch. You owe it, crusader. I will learn where it went; '
               'I do not need to know that to send the bill. Now tell me about the others."',
               c('Continue', 'which_eggs')),
    ])
    _fate_choices(nodes['which_eggs'])
    _fate_choices(nodes['clutch'])
    _fork(visit, 'which_eggs', 2, 'said_project_combat',
          '"They are in your vaults. You broke the stone, then carried off what it guarded." '
          '{n}She turns toward Drezen.{/n} "Another lock. Keep them warm, crusader. '
          'If they are cold when I come for them, Drezen will be warm enough."', forbids=(LEASH,))
    _destruction(visit, 'said_destroyed', [
        '"You broke the shells yourself." {n}Her voice is flat.{/n} "Not the stone. You. '
        'I lay bleeding on a mountain while you smashed my children on the floor. Tell me that part again, to my face."',
        '"You gave the order. Destruction." {n}She pronounces each syllable.{/n} '
        '"The stone listened to you. It could have lowered its fists. You told it to close them."',
        '"The wrong word." {n}Her claws sink through the cart.{/n} "You guessed, and the stone killed them. '
        'I trusted your mouth with my clutch. Now look at me and tell me what came out of it."',
        '"You waited to see what would happen." {n}The horses pull against their ropes.{/n} '
        '"Did the stone disappoint you? Did it take too long? I waited on my mountain too. My waiting bought you time."',
        '"Broken shells on the chamber floor." {n}She holds your gaze.{/n} '
        '"I did not go when the charm called. You went instead. My clutch is dead. Give me your account."',
    ])
    # Preserve the old admissions, but remove their false cause and append exact responsibility.
    nodes['clutch']['Choices'][6]['Text'] = '"They died while I was in the Sanctum. I owe you the account."'
    for answer in nodes['clutch']['Choices'][5:7]:
        _add(answer, 'Forbids', CAUSES[0], CAUSES[1])
    for cause, text in zip(CAUSES[:2], ('"I smashed them. It was my hand."', '"I ordered the stone to destroy them."')):
        nodes['clutch']['Choices'].append(c(text, 'marked',
            requires=('eggs.destroyed', cause), forbids=('eggs.omelet', 'eggs.druids'),
            flags=(P + 'returned', 'devarra.started', P + 'cost.woken_hungry', P + 'marked')))
    nodes['marked']['Text'] = ('"Dead while you stood there." {n}Her claw rakes the cart beside your hand.{/n} '
        '"Now you can stand here while I decide what to do with you. Your story had better be very good."')
    for index, cause in enumerate(CAUSES[:2]):
        target = 'marked.responsible.' + str(index + 1)
        nodes['clutch']['Choices'][-2 + index]['Next'] = target
        visit['Nodes'].append(_voice(target,
            ('"Your hand broke them."' if index == 0 else '"You ordered their deaths."') +
            ' {n}She drives her claw through the cart between your arms, splitting it. The horses rear.{/n} '
            '"Look at what you did. I shall hear your story, crusader. I like to play with my food. '
            'Do not imagine that makes you anything else."', c('[Hold her gaze.]')))
    tithe = _nodes(_scene(scenes, P + 'after.tithe'))['tithe_free']
    tithe['Text'] = tithe['Text'].replace('now that she is off the stone\'s leash', 'now that she has left the mountain where she waited')
    # Account for the saved twelfth in all six fates without naming an unknown keeper.
    for id in ('said_omelet', 'said_druids', 'said_project', 'said_left', 'said_collected', 'said_project_combat'):
        node = _nodes(visit)[id]
        node['Text'] = node['Text'].replace('Nobody had touched them. Nobody had guarded them, either.',
                                           'No guard remained at the door.')

    greybor = _scene(scenes, 'devarra.react.greybor.flown')['Nodes'][0]
    greybor['Text'] = ('{n}Greybor rests his hand on the pommel of his blade.{/n} "We hunted her. '
        'Now she is on your ridge, alive. You have a dragon; I have an unfinished job." '
        '{n}He looks toward the north wall.{/n} "Next time you want the quarry to live, tell me '
        'before I take the contract. Let me decide whether the job is worth my name."')
    _scene(scenes, 'devarra.react.greybor.repeat_work')['Nodes'][0]['Text'] = (
        _scene(scenes, 'devarra.react.greybor.repeat_work')['Nodes'][0]['Text'].replace(
            'Greybor does not look up from the whetstone.', 'Greybor tests his edge with his thumb before he asks about the dragon.'))

    deferred = _scene(scenes, P + 'epilogue.commit')['Nodes'][0]
    deferred['Text'] = ("{n}After the war a grey dragon landed on the Commander's roof. Tiles broke beneath her claws. "
        'The Commander came into the yard barefoot.{/n} "The story will do. Now answer the question you left on my mountain. '
        'Once a year. A small bite. The arm that does not hold your sword." '
        '{n}She waited with her head above the yard until the Commander bared that arm. Then she drew back.{/n} '
        '"Spring. My ridge. Come yourself. I will not send the old man." '
        '{n}In spring she was there, and the Commander climbed to her fire. She took the first small bite; '
        'the Commander bound it and stayed until dawn. The next spring she returned, and found the path occupied.{/n}')
    living = _scene(scenes, P + 'epilogue.woken')['Nodes'][0]
    living['Text'] = ('{n}In spring Devarra returned to the north ridge. The Commander climbed to meet her, '
        'baring the non-sword arm when she lowered her head. She took her small annual bite and watched '
        'while the Commander bound it. After the third appointment the surgeons stopped asking about '
        'the crescent scar. The ruined watchtower remained hers; the stair bore another scratch for every visit.{/n}')
    living.setdefault('Paragraphs', []).extend([
        p('{n}Before the first appointment she demanded the night the Commander had stayed below: '
          'who had been there, what had been said, why the path had remained empty. She heard the whole account. '
          '"The interest," she said. "Now the arm."{/n}', requires=(INTEREST,), forbids=(INTEREST_PAID,)),
        p('{n}At later appointments she sometimes asked about that night below. The Commander had already '
          'paid the account by her fire; she wanted the part where the decision changed.{/n}', requires=(INTEREST_PAID,)),
        p('{n}At the first appointment there was no old bite to show her. She made the crescent herself, '
          'then left room against her flank for the Commander to stay.{/n}', forbids=(T + 'first_bite',)),
    ])
    # No automatic acceptance: the effect-free legacy ending exits remain untouched.
    refused = _scene(scenes, P + 'epilogue.refused')['Nodes'][0]
    refused['Text'] = '{n}A grey woundwyrm hunted the old Wound for years. She passed over Drezen once, high above the north wall. She did not land. The tower stair kept the marks of the Commander\'s visits, with no new line beside them.{/n}'

    from storylines.devarra_round3 import spine
    spine(scenes)


def polish_tower(scenes):
    """SP2 custody, SP3 reopening, SP4 first visit, SP5 wager, SP6 farewell."""
    second = _scene(scenes, T + 'back_up_the_mountain')
    nodes = _nodes(second)
    nodes['her']['Text'] += (' "And interest: the true account of the night you stayed below. '
        'Whose company you kept. What you said about me. Bring it when I light the fire."')
    _add(nodes['her']['Choices'][0], 'Set', INTEREST)
    nodes['yes']['Text'] = ('"Not the sword arm." {n}She looks over the city, then back at you.{/n} '
        '"The night below comes first. Leave the pretty lies down there. I will hear why you came back."')

    first = _scene(scenes, T + 'first_bite')
    nodes = _nodes(first)
    for answer in nodes['ridge']['Choices']:
        _add(answer, 'Forbids', INTEREST)
    nodes['ridge']['Choices'].append(c('Continue', 'interest_story', requires=(INTEREST,)))
    first['Nodes'].extend([
        _voice('interest_story', '"You kept me waiting. Now I collect." {n}She leaves a gap in the ring of fire for you.{/n} '
               '"The night below. Begin with the door you went through instead of mine."',
               c('[Tell her the night as it happened, including why you came back.]', 'interest_collected', flags=(INTEREST_PAID,))),
        _voice('interest_collected', '{n}She stops you twice: once at a name, once where you hurry over your own answer. '
               'At last her claw lifts from the path.{/n} "There. No interest left on that night. Come closer. '
               'The annual tariff has not changed."',
               c('Continue', 'inside', forbids=(FLOWN,)), c('Continue', 'inside_free', requires=(FLOWN,))),
    ])
    for id in ('bite', 'bite_free'):
        # Ordinary tariff has been collected; intimacy is her invitation, not a bill.
        nodes[id]['Text'] = nodes[id]['Text'].replace('"All of it. Pay the rest."', '"Stay. I did not call you up here for your arm alone."')
        nodes[id]['Choices'][0]['Next'] = T + 'first_bite.explicit.1'
    # Slot brief: private first-night continuation after payment, then bandaged morning.
    first['Nodes'].append(n(T + 'first_bite.explicit.1', 'Narrator',
        '{n}The fire burns low around the ruined tower. Before dawn, the path remains empty.{/n}', c('Continue', 'morning'), portrait='Devarra'))
    nodes['after']['Text'] = ('"Small. I said it would be small." {n}She lifts her tail from the stair, '
        'then turns her head to keep you in sight.{/n} "The old man went home. The watch will have seen the fire die. '
        'Let them count another hour. Stay."')
    nodes['after']['Choices'].append(c('[Bind the arm and go down before the watch changes.]', flags=(T + 'first_bite',)))

    dwarf = _scene(scenes, T + 'the_dwarf')
    nodes = _nodes(dwarf)
    _add(nodes['climb']['Choices'][0], 'Forbids', 'greybor.dead', 'greybor.kicked_out')
    _fork(dwarf, 'climb', 1, 'me_free',
          '{n}She brings her eye level with yours.{/n} "The hand that hired the blade. Then the mouth that offered '
          'me another ending." {n}She turns her scar toward you.{/n} "I flew with that wound. You went into Vang\'s house. '
          'I have not forgotten either part. Do not try to make one cancel the other."', requires=(FLOWN,))
    nodes['climb']['Choices'].extend([
        c('"He is dead. You cannot collect from him."', 'dwarf_dead', requires=('greybor.dead',)),
        c('"He left my service. I cannot speak for him."', 'dwarf_gone', requires=('greybor.kicked_out',), forbids=('greybor.dead',)),
    ])
    nodes['me']['Text'] = nodes['me']['Text'].replace('{n}It is almost fond.{/n}', '{n}Her teeth remain level with your throat.{/n}')
    dwarf['Nodes'].extend([
        _voice('dwarf_dead', '"Dead." {n}Her claws scrape the sill.{/n} "Something else took him first. '
               'Then I keep the blade in this scar. You may keep the name."', c('Continue', 'end_dead')),
        _voice('dwarf_gone', '"Then do not." {n}She folds the scar beneath her wing.{/n} '
               '"If he climbs my mountain he will speak for himself. I will hear him before I decide what to eat."', c('Continue', 'end_gone')),
        n('end_dead', 'conversant', '"He is dead, then." {n}The Storyteller lowers his head.{/n} '
          '"He once called my story about the ring not bad. I had hoped to tell him another."', c('"I know."', flags=(T + 'dwarf_spoken',))),
        n('end_gone', 'conversant', '"He has gone." {n}The Storyteller turns toward the gate.{/n} '
          '"Then no message to carry to him. I hope he keeps clear of the ridge."', c('"So do I."', flags=(T + 'dwarf_spoken',))),
    ])
    for node in list(dwarf['Nodes']):
        for answer in list(node['Choices']):
            if answer.get('Next') != 'end':
                continue
            _add(answer, 'Forbids', 'greybor.dead', 'greybor.kicked_out')
            node['Choices'].extend([c('Continue', 'end_dead', requires=('greybor.dead',)),
                c('Continue', 'end_gone', requires=('greybor.kicked_out',), forbids=('greybor.dead',))])

    # Same flaw, both bodily-care histories. She directs the work, rather than becoming a pet.
    for suffix in ('the_itch', 'the_scabs'):
        node = _nodes(_scene(scenes, T + suffix))['silent']
        node['Text'] = ('{n}Her breathing slows while you scrape the last plates loose. When the spade stops, '
            'one eye opens.{/n} "Under the wing. You missed one." {n}She raises it herself. '
            'You finish there and climb down; she tests the shoulder against the wall and leaves the stone standing.{/n}')
    says = _nodes(_scene(scenes, T + 'what_she_says'))['says']
    says['Text'] = says['Text'].replace('She told me so as though she were confessing to a disease.',
        'She made me stand at the sill until she heard you call an order. Then she sent me away.')
    soft = _nodes(_scene(scenes, T + 'the_soft_place'))
    soft['after']['Text'] = ('"There. Now take your hand away. Slowly." {n}She holds the wing above you '
        'while you lift your palm. Then she lowers it around your shoulder.{/n} "Do not tell the old man. '
        'Not your generals. Not the other things you love. This one is mine."')
    # Warmth is requested for the particular injured hide/wing in each history.
    for suffix in ('first_snow', 'first_snow_free'):
        winter = _nodes(_scene(scenes, T + suffix))
        winter['braziers']['Text'] = ('{n}The teamsters stop below the tower. You carry the last brazier inside. '
            'Devarra points with her chin until you put it under the raised wing; she has arranged the others '
            'along her flank. Snow melts on the sill. She drags the new fleeces beneath her and watches you feed the coals.{/n}')
        winter['lean']['Text'] = ('{n}You sit between the braziers with your back against her flank. She shifts '
            'the sore side toward the coals and lowers a wing over you. Outside, the wind rattles the frozen brush. '
            'Inside, her breathing steadies against your shoulder.{/n}')
        winter['lean_her']['Text'] = ('"Warmer than your iron." {n}She keeps the wing lowered.{/n} '
            '"Stay until the coals need feeding. Then you may get up. If the quartermaster wants the brazier back, '
            'send him here to ask for it."')

    clutch = _scene(scenes, T + 'the_clutch')
    nodes = _nodes(clutch)
    nodes['withheld']['Text'] = nodes['withheld']['Text'].replace('I have thought about that every night since.', 'I still count the eggs you kept from me.')
    # Terminal disposition overrides stale route-local custody promises too.
    for answer in nodes['start']['Choices']:
        if answer.get('Next') in ('withheld', 'collected'):
            _add(answer, 'Forbids', *TERMINAL)
    nodes['start']['Choices'].extend([
        c('Continue', 'later_omelet', requires=('eggs.omelet',), forbids=('devarra.trickster.cook_given', 'devarra.trickster.cook_refused')),
        c('Continue', 'later_druids', requires=('eggs.druids',), forbids=('eggs.omelet', P + 'hunting_druids')),
        c('Continue', 'later_destroyed', requires=('eggs.destroyed',), forbids=('eggs.omelet', 'eggs.druids', P + 'pointed_at_xanthir', P + 'marked')),
    ])
    clutch['Nodes'].extend([
        _voice('later_omelet', '"I heard the vault go quiet. Then I smelled your kitchens." {n}She looks at the city.{/n} '
               '"Do not tell me they are warm. Tell me what happened after you promised."', c('[Give her the account.]', 'end')),
        _voice('later_druids', '"The vault is empty. They went east." {n}Her wing blocks the city from view.{/n} '
               '"Men who smelled of gold took them. Your promise does not put them back. Give me their road."', c('[Tell her what you know of the transfer.]', 'end')),
        _voice('later_destroyed', '"Broken shells. No clutch to sit with." {n}She leaves the stair clear.{/n} '
               '"Tell me how it happened. No warm straw in this account."', c('[Give her the account of their destruction.]', 'end')),
    ])
    # An already incurred missing-life bill cannot wait for an optional confession.
    short = _scene(scenes, T + 'one_short')
    short['Requires'] = [EGG_OWED if key == 'nidalynn.trickster.primed' else key for key in short['Requires']]
    for answer in _nodes(short)['start']['Choices']:
        for field in ('Requires', 'Forbids'):
            answer[field] = ['nidalynn.trickster.egg.vault' if key == 'nidalynn.trickster.eggs.vault' else key
                             for key in answer.get(field, [])]
    for node in short['Nodes']:
        for answer in node['Choices']:
            if answer.get('Next') in ('told', 'lied', 'lied_free', 'safe'):
                _add(answer, 'Set', EGG_BILL)
    _nodes(short)['told']['Text'] = ('"The smallest." {n}Her claws close on the sill.{/n} '
        '"Alive, you say. Keep it so. That does not settle what you took from me." '
        '{n}She looks at you.{/n} "I know who carried it out now. I do not yet know whose hearth it reached. '
        'When I name the life you owe, you will hear the price."')

    small = _scene(scenes, T + 'smallest_egg')
    nodes = _nodes(small)
    _fork(small, 'start', 0, 'climb_unhatched',
        '{n}She keeps her head on the sill, watching the east wall.{/n} "Twelve. One still inside its shell, '
        'in the silver\'s keeping. You named it before your people. Now answer to me."', forbids=(HATCHED,))
    _fork(small, 'start', 1, 'climb_free_unhatched',
        '{n}She keeps her head on the sill, watching the east wall.{/n} "Twelve. One still inside its shell, '
        'in the silver\'s keeping. You named it before your people. Now answer to me."', forbids=(HATCHED,))
    # Branch before any bodily kiln setup; no present Nidalynn cameo is manufactured.
    nodes['start']['Text'] = '"She heard your confession. She wants the thief fetched." {n}The Storyteller stands aside.{/n}'
    for answer in nodes['start']['Choices']:
        _add(answer, 'Forbids', NORTH)
    north = deepcopy(nodes['climb_free'])
    north.update(Id='climb_north', Text='{n}Her eye follows the north road.{/n} "The silver took the child north. '
        'I saw them go. Her keeping, her road. You are still here, crusader. So is the bill."')
    nodes['start']['Choices'].append(c('Continue', 'climb_north', requires=(NORTH,)))
    small['Nodes'].append(north)
    for id in ('climb', 'climb_free', 'climb_unhatched', 'climb_free_unhatched', 'climb_north'):
        _fate_choices(_nodes(small)[id])
    _destruction(small, 'destroyed', [
        '"Eleven shells you smashed yourself. One you carried away alive." {n}Her claws bite the sill.{/n} "That was your choice. Account for both parts."',
        '"Eleven under the fists you ordered closed. One carried out before them." {n}Her claws bite the sill.{/n} "You gave the order, crusader."',
        '"Eleven killed by the wrong password. One carried clear." {n}Her claws bite the sill.{/n} "You guessed with their lives."',
        '"Eleven crushed while you watched. One carried clear." {n}Her claws bite the sill.{/n} "You had time to see what happened."',
        '"Eleven dead. One in the silver\'s keeping." {n}Her claws bite the sill.{/n} "Tell me how the shells broke. Do not hide behind the stone."',
    ])
    # Child location and knowledge must not be invented by a clutch-fate paragraph.
    for id in ('kept_eleven', 'eleven', 'omelet', 'druids', 'vault', 'druids_straw'):
        node = _nodes(small)[id]
        parts = node['Text'].split('{n}Her claws close on the stone.{/n}')
        if len(parts) == 2:
            node['Text'] = parts[0] + '{n}Her claws close on the stone.{/n} "And one you carried to the silver, and called a rock."'
    nodes['silver']['Text'] = '"The silver is keeping her. You carried her out." {n}Her lip lifts off one tooth.{/n} "Those are two different debts. I am speaking to the thief."'
    nodes['want']['Text'] = ('"I am not taking her from the silver." {n}She looks at the north road.{/n} '
        '"If my child comes to me, she comes on her own wings. I will not burn her keeper to fetch her. '
        'You, however, took a life from my clutch. You owe one. Tomorrow, when you are old, or at the edge of the world: '
        'I will name it. Do not send the silver to argue for you."')
    nodes['named']['Text'] = '"Good." {n}She settles her chin on the sill.{/n} "The child stays with her keeper. The bill stays with you. Go down."'
    for answer in nodes['start']['Choices']:
        _add(answer, 'Set', EGG_BILL)

    book = _nodes(_scene(scenes, T + 'the_garrison_book'))
    _add(book['tell_her']['Choices'][0], 'Set', REPORTED)
    _add(book['tell_her']['Choices'][1], 'Set', UNREPORTED)
    _add(book['tell']['Choices'][0], 'Set', BOOK_CLOSED)
    roof = _scene(scenes, T + 'on_the_roof')
    nodes = _nodes(roof)
    nodes['her']['Text'] = ('"They are staring again." {n}Her tail dislodges three tiles.{/n} '
        '"I have not eaten anyone tonight. Tell them that. Tell them it is very difficult."')
    _fork(roof, 'roof', 0, 'her_closed',
        '"The book is closed, and still they stare." {n}She shifts along the tiles.{/n} '
        '"The old man told me what my flight cost them. Tonight costs them sleep. I came for your window, crusader. Not their purse."', requires=(BOOK_CLOSED,))
    # Neutral legacy fallback and an independent first response for the unreported wager.
    _fork(roof, 'roof', 0, 'her_unreported',
        '"A hundred to one. I heard them shouting it when I landed." {n}Her eye finds yours.{/n} '
        '"You kept their little book from me. Keep it. I came to look through your window. '
        'Now they can look up at mine."', requires=(UNREPORTED,))

    farewell = _scene(scenes, T + 'before_the_end')
    _add(farewell, 'Requires', 'coronation.seen')
    farewell['DelayHours'] = 0
    _nodes(farewell)['climb']['Text'] = ('"They are preparing the march." {n}Her eye stays on the city.{/n} '
        '"To the place where the Wound goes all the way down. You came to me before the road takes you. Good."')

    from storylines.devarra_round3 import tower
    tower(scenes)


def polish_epilogue(page):
    """Current fate/location, counted return, and the existing hoard counter-gift."""
    for paragraph in page.get('Paragraphs', []):
        req = paragraph.get('Requires', [])
        if T + 'vault_opened' in req and not set(TERMINAL).intersection(req):
            _add(paragraph, 'Forbids', 'eggs.druids')
        if T + 'vault_opened' in req and 'eggs.destroyed' in req:
            _add(paragraph, 'Forbids', 'eggs.druids')
        if EGG_BILL in req and 'grew up in a lime-kiln' in paragraph['Text']:
            paragraph['Text'] = ('{n}The silver kept the smallest of Devarra\'s clutch by the east wall. '
                'When the child could fly she came up the ridge on her own wings. Devarra counted her, '
                'then made room on the sill. The thief\'s bill was a separate matter.{/n}')
            _add(paragraph, 'Requires', HATCHED)
            _add(paragraph, 'Forbids', NORTH)
        if T + 'on_the_roof' in req:
            _add(paragraph, 'Forbids', REPORTED, UNREPORTED)
        if T + 'coin_asked' in req:
            paragraph['Text'] = ('{n}Devarra finally chose her counter-gift: the account of a battle '
                'the Commander had already told her, this time with every name left in. The Commander told it '
                'again on the ridge. She interrupted at each death. The gold coin remained unspent; she '
                'counted it whenever the Commander climbed.{/n}')
    # Slot brief: established annual return; no first-night replay or payment flags.
    page.setdefault('Paragraphs', []).extend([
        dict(p('{n}On a later visit the Commander climbed after the watch bells rang. Devarra lay on the unlit side of the tower, away from the brush fire. The Commander set down the armor and knelt beneath her raised wing, a hand against her warm scales.{/n} "You kept me waiting." {n}Her tail drew the visitor against her belly; the hand moved under her wing, over the seam where the old blow had gone in, and she shuddered the whole length of her. The Commander undressed in the glow of her breath while she watched, her eye a coal, and her claws ground slowly at the stone. "Mine," she said. "Late, and still mine. I have not finished you." The tail wound up the Commander's thigh and held, and the scales ran hot and ridged beneath bare palms as the wing came down and drew them in beneath her.{/n}',
               requires=(T + 'first_bite',)), Id=P + 'epilogue.woken.explicit.1'),
        p('{n}After she had lain among them in the vault, the eggs were carried east to the druids. '
          'The vault stood empty. On that night in later years she looked east from her ridge; the '
          'Commander climbed there to meet her.{/n}', requires=(T + 'vault_opened', 'eggs.druids'), forbids=('eggs.omelet',)),
        p('{n}The silver carried the child north. That was where she grew, beyond Drezen\'s smoke. '
          'Years later she flew south to the grey ridge herself. Devarra watched her land, '
          'counted once, and demanded her story.{/n}', requires=(EGG_BILL, NORTH)),
        p('{n}The smallest shell remained in the silver\'s keeping by the east wall. Devarra never '
          'called the thief\'s bill a price paid for custody.{/n}', requires=(EGG_BILL,), forbids=(NORTH, HATCHED)),
        p('{n}The book closed after Devarra\'s first low flight over the wall. Later she returned to '
          'the citadel roof for the Commander\'s view. The sentries learned to leave that window clear.{/n}',
          requires=(T + 'on_the_roof', REPORTED)),
        p('{n}Her unannounced landing settled the soldiers\' wager. She returned to the roof anyway. '
          'When they shouted odds she asked the Commander to tell her what they were shouting about.{/n}',
          requires=(T + 'on_the_roof', UNREPORTED), forbids=(REPORTED,)),
    ])
