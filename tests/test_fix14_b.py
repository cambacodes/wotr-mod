"""fix14-b: behavioral witnesses on the generated structural story.

The runner regenerates development/Story.json before this module. A diagnostic
snapshot can be selected explicitly while an unrelated generation stage fails;
that narrower check does not establish final-export acceptance.
"""
import json
import os
from pathlib import Path
import unittest

from tests.structure import visible_slots

ROOT = Path(__file__).resolve().parents[1]


class StructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = Path(os.environ.get("RRT_FIX14_STORY_PATH", ROOT / "development/Story.json"))
        cls.story = json.loads(source.read_text(encoding="utf-8"))
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def node(self, sid, nid):
        return next(n for n in self.scenes[sid]["Nodes"] if n["Id"] == nid)

    def has(self, flag, flags, active=()):
        """Evaluate exported predicates, including current loss and route readers."""
        if flag in active:
            return False
        if flag in flags:
            return True
        next_active = (*active, flag)
        has = lambda f: self.has(f, flags, next_active)
        groups = self.story.get("Derived", {}).get(flag)
        if groups is None:
            return False
        if not any(all(has(f) for f in group) for group in groups):
            return False
        if any(has(f) for f in self.story.get("DerivedForbids", {}).get(flag, [])):
            return False
        for name in self.story.get("DerivedOpenRoutes", {}).get(flag, []):
            rel = self.story["Relationships"][name]
            if has(rel["ClosedFlag"]):
                return False
            for loss in [*rel.get("UnavailableFlags", []), *rel.get("EpochUnavailableFlags", [])]:
                override = rel.get("UnavailableOverrides", {}).get(loss)
                if has(loss) and not (override and has(override)):
                    return False
        return True

    def enabled(self, spec, flags):
        has = lambda f: self.has(f, flags)
        overrides = spec.get("ForbidOverrides", {})
        return (all(has(f) for f in spec.get("Requires", []))
                and all(not has(f) or (f in overrides and has(overrides[f]))
                        for f in spec.get("Forbids", []))
                and all(any(has(f) for f in group) for field in ("AnyGroups", "RequiresAnyGroups")
                        for group in spec.get(field, [])))

    def test_dagger_refusal_and_offers_have_exclusive_terminal_accounts(self):
        sid = "areelu.trickster.report.dagger"
        end = self.node(sid, "end")
        for branch, expected in [("keep", 1), ("give_mortal", 0), ("give_witch", 0)]:
            with self.subTest(branch=branch):
                flags = set(self.node(sid, branch)["EnterSet"])
                self.assertEqual(visible_slots(end, flags), {"end", "end/paragraph/" + str(expected)})
        self.assertEqual(self.node(sid, "why")["Choices"][1]["Next"], "keep")
        self.assertEqual(self.node(sid, "keep")["Choices"][0]["Next"], "end")

    def test_graft_outing_accounts_follow_played_branch(self):
        sid = "areelu.trickster.report.graft"
        for index, branch in enumerate(("stand", "wait", "sleep")):
            flags = set(self.node(sid, branch)["EnterSet"])
            self.assertEqual(visible_slots(self.node(sid, "after"), flags),
                             {"after", "after/paragraph/" + str(index)})

    def test_crossroads_stone_account_is_only_for_collected_stone(self):
        sid = "areelu.trickster.report.crossroads"
        end = self.node(sid, "end")
        for branch in ("rift_after", "buy_mortal", "buy_witch", "loud", "watch"):
            flags = set(self.node(sid, branch)["EnterSet"])
            shown = visible_slots(end, flags)
            self.assertEqual("end/paragraph/2" in shown, branch == "watch")
            self.assertEqual(len([slot for slot in shown if slot.startswith("end/paragraph/")
                                  and int(slot.rsplit("/", 1)[1]) >= 2]), 1)

    def test_closed_door_has_its_own_visitor_aftermath(self):
        sid = "areelu.trickster.report.visitors"
        end = self.node(sid, "end")
        self.assertEqual(visible_slots(end, set()), {"end", "end/paragraph/0"})
        self.assertEqual(visible_slots(end, set(self.node(sid, "shut")["EnterSet"])),
                         {"end", "end/paragraph/1"})

    def test_debate_recalled_threat_requires_heard_native_cue(self):
        end = self.node("eritrice.trickster.reconciled_debate", "exchange")
        for heard in (False, True):
            flags = {"eritrice.threatened_by_force"} if heard else set()
            self.assertEqual(visible_slots(end, flags),
                             {"exchange", "exchange/paragraph/" + str(0 if heard else 1)})

    def test_nenio_visit_reads_current_body_and_exclusive_return_history(self):
        visits = self.node("areelu.trickster.finale.after", "end")["Paragraphs"][:2]
        ordinary = {"trickster.ever", "chapter_later", "availability.observed"}
        revival = self.node("nenio.trickster.dead.the_price", "raised")["Choices"][0]
        self.assertEqual(revival["Revive"], "nenio")
        returned = ordinary | set(revival["Set"])
        self.assertEqual([self.enabled(p, ordinary) for p in visits], [True, False])
        self.assertEqual([self.enabled(p, returned) for p in visits], [False, True])
        for loss in ("nenio.life.unavailable", "nenio.returned_actor_lost", "nenio.epoch_unavailable",
                     "nenio.dissolved", "nenio.dead", "nenio.sent_away"):
            with self.subTest(loss=loss):
                self.assertEqual([self.enabled(p, returned | {loss}) for p in visits], [False, False])

    def test_melazmera_references_survive_other_romance_closure_and_absence(self):
        # Earn the owner's existing prerequisites and independently vary the referenced women.
        for sid in ("melazmera.trickster.ch4.plan", "melazmera.trickster.stone.second",
                    "melazmera.trickster.ch4.queen_after", "melazmera.trickster.beat.inquisitor"):
            scene = self.scenes[sid]
            own = {f for f in scene["Requires"] if not f.startswith("crossroute.")}
            for foreign in (set(), {"nocticula.closed", "iomedae.closed"},
                            {"nocticula.epoch_unavailable", "iomedae.epoch_unavailable"}):
                with self.subTest(scene=sid, foreign=foreign):
                    self.assertTrue(self.enabled(scene, own | foreign))
        for ending in ("together", "commit", "declined", "left_free"):
            page = self.node("melazmera.trickster.epilogue." + ending, "page")
            # A completed murder remains recorded after either independent romance closes.
            records = [p for p in page["Paragraphs"]
                       if "melazmera.trickster.cost.inquisitor" in p.get("Requires", [])]
            self.assertEqual(len(records), 1)
            self.assertTrue(self.enabled(records[0], {"melazmera.trickster.cost.inquisitor",
                                                     "iomedae.closed", "iomedae.epoch_unavailable"}))

    def test_eritrice_debt_reader_withholds_callability_after_unreconciled_loss(self):
        earned = {"trickster", "trickster.ever", "trickster.lastcall.open",
                  "availability.observed", "eritrice.trickster.cost.censured"}
        self.assertTrue(self.has("eritrice.lastcall.callable", earned))
        for closure in (set(), {"eritrice.closed"}):
            lost = earned | {"council.fought_nocta_allied", "eritrice.epoch_unavailable"} | closure
            self.assertFalse(self.has("eritrice.lastcall.callable", lost))
            self.assertFalse(self.enabled(self.scenes["eritrice.lastcall.call"], lost))
            for sid in ("trickster.lastcall.last_joke", "trickster.lastcall.last_joke.areelu"):
                # Inspect the reported debt blocker, without assuming that unrelated debts are paid.
                self.assertIn("eritrice.lastcall.callable", self.scenes[sid]["Forbids"])
                self.assertFalse(self.has("eritrice.lastcall.callable", lost))

    def test_predation_is_shown_before_consequences_and_has_player_response(self):
        sid = "melazmera.trickster.ch5.hunger"
        choice = self.node(sid, "ask")["Choices"][0]
        self.assertEqual(choice["Next"], "cultists")
        self.assertEqual(choice["Alignment"]["Direction"], "Evil")
        shown = self.node(sid, "cultists")
        self.assertGreaterEqual(len(shown["Choices"]), 2)
        self.assertEqual({c["Next"] for c in shown["Choices"]}, {"cultists_after"})
        self.assertNotIn("melazmera.trickster.fed.cultists", shown.get("EnterSet", []))
        self.assertIn("melazmera.trickster.fed.cultists", self.node(sid, "cultists_after")["EnterSet"])
        scene = self.scenes[sid]
        self.assertEqual(scene["Kind"], "visit")
        self.assertIn("2570015799edf594daf2f076f2f975d8", scene["Areas"])
        inquisitor = self.node("melazmera.trickster.beat.inquisitor", "do")
        self.assertGreaterEqual(len(inquisitor["Choices"]), 2)
        for response in inquisitor["Choices"]:
            self.assertIn("melazmera.trickster.beat.inquisitor_eaten", response["Set"])
            self.assertIn("melazmera.trickster.cost.inquisitor", response["Set"])


if __name__ == "__main__":
    unittest.main()
