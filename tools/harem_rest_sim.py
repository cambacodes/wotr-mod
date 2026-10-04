"""ER-H3 conditional E9 household load, with every schedule row instantiated.

This is a planning fixture, never shipped content or proof of a native route.
A Tier 3 walk supplies eligibility/gate hours; --conditional exposes the approved day-24 budget assumption.
"""
import argparse
import copy
import json
import math
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from story_format import c, n, p, scene
from tools import rrt_verify as e9

SCHEDULE = ROOT / 'tools/harem-schedule.json'


def roster_fixture(story, data):
    """Instantiate every row and its outcome paragraphs, including inactive/retired reservations.
    Physical dockets use ordinary nodes; conditional paragraphs belong only to the epilogue page.
    Packet nodes contain every child's terminal answers, rather than two representative children.
    """
    fixture = copy.deepcopy(story)
    paragraphs, singletons = [], {}
    for row in data['schedule']:
        ref = row['ref'].lower()
        resolved, unsettled = ('household.protected.' + ref + '.' + outcome for outcome in ('resolved', 'unsettled'))
        docket = scene('harem.sim.' + ref, row['ref'], 'Seelah', row['chapter'], '[Docket]',
                       [n('start', 'Narrator', '{n}' + row.get('note', row['ref']) + '{/n}',
                          c('Settle', flags=(resolved,)), c('Unsettled', flags=(unsettled,)), c('Later', abort=True))],
                       last=row['chapter'], Relationship='household', RestAllowance='household.protected')
        # Reservations that do not emit a new household scene remain in the reproducer for validator coverage.
        docket['ManualOnly'] = False
        docket['Chapters'] = [row['chapter']]
        if row['chapter'] in (3, 5):
            docket['InteractionHub'] = 'household.table'
        else:
            docket.update(Remote=True, Kind='event', RestAllowance=None)
        singletons[row['ref']] = docket
        fixture['Scenes'].append(docket)
        paragraphs.extend((p('{n}%s: settled.{/n}' % row['ref'], requires=(resolved,)),
                           p('{n}%s: unsettled.{/n}' % row['ref'], requires=(unsettled,))))
    for packet in data['packets']:
        nodes = []
        for i, child in enumerate(packet['children']):
            original = copy.deepcopy(singletons[child]['Nodes'][0])
            original['Id'] = child.lower()
            for choice in original['Choices']:
                if not choice['Abort']:
                    choice['Next'] = packet['children'][i + 1].lower() if i + 1 < len(packet['children']) else None
            nodes.append(original)
        fixture['Scenes'].append(scene('harem.sim.packet.' + packet['id'].lower(), packet['name'], 'Seelah', 5,
                                       '[Docket]', nodes, last=5, Relationship='household',
                                       InteractionHub='household.table', RestAllowance='household.protected'))
    fixture['Scenes'].append(scene('harem.sim.outcomes', 'Docket outcomes', 'Epilogue', 5, '',
                                   [n('start', 'Narrator', '{n}The docket is kept.{/n}', c(), paragraphs=paragraphs)],
                                   last=6, Relationship='household'))
    return fixture


def simulate(story, data, route_run, *, arrivals=None, gate_hours=None, cadence=16, conditional=False,
             rematch=False, fallback=False, late_s06=False):
    """Share E9 rests with route letters; protected and pair allowances run concurrently.
    Eligibility and named obligation gates come from the walk, never from an outcome's proposed flag name.
    """
    start5 = sum(float(route_run['chapter_days'].get(ch, 0)) * 24 for ch in range(5))
    arrivals = dict(arrivals or route_run.get('eligible_hours', {}))
    gate_hours = gate_hours or {}
    if conditional:
        deadline = start5 + 24 * 24
        for rel in story['Relationships']:
            arrivals[rel] = deadline  # Exercise the latest permitted arrival, rather than an easier early roster.
        for woman, seat in data['seat_women'].items():
            arrivals[woman] = arrivals.get(seat, deadline)
        # The ideal S06 acknowledgment is in Ch4; its late reunion is a separately reported fallback.
        start4 = sum(float(route_run['chapter_days'].get(ch, 0)) * 24 for ch in range(4))
        for woman in ('minagho', 'chivarro'):
            arrivals[woman] = min(arrivals[woman], start4)
    def arrival(woman):
        return arrivals.get(woman, arrivals.get(data['seat_women'].get(woman)))
    pending, blocked, completed = [], [], {}
    for order, row in enumerate(data['schedule']):
        if not row.get('count') or row.get('status') == 'retired':
            continue
        if row.get('keys') == ['arueshalae.corrupted']:
            continue  # redeemed ideal profile; branch alternatives are exercised in the roster fixture
        chapter = row['chapter']
        if row['ref'] == 'S06.ack' and late_s06:
            chapter = 5
        times = [arrival(woman) for woman in row['women']]
        reads = row.get('reads', [])
        absent = [woman for woman, time in zip(row['women'], times) if time is None]
        if not conditional:
            absent += [key for key in reads if key not in gate_hours]
        if absent:
            blocked.append(dict(ref=row['ref'], missing=absent))
            continue
        chapter_start = sum(float(route_run['chapter_days'].get(ch, 0)) * 24 for ch in range(chapter))
        ready = max([chapter_start] + [time for time in times if time is not None] + [gate_hours[key] for key in reads if key in gate_hours])
        pending.append(dict(ref=row['ref'], order=order, chapter=chapter, ready=ready, allowance='household.protected', children=[row['ref']]))
    # A packet is one slot only when all its children are ready; fallback never strands a later child.
    if not fallback:
        for packet in data['packets']:
            kids = [entry for entry in pending if entry['ref'] in packet['children']]
            if len(kids) == len(packet['children']):
                pending = [entry for entry in pending if entry not in kids]
                pending.append(dict(ref=packet['id'], order=min(entry['order'] for entry in kids), chapter=5, ready=max(entry['ready'] for entry in kids),
                                    allowance='household.protected', children=packet['children']))
    pair_arrival = [arrival(woman) for woman in ('seelah', 'wenduag')]
    pair_ready = max(pair_arrival) if all(time is not None for time in pair_arrival) else None
    pair_steps = ['spar'] + (['rematch'] if rematch else []) + ['watch', 'restraint', 'stood', 'debt_repayment', 'choice', 'morning']
    pair_index, pair_hour = 0, pair_ready
    if pair_ready is None:
        blocked.append(dict(ref='S02.arc', missing=['seelah/wenduag eligibility']))
    chapters = []
    for chapter in (4, 5):
        chapter_start = sum(float(route_run['chapter_days'].get(ch, 0)) * 24 for ch in range(chapter))
        hours = float(route_run['chapter_days'][chapter]) * 24
        end = chapter_start + hours
        rests = int(hours // cadence)
        slots, route = [], next(row for row in route_run['chapters'] if row['chapter'] == chapter)
        if chapter == 4:
            # Ch4 has no Table. S06 is a rest-delivered acknowledgment, charged alongside its four letters.
            eligible = [entry for entry in pending if entry['chapter'] == 4 and entry['ready'] < end]
            for entry in eligible:
                completed[entry['ref']] = max(chapter_start + cadence, entry['ready'])
                pending.remove(entry)
            acknowledgment_beats = len(eligible)
        else:
            acknowledgment_beats = 0
        reservations = [('reserved.optional.%d' % i) for i in range(10)] + [('reserved.mend.%d' % i) for i in range(4)]
        dynamics = ['reserved.dynamic.%d' % i for i in range(3)]
        for hour in range(int(chapter_start + cadence), int(end) + 1, cadence):
            if chapter != 5:
                continue
            # The pursuing player selects S02 early, and its earned rematch when due, from the full Table menu.
            rematch_due = (pair_hour is not None and pair_index < len(pair_steps)
                           and pair_steps[pair_index] == 'rematch' and hour >= pair_hour)
            protected = sorted((entry for entry in pending if entry['chapter'] == chapter and entry['ready'] <= hour),
                               key=lambda entry: (entry['ref'] != 'S02', entry['order']))
            chosen = protected[:1 if rematch_due else 2]
            for entry in chosen:
                pending.remove(entry)
                for ref in entry['children']:
                    completed[ref] = hour
                slots.append((hour, 'household.protected', entry['ref']))
            protected_used = len(chosen)
            pair_used = False
            # S02 is already in the protected docket above; the optional arc starts after its settlement.
            if pair_hour is not None and pair_index < len(pair_steps) and hour >= pair_hour:
                step = pair_steps[pair_index]
                if step == 'spar' and 'S02' not in completed:
                    continue
                if step == 'spar':
                    done = completed['S02']
                elif step == 'rematch':
                    if protected_used >= 2:
                        continue
                    done = hour
                    slots.append((hour, 'household.protected', 'S02.rematch'))
                    protected_used += 1
                else:
                    done = hour
                    slots.append((hour, 'household.pair', 'S02.' + step))
                    pair_used = True
                completed['S02.' + step] = done
                pair_index += 1
                pair_hour = done + (8 if pair_index < len(pair_steps) and pair_steps[pair_index] == 'morning' else 48)
            if pair_ready is not None and hour >= pair_ready:
                if not pair_used and reservations:
                    slots.append((hour, 'household.pair', reservations.pop(0)))
                while protected_used < 2 and dynamics:
                    slots.append((hour, 'household.protected', dynamics.pop(0)))
                    protected_used += 1
        protected_beats = sum(kind == 'household.protected' for _, kind, _ in slots)
        optional_beats = sum(kind == 'household.pair' for _, kind, _ in slots)
        # Reserve all other optional/mending/flavour load in the same allowance, not just the worked pair's six steps.
        reserved_pair = 20 if chapter == 5 else 0
        protected_total = protected_beats
        letters = data['load_caps'].get(str(chapter), {}).get('letters', 0)
        needed = max(route['rests_needed'] + letters, math.ceil(protected_total / 2), reserved_pair)
        missed = [entry['ref'] for entry in pending if entry['chapter'] == chapter]
        if chapter == 5:
            missed += reservations + dynamics
        chapters.append(dict(chapter=chapter, household_beats=protected_beats + optional_beats + letters + acknowledgment_beats,
                             protected=protected_beats, optional=optional_beats, letters=letters,
                             acknowledgments=acknowledgment_beats,
                             reserved_pair=reserved_pair, rests_available=rests, rests_needed=needed,
                             load=round(needed / max(1, rests), 3), deadline_misses=missed, slots=slots))
    return dict(conditional=conditional, rematch=rematch, fallback=fallback, blocked=blocked, chapters=chapters,
                completed=completed, pair_complete='S02.morning' in completed,
                pair_eligibility=pair_ready, paragraphs=2 * len(data['schedule']))


def report(result, emit=print):
    emit('ER-H3 %s load model; spar %s; packets %s' %
         ('conditional' if result['conditional'] else 'walk-timed', 'rematch' if result['rematch'] else 'success',
          'fallback' if result['fallback'] else 'consolidated'))
    for row in result['chapters']:
        emit('Ch%d: %d household beats, %d/%d rests needed/available, load %.3f, deadline misses %s' %
             (row['chapter'], row['household_beats'], row['rests_needed'], row['rests_available'], row['load'], row['deadline_misses']))
    emit('S02 morning completed: %s; eligibility hour: %s; blocked rows: %d; instantiated paragraphs: %d' %
         (result['pair_complete'], result['pair_eligibility'], len(result['blocked']), result['paragraphs']))


# eng7-l11: acceptance inventory consumes W0c contracts; reservations never prove delivery.
def inventory_acceptance(story, data, expectations, walk=None):
    from tools import harem_schedule_lint as schedule_lint, harem_smoothing_lint as smoothing_lint
    errors, _ = schedule_lint.lint(data, story)
    blockers = []
    for key, expected in expectations['expected_schedule_counts'].items():
        if data['expected_counts'].get(key) != expected:
            errors.append('schedule census changed: ' + key)
    for profile in ('ideal', 'worst'):
        total = sum(row[profile] for row in expectations['chapter_ceilings'].values())
        if total != expectations['campaign_ceilings'][profile]:
            errors.append('campaign ceiling does not equal chapter ceilings: ' + profile)
    caps = data['load_caps']['5']
    rests = max(math.ceil(data['expected_counts']['consolidated'] / story['RestAllowances']['household.protected']),
                math.ceil((caps['optional'] + caps['mend']) / story['RestAllowances']['household.pair']))
    if rests != expectations['chapter5_min_table_rests']:
        errors.append('Chapter 5 Table allowance arithmetic changed')
    smoothing = smoothing_lint.load_json(smoothing_lint.DEFAULT_DATA)
    _, _, frictions = smoothing_lint.household_maps()
    _, census = smoothing_lint.form_audit(smoothing, frictions, data['packets'])
    for key, expected in expectations['expected_form_census'].items():
        if census[key] != expected:
            errors.append('form census changed: ' + key)
    if census['unapproved_forms'] or census['over_cap_forms']:
        errors.append('form cap or vocabulary violated')
    by_id = {scene['Id']: scene for scene in story['Scenes']}
    active = [row for row in data['schedule'] if row.get('count') and row.get('status') != 'retired']
    for row in active:
        ids = expectations['row_scene_ids'].get(row['ref'], [])
        if not ids:
            blockers.append('build-sheet scene missing: ' + row['ref'])
        for sid in ids:
            scene = by_id.get(sid)
            if not scene or not scene.get('HouseholdCategory'):
                errors.append('row bound to an absent or unregistered scene: ' + row['ref'] + '/' + sid)
            elif scene.get('HouseholdCategory') == 'protected' and scene.get('RestAllowance') != 'household.protected':
                errors.append('protected row has wrong allowance: ' + sid)
    enmity_producers = [scene['Id'] for scene in story['Scenes'] for node in scene['Nodes']
                       for choice in node['Choices'] if any('.harem.enmity.' in flag for flag in choice.get('Set', []))]
    if not enmity_producers:
        blockers.append('first-wins acceptance: no serialized enmity producers (consume q6a L1-L6 when landed)')
    # Existing E9 automatically schedules earliest native progress. Always label that assumption.
    route_run = e9.simulate_rest_budget(e9.Model(story))
    if not walk:
        blockers.append('Tier-3 S9 native eligibility/gate-hour walk missing')
    else:
        arrivals, gates = walk.get('eligibility_hours', {}), walk.get('gate_hours', {})
        for woman in sorted({w for row in active for w in row['women']}):
            if woman not in arrivals and data['seat_women'].get(woman) not in arrivals:
                blockers.append('native eligibility timestamp missing: ' + woman)
        for key in sorted({key for row in active for key in row.get('reads', [])}):
            if key not in gates:
                blockers.append('native gate timestamp missing: ' + key)
    return dict(status='failed' if errors else 'data_blocked' if blockers else 'ready_for_native_walk',
                errors=errors, blockers=blockers, form_census=census, chapter5_min_table_rests=rests,
                active_rows=len(active), actual_table_beats={row['chapter']: row['table_beats'] for row in route_run['chapters']},
                native_progress_assumed=True, certified=False)
# end eng7-l11


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--story', default=str(ROOT / 'development/Story.json'))
    parser.add_argument('--walk', help='Tier 3 export containing eligibility_hours and gate_hours')
    parser.add_argument('--conditional', action='store_true', help='Explicitly assume the full roster eligible by Ch5 day 24; no reachability proof')
    parser.add_argument('--sim-natives', help='E9 key:chapter progress export')
    parser.add_argument('--reproducer', help='Write a full in-memory roster fixture to this allowed output path')
    # eng7-l11
    parser.add_argument('--inventory', action='store_true', help='Report missing build-sheet/native inputs; never certify reservations')
    # end eng7-l11
    args = parser.parse_args(argv)
    story = json.loads(Path(args.story).read_text(encoding='utf-8-sig'))
    data = json.loads(SCHEDULE.read_text(encoding='utf-8'))
    fixture = roster_fixture(story, data)
    model = e9.Model(story)
    natives = dict((key, int(chapter)) for key, chapter in (item.split(':') for item in args.sim_natives.split(','))) if args.sim_natives else {}
    route_run = e9.simulate_rest_budget(model, natives=natives)
    walk = json.loads(Path(args.walk).read_text(encoding='utf-8')) if args.walk else {}
    # eng7-l11
    if args.inventory:
        expectations = json.loads((ROOT / 'tools/harem_inventory_scenarios.json').read_text(encoding='utf-8'))
        result = inventory_acceptance(story, data, expectations, walk)
        print(json.dumps(result, indent=2))
        return 1 if result['errors'] or result['blockers'] else 0
    # end eng7-l11
    if args.reproducer:
        target = Path(args.reproducer).resolve()
        # eng7-l11: audit artifacts belong outside the checkout.
        if not target.is_relative_to(Path(tempfile.gettempdir()).resolve()) or target.is_relative_to(ROOT):
            parser.error('--reproducer must write in the system temporary directory, outside the repository')
        # end eng7-l11
        target.write_text(json.dumps(fixture, ensure_ascii=False, indent=2), encoding='utf-8')
    passed = True
    for rematch in (False, True):
        result = simulate(story, data, route_run, arrivals=walk.get('eligibility_hours'), gate_hours=walk.get('gate_hours'),
                          conditional=args.conditional, rematch=rematch)
        report(result)
        passed &= result['pair_complete'] and not result['blocked'] and all(
            not chapter['deadline_misses'] and chapter['load'] <= 1 for chapter in result['chapters'])
    if not args.walk:
        print('NOTE: tools/fixtures/all-romance-run.json / S9 native walk is not supplied. This does not certify native reachability.')
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
