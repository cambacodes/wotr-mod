"""Route-only paths: real receipts, debt branches, and late local decisions."""
import copy
import json
import re
from pathlib import Path
import unittest

from storylines import (jerribeth, jerribeth_consequences, jerribeth_counteroffer,
                        jerribeth_progression, jerribeth_fate, jerribeth_trickster,
                        jerribeth_round2 as route, jerribeth_partner as partner)
from tests.test_jerribeth_partner import allowed, walk


def assemble():
    modules = (jerribeth, jerribeth_consequences, jerribeth_counteroffer,
               jerribeth_progression, jerribeth_fate, jerribeth_trickster)
    payload = {"Relationships": {"jerribeth": {"Guidance": ""}},
               "Scenes": copy.deepcopy([s for m in modules for s in m.SCENES])}
    jerribeth_trickster.integrate(payload)
    return {s["Id"]: s for s in payload["Scenes"]}


class RoundTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.events = assemble()

    def test_deferred_notice_never_completes_visit(self):
        letter = self.events["jerribeth.trickster.visit_letter"]
        visit = self.events["jerribeth.trickster.visit"]
        flags = set(letter["Requires"])
        _, endings = walk(letter, flags)
        self.assertTrue(endings)
        self.assertTrue(all(route.DEFERRED in held and route.VISITED not in held for held in endings))
        self.assertGreaterEqual(letter["DelayHours"] - visit["DelayHours"], 96)
        self.assertTrue(all(allowed(visit, set(held)) for held in endings))

    def test_patron_reports_do_not_require_foreign_romance_availability(self):
        from tools.crossroute_checks.mention_context import live_mentions
        for sid in ("jerribeth.refuge", "jerribeth.patron", "jerribeth.fate_envelope"):
            event = self.events[sid]
            self.assertNotIn("crossroute.vellexia.unavailable", event["Forbids"])
            for item in event["Nodes"]:
                self.assertEqual(live_mentions(item["Text"], re.compile(r"\bVellexia\b")), [], item["Id"])

    def test_slots_follow_chosen_intimacy_and_resume_old_aftermath(self):
        briefs = Path("tools/route_packs/explicit_slots/jerribeth")
        self.assertEqual(len(list(briefs.glob("*.json"))), 9)
        for path in briefs.glob("*.json"):
            brief = json.loads(path.read_text(encoding="utf-8"))
            event = self.events[brief["placement"]["scene"]]
            slot = route.node(event, brief["slot_id"])
            self.assertEqual(slot["Text"], brief["default_text"])
            self.assertTrue(any(a["Next"] == brief["placement"]["resume_node"] for a in slot["Choices"]))
            threshold = route.node(event, brief["placement"]["after_node"])
            self.assertTrue(any(a["Next"] == brief["slot_id"] for a in threshold["Choices"]))

    def test_scale_keep_return_and_actual_first_collection(self):
        for sid in ("jerribeth.future", "jerribeth.trickster.visit"):
            _, endings = walk(self.events[sid], set(), "morning_free")
            self.assertTrue(any(route.SCALE_BACK in held and route.SCALE not in held for held in endings))
            self.assertTrue(any({route.SCALE, route.SCALE_PAID} <= held for held in endings))
            self.assertTrue(all(route.SCALE not in held or route.SCALE_PAID in held for held in endings))

    def test_living_and_tenant_evening_attention_paths_have_answers(self):
        event = self.events["jerribeth.evening"]
        for state in (set(), {route.RETURNED, "jerribeth.trickster.cost.tenant"},
                      {route.RETURNED, "jerribeth.trickster.cost.tenant", "jerribeth.trickster.cost.host"}):
            visited, endings = walk(event, state)
            self.assertTrue(endings)
            if route.RETURNED in state:
                self.assertTrue(any(id == "tenant_evening" for id, held in visited))

    def test_visit_has_selectable_pause_and_native_partner_partitions(self):
        event = self.events["jerribeth.trickster.visit"]
        for fate in ((), (partner.PLANT,), (partner.DEAD,), (partner.CHIEF,),
                     (partner.PLANT, partner.RETURNED)):
            for stance in (partner.SHARE, partner.SECRET, partner.EXCLUSIVE):
                flags = {stance, partner.READY, *fate}
                visited, endings = walk(event, flags)
                self.assertTrue(endings)
                self.assertTrue(any(id == "visit_pause" for id, held in visited))
                self.assertTrue(all(route.LOST in held for held in endings))

    def test_late_unpaid_toast_requires_local_collection_or_refusal(self):
        event = self.events["jerribeth.trickster.epilogue.commit"]
        pages = {n["Id"]: n for n in event["Nodes"]}
        for carrier in (set(), {route.LEVY}):
            flags = {"trickster.ever", route.GRUDGE, *carrier}
            visited, endings = walk(event, flags)
            self.assertTrue(endings)
            self.assertTrue(any("late_interest_" in id for id, held in visited))
            for id, held in visited:
                for answer in pages[id]["Choices"]:
                    if allowed(answer, set(held)):
                        self.assertEqual(answer["Set"], [], (id, answer))
            # Test actual individual paths; a union of visited nodes cannot
            # establish that each signing paid the debt.
            pending = [(pages[event["Nodes"][0]["Id"]], False)]
            seen = set()
            while pending:
                item, paid = pending.pop()
                key = (item["Id"], paid)
                if key in seen:
                    continue
                seen.add(key)
                paid |= "late_interest_" in item["Id"] and item["Id"].split("_")[-2] == "paid"
                if item["Id"].startswith("late_local_signed_") or item["Id"].startswith("late_local_signed_mind_"):
                    self.assertTrue(paid, item["Id"])
                for answer in item["Choices"]:
                    if allowed(answer, flags) and answer.get("Next"):
                        pending.append((pages[answer["Next"]], paid))

    def test_legacy_inert_ending_exits_keep_mechanics(self):
        originals = [s for m in (jerribeth, jerribeth_trickster) for s in m.SCENES
                     if s["Owner"].endswith("Epilogue")]
        for before in originals:
            after = self.events[before["Id"]]
            for item in before["Nodes"]:
                if len(item["Choices"]) == 1 and not item["Choices"][0].get("Next"):
                    self.assertEqual(item["Choices"], route.node(after, item["Id"])["Choices"])


if __name__ == "__main__":
    unittest.main()
