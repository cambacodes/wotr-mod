using System;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.Blueprints;
using Kingmaker.Controllers;
using Kingmaker.Controllers.Dialog;
using Kingmaker.Controllers.Units;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using UnityEngine;
using UnityEngine.Serialization;

namespace Kingmaker.DialogSystem;

[Serializable]
public class DialogSpeaker
{
	[CanBeNull]
	[SerializeField]
	[FormerlySerializedAs("Blueprint")]
	private BlueprintUnitReference m_Blueprint;

	public bool MoveCamera = true;

	public bool NotRevealInFoW;

	public bool NoSpeaker;

	public bool SwitchDual;

	[CanBeNull]
	[SerializeField]
	[FormerlySerializedAs("SpeakerPortrait")]
	private BlueprintUnitReference m_SpeakerPortrait;

	public BlueprintUnit Blueprint => m_Blueprint?.Get();

	public BlueprintUnit SpeakerPortrait => m_SpeakerPortrait?.Get();

	public bool NeedsEntity => Blueprint != null;

	[CanBeNull]
	public UnitEntityData GetSpeaker([CanBeNull] UnitEntityData defaultSpeaker, [CanBeNull] BlueprintCueBase cue = null)
	{
		if (NoSpeaker)
		{
			return null;
		}
		if (NeedsEntity)
		{
			return GetEntity(cue);
		}
		return defaultSpeaker;
	}

	[CanBeNull]
	public UnitEntityData GetEntity([CanBeNull] BlueprintCueBase cue = null)
	{
		if (Blueprint == null)
		{
			return null;
		}
		Vector3 dialogPosition = Game.Instance.DialogController.DialogPosition;
		IEnumerable<UnitEntityData> second = Game.Instance.EntityCreator.CreationQueue.Select((EntityCreationController.CreateEntry ce) => ce.Entity).OfType<UnitEntityData>();
		MakeEssentialCharactersConscious();
		UnitEntityData unitEntityData = (from u in Game.Instance.State.Units.Concat(Game.Instance.Player.Party)
			where u.IsInGame && !u.Suppressed
			select u).Concat(second).Select(SelectMatchingUnit).NotNull()
			.Distinct()
			.Nearest(dialogPosition);
		if (unitEntityData == null)
		{
			DialogDebug.Add(cue, "speaker doesnt exist", Color.red);
			return null;
		}
		return unitEntityData;
	}

	[CanBeNull]
	private UnitEntityData SelectMatchingUnit(UnitEntityData unit)
	{
		UnitEntityData unitEntityData = null;
		if (unit.Blueprint == Blueprint)
		{
			unitEntityData = unit;
		}
		else if (SwitchDual)
		{
			UnitEntityData pair = UnitPartDualCompanion.GetPair(unit);
			if (pair != null && pair.Blueprint == Blueprint)
			{
				unitEntityData = pair;
			}
		}
		if (unitEntityData != null && (unitEntityData.State.IsDead || unitEntityData.State.IsUnconscious) && !unitEntityData.State.IsFinallyDead)
		{
			UnitReturnToConsciousController.MakeUnitConscious(unitEntityData);
			UnitLifeController.ForceTickOnUnit(unitEntityData);
		}
		if (!(unitEntityData == null) && !unitEntityData.State.IsDead)
		{
			return unitEntityData;
		}
		return null;
	}

	private void MakeEssentialCharactersConscious()
	{
		foreach (UnitEntityData item in Game.Instance.Player.Party)
		{
			if (item.Blueprint == Blueprint && item.Descriptor.IsEssentialForGame && (item.Descriptor.State.IsDead || item.Descriptor.State.IsUnconscious))
			{
				UnitReturnToConsciousController.MakeUnitConscious(item);
				UnitLifeController.ForceUnitConscious(item);
			}
		}
	}
}
