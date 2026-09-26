# Development verification, 2026-09-25

This is an incomplete expansion checkpoint, not release approval.
The installed addon has not been replaced.

## Revised scope and content-volume gate

The current delivery roster is 37 distinct characters in `ROSTER.md`, including full Ember and Aivu friendship arcs.
The user now requires bespoke attainable Trickster access, with character-appropriate restrictions on other mythic paths.
Earlier all-path tests do not establish this new per-character requirement.
Every resulting arc must meet or exceed a fully developed RanRomance route in meaningful amount and quality.
The planning floor is 21,000 meaningful words per resulting character pending the actual RanRomance benchmark audit, and must increase if that audit requires it.
The Anevia-Irabeth-Commander triad must be at least twice the single-character benchmark, currently 42,000 meaningful words combined, with independent development for both women.
The machine-readable inventory records the effective floor for each relationship group.

`development/content-volume-inventory.json` records a raw development-text count, including choices and repeated branches.
Using the RanRomance audit's tokenizer, it reports 18,722 raw words for the shared Tirabade story, 10,293 for Seelah, 12,894 for Konomi, 4,710 for Jerribeth, 3,927 for Kiana and 1,168 for Ember.
It also reports exact normalized-segment deduplication, separately from prose and choice totals.
These are neither deduplicated meaningful-word counts nor single-playthrough totals.
The reproducible command is `python tools/measure-story-content.py development/Story.json`.
Its focused `--self-test` checks formatting removal, duplicate segments, independent route totals and absence of unsupported external/playthrough credit.
The output records the exact story SHA256 and does not approve a route merely because its word count is large.
The shared Tirabade count cannot simply be credited in full to both women as independent character development.
Verified integrated native content will need separate attribution where it forms part of a resulting arc.
No current route has passed the new full-content benchmark or the complete expanded release gate.
Passage-level writing scores remain limited to the reviewed revision and scope.

## Current 128-scene checkpoint

The development export contains 36 Tirabade scenes, retaining the 34 original scene IDs with revisions, 28 Seelah scenes, 26 Konomi scenes, 18 Jerribeth scenes, 17 Kiana scenes and 3 Ember friendship scenes.
Production DLL SHA256: `C56AA055FDA979984A0140AFDEA822152C0323247D43D3765CB26F23E0C267B9`.
Development story SHA256: `979232347B58685064B708B4F251436E4ACFE9F779F535339D1CC7F1001BCCB1`.
The rules suite passes 66,503 assertions.
The actual-assembly construction and checkpoint-encoding check passes 9,038 assertions over 128 scenes and 3,163 generated blueprints in approximately nine seconds.
External binding verification resolves 192 uses to 54 correctly typed native blueprints.
New read-only selected-answer and completed-etude bindings distinguish Konomi's rank-six dismissal choice from the later completion of her officer state.
The native game records selected answers before their actions and dialogue finish actions, so the new invitation requires both facts and also forbids ordinary presence.
The managed check exercises the actual production dialog-history reader with native `DialogState` and `BlueprintAnswer` objects, testing absent, unrelated, selected and removed answers without mutating the input history.
This does not execute a native dismissal, verify a live save load or prove native etude transitions in Unity.
Alias validation rejects collisions with authored writes, other binding sources, generated timestamps and currently derived state names.
The independent [technical review](../reference/art-review/selected-answer-history-review.md) found no remaining blocker for the bounded readers and current invitation after the derived-alias correction.
`konomi.fate_post` is a remote, one-off authored Trickster invitation attempt, with different letters for prior lovers and other acquaintances.
It writes branch, invitation, scene-completion and normal relationship-journal progress; it does not restart the officer etude, erase dismissal, restore contact or grant affection.
The corrected scene received 91/100 bounded writing review at source SHA256 `CE3CB9B1A034E5C10BFAA63C9966B9F3D7E8210DCE39E53C1E0D915548E33C58`.
The reply and first private meeting now have authored book-event scenes; the continuing private route and any native actor restoration remain outstanding.
Focused tests walk new-acquaintance, existing-lover and committed histories through the invitation, reply and every first-meeting choice, including refusal, postponement, delays and preservation of native dismissal and prior commitments.
The reply and meeting preserve an already initiated correspondence after a switch from Trickster to Legend; only the original magical intervention requires active Trickster powers.
Konomi's stated intent to travel to Nerosyan is preserved through an explicit authored delay for a paid carrier negotiation, and her lodging remains temporary.
The corrected pair received 91/100 bounded writing review and a [canon/continuity review](../reference/canon-review/konomi-private-meeting-review.md) with no remaining material blocker at source SHA256 `79538CB7354B22F9B6714195F750FEBE29AC005F422ECFA5367F264B59088EC6`.
Final source SHA256 `389C4CC0EC5D9E228023284E650045E0E4F6204749BC0D7401FC7416CDF7814E` retains that prose and removes the continuing Trickster requirement from those two nonmagical scenes, with focused Legend-transition checks.
The private-meeting completion records an agreed channel for further personal visits; it does not reopen the official-office scenes or start a native appointment.
The separate [canon review](../reference/canon-review/konomi-fate-post-review.md) found no material blocker for the invitation's authored premise and preserved native history.
Konomi's new letter now has a delivered payoff with two readable invitations, an afternoon ring-toss outing and distinct prize and keepsake outcomes.
The tests continue from the eligible hearing aftermath through every invitation, throw and keepsake branch, including postponement, waiting time, prize ownership, winner-specific teasing and preservation of other relationships.
The outing is authored book-event narration, with no new vendor unit, native minigame, physical inventory item or game-clock advance claimed.
The corrected scene received 91/100 bounded writing review at source SHA256 `F539056D977956D44EACC9D341D45E9FE84C254D5A136C6B29C1B11C6CBA6692`.
The separate [canon review](../reference/canon-review/konomi-new-letter-review.md) confirmed the final staging fixes and found no remaining material issue within this scene's scope.
The new Konomi hearing and aftermath are authored book-event scenes, not new native quests, adjudicator units or changes to Mendev's game rules.
Focused tests traverse public, discreet and repaired-denial histories in Chapters 3 and 5, both evidence decisions and withdrawn permission before reading, then every available aftermath choice.
They verify distinct findings, privacy-history preservation, the repaired-denial callback, refusal, timing, contact requirements, closure and preservation of other relationships.
The next-morning transition inside the hearing is narration; it does not advance the actual game clock.
The independent [canon and continuity review](../reference/canon-review/konomi-hearing-review.md) found no remaining major blocker in these two scenes at source SHA256 `D8F3C575B06A1E88E0D90EEE7697FD67DF4261B2F732FA3FFCF0839DDE73613A`.
The corrected pair received 92/100 bounded writing review in `reviews/story.md` at the same source hash.
The hearing resolves one private complaint; it does not settle the threatened loss of household couriers or complete the full romance.
Konomi's ordinary meetings now require the native capital-presence etude to be Playing.
The focused rules check first reproduced availability without that state, then passed after the authored scene requirements were corrected.
The tests cover loss and return of contact, prevent a bare Trickster flag from substituting for an implemented recovery, and preserve the absent-character letter and endings.
This is an offline rules reproduction, not a Unity end-to-end reproduction of dismissal.
The native rank-6 dismissal and Swarm destruction differ from rank-8 council completion, which does not itself complete the officer's presence etude.
The new requirement does not implement the missing bespoke Trickster contact route.
The independent native evidence is recorded in [Konomi's availability audit](../reference/canon-review/konomi-availability-review.md).
The separate [technical review](../reference/art-review/konomi-presence-gate-review.md) found no blocker for this bounded scene-entry requirement.
It does not establish live etude transitions, interrupt an already open scene or restore missing contact.
The revised original quarrel preserves every pre-existing choice while appending reciprocal waiting preferences.
A direct comparison against installed Story.json preserved all 34 scene IDs, 162 node IDs and 230 existing choice dictionaries at their original indices.
This checks static compatibility, not an actual game-save round trip.
The revised `ordinary` scene received 92/100 bounded writing review at `story.py` SHA256 `5E8B5914C6CD47841C4CD4D899D90BBF06C14A948702E8BDBC46BE7EF91788F1`.
The new shared Tirabade lesson has focused checks for both teaching choices and outing plans, postponement, chapter limits, absent or dead partners and preservation of other romances.
Its corrected source received 92/100 bounded writing review at SHA256 `1C5E28E633165DCF684D2542C70BE69978FDE1B5C3F5C16991EEB9CCA0CEE26E`.
The following outing is walked from every lesson outcome, checking the selected activity, scheduling delay, optional dance and kiss, return choice and preservation of existing relationships.
The corrected outing received 92/100 bounded writing review at source SHA256 `B156DD2AC269B8C8B32CAE3354B01A51F276FA8DD483513364BC080E1CD647DE`.
Focused Seelah letter tests walk both incident outcomes and every available follow-up choice, checking delay, outcome separation, refusal, Chapter 4 limits, unavailable states and preservation of other relationships.
The city visit is staged in authored book-event text; these tests do not prove actor movement, native quest changes or in-game presentation.
The revised incident and discussion received 91/100 bounded writing review at source SHA256 `5311731A438A9451B12371A29E2BE0E2F37E9DAA6BE791415A1CBE1BA64D73C5`.
The subsequent copyist follow-up received 91/100 bounded writing review at source SHA256 `47CFAD1DBA6621CC99FCD6F4243B75BBC5F0BC3728C51289929BCE9674A881F3`.
Tests traverse the follow-up from every discussion outcome, verifying that only the previously agreed signal is offered, that Seelah can respond independently, and that declining the visit grants no completion credit.
The Kiana additions use two actual aftermath cue bindings and do not attach to her exhausted one-shot native dialogues.

Kiana progression covers 56 scenarios across ten named mythic states, both opening letter choices, and widow, waiting and secret-kiss histories.
The transformed variants omit the physical secret-kiss branch while retaining courtship and commitment through conversation.
Tests check native quest/meeting prerequisites, elapsed-time gates, marital consequences, Seelah's response, simultaneous existing commitments, and distinct endings.
These tests supply native outcome flags and available contact rather than executing the campaign that produces them.
Actual exceptional-path contact, interrupted soul rescue and restoration remain unverified and unfinished.
Kiana source portraits have been generated and independently reviewed, with v2 preferred after its headroom correction.
No Kiana portrait crops have been installed or verified in the running game.
The new optional stagecraft scene is included in each simulated Kiana campaign, with checks for its waiting period and suppression after completion.
It supplies a shared theatrical activity without granting romance or commitment flags.
The corrected stagecraft scene received 91/100 writing review at Kiana source SHA256 `124D98662BABE4417A66858C9D891F5FB02943CE6858E1C437F723DF7F395B45`.
This review covers the new scene, not the assembled full route.

Kiana source SHA256 `CD53586EDABF6603FB35979254C6832B3C6FA54884E53929F215B905D61C3836` received 91/100 bounded writing review.
The preceding source `20D0A82B016C16A148E166E543A6A1DDCA38781A15F6C806BB7028CB5294F633` received 96/100 bounded canon review before the seating and dialogue-transition corrections.
Neither score approves runtime contact, art, restoration or the complete expansion.

## Earlier 95-scene tested artifacts

- Production DLL SHA256: `BC52C0A972E43CA95BA18B82A9EA041D9EBD078E2E142A83503F37AF678A502E`.
- Development story SHA256: `3F7454F9BF351FDBA8A3E8EBA4F1DEA724C6C2BF3F544E3BF69E5964165E779A`.
- Content: 34 original scenes, 23 Seelah scenes, 20 Konomi scenes, and 18 Jerribeth scenes.

## Earlier 95-scene results

The production net48 project and managed test project built with zero warnings and errors.
The pure-rule suite passed 30,731 assertions, including Konomi, Seelah, and Jerribeth campaigns, named mythic-state branches, relationship independence, publicity, discretion, inhuman closeness, ending selection, and attempted-denial repair.
Seelah checks cover the alternative transformed opening, absence of physical-intimacy flags on inhuman progression, quest-locked aftermath, and mutually exclusive moderate/bad/incomplete endings.
These simulations supply an available Seelah contact and do not prove her restoration after native departure or death.
Jerribeth checks cover chapter 3/4/5 starts, met/unmet gates, topic knowledge, slower/private evenings, independent closures, patron loss, native unavailability, and ending selection.
They do not treat the native misleading affection marker as romance or consent.
Binding verification resolved 147 uses to 45 correctly typed game blueprints.
The separate actual-assembly test passed 5,877 assertions over 95 scenes and 2,076 generated blueprints.
The latest run completed in 8.60 seconds after the archive reader was changed to look up each extracted AssetId in a set.
It invoked production `Main.Build` and checked four native answer lists, the native Aeon sequence, a parent-epilogue preservation fixture, generated links, entry/choice guards, action ownership, terminal completion configuration, and idempotence.

These checks do not execute the parent mod's initialization, native etude conditions, scene actions against a real player, ToyBox, rendered portraits, or game-save persistence.
The parent-created normal epilogue sequence uses explicitly labeled sentinel references; the test does not claim those are the parent's full slide list.
The command and fixture details are in `../managed-tests/README.md`.

## Independent content review

Konomi source `8EA6E596C8CB500BE7B0930601699F06C0E3350255BFCC82E5874A4F80942CC0` received 95/100 bounded canon fidelity and 91/100 writing.
Seelah continuation source `A8D257D7E675B938EAC487025F465A93FDCB135610CA4ADFDC091B31CE19D625` received 96/100 bounded canon fidelity and 91/100 writing.
Jerribeth source `F607D73B030A2640A809081E53022938E62FF3FEBA4C66001BC485AC41FDD03B` received 96/100 bounded canon fidelity and 91/100 writing.
Seelah's evening illustration received 83/90 observable source-art criteria, with crop and runtime criteria unscored.
Jerribeth's true-form illustration received 69/75 observable source-art criteria against the installed custom reference and written native traits.
That score excludes canonical raster comparison, guise consistency, crops, and runtime presentation.
These are bounded content reviews and do not approve the complete expansion.

Jerribeth's correspondence reads actual native `ShownCues` history through typed preflighted bindings.
Seeing a meeting cue establishes contact only; individual topics use their own history checks.
The invented charm is a narrative correspondence device, not a claim that native telepathy has unrestricted range.
No code restores a dead Jerribeth or turns her native one-shot encounter into a repeatable conversation.

## Timing correction

A progression scenario reproduced a private invitation becoming available immediately after the courtship choice despite its 24-hour delay.
The production engine now registers persistent timestamp flags for authored choice effects and records the first activation time.
The corrected progression test passes, and actual construction checks confirm those timestamp blueprints exist.
Existing saves without historical choice timestamps retain the original timing fallback; the addon cannot reconstruct an unrecorded past choice time.
No real player or save round trip was used to test timestamp actions.
Completed-quest conditions do not acquire timestamps.
The soul-rescue aftermath's delay is measured from the prior relationship scene, so a long-established romance can open it immediately after the native rescue finishes.

## Remaining release work

Complete the remaining romance arcs, actual fate/contact restoration, all-path staging, portrait exports and scene mappings, installer/package changes, and final independent release review.
Maintain the existing installed build until that work is ready for the user's in-game test.

## Retained Seelah resurrection checkpoint

The development story now contains 97 scenes, including two initial Seelah fate scenes.
The recovery action calls the game's `ResurrectAndFullRestore` on exactly one retained fallen companion in `InParty` or `Remote` state.
It records authored progress only after the same entity is alive.
Dismissed companions, missing entities, quest repair and physical contact restoration remain unfinished.

The current source builds with zero warnings and errors.
Rules tests pass 30,778 assertions, including recovery readiness, unrelated absence and closure blockers, and ordinary dialogue remaining unavailable while dead.
These synthetic snapshots do not execute resurrection.
External binding verification resolves 151 uses to 46 correctly typed native blueprints.
Actual managed `Main.Build` construction passes 5,958 assertions for 97 scenes and 2,105 generated blueprints in approximately nine seconds.
The managed fixture checks the recovery unit's native type before seeding its blueprint.
It does not construct a saved companion or execute the recovery action in Unity.

DLL SHA256: `8BB2CE0C4B148FF36EF8F5A22E0D90A8E7C6D209FAC586E0100C4BBA6CB0EB94`.
Story SHA256: `C746612C04FB529A7126A1E35AA43216D934D868B168C3563601EF86F4325222`.
No installed release files were changed.

The reviewed recovery action additionally checks consciousness, saved UniqueId and unchanged companion roster state after resurrection.
The native action is not transactional.
The earlier implementation could leave a living unit without a recovery marker after a late exception.
The checkpoint mechanism below now handles verification and pending progress for that case.
The follow-up dialogue now separates the joke response from sincere reassurance and avoids assuming prior public conversations immediately after revival.

## Pending resurrection reconciliation

Before calling native resurrection, the addon stores a namespaced JSON string in the current player's native `SettingsList` dictionary.
The record includes the original unit identity, roster state, scene identity and exact serialized choice.
Only one retained player-faction companion in the player's `CrossSceneState` qualifies.
The production coordinator checks identity, roster, life and consciousness after the native action.
A living unit is never passed to resurrection again merely to recover missing addon progress.

After dialogue becomes idle, pending records are inspected against the actual current companion.
A restored companion receives the originally authorized scene effects, with existing flag timestamps preserved, before the checkpoint is removed.
Unavailable, changed-identity, changed-roster, still-dead and unconscious results retain their checkpoint and report why verification is pending.
An alive but unconscious partial result still requires actual consciousness recovery; the addon does not claim it is complete or arbitrarily clear conditions.
Recovery messages are scoped to the loaded player.

The runnable failure-injection test executes the production coordinator with a substitute native callback that revives and then throws.
It verifies no immediate credit, serialized checkpoint recovery, no repeated resurrection on a living unit, and rejection of wrong identity, changed roster, ineligible state and unconsciousness.
The actual-assembly check confirms `Player.SettingsList` carries the native `JsonProperty` attribute and that Newtonsoft JSON preserves the nested string checkpoint and its fields.
These are coordinator and encoding checks, not a native save round trip, actual `RecordProgress` fault injection, or resurrection in Unity.

Exact choice matching deliberately blocks automatic credit if a pending action's authored text or effects change between addon versions.
Such records remain intact and require an explicit migration before release updates can promise compatibility across that change.
Dismissed or missing companions, quest repair, physical contact and exceptional-path restoration remain unfinished.

## Ember opening checkpoint

Three Chapter 3 friendship scenes now connect ordinary shared activity, a visitor asking Ember for an answer she cannot give, and reciprocal interest in the Commander.
Both drawing choices and the intervention/listening branches reach the final callback with their state preserved.
Native presence, death, dismissal and temporary plot-absence markers gate these Drezen book events.
Temporary absence does not fail or close the friendship.
Later chapters, native quest-ending variations, actual restored contact and art remain unfinished.
The opening contains 1,168 raw words and is not a full-route delivery against the 21,000-word planning floor.
The checks do not execute these book events or native etude updates in Unity.

Ember source revision C7CCD90A592CD74C2F21860E849B20C902A9DDC5773484CFE3BA1ADF977E0BBF received 91/100 bounded writing review and 96/100 bounded canon review.
Those scores cover only the three opening scenes, not the full character arc or runtime integration.
