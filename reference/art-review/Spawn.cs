using System.Collections.Generic;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence.Versioning;
using Kingmaker.Utility;
using Kingmaker.View.Spawners;

namespace Kingmaker.Designers.EventConditionActionSystem.Actions;

[ComponentName("Actions/Spawn")]
[AllowMultipleComponents]
[TypeId("0652c1b85291c994f8411a22deb2b6ec")]
[PlayerUpgraderAllowed(true)]
public class Spawn : GameAction
{
	[AllowedEntityType(typeof(UnitSpawnerBase))]
	public EntityReference[] Spawners;

	public ActionList ActionsOnSpawn;

	[InfoBox("By default dead units are not respawned. This option ignores RespawnIfDead on spawner")]
	public bool RespawnIfDead;

	public List<UnitSpawnerBase> SpawnerBases { get; private set; }

	public override void RunAction()
	{
		SpawnerBases = SpawnerBases ?? new List<UnitSpawnerBase>();
		EntityReference[] spawners = Spawners;
		for (int i = 0; i < spawners.Length; i++)
		{
			UnitSpawnerBase unitSpawner = GameHelper.GetUnitSpawner(spawners[i]);
			if (unitSpawner == null)
			{
				continue;
			}
			SpawnerBases.Add(unitSpawner);
			UnitEntityData unitEntityData = (RespawnIfDead ? unitSpawner.TrySpawnOrRespawn() : unitSpawner.Spawn());
			if (!(unitEntityData == null))
			{
				using (ContextData<SpawnedUnitData>.Request().Setup(unitEntityData, unitSpawner.Data.HoldingState))
				{
					ActionsOnSpawn.Run();
				}
			}
		}
	}

	public override string GetCaption()
	{
		string text = "";
		if (Spawners != null)
		{
			for (int i = 0; i < Spawners.Length; i++)
			{
				if (i != 0)
				{
					text += ", ";
				}
				if (Spawners[i] != null)
				{
					text += Spawners[i].EntityNameInEditor;
				}
			}
		}
		return "Spawn( " + text + " )";
	}
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
