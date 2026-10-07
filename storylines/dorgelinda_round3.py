"""Authored disclosure repair: her judgment, named people, and later additions.

No new romance price or reconciliation. The compact graph appends to the old
graph, whose indices remain save references. Routine names are supplied in
groups of four; exact history variants record only the people actually named.
"""
from itertools import product

from story_format import c, n

L = 'dorgelinda.ledger.'

# These are the Commander's explanations, not facts Dorgelinda divines. They
# identify the exceptional claim without inventing a visit or a native outcome.
EXPLANATIONS = {
    'areelu': '"Areelu Vorlesh. The woman who opened the Worldwound. We are lovers."',
    'minagho_chivarro': '"Minagho and Chivarro. Both demons, and together. I am with both of them."',
    'hepzamirah': '"Hepzamirah, Baphomet\'s daughter. She is my lover."',
    'devarra': '"Devarra, the dragon. This is more than a bargain between us."',
    'melazmera': '"Melazmera, the umbral dragon of Colyphyr. She is my lover."',
    'iomedae': '"Iomedae herself. I mean her, Quartermaster, not a priestess."',
}
REACTIONS = {
    'areelu': '"Vorlesh?" {n}Her good hand closes on the cup, hard.{/n} "I\'ve packed kit for lads who never came back from that wound. Don\'t ask me to drink to her. No experiments on my soldiers. No touchin\' their stores. You want me as well? You come to my door yourself. She stays outside it."',
    'minagho_chivarro': '"Two demons. Aye, I heard both names." {n}She moves the cup away from the notebook.{/n} "No huntin\' among my drivers. No one followin\' you through my door because she wants what the other one\'s got. What you three do elsewhere is yours. This room stays mine."',
    'hepzamirah': '"Baphomet\'s daughter. Hammer and tongs." {n}She stares at you.{/n} "My wounded aren\'t prey. My lads aren\'t hers to order about. I\'ll have you here, Commander, without her guards at my door. Don\'t bring her quarrels into my yard."',
    'devarra': '"A dragon, and you want me to believe she wants you back?" {n}She studies your face, then exhales.{/n} "Aye. You mean it. No landin\' on my stores, no cattle from the ration train. I\'ll not send a carter up a mountain to fetch you for supper. You get here yourself."',
    'melazmera': '"The dragon from Colyphyr." {n}Her jaw sets.{/n} "Keep her teeth away from my supply road. No driver pays for your nights with her. I\'ll still have you at my table, if you can get here without bringin\' her appetite through the gate."',
    'iomedae': '"Herself?" {n}She searches your face for the joke. Her fingers brush the battered cup.{/n} "I\'ve heard soldiers pray to her with their guts in their hands. You\'d better mean that name. No priest comes tellin\' me what she wants of my bed. If you still want mine, you ask me."',
    'tirabade': '"Anevia and Irabeth. Both of \'em." {n}She nods once.{/n} "They\'ve enough to do keepin\' Drezen standin\'. Don\'t send either of \'em here to settle what you promised the other. Our nights stay ours."',
    'nocticula': '"A demon lord. Hammer and tongs." {n}Her jaw tightens.{/n} "No presents in my stores. No favours called in through you. I\'ll not have my lads bought along with you."',
    'shamira': '"The demon from Alushinyrra? No key to my door. No one from her court leanin\' on my clerks."',
    'jerribeth': '"A demon with a taste for soldiers. Keep her out of my ranks and out of my rooms. I mean it, Commander."',
    'galfrey': '"Royal company." {n}She snorts.{/n} "I answer for the army\'s stores. My bed isn\'t an appointment she hands out."',
    'anevia': '"She\'ll know how to keep a private door private. Tell her this one\'s mine."',
    'irabeth': '"I\'ll not have her put in the middle of a lie. What you promise her, you keep. Same as what you promise me."',
    'seelah': '"The paladin? She can buy her own drink. That bottle behind the returns is for us."',
    'konomi': '"I\'ll hear no advice from her about a suitable match. She can keep that for the council."',
    'kiana': '"Tell her I\'m not askin\' for a part in it. I want you here when you say you\'ll be here."',
    'soana': '"You can go to her. Don\'t promise her your whole life and leave me to find out over supper."',
    'arsinoe': '"No temple business through my private door. She can use the office like everyone else."',
    'targona': '"Aye. She\'ll not need to stand watch over us. I can bolt my own door."',
    'gesmerha': '"Then keep time for her. I\'ll not spend our evening hearin\' you make excuses for missin\' hers."',
    'vellexia': '"Keep her entertainments away from my lads. They\'re soldiers, not a diversion."',
    'aranka': '"No song about my rooms. The sentries have enough to grin about already."',
    'nurah': '"Nurah?" {n}She eyes you sharply.{/n} "No errands in my stores on your say-so. I\'ll check every issue myself."',
    'camellia': '"She can turn her nose up at my dented cup. You\'re the one drinkin\' from it."',
    'eritrice': '"Aye. But I\'ll not dress up for anyone else\'s approval when I\'m off duty."',
    'chadali': '"Then leave enough of the evening for me. I\'m not lettin\' supper burn while you finish another visit."',
    'arueshalae': '"I\'ll judge what she does around my lads. Not what you hope she\'ll do. My rooms stay private."',
    'delamere': '"No huntin\' in my yard. If she wants you out with her, settle the time before you come here."',
    'kaylessa': '"No sentry gets her name from me. You can tell her that much."',
    'mielarah': '"Then arrange your visits. I\'m not sendin\' a supply wagon after you."',
    'nidalynn': '"I want the truth from you. No borrowed tale to keep me sweet."',
    'jannah': '"Aye. Your evenin\'s your own till you promise it to me. Then I expect you."',
    'nenio': '"No experiments in my rooms. I\'ve enough trouble keepin\' the stores dry."',
    'herrax': '"Whatever she charges elsewhere, my cup isn\'t for sale."',
    'terendelev': '"I\'ll not compete with a dragon by shoutin\' louder. You know where my door is."',
    'eliandra': '"She can have her time with you. My supper stays between us."',
    'horzalah': '"No drill in my private rooms. I get enough orders shouted across the yard."',
    'elyanka': '"Don\'t bring anyone else\'s demands to my table. Tell me what you want yourself."',
    'yaniel': '"Then don\'t give either of us a promise you can\'t keep. I\'ve heard enough of those from officers."',
    'wenduag': '"No scrappin\' over you in my stores. I\'ll throw the lot of you out till the issue\'s finished."',
}
FOLLOW_REACTIONS = {
    'areelu': '"Vorlesh, now?" {n}She shoves the returns aside.{/n} "You\'re tellin\' me before she comes near my soldiers. Good. Keep her away from them. I\'ll still have you here, but I\'ll not find her waitin\' behind my door."',
    'minagho_chivarro': '"Both of \'em, then. Not one name with the other left out." {n}She leans forward.{/n} "I\'ll have no demon followin\' you into my rooms to fight over you. Nor into the drivers\' quarters lookin\' for amusement. Our arrangement stays here."',
    'hepzamirah': '"So now there\'s Baphomet\'s daughter." {n}Her mouth tightens.{/n} "No guards in my yard. No frightened carters carryin\' gifts for her. You come alone when I ask for you. I\'m not givin\' her my supper as well."',
    'devarra': '"You\'ve added a dragon?" {n}She gives a short, incredulous bark.{/n} "I\'ll not stretch our ration train to feed her. Nor spend our night waitin\' while you climb down from her mountain. Keep our time, and we\'ll keep it as we agreed."',
    'melazmera': '"Colyphyr\'s dragon. Aye, that changes things." {n}She fixes you with her good eye.{/n} "Not my supply road. Not one of my lads in her teeth. You can still come here. Leave her hunger where you found it."',
    'iomedae': '"Iomedae. You\'re serious." {n}She takes a breath before continuing.{/n} "I\'ll still pray for the lads. Don\'t mix that up with givin\' her a say in my rooms. No priest explains your absence for you. You tell me yourself."',
    'tirabade': '"Both wives, together. I heard that." {n}She nods.{/n} "No need to tell me their names twice. Keep what you\'ve promised them. What you promised me stays between us."',
    'nocticula': '"A demon lord on top of the rest?" {n}She pulls the stores keys closer.{/n} "She gets none of these. Not even if she calls it a favour to you. Our nights stay ours."',
    'shamira': '"Then tell her she\'ll find no court here. I\'ll have you, without her people hangin\' round my clerks."',
    'jerribeth': '"That one stays away from the ranks. I\'m not losin\' a lad because you found another bed."',
    'galfrey': '"Her Majesty as well. Aye." {n}She looks at the door.{/n} "No royal summons interrupts us behind that door. Settle your business before you come."',
    'anevia': '"Anevia too. Tell her I heard it from you. She needn\'t pry it out of a sentry."',
    'irabeth': '"Then be straight with Irabeth. I\'m not coverin\' a lie between you."',
    'seelah': '"Seelah too? Keep her out of my private bottle. I\'m not pourin\' for the whole barracks."',
    'konomi': '"Then she can leave our evenings off the council agenda. I\'m not takin\' advice on you."',
    'kiana': '"Kiana. Aye. Save your explanations for her if you miss her evenin\'. Don\'t rehearse them on me."',
    'soana': '"Then make room for her without handin\' away the nights you promised me."',
    'arsinoe': '"Arsinoe as well. The office stays open for temple issues. My inner door doesn\'t."',
    'targona': '"Aye. No extra watch at my door. I\'m off duty when you\'re in there."',
    'gesmerha': '"Good that you told me. Don\'t let her hear a different promise from yours."',
    'vellexia': '"Vellexia now. My drivers aren\'t somethin\' to bring her when she gets bored."',
    'aranka': '"Aranka. Keep our evenin\' out of the chorus, Commander."',
    'nurah': '"Nurah too? No errands on your seal. I check her issues. That hasn\'t changed."',
    'camellia': '"Camellia. Then she can have her fine cups. You\'re keepin\' the dented one here."',
    'eritrice': '"Aye. I\'ll not have her judge how I keep my rooms."',
    'chadali': '"Then sort your visits before supper. I\'m eatin\' while it\'s hot."',
    'arueshalae': '"Arueshalae too. I\'ll watch what she does around the lads. I\'m not takin\' your affection as proof."',
    'delamere': '"Delamere. No hunt through the yard. The boys have enough arrows to worry about."',
    'kaylessa': '"Kaylessa. I heard you. The sentries won\'t hear it from me."',
    'mielarah': '"Aye. Get back on your own feet. I\'m keepin\' the wagons for supplies."',
    'nidalynn': '"Nidalynn now. Keep tellin\' it plain. I\'ve no time to pick apart a tale."',
    'jannah': '"Then she gets her time, and I get mine. Sort it before you promise."',
    'nenio': '"Nenio too. You\'d better tell her my rooms aren\'t for tryin\' things out."',
    'herrax': '"Herrax. Aye. Don\'t come to me with a price for our night."',
    'terendelev': '"Another dragon. Hammer and tongs. I\'m still expectin\' you through the ordinary door."',
    'eliandra': '"Eliandra too. Then leave our supper between us. No reports afterward."',
    'horzalah': '"Horzalah. Aye. No orders in my rooms. Not hers, not yours."',
    'elyanka': '"I heard you. Her demands stay with her. You speak for yourself here."',
    'yaniel': '"Yaniel. Keep your word with her. I expect mine kept too."',
    'wenduag': '"Wenduag now. If there\'s a scrap over you, it happens outside my stores."',
}


def integrate(payload):
    from storylines.household import PARTNERS
    by = {s['Id']: s for s in payload['Scenes']}
    original = by[L + 'other_columns']
    follow = by[L + 'changed_columns']
    partners = [r for r in PARTNERS if r not in ('dorgelinda', 'ember', 'aivu')]
    assert set(partners) == set(REACTIONS), set(partners) ^ set(REACTIONS)
    derived = payload.setdefault('Derived', {})
    forbids = payload.setdefault('DerivedForbids', {})
    keys = {}
    for rel in partners:
        key = L + 'undisclosed.' + rel
        keys[rel] = key
        derived[key] = [[L + 'current_other.' + rel]]
        forbids[key] = [L + 'disclosed.' + rel]
        if rel in ('anevia', 'irabeth'):
            forbids[key].extend((L + 'current_other.tirabade', L + 'disclosed.tirabade'))
    # The existing count predicate expresses "at least one new name" directly;
    # it has the same truth table as an OR over the live undisclosed readers.
    payload.setdefault('Counts', {})[L + 'new_columns'] = dict(Of=list(keys.values()), Min=1)

    def receipts(rel):
        return [L + 'disclosed.' + rel] + ([L + 'disclosed.anevia', L + 'disclosed.irabeth'] if rel == 'tirabade' else [])

    # Retire duplicate index 3; keep the honest solo answer at saved index 4.
    next(n for n in original['Nodes'] if n['Id'] == 'says')['Choices'][3]['Forbids'].append('trickster.ever')
    important = list(EXPLANATIONS) + ['tirabade', 'nocticula', 'shamira', 'jerribeth', 'galfrey', 'nurah', 'arueshalae']
    routine = [r for r in partners if r not in important]

    for event, changed in ((original, False), (follow, True)):
        nodes = {n['Id']: n for n in event['Nodes']}
        for rel in partners:
            reply = nodes['named.' + rel]
            reply['Text'] = (FOLLOW_REACTIONS if changed else REACTIONS)[rel]
            # The saved graph keeps its original answer effects. Receipts are
            # written by the appended path used in new histories.
            for answer in nodes['names.0']['Choices']:
                if answer.get('Next') == 'named.' + rel and rel in EXPLANATIONS:
                    answer['Text'] = EXPLANATIONS[rel]
        for node in event['Nodes']:
            if node['Id'] == 'names.0' or node['Id'].startswith('named.'):
                for answer in node['Choices']:
                    for field in ('Requires', 'Forbids'):
                        answer[field] = [f.replace(L + 'current_other.', L + 'undisclosed.') for f in answer[field]]
        # Append a compact path; do not delete or reorder the saved graph.
        old = nodes['named']['Choices'][0]
        old['Forbids'].append('trickster.ever')
        nodes['named']['Choices'].append(c('[Tell her what has changed.]' if changed else '[Tell her the names and arrangements.]', 'disclosure.0'))
        steps = [('special', r) for r in important] + [('batch', routine[i:i + 4]) for i in range(0, len(routine), 4)]
        for index, (kind, group) in enumerate(steps):
            nid, nxt = 'disclosure.' + str(index), 'disclosure.' + str(index + 1)
            if kind == 'special':
                rel = group
                # Skip absent and already disclosed lovers together, without a
                # visible empty checklist node: dispatch at the previous reply.
                event['Nodes'].append(n(nid, 'Narrator', '{n}Dorgelinda waits for the rest.{/n}',
                    c(EXPLANATIONS.get(rel, '[Explain your relationship with ' + PARTNERS[rel][1] + '.]'), 'disclosure.reply.' + rel, requires=(keys[rel],)),
                    c('Continue', nxt, forbids=(keys[rel],))))
                words = (FOLLOW_REACTIONS if changed else REACTIONS)[rel]
                event['Nodes'].append(n('disclosure.reply.' + rel, 'Dorgelinda', words,
                    c('[Go on.]', nxt, flags=receipts(rel))))
            else:
                choices = []
                for bits in product((False, True), repeat=len(group)):
                    present = [r for r, bit in zip(group, bits) if bit]
                    absent = [r for r, bit in zip(group, bits) if not bit]
                    text = '[Name ' + ', '.join(PARTNERS[r][1] for r in present) + ' and explain the arrangements.]' if present else 'Continue'
                    choices.append(c(text, nxt, flags=tuple(f for r in present for f in receipts(r)),
                        requires=tuple(keys[r] for r in present), forbids=tuple(keys[r] for r in absent)))
                event['Nodes'].append(n(nid, 'Dorgelinda', '"Who else?"' if not changed else '"Anyone else I haven\'t heard about?"', *choices))
        event['Nodes'].append(n('disclosure.' + str(len(steps)), 'Dorgelinda',
            '"Right. I\'ve heard you. My rooms stay mine. You come here yourself, and nobody draws stores on your seal behind my back." {n}She holds out her good hand.{/n}',
            c('[Take her hand.]', 'shaken')))
        # Keep empty dispatches out of the playable graph by expanding skip
        # gates; only consequential replies and occupied batches need a click.
        compact(event, steps, keys, changed, payload)

    follow['Requires'] = ['trickster.ever', 'dorgelinda.present_now', 'dorgelinda.committed', L + 'new_columns']
    follow['RequiresAnyGroups'] = [[L + 'sole_line', L + 'terms_kept']]
    follow['Nodes'][0]['Text'] = '"Tell me what changed." {n}She sets the stores returns aside.{/n} "I heard you the first time. I want the new names."'
    # New disclosures do not apologize for the unresolved seal quarrel.
    for event in (original, follow):
        end = next(node for node in event['Nodes'] if node['Id'] == 'disclosure.' + str(len(steps)))
        end['Choices'][0]['Forbids'] = [L + 'quarrel_cold', L + 'quarrel_unmended']
        end['Choices'].extend((
            c('[Leave the arrangement as agreed.]', 'disclosure.cold', requires=(L + 'quarrel_unmended',)),
            c('[Leave the arrangement as agreed.]', 'disclosure.cold', requires=(L + 'quarrel_cold',), forbids=(L + 'quarrel_mended', L + 'quarrel_unmended')),
            c('[Take her hand.]', 'shaken', requires=(L + 'quarrel_cold', L + 'quarrel_mended'), forbids=(L + 'quarrel_unmended',)),
        ))
        event['Nodes'].append(n('disclosure.cold', 'Dorgelinda',
            '"I heard you. Doesn\'t settle what happened with my seal." {n}She takes up the stores returns again.{/n}',
            c('[Leave her to the returns.]', flags=(L + 'terms_kept',))))
    # Completion is globally one-shot. Retire the old terminal choices by
    # gating, retaining their indices/effects/targets. Appended answers record
    # the disclosure without recording scene completion, so a new name can
    # reopen the conversation. Old development completion receipts stay intact.
    for node in follow['Nodes']:
        additions = []
        for answer in list(node['Choices']):
            if answer.get('Next') is None:
                additions.append(c(answer['Text'], flags=tuple(answer['Set']),
                    requires=tuple(answer['Requires']), forbids=tuple(answer['Forbids']), abort=True))
                answer['Forbids'].append('trickster.ever')
        node['Choices'].extend(additions)


def compact(event, steps, keys, changed, payload):
    """Jump directly to the next occupied step with mutually exclusive gates."""
    nodes = {n['Id']: n for n in event['Nodes']}
    end = 'disclosure.' + str(len(steps))
    derived, forbids = payload['Derived'], payload['DerivedForbids']

    def dispatch(label, present, absent):
        # Factor a snapshot predicate rather than carrying dozens of stale
        # negative assumptions through every receipt-writing answer. Native
        # entitlement remains a separate positive guard on the actual answer.
        key = L + 'disclosure_dispatch.' + label
        derived[key] = [[keys[r] for r in present]] if present else [['trickster.ever']]
        if absent:
            forbids[key] = list(absent)
        else:
            forbids.pop(key, None)
        ready = key + '.ready'
        payload.setdefault('Counts', {})[ready] = dict(Of=[key], Min=1)
        return (ready, *(L + 'current_other.' + r for r in present))

    prefix = []
    predicates = {}
    for i, (kind, group) in enumerate(steps):
        if kind == 'special':
            predicates[(i, (group,))] = dispatch(group, [group], prefix)
            prefix.append(keys[group])
        else:
            for bits in product((False, True), repeat=len(group)):
                present = tuple(r for r, bit in zip(group, bits) if bit)
                if present:
                    absent = [keys[r] for r, bit in zip(group, bits) if not bit]
                    predicates[(i, present)] = dispatch('batch.' + str(i) + '.' + ''.join('1' if bit else '0' for bit in bits), present, prefix + absent)
            prefix.extend(keys[r] for r in group)
    done = dispatch('done', [], prefix)

    def next_choices(start):
        result = []
        for i in range(start, len(steps)):
            kind, group = steps[i]
            if kind == 'special':
                result.append(c(EXPLANATIONS.get(group, '[Explain your relationship with ' + person(group) + '.]'),
                    'disclosure.reply.' + group, requires=predicates[(i, (group,))]))
            else:
                for bits in product((False, True), repeat=len(group)):
                    present = [r for r, bit in zip(group, bits) if bit]
                    if not present:
                        continue
                    receipt = [L + 'disclosed.' + r for r in present]
                    # A batch has its own response, rather than jumping over
                    # her acknowledgment to the next demand for names.
                    result.append(c('[Name ' + ', '.join(person(r) for r in present) + ' and explain the arrangements.]',
                        'disclosure.batch.' + str(i), flags=tuple(receipt),
                        requires=predicates[(i, tuple(present))]))
        result.append(c('[Hear her answer.]', end, requires=done))
        return result

    nodes['named']['Choices'][-1]['Next'] = 'disclosure.0'
    # Preserve appended dispatcher nodes as well; suspended saves can advance.
    for i, (kind, group) in enumerate(steps):
        nodes['disclosure.' + str(i)]['Choices'] = next_choices(i)
        if kind == 'special':
            nodes['disclosure.reply.' + group]['Choices'] = next_choices(i + 1)
        else:
            event['Nodes'].append(n('disclosure.batch.' + str(i), 'Dorgelinda',
                ([
                    '"So those are the new names. Good. I\'ll not have to ask a sentry what changed."',
                    '"Aye. Our evenings still fit, then? Settle the time before you come here."',
                    '"More company. You\'ve told me yourself. Keep it that way."',
                    '"Right. No need to go through the old names again. I remember what we agreed."',
                    '"They can leave my door alone as well. That hasn\'t changed."',
                    '"That lot now? My supper hour\'s still the same, Commander."',
                    '"Heard you. The dented cup stays here."',
                ] if changed else [
                    '"Aye. I\'ve heard the names. Keep what you promised them. I\'ll have no one sent to my door to ask where you\'ve got to."',
                    '"Right. Make time for them, then. I want our evenings without you jumpin\' up at every footstep."',
                    '"You\'ve been busy." {n}She snorts.{/n} "No messengers through my rooms when we\'re together."',
                    '"Aye. They know what you\'ve promised? See that they do. I\'ll not deliver the news for you."',
                    '"I\'ll leave their doors alone. They can leave mine alone."',
                    '"That lot too? Hammer and tongs. I\'m keepin\' my own supper hour."',
                    '"Heard you. Nobody else uses my cup."',
                ])[sum(kind == 'batch' for kind, _ in steps[:i])],
                *next_choices(i + 1)))
    # Mark a special name when the Commander supplies it, before her response.
    for node in event['Nodes']:
        for answer in node['Choices']:
            target = answer.get('Next') or ''
            if target.startswith('disclosure.reply.'):
                rel = target[len('disclosure.reply.'):]
                answer['Set'] = list(dict.fromkeys(answer['Set'] + [L + 'disclosed.' + rel] +
                    ([L + 'disclosed.anevia', L + 'disclosed.irabeth'] if rel == 'tirabade' else [])))
    # Intermediate dispatchers were construction helpers, never shipped IDs.
    unused = {'disclosure.' + str(i) for i in range(1, len(steps))}
    event['Nodes'] = [node for node in event['Nodes'] if node['Id'] not in unused]


def person(rel):
    from storylines.household import PARTNERS
    return PARTNERS[rel][1]
