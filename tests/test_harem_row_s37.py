"""S37 acceptance walks against the exported runtime payload."""
import copy
import json
from tests.story_fixture import fresh_story
import unittest

from storylines import household_pair_delamere_hepzamirah as row
from tools import rrt_verify as verify


class S37(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.model = verify.Model(cls.story)

    def state(self, respondent=True):
        state = verify.SimState(5, 100)
        state.flags.update(("trickster", "trickster.ever", "trickster.foresight.accepted",
                            "trickster.foresight.cost.promise", "household.table.kept",
                            "delamere.committed", "delamere.trickster.second_hunt_offered",
                            "delamere.trickster.caught", "delamere.trickster.returned",
                            "hepzamirah.trickster.returned"))
        if respondent:
            state.flags.update(("hepzamirah.committed", "hepzamirah.trickster.courier_seen"))
        state.crusade_resources = {"Materials": 300}
        verify.sim_complete(self.model, state)
        return state

    def body(self, step):
        return self.model.by_id[row.key(step)]

    def available(self, step, state):
        verify.sim_complete(self.model, state)
        return verify.sim_available(self.model, self.body(step), state)

    def play(self, step, index, state):
        self.assertTrue(self.available(step, state), step)
        body = self.body(step)
        nodes = {node["Id"]: node for node in body["Nodes"]}
        choice = nodes["start"]["Choices"][index]
        path = [choice]
        while choice["Next"]:
            choice = select_answer(nodes[choice["Next"]]["Choices"], ((None, False, None, None, (), ()),), expected_position=0)
            path.append(choice)
        return verify.sim_play(self.model, body, state, {}, plan=((1, 0, 0, len(path)), path))

    def advance(self, state, hours=48):
        state.hour += hours
        state.rest_spent.clear()
        verify.sim_complete(self.model, state)

    def test_both_primary_tools_and_costs(self):
        for index, proof in ((0, "proof.relic_returned"), (1, "proof.stores_restored")):
            with self.subTest(index=index):
                state = self.state()
                self.assertTrue(self.play("open", 0, state))
                self.assertIn(row.key("goods.equipment_impounded"), state.flags)
                self.assertFalse(self.available("hearing", state))
                self.advance(state, 47)
                self.assertFalse(self.available("hearing", state))
                self.advance(state, 1)
                self.assertTrue(self.play("hearing", index, state))
                self.assertIn(row.key(proof), state.flags)
                self.assertIn(row.key("claim.revoked"), state.flags)
                self.assertIn(row.key("resolved"), state.flags)
                self.assertEqual(state.crusade_resources["Materials"], 300 if index == 0 else 150)
                self.assertEqual(row.key("cost.commander_prize_yielded") in state.flags, index == 0)
                self.assertFalse(self.available("repair", state))
                self.assertEqual(state.rest_spent["household.protected"], 1)

    def test_unsettled_repair_or_final_refusal(self):
        for index in (0, 1):
            state = self.state()
            self.play("open", 0, state)
            self.advance(state)
            self.play("hearing", 2, state)
            self.assertNotIn(row.key("resolved"), state.flags)
            self.assertFalse(self.available("repair", state))
            self.advance(state)
            self.assertTrue(self.play("repair", index, state))
            self.assertIn(row.key("hearing.unsettled"), state.flags)
            self.assertEqual(row.key("resolved") in state.flags, index == 0)
            self.assertEqual(row.key("cost.commander_prize_yielded") in state.flags, index == 0)
            self.assertEqual(row.key("permanent_refusal") in state.flags, index == 1)
            self.assertTrue(verify.route_open(self.model, "delamere", state.flags))
            self.assertTrue(verify.route_open(self.model, "hepzamirah", state.flags))

    def test_suppression_is_permanent_and_aborts_do_nothing(self):
        state = self.state()
        before = copy.deepcopy(state.__dict__)
        self.assertFalse(self.play("open", 2, state))
        self.assertEqual(state.flags - before["flags"], {"household.started"})
        self.assertEqual(state.rest_spent, {})
        self.play("open", 1, state)
        self.advance(state)
        self.assertFalse(self.available("hearing", state))
        self.assertFalse(self.available("repair", state))
        self.assertNotIn(row.key("goods.equipment_impounded"), state.flags)
        for body in row.SCENES:
            abort = select_answer(body["Nodes"][0]["Choices"], ((None, True, None, None, (), ()),), expected_position=-1)
            self.assertTrue(abort["Abort"])
            self.assertEqual(abort["Set"], [])
            self.assertNotIn("Crusade", abort)

    def test_current_attendance_page_path_and_body(self):
        state = self.state(respondent=False)
        self.assertTrue(self.available("open", state))
        self.play("open", 0, state)
        self.advance(state)
        self.assertFalse(self.available("hearing", state))
        state.flags.update(("hepzamirah.committed", "hepzamirah.trickster.courier_seen"))
        self.assertTrue(self.available("hearing", state))
        for flag in ("trickster", "hepzamirah.trickster.returned", "delamere.trickster.returned",
                     "trickster.foresight.accepted"):
            denied = copy.deepcopy(state)
            denied.flags.remove(flag)
            self.assertFalse(self.available("hearing", denied), flag)
        for woman in ("delamere", "hepzamirah"):
            denied = copy.deepcopy(state)
            denied.flags.add(woman + ".closed")
            self.assertFalse(self.available("hearing", denied))
            absent = copy.deepcopy(state)
            absent.flags.add(woman + ".epoch_unavailable")
            self.assertFalse(self.available("hearing", absent))
        denied = self.state(respondent=False)
        denied.flags.add("hepzamirah.closed")
        self.assertTrue(self.available("open", denied))
        denied.flags.add("delamere.closed")
        self.assertFalse(self.available("open", denied))
        denied = copy.deepcopy(state)
        denied.flags.add("sacrifice")
        self.assertFalse(self.available("hearing", denied))
        denied.flags.add("ending.trickster")
        self.assertTrue(self.available("hearing", denied))

    def test_readers_survival_closure_and_all_costs(self):
        def shown(para, flags):
            return (all(f in flags for f in para["Requires"]) and
                    not any(f in flags for f in para["Forbids"]) and
                    all(any(f in flags for f in group) for group in para["AnyGroups"]))
        for woman in ("delamere", "hepzamirah"):
            page = self.model.by_id[woman + ".lastcall.page"]
            paras = [p for p in page["Nodes"][0]["Paragraphs"] if p.get("Id", "").startswith(row.key("reader.lastcall."))]
            self.assertIn(contract_identities(paras),
                    {18: (('household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.resolved.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.resolved.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.known.present_claim.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.known.present_claim.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stone_received.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stone_received.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stores_guarded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stores_guarded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_goods_received.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_goods_received.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_captain_dismissed.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_captain_dismissed.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_guard_claim_yielded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_guard_claim_yielded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_prize_yielded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_prize_yielded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_stores_replaced.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_stores_replaced.returned'),
                          ('household.pair.delamere_hepzamirah.reader.lastcall.delamere.resolved.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.resolved.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.known.present_claim.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.known.present_claim.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stone_received.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stone_received.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stores_guarded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stores_guarded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_goods_received.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_goods_received.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_captain_dismissed.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_captain_dismissed.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_guard_claim_yielded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_guard_claim_yielded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_prize_yielded.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_prize_yielded.returned',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_stores_replaced.living',
                           'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_stores_replaced.returned'))}[18])
            state = self.state()
            state.flags.update([row.key("resolved")] + [row.key("cost." + cost) for cost in row.COSTS])
            for sacrificed, returned, expected in ((False, False, 8), (True, False, 0), (True, True, 8)):
                flags = set(state.flags)
                if sacrificed: flags.add("sacrifice")
                if returned: flags.add("trickster.commander_back")
                self.assertIn(contract_identities([p for p in paras if shown(p, flags)]),
                        {8: (('household.pair.delamere_hepzamirah.reader.lastcall.delamere.resolved.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stone_received.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stores_guarded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_goods_received.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_captain_dismissed.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_guard_claim_yielded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_prize_yielded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_stores_replaced.living'),
                             ('household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.resolved.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stone_received.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stores_guarded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_goods_received.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_captain_dismissed.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_guard_claim_yielded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_prize_yielded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_stores_replaced.returned'),
                             ('household.pair.delamere_hepzamirah.reader.lastcall.delamere.resolved.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stone_received.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_stores_guarded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.delamere_goods_received.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_captain_dismissed.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.hepzamirah_guard_claim_yielded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_prize_yielded.returned',
                              'household.pair.delamere_hepzamirah.reader.lastcall.delamere.cost.commander_stores_replaced.returned'),
                             ('household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.resolved.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stone_received.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_stores_guarded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.delamere_goods_received.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_captain_dismissed.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.hepzamirah_guard_claim_yielded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_prize_yielded.living',
                              'household.pair.delamere_hepzamirah.reader.lastcall.hepzamirah.cost.commander_stores_replaced.living')),
                         0: ((),)}[expected])
            state.flags.add(woman + ".closed")
            verify.sim_complete(self.model, state)
            self.assertFalse(any(shown(p, state.flags) for p in paras))
        records = {e["Id"]: e for e in self.story["Books"]["trickster.ledger"]["Entries"]}
        for destination in ("ledger", "seating"):
            entry = records[row.key("reader." + destination)]
            self.assertFalse(any(".closed" in f or f == "sacrifice" for p in entry["Lines"] for f in p["Forbids"]))
            self.assertTrue(all(any(row.key("cost." + cost) in p["Requires"] for p in entry["Lines"]) for cost in row.COSTS))

    def test_only_row_witnesses_no_policy_or_sibling_writes(self):
        for body in row.SCENES:
            self.assertEqual(body["RestAllowance"], "household.protected")
            self.assertTrue(body["ManualOnly"])
            for node in body["Nodes"]:
                self.assertNotIn("Paragraphs", node)
                for choice in node["Choices"]:
                    self.assertIsNone(choice.get("Check"))
                    for flag in choice["Set"]:
                        self.assertTrue(flag.startswith(row.PREFIX))
                        self.assertFalse(any(token in flag for token in (".attitude.", ".enmity.", ".reconciled.", ".closed", ".committed", ".stance.")))

    def test_exact_terminal_contract_and_reload(self):
        expected = {
            ("open", "impounded"): "open.seen open.ready known.present_claim goods.equipment_impounded",
            ("open", "suppressed"): "open.seen open.suppressed known.present_claim permanent_refusal",
            ("hearing", "relic"): "hearing.seen proof.relic_returned claim.revoked resolved cost.delamere_stone_received cost.hepzamirah_captain_dismissed cost.commander_prize_yielded",
            ("hearing", "stores"): "hearing.seen proof.stores_restored claim.revoked resolved cost.delamere_stores_guarded cost.hepzamirah_guard_claim_yielded cost.commander_stores_replaced",
            ("hearing", "unsettled"): "hearing.seen hearing.unsettled unsettled",
            ("repair", "returned"): "repair.seen proof.goods_returned claim.revoked resolved cost.delamere_goods_received cost.hepzamirah_captain_dismissed cost.commander_prize_yielded",
            ("repair", "refused"): "repair.seen repair.declined permanent_refusal",
        }
        for (step, terminal), flags in expected.items():
            node = next(n for n in self.body(step)["Nodes"] if n["Id"] == terminal)
            self.assertEqual(select_answer(node["Choices"], ((None, False, None, None, (), ()),), expected_position=0)["Set"], [row.key(f) for f in flags.split()])
        state = self.state()
        self.play("open", 0, state)
        self.advance(state)
        self.play("hearing", 2, state)
        saved = json.loads(json.dumps(dict(flags=sorted(state.flags), times=state.times,
                                          hour=state.hour, rest_spent=state.rest_spent)))
        restored = verify.SimState(5, saved["hour"])
        restored.flags.update(saved["flags"])
        restored.times.update(saved["times"])
        restored.rest_spent.update(saved["rest_spent"])
        self.assertFalse(self.available("repair", restored))
        self.advance(restored)
        self.assertTrue(self.play("repair", 0, restored))
        self.assertIn(row.key("proof.goods_returned"), restored.flags)




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
