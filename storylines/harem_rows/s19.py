"""S19: authored dispatch errand; no canon rewrite, echo, or intimate interval.

Contract: hs-C sheet S19, corrected by Writer/plans/harem-lore-check.md.
Only terminal deed witnesses are written. The coordinator owns directional
attitudes, qualified first-wins enmity and Last Call attachment.
"""
from story_format import c, n
from storylines import household, foresight

P = "household.pair.arueshalae_minagho."
PAIR = ("arueshalae", "minagho_chivarro")
QUALIFIED = {
    "arueshalae.harem.enmity.w.minagho": "arueshalae.harem.reconciled.w.minagho",
    "minagho_chivarro.harem.enmity.minagho.arueshalae":
        "minagho_chivarro.harem.reconciled.minagho.arueshalae",
}
DEED = ("lot.restored", "minagho.burden_carried", "arueshalae.part_carried",
        "cost.minagho.exemption_refused", "cost.arueshalae.safe_assignment_yielded",
        "cost.commander.burden_taken")


def terminal(step, outcome, branch):
    flags = [step + ".seen", step + "." + outcome]
    if outcome == "kept":
        flags += list(DEED) + ["good.pity_without_exemption" if branch == "good" else "fallen.rank_answered"]
    elif outcome == "failed":
        flags += ["lot.mishandled" if step == "settle" else "assignment.abandoned"]
    return tuple(P + flag for flag in flags)


def _nodes(step, branch):
    good = branch == "good"
    if step == "settle":
        opening = ('{n}A sealed war dispatch lies beside the drawing bowl. The watch waits beyond the exposed '
                   'lower-wall passage. Minagho finds her slip outside the bowl and pushes it back in.{/n}\n'
                   '"Put mine back. I can smell pity even through your ink."\n'
                   '{n}Arueshalae keeps her own slip among the others.{/n}\n')
        opening += ('"I remember what you did to me. I still pity you. That does not mean I will carry your part."'
                    if good else '"Afraid your brand will sting in the wind? Then stay here. I can use the watch without you."')
        choices = [
            c('"No exemptions. Put every slip back."', check=dict(
                Skill="SkillPerception", DC=20, Success="draw", Failure="botched", CommanderOnly=True)),
            c('"I\'ll carry it with you. Draw, and leave the pity out of it."', "carry"),
            c('"Leave the job to the watch."', "declined"), c("[Later.]", abort=True),
        ]
    else:
        opening = ('{n}Minagho pins the drawn slips beneath the sealed dispatch. Outside, the watch calls for '
                   'the relief signal.{/n}\n"Mine. Hers. Yours. Try counting them this time."\n')
        opening += ('{n}Arueshalae reaches for her assigned slip.{/n} "I will take the approach. You must bring it back, Minagho."'
                    if good else '{n}Arueshalae taps Minagho\'s slip.{/n} "Leave her exposed leg to her. I want to see whether she can still do more than threaten."')
        choices = [c('"Keep the drawn jobs. I\'ll take the spare burden."', "carry"),
                   c('"Arueshalae can carry yours too."', "failed"),
                   c('"Leave this unfinished."', "declined"), c("[Later.]", abort=True)]
    nodes = [n("start", "Minagho", opening, *choices, portrait="Minagho")]
    assignment = "draws" if step == "settle" else "keeps"
    action = ('{n}Minagho ' + assignment + ' the exposed leg. Arueshalae takes the approach that had been sheltered, '
              'while you shoulder the spare burden. Along the lower wall, Arueshalae keeps her bow on '
              'the broken ground beyond Drezen. Minagho carries the seal through the open passage, '
              'hands it to the waiting watch, and brings their answer back herself. Wind has torn '
              'her sleeve; she throws the empty dispatch case onto the table.{/n}\n'
              '"Next time, leave my name in."\n')
    action += ('{n}Arueshalae sets down her bow beside her former jailer.{/n}\n'
               '"I would take that watch with you again. I have not forgotten the prison. But I wanted you to come back."'
               if good else '{n}Arueshalae looks from the torn sleeve to Minagho\'s face.{/n}\n'
               '"You came back with the answer. Good. Next time I need someone on that passage, I will know whom to use."\n'
               '"Use?" {n}Minagho bares her teeth.{/n} "Try ordering me there and see what answer you get."')
    for key in (("draw", "carry") if step == "settle" else ("carry",)):
        lead = ('{n}You catch the last slip beneath the bowl and restore it before the draw.{/n}\n'
                if key == "draw" else '{n}You take the spare assignment yourself. The drawn jobs stand.{/n}\n')
        nodes.append(n(key, "Minagho", lead + action,
                       c(flags=terminal(step, "kept", branch)), portrait="Minagho"))
    failed_key = "botched" if step == "settle" else "failed"
    failure = ('{n}A slip remains under your hand. Minagho pulls it free: her name.{/n}\n'
               '"How touching. You put it back where nobody could draw it."\n'
               if step == "settle" else
               '{n}Minagho snatches her assignment away from Arueshalae.{/n}\n'
               '"So she carries mine, and I wait like a whipped dog? Keep your damned dispatch."\n')
    failure += '{n}Arueshalae watches Minagho crush the slip in her fist.{/n}\n'
    failure += ('"I offered you no pardon, Minagho. And I will not pretend we kept the draw."'
                if good else '"You wanted a place beside me. You got an exemption instead. How embarrassing."')
    nodes.append(n(failed_key, "Minagho", failure,
                   c(flags=terminal(step, "failed", branch)), portrait="Minagho"))
    refusal = ('{n}You give the dispatch to the watch runner. Minagho leaves her slip on the table.{/n}\n'
               '"Let your soldiers scurry, then. Do not call this settled."\n')
    refusal += ('{n}Arueshalae picks up her bow.{/n} "The watch still needs cover. I am going to the wall."'
                if good else '{n}Arueshalae pushes the bowl away.{/n} "What a waste. I wanted to see her earn that sneer."')
    nodes.append(n("declined", "Minagho", refusal,
                   c(flags=terminal(step, "declined", branch)), portrait="Minagho"))
    return nodes


def register(payload, scenes, refs):
    """Append row registrations without changing shared registries or route state."""
    payload.setdefault("Derived", {})[P + "ready"] = [[
        "arueshalae.harem.eligible", "participant.minagho.available"]]
    existing = {s["Id"] for s in scenes}
    for step in ("settle", "retry"):
        for branch in ("good", "fallen"):
            sid = P + step + "." + branch
            if sid in existing:
                continue
            requires = ["participant.minagho.available", "arueshalae.present_now", "minagho.present_now",
                        "arueshalae.redeemed" if branch == "good" else "arueshalae.corrupted"]
            forbids = [P + step + ".seen", "household.closed", "fool_king.gone", "trickster.failed",
                       "engine.l12.commander_unreturned", "minachiv.closed",
                       "minagho_chivarro.trickster.declined_minagho", "inhuman", *QUALIFIED]
            if branch == "good":
                forbids.append("arueshalae.corrupted")
            if step == "retry":
                forbids += [P + "settle.kept", P + "settle.declined"]
            # table_entry supplies current page/Table gates and broad enmity guards.
            # Keep its global entry list unchanged: the row loader owns emission.
            body = household.table_entry(
                sid, "The lot nobody pities", "[Arueshalae and Minagho: the war dispatch]",
                _nodes(step, branch), PAIR, P + ("ready" if step == "settle" else "settle.failed"),
                requires=requires, forbids=forbids, delay=0 if step == "settle" else 48,
                chapters=(5,), ParticipantWomen=["minagho"], ForbidOverrides=QUALIFIED,
                RestAllowance="household.protected", HouseholdCategory="protected",
                HouseholdWitness=P + step + ".seen")
            household.ENTRIES.remove(body)
            foresight.CONSUMERS[sid] = household.PAGE_TAKEN
            # Read-only reservations; their first-wins/reconciliation producers
            # remain integration-owned. Rules.Validate requires every override
            # input to be declared even before its controller is attached.
            pending = payload.setdefault("PendingHooks", [])
            for key, value in body["ForbidOverrides"].items():
                for hook in (key, value):
                    if hook not in pending:
                        pending.append(hook)
            scenes.append(body)
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None and not any(e["Id"] == "seating.s19" for e in ledger["Entries"]):
        kept = [P + "settle.kept", P + "retry.kept"]
        ended = kept + [P + "retry.failed", P + "settle.declined", P + "retry.declined"]

        def line(text, requires=(), forbids=(), groups=()):
            return dict(Text="{n}" + text + "{/n}", Requires=list(requires),
                        Forbids=list(forbids), AnyGroups=[list(g) for g in groups])

        ledger["Entries"].append(dict(
            Id="seating.s19", Section="Seating Notes", Portrait="Arueshalae",
            Title="Arueshalae and Minagho", Text="{n}The lower-wall dispatch.{/n}",
            Requires=["trickster", household.PAGE_TAKEN, household.KEPT], Forbids=[], AnyGroups=[],
            Tooltip="RRT_SeatingNotes", Lines=[
                line("Minagho refused the exemption and carried her lot. Arueshalae kept her own part without calling it pardon.",
                     requires=[P + "good.pity_without_exemption"], groups=[kept]),
                line("They kept the drawn work. Neither let the other call it charity.",
                     requires=[P + "fallen.rank_answered"], groups=[kept]),
                line("I mishandled the lot.", requires=[P + "settle.failed"], forbids=ended),
                line("I abandoned their drawn assignments.", requires=[P + "retry.failed"], forbids=kept),
                line("The watch took the job; the quarrel was left alone.",
                     groups=[[P + "settle.declined", P + "retry.declined"]], forbids=kept),
                line("Their slips are still on the table.",
                     forbids=[P + "settle.seen", P + "retry.seen"]),
                line("Minagho gave up her exemption; Arueshalae gave up the sheltered assignment; I took the spare burden.",
                     requires=[P + flag for flag in DEED if flag.startswith("cost.")]),
            ]))
