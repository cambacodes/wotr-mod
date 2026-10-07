"""S28 histories against the production Python rules mirror and actual route adapters."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s28
from tools import rrt_verify as rules, savecompat


class S28Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)
        cls.payload = copy.deepcopy(cls.base)
        s28.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rules.Model(cls.payload)
        cls.rows = [s for s in cls.model.scenes if s["Id"].startswith(s28.P)]

    def state(self, *, defected=False, mind=False):
        st = rules.SimState(5, 1000)
        st.flags.update(["trickster", "trickster.ever", "trickster.foresight.accepted",
                         "household.table.kept", "jerribeth.committed", "vellexia.committed"])
        for woman in s28.PAIR:
            st.flags.update(self.payload["Derived"][woman + ".payoff.ordinary"][0])
        if defected:
            st.flags.add(s28.DEFECTION)
        if mind:
            st.flags.update(["jerribeth.unavailable", "jerribeth.trickster.returned"])
        rules.sim_complete(self.model, st)
        return st

    def offered(self, st):
        return [s for s in self.rows if rules.sim_available(self.model, s, st)]

    def finish(self, scene, st, route, check="Success"):
        """Select the requested root, then walk the actual graph to completion."""
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        node = nodes["start"]
        index = route
        visited = []
        while True:
            answer = node["Choices"][index]
            self.assertTrue(rules.sim_choice_available(answer, st))
            visited.append(node["Id"])
            if answer["Abort"]:
                return visited
            for flag in answer["Set"]:
                st.flags.add(flag)
                st.times[flag] = st.hour
            target = answer["Check"][check] if answer["Check"] else answer["Next"]
            if target is None:
                st.flags.add(scene["Id"])
                st.times[scene["Id"]] = st.hour
                key = scene["RestAllowance"]
                st.rest_spent[key] = st.rest_spent.get(key, 0) + 1
                rules.sim_complete(self.model, st)
                return visited
            node, index = nodes[target], 0

    def test_each_history_and_channel_selects_exactly_one_primary(self):
        for defected in (False, True):
            for mind in (False, True):
                with self.subTest(defected=defected, mind=mind):
                    offers = self.offered(self.state(defected=defected, mind=mind))
                    self.assertEqual(len(offers), 1)
                    self.assertIn("defected" if defected else "client", offers[0]["Id"])
                    self.assertEqual(offers[0]["Id"].endswith(".mind"), mind)

    def test_page_current_path_chapter_and_contact_are_independent_gates(self):
        for removed in ("trickster.foresight.accepted", "trickster", "jerribeth.committed", "vellexia.committed"):
            st = self.state()
            st.flags.remove(removed)
            rules.sim_complete(self.model, st)
            self.assertEqual(self.offered(st), [], removed)
        for chapter in (3, 4, 6):
            st = self.state()
            st.chapter = chapter
            self.assertEqual(self.offered(st), [])
        for changed_path in ("legend", "dragon", "swarm", "trickster.failed"):
            st = self.state()
            st.flags.add(changed_path)
            rules.sim_complete(self.model, st)
            self.assertEqual(self.offered(st), [], changed_path)

    def test_current_closure_loss_and_later_loss_beat_old_returns(self):
        for mind in (False, True):
            for loss in ("jerribeth.closed", "vellexia.closed", "jerribeth.epoch_unavailable",
                         "vellexia.epoch_unavailable", "jerribeth.returned_actor_lost",
                         "vellexia.returned_actor_lost"):
                st = self.state(mind=mind)
                st.flags.update([loss, "vellexia.trickster.returned"])
                rules.sim_complete(self.model, st)
                self.assertEqual(self.offered(st), [], (mind, loss))
        st = self.state(mind=True)
        st.flags.add("jerribeth.trickster.cost.host")
        rules.sim_complete(self.model, st)
        self.assertEqual(self.offered(st), [])

    def test_sacrifice_requires_existing_commander_return(self):
        st = self.state()
        st.flags.add("sacrifice")
        self.assertEqual(self.offered(st), [])
        st.flags.add("trickster.commander_back")
        self.assertEqual(len(self.offered(st)), 1)

    def test_deeds_follow_both_replies_on_check_and_labor_success(self):
        for defected in (False, True):
            for mind in (False, True):
                for root in (0, 1):
                    st = self.state(defected=defected, mind=mind)
                    offered = self.offered(st)[0]
                    visited = self.finish(offered, st, root)
                    self.assertLess(visited.index("jerribeth"), visited.index("account"))
                    self.assertLess(visited.index("vellexia"), visited.index("account"))
                    self.assertIn(s28.P + "account.kept", st.flags)
                    self.assertEqual(s28.P + "defection.answered" in st.flags, defected)
                    self.assertEqual(s28.P + "client.account_named" in st.flags, not defected)
                    self.assertFalse(any(".reconciled." in f or ".enmity." in f for f in st.flags))
                    self.assertEqual(self.offered(copy.deepcopy(st)), [])

    def test_failure_one_retry_clock_and_all_retry_outcomes(self):
        for defected in (False, True):
            for root in (0, 1, 2, 3):
                st = self.state(defected=defected)
                self.finish(self.offered(st)[0], st, 0, check="Failure")
                self.assertNotIn(s28.P + "account.kept", st.flags)
                self.assertEqual(self.offered(st), [])
                st.hour += 47
                self.assertEqual(self.offered(st), [])
                st.hour += 1
                offers = self.offered(st)
                self.assertEqual(len(offers), 1)
                self.assertIn("retry.", offers[0]["Id"])
                before = copy.deepcopy(st.__dict__)
                self.finish(offers[0], st, root)
                if root == 3:
                    self.assertEqual(st.__dict__, before)
                else:
                    self.assertEqual(self.offered(st), [])
                    self.assertEqual(st.rest_spent["household.protected"], 2)
                    self.assertEqual(s28.P + "account.kept" in st.flags, root == 0)

    def test_primary_refusal_and_abort_never_create_failures(self):
        for root in (2, 3):
            st = self.state()
            before = copy.deepcopy(st.__dict__)
            self.finish(self.offered(st)[0], st, root)
            self.assertNotIn(s28.P + "settle.failed", st.flags)
            if root == 3:
                self.assertEqual(st.__dict__, before)
            else:
                st.hour += 500
                st.rest_spent.clear()
                self.assertEqual(self.offered(st), [])

    def test_allowance_rechecked_and_retry_rechecks_departure(self):
        st = self.state()
        st.rest_spent["household.protected"] = 2
        self.assertEqual(self.offered(st), [])
        st.rest_spent.clear()
        self.finish(self.offered(st)[0], st, 0, check="Failure")
        st.hour += 48
        st.flags.add("vellexia.epoch_unavailable")
        rules.sim_complete(self.model, st)
        self.assertEqual(self.offered(st), [])

    def test_registered_content_does_not_activate_optional_arc_or_change_marhevok(self):
        self.assertEqual(len(self.rows), 8)
        self.assertFalse(any(s["HouseholdCategory"] == "pair" for s in self.rows))
        for page in self.rows:
            writes = [f for node in page["Nodes"] for answer in node["Choices"] for f in answer["Set"]]
            self.assertTrue(all(f.startswith(s28.P) for f in writes))
            self.assertFalse(any("marhevok" in f or "client_of" in f for f in writes))
            self.assertFalse(any(node["Paragraphs"] for node in page["Nodes"]))

    def test_save_compatibility_and_repeat_registration(self):
        self.assertEqual(savecompat.check(self.payload, savecompat.inventory(self.base)), [])
        repeated = copy.deepcopy(self.payload)
        s28.register(repeated, repeated["Scenes"], repeated["Etudes"])
        self.assertEqual(repeated, self.payload)
        self.assertEqual(self.base["SeenCues"][s28.DEFECTION], ["e0ee422a413a5f94ea90bede3096ee56"])
        self.assertNotIn(s28.DEFECTION, self.payload["Etudes"])

    def test_candidates_keep_all_personal_outcomes_and_empty_slot_aftermath(self):
        candidate = s28.OPTIONAL_CANDIDATES[2]
        nodes = {n["Id"]: n for n in candidate["Nodes"]}
        self.assertEqual(nodes["start"]["Choices"][0]["Next"], "jerribeth_answer")
        self.assertEqual(nodes["jerribeth_answer"]["Choices"][0]["Next"], "vellexia_answer")
        self.assertEqual(nodes["vellexia_answer"]["Choices"][0]["Next"], "mutual")
        self.assertEqual(nodes["explicit.1"]["Choices"][0]["Next"], "appointment")
        self.assertEqual(nodes["explicit.1"]["Choices"][0]["Set"], [])
        self.assertEqual(len(nodes["start"]["Choices"]), 5)
        self.assertEqual([s["DelayHours"] for s in s28.OPTIONAL_CANDIDATES], [48, 48, 48, 8])
        self.assertEqual(sum(bool(s.get("HouseholdArcStart")) for s in s28.OPTIONAL_CANDIDATES), 1)
        root = Path(__file__).resolve().parents[1]
        brief = json.loads((root / "tools/route_packs/explicit_slots/harem" /
                           (candidate["Id"] + ".explicit.1.json")).read_text(encoding="utf-8"))
        self.assertEqual(brief["commander"], "absent")
        self.assertTrue(brief["status"].startswith("blocked"))

    def test_w3_reservation_cannot_ship_even_with_every_personal_deed(self):
        """No combination of historical visits or desire activates withheld pages."""
        staged_ids = {s["Id"] for s in s28.OPTIONAL_CANDIDATES}
        self.assertFalse(staged_ids.intersection(s["Id"] for s in self.payload["Scenes"]))
        for defected in (False, True):
            for mind in (False, True):
                st = self.state(defected=defected, mind=mind)
                st.flags.update(f for page in s28.OPTIONAL_CANDIDATES
                                for node in page["Nodes"] for answer in node["Choices"]
                                for f in answer["Set"])
                st.flags.update(s28.BODY_REQUIRES)
                st.flags.update(["jerribeth.trickster.visited", "vellexia.trickster.visited"])
                rules.sim_complete(self.model, st)
                self.assertFalse(staged_ids.intersection(s["Id"] for s in self.offered(st)))
                self.assertNotIn(s28.P + "choice.explicit.1", self.model.authored)

    def test_all_staged_steps_recheck_bodies_and_prescribed_clocks(self):
        predecessors = ("account.kept", "company.both_friends",
                        "invitation.both_interested", "choice.both_yes")
        self.assertEqual(sum(s["DelayHours"] for s in s28.OPTIONAL_CANDIDATES), 152)
        for page, predecessor in zip(s28.OPTIONAL_CANDIDATES, predecessors):
            with self.subTest(step=page["Id"]):
                self.assertIn(s28.P + predecessor, page["Requires"])
                self.assertTrue(set(s28.BODY_REQUIRES).issubset(page["Requires"]))
                self.assertTrue(set(s28.BODY_FORBIDS).issubset(page["Forbids"]))
                self.assertTrue(set(s28.COMMON).issubset(page["Requires"]))
                self.assertTrue(set(s28.LOSSES).issubset(page["Forbids"]))
                self.assertEqual(page["Participants"], s28.PAIR)
                self.assertEqual(page["RestAllowance"], "household.pair")
                self.assertFalse(any(n.get("Paragraphs") for n in page["Nodes"]))

    def test_staged_choices_keep_independent_no_friend_yes_and_abort_outcomes(self):
        """Graph review only: no test body window is registered in production."""
        for page in s28.OPTIONAL_CANDIDATES:
            page = rules.norm_scene(page)
            start = next(n for n in page["Nodes"] if n["Id"] == "start")
            for index in range(len(start["Choices"])):
                with self.subTest(step=page["Id"], answer=index):
                    st = self.state()
                    before = copy.deepcopy(st.__dict__)
                    visited = self.finish(page, st, index)
                    if start["Choices"][index]["Abort"]:
                        self.assertEqual(st.__dict__, before)
                        continue
                    step = page["Id"].removeprefix(s28.P)
                    self.assertIn(s28.P + step + ".seen", st.flags)
                    self.assertEqual(st.rest_spent["household.pair"], 1)
                    self.assertFalse(any(".reconciled." in f or ".enmity." in f for f in st.flags))
                    if step == "choice":
                        outcome = ("both_yes", "jerribeth_no", "vellexia_no", "friends_only")[index]
                        self.assertIn(s28.P + "choice." + outcome, st.flags)
                        self.assertEqual("explicit.1" in visited, index == 0)
                        if index == 0:
                            self.assertLess(visited.index("jerribeth_answer"), visited.index("mutual"))
                            self.assertLess(visited.index("vellexia_answer"), visited.index("mutual"))
                            self.assertEqual(visited[-1], "appointment")

    def test_real_owner_presences_end_on_visited_and_cannot_supply_long_stay(self):
        for woman in s28.PAIR:
            presence = self.payload["Presences"][woman + ".presence"]
            self.assertIn(woman + ".trickster.visited", presence["Forbids"])
            self.assertEqual(presence["MinChapter"], 5)
            self.assertEqual(presence["MaxChapter"], 5)


if __name__ == "__main__":
    unittest.main()
