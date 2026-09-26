# Tirabade chronology repair handoff

The overlay repairs three chronology problems in existing Tirabade scenes.
It does not add a route, establish individual romance outcomes, provide resurrection, or approve the complete campaign.
Independent review and shared registration belong to the parent agent.

## Frozen inputs and deliverables

| File | SHA256 |
| --- | --- |
| `development/Story.json`, main 291 input | `5E068C8E3601E7552AE501C34A8CD7E749207B00A9F32AABB1C5F99A515A4CA0` |
| `storylines/tirabade_chronology.py` | `D12D7CD6F5F685704DD1D387FFDEF8DDAF93E114F5BBBF66A59E7C3576CB9297` |
| `tests/TirabadeChronologyTests.cs` | `3BF8E9CB70EFE368220C41D1939ADBB9CC69BE8092BA72E5F2F51EB0178B90F0` |
| Temporary `after.json` | `E4370D7CA16C25922CB2232261B21F1195DBFD960DB0904597125DADC1E54F80` |

Only the two owned source/test files and this handoff were authored for this repair.
Shared registration, original storyline modules, generated exports, and the completed independent assembled audit were not edited.

## Reproduction before the repair

A fresh Chapter 5 snapshot played the existing acquisition sequence through `ordinary`, without `departure` or `wrote_letter`.
The source permits `return` after `ordinary`, yet its original `now` and `back` text asserted an earlier relationship during the Commander's absence.
The offending phrases were "when you were not there" and "where you left us".
Separate source witnesses found "unfamiliarity" in `shared_night/close` after earlier eligible intimate nights and "scarcely learned to imagine" in `ending_loss/end` despite a developed relationship.

The focused C# reproduction plays these 17 predecessors through the actual `Rules` and the existing test harness traversal helper:

```text
a_cup i_watch a_errand i_hands a_roof i_respite a_crossing i_crossing a_morning i_morning reckoning a_truth i_truth table ordinary a_self i_self
```

Running the new test against the unchanged input failed with `Fresh Chapter 5 still invents a pre-Abyss relationship.`
This is a played source-model reproduction with real availability rules and dialogue traversal, not a Unity or live-save E2E run.

## Changes and history proof

`return/now` and `return/back` now describe the current relationship without assigning its beginning to an earlier chapter.
An appended third answer at `return/start` recalls the actual pre-Abyss departure only when `departure` exists.
Its appended `before_the_abyss` node returns to the existing `now` node.
The original `departure` scene is Chapter 3 only and requires the negotiated `table` scene, so its completion supplies the needed chronology without a new timestamp or engine feature.
`abyss_letter` and `wrote_letter` alone do not prove a negotiated triad and do not unlock this callback.
An old save without the positive departure evidence receives neutral prose.

`shared_night/close` no longer treats physical intimacy as necessarily unfamiliar.
Three appended answers at `shared_night/near` recall the map night, the blue-coat night, or Tessa's room.
Each requires both the corresponding completed scene and its `.night` flag: `three_small_journeys`, `three_open_road`, or `three_rooms_unlocked`.
The existing engine can retain a choice flag after interruption before scene completion, so the night flag alone is insufficient.
These answers lead through the appended `familiar` node to the existing `close` node.
The original close and quiet answers remain available at their original indices.

`ending_loss/end` honors the days actually shared without describing their history as barely begun.
Its availability, terminal answer, and effects are unchanged.
All new relationship developments are authored additions, not claims about native canon.

## Exact focused commands and results

The standalone harness remains at `C:\Users\Z\AppData\Local\Temp\tirabade-chronology-o9w8sqpg`.
Its `Check.csproj` targets `net8.0` and directly compiles the project `src/Story.cs` and owned `tests/TirabadeChronologyTests.cs`.
Its `Program.cs` uses the existing `tests/Program.cs` helpers through `Copy` and `Walk`, with a small Main that deserializes the supplied Story and calls `TirabadeChronologyTests.Run(story, Check)`.
It does not depend on shared test registration.
The `before.json` file is the unchanged input; `after.json` applies only this overlay to that input.

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/tirabade-chronology-o9w8sqpg/Check.csproj' -c Release -- 'C:/Users/Z/AppData/Local/Temp/tirabade-chronology-o9w8sqpg/before.json'
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/tirabade-chronology-o9w8sqpg/Check.csproj' -c Release -- 'C:/Users/Z/AppData/Local/Temp/tirabade-chronology-o9w8sqpg/after.json'
```

The first command failed at the fresh Chapter 5 chronology witness.
The second passed with `PASS 1975 chronology assertions including traversal checks` and exit code 0.
No build warnings were printed.

Coverage includes the actual Chapter 3 departure path followed by Chapter 5 return, fresh Chapter 5 acquisition, unknown old history, letter-only history, saved current-node continuation, and all three earlier intimate-night callbacks.
The test plays the 20-scene expanded sequence to earn the three night histories.
For each callback it also rejects an interrupted night-only history and a completed scene without its night flag.
It checks completion of the familiar-night continuation, preservation of other companion romance flags, and the developed death ending.

A separate structural comparison found identical scene IDs and order, unchanged scene metadata, and unchanged original node IDs and indices.
Every original choice object remains identical at its previous index.
Only four existing texts change: `return/now`, `return/back`, `shared_night/close`, and `ending_loss/end`.
The added choices and nodes append to their respective arrays.

## Integration and remaining limits

Register the overlay after the original Tirabade scenes and expansion overlays, then invoke `integrate(payload)` once.
`SCENES` is empty and a duplicate-application guard rejects a second integration.
Register `TirabadeChronologyTests.Run` in the shared test entry point and rerun the combined rules and managed build checks.
The parent owns these shared edits.

After the overlay, the Tirabade inventory remains 59 scenes with 46,774 raw words and 46,467 distinct-segment words.
The 42,000-word aggregate planning floor remains satisfied; that is not a selected-playthrough requirement or proof of full RanRomance quality parity.
This patch adds 343 words net and does not address the assembled audit's individual-route, late native consequence, Trickster rescue, art, or physical-contact gaps.
No Unity rendering, installed-save continuation, or live ToyBox compatibility was exercised here.
No author approval score is assigned.
