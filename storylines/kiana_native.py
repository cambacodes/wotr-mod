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
    requires=("kiana.separated",), forbids=("kiana.bereaved",), last=99, Relationship="kiana")]
NATIVE_EPILOGUE_EDITS = {
    "81109ea8fb20dbc478cf67116740f4a1": dict(Parent="27bc5f6c94108a446b8273800f7da48b", Dialog="27bc5f6c94108a446b8273800f7da48b",
                                             Key="b261aab4-14ff-41e7-bd72-21aeeab7df44", Replacement=AFTERMATH,
                                             When=[["kiana.separated"]], KeepNativeImage=False, Variants=[]),
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
        edits[cue] = {k: ([list(g) for g in v] if k == "When" else v) for k, v in spec.items()}
    gates = payload.setdefault("NativeGates", {})
    for key, gate in NATIVE_GATES.items():
        if key in gates:
            raise ValueError("kiana_native: conflicting native gate " + key)
        gates[key] = dict(gate, When=[list(g) for g in gate["When"]])
