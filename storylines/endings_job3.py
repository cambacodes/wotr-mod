"""Authored job 3 continuity: selected late answers and partner aftermaths.

No epilogue answer writes campaign acceptance. Existing exits retain their
identity and mechanics; new pages carry only the outcome selected in this graph.
Native anchors: DesnaAdepts/Cue_0004-0005 (13cbf1a6/2c84efa6),
MarhevokTransformed/Cue_0001 (410114ed), SoanaAfterQuest/Cue_0012
(c6789b66), Wenduag/AfterSex/Cue_0043 (2779fd33), checked in /wrath.
The paid letters and existing partner arrangements are authored additions.
"""
from copy import deepcopy

from story_format import c, n, p


def node(event, key):
    return next(x for x in event['Nodes'] if x['Id'] == key)


def require(block, *flags):
    block['Requires'] = list(dict.fromkeys([*block.get('Requires', []), *flags]))


def local_coda(page, text):
    page.setdefault('Paragraphs', []).append(p(text, requires=('lastcall.active',)))


def offer(event, opening, accepted, refused, friend=None):
    """Preserve the inert .continue exit; append the player\'s actual answers."""
    page = event['Nodes'][0]
    exit_answer = page['Choices'][0]
    assert exit_answer['Next'] is None and not exit_answer['Set']
    exit_answer.setdefault('Id', 'continue')
    page['Text'] = opening
    page['Choices'].extend((
        c(accepted[0], 'late_accepted'), c(refused[0], 'late_refused')))
    event['Nodes'].extend((
        n('late_accepted', 'Narrator', accepted[1], c('Continue', page['Id'] + '_exit')),
        n('late_refused', 'Narrator', refused[1], c('Continue', page['Id'] + '_exit')),
        n(page['Id'] + '_exit', 'Narrator', '{n}Her answer stood.{/n}', c()),
    ))
    if friend:
        page['Choices'].append(c(friend[0], 'late_friend'))
        event['Nodes'].append(n('late_friend', 'Narrator', friend[1], c('Continue', page['Id'] + '_exit')))


def late_endings(payload, scenes):
    # The commissioned work and its price do not buy Gesmerha\'s bed.
    for sid in ('gesmerha.trickster.epilogue.commit', 'gesmerha.trickster.epilogue.commit_mourned'):
        scenes[sid]['Requires'] = [f for f in scenes[sid]['Requires'] if f != 'gesmerha.payoff.partner']

    dragon = scenes['devarra.trickster.epilogue.commit']
    offer(dragon,
        '{n}One winter night after the Worldwound closed, Devarra landed on the roof hard enough to crack the tiles. She lowered her head into the yard.{/n}\n'
        '"The story will do. Now for my judgment. You, on my ridge, where I can smell you. My tariff stands: once a year, the arm I choose."\n'
        '{n}Her eye followed the Commander to the door.{/n} "Well? Bare it, or go inside."',
        ('"I will come. Take the arm, and keep a place for me."',
         '{n}The Commander bared an arm. Devarra closed her jaws carefully; blood ran between her teeth.{/n}\n'
         '"Spring. On my ridge. Do not make me fetch you."\n'
         '{n}The first visit lasted until dawn. The Commander returned with burns, a fresh crescent scar, and an appointment for the next spring.{/n}'),
        ('"Collect what the bargain owes you. My bed is no part of it."',
         '{n}Devarra showed the whole length of her teeth.{/n} "Then keep it. You still owe what you promised. I shall enjoy collecting."\n'
         '{n}She left the tiles broken. The account remained; no place beside her had been accepted.{/n}'))
    local_coda(node(dragon, 'late_accepted'),
        '{n}After the last night of the war, Devarra had waited for the Commander to answer her judgment. The bared arm gave her that answer. She counted the later spring visits by the crescents she left in it.{/n}')
    local_coda(node(dragon, 'late_refused'),
        '{n}The call at Threshold had bought no lover. Devarra kept the account under the terms already bargained; the Commander had refused her later invitation.{/n}')

    demon = scenes['hepzamirah.trickster.epilogue.commit']
    offer(demon,
        '{n}After Threshold, Hepzamirah returned with her pack. She dropped it at the Commander\'s door.{/n}\n'
        '"My guards, no priest, and my quarry stays mine. A room, clown? Or your bed? Say which. I have no use for a host who trembles whenever I take what was offered."',
        ('"My bed. Come here, Hepzamirah."',
         '{n}She kicked the pack inside and caught the Commander by the collar. Her kiss tasted of wine; her tusk grazed the lip beneath it.{/n}\n'
         '"Good. Keep those hands busy. My father can wait until morning."\n'
         '{n}She shoved the door shut behind them. At dawn her guards were waiting outside it; she ordered them away and pulled the Commander back by the belt.{/n}'),
        ('"Find another roof."',
         '{n}Hepzamirah lifted the pack.{/n} "Keep your little fortress, then. I have broken better doors."\n'
         '{n}She left with her guards. No invitation followed her.{/n}'),
        ('"A guest room. That is all I offer."',
         '{n}She looked the Commander over, then snorted.{/n} "A roof, then. My guards stay. Try a priest at my door and you will have to buy another door."\n'
         '{n}She took the guest room and kept her own bed. Their bargain had supplied shelter.{/n}'))
    for key, text in (
        ('late_accepted', '{n}Threshold had left her alive in Mutasafen\'s body. It had not chosen her lover. Hepzamirah made that choice at the door, and came back to the bed she had claimed, still intent on killing her father.{/n}'),
        ('late_refused', '{n}The accounts carried out of Threshold remained accounts. Hepzamirah had left the refused doorway with her guards; no shared bed was entered against them.{/n}'),
        ('late_friend', '{n}After Threshold her guards occupied the passage outside the guest room. Hepzamirah owed no lover\'s company for its roof, and offered none.{/n}')):
        local_coda(node(demon, key), text)

    # Existing Nocticula/Chadali choices already express the player\'s answer.
    queen = scenes['nocticula.trickster.epilogue.commit']
    for key in ('after_paid', 'after_refused'):
        local_coda(node(queen, key),
            '{n}The last call of the war had left an answer between them. Nocticula received it in her own chair, after the Commander crossed the room. She kept that place beside her occupied on the evenings she chose; the Commander had finally taken it.{/n}')
    local_coda(node(queen, 'refused_page'),
            '{n}The war ended at Threshold; the Commander later stepped away from her chair. Nocticula remembered the refusal. Her accounts survived it; the place beside her stayed empty.{/n}')
    local_coda(node(queen, 'inn'),
        '{n}The Queen\'s unsigned breakfast note followed the Commander back to the inn. Threshold had left them business; leaving her room had promised her no nights.{/n}')
    luck = scenes['chadali.trickster.epilogue.commit']
    local_coda(node(luck, 'stay'),
        '{n}Whatever was owed at Threshold remained its own account. The night after Chadali brought the orange was their own answer. She returned before supper as she had promised, and kept coming.{/n}')
    for key in ('half', 'coin', 'penny', 'friend'):
        local_coda(node(luck, key),
            '{n}Threshold had settled no question about Chadali\'s bed. She kept the visit the Commander had chosen and left the larger question unanswered.{/n}' if key != 'friend' else
            '{n}When the last call of the war was over, the Commander made room for Chadali as a friend. She brought her news and cookies there; the invitation had asked for nothing else.{/n}')


def eliandra(payload, scenes):
    from storylines.eliandra_trickster import EPILOGUE_PARAGRAPHS
    friendship = 'eliandra.trickster.friendship_chosen'
    # The explicit campaign friendship answer is history. Only the existing
    # later romantic write-back/commit can supersede it.
    for event in payload['Scenes']:
        if not event['Id'].startswith('eliandra.') or event['Owner'].endswith('Epilogue'):
            continue
        for page in event['Nodes']:
            for answer in page['Choices']:
                if answer.get('Next') == 'friend':
                    answer['Set'] = list(dict.fromkeys([*answer['Set'], friendship]))
    payload['Derived']['eliandra.trickster.friendship_current'] = [['trickster.ever', friendship]]
    payload.setdefault('DerivedForbids', {})['eliandra.trickster.friendship_current'] = ['eliandra.committed']
    unasked = scenes['eliandra.trickster.epilogue.unasked']
    unasked['Forbids'].extend(('eliandra.trickster.friendship_current', 'eliandra.trickster.letter_kept'))
    released = scenes['eliandra.trickster.epilogue.released']
    released.setdefault('ForbidOverrides', {})['eliandra.trickster.flirted'] = 'eliandra.trickster.friendship_current'
    released['Forbids'].append('eliandra.trickster.letter_kept')
    for kind in ('late', 'unasked'):
        event = scenes['eliandra.trickster.epilogue.' + kind]
        page = event['Nodes'][0]
        old_paragraphs = deepcopy(page.get('Paragraphs', []))
        romance = old_paragraphs[len(EPILOGUE_PARAGRAPHS):]
        # Historical costs stay on the offer; the journey and night follow yes.
        page['Paragraphs'] = old_paragraphs[:len(old_paragraphs) - len(romance)]
        for block in page['Paragraphs']:
            block['Text'] = block['Text'].replace('because she had chosen a lover', 'because the war had ended')
        offer(event,
            '{n}After Threshold, Eliandra\'s letter from the Sarkorian fords reached the Commander. Her question remained: Drezen, or the road? The stargazers would need an answer before they packed the carts.{/n}' if kind == 'late' else
            '{n}After Threshold, Eliandra reached the Commander\'s door in Drezen, her travelling pack still on her shoulder.{/n}\n"Drezen, or the road? I have wanted to ask you since the basin. Now there is time to hear you."',
            ('"Either. Both. Bring them all. As my lover, Eliandra."',
             '{n}Eliandra set down her pack.{/n} "Both, then. I shall make you say it again tomorrow."\n'
             '{n}When her people had beds for the night, she returned and took the Commander\'s hand. Her travelling cloak fell across the unused chair; she kissed them and drew them past it.{/n}'),
            ('"Take your people north. I have no place for you here."',
             '{n}She shouldered the pack.{/n} "Then I have my answer. They are waiting for me."\n'
             '{n}She took the column north. Her temples opened their doors in Sarkoris; her letters to Drezen concerned the wounded and supplies.{/n}'),
            ('"Come as my friend. I will help your people."',
             '{n}She unrolled the road map on the table.{/n} "A friend, then. Start with this ford. The carts cannot cross it without help."\n'
             '{n}She kept a room with her people, and brought the Commander their news whenever the road led back to Drezen.{/n}'))
        # Keep the previously allocated intimate paragraph identity.
        node(event, 'late_accepted')['Paragraphs'] = romance
        if kind == 'late':
            node(event, 'late_accepted')['Text'] = '{n}The Commander sent the answer to the fords. Eliandra replied before the next convoy left; a month later she reached Drezen with her people and put her pack in the Commander\'s rooms.{/n}\n"Both. I have brought them all. Tonight I want you."'
        for key, text in (
            ('late_accepted', '{n}The war ended before they had answered each other. Afterwards Eliandra kept the road to Sarkoris and the place she had now accepted beside the Commander.{/n}'),
            ('late_refused', '{n}Eliandra remembered the help given her people before Threshold. It bought no place in the Commander\'s rooms after her invitation was refused.{/n}'),
            ('late_friend', '{n}When the last call of the war was over, Eliandra and the Commander remained friends. She still took her people north; their help on the road asked for no shared bed.{/n}')):
            local_coda(node(event, key), text)


def soana(scenes):
    from storylines import soana_partner as partner
    home = 'soana.partner.homecoming_kept'
    reply = 'soana.round2.family_reply'
    for event in scenes.values():
        if event['Id'].startswith('soana.partner.homecoming'):
            for page in event['Nodes']:
                for answer in page['Choices']:
                    if set(answer['Set']) & {partner.TOGETHER, partner.SEPARATED, partner.QUIET_RETURN}:
                        answer['Set'] = list(dict.fromkeys([*answer['Set'], home]))
        if not event['Id'].startswith('soana.') or not event['Owner'].endswith('Epilogue'):
            continue
        for page in event['Nodes']:
            # Existing descriptions of house-bound lovers cannot follow the
            # deliberately concealed return. Her current-love guard stays intact.
            if 'Boots and a travel bundle took their place' in page['Text']:
                base = page['Text']
                page['Text'] = '{n}After the war Soana kept watch over Wintersun. The path to her fire remained open to the Commander.{/n}'
                page.setdefault('Paragraphs', []).append(p(base, forbids=(partner.QUIET_RETURN,)))
            if 'She did keep the second blanket on the pallet' in page['Text']:
                page['Text'] = page['Text'].replace('She did keep the second blanket on the pallet, and she never once put it back on the shelf.', 'She kept the visits they had agreed to.')
            for block in list(page.get('Paragraphs', [])):
                if 'words Soana sent south gave family news' in block['Text']:
                    block['Text'] = '{n}The visits had been an affair, hidden behind a shaman\'s counsel. Soana had kept Corven\'s name; the secret visits alone had sent him no news.{/n}'
                    block['Forbids'].append(partner.QUIET_RETURN)
                if partner.EXCLUSIVE in block.get('Requires', []) and partner.CHOSEN in block.get('Requires', []) and 'sent her separation south' in block['Text']:
                    require(block, partner.PURSUED)
                    page['Paragraphs'].append(p(
                        '{n}Soana had taken off Corven\'s clasp and written her separation. No scout had carried it south. Her family had heard no word of that choice.{/n}',
                        requires=(partner.EXCLUSIVE, partner.CHOSEN), forbids=(partner.PURSUED,)))
                if partner.QUIET_RETURN in block.get('Requires', []) and event['Id'] in partner.LOSS_ENDINGS:
                    block['Text'] = '{n}Corven had come home without learning of the affair. When Soana died, he took her clasp south and told their children himself. The Commander\'s hidden meetings with her were over.{/n}'
                if partner.TOGETHER in block.get('Requires', []) and event['Id'] in partner.LOSS_ENDINGS:
                    block['Text'] = '{n}Corven had kept their marriage after hearing about the Commander. The news of his wife\'s death reached him in the south. He carried it to their children himself.{/n}'
                    block['Forbids'].append(home)
                    page['Paragraphs'].append(p('{n}Corven had been home when his wife died. He took the bark bearing his name south, with the news for their children.{/n}', requires=(partner.TOGETHER, home)))
                    break
            # Existing family tail supplies the quiet-homecoming history.
            # A bedroom scene gets an outdoor variant, including its morning.
            if event['Id'] in ('soana.trickster.epilogue.commit', 'soana.trickster.epilogue.luck_late', 'soana.trickster.epilogue.living_late') and (
                    page['Id'] == 'round2_morning' or '.explicit.' in page['Id']):
                original = page['Text']
                morning = page['Id'] == 'round2_morning'
                page['Text'] = ('{n}Dawn found them still together.{/n}' if morning else
                                '{n}Soana drew the Commander against her.{/n}')
                quiet = ('{n}Soana shook the leaves from her cloak and fastened the old clasp. She touched the bite on the Commander\'s neck, then pulled the collar over it.{/n}\n'
                         '"Let them ask about your bruises. Keep your fine lying tongue off my name."\n'
                         '{n}She went home alone. The Commander took the longer path; no bundle had been left beside Corven\'s bed.{/n}' if morning else
                         '{n}Her cloak lay on the dry bank. Soana caught the Commander\'s belt and pulled them down onto it; her kiss left teeth marks.{/n}\n'
                         '"Here, hunter. No light in the house. No soldiers listening for my name."\n'
                         '{n}She brought the Commander\'s hand beneath her loose shirt, held it there and kissed them again. The stream ran loud below them as she opened the belt.{/n}')
                page.setdefault('Paragraphs', []).extend((
                    p(original, forbids=(partner.QUIET_RETURN,)),
                    p(quiet, requires=(partner.QUIET_RETURN,)),
                ))
    coda = node(scenes['soana.lastcall.page'], 'page')
    original = coda['Text']
    coda['Text'] = '{n}After Threshold the Commander took the Wintersun path again. Soana still had her forest to watch.{/n}'
    coda.setdefault('Paragraphs', []).append(p(original, forbids=(partner.QUIET_RETURN,)))


def pair(scenes):
    page = node(scenes['minachiv.lastcall.page'], 'page')
    page['Text'] = '{n}After Threshold the Commander kept the signed agreement with the lease. Its clauses were read aloud again whenever the rent was due; the ink had survived the war.{/n}'
    # The route already supplied solo/shared stance paragraphs. Retire the
    # unqualified shared-house sentence using its original arrangement receipt.
    for block in page.get('Paragraphs', []):
        if 'Minagho and Chivarro both lived there' in block['Text']:
            require(block, 'minachiv.future_two')


def wenduag(payload, scenes):
    from storylines import wenduag_partner_stance as stance
    exception = 'wenduag.partner.vellexia_exception'
    for sid, event in scenes.items():
        if not sid.startswith('wenduag.'):
            continue
        if sid in ('wenduag.trickster.court.claim', 'wenduag.trickster.court.claim_in_person'):
            node(event, 'partner_exclusive_offer')['Text'] = node(event, 'partner_exclusive_offer')['Text'].replace(
                "I'll stop taking Lann to bed.", "No more lovers while I keep your claim. I'll stop taking Lann to bed. If I want someone else, you hear it before I touch them.")
        if sid.startswith('wenduag.trickster.court.vellexia'):
            choice = node(event, 'what')['Choices'][1]
            twin = deepcopy(choice)
            choice['Forbids'].append(stance.EXCLUSIVE)
            twin['Requires'].append(stance.EXCLUSIVE)
            twin['Next'] = 'exclusive_exception'
            node(event, 'what')['Choices'].append(twin)
            event['Nodes'].append(n('exclusive_exception', 'Wenduag',
                '{n}Wenduag turns away from the window.{/n} "All for yourself. That was your claim. Now you tell me to hunt her."\n'
                '{n}Her teeth show.{/n} "If she wants more than a fright, I want to find out. Say it now. Just her, or I leave her alone."',
                c('"Just Vellexia. I am letting you out of that promise for her."', 'hunt', flags=(exception,)),
                c('"Keep the promise. Leave her alone."', 'leave')))
        for page in event['Nodes']:
            for block in page.get('Paragraphs', []):
                if 'Wenduag answered her kiss and drew her closer' in block['Text']:
                    block.setdefault('AnyGroups', []).append(['wenduag.partner.no_exclusive_claim', exception])
                if 'Lann remained in the Commander' in block['Text'] and 'old nights' in block['Text']:
                    block['Text'] = '{n}Lann remained with the company. His nights with Wenduag in Neathholm belonged to their old life; serving beside her had promised no return to her bed.{/n}'
    payload['Derived']['wenduag.partner.no_exclusive_claim'] = [['trickster.ever']]
    payload.setdefault('DerivedForbids', {})['wenduag.partner.no_exclusive_claim'] = [stance.EXCLUSIVE]


def aranka(payload, scenes):
    from storylines import aranka_trickster as route
    receipt = 'aranka.thall.parting_spoken'
    delivered = 'aranka.thall.coda_delivered'
    payload['Derived'][delivered] = [['trickster.ever', 'lastcall.active', 'aranka.lastcall.route_open',
                                     'aranka.payoff.partner', 'aranka.present_now']]
    for event in scenes.values():
        if not event['Id'].startswith('aranka.trickster.epilogue.'):
            continue
        for page in event['Nodes']:
            for block in page.get('Paragraphs', []):
                if 'unfinished letter to Thall' in block['Text'] or 'Thall\'s death in the Midnight Fane' in block['Text']:
                    block['Forbids'] = [delivered if f == 'lastcall.active' else f for f in block['Forbids']]
    # Retain the merged round-2 contextual nodes and choice indices as dormant
    # save references. New contact is route-owned; it no longer interrupts billing
    # or the intimate threshold and never awards a response from an absent Thall.
    for event in scenes.values():
        sid = event['Id']
        targets = ('signed', 'billing') if sid.startswith('aranka.trickster.verse.duet') else (
            ('desire',) if sid == 'aranka.no_encore_needed' else ())
        for target in targets:
            page = node(event, target)
            original = deepcopy(page)
            old_choices = page['Choices']
            for answer in old_choices:
                answer['Forbids'].append('trickster.ever')
            continuation = deepcopy(original)
            continuation['Id'] = 'thall_' + target
            dead = deepcopy(original)
            dead['Id'] = 'thall_dead_' + target
            page['Choices'].append(c('"Have you heard from him?"', continuation['Id'],
                flags=(receipt,), requires=('trickster.ever',), forbids=(route.THALL_DEAD, 'trickster.ever')))
            page['Choices'].append(c('"Have you heard from him?"', dead['Id'],
                flags=(receipt,), requires=(route.THALL_DEAD, 'trickster.ever'), forbids=('trickster.ever',)))
            # The old answers remain at their saved positions. Appended answers
            # restore the same musical/romantic continuation on Trickster.
            for answer in original['Choices']:
                answer['Requires'].append('trickster.ever')
                page['Choices'].append(answer)
            event['Nodes'].extend((continuation, dead))
    # The Last Call page owns the single conclusion when it is delivered;
    # ordinary ending callbacks yield it in Last Call histories.
    coda = node(scenes['aranka.lastcall.page'], 'page')
    for block in coda.get('Paragraphs', []):
        if block['Text'] == route.THALL_ENDING:
            require(block, receipt)
    call = node(scenes['aranka.lastcall.call'], 'call')
    call['Text'] = call['Text'].replace(route.THALL_CALL, '')


def integrate(payload):
    scenes = {s['Id']: s for s in payload['Scenes']}
    # Readiness remains an opportunity reader. Campaign codas read acceptance.
    for route in ('gesmerha', 'devarra', 'eliandra', 'jerribeth', 'chadali', 'hepzamirah'):
        event = scenes[route + '.lastcall.page']
        event['RequiresAnyGroups'] = [[payload['Relationships'][route]['CommittedFlag']]]
        key = route + '.trickster.partner'
        if key in payload['Derived']:
            payload['Derived'][key] = [g for g in payload['Derived'][key] if route + '.trickster.late_committed' not in g]
    late_endings(payload, scenes)
    eliandra(payload, scenes)
    soana(scenes)
    pair(scenes)
    wenduag(payload, scenes)
    aranka(payload, scenes)
