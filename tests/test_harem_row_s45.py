"""S45 branch transactions, current contacts and append-only knowledge readers."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s45
from tools import rrt_verify, savecompat


class S45(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)
        cls.payload = copy.deepcopy(cls.base)
        s45.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.by = {s["Id"]: s for s in cls.payload["Scenes"]}
        cls.hearing = cls.by[s45.P + "hearing"]
        cls.nodes = {n["Id"]: n for n in cls.hearing["Nodes"]}

    def test_abort_and_every_preterminal_are_effect_free(self):
        for node in self.nodes.values():
            for answer in node["Choices"]:
                if answer["Abort"] or answer["Next"]:
                    self.assertEqual(answer["Set"], [])
                    self.assertFalse(any(k in answer for k in ("Crusade", "RemoveItem", "Revive", "StartEtude", "NativeNext", "Alignment")))
        for variant in ("informed", "concealed", "intimate"):
            for result in s45.outcomes():
                node = self.nodes[variant + "." + result]
                self.assertTrue(select_answer(node["Choices"], ((None, True, None, None, (), ()),), expected_position=1)["Abort"])
                expected = {s45.P + x for x in s45.outcomes()[result]}
                if variant != "informed":
                    expected.add(s45.LATER)
                self.assertEqual(set(select_answer(node["Choices"], ((None, False, None, None, ('household.pair.yaniel_minagho.respondent_current',), ()), (None, False, None, None, (), ())), expected_position=0)["Set"]), expected)
                self.assertNotIn(s45.TOLD, expected)
                self.assertNotIn(s45.SECRET, expected)

    def test_courier_never_earns_shared_attendance(self):
        for variant in ("informed", "concealed", "intimate"):
            choices = self.nodes[variant + ".claim.courier"]["Choices"]
            self.assertEqual([a["Next"] for a in choices[:2]], [variant + ".delivered"] * 2)
            self.assertNotIn(s45.P + "attendance_earned", select_answer(self.nodes[variant + ".delivered"]["Choices"], ((None, False, None, None, ('household.pair.yaniel_minagho.respondent_current',), ()),), expected_position=0)["Set"])

    def test_page_presence_epoch_and_singleton_contract(self):
        required = set(self.hearing["Requires"])
        self.assertTrue({"trickster", "foresight.page_taken", "yaniel.freed.latched", "yaniel.present_now", s45.Y + "returned"} <= required)
        self.assertFalse(any("minachiv" in x or "chivarro" in x for x in required))
        self.assertEqual(self.hearing["Participants"], [])
        self.assertEqual(self.hearing["RestAllowance"], "household.protected")
        self.assertEqual(self.hearing["Chapters"], [5])
        self.assertNotIn("Pair", self.hearing)
        self.assertNotIn("NativeReturnCue", self.hearing)
        self.assertIn("minagho.epoch_unavailable", self.payload["DerivedForbids"][s45.CONTACT])
        self.assertIn("participant.minagho.available", self.payload["Derived"][s45.CONTACT][0])
        for variant in ("informed", "concealed", "intimate"):
            for result in ("destroyed", "delivered"):
                self.assertIn(s45.CONTACT, select_answer(self.nodes[variant + "." + result]["Choices"], ((None, False, None, None, ('household.pair.yaniel_minagho.respondent_current',), ()),), expected_position=0)["Requires"])

    def test_knowledge_precedence_and_save_addresses(self):
        for scene in self.payload["Scenes"]:
            if not scene["Id"].startswith(s45.Y + "commit.trade"):
                continue
            old = next(s for s in self.base["Scenes"] if s["Id"] == scene["Id"])
            for before in old["Nodes"]:
                after = next(n for n in scene["Nodes"] if n["Id"] == before["Id"])
                for answer, successor in zip(before["Choices"], after["Choices"]):
                    self.assertEqual(answer["Next"], successor["Next"])
                    self.assertEqual(answer["Set"], successor["Set"])
                if [a["Next"] for a in before["Choices"][:3]] == ["told", "hid", "ask"]:
                    self.assertEqual(select_answer(after["Choices"],
                            (('household_minagho_told_later',
                              False,
                              None,
                              None,
                              ('household.pair.yaniel_minagho.truth_now_told',),
                              ('yaniel.trickster.minagho_told',)),), expected_position=3)["Next"], "household_minagho_told_later")
                    self.assertIn(s45.TOLD, select_answer(after["Choices"],
                            (('household_minagho_told_later',
                              False,
                              None,
                              None,
                              ('household.pair.yaniel_minagho.truth_now_told',),
                              ('yaniel.trickster.minagho_told',)),), expected_position=3)["Forbids"])
                    for answer in after["Choices"][1:3]:
                        self.assertIn(s45.LATER, answer["Forbids"])
        self.assertEqual(savecompat.check(self.payload), savecompat.check(self.base))

    def test_no_stance_reconciliation_or_intimate_slot(self):
        for node in self.nodes.values():
            for answer in node["Choices"]:
                self.assertTrue(all(flag.startswith(s45.P) for flag in answer["Set"]))
                self.assertFalse(any(word in flag for flag in answer["Set"] for word in ("reconciled", "committed", "enmity", "strain", "lust")))
        self.assertFalse(any("explicit" in n["Id"] for n in self.nodes.values()))

    def test_registration_is_idempotent(self):
        payload = copy.deepcopy(self.payload)
        s45.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(payload, self.payload)

    def test_runtime_contact_loss_and_protected_claimant(self):
        model = rrt_verify.Model(self.payload)
        flags = {"availability.observed", "trickster", "trickster.ever", "chapter_later",
                 "trickster.foresight.accepted", "household.table.kept", s45.Y + "returned",
                 "yaniel.freed.latched", s45.Y + "minagho_seen", s45.SECRET,
                 "minagho_chivarro.trickster.minagho_in"}
        def state(extra=(), remove=()):
            st = rrt_verify.SimState(5, 1000)
            st.flags.update(flags - set(remove))
            st.flags.update(extra)
            rrt_verify.sim_complete(model, st)
            return st
        current = state()
        self.assertIn(s45.CONTACT, current.flags)
        self.assertTrue(rrt_verify.sim_available(model, model.by_id[s45.P + "hearing"], current))
        for loss in ("minachiv.closed", "minagho.returned_actor_lost", "minagho.dead"):
            lost = state((loss,))
            self.assertNotIn(s45.CONTACT, lost.flags)
            self.assertTrue(rrt_verify.sim_available(model, model.by_id[s45.P + "hearing"], lost))
        returned_then_lost = state(("minagho.dead", "minagho_chivarro.trickster.returned_minagho", "minagho.returned_actor_lost"))
        self.assertNotIn(s45.CONTACT, returned_then_lost.flags)
        self.assertIn(s45.CONTACT, state(("chivarro.dead",)).flags)
        for lost_gate in ("trickster", "trickster.foresight.accepted", "yaniel.freed.latched"):
            self.assertFalse(rrt_verify.sim_available(model, model.by_id[s45.P + "hearing"], state(remove=(lost_gate,))))
        for loss in ("yaniel.closed", "yaniel.killed.latched", s45.Y + "left_free", s45.SEEN):
            self.assertFalse(rrt_verify.sim_available(model, model.by_id[s45.P + "hearing"], state((loss,))))

    def test_runtime_disclosure_priority(self):
        model = rrt_verify.Model(self.payload)
        for original, later, secret, favoured in ((True, True, True, False), (False, True, True, False),
                                                (False, False, True, False), (False, False, True, True)):
            st = rrt_verify.SimState(5, 1000)
            st.flags.update([k for k, held in ((s45.TOLD, original), (s45.LATER, later),
                                               (s45.SECRET, secret), (s45.INTIMATE, favoured)) if held])
            if original or later:
                st.flags.add(s45.KNOWN)
            active = [a["Next"] for a in self.nodes["start"]["Choices"] if not a["Abort"] and rrt_verify.sim_choice_available(a, st)]
            expected = "informed.start" if original or later else "intimate.start" if favoured else "concealed.start"
            self.assertEqual(active, [expected])




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
