using System.Collections.Generic;
using System.Text;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ResourceLinks;
using Kingmaker.UI.MVVM._VM.Dialog.BookEvent;
using Kingmaker.UI.MVVM._VM.Dialog.Dialog;
using Kingmaker.UI.MVVM._VM.Tooltip.Utils;
using Kingmaker.UnitLogic.Alignments;
using UniRx;

namespace Kingmaker.UI.MVVM._VM.Dialog.Interchapter;

public class InterchapterVM : BookEventVM
{
	public IReactiveProperty<string> Title { get; } = new ReactiveProperty<string>();

	public bool IsEpilogue { get; }

	public InterchapterVM(bool isEpilogue)
	{
		IsEpilogue = isEpilogue;
		Title.Value = string.Empty;
		TooltipHelper.HideTooltip();
		TooltipHelper.HideInfo();
	}

	protected override void SetPage(BlueprintBookPage page, List<CueShowData> cues, List<BlueprintAnswer> answers)
	{
		base.SetPage(page, cues, answers);
		SetTitle(page);
	}

	private void SetTitle(BlueprintBookPage page)
	{
		string value = page.Title;
		Title.Value = value;
	}

	protected override void SetCues(List<CueShowData> cues)
	{
		StringBuilder stringBuilder = new StringBuilder();
		foreach (CueShowData cue in cues)
		{
			stringBuilder.AppendLine(cue.Cue.DisplayText);
		}
		base.Cues.Add(new CueVM(stringBuilder.ToString(), new List<SkillCheckResult>(), new List<AlignmentShift>()));
	}

	protected override void SetMirror(BlueprintBookPage page)
	{
		if (IsEpilogue)
		{
			SpriteLink foreImageLink = page.ForeImageLink;
			if ((object)foreImageLink != null && foreImageLink.Exists())
			{
				Mirror.Value = page.ForeImageLink.Load();
			}
			else
			{
				Mirror.Value = Game.Instance.Player.MainCharacter.Value.Portrait.FullLengthPortrait;
			}
		}
	}
}
