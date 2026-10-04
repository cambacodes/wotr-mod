"""L4: commitments, successful endings and romantic rewards need live eligibility.

Use registered CommittedFlag, outcome setters and concrete romantic prose;
never invent attraction/cost/reconciliation requirements. Refusal/control/path
failures count only when the relationship or existing Derived guards register
them. A missing registration belongs in ESCALATE, not a new mechanic here.
"""
import re
from tools.earned_presence_lint import live_context
from .common import AND, OR, lit, finding, route_guard, postwar, ep

REWARD = re.compile(r"\b(?:you kiss|kisses you|kiss her|her lips (?:meet|press|touch)|your lips (?:meet|press|touch)|takes you to (?:her|the) bed|draws you (?:into|to) (?:her|the) bed|become lovers|became lovers|she is your lover|your wife|marry me|marry you)\b", re.I)
HAPPY = re.compile(r"(?:^|[._])(?:happy|romance_complete|romantic_reward|clean_outcome|ending_together|together_forever)$")
ROMANTIC_FLAGS = re.compile(r"(?:^|[._])(?:kissed|first_night|lover|lovers|romance_kept|romance_finished)$")
NEGATIVE = re.compile(r"(?:^|[._])(?:lost|loss|apart|unfinished|refused|declined|departed|gone|dead|mourning|hostility|closed)(?:[._]|$)")

# Existing route-owned rules that are not part of Relationship.UnavailableFlags.
# jannah_trickster.py: DECLINED is her refusal; chalk_circle.walked_in is the
# authored public repair. nenio_trickster.py: TAMPERED contaminates the control;
# REPLICATED records the already-authored replication. These are readings of
# shipped conditions, not new reconciliation requirements or mechanics.
AUDITED_ELIGIBILITY = {
    "jannah": ("jannah.trickster.declined", "jannah.trickster.chalk_circle.walked_in", "jannah.trickster.chalk_circle"),
    "nenio": ("nenio.trickster.tampered", "nenio.trickster.replicated", "nenio.trickster.commit.replication"),
}


def audited_eligibility(model, block):
    rule = AUDITED_ELIGIBILITY.get(block.route)
    if not rule or rule[0] not in model.authored or rule[1] not in model.authored:
        return None
    blocked, repaired, source = rule
    # The existing repair choice itself earns the repair; do not demand that
    # it was already completed before selecting that same choice.
    if (block.scene["Id"].startswith(source) and block.slot.startswith("choice")
            and repaired in (block.spec.get("Set") or [])):
        return None
    return OR(lit(blocked, False), lit(repaired))


def earned_control_invariant(model, block, target, proof, choices):
    """Use Model's actual producers to prove an immutable authored control repair.

    A committed history may witness a clean/repaired experiment if EVERY
    commitment producer establishes that fact and EVERY contamination producer
    forbids an already-committed history. This honours fresh shipped saves;
    it never infers live death/departure/path state from old commitment.
    """
    committed = (model.rels.get(block.route) or {}).get("CommittedFlag")
    blocked = AUDITED_ELIGIBILITY[block.route][0]
    if not committed or not proof.implies(block.context, lit(committed)):
        return False
    def producers(key):
        return [choices.get((sid, nid, "choice[%d]" % i)) for sid, nid, i in model.producers.get(key, [])
                if isinstance(i, int)]
    commits, contaminants = producers(committed), producers(blocked)
    return bool(commits and contaminants) and all(
        c is not None and proof.implies(AND(c.context, *(lit(k) for k in c.spec.get("Set") or [])), target)
        for c in commits) and all(c is not None and proof.implies(c.context, lit(committed, False)) for c in contaminants)


def reward(block, rel):
    if block.slot.startswith("choice"):
        if rel.get("CommittedFlag") in (block.spec.get("Set") or []):
            return "commitment " + rel["CommittedFlag"]
        flags = [k for k in block.spec.get("Set") or [] if HAPPY.search(k)]
        if flags:
            return "outcome " + ", ".join(flags)
        late = [k for k in block.spec.get("Set") or [] if k.endswith("late_committed")]
        if late:
            return "commitment " + ", ".join(late)
        if any(ROMANTIC_FLAGS.search(k) for k in block.spec.get("Set") or []):
            return "romantic reward"
    if REWARD.search(block.text):
        return "romantic reward"
    if (postwar(block.scene) and not NEGATIVE.search(block.scene["Id"])
            and (re.search(r"[._]epilogue[._]commit(?:[._]|$)", block.scene["Id"])
                 or any(k.endswith("late_committed") for k in block.scene["Requires"]))
            and block.slot not in ("Entry", "ReturnText") and not block.slot.startswith("choice")):
        return "late commitment outcome"
    if (postwar(block.scene) and not NEGATIVE.search(block.scene["Id"])
            and any(k == rel.get("CommittedFlag") or k.endswith("late_committed") for k in block.scene["Requires"])
            and block.slot not in ("Entry", "ReturnText") and not block.slot.startswith("choice")):
        return "committed outcome"
    return None


def check(model, blocks, proof):
    out = []
    choices = {(b.scene["Id"], b.node["Id"], b.slot): b for b in blocks if b.slot.startswith("choice")}
    for b in blocks:
        if b.scene["Owner"] == "AeonEpilogue":
            continue  # the native rewritten history does not share crusade loss flags
        rel = model.rels.get(b.route) or {}
        reason = reward(b, rel)
        if not reason:
            continue
        guard = route_guard(model, b.route)
        if not proof.implies(b.context, guard):
            out.append(finding("L4", b, "live RouteOpen(%s) at %s" % (b.route, reason), b.route, required=guard))
        eligibility = audited_eligibility(model, b)
        if (eligibility is not None and not proof.implies(b.context, eligibility)
                and not earned_control_invariant(model, b, eligibility, proof, choices)):
            out.append(finding("L4", b, "existing refusal/control guard: NOT %s OR %s" % AUDITED_ELIGIBILITY[b.route][:2], "refusal/control", required=eligibility))
        # A new Trickster commitment/reward requires current power. Historical
        # postwar consequences of a paid return remain valid per T6 doctrine.
        new_act = reason.startswith(("commitment ", "outcome ", "late commitment"))
        path_branch = ".trickster." in b.scene["Id"] or bool(set(ep.TRICKSTER_ROOTS).intersection(
            [*b.scene["Requires"], *(b.spec.get("Requires") or [] if b.slot.startswith("choice") else [])]))
        if (new_act and path_branch
                and not live_context(model.story, b.scene, b.spec if b.slot.startswith("choice") else None)
                and not proof.implies(b.context, ("lit", "trickster.now", True))):
            out.append(finding("L4", b, "trickster.now (or live trickster with trickster.failed forbidden) at " + reason, "current-path",
                               required=OR(lit("trickster.now"), AND(lit("trickster"), lit("trickster.failed", False)))))
    return out
