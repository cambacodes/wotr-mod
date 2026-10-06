"""Replay Eliandra's reviewed history splits against the assembled engine story."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from expansion import make_expansion
from tools.rrt_verify import Model, SimState, sim_available, sim_complete

E = "eliandra.trickster."
LIGHTS = E + "cost.lights_given"
REWARD = E + "cost.reward_returned"
LEAVE = E + "leave_granted"
FLIRT = E + "flirted"


def shown(item, flags):
    return (all(k in flags for k in item.get("Requires", []))
            and not any(k in flags for k in item.get("Forbids", []))
            and all(any(k in flags for k in group)
                    for group in item.get("AnyGroups", [])))


class EliandraPolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = make_expansion()
        cls.model = Model(cls.story)
        cls.scenes = cls.model.by_id

    def state(self, flags, chapter=5):
        state = SimState(chapter, 5000)
        state.flags.update({"trickster", "trickster.ever", "chapter_later",
                            "eliandra.met_ch5", *flags})
        sim_complete(self.model, state)
        return state

    def play(self, suffix, flags=(), choices=None, failure=False, start=None):
        scene = self.scenes[E + suffix]
        nodes = {n["Id"]: n for n in scene["Nodes"]}
        current = start or scene["Nodes"][0]["Id"]
        flags = self.state(flags).flags
        trace = []
        while current:
            self.assertNotIn(current, trace, "Replay loop")
            trace.append(current)
            node = nodes[current]
            open_answers = [(i, a) for i, a in enumerate(node["Choices"])
                            if shown(a, flags)]
            self.assertTrue(open_answers, suffix + "/" + current)
            index = (choices or {}).get(current, open_answers[0][0])
            answer = next((a for i, a in open_answers if i == index), None)
            self.assertIsNotNone(answer, suffix + "/" + current + "/" + str(index))
            flags.update(answer["Set"])
            if answer.get("Check"):
                current = answer["Check"]["Failure" if failure else "Success"]
            else:
                current = answer["Next"]
            flags = self.state(flags).flags
        return flags, set(trace), trace

    def test_eye_treatment_friend_and_romance_complete_separately(self):
        for choices in ({"kiss": 1}, {"eyes": 2}):
            flags, text, _ = self.play("ch5.night_after", {LEAVE, LIGHTS}, choices)
            self.assertIn(E + "eyes_kissed", flags)
            self.assertNotIn(FLIRT, flags)
            self.assertNotIn("eliandra.committed", flags)
            self.assertNotIn("eliandra.closed", flags)
            postwar = self.state(flags, 6)
            self.assertTrue(sim_available(self.model, self.scenes[E + "epilogue.released"], postwar))
            self.assertFalse(sim_available(self.model, self.scenes[E + "epilogue.unasked"], postwar))
        for answer in (0, 1):
            flags, _, trace = self.play("ch5.night_after", {LEAVE, LIGHTS}, {"eyes": answer})
            self.assertTrue({FLIRT, E + "eyes_kissed"} <= flags)
            self.assertIn("right" if answer == 0 else "touch", trace)
        flags, _, _ = self.play("ch5.night_after", {LEAVE, LIGHTS, FLIRT}, {"kiss": 1})
        self.assertIn(FLIRT, flags)  # Friendship does not erase an earlier choice.

    def test_burial_siblings_are_truthful_and_keep_intent(self):
        for buried in (False, True):
            for reply in (1, 2):
                with self.subTest(buried=buried, reply=reply):
                    flags, text, trace = self.play("ch5.lovers",
                        {E + "dead_named", *([E + "buried"] if buried else [])},
                        {"rooms": 2, "herself": reply + (2 if buried else 0)})
                    self.assertIn(E + "lovers.spoken", flags)
                    self.assertEqual(reply == 1, FLIRT in flags)
                    target = "flirt" if reply == 1 else "sleep"
                    self.assertIn(target + ("_buried" if buried else ""), trace)
                    if buried:
                        self.assertNotIn(target, trace)
                        self.assertNotIn("flirt" if reply == 1 else "sleep", trace)

    def test_observation_keeps_stars_and_never_refunds_aurora(self):
        for paid in (False, True):
            flags, text, trace = self.play("ch5.observe",
                {E + "dead_named", *([LEAVE, LIGHTS] if paid else [])}, {"reading": 2 if paid else 1})
            self.assertIn(E + "observed", flags)
            self.assertIn("sky_given" if paid else "sky", trace)
            if paid:
                self.assertNotIn("sky", trace)
                self.assertIn("sky_given", trace)
        for suffix in ("", "_mark"):
            observation = self.scenes[E + "ch5.observe_drezen" + suffix]
            self.assertTrue({LEAVE, E + "no_leave"} <= set(observation["Forbids"]))

    def test_healing_receipt_only_means_witnessed_exceptional_gift(self):
        for returned in (False, True):
            for response in (0, 1):
                for exit in (0, 1):
                    flags, text, trace = self.play("ch5.healer",
                        {E + "dead_named", *([LEAVE, REWARD] if returned else [])},
                        {"talk_returned" if returned else "talk": response,
                         "end_returned" if returned else "end": exit})
                    self.assertEqual(not returned, E + "healing_seen" in flags)
                    if returned:
                        self.assertNotIn("end", trace)
                        self.assertIn("end_returned", trace)
                    ordinary = self.scenes[E + "drezen.ordinary"]["Nodes"][0]
                    open_targets = [a["Next"] for a in ordinary["Choices"] if shown(a, flags)]
                    self.assertEqual(["no_shrine" if returned else "shrine"], open_targets)

    def test_vow_history_respects_all_release_cost_states(self):
        for costs in (set(), {E + "no_leave"}, {LEAVE, LIGHTS},
                      {LEAVE, LIGHTS, REWARD}, {LEAVE, REWARD}):
            for reply in (0, 1):
                flags, text, trace = self.play("ch5.thirteen",
                    {E + "dead_named", *costs}, {"vow": reply})
                self.assertIn(E + "vow_told", flags)
                if LEAVE in costs:
                    self.assertIn("believe_released", trace)
                    self.assertIn("gift_returned" if REWARD in costs else "gift_kept", trace)
                    self.assertNotIn("believe", trace)
                else:
                    self.assertIn("believe", trace)
                    self.assertNotIn("believe_released", trace)

    def test_veil_hypotheticals_are_only_available_before_the_price(self):
        for paid in (False, True):
            for reply in (0, 1):
                flags, text, trace = self.play("ch5.veil",
                    {E + "dead_named", *([LEAVE, LIGHTS] if paid else [])},
                    {"through": reply + (2 if paid else 0)})
                self.assertIn(E + "veil_known", flags)
                self.assertIn(("seam" if reply == 0 else "pray") + ("_given" if paid else ""), trace)
                if paid:
                    self.assertNotIn("seam", trace)
                    self.assertNotIn("pray", trace)

    def test_repaired_flirts_are_intent_without_release_or_commitment(self):
        for suffix in ("", "_drezen", "_drezen_mark"):
            scene = self.scenes[E + "ch5.last_rite" + suffix]
            flirt = scene["Nodes"][0]["Choices"][1]
            self.assertEqual([FLIRT, "eliandra.started"], flirt["Set"])
            self.assertEqual("leave", flirt["Next"])
        flags, _, _ = self.play("ch5.packing", {E + "dead_named", "eliandra.shrine_left"}, {"her": 1})
        self.assertIn(FLIRT, flags)
        self.assertNotIn(LEAVE, flags)
        self.assertNotIn("eliandra.committed", flags)

    def test_all_rite_families_keep_prices_checks_and_prayer_history(self):
        for suffix in ("", "_drezen", "_drezen_mark"):
            for failure in (False, True):
                flags, text, _ = self.play("ch5.last_rite" + suffix,
                    {E + "terms_read"}, {"name": 2}, failure=failure)
                self.assertTrue({LEAVE, LIGHTS} <= flags)
                self.assertEqual(failure, REWARD in flags)
                name = next(n for n in self.scenes[E + "ch5.last_rite" + suffix]["Nodes"] if n["Id"] == "name")
                self.assertEqual([24, 18], [name["Choices"][i]["Check"]["DC"] for i in (1, 2)])
            for choice, cost in ((3, E + "cost.tried_to_cheat"), (4, None)):
                flags, _, _ = self.play("ch5.last_rite" + suffix, {E + "terms_read"}, {"name": choice})
                self.assertIn(E + "no_leave", flags)
                self.assertNotIn(LEAVE, flags)
                self.assertNotIn(LIGHTS, flags)
                if cost:
                    self.assertIn(cost, flags)

    def test_intimacy_cut_and_present_flirt_on_both_hosts(self):
        for suffix in ("", "_mark"):
            for flags in ({LEAVE, LIGHTS, FLIRT}, {LEAVE, REWARD, FLIRT, E + "dead_named"}):
                _, text, trace = self.play("visit.star_heart" + suffix,
                    {*flags, "eliandra.committed"}, {"want": 2, "want_rite": 2})
                self.assertEqual(E + "visit.star_heart" + suffix + ".explicit.1", trace[trace.index("charts") + 1])
                self.assertEqual("morning", trace[trace.index("charts") + 2])
                self.assertNotIn("promise", trace)

    def test_katair_and_lastcall_claim_only_their_earned_histories(self):
        for ending in ("together", "late", "unasked"):
            node = self.scenes[E + "epilogue." + ending]["Nodes"][0]
            paragraph = next(p for p in node["Paragraphs"] if E + "drezen.katair_grave" in p["Requires"])
            self.assertFalse(shown(paragraph, set()))
            self.assertTrue(shown(paragraph, {E + "drezen.katair_grave"}))
        call = self.scenes["eliandra.lastcall.call"]
        daily = next(n for n in call["Nodes"] if n["Id"] == "daily")
        self.assertEqual(call["Nodes"][0]["Choices"][0]["Next"], daily["Id"])
        self.assertIn("eliandra.committed", call["Nodes"][0]["Choices"][0]["Requires"])


if __name__ == "__main__":
    unittest.main()
