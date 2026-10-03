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


# 9c (devarra.md, residual c): once she has taken her clutch (the flight return's "paid" / "owe", devarra.trickster.clutch_collected),
# the native egg interaction (DragonEggs_Dialogue, opened by EnableEggDialog b88c5631) stays shut: an E18 gate on the dialog's own
# condition. Warning-only. The eggs' native fates (omelet, druids, project, destroyed) already close it natively.
NATIVE_GATES = {
    "dragon_eggs.dialog": dict(Target="63f11843f40edd54795fcc0af3f6a20e", Relationship="devarra", When=[["trickster.ever", dt.COLLECTED]]),
}

# 9b (escalated 2): Greybor's Obj5A "Track down and kill the dragon in the Ivory Sanctum" (given by the RedDragon_Fly entrance cutscene)
# completes only when the Sanctum dragon dies. In the flight world she is not there (the E18 spawn gate), so once the Commander has
# stood in the egg chamber (Golems Cue_0006) the objective is failed: the hunt is over, nobody killed her. E19, failed never
# completed (no experience, no "tell Irabeth the dragon is dead"); the quest stays open and the native interchapter ends it.
NATIVE_OBJECTIVE_SETTLEMENTS = {
    "greybor.dragon_hunt.sanctum": dict(Target="fde08188fb6cf654a80cc3f30c3fb5a8", Relationship="devarra",
                                        When=[["trickster.ever", dt.FLOWN, dt.GOLEMS_MET]]),
}


def integrate(payload):
    payload["Scenes"].extend(copy.deepcopy(SCENES))
    gates = payload.setdefault("NativeGates", {})
    for key, gate in NATIVE_GATES.items():
        if key in gates:
            raise ValueError("devarra_native: conflicting native gate " + key)
        gates[key] = dict(gate, When=[list(g) for g in gate["When"]])
    settled = payload.setdefault("NativeObjectiveSettlements", {})
    for key, spec in NATIVE_OBJECTIVE_SETTLEMENTS.items():
        if key in settled:
            raise ValueError("devarra_native: conflicting objective settlement " + key)
        settled[key] = dict(spec, When=[list(g) for g in spec["When"]])
    edits = payload.setdefault("NativeEpilogueEdits", {})
    for cue, spec in NATIVE_EPILOGUE_EDITS.items():
        if cue in edits:
            raise ValueError("devarra_native: conflicting native edit " + cue)
        edits[cue] = {k: ([list(g) for g in v] if k == "When" else v) for k, v in spec.items()}
