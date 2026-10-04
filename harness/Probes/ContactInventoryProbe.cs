using System.Collections.Generic;
using System.Linq;

namespace RRT.TestHarness
{
    // E-Q7-35: observation only. Availability is read from NativeContact's own predicate.
    public sealed class ContactInventoryActor
    {
        public string State = "";
        public bool Usable, Ignorable;
    }

    public sealed class ContactInventoryProbe
    {
        public string Unit = "";
        public List<ContactInventoryActor> Actors = new List<ContactInventoryActor>();
        public string? AnchorWalkability;
        public bool NativeAccepted, SnapshotAccepted, NativeWitnessesPresent;
        public bool ExpectedUsable => Actors.Count(a => a.Usable) == 1 && Actors.All(a => a.Usable || a.Ignorable);
        public string Verdict => ExpectedUsable != NativeAccepted || ExpectedUsable != SnapshotAccepted
            ? "contact-oracle-failure" : !ExpectedUsable ? "skipped-inline"
            : !NativeWitnessesPresent ? "skipped-native" : "usable";
    }
}
