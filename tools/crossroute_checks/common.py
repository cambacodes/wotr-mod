"""Static condition proofs over rrt_verify.Model, not a second runtime story model.

Derived expressions use the model's composites/open_routes/derived_forbids.
Authored flags and historical latches are deliberately opaque: having earned a
flag yesterday does not prove eligibility, location or current power today.
Proofs use a small stdlib propositional solver. Unknown flags are independent;
an unproved guard is reported, never silently treated as an earned outcome.
"""
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from tools import rrt_verify as verify
from tools.earned_presence_lint import ep


def lit(key, positive=True):
    return ("lit", key, positive)


def combine(op, parts):
    flat = set()
    for part in parts:
        if part[0] == op:
            flat.update(part[1:])
        else:
            flat.add(part)
    if len(flat) == 1:
        return next(iter(flat))
    return (op, *sorted(flat, key=repr))


def AND(*parts):
    return combine("and", parts)


def OR(*parts):
    return combine("or", parts)


def NOT(part):
    if part[0] == "lit":
        return lit(part[1], not part[2])
    return combine("or" if part[0] == "and" else "and", map(NOT, part[1:]))


def fields(spec, groups="RequiresAnyGroups", overrides=False):
    parts = [lit(k) for k in spec.get("Requires") or []]
    for key in spec.get("Forbids") or []:
        back = (spec.get("ForbidOverrides") or {}).get(key) if overrides else None
        parts.append(OR(lit(key, False), lit(back)) if back else lit(key, False))
    if spec.get("RequiresAny"):
        parts.append(OR(*(lit(k) for k in spec["RequiresAny"])))
    parts.extend(OR(*(lit(k) for k in g)) for g in spec.get(groups) or [])
    return AND(*parts)


def when(groups):
    return OR(*(AND(*(lit(k.lstrip("!"), not k.startswith("!")) for k in g)) for g in groups))


def route_guard(model, route, woman=None):
    rel = model.rels.get(route) or {}
    # Group seats retain only this woman's losses, plus route-level path blockers.
    seat = (model.story.get("SeatWomen") or {}).get(woman)
    losses = list(rel.get("UnavailableFlags") or [])
    returns = rel.get("UnavailableOverrides") or {}
    if seat:
        other = {f for name, s in (model.story.get("SeatWomen") or {}).items()
                 if s["Relationship"] == route and name != woman for f in s.get("UnavailableFlags") or []}
        losses = [f for f in losses if f not in other]
        returns = {**returns, **(seat.get("UnavailableOverrides") or {})}
    parts = [lit(rel["ClosedFlag"], False)] if rel.get("ClosedFlag") else []
    parts += [OR(lit(f, False), lit(returns[f])) if returns.get(f) else lit(f, False) for f in losses]
    return AND(*parts)


class Proof:
    """Prove context => target by checking that context AND NOT target is unsatisfiable.

    Tseitin clauses keep Derived OR-of-ANDs compact. Counts remain opaque (no
    count key in itself proves a specific member). Cycles remain opaque too.
    Latches imply their sources only for persistent native facts. In all
    latches, a source held NOW still implies the latch; the reverse would turn
    history into live presence and is forbidden.
    """
    def __init__(self, model):
        self.model = model
        self.cache = {}
        self.cyclic = set()
        visited, stack = set(), []
        def visit(key):
            if key in stack:
                self.cyclic.update(stack[stack.index(key):])
                return
            if key in visited:
                return
            stack.append(key)
            for source in verify.composite_inputs(model, key):
                if source in model.composites:
                    visit(source)
            stack.pop()
            visited.add(key)
        for key in model.composites:
            visit(key)

    def implies(self, context, target):
        cache_key = context, target
        if cache_key in self.cache:
            return self.cache[cache_key]
        variables, clauses, active = {}, [], set()

        def encode(expr):
            if expr[0] == "lit" and not expr[2]:
                return -encode(lit(expr[1]))
            if expr in variables:
                return variables[expr]
            v = variables[expr] = len(variables) + 1
            if expr[0] == "lit":
                k = expr[1]
                m = self.model
                definition = None
                if k not in active and k not in self.cyclic and k in m.composites:
                    definition = AND(
                        OR(*(AND(*(lit(x) for x in g)) for g in m.composites[k])),
                        *(lit(f, False) for f in m.derived_forbids.get(k, [])),
                        *(route_guard(m, r) for r in m.open_routes.get(k, [])))
                elif k in m.latches and all(m.is_persistent_native(x) for x in m.latches[k]):
                    definition = OR(*(lit(x) for x in m.latches[k]))
                elif k == "ascended":
                    definition = OR(*(lit(x) for x in ("ascend_all", "ascend_alone", "ascend_areelu", "ascend_companions")))
                elif k == "inhuman":
                    definition = OR(lit("swarm"), lit("true_lich"))
                elif k == "loss":
                    definition = OR(*(lit(x) for x in ("irabeth_dead", "anevia_dead", "irabeth_gone", "anevia_gone", "sacrifice")))
                if definition is not None:
                    active.add(k)
                    w = encode(definition)
                    active.discard(k)
                    clauses.extend([(-v, w), (v, -w)])
                elif k in m.latches:
                    # Rules.Complete records current native sources, while old
                    # confirmations survive after the source disappears.
                    clauses.extend((-encode(lit(source)), v) for source in m.latches[k])
                if "konomi" in m.revivals:
                    # Central live observation, not a historical return flag:
                    # Main.State calls KonomiRecovery.RetainedDead then
                    # ReadLifecycle. ObserveLife records this same retained
                    # actor's current death; ReadLifecycle emits exactly one of
                    # death_unreturned/death_restored. ReturnContact/Correspondence
                    # require that exact actor alive NOW (KonomiRecovery.cs).
                    if k == "konomi.retained_dead":
                        clauses.append((-v, encode(lit("konomi.death_unreturned"))))
                    elif k == "konomi.death_unreturned":
                        clauses.append((-v, -encode(lit("konomi.death_restored"))))
                    elif k in ("konomi.return_contact_available", "konomi.return_correspondence_available"):
                        clauses.append((-v, -encode(lit("konomi.retained_dead"))))
            else:
                children = [encode(x) for x in expr[1:]]
                if expr[0] == "and":
                    clauses.extend((-v, x) for x in children)
                    clauses.append(tuple([v] + [-x for x in children]))
                else:
                    clauses.extend((v, -x) for x in children)
                    clauses.append(tuple([-v] + children))
            return v

        clauses.extend([(encode(context),), (-encode(target),)])

        def satisfiable(cs):
            while True:
                if any(not c for c in cs):
                    return False
                units = {c[0] for c in cs if len(c) == 1}
                if any(-x in units for x in units):
                    return False
                if not units:
                    break
                cs = [tuple(x for x in c if -x not in units) for c in cs if not any(x in units for x in c)]
            if not cs:
                return True
            counts = {}
            for c in cs:
                for x in c:
                    counts[x] = counts.get(x, 0) + 1
            pure = {x for x in counts if -x not in counts}
            if pure:
                return satisfiable([c for c in cs if not any(x in pure for x in c)])
            x = min(cs, key=len)[0]
            return satisfiable(cs + [(x,)]) or satisfiable(cs + [(-x,)])

        result = not satisfiable(clauses)
        self.cache[cache_key] = result
        return result


@dataclass(frozen=True)
class Block:
    scene: dict
    node: dict
    spec: dict
    slot: str
    text: str
    context: tuple
    ancestors: frozenset = frozenset()

    @property
    def route(self):
        return self.scene["Relationship"]


def node_conditions(model, scene):
    """Must-hold choice conditions on ALL incoming paths, using Model.walk_index.

    Nodes have no runtime Requires/Forbids fields. Do not mistake a decorative
    node condition for a gate. Set invalidates earlier negative assumptions;
    guard expressions reading changed flags are dropped conservatively.
    """
    nodes = model.walk_index()[scene["Id"]][2]
    if not scene["Nodes"]:
        return {}, {}, {}
    first = scene["Nodes"][0]["Id"]
    held, changed, ancestors, pending = {first: frozenset()}, {first: frozenset()}, {first: frozenset()}, [first]

    while pending:
        nid = pending.pop()
        for _, c, _, _, sets, _, targets in nodes[nid]:
            additions = fields(c)
            parts = set(additions[1:]) if additions[0] == "and" else {additions}
            carried = set(held[nid]) | parts
            if sets:
                # Only conditions reading a changed flag can become stale.
                # An unrelated Set must not discard a still-live Derived guard.
                carried = {e for e in carried if not dependencies(model, e).intersection(sets)}
                carried.update(lit(k) for k in sets)
            out = frozenset(carried)
            mutations = changed[nid] | frozenset(sets)
            for nxt in targets:
                if nxt not in nodes:
                    continue
                merged = held[nxt] & out if nxt in held else out
                touched = changed.get(nxt, frozenset()) | mutations
                passed = ancestors[nid] | {nid}
                prior = ancestors[nxt] & passed if nxt in ancestors else passed
                if nxt not in held or merged != held[nxt] or touched != changed.get(nxt) or prior != ancestors.get(nxt):
                    held[nxt] = merged
                    changed[nxt] = touched
                    ancestors[nxt] = prior
                    pending.append(nxt)
    return held, changed, ancestors


def dependencies(model, expr, seen=()):
    if expr[0] != "lit":
        return set().union(*(dependencies(model, x, seen) for x in expr[1:]))
    key = expr[1]
    result = {key}
    if key in seen:
        return result
    for source in verify.composite_inputs(model, key):
        result.update(dependencies(model, lit(source), (*seen, key)))
    return result


def after_mutations(model, context, changed):
    if not changed:
        return context
    parts = context[1:] if context[0] == "and" else (context,)
    return AND(*(p for p in parts if not dependencies(model, p).intersection(changed)))


def scene_context(model, s):
    ctx = fields(s, overrides=True)
    # Main.State always adds Rules.ChapterFlag for the current chapter. Scene
    # window checks can therefore establish these existing central inputs.
    window = set(s.get("Chapters") or range(s["MinChapter"], s["MaxChapter"]+1))
    if window == {1}:
        ctx = AND(ctx, lit("chapter_one"), lit("chapter_later", False))
    elif window and all(ch > 1 for ch in window):
        ctx = AND(ctx, lit("chapter_later"), lit("chapter_one", False))
    elif window == {0}:
        ctx = AND(ctx, lit("chapter_one", False), lit("chapter_later", False))
    elif window and 0 not in window:
        ctx = AND(ctx, OR(lit("chapter_one"), lit("chapter_later")))
    # Match the automatic relationship guard only where Available applies it.
    if not verify.is_epilogue(s) and not s.get("TricksterDevice") and not any(s.get(k) for k in ("Recovery", "AfterRecovery", "AfterDeparture")):
        ctx = AND(ctx, route_guard(model, s["Relationship"]))
    women = model.story.get("SeatWomen") or {}
    participants = []
    for r in s.get("Participants") or []:
        named = [w for w in s.get("ParticipantWomen") or [] if women[w]["Relationship"] == r]
        participants.extend(route_guard(model, r, w) for w in named) if named else participants.append(route_guard(model, r))
    ctx = AND(ctx, *participants,
              *(route_guard(model, women[w]["Relationship"], w) for w in s.get("ParticipantWomen") or []))
    return ctx


def blocks(model):
    for s in model.scenes:
        base = scene_context(model, s)
        incoming, changed, ancestors = node_conditions(model, s)
        # Entry and ReturnText are authored cues too; Title is presentation metadata.
        for key in ("Entry", "ReturnText"):
            if s.get(key):
                yield Block(s, {"Id": "@" + key}, s, key, s[key], base)
        for n in s["Nodes"]:
            if n["Id"] not in incoming:
                continue
            ctx = AND(after_mutations(model, base, changed[n["Id"]]), *incoming[n["Id"]])
            if n["Text"] or n.get("Speaker") not in (None, "Narrator", "Commander"):
                yield Block(s, n, n, "text", n["Text"], ctx, ancestors[n["Id"]])
            for i, p in enumerate(n["Paragraphs"]):
                yield Block(s, n, p, "paragraph[%d]" % i, p.get("Text", ""), AND(ctx, fields(p, "AnyGroups")), ancestors[n["Id"]])
            for i, c in enumerate(n["Choices"]):
                yield Block(s, n, c, "choice[%d]" % i, c["Text"], AND(ctx, fields(c)), ancestors[n["Id"]])


def finding(check, block, missing, subject="", excerpt=None, required=None):
    text = re.sub(r"\s+", " ", block.text).strip() if excerpt is None else excerpt
    result = dict(check=check, route=block.route, scene=block.scene["Id"], node=block.node.get("Id", ""),
                  slot=block.slot, subject=subject, excerpt=text[:240], missing_condition=missing)
    if required is not None:
        result["required_condition"] = required
    # Wording is audited separately. Guard/subject changes still invalidate proof.
    identity = {**{k: v for k, v in result.items() if k != "excerpt"}, "context": block.context,
                "location": {k: block.scene.get(k) for k in ("Owner", "Kind", "MinChapter", "MaxChapter", "ContactUnit")},
                "areas": sorted(block.scene.get("Areas") or []), "chapters": sorted(block.scene.get("Chapters") or []),
                "participants": sorted(block.scene.get("Participants") or []),
                "women": sorted(block.scene.get("ParticipantWomen") or []),
                "contacts": sorted(block.scene.get("AdditionalContactUnits") or [])}
    result["fingerprint"] = hashlib.sha256(json.dumps(identity, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return result


def postwar(s):
    return ep.is_epilogue(s) or s["Id"].startswith("lastcall.") or bool(re.search(r"(?:postwar|after_war)", s["Id"]))


def sentences(text):
    return re.split(r"(?<=[.!?])\s+|\n+", text)


def excerpt_at(text, match):
    return re.sub(r"\s+", " ", text[max(0, match.start()-60):match.end()+150]).strip()


def roster(model):
    """Names come from ROSTER.md and registered scene owners/SeatWomen.

    These aliases are spelling/short-name/title variants, never a parallel roster.
    Ambiguous bare 'queen', 'lady', 'dragon' are not names.
    """
    aliases = {
        "arueshalae": ("Arue", "Arushalae"), "camellia": ("Camelia",),
        "galfrey": ("Queen Galfrey", "Queen of Mendev", "Her Majesty"),
        "konomi": ("Lady Konomi",), "iomedae": ("Inheritor",),
        "nocticula": ("Redeemer Queen", "Lady in Shadow"), "minagho": ("Mina",),
        "jannah": ("Jannah Aldori",), "elyanka": ("Elyanka Camilary",),
        "dorgelinda": ("Dorgelinda Stranglehold",), "eliandra": ("Elyandra",),
        "hepzamirah": ("Hepza",), "terendelev": ("the silver dragon",),
        "irabeth": ("Beth",), "anevia": ("Nevi",),
    }
    women = {k: v["Relationship"] for k, v in (model.story.get("SeatWomen") or {}).items()}
    names = {}
    path = Path(verify.MOD) / "ROSTER.md"
    if path.exists():
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("|"):
                continue
            name = line.split("|")[1].strip().strip("*")
            short = name.split()[0].lower() if name else ""
            if short in model.rels or short in women:
                names.setdefault(short, set()).update((name, name.split()[0]))
    for s in model.scenes:
        owner = s["Owner"].removesuffix("Epilogue")
        short = owner.lower()
        if short in model.rels or short in women:
            names.setdefault(short, set()).add(owner)
    for woman in women:
        names.setdefault(woman, set()).add(woman.capitalize())
    return {woman: (woman if woman in model.rels else women.get(woman, woman), re.compile(r"(?<!\w)(?:" + "|".join(
                re.escape(x) for x in sorted(names[woman] | set(aliases.get(woman, ())), key=lambda x: (-len(x), x))) + r")(?!\w)", re.I))
            for woman in sorted(names)}
