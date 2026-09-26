using System;

namespace Tirabade
{
    // Stored as a JSON string in Player.SettingsList before native state changes.
    public sealed class RecoveryAttempt
    {
        public int Version = 1;
        public string UnitId = "";
        public int Roster;
        public string SceneId = "";
        public string ChoiceJson = "";

        public bool Matches(RecoveryStatus state) => Version == 1 && UnitId.Length > 0
            && state.Eligible && state.UnitId == UnitId && state.Roster == Roster;

        public bool IsRestored(RecoveryStatus state) => Matches(state) && !state.Dead && state.Conscious;

        public string PendingReason(RecoveryStatus state)
        {
            if (!state.Eligible) return "The original companion is unavailable, hostile, duplicated, or outside the retained party state. The restoration checkpoint is preserved.";
            if (state.UnitId != UnitId) return "The available companion has a different saved identity. The original restoration checkpoint is preserved.";
            if (state.Roster != Roster) return "The companion's party status has changed. Recovery cannot be credited until the original status is restored.";
            if (state.Dead) return "The original companion is still dead. The recovery scene can be attempted again when its requirements are met.";
            return "The original companion is alive but not conscious. Verification is waiting; resurrection will not be repeated.";
        }

        public bool TryApply(Func<RecoveryStatus> inspect, Action resurrect, out string message)
        {
            try
            {
                var before = inspect();
                if (!Matches(before))
                {
                    message = "The saved companion no longer matches this restoration attempt. No progress was recorded.";
                    return false;
                }
                // A prior call may have revived her before throwing. Never replay it on a living unit.
                if (before.Dead) resurrect();
                if (!IsRestored(inspect()))
                {
                    message = "Restoration is pending. The original companion must be alive and conscious with unchanged party status.";
                    return false;
                }
                message = "The original companion is alive and conscious again, with the same saved identity and party status.";
                return true;
            }
            catch (Exception ex)
            {
                message = "Restoration was interrupted. Its checkpoint has been retained for verification. " + ex.Message;
                return false;
            }
        }
    }

    public sealed class RecoveryStatus
    {
        public string UnitId = "";
        public int Roster;
        public bool Eligible;
        public bool Dead;
        public bool Conscious;
    }
}
