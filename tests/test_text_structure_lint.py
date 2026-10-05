"""eng7-l09: order, nesting, exact inline spans, drafts and action controls."""
import unittest
import json
from pathlib import Path
from tools import text_structure_lint as lint


class TextStructureTests(unittest.TestCase):
    def test_all_mapped_shipped_spans(self):
        import expansion
        story = expansion.make_expansion()
        rows = lint.check(story)
        self.assertFalse(rows["hard"], rows["hard"])
        surfaces = {(sid, location): text for sid, location, text, _, _ in lint.surfaces(story)}
        findings = json.loads((Path(__file__).resolve().parents[1] / "tools/engine_backlog.json").read_text(encoding="utf-8"))["findings"]
        for finding in findings:
            if finding.get("item_id") != "E-Q7-20" or finding["snapshot_evidence"].get("draft_finding"):
                continue
            location = finding["problem"].split()[1] if finding["problem"].startswith("Node ") else "blood"
            key = (finding["scene"], location)
            self.assertIn(key, surfaces, finding["id"])
            text = surfaces[key]
            self.assertFalse(lint.spans(text)[0], finding["id"])
            if finding["route"] == "terendelev":
                # The repaired shipped text must pass; restoring the orphan must fail.
                self.assertTrue(any(r[0] == "orphan-narration-closer"
                                    for r in lint.spans("{/n}" + text)[0]), finding["id"])
        self.assertEqual(rows, {"hard": [], "review": []})
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

    # eng7-f2: exact inline spans must never include intervening speech.
    def test_multiple_spoken_lines_and_continuation_paragraphs(self):
        text = '"Stay." She waits. "Here." She smiles.'
        hard, review = lint.spans(text, "X")
        self.assertFalse(hard)
        self.assertEqual([text[a:b] for _, a, b in review], ['She waits.', 'She smiles.'])
        self.assertEqual(lint.spans('"First paragraph.\n"Second paragraph."', "X"), ([], []))

    def test_ui_and_npc_surfaces_still_validate_tags(self):
        self.assertEqual(lint.spans('A promise under an open sky', kind='ui'), ([], []))
        self.assertTrue(lint.spans('She smiles.', 'Seelah')[1])
        self.assertTrue(lint.spans('Label{/n}', kind='ui')[0])
        self.assertTrue(lint.spans('Speech{/n}', 'Seelah')[0])
    # end eng7-f2

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
