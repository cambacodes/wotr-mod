# Arsinoe opening handoff

Status: unexported author contribution awaiting independent review and integration.
Owned files are `storylines/arsinoe_opening.py`, this handoff, and `reference/canon-review/arsinoe-route-evidence.md`.
No shared source, generated export, test file, installed asset, native blueprint, or other author's file was changed.
The unslop and ponytail instructions were applied.

Source SHA256: `F24DB10E401ED6C1B8969C5FC9FA9FC42A9F0394CAD141C06B51CD1CCDD23CFC`.
There are five scenes, 58 nodes, and 86 choices.
The project's measurement function reports 5,723 raw words, 5,661 distinct-segment words, 5,133 prose words, and 590 choice-label words.
These figures do not certify semantic uniqueness, quality, or a complete route.
Selected complete paths contain 3,096 to 3,600 words by the same tokenizer.
The single-character floor remains at least 21,000 meaningful words and full RanRomance depth, raised if the reference audit requires it.

## Story and choices

| Scene | Subject | Prerequisite | Completion |
|---|---|---|---|
| `arsinoe_city_on_paper` | Her purchase of a misleading city print starts a personal invitation. | Direct native contact, once integrated. | `arsinoe.picture_invitation` |
| `arsinoe_printers_view` | The printer offers two viable ways to correct his trade. | Picture invitation. | `arsinoe.printer_met` |
| `arsinoe_roofs` | Supper above the street develops her taste, travel history, calling, and interest. | Printer meeting. | `arsinoe.roof_shared` |
| `arsinoe_first_impression` | The business result is played, followed by a disagreement about what a picture should show. | Rooftop evening. | `arsinoe.first_impression_kept` |
| `arsinoe_hours_of_her_own` | The player chooses a reading evening or walk, with separate courtship, slow, and friendship conclusions. | First impression. | `arsinoe.opening_kept` |

The initial scene has no delay; later delays are 24, 48, 72, and 48 hours respectively.
The planned area is Drezen, Chapters 3 and 5.
All scenes use relationship `arsinoe`, owner `Arsinoe`, and the authored closure exclusion `arsinoe.closed`.
Other characters' introduction flags are not prerequisites.
Kiana and Konomi can remain optional introducers through their existing `arsinoe.introduced` flag, but the opening can be discovered directly at her own native conversation.
The module neither reads nor writes their romance states.

Keeping the corrected fantasy for sale preserves Tovin's paper budget and leads to three sales, a refused misleading title, and an unfinished original street drawing.
Waiting for original work yields a small printed street edition, a spoiled copy, and a shortage of paper money.
Arsinoe exchanges her own earlier purchase for the new view on that branch.
The Commander does not silently pay a fee, confiscate goods, or order an arrest.
These are authored civilian consequences, not implemented inventory or economy transactions.

The later composition disagreement preserves the printer's agency.
Adding a stall results in an actual alternative drawing, which Arsinoe prefers and Tovin does not promise to publish.
Keeping the open space lets him retain his choice and makes Arsinoe reconsider how demanding a customer she has become.
Neither alternative guarantees profit or wins affection.

Arsinoe initiates the rooftop evening and voices romantic interest herself.
The player chooses courtship, slower exploration, or friendship.
The last scene consumes that choice rather than forcing a kiss on every path.
The courtship path offers a kiss or handholding; slow and friendship paths lend the book without granting the kiss flag.
No commitment, marriage, exclusivity, native romance, or ToyBox setting is changed.
Existing spouses do not automatically exclude the candidate, but their consent is not inferred or invented.

## Native evidence and outstanding bindings

Read `reference/canon-review/arsinoe-route-evidence.md` for exact primary paths, identifiers, and attribution cautions.
It establishes a lawful-neutral adult female aasimar cleric of Abadar from Absalom, with a long traveling career and a prior home in the Stolen Lands.
It does not establish her exact age, present partner status, or universal mythic approval.

The module uses verified ContactUnit `a609ed9b2205d034bb3bb04d2a255681` and AnswerLists `ecaf5cfe8087a4f45a2269974f4885c9`.
The module-level `INTEGRATION_REQUIREMENTS` explicitly says `Implemented: False`.
It is a production handoff record, not an engine gate or substitute for native state.
Do not export this module merely because its Python graph imports.
Root still needs relationship registration, owner and portrait resolution, native actor availability, actual native dialogue suppression, and resumed-contact checks.
In particular, respect the Seelah Q3 VictimsRevived suppression and native combat/cutscene ownership.
The ordinary contact does not cover Threshold, DLC1, absent actors, or resurrection.

The Arueshalae dream objective supplies a natural optional rediscovery hook when the native question about Arsinoe's wishes has actually been asked.
The opening's city discussion is understandable without that quest and does not complete its objective.
Seelah Q2/Q3 and Lann's ceremony provide additional native contact opportunities, but they need actual outcome bindings and contextual writing before they may invoke the opening automatically.
Do not narrate returned souls, a living Elan, a completed marriage, or a friendly reaction to rejecting Lann from a generic introduction flag.
The current opening avoids asserting any of those histories.

For Trickster, a suitable continuation can build on the false city's engraving and Arsinoe's insistence on an honest description.
A possible fate intervention is a real, temporary opportunity to visit a once-possible version of the street, with Arsinoe choosing whether to investigate and returning with knowledge rather than an automatically completed city project.
This is a proposal, not an implemented scene, native fact, resurrection, or present access guarantee.
Lost contact must be restored through actual actor and quest conditions, preserving the original history.
Other mythics still need character-appropriate acceptance, disapproval, interruption, and refusal.
Swarm vendor service is explicitly insufficient evidence for courtship.
The current module is not safe for universal-mythic export without those restrictions.

## Check contract and verification

`arsinoe_city_on_paper/picture` contains a real `c(check=...)` contract for `SkillKnowledgeWorld`, DC 24, CommanderOnly true.
Success enters `recognized`, identifies tidal and architectural details, sets `arsinoe.print_source_found`, and unlocks a more specific confrontation at the printer's counter.
Failure enters `uncertain`, avoids inventing a confident identification, and leads to asking the printer for provenance.
The separate ask and listen choices provide non-roll approaches.
All approaches preserve the full courtship opportunity.
The DC is an authored balance choice for specialized visual interpretation in Chapters 3 and 5, not a DC found in native Arsinoe dialogue.
It needs play-balance review with actual Commander skill distributions and difficulty settings.
The failure is informational and changes the later exchange; it does not punish a build by removing the romance.

The source uses the established `story_format.c` check schema and an allowed `Story.CheckSkills` skill name.
No deterministic Next edge substitutes for the roll on that answer.
The live native roll, skill bonuses, success/failure display, party exclusion, retry behavior, and persistence were not executed by this author.
Those remain root integration verification.

An in-memory Python traversal using the project tokenizer explored all 21,504 complete paths and 8,873 initial deferral paths.
All 58 nodes were reached, both check results were followed, and every selected prerequisite and join had an available continuation.
Assertions verified exclusive business, courtship pace, and next-outing outcomes, plus the absence of a kiss flag outside courtship.
No late abort remained after choices had written progress.
Final import and entry-string checks passed after adding the verified contact metadata.
No persistent test file was added, and no C# or Unity test suite was run by this author.

Root verification should cover alive/present and absent/hidden/dead actors, combat, native dialogue suppression, Chapter 3/5 versus disallowed chapters, delays, closure, interrupted scenes, and resume after native quest changes.
Include other romances and ToyBox configurations in the actual state tests.
The source's additive `arsinoe.*` flags are not evidence by themselves that every shared-engine behavior preserves those states.

## Further content and art

This is an opening, not Arsinoe's whole campaign or a guaranteed review pass.
The next substantial arc should give the Commander something to bring to the relationship, pay off her request to learn their interests, and test her priestly priorities under a real campaign consequence.
The larger route still needs wedding and soul-rescue histories, mythic transitions, disagreement that does not disappear in one evening, developed intimacy, and conditional endings.
Optional relationships with another woman require independently developed mutual attraction; none is assumed here.

Art proposals are the native Arsinoe likeness examining the impossible city print, the rooftop supper with ordinary Drezen visible, and the final close conversation or kiss.
Keep the established aasimar identity and actual native appearance; the text does not prescribe invented wings, a new age, or a replacement body.
Tovin is an authored adult printer and needs visual separation from native named characters.
No art has been generated, reviewed, or installed.
The locations currently exist only as book narration, not added walkable areas, placed actors, or interactive props.
Independent writing, canon, art, and technical review remain required before claiming readiness.
