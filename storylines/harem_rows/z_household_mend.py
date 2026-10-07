"""W4 mend: Camellia's existing private_precision_first_touch repair.

Authored addition; knowledge owns the learned strain input. No pair settlement,
affection, return, or stance is produced here. Sorted last to append new scenes.
"""
from story_format import c, n
from storylines import household


STRAIN = "camellia.harem.strain.galfrey.1"
MEND = "camellia.harem.mend.galfrey.1"
PREFIX = "household.smooth.camellia.galfrey_1."
SCENE_IDS = (PREFIX + "first", PREFIX + "later")


def opportunity(later=False):
    sid = SCENE_IDS[int(later)]
    attempted = sid + ".attempted"
    opening = ('''{n}Camellia sets down her wine and draws her rapier. Outside the tavern, soldiers muster for the march against the Worldwound.{/n}
"Another bout? Do try to make this one worth my time."
{n}She moves the chairs aside with her foot.{/n} "First touch. My blade, your choice of guard."''' if later else
               '''{n}Camellia draws her rapier beside the Table. Outside the tavern, soldiers muster for the march against the Worldwound. She pushes a chair out of reach of the blade.{/n}
"You have had so much to say about the queen's composure. How fortunate that you still have an evening left for mine."
{n}She lifts the point toward your sleeve.{/n} "First touch. You need not stand still for me. I would find that insulting."''')
    nodes = [
        n("start", "Camellia", opening,
          c('[Mobility] [Take your guard and fence to the first touch.]',
            flags=(attempted,), check=dict(Skill="SkillMobility", DC=22,
                                          Success="commander_touch", Failure="camellia_touch",
                                          CommanderOnly=True)),
          c('"I will keep my evening."', "refused", flags=(attempted,)),
          c('"Another time."', abort=True), portrait="Camellia"),
        n("commander_touch", "Camellia", '''{n}You turn her point aside and touch her shoulder before she can recover. Camellia lowers her blade. Her smile arrives a moment late.{/n}
"A touch. Yours. I can count, Commander."
{n}She pulls her sleeve straight and retrieves her wine.{/n} "You may boast of it, if you wish. I shall be occupied elsewhere this evening."''',
          c('[Put away your weapon.]', flags=(attempted, sid + ".commander_won")), portrait="Camellia"),
        n("camellia_touch", "Camellia", '''{n}Her point slips under your guard. A shallow cut opens above your wrist; she withdraws the blade before you can catch it. Camellia watches the bead of blood swell.{/n}
"There. Such a small thing, and all that fine composure gone."
{n}She offers you a clean handkerchief, holding it just beyond your fingers until you look up at her.{/n} "My touch. I expect you to remember whose evening this was."
{n}She sits beside you again, her rapier across her knees. Your wine waits untouched while she describes the opening you gave her.{/n}''',
          c('[Bind the nick and stay for her account of the bout.]',
            flags=(attempted, sid + ".camellia_won", sid + ".cost.nick",
                   sid + ".cost.unmarked_boast_lost", MEND)), portrait="Camellia"),
        n("refused", "Camellia", '''"Of course. I shall find something more entertaining to do."
{n}Camellia sheathes her rapier. She takes her glass with her when she leaves the Table.{/n}''',
          c('[Let her go.]', flags=(attempted, sid + ".refused")), portrait="Camellia"),
    ]
    requires = ["trickster", household.KEPT, "camellia.harem.eligible",
                "camellia.present_now", STRAIN]
    if later:
        requires.append(SCENE_IDS[0] + ".attempted")
    return household._table_scene(
        sid, "First touch", "Camellia", "[Camellia: another first touch]" if later else
        "[Camellia: first touch]", nodes, requires=requires,
        forbids=(MEND, attempted, "camellia.closed", "camellia.epoch_unavailable",
                 "camellia.returned_actor_lost", "camellia.presence.failed",
                 "trickster.failed", "fool_king.gone", "sacrifice"),
        chapters=(5,) if later else (3, 5), delay=48 if later else 0,
        Participants=["camellia"], RestAllowance="household.pair",
        HouseholdCategory="mend", HouseholdWitness=attempted,
        ForbidOverrides={"sacrifice": "trickster.commander_back"})


def register(payload, scenes, refs):
    pending = payload.setdefault("PendingHooks", [])
    if STRAIN not in pending:
        pending.append(STRAIN)
    have = {s["Id"] for s in scenes}
    for later in (False, True):
        if SCENE_IDS[int(later)] not in have:
            scenes.append(opportunity(later))
        household.CONSUMERS[SCENE_IDS[int(later)]] = household.PAGE_TAKEN
