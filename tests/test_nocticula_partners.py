"""Route-local stance, save-shape and current-fate checks, independent of prose."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from storylines import nocticula_partners as partner
from storylines import nocticula_continuation, nocticula_acquired_harbor
from storylines import nocticula_trickster, nocticula_trickster_concession


def allowed(item, flags):
    return (set(item.get("Requires", ())) <= flags
            and not set(item.get("Forbids", ())) & flags
            and all(set(g) & flags for g in item.get("AnyGroups", ())))


def walk(scene, flags, start=None):
    nodes = {n["Id"]: n for n in scene["Nodes"]}
    pending = [(start or scene["Nodes"][0]["Id"], frozenset(flags))]
    visited, results = set(), []
    while pending:
        key, state = pending.pop()
        if (key, state) in visited:
            continue
        visited.add((key, state))
        choices = [c for c in nodes[key]["Choices"] if allowed(c, state)]
        if not choices:
            raise AssertionError((scene["Id"], key, sorted(state)))
        for choice in choices:
            after = state | set(choice["Set"])
            if choice["Next"]:
                pending.append((choice["Next"], frozenset(after)))
            else:
                results.append(after)
    return results


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class NocticulaPartnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = (nocticula_continuation.SCENES + nocticula_acquired_harbor.SCENES
                  + nocticula_trickster.SCENES + nocticula_trickster_concession.SCENES)
        cls.before = deepcopy(source)
        cls.payload = {"Scenes": deepcopy(source)}
        partner.integrate(cls.payload)
        cls.scenes = {s["Id"]: s for s in cls.payload["Scenes"]}

    def test_save_id_order_and_original_answer_slots(self):
        self.assertEqual([new["Id"] for _, new in zip(self.before, self.payload["Scenes"])],
                         [s["Id"] for s in self.before])
        for old in self.before:
            new = self.scenes[old["Id"]]
            self.assertEqual([current["Id"] for _, current in zip(old["Nodes"], new["Nodes"])],
                             [n["Id"] for n in old["Nodes"]])
            for a, b in zip(old["Nodes"], new["Nodes"]):
                for previous, current in zip(a["Choices"], b["Choices"]):
                    # R2 fill nodes splice the heated cut before the old
                    # aftermath. The saved answer index survives; its effects
                    # and old destination remain on the matching continuation.
                    if ".explicit." in (current.get("Next") or "") and previous.get("Next") != current.get("Next"):
                        fill = next(n for n in new["Nodes"] if n["Id"] == current["Next"])
                        if all(".aftermath." in (c.get("Next") or "") for c in fill["Choices"]):
                            fill = next(n for n in new["Nodes"] if n["Id"] == only(fill["Choices"])["Next"])
                        current = next(candidate for legacy, candidate in zip(a["Choices"], fill["Choices"])
                                       if legacy is previous)
                    # N1 splices the marked aftermath before the old morning.
                    if old["Id"] == "noct.her_own_face" and a["Id"] == "night":
                        self.assertEqual(current["Next"], "mark")
                        current = dict(current, Next="morning")
                    if old["Id"] == "noct.second_door" and current.get("Next") == "waking":
                        current = dict(current, Next=None)
                    for key in ("Next", "Set", "Abort", "Check", "NativeNext"):
                        self.assertEqual(previous.get(key), current.get(key), (old["Id"], a["Id"], key))

    def test_current_state_partition_and_no_free_body(self):
        histories = [set(), {partner.KILLED}, {partner.KILLED, partner.RETURNED},
                     {partner.KILLED, partner.RETURNED, partner.BODY},
                     {partner.KILLED, partner.RETURNED, partner.CAPTIVE},
                     {partner.KILLED, partner.RETURNED, partner.CAST},
                     {partner.KILLED, partner.DECLINED},
                     # Paid history survives a completed native etude/path change.
                     {partner.RETURNED, partner.BODY}, {partner.RETURNED},
                     {partner.RETURNED, partner.CAST}, {partner.DECLINED}]
        for flags in histories:
            with self.subTest(flags=flags):
                matches = [name for name, req, bad in partner.STATES
                           if allowed(dict(Requires=req, Forbids=bad), flags)]
                self.assertEqual(only(matches) == "body", partner.BODY in flags)

    def test_every_commit_records_one_stance_and_rejection_closes(self):
        histories = [set(), {partner.KILLED}, {partner.KILLED, partner.RETURNED},
                     {partner.KILLED, partner.RETURNED, partner.BODY},
                     {partner.KILLED, partner.RETURNED, partner.CAPTIVE},
                     {partner.KILLED, partner.RETURNED, partner.CAST}]
        fixtures = [("noct.second_door", "future", "noct.complete", "noct.closed"),
                    ("nocticula.trickster.defeated.chair", "verdict_true", "noct.complete", "noct.closed"),
                    ("noct.acq.an_answer_of_her_own", "risk", "noct.acq.renewed_agreement", "noct.acq.closed")]
        fixtures.extend(("noct.second_door.acquired." + history, "future", "noct.complete", "noct.closed")
                        for history in ("new", "prior", "refused"))
        for sid, node, commit, closed in fixtures:
            for history in histories:
                flags = history | {"noct.future_rivals", "noct.future_power",
                                   "nocticula.trickster.cost.shade_paid"}
                ends = walk(self.scenes[sid], flags, node)
                committed = [x for x in ends if commit in x]
                self.assertTrue(committed, sid)
                for state in committed:
                    self.assertIn(partner.TERMS, state)
                    self.assertEqual(len(state & {partner.P + x for x in ("share", "exclusive", "secret")}), 1)
                    self.assertFalse(closed in state)
                if not partner.KILLED in history or partner.RETURNED in history and not partner.CAST in history:
                    self.assertTrue(any({closed, partner.REFUSED, partner.P + "exclusive"} <= x
                                        and commit not in x for x in ends), sid)
                # No stance answer writes another route's return, body, closure or commitment.
                self.assertTrue(all(not (set(x) - flags) & {partner.RETURNED, partner.BODY} for x in ends))

    def test_secret_discovered_at_existing_receipts_without_erasing_stance(self):
        for state in (set(), {partner.KILLED}, {partner.KILLED, partner.RETURNED},
                      {partner.KILLED, partner.RETURNED, partner.BODY}):
            flags = state | {partner.P + "secret", partner.TERMS}
            for sid, node in (("noct.acq.an_answer_of_her_own", "accept"),
                              ("noct.second_door", "end"),
                              ("nocticula.trickster.defeated.morning", "start")):
                ends = walk(self.scenes[sid], flags, node)
                self.assertTrue(ends)
                self.assertTrue(all({partner.EXPOSED, partner.P + "secret"} <= x for x in ends))

    def test_late_terms_are_optional_and_do_not_grant_return_or_commit(self):
        scene = self.scenes["nocticula.trickster.partner_terms.threshold"]
        self.assertIn("nocticula.trickster.returned", scene["Requires"])
        self.assertIn(partner.TERMS, scene["Forbids"])
        for state in walk(scene, set(scene["Requires"])):
            self.assertNotIn("noct.complete", state)
            self.assertNotIn(partner.RETURNED, state)
        for sid in ("nocticula.trickster.epilogue.commit", "nocticula.trickster.epilogue.declined"):
            self.assertIn(partner.TERMS, self.scenes[sid]["Requires"])

    def test_ending_nodes_read_stances_and_partner_fates(self):
        for scene in self.payload["Scenes"]:
            if scene.get("Relationship") in ("nocticula", "nocticula.acquisition") and scene["Owner"] == "Epilogue":
                for node in scene["Nodes"]:
                    if not any(not c["Next"] for c in node["Choices"]):
                        continue
                    paragraphs = node.get("Paragraphs", [])
                    for stance in ("share", "exclusive", "secret"):
                        self.assertTrue(any(partner.P + stance in p["Requires"] for p in paragraphs), scene["Id"])
                    self.assertTrue(any(partner.KILLED in p["Requires"] for p in paragraphs), scene["Id"])
                    self.assertTrue(any({partner.RETURNED, partner.BODY} <= set(p["Requires"]) for p in paragraphs), scene["Id"])
        self.assertEqual(self.payload["DerivedForbids"]["nocticula.partner_passenger_lost"],
                         ["trickster.commander_back", partner.CAST, partner.DECLINED])

    def test_exposed_living_partner_has_a_separate_current_account(self):
        for dead in (False, True):
            paragraphs = partner.ending_paragraphs(nocticula_dead=dead)
            living = [p for p in paragraphs if set(partner.STATES[0][2]) <= set(p["Forbids"])
                      and partner.P + "secret" not in p["Requires"]]
            self.assertEqual({tuple(p["Requires"]) for p in living},
                             {(), (partner.CHOSEN,), (partner.EXPOSED,)})
            self.assertTrue(allowed(only(p for p in living if allowed(p, {partner.CHOSEN})), {partner.CHOSEN}))
            self.assertTrue(allowed(only(p for p in living if allowed(p, set())), set()))
            self.assertTrue(allowed(only(p for p in living if allowed(p, {partner.EXPOSED})), {partner.EXPOSED}))
            self.assertTrue(any(partner.EXPOSED in p["Requires"] for p in living))

    def test_compiled_terms_never_require_shamiras_physical_availability(self):
        from tests.story_fixture import fresh_story
        payload = fresh_story()
        for scene in payload["Scenes"]:
            if scene["Id"] not in ("noct.second_door", "noct.acq.an_answer_of_her_own",
                                   "nocticula.trickster.defeated.chair", "nocticula.trickster.partner_terms.threshold"):
                continue
            for item in (scene, *(c for n in scene["Nodes"] for c in n["Choices"])):
                self.assertFalse(any(f.startswith("crossroute.shamira.") for f in item["Requires"] + item["Forbids"]), scene["Id"])

    def test_compiled_ending_families_keep_stance_and_current_fate(self):
        from tests.story_fixture import fresh_story
        payload = fresh_story()
        covered = set()
        for scene in payload["Scenes"]:
            if (scene.get("Relationship") not in ("nocticula", "nocticula.acquisition")
                    and scene["Id"] != "nocticula.lastcall.page") or not scene["Owner"].endswith("Epilogue"):
                continue
            for node in scene["Nodes"]:
                if not any(not c["Next"] for c in node["Choices"]):
                    continue
                paragraphs = node.get("Paragraphs", [])
                for stance in ("share", "exclusive", "secret"):
                    self.assertTrue(any(partner.P + stance in p["Requires"] for p in paragraphs), (scene["Id"], node["Id"]))
                if scene["Owner"] != "AeonEpilogue":
                    for flag in (partner.KILLED, partner.RETURNED, partner.BODY, partner.CAST, partner.DECLINED):
                        self.assertTrue(any(flag in p["Requires"] for p in paragraphs), (scene["Id"], node["Id"], flag))
                covered.add(scene["Id"])
        self.assertTrue({"nocticula.lastcall.page", "noct.acq.epilogue.correspondence", "noct.ending_company",
                         "noct.ending_company.acquired.new", "nocticula.trickster.epilogue.commit"} <= covered)


if __name__ == "__main__":
    unittest.main()
