"""S09 progression against the assembled runtime model; no generated-file edits."""
import copy
import unittest

from tests.story_fixture import fresh_story
from storylines.harem_rows import s09
from tools import rrt_verify as rules
from tools.intimacy_contract_lint import walks
from tools.harem_schedule_lint import delayed_clock_errors
from tests.harem_row_walk import walk


class S09Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.rows = {s["Id"]: s for s in cls.model.scenes if s["Id"].startswith(s09.PREFIX)}

    def state(self, evil=True, hour=1000):
        state = rules.SimState(5, hour)
        state.flags.update(("trickster", "trickster.now", "availability.observed", "household.table.kept",
                            "trickster.foresight.accepted", "trickster.foresight.cost.promise",
                            "wenduag.committed", "arueshalae.committed", "wenduag.in_party",
                            "arueshalae.recruited_drezen", "arueshalae.native_alive",
                            "wenduag.trickster.proved", "wenduag.trickster.gate_seen",
                            "wenduag.trickster.claim.given", "arueshalae.trickster.terms"))
        state.flags.add("arueshalae.evil_recruited" if evil else "arueshalae.changed")
        rules.sim_complete(self.model, state)
        return state

    def scene(self, suffix):
        return self.rows[s09.p(suffix)]

    def finish(self, state, suffix, node="plotted"):
        scene = self.scene(suffix)
        choice = select_answer(next(n for n in scene["Nodes"] if n["Id"] == node)["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
        state.flags.update(choice["Set"])
        for flag in choice["Set"]:
            state.times[flag] = state.hour
        rules.sim_complete(self.model, state)

    def test_registration_is_idempotent_and_ids_are_unique(self):
        from storylines import household
        s09.register({}, [], {})
        s09.register({}, [], {})
        ids = [s["Id"] for s in household.ENTRIES if s["Id"].startswith(s09.PREFIX)]
        self.assertEqual(len(ids), 8)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(self.rows))

    def test_unknown_and_corruption_precedence_and_paid_page(self):
        state = self.state(False)
        self.assertTrue(rules.sim_available(self.model, self.scene("settle.good"), state))
        state.flags.add("arueshalae.evil_recruited")
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.good"), state))
        self.assertTrue(rules.sim_available(self.model, self.scene("settle.evil"), state))
        for key in ("arueshalae.changed", "arueshalae.evil_recruited", "arueshalae.recruited_drezen"):
            state.flags.discard(key)
        rules.sim_complete(self.model, state)
        self.assertFalse(any(rules.sim_available(self.model, self.scene("settle." + b), state) for b in ("good", "evil")))
        for removed in ("trickster", "trickster.foresight.accepted"):
            state = self.state()
            state.flags.discard(removed)
            rules.sim_complete(self.model, state)
            self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))

    def test_one_personality_operation_and_48_hour_retry(self):
        state = self.state(False)
        self.finish(state, "settle.good")
        state.flags.add("arueshalae.evil_recruited")
        rules.sim_complete(self.model, state)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))
        self.assertFalse(rules.sim_available(self.model, self.scene("friend_wenduag"), state))
        for evil, branch in ((True, "evil"), (False, "good")):
            state = self.state(evil)
            self.finish(state, "settle." + branch, "blind")
            state.hour += 47
            self.assertFalse(rules.sim_available(self.model, self.scene("retry." + branch), state))
            state.hour += 1
            self.assertTrue(rules.sim_available(self.model, self.scene("retry." + branch), state))
            self.finish(state, "retry." + branch)
            self.assertFalse(rules.sim_available(self.model, self.scene("retry." + branch), state))

    def test_romance_and_presence_alone_do_not_supply_a_body(self):
        for evil, native in ((True, "arueshalae.evil_recruited"), (False, "arueshalae.native_alive")):
            state = self.state(evil)
            scene = self.scene("settle.evil" if evil else "settle.good")
            self.assertTrue(rules.sim_available(self.model, scene, state))
            state.flags.discard(native)
            # Keep the personality classification from a historical solo outcome.
            state.flags.add("arueshalae.trickster.fallen.house_call" if evil else "arueshalae.changed")
            rules.sim_complete(self.model, state)
            self.assertIn("arueshalae.present_now", state.flags)
            self.assertFalse(rules.sim_available(self.model, scene, state))
        state = self.state()
        state.flags.discard("wenduag.in_party")
        rules.sim_complete(self.model, state)
        self.assertIn("wenduag.present_now", state.flags)
        self.assertFalse(rules.sim_available(self.model, self.scene("settle.evil"), state))

    def test_deeds_elapsed_time_mutual_answers_and_morning(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step in ("friend_wenduag", "friend_arueshalae"):
            state.hour += 47
            self.assertFalse(rules.sim_available(self.model, self.scene(step), state))
            state.hour += 1
            self.assertTrue(rules.sim_available(self.model, self.scene(step), state))
            self.finish(state, step, "her")
        state.hour += 48
        self.assertTrue(rules.sim_available(self.model, self.scene("choice"), state))
        for receipt in s09.flags(*s09.FRIEND_W, *s09.FRIEND_A):
            lost = copy.deepcopy(state)
            lost.flags.discard(receipt)
            rules.sim_complete(self.model, lost)
            self.assertFalse(rules.sim_available(self.model, self.scene("choice"), lost))
        self.assertNotIn("wenduag.harem.attitude.arueshalae.lover", state.flags)
        # The direct terminal helper does not execute intermediate ward removal.
        state.flags.update(s09.flags("cost.ward_scroll", "ward.applied_wenduag"))
        self.finish(state, "choice", "after")
        self.assertIn("wenduag.harem.attitude.arueshalae.lover", state.flags)
        self.assertIn("arueshalae.harem.attitude.wenduag.lover", state.flags)
        state.hour += 7
        self.assertFalse(rules.sim_available(self.model, self.scene("morning"), state))
        state.hour += 1
        self.assertTrue(rules.sim_available(self.model, self.scene("morning"), state))

    def test_later_loss_or_closure_blocks_every_step_and_old_return_does_not_help(self):
        for scene in self.rows.values():
            for loss in ("wenduag.closed", "arueshalae.closed", "wenduag.q3_sent_away",
                         "arueshalae.kicked_out_evil", "wenduag.epoch_unavailable", "arueshalae.epoch_unavailable"):
                state = self.state(scene["Id"].endswith("evil") or not scene["Id"].endswith("good"))
                state.flags.update(scene["Requires"])
                self.assertTrue(rules.sim_available(self.model, scene, state), scene["Id"])
                state.flags.update((loss, "wenduag.trickster.returned", "arueshalae.trickster.returned"))
                self.assertFalse(rules.sim_available(self.model, scene, state), (scene["Id"], loss))
            self.assertFalse(scene.get("ContactUnit"))
            self.assertIn(s09.p("body.wenduag"), scene["Requires"])
            self.assertTrue(any(key.startswith(s09.p("body.arueshalae.")) for key in scene["Requires"]))

    def test_scroll_is_spent_on_wenduag_no_abort_after_spend_and_slot_is_inert(self):
        scene = self.scene("choice")
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        choice = select_answer(nodes["protection"]["Choices"], (('threshold', False, None, None, ('arueshalae.ward_held', 'trickster.now', 'wenduag.present_now', 'arueshalae.present_now'), ()),), expected_position=0)
        self.assertEqual(choice["RemoveItem"], s09.SCROLL)
        self.assertEqual(set(choice["Set"]), set(s09.flags("cost.ward_scroll", "ward.applied_wenduag")))
        state = self.state()
        state.flags.add("arueshalae.trickster.fallen.warded")
        self.assertFalse(rules.sim_choice_available(choice, state))
        self.assertTrue(rules.sim_choice_available(select_answer(nodes["protection"]["Choices"], (('no_contact', False, None, None, (), ()),), expected_position=1), state))
        state.flags.add("arueshalae.ward_held")
        self.assertTrue(rules.sim_choice_available(choice, state))
        slot = nodes[s09.p("choice.explicit.1")]
        self.assertEqual(select_answer(slot["Choices"], (('after', False, None, None, (), ()),), expected_position=0)["Next"], "after")
        self.assertEqual(select_answer(slot["Choices"], (('after', False, None, None, (), ()),), expected_position=0)["Set"], [])
        paths = list(walks(scene, set(s09.LIVE) | set(s09.flags("ward.applied_wenduag")), "threshold"))
        _single_result, = paths
        self.assertIn("after", paths[0][0])
        for node in ("threshold", s09.p("choice.explicit.1"), "after"):
            self.assertFalse(any(c["Abort"] for c in nodes[node]["Choices"]))

    def test_optional_choice_walk_requires_fresh_ward_and_preserves_solo_bonds(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step in ("friend_wenduag", "friend_arueshalae"):
            state.hour += 48
            self.finish(state, step, "her")
        state.hour += 48
        scene = self.scene("choice")
        self.assertTrue(rules.sim_available(self.model, scene, state))
        for fresh_ward in (False, True):
            ready = copy.deepcopy(state)
            ready.flags.add("arueshalae.trickster.fallen.warded")
            if fresh_ward:
                ready.flags.add("arueshalae.ward_held")
            outcomes = walk(self, self.model, scene, ready)
            lovers = [outcome for outcome in outcomes if s09.p("choice.both_yes") in outcome.flags]
            self.assertIn(contract_identities(lovers),
                    {0: ((),),
                     1: ((('household.any_eligible',
                           'household.outcome.route_open',
                           'household.pair.camellia_arueshalae.body.camellia',
                           'household.pair.camellia_arueshalae.body.camellia.native',
                           'household.pair.galfrey_arueshalae.voice.native_queen',
                           'household.pair.galfrey_arueshalae.voice.queen',
                           'household.pair.nenio_arueshalae.body.arueshalae',
                           'household.pair.seelah_arueshalae.arueshalae_body',
                           'household.pair.seelah_camellia.camellia_body',
                           'household.pair.seelah_camellia.camellia_native_body',
                           'household.pair.seelah_camellia.seelah_body',
                           'household.pair.seelah_camellia.seelah_native_body',
                           'household.pair.seelah_kiana.conscious',
                           'household.pair.seelah_kiana.soul_clear',
                           'household.pair.wenduag_arueshalae.body.arueshalae.evil',
                           'household.pair.wenduag_arueshalae.body.arueshalae.good',
                           'household.pair.wenduag_arueshalae.body.arueshalae.native_evil',
                           'household.pair.wenduag_arueshalae.body.wenduag',
                           'household.pair.wenduag_arueshalae.choice',
                           'household.pair.wenduag_arueshalae.choice.both_yes',
                           'household.pair.wenduag_arueshalae.choice.seen',
                           'household.pair.wenduag_arueshalae.cost.arueshalae_easy_bait_yielded',
                           'household.pair.wenduag_arueshalae.cost.arueshalae_foot_plan_yielded',
                           'household.pair.wenduag_arueshalae.cost.commander_route_labour',
                           'household.pair.wenduag_arueshalae.cost.ward_scroll',
                           'household.pair.wenduag_arueshalae.cost.wenduag_credit_shared',
                           'household.pair.wenduag_arueshalae.cost.wenduag_solo_boast_yielded',
                           'household.pair.wenduag_arueshalae.deed.arueshalae_cover_kept',
                           'household.pair.wenduag_arueshalae.deed.arueshalae_desire_answer',
                           'household.pair.wenduag_arueshalae.deed.arueshalae_height',
                           'household.pair.wenduag_arueshalae.deed.wenduag_credit_kept',
                           'household.pair.wenduag_arueshalae.deed.wenduag_desire_answer',
                           'household.pair.wenduag_arueshalae.deed.wenduag_ground',
                           'household.pair.wenduag_arueshalae.friend_arueshalae.done',
                           'household.pair.wenduag_arueshalae.friend_arueshalae.seen',
                           'household.pair.wenduag_arueshalae.friend_wenduag.done',
                           'household.pair.wenduag_arueshalae.friend_wenduag.seen',
                           'household.pair.wenduag_arueshalae.ready.evil',
                           'household.pair.wenduag_arueshalae.settle.done',
                           'household.pair.wenduag_arueshalae.settle.evil_done',
                           'household.pair.wenduag_arueshalae.settle.seen',
                           'household.pair.wenduag_arueshalae.ward.applied_wenduag',
                           'household.pair.wenduag_dorgelinda.office_open',
                           'household.pair.wenduag_dorgelinda.wenduag_here',
                           'household.readers.w5.commander.alive',
                           'household.readers.w5.commander.not_sacrificed',
                           'household.readers.w5.s10.clear.nenio',
                           'household.readers.w5.s10.clear.seelah',
                           'household.readers.w5.s10.speaking.nenio',
                           'household.readers.w5.s10.speaking.seelah',
                           'household.readers.w5.s20.clear.jannah',
                           'household.readers.w5.s20.clear.seelah',
                           'household.readers.w5.s20.speaking.jannah',
                           'household.readers.w5.s20.speaking.seelah',
                           'household.readers.w5.s21.clear.seelah',
                           'household.readers.w5.s21.clear.yaniel',
                           'household.readers.w5.s21.speaking.seelah',
                           'household.readers.w5.s21.speaking.yaniel',
                           'household.readers.w5.s29.clear.kiana',
                           'household.readers.w5.s29.clear.seelah',
                           'household.readers.w5.s29.speaking.kiana',
                           'household.readers.w5.s29.speaking.seelah',
                           'household.readers.w5.s30.clear.eliandra',
                           'household.readers.w5.s30.clear.targona',
                           'household.readers.w5.s30.speaking.eliandra',
                           'household.readers.w5.s30.speaking.targona',
                           'household.stance_eligible',
                           'household.table.kept'),),)}[int(fresh_ward)])
            for outcome in outcomes:
                rules.sim_complete(self.model, outcome)
                self.assertIn("wenduag.committed", outcome.flags)
                self.assertIn("arueshalae.committed", outcome.flags)
                mutual = s09.p("choice.both_yes") in outcome.flags
                for a, b in (s09.PAIR, tuple(reversed(s09.PAIR))):
                    self.assertEqual(a + ".harem.attitude." + b + ".lover" in outcome.flags, mutual)
                if mutual:
                    self.assertIn(s09.p("ward.applied_wenduag"), outcome.flags)
                    self.assertIn(s09.p("cost.ward_scroll"), outcome.flags)
                    self.assertEqual(outcome.rest_spent["household.pair"], 1)
                    for receipt in ("deed.wenduag_desire_answer", "deed.arueshalae_desire_answer",
                                    "cost.ward_scroll", "ward.applied_wenduag"):
                        missing = copy.deepcopy(outcome)
                        missing.flags.remove(s09.p(receipt))
                        rules.sim_complete(self.model, missing)
                        self.assertNotIn("wenduag.harem.attitude.arueshalae.lover", missing.flags)
                        self.assertNotIn("arueshalae.harem.attitude.wenduag.lover", missing.flags)
                else:
                    self.assertNotIn(s09.p("ward.applied_wenduag"), outcome.flags)
                    if s09.p("choice.declined") in outcome.flags:
                        outcome.hour += 8
                        self.assertFalse(rules.sim_available(self.model, self.scene("morning"), outcome))

    def test_all_optional_entries_require_current_page_path_and_bodies(self):
        state = self.state()
        self.finish(state, "settle.evil")
        for step, node, hours in (("friend_wenduag", "her", 48),
                                  ("friend_arueshalae", "her", 48),
                                  ("choice", "after", 48), ("morning", "kept", 8)):
            state.hour += hours
            scene = self.scene(step)
            self.assertTrue(rules.sim_available(self.model, scene, state))
            for removed in ("trickster", "trickster.foresight.accepted", "household.table.kept",
                            "wenduag.in_party", "arueshalae.evil_recruited"):
                missing = copy.deepcopy(state)
                missing.flags.remove(removed)
                rules.sim_complete(self.model, missing)
                self.assertFalse(rules.sim_available(self.model, scene, missing), (step, removed))
            for loss in ("wenduag.q3_killed", "arueshalae.evil_dead"):
                lost = copy.deepcopy(state)
                lost.flags.add(loss)
                rules.sim_complete(self.model, lost)
                self.assertFalse(rules.sim_available(self.model, scene, lost), (step, loss))
            self.finish(state, step, node)

    def test_optional_start_needs_actual_base_respect_deeds(self):
        state = self.state()
        self.finish(state, "settle.evil")
        state.hour += 48
        for receipt in s09.RESPECT:
            missing = copy.deepcopy(state)
            missing.flags.remove(s09.p(receipt))
            rules.sim_complete(self.model, missing)
            self.assertFalse(rules.sim_available(self.model, self.scene("friend_wenduag"), missing))

    def test_refusal_abort_allowances_enmity_and_clock_contracts(self):
        for suffix, scene in self.rows.items():
            self.assertEqual(delayed_clock_errors(scene, self.story), [], suffix)
            protected = ".settle." in suffix or ".retry." in suffix
            self.assertEqual(scene["RestAllowance"], "household.protected" if protected else "household.pair")
            self.assertEqual(scene["HouseholdArcStart"], suffix.endswith("friend_wenduag"))
            self.assertEqual(scene["HouseholdArc"], s09.PREFIX.rstrip('.'))
            root = scene["Nodes"][0]
            abort = select_answer(root["Choices"], ((None, True, None, None, (), ()),), expected_position=-1)
            self.assertTrue(abort["Abort"])
            self.assertEqual(abort["Set"], [])
            state = self.state(not suffix.endswith("good"))
            state.flags.update(scene["Requires"])
            state.flags.add("wenduag.harem.enmity.arueshalae")
            self.assertFalse(rules.sim_available(self.model, scene, state))
            state.flags.add("wenduag.harem.reconciled.arueshalae")
            self.assertTrue(rules.sim_available(self.model, scene, state))
            state.rest_spent[scene["RestAllowance"]] = 2 if protected else 1
            self.assertFalse(rules.sim_available(self.model, scene, state))
        effects = [f for s in self.rows.values() for n in s["Nodes"] for c in n["Choices"] for f in c["Set"]]
        self.assertTrue(all(f.startswith(s09.PREFIX) for f in effects))




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
