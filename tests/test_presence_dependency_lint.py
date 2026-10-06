import copy
from functools import lru_cache
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from tools.presence_dependency_lint import check
from tools.presence_exception_schema import guard_fields


class PresenceDependencyTests(unittest.TestCase):
    @classmethod
    @lru_cache(maxsize=1)
    def export(cls):
        story = json.loads((Path(__file__).resolve().parents[1] / "development/Story.json").read_text(encoding="utf-8"))
        return story, set(check(story))

    def test_clean_export(self):
        _, baseline = self.export()
        self.assertEqual(set(), baseline)

    def test_export_and_mutations(self):
        story, baseline = self.export()
        for name in ("camellia.presence", "irabeth.presence", "kaylessa.presence",
                     "minagho_chivarro.presence.minagho", "nurah.presence.cell", "seelah.presence"):
            bad = copy.deepcopy(story)
            bad["PresenceExceptions"].pop(name)
            self.assertTrue(set(check(bad)) - baseline, name)

    def test_circular_earned_flag_is_rejected(self):
        story = {"Relationships": {"woman": {"UnavailableOverrides": {"dead": "returned"}}},
                 "Presences": {"woman.presence": {"Unit": "unit", "Requires": ["dead"]}},
                 "Scenes": [{"Id": "return", "Relationship": "woman", "ContactUnit": "unit",
                             "Requires": ["dead"], "Nodes": [{"Choices": [{"Set": ["returned"]}]}]}],
                 "Derived": {"paid": [["returned"]]},
                 "PresenceExceptions": {"woman.presence": {"Overrides": {"dead": {"Flag": "paid"}}}}}
        self.assertTrue(check(story))
        story["Derived"]["paid"] = [["payment"]]
        self.assertEqual([], check(story))

    def test_bootstrap_producer_behind_same_contact_is_circular(self):
        story = {"Relationships": {"woman": {"UnavailableOverrides": {"dead": "returned"}}},
                 "Presences": {"woman.presence": {"Unit": "unit", "Requires": ["dead", "open"]}},
                 "Scenes": [{"Id": "return", "Relationship": "woman", "ContactUnit": "unit",
                             "Requires": ["dead"], "Nodes": [{"Choices": [{"Set": ["returned"]}]}]},
                            {"Id": "pay", "ContactUnit": "unit", "Requires": [],
                             "Nodes": [{"Choices": [{"Set": ["paid"]}]}]}],
                 "Derived": {"open": [["chapter_later"]]}, "DerivedOpenRoutes": {"open": ["woman"]},
                 "PresenceExceptions": {"woman.presence": {"Overrides": {"dead": {"Flag": "paid"}}}}}
        # eng7-f4: exercise the actual serialized l06 guard rather than a route-open
        # key that never consumes the declared bootstrap.
        story["Relationships"]["woman"].update(ClosedFlag="closed", UnavailableFlags=["dead"])
        declaration = story["PresenceExceptions"]["woman.presence"]
        declaration.update(Guard="woman.presence.route_open", AbsentLosses={})
        for field, values in guard_fields("woman", story["Relationships"]["woman"], declaration).items():
            story.setdefault(field, {}).update(values)
        story["Presences"]["woman.presence"]["Requires"] = ["dead", declaration["Guard"]]
        # eng7-f4 end
        self.assertTrue(check(story))
        story["Scenes"][1].pop("ContactUnit")
        self.assertEqual([], check(story))
        story["Scenes"][1]["ContactUnit"] = "unit"
        story["Derived"]["paid"] = [["pay"]]
        story["Scenes"][1]["Nodes"] = [{"Choices": [{"Set": []}]}]
        self.assertTrue(check(story), "Implicit scene completion can also be circular")

    # eng7-f4: regressions for the all-route dependency inventory.
    def fixture(self):
        rel = {"ClosedFlag": "closed", "UnavailableFlags": ["dead"],
               "UnavailableOverrides": {"dead": "returned"}}
        declaration = {"Guard": "woman.presence.route_open", "AbsentLosses": {},
                       "Overrides": {"dead": {"Flag": "paid", "Reason": "Existing payment stages her arrival."}}}
        story = {"Relationships": {"woman": rel},
                 "Presences": {"woman.presence": {"Unit": "unit", "Requires": [declaration["Guard"]]}},
                 "PresenceExceptions": {"woman.presence": declaration},
                 "Derived": {"paid": [["payment"]]},
                 "Scenes": [{"Id": "return", "Relationship": "woman", "ContactUnit": "unit",
                             "Requires": ["dead"], "Nodes": [{"Id": "start", "Choices": [{"Set": ["returned"]}]}]}]}
        for field, values in guard_fields("woman", rel, declaration).items():
            story.setdefault(field, {}).update(values)
        return story

    def test_default_scope_includes_routes_outside_l06(self):
        story = self.fixture()
        self.assertEqual([], check(story))
        story["Derived"]["paid"] = [["returned"]]
        self.assertTrue(check(story))

    def test_access_return_without_unavailable_override(self):
        story = self.fixture()
        story["Relationships"]["woman"]["UnavailableOverrides"] = {}
        story["Relationships"]["woman"]["TricksterAccess"] = {
            "arrival": {"Detect": [], "Returned": "returned", "Device": "return"}}
        story["Presences"]["woman.presence"]["Requires"].append("returned")
        self.assertTrue(check(story), "Access-only returns must also be inventoried")
        story["Presences"]["woman.presence"]["Requires"].remove("returned")
        self.assertEqual([], check(story))

    def test_composite_and_latched_returns(self):
        for field, groups in (("Derived", [["arrived"]]), ("Latches", ["arrived"]),
                              ("Counts", {"Of": ["arrived"], "Min": 1})):
            story = self.fixture()
            story.setdefault(field, {})["returned"] = groups
            story["Scenes"][0]["Nodes"][0]["Choices"][0]["Set"] = ["arrived"]
            self.assertEqual([], check(story), field)
            story["Derived"]["paid"] = [["returned"]]
            self.assertTrue(check(story), field)

    def test_bootstrap_latches_counts_and_alternatives(self):
        for field, circular, independent in (("Latches", ["returned"], ["returned", "payment"]),
                ("Counts", {"Of": ["returned", "payment"], "Min": 2},
                           {"Of": ["returned", "payment"], "Min": 1})):
            story = self.fixture()
            del story["Derived"]["paid"]
            story.setdefault(field, {})["paid"] = circular
            self.assertTrue(check(story), field)
            story[field]["paid"] = independent
            self.assertEqual([], check(story), field)
        story = self.fixture()
        story["Derived"]["paid"] = [["returned"], ["payment"]]
        self.assertEqual([], check(story))
        story["Derived"]["paid"] = [["returned", "payment"]]
        self.assertTrue(check(story))

    def test_any_groups_and_contact_windows(self):
        for field in ("RequiresAny", "RequiresAnyGroups", "ContactWindows"):
            story = self.fixture()
            presence = story["Presences"]["woman.presence"]
            presence[field] = (["returned"] if field == "RequiresAny" else
                               [["returned"]] if field == "RequiresAnyGroups" else [{"Flag": "returned"}])
            self.assertTrue(check(story), field)
            presence[field] = (["returned", "payment"] if field == "RequiresAny" else
                               [["returned", "payment"]] if field == "RequiresAnyGroups" else [{"Flag": "payment"}])
            self.assertEqual([], check(story), field)

    def test_bootstrap_choice_path_and_crossroute_secondary_contact(self):
        story = self.fixture()
        del story["Derived"]["paid"]
        payer = {"Id": "pay", "Relationship": "other", "Nodes": [
            {"Id": "start", "Choices": [{"Requires": ["returned"], "Next": "paid"}]},
            {"Id": "paid", "Choices": [{"Set": ["paid"]}]}]}
        story["Scenes"].append(payer)
        self.assertTrue(check(story), "A guard on an earlier node must not be skipped")
        payer["Nodes"][0]["Choices"].append({"Next": "paid"})
        self.assertEqual([], check(story))
        payer["AdditionalContactUnits"] = ["unit"]
        self.assertTrue(check(story), "A producer on another route still needs the same actor")
        payer.pop("AdditionalContactUnits")
        payer["RequiresAnyGroups"] = [["returned"]]
        self.assertTrue(check(story))
        payer["RequiresAnyGroups"] = [["returned", "payment"]]
        self.assertEqual([], check(story))

    def test_explicit_retirement_and_nonmatching_device_history(self):
        story = self.fixture()
        del story["Derived"]["paid"]
        story["Scenes"].append({"Id": "retired_payment", "MinChapter": 3, "MaxChapter": 3,
                                "Forbids": ["chapter_later"],
                                "Nodes": [{"Choices": [{"Set": ["paid"]}]}]})
        story["Scenes"][0]["Requires"].append("paid")
        self.assertEqual([], check(story), "A retired return must remain dormant")
        story = self.fixture()
        story["Derived"]["paid"] = [["returned"]]
        story["Scenes"][0]["TricksterState"] = "living"
        story["Relationships"]["woman"]["TricksterAccess"] = {"living": {"Detect": ["alive"]}}
        self.assertEqual([], check(story), "A living device is not a death return")

    def test_remote_return_through_physical_payment_and_failure_receipt(self):
        story = self.fixture()
        del story["Derived"]["paid"]
        remote = story["Scenes"][0]
        remote.pop("ContactUnit")
        remote["Remote"] = True
        remote["Requires"].append("paid")
        story["Scenes"].append({"Id": "pay", "ContactUnit": "unit", "Requires": ["dead"],
                                "Nodes": [{"Choices": [{"Set": ["paid"]}]}]})
        self.assertTrue(check(story), "Remote returns can still depend on a circular physical payment")
        story["Scenes"][1].pop("ContactUnit")
        self.assertEqual([], check(story))
        story = self.fixture()
        story["Derived"]["paid"] = [["receipt"]]
        story["PresenceFailureReceipts"] = {"woman.presence": {
            "Flag": "receipt", "Requires": ["woman.presence.route_open"]}}
        self.assertTrue(check(story), "A failure receipt cannot bootstrap the presence that emits it")
        story["Derived"]["paid"] = [["woman.presence.failed"]]
        self.assertTrue(check(story), "A raw failed-placement input has the same dependency")

    def test_remote_return_requires_eligible_failed_placement(self):
        for evidence in ("woman.presence.failed", "receipt"):
            story = self.fixture()
            remote = story["Scenes"][0]
            remote.pop("ContactUnit")
            remote["Remote"] = True
            remote["Requires"].append(evidence)
            if evidence == "receipt":
                story["PresenceFailureReceipts"] = {"woman.presence": {
                    "Flag": evidence, "Requires": ["payment"]}}
            self.assertEqual([], check(story), evidence)
            story["Derived"]["paid"] = [["returned"]]
            errors = check(story)
            self.assertEqual(1, len(errors), evidence)
            self.assertIn("return: woman/dead requires contact woman.presence", errors[0])
            story["Derived"]["paid"] = [["payment"]]
            if evidence == "receipt":
                story["PresenceFailureReceipts"]["woman.presence"]["Requires"] = ["returned"]
                self.assertTrue(check(story), "Receipt eligibility also depends on the return")
            remote["Requires"].remove(evidence)
            story["Derived"]["paid"] = [["returned"]]
            remote["RequiresAny"] = [evidence, "payment"]
            self.assertEqual([], check(story), "An independent delivery road must stay valid")
            remote.pop("RequiresAny")
            remote["RequiresAnyGroups"] = [[evidence, "payment"]]
            self.assertEqual([], check(story), "Grouped alternatives also preserve independent delivery")
            remote["RequiresAnyGroups"] = [[evidence]]
            self.assertTrue(check(story), "A mandatory failed-placement alternative is circular")
            remote.pop("RequiresAnyGroups")
            remote["Forbids"] = ["dead"]
            remote["ForbidOverrides"] = {"dead": evidence}
            self.assertTrue(check(story), "A required loss lift must also follow failure evidence")

    def test_implicit_bootstrap_completion_needs_a_selectable_terminal(self):
        story = self.fixture()
        story["Derived"]["paid"] = [["pay"]]
        payer = {"Id": "pay", "Remote": True, "Nodes": [
            {"Id": "start", "Choices": [{"Requires": ["returned"]}]}]}
        story["Scenes"].append(payer)
        self.assertTrue(check(story), "A scene cannot complete through a locked terminal answer")
        payer["Nodes"][0]["Choices"].append({"Abort": True})
        self.assertTrue(check(story), "Aborting a scene does not produce its completion flag")
        payer["Nodes"][0]["Choices"].append({})
        self.assertEqual([], check(story), "An independent terminal answer breaks the cycle")

    def test_shared_prerequisite_diamonds_keep_contact_and_independent_roads(self):
        story = self.fixture()
        # Each level repeats the same prerequisites on several alternative roads.
        # The inventory needs their contact union, not every path through them.
        del story["Derived"]["paid"]
        story["Scenes"].append({"Id": "pay", "ContactUnit": "unit", "Nodes": [
            {"Id": "start", "Choices": [{"Set": ["payment"]}]}]})
        previous = "payment"
        for index in range(16):
            key = "diamond.%d" % index
            story["Derived"][key] = [[previous], [previous], [previous]]
            previous = key
        story["Derived"]["paid"] = [[previous]]
        self.assertTrue(check(story), "Repeated roads still require the same physical actor")
        story["Scenes"][-1].pop("ContactUnit")
        self.assertEqual([], check(story), "An independent payment must break the cycle")
        story["Scenes"][-1]["ContactUnit"] = "unit"
        story["Derived"]["paid"].append(["independent_payment"])
        self.assertEqual([], check(story), "An OR road must not inherit a cached cycle failure")

    def test_cli_is_strict_and_all_routes_without_opt_in(self):
        story = self.fixture()
        script = Path(__file__).resolve().parents[1] / "tools/presence_dependency_lint.py"
        with tempfile.TemporaryDirectory(prefix="eng7-f4-") as scratch:
            path = Path(scratch) / "Story.json"
            for circular in (False, True):
                if circular:
                    story["Derived"]["paid"] = [["returned"]]
                path.write_text(json.dumps(story), encoding="utf-8")
                for extra in ([], ["--strict"], ["--all", "--strict"]):
                    run = subprocess.run([sys.executable, str(script), "--story", str(path), *extra],
                                         cwd=scratch, capture_output=True, text=True, encoding="utf-8")
                    self.assertEqual(int(circular), run.returncode, run.stdout + run.stderr)
                    self.assertIn("presence dependencies: %d hard" % int(circular), run.stdout)
    # eng7-f4 end
