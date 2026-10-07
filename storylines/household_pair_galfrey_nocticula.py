"""S39: authored carried undertaking; HAREM-SHEETS-36-41, row 39.

Only deed/cost witnesses are written here. Policy inputs are exported for the
household integrator, which owns first-wins enmity and its one reconciliation.
No bodily Nocticula, passengers, affection, echo or native rewrite is produced.
"""
import copy

from story_format import c, n, p, scene

PREFIX = "household.pair.galfrey_nocticula."
PAIR = ("galfrey", "nocticula")
RETURNED = "galfrey.trickster.returned"
AREA = "2570015799edf594daf2f076f2f975d8"


def f(*names):
    return [PREFIX + name for name in names]


SUCCESS = ("undertaking.seen", "undertaking.held", "resolved",
           "cost.galfrey_sponsorship_withdrawn", "cost.nocticula_factor_overruled",
           "cost.commander_guarantor_kept", "cost.reconnaissance_forgone")
REPAIR = ("last_litter.seen", "last_litter.held", "resolved", *SUCCESS[3:],
          "cost.corrected_demand_carried")
POLICY = dict(
    Respect={"galfrey>nocticula": [f("undertaking.held"), f("last_litter.held")],
             "nocticula>galfrey": [f("undertaking.held"), f("last_litter.held")]},
    Failure=dict(Claimant="galfrey", Respondent="nocticula", Witness=f("undertaking.failed")[0]),
    Reconciliation=dict(Claimant="galfrey", Respondent="nocticula", Witness=f("last_litter.held")[0]),
    Ceiling="respect", Schedule="S39")


def terminal(id, text, flags, cost=None):
    return n(id, "Narrator", text, c(flags=f(*flags), crusade=cost))


def nodes(step, kitrane):
    name = "Kitrane" if kitrane else "Galfrey"
    sponsor = ("Before the Green Crows, Kitrane strikes her name from the sortie's sponsorship."
               if kitrane else
               "Before her officers, Galfrey revokes the escort authority her orderly claimed for the sortie.")
    consent = ('"I can pledge my sword and my name. Mendev\'s orders are no longer mine to give."'
               if kitrane else '"I will withdraw that authority. My wounded soldiers are not a disguise for scouts."')
    deed = ('{n}The courier returns with Nocticula\'s countermand, addressed to the factor by name.{/n}\n'
            '"You were told to waive this levy. You will refund your demand and surrender its collection to another. '
            'Try selling my protection twice again, and I shall collect from you personally."\n'
            '{n}' + sponsor + ' The correction is read aloud; the orderly stands red-faced beside her.{/n}\n'
            '"I condemn her traffic in slaves. I also heard her instruction. She has kept this undertaking."\n'
            '{n}At Drezen\'s departure office, you dismiss the mustered scout captain. He watches you burn the pilot\'s '
            'only survey: both concealed observation points and the patrol interval curl into ash. '
            'The factor\'s protest names you as the meddler who cost him his fee. You sign the reply in your own name.{/n}')
    if step == "open":
        return [
            n("start", "Narrator", '{n}A Mendevian orderly meets you and ' + name + ' in Drezen. His petition concerns wounded crusaders '
              'waiting at a mortal pilot\'s berth in the Midnight Isles. The pilot serves a factor under Nocticula\'s protection; '
              'his passage offer has a price and a limit.{/n}\n'
              '"They need passage, not a demon patron over Mendev," {n}' + name + ' says.{/n}\n'
              '{n}The queen\'s earlier correspondence lies beside the petition.{/n}\n'
              '"Acknowledge whose leave you require. No armed reconnaissance under cover of my indulgence. '
              'I have quite enough guests who mistake hospitality for an opportunity."',
              c('"Her rank, plainly. No scouts. Put my name on the undertaking."', "sent"),
              c('"Write it without her title. Let her mistake courtesy for weakness."', "insult"),
              c('[Later.]', abort=True)),
            terminal("sent", '{n}Fifty crowns buy the pilot\'s harbour survey; a hundred and fifty pay the hired planar courier\'s '
                     'outward and return fares. Two concealed observation points and a patrol interval make the survey worth keeping. '
                     'You place it beside an intelligence sortie plan and summon its scout captain to Drezen\'s departure office.{/n}\n'
                     + consent + '\n{n}The courier returns with Nocticula\'s answer.{/n}\n'
                     '"No levy on this passage. My factor will receive the same instruction. Your name guarantees the absence of scouts, Commander. '
                     'I shall remember it if one strays."',
                     ("open.seen", "open.ready", "survey.acquired", "sortie.mustered", "cost.courier_fares",
                      "cost.commander_guarantor_promised"), ("Finances", -200)),
            terminal("insult", '{n}Your courier delivers the undertaking stripped of Nocticula\'s title. Her reply comes back unopened '
                     'inside a second envelope.{/n}\n"Have your clerk learn whom he addresses before he petitions me."\n'
                     '"You sent an insult in the wounded men\'s names," {n}' + name + ' says. She puts the petition away.{/n}',
                     ("open.seen", "open.insult_sent", "permanent_refusal")),
        ]
    if step == "undertaking":
        return [
            n("start", "Narrator", '{n}At Drezen\'s departure office, the factor\'s new demand lies beside Nocticula\'s instruction: '
              'the old levy, payable before passage. His letter bears his own mark, not hers. The scout captain waits for your orders.{/n}\n'
              '"He expects crippled soldiers to empty their purses rather than quarrel with his mistress," {n}' + name + ' says.{/n}\n'
              '{n}Nocticula\'s earlier reply is equally plain.{/n}\n'
              '"The undertaking covers passage. It does not make your soldiers my spies, or mine your subjects."',
              c('[Carry both answers unchanged and challenge the renewed levy in your own name.]',
                check=dict(Skill="CheckDiplomacy", DC=24, Success="kept", Failure="mistranslated", CommanderOnly=True)),
              c('[Hire the independent interpreter and withdraw your scout captain in person.]', "interpreted"),
              c('"Put a scout on the passage list. She needn\'t know."', "exposed"),
              c('[Later.]', abort=True)),
            terminal("kept", deed, SUCCESS),
            terminal("interpreted", '{n}Your independent interpreter receives three hundred crowns. He lays out the factor\'s '
                     'unauthorized demand without trimming a clause; your challenge bears your name.{/n}\n' + deed,
                     (*SUCCESS, "cost.interpreter_paid"), ("Finances", -300)),
            terminal("mistranslated", '{n}You shorten the demand before forwarding it. Without the factor\'s claim to act on his own '
                     'authority, it reads like a surcharge imposed by the queen. Her reply leaves his collection standing.{/n}\n'
                     '"Your queen keeps the men waiting behind her levy," {n}' + name + ' says.{/n} '
                     '"And you omitted the words that would have exposed her collector. Do not lay that omission at her door."\n'
                     '{n}The scout captain remains mustered. The survey stays on your desk. Nothing has been withdrawn.{/n}',
                     ("undertaking.seen", "undertaking.failed", "unsettled", "cost.commander_delay")),
            terminal("exposed", '{n}The orderly checks the passage list against the muster at Drezen\'s departure office. '
                     'The scout\'s name appears on both. He refuses to send the altered list; its innocent cover is gone.{/n}\n'
                     '"You would use men who cannot stand to conceal an armed scout?" {n}' + name + ' tears the list across.{/n}\n'
                     '{n}Nocticula\'s reply arrives by the existing correspondence.{/n}\n'
                     '"How tiresome. I expected a better lie from you. This undertaking is finished."',
                     ("undertaking.seen", "undertaking.scout_exposed", "permanent_refusal", "cost.commander_cover_lost")),
        ]
    return [
        n("start", "Narrator", '{n}The levy remains. ' + name + ' has kept both your shortened account and the factor\'s full demand. '
          'The latter names the authority he invented; the former concealed it. The survey and the mustered sortie are still yours.{/n}\n'
          '"I will answer the whole demand," {n}she says.{/n} "Carry it this time. Every word."',
          c('"I\'ll carry the factor\'s demand myself. Recall my sortie. Let both women answer the whole of it."', "home"),
          c('"Let the levy stand."', "declined"),
          c('[Later.]', abort=True)),
        terminal("home", '{n}Four hundred crowns pay a fresh planar courier and an independent attestation. '
                 'You carry the marked demand to ' + name + ' yourself; the courier takes that same untrimmed demand to Nocticula. '
                 'Neither woman has to speak to the other.{/n}\n' + deed, REPAIR, ("Finances", -400)),
        terminal("declined", '"Then the delay was your doing, and now you leave it in place," {n}' + name + ' says. '
                 'She takes back the petition. No reply from Nocticula is requested.{/n}',
                 ("last_litter.seen", "last_litter.declined", "permanent_refusal")),
    ]


def make_scenes(payload):
    out = []
    for step, title, req, forbidden, delay in (
        ("open", "The price of passage", (), (), 0),
        ("undertaking", "Two undertakings", ("open.ready", "survey.acquired", "sortie.mustered"), ("permanent_refusal",), 48),
        ("last_litter", "The levy in full", ("undertaking.failed", "survey.acquired", "sortie.mustered"),
         ("resolved", "permanent_refusal"), 48)):
        for kitrane in (False, True):
            requires = ["trickster", "foresight.page_taken", "household.table.kept", *f(*req)]
            forbids = f(step + ".seen", *forbidden)
            overrides = {"noct.acq.council_fight": "nocticula.trickster.returned"}
            forbids.append("noct.acq.council_fight")
            for woman in PAIR:
                requires.append(woman + ".harem.eligible")
                rel = payload["Relationships"][woman]
                forbids.extend([rel["ClosedFlag"], *rel["UnavailableFlags"], *rel.get("EpochUnavailableFlags", [])])
                overrides.update(rel.get("UnavailableOverrides", {}))
            (requires if kitrane else forbids).append(RETURNED)
            out.append(scene(PREFIX + step + (".kitrane" if kitrane else ""), title,
                             "Galfrey", 5, "[Visit the Drezen departure office.]", nodes(step, kitrane),
                             requires=requires, forbids=list(dict.fromkeys(forbids)), delay=delay, last=5,
                             Relationship="household", Chapters=[5], Areas=[AREA], Remote=True, ManualOnly=True,
                             Participants=list(PAIR), RestAllowance="household.protected", ForbidOverrides=overrides,
                             HouseholdCategory="protected", HouseholdWitness=f(step + ".seen")[0]))
    return out


RECORDS = (
    ("resolved", "The levy was countermanded. I burned the survey and recalled my sortie.", ("resolved",), ()),
    ("failed", "My trimmed demand left the queen's levy over the passage.", ("undertaking.failed",), ("resolved",)),
    ("repaired", "I carried the full demand separately; both women then kept their undertaking.", ("last_litter.held",), ()),
    ("insult", "I sent her an insult instead of an undertaking.", ("open.insult_sent",), ()),
    ("scout", "I hid reconnaissance inside the passage undertaking.", ("undertaking.scout_exposed",), ()),
    ("declined", "I let her factor keep the levy.", ("last_litter.declined",), ()),
)
COSTS = {
    "courier_fares": "Two courier fares and the pilot's survey cost 200 Finances: 150 and 50 respectively.",
    "commander_guarantor_promised": "I put my own name on the undertaking.",
    "galfrey_sponsorship_withdrawn": "The orderly's claimed sponsorship of the reconnaissance was publicly withdrawn.",
    "nocticula_factor_overruled": "Nocticula stripped her protected factor of collection on this passage and forfeited his levy.",
    "commander_guarantor_kept": "I answered the factor's public accusation in my own name.",
    "reconnaissance_forgone": "The only acquired survey was burned; the mustered sortie was recalled without a replacement scout.",
    "commander_delay": "My omitted clause prolonged the levy. Both women held me answerable.",
    "commander_cover_lost": "The exposed scout lost this passage's innocent cover.",
    "interpreter_paid": "The independent interpreter cost another 300 Finances.",
    "corrected_demand_carried": "A fresh courier and independent attestation cost another 400 Finances.",
}


def integrate(payload):
    """Append only S39 scenes and readers, after the existing household assembly."""
    from storylines import foresight
    emitted = make_scenes(payload)
    payload["Scenes"].extend(emitted)
    foresight.CONSUMERS.update({s["Id"]: "foresight.page_taken" for s in emitted})
    for woman in PAIR:
        reader = PREFIX + "reader." + woman + ".open"
        payload.setdefault("Derived", {})[reader] = [[woman + ".harem.eligible"]]
        payload.setdefault("DerivedOpenRoutes", {})[reader] = [woman]
    # This reader consumes the owner's Council/earned-return channel, without a
    # second Nocticula death binding or an alternative return device.
    before, after = f("reader.nocticula.before_council", "reader.nocticula.returned")
    payload["Derived"][before] = [["nocticula.harem.eligible"]]
    payload.setdefault("DerivedForbids", {})[before] = ["noct.acq.council_fight"]
    payload["Derived"][after] = [["nocticula.harem.eligible", "nocticula.trickster.returned"]]
    payload["DerivedOpenRoutes"].update({before: ["nocticula"], after: ["nocticula"]})
    payload["Derived"][f("reader.nocticula.open")[0]] = [[before], [after]]
    lines = [dict(Id=PREFIX + "reader." + key, **p("{n}" + text + "{/n}", requires=f(*req), forbids=f(*fb)))
             for key, text, req, fb in RECORDS]
    lines += [dict(Id=PREFIX + "reader.cost." + key,
                   **p("{n}" + text + "{/n}", requires=f("cost." + key))) for key, text in COSTS.items()]
    ledger = payload["Books"]["trickster.ledger"]["Entries"]
    for suffix, section in (("ledger", "Debts"), ("seating", "Seating Notes")):
        ledger.append(dict(Id=PREFIX + "reader." + suffix, Section=section, Portrait="Galfrey",
                           Title="Galfrey and Nocticula: the passage undertaking",
                           Text="{n}A limited undertaking, carried through separate replies.{/n}",
                           Requires=f("open.seen"), Forbids=[], AnyGroups=[], Lines=copy.deepcopy(lines)))
    for woman in PAIR:
        host = next(s for s in payload["Scenes"] if s["Id"] == woman + ".lastcall.page")
        page = next(node for node in host["Nodes"] if node["Id"] == "page")
        paragraphs = page.setdefault("Paragraphs", [])
        living = f("reader." + woman + ".open")
        for key, text, req, fb in RECORDS:
            # These are recollections by the currently present claimant, never
            # a fresh reply from an absent respondent.
            for returned in (False, True):
                paragraphs.append(dict(Id=PREFIX + "reader.lastcall." + woman + "." + key +
                                       (".returned" if returned else ".living"),
                                       **p("{n}" + text + "{/n}", requires=[*living, *f(*req),
                                    *(["sacrifice", "trickster.commander_back"] if returned else [])],
                                    forbids=[*f(*fb), *([] if returned else ["sacrifice"])])))
        for key, text in COSTS.items():
            for returned in (False, True):
                paragraphs.append(dict(Id=PREFIX + "reader.lastcall." + woman + ".cost." + key +
                                       (".returned" if returned else ".living"),
                                       **p("{n}" + text + "{/n}", requires=[*living, *f("cost." + key),
                                    *(["sacrifice", "trickster.commander_back"] if returned else [])],
                                    forbids=[] if returned else ["sacrifice"])))
        reaction = ('{n}She recalls the marked demand.{/n} "Nocticula kept that undertaking. '
                    'It does not excuse the slaves in her city. I did not offer her that excuse."'
                    if woman == "galfrey" else
                    '{n}Nocticula\'s reply dwells on the burnt survey.{/n} "She withdrew her sponsorship '
                    'before her own people. You surrendered something useful. My factor merely surrendered '
                    'something that was never his to demand. I trust he remembers the difference."')
        for returned in (False, True):
            paragraphs.append(dict(Id=PREFIX + "reader.lastcall." + woman + ".reaction" +
                                   (".returned" if returned else ".living"),
                                   **p(reaction, requires=[*living, *f("resolved"),
                                     *(["sacrifice", "trickster.commander_back"] if returned else [])],
                                     forbids=[] if returned else ["sacrifice"])))
