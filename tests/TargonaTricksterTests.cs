using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Targona, Trickster (Writer/handoffs/trickster/targona.md): spend it again, unnoticed (F16). Lariel's light, the part of his
// sword that entered the Commander in Kenabres, used without being spent: the blow that kills her in Areelu's laboratory
// lands with nothing left to spend (killed_in_lab), or the infirmary's last wand never runs down (freed_in_heaven).
// One block per spec rules test (Trk_Targona_*), plus the hooks, the presence, the night, the epilogues and the reactions.
internal static class TargonaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "81297c673b63b60448ef88a10db6bc78";
    private const string Quartermaster = "a380d926e92f70e429681eb9654478f9";
    private const string LabList = "2a75fbc8e86fd514e82117c99fc9e528";
    private const string P = "targona.trickster.";
    private const string Committed = "targona.committed";
    private const string Closed = "targona.closed";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (chapter == 3 || chapter == 5) state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var setup = S(P + "dead.setup");
        var lateLight = S(P + "dead.late_light");
        var oneSoul = S(P + "dead.one_soul");
        var furlough = S(P + "dead.furlough");
        var second = S(P + "dead.second_asking");
        var spent = S(P + "free.spent_light");
        var freeFurlough = S(P + "free.furlough");
        var ward = S(P + "after.ward");
        var quiet = S(P + "after.quiet_ward");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");
        var epFurlough = S(P + "epilogue.furlough");
        Snapshot After(Scene scene, Snapshot w, string node, int choice)
        {
            var target = scene.Nodes.Single(n => n.Id == node).Choices[choice];
            var hit = Program.Walk(scene, w).FirstOrDefault(o => target.Set.All(o.Has));
            check(hit != null && target.Set.Length > 0, "No outcome through " + scene.Id + "/" + node + "/" + choice);
            return hit ?? w;
        }
        bool Reaches(Snapshot w, string flag, int depth = 6)
        {
            if (w.Has(flag)) return true;
            if (depth == 0) return false;
            var later = Later(story, w, 100);
            foreach (var s in story.Scenes.Where(s => s.Relationship == "targona" && !s.Reaction
                                                   && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                                                   && Rules.Available(story, s, later)))
                foreach (var outcome in Program.Walk(s, later))
                    if (Reaches(outcome, flag, depth - 1)) return true;
            return false;
        }

        // Hooks, relationship patch and the presence.
        check(setup.AnswerLists.SequenceEqual(new[] { LabList }) && setup.NativeReturnCue == null && setup.MinChapter == 3
              && setup.MaxChapter == 3 && setup.EntryMythic == "PlayerIsTrickster" && setup.Forbids.Contains("targona.dead_lab")
              && setup.Forbids.Contains("targona.free") && setup.Forbids.Contains("targona.condemned"),
            "The laboratory primer left her list, became inline, or no longer comes before the blow.");
        foreach (var s in new[] { furlough, second, freeFurlough, ward, quiet })
            check(s.InteractionHub == "targona.presence" && s.ContactUnit == Unit && Rules.IsPresenceHubScene(s)
                  && s.Chapters.SequenceEqual(new[] { 3, 5 }) && !Rules.IsRemote(s), "An in-person beat left the infirmary: " + s.Id);
        foreach (var s in new[] { lateLight, oneSoul, spent })
            check(Rules.IsRemote(s), "A letter is physical: " + s.Id);
        check(lateLight.Chapters.SequenceEqual(new[] { 3 }) && oneSoul.Chapters.SequenceEqual(new[] { 3, 5 }) && oneSoul.DelayHours == 72,
            "The late light or the one-soul payoff has the wrong chapters or delay.");
        foreach (var s in new[] { lateLight, oneSoul })
            check(s.TricksterDevice && s.TricksterState == "targona.dead_lab", "A killed-state scene is not an ER-2 device: " + s.Id);
        var rel = story.Relationships["targona"];
        check(rel.UnavailableOverrides["targona.dead_lab"] == P + "returned" && rel.TricksterAccess.Count == 2
              && rel.TricksterAccess["targona.dead_lab"].Device == P + "dead.one_soul"
              && rel.TricksterAccess["freed_in_heaven"].Device == P + "free.spent_light"
              && rel.CommittedFlag == Committed && rel.ClosedFlag == Closed, "Targona's relationship patch is wrong.");
        check(story.Presences.TryGetValue("targona.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Quartermaster && presence.At.Side == "behind" && presence.Dialog == "hub"
              && presence.Forbids.Contains(Closed) && presence.MinChapter == 3 && presence.MaxChapter == 5
              && presence.Requires.Contains(P + "in_drezen"), "Her presence among the cots is missing or malformed.");
        check(!story.Presences.Any(p => p.Key != "targona.presence" && p.Value.At?.NearUnit == Quartermaster && p.Value.At.Side == "behind"),
            "Targona's copy would stand where another presence stands behind the quartermaster.");

        // Trk_Targona_Setup: the primer, before the blow.
        var lab = World(story, 3, "trickster", "trickster.ever");
        check(Rules.Available(story, setup, lab) && !Rules.Available(story, lateLight, lab) && !Rules.Available(story, oneSoul, lab),
            "Trk_Targona_Setup: availability.");
        var joke = setup.Nodes.Single(n => n.Id == "start").Choices[0];
        check(joke.Mythic == "PlayerIsTrickster" && joke.Alignment?.Direction == "Chaotic" && joke.Alignment.Value == 1
              && joke.Text.StartsWith("[Spend it again, quietly]", StringComparison.Ordinal), "The primer lost its joke or its cost.");
        var primed = After(setup, lab, "scroll", 0);
        check(setup.Nodes.Single(n => n.Id == "scroll").Text.Contains("breath of life", StringComparison.Ordinal)
              && setup.Nodes.Single(n => n.Id == "scroll").Text.Contains("two rounds", StringComparison.Ordinal),
            "The primer does not show the wand, or breath of life's two-round limit.");
        check(primed.Has(P + "primed"), "Trk_Targona_Setup: flags.");
        check(Reaches(World(story, 3, "trickster", "trickster.ever", "targona.dead_lab", P + "primed", P + "told_in_lab"), Committed),
            "Trk_Targona_Setup: the commit is unreachable after the blow.");
        // Both native outcomes after the primer: [Attack] (TargonaIsWasKilledInAreeluLab) leads to the scroll's payoff;
        // [Destroy the barrier] (TargonaIsFreeInAreeluLab) leaves the primer unused and opens the freed state's wand night.
        check(!Rules.Available(story, setup, primed), "The primer can be taken twice.");
        var primedKilled = Program.Copy(primed); primedKilled.Flags.Add("targona.dead_lab");
        check(Rules.Available(story, oneSoul, Later(story, primedKilled, 72)) && !Rules.Available(story, lateLight, primedKilled),
            "After the primer, the native kill does not lead to the scroll's payoff.");
        var primedFreed = Program.Copy(primed); primedFreed.Flags.Add("targona.free");
        check(Rules.Available(story, spent, Later(story, primedFreed, 1)) && !Rules.Available(story, oneSoul, Later(story, primedFreed, 72)),
            "After the primer, the native rescue does not open the freed state.");
        foreach (var gone in new[] { "targona.dead_lab", "targona.free", "targona.condemned" })
            check(!Rules.Available(story, setup, World(story, 3, "trickster", "trickster.ever", gone)), "The primer opens after the event: " + gone);

        // Trk_Targona_KilledPrimed: nothing left to spend.
        var killed = World(story, 3, "trickster.ever", "targona.dead_lab", P + "primed");
        var killedFresh = World(story, 3, "trickster.ever", "targona.dead_lab");
        killedFresh.Flags.Add(P + "primed"); killedFresh.Times[P + "primed"] = killedFresh.Hour;
        check(!Rules.Available(story, oneSoul, Later(story, killedFresh, 71)) && Rules.Available(story, oneSoul, Later(story, killedFresh, 72)),
            "Trk_Targona_KilledPrimed: the payoff ignores its three days.");
        check(Rules.Available(story, oneSoul, killed) && !Rules.Available(story, spent, killed), "Trk_Targona_KilledPrimed: availability.");
        var fullPages = new HashSet<string>();
        Program.Walk(oneSoul, killed, (page, _) => fullPages.Add(page));
        check(oneSoul.Nodes.Single(n => n.Id == "full").Text.Contains("It was used. It was not spent.", StringComparison.Ordinal)
              && fullPages.Contains("full") && !fullPages.Contains("cold")
              && oneSoul.Nodes.Single(n => n.Id == "full").Text.Contains("nobody in the room"),
            "The wand is not shown used unnoticed.");
        var returned = After(oneSoul, killed, "news", 0);
        check(returned.Has(P + "returned") && returned.Has(P + "cost.struck_down") && returned.Has("targona.started")
              && returned.Has(P + "cost.left_for_dead"), "Trk_Targona_KilledPrimed: flags.");
        var go = oneSoul.Nodes.Single(n => n.Id == "news").Choices[0];
        check(go.Crusade?.Resource == "Favors" && go.Crusade.Amount == -150, "The return costs the crusade nothing.");
        check(Rules.Available(story, furlough, returned), "Trk_Targona_KilledPrimed: the furlough does not open.");
        check(Reaches(returned, Committed), "Trk_Targona_KilledPrimed: the commit is unreachable.");

        // Trk_Targona_KilledUnprimed: the late light, dearer and spent for good.
        var unprimed = World(story, 3, "trickster", "trickster.ever", "targona.dead_lab");
        check(Rules.Available(story, lateLight, unprimed) && !Rules.Available(story, oneSoul, unprimed),
            "Trk_Targona_KilledUnprimed: availability.");
        var spend = lateLight.Nodes.Single(n => n.Id == "start").Choices[0];
        check(spend.Crusade?.Resource == "Favors" && spend.Crusade.Amount == -300 && spend.Mythic == "PlayerIsTrickster",
            "Trk_Targona_KilledUnprimed: the rite is free.");
        var late = After(lateLight, unprimed, "raise", 0);
        check(late.Has(P + "primed") && late.Has(P + "cost.late") && late.Has(P + "cost.raised_the_hard_way"),
            "Trk_Targona_KilledUnprimed: flags.");
        var lateLater = Later(story, late, 72);
        check(Rules.Available(story, oneSoul, lateLater), "Trk_Targona_KilledUnprimed: the payoff does not follow.");
        var coldPages = new HashSet<string>();
        Program.Walk(oneSoul, lateLater, (page, _) => coldPages.Add(page));
        check(coldPages.Contains("cold") && !coldPages.Contains("full"), "The spent light is shown full.");
        check(!Rules.Available(story, lateLight, World(story, 5, "trickster", "trickster.ever", "targona.dead_lab")),
            "The late fallback opens outside Chapter 3.");
        check(!Rules.Available(story, lateLight, World(story, 3, "trickster.ever", "targona.dead_lab")),
            "The late fallback opens after the path is lost.");

        // Trk_Targona_Furlough: the return beat never commits; the truth forgives, the joke and the lie do not.
        var back = World(story, 5, "trickster.ever", "targona.dead_lab", P + "returned", P + "cost.struck_down");
        check(Rules.Available(story, furlough, back), "Trk_Targona_Furlough: unavailable.");
        var forgiven = After(furlough, back, "truth", 0);
        check(forgiven.Has(P + "forgiven") && !forgiven.Has(Committed), "Trk_Targona_Furlough: flags.");
        check(!furlough.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed)), "The return beat commits.");
        check(Rules.Available(story, ward, Later(story, forgiven, 96)) && !Rules.Available(story, ward, Later(story, forgiven, 95)),
            "Trk_Targona_Furlough: the ward ignores its four days.");
        var joked = After(furlough, back, "joke", 0);
        check(joked.Has(P + "cost.unforgiven") && !Rules.Available(story, ward, Later(story, joked, 200))
              && Rules.Available(story, second, Later(story, joked, 96)), "The glib answer does not lead to the second asking.");
        var lied = After(furlough, back, "lie", 0);
        check(lied.Has(P + "cost.unforgiven") && lied.Has(P + "cost.lied"), "The lie is not recorded.");
        var sorry = After(second, Later(story, joked, 96), "sorry", 0);
        check(sorry.Has(P + "forgiven") && Reaches(sorry, Committed), "The apology does not reopen the ward.");
        var sent = After(second, Later(story, joked, 96), "start", 1);
        check(sent.Has(Closed) && !sent.Has("seelah.closed") && !sent.Has("sosiel.closed"), "Sending her away closes the wrong thing.");

        // Trk_Targona_Commit: the named producer, then the night.
        var ready = World(story, 5, "trickster.ever", "targona.dead_lab", P + "returned", P + "forgiven");
        check(Rules.Available(story, ward, ready) && !Rules.Available(story, quiet, ready), "Trk_Targona_Commit: availability.");
        var committed = After(ward, ready, "dawn", 0);
        check(committed.Has(Committed), "Trk_Targona_Commit: flags.");
        var nightPages = new HashSet<string>();
        Program.Walk(ward, ready, (page, _) => nightPages.Add(page));
        check(nightPages.Contains("threshold") && nightPages.Contains("morning")
              && Program.Walk(ward, ready).Any(o => o.Has(Committed) && o.Has(P + "night_kept")),
            "The commit has no night (Directive 12).");
        check(ward.Nodes.Single(n => n.Id == "threshold").Choices.All(c => c.Next == "morning"),
            "The threshold does not cut to the morning.");
        var left = Program.Walk(ward, ready).Where(o => o.Has(P + "cost.left_the_ward")).ToList();
        check(left.Count > 0 && left.All(o => o.Has(Closed) && !o.Has(Committed)), "Leaving before dawn does not close her route.");

        // Trk_Targona_Declined: her soft no, and the priced second ask.
        var metOnly = World(story, 5, "trickster.ever", "targona.free", P + "met", P + "cost.wand_unspent", P + "primed");
        check(Rules.Available(story, ward, metOnly), "Trk_Targona_Declined: the ward is closed to the freed state.");
        var declined = After(ward, metOnly, "refused", 0);
        check(declined.Has(P + "declined") && !declined.Has(Committed) && !declined.Has(Closed), "Trk_Targona_Declined: flags.");
        check(!Rules.Available(story, ward, Later(story, declined, 200)) && Rules.Available(story, quiet, Later(story, declined, 72))
              && !Rules.Available(story, quiet, Later(story, declined, 71)), "Trk_Targona_Declined: the quiet ward does not follow.");
        var sealedYes = After(quiet, Later(story, declined, 72), "start", 0);
        check(sealedYes.Has(Committed) && sealedYes.Has(P + "cost.light_sealed")
              && Program.Walk(quiet, Later(story, declined, 72)).Any(o => o.Has(P + "night_kept")), "Her price is not paid, or no night follows.");
        var refused = After(quiet, Later(story, declined, 72), "start", 1);
        check(refused.Has(Closed) && !refused.Has(Committed), "Refusing her price does not close her route.");

        // Trk_Targona_Free: the wand that does not run down.
        var free = World(story, 5, "trickster", "trickster.ever", "targona.free");
        check(Rules.Available(story, spent, free) && !Rules.Available(story, oneSoul, free) && !Rules.Available(story, lateLight, free),
            "Trk_Targona_Free: availability.");
        var wand = spent.Nodes.Single(n => n.Id == "start").Choices[0];
        check(wand.Crusade?.Resource == "Favors" && wand.Crusade.Amount == -300 && wand.Mythic == "PlayerIsTrickster"
              && wand.Text.StartsWith("[Spend it again, quietly]", StringComparison.Ordinal), "The wand night lost its joke or its cost.");
        var night = After(spent, free, "night", 0);
        check(night.Has(P + "primed") && night.Has(P + "cost.wand_unspent"), "Trk_Targona_Free: flags.");
        check(Rules.Available(story, freeFurlough, night), "Trk_Targona_Free: she does not come.");
        var met = After(freeFurlough, night, "why", 0);
        check(met.Has(P + "met") && met.Has("targona.started") && Reaches(met, Committed), "Trk_Targona_Free: the commit is unreachable.");
        var labPages = new HashSet<string>();
        var toldFree = Program.Copy(night); toldFree.Flags.Add(P + "told_in_lab");
        Program.Walk(freeFurlough, toldFree, (page, _) => labPages.Add(page));
        check(labPages.Contains("greet_lab") && !labPages.Contains("greet"), "She forgets the barrier.");

        // Trk_Targona_TreatmentDone: the parent Angelic Treatment route runs instead.
        var treated = World(story, 5, "trickster", "trickster.ever", "targona.free", "targona.ran_treatment_completed");
        check(!Rules.Available(story, spent, treated) && !Rules.Available(story, lateLight, treated), "Trk_Targona_TreatmentDone.");

        // Trk_Targona_Epilogue_Late and the siblings.
        var late6 = World(story, 6, "trickster.ever", P + "forgiven");
        check(Rules.Available(story, epCommit, late6) && !Rules.Available(story, epDeclined, late6), "Trk_Targona_Epilogue_Late.");
        check(Rules.Available(story, epFurlough, late6), "The late commit has no furlough page.");
        var wed6 = World(story, 6, "trickster.ever", P + "forgiven", Committed);
        check(!Rules.Available(story, epCommit, wed6) && Rules.Available(story, epFurlough, wed6), "A committed Targona gets the late page.");
        var no6 = World(story, 6, "trickster.ever", P + "met", P + "declined");
        check(Rules.Available(story, epDeclined, no6) && !Rules.Available(story, epCommit, no6) && !Rules.Available(story, epFurlough, no6),
            "The declined page is wrong.");
        var shut6 = World(story, 6, "trickster.ever", P + "forgiven", Closed);
        check(!Rules.Available(story, epCommit, shut6) && !Rules.Available(story, epFurlough, shut6), "A closed route gets a page.");
        foreach (var page in new[] { epCommit, epDeclined, epFurlough })
            check(page.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0), "An epilogue page has effects: " + page.Id);

        // Reactions: exactly Seelah, Sosiel and Ember; guarded; never touching another relationship.
        var reactions = story.Scenes.Where(s => s.Relationship == "targona" && s.Reaction).ToList();
        check(reactions.Select(s => s.Owner).OrderBy(o => o).SequenceEqual(new[] { "Ember", "Seelah", "Sosiel" }),
            "Targona's reactors are not exactly Seelah, Sosiel and Ember.");
        check(S(P + "react.seelah_furlough").Forbids.Contains("seelah_dead") && S(P + "react.seelah_furlough").Forbids.Contains("seelah_gone")
              && S(P + "react.sosiel_forgiven").Forbids.Contains("sosiel.dead") && S(P + "react.sosiel_forgiven").Forbids.Contains("sosiel.kicked_out")
              && S(P + "react.ember_wand").Forbids.Contains("ember_dead") && S(P + "react.ember_wand").Forbids.Contains("ember_gone"),
            "A reaction is not guarded against its reactor's absence.");
        check(Rules.Available(story, S(P + "react.seelah_furlough"), back) && !Rules.Available(story, S(P + "react.seelah_furlough"),
              World(story, 5, "trickster.ever", P + "returned", "seelah_dead")), "Seelah's reaction is wrong.");
        check(!reactions.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(),
            "A reaction sets state.");
        var ember = S(P + "react.ember_wand").Nodes[0].Text;
        check(!new[] { "kiss", "love", "beautiful", "darling" }.Any(w => ember.Contains(w, StringComparison.OrdinalIgnoreCase)),
            "Ember's reaction has romantic framing.");

        // Coexistence: no Targona scene requires another romanceable character's death, departure or closure.
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal)))
            check(!s.Requires.Any(f => f.EndsWith(".closed", StringComparison.Ordinal) && f != Closed
                                   || f.EndsWith("_dead", StringComparison.Ordinal) || f.EndsWith("_gone", StringComparison.Ordinal)),
                "A Targona scene requires another character's loss: " + s.Id);
        Console.WriteLine("PASS: Targona Trickster (Trk_Targona_*): the lab primer, the late light, one soul, the furlough, the ward and the wand.");
    }
}
