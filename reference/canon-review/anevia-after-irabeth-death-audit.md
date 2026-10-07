# Anevia contact after native Irabeth death

Native data supports a living bereaved Anevia appearing in Drezen during the post-Iz ceremony.
It does not establish a normal, persistent free-roam contact window for the new grief visit after that ceremony.
The native departure cue starts `AneviaGone`, which starts the state that hides the exact capital actor.
The frozen `anevia.a_grief_with_a_name` therefore cannot be counted as generally attainable post-bereavement content merely because a source test supplies her contact GUID.

## Evidence and reproduction

The accompanying read-only probe scans the installed `blueprints.zip` for the actual capital spawner and the relevant death/absence flags.
It also records the complete Coronation dialogue folder so its cue joins can be inspected, selected parent etudes, and their installed English localization.
It does not modify the game or authored route.
Run `C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64/python.exe reference/canon-review/anevia-after-irabeth-death-probe.py` from the project root.

Records SHA256: `96CF38382192EF2D987B9ACB18E25C13BC845A7D879D0A20642EA2014BED5E3F`.
Probe SHA256: `A60A47CF4313AA9D76352A4AFAD27D5DBAEC18470FFDFE163B8366ADA77F54FB`.
Each extracted record includes its archive path, actual AssetId and individual source-byte SHA256.
This is installed-source evidence, not a loaded-save or Unity execution result.

## Exact actor and ordinary positioning

The existing `tirabade-capital-contact-records.json` identifies `AneviaTirabade_DrezenCapital`, GameObject 298, in `drezencapital_default_mechanics.scenes`.
The spawner is `86b332a9-5910-4d46-9951-8e06f7dcf0cf`, unit `b5e867e13503c6f41bb1316705efb4a2`, scene asset `3e2b5ea054cd5b2479e7f13134363ef4`.
Its dialogue interaction is `de4cc2dd71694b842be37b75d1705b83`, the ordinary Anevia dialogue containing answer list `33960c7f7af40cd43b7f801a76c87a0b`.
The spawner has SpawnOnSceneInit true, RespawnIfDead false and no direct spawn condition asset.
A separate component has SpawnHidden true.
Consequently the spawner existing in an asset is insufficient evidence that a player can converse with her.

`AneviaTirabade_DefaultActor`, `439b0e79b73e57343ad754e9a1c704e5`, hides this spawner at priority -100 in conflicting group `27d10af5650a01b4d803da81799cbc86`.
`AneviaTirabade_InThroneroom`, `4b441ac2bc063f6439795edc9d98b8a1`, unhides the same actor and moves her to locator `a81a0987-bcbe-466f-a296-013fe628ad0d` at priority -50 in that group.
Its activation condition is NOT `AneviaGone` playing.
It does not independently forbid `IrabethDead`.
Its parent `DrezenCapital_DefaultMechanic`, `30862a76dd4a11049be42d3de26159fb`, links the capital area `2570015799edf594daf2f076f2f975d8` and starts the throne-room positioning etude.
This is positive static support for a bereaved actor before her departure takes effect, subject to active parent mechanics and higher-priority competing positions.
It does not prove the player gets an uninterrupted ordinary dialogue opportunity between returning from Iz and the ceremony.

## Death does not itself mean Anevia has departed

`IrabethDead`, `b14e13f9359585e498fcd81ab95d4d7e`, starts `IrabethNotInDrezen`, `99a03d4f02004b76a5e97c85ba0ec37e`.
That action hides Irabeth's capital actor, not Anevia's.
The Iz death dialogue `48a3a4ff8955b7045bac0ea06092e085` kills its Irabeth summon-pool target and starts this death etude in FinishActions.
`IrabethSacrificedHerselfSavingGalfrey`, `518d91f94fb3a504a91571b7e75c68fc`, is a death child that starts its parent.
`IrabethKilledByPlayer`, `c0f261c4a259da741ab0052f0100c2a0`, also starts the death parent.
Those distinguishable histories must not all be narrated as an innocent military bereavement.

## Positive ceremony appearance and subsequent departure

`Coronation`, `7ef4b33d3aa037f4984e167eae592009`, starts `Coronation_OutdoorKTC`, `a30fa65c287ebb8418736a544797b7f4`.
The outdoor KTC links area part `8a076e720870a44438d13b9b939933fd` and waits until no other etude in its KTC conflicting group is playing.
It starts `Coronation_AneviaPosition`, `7076d6e6f8e984749829211b04119a80`.
That position activates when either `IrabethDead` or `IrabethNotInDrezenCh5_WithGalfrey`, `260454e5186fbd34694a0393097f77b5`, is playing.
At priority 100 it unhides the exact capital Anevia actor and moves her to the coronation locator `0c6a9c0e-59eb-4aae-84a7-a3ad8ac0e476`.
This is direct evidence of native bereaved physical staging, rather than an inference from the absence of AneviaDead.

Coronation `Cue_0421`, `575f7925bbfe4e047bcd666ca27a8c80`, requires IrabethDead playing, AneviaDead not playing and AneviaGone not playing.
Its English text says that her crusade ends here and that without Beth she does not belong.
Its OnShow starts `AneviaGone` immediately.
`SequenceExit_0119`, `2f047a1b27406e841bce7bb3ad2f0890`, references this cue before the subsequent Storyteller portion.
The related bereavement cues 0422, 0436 and 0437 explicitly state that she already knows about Irabeth's death.
An authored grief visit must not present the news as something she learns for the first time after those cues.

The ceremony also distinguishes the Commander admitting personal responsibility.
Answers 0425 and 0430 say the Commander killed Irabeth and lead to cues 0426 and 0431 respectively.
Those cues make Anevia vanish with a hateful glare and start AneviaGone in OnShow or OnStop.
There is no demonstrated native reconciliation or ordinary capital return attached to that response.

## The actual absence guard

`AneviaGone`, `09f46662bcd14a03a0874267e16d6e6f`, starts `AneviaNotInDrezen`, `6125c10886d6465091f4e092618ca55a`.
The latter links capital area `2570015799edf594daf2f076f2f975d8`, uses the same position conflict group at priority 99 and hides the exact Anevia spawner.
Its activation condition is NOT the conjunction of Coronation completed and IrabethDead not playing.
Thus a still-playing IrabethDead marker prevents the alive-wife post-coronation exception from suppressing this absence etude.
The temporary coronation position has higher priority while active, but this cannot be treated as permanent restoration or as a free conversation window after departure.

The ordinary common-dialogue `Cue_0089` is not contrary evidence.
It requires the relevant post-Iz objective completed and IrabethDead NOT playing, along with its other native condition.
It is the living-Irabeth response, not a bereavement contact branch.
A historical death flag also cannot establish whether some separate recovery mod has restored either actor.
No native flag is cleared or rewritten by this audit.

## Consequence for the authored route

Keep physical contact, own-death, own-gone and own-away guards intact.
Do not award a survivor continuation in a test and then describe that fixture as proof that the native actor is normally present.
No supported persistent post-coronation bereavement window has been established here.
Before the departure cue there is conditional static support for Anevia's living actor, but actual ordinary answer-list access and interruption by the forced ceremony remain unresolved.
That narrow possibility is not enough to advertise the current standalone grief scene as a delivered native path.

The truthful present scope is that this chapter needs either an explicitly verified pre-departure opportunity with compatible chronology, or a separately authored voluntary contact/recovery continuation after her departure.
Such a continuation must respect her decision to leave, distinguish the Commander killing Irabeth, and preserve the historical native states.
It cannot merely remove AneviaGone from the guards or repurpose a temporary ceremony unhide as consent to resume romance.
Trickster-specific restoration and later relationship choices remain future completion work.
The frozen authoring source and tests were not changed during this investigation.
