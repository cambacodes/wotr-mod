"""S48 graphs against the actual integration export; no shared registrations."""
import copy
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from tests.story_fixture import row_registration_fixture

from storylines.harem_rows import s48
from tools import rrt_verify as rules
from tools.harem_schedule_lint import delayed_clock_errors
from tools.savecompat import check as savecompat

ROOT = Path(__file__).resolve().parents[1]


def registered():
    return row_registration_fixture(s48)


class S48Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = registered()
        cls.rows = [rules.norm_scene(s) for s in cls.payload["Scenes"] if s["Id"].startswith(s48.P)]
        cls.by = {s["Id"]: s for s in cls.rows}

    def test_savecompat_and_body_attachment(self):
        self.assertEqual(savecompat(self.payload), [])
        self.assertIn(contract_identities(self.rows),
                {15: (('household.pair.herrax_minagho.notice',
                       'household.pair.herrax_minagho.notice.unfinished',
                       'household.pair.herrax_minagho.notice.historical',
                       'household.pair.herrax_minagho.reply',
                       'household.pair.herrax_minagho.retry',
                       'household.pair.herrax_minagho.retry.debt',
                       'household.pair.herrax_minagho.notice.minagho',
                       'household.pair.herrax_minagho.notice.minagho.unfinished',
                       'household.pair.herrax_minagho.notice.historical.minagho',
                       'household.pair.herrax_minagho.reply.minagho',
                       'household.pair.herrax_minagho.retry.minagho',
                       'household.pair.herrax_minagho.retry.minagho.debt',
                       'household.pair.herrax_minagho.reply.table',
                       'household.pair.herrax_minagho.retry.table',
                       'household.pair.herrax_minagho.retry.table.debt'),)}[15])
        ids = [s["Id"] for s in self.rows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(self.by), set(ids))
        for body in self.rows:
            self.assertEqual(body["Relationship"], "household")
            self.assertEqual(body["Chapters"], [5])
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertEqual(body["ParticipantWomen"], ["minagho"])
            if body["InteractionHub"] != "household.table":
                self.assertTrue(rules.household_presence_attachment(self.payload, body), body["Id"])
                self.assertNotIn("foresight.page_taken", body["Requires"])
                self.assertNotIn(s48.P + "minagho_eligible", body["Requires"])

    def test_clocks_abort_witnesses_and_no_attitude_writes(self):
        for body in self.rows:
            self.assertEqual(delayed_clock_errors(body, self.payload), [])
            root = body["Nodes"][0]
            self.assertTrue(select_answer(root["Choices"], ((None, True, None, None, (), ()),), expected_position=-1)["Abort"])
            for node in body["Nodes"]:
                self.assertTrue(without_prose(node["Choices"]), (body["Id"], node["Id"]))
                # Funds can hide a paid option; every page still has an
                # unconditional answer in all histories (including zero funds).
                self.assertTrue(any(not answer["Requires"] and not answer["Forbids"]
                                    and not answer.get("Crusade") for answer in without_prose(node["Choices"])))
                self.assertFalse(node.get("Paragraphs"))
                for choice in without_prose(node["Choices"]):
                    if choice["Abort"]:
                        self.assertFalse(choice["Next"])
                        self.assertFalse(choice["Set"])
                        self.assertFalse(choice.get("Crusade"))
                    for key in choice["Set"]:
                        self.assertNotIn(key, self.payload["Derived"])
                        self.assertFalse(any(word in key for word in (".enmity.", ".reconciled.", ".stance.")))
                    if choice.get("Check"):
                        self.assertEqual(choice["Check"]["DC"], 22)
                        self.assertTrue(choice["Check"]["CommanderOnly"])
                        self.assertFalse(choice["Set"])

    def test_terminal_matrix_and_wrapper_equivalence(self):
        for step in ("reply", "retry"):
            base = self.by[s48.P + step]
            for suffix in (".minagho", ".table"):
                self.assertEqual(without_prose(base["Nodes"]), without_prose(self.by[s48.P + step + suffix]["Nodes"]))
            roots = without_prose(base["Nodes"])[0]["Choices"]
            paid = ordered_answer(roots, 1 if step == "reply" else 0,
                    (((None, False, 'exchanged', 'failed', (), ()),
                      (None, False, None, None, (), ()),
                      ('refused', False, None, None, (), ()),
                      (None, True, None, None, (), ())),
                     ((None, False, None, None, (), ()),
                      ('refused', False, None, None, (), ()),
                      (None, True, None, None, (), ()))))
            self.assertEqual(paid["Set"], list(s48.success(step, True)))
            self.assertEqual(paid["Crusade"], dict(Resource="Finances", Amount=-200 if step == "reply" else -300))
            for node in without_prose(base["Nodes"]):
                if node["Id"] in ("failed", "refused"):
                    for choice in without_prose(node["Choices"]):
                        self.assertNotIn(s48.P + "settled", choice["Set"])
                        self.assertNotIn(s48.P + "herrax_order_withdrawn", choice["Set"])
            if step == "retry":
                self.assertIn([s48.P + "reply.failed", s48.P + "reply.refused"], base["RequiresAnyGroups"])
                self.assertIn(s48.P + "retry.seen", base["Forbids"])

    def test_target_is_current_qualified_and_history_cannot_settle(self):
        self.assertEqual(self.payload["Derived"][s48.P + "target_current"],
                         [["participant.chivarro.available", "chivarro.present_now"]])
        self.assertIn(s48.MC + "chivarro_sent_back", self.payload["DerivedForbids"][s48.P + "target_current"])
        for body in self.rows:
            self.assertNotIn("minagho_chivarro.harem.eligible", body["Requires"])
            self.assertNotIn("chivarro.dead", body["Forbids"])
            if ".historical" in body["Id"]:
                self.assertIn(s48.P + "target_current", body["Forbids"])
                choices = body["Nodes"][0]["Choices"]
                self.assertEqual(select_answer(choices, ((None, False, None, None, (), ()),), expected_position=0)["Set"], list(s48.flags("notice.seen", "notice.historical", "target_unprotected")))
                self.assertIn(contract_identities(choices), {2: (((None, None, None, False, (), ()), (None, None, None, True, (), ())),)}[2])

    def test_page_table_enmity_and_respect_ceiling(self):
        for body in self.rows:
            if body["InteractionHub"] == "household.table":
                self.assertIn("foresight.page_taken", body["Requires"])
                self.assertIn("household.table.kept", body["Requires"])
                for edge, override in s48.EDGES.items():
                    self.assertIn(edge, body["Forbids"])
                    self.assertEqual(body["ForbidOverrides"][edge], override)
            else:
                self.assertFalse(set(s48.EDGES).intersection(body["Forbids"]))
        self.assertFalse(any("explicit" in body["Id"] for body in self.rows))
        for key in ("herrax.harem.attitude.w.minagho.respect", "minagho_chivarro.harem.attitude.minagho.herrax.respect"):
            self.assertIn(s48.P + "settled", self.payload["Derived"][key][0])

    def live_state(self, body):
        model = rules.Model(dict(self.payload, Scenes=self.rows))
        state = rules.SimState(5, 100)
        state.flags.update(body["Requires"])
        state.flags.add("trickster.ever")
        state.flags.update(group[0] for group in body["RequiresAnyGroups"])
        state.flags.add("herrax.harem.eligible")
        state.flags.update(model.composites["minagho_chivarro.harem.eligible"][0])
        seat = self.payload["SeatWomen"]["minagho"]
        state.flags.update(seat["Requires"])
        return model, state

    def test_live_page_closure_enmity_and_shared_step_clock(self):
        body = self.by[s48.P + "reply.table"]
        model, state = self.live_state(body)
        state.times[s48.P + "notice.sent"] = 53
        self.assertFalse(rules.sim_available(model, body, state))
        state.hour = 101
        self.assertTrue(rules.sim_available(model, body, state))
        for gate in ("foresight.page_taken", "trickster", "minagho.present_now", s48.P + "herrax_channel", s48.P + "target_current"):
            absent = copy.deepcopy(state)
            absent.flags.remove(gate)
            self.assertFalse(rules.sim_available(model, body, absent), gate)
        for closed in ("herrax.closed", "minachiv.closed", "minagho.epoch_unavailable"):
            absent = copy.deepcopy(state)
            absent.flags.add(closed)
            self.assertFalse(rules.sim_available(model, body, absent), closed)
        for edge, reconciled in s48.EDGES.items():
            hostile = copy.deepcopy(state)
            hostile.flags.add(edge)
            self.assertFalse(rules.sim_available(model, body, hostile))
            hostile.flags.add(reconciled)
            self.assertTrue(rules.sim_available(model, body, hostile))
        done = copy.deepcopy(state)
        done.flags.add(s48.P + "reply.seen")
        for suffix in ("", ".minagho", ".table"):
            self.assertFalse(rules.sim_available(model, self.by[s48.P + "reply" + suffix], done))

    def test_history_survives_absent_correspondent_and_private_runtime_blocker(self):
        body = self.by[s48.P + "notice.historical"]
        model, state = self.live_state(body)
        state.flags.add("herrax.closed")
        self.assertTrue(rules.sim_available(model, body, state))
        state.flags.add(s48.P + "target_current")
        self.assertFalse(rules.sim_available(model, body, state))
        # Document the existing shared bug instead of falsely certifying the
        # sheet's no-romance private channel: ParticipantsAvailable requires it.
        private = self.by[s48.P + "notice"]
        model, state = self.live_state(private)
        self.assertTrue(rules.sim_available(model, private, state))
        state.flags.remove("herrax.harem.eligible")
        self.assertFalse(rules.sim_available(model, private, state))

    def test_later_losses_withhold_current_target_even_after_earlier_return(self):
        model = rules.Model(dict(self.payload, Scenes=self.rows))
        for loss in ("chivarro.epoch_unavailable", s48.MC + "chivarro_walked", "chivarro.returned_actor_lost",
                     s48.MC + "chivarro_sent_back", s48.MC + "chivarro_declined", "minachiv.closed"):
            state = rules.SimState(5, 100)
            # Actual earned reunion/return, but a newer native loss wins.
            state.flags.update({"availability.observed", "trickster", s48.MC + "returned_chivarro",
                                s48.MC + "chivarro_in", "chivarro.dead", loss})
            rules.sim_complete(model, state)
            self.assertNotIn(s48.P + "target_current", state.flags, loss)

    def test_actual_paid_answers_recheck_and_share_completion(self):
        # Isolate the engine transaction from the separately escalated private
        # Participants eligibility defect; these are the actual row answers.
        for step, index, price in (("reply", 1, 200), ("retry", 0, 300)):
            body = copy.deepcopy(self.by[s48.P + step + ".table"])
            body.update(Participants=[], ParticipantWomen=[], Requires=[], RequiresAnyGroups=[],
                        Forbids=[s48.P + step + ".seen"])
            model = rules.Model(dict(Scenes=[body], Relationships={"household": self.payload["Relationships"]["household"]},
                                     RestAllowances=self.payload["RestAllowances"]))
            answer = ordered_answer(body["Nodes"][0]["Choices"], index,
                    (((None, False, 'exchanged', 'failed', (), ()),
                      (None, False, None, None, (), ()),
                      ('refused', False, None, None, (), ()),
                      (None, True, None, None, (), ())),
                     ((None, False, None, None, (), ()),
                      ('refused', False, None, None, (), ()),
                      (None, True, None, None, (), ()))))
            for balance in (None, 0, price - 1, price, price + 19):
                state = rules.SimState(5, 100)
                state.crusade_resources = None if balance is None else {"Finances": balance}
                before = copy.deepcopy(state.__dict__)
                def publish():
                    state.flags.update(answer["Set"] + [body["Id"]])
                    state.rest_spent["household.protected"] = 1
                expected = balance is not None and balance >= price
                self.assertEqual(rules.sim_paid_choice(model, body, answer, state, publish), expected)
                if expected:
                    self.assertEqual(state.crusade_resources["Finances"], balance - price)
                    self.assertEqual(state.rest_spent["household.protected"], 1)
                    loaded = copy.deepcopy(state)
                    body["Id"] = s48.P + step
                    self.assertFalse(rules.sim_paid_choice(model, body, answer, loaded, publish))
                else:
                    self.assertEqual(state.__dict__, before)




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




def ordered_answer(answers, ordinal, expected_orders):
    """Protect answer order, then select its declared structural destination."""
    actual = tuple(answer_key(answer) for answer in answers)
    if actual not in expected_orders:
        raise AssertionError(('answer order/gates changed', actual, expected_orders))
    for order in expected_orders:
        if order == actual:
            key = next(key for order_index, key in enumerate(order) if order_index == ordinal)
            return select_answer(answers, (key,))
    raise AssertionError('missing declared answer order')

if __name__ == "__main__":
    unittest.main()
