"""eng7-l09: order, nesting, exact inline spans, drafts and action controls."""
from tests.story_fixture import fresh_story
from tools.text_structure_lint import spans as check_spans
import unittest
import json
from pathlib import Path
from tools import text_structure_lint as lint


class TextStructureTests(unittest.TestCase):
    def test_all_mapped_shipped_spans(self):
        import expansion
        story = fresh_story()
        rows = lint.check(story)
        self.assertFalse(rows["hard"], rows["hard"])
        addresses = {(sid, location) for sid, location, _, _, _ in lint.surfaces(story)}
        surfaces = {(sid, location): rendered for sid, location, rendered, _, _ in lint.surfaces(story)}
        findings = json.loads((Path(__file__).resolve().parents[1] / "tools/engine_backlog.json").read_text(encoding="utf-8"))["findings"]
        for finding in findings:
            if finding.get("item_id") != "E-Q7-20" or finding["snapshot_evidence"].get("draft_finding"):
                continue
            location = finding["problem"].split()[1] if finding["problem"].startswith("Node ") else "blood"
            key = (finding["scene"], location)
            self.assertIn(key, addresses, finding["id"])
            text = surfaces[key]
            self.assertFalse(check_spans(text)[0], finding["id"])
            if finding["route"] == "terendelev":
                # The repaired shipped text must pass; restoring the orphan must fail.
                self.assertTrue(any(r[0] == "orphan-narration-closer"
                                    for r in check_spans("{/n}" + text)[0]), finding["id"])
        self.assertEqual(rows, {"hard": [], "review": []})
    def test_order_and_nesting(self):
        for text in ('{/n}before{n}after', '{n}one{n}two{/n}{/n}', '{n}open', 'orphan{/n}'):
            self.assertTrue(check_spans(text)[0], text)
        self.assertEqual([x[0] for x in check_spans('{/n}before{n}after')[0]],
                         ["orphan-narration-closer", "unclosed-narration"])
        text = 'Speech. {n}Unclosed narration.'
        code, start, end = check_spans(text)[0][0]
        self.assertEqual((code, start, end), ("unclosed-narration", 8, 11))

    def test_inline_narration_and_offsets(self):
        text = '"Stay." She shuts the door. {n}Rain falls.{/n} "Yes." Her hand shakes.'
        hard, review = check_spans(text, "X")
        self.assertFalse(hard)
        self.assertEqual(review, [('unmarked-narration-review', 8, 27), ('unmarked-narration-review', 54, 70)])

    # eng7-f2: exact inline spans must never include intervening speech.
    def test_multiple_spoken_lines_and_continuation_paragraphs(self):
        text = '"Stay." She waits. "Here." She smiles.'
        hard, review = check_spans(text, "X")
        self.assertFalse(hard)
        self.assertEqual(review, [('unmarked-narration-review', 8, 18), ('unmarked-narration-review', 27, 38)])
        self.assertEqual(check_spans('"First paragraph.\n"Second paragraph."', "X"), ([], []))

    def test_ui_and_npc_surfaces_still_validate_tags(self):
        self.assertEqual(check_spans('A promise under an open sky', kind='ui'), ([], []))
        self.assertTrue(check_spans('She smiles.', 'Seelah')[1])
        self.assertTrue(check_spans('Label{/n}', kind='ui')[0])
        self.assertTrue(check_spans('Speech{/n}', 'Seelah')[0])
    # end eng7-f2

    def test_owlcat_controls(self):
        for text, kind in (('"Stay," {n}she says.{/n} "Here."', "node"),
                           ('{n}Rain falls.{/n}', "node"), ('"{mf|Sir|Madam}, stay."', "node"),
                           ('[Take her hand.]', "choice"), ('Continue', "choice"), ('"Come with me."', "choice")):
            self.assertEqual(check_spans(text, "X", kind), ([], []), text)

    def test_paragraphs_choices_and_draft_errors(self):
        story = {"Scenes": [{"Id": "draft", "Nodes": [{"Id": "start", "Text": '"Hi." She smiles.',
                 "Paragraphs": [{"Text": "{/n}"}], "Choices": [{"Text": "{n}broken"}]}]}]}
        result = lint.check(story, draft=True)
        self.assertEqual(len(result["hard"]), 2)
        self.assertTrue(all(r["draft"] for r in result["hard"]))
