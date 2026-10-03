"""Devarra's native egg line in the flight world (engine queue 9a; Writer/handoffs/trickster/devarra.md, escalated item 1).

c3/IvorySanctum/DragonEggs/Cue_0007 says the eggs were "most likely laid by the dragon you killed". In the flight world
(devarra.trickster.flown: the pact struck and she escaped) nobody killed her. E14i on a non-epilogue dialog cue: the
replacement is inserted before Cue_0007 in Answer_0004's NextCue ([Examine the eggs]), keeps its answer list, and plays only
while the flight world holds and its scene is available. Read only, warning-only. Save name native-edit.<cue>.
"""
import copy

from story_format import n, scene

from storylines import devarra_trickster as dt

CUE_0007 = "164c14743ee768f409a04f93a040e678"
EGGS = "devarra.trickster.native.eggs_flown"
PACT = dt.P + "flight.pact"

SCENES = [scene(EGGS, "", "DevarraEpilogue", 3, "", [
    n("eggs", "Narrator", "{n}You don't need to be an expert in magical creatures to know that these are dragon eggs, laid by the "
      "dragon who is no longer here. She flew without them.{/n}")],
    requires=("trickster.ever", PACT, dt.FLOWN), last=99, Relationship="devarra")]

NATIVE_EPILOGUE_EDITS = {
    CUE_0007: dict(Parent="2330b54637738fe4fb92b6cd80eb68f7", Dialog="63f11843f40edd54795fcc0af3f6a20e",
                   Key="8e520736-4eaa-4077-aea9-6e4b9a05e854", Replacement=EGGS,
                   When=[["trickster.ever", PACT, dt.FLOWN]], KeepNativeImage=False, Variants=[]),
}


def integrate(payload):
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    edits = payload.setdefault("NativeEpilogueEdits", {})
    for cue, spec in NATIVE_EPILOGUE_EDITS.items():
        if cue in edits:
            raise ValueError("devarra_native: conflicting native edit " + cue)
        edits[cue] = {k: ([list(g) for g in v] if k == "When" else v) for k, v in spec.items()}
