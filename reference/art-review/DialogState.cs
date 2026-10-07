using System.Collections.Generic;
using JetBrains.Annotations;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Newtonsoft.Json;

namespace Kingmaker.DialogSystem.State;

[JsonObject]
public class DialogState
{
	[JsonProperty]
	public readonly HashSet<BlueprintAnswer> SelectedAnswers = new HashSet<BlueprintAnswer>();

	[JsonProperty]
	public readonly Dictionary<BlueprintAnswer, CheckResult> AnswerChecks = new Dictionary<BlueprintAnswer, CheckResult>();

	[JsonProperty]
	public readonly HashSet<BlueprintAnswersList> ShownAnswerLists = new HashSet<BlueprintAnswersList>();

	[JsonProperty]
	public readonly HashSet<BlueprintCueBase> ShownCues = new HashSet<BlueprintCueBase>();

	[JsonProperty]
	public readonly HashSet<BlueprintDialog> ShownDialogs = new HashSet<BlueprintDialog>();

	[JsonProperty]
	[CanBeNull]
	public StartDialogData Scheduled { get; set; }
}
You are not using the latest version of the tool, please update.
Latest version is '11.1.0.9782' (yours is '9.1.0.7988')
