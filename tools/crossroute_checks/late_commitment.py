"""L4: commitments, successful endings and romantic rewards need live eligibility.

Use registered CommittedFlag, outcome setters and concrete romantic prose;
never invent attraction/cost/reconciliation requirements. Refusal/control/path
failures count only when the relationship or existing Derived guards register
them. A missing registration belongs in ESCALATE, not a new mechanic here.
"""
import re
import json
from pathlib import Path
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
CONTRACTS = json.loads((Path(__file__).resolve().parents[1] / "earned_outcome_inventory_contracts.json").read_text(encoding="utf-8"))
AUDITED_ELIGIBILITY = {k: tuple(v) for k, v in CONTRACTS["refusal_control"].items()}


def audited_eligibility(model, block):
    if block.route == "minagho_chivarro" and outcome_woman(block) != "minagho":
        return OR(lit("minagho_chivarro.trickster.chivarro_walked", False), lit("minagho_chivarro.trickster.cost.won_back"))
    if block.route == "mielarah":
        return OR(lit("mielarah.trickster.cost.meant", False), lit("mielarah.deck.oskel_settled"))
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
    if block.node["Id"] in CONTRACTS["mandatory_consumers"].get(block.scene["Id"], []):
        return "romantic response"
    if block.scene["Owner"] == "AeonEpilogue":
        return None
    if block.slot.startswith("choice"):
        # eng7-l13: exact auxiliary framework milestones are not romance.
        if (rel.get("CommittedFlag") in (block.spec.get("Set") or [])
                and rel["CommittedFlag"] not in CONTRACTS["non_romance_commitment_flags"]):
            return "commitment " + rel["CommittedFlag"]
        flags = [k for k in block.spec.get("Set") or [] if HAPPY.search(k)]
        if flags:
            return "outcome " + ", ".join(flags)
        late = [k for k in block.spec.get("Set") or [] if k.endswith("late_committed")]
        if late:
            return "commitment " + ", ".join(late)
        if any(ROMANTIC_FLAGS.search(k) for k in block.spec.get("Set") or []):
            return "romantic reward"
    # eng7-l13: explicit historical/negative prose is not a romantic outcome.
    # Exemptions never excuse a producer added to one of these pages.
    for target in CONTRACTS["exemptions"]:
        sid, _, nid = target.partition("/")
        if (block.scene["Id"] == sid or block.scene["Id"].startswith(sid + ".acquired.")) and (not nid or block.node["Id"] == nid):
            return None
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


def path_branch(block):
    return ".trickster." in block.scene["Id"] or bool(set(ep.TRICKSTER_ROOTS).intersection(
        [*block.scene["Requires"], *(block.spec.get("Requires") or [] if block.slot.startswith("choice") else [])]))


def outcome_woman(block):
    """Explicit solo contracts; the other woman's loss is not a romance price."""
    if block.route != "minagho_chivarro":
        return None
    sid = block.scene["Id"]
    for woman in ("minagho", "chivarro"):
        if (".alone." + woman in sid or sid.endswith(".epilogue." + woman)
                or sid == "minachiv.ending_" + woman):
            return woman
    if sid.endswith(".epilogue.commit") and block.node["Id"] in ("start", "waiting", "went_alone", "regrets_alone"):
        return "chivarro"
    if sid.endswith(".epilogue.commit") and ".explicit." in block.node["Id"]:
        # Round-two inserts wrap saved exits without changing the participant
        # contract. Follow their effect-free continuations to the original
        # solo page instead of treating every new insert as a pair reward.
        nodes = {node["Id"]: node for node in block.scene["Nodes"]}
        pending = [block.node["Id"]]
        seen = set()
        exits = set()
        while pending:
            identity = pending.pop()
            if identity in seen:
                continue
            seen.add(identity)
            if ".explicit." not in identity:
                exits.add(identity)
                continue
            for answer in nodes.get(identity, {}).get("Choices", []):
                if answer.get("Next"):
                    pending.append(answer["Next"])
        if exits and exits <= {"went_alone", "regrets_alone"}:
            return "chivarro"
    return None


def late_refusals(story, key, route):
    """Read raw-term pages and their already-authored refusal overrides."""
    result = {}
    for scene in story["Scenes"]:
        if not (key in scene.get("Requires", []) or
                (scene.get("Relationship") == route and
                 re.search(r"(?:epilogue\.commit|late\.commit|epilogue\.late)$", scene["Id"]))):
            continue
        for flag in scene.get("Forbids", []):
            if re.search(r"(?:declined|refused|refused_her)$", flag):
                repairs = result.setdefault(flag, set())
                repaired = scene.get("ForbidOverrides", {}).get(flag)
                if repaired:
                    repairs.add(repaired)
    return {flag: tuple(sorted(repairs)) for flag, repairs in result.items()}


def acceptance_inventory_check(model, blocks, proof):
    out = []
    choices = {(b.scene["Id"], b.node["Id"], b.slot): b for b in blocks if b.slot.startswith("choice")}
    # eng8-q8h begin: readiness must not prove acceptance; consumers must be feasible.
    inventory = json.loads((Path(__file__).resolve().parents[1] / "late_acceptance_inventory2_contracts.json").read_text(encoding="utf-8"))
    for key, groups in inventory["acceptance"].items():
        route = key.split(".")[0]
        if route not in model.rels:
            continue
        witness = next(b for b in blocks if b.route == route and b.slot == "text")
        target = AND(*(OR(*(lit(flag) for flag in group)) for group in groups))
        if not proof.implies(lit(key), target):
            out.append(finding("L4", witness, "earned acceptance at " + key, "late-acceptance", required=target))
    for sid, groups in inventory["commit_consumers"].items():
        if sid not in model.by_id:
            continue
        witness = next(b for b in blocks if b.scene["Id"] == sid and b.slot == "text")
        target = AND(*(OR(*(lit(flag) for flag in group)) for group in groups))
        if not proof.implies(witness.context, target):
            out.append(finding("L4", witness, "documented proof and personal beat", "permanent-acceptance", required=target))
    for row in inventory["affirmative_consumers"]:
        if row["scene"] not in model.by_id:
            continue
        for i in row["indices"]:
            b = choices.get((row["scene"], row["node"], "choice[%d]" % i))
            if b is None:
                b = next(b for b in blocks if b.scene["Id"] == row["scene"] and b.slot == "text")
                bad = True
            else:
                # A contradictory consumer has no reachable yes. The answer itself
                # supplies the receipt, avoiding jointly-produced ordinary commit.
                bad = (proof.implies(b.context, OR()) or row["flag"] in b.spec.get("Requires", [])
                       or row["flag"] not in b.spec.get("Set", [])
                       or row["forbidden_joint_flag"] in b.spec.get("Set", []))
            if bad:
                out.append(finding("L4", b, "reachable affirmative acceptance producer", "producer-consumer"))
    # end eng8-q8h
    return out


def check(model, blocks, proof):
    # eng8-q8h: same inventory is mandatory in strict L4 and mutation tests.
    out = acceptance_inventory_check(model, blocks, proof)
    choices = {(b.scene["Id"], b.node["Id"], b.slot): b for b in blocks if b.slot.startswith("choice")}
    # eng7-l13: opportunity keys are producers too. A guarded page must not
    # conceal a stale late entitlement still reaching household/coda readers.
    for key in model.story.get("Derived", {}):
        if not key.endswith("late_committed"):
            continue
        route = key.split(".trickster.")[0]
        witnesses = [b for b in blocks if b.route == route and b.slot == "text"]
        if not witnesses:
            continue
        witness = next((b for b in witnesses if key in b.scene["Requires"]), witnesses[0])
        required = [route_guard(model, route)]
        control = audited_eligibility(model, witness)
        if control is not None:
            required.append(control)
        if route == "kaylessa":
            required.append(OR(lit("kaylessa.trickster.declined", False),
                               lit("kaylessa.trickster.knife_picked_up"), lit("kaylessa.committed")))
        elif route != "jannah":
            refusals = late_refusals(model.story, key, route)
            required.extend(OR(lit(f, False), *(lit(back) for back in refusals[f])) for f in sorted(refusals))
        target = AND(*required)
        if not proof.implies(lit(key), target):
            out.append(finding("L4", witness, "live eligibility at Derived producer " + key,
                               "late-entitlement", required=target))
    for b in blocks:
        if b.scene["Owner"] == "AeonEpilogue":
            continue  # the native rewritten history does not share crusade loss flags
        rel = model.rels.get(b.route) or {}
        reason = reward(b, rel)
        if not reason:
            continue
        guard = route_guard(model, b.route, outcome_woman(b))
        if not proof.implies(b.context, guard):
            out.append(finding("L4", b, "live RouteOpen(%s) at %s" % (b.route, reason), b.route, required=guard))
        eligibility = audited_eligibility(model, b)
        if (eligibility is not None and not proof.implies(b.context, eligibility)
                and (b.route not in AUDITED_ELIGIBILITY or not earned_control_invariant(model, b, eligibility, proof, choices))):
            contract = AUDITED_ELIGIBILITY[b.route][:2] if b.route in AUDITED_ELIGIBILITY else (
                ("minagho_chivarro.trickster.chivarro_walked", "minagho_chivarro.trickster.cost.won_back") if b.route == "minagho_chivarro" else
                ("mielarah.trickster.cost.meant", "mielarah.deck.oskel_settled"))
            out.append(finding("L4", b, "existing refusal/control guard: NOT %s OR %s" % contract, "refusal/control", required=eligibility))
        # A new Trickster commitment/reward requires current power. Historical
        # postwar consequences of a paid return remain valid per T6 doctrine.
        new_act = reason.startswith(("commitment ", "outcome ", "late commitment"))
        if (new_act and path_branch(b)
                and not live_context(model.story, b.scene, b.spec if b.slot.startswith("choice") else None)
                and not proof.implies(b.context, ("lit", "trickster.now", True))):
            out.append(finding("L4", b, "trickster.now (or live trickster with trickster.failed forbidden) at " + reason, "current-path",
                               required=OR(lit("trickster.now"), AND(lit("trickster"), lit("trickster.failed", False)))))
    return out
