using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Nocticula, Trickster (Writer/handoffs/trickster/nocticula.md): only your shadow (F11) and her brother's voice (F01).
// One block per spec rules test (Trk_Nocticula_*), plus the registered-route edits (silence, G6, NOC-02) and reactions.
internal static class NocticulaTricksterTests
{
    private const string Dead = "noct.dead";
    private const string Fight = "noct.acq.council_fight";
    private const string Alive = "noct.defeated_not_dead";
    private const string PrimedShadow = "nocticula.trickster.primed_shadow";
    private const string Primed = "nocticula.trickster.primed";
    private const string Returned = "nocticula.trickster.returned";
    private const string Declined = "nocticula.trickster.declined";
    private const string Secret = "nocticula.trickster.cost.shade_secret";
    private const string Paid = "nocticula.trickster.cost.shade_paid";
    private const string Refused = "nocticula.trickster.cost.shade_refused";
    private const string Late = "nocticula.trickster.cost.late";
    private const string Kept = "nocticula.trickster.cost.impersonation_kept";
    private const string Threshold = "765173e2a9e535e4cb66f0ec767c13af";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = "2570015799edf594daf2f076f2f975d8", Hour = 5000 };
        state.Flags.UnionWith(flags);
        if (chapter > 1) state.Flags.Add("chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 1000;
        return state;
    }

    private static Snapshot With(Story story, Snapshot state, params string[] flags)
    {
        var next = Program.Copy(state);
        foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour;
        Rules.Complete(story, next);
        return next;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var clue = S("nocticula.trickster.defeated.debrief_clue");
        var shadow = S("nocticula.trickster.defeated.shadow");
        var lateShadow = S("nocticula.trickster.defeated.late_shadow");
        var callIn = S("nocticula.trickster.defeated.call_in");
        var chair = S("nocticula.trickster.defeated.chair");
        var morning = S("nocticula.trickster.defeated.morning");
        var voice = S("nocticula.trickster.palace.brothers_voice");
        var b1 = S("nocticula.trickster.defeated.epilogue");
        var fooledPage = S("nocticula.trickster.defeated.epilogue.fooled");
        var favour = S("nocticula.trickster.defeated.epilogue.favour");
        var stalemate = S("nocticula.trickster.defeated.epilogue.stalemate");
        var unpriced = S("nocticula.trickster.defeated.epilogue.unpriced");
        var unjoked = S("nocticula.trickster.defeated.epilogue.unjoked");
        var epCommit = S("nocticula.trickster.epilogue.commit");
        var epDeclined = S("nocticula.trickster.epilogue.declined");
        var daeran = S("nocticula.trickster.reaction.daeran");
        var nenio = S("nocticula.trickster.reaction.nenio");
        var missingLine = S("noct.acq.the_missing_line");
        var herHand = S("noct.acq.her_hand");
        var devices = new[] { clue, shadow, lateShadow, voice };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));

        // Hooks and shape: the Council debrief, the Threshold projection, her Chapter 5 audience.
        check(clue.AnswerLists.SequenceEqual(new[] { "aff2802d5af0f77408793b489334befc" })
              && clue.NativeReturnCue == "adf1456e429a3d94693417ef7d090d5e" && clue.ContactUnit == null
              && clue.Nodes.Single(n => n.Id == "socoth").SpeakerUnit == "dcd200c627536c449bc8258eada65c9f",
            "The clue left Socothbenoth's debrief.");
        check(shadow.NativeReturnCue == "77216dc2c3770794f93b010659f4aa64" && callIn.NativeReturnCue == "77216dc2c3770794f93b010659f4aa64"
              && chair.NativeReturnCue == "7d07492b12cf5bd4bb1c88113d5831ab"
              && new[] { shadow, callIn, chair }.All(s => s.AnswerLists.SequenceEqual(new[] { Threshold }) && s.Chapters.SequenceEqual(new[] { 6 })),
            "The Threshold beats left her projection's list.");
        check(voice.AnswerLists.SequenceEqual(new[] { "6a5c262473dfe824886bed3eb3eef59d" })
              && voice.NativeReturnCue == "114211469c9ffd149a73f1c853b2776f" && voice.EntryMythic == "PlayerIsTrickster"
              && voice.Relationship == "nocticula.acquisition", "Her brother's voice left the audience's first list.");
        check(lateShadow.Remote && morning.Remote && new[] { clue, shadow, lateShadow, callIn }.All(s => s.TricksterDevice && s.TricksterState == Dead),
            "Device scenes mislabelled.");
        var rel = story.Relationships["nocticula"];
        check(rel.UnavailableOverrides.TryGetValue(Dead, out var over) && over == Alive && rel.TricksterAccess.Count == 1
              && rel.TricksterAccess[Dead].Returned == Returned, "Nocticula relationship patch missing.");
        check(story.Derived.ContainsKey(Alive) && story.Derived.ContainsKey("nocticula.trickster.cost.forgery_kept"), "Derived keys missing.");
        var joke = shadow.Nodes.Where(n => n.Id != "start").SelectMany(n => n.Choices).Where(c => !c.Abort).ToList();
        check(joke.Count == 4 && joke.All(c => c.Mythic == "PlayerIsTrickster" && c.Text.Contains("I killed your shadow")), "The joke lost its [Trickster] answer.");
        var terms = callIn.Nodes.Single(n => n.Id == "terms").Choices.Single();
        var termsLate = callIn.Nodes.Single(n => n.Id == "terms_late").Choices.Single();
        check(terms.Alignment?.Direction == "Evil" && terms.Alignment.Value == 1 && termsLate.Alignment?.Value == 2
              && terms.NativeNext == "90cfcb7b1c0bacc43b27043074f21301", "The favour does not mark the soul.");

        // Trk_Nocticula_Defeated: the joke at Threshold, then the call-in.
        var defeated = World(story, 6, "trickster", "trickster.ever", Dead, Fight);
        check(defeated.Has(Alive), "Defeated at the Council is not read as alive.");
        check(Rules.Available(story, shadow, defeated) && !Rules.Available(story, voice, defeated)
              && !Rules.Available(story, S("noct.ending_death"), With(story, defeated, "noct.complete")),
            "Trk_Nocticula_Defeated: availability.");
        var joked = Program.Walk(shadow, defeated).Where(r => r.Has(shadow.Id)).ToList();
        check(joked.Count == 1 && joked[0].Has(Primed) && joked[0].Has(Secret) && joked[0].Has("noct.started"), "Trk_Nocticula_Defeated: flags.");
        check(Rules.Available(story, callIn, joked[0]) && !Rules.Available(story, lateShadow, With(story, joked[0], "noct.threshold_met")),
            "Trk_Nocticula_Defeated: no call-in after the joke.");
        var pages = new HashSet<string>();
        Program.Walk(shadow, defeated, (page, _) => pages.Add(page));
        check(pages.Contains("base") && !pages.Contains("seen"), "The base variant is not shown without the clue.");

        // Trk_Nocticula_DebriefClue / _AfterThreshold.
        var council = World(story, 5, "trickster", "trickster.ever", Dead, Fight);
        check(Rules.Available(story, clue, council), "Trk_Nocticula_DebriefClue: clue unavailable.");
        var clued = Program.Walk(clue, council);
        check(clued.Any(r => r.Has(PrimedShadow)) && clued.Any(r => !r.Has(PrimedShadow) && !r.Has(clue.Id))
              && !Rules.Available(story, clue, clued.First(r => r.Has(PrimedShadow))), "Trk_Nocticula_DebriefClue: flags.");
        check(!Rules.Available(story, clue, With(story, council, "noct.threshold_met")), "Trk_Nocticula_DebriefClueAfterThreshold failed.");

        // Trk_Nocticula_DefeatedFooled: the clue wins over the dress; the dress over the base.
        var fooled = World(story, 6, "trickster", "trickster.ever", Dead, Fight, "noct.fooled", PrimedShadow);
        pages.Clear();
        var fooledJoke = Program.Walk(shadow, fooled, (page, _) => pages.Add(page)).Where(r => r.Has(shadow.Id)).ToList();
        check(fooledJoke.Count == 1 && fooledJoke[0].Has(Primed) && pages.Contains("seen") && !pages.Contains("dress"), "Trk_Nocticula_DefeatedFooled failed.");
        pages.Clear();
        Program.Walk(shadow, World(story, 6, "trickster", "trickster.ever", Dead, Fight, "noct.fooled"), (page, _) => pages.Add(page));
        check(pages.Contains("dress") && !pages.Contains("base"), "The dress variant is missing.");

        // Trk_Nocticula_DefeatedLate: the stray shadow on the tent wall, worse terms.
        var missed = World(story, 6, "trickster", "trickster.ever", Dead, Fight, "noct.threshold_met");
        check(Rules.Available(story, lateShadow, missed), "Trk_Nocticula_DefeatedLate: late shadow unavailable.");
        var pinned = Program.Walk(lateShadow, missed).Where(r => r.Has(lateShadow.Id)).ToList();
        check(pinned.Count == 1 && pinned[0].Has(Primed) && pinned[0].Has(Late) && pinned[0].Has(Secret), "Trk_Nocticula_DefeatedLate: flags.");
        check(Rules.Available(story, callIn, pinned[0]) && !Rules.Available(story, lateShadow, pinned[0]), "Trk_Nocticula_DefeatedLate: no call-in.");
        check(lateShadow.Nodes[0].Choices[0].Mythic == "PlayerIsTrickster", "The boot on her shadow is not a [Trickster] answer.");

        // Trk_Nocticula_CallInLate: only the Evil 2 "Agreed." is offered.
        var lateCall = World(story, 6, "trickster.ever", Dead, Fight, Primed, Late);
        var lateOutcomes = Program.Walk(callIn, lateCall).Where(r => r.Has(callIn.Id)).ToList();
        pages.Clear();
        Program.Walk(callIn, lateCall, (page, _) => pages.Add(page));
        check(pages.Contains("terms_late") && !pages.Contains("terms") && lateOutcomes.Any(r => r.Has(Paid) && r.Has(Returned)),
            "Trk_Nocticula_CallInLate failed.");
        var paid = lateOutcomes.First(r => r.Has(Paid));
        check(Rules.Available(story, chair, paid) && Rules.Available(story, b1, paid) && Rules.Available(story, favour, paid)
              && !Rules.Available(story, stalemate, paid), "Trk_Nocticula_CallInLate: continuations.");

        // Trk_Nocticula_CallInRefused: mutual blackmail.
        var onTime = World(story, 6, "trickster.ever", Dead, Fight, Primed);
        var refused = Program.Walk(callIn, onTime).Single(r => r.Has(Refused));
        check(refused.Has(Returned) && Rules.Available(story, stalemate, refused) && !Rules.Available(story, favour, refused),
            "Trk_Nocticula_CallInRefused failed.");
        check(Program.Walk(callIn, onTime).Any(r => !r.Has(callIn.Id) && !r.Has(Returned)), "The call-in cannot be left for later.");

        // Trk_Nocticula_Commit / _CommitDeclined: her test, her yes, her no.
        var returned = World(story, 6, "trickster.ever", Dead, Fight, Returned, Paid);
        check(Rules.Available(story, chair, returned) && Rules.Available(story, epCommit, returned), "Trk_Nocticula_Commit: availability.");
        var chaired = Program.Walk(chair, returned);
        var yes = chaired.Where(r => r.Has("noct.complete")).ToList();
        var no = chaired.Where(r => r.Has(Declined)).ToList();
        check(yes.Count == 2 && no.Count == 2 && no.All(r => !r.Has("noct.complete")), "Her yes and her no are not on both verdicts.");
        check(!Any(yes[0], chair, epCommit, epDeclined) && Rules.Available(story, morning, yes[0]), "Trk_Nocticula_Commit: after the yes.");
        check(Rules.Available(story, epDeclined, no[0]) && !Any(no[0], chair, epCommit), "Trk_Nocticula_CommitDeclined failed.");
        pages.Clear();
        Program.Walk(chair, returned, (page, _) => pages.Add(page));
        check(pages.Contains("threshold") && pages.Contains("refusal"), "The chair lost its threshold or its refusal.");
        foreach (var id in new[] { "noct.ending_sacrifice", "noct.ending_ascent", "noct.ending_changed" })
            check(!Rules.Available(story, S(id), With(story, yes[0], "sacrifice", "ascended", "inhuman")), "A harbor ending plays after the chair: " + id);

        // Trk_Nocticula_FavourUnderLastCall, _Unpriced, _Unjoked.
        // Trk_Nocticula_FavourUnderLastCall waits for the finale (no lastcall.active producer yet; PROGRESS backlog).
        var primedOnly = World(story, 6, "trickster.ever", Dead, Fight, Primed);
        check(Rules.Available(story, unpriced, primedOnly) && !Rules.Available(story, unjoked, primedOnly), "Trk_Nocticula_Unpriced failed.");
        var neither = World(story, 6, "trickster.ever", Dead, Fight);
        check(Rules.Available(story, unjoked, neither) && !Any(neither, unpriced, b1, fooledPage), "Trk_Nocticula_Unjoked failed.");

        // Trk_Nocticula_SilentAfterCouncil: no harbor dream, no letter, between the Council and Threshold.
        var silent = World(story, 5, "trickster", "trickster.ever", Dead, Fight, "noct.parent_active", "noct.parent_agreement_seen",
            "noct.gift", "noct.acq.requested", "noct.acq.seal_received", "noct.acq.council_disclosed");
        check(!Rules.Available(story, S("noct.unlit_quay"), silent) && !Rules.Available(story, missingLine, With(story, silent)),
            "Trk_Nocticula_SilentAfterCouncil failed.");
        foreach (var s in story.Scenes.Where(s => (s.Relationship == "nocticula" || s.Relationship == "nocticula.acquisition")
                                                  && !s.Id.StartsWith("nocticula.trickster.", StringComparison.Ordinal)
                                                  && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Forbids.Contains(Dead)))
            check(s.Forbids.Contains(Fight) && s.ForbidOverrides.TryGetValue(Fight, out var f) && f == Returned
                  && s.ForbidOverrides.TryGetValue(Dead, out var d) && d == Alive, "Ledger row 2 missing on " + s.Id);

        // Trk_Nocticula_BrothersVoice / _Mocked / _TooLate.
        var palace = World(story, 5, "trickster", "trickster.ever", "closets.known", "noct.acq.audience_started");
        check(Rules.Available(story, voice, palace) && !Rules.Available(story, shadow, palace), "Trk_Nocticula_BrothersVoice: availability.");
        var voices = Program.Walk(voice, palace).Where(r => r.Has(voice.Id)).ToList();
        check(voices.Count == 2 && voices.All(r => r.Has("nocticula.trickster.impersonated") && r.Has(Kept))
              && voices.Count(r => r.Has("nocticula.trickster.cost.mocked")) == 1, "Trk_Nocticula_BrothersVoiceMocked failed.");
        check(voice.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null).All(c => c.NativeNext == "20451daada07f744b9d7f3e14a37a864")
              && voice.Nodes.Single(n => n.Id == "bookmark").Choices.Single().Alignment?.Direction == "Chaotic",
            "The voice does not hand back to her native 'You? But I could've sworn...'");
        check(!Rules.Available(story, voice, With(story, palace, "noct.acq.audience_question"))
              && !Rules.Available(story, voice, World(story, 5, "trickster", "noct.acq.audience_started")), "Trk_Nocticula_BrothersVoiceTooLate failed.");
        // The registered audience continues from Cue_0006, and the channel reaches the agreement (NOC-02).
        var afterVoice = With(story, voices[0], "noct.acq.audience_question", "noct.acq.council_disclosed");
        check(Rules.Available(story, S("noct.acq.audience_missed"), afterVoice), "The registered audience does not follow the voice.");
        var scentPages = new HashSet<string>();
        var ready = With(story, afterVoice, "noct.acq.requested", "noct.acq.seal_received", "noct.acq.question_sent", "noct.acq.channel_slow");
        ready.Hour += herHand.DelayHours + 1000;
        check(Rules.Available(story, herHand, ready), "Her hand is unavailable after the voice.");
        Program.Walk(herHand, ready, (page, _) => scentPages.Add(page));
        check(scentPages.Contains("scent_slow_account"), "Her first words through the seal forget the voice.");

        // Trk_Nocticula_AudienceAsked_* (NOC-02): any native answer earns the channel.
        foreach (var answer in new[] { "noct.acq.council_disclosed", "noct.acq.shamira_permission", "noct.acq.shamira_reported", "noct.acq.amused" })
        {
            var asked = World(story, 5, "trickster", "trickster.ever", "noct.acq.audience_question", answer,
                              "noct.acq.requested", "noct.acq.seal_received");
            asked.Hour += missingLine.DelayHours + 1000;
            check(Rules.Available(story, missingLine, asked) && !Rules.Available(story, voice, asked), "Trk_Nocticula_AudienceAsked failed: " + answer);
        }
        var noAnswer = World(story, 5, "trickster", "noct.acq.audience_question", "noct.acq.requested", "noct.acq.seal_received",
                             "noct.socoth_plan_exposed");
        noAnswer.Hour += missingLine.DelayHours + 1000;
        check(!Rules.Available(story, missingLine, noAnswer), "The channel opens with no answer at the audience.");

        // Trk_Nocticula_ParentContract / _AlliedVsCouncil: no device.
        var parent = World(story, 5, "trickster", "trickster.ever", "noct.parent_active", "noct.parent_agreement_seen", "noct.gift");
        check(Rules.Available(story, S("noct.unlit_quay"), parent) && !Any(parent, devices), "Trk_Nocticula_ParentContract failed.");
        var allied = World(story, 6, "trickster", "trickster.ever", "council.fought_nocta_allied", "noct.threshold_met");
        check(!Any(allied, devices) && !Any(allied, callIn, chair), "Trk_Nocticula_AlliedNoThresholdDevice failed.");

        // Trk_Nocticula_PathFailed: no trick without the live path; payoffs of a trick taken still run.
        var failed = World(story, 6, "trickster.was", "trickster.failed", Dead, Fight, "noct.threshold_met");
        check(failed.Has("trickster.ever") && !Any(failed, devices), "Trk_Nocticula_PathFailed failed.");
        check(!Rules.Available(story, clue, World(story, 5, "trickster.was", "trickster.failed", Dead, Fight)), "The clue without the live path.");

        // Reactions: exactly Daeran and Nenio.
        check(Rules.Available(story, daeran, With(story, World(story, 5, "trickster.ever"), "nocticula.trickster.impersonated"))
              && !Rules.Available(story, daeran, World(story, 5, "trickster.ever", "nocticula.trickster.impersonated", "daeran.dead")),
            "Daeran's reaction.");
        check(Rules.Available(story, nenio, joked[0]) && !Rules.Available(story, nenio, With(story, joked[0], "nenio.dissolved")),
            "Nenio's reaction.");
        check(story.Scenes.Count(s => s.Reaction && s.Id.StartsWith("nocticula.trickster.", StringComparison.Ordinal)) == 2, "Reactor count.");
        check(new[] { b1, fooledPage, favour, stalemate, unpriced, unjoked, epCommit, epDeclined }
                  .All(s => s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Alignment == null)),
            "An epilogue page sets a flag.");
        check(epCommit.Nodes[0].Choices.Count == 2, "The late commit gives the Commander no choice.");
    }
}
