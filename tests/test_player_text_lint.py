"""eng7-l09: positive reports and narrow negative controls."""
import json
from pathlib import Path
import unittest
from tools import player_text_lint as lint


def payload(text, speaker="X", **extra):
    return {"Scenes": [{"Id": "fixture", "Nodes": [{"Id": "start", "Speaker": speaker, "Text": text, **extra}]}]}


class PlayerTextTests(unittest.TestCase):
    def test_explicit_speech_and_review_span(self):
        rows = lint.check(payload('{n}"Stay," you tell her.{/n}'))["review"]
        self.assertTrue(any(r["code"] == "embedded-commander-speech" and r["start"] >= 0 for r in rows))

    def test_npc_questions_and_demands_are_not_commander_attributions(self):
        for text in ('"What did you say?"', '"So before you say anything soft: she comes first."',
                     '"Tomorrow at muster you say it again."', '"What will you tell him?"',
                     '"First paragraph.\n"Then you say it again."'):
            self.assertFalse(any(r['code'] == 'embedded-commander-speech'
                                 for r in lint.check(payload(text))['review']), text)
        for text in ('{n}"Stay," you tell her.{/n}', '{n}You say, "Stay."{/n}',
                     '"Stay," you tell her.', '“Stay,” the Commander says.',
                     '"Well?" {n}"Stay," you reply.{/n}'):
            self.assertTrue(any(r['code'] == 'embedded-commander-speech'
                                for r in lint.check(payload(text))['review']), text)

    def test_controls_and_exact_exception(self):
        for text in ('"Have you asked her?"', '"A native-born soldier wrote a draft order."',
                     '{n}He hands the captain her sword.{/n}', '{n}Commander, {mf|he|she} waits.{/n}'):
            self.assertFalse(lint.check(payload(text))["review"], text)
        story = payload('"The observer waits."')
        row = lint.check(story)["review"][0]
        exception = {**row, "reason": "An in-world lookout, reviewed for this exact span."}
        self.assertFalse(lint.check(story, {"exceptions": [exception]})["review"])
        exception["location"] = "other"
        self.assertTrue(lint.check(story, {"exceptions": [exception]})["review"])
        rows = lint.check(payload('"{mf|Sir|Madam}. The Commander lays his sword down."'))["review"]
        self.assertTrue(any(r["code"] == "commander-gender" for r in rows))

    def test_all_display_surfaces_and_therapy_counts(self):
        story = payload('"Yes."', Paragraphs=[{"Text": "registered observer"}], Choices=[{"Text": "native romance"}])
        story["Books"] = {"letter": {"Text": "handler consent"}}
        result = lint.check(story)
        self.assertEqual({r["location"] for r in result["review"]}, {"start/paragraph/0", "start/choice/0", "Text"})
        self.assertEqual(sum(result["therapy_counts"].values()), 1)

    def test_all_mapped_scripted_replies_are_reported(self):
        import expansion
        story = expansion.make_expansion()
        rows = lint.check(story)["review"]
        findings = json.loads((Path(__file__).resolve().parents[1] / "tools/engine_backlog.json").read_text(encoding="utf-8"))["findings"]
        for finding in findings:
            if finding.get("item_id") == "E-Q7-21" and finding["route"] == "arsinoe":
                node = finding["problem"].split()[1]
                rewritten = {("arsinoe_price_of_an_evening", "charge"),
                             ("arsinoe_two_doors", "comparison"),
                             ("arsinoe_a_stone_in_hand", "after_possibility")}
                reported = any(r["scene"] == finding["scene"] and r["location"] == node for r in rows)
                if (finding["scene"], node) in rewritten:
                    self.assertFalse(reported, finding["id"])
                else:
                    self.assertTrue(reported, finding["id"])
