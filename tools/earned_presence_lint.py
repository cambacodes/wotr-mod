#!/usr/bin/env python3
"""earned_presence_lint.py - nothing is free (TRICKSTER-RUBRIC "Binding context (3)" and "(4)", 2026-10-03).

Reads the generated Story.json. HARD rules (exit 1):

EP1 living postwar page: every epilogue-family scene (Owner ends with "Epilogue": RRT pages, Last Call codas, native-slide
    replacements) Forbids "sacrifice" (bare, or lifted only by an alive witness), Requires an alive witness, Requires
    "sacrifice" (a mourning page), is listed in storylines/earned_presence.COMMANDER_ABSENT, or passes EP6. This is the derived state
    trickster.commander_dead = sacrifice AND NOT trickster.commander_back, written as a Forbid plus its override.
EP2 mourning page: an epilogue page that Requires "sacrifice" (or a Derived key that implies it) Forbids
    trickster.commander_back (it never plays beside a Commander who came back), and does not Forbid "sacrifice" (a
    contradiction: the page could never play).
EP3 alive witness: every ALIVE_WITNESSES key is trickster.commander_back or a Derived key each of whose groups, with
    "sacrifice" added, contains a trickster.commander_back group (trickster.ever counted when the group implies it).
EP4 allowlist: every COMMANDER_ABSENT id is an epilogue scene that does not Forbid "sacrifice" (a listed page must be
    one that is meant to play after the death; a stale or contradictory listing fails).
T1 return device: every relationship UnavailableOverrides value and TricksterAccess Returned key implies the Trickster
    path (below), or (UnavailableOverrides only) is a canon reading: a Derived key each group of which implies the
    Trickster path or holds only native keys. Off-Trickster, canon fate stands.
T2 native epilogue edit (E14d): every When group of every variant contains a Trickster-implying key.
T3 native gate (E18): every When group contains a Trickster-implying key.
T4 revival: every choice that revives a unit (Choice.Revive) sits in a Trickster-implying scene or choice.
T5 lifted loss: every ForbidOverrides entry that lifts a woman's loss flag (a relationship UnavailableFlag, Commander path
    flags excepted) or "sacrifice" names a Trickster-implying key or a canon reading (as T1).

T6 current path (engine-q2): trickster.ever is the run latch (the run WAS Trickster); trickster.now holds only while it
    still IS. T6a: every When group of a native edit, suppression, gate or settlement Requires trickster.now, or holds a
    key that only a Trickster act sets (implied with the latches trickster.ever/trickster.was NOT counted as evidence:
    Devarra flown, the guests ransomed, a return). A canon change whose only Trickster evidence is the path latch would
    still fire after a Chapter 4 failure or a Summit conversion. T6b: each storylines/earned_presence.CURRENT_PATH_KEYS key
    that the build derives Requires trickster.now in every group (the foresight public keys' hook).
T7 return/device producers and revivals require trickster.now, or live trickster with trickster.failed forbidden.
    Earned return consumers retain historical trickster.ever; authored flags and latches cannot prove current power.
P1 every physical relationship presence requires the generated route guard.
    Only PRESENCE_RETURN_IN_PROGRESS may lift a loss before reconciliation, with a reason.
    Departure flags set by routes must be UnavailableFlags or have a documented exemption.

EP5 her presence: a committed epilogue page (Requires the CommittedFlag or a *late_committed key; Aeon pages exempt)
    Forbids each of her loss flags that has an earned return (relationship UnavailableOverrides), lifted by that return,
    or Requires the flag or its return.
EP6 paragraph-guarded page: each present PARAGRAPH_GUARDED scene is an epilogue with no scene-level sacrifice Forbid.
    Every non-mourning node text and paragraph Forbids sacrifice with ForbidOverrides {sacrifice: trickster.commander_back}.
    At least one mourning paragraph Requires sacrifice; mourning text Forbids trickster.commander_back and not sacrifice.

REVIEW (advisory, printed with --review): committed epilogue pages that neither Forbid nor Require one of her loss flags
that has NO registered return (a native state whose meaning the route owns: e.g. konomi.retained_dead,
galfrey.killed_by_commander, arsinoe.victims_revived). Each needs a route-owner ruling, not a mechanical Forbid.

"Implies the Trickster path": trickster / trickster.ever / trickster.was; a native Trickster finale; a Derived key whose
every group has an implying key; a Latch whose every source implies; an authored flag (or scene id) every setter of which
sits in a scene whose Requires (or RequiresAnyGroups group, all members) or whose choice Requires holds an implying key.

Usage: python tools/earned_presence_lint.py [--story development/Story.json] [--review]
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from storylines import earned_presence as ep   # noqa: E402
# eng7-l06: validation reads export data, never a generation-time module mutation.
from tools import presence_exception_schema, presence_dependency_lint, presence_failure_lint
from tools.player_text_lint import narration_free
# eng7-l06 end

NATIVE_KINDS = ("Etudes", "CompletedQuests", "SeenCues", "SelectedAnswers", "StartedDialogs", "CompletedEtudes",
                "UnlockableFlags", "QuestObjectives", "InventoryItems", "StartedQuests", "MainCharacterFacts")
COMMANDER_PATHS = {"swarm", "true_lich", "devil", "demon", "lich", "legend", "dragon", "inhuman", "ascended",
                   "trickster.failed"}


class Trickster:
    """Does a key imply the mythic-Trickster path? Memoized, conservative on cycles and unknown keys."""

    def __init__(self, story, roots=None, never=()):
        self.roots = set(ep.TRICKSTER_ROOTS if roots is None else roots)
        self.never = set(never)   # keys that prove nothing (T6: the run latches)
        self.derived = story.get("Derived") or {}
        self.latches = story.get("Latches") or {}
        self.memo = {}
        self.native = {k for kind in NATIVE_KINDS for k in (story.get(kind) or {})}
        self.setters = {}   # flag -> list of (scene, choice or None)
        for s in story.get("Scenes") or []:
            self.setters.setdefault(s["Id"], []).append((s, None))
            for n in s.get("Nodes") or []:
                for c in n.get("Choices") or []:
                    for f in c.get("Set") or []:
                        self.setters.setdefault(f, []).append((s, c))

    def context(self, scene, choice=None):
        if any(self.implies(k) for k in scene.get("Requires") or []):
            return True
        if any(g and all(self.implies(k) for k in g) for g in scene.get("RequiresAnyGroups") or []):
            return True
        return choice is not None and any(self.implies(k) for k in choice.get("Requires") or [])

    def implies(self, key):
        if key in self.memo:
            return self.memo[key]
        self.memo[key] = False   # in progress: a cycle proves nothing
        if key in self.never:
            out = False
        elif key in self.roots or key in ep.NATIVE_TRICKSTER:
            out = True
        elif key in self.derived:
            out = all(any(self.implies(k) for k in g) for g in self.derived[key])
        elif key in self.latches:
            out = all(self.implies(k) for k in self.latches[key])
        elif key in self.setters:
            out = all(self.context(s, c) for s, c in self.setters[key])
        else:
            out = False
        self.memo[key] = out
        return out

    def group_ok(self, group):
        return any(self.implies(k) for k in group)

    def lift_ok(self, key):
        """A lift is earned on the Trickster path, or is only a canon reading of native state (each Derived group either
        implies the Trickster path or is all native keys: Vellexia spared in her final fight, Camellia's kick-out that is
        her native Q3 kill). A canon reading changes nothing off-Trickster."""
        if self.implies(key):
            return True
        groups = self.derived.get(key)
        return bool(groups) and all(self.group_ok(g) or all(k in self.native for k in g) for g in groups)


def loss_flags(rel):
    return [f for f in rel.get("UnavailableFlags") or [] if f not in COMMANDER_PATHS]


def live_context(story, scene, choice=None):
    """Earned flags and latches describe past acts, so only live native/Derived evidence proves a new act."""
    def live(key, seen=()):
        if key == ep.TRICKSTER_NOW:
            return True
        groups = (story.get("Derived") or {}).get(key)
        if not groups or key in seen:
            return False
        return all(any(live(k, (*seen, key)) for k in g) for g in groups)

    requires = [*(scene.get("Requires") or []), *((choice or {}).get("Requires") or [])]
    forbids = [*(scene.get("Forbids") or []), *((choice or {}).get("Forbids") or [])]
    if any(live(k) for k in requires):
        return True
    if "trickster" in requires and "trickster.failed" in forbids:
        return True
    return any(g and all(live(k) or k == "trickster" and "trickster.failed" in forbids for k in g)
               for g in scene.get("RequiresAnyGroups") or [])


# eng8-q8b begin: T6c nominates consumers, independently of producer T7.
def left_trickster_consumers(story):
    contract = json.loads((ROOT / "tools/left_trickster_consumer_contracts.json").read_text(encoding="utf-8"))
    if contract["relationship"] not in story.get("Relationships", {}):
        return []
    by_id = {s["Id"]: s for s in story.get("Scenes", [])}
    errors = []
    required_scenes = [*contract["scenes"], *(
        contract["court_prefix"] + name + suffix
        for name in contract["native_twin_roots"] for suffix in ("", ".native_visit"))]
    for sid in required_scenes:
        if sid not in by_id:
            errors.append("T6c %s: missing registered survival consumer" % sid)
    for sid, scene in by_id.items():
        if sid in contract["scenes"] or sid.startswith(contract["court_prefix"]):
            # The explicit entry contract remains required even when a reward
            # choice or historical return happens to imply additional guards.
            if "trickster.now" not in scene.get("Requires", []):
                errors.append("T6c %s: authored courtship/survival consumer must require trickster.now" % sid)
    reader = contract["return_reader"]
    if (story.get("Derived", {}).get(reader) != contract["return_groups"]
            or story.get("DerivedForbids", {}).get(reader) != contract["return_forbids"]):
        errors.append("T6c %s: legacy survival lift must read current path and actor validity" % reader)
    return errors
# eng8-q8b end


def return_producers(story):
    """Resolve return composites to their authored producers; native readings need no new act."""
    keys = set()
    def visit(key):
        if not key or key in keys:
            return
        keys.add(key)
        for group in (story.get("Derived") or {}).get(key) or []:
            for source in group:
                visit(source)
        for source in (story.get("Latches") or {}).get(key) or []:
            visit(source)
    # eng7-l06
    for declaration in (story.get("PresenceExceptions") or {}).values():
        for entry in declaration.get("Overrides", {}).values():
            visit(entry.get("Flag"))
    for rel in (story.get("Relationships") or {}).values():
        for key in (rel.get("UnavailableOverrides") or {}).values():
            visit(key)
        for access in (rel.get("TricksterAccess") or {}).values():
            visit(access.get("Returned"))
            visit(access.get("Device"))
    return keys


DEPARTURE_FLAG = re.compile(r"(?:^|[._])(?:left_free|gone(?:_to_[a-z0-9_]+)?|departed|expelled|banished|dismissed|sent_home|sent_away|exiled|ran_off)$")
DEVICE_COMPLETION_FLAG = re.compile(r"(?:^|[._])device[._](?:done|complete|completed)$")


def producer_presence_errors(story):
    """T7 producers use current power; P1 physical partners obey RouteOpen and register departures."""
    hard = []
    producers = return_producers(story)
    rels = story.get("Relationships") or {}
    trk = Trickster(story)
    # eng7-l06: every pending return must have an existing current-Trickster producer (cell acquisition is native).
    for name, declaration in (story.get("PresenceExceptions") or {}).items():
        for flag, entry in declaration.get("Overrides", {}).items():
            if not trk.implies(entry.get("Flag")):
                hard.append("P1 %s: bootstrap %s needs a Trickster-earned producer" % (name, flag))
    for s in story.get("Scenes") or []:
        if (s["Id"] in producers or s.get("TricksterDevice")) and not live_context(story, s):
            hard.append("T7 %s: device completion needs trickster.now or trickster with trickster.failed forbidden" % s["Id"])
        for n in s.get("Nodes") or []:
            for i, c in enumerate(n.get("Choices") or []):
                flags = {f for f in c.get("Set") or [] if f in producers or DEVICE_COMPLETION_FLAG.search(f)}
                if (flags or c.get("Revive")) and not live_context(story, s, c):
                    hard.append("T7 %s/%s/choice[%d]: return producer %s needs the current Trickster path"
                                % (s["Id"], n.get("Id"), i, sorted(flags) or "Revive"))
                rel = s.get("Relationship") or "tirabade"
                # eng8-q8a: the nominated bodily-departure receipt co-produces
                # the existing romance closure; its independent living ending stays available.
                from tools.return_provenance_lint import registered_closing_departure
                for flag in c.get("Set") or []:
                    if (DEPARTURE_FLAG.search(flag) and flag not in (rels.get(rel) or {}).get("UnavailableFlags", [])
                            and not (ep.DEPARTURE_EXEMPTIONS.get((rel, flag)) or "").strip()
                            and not registered_closing_departure(rel, s["Id"], n["Id"], i, c, flag)):  # eng8-q8a
                        hard.append("P1 %s: departure %s must be in %s.UnavailableFlags or allowlisted with a reason"
                                    % (s["Id"], flag, rel))
    # eng7-l06: dependency checking is separate from q6a's L1 consumer-presence lint.
    hard.extend(presence_exception_schema.errors(story))
    hard.extend(presence_failure_lint.check(story))
    # eng7-f4: the strict verifier covers contact/return dependencies on every route.
    hard.extend(presence_dependency_lint.check(story))
    # eng7-f4 end
    return hard


def check(story, review=False):
    hard, notes = producer_presence_errors(story), []
    scenes = story.get("Scenes") or []
    by_id = {s["Id"]: s for s in scenes}
    rels = story.get("Relationships") or {}
    trk = Trickster(story)
    back = (story.get("Derived") or {}).get(ep.COMMANDER_BACK)
    if not back:
        hard.append("EP3 %s is not a Derived key" % ep.COMMANDER_BACK)
        back = []

    # EP3: every alive witness is proved from Story.Derived.
    for w in ep.ALIVE_WITNESSES:
        if w == ep.COMMANDER_BACK or [w] in back:
            continue
        groups = (story.get("Derived") or {}).get(w)
        if groups is None:
            continue   # not used by this build; nothing can Require it
        for g in groups:
            have = set(g) | {ep.SACRIFICE} | ({"trickster.ever"} if trk.group_ok(g) else set())
            if not any(set(h) <= have for h in back):
                hard.append("EP3 alive witness %s: group %s does not imply trickster.commander_back once 'sacrifice' "
                            "holds" % (w, g))

    # eng7-l12: paragraph contracts apply even to mourning/allowlisted pages.
    from storylines.engine_q7_l12 import DEAD, inventory
    contracts = inventory("commander_block_contracts.json")["continuations"]
    dead_defined = ((story.get("Derived") or {}).get(DEAD) == [[ep.SACRIFICE]]
                    and (story.get("DerivedForbids") or {}).get(DEAD) == [ep.COMMANDER_BACK])
    for scene in scenes:
        if not ep.is_epilogue(scene) or (ep.guarded(scene, story.get("Derived")) and not ep.mourning(scene, story.get("Derived"))):
            continue
        for node in scene.get("Nodes") or []:
            for index, paragraph in enumerate(node.get("Paragraphs") or []):
                if any(narration_free(paragraph.get("Text", "")).startswith(c["prefix"]) for c in contracts):
                    if not (dead_defined and DEAD in (paragraph.get("Forbids") or [])):
                        hard.append("EP6 %s/%s/paragraph[%d]: living continuation lacks earned Commander survival" %
                                    (scene["Id"], node["Id"], index))

    # EP1 / EP2: postwar pages.
    for s in scenes:
        if s["Id"] in ep.PARAGRAPH_GUARDED:
            if not ep.is_epilogue(s):
                hard.append("EP6 %s: PARAGRAPH_GUARDED scene is not an epilogue" % s["Id"])
            for why in ep.paragraph_guard_errors(s):
                hard.append("EP6 %s/%s" % (s["Id"], why))
            continue
        if not ep.is_epilogue(s):
            continue
        req, forb = set(s.get("Requires") or []), s.get("Forbids") or []
        if req & set(ep.ALIVE_WITNESSES):
            continue
        if ep.mourning(s, story.get("Derived")):
            if ep.COMMANDER_BACK not in forb:
                hard.append("EP2 %s mourns the Commander (Requires sacrifice or a key implying it) but does not Forbid %s"
                            % (s["Id"], ep.COMMANDER_BACK))
            if ep.SACRIFICE in forb:
                hard.append("EP2 %s mourns the Commander but Forbids 'sacrifice': it can never play" % s["Id"])
            continue
        if s["Id"] in ep.COMMANDER_ABSENT:
            continue
        if not ep.guarded(s, story.get("Derived")):
            lift = (s.get("ForbidOverrides") or {}).get(ep.SACRIFICE)
            why = ("lifts 'sacrifice' with %r, which is not an alive witness" % lift) if lift else \
                "stages a postwar page with no commander_dead guard (Forbid 'sacrifice' + override %s)" % ep.COMMANDER_BACK
            hard.append("EP1 %s [%s]: %s" % (s["Id"], s.get("Relationship") or "tirabade", why))

    # EP4: the allowlist is live and coherent.
    for sid, reason in sorted(ep.COMMANDER_ABSENT.items()):
        s = by_id.get(sid)
        if s is None or not ep.is_epilogue(s):
            hard.append("EP4 COMMANDER_ABSENT lists %s, which is not an epilogue scene" % sid)
        elif ep.SACRIFICE in (s.get("Forbids") or []):
            hard.append("EP4 COMMANDER_ABSENT lists %s (%s), but it Forbids 'sacrifice'; drop the listing" % (sid, reason))

    # T1: return devices.
    for name, rel in sorted(rels.items()):
        for flag, ret in sorted((rel.get("UnavailableOverrides") or {}).items()):
            if not trk.lift_ok(ret):
                hard.append("T1 %s: UnavailableOverrides %s -> %s does not imply the Trickster path" % (name, flag, ret))
        for state, acc in sorted((rel.get("TricksterAccess") or {}).items()):
            ret = acc.get("Returned")
            if ret and not trk.implies(ret):
                hard.append("T1 %s: TricksterAccess %s Returned %s does not imply the Trickster path" % (name, state, ret))

    # T2: native epilogue edits.
    for cue, edit in sorted((story.get("NativeEpilogueEdits") or {}).items()):
        for v in [edit] + list(edit.get("Variants") or []):
            for g in v.get("When") or []:
                if not trk.group_ok(g):
                    hard.append("T2 native edit %s / %s: When group %s does not require the Trickster path"
                                % (cue, v.get("Replacement"), g))

    # T3: native gates.
    for name, gate in sorted((story.get("NativeGates") or {}).items()):
        for g in gate.get("When") or []:
            if not trk.group_ok(g):
                hard.append("T3 native gate %s: When group %s does not require the Trickster path" % (name, g))

    # T4 / T5: revivals and lifted losses.
    losses = {f for rel in rels.values() for f in loss_flags(rel)} | {ep.SACRIFICE}
    for s in scenes:
        for n in s.get("Nodes") or []:
            for c in n.get("Choices") or []:
                if c.get("Revive") and not trk.context(s, c):
                    hard.append("T4 %s/%s: a revival outside the Trickster path" % (s["Id"], n.get("Id")))
        for flag, lift in sorted((s.get("ForbidOverrides") or {}).items()):
            if flag in losses and not trk.lift_ok(lift):
                hard.append("T5 %s: ForbidOverrides %s -> %s lifts a loss off the Trickster path" % (s["Id"], flag, lift))

    # T6: the current path. `act` proves a Trickster act without the run latches (the live power and trickster.now count).
    act = Trickster(story, roots=[k for k in ep.TRICKSTER_ROOTS if k not in ep.TRICKSTER_LATCHES], never=ep.TRICKSTER_LATCHES)

    def present(group):
        pos = [k for k in group if not k.startswith("!")]
        return ep.TRICKSTER_NOW in pos or any(act.implies(k) for k in pos if k not in ep.TRICKSTER_ROOTS)

    changes = []
    for cue, edit in sorted((story.get("NativeEpilogueEdits") or {}).items()):
        for v in [edit] + list(edit.get("Variants") or []):
            changes.append(("native edit %s / %s" % (cue, v.get("Replacement")), v.get("When") or []))
    for kind, label in (("NativeEpilogueSuppressions", "native suppression"), ("NativeGates", "native gate"),
                        ("NativeObjectiveSettlements", "native settlement"),
                        ("NativeAnswerEdits", "native answer edit")):  # eng7-f1: same current-path discipline
        for name, spec in sorted((story.get(kind) or {}).items()):
            changes.append(("%s %s" % (label, name), spec.get("When") or []))
    for what, groups in changes:
        for g in groups:
            if trk.group_ok(g) and not present(g):
                hard.append("T6a %s: When group %s has no Trickster evidence but the path latch; read %s (its event can "
                            "come after the run leaves the path)" % (what, g, ep.TRICKSTER_NOW))
    for key, why in sorted(ep.CURRENT_PATH_KEYS.items()):
        for g in (story.get("Derived") or {}).get(key) or []:
            if ep.TRICKSTER_NOW not in g:
                hard.append("T6b %s: group %s does not read %s (%s)" % (key, g, ep.TRICKSTER_NOW, why))

    # eng8-q8b begin
    hard.extend(left_trickster_consumers(story))
    # eng8-q8b end

    # EP5: her own loss with an earned return, on committed pages.
    for s in scenes:
        rel = rels.get(s.get("Relationship") or "tirabade")
        if ep.is_epilogue(s) and rel is not None:
            for flag, ret in ep.her_missing_guards(s, rel, story.get("Derived")):
                hard.append("EP5 %s: committed page stages her alive without Forbid %s (override %s)" % (s["Id"], flag, ret))

    # REVIEW: her own loss on committed pages.
    if review:
        for s in scenes:
            if not ep.is_epilogue(s):
                continue
            rel = rels.get(s.get("Relationship") or "tirabade") or {}
            req = set(s.get("Requires") or [])
            if rel.get("CommittedFlag") not in req and not any(k.endswith("late_committed") for k in req):
                continue
            ov = rel.get("UnavailableOverrides") or {}
            miss = [f for f in loss_flags(rel) if f not in (s.get("Forbids") or []) and f not in req and ov.get(f) not in req
                    and f not in ov]
            if miss:
                notes.append("REVIEW %s: committed page neither Forbids nor Requires her loss flag(s) %s" % (s["Id"], miss))
    # eng7-l07: own consumers and return provenance extend EP5; q6a retains L1/L4/L6 ownership.
    from tools import own_life_lint, return_provenance_lint
    hard.extend(own_life_lint.check(story))
    hard.extend(return_provenance_lint.check(story))
    # eng7-l07 end
    return hard, notes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--story", default=str(ROOT / "development" / "Story.json"))
    ap.add_argument("--review", action="store_true", help="also print the advisory REVIEW lines")
    args = ap.parse_args(argv)
    story = json.loads(Path(args.story).read_text(encoding="utf-8"))
    hard, notes = check(story, review=args.review)
    for line in hard + notes:
        print(line)
    print("earned presence: %d hard, %d review" % (len(hard), len(notes)))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
