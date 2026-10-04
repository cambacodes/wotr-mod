"""eng7-l09: order, nesting, exact inline spans, drafts and action controls."""
import unittest
from tools import text_structure_lint as lint


class TextStructureTests(unittest.TestCase):
    def test_all_mapped_shipped_spans(self):
        import expansion
        import json
        from pathlib import Path
        story = expansion.make_expansion()
        rows = lint.check(story)
        findings = json.loads((Path(__file__).resolve().parents[1] / "tools/engine_backlog.json").read_text())["findings"]
        for finding in findings:
            if finding.get("item_id") != "E-Q7-20" or finding["snapshot_evidence"].get("draft_finding"):
                continue
            location = finding["problem"].split()[1] if finding["problem"].startswith("Node ") else "blood"
            candidates = [r for r in rows["hard"] + rows["review"] if r["scene"] == finding["scene"] and r["location"] == location]
            self.assertTrue(candidates, finding["id"])
            if finding["route"] == "terendelev":
                self.assertTrue(any(r["code"] == "orphan-narration-closer" for r in candidates), finding["id"])
    def test_order_and_nesting(self):
        for text in ('{/n}before{n}after', '{n}one{n}two{/n}{/n}', '{n}open', 'orphan{/n}'):
            self.assertTrue(lint.spans(text)[0], text)
        self.assertEqual([x[0] for x in lint.spans('{/n}before{n}after')[0]],
                         ["orphan-narration-closer", "unclosed-narration"])
        text = 'Speech. {n}Unclosed narration.'
        code, start, end = lint.spans(text)[0][0]
        self.assertEqual((code, text[start:end]), ("unclosed-narration", "{n}"))

    def test_inline_narration_and_offsets(self):
        text = '"Stay." She shuts the door. {n}Rain falls.{/n} "Yes." Her hand shakes.'
        hard, review = lint.spans(text, "X")
        self.assertFalse(hard)
        self.assertEqual([text[a:b] for _, a, b in review], ['She shuts the door.', 'Her hand shakes.'])

    def test_owlcat_controls(self):
        for text, kind in (('"Stay," {n}she says.{/n} "Here."', "node"),
                           ('{n}Rain falls.{/n}', "node"), ('"{mf|Sir|Madam}, stay."', "node"),
                           ('[Take her hand.]', "choice"), ('Continue', "choice"), ('"Come with me."', "choice")):
            self.assertEqual(lint.spans(text, "X", kind), ([], []), text)

    def test_paragraphs_choices_and_draft_errors(self):
        story = {"Scenes": [{"Id": "draft", "Nodes": [{"Id": "start", "Text": '"Hi." She smiles.',
                 "Paragraphs": [{"Text": "{/n}"}], "Choices": [{"Text": "{n}broken"}]}]}]}
        result = lint.check(story, draft=True)
        self.assertEqual(len(result["hard"]), 2)
        self.assertTrue(all(r["draft"] for r in result["hard"]))
