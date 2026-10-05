"""E-Q7-18 temporal assertions and optimistic producer floors."""
from tests.story_fixture import fresh_story
import copy
import json
from pathlib import Path
import unittest

from tools import timeline_contract_lint as lint


def scene(sid, requires=(), delay=0, effects=(), groups=()):
    return dict(Id=sid, Requires=list(requires), DelayHours=delay,
                RequiresAnyGroups=[list(g) for g in groups],
                Nodes=[dict(Id="start", Text="a week", Choices=[dict(Set=list(effects))])])


class TimelineContractTests(unittest.TestCase):
    def test_delay_clock_uses_producers_not_sum_and_all_held_or_inputs(self):
        s = scene("callback", ("origin",), 24, groups=(("paid", "found"),))
        self.assertEqual(lint.arrival_hour(s, {"origin", "paid"}, {"origin": 0, "paid": 72}), 96)
        self.assertEqual(lint.arrival_hour(s, {"origin", "found"}, {"origin": 0, "found": 48}), 72)
        self.assertEqual(lint.arrival_hour(s, {"origin", "paid", "found"},
                                          {"origin": 0, "paid": 72, "found": 120}), 144)
        with self.assertRaisesRegex(ValueError, "OR producer"):
            lint.arrival_hour(s, {"origin"}, {"origin": 0})
        s["RequiresAny"] = ["optional_native"]
        self.assertEqual(lint.arrival_hour(s, {"origin", "paid", "optional_native"},
                                          {"origin": 0, "paid": 72, "optional_native": 500}), 96)

    def test_separate_post_coronation_max_and_mourning_min(self):
        post = dict(origins=["coronation"], maximum_hours=168)
        widow = dict(origins=["entry"], minimum_hours=168)
        self.assertIn("exceeds", lint.check_age(post, {"coronation"}, {"coronation": 300}, 504))
        self.assertIn("below", lint.check_age(widow, {"entry"}, {"entry": 0}, 78))
        for contract, origin in [(post, "coronation"), (widow, "entry")]:
            self.assertIsNone(lint.check_age(contract, {origin}, {origin: 0}, 168))

    def test_missing_future_negative_and_both_origins(self):
        c = dict(origins=["first", "second"], minimum_hours=168)
        for times in ({}, {"first": -1}, {"first": 201}):
            self.assertIn("timestamp", lint.check_age(c, {"first"}, times, 200))
        self.assertIn("missing origin", lint.check_age(c, set(), {}, 200))
        self.assertIsNone(lint.check_age(c, {"first"}, {"first": 0}, 200))
        self.assertIsNone(lint.check_age(c, {"second"}, {"second": 0}, 200))
        self.assertIn("below", lint.check_age(c, {"first", "second"}, {"first": 0, "second": 100}, 200))

    def test_actual_producer_chains_or_and_aborts(self):
        story = {"Etudes": {"native": "guid"}, "Derived": {"route": [["paid"], ["found"]]},
                 "Scenes": [scene("first", ("native",), 24, ("paid",)),
                            scene("alternate", ("native",), 48, ("found",)),
                            scene("next", ("route",), 48, ("done",)),
                            scene("callback", ("done", "first"), 12)]}
        times, trace = lint.producer_floors(story)
        self.assertEqual(times["callback"], 84)
        self.assertEqual(trace["done"]["scene"], "next")
        mutated = copy.deepcopy(story)
        mutated["Scenes"][0]["Nodes"][0]["Choices"][0]["Abort"] = True
        # Abort effects persist, but completion is not a producer.
        times, _ = lint.producer_floors(mutated)
        self.assertIn("paid", times)
        self.assertNotIn("first", times)
        self.assertNotIn("callback", times)

    def test_requires_any_availability_does_not_reset_the_delay_clock(self):
        first = scene("origin-page", ("native",), 24, ("origin",))
        later = scene("late-page", ("native",), 200, ("late",))
        callback = scene("callback", ("origin",), 48, ("done",))
        callback["RequiresAny"] = ["late"]
        story = {"CompletedQuests": {"native": "guid"}, "Scenes": [first, later, callback]}
        times, _ = lint.producer_floors(story)
        self.assertEqual(times["done"], 200)
        self.assertEqual(lint.arrival_hour(callback, {"origin", "late"}, {"origin": 24, "late": 200}, 200), 200)

    def test_calendar_cannot_be_inferred_from_campaign_hours(self):
        c = dict(origins=["offering"], calendar_witness="winter")
        self.assertEqual(lint.check_age(c, {"offering"}, {"offering": 0}, 8760), "missing calendar witness")
        self.assertIsNone(lint.check_age(c, {"offering", "winter"}, {"offering": 0}, 24))

    def test_contract_drift_and_qualified_text(self):
        c = {"contracts": [dict(finding="test:001", scene="callback", source=["fixture"],
                                 claim="a week", origins=["origin"], minimum_hours=168)]}
        story = {"Scenes": [scene("callback", ("origin",), 24)]}
        self.assertEqual(len(lint.lint(story, c)["review"]), 1)
        story["Scenes"][0]["Nodes"][0]["Text"] = "since the race"
        self.assertEqual(lint.lint(story, c)["findings"][0]["status"], "no_change_needed")
        c["contracts"][0]["minimum_hours"] = -1
        self.assertTrue(lint.lint(story, c)["hard"])

    def test_every_mapped_finding_has_a_contract(self):
        root = Path(__file__).resolve().parents[1]
        backlog = json.loads((root / "tools/engine_backlog.json").read_text(encoding="utf-8"))
        expected = next(i["finding_ids"] for i in backlog["items"] if i["id"] == "E-Q7-18")
        contracts = json.loads(lint.DEFAULT.read_text(encoding="utf-8"))["contracts"]
        self.assertCountEqual(expected, [c["finding"] for c in contracts])

    def test_live_composites_rebuild_after_return_and_later_refusal(self):
        prepare = scene("prepare", ("dead",), 24, ("returned",))
        callback = scene("callback", ("returned",), 48, ("done",))
        callback["Forbids"] = ["absent"]
        refuse = scene("refuse", ("returned",), 0, ("refused",))
        story = {"Etudes": {"dead": "guid"},
                 "Derived": {"absent": [["dead"]], "eligible": [["returned"]]},
                 "DerivedForbids": {"absent": ["eligible"], "eligible": ["refused"]},
                 "Scenes": [prepare, callback, refuse]}
        schedule = dict(name="return", native=["dead"], origins=["returned"], minimum_hours=48,
                        steps=[dict(scene="prepare", want=["returned"]), dict(scene="callback", want=["done"])])
        witness = lint.replay_schedule(story, schedule)
        self.assertEqual(witness["hour"], 72)
        self.assertIsNone(witness["failure"])
        schedule["steps"].insert(1, dict(scene="refuse", want=["refused"]))
        with self.assertRaisesRegex(ValueError, "forbidden history: callback"):
            lint.replay_schedule(story, schedule)

    def test_shipped_binding_schedules_and_mutated_waits(self):
        from expansion import make_expansion
        story = fresh_story()
        contracts = json.loads(lint.DEFAULT.read_text(encoding="utf-8"))
        for schedule in contracts["schedules"]:
            witness = lint.replay_schedule(story, schedule)
            self.assertEqual(witness["hour"], 168, witness)
            self.assertIsNone(witness["failure"], witness)
        for sid, delay, schedule_name in [
                ("anevia.trickster.gone.fetched_gate", 48, "called-fetched"),
                ("anevia.trickster.gone.commit", 6, "paid-widow")]:
            with self.subTest(scene=sid):
                mutated = copy.deepcopy(story)
                next(s for s in mutated["Scenes"] if s["Id"] == sid)["DelayHours"] = delay
                schedule = next(s for s in contracts["schedules"] if s["name"] == schedule_name)
                self.assertIsNotNone(lint.replay_schedule(mutated, schedule)["failure"])
        schedule = copy.deepcopy(next(s for s in contracts["schedules"] if s["name"] == "called-fetched"))
        schedule["resources"] = {"Favors": 0}
        with self.assertRaisesRegex(ValueError, "affordable"):
            lint.replay_schedule(story, schedule)
        schedule = copy.deepcopy(contracts["schedules"][0])
        schedule["native"].append("anevia.trickster.primed")
        with self.assertRaisesRegex(ValueError, "authored schedule seed"):
            lint.replay_schedule(story, schedule)


if __name__ == "__main__":
    unittest.main()
