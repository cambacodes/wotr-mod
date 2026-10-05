"""L1: cross-route names and speaking cues read central earned presence."""
import re
from .common import AND, OR, lit, fields, finding, roster, route_guard, excerpt_at, postwar, after_mutations, dependencies
from .mention_context import live_mentions

ACTION = re.compile(r"\b(?:stands?|stood|sits?|sat|leans?|waits?|steps?|walks?|enters?|arrives?|joins?|nods?|smiles?|laughs?|says?|said|asks?|answers?|touches?|takes?|holds?|watches?|turns?|comes?|moves?|puts?|drinks?|sings?|offers?|grins?|lifts?|reaches?|pushes?|pulls?|folds?|sets?|kisses?|embraces?|stayed|joined|arrived|beside|across from|at the table)\b", re.I)

# eng7-l14: verified native audiences, not authored availability shortcuts.
# blueprints.zip: c2_vs/DrezenSiege/Final_Battle_Middle/Cue_0016
# (7be28a11; enGB 94b9121c) addresses the Commander as Minagho; c5/
# Drezen_Under_Siedge/Goddesses_Summit/Cue_0033 and its siblings use
# Nocticula's BlueprintUnit 0cca8c84. These lists already stage the actor.
NATIVE_AUDIENCES = {
    # eng7-l14: MeetCamelia/Cue_0007 (a3b4f763acce63b499983c4a47f652d4,
    # native Seelah 54be53f0) introduces the caves' party before this list.
    "seelah": ("1ca6cf08fceeac141a0df689cecc784a", {0}),
    "minagho": ("41dff710486d05d49bbb663f729ddabd", {2}),
    "nocticula": ("7f18896facfbd614c96e2e4ea2d6c0d5", {5}),
}

# eng7-l14: independent Tirabade refusals leave the native wife/officer in
# place. Other routes use closure for departures, dismissal or hard refusal;
# their existing RouteOpen closure remains part of cross-route availability.
LIVING_AFTER_ROMANCE_REFUSAL = {"irabeth", "anevia"}
NATIVE_COMPANIONS = {"seelah", "ember", "nenio", "arueshalae", "wenduag", "camellia"}

# eng7-l14: these canon-dead bodies have no native death loss in Relationships.
# Read their existing, paid return producers instead of treating an empty loss
# list as proof that a body exists. This grants no return or extra price.
BODY_RETURNS = {w: w + ".trickster.returned" for w in ("hepzamirah", "terendelev", "delamere")}
PRESENCE_LOSSES = {"nidalynn": ["nidalynn.trickster.left_with_it"],
                   "terendelev": ["terendelev.parent_lich_bind"]}


def local_return_overrides(story, scene, woman):
    """eng7-l14: retain the Long Con's existing paid native-host adapter.

    Its original book contract and native-contact tests explicitly lift the
    gone alias after Irabeth's registered return. This is not a global gone
    override: other routes and later departures keep their original vetoes.
    """
    if scene is None or woman != "irabeth" or scene.get("Relationship") != "longcon":
        return {}
    returned = story["Relationships"]["irabeth"].get("UnavailableOverrides", {}).get("irabeth_dead")
    if not returned or scene.get("ForbidOverrides", {}).get("irabeth_gone") != returned:
        return {}
    native_host = (story.get("Presences", {}).get("irabeth.presence") or {}).get("Unit")
    if (scene.get("Owner") == "Irabeth" and
            (native_host and scene.get("ContactUnit") == native_host or scene.get("Kind") == "letter")):
        return {"irabeth_gone": returned}
    return {}


def correspondence_reference(block, woman):
    """Existing authored courier offers/receipts never put Anevia in Drezen.

    The pen is surrendered in second_ask; nevi_reply requires pen_sent and
    waits three days. Only these letter clauses read distant life. Staged
    encounters and returned gate scenes still need the full presence guard.
    """
    # Native witness: ccd140dbf2603734aa323261c2445bec, Epilogues/Cue_0310;
    # enGB cc716238-3702-4913-977d-6189665672b7 sends Anevia and living
    # Irabeth away together after humiliation, not after Irabeth's death.
    # eng7-l14: native Irabeth_gone sends the living Tirabades south
    # together. The existing paid wardrobe reaches Anevia's lodging there;
    # these clauses never return Irabeth to Drezen or reopen her romance.
    native_visits = {
        "anevia.trickster.gone.wardrobe": ({"trickster.now", "anevia.trickster.primed", "anevia_gone"}, {"beth_left"}),
        "anevia.trickster.gone.gate": ({"anevia.trickster.returned"}, {"beth_left", "told_left"}),
        "anevia.trickster.gone.commit": ({"anevia.trickster.returned", "anevia.trickster.gate_seen"}, {"morning_left", "morning_back", "morning_quiet"}),
        "anevia.trickster.epilogue.native_tirabade_left": ({"anevia.trickster.returned"}, {"page"}),
        "anevia.trickster.epilogue.native_tirabade_left_committed": ({"anevia.trickster.returned", "anevia.committed"}, {"page"}),
    }
    if woman == "irabeth":
        spec = native_visits.get(block.scene["Id"])
        return bool(spec and spec[0] <= set(block.scene.get("Requires", [])) and block.node["Id"] in spec[1])
    if woman != "anevia":
        return False
    required = {"trickster.ever", "irabeth.trickster.declined", "irabeth.trickster.back_on_duty"} if block.scene["Id"] == "irabeth.trickster.second_ask" else {"trickster.ever", "irabeth.trickster.pen_sent"}
    if not required <= set(block.scene.get("Requires", [])):
        return False
    if block.scene["Id"] == "irabeth.trickster.second_ask" and block.node["Id"] == "price":
        return "I'll send it to Nevi. If she sends it back" in block.node.get("Text", "")
    if (block.scene["Id"] in ("irabeth.trickster.second_ask", "irabeth.trickster.nevi_reply")
            and block.node["Id"] == "morning"):
        return "I'll write to her myself before breakfast" in block.text
    return False


def presence_guard(model, route, woman, block=None):
    """A Tirabade romance refusal is not a death or a departure.

    Cross-route ordinary dialogue may still address a living Tirabade officer
    or wife. Other routes retain closure, including hard departures.
    Own romance pages and household seats retain their existing RouteOpen gates;
    this check never grants a romance, clears a closure or earns a return.
    """
    guard = route_guard(model, route, woman)
    closed_guard = lit(model.rels[route]["ClosedFlag"], False)
    excluded = ({closed_guard} if woman in LIVING_AFTER_ROMANCE_REFUSAL | NATIVE_COMPANIONS else set())
    if block is not None and correspondence_reference(block, woman):
        away = woman + "_gone"
        back = model.rels[route].get("UnavailableOverrides", {}).get(away)
        excluded.add(OR(lit(away, False), lit(back)) if back else lit(away, False))
    parts = guard[1:] if guard[0] == "and" else (guard,)
    local = local_return_overrides(model.story, block.scene if block else None, woman)
    excluded.update(lit(loss, False) for loss in local)
    closure = (OR(closed_guard, AND(*(lit(f, False) for f in model.rels[route].get("UnavailableFlags", []))))
               if woman in NATIVE_COMPANIONS else AND())
    return AND(*(part for part in parts if part not in excluded), closure,
               *(OR(lit(loss, False), lit(back)) for loss, back in local.items()),
               *(lit(f, False) for f in PRESENCE_LOSSES.get(woman, [])),
               *((lit("trickster.ever"), lit(BODY_RETURNS[woman])) if woman in BODY_RETURNS else ()))


def staged(text, pattern, narrator=False):
    segments = re.findall(r"\{n\}(.*?)\{/n\}", text, re.S)
    if not segments and narrator:
        segments = [text]
    for segment in segments:
        if re.search(r"\b(?:inside your mind|in your thoughts|in your memory|voice whispers)\b", segment, re.I):
            continue
        for match in pattern.finditer(segment):
            # Action must belong to the named woman, not another actor later in
            # the paragraph or a quoted account of yesterday's conversation.
            tail = segment[match.end():match.end()+65].lstrip()
            if (ACTION.match(tail) or re.match(r"(?:is|is standing|is sitting)\b", tail, re.I)
                    or re.match(r"['’]s\s+(?:hand|fingers|wings|tail|mouth|lips|body|shoulder|eyes|gaze|voice|laugh)\b", tail, re.I)):
                return True
    return False


def physical_guard(model, block, woman, route, pattern=None):
    s = block.scene
    if woman == "irabeth" and correspondence_reference(block, woman):
        return presence_guard(model, route, woman, block)
    if local_return_overrides(model.story, s, woman):
        # The original summons continues into the native-host conversation;
        # its paid host adapter is the same contract as the contact version.
        return presence_guard(model, route, woman, block)
    audience = NATIVE_AUDIENCES.get(woman)
    window = set(s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"] + 1))
    if audience and audience[0] in s.get("AnswerLists", []) and window <= audience[1]:
        return presence_guard(model, route, woman)
    # A named native speaker/conversant is already bound by the inline cue.
    # Requiring a spawned visitor clone would hide the real companion's cue.
    # The live route guard still has to be proved independently below.
    pattern = pattern or roster(model)[woman][1]
    if (any(s.get(k) for k in ("NativeReturnCue", "ReturnToList", "ContinueBefore"))
            and pattern.fullmatch(block.node.get("Speaker", ""))
            and (block.node.get("SpeakerUnit") or pattern.fullmatch(s.get("Owner", "")))):
        return presence_guard(model, route, woman)
    # eng7-l14: an explicit authored participant guard supplies current life
    # and route state for narration or a bound inline speaker. It does not
    # require a harem commitment or substitute a visitor clone for the native
    # actor. Actual unit/contact resolution remains the runtime's contract.
    seats = model.story.get("SeatWomen") or {}
    named = [w for w in s.get("ParticipantWomen") or [] if seats[w]["Relationship"] == route]
    if woman in (s.get("ParticipantWomen") or []) or route in (s.get("Participants") or []) and not named:
        return route_guard(model, route, woman)
    alternatives = []
    contacts = {s.get("ContactUnit"), *(s.get("AdditionalContactUnits") or [])}
    for name, p in (model.story.get("Presences") or {}).items():
        if not name.startswith(woman + ".presence"):
            continue
        if not s.get("Remote") and p.get("Unit") in contacts:
            # ContactAvailable requires the primary and additional actors.
            return presence_guard(model, route, woman, block)
        chapters = set(s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"]+1))
        if (s.get("Areas") and set(s["Areas"]) <= {p.get("Area")}
                and chapters <= set(range(p.get("MinChapter", 1), p.get("MaxChapter", 6)+1))):
            alternatives.append(fields(p))
    key = "crossroute.%s.available" % woman
    if key in model.composites:
        return AND(presence_guard(model, route, woman, block), lit(key))
    return OR(*alternatives)


def guarded_on_paths(model, items, proof, block, target):
    """eng7-l14: different valid incoming guards need not share a spelling.

    Check every edge, including its Set effects. Inherit an earlier invariant
    only across edges which cannot change any of its inputs. Cycles without an
    independently proved guard remain unproved; unreachable edges prove safely.
    """
    if proof.implies(block.context, target):
        return True
    if block.slot.startswith("@"):
        return False
    sid = block.scene["Id"]
    contexts = {b.node["Id"]: b.context for b in items if b.scene["Id"] == sid and b.slot == "text"}
    indexed = model.walk_index()[sid][2]
    extra = (fields(block.spec, groups="AnyGroups" if block.slot.startswith("paragraph[") else "RequiresAnyGroups")
             if block.slot.startswith(("paragraph[", "choice[")) else AND())
    touched_inputs = dependencies(model, target) | dependencies(model, extra)
    memo = {}
    def visit(nid, trail=()):
        if nid in memo:
            return memo[nid]
        if proof.implies(AND(contexts.get(nid, AND()), extra), target):
            return True
        if nid in trail or nid == block.scene["Nodes"][0]["Id"]:
            return False
        found = False
        for parent, edges in indexed.items():
            for _, choice, _, _, sets, _, targets in edges:
                if nid not in targets:
                    continue
                found = True
                edge = AND(after_mutations(model, AND(contexts.get(parent, AND()), fields(choice)), sets),
                           *(lit(f) for f in sets))
                if proof.implies(AND(edge, extra), target):
                    continue
                if touched_inputs.intersection(sets) or not visit(parent, (*trail, nid)):
                    memo[nid] = False
                    return False
        memo[nid] = found
        return found
    return visit(block.node["Id"])


def check(model, blocks, proof):
    names = roster(model)
    out = []
    for b in blocks:
        # A declared memory/dream stages a remembered or imagined actor,
        # rather than asserting that actor is alive in the current world.
        if b.scene.get("Kind") in ("memory", "dream"):
            continue
        for woman, (route, pattern) in names.items():
            seat = (model.story.get("SeatWomen") or {}).get(woman) or {}
            if (route == b.route or seat.get("Relationship") == b.route
                    or b.route.startswith(woman + ".")):
                continue
            matches = live_mentions(b.text, pattern, postwar(b.scene))
            match = matches[0] if matches else None
            speaking = b.slot == "text" and pattern.fullmatch(b.node.get("Speaker", ""))
            if not match and not speaking:
                continue
            excerpt = excerpt_at(b.text, match) if match else "Speaker: " + b.node.get("Speaker", "")
            guard = presence_guard(model, route, woman, b)
            guarded = guarded_on_paths(model, blocks, proof, b, guard)
            if not guarded:
                out.append(finding("L1", b, "living %s: departed/dead-unreturned losses with registered earned returns; romance refusal does not remove a living actor" % route,
                                   woman, excerpt, required=guard))
            physical = bool(speaking and b.scene.get("Kind") not in ("memory", "dream", "sending")) or (
                bool(matches) and b.scene.get("Kind") not in ("memory", "dream")
                and staged(b.text, pattern, b.node.get("Speaker") == "Narrator"))
            presence = physical_guard(model, b, woman, route, pattern) if physical else None
            if physical and not guarded_on_paths(model, blocks, proof, b, presence):
                out.append(finding("L1", b, "physical %s: matching guarded presence, ContactUnit or household participant" % woman,
                                   woman + ":physical", excerpt, required=presence))
    return out
