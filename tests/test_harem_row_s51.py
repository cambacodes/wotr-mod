"""S51 graphs, witnesses, clocks, current channels and known shared blockers."""
import copy
import unittest
from tests.story_fixture import fresh_story

import json
from pathlib import Path
from storylines.harem_rows import s51
from storylines import contract_j01
from tools import rrt_verify as rules, savecompat
from tools.harem_schedule_lint import delayed_clock_errors


class WindstepDocket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)
        cls.payload = copy.deepcopy(cls.base)
        s51.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        contract_j01.install(cls.payload)
        cls.model = rules.Model(cls.payload)
        cls.rows = {s["Id"][len(s51.P):]: s for s in cls.model.scenes if s["Id"].startswith(s51.P)}

    def state(self, body="widow", hour=100):
        state = rules.SimState(5, hour)
        state.flags.update(("trickster", "trickster.now", "nidalynn.trickster.met",
                            "availability.observed", "chapter_later",
                            "nidalynn.trickster.hearth.grey_stone" if body == "widow" else "nidalynn.trickster.form_chosen"))
        rules.sim_complete(self.model, state)
        state.available_contacts = {p["Unit"] for k, p in self.payload["Presences"].items()
                                    if k.startswith("nidalynn.presence")}
        return state

    def graph_play(self, name, state, choices, check_success=True):
        """Exercise the real graph without manufacturing romance to satisfy Participants.

        Availability is checked separately, including the documented engine blocker.
        sim_play supplies publication, timestamps, completion and allowance behavior.
        """
        scene = self.rows[name]
        by_id = {n["Id"]: n for n in scene["Nodes"]}
        node = by_id["start"]
        path = []
        for index in choices:
            answer = node["Choices"][index]
            self.assertTrue(rules.sim_choice_available(answer, state))
            path.append(answer)
            if answer.get("Check"):
                target = answer["Check"]["Success" if check_success else "Failure"]
            else:
                target = answer["Next"]
            if target is not None:
                node = by_id[target]
        return rules.sim_play(self.model, scene, state, (), plan=(0, path))

    def physical_available(self, name, state):
        return rules.sim_available(self.model, self.rows[name], state)

    def test_registration_has_exact_graphs_and_no_existing_identity_changes(self):
        self.assertEqual(set(self.rows), {"notice.widow", "notice.chosen", "cell",
                                         "retry.widow", "retry.chosen", "receipt.widow", "receipt.chosen"})
        self.assertEqual([], savecompat.check(self.payload, savecompat.inventory(self.base)))
        self.assertEqual([], rules.validate(self.model))
        for scene in self.rows.values():
            self.assertEqual(scene["Relationship"], "household")
            self.assertEqual(scene["Chapters"], [5])
            self.assertIn("trickster", scene["Requires"])
            self.assertEqual([], delayed_clock_errors(scene, self.payload))
            root = scene["Nodes"][0]["Choices"]
            self.assertTrue(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Abort"])
            self.assertFalse(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Set"])
            self.assertIsNone(select_answer(root, ((None, True, None, None, (), ()),), expected_position=-1)["Next"])
        self.assertEqual(self.rows["cell"]["AnswerLists"], [s51.ar.CELL_LIST])
        self.assertFalse(self.rows["cell"]["ReturnToList"])
        self.assertEqual(self.rows["cell"]["NativeReturnCue"], s51.CELL_ROOT)
        for node in self.rows["cell"]["Nodes"]:
            for choice in node["Choices"]:
                self.assertIsNone(choice.get("NativeNext"))
        self.assertFalse(self.rows["cell"]["Remote"])

    def test_both_direct_successes_wait_and_publish_only_on_terminal(self):
        for body in ("widow", "chosen"):
            for index in (0, 1):
                with self.subTest(body=body, index=index):
                    state = self.state(body)
                    self.graph_play("notice." + body, state, [0, 0])
                    self.assertNotIn("household.protected", state.rest_spent)
                    self.assertFalse(self.physical_available("cell", state))
                    state.hour += 48
                    self.assertTrue(self.physical_available("cell", state))
                    self.graph_play("cell", state, [index, 0])
                    self.assertEqual(state.rest_spent["household.protected"], 1)
                    self.assertNotIn(s51.P + "accounted", state.flags)
                    self.assertNotIn(s51.P + "chart.bundle_carried", state.flags)
                    self.assertFalse(self.physical_available("receipt." + body, state))
                    state.hour += 48
                    state.rest_spent.clear()
                    self.assertTrue(self.physical_available("receipt." + body, state))
                    self.graph_play("receipt." + body, state, [0, 0])
                    self.assertTrue(set(s51.flags("accounted", "no_absolution")) <= state.flags)
                    self.assertFalse(self.physical_available("receipt." + body, copy.deepcopy(state)))
                    self.assertFalse(self.physical_available("receipt." + ("chosen" if body == "widow" else "widow"), state))

    def test_carried_recoveries_do_not_need_areelu_and_have_their_own_receipt_clock(self):
        for body in ("widow", "chosen"):
            for index in (0, 2):
                with self.subTest(body=body, index=index):
                    state = self.state(body)
                    self.graph_play("notice." + body, state, [0, 0])
                    state.hour += 48
                    self.graph_play("cell", state, [index, 0], check_success=False)
                    self.assertIn(s51.P + "chart.bundle_carried", state.flags)
                    self.assertNotIn(s51.P + "cell.chart_erased", state.flags)
                    self.assertFalse(self.physical_available("receipt." + body, state))
                    self.assertFalse(self.physical_available("retry." + body, state))
                    state.flags.add("areelu.closed")
                    state.hour += 48
                    state.rest_spent.clear()
                    self.assertTrue(self.physical_available("retry." + body, state))
                    self.graph_play("retry." + body, state, [0, 0])
                    self.assertIn(s51.BUNDLE_LOST, state.flags)
                    self.assertFalse(self.physical_available("retry." + body, state))
                    self.assertFalse(self.physical_available("receipt." + body, state))
                    state.hour += 48
                    state.rest_spent.clear()
                    self.assertTrue(self.physical_available("receipt." + body, state))
                    self.graph_play("receipt." + body, state, [0, 0])
                    self.assertIn(s51.P + "accounted", state.flags)
                    self.assertEqual(state.times[s51.P + "cell.chart_erased"], 196)

    def test_refusals_and_aborts_do_not_fabricate_erasure_or_pardon(self):
        state = self.state()
        self.graph_play("notice.widow", state, [1, 0])
        self.assertIn(s51.P + "unanswered", state.flags)
        self.assertFalse(self.physical_available("cell", state))
        for name, scene in self.rows.items():
            state = self.state("chosen" if name.endswith("chosen") else "widow")
            before = copy.deepcopy(state.__dict__)
            self.assertFalse(self.graph_play(name, state, [len(scene["Nodes"][0]["Choices"]) - 1]))
            # sim_play may mark household.started when opening; Abort publishes
            # no row outcome, completion or allowance, as required by runtime.
            self.assertEqual({key for key in state.flags if key.startswith(s51.P)},
                             {key for key in before["flags"] if key.startswith(s51.P)})
            self.assertFalse(state.rest_spent)
            self.assertEqual(before["hour"], state.hour)
        for step in ("retry", "receipt"):
            state = self.state()
            self.graph_play(step + ".widow", state, [1, 0])
            self.assertIn(s51.P + "unanswered", state.flags)
            self.assertNotIn(s51.P + "accounted", state.flags)
        writes = {key for scene in self.rows.values() for node in scene["Nodes"]
                  for choice in node["Choices"] for key in choice["Set"]}
        self.assertTrue(all(key.startswith(s51.P) for key in writes))
        self.assertFalse(any(any(word in key for word in ("reconciled", "enmity", "committed", "stance")) for key in writes))

    def test_current_channels_loss_and_shared_body_witness(self):
        state = self.state()
        self.assertTrue(self.physical_available("notice.widow", state))
        self.assertFalse(self.physical_available("notice.chosen", state))
        for missing in ("trickster", "nidalynn.trickster.hearth.grey_stone", "nidalynn.trickster.met"):
            lost = copy.deepcopy(state)
            lost.flags.discard(missing)
            rules.sim_complete(self.model, lost)
            self.assertFalse(self.physical_available("notice.widow", lost))
        for loss in ("nidalynn.closed", "nidalynn.trickster.left_with_it", "nidalynn.epoch_unavailable"):
            lost = copy.deepcopy(state)
            lost.flags.add(loss)
            self.assertFalse(self.physical_available("notice.widow", lost))
        self.graph_play("notice.widow", state, [0, 0])
        state.hour += 48
        self.assertTrue(self.physical_available("cell", state))
        for loss in (s51.PROJECTOR_BROKEN, "areelu.closed", "areelu.epoch_unavailable", "areelu.incinerated"):
            lost = copy.deepcopy(state)
            lost.flags.add(loss)
            self.assertFalse(self.physical_available("cell", lost))
        state.flags.add("nidalynn.trickster.form_chosen")
        self.assertFalse(self.physical_available("notice.chosen", state))

    def test_independent_unromanced_discovery_with_table_closed(self):
        state = self.state()
        self.assertNotIn("foresight.page_taken", state.flags)
        self.assertNotIn("nidalynn.committed", state.flags)
        self.assertNotIn("nidalynn.harem.eligible", state.flags)
        state.flags.add("household.closed")
        self.assertTrue(rules.sim_available(self.model, self.rows["notice.widow"], state))
        self.assertTrue(self.physical_available("notice.widow", state))
        state.available_contacts.clear()
        self.assertFalse(self.physical_available("notice.widow", state))

    def test_readers_are_historical_or_existing_epilogue_pages(self):
        entry = next(e for e in self.payload["Books"]["trickster.ledger"]["Entries"] if e["Id"] == "seating.s51.windstep")
        self.assertEqual(entry["Requires"], list(s51.flags("notice.seen")))
        self.assertFalse(any("present" in key or "eligible" in key for key in entry["Requires"]))
        for host in self.model.scenes:
            for node in host["Nodes"]:
                for paragraph in node.get("Paragraphs", []):
                    if any(key.startswith(s51.P) for key in paragraph.get("Requires", [])):
                        self.assertTrue(rules.is_epilogue(host), host["Id"])
                        if s51.P + "accounted" in paragraph["Requires"]:
                            self.assertIn(s51.P + "no_absolution", paragraph["Requires"])
        for sid in ("areelu.trickster.wager.struck", "areelu.trickster.rivalry.lens"):
            host = self.model.by_id[sid]
            choice = select_answer(host["Nodes"][0]["Choices"],
                    (('s51_field_route',
                      False,
                      None,
                      None,
                      ('household.pair.nidalynn_areelu.cost.areelu_field_notes_lost',
                       'household.pair.nidalynn_areelu.cell.chart_erased'),
                      ()),), expected_position=-1)
            self.assertEqual(choice["Next"], "s51_field_route")
            self.assertEqual(set(choice["Requires"]), set(s51.flags("cost.areelu_field_notes_lost", "cell.chart_erased")))
            self.assertFalse(choice["Set"])




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

if __name__ == "__main__":
    unittest.main()
