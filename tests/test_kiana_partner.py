"""Route-local stance outcomes, native discovery attachment and state partitions."""
import copy
import unittest

from storylines import kiana, kiana_partner as partner, kiana_trickster, kiana_progression
from story_format import c, n, scene


def holds(block, flags):
    return (all(key in flags for key in block.get("Requires", []))
            and not any(key in flags for key in block.get("Forbids", []))
            and all(any(key in flags for key in group) for group in block.get("AnyGroups", [])))


def walk(nodes, start, flags):
    by_id = {node["Id"]: node for node in nodes}
    outcomes = []
    def visit(key, state, visited):
        if key in visited:
            raise AssertionError("Cycle in partner conversation")
        node = by_id[key]
        available = [answer for answer in node["Choices"] if holds(answer, state)]
        if not available:
            raise AssertionError("Page has no selectable answers: " + key)
        for answer in available:
            after = state | set(answer["Set"])
            if answer["Next"] is None:
                outcomes.append(after)
            else:
                visit(answer["Next"], after, visited | {key})
    visit(start, set(flags), set())
    return outcomes


class KianaPartnerTests(unittest.TestCase):
    def payload(self):
        scenes = copy.deepcopy(kiana.SCENES + kiana_progression.SCENES + kiana_trickster.SCENES)
        ep = next(s for s in scenes if s["Id"] == "kiana.trickster.epilogue.commit")
        # The preceding existing appender supplies the two late acceptance choices.
        for old in ep["Nodes"][0]["Choices"][:2]:
            ep["Nodes"][0]["Choices"].append(c(old["Text"], old["Next"],
                flags=("kiana.trickster.late_yes",), forbids=("kiana.trickster.late_yes", "kiana.trickster.late_no")))
        scenes.append(scene("kiana.lastcall.page", "", "Epilogue", 1, "", [n("page", "Narrator", "", c())]))
        payload = dict(Scenes=scenes, SeenCues={}, Etudes={}, Derived={})
        partner.integrate(payload)
        return payload

    def test_every_commitment_host_offers_each_stance_with_earned_outcomes(self):
        data = self.payload()
        for sid in ("kiana.morning", "kiana.trickster.late_question", "kiana.trickster.late_question_letter", "kiana.trickster.epilogue.commit"):
            host = next(s for s in data["Scenes"] if s["Id"] == sid)
            outcomes = walk(host["Nodes"], "partner_terms", {partner.OPEN, "kiana.company", "kiana.rehearsed"})
            for stance in (partner.SHARE, partner.EXCLUSIVE, partner.SECRET):
                accepted = [s for s in outcomes if stance in s and "kiana.closed" not in s]
                self.assertTrue(accepted, sid + ": " + stance)
                for state in accepted:
                    self.assertEqual(len(state & {partner.SHARE, partner.EXCLUSIVE, partner.SECRET}), 1)
                    if stance == partner.SHARE:
                        self.assertIn("kiana.partner_elan_terms_kept", state)
                        self.assertNotIn("kiana.separated", state)
                    elif stance == partner.EXCLUSIVE:
                        self.assertIn("kiana.separated", state)
                        self.assertIn("kiana.partner_breakup_spoken", state)
                    else:
                        self.assertIn("kiana.affair", state)
                        self.assertNotIn("kiana.separated", state)
            refused = [s for s in outcomes if partner.EXCLUSIVE in s and "kiana.closed" in s]
            self.assertTrue(refused)
            self.assertTrue(all("kiana.committed" not in s for s in refused))

    def test_dead_partner_has_no_live_terms_or_stance_switch(self):
        outcomes = walk(partner.stance_nodes(("kiana.committed",)), "partner_terms", {partner.DEAD})
        for state in outcomes:
            self.assertFalse(state & {partner.SHARE, partner.SECRET, partner.EXCLUSIVE})
        self.assertTrue(any("kiana.committed" in state for state in outcomes))

    def test_later_first_promise_keeps_earned_separation(self):
        host = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.a_place_afterward")
        for state in walk(host["Nodes"], "choose", {"kiana.separated"}):
            self.assertIn(partner.EXCLUSIVE, state)
            self.assertIn("kiana.committed", state)
        for state in walk(host["Nodes"], "choose", {"kiana.bereaved"}):
            self.assertFalse(state & {partner.SHARE, partner.EXCLUSIVE, partner.SECRET})

    def test_discovery_is_native_local_and_ends_the_affair(self):
        host = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.partner_discovery")
        self.assertEqual(host["AnswerLists"], [partner.AFTERMATH_LIST])
        self.assertTrue(holds(host, {"trickster.now", partner.SECRET}))
        for flags in ({partner.SECRET, "trickster.ever"}, {"trickster.now"},
                      {"trickster.now", partner.SECRET, partner.DEAD},
                      {"trickster.now", partner.SECRET, "kiana.closed"}):
            self.assertFalse(holds(host, flags))
        for state in walk(host["Nodes"], "start", {"trickster.now", partner.SECRET}):
            self.assertTrue({partner.EXPOSED, "kiana.closed", "kiana.stayed_married"} <= state)
            self.assertNotIn("kiana.separated", state)

    def test_after_reunion_courtship_can_discover_through_existing_seelah_event(self):
        seelah = next(s for s in self.payload()["Scenes"] if s["Id"] == "kiana.seelah")
        entrance = next(a for a in seelah["Nodes"][0]["Choices"] if a.get("Next") == "partner_discovery")
        self.assertEqual(entrance["Next"], "partner_discovery")
        self.assertTrue(holds(entrance, {partner.SECRET}))
        self.assertFalse(holds(entrance, {partner.SECRET, partner.DEAD}))
        for state in walk(seelah["Nodes"], "partner_discovery", {partner.SECRET}):
            self.assertTrue({partner.EXPOSED, "kiana.closed", "kiana.stayed_married"} <= state)

    def test_current_fate_partition_never_inferrs_life_from_old_grief(self):
        paras = partner.partner_paragraphs()
        for flags in (set(), {"kiana.bereaved"}, {"kiana.history_married"},
                      {partner.DEAD}, {partner.LIVE}, {partner.LIVE, partner.DEAD}):
            # The first seven paragraphs partition current state. Later ones
            # separately account for stance and historical separation.
            active = [p for p in paras[:7] if holds(p, flags)]
            self.assertEqual(len(active), 1, flags)
            if "kiana.bereaved" in flags:
                self.assertEqual(active[0]["Forbids"], [partner.DEAD, partner.LIVE])

    def test_every_ending_page_and_lastcall_has_route_local_accounting(self):
        payload = self.payload()
        for host in payload["Scenes"]:
            if host.get("Relationship") != "kiana" and host["Id"] != "kiana.lastcall.page":
                continue
            if host["Owner"] != "Epilogue":
                continue
            for node in host["Nodes"]:
                paragraphs = node.get("Paragraphs", [])
                for state in (set(), {partner.DEAD}, {partner.LIVE, partner.SHARE},
                              {partner.LIVE, partner.SECRET}, {partner.LIVE, "kiana.separated"}):
                    self.assertTrue(any(holds(p, state) for p in paragraphs), host["Id"] + "/" + node["Id"])
        self.assertEqual(payload["SeenCues"]["kiana.elan.death_seen"], partner.DEATH_CUES)
        self.assertEqual(payload["Etudes"][partner.LIVE], "e5e3765b11eec1244a2137c2999f00d1")
        # A Drezen-only Playing etude cannot supply a global death observer.
        self.assertEqual(payload["Derived"][partner.DEAD], [["kiana.elan.death_seen"]])


if __name__ == "__main__":
    unittest.main()
