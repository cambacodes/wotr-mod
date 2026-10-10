"""S26 assembly, absence, channel and unresolved-account contracts."""
import copy
import json
from pathlib import Path
import unittest
from tests.structure import without_prose
from tests.story_fixture import fresh_story

from storylines.harem_rows import s26
from tools import rrt_verify, departure_lint

ROOT = Path(__file__).resolve().parents[1]


class S26Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = fresh_story(include_harem=False)
        # The coordinator's export may already contain this discovered row.
        # Build a clean row fixture while preserving every unrelated entry.
        cls.base["Scenes"] = [s for s in cls.base["Scenes"] if s["Id"] != s26.P + "account"]
        cls.base["Books"]["trickster.ledger"]["Entries"] = [
            e for e in cls.base["Books"]["trickster.ledger"]["Entries"] if e["Id"] != s26.P + "account"]
        cls.base["PendingHooks"] = [f for f in cls.base.get("PendingHooks", []) if f != s26.REMEDY]
        cls.story = copy.deepcopy(cls.base)
        s26.register(cls.story, cls.story["Scenes"], {})
        # Simulate the row with the real transitive adapters. Full-export
        # validation belongs to the strict gate, not every absence assertion.
        simulation = dict(cls.story, Scenes=[cls.story["Scenes"][-1]], Counts={})
        keys = set(simulation["Scenes"][0]["Requires"]) | {s26.REPLY}
        keys.update(f for node in simulation["Scenes"][0]["Nodes"] for answer in node["Choices"]
                    for field in ("Requires", "Forbids") for f in answer[field])
        pending = list(keys)
        while pending:
            key = pending.pop()
            for group in cls.story.get("Derived", {}).get(key, []):
                for dependency in group:
                    if dependency not in keys:
                        keys.add(dependency)
                        pending.append(dependency)
        simulation["Derived"] = {k: v for k, v in cls.story["Derived"].items() if k in keys}
        cls.model = rrt_verify.Model(simulation)
        cls.scene = cls.model.by_id[s26.P + "account"]

    def state(self, *extra):
        state = rrt_verify.SimState(5, 1000)
        state.flags.update(("chapter_later", "trickster", "trickster.foresight.accepted",
                            "trickster.foresight.cost.promise", "gesmerha.wintersun_resolved",
                            "gesmerha.trickster.returned", *extra))
        rrt_verify.sim_complete(self.model, state)
        return state

    def test_unromanced_claimant_does_not_need_respondent(self):
        for absent in ("jerribeth.closed", "jerribeth.unavailable", "jerribeth.epoch_unavailable"):
            state = self.state(absent)
            self.assertTrue(rrt_verify.sim_available(self.model, self.scene, state), absent)
            self.assertNotIn(s26.REPLY, state.flags)
        self.assertEqual(self.scene["Participants"], [])
        self.assertEqual(self.scene["Relationship"], "gesmerha")

    def test_live_entry_rejects_closure_later_loss_failed_anchor_and_repeat(self):
        for blocker in ("gesmerha.closed", "gesmerha.epoch_unavailable", "gesmerha.returned_actor_lost",
                        "gesmerha.presence.failed", s26.P + "account.seen", "trickster.failed"):
            self.assertFalse(rrt_verify.sim_available(self.model, self.scene, self.state(blocker)), blocker)
        for remove in ("trickster", "trickster.foresight.accepted", "gesmerha.trickster.returned"):
            state = self.state()
            state.flags.discard(remove)
            rrt_verify.sim_complete(self.model, state)
            self.assertFalse(rrt_verify.sim_available(self.model, self.scene, state), remove)
        state = self.state()
        state.chapter = 6
        self.assertFalse(rrt_verify.sim_available(self.model, self.scene, state))

    def test_only_earned_current_tenant_can_reply(self):
        for flags in ((s26.RETURNED,), (s26.TENANT,), ("jerribeth.committed",)):
            self.assertNotIn(s26.REPLY, self.state(*flags).flags)
        self.assertIn(s26.REPLY, self.state(s26.RETURNED, s26.TENANT).flags)
        for blocker in (s26.HOST, "jerribeth.closed", "jerribeth.epoch_unavailable", "jerribeth.returned_actor_lost",
                        "jerribeth.trickster.parted"):
            self.assertNotIn(s26.REPLY, self.state(s26.RETURNED, s26.TENANT, blocker).flags, blocker)

    def test_no_free_remedy_attitude_or_native_rewrite(self):
        state = self.state(s26.RETURNED, s26.TENANT)
        self.assertNotIn(s26.REMEDY, state.flags)
        root = self.scene["Nodes"][0]["Choices"]
        self.assertEqual(select_answer(root, (('remedy_reserved', False, None, None, ('household.docket.gesmerha_jerribeth.remedy.authorized',), ()),), expected_position=0)["Requires"], [s26.REMEDY])
        self.assertTrue(select_answer(root, ((None, True, None, None, (), ()),), expected_position=2)["Abort"])
        self.assertEqual(select_answer(root, ((None, True, None, None, (), ()),), expected_position=2)["Set"], [])
        writes = {f for node in self.scene["Nodes"] for answer in node["Choices"] for f in answer["Set"]}
        self.assertEqual(writes, {*s26.WITNESSES, s26.P + "jerribeth_reply_heard"})
        for field in ("Relationships", "Etudes", "SelectedAnswers", "CompletedQuests", "Presences", "SeatWomen"):
            self.assertEqual(self.base[field], self.story[field], field)
        self.assertEqual(without_prose(self.base["Scenes"]), without_prose(self.story["Scenes"][:-1]))

    def test_destroyed_clan_cannot_select_surviving_clan_recall(self):
        state = self.state("gesmerha.dead", "soana.forest_dead", "gesmerha.truth", "gesmerha.illusions")
        self.assertIn(s26.CLAN_DESTROYED, state.flags)
        account = next(n for n in self.scene["Nodes"] if n["Id"] == "account")
        available = [a for a in account["Choices"] if all(f in state.flags for f in a["Requires"])
                     and not any(f in state.flags for f in a["Forbids"])]
        self.assertEqual([a["Next"] for a in available], ["destroyed"])

    def test_registration_and_ledger_are_append_only_and_idempotent(self):
        before = copy.deepcopy(self.story)
        s26.register(before, before["Scenes"], {})
        self.assertEqual(before, self.story)
        entry = self.story["Books"]["trickster.ledger"]["Entries"][-1]
        self.assertEqual(entry["Requires"], [s26.P + "account.seen"])
        self.assertEqual(entry["Section"], "Debts")
        self.assertEqual(self.scene["RestAllowance"], "household.protected")
        self.assertFalse(self.scene.get("HouseholdArcStart", False))
        self.assertEqual(self.scene["Chapters"], [5])
        self.assertEqual(self.scene["InteractionHub"], "gesmerha.presence")

    def test_consumer_dictionary_remains_connected_to_later_household_registration(self):
        consumers = {}
        payload = dict(Scenes=[], ForesightConsumers=consumers)
        s26.register(payload, payload["Scenes"], {})
        consumers["later.household.entry"] = "foresight.page_taken"
        self.assertIs(payload["ForesightConsumers"], consumers)
        self.assertEqual(payload["ForesightConsumers"][s26.P + "account"], "foresight.page_taken")
        self.assertIn("later.household.entry", payload["ForesightConsumers"])

    def test_every_history_has_an_answer_and_every_destination_survives(self):
        nodes = {node["Id"]: node for node in self.scene["Nodes"]}
        for truth, illusions, chief in ((a, b, c) for a in (False, True) for b in (False, True) for c in (False, True)):
            state = self.state(*(["gesmerha.truth"] if truth else []),
                               *(["gesmerha.illusions"] if illusions else []),
                               *(["gesmerha.marhevok_rules"] if chief else []))
            for node in nodes.values():
                self.assertTrue(any(all(f in state.flags for f in answer["Requires"])
                                    and not any(f in state.flags for f in answer["Forbids"])
                                    for answer in node["Choices"]), node["Id"])
        for node in nodes.values():
            for answer in node["Choices"]:
                if answer.get("Next"):
                    self.assertIn(answer["Next"], nodes)

    def test_shared_departure_blocker_has_an_exact_reviewable_classification(self):
        # The shared inventory names every merged row, so validate it against
        # the complete export rather than a fixture containing only S26.
        self.assertEqual(departure_lint.check(fresh_story()), [])
        fragment = json.loads((ROOT / "tools/route_packs/harem/s26-departure-surface.json").read_text(encoding="utf-8"))
        data = departure_lint.contracts()
        self.assertTrue(any(surface['scene'] == fragment['surface']['scene']
                            for surface in data['women']['gesmerha']['surfaces']))




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
