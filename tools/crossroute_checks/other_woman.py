"""L1: cross-route names and speaking cues read central earned presence."""
import re
from .common import OR, fields, finding, roster, route_guard, excerpt_at

ACTION = re.compile(r"\b(?:stands?|stood|sits?|sat|leans?|waits?|steps?|walks?|enters?|arrives?|joins?|nods?|smiles?|laughs?|says?|said|asks?|answers?|touches?|takes?|holds?|watches?|turns?|comes?|moves?|puts?|drinks?|sings?|offers?|grins?|lifts?|reaches?|pushes?|pulls?|folds?|sets?|kisses?|embraces?|stayed|joined|arrived|beside|across from|at the table)\b", re.I)


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


def physical_guard(model, block, woman, route):
    s = block.scene
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
            return route_guard(model, route, woman)
        chapters = set(s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"]+1))
        if (s.get("Areas") and set(s["Areas"]) <= {p.get("Area")}
                and chapters <= set(range(p.get("MinChapter", 1), p.get("MaxChapter", 6)+1))):
            alternatives.append(fields(p))
    return OR(*alternatives)


def check(model, blocks, proof):
    names = roster(model)
    # eng7-f6b: text-only native dialogue keeps canon speakers and native eligibility.
    # A romance refusal never removes Seelah/Jannah/Arsinoe from their native quest.
    from tools import kiana_native_policy
    native_scenes = {}
    approved = kiana_native_policy.contracts()
    for row in model.story.get('NativeOverrides', []):
        target = row.get('Target')
        if target not in approved or row.get('Field') != 'NativeEpilogueEdits' or row.get('Action') != 'REPLACE':
            continue
        spec = model.story.get('NativeEpilogueEdits', {}).get(row.get('RuntimeKey'))
        context = kiana_native_policy.native_context()[target]
        try:
            kiana_native_policy.check(target, spec or {}, context['Found'])
        except ValueError:
            continue
        for variant in [spec, *spec.get('Variants', [])]:
            native_scenes[variant['Replacement']] = context
    # eng7-f6b end
    out = []
    for b in blocks:
        for woman, (route, pattern) in names.items():
            seat = (model.story.get("SeatWomen") or {}).get(woman) or {}
            if (route == b.route or seat.get("Relationship") == b.route
                    or b.route.startswith(woman + ".")):
                continue
            match = pattern.search(b.text)
            speaking = b.slot == "text" and pattern.fullmatch(b.node.get("Speaker", ""))
            if not match and not speaking:
                continue
            excerpt = excerpt_at(b.text, match) if match else "Speaker: " + b.node.get("Speaker", "")
            guard = route_guard(model, route, woman)
            # eng7-f6b: inherited native speech/mentions, never a new appearance.
            native = native_scenes.get(b.scene['Id'], {})
            inherited_speaker = any(pattern.fullmatch(name) for name in native.get('Speakers', []))
            inherited_mention = bool(pattern.search(native.get('Mentions', '')))
            guarded = inherited_speaker or inherited_mention or proof.implies(b.context, guard)
            if not guarded:
                out.append(finding("L1", b, "RouteOpen(%s): closed/departed/dead-unreturned losses with registered earned returns" % route,
                                   woman, excerpt, required=guard))
            physical = bool(speaking and b.scene.get("Kind") not in ("memory", "dream", "sending")) or (
                b.scene.get("Kind") not in ("memory", "dream") and staged(b.text, pattern, b.node.get("Speaker") == "Narrator"))
            presence = physical_guard(model, b, woman, route) if physical else None
            if physical and not inherited_speaker and not proof.implies(b.context, presence):
                out.append(finding("L1", b, "physical %s: matching guarded presence, ContactUnit or household participant" % woman,
                                   woman + ":physical", excerpt, required=presence))
    return out
