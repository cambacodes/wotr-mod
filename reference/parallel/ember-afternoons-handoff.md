# Ember afternoons author handoff

Source: `storylines/ember_afternoons.py`.
SHA256: `3271D913B8767C6C9F089AE1C671088EC1E744D42ED7C71D005B423946EA7D1E`.
The interrupted first scene was preserved, including its original node IDs, choice indices and branch flags.
An abort choice was appended to its opening.
Four connected scenes complete this contribution.
Ownership of both this handoff and the source is released to the parent for integration and independent review.

## Scope and quality status

This is a friendship contribution with five scenes, 53 nodes and 75 choices.
It has 5,279 raw words and 5,241 distinct text-field words under a markup-stripped word tokenizer.
A complete selected path through this contribution contains 3,452 to 3,568 words.
These figures describe this contribution alone, excluding the three existing opening scenes.
They do not establish the character's 21,000-word planning floor, full campaign depth or parity with RanRomance.
No review score is claimed or guaranteed.
Independent writing, characterization, art and integration review remain required, each targeting above 90 on the actual reviewed revision.
No export, registry, shared test, installation or artwork file was changed by this worker.

## Authored events and characterization

The contribution continues the player's actual chalk-bird choice from the existing opening.
General Manyboots and the Rain Inspector have different introductions.
The Commander chooses to perform the fox or narrate while Ember operates both figures.
That choice changes rehearsal, performance and private revision scenes.
Pella, Ilva and Nessa are newly authored adult civilians, not asserted native NPCs.
Pella lends her courtyard and cloth under specific conditions.
Her brother's delivery work temporarily takes the cloth away, as agreed before the loan.
Ember can be disappointed without interpreting the owner as unkind or requiring the Commander to seize another resource.
An overland staging preserves the original afternoon; waiting for the cloth requires Pella to notify guests and permits Nessa to attend on the new day.
The returned cloth's tear is a consequence of the brother's work, and Pella retains responsibility for deciding when to mend her own possession.

The play's fox returns stolen boots in both endings.
One ending emphasizes helping with luggage before the bird chooses to share food.
The other lets the fox ask for help only after returning the bird's property.
Ilva's particular objection responds to the selected ending, without casting her as a villain for disagreeing with Ember.
Her later gift of ribbon confirms that she enjoyed the performance while retaining her objection.
Ember works through her wish to give the fox a friend rather than receiving automatic praise or a Commander lecture that settles the matter.
The player proposes shared enjoyment through a bad song, or a separation followed by the bird voluntarily visiting the fox's gate.
The final scene performs that selected revision rather than summarizing an unseen successful rewrite.
The Commander can request more shared afternoons or ask that the next activity have no audience.
Neither choice closes the friendship or starts a romantic relationship.

Ember remains a childlike friendship character throughout.
There is no sexualization, age-up, romantic courtship, sacred revelation, native quest resolution, guaranteed redemption or new claim about her powers.
The puppets and the civilians are dialog descriptions only; this module does not spawn actors or inventory items.

## Integration and gating

Import this module's `SCENES` into the existing development authoring pipeline only after the parent accepts the contribution's review status.
The worker has not edited `expansion.py` or generated `development/Story.json`.
The module uses existing relationship `ember`, existing native alias `ember.present`, and existing portrait key `Ember`.
There are no new native GUID bindings.
Narrator nodes intentionally have no Ember portrait override; Ember nodes use `Ember`.
The settings are private courtyards in Drezen, delivered through the existing remote-rest conversation mechanism.
All five scenes require chapter 3 and Drezen area `2570015799edf594daf2f076f2f975d8`.
They forbid `ember.closed`, `ember_dead`, `ember_gone` and `ember.absent`.
The presence and unavailable predicates are inherited project contracts, not new proof of runtime actor safety.
They need the same parent runtime review as other Ember content.

| Scene | Additional prerequisite | Delay | Completion flag |
| --- | --- | --- | --- |
| `ember.paper_bird` | `ember.shared_afternoon` | 24 hours | `ember.puppet_project` |
| `ember.missing_cloth` | `ember.puppet_project` | 24 hours | `ember.puppet_rehearsed` |
| `ember.courtyard_play` | `ember.puppet_rehearsed` | 48 hours | `ember.puppet_performed` |
| `ember.after_applause` | `ember.puppet_performed` | 24 hours | `ember.puppet_revision` |
| `ember.second_ending` | `ember.puppet_revision` | 24 hours | `ember.puppet_afternoons_kept` |

Every scene has a no-mutation opening abort choice, allowing postponement.
The performance postponement asks for time before taking the player's place; it does not claim the performance already happened.
All scene IDs use the normal completion recording mechanism.
The module does not set `ember.trusted_friend` or claim full-route commitment.
It does not grant restored access, later-chapter progression or bespoke Trickster recovery.
Those remain necessary full-character work.

## Authored branch flags

| Mutually exclusive choices | Later use |
| --- | --- |
| `ember.player_fox`, `ember.player_narrates` | Rehearsal, public performance and private revision respect the selected role. |
| `ember.stage_road`, `ember.stage_waited` | Public staging and scheduling consequences differ. |
| `ember.play_restitution`, `ember.play_explanation` | Different performed endings, audience objections and revision callbacks. |
| `ember.play_company`, `ember.play_opinion` | The next conversation remembers whether the player offered company or a later opinion. |
| `ember.revision_laughter`, `ember.revision_distance` | The final scene performs either the song or the gate visit. |
| `ember.puppet_more`, `ember.puppet_quiet` | Final response and future continuation hooks differ. |

The progression flags are listed in the integration table above.
All effects are additions to the `ember.` authored namespace.
No other relationship, native quest, faction, companion or mythic state is written.
Existing ToyBox free-love and jealousy settings are neither read nor changed by this module.
That narrow implementation fact does not certify full runtime compatibility.

## Local branch verification

A read-only Python traversal imported the real existing `ember.py` opening and then this five-scene continuation with bytecode writes disabled.
The traversal began from `ember.present` while preserving `konomi.committed` and `seelah.committed` as unrelated relationship markers.
It followed actual eligible choices through all eight scenes, checked targets and cycle freedom, and rejected empty eligible-choice lists.
It reached every new node and choice, including all opening aborts.
There were 3,072 distinct final flag-and-length states and 2,749 abort traversals across the actual opening and continuation.
Every full terminal state retained the unrelated relationship markers and contained `ember.puppet_afternoons_kept`.
The six branch pairs in the table remained exclusive on every complete path.
Abort choices had no flag mutations.
The traversal checked the new scenes' chapter, area, remote, delay and unavailable declarations.
Source import passed Python parsing.

This worker did not run the shared C# rules walker, native binding verification, managed construction, Unity rendering, portrait display, ToyBox or real save/load tests.
Those parent checks and independent content reviews remain outstanding.
The branch walk is author verification, not independent approval.

## Parent integration after review

Final source SHA256: `A036B7D3B2E6B2D213F93D3F894D6C973AE5B393281686C3299878E466750822`.
Nessa now attends only the delayed sea performance, and common audience responses use people present on both schedules.
Shared rehearsal and ending passages preserve the selected fox operator.
The final fox joke no longer invents new boots on the restitution ending.
Independent writing and canon rereview scored this revision 91 in each discipline.
The five scenes are integrated into the 171-entry development export and covered by `tests/EmberAfternoonsTests.cs` through the actual original opening.
No full-character approval is implied.
