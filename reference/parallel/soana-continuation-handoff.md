# Soana continuation handoff

The new module is `storylines/soana_continuation.py`, SHA256 `5723D79D16A1B6B821CAF9B679EB19E2FDA8EF6AAF2584A01D396B43E1567EF8`.
The focused test file is `tests/SoanaContinuationTests.cs`, SHA256 `D1142E2E203181424060C740D24D16B8BBCDEF659750C01CC1868E0F65A87940`.
Both files are released for parent staging and independent review.
Only those files and this handoff were edited for this assignment.
No shared engine, export, existing source, native binding, portrait, or installation was changed.

## Integration

Append this module's `SCENES` after the existing Soana opening.
Register `SoanaContinuationTests.Run(story, Check)` when all six new scene IDs are present.
There is no overlay and no modification of existing scene IDs or choices.
All six scenes use the opening's real ContactUnit `64805abb52739e44280a758f850b300c` and native AnswersList `2b1776f3e398685479ff6b16290b4cc2`.
They remain optional physical Chapter 3 scenes, not remote scenes or new capital contacts.
Each requires `soana.after_quest`, `soana.opening_kept`, its immediate authored predecessor, and either `soana.old_defender` or `soana.bear_dead`.
All retain the native death, Camellia death, dead forest, authored closure, and inhuman exclusions.
All have a 24-hour minimum interval using their required predecessor's timestamp.
Every page has Portrait `Soana`.
The existing native-contact adapter and real Perception skill-check adapter should suffice for this bounded contribution.
Parent staging, bindings, rules, and managed construction checks remain necessary before promotion.

| Scene | Additional prerequisite | Continuing milestone |
| --- | --- | --- |
| `soana.one_account` | `soana.inquiry_invited` | `soana.proposal_kept` |
| `soana.watch_line` | `soana.proposal_kept` | `soana.watch_kept` |
| `soana.price_of_warning` | `soana.watch_kept` | `soana.warning_reckoned` |
| `soana.ordinary_feast` | `soana.warning_reckoned` | `soana.feast_kept` |
| `soana.name_between` | `soana.feast_kept` | `soana.present_named` |
| `soana.lower_bend` | `soana.present_named` | `soana.continuation_kept` |

## Played developments

The Commander returns with a written proposal for an ordinary cord-and-clapper warning.
Soana challenges its title as an account when no experiment has yet happened, corrects the design, and agrees to one limited trial.
The player can defer after admitting the proposal is not the proven method previously requested.
No unnamed expert, imported native manuscript, completed expedition, magic research result, or quest reward is invented.
The page and tools are authored book-scene props rather than implemented inventory items.

Her hostility toward mages remains a live disagreement.
The player may identify as a magic practitioner, directly challenge her old extermination advice, or keep this trial limited to its nonmagical method.
The self-identification is a player-selected statement, not a class check or automatic assertion about the Commander.
No path declares her prejudice cured, and the later scenes do not assume the argument happened in the deferred branch.

At the crossing, the pair assemble and test the warning, observe a false alarm from a branch, and investigate softer movement caused by a boar and a caught twig.
A Commander-only `SkillPerception` check at DC 22 supplies distinct success and failure pages.
The DC is an authored Chapter 3 difficulty for identifying small movement behind reeds before disturbing an animal, not a recovered native encounter DC.
Success observes the actual mechanism without disturbing the boar.
Failure startles it, misses the direct observation, and requires a longer physical test with the recovered twig.
The no-roll alternative patiently divides observation between the two characters, costs daylight, and sees the mechanism occur.
No roll purchases attraction, changes a native quest, grants experience or items, or decides whether she accepts romance.

The player chooses a higher line that misses smaller movement or a lower line used only during an attended daylight watch.
On the next visit, Soana reports the selected method's particular cost.
The raised line produces false alarms and misses a small food thief.
The daytime watch consumes time she needs for gathering and is silent when left unattended.
The pair then physically move it near the cave with an easy release, or take it down and keep the materials and written results.
A principled refusal of her continuing willingness to bind a guardian instead closes these private visits after removing the line.
The final walk recalls the actual disposition, including her unhooking the retained warning or putting away the unused wood.

Living-Orso and dead-bear conversations remain different throughout.
The former names his continuing suffering without claiming the experiment loosens his binding.
The latter confronts the practical absence and her desire for another guardian without inventing resurrection, replacement, or a spirit's consent.
BearDead takes precedence when both native outcome markers exist.
Her final concession is limited to examining a worthwhile method or refusing to pretend a new creature is the old friend returned.
No native outcome alias is written by the module.

The leisure visit uses sour berries, honey, a comic song, and her memories of an imperfect festival.
There are three distinct ways to join the song and two follow-up conversations.
The invented song and small recollections are authored additions, not claimed recovered lyrics.
Their enjoyment is allowed to coexist with disagreement and unfinished forest work.

The next visit makes the present marital uncertainty explicit before the first optional romantic touch.
Soana says Corven remains her husband, she does not know whether he lives, and they did not agree to release each other from their promises.
Those present-tense claims are authored alternate development built around a native marriage whose present status is unspecified.
They are not verified base-game facts, a claim that she is canonically widowed, or invented permission from Corven.
Her desire to explore courtship belongs to her, and the player can knowingly choose it, prefer friendship, wait, or end the visits.
The existing marriage therefore matters without automatically removing her from the candidate roster.

The final walk allows a first kiss only after the explicit courtship decision.
Holding hands and slow courtship remain separate alternatives.
Friendship gets a distinct warm answer and another walk without a kiss, and waiting remains unresolved rather than silently converting into romance.
A newly interested player need not have selected attraction in the opening, because the intervening visits develop the possibility.
No route gains lovers or commitment flags in this contribution.
No other partner is broken up with, penalized, or treated as exclusive.

## Native evidence and identity

The author reread `reference/canon-review/soana-route-evidence.md`, the opening source and handoff, `EXPANSION.md`, and `art/CHARACTER-DESIGN.md`.
The installed `blueprints.zip` and `Wrath_Data/StreamingAssets/Localization/enGB.json` were read directly for the following native cues under `World/Dialogs/c3/Wintersun/SoanaAfterQuest/`.

| Cue | Verified basis |
| --- | --- |
| `Cue_0004`, `27bbd303f3a1a9647965804b039f5c4d` | Her advice to eradicate mages and resentment of Sarkorian rulers. |
| `Cue_0010`, `04bf8499af8e3d84cbc75d07561b56e6` | The Sun Festival, communal singing, Meadow of the Spirits. |
| `Cue_0011`, `4e08e5915295f794bbd916138f033aaa` | Mead, bonfire jumping, Orso and summer flowers. |
| `Cue_0012`, `c6789b662ea5c404f957d9a20b68f5c7` | Wedding to Corven, children, spring, former authority. |
| `Cue_0019`, `2bee7561164fa8d4b947cb7a0202b287` | BearDead Playing gates her search for a suitable new spirit and animal. |
| `Cue_0020`, `7097513c578ec11449eb17e11fd3ce45` | NOT BearDead Playing gates the statement that Orso protects her. |

The established adult dwarf identity, long history, husband, children, forest priorities, and imperfect physical stamina remain intact.
The current art brief permits an appealing humanized visual interpretation with silver hair and blue markings.
It does not authorize rewriting chronology or making her another species.
This module adds no visual-aging requirement, rejuvenation event, mandatory transformation, or new portrait asset.

## Verification performed

The new source imports successfully without shared-file mutation.
A read-only source graph walk visited all 68 pages across living and dead bear histories without a missing target, dead end, or cycle.
It examined 7,574 terminal outcomes including postponements and closures.
The C# tests are delivered for parent execution and were not claimed as executed at author release.
They play the actual three-scene opening first for living, dead, and overlapping native outcomes, with both initial attraction and practical companionship.
They then traverse all continuing choices and both skill outcomes through all six new scenes.
They verify all-page coverage, clear relationship pace and final intimacy outcomes, native and unrelated history preservation, actual contact loss, fake contact-flag rejection, prerequisite loss, unavailable states, Chapter 3 restrictions, continuation after authored closure, and the exact 24-hour boundary.
They preserve deferred timestamps and confirm that resumed contact does not reapply entry delays.
The test deduplicates equivalent flag histories between visits to avoid repeating identical downstream states.

The source count is 7,530 words including all alternatives and 7,493 distinct text-segment words after stripping game markup with the local counter.
These measurements are provisional until the project's canonical inventory counter runs.
Full selected six-scene paths contain 4,114 to 4,567 words, depending on choices and native outcome.
Those path counts include only displayed node text and the chosen answer, not every answer shown in a menu.
The existing opening is separate content, previously measured at 4,250 distinct-segment words.
Even their approximate combined 11,743 words remain well below the 21,000-word full-route floor.
No self-review score, full-campaign pass, or readiness claim is assigned.

## Remaining requirements

Independent literary and canon review must assess the actual source, especially Soana's resistance, the authored marital uncertainty, and transitions between practical companionship and mutual interest.
The 24-hour intervals require multiple Chapter 3 returns and do not guarantee time before a player leaves for the Abyss.
Later access needs verified native contact or an implemented alternative; this module does not invent a Drezen encounter or loosen the chapter gate.
Bespoke Trickster recovery, native Orso reconciliation, her family beyond these memories, later marriage consequences, sustained courtship, commitment, interruptions across chapters, and endings remain unfinished.
Other mythic restrictions and path-transition behavior require the later campaign design.
The experiment itself is narrated book gameplay with a real skill check, not a placed world trap, inventory craft, persistent warning object, or changed forest AI.
Actual game checks must cover live actor eligibility, native answer-list entry, contact loss during a book, skill-roll presentation, save/resume, portrait crops, and coexistence with ToyBox Love Is Free and Jealousy Begone.
Headless checks cannot establish those presentation or runtime observations on their own.

## Review corrections before staging

The reviewer identified two definite joins and two assumptions about native conversation knowledge.
The hand-taking page now works whether the Commander previously accepted her hand or chose a slower afternoon.
Both configurations now actually test the bend toward the cave and the stream before the common account describes both listening limits.
The festival page introduces the spring and answering voices directly, since the native postquest etude does not prove that the Commander heard those optional memories.
Soana states her old advice about mages in the present scene before the player may challenge it.

The author reproduced interrupted replay at the source graph level before correcting it.
A partial high-line choice could previously reopen into the daylight choice, a partial cave-watch choice into removal, and a partial courtship decision into friendship.
The unrepaired graph produced three, one, and one contradictory terminal paths respectively in those representative replay cases.
These are book-flow reproductions, not observations from an actual Unity session.

Opposing-choice guards now preserve the selected warning configuration, disposition, relationship pace, and final intimacy outcome when an unfinished visit reopens.
An already recorded successful or failed observation has an explicit reentry choice instead of a fresh roll that could award the opposing result.
The patient approach remains selectable only when neither skill result has already been recorded.
No history is reset or overwritten.
Closure remains available during a resumed relationship discussion, so this guard does not force continued courtship.
Waiting remains waiting in this contribution; a later authored scene must provide any eventual reconsideration rather than using an interrupted replay as that feature.

The revised source check traversed all 68 pages, 184 distinct partial replays, and 9,082 terminal outcomes including those replays.
The focused C# suite now captures actual partial traversal states, removes the live contact, checks that continuation is blocked, restores contact, reopens the unfinished scene, and verifies mutually exclusive histories stay exclusive.
Independent literary and technical verdicts remain separate from these author checks.
