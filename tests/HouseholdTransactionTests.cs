using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class HouseholdTransactionTests
{
    internal static void Run(Story exported, Action<bool, string> check)
    {
        // GLOBAL-TC's eight terminal prices, including their recovery prices.
        foreach (var (resource, price) in new[] { ("Finances", 200), ("Finances", 300),
            ("Materials", 150), ("Materials", 200), ("Materials", 100), ("Materials", 150),
            ("Materials", 150), ("Materials", 200) })
        {
            var story = new Story { RestAllowances = new Dictionary<string, int> { ["household.protected"] = 2 } };
            story.Relationships["household"] = new Relationship { StartedFlag = "hh.started", ClosedFlag = "hh.closed", CommittedFlag = "hh.committed" };
            var choice = new Choice { Crusade = new CrusadeChoice { Resource = resource, Amount = -price },
                Set = new[] { "docket.seen", "cost.paid", "concession.first", "concession.second" } };
            var scene = new Scene { Id = "docket.singleton", Relationship = "household", Owner = "Seelah", MinChapter = 5, MaxChapter = 5,
                InteractionHub = Rules.TableHub, RestAllowance = "household.protected", Forbids = new[] { "docket.seen" },
                Nodes = new List<Node> { new Node { Id = "start", Text = "Test", Choices = new List<Choice> { choice, new Choice { Abort = true } } } } };
            story.Scenes.Add(scene);
            Snapshot World(int? balance) => new Snapshot { Chapter = 5, Hour = 100,
                CrusadeResources = balance == null ? null : new Dictionary<string, int> { [resource] = balance.Value } };
            bool Take(Snapshot state, bool partial = false, bool throwPublication = false)
            {
                var before = Program.Copy(state);
                return Rules.CrusadeTransaction(choice.Crusade,
                    () => Rules.PaidChoiceAvailable(story, scene, choice, state),
                    () => state.CrusadeResources == null ? (int?)null : state.CrusadeResources[resource],
                    amount => state.CrusadeResources![resource] += partial && amount < 0 ? amount + 1 : amount,
                    () => {
                        if (!Rules.SpendRestAllowance(story, scene, state)) throw new InvalidOperationException("Allowance lost");
                        foreach (var flag in choice.Set) { state.Flags.Add(flag); state.Times[flag] = state.Hour; }
                        state.Flags.Add(scene.Id); state.Times[scene.Id] = state.Hour;
                        state.Flags.Add(Rules.PaymentKey(scene, choice));
                        if (throwPublication) throw new InvalidOperationException("Publication interrupted");
                    },
                    () => { state.Flags = before.Flags; state.Times = before.Times; state.RestSpent = before.RestSpent; }, _ => { });
            }
            foreach (int? funds in new int?[] { null, 0, price - 1, price, price + 73 })
            {
                var state = World(funds); state.Flags.Add("prior.witness"); state.Times["prior.witness"] = 12;
                bool affordable = funds >= price;
                check(Rules.ChoiceAvailable(choice, state) == affordable, "GLOBAL-TC selection affordability mismatch");
                var savedBefore = Program.Copy(state);
                check(Take(state) == affordable, "GLOBAL-TC execution affordability mismatch");
                check(state.Has("prior.witness") && state.Times["prior.witness"] == 12, "Transaction erased earlier evidence");
                if (affordable)
                {
                    check(state.CrusadeResources![resource] == funds - price && choice.Set.All(state.Has)
                        && state.Has(scene.Id) && state.RestSpent["household.protected"] == 1, "Full paid record/debit did not commit");
                    var options = new JsonSerializerOptions { IncludeFields = true };
                    var loaded = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(state, options), options)!;
                    check(!Take(loaded) && loaded.CrusadeResources![resource] == funds - price, "Reload/double click paid twice");
                    check(Take(savedBefore), "An earlier save incorrectly inherited a paid receipt");
                    var singleton = scene.Id; scene.Id = "docket.packet";
                    check(!Take(state), "Packet paid an already settled singleton");
                    scene.Id = singleton;
                }
                else check(!state.Has(scene.Id) && !state.Has("cost.paid") && state.RestSpent.Count == 0, "Rejected purchase published a paid record");
            }
            var stale = World(price);
            check(Rules.ChoiceAvailable(choice, stale), "Menu failed to offer an affordable answer");
            stale.CrusadeResources![resource] = price - 1;
            check(!Take(stale), "Execution trusted the menu's old balance");
            stale.CrusadeResources = null;
            check(!Take(stale), "Execution trusted the menu's old kingdom");
            stale = World(price); stale.RestSpent["household.protected"] = 2;
            check(!Take(stale) && stale.CrusadeResources![resource] == price, "Consumed allowance charged a purchase");
            foreach (bool partial in new[] { false, true })
            {
                var failed = World(price); failed.Flags.Add("prior.witness"); failed.Times["prior.witness"] = 12;
                check(!Take(failed, partial, throwPublication: true), "Partial debit/publication exception reported success");
                check(failed.CrusadeResources![resource] == price && failed.Flags.SetEquals(new[] { "prior.witness" })
                    && failed.Times.Count == 1 && failed.Times["prior.witness"] == 12 && failed.RestSpent.Count == 0,
                    "Transaction rollback left debit, witnesses, timestamps or allowance behind");
            }
            var intermediate = World(price + 73);
            scene.Forbids = Array.Empty<string>();
            intermediate.Flags.Add(Rules.PaymentKey(scene, choice));
            check(!Take(intermediate) && intermediate.CrusadeResources![resource] == price + 73, "Intermediate paid answer replayed its debit");
            var paidOnly = new Node { Choices = new List<Choice> { choice } };
            check(Rules.PaymentExitAvailable(story, scene, paidOnly, intermediate), "A spent paid answer left its page without an exit");
            check(Rules.ChoiceAvailable(scene.Nodes[0].Choices[1], World(null)), "Later disappeared with a missing kingdom");
        }
        SharedClocksAndDeparture(check);
        LegacyPaidContinuation(check);
        PresenceAttachments(exported, check);
        DeedClockValidation(exported, check);
    }

    private static void SharedClocksAndDeparture(Action<bool, string> check)
    {
        var story = new Story { RestAllowances = new Dictionary<string, int> { ["protected"] = 2 } };
        story.Relationships["test"] = new Relationship { ClosedFlag = "closed" };
        var paid = new Choice { Set = new[] { "paid" }, PostPayment = "receipt",
            Crusade = new CrusadeChoice { Resource = "Materials", Amount = -100 } };
        var scene = new Scene { Id = "test.payment", Relationship = "test", MinChapter = 5, MaxChapter = 5,
            ContactUnit = "00000000000000000000000000000001", Requires = new[] { "deed", "form" },
            DelayHours = 48, DelayClocks = new[] { "deed" }, RestAllowance = "protected",
            Nodes = new List<Node> { new Node { Id = "start", Choices = new List<Choice> { paid } },
                new Node { Id = "receipt", Choices = new List<Choice> { new Choice { Abort = true } } } } };
        var state = new Snapshot { Chapter = 5, Hour = 100, CrusadeResources = new Dictionary<string, int> { ["Materials"] = 100 } };
        state.Flags.UnionWith(new[] { "deed", "form", "prior" });
        state.Times["deed"] = 52; state.Times["form"] = 99; state.Times["prior"] = 12;
        state.AvailableContacts.Add(scene.ContactUnit);
        check(Rules.Available(story, scene, state), "A body change restarted the declared predecessor clock");
        state.Hour = 99;
        check(!Rules.Available(story, scene, state), "The predecessor wait opened an hour early");
        state.Hour = 100; state.Times.Remove("deed");
        check(!Rules.Available(story, scene, state), "A missing saved predecessor granted a wait");
        state.Times["deed"] = 52;
        var refresh = new Choice { Set = new[] { "deed", "prior" }, RefreshTimes = new[] { "deed" } };
        foreach (int hour in new[] { 100, 124 })
        {
            state.Hour = hour;
            Rules.RecordFlags(refresh.Set, refresh.RefreshTimes, state).ToArray();
            check(state.Times["deed"] == hour && state.Times["prior"] == 12, "Explicit repeat refreshed the wrong clock");
            state = Program.Copy(state);
        }
        state.Times["deed"] = 52; state.Hour = 100;
        foreach (string fault in new[] { "debit", "publication", "closure", "none" })
        {
            var world = Program.Copy(state); var before = Program.Copy(world); int publications = 0;
            check(!Rules.PostPaymentAvailable(story, scene, paid, world), "Receipt narrated before the debit");
            bool result = Rules.CrusadeTransaction(paid.Crusade,
                () => Rules.PaidChoiceAvailable(story, scene, paid, world),
                () => world.CrusadeResources!["Materials"],
                amount => { world.CrusadeResources!["Materials"] += amount;
                    if (amount < 0 && fault == "debit") world.AvailableContacts.Clear(); },
                () => {
                    publications++;
                    check(world.CrusadeResources!["Materials"] == 0, "Receipt preceded full debit");
                    if (!Rules.SpendRestAllowance(story, scene, world)) throw new InvalidOperationException();
                    Rules.RecordFlags(paid.Set.Concat(new[] { scene.Id }), Array.Empty<string>(), world).ToArray();
                    world.Flags.Add(Rules.PaymentKey(scene, paid));
                    if (fault == "publication") world.AvailableContacts.Clear();
                    if (fault == "closure") world.Flags.Add("closed");
                },
                () => { world.Flags = before.Flags; world.Times = before.Times; world.RestSpent = before.RestSpent; },
                _ => { }, () => Rules.PaymentContextAvailable(story, scene, paid, world));
            check(result == (fault == "none"), "Departure during payment committed a transaction: " + fault);
            check(publications == (fault == "debit" ? 0 : 1), "Departure during debit still published witnesses");
            if (result)
            {
                check(world.CrusadeResources!["Materials"] == 0 && world.RestSpent["protected"] == 1
                    && Rules.PostPaymentAvailable(story, scene, paid, world), "Atomic payment did not open its receipt");
                world.AvailableContacts.Clear();
                check(!Rules.PostPaymentAvailable(story, scene, paid, world), "A departed actor narrated the paid aftermath");
            }
            else check(world.CrusadeResources!["Materials"] == 100 && world.Flags.SetEquals(before.Flags)
                && world.Times.OrderBy(p => p.Key).SequenceEqual(before.Times.OrderBy(p => p.Key)) && world.RestSpent.Count == 0,
                "Departure rollback retained payment state");
        }
    }

    private static void DeedClockValidation(Story exported, Action<bool, string> check)
    {
        var clock = exported.Scenes[0].Id;
        var scene = new Scene { Id = "household.test.clock", Relationship = "household", Owner = "Narrator",
            MinChapter = 5, MaxChapter = 5, InteractionHub = Rules.TableHub, RestAllowance = "household.pair", DelayHours = 48,
            RequiresAnyGroups = new[] { new[] { clock, "household.test.entry_clock" } },
            Nodes = new List<Node> { new Node { Id = "start", Text = "Test", EnterSet = new[] { "household.test.entry_clock" },
                Choices = new List<Choice> { new Choice { Abort = true } } } } };
        exported.Scenes.Add(scene);
        try
        {
            Rules.Validate(exported);
            check(true, "Scene IDs and EnterSet witnesses supply saved clocks");
            scene.RequiresAnyGroups = new[] { new[] { clock, exported.Derived.Keys.First() } };
            bool rejected = false;
            try { Rules.Validate(exported); }
            catch (InvalidOperationException ex) { rejected = ex.Message.Contains("deed clock on every alternative"); }
            check(rejected, "An untimestamped AnyGroups alternative supplied a deed clock");
            scene.Requires = new[] { clock };
            Rules.Validate(exported);
            check(true, "An unconditional saved deed supplies the clock independently of other OR groups");
        }
        finally { exported.Scenes.Remove(scene); }
    }

    private static void LegacyPaidContinuation(Action<bool, string> check)
    {
        var story = new Story();
        story.Relationships["household"] = new Relationship { StartedFlag = "hh.started", ClosedFlag = "hh.closed", CommittedFlag = "hh.committed" };
        var first = new Choice { Set = new[] { "entry.seen" }, Next = "recovery", Crusade = new CrusadeChoice { Resource = "Finances", Amount = -50 } };
        var recovery = new Choice { Set = new[] { "entry.seen", "full.paid" }, Crusade = new CrusadeChoice { Resource = "Finances", Amount = -150 } };
        var scene = new Scene { Id = "legacy.paid", Owner = "Narrator", Relationship = "household", MinChapter = 5, MaxChapter = 5,
            InteractionHub = Rules.TableHub, Forbids = new[] { "entry.seen" }, Nodes = new List<Node> {
                new Node { Id = "start", Text = "Test", Choices = new List<Choice> { first } },
                new Node { Id = "recovery", Text = "Test", Choices = new List<Choice> { recovery } } } };
        var state = new Snapshot { Chapter = 5, Hour = 100, CrusadeResources = new Dictionary<string, int> { ["Finances"] = 200 } };
        check(Rules.PaidChoiceAvailable(story, scene, first, state), "Legacy first payment disappeared");
        state.Flags.Add("entry.seen"); state.Flags.Add(Rules.PaymentKey(scene, first)); state.CrusadeResources["Finances"] -= 50;
        check(!Rules.Available(story, scene, state) && !Rules.PaidChoiceAvailable(story, scene, first, state), "Legacy entry witness allowed root replay");
        check(Rules.PaidChoiceAvailable(story, scene, recovery, state), "Earlier in-conversation entry witness blocked paid recovery");
        state.Flags.Add("hh.closed");
        check(!Rules.PaidChoiceAvailable(story, scene, recovery, state), "Legacy progress exemption bypassed route closure");
        state.Flags.Remove("hh.closed"); recovery.Forbids = new[] { "entry.seen" };
        check(!Rules.PaidChoiceAvailable(story, scene, recovery, state), "Legacy progress exemption bypassed the choice guard");
    }

    private static void PresenceAttachments(Story exported, Action<bool, string> check)
    {
        foreach (var name in new[] { "nidalynn.presence", "nidalynn.presence.chosen", "minagho_chivarro.presence.minagho", "minagho_chivarro.presence.minagho_spared" })
        {
            var presence = exported.Presences[name]; var owner = Rules.PresenceRelationship(name)!;
            var scene = new Scene { Id = "household.test.attachment", Relationship = "household", Owner = "Narrator",
                MinChapter = 5, MaxChapter = 5, Chapters = new[] { 5 }, Areas = new[] { presence.Area }, ContactUnit = presence.Unit,
                InteractionHub = name, Participants = new[] { owner }, ParticipantWomen = owner == "minagho_chivarro" ? new[] { "minagho" } : Array.Empty<string>(),
                Requires = presence.Requires.Select(f => f == "trickster.ever" ? "trickster" : f).ToArray(),
                RequiresAnyGroups = presence.RequiresAnyGroups, Forbids = presence.Forbids.Concat(new[] { "trickster.failed" }).Distinct().ToArray(),
                Nodes = new List<Node> { new Node { Id = "start", Text = "Test", Choices = new List<Choice> { new Choice() } } } };
            exported.Scenes.Add(scene);
            try
            {
                check(Rules.HouseholdPresenceAttachment(exported, scene), "Valid qualified body rejected: " + name);
                Rules.Validate(exported);
                var unit = scene.ContactUnit; scene.ContactUnit = "00000000000000000000000000000001";
                check(!Rules.HouseholdPresenceAttachment(exported, scene), "Wrong presence unit accepted"); scene.ContactUnit = unit;
                var required = scene.Requires;
                foreach (var gate in required.Where(f => f != "trickster"))
                {
                    scene.Requires = required.Where(f => f != gate).ToArray();
                    check(!Rules.HouseholdPresenceAttachment(exported, scene), "Missing current body gate accepted: " + gate);
                }
                scene.Requires = required;
                var forbidden = scene.Forbids; scene.Forbids = Array.Empty<string>();
                check(!Rules.HouseholdPresenceAttachment(exported, scene), "Unguarded closure/form accepted"); scene.Forbids = forbidden;
                scene.Participants = Array.Empty<string>();
                check(!Rules.HouseholdPresenceAttachment(exported, scene), "Missing physical participant accepted"); scene.Participants = new[] { owner };
                scene.Areas = new[] { "00000000000000000000000000000001" };
                check(!Rules.HouseholdPresenceAttachment(exported, scene), "Wrong presence area accepted"); scene.Areas = new[] { presence.Area };
                scene.Chapters = new[] { 6 }; check(!Rules.HouseholdPresenceAttachment(exported, scene), "Out-of-window presence accepted"); scene.Chapters = new[] { 5 };
                scene.InteractionHub = "nidalynn.presence.unknown";
                check(!Rules.HouseholdPresenceAttachment(exported, scene), "Unknown hub accepted"); scene.InteractionHub = name;
                var state = new Snapshot { Chapter = 5, Hour = 1000, Area = presence.Area };
                state.Flags.UnionWith(new[] { "chapter_later", "trickster.ever" });
                foreach (var gate in scene.Requires) HouseholdTests.Earn(exported, state, gate);
                foreach (var group in scene.RequiresAnyGroups) state.Flags.Add(group[0]);
                HouseholdTests.Earn(exported, state, owner + ".harem.eligible");
                if (owner == "minagho_chivarro")
                {
                    if (state.Has("minagho.dead"))
                    {
                        HouseholdTests.Earn(exported, state, "minagho_chivarro.trickster.collateral_delivered");
                        HouseholdTests.Earn(exported, state, "minagho_chivarro.trickster.returned_minagho");
                    }
                    foreach (var gate in exported.SeatWomen["minagho"].Requires) HouseholdTests.Earn(exported, state, gate);
                }
                Rules.Complete(exported, state); state.AvailableContacts.Add(presence.Unit);
                check(Rules.ContactAvailable(exported, scene, state), "Qualified presence did not allow current contact: " + name + " participants=" + Rules.ParticipantsAvailable(exported, scene, state)
                    + " wanted=" + Rules.PresenceWanted(presence, state) + " missing=" + string.Join(",", scene.Requires.Where(f => !state.Has(f)))
                    + " forbids=" + string.Join(",", scene.Forbids.Where(state.Has)));
                state.AvailableContacts.Clear();
                check(!Rules.ContactAvailable(exported, scene, state), "Missing body still supplied contact");
                state.AvailableContacts.Add(presence.Unit);
                if (owner == "minagho_chivarro")
                {
                    var otherDead = Program.Copy(state); otherDead.Flags.Add("chivarro.dead"); Rules.Complete(exported, otherDead);
                    check(Rules.ContactAvailable(exported, scene, otherDead), "Chivarro death vetoed Minagho's qualified attachment");
                    var noReturn = Program.Copy(state); noReturn.Flags.Add("minagho.dead");
                    noReturn.Flags.Remove("minagho_chivarro.trickster.returned_minagho"); Rules.Complete(exported, noReturn);
                    check(!Rules.ContactAvailable(exported, scene, noReturn), "Unreturned Minagho appeared physically");
                }
                state.Flags.Add(exported.Relationships[owner].ClosedFlag);
                check(!Rules.ContactAvailable(exported, scene, state), "Closed body still available");
            }
            finally { exported.Scenes.Remove(scene); }
        }
    }
}
