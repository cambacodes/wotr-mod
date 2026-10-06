"""Commitment, disclosure, state coverage and unchanged Wenduag route contracts."""
import copy
import itertools
import unittest

from story_fixture import fresh_story
from storylines import wenduag_partner_stance as stance

W = "wenduag.trickster."


class WenduagPartnerStanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story = fresh_story()
        cls.scenes = {s["Id"]: s for s in cls.story["Scenes"]}

    def enabled(self, value, flags):
        return (set(value.get("Requires", ())) <= flags
                and not set(value.get("Forbids", ())) & flags
                and all(set(group) & flags for group in value.get("AnyGroups", ())))

    def claim_path(self, suffix, branch, flags):
        flags = set(flags)
        if branch == 1:
            flags.add(stance.EARNED)
        if stance.LANN_IN in flags and not set(stance.LANN_GONE) & flags:
            flags.add(stance.HERE)
        nodes = {n["Id"]: n for n in self.scenes[W + suffix]["Nodes"]}
        node = nodes["partner_intro"]
        self.assertTrue(self.enabled(node["Choices"][branch], flags))
        answer = node["Choices"][branch]
        visited = []
        for _ in range(20):
            flags.update(answer.get("Set", ()))
            node = nodes[answer["Next"]]
            visited.append(node["Id"])
            self.assertNotIn(stance.COMMITTED, flags)
            if node["Id"] == "want":
                return flags, visited
            answers = [a for a in node["Choices"] if self.enabled(a, flags)]
            self.assertTrue(answers, node["Id"])
            # The first enabled answer carries through the chosen stance;
            # additional answers in exclusive/secret are explicit backdowns.
            answer = answers[0]
        self.fail("stance failed to reach the unchanged claim decision")

    def test_all_stances_reach_original_claim_with_current_presence(self):
        for suffix, branch, state, returned in itertools.product(
                ("court.claim", "court.claim_in_person"), range(3),
                (set(), {stance.LANN_IN}, {"lann.kicked_out"}, {"lann.plot_absent"},
                 {stance.LANN_IN, "lann.kicked_out"}), (set(), {stance.RETURNED})):
            with self.subTest(suffix=suffix, branch=branch, state=state, returned=returned):
                flags, visited = self.claim_path(suffix, branch, state | returned)
                self.assertEqual({stance.STANCES[branch]}, set(stance.STANCES) & flags)
                self.assertIn(stance.ACK, flags)
                lann_nodes = {"partner_share_lann", "partner_exclusive_lann"}
                should_meet = branch < 2 and stance.LANN_IN in state and not set(stance.LANN_GONE) & state
                self.assertEqual(should_meet, bool(lann_nodes & set(visited)))
                self.assertEqual(should_meet, stance.KNOWN in flags)
                if branch == 1:
                    self.assertEqual(should_meet, stance.SEPARATED in flags)

    def test_dead_lann_is_memory_and_never_summoned(self):
        for suffix in ("court.claim", "court.claim_in_person"):
            flags, visited = self.claim_path(suffix, 3, {"lann.dead", stance.LANN_IN})
            self.assertEqual(["partner_memory", "want"], visited)
            self.assertFalse(set(stance.STANCES) & flags)

    def test_reveal_does_not_pay_cairn_trust(self):
        for branch in (0, 1):
            flags, visited = self.claim_path("court.claim", branch, {stance.LANN_IN, stance.RETURNED})
            self.assertIn("partner_share_shock" if branch == 0 else "partner_exclusive_shock", visited)
            self.assertFalse({stance.LANN_PAID, stance.LANN_PAID_LATE} & flags)
        nodes = {n["Id"]: n for n in self.scenes[W + "lann.found_out"]["Nodes"]}
        flags = {stance.KNOWN}
        self.assertEqual(["partner_already_seen"], [a["Next"] for a in nodes["start"]["Choices"] if self.enabled(a, flags)])
        self.assertEqual("price", nodes["partner_already_seen"]["Choices"][0]["Next"])
        self.assertEqual(4, len(nodes["price"]["Choices"]))

    def test_discovery_uses_existing_morning_event_and_has_persistent_fallout(self):
        original = self.scenes[W + "react.lann_morning"]
        discovered = self.scenes[W + "react.lann_secret"]
        self.assertEqual(original["AnswerLists"], discovered["AnswerLists"])
        self.assertTrue(set(original["Requires"]) <= set(discovered["Requires"]))
        self.assertIn(stance.SECRET, original["Forbids"])
        self.assertIn(stance.SECRET, discovered["Requires"])
        self.assertIn(stance.DISCOVERED, discovered["Forbids"])
        fallout = set(discovered["Nodes"][0]["Choices"][0]["Set"])
        self.assertTrue({stance.DISCOVERED, stance.SEPARATED, stance.KNOWN} <= fallout)
        self.assertNotIn(stance.CLOSED, fallout)
        self.assertTrue(set(stance.LANN_GONE) <= set(discovered["Forbids"]))

    def test_every_ending_page_has_all_current_states_and_stances(self):
        endings = [s for s in self.story["Scenes"]
                   if s.get("Relationship") == "wenduag" and s["Owner"].endswith("Epilogue")
                   and ".partner." not in s["Id"]]
        endings.append(self.scenes["wenduag.lastcall.page"])
        self.assertEqual(12, len(endings))
        state_guards = [({stance.LANN_IN}, set(stance.LANN_GONE)),
                        ({"lann.dead"}, set()),
                        ({"lann.kicked_out"}, {"lann.dead"}),
                        ({"lann.plot_absent"}, {"lann.dead", "lann.kicked_out"}),
                        (set(), {stance.LANN_IN, *stance.LANN_GONE})]
        for scene in endings:
            for node in scene["Nodes"]:
                # Native replacements are single-text variants, not paragraph
                # pages. Their exhaustive selection contract is checked below.
                if not node.get("Paragraphs"):
                    self.assertTrue(any(scene["Id"] == v["Replacement"]
                                        for edit in self.story["NativeEpilogueEdits"].values()
                                        for v in [edit, *edit.get("Variants", [])]))
                    continue
                paragraphs = node["Paragraphs"]
                for required, forbidden in state_guards:
                    self.assertTrue(any(set(p.get("Requires", ())) == required
                                        and set(p.get("Forbids", ())) == forbidden
                                        for p in paragraphs), (scene["Id"], required))
                for flag in stance.STANCES:
                    self.assertTrue(any(flag in p["Requires"] for p in paragraphs), (scene["Id"], flag))

    def test_native_variants_partition_all_current_states_and_stance_histories(self):
        originals = [s for s in self.story["Scenes"] if s["Id"].startswith(W + "epilogue.native_")
                     and ".partner." not in s["Id"]]
        self.assertEqual(6, len(originals))
        positions = (set(), {stance.SHARE}, {stance.SHARE, stance.SHARED},
                     {stance.EXCLUSIVE}, {stance.EXCLUSIVE, stance.SEPARATED},
                     {stance.SECRET}, {stance.SECRET, stance.DISCOVERED, stance.SEPARATED})
        fixed = {"trickster", "trickster.ever", "trickster.now", "trickster.commander_back", W + "native"}
        for original in originals:
            # Hold finalized body/payoff eligibility true while varying the
            # partner state and stance. Those independent engine guards are not
            # the selection partition this matrix is testing.
            eligible = fixed | (set(original["Requires"]) - {
                stance.COMMITTED, stance.LANN_IN, *stance.LANN_GONE,
                *stance.STANCES, stance.SHARED, stance.SEPARATED, stance.DISCOVERED})
            variants = [s for s in self.story["Scenes"] if s["Id"] == original["Id"]
                        or s["Id"].startswith(original["Id"] + ".partner.")]
            commitments = (True,) if stance.COMMITTED in original["Requires"] else (False, True)
            if stance.COMMITTED in original["Forbids"]:
                commitments = (False,)
            for bits, position, committed in itertools.product(itertools.product((False, True), repeat=4), positions, commitments):
                flags = eligible | position | {f for f, bit in zip((stance.LANN_IN, *stance.LANN_GONE), bits) if bit}
                if committed:
                    flags.add(stance.COMMITTED)
                enabled = [s for s in variants if self.enabled(s, flags)]
                self.assertEqual(1, len(enabled), (original["Id"], bits, position, committed))
                self.assertFalse(enabled[0]["Nodes"][0].get("Paragraphs"))
        for edit in self.story["NativeEpilogueEdits"].values():
            for variant in [edit, *edit.get("Variants", [])]:
                if variant["Replacement"].startswith(W + "epilogue.native_"):
                    self.assertTrue(all("trickster.now" in group for group in variant["When"]))

    def test_old_commitment_choices_and_outcomes_are_retained(self):
        for suffix in ("court.claim", "court.claim_in_person"):
            nodes = {n["Id"]: n for n in self.scenes[W + suffix]["Nodes"]}
            self.assertEqual(["given", "knelt", "struck", "no"],
                             [a["Next"] for a in nodes["want"]["Choices"]])
            for name, outcome in (("given", "given"), ("knelt", "knelt"), ("struck", "struck")):
                flags = set(nodes["after_" + name]["Choices"][0]["Set"])
                self.assertTrue({stance.COMMITTED, "wenduag.started", W + "claim." + outcome} <= flags)
            self.assertIn(stance.CLOSED, nodes["no"]["Choices"][0]["Set"])

    def test_native_text_variants_retain_final_outcome_eligibility(self):
        extra = {stance.LANN_IN, *stance.LANN_GONE, *stance.STANCES,
                 stance.SHARED, stance.SEPARATED, stance.DISCOVERED}
        families = (("native_pack", "pack"), ("native_greybor", "pack"),
                    ("native_ember", "pack"), ("native_greybor_back", "native_commander_back"),
                    ("native_commander_back", "native_commander_back"))
        for family, outcome in families:
            source = self.scenes[W + "epilogue." + outcome]
            prefix = W + "epilogue." + family
            for item in self.story["Scenes"]:
                if item["Id"] != prefix and not item["Id"].startswith(prefix + ".partner."):
                    continue
                self.assertTrue(set(source["Requires"]) - extra <= set(item["Requires"]), item["Id"])
                self.assertTrue(set(source["Forbids"]) - extra <= set(item["Forbids"]), item["Id"])
                self.assertEqual(source.get("ForbidOverrides", {}), item.get("ForbidOverrides", {}), item["Id"])
                self.assertEqual(source.get("RequiresAnyGroups", []), item.get("RequiresAnyGroups", []), item["Id"])

    def test_breakup_survives_later_refusal_of_commitment(self):
        flags, _ = self.claim_path("court.claim", 1, {stance.LANN_IN})
        scene = self.scenes[W + "court.claim"]
        refusal = next(n for n in scene["Nodes"] if n["Id"] == "no")["Choices"][0]
        flags.update(refusal["Set"])
        self.assertNotIn(stance.COMMITTED, flags)
        ending = self.scenes[W + "epilogue.refused"]["Nodes"][0]
        self.assertTrue(any(self.enabled(p, flags) and stance.EXCLUSIVE in p["Requires"]
                            and stance.SEPARATED in p["Requires"] for p in ending["Paragraphs"]))

    def test_lastcall_template_is_idempotent(self):
        from storylines import lastcall_partners
        # The first assembly may have occurred in story_fixture's child process.
        def payload():
            return copy.deepcopy({"Scenes": [s for s in self.story["Scenes"] if s.get("Relationship") == "wenduag"],
                                  "NativeEpilogueEdits": {k: v for k, v in self.story["NativeEpilogueEdits"].items()
                                                          if v["Replacement"].startswith(W)}})
        story = payload()
        stance.integrate(story)
        part = next(p for p in lastcall_partners.PARTNERS if p["key"] == "wenduag")
        before = copy.deepcopy(part["paragraphs"])
        stance.integrate(payload())
        self.assertEqual(before, part["paragraphs"])

    def test_native_text_partition_leaves_other_routes_records_unchanged(self):
        unrelated = dict(Replacement="other.ending", When=[["trickster.now", "other.committed"]])
        payload = dict(Scenes=copy.deepcopy([s for s in self.story["Scenes"]
                                            if s.get("Relationship") == "wenduag"]),
                       NativeEpilogueEdits={"other": copy.deepcopy(unrelated)})
        stance._native_variants(payload, {s["Id"]: s for s in payload["Scenes"]})
        self.assertEqual(unrelated, payload["NativeEpilogueEdits"]["other"])


if __name__ == "__main__":
    unittest.main()
