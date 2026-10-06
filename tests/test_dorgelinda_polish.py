"""Reviewed Dorgelinda polish: retained terms and exhaustive local dispatches."""
import copy
import itertools
import unittest

from storylines import dorgelinda_ledger as ledger
from storylines import dorgelinda_trickster as trickster


L = "dorgelinda.ledger."
P = "dorgelinda.trickster."
C, M, X, N, U = (L + key for key in (
    "quarrel_cold", "quarrel_mended", "quarrel_unmended", "narrowed", "unblessed"))
B = P + "cost.boots_paid"


def visible(item, flags):
    return (all(f in flags for f in item.get("Requires", ()))
            and not any(f in flags for f in item.get("Forbids", ()))
            and all(any(f in flags for f in group)
                    for group in item.get("AnyGroups", ())))


class DorgelindaPolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {"Scenes": copy.deepcopy(trickster.SCENES + ledger.SCENES)}
        ledger.integrate(payload)
        cls.scenes = {scene["Id"]: scene for scene in payload["Scenes"]}

    def node(self, scene, node):
        return next(n for n in self.scenes[scene]["Nodes"] if n["Id"] == node)

    def histories(self, keys):
        for bits in itertools.product((False, True), repeat=len(keys)):
            yield {key for key, bit in zip(keys, bits) if bit}

    def choices(self, scene, node, flags):
        return [c for c in self.node(scene, node)["Choices"] if visible(c, flags)]

    def cold(self, flags):
        return X in flags or (C in flags and M not in flags)

    def rendered(self, scene, flags):
        page = self.node(scene, "page")
        return {i for i, p in enumerate(page.get("Paragraphs", ())) if visible(p, flags)}

    def test_march_covers_all_64_histories_without_expanding_private_terms(self):
        scene = L + "carried_forward"
        for flags in self.histories((B, C, M, X, N, U)):
            with self.subTest(flags=sorted(flags)):
                answers = self.choices(scene, "boots", flags)
                self.assertEqual(len(answers), 1)
                target = answers[0]["Next"]
                if B in flags:
                    self.assertEqual(target, "paid")
                    answers = self.choices(scene, "paid", flags)
                    self.assertEqual(len(answers), 1)
                    target = answers[0]["Next"]
                expected = ("choose_cold" if self.cold(flags) else
                            "choose_reserved" if N in flags else
                            "choose_private" if U in flags else "choose")
                self.assertEqual(target, expected)
                last = self.choices(scene, target, flags)
                self.assertEqual(len(last), 3)
                self.assertEqual([c["Next"] for c in last][::2], ["receipt", "salute"])
                kiss = self.node(scene, last[1]["Next"])
                self.assertEqual(kiss["Choices"][0]["Next"], "end")
                self.assertFalse(kiss["Choices"][0]["Set"])
                self.assertEqual(kiss["Id"], "kiss_cold" if self.cold(flags) else
                                 "kiss_reserved" if N in flags else "kiss_reserved_private" if U in flags else "kiss")

    def test_council_and_postwar_dispatch_keep_cold_priority(self):
        for flags in self.histories((C, M, X, N, U)):
            with self.subTest(flags=sorted(flags)):
                council = self.choices(L + "after_the_council", "start", flags)
                self.assertEqual(len(council), 1 if self.cold(flags) else 2)
                self.assertEqual({c["Next"] for c in council},
                                 {"council_cold"} if self.cold(flags) else {"think", "like"})
                after = self.choices(L + "after_the_war", "tin", flags)
                self.assertEqual(len(after), 1)
                self.assertEqual(after[0]["Next"], "after_cold" if self.cold(flags) else
                                 "after_narrowed" if N in flags else "after")
        for scene, node in (("after_the_council", "council_cold"),
                            ("after_the_war", "after_cold")):
            answer = self.node(L + scene, node)["Choices"][0]
            self.assertIsNone(answer["Next"])
            self.assertFalse(answer["Set"])

    def test_both_ending_families_respect_account_and_relationship(self):
        for flags in self.histories((C, M, X, N, U)):
            for told in (False, True):
                history = flags | {L + "signed_after"}
                if told:
                    history.add(P + "cost.told_all")
                with self.subTest(flags=sorted(history)):
                    committed = self.rendered(P + "epilogue.committed", history)
                    after = self.rendered(P + "epilogue.after_the_war", history)
                    self.assertEqual(8 in committed, told)
                    self.assertEqual(9 in committed, not told)
                    warm = not self.cold(flags) and N not in flags and U not in flags
                    self.assertEqual(len(committed & {10, 11}), int(warm))
                    self.assertEqual(len(after & {2, 11}), int(warm))
                    self.assertEqual(len(after & {7, 12}), int(self.cold(flags)))
                    self.assertEqual(len(after & {5, 9}), int(N in flags and not self.cold(flags)))
                    self.assertEqual(len(after & {6, 10}),
                                     int(U in flags and N not in flags and not self.cold(flags)))
        page = P + "epilogue.committed"
        for disposition, expected in ((ledger.TRUE_BOOKS, 4), (ledger.CLEAN_COPY, 5), (ledger.HER_NAME, 6)):
            text = self.rendered(page, {disposition})
            self.assertIn(expected, text)

    def test_order_has_a_private_rebuke_and_other_rations_keep_thanks(self):
        scene = L + "half_rations"
        for flags, target in ((set(), "last"), ({ledger.ORDERED}, "after_ordered")):
            answers = self.choices(scene, "after", flags)
            self.assertEqual(len(answers), 1)
            self.assertEqual(answers[0]["Next"], target)
            self.assertIsNone(self.node(scene, target)["Choices"][0]["Next"])

    def test_new_forgery_requires_current_path_but_issued_document_is_history(self):
        scene = L + "old_debts"
        for flags, count in (({"trickster.now"}, 3), ({"trickster.ever", "trickster.failed"}, 2),
                             ({"trickster.ever", "legend"}, 2), ({"trickster.ever", "dragon"}, 2)):
            answers = self.choices(scene, "stuck", flags)
            self.assertEqual(len(answers), count)
            self.assertEqual(any(c["Next"] == "forge" for c in answers), count == 3)
        self.assertNotIn("trickster.now", self.scenes[scene]["Requires"])
        self.assertIn("forged", {c["Next"] for c in self.choices(
            L + "three_hundred_helmets", "start", {ledger.FORGED, "trickster.failed"})})

    def test_professional_fallback_and_treasury_payment_make_no_extra_promise(self):
        fallback = self.scenes[P + "epilogue.commit"]
        self.assertIn("dorgelinda.committed", fallback["Forbids"])
        choice = self.node(L + "the_kings_bill", "bill")["Choices"][0]
        self.assertEqual(choice["Crusade"], {"Resource": "Finances", "Amount": -200})
        self.assertEqual(choice["Next"], "mine")


if __name__ == "__main__":
    unittest.main()
