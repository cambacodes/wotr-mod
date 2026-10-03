"""Paragraph validation parity with Rules.Validate in src/Story.cs."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import rrt_verify as rv


def story(owner="Memory", speaker="Narrator", text="Base text.", paragraphs=None):
    return {
        "Relationships": {"her": dict(StartedFlag="her.started", ClosedFlag="her.closed",
                                       CommittedFlag="her.committed")},
        "Scenes": [dict(Id="her.scene", Owner=owner, Relationship="her", MinChapter=3, MaxChapter=5,
                        AnswerLists=["0123456789abcdef0123456789abcdef"], Requires=["her.committed"],
                        Nodes=[dict(Id="start", Speaker=speaker, Text=text, Paragraphs=paragraphs,
                                    Choices=[dict(Text="Continue")])])],
    }


class ParagraphValidationTests(unittest.TestCase):
    def test_paragraphs_on_narrator_speaker_and_epilogue_nodes(self):
        for owner, speaker in (("Memory", "Narrator"), ("Her", "Her"), ("HerEpilogue", "Narrator")):
            with self.subTest(owner=owner, speaker=speaker):
                self.assertEqual(rv.validate(rv.Model(story(owner, speaker, paragraphs=[
                    dict(Text="Optional text.", Requires=["her.started"])]))), [])

    def test_textless_node_needs_a_guaranteed_paragraph(self):
        guaranteed = dict(Text="Always shown.", Requires=["her.committed"],
                          AnyGroups=[["her.started", "her.committed"]])
        self.assertEqual(rv.validate(rv.Model(story(text=" ", paragraphs=[guaranteed]))), [])
        for changes in (dict(Requires=["her.started"]), dict(Forbids=["her.closed"]),
                        dict(AnyGroups=[["her.started"]])):
            with self.subTest(changes=changes):
                paragraph = dict(guaranteed, **changes)
                errors = rv.validate(rv.Model(story(text="", paragraphs=[paragraph])))
                self.assertTrue(any(e.startswith("Invalid paragraphs") for e in errors), errors)

    def test_malformed_paragraphs_are_rejected(self):
        invalid = [None, dict(Text=" "), dict(Text="Text.", Requires=None),
                   dict(Text="Text.", Forbids=None), dict(Text="Text.", AnyGroups=None),
                   dict(Text="Text.", AnyGroups=[None]), dict(Text="Text.", AnyGroups=[[]])]
        for paragraph in invalid:
            with self.subTest(paragraph=paragraph):
                errors = rv.validate(rv.Model(story(paragraphs=[paragraph])))
                self.assertTrue(any(e.startswith("Invalid paragraphs") for e in errors), errors)
        errors = rv.validate(rv.Model(story(paragraphs=None)))
        self.assertIn("Paragraphs cannot be null: her.scene/start", errors)

    def test_runtime_death_evidence_is_known_and_cannot_be_authored(self):
        payload = story(paragraphs=[])
        payload["Derived"] = {"her.unreturned": [["konomi.death_unreturned"]]}
        payload["DerivedForbids"] = {"her.unreturned": ["konomi.death_restored"]}
        self.assertEqual(rv.validate(rv.Model(payload)), [])
        for flag in ("konomi.death_unreturned", "konomi.death_restored"):
            with self.subTest(flag=flag):
                payload["Scenes"][0]["Nodes"][0]["Choices"][0]["Set"] = [flag]
                self.assertIn("Authored contact evidence: her.scene", rv.validate(rv.Model(payload)))


if __name__ == "__main__":
    unittest.main()
