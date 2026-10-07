"""F8: one earned all-romance history survives the integrated availability guards."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import rrt_verify as V

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "tools" / "ideal-run-kit"


class IdealRunRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = V.Model(json.loads((ROOT / "development/Story.json").read_text(encoding="utf-8")))

    def test_combined_runs_earn_every_in_scope_commit_before_its_chapter_closes(self):
        baseline = set(self.model.rels) - {"foresight", "shamira_barracks"}
        self.assertEqual(len(baseline), 47)
        # Chapter limits from the guide's Part 8 table, rather than the simulator's final state.
        chapter3 = {"longcon", "household", "nenio", "targona", "nurah", "eritrice", "devarra",
                    "delamere", "gesmerha", "aranka", "kaylessa", "arsinoe", "chadali"}
        chapter4 = {"herrax"}
        chapter6 = {"nocticula", "areelu", "lastcall", "iomedae"}
        expected = baseline - {"ember", "aivu"}
        for lengths, last_day in (("", 115), ("3:80,5:30", 155)):
            with self.subTest(CHDAYS=lengths), tempfile.TemporaryDirectory(prefix="rrt-f8-test-") as scratch:
                output = Path(scratch) / "run.json"
                env = dict(os.environ, PYTHONHASHSEED="0", CHDAYS=lengths, PYTHONDONTWRITEBYTECODE="1")
                run = subprocess.run([sys.executable, str(KIT / "final_sim.py"), str(output)],
                                     cwd=scratch, env=env, capture_output=True, text=True, timeout=180)
                self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
                data = json.loads(output.read_text(encoding="utf-8"))
                result = data["result"]
                committed = {r["relationship"] for r in result["relationships"] if r["committed"] and r["relationship"] not in {"ember", "aivu", "shamira_barracks"}}
                self.assertEqual(committed & baseline, expected)
                self.assertEqual(committed - baseline, {"foresight"})
                self.assertEqual(next(r["day"] for r in result["relationships"]
                                      if r["relationship"] == "lastcall"), last_day)
                days = {int(ch): length for ch, length in result["chapter_days"].items()}
                for rel in expected:
                    chapter = 3 if rel in chapter3 else 4 if rel in chapter4 else 6 if rel in chapter6 else 5
                    start = sum(d for ch, d in days.items() if ch < chapter) * 24
                    hour = result["commit_hours"][rel]
                    self.assertGreaterEqual(hour, start, rel)
                    self.assertLess(hour, start + days[chapter] * 24, rel)
                self.assertTrue(all(c["rests_needed"] <= c["rests_available"] for c in result["chapters"]))
                log = data["log"]
                self.assertIn("delamere.lastcall.call", {e["id"] for e in log})
                self.assertEqual(sum(e["id"].endswith(".lastcall.call") for e in log), 22)
                signing = next(e for e in log if e["id"] == "dorgelinda.trickster.caravans.countersign")
                self.assertTrue(signing["completed"])
                self.assertIn("dorgelinda.trickster.cost.carts_signed",
                              {flag for c in signing["choices"] for flag in c["set"]})
                page = next(e for e in log if e["id"] == "trickster.foresight.page")
                self.assertIn("trickster.foresight.accepted", {f for c in page["choices"] for f in c["set"]})
                forced = set(data["natives"]) | set(data["timed"]) | set(data["never"])
                self.assertLessEqual(forced, set(self.model.native))

    def test_every_crypt_waking_requires_a_native_lock_and_an_open_trickster_route(self):
        for suffix, chapter, extra in (("crypt.stag", 3, set()), ("crypt.stag_alone", 3, {"kyado.dead"}),
                                        ("crypt.stag_late", 5, set())):
            scene = self.model.by_id["delamere.trickster." + suffix]

            def available(flags):
                state = V.SimState(chapter, 5000)
                state.flags.update(flags | extra)
                V.sim_complete(self.model, state)
                return V.sim_available(self.model, scene, state)

            base = {"trickster", "trickster.ever", "delamere.tomb_visited", "kyado.initiated"}
            for lock in ("delamere.tomb_book_locked_forced", "delamere.tomb_book_locked_opened"):
                with self.subTest(scene=scene["Id"], lock=lock):
                    earned = base | {lock}
                    self.assertTrue(available(earned))
                    self.assertFalse(available(base))
                    self.assertFalse(available(base | {"delamere.tomb_opened_bruteforce"}))
                    self.assertFalse(available(earned | {"delamere.closed"}))
                    self.assertFalse(available(earned - {"trickster"} | {"angel"}))
                    # The native move-order witnesses select the Drezen waking instead.
                    for moved in ("delamere.tomb_opened_peaceful", "delamere.tomb_opened_forced"):
                        self.assertFalse(available(earned | {moved}))


if __name__ == "__main__":
    unittest.main()
