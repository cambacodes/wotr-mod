"""W4 visible knowledge, historical favours, and current single-woman bodies."""
import copy
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from storylines.harem_rows import household_knowledge as row
from tools import rrt_verify as rules, savecompat


class HouseholdKnowledge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(dict(cls.story, Scenes=[s for s in cls.story["Scenes"]
                                                      if s["Id"].startswith(row.PREFIX)]))

    def setUp(self):
        self.scenes = {s["Id"]: s for s in self.model.scenes
                       if s["Id"].startswith(row.PREFIX)}

    def state_for(self, body):
        state = rules.SimState(3, 1000)
        state.flags.update(body["Requires"])
        learner = body["ParticipantWomen"][0]
        state.flags.update(self.story["SeatWomen"][learner]["Requires"])
        # The current route's eligible arm is an input, not a favour producer.
        state.flags.update(self.model.composites[learner + ".harem.eligible"][0])
        return state

    def test_disclosure_and_abort_are_the_only_histories(self):
        self.assertEqual(set(self.scenes), {row.PREFIX + key for key in row.FAVOURS})
        for key in row.FAVOURS:
            body = self.scenes[row.PREFIX + key]
            state = self.state_for(body)
            self.assertTrue(rules.sim_available(self.model, body, state))
            self.assertNotIn(row.STRAIN, state.flags)
            outcomes = walk(self, self.model, body, state)
            self.assertEqual(len(outcomes), 2)
            finished, aborted = outcomes
            self.assertEqual(aborted.flags, state.flags)
            self.assertEqual(aborted.rest_spent, state.rest_spent)
            self.assertTrue(rules.sim_available(self.model, body, aborted))
            self.assertIn(body["Id"] + ".seen", finished.flags)
            self.assertEqual(finished.rest_spent["household.pair"], 1)
            self.assertEqual(row.STRAIN in finished.flags, key == "seelah_aranka")
            for chapter in (3, 5):
                finished.chapter = chapter
                self.assertFalse(rules.sim_available(self.model, body, finished))

    def test_exact_favour_producers_exist_and_false_evidence_does_not_unlock(self):
        for key, outcome in row.FAVOURS.items():
            body = self.scenes[row.PREFIX + key]
            producers = [(s["Id"], n["Id"], i) for s in self.story["Scenes"]
                         for n in s["Nodes"] for i, c in enumerate(n["Choices"])
                         if outcome in c["Set"]]
            self.assertTrue(producers, outcome)
            self.assertNotIn(outcome, self.story.get("Derived", {}))
            for substitute in ("aranka.extension_kept", "aranka.trickster.cost.round_bought",
                               "aranka.trickster.round_kept", "seelah.committed", "seelah.kissed",
                               "seelah.rescued", "wenduag.romance_finished.latched"):
                with self.subTest(key=key, substitute=substitute):
                    state = self.state_for(body)
                    state.flags.remove(outcome)
                    state.flags.add(substitute)
                    self.assertFalse(rules.sim_available(self.model, body, state))

    def test_path_page_eligibility_and_body_are_separate_from_favour(self):
        for body in self.scenes.values():
            woman = body["ParticipantWomen"][0]
            seat = self.story["SeatWomen"][woman]
            for missing in ("trickster", "foresight.page_taken", "household.table.kept",
                            "household.stance_eligible", woman + ".harem.eligible", *seat["Requires"]):
                state = self.state_for(body)
                state.flags.discard(missing)
                # Remove all eligible derivation inputs as well, to model no partnership.
                if missing == woman + ".harem.eligible":
                    for group in self.model.composites[missing]:
                        state.flags.difference_update(group)
                self.assertFalse(rules.sim_available(self.model, body, state), missing)
            for loss in (woman + ".closed", woman + ".epoch_unavailable",
                         "fool_king.gone", "trickster.failed"):
                state = self.state_for(body)
                state.flags.update([loss, woman + ".trickster.returned", "nenio.life.recreated"])
                self.assertFalse(rules.sim_available(self.model, body, state), loss)
            for loss in seat["UnavailableFlags"]:
                state = self.state_for(body)
                state.flags.add(loss)
                self.assertFalse(rules.sim_available(self.model, body, state), loss)
            for chapter in (2, 4, 6):
                state = self.state_for(body)
                state.chapter = chapter
                self.assertFalse(rules.sim_available(self.model, body, state))

    def test_discussed_woman_is_never_an_attendee_or_gate(self):
        for key, target in (("seelah_aranka", "aranka"), ("nenio_seelah", "seelah")):
            body = self.scenes[row.PREFIX + key]
            self.assertNotIn(target, body["Participants"])
            self.assertNotIn(target, body["ParticipantWomen"])
            state = self.state_for(body)
            state.flags.update([target + ".closed", target + ".epoch_unavailable"])
            self.assertTrue(rules.sim_available(self.model, body, state))

    def test_indifferent_never_strains_and_no_other_household_states_are_written(self):
        for key, body in self.scenes.items():
            effects = [f for n in body["Nodes"] for c in n["Choices"] for f in c["Set"]]
            expected = [key + ".seen"] + ([row.STRAIN] if key.endswith("seelah_aranka") else [])
            self.assertEqual(effects, expected)
            self.assertTrue(all(not n.get("Paragraphs") and n["Choices"] for n in body["Nodes"]))
            self.assertFalse(any("explicit" in n["Id"] for n in body["Nodes"]))
            self.assertEqual(body["Participants"], body["ParticipantWomen"])
            self.assertEqual(body["Relationship"], "household")
            self.assertFalse(body.get("Remote"))

    def test_existing_allowance_and_dynamic_cap_apply(self):
        for body in self.scenes.values():
            self.assertEqual(body["HouseholdCategory"], "dynamic")
            self.assertFalse(body.get("HouseholdArcStart"))
            state = self.state_for(body)
            state.rest_spent["household.pair"] = 1
            self.assertFalse(rules.sim_available(self.model, body, state))
            state = self.state_for(body)
            state.chapter = 5
            cap = "household.cap.ch5.dynamic"
            self.assertIn(cap, body["Forbids"])
            others = [source for source in self.story["Counts"][cap]["Of"]
                      if source != body["HouseholdWitness"]]
            for source in others[:3]:
                state.flags.add(source)
            self.assertEqual(self.story["Counts"][cap]["Min"], 3)
            self.assertNotIn(body["HouseholdWitness"], state.flags)
            # Availability reads the cap derived by Rules.Complete, as it reads
            # the explicitly supplied current body and eligibility composites.
            state.flags.add(cap)
            self.assertFalse(rules.sim_available(self.model, body, state))

    def test_append_only_idempotent_and_missing_body_fails_before_mutation(self):
        payload = copy.deepcopy(self.story)
        original = copy.deepcopy(payload)
        row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, original)
        payload["Scenes"] = [s for s in payload["Scenes"] if not s["Id"].startswith(row.PREFIX)]
        before = copy.deepcopy(payload["Scenes"])
        row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(before, payload["Scenes"][:-2])
        self.assertEqual(savecompat.check(payload), [])
        payload["Scenes"] = before
        del payload["SeatWomen"]["nenio"]
        original = copy.deepcopy(payload)
        with self.assertRaisesRegex(ValueError, "bodily SeatWomen"):
            row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(original, payload)

    def test_utf8_and_lf_for_new_files(self):
        root = Path(__file__).resolve().parents[1]
        for name in ("storylines/harem_rows/household_knowledge.py",
                     "tests/test_harem_row_household_knowledge.py",
                     "tools/route_packs/harem/household-knowledge.md"):
            raw = (root / name).read_bytes()
            self.assertNotIn(b"\r", raw)
            self.assertNotIn("\ufffd", raw.decode("utf-8"))

    def test_smoothing_inventory_accepts_only_declared_visible_knowledge(self):
        from tools import harem_smoothing_lint as lint
        payload = dict(Scenes=list(self.scenes.values()), SeatWomen=self.story["SeatWomen"])

        def unclassified(story):
            return bool(lint.RESERVED_IN_STORY.search(lint.knowledge_inventory(json.dumps(story))))

        self.assertFalse(unclassified(payload))
        for missing in ("aranka.trickster.night_kept", "foresight.page_taken", "seelah.present_now"):
            bad = copy.deepcopy(payload)
            bad["Scenes"][0]["Requires"].remove(missing)
            self.assertTrue(unclassified(bad), missing)
        bad = copy.deepcopy(payload)
        bad["Scenes"][1]["Nodes"][1]["Choices"][0]["Set"].append(row.STRAIN)
        self.assertTrue(unclassified(bad), "indifferent second producer")
        bad = copy.deepcopy(payload)
        bad["Scenes"][0]["Nodes"][0]["Choices"][0]["Set"].append(row.STRAIN)
        self.assertTrue(unclassified(bad), "hidden intermediate producer")
        for unknown in (row.STRAIN + ".extra", "nenio.harem.strain.seelah.1",
                        "seelah.harem.mend.aranka.1", "household.smooth.seelah.1.a"):
            bad = copy.deepcopy(payload)
            bad["Scenes"][0]["Nodes"][1]["Choices"][0]["Set"].append(unknown)
            self.assertTrue(unclassified(bad), unknown)


if __name__ == "__main__":
    unittest.main()
