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
tools/earned_presence_lint.py checks the result from the generated Story.json (rules EP1-EP4, T1-T5).
"""

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
    # Both women dead: two absences behind an answered invitation; nobody is staged at the table.
    "minachiv.ending_both_lost": "independent",
    "minachiv.ending_both_lost_completed": "independent",
}

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


# Relationships with two women: each page names which of them is present (Chivarro's alone page plays with Minagho dead),
# so their pages carry their own death guards and are not given a per-woman Forbid mechanically.
GROUP_RELATIONSHIPS = ("tirabade", "minagho_chivarro")


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
    """Append the commander_dead guard to every unguarded postwar page (append-only: Forbids and one override).
    Returns the guarded scene ids for the build log and the tests."""
    from storylines import trickster_world   # the route composites not yet bound into the payload
    derived = {**trickster_world.DERIVED, **(payload.get("Derived") or {})}
    added = []
    for s in payload["Scenes"]:
        if not is_epilogue(s) or s["Id"] in COMMANDER_ABSENT or guarded(s, derived):
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
