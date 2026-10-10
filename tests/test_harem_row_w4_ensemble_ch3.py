"""Ch3 ensemble: current bodies, indexed choices, no pair-state producers."""
import copy
import unittest

from tests.story_fixture import fresh_story
from tests.harem_row_walk import walk
from storylines.harem_rows import w4_ensemble_ch3 as row
from storylines import household
from tools import rrt_verify as rules, savecompat


class Ch3EnsembleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = rules.Model(cls.story)
        cls.scene = cls.model.by_id[row.ID]

    def state(self):
        state = rules.SimState(3, 1000)
        state.flags.update({"trickster", "trickster.foresight.accepted",
                            household.KEPT, "seelah.committed", "seelah.chosen_future",
                            "seelah.short_future_chosen", "seelah.in_party",
                            "nenio.committed", "nenio.trickster.test_running",
                            "nenio.trickster.first_night", "nenio.in_party",
                            "wenduag.romance_finished.latched", "wenduag.in_party"})
        rules.sim_complete(self.model, state)
        return state

    def test_current_page_path_bodies_and_chapter(self):
        state = self.state()
        self.assertTrue(rules.sim_available(self.model, self.scene, state))
        for flag in self.scene["Requires"]:
            with self.subTest(missing=flag):
                missing = copy.deepcopy(state)
                missing.flags.remove(flag)
                self.assertFalse(rules.sim_available(self.model, self.scene, missing))
        for chapter in (1, 2, 4, 5, 6):
            state.chapter = chapter
            self.assertFalse(rules.sim_available(self.model, self.scene, state))

    def test_closure_and_later_departure_survive_old_returns(self):
        for woman in row.WOMEN:
            for loss in (woman + ".closed", woman + ".epoch_unavailable"):
                with self.subTest(loss=loss):
                    state = self.state()
                    state.flags.update([loss, woman + ".trickster.returned", "nenio.life.recreated"])
                    self.assertFalse(rules.sim_available(self.model, self.scene, state))
        state = self.state()
        state.flags.add("sacrifice")
        self.assertFalse(rules.sim_available(self.model, self.scene, state))
        state.flags.add("trickster.commander_back")
        self.assertTrue(rules.sim_available(self.model, self.scene, state))

    def test_every_answer_finishes_or_aborts_without_pair_progression(self):
        outcomes = walk(self, self.model, self.scene, self.state())
        self.assertIn(contract_identities(outcomes),
                {3: ((('household.any_eligible',
                       'household.ensemble.ch3.supper',
                       'household.ensemble.ch3.supper.seen',
                       'household.outcome.route_open',
                       'household.pair.camellia_arueshalae.body.camellia',
                       'household.pair.camellia_arueshalae.body.camellia.native',
                       'household.pair.galfrey_arueshalae.voice.native_queen',
                       'household.pair.galfrey_arueshalae.voice.queen',
                       'household.pair.nenio_arueshalae.body.nenio',
                       'household.pair.seelah_arueshalae.fallen.seelah_body',
                       'household.pair.seelah_camellia.camellia_body',
                       'household.pair.seelah_camellia.camellia_native_body',
                       'household.pair.seelah_camellia.seelah_body',
                       'household.pair.seelah_camellia.seelah_native_body',
                       'household.pair.seelah_kiana.conscious',
                       'household.pair.seelah_kiana.soul_clear',
                       'household.pair.seelah_nenio.body.nenio',
                       'household.pair.seelah_nenio.body.seelah',
                       'household.pair.seelah_nenio.ready',
                       'household.pair.wenduag_arueshalae.body.arueshalae.native_evil',
                       'household.pair.wenduag_arueshalae.body.wenduag',
                       'household.pair.wenduag_dorgelinda.office_open',
                       'household.pair.wenduag_dorgelinda.wenduag_here',
                       'household.readers.w5.commander.alive',
                       'household.readers.w5.commander.not_sacrificed',
                       'household.readers.w5.s10.clear.nenio',
                       'household.readers.w5.s10.clear.seelah',
                       'household.readers.w5.s10.current',
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
                       'household.table.kept'),
                      ('household.any_eligible',
                       'household.ensemble.ch3.supper',
                       'household.ensemble.ch3.supper.seen',
                       'household.outcome.route_open',
                       'household.pair.camellia_arueshalae.body.camellia',
                       'household.pair.camellia_arueshalae.body.camellia.native',
                       'household.pair.galfrey_arueshalae.voice.native_queen',
                       'household.pair.galfrey_arueshalae.voice.queen',
                       'household.pair.nenio_arueshalae.body.nenio',
                       'household.pair.seelah_arueshalae.fallen.seelah_body',
                       'household.pair.seelah_camellia.camellia_body',
                       'household.pair.seelah_camellia.camellia_native_body',
                       'household.pair.seelah_camellia.seelah_body',
                       'household.pair.seelah_camellia.seelah_native_body',
                       'household.pair.seelah_kiana.conscious',
                       'household.pair.seelah_kiana.soul_clear',
                       'household.pair.seelah_nenio.body.nenio',
                       'household.pair.seelah_nenio.body.seelah',
                       'household.pair.seelah_nenio.ready',
                       'household.pair.wenduag_arueshalae.body.arueshalae.native_evil',
                       'household.pair.wenduag_arueshalae.body.wenduag',
                       'household.pair.wenduag_dorgelinda.office_open',
                       'household.pair.wenduag_dorgelinda.wenduag_here',
                       'household.readers.w5.commander.alive',
                       'household.readers.w5.commander.not_sacrificed',
                       'household.readers.w5.s10.clear.nenio',
                       'household.readers.w5.s10.clear.seelah',
                       'household.readers.w5.s10.current',
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
                       'household.table.kept'),
                      ('household.any_eligible',
                       'household.outcome.route_open',
                       'household.pair.camellia_arueshalae.body.camellia',
                       'household.pair.camellia_arueshalae.body.camellia.native',
                       'household.pair.galfrey_arueshalae.voice.native_queen',
                       'household.pair.galfrey_arueshalae.voice.queen',
                       'household.pair.nenio_arueshalae.body.nenio',
                       'household.pair.seelah_arueshalae.fallen.seelah_body',
                       'household.pair.seelah_camellia.camellia_body',
                       'household.pair.seelah_camellia.camellia_native_body',
                       'household.pair.seelah_camellia.seelah_body',
                       'household.pair.seelah_camellia.seelah_native_body',
                       'household.pair.seelah_kiana.conscious',
                       'household.pair.seelah_kiana.soul_clear',
                       'household.pair.seelah_nenio.body.nenio',
                       'household.pair.seelah_nenio.body.seelah',
                       'household.pair.seelah_nenio.ready',
                       'household.pair.wenduag_arueshalae.body.arueshalae.native_evil',
                       'household.pair.wenduag_arueshalae.body.wenduag',
                       'household.pair.wenduag_dorgelinda.office_open',
                       'household.pair.wenduag_dorgelinda.wenduag_here',
                       'household.readers.w5.commander.alive',
                       'household.readers.w5.commander.not_sacrificed',
                       'household.readers.w5.s10.clear.nenio',
                       'household.readers.w5.s10.clear.seelah',
                       'household.readers.w5.s10.current',
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
                       'household.table.kept')),)}[3])
        for state in outcomes[:2]:
            self.assertIn(row.SEEN, state.flags)
            self.assertEqual(state.rest_spent["household.pair"], 1)
            self.assertFalse(rules.sim_available(self.model, self.scene, state))
        self.assertEqual(outcomes[2].flags, self.state().flags)
        self.assertTrue(rules.sim_available(self.model, self.scene, outcomes[2]))
        writes = {flag for node in self.scene["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
        self.assertEqual(writes, {row.SEEN})
        self.assertEqual(self.scene["HouseholdCategory"], "dynamic")
        self.assertFalse(self.scene.get("HouseholdArcStart"))

    def test_existing_allowance_blocks_second_beat(self):
        state = self.state()
        state.rest_spent["household.pair"] = 1
        self.assertFalse(rules.sim_available(self.model, self.scene, state))

    def test_existing_directional_objections_are_not_reconciled_by_supper(self):
        for objection, reconciled in row.OBJECTIONS.items():
            state = self.state()
            state.flags.add(objection)
            self.assertFalse(rules.sim_available(self.model, self.scene, state))
            state.flags.add(reconciled)
            self.assertTrue(rules.sim_available(self.model, self.scene, state))

    def test_append_only_registration_and_save_ids(self):
        payload = copy.deepcopy(self.story)
        before = copy.deepcopy(payload)
        row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(before, payload)
        payload["Scenes"] = [s for s in payload["Scenes"] if s["Id"] != row.ID]
        existing = copy.deepcopy(payload["Scenes"])
        row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(existing, payload["Scenes"][:-1])
        self.assertEqual(savecompat.check(payload), [])
        self.assertEqual([n["Id"] for n in self.scene["Nodes"]], ["start", "sample", "supper"])
        self.assertTrue(all(n["Choices"] and not n.get("Paragraphs") for n in self.scene["Nodes"]))

    def test_missing_body_binding_fails_without_partial_registration(self):
        payload = copy.deepcopy(self.story)
        payload["Scenes"] = [s for s in payload["Scenes"] if s["Id"] != row.ID]
        del payload["Etudes"]["wenduag.in_party"]
        before = copy.deepcopy(payload)
        with self.assertRaisesRegex(ValueError, "native party body"):
            row.register(payload, payload["Scenes"], payload["Etudes"])
        self.assertEqual(before, payload)

    def test_every_speaker_handoff_passes_player_text_lint(self):
        from tools.player_text_lint import check
        findings = check(dict(Scenes=[row.supper()]))
        self.assertEqual(findings["review"], [])


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
