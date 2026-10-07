"""S17 contract: bodies, exact outcomes, one retry, no intimacy or route writes."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import s17
from tools import savecompat
from tools import rrt_verify as verify


class S17Tests(unittest.TestCase):
    def setUp(self):
        self.payload = {"Scenes": [], "Etudes": {}}
        s17.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.scenes = {s["Id"].removeprefix(s17.P): s for s in self.payload["Scenes"]}

    def test_registration_is_append_only_and_repeatable(self):
        old = copy.deepcopy(self.payload)
        s17.register(self.payload, self.payload["Scenes"], self.payload["Etudes"])
        self.assertEqual(old, self.payload)
        self.assertEqual([], savecompat.check(self.payload, savecompat.inventory(old)))

    def test_current_presence_and_real_contact_on_both_steps(self):
        for scene in self.scenes.values():
            self.assertTrue(set(s17.BODY + s17.ELIGIBLE) <= set(scene["Requires"]))
            self.assertTrue(set(s17.BLOCKED) <= set(scene["Forbids"]))
            self.assertEqual(scene["Participants"], ["vellexia", "shamira"])
            self.assertNotIn("ContactUnit", scene)  # Rules.IsTableScene forbids it.
            self.assertNotIn("AdditionalContactUnits", scene)
            self.assertNotIn("Remote", scene)
            self.assertNotIn("Nocticula", str(scene["Participants"]))
        self.assertEqual(self.payload["DerivedOpenRoutes"][s17.P + "ready"], s17.PAIR)
        self.assertEqual(self.payload["Derived"][s17.P + "ready"], [s17.ELIGIBLE + s17.BODY])
        self.assertEqual(s17.BODY_CONTACTS, ["a32a07903e428d34cb0e98a804d40569",
                                            "66e12264eaf6bf74196e20a9d7619cd2"])

    def test_page_live_path_venue_and_budget(self):
        for step, scene in self.scenes.items():
            self.assertTrue({"trickster", "trickster.now", "foresight.page_taken",
                             "household.stance_eligible", "household.table.kept"} <= set(scene["Requires"]))
            self.assertEqual((scene["MinChapter"], scene["MaxChapter"], scene["Chapters"]), (5, 5, [5]))
            self.assertEqual(scene["Areas"], ["2570015799edf594daf2f076f2f975d8"])
            self.assertEqual(scene["InteractionHub"], "household.table")
            self.assertEqual(scene["RestAllowance"], "household.protected")
            self.assertEqual(scene["HouseholdCategory"], "protected")
            self.assertEqual(scene["HouseholdWitness"], s17.P + step + ".seen")
        retry = self.scenes["retry"]
        self.assertEqual(retry["DelayHours"], 48)
        self.assertIn(s17.P + "settle.failed", retry["Requires"])
        self.assertTrue({s17.P + "retry.seen", s17.P + "settle.kept",
                         s17.P + "settle.declined"} <= set(retry["Forbids"]))
        self.assertEqual(self.scenes["settle"]["DelayHours"], 0)

    def test_roots_keep_indices_checks_and_abort(self):
        self.assertEqual([n["Id"] for n in self.scenes["settle"]["Nodes"]][:5],
                         ["start", "floor", "botched", "performance", "declined"])
        self.assertEqual([n["Id"] for n in self.scenes["retry"]["Nodes"]][:4],
                         ["start", "performance", "failed", "declined"])
        for scene in self.scenes.values():
            choices = scene["Nodes"][0]["Choices"]
            self.assertEqual(len(choices), 4)
            self.assertTrue(all(not c["Set"] for c in choices))
            self.assertTrue(choices[3]["Abort"])
            self.assertIsNone(choices[3]["Next"])
        self.assertEqual(self.scenes["settle"]["Nodes"][0]["Choices"][0]["Check"],
                         dict(Skill="CheckDiplomacy", DC=22, Success="floor", Failure="botched", CommanderOnly=True))

    def test_exhaustive_terminal_witnesses_and_graph(self):
        for step, scene in self.scenes.items():
            nodes = {n["Id"]: n for n in scene["Nodes"]}
            success = ["floor_end", "performance_end"] if step == "settle" else ["performance_end"]
            failure = "botched" if step == "settle" else "failed"
            expected = {name: {s17.P + step + ".seen", s17.P + step + ".kept", *s17.DEED}
                        for name in success}
            expected[failure] = {s17.P + step + ".seen", s17.P + step + ".failed", s17.P + "stage.answer_cut_off"}
            expected["declined"] = {s17.P + step + ".seen", s17.P + step + ".declined"}
            for node in nodes.values():
                self.assertNotIn("Paragraphs", node)
                self.assertTrue(node["Choices"])
                for choice in node["Choices"]:
                    if choice["Next"]:
                        self.assertIn(choice["Next"], nodes)
                        self.assertFalse(choice["Set"])
                    elif node["Id"] != "start":
                        self.assertEqual(set(choice["Set"]), expected[node["Id"]])
                    self.assertTrue(all(flag.startswith(s17.P) for flag in choice["Set"]))
                    self.assertFalse(any(word in flag for flag in choice["Set"]
                                         for word in ("attitude", "enmity", "reconciled", "committed", "partner_stance")))
                self.assertLess(len(node["Text"].split()), 180)
            self.assertFalse(any("explicit" in nid for nid in nodes))

    def test_both_successes_require_both_answers_and_bounded_costs(self):
        self.assertEqual(s17.STAGES["respect"], [s17.DEED[:-1]])
        self.assertEqual(set(s17.STAGES), {"rival", "respect"})
        self.assertEqual(s17.FAILURE_CLAIMANT, ("shamira", "vellexia"))
        for scene in self.scenes.values():
            self.assertEqual(scene["ForbidOverrides"], {
                "vellexia.harem.enmity.shamira": "vellexia.harem.reconciled.shamira",
                "shamira.harem.enmity.vellexia": "shamira.harem.reconciled.vellexia"})
            for node in scene["Nodes"]:
                for choice in node["Choices"]:
                    if s17.P + "stage.held" in choice["Set"]:
                        self.assertTrue(set(s17.DEED) <= set(choice["Set"]))
                    if any(f.endswith(".failed") for f in choice["Set"]):
                        self.assertFalse(set(s17.DEED) & set(choice["Set"]))

    def test_selection_rejects_stale_returns_and_nonbodily_histories(self):
        # Use the exported route contracts, including their epoch vetoes; even
        # stale ready/present flags cannot bypass current participant RouteOpen.
        base = json.loads((Path(__file__).resolve().parents[1] / "development/Story.json").read_text(encoding="utf-8-sig"))
        fixture = copy.deepcopy(self.payload)
        fixture["Relationships"] = {key: base["Relationships"][key]
                                    for key in ("household", "vellexia", "shamira")}
        fixture["RestAllowances"] = base["RestAllowances"]
        model = verify.Model(fixture)
        scene = model.by_id[s17.P + "settle"]

        def state():
            st = verify.SimState(5, 1000)
            st.flags.update(scene["Requires"])
            return st

        self.assertTrue(verify.sim_available(model, scene, state()))
        for missing in ("foresight.page_taken", "trickster.now", *s17.BODY):
            st = state()
            st.flags.remove(missing)
            self.assertFalse(verify.sim_available(model, scene, st), missing)
        for blocked in (*s17.BLOCKED, "vellexia.epoch_unavailable", "shamira.epoch_unavailable"):
            st = state()
            st.flags.update([blocked, "vellexia.trickster.returned", "shamira.trickster.returned"])
            self.assertFalse(verify.sim_available(model, scene, st), blocked)
        for chapter in (3, 4, 6):
            st = state()
            st.chapter = chapter
            self.assertFalse(verify.sim_available(model, scene, st))
        for direction in s17.ENMITIES:
            st = state()
            st.flags.add(direction)
            self.assertFalse(verify.sim_available(model, scene, st))
            st.flags.add(scene["ForbidOverrides"][direction])
            self.assertTrue(verify.sim_available(model, scene, st))
        retry = model.by_id[s17.P + "retry"]
        st = state()
        st.flags.update(retry["Requires"])
        st.times[s17.P + "settle.failed"] = 953
        self.assertFalse(verify.sim_available(model, retry, st))
        st.hour = 1001
        self.assertTrue(verify.sim_available(model, retry, st))
        for outcome in ("settle.kept", "settle.declined", "retry.seen"):
            closed = copy.deepcopy(st)
            closed.flags.add(s17.P + outcome)
            self.assertFalse(verify.sim_available(model, retry, closed), outcome)


if __name__ == "__main__":
    unittest.main()
