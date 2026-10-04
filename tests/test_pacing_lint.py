"""The pacing lint (handoff 13 section 6): schema and roster checks, beat counts, REVIEW/WARN, and each HARD rule."""
import copy
import io
import json
from pathlib import Path
import sys
from tests.temp_directory import temporary_directory
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pacing_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "pacing-fixtures"


def fixture(name):
    return pacing_lint.load_json(FIXTURES / name)


def run(*args):
    out = io.StringIO()
    saved, sys.stdout = sys.stdout, out
    try:
        code = pacing_lint.main(list(args))
    finally:
        sys.stdout = saved
    return code, out.getvalue()


class PacingSchemaTests(unittest.TestCase):
    def test_ok_fixture_passes(self):
        code, text = run("--story", str(FIXTURES / "story.json"), "--availability", str(FIXTURES / "availability-ok.json"),
                         "--matrix", str(FIXTURES / "matrix.json"))
        self.assertEqual(code, 0, text)
        self.assertIn("pacing: 0 hard", text)

    def test_schema_fixtures_fail(self):
        for name, message in [("availability-missing.json", "missing entry for roster character 'Gamma'"),
                              ("availability-extra.json", "'Delta' is not a roster character"),
                              ("availability-bad-chapter.json", "bad chapter key '0'"),
                              ("availability-bad-mode.json", "bad mode 'letter'")]:
            with self.subTest(name=name):
                code, text = run("--story", str(FIXTURES / "story.json"), "--availability", str(FIXTURES / name),
                                 "--matrix", str(FIXTURES / "matrix.json"))
                self.assertEqual(code, 2, text)
                self.assertIn(message, text)

    def test_duplicate_entry_exception_evidence_and_verify(self):
        roster = fixture("matrix.json")["characters"]
        roster = [{"character": r["character"], "relationship": r["relationship_id"]} for r in roster]
        cases = []
        base = fixture("availability-ok.json")
        a = copy.deepcopy(base); a["alpha2"] = copy.deepcopy(a["alpha"]); cases.append((a, "has 2 entries"))
        a = copy.deepcopy(base); a["beta"]["exceptions"] = {"5": "because"}; cases.append((a, "must read \"none: <reason>\""))
        a = copy.deepcopy(base); a["beta"]["exceptions"] = {"1": "none: absent"}; cases.append((a, "where she is not present"))
        a = copy.deepcopy(base); del a["alpha"]["evidence"]["4"]; cases.append((a, "present in chapter 4 without evidence"))
        a = copy.deepcopy(base); a["alpha"]["evidence"]["first_met"] = "somewhere"; cases.append((a, "first_met must cite"))
        a = copy.deepcopy(base); a["beta"]["verify"] = False; cases.append((a, "verify is not true"))
        a = copy.deepcopy(base); a["alpha"]["routes"] = [{"relationship": "other"}]; cases.append((a, "roster relationship 'alpha'"))
        for availability, message in cases:
            with self.subTest(message=message):
                with self.assertRaises(pacing_lint.SchemaError) as caught:
                    pacing_lint.validate_availability(availability, roster)
                self.assertIn(message, str(caught.exception))

    def test_roster_snapshot_fallback_and_drift(self):
        availability = fixture("availability-ok.json")
        notes = []
        roster = pacing_lint.resolve_roster(availability, str(FIXTURES / "absent-matrix.json"), notes)
        self.assertEqual([r["character"] for r in roster], ["Alpha", "Beta", "Gamma"])
        self.assertIn("snapshot", notes[0])
        drifted = copy.deepcopy(availability)
        drifted["_roster"][2]["character"] = "Gamma Prime"
        with self.assertRaisesRegex(pacing_lint.SchemaError, "differs from"):
            pacing_lint.resolve_roster(drifted, str(FIXTURES / "matrix.json"), [])


class PacingCountTests(unittest.TestCase):
    def setUp(self):
        self.story = fixture("story.json")
        self.availability = fixture("availability-ok.json")
        self.roster = pacing_lint.resolve_roster(self.availability, str(FIXTURES / "matrix.json"), [])

    def report(self):
        return pacing_lint.lint(self.story, self.availability, self.roster)

    def test_counts_review_warn_info(self):
        report = self.report()
        rows = {row["character"]: row for row in report["characters"]}
        alpha = rows["Alpha"]
        self.assertEqual(alpha["starts"]["1"], {"ip": 1})
        self.assertEqual(alpha["starts"]["3"], {"ip": 2})
        self.assertEqual(alpha["starts"]["4"], {"remote": 1})
        self.assertEqual(alpha["open"]["2"], {"ip": 1})
        self.assertEqual(alpha["open"]["5"], {"ip": 1})
        review = {(r["character"], r["chapter"]): r for r in report["review"]}
        # Chapter 2 and 5: nothing starts, although an earlier beat is still open; exceptions silence Beta's Ch5.
        self.assertEqual(set(review), {("Alpha", "2"), ("Alpha", "5")})
        self.assertEqual(review[("Alpha", "2")]["open_from_earlier"], 1)
        self.assertEqual(len(report["warn"]), 2)
        self.assertTrue(any("Alpha: Chapter 4 in person" in w for w in report["warn"]))
        self.assertIn("Gamma: no route in Story.json yet", report["info"])
        self.assertEqual(report["hard"], [])

    def test_review_is_not_failure_and_prologue_folds_into_chapter_one(self):
        self.story["Scenes"].append({**copy.deepcopy(self.story["Scenes"][0]), "Id": "alpha.prologue", "MinChapter": 0,
                                     "MaxChapter": 1, "Chapters": []})
        report = self.report()
        alpha = {row["character"]: row for row in report["characters"]}["Alpha"]
        self.assertEqual(alpha["starts"]["1"], {"ip": 2})
        with temporary_directory() as directory:
            story = Path(directory) / "story.json"
            story.write_text(json.dumps(self.story), encoding="utf-8")
            code, text = run("--story", str(story), "--availability", str(FIXTURES / "availability-ok.json"),
                             "--matrix", str(FIXTURES / "matrix.json"))
        self.assertEqual(code, 0, text)
        self.assertIn("REVIEW Alpha Ch2", text)

    def test_owner_filter_splits_a_shared_relationship(self):
        self.availability["alpha"]["routes"] = [{"relationship": "alpha", "owners": ["Memory"]}]
        alpha = {row["character"]: row for row in self.report()["characters"]}["Alpha"]
        self.assertEqual(alpha["starts"]["1"], {})
        self.assertEqual(alpha["starts"]["4"], {"remote": 1})


class PacingHardRuleTests(unittest.TestCase):
    def setUp(self):
        self.story = fixture("story.json")
        self.early = self.story["Scenes"][0]
        self.choice = self.early["Nodes"][0]["Choices"][0]

    def rules(self):
        return [(rule, sid) for rule, sid, _ in pacing_lint.hard_violations(self.story)]

    def test_clean(self):
        self.assertEqual(self.rules(), [])

    def test_h1_trickster_reads_and_content(self):
        for mutate in (lambda: self.early["Requires"].append("trickster"),
                       lambda: self.early["Forbids"].append("trickster.ever"),
                       lambda: self.choice["Requires"].append("trickster"),
                       lambda: self.early.update(TricksterDevice=True),
                       lambda: self.early.update(EntryMythic="Trickster"),
                       lambda: self.choice.update(Mythic="Trickster")):
            self.setUp()
            mutate()
            self.assertEqual(self.rules(), [("H1", "alpha.early")])

    def test_h1_ignores_chapter_three(self):
        self.story["Scenes"][1]["Requires"].append("trickster")
        self.assertEqual(self.rules(), [])

    def test_h2_commit_and_trickster_start(self):
        self.choice["Set"].append("alpha.committed")
        self.assertEqual(self.rules(), [("H2", "alpha.early")])
        self.setUp()
        self.choice["Set"].append("alpha.started")   # only a Trickster scene starts alpha: a Trickster route
        self.assertEqual(self.rules(), [("H2", "alpha.early")])
        self.setUp()
        self.choice["Set"].append("beta.started")    # a path-neutral Ch3 scene starts beta: a base route
        self.assertEqual(self.rules(), [])

    def test_h2_framework_relationship_outside_the_roster(self):
        # Doc 15 section 7: the Long Con starts in Ch1 and is no romance; with the roster given, only its routes count.
        self.choice["Set"].append("alpha.started")
        rules = [(rule, sid) for rule, sid, _ in pacing_lint.hard_violations(self.story, paced={"beta"})]
        self.assertEqual(rules, [])
        rules = [(rule, sid) for rule, sid, _ in pacing_lint.hard_violations(self.story, paced={"alpha"})]
        self.assertEqual(rules, [("H2", "alpha.early")])
        self.setUp()
        self.choice["Set"].append("alpha.committed")   # the CommittedFlag rule still covers every relationship
        rules = [(rule, sid) for rule, sid, _ in pacing_lint.hard_violations(self.story, paced={"beta"})]
        self.assertEqual(rules, [("H2", "alpha.early")])

    def test_h3_native_keys_and_romance_etudes(self):
        self.choice["Set"].append("kenabres.fallen")
        self.assertEqual(self.rules(), [("H3", "alpha.early")])
        self.setUp()
        self.story["Scenes"][1]["Nodes"][0]["Choices"][0]["Set"].append("alpha.native_romance")
        self.assertEqual(self.rules(), [("H3", "alpha.mid")])   # romance etudes: any chapter
        self.setUp()
        self.story["Scenes"][1]["Nodes"][0]["Choices"][0]["Set"].append("kenabres.fallen")
        self.assertEqual(self.rules(), [])                       # other native keys: Ch1-2 only

    def test_h4_other_partner_commit_and_harem(self):
        self.early["Forbids"].append("beta.committed")
        self.assertEqual(self.rules(), [("H4", "alpha.early")])
        self.setUp()
        self.choice["Set"].append("alpha.harem.pair")
        self.assertEqual(self.rules(), [("H4", "alpha.early")])
        self.setUp()
        self.early["Requires"].append("alpha.committed")         # her own state is not another partner's
        self.assertEqual(self.rules(), [])

    def test_hard_exit_code(self):
        self.choice["Set"].append("alpha.committed")
        with temporary_directory() as directory:
            story = Path(directory) / "story.json"
            story.write_text(json.dumps(self.story), encoding="utf-8")
            code, text = run("--story", str(story), "--availability", str(FIXTURES / "availability-ok.json"),
                             "--matrix", str(FIXTURES / "matrix.json"))
        self.assertEqual(code, 1)
        self.assertIn("HARD H2 alpha.early", text)


class PacingRepositoryTests(unittest.TestCase):
    def test_repository_availability_and_story(self):
        story = ROOT / "development" / "Story.json"
        if not story.is_file():
            self.skipTest("development/Story.json not generated")
        availability = pacing_lint.load_json(pacing_lint.DEFAULT_AVAILABILITY)
        self.assertEqual(len([k for k in availability if not k.startswith("_")]), 43)
        roster = pacing_lint.resolve_roster(availability, str(pacing_lint.DEFAULT_MATRIX), [])
        self.assertEqual(len(roster), 43)
        report = pacing_lint.lint(pacing_lint.load_json(story), availability, roster)
        self.assertEqual(report["hard"], [])


if __name__ == "__main__":
    unittest.main()
