"""Structure regressions for fix17a; prose changes are never test contracts."""
import json
from pathlib import Path
import re
import unittest

from tests.story_fixture import fresh_story
from tools import hub_attachment_lint, prose_pending_lint, rrt_verify
from tools.crossroute_checks.mention_context import live_mentions


class StructureTests(unittest.TestCase):
    def test_registration_fixture_keeps_nominated_delivery_foundations(self):
        from tests.story_fixture import row_registration_fixture
        from storylines.harem_rows import s48
        payload = row_registration_fixture(s48)
        ids = {s["Id"] for s in payload["Scenes"]}
        self.assertTrue({"household.ensemble.ch5.arrows",
                         "household.docket.gesmerha_jerribeth.account"} <= ids)
        # Omitting either foundation remains an error through the real checker.
        for sid in ("household.ensemble.ch5.arrows",
                    "household.docket.gesmerha_jerribeth.account"):
            broken = dict(payload, Scenes=[s for s in payload["Scenes"] if s["Id"] != sid])
            self.assertTrue(any(sid + ": missing registered scene" in e
                                for e in hub_attachment_lint.gameplay_entry_lint(broken)))

    def test_export_has_visible_pages_and_registered_pending_if_any(self):
        payload = fresh_story()
        self.assertEqual(rrt_verify.validate(rrt_verify.Model(payload)), [])
        registry = json.loads(Path("tools/route_packs/plans/prose-pending.json").read_text(encoding="utf-8"))
        self.assertEqual(prose_pending_lint.check(payload, registry, integration=True), [])

    def test_reviewed_partner_reference_does_not_exempt_a_new_appearance(self):
        pattern = re.compile(r"\bShamira\b", re.I)
        self.assertTrue(live_mentions("Shamira steps into the room and takes your hand.",
                                      pattern, False, "noct.second_door"))
