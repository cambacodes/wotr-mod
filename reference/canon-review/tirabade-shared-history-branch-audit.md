# Tirabade shared history branch audit

Date: 2026-09-26.
Scope: independent read-only design audit of native scar, Queen-loss, and Irabeth morale evidence for optional shared `return` and `last_watch` responses.
No story, metadata, source, installed asset, or native state was changed.
This is not approval of unwritten response prose or a Unity test.

The existing history keys are sufficient for optional recollections with carefully limited claims.
They are insufficient to infer forgiveness, present emotional recovery, or every occurrence of the underlying event.
There is also a native state for the Commander's violence against Irabeth, so an eventual implementation need not infer that event from a conversation alone.

## Scar history

`storylines/irabeth_independent.py` registers `irabeth.scar_known` against two observed cues.
The engine reads these as alternative history witnesses, not a requirement that both conversations happened.

| Witness | Native blueprint | Meaning |
| --- | --- | --- |
| `c7a7717c516039d498a7525baf6abe04` | `World/Dialogs/NPC_Common/Irabeth/Cue_0071.jbp` | Irabeth touches her face, justifies the Commander's intervention, and asks that the subject not be raised again. |
| `8e808b69a43ed4f43b8eb39d27990a4a` | `World/Dialogs/NPC_Common/Anevia/Cue_0045.jbp` | Anevia says Irabeth refused to have the scar healed and treats it as a reminder of disgrace. |

Anevia's preceding `Cue_0044`, asset `0986b5a3bc4f7ae4aa858dcb4aa8e9e6`, explicitly identifies the Commander as the person who cut Irabeth.
It also expresses Anevia's anger and changed view of the Commander.
The continuation goes directly to the registered Anevia witness.

The combined key supports a reference to harm the Commander caused.
It does not always support "you told me" addressed specifically to Irabeth, since the player may have heard only Anevia.
It does not prove Anevia heard the Commander's private exchange with Irabeth, or that either woman has forgiven the act.
Irabeth's self-blame must not be mistaken for the reviewer's endorsement of the injury or proof that the injury helped her.
An optional new conversation can revisit the subject, but her native request to stop discussing it deserves an actual possible boundary in the authored response.

The underlying etude is `IrabethEncouragedByDemon`, GUID `b4f08736cf124ae4996fcef7c0a33bf1`.
Its native definition is under `World/Etudes/Common/WrathOfTheRighteous/Chapter02_Extra/IrabethWithUs/IrabethInDrezenEncouraged/`.
The misleadingly positive name does not mean romantic encouragement or healthy recovery.
The etude includes native portrait replacement actions for Irabeth variants.

`World/Dialogs/c2_vs/DrezenSiege/Council/Answer_0058.jbp`, asset `183cdfc65be9e8949b8b4aba7b8404d8`, starts that etude when the player selects the inner-demon response.
The later Irabeth scar question `Answer_0070`, asset `2ae38a949a0eb8e42aa32ac4583cb208`, requires this etude Playing.
The Anevia scar question `Answer_0043`, asset `2c8db2c92c5f9b340b36a6c7955decc2`, accepts its Started or Playing status.

An optional future event-history binding could therefore read the original selected answer `183cdfc65be9e8949b8b4aba7b8404d8`.
A live etude binding is also possible, but the current generic `Etudes` reader checks Playing, not every native Started state.
Do not claim those two methods are identical over dormant, completed, or externally edited states.
Neither additional binding is necessary if this revision deliberately offers only callbacks to the already observed scar discussions.

## Queen-loss history

`irabeth.queen_loss_known` observes `d47bcd8d88f8ea149a596ca927e1153f`, native `World/Dialogs/NPC_Common/Irabeth/Cue_0197.jbp`.
Irabeth says she failed to guard the Queen, that the Queen is dead, and that the Commander should not rely on her.
The localization key is `26d166cf-ac3c-4734-84fc-52dfed2abbc5`.
This supports "you told me about the Queen at Iz" addressed to Irabeth.
It does not establish a later change in her opinion or present-day forgiveness of herself.

Its incoming `Answer_0196`, asset `cab65208835a4ea459dc20503112a247`, requires all of these native conditions:

- `Obj4_FightDeskari`, GUID `8b0c2479c21eaf14db524dd888a106a7`, is Completed.
- `GalfreyDead`, GUID `a4f20ae9f6a6c3d4ba204721589470a2`, is Playing.
- `PlayerIsKnightCommanderAfterFane`, GUID `37a2df11c979ed446b6716142b2b01f5`, is not Playing.

The last condition corresponds to the native history that permits Irabeth's account of going with the Queen.
It is not a generic "Irabeth sad" flag.
The `GalfreyDead` definition explicitly includes death regardless of cause, including the undead case, so that etude alone would be a weaker and broader substitute for the observed conversation.

Using the seen cue preserves the exact known history without rebuilding these native prerequisites.
Do not offer the Queen-loss response solely because the shared route has reached chapter 5 or the `return` scene.
The observed cue can be absent before Iz even though the shared reunion is available.
Conversely, history can remain recorded after later changes to live state, so phrase the callback as remembering her account rather than a fresh universal declaration about the Queen's current condition.

## Morale

The shared story already binds these native etudes:

- `broken`: `IrabethBroken_Chapter03`, GUID `7a038ff7b70e91844954407b18e8feb6`.
- `encouraged`: `IrabethEncouraged_Chapter03`, GUID `8b0924efc23df3540b4d8b5fbffd522f`.

These are distinct from the earlier demon-injury etude.
Neither should be inferred from the scar history key.
The current snapshot reads their actual Playing status, not a numeric affection score or a diagnosis.

Native usage persists beyond chapter 3.
`World/Dialogs/c6/ThresholdExterior/IrabethAnevia_Threshold/Cue_0002.jbp`, asset `33038b17ba9e8fe46b692ff8eff81e99`, requires Broken Playing.
Its alternative `Cue_0001`, asset `fba43765b99d2b249a2da3ff34e5d3ed`, requires Broken not Playing.
This makes morale-sensitive final-watch characterization well grounded.
It does not authorize the addon to clear Broken after a tender conversation.

For optional responses, use Broken first, Encouraged only when not Broken, and an unconditional neutral continuation.
The independent route already uses that precedence.
This avoids offering incompatible descriptions if external tools leave both states active, while making no claim that their native mutual exclusivity was exhaustively proven here.
Absence of both flags must not be described as proof of complete recovery.

## Proposed integration scope

At `return/now`, optional scar or morale responses can make its present generic discussion specific without assuming every player has the same history.
The Queen-loss callback can also be offered there only when the actual conversation has been seen; the shared reunion itself does not establish that timing.
At `last_watch/start`, the same witnessed histories can support an optional acknowledgement before the existing forward-looking choices.
Return to the existing scene path afterward and leave an ordinary choice available when no history is known.

No additional native mutation is justified by this design.
Use authored local memory only if a later callback needs to know which optional discussion happened.
Do not award native morale recovery, rewrite the violence event, restore the Queen, or silently convert a woman's self-blame into consent or forgiveness.
New prose may establish a changed personal response through its own events, but it must distinguish that authored development from the existing game flags.

Focused verification should cover no known history, each scar witness separately, both witnesses, Queen history present and absent, Broken, Encouraged, both morale states, and neither morale state.
Check that every optional branch rejoins a valid scene node and that no choice writes native history or morale keys.
The review remains scoped to these proposed source-grounded branches; authors still need an independent reading of the actual new dialogue.
