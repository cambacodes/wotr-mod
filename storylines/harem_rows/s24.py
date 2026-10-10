"""S24: authored noncontact bout; native acquaintance is not a former romance.

Canon anchors (reopened in blueprints.zip/enGB): Velexia_Main/Cue_0058,
c8cd8cd451fb812488a3964afcee266c, and Cue_0038,
13b2ee15ce8f769428ef468b371730b9. Arueshalae/Cue_0083,
0cb8bb696bff85a42ab5345280a9fe1c, forbids assuming safe caresses.
No native facts, touch protection, relationship terms or return devices change.
"""
from copy import deepcopy

from story_format import c, n
from storylines import household


PREFIX = "household.pair.arueshalae_vellexia."
PAIR = ("arueshalae", "vellexia")
BODY_REQUIRES = ("arueshalae.present_now", "vellexia.present_now", "vellexia.trickster.in_person")
BODY_FORBIDS = ("arueshalae.closed", "vellexia.closed", "vellexia.trickster.kept_as_mirror",
                "household.closed", "fool_king.gone", "trickster.failed",
                "engine.l12.commander_unreturned")
RESPECT_WITNESSES = ("bout.bounded", "arueshalae.bait_ended", "vellexia.halt_kept",
                     "cost.arueshalae.easy_pleasure_refused", "cost.vellexia.feeding_taunt_yielded")


def P(suffix):
    return PREFIX + suffix


def _success(step, fallen):
    return tuple(P(x) for x in (step + ".seen", step + ".kept", *RESPECT_WITNESSES,
                               "cost.commander.referee_time",
                               "fallen.command_refused" if fallen else "good.renunciation_kept"))


def _nodes(step, fallen):
    opening = '''{n}Two staves lie across the corner table. Beyond it, crusaders wait with a map of the next assault. Vellexia takes a staff and smiles at Arueshalae.{/n}
"Drezen! All these aching soldiers, and you amuse yourself with sticks. Have you forgotten how to make someone scream?"
'''
    if fallen:
        opening += '''"No. But I choose who screams." {n}Arueshalae takes the other staff by its end, keeping its full length between them.{/n} "You always did mistake an audience for a pack of pets."
"Then entertain me without the leash, dear. If you can."'''
    else:
        opening += '''{n}Arueshalae's fingers tighten on the staff.{/n} "I remember you, Vellexia. And I remember what you call amusement. We can cross staves. Nothing else."
"You used to finish your pleasures. Has Desna forbidden that too?"'''
    if step == "retry":
        opening += '''
{n}Arueshalae places her staff back on the table. Vellexia's smile thins. Neither will take it up until you stand between the cleared benches.{/n}'''
        choices = (
            c('"Keep your distance. I will call the halt."', "refereed"),
            c('"Finish it without a referee."', "failed"),
            c('"Leave it."', "declined"),
            c('[Later.]', abort=True),
        )
    else:
        choices = (
            c('"I\'ll call the bout. Keep it between the two of you."', check=dict(
                Skill="SkillAthletics", DC=20, Success="bounded", Failure="botched", CommanderOnly=True)),
            c('"Put the furniture aside. I\'ll stand at the edge and call every halt."', "refereed"),
            c('"There will be no bout here."', "declined"),
            c('[Later.]', abort=True),
        )
    ending = ('''"Find yourself a pet who stops when you clap." {n}Arueshalae lowers her staff without approaching.{/n}
"Oh, I have plenty. Half of them are holding up my lamps. Very few could ever knock a weapon out of my hands. You were always my favourite."'''
              if fallen else
              '''"You wanted a bout. That is what I finished." {n}Arueshalae lowers her staff without approaching.{/n}
"How dreary. And how irritating that you did it well. I taught you better than sticks, little bird. I taught you to finish."''')
    deed = '''{n}You stay at the edge of the cleared floor. Each time Vellexia tries to close the distance, you call them back to staff's reach. The soldiers' briefing waits while the staves crack together. Arueshalae catches Vellexia's shaft with her own and sends it spinning under a bench.{/n}
"Enough," {n}Arueshalae says. Vellexia's hand opens. She leaves the fallen staff where it lies.{/n}
''' + ending + '''
{n}Vellexia steps aside for the crusaders, still smiling at Arueshalae. The assault map can finally be unrolled.{/n}'''
    result = "failed" if step == "retry" else "botched"
    failure = ('''{n}You turn away. Vellexia slides her grip up the staff and beckons Arueshalae closer.{/n}
"No sticks, then. Show me what you really want."
{n}Arueshalae drops her staff across the space between them. The bout ends before either can approach.{/n}
''' if step == "retry" else
               '''{n}You lunge to catch a rolling bench. Vellexia steps past your shoulder and beckons Arueshalae closer.{/n}
"No sticks, then. Show me what you really want."
{n}You wrench the bench between them. Arueshalae sets her staff across it. Neither has touched the other.{/n}
''')
    failure += ('''"Order your own pets about." {n}Arueshalae turns her back on Vellexia.{/n}'''
                if fallen else '''"I know what comes after that invitation. I will not do it again." {n}Arueshalae turns her back on Vellexia.{/n}''')
    failure += '''
"And here I thought a war might cure this city's dullness. Run along, then. You always did come back hungrier." {n}Vellexia tosses her staff onto the table. The crusaders retrieve their map.{/n}'''
    nodes = [n("start", "Narrator", opening, *choices)]
    if step == "settle":
        nodes.append(n("bounded", "Narrator", '''{n}You haul the benches clear and catch the first crossing of the staves before Vellexia can turn it into a rush.{/n}
''' + deed,
                       c(flags=_success(step, fallen))))
    nodes.extend([
        n("refereed", "Narrator", '''{n}You move the last bench yourself and take your place. Neither woman gets a private audience tonight.{/n}
''' + deed,
          c(flags=_success(step, fallen))),
        n(result, "Narrator", failure, c(flags=(P(step + ".seen"), P(step + ".failed"), P("bout.interrupted")))),
        n("declined", "Narrator", '''{n}Arueshalae puts down her staff. Vellexia lets hers fall with a clatter among the cups.{/n}
"Do bring me something less tedious next time, Commander. Your war will not last forever, and neither will her diet."
{n}Arueshalae pulls the assault map out from under the staff and spreads it for the waiting soldiers.{/n}''',
          c(flags=(P(step + ".seen"), P(step + ".declined")))),
    ])
    return nodes


def _scene(step, fallen):
    branch = "fallen" if fallen else "good"
    requires = (*BODY_REQUIRES, "arueshalae.corrupted" if fallen else "arueshalae.redeemed")
    forbids = (*BODY_FORBIDS, P(step + ".seen"))
    if not fallen:
        forbids += ("arueshalae.corrupted",)
    if step == "retry":
        forbids += (P("settle.kept"), P("settle.declined"))
    # Use the central attendance/enmity envelope without accumulating module-global
    # registrations across repeated builds or leaking these scenes into other payloads.
    entries, consumers = list(household.ENTRIES), dict(household.CONSUMERS)
    try:
        body = household.table_entry(
            P(step + "." + branch), "A bout without feeding", '[Arueshalae and Vellexia: the staves]',
            _nodes(step, fallen), PAIR, P("settle.failed" if step == "retry" else "ready"),
            requires=requires, forbids=forbids, delay=48 if step == "retry" else 0, chapters=(5,),
            RestAllowance="household.protected", HouseholdCategory="protected",
            HouseholdWitness=P(step + ".seen"), HouseholdSchedule="S24", HouseholdOrder=5.46)
        body["MaxChapter"] = 5
        return body
    finally:
        household.ENTRIES[:] = entries
        household.CONSUMERS.clear()
        household.CONSUMERS.update(consumers)


def _ledger():
    def line(text, requires=(), forbids=(), groups=()):
        return dict(Text="{n}" + text + "{/n}", Requires=list(requires), Forbids=list(forbids),
                    AnyGroups=[list(g) for g in groups])
    kept = (P("settle.kept"), P("retry.kept"))
    declined = (P("settle.declined"), P("retry.declined"))
    return dict(Id="seating.arueshalae.vellexia", Section="Seating Notes", Portrait="Arueshalae",
                Title="Arueshalae and Vellexia", Text="{n}Two staves. No feeding.{/n}",
                Requires=["trickster", household.PAGE_TAKEN, household.KEPT], Forbids=[], AnyGroups=[],
                Tooltip="RRT_SeatingNotes", Lines=[
                    line("Arueshalae ended the bait. Vellexia kept the halt.", groups=[kept]),
                    line("She would not return to the pleasure Vellexia offered.", [P("good.renunciation_kept")]),
                    line("She would not take a patron's command for an invitation.", [P("fallen.command_refused")]),
                    line("I kept the assault briefing waiting while I called their halts.", [P("cost.commander.referee_time")]),
                    line("Vellexia gave up her feeding spectacle, not her taste for it.", [P("cost.vellexia.feeding_taunt_yielded")]),
                    line("I interrupted the bout before either could claim the answer.", [P("settle.failed")], [P("retry.seen")]),
                    line("I left the bout without its referee.", [P("retry.failed")]),
                    line("I refused the bout.", groups=[declined]),
                    line("Vellexia's challenge is unanswered.", forbids=[P("settle.seen")]),
                ])


def register(payload, scenes, refs):
    """Register in a fully assembled route payload before final household validation.

    `scenes` and `refs` are the discovery API's compatibility arguments. Do not
    replace its base-route list or invent absent route/native adapters.
    """
    if any(s["Id"].startswith(PREFIX) for s in payload["Scenes"]):
        return
    payload.setdefault("Derived", {})[P("ready")] = [[
        "arueshalae.harem.eligible", "vellexia.harem.eligible", "vellexia.trickster.in_person"]]
    # Read-only ladder adapters: witnessed conduct, never an attitude Set effect.
    # The controller retains ownership of enmity and reconciliation suppression.
    for a, b in (PAIR, PAIR[::-1]):
        stage = a + ".harem.attitude." + b + "."
        payload["Derived"][stage + "respect"] = [[P(w) for w in RESPECT_WITNESSES]]
        payload["Derived"][stage + "rival"] = [[P("ready")]]
        payload.setdefault("DerivedForbids", {})[stage + "rival"] = [stage + "respect"]
    entries = [_scene(step, fallen) for step in ("settle", "retry") for fallen in (False, True)]
    payload["Scenes"].extend(deepcopy(entries))
    # Paid-page manifest registration does not grant the page or either outcome.
    from storylines import foresight
    foresight.CONSUMERS.update({entry["Id"]: household.PAGE_TAKEN for entry in entries})
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (PAIR, PAIR[::-1]):
        for key in (household.enmity(a, b), a + ".harem.reconciled." + b):
            if key not in pending:
                pending.append(key)
    payload["Books"]["trickster.ledger"]["Entries"].append(_ledger())
