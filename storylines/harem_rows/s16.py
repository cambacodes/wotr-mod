"""S16: authored public dispatch correction, hs-C fields 1-11.

Two separately received replies; no joint audience, intimacy or native rewrite.
Only the sheet's deed receipts are written. Shared stance/failure policy and
Ledger/Last Call readers remain integration-owned (see the implementation note).
"""
from story_format import c, n, scene
from storylines import household

P = "household.pair.galfrey_konomi."
DREZEN = "2570015799edf594daf2f076f2f975d8"
QUEEN = "8c5dcc93d68d0ed44afd43902201da40"
KITRANE = "a8b7f6fd39ff2974f8b5fbf944a7f735"
KONOMI = "ca2d58c5c65723945857e04fb85d30ce"
DEEDS = (
    "correction.delivered", "galfrey.name_withheld", "konomi.office_named",
    "cost.galfrey.endorsement_withheld", "cost.konomi.joint_cover_lost",
    "cost.commander.errand",
)


def receipts(step, outcome):
    extra = DEEDS if outcome == "kept" else (
        ("misattribution.witnessed",) if outcome == "failed" else ())
    return tuple(P + suffix for suffix in (step + ".seen", step + "." + outcome, *extra))


def _nodes(step, kitrane, post):
    name = "Kitrane" if kitrane else "Queen Galfrey"
    opening = (
        '{n}A dispatch for the next march has come back to headquarters. '
        'Its cover names Queen Galfrey as approving an instruction from Konomi’s office. '
        'The courier points to a correction beside the royal name.{/n}\n'
    )
    opening += (
        '{n}Kitrane has struck it through: “Not an order from the Queen.” '
        'The courier still needs an answer from Konomi.{/n}' if kitrane else
        '{n}Galfrey has struck it through: “Not approved by the Crown.” '
        'The courier still needs an answer from Konomi.{/n}'
    )
    if post:
        opening += ('\n{n}Konomi’s private address is on the packet. Her answer must '
                    'come through the post she kept when she left Drezen.{/n}')
    else:
        opening += '\n{n}Konomi is at her office. The courier waits beside the saddled horse.{/n}'
    if step == "retry":
        opening = ('{n}The disputed cover lies beside the dispatch. Your first account '
                   'blurred the two replies; the courier has brought it back again.{/n}\n' + opening)
        choices = [
            c('"I’ll deliver the correction and hear the answers separately."', "returned"),
            c('"Use the old cover."', "failed"),
            c('"Leave it unanswered."', "declined"),
        ]
    else:
        choices = [
            c('[Diplomacy DC 22] "I’ll carry the correction as each of you wrote it."',
              check=dict(Skill="CheckDiplomacy", DC=22, Success="carried",
                         Failure="misquoted", CommanderOnly=True)),
            c('"I’ll take it back myself and wait for both replies."', "returned"),
            c('"Send it without either endorsement."', "declined"),
        ]
    choices.append(c('[Later.]', abort=True))
    nodes = [n("start", "Narrator", opening, *choices)]
    galfrey = (
        '{n}At the market stall, Kitrane reads the returned cover, her mailed finger '
        'stopping at the crossed-out name.{/n} "They buried their queen. They cannot '
        'keep ordering things in her name. If the Council wants this instruction, '
        'let it answer for it. I have Crows to drill."' if kitrane else
        '{n}In her audience, Galfrey reads the returned cover and pushes it back.{/n} '
        '"Her instructions are hers. Strike my name from the cover. If the Council '
        'wants my approval, it can bring its reasons before me. It will not borrow '
        'the Crown while I am attending to the war."'
    )
    konomi = (
        '{n}Konomi’s reply arrives through her private post. Beneath the correction '
        'she has written:{/n} ' if post else
        '{n}At her office, Konomi reads the correction. Her ears draw back; '
        'she writes her own title beneath the instruction.{/n} '
    )
    konomi += ('"Then let the Council answer for it. Your correction does not dismiss '
               'my correspondents. The instruction stands under my office’s authority. '
               'You may carry that answer back, Commander — exactly as written."')
    end = ('{n}You return the corrected dispatch to the waiting courier. It carries '
           'Konomi’s instruction and ' + name + '’s refusal to endorse it, each '
           'under its own name. The horse leaves headquarters at last.{/n}')
    for node_id in (("carried", "returned") if step == "settle" else ("returned",)):
        labour = ('{n}You carry the packet yourself and wait through both answers.{/n}\n'
                  if node_id == "returned" else
                  '{n}You carry each correction back without folding one answer into the other.{/n}\n')
        nodes.append(n(node_id, "Narrator", labour + galfrey + '\n' + konomi + '\n' + end,
                       c(flags=receipts(step, "kept"))))
    failure = (
        '{n}You summarize the corrections as agreement on the instruction. The courier '
        'lays your account beside the cover and points to the crossed-out royal name. '
        'He takes the disputed packet back to headquarters. Neither reply has changed.{/n}'
        if step == "settle" else
        '{n}The courier ties the old cover over the corrected dispatch. The crossed-out '
        'name disappears beneath it. At the gate, he repeats the supposed royal approval '
        'to the waiting officers. You have let the wrong authority travel with the order.{/n}'
    )
    nodes.append(n("misquoted" if step == "settle" else "failed", "Narrator", failure,
                   c(flags=receipts(step, "failed"))))
    nodes.append(n("declined", "Narrator",
                   '{n}You leave the correction unanswered. The courier takes the packet '
                   'away without a joint endorsement. The dispute remains.{/n}',
                   c(flags=receipts(step, "declined"))))
    return nodes


def register(payload, scenes, refs):
    """Register once in the payload, leaving the base route scene list untouched."""
    existing = {s["Id"] for s in payload["Scenes"]}
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [["galfrey.harem.eligible", "konomi.harem.eligible"]]
    for step in ("settle", "retry"):
        for kitrane in (False, True):
            for post in (False, True):
                suffix = (".kitrane" if kitrane else "") + (".post" if post else "")
                sid = P + step + suffix
                if sid in existing:
                    continue
                requires = ["trickster", household.PAGE_TAKEN, household.STANCE_ELIGIBLE,
                            household.KEPT, P + "ready", "galfrey.present_now"]
                forbids = ["household.closed", "fool_king.gone", "trickster.failed",
                           "engine.l12.commander_unreturned", "galfrey.closed",
                           "galfrey.killed_by_commander", "galfrey.epoch_unavailable",
                           "galfrey.returned_actor_lost", "konomi.closed", "konomi.retained_dead",
                           "konomi.returned_actor_lost", P + step + ".seen"]
                requires.append("galfrey.trickster.returned" if kitrane else "galfrey.final")
                if not kitrane:
                    forbids.extend(["galfrey.dead", "galfrey.trickster.returned"])
                if post:
                    requires.extend(["konomi.private_departed", "konomi.private_address",
                                     "konomi.private_letters", "konomi.reachable_by_letter"])
                    forbids.extend(["konomi.dead.unreturned", "konomi.present", "inhuman", "konomi.farewell",
                                    "konomi.missed_contact_invalidated"])
                else:
                    requires.append("konomi.present_now")
                    forbids.extend(["konomi.private_departed", "konomi.epoch_unavailable"])
                if step == "retry":
                    requires.append(P + "settle.failed")
                    forbids.extend([P + "settle.kept", P + "settle.declined"])
                body = scene(sid, "The courier sent back twice", "Narrator", 5, "",
                             _nodes(step, kitrane, post), requires=requires, forbids=forbids,
                             delay=48 if step == "retry" else 0, last=5, Relationship="household",
                             Chapters=[5], Areas=[DREZEN], Remote=True, ManualOnly=True, Kind="event",
                             Participants=["galfrey", "konomi"], Pair=["galfrey", "konomi"],
                             ParticipantWomen=[], RestAllowance="household.protected",
                             HouseholdCategory="protected", HouseholdWitness=P + step + ".seen",
                             ContactUnit=KITRANE if kitrane else QUEEN,
                             AdditionalContactUnits=[] if post else [KONOMI])
                if not post:
                    body["RequiresAnyGroups"] = [["konomi.present", "konomi.trickster.presence_on"]]
                payload["Scenes"].append(body)
                household.CONSUMERS[sid] = household.PAGE_TAKEN
