"""Round-two branch histories, independent of the shared campaign fixtures."""
import json
import copy
import unittest
from unittest.mock import patch
from pathlib import Path

from storylines import eliandra_stars as stars, eliandra_trickster as main

E = main.E


def visible(item, flags):
    return (set(item.get("Requires", ())) <= flags
            and not set(item.get("Forbids", ())) & flags)



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class EliandraRoundTwoTests(unittest.TestCase):
    def test_wall_reading_earns_access_but_not_a_shrine_memory(self):
        for scene in main.SCENES + stars.SCENES:
            if scene["Id"].startswith(E + "ch5.last_rite"):
                place = next(n for n in scene["Nodes"] if n["Id"] == "place")
                for flags, expected in (({main.OBSERVED}, "heart_new"),
                                        ({main.OBSERVED, E + "ch5.observe"}, "heart_known")):
                    self.assertEqual([expected], [a["Next"] for a in place["Choices"] if visible(a, flags)])
                start = scene["Nodes"][0]
                self.assertTrue(all(main.STARTED in a["Set"] for a in start["Choices"]))

    def test_every_intimacy_declaration_has_its_actual_memory(self):
        for scene in stars.SCENES:
            if scene["Id"] not in (E + "visit.star_heart", E + "visit.star_heart_mark"):
                continue
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            for ident in ("look", "look_up"):
                for flags, expected in ((set(), "want_observation"),
                                        ({E + "terms_known"}, "want_rite"),
                                        ({main.DEAD_NAMED}, "want")):
                    self.assertEqual([expected], [a["Next"] for a in nodes[ident]["Choices"] if visible(a, flags)])
            slot = scene["Id"] + ".explicit.1"
            self.assertEqual(slot, saved_answer(nodes["charts"]["Choices"], 0)["Next"])
            self.assertEqual("morning", saved_answer(nodes[slot]["Choices"], 0)["Next"])
            self.assertFalse(saved_answer(nodes[slot]["Choices"], 0)["Set"])
            self.assertEqual([main.HEART_SEEN, main.CHARTS], saved_answer(nodes["end"]["Choices"], 0)["Set"])

    def test_written_yes_never_claims_a_road_yes(self):
        for scene in stars.SCENES:
            if scene["Id"] not in (E + "drezen.road", E + "drezen.road_mark"):
                continue
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            for flags, expected in ((set(), "war"), ({main.LETTER_ANSWERED}, "war_letter")):
                answers = [a for a in nodes["why"]["Choices"] if visible(a, flags) and a["Next"] != "yes"]
                self.assertEqual([expected], [a["Next"] for a in answers])
                self.assertEqual([E + "drezen.road_open"], saved_answer(nodes[expected]["Choices"], 0)["Set"])

    def test_away_blocks_both_hosts_and_all_physical_twins(self):
        for key, host in stars.PRESENCES.items():
            if key == stars.ARRIVAL:
                self.assertIn(main.AWAY, host["Requires"])
                self.assertEqual(48, host["DelayHours"])
                continue
            self.assertIn(main.AWAY, host["Forbids"])
            self.assertIn("eliandra.attacked", host["Forbids"])
        for scene in stars.SCENES:
            self.assertIn(main.AWAY, scene["Forbids"])
            self.assertIn("eliandra.attacked", scene["Forbids"])
        returned = next(s for s in main.SCENES if s["Id"] == E + "ch5.return_from_fords")
        self.assertFalse(returned.get("Remote", False))
        self.assertEqual(stars.ARRIVAL, returned["InteractionHub"])
        self.assertEqual(main.UNIT, returned["ContactUnit"])
        self.assertNotIn("Kind", returned)
        self.assertFalse(returned.get("ReturnToList", False))
        from tools.savecompat import choice_identities
        for node in returned["Nodes"]:
            identities = choice_identities(returned, node)
            ordinal = 0
            for identity in identities:
                self.assertEqual(identity['GuidFor'], 'answer.%s.%s.%d' % (returned['Id'], node['Id'], ordinal))
                ordinal += 1
            self.assertEqual([identity['Id'] for identity in identities], [c.get('Id') for c in node['Choices']])
        self.assertIn(main.LETTER_ANSWERED, returned["Requires"])
        self.assertIn(main.AWAY, returned["Requires"])
        self.assertEqual(48, returned["DelayHours"])
        self.assertNotIn(main.RETURNED, returned["Requires"])
        self.assertEqual([main.RETURNED], saved_answer(returned["Nodes"][-1]["Choices"], 0)["Set"])
        payload = {}
        main.integrate(payload)
        self.assertEqual([main.RETURNED], payload["DerivedForbids"][main.AWAY])

    def test_delayed_deceit_is_paid_before_her_acceptance(self):
        for suffix, receipt in (('late', main.LIED_ABOUT_HAND), ('unasked', main.TRIED_TO_CHEAT)):
            scene = next(s for s in main.SCENES if s['Id'] == E + 'epilogue.' + suffix)
            page = next(n for n in scene['Nodes'] if n['Id'] == 'page')
            debt = [p for p in page['Paragraphs'] if receipt in p['Requires']]
            self.assertTrue(debt)
            self.assertTrue(all(not visible(p, set()) for p in debt))
            self.assertTrue(any(visible(p, {receipt}) for p in debt))
            self.assertTrue(all(not c['Set'] for c in page['Choices']))

    def test_reunion_slot_requires_an_actually_shared_first_night(self):
        together = next(s for s in main.SCENES if s["Id"] == E + "epilogue.together")["Nodes"][0]
        slot = next(p for p in together["Paragraphs"] if p.get("Id"))
        self.assertFalse(visible(slot, set()))
        self.assertTrue(visible(slot, {main.HEART_SEEN}))
        counterpart, = [p for p in together["Paragraphs"] if main.HEART_SEEN in p["Forbids"]]
        self.assertTrue(visible(counterpart, set()))
        self.assertFalse(visible(counterpart, {main.HEART_SEEN}))

    def test_native_loss_and_historical_contact_are_observed(self):
        self.assertEqual("207ad04e9ad523f49af8c2a889a8e33e", main.BINDINGS["SelectedAnswers"]["eliandra.attacked"])
        for scene in main.SCENES:
            if main.PATH_FIT.get(scene["Id"]) == "N-fit":
                self.assertIn("eliandra.met_ch3", scene["Forbids"])
        self.assertIn("eliandra.attacked", main.RELATIONSHIP["UnavailableFlags"])

    def test_all_five_slot_briefs_match_their_live_defaults(self):
        from tests.story_fixture import fresh_story
        from tests.fix16b_structure import reachable_nodes
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        folder = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/eliandra"
        for path in folder.glob("*.json"):
            brief = json.loads(path.read_text(encoding="utf-8"))
            sid = brief["slot_id"].rsplit(".explicit.", 1)[0]
            scene = scenes[sid]
            with self.subTest(slot=brief["slot_id"]):
                nodes = {n["Id"]: n for n in scene["Nodes"]}
                if brief["slot_id"] in nodes:
                    slot = nodes[brief["slot_id"]]
                    self.assertIn(slot["Id"], reachable_nodes(scene))
                    self.assertEqual(["morning"], [c["Next"] for c in slot["Choices"]])
                    self.assertTrue(all(not c["Set"] for c in slot["Choices"]))
                else:
                    host = "page" if sid.endswith(".together") else "late_accepted"
                    page = nodes[host]
                    slot = next(p for p in page["Paragraphs"] if p.get("Id") == brief["slot_id"])
                    self.assertIn(host, reachable_nodes(scene))
                    self.assertFalse(slot.get("Set"))
                    successor = None if host == "page" else "page_exit"
                    self.assertTrue(all(c["Next"] == successor and not c["Set"] for c in page["Choices"]))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scenes = copy.deepcopy(main.SCENES)
        scene = next(s for s in scenes if s['Id'] == E + 'epilogue.late')
        page = next(n for n in scene['Nodes'] if n['Id'] == 'page')
        for paragraph in page['Paragraphs']:
            if main.LIED_ABOUT_HAND in paragraph['Requires']:
                paragraph['Requires'] = []
        with patch.object(main, 'SCENES', scenes):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_delayed_deceit_is_paid_before_her_acceptance()


if __name__ == "__main__":
    unittest.main()
