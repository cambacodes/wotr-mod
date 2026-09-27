# Tirabade morale branch engineering review

Reviewed on 2026-09-26.
Initial verdict: revision required for an existing assembled answer identity regression.
This review covers branching and tests, not the new prose's literary or canon quality.

## Initial snapshot

| Input | SHA256 |
| --- | --- |
| `storylines/tirabade_chronology.py` | 842E5FBBC1E6ADD8ABB4650BCF88E92E5D2ABE0A89DD754FD114818F346DAABC |
| `tests/TirabadeChronologyTests.cs` | 59FE83D64D4AC1FB9F4A4FF134E92E42586FDC43F7E7951FB875EBF872CA3B78 |
| Isolated candidate Story.json | 44DA475F4482E88DEC93DBB82D5667A331084328C7640FBED2AA2B291D66589D |

The isolated candidate is `C:/Users/Z/AppData/Local/Temp/tirabade-morale-cv_ph8v0/Story.json`.
The comparison export is the shared 585-scene file with SHA256 `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A`.
Root produced the candidate while keeping unrelated in-progress late-module edits out of the assembly.
I did not regenerate the shared export or edit source files.

## Required correction

The initial `return/now` assembled choice sequence changes from `future, back, back_negotiated` to `future, back, morale, back_negotiated`.
The new chronology append runs before the later independent bridge appends its existing negotiated answer.
Consequently `back_negotiated` moves from index 2 to index 3, and index 2 now identifies a different answer.
The native answer GUID scheme uses the index, so preserving only the original two base-route choices is insufficient.
I reproduced the two sequences directly from the frozen candidate and shared export.

The current test checks indices 0 and 1 only and therefore misses this regression.
Append morale after the already assembled negotiated answer and assert the complete previously exported prefix.
No other ordering defect was found in the initial changed scenes.

## Checks that passed

The `last_watch/start` and `last_watch/after` original choice prefixes retain their original positions and data except the intended added Broken prohibition on the life answer.
The alternate is a deep copy, so its added requirement does not mutate the original requirement list.
The original gets `Forbids: broken`; the alternate gets `Requires: broken` and points to `life_broken`.
With no morale flag or Encouraged alone, the available life response is `life`.
With Broken alone or both Broken and Encouraged, it is `life_broken`.
I independently enumerated these four states for both incoming pages from the actual candidate.
The alternate then rejoins `end`, which retains the existing last_words effect and scene completion.

The optional reunion morale question requires Broken and leads through `morale` to the existing future page.
No new branch writes either native morale flag.
I inspected every choice Set in the two changed scenes as well as the construction diff.
These branches observe morale rather than inventing recovery or clearing a native state.

The added tests use the actual Rules.Match-based traversal and include the adversarial state with both flags present.
Collecting every reachable page across every answer would catch either life page being reachable in the wrong state, including a missing prohibition on the original answer.
The tests also require a completed final watch and preserve the two unrelated romance flags.
Those checks test behavior rather than simply repeating the source's guard lists.
The old-base-prefix assertion is the material coverage gap identified above.

## Boundaries

The existing scene walker explores JSON graphs and applies authored Set effects to snapshots.
It does not run Unity dialogue, establish live etude observation, or inspect the rendered choice list.
Its visit callback reports reachable nodes, not a live saved conversation resumed halfway through a page.
This engineering review cannot certify the literary consistency of already-open pages if native morale changes during an in-progress conversation.
The game's actual condition evaluation and saved dialogue resumption remain live verification boundaries.

## Corrected ordering review

Final scoped verdict: pass after the separate morale integration stage preserves the existing assembled answer prefix.
The initial defect and reproduction above remain part of the review record.

| Corrected input | SHA256 |
| --- | --- |
| `expansion.py` | 6E8D16BEF2C151F16C651D0D36583F22CA3FAB305967D4014B8EB88225B26393 |
| `storylines/tirabade_chronology.py` | F3ACB49FA8B7F46C815CDFC805D06AFFFD919B387ADE23C08D772FE11220865E |
| `tests/TirabadeChronologyTests.cs` | B8984F11139805870C12116B05DC8739175049C39E04C608DD8B5D1CAFDBF3F9 |
| Corrected isolated candidate | 1DD0CDE6C952ADAAF50CD676C33848014AFD36B5E54E4EECE7693E86780A988F |

The corrected candidate is `C:/Users/Z/AppData/Local/Temp/tirabade-morale-fixed-g9omrnz0/Story.json`.
The new `integrate_morale` call follows the optional independent bridge block and runs in either assembly mode.
The old chronology stage retains its previous position.
In the full assembled candidate, return/now now has `future, back, back_negotiated, morale`.
The new test explicitly checks negotiated index 2 and morale index 3 when the negotiated route exists.
I evaluated that assertion against both actual candidates: the initial candidate fails and the corrected candidate passes.

I compared every preexisting choice at its original index across all 585 scenes against the shared comparison export.
There are no changes to Next, Check, Set or Abort at any original choice position.
The only other existing choice differences are the two intended Broken prohibitions and the two progression labels covered by the separate literary review.
This checks the actual assembled output rather than assuming that appending within one module preserves ordering after other integrations.

The corrected last_watch object is identical to the initially inspected candidate.
I repeated the four-state paired-guard probe against the corrected file and confirmed Broken priority without contradictory life destinations.
Root reported its full Rules run on this corrected candidate exited zero with 25,958,725 assertions.
I did not duplicate that full run; my independent checks were the complete existing-choice comparison, old-versus-fixed regression probe and corrected four-state guard probe.
No shared output, source or test file was changed by this review.
