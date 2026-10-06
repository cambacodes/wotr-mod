"""Konomi's authored clocks, accounts, choices and slot continuations."""
import json
import os
import unittest
from pathlib import Path

from tools import rrt_verify as verify
from tools import savecompat


class KonomiRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exported = os.environ.get("RRT_KONOMI_TEST_STORY")
        if exported:
            cls.story = json.loads(Path(exported).read_text(encoding="utf-8"))
        else:
            from expansion import make_expansion
            cls.story = make_expansion()
        cls.model = verify.Model(cls.story)
        cls.by = {s["Id"]: s for s in cls.story["Scenes"]}

    def node(self, sid, nid):
        return next(n for n in self.by["konomi." + sid]["Nodes"] if n["Id"] == nid)

    def available_at(self, sid, choice, hour, dispatched=100, reload=False):
        page = self.model.by_id["konomi." + sid]
        state = verify.SimState(5, hour)
        state.flags.update(page["Requires"])
        state.times.update({f: 0 for f in page["Requires"]})
        for flag in choice["Set"]:
            state.flags.add(flag)
            state.times[flag] = dispatched
        if reload:
            saved = json.loads(json.dumps({"chapter": state.chapter, "hour": state.hour,
                "flags": sorted(state.flags), "times": state.times}))
            state = verify.SimState(saved["chapter"], saved["hour"])
            state.flags.update(saved["flags"])
            state.times.update(saved["times"])
        return verify.sim_available(self.model, page, state)

    def test_road_wait_starts_at_payment_and_survives_reload(self):
        choice = self.node("trickster.dismissed.late", "driver")["Choices"][-1]
        self.assertNotIn("konomi.trickster.back_from_the_road", choice["Set"])
        self.assertIn("konomi.trickster.road_sent", choice["Set"])
        for age, expected in ((0, False), (47, False), (48, True)):
            for reload in (False, True):
                self.assertEqual(expected, self.available_at("trickster.dismissed.arrival", choice, 100 + age, reload=reload))

    def test_report_wait_and_letter_fallback_are_separate(self):
        choice = self.node("trickster.never_arrived.accredited", "nerosyan")["Choices"][-1]
        self.assertNotIn("konomi.trickster.arrived", choice["Set"])
        self.assertIn("konomi.trickster.report_sent", choice["Set"])
        for age, expected in ((0, False), (95, False), (96, True)):
            for reload in (False, True):
                self.assertEqual(expected, self.available_at("trickster.never_arrived.arrival", choice, 100 + age, reload=reload))
        fallback = self.by["konomi.trickster.never_arrived.audience_letter"]
        self.assertEqual(96, fallback["DelayHours"])
        self.assertIn("konomi.trickster.never_arrived.audience", fallback["Forbids"])
        self.assertIn("konomi.trickster.returned", fallback["Forbids"])

    def test_same_account_with_or_without_early_credit(self):
        full = -self.node("trickster.never_arrived.rooms", "start")["Choices"][0]["Crusade"]["Amount"]
        early = -self.node("trickster.never_arrived.audience", "start")["Choices"][1]["Crusade"]["Amount"]
        remaining = -self.node("trickster.never_arrived.rooms", "start")["Choices"][3]["Crusade"]["Amount"]
        negotiated = -self.node("trickster.never_arrived.rooms", "haggle")["Choices"][0]["Crusade"]["Amount"]
        negotiated_credit = -self.node("trickster.never_arrived.rooms", "haggle_rest")["Choices"][0]["Crusade"]["Amount"]
        self.assertEqual((250, 225), (full, negotiated))
        self.assertEqual(full, early + remaining)
        self.assertEqual(negotiated, early + negotiated_credit)

    def test_first_supper_earns_only_an_invitation(self):
        close = self.node("trickster.never_arrived.rooms", "stay")["Choices"]
        active = [x for x in close if "trickster.ever" not in x["Forbids"]]
        self.assertTrue(active)
        for answer in active:
            self.assertNotIn("konomi.trickster.rooms_kept", answer["Set"])
            self.assertNotIn("konomi.lovers", answer["Set"])
            self.assertNotEqual("accept", answer["Next"])
        second = self.by["konomi.trickster.never_arrived.second_supper"]
        self.assertEqual(48, second["DelayHours"])
        answers = second["Nodes"][0]["Choices"]
        self.assertEqual(["accept", "business", None], [a["Next"] for a in answers])
        self.assertTrue(answers[-1]["Abort"])
        self.assertIn("konomi.trickster.rooms_kept", answers[0]["Set"])

    def test_privacy_on_direct_and_retry_acceptance(self):
        for nid in ("answer", "courted", "wants"):
            target = self.node("trickster.dismissed.private", nid)
            self.assertIn("seal", target["Text"])
            self.assertIn("seal", target["Choices"][0]["Text"])
        retry = self.node("trickster.dismissed.a_season", "price")
        self.assertIn("Nobody in your chancery opens", retry["Text"])
        self.assertIn("public refusal", retry["Choices"][0]["Text"])

    def test_whole_chains_fit_their_phase_budgets(self):
        names = ["capital_letter", "return_offer", "private_reunion", "lease_offer", "chosen_evening", "private_future_choice"]
        self.assertEqual(408, sum(self.by["konomi." + sid]["DelayHours"] for sid in names))
        names = ["trickster.dismissed.late", "trickster.dismissed.arrival", "trickster.dismissed.terms", "trickster.dismissed.private"]
        self.assertEqual(168, sum(self.by["konomi." + sid]["DelayHours"] for sid in names))
        self.assertEqual(72, self.by["konomi.trickster.dismissed.a_season"]["DelayHours"])

    def test_slot_defaults_and_destinations_have_matching_briefs(self):
        root = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots/konomi"
        slots = []
        for s in self.story["Scenes"]:
            if s.get("Relationship") != "konomi":
                continue
            ids = {n["Id"] for n in s["Nodes"]}
            for n in s["Nodes"]:
                if ".explicit." not in n["Id"]:
                    continue
                slots.append(n["Id"])
                self.assertTrue(n["Text"].startswith("{n}"))
                self.assertIn(n["Choices"][0]["Next"], ids)
                brief = json.loads((root / (n["Id"] + ".json")).read_text(encoding="utf-8"))
                self.assertEqual(["a man", "a woman"], brief["commander_variants"])
        self.assertEqual(8, len(slots))  # Seven moments, plus the retained rooms continuation.

    def test_postwar_legacy_continue_keeps_identity_and_mechanics(self):
        page = self.by["konomi.trickster.epilogue.refused"]
        start = self.node("trickster.epilogue.refused", "start")
        old = start["Choices"][0]
        self.assertEqual("continue", old["Id"])
        self.assertFalse(any(old.get(k) for k in savecompat.EXIT_MECHANICS))
        self.assertIn("konomi.closed", page["Forbids"])
        for node in page["Nodes"]:
            self.assertTrue(all(not ch["Set"] for ch in node["Choices"]))


if __name__ == "__main__":
    unittest.main()
