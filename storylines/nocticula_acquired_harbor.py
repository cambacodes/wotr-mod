"""History-aware copies of the harbor visits after the earned Trickster bridge.

Unregistered author draft. Native parent, Gift and seen-cue bindings are read-only.
The hosted dreams are the bridge's authored mechanism, not a replacement Gift.
All romantic participants are unrelated adults; intimacy is graphic and explicit.
Root must exclude original harbor scenes when bridge readiness selects this family.
Original completion aliases preserve the existing progress and ending contracts.
"""
from copy import deepcopy

from story_format import c, n
from storylines import nocticula_continuation as original


HISTORIES = {
    "new": "noct.join.history_new",
    "refused": "noct.join.history_refused",
    "prior": "noct.join.history_prior",
}
BRIDGE = (
    "noct.join.harbor_variant_ready", "noct.join.recurring_dreams_accepted",
    "noct.join.exit_demonstrated", "noct.join.a_chosen_shore_done",
)
RELATIONSHIP = deepcopy(original.RELATIONSHIP)
RELATIONSHIP.update(
    Description=original.RELATIONSHIP["Description"],
    Guidance="After completing the Trickster correspondence and accepting the hosted meetings, rest in Drezen to hear Nocticula's harbor proposal. While the Gift holds, her dreams carry you into her court; what you decide there happens. Her invitation does not accept an earlier refused offer, restore a lost Gift or settle the Worldwound. Each undertaking and private invitation can still be declined.",
)


# Coordinator N1 ruling: freeze both authoring and integrated clone surfaces.
# The baseline is persistent save-compatible source data, not a generated export.
import json
from pathlib import Path

BASELINE = json.loads(Path(__file__).with_name("nocticula_acquired_baseline.json").read_text(encoding="utf-8"))
SCENES = deepcopy(BASELINE["Scenes"])


def frozen_integrated():
    from storylines.nocticula_n1 import RETIRED, retire
    scenes = deepcopy(BASELINE["IntegratedScenes"])
    for s in scenes:
        if not s["Owner"].endswith("Epilogue") and "chapter_later" not in s["Forbids"]:
            s["Forbids"].append("chapter_later")
        if s["Id"].split(".acquired.")[0].removeprefix("noct.") in RETIRED:
            retire(s)
    return scenes


def validate():
    """Count selected played paths after an explicitly supplied bridge fixture."""
    import runpy
    from functools import cache
    from itertools import product
    from pathlib import Path
    from storylines.nocticula_trickster_acquisition import allowed
    from storylines.nocticula_trickster_concession import outcomes
    words = cache(runpy.run_path(str(Path(__file__).resolve().parents[1] / "tools/measure-story-content.py"))["words"])
    assert len({s["Id"] for s in SCENES}) == len(SCENES)
    donor_snapshot = deepcopy(original.SCENES)
    native = set(original.ETUDES) | set(original.SEEN_CUES)
    native |= {"noct.acq.gift_renewed", "noct.acq.original_gift_completed"}
    for s in SCENES:
        assert len({p["Id"] for p in s["Nodes"]}) == len(s["Nodes"])
        for p in s["Nodes"]:
            for choice in p["Choices"]:
                assert not native.intersection(choice["Set"])
                assert not (choice.get("Check") and choice.get("Next"))
    results = {}
    closure_count = 0
    ending_checks = 0
    for history in HISTORIES:
        base = {*BRIDGE, HISTORIES[history], "trickster", "noct.acq.renewed_agreement"}
        gift_states = (set(), {"noct.gift"}, {"noct.acq.gift_renewed"},
                       {"noct.gift", "noct.acq.gift_renewed"})
        faces = [s for s in SCENES if s["Id"].startswith("noct.her_own_face.acquired." + history)]
        for gift_state in gift_states:
            eligible = [s for s in faces if allowed(s, base | gift_state | {"noct.dessa_safe"})]
            assert len(eligible) == 1
            assert not any(allowed(s, base | gift_state | {"noct.dessa_safe", "noct.her_own_face"}) for s in faces)
            for chosen in ("company", "alliance", "limit"):
                for dead, changed, ascent, sacrifice in product((False, True), repeat=4):
                    state = base | gift_state | {"noct.complete", "noct.chosen_" + chosen}
                    for active, flag in ((dead, "noct.dead"), (changed, "inhuman"),
                                         (ascent, "ascended"), (sacrifice, "sacrifice")):
                        if active:
                            state.add(flag)
                    eligible = [s for s in SCENES if s["Owner"] == "Epilogue"
                                and s["Id"].endswith(".acquired." + history) and allowed(s, state)]
                    expected = "death" if dead else "changed" if changed else "ascent" if ascent else "sacrifice" if sacrifice else chosen
                    assert len(eligible) == 1 and eligible[0]["Id"].startswith("noct.ending_" + expected + ".")
                    ending_checks += 1
        aeon = next(s for s in SCENES if s["Id"] == "noct.ending_aeon.acquired." + history)
        assert allowed(aeon, base | {"noct.complete"})
        assert not allowed(aeon, base)
    for history in HISTORIES:
        for gift in ("absent", "original", "renewed"):
            # The acquired prior-pact opening concerns lost original patronage.
            if history == "prior" and gift == "original":
                continue
            for question, witnesses in product(("passengers", "profit"), ((),
                    ("noct.parent_ambition_heard",), ("noct.socoth_plan_exposed",),
                    ("noct.parent_ambition_heard", "noct.socoth_plan_exposed"))):
                base = {*BRIDGE, HISTORIES[history], "trickster", "noct.acq.renewed_agreement",
                        "noct.join.first_question_" + question, *witnesses}
                if history == "refused":
                    base.add("noct.parent_rejected")
                elif history == "prior":
                    base.update(("noct.parent_active", "noct.acq.original_gift_completed"))
                if gift != "absent":
                    base.add("noct.gift" if gift == "original" else "noct.acq.gift_renewed")
                family = [s for s in SCENES if ".acquired." + history in s["Id"] and (
                    not s["Id"].startswith("noct.her_own_face") or s["Id"].endswith("." + gift))]
                visits = [s for s in family if s["Owner"] == "Memory"]
                endings = [s for s in family if s["Owner"] == "Epilogue" and s["Id"].split(".")[1] in (
                    "ending_company", "ending_alliance", "ending_limit")]
                states = {frozenset(base): (0, 0)}
                assert len([s for s in SCENES if s["Id"].startswith("noct.unlit_quay.") and allowed(s, base)]) == 1
                for missing in BRIDGE:
                    assert not any(allowed(s, base - {missing}) for s in visits)
                for other in HISTORIES.values():
                    if other != HISTORIES[history]:
                        assert not any(allowed(s, base | {other}) for s in visits)
                for s in visits:
                    original_id = s["Id"].split(".acquired.")[0]
                    assert not allowed(s, base | {original_id})
                    for page in s["Nodes"]:
                        for choice in page["Choices"]:
                            if choice["Abort"]:
                                assert original_id not in choice["Set"]
                # Preserve only flags tested later, retaining min/max prefixes.
                for index, s in enumerate(visits):
                    later = visits[index + 1:] + endings
                    used = set()
                    for future in later:
                        for item in (future, *(c for p in future["Nodes"] for c in p["Choices"])):
                            used.update(item["Requires"] + item["Forbids"])
                    updated = {}
                    for state, (low, high) in states.items():
                        assert allowed(s, state), (s["Id"], state)
                        for final, count in outcomes(s, state, words):
                            if "noct.closed" in final:
                                closure_count += 1
                                assert not any(allowed(future, final) for future in visits[index + 1:])
                                continue
                            assert s["Id"].split(".acquired.")[0] in final
                            key = frozenset(final & used)
                            bounds = (low + count, high + count)
                            old = updated.get(key, bounds)
                            updated[key] = (min(old[0], bounds[0]), max(old[1], bounds[1]))
                    states = updated
                lows, highs = [], []
                for state, (low, high) in states.items():
                    eligible = [s for s in endings if allowed(s, state)]
                    assert len(eligible) == 1
                    for final, count in outcomes(eligible[0], state, words):
                        lows.append(low + count); highs.append(high + count)
                results[history + "/" + gift + "/" + question + "/" + str(len(witnesses)) + ":" + ",".join(witnesses)] = dict(minimum=min(lows), maximum=max(highs))
    assert original.SCENES == donor_snapshot
    return dict(delivery_scenes=len(SCENES), unique_visits=24, unique_recollections=8,
                fixtures=len(results), closure_paths=closure_count, ending_gate_checks=ending_checks, selected_words=results,
                minimum=min(x["minimum"] for x in results.values()),
                maximum=max(x["maximum"] for x in results.values()),
                status="author draft; unregistered; independent review and runtime verification required")


if __name__ == "__main__":
    import hashlib
    import json
    from pathlib import Path
    result = validate()
    result["sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
    print(json.dumps(result, indent=2))
