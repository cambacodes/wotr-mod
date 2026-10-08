"""Job-4 parked saves and selectable paths through the shortened base chain."""
import unittest

from tests.story_fixture import fresh_story
from storylines import minachiv_scaffolding as route
from tools import rrt_verify as verify


class MinachivScaffoldingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.pages = {s["Id"]: s for s in cls.story["Scenes"]}
        cls.model = verify.Model(cls.story)
        cls.available_pages = cls.model.by_id

    def page(self, sid):
        return self.pages[route.PREFIX + sid]

    def node(self, sid, nid):
        return next(n for n in self.page(sid)["Nodes"] if n["Id"] == nid)

    def state(self, *flags):
        state = verify.SimState(5, 5000)
        state.flags.update(("chapter_later", "trickster", "trickster.ever", "availability.observed",
                            "minagho.ran_complete", "minagho.book_three_finished",
                            "chivarro.searching", *flags))
        verify.sim_complete(self.model, state)
        return state

    def test_each_rewired_gate_accepts_its_parked_save(self):
        for sid, (old, new) in route.REWIRED.items():
            with self.subTest(scene=sid):
                page = self.page(sid)
                self.assertNotIn(route.PREFIX + old, page["Requires"])
                self.assertIn(route.PREFIX + new, page["Requires"])
                state = self.state(route.PREFIX + new)
                self.assertTrue(verify.sim_available(self.model, self.available_pages[page["Id"]], state))
                state.flags.discard(route.PREFIX + new)
                self.assertFalse(verify.sim_available(self.model, self.available_pages[page["Id"]], state))

    def test_all_retired_scenes_keep_nodes_but_cannot_open_in_chapter_five(self):
        for sid in route.RETIRED:
            page = self.page(sid)
            self.assertIn("chapter_later", page["Forbids"])
            self.assertEqual("event", page["Kind"])
            self.assertTrue(page["Nodes"])
            self.assertTrue(all(n["Text"] == route.RETIRED_TEXT for n in page["Nodes"]))
            state = self.state(*page["Requires"])
            self.assertFalse(verify.sim_available(self.model, self.available_pages[page["Id"]], state))

    def test_branchless_old_saves_have_fallbacks_and_branch_saves_keep_originals(self):
        for sid, nid, index, predecessor, branches in (
            ("what_the_offer_bought", "start", 3, "offer_heard",
             ("business_chosen", "bait_chosen", "refusal_chosen")),
            ("when_the_door_opens", "ending", 2, "preview_kept", ("winter_ending", "host_ending")),
            ("after_the_last_lamp", "start", 2, "show_kept", ("after_show_promised", "after_show_open")),
        ):
            choices = self.node(sid, nid)["Choices"]
            state = self.state(route.PREFIX + predecessor)
            self.assertTrue(verify.sim_choice_available(choices[index], state))
            for branch in branches:
                state = self.state(route.PREFIX + predecessor, route.PREFIX + branch)
                self.assertFalse(verify.sim_choice_available(choices[index], state))
                self.assertTrue(any(verify.sim_choice_available(a, state) for a in choices[:index]))

    def test_forger_legacy_terminals_and_appended_onward_choices(self):
        for nid in ("proof", "price", "question"):
            choices = self.node("the_price_of_her_name", nid)["Choices"]
            self.assertIsNone(choices[0]["Next"])
            self.assertIn("minachiv.forger_spared", choices[0]["Set"])
            self.assertIn("minachiv.name_kept", choices[0]["Set"])
            self.assertEqual("alley", choices[1]["Next"])
            self.assertNotIn("minachiv.forger_spared", choices[1]["Set"])

    def test_door_terminal_sets_only_the_selected_after_show_variant(self):
        choices = self.node("when_the_door_opens", "after")["Choices"]
        for barred, flag in ((False, "after_show_promised"), (True, "after_show_open")):
            state = self.state(*(route.flags("door_barred") if barred else ()))
            selectable = [a for a in choices if verify.sim_choice_available(a, state)]
            self.assertEqual(1, len(selectable))
            self.assertTrue(set(route.flags("show_kept", "entrance_chosen", "ending_rehearsed", flag))
                            <= set(selectable[0]["Set"]))

    def test_new_nodes_use_one_placeholder_and_no_conditional_paragraphs(self):
        for sid in ("the_remaining_customers", "what_the_offer_bought", "minaghos_unfinished_sentence",
                    "the_performer_and_the_key", "the_price_of_her_name", "the_first_small_audience",
                    "when_the_door_opens"):
            placeholders = [n for n in self.page(sid)["Nodes"] if n["Text"].startswith("[PROSE PENDING:")]
            self.assertTrue(placeholders, sid)
            for node in placeholders:
                self.assertEqual("[PROSE PENDING: minachiv." + sid + "]", node["Text"])
                self.assertFalse(node.get("Paragraphs"))

    def test_street_and_door_deliver_as_drezen_book_visits(self):
        for sid in ("minaghos_unfinished_sentence", "when_the_door_opens"):
            page = self.page(sid)
            self.assertTrue(page["Remote"])
            self.assertEqual("visit", page["Kind"])
            self.assertEqual(["2570015799edf594daf2f076f2f975d8"], page["Areas"])
            self.assertFalse(page.get("AnswerLists"))
            self.assertFalse(page.get("NativeReturnCue"))

    def test_brand_fallback_has_no_invented_producer(self):
        self.assertEqual([["minagho.ran_complete"]], self.story["Derived"]["minachiv.brand_live"])
        self.assertFalse(any("minachiv.brand_live" in a["Set"] for s in self.story["Scenes"]
                             for n in s["Nodes"] for a in n["Choices"]))

    def test_late_generated_legacy_leave_keeps_morning_index_two(self):
        choices = self.node("minaghos_unfinished_sentence", "morning")["Choices"]
        self.assertEqual("[Leave.]", choices[2]["Text"])
        self.assertTrue(choices[2]["Abort"])
        self.assertEqual(["minagho_chivarro.outcome.eligible"], choices[2]["Forbids"])
        self.assertFalse(choices[2]["Set"])
        self.assertEqual(31, choices[3]["Check"]["DC"])

    def test_zero_resources_leave_a_selectable_call_and_all_results_can_continue(self):
        for sid, nid in (("minaghos_unfinished_sentence", "morning"),
                         ("the_performer_and_the_key", "fee"),
                         ("the_first_small_audience", "proposal"),
                         ("when_the_door_opens", "first_scene")):
            for budget in (0, 49, 50, 99, 100, 199, 200):
                with self.subTest(scene=sid, node=nid, budget=budget):
                    state = self.state("minachiv.private_booking")
                    state.crusade_resources = {"Finances": budget, "Favors": budget}
                    self.assertTrue(any(verify.sim_choice_available(a, state)
                                        for a in self.node(sid, nid)["Choices"]))
        # Payment is checked before entering these nodes; no unaffordable sole exit.
        for sid, nid in (("minaghos_unfinished_sentence", "protect_success"),
                         ("minaghos_unfinished_sentence", "protect_failure"),
                         ("the_performer_and_the_key", "officer_names_bought"),
                         ("the_first_small_audience", "outbid")):
            self.assertTrue(all(not a.get("Crusade") for a in self.node(sid, nid)["Choices"]))

    def test_retirement_inventory_and_slot_index_cover_the_same_hosts(self):
        import json
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        expected = set(route.flags(*route.RETIRED))
        for name in ("departure", "payoff", "participant_inventory", "earned_outcome_inventory",
                     "own_life", "implicit_participant_inventory"):
            data = json.loads((root / "tools" / (name + "_contracts.json")).read_bytes())
            self.assertEqual(expected, set(data["minachiv_retired_surfaces"]))
        slots = json.loads((root / "tools/route_packs/plans/minachiv-slot-index.json").read_bytes())
        self.assertEqual(expected, set(slots["retired_hosts"]))
        self.assertEqual([], slots["dropped_slots"])


if __name__ == "__main__":
    unittest.main()
