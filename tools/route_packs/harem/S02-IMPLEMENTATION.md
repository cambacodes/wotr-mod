# S02 — Seelah / Wenduag

Authored RRT addition, implementing doc 16 §8b, the reviewed A1–A10 amendments
in `storylines/household_pair_seelah_wenduag.py`, and W1-S02 of WAVE-PLAN.
No native event, death, quest, romance etude or slide is rewritten.

The existing Ch5 Table opener is AnswersList_0054
`6dccfd39947ef4242a8afbe36b21a46c`, returning through Cue_0065
`7b050ba0745bf144e815632e39b34853`. Pair entries use that system door;
they do not add their own native return. The `c3` archive folder does not
change its Chapter05 gate.

Native voice evidence was reopened in `/wrath/blueprints.zip` and
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`: all S1–S7,
W1–W6 and P1–P2 paths, asset GUIDs and localization keys in the pair-data
EVIDENCE table. P1 supplies a fight/date suggestion, never existing love.
W5 supplies Wenduag's attraction to strength; W6 preserves her wickedness.
No unplayed banter, Acemi recollection or Savamelekh outcome is asserted.
Brask's optional recalls use only the existing cairn claim receipts, with
Seelah reacting to the disclosed action instead of silently blessing it.

`storylines/harem_s02.py` registers eleven scenes with the existing API;
`story.py` supplies only this pair's controller-owned derived stages from
the approved LADDER. Prose publishes incident witnesses, never attitudes,
enmity, strain, reconciliation or romance closure. Higher stages suppress
lower readers. Unreconciled directed enmity suppresses both stage readers
and entries; the existing matching reconciliation overrides are retained.
The shared controller's enmity producers remain its owner's responsibility.

Every entry requires the paid page and current Trickster stance. Both women
must be eligible, have open routes, and satisfy their current `present_now`
observations; historical return flags alone do not override later losses.
Wenduag's native finished-romance eligibility remains available through the
household adapter. The invitation is Ch5 with no invented delivery delay.
Spar/rematch use the protected allowance; later deeds use the pair allowance.
The optional arc begins at watch and counts six distinct witnesses, with
personal-order wrappers sharing their original exhaustion witnesses.
Delays use enacted deed receipts, including the repayment receipt before
choice. No Derived stage is treated as a clock. No Ch4 or Ch6 fallback.

Rusk, the gully ambush, willing crusade scouts, the extraction watch and the
lower-wall tower are authored incidents. They are narrated within the Table
dialogue, with no spawned battle or new quest. Wenduag sacrifices revenge
and an already planned hunt to keep command of her hunters and pay a strong
fighter's debt. Seelah spends a watch and suffers the prescribed wound.
The restraint rule covers all captives on their shared operations, including
maiming, interrogation by injury, trophy killing, delegated abuse and staged
escapes. It does not reform Wenduag or buy access to Seelah's body.

Failed spar permits the one prescribed rematch. Failed rematch, declined
rematch, failed rescue, ordered execution and Commander betrayal retain
distinct receipts. No new remedy or reconciliation condition is added.
Only the watch-taken branch contains both independent answers, the slot
`household.pair.seelah_wenduag.choice.explicit.1`, and `choice.both_yes`.
The household evening is a complete nonsexual alternative. Morning reads
the mutual answer and retains prayer, live custody and independent duties.
The brief is under `tools/route_packs/explicit_slots/harem/seelah_wenduag/`;
the default slot contains only the heated cut. No explicit prose or echo.

Acceptance: `test_harem_s02` executes both personal-deed orders, all major
negative histories, abort, attendance, paid-page and reconciliation guards,
clocks and allowance metadata. `HaremS02Tests` walks both orders for native
finished romance and authored Wenduag courtship, using exported native-aware
predicates and the actual C# answer graph. W5 Ledger and
Last Call readers are separately scheduled work; this implementation does
not edit their shared hosts or claim whole-roster enmity certification.
