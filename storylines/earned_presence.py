"""Earned presence (TRICKSTER-RUBRIC "Binding context (3)" and "(4)", user rules 2026-10-03).

Nothing is free. A Commander who died in the final self-sacrifice (native Ending_PlayerSacrifice, GrandFinal Answer_0017
"[Step into the Wound]") and prepared no return gets no living postwar page: no romance page, epilogue, Last Call coda or
household page that stages {mf|him|her} alive after the war.

The derived state, `trickster.commander_dead`, is

    sacrifice AND NOT trickster.commander_back

where trickster.commander_back (trickster_world.DERIVED) is the OR of every earned return: the Trickster punchline finales
(TT-22, "found a way of cheating death"), Iomedae's bridge (iomedae.appointment_kept, iomedae.trickster.rescued) and Last
Call's flask (H2: the Ledger taken, the Wound closed by the sacrifice, the bottle pillar). Story.Derived is an OR of
AND-groups without negation, so the key is written on a page as one Forbid with its override, never as a Derived entry:

    Forbids "sacrifice", ForbidOverrides {"sacrifice": "trickster.commander_back"}

(Rules.ForbidHolds: the Forbid blocks only while the override does not hold.) A page may instead Require an alive witness
(ALIVE_WITNESSES: a key that implies the Commander walked out of the rift, such as lastcall.active).

integrate() applies that guard to every epilogue-family scene (Owner ...Epilogue: RRT pages, Last Call codas, native-slide
replacements) that does not carry it, unless the page is listed in COMMANDER_ABSENT: a page that mourns the Commander
(Requires "sacrifice"), or one that never stages the Commander alive after the war and so stays true after the death.
PARAGRAPH_GUARDED pages mix living and mourning text and are exempt only after their individual guards are verified.
tools/earned_presence_lint.py checks the result from the generated Story.json (rules EP1-EP6, T1-T7, P1).
"""
import re

SACRIFICE = "sacrifice"
COMMANDER_BACK = "trickster.commander_back"
COMMANDER_DEAD = "trickster.commander_dead"   # documentation name only: written as the guard below
GUARD = {"Forbids": [SACRIFICE], "ForbidOverrides": {SACRIFICE: COMMANDER_BACK}}

# Keys whose presence proves the Commander is alive after the war even when "sacrifice" holds (each one's groups are
# covered by a trickster.commander_back group once "sacrifice" is added; the lint re-proves it from Story.Derived).
ALIVE_WITNESSES = (COMMANDER_BACK, "trickster.cheated_death", "lastcall.active", "lastcall.h1", "lastcall.h2",
                   "lastcall.dead_on_record", "iomedae.appointment_kept", "iomedae.trickster.rescued",
                   "iomedae.trickster.buried_alive")

# Pages that may play after an unreturned sacrifice because they never stage the Commander alive after the war.
# Pages that Require "sacrifice", or a key that implies it (the mourning pages), are exempt without a listing.
COMMANDER_ABSENT = {
    # The trio's loss pages: the future the war took, told without the Commander in the room.
    "ending_loss": "independent",
    "tirabade.negotiated_ending_loss": "independent",
    # Her life after a romance that ended or never began; no postwar meeting with the Commander.
    "jerribeth.ending_unfinished": "independent",
    "kiana.ending_apart": "independent",
    "kiana.ending_unfinished": "independent",
    "kiana.trickster.ending_unfinished": "independent",
    "vellexia.ending_hostility": "independent",
    "arsinoe.trickster.epilogue.foreclosure_closed": "independent",
    "nocticula.trickster.defeated.epilogue.fooled": "independent",
    "nocticula.trickster.defeated.epilogue.mirror": "independent",
    "aranka.trickster.epilogue.declined": "independent",
    "hepzamirah.trickster.epilogue.refused": "independent",
    "targona.trickster.epilogue.declined": "independent",
    "jannah.trickster.epilogue.gone": "independent",
    "terendelev.trickster.epilogue.rest": "independent",
    "irabeth.trickster.epilogue.native_tirabade_south": "independent",
    # Native Queen-slide replacements describe her reign without staging a living Commander (engine-q2 item 5).
    "galfrey.native.queen_reclaimed": "native_queen",
    "galfrey.native.queen_reclaimed_twin": "native_queen",
    # Both women dead: two absences behind an answered invitation; nobody is staged at the table.
    "minachiv.ending_both_lost": "independent",
    "minachiv.ending_both_lost_completed": "independent",
}

# Route pages registered here may be absent from a partial build. When present, every non-mourning text block must
# carry GUARD, and at least one paragraph must mourn the unreturned sacrifice. EP6 checks the exported page too.
PARAGRAPH_GUARDED = {"irabeth.return_epilogue"}

# The mythic-Trickster path (Binding context (4)): a canon change must require one of these, directly or through a
# Derived/Latch/authored key whose every source does. The four Trickster finales exist only on the Trickster path.
TRICKSTER_ROOTS = ("trickster", "trickster.ever", "trickster.was", "trickster.now")

# Engine-q2: the GLOBAL current-path reader (expansion.trickster_engine; Rules.TricksterNow). trickster.ever and
# trickster.was record that the run WAS Trickster; trickster.now holds only while it still IS (it drops at a Chapter 4
# failure or a Goddesses' Summit conversion). earned_presence_lint T6:
# T6a: a native canon change (edit, suppression, gate, settlement) whose When group has no Trickster evidence besides the
#      path latch reads trickster.now (its event can come after the run leaves the path; canon stands off the path).
# T6b: each key below, when the build derives it, reads trickster.now in every group. The foresight public keys
#      (claude/shyka, foresight.py, unmerged here) are the hook: the page's gated outcomes are canon changes made later,
#      so they need the current path; the prices already paid (foresight.memory_gone.*) stay on trickster.ever.
TRICKSTER_NOW = "trickster.now"
TRICKSTER_LATCHES = ("trickster.ever", "trickster.was")
CURRENT_PATH_KEYS = {
    "foresight.page_taken": "Shyka's page opens gated outcomes in later chapters: a canon change made after the bargain",
    "foresight.gate_believed": "the gate watch acts on the page's knowledge at a later native event",
}
NATIVE_TRICKSTER = ("ending.trickster", "ending.trickster_full", "ending.trickster_allplanes", "ending.trickster_allplanes_fw")


def is_epilogue(scene):
    """A postwar page. The Aeon rewrite (Owner "AeonEpilogue") tells a history in which the crusade never happened; it
    stages no postwar Commander and never shares a world with the Wound sacrifice, so it is not a postwar page here."""
    owner = scene.get("Owner") or ""
    return owner.endswith("Epilogue") and owner != "AeonEpilogue"


def implies_sacrifice(key, derived, seen=()):
    """The key holds only when "sacrifice" does: "sacrifice" itself, or a Derived key every group of which has such a key
    (areelu.trickster.commander_burned = sacrifice + the Wound closed)."""
    if key == SACRIFICE:
        return True
    groups = (derived or {}).get(key)
    if not groups or key in seen:
        return False
    return all(any(implies_sacrifice(k, derived, (*seen, key)) for k in g) for g in groups)


def mourning(scene, derived=None):
    """A page that plays only after the sacrifice: it Requires "sacrifice" or a key that implies it."""
    return any(implies_sacrifice(k, derived) for k in scene.get("Requires") or [])


def guarded(scene, derived=None):
    """True when the page cannot play beside a dead Commander, or is a mourning page."""
    requires = set(scene.get("Requires") or [])
    if requires & set(ALIVE_WITNESSES) or mourning(scene, derived):
        return True
    if SACRIFICE in (scene.get("Forbids") or []):
        lift = (scene.get("ForbidOverrides") or {}).get(SACRIFICE)
        return lift is None or lift in ALIVE_WITNESSES
    return False


def paragraph_guard_errors(scene):
    """Conservatively treat every non-mourning node text or paragraph as living; no prose heuristics or silent exemptions."""
    errors = []
    mourns = False
    if SACRIFICE in (scene.get("Forbids") or []):
        errors.append("scene Forbids 'sacrifice', blocking its mourning paragraphs")
    for node in scene.get("Nodes") or []:
        blocks = [(node.get("Id"), node)] if (node.get("Text") or "").strip() else []
        blocks += [("%s/paragraph[%d]" % (node.get("Id"), i), p)
                   for i, p in enumerate(node.get("Paragraphs") or [])]
        for label, block in blocks:
            forbids = block.get("Forbids") or []
            if SACRIFICE in (block.get("Requires") or []):
                mourns |= block is not node
                if COMMANDER_BACK not in forbids or SACRIFICE in forbids:
                    errors.append("%s: mourning text must Forbid %s and must not Forbid 'sacrifice'"
                                  % (label, COMMANDER_BACK))
            elif (SACRIFICE not in forbids
                  or (block.get("ForbidOverrides") or {}).get(SACRIFICE) != COMMANDER_BACK):
                errors.append("%s: living text needs Forbid 'sacrifice' + override %s" % (label, COMMANDER_BACK))
    if not mourns:
        errors.append("no mourning paragraph Requires 'sacrifice'")
    return errors


# Relationships with two women: each page names which of them is present (Chivarro's alone page plays with Minagho dead),
# so their pages carry their own death guards and are not given a per-woman Forbid mechanically.
GROUP_RELATIONSHIPS = ("tirabade", "minagho_chivarro")

# Engine-q5: these departures concern someone else, correspondence, or a dream rather than a physical partner.
DEPARTURE_EXEMPTIONS = {
    ("konomi", "konomi.private_departed"): "Her private romance continues by post; her physical presence explicitly forbids this flag.",
    ("nocticula", "noct.ilvara_exiled"): "Ilvara is the hearing's subject, not Nocticula.",
    ("dorgelinda", "dorgelinda.ledger.driver_sent_home"): "The convoy driver leaves, not Dorgelinda.",
    ("kaylessa", "kaylessa.trickster.wasp_sent_home"): "The wasp is dismissed, not Kaylessa.",
    ("galfrey", "galfrey.trickster.envoy.sent_home"): "The envoy leaves, not Galfrey.",
    ("iomedae", "iomedae.trickster.sent_away"): "Declines the banner dream; no physical Iomedae has arrived.",
}
# Coordinator ruling: a paid return may put her in reach of the scene that completes it.
# This lifts only the named loss for physical presence; relationship and household guards are unchanged.
PRESENCE_RETURN_IN_PROGRESS = {
    "aranka": {
        "aranka.ran_failure": {
            "Flag": "aranka.trickster.answered",
            "Reason": "The paid second verse brings her to Drezen; the physical reckoning earns moral repair.",
        },
    },
}
PRESENCE_CHAPTERS = [["chapter_one"], ["chapter_later"]]


def presence_relationship(key):
    match = re.fullmatch(r"(.+?)\.presence(?:\.[a-z0-9_]+)?", key)
    return match[1] if match else None


def presence_guard(relationship):
    return relationship + ".presence.route_open"


def presence_guard_fields(rel, relationship):
    """Compile only listed returns into presence guards, using existing DerivedForbids."""
    key = presence_guard(rel)
    fields = {"Derived": {key: [list(g) for g in PRESENCE_CHAPTERS]}}
    progress = PRESENCE_RETURN_IN_PROGRESS.get(rel)
    if not progress:
        fields["DerivedOpenRoutes"] = {key: [rel]}
        return fields
    blockers = [relationship["ClosedFlag"]]
    forbids = fields["DerivedForbids"] = {}
    for flag in relationship.get("UnavailableFlags") or []:
        blocked = key + ".blocked." + flag
        fields["Derived"][blocked] = [[flag]]
        blockers.append(blocked)
        lifts = list(dict.fromkeys(filter(None, [
            (relationship.get("UnavailableOverrides") or {}).get(flag),
            (progress.get(flag) or {}).get("Flag"),
        ])))
        if lifts:
            forbids[blocked] = lifts
    forbids[key] = blockers
    return fields


def integrate_presences(payload):
    """Physical presences obey route closure, with only documented paid returns in progress."""
    for name, presence in (payload.get("Presences") or {}).items():
        rel = presence_relationship(name)
        if rel not in payload["Relationships"]:
            continue
        key = presence_guard(rel)
        for field, guards in presence_guard_fields(rel, payload["Relationships"][rel]).items():
            entries = payload.setdefault(field, {})
            for guard, value in guards.items():
                if guard in entries and entries[guard] != value:
                    raise ValueError("Conflicting presence route guard: " + guard)
                entries[guard] = value
        if key not in (presence.get("Requires") or []):
            presence["Requires"] = [*(presence.get("Requires") or []), key]


def committed_page(scene, relationship):
    requires = scene.get("Requires") or []
    return relationship.get("CommittedFlag") in requires or any(k.endswith("late_committed") for k in requires)


def her_missing_guards(scene, relationship, derived=None):
    """Her own loss flags with an earned return (relationship UnavailableOverrides) that a committed page neither Forbids
    nor Requires (nor Requires the return for). Aeon pages (a history in which the crusade never happened) and the
    two-woman relationships (GROUP_RELATIONSHIPS) are exempt.
    A Story.Derived loss flag (which a ForbidOverride may not name) counts as forbidden when every one of its groups has a
    forbidden member (chadali.lost_at_council: the page forbids council.fought and council.fought_nocta_allied)."""
    if (not committed_page(scene, relationship) or "aeon" in scene["Id"]
            or (scene.get("Relationship") or "tirabade") in GROUP_RELATIONSHIPS):
        return []
    requires, forbids = set(scene.get("Requires") or []), scene.get("Forbids") or []
    returns = relationship.get("UnavailableOverrides") or {}

    def covered(flag):
        groups = (derived or {}).get(flag)
        return flag in forbids or bool(groups) and all(any(k in forbids for k in g) for g in groups)
    return [(flag, ret) for flag, ret in returns.items()
            if not covered(flag) and flag not in requires and ret not in requires]


def integrate(payload):
    """Guard living postwar pages, validate paragraph exemptions, and remove the two realm slides' Commander guards.
    Returns the guarded scene ids for the build log and the tests."""
    integrate_presences(payload)
    from storylines import trickster_world   # the route composites not yet bound into the payload
    derived = {**trickster_world.DERIVED, **(payload.get("Derived") or {})}
    added = []
    for s in payload["Scenes"]:
        if not is_epilogue(s):
            continue
        # These two realm slides inherited an explicit Commander guard; their subject is Galfrey's reign.
        if COMMANDER_ABSENT.get(s["Id"]) == "native_queen":
            s["Forbids"] = [f for f in s.get("Forbids") or [] if f != SACRIFICE]
            s["ForbidOverrides"] = {f: lift for f, lift in (s.get("ForbidOverrides") or {}).items() if f != SACRIFICE}
        if s["Id"] in PARAGRAPH_GUARDED:
            errors = paragraph_guard_errors(s)
            if errors:
                raise ValueError("Earned presence: %s: %s" % (s["Id"], "; ".join(errors)))
            continue
        if s["Id"] in COMMANDER_ABSENT or guarded(s, derived):
            continue
        # Routes share Forbids lists and ForbidOverrides dicts between pages (**EP); copy before appending.
        overrides = dict(s.get("ForbidOverrides") or {})
        if SACRIFICE in overrides:
            raise ValueError("Earned presence: %s lifts 'sacrifice' with %r, which is not an earned return"
                             % (s["Id"], overrides[SACRIFICE]))
        s["Forbids"] = [*(s.get("Forbids") or []), SACRIFICE]
        overrides[SACRIFICE] = COMMANDER_BACK
        s["ForbidOverrides"] = overrides
        added.append(s["Id"])
    # Her own presence: a committed page never stages her alive after her death or departure unless her earned return
    # (the relationship's UnavailableOverrides value, Trickster-only or a canon reading) holds.
    for s in payload["Scenes"]:
        rel = payload["Relationships"].get(s.get("Relationship") or "tirabade")
        if not is_epilogue(s) or rel is None:
            continue
        for flag, ret in her_missing_guards(s, rel, derived):
            overrides = dict(s.get("ForbidOverrides") or {})
            if flag in overrides:
                continue
            if flag in derived:
                raise ValueError("Earned presence: %s stages %s alive without guarding the composite %s; forbid its sources"
                                 % (s["Id"], s.get("Relationship"), flag))
            s["Forbids"] = [*(s.get("Forbids") or []), flag]
            overrides[flag] = ret
            s["ForbidOverrides"] = overrides
            added.append(s["Id"] + "!" + flag)
    return added
