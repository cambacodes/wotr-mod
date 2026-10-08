using System;
using System.Collections.Generic;
using System.Linq;
using JetBrains.Annotations;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Classes.Experience;
using Kingmaker.Blueprints.Root;
using Kingmaker.Controllers.Combat;
using Kingmaker.Controllers.Units;
using Kingmaker.Designers;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.ContextData;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Enums;
using Kingmaker.GameModes;
using Kingmaker.Localization;
using Kingmaker.PubSubSystem;
using Kingmaker.QA;
using Kingmaker.ResourceLinks;
using Kingmaker.RuleSystem.Rules;
using Kingmaker.UnitLogic.Abilities.Components;
using Kingmaker.UnitLogic.Alignments;
using Kingmaker.UnitLogic.Parts;
using Kingmaker.Utility;
using Kingmaker.View;
using Kingmaker.View.MapObjects;
using Kingmaker.Visual.Animation.Actions;
using Kingmaker.Visual.Animation.Kingmaker;
using Kingmaker.Visual.Sound;
using Owlcat.Runtime.Core.Logging;
using Owlcat.Runtime.Core.Utils;
using UnityEngine;

namespace Kingmaker.Controllers.Dialog;

public class DialogController : IController, IControllerStart, IControllerStop, IAreaHandler, IGlobalSubscriber, ISubscriber
{
	private class MakeSpeakersNotRequiredClass : IDisposable
	{
		public MakeSpeakersNotRequiredClass()
		{
			IgnoreRequiredSpeakers = true;
		}

		public void Dispose()
		{
			IgnoreRequiredSpeakers = false;
		}
	}

	private class InterceptBookPageImageChange : ChangeBookEventImage.IHandler, IGlobalSubscriber, ISubscriber
	{
		private SpriteLink m_Image;

		public void OnImageChanged(SpriteLink image)
		{
			m_Image = image;
		}

		public void RunAction()
		{
			if (!(m_Image == null))
			{
				SpriteLink img = m_Image;
				EventBus.RaiseEvent(delegate(ChangeBookEventImage.IHandler h)
				{
					h.OnImageChanged(img);
				});
			}
		}
	}

	private BlueprintCue m_CurrentCue;

	private FogOfWarRevealerSettings m_RevealedSpeaker;

	private bool m_HeadlessMode;

	public BlueprintDialog Dialog;

	public bool AutosaveDialogStart;

	private string m_CustomSpeakerName;

	private string m_CustomSpeakerColor;

	private bool m_CapitalPartyChecksEnabled;

	public Vector3 DialogPosition;

	[NotNull]
	public HashSet<UnitEntityData> InvolvedUnits = new HashSet<UnitEntityData>();

	private readonly List<BlueprintAnswer> m_Answers = new List<BlueprintAnswer>();

	[CanBeNull]
	private BlueprintCueBase m_ContinueCue;

	[NotNull]
	public readonly HashSet<BlueprintCueBase> LocalShownCues = new HashSet<BlueprintCueBase>();

	[NotNull]
	public readonly HashSet<BlueprintAnswer> LocalSelectedAnswers = new HashSet<BlueprintAnswer>();

	[NotNull]
	public readonly HashSet<BlueprintAnswersList> LocalShownAnswerLists = new HashSet<BlueprintAnswersList>();

	[NotNull]
	public readonly HashSet<BlueprintCheck> LocalPassedChecks = new HashSet<BlueprintCheck>();

	[NotNull]
	public readonly HashSet<BlueprintCheck> LocalFailedChecks = new HashSet<BlueprintCheck>();

	private BlueprintCueBase m_CueToPlay;

	private bool m_CuePlayScheduled;

	private bool m_DialogStopScheduled;

	private int m_CuesPlayedThisFrame;

	private int m_PlayingBookPageCount;

	private readonly List<CueShowData> m_BookPageCues = new List<CueShowData>();

	[NotNull]
	private readonly Stack<CueSequence> m_Sequences = new Stack<CueSequence>();

	[NotNull]
	private List<SkillCheckResult> m_SkillChecks = new List<SkillCheckResult>();

	[NotNull]
	public List<AlignmentShift> AlignmentShifts = new List<AlignmentShift>();

	private Alignment m_OldPlayerAlignment;

	private float m_FirstSpeakerReturnOrientation;

	private UnitAnimationActionHandle m_CurrentSpeakerAnimation;

	public BlueprintCue CurrentCue
	{
		get
		{
			return m_CurrentCue;
		}
		private set
		{
			CameraRig cameraRig = Game.Instance.UI.GetCameraRig();
			bool flag = false;
			if (m_CurrentCue != null)
			{
				m_CurrentCue.OnStop.Run();
				if (m_CurrentCue.Speaker.MoveCamera && cameraRig.Mode == CameraMode.Default)
				{
					cameraRig.ScrollTo(DialogPosition);
				}
			}
			else
			{
				flag = true;
			}
			if (m_CurrentSpeakerAnimation != null)
			{
				m_CurrentSpeakerAnimation.Release();
				m_CurrentSpeakerAnimation = null;
			}
			m_CurrentCue = value;
			if (m_CurrentCue != null)
			{
				UnitEntityData currentSpeaker = CurrentSpeaker;
				CurrentSpeaker = m_CurrentCue.Speaker.GetSpeaker(FirstSpeaker);
				SwitchSpeakerIn(CurrentSpeaker);
				PlayAnimation(CurrentSpeaker, m_CurrentCue.Animation);
				AddInvolvedUnit(CurrentSpeaker);
				if (!m_CurrentCue.Speaker.NotRevealInFoW && CurrentSpeaker != null && CurrentSpeaker.IsInGame && !CurrentSpeaker.InStealthFor(Game.Instance.Player.Group))
				{
					if (flag || CurrentSpeaker != currentSpeaker)
					{
						TurnOffSpeakerHighlight();
						FogOfWarRevealerSettings fogOfWarRevealerSettings = CurrentSpeaker.View.FogOfWarRevealer;
						if (fogOfWarRevealerSettings == null)
						{
							fogOfWarRevealerSettings = (m_RevealedSpeaker = CurrentSpeaker.View.gameObject.EnsureComponent<FogOfWarRevealerSettings>());
							fogOfWarRevealerSettings.Reveal();
							fogOfWarRevealerSettings.DefaultRadius = false;
							fogOfWarRevealerSettings.Radius = 1f;
						}
						if (!fogOfWarRevealerSettings.enabled)
						{
							fogOfWarRevealerSettings.Enable();
							fogOfWarRevealerSettings.DefaultRadius = false;
							fogOfWarRevealerSettings.Radius = 1f;
						}
					}
				}
				else
				{
					TurnOffSpeakerHighlight();
				}
				if (m_CurrentCue.TurnSpeaker)
				{
					TurnUnit(CurrentSpeaker, m_CurrentCue.Listener);
				}
				if (m_CurrentCue.Speaker.MoveCamera && CurrentSpeaker != null && cameraRig.Mode == CameraMode.Default)
				{
					cameraRig.ScrollTo(CurrentSpeaker.Position);
				}
				m_CurrentCue.OnShow.Run();
			}
			else
			{
				TurnOffSpeakerHighlight();
			}
		}
	}

	[CanBeNull]
	public UnitEntityData Initiator { get; private set; }

	[CanBeNull]
	public UnitEntityData FirstSpeaker { get; private set; }

	[CanBeNull]
	public UnitEntityData CurrentSpeaker { get; private set; }

	[CanBeNull]
	public MapObjectView MapObject { get; private set; }

	[CanBeNull]
	public UnitEntityData ActingUnit { get; private set; }

	public string CurrentSpeakerName
	{
		get
		{
			if (CurrentCue != null && CurrentCue.Speaker.SpeakerPortrait != null)
			{
				return CurrentCue.Speaker.SpeakerPortrait.CharacterName;
			}
			if (CurrentSpeaker != null)
			{
				return CurrentSpeaker.CharacterName;
			}
			if (!string.IsNullOrEmpty(m_CustomSpeakerName) && m_CustomSpeakerName != "<null>")
			{
				return m_CustomSpeakerName;
			}
			return string.Empty;
		}
	}

	public BlueprintUnit CurrentSpeakerBlueprint
	{
		get
		{
			if (CurrentCue != null && CurrentCue.Speaker.SpeakerPortrait != null)
			{
				return CurrentCue.Speaker.SpeakerPortrait;
			}
			if (CurrentSpeaker != null)
			{
				return CurrentSpeaker.Blueprint;
			}
			return null;
		}
	}

	public string CurrentSpeakerColor
	{
		get
		{
			BlueprintUnit currentSpeakerBlueprint = CurrentSpeakerBlueprint;
			if (currentSpeakerBlueprint != null)
			{
				return ColorUtility.ToHtmlStringRGB(currentSpeakerBlueprint.Color);
			}
			return m_CustomSpeakerColor;
		}
	}

	public IEnumerable<BlueprintAnswer> Answers => m_Answers;

	private bool PlayingBookPage => m_PlayingBookPageCount > 0;

	public static bool IgnoreRequiredSpeakers { get; private set; }

	private static bool PreventDialogStart => Game.Instance.IsModeActiveOrActivateSoon(GameModeType.Rest);

	public DialogController(bool headlessMode)
	{
		m_HeadlessMode = headlessMode;
	}

	public void Tick()
	{
		if (Dialog == null)
		{
			StopDialog();
		}
		else if (m_CuePlayScheduled)
		{
			m_CuesPlayedThisFrame = 0;
			m_CuePlayScheduled = false;
			PlayCue(m_CueToPlay);
		}
		m_DialogStopScheduled = false;
	}

	public void SetHeadlessMode(bool enabled)
	{
		m_HeadlessMode = enabled;
	}

	public void StartDialogWithUnit([NotNull] BlueprintDialog dialog, [NotNull] UnitEntityData unit, [CanBeNull] UnitEntityData initiator = null)
	{
		StartDialog(dialog, initiator, unit, null, null);
	}

	public void StartDialogWithMapObject([NotNull] BlueprintDialog dialog, [NotNull] MapObjectView mapObject, [CanBeNull] LocalizedString speakerName, [CanBeNull] UnitEntityData initiator = null)
	{
		StartDialog(dialog, initiator, null, mapObject, speakerName);
	}

	public void StartDialogWithoutTarget([NotNull] BlueprintDialog dialog, [CanBeNull] LocalizedString speakerName, [CanBeNull] UnitEntityData initiator = null)
	{
		StartDialog(dialog, initiator, null, null, speakerName);
	}

	private void StartDialog([NotNull] BlueprintDialog dialog, [CanBeNull] UnitEntityData initiator, [CanBeNull] UnitEntityData unit, [CanBeNull] MapObjectView mapObject, [CanBeNull] LocalizedString customSpeakerName)
	{
		PFLog.Default.Log(dialog, $"Requested dialog start {dialog}");
		StartDialogData scheduled = Game.Instance.Player.Dialog.Scheduled;
		if (scheduled != null)
		{
			PFLog.Default.Error($"Another dialog already scheduled! (current: {dialog}, scheduled: {scheduled.Dialog.name})");
		}
		if (AutosaveDialogStart)
		{
			SaveManager saveManager = Game.Instance.SaveManager;
			SaveInfo dialogSaveSlot = saveManager.GetDialogSaveSlot();
			LoadingProcess.Instance.StartLoadingProcess(saveManager.SaveRoutine(dialogSaveSlot), null, LoadingProcessTag.Save);
		}
		Game.Instance.Player.Dialog.Scheduled = new StartDialogData
		{
			Dialog = dialog,
			Initiator = initiator,
			Unit = unit,
			MapObject = mapObject?.Data,
			CustomSpeakerName = customSpeakerName
		};
		if (!PreventDialogStart)
		{
			StartScheduledDialog();
		}
	}

	public void StartScheduledDialog()
	{
		StartDialogData scheduled = Game.Instance.Player.Dialog.Scheduled;
		if (scheduled == null)
		{
			PFLog.Default.Error("Has no scheduled dialog");
			return;
		}
		if (scheduled.IsScheduled)
		{
			PFLog.Default.Error("Dialog already scheduled");
			return;
		}
		scheduled.IsScheduled = true;
		if (m_HeadlessMode)
		{
			StartScheduledDialogImmediately();
		}
		else
		{
			Game.Instance.ScheduleAction(StartScheduledDialogImmediately);
		}
	}

	private void StartScheduledDialogImmediately()
	{
		if (PreventDialogStart)
		{
			return;
		}
		StartDialogData scheduled = Game.Instance.Player.Dialog.Scheduled;
		Game.Instance.Player.Dialog.Scheduled = null;
		if (scheduled == null)
		{
			PFLog.Default.Error("Has no scheduled dialog");
			return;
		}
		if (Game.Instance.IsModeActive(GameModeType.Dialog))
		{
			PFLog.Default.Error("Trying to start dialog twice");
			return;
		}
		if (Game.Instance.Player.GameOverReason.HasValue)
		{
			PFLog.Default.Error("Trying to start dialog when the game is over");
			return;
		}
		Game.Instance.ProjectileController.Clear();
		Clear();
		Dialog = scheduled.Dialog;
		Initiator = scheduled.Initiator;
		FirstSpeaker = scheduled.Unit;
		CurrentSpeaker = scheduled.Unit;
		MapObject = (MapObjectView)scheduled.MapObject.FindView();
		m_CustomSpeakerName = scheduled.CustomSpeakerName;
		m_CustomSpeakerColor = CurrentSpeakerColor;
		DialogDebug.Init(Dialog);
		PFLog.Default.Log(Dialog, $"Trying to start dialog {Dialog}");
		FillStartPosition();
		bool flag = true;
		if (!Dialog.Conditions.Check(Dialog))
		{
			flag = false;
			DialogDebug.Add(Dialog, "start conditions failed", Color.red);
		}
		BlueprintCueBase blueprintCueBase = Dialog.FirstCue.Select();
		if (blueprintCueBase == null)
		{
			flag = false;
			DialogDebug.Add(Dialog, "could not select first cue", Color.red);
		}
		if (FirstSpeaker != null)
		{
			CutscenePlayerView controllingPlayer = CutsceneControlledUnit.GetControllingPlayer(FirstSpeaker);
			if (controllingPlayer != null && controllingPlayer.Cutscene.ForbidDialogs)
			{
				flag = false;
				DialogDebug.Add(Dialog, $"first speaker {FirstSpeaker.Blueprint} is busy in cutscene {controllingPlayer.Cutscene} ({controllingPlayer.Cutscene.AssetGuid})", Color.red);
			}
		}
		if (blueprintCueBase is BlueprintBookPage page && !CanShowAnyCue(page))
		{
			flag = false;
			DialogDebug.Add(Dialog, "could not show any cue", Color.red);
		}
		using ((FirstSpeaker != null) ? ContextData<ClickedUnitData>.Request().Setup(FirstSpeaker) : null)
		{
			using ((MapObject != null) ? ContextData<MapObjectData>.Request().Setup(MapObject.Data) : null)
			{
				if (!flag)
				{
					BlueprintDialog dialog = Dialog;
					dialog.ReplaceActions.Run();
					Clear();
					EventBus.RaiseEvent(delegate(IDialogFinishHandler h)
					{
						h.HandleDialogFinished(dialog, success: false);
					});
					return;
				}
				Dialog.StartActions.Run();
			}
		}
		AddInvolvedUnit(scheduled.Unit);
		AddInvolvedUnit(scheduled.Initiator);
		if (FirstSpeaker != null && Initiator != null)
		{
			m_FirstSpeakerReturnOrientation = FirstSpeaker.DesiredOrientation;
			if (Dialog.TurnFirstSpeaker)
			{
				TurnUnit(FirstSpeaker, null);
			}
		}
		m_OldPlayerAlignment = Game.Instance.Player.Alignment;
		if (!m_HeadlessMode)
		{
			EventBus.RaiseEvent(delegate(INewServiceWindowUIHandler h)
			{
				h.HandleCloseAll();
			});
			EventBus.RaiseEvent(delegate(IVendorUIHandler h)
			{
				h.HandleTradeEnding();
			});
			CameraRig cameraRig = Game.Instance.UI.GetCameraRig();
			if ((bool)cameraRig && cameraRig.Mode == CameraMode.Default)
			{
				cameraRig.ScrollTo(DialogPosition);
			}
			Game.Instance.StartMode(GameModeType.Dialog);
			Game.Instance.ScheduleAction(delegate
			{
				if (Game.Instance.IsModeActive(GameModeType.Dialog))
				{
					EventBus.RaiseEvent(delegate(IDialogInteractionHandler h)
					{
						h.StartDialogInteraction();
					});
				}
			});
		}
		ScheduleCue(blueprintCueBase);
		DialogDebug.Add(Dialog, "Started dialog", Color.green);
		Game.Instance.Player.Dialog.ShownDialogs.Add(Dialog);
	}

	private void FillStartPosition()
	{
		bool flag = false;
		if (Dialog.StartPosition != null)
		{
			try
			{
				DialogPosition = Dialog.StartPosition.GetValue();
				flag = true;
			}
			catch (Exception ex)
			{
				PFLog.Default.Exception(ex, null);
			}
		}
		if (!flag)
		{
			if (FirstSpeaker != null)
			{
				DialogPosition = FirstSpeaker.Position;
			}
			else if (MapObject != null)
			{
				DialogPosition = MapObject.transform.position;
			}
			else if (Game.Instance.IsModeActive(GameModeType.GlobalMap))
			{
				DialogPosition = Game.Instance.UI.GetCameraRig().transform.position;
			}
			else
			{
				DialogPosition = Game.Instance.Player.MainCharacter.Value.Position;
			}
		}
	}

	private void ScheduleCue(BlueprintCueBase cue)
	{
		if (cue == null)
		{
			StopDialog();
			return;
		}
		m_CueToPlay = cue;
		m_CuePlayScheduled = true;
	}

	private void AddInvolvedUnit([CanBeNull] UnitEntityData unit)
	{
		if (!(unit == null))
		{
			if (CutsceneControlledUnit.GetControllingPlayer(unit) == null)
			{
				unit.Commands.InterruptAll();
			}
			unit.ForceExitStealth();
			InvolvedUnits.Add(unit);
		}
	}

	private void Clear()
	{
		Dialog = null;
		CurrentCue = null;
		ActingUnit = null;
		m_CapitalPartyChecksEnabled = false;
		m_CueToPlay = null;
		m_CuePlayScheduled = false;
		m_Answers.Clear();
		m_ContinueCue = null;
		m_Sequences.Clear();
		m_BookPageCues.Clear();
		m_SkillChecks.Clear();
		AlignmentShifts.Clear();
		InvolvedUnits.Clear();
		m_PlayingBookPageCount = 0;
		LocalShownCues.Clear();
		LocalSelectedAnswers.Clear();
		LocalShownAnswerLists.Clear();
		LocalPassedChecks.Clear();
		LocalFailedChecks.Clear();
		DialogPosition = Vector3.zero;
		TurnOffSpeakerHighlight();
	}

	private void TurnOffSpeakerHighlight()
	{
		if (m_RevealedSpeaker != null)
		{
			UnityEngine.Object.Destroy(m_RevealedSpeaker);
			m_RevealedSpeaker = null;
		}
	}

	public void StopDialog()
	{
		if (m_DialogStopScheduled)
		{
			return;
		}
		m_DialogStopScheduled = true;
		BlueprintDialog dialog = Dialog;
		if (!m_HeadlessMode)
		{
			Game.Instance.StopMode(GameModeType.Dialog);
			Game.Instance.ScheduleAction(delegate
			{
				try
				{
					EventBus.RaiseEvent(delegate(IDialogInteractionHandler h)
					{
						h.StopDialogInteraction();
					});
				}
				catch (Exception ex)
				{
					PFLog.Default.Exception(Dialog, ex, null);
				}
			});
		}
		if (FirstSpeaker != null && Initiator != null)
		{
			FirstSpeaker.DesiredOrientation = m_FirstSpeakerReturnOrientation;
		}
		foreach (UnitEntityData involvedUnit in InvolvedUnits)
		{
			StopDialogAnimations(involvedUnit);
		}
		Clear();
		dialog?.FinishActions.Run();
	}

	public void SelectAnswer(BlueprintAnswer answer, UnitEntityData manualUnitSelection = null)
	{
		if ((bool)AbilitySwitchDualCompanion.IsPlaying || CurrentCue == null)
		{
			return;
		}
		if (!answer.IsSystem() && !m_Answers.Contains(answer))
		{
			PFLog.Default.Error("Trying to select invalid dialog answer {0}", answer);
			return;
		}
		if (manualUnitSelection == null && answer.CharacterSelection.SelectionType == CharacterSelection.Type.Manual)
		{
			PFLog.Default.Error("A unit must be specified for selected answer. Answer: {0}", answer);
			return;
		}
		DialogDebug.Init(Dialog);
		AddHistoryEntry(CurrentCue, CurrentSpeakerName, CurrentSpeakerColor);
		AddHistoryEntry(answer);
		bool flag = !LocalSelectedAnswers.Contains(answer);
		if (!Game.Instance.Player.Dialog.SelectedAnswers.Contains(answer))
		{
			Game.Instance.Player.Dialog.SelectedAnswers.Add(answer);
		}
		if (flag)
		{
			LocalSelectedAnswers.Add(answer);
		}
		ActingUnit = answer.CharacterSelection.SelectUnit(answer, manualUnitSelection, forceManual: true);
		if (answer.CharacterSelection.SelectionType != CharacterSelection.Type.Keep)
		{
			m_CapitalPartyChecksEnabled = answer.CapitalPartyChecksEnabled;
		}
		answer.OnSelect.Run();
		answer.ApplyAlignmentShift();
		if (answer.Experience != DialogExperience.NoExperience && flag)
		{
			GameHelper.GainExperience(ExperienceHelper.GetDialogXp(answer.Experience, null, Dialog.OverrideAreaCR));
		}
		BlueprintCueBase blueprintCueBase = SelectNextCue(answer);
		if (blueprintCueBase == null)
		{
			StopDialog();
		}
		ScheduleCue(blueprintCueBase);
		EventBus.RaiseEvent(delegate(ISelectAnswerHandler h)
		{
			h.HandleSelectAnswer(answer);
		});
	}

	public bool NextCueHasNewAnswers([NotNull] BlueprintAnswer answer)
	{
		List<BlueprintCueBase> allNextCues = answer.NextCue.GetAllNextCues();
		if (allNextCues == null)
		{
			return false;
		}
		foreach (BlueprintCueBase item in allNextCues)
		{
			if (item is BlueprintCue blueprintCue && blueprintCue.HasNewAnswers())
			{
				return true;
			}
		}
		return false;
	}

	public bool NextCueWasShown([NotNull] BlueprintAnswer answer)
	{
		List<BlueprintCueBase> allNextCues = answer.NextCue.GetAllNextCues();
		if (allNextCues == null)
		{
			return false;
		}
		foreach (BlueprintCueBase item2 in allNextCues)
		{
			if (item2 is BlueprintCue item && Game.Instance.Player.Dialog.ShownCues.Contains(item))
			{
				return true;
			}
		}
		return false;
	}

	[CanBeNull]
	private BlueprintCueBase SelectNextCue([NotNull] BlueprintAnswer answer)
	{
		if (answer.IsContinue())
		{
			if (m_ContinueCue == null)
			{
				PFLog.Default.Error("Continue answer was selected but continue cue is not specified");
			}
			return m_ContinueCue;
		}
		if (answer.IsExit())
		{
			return null;
		}
		BlueprintCueBase blueprintCueBase = answer.NextCue.Select();
		if (blueprintCueBase == null && m_Sequences.Any())
		{
			CueSequence cueSequence = m_Sequences.Peek();
			blueprintCueBase = cueSequence.PollNextCue();
			if (blueprintCueBase == null)
			{
				m_Sequences.Pop();
				blueprintCueBase = cueSequence.Blueprint.Exit?.Continue.Select();
			}
		}
		return blueprintCueBase;
	}

	private void AddHistoryEntry([NotNull] BlueprintAnswer answer)
	{
		if (answer.AddToHistory)
		{
			string line;
			if (Dialog.Type == DialogType.Common)
			{
				string answerFormatWithColorName = DialogFormats.AnswerFormatWithColorName;
				string characterName = GameHelper.GetPlayerCharacter().CharacterName;
				string arg = ColorUtility.ToHtmlStringRGB(GameHelper.GetPlayerCharacter().Blueprint.Color);
				line = string.Format(answerFormatWithColorName, arg, characterName, answer.Text);
			}
			else
			{
				string answerFormatWithoutName = DialogFormats.AnswerFormatWithoutName;
				line = string.Format(answerFormatWithoutName, answer.Text);
			}
			EventBus.RaiseEvent(delegate(IDialogHandler h)
			{
				h.HandleOnDialogHistory(line);
			});
		}
	}

	private void AddHistoryEntry([NotNull] BlueprintCue cue, string speakerName, string speakerColor)
	{
		string line;
		if (!string.IsNullOrEmpty(speakerName))
		{
			if (!string.IsNullOrEmpty(speakerColor))
			{
				line = string.Format(DialogFormats.SpeakerFormatWithColorName, "", speakerColor, speakerName, cue.DisplayText, ColorUtility.ToHtmlStringRGB(BlueprintRoot.Instance.UIRoot.DialogColors.Narrator));
			}
			else
			{
				line = string.Format(DialogFormats.SpeakerFormatWithName, "", speakerName, cue.DisplayText, ColorUtility.ToHtmlStringRGB(BlueprintRoot.Instance.UIRoot.DialogColors.Narrator));
			}
		}
		else
		{
			line = string.Format(DialogFormats.NarratorsTextFormat, cue.DisplayText);
		}
		EventBus.RaiseEvent(delegate(IDialogHandler h)
		{
			h.HandleOnDialogHistory(line);
		});
	}

	private void PlayCue(BlueprintCueBase cue)
	{
		if (m_CuesPlayedThisFrame++ > 1000)
		{
			throw new InvalidOperationException($"Stack overflow while playing dialog cues. Dialog: {Dialog}, One of cues: {cue}");
		}
		if (cue == null)
		{
			StopDialog();
			return;
		}
		LocalShownCues.Add(cue);
		Game.Instance.Player.Dialog.ShownCues.Add(cue);
		m_Answers.Clear();
		m_ContinueCue = null;
		DialogDebug.Add(cue, "played", Color.green);
		if (cue is BlueprintCue)
		{
			PlayBasicCue((BlueprintCue)cue);
		}
		if (cue is BlueprintCheck)
		{
			PlayCheck((BlueprintCheck)cue);
		}
		if (cue is BlueprintCueSequence)
		{
			PlaySequence((BlueprintCueSequence)cue);
		}
		if (cue is BlueprintBookPage)
		{
			PlayBookPage((BlueprintBookPage)cue);
		}
	}

	private void AddAnswers([NotNull] IEnumerable<BlueprintAnswerBase> answers, [CanBeNull] BlueprintCueBase continueCue)
	{
		if (continueCue == null)
		{
			foreach (BlueprintAnswerBase answer in answers)
			{
				if (answer is BlueprintAnswersList blueprintAnswersList && blueprintAnswersList.CanSelect())
				{
					Game.Instance.Player.Dialog.ShownAnswerLists.Add(blueprintAnswersList);
					LocalShownAnswerLists.Add(blueprintAnswersList);
					AddAnswers(blueprintAnswersList.Answers.Dereference(), continueCue);
					return;
				}
			}
		}
		m_Answers.Clear();
		m_ContinueCue = null;
		if ((bool)continueCue)
		{
			m_Answers.Add(Dialog.GetContinueAnswer());
			m_ContinueCue = continueCue;
		}
		else
		{
			foreach (BlueprintAnswerBase answer2 in answers)
			{
				if (answer2 is BlueprintAnswer blueprintAnswer && blueprintAnswer.CanShow())
				{
					m_Answers.Add(blueprintAnswer);
				}
			}
		}
		if (!Answers.Empty())
		{
			return;
		}
		if (m_Sequences.Count > 0)
		{
			CueSequence cueSequence = m_Sequences.Peek();
			BlueprintCueBase blueprintCueBase = cueSequence.PollNextCue();
			if (blueprintCueBase != null)
			{
				m_Answers.Add(Dialog.GetContinueAnswer());
				m_ContinueCue = blueprintCueBase;
				return;
			}
			m_Sequences.Pop();
			BlueprintSequenceExit exit = cueSequence.Blueprint.Exit;
			if ((bool)exit)
			{
				AddAnswers(exit.Answers.Dereference(), exit.Continue.Select());
			}
			else
			{
				m_Answers.Add(Dialog.GetExitAnswer());
			}
		}
		else
		{
			m_Answers.Add(Dialog.GetExitAnswer());
		}
	}

	private void PlayBasicCue(BlueprintCue cue)
	{
		CurrentCue = cue;
		cue.ApplyAlignmentShift();
		BlueprintCueBase blueprintCueBase = cue.Continue.Select();
		CueShowData cueShowData = new CueShowData(cue, m_SkillChecks, AlignmentShifts);
		Alignment alignment = Game.Instance.Player.Alignment;
		if (m_OldPlayerAlignment != alignment)
		{
			cueShowData.NewAlignment = alignment;
			m_OldPlayerAlignment = alignment;
		}
		m_SkillChecks.Clear();
		AlignmentShifts.Clear();
		if (!PlayingBookPage)
		{
			AddAnswers(cue.Answers.Dereference(), blueprintCueBase);
			EventBus.RaiseEvent(delegate(IDialogCueHandler h)
			{
				h.HandleOnCueShow(cueShowData);
			});
		}
		else
		{
			m_BookPageCues.Add(cueShowData);
		}
		if (PlayingBookPage && (bool)blueprintCueBase)
		{
			PlayCue(blueprintCueBase);
		}
		if (cue.Experience != DialogExperience.NoExperience && (cue == CurrentCue || !LocalShownCues.Contains(cue)))
		{
			GameHelper.GainExperience(ExperienceHelper.GetDialogXp(cue.Experience, null, Dialog.OverrideAreaCR));
		}
	}

	private void PlayCheck(BlueprintCheck check)
	{
		UnitEntityData unitEntityData = check.GetTargetUnit();
		if (unitEntityData == null && ActingUnit != null)
		{
			unitEntityData = ActingUnit;
		}
		SkillCheckResult skillCheckResult;
		if (unitEntityData != null)
		{
			skillCheckResult = new SkillCheckResult(GameHelper.TriggerStatCheck(RuleStatCheck.Create(unitEntityData, check.Type, check.GetDC()), null, !check.BanPartyCheckInCamp), unitEntityData);
		}
		else
		{
			RulePartyStatCheck rulePartyStatCheck = new RulePartyStatCheck(check.Type, check.GetDC(), m_CapitalPartyChecksEnabled);
			Game.Instance.Rulebook.TriggerEvent(rulePartyStatCheck);
			unitEntityData = rulePartyStatCheck.Roller;
			skillCheckResult = new SkillCheckResult(rulePartyStatCheck.StatCheck, unitEntityData);
		}
		if (skillCheckResult.Passed)
		{
			LocalPassedChecks.Add(check);
			LocalFailedChecks.Remove(check);
			if (check.Experience != DialogExperience.NoExperience)
			{
				GameHelper.GainExperienceForSkillCheck(ExperienceHelper.GetDialogXp(check.Experience, check.GetDC(), Dialog.OverrideAreaCR), unitEntityData);
			}
		}
		else if (!LocalPassedChecks.Contains(check))
		{
			LocalFailedChecks.Add(check);
		}
		if (!check.Hidden || skillCheckResult.Passed)
		{
			m_SkillChecks.Add(skillCheckResult);
		}
		PlayCue(skillCheckResult.Passed ? check.Success : check.Fail);
	}

	private void PlaySequence(BlueprintCueSequence sequence)
	{
		CueSequence cueSequence = new CueSequence(sequence);
		m_Sequences.Push(cueSequence);
		BlueprintCueBase blueprintCueBase = cueSequence.PollNextCue();
		if (blueprintCueBase == null)
		{
			PFLog.Default.Error("Could not select first cue in cue sequence ({0}).", sequence);
			StopDialog();
		}
		else
		{
			PlayCue(blueprintCueBase);
		}
	}

	private void PlayBookPage(BlueprintBookPage page)
	{
		try
		{
			m_PlayingBookPageCount++;
			InterceptBookPageImageChange interceptBookPageImageChange = new InterceptBookPageImageChange();
			using (EventBus.Subscribe(interceptBookPageImageChange))
			{
				page.OnShow.Run();
				bool flag = false;
				foreach (BlueprintCueBase item in page.Cues.Dereference())
				{
					if (item.CanShow())
					{
						flag = true;
						PlayCue(item);
					}
				}
				if (!flag)
				{
					LogChannel.Default.ErrorWithReport("Could not select any cue in book page ({0}).", page);
					StopDialog();
					return;
				}
				AddAnswers(page.Answers.Dereference(), null);
				EventBus.RaiseEvent(delegate(IBookPageHandler h)
				{
					h.HandleOnBookPageShow(page, m_BookPageCues, m_Answers);
				});
				interceptBookPageImageChange.RunAction();
			}
		}
		finally
		{
			m_BookPageCues.Clear();
			m_PlayingBookPageCount--;
		}
	}

	private bool CanShowAnyCue(BlueprintBookPage page)
	{
		foreach (BlueprintCueBase item in page.Cues.Dereference())
		{
			if (item.CanShow())
			{
				return true;
			}
		}
		return false;
	}

	private void TurnUnit([CanBeNull] UnitEntityData unit, [CanBeNull] BlueprintUnit listener)
	{
		if (unit == null || m_HeadlessMode)
		{
			return;
		}
		float listenerRange = BlueprintRoot.Instance.Dialog.ListenerRange;
		UnitEntityData unitEntityData = null;
		if (listener != null)
		{
			unitEntityData = Game.Instance.State.Units.Where((UnitEntityData u) => u.Blueprint == listener).Nearest(unit.Position);
			if (unitEntityData != null && unit.DistanceTo(unitEntityData) > listenerRange)
			{
				unitEntityData = null;
			}
		}
		if (unitEntityData != null)
		{
			unit.LookAt(unitEntityData.Position);
			unitEntityData.ForceExitStealth();
			return;
		}
		if (unit.IsDirectlyControllable)
		{
			Vector3 point = ((FirstSpeaker != null) ? FirstSpeaker.Position : DialogPosition);
			unit.LookAt(point);
			return;
		}
		UnitEntityData value = Game.Instance.Player.MainCharacter.Value;
		UnitEntityData unitEntityData2 = ((unit.DistanceTo(value) <= listenerRange || Initiator == null) ? value : Initiator);
		unit.LookAt(unitEntityData2.Position);
		unitEntityData2.ForceExitStealth();
	}

	private static void SwitchSpeakerIn(UnitEntityData unit)
	{
		if (unit == null || (unit.IsPlayerFaction && unit.IsInGame))
		{
			return;
		}
		UnitPartDualCompanion unitPartDualCompanion = unit.Get<UnitPartDualCompanion>();
		if (unitPartDualCompanion == null || unitPartDualCompanion.IsActive)
		{
			return;
		}
		UnitEntityData value = unitPartDualCompanion.PairCompanion.Value;
		if (value == null)
		{
			PFLog.Default.Error("Pair unit not found");
			return;
		}
		UnitPartDualCompanion unitPartDualCompanion2 = value.Get<UnitPartDualCompanion>();
		if (unitPartDualCompanion2 == null)
		{
			PFLog.Default.Error("Pair part not found");
		}
		else
		{
			unitPartDualCompanion2.SwitchOut();
		}
	}

	private void PlayAnimation([CanBeNull] UnitEntityData unit, DialogAnimation animation)
	{
		if (!(unit?.View?.AnimationManager == null) && !m_HeadlessMode && animation != DialogAnimation.None)
		{
			m_CurrentSpeakerAnimation = unit.View.AnimationManager.CreateHandle(UnitAnimationType.DialogCueAnimation);
			if (m_CurrentSpeakerAnimation == null)
			{
				PFLog.Default.ErrorWithReport($"DialogCueAnimation is missing (dialog: {Dialog.name}, unit: {unit})");
				return;
			}
			m_CurrentSpeakerAnimation.Variant = (int)animation;
			unit.View.AnimationManager.Execute(m_CurrentSpeakerAnimation);
		}
	}

	public void Activate()
	{
	}

	public void Deactivate()
	{
	}

	public void Start()
	{
		UnitCombatLeaveController.TickGroups(ignoreTimer: true);
		if (Dialog.TurnPlayer)
		{
			TurnUnit(Game.Instance.Player.MainCharacter, null);
			TurnUnit(Initiator, null);
		}
		if (FirstSpeaker != null)
		{
			AddInvolvedUnit(FirstSpeaker);
		}
		foreach (UnitEntityData unit in Game.Instance.State.Units)
		{
			if (!CutsceneControlledUnit.GetControllingPlayer(unit))
			{
				unit.Commands.InterruptAll();
			}
		}
		EventBus.RaiseEvent(delegate(IDialogStartHandler h)
		{
			h.HandleDialogStarted(Dialog);
		});
	}

	public void Stop()
	{
		List<UnitEntityData> list = InvolvedUnits.ToTempList();
		SoundState.Instance.StopDialog();
		EventBus.RaiseEvent(delegate(IDialogFinishHandler h)
		{
			h.HandleDialogFinished(Dialog, success: true);
		});
		Clear();
		foreach (UnitEntityData item in list)
		{
			CutsceneControlledUnit.UpdateActiveCutscene(item);
		}
	}

	private static void StopDialogAnimations(UnitEntityData unit)
	{
		List<AnimationActionHandle> list = unit.View?.AnimationManager?.ActiveActions;
		if (list == null)
		{
			return;
		}
		foreach (UnitAnimationActionHandle item in list)
		{
			if (item.Action.Type == UnitAnimationType.DialogCueAnimation)
			{
				item.Release();
			}
		}
	}

	public void Dispose()
	{
		m_CurrentCue = null;
		Clear();
	}

	public void OnAreaBeginUnloading()
	{
		if (Dialog == null)
		{
			Initiator = null;
			FirstSpeaker = null;
			CurrentSpeaker = null;
			ActingUnit = null;
			m_CapitalPartyChecksEnabled = false;
		}
	}

	public void OnAreaDidLoad()
	{
	}

	public static IDisposable MakeSpeakersNotRequired()
	{
		return new MakeSpeakersNotRequiredClass();
	}
}
