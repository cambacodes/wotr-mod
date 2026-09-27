# Targona's Trickster recovery route development

This report records a source-only development slice for a new missed-or-declined romance acquisition path.
The module is separate from the reviewed Targona continuation and does not modify parent romance state.
It is not integrated, independently reviewed, runtime tested, or ready for play.

## Canon evidence and authored alternate

The installed native blueprint identifies Targona as female and lawful good, depicts an adult celestial warrior, and gives no exact age.
Native dialogue establishes her liberation distress, a lasting change to her wing, her own judgment about Heaven, and the ability to contact celestial brethren on Golarion.
That contact line is not evidence of unrestricted communication with the Commander.
The parent RanRomance finale is a completed treatment quest plus one witnessed final cue, rather than merely opening its finale dialogue.
The nonromantic terminal cue GUIDs used here are `ad655c40be31401386b85287483b3841` and `cfc5f3cb2cf94672a96cab742e62225d`.
The latter is the Aeon or Trickster nonromantic branch involving Anograt.
The parent romance etude is `80cb9c6f466b4eaaaa9561ca56c5f348` and is read as a blocker, never changed.
Existing source research finds no proof of universal chapter-five physical presence for a Trickster Commander.
The authored contents therefore use the established correspondence channel and do not spawn or unhide Targona's Angel-gated Drezen actor.

The report's canon claims derive from `reference/canon-review/targona-route-evidence.md` and `targona-parent-bindings.json`.
The described contradictory courier report, waystation marker, runner, limited Trickster effect, and resulting courtship invitation are authored alternate events, not base-game quests or dialogue.
The old nonromantic ending remains intact, and Targona herself initiates the possible new meeting only after a separate task.
The Commander can decline at every relevant turn without losing the correspondence.
The skill check governs how much the Commander can infer from the documents, not Targona's interest or consent.
On a failed Perception check, the Commander may stop for the safe daylight inspection or recover by tracing the courier's route without claiming certainty, so the roll does not permanently close the invitation.
The no-roll route uses the same safe daylight inspection and does not gate the relationship behind a roll.

## Native and authored gates

The source module binds the existing freedom and transformation etudes, completed parent treatment quest, and the two nonromantic ending cues by their researched GUIDs.
It requires current Trickster status, an allowed pre-existing parent route history, the completed treatment, a nonromantic ending, and the first correspondence scene from `targona_opening.py`.
It blocks active parent romance, death, condemnation, incompatible transformed histories, and non-Trickster mythic status.
Requiring `targona.correspondence_opened` gives the branch an actual authored written contact channel rather than inventing telepathy or an unverified physical location.
The first letter is Targona's invitation to examine a separate report; refusal ends only the errand.
The side task cannot locate or summon a stranded person, transport a character, heal Targona, alter the old laboratory, or compel a response.
Its Trickster intervention makes one marker distinguish an actual touch from a repeated sound and expires after the test.
The result confirms there is no stranded person, avoiding an invented rescue used as a reward.

The source maps ten path-appropriate entry concepts in `PATH_ENTRY_PLANS` to keep the overall roster requirement visible.
Only the Trickster recovery branch is authored here.
Angel and Azata should build from their established service bonds and direct consent.
Aeon should use evidence-led judgment and preserve Anograt's separate voice.
Demon must make protection costly and preserve Targona's ability to reject the Commander.
Lich needs a verified non-necromantic refuge and informed consent, while refusing incompatible death or transformation histories.
Devil needs explicit revocable terms and no infernal coercion as courtship.
Legend needs a mortal future without falsely claiming wing restoration.
Gold Dragon needs source verification of her post-transformation body and a matching available actor.
Swarm requires a separately authored survival or escape intervention and must refuse acquisition after terminal identity loss or death.
These are design directions only and do not establish that all ten routes are attainable today.

## Current content and gaps

The module contains two manually selected letter scenes, an investigation check with a safe no-roll branch, refusal branches, and a new invitation initiated by Targona.
The second scene deliberately stops at a meeting invitation because there is no verified non-Angel physical actor or location for this history.
No date scene, in-person relationship arc, explicit romance progression, mature intimacy sequence, finale, epilogue, or outcome art is implemented here.
This is a small acquisition prototype, not a complete route.
The project hard standard of at least 21,000 meaningful route words and a complete, replayable arc remains unmet by this module.
No word-count parity with the installed route has been established.
The source must be imported and its `RELATIONSHIP`, native etude, quest, and cue declarations merged by an authorized integration owner.
The authored event flags in this source presently have no parent-module consumers.
In particular, `targona.trickster_acq.meeting_pending` needs a staged meeting producer before it can become a live progression flag.
The neutral `TargonaCorrespondence` portrait asset and actual book background still require installation checks and in-game rendering verification.

## Required review and verification

An independent canon reviewer should verify the premise against the installed script and assess whether each authored transition preserves Targona's voice and agency.
An independent narrative reviewer should assess pacing, character depth, Trickster mechanics, maturity, and whether the route reads like a game expansion rather than an imposed second chance.
A separate technical reviewer must inspect source graph reachability, native GUID resolution, mutual exclusion, flag consumers, content export, and save-state behavior.
The route needs suitable commissioned or generated art reviewed against Targona's game model and all outcome states.
After implementation, test both parent nonromantic terminal cues, allowed histories, each blocked history, check success, failure and route-tracing recovery, both safe exits, player refusal, and current-path changes.
Then verify export bindings and run the native mod in game, including manual letter delivery, correspondence timing, actor availability, and persistence across save/load.
No reviewer score or approval is claimed by the author.
