"""History regressions from the two Mielarah audits, without the full story build."""
import copy
import json
from pathlib import Path
import subprocess
import unittest
from storylines import mielarah_deck as deck, mielarah_trickster as route
from tools import savecompat
ROOT = Path(__file__).resolve().parents[1]
P, D = (route.P, route.D)

def nodes(scene):
    return {node["Id"]: node for node in scene["Nodes"]}

def answers(node, flags):
    return [answer for answer in node["Choices"]
            if set(answer["Requires"]) <= flags and not set(answer["Forbids"]) & flags]

class MielarahRound2Tests(unittest.TestCase):

    def setUp(self):
        self.scenes = {scene["Id"]: scene for scene in [*route.SCENES, *deck.SCENES]}

    def test_truth_then_withdraw_never_dispatches_a_paid_minder(self):
        flags = {route.PATTERN, route.TOLD, route.REFUSED}
        landing = answers(nodes(self.scenes[P + "colyphyr.landfall"])["start"], flags)
        self.assertEqual(["voyage"], [a["Next"] for a in landing])
        for suffix in ("", ".arcade"):
            dispatch = answers(nodes(self.scenes[D + "nearest" + suffix])["start"], flags)
            self.assertEqual(["none"], [a["Next"] for a in dispatch])
            paid = answers(nodes(self.scenes[D + "nearest" + suffix])["start"],
                            {route.PATTERN, route.TOLD, route.MINDER, route.PAID})
            self.assertEqual(["alive"], [a["Next"] for a in paid])

    def test_previous_misses_extend_into_weather_and_sleep(self):
        for suffix in ("", ".arcade"):
            wheel = nodes(self.scenes[D + "wheel" + suffix])
            emergence = next(n for n in wheel.values() if any(a["Next"] == "above" for a in n["Choices"]))
            morning = nodes(self.scenes[D + "morning" + suffix])["start"]
            for flags, expected in ((set(), "above"), ({P + "repeated"}, "above_repeat"),
                                    ({D + "wounded_carried"}, "above_rescue"),
                                    ({P + "repeated", D + "wounded_carried"}, "above_repeat")):
                self.assertEqual([expected], [a["Next"] for a in answers(emergence, flags)])
                self.assertEqual([expected.replace("above", "block")],
                                 [a["Next"] for a in answers(morning, flags)])

    def test_owed_settlement_guards_unfinished_without_changing_ending_exits(self):
        ending = self.scenes[P + 'epilogue.unfinished']
        for owed in (route.OSKEL_DEAD, route.MEANT):
            self.assertIn(owed, ending['Forbids'])
            self.assertEqual(D + 'oskel_settled', ending['ForbidOverrides'][owed])
        for nid in ('climb', 'fly'):
            ordered_answer_1, *_ = nodes(ending)[nid]['Choices']
            exit = ordered_answer_1
            self.assertEqual([], exit['Set'])
            self.assertIsNone(exit['Next'])

    def test_paid_bearing_is_not_arrival_and_late_search_is_dated(self):
        contact = route.DERIVED[route.CONTACT]
        self.assertNotIn([route.RETURNED], contact)
        self.assertEqual([[route.RETURNED]], route.DERIVED[P + "returned_third"])
        arrival = self.scenes[P + "fourth.arrival"]
        self.assertEqual(1080, arrival["DelayHours"])
        self.assertIn(route.SHIP_LOST, arrival["Requires"])
        self.assertNotIn(route.CONTACT, arrival["Requires"])
        for hub in ("mielarah.presence.fourth_arrival", "mielarah.presence.fourth_arrival_arcade"):
            presence = route.PRESENCES[hub]
            self.assertFalse(set(presence["Requires"]) & set(presence["Forbids"]))
        late = self.scenes[P + "raid.ashore_drezen"]
        self.assertEqual(720, late["DelayHours"])
        self.assertIn(route.SEARCH_LAUNCHED, late["Requires"])
        self.assertIn(route.SEARCH_LAUNCHED, self.scenes[P + "raid.ashore"]["Forbids"])

    def test_victory_letter_requires_completed_native_quest(self):
        self.assertEqual("f10653a2a7032214a9dd3039d156f55d",
                         route.BINDINGS["CompletedQuests"][P + "colyphyr.completed"])
        self.assertIn(P + "colyphyr.finished", self.scenes[P + "colyphyr.letter"]["Requires"])

    def test_four_slots_keep_first_night_on_the_legacy_answer(self):
        for stem in ('wheel', 'quarterdeck'):
            for suffix in ('', '.arcade'):
                sid = D + stem + suffix
                ns = nodes(self.scenes[sid])
                ordered_answer_2, *_ = ns['threshold']['Choices']
                exit = ordered_answer_2
                self.assertEqual([route.NIGHT], exit['Set'])
                self.assertEqual('explicit.1', exit['Next'])
                ordered_answer_3, *_ = ns['explicit.1']['Choices']
                self.assertEqual([], ordered_answer_3['Set'])
                brief = json.loads((ROOT / 'tools/route_packs/explicit_slots/mielarah' / (sid + '.explicit.1.json')).read_text(encoding='utf-8'))
        self.assertIn(route.NIGHT, self.scenes[D + 'quarterdeck']['Forbids'])

    def test_warning_spends_no_remote_delivery_in_any_deferred_chain(self):
        for sid in (P + 'spade.dream', P + 'spade.watch_arcade', P + 'fourth.arrival'):
            self.assertFalse(self.scenes[sid].get('Remote', False))
            self.assertEqual(route.UNIT, self.scenes[sid]['ContactUnit'])
        for chain in (('raid.rope', 'raid.rock'), ('raid.elbow', 'raid.rock'), ('storm.word', 'storm.survivor_drezen'), ('raid.overboard_drezen', 'raid.ashore_drezen')):
            self.assertEqual([self.scenes[P + part].get('Remote', False) for part in chain], [True, True])

    def test_frozen_route_save_inventory(self):
        before = []
        for name in ("mielarah_trickster", "mielarah_deck"):
            source = subprocess.check_output(["git", "show", "HEAD:storylines/" + name + ".py"], cwd=ROOT)
            namespace = {"__name__": "round2_baseline_" + name}
            exec(compile(source, name, "exec"), namespace)
            before.extend(copy.deepcopy(namespace["SCENES"]))
        self.assertEqual([], savecompat.check({"Scenes": list(self.scenes.values())},
                                            savecompat.inventory({"Scenes": before})))
if __name__ == '__main__':
    unittest.main()
