"""Irabeth's cuts, receipt collection and refusal histories."""
import copy
import json
from pathlib import Path
import unittest
from itertools import zip_longest
from tests.structure import without_prose
import story
from storylines import irabeth_independent, irabeth_partner_stance
from storylines import irabeth_return_invitation, irabeth_round2, irabeth_trickster
from tests.test_irabeth_partner_stance import walk
from tools import savecompat

class IrabethRound2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scenes = copy.deepcopy(story.scenes + irabeth_independent.SCENES +
                               irabeth_trickster.SCENES + irabeth_return_invitation.SCENES)
        irabeth_partner_stance.integrate({"Scenes": scenes})
        cls.before = copy.deepcopy(scenes)
        cls.payload = {"Scenes": scenes}
        irabeth_round2.integrate(cls.payload)
        irabeth_partner_stance.cover_endings(scenes)
        cls.books = {b["Id"]: b for b in scenes}

    def test_all_saved_indices_destinations_and_exits_survive(self):
        self.assertEqual([], savecompat.check(self.payload, savecompat.inventory({'Scenes': self.before})))
        for book in self.before:
            current = self.books[book['Id']]
            self.assertTrue(all((new is not None and old['Id'] == new['Id'] for old, new in zip_longest(book['Nodes'], current['Nodes']) if old is not None)))
            for old, new in zip(book['Nodes'], current['Nodes']):
                self.assertTrue(all(new is not None for old, new in zip_longest(old['Choices'], new['Choices']) if old is not None))
                for left, right in zip(old['Choices'], new['Choices']):
                    self.assertEqual(left.get('Next'), right.get('Next'))
                if book['Owner'].endswith('Epilogue'):
                    self.assertEqual(without_prose(old['Choices']), without_prose(new['Choices']))

    def test_every_brief_has_one_reachable_cut(self):
        briefs = list(irabeth_round2.SLOTS.glob('*.json'))
        self.assertEqual({json.loads(p.read_text(encoding='utf-8'))['slot_id'] for p in briefs}, {
            'i_crossing.explicit.1',
            'irabeth.a_road_she_would_choose.explicit.1',
            'irabeth.the_hour_before_battle.explicit.1',
            'irabeth.trickster.commit.explicit.1',
            'irabeth.trickster.commit.explicit.2',
            'irabeth.trickster.nevi_reply.explicit.1',
            'irabeth.trickster.nevi_reply.explicit.2',
            'irabeth.trickster.second_ask.explicit.1',
            'irabeth.trickster.second_ask.explicit.2',
            'irabeth.without_an_account.explicit.1',
        })
        for path in briefs:
            brief = json.loads(path.read_text(encoding='utf-8'))
            found = [(book, page) for book in self.books.values() for page in book['Nodes'] if page['Id'] == brief['slot_id']]
            (book, slot), = found
            self.assertEqual(slot['Id'], brief['slot_id'])
            self.assertTrue(any((a.get('Next') == slot['Id'] for page in book['Nodes'] for a in page['Choices'])))
            self.assertFalse(slot.get('Paragraphs'))

    def test_signature_and_muster_belong_only_to_night_branches(self):
        for sid, nid in (('irabeth.without_an_account', 'private'), ('irabeth.the_hour_before_battle', 'night')):
            book = self.books[sid]
            night = next((p for p in book['Nodes'] if p['Id'] == nid))
            self.assertTrue(any((a.get('Next', '').endswith('.explicit.1') for a in night['Choices'])))
            for page in book['Nodes']:
                if page['Id'] in ('rest', 'held', 'space', 'hold', 'talk'):
                    self.assertFalse(any(('.explicit.' in (a.get('Next') or '') for a in page['Choices'])))
        ordinary = next((p for p in self.books['irabeth.without_an_account']['Nodes'] if p['Id'].endswith('.after_explicit.1')))
        battle = next((p for p in self.books['irabeth.the_hour_before_battle']['Nodes'] if p['Id'].endswith('.after_explicit.1')))

    def test_partner_discovery_never_grants_free_forgiveness(self):
        for sid in ("irabeth.the_hour_before_battle", "irabeth.trickster.back_on_duty"):
            for native in ((), ("anevia_dead",), ("anevia_gone",),
                           ("anevia_gone", "anevia.trickster.returned")):
                endings = walk(self.books[sid], (irabeth_partner_stance.SECRET, *native))
                self.assertTrue(endings)
                self.assertTrue(all("irabeth.closed" in flags for flags in endings))

    def test_request_waits_for_irabeths_answer(self):
        book = self.books["irabeth.trickster.commit"]
        requests = next(p for p in book["Nodes"] if p["Id"] == "answer")
        for answer in requests["Choices"]:
            if answer.get("Next") == "reckon" and not set(answer["Requires"]) & set(answer["Forbids"]):
                self.assertNotIn("irabeth.committed", answer["Set"])
        own = next(p for p in book["Nodes"] if p["Id"] == "reckon")
        self.assertTrue(all("irabeth.committed" in a["Set"] for a in own["Choices"]))

    def test_departure_requires_deed_and_keeps_office_unavailable(self):
        pack = Path(__file__).resolve().parents[1] / "tools/route_packs/irabeth-departure-continuation.json"
        books = {b["Id"]: b for b in json.loads(pack.read_text(encoding="utf-8"))["Scenes"]}
        offer = books["irabeth.return_own_invitation"]
        self.assertIn("irabeth.return_advice_used", offer["Requires"])
        visit = books["irabeth.return_private_visit"]
        self.assertIn("irabeth.return_personal_invitation", visit["Requires"])
        endings = walk(visit)
        self.assertTrue(any("irabeth.return_personal_yes" in f for f in endings))
        self.assertTrue(any("irabeth.return_personal_friend" in f for f in endings))
        self.assertTrue(any("irabeth.return_personal_declined" in f for f in endings))
        for flags in endings:
            self.assertFalse(set(flags) & {"irabeth.committed", "irabeth.lover", "irabeth.trickster.returned"})
        for book in books.values():
            for page in book["Nodes"]:
                self.assertTrue(all(not a.get("Crusade") for a in page["Choices"]))
        self.assertTrue(set(books).isdisjoint(b["Id"] for b in irabeth_return_invitation.SCENES))
if __name__ == '__main__':
    unittest.main()
