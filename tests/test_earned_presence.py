"""Earned presence (TRICKSTER-RUBRIC "Binding context (3)" and "(4)"): tools/earned_presence_lint.py and the
storylines/earned_presence.py guard pass. Fixtures for every rule, the pass on a toy payload, and two worlds checked on
the generated story: off-Trickster canon stands (native slides play, the dead stay dead) and the lint is clean."""
import copy
import json
from pathlib import Path
import sys
import unittest
from tests.structure import without_prose

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
            dict(Id="her.device", Owner="Her", Relationship="her", Requires=["trickster", "her.dead"], Forbids=["trickster.failed"],
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


def mixed_page():
    s = page("irabeth.return_epilogue")
    s["Nodes"] = [dict(Id="page", Text="", Paragraphs=[
        dict(Text="The Commander visits her.", **copy.deepcopy(ep.GUARD)),
        dict(Text="They take another journey.", **copy.deepcopy(ep.GUARD)),
        dict(Text="She mourns the Commander.", Requires=[ep.SACRIFICE], Forbids=[ep.COMMANDER_BACK]),
    ])]
    return s


class LintRules(unittest.TestCase):
    def setUp(self):
        self._absent = dict(ep.COMMANDER_ABSENT)
        ep.COMMANDER_ABSENT.clear()
        self._paragraph_guarded = set(ep.PARAGRAPH_GUARDED)
        ep.PARAGRAPH_GUARDED.clear()

    def tearDown(self):
        ep.COMMANDER_ABSENT.clear()
        ep.COMMANDER_ABSENT.update(self._absent)
        ep.PARAGRAPH_GUARDED.clear()
        ep.PARAGRAPH_GUARDED.update(self._paragraph_guarded)

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

    def test_ep6_mixed_page(self):
        s = base()
        s["Scenes"].append(mixed_page())
        ep.PARAGRAPH_GUARDED.add("irabeth.return_epilogue")
        self.assertEqual(hard(s), [])

    def test_ep6_every_living_paragraph_needs_the_exact_guard(self):
        for i in (0, 1):
            for change in (dict(Forbids=[]), dict(ForbidOverrides={}),
                           dict(ForbidOverrides={ep.SACRIFICE: "her.committed"})):
                with self.subTest(paragraph=i, change=change):
                    s = base()
                    mixed = mixed_page()
                    mixed["Nodes"][0]["Paragraphs"][i].update(change)
                    s["Scenes"].append(mixed)
                    ep.PARAGRAPH_GUARDED.add(mixed["Id"])
                    found = hard(s)
                    self.assertEqual(len(found), 1)
                    self.assertTrue(found[0].startswith("EP6 irabeth.return_epilogue/page/paragraph[%d]" % i))

    def test_ep6_node_text_needs_its_own_guard(self):
        s = base()
        mixed = mixed_page()
        mixed["Nodes"][0]["Text"] = "The Commander arrives."
        s["Scenes"].append(mixed)
        ep.PARAGRAPH_GUARDED.add(mixed["Id"])
        self.assertTrue(any(x.startswith("EP6 irabeth.return_epilogue/page: living text") for x in hard(s)))
        mixed["Nodes"][0].update(copy.deepcopy(ep.GUARD))
        self.assertEqual(hard(s), [])

    def test_ep6_mourning_must_exist_and_only_play_while_dead(self):
        for change, message in ((dict(Requires=[]), "no mourning paragraph"),
                                (dict(Forbids=[]), "mourning text must Forbid"),
                                (dict(Forbids=[ep.COMMANDER_BACK, ep.SACRIFICE]), "mourning text must Forbid")):
            with self.subTest(change=change):
                s = base()
                mixed = mixed_page()
                mixed["Nodes"][0]["Paragraphs"][2].update(change)
                s["Scenes"].append(mixed)
                ep.PARAGRAPH_GUARDED.add(mixed["Id"])
                self.assertTrue(any(x.startswith("EP6 ") and message in x for x in hard(s)))

    def test_ep6_scene_guard_cannot_hide_mourning(self):
        s = base()
        mixed = mixed_page()
        mixed.update(copy.deepcopy(ep.GUARD))
        s["Scenes"].append(mixed)
        ep.PARAGRAPH_GUARDED.add(mixed["Id"])
        self.assertTrue(any(x.startswith("EP6 ") and "blocking its mourning" in x for x in hard(s)))
        mixed["Forbids"] = []
        mixed["Owner"] = "Her"
        self.assertTrue(any(x.startswith("EP6 ") and "not an epilogue" in x for x in hard(s)))

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
        s["NativeEpilogueEdits"]["cue"]["When"] = [["her.committed", "trickster.now"]]
        self.assertEqual(hard(s), [])

    def test_t3_native_gate_needs_the_trickster_path(self):
        s = base()
        s["NativeGates"]["gate"] = dict(When=[["her.committed"]])
        self.assertTrue(any(x.startswith("T3 native gate gate") for x in hard(s)))
        s["NativeGates"]["gate"]["When"] = [["her.returned"]]
        self.assertEqual(hard(s), [])

    def test_t6a_canon_change_needs_the_current_path(self):
        # Engine-q2: her commitment is not a Trickster act, so the run latch is the edit's only Trickster evidence.
        s = base()
        s["NativeEpilogueEdits"]["cue"] = dict(Replacement="her.ending_together", When=[["her.committed", "trickster.ever"]], Variants=[])
        s["NativeGates"]["gate"] = dict(When=[["trickster.was", "her.committed"]])
        s["NativeEpilogueSuppressions"] = {"sup": dict(When=[["trickster.ever", "her.committed", "!her.closed"]])}
        s["NativeObjectiveSettlements"] = {"obj": dict(When=[["trickster.ever", "her.committed"]])}
        s["Etudes"]["trickster.was"] = "g6"
        found = hard(s)
        for what in ("native edit cue", "native gate gate", "native suppression sup", "native settlement obj"):
            self.assertTrue(any(x.startswith("T6a " + what) for x in found), what)
        s["NativeEpilogueEdits"]["cue"]["When"] = [["her.committed", "trickster.now"]]
        s["NativeGates"]["gate"]["When"] = [["trickster.now", "her.committed"]]
        s["NativeEpilogueSuppressions"]["sup"]["When"] = [["trickster.now", "her.committed", "!her.closed"]]
        s["NativeObjectiveSettlements"]["obj"]["When"] = [["trickster.now", "her.committed"]]
        self.assertEqual(hard(s), [])

    def test_t6a_a_trickster_act_keeps_the_latch(self):
        # Her return was set by a device that needed the live power: a historical act, read with the run latch.
        s = base()
        s["NativeGates"]["gate"] = dict(When=[["trickster.ever", "her.returned"]])
        self.assertEqual(hard(s), [])
        # A key whose only Trickster source is the latch proves no act.
        s["Derived"]["her.latch_only"] = [["trickster.ever", "her.committed"]]
        s["NativeGates"]["gate"]["When"] = [["trickster.ever", "her.latch_only"]]
        self.assertTrue(any(x.startswith("T6a native gate gate") for x in hard(s)))

    def test_t6b_current_path_keys(self):
        s = base()
        key = sorted(ep.CURRENT_PATH_KEYS)[0]
        s["Derived"][key] = [["trickster.ever", "her.committed"]]
        self.assertTrue(any(x.startswith("T6b " + key) for x in hard(s)))
        s["Derived"][key] = [["trickster.now", "her.committed"]]
        self.assertEqual(hard(s), [])

    def test_t4_revival_off_trickster(self):
        s = base()
        s["Scenes"][1]["Nodes"][0]["Choices"][0]["Revive"] = "her"
        self.assertTrue(any(x.startswith("T4 her.commit") for x in hard(s)))
        s["Scenes"][1]["Requires"] = ["trickster"]
        s["Scenes"][1]["Forbids"] = ["trickster.failed"]
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

    def test_queen_slides_drop_only_the_commander_guard(self):
        from storylines import galfrey_queen_slide
        s = base()
        originals = copy.deepcopy(galfrey_queen_slide.SCENES)
        s["Scenes"].extend(copy.deepcopy(originals))
        for original in originals:
            ep.COMMANDER_ABSENT[original["Id"]] = "native_queen"
        added = ep.integrate(s)
        for original, exported in zip(originals, s["Scenes"][-2:]):
            with self.subTest(scene=original["Id"]):
                self.assertNotIn(original["Id"], added)
                expected = copy.deepcopy(original)
                expected["Forbids"].remove(ep.SACRIFICE)
                del expected["ForbidOverrides"][ep.SACRIFICE]
                self.assertEqual(without_prose(exported), without_prose(expected))
        self.assertEqual(without_prose(galfrey_queen_slide.SCENES), without_prose(originals))
        self.assertEqual(hard(s), [])
        self.assertEqual(ep.integrate(s), [])

    def test_mixed_page_skips_scene_guard_only_when_valid(self):
        s = base()
        mixed = mixed_page()
        s["Scenes"].append(mixed)
        ep.PARAGRAPH_GUARDED.add(mixed["Id"])
        before = copy.deepcopy(mixed)
        self.assertEqual(ep.integrate(s), [])
        self.assertEqual(without_prose(mixed), without_prose(before))
        self.assertEqual(hard(s), [])
        mixed["Nodes"][0]["Paragraphs"][1]["Forbids"] = []
        with self.assertRaisesRegex(ValueError, r"irabeth.return_epilogue: page/paragraph\[1\]"):
            ep.integrate(s)


@unittest.skipUnless(STORY.exists(), "development/Story.json not generated")
class GeneratedStory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = json.loads(STORY.read_text(encoding="utf-8"))

    def test_current_path_reader(self):
        story = json.loads(STORY.read_text(encoding="utf-8"))
        self.assertEqual(story["Derived"].get(ep.TRICKSTER_NOW), [["trickster"]])
        self.assertTrue({"trickster.failed", "dragon", "legend", "swarm"} <= set(story["DerivedForbids"][ep.TRICKSTER_NOW]))
        leaky = [x["Id"] for x in story["Scenes"] if "trickster" in x["Requires"]
                 and "trickster.failed" not in x["Requires"] + x["Forbids"]]
        self.assertEqual(leaky, [])

    def test_lint_clean(self):
        self.assertEqual(hard(self.story), [])

    def test_queen_replacements_survive_an_unreturned_sacrifice(self):
        from storylines import galfrey_queen_slide
        by = {s["Id"]: s for s in self.story["Scenes"]}
        for cue, (sid, _) in galfrey_queen_slide.REPLACEMENTS.items():
            with self.subTest(scene=sid):
                scene = by[sid]
                self.assertIn(sid, ep.COMMANDER_ABSENT)
                self.assertNotIn(ep.SACRIFICE, scene["Forbids"])
                self.assertNotIn(ep.SACRIFICE, scene.get("ForbidOverrides") or {})
                self.assertEqual(scene["Requires"], ["trickster.ever", galfrey_queen_slide.RETURNED, galfrey_queen_slide.CROWN, "galfrey.present_now"])
                edit = self.story["NativeEpilogueEdits"][cue]
                self.assertEqual(edit["Replacement"], sid)
                self.assertEqual(edit["When"], [list(dict.fromkeys([*g, "galfrey.present_now"])) for g in galfrey_queen_slide.WHEN])

    def test_jerribeth_unfinished_keeps_earned_commander_return_guard(self):
        scene = next(s for s in self.story["Scenes"] if s["Id"] == "jerribeth.ending_unfinished")
        self.assertNotIn(scene["Id"], ep.COMMANDER_ABSENT)
        self.assertIn(ep.SACRIFICE, scene["Forbids"])
        self.assertEqual(scene["ForbidOverrides"][ep.SACRIFICE], ep.COMMANDER_BACK)

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
