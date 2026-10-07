# Konomi private absence chronology repair

## Scope and reproduction

This repair addresses the deferred catch-up contradiction identified in `reference/story-review/konomi-final-independence-review.md`.
It changes only `storylines/konomi_private_absence.py` and adds `tests/KonomiAbsenceChronologyTests.cs`.
Root owns shared test registration and the narrowly adjusted legacy page-coverage assertion.

I independently reran the reviewer's actual rules traversal against frozen export `C3C9D2D3FE27F64E883DFEFA8A99E5E26F09612DEA6CCFE1B37C04C11AF86210`.
The 802-assertion reproduction plays the Chapter 5 acquisition, reunion, career decision, career consequences and farewell, then reaches the obsolete uncertainty in the still-available manual catch-up.
It uses `Rules.Available` and `Program.Walk`, not just seeded authored career flags.
The starting native fixture is Chapter 5 Drezen with Trickster, dismissed Konomi and completed office.

`fate_post -> fate_reply -> private_meeting -> carriers -> before_road -> private_departure -> capital_letter -> return_offer -> private_reunion -> lease_offer -> chosen_evening -> private_future_choice -> private_return_terms -> private_kept_hours -> private_last_visit`

The catch-up remains available after this chain by design.
The repair retains that access.

## What changed

`absence_now` no longer claims that her career is still merely a collection of proposals or that she has not found work leading to influence.
It discusses the continuing competition for her evenings without contradicting a signed agreement.
`absence_her_days` now recounts the two reception proposals in the past tense.
Both shared pages retain their original IDs and three mythic-answer indices.
Their revised text also appears in the initial reunion, where it remains truthful before career decisions.

The catch-up alone appends optional recollection choices after those original answers.
On valid played histories exactly one career recollection is available at either entry page.
Players may keep the original shorter conversation instead.
The new pages never make career decisions, change native outcomes, alter relationship commitments or require a replay.

| New page suffix after `absence_career_` | Earned history |
| --- | --- |
| `decision_now` | Initial career choice accepts immediately; later terms not sent |
| `decision_wait` | Initial career choice delays; later terms not sent |
| `terms_exclusive` | Seasonal first-refusal terms sent; acceptance not yet played |
| `terms_portfolio` | Smaller guarantee terms sent; acceptance not yet played |
| `paid_exclusive` | Accepted seasonal agreement and played visit; farewell not complete |
| `paid_portfolio` | Accepted smaller guarantee and played visit; farewell not complete |
| `settled_exclusive` | Completed career farewell, seasonal influence and paid tenant option |
| `settled_portfolio` | Completed career farewell, independent search and its paid result |
| `future` | Common return to the existing Legend, Trickster or other-path answer |

All new pages use the existing Konomi portrait key.
No image is supplied by this repair.
The initial reunion receives none of the new career pages because it precedes those decisions.

## Checks

Python compilation passed.
An independent comparison against the frozen export confirmed that all scene IDs and gates remain identical, all existing node IDs preserve their order, and every original answer array is an exact prefix of the repaired array.
Only the two named existing pages in reunion and catch-up changed.
The nine career pages are appended to catch-up.

`Rules.Validate`, the new chronology suite and the existing private absence suite passed together with 371,366 assertions.
The temporary runner copies the actual `Program.Walk` and `Program.Copy` helpers and compiles the actual `src/Story.cs`.
It uses this command:

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/konomi-absence-chronology-loxodquz/Check.csproj' -- 'C:/Users/Z/AppData/Local/Temp/konomi-absence-chronology-loxodquz/candidate.json'
```

The new suite plays Chapter 5 acquisition and both initial career decisions, tests before and after the chosen evening, both relationship futures, both subsequent agreements, both afternoon costs and all current mythic reply branches.
It covers every new page, original answer ordering, unfinished-page history preservation, deferral, acknowledgement replay blocking and existing native or relationship blockers.
Existing timestamps and flags remain intact.
The only new persisted catch-up results remain the existing acknowledgement, optional kiss and scene completion flags.
A separately labeled legacy fixture exercises a saved private absence record without claiming native attainability of its earlier history.

## Native chronology limitation

The independent native audit identifies `Kingdom/CrusadeProjects/RankUps/Diplomacy/DiplomacyRankUp6Project.jbp`, GUID `1b198b45455d452b8772b9d9f418f864`, as requiring active Chapter 5, GUID `5b01aa690202e584888dfc600a4aac0a`.
See the exact native records and hashes in `reference/story-review/konomi-final-independence-review.md`.
The earlier Chapter 3 dismissal fixtures are synthetic compatibility scenarios, not proof of an ordinary attainable early dismissal or private Chapter 4 absence.
This fix adds no earlier native dismissal, fabricated rank outcome, actor spawn or mythic access.
The new primary regression starts at the native Chapter 5 dismissal endpoint and earns its authored history from there.
Actual Unity execution remains untested.

## Released files

| File | SHA256 |
| --- | --- |
| `storylines/konomi_private_absence.py` | `6DA8E3C1FD997ACFD143095E79E6ED5381092976BA030989595ED464A4F8C963` |
| `tests/KonomiAbsenceChronologyTests.cs` | `FD1E5EF417E1AACA1731344AF1BC0D51420071A6DC5A56B8F036DE31D2BD249F` |

The source is frozen for independent review.
These tests do not assign writing scores or approve the complete character.
