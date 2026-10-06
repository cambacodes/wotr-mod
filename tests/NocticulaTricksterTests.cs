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
        // eng7-l12: Chapter 6 shadow/chair encounters take place at Threshold.
        var state = new Snapshot { Chapter = chapter, Area = chapter == 6 ? "10c4b0e2af186ba46ab4d238d00a40a8" : "2570015799edf594daf2f076f2f975d8", Hour = 5000 };
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
        check(joke.Count == 4 && joke.All(c => c.Mythic == "PlayerIsTrickster" && SurfaceIds.Has(SurfaceIds.Of(story, c), "[nocticula.trickster.defeated.shadow/seen/choice/0][nocticula.trickster.defeated.shadow/dress/choice/0][nocticula.trickster.defeated.shadow/voice/choice/0][nocticula.trickster.defeated.shadow/base/choice/0]")), "The joke lost its [Trickster] answer.");
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
        var lateCall = World(story, 6, "trickster", "trickster.ever", Dead, Fight, Primed, Late);
        var lateOutcomes = Program.Walk(callIn, lateCall).Where(r => r.Has(callIn.Id)).ToList();
        pages.Clear();
        Program.Walk(callIn, lateCall, (page, _) => pages.Add(page));
        check(pages.Contains("terms_late") && !pages.Contains("terms") && lateOutcomes.Any(r => r.Has(Paid) && r.Has(Returned)),
            "Trk_Nocticula_CallInLate failed.");
        var paid = lateOutcomes.First(r => r.Has(Paid));
        // Ledger row 11: the favour page is a relationship page (committed); a debt outside the romance has its own page.
        check(Rules.Available(story, chair, paid) && Rules.Available(story, b1, paid) && !Rules.Available(story, favour, paid)
              && Rules.Available(story, favour, With(story, paid, "noct.complete")) && !Rules.Available(story, S("nocticula.trickster.defeated.epilogue.debt"), paid) && Rules.Available(story, S("nocticula.trickster.defeated.epilogue.debt"), With(story, paid, Declined))
              && !Rules.Available(story, S("nocticula.trickster.defeated.epilogue.debt"), With(story, paid, "noct.complete"))
              && !Rules.Available(story, stalemate, paid), "Trk_Nocticula_CallInLate: continuations.");

        // Trk_Nocticula_CallInRefused: mutual blackmail.
        var onTime = World(story, 6, "trickster", "trickster.ever", Dead, Fight, Primed);
        var refused = Program.Walk(callIn, onTime).Single(r => r.Has(Refused));
        check(refused.Has(Returned) && !Rules.Available(story, stalemate, refused) && Rules.Available(story, stalemate, With(story, refused, "noct.complete")) && !Rules.Available(story, favour, refused),
            "Trk_Nocticula_CallInRefused failed.");
        check(Program.Walk(callIn, onTime).Any(r => !r.Has(callIn.Id) && !r.Has(Returned)), "The call-in cannot be left for later.");

        // Trk_Nocticula_Commit / _CommitDeclined: her test, her yes, her no.
        var unnegotiated = World(story, 6, "trickster", "trickster.ever", Dead, Fight, Returned, Paid);
        check(!Rules.Available(story, epCommit, unnegotiated), "A late romance bypasses the Shamira terms.");
        var stanceOutcomes = Program.Walk(chair, unnegotiated);
        check(stanceOutcomes.Where(r => r.Has("noct.complete")).All(r => r.Has("nocticula.partner_terms")
              && new[] { "share", "exclusive", "secret" }.Count(s => r.Has("nocticula.partner_stance." + s)) == 1)
              && stanceOutcomes.Any(r => r.Has("nocticula.partner_stance.share") && r.Has("noct.complete"))
              && stanceOutcomes.Any(r => r.Has("nocticula.partner_stance.secret") && r.Has("noct.complete"))
              && stanceOutcomes.Any(r => r.Has("nocticula.partner_stance.exclusive") && r.Has("noct.closed") && !r.Has("noct.complete")),
              "Nocticula partner stances lost an accepted or refused branch.");
        var returned = With(story, unnegotiated, "nocticula.partner_terms", "nocticula.partner_stance.share");
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
        // Sol BEL: her reason for wanting the Commander close is what she actually saw on this road. Only a Commander who
        // looked at the floor (the debrief clue) hears about the floor.
        foreach (var (road, flag) in new (string, string?)[] { ("why_floor", PrimedShadow), ("why_late", Late), ("why_dress", "noct.fooled"),
                                                               ("why_voice", "nocticula.trickster.cost.mocked"), ("why_base", null) })
        {
            var roadWorld = flag == null ? returned : With(story, returned, flag);
            var seen = new HashSet<string>();
            Program.Walk(chair, roadWorld, (page, _) => seen.Add(page));
            check(seen.Contains(road) && seen.Count(p => p.StartsWith("why_", StringComparison.Ordinal)) == 1,
                "The chair's reason on the " + road + " road is not its own (" + string.Join(",", seen.Where(p => p.StartsWith("why_", StringComparison.Ordinal))) + ").");
        }
        foreach (var id in new[] { "noct.ending_sacrifice", "noct.ending_ascent", "noct.ending_changed" })
            check(!Rules.Available(story, S(id), With(story, yes[0], "sacrifice", "ascended", "inhuman")), "A harbor ending plays after the chair: " + id);

        // Trk_Nocticula_FavourUnderLastCall, _Unpriced, _Unjoked.
        // Trk_Nocticula_FavourUnderLastCall waits for the finale (no lastcall.active producer yet; PROGRESS backlog).
        var primedOnly = World(story, 6, "trickster", "trickster.ever", Dead, Fight, Primed);
        check(Rules.Available(story, unpriced, primedOnly) && !Rules.Available(story, unjoked, primedOnly), "Trk_Nocticula_Unpriced failed.");
        var neither = World(story, 6, "trickster", "trickster.ever", Dead, Fight);
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
        check(Rules.Available(story, daeran, With(story, World(story, 5, "trickster", "trickster.ever"), "nocticula.trickster.impersonated"))
              && !Rules.Available(story, daeran, World(story, 5, "trickster", "trickster.ever", "nocticula.trickster.impersonated", "daeran.dead")),
            "Daeran's reaction.");
        check(Rules.Available(story, nenio, joked[0]) && !Rules.Available(story, nenio, With(story, joked[0], "nenio.dissolved")),
            "Nenio's reaction.");
        // Sol INT: a Nenio who died, was killed, sent away or kicked out and then came back on her own Trickster road reacts;
        // one who is gone does not; dissolved stays blocking (her producer never reverses it).
        foreach (var gone in new[] { "nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out" })
            check(!Rules.Available(story, nenio, With(story, joked[0], gone))
                  && Rules.Available(story, nenio, With(story, joked[0], gone, "nenio.trickster.returned",
                      gone == "nenio.dead" ? "nenio.trickster.cost.recreated" : gone == "nenio.killed_by_commander" ? "nenio.trickster.cost.unremembered" : "nenio.trickster.cost.demoted")), // eng8-q8a: matching paid receipt fixture
                "Nenio's reaction ignores her return after " + gone + ".");
        check(!Rules.Available(story, nenio, With(story, joked[0], "nenio.dissolved", "nenio.trickster.returned")),
            "Nenio's reaction plays for a dissolved Nenio.");

        // Sol INT: both Nocticula relationships share one post-bag slot (the spec's shared rotation key).
        check(Rules.RotationKey(story, "nocticula") == "nocticula" && Rules.RotationKey(story, "nocticula.acquisition") == "nocticula",
            "Nocticula's two relationships do not share the rotation key.");
        var bothOpen = story.Scenes.Where(s => (s.Relationship == "nocticula" || s.Relationship == "nocticula.acquisition") && Rules.IsMailbagLetter(s)).ToList();
        var anyState = World(story, 5, "trickster", "trickster.ever");
        check(Rules.MailbagArrivals(story, anyState).Count(s => Rules.RotationKey(story, s.Relationship) == "nocticula") <= 1 && bothOpen.Count > 0,
            "Two Nocticula letters can arrive at one rest.");

        // Sol INT/HOW (ledger row 11): Nocticula smells Shamira in the Commander only when she actually came in through the
        // door held open at the briefing; never on a bare native kill, never after the late road (the audience is over by
        // then), and never once she was refused, thrown out or woke in a body.
        var courtShamira = S("nocticula.trickster.court.shamira");
        var killedOnly = World(story, 5, "trickster", "trickster.ever", "shamira.killed");
        var primedKill = With(story, killedOnly, "shamira.trickster.primed");
        check(!Rules.Available(story, courtShamira, killedOnly), "Court: a native kill without the door held open puts Shamira in the Commander's head.");
        check(Rules.Available(story, courtShamira, primedKill), "Court: the prepared capture does not reach Nocticula's audience.");
        check(!Rules.Available(story, courtShamira, With(story, killedOnly, "shamira.trickster.made_room", "shamira.trickster.returned")),
            "Court: the late capture (made room at the first rest) is smelled at an audience that came before it.");
        check(!Rules.Available(story, courtShamira, With(story, killedOnly, "shamira.trickster.declined", "shamira.closed")),
            "Court: a Shamira let go under is greeted.");
        foreach (var gone in new[] { "shamira.trickster.declined", "shamira.trickster.cast_out", "shamira.trickster.embodied" })
            check(!Rules.Available(story, courtShamira, With(story, primedKill, gone)), "Court: plays after " + gone + ".");
        check(story.Scenes.Count(s => s.Reaction && s.Id.StartsWith("nocticula.trickster.", StringComparison.Ordinal)) == 2, "Reactor count.");
        check(new[] { b1, fooledPage, favour, stalemate, unpriced, unjoked, epCommit, epDeclined }
                  .All(s => s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Alignment == null)),
            "An epilogue page sets a flag.");
        check(epCommit.Nodes[0].Choices.Count == 7 && epCommit.Nodes.Single(n => n.Id == "yes_page").Choices.Count == 3,
            "The late commit gives the Commander no choice, or no refusal.");
        // Sol BEL: the late commit carries her test and this road's reason before her yes, and the Commander may refuse.
        foreach (var (road, flag) in new (string, string?)[] { ("m_floor", PrimedShadow), ("m_late", Late), ("m_base", null) })
        {
            var seen = new HashSet<string>();
            var w6 = World(story, 6, "trickster", "trickster.ever", Returned, Paid, "nocticula.partner_terms", "nocticula.partner_stance.share");
            Program.Walk(epCommit, flag == null ? w6 : With(story, w6, flag), (id, _) => seen.Add(id));
            check(seen.Contains(road) && seen.Count(x => x.StartsWith("m_", StringComparison.Ordinal)) == 1 && seen.Contains("refused_page"),
                "The late commit's reason on the " + road + " road is not its own, or there is no refusal.");
        }
        // Sol INT/COX: pages of a life after the war only for a Commander who has one; the harbor's permanent loss never over one.
        var dead6 = World(story, 6, "trickster", "trickster.ever", Returned, Paid, Primed, "sacrifice");
        var back6 = With(story, dead6, "trickster.commander_back");
        check(!Rules.Available(story, b1, dead6) && Rules.Available(story, b1, back6) && !Rules.Available(story, epCommit, dead6)
              && Rules.Available(story, S("nocticula.trickster.defeated.epilogue.unanswered"), dead6)
              && !Rules.Available(story, S("nocticula.trickster.defeated.epilogue.unanswered"), back6),
            "Nocticula's pages ignore the Commander's death or survival.");
        var harborLoss = World(story, 6, "trickster", "trickster.ever", "noct.complete", "sacrifice");
        check(Rules.Available(story, S("noct.ending_sacrifice"), harborLoss) && !Rules.Available(story, S("noct.ending_sacrifice"), With(story, harborLoss, "trickster.commander_back"))
              && story.Scenes.Where(s => s.Id.StartsWith("noct.ending_sacrifice", StringComparison.Ordinal)).All(s => s.Forbids.Contains("trickster.commander_back"))
              && Rules.Available(story, S("noct.ending_company"), With(story, harborLoss, "noct.chosen_company", "trickster.commander_back")),
            "The harbor's sacrifice ending plays over a Commander who came back, or the living ending does not.");
        // Sol COX: on the late road (one Chapter 6 rest) the morning after is inside the chair; the remote morning is not needed.
        var lateChair = World(story, 6, "trickster", "trickster.ever", Dead, Fight, Returned, Paid, Late);
        var lateSeen = new HashSet<string>(); Program.Walk(chair, lateChair, (id, _) => lateSeen.Add(id));
        check(lateSeen.Contains("morning_late_paid") && !Rules.Available(story, morning, With(story, lateChair, "nocticula.trickster.said_yes")),
            "The late road needs a second Chapter 6 rest for the morning, or her refusal waits on Areelu's death.");
        // Ledger 05 row 11: the fourth court (Horzalah), Nocticula's read of the Guild's box.
        var courtH = S("nocticula.trickster.court.horzalah");
        var hWorld = World(story, 6, "trickster", "trickster.ever", "horzalah.trickster.returned");
        check(Rules.Available(story, courtH, hWorld) && !Rules.Available(story, courtH, World(story, 6, "trickster", "trickster.ever"))
              && !Rules.Available(story, courtH, With(story, hWorld, Fight)) && Rules.Available(story, courtH, With(story, hWorld, Fight, Returned))
              && courtH.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).All(f => f.StartsWith("nocticula.", StringComparison.Ordinal)),
            "Nocticula's Horzalah court is missing, speaks between the Council and Threshold, or touches Horzalah's flags.");

        // Trk_Nocticula_CourtVellexiaKept / court variants (ledger row 11): Nocticula learns of Vellexia's season at Threshold.
        var court = S("nocticula.trickster.court.vellexia");
        var mirror = S("nocticula.trickster.defeated.epilogue.mirror");
        var mirrorKept = S("nocticula.trickster.defeated.epilogue.mirror_kept");
        const string SecretV = "nocticula.trickster.secret_known.vellexia";
        check(court.AnswerLists.SequenceEqual(new[] { Threshold }) && court.NativeReturnCue == "c10ef2b50ade65f42bbaa0cdfa61b7f9"
              && court.Chapters.SequenceEqual(new[] { 6 }) && court.ForbidOverrides.TryGetValue(Fight, out var courtOver) && courtOver == Returned,
            "The Vellexia court scene left her projection's list.");
        var courtSeen = new Dictionary<string, string> {
            ["vellexia.trickster.kept_as_mirror"] = "kept", ["vellexia.trickster.cost.diminished"] = "diminished",
            ["vellexia.trickster.unmirrored"] = "furniture" };
        foreach (var (outcome, node) in courtSeen)
        {
            var w = World(story, 6, "trickster", "trickster.ever", "vellexia.trickster.presumed_dead", outcome);
            check(Rules.Available(story, court, w), "Trk_Nocticula_CourtVellexia: unavailable with " + outcome);
            pages.Clear();
            var told = Program.Walk(court, w, (page, _) => pages.Add(page)).Where(r => r.Has(court.Id)).ToList();
            check(pages.Contains(node) && pages.Count(p => p != "start") == 1 && told.Count == 1 && told[0].Has(SecretV)
                  && !Rules.Available(story, court, told[0]), "Trk_Nocticula_CourtVellexia: variant " + node);
            check(Rules.Available(story, outcome.EndsWith("kept_as_mirror") ? mirrorKept : mirror, told[0])
                  && !Rules.Available(story, outcome.EndsWith("kept_as_mirror") ? mirror : mirrorKept, told[0]),
                "Trk_Nocticula_CourtVellexia: the wrong mirror page for " + outcome);
        }
        check(!Rules.Available(story, court, World(story, 6, "trickster", "trickster.ever")), "The court scene without Vellexia's season.");
        var hidden = World(story, 6, "trickster", "trickster.ever", Dead, Fight, "vellexia.trickster.presumed_dead", "vellexia.trickster.unmirrored");
        check(!Rules.Available(story, court, hidden) && Rules.Available(story, court, With(story, hidden, Primed, Returned)),
            "The court scene speaks before the Threshold call-in.");
        check(new[] { mirror, mirrorKept }.All(s => s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0 && c.Alignment == null)),
            "A mirror page sets a flag.");
        // The favour is visible the morning after: Daeran reads the unnamed debt when she was paid and he is present.
        var morningPaid = World(story, 6, "trickster", "trickster.ever", "nocticula.trickster.said_yes", Paid);
        pages.Clear();
        Program.Walk(morning, morningPaid, (page, _) => pages.Add(page));
        check(pages.Contains("daeran"), "The morning after hides the unnamed favour from Daeran.");
        foreach (var gone in new[] { "daeran.dead", "daeran.kicked_out" })
        {
            pages.Clear();
            var outs = Program.Walk(morning, With(story, morningPaid, gone), (page, _) => pages.Add(page));
            check(!pages.Contains("daeran") && outs.Any(r => r.Has(morning.Id)), "The morning after strands or shows an absent Daeran: " + gone);
        }
        pages.Clear();
        Program.Walk(morning, World(story, 6, "trickster", "trickster.ever", "nocticula.trickster.said_yes", Refused), (page, _) => pages.Add(page));
        check(!pages.Contains("daeran") && !pages.Contains("note_paid") && !pages.Contains("note_paid_alone"), "Daeran or the note reads a favour that was refused.");
        check(morning.Nodes[0].Choices[0].Next == null,
            "The morning's choice 0 moved (save slot).");
        var order = story.Scenes.Select(s => s.Id).ToList();
        check(order.IndexOf(mirror.Id) < order.IndexOf(mirrorKept.Id) && order.IndexOf(mirrorKept.Id) < order.IndexOf(favour.Id),
            "The mirror pages are out of sibling order (b6, b7 before b8).");
    }
}
