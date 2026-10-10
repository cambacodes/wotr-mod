"""Route-source conversations and cuts; shared generated guards are escalated."""
import itertools
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from storylines import galfrey_trickster as g, galfrey_kitrane as k



def saved_answer(answers, ordinal):
    """Read an answer by its preserved save order, independently of wording."""
    if ordinal < 0:
        ordinal += len(answers)
    for position, answer in enumerate(answers):
        if position == ordinal:
            return answer
    raise AssertionError(('missing saved answer', ordinal))

class GalfreyRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenes = {s["Id"]: s for s in g.SCENES + k.SCENES}

    def holds(self, key, flags):
        if key.startswith("!"):
            return not self.holds(key[1:], flags)
        if key in flags:
            return True
        return any(all(self.holds(x, flags) for x in group)
                   for group in g.DERIVED.get(key, []))

    def traverse(self, event, flags):
        """Explore every selectable answer and both outcomes of skill checks."""
        nodes = {n["Id"]: n for n in event["Nodes"]}
        pending = [(event["Nodes"][0]["Id"], frozenset(flags))]
        visited = set()
        reached = set()
        while pending:
            nid, state = pending.pop()
            if (nid, state) in visited:
                continue
            visited.add((nid, state))
            node = nodes[nid]
            reached.add(node["Id"])
            choices = [c for c in node["Choices"]
                       if all(self.holds(x, state) for x in c.get("Requires", []))
                       and not any(self.holds(x, state) for x in c.get("Forbids", []))]
            self.assertTrue(choices, (event["Id"], nid, sorted(state)))
            for choice in choices:
                after = state | frozenset(choice.get("Set", []))
                destinations = ([choice["Check"][b] for b in ("Success", "Failure")]
                                if choice.get("Check") else [choice.get("Next")])
                pending.extend((dest, after) for dest in destinations if dest)
        return reached

    def test_deathbed_name_and_carrier_histories_have_answers(self):
        for met, seed, manuscripts, irabeth, rank in itertools.product((False, True), repeat=5):
            flags = {"trickster", "iomedae.closed", "seelah_dead"}
            flags.update(x for x, on in ((g.MET, met), (g.CROWS_MOOTED, seed),
                         (g.MANU, manuscripts), ("irabeth_dead", irabeth), (g.KC_KEPT, rank)) if on)
            reached = self.traverse(self.scenes[g.OFFER], flags)
            if not met:
                self.assertIn("watch.name_supplied", reached)
                self.assertNotIn("watch", reached)

    def test_source_returns_do_not_require_unrelated_open_relationships(self):
        for sid in (g.P + "return.kitrane", g.P + "return.kitrane_scarred",
                    g.P + "return.kitrane_stall", g.P + "return.kitrane_scarred_stall"):
            for service, cost in itertools.product((False, True), (None, g.ALONE, g.LATE_FOUND)):
                flags = {"iomedae.closed", "irabeth_dead", g.EULOGY_TRUE}
                if service:
                    flags.add(g.JOINED)
                if cost:
                    flags.add(cost)
                reached = self.traverse(self.scenes[sid], flags)
                if not service:
                    self.assertNotIn("why", reached)
                    self.assertIn("why.chosen_late", reached)

    def test_unpaid_preparation_names_crows_supplies(self):
        unpaid = self.traverse(self.scenes[g.P + 'iz.alone'], {g.CROWS_MOOTED, g.KC_KEPT})
        self.assertIn('letter3.crows_supplies', unpaid)
        self.assertNotIn('letter3', unpaid)
        paid = self.traverse(self.scenes[g.P + 'iz.alone'], {g.E_MOOTED, g.P + 'standing_orders.paid'})
        self.assertIn('letter3', paid)
        self.assertNotIn('letter3.crows_supplies', paid)

    def test_four_slots_resume_original_aftermaths_without_effects(self):
        directory = Path(__file__).parents[1] / "tools/route_packs/explicit_slots/galfrey"
        briefs = list(directory.glob("*.json"))
        self.assertEqual(4, len(briefs))
        for path in briefs:
            brief = json.loads(path.read_text(encoding="utf-8"))
            scene = self.scenes[brief["continuity"]["source_scene"]]
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            slot = nodes[brief["slot_id"]]
            self.assertEqual(brief["slot_id"], saved_answer(nodes[brief["continuity"]["insert_after"]]["Choices"], 0)["Next"])
            self.assertEqual(brief["continuity"]["resume_at"], saved_answer(slot["Choices"], 0)["Next"])
            self.assertEqual([], saved_answer(slot["Choices"], 0)["Set"])

    def test_tent_collects_deferred_kiss_and_returns_from_drill(self):
        for suffix in ('', '_stall'):
            scene = self.scenes[g.P + 'visit.tent' + suffix]
            reached = self.traverse(scene, {g.P + 'reel_kiss_saved', k.CROWS_ORDER})
            self.assertTrue({'armour', 'majesty', 'drill'} <= reached)
            self.assertNotIn('armour.no_deferred_kiss', reached)
            drill = next(n for n in scene['Nodes'] if n['Id'] == 'drill')
            self.assertTrue(all({g.P + 'tent_seen', g.P + 'morning_drill'} <= set(c['Set']) for c in drill['Choices']))

    def test_dead_commander_keeps_her_independent_political_future(self):
        scene = self.scenes[g.P + 'epilogue.widow']
        self.assertIn('sacrifice', scene['Requires'])
        paras = scene['Nodes'][0]['Paragraphs']
        for outcome in (g.CROWN, g.FOREVER):
            reader, = [p for p in paras if outcome in p['Requires']]
            self.assertEqual(reader['Requires'], [outcome])
            self.assertEqual(reader['Forbids'], [])
        self.assertTrue(all(not c['Set'] for n in scene['Nodes'] for c in n['Choices']))

    def test_late_rescue_does_not_receive_preparation_credit(self):
        for suffix in ('', '_stall'):
            reached = self.traverse(self.scenes[g.P + 'kitrane.king' + suffix], {g.ALONE, g.LATE_FOUND})
            self.assertIn('made', reached)
            self.assertNotIn('made.prepared_alone', reached)

    def test_living_waits_keep_the_four_day_trial(self):
        expected = {"alive.kitrane": 0, "alive.plan": 0, "alive.plan_report": 24,
                    "alive.trial": 0, "alive.trial_report": 96, "alive.oath": 0,
                    "alive.after_no": 48}
        self.assertEqual(expected, {name: self.scenes[g.P + name]["DelayHours"] for name in expected})
        scene = k.ALIVE_UNFINISHED
        self.assertNotIn(scene["Id"], self.scenes)
        self.assertIn(g.COMMITTED, scene["Forbids"])
        self.assertNotIn(g.COMMITTED, scene["Requires"])

    def test_disclosure_requires_irabeth_currently_present(self):
        scene = self.scenes[g.P + 'kitrane.irabeth']
        absent = self.traverse(scene, {g.CROWS_DREZEN})
        self.assertTrue({'disclose', 'irabeth_answer'}.isdisjoint(absent))
        present = self.traverse(scene, {g.CROWS_DREZEN, 'irabeth.present_now'})
        self.assertTrue({'disclose', 'irabeth_answer'} <= present)

    def test_rescue_setup_and_release_agree_across_histories(self):
        prepared = self.traverse(self.scenes[g.BRIEFED_ID], set())
        self.assertTrue({'orders', 'why.drezen', 'take', 'take_supplies'} <= prepared)
        offer = {n['Id']: n for n in self.scenes[g.OFFER]['Nodes']}
        self.assertEqual([c['Next'] for c in offer['read']['Choices']], ['sight', 'offer'])
        self.assertEqual([c['Next'] for c in offer['blind']['Choices']], ['offer_blind'])
        for suffix in ('', '_stall'):
            reached = self.traverse(self.scenes[g.P + 'iz.eulogy' + suffix], {g.P + 'cost.rent_scar'})
            self.assertTrue({'tent', 'done'} <= reached)
        for paid in (False, True):
            flags = {g.CROWS_MOOTED, g.KC_KEPT} | ({g.P + 'standing_orders.paid'} if paid else set())
            reached = self.traverse(self.scenes[g.P + 'iz.alone'], flags)
            self.assertIn('letter3' if paid else 'letter3.crows_supplies', reached)
            self.assertIn('post', reached)

    def test_late_recovery_is_performed_before_she_speaks(self):
        scene = self.scenes[g.P + 'iz.cortege']
        nodes = {n['Id']: n for n in scene['Nodes']}
        self.assertEqual([c['Next'] for c in nodes['bought']['Choices']], ['in'])
        self.assertEqual({c['Next'] for c in nodes['in']['Choices']}, {'flare', 'flare_told', 'flare_told.unworn'})
        for key in ('flare', 'flare_told', 'flare_told.unworn'):
            self.assertEqual({c['Next'] for c in nodes[key]['Choices']}, {'wake', 'wake.unworn'})
        for key in ('wake', 'wake.unworn'):
            self.assertEqual([c['Next'] for c in nodes[key]['Choices']], ['choose', 'rest'])
            self.assertIn(g.CLOSED, saved_answer(nodes[key]['Choices'], 1)['Set'])
        self.assertEqual([c['Next'] for c in nodes['choose']['Choices']], ['sergeant'])
        self.assertIn(g.LATE_FOUND, saved_answer(nodes['sergeant']['Choices'], 0)['Set'])
        self.assertTrue(all(not c['Set'] for c in nodes['rest']['Choices']))

    def test_private_restitution_does_not_require_reclaiming_crown(self):
        for suffix in ('', '_stall'):
            coffin = self.traverse(self.scenes[g.P + 'kitrane.coffin' + suffix], set())
            self.assertTrue({'letter', 'named', 'kept', 'cold', 'belt'} <= coffin)
            crown = self.traverse(self.scenes[g.P + 'kitrane.crown' + suffix], {g.KEPT})
            self.assertTrue({'kept', 'crown', 'end_forever'} <= crown)
            self.assertNotIn('end_crown', crown)
        for ending in ('kitrane', 'sworn', 'late', 'widow'):
            paragraphs = self.scenes[g.P + 'epilogue.' + ending]['Nodes'][0]['Paragraphs']
            self.assertTrue(any(p['Requires'] == [g.FOREVER] and not p['Forbids'] for p in paragraphs))

    def test_rewritten_behavior_rejects_mutated_fixture(self):
        scene = self.scenes[g.P + 'iz.alone']
        choice = next(c for n in scene['Nodes'] if n['Id'] == 'crows'
                      for c in n['Choices'] if c['Next'] == 'letter3.crows_supplies')
        with patch.dict(choice, Next='letter3'):
            with patch.object(self, "_outcome", None), self.assertRaises(AssertionError):
                self.test_unpaid_preparation_names_crows_supplies()


if __name__ == "__main__":
    unittest.main()
