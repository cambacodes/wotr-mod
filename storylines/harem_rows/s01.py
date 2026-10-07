"""S01: authored patrol/snare incident; native contempt is a voice anchor only.

Reviewed contract: hs-B/sheets/B.md S01, corrected by harem-lore-check.md.
No return, romance, partner stance, enmity or reconciliation is produced here.
The primary and its one retry each charge the existing protected allowance.
"""
from story_format import c, n, scene
from storylines import household

PREFIX = "household.pair.camellia_wenduag."
PAIR = ("camellia", "wenduag")


def p(suffix):
    return PREFIX + suffix


DEEDS = tuple(map(p, ("deed.camellia_approach", "deed.wenduag_hunters_moved",
                     "cost.camellia_mask_read", "cost.wenduag_plan_yielded")))
SUCCESS = DEEDS + (p("cost.commander_snare_labour"),)
# Reader groups belong to registration, never to answer effects. No warmer stage.
LADDER = {
    a + ".harem.attitude." + b + "." + stage: [list(receipts)]
    for a, b in (PAIR, PAIR[::-1])
    for stage, receipts in (("rival", (p("settle.seen"),)), ("respect", DEEDS))
}


def _nodes(retry):
    if retry:
        opening = '''{n}At the Table, Wenduag drops a length of snare wire beside Camellia's glass. The loop has caught nothing. Camellia moves her wine out of its reach.{/n}
"The cultists still use the covered alley," {n}Camellia says.{/n} "Unless you intend to wait until they die of old age?"
"My hunters are watching it. They haven't moved the trap." {n}Wenduag bares her teeth.{/n} "Come and turn it. This time, keep your eyes where she points."'''
        choices = (
            c('[Reset the same snare and wait with them.]', 'reversed'),
            c('"I am done with this snare."', 'refused'),
            c('"Later."', abort=True),
        )
    else:
        opening = '''{n}Wenduag spreads a rough street plan across the Table. Two crusade scouts wait nearby. She taps the approach to a ruined courtyard in Drezen's lower town.{/n}
"A cult patrol. Armed. My hunters will drive them onto the wire."
"How industrious." {n}Camellia's finger settles on the covered alley behind the courtyard.{/n} "But that is where they will come from. The other street exposes their backs."
"You sound very sure, princess," {n}Wenduag says.{/n}
"Then come and look. You may learn something." {n}Camellia smooths her glove. Wenduag rolls up the plan with a sharp jerk.{/n}'''
        choices = (
            c('[Turn the snare toward the approach Camellia identifies.]', 'reversed'),
            c('"Leave it facing the old approach."', 'missed'),
            c('"I am leaving this to the garrison."', 'refused'),
            c('"Later."', abort=True),
        )
    step = 'retry' if retry else 'settle'
    nodes = [n('start', 'Narrator', opening, *choices),
             n('reversed', 'Narrator', '''{n}In the courtyard, Camellia crouches beside the wire without letting her skirt touch the mud. She lifts the loop and points to a scrape beneath the alley arch.{/n}
"There. Shoulder height, when the foot catches. Not the neck. You would pull it loose."
{n}Wenduag watches her hands, then signals the scouts onto the flanking roofs herself.{/n}
"Keep pointing. I'll move my hunters."
{n}You drag the anchor round, drive it between the stones and haul the wire taut. By the time you take cover, your palms are raw. Boots scrape in the alley. The first cultist falls hard; the scouts' bolts drive his companions back against the wall.{/n}
"Your quarry would have admired it from the other street," {n}Camellia murmurs.{/n}
"You know how to make something struggle." {n}Wenduag studies her instead of the fallen man. Camellia pulls her glove straight.{/n} "I'll remember that."
"Remember the alley. Your hunters are waiting for you."''',
               c('[Return to the Table.]', flags=(p(step + '.seen'), p(step + '.done'))
                 + (() if not retry else (p('settle.done'),)) + SUCCESS)),
             n('refused', 'Narrator', '''{n}The garrison takes over the watch. Camellia withdraws her hand from the plan.{/n}
"Perhaps their sergeant will listen."
"Let him waste his men on your advice, then." {n}Wenduag snatches up the wire. Neither woman offers to stay with the other.{/n}''',
               c('[Leave the quarrel unsettled.]', flags=(p(step + '.seen'), p(step + '.refused'), p('unsettled'))))]
    if not retry:
        nodes.append(n('missed', 'Narrator', '''{n}You leave the snare across the open street. Wenduag sends the scouts to cover it. Camellia waits beside the alley, well clear of the wire.{/n}
{n}The patrol comes under the arch. A boot scuffs stone; Wenduag turns too late. Crossbow bolts strike the courtyard wall. The scouts duck, and the cultists slip back through the covered passage. One of them whistles a warning.{/n}
"There goes your fine ambush." {n}Camellia brushes stone dust from her sleeve.{/n}
"I saw." {n}Wenduag jerks her chin at the scouts.{/n} "Watch the alley. Leave the wire where it is. They'll look for us now."
{n}The old approach is useless. Camellia walks past Wenduag without another word.{/n}''',
                       c('[Keep the approach watched.]', flags=(p('settle.seen'), p('settle.failed'),
                                                               p('cost.commander_approach_lost')))))
    return nodes


def _scene(retry):
    step = 'retry' if retry else 'settle'
    enmities = tuple(household.enmity(a, b) for a, b in (PAIR, PAIR[::-1]))
    requires = ('trickster', 'trickster.now', household.PAGE_TAKEN, household.STANCE_ELIGIBLE,
                household.KEPT, 'camellia.harem.eligible', 'wenduag.harem.eligible',
                'camellia.present_now', 'wenduag.present_now', p('settle.failed') if retry else p('ready'))
    forbids = ('fool_king.gone', 'trickster.failed', 'camellia.closed', 'wenduag.closed',
               'camellia.epoch_unavailable', 'wenduag.epoch_unavailable',
               'camellia.returned_actor_lost', 'wenduag.returned_actor_lost',
               'wenduag.trickster.echo.abyss.unavailable', 'sacrifice', p(step + '.seen')) + enmities
    if retry:
        forbids += (p('settle.done'), p('unsettled'))
    overrides = {household.enmity(a, b): a + '.harem.reconciled.' + b for a, b in (PAIR, PAIR[::-1])}
    overrides['sacrifice'] = 'trickster.commander_back'
    return scene(p(step), 'The snare facing the wrong way', 'Camellia', 5,
                 '[Camellia and Wenduag: reset the snare.]' if retry else '[Camellia and Wenduag: the cult patrol.]',
                 _nodes(retry), requires=requires, forbids=forbids, delay=48 if retry else 0, last=5,
                 Relationship='household', Chapters=[5], Areas=[household.DREZEN],
                 InteractionHub=household.TABLE_HUB, Participants=list(PAIR), Pair=list(PAIR),
                 ParticipantWomen=[], RestAllowance='household.protected', HouseholdCategory='protected',
                 HouseholdWitness=p(step + '.seen'), ForbidOverrides=overrides)


def register(payload, scenes, refs):
    """Append this row once; supports the pre-household discovery hook."""
    derived = payload.setdefault('Derived', {})
    derived[p('ready')] = [[w + suffix for w in PAIR for suffix in ('.harem.eligible', '.present_now')]]
    # The household integrator reads these witnesses; no answer creates a stage.
    derived.update(LADDER)
    # The shared registry has not reserved S01's directions yet. Declare the
    # controller-owned inputs without supplying an enmity/failure producer.
    pending = payload.setdefault('PendingHooks', [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (household.enmity(a, b), a + '.harem.reconciled.' + b):
            if key not in pending:
                pending.append(key)
    have = {s['Id'] for s in scenes}
    for retry in (False, True):
        body = _scene(retry)
        if body['Id'] not in have:
            scenes.append(body)
        household.CONSUMERS[body['Id']] = household.PAGE_TAKEN
