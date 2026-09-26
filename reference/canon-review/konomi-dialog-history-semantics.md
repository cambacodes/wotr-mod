# Konomi dialogue history semantics

The parent freshly decompiled the installed Assembly-CSharp.dll for this investigation.
Its SHA256 is `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953`.
The generated references are `game-DialogSeen-current.cs`, `game-DialogState-current.cs` and `game-DialogController-current.cs` in this directory.

Native DialogSeen tests membership in `Game.Instance.Player.Dialog.ShownDialogs`.
DialogController adds the dialogue after scheduling its first cue and logging Started dialog.
It does not wait for the dialogue's finish actions.
DialogState serializes ShownDialogs as a JsonProperty alongside cue and answer history.
Consequently a native DialogSeen condition is evidence that a dialogue began, not that its final decision or finish actions ran.
The existing parent ReadDialogHistory adapter reads shown cues and selected answers but does not read shown dialogues.

## Political integration consequence

The native officer's rank-eight response uses rank-eight DialogSeen plus the approved-foreign-help playing etude, with foreign intervention taking precedence over the domestic fallback.
The rank-six crisis response is lower priority than both rank-eight responses.
An adapter reproducing that native report must preserve those precise predicates and ordering, including the fact that dialogue history records starts.
It must not advertise an equivalent predicate as completed rank-eight business.

The rank-eight final cue `7f64a30ceb4bfb046990bccbded7ac75` explicitly states that the Diplomatic Council has served its purpose.
The existing SeenCues adapter can bind that cue for a bounded memory such as `konomi.council_conclusion_seen`.
That is a suitable prerequisite for remembering the conclusion, not a replacement for current officer presence or an assurance that all finish actions ran.
Native dismissal remains the separate selected-answer predicate already bound as `konomi.dismissed`.
The capital officer etude can remain active after council conclusion; no new dialogue should infer dismissal from the conclusion cue.

## Required cases before promotion

- Rank six started, without rank eight, retains the native crisis-report precedence.
- Rank eight started but its conclusion cue unseen must not invent a remembered closing speech.
- Rank eight seen plus approved foreign help selects foreign intervention before the domestic fallback.
- Rank eight seen without that playing etude selects the native domestic fallback.
- Conclusion cue seen while the officer remains present allows a concluded-council memory without inventing dismissal.
- Actual dismissal uses the selected answer and preserves existing private-contact requirements.
- Missing or interrupted histories receive neutral context rather than a fabricated completed decision.

No new native history binding or story reaction was exported in this investigation.
It resolves the uncertain history semantics identified in `konomi-political-state-findings.md` and prevents a dialogue-start predicate from being mislabeled as quest completion.
