"""Chivarro's confirmed death (Writer/handoffs/trickster/chivarro.md, Provenance: the ChivarroKilled split).

ChivarroKilled (fd2ab9b6, bound as `chivarro.dead`) has two native producers (blueprints.zip, 2026-10-03):
- ChivarroWasTeleportedAway's EvaluatedUnitDeathTrigger "Chivarro death" (spawner ChivarroAttacked 5d051d3f): StartEtude
  ChivarroKilled, SetObjectiveStatus Complete on AvengeInsults/Obj3_ExiledChivarro (7ce588c0), GiveObjective
  Obj4_ReturnToHerraxa (c484e749). This is the death.
- ChivarroAbusedScene's gate f6b3213f, CommandAction 1 (0e1214a5): StartEtude ChivarroKilled alone, when the to-the-death
  fight begins. No death yet.
Obj3_ExiledChivarro is completed by nothing else: Herraxa_dialogue/Cue_0045_KillChivarro only gives it, and Answer_0046
("Chivarro is dead.", shown while ChivarroKilled plays) completes Obj4, not Obj3. A finished quest fails its unfinished
objectives (QuestObjective.TryFailOnQuestFinished); it never completes them.

So the confirmed death is ChivarroKilled AND Obj3 Completed. `chivarro.dead` keeps its meaning (the etude, which old saves
already hold either way); this module only adds the read-only keys. Switching scenes to `chivarro.dead_confirmed` is left
to the Minagho/Chivarro polish (see the list in the engine-queue report).
"""

EXILE_DONE = "chivarro.exile_objective_done"    # QuestObjectives AvengeInsults/Obj3_ExiledChivarro 7ce588c0, Completed
CONFIRMED = "chivarro.dead_confirmed"           # Derived: ChivarroKilled + Obj3 completed (the death trigger fired)
OBJ3 = "7ce588c0d2e296b41be4f754edbe60d3"

QUEST_OBJECTIVES = {EXILE_DONE: [OBJ3, "Completed"]}
DERIVED = {CONFIRMED: [["chivarro.dead", EXILE_DONE]]}


def integrate(payload):
    """Bind the objective read and the derived key (after trickster_world, which binds chivarro.dead)."""
    if "chivarro.dead" not in (payload.get("Etudes") or {}):
        return   # nothing reads ChivarroKilled in this build
    objectives = payload.setdefault("QuestObjectives", {})
    for key, value in QUEST_OBJECTIVES.items():
        if objectives.get(key, value) != value:
            raise ValueError("chivarro_death: conflicting QuestObjectives binding " + key)
        objectives[key] = list(value)
    derived = payload.setdefault("Derived", {})
    for key, groups in DERIVED.items():
        if derived.get(key) not in (None, groups):
            raise ValueError("chivarro_death: conflicting derived key " + key)
        derived[key] = [list(g) for g in groups]
