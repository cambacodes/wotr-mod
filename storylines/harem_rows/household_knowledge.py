"""W4 knowledge slice: Seelah learns a favour; Nenio learns without strain.

Authored incidents, not native banter histories. See the eleven-field contract
in tools/route_packs/harem/household-knowledge.md. Only the learner attends.
The integrator's current bodily SeatWomen guards remain authoritative.
"""
import copy

from story_format import c, n, scene

PREFIX = "household.knowledge."
# Explicit chosen outcomes from 06 favour_outcomes, never scene completions.
FAVOURS = {"seelah_aranka": "aranka.trickster.night_kept",
           "nenio_seelah": "seelah.platform_kept"}
STRAIN = "seelah.harem.strain.aranka.1"


def knowledge_scenes():
    return [
        _beat("seelah_aranka", "Seelah", "seelah", "The singer's night",
            '"I remember Aranka singing from the roof after our night together."',
            '''{n}Seelah sits at the corner table, rubbing dried demon blood from a nick in her gauntlet. She looks up as you approach.{/n}
"Tell me something that didn't happen on patrol. Please. I've had enough of claws for one evening."''',
            '''"Ha! I'll bet the whole street heard her."
{n}Seelah reaches for the other cup, then leaves it where it is.{/n}
"I'd have liked a night worth singing about. Somehow I keep getting the patrols."
{n}She bends the dented edge of the gauntlet back into place.{/n}
"Don't look like that. I'm not asking you to take that night away from her. But I'm finishing my drink alone tonight."''',
            "[Leave her to her drink.]", (STRAIN,)),
        _beat("nenio_seelah", "Nenio", "nenio", "An hour for the paladin",
            '"I remember Seelah asking to meet in private after the yard work. I made time for her."',
            '''{n}Nenio has covered the corner table with a sketch of Drezen's walls. Her finger stops at a gap in the lines.{/n}
"Commander! I require a demonstration of the view from this point. The parapet conceals the demon siegeworks. At what hour can you accompany me?"''',
            '''"A private meeting with the paladin girl? Excellent! I shall need you for less than an hour."
{n}Nenio turns the sketch sideways, peering at the gap.{/n}
"She would bring armor, and then I would have to explain why standing on the stool in armor invalidates the measurement."
{n}She draws a small cross beside the parapet and gathers up the sheet.{/n}
"I can measure the stool first. Do not move it, Commander."''',
            "[Leave the stool where it is.]", ()),
    ]


def _beat(key, owner, learner, title, disclosure, opening, reaction, finish, effects):
    sid = PREFIX + key
    return scene(sid, title, owner, 3, "[" + title + "]", [
        n("start", owner, opening,
          c(disclosure, "learned"),
          c("[Later.]", abort=True)),
        n("learned", owner, reaction,
          c(finish, flags=(sid + ".seen", *effects))),
    ], requires=("trickster", "foresight.page_taken", "household.table.kept",
                 "household.stance_eligible", learner + ".harem.eligible",
                 learner + ".present_now", FAVOURS[key]),
       forbids=("fool_king.gone", "trickster.failed", sid + ".seen"),
       optional=True, Relationship="household", Chapters=[3, 5],
       Areas=["2570015799edf594daf2f076f2f975d8"],
       InteractionHub="household.table", Participants=[learner],
       ParticipantWomen=[learner], RestAllowance="household.pair",
       HouseholdCategory="dynamic", HouseholdWitness=sid + ".seen")


def register(payload, scenes, refs):
    """Append the slice without inventing bodies, favours or relationship states."""
    additions = knowledge_scenes()
    have = {s["Id"] for s in scenes}
    missing = [s for s in additions if s["Id"] not in have]
    for body in missing:
        woman = body["ParticipantWomen"][0]
        seat = payload.get("SeatWomen", {}).get(woman, {})
        if (seat.get("Relationship") != woman
                or woman + ".present_now" not in seat.get("Requires", [])
                or len(seat["Requires"]) < 2):
            raise ValueError("W4 knowledge needs current bodily SeatWomen: " + woman)
    scenes.extend(copy.deepcopy(missing))
    payload.setdefault("ForesightConsumers", {}).update(
        {body["Id"]: "foresight.page_taken" for body in additions})
