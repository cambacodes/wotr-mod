"""Wave 1 registration and the inventory of deed, history and living surfaces."""
import json
from pathlib import Path
import unittest

from tests.story_fixture import fresh_story


ROOT = Path(__file__).resolve().parents[1]


class RowRegistryTests(unittest.TestCase):
    def test_historical_dismissals_do_not_exempt_actual_departures(self):
        from tools.earned_presence_lint import producer_presence_errors
        declared = json.loads((ROOT / "tools/harem_wave1_contracts.json").read_text(encoding="utf-8"))
        flags = list(declared["departure_exemptions"]["household"])
        story = {"Relationships": {"household": {"UnavailableFlags": []}},
                 "Scenes": [{"Id": "household.test", "Relationship": "household",
                             "Nodes": [{"Id": "start", "Choices": [{"Set": [*flags, "household.gone"]}]}]}]}
        errors = producer_presence_errors(story)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("departure household.gone", errors[0])

    def test_register_twice_preserves_source_and_scene_order(self):
        from story import make_story, scenes
        first, second = make_story(), make_story()
        self.assertEqual([s["Id"] for s in first["Scenes"]],
                         [s["Id"] for s in second["Scenes"]])
        self.assertEqual(first["Derived"], second["Derived"])
        self.assertEqual(first["PendingHooks"], second["PendingHooks"])
        self.assertEqual(first["Scenes"][:len(scenes)], scenes)
        self.assertIsNot(first["Scenes"], scenes)
        ids = [s["Id"] for s in first["Scenes"]]
        self.assertEqual(len(ids), len(set(ids)))
        # The base builder has no presence/household contracts yet.
        self.assertFalse(any(s['Id'].startswith('household.') for s in first['Scenes']))

    def test_assembled_registration_keeps_late_rows_and_presence_contracts(self):
        story = fresh_story()
        from tools.rrt_verify import Model, household_presence_attachment
        model = Model(story)
        for sid in ('household.pair.shamira_arueshalae.settle.good',
                    'household.pair.herrax_minagho.notice.minagho',
                    'household.pair.wenduag_vellexia.notice',
                    'household.pair.yaniel_areelu.commission'):
            self.assertIn(sid, model.by_id)
        for body in model.scenes:
            if (body['Relationship'] == 'household' and body.get('ContactUnit')
                    and body.get('InteractionHub')):
                self.assertTrue(household_presence_attachment(story, body), body['Id'])

    def test_every_row_surface_is_classified_once(self):
        story = fresh_story()
        contracts = json.loads((ROOT / "tools/harem_wave1_contracts.json").read_text(encoding="utf-8"))
        self.assertEqual(set(contracts["rows"]), {"s02", "s04", "s06", "s07", "s36", "s37", "s38", "s39", "s40", "s41"})
        scene_ids = [s["Id"] for s in story["Scenes"]]
        self.assertEqual(len(scene_ids), len(set(scene_ids)))
        for row, contract in contracts["rows"].items():
            pair = ("seelah_camellia" if row == "s04" else
                    Path(contract["source"]).stem.removeprefix("household_pair_"))
            prefix = "household.pair." + pair + "."
            with self.subTest(row=row):
                self.assertEqual(contract["scenes"], [s["Id"] for s in story["Scenes"] if s["Id"].startswith(prefix)])
                self.assertEqual(contract["history_books"], [e["Id"] for e in story["Books"]["trickster.ledger"]["Entries"] if e["Id"].startswith(prefix)])
                hosts = [s["Id"] for s in story["Scenes"] if any(
                    any(f.startswith(prefix) for f in p.get("Requires", []))
                    for n in s["Nodes"] for p in n.get("Paragraphs", []))]
                self.assertEqual(contract["living_reader_hosts"], hosts)
