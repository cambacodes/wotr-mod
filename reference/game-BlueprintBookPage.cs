using System.Collections.Generic;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Kingmaker.ResourceLinks;
using UnityEngine;

namespace Kingmaker.DialogSystem.Blueprints;

[TypeId("b6d078a4ae218fe4a82f3fb5707b7e1f")]
public class BlueprintBookPage : BlueprintCueBase
{
	public List<BlueprintCueBaseReference> Cues = new List<BlueprintCueBaseReference>();

	public List<BlueprintAnswerBaseReference> Answers = new List<BlueprintAnswerBaseReference>();

	public ActionList OnShow;

	public SpriteLink ImageLink;

	[Header("Interchapter Additional Properties")]
	public SpriteLink ForeImageLink;

	public LocalizedString Title;
}
