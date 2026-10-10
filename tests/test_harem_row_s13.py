"""S13 current-presence, deed clocks, bilateral answers and retired-slot walks."""
import copy
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from storylines.harem_rows import s13
from tools import rrt_verify as rules, savecompat, harem_schedule_lint, player_text_lint


class S13Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.rows = {s["Id"].removeprefix(s13.P): s for s in cls.model.scenes if s["Id"].startswith(s13.P)}

    def state(self):
        state = rules.SimState(5, 1000)
        state.flags.update(("trickster", "availability.observed", "household.table.kept",
                            "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "nenio.committed", "nenio.in_party", "nenio.trickster.first_night",
                            "nenio.trickster.test_running", "nenio.trickster.cost.name_filed",
                            "arueshalae.committed", "arueshalae.trickster.terms",
                            "arueshalae.recruited_drezen", "arueshalae.native_alive", "arueshalae.elysium"))
        rules.sim_complete(self.model, state)
        return state

    def finish(self, state, step, node):
        answer = select_answer(next(n for n in self.rows[step]["Nodes"] if n["Id"] == node)["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
        state.flags.update(answer["Set"])
        state.times.update({key: state.hour for key in answer["Set"]})
        rules.sim_complete(self.model, state)

    def playable_copy(self, step):
        """Test reserved content without removing the shipping retirement gate."""
        body = copy.deepcopy(self.rows[step])
        if step != "ack":
            body["Forbids"].remove(s13.P + "ack.heard")
        return body

    def test_ack_is_playable_and_refusal_is_authored(self):
        state = self.state()
        self.assertTrue(rules.sim_available(self.model, self.rows["ack"], state))
        outcomes = walk(self, self.model, self.rows["ack"], state)
        complete = [s for s in outcomes if s13.REFUSED in s.flags]
        _single_result, = complete
        self.assertIn(s13.P + "ack.heard", complete[0].flags)
        self.assertNotIn(s13.P + "nenio.friend", complete[0].flags)
        self.assertNotIn(s13.REFUSED, self.story.get("SeenCues", {}))
        self.assertFalse(rules.sim_available(self.model, self.rows["ack"], complete[0]))
        self.assertTrue(any(s.flags == state.flags for s in outcomes))

    def test_every_surface_requires_page_live_path_actual_bodies_and_current_routes(self):
        body = self.rows["ack"]
        for removed in ("trickster", "trickster.foresight.accepted", "nenio.in_party",
                        "arueshalae.native_alive", "arueshalae.recruited_drezen"):
            state = self.state()
            state.flags.discard(removed)
            rules.sim_complete(self.model, state)
            self.assertFalse(rules.sim_available(self.model, body, state), removed)
        for loss in s13.EXCLUDED:
            state = self.state()
            state.flags.update((loss, "nenio.trickster.returned", "arueshalae.trickster.returned"))
            rules.sim_complete(self.model, state)
            # Explicit computed guard fixture: model completion recalculates
            # epochs/personality from observations, rather than accepting inputs.
            state.flags.add(loss)
            self.assertFalse(rules.sim_available(self.model, body, state), loss)
        for step, scene in self.rows.items():
            self.assertEqual(scene["ParticipantWomen"], list(s13.PAIR))
            self.assertTrue(set(s13.COMMON) <= set(scene["Requires"]), step)
            self.assertIn("foresight.page_taken", scene["Requires"])
            self.assertFalse(any(n.get("Paragraphs") for n in scene["Nodes"]))
        for chapter in (2, 4, 6):
            state = self.state()
            state.chapter = chapter
            self.assertFalse(rules.sim_available(self.model, body, state))
        state = self.state()
        state.chapter = 3
        self.assertTrue(rules.sim_available(self.model, body, state))

    def test_budget_retirement_preserves_all_four_steps(self):
        state = self.state()
        self.finish(state, "ack", "heard")
        for step in ("company", "desire", "choice", "choice.warded", "morning"):
            body = self.rows[step]
            self.assertIn(s13.P + "ack.heard", body["Requires"])
            self.assertIn(s13.P + "ack.heard", body["Forbids"])
            self.assertFalse(rules.sim_available(self.model, body, state))
            self.assertTrue(body["ManualOnly"])
            self.assertFalse(body.get("InteractionHub"))
        self.assertEqual([s for s, b in self.rows.items() if b["HouseholdArcStart"]], ["company"])
        self.assertEqual([self.rows[s]["DelayHours"] for s in ("company", "desire", "choice", "morning")], [0, 48, 48, 8])

    def test_release_and_personality_are_independent_and_start_caps_do_not_gate_continuation(self):
        state = self.state()
        self.finish(state, "ack", "heard")
        self.finish(state, "company", "kept")
        self.finish(state, "desire", "named")
        state.flags.discard("arueshalae.changed")
        state.flags.discard("arueshalae.elysium")
        rules.sim_complete(self.model, state)
        state.flags.update(("nenio.harem.attitude.arueshalae.friend", "arueshalae.harem.attitude.nenio.friend"))
        state.hour += 48
        self.assertIn("arueshalae.redeemed", state.flags)
        self.assertFalse(rules.sim_available(self.model, self.playable_copy("choice"), state))
        self.assertTrue(rules.sim_available(self.model, self.playable_copy("choice.warded"), state))
        for step in ("desire", "choice", "choice.warded", "morning"):
            self.assertFalse(any("household.cap." in f for f in self.rows[step]["Forbids"]), step)

    def test_each_local_stage_requires_earned_deeds_and_contact_safety(self):
        derived = {k: v for k, v in self.story["Derived"].items()
                   if k.startswith(s13.P) and k.endswith((".friend", ".lover"))}
        model = rules.Model(dict(Scenes=[], Derived=derived,
                                DerivedForbids={k: ["arueshalae.corrupted"] for k in derived}))
        for key, groups in derived.items():
            for group in groups:
                full = rules.SimState(5, 1000)
                full.flags.update(group)
                rules.sim_complete(model, full)
                self.assertIn(key, full.flags)
                for missing in group:
                    state = rules.SimState(5, 1000)
                    state.flags.update(set(group) - {missing})
                    rules.sim_complete(model, state)
                    self.assertNotIn(key, state.flags, (key, missing))
                full.flags.add("arueshalae.corrupted")
                rules.sim_complete(model, full)
                self.assertNotIn(key, full.flags)

    def test_chronological_deeds_clocks_and_allowances(self):
        state = self.state()
        self.finish(state, "ack", "heard")
        self.assertTrue(rules.sim_available(self.model, self.playable_copy("company"), state))
        self.finish(state, "company", "kept")
        state.hour += 47
        self.assertFalse(rules.sim_available(self.model, self.playable_copy("desire"), state))
        state.hour += 1
        self.assertTrue(rules.sim_available(self.model, self.playable_copy("desire"), state))
        self.finish(state, "desire", "named")
        state.flags.update(("nenio.harem.attitude.arueshalae.friend", "arueshalae.harem.attitude.nenio.friend"))
        state.hour += 48
        self.assertTrue(rules.sim_available(self.model, self.playable_copy("choice"), state))
        for woman in s13.PAIR:
            self.assertIn(s13.P + woman + ".friend", state.flags)
            self.assertNotIn(s13.P + woman + ".lover", state.flags)
        self.finish(state, "choice", "kept_safe")
        state.hour += 7
        self.assertFalse(rules.sim_available(self.model, self.playable_copy("morning"), state))
        state.hour += 1
        self.assertTrue(rules.sim_available(self.model, self.playable_copy("morning"), state))
        state.rest_spent["household.pair"] = 1
        self.assertFalse(rules.sim_available(self.model, self.playable_copy("morning"), state))
        state = self.state()
        state.rest_spent["household.protected"] = 2
        self.assertFalse(rules.sim_available(self.model, self.rows["ack"], state))

    def test_ward_is_consumed_after_both_answers_with_selectable_fallback(self):
        scene = self.rows["choice.warded"]
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        self.assertEqual(select_answer(nodes["start"]["Choices"], (('nenio_yes', False, None, None, ('arueshalae.ward_held',), ()),), expected_position=0)["Next"], "nenio_yes")
        self.assertEqual(select_answer(nodes["nenio_yes"]["Choices"], (('arueshalae_yes', False, None, None, (), ()),), expected_position=0)["Next"], "arueshalae_yes")
        self.assertEqual(select_answer(nodes["arueshalae_yes"]["Choices"], (('ward_application', False, None, None, (), ()),), expected_position=0)["Next"], "ward_application")
        costs = [(n["Id"], c) for n in scene["Nodes"] for c in n["Choices"] if c.get("RemoveItem")]
        _single_result, = costs
        cost_node, cost_answer = _single_result
        self.assertEqual(cost_node, "ward_application")
        self.assertEqual(cost_answer["RemoveItem"], s13.SCROLL)
        for held in (False, True):
            state = self.state()
            if held:
                state.flags.add("arueshalae.ward_held")
            outcomes = walk(self, self.model, scene, state)
            yes = [s for s in outcomes if s13.P + "choice.both_yes" in s.flags]
            self.assertEqual(bool(yes), held)
            self.assertTrue(all(s13.P + "choice.ward_spent" in s.flags for s in yes))
        # Inventory disappears after agreeing: ward_application still has an exit.
        state = self.state()
        self.assertIn(contract_identities([c for c in nodes['ward_application']['Choices'] if rules.sim_choice_available(c, state)]), {1: ((('declined', None, None, False, (), ()),),)}[1])

    def test_slot_empty_filled_flow_and_refusal_outcomes(self):
        for step, body in self.rows.items():
            state = self.state()
            state.flags.add("arueshalae.ward_held")
            original = walk(self, self.model, body, state)
            filled = copy.deepcopy(body)
            for node in filled["Nodes"]:
                if node["Id"] == s13.P + "choice.explicit.1":
                    self.assertEqual(select_answer(node["Choices"], (('kept_safe', False, None, None, (), ()), ('kept_warded', False, None, None, (), ())), expected_position=0)["Set"], [])
                    node["Text"] = "User supplied interval."
            self.assertEqual([s.flags for s in original], [s.flags for s in walk(self, self.model, filled, state)])
            if step not in ("ack", "morning"):
                declined = [s for s in original if s13.P + "arc.declined" in s.flags]
                self.assertTrue(declined, step)
                self.assertTrue(all(s13.P + "choice.both_yes" not in s.flags for s in declined))

    def test_registration_savecompat_and_surface_inventory(self):
        story = copy.deepcopy(self.story)
        s13.register(story, story["Scenes"], story["Etudes"])
        self.assertEqual(story, self.story)
        self.assertEqual(savecompat.check(story), [])
        self.assertEqual(player_text_lint.check({"Scenes": list(self.rows.values())})["review"], [])
        for body in self.rows.values():
            self.assertEqual(harem_schedule_lint.delayed_clock_errors(body, story), [])
            self.assertEqual(story["ForesightConsumers"][body["Id"]], "foresight.page_taken")
        data = json.loads((Path(__file__).resolve().parents[1] / "tools/route_packs/harem/s13-contract.json").read_text(encoding="utf-8"))
        self.assertEqual(data["scenes"], [b["Id"] for b in self.rows.values()])
        self.assertEqual(data["history_books"], [])
        writes = {f for b in self.rows.values() for n in b["Nodes"] for c in n["Choices"] for f in c["Set"]}
        self.assertTrue(all(f.startswith(s13.P) or f == s13.REFUSED for f in writes))
        self.assertFalse(writes.intersection(story["Derived"]))




def answer_key(answer):
    """Identify an answer by its destination/check and gates, never localization."""
    check = answer.get('Check') or {}
    return (answer.get('Next'), answer.get('Abort', False),
            check.get('Success'), check.get('Failure'),
            tuple(answer.get('Requires', ())), tuple(answer.get('Forbids', ())))


def select_answer(answers, keys, expected_position=None):
    # A destination is independent of its availability gates. Gates disambiguate
    # parallel answers that intentionally share a destination.
    matching = [answer for answer in answers if answer_key(answer)[:4] in {key[:4] for key in keys}]
    try:
        answer, = matching
    except ValueError:
        matching = [answer for answer in answers if answer_key(answer) in keys]
        try:
            answer, = matching
        except ValueError as error:
            raise AssertionError(('missing or ambiguous answer', keys,
                                  tuple(answer_key(answer) for answer in answers))) from error
    if expected_position is not None:
        # Save addresses retain answer order even when prose or gates change.
        slot = expected_position if expected_position >= 0 else len(answers) + expected_position
        saved_answer = next(candidate for position, candidate in enumerate(answers) if position == slot)
        if saved_answer is not answer:
            raise AssertionError(('saved answer order changed', keys, expected_position))
    return answer

def contract_identity(value):
    """Project saved identities and gates; paragraph wording is irrelevant."""
    if isinstance(value, dict):
        if 'Id' in value:
            return value['Id']
        check = value.get('Check') or {}
        return (value.get('Next'), check.get('Success'), check.get('Failure'),
                value.get('Abort', False), tuple(value.get('Requires', ())),
                tuple(value.get('Forbids', ())))
    if hasattr(value, 'flags'):
        return tuple(sorted(flag for flag in value.flags if flag.startswith('household.')))
    if isinstance(value, (tuple, list)):
        return tuple(contract_identity(item) for item in value)
    return value


def contract_identities(values):
    return tuple(contract_identity(value) for value in values)


if __name__ == "__main__":
    unittest.main()
