using System;

namespace Tirabade
{
    // Persist before entering SpawnUnit. An ambiguous submitted attempt is never spawned twice.
    public sealed class TerendelevDeliveryAttempt
    {
        public int Version = 1;
        public string UnitId = "";
        public string Provenance = "";
        public bool Submitted;
        public bool Confirmed;

        public bool Valid => Version == 1 && Guid.TryParse(UnitId, out _) && !string.IsNullOrWhiteSpace(Provenance)
            && (!Confirmed || Submitted);

        public bool CanSubmit(bool authorized, bool destinationReady, bool identityAbsent) =>
            Valid && authorized && destinationReady && identityAbsent && !Submitted && !Confirmed;

        public bool Submit(bool authorized, bool destinationReady, bool identityAbsent, Action persist, Action spawn)
        {
            if (!CanSubmit(authorized, destinationReady, identityAbsent)) return false;
            Submitted = true;
            persist();
            spawn();
            return true;
        }

        public bool TryConfirm(bool authorized, bool exactIdentity, bool committed, bool usable)
        {
            if (!Valid || !Submitted || !authorized || !exactIdentity || !committed || !usable) return false;
            Confirmed = true;
            return true;
        }
    }

    public enum TerendelevDeliveryResult { NotRequested, Pending, Confirmed, Blocked }
}
