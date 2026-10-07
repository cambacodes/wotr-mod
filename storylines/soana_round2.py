"""Route-owned round-two situations; append-only save references.

Authored additions: Gundrun correspondence and Corven's voice, the surviving
imprint in Soana's dead hand, and postwar invitations. Native evidence and the
fixed atlas allocation are recorded in tools/route_packs/plans/soana-setpieces.md.
Neither family delivery, forest work nor a life-link purchases affection.
"""
from copy import deepcopy

from story_format import c, n, p, scene
from storylines import soana_partner as P

R = 'soana.trickster.returned'
EFFECTIVE = 'soana.round2.returned_now'
MARRIAGE = 'soana.round2.partner_answer'
INVITED = 'soana.round2.renewed_welcome'
CURRENT = 'soana.round2.current_love'
LATE_YES = 'soana.round2.postwar_accepted'
READY = 'soana.round2.postwar_ready'
RETIRED = 'soana.closed'
FORBIDDEN = ('soana.closed', 'soana.trickster.friends', 'soana.later_friends',
             'soana.late_friends', 'soana.late_romance_ended', P.BROKEN)


def page(event, key):
    return next(x for x in event['Nodes'] if x['Id'] == key)


def text(event, key, value):
    page(event, key)['Text'] = value


def require(block, *flags):
    block['Requires'] = list(dict.fromkeys([*block.get('Requires', []), *flags]))


def retire(answer):
    # Keep the original target, index, ID and effects for existing saves.
    answer['Requires'].append(RETIRED)


def slot(event, host, number, cut, rejoin):
    """Append a user-filled segment; retain the old Continue at its old index."""
    key = event['Id'] + '.explicit.' + str(number)
    old = page(event, host)['Choices'][0]
    retire(old)
    page(event, host)['Choices'].append(c('[Draw her close.]', key))
    # Content brief: same-named JSON under explicit_slots/soana; heated cut default.
    event['Nodes'].append(n(key, 'Narrator', cut, c('[Stay until morning.]', rejoin)))


def family(scenes):
    for event in scenes:
        sid = event['Id']
        if not sid.startswith('soana.partner.') or '.epilogue.' in sid:
            continue
        if sid.endswith('.returned'):
            # The dead native unit never hosts the return copy.
            require(event, EFFECTIVE)
            event['ForbidOverrides'] = {f: EFFECTIVE for f in P.LOSS}
        if '.dispatch' in sid:
            text(event, 'read', '''{n}Soana holds the old letter by its sound edge. Her thumb stops beneath Roan's name.{/n}
"Gundrun. She begged me to go there. I stayed. Do you think I forgot the way south?"
{n}She takes the fresh inquiry and squints at the small letters.{/n}
"That could be Corven's hand. Or something that has seen it. Ask what he called me when I threw his wedding wreath at him. Not the color of the flowers."
{n}She snatches the blank sheet from you.{/n} "I shall write it. You can carry it. You will not speak for me."''')
            page(event, 'sent')['Choices'].append(c('[Send her question. Let the family hear her own words.]',
                forbids=(P.SHARE, P.SECRET, P.EXCLUSIVE)))
            page(event, 'read')['Choices'].append(c('[Send her question by the southern relay. No journey promised.]',
                'sent', flags=(P.PURSUED, 'soana.round2.correspondence_only')))
            # Near-discovery happens in the existing messenger scene, after she
            # deliberately chose an affair. No new concealment mechanic.
            page(event, 'sent')['Choices'].append(c('[Wait while she answers the family inquiry.]',
                'family_inquiry', requires=(P.SECRET,)))
            event['Nodes'].append(n('family_inquiry', 'Soana', '''{n}The scout looks from the old clasp to a second blanket. A collar has fallen across it. Soana picks it up before he can ask whose it is.{/n}
"Roan wants to know why I am writing again? Tell her her mother has found a fool willing to carry letters through demon country."
{n}She gives you the collar, then folds her own question over the fresh sheet.{/n}
"That is enough from you. Corven will have my words, not a tale you made softer for his ears."
{n}When the scout has gone, she keeps hold of your sleeve.{/n} "I want you back. I have not forgotten whose clasp this is."''', c('[Leave her reply with the messenger.]'), portrait='Soana'))
        elif '.homecoming' in sid:
            for item in event['Nodes']:
                for answer in item['Choices']:
                    if set(answer['Set']) & {P.TOGETHER, P.SEPARATED, P.QUIET_RETURN}:
                        answer['Set'].append('soana.partner.homecoming_kept')
            # Arrival and correspondence are separate histories. Existing paid
            # escort retains its 168-hour journey; an unpaid letter stays a letter.
            event['Forbids'].append('soana.round2.correspondence_only')
            text(event, 'start', '''{n}An elderly dwarf stops at the cave mouth. Behind him, their grown son lowers a travel pack. The escort waits below the bend, watching the demon road. Corven does not enter.{/n}
"What did you call me?" {n}Soana asks.{/n}
"A thorn bush in a wedding wreath. You threw it twice," {n}Corven answers.{/n}
{n}Her fingers leave the clasp. She crosses to him herself. They hold each other awkwardly, her staff caught between them.{/n}
"You found the road, bloody fool."
"Your words found me. I came to hear the rest."
{n}He looks past her at the bedding. She turns to face you.{/n}''')
            page(event, 'start')['Choices'].append(c('[Hear what she tells her husband.]', 'family_answer',
                forbids=(P.SHARE, P.SECRET, P.EXCLUSIVE)))
            event['Nodes'].append(n('family_answer', 'Soana', '''"I stayed here. You know why. Roan knows why, and she still curses me for it."
{n}She takes his pack, but he keeps hold of the strap.{/n}
"This hunter has kept coming. I wanted those visits. I want more than a hunter's report. You will hear it from me before there is another bed in this house."
"And what am I to come home to?" {n}Corven asks.{/n}
"Me. If you still want that stubborn woman. I have not pulled your place out by the roots."
{n}Their son sets down his own pack well away from the blankets.{/n} "Say it plainly. I won't carry guesses between you."''',
                c('"I would be her lover. Hear her answer, and give your own."', 'share', flags=(P.SHARE, P.DECIDED)),
                c('"Keep your marriage. I came as a friend."', 'family_friend'), portrait='Soana'))
            event['Nodes'].append(n('family_friend', 'Soana', '''{n}She puts Corven's pack beside the clasp and gives you the cup nearest the door.{/n}
"A friend, then. You shall still hear me curse the next demon patrol."
{n}Corven sits by the fire. Their son begins unlacing his road-worn boots.{/n}''',
                c('[Leave the family their evening.]', flags=(P.TOGETHER, P.CONFIRMED, 'soana.trickster.friends')), portrait='Soana'))
        elif '.returned_letter' in sid:
            # Legacy burning remains a costly consequence, not a v1 scheme.
            page(event, 'verdict')['Choices'].append(c('[Carry her answer. Your visits are over.]', 'answer_share',
                forbids=(P.SHARE, P.SECRET, P.EXCLUSIVE)))


def correspondence_scene(returned=False):
    event = P.cave('reply', 'The words that came south', '"The relay brought Corven\'s answer."', [
        n('start', 'Soana', '''{n}Soana breaks the fold herself. Outside, a scout checks the road for demons. She reads one line twice, then touches the clasp.{/n}
"A thorn bush in a wedding wreath. I threw it twice. Nobody else heard him say it."
{n}She lays the answer beside Roan's old letter.{/n}
"He is alive. South of the Wound. Not at my door. I sent him the truth about you; now you shall hear his own words."''',
          c('[Hear the answer to her proposed arrangement.]', 'share', requires=(P.SHARE,)),
          c('[Hear him before choosing what these visits mean.]', 'share', forbids=(P.SHARE, P.SECRET, P.EXCLUSIVE)),
          c('[Hear the answer to her separation.]', 'exclusive', requires=(P.EXCLUSIVE, P.CHOSEN)),
          c('[Hear the family news. The affair was not in her letter.]', 'secret', requires=(P.SECRET,))),
        n('share', 'Narrator', '''{n}She reads Corven's answer aloud.{/n}
"'So you want the hunter as well as the husband. I won't thank the hunter. I have waited years for your own words, and these are bitter ones. I still want my wife. You still want me — say that plainly. If I come north, I keep my bed. No child of ours carries messages between lovers. Tell me yourselves.'"
{n}Soana puts charcoal to fresh bark.{/n}
"I want him. I want you too, hunter. He will have those words. No slipping away and leaving me to answer alone."''',
          c('"He hears it from us. I will keep those terms."', 'accepted'),
          c('"Keep his place. I shall remain your friend."', 'friend')),
        n('accepted', 'Soana', '''{n}She writes the answer, folds it, and puts it in the scout's hand. Then she takes yours.{/n}
"He has answered. So have I. Now come back when I ask for you. Not only when a beast needs bleeding."
{n}Her thumb rubs a callus on your palm. She does not let go until the scout has left.{/n}''',
          c('[Leave her words with the relay. Return for her.]', flags=(P.SHARE, P.DECIDED,
              P.CONFIRMED, P.TOGETHER, 'soana.round2.reply_accepted')), portrait='Soana'),
        n('exclusive', 'Narrator', '''{n}She reads without looking up.{/n}
"'Then you have ended your vows. I am no longer your husband. I shall not cross the Wound expecting otherwise. The children will hear it from me too. Don't write calling me home.'"
{n}Soana sets the clasp beside the letter.{/n} "You wanted my answer. You have heard his as well. Stay if you meant what you said. No telling me it will all come right."''',
          c('[Stay after hearing the cost of her choice.]', flags=(P.CONFIRMED, P.SEPARATED, 'soana.round2.reply_accepted'))),
        n('secret', 'Soana', '''"He asks whether the spring still runs. Whether I still keep his clasp. He thinks he is writing to his wife as she was."
{n}She folds the letter against her throat, then sets it beyond the blanket.{/n}
"I took you for my lover. I shall not tell you that a letter washes that clean. Go now. I want to answer this without your hands distracting me."''',
          c('[Leave her with his words.]', flags=('soana.round2.family_reply',)), portrait='Soana'),
        n('friend', 'Soana', '''{n}She lets your hand go and writes her answer to Corven.{/n}
"A friend. I can write that without scratching the words out. Bring news of the demon road when you come."''',
          c('[Leave as her friend.]', flags=(P.CONFIRMED, P.TOGETHER, 'soana.trickster.friends')), portrait='Soana'),
    ], ('trickster.now', P.PURSUED, 'soana.round2.correspondence_only'), delay=168,
       forbids=(P.CONFIRMED, 'soana.round2.family_reply'))
    if returned:
        event['Id'] += '.returned'
        event['AnswerLists'] = []
        event['InteractionHub'] = 'soana.presence'
        event['Requires'].remove('soana.after_quest')
        require(event, EFFECTIVE)
        event['Forbids'].remove(R)
        event['ForbidOverrides'] = {f: EFFECTIVE for f in P.LOSS}
    return event


def prepare(scenes):
    from storylines import soana_continuation as C, soana_later_progression as L, soana_late_campaign as V
    family(scenes)
    scenes.extend((correspondence_scene(), correspondence_scene(True)))
    by = {s['Id']: s for s in scenes + C.SCENES + L.SCENES + V.SCENES}
    knot = by['soana.trickster.killed.knot']
    text(knot, 'pelt', '''{n}Clay dust lies beneath Orso's grey pelt. The medallion is gone. The scar on the dead hide answers nothing.{/n}
{n}Back in the cave, Soana's cold hand is clenched. You open it. The knot is worn into her palm, the same crossings as the bear-brand. One line darkens when your thumb presses it. Beneath the pelt, the matching line tightens.{/n}
{n}The animal's end is broken. The hand that held the spirit for years still holds a strand.{/n}''')
    text(knot, 'carcass', '''{n}The grass is dead around Orso. His brand is a scar on cold hide; it does not answer your fingers.{/n}
{n}In the cave you open Soana's clenched hand. Years of gripping her binding have worn its crossings into her palm. You press one line. The matching line beneath the dead fur contracts; her fingers close on yours.{/n}
{n}The thing she held is still pulling against its keeper. The bear is dead. Her strand has not let it go.{/n}''')
    text(knot, 'bait', '''{n}You copy the old crossings into the dead hide, then open your palm and bleed into them. You keep Soana's cold hand over yours, her worn imprint against the recut brand.{/n}
{n}Near dawn the same crossing pulls in all three palms. The horned mark she scratched on the cave wall blackens. Something strains against the keeper's hand, then against yours. Soana's dead fingers close. The clay dust stays dust; Orso does not breathe.{/n}
{n}The bound spirit has found a living grip to fight. You can offer it that grip in exchange for its keeper's life.{/n}''')
    # The registered pivot is her examination and retaking of her own work.
    acc = by['soana.trickster.returned.accounting']
    text(acc, 'judged', '''{n}Soana kneels beside the last grave. She sets its stone upright, then follows the cleared water with her eyes. At the seed-bed she pulls one stake loose and drives it a hand's breadth farther out. She takes the bowl from you.{/n}
"Mine. I shall tend it."
{n}She rises slowly, using her stick. It stays beside her now, clear of the path.{/n}
"I have not forgotten what was done to me here. Don't come expecting me to kiss it better."
{n}Her gaze catches on your mouth; she looks away, annoyed.{/n}
"Come in three days. For me. I want to find out whether I still want you by my fire when there's nothing left to carry."''')
    # Frustrated desire after the dangerous working, with Commander speech
    # left to the existing answer that admitted interrupting it.
    text(by['soana.what_followed_home'], 'interrupted', '''"You saw my signal. You broke the line anyway."
{n}Her hands close on the stick. Outside, Mervika cuts another spoiled length of cord.{/n}
"The thing had Corven's voice. I heard it too. I thought I could draw it clear. My saplings are dead. You may congratulate yourself on my breathing somewhere else."
{n}She looks toward the nursery, then nudges a stone away from your seat.{/n}
"Someone else holds the lid next time. You carry clay. And water. Mervika brought seed."
{n}She knocks the stick against the floor beside her.{/n} "Sit. I am tired of looking up at you, bloody hunter."''')
    # Existing road dispute now bears the wartime supply pressure (SOA-01).
    dispute = by['soana.the_unwelcome_path']
    page(dispute, 'start')['Text'] = '''{n}Fresh wheel-ruts stop above the seed-bed. A cart has brought supplies for the demon road; the old crossing is flooded. Soana stands in the only dry approach with her stick planted across it.{/n}
"Your soldiers need a road. My seedlings need roots that haven't been ground under a wheel. You shall hear both before you start cutting."
''' + page(dispute, 'start')['Text']
    # Delivered words replace the unsent-bark impasse, on an actual branch.
    promise = by['soana.a_promise_still_spoken']
    old = page(promise, 'start')['Choices']
    for answer in old:
        require(answer, 'soana.round2.no_family_delivery')
    page(promise, 'start')['Choices'].append(c('[Hear what she decided after sending her words south.]', 'delivered',
        requires=(P.PURSUED,)))
    promise['Nodes'].append(n('delivered', 'Soana', '''{n}The bark on her lap bears corrections. The sheet she sent south is gone.{/n}
"My words went with the scout. Not yours. Corven shall hear them without some kindly fool sanding my teeth down."
{n}She looks at you, then at the tools scattered across your usual stone.{/n}
"And now I want company without a bleeding beast at the door. That was harder to write than the news about the forest."
{n}She clears the stone with one sweep of her arm.{/n} "Sit, if that is what you came for."''',
        c('[Tell her what you want from these visits.]', 'history'), portrait='Soana'))
    days = by['soana.the_days_she_counted']
    # Same append-only treatment for the delivered family account at commitment.
    page(days, 'letter')['Text'] = '''{n}Soana folds her account of the wood and keeps it in her own hand.{/n}
"Where I planted. Where it stayed bare. Your name. He shall have those words from me."
{n}She glances at the clasp, then at your bundle.{/n}
"I want you back. If you mean to stay as my lover, you shall hear what becomes of that house too. No calling me a widow because you haven't seen him."
{n}She moves her stick out of the place beside her.{/n} "You are here now. Say what you came to say."'''
    nights(by)
    lastcall_record()


def lastcall_record():
    """Amend Soana's own record; do not edit the shared emitter or collectors."""
    from storylines import lastcall_partners
    record = next(x for x in lastcall_partners.PARTNERS if x['key'] == 'soana')
    record['page_forbids'] = tuple(dict.fromkeys((*record['page_forbids'], 'soana.round2.no_current_love')))
    record['page_forbid_overrides'].update({f: EFFECTIVE for f in P.LOSS})
    record['call']['entry'] = '[Name the Wintersun debt] "What was promised is still owed. Collect from the living."'
    record['call']['text'] = '''{n}The fire smells of cold moss. You name what was promised at Wintersun: Soana's winter blood, a portion shared only if you offered your own palm, or the grip transferred from the keeper's hand. Beyond the fire, something listens for the debt that belongs to it.{/n}'''
    for block in record['paragraphs']:
        if P.TOGETHER in block.get('Requires', []) and 'come home' in block['Text']:
            block['Text'] = '{n}Corven had answered for himself and kept the marriage, with his own bed and no children carrying messages between lovers. Soana kept writing him. His answer had never been counted as his arrival.{/n}'
        if P.CONFIRMED in block.get('Forbids', ()) and "fate was still unknown" in block['Text']:
            block['Forbids'].append('soana.round2.family_reply')
        if 'spirits came for their portion' in block['Text']:
            require(block, 'soana.trickster.cost.portion_shared')
        if 'retied' in block['Text'] and 'knot' in block['Text']:
            require(block, EFFECTIVE, 'soana.trickster.accounting_invited')
    record['paragraphs'] = (*record['paragraphs'],
        p('{n}Corven was alive in the south. Soana had recognized his answer to her wedding question and written him family news. Her lover had not been named in those letters. His clasp stayed beside the bedding; she knew whose words she still owed.{/n}',
          requires=('soana.round2.family_reply',)),
        p('{n}The Abyss spirit pulled against the knot that had held it in Orso. Soana closed her fist on the binding and dragged it back. No woodland offering fed that creditor. The life at the other end remained the price they had chosen.{/n}',
          requires=('soana.lastcall.called', EFFECTIVE, 'soana.trickster.cost.knot_bearer')),
        p('{n}Soana opened her own palm at the cave mouth each winter. The Commander had watched that first payment without offering theirs. The wood knew her taste; it had acquired no taste for the visitor.{/n}',
          requires=('soana.trickster.cost.blood_given',), forbids=('soana.trickster.cost.portion_shared',)),
    )


def nights(by):
    living = (
        ('soana.after_the_last_visitor', '{n}Soana pulls you onto the spread blanket, her bare shoulders warm beneath your hands. She catches your mouth before you can speak; the tools scrape stone as she pushes them farther away.{/n}'),
        ('soana.before_the_far_road', '{n}Her shawl falls over the tools. Soana draws you against her bare skin and pulls the blanket beneath you, keeping her mouth on yours as the cave darkens.{/n}'),
    )
    for sid, cut in living:
        event = by[sid]
        night = page(event, 'night')
        # Keep the old node and outgoing answer; split its composite morning.
        marker = '{n}In the morning'
        pos = night['Text'].find(marker)
        if pos < 0:
            pos = night['Text'].find('{n}Morning')
        assert pos >= 0, sid
        morning = night['Text'][pos:]
        night['Text'] = night['Text'][:pos].rstrip()
        event['Nodes'].append(n('round2_morning', 'Soana', morning,
            *deepcopy(night['Choices']), portrait='Soana'))
        slot(event, 'night', 1, cut, 'round2_morning')
    cuts = {
        'terms': (
            '{n}Soana puts the cord safely beside the furs, then pulls your loosened shirt from your shoulders. Her kiss is fierce; her free hand drags you down beside her.{/n}',
            '{n}She sets the sharp fragments beyond the furs. Then Soana catches your belt, draws you against her bare shoulders, and kisses you until you both sink onto the pelts.{/n}'),
        'second_ask': (
            '{n}She lays your marked wrist clear of the cord and pulls you closer with her other hand. Her clothes fall beside the furs; she meets your kiss with a hungry, cracked laugh.{/n}',
            '{n}The fragments lie out of reach. Soana keeps the sore wrist clear as she draws you onto the furs, her bare shoulder pressed to your mouth.{/n}'),
        'rebind': (
            '{n}Soana puts the cord down herself and pulls you into the place she has cleared beside her. Her mouth finds yours; her grip on your collar does not slacken.{/n}',
            '{n}She sets the shards beside her tools and catches your shirt in both hands. Soana draws you down into the furs, meeting you with a kiss that leaves you breathless.{/n}'),
    }
    for kind, pair in cuts.items():
        event = by['soana.trickster.returned.' + kind]
        for number, host in enumerate(('night', 'night_clay'), 1):
            token = 'cord' if number == 1 else 'fragments'
            renewal = 'I asked you back. I meant it.' if kind == 'rebind' else 'No more talk of graves tonight.'
            text(event, host, '''{n}Soana finishes the binding before she touches your belt. She loosens the tie over the mark and sets the ''' + token + ''' beside the tools.{/n}
"That is the knot's business finished. This is mine. ''' + renewal + '''"
{n}She draws your mouth to hers. Her rough fingers work the buckle, impatient with the iron.{/n}''')
            slot(event, host, number, pair[number - 1], 'morning')
        if kind == 'rebind':
            text(event, 'morning', '''{n}Your shirt lies under the spade handle. Soana sits beside the furs, bare shoulder against yours, inspecting the wrist she has bound anew. She moves your fingers away from the token.{/n}
"Still mine. Don't pick at it."
{n}She pushes smoked fish into your free hand, then reaches for her seed bowl.{/n} "Eat. The demons will not wait while you stare at me."''')
        elif kind == 'second_ask':
            text(event, 'morning', '''{n}Soana unties the temporary strip before you wake fully. The chosen cut has closed into a pale ridge. She keeps it clear of the fur, then drops your misplaced shirt on your face.{/n}
"White, as I said. It will ache in winter. You made me ask twice; don't make me tell you where your clothes are twice."
{n}Smoked fish waits by the hearth. Her warm knee presses yours once before she gets up to tend her binding.{/n} "Go and fight. Don't die first."''')
        else:
            text(event, 'morning', '''{n}Soana is awake beside you, her braid loose over your discarded shirt. She lifts your marked wrist clear of the blanket and checks the binding with a scowl.{/n}
"Your end is sore. It is supposed to be. Leave it alone."
{n}She kisses your unmarked knuckles, then shoves the shirt into your hand. Smoked fish waits beside the cold hearth.{/n} "Eat before you go. I have a forest to plant, and you have demons to kill."''')
    for kind, cut in (
        ('bowl', '{n}Soana sets the die beyond your reach, then draws your hands back to her warm bare skin. She kisses you hard and pulls you after her into the furs.{/n}'),
        ('second_ask', '{n}She sets both dice aside. Soana catches your mouth with hers and draws you onto the furs, laughing roughly when your shirt snags beneath her hand.{/n}'),
    ):
        event = by['soana.trickster.missed.' + kind]
        text(event, 'threshold', '''{n}She puts the offering out of reach before she unfastens her clothes. Outside the cave, the bear's footfalls recede toward the road.{/n}
"Leave the bowl. I have not asked a bone to choose my lover."
{n}Her hand closes on your belt. She pulls you against her and kisses you, hard enough to stop the next word.{/n}''')
        if kind == 'second_ask':
            text(event, 'night', '''{n}Soana weighs the second die, then puts it beside its brother. She clears the place beside her with her foot.{/n}
"I made you wait for an answer. Then you made me ask again. Enough waiting, hunter. Come here."''')
            text(event, 'morning', '''{n}Both dice sit twenty up. Your shirt is caught beneath Soana's elbow; she refuses to move until she has eaten the fish you pass her.{/n}
"Honest bones at your soldiers' fire now. Don't come whining when you lose."
{n}She frees the shirt and pulls you back for a kiss before you put it on. Outside, the she-bear sniffs the demon road.{/n} "Off with you. My luck has work to do."''')
        slot(event, 'threshold', 1, cut, 'morning')


def postwar(event, kind):
    """Fresh yes on the page; the saved .continue remains effect-free."""
    start = event['Nodes'][0]
    if kind == 'commit':
        # Keep paragraph positions read by the integrated payoff contract.
        start['Paragraphs'][4]['Text'] = '''{n}The following spring Soana held out a cord plaited from her own hair.{/n} "Your life at the other end. You know what it holds. Do you still want me, hunter?"'''
        require(start['Paragraphs'][4], 'soana.trickster.accounting_invited')
    for response in event['Nodes']:
        if response['Id'].startswith('partner_') and 'exclusive' not in response['Id']:
            for paragraph in response.get('Paragraphs', []):
                if 'new cord' in paragraph['Text'] or 'life to hers' in paragraph['Text']:
                    paragraph['Text'] = '''{n}Soana held the cord clear of the furs.{/n} "Say it before we lie down. Mine first. Or keep your life and leave my knot alone."'''
    cut = {
        'commit': '{n}Soana laid the new cord beside the furs and caught the Commander\'s belt. She pulled them down against her bare shoulders, kissed them hard, and pushed the discarded shirt across the cold stone.{/n}',
        'luck_late': '{n}Back in Wintersun, Soana put the die beside her bowl and pulled the Commander against her. Her shawl slipped from her shoulders; she caught their mouth with hers and drew them down into the furs.{/n}',
        'living_late': '{n}Soana pushed her tools beyond the blanket and pulled the Commander down beside her. Her bare shoulder pressed against their mouth; she gripped their collar and drew them closer.{/n}',
    }[kind]
    target = event['Id'] + '.explicit.1'
    # Append to every accepted stance continuation; no inherited exit effects
    # change. The old accept still accepts that stance, but no longer invents
    # a night or household consent before a fresh romantic answer.
    for response in list(event['Nodes']):
        if response['Id'] != 'start' and not response['Id'].startswith(('partner_share_', 'partner_secret_')):
            continue
        response['Choices'].append(c('"Mine first. I want you."' if kind == 'commit' else '[Return to Wintersun. Stay when she draws you close.]',
            target, flags=(LATE_YES,), requires=(P.DECIDED, MARRIAGE),
            forbids=FORBIDDEN))
    event['Nodes'].extend((
        n(target, 'Narrator', cut, c('[Stay until morning.]', 'round2_morning')),
        n('round2_morning', 'Soana', '''{n}In the morning Soana pushed the Commander's crumpled shirt across the furs. She kept a bare shoulder against them while she divided the smoked fish.{/n}
"Eat. The war is over; that is no reason to go thin."
{n}She got up to fetch her tools, then came back and kissed them with the fish still in her hand.{/n} "You can stay while I work. Keep those boots out of the seed-bed."''', dict(c('[Keep the visit she chose.]'), Id='continue'), portrait='Soana'),
    ))
    # The slot brief promises a specific final transition into this aftermath.
    # Ritual ownership is paid on the vow road only, not derived from the night.
    if kind == 'commit':
        for response in event['Nodes']:
            for answer in response['Choices']:
                if answer.get('Next') == target:
                    answer['Set'].extend(('soana.trickster.cost.knot_bearer',))
                    answer['Next'] = 'round2_vow'
        event['Nodes'].append(n('round2_vow', 'Soana', '''{n}Soana put the new cord round the marked wrist and tied its other end to her own. The pull settled between the two lives. She held the knot until it stopped trembling, then loosened the temporary tie over the skin.{/n}
"There. Yours first. As you said."
{n}She laid the cord beside the furs and drew the Commander closer by the belt.{/n}''',
            c('[Stay when she draws you down.]', target), portrait='Soana'))
    for response in event['Nodes']:
        for block in response.get('Paragraphs', []):
            # Legacy paragraphs keep indices/metadata and cease promising an
            # unplayed consummation or binding merely from a stance selection.
            if 'led them down' in block['Text'] or 'tied their life' in block['Text']:
                require(block, LATE_YES)


def integrate(payload):
    """Apply only Soana-owned readers/scenes after the existing route emitter."""
    from storylines import soana_round3
    soana_round3.predicates(payload)
    derived = payload.setdefault('Derived', {})
    negatives = payload.setdefault('DerivedForbids', {})
    def negative(key, flags):
        derived[key] = [['availability.observed']]
        negatives[key] = list(flags)
        return key
    # Live night scenes forbid closure, so that existing flag retires their old
    # direct cut. No impossible Derived/DerivedForbids conjunction is authored.
    no_path = negative('soana.round2.ordinary_path', ('trickster.now',))
    no_return = negative('soana.round2.not_returned', (R,))
    negative('soana.round2.no_family_delivery', (P.PURSUED,))
    derived[EFFECTIVE] = [[R, 'trickster.now']]
    derived[MARRIAGE] = [[no_path], [P.TOGETHER, P.CONFIRMED],
                         [P.EXCLUSIVE, P.CHOSEN, P.SEPARATED, P.CONFIRMED], [P.SECRET]]
    negatives[MARRIAGE] = [P.BROKEN]
    derived[INVITED] = [[no_return], [EFFECTIVE, 'soana.trickster.accounting_invited']]
    derived[CURRENT] = [['soana.committed', MARRIAGE, INVITED], [LATE_YES, MARRIAGE, INVITED]]
    negatives[CURRENT] = list(FORBIDDEN)
    not_current = negative('soana.round2.no_current_love', (CURRENT,))
    # Engine round 3 preserves extra negative guards on these route predicates.
    for key in ('soana.harem.eligible',):
        negatives.setdefault(key, []).append(not_current)
    derived[READY] = [['trickster.now', 'soana.progression_kept', 'soana.later_courting', MARRIAGE]]
    negatives[READY] = [*FORBIDDEN, *P.LOSS, R, 'soana.committed', 'soana.late_future_chosen']

    by = {s['Id']: s for s in payload['Scenes']}
    rel = payload['Relationships']['soana']
    rel['UnavailableOverrides'] = {f: EFFECTIVE for f in P.LOSS}
    require(payload['Presences']['soana.presence'], EFFECTIVE)
    for event in payload['Scenes']:
        if event.get('Relationship') != 'soana' and not event['Id'].startswith('soana.'):
            continue
        for field in ('Requires', 'Forbids', 'RequiresAny'):
            event[field] = [EFFECTIVE if k == R else k for k in event.get(field, [])]
        for group in event.get('RequiresAnyGroups', []):
            group[:] = [EFFECTIVE if k == R else k for k in group]
        for flag, override in event.get('ForbidOverrides', {}).items():
            if override == R:
                event['ForbidOverrides'][flag] = EFFECTIVE
        for node in event['Nodes']:
            if node['Id'].startswith('partner_exclusive_') and node['Id'].endswith('_chosen'):
                # She has already taken off the clasp and said she ends the
                # vows on this page. That decision lets her send the separation;
                # her old acceptance still pays its own exact costs only later.
                # Native audience cues cannot write on display. The selected
                # answer that reaches her verdict records the same decision.
                for previous in event['Nodes']:
                    for answer in previous['Choices']:
                        if answer['Next'] == node['Id']:
                            answer['Set'] = list(dict.fromkeys([
                                *answer['Set'], P.EXCLUSIVE, P.DECIDED, P.CHOSEN]))
            for block in node.get('Paragraphs', []):
                for field in ('Requires', 'Forbids'):
                    block[field] = [EFFECTIVE if k == R else k for k in block.get(field, [])]
                if P.TOGETHER in block.get('Requires', []) and 'come home' in block['Text'] and event['Id'] not in P.LOSS_ENDINGS:
                    block['Text'] = '{n}Corven had answered for himself. He had agreed to keep the marriage, with his own bed and no messages passed through their children. Soana wrote him herself. Neither a letter nor a lover at her fire decided whether he came north.{/n}'
                if P.CONFIRMED in block.get('Forbids', ()) and "fate was still unknown" in block['Text']:
                    block['Forbids'].append('soana.round2.family_reply')
                if 'bark addressed to him had stayed under its weight through every secret visit' in block['Text']:
                    block['Text'] = '{n}The visits had been an affair, hidden behind a shaman\'s counsel. The words Soana sent south gave family news; they did not tell Corven about the lover at her fire.{/n}'
            guarded = False
            for answer in node['Choices']:
                # Existing commitment producers keep every effect, including
                # their exact costs; only actual partner/reckoning history gates
                # their yes. A secret is consciously an affair, never acceptance.
                if ('soana.committed' in answer['Set'] or
                    event['Id'] == 'soana.trickster.returned.rebind' and
                    'soana.trickster.cost.knot_bearer' in answer['Set']):
                    require(answer, MARRIAGE, INVITED)
                    guarded = True
            if guarded:
                node['Choices'].append(c('[Leave the promise unanswered. Return when she asks again.]',
                    abort=not event['Owner'].endswith('Epilogue')))
            if event['Owner'].endswith('Epilogue'):
                node.setdefault('Paragraphs', []).append(p('{n}Corven was alive in the south. His wedding answer had reached Soana; she had sent family news back. The affair was still absent from her letters. No letter had brought him to her door.{/n}',
                    requires=('soana.round2.family_reply',)))
        if '.returned.' in event['Id'] or event['Id'].endswith('.returned'):
            require(event, EFFECTIVE)
    # Her on-page courtship/first kiss follows an earned honest answer, or her
    # own knowingly secret choice; ordinary living friendship has no new gate.
    name = by['soana.name_between']
    require(page(name, 'marriage')['Choices'][0], MARRIAGE)
    page(name, 'marriage')['Choices'].append(c('"I want you, even if we must call this an affair."', 'round2_affair',
        requires=('trickster.now',), forbids=(P.SHARE, P.EXCLUSIVE, 'soana.friendship_chosen'),
        flags=(P.SECRET, P.DECIDED, 'soana.courtship_chosen')))
    name['Nodes'].append(n('round2_affair', 'Soana', '''{n}Soana shuts her fist round the clasp.{/n}
"An affair. There. We can both hear the word. Corven is my husband; I don't know where he is yet."
{n}She looks at your mouth, then pulls your hand against her knee.{/n}
"I want you. Enough to be this foolish. No calling it a blessing from the spirits. If he asks, I answer him myself."''',
        c('[Take the hand she offers.]', 'court'), portrait='Soana'))
    text(name, 'marriage', '''"Corven laid flowers on my head. I became his wife. We had children. You shall not invent a grave to make room for yourself."
{n}She grips the old clasp, then lets it fall against her shawl.{/n}
"And still I watch the path when you are late. Curse you, I have work enough without listening for your boots."
{n}She knocks the folded cloth off the place beside her.{/n}
"Say what you came for. I shall give my own answer."''')
    for sid in ('soana.trickster.returned.terms', 'soana.trickster.missed.bowl'):
        for node in by[sid]['Nodes']:
            if 'Hear this first' in node['Text']:
                node['Text'] = node['Text'].replace('I had a husband. Corven.', 'Corven laid the flowers on my head. I became his wife.')
                node['Text'] = node['Text'].replace('He laid a wreath of the first summer flowers on my head and I became his wife. He is gone, and I do not know where, or whether he lives.',
                    'We had children. You have heard whose place this was. A visitor at my fire does not erase those years.')
                node['Text'] = node['Text'].replace('Take me with him in it, or do not take me.', 'You shall hear my own answer about you before I tie anything.')
    for sid, nid in (('soana.lower_bend', 'kiss_offer'), ('soana.after_the_last_visitor', 'desire'),
                     ('soana.before_the_far_road', 'desire')):
        event = by[sid]
        for node in event['Nodes']:
            for answer in node['Choices']:
                if answer.get('Next') == nid:
                    require(answer, MARRIAGE)
        # Keep a selectable departure if a pending family answer blocks touch.
        page(event, event['Nodes'][0]['Id'])['Choices'].append(c('[Return after she has heard the southern answer.]', abort=True))
    # A kiss-only living courtship remains romantic, even without full commitment.
    # It consumes her already chosen courtship, rather than manufacturing a vow.
    courting = 'soana.round2.current_courtship'
    derived[courting] = [['soana.later_courting', MARRIAGE, INVITED]]
    negatives[courting] = list(FORBIDDEN)
    require(by['soana.ending_chosen_visits'], courting)
    for sid in ('soana.ending_kept_life',
                'soana.trickster.epilogue.knot', 'soana.trickster.epilogue.luck',
                'soana.trickster.epilogue.unvowed'):
        require(by[sid], CURRENT)
    # Unvowed love is invited love. Historical commitment cannot invent the
    # graves, admission, work or her invitation in a summary after the war.
    unvowed = by['soana.trickster.epilogue.unvowed']
    require(unvowed, 'soana.trickster.accounting_invited')
    unvowed['Nodes'][0]['Paragraphs'][1]['Text'] = '{n}The old promise alone opened no place beside her blanket. Her seed-bed grew behind the fence; the knot stayed in her own hands.{/n}'
    unfinished = by['soana.trickster.epilogue.unfinished']
    unfinished['Forbids'] = [k for k in unfinished['Forbids'] if k not in ('soana.committed', 'soana.trickster.late_committed')]
    unfinished['Forbids'].append('soana.trickster.accounting_invited')
    unfinished['Nodes'][0]['Paragraphs'].extend((
        p('{n}The Commander had come for the graves. The stream and the stakes still waited for the answer she had demanded. She took up the spade herself; the visitor had never become her welcomed lover again.{/n}', requires=('soana.trickster.graveyard_kept',)),
        p('{n}Nobody came back for the graves. Soana buried the last hind alone, stopping often to rest the hand that held her leash.{/n}', forbids=('soana.trickster.graveyard_kept',)),
    ))
    for kind in ('commit', 'luck_late'):
        postwar(by['soana.trickster.epilogue.' + kind], kind)
    living = scene('soana.trickster.epilogue.living_late', 'The long visit', 'Epilogue', 5, '', [
        n('start', 'Soana', '''{n}The following spring the Commander returned to Wintersun. Soana set down the tools before the visitor could offer to carry them. The woods outside still needed watching; she left the stick beside the door.{/n}
"No beast bleeding behind you? No new trick to put in a bowl? Good."
{n}She pushed the blanket clear of the tools.{/n}
"I asked you back when the working was finished. I still want you here. Stay for the long visit. As my lover, if you mean it. The forest can spare me a night."''',
          dict(c('[Leave her invitation unanswered.]'), Id='continue'), portrait='Soana'),
    ], requires=(READY, P.DECIDED), forbids=('sacrifice',), Relationship='soana', last=99,
       ForbidOverrides={'sacrifice': 'trickster.commander_back'})
    postwar(living, 'living_late')
    for node in (living['Nodes'][0], page(living, 'round2_morning')):
        node.setdefault('Paragraphs', []).extend(deepcopy(P.paragraphs()))
        for block in node['Paragraphs']:
            if P.TOGETHER in block['Requires']:
                block['Text'] = '{n}Corven had answered Soana himself and kept their marriage, with his own bed and no children carrying messages between lovers. She kept writing him. A letter had brought his answer; it had never been counted as his arrival.{/n}'
            if P.CONFIRMED in block.get('Forbids', ()) and "fate was still unknown" in block['Text']:
                block['Forbids'].append('soana.round2.family_reply')
        node['Paragraphs'].append(p('{n}Corven was alive in the south. His wedding answer had reached Soana; her family news went back by the relay. She still owed him words about the affair.{/n}', requires=('soana.round2.family_reply',)))
    payload['Scenes'].append(living)
    # Retain the atlas allocation, creditor identity, and correct chronology in
    # the route-owned coda. Shared ledger/collector entries need coordinator work.
