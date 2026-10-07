"""W5 reviewed alliance slice (hs-D): S10, S20, S21, S29 and S30.

AUTHORED RRT aftermaths, not native event rewrites. Read-only registration:
no scenes, answers, stage/stance/return producers, intimacy or allowance charge.
Historical records survive absence; current notes and codas never supply bodies.
"""
from story_format import p
from storylines.harem_rows import s10, s20, s21, s29, s30


P = "household.readers.w5."
STAGES = ("rival", "respect", "friend", "lover")
ROWS = {
    "s10": dict(pair=("seelah", "nenio"), prefix=s10.PREFIX,
                seen=s10.PREFIX + "question.seen", kept=s10.ANSWERED,
                declined=s10.PREFIX + "question.declined", title="The watch question", hosts=("seelah",)),
    "s20": dict(pair=("seelah", "jannah"), prefix="household.pair.seelah_jannah.",
                seen=s20.ACCOUNT, outcomes=s20.OUTCOMES, title="Jannah's account"),
    "s21": dict(pair=("seelah", "yaniel"), prefix=s21.P,
                seen=s21.P + "watch.seen", kept=s21.KEPT,
                declined=s21.P + "watch.declined", title="The gate watch"),
    "s29": dict(pair=("seelah", "kiana"), prefix=s29.PREFIX,
                seen=s29.P("ward.seen"), kept=s29.HELPED,
                declined=s29.P("ward.declined"), title="The ward visit", hosts=("seelah",)),
    "s30": dict(pair=("eliandra", "targona"), prefix=s30.PREFIX,
                seen=s30.PREFIX + "charges.seen", kept=s30.ANSWERED,
                declined=s30.DECLINED[1], title="The road map"),
}

# Recall only what the deed actually established. No successful evacuation,
# resumed romance, completed duel, conversion or restored former Nenio memory.
RECALL = {
    "s10": {
        "seelah": '{n}Seelah remembered the broken watch lantern and Nenio crossing out the curses. "She asked what I did when the man could no longer shout. A better question. A bloody long evening, though."{/n}',
        "nenio": '{n}Nenio kept Seelah\'s account of the ladder with the sketch of the broken lantern. The paladin had been afraid and had stayed. Nenio had discarded the word list; the decision still required investigation.{/n}',
    },
    "s21": {
        "seelah": '{n}Seelah recalled crouching beneath the wagon while Yaniel set the sentries to work. "I wanted to hear about Radiance. She wanted the men counted. Fair enough. We stayed until the relief."{/n}',
        "yaniel": '{n}Yaniel remembered Seelah searching beneath the wagon instead of praising her sword. "She took the right side of the gate. I took the left. The sergeant got his two pairs of hands."{/n}',
    },
    "s29": {
        "seelah": '{n}Seelah remembered the scout\'s blood stiffening the cloth and Kiana showing her where to hold his arm. "I brought a jug. She needed hands. At least I managed to give her those."{/n}',
        "kiana": '{n}Kiana recalled the private half-hour she had spent binding the scout\'s wound instead. Seelah had held his arm as directed. "The princess acquired a paladin who could follow instructions. A useful addition to the play."{/n}',
    },
    "s30": {
        "eliandra": '{n}Eliandra remembered spending her Pulura audience on the stargazers and the wounded carts. Targona had heard their names before marking the road. "We agreed to look together once they were through. I did not ask her to stop fighting."{/n}',
        "targona": '{n}Targona recalled Eliandra\'s cup across the arrow on the map. "She named the people behind us. I offered to guard their road, then asked her to help me find where to strike. We had both answered."{/n}',
    },
}

DEFERRED = {
    "s10": "The question about Seelah's watch remained unanswered; Nenio had received neither the account nor its correction.",
    "s21": "The offered gate watch had been declined. No shared watch was entered against the two names.",
    "s29": "The ward invitation had been declined. The Commander had not stayed for Kiana's account.",
    "s30": "Eliandra and Targona had kept separate tasks. The map recorded no agreement between them.",
}
UNPLAYED = {
    "s10": "There was no account of the broken watch lantern among the Commander's recollections of Seelah and Nenio.",
    "s21": "There was no shared gate watch with Seelah among the Commander's recollections of Yaniel.",
    "s29": "The Commander's recollections held no visit with Seelah to Kiana's wounded scout.",
    "s30": "The Commander's recollections held no road-map audience between Eliandra and Targona.",
}
JANNAH = (
    "Jannah had gone to Seelah herself and returned to the gaol with a handprint and a grin. Houndheart was hers to explain; she had not left the Commander to do it.",
    "The Commander had offered to tell Seelah. Jannah had asked for the facts, without an explanation in her name. That offer supplied no answer from Seelah.",
    "Jannah's account to Seelah had been put off. The little cart on her tankard had faced the wall; her circle had not settled that conversation.",
)
HISTORY = {
    "s21": "{n}Yaniel directed the gate watch; Seelah searched beneath the wagon and counted the arrivals. Yaniel spent the watch working instead of receiving praise. Seelah followed her direction, and they stayed until the relief.{/n}",
    "s29": "{n}Kiana spent the private half-hour binding the wounded scout. Seelah held his arm where the healer directed. Kiana finished the dressing and invited her friend to return.{/n}",
}


def _append_unique(items, value):
    if value not in items:
        items.append(value)


def _current(payload, row, spec):
    """Supported read-only predicates; current route openness includes loss epochs."""
    derived = payload.setdefault("Derived", {})
    forbids = payload.setdefault("DerivedForbids", {})
    opens = payload.setdefault("DerivedOpenRoutes", {})
    clear = P + "commander.not_sacrificed"
    derived[clear] = [["availability.observed"]]
    forbids[clear] = ["sacrifice"]
    alive = P + "commander.alive"
    derived[alive] = [[clear], ["trickster.commander_back"]]
    key = P + row + ".current"
    requirements = ["trickster.now", "foresight.page_taken", "household.table.kept", alive]
    for woman in spec["pair"]:
        requirements.extend([woman + ".present_now", woman + ".harem.eligible"])
    # These existing bodily channels, not a meeting/letter or barrier voice,
    # qualified the authored deed. Retain them for living recollections.
    channels = {
        "s10": ["household.pair.seelah_nenio.body.seelah", "household.pair.seelah_nenio.body.nenio"],
        "s20": ["jannah.trickster.returned"],
        "s21": ["yaniel.freed.latched", "yaniel.trickster.returned"],
        "s29": [s29.P("conscious"), s29.P("met")],
        "s30": ["eliandra.met_ch5", "targona.trickster.in_drezen"],
    }
    derived[key] = [[*requirements, *channels[row]]]
    opens[key] = list(spec["pair"])
    forbids[key] = ["household.closed"]
    if row == "s30":
        forbids[key].append("eliandra.trickster.away")
    return key


def _stage_lines(payload, row, spec, current):
    """Enmity wins before the highest stage; reconciliation remains owner-produced."""
    lines = []
    pending = payload.setdefault("PendingHooks", [])
    for a, b in (spec["pair"], spec["pair"][::-1]):
        edge = a + ".harem.enmity." + b
        mend = a + ".harem.reconciled." + b
        clear = P + row + ".clear." + a
        payload["Derived"][clear] = [["availability.observed"]]
        payload["DerivedForbids"][clear] = [edge]
        peace = P + row + ".speaking." + a
        payload["Derived"][peace] = [[clear], [mend]]
        for flag in (edge, mend, *(a + ".harem.attitude." + b + "." + stage for stage in STAGES)):
            _append_unique(pending, flag)
        lines.append(p('{n}%s will not speak to %s.{/n}' % (a.capitalize(), b.capitalize()),
                       requires=(current, edge), forbids=(mend,)))
        labels = {"rival": "a rival", "respect": "worthy of respect", "friend": "a friend", "lover": "a lover"}
        for index, stage in enumerate(STAGES):
            attitude = a + ".harem.attitude." + b + "."
            lines.append(p('{n}%s regards %s as %s.{/n}' % (a.capitalize(), b.capitalize(), labels[stage]),
                           requires=(current, peace, attitude + stage),
                           forbids=tuple(attitude + above for above in STAGES[index + 1:])))
    return lines


def register(payload, scenes, refs):
    """Run after row producers, append only to existing Epilogue destinations."""
    ledger = payload["Books"]["trickster.ledger"]["Entries"]
    hosts = {scene["Id"]: scene for scene in payload["Scenes"]}
    for row, spec in ROWS.items():
        current = _current(payload, row, spec)
        # Separate current reading: prior historical entries stay byte-for-byte
        # as assembled, and do not acquire an attendance requirement.
        entry = dict(Id=P + row + ".seating", Section="Seating Notes",
                     Portrait=spec["pair"][0].capitalize(), Title=spec["title"] + ": now",
                     Text="{n}The names beside this account have their own present ties.{/n}",
                     Requires=[current], Forbids=[], AnyGroups=[], Tooltip="RRT_SeatingNotes",
                     Lines=_stage_lines(payload, row, spec, current))
        # S21/S29 had no historical Notes on the integration base.
        if row in ("s21", "s29"):
            _append_unique(ledger, dict(
                Id=spec["prefix"] + "seating", Section="Seating Notes",
                Portrait="Seelah", Title=spec["title"], Text="{n}An account from the crusade.{/n}",
                Requires=[spec["seen"]], Forbids=[], AnyGroups=[], Tooltip="RRT_SeatingNotes",
                Lines=[p(HISTORY[row], requires=spec["kept"]),
                       p("{n}" + DEFERRED[row] + "{/n}", requires=(spec["declined"],))]))
        # Kiana/Nenio's route-owned finalizers append after this registry and
        # apply fixed-position contracts. Their new Last Call attachments need
        # the shared finalizer owner; do not shift its indices.
        for woman in spec.get("hosts", spec["pair"]):
            host = hosts[woman + ".lastcall.page"]
            if host["Owner"] != "Epilogue":
                raise ValueError("W5 living reader requires an existing Epilogue: " + host["Id"])
            paragraphs = host["Nodes"][0]["Paragraphs"]
            living = (current, *(body + ".present_now" for body in spec["pair"]))
            if row == "s20":
                for outcome, text in zip(spec["outcomes"], JANNAH):
                    _append_unique(paragraphs, p("{n}" + text + "{/n}", requires=(*living, spec["seen"], outcome)))
                _append_unique(paragraphs, p("{n}The Commander's recollections held no gaol account from Jannah about Seelah.{/n}",
                                            requires=living, forbids=(spec["seen"], *spec["outcomes"])))
            else:
                _append_unique(paragraphs, p(RECALL[row][woman], requires=(*living, *spec["kept"])))
                _append_unique(paragraphs, p("{n}" + DEFERRED[row] + "{/n}", requires=(*living, spec["seen"], spec["declined"])))
                _append_unique(paragraphs, p("{n}" + UNPLAYED[row] + "{/n}", requires=living,
                                            forbids=(spec["seen"], *spec["kept"], spec["declined"])))
        if row == "s29":
            # Current Elan terms are read separately from the old ward deed.
            # Use S29's established precedence without granting any agreement.
            prior = []
            for node_id, flag, text in s29.ACCOUNTS:
                _append_unique(entry["Lines"], p("{n}Kiana's present account of Elan:{/n} " + text,
                                                requires=(current, flag), forbids=prior))
                prior.append(flag)
            _append_unique(entry["Lines"], p("{n}Kiana has supplied no present account of Elan.{/n}",
                                            requires=(current,), forbids=prior))
        _append_unique(ledger, entry)
