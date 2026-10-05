import copy
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools import canon_partner_lint as lint


def choice(text="Continue", next_node=None, sets=(), requires=(), forbids=()):
    return dict(Text=text, Next=next_node, Set=list(sets), Requires=list(requires), Forbids=list(forbids))


def node(nid, text, *choices, paragraphs=()):
    return dict(Id=nid, Text=text, Speaker="Woman", Choices=list(choices), Paragraphs=list(paragraphs))


def scene(sid, nodes, chapter=3, owner="Woman", requires=(), forbids=(), **extra):
    return dict(Id=sid, Relationship="woman", Owner=owner, MinChapter=chapter, MaxChapter=chapter,
                Nodes=nodes, Requires=list(requires), Forbids=list(forbids), **extra)


def fixture():
    registry = dict(roster=[dict(woman="Woman", relationship="woman", partners=[dict(
        name="Partner", relationship_type="wife", aliases=["Patsy"], scope="campaign",
        native_fates=[dict(state="alive", when=[["!partner.dead"]]),
                      dict(state="dead", when=[["partner.dead"]])])])])
    story = dict(Relationships={"woman": dict(StartedFlag="woman.started", ClosedFlag="woman.closed",
                                             CommittedFlag="woman.committed")},
                 Etudes={"partner.dead": "a" * 32}, Scenes=[
        scene("ack", [node("start", "Partner is my wife. She knows about us.", choice())], forbids=["woman.committed"]),
        scene("commit", [node("start", "Stay with me.", choice(sets=["woman.committed"]))]),
        scene("ending", [node("page", "Our days continued.", choice(), paragraphs=[
            dict(Text="Partner stayed with us.", Requires=[], Forbids=["partner.dead"]),
            dict(Text="Partner died; we kept her letters.", Requires=["partner.dead"], Forbids=[])])],
              chapter=6, owner="WomanEpilogue", requires=["woman.committed"])])
    return story, registry


class CanonPartnerTests(unittest.TestCase):
    def codes(self, story, registry):
        return [r["code"] for r in lint.check(story, registry)["findings"]]

    def test_coherent_fixture_and_inputs_not_rewritten(self):
        story, registry = fixture()
        before = copy.deepcopy(story)
        self.assertEqual(self.codes(story, registry), [])
        # The shared verifier normalizes missing fields, but leaves prose,
        # choice ordering, state and IDs intact.
        for old, current in zip(before["Scenes"], story["Scenes"]):
            self.assertEqual(old["Id"], current["Id"])
            for a, b in zip(old["Nodes"], current["Nodes"]):
                self.assertEqual(a["Text"], b["Text"])
                self.assertEqual(a["Id"], b["Id"])
                self.assertEqual([c["Set"] for c in a["Choices"]], [c["Set"] for c in b["Choices"]])

    def test_missing_acknowledgement_and_ending(self):
        story, registry = fixture()
        story["Scenes"] = story["Scenes"][1:2]
        self.assertIn("acknowledgement_before_commitment", self.codes(story, registry))
        self.assertIn("partner_state_ending_coverage", self.codes(story, registry))

    def test_postcommit_mention_does_not_acknowledge_before_commitment(self):
        story, registry = fixture()
        story["Scenes"][0]["Requires"] = ["woman.committed"]
        story["Scenes"][0]["Forbids"] = []
        self.assertIn("acknowledgement_before_commitment", self.codes(story, registry))

    def test_later_chapter_ack_is_too_late(self):
        story, registry = fixture()
        story["Scenes"][0].update(MinChapter=5, MaxChapter=5, Forbids=[])
        self.assertIn("acknowledgement_before_commitment", self.codes(story, registry))

    def test_earlier_chapter_postcommit_ack_is_still_too_late(self):
        story, registry = fixture()
        story["Scenes"][0].update(MinChapter=2, MaxChapter=2, Requires=["woman.committed"], Forbids=[])
        self.assertIn("acknowledgement_before_commitment", self.codes(story, registry))

    def test_same_scene_ack_dominates_commitment(self):
        story, registry = fixture()
        story["Scenes"].pop(0)
        story["Scenes"][0]["Nodes"].insert(0, node("ack", "Patsy knows and will join us.", choice(next_node="start")))
        self.assertNotIn("acknowledgement_before_commitment", self.codes(story, registry))

    def test_bypass_cannot_claim_dominance(self):
        story, registry = fixture()
        story["Scenes"].pop(0)
        story["Scenes"][0]["Nodes"] = [node("entry", "Choose.", choice(next_node="ack"), choice(next_node="start")),
                                        node("ack", "Partner knows.", choice(next_node="start")),
                                        node("start", "Stay.", choice(sets=["woman.committed"]))]
        self.assertIn("acknowledgement_before_commitment", self.codes(story, registry))

    def test_ungated_commitment_absence(self):
        story, registry = fixture()
        story["Scenes"][1]["Nodes"][0]["Text"] = "Partner is dead. Stay."
        self.assertIn("ungated_commitment_absence", self.codes(story, registry))
        story["Scenes"][1]["Requires"] = ["partner.dead"]
        self.assertNotIn("ungated_commitment_absence", self.codes(story, registry))

    def test_all_incoming_edges_must_guard_absence(self):
        story, registry = fixture()
        story["Scenes"][1]["Nodes"] = [node("entry", "Choose.", choice(next_node="claim", requires=["partner.dead"]),
                                                                    choice(next_node="claim")),
                                        node("claim", "Partner is dead.", choice(sets=["woman.committed"]))]
        self.assertIn("ungated_commitment_absence", self.codes(story, registry))
        story["Scenes"][1]["Nodes"][0]["Choices"][1]["Requires"] = ["partner.dead"]
        self.assertNotIn("ungated_commitment_absence", self.codes(story, registry))

    def test_denial_is_not_absence_assertion(self):
        story, registry = fixture()
        story["Scenes"][1]["Nodes"][0]["Text"] = "Partner is not dead. I love her."
        self.assertNotIn("ungated_commitment_absence", self.codes(story, registry))

    def test_ending_both_states_needed(self):
        story, registry = fixture()
        story["Scenes"][2]["Nodes"][0]["Paragraphs"].pop()
        self.assertIn("missing_partner_state", self.codes(story, registry))

    def test_ungated_name_drop_is_not_state_coverage(self):
        story, registry = fixture()
        story["Scenes"][2]["Nodes"][0]["Paragraphs"] = []
        story["Scenes"][2]["Nodes"][0]["Text"] = "Partner stayed."
        self.assertIn("partner_state_ending_coverage", self.codes(story, registry))

    def test_other_ending_cannot_cover_missing_page(self):
        story, registry = fixture()
        story["Scenes"].append(scene("other_ending", [node("page", "We stayed together.", choice())],
                                     chapter=6, owner="WomanEpilogue", requires=["woman.committed"]))
        result = lint.check(story, registry)
        gaps = [r for r in result["findings"] if r["code"] == "partner_state_page_gap"]
        self.assertEqual([r["scene"] for r in gaps], ["other_ending"])

    def test_complementary_paragraphs_cover_all_incoming_histories(self):
        story, registry = fixture()
        story["Scenes"][2]["Nodes"][0]["Paragraphs"] = [
            dict(Text="Partner stayed near.", Requires=["choice.a"], Forbids=["partner.dead"]),
            dict(Text="Partner lived elsewhere.", Requires=[], Forbids=["partner.dead", "choice.a"]),
            dict(Text="Partner died.", Requires=["partner.dead"], Forbids=[])]
        self.assertEqual(self.codes(story, registry), [])
        story["Scenes"][2]["Nodes"][0]["Paragraphs"].pop(1)
        self.assertIn("partner_state_page_gap", self.codes(story, registry))

    def test_native_override_is_not_an_epilogue(self):
        story, registry = fixture()
        story["Scenes"][2]["NativeReturnCue"] = "b" * 32
        self.assertIn("partner_state_ending_coverage", self.codes(story, registry))

    def test_lastcall_conversation_is_not_a_postwar_page(self):
        story, registry = fixture()
        story["Scenes"].append(scene("woman.lastcall.call", [node("hello", "Come to me.", choice())],
                                     requires=["woman.committed"]))
        self.assertEqual(self.codes(story, registry), [])

    def test_registered_native_dialogue_and_variants_are_not_endings(self):
        story, registry = fixture()
        native = copy.deepcopy(story["Scenes"][2])
        native["Id"] = "aftermath"
        variant = copy.deepcopy(native)
        variant["Id"] = "aftermath.other"
        story["Scenes"][2:] = [native, variant]
        story["NativeOverrides"] = [dict(Target="cue", TargetType="cue", Evidence="World/Dialogs/Quest/Aftermath.jbp")]
        story["NativeEpilogueEdits"] = {"cue": dict(Replacement="aftermath", Variants=[dict(Replacement="aftermath.other")])}
        self.assertIn("partner_state_ending_coverage", self.codes(story, registry))
        story["NativeOverrides"][0].update(TargetType="slide", Evidence="World/Dialogs/Epilogues/Cue.jbp")
        self.assertEqual(self.codes(story, registry), [])

    def test_native_breakup_does_not_prove_current_death(self):
        story, registry = fixture()
        partner = registry["roster"][0]["partners"][0]
        partner["native_resolution"] = dict(status="former", reason="Native farewell and reaction.")
        story["Scenes"].pop(2)
        self.assertEqual(self.codes(story, registry), [])
        story["Scenes"][1]["Nodes"][0]["Text"] = "Partner is dead. Stay with me."
        self.assertIn("ungated_commitment_absence", self.codes(story, registry))

    def test_coercion_and_dlc_counterpart_scope_is_explicit(self):
        for scope in ("coercion", "dlc1_anomaly"):
            with self.subTest(scope=scope):
                story, registry = fixture()
                registry["roster"][0]["partners"][0]["scope"] = scope
                story["Scenes"] = story["Scenes"][1:2]
                result = lint.check(story, registry)
                self.assertEqual(result["entries"][0]["scope_review"], scope)
                self.assertEqual(result["findings"], [])

    def test_shared_lastcall_checked_separately(self):
        story, registry = fixture()
        entry = registry["roster"][0]
        entry["shared_scene_ids"] = ["woman.lastcall.page"]
        page = scene("woman.lastcall.page", [node("page", "The Commander came home.", choice())], owner="Epilogue")
        page["Relationship"] = "lastcall"
        story["Scenes"].append(page)
        self.assertIn("partner_state_ending_coverage", self.codes(story, registry))
        page["Nodes"][0]["Paragraphs"] = copy.deepcopy(story["Scenes"][2]["Nodes"][0]["Paragraphs"])
        self.assertEqual(self.codes(story, registry), [])

    def test_derived_guard_and_historical_latch_distinction(self):
        story, registry = fixture()
        story["Derived"] = {"partner.lost": [["partner.dead"]]}
        story["Scenes"][1].update(Requires=["partner.lost"])
        story["Scenes"][1]["Nodes"][0]["Text"] = "Partner is dead."
        self.assertNotIn("ungated_commitment_absence", self.codes(story, registry))
        # An unlockable flag can change; a latch remembers its old value, not
        # a current death. This cannot discharge a current death claim.
        story.pop("Etudes")
        story["UnlockableFlags"] = {"partner.dead": {"Guid": "a" * 32, "Min": 1}}
        story["Latches"] = {"partner.history_lost": ["partner.dead"]}
        story["Scenes"][1]["Requires"] = ["partner.history_lost"]
        self.assertIn("ungated_commitment_absence", self.codes(story, registry))

    def test_report_exit_zero_strict_optional(self):
        story, registry = fixture()
        story["Scenes"] = story["Scenes"][1:2]
        with tempfile.TemporaryDirectory(prefix="rrt-partner-test-") as tmp:
            paths = [Path(tmp) / filename for filename in ("story.json", "registry.json")]
            for path, data in zip(paths, (story, registry)):
                path.write_text(json.dumps(data), encoding="utf-8")
            argv = ["--story", str(paths[0]), "--registry", str(paths[1])]
            self.assertEqual(lint.main(argv), 0)
            self.assertEqual(lint.main([*argv, "--strict"]), 1)

    def test_roster_complete(self):
        registry = json.loads(lint.REGISTRY.read_text(encoding="utf-8"))
        self.assertEqual(len(registry["roster"]), 41)
        self.assertEqual(len({e["woman"] for e in registry["roster"]}), 41)
        self.assertFalse({"Ember", "Aivu"} & {e["woman"] for e in registry["roster"]})

    def test_canon_citation_verifies_guid_key_and_exact_line(self):
        citation = dict(path="World/Dialogs/partner.jbp", guid="a" * 32, key="key", text="My wife.")
        registry = {"roster": [{"partners": [{"evidence": [citation]}]}]}
        with tempfile.TemporaryDirectory(prefix="rrt-partner-evidence-") as tmp:
            archive, localization = Path(tmp) / "blueprints.zip", Path(tmp) / "enGB.json"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr(citation["path"], json.dumps({"AssetId": "a" * 32, "Data": {"Text": {"m_Key": "key"}}}))
            localization.write_text(json.dumps({"strings": {"key": "My wife."}}), encoding="utf-8")
            self.assertEqual(lint.verify_evidence(registry, archive, localization)["errors"], [])
            citation["guid"] = "b" * 32
            self.assertTrue(lint.verify_evidence(registry, archive, localization)["errors"])
            citation.update(guid="a" * 32, key="other", text="My wife.")
            localization.write_text(json.dumps({"strings": {"key": "My wife.", "other": "My wife."}}), encoding="utf-8")
            self.assertIn("localized key absent", " ".join(lint.verify_evidence(registry, archive, localization)["errors"]))
            citation.update(key="key", text="Altered line.")
            self.assertIn("localized line mismatch", " ".join(lint.verify_evidence(registry, archive, localization)["errors"]))


if __name__ == "__main__":
    unittest.main()
