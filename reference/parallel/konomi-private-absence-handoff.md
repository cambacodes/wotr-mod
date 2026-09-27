# Konomi private absence and reunion handoff

Released for independent review on 2026-09-26.
Only the assigned source, focused test and this handoff were changed.
No shared export, engine, registration, installed mod or native asset was edited.
No author quality score, full-route parity or release approval is claimed.

Source SHA256: `0F8F758771E5087CA7AEFFFB234C81DB4318096C9558232C50BADAD3B1432D9B`.
Test SHA256: `D1973C27D5B71EBAA6ECB52C53650CE1922B4F7C0B436FEAEFBEDF5E039036C6`.

## Contribution and actual played choices

`private_absence` supplies a Chapter 4 scene for the already-dismissed private route after its actual departure and address.
A broken pouch fastening brings the address into the Commander's hands.
The player repairs it and chooses either to keep an undelivered account or to remember the concrete horse-and-sleeve moment from the existing private departure.
Each supports a distinct wish: being wanted without having to perform a task, or hearing what Konomi chose while they were apart.
Four terminal outcomes preserve those two choices without recording abandoned intermediate branches.
The account stays with the Commander.
No courier, impossible clerk, news delivery or Konomi response is fabricated in the Abyss.

The appended private reunion conversation can read that account or hear the remembered incident and respond to its selected concern.
Konomi can affirm that she wants company without pretending she will never need help.
She can also admit that she chose a reception and professional introductions instead of reserving every evening for possible news.
The Commander may admit an unfair wish to have been missed constantly; she does not offer to have been more miserable to reassure them.
Her ambitions and irritation survive the affectionate response.
The later kiss is offered and chosen, with a quiet conversation available instead.
Intimacy is adult and graphic and explicit.

Current Legend receives a specific response about giving up the power that first opened postal access.
Konomi acknowledges that power had uses she valued, then distinguishes their continuing practical arrangements from a vanished or unreliable magical door.
The invitation had the Commander's name and the answer was hers.
Neither Legend nor any other path receives a new Trickster flag or a restored council office.
The current Trickster reply also accepts that the missed days cannot simply be rewritten to improve the romance.
Other eligible embodied current histories retain a grounded invitation reply.

## Old letters and chronology repair

The earlier ordinary `unsent` letter has its own first presentation when it remains undiscussed.
Wonder and fear histories receive different replies; a legacy wrote flag without its detailed topic has a fallback.
The gardening question is recognized without claiming that the dismissed officer still occupies her old office.
These older-letter replies lead into present private work rather than inventing an earlier private exile during the Abyss.

The final predicates address a reproduced late-dismissal failure.
A player may finish the ordinary Chapter 5 return, then dismiss Konomi and earn the entire private departure/correspondence sequence afterward.
That history cannot receive a first presentation of the same old letter or imply that she was pursuing her private Nerosyan career during Chapter 4.
Completed ordinary return conservatively chooses a reply about having already spoken since coming home.
It does not falsely assert that the optional letter branch was selected, because ordinary return can finish through her own account instead.
The earlier wonder_answered and fear_answered flags also select this reply when an ordinary letter response was played but the enclosing return scene was interrupted.
The new Chapter 4 private_absence_kept record alone authorizes the retrospective private-reception discussion.
An old save without that record uses a present-focused discussion about visits and work after dismissal.

## Integration and save compatibility

Append SCENES from `storylines.konomi_private_absence`, then call `integrate(payload)` after the existing Konomi modules.
Register `KonomiPrivateAbsenceTests.Run` when `konomi.private_absence` exists.
The new module supplies two scenes with 30 pages and appends 21 pages to the existing private reunion.
The added partner-menu answers are appended after every existing answer.
Every original scene field, node field and existing choice prefix was independently compared with the pre-integration payload and preserved exactly.
The integrate function is idempotent.

The original reunion's three partner answers remain available and leave the new discussion for another visit.
The new entry says so explicitly.
Taking an appended reunion completion retains both `konomi.private_returned` and `konomi.reunion_kept`, which the existing later private career progression requires.
The absence and acknowledgement are not new prerequisites for the original romance.
Skipping both still permits the original lease-offer continuation.

`private_absence_catchup` is an explicit manual Chapter 5 conversation for older saves or deferred discussions.
It requires the already-earned private return and address, retains dismissal/completed-office restrictions, and excludes ordinary presence, inhuman state, closure and private parting.
It is absent from the automatic rest queue.
A completed new acknowledgement suppresses catch-up repetition.
An aborted catch-up writes no history.
Completed older future/farewell flags are not reset, and no retroactive Chapter 4 record is granted by catch-up.

The catch-up inherits the private route's unitless authored delivery.
Its scene describes a conversation arranged during one of her visits; the existing flags establish the authored private return, not a verified current live NPC or the timing of every later visit.
It does not manufacture a new ContactUnit or prove that a native unit is currently in Drezen.
A late manual catch-up can be offered while private_returned remains historical, so confirming an actual current visit and handling external state changes during a running book remain runtime/integration limitations.
This contribution does not claim to solve physical contact or cancel a unitless book immediately when an external mod changes a native state.

## Measured length

The standard project tokenizer measures 7,456 raw words across all new scene text, appended text and added entry answers.
After deduplicating repeated exact prose/answer segments shared by the reunion and catch-up delivery contexts, the contribution is 4,364 distinct words.
The duplicated delivery copy must not be counted as two new player encounters.

For the four new Chapter 4 outcomes followed by their appended reunion answer, exhaustive source walks measure 1,475-1,654 selected new words on current Trickster and 1,517-1,696 on current Legend.
Each range has 16 compatible completed paths and includes the chosen added entry answer.
These counts exclude the original reunion prefix, which belongs to existing content, and include only one selected absence/reunion branch.
A manual Legend catch-up without a kept account adds 859-986 selected words.
An older undiscussed fear letter adds 979-984; an older wonder letter adds 965-970; an already-played ordinary return adds 835-840.
Those are alternative histories, not additive requirements.

Konomi's previously measured aggregate exceeded the 21,000-word planning floor before this addition.
This module contributes act continuity and reactivity; its raw or distinct total does not certify full RanRomance selected-route length, breadth or quality parity.
The later private career consequence and pre-final-battle farewell identified as the next readiness priority remain separate work.

## Verification performed

Temporary isolated runner: `C:/Users/Z/AppData/Local/Temp/konomi-private-absence-check-hgxc9iu_/Check.csproj`.
The adjacent Story.json contains the candidate assembled from the existing development export plus this module.
The runner executes actual shared Rules.Validate and Program.Walk helpers against the candidate.
Final result: 285,327 focused assertions passed.

The suite plays fresh dismissed and established dismissed private acquisition, history repair when needed, carriers, the pre-road evening and departure before entering Chapter 4.
It traverses all four absence outcomes, original letter outcomes, legacy letter detail omissions, all three current-path responses, original reunion deferral and manual catch-up.
It verifies every new/appended page, protection of native and other-romance state, no mythic regrant, no intermediate new-scene flags or timestamps, all new scene gates and preservation of the original career continuation.
The new acknowledgement is never set on an unfinished reply page.
Existing earlier reunion choices retain their own original intermediate behavior; that behavior was not silently rewritten.

The late-dismissal reproduction separately plays ordinary margin through reckoning, Chapter 4 unsent and Chapter 5 return before changing the native fixture to dismissed/completed office.
It then plays the actual private acquisition, history repair, departure, letters and return offer, and switches from earned Trickster access to current Legend.
The test verifies departure occurs after the original return timestamp and that both reunion and manual catch-up use the present-focused response without repeating first delivery or earlier private exile.
Additional fixtures cover partially answered ordinary letters without a completed return flag.

Independent writing/canon review and combined schema, binding and managed build checks are still required before promotion.
Native game/save, UI, portrait and ToyBox coexistence were not exercised by this source-level work.
