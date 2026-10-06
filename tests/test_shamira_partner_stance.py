"""State/ID checks for Shamira's partner decisions; no prose snapshots."""
import copy
import json
from pathlib import Path
import unittest

from storylines import shamira_dream, shamira_trickster, shamira_partner as partner


def visible(choice, flags):
    return set(choice.get("Requires", ())) <= flags and not set(choice.get("Forbids", ())) & flags


def walk(scene, flags=(), start="start"):
    nodes = {node["Id"]: node for node in scene["Nodes"]}
    results = []

    def visit(id, state, trace):
        if id is None:
            results.append((state, trace))
            return
        if id in trace:
            raise AssertionError("Cycle: " + id)
        choices = [choice for choice in nodes[id]["Choices"] if visible(choice, state)]
        if not choices:
            raise AssertionError("No selectable answer: " + id)
        for choice in choices:
            visit(choice.get("Next"), state | set(choice.get("Set", ())), trace + [id])

    visit(start, set(flags), [])
    return results


class ShamiraPartnerStanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Integration exercises the route's actual generator, independently of
        # whether a caller has a fresh development export.
        cls.base = copy.deepcopy(shamira_trickster.SCENES + shamira_dream.SCENES)
        payload = {"Scenes": copy.deepcopy(cls.base)}
        partner.integrate(payload)
        cls.scenes = {scene["Id"]: scene for scene in payload["Scenes"]}
        cls.states = tuple(("trickster.now", *state) for state in
                           ((), (partner.DEAD, partner.HIDING), (partner.DEAD,),
                            (partner.DEAD, partner.HIDING, partner.RETURNED)))

    def test_save_references_and_original_answer_positions_remain(self):
        for before in self.base:
            after = self.scenes[before["Id"]]
            old_ids = [node["Id"] for node in before["Nodes"]]
            self.assertEqual([node["Id"] for node in after["Nodes"][:len(old_ids)]], old_ids)
            for old, new in zip(before["Nodes"], after["Nodes"]):
                self.assertGreaterEqual(len(new["Choices"]), len(old["Choices"]))
            if before["Id"] in (partner.P + "harem", partner.P + "harem_awning"):
                search = next(node for node in after["Nodes"] if node["Id"] == "search")
                self.assertEqual([c.get("Next") for c in search["Choices"][:3]], ["lost", "won", "thrown"])
                for index, flag in enumerate((partner.P + "lost_on_purpose", partner.ALLY, partner.CLOSED)):
                    self.assertIn(flag, search["Choices"][index]["Set"])
                self.assertNotIn(partner.COMMITTED, search["Choices"][0]["Set"])
            for field in ("Requires", "Forbids", "MinChapter", "MaxChapter"):
                self.assertEqual(before[field], after[field])

    def test_commitment_requires_chosen_terms_in_both_placements(self):
        for id in (partner.P + "harem", partner.P + "harem_awning"):
            for state in self.states:
                results = walk(self.scenes[id], state)
                for flags, trace in results:
                    if partner.COMMITTED in flags:
                        self.assertIn("partner_start", trace)
                        self.assertEqual(sum(flag in flags for flag in (partner.SHARE, partner.SECRET)), 1)
                        self.assertNotIn(partner.EXCLUSIVE, flags)
                    if partner.EXCLUSIVE in flags:
                        self.assertIn(partner.CLOSED, flags)
                        self.assertNotIn(partner.COMMITTED, flags)
                    self.assertNotIn(partner.RETURNED, flags - set(state))
                self.assertTrue(any(partner.COMMITTED in flags and partner.CLOSED not in flags for flags, _ in results))
                self.assertTrue(any(partner.EXCLUSIVE in flags for flags, _ in results))

    def test_sharing_has_partner_response_before_commitment(self):
        for state, want in zip(self.states, ("alive", "hiding", "dead", "returned")):
            for flags, trace in walk(self.scenes[partner.P + "harem"], state):
                if partner.SHARE not in flags:
                    continue
                self.assertIn("partner_share_" + want, trace)
                if want != "dead":
                    self.assertIn(partner.KNOWN, flags)
                    self.assertIn(partner.PAID, flags)
                    self.assertIn("partner_public_court", trace)
                else:
                    self.assertNotIn(partner.KNOWN, flags)

    def test_secret_discovery_and_breakup_in_existing_court(self):
        for state, want in zip(self.states, ("alive", "hiding", "dead", "returned")):
            results = [(flags, trace) for flags, trace in walk(self.scenes[partner.P + "harem"], state)
                       if partner.SECRET in flags]
            self.assertTrue(results)
            for flags, trace in results:
                self.assertIn("partner_discovery", trace)
                self.assertIn("partner_found_" + want, trace)
                self.assertIn(partner.EXPOSED, flags)
                self.assertNotIn("partner_public_court", trace)
                if want != "dead":
                    self.assertTrue(partner.PAID in flags or partner.BROKEN in flags)
                if partner.BROKEN in flags:
                    self.assertIn(partner.CLOSED, flags)
                    self.assertNotIn("bell_end", trace)

    def test_late_page_records_terms_without_new_eligibility_or_return(self):
        for state in self.states:
            for flags, trace in walk(self.scenes[partner.P + "epilogue.late"], state, start="page"):
                if trace == ["page"]:
                    self.assertEqual(flags, set(state))
                    continue
                self.assertEqual(sum(flag in flags for flag in (partner.SHARE, partner.EXCLUSIVE, partner.SECRET)), 1)
                self.assertNotIn(partner.COMMITTED, flags)
                self.assertNotIn(partner.RETURNED, flags - set(state))
                self.assertIn("partner_late_no" if partner.CLOSED in flags else "partner_late_end", trace)

    def test_every_epilogue_and_lastcall_has_disjoint_current_states_and_stances(self):
        from storylines import lastcall_partners
        pages = [scene["Nodes"][0] for id, scene in self.scenes.items()
                 if id.startswith(partner.P + "epilogue.")]
        pages += self.scenes[partner.P + "epilogue.late"]["Nodes"][1:]
        pages += [next(scene for _, scene in lastcall_partners.pages()
                       if scene["Id"] == "shamira.lastcall.page")["Nodes"][0]]
        for node in pages:
            paragraphs = node.get("Paragraphs", ())
            current = [p for p in paragraphs if
                       ((partner.DEAD in (*p.get("Requires", ()), *p.get("Forbids", ()))
                         or partner.HIDING in p.get("Requires", ()))
                        and partner.RETURNED in (*p.get("Requires", ()), *p.get("Forbids", ())))
                       or partner.RETURNED in p.get("Requires", ())]
            for state in self.states:
                self.assertEqual(sum(visible(p, set(state)) for p in current), 1)
            if node["Id"] in ("page", "partner_late_end", "partner_late_no"):
                for stance in (partner.SHARE, partner.EXCLUSIVE, partner.SECRET):
                    self.assertTrue(any(stance in p.get("Requires", ()) for p in paragraphs))

    def test_broken_committed_affair_has_an_ending(self):
        scene = self.scenes[partner.P + "epilogue.closed_door"]
        self.assertEqual(scene["ForbidOverrides"].get(partner.COMMITTED), partner.BROKEN)
        self.assertIn(partner.CLOSED, scene["Requires"])

    def test_generated_partner_state_is_independent_of_nocticula_romance_closure(self):
        path = Path(__file__).resolve().parents[1] / "development" / "Story.json"
        story = json.loads(path.read_text(encoding="utf-8"))
        for scene in story["Scenes"]:
            if scene["Id"] not in self.scenes and scene["Id"] != "shamira.lastcall.page":
                continue
            if scene["Id"] in (partner.P + "harem", partner.P + "harem_awning"):
                search = next(node for node in scene["Nodes"] if node["Id"] == "search")
                # The generator originally appended this answer after the
                # three authored game answers; its serialized index is saved.
                self.assertGreaterEqual(len(search["Choices"]), 4)
                leave = search["Choices"][3]
                self.assertTrue(leave["Abort"])
                self.assertIsNone(leave.get("Next"))
                self.assertEqual(leave["Set"], [])
                self.assertEqual(leave["Requires"], [])
                self.assertEqual(leave["Forbids"], ["trickster.now"])
                self.assertFalse(any("crossroute.nocticula" in flag for flag in
                                     search["Choices"][0]["Requires"] + search["Choices"][0]["Forbids"]))
            if not (scene["Id"].startswith(partner.P + "epilogue.") or scene["Id"] == "shamira.lastcall.page"):
                continue
            current = [p for p in scene["Nodes"][0].get("Paragraphs", ()) if
                       (partner.DEAD in (*p.get("Requires", ()), *p.get("Forbids", ()))
                        and partner.RETURNED in (*p.get("Requires", ()), *p.get("Forbids", ())))
                       or (partner.HIDING in p.get("Requires", ()) and partner.RETURNED in p.get("Forbids", ()))
                       or partner.RETURNED in p.get("Requires", ())]
            for state in self.states:
                self.assertEqual(sum(visible(p, set(state) | {"noct.closed"}) for p in current), 1,
                                 scene["Id"] + ": partner status lost behind another romance's gate")


if __name__ == "__main__":
    unittest.main()
