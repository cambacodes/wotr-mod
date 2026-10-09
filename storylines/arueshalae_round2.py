"""Round 2 Arueshalae continuations, authored against the set-piece and TP sheets.

Only this route's existing situations are adapted. Saved answers and destinations
remain in place; alternate histories and explicit cuts append nodes/answers.
Dimalchio is a former lover (native Q2), not a live partner. No echo is allocated.
"""
from copy import deepcopy
from story_format import c, n, p

T = 'arueshalae.treatment.'
P = 'arueshalae.trickster.'
CHANGED = 'arueshalae.changed'
INTAKE = T + 'intake'
FAST_ACTIVE = T + 'fast_unresolved'
DREZEN = '2570015799edf594daf2f076f2f975d8'


def integrate(payload):
    scenes = {s['Id']: s for s in payload['Scenes'] if s.get('Relationship') == 'arueshalae'}
    # Legacy location twins intentionally share authoring lists. Detach each
    # scene before appending its own saved destinations.
    for route_scene in scenes.values():
        route_scene['Nodes'] = deepcopy(route_scene['Nodes'])

    def node(sid, nid):
        return next(nd for nd in scenes[sid]['Nodes'] if nd['Id'] == nid)

    def add(sid, nid, text, *answers, speaker='Arueshalae'):
        nd = n(nid, speaker, text, *answers, portrait='Arueshalae')
        scenes[sid]['Nodes'].append(nd)
        return nd

    def guard(answer, field, *keys):
        answer[field] = list(dict.fromkeys(answer.get(field, []) + list(keys)))

    # Existing promised interval is unresolved until her existing seven-day
    # decision. No timer, new cost or reconciliation condition is introduced.
    payload.setdefault('Derived', {})[FAST_ACTIVE] = [[T + 'fast']]
    payload.setdefault('DerivedForbids', {})[FAST_ACTIVE] = [T + 'prescription', CHANGED]
    contact_scenes = [T + name for name in ('old_name', 'the_dance', 'abyss_dose', 'the_scar', 'kitchen', 'night')]
    for sid in contact_scenes:
        for nd in scenes[sid]['Nodes']:
            for answer in nd['Choices']:
                if answer.get('RemoveItem') and answer.get('Next') not in ('hers',):
                    guard(answer, 'Forbids', FAST_ACTIVE)
    # The wall's already-paid handholding ends at minute six. Elapsed time
    # supplies no extra ward, stopping intervention or use of her old name.
    # Every no-contact alternative is retained during the fast.

    # A cat's ordinary claws cannot account for a succubus scar. Keep the old
    # scene/node/answer identities; the keepsake is now the played acceptance.
    sid = T + 'the_cat'
    node(sid, 'science')['Choices'][1]['Text'] = '"Let me see this famous hand, then."'
    sid = T + 'the_scar'
    scenes[sid]['Title'] = 'The empty hand'
    node(sid, 'start')['Text'] = ('{n}She offers her hand, back uppermost. It is unmarked.{/n} '
        '"The cat slept on it. I keep looking, as if there ought to be something there. You asked to see it. There."')
    node(sid, 'mark')['Text'] = ('"Nothing to show anybody." {n}She turns her palm over.{/n} '
        '"It liked me. I was late for muster because it liked me. That is quite enough trouble for one cat."')
    node(sid, 'mark')['Choices'][0]['Text'] = '"Keep the memory, then."'
    node(sid, 'mark')['Choices'][1]['Text'] = '[Spend a Scroll of Death Ward: have it read at the shrine door, then kiss her hand]'
    node(sid, 'mark')['Choices'][2]['Text'] = '[Kiss her hand]'
    node(sid, 'keep')['Text'] = ('"Yes. I will." {n}She folds her hands together.{/n} '
        '"I never thought I would be so pleased about sitting still. Go on. Laugh. I did."')
    node(sid, 'kiss')['Text'] = ('{n}She watches you return from the shrine with the ward read. You kiss the back of her hand. '
        'Nothing drains from you. Her fingers close on yours.{/n} "For this? You spent a scroll for this?" '
        '{n}She bends and kisses your knuckles in return, then lets go well before the ward ends.{/n} '
        '"Now I have something else to remember."')
    node(sid, 'kiss_e')['Text'] = ('{n}You kiss her hand. She holds yours, watching your warm fingers.{/n} '
        '"I still expect the cold. Even now." {n}She kisses your knuckles.{/n} "There. Two things to remember."')

    # Physical Drezen staging, including the cat and every chapel sibling.
    for suffix in ('the_cat', 'the_song', 'the_scar', 'the_novice', 'rainy_day', 'the_second_chair', 'the_bakery', 'abyss_dose'):
        scenes[T + suffix]['Areas'] = [DREZEN]
    for suffix in ('chaplain.censer', 'chaplain.complaint', 'chaplain.wedding', 'chaplain.sermon', 'chaplain.prayer', 'terms_again_chaplain'):
        scenes[P + suffix]['Areas'] = [DREZEN]
    # Recollection of Vellexia does not require her present availability.
    for sid in (T + 'teach_me', T + 'the_second_chair'):
        scenes[sid]['Forbids'] = [key for key in scenes[sid]['Forbids'] if not key.startswith('vellexia.')]

    # The tower's daybook passage exists only in histories that undertook the open hand (intake).
    sid = T + 'morning'
    scenes[sid]['Entry'] = '"Good morning."'
    start = node(sid, 'start')
    for answer in start['Choices']:
        guard(answer, 'Requires', INTAKE)
    start['Text'] = ('{n}First light rises grey over the Worldwound. She sits on the broken bell-floor in your shirt, '
        'one wing resting over your wrapped shoulders. She catches you looking and smiles without looking away.{/n} '
        '"I am keeping this until we go down. You can explain it at council."')
    start['Choices'].append(c('Continue', 'ordinary', forbids=(INTAKE,)))
    # Her daybook passage is retained as an appended intake-specific passage, so
    # untreated released/chaplain lovers never acquire somebody else's daybook.
    for answer in start['Choices'][:2]:
        old = answer['Next']
        answer['Next'] = 'notes_' + old
        add(sid, 'notes_' + old,
            '{n}She shields the daybook on her knees.{/n} "Don\'t look. I drew a diagram and crossed it out because it was indecent. Then I drew it again because it was accurate."',
            c('Continue', old))
    add(sid, 'ordinary',
        '{n}She pulls your cloak closer around you and rests her cheek against the covered shoulder.{/n} '
        '"The watch changed twice while you slept. I could have flown down. I wanted to stay."',
        c('Continue', 'count_e', requires=(CHANGED,)),
        c('Continue', 'count', forbids=(CHANGED,)))
    for nid in ('count', 'count_e'):
        for answer in node(sid, nid)['Choices']:
            guard(answer, 'Requires', INTAKE)
        node(sid, nid)['Choices'].append(c('"Stay until the sun is up."', 'stay_' + nid, flags=(T + 'morning',)))
        add(sid, 'stay_' + nid,
            ('{n}She leans forward and kisses your mouth, slowly, then takes your hand.{/n} "Yes. I want another morning like this."'
             if nid == 'count_e' else
             '{n}She kisses your forehead through the cloak and settles beside you.{/n} "Yes. Keep this between us. I want you warm when we go down."'))
    # Sosiel's line is a reaction to a real treatment and warded night.
    scenes[T + 'react.sosiel_morning']['Requires'] += [INTAKE, T + 'night.warded']

    # Farewell uses the tower shared by every morning history. Optional
    # recollections retain indices, but must have all their actual producers.
    sid = T + 'the_eve'
    node(sid, 'start')['Text'] = ('{n}On the edge of the camp she lifts a lantern to find your face. '
        'Beyond the pickets, the road toward Threshold is dark.{/n} "I wanted to see you before the next muster. '
        'I keep thinking about the tower. How quiet it was up there."')
    node(sid, 'fear')['Text'] = ('"I am afraid of what is at the bottom of the Wound." {n}She sets the lantern down.{/n} '
        '"I remember how I answered when the Abyss called. I have to go back there with you. '
        'If you see me falter, call me. Don\'t wait for me to ask."')
    guard(node(sid, 'fear')['Choices'][1], 'Requires', T + 'rx_want', T + 'mealtimes', T + 'kitchen', T + 'relapse')
    node(sid, 'fear')['Choices'].append(c('"The tower. You stopped, and I stayed. Remember that."', 'tower', flags=(T + 'the_eve',)))
    node(sid, 'joke')['Text'] = ('"I will hear it." {n}She laughs, and catches your sleeve.{/n} '
        '"I will probably be furious. That should help. Come back after this is done. I want to hear another terrible joke."')
    add(sid, 'tower',
        '"I remember." {n}Her fingers tighten on your sleeve.{/n} "I chose that night. I will choose what I do down there too. '
        'But I want to hear you. Stay where I can hear you."')
    guard(node(T + 'after_the_war', 'you')['Choices'][1], 'Requires', INTAKE)

    # A replacement evening has a real prior promise (dance/after). Otherwise
    # this is a fresh invitation, never an invented missed Tuesday.
    sid = T + 'rainy_day'
    old_start = node(sid, 'start')
    old_start['Choices'][0]['Forbids'].append(T + 'the_dance')
    old_start['Choices'].append(c('Continue', 'evening', requires=(T + 'the_dance',)))
    add(sid, 'evening',
        '"Twice a week, you said." {n}She points at the rain on the shutters.{/n} '
        '"We cannot dance in that. I am annoyed. I wanted this evening." '
        '{n}She shifts her wings to make room on the cot.{/n} "Then stay here instead. I am keeping the evening, even if the fiddlers hide indoors."',
        c('"Then this evening is yours."', 'stay'),
        c('"The dispatches cannot wait."', 'duties', flags=(T + 'rainy_day',)))
    add(sid, 'duties',
        '{n}She draws her wings back over the empty place.{/n} "Go, then. I know what the dispatches mean. '
        'I can know that and still be annoyed. When you have an evening, bring it here yourself."')

    # Service cannot be an affection switch. Both changed and unreleased
    # women answer privately; native release is a completed fact.
    sid = P + 'failed.chaplain'
    scenes[sid]['Entry'] = '[Bring a sword and censer to the vestry] "The second company needs a chaplain."'
    sid = P + 'terms'
    question = node(sid, 'question')
    old_answers = deepcopy(question['Choices'])
    for nd in scenes[sid]['Nodes']:
        if nd['Id'] != 'question':
            for answer in nd['Choices']:
                if answer.get('Next') == 'question':
                    guard(answer, 'Forbids', CHANGED)
                    alt = deepcopy(answer)
                    alt['Next'] = 'question_changed'
                    alt['Forbids'].remove(CHANGED)
                    guard(alt, 'Requires', CHANGED)
                    nd['Choices'].append(alt)
                    break
    add(sid, 'question_changed',
        '"The hunger is gone. Desna gave me that. She did not choose this for me." '
        '{n}She sets the blade aside.{/n} "I want you. You know what I did before I changed. Will you have me with those memories too?"',
        *old_answers)
    # Retry lines cannot invent a witnessed week of repeated wards.
    node(T + 'rite_slipped', 'vow')['Text'] = ('"On the road." {n}She stays in the far corner.{/n} '
        '"Desnans don\'t swear on the road lightly; travellers die on it. Then a week apart, and I\'ll count it. '
        'When it\'s done I\'ll come to you, not the other way round, and I\'ll be hungry, and you\'ll be warded."')

    # First-quarrel disclosure is collected by later paid contact, without a
    # new fee/gate. The seal/price is stated before either reading is chosen.
    promise_read = T + 'price_disclosed'
    refusal_read = T + 'price_disputed'
    for nd in scenes[T + 'first_quarrel']['Nodes']:
        if nd['Id'] in ('promise', 'cant'):
            nd['Choices'][0]['Set'].append(promise_read if nd['Id'] == 'promise' else refusal_read)
    for sid in contact_scenes:
        for nd in scenes[sid]['Nodes']:
            for answer in nd['Choices']:
                if answer.get('RemoveItem') and not (set(answer.get('Requires', [])) & set(answer.get('Forbids', []))):
                    answer['Text'] = answer['Text'].replace('Spend a Scroll of Death Ward:', 'Tell her the scroll costs 700 gold; spend a Scroll of Death Ward:')

    # Explicit slots are alternative heated cuts, never new nights or receipts.
    sid = T + 'night'
    undress = node(sid, 'undress')
    for index, suffix, dest, text in (
        (0, 'explicit.2', 'morning_after', '{n}She answers your kiss with another, her wings closing around you on the cloak. Later she settles her ear against your chest and listens to your heartbeat.{/n}'),
        (1, 'explicit.1', 'morning_after_paid', '{n}She draws you down onto the cloak, counting under her breath between kisses. Before the ward runs out she tears herself off you and drags her cloak between your skin and hers, panting, furious at the clock.{/n}'),
    ):
        undress['Choices'][index]['Next'] = sid + '.' + suffix
        # Content brief lives in tools/route_packs/explicit_slots/arueshalae/.
        add(sid, sid + '.' + suffix, text, c('Continue', dest), speaker='Narrator')
    for sid in (P + 'fallen.roof', P + 'evil.window', P + 'evil.window_yard'):
        cut = node(sid, 'cut')
        dest = cut['Choices'][0]['Next']
        cut['Choices'][0]['Next'] = sid + '.explicit.1'
        # Current fallen: warded, remaining minutes only; legacy windows keep
        # their old paid/ward variants and destination/effects exactly.
        text = ('{n}She pulls you close on the wet slates. Before the ward expires, she lets go and gathers you into the shelter of her wings.{/n}'
                if sid == P + 'fallen.roof' else
                '{n}She pulls you close against the wet slates. Later she draws back from you, rain running off her wings.{/n}')
        add(sid, sid + '.explicit.1', text,
            c('Continue', dest), speaker='Narrator')

    # Fallen recruit first negotiation (arue12: no physician, no fee); research
    # and daybook callbacks require their actual separate histories.
    sid = P + 'fallen.house_call'
    start = node(sid, 'start')
    start['Text'] = ('{n}She lets you take her wrist through the black silk, and laughs, low and delighted, and does not pull away.{/n} '
        '"Still holding a succubus through a sleeve, darling? Look at the earnest face." '
        '{n}She leans in until her mouth is at your ear.{/n} "I worship one god now, and she\'s standing right here, and she\'s starving. '
        'Keep that face. I want to watch it when I tell you what I eat."')
    guard(start['Choices'][0], 'Requires', T + 'studied', INTAKE)
    # Existing untreated alternative stays at index 1, now complementary to
    # all treatment fragments, not just one coarse derived key.
    start['Choices'][1]['Forbids'] = []
    start['Choices'][1]['Next'] = 'research_check'
    add(sid, 'research_check',
        '"You came all this way with your blood still in you. How thoughtful." {n}She draws a nail along your cuff, over the vein.{/n}',
        c('Continue', 'price', forbids=(T + 'studied',)),
        c('Continue', 'research_only', requires=(T + 'studied',), forbids=(INTAKE,)),
        c('Continue', 'price', requires=(T + 'studied', INTAKE)))
    add(sid, 'research_only',
        '"I remember those books. Did you find a price you liked?" {n}She smiles.{/n} "I can improve on it."', c('Continue', 'price'))
    node(sid, 'candles')['Text'] = ('"The shrine books. Your sums in the margin. My careful notes." '
        '{n}She hooks a nail in your cuff.{/n} "I burned the daybook. I read every page as it caught, all those little notes about how mortals pass the bread, '
        'and I laughed until the smoke made me cough. I remember wanting you, too. I still do. It\'s just that now I want you the way I want everything else."')
    # arue12: the charred corner is burned in front of the Commander (base text); no kept regret.

    # Endings: no paid ward after release, no invented abstinence or absolution.
    for sid in (T + 'epilogue.together', T + 'epilogue.freed', P + 'epilogue.kept'):
        page = node(sid, 'page')
        page.setdefault('Paragraphs', []).append(p(
            '{n}Once her nature changed, she kept her cottage away from the settlements. The Commander visited, '
            'and she sometimes came to Drezen, carrying her own bag and expecting supper. She went home again when she wished.{/n}', requires=(CHANGED,)))
    page = node(T + 'epilogue.together', 'page')
    page['Paragraphs'] += [
        p('{n}Every scroll after that had its price named before the seal broke, as she had made the Commander swear. Some nights she heard the price and said no, '
          'and lay awake beside the shut case, hungry, and would not be bought. Most nights she said yes, and made very sure the gold was the cheapest thing either of them spent.{/n}', requires=(promise_read,), forbids=(CHANGED,)),
        p('{n}They went on quarrelling over the scrolls for years. She hated being paid for, and said so at length, in front of guests; then she came to bed, and the seal was broken, and she let it be paid for anyway, and was furious about it in the morning.{/n}', requires=(refusal_read,), forbids=(CHANGED,)),
        p('{n}There was no bargain with her queen. When Nocticula was mentioned at table, Arueshalae smiled the old smile from the long tables of the Upper City, and took a fold of the Commander\'s sleeve in her fist, as if somebody might try to take it from her.{/n}', requires=(T + 'promised_no_deals',)),
    ]
    page = node(P + 'epilogue.kept', 'page')
    for par in page.get('Paragraphs', []):
        if 'kept the stole' in par['Text']:
            par['Text'] = '{n}She kept the stole. On visits to Drezen she blessed the second company\'s swords at dawn and went hunting for the Commander by noon, and if anyone in the company had an opinion about the order of the two, they kept it to themselves.{/n}'
        if 'pulse first' in par['Text']:
            guard(par, 'Forbids', CHANGED)
            par['Text'] = '{n}She kept a tally book of every minute the scrolls had bought her. At each reunion she stood close enough to smell the Commander\'s blood under the skin, the way she had once stood beside the men she meant to finish, and did not touch, and stayed to hear the news.{/n}'
    for sid in (P + 'epilogue.kept', P + 'epilogue.commit', T + 'epilogue.together'):
        node(sid, 'page').setdefault('Paragraphs', []).extend([
            p('{n}The Commander never again announced anything at her altar. When she came back from her service she hung up the stole herself and came looking for {mf|him|her} in private, where nobody was kneeling and nobody was watching.{/n}', requires=(P + 'cost.no_staging',)),
            p('{n}There was no second joke played with her life. She had been the punchline once, and she made very sure, for the rest of the Commander\'s days, that she was never anybody\'s joke again, the Commander\'s least of all.{/n}', requires=(P + 'cost.no_second_joke',)),
        ])
    page = node(P + 'epilogue.commit', 'page')
    for par in list(page.get('Paragraphs', [])):
        if 'hunger and the prayer' in par['Text']:
            guard(par, 'Forbids', CHANGED)
            alt = deepcopy(par);alt['Forbids'].remove(CHANGED);guard(alt, 'Requires', CHANGED)
            alt['Text'] = '{n}On the chapel steps she kept her service and took the Commander as well, because she wanted both and saw no reason to go hungry for either. Her hunger was gone. Her memories were not; she told them at table, and would not be loved by anyone who needed her to forget them.{/n}'
            page['Paragraphs'].append(alt)
        if 'month after Threshold' in par['Text']:
            par['Text'] = ('{n}She had asked once, on the edge of her bedroll, for the scrolls and the hand to stop, to see whether she still wanted the Commander with nothing in it for the hunger. She did. '
                'When the war was over she did not wait to be sent for. '
                'She took a fold of the Commander\'s sleeve in her fist and said "Stay," as if it were an order, and it was.{/n}')
    page = node(P + 'epilogue.declined', 'page')
    for par in page.get('Paragraphs', []):
        if 'daybook' in par['Text']:
            guard(par, 'Requires', INTAKE)
            par['Text'] = '{n}She kept her daybook. One line, the thing she had meant to ask the Commander, sat alone on a page for a year; then she turned the page and wrote something else, and did not cross it out.{/n}'
    page['Paragraphs'] += [
        p('{n}The Commander had once asked her for only the parts of her that prayed, and she had refused. The end of the war did not change her answer. She was all of herself or none, and the Commander had chosen none.{/n}', requires=(P + 'cost.saint_only',)),
        p('{n}She had never waited to be asked. The Commander took time, and she gave it, and did not ask twice. The next question was the Commander\'s to ask, and she was far too proud, and far too busy living, to sit and wait for it.{/n}',
          requires=(T + 'relapse_two',), forbids=(P + 'cost.saint_only',)),
    ]

    # Verified hub confession history: these native cues establish what was
    # actually heard. A fresh confession never pretends it was already told.
    known_priestess = T + 'priestess_heard'
    payload.setdefault('SeenCues', {})[known_priestess] = [
        '6f76ee9e8f7e7d2459e44c057f219c43', '0ab5962c69552ca4ca21c787294a6c8e']
    sid = T + 'the_priestess'
    start = node(sid, 'start')
    guard(start['Choices'][0], 'Forbids', known_priestess)
    start['Choices'].append(c('Continue', 'told', requires=(known_priestess,)))
    add(sid, 'told',
        '"I told you about her when you asked about Desna. I could say what the goddess did. What I did was harder." '
        '{n}She opens the prayer book again.{/n} "I want to say it plainly this time."', c('Continue', 'tell'))
    # The original question is valid for either prescription; its recap gets
    # an appended producer-specific line, with hands only after the procedure.
    tell = node(sid, 'tell')
    tell['Choices'][0]['Next'] = 'recap'
    add(sid, 'recap', '"I have been doing what you asked." {n}She looks at the book.{/n}',
        c('Continue', 'recap_watch', requires=(T + 'rx_watch',)),
        c('Continue', 'recap_want', requires=(T + 'rx_want',), forbids=(T + 'rx_watch',)))
    for variant, text in (
        ('watch', '"Watching them eat. Trying to understand what they give each other."'),
        ('want', '"Finding things I want that are not someone to take. Writing them down."'),
    ):
        add(sid, 'recap_' + variant, text,
            c('Continue', 'recap_hand', requires=(T + 'touched',)),
            c('Continue', 'question', forbids=(T + 'touched',)))
    add(sid, 'recap_hand', '"And I held your hand. I let go while it was still safe."', c('Continue', 'question'))

    sid = P + 'chaplain.wedding'
    guard(node(sid, 'start')['Choices'][0], 'Forbids', CHANGED)
    node(sid, 'start')['Choices'].append(c('Continue', 'fear_changed', requires=(CHANGED,)))
    add(sid, 'fear_changed',
        '"I can bind their hands now. My touch takes nothing." {n}She twists the ribbon between her fingers.{/n} '
        '"But I still remember what a bargain sounded like in the Upper City. I want to get this right. Come with me."',
        *deepcopy(node(sid, 'fear')['Choices']))
    # A real ward expires after seven minutes including the return upstairs
    # and flight. Her dangerous dawn remark recalls stopping before that edge.
    nd = node(P + 'fallen.roof', 'after')
    nd['Text'] = nd['Text'].replace('There is a black feather on the pillow.', 'Your torn shirt lies on the pillow.')
    nd['Text'] = nd['Text'].replace('I let go at seven.', 'I let go before seven.')
    for sid in (P + 'evil.window', P + 'evil.window_yard'):
        nd = node(sid, 'after')
        nd['Text'] = nd['Text'].replace('There is a black feather on the pillow, and under it,', 'On your torn shirt,')

    # Both old dance result nodes share the same finite, paid ward. Neither
    # gets a fresh seven minutes after the approach or preceding reel.
    sid = T + 'the_dance'
    node(sid, 'dance')['Text'] = ('{n}The chaplain reads the ward at the chapel steps. She takes your hand, '
        'then pulls you toward the square. A sergeant treads on your foot; she laughs and nearly misses her own step.{/n} '
        '"Damn it. I could do this in the Upper City. There were fewer boots."')
    node(sid, 'cure')['Text'] = ('{n}The steps and approach have used two minutes. She counts the rest between turns, '
        'and moves her fingers to your sleeve before the ward ends. The next dance begins with cloth between you.{/n} '
        '"I want that one too. Come on."')
    node(sid, 'glove')['Text'] = ('{n}She feels the ward hold but keeps watching the chapel clock. '
        'Two minutes went on the approach. Before the remainder is spent, she moves to your sleeve and keeps dancing.{/n}')
    # Expense disclosure also covers an offered scroll, not only a kiss.
    answer = node(T + 'teach_me', 'cant')['Choices'][2]
    answer['Text'] = '[Tell her the scroll costs 700 gold, then put it in her hand] "This one is yours. Spend it on whoever you like."'
