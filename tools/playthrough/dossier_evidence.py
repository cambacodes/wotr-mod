"""Compact references and whole-chapter diagnostics from the existing trace/export."""
import collections
import json

GATES = ('Requires', 'Forbids', 'RequiresAny', 'RequiresAnyGroups', 'ForbidOverrides',
         'MinChapter', 'MaxChapter', 'Chapters', 'EntryMythic', 'DelayHours', 'RestAllowance')
HOSTS = ('AnswerLists', 'NativeReturnCue', 'ContinueBefore', 'ReturnToList', 'ContactUnit',
         'AdditionalContactUnits', 'Areas', 'InteractionHub', 'Remote', 'ManualOnly', 'TableHosted')
PRESENCE = ('Participants', 'ParticipantWomen', 'ParticipantContacts', 'ContactWitness',
            'PrivateParticipants', 'AfterDeparture', 'Kind')


def evidence(ctx, scene):
    presence = (ctx.story.get('Presences') or {}).get(scene.get('InteractionHub'))
    return dict(entry_gates={k: scene[k] for k in GATES if k in scene},
                host_return={k: scene[k] for k in HOSTS if k in scene},
                presence={k: scene[k] for k in PRESENCE if k in scene},
                presence_definition=presence,
                relationship=ctx.model.rels.get(scene['Relationship'], {}))


def node_states(ctx, event, before):
    scene = ctx.model.by_id[event['id']]
    held = set(before)
    sf = ctx.model.rels.get(scene['Relationship'], {}).get('StartedFlag')
    if sf and not ctx.V.is_epilogue(scene) and scene.get('NativeReturnCue') is None: held.add(sf)
    rows = []
    for i, step in enumerate(event['steps']):
        node = ctx.model.nodes[event['id']][step['node']]
        entry = set(held)
        held.update(node.get('EnterSet', []))
        visible = set(held)
        choice = node['Choices'][step['index']]
        held.update(step.get('set', choice.get('Set', [])))
        rows.append(dict(address=event['id'] + '/' + step['node'], step=i,
                         before_entry=sorted(entry), visible=sorted(visible), after_choice=sorted(held),
                         choice_index=step['index'], paragraphs=step['paragraphs'],
                         choice_gates={k: choice[k] for k in ('Requires', 'Forbids', 'Mythic', 'Check', 'RemoveItem', 'Crusade') if k in choice},
                         paragraph_gates=[dict(index=p, **{k: node['Paragraphs'][p].get(k, []) for k in ('Requires', 'Forbids', 'AnyGroups')}) for p in step['paragraphs']]))
    if event.get('end_node'):
        end = event['end_node']; node = ctx.model.nodes[event['id']][end['node']]
        entry = set(held); held.update(node.get('EnterSet', []))
        rows.append(dict(address=event['id'] + '/' + end['node'], step=len(rows),
                         before_entry=sorted(entry), visible=sorted(held), after_choice=None,
                         choice_index=None, paragraphs=end['paragraphs']))
    return rows


def visible_words(ctx, event):
    nodes = ctx.model.nodes[event['id']]
    spans = []
    for step in event['steps'] + ([event['end_node']] if event.get('end_node') else []):
        node = nodes[step['node']]
        text = node.get('Text', '') + ' ' + ' '.join(node['Paragraphs'][p]['Text'] for p in step['paragraphs'])
        spans.append(len(text.split()))
    answers = sum(len(nodes[s['node']]['Choices'][s['index']]['Text'].split()) for s in event['steps'])
    return sum(spans) + answers, max(spans, default=0)


def timeline(ctx, chapter, items, trace):
    scenes = [it for it in items if it[0] == 'scene']
    windows = collections.Counter(it[1]['hour'] for it in scenes)
    lines = ['# Whole-chapter timeline: ' + str(chapter), '',
             'Evidence level: simulated. Days/gaps are simulated, not in-game pacing or access proof.',
             'Node states are export replay; scene before/after states are trace-recorded.',
             'Checks always succeed; resources, area and contacts are assumed. Unvisited branches are uncovered.',
             'Native keys scheduled by the kit and derived world state are not played native-choice history.', '',
             '| Event | Day/hour | Origin | Address | Delivery | Words | Longest text span before choice | Choices with distinct exported outcomes | Costs / checks | Setup/payoff flags |',
             '|---|---|---|---|---|---|---|---|---|---|']
    total_words, longest, remote, distinct = 0, 0, 0, 0
    producers = {}
    for kind, ev, state in items:
        ref = 'trace.json#/events/' + str(ev['_ordinal'])
        if kind != 'scene':
            native = [f for f in ev['on'] + ev['off'] if f in ctx.model.native]
            authored = [f for f in ev['on'] + ev['off'] if f not in ctx.model.native]
            lines.append('| %s | %s/%s | scheduled native / derived (earning unknown) | native: %s; other: %s | world | - | - | - | - | on %s; off %s |' %
                         (ref, ev['day'], ev['hour'], ', '.join(native), ', '.join(authored), ', '.join(ev['on']), ', '.join(ev['off'])))
            for f in ev['on']: producers[f] = ref
            for f in ev['off']: producers.pop(f, None)
            continue
        scene = ctx.model.by_id[ev['id']]
        words, span = visible_words(ctx, ev)
        total_words += words; longest = max(longest, span); remote += bool(ev['remote'])
        count, costs, links = 0, [], []
        states = node_states(ctx, ev, state)
        for step, snap in zip(ev['steps'], states):
            node = ctx.model.nodes[ev['id']][step['node']]
            visible = set(snap['visible'])
            signatures = set()
            for c in node['Choices']:
                if all(f in visible for f in c.get('Requires', [])) and not any(f in visible for f in c.get('Forbids', [])):
                    signatures.add(json.dumps({k: c.get(k) for k in ('Next','Set','Abort','Check','Crusade','RemoveItem','StartEtude','NativeNext','Revive')}, sort_keys=True))
            count += len(signatures) > 1
            c = node['Choices'][step['index']]
            if step.get('crusade'): costs.append('resource effect ' + json.dumps(step['crusade'], sort_keys=True))
            if c.get('RemoveItem'): costs.append('item removal (export; runtime inventory unproved)')
            if step.get('check'): costs.append('check success (assumed); failure uncovered')
            for f in c.get('Requires', []): links.append(f + ' <- ' + producers.get(f, 'earlier/unknown'))
        distinct += count
        for f in scene.get('Requires', []): links.append(f + ' <- ' + producers.get(f, 'earlier/unknown'))
        lines.append('| %s | %s/%s | authored mod scene; native-key effects: %s | `%s` | %s | %s | %s | %s | %s | %s |' %
                     (ref, ev['day'], ev['hour'], ', '.join(f for f in ev['set'] if f in ctx.model.native) or 'none',
                      ev['id'], 'remote' if ev['remote'] else 'physical (assumed)', words, span, count,
                      '; '.join(costs) or 'none', '; '.join(dict.fromkeys(links)).replace('|', '\\|') or 'none'))
        for f in ev['set']: producers[f] = ev['id']
        for f in ev.get('unset', []): producers.pop(f, None)
    hours = sorted(windows)
    gaps = [b - a for a, b in zip(hours, hours[1:])]
    lines += ['', '- Scenes per delivery window (simulated hour): ' + str(dict(sorted(windows.items()))),
              '- Visible words (includes chosen answers): ' + str(total_words),
              '- Longest uninterrupted node text: ' + str(longest) + ' words (native transitions unmodelled).',
              '- Choices with distinct exported outcomes: ' + str(distinct) + ' (alternative outcomes uncovered; native/Mythic/item access unproved).',
              '- Remote/physical mix: %d/%d (physical access assumed).' % (remote, len(scenes) - remote),
              '- Largest simulated delivery gap: ' + str(max(gaps, default=0)) + ' hours.',
              '- Missed windows: unknown; unvisited scenes are not proof of a missed legal window.',
              '- Required route beats: unknown (no declared beat matrix in trace/1).',
              '- Trace-declared skipped scenes (run-wide): ' + json.dumps(trace['summary'].get('skipped_scenes', 'unknown'), ensure_ascii=False), '']
    return '\n'.join(lines)
