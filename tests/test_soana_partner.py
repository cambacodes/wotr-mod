"""Partner stance, earned Corven presence and route-local save references."""
import copy
import itertools
import unittest

from storylines import soana_partner as P, soana_late_campaign as L, soana_trickster as T
from storylines import lastcall_partners
from storylines import soana_round2 as R2


def available(answer, flags):
    return set(answer.get("Requires", ())) <= flags and not set(answer.get("Forbids", ())) & flags


def metadata(value):
    """Compare save/state contracts without making the prose a test oracle."""
    if isinstance(value, dict):
        return {k: metadata(v) for k, v in value.items()
                if k not in {"Text", "Title", "Entry", "Guidance"}}
    if isinstance(value, (list, tuple)):
        return [metadata(v) for v in value]
    return value


def walks(event, flags=(), node=None, path=()):
    nodes = {page["Id"]: page for page in event["Nodes"]}
    node = node or event["Nodes"][0]["Id"]
    assert node not in path, (event["Id"], path, node)
    answers = [a for a in nodes[node]["Choices"] if available(a, set(flags))]
    assert answers, (event["Id"], node, "Page has no selectable answers")
    for answer in answers:
        after = set(flags) | set(answer["Set"])
        if answer.get("Next"):
            yield from walks(event, after, answer["Next"], (*path, node))
        else:
            yield after, (*path, node), answer


def only(items):
    """A continuation is deterministic only when there is exactly one answer."""
    try:
        (item,) = items
    except ValueError as error:
        raise AssertionError("Expected one structural continuation") from error
    return item


class SoanaPartnerTests(unittest.TestCase):
    def test_every_existing_commitment_records_one_stance(self):
        producers = {
            "soana.the_days_she_counted": ("commit",),
            "soana.trickster.returned.terms": ("bind", "bind_clay"),
            "soana.trickster.returned.second_ask": ("price",),
            "soana.trickster.missed.bowl": ("terms",),
            "soana.trickster.missed.second_ask": ("start",),
        }
        scenes = {s["Id"]: s for s in L.SCENES + T.SCENES}
        for sid, nodes in producers.items():
            for node, spent in itertools.product(nodes, (False, True)):
                flags = {R2.MARRIAGE, R2.INVITED}
                if spent:
                    flags.add("soana.trickster.cost.medallion_spent")
                with self.subTest(scene=sid, node=node, spent=spent):
                    results = list(walks(scenes[sid], flags, node))
                    stances = set()
                    for after, _, _ in results:
                        stance = after & {P.SHARE, P.EXCLUSIVE, P.SECRET}
                        self.assertLessEqual(len(stance), 1)
                        if "soana.committed" in after:
                            self.assertEqual(len(stance), 1)
                            self.assertNotIn(P.EXCLUSIVE, after)
                            self.assertIn(P.DECIDED, after)
                            stances.update(stance)
                        if P.EXCLUSIVE in after:
                            self.assertNotIn("soana.committed", after)
                            self.assertTrue(after & {"soana.closed", "soana.late_romance_ended", "soana.trickster.friends"})
                            self.assertNotIn("soana.trickster.cost.knot_bearer", after)
                    self.assertEqual(stances, {P.SHARE, P.SECRET})

    def test_postwar_invitations_also_offer_all_three_stances(self):
        ids = {"soana.trickster.epilogue.commit", "soana.trickster.epilogue.luck_late"}
        for event in (s for s in T.SCENES if s["Id"] in ids):
            with self.subTest(scene=event["Id"]):
                results = list(walks(event))
                self.assertEqual({frozenset(after & {P.SHARE, P.EXCLUSIVE, P.SECRET})
                                  for after, _, _ in results},
                                 {frozenset(), *(frozenset([f]) for f in (P.SHARE, P.EXCLUSIVE, P.SECRET))})
                for after, _, _ in results:
                    self.assertNotIn("soana.committed", after)
                    self.assertEqual("soana.closed" in after, P.EXCLUSIVE in after)
                if event["Id"].endswith(".commit"):
                    self.assertIn(P.DECIDED, only(p for n in event["Nodes"] if n["Id"] == "start" for p in n["Paragraphs"] if P.DECIDED in p["Requires"] and P.EXCLUSIVE in p["Forbids"])["Requires"])
                    self.assertIn(P.EXCLUSIVE, only(p for n in event["Nodes"] if n["Id"] == "start" for p in n["Paragraphs"] if P.DECIDED in p["Requires"] and P.EXCLUSIVE in p["Forbids"])["Forbids"])
                    self.assertTrue(all(P.DECIDED not in p["Requires"]
                                        for p in event["Nodes"][0]["Paragraphs"][:4]))

    def test_corven_arrival_requires_paid_pursuit_and_earned_soana(self):
        dispatch, arrival, exposure = P.SCENES[:3]
        self.assertIn("trickster.now", dispatch["Requires"])
        self.assertIn("soana.started", dispatch["Requires"])
        self.assertNotIn("soana.committed", dispatch["Requires"])
        self.assertIn(P.PURSUED, arrival["Requires"])
        self.assertIn("trickster.ever", arrival["Requires"])
        self.assertGreaterEqual(arrival["DelayHours"], 168)
        self.assertIn(P.BURIED, exposure["Requires"])
        for event in (dispatch, arrival, exposure):
            self.assertEqual(event["RequiresAnyGroups"], [])
        for event in (dispatch, arrival, exposure):
            self.assertEqual(event["ContactUnit"], P.ACTOR)
            self.assertEqual(event["Areas"], [P.WINTERSUN])
            self.assertEqual(event["Chapters"], [3, 5])
            for flag in P.LOSS:
                self.assertIn(flag, event["Forbids"])
            self.assertIn(P.RETURNED, event["Forbids"])
            self.assertIn("soana.after_quest", event["Requires"])
            self.assertTrue(event["AnswerLists"])
        for event in P.SCENES[3:6]:
            self.assertEqual(event["InteractionHub"], "soana.presence")
            self.assertIn(P.RETURNED, event["Requires"])
            self.assertEqual(event["AnswerLists"], [])
            self.assertNotIn("soana.after_quest", event["Requires"])
            for flag in P.LOSS:
                self.assertEqual(event["ForbidOverrides"][flag], R2.EFFECTIVE)
        for stance in (P.SHARE, P.SECRET):
            results = list(walks(dispatch, {stance}))
            for after, path, answer in results:
                if P.PURSUED in after:
                    self.assertIn("read", path)
                    payment = next(a for n in dispatch["Nodes"] for a in n["Choices"]
                                   if P.PURSUED in a["Set"] and a.get("Crusade"))
                    self.assertEqual(payment["Crusade"], {"Resource": "Finances", "Amount": -75})
                    self.assertTrue(any(P.PURSUED in a["Set"] and not a.get("Crusade")
                                        for n in dispatch["Nodes"] for a in n["Choices"]))
                self.assertNotIn(P.CONFIRMED, after)
                self.assertNotIn(P.TOGETHER, after)

    def test_confirmation_always_records_an_ending_state(self):
        for event in P.SCENES:
            for page in event["Nodes"]:
                for answer in page["Choices"]:
                    if P.CONFIRMED in answer["Set"]:
                        self.assertIsNone(answer.get("Next"))
                        self.assertEqual(len(set(answer["Set"]) & {P.TOGETHER, P.SEPARATED, P.DISTANT, P.QUIET_RETURN}), 1)

    def test_partner_answers_and_affair_fallout_are_real(self):
        for stance in (P.SHARE, P.SECRET):
            for after, path, _ in walks(P.SCENES[1], {stance, P.PURSUED, "soana.committed"}):
                self.assertIn(P.CONFIRMED, after)
                if stance == P.SHARE:
                    self.assertIn(P.TOGETHER, after)
                    self.assertNotIn(P.SEPARATED, after)
                    self.assertNotIn(P.EXPOSED, after)
                else:
                    self.assertIn(P.SEPARATED, after)
                    self.assertIn(P.EXPOSED, after)
                    self.assertIn(P.BROKEN, after)
                    self.assertIn("soana.closed", after)
        for stance in (P.SHARE, P.SECRET):
            for after, _, _ in walks(P.SCENES[2], {stance, P.BURIED, "soana.committed"}):
                self.assertIn(P.CONFIRMED, after)
                self.assertIn(P.DISTANT if stance == P.SHARE else P.SEPARATED, after)
                self.assertNotIn(P.TOGETHER, after)
                self.assertIn(P.BROKEN, after)
                self.assertIn("soana.closed", after)
                self.assertEqual(P.EXPOSED in after, stance == P.SECRET)

    def test_every_ending_page_and_lastcall_reads_current_state(self):
        pages = [s for s in L.SCENES + T.SCENES if s.get("Relationship") == "soana" and s["Owner"].endswith("Epilogue")]
        pages.extend(s for rel, s in lastcall_partners.pages() if rel == "soana")
        self.assertTrue({"soana.lastcall.page", "soana.trickster.epilogue.commit", "soana.trickster.epilogue.luck_late"}
                        <= {s["Id"] for s in pages})
        for event in pages:
            for page in event["Nodes"]:
                with self.subTest(scene=event["Id"], node=page["Id"]):
                    paragraphs = page.get("Paragraphs", [])
                    unset = [p for p in paragraphs if set((P.SHARE, P.EXCLUSIVE, P.SECRET)) <= set(p.get("Forbids", ()))]
                    self.assertTrue(available(only(unset), set()))
                    self.assertTrue(all(not available(only(unset), {s}) for s in (P.SHARE, P.EXCLUSIVE, P.SECRET)))
                    for known in (set(), {P.CONFIRMED, P.TOGETHER}, {P.CONFIRMED, P.SEPARATED}, {P.CONFIRMED, P.DISTANT}):
                        flags = known | {P.SHARE}
                        state = [p for p in paragraphs if available(p, flags)
                                 and (P.CONFIRMED in p.get("Forbids", ()) or
                                      set(p.get("Requires", ())) & {P.TOGETHER, P.SEPARATED, P.DISTANT})]
                        # Unknown stance/lead paragraphs can also forbid CONFIRMED;
                        # the first state paragraph must always cover the history.
                        self.assertTrue(state)
                    self.assertTrue(any(P.SHARE in p.get("Requires", ()) for p in paragraphs))
                    self.assertTrue(any(P.SECRET in p.get("Requires", ()) for p in paragraphs))
                    self.assertTrue(any(P.EXCLUSIVE in p.get("Requires", ()) for p in paragraphs))

    def test_registered_debt_paragraph_slots_survive_integration(self):
        from storylines import soana_opening, soana_continuation, soana_later_progression
        payload = {"Scenes": copy.deepcopy(soana_opening.SCENES + soana_continuation.SCENES +
                                            soana_later_progression.SCENES + L.SCENES + T.SCENES),
                   "Relationships": {"soana": {"Guidance": ""}}}
        T.integrate(payload)
        scenes = {s["Id"]: s for s in payload["Scenes"]}
        for name in T.ALIVE_ENDINGS:
            event = scenes["soana.ending_" + name]
            for page in event["Nodes"]:
                if any(a.get("Next") for a in page["Choices"]):
                    continue
                with self.subTest(scene=event["Id"], node=page["Id"]):
                    self.assertEqual(metadata(page["Paragraphs"][:3]), metadata(T.ALIVE_PARAGRAPHS))
                    if name == "sacrifice":
                        self.assertIn(metadata(T.PORTION_DEAD), [metadata(p) for p in page["Paragraphs"]])
                    self.assertTrue(any(P.CONFIRMED in p.get("Forbids", ())
                                        for p in page["Paragraphs"][3:]))
        before = copy.deepcopy(payload["Scenes"])
        P.finish_normal_endings(payload["Scenes"])
        # Round-two correspondence adds a distinct marriage paragraph. A later
        # partner-tail reconciliation may move those additions, but must keep
        # the registered three creditor slots at their original indices.
        old = {s['Id']: s for s in before}
        for event in payload['Scenes']:
            if event['Id'] not in {'soana.ending_' + name for name in T.ALIVE_ENDINGS}:
                continue
            for actual, prior in zip(event['Nodes'], old[event['Id']]['Nodes']):
                self.assertEqual(metadata(actual.get('Paragraphs', [])[:3]),
                                 metadata(prior.get('Paragraphs', [])[:3]))

    def test_lastcall_amendment_is_route_local_and_idempotent(self):
        before = copy.deepcopy(lastcall_partners.PARTNERS)
        P.lastcall()
        P.lastcall()
        self.assertEqual(metadata(before), metadata(lastcall_partners.PARTNERS))


if __name__ == "__main__":
    unittest.main()
