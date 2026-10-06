"""eng7-l14: history versus live prose, earned reachability and stable IDs."""
import copy
import re
import unittest
from tests.structure import without_prose

from storylines import crossroute_presence as guard
from tools.crossroute_checks import other_woman
from tools.crossroute_checks.common import AND, lit, Proof, verify, blocks, fields
from tools.crossroute_checks.mention_context import live_mentions, reference_reason
from tests.test_crossroute_lint import fixture, relationship, run


class MentionContextTests(unittest.TestCase):
    def test_native_campaign_records_do_not_require_a_current_romance(self):
        pattern = re.compile("Anevia|Irabeth|Beth", re.I)
        for history in ("Anevia left Drezen at the Coronation a widow.",
                        "Irabeth survived Iz.", "Irabeth outlived Iz.",
                        "Irabeth came back from Iz.", "Anevia had gone south.",
                        "Beth always came first.", "Beth never reconciled with the Commander.",
                        "News of Beth's survival followed her.",
                        "She returned after taking Irabeth away from the Commander's betrayal.",
                        "The humiliation she had suffered in Drezen eroded Irabeth's fighting spirit."):
            with self.subTest(history=history):
                self.assertEqual(live_mentions(history, pattern, postwar=True), [])
                self.assertTrue(live_mentions(history + " Irabeth waits in the doorway.", pattern, postwar=True))
                self.assertTrue(live_mentions(history.rstrip(".") + ", but she will visit tonight.", pattern, postwar=True))
        self.assertTrue(live_mentions("Anevia went south every winter.", pattern, postwar=True))
        self.assertTrue(live_mentions("Irabeth came back every winter.", pattern, postwar=True))

    def test_unreturned_absence_is_readable_without_bringing_the_woman_back(self):
        pattern = re.compile("Beth", re.I)
        history = "Beth had not come back from Iz. She had another name to remember."
        self.assertEqual(live_mentions(history, pattern, postwar=True), [])
        self.assertEqual(len(live_mentions(history + " Beth waits in the doorway.", pattern, postwar=True)), 1)
        self.assertTrue(live_mentions("Beth had not come back from Iz, but she will visit tonight.",
                                      pattern, postwar=True))

    def test_first_session_record_survives_loss_without_exempting_current_visits(self):
        pattern = re.compile("Eritrice", re.I)
        history = ("Chadali kept the minutes of that first session. Beside the laughter, "
                   "Eritrice had drawn the little squiggle. Chadali still tapped it.")
        self.assertEqual(live_mentions(history, pattern, postwar=True), [])
        self.assertEqual(len(live_mentions(history + " Eritrice waits at the door.", pattern, postwar=True)), 1)
        self.assertTrue(live_mentions(history.replace("had drawn", "had drawn, but she will visit tonight beside"),
                                      pattern, postwar=True))
        self.assertTrue(live_mentions("Eritrice drew the minutes every winter.", pattern, postwar=True))

    def test_campaign_news_reaction_does_not_restore_its_witness(self):
        pattern = re.compile(r"\bCamellia\b", re.I)
        history = "{n}Camellia said, when the news reached camp, and tilted her head.{/n}"
        self.assertEqual(live_mentions(history, pattern, postwar=True), [])
        self.assertTrue(live_mentions(history + " Camellia waits here tonight.", pattern, postwar=True))
        self.assertTrue(live_mentions(history.replace("and tilted her head", "and she waits here tonight"),
                                      pattern, postwar=True))

    def test_history_mourning_reputation_and_religion_do_not_assert_life(self):
        for text in (
            "I remember Seelah.", "Seelah is in any answer I give, whether she's here to give it with me or not.", "Seelah died at Iz.", "Seelah loved me alive.", "Seelah's told me so.", "Nobody has said that since Seelah.", "Seelah's spare surcoat lies on the chair.", "Seelah's knights could hear it.", "The woman who had loved Seelah kept her anger.",
            "They are paid better than they were under Seelah.",
            "I held the mouth of that hole for Seelah because I chose to.",
            "I have been called Seelah by my father's guests.",
            "Seelah came to visit, the first year. Then she stopped coming.",
            "Seelah was the cleverest of us.",
            '"Tell me about Seelah."', "Keep Seelah's war out of the palace.",
            "Not served, the way Seelah served.",
            "I remember Lady Seelah's guests.", "A table like Lady Seelah's.",
            "Lady Seelah's guests spent everything to sit at her table.",
            "There was a Seelah on my menu. A boy who wore her face.",
            "You put a deposit on her corpse. 'One Seelah, forever.'", "Speak about losing Seelah.", "Seelah's grave is outside the walls.", "We speak about Seelah's absence.",
            "Seelah's reputation survived the siege.", "Seelah gave me this sword in Kenabres.",
            "Seelah is brave.", "Seelah would tell me that is not how to read it.",
            "\"Seelah's. Nothing important.\"",
            "{n}She tells a small story about a pen Seelah swore she had not stolen.{/n}",
            "I recall Seelah in Kenabres. Now I keep her old shield.",
        ):
            with self.subTest(text=text):
                self.assertEqual(run(other_woman, fixture(text)), [])
        pattern = re.compile(r"the silver dragon", re.I)
        self.assertEqual(live_mentions("The silver dragon who knelt over you in the festival square, and what she promised you.", pattern), [])
        pattern = re.compile(r"Iomedae|Inheritor", re.I)
        for text in ("The Church of Iomedae asks for the sword.", "Iomedae help me.",
                     "An acolyte of Iomedae put it out.", "The Inheritor's crusade.",
                     "The Hand of the Inheritor is holding the Fane.", "I thank Iomedae."):
            self.assertEqual(live_mentions(text, pattern), [])
        self.assertEqual(live_mentions("The Iomedaean chapter-master wrote to you.", re.compile("Iomedaean", re.I)), [])

    def test_live_staging_dialogue_reactions_and_plans_require_availability(self):
        for text in ("Seelah stands beside the fire.", "Seelah laughs at your answer.",
                     "I will hold the line for Seelah tomorrow.",
                     "I will meet Seelah tomorrow.", "Seelah's letter says she will visit tonight.",
                     "Seelah said she'll meet you.", "Since Seelah is here, we can begin.",
                     '"Tell me about Seelah. Will she visit tonight?"',
                     "{n}Seelah served the meal and sat beside you.{/n}",
                     "Lady Seelah's guests will visit tomorrow.",
                     "Seelah stands in Kenabres.", "You go where Seelah is standing.", "{n}Seelah killed a guard and raised her sword.{/n}", "{n}Seelah said nothing and raised her cup.{/n}"):
            with self.subTest(text=text):
                self.assertTrue(run(other_woman, fixture(text)))
        s = fixture("I remember that fight.")
        s["Scenes"][0]["Nodes"][0]["Speaker"] = "Seelah"
        self.assertTrue(run(other_woman, s))

    def test_mixed_history_and_live_occurrences_are_checked_separately(self):
        s = fixture("I remember Seelah in Kenabres. Seelah waits by the door.")
        self.assertTrue(run(other_woman, s))
        self.assertEqual(run(other_woman, fixture("Seelah's old letter lies on the desk.")), [])
        # An epilogue's past tense describes a new future, not a past memory.
        self.assertTrue(run(other_woman, fixture("Seelah kept the lamp filled every morning.", True)))
        self.assertTrue(run(other_woman, fixture("Seelah once joined them in Nerosyan.", True)))
        self.assertTrue(run(other_woman, fixture("I held the line for Seelah every winter.", True)))
        self.assertTrue(run(other_woman, fixture("Seelah tortured servants every winter.", True)))
        self.assertTrue(run(other_woman, fixture("I remember Seelah, but she is here now.")))

    def test_shyka_quoted_past_does_not_exempt_a_later_live_cameo(self):
        text = ('{n}Shyka reaches out, and does not touch you, and speaks in your voice: the voice you had that day, hoarse and young.{/n}\n'
                '"Seelah stood in the caves." {n}You hear every word for the last time.{/n}')
        pattern = re.compile("Seelah", re.I)
        self.assertEqual(live_mentions(text, pattern), [])
        self.assertEqual(len(live_mentions(text + " {n}Seelah waits at the door.{/n}", pattern)), 1)

    def test_reference_cannot_exempt_relative_or_coordinated_live_claim(self):
        for text in (
            "Unlike Seelah, who stands beside the fire, I am tired.",
            "If Seelah joins us tonight, we can begin.",
            "If Seelah watches the gate tonight, we can begin.",
            "If Seelah will join us tonight, we can begin.",
            "I remember Seelah, who now waits at the gate.",
            "I remember Seelah, who is now standing at the gate.",
            "I remember Seelah, who now watches the gate.",
            "Unlike Seelah, who leans against the gate, I am tired.",
            "Unlike Seelah, who will join us tonight, I am tired.",
            "Seelah is gone, but she waits at the gate.",
            "Seelah has already had a word with me and will meet us tonight.",
            "Seelah is brave and stands at the gate.",
            "Seelah's old letters lie on the desk; she arrives tonight.",
            "Seelah's old letters lie on the desk; she is here now.",
            "Seelah's old letters lie on the desk; she holds my hand.",
        ):
            with self.subTest(text=text):
                story = fixture(text)
                self.assertTrue(run(other_woman, story))
                guard.integrate(story)
                self.assertEqual(run(other_woman, story), [])
                model = verify.Model(copy.deepcopy(story))
                proof = Proof(model)
                context = AND(lit("chapter_later"), fields(story["Scenes"][0], overrides=True))
                self.assertTrue(proof.implies(AND(context, lit("seelah.dead")), lit("seelah.returned")))
                self.assertFalse(proof.implies(AND(context, lit("trickster.ever"), lit("seelah.dead"), lit("seelah.returned")),
                                               lit("seelah.returned", False)))
        self.assertTrue(run(other_woman, fixture("Seelah came to visit, the first year. Then she stopped coming.", True)))
        for text in ("Unlike Seelah, I never liked wine.",
                     "If Seelah were here, she would have laughed.",
                     "I remember Seelah, who once stood beside the fire.",
                     "Seelah's old letters lie on the desk; I arrive tonight.",
                     "{n}A knight of Seelah's company takes off his helmet and holds it under his arm.{/n}",
                     "{n}When Seelah's name was spoken in her hearing she went quiet, and later she would go and stand a watch.{/n}"):
            with self.subTest(reference=text):
                self.assertEqual(run(other_woman, fixture(text)), [])

    def test_declared_memory_does_not_require_current_life(self):
        s = fixture("{n}Seelah stands beside you in Kenabres.{/n}")
        s["Scenes"][0]["Kind"] = "memory"
        self.assertEqual(run(other_woman, s), [])
        before = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(before))

    def test_paid_prologue_receipt_does_not_require_the_dragon_return(self):
        text = "The Commander paid for the page with a morning in Kenabres: the silver dragon's promise in the festival square."
        pattern = re.compile(r"the silver dragon", re.I)
        self.assertEqual(live_mentions(text, pattern, postwar=True), [])
        self.assertTrue(live_mentions(text[:-1] + ", but she will visit tonight.", pattern, postwar=True))
        story = fixture(text, epilogue=True)
        story["Relationships"]["terendelev"] = dict(relationship("terendelev"), UnavailableFlags=[])
        guard.integrate(story)
        self.assertNotIn("crossroute.terendelev.available", story["Scenes"][0]["Requires"])
        self.assertEqual(run(other_woman, story), [])

    def test_campaign_killer_receipt_survives_the_killers_later_loss(self):
        for sid in ("soana.ending_native_loss", "soana.ending_unfinished_loss"):
            with self.subTest(scene=sid):
                story = fixture("{n}Camellia killed Soana. The cave kept her old blanket.{/n}", True)
                story["Relationships"]["soana"] = dict(relationship("soana"), UnavailableFlags=[])
                story["Relationships"]["camellia"] = relationship("camellia")
                scene = story["Scenes"][0]
                scene.update(Id=sid, Relationship="soana")
                scene["Nodes"][0]["Id"] = "camellia"
                guard.integrate(story)
                scene = story["Scenes"][0]
                self.assertEqual(scene["Requires"], [])
                self.assertEqual(scene["Forbids"], [])
                self.assertEqual(run(other_woman, story), [])
                proof = Proof(verify.Model(copy.deepcopy(story)))
                lost = AND(lit("camellia.dead"), lit("camellia.departed"), lit("camellia.closed"),
                           lit("camellia.returned", False))
                self.assertTrue(proof.implies(lost, fields(scene, overrides=True)))
                self.assertFalse(proof.implies(lost, lit("camellia.returned")))
                scene["Nodes"][0]["Text"] += " {n}Camellia waits at the gate.{/n}"
                self.assertTrue(run(other_woman, story))
        self.assertTrue(run(other_woman, fixture(
            "{n}During the crusade, Seelah killed Soana and she will visit tonight.{/n}", True)))

    def test_foresight_witness_recollections_keep_departed_helpers_historical(self):
        texts = (
            '"Then I got a proper look at your face and thought: oh, that\'s the one Terendelev healed."',
            '"That was you, the first time I ever saw you. Down in the caves, grey as a fish, and Seelah with her hand on her sword because she thought you were a cultist."',
        )
        for text in texts:
            with self.subTest(text=text):
                story = fixture(text)
                story["Relationships"]["terendelev"] = dict(relationship("terendelev"), UnavailableFlags=[])
                guard.integrate(story)
                self.assertEqual(run(other_woman, story), [])
                self.assertFalse(any(f.startswith("crossroute.") for f in story["Scenes"][0]["Requires"] + story["Scenes"][0]["Forbids"]))
        self.assertTrue(run(other_woman, fixture("Seelah healed me and will visit tonight.")))


class GuardPassTests(unittest.TestCase):
    def test_prologue_native_audience_uses_losses_without_a_later_chapter_flag(self):
        story = fixture("{n}Seelah stands beside Camellia.{/n}")
        scene = story["Scenes"][0]
        scene.update(MinChapter=0, MaxChapter=0, Chapters=[0], ReturnToList=True,
                     AnswerLists=[other_woman.NATIVE_AUDIENCES["seelah"][0]])
        guard.integrate(story)
        scene = story["Scenes"][0]
        self.assertEqual(scene["Requires"], [])
        self.assertEqual(run(other_woman, story), [])
        proof = Proof(verify.Model(copy.deepcopy(story)))
        present = AND(*(lit(f, False) for f in
            ("chapter_one", "chapter_later", "trickster.ever", "seelah.dead", "seelah.departed", "seelah.refused", "trickster.failed")))
        self.assertTrue(proof.implies(present, fields(scene, overrides=True)))
        self.assertFalse(proof.implies(present, lit("seelah.dead")))
        self.assertTrue(proof.implies(fields(scene, overrides=True), lit("seelah.dead", False)))

    def test_partner_presence_keeps_restricted_reader_contracts(self):
        for route in ("longcon", "lastcall", "nenio", "aranka"):
            with self.subTest(route=route):
                story = fixture("{n}Galfrey stands beside the fire.{/n}")
                story["Relationships"][route] = dict(relationship(route), UnavailableFlags=[])
                scene = story["Scenes"][0]
                scene.update(Relationship=route, Requires=[route + ".begun"])
                guard.integrate(story)
                scene = story["Scenes"][0]
                self.assertNotIn("galfrey.closed", scene["Requires"] + scene["Forbids"])
                self.assertEqual(run(other_woman, story), [])
                proof = Proof(verify.Model(copy.deepcopy(story)))
                self.assertTrue(proof.implies(AND(lit("chapter_later"), fields(scene, overrides=True)), lit("galfrey.closed", False)))
                self.assertEqual(scene["Requires"], [route + ".begun"])
                earned = AND(lit("chapter_later"), lit("galfrey.dead"), lit("galfrey.returned"),
                             lit(route + ".begun"), *(lit(f, False) for f in
                                 ("galfrey.closed", "galfrey.departed", "galfrey.refused", "trickster.failed")))
                self.assertTrue(proof.implies(earned, fields(scene, overrides=True)))
                self.assertFalse(proof.implies(earned, lit("galfrey.returned", False)))

    def test_guest_body_return_does_not_restart_original_delay(self):
        story = fixture("{n}The silver dragon stands beside the fire.{/n}")
        story["Relationships"]["terendelev"] = dict(relationship("terendelev"), UnavailableFlags=[])
        scene = story["Scenes"][0]
        scene.update(Requires=["funeral.latched"], DelayHours=72)
        guard.integrate(story)
        scene = story["Scenes"][0]
        self.assertEqual(scene["Requires"], ["funeral.latched"])
        self.assertEqual(scene["DelayHours"], 72)
        self.assertEqual(run(other_woman, story), [])
        proof = Proof(verify.Model(copy.deepcopy(story)))
        context = AND(lit("chapter_later"), fields(scene, overrides=True))
        self.assertTrue(proof.implies(context, lit("terendelev.trickster.returned")))
        earned = AND(lit("chapter_later"), lit("trickster.ever"), lit("funeral.latched"),
                     lit("terendelev.trickster.returned"), lit("terendelev.closed", False),
                     lit("terendelev.parent_lich_bind", False))
        self.assertTrue(proof.implies(earned, fields(scene, overrides=True)))
        self.assertFalse(proof.implies(earned, lit("terendelev.trickster.returned", False)))

    def test_native_reaction_reads_return_without_a_stale_absence_veto(self):
        story = fixture("The officer answers.")
        story["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        scene = story["Scenes"][0]
        scene.update(Reaction=True)
        scene["Nodes"][0]["Speaker"] = "Irabeth"
        guard.integrate(story)
        scene = story["Scenes"][0]
        self.assertNotIn("crossroute.irabeth.unavailable", scene["Forbids"])
        self.assertEqual(scene["ForbidOverrides"]["irabeth_dead"], "irabeth.trickster.returned")
        proof = Proof(verify.Model(copy.deepcopy(story)))
        earned = AND(lit("irabeth_dead"), lit("irabeth.trickster.returned"), lit("irabeth_gone", False))
        self.assertTrue(proof.implies(earned, fields(scene, overrides=True)))
        self.assertTrue(proof.implies(AND(fields(scene, overrides=True), lit("irabeth_dead")),
                                     lit("irabeth.trickster.returned")))
        self.assertEqual(run(other_woman, story), [])

    def test_longcon_native_host_retains_its_existing_paid_departure_adapter(self):
        s = fixture("{n}Irabeth closes the ledger.{/n}")
        s["Relationships"]["longcon"] = dict(relationship("longcon"), UnavailableFlags=[], UnavailableOverrides={})
        s["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        s["Presences"] = {"irabeth.presence": dict(Unit="native-irabeth", Requires=["irabeth.trickster.returned"])}
        scene = s["Scenes"][0]
        scene.update(Id="longcon.the_talk", Relationship="longcon", Owner="Irabeth",
            ContactUnit="native-irabeth", Requires=["longcon.begun"],
            Forbids=["irabeth_dead", "irabeth_gone"],
            ForbidOverrides={"irabeth_dead": "irabeth.trickster.returned",
                             "irabeth_gone": "irabeth.trickster.returned"})
        guard.integrate(s)
        scene = s["Scenes"][0]
        self.assertEqual(scene["Requires"], ["longcon.begun"])
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        context = fields(scene, overrides=True)
        paid = AND(lit("longcon.begun"), lit("irabeth_gone"), lit("irabeth_dead"),
                   lit("irabeth.trickster.returned"), lit("swarm", False), lit("true_lich", False))
        self.assertTrue(proof.implies(paid, context))
        self.assertFalse(proof.implies(paid, lit("irabeth.trickster.returned", False)))
        self.assertTrue(proof.implies(AND(context, lit("irabeth_gone")), lit("irabeth.trickster.returned")))
        # Neither another route nor an unbound contact inherits this adapter.
        self.assertEqual(other_woman.local_return_overrides(s, dict(scene, Relationship="galfrey"), "irabeth"), {})
        self.assertEqual(other_woman.local_return_overrides(s, dict(scene, ContactUnit="other-unit"), "irabeth"), {})
        summons = copy.deepcopy(s)
        letter = summons["Scenes"][0]
        letter.update(Id="longcon.the_summons", Kind="letter", Remote=True)
        letter.pop("ContactUnit")
        guard.integrate(summons)
        self.assertEqual(run(other_woman, summons), [])

    def test_fixed_native_audience_fields_keep_the_same_live_guard_on_every_arm(self):
        s = fixture("Minagho turns toward the door.")
        s["Relationships"]["minagho_chivarro"] = relationship("minachiv")
        scene = s["Scenes"][0]
        scene.update(Owner="Minagho", Chapters=[2],
            AnswerLists=["41dff710486d05d49bbb663f729ddabd"],
            NativeReturnCue="7be28a1118c8af24ebf757789b9cfa4c",
            Requires=["offer.begun"], Forbids=["offer.done"],
            RequiresAnyGroups=[["offer.loud", "offer.quiet"]])
        guard.scene_guard(scene, s, "minagho", "minagho_chivarro")
        self.assertEqual(scene["Requires"], ["offer.begun"])
        self.assertEqual(scene["Forbids"], ["offer.done"])
        self.assertEqual(scene["RequiresAnyGroups"],
            [["offer.loud", "offer.quiet"], ["crossroute.minagho.available"]])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        live = lit("crossroute.minagho.available")
        self.assertTrue(proof.implies(fields(scene), live))
        earned = AND(lit("chapter_later"), lit("minachiv.dead"), lit("minachiv.returned"),
            lit("minachiv.closed", False), lit("minachiv.departed", False),
            lit("minachiv.refused", False), lit("trickster.failed", False))
        self.assertTrue(proof.implies(earned, live))
        self.assertFalse(proof.implies(earned, lit("minachiv.returned", False)))

    def test_each_incoming_guard_is_proved_even_when_their_spellings_differ(self):
        s = fixture("The fire burns.")
        guard.availability(s, "seelah", "seelah")
        nodes = s["Scenes"][0]["Nodes"]
        nodes[0]["Choices"] = [dict(Text="Speak.", Next="guest",
            Forbids=["seelah.closed", "seelah.dead", "seelah.departed", "seelah.refused", "trickster.failed"]),
            dict(Text="Speak after the return.", Next="guest", Requires=["seelah.returned"],
                 Forbids=["seelah.closed", "seelah.departed", "seelah.refused", "trickster.failed"])]
        nodes.append(dict(Id="guest", Speaker="Seelah", Text="Seelah stands beside the fire.", Choices=[dict(Text="Leave", Next=None)]))
        self.assertEqual(run(other_woman, s), [])
        # An edge which changes a live input cannot inherit yesterday's guard.
        nodes[0]["Choices"][0]["Set"] = ["seelah.dead"]
        self.assertTrue(run(other_woman, s))
        nodes[0]["Choices"][0].pop("Set")
        nodes[0]["Choices"].append(dict(Text="Speak without earning it.", Next="guest"))
        self.assertTrue(run(other_woman, s))

    def test_presence_departure_veto_survives_an_empty_relationship_loss_list(self):
        s = fixture("Nidalynn stands beside the fire.")
        s["Relationships"].pop("seelah")
        s["Relationships"]["nidalynn"] = dict(relationship("nidalynn"), UnavailableFlags=[], UnavailableOverrides={})
        guard.integrate(s)
        proof = Proof(verify.Model(copy.deepcopy(s)))
        self.assertTrue(proof.implies(lit("crossroute.nidalynn.available"), lit("nidalynn.trickster.left_with_it", False)))
        gone = AND(lit("chapter_later"), lit("nidalynn.trickster.left_with_it"))
        self.assertTrue(proof.implies(gone, lit("crossroute.nidalynn.available", False)))
        self.assertEqual(run(other_woman, s), [])

    def test_canon_dead_body_needs_existing_paid_return_and_retains_hard_refusal(self):
        for woman in ("hepzamirah", "terendelev", "delamere"):
            s = fixture(woman.title() + " stands beside the fire.")
            s["Relationships"].pop("seelah")
            s["Relationships"][woman] = dict(relationship(woman), UnavailableFlags=[], UnavailableOverrides={})
            guard.integrate(s)
            for groups in s["Derived"].values():
                self.assertTrue(all(group and len(group) == len(set(group)) for group in groups))
            proof = Proof(verify.Model(copy.deepcopy(s)))
            key = "crossroute." + woman + ".available"
            self.assertTrue(proof.implies(lit(key), lit(woman + ".trickster.returned")))
            self.assertTrue(proof.implies(lit(key), lit(woman + ".closed", False)))
            earned = AND(lit("chapter_later"), lit("trickster.ever"), lit(woman + ".trickster.returned"),
                lit(woman + ".closed", False), lit("terendelev.parent_lich_bind", False),
                lit(woman + ".committed", False), lit(woman + ".started", False))
            self.assertTrue(proof.implies(earned, lit(key)))
            self.assertFalse(proof.implies(earned, lit(woman + ".trickster.returned", False)))
            self.assertEqual(run(other_woman, s), [])

    def test_live_guard_blocks_losses_and_preserves_earned_return_without_romance(self):
        s = fixture("{n}Seelah stands beside the fire.{/n}")
        original = copy.deepcopy(s["Scenes"])
        guard.integrate(s)
        self.assertEqual(run(other_woman, s), [])
        key = "crossroute.seelah.available"
        model = verify.Model(copy.deepcopy(s))
        proof = Proof(model)
        for loss in ("seelah.dead", "seelah.departed", "seelah.refused"):
            self.assertTrue(proof.implies(AND(lit(key), lit(loss)), lit("seelah.returned")) if loss == "seelah.dead"
                            else proof.implies(AND(lit(key)), lit(loss, False)))
        earned = AND(lit("chapter_later"), lit("seelah.dead"), lit("seelah.returned"),
                     *(lit(k, False) for k in ("seelah.closed", "seelah.departed", "seelah.refused",
                                              "trickster.failed", "seelah.committed", "seelah.started")))
        self.assertTrue(proof.implies(earned, lit(key)))
        # The earned world is satisfiable: the assertion above is not vacuous.
        self.assertFalse(proof.implies(earned, lit("seelah.returned", False)))
        # Complete-only rules snapshots still read the same current losses.
        no_native_chapter_reader = AND(lit("trickster.ever"), lit("seelah.dead"), lit("seelah.returned"),
            *(lit(f, False) for f in ("chapter_one", "chapter_later", "seelah.closed", "seelah.departed", "seelah.refused", "trickster.failed")))
        self.assertTrue(proof.implies(no_native_chapter_reader, lit(key)))
        self.assertFalse(proof.implies(no_native_chapter_reader, lit("seelah.returned", False)))
        # A native companion's romance refusal leaves her undeparted body.
        closed_but_alive = AND(lit("chapter_later"), lit("seelah.closed"),
                               *(lit(k, False) for k in ("seelah.dead", "seelah.departed", "seelah.refused", "trickster.failed")))
        self.assertTrue(proof.implies(closed_but_alive, lit(key)))
        self.assertFalse(proof.implies(closed_but_alive, lit("seelah.closed", False)))
        closed_return = AND(lit("chapter_later"), lit("seelah.closed"), lit("seelah.dead"), lit("seelah.returned"))
        self.assertTrue(proof.implies(closed_return, lit(key, False)))
        self.assertEqual(s["Relationships"], fixture()["Relationships"])
        self.assertEqual([n["Id"] for n in s["Scenes"][0]["Nodes"]], [n["Id"] for n in original[0]["Nodes"]])
        self.assertEqual(without_prose(s["Scenes"][0]["Nodes"][0]["Choices"]), without_prose(original[0]["Nodes"][0]["Choices"]))
        first = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(first))

    def test_tirabade_romance_refusal_retains_living_native_wife_and_officer(self):
        s = fixture("Irabeth stands beside the fire.")
        s["Relationships"].pop("seelah")
        s["Relationships"]["irabeth"] = relationship("irabeth")
        guard.integrate(s)
        proof = Proof(verify.Model(copy.deepcopy(s)))
        native_wife = AND(lit("chapter_later"), lit("irabeth.closed"),
            *(lit(f, False) for f in ("irabeth.dead", "irabeth.departed", "irabeth.refused", "trickster.failed")))
        self.assertTrue(proof.implies(native_wife, lit("crossroute.irabeth.available")))
        self.assertFalse(proof.implies(native_wife, lit("irabeth.closed", False)))
        self.assertEqual(run(other_woman, s), [])

    def test_mourning_remains_available_and_does_not_require_return(self):
        s = fixture("{n}Seelah died at Iz. I remember Seelah in Kenabres.{/n}")
        before = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(before))

    def test_mixed_epilogue_keeps_owner_page_and_gates_all_guests(self):
        s = fixture("{n}Galfrey keeps her sword.{/n}\n{n}Seelah arrives with Ember.{/n}", True)
        s["Relationships"]["ember"] = relationship("ember")
        s["Scenes"].append(dict(Id="ember.owner", Owner="Ember", Relationship="ember", Nodes=[]))
        node = s["Scenes"][0]["Nodes"][0]
        node["Paragraphs"] = [dict(Text="The standard remains.")]
        guard.integrate(s)
        node = s["Scenes"][0]["Nodes"][0]
        self.assertEqual(len(node["Paragraphs"]), 2)
        self.assertEqual(without_prose(node["Paragraphs"][0]), {})
        self.assertEqual(set(node["Paragraphs"][1]["Requires"]),
                         {"crossroute.seelah.available", "crossroute.ember.available"})
        self.assertEqual(s["Scenes"][0]["Requires"], [])
        self.assertEqual(run(other_woman, s), [])

    def test_shared_generator_collections_do_not_leak_guards_to_siblings(self):
        s = fixture("{n}Seelah stands beside the fire.{/n}")
        sibling = copy.deepcopy(s["Scenes"][0])
        sibling["Id"] = "galfrey.independent"
        sibling["Nodes"][0]["Text"] = "{n}Galfrey keeps her sword.{/n}"
        shared_forbids, shared_overrides = [], {}
        for scene in (s["Scenes"][0], sibling):
            scene["Forbids"] = shared_forbids
            scene["ForbidOverrides"] = shared_overrides
        s["Scenes"].append(sibling)
        guard.integrate(s)
        self.assertIn("crossroute.seelah.unavailable", s["Scenes"][0]["Forbids"])
        self.assertEqual(s["Scenes"][1]["Forbids"], [])
        self.assertEqual(s["Scenes"][1]["ForbidOverrides"], {})
        self.assertEqual(shared_forbids, [])
        self.assertEqual(shared_overrides, {})

    def test_existing_living_choice_and_descendants_keep_selectable_answers(self):
        s = fixture("A quiet room.")
        scene = s["Scenes"][0]
        scene["Nodes"][0]["Choices"] = [dict(Text="Ask Seelah tonight.", Next="later", Set=[],
            Requires=[], Forbids=["seelah.closed", "seelah.dead", "seelah.departed", "seelah.refused", "trickster.failed"])]
        scene["Nodes"].append(dict(Id="later", Speaker="Galfrey", Text="{n}Seelah stands by the fire.{/n}",
            Choices=[dict(Text="Keep that goodbye for Seelah.", Next=None, Set=[], Requires=[], Forbids=[])]))
        before = copy.deepcopy(scene["Nodes"])
        guard.integrate(s)
        self.assertEqual(without_prose(s["Scenes"][0]["Nodes"]), without_prose(before))
        self.assertEqual(s["Scenes"][0]["Forbids"], [])
        self.assertEqual(run(other_woman, s), [])

    def test_widow_recitation_retains_the_same_remembered_counsel(self):
        s = fixture("Nevi says I built the cage myself.")
        s["Relationships"]["anevia"] = s["Relationships"].pop("seelah")
        scene = s["Scenes"][0]
        scene.update(Id="irabeth.a_name_on_the_list", Relationship="irabeth", Owner="Irabeth")
        s["Relationships"]["irabeth"] = relationship("irabeth")
        scene["Nodes"][0]["Id"] = "company"
        s["Scenes"].append(dict(Id="anevia.owner", Owner="Anevia", Relationship="anevia", Nodes=[]))
        guard.integrate(s)
        self.assertEqual(s["Scenes"][0]["Forbids"], [])

    def test_changed_counsel_keeps_npc_speech_without_unselected_commander_turns(self):
        s = fixture()
        scene = s["Scenes"][0]
        scene["Id"] = "anevia.a_key_that_is_hers"
        node = scene["Nodes"][0]
        node["Id"] = "room"
        node["Text"] = ('"Beth says I should learn to make a loaf."\n"Would it fit here?"\n'
                        '"No. And I won\'t put it here."\n"You want that with Irabeth."\n"Yes. I want breakfast."')
        guard.integrate(s)
        text = s["Scenes"][0]["Nodes"][0]["Text"]
        from tools.player_text_lint import check
        self.assertFalse([r for r in check(s)["review"] if r["code"] == "speaker-attribution-review"])

    def test_widow_negotiation_appends_neutral_boundary_without_retargeting_answers(self):
        s = fixture()
        s["Relationships"]["anevia"] = s["Relationships"].pop("seelah")
        s["Relationships"]["irabeth"] = relationship("irabeth")
        scene = s["Scenes"][0]
        scene.update(Id="irabeth.the_question_outside_duty", Relationship="irabeth", Owner="Irabeth")
        scene["Nodes"] = [dict(Id="start", Speaker="Irabeth", Text="The question.",
            Choices=[dict(Text="Tell me.", Next="rank", Set=[], Requires=[], Forbids=[])]),
            dict(Id="rank", Speaker="Irabeth", Text='"And away from council?"\n"Some nights I\'ll have promised Nevi. Then it\'s no."',
            Choices=[dict(Text="I understand.", Next=None, Set=[], Requires=[], Forbids=[])])]
        s["Scenes"].append(dict(Id="anevia.owner", Owner="Anevia", Relationship="anevia", Nodes=[]))
        guard.integrate(s)
        nodes = s["Scenes"][0]["Nodes"]
        self.assertEqual([n["Id"] for n in nodes], ["start", "rank", "eng7_l14.rank_without_wife"])
        self.assertEqual(nodes[0]["Choices"][0]["Next"], "rank")
        self.assertEqual(nodes[0]["Choices"][1]["Next"], "eng7_l14.rank_without_wife")
        self.assertIn("crossroute.anevia.unavailable", nodes[0]["Choices"][0]["Forbids"])
        self.assertEqual(nodes[0]["Choices"][2]["Requires"], ["crossroute.anevia.unavailable"])
        self.assertEqual(len(nodes[0]["Choices"]), 3)
        self.assertEqual(s["Scenes"][0]["Forbids"], [])
        first = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(first))
        self.assertEqual(run(other_woman, s), [])

    def test_optional_live_branch_keeps_neutral_answer_and_earned_return(self):
        s = fixture("The fire burns.")
        scene = s["Scenes"][0]
        scene["Nodes"][0]["Choices"] = [dict(Text="Speak privately.", Next="bridge"),
                                            dict(Text="Leave.", Next=None)]
        scene["Nodes"].extend([
            dict(Id="bridge", Speaker="Galfrey", Text="A quiet moment.",
                 Choices=[dict(Text="Continue", Next="guest")]),
            dict(Id="guest", Speaker="Seelah", Text="{n}Seelah stands beside you.{/n}",
                 Choices=[dict(Text="Continue", Next=None)])])
        guard.integrate(s)
        nodes = s["Scenes"][0]["Nodes"]
        self.assertEqual(s["Scenes"][0]["Forbids"], [])
        self.assertEqual(nodes[0]["Choices"][0]["Forbids"], ["crossroute.seelah.unavailable"])
        self.assertEqual(without_prose(nodes[0]["Choices"][1]), dict(Next=None))
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        earned = AND(lit("chapter_later"), lit("seelah.dead"), lit("seelah.returned"),
                     *(lit(k, False) for k in ("seelah.closed", "seelah.departed", "seelah.refused", "trickster.failed")))
        self.assertTrue(proof.implies(earned, fields(nodes[0]["Choices"][0])))
        self.assertFalse(proof.implies(earned, lit("seelah.returned", False)))
        lost = AND(lit("chapter_later"), lit("seelah.dead"), lit("seelah.returned", False))
        self.assertTrue(proof.implies(lost, lit("crossroute.seelah.unavailable")))
        self.assertTrue(proof.implies(lost, fields(nodes[0]["Choices"][1])))

    def test_native_present_etude_does_not_block_existing_no_guest_branch_after_death(self):
        s = fixture("The forge is quiet.")
        s["Etudes"] = {f: "a" * 32 for f in (*s["Relationships"]["seelah"]["UnavailableFlags"], "seelah.present")}
        scene = s["Scenes"][0]
        scene["Nodes"][0]["Choices"] = [dict(Text="Continue", Next="guest", Requires=["seelah.present"]),
            dict(Text="Continue", Next="alone", Forbids=["seelah.present"])]
        scene["Nodes"].extend([
            dict(Id="guest", Speaker="Seelah", Text="Seelah stands by the forge.", Choices=[dict(Text="Leave", Next=None)]),
            dict(Id="alone", Speaker="Galfrey", Text="The forge is quiet.", Choices=[dict(Text="Leave", Next=None)])])
        guard.integrate(s)
        choices = s["Scenes"][0]["Nodes"][0]["Choices"]
        self.assertEqual(s["Scenes"][0]["Forbids"], [])
        self.assertEqual([c["Next"] for c in choices], ["guest", "alone", "alone"])
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        dead = AND(lit("chapter_later"), lit("seelah.present"), lit("seelah.dead"), lit("seelah.returned", False))
        self.assertTrue(proof.implies(dead, fields(choices[2])))
        self.assertTrue(proof.implies(dead, lit("crossroute.seelah.unavailable")))
        earned = AND(lit("chapter_later"), lit("seelah.present"), lit("seelah.dead"), lit("seelah.returned"),
            *(lit(f, False) for f in ("seelah.closed", "seelah.departed", "seelah.refused", "trickster.failed")))
        self.assertTrue(proof.implies(earned, fields(choices[0])))
        self.assertFalse(proof.implies(earned, lit("seelah.returned", False)))
        first = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(first))

    def test_guest_guard_covers_every_incoming_parent_after_fallback_lookup(self):
        s = fixture("The forge is quiet.")
        s["Etudes"] = {f: "a" * 32 for f in (*s["Relationships"]["seelah"]["UnavailableFlags"], "seelah.present")}
        scene = s["Scenes"][0]
        scene["Nodes"][0]["Choices"] = [dict(Text="First door", Next="first"), dict(Text="Second door", Next="second")]
        for parent in ("first", "second"):
            scene["Nodes"].append(dict(Id=parent, Speaker="Galfrey", Text="A door.", Choices=[
                dict(Text="Continue", Next="guest", Requires=["seelah.present"]),
                dict(Text="Leave", Next=None, Forbids=["seelah.present"])]))
        scene["Nodes"].append(dict(Id="guest", Speaker="Seelah", Text="Seelah stands by the forge.", Choices=[dict(Text="Leave", Next=None)]))
        guard.integrate(s)
        self.assertEqual(run(other_woman, s), [])
        for parent in s["Scenes"][0]["Nodes"][1:3]:
            self.assertIn("crossroute.seelah.unavailable", parent["Choices"][0]["Forbids"])
            self.assertEqual(len(parent["Choices"]), 3)
            self.assertIn("seelah.present", parent["Choices"][2]["Requires"])

    def test_departed_spouse_branch_keeps_neutral_morning_and_reads_later_return(self):
        s = fixture("A quiet room.")
        s["Relationships"].pop("seelah")
        s["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        s["Relationships"]["anevia"] = dict(relationship("anevia"),
            UnavailableFlags=["anevia_dead", "anevia_gone", "swarm", "true_lich"],
            UnavailableOverrides={"anevia_gone": "anevia.trickster.returned"})
        s["Etudes"] = {f: "a" * 32 for f in ("irabeth_dead", "irabeth_gone", "anevia_dead", "anevia_gone", "swarm", "true_lich")}
        scene = s["Scenes"][0]
        scene.update(Id="anevia.trickster.gone.commit", Owner="Anevia", Relationship="anevia",
            Requires=["trickster.ever", "anevia.trickster.returned", "anevia.trickster.gate_seen"])
        scene["Nodes"] = [dict(Id="start", Speaker="Anevia", Text="A quiet room.", Choices=[dict(Text="Continue", Next="threshold")]),
            dict(Id="threshold", Speaker="Anevia", Text="Grey light.", Choices=[
                dict(Text="Continue", Next="morning_left", Requires=["irabeth_gone"], Forbids=["irabeth.trickster.returned"]),
                dict(Text="Continue", Next="morning_quiet", Requires=["irabeth.trickster.returned"]),
                dict(Text="Continue", Next="morning", Forbids=["irabeth_gone", "irabeth.trickster.returned"])]),
            dict(Id="morning_left", Speaker="Anevia", Text="Beth's gonna know the second she looks at me.", Choices=[dict(Text="Leave", Next=None)]),
            dict(Id="morning_quiet", Speaker="Anevia", Text="Beth's gonna know the second she looks at me.", Choices=[dict(Text="Leave", Next=None)]),
            dict(Id="morning", Speaker="Anevia", Text="If Beth ever walks back through that gate, she'll know.", Choices=[dict(Text="Leave", Next=None)])]
        guard.integrate(s)
        scene = s["Scenes"][0]
        self.assertEqual(without_prose(scene["Nodes"][0]["Choices"]), [dict(Next="threshold")])
        choices = scene["Nodes"][1]["Choices"]
        self.assertEqual([c["Next"] for c in choices], ["morning_left", "morning_quiet", "morning", "morning"])
        self.assertNotIn("crossroute.irabeth.correspondent_unavailable", choices[1].get("Forbids", []))
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        dead = AND(lit("chapter_later"), lit("irabeth_gone"), lit("irabeth_dead"),
            lit("irabeth.trickster.returned", False), lit("swarm", False), lit("true_lich", False))
        self.assertTrue(proof.implies(dead, fields(choices[3])))
        earned = AND(lit("chapter_later"), lit("irabeth.trickster.returned"), lit("irabeth_dead"),
            lit("swarm", False), lit("true_lich", False))
        self.assertTrue(proof.implies(earned, fields(choices[1])))
        self.assertFalse(proof.implies(earned, lit("irabeth.trickster.returned", False)))

    def test_existing_courier_offer_does_not_reappear_departed_wife(self):
        s = fixture("I'll send it to Nevi. If she sends it back, the answer's no.")
        s["Relationships"]["anevia"] = dict(relationship("anevia"),
            UnavailableFlags=["anevia_dead", "anevia_gone", "swarm", "true_lich"],
            UnavailableOverrides={"anevia_gone": "anevia.trickster.returned"})
        s["Relationships"]["irabeth"] = relationship("irabeth")
        scene = s["Scenes"][0]
        scene.update(Id="irabeth.trickster.second_ask", Owner="Irabeth", Relationship="irabeth",
            MinChapter=5, MaxChapter=5,
            Requires=["trickster.ever", "irabeth.trickster.declined", "irabeth.trickster.back_on_duty"])
        scene["Nodes"][0].update(Id="price", Speaker="Irabeth")
        s["Scenes"].append(dict(Id="anevia.owner", Owner="Anevia", Relationship="anevia", Nodes=[]))
        before = copy.deepcopy(s)
        guard.integrate(s)
        scene = s["Scenes"][0]
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        self.assertTrue(proof.implies(AND(lit("chapter_later"), fields(scene, overrides=True)), lit("anevia_dead", False)))
        distant = AND(lit("chapter_later"), lit("anevia_gone"), lit("anevia.trickster.returned", False),
                      *(lit(k, False) for k in ("anevia_dead", "swarm", "true_lich")))
        self.assertTrue(proof.implies(distant, lit("crossroute.anevia.correspondent")))
        self.assertTrue(proof.implies(AND(distant, *(lit(k) for k in before["Scenes"][0]["Requires"])),
                                     fields(scene, overrides=True)))
        self.assertFalse(proof.implies(distant, lit("anevia.trickster.returned")))
        self.assertTrue(proof.implies(lit("crossroute.anevia.correspondent"), lit("anevia_dead", False)))
        # The same clause in another scene or without its existing paid-story
        # prerequisites cannot grant a distant-contact exception.
        before["Scenes"][0]["Requires"].remove("irabeth.trickster.declined")
        guard.integrate(before)
        proof = Proof(verify.Model(copy.deepcopy(before)))
        self.assertTrue(proof.implies(AND(lit("chapter_later"), fields(before["Scenes"][0], overrides=True), lit("anevia_gone")),
                                     lit("anevia.trickster.returned")))

    def test_paid_native_south_road_contact_keeps_departure_and_death_consequences(self):
        s = fixture("{n}Beth stands beside the bed.{/n}")
        s["Relationships"]["anevia"] = relationship("anevia")
        s["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        scene = s["Scenes"][0]
        scene.update(Id="anevia.trickster.gone.wardrobe", Owner="Anevia", Relationship="anevia",
            TricksterDevice=True, MinChapter=5, MaxChapter=5,
            Requires=["trickster.now", "anevia.trickster.primed", "anevia_gone", "irabeth_gone"])
        scene["Nodes"][0]["Id"] = "beth_left"
        s["Scenes"].append(dict(Id="irabeth.owner", Owner="Irabeth", Relationship="irabeth", Nodes=[]))
        original = copy.deepcopy(s)
        guard.integrate(s)
        scene = s["Scenes"][0]
        self.assertEqual(run(other_woman, s), [])
        self.assertEqual(s["Relationships"], original["Relationships"])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        away = AND(lit("chapter_later"), lit("irabeth_gone"), lit("irabeth.closed"),
                   lit("irabeth.trickster.returned", False),
                   *(lit(k, False) for k in ("irabeth_dead", "swarm", "true_lich")))
        self.assertTrue(proof.implies(away, lit("crossroute.irabeth.correspondent")))
        self.assertTrue(proof.implies(AND(away, *(lit(k) for k in original["Scenes"][0]["Requires"])),
                                     fields(scene, overrides=True)))
        self.assertFalse(proof.implies(away, lit("irabeth.trickster.returned")))
        self.assertTrue(proof.implies(AND(lit("crossroute.irabeth.correspondent"), lit("irabeth_dead")),
            lit("irabeth.trickster.returned")))
        self.assertTrue(proof.implies(AND(lit("chapter_later"), fields(scene, overrides=True), lit("irabeth_dead")),
                                     lit("irabeth.trickster.returned")))
        original["Scenes"][0]["Requires"].remove("anevia.trickster.primed")
        guard.integrate(original)
        proof = Proof(verify.Model(copy.deepcopy(original)))
        self.assertTrue(proof.implies(AND(lit("chapter_later"), fields(original["Scenes"][0], overrides=True), lit("irabeth_gone")),
                                     lit("irabeth.trickster.returned")))

    def test_later_loss_uses_existing_reproach_and_keeps_killer_account(self):
        s = fixture("A quiet arrival.")
        s["Relationships"]["anevia"] = relationship("anevia")
        s["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        scene = s["Scenes"][0]
        scene.update(Id="anevia.trickster.gone.wardrobe", Owner="Anevia", Relationship="anevia",
            TricksterDevice=True, MinChapter=5, MaxChapter=5,
            Requires=["trickster.now", "anevia.trickster.primed", "anevia_gone"])
        scene["Nodes"][0]["Choices"] = [
            dict(Text="Continue", Next="beth_left", Requires=["irabeth_gone"], Forbids=["irabeth.trickster.returned"]),
            dict(Text="Continue", Next="beth_dead", Forbids=["irabeth_gone", "irabeth.trickster.returned"]),
            dict(Text="Continue", Next="beth_back", Requires=["irabeth.trickster.returned"])]
        scene["Nodes"].extend([
            dict(Id="beth_left", Speaker="Narrator", Text="{n}Beth stands beside the bed.{/n}", Choices=[dict(Text="Continue")]),
            dict(Id="beth_dead", Speaker="Anevia", Text="You didn't come through anything for Beth.", Choices=[dict(Text="Continue")]),
            dict(Id="killer", Speaker="Anevia", Text="You killed her.", Choices=[dict(Text="Continue")]),
            dict(Id="beth_back", Speaker="Anevia", Text="The letter remains.", Choices=[dict(Text="Continue")])])
        s["Scenes"].append(dict(Id="irabeth.owner", Owner="Irabeth", Relationship="irabeth", Nodes=[]))
        original_targets = [c["Next"] for c in scene["Nodes"][0]["Choices"]]
        guard.integrate(s)
        scene = s["Scenes"][0]
        choices = scene["Nodes"][0]["Choices"]
        self.assertEqual([c["Next"] for c in choices[:3]], original_targets)
        self.assertEqual([c["Next"] for c in choices[3:]], ["beth_dead", "killer"])
        self.assertEqual(scene["Forbids"], [])
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        lost = AND(lit("chapter_later"), lit("irabeth_gone"), lit("irabeth_dead"),
                   lit("irabeth.trickster.returned", False))
        self.assertTrue(proof.implies(AND(lost, lit("anevia.irabeth_killed_by_commander", False)), fields(choices[3])))
        self.assertTrue(proof.implies(AND(lost, lit("anevia.irabeth_killed_by_commander")), fields(choices[4])))
        self.assertTrue(proof.implies(lost, lit("crossroute.irabeth.correspondent_unavailable")))
        first = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(first))

    def test_fetched_receipt_survives_later_death_but_future_visit_does_not(self):
        s = fixture("The Commander keeps the record.", True)
        s["Relationships"]["irabeth"] = dict(relationship("irabeth"),
            UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
            UnavailableOverrides={"irabeth_dead": "irabeth.trickster.returned"})
        s["Scenes"].append(dict(Id="irabeth.owner", Owner="Irabeth", Relationship="irabeth", Nodes=[]))
        historical = "Whenever the Commander asked, she said she had come back because Beth had fetched her."
        future = "Whenever Beth was in the room, she said it was the other way round."
        s["Scenes"][0]["Nodes"][0]["Paragraphs"] = [dict(Text=historical + " " + future, Requires=["fetched.known"])]
        guard.integrate(s)
        paragraphs = s["Scenes"][0]["Nodes"][0]["Paragraphs"]
        self.assertEqual(without_prose(paragraphs[0]), dict(Requires=["fetched.known"]))
        self.assertEqual(len(paragraphs), 2)
        self.assertIn("crossroute.irabeth.available", paragraphs[1]["Requires"])
        self.assertEqual(run(other_woman, s), [])
        proof = Proof(verify.Model(copy.deepcopy(s)))
        dead = AND(lit("fetched.known"), lit("irabeth_dead"), lit("irabeth.trickster.returned", False))
        self.assertTrue(proof.implies(dead, fields(paragraphs[0])))
        self.assertTrue(proof.implies(AND(fields(paragraphs[1]), lit("irabeth_dead")), lit("irabeth.trickster.returned")))
        first = copy.deepcopy(s)
        guard.integrate(s)
        self.assertEqual(without_prose(s), without_prose(first))

    def test_pair_seat_never_requires_other_woman_alive_or_committed(self):
        s = fixture()
        s["Relationships"]["pair"] = relationship("pair")
        s["Relationships"]["pair"]["UnavailableFlags"] = ["seelah.dead", "galfrey.dead"]
        s["Relationships"]["pair"]["UnavailableOverrides"] = {"seelah.dead": "seelah.returned"}
        s["SeatWomen"] = {"seelah": dict(Relationship="pair", UnavailableFlags=["seelah.dead"]),
                          "galfrey": dict(Relationship="pair", UnavailableFlags=["galfrey.dead"])}
        del s["Relationships"]["seelah"]
        key = guard.availability(s, "seelah", "pair")
        proof = Proof(verify.Model(s))
        earned = AND(lit("chapter_later"), lit("seelah.dead"), lit("seelah.returned"),
                     lit("pair.closed", False), lit("galfrey.dead"), lit("pair.committed", False))
        self.assertTrue(proof.implies(earned, lit(key)))
        self.assertFalse(proof.implies(earned, lit("galfrey.dead", False)))

    def test_native_audience_proves_staging_only_at_its_real_chapter_and_list(self):
        s = fixture("{n}Seelah stands by the door.{/n}")
        # A native witness never supplies an unrelated actor or route life.
        s["Scenes"][0]["AnswerLists"] = ["41dff710486d05d49bbb663f729ddabd"]
        self.assertTrue(run(other_woman, s))

    def test_participant_key_name_alone_cannot_hide_a_live_loss(self):
        s = fixture("{n}Seelah stands beside the fire.{/n}")
        s["Derived"]["crossroute.seelah.available"] = [["ready"]]
        s["Scenes"][0]["Requires"] = ["crossroute.seelah.available"]
        self.assertEqual({f["subject"] for f in run(other_woman, s)}, {"seelah", "seelah:physical"})

    def test_inline_binding_is_preserved_instead_of_requiring_a_visitor_clone(self):
        s = fixture("{n}Seelah raises her mug.{/n}")
        s["Scenes"][0]["NativeReturnCue"] = "native-cue"
        s["Scenes"][0]["Nodes"][0].update(Speaker="Seelah", SpeakerUnit="native-seelah")
        s["Presences"] = {"seelah.presence": dict(Unit="visitor-clone", Area="drezen")}
        guard.integrate(s)
        self.assertNotIn("ContactUnit", s["Scenes"][0])
        self.assertNotIn("AdditionalContactUnits", s["Scenes"][0])
        self.assertEqual(run(other_woman, s), [])


if __name__ == "__main__":
    unittest.main()
