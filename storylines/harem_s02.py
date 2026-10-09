"""Authored S02 incidents; execute the reviewed pair sheet, not new mechanics.

Canon anchors and staging limits: household_pair_seelah_wenduag.EVIDENCE.
Registration uses the existing household API; state belongs to story.py.
"""
from story_format import c, n
from storylines import household as hh, household_pair_seelah_wenduag as sheet

P = sheet.P
SLOT = P("choice.explicit.1")
LABELS = dict(spar='First blood', rematch='One last bout', watch='The false trail',
              restraint='A bound enemy', stood='The blade on the bank',
              debt_repayment='The extraction watch', choice='The unfinished bout', morning='Morning muster')


def page(id, speaker, text, *answers):
    return n(id, speaker, text, *answers, portrait=speaker if speaker != "Narrator" else "Seelah")


def terminal(id, speaker, text, flags):
    return page(id, speaker, text, c("Continue", flags=flags))


# Every account is enacted on the selected branch, before its terminal receipt.
OPENINGS = {
    "spar": ('Seelah', '{n}Seelah plants her shield beside the Table. Wenduag kicks two stools apart, marking a ring.{/n}\n"The cult patrols can wait for us to finish supper. Apparently Wenduag can’t."\n{n}Wenduag rolls her shoulders.{/n} "You carry that shield everywhere. Let us see what you can do without it."'),
    "rematch": ('Wenduag', '"The paladin still has both hands. I still have mine. Your tavern survived. What is stopping us?"\n{n}Seelah draws a chalk line around the cleared floor.{/n} "One nick. Then we stop. There are wounded soldiers who need the healers more than we do."'),
    "watch": ('Wenduag', '"Rusk. A scout captain for the cult. He drove me into a gully and put arrows through both ways out. I crawled under his dead to escape."\n{n}She spreads a patrol sketch on the Table. Three crusade scouts lean closer.{/n} "Some of his archers escaped me. They will come back. I need hunters who can follow a false trail without trampling it flat."\n{n}Seelah turns the sketch toward the scouts.{/n} "And someone to hold the road when the trap closes. I’ll do that."'),
    "restraint": ('Seelah', '{n}On the reconnaissance run, Rusk takes the bait. Now he kneels bound beside the road; Wenduag catches his smallest finger in her fist. Seelah grips her wrist.{/n}\n"No. He’s beaten. Put the knife away."\n"He left me bleeding in a ditch. My hunters should see what happens to a man who tries that." {n}Wenduag snarls.{/n}\n"They can see you bring him back alive. I’ll take his first watch myself." {n}Seelah answers.{/n}'),
    "stood": ('Wenduag', '{n}At the outer ditch, a cult archer rises behind Wenduag. Seelah shoves her aside and takes the blade across her upper arm. A second scout drops from the bank, cutting off their retreat.{/n}\n"Move!" {n}Seelah braces her shield against him. Blood runs into her glove. Wenduag reaches for an arrow, but the paladin is in her line of fire.{/n}'),
    "debt_repayment": ('Seelah', '"Rusk’s scouts have been seen near the wall. I want you on his watch tonight."\n{n}Wenduag’s claws scrape the Table.{/n} "Tonight was my hunt. I chose the ground. I laid the bait."\n"You told me you owed me a dangerous watch. This is the one." {n}Seelah says.{/n}\n{n}Wenduag pushes her hunting sketch aside.{/n} "Then I will bring my hunters. Rusk will hear them outside his door all night."'),
    "choice": ('Wenduag', '{n}At the lower-wall watch post, Wenduag catches Seelah’s belt as she passes. The paladin turns, grinning, and pins the hunter’s wrist against the stone.{/n}\n"Our bout was unfinished," {n}Wenduag says.{/n} "You stopped just when it grew interesting."\n"First blood. Remember?" {n}Seelah says.{/n}\n"I remember your hands." {n}Wenduag answers.{/n}\n{n}A horn sounds from the far wall. Seelah looks toward the stairs, then back at Wenduag.{/n} "We’re still on watch."'),
    "morning": ('Seelah', '{n}Seelah finishes her morning prayer beside the tower’s narrow window. Below, Wenduag’s hunters bring Rusk back from questioning, alive and with both hands whole.{/n}\n"Still praying after last night?" {n}Wenduag leans in the doorway.{/n}\n"Yes. And still watching your prisoners." {n}Seelah says.{/n}\n{n}Seelah catches her belt again and pulls her close for a kiss.{/n} "You can complain on the stairs. We owe the watch a report."\n"My hunters know the rule." {n}Wenduag answers.{/n}'),
}

CHECK_TEXT = {
    "spar": (
        '{n}You hold the ring when Wenduag tries to drive Seelah through it. Seelah catches the hunter’s arm; Wenduag twists under hers. A thin red line appears on Seelah’s wrist. Both stop.{/n}\n"Fast," {n}Seelah says, laughing.{/n}\n"Strong," {n}Wenduag answers. She lets go without being pulled away.{/n}',
        '{n}You lose your footing between the stools. Wenduag follows Seelah past the line; the paladin catches her next stroke on a raised forearm and shoves her back.{/n}\n"Enough! You heard the rule." {n}Seelah shouts.{/n}\n"Then find a referee who can keep up." {n}Wenduag snaps.{/n}'),
    "rematch": (
        '{n}You see Wenduag shift her weight and call the edge of the ring before she crosses it. Seelah turns the rush, opening a shallow cut on the hunter’s shoulder. Wenduag steps back, breathing hard.{/n}\n"That one was yours, paladin." {n}Wenduag says.{/n}\n"Buy me a drink and I’ll stop enjoying it so much." {n}Seelah answers.{/n}',
        '{n}You miss the feint. Wenduag’s blow lands after Seelah has stopped; the paladin thrusts her away and takes up her shield.{/n}\n"That’s the last bout I’ll fight here." {n}Seelah says.{/n}\n"Keep your shield, then." {n}Wenduag spits into the chalk ring. Neither offers another match.{/n}'),
    "stood": (
        '{n}You slam into the scout on the bank, clearing Seelah’s retreat. She drags Wenduag behind her shield; the hunter’s arrow drops the first archer. At the Table afterward, Seelah’s sleeve is stiff with blood.{/n}\n"You stood your ground," {n}Wenduag says.{/n}\n"You were behind me." {n}Seelah answers.{/n}\n"Ask for a dangerous watch. I will take it. I won’t have you saying I hid behind you." {n}Wenduag says.{/n}',
        '{n}The scout knocks you into the ditch. Seelah holds him long enough for Wenduag to crawl clear, then scrambles after her. They return without the patrol’s trail, the paladin’s arm bound in a bloody strip of cloth.{/n}\n"We’re alive," {n}Seelah says.{/n}\n"And they know where we are." {n}Wenduag breaks the arrow she never got to loose.{/n}'),
}

RESULTS = {
    ("spar", 1): ('Seelah', '"All right. Put the stools back. There’s room for us both on tomorrow’s patrol, even if there isn’t room for this tonight."\n{n}Wenduag shoulders past the cleared ring without answering.{/n}'),
    ("rematch", 1): ('Seelah', '"Then we’re done here."\n{n}Seelah wipes away the chalk. Wenduag takes her knife and leaves for the wall. The cult patrol remains tomorrow’s business; neither asks for another bout.{/n}'),
    ("watch", 0): ('Wenduag', '{n}The scouts take Wenduag’s trail marks. On the wall that night, Seelah spots a gap in their return route; Wenduag moves the last hunter to cover it.{/n}\n"That one will live longer if he listens," {n}Seelah says.{/n}\n"He will listen. He wants to hunt with me again." {n}Wenduag says.{/n}'),
    ("restraint", 0): ('Wenduag', '{n}Wenduag releases Rusk’s finger. She turns to the scouts before Seelah can speak.{/n}\n"On our shared hunts, every enemy who yields or is taken goes alive and whole to guarded custody. No knives in the questioning. No trophies. No hunter doing it for me. And no convenient escape."\n{n}She thrusts Rusk at the guards.{/n} "Take him."\n"I’ll keep the first watch," {n}Seelah says. Wenduag watches her lead away the revenge she had caught.{/n}'),
    ("restraint", 1): ('Seelah', '"He’s bound. I won’t help you kill him."\n{n}Seelah leaves the escort. Your order is carried out before sunset. Wenduag watches Rusk hang; there is no prisoner to bring to the paladin’s watch.{/n}'),
    ("debt_repayment", 0): ('Wenduag', '{n}That night Wenduag’s hunters turn the extraction party into her waiting arrows. Seelah holds Rusk’s door. By dawn the cultists outside are dead, and the prisoner inside is breathing. Wenduag’s baited hunting ground lies untouched.{/n}\n"There. Your watch, paid in full."\n"It was," {n}Seelah answers. She hands Wenduag the patrol report to mark with her own names.{/n}'),
    ("debt_repayment", 1): ('Wenduag', '"You think I need you to arrange an accident for me?"\n{n}Wenduag bares her teeth.{/n} "My hunters heard my order. They will see me keep it."\n{n}She spends the night driving off Rusk’s rescuers while Seelah guards his door. Her own hunt is lost; the prisoner lives.{/n}\n"You heard her," {n}Seelah says to you. She signs the watch report beside Wenduag’s mark.{/n}'),
    ("debt_repayment", 2): ('Seelah', '{n}You kill Rusk before the watch can begin. Seelah pushes between you and the body, too late.{/n}\n"I asked for guards. You made me stand beside an execution."\n{n}Wenduag looks down at the dead captive.{/n} "And you spent my debt without letting me pay it. Do not offer me another gift like that."'),
    ("choice", 1): ('Seelah', '{n}Seelah releases Wenduag’s wrist, but stays beside her on the wall.{/n}\n"Then we keep the watch. Come back to the Table afterward. I’m buying."\n"You will regret saying that. I am hungry." {n}Wenduag answers.{/n}\n{n}Wenduag checks the road below, leaving her shoulder against Seelah’s.{/n}'),
    ("morning", 0): ('Wenduag', '"He stays alive. The men trying to steal him don’t."\n{n}Seelah buckles on her shield.{/n}\n"And anyone who surrenders comes back whole. I’ll be there." {n}Seelah says.{/n}\n"I know where you will stand, paladin." {n}Wenduag follows her down to the morning muster.{/n}'),
}


def nodes(step):
    name = step['id'][len(sheet.PREFIX):].split('.')[0]
    speaker, text = OPENINGS[name]
    answers, pages = [], []
    for index, outcome in step['outcomes'].items():
        if outcome.get('abort'):
            answers.append(c('"Later."', abort=True))
        elif 'check' in step and index == step.get('choice', 0):
            skill, dc = step['check']
            answers.append(c(outcome['label'], check=dict(Skill=skill, DC=dc, Success='held', Failure='failed')))
            for target, flags, prose in zip(('held', 'failed'), (step['success'], step['failure']), CHECK_TEXT[name]):
                pages.append(terminal(target, 'Narrator', prose, flags))
        elif name == 'choice' and index == 0:
            answers.append(c('"I’ll take your watch until dawn."', 'seelah_yes'))
            pages.extend([
                page('seelah_yes', 'Seelah', '"Good. Wenduag — I still won’t watch you break a prisoner. Last night didn’t change that."\n{n}She slides her hand from Wenduag’s wrist to her shoulder.{/n}\n"But I’ve been wanting to finish that bout too. Come upstairs."', c('Continue', 'wenduag_yes')),
                page('wenduag_yes', 'Wenduag', '"You still mean to get in my way."\n{n}Wenduag pulls Seelah against her. The paladin kisses her hard, then laughs into her mouth.{/n}\n"Yes." {n}Seelah answers.{/n}\n"Then you had better keep those strong hands ready." {n}Wenduag says.{/n}\n{n}Wenduag leads her toward the stairs, leaving her bow beside you.{/n}\n{n}She does not wait for the top. On the second landing she backs Seelah into the wall and takes her face in both claw-callused hands, and the paladin gives as good as she gets, armour-straps and bow-belt scattered down the stairs behind them as the hunter’s teeth find her throat and Seelah’s hands find the hunter’s hips. Their sparring has always ended in this: breath, strength, the satisfaction of being matched. Wenduag tears the paladin’s shirt open and laughs at the cry it gets out of her. Seelah hauls the hunter’s leathers up over her head and flings them down the stair. "Still on watch," Seelah gasps. "Not for the next hour," Wenduag says, and lifts her bodily through the door of the upper room.{/n}', c('Continue', SLOT)),
                page(SLOT, 'Narrator', '{n}The bout continues upstairs. Below them, you keep their watch. Beyond the wall, the cult’s signal fires burn until dawn.{/n}', c('Continue', 'held')),
                terminal('held', 'Narrator', '{n}At dawn, footsteps sound above you. Seelah comes down first, with Wenduag’s hand still hooked in her belt. They take back the watch together.{/n}', tuple(outcome['flags']) + (outcome['mutual'],)),
            ])
        else:
            target = 'result_%d' % index
            answers.append(c(outcome['label'], target))
            who, prose = RESULTS[name, index]
            pages.append(terminal(target, who, prose, outcome['flags']))
    if name == 'watch':
        # Optional knowledge comes from the played claim, never native romance
        # completion or the page. Keep the original terminal at index zero.
        flags = step['optional_reads']
        result = next(p for p in pages if p['Id'] == 'result_0')
        result['Choices'][0]['Forbids'] = list(flags)
        recalls = (
            '"Brask pointed that hand at me. I broke two of its fingers."\n{n}Seelah puts down the patrol sketch.{/n}\n"Bound, was he? Don’t expect me to stand aside for that." {n}Seelah says.{/n}\n"Then stand where I can see you, paladin. We have a hunt to finish." {n}Wenduag answers.{/n}',
            '"Brask begged my pardon on his knees. Wenduag of Neathholm. Every word."\n"Good," {n}Seelah says.{/n} "He can remember it when he opens the gate for our scouts."\n"He remembers. I make sure of that." {n}Wenduag says.{/n}',
            '"The Commander cut Brask’s hand with my knife. He shows the scar every time he salutes."\n{n}Seelah looks at you.{/n}\n"You cut a bound man? We’ll talk about that. These scouts still need their road held."\n"Then hold it," {n}Wenduag answers. She takes back the patrol sketch.{/n}',
        )
        for index, (flag, prose) in enumerate(zip(flags, recalls)):
            target = 'brask_%d' % index
            result['Choices'].append(c('Continue', target, requires=(flag,), forbids=flags[:index]))
            pages.append(terminal(target, 'Wenduag', prose, step['outcomes'][0]['flags']))
    return [page('start', speaker, text, *answers)] + pages


def register():
    """Idempotent registration before household.integrate copies its entries."""
    if any(s['Id'] == P('spar') for s in hh.ENTRIES):
        return
    sheet.validate(set(hh.PARTNERS))
    for step in sheet.STEPS:
        if step.get('kind') == 'derived':
            continue
        if step['id'] == P('invite'):
            body = hh.invitation(step['id'], 'wenduag', 'Wenduag', 'An unfinished challenge',
                '"Bring the paladin to the Table. I want a bout, and she wants rules. The cult scouts can wait while we settle which of us puts the other on the floor."',
                P('invited'), requires=('seelah.harem.eligible', 'seelah.present_now', 'wenduag.present_now'),
                forbids=(P('invite.seen'), hh.KING_GONE), chapter=5, delay=0)
            body['Participants'] = list(sheet.PAIR)
            body['Nodes'][0]['Choices'] = [c('Reply', flags=(P('invite.seen'), P('invited'))), c('"Later."', abort=True)]
            continue
        label = LABELS[step['id'][len(sheet.PREFIX):].split('.')[0]]
        body = hh.table_entry(step['id'], label,
            '[Seelah and Wenduag: %s]' % label, nodes(step), sheet.PAIR,
            P('invited'), requires=tuple(step.get('requires', ())) + ('seelah.present_now', 'wenduag.present_now'),
            forbids=tuple(step.get('forbids', ())) + (hh.KING_GONE, 'trickster.failed'),
            chapters=(5,), delay=step['delay'], RestAllowance=step['rest_allowance'],
            RequiresAnyGroups=[list(g) for g in step.get('any_groups', ())],
            HouseholdCategory='protected' if step['id'] in (P('spar'), P('rematch')) else 'pair',
            HouseholdWitness=step['seen'], HouseholdArc=P('arc'), HouseholdArcStart=step['id'] == P('watch'))
        # The later mutual answer also waits from the completed repayment deed.
        if step['id'] == P('choice'):
            body['Requires'].append(P('debt_repayment.seen'))
