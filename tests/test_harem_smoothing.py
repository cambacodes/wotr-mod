"""Harem smoothing lint (doc 16 section 8c.3): the shipped data passes, the form audit arithmetic is pinned, and defects are caught."""
import contextlib
import copy
import io
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import harem_smoothing_lint as lint  # noqa: E402

DATA = lint.load_json(lint.DEFAULT_DATA)
PARTNERS, PAIR_WOMEN, FRICTIONS = lint.household_maps()
PACKETS = lint.load_json(lint.SCHEDULE)["packets"]


def errors(data, story=None):
    return lint.lint(data, story, None, PARTNERS, PAIR_WOMEN)


def woman(data, wid):
    return next(w for w in data["women"] if w["id"] == wid)


class ShippedData(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(errors(DATA), [])

    def test_roster_and_tags(self):
        self.assertEqual(len(DATA["women"]), 41)
        counts = {t: len(ids) for t, ids in DATA["doc16_tags"].items()}
        self.assertEqual(counts, {"possessive": 5, "competitive": 14, "communal": 13, "indifferent": 9})

    def test_doc16_parser(self):
        text = "".join("| **%s** | %s | x | y |\n" % (t, ", ".join(n.capitalize() for n in ids))
                        for t, ids in DATA["doc16_tags"].items())
        self.assertEqual(lint.parse_doc16_tags(text), DATA["doc16_tags"])

    def test_form_audit_pinned(self):
        _, t = lint.form_audit(DATA, FRICTIONS, PACKETS)
        exp = DATA["expected_audit"]
        for k in ("frictions", "smoothing", "combined", "with_reservations", "packets", "charged", "capacity",
                  "over_cap_forms"):
            self.assertEqual(t[k], exp[k], k)

    def test_strict_form_audit_passes(self):
        """Rulings D1/D2 (W0b): at least 20 forms, no form above the cap of two, nothing outside the vocabulary."""
        rows, t = lint.form_audit(DATA, FRICTIONS, PACKETS)
        self.assertGreaterEqual(len(DATA["forms"]), 20)
        self.assertEqual(len(DATA["forms"]), len(set(DATA["forms"])))
        self.assertEqual(DATA["form_cap"], 2)
        self.assertEqual(t["unapproved_forms"], [])
        self.assertEqual(max(r[5] for r in rows), 2)
        self.assertEqual(t["over_cap_forms"], 0)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(lint.main(["--strict-forms"]), 0)

    def test_allocation_pinned(self):
        """W0b reallocation: forms of the reassigned repairs, frictions and packet K1 (motives and actions unchanged)."""
        got = {w["id"] + "/" + (r.get("variant") or "-"): r["form"] for w, r in lint.repairs(DATA)}
        for k, v in {"vellexia/-": "a private rehearsal", "aranka/-": "a private rehearsal", "konomi/-": "a precedence drill",
                     "chivarro/-": "a procurement", "dorgelinda/-": "a procurement", "wenduag/-": "a wrestling escape",
                     "mielarah/-": "a route-plotting exercise", "shamira/-": "a negotiation", "horzalah/-": "a trap reversal",
                     "irabeth/-": "a watch handover", "gesmerha/-": "a craft lesson", "arueshalae/redeemed": "a menu composition",
                     "arueshalae/corrupted": "a trade", "yaniel/-": "a corrective errand",
                     "herrax/-": "a performance at the Fool King's court", "eliandra/-": "an observance placement",
                     "chadali/-": "a drawing of lots"}.items():
            self.assertEqual(got[k], v, k)
        fr = {(f["a"], f["b"]): f["form"] for f in FRICTIONS}
        self.assertEqual(fr[("seelah", "camellia")], "a vigil for the dead")
        self.assertEqual(fr[("arueshalae", "nocticula")], "a renunciation before witnesses")
        self.assertEqual(fr[("seelah", "areelu")], "a restitution inspection")
        self.assertEqual([p["form"] for p in PACKETS], ["a restitution inspection", "an evidence hearing", "a negotiation"])

    def test_terms_provenance_refreshed(self):
        """Ruling D5: 06 section 1a records terms for every route, so every row is R with a 06 <slug>.terms source."""
        for w in DATA["women"]:
            slug = "minagho_chivarro" if w["id"] in ("minagho", "chivarro") else w["id"]
            self.assertEqual((w["provenance"], w["terms_source"]), ("R", "06 %s.terms" % slug), w["id"])

    def test_unapproved_packet_form_is_flagged(self):
        _, t = lint.form_audit(DATA, FRICTIONS, [{"form": "a picnic"}])
        self.assertEqual(t["unapproved_forms"], ["a picnic"])

    def test_reserved_names_unused(self):
        self.assertEqual(errors(DATA, '{"Requires": ["seelah.harem.eligible"]}'), [])
        self.assertTrue(errors(DATA, '{"Set": ["seelah.harem.mend.camellia.1"]}'))
        self.assertTrue(errors(DATA, '{"Id": "household.smooth.kiana.1.a"}'))


class Defects(unittest.TestCase):
    def setUp(self):
        self.d = copy.deepcopy(DATA)

    def test_indifferent_with_repair(self):
        woman(self.d, "nenio")["repairs"] = copy.deepcopy(woman(self.d, "kiana")["repairs"])
        self.assertTrue(any("indifferent" in e for e in errors(self.d)))

    def test_susceptible_without_repair(self):
        woman(self.d, "kiana")["repairs"] = []
        self.assertTrue(any("needs at least one repair" in e for e in errors(self.d)))

    def test_unknown_form(self):
        woman(self.d, "kiana")["repairs"][0]["form"] = "a picnic"
        self.assertTrue(any("not in 08" in e for e in errors(self.d)))

    def test_nearest_cross_tag(self):
        woman(self.d, "kiana")["repairs"][0]["nearest"] = ["seelah", "kaylessa", "nenio"]
        self.assertTrue(any("different default tag" in e for e in errors(self.d)))

    def test_mechanism_cap(self):
        for wid in ("seelah", "kiana", "kaylessa"):
            woman(self.d, wid)["repairs"][0]["mechanism"] = "same"
        self.assertTrue(any("mechanism same" in e for e in errors(self.d)))

    def test_arueshalae_absence_fallback(self):
        woman(self.d, "arueshalae")["repairs"][1]["requires"] = []
        self.assertTrue(any("arueshalae/corrupted" in e for e in errors(self.d)))

    def test_ember_excluded(self):
        self.d["women"].append(dict(woman(self.d, "kiana"), id="ember", rel="ember"))
        self.assertTrue(any("friendship-only" in e for e in errors(self.d)))

    def test_seat_override_drift(self):
        self.d["seat_overrides"]["tirabade"]["mode"] = "own_household"
        self.assertTrue(any("seat overrides drift" in e for e in errors(self.d)))

    def test_tag_drift(self):
        woman(self.d, "seelah")["default"] = "communal"
        self.assertTrue(any("doc 16 says" in e for e in errors(self.d)))

    def test_bad_engb_key(self):
        woman(self.d, "seelah")["canon"].append("not-a-key")
        self.assertTrue(any("malformed" in e for e in errors(self.d)))

    def test_over_cap_detected(self):
        woman(self.d, "kiana")["repairs"][0]["form"] = "a wager"
        _, t = lint.form_audit(self.d, FRICTIONS, PACKETS)
        self.assertEqual(t["over_cap_forms"], 1)

    def test_variants_charge_a_form_once(self):
        """D2: Arueshalae's mutually exclusive variants on one form charge it once."""
        a = woman(self.d, "arueshalae")["repairs"]
        _, before = lint.form_audit(self.d, FRICTIONS)
        a[0]["form"] = a[1]["form"]
        _, t = lint.form_audit(self.d, FRICTIONS)
        self.assertEqual(t["smoothing"], before["smoothing"] - 1)

    def test_retry_not_charged(self):
        r = woman(self.d, "kiana")["repairs"][0]
        woman(self.d, "kiana")["repairs"].append(dict(r, mechanism="kiana_retry", action=r["action"] + " Again.", retry=True))
        _, t = lint.form_audit(self.d, FRICTIONS)
        self.assertEqual(t["smoothing"], DATA["expected_audit"]["smoothing"])

    def test_retired_repair_not_counted(self):
        r = woman(self.d, "seelah")["repairs"][0]
        woman(self.d, "seelah")["repairs"].append(dict(r, retired=True))
        self.assertEqual(errors(self.d), [])
        _, t = lint.form_audit(self.d, FRICTIONS)
        self.assertEqual(t["smoothing"], DATA["expected_audit"]["smoothing"])


if __name__ == "__main__":
    unittest.main()
