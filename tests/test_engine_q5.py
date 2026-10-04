"""ENGINE-Q5: current power earns returns; RouteOpen controls physical presence."""
import copy
import unittest

from storylines import earned_presence as ep
from tools import earned_presence_lint as lint


def fixture():
    return {
        "Relationships": {"her": {"ClosedFlag": "her.closed", "UnavailableFlags": ["her.dead", "her.gone"],
                                    "UnavailableOverrides": {"her.dead": "her.returned", "her.gone": "her.returned"},
                                    "TricksterAccess": {"dead": {"Device": "her.device", "Returned": "her.returned"}}}},
        "Derived": {}, "Latches": {},
        "Scenes": [{"Id": "her.device", "Relationship": "her", "Requires": ["trickster.ever"],
                    "Nodes": [{"Id": "end", "Choices": [{"Set": ["her.returned"], "Revive": "her"}]}]}],
        "Presences": {"her.presence": {"Requires": ["trickster.ever", "her.returned"]}},
    }


class LiveReturnTests(unittest.TestCase):
    def test_historical_return_and_revival_are_rejected(self):
        s = fixture()
        errors = lint.producer_presence_errors(s)
        self.assertTrue(any(x.startswith("T7 her.device:") for x in errors))
        self.assertTrue(any("choice[0]" in x and "T7" in x for x in errors))
        s["Scenes"][0]["Requires"].append("trickster.now")
        self.assertFalse(any(x.startswith("T7") for x in lint.producer_presence_errors(s)))

    def test_choice_guard_and_failed_native_path(self):
        s = fixture()
        scene = s["Scenes"][0]
        choice = scene["Nodes"][0]["Choices"][0]
        choice["Requires"] = ["trickster"]
        self.assertFalse(lint.live_context(s, scene, choice))
        choice["Forbids"] = ["trickster.failed"]
        self.assertTrue(lint.live_context(s, scene, choice))
        self.assertFalse(lint.live_context(s, scene))
        choice["Requires"] = ["trickster.now"]
        choice["Forbids"] = []
        self.assertTrue(lint.live_context(s, scene, choice))

    def test_earned_flag_latch_and_mixed_or_do_not_prove_current_power(self):
        s = fixture()
        scene = s["Scenes"][0]
        s["Scenes"].append({"Id": "her.setup", "Requires": ["trickster.now"],
                            "Nodes": [{"Choices": [{"Set": ["her.paid"]}]}]})
        s["Latches"]["her.latched"] = ["trickster.now"]
        for key in ("her.paid", "her.latched", "trickster.ever", "trickster.was"):
            scene["Requires"] = [key]
            self.assertFalse(lint.live_context(s, scene), key)
        scene["RequiresAnyGroups"] = [["trickster.now", "her.paid"]]
        self.assertFalse(lint.live_context(s, scene))
        scene["RequiresAnyGroups"] = [["trickster.now"]]
        self.assertTrue(lint.live_context(s, scene))

    def test_return_composite_and_device_completion(self):
        s = fixture()
        s["Relationships"]["her"]["UnavailableOverrides"]["her.dead"] = "her.back"
        s["Derived"]["her.back"] = [["trickster.ever", "her.raised"]]
        s["Scenes"][0]["Nodes"][0]["Choices"][0] = {"Set": ["her.raised"]}
        self.assertTrue(any("her.raised" in x for x in lint.producer_presence_errors(s)))
        s["Scenes"][0]["Nodes"] = []
        s["Scenes"][0]["TricksterDevice"] = True
        self.assertTrue(any(x.startswith("T7 her.device:") for x in lint.producer_presence_errors(s)))

    def test_historical_consumers_stay_valid(self):
        s = fixture()
        s["Scenes"][0]["Requires"] = ["trickster.now"]
        s["Scenes"].append({"Id": "her.after", "Relationship": "her",
                            "Requires": ["trickster.ever", "her.returned"], "Nodes": []})
        self.assertFalse(any(x.startswith("T7") for x in lint.producer_presence_errors(s)))

    def test_device_completion_flags_without_return_metadata(self):
        s = fixture()
        s["Relationships"] = {}
        s["Scenes"][0]["Nodes"][0]["Choices"][0] = {"Set": ["her.device_completed"]}
        self.assertTrue(any("her.device_completed" in x for x in lint.producer_presence_errors(s)))


class PhysicalPresenceTests(unittest.TestCase):
    def test_central_guard_is_idempotent_and_does_not_alias_requirements(self):
        s = fixture()
        original = copy.deepcopy(s["Presences"])
        s["Presences"]["her.presence.second"] = dict(s["Presences"]["her.presence"])
        ep.integrate_presences(s)
        key = ep.presence_guard("her")
        self.assertEqual(s["DerivedOpenRoutes"][key], ["her"])
        self.assertEqual(s["Derived"][key], ep.PRESENCE_CHAPTERS)
        self.assertEqual(original["her.presence"]["Requires"], ["trickster.ever", "her.returned"])
        before = copy.deepcopy(s)
        ep.integrate_presences(s)
        self.assertEqual(s, before)
        self.assertFalse(any(x.startswith("P1") for x in lint.producer_presence_errors(s)))

    def test_missing_wrong_or_weakened_guard_fails(self):
        for mutation in ("absent", "wrong_route", "weak_groups"):
            with self.subTest(mutation=mutation):
                s = fixture()
                ep.integrate_presences(s)
                key = ep.presence_guard("her")
                if mutation == "absent":
                    s["Presences"]["her.presence"]["Requires"].remove(key)
                elif mutation == "wrong_route":
                    s["DerivedOpenRoutes"][key] = ["someone_else"]
                else:
                    s["Derived"][key] = [["her.returned"]]
                self.assertTrue(any(x.startswith("P1 her.presence:") for x in lint.producer_presence_errors(s)))

    def test_departures_need_registration_or_reason(self):
        s = fixture()
        c = s["Scenes"][0]["Nodes"][0]["Choices"][0]
        c["Set"] = ["her.left_free"]
        self.assertTrue(any("departure her.left_free" in x for x in lint.producer_presence_errors(s)))
        s["Relationships"]["her"]["UnavailableFlags"].append("her.left_free")
        self.assertFalse(any("departure her.left_free" in x for x in lint.producer_presence_errors(s)))
        s["Relationships"]["her"]["UnavailableFlags"].remove("her.left_free")
        from unittest.mock import patch
        with patch.dict(ep.DEPARTURE_EXEMPTIONS, {("her", "her.left_free"): "Temporary trip; contact forbids it."}):
            self.assertFalse(any("departure her.left_free" in x for x in lint.producer_presence_errors(s)))
        with patch.dict(ep.DEPARTURE_EXEMPTIONS, {("her", "her.left_free"): ""}):
            self.assertTrue(any("departure her.left_free" in x for x in lint.producer_presence_errors(s)))


class ReturnInProgressTests(unittest.TestCase):
    def story(self):
        rel = {"ClosedFlag": "aranka.closed",
               "UnavailableFlags": ["aranka.ran_failure", "aranka.dead", "aranka.gone"],
               "UnavailableOverrides": {"aranka.ran_failure": "aranka.trickster.moral_repaired"}}
        s = {"Relationships": {"aranka": rel}, "Derived": {},
             "Presences": {"aranka.presence": {"Requires": []}, "aranka.presence.yard": {"Requires": []}},
             "Scenes": [{"Id": "aranka.reply", "Relationship": "aranka", "Requires": ["trickster.now"],
                         "Nodes": [{"Choices": [{"Set": ["aranka.trickster.answered"]}]}]}]}
        ep.integrate_presences(s)
        return s

    def test_only_documented_loss_is_lifted_and_integration_is_idempotent(self):
        s = self.story()
        before = copy.deepcopy(s)
        ep.integrate_presences(s)
        self.assertEqual(s, before)
        self.assertFalse(lint.producer_presence_errors(s))
        rel = s["Relationships"]["aranka"]
        self.assertEqual(rel["UnavailableOverrides"], {"aranka.ran_failure": "aranka.trickster.moral_repaired"})
        key = ep.presence_guard("aranka")
        loss = key + ".blocked.aranka.ran_failure"
        self.assertEqual(s["DerivedForbids"][loss],
                         ["aranka.trickster.moral_repaired", "aranka.trickster.answered"])
        self.assertNotIn(key, s.get("DerivedOpenRoutes", {}))
        for flag in ("aranka.dead", "aranka.gone"):
            self.assertNotIn(key + ".blocked." + flag, s["DerivedForbids"])

    def test_unlisted_lift_and_missing_loss_or_closure_fail_p1(self):
        key = ep.presence_guard("aranka")
        for mutation in ("unlisted_lift", "missing_loss", "missing_closure", "route_guard"):
            with self.subTest(mutation=mutation):
                s = self.story()
                if mutation == "unlisted_lift":
                    s["DerivedForbids"][key + ".blocked.aranka.dead"] = ["aranka.trickster.answered"]
                elif mutation == "missing_loss":
                    s["DerivedForbids"][key].remove(key + ".blocked.aranka.dead")
                elif mutation == "missing_closure":
                    s["DerivedForbids"][key].remove("aranka.closed")
                else:
                    s["DerivedOpenRoutes"] = {key: ["aranka"]}
                self.assertTrue(any(x.startswith("P1") for x in lint.producer_presence_errors(s)))

    def test_exception_needs_reason_registered_loss_and_live_producer(self):
        from unittest.mock import patch
        s = self.story()
        for mutation in ("no_reason", "blank_reason", "unregistered_loss", "non_trickster_flag"):
            progress = copy.deepcopy(ep.PRESENCE_RETURN_IN_PROGRESS)
            entry = progress["aranka"]["aranka.ran_failure"]
            if mutation == "no_reason":
                entry.pop("Reason")
            elif mutation == "blank_reason":
                entry["Reason"] = " "
            elif mutation == "unregistered_loss":
                progress["aranka"]["aranka.unregistered"] = progress["aranka"].pop("aranka.ran_failure")
            else:
                entry["Flag"] = "chapter_later"
            with self.subTest(mutation=mutation), patch.dict(ep.PRESENCE_RETURN_IN_PROGRESS, progress, clear=True):
                self.assertTrue(any(x.startswith("P1") for x in lint.producer_presence_errors(s)))
        s["Scenes"][0]["Requires"] = ["trickster.ever"]
        self.assertTrue(any(x.startswith("T7") for x in lint.producer_presence_errors(s)))


if __name__ == "__main__":
    unittest.main()
