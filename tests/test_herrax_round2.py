"""Round-2 situations: real decisions, result-specific memories and earned cuts."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story
from tests.fix16b_structure import declared_host, reachable_nodes

from storylines import herrax_house as house
from storylines import herrax_trickster as route


SCENES = {s["Id"]: s for s in [*route.SCENES, *house.SCENES]}


def available(answer, flags):
    return set(answer.get("Requires", ())) <= flags and not set(answer.get("Forbids", ())) & flags


def walk(scene_id, flags, selections):
    event = SCENES[scene_id]
    nodes = {n["Id"]: n for n in event["Nodes"]}
    node = event["Nodes"][0]
    visited = []
    for _ in range(60):
        visited.append(node["Id"])
        answers = [(i, a) for i, a in enumerate(node["Choices"]) if available(a, flags)]
        if not answers:
            raise AssertionError((scene_id, node["Id"], "no selectable answer"))
        index = selections.get(node["Id"], answers[0][0])
        answer = node["Choices"][index]
        if not available(answer, flags):
            raise AssertionError((scene_id, node["Id"], index, "unavailable answer"))
        flags.update(answer.get("Set", ()))
        if not answer.get("Next"):
            return visited, flags
        node = nodes[answer["Next"]]
    raise AssertionError("loop")


class HerraxRound2Tests(unittest.TestCase):
    def test_both_first_nights_reach_slot_and_breakfast(self):
        for suffix, flags in [("reachable", {route.KNIFE_TAKEN, route.BAIT}),
                              ("reachable_restored", {route.RESTORED})]:
            sid = route.H + "madam." + suffix
            for scar_choice in (0, 1):
                visited, final = walk(sid, set(flags), {"offer": 0, "desire": scar_choice})
                self.assertIn(sid + ".explicit.1", visited)
                self.assertIn("morning2", visited)
                self.assertIn(route.COMMITTED, final)
                self.assertIn(route.MORNING, final)

    def test_refusal_never_reaches_intimacy(self):
        for suffix, flags in [("reachable", {route.KNIFE_TAKEN, route.BAIT}),
                              ("reachable_restored", {route.RESTORED})]:
            visited, final = walk(route.H + "madam." + suffix, flags, {"offer": 1})
            self.assertIn(route.CLOSED, final)
            self.assertNotIn(route.COMMITTED, final)
            self.assertFalse(any("explicit" in node for node in visited))

    def test_hand_return_receipt_counts_only_observed_coin_return(self):
        for coin in (False, True):
            flags = {route.HANDED, route.BLOWN}
            if coin:
                flags.add(route.COIN_BACK)
            visited, _ = walk(route.H + "madam.reachable", flags, {})
            self.assertIn("handed_blown" if coin else "handed_blown_no_coin", visited)

    def test_late_face_to_face_decision_precedes_act(self):
        sid = route.H + "epilogue.after_hours.invitation"
        for madam in (False, True):
            offer = "madam_offer" if madam else "rooms_offer"
            for refuse in (False, True):
                visited, flags = walk(sid, {route.MADAM} if madam else set(), {offer: int(refuse)})
                self.assertIn(offer, visited)
                self.assertEqual(refuse, route.CLOSED in flags)
                self.assertEqual(not refuse, route.H + "epilogue.after_hours.explicit.1" in visited)
                self.assertEqual(not refuse, "morning" in visited)
        ending = SCENES[route.H + "epilogue.after_hours"]
        self.assertEqual("scene:" + sid, ending["EpilogueAfter"])
        exit = select_answer(ending["Nodes"][0]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
        self.assertFalse(any(exit.get(k) for k in ("Next", "Set", "Requires", "Forbids", "Check", "Abort")))

    def test_repeat_visit_reaches_repeat_slot(self):
        for choice in (0, 1):
            visited, _ = walk(house.STAIRS, {route.COMMITTED}, {"timed": 0, "close": choice})
            self.assertIn(house.STAIRS + ".explicit.1", visited)
            self.assertIn("return_morning", visited)

    def test_late_return_remembers_completed_punishments(self):
        scenes = {s["Id"]: s for s in fresh_story()["Scenes"]}
        visit = scenes[route.H + "epilogue.after_hours.invitation"]
        paragraphs = visit["Nodes"][0]["Paragraphs"]
        # Identify memories by their receipts, independently of paragraph order.
        cases = [(route.BAIT, {route.BAIT}, {route.LESSON, route.DECLINED}),
                 (route.BLOWN, {route.BLOWN}, {route.BAIT, route.LESSON, route.DECLINED}),
                 (route.RESTORED, {route.RESTORED, route.DECLINED, route.LESSON}, {"herrax.house.a_night_late"})]
        for receipt, flags, blockers in cases:
            candidates = [p for p in paragraphs if p.get("Requires") == [receipt]]
            self.assertTrue(candidates, receipt)
            memory = next(p for p in candidates if blockers <= set(p["Forbids"]))
            self.assertTrue(available(memory, flags))
            self.assertFalse(available(memory, flags - {receipt}))
            for blocker in blockers:
                self.assertFalse(available(memory, flags | {blocker}))
        late = next(p for p in paragraphs if p.get("Requires") == [route.RESTORED, "herrax.house.a_night_late"])
        earned = {route.RESTORED, "herrax.house.a_night_late"}
        self.assertTrue(available(late, earned))
        for receipt in earned:
            self.assertFalse(available(late, earned - {receipt}))

    def test_bet_collection_does_not_depend_on_reading_the_packet(self):
        for suffix in ("reachable", "after_hours"):
            page = SCENES[route.H + "epilogue." + suffix]["Nodes"][0]
            receipts = [p for p in page["Paragraphs"] if house.BET_LOST in p.get("Requires", ())]
            self.assertTrue(receipts)
            for receipt in receipts:
                self.assertIn(house.BET_LOST, receipt["Requires"])
                self.assertNotIn(house.BUNDLE, receipt["Requires"])
                self.assertNotIn(house.BET_COLLECTED, receipt["Requires"])

    def test_morevet_death_has_no_live_entry_or_unguarded_incoming_edge(self):
        for event in SCENES.values():
            nodes = {n['Id']: n for n in event['Nodes']}
            for absent_id in nodes:
                if not absent_id.endswith('.morevet_absent'):
                    continue
                living_id = absent_id.removesuffix('.morevet_absent')
                self.assertIn(living_id, nodes)
                for source in nodes.values():
                    living = [a for a in source['Choices'] if a.get('Next') == living_id]
                    absent = [a for a in source['Choices'] if a.get('Next') == absent_id]
                    for answer in living:
                        self.assertIn(route.MOREVET_DEAD, answer['Forbids'])
                    for answer in absent:
                        self.assertIn(route.MOREVET_DEAD, answer['Requires'])
                        self.assertTrue(available(answer, set(answer['Requires'])))
                    self.assertEqual(bool(living), bool(absent))
        for sid in (house.B + 'honeyed_tongue', house.B + 'morevet_laughs'):
            self.assertIn(route.MOREVET_DEAD, SCENES[sid]['Forbids'])

    def test_folded_discovery_requires_current_body(self):
        for event in SCENES.values():
            for node in event["Nodes"]:
                for answer in node["Choices"]:
                    if answer.get("Next") in ("chiv", "b_chiv"):
                        self.assertIn("chivarro.present_now", answer["Requires"])

    def test_failed_sale_memories_do_not_award_a_sale(self):
        event = SCENES[house.L + 'the_courier']
        nodes = {n['Id']: n for n in event['Nodes']}
        for nid in ('reply.con_blown', 'b_offer.con_blown'):
            self.assertIn(nid, nodes)
            incoming = [a for n in nodes.values() for a in n['Choices'] if a.get('Next') == nid]
            self.assertTrue(incoming)
            self.assertTrue(all(route.BLOWN in a['Requires'] for a in incoming))
            self.assertFalse(any(route.HANDED in a['Set'] for a in nodes[nid]['Choices']))


    def test_court_question_has_local_answers_before_packet_continues(self):
        event = SCENES[house.COURIER]
        for node_id in ("b_lady", "b_lady_hiding"):
            for lover, closed in ((False, False), (True, False), (True, True)):
                flags = {route.COMMITTED}
                if closed:
                    flags.add("noct.closed")
                if lover:
                    flags.add("noct.complete")
                nodes = {n["Id"]: n for n in event["Nodes"]}
                question = nodes[node_id]
                self.assertEqual("b_news", select_answer(question["Choices"], (('b_news', False, None, None, (), ('herrax.morevet_dead',)),), expected_position=0)["Next"])
                self.assertEqual("b_news.morevet_absent", select_answer(question["Choices"], (('b_news.morevet_absent', False, None, None, ('herrax.morevet_dead',), ()),), expected_position=1)["Next"])
                choices = [a for a in question["Choices"][2:] if available(a, flags)]
                self.assertIn(contract_identities(choices),
                        {3: ((('court_reply_truth',
                               None,
                               None,
                               False,
                               ('noct.complete',),
                               ('noct.closed',)),
                              ('court_reply_evade', None, None, False, (), ()),
                              ('court_reply_refuse', None, None, False, (), ())),
                             (('court_reply_evade', None, None, False, (), ()),
                              ('court_reply_refuse', None, None, False, (), ()),
                              ('court_reply_none',
                               None,
                               None,
                               False,
                               ('noct.complete', 'noct.closed'),
                               ())),
                             (('court_reply_none', None, None, False, (), ('noct.complete',)),
                              ('court_reply_evade', None, None, False, (), ()),
                              ('court_reply_refuse', None, None, False, (), ())))}[3])
                truth = next(a for a in choices if house.L + "court.truth" in a["Set"])
                self.assertEqual(lover and not closed, house.L + "court.lover" in truth["Set"])
                self.assertEqual(closed, house.L + "court.former" in truth["Set"])
                for answer in choices:
                    receipt = nodes[answer["Next"]]
                    self.assertTrue(any(available(a, flags) and a.get("Next", "").startswith("b_news") for a in receipt["Choices"]))

    def test_morevet_absence_has_separate_observer_channel(self):
        night = SCENES[route.H + 'madam.the_night']
        source = next(n for n in night['Nodes'] if n['Id'] == 'start')
        for dead in (False, True):
            flags = {route.BAIT} | ({route.MOREVET_DEAD} if dead else set())
            selected = [a['Next'] for a in source['Choices'] if available(a, flags)]
            self.assertEqual(selected, ['arch.morevet_absent' if dead else 'arch'])

    def test_all_four_briefs_have_reachable_default_nodes(self):
        folder = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/herrax"
        files = list(folder.glob("*.json"))
        scenes = {scene["Id"]: scene for scene in fresh_story()["Scenes"]}
        self.assertTrue(files)
        for brief in files:
            data = json.loads(brief.read_text(encoding="utf-8-sig"))
            sid, nid = declared_host(brief.stem, data, scenes)
            with self.subTest(brief=brief.stem, scene=sid, node=nid):
                self.assertIn(nid, reachable_nodes(scenes[sid]))
                self.assertEqual({"Id": data["commander_variants"]}["Id"], ["a man", "a woman"])





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
