"""S52's exact verdict, independent office audience and irreversible outcomes."""
import copy
import json
from pathlib import Path
import unittest
from tests.story_fixture import fresh_story

from storylines.harem_rows import s52
from tools import rrt_verify as rules, savecompat
from tools.harem_schedule_lint import delayed_clock_errors

ROOT = Path(__file__).resolve().parents[1]


class RowS52(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = fresh_story(include_harem=False)
        if not any(s["Id"] == s52.P + "docket" for s in cls.payload["Scenes"]):
            s52.register(cls.payload, cls.payload["Scenes"], cls.payload["Etudes"])
        cls.model = rules.Model(cls.payload)
        cls.rows = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(s52.P)}

    def state(self, *extra, verdict=True):
        st = rules.SimState(5, 100)
        st.flags.update(["trickster", "availability.observed", "dorgelinda.present", *extra])
        if verdict:
            st.flags.update([s52.SELECTED, s52.VERDICT])
        rules.sim_complete(self.model, st)
        return st

    def available(self, step, state):
        return rules.sim_available(self.model, self.rows[s52.P + step], state)

    def test_exact_selected_answer_and_seen_outcome_both_required(self):
        self.assertEqual(self.payload["SelectedAnswers"][s52.SELECTED], "e0c8aca7fe35b844a8ab76f96f2b3372")
        self.assertEqual(self.payload["SeenCues"][s52.VERDICT], ["513decde8a1bc7143bb2828521dad79f"])
        for selected, seen in ((False, False), (False, True), (True, False), (True, True)):
            with self.subTest(selected=selected, seen=seen):
                extra = ([s52.SELECTED] if selected else []) + ([s52.VERDICT] if seen else [])
                self.assertEqual(self.available("docket", self.state(*extra, verdict=False)), selected and seen)
        for alternative in ("hanged_lann", "prison", "hushed", "redeemed"):
            self.assertFalse(self.available("docket", self.state("dorgelinda.verdict_" + alternative, verdict=False)))

    def test_no_romance_page_council_etude_or_wenduag_needed(self):
        for absence in ("wenduag.closed", "wenduag.killed", "wenduag.dead_any", "wenduag.kicked_out", "wenduag.epoch_unavailable"):
            st = self.state(absence)
            self.assertTrue(self.available("docket", st))
            self.assertFalse(self.available("docket.live", st))
        self.assertTrue(self.available("docket", self.state()))
        for blocker in ("dorgelinda.closed", "dorgelinda.epoch_unavailable", "swarm"):
            self.assertFalse(self.available("docket", self.state(blocker)))
        st = self.state(); st.flags.remove("dorgelinda.present")
        rules.sim_complete(self.model, st)
        self.assertFalse(self.available("docket", st))
        for chapter in (3, 4, 6):
            st = self.state(); st.chapter = chapter
            self.assertFalse(self.available("docket", st))
        st = self.state(); st.flags.remove("trickster")
        rules.sim_complete(self.model, st)
        self.assertFalse(self.available("docket", st))

    def test_live_variant_needs_current_body_and_open_route(self):
        st = self.state("wenduag.in_party")
        self.assertTrue(self.available("docket.live", st))
        # Native InParty also includes remote/detached companions. The history
        # remains selectable even when a live wrapper's physical check fails.
        self.assertTrue(self.available("docket", st))
        self.assertEqual(self.rows[s52.P + "docket.live"]["AdditionalContactUnits"], [s52.WENDUAG_UNIT])
        self.assertFalse(self.rows[s52.P + "docket"]["AdditionalContactUnits"])
        # E9 assumes all contacts present. An earned off-party body may answer
        # as well; the compiled runtime checks its actual local contact unit.
        self.assertTrue(self.available("docket.live", self.state("wenduag.trickster.returned")))
        for loss in ("wenduag.closed", "wenduag.q3_killed", "wenduag.epoch_unavailable", "wenduag.returned_actor_lost"):
            st = self.state("wenduag.in_party", "wenduag.trickster.returned",
                            "wenduag.trickster.echo.abyss.returned_available", loss)
            self.assertFalse(self.available("docket.live", st), loss)
            self.assertTrue(self.available("docket", st), loss)

    def test_recovery_48_hours_and_permanent_outcomes(self):
        for source in ("docket.failed", "docket.refused"):
            st = self.state(s52.P + source, s52.P + "docket.seen")
            st.times[s52.P + source] = 100
            for hour, expected in ((147, False), (148, True)):
                st.hour = hour
                self.assertEqual(self.available("retry", st), expected)
            st.flags.add(s52.P + "retry.seen")
            self.assertFalse(self.available("retry", st))
        for terminal in ("provisioned", "blame_shifted", "unanswered"):
            st = self.state(s52.P + terminal, s52.P + "docket.seen")
            self.assertFalse(self.available("docket", st))
            self.assertFalse(self.available("retry", st))
        for row in self.rows.values():
            self.assertEqual(delayed_clock_errors(row, self.payload), [])
            self.assertEqual(row["RestAllowance"], "household.protected")
            self.assertFalse(any(".cap." in key for key in row["Forbids"]))

    def test_actual_paid_answers_transaction_matrix_replay_and_live_wrapper(self):
        for step, index, price in (("docket", 1, 150), ("retry", 0, 200)):
            row = self.rows[s52.P + step]
            choice = row["Nodes"][0]["Choices"][index]
            for funds in (None, 0, price - 1, price, price + 70):
                with self.subTest(step=step, funds=funds):
                    st = self.state("chapter_later")
                    if step == "retry":
                        st.flags.update(s52.flags("docket.failed", "docket.seen"))
                        st.times[s52.P + "docket.failed"] = 0
                    st.crusade_resources = None if funds is None else {"Materials": funds}
                    before = copy.deepcopy(st.__dict__)
                    def publish():
                        st.flags.update(choice["Set"] + [row["Id"]])
                        st.times.update({f: st.hour for f in choice["Set"] + [row["Id"]]})
                        st.rest_spent["household.protected"] = 1
                    accepted = funds is not None and funds >= price
                    self.assertEqual(rules.sim_paid_choice(self.model, row, choice, st, publish), accepted)
                    if accepted:
                        self.assertEqual(st.crusade_resources["Materials"], funds - price)
                        self.assertIn(s52.P + "load_received", st.flags)
                        self.assertFalse(rules.sim_paid_choice(self.model, row, choice, st, publish))
                        st.flags.add("wenduag.in_party"); rules.sim_complete(self.model, st)
                        wrapper = self.rows[s52.P + step + ".live"]
                        self.assertFalse(rules.sim_paid_choice(self.model, wrapper, wrapper["Nodes"][0]["Choices"][index], st, publish))
                    else:
                        self.assertEqual(st.__dict__, before)

    def test_save_ids_abort_and_exhaustive_outcomes(self):
        self.assertEqual(savecompat.check(self.payload), [])
        for row in self.rows.values():
            for node in row["Nodes"]:
                self.assertFalse(node.get("Paragraphs"))
                for answer in node["Choices"]:
                    self.assertTrue(all(f.startswith(s52.P) for f in answer["Set"]))
                    self.assertFalse(any("enmity" in f or "reconciled" in f or "committed" in f for f in answer["Set"]))
                    if answer["Abort"]:
                        self.assertFalse(answer["Set"])
                        self.assertIsNone(answer["Next"])
                        self.assertIsNone(answer.get("Crusade"))
            self.assertTrue(select_answer(row["Nodes"][0]["Choices"], ((None, True, None, None, (), ()),), expected_position=-1)["Abort"])
            self.assertFalse(row.get("NativeReturnCue"))
        root = self.rows[s52.P + "docket"]["Nodes"][0]
        self.assertEqual(select_answer(root["Choices"], ((None, False, 'received', 'short', (), ()),), expected_position=0)["Check"]["DC"], 20)
        self.assertEqual(select_answer(root["Choices"], ((None, False, 'received', 'short', (), ()),), expected_position=0)["Set"], [])

    def test_every_page_has_an_answer_even_without_money(self):
        for row in self.rows.values():
            self.assertEqual(row["Areas"], [s52.DREZEN])
            self.assertEqual(row["AnswerLists"], [s52.HUB])
            self.assertEqual(row["ContactUnit"], s52.UNIT)
            for funds in (None, 0, 149, 150, 199, 200):
                st = self.state()
                st.crusade_resources = None if funds is None else {"Materials": funds}
                for node in row["Nodes"]:
                    self.assertTrue(any(rules.sim_choice_available(answer, st) for answer in node["Choices"]),
                                    (row["Id"], node["Id"], funds))

    def test_paid_execution_rechecks_current_funds_office_and_allowance(self):
        row = self.rows[s52.P + "docket"]
        choice = select_answer(row["Nodes"][0]["Choices"], ((None, False, None, None, (), ()),), expected_position=1)
        for change in ("funds", "kingdom", "allowance", "office_closed", "office_gone", "publication"):
            with self.subTest(change=change):
                st = self.state(); st.crusade_resources = {"Materials": 150}
                self.assertTrue(rules.sim_choice_available(choice, st))
                if change == "funds": st.crusade_resources["Materials"] = 149
                elif change == "kingdom": st.crusade_resources = None
                elif change == "allowance": st.rest_spent["household.protected"] = 2
                elif change == "office_closed":
                    st.flags.add("dorgelinda.closed"); rules.sim_complete(self.model, st)
                elif change == "office_gone":
                    st.flags.remove("dorgelinda.present"); rules.sim_complete(self.model, st)
                before = copy.deepcopy(st.__dict__)
                def publish():
                    st.flags.update(choice["Set"])
                    raise RuntimeError("Publication failed")
                self.assertFalse(rules.sim_paid_choice(self.model, row, choice, st, publish))
                self.assertEqual(st.__dict__, before)




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
