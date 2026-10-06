"""The authored disguise disclosure records history without adding a partner gate."""
import unittest

from expansion import make_expansion
from storylines import lastcall_partners, nidalynn_trickster as route


class NidalynnPartnerClaimTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = make_expansion()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def test_every_reveal_answer_records_the_disguise(self):
        reveal = self.scenes[route.P + "hearth.listening"]
        name = next(n for n in reveal["Nodes"] if n["Id"] == "name")
        self.assertEqual([c["Next"] for c in name["Choices"]], ["dragon", "belly", "second"])
        for choice in name["Choices"]:
            self.assertEqual(choice["Set"], [route.REVEALED, route.PARTNER_DISGUISE])

    def test_both_commitments_keep_the_existing_choices_and_record_history(self):
        expected = {
            route.P + "ridge.first_flight": ("offer", [route.COMMITTED, route.SALT, route.PROPOSED]),
            route.P + "kiln.the_heel": ("wait", [route.COMMITTED, route.SALT]),
        }
        actual = []
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") != route.REL:
                continue
            for node in scene["Nodes"]:
                for index, choice in enumerate(node["Choices"]):
                    if route.COMMITTED not in choice.get("Set", []):
                        continue
                    actual.append(scene["Id"])
                    node_id, old_flags = expected[scene["Id"]]
                    self.assertEqual((node["Id"], index), (node_id, 0))
                    self.assertEqual(choice["Set"], [*old_flags, route.PARTNER_DISGUISE])
                    self.assertEqual(choice["Requires"], ["trickster.now"])
                    self.assertFalse(choice["Forbids"])
        self.assertCountEqual(actual, expected)

    def test_no_stance_or_eligibility_gate_for_a_fictional_bond(self):
        for scene in self.story["Scenes"]:
            if scene.get("Relationship") != route.REL and scene["Id"] != "nidalynn.lastcall.page":
                continue
            contexts = [scene, *scene["Nodes"]]
            contexts.extend(c for n in scene["Nodes"] for c in n["Choices"])
            contexts.extend(p for n in scene["Nodes"] for p in n.get("Paragraphs", []))
            for context in contexts:
                for field in ("Requires", "Forbids", "Set"):
                    flags = context.get(field, [])
                    self.assertFalse(any(f.startswith("nidalynn.partner_stance.") for f in flags))
                    if field != "Set":
                        self.assertNotIn(route.PARTNER_DISGUISE, flags)

    def test_all_nine_endings_keep_existing_paragraph_indices(self):
        counts = dict(salt=25, late=22, heel=22, wolves=0, unreturned=22,
                      apart=22, claimed=22, lie=22, given=0)
        for ending, count in counts.items():
            scene = self.scenes[route.P + "epilogue." + ending]
            self.assertIn("trickster.ever", scene["Requires"])
            page = scene["Nodes"][0]
            self.assertEqual(page["Id"], "page")
            # Static history keeps the wolves/fire pages free of conditional paragraphs
            # and leaves all other endings' existing paragraph indices intact.
            self.assertEqual(len(page["Paragraphs"]), count)

    def test_lastcall_extension_is_local_and_idempotent(self):
        page = self.scenes["nidalynn.lastcall.page"]["Nodes"][0]
        self.assertEqual(page["Id"], "page")
        self.assertEqual(len(page["Paragraphs"]), 10)
        self.assertFalse(page["Paragraphs"][7]["Requires"])
        self.assertFalse(page["Paragraphs"][7]["Forbids"])
        def states():
            return [(part["rel"], [(tuple(p["Requires"]), tuple(p["Forbids"]),
                                   tuple(tuple(g) for g in p["AnyGroups"]))
                                  for p in part["paragraphs"]])
                    for part in lastcall_partners.PARTNERS]
        before = states()
        payload = {"Presences": {}, "SeenCues": {}}
        route.integrate(payload)
        route.integrate(payload)
        self.assertEqual(states(), before)


if __name__ == "__main__":
    unittest.main()
