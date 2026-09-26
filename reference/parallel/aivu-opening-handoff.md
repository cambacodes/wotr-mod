# Aivu opening handoff

Author ownership is limited to `storylines/aivu_opening.py`, `tests/AivuOpeningTests.cs`, `reference/canon-review/aivu-route-evidence.md`, and this handoff.
No shared exporter, runtime, generated story, other author's source, or art was modified.

## Released contribution

Source SHA-256: `EB0B616F2A6EA722A43A4376FAB1FC2E2BD64CDF2EB6A69D1733D480097C9784`.
Test SHA-256: `2B780FD51C75218F5A9D737FFB3912F6836A4DC15114ED4B57266E226F44809E`.
The module exports `SCENES`, `ETUDES`, and `RELATIONSHIP` with no cross-module overlays.
Register four scenes, two new native absence aliases, and relationship key `aivu`.
Existing alias `azata` is required; it is never authored or granted.
The relationship's `CommittedFlag` is `aivu.trusted`, an earned friendship marker, with no romantic interpretation.

| Scene suffix | Delay | Played development |
| --- | --- | --- |
| `a_city_with_wings` | 0 hours | Aivu owns an aerial map project; choose shared names or two sides after meeting someone whose home appears on it. |
| `the_roof_below` | 24 hours | Aivu admits damaging a laundry awning; physical repair gives either space or shared work to the frightened laundry hand. |
| `a_way_for_feet` | 48 hours | Respect a new fear without borrowing captivity history; clear a cart by inspection, dismantle it after waiting, or mark the blocked route and leave it. |
| `someone_elses_turn` | 48 hours | A real map trial exposes different design faults, recalls earned repair/clearance choices, and lets Aivu choose more exploration or a useful copy with the Commander. |

All scene IDs have prefix `aivu.`.
Both Perception DC 18 outcomes are playable; failed inspection changes the job to a longer collaborative dismantling rather than closing friendship.
Mutually exclusive map, repair, passage, and next-project flags are set only at terminal choices after their narrative is played.
Aborting at entry leaves the scene available and changes no outcome flags.
No native quest, other romance, or pet state is altered.
ToyBox free-love/no-jealousy settings have no role in this friendship's eligibility or outcomes.

## Measurement and focused verification

The project's content tokenizer counted 4 scenes, 27 pages, 4,186 raw words, 4,179 distinct whole-segment words, and 7 exact repeated words.
There are 128 completed choice/check traversals across the actual earned chain, ranging from 2,571 to 2,810 selected prose-plus-choice words.
Counts exclude titles, journal metadata, entry labels, unselected alternatives, and external game/RanRomance content.
This opening is far below the eventual 21,000-word per-character floor and is not a finished full friendship route or RanRomance parity claim.

Isolated harness: `C:/Users/Z/AppData/Local/Temp/aivu-check-zbe6apnn/Check.csproj`.
Command: `dotnet run --project <harness> -- <same-directory>/story.json`.
Result on the released revision: `PASS 2046`.
The harness compiles the actual `Story.cs`, `RecoveryAttempt.cs`, `TerendelevDeliveryAttempt.cs`, and test sources against a temporary candidate JSON with this module added in memory.
It calls only `AivuOpeningTests.Run` and does not build or replace the shared installed mod.
The first harness compile lacked the newly added Terendelev helper; adding that existing source to the temporary project resolved the harness dependency, with no project-source change.

Focused checks traverse earned predecessors, both roll outcomes, every page, abort and incomplete replay, exact delay boundaries, native detachment interruptions, missing actual pet, wrong area/chapter, isolated Trickster rejection, continued existing romances, and incompatible terminal outcomes.
These are Rules-level checks, not a Unity E2E session or an independent literary score.

## Promotion limits

The evidence file documents the material remaining blocker: actual Chapter 3 capital attachment to the verified pet/main answer list is not proven by the blueprint archive alone.
Do not label the opening in-game ready until a real Azata save verifies the actor, area, and native dialogue or root implements a separately verified contact.
The exported scene contract preserves native ownership and fails closed on missing pet or absence flags.
Later Azata rescue-sensitive content, a bespoke attainable Trickster guest route, other appropriate mythic handling, art, full-length development, and independent writing/canon review remain required.
No full-route approval or author review score is supplied.
