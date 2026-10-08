using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Harem layer, wave 0 (16-HOUSEHOLD-DYNAMICS s3 "The Arueshalae branch key", s8c item 1): arueshalae.redeemed and
// arueshalae.corrupted, two positive Derived keys (storylines/household.py ARUESHALAE_BRANCH). Rules walks for every native
// and authored state the groups name, the ambiguous states that must select neither, and the producer Set arrays the
// authored groups depend on. Branch selection follows the consumer contract: a good row Requires redeemed AND Forbids
// corrupted; a corrupted row Requires corrupted.
internal static class ArueshalaeBranchTests
{
    private const string Redeemed = "arueshalae.redeemed";
    private const string Corrupted = "arueshalae.corrupted";
    private const string P = "arueshalae.trickster.";
    private const string EvilDead = "arueshalae.evil_dead";
    private const string Recruited = "arueshalae.evil_recruited";

    private static Snapshot Walk(Story story, IEnumerable<string> flags)
    {
        var state = new Snapshot { Chapter = 5, Hour = 5000 };
        state.Flags.Add("trickster");
        state.Flags.Add("trickster.ever");
        state.Flags.UnionWith(flags);
        Rules.Complete(story, state);
        return state;
    }

    // "3a" (good rows 3a/13 and the good versions of 9/11), "3b" (corrupted rows), or "neither".
    private static string Branch(Snapshot s) =>
        s.Has(Corrupted) ? "3b" : s.Has(Redeemed) ? "3a" : "neither";

    private static IEnumerable<(Scene scene, Node node, int index, Choice choice)> Setters(Story story, string flag) =>
        story.Scenes.SelectMany(s => s.Nodes.SelectMany(n => n.Choices.Select((c, i) => (s, n, i, c))))
            .Where(t => t.c.Set.Contains(flag));

    private static Choice ChoiceAt(Story story, string scene, string node, int index) =>
        story.Scenes.Single(s => s.Id == scene).Nodes.Single(n => n.Id == node).Choices[index];

    internal static void Run(Story story, Action<bool, string> check)
    {
        // The groups, exactly (Story.Derived syntax: OR of AND-groups).
        string Groups(string key) => story.Derived.TryGetValue(key, out var g)
            ? string.Join(" | ", g.Select(a => string.Join("+", a))) : "<missing>";
        check(Groups(Redeemed) == "arueshalae.changed | " + P + "aftertaste | " + P + "returned+" + P + "cost.gift_torn | " + P + "cost.chaplain"
            + " | arueshalae.recruited_drezen | arueshalae.recruited_redoubt",
            "arueshalae.redeemed groups differ: " + Groups(Redeemed));
        check(Groups(Corrupted) == Recruited + " | " + P + "returned+" + P + "cost.nocticula_debt | " + P + "returned+" + P
            + "cost.nocticula_favour | " + P + "reunited | " + P + "fallen.house_call | arueshalae.fallen", "arueshalae.corrupted groups differ: " + Groups(Corrupted));

        // The native sources are bound as the existing readers bind them (the assembled payload, before any pair prose).
        check(story.Derived.TryGetValue("arueshalae.changed", out var changed)
            && string.Join(" | ", changed.Select(a => string.Join("+", a))) == "arueshalae.elysium | arueshalae.back_to_reality",
            "arueshalae.changed is not the native release (elysium | back_to_reality).");
        check(story.SeenCues.TryGetValue("arueshalae.back_to_reality", out var cues)
            && cues.Contains("6b24754fcea768342a30a1e18ce91b92") && cues.Contains("8ad7c2ba0e060e545b12269cc5ced777"),
            "BackToReality Cue_0018/Cue_0025 are not bound to arueshalae.back_to_reality.");
        check(story.StartedDialogs.TryGetValue("arueshalae.elysium", out var best) && best == "3edf6ac1aefa1e3429ca04c60cb8565c",
            "The Ch5 BestEnding dialog is not bound to arueshalae.elysium.");
        check(story.Etudes.TryGetValue(Recruited, out var evil) && evil == "005c2284d7e5ac54c887bb3781e45d0c",
            "EvilArushaRecruited is not bound to arueshalae.evil_recruited.");
        // Native good recruitment and the fall (read-only; ArueshalaeStates children with no activation condition, area or
        // chapter cascade): RecruitedInDrezen, RecruitedFinally, and ArueshalaeIsEvil (started by her fall with Unrecruit).
        foreach (var (key, guid) in new[] { ("arueshalae.recruited_drezen", "c2df9c6dd50caba4aade683908ac5ae3"),
                     ("arueshalae.recruited_redoubt", "b3b87ce125827084cae26aaced267697"), ("arueshalae.fallen", "e85e8acd74d231e44ad7d6d2d5dab43c") })
            check(story.Etudes.TryGetValue(key, out var g) && g == guid && !story.PermanentEtudes.Contains(key)
                && Rules.EtudeHeld(story, key, true, false) && !Rules.EtudeHeld(story, key, false, true),
                "Arueshalae branch etude " + key + " is not a Playing-only read of " + guid + ".");
        // The recruitment binder reads Playing only: Started-and-dormant or merely Completed never classifies her.
        check(Rules.EtudeHeld(story, Recruited, true, false) && !Rules.EtudeHeld(story, Recruited, false, false)
            && !Rules.EtudeHeld(story, Recruited, false, true), "arueshalae.evil_recruited is not a Playing-only read.");

        // Producers: the authored sources come from the choices the groups were written against (indices are save references).
        bool Sets(string scene, string node, int i, params string[] flags) => flags.All(ChoiceAt(story, scene, node, i).Set.Contains);
        check(Sets(P + "returned.aftertaste", "test", 0, P + "aftertaste") && Sets(P + "returned.aftertaste", "test", 1, P + "aftertaste"),
            "Aftertaste test [0]/[1] do not set the aftertaste flag.");
        check(Sets(P + "dead.starving", "thread", 0, P + "cost.gift_torn") && Sets(P + "dead.starving", "thread", 1, P + "cost.gift_torn")
            && Sets(P + "dead.starving", "plea", 0, P + "returned") && Sets(P + "dead.starving", "plea", 1, P + "returned")
            && !ChoiceAt(story, P + "dead.starving", "plea", 2).Set.Contains(P + "returned"),
            "The legacy good return's torn-gift/return producers moved.");
        check(Sets(P + "failed.chaplain", "sword", 0, P + "cost.chaplain")
            && story.Scenes.Single(s => s.Id == P + "failed.chaplain").Forbids.Contains(Recruited), "The chaplain producer moved.");
        foreach (var node in new[] { "queen", "late", "fooled", "unanswered" })
            check(Sets(P + "evil.second_opinion", node, 0, P + "returned", P + "cost.nocticula_debt")
                && Sets(P + "evil.second_opinion", node, 1, P + "returned", P + "cost.nocticula_favour")
                && !ChoiceAt(story, P + "evil.second_opinion", node, 2).Set.Contains(P + "returned"),
                "The legacy queen payment producers moved on " + node + ".");
        check(Sets(P + "fallen.house_call", "ask", 0, P + "fallen.house_call") && Sets(P + "fallen.house_call", "ask", 1, P + "fallen.house_call")
            && Sets(P + "fallen.house_call", "ask", 2, P + "fallen.house_call"), "The fallen house call does not mark every answer.");
        // Branch invariant over EVERY producer: a corrupted source is only set where she is evil (evil death or evil
        // recruitment required); a good source is only set where the evil states are forbidden.
        bool EvilScene(Scene s) => s.Requires.Contains(EvilDead) || s.Requires.Contains(Recruited);
        bool GoodScene(Scene s) => s.Forbids.Contains(EvilDead) || s.Forbids.Contains(Recruited);
        foreach (var flag in new[] { P + "cost.nocticula_debt", P + "cost.nocticula_favour", P + "reunited", P + "fallen.house_call" })
        {
            var setters = Setters(story, flag).ToList();
            check(setters.Count > 0 && setters.All(t => EvilScene(t.scene)),
                "A corrupted source is set outside her evil states: " + flag + " in "
                + string.Join(",", setters.Where(t => !EvilScene(t.scene)).Select(t => t.scene.Id).Distinct()));
        }
        foreach (var flag in new[] { P + "aftertaste", P + "cost.gift_torn", P + "cost.chaplain" })
        {
            var setters = Setters(story, flag).ToList();
            check(setters.Count > 0 && setters.All(t => GoodScene(t.scene)),
                "A redeemed source is set where her evil states are allowed: " + flag + " in "
                + string.Join(",", setters.Where(t => !GoodScene(t.scene)).Select(t => t.scene.Id).Distinct()));
        }
        // Nothing sets either classifier, and no scene latches them: they are Derived only.
        check(!Setters(story, Redeemed).Any() && !Setters(story, Corrupted).Any(), "A choice sets an Arueshalae branch key directly.");

        // Rules walks (16 s8b acceptance: redeemed, corrupted and unknown select 3a, 3b or neither).
        var walks = new (string name, string[] flags, bool redeemed, bool corrupted, string branch)[]
        {
            ("native release, Cue_0018/0025 seen", new[] { "arueshalae.back_to_reality" }, true, false, "3a"),
            ("native BestEnding started", new[] { "arueshalae.elysium" }, true, false, "3a"),
            ("native evil recruitment Playing", new[] { Recruited }, false, true, "3b"),
            ("native recruitment in Drezen (Ch2 prison)", new[] { "arueshalae.recruited_drezen" }, true, false, "3a"),
            ("native recruitment at the redoubt (Ch3)", new[] { "arueshalae.recruited_redoubt" }, true, false, "3a"),
            ("recruited good, then fell (not re-recruited)", new[] { "arueshalae.recruited_drezen", "arueshalae.fallen" }, true, true, "3b"),
            ("recruited at the redoubt, fell, recruited evil", new[] { "arueshalae.recruited_redoubt", "arueshalae.fallen", Recruited }, true, true, "3b"),
            ("fallen, never recruited good", new[] { "arueshalae.fallen" }, false, true, "3b"),
            ("recruited good, fell, killed in the lair", new[] { "arueshalae.recruited_drezen", "arueshalae.fallen", EvilDead }, true, true, "3b"),
            ("legacy good return, torn gift", new[] { P + "returned", P + "cost.gift_torn", P + "cost.fed_on_you" }, true, false, "3a"),
            ("Aftertaste answered (fed on you)", new[] { P + "returned", P + "cost.fed_on_you", P + "aftertaste", P + "said_every_time" }, true, false, "3a"),
            ("Aftertaste answered (fed on a prisoner)", new[] { P + "returned", P + "cost.fed_on_prisoner", P + "aftertaste", P + "said_if_asked" }, true, false, "3a"),
            ("failed romance, chaplain accepted", new[] { "arueshalae.failed", P + "cost.chaplain" }, true, false, "3a"),
            ("legacy evil return, queen debt", new[] { EvilDead, P + "returned", P + "cost.nocticula_debt" }, false, true, "3b"),
            ("legacy evil return, queen favour", new[] { EvilDead, P + "returned", P + "cost.nocticula_favour" }, false, true, "3b"),
            ("legacy reunion, feeding refused", new[] { EvilDead, P + "returned", P + "cost.nocticula_debt", P + "reunited", P + "cost.sent_away_hungry" }, false, true, "3b"),
            ("fallen house call, romance refused", new[] { Recruited, P + "fallen.house_call", "arueshalae.closed" }, false, true, "3b"),
            ("fallen house call alone", new[] { P + "fallen.house_call" }, false, true, "3b"),
            ("good history, then evil recruitment", new[] { "arueshalae.back_to_reality", P + "cost.chaplain", Recruited }, true, true, "3b"),
            ("good return history, then queen-paid return", new[] { P + "aftertaste", P + "returned", P + "cost.nocticula_favour" }, true, true, "3b"),
            ("empty", new string[0], false, false, "neither"),
            ("returned alone", new[] { P + "returned" }, false, false, "neither"),
            ("queen debt alone", new[] { P + "cost.nocticula_debt" }, false, false, "neither"),
            ("queen favour alone", new[] { P + "cost.nocticula_favour" }, false, false, "neither"),
            ("torn gift alone", new[] { P + "cost.gift_torn" }, false, false, "neither"),
            ("dead", new[] { "arueshalae_dead" }, false, false, "neither"),
            ("evil dead", new[] { EvilDead }, false, false, "neither"),
            ("dismissed", new[] { "arueshalae.kicked_out", "arueshalae.kicked_out_evil" }, false, false, "neither"),
            ("failed romance alone", new[] { "arueshalae.failed" }, false, false, "neither"),
            ("native romance active", new[] { "arueshalae.native_romance" }, false, false, "neither"),
            ("mod started/committed", new[] { "arueshalae.started", "arueshalae.committed" }, false, false, "neither"),
            ("late committed", new[] { P + "late_committed" }, false, false, "neither"),
            ("supportive lab answer, dream kiss, early Desna, treatment intake",
                new[] { "arueshalae.lab_seen", "arueshalae.dream_woken", "arueshalae.early.desna", "arueshalae.treatment.mealtimes" }, false, false, "neither"),
            ("nocticula claimed", new[] { "arueshalae.nocticula_claimed" }, false, false, "neither"),
        };
        // Coexistence: every other romance committed at once leaves the classification unchanged.
        var others = story.Relationships.Where(r => r.Key != "arueshalae" && !string.IsNullOrEmpty(r.Value.CommittedFlag))
            .Select(r => r.Value.CommittedFlag).ToArray();
        check(others.Length > 10, "The coexistence walk found no other committed flags.");
        foreach (var w in walks)
        {
            foreach (var (label, extra) in new[] { ("", new string[0]), (" + every other romance committed", others) })
            {
                var s = Walk(story, w.flags.Concat(extra));
                check(s.Has(Redeemed) == w.redeemed && s.Has(Corrupted) == w.corrupted && Branch(s) == w.branch,
                    $"Arueshalae branch walk '{w.name}{label}': redeemed={s.Has(Redeemed)} corrupted={s.Has(Corrupted)} branch={Branch(s)}"
                    + $" (expected {w.redeemed}/{w.corrupted}/{w.branch}).");
            }
        }
        // A classified Arueshalae who is later unavailable keeps her classification (history); availability is the pair
        // scenes' own gates (dead, dismissed, closed), never this key's.
        var gone = Walk(story, new[] { "arueshalae.back_to_reality", "arueshalae_dead" });
        check(gone.Has(Redeemed) && !gone.Has(Corrupted), "A dead redeemed Arueshalae loses her branch history.");
        // No consumer exists yet; when one lands, a redeemed consumer must also Forbid corrupted (corruption wins).
        foreach (var s in story.Scenes.Where(s => s.Requires.Contains(Redeemed)))
            check(s.Forbids.Contains(Corrupted), "A redeemed-branch scene does not Forbid arueshalae.corrupted: " + s.Id);
    }
}
