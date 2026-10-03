"""Earned presence (TRICKSTER-RUBRIC "Binding context (3)" and "(4)"): tools/earned_presence_lint.py and the
storylines/earned_presence.py guard pass. Fixtures for every rule, the pass on a toy payload, and two worlds checked on
the generated story: off-Trickster canon stands (native slides play, the dead stay dead) and the lint is clean."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import earned_presence_lint as lint  # noqa: E402
from storylines import earned_presence as ep  # noqa: E402

STORY = ROOT / "development" / "Story.json"


def page(id, rel="her", requires=(), forbids=(), overrides=None, owner="Epilogue", anygroups=None):
    s = dict(Id=id, Owner=owner, Relationship=rel, Requires=list(requires), Forbids=list(forbids), Nodes=[])
    if overrides:
        s["ForbidOverrides"] = dict(overrides)
    if anygroups:
        s["RequiresAnyGroups"] = anygroups
    return s


def base():
    """A toy story: her route (committed, dead, returned on the Trickster path), a living page, a mourning page."""
    return {
        "Etudes": {"sacrifice": "g1", "her.dead": "g2", "ending.wound_closed": "g3", "ending.trickster": "g4", "trickster": "g5"},
        "Latches": {"trickster.ever": ["trickster"]},
        "Derived": {"trickster.commander_back": [["sacrifice", "trickster.ever", "ending.trickster"]]},
        "Relationships": {"her": dict(CommittedFlag="her.committed", ClosedFlag="her.closed", UnavailableFlags=["her.dead", "swarm"],
                                      UnavailableOverrides={"her.dead": "her.returned"},
                                      TricksterAccess={"dead": dict(Returned="her.returned")})},
        "Scenes": [
            dict(Id="her.device", Owner="Her", Relationship="her", Requires=["trickster.ever", "her.dead"], Forbids=[],
                 Nodes=[dict(Id="n", Choices=[dict(Set=["her.returned"], Requires=[], Forbids=[])])]),
            dict(Id="her.commit", Owner="Her", Relationship="her", Requires=[], Forbids=[],
                 Nodes=[dict(Id="n", Choices=[dict(Set=["her.committed"], Requires=[], Forbids=[])])]),
            page("her.ending_together", requires=("her.committed",), forbids=("her.closed", "sacrifice", "her.dead"),
                 overrides={"sacrifice": "trickster.commander_back", "her.dead": "her.returned"}),
            page("her.ending_sacrifice", requires=("her.committed", "sacrifice"), forbids=("trickster.commander_back", "her.dead"),
                 overrides={"her.dead": "her.returned"}),
        ],
        "NativeEpilogueEdits": {}, "NativeGates": {},
    }


def hard(story):
    found, _ = lint.check(story)
    return found


class LintRules(unittest.TestCase):
    def setUp(self):
        self._absent = dict(ep.COMMANDER_ABSENT)
        ep.COMMANDER_ABSENT.clear()

    def tearDown(self):
        ep.COMMANDER_ABSENT.clear()
        ep.COMMANDER_ABSENT.update(self._absent)

    def test_clean_fixture(self):
        self.assertEqual(hard(base()), [])

    def test_ep1_living_page_after_the_sacrifice(self):
        s = base()
        s["Scenes"].append(page("her.ending_open", requires=("her.committed",), forbids=("her.closed", "her.dead"),
                                overrides={"her.dead": "her.returned"}))
        self.assertEqual([x.split(" ")[:2] for x in hard(s)], [["EP1", "her.ending_open"]])

    def test_ep1_lift_by_a_non_return(self):
        s = base()
        s["Scenes"][2]["ForbidOverrides"]["sacrifice"] = "her.committed"
        self.assertTrue(any(x.startswith("EP1 her.ending_together") and "not an alive witness" in x for x in hard(s)))

    def test_ep1_alive_witness_and_allowlist(self):
        s = base()
        s["Scenes"].append(page("her.lastcall", requires=("trickster.commander_back",)))
        s["Scenes"].append(page("her.ending_apart", requires=("her.closed",)))
        self.assertEqual([x[:3] for x in hard(s)], ["EP1"])
        ep.COMMANDER_ABSENT["her.ending_apart"] = "independent"
        self.assertEqual(hard(s), [])

    def test_ep2_mourning_page_must_quiet_after_a_return(self):
        s = base()
        s["Scenes"][3]["Forbids"] = ["her.dead"]
        self.assertTrue(any(x.startswith("EP2 her.ending_sacrifice") for x in hard(s)))
        s["Scenes"][3]["Forbids"] = ["trickster.commander_back", "sacrifice", "her.dead"]
        self.assertTrue(any("can never play" in x for x in hard(s)))

    def test_ep2_composite_mourning(self):
        s = base()
        s["Derived"]["her.burned"] = [["sacrifice", "ending.wound_closed"]]
        s["Scenes"].append(page("her.burned_page", requires=("her.burned",), forbids=("sacrifice",),
                                overrides={"sacrifice": "trickster.commander_back"}))
        self.assertTrue(any(x.startswith("EP2 her.burned_page") for x in hard(s)))

    def test_ep4_stale_allowlist(self):
        ep.COMMANDER_ABSENT["nobody"] = "independent"
        ep.COMMANDER_ABSENT["her.ending_together"] = "independent"
        found = [x for x in hard(base()) if x.startswith("EP4")]
        self.assertEqual(len(found), 2)

    def test_ep5_her_own_death(self):
        s = base()
        s["Scenes"][2]["Forbids"].remove("her.dead")
        self.assertTrue(any(x.startswith("EP5 her.ending_together") for x in hard(s)))

    def test_t1_return_device_off_trickster(self):
        s = base()
        s["Scenes"][0]["Requires"] = ["her.dead"]          # the device no longer needs the Trickster path
        found = hard(s)
        self.assertTrue(any(x.startswith("T1 her: UnavailableOverrides") for x in found))
        self.assertTrue(any(x.startswith("T1 her: TricksterAccess") for x in found))

    def test_t1_canon_reading_is_not_a_canon_change(self):
        s = base()
        s["SeenCues"] = {"her.spared": ["c1"]}
        s["Derived"]["her.survived"] = [["her.spared"], ["her.returned"]]
        s["Relationships"]["her"]["UnavailableOverrides"]["her.dead"] = "her.survived"
        s["Scenes"][2]["ForbidOverrides"]["her.dead"] = "her.survived"
        self.assertEqual(hard(s), [])

    def test_t2_native_edit_needs_the_trickster_path(self):
        s = base()
        s["NativeEpilogueEdits"]["cue"] = dict(Replacement="her.ending_together", When=[["her.committed"]], Variants=[])
        self.assertTrue(any(x.startswith("T2 native edit cue") for x in hard(s)))
        s["NativeEpilogueEdits"]["cue"]["When"] = [["her.committed", "trickster.ever"]]
        self.assertEqual(hard(s), [])

    def test_t3_native_gate_needs_the_trickster_path(self):
        s = base()
        s["NativeGates"]["gate"] = dict(When=[["her.committed"]])
        self.assertTrue(any(x.startswith("T3 native gate gate") for x in hard(s)))
        s["NativeGates"]["gate"]["When"] = [["her.returned"]]
        self.assertEqual(hard(s), [])

    def test_t4_revival_off_trickster(self):
        s = base()
        s["Scenes"][1]["Nodes"][0]["Choices"][0]["Revive"] = "her"
        self.assertTrue(any(x.startswith("T4 her.commit") for x in hard(s)))
        s["Scenes"][1]["Requires"] = ["trickster"]
        self.assertEqual(hard(s), [])

    def test_t5_lifted_loss_off_trickster(self):
        s = base()
        s["Scenes"][2]["ForbidOverrides"]["her.dead"] = "her.committed"
        self.assertTrue(any(x.startswith("T5 her.ending_together") for x in hard(s)))


class GuardPass(unittest.TestCase):
    setUp = LintRules.setUp
    tearDown = LintRules.tearDown

    def payload(self):
        s = base()
        shared = {"her.dead": "her.returned"}
        s["Scenes"] += [page("her.ending_open", requires=("her.committed",), forbids=["her.closed", "her.dead"], overrides=shared),
                        page("her.ending_other", requires=("her.committed",), forbids=["her.closed", "her.dead"], overrides=shared),
                        page("her.ending_late", requires=("her.trickster.late_committed",), forbids=["her.closed"])]
        return s

    def test_guards_living_pages_and_leaves_mourning_alone(self):
        s = self.payload()
        added = ep.integrate(s)
        by = {x["Id"]: x for x in s["Scenes"]}
        self.assertIn("her.ending_open", added)
        self.assertEqual(by["her.ending_open"]["ForbidOverrides"]["sacrifice"], "trickster.commander_back")
        self.assertNotIn("sacrifice", by["her.ending_sacrifice"]["Forbids"])
        # The shared dict of another page is not mutated through this one.
        self.assertIsNot(by["her.ending_open"]["ForbidOverrides"], by["her.ending_other"]["ForbidOverrides"])
        # Her own return: the late commit page gains her death guard, lifted by her return.
        self.assertIn("her.dead", by["her.ending_late"]["Forbids"])
        self.assertEqual(by["her.ending_late"]["ForbidOverrides"]["her.dead"], "her.returned")
        self.assertEqual(hard(s), [])
        self.assertEqual(ep.integrate(s), [])   # idempotent

    def test_refuses_a_non_return_lift(self):
        s = self.payload()
        s["Scenes"].append(page("her.bad", requires=("her.committed",), overrides={"sacrifice": "her.committed"}))
        with self.assertRaises(ValueError):
            ep.integrate(s)


@unittest.skipUnless(STORY.exists(), "development/Story.json not generated")
class GeneratedStory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads(STORY.read_text(encoding="utf-8"))

    def test_lint_clean(self):
        self.assertEqual(hard(self.story), [])

    def test_off_trickster_canon_stands(self):
        """Worst-case off-Trickster world: every key that does not imply the Trickster path holds (native state and every
        authored flag reachable without it), closed under Story.Derived and Latches. No native slide is replaced, no native
        gate opens, no revival is offered, and no return lifts a death except a canon reading of native state."""
        s = self.story
        trk = lint.Trickster(s)
        keys = set()
        for sc in s["Scenes"]:
            keys.update(lint_keys(sc))
        for kind in lint.NATIVE_KINDS + ("Derived", "Latches"):
            keys.update((s.get(kind) or {}).keys())
        world = {k for k in keys if not trk.implies(k) and k not in s.get("Derived", {}) and k not in s.get("Latches", {})}
        changed = True
        while changed:
            changed = False
            for k, srcs in (s.get("Latches") or {}).items():
                if k not in world and any(x in world for x in srcs):
                    world.add(k); changed = True
            for k, groups in (s.get("Derived") or {}).items():
                if k not in world and any(all(x in world for x in g) for g in groups):
                    world.add(k); changed = True
        for root in ep.TRICKSTER_ROOTS + ep.NATIVE_TRICKSTER:
            self.assertNotIn(root, world)
        for cue, edit in (s.get("NativeEpilogueEdits") or {}).items():
            for v in [edit] + list(edit.get("Variants") or []):
                self.assertFalse(any(all(k in world for k in g) for g in v["When"]),
                                 "native slide %s replaced off-Trickster by %s" % (cue, v["Replacement"]))
        for name, gate in (s.get("NativeGates") or {}).items():
            self.assertFalse(any(all(k in world for k in g) for g in gate["When"]), "native gate %s opens off-Trickster" % name)
        canon = []
        for name, rel in s["Relationships"].items():
            for flag, ret in (rel.get("UnavailableOverrides") or {}).items():
                if ret in world:
                    self.assertTrue(trk.lift_ok(ret), "%s: %s lifted off-Trickster by %s" % (name, flag, ret))
                    canon.append(ret)
            for acc in (rel.get("TricksterAccess") or {}).values():
                self.assertNotIn(acc.get("Returned"), world)
        self.assertEqual(sorted(set(canon)), ["camellia.trickster.killed_held", "vellexia.fight_survived"])
        for sc in s["Scenes"]:
            for nd in sc.get("Nodes") or []:
                for ch in nd.get("Choices") or []:
                    if ch.get("Revive"):
                        self.assertFalse(all(k in world for k in sc["Requires"] + ch["Requires"]),
                                         "revival offered off-Trickster in " + sc["Id"])


def lint_keys(scene):
    for field in ("Requires", "Forbids"):
        yield from scene.get(field) or []
    for g in scene.get("RequiresAnyGroups") or []:
        yield from g
    yield from (scene.get("ForbidOverrides") or {}).values()
    for nd in scene.get("Nodes") or []:
        for ch in nd.get("Choices") or []:
            yield from ch.get("Set") or []
            yield from ch.get("Requires") or []


if __name__ == "__main__":
    unittest.main()
