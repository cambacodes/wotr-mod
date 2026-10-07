"""S06: current arrivals, qualified solo histories and one protected completion."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines import household_pair_minagho_chivarro as pair
from tools import rrt_verify as rules


class S06Acknowledgment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.pages = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(pair.P)}

    def state(self, *, minagho=True, chivarro=True, returned=True):
        state = rules.SimState(5, 1000)
        state.flags.update(["chapter_later", "trickster", "trickster.foresight.accepted",
                            "trickster.foresight.cost.promise", "availability.observed",
                            "minachiv.complete", "minachiv.before_the_last_road",
                            "minachiv.future_two", pair.R + "reunited"])
        if minagho:
            state.flags.add(pair.R + "minagho_in")
            if returned:
                state.flags.update(["minagho.dead", pair.R + "returned_minagho"])
            else:
                state.flags.add("minagho.spared.latched")
        else:
            state.flags.add("minagho.dead")
        if chivarro:
            state.flags.add(pair.R + "chivarro_in")
        else:
            state.flags.update(["chivarro.dead", "chivarro.exile_objective_done"])
        rules.sim_complete(self.model, state)
        return state

    def available(self, suffix, state):
        rules.sim_complete(self.model, state)
        page = self.pages[pair.P + "ack" + suffix]
        # The static simulator predates AbsentPartnerFlags. Mirror the C#
        # Blocks predicate using only the presence's validated absent losses.
        model = copy.copy(self.model)
        model.rels = copy.deepcopy(self.model.rels)
        absent = page.get("AbsentPartnerFlags", [])
        model.rels[pair.REL]["UnavailableFlags"] = [
            f for f in model.rels[pair.REL]["UnavailableFlags"] if f not in absent]
        presence = self.story["Presences"][page["InteractionHub"]]
        return (rules.presence_wanted(presence, state, page["Areas"][0])
                and rules.sim_available(model, page, state))

    def test_current_pair_and_each_solo_channel(self):
        for suffix, kwargs in [
            ("", {}), (".pair_spared", dict(returned=False)),
            (".minagho", dict(chivarro=False)),
            (".spared", dict(chivarro=False, returned=False)),
            (".chivarro", dict(minagho=False)),
        ]:
            with self.subTest(suffix=suffix):
                self.assertTrue(self.available(suffix, self.state(**kwargs)))

    def test_couple_acknowledgment_does_not_require_commander_romance(self):
        state = self.state()
        state.flags.difference_update(["minachiv.complete", "minachiv.before_the_last_road",
                                       "minachiv.future_two"])
        self.assertTrue(self.available("", state))
        state = self.state(chivarro=False)
        state.flags.difference_update(["minachiv.complete", "minachiv.before_the_last_road",
                                       "minachiv.future_two"])
        self.assertTrue(self.available(".minagho", state))

    def test_death_recall_requires_the_existing_death_state(self):
        for suffix, kwargs, other in [(".minagho", dict(chivarro=False), "chivarro"),
                                      (".chivarro", dict(minagho=False), "minagho")]:
            state = self.state(**kwargs)
            page = self.pages[pair.P + "ack" + suffix]
            answer = next(a for a in page["Nodes"][0]["Choices"] if a["Next"] == "dead")
            self.assertTrue(pair.STATE + other + ".dead" in state.flags)
            self.assertTrue(rules.sim_choice_available(answer, state))
            state.flags.discard(pair.STATE + other + ".dead")
            self.assertFalse(rules.sim_choice_available(answer, state))

    def test_living_distant_partner_is_not_attendance(self):
        state = self.state()
        state.flags.remove(pair.R + "chivarro_in")
        rules.sim_complete(self.model, state)
        self.assertIn("chivarro.present_now", state.flags)
        self.assertFalse(self.available("", state))
        self.assertTrue(self.available(".minagho", state))

    def test_page_path_closure_sacrifice_and_later_loss(self):
        for flag in ("minachiv.closed", "trickster.failed", "sacrifice",
                     "minagho.returned_actor_lost", "chivarro.returned_actor_lost",
                     pair.REL + ".presence.minagho.failed",
                     pair.REL + ".presence.chivarro.failed",
                     pair.R + "chivarro_sent_back", pair.R + "declined_minagho"):
            with self.subTest(flag=flag):
                state = self.state()
                state.flags.add(flag)
                self.assertFalse(self.available("", state))
        for remove in ("trickster", "trickster.foresight.accepted", pair.R + "minagho_in",
                       pair.R + "chivarro_in", pair.R + "reunited"):
            with self.subTest(remove=remove):
                state = self.state()
                state.flags.remove(remove)
                self.assertFalse(self.available("", state))
        state = self.state()
        state.flags.update(["sacrifice", "ending.trickster_full"])
        self.assertTrue(self.available("", state))

    def test_shared_witness_and_allowance_block_all_wrappers(self):
        for suffix, page in self.pages.items():
            self.assertIn(pair.ACK, page["Forbids"])
            self.assertEqual(page["RestAllowance"], "household.protected")
            self.assertEqual(page["HouseholdWitness"], pair.ACK)
            self.assertEqual(page["Relationship"], pair.REL)
            self.assertFalse(page["Participants"])
            declaration = self.story["PresenceExceptions"][page["InteractionHub"]]
            self.assertTrue(set(page.get("AbsentPartnerFlags", [])) <= set(declaration["AbsentLosses"]))
        state = self.state()
        state.flags.add(pair.ACK)
        self.assertFalse(self.available("", state))
        state = self.state()
        state.rest_spent["household.protected"] = 2
        self.assertFalse(self.available("", state))

    def test_solo_states_never_stage_the_missing_woman(self):
        for suffix, own in ((".minagho", "minagho"), (".spared", "minagho"),
                            (".chivarro", "chivarro")):
            page = self.pages[pair.P + "ack" + suffix]
            self.assertEqual(pair.WOMEN[page["Id"]], [own])
            self.assertTrue(all(node["Speaker"].lower() == own for node in page["Nodes"]))
            root = page["Nodes"][0]
            self.assertTrue(any(not a["Requires"] and not a["Forbids"] and not a["Abort"]
                                for a in root["Choices"]))

    def test_terminals_only_acknowledge_and_abort_is_clean(self):
        for page in self.pages.values():
            for node in page["Nodes"]:
                for answer in node["Choices"]:
                    if answer["Abort"]:
                        self.assertEqual(answer["Text"], "[Later.]")
                        self.assertFalse(answer["Set"])
                        self.assertIsNone(answer["Next"])
                    for flag in answer["Set"]:
                        self.assertTrue(flag.startswith(pair.P))
                        self.assertNotIn(".harem.", flag)
                    if answer["Next"] is None and not answer["Abort"]:
                        self.assertIn(pair.ACK, answer["Set"])
