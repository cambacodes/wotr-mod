"""W5 alliance readers: earned history, live channels and mutually exclusive state."""
import copy
import json
from pathlib import Path
import unittest

from storylines.harem_rows import w5_readers as readers
from tests.story_fixture import fresh_story
from tools import rrt_verify as verify, savecompat


ROOT = Path(__file__).resolve().parents[1]


def visible(block, flags):
    return (set(block.get("Requires", [])) <= flags
            and not set(block.get("Forbids", [])) & flags
            and all(set(group) & flags for group in block.get("AnyGroups", [])))


class W5ReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = fresh_story()
        # Test registration itself even when discovery supplied an assembled export.
        for scene in cls.before["Scenes"]:
            for node in scene["Nodes"]:
                if "Paragraphs" in node:
                    node["Paragraphs"][:] = [p for p in node["Paragraphs"]
                                              if not any(k.startswith(readers.P) for k in p["Requires"])]
        entries = cls.before["Books"]["trickster.ledger"]["Entries"]
        entries[:] = [entry for entry in entries if not entry["Id"].startswith(readers.P)
                      and entry["Id"] not in (readers.s21.P + "seating", readers.s29.P("seating"))]
        for field in ("Derived", "DerivedForbids", "DerivedOpenRoutes"):
            for key in list(cls.before[field]):
                if key.startswith(readers.P):
                    del cls.before[field][key]
        cls.story = copy.deepcopy(cls.before)
        readers.register(cls.story, cls.story["Scenes"], cls.story["Etudes"])
        cls.model = verify.Model(copy.deepcopy(cls.story))
        cls.hosts = {scene["Id"]: scene for scene in cls.story["Scenes"]}
        cls.inventory = json.loads((ROOT / "tools/harem_w5_readers.json").read_text(encoding="utf-8"))

    def state(self, row, extra=(), omit=()):
        state = verify.SimState(6, 1000)
        visited = set()
        def seed(key):
            if key in visited:
                return
            visited.add(key)
            if key in self.model.composites:
                for need in self.model.composites[key][0]:
                    seed(need)
            else:
                state.flags.add(key)
        seed(readers.P + row + ".current")
        for key in extra:
            seed(key)
        state.flags.difference_update(omit)
        state.flags.update(extra)
        verify.sim_complete(self.model, state)
        return state.flags

    def paragraphs(self, row, woman):
        return [p for p in self.hosts[woman + ".lastcall.page"]["Nodes"][0]["Paragraphs"]
                if readers.P + row + ".current" in p["Requires"]]

    def test_all_current_readers_need_page_path_channels_and_survival(self):
        for row, spec in readers.ROWS.items():
            key = readers.P + row + ".current"
            with self.subTest(row=row):
                self.assertIn(key, self.state(row))
                for lost in ("trickster", "trickster.foresight.accepted", "household.table.kept"):
                    self.assertNotIn(key, self.state(row, omit=(lost,)))
                for loss in ("trickster.failed", "legend", "sacrifice", "household.closed"):
                    self.assertNotIn(key, self.state(row, extra=(loss,)))
                self.assertIn(key, self.state(row, extra=("sacrifice", "trickster.commander_back")))
                for woman in spec["pair"]:
                    for loss in (woman + ".closed", woman + ".epoch_unavailable", woman + ".returned_actor_lost"):
                        self.assertNotIn(key, self.state(row, extra=(loss,)))

    def test_earned_return_is_scoped_and_cannot_override_a_later_loss(self):
        key = readers.P + "s30.current"
        returned = ("targona.dead_lab", "targona.trickster.returned")
        self.assertIn(key, self.state("s30", extra=returned))
        for loss in ("targona.dead_lair", "targona.condemned", "targona.epoch_unavailable",
                     "eliandra.dead", "eliandra.trickster.away"):
            self.assertNotIn(key, self.state("s30", extra=(*returned, loss)), loss)
        self.assertNotIn(key, self.state("s30", omit=("eliandra.met_ch5",), extra=("eliandra.met_ch3",)))
        self.assertNotIn(key, self.state("s30", omit=("targona.trickster.met", "targona.trickster.returned"),
                                        extra=("targona.free",)))

    def test_recall_needs_every_deed_and_cost_and_never_promotes_affection(self):
        for row, spec in readers.ROWS.items():
            if row == "s20":
                continue
            for woman in spec.get("hosts", spec["pair"]):
                success, declined, unplayed = self.paragraphs(row, woman)
                flags = self.state(row, extra=spec["kept"])
                self.assertEqual([success], [p for p in (success, declined, unplayed) if visible(p, flags)])
                for missing in spec["kept"]:
                    self.assertFalse(visible(success, flags - {missing}), (row, woman, missing))
                flags = self.state(row, extra=(spec["seen"], spec["declined"]))
                self.assertEqual([declined], [p for p in (success, declined, unplayed) if visible(p, flags)])
                self.assertEqual([unplayed], [p for p in (success, declined, unplayed)
                                            if visible(p, self.state(row))])

    def test_jannah_offer_is_not_a_meeting_and_deferral_not_a_duel(self):
        spec = readers.ROWS["s20"]
        for woman in spec["pair"]:
            blocks = self.paragraphs("s20", woman)
            for index, outcome in enumerate(spec["outcomes"]):
                flags = self.state("s20", extra=(spec["seen"], outcome))
                self.assertEqual([blocks[index]], [p for p in blocks if visible(p, flags)])
                self.assertFalse(visible(blocks[index], flags - {spec["seen"]}))
            self.assertIn("no answer from Seelah", blocks[1]["Text"])
            self.assertIn("had not settled", blocks[2]["Text"])

    def test_highest_stage_and_enmity_precedence_are_directional(self):
        for row, spec in readers.ROWS.items():
            entry = next(e for e in self.story["Books"]["trickster.ledger"]["Entries"]
                         if e["Id"] == readers.P + row + ".seating")
            for direction, (a, b) in enumerate((spec["pair"], spec["pair"][::-1])):
                lines = entry["Lines"][direction * 5:direction * 5 + 5]
                # Binding order, independent of the implementation's STAGES.
                canonical = ("rival", "respect", "friend", "lover")
                for mask in range(16):
                    stages = [a + ".harem.attitude." + b + "." + stage
                              for i, stage in enumerate(canonical) if mask & (1 << i)]
                    for hostile, mended in ((False, False), (True, False), (True, True)):
                        extra = stages + ([a + ".harem.enmity." + b] if hostile else [])
                        extra += [a + ".harem.reconciled." + b] if mended else []
                        shown = [line for line in lines if visible(line, self.state(row, extra=extra))]
                        highest = a + ".harem.attitude." + b + "." + canonical[mask.bit_length() - 1] if mask else None
                        expected = ([lines[0]] if hostile and not mended else
                                    [next(line for line in lines if highest in line["Requires"])] if mask else [])
                        self.assertEqual(expected, shown, (row, a, mask, hostile, mended))

    def test_current_partner_account_overrides_older_kiana_history(self):
        entry = next(e for e in self.story["Books"]["trickster.ledger"]["Entries"]
                     if e["Id"] == readers.P + "s29.seating")
        account = entry["Lines"][10:]
        keys = [flag for _, flag, _ in readers.s29.ACCOUNTS]
        for mask in range(1 << len(keys)):
            flags = {readers.P + "s29.current", *(k for i, k in enumerate(keys) if mask & (1 << i))}
            shown = [line for line in account if visible(line, flags)]
            expected = account[next(i for i in range(len(keys)) if mask & (1 << i))] if mask else account[-1]
            self.assertEqual([expected], shown)

    def test_history_survives_absence_without_living_speech(self):
        entries = self.story["Books"]["trickster.ledger"]["Entries"]
        for row in ("s21", "s29"):
            spec = readers.ROWS[row]
            entry = next(e for e in entries if e["Id"] == spec["prefix"] + "seating")
            flags = self.state(row, extra=(*spec["kept"], spec["pair"][0] + ".closed", "sacrifice"))
            self.assertTrue(visible(entry, flags))
            self.assertTrue(visible(entry["Lines"][0], flags))
            for woman in spec.get("hosts", spec["pair"]):
                self.assertFalse(any(visible(p, flags) for p in self.paragraphs(row, woman)))

    def test_classification_and_append_only_registration(self):
        from tools import payoff_lint, departure_lint
        self.assertEqual([], payoff_lint.check(copy.deepcopy(self.story)))
        self.assertEqual([], departure_lint.check(copy.deepcopy(self.story)))
        actual = {(s["Id"], n["Id"], i) for s in self.story["Scenes"] for n in s["Nodes"]
                  for i, p in enumerate(n.get("Paragraphs", []))
                  if any(k.startswith(readers.P) for k in p["Requires"])}
        self.assertEqual(actual, {(s["scene"], s["node"], s["paragraph"]) for s in self.inventory["living"]})
        self.assertEqual(26, len(actual))
        for old, new in zip(self.before["Scenes"], self.story["Scenes"]):
            self.assertEqual(old["Id"], new["Id"])
            for oldnode, newnode in zip(old["Nodes"], new["Nodes"]):
                self.assertEqual(oldnode["Id"], newnode["Id"])
                self.assertEqual(oldnode["Choices"], newnode["Choices"])
                self.assertEqual(oldnode["Text"], newnode["Text"])
                self.assertEqual(oldnode.get("Paragraphs", []), newnode.get("Paragraphs", [])[:len(oldnode.get("Paragraphs", []))])
        for woman in ("kiana", "nenio"):
            old = next(s for s in self.before["Scenes"] if s["Id"] == woman + ".lastcall.page")
            self.assertEqual(old, self.hosts[woman + ".lastcall.page"])
        for field in ("Relationships", "DepartureEpochs", "Presences", "SeatWomen", "Counts", "RestAllowances"):
            self.assertEqual(self.before.get(field), self.story.get(field))
        self.assertEqual([], savecompat.check(self.story, savecompat.inventory(self.before)))
        repeated = copy.deepcopy(self.story)
        readers.register(repeated, repeated["Scenes"], repeated["Etudes"])
        self.assertEqual(self.story, repeated)

    def test_static_inventory_rejects_missing_receipt_route_and_survival_guards(self):
        from tools.harem_w5_readers_lint import check
        story = copy.deepcopy(self.story)
        block = next(p for s in story["Scenes"] if s["Id"] == "yaniel.lastcall.page"
                     for p in s["Nodes"][0]["Paragraphs"] if readers.P + "s21.current" in p["Requires"])
        block["Requires"].remove(readers.s21.P + "cost.seelah_left_praise")
        self.assertTrue(any("deed/cost" in error for error in check(story)))
        story = copy.deepcopy(self.story)
        story["DerivedOpenRoutes"][readers.P + "s30.current"] = []
        self.assertTrue(any("route/epoch" in error for error in check(story)))
        story = copy.deepcopy(self.story)
        story["DerivedForbids"][readers.P + "commander.not_sacrificed"] = []
        self.assertTrue(any("Commander survival" in error for error in check(story)))
        # The static classification is optional for a deliberately disabled-row
        # authoring build, and performs no paragraph-position runtime writes.
        self.assertEqual([], check(self.before))
