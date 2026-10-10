"""Text ownership enforcement must ignore all gameplay metadata."""
from tools.voice_lock_lint import text_sha as check_text_digest
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



def by_contract(items, contracts):
    """Find a structural outcome; gaps and overlaps violate the contract."""
    matches = [item for item in items
               if any(all(item.get(field) == value for field, value in contract.items())
                      for contract in contracts)]
    try:
        result, = matches
    except ValueError as error:
        raise AssertionError('Expected one matching structural outcome') from error
    return result

class VoiceLockTests(unittest.TestCase):
    def test_hash_serialization_is_stable_utf8(self):
        fixture = {'Nodes': [{'Text': 'café—α', 'Choices': [], 'Paragraphs': []}]}
        payload = json.dumps([['café—α', [], []]], ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        self.assertEqual(hashlib.sha256(payload).hexdigest(), check_text_digest(fixture))

    def test_boundaries_and_order_are_hashed(self):
        original = by_contract(sample()['Scenes'], [{'Id': 'route.scene'}])
        changed = copy.deepcopy(original)
        by_contract(changed['Nodes'], [{'Id': 'start'}])["Choices"].reverse()
        self.assertNotEqual(check_text_digest(original), check_text_digest(changed))
        # Joining raw strings would fail to distinguish these two texts.
        a = {"Nodes": [{"Text": "ab", "Choices": [{"Text": "c"}]}]}
        b = {"Nodes": [{"Text": "a", "Choices": [{"Text": "bc"}]}]}
        self.assertNotEqual(check_text_digest(a), check_text_digest(b))


if __name__ == "__main__":
    unittest.main()
