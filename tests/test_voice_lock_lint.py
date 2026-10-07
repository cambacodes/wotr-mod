"""Text ownership enforcement must ignore all gameplay metadata."""
import copy
import hashlib
import json
import unittest

from tools import voice_lock_lint as lint


def sample():
    return {"Scenes": [{"Id": "route.scene", "Nodes": [
        {"Id": "start", "Text": "Anevia's café — {n}wait.{/n}",
         "Paragraphs": [{"Text": "Conditional prose", "Requires": ["earned"]}],
         "Choices": [{"Text": "Stay", "Next": "end"}, {"Text": "Leave"}]},
        {"Id": "end", "Text": "Goodbye", "Choices": []}]}]}


class VoiceLockTests(unittest.TestCase):
    def test_hash_serialization_is_stable_utf8(self):
        expected = [["Anevia's café — {n}wait.{/n}", ["Conditional prose"], ["Stay", "Leave"]],
                    ["Goodbye", [], []]]
        payload = json.dumps(expected, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), lint.text_sha(sample()["Scenes"][0]))

    def test_boundaries_and_order_are_hashed(self):
        original = sample()["Scenes"][0]
        changed = copy.deepcopy(original)
        changed["Nodes"][0]["Choices"].reverse()
        self.assertNotEqual(lint.text_sha(original), lint.text_sha(changed))
        # Joining raw strings would fail to distinguish these two texts.
        a = {"Nodes": [{"Text": "ab", "Choices": [{"Text": "c"}]}]}
        b = {"Nodes": [{"Text": "a", "Choices": [{"Text": "bc"}]}]}
        self.assertNotEqual(lint.text_sha(a), lint.text_sha(b))


if __name__ == "__main__":
    unittest.main()
