"""Kiana's native reconciliations (engine queue 8; Writer/handoffs/trickster/kiana.md, Polish pass residuals 1-2).

8a: VendorArsinoe/Answer_0025 ("Is there any news about the poor folk whose souls were stolen?" -> Cue_0026, her search
found nothing) stays offered after the Commander ransomed or bought back the guests. A reviewed E18 gate hides it in those
worlds (the list the game already shows once Seelah's Q3 has started). Read only; warning-only on refusal.
"""
import copy

from story_format import n, scene

from storylines import kiana_trickster as kt

# 8c: Seelah Q3's ElandKianaAftermath (dialog 27bc5f6c) opens on Cue_0001 "Elan and Kiana fall into each other's arms". A couple
# that separated (kiana.separated) gets its own line in the same place (E14i, the dialog's FirstCue); Seelah's "Let's give them
# some space" (Cue_0002) still follows. Read only, warning-only.
AFTERMATH = "kiana.native.aftermath_separated"
SCENES = [scene(AFTERMATH, "", "KianaEpilogue", 3, "", [
    n("arms", "Narrator", "{n}Elan and Kiana face each other, both alive, both whole. Kiana takes his hands and holds them a "
      "moment, and she is the one who lets go first. Whatever they had been to one another, they were not that now, and "
      "neither of them pretended otherwise in front of a crowd.{/n}")],
    # No seelah.elan_dead forbid: that etude is Playing-only in Drezen (E3), and the aftermath dialog itself needs Elan alive.
    # Engine-q2: trickster.now, not the run latch. kiana.separated is set on every path, so the path is this edit's only
    # Trickster evidence, and the aftermath can play after a Chapter 4 failure or a Summit conversion (T6a).
    requires=("trickster.now", "kiana.separated"), forbids=("kiana.bereaved",), last=99, Relationship="kiana")]

# 6b (kiana.md, Polish residual 2): a ransom or a buy-back already brought every guest home (Arsinoe broke the stones in the ward),
# so native Q3 would recover them a second time. Read only, warning-only, Trickster only.
# - JewelerFinal/Cue_0051 (Seelah pours the bowl of soul-gems into a pouch, "We have the souls..."): the settings are still in
#   Sunhammer's bowl, the sockets empty. The replacement keeps the cue's cutscene and quest steps (ReturnSouls is still given).
# - ElandKianaAftermath/Cue_0001 ("fall into each other's arms"): the couple has been awake since the ward; a second variant after
#   the separated line. Seelah's "Let's give them some space" still follows.
HOME_WORLDS = [["trickster.ever", kt.RANSOMED], ["trickster.ever", kt.BOUGHT]]
BOWL = "kiana.native.q3_bowl_emptied"
AFTERMATH_HOME = "kiana.native.aftermath_home"
CUE_0051 = "4255f49c18c69aa4ab4d5582d0b6f39e"
SCENES += [
    scene(BOWL, "", "KianaEpilogue", 3, "", [
        n("bowl", "Narrator", "{n}Seelah tips the bowl of jewelry into a pouch: rings, pendants, a bride's circlet, every setting from the "
          "wedding, and every socket in them empty. The stones were prised out and sold back to Drezen, and Arsinoe broke them there, "
          "one clean tap at a time.{/n} \"Empty. Every one of them. He kept the settings anyway, like receipts.\" {n}She closes the pouch "
          "all the same.{/n} \"Arsinoe will want these for her ledger. Let's go, {name}! I... don't want to stay here any longer.\"")],
        requires=("trickster.ever",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], last=99, Relationship="kiana"),
    scene(AFTERMATH_HOME, "", "KianaEpilogue", 3, "", [
        n("arms", "Narrator", "{n}Elan and Kiana are waiting at the front of the crowd. They have been awake since the night the stones "
          "were broken in the ward, and they have had time to be glad already; Kiana has his arm all the same, and does not let go "
          "of it, heedless of everyone else around them.{/n}")],
        requires=("trickster.ever",), RequiresAnyGroups=[[kt.RANSOMED, kt.BOUGHT]], forbids=("kiana.separated", "kiana.bereaved"),
        last=99, Relationship="kiana"),
]
NATIVE_EPILOGUE_EDITS = {
    "81109ea8fb20dbc478cf67116740f4a1": dict(Parent="27bc5f6c94108a446b8273800f7da48b", Dialog="27bc5f6c94108a446b8273800f7da48b",
                                             Key="b261aab4-14ff-41e7-bd72-21aeeab7df44", Replacement=AFTERMATH,
                                             When=[["trickster.now", "kiana.separated"]], KeepNativeImage=False,
                                             Variants=[dict(Replacement=AFTERMATH_HOME, When=HOME_WORLDS, KeepNativeImage=False)]),
    CUE_0051: dict(Parent="800706e8e47847f4e88e2c3c586706de", Dialog="fa5e885aaa9840f419939176d38d176b",
                   Key="8e4494ff-5209-44e1-9e80-98a8b9d2a6a9", Replacement=BOWL, When=HOME_WORLDS, KeepNativeImage=False, Variants=[]),
}

NATIVE_GATES = {
    "arsinoe.souls_search_answer": dict(Target="41d9638f7d971164fab4efdbbbffbe70", Relationship="kiana",
                                        When=[["trickster.ever", kt.RANSOMED], ["trickster.ever", kt.BOUGHT]]),
}


def integrate(payload):
    """Register the gates and the aftermath line (after kiana_trickster)."""
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    edits = payload.setdefault("NativeEpilogueEdits", {})
    for cue, spec in NATIVE_EPILOGUE_EDITS.items():
        if cue in edits:
            raise ValueError("kiana_native: conflicting native edit " + cue)
        edits[cue] = {k: ([list(g) for g in v] if k == "When" else
                          [dict(x, When=[list(g) for g in x["When"]]) for x in v] if k == "Variants" else v) for k, v in spec.items()}
    gates = payload.setdefault("NativeGates", {})
    for key, gate in NATIVE_GATES.items():
        if key in gates:
            raise ValueError("kiana_native: conflicting native gate " + key)
        gates[key] = dict(gate, When=[list(g) for g in gate["When"]])
