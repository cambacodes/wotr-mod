"""Authored shared-clock bindings for approved rulings 08, 09 and 42.

Only the named predecessor deeds start these waits. Body/presence requirements
remain availability gates; existing save flags and hour keys retain their IDs.
"""
from story_format import c, n
from storylines.delamere_trickster import HUNT_POSTPONED, SECOND_HUNT
from storylines.harem_rows import s50, s51


def integrate(story):
    for scene in story['Scenes']:
        sid = scene['Id']
        if sid.startswith(s50.P):
            step = sid[len(s50.P):].split('.')[0]
            if step == 'custody':
                scene['DelayClocks'] = [s50.P + 'notice.opened']
            elif step == 'repair':
                scene['DelayClocks'] = [s50.P + 'custody.failed', s50.P + 'custody.refused']
            if step in ('custody', 'repair'):
                paid = next(choice for node in scene['Nodes'] for choice in node['Choices']
                            if (choice.get('Crusade') or {}).get('Amount', 0) < 0)
                paid['PostPayment'] = 'paid_delivery'
                # New authored aftermath; original nodes/answers and pre-debit
                # narration remain byte-for-byte intact.
                scene['Nodes'].append(n('paid_delivery', 'Nidalynn',
                    '''{n}The hired men bring the cart to the kiln. Nidalynn opens the sacks, lifts out a piece of goat meat and checks beneath it. Arrows clatter on the wall above.{/n}
"Whole. That's the load I chose. Put it inside; I'll cut it before she starts biting the sacks."
{n}She carries her own bowl through the door and pulls it shut against the scrape of claws.{/n}''',
                    c('[Leave the feed with her.]', abort=True)))
        elif sid.startswith(s51.P):
            step = sid[len(s51.P):].split('.')[0]
            clocks = {'cell': ['notice.carried'], 'retry': ['cell.failed', 'cell.refused'],
                      'receipt': ['cell.chart_erased']}.get(step)
            if clocks:
                scene['DelayClocks'] = [s51.P + key for key in clocks]
        if sid in ('delamere.trickster.woods.second_hunt',
                   'delamere.trickster.woods.second_hunt_page',
                   'delamere.trickster.woods.second_hunt_late'):
            scene['DelayClocks'] = [SECOND_HUNT, HUNT_POSTPONED]
            for node in scene['Nodes']:
                for choice in node['Choices']:
                    if HUNT_POSTPONED in choice['Set']:
                        choice['RefreshTimes'] = [HUNT_POSTPONED]
